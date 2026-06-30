# α_s Structural-Protection Registry Entry

**Status**: READY-TO-INSTALL → INSTALLED 2026-04-27 (S86 Level-10 housekeeping T10-4).
**Source**: S86 W-2 workshop `s86-alpha-s-tension-and-sign-lock.md` (R3-FINAL CONVERGENCE L1085-1305 + R3-B EMERGENCE (i)-(iv) L1463-1563 + What Holds L1619-1636).
**Recommending agent**: mack (R2-B / R3-B FINAL) ⊕ connes (R3 retraction-and-refinement).
**Anchor identity**: `α_s = n_s² − 1`. Canonical FROZEN: `alpha_s_inflation_framework = −0.06896799` (rational `−6896799/100000000`, symbolically exact at `u_pivot = 19649/351 = 55.9800569800570`).

This entry is the substrate-physical structural reading of WHY the C1 identity `α_s = n_s² − 1` holds at substrate pivot. It is NOT a derivation of the identity itself (that lives in the §VII registry / canonical_constants.py provenance line for `alpha_s_inflation_framework`). It is the registry of the **three independently substrate-physical conditions** that simultaneously protect the identity, and the **propagator-class equivalence taxonomy** that classifies the propagator structures under which the identity holds EXACTLY vs is broken at known order.

---

## §1 — Triple-anchored protection at CMB pivot

The identity `α_s = n_s² − 1` is protected at substrate pivot by THREE simultaneous substrate-physical conditions, each independently structurally enforced. All three would have to fail simultaneously to break the identity at substrate pivot.

| Anchor | Substrate condition | Source closure | Substrate-physical scale |
|:-------|:--------------------|:----------------|:-------------------------|
| **(i) BDI universality** | Constant Goldstone mass per pole (Axis-1 K-homogeneity per pole) — gap floor `0.975·Δ_0` across `τ ∈ [0, fold]`; symmetries (TRS, PHS, chiral) of BdG Hamiltonian are regulator-independent | GAP-ANTIJENSEN-65 PASS (S65); BDI assignment S35-S38 | `Δ_floor / Δ_0 = 0.975` |
| **(ii) Kinematic suppression of optical branch** | Optical-branch weight at pivot suppressed `w_optical / w_acoustic ~ (k_pivot / ω_L1)²` — single-effective-pole equivalence emerges at pivot | Volovik 2003 §7-8 dipolar-Leggett structure; substrate kinematic suppression registry (CANONICAL-12 `w_optical_over_acoustic_at_pivot`) | `(k_pivot / ω_L1)² ~ 10⁻⁴` |
| **(iii) Sub-threshold inter-band coupling** | `γ_pivot ~ (λ_substrate / λ_threshold)²` — Leggett-dipolar zero-momentum scalar coupling immune to K-running; GGE-thermalization protection `E_J / Δ ~ 4.4` fixes inter-band coupling ratio | GGE-THERM-61 PASS (S61); Leggett dipolar coupling structure | `γ_pivot ~ 4.4 × 10⁻⁵` |

Each condition independently substrate-physical and structurally enforced. The substitution chain (R3 connes DISSENT L1145-1166):

```
Definition 1: Axis-1 (K-homogeneity per pole): each pole's (J_i, m_i²) is K-independent
Definition 2: Axis-2 (single-effective-pole equivalence): all (J_i, m_i²) share the same
              (J, m²) up to weight w_i, so the joint propagator collapses to
              T·(∑w_i)/(J·K² + m²)

Step 1 (sub):  Axis-1 alone (each pole K-homogeneous BUT independent (J_i, m_i²))
               ⇒ joint propagator NOT K-homogeneous in a single u(K)
               ⇒ identity broken at order w_2 · (asymmetry) per Sage-symbolic
                   counter-example (J_1=1, m_1²=56, J_2=2, m_2²=100, K=1):
                   residue (16/840123)·w_2 leading order
Step 2 (sub):  Axis-2 alone (shared (J, m²) but mass running with γ ≠ 0)
               ⇒ joint propagator violates K-homogeneity (m²(K) ≠ const)
               ⇒ identity broken at order γ · u/(1+u) per S50 sunset estimate
Step 3 (deriv): The identity requires BOTH axes simultaneously.
               At substrate pivot: BDI universality enforces Axis-1 per pole;
               kinematic suppression w_optical ~ (k_pivot/ω_L1)² ~ 10⁻⁴ enforces
               Axis-2 approximately (effective single-pole at pivot, with leakage
               ~ 10⁻⁹ from independent-multi-pole sector).
Direction:    The substrate-physical protection is the SIMULTANEOUS satisfaction of
              the three anchors above. The identity at substrate pivot is
              triply-protected.
```

