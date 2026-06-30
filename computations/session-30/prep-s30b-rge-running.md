# Prep Block: S30B-RGE-RUNNING

## Gate Metadata
- **Gate ID**: S30B-RGE-RUNNING
- **Trigger**: [VERIFY]
- **Classification**: PARTICLE (gauge-coupling running — representation content of D_K through SM beta functions)
- **Source script**: `computations/session-30/s30b_rge_running.py`
- **rebuild**: `computations/_shared/t3-intake/s30b_rge_running.py`
- **Session origin**: S30Bb (2026-03-01, einstein-theorist agent)

## Hypothesis
The bare metric ratio g1/g2 = sqrt(L2/L1) extracted at the best point on the Formula B Weinberg contour in (tau, eps) space, run from the KK scale down to M_Z via SM one-loop RGE, reproduces the PDG value sin^2(theta_W)(M_Z) = 0.23122 for some M_KK in [10^10, 10^18] GeV with zero additional parameters.

## Pre-Registered Pass/Fail/INFO Criteria

| Gate | PASS | FAIL | INFO |
|:-----|:-----|:-----|:-----|
| RGE-A | sin^2(theta_W)(M_Z) = 0.23122 crossed for some M_KK in [10^10, 10^18] GeV | No crossing in range | Crossing outside [10^10, 10^18] but inside [10^4, 10^19] |
| RGE-B (conditional on RGE-A PASS) | abs(alpha_1(M_Z) - 0.01699) / 0.01699 < 0.05 | > 0.05 deviation | 0.05-0.10 |
| B-30rge | sin^2(M_Z) outside [0.15, 0.30] over the full M_KK window | (fires => anomaly boundary) | inside [0.15, 0.30] |
| B-30nck | Lambda_SA/M_KK outside [10^-3, 10^3] | (fires => tension) | inside [10^-3, 10^3] |

Tolerance rule: RATIO (dimensionless running ratio), ABSOLUTE for sin^2 threshold gates.

## Machinery Pin (PRDR)

| Parameter | Value | Source |
|:----------|:------|:-------|
| `N_eval` | 3001 log-uniform M_KK points | script line `log_M_range = np.linspace(4, 19, 3001)` |
| `L_max` | NA (RGE integration, no spectral truncation) | — |
| `scan_range` | log10(M_KK) in [4, 19] | script |
| `step_size` | d(log10 M_KK) = 15/3000 = 0.005 | derived |
| `tolerance` | 0.010 on sin^2_B for Weinberg contour selection | `tol = 0.010` (local) |
| `scheme` | SM one-loop RGE | b_i = (41/10, -19/6, -7) |
| `convention` | GUT-normalized g_1 = sqrt(5/3) g_Y | `r_KK = 5.0 * g1g2_KK**2` |
| `random_seed` | NA (deterministic) | — |
| `GPU path` | CPU-only (OMP_NUM_THREADS=8 pre-numpy) | small RGE ODE, GPU unnecessary |

## Input SHA-256 Pins
| File | SHA-256 (full 64-char) |
|:-----|:-----------------------|
| `s30b_grid_bcs.npz` | `5efa5c10ba24310b1efb0a37713d74ecde4b9367221f1965a0934bbf7c3ae4e6` |

Closure SHA-256 = SHA-256(json.dumps(pin_map, sort_keys=True, separators=(',',':'))):
`815aa927ac8518d5b74ccdf50e271ef4204476cf725fd9a656115586bc56a4b5`

## Expected Output 4-tuple
`(value=<v>, scheme=SM_one_loop, convention=GUT_normalized, L_max=NA)`

Observed: `(value=no_crossing, scheme=SM_one_loop, convention=GUT_normalized, L_max=NA)`

## Substitution Chain: b_i Sign Convention

Step 1 (definition):
    Standard SM one-loop RGE:  d(1/alpha_i) / d(ln mu) = -b_i / (2*pi)
    with b_1 = +41/10, b_2 = -19/6, b_3 = -7 in GUT normalization.

Step 2 (integration from M_KK down to mu < M_KK):
    1/alpha_i(mu) - 1/alpha_i(M_KK) = -b_i/(2*pi) * (ln mu - ln M_KK)
                                     = +b_i/(2*pi) * ln(M_KK/mu)
    => 1/alpha_i(mu) = 1/alpha_i(M_KK) + b_i/(2*pi) * ln(M_KK/mu)
    [matches script line 137]

