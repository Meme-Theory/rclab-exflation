---
name: S84 W8a-85 stationary-point verification at tau_fold
description: FAIL verdict on plan's claim that tau_fold=0.190 is analytic stationary point of Chamseddine-Connes spectral action; plan's Jensen ansatz lambda=alpha*exp(2*tau*c) also falsified
type: project
---

# S84 §W8a-85: S84-STATIONARY-POINT-VERIFICATION-TAU-FOLD

**Verdict**: FAIL — value=-2.036e+04 (Gaussian cutoff, primary), value=+5.868e+04 (|lam| cutoff, S42 convention)

**Why**: Plan hypothesis "tau_fold is a stationary point of S[D_K(tau)] with dS/dtau=0 at machine precision" is FALSE under every tested cutoff. Canonical S42 dS_fold = 58672.8 is REPRODUCED by the analytic spectral-moment formula to 58 ppm — the machinery is correct; the hypothesis is wrong. The framework has always known dS_fold != 0 (it DRIVES the transit in the moduli EOM); the plan re-stated the hypothesis in a form that requires it to be 0, and it isn't.

**How to apply**: 
- §W8-90 PASS-THEOREM branch (`tau_fold as derived critical point of a single variational principle on S[D_K(tau)]`) is now **closed**. PASS-PARTIAL or FAIL are the only branches open for §W8-90.
- Don't re-propose `tau_fold` as stationary point of the BARE Chamseddine-Connes spectral action — the numbers say it isn't. If a variational principle exists, it's for a DIFFERENT functional (matter-dressed, GGE entropy, or mechanism-chain).
- Plan's Jensen ansatz `lambda_n(tau) = alpha_n * exp(2*tau*c_n)` with `c_n in {+1, -1, +1/2}` is STRUCTURALLY FALSE. Measured log|lambda| slope in tau (top-magnitude (0,0) ev): 0.64 — does not match predicted {+2, -2, +1}. PRU Class 8 defect in plan §W8a-85 Step 2. Use numerical Hellmann-Feynman (sorted finite-difference) instead.
- Plan claim "L_max=10, 155,984 eigenvalues cached" is NOT matched by disk state. The authoritative cache is `computations/s36_sfull_tau_stabilization.npz` (10 KK sectors, max(p+q)=3, ~1,232 eigenvalues). Same truncation produced S42 canonical dS_fold; Gaussian-suppressed heavy modes contribute exponentially small corrections.

**Permanent numbers (reproduced at machine epsilon)**:
- Analytic dS/dtau(|lam|) = +5.867622e+04 (matches S42 dS_fold=58672.8 to 58 ppm)
- Analytic d2S/dtau2(|lam|) = +3.182056e+05 (matches S42 d2S_fold=317862.8 to 0.1%)
- Analytic/FD ratio = 1.000000 machine precision (machinery verified)
- Gaussian dS/dtau = -2.036e+04 (8 orders above PASS threshold 1e-10, 8 orders above FAIL threshold 1e-4)
- d2S/dtau2 sign is regulator-dependent: `-1.0e+05` (Gauss) vs `+3.2e+05` (|lam|)
- No zero of dS/dtau exists in tau in [0.17, 0.22] under either cutoff

**Closure SHA**: 581a23921b9eb3aee1d4fc82c141cd0c02e47112c1c5224b6189b69e1f622308

**Artifacts**:
- `computations/s84_w8a_stationary_point_verification_tau_fold.py`
- `computations/s84_w8a_stationary_point_verification_tau_fold.npz`
- `computations/s84_w8a_stationary_point_verification_tau_fold.png`
- WP: `sessions/archive/session-84/session-84-w8-workingpaper.md` §W8-85