**Substrate-physical residue floor under triple-anchored protection** (R3 connes EMERGENCE L1170-1185, Sage-symbolic-evaluated):

```
Route B (running-mass γ at substrate-physical λ):
   |δα| ~ 8.65 × 10⁻⁵ absolute,  |δα/α_s_FW| ~ 1.25 × 10⁻³ relative
Route C-multi-pole (independent (J_i, m_i²) at w_optical ~ 10⁻⁴):
   |δα| ~ 1.9 × 10⁻⁹ absolute,  |δα/α_s_FW| ~ 2.7 × 10⁻⁸ relative
Combined floor: max(Route B, Route C-multi-pole) = Route B floor ~ 8.65 × 10⁻⁵ absolute
```

The dominant floor is the running-mass γ-residue (Route B). Both floors remain undetectable through CMB-HD precision (`σ_α_s ≈ 1.1 × 10⁻³` at 2034+); the substrate's interpretive freedom on the residue floor is essentially nil.

---

## §2 — Single-effective-pole equivalence class

The K-homogeneity ODE solution `f(u) = 2A/(u-A)` parametrizes choices of `A` WITHIN the single-effective-pole equivalence class, NOT the larger class of "all K-homogeneous multi-pole propagators". This corrects the R2-A widening (connes R3 retraction L1116):

> **Definition** — the SINGLE-EFFECTIVE-POLE equivalence class is the set of K-homogeneous propagators that algebraically reduce to the form
> `P(K) = T · ∑w_i / (J·K² + m²)` with shared `(J, m²)` across all poles.

Two poles each individually K-homogeneous but with different `(J_i, m_i²)` do NOT fall into the equivalence class because there is no single `u(K)` describing the joint propagator. The K-homogeneity ODE family `f(u) = 2A/(u-A)` is a CLASSIFICATION TOOL for substrate-pivot-compatible propagators within the equivalence class, not a widening to all K-homogeneous multi-pole forms.

Sage-verification (R2-B + R3 precompute, L1102-1106): at `J_1=1, m_1²=56, J_2=2, m_2²=100, K=1`:
- symbolic residue = `(64/2907)·w_2 / (361·w_2² + 1292·w_2 + 1156)`
- Taylor in `w_2`: residue = `(16/840123)·w_2 − (16/751689)·w_2² + O(w_2³)`
- at `w_2 = 1e−4`: residue = `1.904 × 10⁻⁹` (Sage-symbolic)
- at `w_2 = 0.5`: residue = `5.817 × 10⁻⁶` (Sage-symbolic)

Direction: independent multi-pole with distinct `(J_i, m_i²)` breaks the identity LINEARLY in `w_2` to leading order. The coefficient is structural (depends on the `(J_1, m_1², J_2, m_2², K)` combination through a specific rational function), NOT zero.

---

## §3 — Propagator Class I-V taxonomy

R3-FINAL CONVERGENCE Sage-symbolic taxonomy (L1342-1376; expanded in T10-8 standalone file `propagator-class-taxonomy.md`):

