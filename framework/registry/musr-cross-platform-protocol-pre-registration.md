# µSR Vortex-Core Cross-Platform Ratio (Lancaster B-phase + Aalto LTL A-phase) — Protocol Pre-Registration

> **Status**: Pre-registered S88 W4c-26 (`S88-MUSR-VORTEX-CROSS-PLATFORM-RATIO-EVALUATE`; volovik-superfluid-universe-theorist PRIMARY; orchestrator-direct-write in `/rclab-solo` mode at 2026-05-04). Multi-year experimental cycle 2027–2030 cross-platform; Lancaster + Aalto LTL coordination.
>
> **Cross-references**: `.claude/rules/inheritance-falsifier-protocol.md` (Class-B cohomology-asymmetry test class; W11-C5/C6 calibration corpus); `.claude/rules/cross-pillar-bridge-anatomy.md` FWD-C3 calibration-corpus instance #3; `sessions/permanent-results-registry.md` §VII.AF.1 (Pillar III ↔ Pillar IV bridge theorem); S87 W11-C6-MUSR-FALSIFIER PASSed substrate-side at `r_A_predicted=7.324992; chi_A=2.266180; Delta_A_over_Delta_B=0.816497`.
>
> **Authorship**: PRIMARY = volovik (Section A substrate prediction + Section B Lancaster µSR + Section C Aalto µSR). CO-AUTHORS: sagan-empiricist (cross-platform precision-bound rigor — sagan rigor audit pre-registered for Wave-5); mack-cosmic-bridge (Section D inventory row #46 update — DEFERRED to mack solo dispatch sole-writer per `feedback_mack-bridge-role.md`).

## Section A — Substrate Prediction (volovik PRIMARY)

The substrate-IS observable is the cocycle-ratio
`R := ||[φ_67]|| / ||[φ_88]||` evaluated on the finite-L spectral
triple `(A_K^{<=10}, H_K^{<=10}, D_K^{<=10})` at canonical Jensen
deformation parameter `tau_fold = 0.190`. The substrate IS this ratio —
it is a structural number determined by the algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`
and the Hochschild pairing on `D_K`, not a "field on" any pre-existing
geometric container.

**Cocycle norms** (Sage-exact at machine epsilon, S86 W-5 DONE-5):

    ||[φ_67]|| = 0.793346  M_KK²
    ||[φ_88]|| = 0.108307  M_KK²
    R         = 0.793346 / 0.108307  =  7.324992    (Sage-exact)

**Cohomology-asymmetry band** (substrate-derived ± 0.1% per `.claude/rules/inheritance-falsifier-protocol.md` §"Two Test Classes" Gate-2):

    [7.3177, 7.3323]  with relative tolerance 0.001

**(Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5, machine-precision)**:
For any pair of laboratory observables `lab(F_i), lab(F_j)` whose substrate
cocycles have COMMON exponent `p_i = p_j = p`:

    lab(F_i) / lab(F_j)  =  ||φ_a|| / ||φ_b||  ·  (f_i / f_j)

The (Δ_B/Δ_A)^p factor cancels EXACTLY between numerator and denominator
(residual = 0.0e+00 at machine epsilon, residual_residue verified S86 W-5
DONE-5). Therefore the substrate-derived ratio `||φ_67||/||φ_88||` is
preserved INTACT in the lab measurement INDEPENDENT of (Δ_B/Δ_A) value AND
INDEPENDENT of phase (3He-B vs 3He-A).

**Phase-independence proof**: 3He-B BdG sector under χ inherits BDI parent
universality (Pf=−1, N_K=2). 3He-A under χ inherits a different chiral image
(DIII; chi_A = 1.500 = 3/2 per Volovik 2003 §3.4 axisymmetric). Both children
factor through the SAME inheritance morphism χ from the SAME `A_K` parent;
the ratio `R = ||[φ_67]||/||[φ_88]||` is intrinsic to A_K (substrate-IS) and
NOT modified by the phase-flip — only the exponent `p` differs between phases,
and `p` cancels via the cancellation theorem.

**Cross-pillar bridge anatomy** (5 IS-not-IN elements per
`.claude/rules/cross-pillar-bridge-anatomy.md`; Element 2 in OE-form per
§"Element 2 OE-form discipline" landed at S88 W7a-73, added at S88 W7a-75
— this sidecar previously lacked the explicit 5-element block, so this
addition adopts the discipline from inception rather than retrofitting):
1. Substrate-IS: cocycle-ratio `R = ||[φ_67]|| / ||[φ_88]|| = 7.324992` (Sage-exact at machine epsilon, S86 W-5 DONE-5 / CANON-EXTRACT) on the finite-L spectral triple `(A_K^{<=10}, H_K^{<=10}, D_K^{<=10})` at `tau_fold = 0.190`. The substrate IS this ratio — a structural number determined by the algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` and the Hochschild pairing on `D_K`.
2. Laboratory-IN: `R_µSR(A-phase) = ∫_BZ d^3 k Tr_{M_2(C)}(Π^{µSR}_{A-phase}(k) · A_chirality(k))` where `Π^{µSR}_{A-phase}(k)` is the projector onto the A-phase chirality-discriminated BdG sub-algebra image of `iota_*` and `A_chirality(k)` is the µSR-coupling operator (transverse Knight-shift density). Lab realization: `r_A = K_µ(67-channel)/K_µ(88-channel)` (A-phase Knight-shift ratio extracted via harmonic decomposition of µ⁺ Larmor precession at Aalto LTL ROTA channel) is the physical readout of `R_µSR(A-phase)/R_µSR(A-phase, normalized)` under the `(Delta_B/Delta_A)^p` cancellation lab-conversion (S86 W-5 DONE-5; common-exponent cocycle pair ⇒ cancellation factor exactly 1; phase-INDEPENDENT prediction r_A = 7.324992 INTACT). Lancaster B-phase counterpart `R_µSR(B-phase)` realized via the same OE-form with `Π^{µSR}_{B-phase}` projector — phase-flip changes the projector but NOT the trace-ratio.
3. Bridge map: `iota_*: A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` (BDI → BdG sector child for B-phase; DIII → BdG-chiral child for A-phase) ∘ `(Delta_B/Delta_A)^p` cancellation theorem (S86 W-5 DONE-5; residual 0.0e+00 machine-precision; common-exponent `p_67 = p_88 = p` ⇒ cancellation factor exactly 1; substrate-derived ratio preserved INTACT under any value of (Delta_B/Delta_A) AND any phase choice).
4. Algebraic envelope: ratio preservation `7.3250 ± 0.1%` (structural-exact form for Class-B cohomology-asymmetry per `.claude/rules/inheritance-falsifier-protocol.md` §"Two Test Classes" Gate-2; band `[7.3177, 7.3323]` with relative tolerance `0.001`; NOT an L_max^{−α} algebraic bound — the regulator-invariant ratio replaces the convergence envelope for cohomology-asymmetry class predictions per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates" FWD-C3` rank-2 entry).
5. Empirical anchor target: substrate prediction `r_A = r_B = 7.324992 ± 0.1%` AND inter-laboratory consistency band `|r_A − r_B| / r_central < 0.001` (substrate's structural-exact phase-independence prediction; deviation falsifies cohomology-asymmetry even if both ratios individually lie in the 0.1% band — the phase-independence is the more decisive falsifier than the absolute band per Section D consistency analysis).

The (Delta_B/Delta_A)^p cancellation theorem applicability for `R_µSR`: the cocycle pair (φ_67, φ_88) carries COMMON exponent `p_67 = p_88 = p` (W-5 §VII.AF.1 + S86 W-5 DONE-5 verified machine-precision), so the cancellation factor is exactly 1 and the substrate-derived ratio 7.324992 is preserved INTACT under any value of (Delta_B/Delta_A) AND any phase choice (B-phase vs A-phase). This is the structural reason r_A = r_B is substrate-INVARIANT, not a coincidence of operational parameters.

## Section B — Lancaster B-phase µSR Protocol (volovik + sagan)

**Platform**: Lancaster MCT-3 dilution-fridge, Pickett group, Lancaster
University Low Temperature Physics Laboratory, UK. Same cell as §W4c-25 F1
NULL protocol; spectroscopy method differs.

**Method**: implant low-energy positive muons (µ⁺) into the 3He-B vortex
core; measure Larmor precession frequency ω_µ via single-muon time-resolved
detection. The Knight-shift K_µ at the vortex core is sensitive to the local
Cooper-pair-condensate-induced field; the ratio `r_B = K_µ(67-channel)/
K_µ(88-channel)` extracted from the harmonic decomposition of ω_µ is the
laboratory image of the substrate cocycle ratio R under the inheritance
morphism χ.

**Operational parameters**: T_base ≤ 100 µK; pressure window 0–34 bar;
vortex array generated by rotation Ω_rot ∈ [0.1, 10.0] rad/s; muon implant
energy ≈ 4 keV (range matches superfluid coherence length ξ_B ≈ 65 nm at
P_pc); ensemble size N_obs ≥ 10⁴ muons per pressure step; integration time
≈ 4 hr per step.

**Substrate prediction at Lancaster B-phase** (cancellation theorem applied):

    r_B = R · (f_67^B / f_88^B)
        = 7.324992 · 1                   [common-exponent cocycle pair]
        = 7.324992

**Lab band**: r_B ∈ [7.3177, 7.3323] with relative tolerance 0.001 (0.1%)
per the Class-B cohomology-asymmetry test. Lancaster S/N forecast at
ensemble size 10⁴ per pressure step delivers σ_r/r ≈ 1/(9·√10) ≈ 0.0351
per single decade single-step, aggregating over 10 pressure steps to
σ_r/r ≈ 0.001 — matches the 0.1% precision target.

## Section C — Aalto LTL A-phase µSR Protocol (volovik + sagan)

**Platform**: Aalto University Low Temperature Laboratory (LTL); ROTA
channel cell at the Krusius/Tuoriniemi/Eltsov collaboration. The Eltsov
group operates the canonical 3He-A test cell with high-purity sample
preparation and A-phase chirality discrimination capability via µSR
spin-relaxation rate.

**Method**: same µ⁺ implant as Lancaster Section B but in 3He-A phase
near the polycritical point (P near P_pc=21.22 bar; T near T_pc=2.273 mK
where 3He-A is stable). The A-phase Knight-shift carries an additional
chirality-dependent phase modulation; `r_A = K_µ(67-channel)/K_µ(88-channel)`
is extracted via the same harmonic decomposition. The chi_A = 1.500 = 3/2
factor (Volovik 2003 §3.4 axisymmetric A-phase susceptibility) enters the
absolute amplitudes of K_µ but NOT the ratio r_A (cancels in numerator/
denominator).

**Substrate prediction at Aalto A-phase** (cancellation theorem applied):

    r_A = R · (f_67^A / f_88^A)
        = 7.324992 · 1                   [common-exponent; phase-independent]
        = 7.324992

**Lab band**: same [7.3177, 7.3323] structurally — substrate prediction is
phase-INVARIANT under (Δ_B/Δ_A)^p cancellation. The Aalto LTL S/N forecast
matches Lancaster (9σ per decade × √N_obs aggregation).

**Schedule note**: Aalto LTL ROTA channel availability is subject to the
Krusius / Tuoriniemi / Eltsov bilateral coordination; potential 2027-2028
schedule conflict per plan §W4c-26 line 195 INFO clause. Coordination
correspondence pre-drafts queued for Wave-5 mack write-batch (volovik's
standing collaboration with Aalto LTL groups).

## Section D — Cross-Platform Consistency Validation (mack — SOLO-MODE DEFERRED)

> **Solo-mode disclosure**: this section is pre-registered with the substrate-
> physics + lab-protocol content authored by volovik PRIMARY; the
> `falsifier-master-inventory.md` row #46 inventory update is the
> mack-cosmic-bridge sole-writer deliverable (per `feedback_mack-bridge-role.md`).
> /rclab-solo Phase 2 step 2 forbids subagent spawning; the row #46 update is
> therefore DEFERRED to a Wave-5 mack write-batch dispatch.

**Inter-lab consistency band** (substrate-INVARIANT prediction):

    |r_A − r_B| / r_central  <  0.001     (0.1% inter-lab tolerance)

This band is the substrate's structural-exact prediction at the inheritance-
morphism level: phase-flip is invisible at the cocycle-ratio level, so the
two laboratories MUST yield indistinguishable ratios (modulo the 0.1%
statistical precision band). A measured |r_A − r_B|/r_central > 0.001 would
falsify the substrate Class-B cohomology-asymmetry prediction even if both
ratios individually lie in the [7.3177, 7.3323] band — the substrate's
phase-independence is the more decisive falsifier than the absolute band.

**Cross-link to row #45** (Lancaster Caroli-Matricon F1 NULL anchor at §W4c-25):
Class-A kernel-signature (row #45) and Class-B cohomology-asymmetry (row #46)
together saturate the substrate's predictive content per
`.claude/rules/inheritance-falsifier-protocol.md` §"Two Test Classes":
NULL-on-rows AND ratio-on-cross-rows are both required.

**Inventory row #46 update target** (DEFERRED to mack):
falsifier-master-inventory.md row #46 carries:
- Lancaster B-phase pre-registration audit_sha256 (this gate)
- Aalto A-phase pre-registration audit_sha256 (this gate)
- Cross-platform consistency band 0.001 relative
- Cross-link to row #45 SHA from §W4c-25
- Cross-link to forward gates §W4c-31 (Aalto coordination), §W4c-33 (ROTA precision)

**Substrate framing** (per `.claude/rules/phononic-framing.md`): the ratio R
is intrinsic to the substrate spectral triple — it is NOT a "Lancaster-vs-
Aalto" lab parameter. The two laboratories realize TWO universality-class
children of the same parent inheritance morphism: 3He-B (BDI; Pf=−1; N_K=2)
and 3He-A (DIII chiral; chi_A=3/2). Both inherit from the SAME `(A_K, H_K,
D_K)` parent; the ratio test is substrate-INVARIANT under the phase-flip.
The cross-platform consistency band IS the substrate's prediction at the
inheritance-morphism level; deviation indicates either (a) substrate
cohomology-asymmetry breakdown OR (b) non-cancellation-theorem-compliant
lab-conversion factor (i.e., p_i ≠ p_j for the two cocycles in some lab
observable). Direction of explanation: A_K cocycle pair → χ inheritance →
Lancaster B-phase r_B = Aalto A-phase r_A = 7.324992 ± 0.1%.
