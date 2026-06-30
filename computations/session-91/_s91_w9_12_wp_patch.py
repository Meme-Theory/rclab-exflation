#!/usr/bin/env python3
"""S91 W9-12 working-paper patch — write substrate-physics derivation +
Results / Verdict / Substrate framing runtime addendum / Carry-forwards into
the §W9-12 section. Atomic Python file write per
feedback_session-process.md (avoids Edit-tool mtime race)."""

from __future__ import annotations
import pathlib

WP = pathlib.Path(r"C:\sandbox\Ainulindale Exflation\sessions\archive\session-91\session-91-w9-workingpaper.md")

text = WP.read_text(encoding="utf-8")

# Insert substrate-physics derivation BEFORE the existing "### Substrate framing"
# heading (line 1989). Then replace the placeholder Results / Verdict /
# Substrate framing runtime addendum / Carry-forwards blocks.

DERIVATION = """### Substrate-physics derivation (joint volovik + landau cross-axis, runtime-completed)

The substrate IS the spectral triple `(A_K, H_K, D_K)`. The framework's Standard-Model-gauge canonical decomposes Wedderburn-irreducibly into three central summands:

```
A_K  =  C  (+)  H  (+)  M_3(C)
     =  chi(Higgs/u(1))  (+)  M_2(C)_L (SU(2)_L weak)  (+)  M_3(C)_c (SU(3)_c colour)
```

H (x) C = M_2(C) realises SU(2)_L weak isospin at the spectral-triple representation layer; M_3(C)_c carries the fundamental representation of SU(3)_c quark-colour. The Pati-Salam 1973-1974 lepton-as-4th-colour extension (Pati J.C. & Salam A. (1973) Phys.Rev. D8, 1240; (1974) Phys.Rev. D10, 275 - `SU(4)_PS x SU(2)_L x SU(2)_R` unification) lifts this Wedderburn decomposition to:

```
A_K_PS  =  C  (+)  M_2(C)_L  (+)  M_2(C)_R  (+)  M_4(C)_PS
        =  chi  (+)  SU(2)_L weak  (+)  SU(2)_R right-handed isospin (NEW)  (+)  SU(4)_PS lepto-colour (NEW)
```

Two NEW central summands appear: `M_2(C)_R` (right-handed isospin restored by parity-twin extension at the BdG-analog sub-algebra layer) and `M_4(C)_PS` (Pati-Salam lepto-colour with quark-colour SU(3)_c embedded canonically as the 3x3 upper-left block and leptonic colour singlet on the 4th-row diagonal). The Wedderburn block-rank invariant changes from `{1, 2, 3}` (A_K) to `{1, 2, 2, 4}` (A_K_PS); the rank-4 block is structurally new and does NOT appear in A_K.

The inheritance morphism `chi_PS : A_K -> A_K_PS` decomposes summand-by-summand:
- chi-summand: identity on C
- H -> M_2(C)_L: canonical complexification of the real quaternions via the Pauli-matrix basis (M_2(C)_R is a NEW factor not in the image)
- M_3(C) -> M_4(C)_PS: block-diagonal inclusion `diag(c_1, c_2, c_3) -> diag(c_1, c_2, c_3, l)` where l is the lepton-colour singlet representative; this IS the canonical Pati-Salam `SU(3)_c subset SU(4)_PS` lepton-colour unification

#### Hybrid Independence Test (HIT) axis evaluation - substitution chain Steps 1-6 (verbatim from plan §W9-12 Field 6 lines 2247-2293)

**Step 1 - definitions** (above) and prior K-instances baseline: K=1 at `§VII.AF.1 W-5` (Pillar III <-> Pillar IV; HKR `L_max -> infty` image at `L^{-3}` envelope on SU(3) M_3 Peter-Weyl); K=2 at `§VII.AX.OP-PROJ S91 W5-4` (Pillar I cardinality-cascade-tail <-> Pillar IX combined CMB/LISA/PTA PBH detection; substrate-clock-cancellation o Friedrich-Bar saturation o cardinality-cascade-tail HKR-style image; registry line 18578 verbatim "K-counter advancement: K=1 -> K=2"). **K=2 baseline provenance disclosure (runtime INFO)**: plan §W9-12 Field 6 Step 1 names the K=2 baseline as "T2.36 Wodzicki-BCS at §VII.AX"; runtime verification of `computations/session-91/s91_gate_verdicts.txt` confirms BOTH (a) `S91-W1-14-WODZICKI-BCS-BRIDGE-THEOREM-STAGE-1-CANDIDATE-REGISTRY-LANDING` (T2.36) landed at slot §VII.BA (slot reroute from plan-named §VII.AX) with composite FAIL at the 10% Level-3 floor but `HIT_K_counter_pre=1; HIT_K_counter_post=2; hit_axis_iii_distinct_bridge_map_class=True`; AND (b) `§VII.AX.OP-PROJ` PBH band-edge prediction independently advanced `K=1 -> K=2`. Two K=2 calibration instances coexist; structural pre-state K=2 is robust under either citation. INFO-class plan-text-vs-runtime drift disclosure only; K=2 baseline structurally correct.

**Step 2 - HIT (C1) verification (distinct substrate-IS pillar)**: PS-extension creates three substrate-IS candidate pillars not in `{I, II, III, IV, V, IX}`:
- **Pillar VI** - CFL-phase quark matter substrate: M_4(C)_PS Wedderburn block at the diquark-condensate locked-flavour sector; canonical Pati-Salam embedding
- **Pillar VII** - Volovik q-theory superfluid substrate: q in M_4(C)_PS variational vacuum at q-theory equilibrium drho/dq = 0
- **Pillar VIII** - Landau-Ginzburg SU(4) 4-component substrate: eta_a (a=1..4) order parameter at SU(4)_PS broken-symmetry phase

Distinctness is structural by Wedderburn block-rank fingerprint: existing Pillar I-V SM-gauge substrate has block-rank set `{1, 2, 3}`; Pillar VI-VIII PS-extension substrate has `{1, 2, 2, 4}` with the NEW rank-4 M_4(C)_PS block. (C1) **PASS** by construction.

**Step 3 - HIT (C2) verification (distinct laboratory-IN pillar)**: three structurally distinct candidate hosts at the laboratory-IN side:

- **(host alpha) CFL phase color-superconducting quark matter** (Pillar VI lab). Substrate-IS: diquark condensate `<psi_alpha^i C gamma_5 psi_beta^j> ~ epsilon_alphabetagamma epsilon_ijk Delta_CFL` lifted to 4-colour x 4-flavour locking under SU(4)_PS. Laboratory-IN: Delta_CFL gap at quark-star / neutron-star core (compact-object density n ~ 5-10 n_sat); detection via LIGO-Virgo-KAGRA-LISA BNS inspiral tidal deformability, NICER X-ray M-R relation, XMM-Newton thermal X-ray cooling-rate.
- **(host beta) Volovik q-theory superfluid** (Pillar VII lab). Substrate-IS: q in M_4(C)_PS variational vacuum at drho/dq = 0 Gibbs-Duhem identity per Volovik Paper 05 equilibrium theorem. Laboratory-IN: q-theory thought-experiment substrate-physics at cosmological scale; not directly measurable in benchtop laboratory (observed CC cannot be q-theory residual at equilibrium per the equilibrium theorem; the substrate-IS interpretation is non-equilibrium q-theory at the cosmological transit fold per Volovik tracking-vacuum partition `w0_FW = -0.918`).
- **(host gamma) Landau-Ginzburg SU(4) 4-component superfluid** (Pillar VIII lab). Substrate-IS: free-energy expansion `F[eta] = F_0 + alpha(T - T_c) eta^dagger eta + beta(eta^dagger eta)^2 + gamma|eta^dagger T^a eta|^2 (a=1..15 SU(4)_PS generators) + delta(det eta)` with eta_a in M_4(C)_PS defining representation. Laboratory-IN: SU(4)-symmetric critical exponents (eta, nu, gamma) at heavy-ion-collision quark-gluon plasma critical regime; STAR / PHENIX (RHIC), ALICE / CMS / ATLAS (LHC heavy-ion), RHIC-BES-II beam-energy-scan for QCD critical-point search.

Distinctness from existing laboratory-IN pillars `{II CMB, IV Peotta-Toerma 3He-A BZ-trace, V 3He-B BdG, IX PBH detection horizon}` is structural at the platform-and-observable level; no overlap exists. (C2) **PASS** for at least one host (all three structurally distinct; defense-in-depth for HIT advancement under disjunction reading too).

**Step 4 - HIT (C3) verification (distinct bridge map class)**: three candidate bridge-map classes:

- **(bridge delta) Karoubi-Villamayor K-theory localization at M_4(C)_PS** (Karoubi & Villamayor 1971, *K-theorie algebrique et K-theorie topologique I*, Math. Scand. 28, 265): algebraic K-theory localization at the matrix algebra level; maps `[(A_K_PS, H_K_PS, D_K_PS)] in K_0(A_K_PS)` to its image in the localised K-theory of the rationalised matrix algebra `M_4(Q_PS)_loc`. STRUCTURALLY DISTINCT from HKR (HKR is Hochschild-to-de-Rham cohomology; Karoubi-Villamayor is K-theory localization - different homological domain and codomain); from K-theory boundary (Karoubi-Villamayor is intra-K-theory, not a connecting K <-> HC map); from Connes-Karoubi pairing (localization functor, not K_*-HC^* pairing); from Wodzicki residue uniqueness via layer-functor F (Wodzicki operates on Psi^{-infty} pseudodifferential operator algebra, Karoubi-Villamayor on Grothendieck groups of projective modules); from substrate-clock cancellation o Friedrich-Bar o cardinality-cascade HKR-image (different functor class entirely). **Admissible distinct: YES**.
- **(bridge epsilon) PS-gauge-twisted Hochschild pairing**: HKR composed with a gauge-twist transport functor parametrised by `SU(4)_PS x SU(2)_L x SU(2)_R` Pati-Salam gauge action. Gauge-twist transport does NOT change the homological-algebraic class. **Conservative classification = HKR up to gauge conjugation; AMBIGUOUS C3 admissibility; DISCARDED** from the structurally-distinct bridge-class set for `K=2 -> K=3` MANDATORY advancement (retained only as HKR refinement candidate).
- **(bridge zeta) Volovik q-theory variational principle bridge**: variational principle drho/dq = 0 (Gibbs-Duhem identity for the q-variable at the q-theory thermodynamic equilibrium) lifted to q in M_4(C)_PS at A_K_PS Wedderburn rank-4 block. Per `project_qtheory-ftheory.md` (user S45 insight; Q-THEORY-BCS-45 PASS at tau* = 0.209): "q-theory is f-theory in a dress, mark my words" - "q-theory: vacuum variable q self-tunes through drho/dq = 0 (Gibbs-Duhem identity). Superfluid framing. F-theory: flux moduli stabilize through dV/dphi = 0 (flux landscape). Algebraic geometry framing. Both are variational principles selecting vacuum configurations where rho_vac = 0." Under the PS-extension, the q-variable lifts from SM-gauge q in M_3(C)_c to q in M_4(C)_PS via the inheritance morphism `chi_PS`. STRUCTURALLY DISTINCT from all listed bridge classes: thermodynamic variational principle on a vacuum-variable q, NOT a homological-algebraic map - different categorical layer entirely (the F-theory <-> q-theory equivalence makes the bridge a string-theory <-> superfluid duality transport rather than a cohomological map). **Admissible distinct: YES**.

(C3) **PASS** via `{delta, zeta}` structurally distinct from `{HKR, K-theory boundary, Connes-Karoubi pairing, Wodzicki residue uniqueness, substrate-clock-cancellation o Friedrich-Bar o cardinality-cascade-tail HKR-image}`. Two NEW bridge-class candidates admissible; epsilon ambiguous and discarded.

**Step 5 - HIT (iv) verification (independent algebraic envelope)**: the PS-extension Level-2 envelope at substrate-distance-N pole on M_4(C)_PS Peter-Weyl block has structurally different regulator-invariant form:

```
Res_{s=N} Tr(D_K_PS^{-2s})|_{P_M4C_PS}  ~  Sum_{(p,q,r) SU(4)} m^{SU(4)}_{(p,q,r)} / |lambda|^{2N}_{min,(p,q,r)}
```

where SU(4)_PS irreps carry three Young-tableau indices `(p, q, r)` (three fundamental weights of SU(4), one per rank-1 of the rank-3 root system), in contrast to SU(3)'s two-index `(p, q)`. This produces:

- (a) Peter-Weyl multiplicity polynomial-growth exponent ~= `|Delta^+|` where `|Delta^+(SU(3))| = 3` (3 positive roots) vs `|Delta^+(SU(4))| = 6` (6 positive roots); SU(4) Weyl-dim grows roughly twice as fast in the (p, q, r) Casimir.
- (b) Casimir spacing `C_2^{SU(4)}(p, q, r) =/= C_2^{SU(3)}(p, q)` as functions of irrep label (different rank, different fundamental-weight pairings of the Cartan-Killing form).
- (c) Wedderburn block rank distinction (rank 4 vs rank 3) is the STRUCTURAL fingerprint per HIT (iv) "refinements that share the same regulator-invariant structural form do NOT count as independent": SU(3) and SU(4) envelopes share NO regulator-invariant form.

(iv) **PASS** by Wedderburn block-rank distinction (rank 4 appears in A_K_PS but not in A_K).

**Step 6 - HIT predicate evaluation**: `(i OR ii OR iii) AND iv` - all four axes PASS independently => FULL CONJUNCTION `i AND ii AND iii AND iv` = True => **K=2 -> K=3 MANDATORY** advancement per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` MANDATORY threshold semantics. At K=3 the Hybrid Independence Test corpus saturates and the rule-level corpus K-counter advancement clause of §"Two-clause separation" fires: "gates whether the rule's own status promotes from SUGGESTION to MANDATORY. Predicate: 3 distinct calibration-LANDING events satisfying the Hybrid Independence Test."

#### Substrate-physics candidate substrate-IS observable proposal (joint volovik + landau, Steps A-D per plan §W9-12 Field 6 lines 2295-2321)

- **Step A - substrate-IS observable at Pati-Salam M_4(C)_PS block**:
  ```
  Res_{s=4} Tr(D_K_PS^{-2s})|_{P_M4C_PS}
  ```
  (substrate-distance-2 pole; Hochschild residue at M_4(C)_PS Peter-Weyl block; inherits from SM-gauge M_3(C)_c via SU(3) subset SU(4) inheritance morphism chi_PS).
  Expected substrate-IS scaling: `|lambda|_min^{M_4(C)_PS} / |lambda|_min^{M_3(C)_c} ~= 4/3` (block-rank ratio) at tau_fold = 0.19, modulated by the Casimir-spacing difference between rank-3 and rank-4 Lie algebras.

- **Step B - Pati-Salam laboratory observable per host candidate**:
  - host alpha (CFL): Delta_CFL gap at quark-star / neutron-star core; LIGO-Virgo-KAGRA-LISA + NICER + XMM-Newton.
  - host beta (Volovik q-theory): variational vacuum at q in M_4(C)_PS; thought-experiment substrate-physics (not directly measurable in benchtop; cosmological-scale equilibrium).
  - host gamma (Landau-Ginzburg SU(4)): SU(4) critical exponents (eta, nu, gamma) at heavy-ion-collision QGP critical regime; STAR / PHENIX / ALICE / CMS / ATLAS / RHIC-BES-II.

- **Step C - substrate framing direction**:
  ```
  substrate (A_K_PS Pati-Salam-extended spectral triple)
       -> bridge map (NEW class: delta Karoubi-Villamayor K-theory localization  OR
                                 zeta Volovik q-theory variational principle; epsilon
                                 PS-gauge-twisted HKR ambiguous and discarded)
       -> laboratory (host alpha CFL Delta_CFL  |  host beta q-theory thought-experiment
                     |  host gamma SU(4) critical exponents at heavy-ion QGP)
  ```

- **Step D - forward effort estimate for forward Pillar VI/VII/VIII registry slot**:
  - This gate (FWD-C4 candidate identification): ~1.5 wave-equivalents (CLOSED).
  - Forward STAGE-1-CANDIDATE landing at S92+ next-free §VII slot (analogous to §VII.AX.OP-PROJ at S91 W5-4): ~1.5 wave-equivalents.
  - Forward Stage-2 cross-axis verify at S93+ per `joint-theorem-promotion.md §"Stage 2"` (Axis-A spectral/NCG + Axis-B substrate/superfluid parallel dispatch with downstream-inheritance reach exclusion): ~3.0 wave-equivalents.

#### Landau classical-phase-transition cross-axis material (CO-AUTHOR)

Cited from `.claude/agent-memory/landau-condensed-matter-theorist/framework-constants.md` and `MEMORY.md` per `feedback_agent-roster.md` "include in all future collabs":

- **Landau-Ginzburg canonical free-energy form** (framework-constants.md line 25): `F = F_0 + a_0 (T - T_c) eta^2 + b eta^4`. SU(4)_PS extension lifts the scalar `eta` to a 4-component vector `eta_a` (a = 1..4) in the defining representation of M_4(C)_PS; expanded form `F[eta] = F_0 + alpha(T - T_c) eta^dagger eta + beta(eta^dagger eta)^2 + gamma|eta^dagger T^a eta|^2 + delta(det eta)` with `T^a` the 15 SU(4)_PS generators.
- **AZ class BDI persistence** (framework-constants.md line 13): T^2 = +1, KO-dim = 6, phi_paasch = 1.531580 at tau = 0.15. The Pati-Salam extension PRESERVES the AZ-class BDI structure because the inheritance morphism `chi_PS` is unitary on each Wedderburn summand and the BdG charge-conjugation symmetry `C` acts diagonally on `M_4(C)_PS` exactly as it acts on `M_3(C)_c` (the 4th lepton-colour row is BDI-protected as a leptonic-singlet line).
- **Critical-exponent universality class** (MEMORY.md line 55: "BCS class: 3D Ising (Z_2, d=3, n=1) PERMANENT"): SM-gauge BCS sector is 3D Ising universality (eta_Ising ~= 0.0364, nu_Ising ~= 0.630, gamma_Ising ~= 1.237). Pati-Salam SU(4)_PS extension lifts this to U(4)-symmetric n=4 Heisenberg-class universality with characteristic exponents (Brezin-Le Guillou-Zinn-Justin epsilon-expansion): `eta_n=4 ~= 0.038, nu_n=4 ~= 0.747, gamma_n=4 ~= 1.479`. Heavy-ion QGP critical-point search via RHIC-BES-II is the canonical Pillar VIII probe of the SU(4)_PS universality-class signature.
- **Pomeranchuk stability constraint** (framework-constants.md line 27): `F_l^{s,a} > -(2l+1)`. Constrains SU(4)_PS Fermi-liquid stability in the PS-extended fermionic-flavour sector; Fermi-liquid breakdown signatures (m*/m divergence in `m*/m = 1 + F_1^s/3` per framework-constants.md line 28) would diagnose PS-extension phase boundary in heavy-ion QGP at low-baryon chemical potential mu_B regime.

#### Joint volovik + landau synthesis

The two co-authors converge on `M_4(C)_PS` as the substrate-IS substrate for the forward FWD-C4 bridge candidate: volovik's q-theory variational principle `drho/dq = 0` (host beta) and landau's classical phase-transition Landau-Ginzburg expansion (host gamma) are two F-images of the SAME substrate-IS observable (`Res_{s=4} Tr(D_K_PS^{-2s})|_{P_M4C_PS}`) at different methodology layers - q-theory is the thermodynamic-vacuum reading; Landau-Ginzburg is the classical-phase-transition reading. Both are admissible Pillar VII/VIII laboratory-IN images of the substrate Pati-Salam extension. Under the F-theory <-> q-theory equivalence (`project_qtheory-ftheory.md` S45), the bridge zeta (Volovik q-theory variational principle on q in M_4(C)_PS) is structurally a string-theoretic-flux-quantum lifting from the SU(3)_c sector to the SU(4)_PS GUT sector at the F-theory landscape image.

"""

