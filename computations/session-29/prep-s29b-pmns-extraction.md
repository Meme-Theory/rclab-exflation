### S29B-PMNS-EXTRACTION

- **Session**: S29b (original `sessions/archive/session-29/` synthesis) — re-run under S81 canonical verdict standards.
- **Path**:
  - Source (archive): `computations/session-29/s29b_pmns_extraction.py`
  - rerun script (new):  `computations/session-29/s29b_pmns_extraction.py`
  - Output NPZ:       `computations/_shared/t3-intake/s29b_pmns_extraction.npz`
  - Verdict file:     `computations/_shared/t3-intake/s29b_pmns_extraction_verdict.txt`
- **Classification**: PARTICLE
  - Mixing-angle extraction from the (0,0) singlet sector of D_K on Jensen-deformed SU(3). Representation-theoretic content of D_K — quantum numbers, not phononic excitations of the fabric.

- **Tolerance rule**: REPORT-VALUE (INFO). The S29b script is a compute-and-report gate. The observational PASS/FAIL window (`sin^2(theta_13) in [0.015, 0.030]` for P-29b; outside [0.005, 0.10] for B-29b) lives at the session-synthesis layer, not at the rerun script level. The canonical line therefore records `INFO` with the full numerical 4-tuple; no ratio/absolute threshold is applied in the canonical line.

- **Input SHA-256 pins (FULL 64-char hex)**:
  - `s23a_kosmann_singlet.npz`: `ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214`
  - Closure SHA-256 (JSON-sorted pin map): `d05c87930b4eaebd4b784a4c2fff73c4f57602b970114f16fc9a72cd0caf222c`

- **PRU machinery pin (PRDR)**:
  - `scheme`: Method B = degenerate perturbation theory reduction to 3x3 tridiagonal.
    - `V_12 = ||V[8, 9:13]||_2` (Frobenius norm of L1->L2 coupling row).
    - `L2_eff = V[8, 9:13] / V_12` (dominant L2 linear combination).
    - `V_23 = ||L2_eff @ V[9:13, 13:16]||_2` (Frobenius norm of effective L2->L3 coupling).
    - `V_13 = 0` exact (selection rule from S23a).
  - `convention`: `U[alpha, i]` with `alpha = flavor (e,mu,tau)`, `i = mass (1,2,3)` ascending. `sin^2(theta_13) = |U_e3|^2`, `tan^2(theta_12) = |U_e2|^2 / |U_e1|^2`, `tan^2(theta_23) = |U_mu3|^2 / |U_tau3|^2`.
  - `subspace`: positive-sector singlet indices 8..15 of the 16-eigenvalue D_K block; L1 = idx 8, L2 = idx 9..12, L3 = idx 13..15.
  - `tau grid`: `[0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]` from source npz.
  - `tau_fold` (canonical): `0.19` — grid-nearest is `tau = 0.20` (selected automatically; tau=0 excluded since coupling vanishes there and no 3x3 reduction is possible).
  - `eigensolver`: `numpy.linalg.eigh` on 3x3 real-symmetric H (also 16x16 for Method A cross-check). CPU path (matrix size <= 16), `OMP_NUM_THREADS=8`, `MKL_NUM_THREADS=8` set pre-numpy import.
  - `PDG reference (local, citation-only)`: PDG 2024 — `sin^2(theta_13) = 0.0220 +/- 0.0007`, `theta_12 = 33.44 +/- 0.77 deg`, `theta_23 = 49.1 +/- 1.0 deg`, `Delta m^2_32 / Delta m^2_21 = 32.6`.
  - `random_seed`: N/A (deterministic eigh on fixed inputs).
  - `GPU`: not used (matrices too small; CPU eigh is optimal, confirmed in canonical-environment rule).

- **Substitution chain (sign/direction claim for best-fit vs PDG)**:
  - Step 1 (definition): `sin^2(theta_13) := |U_e3|^2` — PMNS element, squared modulus.
  - Step 2 (PDG reference): `PDG_sin2_theta13 = 0.0220` (PDG 2024).
  - Step 3 (substitution): `delta := sin2_13_fit - PDG_sin2_theta13`.
  - Step 4 (simplification): `delta = 0.202569 - 0.0220 = 0.180569`.
  - Step 5 (direction from canonical form): `delta > 0 <=> sin2_13_fit > PDG_sin2_theta13 <=> best-fit ABOVE PDG`.
  - Python-verified: `sin2_13_fit=0.202569`, `delta=+0.180569`, `direction_label=ABOVE_PDG` (printed by script; matches the independent S32C report of `sin2_13_fold=0.213138` at the fold via cubic spline, same sign and comparable OOM).

- **Expected output 4-tuple** (S81 canonical form):
  - `value = sin2_13=0.202569, theta12=36.547deg, theta23=41.971deg, R=0.3810, delta_fit_vs_PDG=+0.180569(ABOVE_PDG)`
  - `scheme = MethodB_degenerate_PT_tridiagonal_3x3_eigh`
  - `convention = U[alpha,i]_ascending_mass_flavor_basis_sin2_13=|U_e3|^2_tan2_12=|U_e2|^2/|U_e1|^2_tan2_23=|U_mu3|^2/|U_tau3|^2`
  - `L_max = singlet_L1L2L3_subspace_0..15_tau_grid_nearest_to_tau_fold=0.19_tau_used=0.2`
  - `sha256 = d05c87930b4eaebd4b784a4c2fff73c4f57602b970114f16fc9a72cd0caf222c`

- **Status**: INFO (report-value). The numerical result constrains the singlet-sector tridiagonal scheme and quantifies how far `sin^2(theta_13)` sits above the PDG band at grid-nearest-to-fold. PASS/FAIL against the observational window is handled by the session-synthesis layer (B-29b / P-29b), not by this rerun verdict.
