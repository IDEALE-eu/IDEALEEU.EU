import { useEffect, useState } from 'react'
import type { DigitalPassport, FilterState } from '@/types'
import { passportKV } from '@/lib/kv'
import { seedPassports } from '@/data/seed'

function App() {
  const [passports, setPassports] = useState<DigitalPassport[]>([])
  const [filters, setFilters] = useState<FilterState>({
    search: '',
    domain: 'all',
    phase: 'all',
    state: 'all',
    status: 'all',
  })
  const [view, setView] = useState<'dashboard' | 'templates'>('dashboard')

  // Initialize data on mount
  useEffect(() => {
    // Check if we have data
    const keys = passportKV.keys()
    
    if (keys.length === 0) {
      // Initialize with seed data
      seedPassports.forEach(passport => {
        passportKV.set(passport.id, passport)
      })
    }

    // Load all passports
    loadPassports()
  }, [])

  const loadPassports = () => {
    const keys = passportKV.keys()
    const loaded = keys
      .map(key => passportKV.get<DigitalPassport>(key))
      .filter((p): p is DigitalPassport => p !== null)
    setPassports(loaded)
  }

  // Filter passports
  const filteredPassports = passports.filter(passport => {
    if (filters.search && !passport.title.toLowerCase().includes(filters.search.toLowerCase()) && 
        !passport.utcs_ref.toLowerCase().includes(filters.search.toLowerCase())) {
      return false
    }
    if (filters.domain !== 'all' && passport.domain !== filters.domain) return false
    if (filters.phase !== 'all' && passport.phase !== filters.phase) return false
    if (filters.state !== 'all' && passport.state !== filters.state) return false
    if (filters.status !== 'all' && passport.verification_status !== filters.status) return false
    return true
  })

  // Calculate statistics
  const stats = {
    total: passports.length,
    verified: passports.filter(p => p.verification_status === 'verified').length,
    pending: passports.filter(p => p.verification_status === 'pending').length,
    qs_anchored: passports.filter(p => p.qs_anchored).length,
  }

  return (
    <div className="min-h-screen bg-white">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-[oklch(0.35_0.12_250)] text-white shadow-md">
        <div className="max-w-7xl mx-auto px-8 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-[32px] font-bold tracking-[-0.02em]">
                Aerospace Digital Passports
              </h1>
              <p className="text-sm opacity-90 mt-1">
                UTCS Manifest Viewer & Lifecycle Tracker
              </p>
            </div>
            <div className="flex items-center gap-6">
              <button
                onClick={() => setView('dashboard')}
                className={`px-4 py-2 rounded transition-colors ${
                  view === 'dashboard'
                    ? 'bg-white text-[oklch(0.35_0.12_250)]'
                    : 'bg-[oklch(0.45_0.12_250)] hover:bg-[oklch(0.40_0.12_250)]'
                }`}
              >
                Dashboard
              </button>
              <button
                onClick={() => setView('templates')}
                className={`px-4 py-2 rounded transition-colors ${
                  view === 'templates'
                    ? 'bg-white text-[oklch(0.35_0.12_250)]'
                    : 'bg-[oklch(0.45_0.12_250)] hover:bg-[oklch(0.40_0.12_250)]'
                }`}
              >
                Templates Library
              </button>
            </div>
          </div>
          
          {/* Statistics */}
          {view === 'dashboard' && (
            <div className="flex gap-6 mt-4 text-sm">
              <div>
                <span className="opacity-75">Total:</span>{' '}
                <span className="font-semibold">{stats.total}</span>
              </div>
              <div>
                <span className="opacity-75">Verified:</span>{' '}
                <span className="font-semibold">{stats.verified}</span>
              </div>
              <div>
                <span className="opacity-75">Pending:</span>{' '}
                <span className="font-semibold">{stats.pending}</span>
              </div>
              <div>
                <span className="opacity-75">QS Anchored:</span>{' '}
                <span className="font-semibold">{stats.qs_anchored}</span>
              </div>
            </div>
          )}
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-8 py-6">
        {view === 'dashboard' ? (
          <>
            {/* Filter Panel */}
            <div className="bg-[oklch(0.96_0.01_260)] rounded-lg p-6 mb-8">
              <h2 className="text-[18px] font-semibold mb-4">Filters</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
                <div>
                  <label className="block text-sm font-medium mb-2">Search</label>
                  <input
                    type="text"
                    placeholder="Title or UTCS ref..."
                    value={filters.search}
                    onChange={(e) => setFilters({ ...filters, search: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-[oklch(0.35_0.12_250)]"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-2">Domain</label>
                  <select
                    value={filters.domain}
                    onChange={(e) => setFilters({ ...filters, domain: e.target.value as any })}
                    className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-[oklch(0.35_0.12_250)]"
                  >
                    <option value="all">All Domains</option>
                    <option value="AAA">AAA - Airframes</option>
                    <option value="PPP">PPP - Propulsion</option>
                    <option value="EDI">EDI - Electronics</option>
                    <option value="IIS">IIS - Information</option>
                    <option value="EEE">EEE - Electrical</option>
                    <option value="CQH">CQH - Cryogenics</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium mb-2">Phase</label>
                  <select
                    value={filters.phase}
                    onChange={(e) => setFilters({ ...filters, phase: e.target.value as any })}
                    className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-[oklch(0.35_0.12_250)]"
                  >
                    <option value="all">All Phases</option>
                    <option value="CAD">CAD - Design</option>
                    <option value="CAE">CAE - Analysis</option>
                    <option value="CAM">CAM - Manufacturing</option>
                    <option value="CAV">CAV - Validation</option>
                    <option value="CMP">CMP - Compliance</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium mb-2">Status</label>
                  <select
                    value={filters.status}
                    onChange={(e) => setFilters({ ...filters, status: e.target.value as any })}
                    className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-[oklch(0.35_0.12_250)]"
                  >
                    <option value="all">All Status</option>
                    <option value="verified">Verified</option>
                    <option value="pending">Pending</option>
                    <option value="drift">Drift</option>
                    <option value="failed">Failed</option>
                  </select>
                </div>
                <div className="flex items-end">
                  <button
                    onClick={() => setFilters({
                      search: '',
                      domain: 'all',
                      phase: 'all',
                      state: 'all',
                      status: 'all',
                    })}
                    className="w-full px-4 py-2 bg-[oklch(0.55_0.01_260)] text-white rounded hover:bg-[oklch(0.50_0.01_260)] transition-colors"
                  >
                    Reset
                  </button>
                </div>
              </div>
            </div>

            {/* Passport Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredPassports.length === 0 ? (
                <div className="col-span-full text-center py-12">
                  <p className="text-[oklch(0.55_0.01_260)] text-lg">
                    No passports match your filters
                  </p>
                </div>
              ) : (
                filteredPassports.map((passport) => (
                  <div
                    key={passport.id}
                    className="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-md transition-shadow"
                    style={{ borderLeftWidth: '4px', borderLeftColor: `oklch(0.55 0.15 250)` }}
                  >
                    <div className="flex items-start justify-between mb-3">
                      <span
                        className="px-2 py-1 rounded text-xs font-medium text-white"
                        style={{ backgroundColor: `oklch(0.55 0.15 250)` }}
                      >
                        {passport.domain}
                      </span>
                      <span
                        className="px-2 py-1 rounded text-xs font-medium"
                        style={{
                          backgroundColor: passport.verification_status === 'verified' 
                            ? 'oklch(0.85 0.08 145)' 
                            : 'oklch(0.90 0.08 95)',
                          color: passport.verification_status === 'verified'
                            ? 'oklch(0.30 0.15 145)'
                            : 'oklch(0.40 0.14 95)',
                        }}
                      >
                        {passport.verification_status.toUpperCase()}
                      </span>
                    </div>
                    
                    <h3 className="font-semibold text-[18px] mb-2">{passport.title}</h3>
                    
                    <div className="text-sm space-y-1 mb-4">
                      <div className="flex justify-between">
                        <span className="text-[oklch(0.55_0.01_260)]">UTCS Ref:</span>
                        <span className="font-mono text-[13px]">{passport.utcs_ref}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-[oklch(0.55_0.01_260)]">Phase:</span>
                        <span className="font-medium">{passport.phase}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-[oklch(0.55_0.01_260)]">State:</span>
                        <span className="font-medium">{passport.state}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-[oklch(0.55_0.01_260)]">Progress:</span>
                        <span className="font-medium">{passport.lifecycle_progress}%</span>
                      </div>
                    </div>

                    <div className="flex gap-2 text-xs">
                      {passport.qs_anchored && (
                        <span className="px-2 py-1 bg-[oklch(0.90_0.08_300)] text-[oklch(0.35_0.15_300)] rounded">
                          QS ✓
                        </span>
                      )}
                      {passport.cb_anchored && (
                        <span className="px-2 py-1 bg-[oklch(0.85_0.08_145)] text-[oklch(0.30_0.15_145)] rounded">
                          CB ✓
                        </span>
                      )}
                    </div>
                  </div>
                ))
              )}
            </div>
          </>
        ) : (
          <div className="text-center py-12">
            <h2 className="text-2xl font-semibold mb-4">Templates Library</h2>
            <p className="text-[oklch(0.55_0.01_260)]">
              Templates library will be implemented in the next phase
            </p>
          </div>
        )}
      </main>
    </div>
  )
}

export default App