Step 3 (direction):
    ln(M_KK/mu) > 0 since M_KK > mu.
    For b_1 = +4.1 > 0:  1/alpha_1(mu) > 1/alpha_1(M_KK)  => alpha_1(mu) < alpha_1(M_KK)
                        [U(1)_Y NOT asymptotically free — coupling is smaller at lower energy
                         because of positive beta function contribution from matter content]
    For b_2 = -3.17 < 0: 1/alpha_2(mu) < 1/alpha_2(M_KK) => alpha_2(mu) > alpha_2(M_KK)
                        [SU(2)_L asymptotically free — coupling grows at low energy]

Step 4 (Weinberg angle direction):
    sin^2(theta_W) = alpha_Y / (alpha_Y + alpha_2), alpha_Y = (3/5) alpha_1_GUT
    d/d(ln mu^-1) [sin^2 theta_W] involves:
      alpha_Y decreasing (b_Y > 0)
      alpha_2 increasing (b_2 < 0)
    Both trends push sin^2(theta_W) DOWN at lower mu.

Step 5 (numerical conclusion):
    Starting sin^2(theta_W)_KK = 3*L2/L1 / (1 + 3*L2/L1) = 0.241205 at M_KK.
    Target at M_Z = 0.23122.
    Naive target is BELOW starting value (0.23122 < 0.241205), so by direction
    alone the running COULD hit the target.
    Actual RGE scan: max sin^2(M_Z) over M_KK in [10^4, 10^19] = 0.218830 at M_KK = 10^4.
    Over the pre-registered gate window [10^10, 10^18]: sin^2(M_Z) in [0.134, 0.172].
    Running OVERSHOOTS the target — by M_Z, sin^2 has dropped ~5-10 percentage
    points below PDG across the entire gate window.
    VERDICT: RGE-A FAIL — crossing never occurs.

## Constraint-Surface Implication
- Eliminated region: RGE-A ansatz under Formula B at single best (tau, eps) grid point with g1/g2 = 0.325514 and SM one-loop running with PDG inputs.
- Preserved freedom (gate cannot test):
  (i) Two-loop corrections.
  (ii) Non-SM matter content between M_Z and M_KK (e.g., KK tower thresholds, supersymmetric states).
  (iii) Alternate formula normalizations (e.g., 5*L2/L1 instead of 3*L2/L1).
  (iv) Non-best-V contour points (the scan across 15 contour points shows the trend is uniform FAIL — see stdout table).

## Closure Statement
RGE-A at one-loop SM with PDG inputs and Formula B normalization FAILS the pre-registered gate. The failure is DIRECTIONAL but MAGNITUDE-inconsistent: the sign of d(sin^2)/d(ln mu) is correct for descent toward 0.23122, but the magnitude undershoots by 5-10 percentage points in sin^2 across the full GUT-scale M_KK window. B-30nck fires at 10^15 above threshold (Lambda_SA = 10^31 GeV, 15 OOM above M_Planck), indicating the unification of alpha_1 and alpha_2 starting from this normalization is nonphysical.

This gate closes the single-parameter Formula-B-at-best-contour-point path as a zero-parameter prediction of sin^2(theta_W)(M_Z). Further tests require additional parameters (extended beta content or threshold corrections).

## Canonical Constants Usage
- **Imported**: `M_Z`, `sin2_thetaW_MSbar`, `b1_SM`, `b2_SM` from `canonical_constants.py`
- **Tagged `# (local)`**: `ALPHA_1_MZ`, `ALPHA_2_MZ`, `SIN2_TW_PDG`, `B1`, `B2`, `B3`, `tol`
- **Not modified**: `canonical_constants.py` (per project rules)
- **Candidate for promotion to canonical**: `alpha_1_MZ = 0.01699`, `alpha_2_MZ = 0.03376` (PDG 2024) — used in this script and any future electroweak RGE work. Flagged but not promoted in this rerun pass.

## Environment
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe` (Python 3.12, torch 2.9.1+rocm available)
- CPU path: `OMP_NUM_THREADS=8`, `MKL_NUM_THREADS=8` set before numpy import
- Runtime: 0.2 s (small RGE ODE, no GPU needed)
- Outputs: `s30b_rge_running.npz`, `s30b_rge_running.png` in `computations/_shared/t3-intake/`
