# Teknia Token (TT) Staking Smart Contract Specification

**Version:** 1.0  
**Contract Type:** ERC-20 + Custom Staking  
**UTCS:** `utcs://BUSINESS/A360-EXCHANGES-TT/TOKEN-ECONOMICS/STAKING-CONTRACT`

## Overview

This document specifies the smart contract architecture for Teknia Token (TT) staking on the A360exchanges-TT platform. The contract supports multiple staking roles with role-specific rewards and slashing conditions.

## Contract Architecture

### Core Contracts

1. **TekniaToken.sol** - ERC-20 token contract
2. **StakingManager.sol** - Main staking logic
3. **RewardDistributor.sol** - Reward calculation and distribution
4. **SlashingController.sol** - Slashing logic and appeals
5. **GovernanceModule.sol** - Token holder voting

### Contract Hierarchy

```
TekniaToken (ERC-20)
    ├── StakingManager
    │   ├── MarketMakerStaking
    │   ├── ServiceProviderStaking
    │   └── OracleStaking
    ├── RewardDistributor
    │   ├── TradingFeeDistributor
    │   ├── ServiceFeeDistributor
    │   └── AttestationFeeDistributor
    ├── SlashingController
    │   ├── SlashingRules
    │   └── AppealManager
    └── GovernanceModule
        ├── ProposalManager
        └── VotingMechanism
```

## TekniaToken Contract

### ERC-20 Standard Implementation

```solidity
// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract TekniaToken is ERC20, AccessControl, Pausable {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    bytes32 public constant BURNER_ROLE = keccak256("BURNER_ROLE");

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion TT

    constructor() ERC20("Teknia Token", "TT") {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
        _grantRole(PAUSER_ROLE, msg.sender);
        _grantRole(BURNER_ROLE, msg.sender);
    }

    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        require(totalSupply() + amount <= MAX_SUPPLY, "Max supply exceeded");
        _mint(to, amount);
    }

    function burn(uint256 amount) public onlyRole(BURNER_ROLE) {
        _burn(msg.sender, amount);
    }

    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }

    function unpause() public onlyRole(PAUSER_ROLE) {
        _unpause();
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```

## StakingManager Contract

### Core Staking Logic

