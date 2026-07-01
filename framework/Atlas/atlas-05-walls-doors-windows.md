# Atlas D05: Walls, Doors, and Windows

**Scope**: Sessions 1-118 (Dec 2024 — Jun 2026)
**Updated**: 2026-05-09 (S52-S88 uplift; +11 walls W11-W21, +14 doors session-keyed, +18 windows Window-7..24); 2026-06-20 (S110 HK-GEOM-WALL: +1 organizing wall W22, investigation-track); **2026-07-01 (S110→S118 uplift; S119-current: +3 substrate walls W23-W25 + greybody candidate wall, +10 session-keyed doors S89-S118, +3 windows Window-25..27; STAGE-1→STAGE-3 door promotions; LISA-Ω_GW live-forecast down-tagged — falsifier migrated GW→LSS)**
**Totals**: 25 numbered walls (W1-W18 substrate-physics + W19-W21 methodology-floor + W22 organizing + W23-W25 substrate-physics S89-S118) / 37 doors / 27 windows (26 OPEN + 1 permanently CLOSED)

---

## I. Walls (Structural Obstructions)

### W1: Weyl Asymptotic F/B Ratio

- **Statement**: The ratio of fermionic to bosonic spectral weight on Jensen-deformed SU(3) is F/B = 16/44 = 0.364 (fiber dimension), asymptotically tau-independent by Weyl's law. The spectral-weighted ratio is F/B = 0.55. Any volume-preserving deformation of any compact manifold produces a tau-independent F/B ratio in the UV.
- **Proof session**: S18 (first observed), S20b (proven structural via Weyl's law), S22c (Trap 3)
- **Scope**: Blocks ALL perturbative spectral functionals that depend on the UV balance of bosonic and fermionic modes. Specifically: Coleman-Weinberg, Casimir energy (all field content), spectral back-reaction, Higgs-sigma portal, signed gauge-threshold corrections. Any mechanism that requires the F/B ratio to vary with tau to produce a minimum is killed.
- **Closures attributed**: 6 (mechanisms #2, 3, 4, 8, 12, 15 in D02)
- **Escape**: Low-mode regime (N < 200) where autocorrelation corrections are O(N^{-1/8}) ~ 50-60%. BCS operates in this regime. The UV tail controls the spectral action, but BCS condensation depends on the IR density of states near the van Hove fold.

---

### W2: Peter-Weyl Block-Diagonality

- **Statement**: D_K is exactly block-diagonal in the Peter-Weyl basis for ANY left-invariant metric on ANY compact semisimple Lie group. Three independent proofs (algebraic, representation-theoretic, numerical at 8.4e-15). The off-diagonal matrix elements C_nm between distinct (p,q) sectors vanish identically.
- **Proof session**: S22b (8.4e-15, three proofs)
- **Scope**: Blocks ALL mechanisms requiring cross-sector coupling in the Dirac spectrum. Inter-sector cancellation of spectral sums, inter-sector energy transfer, coupled delta_T crossing, coupled V_IR minimum. The signed-sums escape route (b_1 - b_2 sign change) is killed because each sector is independently monotone with no possibility of inter-sector cancellation.
- **Closures attributed**: 3 (mechanisms #13, 14, 20 in D02)
- **Escape**: Nothing -- this is exact. Block-diagonality is a consequence of representation theory, not an approximation. However, it does NOT prevent the physical BCS condensate from carrying inter-sector quantum numbers (Cooper pairs carry K_7 charge from B2, which connects to B1/B3 through the Josephson coupling in the many-body Hamiltonian, not through D_K matrix elements).

---

### W3: Spectral Gap at mu = 0

- **Statement**: D_K has spectral gap lambda_min > 0 at all tau on the Jensen curve. D_total gap minimum = 0.790 M_KK at tau = 0.27. The gap never closes. At mu = 0, there is no Fermi surface, and BCS pairing in the standard sense (Cooper instability at the Fermi surface) is absent.
- **Proof session**: S17a (gap observed), S19a S-4 (fermion condensate killed), S23a K-1e (Kosmann-BCS decisive), S30Ab (Pfaffian trivial, gap > 0 confirmed at 75 tau values)
- **Scope**: Blocks ALL mechanisms requiring a Fermi surface or zero-energy states at mu = 0. Banks-Casher fermion condensate, Kosmann-BCS at mu = 0, gap-edge self-coupling. Also blocks canonical and grand canonical mu != 0 routes via particle-hole symmetry (S34).
- **Closures attributed**: 5 (mechanisms #5, 17, 18, 25, 26 in D02)
- **Escape**: BCS at finite effective mu (the KC chain, which generates mu_eff through phonon collisions). The van Hove singularity at the B2 fold produces a divergent DOS that triggers BCS through the 1D theorem (any g > 0, RG-BCS-35) without requiring a Fermi surface. The escape is the recognition that BCS on a compact manifold is NOT the same as BCS in a metal -- the critical coupling is zero.

---

### W4: Spectral Action Monotonicity (Structural Monotonicity Theorem)

- **Statement**: The weighted spectral mean <lambda^2>(tau) increases monotonically under volume-preserving Jensen deformation. For any monotonically decreasing cutoff function f, the spectral action S_f(tau) = Tr f(D^2/Lambda^2) decreases monotonically. For any increasing f, S_f increases. No local minimum exists at any tau in [0, 0.5] for any monotone f, any Lambda > 0, any of the 10 tested Peter-Weyl sectors. Verified at 9,600 individual checks (10 cutoffs x 6 Lambda x 16 tau x 10 sectors).
- **Proof session**: S37 CUTOFF-SA-37 (definitive), with precursors at S17a (V_tree), S18 (CW), S20a (SD), S24a (V_spec), S36 (S_full)
- **Scope**: Blocks ALL single-trace spectral action mechanisms with monotone cutoff functions. This is the most powerful wall, closing the entire category of "spectral action tau-stabilization." Includes: V_tree, CW, Casimir (all modes), Seeley-DeWitt, V_spec at all rho, Connes 8-cutoff, V'' spinodal, Kerner bridge, V_total on U(2)-inv surface, Freund-Rubin, full 28D Hessian, foam non-monotone, occupied-state SA, unexpanded SA. The wall extends to all smooth monotone cutoffs, all Lambda, and all 28 dimensions of the left-invariant metric space (HESS-40).
- **Closures attributed**: 13+ (mechanisms #1, 7, 9, 10, 11, 19, 22, 23, 24, 30, 37, 45, 47, 48 in D02)
- **Escape**: (1) Wheeler-DeWitt quantum localization (wavefunction can peak on a monotone slope). (2) Instanton-averaged path integral (breaks single-vacuum assumption). (3) Multi-trace spectral action (product of monotone functions is not necessarily monotone). (4) Off-Jensen moduli (theorem proven only on Jensen; multi-parameter landscape may have saddle points). (5) Non-spectral-action functionals entirely.

---

### W5: Berry Curvature Vanishing

- **Statement**: K_a is anti-Hermitian (||K_a + K_a^dag|| < 1.12e-16, structural) for the Kosmann derivative on Jensen-deformed SU(3). This implies Berry curvature Omega = 0 identically for ALL eigenstates, ALL sectors, ALL tau. Extends to ANY compact Lie group with left-invariant metric.
- **Proof session**: S25 (definitive, machine epsilon)
- **Scope**: Blocks ALL topological mechanisms based on Berry phase physics (Berry curvature monopoles, Chern numbers of eigenvalue bundles, topological transitions driven by Berry flux). The S21a "Berry curvature monopoles" were reclassified as quantum metric (Provost-Vallee), not Berry curvature.
- **Closures attributed**: 0 directly (Berry-based mechanisms were never independently proposed and tested as tau-stabilization candidates). The wall preemptively closes a class of mechanisms.
- **Escape**: Off-Jensen deformations where K_a may not be anti-Hermitian. Pfaffian Z_2 (which is a discrete topological invariant, not a Berry curvature quantity). Note: Pfaffian = +1 on Jensen at all tau (W5b in mega-matrix), but off-Jensen is untested.

---

### W6: NCG-KK Scale Irreconcilability

- **Statement**: The NCG spectral action cutoff Lambda_SA and the KK mass scale M_KK are irreconcilable. Lambda_SA/M_KK = 10^6 at tau = 0.21, and 10^15 at tau = 0.57. The spectral action identification (Lambda_SA = M_KK) fails by 6-15 orders of magnitude at all tested tau values.
- **Proof session**: S30Bb (B-30nck), S31Ba (B-31nck)
- **Scope**: Blocks the identification of the NCG spectral action cutoff with the KK compactification scale. This does not close the mathematical structure (D_K eigenvalues, selection rules, etc.) but closes the physical interpretation connecting the spectral action to 4D gauge kinetic terms at M_KK.
- **Closures attributed**: 0 directly (this is an interpretive wall, not a mechanism closure)
- **Escape**: (1) Abandon NCG identification entirely (pure KK interpretation). (2) Threshold corrections from heavy KK modes (unprecedented but theoretically possible). (3) Non-standard M_KK.

---

### W7: alpha_s = n_s^2 - 1 Structural Identity (NEW, S50)

- **Statement**: For ANY equilibrium propagator with K^2 dispersion on a compact Josephson lattice with broken U(1), the spectral running alpha_s is algebraically determined by the tilt n_s through alpha_s = n_s^2 - 1. Five independent proofs: (1) 3-pole degeneracy (poles 99.95% degenerate), (2) running mass algebraic bound gamma < 1-n_s = 0.035, (3) zero-mode protection preventing eikonal damping, (4) RPA vertex correction suppressed by mass hierarchy, (5) Goldstone theorem enforcing K^2 dispersion.
- **Proof session**: S50 (five proofs in W1-A, W1-F, W1-H, W2-A, W2-B); promoted to **§VII.X.1 STAGE-3-PERMANENT** at S85 W2-9 (Sage-exact rational form: α_s = -8587279/100000000 at u_pivot = 19649/351).
- **Scope**: Blocks ALL mechanisms for generating the observed alpha_s = -0.008 from a K^2 Josephson propagator with n_s = 0.965. The identity gives the substrate-distance (BZ) running alpha_s = -0.0858728 (§VII.X.1 Sage-exact, Mellin s=3), scale-separated from the Goldstone-pivot (CMB-channel) running ~0 by deg(T_{BZ->pivot})=2; the older single-label "-0.069 at 6-8 sigma" conflated the two channels. Closes 3-pole Leggett, running mass, anomalous dispersion within the phase sector.
- **Closures attributed**: 3 (mechanisms #56.1, 56.3, 56.5 in D02)
- **Escape**: Correlators from OUTSIDE the Josephson phase sector. The SA correlator has 110% pole spread and breaks the identity. Pair-transfer sinc^2 form factor also breaks it. The escape requires mixing between the phase sector and other spectral sectors.

---

### W8: Anderson-Higgs Impossibility for U(1)_7 (NEW, S51)

- **Statement**: K_7 cannot be gauged within the NCG inner fluctuation framework. Three independent proofs: (1) Commutant obstruction: [D_K, K_7] = 0 implies trivial 1-form A_7 = a[D_K, K_7] = 0 at tree level. This propagates to all loop orders because any function Sigma(D_K) satisfies [K_7, Sigma(D_K)] = 0. (2) Categorical distinction: K_7 is a Kosmann derivative (diffeomorphism generator), not an inner automorphism of A_F (gauge generator). NCG gauge fields arise exclusively from inner automorphisms. (3) Even forcing the off-diagonal breaking (epsilon = 0.117) gives m_gauge = 0.12-0.54 M_KK, 15-65x below the [8,16] target.
- **Proof session**: S51 W1-C (GAUGE-U1K7-51)
- **Scope**: Blocks the Anderson-Higgs mechanism as a route to giving the Goldstone a mass. The Goldstone boson of U(1)_7 breaking cannot be eaten by a gauge field. Closes the sole surviving Goldstone theorem loophole identified by Landau in S50 collab.
- **Closures attributed**: 1 (mechanism #56.18 in D02)
- **Escape**: Physics outside the NCG inner fluctuation framework. External gauging of K_7 (not from the spectral triple), or a mass mechanism that does not involve gauge field absorption.

---

### W9: Convex Combination Theorem for Additive Mixing (NEW, S51)

- **Statement**: The spectral index of an additive mixture P_phys(K) = (1-beta)*P_G(K) + beta*chi_SA(K) is a convex combination of the individual spectral indices, bounded by [min(n_s_G, n_s_SA), max(n_s_G, n_s_SA)] at each K. At K_pivot = 2.0 M_KK: n_s(Goldstone) = -0.996, n_s(SA) = +0.150. The mixed n_s is bounded above by +0.150, while the target is 0.965.
- **Proof session**: S51 W2-A (SA-GOLDSTONE-MIXING-51)
- **Scope**: Blocks additive SA-Goldstone mixing at K_pivot = 2.0 M_KK. The obstruction is the mass problem: K_pivot/K* = 22.9, placing the Goldstone deep in its K^{-2} regime. The Goldstone mass 0.070 M_KK is 170x below the required 11.85 M_KK.
- **Closures attributed**: 1 (mechanism #56.20 in D02)
- **Escape**: Remapping K_pivot to K < K* = 0.087 M_KK. At these scales, both correlators are nearly flat, the SA pole spread breaks the identity, and n_s = 0.965 is achievable with beta > 0.9 and alpha_s in [-0.040, 0]. This requires >= 3.1 e-folds from the stiff epoch, obtainable from tau_i <= 1.7e-5 (EFOLD-MAPPING-52).

---

### W10: Zero-Mode Protection on T^2 (NEW, S50-S51)

- **Statement**: The Goldstone is a KK n = 0 mode on T^2 (the torus of the tessellation cell). Its wavefunction psi_0 = 1/sqrt(A) is constant, hence orthogonal to ALL higher KK eigenstates. This gives <0|V|n> = 0 to ALL ORDERS in the Born series for any position-diagonal operator V. Extended in S51 from first-order to all-orders Born.
- **Proof session**: S50 W1-H (eikonal damping), S51 W1-B (local resonance)
- **Scope**: Blocks ALL mechanisms that attempt to scatter the Goldstone into higher KK modes via position-dependent potentials. Eikonal texture damping, local resonance T-matrix mass enhancement, texture Born scattering.
- **Closures attributed**: 2 (mechanisms #56.4, 56.17 in D02)
- **Escape**: Mechanisms that are NOT position-diagonal (e.g., derivative coupling d/dx). The zero-point parametric mechanism (S51 W1-B) achieves m_eff = 2.45 M_KK precisely because it couples through d^2c/dphi^2 (a medium property, not a potential), circumventing the zero-mode protection. But this is still 5x short of the target.

---

### W11: Volovik CC Tracking Wall (NEW, S66 DILUTION-CC-66)

- **Statement**: Volovik q-theory thermodynamic relaxation: rho_vac ~ M_Pl² H²; rho_vac/rho_obs = 1.032 at present epoch (0.01 OOM from observation). FUNCTIONAL-INDEPENDENT (Gibbs-Duhem rho_vac = ε(q) − μq → 0 holds for any spectral functional). The 114 OOM gap IS the expansion history, NOT a fine-tuning problem.
- **Proof session**: S66 W1-A + Workshop 4
- **Scope**: Excludes the substrate-IS region where CC is treated as a static vacuum-energy fine-tuning problem; converts the 114 OOM gap from "open problem" to "misidentified expansion history". Anchored by Door 12 (mechanistic) + Door-S58 + Door-S66 (registry pins). Promotion gap: lacks dedicated §VII slot — recommend §VII.AT allocation in S89+ housekeeping.
- **Registry cite**: `framework-cc-oom.md`; `permanence-map.md` Pillar II anchor; `canonical_constants.py:1243` w0_FW = -0.918
- **Escape**: BBN-VOLOVIK-67 carry-forward must confirm rho_vac/rho_rad = 0.67 at z~10^9 nucleosynthesis is consistent with Scenario B; partial-PASS at S72.

---

### W12: Eps_H Spectral Functional Sign-Reversal (NEW, S66 functional crisis; W17 candidate companion)

- **Statement**: The Hubble slow-roll parameter eps_H = (1/2)(dS/dtau)²/(S · d²S/dtau²) sign-reverses across cutoff functions: sqrt(x) gives +0.022 (red tilt n_s = 0.9595 BCS+CW-dressed; committed bare √x = 0.9590); zeta/exponential gives negative (blue tilt n_s > 1). n_s spread across functionals 0.164 = 39× Planck error.
- **Proof session**: S66 (functional crisis surfaced); §VII.AB.1 Substrate Sign-Lock at S86 W-2.
- **Scope**: Excludes the substrate-IS region where a single bare eps_H reading can fix n_s without functional-class declaration; forces every n_s prediction to declare its regulator class (Chamseddine-Connes sqrt as unique survivor per S67 FUNCTIONAL-SELECT closure at 15.5-36.9σ Bayesian evidence).
- **Registry cite**: §VII.AB.1 (`permanent-results-registry.md:14911`); FUNCTIONAL-SELECT-67 carry-forward
- **Escape**: FUNCTIONAL-SELECT-67 closure; if Chamseddine-Connes sqrt is selected, the +0.022 red-tilt sub-family is canonical and σ_8 = 0.799 derivation is preserved.

---

### W13: F_4-MB Structural Wall Family (NEW, S86 1a-S1)

- **Statement**: At L_max=10 on the canonical D_K spectrum cache, the substrate's a_0 Seeley-DeWitt slot under {ζ, Zubarev, SDW} ∘ Mellin-Barnes residue ∘ CM-1995-SD-subtraction CANNOT be suppressed below |Λ_CC^MB|/|a_0^trunc| ≤ 0.5. Worst-case ratio 9.4557 (Zubarev). 4 constituent FAILs (S85-W0-7, S85-W0-11, S85-W0-20, S86-W2-1) on shared lens. F_4 = {ζ, Zubarev, SDW} closed on Axis_F4_MB.
- **Proof session**: S86 1a-S1 (volovik+connes+gen-physicist co-signed)
- **Scope**: Excludes the substrate-IS Pillar-III multiplier-algebra route to CC-suppression on F_4; 3 surviving corridors (q-theory C-Q, dilution C-D, Friedmann two-layer C-2L) all on disjoint axes.
- **Registry cite**: §VII.Z (`permanent-results-registry.md:15210`); §VII.V.A WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A (line 16024)
- **Escape**: Disjoint-axis CC-suppression corridors (Volovik tracking via W11; Friedmann two-layer C-2L; q-theory C-Q route).

---

### W14: Algebra-Axis Orthogonality Wall (NEW, S87 W-2 R3, MANDATORY at K=3)

- **Statement**: Algebra-INVARIANT (spectrum-only functional family) and algebra-DEPENDENT (state-pair functional family) are STRUCTURALLY ORTHOGONAL in identity-class membership: no closed-form {λ_n}-only identity reproduces any algebra-DEPENDENT functional, and conversely no state-functional-only identity reproduces any algebra-INVARIANT spectral moment. NCG axioms 1+5 + Connes-Moscovici 1995 §III.4 + axioms 4+6 + Poincaré duality + chirality-vs-A_F block-grading mismatch ensure structural orthogonality. Conjecture promoted MANDATORY at K=3 calibration corpus instances.
- **Proof session**: S87 W-2 R3 close (lizzi PRIMARY + connes CO-AUTHOR + mack CO-AUTHOR)
- **Scope**: Excludes the substrate-IS region where a substrate observable can be cited in single-axis form when both algebra-axes are admissible; forces every theorem text to declare its axis (corner-cell + pole). 4-corner partition: I=INV×s=3, II=INV×s=4, III=DEP×s=3, IV=DEP×s=4.
- **Registry cite**: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`; `pru-class-corpus.md §6`; §VII.U.2 (`permanent-results-registry.md` four-corner classification S88 W5b-45)
- **Escape**: None at the algebra-axis level (structural orthogonality is exact). Cross-corner co-primary structures FORBIDDEN per W15.

---

### W15: Cross-Corner Co-Primary Wall (NEW, S88 W-15 V.6)

- **Statement**: Two anchors on different algebra-axes (one on Cell I `n_s²−1` algebra-INVARIANT spectrum-only-functional cell, one on Cell IV variance theorem algebra-DEPENDENT state-pair-functional cell) cannot enter a single non-fungible SOURCE-DOUBLE-CITE-CO-PRIMARY chain; the two cells live on orthogonal algebra-axes (subordinate to W14).
- **Proof session**: S88 W-15 V.6 (W5a-44 surfacing of §VII.AN cross-corner conflation)
- **Scope**: Excludes the substrate-IS region where one CO-PRIMARY chain spans two structurally orthogonal cells; forces orthogonal-companion structure when both projections are independently registry-eligible.
- **Registry cite**: `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"` clause 4; `_registry_landing_audit.py` Class-(g) extension (S89-CROSS-CORNER-CO-PRIMARY-AUDIT)
- **Escape**: STRUCTURALLY-ORTHOGONAL-COMPANION structure (e.g., §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ split) when both algebra-axis readings are independently registry-eligible.

---

### W16: Layer-2-Non-Binding Bare-Decomposition Wall (NEW, S88 W8-88, MANDATORY at K=3)

- **Statement**: Bare-decomposition envelopes (Level-2-non-binding: substrate-internal Mellin-truncation rates with no HKR image to a continuum laboratory observable) DO NOT bind Level-1 cohomology classes; cannot count toward registry-PASS regardless of how tightly the Level-3 anchor satisfies the numerical bound; false-PASS pathway closed by construction.
- **Proof session**: S88 W8-88 (gen-physicist PRIMARY + connes-ncg-theorist CO-AUTHOR)
- **Scope**: Excludes the substrate-IS region where a `L^{-α}` algebraic envelope on a substrate-internal Tr(D_K^{-2s}) can pose as cross-pillar bridge evidence; routes to plan-freeze halt with HKR map citation requirement.
- **Registry cite**: `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` (MANDATORY at K=3 promoted at S88 W-22 W7a-74 V.5 close)
- **Escape**: Genuine HKR-binding Level-2 envelopes (Level-2-binding sub-class) where `L^{-α}` rate bounds the HKR-image convergence to the laboratory-IN observable. §VII.AF.1 + W3b-15 K=2 corpus.

---

### W17: Bare-Eigenvalue Parity-Blindness Wall (NEW, S85 W2-7 Bulletin #2)

- **Statement**: Even Seeley-DeWitt theorem: even-grading regulator-weighted Mellin moments (η-invariant alone) cannot decode odd-grading HP^1 content on the (C_H, C_epsH) parity-twin pair; canonical (η = 0, GV ≠ 0) signature on parity-twin pair structurally excludes η-only protocols.
- **Proof session**: S85 W2-7 (Bulletin #2 promotion); reinforced S86 W-11 RULE-2
- **Scope**: Excludes the substrate-IS region where η-detection alone discriminates parity-twin pairs; forces odd-grading observables (GV-Heitsch, K-theoretic torsion, η-Cheeger-Simons secondary classes) on HP^1 detection.
- **Registry cite**: `regulator-pin-discipline.md §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension"`; §VII.W (`permanent-results-registry.md:15003`); §VII.P′ (S86 W-11)
- **Escape**: Odd-grading detector class (GV-Heitsch, K-theoretic torsion).

---

### W18: Mechanical-Closure Type-F/Type-S Layer-Separability Wall (NEW, S88 W8-89; SUGGESTION at K=1)

- **Statement**: Type-F (single-summand-projection trace; algebra-INVARIANT) and Type-S (state-pair functional; algebra-DEPENDENT) sub-observables are structurally separated under the algebra-axis orthogonality 4-corner classification; mechanical closure on Type-F is admissible-with-conditions L1-L4 ONLY; mechanical closure on Type-S is NEVER admissible.
- **Proof session**: S88 W8-89 (gen-physicist orchestrator-direct-write; Stage-2 PASS-AND required from connes-spectral + volovik-substrate cross-reviewers)
- **Scope**: Excludes the substrate-IS region where state-pair functionals can be silently mechanically closed via Type-F partition admissibility; the convention-tag honesty discipline L4 is the boundary against PROHIBITED_ACTIONS Class 1 (convention-shopping).
- **Registry cite**: `mechanical-closure-discipline.md §"Layer-separability carve-out (admissible-with-conditions)"`
- **Escape**: K=3 promotion on calibration corpus saturation (currently K=1 advisory).

---

### W22: Geometry/Topology Dichotomy (ORGANIZING wall, NEW S110 HK-GEOM-WALL; inv-11 W3, investigation-track)

- **Statement**: Substrate obstructions split into a ROBUST topological class and a FRAGILE geometric class — topological-index observables commuting with the foam Hamiltonian (`[H_foam, topological-index] = 0`) are robust under deformation, whereas spectral-geometry observables that are not foam-stable are fragile. inv-11 W3 confirmed this robust-topological-vs-fragile-geometric split throughout the investigation excursion.
- **Status**: ORGANIZING wall — a classification device organizing the confirmed robust/fragile pattern, promoted from inv-11 W3 (investigation-track per `gate-verdicts.md §"Investigation-Track"`); NOT a new machine-ε substrate-physics theorem (unlike W1-W18). A heavier §VII registry slot is the forward option pending session-promotion of the underlying `[H_foam, topological-index] = 0` observable.
- **Proof session**: inv-11 W3 (investigation excursion; = inv-11 HY3). Session-promotion of the underlying observable not yet performed.
- **Scope**: Organizes which obstruction-class a result occupies (topological-robust vs geometric-fragile); guides which results survive deformation / foam-stability stress.
- **Registry cite**: `sessions/investigation/_promotion-triage.md` Bucket-3 §A (HK-GEOM-WALL).
- **Robust-class exemplar (NEW, S100a/S101)**: §VII.BM ε_LX **Foam-Protection identity** `[H_foam(N), ε_LX] = 0` for all N in the Wheeler-√N class — a foam-stable topological index that survives every foam configuration; the concrete occupant of W22's robust-topological class.
- **Escape**: §VII slot session-promotion (heavier registry landing) elevates the organizing wall to a registered structural result.

---

### W23: Superalgebra-Extension Obstruction (NEW, S96 §VII.BJ)

- **Statement**: No nontrivial Z/2-graded superalgebra extension of the substrate's finite algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` exists. Structural-existence theorem, exact, L-independent.
- **Proof session**: S96 S-1 (NYT-Q4 connes-synthesis §I–II); §VII.BJ STAGE-1-CANDIDATE
- **Scope**: Excludes the substrate-IS region where a supersymmetric (graded-algebra) enlargement of the finite spectral triple supplies a SUSY-partner spectrum or new light states. The substrate's finite algebra admits no super-extension — SUSY completions are structurally closed at the algebra level.
- **Closures attributed**: 1 (SUSY/superalgebra-extension corridor).
- **Escape**: physics outside `A_K` (external SUSY not arising from the spectral triple). None at the `A_K` algebra level.

---

### W24: Recursive-Casimir Yukawa-SHAPE Wall (NEW, S103 → §VII.CK S114 → UNCONDITIONAL S117)

- **Statement**: Within the recursive Casimir-graded ω-ladder on `(A_K, H_K, D_K)`, there is **no G-invariant non-monotone sign-changing degree of freedom**. The gen-2 Yukawa mass-splitting SHAPE (the sign structure of the generation hierarchy) cannot be produced by any Casimir-graded functional. The SCALE branch dissolves via M_KK-derivation; the SHAPE branch is a permanent wall.
- **Proof session**: S103 (`CF-S103-NO-SIGN-HANDLE` identified) → S114 W3-3 (§VII.CK SHAPE-wall landing) → S117 W2 (Stage-2 PASS-AND, axis-A lizzi + axis-B volovik → §VII.CK UNCONDITIONAL)
- **Scope**: Excludes Casimir-graded routes to the fermion-generation SHAPE (the mass-splitting sign pattern). Yukawa-hierarchy magnitude (SCALE) is derivable from M_KK; the SHAPE is walled.
- **Closures attributed**: 1 (gen-2 Yukawa-SHAPE-from-Casimir-graded-calculus).
- **Escape**: an off-Casimir full-SU(3) σ-model (beyond the C_2-graded ω-ladder) could carry the non-monotone DOF — untested forward gate; the wall is specific to the Casimir-graded calculus.

---

### W25: One-Loop Effective-Action Monotonicity — τ-selection (NEW, S95)

- **Statement**: The tree+one-loop-corrected effective action of the spectral moments is monotone in τ — **no interior well** at any τ on the Jensen curve (`S95-W2-3-NO-WELL-ONE-LOOP` PASS, value=0; `T-STAR-ONELOOP-ORIGIN` FAIL). Extends W4 (bare spectral-action monotonicity) to the one-loop-corrected effective potential.
- **Proof session**: S95 W2-3
- **Scope**: Excludes one-loop / variational dynamical selection of τ_fold: τ_fold cannot be fixed by minimizing an effective potential (tree or one-loop). The sole surviving selection route is the dynamical MECHANISM-CHAIN (I-1 + Turing + RPA + WALL + BCS first-order-transition criterion, Door 1); otherwise τ_fold = 0.190 remains an empirical input ("the last tuned number").
- **Closures attributed**: 1 (one-loop/variational τ-selection corridor). May alternatively be read as an explicit one-loop extension of W4.
- **Escape**: dynamical (non-variational) MECHANISM-CHAIN first-order transition; or τ_fold empirical.

---

## I-A. Methodology-Floor Walls (process discipline; NOT substrate-physics theorems)

> **Provenance**: Sub-section divider added 2026-05-10 per Sagan finding 05-2 (atlas-uplift hygiene pass). The walls W19-W21 below are RULE-FILE MANDATORY (process discipline at the layer-functor F methodology-side image per `epistemic-discipline.md §"Layer-Decomposition"`), structurally distinct from W1-W18 (substrate-physics walls — machine-epsilon proven structural identities, monotonicity theorems, representation-theoretic constraints, observational anchors). Methodology-floor walls close audit-floor pathologies BY CONSTRUCTION at plan-freeze; substrate-physics walls close mechanism-class regions by computation. Conflating the two layers inflates substrate-physics directional reading; cross-link to atlas-06 (probability trajectory layer-tag convention) and atlas-10 (METHODOLOGY-FLOOR + CALIBRATION-CORPUS taxonomy disclaimer).
>
> Each wall below carries its rule-file source + MANDATORY status at plan-freeze. NONE of these walls are "PROVEN" in the substrate-physics theorem sense (no machine-epsilon eigenvalue identity, no NCG-axiomatic derivation chain producing a concrete substrate-physics observable). They ARE MANDATORY at plan-freeze under the structural-discipline image of F.

---

### W19: PRU Class 8.0-8.6 Sub-Class Walls (methodology layer; multiple sessions)

- **Statement**: Pre-Registration Underspecification class taxonomy: Class 8.0/8.1 machinery-pin cardinality (S78); Class 8.2 verifier-rubric (S86 W-12, MANDATORY at K=5 post-S88 W-7 + W-21 + W-22 simultaneous K=2→K=5 advancement, 2026-05-08); Class 8.3 publication-precision (S86 W1c-8, MANDATORY at K=4 S87 W8); Class 8.4 representation-convention-pin (S88 W-16 W5b-50, K=1 advisory); Class 8.5 joint-hypersurface-pre-registration-form (S88 W-15 W4c-36, K=1 advisory); Class 8.6 layered-substitution-chain-audit (S88 W-17 W5b-47, K=1 advisory).
- **Proof session**: Multiple S78-S88 sessions; full taxonomy tabulated S88
- **Scope**: Excludes methodology-layer regions where rubric-form failure / precision-floor mismatch / convention-pin drift / hypersurface-form drift / layered-substitution-chain-audit failure can produce false-PASS verdicts. Each sub-class is a wall against a specific plan-authorship pathology.
- **Registry cite**: `epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"`; `pru-class-corpus.md §1-§7`
- **Escape**: K=3 promotion threshold for advisory sub-classes (8.4-8.6 currently K=1).

---

### W20: Joint-Theorem Single-Axis Promotion Wall (methodology layer; S86 W-9 RULE-1)

- **Statement**: Joint cross-axis theorems CANNOT enter `permanent-results-registry.md` STAGE-3-PERMANENT without 4-stage pathway (Stage 0 workshop-internal → Stage 1 STAGE-1-CANDIDATE registry → Stage 2 two-agent parallel cross-axis verify WITHOUT prior workshop context → Stage 3 PERMANENT); single-agent verification on joint clauses is structurally INSUFFICIENT (audit script `_joint_theorem_independent_verify_audit.py` REFUSES single-agent firings).
- **Proof session**: S86 W-9 RULE-1 (lizzi+transit, Path-(c) reassessment workshop)
- **Scope**: Excludes the methodology-layer region where shared-context-produced agreement among workshop authors can be mistaken for independent confirmation. The 4-stage pathway is the sole admissible route for joint cross-axis theorems.
- **Registry cite**: `joint-theorem-promotion.md` (MANDATORY); first calibration §VII.AH (S87 W9a-1); second §VII.AM (S88 W1b2-65)
- **Escape**: Stage-2 PASS-AND on two-agent parallel cross-axis verify per the protocol's substrate-input-orthogonality clause (S88 W7c-167 V.1).

---

### W21: Cross-Pillar Bridge 5-Anatomy + 3-Level Wall (methodology layer; S86 W-5; MANDATORY at K=3 S88 W4a-17)

- **Statement**: Every cross-pillar bridge entry MUST declare ALL 5 IS-not-IN anatomy elements (substrate-IS observable / laboratory-IN observable / bridge map / algebraic envelope / empirical anchor) AND the 3-level structural-confidence ladder (Level-1 cohomology-class identity / Level-2 algebraic envelope / Level-3 empirical anchor); Level-3 must satisfy Level-2 at canonical L_max for registry-PASS; entries lacking the structure are registry-incomplete and route to plan-freeze halt.
- **Proof session**: S86 W-5 RULE-1+2 (volovik+connes); MANDATORY at K=3 promoted S88 W4a-17 (3 calibration corpus instances: §VII.AF.1 LANDED + §VII.AH STAGE-1-CANDIDATE + §VII.W-3.LAB STAGE-1-CANDIDATE)
- **Scope**: Excludes the methodology-layer region where ad-hoc cross-pillar bridge claims (without explicit HKR / K-theory boundary / Connes-Karoubi pairing citation) can enter the registry; forces the substrate→laboratory direction of explanation.
- **Registry cite**: `cross-pillar-bridge-anatomy.md`; §VII.AF.1 (`permanent-results-registry.md:14690`); §VII.AH; §VII.AM (line 16367); §VII.W-3.LAB (line 16693)
- **Escape**: None at the registry-anatomy level (structural requirement).

---

## II. Doors (Permanently Open Routes)

These are results that survive unconditionally. No future computation can close them.

### Door 1: BCS Mechanism Chain (Unconditional, 5/5 links)

- **What it is**: The complete chain from van Hove fold through BCS condensation: I-1 (van Hove singularity, structurally stable A_2 catastrophe) -> RPA (M_max = 1.674, 38x above threshold) -> Turing (W = 1.9-3.2x, pairing coherence across wall) -> WALL (rho = 14.02, Z = 1.016, Eckart worst-case) -> BCS (E_cond = -0.115, unconditional for any g > 0 by 1D theorem).
- **What it gives**: BCS condensation OCCURS at the van Hove fold. Cooper pairs carry K_7 charge +/-1/2. The condensate breaks U(1)_7 spontaneously. The Bogoliubov quasiparticle spectrum is the candidate CDM.
- **What it does not solve**: WHY tau reaches the fold (no tau-stabilization mechanism), WHAT the 4D observer sees (transit dynamics), HOW n_s = 0.965 emerges.
- **Sessions**: S28 (KC chain), S32 (RPA PASS), S33 (TRAP PASS), S34 (corrected), S35 (unconditional)

### Door 2: Pure Mathematics Publications

- **What it is**: Twelve publishable standalone mathematical results that survive regardless of the framework's physical fate (permanent-results-registry.md Section I). Includes block-diagonality theorem, monotonicity theorem, algebraic traps, van Hove zero-critical-coupling, LZ retraction, Cl(8) bridge, Berry curvature vanishing, spectral Bianchi identity, 8D Petrov classification, spectral flow = 0 theorem, grading theorem, perturbative exhaustion.
- **What it gives**: JGP/CMP/JMP/PRD-level papers on spectral geometry of Dirac operators on compact Lie groups. New connections between NCG, Berry geometry, and Clifford algebra.
- **What it does not solve**: These are mathematical facts about D_K on SU(3), not cosmological predictions.
- **Sessions**: S7-S28 (accumulated)

### Door 3: SA Correlator Identity Breaking

- **What it is**: The spectral action two-point function chi_SA(K) = Sum W_{(p,q)}/(K^2 + C_2(p,q)) has 110% pole spread (C_2 from 1.33 to 9.33), qualitatively distinct from the Josephson phase propagator (0.051% pole spread). Goldstone's theorem does NOT protect it. The alpha_s = n_s^2 - 1 identity IS broken by chi_SA (deviation = 0.066, effective alpha = 0.86).
- **What it gives**: A structurally distinct correlator that escapes W7. The mixing of SA and Goldstone sectors at K < K* produces viable (n_s, alpha_s) pairs.
- **What it does not solve**: The K_pivot mapping (whether the physical CMB scale maps to K < K*). The SA correlator is also cutoff-dependent in its sector weights (S51 CUTOFF-CONV-51: alpha_eff stable at 4.7% variation, but identity deviation at 33% variation).
- **Sessions**: S50 cross-domain (discovery), S51 W1-D (cutoff convergence), S51 W2-A (mixing model)

### Door 4: sigma_8 = 0.799 (Observationally Viable Prediction)

- **What it is**: sigma_8 = 0.799 (framework), sitting between Planck (0.811 +/- 0.006) and lensing (~0.76 +/- 0.03). Within ~2.0 sigma of Planck and ~1.6 sigma of lensing.
- **What it gives**: A zero-free-parameter cosmological prediction that is observationally viable. If the sigma_8 tension between Planck and lensing persists, this prediction discriminates: it favors the lensing value.
- **What it does not solve**: sigma_8 is no longer the *sole* surviving observational prediction — n_s = 0.9590 (Door 8), m_H = 131.8 GeV (Door-S102-mH), Ω_DM h² = 0.120 (Door 13), A_s (Door-S118-As), Σm_ν (Window-25), and Ω_k (Window-26) are all now viable. **α_s** is the S92 scale-separated PAIR (Goldstone-pivot ≈0 = the CMB-channel value, 0.37σ vs ACT-DR4+Planck; substrate-distance −0.0858728 = BZ geometric floor, not CMB-comparable); the single-label +0.00117 (post-S85 RUNNING-NS-63) and −0.069 / "6–8σ" (K_pivot=2.0-era) readings are RETIRED — they conflated the two channels.
- **Sessions**: S50 W2-F (confirmed viable, S49 overestimate corrected by 14x); α_s re-pin S85

### Door 5: Leggett Dipolar Identification

- **What it is**: The Leggett mode on Jensen-deformed SU(3) maps to the Leggett frequency of superfluid 3He within 18%. Quality factor Q = 670,000 (all pair-breaking channels energetically forbidden). The Leggett mass is physical and undamped.
- **What it gives**: A concrete identification between internal BCS dynamics and known condensed matter physics. The ratio omega_L2/omega_L1 = phi_paasch at the crossing tau = 0.211686 (confirmed to 6 significant figures). This is a geometric identity connecting many-body BCS to single-particle Dirac spectral geometry.
- **What it does not solve**: The Leggett mass m_L = 0.070 M_KK is 170x below the mass required for n_s = 0.965.
- **Sessions**: S48 (identification), S49 (phi crossing), S50 W1-D/W1-E (Q factor and crossing confirmation)

### Door 6: Phi Crossing Geometric Identity

- **What it is**: At tau = 0.211686, the ratio of the two Leggett mode frequencies equals phi_paasch = 1.53158 to machine precision (4.4e-15). The ratio J_12/J_23 = 19.52 is algebraically constant. This is a pure geometric identity -- it connects the BCS collective dynamics (Josephson coupling ratio) to the Dirac eigenvalue ratio that defines phi_paasch.
- **What it gives**: A deep structural connection between the framework's two layers (single-particle geometry and many-body physics). Publishable as pure mathematics.
- **What it does not solve**: The physical significance of the crossing. It occurs at tau = 0.2117, close to but distinct from the van Hove fold at tau = 0.190.
- **Sessions**: S49 (discovery), S50 W1-E (confirmed 6 sig figs)

### Door 7: Acoustic Hawking Temperature

- **What it is**: T_acoustic agrees with T_Gibbs to 0.7% (zero free parameters). The 4D acoustic metric derived from the BdG sound speed on the tessellation fabric produces a Hawking-analogue temperature that matches the thermodynamic temperature from the Gibbs ensemble.
- **What it gives**: A non-trivial self-consistency check of the framework's thermodynamic structure. The acoustic Hawking temperature is determined by the BCS sound speed and the tessellation geometry, both of which are derived from D_K.
- **What it does not solve**: This is a consistency check, not a prediction.
- **Sessions**: S40

### Door 8: n_s = 0.9590 (committed) from Hubble Slow-Roll (S62, COMMITTED S67 functional-selection)

- **What it is**: KZ-NS-62 PASS. The spectral action S(tau) at the fold yields epsilon_H = (1/2)(dS/dtau)^2/(S·d^2S/dtau^2), n_s = 1 − 2·epsilon. **The functional is COMMITTED to the √x (Chamseddine–Connes) generating functional**: `n_s_FW_sqrt_cutoff = 0.9590`. Zero free parameters. **1.40σ Planck-alone; 4.73σ global anchor-ladder** (Šidák N=4). A distinct scheme, `n_s_framework = 0.9561` (constant-ε gauge-invariant, Row #55 FWD-C1), is kept separately.
- **What it gives**: A committed zero-free-parameter n_s. The functional-selection question (FUNCTIONAL-SELECT-67) is resolved at the **magnitude** level: Bayesian evidence excludes exp(−x) at 15.5σ and compact at 36.9σ, selecting the √x family as the unique surviving cutoff. Spectral index is occupation-invariant (Bogoliubov |β|² does not affect tilt).
- **What it does not solve**: The eps_H **sign-reversal** between cutoff families (√x red-tilt vs zeta/exponential blue-tilt) remains the structural floor — **W12 captures the sign-reversal** (atlas-04 Mechanism B = BROKEN-AT-SIGN + CONDITIONAL). The commit is to the √x family; the sign-level scheme-dependence is why Q40 (eps_H observational discrimination) stays LIVE-PENDING (CMB-S4/CMB-HD).
- **Sessions**: S62 W2-01 (KZ-NS-62), S65 (BCS dressing), S66 (functional crisis), S67 (FUNCTIONAL-SELECT commit)

### Door 9: CF-9 Algebraic Identity (PERMANENT, S62)

- **What it is**: BERRY-PROJECTION-62 PASS at machine epsilon (deviation < 2e-14). |A_coset|^2 = 3/2 + (3/2)e^{-4*tau} verified EXACTLY across tau = [0, 0.5]. The A-tensor (Berry curvature = NCG inner fluctuation = KK A-tensor) triple identification is an algebraic identity, not an approximation.
- **What it gives**: The quantitative bridge between three distinct mathematical frameworks (Berry geometric phase, NCG inner fluctuations, and KK dimensional reduction). The selection rule: 16/136,480 modes participate. The decomposition: u(1) component tau-independent (topological), su(2) component decays as e^{-4*tau}.
- **What it does not solve**: This is a structural identity, not a dynamical mechanism. It constrains the coupling between internal and external degrees of freedom.
- **Sessions**: S62 W1-02

### Door 10: Meissner Permanence Under GGE (NEW, S62)

- **What it is**: MEISSNER-GGE-62 PASS. D_s(GGE) = 6.283 M_KK^2, ratio D_s(GGE)/D_s(fold) = 0.9885. The superfluid weight survives the transit at 98.85% strength. Type-I classification preserved (kappa = 0.409 < 0.707). London penetration depth increases by only 0.6%. Five independent routes computed, all PASS.
- **What it gives**: The DM-SM decoupling mechanism (gauge boson Meissner mass) is permanent. The GGE non-thermality is key: a thermal state at the same effective temperature would have D_s = 5.45 (14% lower). Richardson-Gaudin integrability protects the condensate fraction.
- **What it does not solve**: The quantitative CDM abundance (requires transit rate). The f_DM fraction remains the sole bottleneck.
- **Sessions**: S62 W2-02

### Door 11: CDM by Construction

- **What it is**: CDM-CONSTRUCT-44 PASS. T^{0i}_4D = 0 exact (homogeneous creation). v_eff = 3.48e-6 c. The Bogoliubov quasiparticles from the transit are automatically cold and pressureless in 4D.
- **What it gives**: CDM without a dark sector Lagrangian. The quasiparticles are fiber-localized (no 4D spatial momentum), giving zero free-streaming length.
- **What it does not solve**: The CDM abundance (requires knowing the pair creation rate and transit dynamics quantitatively). The sigma/m ratio is 5.7e-51 cm^2/g (unobservably small self-interaction).
- **Sessions**: S42, S44

### Door 12: Volovik CC Relaxation — PASS 0.01 OOM (NEW, S66)

- **What it is**: DILUTION-CC-66 PASS (Scenario B). Volovik q-theory thermodynamic relaxation: rho_vac ~ M_Pl^2 H^2, tracking the expansion rate. Landing: rho_vac(today)/rho_obs = 1.032 (0.01 OOM from observation). The 114 OOM gap IS the expansion history itself, not a fine-tuning problem.
- **What it gives**: A CC mechanism that lands within 0.01 OOM of observation with zero tuning. The Volovik Gibbs-Duhem identity (rho_vac = epsilon(q) - mu*q -> 0 as q adjusts) is FUNCTIONAL-INDEPENDENT.
- **What it does not solve**: BBN constraint: rho_vac/rho_rad = 0.67 at nucleosynthesis (BBN-VOLOVIK-67). Status downgraded by S74 W4-W to scheme-locked (a_0-scheme drifts +1.87 OOM L=3→7; chi_2 = M_1/(N·lam_max) f*-scheme L_max-stable at -0.47 OOM); structural CC framework survives but PASS scheme-locked.
- **Sessions**: S66 W1-A; downgrade S74 W4-W

### Door 13: Leggett DM — 0.6% from Planck (NEW, S66)

- **What it is**: Leggett-only dark matter prediction: Omega_DM h^2 = 0.120 (observed: 0.1186 +/- 0.0020, 0.7 sigma). z_eq = 3425 (observed: 3402 +/- 26, 0.88 sigma). sigma/m = 0 (consistent with all direct detection nulls). lambda_fs = 9.85e-23 Mpc (22 OOM below WDM constraint).
- **What it gives**: A DM candidate with zero free parameters at 0.6% from Planck. The Leggett quasiparticle (inter-band coherence mode) is automatically cold, collisionless, and non-annihilating by construction. Five observational channels all PASS simultaneously.
- **What it does not solve**: Gravitational stability — the Leggett mode must be stable against gravitational decay (Gamma_grav < H_0). LEGGETT-GRAV-DECAY-67 is a CRITICAL S67 gate.
- **Sessions**: S66 (consolidated from S58 Volovik partition + S66 Leggett analysis)

---

## II-A. New Doors (S52-S88, session-keyed)

> **Provenance**: Session-keyed doors added 2026-05-09 per S88 atlas-uplift workshop. These are 14 additional doors closing constraints S52-S88 (former assumptions becoming proven; mechanism classes converted from open to permanently established). Sequential numbering interrupted at Door 13 (S66 era); session-keyed naming used for clarity.

| Door-id | What was constrained | Closing session | Registry / rule cite |
|:--------|:---------------------|:----------------|:---------------------|
| **Door-S58** | Volovik partition w_0 = -0.918 derivation; substrate compaction observable established as PRIMARY CC mechanism | S58 final synthesis | `falsifier-watchlist.md` w_0 row; `canonical_constants.py:1243`; `permanence-map.md` Pillar II anchor |
| **Door-S62** | n_s = **0.9590 committed** (√x cutoff; see Door 8) from Hubble slow-roll (KZ-NS-62 PASS); first viable n_s prediction in 62 sessions | S62 W2-01 (COMMITTED S67) | atlas-05 Door 8; `falsifier-master-inventory.md` row 1.a |
| **Door-S62-Meissner** | Meissner Permanence Under GGE; DM-SM decoupling permanent | S62 W2-02 | atlas-05 Door 10 |
| **Door-S62-CFq** | CF-9 Algebraic Identity (BERRY-PROJECTION-62 PASS); Berry/NCG/KK triple identification | S62 W1-02 | atlas-05 Door 9 |
| **Door-S66** | DILUTION-CC-66 PASS at 0.01 OOM (Volovik tracking); 114 OOM gap converted from open problem to expansion-history reading | S66 W1-A + Workshop 4 | atlas-05 Door 12; `framework-cc-oom.md` |
| **Door-S66-Leggett** | Leggett-only DM Omega_DM h² = 0.120 at 0.6% from Planck; 5 channels PASS | S66 (consolidated S58 + S66) | atlas-05 Door 13 |
| **Door-S70** | LEGGETT-MOMENT closing as Type-F (single-summand-projection trace) observable; algebra-INVARIANT classification; mechanically closed under §VII.U.2 4-corner rule | S70 era | `mechanical-closure-discipline.md §"Layer-separability carve-out"` |
| **Door-S86-3HeB** | 3He-B inheritance closing (rank-2 cocycle generators of ker(ι_*) characterized; 4-gate falsifier protocol pre-registered: Gate 1 NULL on F1+F2+F5; Gate 2 ratio 7.3250±0.1%; Gate 3 NULL on F3+F4; Gate 4 F4 multi-pressure slope) | S86 W-5 | `inheritance-falsifier-protocol.md`; §VII.AF.1 (`permanent-results-registry.md:14690`) |
| **Door-S86-JTP** | Joint Theorem Promotion Pathway closing as 4-stage MANDATORY structural rule; replaces ad-hoc multi-author cross-citation | S86 W-9 | `joint-theorem-promotion.md`; calibration corpus §VII.AH |
| **Door-S86-CPB** | Cross-pillar bridge closing as 5-anatomy + 3-level ladder MANDATORY at K=3; first registered bridge §VII.W (Pillar III ↔ Pillar IV). **§VII.W-3.LAB 3He-B/3He-A inheritance bridge promoted STAGE-3-PERMANENT** (S100a Stage-2 PASS-AND `S100a-VIIW3LAB-STAGE2-VERIFY`) — resolves atlas-05 Window-10 | S86 W-5 + S88 W4a-17 → STAGE-3 S100a | `cross-pillar-bridge-anatomy.md`; §VII.AF.1 + §VII.W-3.LAB |
| **Door-S87-S88** | α_s 11.31σ Tension + S50-51 Sign-AND-Magnitude Lock (under C1 identity α_s = n_s²−1; sign and magnitude are the SAME lock); Triple-Protection Reading at CMB pivot | S86 W-2 (mack+volovik+connes co-signed) | §VII.AB.1-§VII.AB.7 (`permanent-results-registry.md:14911-14982`) |
| **Door-S87-PathC** | Joint F_2-Class Path-(c) Theorem (lizzi+transit; 6-clause statement; 4 corrigenda); SOURCE-DOUBLE-CITE-CO-PRIMARY structure registered; STAGE-1-CANDIDATE per joint-theorem-promotion.md | S86 W-9 → S87 W9a-1 | §VII.AH (`permanent-results-registry.md:15522`) |
| **Door-S88-UniLock** | Universal Lock Condition (Substrate Horizon-Trigger Theorem) **STAGE-3-PERMANENT** (promoted S100a via 3-agent blind Stage-2 PASS-AND `S100a-VIIAM-STAGE2-VERIFY`); 3-clause joint theorem unifying J3 BH-horizon-pixelation-lock + S58 fold-effacement Γ_eff=0.99970 + W1b2-64 cascade-tail Page-time non-activation | S88 W1b2-65 → STAGE-3 S100a | §VII.AM (`permanent-results-registry.md`) |
| **Door-S88-WedderburnFrobenius** | Wedderburn-Artin Frobenius Rescue Class Theorem promoted STAGE-3-PERMANENT; A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) realizes the rescue class | S88 W4a-17 | §VII.W-3.ALGEBRAIC + §VII.W-3.SUBSTRATE (`permanent-results-registry.md:16590, 16657`) |

### New Doors (S89–S118)

> **Provenance**: 10 session-keyed doors added 2026-07-01 (S110→S118 uplift). Physics-foregrounded (cross-pillar bridges, observable route-pins, substrate BH structure). Meta/registry machinery compressed per campaign contract §2.

| Door-id | What was constrained / opened | Closing session | Registry / rule cite |
|:--------|:------------------------------|:----------------|:---------------------|
| **Door-S93-AU** | FWD-C1 **Pillar I ↔ Pillar II** bridge (spectral-action n_s ↔ Planck CMB) STAGE-3-PERMANENT — first Pillar I↔II cross-pillar bridge; CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class | S89 W7c land → STAGE-3 S93 W2-2 | §VII.AU.OP-PROJ; Stage-2 PASS-AND S92 §W5-4 ∧ §W5-5 |
| **Door-S95-BG** | α_s **Connes–Karoubi K₀-pairing transport bridge** at the a_4 Yang-Mills pole s=2 (substrate→CMB-pivot α_s transport) STAGE-3-PERMANENT | S95 W1-1 (`CF-S95-HK-1`) | §VII.BG; two-agent Stage-2 cross-axis PASS-AND |
| **Door-S96-BH** | **Topological sound-speed identity `c_s² = 0`** (Kasparov-product-factorization bridge), Layer-1/topology — the topological protection underlying the domain-wall GW closure (C2) | S96 W7-8 | §VII.BH (van-den-dungen author) *[full physical scope: confirm slot text]* |
| **Door-S96-BI** | Substrate → **horizon area law `S = A/4G_N`** (a_2 spectral-monotonicity → area law at two horizon types); substrate-first: the area theorem is Level-3 **EMERGENT**, not assumed | S96 W-3 NYT-Q7 | §VII.BI.OP-PROJ STAGE-1-CANDIDATE; PRIMARY + INDEPENDENT-CROSS-CHECK |
| **Door-S90-AW** | **Substrate-Clock-Uniqueness Theorem** — the substrate fold-time rate is structurally unique | S90 W2 CF-19 | §VII.AW.OP-PROJ |
| **Door-S101-H0** | **H₀ = 67.40 km/s/Mpc** anchor-ladder re-pin (G_N-ratio channel; spinor √16 = 4 EXACT; G_N^FW/G_N^obs = 1.000000). **Anchor value, NOT anchor-independent** (`H0_FW` not a registered canonical); NON-PROMOTION-BY-HELD-NUMBER lifted; 65.4 / 68.77 RETIRED | S100a (structural √16) + S101 W4-4 (magnitude) | `falsifier-master-inventory.md` Row #81; `falsifier-watchlist.md` H_0 |
| **Door-S102-mH** | **m_H = 131.8 GeV route-PINNED** — Route B KK-threshold DIRECT (a_4-moment correction to the \|S\|² fiber mode) canonical; Route A (KK-L5 Aitken) cross-check; 134.0 GeV tree. Resolves the m_H route ambiguity (supersedes Window-6) | S102 W4 | `m_H_FW_KK_threshold` |
| **Door-S106-gravastar** | Substrate BH interior = **Lobo dark-energy condensate (w ≈ −0.918), NOT a Mazur–Mottola de-Sitter gravastar**; the 8% departure from w=−1 IS the w0_FW prediction; core = supersonic **acoustic white-hole** interior (Mach=1 acoustic surface, not a GR metric horizon) | S106 bh-cosmo-incursion | `session-106/bh-cosmo-incursion/sub-gravastar-structure-landau.md` |
| **Door-S118-As** | **A_s closes ZERO-PARAMETER** — substrate sound speed `c_s = 0.5685` (a_2-curvature GGE fold) lands in the GS-1 window ⇒ A_s = 3.2994e-9 (regime-MARGINAL); FUNCTIONAL-PLURALISM-PERMANENT (S114), POINT type. A_s is **no longer "excluded"** | S118 W1-1 (`CF-S118-AS-CS-SUBSTRATE-FIRST` PASS ⭐) | `c_s_a2curv_GGE_fold = 0.5685294372…`; `A_s_FW` |
| **Door-S101-BN** | **Dual-Z₃ generation lever** — exact closed form `c(φ) = 1/(1+8cos²φ)` → {1/9, 1/3, 1/3}; **structurally lepton-only** | S100a W2-1 → S101 W6-2 | §VII.BN |

---

## II-B. Candidate Walls (S64-S66) — Not Yet Numbered

These structural results function like walls (they close classes of mechanisms) but have not been formally promoted to numbered wall status.

### R-Monotonicity (S64)

- **Statement**: dR/dtau >= 0 by AM-GM on volume-preserving Jensen deformation. Scalar curvature R increases monotonically, making a_2 diverge exponentially. CC via Jensen transit is structurally blocked because a_2 (gravity) grows faster than any polynomial correction.
- **Session**: S64 W1-A
- **Impact**: Closes CC Path C (Jensen transit). Establishes that on-Jensen deformations cannot reduce a_2.

### a_0/a_2 Trap (S64)

- **Statement**: Decreasing R (off-Jensen) INCREASES a_0/a_2. The CC ratio worsens when scalar curvature is reduced. This is the off-Jensen analog of the constant-ratio trap (W1) for the CC.
- **Session**: S64 W2-A
- **Impact**: Closes off-Jensen CC descent routes. The CC problem is structurally trapped in both directions.

### Frustration Triangle (S66)

- **Statement**: No single spectral centroid eta simultaneously satisfies n_s(red) + CC(small) + Mott(accessible). Three observational requirements pull in incompatible directions.
- **Session**: S66
- **Impact**: Establishes a structural tension between three observational channels. Resolution requires either the Volovik mechanism (decoupling CC from eta) or functional selection (choosing the centroid by other means).

### Frozen Spectrum Theorem (S79 C12; W11-candidate-pre-promotion)

- **Statement**: Substrate spectrum invariant under transit at machine precision **10^{-113}**. Wall-class candidate.
- **Session**: S79 C12 (connes + lizzi)
- **Impact**: Closes any mechanism requiring spectrum drift through the fold; substrate spectral rigidity is an exact theorem at machine precision.

### Alternative-Greybody No-Go (NEW, S118 W1; WALL-STRENGTHENED-4-CLASS-EMPIRICAL — full proof pending S119)

- **Statement**: The alternative greybody-factor construction (an off-substrate route to the emission/A_s normalization) FAILs across 4 classes as a pre-registered empirical wall (`CF-S118-ALT-GREYBODY-WALL` FAIL). Full no-go proof queued as `CF-S119-GREYBODY-NOGO-PROOF`.
- **Session**: S118 W1
- **Impact**: Empirically closes the alternative-greybody corridor; the substrate-first A_s closure (`c_s = 0.5685` ⇒ A_s zero-parameter, Door-S118-As) is the surviving route. *[physical scope from S118 verdict-index; confirm against `session-118-w1-workingpaper.md` before promotion to numbered wall.]*

---

## III. Windows (Conditional Routes)

Each window has a specific condition that determines whether it opens or remains shut.

### Window 1: SA-Goldstone Mixing at K < K* (THE decisive window)

- **Condition**: The physical CMB pivot k = 0.05 Mpc^{-1} must map to K_fabric < K* = 0.087 M_KK. This requires >= 3.1 e-folds of expansion from the stiff epoch, obtainable from tau_i <= 1.7e-5 (0.009% of tau_fold).
- **What computation decides it**: EFOLD-MAPPING-52 -- compute the full expansion history from tau = 0 to present, including stiff epoch, transit, GGE relic epoch, and transition to radiation domination. Extract the physical K_pivot mapping from total e-folds.
- **Current status**: PRELIMINARY PASS. S64 quantified physical transit e-folds: N_e = 3.73e-3. E-fold estimate gives N_e = 3.3 from tau_i = 10^{-5} (margin 0.2). The natural initial condition (near-round metric) gives tau_i << 10^{-5}, providing ample margin. But the computation is approximate (stiff-epoch w = 1 assumed, no backreaction).
- **If PASS**: SA-Goldstone additive mixing produces n_s = 0.965 with beta > 0.9 and alpha_s in [-0.040, 0]. The identity IS broken at K < K*. The framework's n_s prediction survives.
- **If FAIL**: All cosmological predictions are excluded. The mathematics survives as pure spectral geometry.
- **Depends on**: W9 (convex combination theorem establishes the K_pivot threshold), S51 W2-A (mixing model parametrics)

### Window 2: Q-Theory CC Crossing -- CLOSED (S62)

- **Previous condition**: Physical pair number N >= 2 at the fold for q-theory self-tuning.
- **S62 verdict**: CC-QTHEORY-GGE-62 **FAIL**. Monotonicity theorem: dE_ZP/dq = (1/4) sum (2N_n + 1) d_n / omega_n(q) > 0 for ALL q > -lambda_min^2. No interior equilibrium exists.
- **Structural conclusion**: CC problem = integrability problem. The BCS transit creates Richardson-Gaudin conserved integrals that lock GGE occupations.
- **This window is permanently CLOSED.** Resolution required Volovik tracking (Door 12 / W11).

### Window 3: Off-Jensen 5D Moduli Landscape — SUBSTANTIALLY CLOSED (S76 W2-J)

- **Previous condition**: The full 5-parameter U(2)-invariant moduli space must contain a saddle point, minimum, or topologically nontrivial feature not accessible on the 1-parameter Jensen line.
- **S76 verdict**: W2-J off-Jensen 5D moduli Hessian + ridge dynamics: **35D restoring potential**, ridge-confined trajectories. Mechanism D substantially closed (atlas-04 row D). The Off-Jensen excursion question is resolved: confined ridge, not free landscape.
- **Status**: SUBSTANTIALLY CLOSED. Residual carry-forward: T4 instability at boundary (eigenvalue -9.9 at tau = 0.60, eps = +0.15).

### Window 4: Higher PW Truncation Spectrum

- **Condition**: Eigenvalues at max_pq_sum = 30 must reach 12 M_KK. The scaling law (S51 HIGH-PW-51) gives max|lambda| = 0.633*sqrt(C_2) + 0.555, predicting R = 12.05 M_KK at N = 30.
- **What computation decides it**: Weight-space irrep construction (avoiding the exponentially large tensor-product-then-project algorithm).
- **Current status**: INFO. S51 computed N = 8 (spectral radius 3.92 M_KK). N = 30 computationally accessible but not implemented.
- **Depends on**: S51 HIGH-PW-51 (scaling law), computational implementation of weight-space algorithm

### Window 5: Strutinsky Shell Correction to chi_SA

- **Condition**: The shell correction to the SA susceptibility chi_SA = d^2S/dtau^2 is 49% of the smooth part (S51 STRUTINSKY-51). If the shell structure at higher PW truncation changes the balance, the effective n_s from the SA sector could shift.
- **Current status**: FAIL at current truncation (n_s_smooth = -0.80 at Lambda = 12 M_KK).
- **Depends on**: Window 4 (higher PW truncation required)

### Window 6: KK Threshold Corrections for Higgs Mass (NEW, S62)

- **Condition**: The KK-threshold correction to the |S|² fiber-embedding mode fixes m_H from the a_4 Yang-Mills+Higgs-quartic moment.
- **Current status**: **ROUTE-PINNED S102 (Door-S102-mH)** — `m_H = 131.8 GeV` via Route B (KK-threshold DIRECT, `m_H_FW_KK_threshold`); Route A (KK-L5 Aitken) is the cross-check; 134.0 GeV tree. The framework **commits** to 131.8 GeV (5.4% above observed 125.1) as the substrate prediction — this is a zero-parameter output, not a fit to 125.1. (The earlier 127.5 GeV Aitken / "160 GeV 2-loop / match-to-125.1" framing is SUPERSEDED.)
- **Depends on**: `a_4_FW_zeta` (S75), `s66_kk_threshold_l5_results.txt`

---

## III-A. New Windows (S52-S88)

> **Provenance**: Session-keyed windows added 2026-05-09 per S88 atlas-uplift workshop. 18 new windows opened S52-S88 (~3× the pre-S52 inventory). Of these: 8 computational (0-yr horizon), 4 short-horizon observational (1-4 yr), 6 long-horizon (5-9 yr).

| Window-id | Conditional-PASS condition | Falsifier protocol | Detection horizon | Current status |
|:----------|:---------------------------|:-------------------|:-------------------|:----------------|
| **Window-7** | FUNCTIONAL-SELECT-67: which spectral functional generates n_s? **COMMITTED** — the √x (Chamseddine–Connes) family is selected (Bayesian evidence excludes exp(−x) at 15.5σ, compact at 36.9σ); `n_s = 0.9590` canonical (Door 8). Residual: sign-level scheme-dependence (W12) stays LIVE-PENDING as Q40 | resolved at magnitude level; sign-axis → CMB-S4/CMB-HD | 0 yr (magnitude COMMITTED; sign-axis observational) | **COMMITTED (√x); sign-axis LIVE-PENDING** |
| **Window-8** | BBN-VOLOVIK-67: Volovik tracking vacuum at z~10^9; rho_vac/rho_rad = 0.67 at nucleosynthesis | S67 carry-forward | 0 yr (deferred since S67) | partial PASS at S72 audit; xcorr cross-channel OPEN since S85 W4 |
| **Window-9** | TRANSIT-PS-67: transit power spectrum vs A_s mismatch; α_s prediction adjudication | S67 carry-forward | 0 yr (deferred since S67) | n/a (computational gate) |
| **Window-10** | Cross-pillar K=3 Stage-2 verify: §VII.W-3.LAB STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion via blind cross-axis PASS-AND | **RESOLVED S100a** (`S100a-VIIW3LAB-STAGE2-VERIFY` Stage-2 PASS-AND) → §VII.W-3.LAB **STAGE-3-PERMANENT** (Door-S86-CPB) | 0 yr — DONE | **RESOLVED (computational gate closed S100a)** |
| **Window-11** | 3He-B vortex spectroscopy (W11-C5): Caroli-Matricon ladder asymmetry at φ_67-clean; Gate 1 NULL on F1+F2+F5; Gate 2 ratio 7.3250±0.1%; Lancaster MCT-3 / Helsinki ROTA cells | `inheritance-falsifier-protocol.md` 4-gate; FAIL on any non-NULL detection on F1/F2/F5 OR ratio outside band | ~5 yr (MCT-3 horizon 2026-2031) | not yet observed (lab-falsifier; SI value 58.9589 MHz at SW1) |
| **Window-12** | LISA Ω_GW — **amplitude leg RETIRED (S96)**: the broken U(1)_7 vacuum manifold is connected (π₀(U(1))=0) ⇒ **Ω_GW walls = 0 EXACT**; (C)-null is structural, not a live 11-OOM forecast. Peak GW is detector-sterile (8.48e39 Hz). Falsifier **migrated GW → LSS** (see Window-27) | `falsifier-master-inventory.md` (GW rows down-tagged; LSS Rows #71/#72) | — (GW-detector-sterile) | **RETIRED (not a live GW forecast; superseded by LSS f·σ₈)** |
| **Window-13** | LiteBIRD n_T (decisive 4.250σ): Path-H r=0.00745 vs Path-C r=0.0117 internal-consistency split (36.3% Path-C-relative); LiteBIRD 4.250σ decisive over BK-Array 2026 1.417σ marginal | `falsifier-master-inventory.md` row #2; Path-H/Path-C internal-consistency adjudication | ~4 yr (LiteBIRD 2030) | 4.250σ decisive |
| **Window-14** | DESI DR3 w₀-wₐ: framework prediction w_0 = -0.918 (canonical) or -0.842454 (R_842 branch-(iv)) vs LCDM w_0 = -1.0; post-Dovekie 2.130σ for canonical, 0.731σ for branch-(iv) | `falsifier-watchlist.md` w_0 row; null result w_0 = -1.000 ± 0.015 closes Volovik-partition branch at ~5σ | ~1 yr (DESI DR3 2027) | **w₀ = −0.918 @ 2.13σ** canonical / 0.731σ R_842 (post-Dovekie); **wₐ = 0 (triple-locked) @ 3.43σ** vs DESI DR2 (post-Dovekie tightening from 2.92σ; framework fixed, data moving away). **R_842 binding NOT yet triggered**: DR3 IS the binding instrument, not the DES-Dovekie DR2 reanalysis. |
| **Window-15** | CMB-S4 α_s (S92 scale-separation): framework CMB-channel prediction is the Goldstone-pivot running α_s ≈ 0 (`alpha_s_pivot_goldstone`, P_∇φ=K⁰ at pivot); the substrate-distance (BZ) −0.0858728 (`alpha_s_substrate_distance_1`) is NOT CMB-detector-comparable (geometric floor). Single-label +0.00117 (S63 RUNNING-NS-63) / −0.069 (pre-S85) RETIRED (channel conflation) | `falsifier-watchlist.md` α_s row; CMB-S4 PASS if α_s consistent with ≈0 (pivot band), FAIL if a nonzero central is confirmed at high σ | ~4 yr (CMB-S4 2030) | Goldstone-pivot ≈0 vs ACT-DR4 (Aiola+ 2020) +0.0023 ± 0.0063: 0.37σ; vs Planck −0.0045 ± 0.0067: 0.67σ — essentially indistinguishable from ΛCDM. |
| **Window-16** | CMB-HD α_s: tighter σ than CMB-S4; same canonical prediction as Window-15 (Goldstone-pivot ≈0, CMB channel) | `falsifier-watchlist.md` α_s row; redundant with Window-15 but instrument-distinct | ~9 yr (CMB-HD 2035) | pivot ≈0 indistinguishable from ΛCDM; CMB-HD's tighter σ is the sharpest test for a nonzero pivot-channel running |
| **Window-17** | Hyper-K proton lifetime: framework prediction ~10^36 yr (one-parameter from M_KK); current bound ~10^35 yr at Hyper-K Yr-10 | `falsifier-watchlist.md` proton_lifetime row | ~9 yr (Hyper-K 2030s) | one-sided lower-bound test |
| **Window-18** | g_1/g_2 RGE convergence: framework prediction 0.684 at τ=0.19; observed 0.709; 3.5% below — pending RGE running refinement | `falsifier-watchlist.md` g_1/g_2 row | 0 yr (computational; refinement queued) | LIVE (observational uncertainty dominates) |
| **Window-19** | H_0 spinor-factor resolution: factor √16 = 4 EXACT RESOLVED (S100a, `S100a-H0-SPINOR-FACTOR` PASS, Q27); magnitude RE-PINNED S101 W4-4 (`S101-H0-PROPER-A2` PASS, audit `cd8e8c0b125a…`) to **H_0 = 67.40 km/s/Mpc** via the G_N-ratio channel (G_N^FW/G_N^obs = 1.000000, N = 0.999859) WITH the anchor-degeneracy disclosure (NOT anchor-independent H_0; 65.4 RETIRED). NON-PROMOTION-BY-HELD-NUMBER LIFTED; anchor-independent H_0 → CF-S102-H0-ANCHOR-INDEPENDENT | `falsifier-watchlist.md` H_0 row + `falsifier-master-inventory.md` Row #81 | 0 yr (computational; structural leg + magnitude both resolved S100a/S101) | LIVE — FLAGSHIP (re-pinned S101) |
| **Window-20** | 3He-A NMR sweet-spot (SW1): 58.9589 MHz at λ_6 direction; detection_ratio 58958.86 over σ_detect 0.001 MHz; LAB-FALSIFIER-A class | `falsifier-master-inventory.md` row #13 + lab-falsifier suite §13-21; 5-yr decision tree pointer `s86_w11_lab_falsifier_evoi_tree.json:rows[0]` | ~5 yr (2031 per W11-C6 EVOI ladder) | lab-falsifier (P_decisive 0.30-0.50) |
| **Window-21** | FeSe NMR sweet-spot (SW2): 364.5177 ppm at λ_7 direction; detection_ratio 72.90 over σ_detect 5.0 ppm | `falsifier-master-inventory.md` row #14 | ~5 yr (2031) | lab-falsifier |
| **Window-22** | 173Yb optical-lattice sweet-spot (SW3, **UNIQUE λ_8 channel**): 1.4250 s^{-1} at λ_8 direction; **FAIL-AT-LAB on SW3 is the framework's strongest single-row substrate-direction-falsification trigger** | `falsifier-master-inventory.md` row #15 | ~5 yr (2031) | lab-falsifier (single λ_8 measurement) |
| **Window-23** | f_NL_folded laboratory-IN observable (CMB / 21-cm bispectrum): 3-pathway GGE-coupling discriminator with pin range [0.0547, 0.7685] (~14× span); SUBSTRATE-IS counterpart at φ_3 ∈ HC^3(A_K) is Window-24 | `falsifier-master-inventory.md` row #9a (LAB-IN) + #9b (SUBSTRATE-IS); CF-28 split | ~9 yr (CMB-S4 σ=6.9 / SKA-1 σ~0.15 in 2035s) | n/a (forecast pending) |
| **Window-24** | φ_3 substrate cocycle in HC^3(A_K) (rank-3 Hochschild; 3-pt-connected vertex): substrate-IS structural anchor for laboratory-IN Window-23; HKR-bridge image; analytic-extrapolation 1.0e-6 at L_max=10 | CF-25 STAGE-1-CANDIDATE; Level-3/Level-2 = 1/L = 0.10 universally (LQT rank-inheritance) | 0 yr (substrate-side; STAGE-1-CANDIDATE pending Stage-2 verify) | n/a (computational gate) |

### New Windows (S89–S118)

| Window-id | Conditional-PASS condition | Falsifier | Detection horizon | Current status |
|:----------|:---------------------------|:----------|:------------------|:---------------|
| **Window-25** | **Σm_ν neutrino mass sum**: substrate type-I seesaw (m_ν = −m_Dᵀ M_R⁻¹ m_D; M_R = D_K B-branch fold energies on M₃(ℂ)) ⇒ **Σm_ν = 0.0582 eV**; normal ordering B1<B2<B3 (machine-ε) | DESI-2024 (arXiv:2404.03002) **Σm_ν < 0.072 eV** 95% CL (external) | ~1–4 yr (DESI DR3 / CMB-S4) | **PASS** (0.0582 < 0.072); FAIL if the cosmological bound tightens below ~0.058 eV | S96/S99 |
| **Window-26** | **Ω_k spatial flatness**: zero-free-parameter Ω_k = 0 | CMB+BAO flatness constraint | 0 yr (computational; observationally sharpened) | **PASS (0.368σ, S117)** |
| **Window-27** | **LSS f·σ₈ growth** — the GW→LSS-migrated falsifier: after the GW-amplitude retirement (Window-12) this is the **#1 non-CMB falsifier** | `falsifier-master-inventory.md` Rows #71/#72 | growth-survey horizon (DESI / Euclid / LSST, ~2027–2032) | **LIVE — #1 non-CMB falsifier** |

**Window detection-horizon urgency (Sagan-empiricist flag)**: **Window-14 (DESI DR3 2027)** remains the framework's nearest decisive observational test, now joined by **Window-27 (LSS f·σ₈ growth)** as the #1 non-CMB falsifier following the GW-amplitude retirement (Window-12). Resolved since the S88 snapshot: **Window-7 COMMITTED** (√x functional; n_s=0.9590), **Window-10 RESOLVED** (§VII.W-3.LAB STAGE-3 S100a). Windows-8/9 (BBN-VOLOVIK / TRANSIT-PS) remain computational carry-forwards. *(A cross-framework spectral-dimension discriminator — substrate d_s(σ_*≈1.4005 M_KK⁻²) vs CDT/asymptotic-safety, S92 — is tracked as a candidate comparison, not an instrument falsifier.)*

---

## IV. Cross-Reference: Walls vs. Doors (extended)

| Wall | Doors it DOES NOT block | Explanation |
|:-----|:------------------------|:------------|
| W1 (F/B ratio) | Door 1 (BCS chain) | BCS operates in the IR near the van Hove fold, not in the UV where W1 holds |
| W2 (block-diagonal) | Door 1 (BCS chain) | BCS Hamiltonian couples sectors through the many-body V matrix, not through D_K |
| W3 (spectral gap) | Door 1 (BCS chain) | Van Hove divergent DOS triggers BCS through the 1D theorem, not through a Fermi surface |
| W4 (monotonicity) | Door 3 (SA correlator), Door 8 (n_s) | SA correlator uses derivatives of S; Hubble SA uses curvature ratio, not S value |
| W7 (identity) | Door 3 (SA correlator), Door 8 (n_s) | SA correlator has K^{-alpha} with alpha != 2; Hubble SA bypasses the Josephson sector |
| W9 (convex combination) | Window 1 (K < K*) | The bound is K-dependent; at K < K*, both correlators are flat |
| W11 (Volovik CC tracking) | Door 12, Door-S58, Door-S66 | The wall converts CC fine-tuning interpretation to expansion-history reading; the doors ARE the same mechanism's mechanistic + registry anchors |
| W12 (eps_H sign reversal) | Door-S62, Door 8 | Door 8 / Door-S62 carry the n_s prediction; W12 is the SCHEME-DEPENDENT caveat — doors NOT blocked, only conditioned on FUNCTIONAL-SELECT-67 |
| W14 (algebra-axis orthogonality) | Door-S87-PathC, Door-S88-UniLock | These doors are joint-theorem STAGE-1-CANDIDATEs; W14 is the underlying structural constraint they obey, not a blocker |
| W18 (Type-F/Type-S layer-separability) | Door-S70 (Leggett Type-F) | LEGGETT-MOMENT closes as Type-F (algebra-INVARIANT); the wall admits Type-F closure under L1-L4 conditions |
| W19-W21 (methodology walls) | All substrate-physics doors | Methodology walls operate at the layer-functor F image (methodology side); they bind plan-freeze admissibility, not substrate-physics doors |
| All walls | Door 9 (CF-9 identity) | Pure algebraic identity; immune to all dynamical constraints |
| All walls | Door 10 (Meissner GGE), Door-S62-Meissner | Meissner permanence follows from Richardson-Gaudin integrability, not spectral action |

---

## V. The Constraint Surface Diagram (S88 snapshot; S89–S118 deltas in §I/§II-A/§III-A)

```
CLOSED (by wall)                              OPEN (conditional)                 PERMANENTLY OPEN
=================                             ==================                 ================

W1: All perturbative                          Window 1: SA-Goldstone at K<K*    Door 1:  BCS chain (5/5)
    F/B-dependent (6 mech)                    Window 4: Higher PW truncation    Door 2:  Pure math
W2: Cross-sector D_K (3 mech)                 Window 5: Strutinsky at high PW   Door 3:  SA correlator
W3: All mu=0 BCS (5 mech)                     Window 6: KK threshold m_H        Door 4:  σ_8 = 0.799
W4: All spectral action                       Window 7: FUNCTIONAL-SELECT-67    Door 5:  Leggett dipolar
    tau-stabilization (13+ mech)              Window 8: BBN-VOLOVIK-67          Door 6:  Phi crossing
W5: Berry curvature topological               Window 9: TRANSIT-PS-67           Door 7:  Acoustic T_H
W6: NCG-KK scale identification               Window 10: Cross-pillar K=3 Stage-2 [RESOLVED S100a] Door 8:  n_s = 0.9590
W7: Josephson-sector n_s (3 mech)             Window 11: 3He-B vortex spectro    Door 9:  CF-9 identity
W8: Anderson-Higgs U(1)_7 (1 mech)            Window 12: LISA Ω_GW (CGWB) [RETIRED→LSS]       Door 10: Meissner GGE
W9: Additive mixing K=2.0 (1 mech)            Window 13: LiteBIRD n_T 4.250σ     Door 11: CDM by construction
W10: Zero-mode protection (2 mech)            Window 14: DESI DR3 (2027)        Door 12: Volovik CC PASS
W11: Volovik CC fine-tuning interp            Window 15: CMB-S4 α_s             Door 13: Leggett DM 0.6%
W12: eps_H sign-reversal scheme-dep           Window 16: CMB-HD α_s             Door-S58: Volovik partition w_0
W13: F_4-MB Pillar-III multiplier             Window 17: Hyper-K proton         Door-S62: KZ-NS-62 first n_s
W14: Algebra-axis orthogonality K=3           Window 18: g_1/g_2 RGE            Door-S62-Meissner: Meissner perm
W15: Cross-corner co-primary chains           Window 19: H_0 spinor factor      Door-S62-CFq: CF-9 BERRY
W16: Layer-2-non-binding bare-decomp          Window 20: 3He-A NMR SW1          Door-S66: DILUTION-CC PASS
W17: η-only HP^1 detection                    Window 21: FeSe NMR SW2           Door-S66-Leggett: Ω_DM 0.6%
W18: Type-S mech-closure silently             Window 22: 173Yb optical SW3      Door-S70: LEGGETT-MOMENT
W19: PRU 8.0-8.6 plan-author paths            Window 23: f_NL_folded LAB-IN     Door-S86-3HeB: Inheritance
W20: Joint-theorem single-axis prom           Window 24: φ_3 SUBSTRATE-IS       Door-S86-JTP: Joint 4-stage
W21: Cross-pillar 5+3 ad-hoc                                                    Door-S86-CPB: Cross-pillar K=3
                                              CLOSED WINDOWS                    Door-S87-S88: α_s sign-mag lock
                                              ==============                    Door-S87-PathC: Joint F_2-class
                                              Window 2: Q-theory CC             Door-S88-UniLock: Universal Lock
                                                  (PERMANENTLY CLOSED)          Door-S88-WedderburnFrobenius
                                              Window 3: Off-Jensen 5D moduli
                                                  (SUBSTANTIALLY CLOSED via     CANDIDATE WALLS (II-B)
                                                   S76 W2-J 35D restoring)      ======================
                                                                                R-Monotonicity (S64)
                                                                                a_0/a_2 Trap (S64)
                                                                                Frustration Triangle (S66)
                                                                                Frozen Spectrum 10^{-113} (S79)
```

> **Note**: the ASCII diagram above is the **S88 snapshot**. S89–S118 deltas (below) are not re-drawn into the columns; consult §I (walls W23-W25), §II-A (New Doors) and §III-A (New Windows) for the current cells.

**S118-current assessment**: 25 numbered walls / 37 doors / 27 windows (26 OPEN + 1 permanently CLOSED). The S89–S118 arc added three substrate-physics walls (**W23** superalgebra-extension obstruction, **W24** recursive-Casimir Yukawa-SHAPE wall, **W25** one-loop effective-action monotonicity closing the last variational τ-selection corridor) plus the empirically-strengthened greybody candidate wall. It opened the first **Pillar I↔II** and **α_s a_4-transport** cross-pillar bridges (Doors-S93-AU / S95-BG), the substrate→area-law bridge (Door-S96-BI), the **BH-interior = acoustic-white-hole / Lobo dark-energy condensate** identification (Door-S106-gravastar), and **route-pinned three flagship observables** — m_H = 131.8 GeV (Door-S102-mH), H₀ = 67.40 anchor-ladder (Door-S101-H0), and A_s zero-parameter via c_s = 0.5685 (Door-S118-As). Two S88 STAGE-1 doors promoted to STAGE-3-PERMANENT (Universal Lock §VII.AM; 3He-B inheritance §VII.W-3.LAB) and two observable questions RESOLVED (Window-7 √x functional commit; Window-10 cross-pillar Stage-2). The single largest **removal**: the LISA Ω_GW amplitude leg is RETIRED (walls = 0 EXACT, π₀(U(1))=0) — the falsifier **migrated GW→LSS** (Window-27 f·σ₈ growth is now the #1 non-CMB test). **Window-14 DESI DR3 (2027)** remains the nearest decisive observational test. New viable observables: Σm_ν (Window-25, PASS), Ω_k flatness (Window-26, PASS), n_s = 0.9590 committed (Door 8, 1.40σ Planck-alone).

---

*Compiled from: permanent-results-registry.md, constraint-mega-matrix.md, atlas-01-session-timeline.md, atlas-02-mechanism-lifecycle.md, atlas-04-assumptions.md, atlas-06-probability-trajectory.md, falsifier-master-inventory.md, falsifier-watchlist.md, cross-pillar-bridge-anatomy.md, joint-theorem-promotion.md, mechanical-closure-discipline.md, registry-landing.md, regulator-pin-discipline.md, epistemic-discipline.md, framework-cc-oom.md, session working papers S39-S88, MEMORY.md. This document is the authoritative structural landscape — walls block, doors open, windows depend on one computation. Updated 2026-05-09 (S52-S88 uplift; 11 new walls W11-W21, 14 new session-keyed doors, 18 new windows Window-7..24); **2026-07-01 (S110→S118 uplift; S119-current: +3 substrate walls W23-W25 + greybody candidate, +10 session-keyed doors S89-S118, +3 windows Window-25..27; STAGE-1→STAGE-3 promotions §VII.AM/W-3.LAB; Windows-7/10 resolved; LISA Ω_GW amplitude leg RETIRED — falsifier migrated GW→LSS). Canonical value-set per campaign contract §6; per-session detail in `_uplift-S119-materials/30-closures-walls-S89-S118.md`.**\*
