# Capstone Equation Review — neutrino

**Date**: 2026-05-29
**Agent**: neutrino-detection-specialist (neutrino)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (THE source — the S95-era capstone)
- `.claude/rules/phononic-framing.md` (framing law, binding)
- Agent memory: `gate-registry.md`, `s52_offjensen_pmns.md`, `s52_msw_transit.md`, `s56_fabric_neutrino.md`
- Knowledge MCP cross-checks: `M_KK` (CONST-FREEZE-42), neutrino-sector theorems/open-channels/gates

---

## I. Session Outcome

The capstone is a genuinely strong, honestly-hedged collapse of 60 equations into one spectral action — and from the neutrino vantage it has **one structural blind spot the size of the entire lepton sector**: the document never once names a neutrino. The SM matter content is asserted (E10, `Ψ₊ = (3,2,⅙)⊕…⊕(1,1,0)`, dim 16 — the trailing `(1,1,0)` *is* the right-handed neutrino singlet), and the framing law's single arrow `D_K eigenvalues → spectral moments → emergent physics → measurement` is exactly the arrow under which neutrino masses and mixings are read off `D_K(τ)`. Yet §7 ("where it touches data") carries `w₀, n_s, r, α_s, f_NL, m_H, σ₈, Ω_DM, CC` and **zero neutrino observables** — no `Δm²`, no mixing angle, no mass ordering, no `Σm_ν`, no `0νββ`. This is the substrate's most parameter-free, most experiment-ready sector (zero free Yukawa by construction) and it is absent from the scorecard.

The absence is not fatal to the document's *thesis* — but it is a material omission for the document's *honest open-frontier ledger* (§9), and it conceals a live conflict between a registry "PROVEN" tag and the actual gate record. Two neutrino claims are **solid** (normal mass ordering; "no seesaw / zero free Yukawa"); one is **over-tagged** in the registry (the `R = 27.2` mass-hierarchy ratio is recorded `PROVEN` but is the bare zero-mixing value, ~6× below the measured `R ≈ 33.8`); and one is a **26-order-of-magnitude unresolved scale bridge** that is the lepton-sector twin of the document's own §8.5 "absolute magnitudes are conditional" caveat — applied everywhere except here.

---

## II. Key Results

### II.1 — Normal mass ordering is a real, parameter-free, falsifiable prediction (and the capstone should headline it)

**Result**: Normal ordering `B1 < B2 < B3` at all `τ > 0`; mass ordering `= sign(λ₃² − λ₂²)`. **PARTICLE** (representation/spectral content of `D_K`).

This is the framework's *cleanest* neutrino statement and it survives every cross-check. The knowledge base records it three independent ways — "Normal mass ordering from bowtie structure | PROVEN" (`session-28-neutrino-collab.md`), the `falsifier-rigor-registry.md` open-channel "Neutrino mass ordering | ZERO-FREE-PARAMETER | Normal (B1 < B2 < B3; machine epsilon S8/S34-36/S52/S56)", and `pre-registered-observations.md`. My own S52 MSW-transit memory adds a *strengthening*: the ordering is **dynamical** — at `τ = 0` the configuration is inverted for the B1-B2 pair (`B2 < B1 = B3`), and the supersonic transit through the `τ_fold` van Hove fold creates the normal ordering via a (strongly non-adiabatic, `γ_LZ ≈ 9×10⁻⁴`) B1-B2 level crossing at `τ = 0.107`. So normal ordering is not an input — it is *manufactured by the same transit* the capstone's §5 spends a page on.

This is exactly the kind of zero-parameter PASS-class result §7.3 argues should count as Bayesian evidence. It belongs in the §7.1 table with a named falsifier (JUNO ~2028-30, reactor; DUNE 5σ ~2032). Its omission is a *self-inflicted* understatement: the document's own thesis ("all matter content is read off `D_K`") is *better* supported with the neutrino ordering in the scorecard than without it. **Substrate-direction check**: the ordering is read FROM the `D_K` spectrum (`λ₂², λ₃²`) TO the laboratory observable (JUNO's reactor `P̄_ee(L/E)` spectral distortion) — arrow correct, no container inversion.