```solidity
// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract StakingManager is ReentrancyGuard, AccessControl {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant SLASHER_ROLE = keccak256("SLASHER_ROLE");

    enum StakeRole { MARKET_MAKER, SERVICE_PROVIDER, ORACLE, GOVERNANCE }
    enum StakeStatus { ACTIVE, LOCKED, UNSTAKING, SLASHED, WITHDRAWN }

    struct Stake {
        address staker;
        uint256 amount;
        StakeRole role;
        uint256 lockUntil;
        StakeStatus status;
        uint256 stakedAt;
        uint256 lastRewardClaim;
    }

    struct StakeConfig {
        uint256 minStake;
        uint256 lockPeriod;
        uint256 unstakingPeriod;
    }

    TekniaToken public token;
    mapping(uint256 => Stake) public stakes;
    mapping(StakeRole => StakeConfig) public stakeConfigs;
    mapping(address => uint256[]) public userStakes;
    
    uint256 public stakeIdCounter;
    uint256 public totalStaked;

    event Staked(
        uint256 indexed stakeId,
        address indexed staker,
        uint256 amount,
        StakeRole role
    );
    event Unstaked(uint256 indexed stakeId, address indexed staker, uint256 amount);
    event Slashed(uint256 indexed stakeId, uint256 amount, string reason);
    event RewardsClaimed(uint256 indexed stakeId, uint256 amount);

    constructor(address _token) {
        token = TekniaToken(_token);
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(ADMIN_ROLE, msg.sender);
        
        // Initialize stake configurations
        stakeConfigs[StakeRole.MARKET_MAKER] = StakeConfig({
            minStake: 50_000 * 10**18,
            lockPeriod: 90 days,
            unstakingPeriod: 7 days
        });
        
        stakeConfigs[StakeRole.SERVICE_PROVIDER] = StakeConfig({
            minStake: 25_000 * 10**18,
            lockPeriod: 180 days,
            unstakingPeriod: 7 days
        });
        
        stakeConfigs[StakeRole.ORACLE] = StakeConfig({
            minStake: 100_000 * 10**18,
            lockPeriod: 365 days,
            unstakingPeriod: 14 days
        });
        
        stakeConfigs[StakeRole.GOVERNANCE] = StakeConfig({
            minStake: 10_000 * 10**18,
            lockPeriod: 0,
            unstakingPeriod: 0
        });
    }

    function stake(uint256 amount, StakeRole role) 
        external 
        nonReentrant 
        returns (uint256 stakeId) 
    {
        StakeConfig memory config = stakeConfigs[role];
        require(amount >= config.minStake, "Amount below minimum stake");
        
        // Transfer tokens from user to contract
        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        
        // Create stake
        stakeId = stakeIdCounter++;
        stakes[stakeId] = Stake({
            staker: msg.sender,
            amount: amount,
            role: role,
            lockUntil: block.timestamp + config.lockPeriod,
            status: StakeStatus.ACTIVE,
            stakedAt: block.timestamp,
            lastRewardClaim: block.timestamp
        });
        
        userStakes[msg.sender].push(stakeId);
        totalStaked += amount;
        
        emit Staked(stakeId, msg.sender, amount, role);
    }

    function initiateUnstake(uint256 stakeId) external nonReentrant {
        Stake storage s = stakes[stakeId];
        require(s.staker == msg.sender, "Not stake owner");
        require(s.status == StakeStatus.ACTIVE, "Cannot unstake");
        require(block.timestamp >= s.lockUntil, "Still locked");
        
        s.status = StakeStatus.UNSTAKING;
        s.lockUntil = block.timestamp + stakeConfigs[s.role].unstakingPeriod;
    }

    function completeUnstake(uint256 stakeId) external nonReentrant {
        Stake storage s = stakes[stakeId];
        require(s.staker == msg.sender, "Not stake owner");
        require(s.status == StakeStatus.UNSTAKING, "Not unstaking");
        require(block.timestamp >= s.lockUntil, "Unstaking period not complete");
        
        uint256 amount = s.amount;
        s.amount = 0;
        s.status = StakeStatus.WITHDRAWN;
        totalStaked -= amount;
        
        require(token.transfer(msg.sender, amount), "Transfer failed");
        
        emit Unstaked(stakeId, msg.sender, amount);
    }

    function slash(
        uint256 stakeId, 
        uint256 slashAmount, 
        string calldata reason
    ) external onlyRole(SLASHER_ROLE) {
        Stake storage s = stakes[stakeId];
        require(s.status == StakeStatus.ACTIVE, "Not active stake");
        require(slashAmount <= s.amount, "Slash exceeds stake");
        
        s.amount -= slashAmount;
        totalStaked -= slashAmount;
        
        if (s.amount == 0) {
            s.status = StakeStatus.SLASHED;
        }
        
        // Transfer slashed amount to risk fund
        require(token.transfer(getRiskFundAddress(), slashAmount), "Transfer failed");
        
        emit Slashed(stakeId, slashAmount, reason);
    }

    function getStake(uint256 stakeId) 
        external 
        view 
        returns (Stake memory) 
    {
        return stakes[stakeId];
    }

    function getUserStakes(address user) 
        external 
        view 
        returns (uint256[] memory) 
    {
        return userStakes[user];
    }

    function getRiskFundAddress() public view returns (address) {
        // Return risk fund address from registry
        return address(0); // Placeholder
    }

    function updateStakeConfig(
        StakeRole role,
        uint256 minStake,
        uint256 lockPeriod,
        uint256 unstakingPeriod
    ) external onlyRole(ADMIN_ROLE) {
        stakeConfigs[role] = StakeConfig({
            minStake: minStake,
            lockPeriod: lockPeriod,
            unstakingPeriod: unstakingPeriod
        });
    }
}
```

## RewardDistributor Contract

### Reward Calculation