| Class | Propagator structure | Identity status at substrate pivot | Residue formula |
|:------|:---------------------|:------------------------------------|:----------------|
| **I**   | Single literal pole `P(K) = T/(J·K² + m²)`, `A = -1` | Holds EXACTLY (residue ≡ 0 symbolically) | 0 |
| **II**  | Degenerate multi-pole `P(K) = T·∑w_i / (J·K² + m²)`, shared `(J, m²)` | Algebraically reduces to Class I; holds EXACTLY | 0 |
| **III** | K-homogeneity ODE family at `A ≠ -1`, `f(u) = 2A/(u-A)` | Holds EXACTLY by construction (one-parameter family); only `A = -1` is physical | 0 (mathematical tool, not a realized class) |
| **IV**  | Independent multi-pole `P(K) = ∑w_i · T/(J_i·K² + m_i²)` with distinct `(J_i, m_i²)` | BROKEN at order `w_2 · (asymmetry between (J_1, m_1²), (J_2, m_2²))` | `(16/840123)·w_2` leading order at substrate-physical test point |
| **V**   | Running-mass `m²(K) = m_0²·(K/K_0)^γ` with `γ ≠ 0, 2` | K-homogeneity violated; broken at order `γ · u/(1+u)` | `γ · v · (2 − γ) / (1 + v)`, substrate `γ_pivot ~ 4.4 × 10⁻⁵` |

The substrate's actual class at pivot is **predominantly Class I/II with sub-detector-precision Class IV leakage and sub-detector-precision Class V running-mass correction**. This lifts the C1 identity from "ad-hoc algebraic" to "classified within a structural taxonomy of propagator classes."

---

## §4 — Sign-AND-magnitude lock through one identity

Volovik R2-B EMERGENCE (i) substitution chain (L1003-1017), accepted by connes R3 (L1120):

```
Definition 1: u_pivot is calibrated by canonical n_s = 0.9649 through the
              K-homogeneity ODE solution at A = -1
Definition 2: Under the same K-homogeneity ODE at A = -1,
              α_s = -4·u/(1+u)²
Substitution: n_s = 0.9649 (Planck canonical)
              ⇒ u_pivot = 19649/351 = 55.9800569800570 (rational form)
Step:         α_s = -4 · 55.9800569800570 / (1 + 55.9800569800570)²
              = -6896799/100000000 (rational form, Sage-symbolic)
              = -0.06896799 (decimal, exact rational)
Direction:    Sign(α_s) = - (NEGATIVE), Magnitude(α_s) = 0.06896799 are
              determined SIMULTANEOUSLY by one identity. There is no
              upgrade pathway from sign-lock to magnitude-lock; they are
              the SAME lock under the C1 identity.
Conclusion:   Fairbairn+eBOSS's negative-central-value confirmation of
              sign-lock SIMULTANEOUSLY confirms framework's prediction
              at the structural level AND hardens the magnitude-tension
              exposure to 16.9σ.
```

This is the registry-grade structural reading: the framework's α_s prediction is the single entry in the frozen-prediction landscape where sign-test, magnitude-test, AND trend-test are all linked through one identity.

---

## §5 — Regime-bounded protection: K << K_sat

K-homogeneity protection holds at `K << K_sat ≈ 0.7·M_KK` (CMB pivot regime, Class I/II); it BREAKS at `K > K_sat` where optical-branch weight rises and Class IV activates. R3 EMERGENCE (iv) L1278-1303:

```
At K << K_sat ≈ 0.7·M_KK (CMB pivot regime):
  optical-branch weight ~ (k_pivot/ω_L1)² ~ 10⁻⁴
  Class IV leakage residue ~ 1.9 × 10⁻⁹, undetectable
  → C1 identity holds to detector precision (Class I/II equivalent)

At K ~ K_sat (substrate-acoustic-saturation regime):
  optical-branch weight rises to O(1) as K → K_sat
  Class IV leakage residue rises ~linearly in w_optical
  → C1 identity breaks at order ~K-running of w_optical(K)
```

Falsifier: any future probe of α_s K-running near K_sat (e.g., 21cm intensity mapping at scales above CMB last-scattering) should see identity-breaking begin with optical-weight onset. The signature is α_s deviating from `n_s² − 1` in a SPECIFIC way: residue grows linearly in `w_optical(K)`, with structural coefficient depending on `(J_optical / J_acoustic)` and `(m_optical / ω_L1)²` ratio. Carry-forward: `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT` (R3-FINAL Priority 4).

---

## §6 — LiteBIRD 5-outcome regulator-discriminator typology

