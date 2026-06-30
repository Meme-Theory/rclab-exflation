# Prep: S46-OMEGA-CLASSIFY

## Domain Identification & Task-Description Mismatch

**Task description** said: *"cosmological Omega_X classification (matter,
radiation, DE, DM, curvature partition)"*.

**Actual script domain**: Connes NCG inner-fluctuation module
**Omega^1_D(A_F)** — spectral 1-form classification under gamma_F grading
into gauge (even) vs scalar (odd) directions, with tau scan of lightest
mass-squared eigenvalue.

The two "Omega"s share only the letter. S46 has NO cosmological Omega_X
partition routine. The cosmic-web agent confirms: any cosmological Omega_X
assessment must be re-routed to S66-S69 DESI/Pantheon-chain scripts, not
to this module.

Proceeded with the actual gate (the pre-registered one in the script)
rather than inventing a nonexistent cosmological computation.

## Steps Executed

1. **Located**: `computations/_shared/t3-intake/s46_omega_classify.py`
   (active copy); archived source at `computations/session-46/s46_omega_classify.py`.

2. **MCP knowledge queries** (all three per task):
   - `trace_entity("omega_classify")` -> single provenance record, gate
     CLASSIFY-46, output s46_omega_classify.npz.
   - `search_knowledge("S46 Omega classify")` -> 20 hits, all point to
     inner-fluctuation module code, no cosmological Omega_X.
   - `get_constant("Omega_Lambda")` = 0.685 (Planck 2018, no provenance
     tag — task did not require adding one).

3. **Canonical import verification**: Script already imports `from
   canonical_constants import *` and uses `TAU_FOLD_CANON = tau_fold`
   (tagged `# (local)` alias). No hardcodes found; no edits needed to
   `canonical_constants.py`.

4. **Local-variable tagging audit**: All intermediate values already
   tagged per  CLAUDE.md. No missing tags.

5. **SHA-256 input pins**:
   - `t3-intake/s46_omega_classify.py`: drifted (stale pin
     `59248d1f...`). Updated to current `fdb95e8d...` (post-edit pre-run
     state). Bootstrap paradox documented.
   - `canonical_constants.py`: pin `68b50cd3...` matches current file.
   - `dirac_spectrum.py`: pin `eee1b6fd...` matches current file.

6. **Closure SHA** (ordered pin concat):
   `6d0c39941a54355f8d16e9bf91e8dbe079d3d5ad045e6e56c5d855d9a599573c`
   (64-char, verified via Python hashlib on the script's own closure
   computation in the run output).

7. **Ran script** with `OMP_NUM_THREADS=8 MKL_NUM_THREADS=8` on venv312.
   Runtime: 65.8 s. Output: `s46_omega_classify.npz` saved.

8. **Verdict**: FAIL (pre-registered branch: all scalar modes massive at
   all scanned tau).

## Substitution Chain — Omega_DE Direction vs Planck

Since the task requested an Omega_DE direction claim chain, and the
S46 script does NOT produce Omega_DE, I provide the chain for the
framework's cosmological Omega_Lambda consistency with Planck, drawn
from canonical constants and S67 closed results (NOT from this run).

Step 1 (definitions):
  Omega_Lambda = rho_Lambda / rho_crit (Planck 2018 observational)
  Planck best-fit:  Omega_Lambda = 0.685  (canonical_constants)
  Framework w_0:    -0.918  (DESI-VOLOVIK-67, closed S67,
                              canonical_constants.w0_FW)

Step 2 (substitution for flatness):
  Omega_total = Omega_Lambda + Omega_m + Omega_r
               = 0.685 + 0.315 + 9.15e-5
               = 1.000091500

Step 3 (canonical form):
  |Omega_total - 1| = 9.15e-5

Step 4 (direction from canonical form):
  |Omega_total - 1| < 10^-3  ->  universe flat within Planck 1-sigma.
  Framework's w_0 = -0.918 shift is a 2.91-sigma (1D) / 4.12-sigma (2D)
  tension with DESI DR2 at z_pivot (S58 result, not this gate).
  It does NOT redistribute the Omega_X partition at z=0 measurably.

**For THIS gate's actual direction claim** (scalar-mass at fold vs round):

Step 1 (definitions):
  m^2_min(tau) = min eigvalue of M^2 on odd-graded Omega^1_D subspace

Step 2 (substitution, from run output):
  m^2_min(0.00) = +0.000649
  m^2_min(0.19) = +0.000870

Step 3 (simplification):
  delta = +0.000870 - (+0.000649) = +0.000221

Step 4 (direction):
  delta > 0  =>  fold HEAVIER than round.
  m^2_min > 0 for all tau in [0.00, 0.30].
  No tachyonic mode. FAIL branch of pre-registered gate.

## Deliverables

- `computations/_shared/t3-intake/s46_omega_classify_verdict.txt`
- `computations/_shared/t3-intake/prep-s46-omega-classify.md` (this file)
- `computations/_shared/t3-intake/s46_omega_classify.npz` (data)
- `computations/_shared/t3-intake/_s46_run.log` (full stdout)

## Constraint-Map Update

The S46 re-run CLOSES one specific tau-stabilization mechanism
candidate: "Jensen deformation induces tachyonic instability in the
odd-graded (scalar) subspace of Omega^1_D(A_F)". Result: **no such
instability exists**; all 279 scalar modes remain positive-massed
across tau in [0.00, 0.30]; fold is not a saddle in this sector.

Remaining candidates for tau-stabilization (not closed by this gate):
- Spectral action variation dS/dtau, d2S/dtau2 (standard route,
  already pinned in canonical_constants)
- Transit-dynamics: instanton gas, Parker squeezing, first-order
  phase transition at the fold (S36+ paradigm)
- Higher inner fluctuations Omega^2_D, Omega^3_D (untested here)
- Sector-dependent D_K boundary conditions (untested here)

Cosmic-web agent note: this gate is NOT a cosmological test. It
does not touch P(k), xi(r), BAO scale, void statistics, or bulk
flows. Classification: GEOMETRIC (fiber-internal spectral
structure). No substrate-to-observable bridge is engaged.
