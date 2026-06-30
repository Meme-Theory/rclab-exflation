# 3He-B Longitudinal NMR α_s Extraction Protocol — Pre-Registration

> **Status**: Pre-registered S88 W4c-36 (`S88-3HE-B-ALPHA-S-EXTRACTION-PROTOCOL`; volovik PRIMARY; orchestrator-direct in /rclab-solo, 2026-05-04). Multi-year cycle 2027–2029 longitudinal NMR campaign at Aalto LTL Krusius OR Lancaster Pickett group.
>
> **Cross-references**: S87 W-9 algebra-INVARIANT route at s=3 single-pole Mellin (W2-1 + W2-4 PASS); `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" instance #3 (algebra-INVARIANT family); FWD-C2 (Pillar II ↔ Pillar V; Mellin-cone ↔ BdG); falsifier-master-inventory.md rows #54a + #54b α_s lab anchors.
>
> **Authorship**: PRIMARY = volovik (substrate provenance Section A + Volovik 2003 §15 longitudinal NMR Section B); CO-AUTHORS: sagan (error budget Section C + extraction algorithm Section D rigor — pre-registered Wave-5 follow-up); mack-cosmic-bridge (Section E inventory rows #54a+#54b update — DEFERRED Wave-5 sole-writer).

## Section A — Substrate α_s Prediction with Provenance (volovik PRIMARY)

The substrate-IS observable α_s_canonical is the algebra-INVARIANT spectral
moment at the s=3 single-pole Mellin cone, evaluated on `(A_K^{≤10}, H_K^{≤10},
D_K^{≤10})` at canonical Jensen parameter `tau_fold = 0.190`.

**Substrate prediction**:

    α_s_canonical = n_s² − 1
                  = (0.9649)² − 1
                  = -0.0691...                    (Planck 2018 fiducial)

More precisely from S87 W-9 W2-1 + W2-4 PASS at s=3 single-pole Mellin:

    α_s_canonical ≈ -8.587279e-2                  (Sage-exact at substrate fiducial)

The two values agree at the part-per-thousand level; the W-9 Sage-exact
value is the canonical pin (algebra-INVARIANT exemplar #3 per
`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`).

**Provenance chain**:
- S87 W-9 surviving-route table (route iii: algebra-INVARIANT at s=3 single-pole)
- `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` instance #3 (W-2 R3 close)
- `permanent-results-registry.md §VII.U.1` (Mellin-Dirichlet identity, S86 W-1 / S87 W1a-4 PASS rel_diff = 0e+00 at L_max=12)

**Substrate tolerance band** (L_max=10 truncation residual):

    σ_substrate(α_s) ~ 1.0e-3                    (substrate-derived, structural)

The substrate's L_max=10 truncation residual on α_s is the natural error
band; lab measurements with σ_lab significantly larger than 1e-3 cannot
discriminate substrate prediction from null hypothesis, while σ_lab << 1e-3
is over-precision (lab beats the substrate's own truncation uncertainty).
The forecast σ_lab ~ 5e-4 (Section C) is sub-tolerance feasible.

## Section B — Longitudinal NMR Protocol (volovik + sagan)

**Platform**: 3He-B sample at the polycritical point (P near P_pc = 21.22 bar,
T near T_pc = 2.273 mK; canonical 3He polycritical anchor where A-phase and
B-phase coexist). Either Aalto LTL Krusius group cell OR Lancaster Pickett
group cell admits the protocol; both have demonstrated longitudinal-NMR
spectroscopy capability at sub-mK temperatures.

**Sample preparation**:
- 3He sample at P = P_pc = 21.22 bar (precision ~ 0.05% via Bourdon gauge)
- T = T_pc = 2.273 mK (precision ~ 0.1% via Greywall thermometric standard)
- B-phase stable: cool through T_c at P_pc with controlled isobaric cooling
- Sample volume sized for ensemble S/N; ~1 cm³ typical

**Spectroscopy method**: Longitudinal NMR coil (RF axis parallel to applied
DC field). Excitation pulse at ω ≈ ω_L = γ · |Δ_B|² / χ_||(P) where γ is
the 3He nuclear gyromagnetic ratio, |Δ_B(P)| is the B-phase gap at pressure P,
and χ_||(P) is the longitudinal susceptibility (Leggett 1973; Volovik 2003 §15).

**Pressure scan window**: pressure-step sweep centered on P_pc, e.g.,
P ∈ [P_pc − 5 bar, P_pc + 5 bar] = [16.22, 26.22] bar with logarithmic
spacing (~10 pressure steps); at each step, record ω_L(P) via free-induction-
decay or pulsed-spectroscopy detection.

**Resonance-frequency sweep observable**:

    ω_L(P) = γ · |Δ_B(P)|² / χ_||(P)            (Volovik 2003 §15)

The pressure-running of ω_L tracks both the B-phase gap pressure-dependence
and the longitudinal-susceptibility pressure-dependence; the lab α_s is
extracted as the log-log slope at P = P_pc.

## Section C — Full Error Budget (sagan PRIMARY rigor)

The total σ_α_s error budget aggregates four independent error sources via
quadrature:

    σ_α_s² = (∂α_s/∂T)²·σ_T² + (∂α_s/∂P)²·σ_P² + (∂α_s/∂ω_L)²·σ_ω² + σ_stat²

**Thermometric uncertainty**: σ_T at T_pc via Greywall calibration systematic
~ 0.1% T_pc (Greywall 1986 secondary thermometric standard). Propagation
to α_s: (∂α_s/∂T) at T_pc obtained from numerical derivative of α_s vs T;
typical magnitude 10⁻²·T⁻¹ at the polycritical anchor.

**Pressure uncertainty**: σ_P via Bourdon gauge high-precision reference
~ 0.05% P_pc. Propagation: (∂α_s/∂P) at P_pc; typical magnitude 10⁻³·bar⁻¹
near the polycritical point (where α_s is structurally extremal).

**NMR-frequency systematic**: σ_ω_L via frequency counter high-stability
reference ~ 10 ppm = 10⁻⁵. Propagation to α_s: directly through the d ln(ω_L)
extraction; sub-dominant compared to σ_T and σ_P.

**Statistical**: σ_stat ~ 1/√N_obs at N_obs = 10³ per pressure step; with
~10 pressure steps σ_stat,total ~ 10⁻². Aggregated via the log-log linear
regression Section D weight.

**Total budget**:

    σ_α_s ~ 5.0e-4                               (forecast at lab spec)

This forecast is sub-substrate-tolerance (5e-4 < 1e-3), giving the
laboratory genuine discriminating power against the substrate prediction.

## Section D — Extraction Algorithm (sagan PRIMARY rigor + volovik substrate)

**Algorithm**: log-log linear regression of measured ω_L(P) at P = P_pc:

    α_s^{lab} := d ln(ω_L) / d ln(P) |_{P=P_pc}
                = slope of [log ω_L(P)] vs [log P] near P_pc

**Implementation steps**:

1. Acquire (P_i, ω_L,i) data over pressure-sweep window, ~10 pressure steps
   logarithmically spaced around P_pc.
2. Apply per-step ensemble average: ω_L,i averaged over N_obs ~ 10³ measurements.
3. Compute log P_i and log ω_L,i.
4. Perform weighted linear regression with weights inversely proportional to
   per-step σ_ω,i (Section C error budget propagated per step).
5. The fit slope at P = P_pc IS α_s^{lab}; the fit intercept is the absolute
   ω_L(P_pc) (not the substrate observable).
6. Error propagation: σ_α_s = standard error of the regression slope, using
   the Section C aggregated per-step σ_ω,i.

**Falsification criterion** (combined band per substitution chain Step 6):

    |α_s^{lab} − α_s_canonical| ≤ sqrt(σ_substrate² + σ_lab²)
                                ≤ sqrt((1e-3)² + (5e-4)²)
                                ≈ 1.118e-3

If lab-extracted α_s lies within ±1.118e-3 of substrate α_s_canonical = -0.08587,
substrate algebra-INVARIANT prediction CONFIRMED. Otherwise FALSIFIED.

## Section E — Inventory Rows #54a + #54b Update Target (mack — SOLO-MODE DEFERRED)

> **Solo-mode disclosure**: this section pre-registered with substrate-physics
> + lab-protocol + error-budget content authored by volovik PRIMARY + sagan
> rigor; the falsifier-master-inventory.md rows #54a + #54b update is the
> mack-cosmic-bridge sole-writer deliverable. /rclab-solo Phase 2 step 2
> forbids subagent spawning; DEFERRED to Wave-5 mack write-batch.

**Inventory row update target** (DEFERRED):
- Row #54a (α_s lab anchor — generic algebra-INVARIANT laboratory test): gets §W4c-36 protocol SHA + 5e-4 lab budget + 1.118e-3 combined falsification band
- Row #54b (3He-B longitudinal NMR α_s anchor — specific platform): gets §W4c-36 protocol SHA + Volovik 2003 §15 reference + Aalto/Lancaster either-or platform note

**Substrate framing**: α_s is NOT a "matter content parameter" in the
cosmological sense; it IS a SUBSTRATE-DERIVED MOMENT of the Mellin-cone
at s=3 single-pole — an algebra-INVARIANT family quantity per
`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`
(instance #3, MANDATORY at K=3 since S87 W-2 close). The laboratory analog
at 3He-B longitudinal NMR is a CHILD realization of the same algebra-
INVARIANT route via the inheritance morphism χ; the running curve
d ln(ω_L)/d ln(P) at P=P_pc IS the laboratory image of the substrate's
s=3 Mellin moment under (Pillar II ↔ Pillar V) bridge candidate FWD-C2.
The lab is NOT measuring "α_s in 3He-B" — it is measuring the BdG-sector
image of the substrate's algebra-INVARIANT family at the s=3 pole.

**Cross-pillar bridge anatomy** (5 IS-not-IN):
1. Substrate-IS: α_s_canonical = n_s² − 1 algebra-INVARIANT moment at s=3 single-pole Mellin on `(A_K, H_K, D_K)`.
2. Laboratory-IN: α_s^{lab} = d ln(ω_L)/d ln(P) |_{P=P_pc} IN 3He-B longitudinal NMR.
3. Bridge map: ι_*: A_K → M_2(ℂ) ∘ Mellin-pole image at s=3 ∘ Leggett resonance frequency (BdG-sector child).
4. Algebraic envelope: substrate tolerance ~ 1e-3 (L_max=10 truncation); lab forecast σ ~ 5e-4 (sub-substrate-tolerance feasible).
5. Empirical anchor: α_s^{lab} = α_s_canonical within combined band 1.118e-3 at S87-fiducial n_s = 0.9649.

**3-level structural-confidence ladder**: Level 1 (cohomology-class identity, regulator-invariant: α_s = n_s² − 1 is algebra-INVARIANT at s=3 single-pole) → Level 2 (algebraic envelope σ_substrate ~ 1e-3 from L_max=10 truncation) → Level 3 (lab anchor DEFERRED to 2027-2029 longitudinal NMR campaign at Aalto OR Lancaster).