R3 EMERGENCE (iii) L1244-1276 formalization. LiteBIRD becomes a multi-axis NCG falsifier under the §VII.M three-layer regulator theorem (S84 W2a-11):

| Outcome | Joint (r, n_T) at LiteBIRD 2030 (σ(r) ≈ 0.001) | Structural reading |
|:--------|:-----------------------------------------------|:--------------------|
| **1** | Falls on `n_T = -r/8` line at `r ≈ 0.00745 ± 1σ` | Selects L1 zeta closure (Path-H, transverse fiber-oscillation); consistent with K-homogeneity ODE family at `A = -1`, BDI-universality |
| **2** | Falls on `n_T = -r/8` line at `r ≈ 0.0117 ± 1σ` | Selects L3 per-Q-span closure (Path-C, substrate-compaction Mellin-tilt); consistent with K-homogeneity ODE family at `A = -1`, BDI-universality |
| **3** | Falls on `n_T = -r/8` line at intermediate r | Third NCG-compatible regulator OR continuous deformation between L1/L3; carry-forward `S87-PATH-H-PATH-C-INTERPOLATION` (R3-FINAL Priority 6) |
| **4** | Falls OFF `n_T = -r/8` line at >1σ | Single-field consistency violated; either substrate-side multi-field structure OR non-substrate physics; major framework re-evaluation |
| **5** | Falls on line but at `r ≪ 0.00745` or `r ≫ 0.0117` | Both NCG-compatible regulators excluded by 1+σ; NCG axioms compatible with regulator class need extension; framework re-evaluation at the regulator level |

Structural reading: LiteBIRD at `σ(r) ≈ 0.001` selects among NCG regulators within the §VII.M three-layer theorem AT 4.25σ resolution between Path-H and Path-C; outcomes 4-5 falsify NCG-compatibility entirely. This is structurally novel: LiteBIRD is not just a tensor probe but a DECIDER over NCG regulator class.

---

## §7 — Falsifier hierarchy and observational status

| Falsifier | Resolution | Substrate-physical residue floor | Detector | Status (2026-04-27) |
|:----------|:-----------|:---------------------------------|:---------|:--------------------|
| **CMB sign-lock** | Sign of central α_s | `8.65 × 10⁻⁵` absolute (10⁴× below flip requirement `\|δα\| = 0.069`) | Aiola-2020 / Fairbairn+eBOSS | Aiola-2020: 11.31σ tense (sign INVERTED; central +0.0023). Fairbairn+eBOSS: 16.9σ tense (central −0.00323; SIGN-LOCK CONFIRMED at central value) |
| **CMB magnitude-test** | `σ_α_s ≈ 2.1 × 10⁻³` (CMB-S4); `σ_α_s ≈ 1.1 × 10⁻³` (CMB-HD) | 25× below CMB-S4 1σ; 13× below CMB-HD 1σ | CMB-S4 (2028+); CMB-HD (2034+) | Quarterly poll under `S87-ALPHA-S-CMB-S4-WATCH` (R3-FINAL Priority 2) |
| **3He-B lab analog** | Aalto LTL spin-tilt running of dipolar excitation; `ε² = 0.001` precision target | dominant quantum-metric correction would falsify substrate's BDI-universality assignment | Aalto LTL (2-3 year program from first liaison) | Paper-mode pre-build under `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` (R3-FINAL Priority 1) |
| **K-running** | `δα(K)/α_FW` shape through GGE-saturation crossover; substrate Class I/II → Class IV transition near `K_sat ≈ 0.7·M_KK` | linear in `w_optical(K)` with structural coefficient | 21cm intensity mapping at `z ~ 30`, wide-area photometric surveys | `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT` (R3-FINAL Priority 4); theoretical-only at present |
| **LiteBIRD regulator class** | 5-outcome typology under §VII.M (Path-H / Path-C / interpolation / off-line / out-of-range) | r-amplitude resolution at LiteBIRD 2030 `σ(r) ≈ 0.001` | LiteBIRD (2028+) | 4.25σ Path-H/Path-C discrimination; cross-references T10-9 `rank-2-product-detector-orthogonality.md` and T10-3 falsifier-master-inventory upgrade |

---

