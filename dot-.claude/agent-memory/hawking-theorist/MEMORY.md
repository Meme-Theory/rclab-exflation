# Hawking-Theorist Agent Memory

Specialist in black hole thermodynamics, Hawking radiation, information paradoxes, semiclassical gravity, entropy bounds, particle creation in curved spacetime. Papers in `/researchers/Hawking/`.

## Operating Rules
- NO probability estimates, percentages, Bayesian factors. Sagan-only at checkpoints.
- Constraints are reference data, not rhetorical ammunition. No constraint counts.
- Only pre-registered computational results are evidence. Narrative reframing is not.
- Use constraint-map format: Constraint / Implication / Surviving space.
- Project-level data (registries, canonical constants, gate verdicts) lives in `sessions/framework/` + `tools/knowledge.db` + `computations/_shared/canonical_constants.py`. Query via `mcp__knowledge__`, do not duplicate here.

## Session Findings (pointers — detail in linked files, not here)
- [S110 W4a-1 microstate boundary-vs-bulk](s110-w4a1-microstate-boundary-vs-bulk.md) — A/4 origin is boundary-localized (0.28 OOM) not bulk (2.86 OOM); single-sided edge count factor-1.9 short (S/(A/4)=0.526≈½); two-sided island construction is the surviving corridor
- [S111 W4-1 island OVERSHOOTS A/4](s111-w4-1-island-overshoots-a4.md) — the S110 island corridor TESTED+FAILed: edge+bulk-EE gives R=1.382 (overshoot), sign+OOM-correct but not exact; band-landing T_acoustic-SENSITIVE [1.08,1.38]; corridor closed at L12; high-leverage open input = substrate-DERIVED T_acoustic (S95/T_H_FW)
- [S111 W1-2 CLOCKLOC1-CED dual-H frame](s111-w1-2-ced-dual-h-frame.md) — (C,E,D) triple closes PASS (|Λ−3H²|=2.91e-11, (D) well-posed); DUAL-H trap: use kinematic H≈0.26 for friction NOT √(V/3)≈289 (4-OOM over-drive); closure Λ=3H² frame-invariant
- [S112 W3-1 B5A bracketed causal-patch CLOSES](s112-w3-1-b5a-bracketed-causal-patch-closes.md) — FAIL (sign=PASS/mag=FAIL): Mach-13.75 one-directional white-hole causal patch leaves exit-slice microstate at EDGE undershoot R=0.530 (f_bulk=0.00396, captures 60/15237 nats); corridor "QES/island=A/4 via causal-patch" CLOSED; bracket [0.526,1.382] interior pinned at LOWER edge, NOT unity; anti-tautology held wide (FORBIDDEN f*=0.5536 far off); surviving route = two-sided TFD not single-sided exit slice
- [S114 W4-2 B5A TFD two-sided CLOSES](s114-w4-2-b5a-tfd-two-sided-closes.md) — FAIL (sign=PASS/mag=FAIL): the SURVIVING two-sided TFD route from S112 ALSO FAILs — doubling 2W/M gives f_bulk^TFD=0.009757, R_TFD=0.5347, still edge undershoot (|R−1|=0.465); A/4-via-causal-patch corridor CLOSES on BOTH single-sided AND two-sided-TFD; Mach-13.75 cone (sin θ_c=1/M=0.073) too narrow even doubled vs PASS band f∈[0.437,0.670]; B5A bracket trilogy S110/S111/S112/S114 COMPLETE (causal-patch routes); bracket basis = sbulk_primary 15236.71 NOT S_bulk_total 180723.4 (plan-label trap)
- [S115 W3-3 B5A TFD-QES OVERSHOOTS to 2A/4](s115-w3-3-b5a-tfd-qes-overshoots-2a4.md) — INFO (sign=PASS/mag=FAIL/regime=MARGINAL): the GENUINE two-sided QES (not the S114 causal-patch interpolant) gives R_QES=2.0001 — perfect-TFD cross-copy entanglement PURIFIES the single-sided bulk-EE → S_gen^TFD=2·Area/4 (monotone) → QES at boundary → 2·(A/4); OVERSHOOTS A/4 by the SECOND horizon (eternal-BH has 2 bifurcate horizons). No interior QES exists (monotone S_gen; regime MARGINAL, NOT VALID — float-noise sign-flip excluded by NEG_FLOOR). B5A microstate gap is STRUCTURAL across ALL island mechanisms: edge 0.526 / single-sided 1.382 / causal-patch 0.535 / two-sided-QES 2.000 — two-sided-island corridor CLOSED; A/4 is the full horizon count, GGE-relic island EE is a DIFFERENT functional
- [S116 W6 BC-fork HH layer-assignment](s116-w6-bc-fork-hh-layer-assignment.md) — Ψ(τ=0) BC adjudication (HH vs Vilenkin): converges to a LAYER ASSIGNMENT — HH is the WDW-constraint parent (S(τ), τ=0 S-min/regular South Pole, Neumann HT-2), "Vilenkin" the decohered outgoing WKB branch of Ψ_HH's classical limit. Eq. H-R3-1 (Sage-verified ∂_τJ=0): reflecting τ=0 datum → J=Im(Ψ*∂_τΨ)≡0 globally → real standing wave (HH-parent) even in s2 allowed region; fundamental J≠0 = answer-shopping + a Q45 choice. e-fold gap BC-INVARIANT (N_e=0.1734, flips exp(±B) sign not |B|=22.2552) → Track B; EFOLD-MAPPING-52 IC-indep scoped to s1; S70 routes count→TRANSIT-PS-67 (BC reaches only adiabatic cap). Residual = Q45 OPERATOR canonicity (S110-CF1 s1/s2 ρ_c≈13.41), two-stage CF-S117 (measure J at ρ_c under -BOTH). Convention -HH canonical/-BOTH diagnostic. My R3 on record; quantum-foam writes Turn-B verdict
- [S117 W5-2 WDW J≡0 family rigor](s117-w5-2-wdw-j-family-rigor.md) — INFO (designed): lifts the S116-W6 Neumann J≡0 to the WHOLE real self-adjoint (Robin) family on [0,τ_fold]. 4 Sage-exact boundary-form IDs (real-Robin⇒J(0)=0 ∀θ / dJ/dτ=Im(W)|Ψ|²=0 / Vilenkin J0=k|Ψ|²≠0 / separated-self-adjoint⟺Im(A1/A2)=0⟺real-Robin); J0_max_abs=0.0 across 181 θ. Two sharpenings: (1) E-INDEPENDENCE — theorem needs only W bounded near τ=0 NOT W(0)=0, so the W(0)=0 anchor is cosmetic (INFO = s63 grid τ_min=0.10 doesn't reach τ=0, extrapolated; NOT a theorem gap); (2) U(2) SCOPE — "Robin"=separated=admissible (J≡0); coupled/Bloch carry J≠0 but identify τ=0≅τ_fold (S¹) topologically excluded; Vilenkin non-self-adjoint=non-unitary excluded. J≡0 = no unitary amplitude leak through the τ=0 floor. Strengthens HH-UNCONDITIONAL cosmogenesis

## Core Equations (load-bearing for re-derivation)
- Hawking T = hbar*kappa/(2pi*k_B); Unruh T = hbar*a/(2pi*c*k_B)
- S_BH = A/(4*l_P^2); Page curve: S_rad = min{c*t, S_BH(t)}
- Island: S = min_I ext_{dI}[A(dI)/(4G) + S_bulk(I+R)]
- Bogoliubov: |beta|^2 = exp(-2pi*omega/kappa)*|alpha|^2; |alpha|^2 - |beta|^2 = 1 (bosonic)
- GH dS temp: T = H/(2pi); First law: dM = (kappa/8pi)dA + Omega_H dJ + Phi_H dQ

## Phonon-Exflation Framing (substrate-first)
- Spectral action = phonon free energy (identity not metaphor). V_CW = Helmholtz F(s,mu).
- Trans-Planckian universality: modified dispersion does not change thermal result (H-5).
- Jacobson 1995: Einstein eqs FROM thermodynamics. Euclidean path integral = Tr f(D^2/Lambda^2) on compact K.
- Direction of explanation: substrate -> emergent GR. NEVER invert. (S63 R2 framing-correction precedent.)

## Quick Reference: Task to Hawking Papers
- Spectral action / V_eff: 07, 03, 09. Particle creation: 05, 12, 07.
- Entropy counting: 11, 07, 14. Information in KK: 06, 14, 13, 10.
- CRITICAL: 03, 04, 05, 07, 11, 12, 14.

## Permanent Retractions (prevents re-derivation)
- HP first-order BCS, no-boundary, B-H area law, entropy staircase, NG mode, Schwinger-instanton (S26-39)
- Permanent GGE relic, preheating w/o reheating, HP at fold, trace anomaly O(N) (S39)
- E-FINAL, T-ACOUSTIC, H_0=68.8, N_factor sqrt(16) convergence (S40/S60)
- CC impedance mismatch, Model E BCS splitting, metastability=CC (S63)
- Monotonicity hierarchy rigid chain->tree (S64). Area explains substrate (inverted, S63/S64).
- W1-E subsonic Mach (dim error, S64). R-G dephasing as moduli stabilization (S73B).
- H1 dispersive group-velocity greybody (S73B). Weyl protection conjecture (S71).

## Pre-Registered Gates (still active for Hawking)
- H-66-1: AMPLITUDE-NORM. Rigorous A_s from GGE graph modes. |log10(A_s/A_s^obs)|<1.0.
- H-66-2: TENSOR-TILT-TRANSFER. n_T at CMB via GGE transfer. n_T(k_CMB)>0.

## Hawking-Specific Methodological Notes
- Bogoliubov computations: always verify normalization |alpha|^2 - |beta|^2 = 1.
- Limiting cases checklist: flat space (no particles), Schwarzschild (T=1/8piM), de Sitter (T=H/2pi).
- Stress-energy conservation: nabla_mu T^{mu nu} = 0 (possibly with anomaly).
- Energy conditions: state which (weak/strong/dominant/null) and quantum-regime validity.
- For substrate analogs: identify TWO-COMPONENT mixture (thermal from horizon + coherent from squeeze) when applicable; substrate is one-sided horizon spectrum (Israel TFD with squeezed initial state).
- Page curve check: S_rad against min{c*t, S_BH(t)} trajectory.
- Container-thinking trap: "in curved spacetime" -> reframe as "fiber spectrum reorganizes."
- Analog-T surface-gravity disputes: separate TWO orthogonal axes BEFORE adjudicating - (a) WHICH surface (tau value), (b) WHICH kappa-convention. Two corpus conventions: Visser/BLV kappa=(1/2)|d_n(c^2-v^2)| = c_s*|dv/dn| at v=c (carries factor c, Sage-exact under const c) vs bare velocity-gradient kappa_v=|dv/dtau| (NO factor c, S73A/S71). They differ by exactly c_BLV=0.485. An apparent "25x discrepancy" can be surface-tau ratio x convention-factor placement. S95 W4: corpus "entry temperature"=72.8 M_KK is BARE kappa_v at a2-kinematic tau=0.2195; W4-1's 2.948 is Visser kappa at distinct BLV-discriminant tau0=0.1125 (NOT a competing entry-T, NOT an artifact).
- Analog-T KIND-tagging (THIRD axis, beyond surface-tau + kappa-convention): at the SAME tau, distinct surface-gravity FUNCTIONALS coexist WITHOUT contradiction. The reader-trap is collapsing them into one functional. Three KINDs at tau_fold=0.190: THERMODYNAMIC-modulus (kappa_V=1/2|V'|=0 double-root on the 2D Jensen-modulus potential metric, V=V'=0/V''=2>0, s85_w6 kappa_at_dump=0.0) / GIBBONS-HAWKING-emergent (T_GH=0.2172 on the emergent 4D acoustic horizon, a2 channel, exp(-2tau)/pi; s29c GATE is FAIL on T_GH-vs-T_eff RATIO but the VALUE 0.2172 reproduces) / SONIC (0.112 M_KK = v=c_BLV Mach-1, internal-acoustic). kappa_V (modulus metric) and T_GH (emergent horizon) are DIFFERENT geometric objects -> NOT two values of one functional.
- 0.112 M_KK RELABEL: S53/S63 "GGE relic temperature" (s53_phonon_eos_output.txt) = internal-acoustic SONIC surface, NOT the observed relic temperature. OBSERVED relic spectral T = a4 value 7.578 M_KK (=T_eff/T_compound PROVEN S75, condensation-exit; distinct from a4_fold=1350.72 the dimensionful SDW coeff).
- KITAEV identity 2pi*T(a4)=kappa_exit: 2pi*7.578=47.614=kappa_exit (a4-row surface gravity 47.61). MSS chaos-bound saturation 2piT IS the analog surface gravity kappa at the a4 exit surface. Exflation = horizon process (kappa real on emergent metric) that is NON-CHAOTIC (lambda_L=0) -> causal/thermodynamic edges, not scrambling edges. (S96 W7-6 PASS.)
- Greybody-vs-freeze-in double-derivation (S100a W3-10 INFO, sign=PASS): with ONE scalar omega pin, E_A=2pi*omega/kappa_SONIC is C2-FLAT while E_B=S0*C2 is C2-LINEAR -> scalar pin can only straddle the heavy pair, never close 10% on both; exact closure needs Casimir-graded offsets omega_i=S0*C2_i*T_acoustic. Found: S0_fit*T_acoustic=0.18975 = tau_fold to 0.13% (the omega-match per-Casimir quantum IS the fold position) -> graded closure would have zero free params if W3-11 threshold identity lands. kappa_SONIC=28/125*pi=0.70372 (5sf Sage-exact from canonical T_acoustic=0.112, SONIC KIND only); a "0.7048" literal in circulation is transcription drift, REJECTED.

## Cross-Reference Pointers (do not duplicate, query instead)
- Permanent theorems list, observational results, gate verdicts: `sessions/permanent-results-registry.md` + `mcp__knowledge__.search_knowledge(...)`
- Closed mechanisms (27+ equilibrium, 5/5 baryogenesis): `mcp__knowledge__.list_entities("closed")`
- Canonical constants (M_KK, tau_fold, Delta_BCS, T_H, kappa values): `mcp__knowledge__.get_constant(name)`
- Past session results S29-S75: query `mcp__knowledge__.search_knowledge(topic)` and `tools/knowledge.db`
- Falsifier inventory + cross-pillar bridges: `sessions/framework/registry/`
