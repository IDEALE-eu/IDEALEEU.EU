# TFA Structure Management Makefile
# ===================================
# This Makefile helps create and manage the TFA directory structure
# and artifacts for the AMPEL360-AIR-T aircraft model.

# VARIABLES (override with make VAR=value)
DOMAIN ?= XXX
ATA_CHAPTER ?= ATA-XX
ATA_MID ?= ATA-XX-YY
COMP ?= ATA-XX-YY-ZZ
EFFECT ?= 0001-9999
SUBPROD_ID ?= SUBPROD_001
SUBJECT_ID ?= SUBJ_001
ITEM_DESC ?= example-item
OWNER ?= Engineering

# Base paths
PRODUCT = AMPEL360-AIR-T
ARCH = BWB-H2-Hy-E
FAMILY = Q100_STD01
BASE_PATH = $(PRODUCT)/ARCH/$(ARCH)/FAMILY/$(FAMILY)

# Computed paths
ROOT = $(BASE_PATH)/DOMAIN/$(DOMAIN)/$(ATA_CHAPTER)/SYSTEMS/$(ATA_MID)
PLM = $(ROOT)/PLM/CAx
CONF = $(BASE_PATH)/CONF/BASELINE/COMPONENTS/$(COMP)

# Colors for output
COLOR_RESET = \033[0m
COLOR_GREEN = \033[32m
COLOR_BLUE = \033[34m
COLOR_YELLOW = \033[33m

.PHONY: help init add-item validate clean list-structure

# Default target
help:
	@echo "$(COLOR_BLUE)TFA Structure Management$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_GREEN)Available targets:$(COLOR_RESET)"
	@echo "  make init              - Initialize PLM/CAx directory structure"
	@echo "  make add-item          - Add a new item/artifact"
	@echo "  make validate          - Validate structure integrity"
	@echo "  make list-structure    - List current structure"
	@echo "  make clean             - Remove generated files"
	@echo ""
	@echo "$(COLOR_GREEN)Variables (set with make VAR=value):$(COLOR_RESET)"
	@echo "  DOMAIN       - Domain ID (default: $(DOMAIN))"
	@echo "  ATA_CHAPTER  - ATA chapter (default: $(ATA_CHAPTER))"
	@echo "  ATA_MID      - System ID (default: $(ATA_MID))"
	@echo "  COMP         - Component ID (default: $(COMP))"
	@echo "  EFFECT       - Effectivity range (default: $(EFFECT))"
	@echo "  SUBPROD_ID   - Subproduct ID (default: $(SUBPROD_ID))"
	@echo "  SUBJECT_ID   - Subject ID (default: $(SUBJECT_ID))"
	@echo "  ITEM_DESC    - Item description (default: $(ITEM_DESC))"
	@echo "  OWNER        - Owner/responsible (default: $(OWNER))"
	@echo ""
	@echo "$(COLOR_YELLOW)Example usage:$(COLOR_RESET)"
	@echo "  make init DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS ATA_CHAPTER=ATA-53 ATA_MID=ATA-53-10"
	@echo "  make add-item DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS ATA_CHAPTER=ATA-53 ATA_MID=ATA-53-10 \\"
	@echo "                COMP=ATA-53-10-01 SUBPROD_ID=SUBPROD_001 SUBJECT_ID=SUBJ_001 \\"
	@echo "                ITEM_DESC=design-spec OWNER=StructuralTeam"

# Initialize PLM directory structure
init:
	@echo "$(COLOR_BLUE)Initializing PLM/CAx structure...$(COLOR_RESET)"
	@mkdir -p "$(PLM)/CAD"
	@mkdir -p "$(PLM)/CAE"
	@mkdir -p "$(PLM)/CAM"
	@mkdir -p "$(PLM)/CAI"
	@mkdir -p "$(PLM)/CAO"
	@mkdir -p "$(PLM)/CAP"
	@mkdir -p "$(PLM)/CAS"
	@mkdir -p "$(PLM)/CAV"
	@mkdir -p "$(PLM)/CMP"
	@echo "$(COLOR_GREEN)✓ PLM structure created at: $(PLM)$(COLOR_RESET)"
	@mkdir -p "$(CONF)"
	@echo "$(COLOR_GREEN)✓ CONF structure created at: $(CONF)$(COLOR_RESET)"

# Add a new item/artifact
add-item:
	@echo "$(COLOR_BLUE)Adding new item...$(COLOR_RESET)"
	@if [ ! -f "./scripts/add_item.sh" ]; then \
		echo "$(COLOR_YELLOW)⚠ Script not found: ./scripts/add_item.sh$(COLOR_RESET)"; \
		exit 1; \
	fi
	@chmod +x ./scripts/add_item.sh
	@./scripts/add_item.sh "$(DOMAIN)" "$(ATA_CHAPTER)" "$(ATA_MID)" "$(COMP)" \
		"$(EFFECT)" "$(SUBPROD_ID)" "$(SUBJECT_ID)" "$(ITEM_DESC)" "$(OWNER)"
	@echo "$(COLOR_GREEN)✓ Item added successfully$(COLOR_RESET)"

# Validate structure
validate:
	@echo "$(COLOR_BLUE)Validating TFA structure...$(COLOR_RESET)"
	@if [ ! -f "./tools/validate_tree.py" ]; then \
		echo "$(COLOR_YELLOW)⚠ Validator not found: ./tools/validate_tree.py$(COLOR_RESET)"; \
		echo "$(COLOR_YELLOW)  Run 'make help' for setup instructions$(COLOR_RESET)"; \
		exit 1; \
	fi
	@python3 ./tools/validate_tree.py --domain "$(DOMAIN)" --ata-chapter "$(ATA_CHAPTER)" \
		--ata-mid "$(ATA_MID)" --comp "$(COMP)"

# List current structure
list-structure:
	@echo "$(COLOR_BLUE)Current TFA Structure:$(COLOR_RESET)"
	@if [ -d "$(ROOT)" ]; then \
		tree -L 4 "$(ROOT)" 2>/dev/null || ls -R "$(ROOT)"; \
	else \
		echo "$(COLOR_YELLOW)⚠ Structure not found at: $(ROOT)$(COLOR_RESET)"; \
		echo "  Run 'make init' first"; \
	fi

# Clean generated files
clean:
	@echo "$(COLOR_YELLOW)⚠ This will remove validation logs and temporary files$(COLOR_RESET)"
	@read -p "Continue? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		rm -f validation_report.txt; \
		find . -name "*.pyc" -delete; \
		find . -name "__pycache__" -type d -delete; \
		echo "$(COLOR_GREEN)✓ Cleaned$(COLOR_RESET)"; \
	fi

# Install dependencies (if needed)
install-deps:
	@echo "$(COLOR_BLUE)Checking dependencies...$(COLOR_RESET)"
	@which python3 > /dev/null || (echo "$(COLOR_YELLOW)⚠ Python3 not found$(COLOR_RESET)" && exit 1)
	@echo "$(COLOR_GREEN)✓ Python3 found$(COLOR_RESET)"
	@which tree > /dev/null || echo "$(COLOR_YELLOW)⚠ tree command not found (optional)$(COLOR_RESET)"
	@echo "$(COLOR_GREEN)✓ Dependencies OK$(COLOR_RESET)"