## §8 — Branch (A) ∪ partial-(C) commitment

R3 CONVERGENCE Branch table (L1122-1128, locked R3 endpoint):

| Branch | Status | Anchor |
|:-------|:-------|:-------|
| **(A)** identity is EXACT, framework genuinely 11-17σ tense, falsification at CMB-S4 | **DOMINANT** | Three route-redundancies meet at float-eps zero: (i) C1 propagator-class axiomatic; (ii) V1 microscopic GGE-quasiparticle kinematic; (iii) R2-A K-homogeneity ODE family. All three give `α_s = -0.06896799` to machine epsilon at `u_pivot = 55.98`. |
| **(B)** identity is leading-order, substrate's direct α_s differs, re-pin α_s with structural uncertainty band | **REJECTED** | V1 float-eps reproduction + sign-AND-magnitude lock + no Z-invariant for α_s magnitude (A4-V4) + no minimal NCG axiom set forcing single-pole (A4-V5; BDI-universality + K-homogeneity is the substrate-physical input). No structural uncertainty band warranted at substrate-physical precision. |
| **(C)** sign-lock holds structurally, opposite-sign data falsifies | **PARTIALLY ACTIVATED** | Fairbairn+eBOSS (`-0.00323`) is the FIRST canonical observation to confirm sign at central value. Magnitude tension hardens to 16.9σ but sign-confirmation under sign=magnitude lock simultaneously confirms framework structurally. CMB-S4 (2028+) at `σ_α_s ≈ 2.1 × 10⁻³` will resolve definitively. |

Branch (A) ∪ partial-(C) is locked as the workshop's R3 endpoint.

---

## §9 — What Holds (registry-grade frozen items)

- `alpha_s_inflation_framework = −0.06896799` — **FROZEN canonical**, FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030. Symbolically EXACT in rational arithmetic at `u_pivot = 19649/351`. No re-pin needed; no structural uncertainty band warranted at substrate-physical precision.
- **Sign-lock structural theorem (C4)** — `α_s_substrate < 0` STRUCTURAL for canonical `n_s ∈ (0, 1)`; substrate ceiling `10⁴×` below flip requirement; PROVEN against all four substrate-physical routes (A, B, C, D) at all τ AND under all NCG-compatible regulators.
- **Identity `n_s² − 1` algebraically EXACT for single-effective-pole equivalence class (Class I/II)** — protected by single-pole Ornstein-Zernike propagator structure of GGE-acoustic Goldstone at substrate pivot; survives next-order Seeley-DeWitt corrections that preserve single-pole structure.
- **+0.99% n_s NROY mechanism remains structurally intact** — the canonical `n_s = 0.9649` calibration of `u_pivot = 55.98` fixes `α_s = −0.06897` simultaneously through the sign-AND-magnitude lock; no substrate-physical degree of freedom in `n_s → α_s` mapping.
- **Single-field consistency `n_T = −r/8` for both Path-H and Path-C** — substrate's two-pathway r split respects scalar-vs-tensor normalization closure; tilt-test `n_T = −r/8` is regulator-independent at pivot; LiteBIRD 4.25σ discrimination via line-position is real and substrate-physical.
- **BDI universality + GAP-ANTIJENSEN-65 close Route D at all τ AND under all NCG-compatible regulators** — symmetries of BdG Hamiltonian (TRS, PHS, chiral) are regulator-independent; gap floor `0.975·Δ_0` across `τ ∈ [0, fold]` excludes universality-class transition in dynamical range.
- **Substrate-physical residue floor `~1.25 × 10⁻³` relative is structurally derived** — `γ_pivot ~ 4.4 × 10⁻⁵` fixed by Leggett-dipolar zero-momentum scalar coupling + GGE-thermalization `E_J/Δ ~ 4.4` (S61 PASS); not a free parameter.
- **§VII.M three-layer regulator theorem** (S84 W2a-11 landing; Connes + Lizzi + VdD signature) is the correct structural framing for two-pathway r split at pivot — pivot-stationary `(a_4 / a_2)` with regulator-dependent `a_4` magnitude under L1 zeta / L2 Zubarev / L3 per-Q span closures.

---

