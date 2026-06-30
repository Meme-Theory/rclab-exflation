---
name: S80 Results Cluster (M_KK Pin + CC-Ratios-Only Theorem)
description: S80 W0-8 M_KK axiomatic pin documentation + S80 W1-4 CC-Ratios-Only Theorem (§VII.I candidate)
type: project
---

## S80 W0-8: M_KK Structural-Role Documentation -- PASSED

### Core Result
M_KK is the AXIOMATIC SOLE external dimensional pin. All other mass/length/time/energy scales derive from M_KK via Chamseddine-Connes spectral action on almost-commutative spectral triple (C^inf(M_4) ⊗ A_F, L^2(S) ⊗ H_F, D_M ⊗ 1 + γ_5 ⊗ D_F).

### Citation Anchors (literature-permanent)
- **CC96 sec 4** (Chamseddine-Connes 1996, Commun. Math. Phys. 186 731-750, hep-th/9606001): fixes Λ as SINGLE dimensional generator of Tr f(D^2/Λ^2) ~ 2*f_4*Λ^4*a_0 + 2*f_2*Λ^2*a_2 + f_0*a_4. Newton-constant pin: 1/κ_0^2 = 4*f_2*Λ^2/π^2.
- **CCM 2007 sec 1.17-1.20** (Chamseddine-Connes-Marcolli, Adv. Theor. Math. Phys. 11 991-1089, hep-th/0610241): Λ as unification scale; gauge BCs g_1^2 = g_2^2 = (5/3)*g_3^2; Higgs quartic λ_0 = (π^2/(2*f_0))*b/a^2; non-minimal ξ_0*R*|H|^2 coupling.
- **CC96 sec 7.3**: Λ ≡ M_KK (Kaluza-Klein compactification mass = 1/R_K).

### Derivation-Category Structure
Every dimensional Q = R · M_KK^m where R is dimensionless D_K-ratio:
- m = 2: energies from a_2 (Newton's constant, Higgs mass)
- m = 4: vacuum-energy densities from a_0 (ρ_Λ_spectral)
- m = 0: dimensionless (n_s, α_s, sin^2(θ_W), τ_fold)
- m = -1: lengths (l_phonon, ξ_BCS, R_K)

### Residual Ambiguities (non-blocking)
- CF-2 cites arXiv:0706.3688 for CCM 2007 while corpus has hep-th/0610241 (same body of work; primary preprint vs companion).
- CCM 2007 sec 1.17-1.20 maps to corpus-transcription sec 3.1-3.4.
- Single-pin |{M_i}| = 1 claim pending S80-FRAMEWORK-SINGLE-PIN-VERIFICATION (CF-4) for v_ew + m_H_obs derivation-path audit.

**Apply**: Cite CC96 sec 4 + CCM 2007 sec 1.17-1.20 jointly. When classifying constants RATIO vs ABSOLUTE, apply Q = R · M_KK^m. Do NOT relabel M_KK as "input" or "free parameter".

## S80 W1-4 CC-Ratios-Only Theorem -- PROVEN (2026-04-17, §VII.I candidate)

### Theorem
Weight-balanced combinations of Seeley-DeWitt moments and Mellin moments of regulator f in CC96 eq 2.11 are spectral-triple invariants (f-independent).

### Application Protocol
Express observable as polynomial E = C(a) · ∏_k (f_k)^{q_k} in SDW moments a_n(D^2) and Mellin moments f_k.
1. Check weight-balance: q_k(E) = Σ_{i: M_i = f_k} p_i = 0 for every Mellin-index k ∈ K_d.
2. If q_k = 0 ∀k: f-invariant (PASS).
3. If any q_k ≠ 0: f-dependent; must specify scheme.

### Cases
- **(i)** Pure a-ratios ∏ a_{n_i}^{p_i} are trivially weight-balanced. PASS.
- **(ii)** Weighted Q_m/Q_n with m ≠ n is f-dependent (52% spread across 3 regulators).
- **(iii)** Task-prompt R_{m,n} = (a_m/a_n)·(f_n/f_m) admits two readings; Reading A reduces to Case (i), Reading B is counterexample (73% spread).

### Dimensional closure (|{M_i}| = 1)
For pure a-ratio dimensionless: Σ_i p_i(d − n_i) = 0. P4-D CN-CV3 single-pin requirement with M_KK as sole external dimensional scale.

### Scope caveat
Level-1 (full Hilbert trace) only. Level-2+ protection (dim H_π ≥ 2 criterion CN-EM3) is SEPARATE theorem -- S80 CF-5.

### Sanity check (`computations/s80_cc_ratios_proof_sanity.py`)
- spread(a_0/a_2 across 3 regulators) = 0 exactly (algebraic identity)
- spread(a_0·a_4/a_2^2 across 3 regulators) = 0 exactly (R_1 is Theorem Case (i))
- spread(Q_0/Q_2) = 0.5176 (f-dependent)
- spread((a_0/a_4)·(f_4/f_0)) = 0.73 (Reading-B counterexample)

### Files
- Primary proof: `sessions/archive/session-80/session-80-results-workingpaper.md §W1-4`
- Alt proof: same file §W1-4-alt (spectral-geometer)
- Python sanity: `computations/s80_cc_ratios_proof_sanity.py`
- Verdict: `computations/s80_gate_verdicts.txt`
- Draft §VII.I: embedded in workingpaper §W1-4

### Cross-references
P4-D CN-EM1/CN-CV1 (`sessions/archive/session-79/workshops/p4-d-ratios-vs-absolutes-meta.md:1469-1493`); Connes-Moscovici 1995 (researchers/Connes/06); CC96 eq 2.11 (07); CCM 2007 §3.1 (10).

### Task-prompt clarification
The literal R_{m,n} = (a_m/a_n)·(f_n/f_m) is ambiguous. INTENDED reading (A) -- "correction factor cancels explicit f-normalization in Q_m/Q_n" -- reduces to a_m/a_n which IS f-independent. LITERAL-INDEX reading (B) is counterexample. Honest theorem statement is P4-D CN-EM1: pure a-ratios are f-independent; weight-balance (q_k = 0 ∀k) is the general condition.

**Load-bearing**: Every framework prediction classified "structural from CCM" in permanent-results-registry §VII inherits this theorem as formal scheme-invariance proof. PUBLISHABLE regardless of framework physical-fate. JGP/CMP target.