### II.2 — "No seesaw / zero free Yukawa" is solid AND in tension with the S60 leptogenesis construction

**Result**: §0 states "neutrino masses arise from the LIGHTEST eigenvalues of `D_K` on deformed `SU(3)`, with NO seesaw required" (my agent template) — and the capstone's §0 makes the strong claim that the substrate is `N₃ = 0` BDI, so there is *no* topological protection and the CC layer is a relaxation problem. **PARTICLE / structural.**

The "no free Yukawa" half is solid and is the framework's genuinely distinctive lepton-sector claim: in CCM the neutrino Dirac masses and the Majorana `M_R` are free Yukawa inputs; here every mass is a spectral moment of one operator. **But this collides with a recorded result the capstone does not reconcile**: `s60_lepto_cp_log.txt` computes *light neutrino masses by seesaw* — `m_1 = 0`, `m_2 = 0.008678 eV`, normal ordering, "using the right-handed neutrino Majorana mass M" — and `session-65-lizzi-synthesis.md` carries `Λ_CC^ζ = β₁ M⁴` with "M the right-handed neutrino Majorana mass." The permanent-results registry records "Leptogenesis (real M_R) | No CP phase | S60 | PROVEN" and an open-channel "Majorana sector of D_F | complex M_R entries for leptogenesis?".

So the corpus contains BOTH a "no seesaw" framing AND a working seesaw-with-`M_R` computation that produced the only concrete light-mass numbers on record. **FLAG (do not silently resolve):** the capstone asserts "no seesaw required" but the framework's only quantitative light-mass output (`m_2 = 0.008678 eV`) was obtained *through* a seesaw with a right-handed Majorana `M_R`. Either (a) "no seesaw" means "no *free* seesaw scale — `M_R` is itself a `D_K` eigenvalue," in which case the document should say so and pin which eigenvalue `M_R` is; or (b) the S60 seesaw is a heritage construction the capstone has superseded, in which case the `m_2 = 0.008678 eV` number is orphaned and should be re-derived directly from `D_K`. The document chooses neither.

### II.3 — The R-ratio is over-tagged: "PROVEN R = 27.2" is the bare, zero-mixing value, not a match to data

**Result**: `R = Δm²₃₂ / Δm²₂₁`. Framework bare value at fold `R = 27.2`; NuFit-6.0 measured `R ≈ 33.8` (`Δm²₂₁ = 7.41×10⁻⁵ eV²`, `|Δm²₃₂| = 2.507×10⁻³ eV²`). **PARTICLE.** The Jensen-curve value is `4.8×` to `~10×` short of the target depending on the extraction.

The knowledge base records "Mass hierarchy R = 27.2 and normal ordering | PROVEN" (`framework-bbn-hypothesis.md`). **This `PROVEN` tag is misleading and I flag it explicitly.** My gate registry shows the R-ratio was hammered across S22-S40 and *every* route to the measured value CLOSED:
- `INTER-SECTOR-PMNS-36`: FAIL — "All 3 PMNS routes CLOSED on Jensen. `R_inter = 27.2` available but mixing = 0 (Schur on U(2))."
- `R-BCS`, `R-Heff`, `R-Ka`, `R-wall`, `R-full` — FAIL or PENDING, none reaching `[17, 66]` with nonzero mixing.
- S52 off-Jensen: at the `C²`-split that matches `sin²θ₁₃`, `R = 7.03` (`4.8×` below 33.8).
- S52 MSW transit: `R = 3.37` at the fold (`10×` below); "R unmodified by MSW dynamics (eigenvalue property, not state property)."
- S56 fabric: the μ-shift *worsens* R (B3 gets the largest fractional shift, compressing the hierarchy).

