# Class-A Decisive Triplet (F1 + F2 + F5) — Aalto LTL Lab Dispatch Pre-Registration

> **Status**: Pre-registered S88 W4c-32 (`S88-3HE-B-CLASS-A-LAB-DISPATCH`; volovik PRIMARY; orchestrator-direct in /rclab-solo, 2026-05-04). Multi-year cycle 2027–2030.
>
> **Cross-references**: `.claude/rules/inheritance-falsifier-protocol.md` §"Two Test Classes" + §"Four-Gate Structure" (W11-C5 calibration corpus); `sessions/permanent-results-registry.md` §VII.AF.1 (substrate-side anchor); §W4c-25 Lancaster F1 cross-platform; §W4c-31 Aalto LTL coordination matrix.

## Section A — Per-Row Substrate Predictions (volovik PRIMARY)

The Class-A kernel-signature decisive triplet (F1, F2, F5) consists of
three substrate-clean cocycle observables, each probing an independent
generator in `ker(ι_*)`. Per `inheritance-falsifier-protocol.md` §"Two
Test Classes":

> "Class A — Kernel-Signature Test: row-wise NULL prediction across
> each F-row of the falsifier inventory ... [confirms] BdG-restricted
> spectrum carries no ker(ι_*) cocycle."

**Row F1 — Caroli-Matricon ladder asymmetry** (Volovik 2003 §6):
- Substrate cocycle: [φ_67] (chiral pair, angular OFF-diagonal sector)
- Substrate margin: ‖[φ_67]‖_{Caroli-Matricon} = 0.573193 M_KK² (S86 W-5 §VII.AF.1 calibration)
- Lab observable: F1 = (E_+ − E_-)/(E_+ + E_-) at vortex-core n=0 minigap
- Substrate prediction: F1^{lab} = NULL at substrate-clean level (Class-A kernel-signature)
- Class-A direction: NULL is structural-cohomological, not statistical-precision

**Row F2 — NMR satellite peak ratio** (cocycle partner of φ_67):
- Substrate cocycle: derived from φ_67 (cocycle partner channel; S86 W-5 §VII.AF.1)
- Substrate margin: derived from same chiral-pair structure as F1; analogous M_KK² order of magnitude
- Lab observable: ratio of NMR satellite peak intensities probing the off-diagonal channel
- Substrate prediction: F2^{lab} = NULL (Class-A kernel-signature; same ker(ι_*) generator family)

**Row F5 — Andreev reflection edge-state asymmetry** (chiral pair of φ_67):
- Substrate cocycle: chiral pair partner of φ_67 in the (lambda_6, lambda_7) sector
- Substrate margin: derived analogously from S86 W-5 calibration
- Lab observable: edge-state asymmetry from Andreev reflection at the BdG sector boundary
- Substrate prediction: F5^{lab} = NULL (Class-A kernel-signature)

**Decisive vs supporting separation**: F1 + F2 + F5 are substrate-CLEAN
cocycle generators (each probes ONE independent ker(ι_*) element);
their combined NULL prediction is the substrate's most decisive Class-A
falsifier set. Rows F3 + F4 are cocycle-DEGENERATE (multiple substrate
cocycles superpose at those observables); they require the slope-
discrimination Gate-4 from the 4-Gate Structure (handled at §W4c-34
(Δ_B/Δ_A) calibration family).

## Section B — Aalto Group / Cell Assignment Per Row (volovik + sagan)

Each row maps to an independent Aalto observable per the §W4c-31
multi-session coordination matrix:

| Row | Aalto group | Cell + method | Lab observable |
|:----|:------------|:--------------|:----------------|
| F1 | Krusius | ROTA channel + transverse-NMR ladder | First-harmonic ladder asymmetry |
| F2 | Krusius | ROTA channel + longitudinal NMR | Satellite peak ratio (90°-rotated coil) |
| F5 | Tuoriniemi | Nanofluidic 3He cell + Andreev reflection | Edge-state asymmetry from sub-µm channel walls |

**Why two of three to Krusius**: F1 + F2 both rely on the rotation-
stabilized vortex array; the same ROTA cell generates both observables
modulo the transverse-vs-longitudinal NMR coil rotation. This shares
the cell-engineering overhead and provides cross-checking within the
same physical sample.

