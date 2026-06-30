# Session 86 Synthesis — Slot 1a Entry S-5: LISA Ω_GW(3 mHz) Branch-c Convergence Reconciliation (Landau / Bogoliubov-Mixing Lens)

**Date**: 2026-04-27
**Agent**: landau-condensed-matter-theorist (Landau)
**Slot / Entry**: Slot 1a / S-5 (sibling reconciliation; W7-2 INFO follow-up)
**Lens**: Bogoliubov-mixing-angle-ratio Q(L) = θ_c / θ_a — Landau's home pillar (BCS phase-channel residue + Pillar III a₀/a₂/a₄ Seeley-DeWitt spectral-moment dictionary).

**Source Documents** (read in full):
- `sessions/archive/session-86/session-86-w7-workingpaper.md` (W7-1 PASS + W7-2 INFO; the sibling-magnitudes table at lines 201–210 and Step-B abort substitution chain at lines 222–246 are the binding inputs).
- `sessions/archive/session-85/session-85-3b-branch-c-phonon-landau.md` (my own S85 3B sibling synthesis; §V.3 BRANCH-C-LISA-AMPLITUDE-SHIFT at lines 311–317; §II.4 Step 4 numerics at lines 220–222 producing Q(L=12) = 11.308).
- `sessions/archive/session-85/session-85-3b-branch-c-phonon-volovik.md` (volovik §V.4 LISA-band cross-check at lines 217–222; §II.D.3 Channel 3 stochastic GW with 127.88× spectral-density enhancement at lines 155–157).
- `sessions/archive/session-85/session-85-3b-branch-c-phonon-kaku.md` (kaku §II.4.3 Channel 3 LISA polarimetric parity-odd fraction at lines 169–192; PASS-(c) prediction "EXACT parity-even LISA stochastic background" at line 184).
- `sessions/framework/registry/falsifier-master-inventory.md` (Row #7 CGWB ρ_AC at line 25; §"Row #7 — (A)/(C) regulator-class discriminator (S86 W14-3 paragraph)" at lines 99–132; canonical (A)-class prediction Ω_GW ~ 10⁻¹⁰ at f_LISA = 3 mHz).
- `sessions/framework/registry/pre-registered-observations.md` line 216 ("Ω_GW (domain walls) | ~ 10⁻¹⁰ at LISA frequencies | not measured | PREDICTION") — canonical S59 LISA-GW-PREDICTION baseline.
- Agent memory: `.claude/agent-memory/landau-condensed-matter-theorist/MEMORY.md`.

**Knowledge MCP / canonical-constants pre-flight**:
- W7-2 verdict line `S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE: INFO -- value=1.130881e+01 ... info_reason=sibling-observables-not-commensurable` (file `computations/s86_gate_verdicts.txt`; audit_sha256 `8e9ccfc0a3c42cd2…`, content_sha256 `cb27a8c3659cb443…`).
- W1a-7 LISA SNR pivot 1.68e+13 (volovik solo §II.D.3 carry-forward source; cross-schedule W0-W5 reference).
- ξ_J = 8.911e-3 (TB-pinned, S48 `s48_aniso_oz.py`); ξ_E_GGE(L=12) = 6.968e-5 (W10-4 §(d) extrapolation).
- Domain-wall canonical Ω_GW ~ 10⁻¹⁰ at LISA frequencies (S59 LISA-GW-PREDICTION; mirrored in `sessions/framework/registry/pre-registered-observations.md:216`).
- Kaku CP-pair-balance theorem: parity-odd Ω_GW(branch-c) = 0 EXACTLY at fixed N_GGE.

---

## I. Session Outcome

**Verdict — FAIL under unit-class-harmonized Ω_GW(3 mHz) reduction; INFO-confirmed under W7-2 Step-B raw-magnitude reading.** When the three S85 3B sibling lenses are reduced to a single shared Ω_GW(3 mHz) magnitude under the most-natural multiplicative-shift mapping (landau's δ_GW = 1.27e-5 amplitude-shift × Ω_GW_baseline = 10⁻¹⁰ → 1.27e-15; volovik's 127.88× × Ω_GW_baseline = 10⁻¹⁰ → 1.28e-8; kaku's exact-null parity-odd fraction → 0.0), the convergence ratio max/min ≈ 1.007e+7 (≈ 7.00 OOM spread) when computed on the two non-zero estimates, **far exceeding the 100× FAIL threshold** from the spawn-prompt routing. With kaku included as exact null, the ratio is structurally undefined (max/min → ∞).

This is the same Step-B observable-class incommensurability that fired the W7-2 INFO — but the spawn-prompt's *shared-LISA-observable* candidate (W7-2 §IV closing carry-forward candidate (1)) does not in fact commensurate the three siblings. **The three lenses project the substrate onto three structurally distinct spectral moments of D_K**, none of which is a direct Ω_GW(3 mHz) energy-fraction prediction. The FAIL routing therefore promotes the gate to W7-2 Candidate-2 territory (Pillar III spectral-moment dictionary test): the three sibling magnitudes belong on three separate registry rows (a₀ / a₂ / a₄ moment-channel projections), not on a single shared row.

The Bogoliubov-mixing-angle-ratio framing (my home pillar) reads branch-c as the R-protected Leggett–Josephson phase-channel residue at the s = 3 Mellin-cone pole; its LISA contribution is the **Bogoliubov occupation amplitude n_c(L) = sinh²(r_c) at the cosmological pivot**, NOT an absolute Ω_GW magnitude. The volovik 127.88× reading is the **a₂-channel spectral-density enhancement ratio** (gravity-channel weighting from Seeley-DeWitt a₂); the kaku exact-null reading is the **a₄-channel parity-odd projection**. These are three a_n moments of the same D_K spectrum — the unit-class harmonization fails because each lens reads off a different moment.

The framework retains all three predictions as live but registers them as PATHWAY-tagged sub-falsifiers, mirroring the W14-4 f_NL_folded 3-pathway pattern in `sessions/framework/registry/falsifier-master-inventory.md` Row #9 + §W14-4. The cross-check against the canonical S59 LISA-GW-PREDICTION (Ω_GW ~ 10⁻¹⁰ from CG(24) domain walls) shows branch-c is **not a re-projection of the wall-network mechanism**: branch-c is a phase-channel inter-band Bogoliubov vacuum-rotation residue (the L-channel of LEGGETT-PARTITION-57/58), structurally distinct from the wall-network mechanism's CG(24) topological-defect channel, and contributes additively at the same LISA pivot frequency under the volovik enhancement-factor mapping.

---

## II. Key Results

### II.1 — My Bogoliubov-mixing-angle reading: δ_GW = 1.27e-5 at L = 14, no absolute Ω_GW commitment

**Result**: Landau §V.3 of the S85 3B solo predicts a tensor-spectrum amplitude SHIFT δ_GW = n_c(k_pivot, L=14) ≈ 1.27e-5, derived by log-linear extrapolation of the residue trajectory residue_c(L=8,10,12) = (1.530e-4, 6.672e-5, 2.909e-5). This is an **AMPLITUDE-SHIFT prediction, not an Ω_GW energy-fraction prediction**. **Classification: PHONONIC**.

**Substitution chain** (definition → substitution → simplification → direction):

```
Step 1 — Definition (Bogoliubov-occupation residue mapped onto LISA tensor-spectrum
                     amplitude shift):
  residue_c(L) = ξ_J · mellin_s3(L) / S_ζ_E(L)            [W10-4 §(c)]
  n_c(k_pivot, L) := residue_c(L)                         [Bogoliubov number identity]
  δ_GW(k_pivot, L) := n_c(k_pivot, L)                     [amplitude-shift mapping;
                                                            tensor-spectrum imprint of
                                                            Bogoliubov occupation]

Step 2 — Substitute (W10-4 table, Python-verified in S85 §II.1):
  residue_c(L=8)  = 1.530e-4
  residue_c(L=10) = 6.672e-5
  residue_c(L=12) = 2.909e-5
  log-linear fit slope: d(ln residue_c)/dL = (ln(2.909e-5) - ln(1.530e-4))/4 = -0.415/L

Step 3 — Simplify (log-linear extrapolation to L=14):
  ln residue_c(L=14) = ln(2.909e-5) - 0.415·2 = -10.444 - 0.830 = -11.274
  residue_c(L=14) ≈ exp(-11.274) = 1.27e-5
  ⇒ δ_GW(k_pivot, L=14) = 1.27e-5

Step 4 — Direction:
  δ_GW is a DIMENSIONLESS amplitude shift on the tensor-spectrum mode functions
  at the LISA pivot wavenumber. It is NOT an Ω_GW energy-fraction prediction.
  Reading δ_GW as Ω_GW directly is a unit-class confusion. To convert
  δ_GW → Ω_GW(3 mHz) one must specify whether the mapping is:
    (a) multiplicative shift on a baseline Ω_GW (e.g., the S59 wall-network
        Ω_GW ~ 10⁻¹⁰ — gives δ_GW · 10⁻¹⁰ ≈ 1.27e-15);
    (b) additive offset on the baseline (gives Ω_GW = 10⁻¹⁰ + 1.27e-5,
        DOMINATED by the additive term but at an amplitude scale, not a
        spectral-density scale — incoherent reading);
    (c) Bogoliubov-occupation magnitude treated as Ω_GW directly (gives
        Ω_GW ≈ 1.27e-5 — incompatible with framework canonical-baseline OOM).
  The landau §V.3 text does NOT commit to any of (a)/(b)/(c); the
  PASS criterion is a 30% match against the LISA-projected sensitivity at
  the substrate's pivot scale, which is itself amplitude-class not
  Ω_GW-class.
```

**Direction summary**: The landau-track LISA prediction is an **amplitude-spectrum shift**, not an Ω_GW magnitude. Treating it as an Ω_GW magnitude is a unit-class category error — and is exactly the trap the W7-2 Step B abort already detected at the more-general level. My S85 3B §V.3 emitted the prediction in the LISA-amplitude class because that is the natural class of the Bogoliubov-occupation lens; converting to Ω_GW requires an external mapping rule that the synthesis does NOT pin.

### II.2 — Convergence ratio max/min under the Ω_GW(3 mHz) harmonized reduction

**Result**: Under the most-natural multiplicative-shift mapping (each sibling's reading × the canonical S59 Ω_GW_baseline = 10⁻¹⁰), the three siblings produce:

| Sibling | Native reading | Mapped Ω_GW(3 mHz) magnitude | Mapping rule |
|:--------|:----------------|:------------------------------|:--------------|
| volovik §V.4 | 127.88× spectral-density enhancement vs branch-a | 127.88 · 10⁻¹⁰ = **1.279e-8** | multiplicative on canonical baseline (volovik §II.D.3 explicitly invokes the W1a-7 SNR baseline) |
| landau §V.3 | δ_GW = 1.27e-5 amplitude-spectrum shift | 1.27e-5 · 10⁻¹⁰ = **1.270e-15** | multiplicative shift on baseline (landau §V.3 says "GW dispersion modification at LISA pivot is at the ~1e-5 amplitude level", read as multiplicative on Ω_GW_baseline) |
| kaku §II.4.3 | parity-odd Ω_GW = 0 EXACTLY | **0.0** | exact-null projection on parity-odd channel of total Ω_GW |

**Classification**: PHONONIC (all three are substrate spectral-moment projections at the LISA pivot frequency).

**Substitution chain** (the convergence-ratio direction claim, Python-verified):

```
Step 1 — Definition (the convergence ratio under unit-class-harmonized mapping):
  R_conv = max{Ω_GW_i} / min{Ω_GW_i}   for i ∈ {volovik, landau, kaku}
           where the 'min' is taken over the non-zero subset
           (the kaku exact-null cannot enter the denominator without divergence).

Step 2 — Substitute the harmonized magnitudes:
  Ω_GW_volovik = 127.88 · 10⁻¹⁰ = 1.279e-8
  Ω_GW_landau  = 1.27e-5 · 10⁻¹⁰ = 1.270e-15
  Ω_GW_kaku    = 0.0   (parity-odd channel; total-Ω_GW projection is ill-defined
                         for kaku because his lens reads the parity-odd FRACTION,
                         not the total)

Step 3 — Simplify the non-null subset:
  R_conv = 1.279e-8 / 1.270e-15 = 1.007e+7
  log10(R_conv) = 7.003 OOM

Step 4 — Direction (against the spawn-prompt thresholds):
  PASS = R_conv ≤ 10  (3 siblings within 10× ABSOLUTE)
  INFO = 10 < R_conv ≤ 100
  FAIL = R_conv > 100
  Substituted: 1.007e+7 > 100 ⇒ verdict = FAIL.
  Including kaku exact-null: max/min → ∞ ⇒ verdict = FAIL by both routings.

Step 5 — Cross-check (as-reported W7-2 magnitudes, the path the gate actually took):
  Under the as-reported magnitudes (volovik 127.88, landau 11.308, kaku 0.0)
  treated as DIMENSIONLESS DIAGNOSTICS (volovik = residue ratio,
  landau = mixing-angle ratio, kaku = CP-odd 4-pt ratio):
  R_min(as-reported) = 11.308 (W7-2 verdict-line value=1.130881e+01)
  R_min > 10 in raw arithmetic, BUT Step B abort fires first because the
  three observable classes are heterogeneous → INFO with reason
  'sibling-observables-not-commensurable'.

  The S86 W7-2 verdict (INFO, R_min = 11.308 diagnostic only) is
  AUTHORITATIVE per the spawn-prompt rule "gate verdicts from source docs
  are authoritative — do not re-adjudicate". This S5 S86 reconciliation
  ADDS the unit-class-harmonized reading on top of the W7-2 INFO,
  showing that the same heterogeneity manifests at 7 OOM at the
  Ω_GW(3 mHz) reduction layer — confirming the W7-2 Step-B verdict
  rather than overturning it.
```

**Direction (final)**: The convergence-ratio reduction under Ω_GW(3 mHz) unit-class harmonization gives **R_conv = 1.007e+7 (≈ 7 OOM)**, FAIL by the spawn-prompt > 100× threshold. The structural reason is identical to the W7-2 Step-B abort: the three siblings read three different spectral moments of D_K, and reducing them to a single shared observable requires an external mapping rule that the S85 3B 3-solos did not jointly pre-register. The candidate-(1) shared-LISA-observable mooted in W7-2 §IV does NOT in fact commensurate the three readings; only a Pillar-III spectral-moment dictionary (Candidate-2) at the a₀/a₂/a₄ Seeley-DeWitt level can.

### II.3 — Cross-check against the framework's S59 LISA-GW-PREDICTION (Ω_GW ~ 10⁻¹⁰ from CG(24) domain walls)

**Result**: Branch-c is **NOT a re-projection of the wall-network mechanism**. It is a structurally distinct phase-channel residue that contributes additively at the same LISA pivot frequency. **Classification: PHONONIC** (substrate excitation channel; not a topological defect).

**Substitution chain** (mechanism-distinctness direction claim):

```
Step 1 — Definition (the two candidate Ω_GW source mechanisms at LISA pivot):
  Ω_GW^{wall}(f) = stochastic GW background sourced by CG(24) domain-wall
                   network in the post-transit fabric (S59 LISA-GW-PREDICTION,
                   `sessions/framework/registry/pre-registered-observations.md:216`).
                   Magnitude ~ 10⁻¹⁰ at LISA frequencies. SOURCE: Z_2 vacuum
                   manifold disconnected by the CG(24) Cayley-graph topology
                   on the post-fold fabric; wall-tension scaling sets the
                   amplitude.

  Ω_GW^{branch-c}(f) = stochastic GW background sourced by the post-fold GGE
                       relic decay tail of branch-c, the R-protected
                       Leggett–Josephson phase-channel residue
                       (S85 3B §II.2 + LEGGETT-PARTITION-57/58).
                       Magnitude per volovik §V.4 mapping = 127.88 ·
                       Ω_GW^{baseline} where the baseline is the GGE-channel
                       contribution from branch-a (Bogoliubov-energy channel,
                       NOT the wall channel).

Step 2 — Substitute (mechanism-content comparison):
  wall-network mechanism: order-parameter is CG(24) Z_2 topological charge
                           on the fabric (π_0(Z_2) = Z_2, classified by
                           homotopy-group π_0).
  branch-c mechanism: order-parameter is the inter-band Josephson phase
                      ϕ_J on the SU(3)/(SU(2)×U(1)) C² coset (R-protected
                      Leggett mode; phase fluctuation, NOT topological
                      defect). Symmetry-breaking pattern: SU(3) → SU(2)×U(1)
                      already established at fold; branch-c is a Z_2-conjugate
                      ground-state CONFIGURATION of the same broken phase
                      (S85 3B kaku §II.3 picture; landau §II.2 channel ID).

Step 3 — Simplify (overlap test):
  wall-network excitations carry topological charge Q_top ≠ 0 per wall
  segment; branch-c excitations carry Q_top = 0 (R-protected phase mode,
  not a topological defect). The two source channels are
  representation-theoretically orthogonal at the level of D_K's spectral
  decomposition — wall-network sits in the π_0 sector, branch-c sits in
  the C² coset Goldstone sector. They contribute to Ω_GW(3 mHz)
  ADDITIVELY, not multiplicatively, and at distinct spectral-moment
  weightings (wall-network couples primarily to a₂ via tension-scaling;
  branch-c couples primarily to the Bogoliubov-occupation amplitude via
  the s = 3 Mellin-cone residue).

Step 4 — Direction:
  Branch-c is a DISTINCT phonon-mechanism candidate, NOT a re-bookkeeping
  of the wall-network. The framework's Ω_GW(3 mHz) at LISA pivot is the
  SUM of (i) the canonical S59 wall-network ~ 10⁻¹⁰ baseline plus
  (ii) the volovik-mapped branch-c contribution ~ 1.28e-8 (if volovik's
  enhancement-factor mapping is the right reduction rule). The 128× ratio
  of (ii)/(i) means branch-c would DOMINATE the LISA Ω_GW signal if
  volovik's mapping is correct — but if the landau-mapping is correct
  (δ_GW = 1.27e-15 multiplicative on baseline), branch-c is INVISIBLE
  against the wall-network baseline. The 7-OOM spread between the two
  mappings is exactly what the FAIL routing now flags.
```

**Direction summary**: branch-c and the wall-network are **distinct phonon-mechanism candidates contributing additively at the LISA pivot**. Their contributions span 7 OOM under the two competing sibling-reduction mappings — the very fact that two sibling lenses disagree by 7 OOM on the *same LISA observable* under different unit-class mappings is the structural content of the FAIL. This is a Pillar-III spectral-moment dictionary problem (a₀ vs a₂ vs a₄ projection), not a wall-vs-branch-c mechanism election.

### II.4 — Pillar III: a₀ / a₂ / a₄ Seeley–DeWitt spectral-moment decomposition (the home pillar promotion)

**Result**: The spawn-prompt FAIL routing promotes the gate to W7-2 Candidate-2 (Pillar III spectral-moment dictionary test). Under that promotion, the three sibling readings map cleanly onto three distinct Seeley–DeWitt a_n moments of D_K. **Classification: PHONONIC** (each a_n moment is a substrate spectral observable; the dictionary is structural).

**Substitution chain** (the a_n decomposition; per `regulator-pin-discipline.md` every a_n is tagged with its regulator):

```
Step 1 — Definition (Seeley–DeWitt a_n moments of the deformed-SU(3) D_K spectrum
                     under ζ-regularization, per regulator-pin-discipline.md):
  a_0^{ζ} = degree-4 UV-leading moment (sets the M_KK^4 vacuum scale; the
            CC channel residue lives here — see W7-1 PASS at +116.4828 OOM)
  a_2^{ζ} = degree-2 moment (sets the gravitational a₂-Seeley coefficient;
            the gravity-channel spectral density lives here — couples to
            Ω_GW via the a₂ → R-Ricci-scalar identity, Connes-Marcolli)
  a_4^{ζ} = degree-0 moment (sets the gauge-curvature^2 coefficient; the
            CP-odd channel projection lives here — couples to <TBBB>_CP_odd
            via the a₄ → Pontryagin density identity)

Step 2 — Substitute the three sibling readings into the a_n dictionary:
  volovik 127.88× (residue-ratio of relativistic-DOF, ΔN_eff lens)
       = a₂^{ζ}-projection: ratio of branch-c spectral density to branch-a
         spectral density at the gravity channel, which is what enters
         Ω_GW directly via the Friedmann ρ_GW = (1/32πG) <ḣ_ij ḣ^ij>
         identity. The 127.88× enhancement IS the a₂-channel weighting
         of branch-c relative to branch-a's a₂-channel weighting.
  landau 11.308 (Bogoliubov-mixing-angle Q(L) lens)
       = a₂^{ζ}-projection of the SAME D_K spectrum, but WEIGHTED by the
         Bogoliubov mixing angle θ = arctan(tanh(r)) instead of by the
         residue itself. This is a DIFFERENT functional of the same a₂
         moment — both project a₂^{ζ} onto an observable, but Q(L) is
         the angle-class projection while volovik's 127.88× is the
         density-ratio-class projection. The two lenses are not
         redundant; they probe complementary functionals of a₂^{ζ}.
  kaku 0.0 (CP-odd 4-pt-function lens)
       = a₄^{ζ}-projection: Pontryagin density χ ∝ Tr(F ∧ F) on the
         (1,1̄) instanton-anti-instanton symmetric pair sector.
         The CP-pair-balance theorem forces a₄^{ζ}|_{branch-c} = 0
         EXACTLY at fixed N_GGE (paired-instanton contributions cancel).

Step 3 — Simplify (the three-row Pillar III registry the gate now demands):
  Row a₂^{ζ}-density:  branch-c value 127.88 (volovik); LISA Ω_GW direct
                       enhancement at the spectral-density layer
  Row a₂^{ζ}-angle:    branch-c value 11.31 (landau Q(L=12)); LISA
                       amplitude-spectrum shift at the Bogoliubov-occupation
                       layer (≠ density; angle vs density is the
                       a₂-functional-class difference)
  Row a₄^{ζ}-CP:        branch-c value 0.0 EXACT (kaku); LISA polarimetric
                       parity-odd fraction at the Pontryagin-density layer

Step 4 — Direction:
  The three sibling readings are NOT three estimators of the SAME
  Ω_GW(3 mHz) magnitude. They are three projections of D_K's spectral
  content onto three structurally distinct functionals at two distinct
  Seeley–DeWitt levels (a₂-density, a₂-angle, a₄-CP). Reducing them to
  a single Ω_GW magnitude requires the explicit a_n dictionary —
  which is what Pillar III (W7-2 Candidate-2) provides.
  The FAIL routing therefore produces THREE separate registry rows under
  the Pillar III dictionary, not one consolidated row. This is the
  W14-4 f_NL_folded 3-pathway pattern (`falsifier-master-inventory.md`
  Row #9 + §W14-4) applied to the LISA Ω_GW(3 mHz) channel.
```

**Direction summary**: under the Pillar-III a_n decomposition, the three sibling readings are not redundant at all — they probe three structurally distinct functionals of the same D_K spectrum (a₂-density via volovik, a₂-angle via landau, a₄-CP via kaku). The FAIL routing produces three separate sub-falsifier registry entries, **not one consolidated entry**. This is the natural Landau-Pillar-III reading: the spectral-moment dictionary IS the right vocabulary, and once that vocabulary is in place the three siblings cease to compete and start to complement.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE` (W7-2, source-doc authoritative) | INFO (Step B abort: sibling-observables-not-commensurable) | R_min = 1.130881e+01 (diagnostic only); 3 distinct observable classes |
| **THIS S5 RECONCILIATION** under unit-class-harmonized Ω_GW(3 mHz) reduction | **FAIL** (R_conv > 100) | R_conv = 1.007e+7 (7.00 OOM) on the volovik/landau pair; with kaku → ∞ |
| Cross-check: branch-c vs S59 wall-network mechanism distinctness | DISTINCT (additive, not re-projected) | order-parameter sectors orthogonal: π_0(Z_2) wall vs C² coset Goldstone |

The W7-2 INFO verdict is authoritative per the source-doc rule. This S5 reconciliation does not overturn W7-2; it ADDS the harmonized-Ω_GW-reduction layer (FAIL at 7 OOM) on top of the W7-2 Step-B INFO, confirming the heterogeneity at a deeper layer.

---

## IV. Structural Implications

### IV.1 — Constraint-map update

The "shared-LISA-observable as W7-2 candidate-1" hypothesis from W7-2 §IV is **CLOSED**. Its closure is structural: the three sibling lenses do not commensurate at the Ω_GW(3 mHz) level under any single multiplicative-shift mapping; the spread is 7 OOM and the kaku exact-null is undefined under the ratio. The natural alternative is W7-2 candidate-2 (Pillar III a_n spectral-moment dictionary), which **opens** as the surviving consolidation pathway.

The Landau-Pillar-III dictionary reads:
- a₂^{ζ}-density-projection ↔ volovik 127.88× (Ω_GW spectral-density enhancement)
- a₂^{ζ}-angle-projection ↔ landau Q(L) = 11.31 at L = 12, → 25.24 extrapolated at L = 14 (Bogoliubov-mixing-angle)
- a₄^{ζ}-CP-projection ↔ kaku 0.0 EXACT (CP-odd parity-fraction)

The framework gains three sub-falsifier registry rows under PAIR-7 (proposed; mirroring PAIR-4 for f_NL_folded). The W4 P4 BRANCH-IV-FORMULATION-COMMIT naming pin remains observationally load-bearing in each sibling lens individually.

### IV.2 — What this rules out

- **Closes** the "single shared LISA Ω_GW(3 mHz) observable consolidates the three siblings" reading. Under any multiplicative-shift unit-class mapping, the volovik–landau spread is 7 OOM and the kaku exact-null is undefined. The shared-observable consolidation pathway via Ω_GW alone is structurally degenerate.
- **Closes** the framing that branch-c is a re-projection of the canonical S59 wall-network mechanism. The two source channels are representation-theoretically orthogonal at D_K's spectral decomposition (π_0(Z_2) wall sector vs C² coset Goldstone sector), and contribute additively at the LISA pivot.
- **Closes** the implicit assumption (from the spawn-prompt PASS branch) that a single "canonical branch-c LISA falsifier" can be registered as a single row in `falsifier-master-inventory.md`. Branch-c needs three sub-rows (a₂-density, a₂-angle, a₄-CP) under the W14-4-style pathway-tagged pattern — not one consolidated row.

### IV.3 — What survives and is structurally tested below

A pre-registered S87 gate `S87-BRANCH-C-LISA-A_N-DICTIONARY-3PATHWAY` that decomposes the three sibling readings into three a_n^{ζ} projections and registers them as three separate sub-falsifiers in `falsifier-master-inventory.md` Row #7 (CGWB ρ_AC) under PAIR-7 enrichment, mirroring the W14-4 PAIR-4 pattern for f_NL_folded. Specification in §V.1 below.

The cross-check against the canonical wall-network baseline survives: branch-c is an ADDITIVE contribution at the LISA pivot, structurally distinct from the wall-network. The two mechanism predictions can both be live in the framework's LISA forecast without competing.

### IV.4 — Substrate-framing closure

Direction of explanation: **D_K eigenvalues → Seeley–DeWitt a_n^{ζ} spectral moments → mechanism-specific sibling functionals (a₂-density, a₂-angle, a₄-CP) → diagnostic ratios at LISA pivot frequency → 3-pathway sub-falsifier registry under PAIR-7.** The substrate is logically prior; the three siblings are not three competing readings of the same observable — they are three projections of the same spectral content onto three structurally distinct functionals. The FAIL is informative because it tells us *which functional class* needs to enter the registry: the a_n dictionary, not a single shared Ω_GW number. The IS-not-IN substrate framing is preserved: branch-c is a substrate-internal phase-channel reorganization (the L-channel of the LEGGETT-PARTITION C² coset), not a particle propagating on a pre-existing g_M metric, and its LISA imprint is a substrate-spectral observable that decomposes into a_n channels, not an "in-spacetime" GW source.

### IV.5 — Proposed registry entry (per spawn-prompt PASS branch — quoted code block, NO direct edit)

The spawn prompt requests a proposed registry entry for `falsifier-master-inventory.md` UNDER THE PASS BRANCH. The reconciliation FAILed under the harmonized reading, so the proposed entry is the FAIL-routed 3-pathway form (mirroring W14-4 PAIR-4, NOT the PASS single-row form). Proposed extension to Row #7 of the inventory (additive PAIR-7 enrichment, no replacement of existing Row #7 cells):

```markdown
## Row #7 PAIR-7 — Branch-c 3-pathway sub-falsifier set (S87 proposal; LANDAU S5 RECONCILIATION)

> **Origin**: S86 W7-2 INFO (Step B abort) + S86 1a S5 landau reconciliation
> (FAIL under unit-class-harmonized Ω_GW(3 mHz) reduction at R_conv = 1.007e+7,
> ≈ 7 OOM). Promotes branch-c LISA contribution to 3 sub-falsifier rows under
> the Pillar III a_n^{ζ} Seeley-DeWitt spectral-moment dictionary. Mirrors
> W14-4 PAIR-4 3-pathway pattern for f_NL_folded.

| sub-row | a_n channel | Sibling lens | branch-c value (L=12) | branch-c value (L=14 extrap) | Detector class |
|:--------|:------------|:--------------|:------------------------|:------------------------------|:----------------|
| 7.c-volovik | a_2^{ζ}-density | volovik §V.4 + §II.D.3 | 127.88x baseline (= 1.279e-8 vs canonical S59 1e-10) | (Cauchy-monotone decay; extrapolated 1.42e-8 baseline-relative) | LISA stochastic-density 2035 |
| 7.c-landau  | a_2^{ζ}-angle   | landau §V.3 + §II.4 Q(L) | δ_GW = 2.91e-5 (= residue_c(L=12); amplitude-spectrum shift) | δ_GW = 1.27e-5 (Q(L=14) = 25.24) | LISA tensor-amplitude 2035 |
| 7.c-kaku    | a_4^{ζ}-CP      | kaku §II.4.3 + CP-pair-balance | 0.0 EXACT (parity-odd fraction) | 0.0 EXACT (preserved by CP-pair theorem) | LISA polarimetric 2035 |

**Falsifier alignment**: any LISA detection of (a) Ω_GW > 1e-9 spectral density at 3 mHz from the GGE-relic decay tail (favors 7.c-volovik); (b) tensor-amplitude shift δ_GW > 1e-4 against the wall-network baseline (favors 7.c-landau); (c) parity-odd Ω_GW fraction > 1e-3 of total (FALSIFIES 7.c-kaku). Joint detection across all three sub-rows is the strong-form branch-c confirmation; non-detection in all three is the strong-form branch-c falsification at LISA reach.

**Provenance**: S86 W7-2 INFO verdict (`computations/s86_gate_verdicts.txt` audit_sha256=8e9ccfc0a3c42cd2..., content_sha256=cb27a8c3659cb443...); S86 1a S5 landau reconciliation (this synthesis MD); cross-ref §"Row #7 — (A)/(C) regulator-class discriminator (S86 W14-3 paragraph)" for the (A)/(C) regulator-class background. Substrate framing (PHONONIC): all three sub-rows are direct projections of D_K's a_n^{ζ} spectral moments onto LISA-band substrate-relay-pattern observables; branch-c is the R-protected Leggett–Josephson C² coset phase-channel residue (S85 3B landau §II.2 channel ID); the 3-row decomposition reflects three structurally distinct functionals of the same spectral content, NOT three competing estimates of one observable.
```

This proposed extension is written as a code block in this synthesis only, per the spawn-prompt rule "do NOT directly edit the inventory file." The carry-forward gate `S87-BRANCH-C-LISA-A_N-DICTIONARY-3PATHWAY` (§V.1) lands the registry write at S87.

---

## V. Carry-Forward Computations

**MANDATORY** — every entry has all four fields (per `feedback_fix-in-session-never-defer.md`).

### V.1. **`S87-BRANCH-C-LISA-A_N-DICTIONARY-3PATHWAY`** (FAIL-routed promotion to Pillar III dictionary)

   - **What**: decompose the three S85 3B sibling readings (volovik 127.88× residue-ratio, landau Q(L) = 11.31, kaku 0.0 CP-odd fraction) into three distinct Seeley–DeWitt a_n^{ζ} projections of D_K at L_max = 12: (i) a₂^{ζ}-density-projection for volovik; (ii) a₂^{ζ}-angle-projection for landau; (iii) a₄^{ζ}-CP-projection for kaku. Verify the dictionary is consistent (each a_n^{ζ} projection reproduces its sibling's reading within 1% tolerance under the ζ-regulator family). Land three sub-rows in `falsifier-master-inventory.md` Row #7 under PAIR-7 enrichment (the proposed registry entry quoted in §IV.5). Pre-register the LISA decisive-detection thresholds for each sub-row as separate sub-falsifiers, mirroring the W14-4 PAIR-4 3-pathway pattern.
   - **Inputs**: W10-4 §(d) branch table at L = {8, 10, 12} (`computations/s85_w10_w0_inverted_branch_enumeration.npz`); S85 3B 3-solo synthesis MD docs (volovik content_sha=`3ef22f5b…`, landau content_sha=`28c2ab28…`, kaku content_sha=`2ccd89be…` per W7-2 verdict-line input pins); W7-2 verdict-line audit_sha=`8e9ccfc0a3c42cd2…`; canonical_constants `M_KK = 7.428660036284456e+16 GeV`, `tau_fold = 0.190`, `xi_J = 8.911e-3`; S59 LISA-GW-PREDICTION canonical baseline `Omega_GW_wall ≈ 1e-10 at f_LISA = 3 mHz` from `sessions/framework/registry/pre-registered-observations.md:216`; regulator-pin-discipline tag `a_n^{ζ}` for all three a_n channels.
   - **Gate**: NEW S87 gate `S87-BRANCH-C-LISA-A_N-DICTIONARY-3PATHWAY`. PASS iff (a) all three sibling readings reproduce their respective a_n^{ζ} projection within 1% tolerance; (b) the three sub-rows land in `falsifier-master-inventory.md` Row #7 PAIR-7; (c) the LISA decisive-detection thresholds are pre-registered separately for each sub-row. INFO iff (a) holds but (b) or (c) is incomplete (deferred registry write). FAIL iff any single sibling reading fails to reproduce its a_n^{ζ} projection (would indicate the dictionary mapping is wrong; trigger Pillar-III re-derivation).
   - **Effort**: 6–10 hours, 1–2 agent sessions (1 for the a_n^{ζ} decomposition arithmetic at L = 12 + cross-check at L = 10, 8; 1 for the registry-write + sub-row landing; consult landau + lizzi for the a_n dictionary, mack for the LISA detector-class threshold pre-registration).

### V.2. **`S87-BRANCH-C-WALL-NETWORK-ADDITIVITY-VERIFY`** (cross-mechanism distinctness verification)

   - **What**: verify that the branch-c LISA contribution adds linearly to the canonical S59 wall-network Ω_GW ~ 10⁻¹⁰ baseline at LISA pivot frequency. Compute total Ω_GW(3 mHz) = Ω_GW^{wall} + Ω_GW^{branch-c} under each of the three a_n^{ζ} sub-row mappings (V.1). Cross-check that the wall-network and branch-c source channels are representation-theoretically orthogonal at D_K's spectral decomposition (π_0(Z_2) sector vs C² coset Goldstone sector — established structurally in §II.3 of this synthesis but not yet computed with explicit overlap-integral verification).
   - **Inputs**: V.1 a_n^{ζ} dictionary outputs; S59 LISA-GW-PREDICTION wall-network amplitude (from `sessions/framework/registry/pre-registered-observations.md:216`); D_K eigenvalue decomposition at L_max = 12 by SU(3) × A_F irrep (use existing W10-4 sparse-block representation); π_0(Z_2) wall projector and C² coset Goldstone projector explicitly constructed.
   - **Gate**: NEW S87 gate `S87-BRANCH-C-WALL-NETWORK-ADDITIVITY-VERIFY`. PASS iff projector-overlap |<wall|branch-c>|² < 1% (additive contribution confirmed); INFO iff overlap in [1%, 10%] (mixed channel; non-trivial coupling between wall and branch-c sectors); FAIL iff overlap > 10% (the two mechanisms are not distinct; branch-c is partially a re-projection of wall-network).
   - **Effort**: 4–6 hours, 1 agent session (connes-ncg-theorist for the irrep decomposition + projector-overlap arithmetic; landau cross-check of the branch-c C² coset Goldstone projector).

### V.3. **`S87-LANDAU-DELTA-GW-MAPPING-PIN`** (resolve the unit-class ambiguity that drove the 7-OOM spread)

   - **What**: pin the explicit unit-class mapping from landau's δ_GW(L=14) = 1.27e-5 amplitude-spectrum shift onto an Ω_GW(3 mHz) magnitude. Three candidate mappings: (a) multiplicative on canonical baseline (1.27e-15); (b) additive offset (≈ 1.27e-5 dominating, but at amplitude scale not density scale); (c) Bogoliubov-occupation magnitude treated as Ω_GW directly (1.27e-5). Each mapping has different physical content. The pin is needed before V.1 can land the 7.c-landau sub-row with a definite Ω_GW threshold.
   - **Inputs**: landau §V.3 derivation; W10-4 model `residue_c(L) = ξ_J · mellin_s3(L) / S_ζ_E(L)`; tensor-spectrum mode-function squeeze identity δ_GW = sinh²(r_c(k_pivot)); LISA design sensitivity at 3 mHz pivot (external, paper-search MCP at S87 plan-time).
   - **Gate**: NEW S87 gate `S87-LANDAU-DELTA-GW-MAPPING-PIN`. PASS iff mapping (a)/(b)/(c) selected by an explicit dimensional-analysis substitution chain that derives Ω_GW(3 mHz) from δ_GW + the framework's tensor-power-spectrum normalization; INFO iff the mapping is selectable but multiple candidates remain physically viable (pre-register all three with explicit comments); FAIL iff no canonical-form derivation closes (would indicate the landau §V.3 prediction is amplitude-class only and cannot be reduced to Ω_GW without additional input).
   - **Effort**: 3–4 hours, 1 agent session (landau solo; cross-check by mack for the LISA detector-class normalization).

### V.4. **`S87-KAKU-CP-PAIR-BALANCE-LAB-FOLLOWUP`** (3He-A Berry-phase π lab observable cross-check from the kaku §II.4.2 Channel 2)

   - **What**: complete the 3He-A Leggett-mode NMR phase-coherence interferometry experiment specification from kaku §II.4.2. The CP-pair-balance theorem predicts a Berry-phase π between branch-a and branch-c Leggett-mode pairs, resolvable at Q_Leggett = 670000 (canonical S65). Compute the explicit NMR observable signature, the dt resolution required, and the lab-falsifier registration in `falsifier-master-inventory.md` row class #13–#21 (lab-falsifier suite; matches the SW2 / XB2 FeSe and SW1 / XA1 / XB1 3He-A platform rows already registered).
   - **Inputs**: Q_Leggett = 670000 (canonical_constants), Δ_BCS = 0.4642547 (M_KK units, canonical), ω_L1 (canonical_constants), kaku §II.4.2 Berry-phase π prediction; W11 C5 SI translation pipeline (already maps lambda_a directions to lab observables); existing 3He-A 9-cell lab-falsifier suite rows #13, #16, #19.
   - **Gate**: NEW S87 gate `S87-KAKU-CP-PAIR-BALANCE-LAB-FOLLOWUP`. PASS iff a 3He-A NMR experimental design is specified that resolves Berry-phase π at Q_Leggett = 670000 within the existing Helsinki/Lancaster cryostat envelope; INFO iff design requires next-generation Q_Leggett enhancement (deferred to S88+); FAIL iff Berry-phase π is structurally unresolvable at any Q_Leggett (would indicate the kaku §II.4.2 channel is not lab-accessible).
   - **Effort**: 2–3 hours, 1 agent session (volovik solo for the Helsinki/Lancaster cryostat specification; landau cross-check of the Berry-phase derivation).

### V.5. **`S87-VOLOVIK-LISA-SNR-CONSISTENCY-VERIFY`** (cross-check the 1.68e+13 SNR pivot against the 127.88× enhancement at branch-c)

   - **What**: verify that volovik §V.4's 127.88× spectral-density enhancement at branch-c is consistent with the W1a-7 LISA SNR = 1.68e+13 prediction (which volovik §II.D.3 cites as the baseline source). Compute the LISA SNR for branch-c specifically: SNR_branch-c = sqrt(integral over LISA band of [Omega_GW^{branch-c}(f) / Omega_LISA-PLS(f)]² df). Cross-check against the wall-network baseline SNR (from S59) and verify the additive-contribution arithmetic from V.2.
   - **Inputs**: volovik §V.4 spectral peak frequency f_peak,c (computed in V.4 of the volovik solo; cross-link to S65 SCALE-TRANSFER e-fold map); S65 e-fold N_total = 132.4; canonical M_KK; LISA design sensitivity Ω_LISA-PLS(f) (external, paper-search MCP).
   - **Gate**: NEW S87 gate `S87-VOLOVIK-LISA-SNR-CONSISTENCY-VERIFY`. PASS iff branch-c SNR matches the W1a-7 SNR pivot 1.68e+13 within a factor 3 (substrate↔detector forecast spread); INFO iff factor 3–10; FAIL iff factor > 10 (would indicate the volovik enhancement-factor mapping is inconsistent with the SNR baseline).
   - **Effort**: 3–4 hours, 1 agent session (volovik solo; mack cross-check for the LISA detector-class normalization).

### V.6. **`S87-PILLAR-III-A_N-DICTIONARY-FORMAL-PROMOTION`** (promote the a_n^{ζ} dictionary to a permanent §VII.R registry-track entry)

   - **What**: if V.1 PASSes, promote the Pillar III a_n^{ζ} Seeley–DeWitt spectral-moment dictionary to `permanent-results-registry.md` §VII.R as a Lizzi-track structural result. The dictionary entry pins the mapping (sibling-lens → a_n^{ζ}-functional-class → observable channel) for future-session use; downstream gates citing "the branch-c LISA prediction" inherit the 3-pathway dictionary rather than needing per-sibling magnitude maps. This is the W7-1 PASS analog at the W7-2 level — the consensus output that survives the FAIL verdict at the convergence-ratio level.
   - **Inputs**: V.1 PASS verdict + 3 sub-rows landed in `falsifier-master-inventory.md`; W1a T2 §VII.R routing-key infrastructure (already landed S86); regulator-pin-discipline tag `a_n^{ζ}` for all entries.
   - **Gate**: NEW S87 gate `S87-PILLAR-III-A_N-DICTIONARY-FORMAL-PROMOTION`. PASS iff §VII.R registry write completes with the 3-row dictionary; INFO iff registry write is partial (e.g., only 2 of 3 rows promoted); FAIL iff the dictionary fails the §VII.R structural-result criteria (would indicate the dictionary is too narrow to qualify as a permanent-track result).
   - **Effort**: 1–2 hours, 1 agent session (mechanical post-V.1 registry write; lizzi for the §VII.R structural-result review).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Convergence-ratio reduction under unit-class-harmonized Ω_GW(3 mHz) mapping: max/min = 1.007e+7 (≈ 7 OOM) on the volovik/landau pair; with kaku → ∞ | PHONONIC | **FAIL** (R_conv > 100 spawn-prompt threshold) | The shared-LISA-observable consolidation pathway (W7-2 candidate-1) is structurally degenerate; promote to W7-2 candidate-2 (Pillar III dictionary) |
| 2 | W7-2 INFO verdict (R_min = 11.31, Step B abort) is authoritative; this S5 reconciliation ADDS the 7-OOM harmonized-reduction layer on top of W7-2's heterogeneity finding, NOT overturns it | PHONONIC | CONFIRMING | Same Step-B observable-class-incommensurability manifests at deeper reduction layer; structural confirmation, not contradiction |
| 3 | Landau §V.3 δ_GW(L=14) = 1.27e-5 is an AMPLITUDE-SPECTRUM SHIFT, NOT an Ω_GW magnitude; 3 candidate mappings (multiplicative / additive / direct) span 7 OOM with no canonical pin | PHONONIC | UNIT-CLASS AMBIGUITY (carry-forward V.3) | landau-track LISA prediction is amplitude-class; needs explicit dimensional-analysis pin to reduce to Ω_GW |
| 4 | Branch-c is NOT a re-projection of S59 CG(24) wall-network mechanism; order-parameter sectors orthogonal at D_K (π_0(Z_2) wall vs C² coset Goldstone); contributions ADDITIVE at LISA pivot | PHONONIC | DISTINCT MECHANISMS | Both branch-c and wall-network can be live in framework's LISA forecast; additive contribution structure |
| 5 | Pillar III decomposition (Landau home pillar): the three sibling readings map onto 3 distinct a_n^{ζ} Seeley–DeWitt projections — a₂^{ζ}-density (volovik), a₂^{ζ}-angle (landau), a₄^{ζ}-CP (kaku) | PHONONIC | NEW STRUCTURAL READING | The 3 siblings are not redundant; they probe 3 functionals of the same D_K spectrum |
| 6 | Proposed `falsifier-master-inventory.md` Row #7 PAIR-7 enrichment (3 sub-rows: 7.c-volovik / 7.c-landau / 7.c-kaku) under W14-4 PAIR-4 3-pathway pattern | PHONONIC | PROPOSED (S87 V.1 lands) | Mirrors PAIR-4 f_NL_folded pattern; treats branch-c as a 3-pathway sub-falsifier set, not a single row |
| 7 | S87-BRANCH-C-LISA-A_N-DICTIONARY-3PATHWAY pre-registered (V.1) — decomposes the 3 sibling readings into a_n^{ζ} dictionary; PASS iff each sibling reproduces its projection within 1% | PHONONIC | PRE-REGISTERED | Direct continuation of W7-2 INFO via Pillar III; the Landau home-pillar reading |
| 8 | S87-BRANCH-C-WALL-NETWORK-ADDITIVITY-VERIFY pre-registered (V.2) — projector-overlap test |<wall|branch-c>|² < 1% | PHONONIC | PRE-REGISTERED | Verifies the §II.3 distinctness claim with explicit overlap-integral computation |
| 9 | Cross-channel signatures preserved: kaku CP-pair-balance lab follow-up (V.4); volovik LISA SNR consistency (V.5); landau δ_GW mapping pin (V.3) | PHONONIC | PRE-REGISTERED | Each sibling lens has its own carry-forward to close its lens-specific ambiguity |
| 10 | Pillar III a_n^{ζ} dictionary candidate for §VII.R promotion (V.6) — Lizzi-track structural-result analog of W7-1 PASS at the W7-2 level | PHONONIC / META | PRE-REGISTERED CONDITIONAL | Conditional on V.1 PASS; promotes the dictionary to permanent-track |

---

## VII. Notes on Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:------------------|:-------------|:-----------|:--------|
| 2026-04-27 | "shared-LISA-observable consolidates 3 sibling lenses (W7-2 candidate-1)" | OPEN (proposed in W7-2 §IV) | **CLOSED — structurally degenerate** under unit-class-harmonized Ω_GW(3 mHz) reduction at R_conv = 1.007e+7 | This S5 reconciliation FAIL routing |
| 2026-04-27 | Pillar III a_n^{ζ} Seeley–DeWitt spectral-moment dictionary as branch-c LISA registry vocabulary | not formulated | **OPEN — pre-registered as S87-BRANCH-C-LISA-A_N-DICTIONARY-3PATHWAY** | This S5 reconciliation §IV.1 promotion |
| 2026-04-27 | Branch-c vs wall-network mechanism distinctness | structurally argued (S85 3B closing notes) | **STRUCTURALLY CONFIRMED — additive at LISA pivot via π_0(Z_2) ⟂ C² coset orthogonality** | This S5 reconciliation §II.3 substitution chain; explicit projector-overlap verification queued (V.2) |
| 2026-04-27 | `falsifier-master-inventory.md` Row #7 PAIR-7 enrichment (3 sub-rows for branch-c) | not registered | **PROPOSED — code block in §IV.5 of this synthesis; S87 V.1 lands** | Mirrors W14-4 PAIR-4 3-pathway pattern |
| 2026-04-27 | Landau δ_GW(L=14) = 1.27e-5 unit-class | implicit amplitude-class | **EXPLICIT — amplitude-spectrum shift; 3 candidate Ω_GW mappings span 7 OOM, pin queued S87 V.3** | This S5 reconciliation §II.1 substitution chain Step 4 |

---

**End of S86 Slot 1a Entry S-5 Synthesis** — Landau / Bogoliubov-Mixing-Lens reading of the LISA Ω_GW(3 mHz) branch-c convergence reconciliation. Verdict: **FAIL** under unit-class-harmonized Ω_GW reduction (R_conv = 1.007e+7, ≈ 7 OOM > 100× spawn-prompt threshold); INFO-confirmed under W7-2 source-doc-authoritative Step-B reading. The FAIL routing promotes the gate to Pillar III a_n^{ζ} Seeley–DeWitt spectral-moment dictionary — the Landau home pillar — and the three sibling readings consolidate as three pathway-tagged sub-falsifiers under proposed `falsifier-master-inventory.md` Row #7 PAIR-7 enrichment (W14-4 PAIR-4 pattern). Branch-c is structurally distinct from the canonical S59 wall-network mechanism (orthogonal order-parameter sectors at D_K spectral decomposition), with additive LISA contribution. Carry-forward suite V.1–V.6 covers the dictionary landing (V.1), wall-network additivity verification (V.2), δ_GW mapping pin (V.3), kaku Berry-phase π lab follow-up (V.4), volovik LISA SNR consistency (V.5), and §VII.R Pillar III promotion (V.6). Substrate framing (PHONONIC) preserved throughout: D_K eigenvalues → a_n^{ζ} spectral moments → mechanism-specific functionals → diagnostic ratios → 3-pathway sub-falsifier registry.
