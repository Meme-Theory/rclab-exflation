---
name: qeq-drive-h-parity-100a
description: S100a W1-2 FAIL — GD-derived q_eq(H) is exponent-locked at H^2 (EVEN-in-H parity theorem); slope-1 tracking leg is imposed-closure only; KV self-consistent back-reaction is the open route
metadata:
  type: project
---

S100a-W1-2-QEQ-DRIVE (FAIL, composite sign=PASS/mag=FAIL/regime=VALID, domfrac=1.0000): the plan's candidate-(i) Gibbs-Duhem drive `q_eq(H) = (dq/dmu)·mu(H)`, EVALUATED, gives q_eq = kappa2·H^2 — NOT linear. Chain: T = H/pi (Volovik Paper 11) x bulk dS entropy density s = 3H/4G => s(T) = (3pi/4G)T => delta-mu = -(1/n_q)Int s dT = -(3/(8 pi G n_q))H^2 => q_eq = chi·delta-mu = kappa2 H^2, kappa2 = 3/(8 pi G n_q k_curv). Integrated on arr_H_bare_t: slope d ln q/d ln H = 2.0556 (R^2 0.9955; exponent transmits + tracking-lag 0.056 from the Hdot-spike in the tail, eps_ad=0.90 locally). kappa2-invariance 7.6e-8 (multiplicative-cancellation identity — NO coefficient ever tunes a log-derivative slope; only the exponent moves it).

**H-parity theorem (durable)**: T and s are |H|-odd; the Gibbs-Duhem potential shift Int s dT is |H|-EVEN => no substrate-internal EQUILIBRIUM thermodynamic potential can carry a term linear in H. The odd-in-H sector is dissipative and in the friction ODE it IS the 3Hq' term — not a potential. Hence q_eq ∝ H (the slope-1-capable form) is structurally IMPOSED-closure-only on a fixed backbone. n = 2 x slope: GD drive gives n≈4 on fixed backbone, not n=2.

**Why:** the corpus-faithful KV mechanism for rho_vac ~ H^2 (Papers 25 §V / 35) is oscillation-energy SELF-CONSISTENCY (q-oscillation energy dominates Friedmann, redshifts dust-like, amplitude ∝ a^{-3/2} ∝ H on the self-consistent a ∝ t^{2/3} background) — a back-reaction mechanism, not a drive, structurally unavailable when H(tau) is pinned.

**How to apply:** (1) any future "substrate q_eq(H) drive" proposal: check H-parity first — equilibrium-sector drives are even (H^2 leading), so adiabatic tracking transmits even exponents; (2) the genuine forward gate is SELF-CONSISTENT back-reaction (H re-derived from q-oscillation energy via §6.3 closure; CF candidate logged in WP §W1-2); (3) slope-vs-coefficient: log-derivative observables are coefficient-blind (math-scripts.md multiplicative-cancellation) — only exponents are gate-bearing; (4) C10 Object-C = STRUCTURALLY-CONDITIONAL, capstone §8.5 OPEN by design; DILUTION-CC's q∝H conditionality now has its structural locus (odd-sector smuggling). Verdict + artifacts: computations/session-100a/s100a_w1_qeq_drive.{py,npz,png}, audit e31d45cf5309b32c.