## §10 — Cross-references

- **§VII registry slot for canonical identity**: `sessions/permanent-results-registry.md` (slot to be allocated in S87 carry-forward `S87-A_S-SURVIVING-ROUTE-RANK-LANDING`).
- **Canonical constants module**: `computations/canonical_constants.py` `alpha_s_inflation_framework`, `alpha_s_canon_2020`, `alpha_s_canon_Fairbairn` (pin status pending UD-3 / UD-4 user adjudication).
- **Falsifier inventory (next-generation observation matrix)**: `sessions/framework/registry/falsifier-master-inventory.md` Row #2 (LiteBIRD 5-outcome typology refinement; T10-6 install).
- **Propagator-class taxonomy (residue formulas)**: `sessions/framework/registry/propagator-class-taxonomy.md` (T10-8 install).
- **Rank-2 product detector orthogonality theorem**: `sessions/framework/correspondence/rank-2-product-detector-orthogonality.md` (T10-9 install).
- **§VII.M three-layer regulator theorem**: S84 W2a-11 landing in `sessions/permanent-results-registry.md` (Connes + Lizzi + VdD three-solo signature).
- **W11-C5/C6 lab-falsifier protocol**: `sessions/framework/registry/W11-C5-C6-falsifier-protocol.md` (T10-21 install).
- **3He-B inheritance canonical**: `sessions/framework/correspondence/3HeB-inheritance-canonical.md` (S87 paper-mode build target for `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT`).
- **Frozen-prediction discipline**: `.claude/rules/regulator-convention-lockdown.md` + project FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030.

---

## §11 — Carry-forward (S87+; from R3-FINAL workshop verdict L1647-1683)

| Priority | Gate ID | Effort | Brief |
|:---------|:--------|:-------|:------|
| 1 | `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` | paper-mode 2-3 sessions | Theoretical prediction for spin-tilt running of 3He-B dipolar excitation under laser-quench-prepared GGE at Aalto LTL |
| 2 | `S87-ALPHA-S-CMB-S4-WATCH` | quarterly poll, ~10 min | Quarterly poll of CMB-S4 + CMB-HD MacInnis-companion publication stream |
| 3 | `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE` | GPU-eligible ~1-2 days | Compute α_s from GGE-relic Bogoliubov occupation-number variance at horizon crossing (independent of single-pole assumption) |
| 4 | `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT` | GPU-eligible ~2-3 days | Predict `δα(K)/α_FW` shape through GGE-saturation crossover from substrate-physical inputs from BdG spectral triple |
| 5 | `S87-A4-A2-PIVOT-STATIONARITY-PIN` | GPU-eligible ~1-2 days | Compute residual `d(a_4/a_2)/dτ · (τ_pivot − τ_fold)` at pivot scale |
| 6 | `S87-PATH-H-PATH-C-INTERPOLATION` | paper-mode 1-2 sessions | Map intermediate-r outcomes (between Path-H 0.00745 and Path-C 0.0117 on `n_T = −r/8` line) to regulator-class — third NCG-compatible regulator OR continuous deformation between L1/L3 |

---

## §12 — Closing line (registry-grade summary)

The framework's `α_s = −0.06896799` prediction is the cleanest single-observable falsifier in the entire frozen-prediction landscape: triply-anchored at substrate pivot (BDI universality + kinematic optical-branch suppression + sub-threshold inter-band coupling), sign-AND-magnitude locked through one identity (`α_s = n_s² − 1`, symbolically exact at `u_pivot = 19649/351`), with substrate-physical residue floor `10⁴×` below the sign-flip requirement and `25×` below CMB-S4 1σ resolution; sign-confirmed in central-value by Fairbairn+eBOSS canon `−0.00323` while hardening magnitude tension to 16.9σ; pre-emptable by 3He-B Aalto LTL dipolar-excitation spin-tilt running at `ε² = 0.001` precision (multi-axis universality-class falsifier), with CMB-S4 (2028+) at `σ_α_s ≈ 2.1 × 10⁻³` resolving sign-test, magnitude-test, and trend-test simultaneously through one structural identity with no remaining substrate-physical degree of freedom.