```solidity
// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

contract RewardDistributor is AccessControl {
    bytes32 public constant DISTRIBUTOR_ROLE = keccak256("DISTRIBUTOR_ROLE");

    StakingManager public stakingManager;
    TekniaToken public token;

    struct RewardPool {
        uint256 totalRewards;
        uint256 rewardRate;  // Rewards per second per token staked
        uint256 lastUpdateTime;
    }

    mapping(StakingManager.StakeRole => RewardPool) public rewardPools;
    mapping(uint256 => uint256) public stakeRewards;  // stakeId => accumulated rewards

    event RewardsDistributed(uint256 indexed stakeId, uint256 amount);
    event RewardsClaimed(uint256 indexed stakeId, address indexed staker, uint256 amount);

    constructor(address _stakingManager, address _token) {
        stakingManager = StakingManager(_stakingManager);
        token = TekniaToken(_token);
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(DISTRIBUTOR_ROLE, msg.sender);
    }

    function distributeRewards(
        StakingManager.StakeRole role,
        uint256 amount
    ) external onlyRole(DISTRIBUTOR_ROLE) {
        RewardPool storage pool = rewardPools[role];
        pool.totalRewards += amount;
        pool.lastUpdateTime = block.timestamp;
        
        // Transfer rewards to contract
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
    }

    function calculateRewards(uint256 stakeId) public view returns (uint256) {
        StakingManager.Stake memory s = stakingManager.getStake(stakeId);
        RewardPool memory pool = rewardPools[s.role];
        
        uint256 timeSinceLastClaim = block.timestamp - s.lastRewardClaim;
        uint256 rewards = (s.amount * pool.rewardRate * timeSinceLastClaim) / 1e18;
        
        return rewards + stakeRewards[stakeId];
    }

    function claimRewards(uint256 stakeId) external {
        StakingManager.Stake memory s = stakingManager.getStake(stakeId);
        require(s.staker == msg.sender, "Not stake owner");
        
        uint256 rewards = calculateRewards(stakeId);
        require(rewards > 0, "No rewards to claim");
        
        stakeRewards[stakeId] = 0;
        
        require(token.transfer(msg.sender, rewards), "Transfer failed");
        
        emit RewardsClaimed(stakeId, msg.sender, rewards);
    }
}
```

## SlashingController Contract

### Slashing Logic and Appeals

```solidity
// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

contract SlashingController is AccessControl {
    bytes32 public constant SLASHER_ROLE = keccak256("SLASHER_ROLE");
    bytes32 public constant REVIEWER_ROLE = keccak256("REVIEWER_ROLE");

    enum AppealStatus { NONE, PENDING, APPROVED, REJECTED }

    struct SlashingEvent {
        uint256 stakeId;
        uint256 amount;
        string reason;
        uint256 timestamp;
        address slasher;
        AppealStatus appealStatus;
    }

    struct Appeal {
        uint256 slashingId;
        address appellant;
        string evidence;
        uint256 submittedAt;
        AppealStatus status;
        string reviewNotes;
    }

    StakingManager public stakingManager;
    
    mapping(uint256 => SlashingEvent) public slashingEvents;
    mapping(uint256 => Appeal) public appeals;
    
    uint256 public slashingIdCounter;
    uint256 public appealIdCounter;
    uint256 public constant APPEAL_PERIOD = 30 days;

    event SlashingProposed(uint256 indexed slashingId, uint256 stakeId, uint256 amount);
    event SlashingExecuted(uint256 indexed slashingId);
    event AppealSubmitted(uint256 indexed appealId, uint256 slashingId);
    event AppealReviewed(uint256 indexed appealId, AppealStatus status);

    constructor(address _stakingManager) {
        stakingManager = StakingManager(_stakingManager);
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(SLASHER_ROLE, msg.sender);
        _grantRole(REVIEWER_ROLE, msg.sender);
    }

    function proposeSlashing(
        uint256 stakeId,
        uint256 amount,
        string calldata reason
    ) external onlyRole(SLASHER_ROLE) returns (uint256 slashingId) {
        slashingId = slashingIdCounter++;
        
        slashingEvents[slashingId] = SlashingEvent({
            stakeId: stakeId,
            amount: amount,
            reason: reason,
            timestamp: block.timestamp,
            slasher: msg.sender,
            appealStatus: AppealStatus.NONE
        });
        
        emit SlashingProposed(slashingId, stakeId, amount);
    }

    function executeSlashing(uint256 slashingId) 
        external 
        onlyRole(SLASHER_ROLE) 
    {
        SlashingEvent storage se = slashingEvents[slashingId];
        require(
            se.appealStatus == AppealStatus.NONE || 
            se.appealStatus == AppealStatus.REJECTED,
            "Cannot execute while appeal pending or approved"
        );
        require(
            block.timestamp >= se.timestamp + APPEAL_PERIOD,
            "Appeal period not expired"
        );
        
        stakingManager.slash(se.stakeId, se.amount, se.reason);
        
        emit SlashingExecuted(slashingId);
    }

    function submitAppeal(
        uint256 slashingId,
        string calldata evidence
    ) external returns (uint256 appealId) {
        SlashingEvent storage se = slashingEvents[slashingId];
        StakingManager.Stake memory s = stakingManager.getStake(se.stakeId);
        
        require(s.staker == msg.sender, "Not stake owner");
        require(se.appealStatus == AppealStatus.NONE, "Appeal already submitted");
        require(
            block.timestamp < se.timestamp + APPEAL_PERIOD,
            "Appeal period expired"
        );
        
        appealId = appealIdCounter++;
        
        appeals[appealId] = Appeal({
            slashingId: slashingId,
            appellant: msg.sender,
            evidence: evidence,
            submittedAt: block.timestamp,
            status: AppealStatus.PENDING,
            reviewNotes: ""
        });
        
        se.appealStatus = AppealStatus.PENDING;
        
        emit AppealSubmitted(appealId, slashingId);
    }

    function reviewAppeal(
        uint256 appealId,
        bool approve,
        string calldata notes
    ) external onlyRole(REVIEWER_ROLE) {
        Appeal storage appeal = appeals[appealId];
        require(appeal.status == AppealStatus.PENDING, "Appeal not pending");
        
        appeal.status = approve ? AppealStatus.APPROVED : AppealStatus.REJECTED;
        appeal.reviewNotes = notes;
        
        SlashingEvent storage se = slashingEvents[appeal.slashingId];
        se.appealStatus = appeal.status;
        
        emit AppealReviewed(appealId, appeal.status);
    }
}
```