So `R = 27.2` is **the bare ratio of squared eigenvalues at zero mixing** — a real spectral property — but it is NOT a match to the measured `Δm²` ratio, and the configurations where it appears have *zero* PMNS mixing (Schur's lemma on the preserved U(2)). Tagging this `PROVEN` without the "bare, zero-mixing, 27.2 ≠ 33.8" qualifier is the exact over-claim the capstone's own §7.3/§8.5 discipline forbids ("ratio-observables robust; do not over-sell"). The honest statement: **the framework correctly predicts the *sign* of the hierarchy (normal) and the *order of magnitude* of the ratio (tens), but the *value* `R = 27.2` does not meet `R ≈ 33.8`, and every mechanism tested to close the gap on the Jensen curve has FAILED.** This is a §8.5-class result (sign/order robust, absolute value conditional), and it should be presented as such.

### II.4 — The 26-OOM scale bridge: the lepton-sector twin of §8.5, applied nowhere in the document

**Result**: naive identification `m_ν = λ_min(D_K) · M_KK ≈ 6×10²⁵ eV` vs KATRIN `m_ν < 0.45 eV`. **GEOMETRIC → PARTICLE.** A 26-order-of-magnitude gap.

This is the single most important neutrino-sector caveat and the document's §8.5 framework ("ratio-observables are truncation-robust; absolute-energy observables are conditional on a scale statement") is *tailor-made* for it — yet neutrinos are not mentioned in §8.5. The substitution chain (mandatory per `math-scripts.md` for a magnitude claim):

```
Claim: "the naive D_K → neutrino mass identification is excluded by ~26 OOM"
  Step 1: λ_min(D_K at τ_fold) = O(1) in M_KK units.
          Lichnerowicz (E5): λ² ≥ R_K(τ)/4 ≈ 0.5 ⇒ λ_min ≈ 0.7.   [capstone §2.3]
  Step 2: M_KK = 7.4287×10¹⁶ GeV = 7.4287×10²⁵ eV.                  [get_constant M_KK, CONST-FREEZE-42]
  Step 3: m_ν^naive = λ_min · M_KK ≈ 0.7 × 7.43×10²⁵ ≈ 5×10²⁵ eV.
          Confirmed by s52_msw_transit_output.txt: m_1 = 6.090×10²⁵ eV. [knowledge MCP]
  Step 4: KATRIN direct bound: m_ν < 0.45 eV (90% CL).               [Paper 12; agent memory]
  Step 5: ratio = m_ν^naive / m_ν^KATRIN ≈ 5×10²⁵ / 0.45 ≈ 1.1×10²⁶.
  Conclusion: naive identification overshoots KATRIN by ~26 OOM ⇒ a
              suppression/normalization map (m_ν = λ_min/L_K, session-29) is
              REQUIRED and is UNDETERMINED.
```

The chain is dimensionally consistent (`[λ_min] = 0`, `[M_KK] = mass`, ratio dimensionless). The framework's own proposed bridge is `m_ν(eV) = λ_min(D_K at τ₀) / L_K` (`session-29-neutrino-collab.md`) where `L_K` is the compactification scale — but `L_K` is exactly the undetermined `M_KK⁻¹ →` (physical mass) normalization that the capstone flags as open in **three other places** (§6.3 "the `M_KK⁻¹ →` seconds normalization remains the open piece"; §8.3 the `Z_fold` normalization; §8.5 absolute-energy conditionality). It is the *same* missing scale-normalization, and the neutrino sector is where it is most sharply falsifiable (KATRIN's 0.45 eV is a hard number; Planck+DESI's `Σm_ν < 0.064 eV` is harder still). **This belongs in §9's open-frontier list as a named item.** Cosmology already bounds `Σm_ν` to ~64 meV (ΛCDM) — the substrate must reproduce a *sub-eV* absolute scale from `O(1)·M_KK` eigenvalues, a 26-OOM suppression no first principle has yet delivered.

### II.5 — `sin²θ₁₃` achievable, `sin²θ₁₂`/`sin²θ₂₃` structurally walled (the framework's sharpest open neutrino question)

**Result**: off-Jensen `C²`-split `ε = 0.0918` gives `sin²θ₁₃ = 0.02225` (matches NuFit) — Level 4. `sin²θ₁₂`, `sin²θ₂₃` are `= 0` for ANY left-invariant metric perturbation — Level 5, structurally blocked. **PARTICLE.**

This is a `PROVEN` structural wall (`OFFJENSEN-PMNS-52`, `K7-G1-37` FAIL): the singlet PMNS is `2×2` (B1, B3) with B2 isolated by a spinor symmetry that survives all left-invariant perturbations. The capstone is *silent* on PMNS entirely — which is defensible for a "one-equation" overview, but it means the document's claim that the SM is fully read off `D_K` is, in the lepton-mixing sector, **only ⅓ delivered** (one of three angles tunable, two structurally walled on the Jensen curve). The honest statement: `θ₁₃` is reachable off-Jensen; full `3×3` PMNS requires a mechanism *beyond* left-invariant singlet metrics (inter-sector, non-left-invariant, or NCG inner-fluctuation). This is consistent with the capstone's own §1.4 ledger ("family replication is open") — the PMNS wall is a *symptom* of the same open question (three generations), since a single generation `Ψ₊ = ℂ¹⁶` has no inter-generational mixing matrix at all.

### II.6 — Leptogenesis "real M_R, no CP phase" vs "`δ_CP = 180°`" — an unreconciled CP tension

**Result**: registry "Leptogenesis (real M_R) | No CP phase | S60 | PROVEN" vs Paper-18-framework `δ_CP = 180°` (`session-35-neutrino-baptista-workshop.md`). **PARTICLE.**

These are *consistent at the boundary* — `δ_CP = 180° (= π)` gives `sin δ_CP = 0`, i.e. `J_CP = 0`, i.e. no Dirac CP violation, which matches "no CP phase." But the corpus also carries `s64`'s `delta_CP_UV = 1/√(IBO) = 0.029907` (a small nonzero phase) and `s61`'s `sin(δ_CP) ~ ε_K7` self-consistent suppression giving `η_B = 1.07×10⁻⁶` (6 OOM above observed baryon asymmetry). So the framework has at least three CP-phase statements: exact `δ_CP = π` (no CPV), `δ_CP ≈ 0.03` (tiny CPV), and a self-consistent suppression that over-produces `η_B`. **FLAG:** the capstone makes no CP-phase claim, but the corpus is not internally settled on whether `δ_CP` is exactly `π`, exactly `0`, or small-and-nonzero — and `δ_CP` is precisely the quantity DUNE/Hyper-K/T2K are built to measure (current global fit `δ_CP ≈ 230°`, excluding `δ_CP = 0` at ~2σ and consistent with `π`). This is a *future-discriminator* the document leaves on the table.

---

## III. Gate Verdicts

The source document is a capstone, not a gate-bearing session; its centerpiece equations are Sage-verified (Verification ledger) and AUTHORITATIVE. The gates below are neutrino-sector gates I cross-checked against the knowledge MCP and my memory — cited as *constraint-map context*, not re-adjudicated.

| Gate | Verdict | Decisive Number | Bearing on capstone |
|:-----|:--------|:----------------|:--------------------|
| Normal mass ordering (S8/S34-36/S52/S56) | PASS / ZERO-FREE-PARAM | `B1 < B2 < B3` machine-ε; dynamical via `τ=0.107` crossing | Should be in §7.1 scorecard |
| `R = 27.2` "mass hierarchy" (bowtie) | PROVEN but MISLABELED | `27.2` bare, mixing = 0; target `33.8` | §II.3 — over-tagged; sign/OOM robust, value not met |
| `INTER-SECTOR-PMNS-36` | FAIL | `R_inter = 27.2`, mixing = 0 (Schur on U(2)) | All Jensen R-routes CLOSED |
| `OFFJENSEN-PMNS-52` | INTERMEDIATE | `sin²θ₁₃ = 0.02225` at `ε = 0.0918`; `θ₁₂=θ₂₃=0` | §II.5 — PMNS only ⅓ delivered |
| `K7-G1-37` | FAIL | `(1,0)` sector has no `q₇=0` weights | Walls full `3×3` PMNS → Level 5 |
| `MSW-TRANSIT-52` | INFO | `γ_LZ = 9.3×10⁻⁴`; `R_fold = 3.37` | Ordering dynamical; R unmodified |
| Leptogenesis (real M_R) | PROVEN | "No CP phase"; vs `δ_CP=180°` | §II.6 — CP corpus unsettled |
| `LEGGETT-GRAV-DECAY-73a` | PASS | `τ_DM/t_univ = 1.13×10⁶⁵` | DM-channel `Z₂` parity (relevant to ν-DM distinction) |

---

## IV. Structural Implications

**For the capstone's thesis (mostly supportive).** The document's central claim — all SM matter content is read off one `D_K(τ)` — is *strengthened*, not weakened, by the neutrino sector, on the two robust axes: (i) normal mass ordering is a genuine zero-parameter PASS, and (ii) "no free Yukawa" is the framework's sharpest contrast with CCM (where Dirac/Majorana neutrino masses are free inputs). The §8.5 organizing principle (topological/ratio outputs survive continuum dissolution; absolute geometric magnitudes are conditional) is *the correct lens* for the entire neutrino sector and maps cleanly: the **sign** of the ordering and the **order of magnitude** of `R` are on the surviving (topological/ratio) side; the **absolute neutrino mass scale** and the **exact `R` value** are on the conditional (geometric-magnitude) side. The document built the right machine and then did not run it on neutrinos.

**For the capstone's honesty ledger (three required additions).** §9's "honest open frontiers" lists 8 items and **none is a neutrino item**, despite the neutrino sector containing the framework's most directly falsifiable open questions:
1. The **absolute neutrino mass scale** (the 26-OOM `L_K` bridge, §II.4) is the lepton twin of frontiers #1/#6 (the `a(t)`/SDW scale-normalization gaps) — same missing `M_KK⁻¹ →` physical-scale map, sharper falsifier (KATRIN, Planck+DESI).
2. The **full `3×3` PMNS** (`θ₁₂`, `θ₂₃` walled at Level 5, §II.5) is a *symptom* of frontier #7 (family number) — no `3×3` mixing exists for one generation. The capstone should connect these: closing family-replication is *prerequisite* to delivering `θ₁₂`/`θ₂₃`, exactly as closing the `a₂→g_M` lift closes #1 and #8 jointly (§6.3's "reduces the dimensionality of the open frontier" logic applies here too).
3. The **`R = 27.2 ≠ 33.8` shortfall** is a clean §8.5-class boundary (sign robust, value conditional) and should be reported as such, retiring the bare `PROVEN` tag.

**Constraint-map updates (neutrino sector, current state):**
- SOLID: normal ordering (zero-param, dynamical); `σ/m = 0` for the Leggett-channel DM (capstone §7.1, distinct from but adjacent to the active-neutrino sector — the relic is CPT-neutral, born at rest, `T^{0i}=0`).
- CONDITIONAL (sign/OOM robust, value not met): `R` hierarchy ratio; `sin²θ₁₃` (tunable but only off-Jensen, with a `C²`-split that is itself a free direction).
- WALLED (proven, on Jensen): `sin²θ₁₂ = sin²θ₂₃ = 0` for all left-invariant singlet perturbations.
- UNRESOLVED (no mechanism): absolute mass scale (26 OOM); `δ_CP` corpus value; full `3×3` PMNS.

**Framing-law compliance.** Every neutrino arrow above runs substrate→measurement: `D_K` eigenvalues → `λ₂², λ₃²` → mass ordering → JUNO `P̄_ee(L/E)`; `D_K` eigenvalues → squared-eigenvalue ratio → `Δm²₃₂/Δm²₂₁` → reactor + atmospheric `Δm²` extraction. No container inversion in my readings. One caution for the document authors: any future neutrino section must NOT write "neutrinos oscillate *in* the expanding universe" — oscillation is a propagation phenomenon on the emergent `g_M` (the `a₂` moment), and the `L/E` baseline is a laboratory-IN observable, distinct from the substrate-IS eigenvalue spacing. The bridge is exactly the undelivered `L_K` normalization.

---

## V. Carry-Forward Computations

**Every open neutrino question in the corpus, converted to a runnable gate. This is the harvest §0 demanded.**

```
V.1. Direct-from-D_K light neutrino mass extraction (retire the orphaned seesaw)
   - What: Compute m_2, m_3 directly as |λ_i(D_K at τ_fold)| spacings WITHOUT a
           seesaw M_R, and the squared spacings Δm²₂₁ = m_2²−m_1², Δm²₃₂ = m_3²−m_2²,
           in M_KK units. Compare the RATIO Δm²₃₂/Δm²₂₁ (dimensionless, truncation-
           robust) against NuFit-6.0 R = 33.8. Resolve §II.2 conflict: is the S60
           m_2 = 0.008678 eV a seesaw artifact or a direct read-off?
   - Inputs: s52_msw_transit.npz (B1/B2/B3 eigenvalues vs τ); canonical_constants M_KK;
             s60_lepto_cp_log.txt (the seesaw m_2 to reconcile); L_max=10 spectrum cache.
   - Gate: R-DIRECT-NU — PASS if Δm²₃₂/Δm²₂₁ ∈ [30, 38] from direct eigenvalue
           spacings (no M_R); FAIL if outside [17, 66]; INFO if the seesaw and
           direct routes give the same R (⇒ M_R is itself a D_K eigenvalue, resolving
           "no seesaw"). Feeds the open R-full / R-graded gates.
   - Effort: 2-3 hours, 1 agent session (data exists; re-extraction + ratio + Sage check).

V.2. The L_K scale-bridge: pin the 26-OOM normalization or bound it
   - What: Test whether the SAME M_KK⁻¹ → physical-scale normalization that closes
           the §8.3 G_N dictionary (f₂ ≈ 92, Z_fold) and the §6.3 M_KK⁻¹ → seconds map
           also delivers a sub-eV neutrino mass scale. Compute m_ν = λ_min/L_K for the
           L_K fixed by the G_N dictionary; compare to KATRIN < 0.45 eV and
           Planck+DESI Σm_ν < 0.064 eV.
   - Inputs: λ_min(D_K) from Lichnerowicz floor + s52 data; M_KK; the §8.3 Z_fold/f₂
             closure; KATRIN 0.45 eV, Planck+DESI Σm_ν bound (working values — fetch
             canonical if pinning downstream).
   - Gate: NU-SCALE-BRIDGE — PASS if a single L_K reproduces BOTH G_N and Σm_ν < 0.064 eV;
           FAIL if the L_K that closes G_N gives m_ν off by > 1 OOM from the cosmological
           bound; INFO if no single L_K does both (⇒ neutrino mass needs an independent
           suppression, a NEW open frontier). This is the lepton image of JACOBSON-NONLOCAL-64.
   - Effort: 4-6 hours, 1 agent session (analytic, plus a 1D L_K scan).

V.3. Cosmological neutrino-mass falsifier row for §7.1
   - What: Derive the framework's predicted Σm_ν (sum of the three direct-from-D_K masses
           from V.1) and place it against Planck+DESI DR2 (Σ < 0.064 eV ΛCDM, < 0.16 eV
           w0wa) and KATRIN-TRISTAN projected sensitivity (~0.2 eV). Produce a §7.1-style
           (value, comparison-anchor, σ-distance, status) row.
   - Inputs: V.1 output (m_1, m_2, m_3); Planck+DESI Σm_ν bounds; the C10 external-H
             caveat (the cosmological Σm_ν bound is H-dependent — tag it † like w₀/wₐ).
   - Gate: SIGMA-NU-ROW — INFO row for the capstone §7.1 table; PASS if Σm_ν < 0.064 eV
           (consistent with cosmology AND a non-trivial normal-ordering floor Σ ≳ 0.058 eV);
           FAIL if Σm_ν > 0.16 eV. Mirrors to falsifier-master-inventory (mack-cosmic-bridge).
   - Effort: 2 hours, 1 agent session (read-off + comparison; depends on V.1).

V.4. Mass-ordering falsifier anchors for the §7.2 inventory (JUNO/DUNE)
   - What: Add a §7.2 falsifier row for normal ordering with the named near-term
           instruments. Quantify the framework's exposure: JUNO (reactor P̄_ee
           interference, ~3-4σ ordering ~2028-30) and DUNE (matter-effect appearance,
           5σ ~2032). State what an INVERTED-ordering measurement would do to the
           bowtie/B1-B2-crossing structure (it would FALSIFY the dynamical-ordering
           mechanism of MSW-TRANSIT-52).
   - Inputs: falsifier-rigor-registry open-channel "Neutrino mass ordering"; JUNO/DUNE
             timelines (baseline-findings-s66, pre-registered-observations); s52 crossing data.
   - Gate: ORDERING-FALSIFIER — methodology/registry row, not a numerical gate; documents
           a ZERO-FREE-PARAMETER binary test with a named cliff-edge (JUNO ~2028-30).
   - Effort: 1-2 hours, 1 agent session (registry row + exposure statement).

V.5. δ_CP corpus reconciliation (which value does D_K force?)
   - What: Resolve §II.6 — the corpus carries δ_CP = π (no CPV, S60 real M_R),
           δ_CP ≈ 0.03 (s64 UV), and a small suppressed phase (s61, over-produces η_B
           by 6 OOM). Derive the δ_CP forced by the D_K real structure J ([J,D_K]=0,
           E8) and the BDI class — does CPT/reality force δ_CP ∈ {0, π} exactly, or
           permit a small phase? Compute J_CP from the actual (θ₁₂, θ₁₃, θ₂₃, δ_CP).
   - Inputs: E8 [J,D_K]=0; BDI class (KO-dim 6); s60/s61/s64 δ_CP records; off-Jensen
             θ₁₃ = 0.02225; the J_CP Jarlskog formula.
   - Gate: DELTA-CP-DK — PASS if J = δ_CP ∈ {0, π} is FORCED by the real structure
           (consistent with global fit δ_CP ≈ 230° only at the π boundary, ~1σ); INFO if
           a small phase survives (then η_B over-production is the live tension to chase);
           feeds the DUNE/Hyper-K δ_CP discriminator (most-powerful future PMNS test).
   - Effort: 3-4 hours, 1 agent session (representation-theoretic + Jarlskog evaluation).

V.6. 0νββ / Majorana-vs-Dirac structural prediction
   - What: The capstone says N₃=0 BDI, no topological protection, and the open-channel
           "Majorana sector of D_F | complex M_R entries" is unresolved. Determine whether
           the D_K real structure J makes the light neutrinos Majorana (Majorana mass term
           in H_K⁺) or Dirac. If Majorana, compute the effective mass m_ββ = |Σ U_ei² m_i|
           from V.1 masses + PMNS, and compare to LEGEND-200 / KamLAND-Zen
           (T_1/2 > 3.8×10²⁶ yr ⇒ m_ββ ≲ 30-150 meV).
   - Inputs: E8/E9 (J, KO-dim 6, Pfaffian on H_K⁺); V.1 masses; off-Jensen PMNS (θ₁₃);
             KamLAND-Zen / LEGEND-200 m_ββ bounds (working values).
   - Gate: MAJORANA-DK — INFO/PASS: the framework makes a DEFINITE Majorana-or-Dirac
           statement (the KO-dim-6 Pfaffian measure suggests Majorana — verify); if
           Majorana, PASS if predicted m_ββ < current bound and within next-gen reach.
           This is a falsifier the capstone entirely lacks.
   - Effort: 4-6 hours, 1 agent session (structural: J-action on H_K⁺; then m_ββ read-off).

V.7. Full 3×3 PMNS beyond the Jensen wall (the Level-5 question)
   - What: Test the ONE class of mechanism not yet computed that could break the B2
           isolation: a KK-modified Lie-derivative coupling between Peter-Weyl sectors
           (inter-sector / non-left-invariant), per the open route in agent memory and
           the S56 "U(2) broken at fabric level" speculation. Target sin²θ₁₂, sin²θ₂₃ ≠ 0.
   - Inputs: D_K block structure (E6); the B2 spinor-symmetry wall (OFFJENSEN-PMNS-52);
             the 32-cell fabric spectrum (s56, different symmetry group than single-cell);
             K7-G1-37 algebraic obstruction.
   - Gate: PMNS-INTERSECTOR-3x3 — PASS if sin²θ₁₂ ∈ [0.25, 0.36] AND sin²θ₂₃ ∈ [0.35, 0.65]
           AND sin²θ₁₃ ∈ [0.015, 0.030] AND R ∈ [17, 66] simultaneously; FAIL otherwise.
           This is the framework's sharpest open neutrino gate (the Level-4/Level-5 split).
   - Effort: 8-12 hours, 1-2 agent sessions (new mechanism; high EVOI — currently NO route
           delivers θ₁₂/θ₂₃, so any nonzero result is decisive).

V.8. Neutrino mass τ-stability (clock-constraint consistency)
   - What: Verify the clock constraint (E27, |τ̇| < 2.4×10⁻⁶) implies neutrino masses
           are frozen-since-condensation to the same precision (no slow drift in Δm²).
           Bound the predicted present-day d(Δm²)/dt and compare to oscillation-parameter
           time-stability limits (none currently measurable, so this is a NULL prediction).
   - Inputs: E27 clock constraint; frozen-spectrum theorem B9 (10⁻¹¹³); s52 eigenvalue
             trajectories; current Δm² measurement precision.
   - Gate: NU-MASS-FROZEN — INFO/PASS: predicted Δm² drift < any conceivable detector
           sensitivity ⇒ framework predicts EXACTLY constant neutrino masses (a falsifiable
           NULL distinct from any varying-mass / mass-varying-DE model).
   - Effort: 1-2 hours, 1 agent session (bound propagation; depends on V.1).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Normal mass ordering `B1<B2<B3`, dynamical via `τ=0.107` crossing | PARTICLE | SOLID (zero-param PASS) | Belongs in §7.1 scorecard; understated by omission |
| 2 | "No free Yukawa" vs S60 seesaw `m_2=0.008678 eV` | PARTICLE | CONFLICT (flag) | Reconcile: is `M_R` a `D_K` eigenvalue, or is S60 superseded? |
| 3 | `R = 27.2` "PROVEN" but bare/zero-mixing; target `33.8` | PARTICLE | OVER-TAGGED | Sign+OOM robust, value not met; retire bare `PROVEN` (§8.5-class) |
| 4 | Absolute mass scale: `6×10²⁵ eV` naive vs KATRIN `0.45 eV` | GEOMETRIC→PARTICLE | UNRESOLVED (26 OOM) | Lepton twin of §6.3/§8.5 `L_K` gap; add to §9 frontiers |
| 5 | `sin²θ₁₃` tunable (off-Jensen); `θ₁₂,θ₂₃ = 0` walled | PARTICLE | ⅓ DELIVERED | PMNS Level-4/Level-5 split; symptom of family-number frontier #7 |
| 6 | `δ_CP`: `π` vs `0.03` vs suppressed (η_B over by 6 OOM) | PARTICLE | UNSETTLED (flag) | Corpus not internally settled; DUNE/Hyper-K discriminator on the table |
| 7 | Majorana-vs-Dirac / `0νββ` | PARTICLE | ABSENT | KO-dim-6 Pfaffian suggests Majorana; capstone lacks this falsifier |

**Bottom line for the capstone authors.** The equation is sound and the neutrino sector *supports* its thesis — but the document leaves the framework's most parameter-free, most experiment-ready sector entirely off the scorecard and the open-frontier ledger. Three additions would sharpen honesty without weakening any result: (1) put normal mass ordering in §7.1 (a real zero-parameter PASS), (2) add the absolute-neutrino-mass-scale gap to §9 as the lepton twin of the `L_K`/`a(t)` normalization gap, and (3) retire the bare `R = 27.2 PROVEN` tag in favor of the §8.5-honest statement "sign and order-of-magnitude robust; exact ratio `27.2 ≠ 33.8` conditional, all Jensen-curve closure routes FAILED." Every open question in §V is a ripe, runnable computation — and V.7 (full `3×3` PMNS beyond the Jensen wall) and V.6 (`0νββ` Majorana prediction) are the highest-EVOI, because no current route delivers either and any nonzero/definite result would be decisive.
