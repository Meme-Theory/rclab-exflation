---
name: s116-q23-as-grounding
description: S116 Wave-1 Q23 A_s planning grounding — CF21 already reconciled (INV12-W3-5), live A_s routes + OOM map, squeeze×greybody factorization, S110-CF-AS2 regime-breakdown
metadata:
  type: project
---

S116 Wave-1 (Q23 A_s normalization) plan-freeze grounding. The context file's "2.38 / 3.15 / 4.56 OOM" framing is STALE; the true current state:

**CF21 ALREADY RECONCILED** — `INV12-W3-5-CF21-HTILDE-RECONCILE` (PASS, `computations/investigation-12/inv12_gate_verdicts.txt`): `cc3=2.000000`, `oomH_TDLI=2.3798` (H̃-space), `oomAs_TDLI=4.7595` (A_s-space), `fig238=Htilde-space`, `fig456=As-space-stale-live4.76`, `Hratio_TD_base=1.2532 ≈ sqrt157=1.2535`. So **2.38 (H̃-space) and 4.76 (A_s-space) are the SAME divergence in two spaces, related by CC3 factor-2 (A_s ∝ H̃²)**; the "4.56" was a stale rendering of the live 4.76. NOT divergent figures. (atlas-08 CF21 + atlas-04 still carry the un-reconciled "2.38 vs 4.56" — a capstone-hygiene drift.)

**Live A_s OOM map vs Planck A_s=2.1e-9** (the S115 sudden↔adiabatic axis, PLURALISM-PERMANENT):
- TD/zeta UNIFIED-AS-79 (Branch-A): A_s=3.2994e-9, OOM=+0.196 (ratioPlanck 1.5712)
- maxent (S115): 1.4006e-8, +0.824
- box-delta/impulse `A_s_FW` (S111-CF-AS3a, NOT superseded, CANONICAL): 1.5367e-8, +0.864
- Parker inv6 (S110 pair): 5.99e-8, +1.455
- Connes-Parker (S115): 7.068e-8, +1.527
- existing-routes spread (TD/zeta→Parker) = **1.259 OOM** = `S115-AS-NEWAXIS-SELECTOR spread_existing_OOM`; maxent+Connes selector FAILed to collapse (min_collapse_dist 0.628 ≫ 0.1 band).

**Factorization**: A_s = (squeeze) × (greybody filter).
- SQUEEZE (S111 recipe): A_s=|β_{k̂}|²/(2π²), N_norm=ξ_KZ³, k̂=1/ξ_KZ=53.30 M_KK (`xi_KZ_FW=0.018760`), |β|² from S100b box-delta SUDDEN spectrum (MAGNITUDE source). Fold-window grid = REGIME source (89/89 frozen-superhorizon, WKB leg EMPTY, Z_norm=1). Naive fold-window UV-extrapolation → +9.37 OOM = discredited artifact (use box-delta for magnitude, fold-window for regime — TWO-SPECTRA-TWO-ROLES).
- GREYBODY FILTER: fitted Γ=0.511872 (S95 W4-3, sigmoid at band-midpoint 0.9418). `INV12-W3-4` derived ∫Γ=0.036265 (static κ_exit=47.6146 barrier) → agreement 0.929 FAIL; bracket {κ_exit²→0.036, T_compound²=57.43→0.836} straddles 0.512 at NO substrate scale. **`S110-CF-AS2-GREYBODY` (FAIL)**: a DYNAMICAL substrate barrier (ω_q=2.0128 / relic_rms=2.9253) reproduces 0.512 to `best_inband_rel_dev=0.0494` (magnitude=PASS!) BUT `eps_WKB=γ_clock/κ_eff²=7.34@ω_q, 3.48@relic_rms ≫1`, `domain_used_frac=0.143` → `regime=BREAKDOWN` → composite FAIL. So magnitude is substrate-REACHABLE, WKB-INVALIDATED. Live CF-AS-2 question: does an EXACT (non-WKB) finite-rate BdG scattering validate the magnitude-PASS, or is the greybody irreducibly fitted (A2 knob, structural-closure)? **RESOLVED S116-W1-AS-CF2 FAIL** (audit_sha256=c7bb96b625ede2b3…, regime VALID): greybody IRREDUCIBLY FITTED. EXACT 3-channel Floquet coupled-channel scattering (Ω=ω_q, validity=ODE-convergence NOT eps_WKB) shows substrate-fixed barrier scales STRADDLE 0.512 (∫Γ∈[0.00065,0.99999]; closest relic_rms,V0=κ²→0.654, agree 0.278≫0.10) on BOTH static AND finite-rate channels. Finite-rate correction ≤6.9e-4 even at DTC threshold h=0.0725 (**Kapitza high-frequency averaging**: fast eps_WKB≫1 but small-amplitude drive averages to static barrier). Floquet monodromy max|Tr M|=1.99999446<2, frac_resonance=0 (no parametric amplification; INV12-W3-2 lineage). **eps_WKB DECOUPLING**: f_used_ODE=1.00 VALID vs S110 f_used_epsWKB=0.143 BREAKDOWN — SAME barrier, the eps_WKB breakdown was a WKB-METHOD artifact, not a physics wall. So the closure is STRONGER than S110: not "reachable-but-WKB-invalid" but "exact valid treatment confirms 0.512 has no substrate scale." 0.512 lives only at the in-band V0 fit (A2 knob = S95 sigmoid at band-midpoint 0.9418). Cross-checks: ODE-vs-closed-PT 1.2e-10, ODE-vs-Floquet(h→0) 1.0e-10≤1e-8, monodromy h0-vs-analytic 4.9e-15, Manley-Rowe norm-dev 3.1e-5.

**CF23 SPLIT (S110)**: (a) FLOOR A_s≥A_s^BD PERMANENT 3-axis; (b) MAGNITUDE/upper-edge SCHEME-DEPENDENT FILTER = OPEN = the live CF-B1/CF-AS-2/CF-AS-3 question.

**n_s scheme split** (regulator-variants, NOT a contradiction): n_s_FW_sqrt_cutoff=0.959 (S103, sqrt-cutoff), n_s_framework=0.9561 (S85, Route-B exact 9561/10000), n_s_canon=0.9649 (Planck). deg(T_BZ→pivot)=+2 NON-SCALAR (S93 W7-1) sets which leaf a detector reads.

S116 gate design: CF-B1=squeeze magnitude promotion + L_max POINT-vs-BAND (AS3b-deferred); CF-AS-2=exact non-WKB greybody (build on S110-CF-AS2 regime-breakdown); CF-AS-3=product reconciliation (mack) collapse-vs-S115-PLURALISM + n_s split. See [[s116_q23_as_grounding]] companions in MEMORY.md A_s rows.
