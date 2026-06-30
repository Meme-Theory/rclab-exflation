### S22A-PAASCH-CURVE
- Session: S22a (re-run under S81 canonical verdict form)
- Path: computations/session-22/s22a_paasch_curve.py
- Current SHA head: 1e2261a470f0a7ff
- MCP baseline: phi_paasch = 1.531580 (get_constant returns 1.53158; canonical_constants.py L125 states "1.531580 PROVEN (S12, machine epsilon). Paasch spectral ratio at s=0.15"). trace_entity("paasch_curve") returns 1 provenance (s22a_paasch_curve.py -> s22a_paasch_curve.npz/.png) + 10 equation hits. search_knowledge("S22a Paasch curve") returns 1 provenance + 19 equation hits, all src=s22a_paasch_curve.py or downstream s33w3_paasch_dump_point.py.
- Classification: GEOMETRIC (D_K eigenvalue ratio m_{(3,0)} / m_{(0,0)} on Jensen-deformed SU(3); pure spectral-triple property; no phononic excitation involved; ratio IS the fabric's structural invariant, not an emergent observable)
- Tolerance: THEOREM machine-epsilon (re-run must reproduce existing s22a_paasch_curve.npz key-by-key: ratio vector, crossings list, tau_closest, ratio_closest; s19a_sweep_data.npz is a static pinned input)
- Input pin list:
  - s22a_paasch_curve.py (script, original at computations/_shared/): sha256=1e2261a470f0a7ff99ef30c35cffd76d8a4ccc69fcfec00e59ab71eca2f81706
  - s19a_sweep_data.npz (upstream eigendata, static): sha256=ad2a0da375f516aa24430db6630c733300428fa9682b0986a70b9b766aec1f5a
  - canonical_constants.py (phi_paasch source): sha256=68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
- PRU machinery:
  - phi_paasch: pinned = 1.531580 (canonical_constants.py L125; PROVEN S12 machine-eps; solution to x = e^{-x^2} transcendental)
  - tau grid: pinned = np.arange(0, 2.01, 0.1), 21 points (inherited from s19a_sweep_data.npz; not a free parameter)
  - Load-bearing sectors: pinned = {(0,0), (3,0), (0,3)} (SU(3) irrep labels p,q)
  - Interpolation: pinned = scipy.interpolate.CubicSpline with brentq root-bracketing on adjacent sign changes
  - tau_fine grid for crossing search: pinned = np.linspace(0, 2, 2000) (crossings) and np.linspace(0, 2, 10000) (closest approach)
  - Crossing pre-reg range: [0.14, 0.16] for M1 interpretation
  - M1 reference: pinned = 0.1084 (tau-location of M1 ridge feature; local variable, informational only)
  - random_seed: N/A (deterministic spline evaluation and brentq on monotone delta)
  - Compute path: scipy (CubicSpline, brentq) and numpy on CPU; all arrays are 21-point or smaller 1D; GPU not warranted.
- Substitution chain (direction claim: "r(tau) crosses phi_paasch in [0.10, 0.20]"):
  Step 1: r(tau) := E_{(3,0)}(tau) / E_{(0,0)}(tau)                 [definition, script L93]
  Step 2: delta(tau) := r(tau) - phi_paasch                          [script L114]
  Step 3: r(0.10) = 1.53708755 and r(0.20) = 1.51997722               [values from s19a_sweep_data.npz]
  Step 4: delta(0.10) = +0.00550755, delta(0.20) = -0.01160278        [substitution]
  Step 5: sign(delta(0.10)) * sign(delta(0.20)) = (+1)(-1) = -1 < 0  [canonical form]
  Step 6: by the intermediate value theorem for the CubicSpline interpolant of delta on [0, 2], exactly one root exists in [0.10, 0.20].  [direction read-off]
  Conclusion: the spline delta(tau) has a root in [0.10, 0.20]; brentq localizes it. At tau=0, delta(0)=-0.00405 (< 0), and delta(0.10)=+0.0055 (> 0), so a FIRST crossing also exists in [0, 0.10]. The second crossing (the M1-relevant one) lies in [0.10, 0.20].
- Gate thresholds (pre-registered, S81 canonical form):
  - PASS: reproduction of s22a_paasch_curve.npz values to relative error <= 1e-12 on {ratio[i], tau_closest, ratio_closest} and absolute match on crossings[] to within 1e-10 tau.
  - FAIL: any deviation above 1e-10 on crossings[] or 1e-12 relative on ratio vector.
  - INFO only: updated SHA pins if inputs have drifted since S22a.
- Expected output 4-tuple:
  (value = "tau_closest=0.01880188, ratio_closest=1.53158601, crossings=[0.04240363, 0.13218843]",
   scheme = "s19a-eigendata-spline-brentq",
   convention = "r=E30/E00_min_per_sector",
   L_max = "max_pq_sum=6_from_s19a")
- What PASS means: phi_paasch = 1.531580 is preserved as the exact Paasch-ratio anchor at s=0.15 (via the second crossing in [0.10, 0.20]) even under S81 canonical-import scrutiny. MCP baseline holds machine-exact.
- What FAIL means: drift in s19a_sweep_data.npz or canonical_constants.py has broken the S12 proof. Re-verification across S22a downstream scripts (s33w3_paasch_dump_point.py, etc.) required.