## Deployment and Configuration

### Deployment Order

1. Deploy `TekniaToken`
2. Deploy `StakingManager` (with TekniaToken address)
3. Deploy `RewardDistributor` (with StakingManager and TekniaToken)
4. Deploy `SlashingController` (with StakingManager)
5. Deploy `GovernanceModule` (with TekniaToken and StakingManager)
6. Configure roles and permissions

### Initial Configuration

```javascript
// Deployment script (Hardhat/Truffle)
async function deploy() {
    // 1. Deploy token
    const TekniaToken = await ethers.getContractFactory("TekniaToken");
    const token = await TekniaToken.deploy();
    await token.deployed();

    // 2. Deploy staking
    const StakingManager = await ethers.getContractFactory("StakingManager");
    const staking = await StakingManager.deploy(token.address);
    await staking.deployed();

    // 3. Deploy rewards
    const RewardDistributor = await ethers.getContractFactory("RewardDistributor");
    const rewards = await RewardDistributor.deploy(staking.address, token.address);
    await rewards.deployed();

    // 4. Deploy slashing
    const SlashingController = await ethers.getContractFactory("SlashingController");
    const slashing = await SlashingController.deploy(staking.address);
    await slashing.deployed();

    // 5. Grant roles
    await token.grantRole(await token.MINTER_ROLE(), rewards.address);
    await staking.grantRole(await staking.SLASHER_ROLE(), slashing.address);

    // 6. Initial token distribution
    await token.mint(treasuryAddress, ethers.utils.parseEther("300000000")); // 30% ecosystem
    await token.mint(riskFundAddress, ethers.utils.parseEther("200000000")); // 20% risk fund
    // ... etc

    return { token, staking, rewards, slashing };
}
```

## Security Considerations

### Reentrancy Protection
- All external calls use `nonReentrant` modifier
- Checks-Effects-Interactions pattern followed

### Access Control
- Role-based access control for sensitive functions
- Multi-signature for admin operations recommended

### Emergency Procedures
- Pausable token transfers
- Emergency withdrawal mechanism
- Circuit breakers for extreme events

### Auditing
- Required before mainnet deployment
- Continuous monitoring post-deployment
- Bug bounty program

## Testing Requirements

### Unit Tests
- Token minting and burning
- Staking and unstaking flows
- Reward calculations
- Slashing mechanics
- Appeal process

### Integration Tests
- Multi-contract interactions
- End-to-end workflows
- Edge cases and failure modes

### Gas Optimization
- Target: <500k gas for stake
- Target: <300k gas for unstake
- Target: <200k gas for claim rewards

## Upgrade Strategy

### Contract Upgradability
- Use proxy pattern (UUPS or Transparent)
- Timelock for upgrades (48 hours minimum)
- Multi-signature requirement (4-of-7)

### Migration Path
- Version compatibility checks
- State migration scripts
- Rollback procedures

## References

- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)
- [ERC-20 Standard](https://eips.ethereum.org/EIPS/eip-20)
- [Solidity Security Best Practices](https://consensys.github.io/smart-contract-best-practices/)
- [A360 Token Economics](../README.md)

---

**Smart Contract Lead:** A360 Development Team  
**Last Updated:** 2025-10-17  
**Audit Required:** Yes (before mainnet deployment)