**Why F5 to Tuoriniemi**: the nanofluidic 3He cell's sub-µm channel
geometry creates a controlled BdG-sector boundary at the wall;
Andreev reflection from this boundary directly samples the edge-state
asymmetry of the chiral-pair cocycle. Krusius ROTA cannot replicate
this geometry (rotation requires bulk fluid).

## Section C — Statistical-Power Forecast Per Row at 9σ S/N (sagan + volovik)

The lab S/N forecast for each row at the Aalto LTL cell sensitivity
delivers σ_F_i ≈ 9.0 per one-decade pressure window 0–34 bar. The
per-row statistical-power calculation:

    σ_F_i / F_substrate = 1 / (S/N · √N_obs)
                        = 1 / (9 · √(10⁴))
                        ≈ 1.11e-3 per pressure step
                        ≈ 0.001 aggregated over 10 pressure steps

A non-NULL detection at the 9σ level on ANY single row falsifies the
substrate Class-A prediction unless the Class-B cohomology-asymmetry
ratio test (§W4c-26 / §W4c-33) survives in the cross-cocycle channel
— the substrate's overall PASS requires NULL-on-rows AND ratio-on-cross
per `inheritance-falsifier-protocol.md` §"Two Test Classes".

Statistical-power calculation assumes:
- N_obs = 10⁴ per pressure step (forecast at Aalto LTL ensemble size)
- 10 pressure steps per decade (logarithmic spacing 0–34 bar)
- Independent measurements per row (independent statistical aggregation)

Cross-platform replication at Lancaster MCT-3 (§W4c-25) provides an
INDEPENDENT 9σ NULL test on F1, doubling the Class-A discrimination
power against single-platform systematics.

## Section D — Inventory Rows #45 + #47 + #48 Update Target (mack — SOLO-MODE DEFERRED)

> **Solo-mode disclosure**: this section pre-registered with substrate-
> physics content authored by volovik PRIMARY; the falsifier-master-
> inventory.md rows #45 + #47 + #48 update is the mack-cosmic-bridge
> sole-writer deliverable. /rclab-solo Phase 2 step 2 forbids subagent
> spawning; the row updates are DEFERRED to a Wave-5 mack write-batch.

**Inventory row update target** (DEFERRED):
- Row #45 (Lancaster Caroli-Matricon F1 NULL) — already addressed at §W4c-25; this gate adds Aalto Krusius ROTA F1 SHA cross-link
- Row #47 (F2 NMR satellite ratio) — Aalto Krusius longitudinal NMR coordination SHA + 9σ S/N forecast
- Row #48 (F5 Andreev edge-state asymmetry) — Aalto Tuoriniemi nanofluidic Andreev coordination SHA + 9σ S/N forecast

**Decisive-triplet leverage**: a single non-NULL detection on any one
of F1, F2, F5 falsifies the substrate Class-A prediction directly
(modulo Class-B rescue). Three independent rows × two platforms
(Lancaster + Aalto) = SIX independent NULL tests on the kernel-signature
prediction. The falsifier-master-inventory.md row structure makes this
explicit; the mack write-batch installs the cross-link SHAs.

**Substrate framing**: F1, F2, F5 are NOT three "different experiments"
— they are three independent observables, each probing a substrate-
clean cocycle generator in `ker(ι_*)`. The decisive triplet is the
substrate's most leverage-rich falsifier set: a non-NULL on any ONE
row falsifies the substrate Class-A prediction (modulo Class-B rescue).
Direction of explanation: A_K cocycle pair → χ inheritance → BdG-sector
image → three Aalto observables → three NULL predictions at 9σ S/N.

**Cross-pillar bridge anatomy** (5 IS-not-IN):
1. Substrate-IS: ‖[φ_67]‖_{F1, F2, F5} on `(A_K, H_K, D_K)`.
2. Laboratory-IN: F1^{lab}, F2^{lab}, F5^{lab} at Aalto LTL three-group cells.
3. Bridge map: ι_*: A_K → M_2(ℂ) ∘ (Δ_B/Δ_A)^p per row.
4. Algebraic envelope: per-row substrate margin ± 9σ statistical band.
5. Empirical anchor: NULL on all three rows.

**3-level ladder**: Level 1 (kernel-signature cohomology identity, regulator-invariant) → Level 2 (structural-exact NULL form, no L_max⁻α envelope) → Level 3 (lab anchor DEFERRED to 2027–2030 multi-row campaign).