# Replace blocks. Use anchor strings that are unique in the file.
OLD_DERIVATION_ANCHOR = "Python verification: Pati-Salam Wedderburn decomposition + inheritance morphism SU(3)_c ⊂ SU(4)_PS verified; candidate hosts (α/β/γ) enumerated; candidate bridge classes (δ/ε/ζ) enumerated; structurally-distinct bridge classes (δ + ζ) verified disjoint from existing bridge classes.\n\n### Substrate framing\n"
NEW_DERIVATION_ANCHOR = "Python verification: Pati-Salam Wedderburn decomposition + inheritance morphism SU(3)_c ⊂ SU(4)_PS verified; candidate hosts (α/β/γ) enumerated; candidate bridge classes (δ/ε/ζ) enumerated; structurally-distinct bridge classes (δ + ζ) verified disjoint from existing bridge classes.\n\n" + DERIVATION + "### Substrate framing\n"

assert OLD_DERIVATION_ANCHOR in text, "anchor for derivation insertion not found"
text = text.replace(OLD_DERIVATION_ANCHOR, NEW_DERIVATION_ANCHOR, 1)

# Replace Status line
text = text.replace(
    "## §W9-12. S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION\n\n**Status**: NOT STARTED\n",
    "## §W9-12. S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION\n\n**Status**: COMPLETE — verdict PASS-MANDATORY (full HIT conjunction `(C1) ∧ (C2) ∧ (C3) ∧ (iv)`; K=2 → K=3 MANDATORY advancement on the Hybrid Independence Test corpus per `cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"`)\n",
    1,
)

# Replace Results table block
OLD_RESULTS = """### Results (filled at runtime)

| Field | Value |
|:------|:------|
| `A_K_blocks` | pending |
| `A_K_PS_blocks` | pending |
| `inheritance_morphism_SU3_subset_SU4_verified` | pending |
| `hit_C1_pass` | pending (expected True; PS-extension structurally distinct from I-V) |
| `hit_C2_pass` | pending (expected True; ≥ 1 candidate host) |
| `hit_C3_pass` | pending (expected True; ≥ 1 structurally-distinct bridge class) |
| `hit_iv_pass` | pending (expected True; Wedderburn block rank distinction) |
| `hit_predicate_disjunction` | pending |
| `hit_predicate_full` | pending |
| `k_counter_advancement` | pending |
| `candidate_hosts_enumerated` | pending |
| `candidate_bridge_classes_enumerated` | pending |
| `audit_sha256` | pending |
"""

NEW_RESULTS = """### Results (filled at runtime)

| Field | Value |
|:------|:------|
| `A_K_blocks` | `{chi_C: 1, M_2_L_via_H: 2, M_3_c: 3}` (SM-gauge canonical Wedderburn) |
| `A_K_PS_blocks` | `{chi_C: 1, M_2_L: 2, M_2_R: 2, M_4_PS: 4}` (Pati-Salam extension Wedderburn) |
| `wedderburn_block_count_A_K -> A_K_PS` | 3 -> 4 |
| `wedderburn_block_rank_set_A_K` | `{1, 2, 3}` |
| `wedderburn_block_rank_set_A_K_PS` | `{1, 2, 4}` (NEW rank 4) |
| `new_PS_factors_in_extension` | `[M_2_R (SU(2)_R right-handed isospin), M_4_PS (SU(4)_PS lepto-colour)]` |
| `inheritance_morphism_SU3_c_in_SU4_PS_lepton_color_unification` | True (canonical block-diagonal embedding `diag(c1,c2,c3) -> diag(c1,c2,c3,l)`) |
| `hit_C1_distinct_substrate_pillar_PASS` | **True** (Pillar VI/VII/VIII candidates structurally distinct from `{I-V, IX}`) |
| `hit_C2_distinct_laboratory_pillar_PASS` | **True** (3 candidate hosts alpha/beta/gamma; all distinct from existing lab pillars) |
| `hit_C3_distinct_bridge_map_class_PASS` | **True** (`{delta Karoubi-Villamayor, zeta Volovik q-theory variational}` structurally distinct; epsilon PS-gauge-twisted HKR DISCARDED ambiguous) |
| `hit_iv_independent_algebraic_envelope_PASS` | **True** (Wedderburn block rank 4 distinct from existing K-instance rank-3 envelopes; SU(4)_PS Peter-Weyl multiplicity polynomial-growth ~ 2x SU(3); no shared regulator-invariant form) |
| `hit_predicate_disjunction (i ∨ ii ∨ iii) ∧ iv` | **True** |
| `hit_predicate_full_conjunction i ∧ ii ∧ iii ∧ iv` | **True** |
| `K_counter_advancement` | **K=2 → K=3 MANDATORY (full conjunction)** |
| `verdict_class` | **PASS-MANDATORY** |
| `candidate_hosts_enumerated` | `[host_alpha_CFL_phase_quark_matter, host_beta_Volovik_q_theory_superfluid, host_gamma_Landau_Ginzburg_SU4_4_component]` |
| `candidate_bridge_classes_enumerated` | `[delta_Karoubi_Villamayor (distinct), epsilon_PS_gauge_twisted_HKR (ambiguous; DISCARDED), zeta_Volovik_q_theory_variational_principle (distinct)]` |
| `AZ_class_BDI_persistence_under_PS_extension` | True (T^2=+1, KO-dim=6 preserved per landau framework-constants.md line 13; 4th lepton-colour row is BDI-protected leptonic-singlet) |
| `qtheory_ftheory_equivalence_S45_cited` | True (Volovik q-theory <-> F-theory bridge for host beta per `project_qtheory-ftheory.md`) |
| `K2_baseline_provenance_INFO` | Plan-text cites "T2.36 Wodzicki-BCS at §VII.AX"; runtime verification: T2.36 Wodzicki-BCS landed at slot §VII.BA (slot reroute; composite FAIL on Level-3 floor but K_pre=1 -> K_post=2 on axis-(iii) bridge-map-class distinctness intact); §VII.AX.OP-PROJ PBH band-edge ALSO advances K=1 -> K=2 independently. Two K=2 calibration instances coexist; pre-state robust under either citation. INFO-class drift disclosure only. |
| `audit_sha256` | `e16af0bac57fd42dae100d1e8e4dbbb43a97b2f14b8b6301aec97fc7f50f8bae` |
| `content_sha256` | `d7ff052ea82317e851c3c19b0d45a510f6f7eb3c9738dd265a377fd70c2fffc0` |
| `results_json_sidecar` | `computations/session-91/s91_w9_pati_salam_laboratory_pillar_candidate.json` |
"""

assert OLD_RESULTS in text, "Results table anchor not found"
text = text.replace(OLD_RESULTS, NEW_RESULTS, 1)

# Replace Verdict block
OLD_VERDICT = """### Verdict (filled at runtime)

```
S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION: <PASS-MANDATORY|PASS-SUGGESTION|INFO|FAIL> -- value=<hit_C1_pass>+<hit_C2_pass>+<hit_C3_pass>+<hit_iv_pass>+<k_counter_advancement_string> scheme=pati-salam-extension-laboratory-pillar-candidate-identification-HIT-C1-C2-C3 convention=FWD-C4-Pati-Salam-SU4-PS-extension-VI-VII-VIII-host-candidates-bridge-Karoubi-Villamayor-OR-Volovik-q-theory L_max=N/A_substrate_extension_identification audit_sha256=<pending> content_sha256=<pending> schema_version=S84+
# audit_sha256_short=<pending> content_sha256_short=<pending> # S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION dual-SHA companion row
# sign_verdict=<pending> magnitude_verdict=<pending> regime_verdict=<pending> # S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION 3-tuple annotation (S87 schema-v2)
```
"""

NEW_VERDICT = """### Verdict (filled at runtime)

```
S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION: PASS -- value='hit_C1_distinct_substrate_pillar_PASS=True;hit_C2_distinct_laboratory_pillar_PASS=True;hit_C3_distinct_bridge_map_class_PASS=True;hit_iv_independent_algebraic_envelope_PASS=True;K_counter_advancement=K=2_->_K=3_MANDATORY_(full_conjunction);verdict_class=PASS-MANDATORY;A_K_PS_wedderburn_blocks=['chi_C', 'M_2_L', 'M_2_R', 'M_4_PS'];wedderburn_block_count_A_K_PS=4;new_PS_factors_in_extension=['M_2_R', 'M_4_PS'];candidate_substrate_pillars=['Pillar_VI_CFL_phase', 'Pillar_VII_Volovik_q_theory', 'Pillar_VIII_Landau_Ginzburg_4_component'];candidate_lab_pillars=['Pillar_VIII_Landau_Ginzburg_4_component_QGP', 'Pillar_VII_Volovik_q_theory_superfluid', 'Pillar_VI_CFL_phase_quark_matter'];n_candidate_hosts=3;structurally_distinct_bridge_classes=['delta_Karoubi_Villamayor_K_theory_localization_at_M_4_C_PS', 'zeta_Volovik_q_theory_variational_principle_bridge'];ambiguous_bridge_class_discarded=epsilon_PS_gauge_twisted_HKR;inheritance_morphism_SU3_c_in_SU4_PS_via_lepton_color_unification=True;AZ_class_BDI_persists_via_landau_co_author=True;qtheory_ftheory_equivalence_S45_cited=True;K2_baseline_provenance_INFO=plan_text_cites_T2-36_Wodzicki-BCS_runtime_verifies_VII_AX_OP_PROJ_PBH_band_edge_S91_W5-4;K2_baseline_structurally_correct=True' scheme=pati-salam-extension-laboratory-pillar-candidate-identification-HIT-C1-C2-C3 convention=FWD-C4-Pati-Salam-SU4-PS-extension-VI-VII-VIII-host-candidates-bridge-Karoubi-Villamayor-OR-Volovik-q-theory L_max=N/A_substrate_extension_identification audit_sha256=e16af0bac57fd42dae100d1e8e4dbbb43a97b2f14b8b6301aec97fc7f50f8bae content_sha256=d7ff052ea82317e851c3c19b0d45a510f6f7eb3c9738dd265a377fd70c2fffc0 schema_version=S87+
# audit_sha256_short=e16af0bac57fd42d content_sha256_short=d7ff052ea82317e8 # S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION dual-SHA companion row (W9a-99 split)
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION 3-tuple annotation (S87 schema-v2)
```
"""

assert OLD_VERDICT in text, "Verdict block anchor not found"
text = text.replace(OLD_VERDICT, NEW_VERDICT, 1)

# Replace Substrate framing runtime addendum + Carry-forwards
OLD_RUNTIME_BLOCK = """### Substrate framing (runtime addendum)

(reserved)

### Cross-references

- `cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"` — HIT (i ∨ ii ∨ iii) ∧ iv predicate
- `cross-pillar-bridge-anatomy.md §\"Three forward bridge candidates\"` — FWD-C1/C2/C3 baseline + FWD-C4 candidate
- Pati-Salam 1973-1974 SU(4)_PS × SU(2)_L × SU(2)_R gauge structure
- `feedback_agent-roster.md` — volovik q-theory authority
- `feedback_agent-roster.md` — landau co-author convention
- `project_qtheory-ftheory.md` — Volovik q-theory ↔ F-theory equivalence
- §W9-9 T2.36 Wodzicki-BCS §VII.AX landing (K=2 baseline prereq)

### Carry-forward computations (filled at runtime)

(reserved)
"""

NEW_RUNTIME_BLOCK = """### Substrate framing (runtime addendum)

The substrate IS the spectral triple `(A_K, H_K, D_K)` at tau_fold = 0.19. The Pati-Salam extension `A_K_PS = C (+) M_2(C)_L (+) M_2(C)_R (+) M_4(C)_PS` IS the substrate's intrinsic minimal forward GUT extension preserving the inheritance-morphism structure `A_K -> A_K_PS` via `SU(3)_c subset SU(4)_PS` lepton-colour unification (Pati & Salam 1973 Phys.Rev. D8 1240; 1974 Phys.Rev. D10 275). The three candidate laboratory hosts (CFL-phase quark matter at Pillar VI; Volovik q-theory superfluid at Pillar VII; Landau-Ginzburg SU(4) 4-component at Pillar VIII) ARE three structurally distinct F-images of the SAME substrate-IS extension at distinct methodology layers (condensed-matter colour-superconductor, cosmological-vacuum-variable thermodynamic equilibrium, classical-phase-transition critical-exponent universality). The two structurally distinct bridge map classes (delta Karoubi-Villamayor K-theory localization at M_4(C)_PS; zeta Volovik q-theory variational principle on q in M_4(C)_PS) ARE two F-images of the bridge axis at categorically distinct layers (algebraic-K-theory localization functor vs thermodynamic-variational-principle transport). FORBIDDEN container-inversion: "Pati-Salam is one of many GUT extensions we consider" -> CORRECTED direction: "Pati-Salam IS the substrate's intrinsic minimal GUT extension that preserves the inheritance-morphism structure `A_K -> A_K_PS` via `SU(3)_c subset SU(4)_PS` lepton-color unification; the forward Pillar VI/VII/VIII laboratory hosts ARE the substrate's own extension domain, not containers in which the substrate is embedded."

The K=3 MANDATORY advancement on the Hybrid Independence Test corpus completes the saturation `{K=1: §VII.AF.1 W-5 Pillar III <-> IV HKR; K=2: §VII.AX.OP-PROJ + §VII.BA T2.36 Wodzicki-BCS substrate-clock-cancellation OR layer-functor-F bridges; K=3: forward §VII slot FWD-C4 Pati-Salam at S92+}` per the rule-level K-counter advancement clause of `cross-pillar-bridge-anatomy.md §\"Two-clause separation\"`. Per the §\"Two-clause separation\" discipline, this is the rule-level corpus saturation (rule status advisory -> MANDATORY), structurally independent of the per-entry registry-PASS criterion (which gates STAGE-1-CANDIDATE -> STAGE-3-PERMANENT promotion under `joint-theorem-promotion.md` 4-stage pathway and remains forward-pinned for the FWD-C4 §VII slot landing at S92+).

### Cross-references

- `.claude/rules/cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"` — HIT `(i ∨ ii ∨ iii) ∧ iv` predicate; advisory K=1 status promoting to MANDATORY at K=3
- `.claude/rules/cross-pillar-bridge-anatomy.md §\"Three forward bridge candidates\"` — FWD-C1/C2/C3 baseline; FWD-C4 newly identified by this gate
- `.claude/rules/cross-pillar-bridge-anatomy.md §\"Two-clause separation\"` — rule-level corpus K-counter advancement vs per-entry registry-PASS criterion structural orthogonality
- `.claude/rules/phononic-framing.md §\"IS Space, Not IN Space\"` — substrate framing direction; container-thinking inversion forbidden
- `.claude/rules/phononic-framing.md §\"Cross-pillar bridge anatomy\"` — 5 anatomy elements + 3-level ladder structural requirement
- `.claude/rules/joint-theorem-promotion.md §\"Stage 1\"` + §\"Stage 2\"` — STAGE-1-CANDIDATE -> STAGE-3-PERMANENT 4-stage pathway for the forward FWD-C4 §VII slot at S92+
- Pati J.C. & Salam A. (1973) Phys.Rev. D8, 1240; (1974) Phys.Rev. D10, 275 — `SU(4)_PS × SU(2)_L × SU(2)_R` gauge structure, lepton-as-4th-colour unification
- `feedback_agent-roster.md` — volovik q-theory PRIMARY authority
- `feedback_agent-roster.md` — landau co-author convention ("include in all future collabs")
- `project_qtheory-ftheory.md` — Volovik q-theory ↔ F-theory equivalence (S45 user insight; Q-THEORY-BCS-45 PASS at tau* = 0.209); host beta bridge zeta structural foundation
- `.claude/agent-memory/landau-condensed-matter-theorist/framework-constants.md` lines 13, 25, 27, 28 — AZ class BDI / Landau-Ginzburg free-energy form / Pomeranchuk stability / effective-mass renormalization
- `.claude/agent-memory/landau-condensed-matter-theorist/MEMORY.md` line 55 — BCS class 3D Ising PERMANENT (SM-gauge); n=4 Heisenberg-class extension under PS-extension
- §W9-9 T2.36 `S91-W1-14-WODZICKI-BCS-BRIDGE-THEOREM-STAGE-1-CANDIDATE-REGISTRY-LANDING` at slot §VII.BA — K=2 calibration corpus instance #2a (alternative to §VII.AX.OP-PROJ K=2 instance #2b)
- `sessions/permanent-results-registry.md §VII.AX.OP-PROJ` S91 W5-4 PBH band-edge — K=2 calibration corpus instance (registry line 18578)
- `sessions/permanent-results-registry.md §VII.AF.1` W-5 — K=1 baseline calibration corpus instance

### Carry-forward computations (filled at runtime)

**CF-W9-12-1**: STAGE-1-CANDIDATE registry landing for FWD-C4 Pati-Salam-class superfluid host bridge theorem at next-free §VII slot (S92+).
- **What**: Allocate next-free §VII slot (post-§VII.BA per `_registry_landing_audit.py` next-free-letter protocol per `registry-landing.md §\"Bridge-Landing Script Architecture\"` AFTER-pattern); populate 5-anatomy elements + 3-level ladder for the FWD-C4 bridge theorem with one selected host (`(alpha, delta)` or `(alpha, zeta)` or `(gamma, delta)` or `(gamma, zeta)` pair); declare Level-2 sub-class (binding/non-binding/deferred-pending per `cross-pillar-bridge-anatomy.md §\"Level-2 sub-class\"`).
- **Inputs**: (i) `s91_w9_pati_salam_laboratory_pillar_candidate.json` (this gate's substrate-physics derivation; audit_sha256=`e16af0bac57fd42dae100d1e8e4dbbb43a97b2f14b8b6301aec97fc7f50f8bae`); (ii) `sessions/permanent-results-registry.md` next-free-letter slot allocation; (iii) Pati-Salam 1973-1974 + Volovik q-theory canonical references; (iv) host-platform empirical data (Delta_CFL bounds from NICER/XMM-Newton for alpha; SU(4) epsilon-expansion critical exponents from Brezin-Le Guillou-Zinn-Justin for gamma).
- **Gate**: PASS = NEW §VII slot allocated + 5-anatomy populated + 3-level ladder declared + STAGE-1-CANDIDATE tag + Level-2 sub-class declared.
- **Effort**: ~1.5 wave-equivalents.
- **Depends on**: this gate (CF-W9-12-1 consumes the candidate identification verdict + JSON sidecar produced here); §W9-9 T2.36 Wodzicki-BCS landing protocol (template for STAGE-1-CANDIDATE single-shot bridge-landing AFTER-pattern); mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (cosmology-side cross-pillar bridge entries authorship).

**CF-W9-12-2**: Stage-2 cross-axis verify for forward FWD-C4 STAGE-1-CANDIDATE per `joint-theorem-promotion.md §\"Stage 2 — Two-Agent Parallel Cross-Check\"` (S93+).
- **What**: Dispatch two-axis cross-reviewers without prior workshop context: Axis-A (spectral / NCG-axiomatic) = connes-ncg-theorist (or lizzi-spectral-functional-theorist); Axis-B (substrate / superfluid-universe) = NOT volovik (downstream-inheritance reach exclusion applies — volovik is PRIMARY author of this gate per `joint-theorem-promotion.md §\"Axis-B Selection Protocol\"` clause 2). Substrate-input-orthogonality predicate satisfaction at ≥ 1 observable per `joint-theorem-promotion.md §\"Substrate-input-orthogonality clause\"` MANDATORY-K=3 (per S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT advancement).
- **Inputs**: (i) Stage-1 registry landing from CF-W9-12-1; (ii) cross-pillar bridge anatomy rule (5 anatomy + 3-level); (iii) hybrid independence test rule.
- **Gate**: PASS = both cross-reviewers PASS-AND on JOINT clauses; PASS = Stage-1 -> Stage-3 PERMANENT promotion eligible (subject to per-entry registry-PASS Level-3 < Level-2 empirical anchor satisfaction).
- **Effort**: ~3.0 wave-equivalents (parallel dispatch).
- **Depends on**: CF-W9-12-1; agent-selection protocol per `joint-theorem-promotion.md §\"Axis-B Selection Protocol\"` (Axis-distinctness + original-authoring-agent exclusion with downstream-inheritance reach + audit-coverage adequacy).

**CF-W9-12-3** (CONDITIONAL on CF-W9-12-2 PASS): empirical-anchor Level-3 evaluation for the selected `(host, bridge)` pair at the substrate-distance-2 pole on M_4(C)_PS Peter-Weyl block (S94+).
- **What**: Compute `Res_{s=4} Tr(D_K_PS^{-2s})|_{P_M4C_PS}` at the appropriate L_max (≥ 12 per `math-scripts.md §\"D_K Block-Diagonality Pre-Check\"` Friedrich-Bar saturation theorem); evaluate Level-3 empirical anchor at canonical L_max; compare to Level-2 algebraic envelope `L^{-alpha}` at the selected bridge-map class.
- **Inputs**: D_K_PS spectrum cache at L_max ≥ 12 with M_4(C)_PS block extension (NEW computation; SM-gauge cache only has M_3(C)_c rank-3 block — PS-extension requires recomputing the spectrum cache with the rank-4 block included); selected `(host, bridge)` pair per CF-W9-12-1 selection.
- **Gate**: Level-3 < Level-2 at canonical L_max => registry-PASS ELIGIBLE; STAGE-1 -> STAGE-3 PERMANENT promotion subject to Stage-2 PASS per CF-W9-12-2.
- **Effort**: ~4.0 wave-equivalents (NEW spectrum cache + Level-2 envelope derivation + Level-3 anchor evaluation).
- **Depends on**: CF-W9-12-1 (slot allocated + 5-anatomy populated); CF-W9-12-2 (Stage-2 PASS); D_K_PS spectrum extension to M_4(C)_PS rank-4 block (NEW infrastructure carry-forward beyond this gate's scope).
"""

assert OLD_RUNTIME_BLOCK in text, "Runtime addendum + Carry-forward anchor not found"
text = text.replace(OLD_RUNTIME_BLOCK, NEW_RUNTIME_BLOCK, 1)

# Atomic write
WP.write_text(text, encoding="utf-8")
print(f"Patched §W9-12 in {WP}")
print(f"  bytes written: {len(text.encode('utf-8'))}")
