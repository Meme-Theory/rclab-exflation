---
gate: S19A-FALSE-VACUUM-ANALYSIS
session_registered: S81
pre_s34_status: EXEMPT from canonical_constants import mandate
                 (S19a is S19; project rule: scripts S33 and below
                  are exempt; pattern applied as hygiene)
trigger: [VERIFY]  # reproducibility audit of pre-canonical diagnostic
classification: GEOMETRIC
 # Spectral-geometry diagnostic of Jensen-deformed D_K.
 # Not PHONONIC (no GGE excitation dynamics), not PARTICLE (no
 # representation-theoretic content), not NON-PHONONIC (it directly
 # concerns the fabric's spectral structure).
runner: Workhorse-Transit-Dynamics
date: 2026-04-17
---

# Prep: S19A-FALSE-VACUUM-ANALYSIS

## Origin & Scope

Script: `computations/session-19/s19a_false_vacuum_analysis.py`  (origin S19a, 2026-02-15)
Author (original): Tesla-Resonance
Copy:  `computations/_shared/t3-intake/s19a_false_vacuum_analysis.py`

**Pre-S34 exemption:** Per project CLAUDE.md, scripts S33 and below are
exempt from the `from canonical_constants import *` mandate. S19a is deep
pre-S34. No canonical-constants violations exist. pattern applied as
hygiene only: the script has NO framework constants to import; all literals
are topological (d_s = 4, 8), finite-difference steps (d_log_sigma = 0.01),
or local reference baselines (S_ref = 8, gap_ref = gaps[0], E_ref = vac[0]).

## Hypothesis Under Test

**Not a pass/fail gate.** Diagnostic-class. The script establishes whether
the Jensen-deformed D_K spectrum develops a "spectral desert" regime at
large tau, as conjectured from the observation that d_s > 8 (topological
dimension) beyond tau ~ 1.0. The outputs are structural inputs to the S19d
closed mechanism "Spectral back-reaction" (session-40 working paper).

## Pre-Registered Outputs (diagnostic)

| Quantity        | Interpretation                                 |
|:----------------|:-----------------------------------------------|
| `rate_gap`      | Exponential growth rate of spectral gap in tau |
| `rate_vac`      | Exponential growth rate of <lambda^2> in tau   |
| `d_s_min`       | Minimum of spectral dimension at sigma = 1     |
| `tau_at_ds_min` | tau where d_s is minimized                     |
| `H_boundary`    | tau at which habitability H(tau) = 0.5         |

None of these have a pre-registered PASS/FAIL threshold. The re-run
verifies REPRODUCIBILITY against the original script.

## Machinery Pins (PRDR)

| Parameter        | Pin                                          |
|:-----------------|:---------------------------------------------|
| `max_pq_sum`     | 6  (fixed by sweep_data generator)           |
| `tau_grid`       | linspace(0.0, 2.0, 21)                       |
| `d_log_sigma`    | 0.01 (centered finite-difference)            |
| `sigma_star`     | 1.0 (habitability reference)                 |
| `beta_star`      | 1.0 (habitability reference)                 |
| `sigma_grid`     | logspace(-1, 1.5, 40)                        |
| `GPU path`       | CPU-only (numpy heat-kernel sum, no BLAS)    |
| `random_seed`    | N/A (deterministic)                          |
| `scheme`         | PW-weighted spectral heat kernel             |
| `convention`     | d_log_sigma = 0.01 centered FD               |
| `L_max`          | max_pq_sum = 6                               |

## Inputs & SHA-256 Pins (64-char hex)

| Input                              | SHA-256                                                                 |
|:-----------------------------------|:------------------------------------------------------------------------|
| script (migrated)                  | `3f4706e403267bf1159d4543695f4f448bc69ac3ad5abafe1e52ba00640e21ed`      |
| script (original, archive)         | `3b6e61301a1b7d80f19f9dc6889f49c0b8bd14b94eb92264f3627d94e79e0a60`      |
| `s19a_sweep_data.py`               | `b7dfacaa0e9bfd7b403cc985ffc9e2be796eea6090adbb02db865bc5cc044529`      |
| `s19a_sweep_data.npz`  (757 KB)    | `ad2a0da375f516aa24430db6630c733300428fa9682b0986a70b9b766aec1f5a`      |
| `canonical_constants.py` (unmod)   | `68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f`      |

**Closure SHA-256** (JSON-sorted input-pin map of {script, sweep_data_py,
sweep_data_npz}):
`95eeb4619abeaabc9d5c120b51da7aeabdab2a978358498ed3289a959665f68a`

## Expected Output 4-Tuple

```
value={rate_vac:1.613531,rate_gap:0.730475,d_s_min:6.3091,tau_at_ds_min:0.900}
scheme=PW-weighted-spectral-heat-kernel
convention=d_log_sigma=0.01_centered_finite_difference
L_max=max_pq=6
```

## Substitution Chains

Two direction claims appear in the script's output. Chains:

### [SIGN] "Vacuum energy grows exponentially"
- Def: `rate_vac = slope of polyfit(tau, log(<lambda^2>), 1)`
- Sub: `numpy.polyfit(tau_values, np.log(vac['mean_lambda_sq']), 1)[0]`
- Simplify: scalar = 1.613531
- Direction: `rate_vac > 0`  =>  monotonic exponential growth
- Verified: `rate_vac = 1.613531` reproduced via independent polyfit
  (match to 6 decimals).

### [SIGN] "d_s exceeds topological dimension 8 at large tau"
- Def: `d_s(tau, sigma) = -2 * d_log K / d_log sigma`, `K = Sum_n mult_n * exp(-sigma * lam_n^2)`
- Sub: centered finite difference with `d_log_sigma = 0.01`
- Simplify: `d_s_surface[i,j]` computed on (tau, sigma) grid
- Direction: at sigma = 1, d_s minimum = 6.31 at tau = 0.9; rises past 8
  by tau ~ 1.1 (see "d_s > 8 onset: tau ~ 1.0-1.2" in console output)
- Verified: d_s boundary crossings at sigma = 0.438 -> tau = 1.909 and
  sigma = 0.915 -> tau = 1.467; consistent with monotonic rise after min.

### [CITED] "V_eff is monotonically decreasing"
- Source: Session 18 closure (V_eff monotonicity proof).
- Not computed in this script; cited only.
- No substitution chain needed here — chain lives in Session 18 artifacts.

## Cross-Checks Before Verdict

1. **Closure SHA independently recomputed** (hand-constructed JSON blob
   with 3 input pins): matches script emission byte-for-byte.
2. **rate_vac independently fit** via `numpy.polyfit`: 1.613531 (exact).
3. **Sector transition in spectral gap**: (0,1) -> (0,0) -> (1,0) as
   expected from Jensen eigenvalue reshuffling.

## PASS / FAIL / INFO Interpretation

- No pre-registered threshold. Verdict class is **INFO** by construction.
- Reproducibility class: **EXACT-MATCH** (script output matches S19a
  archival claims to 6 decimals; closure SHA is deterministic).

## Downstream Impact Flag

**FLAGGED — results feed downstream, but unchanged by re-run.**

| Downstream artifact | What it uses | Status |
|:--------------------|:-------------|:-------|
| s63_fermionic_qtheory.py | `N_F_S19 = 439488`, `N_B_S19 = 52556` (PW counts from sweep data, not from this analysis) | UNCHANGED (deterministic from max_pq_sum = 6) |
| session-40-results-workingpaper.md | "Spectral back-reaction" CLOSED MECHANISM cites rate_vac, rate_gap, d_s_min | UNCHANGED |
| session-73b-results-workingpaper.md | "modulus stabilization requires BCS dressing or instanton back-reaction (kappa < 1 opens at tau = 0.48)" | UNCHANGED (cites structure, not numerics) |
| Sibling S19a scripts | Share sweep_data.npz independently | No cross-coupling |

No canonical constant, gate verdict, or closed mechanism is affected by
this re-run.

## Boundary Mapping (what this diagnostic establishes)

PASS (structurally): This diagnostic ESTABLISHED the structural walls
that became the S19d "Spectral back-reaction" closure:
  - Physical-regime upper boundary at tau ~ 1.0 (d_s > 8 onset)
  - Habitability cliff at tau ~ 0.96 (H -> 0 exponentially above)
  - Super-linear vacuum-energy cost (rate_vac = 1.614 >> rate_gap = 0.730)

FAIL (what it does NOT constrain):
  - Does not, by itself, CLOSE modulus stabilization (S19d does that)
  - Does not provide the kappa < 1 opening at tau = 0.48 (that's S73b)
  - Does not compute the F_spectral(tau) force (that's the NEXT STEP
    noted in the script itself — addressed by S19d/S40)

## Command to Reproduce

```bash
# From project root:
cd computations/_shared/t3-intake
"C:/sandbox/Ainulindale Exflation/phonon-exflation-sim/.venv312/Scripts/python.exe" s19a_false_vacuum_analysis.py
```

Required files in `t3-intake/`:
- `s19a_false_vacuum_analysis.py`  (migrated)
- `s19a_sweep_data.py`                (copied from archive)
- `s19a_sweep_data.npz`               (copied from archive)

The script also needs `computations/_shared/dirac_spectrum.py` on
`sys.path` (already provided via the `..` insert in the migration).

## Migration Delta

| Change | Location |
|:-------|:---------|
| Added `import json, hashlib` | top |
| Added canonical import stub (hygiene, noqa) | after `sys.path.insert` |
| Added `_sha256_file()` helper | module top |
| Added `PIN-BLOCK-BEGIN/END` prologue in `main()` | main() |
| Added `CLOSURE-SHA256` emission | main() prologue |
| Added `4TUPLE-BEGIN/END` in `main()` | main() epilogue |
| Tagged 5 `# (local)` on: `d_log_sigma` (x2), `S = 0`, `h_ds = 1.0`, `S_ref = 8.0` | lines 139, 178, 202, 211, 218 |

No algorithmic change. No canonical_constants.py modification.
