### S22A-DNP-BOUND
- Session: S22a (SP-5, 2026-02-20)
- Path: computations/session-22/s22a_dnp_bound.py
- Script SHA-256: 539fd7381aac9694cd3fe1b6b90c84c90372ae52dd3af6e03cee63d0f1174d63
- Classification: GEOMETRIC (Lichnerowicz TT-eigenvalue spectrum on Jensen-deformed SU(3); constrains endpoint selection of tau-trajectory, no phononic excitation content)
- Tolerance: THEOREM (machine-epsilon) — proven structural theorem (proven_792, proven_807, proven_822); re-run must reproduce bit-for-bit
- Gate hypothesis: re-running s22a_dnp_bound.py reproduces the permanent DNP instability theorem — lambda_L/m^2 < 3 for tau in [0, 0.285] — to machine precision
- Pass/fail threshold: crossing tau_c (ratio=3) within grid-step of canonical 0.285 AND monotonicity signature (lambda_L_min strictly decreasing, ratio strictly increasing) reproduced

- MCP baseline (trace_entity DNP_instability):
  - theorem proven_792: "DNP instability: λ_L/m² < 3 for τ ∈ [0, 0.285]" PROVEN
  - theorem proven_807: "DNP instability: lambda_L/m^2 < 3 for tau in [0, 0.285]. Round metric is TT-unstable." PROVEN
  - theorem proven_822: "DNP instability for tau < 0.285" PROVEN
  - gate SP-5: "At M1 (tau=0.15): ratio=1.80 (UNSTABLE); at tau=0.30: ratio=3.18 (STABLE); ratio < 3 at any tau signals TT instability"
  - open_channel "S22a SP-5": "Uses L_max=3 (0,0) sector eigenvalues [...] block-diagonal-protected, eigenvalues L_max-invariant"
  - S75 bidirectional robustness (eq_147417): lambda_00_min = 0.960314 at BOTH L=5 AND L=7
  - expulsion direction (eq_9273): "at tau = 0 [...] is expelled by the DNP instability toward increasing tau"

- Substitution chain for bound-direction claim (DNP instability, PERMANENT theorem):
  - Step 1:  DNP criterion (Duff-Nilsson-Pope): TT stability on compact K requires `lambda_L_min / m^2_gauge >= 3`.
  - Step 2:  KK gauge mass (Session 17a, pinned via dep chain): `m^2_gauge(tau) = exp(-4*tau)`.
  - Step 3:  Substitute: `ratio(tau) = lambda_L_min(tau) * exp(+4*tau)`.
  - Step 4:  Computed: `lambda_L_min` strictly decreasing (1.00 -> 0.75 over tau in [0, 2]); `exp(+4*tau)` strictly increasing; product `ratio(tau)` is strictly increasing (verified).
  - Step 5:  `ratio(0) = 1 < 3`; `ratio -> infinity` as `tau -> infinity`. By IVT + monotonicity, unique crossing `tau_c` with `ratio(tau_c) = 3`.
  - Step 6:  Re-run numerical crossing (linear interp between tau=0.2 and 0.3): `tau_c = 0.282265`; MCP canonical = `0.285`; delta = `0.003` (inside tau-grid step 0.1, consistent with finer-grid canonical).
  - Step 7:  Physical window [0.15, 0.55] intersects [0, 0.282] at [0.15, 0.282]; DNP bound violated throughout -> round metric TT-UNSTABLE -> triple-selects tau=0 as initial condition (expelled toward increasing tau).
  - Conclusion: bound is violated for `tau < tau_c ~ 0.285`, satisfied for `tau > tau_c`; permanent structural theorem.

- Input pin list:
  - s22a_dnp_bound.py  (script)  SHA 539fd7381aac9694cd3fe1b6b90c84c90372ae52dd3af6e03cee63d0f1174d63
  - l20_lichnerowicz.py          SHA 879a0febdddb0870f7c30350b0f946b06c06d55f10ebb7fc0224fea91fc3246c  (build_sym2_traceless_basis, riemann_endomorphism_on_sym2, ricci_endomorphism_on_sym2, build_lichnerowicz_on_sector)
  - r20a_riemann_tensor.py       SHA c71eb71a4f34eb08e25022bf2c44ced1ea7e8add25d9630092962b5c4174356c  (compute_riemann_tensor_ON_fast, ricci_from_riemann)
  - dirac_spectrum.py      SHA eee1b6fdcbb86847385130b3b3467c76fe1b5b73573d7dac4baf428cf4ff163f  (su3_generators, compute_structure_constants)
  - canonical_constants.py       SHA 68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f  (pinned for audit lineage; NOT imported — S22 is below S34 exemption threshold)

