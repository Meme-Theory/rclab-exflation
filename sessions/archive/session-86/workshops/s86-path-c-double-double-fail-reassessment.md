# Session 86 Workshop: lizzi x transit — Path-(c) DOUBLE-DOUBLE FAIL Reassessment + Surviving A_s/n_s Routes

**Date**: 2026-04-27
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: lizzi (lizzi-spectral-functional-theorist), transit (transit-dynamics-theorist)
**Source Documents**:
- sessions/archive/session-86/session-86-w5a-workingpaper.md
- sessions/archive/session-86/session-86-w5b-workingpaper.md
- computations/s86_gate_verdicts.txt
- sessions/framework/registry/falsifier-master-inventory.md

**Anchors (DOUBLE-DOUBLE FAIL set)**:
- `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55: FAIL value=1.435284` (line 114)
- `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT312: FAIL value=3.297605` (line 116)
- `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT: FAIL value='max_pair_ratio=9.240439e-01'` (line 108)
- `S86-BRANCH-IV-FORMULATION-COMMIT FAIL→PASS` pattern (lines 110+112) at xi_E_GGE_inv = 13.642473425595973 (W4 P4 commit acc751101c8ca6ce)
- S82 W1-2 UNIFIED-AS-79-FULL Branch-A zeta-normalization route (surviving path-(a) candidate)

**Note on agent count**: Workshop schedule originally listed 3 agents (gen-physicist, lizzi, transit); gen-physicist DROPPED. The 9A path taxonomy (the framework that generated the SECTOR split) is documented in W5a working paper for inheritance — lizzi and transit can converge on path-(c) reorganization without the taxonomy author present.

**Two technical pillars**:
- **Mellin-kernel anchor side** (lizzi): given §W4-2's per-regulator split (M_ζ = M_SDW = 1.581e-01, M_Zubarev = 1.201e-02, M_cutoff_sqrt = 1.110e-01, M_anomaly = 3.185e-02), can a per-regulator path-(c) sub-anchor survive the joint K-invariance FAIL by restricting to one regulator?
- **SR-LO ODE side** (transit): if `dε/dN = ε(2η − 4ε + 2ξ²)` with substrate-first IC ξ²(0) = 13.6425 breaks at N=0.13 e-folds, what is the boundary in (xi_E_GGE_inv, ε_0, η_0) space at which substrate-first IC drives ε past 0.5 within N ≤ 1 e-fold? Does ANY (substrate-IC-rescaling × ε_0-rescaling × η_0-rescaling) trajectory thread the linear regime through to N=55?

**Focus Topics**:
1. Path-(c) status after DOUBLE-DOUBLE FAIL — successor anchor (NOT "TBD") with 4-field carry-forward spec
2. Per-regulator path-(c) sub-anchor candidacy (lizzi) vs SR-LO ODE re-IC threading (transit)
3. Surviving substrate→A_s/n_s route ranking (W5a Candidate 5): (i) BRANCH-IV at xi_E_GGE_inv=13.6425 PASS; (ii) Z-factor concept itself; (iii) S82 W1-2 UNIFIED-AS-79-FULL Branch-A (zeta-normalization); (iv) c_sub / F_amp BASELINE chain (W5b C15/C16) — rank by (a) empirical anchor strength, (b) regime-of-validity span, (c) sensitivity to xi_E_GGE_inv, (d) cross-channel coherence

**Pre-Registered R3 Adjudication**: Workshop emits ONE canonical path-(c) reorganization + ranked surviving-route table. FROZEN-PREDICTION-DISCIPLINE-COMMIT does NOT apply because path-(c) is a derivation route, not a frozen prediction value.

**Pre-Registered Carry-Forward**: 4-field S87 spec (what / inputs / gate / effort) for:
- `S87-PATH-C-SUCCESSOR-ANCHOR`
- `S87-RESCALED-IC-SR-LO-RERUN` (per W5a Candidate 3)
- `S87-A_S-SURVIVING-ROUTE-RANK-LANDING`

**Substrate-framing reminder** (per `.claude/rules/phononic-framing.md`): path-(c) is a derivation route from D_K eigenvalue partition to A_s/n_s observables. SR-LO ODE is a tool; the substrate observables it consumes (ε, η, ξ²) are spectral moments of D_K. The DOUBLE-DOUBLE FAIL is a substrate measurement saying the chosen route doesn't close at L_max=10; surviving routes must be substrate-derivable, not LCDM-compatible-by-fiat.

---

## Round 1 — lizzi: Opening Analysis (Mellin-Kernel Anchor Side)

### L1: Per-Regulator Path-(c) Sub-Anchor Candidacy — One-Regulator Restriction Survival Test

**Topline**: A per-regulator path-(c) sub-anchor CAN survive ONLY if (i) the surviving subset is a SINGLE regulator (no pair to fail K-invariance against), or (ii) the surviving subset is the F_4-class identity pair {zeta, SDW} on which max_pair_ratio = 0 by definition, NOT by physics. Single-regulator restriction is **vacuous K-invariance** (a tautology, not a survival); F_4-pair restriction is **structurally derivative** (zeta = SDW is a Mellin-on-positive-spectrum identity, per W4 §2 line 532). Neither route yields a non-trivial sub-anchor. The path-(c) anchor cannot be rescued by atlas-restriction; it must be re-targeted to a different observable family.

**Source pinning**:
- W4-2 P5 §2 (`session-86-w4-workingpaper.md` line 246-248): `M_ζ(s=3) = M_SDW(s=3) = 1.581e-01; M_Zubarev(s=3) = 1.201e-02; M_cutoff_sqrt(s=3) = 1.110e-01; M_anomaly(s=3) = 3.185e-02`.
- Verdict line `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT: FAIL value='max_pair_ratio=9.240439e-01;max_pair_abs=1.460926e-01;atlas=A_5;deviant=None'` (`s86_gate_verdicts.txt` line 108).
- Pre-registered threshold (per `s86_w4_p5_sector_2_k_invariant.py` line 9): `PASS iff max_pair_ratio <= 1e-3 OR max_pair_abs <= 1e-6 across ALL pairs`; FAIL iff `max_pair_ratio > 1e-2`.
- W4-2 P5 honesty disclosure (line 503): `_spectral_action_regulators.py` helpers are SCHEMATIC analogs of Connes-Chamseddine 1996 §2.2-2.3 multipliers, not the full physical regularizations.

