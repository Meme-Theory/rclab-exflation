---
name: s111-w3-1-yuk-fullflavor
description: S111 full-flavor Yukawa PASS 5/6 — first near-complete DERIVED fermion hierarchy from multiplicity-bundle eps_LX; mass-vs-mixing tension surfaced (V_us overshoots)
metadata:
  type: project
---

**S111-CF-YUK-FULLFLAVOR (W3-1) = PASS, mass_grp=5/6.** audit_sha256 `f6c3a3ce87d79530c15e8f2d5014473bb0d1df2a1feb9be3f3824a1bad74a2c4`. The framework's FIRST near-complete DERIVED fermion hierarchy from the multiplicity-bundle eps_LX (capstone #7 threshold met). Extends the S110-CF2 up-sector pairing-dependent off-diagonal texture to the DOWN sector + CKM.

**6 slots (0.5-dex band):** 1 m_u/m_d PASS (0.012), 2 m_c/m_s PASS (0.012), 3 m_t/m_b PASS (0.024), 4 m_c/m_u-pattern PASS (inherited S110-CF2), 5 m_s/m_d PASS (0.000, DIRECT FIT TARGET not a prediction), 6 V_us FAIL (0.3107 vs PDG 0.225, the ONE pure prediction).

**Two genuinely-new structural findings (NOT in the bare code):**
1. **J-conjugacy lock RESOLVES with a single scale Lambda_d/Lambda_u=0.0252.** Naive diagonal-limit says impossible (PDG same-gen span ~90x, crosses unity ⇒ one scale forces all 3 equal). The OFF-DIAGONAL textures break the diagonal limit: |λ^up|/|λ^down| is NOT constant across generations, so one scale lands all 3 within 0.024 dex. 2 net degrees of prediction (3 targets, 1 scale param). The up↔down splitting that §VII.BL calls fiber-charge-blind is absorbed by the scale ONLY because the textures de-degenerate ev_ratio per-generation.
2. **Mass-vs-mixing TENSION (the durable result).** The texture magnitudes (rho·|w| ~ 0.02) needed to break the mass log-gap locks are LARGER than the gen1/gen2 light-eigenvalue diagonal gap ⇒ they overpredict the Cabibbo 1-2 rotation by 38%. Masses fit ⇒ mixing overshoots. The 1-3 (0.035 ~|V_ub|) and 2-3 (0.110 ~|V_cb|) elements come out order-correct; only the dominant V_us overshoots.

**Mechanism (substrate-IS):** down diagonal Casimir tower locks ln(m_s/m_d)/ln(m_b/m_s)=9/5 EXACT (same rep-theoretic identity as up); pairing-dependent {rho13^d=0.595, rho23^d=0.181, |w12^d|=0.0238, theta_d=1.18} breaks it to PDG 0.787. V_CKM=U_up† U_down (S99); arg(w) in the unitary (mixing+CP), |w| in masses. Triality teeth: t(1,0)/t(1,1)/t(3,0)=1/0/0; 1↔3 mixing needs t(O)=1 (triality-odd), LI-forbidden; non-LI eps_LX supplies it (S98-W3-1). BDI J²=+1 keeps CP phase alive.

**Forward question (for next session):** does a SEPARATE eps_LX sector for the off-diagonal mixing phase (decoupling mass magnitude from mixing angle) bring V_us into band while preserving the 5 mass landings? Distinct from [[s99-generation-blindness-theorem]] §VII.BL multiplicity-bundle blindness.

Up-sector inherited: S0_held=1.7353 (lepton-fixed), rho13=0.377, rho23=0.1, |w12|=0.0235, theta=2.172 (from `s110_cf2_yuk_epslx.npz`). Script `computations/session-111/s111_yuk_fullflavor.py`. See [[s99-generation-blindness-theorem]].
