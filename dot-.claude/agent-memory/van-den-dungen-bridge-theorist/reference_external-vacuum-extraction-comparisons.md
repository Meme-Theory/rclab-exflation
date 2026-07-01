---
name: external-vacuum-extraction-comparisons
description: Two categorical principles for bridging our framework against external vacuum-energy-extraction / EM-drive / dark-sector-coupling proposals (DIA-08-1004-007, White et al. PRR 2026, etc.). Used when adjudicating cross-framework comparisons in my role as bridge theorist.
metadata:
  type: reference
---

# Cross-framework comparison principles for vacuum-extraction proposals

When comparing our framework to external papers proposing vacuum-energy extraction, EM-drive-style propulsion, dark-sector coupling, or analog Casimir engineering (canonical examples: DIA-08-1004-007 "Concepts for Extracting Energy From the Quantum Vacuum"; White et al. PRR 8, 013264 (2026) "Emergent quantization from a dynamic vacuum"; Sonny White / Casimir Inc. line of work), apply these two structural principles before evaluating any specific proposal.

## Principle 1 — Bath-closure categorical principle

In our framework, the substrate is a finite spectral triple `(A_K, H_K, D_K)` with 155,984 eigenvalues at L_max=10. Every operator on the substrate decomposes onto this spectrum. **There is no operator that lives "between" the eigenmodes**; there is no separable "source bath" vs "device sink" partition because all states are co-resident in `H_K`.

External vacuum-extraction proposals implicitly assume a state-space with `E_vacuum` and a separate device-state with `E_device`, and ask how to make `E_device` grow by depleting `E_vacuum`. **This conflates two projections of the SAME spectral content** — at the substrate layer, the algebraic identity `E_vacuum + E_device = const` is structural, not thermodynamic. It's not that you can't get something from nothing; it's that there is no "from" — the bath and the device are co-resident in `H_K`.

This is the structural reason QED's "hardwired ZPF modes" forbid Type-II continuous extraction (per DIA pp. 25-26 taxonomy), and the structural reason any vacuum-engine proposal that frames extraction as "tap the reservoir, drain a fraction into the device" fails *categorically* in our framework — independent of whether the proposal honors energy conservation thermodynamically.

**Application**: when reading an external paper that proposes vacuum-energy extraction, the first structural check is whether the proposal assumes separable bath/device states. If yes, the proposal falls under bath-closure regardless of mechanism. If no — i.e., the proposal is genuinely about *spatial asymmetry* of an already-flowing process — apply Principle 2.

## Principle 2 — Sector-asymmetry quantitative obstruction

Dark energy in our framework is the 0.03% substrate→visible leakage at impedance mismatch `Γ_eff = 0.99970`. The leakage rate is governed by τ-evolution (Jensen deformation parameter). **τ is a scalar field on M⁴, so spatial gradients `∂τ/∂x^i` are mathematically admissible** — the substrate doesn't forbid local anisotropy of leakage.

R-monotonicity (S64 path-C closure) constrains *global* substrate degradation as monotone, not *local* leakage isotropy. So a directional asymmetry of leakage producing net thrust on a device is **structurally permitted in principle**.

**Quantitatively, it fails by ~9-15 OOM** with known boundary-modification mechanisms:
- Cosmological leakage rate at lab scale: `H₀ ≈ 70 km/s/Mpc ≈ 2 × 10⁻¹⁸ /s`
- For useful thrust (`a = 0.01 g ≈ 0.1 m/s²` on lab-scale device): need local leakage enhancement factor ~10¹⁵ above cosmological rate
- Casimir-scale boundary modification: enhances ZPF mode density by ~10⁶ at 100nm plate separation
- Gap: ~10⁹

This is the same OOM-gap the DIA paper concedes on p. 40 ("vacuum energy density difference between parallel plates and the region outside them in free space is simply not large enough in magnitude for large-scale engineering purposes").

**Open crack worth noting**: Volovik's superfluid-universe program has analog horizon enhancements (acoustic horizons in ³He-B amplify Hawking-like sector-crossing emission by many OOM over bulk). If the substrate admits an analogous "dark-energy horizon" — a boundary geometry that locally enhances substrate→visible leakage by orders of magnitude — the 9 OOM gap could in principle be closeable. **This is NOT characterized in the framework**. It's the kind of question that would emerge from doing the substrate-→-effective-field-theory reduction chain (DIA-investigation W-DIA-1) AND then asking what analog-horizon structures exist in the reduced description. Until that's worked out, the magnitude obstruction stands.

## Practical workflow for cross-framework adjudication

When evaluating an external vacuum-extraction proposal:

1. **Does the proposal assume separable bath/device states?** If yes → bath-closure (Principle 1) kills it categorically. Document and move on.
2. **Does the proposal exploit spatial asymmetry of an already-flowing process?** If yes → Principle 2 applies. Check quantitatively: what amplification factor over cosmological-scale leakage rate is needed for the claimed effect? Compare to known boundary-modification mechanisms (Casimir ≈ 10⁶, atomic ≈ 10⁹, accelerator-scale ≈ 10¹² for special cases). Gap > 6 OOM → "magnitude obstruction, structurally permitted."
3. **Does the proposal invoke analog-horizon or other non-standard amplification?** Flag as open question requiring framework characterization (typically routes to W-DIA-1 or successor workshop).
4. **Cross-link** to `phononic-framing.md §"IS Space, Not IN Space"` to verify the external proposal's substrate-IS framing is consistent. Most EM-drive proposals fail this check by treating the substrate as a container with internal vacuum modes rather than IS the modes.

## Calibration corpus

- **EM-drive (White et al. Eagleworks line, pre-2026)**: bath-closure violation; proposal frames vacuum as separable reservoir tappable by closed-cavity geometry. KILLED by Principle 1.
- **White et al. PRR 8, 013264 (2026)** "Emergent quantization from a dynamic vacuum": NOT a vacuum-extraction paper — Madelung-reverse interpretation of hydrogen quantization from dispersive vacuum. Compatible with our framework as effective-field-theory reduction (pending W-DIA-1 verdict). No bath-closure violation.
- **DIA-08-1004-007 (April 2010)**: theoretical survey, not a proposal. Identifies the bath-closure problem under QED axioms (pp. 25-26). Game-changer path (§VI pp. 37-41) is emergent-spacetime theories (Volovik) — i.e., the same lineage our framework belongs to.
- **Dark-matter / dark-energy thruster** (sci-fi-framed thought experiment, conversation 2026-05-17): NOT bath-closure (correctly targets spatial asymmetry of leakage); KILLED by Principle 2 magnitude gap (~9-15 OOM). Open via [[volovik-analog-horizon-enhancement]] if that gets characterized.

## Cross-link

- [[s61-s64-bundle]] — S64 R-monotonicity closure of path C
- [[s70-s75-bundle]] — Volovik partition + effacement mechanism details
- [[s82-kasparov-abelian-proof]] — substrate-IS predicate enforcement at the L2 layer
- `sessions/archive/session-91/DIA-investigation-schedule.md` — DIA-derived workshop schedule (W-DIA-1, W-DIA-2) where Principle-2 analog-horizon question routes for forward characterization