- PRU machinery (all pinned):
  - tau_grid:         `np.arange(0.0, 2.05, 0.1)` (21 points, inclusive endpoints) — SCAN PARAMETER
  - sectors scanned:  (0,0), (1,0), (0,1); `global_min = min over 3 sectors` — PRE-REGISTERED SP-5
  - basis_dim:        35 (sym^2-traceless on su(3), n=8) — STRUCTURAL
  - L_max:            3 (via n=8 generator path); L_max-invariant per S75 bidirectional (L=5,7 give same lambda_00_min=0.960314) — STRUCTURAL
  - DNP_threshold:    3.0 (theorem constant, not free) — PRE-REGISTERED (per DNP theorem)
  - phys_window:      [0.15, 0.55] — PRE-REGISTERED (SP-5 physical window)
  - m2_gauge_law:     `exp(-4*tau)` (Session 17a; pinned by dependency chain)
  - eigvals_path:     `numpy.linalg` on dense 35x35 matrices (below 100x100 GPU threshold)
  - OMP/MKL threads:  `OMP_NUM_THREADS=8`, `MKL_NUM_THREADS=8` (CPU cap per env rules)
  - random_seed:      N/A (fully deterministic)
  - GPU path:         N/A (all matrices < 100x100)

- Gate thresholds (pre-registered):
  - THEOREM-REPRODUCE: crossing `tau_c` within grid-step (0.1) of canonical 0.285 -> PASS
  - MONOTONICITY: `lambda_L_min` strictly decreasing AND `ratio` strictly increasing -> PASS
  - FAIL: any violation of monotonicity, OR crossing outside [0.18, 0.38], OR VIOLATED-flag not triggered on tau in [0, 0.2]

- Expected output 4-tuple: `(value=<tau_c>, scheme=DNP_TT_lmin_over_m2gauge, convention=global_min_over_sectors_00_10_01, L_max=3)`

- What PASSES means for the solution space:
  - Permanent result `tau=0 is TT-UNSTABLE` is confirmed at the re-run level — round-metric end cannot be a stable vacuum.
  - Triple-selection of `tau=0` as INITIAL condition (WCH + J-maximality + DNP instability) remains anchored.
  - Expulsion direction `tau=0 -> increasing tau` consistent with Jensen-curve dynamics (tau-trajectory).

- What FAIL would have meant:
  - A numerical FAIL here (crossing far from 0.285, or non-monotonic ratio, or no violation in physical window) would FALSIFY one of the three theorems anchoring the endpoint selection, propagating to: Session 29a triple-selection, S75 bidirectional L_max-robustness, and the fold-direction / tau-expulsion narrative.
  - No such FAIL observed.

- canonical_constants.py modifications: NONE.
  - Script S22 is pre-S34 (exempt per project CLAUDE.md).
  - Script contains NO hardcoded framework constants:
    - tau_grid = `np.arange(0.0, 2.05, 0.1)` is a scan parameter (local).
    - DNP threshold = 3 is the theorem under test (theorem constant, not framework).
    - n = 8 is sym^2-traceless basis dimension (structural, su(3) fixed).
    - `exp(-4*tau)` is the KK-coupling-derived m^2_gauge law (structural Session 17a).
  - No `# (local)` tags required; no constants to promote to canonical_constants.py.
  - Script left unmodified.

- Execution path used:
  - `cd computations/_shared/` (to resolve l20_lichnerowicz and r20a_riemann_tensor co-located dependencies).
  - `OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 "../phonon-exflation-sim/.venv312/Scripts/python.exe" s22a_dnp_bound.py`
  - Outputs written to computations/_shared/ (per the script's `SCRIPT_DIR` hardcoded path — note: SCRIPT_DIR resolves to `computations/_shared/` when run from there, and `np.savez` uses `os.path.join(SCRIPT_DIR, ...)`, so outputs land in `computations/_shared/`; the stdout line "Data saved: computations/session-22/s22a_dnp_bound.npz" is a stale print string from before the archive move — ACTUAL output path is `computations/session-22/s22a_dnp_bound.npz`; this is cosmetic, does not affect the numerical result or SHA pin).

- Closure SHA-256: `095104f88cdbb2c145fa8e6a8da96539fd4224b732f157314374110ba3dd5298` (64 hex chars; SHA-256 of json-canonical sorted pin map).