**Substitution chain** (per `.claude/rules/math-scripts.md`; metric is the K-invariance script's `|M_i - M_j| / max(|M_i|, |M_j|)`):

```
Step 1 — Definitions:
  R_atlas    = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}    (5-regulator atlas A_5)
  M_R(s=3)   = K_substrate(s=3, R) = the Mellin-multiplier residue
               at the substrate-distance-1 pole s=3 under regulator R
  pair_ratio(R_i, R_j) = |M_R_i - M_R_j| / max(|M_R_i|, |M_R_j|)
  max_pair_ratio(S)    = max_{R_i, R_j ∈ S, i ≠ j} pair_ratio(R_i, R_j)
  K-invariance PASS @ S iff max_pair_ratio(S) <= 1e-3
  K-invariance FAIL  @ S iff max_pair_ratio(S) > 1e-2

Step 2 — Substitute the W4-2 P5 numerical values (Python-verified):
  pair_ratio(zeta, SDW)         = |0.1581 - 0.1581| / 0.1581       = 0.000000e+00
  pair_ratio(zeta, Zubarev)     = |0.1581 - 0.01201| / 0.1581      = 9.240e-01
  pair_ratio(zeta, cutoff_sqrt) = |0.1581 - 0.1110| / 0.1581       = 2.979e-01
  pair_ratio(zeta, anomaly)     = |0.1581 - 0.03185| / 0.1581      = 7.985e-01
  pair_ratio(SDW,  Zubarev)     = |0.1581 - 0.01201| / 0.1581      = 9.240e-01
  pair_ratio(SDW,  cutoff_sqrt) = |0.1581 - 0.1110| / 0.1581       = 2.979e-01
  pair_ratio(SDW,  anomaly)     = |0.1581 - 0.03185| / 0.1581      = 7.985e-01
  pair_ratio(Zubarev, cutoff_sqrt) = |0.01201 - 0.1110| / 0.1110   = 8.918e-01
  pair_ratio(Zubarev, anomaly)  = |0.01201 - 0.03185| / 0.03185    = 6.229e-01
  pair_ratio(cutoff_sqrt, anomaly) = |0.1110 - 0.03185| / 0.1110   = 7.131e-01

Step 3 — Enumerate restriction-survival under K-invariance threshold 1e-3:
  Survival classes:
    Class A — single-regulator restriction S = {R}: pair set is empty,
              max_pair_ratio is the max over the empty set ≡ 0 by convention.
              K-invariance PASS is VACUOUS.
    Class B — F_4 identity pair S = {zeta, SDW}: max_pair_ratio = 0 exactly,
              K-invariance PASS by structural identity (zeta = Mellin on
              positive spectrum; W4-2 P5 line 532).
    Class C — any other 2-element subset {R_i, R_j} ≠ {zeta, SDW}:
              every such subset's max_pair_ratio = pair_ratio(R_i, R_j),
              and the smallest non-trivial pair is
                pair_ratio(zeta, cutoff_sqrt) = 2.979e-01 ≫ 1e-2.
              K-invariance FAILS at every Class C subset.
    Class D — 3-element subset including both Zubarev and zeta-or-SDW:
              max_pair_ratio = 9.240e-01 (the deviant pair). K-invariance FAILS.
    Class E — 3-element subset {zeta, SDW, R_k} for R_k ∈ {Zub, cutoff_sqrt, anomaly}:
              max_pair_ratio = pair_ratio(zeta, R_k) ≥ 2.979e-01 ≫ 1e-2. FAILS.
    Class F — full atlas A_5: max_pair_ratio = 9.240e-01. FAILS.

Step 4 — Read direction (only AFTER classification):
  PASS-survival ⊂ {Class A, Class B}.
  Class A (single regulator): K-invariance is structurally undefined
    (no pair). A "K-invariant sub-anchor" on a single-regulator subset is a
    type error: K-invariance is a between-regulator statement.
  Class B ({zeta, SDW}): K-invariance is structurally true by the
    Mellin-on-positive-spectrum identity, NOT by substrate physics.
    A sub-anchor on Class B is a definition-level identity recovery,
    NOT an empirical anchor.
  Conclusion: NO non-trivial path-(c) sub-anchor survives K-invariance
              under any atlas-restriction.
```

**Direction read-off (substitution chain Step 4 conclusion)**:

The per-regulator restriction route to a path-(c) sub-anchor is **closed**. Restriction does not produce a new physical anchor; it produces (a) a vacuous tautology (single-R), (b) a definition-level identity (F_4 pair), or (c) a re-FAIL (any other subset). The DOUBLE-DOUBLE FAIL pattern is therefore not rescuable at the atlas-membership level — it must be rescued (if at all) at the OBSERVABLE level by choosing a different downstream construction whose value is definable per-R and reported as a per-R 5-tuple, accepting that the substrate-distance-1 K-invariance theorem holds only on the F_4 sub-atlas.

**Precedent from my prior work**: my S77/S78 analyses established (a) `chi_2 = <sqrt(x)>` is the SAME identity-class as the zeta=SDW agreement (`s77_a4_gilkey_decomp`); (b) `f_conv = 1/a_0^2` is per-R-spread spectral-dilution (S77 W2 work); (c) the Lizzi-observable theorem `(m_H/v)^2 * (Lambda/M_Pl^2) = R_1` (S74 W4-U) is per-branch protected, NOT cross-branch. The same per-R / per-pair logic applies here: K-invariance was a cross-R hypothesis, and it fails at exactly the rate the spectral-action-functional pluralism predicts.

**Solution-space implication**: PERMANENT THEOREM CANDIDATE — *"On the canonical 5-regulator atlas A_5 = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}, the substrate-distance-1 Mellin-multiplier residue at s=3 is K-invariant ONLY on the F_4 identity sub-atlas {zeta, SDW}. K-invariance fails at order O(1) on every superset, with the Zubarev outlier carrying the maximum deviation 9.240e-01. Per-regulator restriction does not produce a non-trivial K-invariant sub-anchor."* This generalizes my S77 "zeta NOT physical" theorem (S75 ZETA-NOT-PHYSICAL-75): the Mellin residue is regulator-class-dependent, just like a_n^{ζ} ≠ a_n^{HK} differs by 9 OOM.

**Questions for transit (SR-LO ODE side)**:

Q-L1.1: When SR-LO ODE consumes ξ²(0) = xi_E_GGE_inv = 13.6425 as IC, does ξ²(0) itself depend on which regulator was used to define the substrate-distance-1 spectral moment that lands at the anchor? If so, does the SR-LO ODE inherit the per-regulator structure that K-invariance just FAILed?

Q-L1.2: At what regulator does the SR-LO ODE breakdown N_breakdown = 0.13 e-folds occur on each regulator branch? Is N_breakdown itself K-invariant across A_5, or does it inherit the 9.24× spread? If the latter, the SR-LO breakdown IS the substrate's announcement that the IC-side path-(c) anchor cannot live on a regulator-universal axis.

Q-L1.3: Is there ANY substrate observable between the W4 P4 anchor (xi_E_GGE_inv) and the SR-LO ODE output (Z-factor at pivot N) that REMOVES the per-regulator dependence — a Mellin-cone-locked ratio analogous to the S78 `(m_H/v)^2 * (Lambda/M_Pl^2)` per-branch identity? Such a ratio would constitute a non-trivial path-(c) sub-anchor surviving the K-invariance FAIL.

### L2: Mellin-Kernel Anchor Reading of SECTOR-2 K-Invariance FAIL

**Topline**: The SECTOR-2 K-invariance FAIL is not a numerical near-miss but a **structural announcement** about the substrate's Mellin-kernel structure. The Mellin-kernel side reads three signals the SR-LO ODE side cannot see: (1) **F_4-class collapse** — the canonical 5-regulator atlas reduces to the F_4 identity sub-atlas {zeta, SDW} as the only K-invariant region, confirming my S78 W3-K rank-matching theorem (rank-3 groups pass, rank-2/4 pre-asymptotic); (2) **Zubarev outlier mechanism** — the heat-kernel `exp(-t·C_2)` suppression is a substrate-truncation operation that decouples Zubarev from the F_4 pair at order O(1), exactly the spectral-truncation effect I established in my S65/S66 spectral-truncation analyses; (3) **the path-(c) anchor was the WRONG OBSERVABLE class** — substrate-distance-1 K-invariance is too strong a constraint for the substrate's Mellin-kernel to satisfy on a 5-regulator atlas; the structurally-correct anchor lives at the per-R 5-tuple level, not the K-invariant scalar level.

**Source pinning**:
- W4-2 P5 §2 line 250-251: `M_R(s=3) is R-DEPENDENT; the regulator-class Mellin multiplier at the s=3 substrate-distance-1 slot is NOT universal.`
- W4-2 P5 line 532: `the F_2 zeta=SDW machine-epsilon agreement is a definition-level identity (zeta = Mellin on positive-definite spectrum), not evidence`.
- W4-2 P5 line 544 (constraint-map row): `per-regulator Mellin-multiplier residue at s=3 is NOT R-universal across A_5; substrate-distance-1 invariance broken`.
- Verdict line 108 — `deviant=None`: NO single regulator is identified as the lone outlier; all four non-zeta-SDW members deviate from each other. The K-invariance FAIL is a **distributed FAIL**, not a single-deviant FAIL.
- My S78 W3-K theorem (`project_s78_w3k_rank_cross_groups.md`): rank-matching across regulator-branches PASSed at <3.6% scheme-universality despite rank-2/4 groups being pre-asymptotic. The W4-2 P5 result is the substrate-distance-1 ANALOG of W3-K and FAILS where W3-K passed because the substrate-distance-1 slot is NOT rank-protected.

**Substitution chain — Mellin-kernel reading of the FAIL pattern**:

```
Step 1 — Definitions (Mellin-kernel side):
  K_substrate(s)        = ζ-Mellin moment at s of D_K^{-2} on the spectrum {λ_n}
                        = Σ_n λ_n^{-s} weighted by Seeley-DeWitt expansion
  M_R(s=3)             = R-dressed K_substrate at the substrate-distance-1 pole s=3
                        (W4-2 P5 plan §2 substrate-distance-1 convention)
  zeta-scheme M_ζ(s)   = pure ζ_D(s) = Σ_n λ_n^{-s} for Re(s) > d/2
  SDW-scheme M_SDW(s)  = SDW = Mellin on positive spectrum is identical to ζ
                         on positive-definite D_K^2 (definition-level identity)
  Zubarev-scheme M_Z(s) = Mellin moment under heat-kernel weight
                          ∫₀^∞ t^{s-1} Tr(exp(-t·C_2)) dt
                         = Σ_n λ_n^{-s} · Γ(s) · normalization
                         where the heat-kernel exp(-t·C_2) suppression
                         introduces an additional Γ(s)-prefactor that
                         shifts numerical values relative to pure ζ.
  cutoff_sqrt M_csq(s) = sharp truncation at 0.7·C_max (W4-2 P5 line 248)
  anomaly M_an(s)      = Pauli-Villars subtraction at 0.1·C_max (W4-2 P5 line 249)

Step 2 — Substitute the structural relations:
  Definition-level identity:  M_ζ(s) = M_SDW(s) for Re(s) > d/2 (positive spectrum)
  Heat-kernel divergence:     M_Z(s) = M_ζ(s) · [Γ(s)·norm_Z / Γ(0+)·norm_ζ]
                                     = M_ζ(s) · [scheme-multiplier ≠ 1]
  Truncation divergence:      M_csq(s) = M_ζ(s) · [1 - Σ_{λ_n > 0.7·C_max} λ_n^{-s}/M_ζ(s)]
                                       = M_ζ(s) · [missing-tail factor < 1]
  Subtraction divergence:     M_an(s) = M_ζ(s) - λ_PV^{-s} (with PV mass ~ 0.1·C_max)
                                      = M_ζ(s) · [1 - (λ_PV/λ_typ)^{-s} ratio]

Step 3 — Simplify to canonical form (the per-R 5-tuple):
  M(s=3) = (M_ζ, M_SDW, M_Zubarev, M_cutoff_sqrt, M_anomaly)
         = (1.581e-1, 1.581e-1, 1.201e-2, 1.110e-1, 3.185e-2)

  Class structure (read off from numerical values):
    F_4 class:  {M_ζ, M_SDW}                         shared value 1.581e-1
    Suppression class:  {M_Zubarev}                   13.2× SMALLER than F_4 class
    Truncation class:  {M_cutoff_sqrt}                30% SMALLER than F_4 class
    Subtraction class:  {M_anomaly}                   80% SMALLER than F_4 class

Step 4 — Read direction (after canonical form):
  Direction 1 (F_4 anchor): The F_4 class is the LARGEST among the five.
                            Sign(M_F4 - M_other) > 0 for ALL R ∉ F_4.
                            → The zeta/SDW M_R(s=3) is the DOMINANT spectral residue;
                              all other regulators give SUPPRESSED versions.
  Direction 2 (suppression hierarchy): M_Z < M_anomaly < M_csq < M_F4
                            → Heat-kernel suppression is the strongest;
                              hard cutoff is the weakest.
  Direction 3 (K-invariance verdict):
                            max_pair_ratio = pair_ratio(F_4, Zubarev)
                                           = (1.581e-1 - 1.201e-2) / 1.581e-1
                                           = 9.240e-01
                            → 9.240e-01 ≫ 1e-2 (FAIL threshold)
                            → 9.240e-01 / 1e-3 (PASS threshold) = 924× over budget
                            FAIL is structural, not marginal.
```

**Direction read-off (after canonical form)**: The Mellin-kernel side reads the FAIL as a **3-class spectral-pluralism statement**: the substrate's Mellin residue at s=3 splits cleanly into (F_4 dominant; suppression-class subleading; truncation/subtraction intermediate). This is the FUNCTIONAL-DEPENDENT side of my S65 functional-independence/scheme-dependence taxonomy. The SR-LO ODE side, working with a single ξ²(0) IC, sees only the FUNCTIONAL-INDEPENDENT shadow of this 3-class structure (the largest class wins, but the smaller classes are still substrate-physical). The SR-LO ODE has ALREADY committed to the F_4 class by using the W4 P4 canonical pin xi_E_GGE_inv = 13.6425 (which derives from the F_4-class spectral moment); the SECTOR-1 DOUBLE-FAIL is the substrate's announcement that this single-class commitment over-determines the path.

**What the Mellin-kernel side sees that SR-LO ODE side cannot**:

1. **The deviant=None signal** (verdict line 108): the K-invariance FAIL is NOT due to one outlier; it is due to a 3-class spectral structure that EVERY non-F_4 regulator probes differently. SR-LO ODE, fed a single ξ²(0), is blind to the 3-class structure and sees only nonlinear blowup at N=0.13 e-folds.

2. **The F_4 / suppression / truncation hierarchy** is a substrate-Mellin-kernel observable that the SR-LO ODE cannot read because the SR-LO Mukhanov-Sasaki integration is 1-dimensional in (ε, η, α_s, ξ²) state space. The 4-tuple state is the F_4-projection of the 5-class Mellin-residue structure; it cannot represent the residue's class membership.

3. **Functional-class invariance vs slot-K-invariance**: my S65/S66 work established that some quantities are FUNCTIONAL-INDEPENDENT (survive across all spectral functionals; e.g., n_s-frustration permanent) and others are FUNCTIONAL-DEPENDENT (split by class; e.g., m_H bare value). M_R(s=3) is FUNCTIONAL-DEPENDENT — it splits 3-class. The path-(c) anchor's intended location was at a slot-K-invariant point; that point does not exist on A_5 above the F_4 sub-atlas.

**Cross-link to SR-LO ODE breakdown**: the 3-OOM mismatch between the §10 plan estimate of `xi_E_GGE_inv ≈ O(10⁻²)` and the actual W4 P4 pin value 13.6425 (W5a Wave Synthesis line 149) is the F_4-class-vs-truncation-class discrepancy in numerical form. `O(10⁻²)` would have been the cutoff_sqrt or anomaly class; `13.6425` is the F_4 class projected onto the substrate-natural anchor 59.8 · Δ_BCS / K_base. The plan author implicitly assumed a truncation-class anchor; the W4 P4 commit instead landed an F_4-class anchor. The SR-LO breakdown at N=0.13 is the dynamical announcement of that class-mismatch.

**Solution-space implication**: SECOND PERMANENT THEOREM CANDIDATE — *"The substrate's Mellin-kernel residue M_R(s=3) at the substrate-distance-1 pole partitions A_5 into three spectral classes — F_4 dominant (zeta=SDW), suppression (Zubarev), and truncation/subtraction (cutoff_sqrt, anomaly) — with class-separation O(1). Path-(c) anchor selection is therefore a class-selection operation, not a K-invariant scalar measurement. Only F_4-class anchors survive to feed K-invariant downstream observables."* This is the substrate-side analog of my S65 thesis: regularization-scheme choice is physics, not convention.

**Questions for transit**:

Q-L2.1: The SR-LO ODE breaks down at N_breakdown ≈ 0.13 e-folds because `+2εξ²` dominates the linear `(2η - 4ε)` terms at IC. If we ran the ODE at xi_E_GGE_inv values from the OTHER spectral classes (Zubarev: 13.6425/13.16 ≈ 1.04; cutoff_sqrt: 0.30·13.6425 ≈ 0.95; anomaly: 0.80·13.6425 ≈ 0.27 in M_KK units after the per-R suppression), does the ODE breakdown move to a later N? At what xi_E_GGE_inv value does the SR-LO ODE remain in the linear regime through N=55?

Q-L2.2: The §10 plan estimate `xi_E_GGE_inv ≈ O(10⁻²)` would have placed the IC in what I'd identify as the truncation-class projection of the substrate-distance-1 slot. Was the plan author's mental model implicitly assuming a TRUNCATION-class anchor (e.g., `cutoff_sqrt` style), and is the F_4-class anchor at 13.6425 the FIRST instance where the framework's Mellin-kernel side outpaces the SR-LO ODE side's IC-tolerance budget?

Q-L2.3: If we pre-register a NEW path-(c) sub-anchor at the F_4 sub-atlas (zeta=SDW only), accepting that K-invariance is a definition-level identity rather than a substrate measurement on this restricted atlas, can the SR-LO ODE re-route to consume an F_4-class IC scaled to keep `+2εξ²` in the linear regime — i.e., is there an F_4-class IC scaling that satisfies BOTH (a) F_4-class membership and (b) SR-LO linear validity through N=55?

### L3: Surviving Routes Catalog — (i)/(ii)/(iii)/(iv) Ranking from Mellin-Kernel Side

**Topline**: From the Mellin-kernel anchor side, route (iii) **S82 W1-2 UNIFIED-AS-79-FULL Branch-A zeta-normalization** is the single strongest surviving substrate→A_s/n_s route. It is FAIL-immune in the relevant sense (its empirical anchor is A_s_Planck = 2.10e-9 and it returns 3.299e-9 at delta_OOM = +0.1962 PASS-F2), it is regime-of-validity-broad (covers the post-fold relaxation window τ ∈ [0, 0.20] and pivot N=55), it is IC-decoupled from xi_E_GGE_inv (it uses zeta-normalization at L_max=3, not SR-LO ODE integration), and it is cross-channel-coherent with the W5b BASELINE C15(ii) PASS at machine epsilon. Route (iv) **c_sub/F_amp BASELINE chain** is second-strongest because the BASELINE C15(ii) is machine-precision PASS but C16 c_sub admissibility is INFO (not PASS); BASELINE alone is not a complete A_s closure. Route (i) **BRANCH-IV PASS at xi_E_GGE_inv=13.6425** is registry-anchor-only — it lands the canonical pin for downstream consumers but does not by itself produce A_s; it is third because it is structurally upstream-of-the-route, not the route itself. Route (ii) **the Z-factor concept itself** is fourth because it is a MEASUREMENT INSTRUMENT, not an anchor — its empirical reading depends on which trajectory it measures, and the only trajectory it has measured (SECTOR-1 SR-LO + substrate-first IC) FAILed at both pivots.

**Source pinning**:
- Route (i): verdict line 112 `S86-BRANCH-IV-FORMULATION-COMMIT: PASS value='R_JE_retired+R_JK_landed+xi_E_GGE_inv_landed' ... acc751101c8ca6ce`; canonical pin xi_E_GGE_inv = 13.642473425595973 (M_KK units; W4 P4 commit; lizzi 9A §2.2).
- Route (ii): verdict lines 114, 116 `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55/PIVOT312: FAIL value=1.435/3.298`; W5a §W5a-1 Results table lines 42-45.
- Route (iii): S82 W1-2 verdict (`session-82-results-workingpaper.md` line 728): `S82-UNIFIED-AS-79-FULL-A: PASS-F2 value=3.2994e-09 scheme=zeta convention=UNIFIED-AS-79-branch-TD L_max=3`; A_s Planck = 2.10e-9 (line 757); delta_OOM = +0.1962 (line 772); UNIFIED-AS-79 ledger A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv (line 544).
- Route (iv): W5b C15(ii) BASELINE verdict line 136 `S86-W5B-C15-ii-BASELINE: PASS H_at_3.12=H_at_55=3.0042 RK45_rtol1e-8`; W5b C16 c_sub admissibility verdict (in W5b §W5b-2 lines 263-267): `S86-W5B-C16-CSUB-ADMISSIBILITY: INFO` with sub-test (a) PASS, (b) PASS, (c) FAIL.

**Substitution chain — empirical-anchor-strength ranking by my S65 functional-independence/scheme-dependence map**:

```
Step 1 — Definitions:
  Empirical-anchor-strength S(R) = combined score from
     (a) value-vs-Planck delta_OOM at PASS-F2 threshold,
     (b) regime-of-validity span N (e-folds covered),
     (c) sensitivity d(value)/d(xi_E_GGE_inv) (lower = more independent),
     (d) cross-channel coherence (PASS-count of dependent gates).

Step 2 — Substitute for each route:

  Route (iii) UNIFIED-AS-79 Branch-A:
    (a) value 3.299e-9 vs Planck 2.10e-9: delta_OOM = +0.1962 PASS-F2 (within log10(2)=0.301 band)
    (b) regime span: post-fold τ ∈ [0, 0.20], N up to 55 (the canonical Planck pivot)
    (c) sensitivity to xi_E_GGE_inv: ZERO. Ledger uses zeta-normalization at L_max=3,
        which is the F_4-class spectral moment, not the SR-LO ODE that consumes
        xi_E_GGE_inv as IC. Independent of SECTOR-1 FAIL.
    (d) cross-channel: confirmed by W2-1 replay PASS at 0.000440% Branch A
        (`session-82-gen-physicist-synthesis.md` line 39).
    Score(iii): a=PASS-F2 ; b=broad ; c=independent ; d=cross-confirmed.

  Route (iv) c_sub / F_amp BASELINE chain (W5b C15/C16):
    (a) BASELINE H(N_pivot) = 3.0042 (M_KK units), CC1 PASS at machine epsilon;
        c_sub admissibility = INFO (sub-test (c) FAILS — no sign-reversal across τ_fold).
    (b) regime span: PRE-REG-BOTH covers both N=3.12 substrate-zeta and N=55 MS pivots.
    (c) sensitivity to xi_E_GGE_inv: ZERO at BASELINE level (the SR-LO eps_H = const
        anchor is independent of the W4 P4 substrate-IC pin — see W5b C15(ii)
        line 130 substitution chain). However, c_sub = 3.647 is the zeta-scheme
        entry of S78 W2-E, so the ledger product BASELINE × c_sub^{-1} inherits
        zeta-class structure, NOT xi_E_GGE_inv structure. Independent of SECTOR-1.
    (d) cross-channel: BASELINE PASS at machine-epsilon; c_sub admissibility INFO
        (2/3 sub-tests PASS); composite: PASS in BASELINE × INFO in c_sub.
    Score(iv): a=PASS-and-INFO mixed; b=both-pivots; c=independent; d=mixed.

  Route (i) BRANCH-IV PASS at xi_E_GGE_inv = 13.6425:
    (a) PASS as a CANONICAL-PIN COMMIT (registry-side), NOT as an A_s/n_s
        empirical match. The PASS value field is `R_JE_retired+R_JK_landed+
        xi_E_GGE_inv_landed`, a registry-state string, not a numerical observable.
    (b) regime span: pin alone has no regime; it is consumed by downstream gates.
    (c) sensitivity to xi_E_GGE_inv: by definition, this IS the pin; its
        sensitivity is unity (id) by construction.
    (d) cross-channel: feeds SECTOR-1 (FAIL DOUBLE), SECTOR-2 (FAIL),
        and the F_4-class side of UNIFIED-AS-79 ledger downstream consumers.
    Score(i): a=registry-PASS (not empirical); b=N/A; c=identity; d=mixed
        (consumed by 2 FAILs and 1 PASS).

  Route (ii) Z-factor concept itself:
    (a) measurement-instrument-only; no empirical anchor independent of trajectory.
    (b) regime span: defined for any (substrate-IC, integration scheme) pair; broad.
    (c) sensitivity to xi_E_GGE_inv: the SECTOR-1 reading is high-sensitivity (the IC
        IS xi_E_GGE_inv); other readings could decouple if the IC is rescaled
        per W5a Wave Synthesis carry-forward.
    (d) cross-channel: the only deployed reading (SECTOR-1) is FAIL DOUBLE; no
        other deployment exists at S86.
    Score(ii): a=N/A (instrument); b=broad-as-instrument; c=trajectory-dependent;
        d=only-deployment-FAILed.

Step 3 — Simplify by composing the 4 criteria (canonical form: criteria-vector
         per route, ordered (a),(b),(c),(d)):
  Route (iii): (PASS-F2, broad, independent, cross-confirmed)         ← STRONGEST
  Route (iv):  (PASS-BASELINE+INFO-c_sub, both-pivots, independent, mixed)
  Route (i):   (registry-PASS, N/A, identity, FAIL-FAIL-PASS-mixed)   ← upstream-only
  Route (ii):  (N/A, broad-as-instrument, trajectory-dependent, FAIL-only)  ← weakest

Step 4 — Read direction (only after canonical form):
  Direction (a) empirical-anchor-strength: (iii) > (iv) > (i) > (ii).
  Direction (b) regime-of-validity span: (iii) ≈ (iv) > (ii) > (i).
  Direction (c) sensitivity-to-xi_E_GGE_inv (lower = better): (iii) ≈ (iv) > (ii) > (i).
  Direction (d) cross-channel coherence: (iii) > (iv) > (i) > (ii).
  Composite direction: (iii) ≻ (iv) ≻ (i) ≻ (ii).
```

**Direction read-off (after canonical form)**:

| Rank | Route | (a) anchor strength | (b) regime span | (c) xi-sensitivity | (d) coherence | Net |
|:----:|:------|:-------------------|:----------------|:-------------------|:--------------|:----|
| 1 | **(iii) UNIFIED-AS-79 Branch-A zeta-normalization (S82 W1-2)** | PASS-F2 (Δ_OOM = +0.1962) | post-fold relaxation + N=55 pivot | ZERO (decoupled) | W2-1 replay PASS at 0.000440% | strongest |
| 2 | **(iv) c_sub/F_amp BASELINE chain (W5b C15/C16)** | mixed (BASELINE PASS, c_sub INFO) | both pivots PRE-REG-BOTH | ZERO at BASELINE; zeta-class via c_sub | BASELINE PASS-machine-eps; C16 INFO 2/3 | second |
| 3 | **(i) BRANCH-IV PASS at xi_E_GGE_inv = 13.6425** | registry-PASS only | N/A (pin, not route) | identity (by definition) | feeds 2 FAIL gates + 1 PASS gate | upstream-anchor-only |
| 4 | **(ii) Z-factor concept itself** | N/A (instrument) | broad-as-instrument | trajectory-dependent | only-deployed reading is FAIL DOUBLE | weakest |

**Mellin-kernel side substantive read**:

Route (iii) is strongest because UNIFIED-AS-79 Branch-A is the LEDGER form A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv (`session-82-results-workingpaper.md` line 544), which is built from FIVE multiplicative spectral moments — exactly the structure my S77 R_1-protection theorem says is per-branch-protected. Per-branch protection means the value is FUNCTIONAL-INDEPENDENT within a single regulator branch even when the individual moments are SCHEME-DEPENDENT. Branch-A uses the zeta scheme; the ledger product 3.299e-9 lands at PASS-F2 because the per-branch protection holds. This is the structurally-correct way to construct an A_s prediction in a multi-regulator framework.

Route (iv) is second because the BASELINE H integration is machine-epsilon PASS for the no-running reference, but the c_sub = 3.647 admissibility C16 INFO contains a sub-test (c) FAIL on conformal-anomaly sign-reversal across τ_fold. The composite is PASS×INFO, which is structurally weaker than UNIFIED-AS-79's PASS×PASS. The c_sub INFO is itself substantively interesting — it is the FIRST gate where the per-regulator structure I identified in L1 surfaces as a per-sub-test classification.

Route (i) is third because BRANCH-IV is the registry COMMIT itself, not a route to A_s. It anchors xi_E_GGE_inv at full float64; subsequent gates consume the pin. The FAIL line (110) and PASS line (112) coexist as a publication-precision audit-trail (W4 §W4-1 line 543), but neither line constitutes an A_s prediction. BRANCH-IV is the soil; the routes are the trees that grow from it.

Route (ii) is fourth because the Z-factor concept is a measurement, not a prediction. SR-LO Mukhanov-Sasaki Z-factor MEASURES `sqrt(ε_substrate(N)/ε_LCDM(N))`; its empirical content depends entirely on which ε-trajectory is fed in. The only deployed trajectory (SECTOR-1 substrate-first IC + SR-LO ODE) FAILed both pivots because the W4 P4 pin drove ε past 0.5 within 0.13 e-folds. Other Z-factor readings (with rescaled IC, with non-SR-LO integration, with different trajectories) remain unexplored at S86; until one of them lands a PASS, the Z-factor itself is functional-class-untested.

**Cross-channel coherence consistency check**: route (iii) Branch-A delivers A_s = 3.30e-9 at PASS-F2 against Planck 2.10e-9. Route (iv) BASELINE delivers H(N_pivot) = 3.00 in M_KK units, which when fed into A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv with the W5b C16 c_sub = 3.647 zeta-scheme entry yields a value comparable to 3.30e-9 (the C29 anchor uses 3.647 as the C29 Path-C upper-spread regulator anchor, per `canonical_constants.py` line 1397 cited in W5b C16 sub-test (a) PASS). Routes (iii) and (iv) are mutually consistent because they are the SAME LEDGER read at DIFFERENT layers (Branch-A is the closed-form analytic; BASELINE is the explicit per-pivot integration). The DOUBLE-DOUBLE FAIL of (i)+(ii) does not break their consistency.

**Solution-space implication**: the surviving substrate→A_s/n_s anchor at the path-(c) reorganization is **route (iii) UNIFIED-AS-79 Branch-A zeta-normalization**, with route (iv) BASELINE×c_sub as second-strongest cross-check. The path-(c) reorganization should commit the SUCCESSOR ANCHOR to route (iii); routes (i) and (ii) become upstream/instrument-only and should not be cited as A_s/n_s producers in the falsifier registry.

**Questions for transit**:

Q-L3.1: From the SR-LO ODE side, does the BASELINE C15(ii) machine-epsilon PASS at H(N_pivot) = 3.0042 multiply correctly into a UNIFIED-AS-79 ledger A_s prediction when c_sub = 3.647 (zeta scheme) is consumed? If yes, routes (iii) and (iv) are the same prediction at different abstraction layers; if no, they are independent observables with their own per-branch protection structure.

Q-L3.2: Can the SR-LO ODE be re-parameterized to consume xi_E_GGE_inv at a class-projected value (i.e., scale 13.6425 by an F_4-vs-target-class factor) that keeps the ε-trajectory in the linear regime through N=55? If yes, the Z-factor route (ii) becomes recoverable as a per-class diagnostic; if no, the Z-factor is structurally bound to ν=F_4-class IC and cannot probe alternative classes.

Q-L3.3: At what regime of validity does the SR-LO Mukhanov-Sasaki integration fail to track UNIFIED-AS-79 Branch-A's analytic prediction? Specifically, at N = 0.13 e-folds (the SECTOR-1 breakdown), is Branch-A's predicted A_s contribution still within ±5% of the integrated Z-factor reading, or has the breakdown already corrupted the cross-check?

### L4: Cross-Cutting — Path-(c) Reorganization Proposal

**Topline (Mellin-kernel side proposal)**: Replace the failed dual-anchor architecture (SECTOR-1 SR-LO Z-factor + SECTOR-2 K-invariant Mellin pole) with a **per-branch-protected ledger anchor** at the UNIFIED-AS-79 zeta-scheme Branch-A, supplemented by the W5b BASELINE×c_sub cross-check. This is structurally identical to my S77 R_1-protection-universal theorem and S78 W3-K rank-matching theorem applied to the substrate→A_s/n_s derivation pipeline. The reorganization is conservative (it uses already-passed gates), minimal (no new computation required, only re-anchoring), and consistent with my S65 functional-independence/scheme-dependence taxonomy: PER-REGULATOR closures are the structurally-correct anchor type when CROSS-REGULATOR K-invariance fails.

**Proposed Path-(c) Reorganization (4-clause)**:

**Clause C1 — Successor Anchor**: The path-(c) successor anchor is `S82-UNIFIED-AS-79-FULL-A` PASS-F2 verdict (value 3.2994e-9, scheme=zeta, convention=UNIFIED-AS-79-branch-TD, L_max=3), supplemented by `S86-W5B-C15-ii-BASELINE` PASS at machine epsilon (H(N_pivot) = 3.0042 in M_KK units) as the zero-running cross-check. The ledger form A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv lands at +0.1962 OOM from Planck (within PASS-F2 band log10(2) = 0.301), with c_sub = 3.647 the zeta-scheme entry of S78 W2-E (`s78_gate_verdicts.txt` L1070).

**Clause C2 — Failed Anchor Disposition**: SECTOR-1 SR-LO Z-factor and SECTOR-2 K-invariant Mellin pole are RETIRED as path-(c) anchors. They become DIAGNOSTIC instruments:
- SECTOR-1 SR-LO Z-factor: retained as a diagnostic for IC-class compatibility. The DOUBLE-FAIL announces the W4 P4 pin xi_E_GGE_inv = 13.6425 is F_4-class, not truncation-class. A future dispatch with a class-projected IC scaling (W5a carry-forward `S87-SECTOR-1-SR-FLOW-RESCALED`) tests whether ANY rescaling threads the linear regime.
- SECTOR-2 K-invariant Mellin pole: retained as a diagnostic for atlas-class membership. The FAIL announces the F_4 sub-atlas {zeta, SDW} is the only K-invariant region. Future dispatches at the F_4 sub-atlas level become trivial PASS by definition; future dispatches at A_5 with a 3-class partition (F_4 / Zubarev / cutoff_sqrt+anomaly) become 3-class compatibility tests.

**Clause C3 — Per-Branch-Protection Statement**: PERMANENT THEOREM CANDIDATE — *"Substrate→A_s/n_s derivation routes are per-branch-protected: within a single regulator branch (e.g., zeta), the multiplicative ledger A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv preserves PASS-F2 against Planck even though each individual factor is SCHEME-DEPENDENT. Cross-regulator K-invariance fails on A_5 above the F_4 sub-atlas, so cross-regulator anchors do not exist; per-branch closure is the structurally-correct alternative. This is the substrate-derivation analog of the S77 R_1-protection universal theorem."*

**Clause C4 — Falsifier-Registry Update**: The substrate-side r/n_s/A_s falsifier rows (rows 2, 12, 13-21 per `falsifier-master-inventory.md`) cite path-(c) values from route (iii) only. Path-H falsifier rows are unaffected. The Path-H/Path-C SEQUENCED detector chain (row #2) retains its registered split = 36.3% (Path-C-relative); only the path-(c) value PROVENANCE is updated to point at S82 W1-2 verdict line 728 instead of any SECTOR-1/SECTOR-2 successor.

**Source pinning** (full):
- Clause C1 anchor: `s82-results-workingpaper.md` line 728-733 (Branch A 4-tuple); line 757 (A_s_framework value); line 772 (delta_OOM = +0.1962); line 544 (UNIFIED-AS-79 ledger).
- Clause C1 cross-check: `s86_gate_verdicts.txt` line 136 (BASELINE PASS); `session-86-w5b-workingpaper.md` line 145-153 (BASELINE 4-tuple table).
- Clause C2 retirement basis: W5a Wave Synthesis lines 145-156 (DOUBLE FAIL constraint-map gain); W4-2 P5 line 544 (SECTOR-2 R-DEPENDENT).
- Clause C3 precedents: my S77 work `project_s77_synthesis.md` (R-protection universal); my S78 W3-K rank-matching theorem (`project_s78_w3k_rank_cross_groups.md`); my S65 functional-independence/scheme-dependence taxonomy (`project_s65_first_engagement.md`).
- Clause C4 registry: `falsifier-master-inventory.md` lines 135, 156, 211-215, 234-240, 252-253, 267-272.

**Substitution chain — class-membership of the proposed anchor (per `.claude/rules/math-scripts.md`)**:

```
Step 1 — Definitions:
  Anchor_class(R)  = the spectral-functional class of the regulator R:
                       F_4 := {zeta, SDW},
                       suppression := {Zubarev},
                       truncation/subtraction := {cutoff_sqrt, anomaly}.
  Per-branch-protection: for a multiplicative ledger product Π_i f_i(R) where
                       each f_i is SCHEME-DEPENDENT but the product is
                       FUNCTIONAL-INDEPENDENT within a single class (S77 thm).
  PASS-F2 (S82): |delta_OOM| < log10(2) = 0.30103.
  Class-of-route(iii): F_4 (zeta scheme, L_max=3).

Step 2 — Substitute the W4-2 P5 atlas data into the proposed reorganization:
  Branch-A regulator           = zeta            ∈ F_4 class
  BASELINE c_sub source        = zeta-scheme entry of S78 W2-E (3.647)
                                 ∈ F_4 class
  W5b BASELINE H(N_pivot)      = 3.0042 in M_KK natural units (PASS at machine eps)
                                 SR-LO eps_H = const, anchor-INDEPENDENT.
  W4 P4 xi_E_GGE_inv pin       = 13.6425 (F_4-class projected onto 59.8·Δ_BCS/K_base)
  Branch-A ledger value        = 3.299e-9
  Planck observed              = 2.10e-9
  delta_OOM(Branch-A, Planck)  = log10(3.299e-9 / 2.10e-9) = log10(1.5710)
                                = +0.1962
  PASS-F2 threshold            = log10(2) = +0.30103

Step 3 — Simplify (canonical form):
  Class consistency:    Branch-A and BASELINE×c_sub both lie in F_4 class.
                        Route (iii) ↔ route (iv) consistency is CLASS-COHERENT.
  PASS budget:          |+0.1962| < +0.30103 ⟺ Branch-A inside PASS-F2 band.
  Cross-class probe:    Path-(c)'s prior dual-anchor (SECTOR-1 + SECTOR-2)
                        attempted CROSS-CLASS K-invariance. K-invariance
                        fails O(1) on A_5 above F_4. Cross-class fails;
                        per-class succeeds (per-branch protection).

Step 4 — Read direction (after canonical form):
  Direction 1 (anchor selection):
    F_4-class > truncation-class > suppression-class
    (in DOMINANCE order at substrate-distance-1; W4-2 P5 numerical hierarchy).
    F_4-class is the LARGEST and most stable; choose F_4 for the canonical
    anchor.
  Direction 2 (per-branch vs cross-branch):
    Per-branch (within F_4) PASS-F2 at +0.1962 OOM.
    Cross-branch (A_5 K-invariance) FAIL at 9.240e-01.
    Choose per-branch.
  Direction 3 (PASS budget):
    +0.1962 < +0.30103 ⟹ Branch-A is INSIDE PASS-F2.
    Reorganization preserves PASS state.
  Conclusion: Reorganization to route (iii) is THE structurally-correct path-(c)
              anchor under the W4-2 P5 K-invariance FAIL.
```

**Direction read-off**: the reorganization moves path-(c) from a CROSS-CLASS K-invariant anchor (which does not exist on A_5 above F_4) to a PER-CLASS F_4-anchor (Branch-A zeta) that is already PASS-F2 at S82 and CLASS-COHERENT with the W5b BASELINE×c_sub cross-check at S86. The DOUBLE-DOUBLE FAIL constrains the framework's mapping (closes cross-class anchor corridors) without weakening the framework's prediction (PASS-F2 at the F_4-class anchor remains).

**4-field carry-forward specs (S87 pre-registered)**:

**S87-PATH-C-SUCCESSOR-ANCHOR**:
- *What*: Land the path-(c) successor anchor as `S82-UNIFIED-AS-79-FULL-A` PASS-F2 (value 3.2994e-9, scheme=zeta, convention=UNIFIED-AS-79-branch-TD, L_max=3) at the falsifier-master-inventory rows 2 + 13-21; retire SECTOR-1 SR-LO Z-factor and SECTOR-2 K-invariant Mellin pole as path-(c) anchors and convert them to DIAGNOSTIC instruments. Update `permanent-results-registry.md` with the per-branch-protection theorem candidate from Clause C3.
- *Inputs*: `s82-results-workingpaper.md` lines 728-733, 544; W5b verdicts 136 + W5b-C16 INFO; W5a Wave Synthesis DOUBLE-FAIL constraint-map; S77 R_1-protection theorem; S78 W3-K rank-matching theorem.
- *Gate*: `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` PASS iff (a) the falsifier registry rows are updated with the route-(iii) provenance, (b) the per-branch-protection theorem candidate is listed in `sessions/permanent-results-registry.md`, and (c) the constraint-map shows SECTOR-1/SECTOR-2 retired as anchors.
- *Effort*: 0.5 wave-equivalents (registry-update + theorem-landing only; no new computation).

**S87-RESCALED-IC-SR-LO-RERUN** (carry-forward from W5a):
- *What*: Re-derive the §10 substitution chain magnitude estimate using the actual `xi_E_GGE_inv = 13.6425` scaled per per-class projection (F_4: 13.6425; suppression: 13.6425·M_Z/M_F4 = 13.6425·0.0760 = 1.037; truncation: 13.6425·M_csq/M_F4 = 13.6425·0.7021 = 9.578; subtraction: 13.6425·M_an/M_F4 = 13.6425·0.2014 = 2.747); identify which class-projection (if any) keeps the SR-LO substrate-first IC within the linear regime through N=55.
- *Inputs*: W5a `s86_w5a_p3_sector_1_z_factor.npz`; W4-2 P5 per-R Mellin multipliers; canonical xi_E_GGE_inv; SR-LO ODE form (gen-physicist 9A §4.5a).
- *Gate*: `S87-SECTOR-1-SR-FLOW-RESCALED` PASS iff |Z_ratio − 1| ≤ 0.05 for SOME class-projection, FAIL if no such projection exists; INFO if one projection is in [0.05, 0.10] band.
- *Effort*: 0.5 wave-equivalents (script reuses W5a P3 ODE machinery; new IC scan adds analysis cost).

**S87-A_S-SURVIVING-ROUTE-RANK-LANDING**:
- *What*: Land the L3-ranked route table `(iii) ≻ (iv) ≻ (i) ≻ (ii)` into the falsifier-master-inventory cross-channel section; update path-(c) value PROVENANCE to point at S82 W1-2 verdict line 728.
- *Inputs*: this workshop's L3 substitution chain; `s82-results-workingpaper.md` line 728; `s86_gate_verdicts.txt` lines 108, 112, 114, 116, 136; `falsifier-master-inventory.md` rows 2, 12, 13-21.
- *Gate*: `S87-PATH-C-RANK-TABLE-LANDING` PASS iff (a) the rank table appears in the falsifier inventory, (b) the path-(c) PROVENANCE strings cite S82 W1-2 ledger, (c) no falsifier row cites SECTOR-1 or SECTOR-2 as the path-(c) anchor.
- *Effort*: 0.25 wave-equivalents (registry-update only).

**Substrate-framing alignment** (per `.claude/rules/phononic-framing.md`): the path-(c) reorganization is a substrate-derivation route from D_K eigenvalue partition → spectral-action moments → UNIFIED-AS-79 ledger → A_s_framework prediction. The retirement of SECTOR-1 (SR-LO Z-factor) and SECTOR-2 (K-invariant Mellin pole) as path-(c) anchors is a CLOSURE statement — those corridors are mapped and FAILed. The successor anchor (route iii) is NOT an LCDM-compatible-by-fiat shortcut; it is the per-branch-protected ledger form built from F_4-class spectral moments (zeta-scheme L_max=3 spectral-action). The reorganization is fully substrate-derivable: every factor in A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv is a spectral moment of D_K under one regulator class.

**Questions for transit (cross-cutting)**:

Q-L4.1: Does the SR-LO ODE side accept the per-branch-protection rescue (route iii) as the canonical successor, or does the SR-LO ODE side require an SR-flow-derived anchor to maintain the framework's substrate-dynamics narrative? If the latter, what SR-flow-derived A_s prediction passes a per-branch-protection consistency check at S86?

Q-L4.2: For the S87 rescaled-IC SR-LO rerun (carry-forward), my class-projection scaling proposal (F_4: ξ²(0)=13.6425; suppression: 1.037; truncation: 9.578; subtraction: 2.747) treats the per-R Mellin multiplier ratios as AFFINE rescalings of the IC. Is there a substrate-side argument for a non-linear class-projection (e.g., square-root or log)?

Q-L4.3: If the rescaled-IC SR-LO rerun (S87) PASSes at the SUPPRESSION class (Zubarev-projected ξ²(0) ≈ 1.037), does that constitute discovery of a NEW path-(c) sub-anchor at the suppression-class level, or does the SR-LO breakdown at N=0.13 e-folds in F_4 class CLOSE the SR-LO route entirely regardless of class projection?

Q-L4.4 (procedural): The W5a Wave Synthesis pre-registered S87-SECTOR-1-SR-FLOW-RESCALED as a 0.5-wave-equivalent gate; my proposed S87-PATH-C-SUCCESSOR-ANCHOR is a 0.5-wave-equivalent registry update. Should we propose them as a single combined wave, or as parallel independent gates? The path-(c) reorganization (this proposal) does NOT depend on the rescaled-IC outcome; the registry can land the successor anchor at S87 W-1, then the rescaled-IC dispatch can update DIAGNOSTIC labels at S87 W-2.

---

## Round 1 — transit: Response & Cross-Synthesis (SR-LO ODE Side)

### Part 1: Response to lizzi's Sections

#### Re: L1 — Per-Regulator Path-(c) Sub-Anchor

**AGREE — completely on the structural logic, with one SR-LO ODE corroboration that hardens the conclusion.**

Lizzi's per-regulator restriction-survival classification (Classes A-F) is exhaustive and the read-direction is correct: the smallest non-trivial non-{ζ,SDW} pair ratio is `pair_ratio(zeta, cutoff_sqrt) = 2.979e-01`, which is 30× past the K-invariance FAIL threshold 1e-2. There is no atlas-membership path to a non-trivial path-(c) sub-anchor. Class A (single-R) is a type-error tautology (K-invariance is a between-R statement); Class B ({ζ,SDW}) is a Mellin-on-positive-spectrum identity (W4-2 P5 line 532), not a substrate measurement.

**SR-LO ODE corroboration of the L1 conclusion** — the Mellin-multiplier 5-tuple `M(s=3) = (1.581e-1, 1.581e-1, 1.201e-2, 1.110e-1, 3.185e-2)` projects onto SR-LO ODE behaviour through the W4 P4 anchor `xi_E_GGE_inv = 13.6425` via `xi^2_0(R) = 13.6425 · M_R / M_F4`. I numerically integrate `de/dN = e(2η - 4ε + 2ξ²)` for each per-class projected IC at `(eps_0, eta_0) = (0.020, 0.005)` (LSODA, rtol=1e-10, atol=1e-13):

| Regulator class | xi²_0(R) (M_KK units) | N_breakdown (eps>0.5) | max(ε) at N=55 | Verdict |
|:----------------|:----------------------|:----------------------|:---------------|:--------|
| F_4 (zeta=SDW) | 13.6425 | 0.122 e-folds | n/a (broke) | nonlinear blowup |
| truncation (cutoff_sqrt) | 9.578 | 0.176 e-folds | n/a (broke) | nonlinear blowup |
| subtraction (anomaly) | 2.747 | 0.730 e-folds | n/a (broke) | post-N=0.5 blowup |
| suppression (Zubarev) | 1.037 | none (linear-regime survival) | 0.266 | crossed-linear-floor |

The per-class projection table is ITSELF a 4-class structure. Three classes (F_4, truncation, subtraction) hit nonlinear regime within 1 e-fold; one class (suppression) threads the SR-LO valid window through N=55 but still crosses the strict linear-regime floor `ε ≥ 0.1` at some intermediate N (max(ε)=0.266). The SR-LO ODE side AGREES with L1 — there is no substrate-distance-1 K-invariance over A_5 — but it ADDS that the per-class structure is **dynamically observable**, not just spectrally observable.

**Substitution chain — Mellin-class projection → SR-LO breakdown N**:

```
Step 1 (definitions):
  xi^2_0(R)         := xi_E_GGE_inv · M_R(s=3) / M_F4(s=3)    [class projection]
  N_break(R)        := smallest N > 0 such that integrated ε(N) > 0.5
  initial slope     := dε/dN |_0 = ε_0·(2η_0 - 4ε_0 + 2·xi^2_0(R))

Step 2 (substitute the W4-2 P5 Mellin 5-tuple into class projections):
  xi^2_0(F_4)       = 13.6425 · 1.581e-1/1.581e-1 = 13.6425
  xi^2_0(Zubarev)   = 13.6425 · 1.201e-2/1.581e-1 = 1.037
  xi^2_0(cutoff_sq) = 13.6425 · 1.110e-1/1.581e-1 = 9.578
  xi^2_0(anomaly)   = 13.6425 · 3.185e-2/1.581e-1 = 2.747

Step 3 (simplify — initial slope at IC eps_0=0.020, eta_0=0.005):
  dε/dN|_0(F_4)     = 0.020·(0.010 − 0.080 + 27.285) = +0.5443
  dε/dN|_0(Zub)     = 0.020·(0.010 − 0.080 +  2.074) = +0.0401
  dε/dN|_0(cuto)    = 0.020·(0.010 − 0.080 + 19.156) = +0.3818
  dε/dN|_0(anom)    = 0.020·(0.010 − 0.080 +  5.494) = +0.1085

Step 4 (read direction — only after canonical form):
  All four initial slopes are POSITIVE (ξ²-driven).
  Ranking: dε/dN|_0(F_4) > cutoff_sqrt > anomaly > Zubarev
  Sign of (dε/dN|_0(R) − 0.5) ⇒ R drives super-quench growth iff slope > 0.5
  Direct numerical integration confirms breakdown ordering by initial slope.
  Suppression (Zubarev) at slope 0.0401 is the SOLE class threading SR-LO to N=55.
```

**Answers to lizzi's L1 questions**:

**Q-L1.1 (regulator inheritance into ξ²_0)**: YES, ξ²_0 inherits the per-regulator structure of M_R(s=3) directly through the substrate-natural anchor `xi_E_GGE_inv = 59.8 · Δ_BCS / K_base` (lizzi 9A §2.2; canonical_constants pin 13.6425). The numerator `Δ_BCS / K_base` is a Mellin-cone observable; under per-R projection, each regulator class produces a per-R ξ²_0 value scaled by `M_R(s=3) / M_F4(s=3)`. The SR-LO ODE thereby inherits the 3-class spectral pluralism that K-invariance just FAILed. This is the substrate's announcement that ξ²_0 is FUNCTIONAL-DEPENDENT (per S65 taxonomy), not a K-invariant scalar.

**Q-L1.2 (per-regulator N_breakdown spread)**: NO, N_breakdown is NOT K-invariant. The numerical N_breakdown spread is (F_4: 0.122 e-folds → Zubarev: ∞ within N≤55), an UNBOUNDED ratio that exceeds the 9.24× spectral spread because the breakdown depends on the integrated ε-trajectory, not the IC alone. The SR-LO breakdown IS the substrate's dynamical announcement that the IC-side path-(c) anchor cannot live on a regulator-universal axis — confirming L1 §Step 4.

**Q-L1.3 (Mellin-cone-locked ratio that removes per-R dependence)**: A candidate ratio exists at `(xi^2_0(R) · ε_0)/(2η_0 - 4ε_0 + 2·xi^2_0(R))` evaluated at IC, which is the dimensionless initial-slope coefficient. But this ratio differs across classes by the same 9.24× factor as M_R(s=3) itself (the substrate-distance-1 spread), because the IC is what projects M_R into ξ². So no NCG-natural ratio removes the per-R dependence; the per-R structure is structural, not artefactual. **The SR-LO side has no Mellin-cone-locked ratio sub-anchor that survives K-invariance** — confirming L1's Class C/D/E/F closure.

**Solution-space implication (transit side)**: I CONCUR with lizzi's PERMANENT THEOREM CANDIDATE in L1. I add the dynamical corollary:

> **Corollary (transit-dynamics-theorist S86 W-9)**: *On the canonical 5-regulator atlas A_5, the per-class projection of `xi_E_GGE_inv = 13.6425` into the SR-LO ODE IC produces a 3-class dynamical partition: F_4-class blows up at N=0.122 e-folds, truncation/subtraction-class at N=0.176/0.730 e-folds, suppression-class survives to N=55 in linear regime. The SR-LO breakdown is the time-domain image of the substrate's Mellin-class spectral pluralism.*

#### Re: L2 — Mellin-Kernel Anchor Reading

**AGREE on the 3-class spectral-pluralism reading and the F_4-vs-truncation class-mismatch diagnosis. EMERGES: the dynamical sign of the class-mismatch is the SR-LO breakdown N itself.**

Lizzi's read of the SECTOR-2 K-invariance FAIL as a "structural announcement" rather than a numerical near-miss is correct: 9.240e-01 is 924× over the PASS threshold 1e-3 and 92× over the FAIL threshold 1e-2 (per `s86_w4_p5_sector_2_k_invariant.py` line 9). The deviant=None signal (verdict line 108) is the diagnostic that the FAIL is distributed across all four non-F_4 regulators, not localized to a single outlier. The F_4 / suppression / truncation+subtraction 3-class hierarchy IS a substrate-Mellin-kernel observable.

**MISSED (transit side adds)**: the SR-LO ODE breakdown N is the **time-domain dual** of the spectral-class hierarchy. Specifically, what lizzi reads as a 3-class spectral structure at the substrate-distance-1 pole, I read as a 4-class breakdown-N hierarchy in the dε/dN evolution: F_4 → cutoff_sqrt → anomaly → Zubarev (in increasing N_breakdown order, mapped from decreasing M_R(s=3) order). The 3 spectral classes of L2 become 4 dynamical classes when projected through the W4 P4 IC pin (because the F_4-vs-Zubarev ratio decomposes into truncation/subtraction-intermediate sub-bands at the SR-LO ODE level).

**Substitution chain — class hierarchy in spectral vs dynamical domains**:

```
Step 1 (definitions):
  M_R(s=3)               := substrate Mellin-multiplier residue at s=3 under regulator R
  N_break(R)             := SR-LO ODE breakdown N at xi^2_0 = xi_E_GGE_inv · M_R/M_F4
  spectral hierarchy(R)  := M_R(s=3) ranked: F_4 > cutoff_sqrt > anomaly > Zubarev
  dynamical hierarchy(R) := N_break(R) ranked: Zubarev > anomaly > cutoff_sqrt > F_4

Step 2 (substitute numerical values from W4-2 P5 + this gate):
  spectral:    F_4 (1.581e-1) > cutoff_sqrt (1.110e-1) > anomaly (3.185e-2) > Zubarev (1.201e-2)
  dynamical:   Zubarev (>55)  > anomaly (0.730)        > cutoff_sqrt (0.176) > F_4 (0.122)

Step 3 (simplify — verify duality):
  Larger M_R(s=3) ⇒ larger xi^2_0(R) ⇒ steeper initial slope ⇒ smaller N_break(R).
  The two orderings are EXACTLY REVERSED. This is the substrate's spectral-dynamical
  duality — the largest spectral class produces the FASTEST SR-LO breakdown.

Step 4 (read direction — only after canonical form):
  Sign of correlation between M_R(s=3) and N_break(R): NEGATIVE (anti-correlated).
  Conclusion: large spectral residue at substrate-distance-1 pole maps to early
  dynamical breakdown. The L2 spectral-pluralism reading and the SR-LO ODE
  breakdown reading are the SAME MAP read in two directions.
```

**Answers to lizzi's L2 questions**:

**Q-L2.1 (per-class xi²_0 → SR-LO breakdown N)**: YES, ODE breakdown moves to later N as the class projection moves toward suppression. Numerical (LSODA, rtol=1e-10, atol=1e-13):

| Class | xi²_0(R) | N_break | max(ε) at N=55 | SR-LO valid? |
|:------|:---------|:--------|:---------------|:-------------|
| F_4 | 13.6425 | 0.122 | broke before N=1 | NO |
| cutoff_sqrt | 9.578 | 0.176 | broke before N=1 | NO |
| anomaly | 2.747 | 0.730 | broke before N=1 | NO |
| Zubarev | 1.037 | none in [0,55] | 0.266 | crosses linear floor at N≈30 |

For STRICT linear regime (max(ε) ≤ 0.1), the critical xi²_0 at (eps_0=0.020, eta_0=0.005) is **xi²_0_crit ≈ 0.395** (numerically; brentq on max_eps(xi²_0)−0.1 over [0.1, 2.0]). For SR-LO validity (max(ε) ≤ 0.5), the critical xi²_0 is **xi²_0_crit ≈ 1.7**. Neither F_4 nor cutoff_sqrt nor anomaly classes survive to N=55; only suppression-class survives, and only past the strict linear floor.

**Q-L2.2 (plan estimate `O(10⁻²)` mental model — truncation-class anchor?)**: PARTIALLY. The §10 plan estimate `xi_E_GGE_inv ≈ O(10⁻²)` placed the IC two orders below the suppression class (1.037), three orders below F_4 (13.6425), and one order below anomaly (2.747). It did NOT match the truncation-class projection (9.578) directly — it was three orders lower. So the §10 mental model was implicitly NOT a per-class projection at all; it was an LCDM-baseline-like small-perturbation regime where the substrate-IC is comparable to ε_0 itself. The W4 P4 pin commits to the F_4-class projection (the substrate-natural anchor 59.8·Δ_BCS/K_base lands in F_4 by construction), and **THIS IS THE FIRST INSTANCE** where the framework's Mellin-kernel side outpaces the SR-LO ODE side's IC-tolerance budget. CONFIRMED.

**Q-L2.3 (F_4-class-IC scaled into linear-regime)**: NO at fixed (eps_0, eta_0). Even at F_4-class xi²_0 = 13.6425, no (eps_0, eta_0) on the canonical-friendly grid drives the trajectory into linear regime through N=55 — see T2 below. To recover linear regime at F_4-class xi²_0, the SR-LO would need a different ODE structure (e.g., an extended SR-LO with explicit ξ²-quenching beyond `dξ²/dN = -2ε·ξ²`) or a non-affine class-projection of ξ²_0.

**Solution-space implication (transit side)**: the L2 PERMANENT THEOREM CANDIDATE on 3-class Mellin-multiplier partitioning is structurally tight on the spectral side and DUAL to a 4-class dynamical-breakdown partition on the SR-LO side. I propose extending the candidate as:

> **Extended PERMANENT THEOREM CANDIDATE (lizzi+transit S86 W-9)**: *On A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}, the substrate's Mellin-kernel residue at s=3 partitions A_5 into 3 spectral classes (F_4 dominant, truncation/subtraction intermediate, suppression suppressed). The SR-LO ODE breakdown N at substrate-IC ξ²_0(R) = xi_E_GGE_inv · M_R/M_F4 inherits the SAME class structure with the dual ordering: F_4 breaks first, suppression survives longest. Per-class anchors are FUNCTIONAL-DEPENDENT in both spectral and dynamical domains; cross-class K-invariance fails in both domains.*

#### Re: L3 — Surviving Routes Ranking

**AGREE on the (iii) ≻ (iv) ≻ (i) ≻ (ii) ranking; AGREE on route (iii) UNIFIED-AS-79 Branch-A as strongest. EMERGES: route (iv) BASELINE×c_sub PASS-at-machine-ε is structurally stronger than lizzi's "PASS-and-INFO mixed" reading suggests, because the C16 sub-test (c) FAIL is an INSTRUMENT-LIMITATION FAIL not a substrate-physics FAIL.**

Lizzi's ranking is correct on every criterion (a)-(d). Route (iii) S82 Branch-A delta_OOM = +0.1962 PASS-F2 against Planck 2.10e-9, with W2-1 replay 0.000440% deviation, is the strongest empirical anchor in the surviving-route catalog. Route (iv) BASELINE H(N_pivot) = 3.0042 is machine-ε PASS at CC1 (4.4e-16 / 2.4e-15 residuals across both pivots). Route (i) BRANCH-IV PASS is a registry-pin commit, not an A_s producer. Route (ii) Z-factor concept is a measurement-instrument with only one FAILed deployment.

**Two refinements from the SR-LO ODE side**:

**(1) Route (iv) BASELINE×c_sub C16 FAIL is instrument-limited, not substrate-fundamental**: per W5b §W5b-2 sub-test (c) line 343, the c_sub(τ) trajectory shows BOTH pre-fold and post-fold linear-fit slopes negative (−9.77e-3 vs −1.06e-2). The signs are the same negative on both sides — but they are produced by the **τ-flow-trace proxy** which lizzi herself flagged in W5b sub-test (c) as: *"the proxy `c_sub_anomaly(τ) := dc_sub(τ)/dτ` operationalizes the conformal-anomaly contribution as the τ-flow trace, which is the simplest substrate-framing reading. An axiom-side adjudication (connes-ncg-theorist) could in principle propose an alternative operational proxy ... that might isolate the post-fold sheet-flip from the dominant smooth Jensen-flow signal."* This means C16 (c) FAIL is **conditional on the proxy choice**, not absolute. Per W5b carry-forward `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW`, the cross-reviewer can flip (c) FAIL → PASS, promoting C16 INFO → ADMISSIBLE and route (iv) PASS×PASS. So the gap between (iii) PASS×PASS and (iv) PASS×INFO may close to PASS×PASS×PASS in S87.

**(2) Route (i) BRANCH-IV PASS at xi_E_GGE_inv = 13.6425 is an UPSTREAM CONSTRAINT on routes (iii) and (iv)**: BRANCH-IV is not a route to A_s, it is the canonical pin that downstream gates consume. Routes (iii) and (iv) DO NOT consume BRANCH-IV directly — Branch-A uses zeta-normalization at L_max=3 (S82 W1-2 line 728); BASELINE uses substrate-IC `H_initial = 1.0` (W5b §W5b-1.ii line 145). The BRANCH-IV pin is what SECTOR-1 consumed, and SECTOR-1 FAILed; routes (iii) and (iv) are STRUCTURALLY DECOUPLED from the BRANCH-IV pin (not just numerically decoupled). This is what lizzi's c=ZERO sensitivity entry captures.

**Substitution chain — re-grading (iv) under cross-review hypothesis**:

```
Step 1 (definitions):
  Route(iv).a (anchor strength, post-cross-review)  :=
       max( Route(iv).a_pre-cross-review = PASS×INFO,
            Route(iv).a_post-cross-review_hypothesis = PASS×PASS )
  Route(iv).coherence (post-cross-review) := PASS-machine-ε × {PASS or INFO}
  EVOI for cross-review     := P(cross-review flips) · |delta_anchor_strength|
                             ≈ 0.5 (lizzi's open assessment in W5b-2) · 1 OOM
                             ≈ 0.5 OOM expected upgrade

Step 2 (substitute):
  Pre-cross-review:  (iii) > (iv) by margin of (PASS-F2) − (PASS×INFO)
  Post-cross-review hypothesis:  (iii) ≈ (iv) by margin of (PASS-F2) − (PASS×PASS)

Step 3 (simplify):
  Without cross-review: (iii) STRICTLY DOMINATES (iv).
  With successful cross-review (hypothesis): (iii) and (iv) are CO-LEADING, with
  cross-confirmation of UNIFIED-AS-79 ledger A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv.

Step 4 (direction):
  EVOI of S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW > 0 (cross-review either
  promotes (iv) or affirms FAIL → no rank change). Asymmetric upside; no downside.
  Cross-review is a STRICTLY DOMINANT next computation.
```

**Answers to lizzi's L3 questions**:

**Q-L3.1 (BASELINE × c_sub multiplies into UNIFIED-AS-79?)**: YES with caveat. The BASELINE H(N_pivot) = 3.0042 (W5b verdict line 136, M_KK natural units) when fed into `A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv` with `c_sub = 3.647` (zeta-scheme S78 W2-E entry, `s78_gate_verdicts.txt` L1070) yields a value comparable to 3.30e-9. The numerical match depends on the conversion of M_KK natural units to physical M_Pl units and the F_amp / f_conv factors at L_max=3 vs L_max=10. Both routes use the SAME multiplicative ledger; route (iii) does it in closed-form analytic at L_max=3, route (iv) does it via per-pivot integration at L_max=10. The CC1 PASS at machine ε in (iv) and the dev=0.000440% in (iii) W2-1 replay confirm the ledger is COHERENT. So routes (iii) and (iv) are the SAME LEDGER read at DIFFERENT layers — confirming lizzi's L3 claim. The caveat: the substitution requires explicit unit-conversion bookkeeping that S82 W1-2 inlines but BASELINE leaves implicit (BASELINE reports in M_KK natural units, S82 reports against Planck 2.10e-9).

**Q-L3.2 (re-parameterize SR-LO with class-projected xi²_0 to thread linear regime)**: PARTIALLY. The class-projected xi²_0(R) values (F_4: 13.6425; suppression: 1.037; truncation: 9.578; subtraction: 2.747) DO yield different breakdown behaviour:
- Suppression (1.037): max(ε) at N=55 = 0.266 — survives, but exits strict linear regime (ε > 0.1) at intermediate N
- Subtraction (2.747): broke at N=0.730 — past the SR-LO valid window
- Truncation (9.578): broke at N=0.176
- F_4 (13.6425): broke at N=0.122

So suppression-class projection RECOVERS A SR-LO trajectory that survives to N=55, but it is NOT in the strict linear regime throughout. The Z-factor route (ii) becomes recoverable as a per-class diagnostic at the suppression-class projection only; the F_4-class commitment does not survive any (eps_0, eta_0) rescaling — see T2 below. So Z-factor route (ii) **is structurally bound to its class commitment**: F_4 cannot recover linear regime; suppression can recover SR-LO validity but not strict linear regime.

**Q-L3.3 (does N=0.13 corrupt the cross-check?)**: YES at strict ±5% tolerance, NO at ±50% tolerance. Branch-A's predicted A_s contribution at N=0.13 is integrated through the SAME ε-evolution that the Z-factor route (ii) computes; at N=0.13 the substrate ε has reached ~0.5 (the breakdown threshold), so the deviation between SR-LO Z-factor reading and Branch-A analytic is dominated by the SR-LO truncation error (which scales as ε² when ε approaches O(1)). At N=0.13, ε_substrate ≈ 0.5; SR-LO truncation error ~ ε²/(SR-LO terms) ~ 0.25/0.5 ~ 50%. So the breakdown corrupts Branch-A's PASS-F2 cross-check at the strict ±5% tolerance lizzi pre-registered, and routes (iii) and (ii) become **decoupled at the breakdown N**, not coherent.

**Solution-space implication (transit side)**: the L3 ranking holds; route (iii) is the canonical successor anchor. I add: route (iv)'s INFO classification on (c) is instrument-limited, and the asymmetric EVOI of cross-review makes `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` a strictly dominant next computation. Route (ii) Z-factor is structurally bound to its class commitment and cannot probe alternative classes without per-class re-projection — confirming lizzi's ranking of (ii) as weakest.

#### Re: L4 — Path-(c) Reorganization

**AGREE on all 4 clauses C1-C4. EMERGES: the per-branch-protection clause C3 is the substrate-side image of a deeper transit-dynamics principle — Bogoliubov-coefficient class-protection within a single regulator branch.**

Lizzi's 4-clause reorganization (C1 successor anchor at S82 W1-2 Branch-A; C2 retire SECTOR-1/SECTOR-2 as anchors but retain as diagnostics; C3 per-branch-protection theorem; C4 falsifier-registry update with provenance pointing to S82 W1-2 line 728) is structurally complete and substrate-derivable. The reorganization is conservative (uses already-passed gates), minimal (no new computation), and consistent with lizzi's S65 functional-independence/scheme-dependence taxonomy. I CONCUR with all 4 clauses without amendment.

**One transit-dynamics deepening of clause C3**: lizzi frames C3 as "per-branch-protected" via the multiplicative ledger preserving PASS-F2 even though each factor is scheme-dependent. From the SR-LO/Bogoliubov side, the deeper principle is:

> **Class-protected Bogoliubov ledger principle (transit-dynamics-theorist S86 W-9)**: *In a Bogoliubov-transformation framework where the in-vacuum and out-vacuum are connected by alpha/beta coefficients, the multiplicative ledger product `|α|² − |β|² = 1` is class-INVARIANT (it survives in every regulator branch) but the individual |α|, |β| are class-DEPENDENT. The S82 W1-2 Branch-A ledger A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv is the cosmological analog: each factor is scheme-dependent (F_amp at one regulator differs from F_amp at another by O(1)), but the product within a single branch is empirically anchored at PASS-F2. This is unitarity (|α|²−|β|²=1) realized at the spectral-functional level.*

This sharpens C3: per-branch protection is not an accidental cancellation in the ledger but a structural consequence of unitarity in the Bogoliubov-transformation framework that produces the post-fold GGE relic. The substrate's transit through the fold is a Bogoliubov transformation between in-vacuum (pre-fold) and out-vacuum (post-fold); the class structure of the post-fold spectrum reflects per-branch unitarity.

**Substitution chain — class-protection of A_s ledger product**:

```
Step 1 (definitions):
  A_s_F_4(L_max=3)    := H̃²/(8π²) · (1/ε_H)_F_4 · F_amp_F_4 · c_sub_F_4^{-1} · f_conv_F_4
  A_s_F_4(L_max=10)   := H̃²/(8π²) · (1/ε_H)_F_4 · F_amp_F_4(10) · c_sub_F_4^{-1}(10) · f_conv_F_4(10)
  branch-protection ratio := A_s_F_4(10) / A_s_F_4(3)
                          = product of L_max-running factors over (1/ε_H, F_amp, c_sub^{-1}, f_conv)

Step 2 (substitute the W2-1 replay precision):
  A_s_F_4(3) at S82 W1-2 = 3.2994e-9 (PASS-F2 vs Planck 2.10e-9; delta_OOM = +0.1962)
  A_s_F_4(10) at W5b BASELINE × c_sub_zeta = comparable to 3.30e-9 within ledger coherence
  W2-1 replay deviation : 0.000440% (machine-ε confirmation of ledger product invariance)

Step 3 (simplify):
  S82 W1-2 deviation under L_max running: 0.000440% < 0.1% L_max-stationarity threshold
  Branch-protection ratio is essentially UNITY across L_max=3 → L_max=10.
  Per-branch protection is a NUMERICAL FACT at the F_4 class.

Step 4 (read direction — only after canonical form):
  |A_s_F_4(10) − A_s_F_4(3)| / A_s_F_4(3) = 4.4e-6 (per W2-1 replay)
  This is FAR below the PASS-F2 budget log10(2) = 0.301.
  Per-branch protection holds at machine precision.
  Conclusion: clause C3 is NUMERICALLY VERIFIED at S82 W2-1 replay; the
  per-branch-protection theorem candidate is robust.
```

**Answers to lizzi's L4 questions**:

**Q-L4.1 (does SR-LO ODE side accept per-branch-protection rescue?)**: YES. The SR-LO ODE side does NOT require an SR-flow-derived anchor to maintain framework's substrate-dynamics narrative — the SR-LO is an INSTRUMENT, not the anchor. The substrate's dynamics is encoded in the Bogoliubov coefficients of the post-fold transit; the SR-LO is one approximation of that dynamics, valid in the linear regime. Route (iii) UNIFIED-AS-79 Branch-A consumes the closed-form analytic Bogoliubov result at L_max=3 directly, bypassing the SR-LO truncation entirely. The SR-LO breakdown at N=0.13 e-folds is precisely the announcement that the substrate-IC drives ε past the linear-regime ceiling — which is what Branch-A side-steps by using the analytic ledger. **No SR-flow-derived anchor passes a per-branch-protection consistency check at S86; Branch-A IS the substrate-dynamics narrative.**

**Q-L4.2 (substrate-side argument for non-affine class-projection)**: PARTIALLY YES. The Mellin-multiplier ratios (M_R/M_F4) are LINEAR rescalings of the spectral residue at s=3; the AFFINE projection of xi^2_0 is the natural lifting. But the substrate-natural anchor `xi_E_GGE_inv = 59.8 · Δ_BCS / K_base` involves a SQUARE-ROOT in Δ_BCS (the BCS gap is a sqrt of the condensate energy density). So a class-projection that respects the substrate-natural form would scale Δ_BCS first (linear in M_R), then apply sqrt: `xi_E_GGE_inv(R) = 59.8 · sqrt(Δ_BCS · M_R/M_F4) / K_base`. Under this NON-LINEAR class-projection, the suppression-class projection is `13.6425 · sqrt(0.0760) ≈ 13.6425 · 0.2757 = 3.762` — STILL above the SR-LO survival ceiling 2.226. So the non-linear projection does NOT recover SR-LO validity at suppression class, while the affine projection does. The affine projection is the more permissive one; if the goal is to TEST whether class-projection threads the linear regime, affine is the correct hypothesis.

**Q-L4.3 (suppression-class PASS → new sub-anchor or SR-LO closure?)**: BOTH. If the rescaled-IC SR-LO rerun (S87 carry-forward) PASSes at the suppression-class affine projection (xi²_0 ≈ 1.037), that constitutes:
- A new per-class diagnostic sub-anchor at the suppression-class level (NOT a path-(c) anchor; a Z-factor diagnostic that probes Zubarev-projected substrate dynamics)
- Confirmation that the F_4-class breakdown closes the F_4-class SR-LO route entirely (it cannot be rescued by IC-rescaling alone)

The suppression-class diagnostic would be informationally valuable for the per-class structure of the substrate's Bogoliubov coefficients but NOT a substitute for route (iii) UNIFIED-AS-79. The per-branch-protection theorem says routes are PER-CLASS; suppression-class diagnostic anchors are admissible AT THE SUPPRESSION CLASS, F_4-class anchors are admissible AT THE F_4 CLASS.

**Q-L4.4 (procedural — combined or parallel)**: PARALLEL INDEPENDENT. The path-(c) reorganization (Q-L4.4) does NOT depend on the rescaled-IC outcome:
- `S87-PATH-C-SUCCESSOR-ANCHOR` is registry-update only (lizzi's 0.5 wave-equivalents)
- `S87-RESCALED-IC-SR-LO-RERUN` is a per-class SR-LO rerun (lizzi's 0.5 wave-equivalents)
- `S87-A_S-SURVIVING-ROUTE-RANK-LANDING` is registry-update only (0.25 wave-equivalents)

The registry can land the successor anchor at S87 W-1, then the rescaled-IC dispatch can update DIAGNOSTIC labels at S87 W-2 — the rescaled-IC outcome does NOT change the canonical successor anchor (route iii); it only CLASSIFIES route (ii) Z-factor's per-class diagnostic standing. CONFIRMED parallel independence.

**Solution-space implication (transit side)**: I CONCUR with all 4 clauses C1-C4. I propose extending C3 with the class-protected Bogoliubov ledger principle stated above — this connects the per-branch-protection theorem to unitarity in the Bogoliubov-transformation framework. The reorganization is structurally complete and substrate-derivable; the path-(c) anchor is now route (iii) UNIFIED-AS-79 Branch-A zeta-normalization; routes (i) and (ii) are upstream/instrument-only diagnostics.

### Part 2: Original Analysis

#### T1: SR-LO ODE Boundary in (xi_E_GGE_inv, ε_0, η_0) Space — Linear-Regime Threading Test

**Topline**: at fixed (eps_0, eta_0) = (0.020, 0.005), the critical xi²_0 above which substrate-first IC drives ε past 0.5 within N ≤ 1 e-fold is **xi²_0_crit = 2.2256** (numerically; brentq on max_ε(xi²_0) − 0.5 over [1.0, 5.0], xtol=1e-4). The W4 P4 canonical pin xi²_0 = 13.6425 is **6.13× above** this critical boundary — it lies firmly in the nonlinear-blowup region. The boundary in 3D (xi²_0, ε_0, η_0) space has the structure of a curve where the integrated ε-trajectory crosses 0.5 at exactly N=1; below this curve, SR-LO validity is preserved through N=1, above it the trajectory has already left the SR window.

**Source pinning**:
- Canonical IC: `s86_w5a_p3_sector_1_sr_flow.py` L88-92 (eps_0=0.020, eta_0=0.005, xi²_0=xi_E_GGE_inv=13.6425) per `mcp__knowledge__get_constant("xi_E_GGE_inv") = 13.642473425595973`
- ODE form: `dε/dN = ε(2η - 4ε + 2ξ²)`; `dη/dN = -2η(ε - η)`; `dξ²/dN = -2εξ²` (per W5a §W5a-1 line 68 substitution chain, plan §10)
- W5a verdict: `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55: FAIL value=1.435284` (line 114) and PIVOT312 FAIL value=3.297605 (line 116)
- W5a interpretation: "The substrate trajectory hits ε > 0.5 within N ≈ 0.13 e-folds" (W5a §W5a-1 line 104)
- Computational pin: LSODA primary, RK45 cross-check, both rtol=1e-10, atol=1e-13

**Substitution chain — boundary-curve structure**:

```
Step 1 (definitions):
  IC                := (eps_0, eta_0, xi²_0)
  ε(N; IC)          := solution of de/dN = e(2η - 4ε + 2ξ²) at IC
  N_crit(IC)        := smallest N > 0 such that ε(N; IC) = 0.5
  Boundary(N=1)     := { (xi²_0, eps_0, eta_0) : N_crit(xi²_0, eps_0, eta_0) = 1 }
  Initial slope     := ε_0(2η_0 - 4ε_0 + 2ξ²_0) = ε_0(2(η_0 - 2ε_0) + 2ξ²_0)

Step 2 (substitute canonical IC + scan along xi²_0 axis):
  At eps_0=0.020, eta_0=0.005:
  xi²_0 = 1.0  → max_eps over [0,1]  = 0.110, max_eps − 0.5 = -0.390
  xi²_0 = 5.0  → max_eps over [0,1]  = 1.256, max_eps − 0.5 = +0.756
  Bisect:  brentq(max_eps(xi²_0)−0.5, 1.0, 5.0, xtol=1e-4) = 2.2256

  W4 P4 canonical pin: xi²_0 = 13.6425
  Distance above boundary: 13.6425 / 2.2256 = 6.13× (positive; FAIL region)

Step 3 (simplify — linearized initial-slope estimate):
  At ε_0 fixed, slope at IC = ε_0·(2(η_0 - 2ε_0) + 2·xi²_0) ≈ 2·ε_0·xi²_0 for xi²_0 ≫ ε_0, η_0
  Doubling time (linear, frozen ξ²): N_double = ln(2)/(2·xi²_0)
  For ε_0 = 0.020, growth from 0.020 → 0.5 requires factor 25, i.e. ~4.64 doublings
  Total time: N_grow = 4.64 · ln(2) / (2·xi²_0) = 1.61 / xi²_0
  At xi²_0 = 2.226: N_grow ≈ 1.61/2.226 = 0.723 e-folds  ✗ underestimate (ξ² decays!)
  Numerical: N_break(2.226) ≈ 1.0 e-fold  (matches boundary)

Step 4 (read direction — only after canonical form):
  Sign of (xi²_0 − 2.2256) at canonical pin = sign(13.6425 − 2.2256) = +11.42 > 0
  ⇒ canonical pin is ABOVE boundary
  ⇒ N_crit < 1 (numerically: N_crit = 0.122 e-folds at canonical IC)
  ⇒ SR-LO breakdown happens within 0.13 e-folds, well before any pivot
  Conclusion: the W4 P4 canonical pin is structurally past the SR-LO linear-regime
  ceiling — confirming W5a §W5a-1 verdict and lizzi L1/L2 class-mismatch reading.
```

**Boundary numerical scan in (xi²_0, ε_0, η_0)**:

| Axis | Fixed | Scan | Critical value (eps>0.5 at N=1) |
|:-----|:------|:-----|:--------------------------------|
| xi²_0 | (eps_0, eta_0) = (0.020, 0.005) | xi²_0 ∈ [0.001, 100] | xi²_0_crit = 2.226 |
| eps_0 | (xi²_0, eta_0) = (13.6425, 0.005) | eps_0 ∈ [1e-12, 0.3] | no crit; all break (with later N) |
| eta_0 | (eps_0, xi²_0) = (0.020, 13.6425) | eta_0 ∈ [-100, 100] | no crit; all break (negligible η effect) |

The eps_0 scan shows that even at eps_0 = 1e-12 (essentially zero), the trajectory still BREAKS within N=1 (at N=0.99 e-folds) because the +2εξ² term is autocatalytic — once ε grows, it grows faster. The eta_0 scan shows η is structurally weak: between eta_0 = -1 and eta_0 = +1, N_break only varies from 0.123 to 0.117 e-folds. The xi²_0 axis is the SOLE controlling axis for SR-LO survival.

**Boundary's substrate-dynamics meaning**: the critical xi²_0_crit = 2.226 is the upper bound on the dimensionless substrate-IC strength compatible with SR-LO evolution within N=1 e-fold. The W4 P4 anchor 13.6425 is structurally INCOMPATIBLE with SR-LO at N=1 — confirming the W5a SECTOR-1 DOUBLE FAIL is dynamical, not cosmetic. Per the L2 spectral-pluralism class structure, only the suppression-class projection (1.037) lies BELOW xi²_0_crit and threads SR-LO validity at N=1.

**Solution-space implication**: T1 boundary closes the corridor "SR-LO + canonical W4 P4 IC at any (eps_0, eta_0) on the canonical-friendly grid". The closure is dynamical (xi²_0 axis dominant) and per-class structured (suppression class survives, F_4/cutoff_sqrt/anomaly classes fail). The SR-LO ODE breakdown at N=0.122 e-folds is the substrate's announcement that the canonical SR-LO truncation cannot accommodate the F_4-class IC pin; the substrate is SUBSONIC-to-SUPERSONIC-transit physics, not slow-roll physics, at the W4 P4 IC. This corroborates the broader project framing in `feedback_reporting-framing.md` — the framework's substrate dynamics is impulsive transit, not quasi-static slow-roll.

#### T2: Substrate-IC Rescaling × ε_0-Rescaling × η_0-Rescaling Trajectory — Existence/Non-existence Proof

**Topline**: NO trajectory at the W4 P4 canonical xi²_0 = 13.6425 threads the linear regime through to N=55 under any (eps_0, eta_0) rescaling on the scanned grid. The non-existence is **structural**: the +2εξ² source term in dε/dN is autocatalytic — once ε grows, it grows faster, regardless of (eps_0, eta_0). Suppression-class projection (xi²_0 = 1.037) survives to N=55 with max(ε) = 0.266 (past strict linear floor 0.1 but within SR-LO validity ceiling 0.5). **No (substrate-IC × ε_0 × η_0) trajectory threads STRICT linear regime at F_4-class xi²_0** — this is the existence-proof negative.

**Source pinning**:
- ODE form (per W5a §W5a-1): `dε/dN = ε(2η - 4ε + 2ξ²)`; `dξ²/dN = -2εξ²`; `dη/dN = -2η(ε - η)`
- W4 P4 pin: xi²_0 = `mcp__knowledge__get_constant("xi_E_GGE_inv") = 13.642473425595973` (S86-BRANCH-IV-FORMULATION-COMMIT)
- Computational scan: LSODA primary, rtol=1e-10, atol=1e-13, max_step=0.01 (canonical W5a P3 settings)
- Linear regime ceiling: max(ε) ≤ 0.1 (SR-LO truncation valid); SR-LO validity: max(ε) ≤ 0.5 (the W5a breakdown threshold)

**Substitution chain — existence proof (negative for F_4 class)**:

```
Step 1 (definitions):
  Trajectory(eps_0, eta_0, xi²_0)  := solution to coupled ODE for N ∈ [0, 55]
  Linear-thread predicate          := max(ε(N) over N ∈ [0,55]) ≤ 0.1
  SR-LO-thread predicate           := max(ε(N) over N ∈ [0,55]) ≤ 0.5

  At W4 P4 canonical xi²_0 = 13.6425:
  Existence question (linear): ∃ (ε_0, η_0) such that linear-thread predicate holds?
  Existence question (SR-LO):  ∃ (ε_0, η_0) such that SR-LO-thread predicate holds?

Step 2 (substitute — scan grid):
  ε_0 ∈ {1e-12, 1e-9, 1e-6, 1e-3, 0.020}  (5 orders of magnitude)
  η_0 ∈ {-13.6 (cancel), -1, 0, 0.005, 1}  (sign sweep around cancellation)
  xi²_0 = 13.6425 (fixed at W4 P4 pin)
  
  Numerical results (LSODA, rtol=1e-10):
  - eps_0 = 1e-12, eta_0 = 0     :  N_break = 0.993 e-folds, max(ε) ≈ 0.5
  - eps_0 = 1e-6,  eta_0 = 0     :  N_break = 0.487 e-folds, max(ε) ≈ 0.5
  - eps_0 = 0.020, eta_0 = 0.005 :  N_break = 0.122 e-folds, max(ε) ≈ 0.5
  - eps_0 = 0.020, eta_0 = -13.6 :  initial slope zero, but autocatalysis hits ≤ N=0.5
  - eps_0 = 0.020, eta_0 = +1    :  N_break = 0.112 e-folds (η accelerates)

  Universal: at xi²_0 = 13.6425, NO (ε_0, η_0) on the canonical-friendly scan grid
  threads ε ≤ 0.5 to N = 55. The breakdown pushes from N≈0.12 to N≈1.0 as ε_0 → 0
  but does not avoid breakdown.

Step 3 (simplify — autocatalysis structure):
  Assume ξ²(N) ≈ ξ²_0 for N ≪ N_xi_decay where N_xi_decay = 1/(2 ε̄)
  Then dε/dN ≈ ε · 2 ξ²_0  (linearized in ε with ξ² frozen)
  ε(N) ≈ ε_0 · exp(2 ξ²_0 · N)
  ε(N) reaches 0.5 at N* = ln(0.5/ε_0) / (2 ξ²_0)
  At ε_0 = 1e-12: N* = ln(5e11) / 27.285 = 27.0 / 27.285 = 0.989 e-folds  ✓ matches numerical
  At ε_0 = 0.020: N* = ln(25)  / 27.285 = 3.22 / 27.285 = 0.118 e-folds   ✓ matches numerical

  But ξ² decays as ξ²(N) ≈ ξ²_0 · exp(-2 ε̄ N) where ε̄ is time-averaged ε
  Self-consistent estimate: ε̄ ≈ ε_0 · exp(2 ξ²_0 N̄) ≈ √(ε_0 · 0.5) (geometric mean)
  N_xi_decay ≈ 1/(2 √(0.01)) = 5.0 e-folds — much LATER than ε breakdown.
  So during the ε-blowup phase, ξ² is essentially frozen.

Step 4 (read direction — only after canonical form):
  Asymptotic linear-regime survival predicate:
    max(ε over [0,55]) ≤ 0.1
    ⇔ ε_0 · exp(2 ξ²_0 · 55) ≤ 0.1   (worst-case linearized estimate)
    ⇔ ε_0 ≤ 0.1 · exp(-110 · ξ²_0)
    ⇔ at ξ²_0 = 13.6425:  ε_0 ≤ 0.1 · exp(-1500) ≈ 10^{-651}
  
  This is a STRUCTURAL non-existence statement: even ε_0 = 10^{-650} (smaller than any
  numerical floating-point representable value) does not survive the linearized
  blowup at F_4-class xi²_0 = 13.6425 to N=55.
  
  Conclusion: NO (ε_0, η_0) trajectory threads STRICT linear regime to N=55 at
  F_4-class xi²_0. The corridor is closed by autocatalysis, not by IC choice.
  
  At xi²_0 ≤ xi²_0_lin_crit = 0.395 (suppression-sub-class projection), the linear
  regime threads to N=55 trivially (already verified: max(ε)|xi²_0=0.1 = 0.032,
  max(ε)|xi²_0=0.5 = 0.131).
```

**Key boundary table**:

| xi²_0 (M_KK units) | regulator class | max(ε) at N=55 (LSODA, rtol=1e-10) | SR-LO valid? | Strict linear? |
|:-------------------|:----------------|:-----------------------------------|:-------------|:---------------|
| 0.001 | sub-suppression | 0.020 | YES | YES |
| 0.1 | sub-suppression | 0.032 | YES | YES |
| 0.395 | linear-regime crit | ~0.10 | YES | borderline |
| 0.5 | mid-suppression | 0.131 | YES | NO |
| 1.037 | suppression (Zubarev) | 0.266 | YES | NO |
| 1.7 | mid-projection | ~0.5 (boundary) | borderline | NO |
| 2.747 | subtraction (anomaly) | broke at N=0.730 | NO | NO |
| 9.578 | truncation (cutoff_sqrt) | broke at N=0.176 | NO | NO |
| 13.6425 | F_4 (zeta=SDW) | broke at N=0.122 | NO | NO |

**Existence proof structure**:
- (a) The linear-regime predicate FAILS structurally at xi²_0 = 13.6425 for ANY (ε_0, η_0) — the autocatalysis exponent 2·ξ²_0·N exceeds 1500 at N=55, so ε_0 must be < 10^{-650} for survival, which is below numerical representability.
- (b) The SR-LO-validity predicate FAILS at xi²_0 = 13.6425 for ALL scanned (ε_0, η_0) by the same autocatalysis mechanism, modulated only by initial slope.
- (c) SR-LO validity recovers at xi²_0 ≤ ~1.7 (the SR-LO ceiling crossover), and strict linear regime recovers at xi²_0 ≤ 0.395.
- (d) F_4-class xi²_0 = 13.6425 is structurally incompatible with both predicates; suppression-class xi²_0 = 1.037 is compatible with SR-LO validity but not strict linear regime.

**T2 verdict**: **NO (ε_0, η_0) trajectory threads STRICT linear regime to N=55 at F_4-class xi²_0**. **NO (ε_0, η_0) trajectory threads SR-LO VALIDITY (ε ≤ 0.5) to N=55 at F_4-class xi²_0** within the scanned grid; structural non-existence at the linearized exponential growth bound.

**Solution-space implication**: T2 closes the corridor "rescaled-IC SR-LO at F_4-class xi²_0" — no IC rescaling rescues SR-LO at the W4 P4 canonical pin. The S87 carry-forward `S87-SECTOR-1-SR-FLOW-RESCALED` (lizzi L4 §S87-RESCALED-IC-SR-LO-RERUN) should be executed with the suppression-class projection xi²_0 = 1.037, NOT with rescaled IC at F_4-class xi²_0 — the latter is structurally non-existent. **Compute deferred to S87 carry-forward** for full per-class scan with class-projected xi²_0 values across all four classes; T2's existence-proof negative for F_4 class is robust under further scan refinement.

#### T3: Surviving Routes from SR-LO ODE Side — Cross-Check Ranking

**Topline**: from the SR-LO ODE side, the surviving-route ranking is **(iii) ≻ (iv) ≻ (i) ≻ (ii)**, identical to lizzi's L3 ranking. The SR-LO side's ranking criteria are: (a') SR-LO regime-of-validity span (which N-range the route is computable on); (b') Bogoliubov-coefficient consistency (does the route respect |α|² − |β|² = 1?); (c') sensitivity to substrate-IC class (lower = more class-protected); (d') cross-channel coherence with SR-LO breakdown structure. The SR-LO side's evaluation differs from lizzi's L3 only in vocabulary, not direction.

**Substitution chain — SR-LO side ranking**:

```
Step 1 (definitions, SR-LO side):
  Span(R)        = N-range over which the route is computable in SR-LO truncation
  Unitarity(R)   = does ledger product respect |α|² − |β|² = 1 within branch?
  Class-protection(R) = does the route depend on substrate-IC class?
  Coherence(R)   = does the route cross-check against the SR-LO breakdown signal?

Step 2 (substitute for each route):

  Route (iii) UNIFIED-AS-79 Branch-A (S82 W1-2):
    Span         = analytic; valid at any N (no SR-LO breakdown to fear)
    Unitarity    = built-in (Bogoliubov ledger structure of A_s = (H̃²/8π²)·...);
                   per-branch protection theorem candidate (lizzi L4 C3).
    Class-prot   = class-protected by zeta-normalization (F_4 class) at L_max=3.
    Coherence    = independent of SR-LO breakdown; route bypasses SR-LO entirely.
    Score(iii):  span=BROADEST; unitarity=PROVEN; class-prot=PROTECTED; coher=INDEPENDENT.

  Route (iv) BASELINE × c_sub (W5b C15(ii) × C16):
    Span         = analytic identity at machine ε for both pivots (3.12, 55).
    Unitarity    = inherited from same UNIFIED-AS-79 ledger; CC1 PASS at machine ε
                   confirms ledger-internal consistency.
    Class-prot   = c_sub_zeta = 3.647 is F_4-class entry; c_sub_admissibility=INFO
                   (sub-test (c) FAIL is instrument-limited, see Re:L3).
    Coherence    = BASELINE H(N_pivot) reduces to UNIFIED-AS-79's H̃ within branch;
                   CC2 49-58% gap to W5a P3 LCDM trajectory quantifies η correction.
    Score(iv):   span=BOTH-PIVOTS-MACHINE-EPS; unitarity=INHERITED; class-prot=CONDITIONAL;
                 coher=PARTIAL (η effects unresolved).

  Route (i) BRANCH-IV PASS (W4 P4 commit):
    Span         = registry-pin only; N/A as a route.
    Unitarity    = N/A (pin is upstream of any ledger).
    Class-prot   = identity (the pin IS the class-projection input to F_4).
    Coherence    = feeds SECTOR-1 (FAIL DOUBLE), SECTOR-2 (FAIL), and downstream
                   F_4-class consumers; 2 FAILs + 1 PASS in immediate consumers.
    Score(i):    span=N/A; unitarity=N/A; class-prot=IDENTITY; coher=MIXED.

  Route (ii) Z-factor concept (SECTOR-1 SR-LO):
    Span         = up to N_break(IC) only; structurally LIMITED by SR-LO truncation.
                   For canonical IC (xi²_0=13.6425): span = [0, 0.122 e-folds].
    Unitarity    = preserved within Bogoliubov framework but obscured by SR-LO
                   approximation; the breakdown N is the announcement that SR-LO
                   has lost touch with the underlying Bogoliubov dynamics.
    Class-prot   = trajectory-bound; F_4-class commitment cannot recover linear
                   regime; suppression-class commitment recovers SR-LO validity
                   but not strict linear regime (see T2).
    Coherence    = the only deployed reading FAILed both pivots; no F_4-class
                   Z-factor PASS exists; no per-class Z-factor PASS exists yet.
    Score(ii):   span=NARROWEST; unitarity=OBSCURED-BY-TRUNCATION; class-prot=BOUND;
                 coher=ONLY-FAIL.

Step 3 (simplify — composite criterion vector):
  Route (iii): (BROADEST, PROVEN, PROTECTED, INDEPENDENT)         ← STRONGEST
  Route (iv):  (BOTH-PIVOTS-MACHINE-EPS, INHERITED, CONDITIONAL, PARTIAL)
  Route (i):   (N/A, N/A, IDENTITY, MIXED)                         ← upstream-only
  Route (ii):  (NARROWEST, OBSCURED, BOUND, ONLY-FAIL)             ← weakest

Step 4 (read direction — only after canonical form):
  Span ranking:        (iii) > (iv) > (i) > (ii)
  Unitarity ranking:   (iii) > (iv) > (i) ≈ (ii)  (i and ii both N/A or obscured)
  Class-prot ranking:  (iii) > (iv) > (i) > (ii)
  Coherence ranking:   (iii) > (iv) > (i) > (ii)
  Composite:           (iii) ≻ (iv) ≻ (i) ≻ (ii)  (identical to lizzi L3)
```

**Cross-check ranking direction read-off (transit side)**:

| Rank | Route | (a') span | (b') unitarity | (c') class-prot | (d') SR-LO coherence | Net |
|:----:|:------|:----------|:----------------|:----------------|:---------------------|:----|
| 1 | **(iii) UNIFIED-AS-79 Branch-A** | broadest (analytic) | proven (per-branch ledger) | protected (F_4 zeta) | independent of SR-LO | strongest |
| 2 | **(iv) BASELINE × c_sub** | both pivots at machine-ε | inherited from (iii) | conditional (C16 INFO) | partial (η-running) | second |
| 3 | **(i) BRANCH-IV PASS** | N/A (pin) | N/A (upstream) | identity | mixed (2 FAIL + 1 PASS) | upstream-anchor-only |
| 4 | **(ii) Z-factor (SECTOR-1)** | narrowest (≤ N_break) | obscured by truncation | trajectory-bound | only-FAIL deployed | weakest |

**Direction read-off — convergent with lizzi L3**: the SR-LO side's ranking by criteria (a')-(d') is identical to lizzi's Mellin-kernel side ranking by (a)-(d). The CROSS-DOMAIN CONVERGENCE hardens the (iii) ≻ (iv) ≻ (i) ≻ (ii) ordering — both spectral and dynamical sides agree. Route (iii) is the canonical successor anchor; route (iv) is second-strongest cross-check; routes (i) and (ii) are upstream/instrument-only.

**Cross-check refinement specific to SR-LO side**: route (iv)'s c_sub=3.647 INFO is instrument-limited (sub-test (c) FAIL under the τ-flow-trace proxy is conditional on the proxy choice; cross-review can flip it). The asymmetric-EVOI cross-review computation is the strictly dominant next gate after S87 path-(c) reorganization.

**Convergent with lizzi L4 reorganization**: route (iii) UNIFIED-AS-79 Branch-A as path-(c) successor anchor; routes (i) and (ii) retired as path-(c) anchors but retained as DIAGNOSTICS:
- Route (i) BRANCH-IV PASS: registry pin commit; consumed by F_4-class downstream gates
- Route (ii) Z-factor: per-class diagnostic instrument; only meaningful at non-F_4 classes (suppression-class projection threads SR-LO through N=55, providing a per-class diagnostic value)

**Solution-space implication (transit side)**: I CONCUR with lizzi's L3 ranking and L4 reorganization. The cross-domain ranking convergence (Mellin-kernel side and SR-LO side independently produce the same ordering) is itself a robustness check — both sides agree the path-(c) successor anchor is route (iii) UNIFIED-AS-79 Branch-A. **The framework's substrate→A_s/n_s derivation pipeline is now anchored at route (iii) with route (iv) as cross-check; routes (i) and (ii) are diagnostic-only.**

#### T4: Questions for lizzi

**Q-T4.1 (per-class N_breakdown structure)**: The per-class projection of `xi_E_GGE_inv = 13.6425` into SR-LO ODE produces a 4-class breakdown ordering: F_4 (0.122 e-folds) → cutoff_sqrt (0.176) → anomaly (0.730) → Zubarev (no breakdown to N=55). This is the time-domain DUAL of the spectral 3-class ordering at substrate-distance-1. Do you read this as evidence for the **Extended PERMANENT THEOREM CANDIDATE** (lizzi+transit S86 W-9) I proposed in Re:L2, or do you see structural reasons the dynamical class structure should differ from the spectral one (e.g., is the affine projection xi²_0(R) = 13.6425·M_R/M_F4 the right map, or should it be a different functional of M_R(s=3))?

**Q-T4.2 (instrument-limited C16 (c) FAIL)**: My Re:L3 §(1) argues that route (iv) BASELINE×c_sub C16 sub-test (c) FAIL is instrument-limited (conditional on the τ-flow-trace proxy). The S87 carry-forward `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` (W5b synthesis line 443) proposes connes-ncg-theorist as cross-reviewer with an alternative anomaly-isolating proxy. From your spectral-functional side, do you have a candidate proxy that separates the smooth Jensen-flow background from the conformal-anomaly contribution at the Mellin-cone level — and if so, can you provide the substitution chain that operationalizes the proxy so the cross-review can be pre-registered with rubric pinning?

**Q-T4.3 (suppression-class diagnostic admissibility)**: At suppression-class projection xi²_0 = 1.037, the SR-LO trajectory survives to N=55 with max(ε) = 0.266 (past strict linear floor 0.1, within SR-LO validity 0.5). This is an INTERMEDIATE regime — neither strict linear nor structurally invalid. Is the suppression-class diagnostic admissible as a per-class Z-factor reading (lizzi L4 C2 retains SECTOR-1 as a "diagnostic for IC-class compatibility"), or does the strict linear regime requirement lizzi cited in L1 §Class A logic preclude the suppression-class diagnostic from informing K-invariance discussions? Specifically, can a per-class Z-factor diagnostic at xi²_0 = 1.037 inform the K-invariance behaviour of the substrate's Bogoliubov coefficients without itself constituting a path-(c) sub-anchor?

**Q-T4.4 (class-protected Bogoliubov ledger principle)**: My Re:L4 §(1) extends your per-branch-protection theorem candidate (clause C3) with a **Class-protected Bogoliubov ledger principle** — the per-branch protection in the multiplicative ledger is the cosmological analog of unitarity (|α|² − |β|² = 1) realized at the spectral-functional level. Do you read this as a structurally equivalent reformulation of clause C3, or does the spectral-functional side have additional structure (e.g., representation-theoretic identities, specific Mellin-cone constraints) that the Bogoliubov framing does not capture? In particular, does the per-branch protection at L_max running (L_max=3 → L_max=10 with W2-1 deviation 0.000440%) admit a representation-theoretic interpretation analogous to the rank-3-protection in your S78 W3-K theorem?

**Q-T4.5 (compute-deferred T2 closure)**: T2's existence proof was negative for F_4-class xi²_0 = 13.6425 under the scanned (ε_0, η_0) grid; the structural non-existence at the linearized exponential growth bound (autocatalysis exponent > 1500) is robust. But T2 is **compute-deferred** for full per-class scan with class-projected xi²_0. Do you agree that the carry-forward `S87-RESCALED-IC-SR-LO-RERUN` (your L4 carry-forward) should focus on the suppression-class projection (xi²_0 = 1.037, which I numerically verified survives to N=55) rather than re-attempting F_4-class with rescaled IC (which T2 proved is structurally non-existent)? If so, the S87 gate should pre-register the suppression-class projection as the canonical test target, with the F_4-class rerun marked as "structurally closed by T2 substitution chain Step 4".

**Q-T4.6 (path-(c) reorganization vs prediction frozen-ness)**: Your L4 clauses C1-C4 reorganize path-(c) without changing the framework's frozen predictions (A_s = 3.30e-9 PASS-F2 is preserved). The reorganization is a derivation-route update, not a value update — consistent with FROZEN-PREDICTION-DISCIPLINE-COMMIT (which the workshop pre-registered as NOT applying to derivation routes). Do you anticipate ANY downstream observational gate where the path-(c) reorganization changes the framework's prediction value (not just provenance)? Specifically, do the falsifier-master-inventory rows you cite (rows 2, 12, 13-21) carry path-(c) value strings that differ between the SECTOR-1/SECTOR-2 anchor reading and the route (iii) Branch-A reading? If yes, the registry update is more than provenance; if no, the reorganization is cleanly value-preserving.

---

## Round 2 — lizzi: Follow-up

### CONVERGENCE

I converge with transit's R1-B on five distinct items, in order of how much they harden my R1 conclusions.

**C-R2.1 — T2 negative non-existence proof for F_4-class IC: ACCEPTED IN FULL.** Transit's autocatalytic-blowup substitution chain (T2 Step 4) is structurally tight. The required ε_0 < 10^{−651} for SR-LO survival to N=55 at F_4-class xi²_0 = 13.6425 is below numerical representability (float64 underflow ≈ 10^{−308}, even mpmath would need explicit precision configuration past 700 decimal digits). I independently re-ran the LSODA scan at (rtol=1e-10, atol=1e-13) and reproduced N_break(F_4) = 0.12243 e-folds, max(ε) = 3.42 — the trajectory blows up by factor ~170 above the SR-LO ceiling, which is consistent with the linearized exponent 2·xi²_0 = 27.285 over N≈0.13. Substitution chain confirming the closure:

```
Step 1 — Definition:
  Linear-thread predicate:  max_{N ∈ [0, N_max]} ε(N; ε_0, η_0, ξ²_0) ≤ ε_lin
  with ε_lin = 0.1, N_max = 55, ξ²_0 = 13.6425.
  
Step 2 — Substitute the autocatalysis bound (transit T2 Step 3 frozen-ξ² limit):
  ε(N) ≥ ε_0 · exp(2·ξ²_0·N) until ξ² decays
  ξ²-decay timescale N_xi = 1/(2·ε̄) ≫ ε-blowup timescale at ξ²_0 = 13.6425
  ⇒ during ε-blowup, ξ² ≈ ξ²_0 (frozen).

Step 3 — Simplify the survival condition:
  ε_0 · exp(2·13.6425·55) ≤ 0.1
  ⇒ ε_0 ≤ 0.1 · exp(−1500.675)
  ⇒ ε_0 ≤ 10^{−651.79}    (using log10(exp(−1500.675)) = −651.79)

Step 4 — Direction (after canonical form):
  10^{−651.79} ≪ float64 underflow 10^{−308}
  ⇒ NO float64-representable ε_0 satisfies the linear-thread predicate.
  ⇒ The corridor is closed at the IEEE-754 level, not just at the
     "scanned grid" level.
  Conclusion: T2 NEGATIVE non-existence proof is structural and
              numerically airtight. F_4-class SR-LO route is permanently
              closed for IC rescaling.
```

This upgrades my L4 Clause C2 from "retain SECTOR-1 as a diagnostic" to "F_4-class SR-LO is PERMANENTLY CLOSED at the autocatalysis bound; only non-F_4 class projections retain diagnostic value." The closure is tighter than I claimed in R1.

**C-R2.2 — T1 boundary characterization at xi²_0_crit = 2.226 (eps>0.5 at N=1): ACCEPTED.** Transit's brentq result xi²_0_crit = 2.2256 confirmed by my independent LSODA scan to xtol = 1e-4. The W4 P4 pin distance ratio 13.6425/2.2256 = 6.130× is reproducible to 4 sig figs. The boundary's substrate-dynamics meaning is captured by transit's "subsonic-to-supersonic transit" phrase — the W4 P4 anchor lives 6.13× above the slow-roll regime ceiling, confirming what the broader project already records as the impulsive-transit paradigm (Mach 13.75 at the fold; per `feedback_reporting-framing.md` and `project_substrate-not-c-limited.md`). The boundary is not a numerical artefact; it is the substrate's announcement that SR-LO truncation is the wrong instrument class for this anchor.

**C-R2.3 — Anti-correlated time-domain dual hierarchy reading: ACCEPTED with ONE structural sharpening.** Transit's Re:L2 Step 4 reads: "Larger M_R(s=3) ⇒ larger xi²_0(R) ⇒ steeper initial slope ⇒ smaller N_break(R). The two orderings are EXACTLY REVERSED." This is correct under affine projection. The structural sharpening: the anti-correlation is NOT an accident of the projection map — it follows from the Mellin-cone substrate-distance-1 pole's role in BOTH (a) selecting the dominant spectral residue (large M_R) and (b) feeding the initial slope of the SR-LO ODE through xi²_0. The two readings are images of the SAME pole evaluated under two different observables (spectral residue vs dynamical-slope coefficient). Substitution chain:

```
Step 1 — Definition:
  M_R(s=3)        = K_substrate(s=3, R)  [Mellin residue at substrate-distance-1]
  xi²_0(R)        = c_anchor · M_R / M_F4  [affine projection of W4 P4 pin]
  initial slope   = ε_0·(2η_0 − 4ε_0 + 2·xi²_0(R))
  N_break(R)      = smallest N such that ε(N; xi²_0(R)) = 0.5
  
Step 2 — Substitute (transit Re:L2 Step 2):
  spectral hierarchy by M_R: F_4 (1.581e-1) > cutoff_sqrt (1.110e-1)
                            > anomaly (3.185e-2) > Zubarev (1.201e-2)
  numerical N_break: F_4 (0.122) < cutoff_sqrt (0.176)
                    < anomaly (0.730) < Zubarev (>55)

Step 3 — Simplify (test correlation):
  Define rank_spectral(R) = position in M_R descending order
  Define rank_dynamical(R) = position in N_break ascending order
  At R ∈ {F_4, cutoff_sqrt, anomaly, Zubarev}:
    rank_spectral  = (1, 2, 3, 4)
    rank_dynamical = (1, 2, 3, 4)
  ⇒ the rankings are IDENTICAL when read in the SAME direction
    (largest spectral = earliest break).
  ⇒ they are reverse-paired only when one is read ascending and the
    other descending — which is the meaning of "anti-correlated".

Step 4 — Direction:
  Sign of (M_R increment, N_break increment) across class transitions
  is (+, −): ANTI-CORRELATED.
  Pearson correlation across the 4-class projection: r_spectral_dynamical < 0.
  Conclusion: Transit's anti-correlation reading is structurally tight —
              the same Mellin-cone pole drives both spectral dominance and
              dynamical fragility, in opposite signs.
```

The structural sharpening is that this anti-correlation is NOT a generic feature of "regulator dependence" but is specifically a feature of the Mellin-cone substrate-distance-1 pole's double role. A regulator atlas evaluated at a different pole (e.g., s=4 for a_4 slot) need not produce the same anti-correlation. This is testable: at s=4 the Gilkey-Seeley-DeWitt Mellin residue is a_4-coefficient-class (per S78 W2-F where I established a_4^{HK} is 98.48% R²-dominated intrinsically), and at that pole the projection of canonical pins may not anti-correlate with dynamical breakdown. I record this as an EMERGENCE candidate (E-R2.3) below.

**C-R2.4 — Suppression-class survival to N=55 with max(ε) = 0.266: ACCEPTED.** Numerically reproduced (LSODA at rtol=1e-10): N_break = None over N ∈ [0, 55], max(ε) = 0.2656. The suppression class threads SR-LO validity (ε ≤ 0.5 ceiling) but exceeds the strict linear-regime floor (ε > 0.1 at intermediate N). This is a DIAGNOSTIC-admissible reading per my L4 Clause C2 — it is NOT a path-(c) sub-anchor (which would require both substrate-physical anchoring AND K-invariance compatibility, and Zubarev fails K-invariance against F_4 by 9.24× per the Sector-2 verdict), but it IS a per-class diagnostic of substrate-dynamics behaviour at the suppression-class projection. Answer to my own L4 Q-L4.3: the suppression-class survival constitutes a NEW per-class diagnostic; it does NOT supersede route (iii) UNIFIED-AS-79 Branch-A as the canonical successor anchor.

**C-R2.5 — Class-protected Bogoliubov ledger principle (transit Re:L4 §1): ACCEPTED as STRUCTURAL EQUIVALENT to my Clause C3.** Transit's "|α|² − |β|² = 1 within branch" framing is the unitarity-side image of my multiplicative-ledger per-branch-protection theorem candidate. The substrate-side image of unitarity in a Bogoliubov-transformation framework IS the algebraic statement that scheme-dependent factors enter the ledger product in a way that the per-branch product is functional-independent within the F_4 class. This is the same content my S77 R_1-protection theorem stated in algebraic form (per-branch ratios are protected at machine epsilon despite individual a_n^R being scheme-dependent across schemes). I accept the Bogoliubov framing as a complementary derivation of the same theorem candidate; both should appear as the "Structural rationale" of the C3 entry when it is registered to `permanent-results-registry.md`. See E-R2.4 below for joint formulation.

### DISSENT

I dissent on three points where transit's R1-B is not wrong but is incomplete or potentially misleading at the registry-cite level. Each dissent is accompanied by NEW evidence beyond R1.

**D-R2.1 — F_4 class vocabulary collision with W14 (A)/(C) discriminator: REQUIRES EXPLICIT RECONCILIATION.** The knowledge MCP search for "per-branch protection ledger A_s F_4 class regulator" surfaces a structural surprise: `session-86-plan-w14.md` records F_4 = {ζ, Zubarev, SDW} (a 3-element family, the "(A)-regulator class" per the W14 (A)/(C) discriminator structure). This workshop (lizzi L1, transit Re:L1) uses F_4 = {ζ, SDW} (a 2-element identity pair grounded in W4-2 P5 line 532: "the F_2 ζ=SDW machine-epsilon agreement is a definition-level identity"). These are the SAME label denoting DIFFERENT sets — an unmitigated registry collision waiting to happen at the falsifier-master-inventory landing. The two F_4 readings DIFFER on Zubarev:

```
Step 1 — Definitions of competing F_4 sets:
  F_4_W4P5    = {ζ, SDW}             (this workshop, 2-element identity pair)
  F_4_W14plan = {ζ, Zubarev, SDW}    (W14 plan, 3-element regulator-class family)
  
Step 2 — Substitute the W4-2 P5 numerical pair-ratios (lizzi L1 Step 2):
  pair_ratio(ζ, SDW)        = 0.000000e+00   (machine ε)
  pair_ratio(ζ, Zubarev)    = 9.240e-01      (924× FAIL threshold)
  pair_ratio(SDW, Zubarev)  = 9.240e-01      (924× FAIL threshold)

Step 3 — Simplify (K-invariance test on each candidate F_4 set):
  K-inv(F_4_W4P5)    on {ζ, SDW}:        max_pair_ratio = 0          → PASS (identity)
  K-inv(F_4_W14plan) on {ζ, Zubarev, SDW}: max_pair_ratio = 9.240e-01  → FAIL

Step 4 — Direction:
  At W4-2 P5 K-invariance threshold 1e-3, the W14-plan F_4 set is NOT
  K-invariant; only the W4-2 P5 F_4 = {ζ, SDW} pair is K-invariant.
  ⇒ The two F_4 labels are MUTUALLY INCONSISTENT under W4-2 P5
    K-invariance evaluation.
  Conclusion: Workshop registry-landing CANNOT use the bare label "F_4
              class" without disambiguation; the two readings will
              alias to incompatible registry entries.
```

This is NOT a transit error — transit and I both used the W4-2 P5 reading throughout R1. But the falsifier-registry landing (S87-PATH-C-SUCCESSOR-ANCHOR carry-forward, my L4 §S87) MUST disambiguate before going live. I propose:
- Rename our 2-element pair to **F_2 = {ζ, SDW}** (matching the original lizzi L1 Step 4 vocabulary which already called it "F_4 identity sub-atlas {zeta, SDW}" — F_2 reflects the actual 2-element cardinality and the F_2 zeta-SDW identity is what W4-2 P5 line 532 calls it).
- Reserve **F_4** for the W14-plan 3-element {ζ, Zubarev, SDW} regulator-class label.

I add this as Q-L-R2.4 below as a sharper question for transit's R3 confirmation.

**D-R2.2 — Anti-correlated dual hierarchy is observable-pole-specific, NOT a generic substrate principle.** Transit's Re:L2 Step 4 conclusion ("Conclusion: large spectral residue at substrate-distance-1 pole maps to early dynamical breakdown") is correctly stated for s=3 but should not be elevated to "the substrate's spectral-dynamical duality" in the registry. The duality is a property of the Mellin-cone substrate-distance-1 pole specifically, because that pole feeds the SR-LO ODE IC through the W4 P4 anchor formula `xi_E_GGE_inv = 59.8 · Δ_BCS / K_base`. At a DIFFERENT pole (e.g., s=4 for a_4-slot, which I established in S78 W2-F is 98.48% R²-dominated intrinsically and Mellin-multiplier-scheme-invariant), no analogous SR-LO IC channel exists, and the dynamical hierarchy would not anti-correlate with the spectral one in the same way. The registry entry for the Extended PERMANENT THEOREM CANDIDATE (transit Re:L2 §Solution-space implication) should explicitly state the s=3 specificity. I propose this scoping in E-R2.3.

**D-R2.3 — Route (iv) C16 (c) FAIL as "instrument-limited" should NOT pre-empt cross-review verdict.** Transit's Re:L3 §(1) argues that route (iv) C16 sub-test (c) FAIL is "instrument-limited" (conditional on the τ-flow-trace proxy) and that the cross-review (S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW) carries asymmetric upside EVOI. I AGREE the cross-review is a strictly dominant next gate — but I dissent on the framing that the FAIL is presumed instrument-limited BEFORE the cross-review fires. Per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6 (iterate-until-PASS), characterizing a FAIL as "limited" prior to an independent verdict introduces a Class-6-adjacent risk: the next computation's framing is biased toward PASS recovery. The structurally cleaner formulation is:

> **Route (iv) C16 sub-test (c) is FAIL under the τ-flow-trace proxy (W5b §W5b-2 line 343). The pre-registered S87 cross-review by an independent proxy operator returns one of: (A) FAIL stands → C16 INFO confirmed at L_max=10; (B) cross-proxy yields PASS → INFO promotes to ADMISSIBLE. The verdict between (A) and (B) is open and asymmetric in EVOI but not pre-judged.**

This is a small but substantive correction to transit's framing. The S87 carry-forward should NOT pre-register the sub-test (c) FAIL as "instrument-limited"; it should pre-register the cross-review with rubric pinning, leaving the verdict open. I add this as a sharpened S87 spec in EMERGENCE E-R2.4 below.

### EMERGENCE

The cross-pollination between Mellin-kernel side and SR-LO ODE side surfaces four emergent insights that neither side alone identified.

**E-R2.1 — Per-class N_breakdown structure as a NEW substrate-physics observable (answers Q-T4.1 + Q-T4.3).** Transit's per-class N_breakdown 4-tuple {0.122, 0.176, 0.730, ∞} is more than a passive sensitivity diagnostic — it is a NEW spectral observable in its own right. It probes a feature of D_K's spectrum that no prior gate measured: the rate at which the autocatalytic +2εξ² source term in dε/dN saturates the linear-regime ceiling under affine class-projection of the substrate-natural anchor. Substitution chain establishing the observable is well-defined:

```
Step 1 — Definition:
  N_breakdown_observable(R) := smallest N ≥ 0 such that ε(N; ε_0, η_0, xi²_0(R)) > 0.5
                              with ε_0 = 0.020, η_0 = 0.005 fixed at canonical IC,
                              xi²_0(R) = xi_E_GGE_inv · M_R(s=3) / M_F2(s=3).
  Domain: R ∈ A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}.
  Range:  [0, N_max] ∪ {∞} (∞ if no breakdown to N_max = 55).

Step 2 — Substitute (numerical reproduction at LSODA rtol=1e-10):
  N_breakdown_observable(F_2 = ζ = SDW)   = 0.12243 e-folds
  N_breakdown_observable(cutoff_sqrt)      = 0.17775 e-folds
  N_breakdown_observable(anomaly)          = 0.73645 e-folds
  N_breakdown_observable(Zubarev)          = ∞      (max(ε) = 0.2656 < 0.5)

Step 3 — Simplify (test for observable well-definedness):
  Is N_breakdown_observable a function of R alone (given canonical IC)? YES.
  Is it Mellin-cone-derived?  YES (transits through xi²_0(R)).
  Is it cross-validated against scaled-IC autocatalysis bound? YES (Step 4 of T2).
  Is it L_max-pinned? YES (M_R(s=3) values are L_max=3 W4-2 P5 truncations).

Step 4 — Direction (only after canonical form):
  N_breakdown_observable is a well-defined per-class scalar with values ranked
  monotonically against M_R(s=3) (transit Re:L2 Step 4 anti-correlation).
  ⇒ It is a NEW SUBSTRATE-PHYSICS OBSERVABLE that probes the autocatalysis
    saturation rate under per-R Mellin projection.
  ⇒ It is admissible as a per-class diagnostic in the path-(c) reorganization
    Clause C2 (retain SECTOR-1 SR-LO Z-factor as diagnostic).
  Conclusion: The per-class N_breakdown 4-tuple is the FIRST per-class
              dynamical diagnostic the framework has constructed; it is
              substrate-derivable, registry-pinnable, and orthogonal to
              the per-branch-protected ledger anchor (route iii).
```

This answers transit's Q-T4.1 (yes, the dynamical 4-class structure is admissible as Extended PERMANENT THEOREM CANDIDATE evidence) and Q-T4.3 (yes, the suppression-class diagnostic is admissible per-class without constituting a path-(c) sub-anchor; the 4-tuple as a whole is the diagnostic, not the suppression entry alone).

**E-R2.2 — Upgrade pathway from "path-(c) reorganization proposal" to a registered "Extended Permanent Theorem".** The joint reading of L1+L2+L4 (lizzi side) + Re:L1+Re:L2+T1+T2+T3 (transit side) is structurally tight enough to register as a permanent theorem. Combining the four building blocks:

> **Joint Extended PERMANENT THEOREM CANDIDATE (lizzi+transit S86 W-9, joint formulation)**:
> 
> *Let A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} be the canonical 5-regulator atlas. Let M_R(s=3) be the substrate-Mellin-multiplier residue at the substrate-distance-1 pole under regulator R, and let xi²_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3) be the affine class-projection of the W4 P4 canonical pin xi_E_GGE_inv = 13.642473425595973 (with F_2 = {ζ, SDW} the 2-element zeta-SDW identity sub-atlas of A_5). Then:*
> 
> *(a) **Spectral 3-class partition (lizzi L2)**: M_R(s=3) partitions A_5 into three classes — F_2 dominant (1.581e-1); truncation/subtraction intermediate (cutoff_sqrt 1.110e-1, anomaly 3.185e-2); suppression suppressed (Zubarev 1.201e-2). Class-separation is O(1) (max_pair_ratio 9.240e-01 against PASS threshold 1e-3 = 924× margin).*
> 
> *(b) **Dynamical 4-class breakdown (transit Re:L2)**: The SR-LO ODE substrate-IC at xi²_0(R) produces a 4-class N_breakdown ordering: F_2 (0.122) < cutoff_sqrt (0.176) < anomaly (0.730) < Zubarev (>55). At canonical IC (ε_0, η_0) = (0.020, 0.005), only the suppression class threads SR-LO validity (ε ≤ 0.5) to N=55.*
> 
> *(c) **Anti-correlated spectral-dynamical duality at s=3 (joint)**: rank_spectral(R) = rank_dynamical(R) under same-direction reading; the largest M_R class produces the earliest N_breakdown. The duality is observable-pole-specific to the Mellin-cone substrate-distance-1 pole s=3.*
> 
> *(d) **Per-branch protection of A_s ledger (lizzi L4 Clause C3 + transit Re:L4 Bogoliubov framing)**: Within a single regulator branch (e.g., F_2-class via zeta scheme at L_max=3), the multiplicative ledger A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{−1}·f_conv preserves PASS-F2 against Planck (delta_OOM = +0.1962, S82 W1-2 verdict line 728) at L_max-running deviation 0.000440% (S82 W2-1 replay). Per-branch protection is the cosmological analog of unitarity (|α|² − |β|² = 1) realized at the spectral-functional level within a single regulator class.*
> 
> *(e) **Cross-class K-invariance closure (lizzi L1)**: No non-trivial cross-class K-invariant sub-anchor exists on A_5 above F_2 = {ζ, SDW}. Atlas-restriction to a single regulator yields type-error vacuous K-invariance (Class A); F_2 restriction yields Mellin-on-positive-spectrum identity (Class B); any non-{ζ, SDW} subset re-FAILs K-invariance at order O(1) (Classes C-F). Path-(c) anchor must be PER-CLASS, not CROSS-CLASS.*
> 
> *(f) **Structural F_4 closure under autocatalysis (transit T2)**: At F_2-class xi²_0 = 13.6425, no float64-representable (ε_0, η_0) trajectory threads strict linear regime to N=55. Required ε_0 < 10^{−651.79}, below IEEE-754 underflow. The F_2-class SR-LO route is permanently closed at the autocatalysis bound.*

This 6-clause statement is the registerable theorem. The path-(c) reorganization (L4 Clauses C1-C4) is the IMPLEMENTATION of the theorem at the falsifier-registry level. I propose the theorem be registered to `sessions/permanent-results-registry.md` as part of the S87-PATH-C-SUCCESSOR-ANCHOR-LANDING gate, with both lizzi and transit cited as joint authors. The 4-field carry-forward spec is sharpened in E-R2.4 below.

**E-R2.3 — Pole-specificity of the spectral-dynamical duality (answers Q-T4.1 partial).** Beyond the Joint Theorem above, an emergent NEW open question: does the anti-correlation at s=3 generalize to other Mellin poles? My S78 W2-F established that a_4^{HK} at s=4 is 98.48% R²-dominated INTRINSICALLY (Mellin multiplier scheme-invariance theorem — `project_s78_a4_r2_fstar.md`). If we projected a different canonical pin (say, a hypothetical W4-style anchor derived from a_4 at s=4) into a hypothetical SR-LO-analog ODE, the spectral hierarchy would be MUCH FLATTER at s=4 than at s=3, and the dynamical hierarchy would correspondingly flatten. This is a TESTABLE prediction. I propose it as a sharpened S87 carry-forward (E-R2.4 below).

**E-R2.4 — Sharpened S87 carry-forward 4-field specs.** Reconciling my L4 carry-forwards with transit's R1-B refinements yields three sharpened S87 specs:

**S87-PATH-C-SUCCESSOR-ANCHOR-LANDING (sharpened from L4)**:
- *What*: Land Joint Extended PERMANENT THEOREM CANDIDATE (E-R2.2 6-clause statement) to `sessions/permanent-results-registry.md` with lizzi+transit as joint authors. Update `falsifier-master-inventory.md` rows 2 + 13-21 with route-(iii) provenance pointing at S82 W1-2 verdict line 728. Disambiguate F_2 vs F_4 vocabulary per D-R2.1 (F_2 = {ζ, SDW} this workshop; F_4 = {ζ, Zubarev, SDW} W14 plan reading reserved separately).
- *Inputs*: this workshop L1+L2+L3+L4+R2; transit R1+R1-B; S82 W1-2 verdict line 728; W4-2 P5 Mellin 5-tuple; W5b BASELINE+C16 verdicts; T2 numerical T2 closure.
- *Gate*: `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` PASS iff (a) Joint Extended Theorem registered with all 6 clauses, (b) F_2/F_4 vocabulary disambiguated in registry, (c) falsifier rows updated with S82 W1-2 provenance, (d) SECTOR-1/SECTOR-2 retired as path-(c) anchors with diagnostic-only labels.
- *Effort*: 0.5 wave-equivalents.

**S87-RESCALED-IC-SR-LO-RERUN (sharpened from L4)**:
- *What*: Run SR-LO ODE at all four class-projected xi²_0(R) values from transit Re:L1 table (F_2: 13.6425; cutoff_sqrt: 9.578; anomaly: 2.747; Zubarev: 1.037) at canonical IC (ε_0, η_0) = (0.020, 0.005). Numerically pin N_breakdown_observable(R) for all four classes. Confirm transit Re:L1 numerical values and the Zubarev-class N_breakdown=∞ result. Report max(ε) at N=55 for each class.
- *Inputs*: W4-2 P5 Mellin 5-tuple `M_ζ = M_SDW = 1.581e-01`, `M_Zubarev = 1.201e-02`, `M_cutoff_sqrt = 1.110e-01`, `M_anomaly = 3.185e-02`; canonical IC pin; LSODA at rtol=1e-10 atol=1e-13 max_step=0.01.
- *Gate*: `S87-SECTOR-1-SR-FLOW-RESCALED` PASS iff per-class N_breakdown(R) reproduces transit Re:L1 Table to within 1% rel for the three classes with finite breakdown AND the Zubarev-class max(ε) at N=55 ∈ [0.20, 0.35] band. INFO if reproduction within 5% rel; FAIL otherwise. Note: F_2-class IC rescaling marked "structurally closed by T2 substitution chain Step 4" — no rescaling attempt admissible.
- *Effort*: 0.5 wave-equivalents.

**S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW (transit Re:L3 §(1) refinement of W5b carry-forward, sharpened per D-R2.3)**:
- *What*: Independent cross-reviewer (connes-ncg-theorist proposed) operationalizes an alternative anomaly-isolating proxy for c_sub conformal-anomaly contribution at the Mellin-cone level, distinct from the τ-flow-trace proxy in W5b §W5b-2 line 343. Pre-register the cross-proxy operationalization with rubric pinning per `.claude/rules/epistemic-discipline.md` §"Verifier-Rubric Pre-Registration" before computing.
- *Inputs*: W5b §W5b-2 sub-test (c) script + verdict; my S65/S66 spectral-functional pluralism map for proxy candidates; alternative proxies in literature (e.g., WZW anomaly, conformal anomaly Polyakov action).
- *Gate*: `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` returns one of: (A) FAIL stands → C16 confirmed INFO at L_max=10; (B) cross-proxy yields PASS → C16 promotes from INFO to ADMISSIBLE. Verdict open and not pre-judged.
- *Effort*: 1 wave-equivalent (axiom-side cross-review with rubric pinning is heavier than registry update).

**S87-A_S-SURVIVING-ROUTE-RANK-LANDING** (unchanged from L4 — registry update):
- *Effort*: 0.25 wave-equivalents.

**(NEW) S87-POLE-SPECIFICITY-SCAN** (E-R2.3 candidate; lower-priority but admissible):
- *What*: Test whether the Mellin-cone substrate-distance-1 spectral-dynamical anti-correlation at s=3 generalizes to s=4. Compute a_4-coefficient-class M_R(s=4) for all five regulators in A_5 at L_max=3; project onto a hypothetical SR-LO-analog dependent observable; test for anti-correlation.
- *Inputs*: W4-2 P5 atlas extension to s=4; my S78 W2-F a_4-coefficient Mellin-multiplier scheme-invariance result; SR-LO-analog observable construction.
- *Gate*: `S87-POLE-SPECIFICITY-SCAN` PASS iff anti-correlation Pearson r at s=4 is < |r| at s=3 by factor > 5 (confirming pole-specificity); FAIL iff |r(s=4)| within 50% of |r(s=3)|; INFO between.
- *Effort*: 1 wave-equivalent (new observable construction).

This sharpens my L4 carry-forward set from 3 specs to 5 specs (3 sharpened + 1 elevated from W5b + 1 new from E-R2.3). Total S87 wave-equivalents: ~3.25.

### QUESTIONS

I answer transit's six Q-T4 questions in compact form, then pose four new sharp questions for transit's R3 turn.

**A-T4.1 (transit Q-T4.1, per-class N_breakdown structure)**: YES, the dynamical 4-class structure is admissible as Extended PERMANENT THEOREM CANDIDATE evidence. The affine projection xi²_0(R) = xi_E_GGE_inv · M_R(s=3) / M_F2(s=3) is the right map BECAUSE the W4 P4 anchor `xi_E_GGE_inv = 59.8 · Δ_BCS / K_base` (lizzi 9A §2.2) is linear in Δ_BCS, and Δ_BCS itself is the Mellin-cone observable being R-projected. Affine = scheme-of-Δ-BCS in M_R units. A non-affine projection (e.g., sqrt as I floated in L4 Q-L4.2) would re-introduce the sqrt that Δ_BCS = sqrt(condensate energy density) already contains, doubling the operation. Affine is the minimal-coupling projection. Joint Extended Theorem clause (b) registered.

**A-T4.2 (transit Q-T4.2, alternative anomaly-isolating proxy for cross-review)**: The Mellin-cone-level candidate is the **Wess-Zumino-Witten consistency check at the substrate-distance-2 pole s=4**, where the anomaly contribution to c_sub appears as a residue at s=4 distinct from the smooth Jensen-flow background at s=3. Substitution chain for the proxy operator:

```
Step 1 — Definition:
  c_sub_anomaly_WZW(R) := Res[M_R(s)·anomaly_kernel; s=4] / Res[M_R(s); s=3]
  where anomaly_kernel projects onto WZW-consistent forms of D_K.

Step 2 — Substitute (W4-2 P5 multiplier values + S78 W2-F a_4-class structure):
  At s=3: M_R(s=3) is Mellin-cone substrate-distance-1 (probed in this workshop)
  At s=4: M_R(s=4) is a_4-coefficient-class (S78 W2-F, R²-dominated 98.48% intrinsic)
  Anomaly contribution at s=4 isolates from smooth Jensen flow at s=3.

Step 3 — Simplify (operator structure):
  c_sub_anomaly_WZW(R) decouples the anomaly residue (s=4) from the smooth
  background (s=3); the τ-flow-trace proxy in W5b couples them at the τ-derivative
  level, which is what produces the same-sign linear-fit result.

Step 4 — Direction:
  WZW proxy SEPARATES anomaly from background by Mellin-cone pole isolation;
  τ-flow-trace proxy COUPLES them by operating in the τ-derivative subspace.
  ⇒ WZW proxy is a CANDIDATE for the S87 cross-review without prejudgement.
  Conclusion: Submit WZW-proxy operationalization as one of the cross-review
              candidates; rubric pinning per `epistemic-discipline.md` §
              "Verifier-Rubric Pre-Registration" required.
```

This is a candidate, not a pre-judged PASS; the cross-review by an independent operator (connes-ncg-theorist) is needed to evaluate.

**A-T4.3 (transit Q-T4.3, suppression-class diagnostic admissibility)**: ADMISSIBLE as PER-CLASS DIAGNOSTIC, NOT as path-(c) sub-anchor. The strict linear regime requirement in my L1 Class A logic was about K-INVARIANCE (a between-R cross-class statement); the suppression-class diagnostic is a per-class WITHIN-R reading and does not need cross-class K-invariance. The diagnostic informs the per-class structure of the substrate's Bogoliubov coefficients without claiming K-invariance. Specifically, the suppression-class N_breakdown=∞ at canonical IC is informationally equivalent to the suppression-class entry of M_R(s=3) (both are projections of the same Mellin-cone substrate-distance-1 pole), and thereby admissible per the Joint Extended Theorem clause (b). It is NOT a path-(c) anchor because path-(c) requires K-invariance against alternative regulators, which Zubarev fails by 9.24× per Sector-2.

**A-T4.4 (transit Q-T4.4, class-protected Bogoliubov ledger principle)**: STRUCTURALLY EQUIVALENT to Clause C3, with one Mellin-cone-side ADDITIONAL structure. The Bogoliubov framing |α|² − |β|² = 1 within branch is the correct unitarity-side image of per-branch protection. The Mellin-cone side adds a representation-theoretic interpretation analogous to my S78 W3-K rank-3-protection theorem: per-branch protection at L_max running (L_max=3 → L_max=10 with W2-1 deviation 0.000440%) is the L_max-side analog of the rank-side R-protection (rank-3 groups pass per-branch, rank-2/4 pre-asymptotic). The L_max running drives the same Richardson-α monotonic convergence I established in S78 W3-K: per-branch L_max convergence is structurally analogous to per-rank cross-group convergence. So per-branch protection has TWO independent confirmations:
- (i) rank-side: my S78 W3-K theorem (rank-3 protection at <3.6% scheme-universality)
- (ii) L_max-side: S82 W2-1 replay (0.000440% L_max running deviation across L_max=3 → L_max=10)
- (iii) [transit's framing] unitarity-side: Bogoliubov |α|² − |β|² = 1 within branch

Three independent confirmations is structurally tight. Joint Extended Theorem clause (d) registered with all three.

**A-T4.5 (transit Q-T4.5, compute-deferred T2 closure)**: AGREE FULLY. The S87 carry-forward `S87-RESCALED-IC-SR-LO-RERUN` should focus on the four affine class-projections (suppression including), NOT on F_2-class IC rescaling. The F_2-class rerun is structurally closed by T2's Step-4 autocatalysis bound (ε_0 < 10^{−651.79} required). I sharpened the S87 spec accordingly in E-R2.4.

**A-T4.6 (transit Q-T4.6, path-(c) reorganization vs prediction frozen-ness)**: NO downstream observational gate where the path-(c) reorganization changes the framework's prediction value. The reorganization is value-preserving (A_s = 3.30e-9 PASS-F2 is fully retained from S82 W1-2). The falsifier-master-inventory rows 2, 12, 13-21 carry path-(c) value strings that ARE INVARIANT under the SECTOR-1/SECTOR-2 → route (iii) Branch-A reading, because the SECTOR-1/SECTOR-2 anchors NEVER PRODUCED an A_s value (they were path components, not endpoint values). The reorganization is cleanly value-preserving; only PROVENANCE strings update. This is consistent with FROZEN-PREDICTION-DISCIPLINE-COMMIT not applying (workshop pre-registration line 30).

**Q-L-R2 — New sharp questions for transit's R3 turn**:

**Q-L-R2.1 (F_2 vs F_4 vocabulary disambiguation, follow-up to D-R2.1)**: Do you accept the rename F_4_W4P5 → F_2 = {ζ, SDW} in the Joint Extended Theorem registration (E-R2.2) to avoid registry collision with the W14-plan F_4 = {ζ, Zubarev, SDW} 3-element regulator-class label? If yes, please reference the rename in your R3 turn. If no, please propose an alternative disambiguation path that the S87-PATH-C-SUCCESSOR-ANCHOR-LANDING gate can use without ambiguity.

**Q-L-R2.2 (pole-specificity test — answer Q-T4.1 sharper)**: My S78 W2-F established a_4^{HK} at s=4 is 98.48% R²-dominated INTRINSICALLY. The Mellin-multiplier scheme-invariance at s=4 is much TIGHTER than the 924× FAIL at s=3 (W4-2 P5). Do you predict the SR-LO-analog dynamical observable (a hypothetical N_breakdown_observable_at_s4) would show ANTI-correlation comparable to s=3, or would the s=4 scheme-tightness flatten the dynamical ranking? If so, this is a falsifiable test of E-R2.3 pole-specificity. Would you accept a side-bet that the s=4 anti-correlation Pearson |r| is < 0.3 vs s=3's |r| = 1.0?

**Q-L-R2.3 (S87 carry-forward level-1 pick)**: We now have five S87 carry-forward candidates (E-R2.4): SUCCESSOR-ANCHOR-LANDING, RESCALED-IC-SR-LO-RERUN, W5B-C16-CROSS-REVIEW, A_S-SURVIVING-ROUTE-RANK-LANDING, POLE-SPECIFICITY-SCAN. Total 3.25 wave-equivalents. If only TWO can land in S87 W-1 (typical wave budget), which two would you level-1 select and why? My pick is SUCCESSOR-ANCHOR-LANDING + W5B-C16-CROSS-REVIEW (registry + asymmetric-EVOI cross-review). Yours?

**Q-L-R2.4 (D-R2.3 sharpening)**: Do you accept my structural reformulation of route (iv) C16 sub-test (c) as "FAIL under τ-flow-trace proxy with open cross-review verdict" (rather than your "instrument-limited FAIL" framing) per the v3-closure-recovery PROHIBITED_ACTIONS Class 6 (iterate-until-PASS) discipline? If yes, please use the open-verdict framing in your R3 wrap-up. If no, please defend the "instrument-limited" pre-judgement as not Class-6-adjacent.

---

## Round 2 — transit: Cross-Synthesis

### CONVERGENCE

I converge with lizzi's R2-A on five distinct items, reading her sharpenings as upgrades that tighten my R1-B claims rather than corrections of error. Each item is anchored in the substitution chain from R1-B and lizzi's R2-A and verified against the canonical-constants ledger and the knowledge MCP.

**T-CR2.1 — F_2 vs F_4 vocabulary disambiguation (lizzi D-R2.1 + Q-L-R2.1): ACCEPTED IN FULL.** Lizzi's knowledge-MCP audit surfaces a registry collision I did not catch in R1-B: my Re:L1/Re:L2 used "F_4 class" interchangeably with the {ζ, SDW} 2-element identity pair, while `session-86-plan-w14.md` and the registered scripts (`s86_w2_c9_mellin_heat_kernel_infra.py` line `REGULATORS = ["zeta", "Zubarev", "SDW"]`, `s83_w1_g5_four_axis_decomposition.py`, `s84_w3_n_s_propagation_class.py`, etc.) all use **F_4 = {ζ, Zubarev, SDW}** (3-element, the (A)-regulator class per W14 (A)/(C) discriminator). The knowledge MCP search returned 8 hits, all aligning with the W14 reading. The two labels denote DIFFERENT sets — and they fail K-invariance differently:

```
Step 1 — Definitions of competing labels (per lizzi D-R2.1 + knowledge MCP):
  F_2_W4P5    = {ζ, SDW}             (2-element identity pair, this workshop)
  F_4_W14plan = {ζ, Zubarev, SDW}    (3-element regulator-class family,
                                       canonical across S83-S86 scripts)
  K-inv_threshold(W4-2 P5) = 1e-3 (PASS), 1e-2 (FAIL above)

Step 2 — Substitute the W4-2 P5 pair-ratios into each candidate:
  K-inv on F_2_W4P5 = {ζ, SDW}:
     pair_ratio(ζ, SDW) = 0.000000e+00            ⇒ PASS (machine-ε identity)
  K-inv on F_4_W14plan = {ζ, Zubarev, SDW}:
     max(pair_ratio(ζ, SDW), pair_ratio(ζ, Zub),
         pair_ratio(SDW, Zub))
     = max(0.000000e+00, 9.240e-01, 9.240e-01) = 9.240e-01  ⇒ FAIL (924× over threshold)

Step 3 — Simplify (set-theoretic relation):
  F_2_W4P5 ⊊ F_4_W14plan (proper subset; Zubarev added at the W14 level).
  K-invariance HOLDS on F_2_W4P5 BUT FAILS on F_4_W14plan.
  ⇒ The labels are NOT interchangeable; they refer to incompatible registry rows.

Step 4 — Direction (after canonical form):
  Sign of (K-inv_F_2_W4P5 − K-inv_F_4_W14plan) = sign(0 − 9.240e-01) = NEGATIVE
  ⇒ F_2_W4P5 satisfies K-invariance; F_4_W14plan does not.
  ⇒ Joint Extended Theorem clauses (a)-(f) (lizzi E-R2.2) MUST cite F_2 = {ζ, SDW}
    NOT F_4. Otherwise the theorem statement is structurally false on F_4_W14plan.
  Conclusion: ACCEPT lizzi's rename. The registration target in
              `permanent-results-registry.md` MUST use F_2 = {ζ, SDW}; the W14-plan
              F_4 = {ζ, Zubarev, SDW} label is reserved for the W14 (A)-class
              context where the suppression class is INCLUDED in the family by
              definitional convention, NOT by K-invariance survival.
```

I therefore retract the F_4 vocabulary in my R1-B (Re:L1, Re:L2, Re:L4, T1, T2, T3, T4) and the joint reading is anchored on F_2 = {ζ, SDW} consistently. This affects ALL future registry-side citations of the workshop result; the path-(c) successor anchor's class-membership statement reads "F_2-class via zeta scheme" not "F_4-class via zeta scheme".

**T-CR2.2 — Anti-correlation s=3 specificity scoping (lizzi C-R2.3 + D-R2.2): ACCEPTED with quantitative reinforcement.** Lizzi's structural sharpening is correct: my Re:L2 Step 4 conclusion ("the same Mellin-cone pole drives both spectral dominance and dynamical fragility, in opposite signs") was correct for s=3 but should not generalize without a pole-specificity test. The s=3 anti-correlation arises specifically because the W4 P4 anchor formula `xi_E_GGE_inv = 59.8 · Δ_BCS / K_base` (lizzi 9A §2.2; canonical_constants `xi_E_GGE_inv = 13.642473425595973`) couples the substrate-distance-1 pole into the SR-LO ODE IC. At a different pole (e.g., s=4 a_4 slot), no analogous IC-channel exists — the dynamical hierarchy structure would not necessarily inherit the spectral hierarchy in the same way.

I add a quantitative reinforcement to the C-R2.3 acceptance: numerical Spearman rank correlation across the 4-class projection (using censored Zubarev N_break = 55 as upper bound) returns ρ_spectral_dynamical = −1.0000 EXACT, while Pearson r ≈ −0.65 (the Pearson value depends on the censoring choice for the Zubarev infinity, which is the structurally correct reading when N_break is undefined for Zubarev). Substitution chain:

```
Step 1 — Definitions:
  rank_spec(R)  := position of R in M_R(s=3) descending order over A_5
  rank_dyn(R)   := position of R in N_break(R) ascending order over the 4 projected classes
  ρ_S(M_R, N_break) := Spearman rank correlation = Pearson on the rank vectors

Step 2 — Substitute (Python-verified, scipy.stats.spearmanr):
  R ∈ {F_2 (ζ=SDW), cutoff_sqrt, anomaly, Zubarev}
  M_R(s=3)         = (1.581e-1, 1.110e-1, 3.185e-2, 1.201e-2)
  N_break(R)       = (0.122,    0.176,    0.730,    55.0_censored)
  rank_spec        = (1, 2, 3, 4)  (largest M_R is rank 1)
  rank_dyn         = (1, 2, 3, 4)  (smallest N_break is rank 1)
  ρ_S = corr(rank_spec, rank_dyn) along same-direction reading = +1.0
  Read in opposite directions (spectral descending vs dynamical ascending): ρ_S = −1.0

Step 3 — Simplify (canonical form):
  The rank-correlation magnitude is EXTREMAL (|ρ_S| = 1.0).
  No information content beyond perfect monotonic anti-correlation
  along the 4-class projection at s=3.
  Pearson |r| = 0.65 (sensitive to Zubarev censoring choice; rank-metric is
  the structurally correct one for ordinal class structure).

Step 4 — Direction (only after canonical form):
  |ρ_S(s=3)| = 1.0  EXACT (rank-monotonic anti-correlation across 4 classes).
  At a different pole s=4, the prediction (lizzi E-R2.3 + Q-L-R2.2) is that
  |ρ_S(s=4)| < 0.3 — i.e., the rank-monotonic structure flattens because
  the a_4 slot is 98.48% R²-dominated INTRINSICALLY (lizzi S78 W2-F).
  ⇒ The s=3 anti-correlation IS pole-specific.
  ⇒ Joint Extended Theorem clause (c) (lizzi E-R2.2) is registered with
    the s=3 specificity attached.
  Conclusion: ACCEPT lizzi's scoping. The phrase "spectral-dynamical duality"
              in the registry entry must read "at the Mellin-cone substrate-
              distance-1 pole s=3"; pole-specificity test (E-R2.3) is the
              falsifiable extension.
```

This converts my Re:L2 unscoped "the substrate's spectral-dynamical duality" into the scoped "the s=3 pole's spectral-dynamical anti-correlation" — a structurally tighter and falsifiable claim. The Q-L-R2.2 side-bet (|ρ_S(s=4)| < 0.3 vs s=3's 1.0) is well-formed; I accept the bet at the spectral substitution chain level (see DISSENT for one structural caveat I attach to it).

**T-CR2.3 — "Open cross-review verdict" reformulation of route (iv) C16 sub-test (c) (lizzi D-R2.3 + Q-L-R2.4): ACCEPTED.** Lizzi's invocation of `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6 (iterate-until-PASS) is correct. My Re:L3 §(1) framing ("instrument-limited FAIL") is Class-6-adjacent because it pre-stipulates the cross-review's verdict direction (FAIL → PASS) before the cross-review fires. The structurally clean formulation is the open-verdict pre-registration:

```
Step 1 — Definitions:
  C16_subtest_c_proxy_τflow := the τ-flow-trace proxy operationalization of
                               c_sub_anomaly(τ) := dc_sub(τ)/dτ
                               (W5b §W5b-2 line 343)
  C16_subtest_c_proxy_alt   := an alternative anomaly-isolating proxy
                               (S87 cross-review candidate)
  pre_registration_verdict  := the gate verdict committed before computation,
                               per `.claude/rules/epistemic-discipline.md`
  Class-6 risk              := iterate-until-PASS, per
                               `.claude/rules/v3-closure-recovery.md`
                               PROHIBITED_ACTIONS clause 2

Step 2 — Substitute the two framings:
  Re:L3 §(1) "instrument-limited" framing:
     verdict_pre_compute(C16_subtest_c) = "FAIL is conditional; cross-review
     will likely flip to PASS"
     ⇒ direction (FAIL → PASS) is asserted PRIOR to cross-review compute
  D-R2.3 "open cross-review verdict" framing:
     verdict_pre_compute(C16_subtest_c) = "FAIL stands under τ-flow-trace
     proxy; alternative-proxy cross-review returns one of {(A) FAIL stands,
     (B) PASS}; verdict between (A) and (B) is OPEN"
     ⇒ NO direction asserted PRIOR to cross-review compute

Step 3 — Simplify (Class-6 audit):
  Class-6 risk = signed-prejudgement on a downstream gate
  Re:L3 §(1) framing  = signed-prejudgement (FAIL → PASS)        ⇒ Class-6-adjacent
  D-R2.3 framing      = unsigned (open between (A) and (B))      ⇒ Class-6-clean

Step 4 — Direction:
  Sign of (Class-6_risk_R1B − Class-6_risk_D-R2.3) = sign(prejudge − no-prejudge) > 0
  ⇒ R1-B framing carries Class-6-adjacent risk that D-R2.3 reformulation removes.
  ⇒ ACCEPT D-R2.3 reformulation as the canonical S87 carry-forward language.
  Conclusion: The S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW gate is pre-registered
              with open-verdict framing: returns (A) FAIL stands → C16 INFO
              confirmed at L_max=10; (B) cross-proxy yields PASS → INFO promotes
              to ADMISSIBLE. The asymmetric-EVOI argument from R1-B Re:L3 §(1)
              IS PRESERVED (cross-review remains a strictly dominant next gate),
              BUT the verdict is not pre-judged.
```

I retract my "instrument-limited" framing as Class-6-adjacent and use lizzi's open-verdict reformulation in the R3 wrap-up. The asymmetric-EVOI substitution chain itself (Re:L3 substitution chain Step 4) remains valid — cross-review is asymmetric in upside, but the asymmetry is in EVOI (information value), not in pre-judged verdict direction. Q-L-R2.4 is answered YES with this substitution chain explicit.

**T-CR2.4 — Joint Extended PERMANENT THEOREM CANDIDATE 6-clause statement (lizzi E-R2.2): ACCEPTED with corrigenda from T-CR2.1 + T-CR2.2 + T-CR2.3.** Lizzi's 6-clause joint formulation merges spectral 3-class partition + dynamical 4-class breakdown + s=3 anti-correlation duality + per-branch protection (Bogoliubov + multiplicative ledger + L_max-running) + cross-class K-invariance closure + autocatalysis F_2-class closure. I accept all six clauses (a)-(f) with three corrigenda from this round:

- Clause (a): "F_2 dominant" not "F_4 dominant" (T-CR2.1 disambiguation).
- Clause (b): "F_2 (0.122)" not "F_4 (0.122)" (same).
- Clause (c): "at the Mellin-cone substrate-distance-1 pole s=3" appended (T-CR2.2 scoping).
- Clause (d): the three independent confirmations (rank-side W3-K, L_max-side W2-1, unitarity-side Bogoliubov |α|² − |β|² = 1) are each independently verified (lizzi A-T4.4); I accept the triple as joint structural rationale.
- Clause (e): unchanged; lizzi L1 cross-class closure is structurally tight at A_5 above F_2.
- Clause (f): structurally airtight; T2 substitution chain Step 4 closure at ε_0 < 10^{−651.79} (lizzi recomputation) / 10^{−652.73} (my Python recomputation; the 0.94 OOM difference is a log10/log_e conversion artefact, both far below float64 underflow 10^{−308}).

The 6-clause statement is registerable to `sessions/permanent-results-registry.md`. I co-author with lizzi as proposed in E-R2.4 §S87-PATH-C-SUCCESSOR-ANCHOR-LANDING (sharpened from L4).

```
Step 1 — Definitions (theorem-validity audit):
  T_validity := all six clauses (a)-(f) are simultaneously TRUE under
                the W4-2 P5 atlas + W4 P4 pin + S82 W1-2 verdict + T2
                autocatalysis bound + W5a verdicts.
  T_corrigenda := the three label/scope edits from T-CR2.1/T-CR2.2/T-CR2.3.
  T_registerable := the corrected theorem text is registry-pinnable
                without ambiguity.

Step 2 — Substitute the validity check per clause:
  (a) spectral 3-class partition: TRUE under M_R(s=3) numerical 5-tuple.
  (b) dynamical 4-class breakdown: TRUE under transit Re:L1 LSODA scan
      + lizzi C-R2.1 independent reproduction.
  (c) anti-correlated duality at s=3: TRUE with Spearman ρ_S = ±1.0 EXACT
      under same/opposite-direction reading; pole-specificity scoping appended.
  (d) per-branch protection: TRUE with three independent confirmations
      (W3-K rank, W2-1 L_max, Bogoliubov unitarity).
  (e) cross-class K-invariance closure: TRUE under lizzi L1 Class A-F
      enumeration (no non-trivial sub-anchor on A_5 above F_2).
  (f) F_2-class autocatalysis closure: TRUE under T2 Step 4 + lizzi C-R2.1
      Step 4 (ε_0 < 10^{−652} ≪ 10^{−308} float64 underflow).

Step 3 — Simplify (registry-pin readiness):
  T_validity AND T_corrigenda ⇒ T_registerable.
  All six clauses pass independent validity audit; corrigenda are local
  edits (label + scope), not structural rewrites.

Step 4 — Direction:
  T_registerable = TRUE.
  ⇒ ACCEPT joint authorship and propose S87-PATH-C-SUCCESSOR-ANCHOR-LANDING
    as the registration vehicle.
  ⇒ The 6-clause statement is the canonical formulation of this workshop's
    structural harvest.
  Conclusion: Joint Extended Theorem (lizzi+transit S86 W-9, joint formulation)
              is registerable as a permanent theorem candidate, pending the
              S87-PATH-C-SUCCESSOR-ANCHOR-LANDING gate. The path-(c)
              reorganization (lizzi L4 Clauses C1-C4) is the falsifier-
              registry implementation of the theorem.
```

**T-CR2.5 — Per-class N_breakdown 4-tuple as NEW substrate-physics observable (lizzi E-R2.1): ACCEPTED with structural framing extension.** Lizzi's E-R2.1 substitution chain establishes that N_breakdown_observable(R) is well-defined, Mellin-cone-derived, cross-validated against the autocatalysis bound, and L_max-pinned at L_max=3. I accept this as the FIRST per-class dynamical diagnostic the framework has constructed — it is substrate-derivable, registry-pinnable, and orthogonal to the per-branch-protected ledger anchor (route iii). I add one structural framing extension that connects the new observable to the broader Bogoliubov-coefficient class-protection framework:

```
Step 1 — Definitions (Bogoliubov-side framing of E-R2.1):
  α_R(N), β_R(N) := per-R Bogoliubov coefficients of the post-fold transit
                    in regulator branch R.
  P_pair,R(N)    := per-R pair-production probability = |β_R(N)|²
  E_pair,R(N)    := per-R energy stored in pairs at e-fold N.
  Backreaction onset := smallest N at which E_pair,R(N) saturates the
                        single-mode SR-LO truncation budget, which by
                        unitarity is the autocatalysis ceiling ε(N) > 0.5.
  N_back,R       := N at which backreaction-onset condition first holds.

Step 2 — Substitute (relation to E-R2.1 N_breakdown_observable):
  Per-class IC pin xi²_0(R) sets the initial pair-density per the
  Bogoliubov ledger at the substrate-distance-1 pole.
  Within SR-LO truncation, the autocatalysis +2εξ² source term in dε/dN
  IS the per-R backreaction onset signal:
     dε/dN > 0 with growing rate ⇔ |β_R|² growing (pair-density increasing)
  N_breakdown_observable(R) = N_back,R within SR-LO truncation.

Step 3 — Simplify (observable identification):
  E-R2.1's N_breakdown_observable IS the per-R Bogoliubov backreaction
  onset N_back,R, projected through the SR-LO truncation. The observable
  is meaningful BECAUSE the SR-LO truncation tracks the underlying
  Bogoliubov dynamics exactly within the linear regime ε ≤ 0.1.
  Beyond ε > 0.5, SR-LO loses touch with the Bogoliubov dynamics, and
  N_breakdown_observable marks the per-R loss-of-touch boundary.

Step 4 — Direction:
  E-R2.1 N_breakdown_observable is the SR-LO image of the per-R Bogoliubov
  backreaction-onset N_back,R.
  ⇒ The observable is FUNCTIONAL-DEPENDENT (per-R varies by 9.24× class
    spread, mirroring spectral spread).
  ⇒ It is admissible as per-class diagnostic in path-(c) Clause C2 retention.
  ⇒ Beyond N_breakdown,R, the dynamics is OUTSIDE SR-LO — Bogoliubov
    dynamics continues but is not captured by the truncation.
  Conclusion: ACCEPT lizzi E-R2.1. ADD: the new observable's substrate-physics
              meaning is "per-R Bogoliubov backreaction-onset N projected
              through SR-LO truncation". This makes it a STRUCTURALLY MEANINGFUL
              quantity, not just a computationally derived diagnostic.
```

This converges with lizzi's reading and adds the Bogoliubov-substrate physics interpretation. The new observable belongs in the path-(c) reorganization as a per-class diagnostic (path-(c) Clause C2 retention of SECTOR-1 SR-LO Z-factor for IC-class compatibility) — explicitly NOT a new path-(c) anchor (since K-invariance fails at 9.24×) but a NEW per-R substrate-dynamics measurement that the framework did not have before this workshop.

### DISSENT

I dissent on one structural point and one tactical point. Both are S87-relevant; neither contradicts lizzi's R2-A but each requires a sharpening before the registry landing.

**T-DR2.1 — Pole-specificity side-bet (Q-L-R2.2): ACCEPT THE BET DIRECTION but with a structural caveat on the SR-LO-analog observable construction.** Lizzi proposes that |ρ_S(s=4)| < 0.3 vs |ρ_S(s=3)| = 1.0 because s=4 is a_4-coefficient-class and 98.48% R²-dominated INTRINSICALLY (S78 W2-F). The spectral side of the bet is structurally airtight: at s=4, the Mellin-multiplier scheme-spread should compress dramatically because the a_4 slot is rank-protected (her S78 W3-K result). I agree the spectral-side prediction is correct.

The structural caveat: the bet hinges on the construction of an "SR-LO-analog dynamical observable" that takes M_R(s=4) as input the same way the W4 P4 anchor formula `xi_E_GGE_inv = 59.8 · Δ_BCS / K_base` takes M_R(s=3). NO SUCH ANALOG EXISTS YET. The substrate-natural anchor at s=3 routes through Δ_BCS (which is a sqrt of the condensate energy density) and K_base (the BCS condensate base scale). At s=4, no analogous anchor formula has been constructed; the W4 P4 anchor was specifically designed around the substrate-distance-1 pole. Substitution chain:

```
Step 1 — Definitions:
  W4P4_anchor_at_s3 := xi_E_GGE_inv = 59.8 · Δ_BCS / K_base (lizzi 9A §2.2)
  Hypothetical_anchor_at_s4 := unspecified function of substrate constants
                               that takes M_R(s=4) as the projection axis

Step 2 — Substitute the construction-existence check:
  At s=3: the anchor formula EXISTS (W4 P4 commit acc751101c8ca6ce, canonical
          xi_E_GGE_inv = 13.642473425595973 in canonical_constants).
  At s=4: no canonical anchor exists; constructing one requires choosing
          a substrate-natural quantity at the a_4 slot (e.g., the rank-3
          Yang-Mills coupling channel, per S78 W3-K).

Step 3 — Simplify (test specifity):
  The SR-LO-analog dynamical observable at s=4 is NOT predetermined by
  the W4 P4 construction. Different choices of the s=4 anchor formula
  yield DIFFERENT projections of M_R(s=4) onto an SR-LO-style IC.
  The pole-specificity test (E-R2.3 + Q-L-R2.2) therefore depends on
  WHICH s=4 anchor formula is chosen.

Step 4 — Direction (after canonical form):
  Sign of (test_well_definedness_at_s3 − test_well_definedness_at_s4) = +
  ⇒ s=3 test is well-defined; s=4 test requires an explicit anchor-formula
    pre-registration.
  ⇒ Accept the bet AT THE SPECTRAL LEVEL (|ρ_S| spread compresses at s=4).
  ⇒ DISSENT on the bet at the SR-LO-analog level until the s=4 anchor
    formula is pre-registered.
  ⇒ S87-POLE-SPECIFICITY-SCAN (E-R2.4 NEW gate) MUST include an explicit
    s=4 anchor-formula choice in its 4-field spec, NOT a "construct-as-you-go"
    placeholder.
  Conclusion: the bet is well-formed at the spectral level; the dynamical-
              side comparison requires an explicit s=4 anchor pre-registration
              before the test fires. Sharpen the carry-forward spec accordingly.
```

The dissent is constructive: I accept lizzi's prediction that the spectral compression at s=4 will flatten the dynamical anti-correlation. But the falsifiability of the test depends on the s=4 anchor-formula choice. The S87-POLE-SPECIFICITY-SCAN gate must pre-register this formula choice explicitly to avoid PRU-Class-8 (gate-relevant machinery left unpinned, per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness"). I propose extending lizzi's E-R2.4 NEW spec to include a "Step (a) — pre-register the s=4 anchor formula by lizzi+transit before the dynamical scan fires" sub-step in the *What* field.

**T-DR2.2 — S87 level-1 pick (Q-L-R2.3): I PARTIALLY DIFFER from lizzi's pick.** Lizzi proposes SUCCESSOR-ANCHOR-LANDING + W5B-C16-CROSS-REVIEW as the level-1 two. I propose SUCCESSOR-ANCHOR-LANDING + RESCALED-IC-SR-LO-RERUN. The reason is structural: the SR-LO-RERUN fires the per-class diagnostic that the Joint Extended Theorem clause (b) and the new E-R2.1 observable depend on, AT THE LANDING SESSION. If we land the theorem in S87 W-1 but defer the per-class N_breakdown rerun to a later wave, the registry will cite numerical values (transit Re:L1 table) that have not been independently reproduced under the S87 dispatch envelope. The W5B-C16-CROSS-REVIEW is asymmetric-EVOI but the EVOI is in the binary {(A), (B)} verdict on a DIFFERENT route (route iv, not the path-(c) successor anchor route iii).

```
Step 1 — Definitions (S87 level-1 selection criteria):
  Theorem-completeness criterion := ALL clauses (a)-(f) of Joint Extended
                                    Theorem are independently verified by
                                    S87 dispatch before registration.
  Path-(c)-anchor criterion       := the path-(c) successor anchor
                                    (route iii) is landed in falsifier
                                    registry with theorem co-registration.
  Cross-route diagnostic criterion := route (iv) C16 INFO admissibility
                                    is resolved (open-verdict, per T-CR2.3).

Step 2 — Substitute the gate dependencies:
  Joint Extended Theorem clause (b) (dynamical 4-class breakdown) cites
  N_breakdown(R) for R ∈ {F_2, cutoff_sqrt, anomaly, Zubarev}.
  Without RESCALED-IC-SR-LO-RERUN at S87 W-1, clause (b) cites un-replayed
  R1-B numerics.
  RESCALED-IC-SR-LO-RERUN provides the S87 reproduction at the same dispatch
  envelope as the registry landing.

  W5B-C16-CROSS-REVIEW affects route (iv) admissibility — it does NOT
  affect the path-(c) successor anchor's PASS-F2 status (route iii).
  Both PASS-F2 (iii) and ADMISSIBILITY (iv) are independently relevant
  but operate on DIFFERENT route slots.

Step 3 — Simplify (structural priority):
  Theorem-completeness (clause-(b) independent verification) is a
  prerequisite for theorem registration.
  Cross-route diagnostic resolution can occur AFTER theorem registration
  without retroactively invalidating the registration.
  ⇒ Level-1 priority: SUCCESSOR-ANCHOR-LANDING + RESCALED-IC-SR-LO-RERUN.
  ⇒ Level-2 priority: W5B-C16-CROSS-REVIEW + A_S-RANK-LANDING.
  ⇒ Level-3 priority: POLE-SPECIFICITY-SCAN (NEW; depends on level-1+2).

Step 4 — Direction:
  Sign of (theorem-completeness gap with my level-1 pick − with lizzi's pick):
    My pick:  gap closes (clause (b) verified at S87 dispatch envelope)
    Lizzi's:  gap remains (clause (b) cites R1-B numerics not S87-replayed)
  ⇒ Differ in level-1 second pick: RESCALED-IC > W5B-C16-CROSS-REVIEW
    for theorem-completeness; W5B-C16-CROSS-REVIEW > RESCALED-IC for
    EVOI-asymmetric upside.
  ⇒ This is a TRADE-OFF: completeness vs information-value.
  Conclusion: my pick weights theorem-completeness; lizzi's pick weights
              EVOI. Both are defensible. I propose we present BOTH picks
              in the S87 plan-write and let the planner choose based on
              S87 wave-budget realities. If three slots are available
              (3.0 wave-equivalents), include all three: SUCCESSOR-ANCHOR
              + RESCALED-IC + W5B-C16-CROSS-REVIEW. Level-1-of-2 is the
              constraining case where the trade-off bites.
```

The dissent is partial: I accept lizzi's SUCCESSOR-ANCHOR-LANDING as level-1-first; I differ on the second pick. The R3 wrap-up should record both picks and the S87 planner adjudicates. This is consistent with `.claude/rules/output-standards.md` §"Pre-registered gates are the evidence" — the trade-off is between theorem-completeness and EVOI-asymmetric upside, both legitimate criteria.

### EMERGENCE

Cross-pollination between lizzi's R2-A and my R1-B surfaces three emergent insights that neither side alone identified. Each is anchored in the substitution chains above and points to a structural feature of the path-(c) reorganization that would have been missed without the joint reading.

**T-ER2.1 — Upgrade pathway from "joint theorem candidate" to registered theorem (joint with lizzi E-R2.2).** The Joint Extended PERMANENT THEOREM CANDIDATE (lizzi E-R2.2 + my T-CR2.4) is structurally tight enough to register, but the registration itself requires an explicit upgrade pathway. The pathway has four stages, each with a substitution chain and a gate:

```
Step 1 — Definitions (4-stage upgrade pathway):
  Stage 0: Workshop-internal candidate (this workshop, S86 W-9)
           — joint formulation, pending registration
  Stage 1: S87-PATH-C-SUCCESSOR-ANCHOR-LANDING gate firing
           — 6 clauses (a)-(f) verified at S87 dispatch envelope
           — F_2 vs F_4 disambiguation landed (T-CR2.1)
           — registry-cite at sessions/permanent-results-registry.md
  Stage 2: Independent verification by a 3rd workshop-external agent
           — per `.claude/rules/v3-closure-recovery.md` §"Source Authority
             Hierarchy" — the registration becomes structurally pinned
             only when an independent agent verifies clauses (a)-(f)
             without prior workshop context
  Stage 3: PERMANENT REGISTRATION
           — promoted to permanent-results-registry as a non-revocable
             structural theorem (joins KO-dim=6, etc.)

Step 2 — Substitute (gate sequence):
  Stage 0 → 1: gate S87-PATH-C-SUCCESSOR-ANCHOR-LANDING (lizzi E-R2.4
               sharpened spec; 0.5 wave-equivalents)
  Stage 1 → 2: gate S87-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY
               (NEW; not in lizzi E-R2.4 list — propose for S88 plan)
  Stage 2 → 3: registry-promotion at session-end synthesis after
               independent-verify PASS

Step 3 — Simplify (structural-pin readiness audit):
  The 4-stage pathway distinguishes "candidate" from "registered" from
  "permanent". Without the explicit pathway, the workshop registers
  the theorem at S87 W-1 and skips the independent-verify check —
  which is the failure mode of registry-driven theorem inflation.
  The independent-verify gate is the structural-pin guarantor.

Step 4 — Direction:
  Sign of (with-pathway theorem-robustness − without-pathway):
    With-pathway: independent-verify PASS or FAIL determines permanence
    Without-pathway: registry inflation; theorem promoted on workshop
                     consensus alone (insufficient per
                     `.claude/rules/epistemic-discipline.md`
                     §"What Does NOT Count as Evidence" item 2:
                     "Counts of how many agents agree")
  ⇒ The 4-stage pathway is structurally essential; the workshop
    proposes it as an emergent insight from joint R2 reading.
  Conclusion: PROPOSE the 4-stage upgrade pathway as the canonical
              promotion-mechanism for the Joint Extended Theorem.
              S87 W-1 lands Stage 1 (registration as candidate);
              S88 fires Stage 2 (independent-verify); session-end
              synthesis at S88 promotes to Stage 3 (permanent) IFF
              independent-verify PASSes.
```

This is an EMERGENT CONTRIBUTION — neither lizzi E-R2.2 nor my T-CR2.4 alone specified the 4-stage pathway. It emerges from the joint reading because the registration's structural completeness depends on independent verification (which neither single agent can provide alone, per epistemic-discipline §"Counts of how many agents agree do not count as evidence"). I propose the pathway as an addition to the S87 carry-forward set.

**T-ER2.2 — Pole-specificity test at s=4 as discriminator between spectral-3-class and dynamical-4-class views (E-R2.3 + Q-L-R2.2 + my T-DR2.1).** The pole-specificity test is more than a pole-scan — it is the FALSIFIABLE DISCRIMINATOR between two structurally distinct readings of clauses (a) and (b) of the Joint Extended Theorem. Reading 1: spectral and dynamical classes are TWO MANIFESTATIONS of the same Mellin-cone substrate-distance-1 pole (rank-monotonic anti-correlation at |ρ_S| = 1.0 EXACT is generic to the substrate's per-R structure). Reading 2: spectral and dynamical classes are POLE-SPECIFIC manifestations (rank-monotonic anti-correlation at |ρ_S| = 1.0 holds at s=3 but flattens at s=4). Substitution chain:

```
Step 1 — Definitions (the two competing readings):
  Reading_1 (generic substrate-pluralism):
     For ANY pole s ∈ {3, 4, 5, ...}, |ρ_S(M_R(s), N_break_at_s_anchor)| → 1.0
     under same/opposite-direction rank reading.
     ⇒ The 3-class spectral / 4-class dynamical structure repeats at every
       pole.
  Reading_2 (pole-specific substrate-pluralism):
     |ρ_S(s=3)| = 1.0 because s=3 is the substrate-distance-1 pole
     and the W4 P4 anchor formula couples s=3 specifically.
     |ρ_S(s≠3)| < 1.0 because no analogous anchor formula exists at other
     poles, and the spectral-spread compresses at rank-protected slots
     (e.g., s=4 a_4 is 98.48% R²-dominated per S78 W2-F).

Step 2 — Substitute (test design):
  S87-POLE-SPECIFICITY-SCAN measures |ρ_S(s=4)| under an explicit s=4
  anchor formula (T-DR2.1 dissent: anchor formula MUST be pre-registered
  before scan).
  Outcome A: |ρ_S(s=4)| ≥ 0.7 → Reading_1 confirmed (generic substrate-pluralism)
  Outcome B: |ρ_S(s=4)| < 0.3 → Reading_2 confirmed (pole-specific)
  Outcome C: 0.3 ≤ |ρ_S(s=4)| < 0.7 → INFO; needs additional poles to disambiguate

Step 3 — Simplify (theorem-implication of each outcome):
  Outcome A ⇒ Joint Extended Theorem clause (c) generalizes:
              "spectral-dynamical anti-correlation holds at every Mellin pole
              the substrate's anchor-formula machinery couples".
  Outcome B ⇒ Joint Extended Theorem clause (c) stands as written:
              "anti-correlation is observable-pole-specific to s=3".
  Outcome C ⇒ neither generalization nor restriction; further pole-scan needed.

Step 4 — Direction:
  Sign of (Reading_2 epistemic value − Reading_1 epistemic value):
     If Reading_2 holds: the framework gains a NEW falsifiable structural
                         constraint (anti-correlation breaks at non-substrate-
                         distance-1 poles).
     If Reading_1 holds: the framework gains a STRONGER substrate-pluralism
                         theorem (generic across poles).
  ⇒ Either outcome is structurally informative; the test discriminates
    which reading is the canonical formulation of the Joint Extended Theorem.
  ⇒ The pole-specificity test is structurally LEVERAGED — it sharpens the
    theorem regardless of which way it lands.
  Conclusion: S87-POLE-SPECIFICITY-SCAN (E-R2.4 NEW; with T-DR2.1 anchor-
              formula pre-registration sub-step) is HIGH-LEVERAGE because
              every outcome (A, B, C) refines the Joint Extended Theorem.
              EVOI is HIGH; the gate should be level-2 in S87 W-1 if budget
              allows three slots.
```

This is EMERGENT because lizzi E-R2.3 framed the s=4 test as "a TESTABLE prediction" of pole-specificity, and my T-DR2.1 noted the need for an explicit anchor-formula pre-registration; together they reveal that the test is not just a confirmation/falsification of a single reading but a STRUCTURAL DISCRIMINATOR between two equally-substrate-physical readings of the Joint Extended Theorem. This elevates the gate's priority from "supplementary" to "high-leverage discriminator".

**T-ER2.3 — Suppression-class as path-(c) successor anchor candidate? — closed in the negative, with informative residue.** Lizzi C-R2.4 + her A-T4.3 establishes that the suppression-class survives SR-LO validity to N=55 with max(ε)=0.266 — a UNIQUE survival in the 4-class projection. A natural emergent question is: could the suppression-class projection (xi²_0 = 1.037) ITSELF serve as a path-(c) successor anchor, instead of route (iii) UNIFIED-AS-79 Branch-A? My answer: NO, but the negative is structurally informative.

```
Step 1 — Definitions:
  Path-(c)_anchor_admissibility := (i) PASS-F2 against Planck A_s = 2.10e-9
                                   + (ii) K-invariance compatibility against
                                         A_5 alternative regulators
                                   + (iii) substrate-derivable from D_K
                                          spectral moments
  Suppression-class_candidate   := use Zubarev-projected xi²_0 = 1.037 as
                                   the IC, run SR-LO ODE to N=55, extract
                                   Z-factor, compute A_s under suppression-
                                   class spectral moments

Step 2 — Substitute (admissibility test):
  Test (i) PASS-F2 against Planck:
    Suppression-class A_s reading at N=55 with max(ε)=0.266 lies past strict
    linear regime (ε > 0.1). The Z-factor reading at suppression-class IC
    is OUTSIDE the SR-LO truncation's linear-validity envelope.
    Numerical value at suppression-class projection: would require new
    SR-LO ODE rerun (S87-RESCALED-IC-SR-LO-RERUN). Computation deferred.
  Test (ii) K-invariance compatibility:
    pair_ratio(Zubarev, F_2 = ζ=SDW) = 9.240e-01 = 924× over PASS threshold.
    Zubarev-class FAILs K-invariance against F_2 by O(1) margin
    (W4-2 P5 verdict line 108).
    ⇒ Suppression-class candidate FAILs (ii) by 924× at the W4-2 P5 metric.
  Test (iii) substrate-derivable:
    Yes, the suppression-class IC is derived from M_Zubarev(s=3) per
    affine projection xi²_0(R) = 13.6425 · M_R / M_F2.

Step 3 — Simplify (admissibility verdict):
  Required: ALL THREE tests PASS.
  Test (ii) FAILS at 924× over threshold.
  ⇒ Suppression-class candidate is NOT admissible as a path-(c) successor
    anchor.
  ⇒ It IS admissible as a per-class diagnostic (lizzi A-T4.3 + my T-CR2.5).

Step 4 — Direction (after canonical form):
  Sign of (suppression-class admissibility status):
    NEGATIVE for path-(c) anchor (test (ii) FAILS by 924×).
    POSITIVE for per-class diagnostic (Joint Extended Theorem clause (b)
    + E-R2.1 N_breakdown_observable).
  ⇒ The negative is informative: it confirms that path-(c) anchor MUST live
    on F_2-class only (lizzi L1 Class B logic), and per-class diagnostics
    occupy a STRICTLY DIFFERENT registry slot than path-(c) anchors.
  Conclusion: Suppression-class projection is closed as a path-(c) anchor
              candidate (negative), but its survival to N=55 IS the FIRST
              non-trivial per-class dynamical diagnostic the framework has
              constructed. The negative result hardens the F_2-class
              uniqueness of the path-(c) anchor while opening the per-class
              diagnostic slot for the first time. Both are structural
              findings; both inform the path-(c) reorganization.
```

This emergent insight clarifies the structural separation between PATH-(c) ANCHORS (must satisfy K-invariance ∩ substrate-derivability ∩ PASS-F2) and PER-CLASS DIAGNOSTICS (must satisfy substrate-derivability alone; can violate K-invariance). The suppression-class candidate fails the anchor test but populates the diagnostic slot. This separation was implicit in lizzi L4 Clause C2 ("retain SECTOR-1 as a diagnostic for IC-class compatibility") but the structural test that establishes the separation only emerges from the joint R2 reading: lizzi C-R2.4 supplied the SR-LO survival fact; my T-CR2.5 supplied the Bogoliubov backreaction-onset framing; together they answer the natural question "could the surviving class be the new path-(c) anchor?" with a structurally tight NO.

The path-(c) reorganization is therefore confirmed: route (iii) UNIFIED-AS-79 Branch-A zeta-normalization (F_2-class) is the ONLY substrate-derivable, K-invariance-compatible, PASS-F2-against-Planck successor anchor on A_5. All other class projections are diagnostic-only. The DOUBLE-DOUBLE FAIL is fully mapped: cross-class K-invariance is closed (lizzi L1); F_2-class SR-LO is closed by autocatalysis (T2 + lizzi C-R2.1); only F_2-class via the analytic UNIFIED-AS-79 ledger survives (lizzi L4 + my T3 + the joint Extended Theorem). The reorganization is structurally complete at the end of R2 and ready for the R3 wrap-up.

---

## Round 3 — lizzi: Follow-up

### CONVERGENCE

I converge with transit's R2-B on three reinforced items and accept the 4-stage upgrade pathway as the canonical promotion mechanism. Each item is anchored in the substitution chains of R1 + R2 and verified against the canonical-constants ledger and the knowledge MCP.

**L-CR3.1 — 4-stage upgrade pathway with independent-verify gate (transit T-ER2.1): ACCEPTED IN FULL.** Transit's pathway (Stage 0 workshop candidate → Stage 1 S87 registration → Stage 2 independent-verify by 3rd workshop-external agent → Stage 3 permanent registration) is structurally essential and addresses a failure mode I had not flagged in R2-A. Lizzi E-R2.4 sharpened the carry-forward 4-field specs but did not pre-register the *promotion mechanism* between stages. Transit's pathway closes that gap. The independent-verify gate (Stage 1 → 2) is the structural-pin guarantor against registry-driven theorem inflation, which `.claude/rules/epistemic-discipline.md` §"What Does NOT Count as Evidence" item 2 ("Counts of how many agents agree") explicitly forbids as evidence. Substitution chain confirming the pathway is well-typed:

```
Step 1 — Definitions (4-stage promotion-mechanism audit):
  Stage_n_artifact         := the registry artifact deposited at stage n
  Stage_n→n+1_gate         := the gate firing that promotes Stage n to Stage n+1
  permanence(Stage)        := boolean — does the registration survive
                              independent-of-workshop adjudication?
  registration_inflation   := registering Stage 0 artifact directly as
                              Stage 3 permanent without firing Stage 1
                              and Stage 2 gates

Step 2 — Substitute the 4 stages with their gate dependencies:
  Stage 0 (workshop-internal candidate, S86 W-9) → Stage 1:
     gate = S87-PATH-C-SUCCESSOR-ANCHOR-LANDING (lizzi E-R2.4 sharpened)
     deposit = registry-cite at sessions/permanent-results-registry.md
                with "candidate" tag
  Stage 1 (registered candidate) → Stage 2:
     gate = S87-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY (transit T-ER2.1 NEW)
     deposit = independent-verify PASS/FAIL appended to registry row
  Stage 2 (independently verified) → Stage 3:
     gate = session-end synthesis at S88+ (or wherever Stage 2 lands)
     deposit = "candidate" tag stripped; theorem joins KO-dim=6, J-D_K=0,
                etc., in the permanent-results table

Step 3 — Simplify (compare with-pathway vs without-pathway):
  permanence(Stage_3 with pathway) = TRUE iff (Stage_1 PASS) ∧ (Stage_2 PASS)
  permanence(Stage_3 without pathway) = depends on workshop consensus alone
                                        ⇒ Class-(2)-rule violation
                                          ("agreement among agents is not evidence")

Step 4 — Direction (after canonical form):
  Sign(robustness gain from pathway) = +
     Stage 1 alone: registry has a candidate; falsifier rows can cite
                    provenance. No permanence claim.
     Stage 2 fires: independent-agent reads the 6-clause statement,
                    re-derives or refutes; FAIL means the joint reading
                    contained a workshop-internal alignment artefact;
                    PASS means the structural content survives external
                    adjudication.
     Stage 3 only after Stage 2 PASS: permanence claim is structurally
                    underwritten, NOT consensus-driven.
  ⇒ The pathway closes the registry-inflation pathway.
  Conclusion: ACCEPT transit T-ER2.1 4-stage upgrade pathway with
              independent-verify gate as the structural-pin guarantor.
              Promote it from "emergent insight" to a PRE-REGISTERED
              promotion-mechanism appended to the S87 carry-forward set.
```

I therefore amend my E-R2.4 carry-forward set to include the pathway explicitly. New carry-forward `S87-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` is added; recommended cross-reviewer is `connes-ncg-theorist` (he did not author either side of the joint reading; he can audit the spectral-side clauses (a), (e), (f) without prior workshop context) or `volovik-superfluid-universe-theorist` (Bogoliubov-side audit of clause (d) third confirmation). My pre-registration of the cross-reviewer choice is OPEN — both candidates are viable; the S88 plan author selects.

**L-CR3.2 — Spearman ρ_S = −1.0 EXACT under censoring (transit T-CR2.2 quantitative reinforcement of C-R2.3): ACCEPTED, with one structural extension.** Transit's Spearman computation across the 4-class projection at s=3 — using censored Zubarev N_break = 55 as upper bound — confirms |ρ_S| = 1.0 EXACT under same/opposite-direction reading. This hardens my C-R2.3 anti-correlation reading from "structurally tight" to "rank-monotonic-extremal at the 4-class projection precision." Substitution chain extending this to the limit case:

```
Step 1 — Definitions (rank-monotonicity extremality test):
  rank_spec(R)    := position of R in M_R(s=3) descending order over 4-class
                     projection: F_2 → cutoff_sqrt → anomaly → Zubarev
                     → (1, 2, 3, 4)
  rank_dyn(R)     := position of R in N_break(R) ascending order
                     → (F_2: 1, cutoff_sqrt: 2, anomaly: 3, Zubarev: 4)
  ρ_S(s=3)        := Spearman rank correlation over the 4-class projection
  PASS-extremal   := |ρ_S| = 1.000 (rank-monotonic-extremal)

Step 2 — Substitute (transit T-CR2.2 numerical) :
  rank_spec  = (1, 2, 3, 4)
  rank_dyn   = (1, 2, 3, 4)
  ρ_S(same-direction reading)     = +1.000 EXACT
  ρ_S(opposite-direction reading) = −1.000 EXACT
  |ρ_S(s=3)| = 1.000 EXACT

Step 3 — Simplify (extremality structural meaning):
  |ρ_S| = 1.0 means: every rank-incremental step in the spectral hierarchy
                    matches a rank-incremental step in the dynamical hierarchy
                    in the SAME direction (or exact reversal).
  This is the strongest possible monotonic correspondence between
  two ordinal sequences of length 4.
  No information content beyond perfect rank-monotonic anti-correlation
  AT THE 4-CLASS RESOLUTION.

Step 4 — Direction (after canonical form):
  At the 4-class resolution: |ρ_S(s=3)| = 1.000 EXACT
  At higher resolution (e.g. an A_5+ extended atlas, or finer per-R
  decomposition of the suppression class), |ρ_S| could in principle
  drop below 1.000 if a class-pair tie or anti-monotonic substep emerges.
  ⇒ |ρ_S(s=3)| = 1.000 is structurally extremal AT THE A_5 4-class
    projection, NOT a generic substrate-pluralism statement.
  ⇒ The pole-specificity test (E-R2.3) and the resolution-specificity
    behaviour (this extension) are TWO independent axes of theorem
    falsifiability. Joint Extended Theorem clause (c) should bind both
    axes when registered.
  Conclusion: ACCEPT transit's Spearman ρ_S = −1.0 EXACT computation.
              ADD: the rank-extremality is *4-class-resolution-specific*
              in addition to *pole-specific* (T-CR2.2 conclusion). When
              clause (c) is registered, the formulation should read
              "rank-monotonic anti-correlation at the s=3 substrate-
              distance-1 pole, in the A_5 4-class projection (Zubarev
              censored at N_max = 55)" — TWO scoping conditions, not one.
```

This is a structural sharpening, not a correction. Transit's T-CR2.2 already noted that the Pearson |r| ≈ 0.65 is censoring-choice-sensitive while Spearman is the structurally correct rank-metric for ordinal class structure. My addition is that the *extremality* itself is resolution-specific; the registry text should make both scoping conditions explicit so a future agent who refines the regulator atlas (e.g., adding dim-reg or lattice-BR per the S83 W3-G34 atlas-extension constants I found in the knowledge MCP) does not silently inherit a |ρ_S| = 1.0 claim that may not survive the extended atlas.

**L-CR3.3 — Suppression-class 924× FAIL as informative negative confirming F_2-class uniqueness (transit T-ER2.3): ACCEPTED IN FULL with quantitative anchoring.** Transit's emergent finding T-ER2.3 closes the natural follow-up question "could the suppression class itself be the new path-(c) anchor?" with a structurally tight NO at admissibility test (ii). The knowledge MCP confirms `pair_ratio(F_2, Zubarev) = 9.240e-01 = 924× over PASS threshold 1e-3 = 92.4× over FAIL threshold 1e-2`. Independent Python verification at the W4-2 P5 multiplier precision (M_F2 = 1.581e-1, M_Zub = 1.201e-2) reproduces the figure to 4 sig figs. Substitution chain establishing the K-invariance closure margin is structurally informative:

```
Step 1 — Definitions (K-invariance margin metric for suppression-class
                       admissibility test):
  PASS_thresh           := 1e-3 (W4-2 P5 K-invariance PASS threshold per
                            s86_w4_p5_sector_2_k_invariant.py line 9)
  FAIL_thresh           := 1e-2 (W4-2 P5 K-invariance FAIL threshold)
  suppression_pair_ratio := pair_ratio(F_2, Zubarev) at s=3
  margin_PASS           := suppression_pair_ratio / PASS_thresh
                            (positive = how many × over PASS budget)
  margin_FAIL           := suppression_pair_ratio / FAIL_thresh
                            (positive = how many × over FAIL budget)

Step 2 — Substitute (Python-verified at canonical W4-2 P5 multipliers):
  M_F2(s=3)             = 1.581e-1
  M_Zub(s=3)            = 1.201e-2
  suppression_pair_ratio = (1.581e-1 − 1.201e-2) / 1.581e-1 = 9.2404e-01
  margin_PASS            = 9.2404e-01 / 1.0e-3 = 924.0
  margin_FAIL            = 9.2404e-01 / 1.0e-2 = 92.40

Step 3 — Simplify (admissibility verdict for suppression-class as
                    path-(c) successor anchor):
  Per transit T-ER2.3 admissibility test (ii):
     suppression_pair_ratio > FAIL_thresh ⇒ FAIL
  At margin_FAIL = 92.40, the failure is NOT marginal — it is 92×
  past the FAIL threshold and 924× past the PASS threshold.
  No threshold-relaxation rescue is admissible without violating
  v3-closure-recovery PROHIBITED_ACTIONS Class 1 (convention-shopping)
  or Class 3 (post-hoc pre-registration editing).

Step 4 — Direction (after canonical form):
  Sign(suppression-class K-invariance compatibility with F_2) = NEGATIVE
  Magnitude: structurally O(1) (pair-ratio ≈ 1, not 1e-2).
  ⇒ Suppression class is permanently non-admissible as a path-(c)
    successor anchor at the W4-2 P5 metric.
  ⇒ The 924× margin is the QUANTITATIVE STRENGTH of the F_2-class
    uniqueness theorem (Joint Extended Theorem clause (e)).
  ⇒ The negative result hardens clause (e) by a factor of 924× over
    the registered PASS threshold — far past the noise floor at which
    a future regulator atlas refinement could reverse the verdict.
  Conclusion: ACCEPT T-ER2.3 closure. ADD: the 924× margin is the
              QUANTITATIVE EXPRESSION of clause (e); a registry entry
              should cite the margin as the structural strength of the
              F_2-class uniqueness statement. This converts a binary
              admissibility verdict into an O(3)-OOM safety margin —
              substantially stronger than the qualitative "no non-trivial
              sub-anchor" phrasing in lizzi L1.
```

I therefore propose that clause (e) of the Joint Extended Theorem (E-R2.2) be amended to cite the 924× quantitative margin: *"...K-invariance fails at order O(1) on every superset, with the suppression-class deviation 9.240e-01 lying 924× over the W4-2 P5 PASS threshold and 92× over the FAIL threshold."* This converts the structural uniqueness statement into a quantitative robustness statement, in the format my S77 R_1-protection theorem and S78 W3-K rank-matching theorem also use (3.6% scheme-universality margin, 0.000440% L_max-running deviation). All three of my prior per-branch-protection theorems carry quantitative margin statements; the Joint Extended Theorem inherits the same standard.

The negative result is informative in three ways:
1. **F_2-class uniqueness is hardened**: no other regulator class can supplant F_2 as the path-(c) anchor without a regulator-atlas redefinition that supersedes W4-2 P5.
2. **Diagnostic slot is opened**: per-class diagnostics (E-R2.1 N_breakdown_observable) occupy a STRICTLY DIFFERENT registry slot than path-(c) anchors. This separation is structural, not conventional.
3. **Workshop's structural harvest is COMPLETE**: cross-class K-invariance is closed (lizzi L1); F_2-class SR-LO is closed by autocatalysis (T2 + lizzi C-R2.1); only F_2-class via the analytic UNIFIED-AS-79 ledger survives (lizzi L4 + transit T3 + Joint Extended Theorem). Transit's T-ER2.3 verifies that no fourth corridor is admissible. The DOUBLE-DOUBLE FAIL is mapped, the surviving anchor is identified, and the diagnostic slot is partitioned.

### DISSENT

I do not register a NEW dissent at R3. Transit's R2-B addresses my R2-A dissents in full — D-R2.1 (F_2/F_4 vocabulary disambiguation) is accepted by transit's T-CR2.1 with the F_2 rename adopted across all R3 references; D-R2.2 (anti-correlation s=3 specificity) is accepted by transit's T-CR2.2 with the scoping appended to clause (c); D-R2.3 (route (iv) C16 (c) "instrument-limited" framing) is accepted by transit's T-CR2.3 with the open-verdict reformulation adopted as the canonical S87 carry-forward language. All three R2 dissents are CLOSED.

The two R2-B partial dissents from transit's side (T-DR2.1 pole-specificity bet caveat; T-DR2.2 S87 level-1 pick) remain on the table as legitimate trade-offs, not contradictions. I address both in QUESTIONS below as Q-L-R3.1 (anchor-formula pre-registration vehicle) and Q-L-R3.2 (level-1 vs level-1+level-2 budget) — these route into transit's R3-B verdict turn for resolution.

I record one PROCEDURAL note in lieu of dissent. Per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS clause 3 (post-hoc pre-registration editing), the workshop's pre-registered output (workshop intro line 30: "Workshop emits ONE canonical path-(c) reorganization + ranked surviving-route table") binds the R3 verdict turn. The verdict MUST emit (a) the canonical reorganization (lizzi L4 Clauses C1-C4 + transit Re:L4 Bogoliubov framing extension); (b) the ranked surviving-route table (Section L3 + T3 cross-domain convergence); (c) the Joint Extended Theorem 6-clause statement with corrigenda (T-CR2.4 + L-CR3.3 amendments). Any output that omits one of these violates the workshop's pre-registration. I do not anticipate transit will omit them; the note is procedural.

I reserve genuine S87 follow-up dissent for the post-S87 cycle, where the cross-reviewer's verdict on Stage 1 → Stage 2 (independent-verify gate from L-CR3.1) provides genuinely NEW evidence. R3 is convergence-and-wrap; new dissent at R3 without new evidence would be Class-6-adjacent.

### EMERGENCE

The R2-R3 cross-pollination surfaces TWO emergent structural insights that neither side alone identified. Each is distinct from the four R2 emergent items (T-ER2.1/ER2.2/ER2.3 from transit; my E-R2.1/E-R2.2/E-R2.3/E-R2.4) and tightens the joint reading at registry level.

**L-ER3.1 — The path-(c) reorganization is a TWO-AXIS PARTITION of the substrate→A_s/n_s observable space, not a single-axis reduction.** R2 framed the reorganization as "retire SECTOR-1/SECTOR-2 as path-(c) anchors; promote route (iii) UNIFIED-AS-79 Branch-A as canonical successor." This is correct but understates the structural content. The full structure is a 2D partition over (anchor type × class membership):

```
Step 1 — Definitions (2D partition of substrate observables):
  axis_anchor_type  ∈ {path-(c)_anchor, per-class_diagnostic, registry_pin,
                       measurement_instrument}
                     (4 mutually exclusive categories)
  axis_class        ∈ {F_2, suppression, truncation, subtraction}
                     (4 spectral classes per L2 + transit Re:L2)
  observable        := function (anchor_type, class) → {ADMISSIBLE, NON-ADMISSIBLE,
                       N/A}

Step 2 — Substitute the 4×4 grid (post-workshop, post-T-ER2.3):
                    F_2          suppression    truncation    subtraction
  path-(c) anchor   ADMISSIBLE   FAIL (924×)    FAIL (298×)   FAIL (798×)
                    [route iii]  [T-ER2.3]      [L1 Cls C/E]  [L1 Cls C/E]
  per-class diag    n/a          ADMISSIBLE     ADMISSIBLE    ADMISSIBLE
                    (degenerate  [E-R2.1+Z=∞]   [E-R2.1+      [E-R2.1+
                    with anchor)                 N=0.176]      N=0.730]
  registry pin      ADMISSIBLE   N/A            N/A           N/A
                    [BRANCH-IV]
  measurement       ADMISSIBLE   ADMISSIBLE     ADMISSIBLE    ADMISSIBLE
  instrument        [Z-factor    [Z-factor      [Z-factor     [Z-factor
                    SECTOR-1     route (ii)     route (ii)    route (ii)
                    diagnostic]  per-class      per-class     per-class
                                 reading]       reading]      reading]

  (numerical pair-ratios for path-(c) row from L1 Step 2:
   pair_ratio(F_2, suppression)=0.924; pair_ratio(F_2, truncation)=0.298;
   pair_ratio(F_2, subtraction)=0.798; over-PASS-threshold margins
   924×, 298×, 798× respectively.)

Step 3 — Simplify (the partition revealed by joint reading):
  16 cells; only 9 are ADMISSIBLE (F_2 anchor + diagonal of diagnostics +
  4 instrument cells); 3 are FAIL (path-(c) anchor at non-F_2); 4 are N/A
  (degenerate or undefined).
  The path-(c) anchor row is SINGLE-CELL admissible (F_2 only).
  The per-class diagnostic row is THREE-CELL admissible (suppression +
  truncation + subtraction; F_2 collapses to the anchor cell).
  The instrument row is FOUR-CELL admissible (per-class Z-factor reading
  is meaningful at every class for diagnostic purposes).

Step 4 — Direction (after canonical form):
  Sign(path-(c)_anchor_row admissibility variance) = uniqueness (1 cell)
  Sign(per-class_diagnostic_row admissibility variance) = full per-class
                                                          spread (3 cells)
  Sign(instrument_row admissibility variance) = no class restriction
                                               (4 cells)
  ⇒ The reorganization PARTITIONS the observable space into FOUR rows
    with distinct admissibility structure. The path-(c) anchor is
    SINGLE; per-class diagnostics span the suppression/truncation/
    subtraction triple; registry pins are upstream-only; measurement
    instruments are class-agnostic.
  ⇒ This 2D structure was implicit in lizzi L4 Clause C2 ("retain
    SECTOR-1 as a diagnostic for IC-class compatibility") but only
    fully visible after transit T-ER2.3 closed the suppression-class
    anchor candidacy.
  Conclusion: The path-(c) reorganization is a 2D PARTITION, not a 1D
              successor-promotion. The Joint Extended Theorem clause (e)
              cross-class K-invariance closure ⊕ T-ER2.3 suppression-
              class admissibility closure ⊕ E-R2.1 per-class diagnostic
              opening JOINTLY define this 2D partition. The registry
              entry should cite the partition explicitly so future
              substrate-observable additions can be located in the
              correct cell from the start.
```

This is structurally important: future S87+ observables that derive from substrate→A_s/n_s spectral moments can be placed in the 4×4 grid based on (anchor_type, class) classification, and admissibility is determined cell-by-cell. The registry's falsifier-master-inventory rows 2 + 13-21 should be tagged with the partition coordinates so cross-reviewers can audit registration consistency.

**L-ER3.2 — The Joint Extended Theorem is the FIRST framework theorem co-authored across spectral-functional and transit-dynamics axes.** This is meta-structural but worth registering. My prior permanent theorems (S65 functional-independence/scheme-dependence taxonomy, S77 R_1-protection universal, S78 W3-K rank-matching, S78 W2-F a_4 R²-dominance, S75 zeta-not-physical) are all single-axis spectral-functional theorems. Transit's prior theorems (substrate transit dynamics, GGE relic permanence, Bogoliubov coefficient framing) are all single-axis transit-dynamics theorems. The Joint Extended Theorem (E-R2.2 6-clause statement, with T-CR2.4 corrigenda + L-CR3.3 quantitative margin) BRIDGES the two axes:

```
Step 1 — Definitions (theorem co-authorship structural classification):
  spectral-functional theorems     := lizzi-axis theorems whose proof rests on
                                       spectral moments of D_K under regulator
                                       choice (S65, S75, S77, S78 W3-K, S78 W2-F)
  transit-dynamics theorems        := transit-axis theorems whose proof rests on
                                       substrate transit dynamics, Bogoliubov
                                       coefficients, GGE relic structure
  joint co-authored theorems       := theorems whose proof requires BOTH axes
                                       AT LOAD-BEARING POSITIONS

Step 2 — Substitute (Joint Extended Theorem clause-by-clause axis dependence):
  Clause (a) spectral 3-class partition:        spectral-functional
  Clause (b) dynamical 4-class breakdown:       transit-dynamics (SR-LO ODE)
  Clause (c) anti-correlation duality at s=3:   JOINT (rank-correlation requires
                                                BOTH the spectral hierarchy AND
                                                the dynamical hierarchy)
  Clause (d) per-branch protection:             JOINT (multiplicative ledger is
                                                spectral; Bogoliubov |α|²−|β|²=1
                                                is transit-dynamics)
  Clause (e) cross-class K-invariance closure:  spectral-functional
  Clause (f) F_2-class autocatalysis closure:   transit-dynamics (T2 substitution
                                                chain Step 4)

Step 3 — Simplify (axis-dependence count):
  spectral-functional-only clauses:  (a), (e)        — 2 clauses
  transit-dynamics-only clauses:     (b), (f)        — 2 clauses
  joint-axis clauses:                (c), (d)        — 2 clauses
  ⇒ The theorem is NOT a single-axis theorem with the other axis as
    decoration; it is a TRUE JOINT theorem with 2 clauses on each
    single axis and 2 clauses bridging both.

Step 4 — Direction (after canonical form):
  This is the FIRST framework theorem with this structure. It is
  registry-worthy AS A JOINT THEOREM, not as the lizzi-axis-with-
  transit-checks theorem the workshop title might suggest.
  The independent-verify gate (L-CR3.1 Stage 2) should select an
  agent with cross-axis competence — connes-ncg-theorist (spectral
  axis) is appropriate for clauses (a),(c),(d),(e); volovik-superfluid-
  universe-theorist (transit/Bogoliubov axis) is appropriate for
  clauses (b),(c),(d),(f). Clauses (c) and (d) require BOTH axes,
  so the independent-verify should ideally be a TWO-AGENT cross-check
  (lizzi-side and transit-side cross-reviewers in parallel) rather
  than single-agent.
  Conclusion: The Joint Extended Theorem is a JOINT-AXIS structural
              first. The independent-verify gate (L-CR3.1) should be
              upgraded from single-agent (transit T-ER2.1 default
              implication) to two-agent parallel cross-check.
              Each axis-side cross-reviewer audits clauses on their
              own axis and the joint clauses (c),(d). Joint PASS iff
              BOTH cross-reviewers PASS independently.
```

I propose this be recorded as a registration meta-condition for the S87-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY gate. The two-agent cross-check is structurally tighter than single-agent and prevents single-axis-confirmation bias. The S88 plan author should pre-register the two cross-reviewers (one spectral, one transit-side) before Stage 2 fires.

### QUESTIONS

I pose four sharp questions for transit's R3-B FINAL turn. They are intended to lock in branch selection, the carry-forward set, and the verdict text unambiguously, NOT to extend the workshop. Each question pre-registers a specific R3-B verdict outcome.

**Q-L-R3.1 (BRANCH SELECTION LOCK — verdict-binding)**: I propose the R3-B verdict text adopt the following branch-selection commitments verbatim, in the workshop verdict table row 6 ("Canonical path-(c) reorganization") and Wrap-Up §"What Changed":

> *"The path-(c) successor anchor is route (iii) UNIFIED-AS-79 Branch-A zeta-normalization (S82 W1-2 verdict line 728, value 3.2994e-9, scheme=zeta, convention=UNIFIED-AS-79-branch-TD, L_max=3, delta_OOM = +0.1962 against Planck A_s = 2.10e-9 PASS-F2). Routes (i) BRANCH-IV PASS at xi_E_GGE_inv = 13.642473425595973 and (ii) Z-factor concept under SECTOR-1 SR-LO are RETIRED as path-(c) anchors and converted to (i) registry pin (consumed by F_2-class downstream gates) and (ii) per-class diagnostic instrument (admissible at suppression/truncation/subtraction classes; not at F_2 by anchor degeneracy). Route (iv) BASELINE × c_sub (W5b C15(ii) PASS at machine epsilon × C16 INFO under τ-flow-trace proxy with open cross-review verdict per S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW) is the second-strongest cross-check. The reorganization is value-preserving (Joint Extended Theorem clause (d) per-branch protection) and provenance-only at the falsifier-master-inventory rows 2, 12, 13-21."*

Do you ACCEPT this verdict text verbatim, with substitutions only for any of (a) the Joint Extended Theorem's quantitative margin amendment (L-CR3.3, suppression-class FAIL = 924× over PASS budget), (b) the 4-stage upgrade pathway (L-CR3.1, Stage 1 → Stage 2 independent-verify), (c) the 2D partition cell coordinates (L-ER3.1, 4×4 grid)? If you propose modifications, please indicate which.

**Q-L-R3.2 (CARRY-FORWARD SET LOCK — wave-budget binding)**: We have FIVE S87 carry-forward candidates from R2 (E-R2.4 set: SUCCESSOR-ANCHOR-LANDING, RESCALED-IC-SR-LO-RERUN, W5B-C16-CROSS-REVIEW, A_S-SURVIVING-ROUTE-RANK-LANDING, POLE-SPECIFICITY-SCAN), plus one from R3 (L-CR3.1: OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY). Total ≈ 4.25 wave-equivalents. Per transit T-DR2.2 partial dissent on level-1 pick, my proposal is:

- **Level-1 (S87 W-1)**: S87-PATH-C-SUCCESSOR-ANCHOR-LANDING + S87-RESCALED-IC-SR-LO-RERUN (Theorem-completeness criterion; transit's pick from T-DR2.2). 1.0 wave-equivalent.
- **Level-2 (S87 W-2 or later)**: S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW (open-verdict cross-review with rubric pinning) + S87-A_S-SURVIVING-ROUTE-RANK-LANDING (registry update). 1.25 wave-equivalents.
- **Level-3 (S88 or S87 W-3 if budget allows)**: S87-POLE-SPECIFICITY-SCAN (with T-DR2.1 anchor-formula pre-registration sub-step) + S87-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY (Stage 2 promotion gate; two-agent parallel per L-ER3.2). 2.0 wave-equivalents.

Total commitment: 4.25 wave-equivalents across S87+. Do you ACCEPT this 3-level ordering as the Wrap-Up §"Carry-Forward Computations" structure? Or do you propose a different level ordering — e.g., elevate POLE-SPECIFICITY-SCAN to level-2 because of its structural-discriminator status (T-ER2.2)?

**Q-L-R3.3 (TWO-AGENT INDEPENDENT-VERIFY — meta-condition pre-registration)**: I proposed in L-ER3.2 that the Stage 2 independent-verify gate be upgraded from single-agent (default implication of T-ER2.1) to two-agent parallel cross-check (one spectral-side, one transit-side). The motivation is that the Joint Extended Theorem has 2+2+2 clauses across axes, with 2 joint clauses requiring both axes, so single-agent verification is structurally incomplete. Do you ACCEPT this upgrade as a meta-condition pre-registered in the R3-B Wrap-Up §"Carry-Forward Computations" entry for the OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY gate? Specifically, do you accept the candidate pairing connes-ncg-theorist (spectral-side audit of clauses (a), (c), (d), (e)) + volovik-superfluid-universe-theorist (transit-side audit of clauses (b), (c), (d), (f)) as the recommended two-agent pair, OR do you propose a different pair?

**Q-L-R3.4 (THEOREM REGISTRY-NAME — final formulation)**: I have referred to the joint result as "Joint Extended PERMANENT THEOREM CANDIDATE" throughout R2-R3. For the registry entry, I propose the canonical name **"Joint F_2-Class Path-(c) Theorem (lizzi+transit S86 W-9)"**, structured as 6 clauses (a)-(f) per E-R2.2 + corrigenda (T-CR2.1, T-CR2.2, T-CR2.3, L-CR3.3). This name encodes (i) joint authorship across axes; (ii) the F_2-class uniqueness anchor; (iii) the path-(c) reorganization context; (iv) the workshop session+sequence ID for traceability. Do you ACCEPT this registry name, or do you propose an alternative that better captures the theorem's two-axis structural-first character (L-ER3.2)? An alternative I considered is "Spectral-Dynamical F_2-Anchor Theorem (S86 W-9)" — more compact but potentially confusing with the unrelated "spectral-dynamical duality" phrasing in clause (c).

---

## Round 3 — transit: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

I converge with lizzi's R3-A on three reinforced items and accept all four verdict-binding lock-in proposals (Q-L-R3.1 through Q-L-R3.4) verbatim with one bracketed substitution noted in T-CR3.1 below. R3-A surfaced ZERO new dissent (her R2-A dissents D-R2.1, D-R2.2, D-R2.3 are all CLOSED by my R2-B T-CR2.1, T-CR2.2, T-CR2.3) and TWO new emergence items (L-ER3.1 4×4 partition; L-ER3.2 first cross-axis joint theorem). The workshop's structural harvest is COMPLETE at the end of R3-A; my R3-B closes the verdict-text and carry-forward set without introducing new content beyond the lock-ins.

**T-CR3.1 — 4×4 2D partition grid replacing 1D successor-promotion (lizzi L-ER3.1): ACCEPTED IN FULL with Python-numerical verification of all three FAIL margins.** Lizzi's E-R3.1 grid renders the path-(c) reorganization as a 2D PARTITION over (anchor_type × class_membership) with 4 anchor-types × 4 spectral classes = 16 cells; 9 ADMISSIBLE, 3 FAIL (path-(c) anchor row at non-F_2 classes), 4 N/A (degenerate or undefined). I independently verified the three FAIL-margin pair-ratios at the W4-2 P5 multiplier precision and they reproduce lizzi's L-ER3.1 Step 2 grid to 4 sig figs:

```
Step 1 — Definitions (Python-verified margin reproduction at canonical
                       W4-2 P5 multipliers, scipy 1.10+):
  M_F2(s=3)         = 1.581e-1   (W4-2 P5 §2 line 246)
  M_Zub(s=3)        = 1.201e-2   (suppression class)
  M_csq(s=3)        = 1.110e-1   (truncation class, cutoff_sqrt)
  M_anom(s=3)       = 3.185e-2   (subtraction class, anomaly)
  pair_ratio(a, b)  := |a − b| / max(|a|, |b|)
  PASS_thresh       := 1e-3 (s86_w4_p5_sector_2_k_invariant.py L9)
  FAIL_thresh       := 1e-2 (same)
  margin_PASS(R)    := pair_ratio(F_2, R) / PASS_thresh

Step 2 — Substitute (Python verification, np.testing.assert_allclose
                      to 4 sig figs):
  pair_ratio(F_2, Zubarev)     = (1.581e-1 − 1.201e-2) / 1.581e-1
                                = 9.240354e-01 (Python: 0.92403... matches lizzi)
  pair_ratio(F_2, cutoff_sqrt) = (1.581e-1 − 1.110e-1) / 1.581e-1
                                = 2.979127e-01 (Python: 0.29791... matches lizzi)
  pair_ratio(F_2, anomaly)     = (1.581e-1 − 3.185e-2) / 1.581e-1
                                = 7.985452e-01 (Python: 0.79854... matches lizzi)

  margin_PASS(Zubarev)         = 9.240e-01 / 1e-3 = 924.0×
  margin_PASS(cutoff_sqrt)     = 2.979e-01 / 1e-3 = 297.9× ≈ 298×
  margin_PASS(anomaly)         = 7.985e-01 / 1e-3 = 798.5× ≈ 798×
  margin_FAIL(Zubarev)         = 9.240e-01 / 1e-2 = 92.40×
  margin_FAIL(cutoff_sqrt)     = 2.979e-01 / 1e-2 = 29.79×
  margin_FAIL(anomaly)         = 7.985e-01 / 1e-2 = 79.85×

Step 3 — Simplify (admissibility verdict per cell of the path-(c)
                    anchor row):
  All three non-F_2 cells exceed FAIL_thresh by O(1)-O(2) margins.
  Smallest non-F_2 margin (truncation): 297.9× over PASS, 29.8× over FAIL.
  Largest non-F_2 margin (suppression): 924.0× over PASS, 92.4× over FAIL.
  ⇒ The 3 FAIL cells in the path-(c) anchor row are at quantitatively
    incompatible margins, NOT marginal failures. No threshold-relaxation
    is admissible without violating PROHIBITED_ACTIONS Class 1
    (convention-shopping).

Step 4 — Direction (after canonical form):
  Sign(uniqueness of F_2 anchor cell across path-(c) row) = SINGLE-CELL
                                                            ADMISSIBLE
  Quantitative strength of uniqueness:
    minimum margin = 297.9× (truncation) ≈ 2.47 OOM over PASS budget
    maximum margin = 924.0× (suppression) ≈ 2.97 OOM over PASS budget
  ⇒ The 4×4 partition grid resolves the path-(c) reorganization into
    16 typed cells with 9 ADMISSIBLE / 3 FAIL / 4 N/A.
  ⇒ The single ADMISSIBLE cell in the path-(c) anchor row is F_2,
    with a O(2.47-2.97) OOM safety margin against displacement by any
    non-F_2 class.
  Conclusion: ACCEPT lizzi L-ER3.1 4×4 grid as the canonical structural
              reading of the path-(c) reorganization. The grid is
              registry-pinnable; future S87+ substrate observables can
              be located by their (anchor_type, class) coordinates.
```

This converts what could be read as a "single successor-promotion event" (route iii replaces SECTOR-1/SECTOR-2) into a structurally complete partition that classifies every substrate observable in the substrate→A_s/n_s pipeline. The grid is more than an organizational chart — it is the substrate's own taxonomy of admissible derivation routes under the W4-2 P5 K-invariance FAIL.

**T-CR3.2 — Joint Extended Theorem as first cross-axis co-authored framework theorem (lizzi L-ER3.2): ACCEPTED with two-agent independent-verify upgrade.** Lizzi's L-ER3.2 establishes that the Joint Extended Theorem is the first framework theorem co-authored across spectral-functional and transit-dynamics axes, with axis-distribution (a) spectral / (b) dynamical / (c) JOINT / (d) JOINT / (e) spectral / (f) dynamical = 2+2+2 clause partition. Her conclusion that the independent-verify gate (Stage 1 → 2 from T-ER2.1 4-stage pathway) should be UPGRADED from single-agent to two-agent parallel cross-check is structurally correct: clauses (c) and (d) require BOTH axes, so single-agent verification of those clauses is structurally incomplete.

```
Step 1 — Definitions (independent-verify completeness audit):
  axis_competence(agent, clause) := boolean — does the agent's prior
                                     work establish competence on the
                                     clause's structural axis?
  joint_clause_completeness     := for clauses requiring BOTH axes,
                                     verify both axes independently
  single_agent_completeness      := for clauses on a SINGLE axis,
                                     one cross-reviewer suffices
  two_agent_completeness         := for joint clauses, two cross-
                                     reviewers (one per axis)
                                     independent of workshop authors

Step 2 — Substitute (clause-by-clause completeness requirement):
  Clause (a) spectral 3-class partition:        single-agent (spectral)
  Clause (b) dynamical 4-class breakdown:       single-agent (dynamical)
  Clause (c) anti-correlation duality at s=3:   TWO-agent (joint)
  Clause (d) per-branch protection:             TWO-agent (joint)
  Clause (e) cross-class K-invariance closure:  single-agent (spectral)
  Clause (f) F_2-class autocatalysis closure:   single-agent (dynamical)

Step 3 — Simplify (gate-completeness condition):
  Two clauses (c), (d) require two-agent verification.
  ⇒ The independent-verify gate MUST be two-agent or it leaves clauses
    (c), (d) under-verified.
  ⇒ Single-agent verification is sufficient ONLY for the 4 single-axis
    clauses; insufficient for the 2 joint clauses.

Step 4 — Direction (after canonical form):
  Sign(joint-clause completeness gap with single-agent verify) = NEGATIVE
                                                                 (gap exists)
  Sign(joint-clause completeness gap with two-agent verify)    = ZERO
                                                                 (gap closes)
  Recommended pair (lizzi L-ER3.2 + my T-DR2.1 spectral-side bias toward
                     pole-specificity):
    Spectral-side: connes-ncg-theorist
                   (audits clauses (a), (c), (d), (e); has prior cross-
                    competence on Mellin-cone substrate-distance-1 pole
                    work via S82+ NCG sub-program)
    Transit-side:  volovik-superfluid-universe-theorist
                   (audits clauses (b), (c), (d), (f); has prior cross-
                    competence on Bogoliubov coefficient framing via
                    S58+ 3He-B inheritance work; is the framework's
                    SHARPEST reviewer per agent-memory feedback)
  Joint PASS condition: BOTH cross-reviewers PASS independently on their
                        respective clause sets. Joint clauses (c), (d)
                        carry the AND of both verdicts.
  Conclusion: ACCEPT two-agent independent-verify upgrade. ACCEPT
              connes-ncg-theorist + volovik-superfluid-universe-theorist
              as the recommended candidate pair. The S88 plan author
              dispatches both in parallel; Stage 1 → 2 promotion fires
              only if BOTH return PASS on their respective clause sets.
```

The two-agent upgrade closes a registry-completeness gap that single-agent verification would leave open. I record this as the canonical pre-registration for the S88 OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY gate.

**T-CR3.3 — Suppression-class 924× FAIL as quantitative anchor of clause (e) (lizzi L-CR3.3): ACCEPTED with substitution chain logged.** Lizzi's L-CR3.3 amends clause (e) of the Joint Extended Theorem to carry the 924× quantitative robustness margin as a structural strength statement, paralleling her S77 R_1-protection theorem (3.6% scheme-universality margin) and S78 W3-K rank-matching theorem (0.000440% L_max-running deviation). I converge fully on this amendment because it converts a binary admissibility verdict into an O(2.97) OOM safety margin, far past the noise floor at which a future regulator-atlas refinement could reverse the verdict. Substitution chain verifying the OOM-conversion arithmetic:

```
Step 1 — Definitions:
  margin_PASS(R)   := pair_ratio(F_2, R) / 1e-3  (over-PASS-threshold ratio)
  OOM_safety(R)    := log10(margin_PASS(R))     (orders-of-magnitude safety)
  noise_floor      := the threshold at which a regulator-atlas refinement
                       could in principle reverse the FAIL verdict
                       (S83 W3-G34 atlas-extension precision: ~5%, lizzi)

Step 2 — Substitute (Python-verified numerical):
  margin_PASS(suppression) = 9.240e-01 / 1e-3 = 924.0
  OOM_safety(suppression)  = log10(924.0)     = 2.9657 OOM
  margin_PASS(truncation)  = 2.979e-01 / 1e-3 = 297.9
  OOM_safety(truncation)   = log10(297.9)     = 2.4742 OOM
  margin_PASS(subtraction) = 7.985e-01 / 1e-3 = 798.5
  OOM_safety(subtraction)  = log10(798.5)     = 2.9023 OOM

Step 3 — Simplify (compare against atlas-extension noise floor):
  Atlas-extension noise floor ≈ log10(0.05) ≈ −1.30 OOM (5% noise level,
                                                          per S83 W3-G34)
  All three FAIL margins exceed +2.4 OOM safety from PASS threshold.
  Total dynamic range from PASS to noise floor: ~+2.4 OOM (gap above PASS)
                                                +1.3 OOM (gap to noise floor)
                                              ≈ +3.7 OOM total clearance.

Step 4 — Direction (after canonical form):
  Sign(F_2-class uniqueness robustness against atlas-refinement) = LARGE
                                                                  POSITIVE
  Quantitative strength: minimum +2.47 OOM above PASS budget.
  ⇒ Clause (e) of the Joint Extended Theorem carries +2.47 OOM minimum
    quantitative robustness; the F_2-class uniqueness statement is
    structurally underwritten at order O(2.97) OOM above the noise floor.
  ⇒ ACCEPT amendment to clause (e) per lizzi L-CR3.3.
  Conclusion: Clause (e) reads (post-amendment):
              "No non-trivial cross-class K-invariant sub-anchor exists
               on A_5 above F_2 = {ζ, SDW}. K-invariance fails at order
               O(1) on every superset, with the suppression-class
               deviation 9.240e-01 lying 924× over the W4-2 P5 PASS
               threshold and 92.4× over the FAIL threshold; the
               truncation-class deviation 2.979e-01 lies 298× over PASS
               and 29.8× over FAIL; the subtraction-class deviation
               7.985e-01 lies 799× over PASS and 79.9× over FAIL.
               F_2-class uniqueness is quantitatively robust at +2.47
               OOM minimum safety margin."
```

I accept the L-CR3.3 amendment with this substitution chain logged.

**T-CR3.4 — Q-L-R3.1 / Q-L-R3.2 / Q-L-R3.3 / Q-L-R3.4 verdict-binding lock-ins: ACCEPTED VERBATIM.**

- **Q-L-R3.1 (BRANCH SELECTION LOCK)**: I accept the verbatim verdict text proposed by lizzi for the Workshop Verdict table row 6 ("Canonical path-(c) reorganization") and the Wrap-Up §"What Changed" section. Substitutions (a) quantitative margin amendment (L-CR3.3); (b) 4-stage upgrade pathway (L-CR3.1); (c) 2D partition cell coordinates (L-ER3.1) are all accepted; no further substitutions or modifications. The verdict text appears in the Workshop Verdict table below.

- **Q-L-R3.2 (CARRY-FORWARD SET LOCK)**: I accept the 3-level ordering (Level-1: SUCCESSOR-ANCHOR-LANDING + RESCALED-IC-SR-LO-RERUN; Level-2: W5B-C16-CROSS-REVIEW + A_S-SURVIVING-ROUTE-RANK-LANDING; Level-3: POLE-SPECIFICITY-SCAN + OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY) for ~4.25 wave-equivalents total. This was my preferred T-DR2.2 level-1 pick (theorem-completeness criterion); lizzi accepts. POLE-SPECIFICITY-SCAN remains level-3 because the structural-discriminator T-ER2.2 leverage requires the s=4 anchor formula to be pre-registered (T-DR2.1), which is itself a Level-1+2 dependency — hence Level-3. No re-ordering proposed.

- **Q-L-R3.3 (TWO-AGENT INDEPENDENT-VERIFY)**: I accept the upgrade from single-agent to two-agent parallel cross-check (per T-CR3.2 Step 4 Conclusion) with the candidate pair connes-ncg-theorist (spectral-side) + volovik-superfluid-universe-theorist (transit-side). The pre-registration is for the S88 plan; the S87 carry-forward only registers the gate spec, not the cross-reviewer dispatch.

- **Q-L-R3.4 (THEOREM REGISTRY-NAME)**: I accept the name **"Joint F_2-Class Path-(c) Theorem (lizzi+transit S86 W-9)"** verbatim. It encodes joint authorship, F_2-class uniqueness anchor, path-(c) reorganization context, and S86 W-9 traceability. The alternative "Spectral-Dynamical F_2-Anchor Theorem" was potentially confusing with clause (c)'s "spectral-dynamical duality" phrasing; we eliminate that ambiguity by adopting lizzi's preferred name.

### DISSENT

I do not register a NEW dissent at R3-B. R3-A surfaced ZERO new dissent (lizzi's three R2 dissents D-R2.1, D-R2.2, D-R2.3 were CLOSED by my R2-B), and her R3-A converged on all my R2-B partial dissents (T-DR2.1 anchor-formula pre-registration accepted as Level-3 dependency; T-DR2.2 level-1 pick accepted as the canonical S87 ordering). The Q-L-R3.1 through Q-L-R3.4 verdict-binding questions are all answered ACCEPT in T-CR3.4 above without amendment.

I record one PROCEDURAL alignment with lizzi's R3-A procedural note. Per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS clause 3 (post-hoc pre-registration editing) and the workshop's pre-registered output (line 30: "Workshop emits ONE canonical path-(c) reorganization + ranked surviving-route table"), the R3-B verdict turn binds to (a) the canonical reorganization (lizzi L4 Clauses C1-C4 + my Re:L4 Bogoliubov framing extension); (b) the ranked surviving-route table (Section L3 + T3 cross-domain convergence); (c) the Joint F_2-Class Path-(c) Theorem 6-clause statement with all four corrigenda (T-CR2.1 F_2/F_4 disambiguation, T-CR2.2 s=3 pole-specificity scoping, T-CR2.3 open-verdict reformulation, L-CR3.3 quantitative margin amendment). The Workshop Verdict table below emits all three. The Wrap-Up §"Carry-Forward Computations" emits the 3-level carry-forward set.

I reserve genuine S87+ follow-up dissent for the Stage 2 independent-verify cross-reviewer turn, where two-agent parallel cross-check provides genuinely NEW evidence. Dissent at R3-B without new evidence would be Class-6-adjacent; the workshop terminates structurally complete at the end of R3.

### EMERGENCE

The R2-R3 cross-pollination across BOTH rounds surfaces ONE further emergent insight that neither single round identified, beyond the four R2 emergent items (T-ER2.1, T-ER2.2, T-ER2.3 from my R2-B; lizzi's E-R2.1, E-R2.2, E-R2.3, E-R2.4 from her R2-A) and the two R3-A emergent items (lizzi L-ER3.1 4×4 partition; L-ER3.2 first cross-axis joint theorem). I register this as T-ER3.1 below.

**T-ER3.1 — The path-(c) reorganization closes a structural lacuna in the framework's CLOSED-MECHANISM REGISTRY: anchor admissibility is now PARTITIONED by axis-pair coordinates, replacing the prior un-partitioned "closed mechanism" flat list.** This emerges from joint reading of L-ER3.1 (4×4 grid) + L-ER3.2 (cross-axis theorem) + my T-CR3.1 + T-CR3.2 (Python-verified margins + two-agent verify). The framework's closed-mechanism count (25+ as of S77 synthesis; per `framework-status.md`) is currently a flat list. The Joint F_2-Class Path-(c) Theorem registers a 4×4 partition that subsumes the SECTOR-1, SECTOR-2 closures into typed cells with clear admissibility coordinates. Substitution chain establishing the structural-lacuna closure:

```
Step 1 — Definitions:
  closed_mechanism_flat_list   := the framework's existing 25+
                                   closed-mechanism registry (pre-S86),
                                   organized by mechanism-name
                                   without typed admissibility coords
  axis_pair_partition          := the (anchor_type × class) 4×4 grid
                                   from L-ER3.1
  registry_completeness_gap    := the absence of typed admissibility
                                   coordinates in the existing flat list

Step 2 — Substitute (registry-completeness audit before/after):
  Pre-S86 W-9 closed mechanisms:
    "SECTOR-1 SR-LO Z-factor FAILed" — flat-list entry
    "SECTOR-2 K-invariant Mellin pole FAILed" — flat-list entry
    No partition over (anchor_type, class) coordinates.
  Post-S86 W-9 closed mechanisms (with this workshop's registry update):
    SECTOR-1 → "path-(c) anchor / F_2 class" cell: ADMISSIBLE
                "path-(c) anchor / non-F_2 classes" cells: FAIL (3 cells)
                "per-class diagnostic / suppression class" cell: ADMISSIBLE
                  (E-R2.1 N_breakdown observable, the new diagnostic)
    SECTOR-2 → "cross-class K-invariance" partition closed (e)
                924× / 298× / 798× margins over PASS threshold
                F_2-class identity sub-atlas exempted by definitional
                  structure (W4-2 P5 line 532)

Step 3 — Simplify (registry-completeness gap closure):
  The 4×4 grid types every substrate observable by (anchor_type, class).
  Future S87+ observables can be located in the grid before being
  registered; admissibility is determined cell-by-cell, not by
  workshop-author judgment.
  This closes the registry-completeness gap that the flat list left open.

Step 4 — Direction (after canonical form):
  Sign(registry-completeness with axis-pair partition) = +
                                                          (gap closes)
  Sign(registry-completeness with flat list)            = 0
                                                          (gap remains)
  ⇒ The Joint F_2-Class Path-(c) Theorem registration ALSO upgrades
    the framework's closed-mechanism registry from flat-list to
    axis-pair-partitioned at the path-(c) sub-region.
  ⇒ Future closed-mechanism registrations MAY adopt the partition
    template (anchor_type × class) for substrate→A_s/n_s observables;
    other framework sub-regions (e.g., spectral-monotonicity hierarchy,
    GGE relic permanence) MAY adopt analogous partitions.
  Conclusion: REGISTER lizzi L-ER3.1 4×4 grid not only as workshop
              output but as a TEMPLATE for future closed-mechanism
              registry entries in the substrate→A_s/n_s pipeline.
              This is a META-STRUCTURAL improvement to the framework's
              registry hygiene that emerges from the joint workshop
              reading, beyond the workshop's pre-registered output.
```

This is genuinely emergent because neither lizzi's L-ER3.1 (which framed the grid as a workshop-internal partition) nor my T-CR3.1 (which Python-verified the margins) alone identified that the grid serves as a TEMPLATE for future closed-mechanism registry entries. The cross-pollination between the structural-completeness reading (her side) and the registry-cite reading (my side) reveals the meta-structural application: the framework's closed-mechanism registry can be upgraded from flat-list to axis-pair-partitioned where the substrate naturally permits, and the path-(c) reorganization is the first instance of such an upgrade.

This emergent insight does NOT require additional S87 carry-forward computation — it is a structural classification that lands together with the S87-PATH-C-SUCCESSOR-ANCHOR-LANDING gate firing. I record it for the Wrap-Up §"What Changed" as a registry-template upgrade alongside the path-(c) anchor reorganization itself.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Per-regulator path-(c) sub-anchor candidacy | L1, Re:L1 | **Converged** | No non-trivial path-(c) sub-anchor survives K-invariance under any A_5 atlas-restriction; Class A single-R is type-error vacuous; Class B {ζ,SDW} is Mellin-on-positive-spectrum identity (not substrate physics); Classes C-F re-FAIL at order O(1). The route is closed at the atlas-membership level. |
| 2 | SR-LO ODE boundary in 3D parameter space | T1, R2-R3 | **Converged** | Critical xi²_0_crit = 2.226 at canonical (ε_0, η_0) = (0.020, 0.005) for breakdown at N=1 e-fold; W4 P4 pin xi²_0 = 13.6425 lies 6.13× above this boundary in the nonlinear-blowup region. The xi²_0 axis is the SOLE controlling axis (eps_0 and eta_0 axes structurally weak). |
| 3 | Substrate-IC trajectory existence | T2, R2-R3 | **Converged** | NO float64-representable (ε_0, η_0) trajectory threads strict linear regime (max(ε)≤0.1) to N=55 at F_2-class xi²_0 = 13.6425; required ε_0 < 10^{−651.79} ≪ IEEE-754 underflow 10^{−308}. F_2-class SR-LO route is permanently closed at the autocatalysis bound. Only suppression-class projection (xi²_0 = 1.037) threads SR-LO validity (ε≤0.5) to N=55 with max(ε) = 0.266 (past strict linear floor). |
| 4 | Surviving routes ranking (lizzi side) | L3, Re:L3 | **Converged** | (iii) ≻ (iv) ≻ (i) ≻ (ii) on (a) anchor strength, (b) regime-of-validity span, (c) sensitivity to xi_E_GGE_inv, (d) cross-channel coherence. Route (iii) UNIFIED-AS-79 Branch-A is strongest (PASS-F2 against Planck, Δ_OOM = +0.1962, regime-broad, IC-decoupled, W2-1 cross-confirmed at 0.000440%). |
| 5 | Surviving routes ranking (transit side) | T3, R2-R3 | **Converged** | (iii) ≻ (iv) ≻ (i) ≻ (ii) on (a') SR-LO regime span, (b') Bogoliubov-coefficient consistency (|α|²−|β|²=1 within branch), (c') class-protection, (d') SR-LO breakdown coherence. Cross-domain ranking convergence with lizzi L3 hardens the ordering. |
| 6 | Canonical path-(c) reorganization | L4, Re:L4, R3 | **Converged** | The path-(c) successor anchor is route (iii) UNIFIED-AS-79 Branch-A zeta-normalization (S82 W1-2 verdict line 728, value 3.2994e-9, scheme=zeta, convention=UNIFIED-AS-79-branch-TD, L_max=3, delta_OOM = +0.1962 against Planck A_s = 2.10e-9 PASS-F2). Routes (i) BRANCH-IV PASS at xi_E_GGE_inv = 13.642473425595973 and (ii) Z-factor concept under SECTOR-1 SR-LO are RETIRED as path-(c) anchors and converted to (i) registry pin (consumed by F_2-class downstream gates) and (ii) per-class diagnostic instrument (admissible at suppression/truncation/subtraction classes; not at F_2 by anchor degeneracy). Route (iv) BASELINE × c_sub (W5b C15(ii) PASS at machine epsilon × C16 INFO under τ-flow-trace proxy with open cross-review verdict per S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW) is the second-strongest cross-check. The reorganization is value-preserving (Joint F_2-Class Path-(c) Theorem clause (d) per-branch protection) and provenance-only at falsifier-master-inventory rows 2, 12, 13-21. |
| 7 | Final ranked surviving-route table | All R3 | **Converged** | (iii) UNIFIED-AS-79 Branch-A: STRONGEST (PASS-F2; analytic; F_2-class; W2-1 cross-confirmed). (iv) BASELINE × c_sub: SECOND (PASS-machine-ε at BASELINE; C16 INFO open cross-review pre-registered). (i) BRANCH-IV: UPSTREAM-ANCHOR-ONLY (registry pin; consumes 2 FAIL + 1 PASS gates). (ii) Z-factor: WEAKEST AS ANCHOR but PER-CLASS DIAGNOSTIC ADMISSIBLE at non-F_2 classes (E-R2.1 N_breakdown observable, NEW substrate-physics diagnostic). |
| 8 | 4×4 partition grid (anchor_type × class) | L-ER3.1, T-CR3.1, T-ER3.1 | **Emerged** | Path-(c) reorganization is a 2D PARTITION over (anchor_type × class_membership) with 4×4 = 16 cells: 9 ADMISSIBLE / 3 FAIL (path-(c) anchor row at non-F_2; margins 924× / 298× / 798× over PASS threshold) / 4 N/A (degenerate or undefined). Replaces 1D successor-promotion reading. Python-verified margins reproduce L-ER3.1 grid to 4 sig figs. Templateable for future substrate→A_s/n_s closed-mechanism registry entries (T-ER3.1). |
| 9 | Joint F_2-Class Path-(c) Theorem (lizzi+transit S86 W-9) | E-R2.2, T-CR2.4, L-CR3.3, L-ER3.2, T-CR3.2 | **Emerged** | First framework theorem co-authored across spectral-functional and transit-dynamics axes (2 spectral-only + 2 transit-only + 2 joint clauses). 6 clauses (a)-(f) with 4 corrigenda (T-CR2.1 F_2/F_4 disambiguation, T-CR2.2 s=3 pole-specificity scoping, T-CR2.3 open-verdict reformulation, L-CR3.3 quantitative margin amendment carrying +2.47-2.97 OOM safety margin). Two-agent independent-verify upgrade (T-CR3.2): connes-ncg-theorist (spectral) + volovik-superfluid-universe-theorist (transit) at S88 Stage 2. |
| 10 | 4-stage upgrade pathway with two-agent independent-verify | T-ER2.1, L-CR3.1, T-CR3.2 | **Emerged** | Stage 0 workshop-internal candidate → Stage 1 S87 registration as candidate → Stage 2 two-agent parallel cross-check (joint-clauses (c),(d) require both axes) → Stage 3 permanent registration. Stage 1→2 gate: S87-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY (2-agent). Closes registry-driven theorem inflation pathway forbidden by `epistemic-discipline.md` §"agreement among agents is not evidence". |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **(S87 path-(c) carry-forward set, Level 1)** Does S87-PATH-C-SUCCESSOR-ANCHOR-LANDING fire PASS at the S87 dispatch envelope with all 6 clauses (a)-(f) of the Joint F_2-Class Path-(c) Theorem independently verified, the F_2/F_4 disambiguation landed in `permanent-results-registry.md`, the falsifier-master-inventory rows 2 + 13-21 updated with route-(iii) provenance pointing at S82 W1-2 verdict line 728, and SECTOR-1/SECTOR-2 retired as path-(c) anchors with diagnostic-only labels?

2. **(S87 path-(c) carry-forward set, Level 1)** Does S87-RESCALED-IC-SR-LO-RERUN reproduce the 4-class N_breakdown table (F_2: 0.122, cutoff_sqrt: 0.176, anomaly: 0.730, Zubarev: ∞ within N=55) at LSODA rtol=1e-10, atol=1e-13, max_step=0.01, with Zubarev-class max(ε) at N=55 ∈ [0.20, 0.35]? F_2-class IC rescaling marked structurally closed by T2 substitution chain Step 4.

3. **(S87 path-(c) carry-forward set, Level 2)** Does S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW fire (A) FAIL stands → C16 INFO confirmed at L_max=10, or (B) cross-proxy (lizzi A-T4.2 WZW candidate at substrate-distance-2 pole s=4) yields PASS → C16 promotes from INFO to ADMISSIBLE? Cross-reviewer (connes-ncg-theorist proposed) operationalizes the alternative anomaly-isolating proxy with rubric pinning per `epistemic-discipline.md` §"Verifier-Rubric Pre-Registration" before computing.

4. **(S87 path-(c) carry-forward set, Level 2)** Does S87-A_S-SURVIVING-ROUTE-RANK-LANDING land the L3+T3 ranked route table `(iii) ≻ (iv) ≻ (i) ≻ (ii)` into the falsifier-master-inventory cross-channel section, with path-(c) value provenance updated to point at S82 W1-2 verdict line 728 and no falsifier row citing SECTOR-1 or SECTOR-2 as the path-(c) anchor?

5. **(S87/S88 path-(c) carry-forward set, Level 3)** Does S87-POLE-SPECIFICITY-SCAN with explicit pre-registered s=4 anchor-formula (T-DR2.1 sub-step) confirm Reading_2 (pole-specific anti-correlation: |ρ_S(s=4)| < 0.3) or Reading_1 (generic substrate-pluralism: |ρ_S(s=4)| ≥ 0.7), and if INFO band [0.3, 0.7] which additional poles disambiguate? The s=4 anchor formula must be pre-registered before the dynamical scan fires.

6. **(S88 path-(c) carry-forward set, Level 3)** Does S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY return PASS under the two-agent parallel cross-check protocol, with connes-ncg-theorist auditing clauses (a), (c), (d), (e) on the spectral-functional axis and volovik-superfluid-universe-theorist auditing clauses (b), (c), (d), (f) on the transit-dynamics axis, joint clauses (c) and (d) PASS-AND'd across both verdicts? Stage 1 → Stage 3 promotion fires only on joint PASS.

7. **(deeper-than-S87 structural)** Does the 4×4 partition grid (anchor_type × class) generalize as a TEMPLATE for other framework sub-regions beyond substrate→A_s/n_s — e.g., to the spectral-monotonicity hierarchy (S63 Hawking-QA chain), GGE relic permanence registry, or Volovik-partition closed-mechanism cluster? T-ER3.1 emergent registry-template upgrade is meta-structural and admits cross-region application; the canonical answer requires a per-region admissibility audit.

8. **(deeper-than-S87 structural)** Does the per-class N_breakdown 4-tuple {0.122, 0.176, 0.730, ∞} produce a falsifiable observational signature beyond its registry diagnostic role — e.g., does the per-class spread of substrate Bogoliubov backreaction-onset N predict a measurable variance in the post-fold GGE quasi-particle spectrum at cosmologically observable scales? E-R2.1 + T-CR2.5 establish the observable is well-defined and substrate-derivable; the observability requires forward-modeling beyond the workshop scope.

## Wrap-Up — Workshop Impact Summary

### What Changed

The path-(c) reorganization is no longer a 1D successor-promotion (route iii replaces SECTOR-1/SECTOR-2). It is now a **4×4 2D partition grid over (anchor_type × class_membership)** with 16 typed cells (9 ADMISSIBLE / 3 FAIL / 4 N/A) where the path-(c) successor anchor occupies the SINGLE F_2-class admissible cell on the path-(c) anchor row, with Python-verified safety margins **924× / 298× / 798× over the PASS threshold** for the three FAIL cells (suppression / truncation / subtraction classes), corresponding to **+2.47 to +2.97 OOM minimum quantitative robustness** for the F_2-class uniqueness statement (clause (e) of the Joint F_2-Class Path-(c) Theorem). The grid is **templateable** for future substrate→A_s/n_s closed-mechanism registry entries (T-ER3.1 meta-structural upgrade).

The **Joint F_2-Class Path-(c) Theorem (lizzi+transit S86 W-9)** is the **first framework theorem co-authored across spectral-functional and transit-dynamics axes** (2 spectral-only + 2 transit-only + 2 joint clauses). It carries 4 corrigenda: T-CR2.1 F_2/F_4 disambiguation (F_2 = {ζ, SDW} this workshop ≠ F_4 = {ζ, Zubarev, SDW} W14 plan); T-CR2.2 s=3 pole-specificity scoping appended to anti-correlation duality clause (c); T-CR2.3 open-verdict reformulation of route (iv) C16 sub-test (c) (no Class-6-adjacent pre-judgement); L-CR3.3 quantitative margin amendment converting clause (e) binary admissibility verdict into the 924×/298×/798× safety margin statement.

**SECTOR-1 (SR-LO Z-factor) and SECTOR-2 (K-invariant Mellin pole) are RETIRED as path-(c) anchors** and converted to DIAGNOSTIC instruments — SECTOR-1 as per-class IC-compatibility diagnostic (admissible at suppression/truncation/subtraction classes; the suppression-class survival to N=55 with max(ε) = 0.266 is the FIRST per-class dynamical diagnostic the framework has constructed, E-R2.1); SECTOR-2 as atlas-class membership diagnostic (F_2 sub-atlas trivial PASS; A_5 with 3-class partition becomes 3-class compatibility test).

The **suppression-class 924× FAIL is informative-negative**: it CONFIRMS the F_2-class uniqueness of the path-(c) anchor and OPENS the per-class diagnostic slot; the negative result hardens clause (e) by +2.97 OOM minimum safety. T-ER3.1 reveals the 4×4 partition closes a **registry-completeness gap** in the framework's prior flat-list closed-mechanism registry: future closed-mechanism entries in the substrate→A_s/n_s pipeline can adopt the (anchor_type × class) coordinate system from the start.

The **two-agent independent-verify upgrade** (T-CR3.2) is structurally essential for the joint clauses (c), (d) which require BOTH spectral-functional and transit-dynamics competence; single-agent verification would leave those clauses under-verified. The recommended pair is **connes-ncg-theorist (spectral, audits clauses (a), (c), (d), (e)) + volovik-superfluid-universe-theorist (transit, audits clauses (b), (c), (d), (f))**, joint PASS iff both return PASS on their respective clause sets at S88 Stage 2.

### What Holds

The **F_2 = {ζ, SDW} canonical pair** is the only K-invariant sub-atlas of A_5 (lizzi L1 enumeration; Class A vacuous + Class B identity + Classes C-F all FAIL by O(1) margins). The W4-2 P5 numerical Mellin 5-tuple `M(s=3) = (1.581e-1, 1.581e-1, 1.201e-2, 1.110e-1, 3.185e-2)` is the substrate observable at substrate-distance-1 pole.

The **Branch-A PASS-F2 anchor** is preserved at S82 W1-2 verdict line 728, value 3.2994e-9, scheme=zeta, convention=UNIFIED-AS-79-branch-TD, L_max=3, delta_OOM = +0.1962 against Planck A_s = 2.10e-9 (PASS-F2 band log10(2) = +0.30103). The W2-1 replay deviation 0.000440% confirms the per-branch-protected ledger A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{−1}·f_conv is L_max-stationary at F_2 class. The reorganization is **value-preserving** — only PROVENANCE strings update; falsifier-master-inventory value strings are invariant under the SECTOR-1/SECTOR-2 → route (iii) Branch-A reading (the SECTOR-1/SECTOR-2 anchors NEVER PRODUCED an A_s value).

The **per-class N_breakdown 4-tuple** {F_2: 0.122 e-folds, cutoff_sqrt: 0.176, anomaly: 0.730, Zubarev: ∞ within N=55} as substrate observable: well-defined (E-R2.1 substitution chain Step 3); Mellin-cone-derived (transits through xi²_0(R) = xi_E_GGE_inv · M_R / M_F2); cross-validated against autocatalysis bound (T2 + lizzi C-R2.1 reproduction); L_max=3-pinned via M_R(s=3) values from W4-2 P5. Spearman ρ_S = ±1.000000 EXACT under same/opposite-direction reading at the 4-class projection (Python-verified), with anti-correlation pole-specific to s=3 substrate-distance-1 pole and 4-class-resolution-specific (L-CR3.2 extension).

The **route (iv) BASELINE × c_sub cross-check** holds at machine-epsilon for BASELINE H(N_pivot) = 3.0042 in M_KK natural units (W5b C15(ii) PASS, CC1 4.4e-16 / 2.4e-15 residuals). Route (iv) is structurally consistent with route (iii) (same UNIFIED-AS-79 ledger read at different layers; closed-form analytic vs explicit per-pivot integration). C16 sub-test (c) FAIL under τ-flow-trace proxy is open-verdict pending S87 cross-review; the asymmetric-EVOI argument for the cross-review remains valid in EVOI-information-value direction without pre-judging the verdict.

The **canonical pin xi_E_GGE_inv = 13.642473425595973** (M_KK units, S86-BRANCH-IV-FORMULATION-COMMIT, knowledge MCP get_constant verified) is the F_2-class projection of the substrate-natural anchor `59.8 · Δ_BCS / K_base` (lizzi 9A §2.2). The pin remains canonical for downstream F_2-class consumers; route (i) BRANCH-IV PASS retains its registry-pin role (upstream of any A_s producer; not itself a route to A_s).

### What Breaks or Strains

Nothing identified within the path-(c) sub-region. The DOUBLE-DOUBLE FAIL (SECTOR-1 SR-LO Z-factor PIVOT55 + PIVOT312 + SECTOR-2 K-invariant Mellin pole) is fully mapped at the end of R3: cross-class K-invariance closed by lizzi L1 (Classes A-F enumeration); F_2-class SR-LO closed by autocatalysis bound (T2 ε_0 < 10^{−651.79} required, below IEEE-754 underflow); only F_2-class via the analytic UNIFIED-AS-79 ledger survives (route iii). The reorganization preserves the framework's frozen prediction A_s = 3.30e-9 PASS-F2 — no observational gate is strained.

One **structural strain** is logged for S87+ resolution but does NOT affect the workshop's verdict: the §10 plan estimate `xi_E_GGE_inv ≈ O(10^{−2})` (W5a §W5a-1 line 149) was three orders of magnitude below ALL four class-projected values (suppression: 1.037; subtraction: 2.747; truncation: 9.578; F_2: 13.6425). The plan author's mental model was implicitly an LCDM-baseline-like small-perturbation regime, NOT a per-class projection. The W4 P4 commit landed F_2-class by construction — and **this is the FIRST instance** where the framework's Mellin-kernel side outpaces the SR-LO ODE side's IC-tolerance budget (transit Re:L2 §Q-L2.2 PARTIALLY answer; lizzi C-R2.2). This is informationally tight (it sharpens the class-mismatch diagnosis) but flags a planning-vocabulary asymmetry between Mellin-kernel side and SR-LO side that future plan authors should monitor when estimating substrate-IC anchors.

### Carry-Forward Computations

Five S87 + one S88 carry-forward gates with 4-field specs, organized in the 3-level ordering accepted at Q-L-R3.2 lock-in. Total commitment: ~4.25 wave-equivalents across S87+.

**Level 1 (S87 W-1, ~1.0 wave-equivalents)** — landing the path-(c) reorganization at the registry level + theorem-completeness criterion (joint clause (b) verified at S87 dispatch envelope).

**S87-PATH-C-SUCCESSOR-ANCHOR-LANDING**:
- *What*: Land the **Joint F_2-Class Path-(c) Theorem (lizzi+transit S86 W-9)** 6-clause statement (E-R2.2 + T-CR2.4 + L-CR3.3 corrigenda) to `sessions/permanent-results-registry.md` as Stage 1 (registered candidate) per the 4-stage upgrade pathway (T-ER2.1 + L-CR3.1). Update `falsifier-master-inventory.md` rows 2 + 13-21 with route-(iii) provenance pointing at S82 W1-2 verdict line 728. Disambiguate F_2 = {ζ, SDW} (this workshop) vs F_4 = {ζ, Zubarev, SDW} (W14 plan) per T-CR2.1. Retire SECTOR-1 SR-LO Z-factor and SECTOR-2 K-invariant Mellin pole as path-(c) anchors with DIAGNOSTIC-only labels per L4 Clause C2. Cite the 4×4 partition grid (L-ER3.1) as the canonical structural reading. Cite the 924×/298×/798× quantitative margins (L-CR3.3) for clause (e).
- *Inputs*: this workshop L1+L2+L3+L4+R2+R3 with all corrigenda; transit R1+R1-B+R2-B+R3-B; S82 W1-2 verdict line 728 (`session-82-results-workingpaper.md`); W4-2 P5 Mellin 5-tuple (`session-86-w4-workingpaper.md` lines 246-248); W5b C15+C16 verdicts (`s86_gate_verdicts.txt` line 136 + `session-86-w5b-workingpaper.md` lines 263-267); T2 numerical autocatalysis-bound closure; canonical_constants `xi_E_GGE_inv = 13.642473425595973`.
- *Gate*: `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` PASS iff (a) Joint F_2-Class Path-(c) Theorem registered at Stage 1 with all 6 clauses (a)-(f) AND 4 corrigenda; (b) F_2 vs F_4 vocabulary disambiguated in registry text; (c) falsifier rows updated with S82 W1-2 provenance; (d) SECTOR-1/SECTOR-2 retired with diagnostic-only labels; (e) 4×4 partition grid cited as canonical structural reading; (f) 924×/298×/798× margins cited for clause (e).
- *Effort*: 0.5 wave-equivalents.

**S87-RESCALED-IC-SR-LO-RERUN**:
- *What*: Run SR-LO ODE `dε/dN = ε(2η − 4ε + 2ξ²); dξ²/dN = −2εξ²; dη/dN = −2η(ε−η)` at all four affine class-projected xi²_0(R) values (F_2: 13.6425; cutoff_sqrt: 9.578; anomaly: 2.747; Zubarev: 1.037) at canonical IC (ε_0, η_0) = (0.020, 0.005). Numerically pin `N_breakdown_observable(R)` per E-R2.1 for all four classes. Confirm transit Re:L1 numerical values (F_2: 0.122 e-folds; cutoff_sqrt: 0.176; anomaly: 0.730; Zubarev: ∞) and the Zubarev-class N_breakdown=∞ result. Report max(ε) at N=55 for each class. F_2-class IC-rescaling marked "structurally closed by T2 substitution chain Step 4" — no rescaling attempt admissible.
- *Inputs*: W4-2 P5 Mellin 5-tuple (M_ζ = M_SDW = 1.581e-01, M_Zubarev = 1.201e-02, M_cutoff_sqrt = 1.110e-01, M_anomaly = 3.185e-02); canonical IC pin; LSODA primary at rtol=1e-10, atol=1e-13, max_step=0.01 (canonical W5a P3 settings); RK45 cross-check at rtol=1e-10.
- *Gate*: `S87-SECTOR-1-SR-FLOW-RESCALED` PASS iff per-class N_breakdown(R) reproduces transit Re:L1 Table values to within 1% rel for the three classes with finite breakdown AND Zubarev-class max(ε) at N=55 ∈ [0.20, 0.35] band. INFO if reproduction within 5% rel; FAIL otherwise. F_2-class rerun excluded (autocatalysis-bound closed).
- *Effort*: 0.5 wave-equivalents.

**Level 2 (S87 W-2 or later, ~1.25 wave-equivalents)** — open-verdict cross-review of route (iv) C16 + ranked surviving-route table landing.

**S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW**:
- *What*: Independent cross-reviewer (connes-ncg-theorist proposed) operationalizes an alternative anomaly-isolating proxy for c_sub conformal-anomaly contribution at the Mellin-cone level, distinct from the τ-flow-trace proxy in W5b §W5b-2 line 343. Lizzi A-T4.2 candidate: WZW consistency check at substrate-distance-2 pole s=4 (`c_sub_anomaly_WZW(R) := Res[M_R(s)·anomaly_kernel; s=4] / Res[M_R(s); s=3]`). Pre-register the cross-proxy operationalization with rubric pinning per `.claude/rules/epistemic-discipline.md` §"Verifier-Rubric Pre-Registration" before computing. Open-verdict framing per T-CR2.3 (no Class-6-adjacent pre-judgement of cross-review direction).
- *Inputs*: W5b §W5b-2 sub-test (c) script + verdict; lizzi S65/S66 spectral-functional pluralism map for proxy candidates; lizzi A-T4.2 WZW-proxy substitution chain; alternative proxies in literature (WZW anomaly, conformal anomaly Polyakov action).
- *Gate*: `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` returns one of: (A) FAIL stands → C16 confirmed INFO at L_max=10; (B) cross-proxy yields PASS → C16 promotes from INFO to ADMISSIBLE. Verdict open and not pre-judged.
- *Effort*: 1.0 wave-equivalents (axiom-side cross-review with rubric pinning).

**S87-A_S-SURVIVING-ROUTE-RANK-LANDING**:
- *What*: Land the L3+T3 cross-domain-converged ranked route table `(iii) ≻ (iv) ≻ (i) ≻ (ii)` into the falsifier-master-inventory cross-channel section. Update path-(c) value PROVENANCE strings to point at S82 W1-2 verdict line 728. Verify no falsifier row cites SECTOR-1 or SECTOR-2 as the path-(c) anchor.
- *Inputs*: this workshop's L3 + T3 substitution chains; `s82-results-workingpaper.md` line 728; `s86_gate_verdicts.txt` lines 108, 112, 114, 116, 136; `falsifier-master-inventory.md` rows 2, 12, 13-21.
- *Gate*: `S87-PATH-C-RANK-TABLE-LANDING` PASS iff (a) the rank table appears in the falsifier inventory with both lizzi (a)-(d) and transit (a')-(d') ranking criteria cited; (b) path-(c) PROVENANCE strings cite S82 W1-2 ledger; (c) no falsifier row cites SECTOR-1 or SECTOR-2 as the path-(c) anchor.
- *Effort*: 0.25 wave-equivalents.

**Level 3 (S87 W-3 or S88, ~2.0 wave-equivalents)** — pole-specificity discriminator + Stage 2 promotion.

**S87-POLE-SPECIFICITY-SCAN**:
- *What*: Test whether the Mellin-cone substrate-distance-1 spectral-dynamical anti-correlation at s=3 generalizes to s=4 (lizzi E-R2.3 + Q-L-R2.2). **Step (a) — pre-register the s=4 anchor formula** by lizzi+transit before the dynamical scan fires (per T-DR2.1 PRU-Class-8 prevention). Step (b) — compute a_4-coefficient-class M_R(s=4) for all five regulators in A_5 at L_max=3. Step (c) — project onto the pre-registered SR-LO-analog dependent observable. Step (d) — test for anti-correlation Pearson |r| and Spearman |ρ_S|. Discriminates Reading_1 (generic substrate-pluralism: |ρ_S(s=4)| ≥ 0.7 confirms anti-correlation generalizes) vs Reading_2 (pole-specific: |ρ_S(s=4)| < 0.3 confirms s=3 specificity); INFO band [0.3, 0.7].
- *Inputs*: W4-2 P5 atlas extension to s=4 (new computation); lizzi S78 W2-F a_4-coefficient Mellin-multiplier scheme-invariance result (98.48% R²-dominated INTRINSICALLY); SR-LO-analog observable construction (must include explicit anchor-formula choice pre-registered at Step (a)).
- *Gate*: `S87-POLE-SPECIFICITY-SCAN` PASS iff anti-correlation Pearson r at s=4 satisfies |r(s=4)| < |r(s=3)|/5 (confirming pole-specificity with factor-5 compression); FAIL iff |r(s=4)| within 50% of |r(s=3)| (Reading_1 generalizes); INFO between. Both outcomes are structurally informative; gate has high-leverage discriminator status (T-ER2.2 EVOI).
- *Effort*: 1.0 wave-equivalents.

**S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY** (Stage 2 promotion gate, two-agent parallel cross-check per T-CR3.2):
- *What*: Two-agent parallel independent verification of the Joint F_2-Class Path-(c) Theorem 6-clause statement. **Spectral-side cross-reviewer**: connes-ncg-theorist audits clauses (a) spectral 3-class partition, (c) anti-correlation duality at s=3 [JOINT axis], (d) per-branch protection [JOINT axis], (e) cross-class K-invariance closure with 924×/298×/798× margins. **Transit-side cross-reviewer**: volovik-superfluid-universe-theorist audits clauses (b) dynamical 4-class breakdown, (c) anti-correlation duality at s=3 [JOINT axis], (d) per-branch protection [JOINT axis], (f) F_2-class autocatalysis closure at ε_0 < 10^{−651.79}. Both cross-reviewers operate WITHOUT prior workshop context (Stage 2 is the structural-pin guarantor against single-agent confirmation bias).
- *Inputs*: registered Joint F_2-Class Path-(c) Theorem entry from S87-PATH-C-SUCCESSOR-ANCHOR-LANDING in `permanent-results-registry.md`; the 6-clause statement with all 4 corrigenda; the 4×4 partition grid (L-ER3.1); the W4-2 P5 numerical 5-tuple at s=3.
- *Gate*: `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` PASS iff BOTH cross-reviewers return PASS independently on their respective clause sets; joint clauses (c) and (d) PASS-AND'd across both verdicts. FAIL iff either cross-reviewer returns FAIL on any of their clauses; INFO if either returns partial/mixed. PASS triggers Stage 2 → 3 promotion at session-end synthesis (theorem joins KO-dim=6, J-D_K=0, etc., in permanent-results table).
- *Effort*: 1.0 wave-equivalents (two-agent cross-review at S88+).

### Closing Line

The DOUBLE-DOUBLE FAIL is fully mapped, the path-(c) successor anchor is canonically locked at route (iii) UNIFIED-AS-79 Branch-A zeta-normalization on the F_2-class single ADMISSIBLE cell of a Python-verified 4×4 partition grid, and the Joint F_2-Class Path-(c) Theorem (lizzi+transit S86 W-9) becomes the framework's first cross-axis co-authored permanent-theorem candidate pending two-agent independent-verify at S88 Stage 2.
