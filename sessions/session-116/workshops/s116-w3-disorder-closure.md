# S116-W3-DISORDER-CLOSURE — Goldstone-mass disorder route: structural-closure vs surviving-channel

**Date**: 2026-06-27
**Gate**: `S116-W3-DISORDER-CLOSURE` (gate_type: workshop, Wave 3, Session 116)
**Format**: 2-agent adversarial adjudication, 3 rounds, sequential turns on this shared document
**Agents**: `landau-condensed-matter-theorist` (structural-closure pole — argues **CLOSED-BY-GRAPH-SCALE-WALL**) vs `phonon-first-cosmologist` (surviving-channel pole — argues **OPEN-VIA-SURVIVING-CHANNEL**)
**Closure**: artifact-existence (NO verdict line, per `wave-classification.md §M1`). Must end with R1/R2/R3 filled + a `## Structural Verdict` (CLOSED-BY-GRAPH-SCALE-WALL vs OPEN-VIA-<named-mechanism>, with the ceiling formula + the mechanism selector handed to `S116-W3-GOLDSTONE-M2`) + `## Wrap-Up`.

## Adjudication Question

> Given the inv5 Imry-Ma FAIL (`frac170 = 4.036e-05`; canonical Larkin construction A FAILS LEG1 no-enhancement; the disorder-family ceiling — construction E, whole C²-backbone-as-random-field at ξ=1 bond — reaches only `frac170 ≈ 0.0118 = J_C2/(170·Δ_BCS)`), and the collab §5 Cheeger bound `m_G ≥ h(L)/2` with `h ~ 2J_C2/Vol(cell)` (which gives `m_G ~ J_C2 ~ 0.93 M_KK ≈ 2Δ_BCS`, the SAME coupling-scale ceiling) — is the disorder→Goldstone-mass route to the 170× factor STRUCTURALLY CLOSED, or does a non-Imry-Ma disorder mechanism survive?
>
>   (a) **STRUCTURAL-CLOSURE READING (Landau pole)**: the route is permanently closed by the Josephson-graph coupling-scale ceiling. The phase Goldstone's mass — whether from Imry-Ma random-field domain pinning OR the Cheeger isoperimetric connectivity gap OR the NSR pseudogap — is a spectral moment of the SAME Josephson-coupling graph {J_C2, J_su2, J_u1}, and a graph cannot pin its own phase mode harder than its stiffest bond: `m_G ≤ J_C2 ≈ 0.93 M_KK ≈ 2Δ_BCS`. The 170× target (`170·Δ_BCS ≈ 78.9 M_KK`) is ~85× above this universal ceiling. `frac170 ≤ ~0.012` is a WALL, not a parameter shortfall. NO non-Imry-Ma disorder mechanism survives; the protection (below-edge, DM-survival) and the shortfall (170×) are the same graph-scale stability statement.
>   (b) **SURVIVING-CHANNEL READING (phonon-first pole)**: the closed corridors (Imry-Ma/NSR/CFL) do NOT exhaust the disorder-adjacent space. A different ξ_disorder scaling from the FULL Josephson-coupling distribution (not just the rms h_rf the inv5 gate used) — a rare-region / Griffiths heavy-tail, a collective/cooperative resonance, or a flat-band-quench analogue from a distinct condensed-matter system — could anchor a heavier mass; the route is OPEN pending that mechanism. Alternatively the 170× is simply not a disorder observable (it is the W2-2 two-scale pseudogap), making Q3's disorder framing the wrong question rather than a closed wall.
>   (c) **DISCRIMINATOR**: is there a substrate mechanism deriving m_G from the coupling graph that EXCEEDS the construction-E / Cheeger ceiling `frac170 ≈ 0.012` by enough to matter (toward 170×)? If the ceiling argument (a) is airtight (no graph-derived mechanism escapes `m_G ≤ J_C2`), the route is CLOSED-BY-GRAPH-SCALE-WALL and the DM mass is graph-unanchored (Reading B of WS-S112-4, structurally like M_KK). If (b) names a concrete escape, the route is OPEN-VIA-SURVIVING-CHANNEL and `S116-W3-GOLDSTONE-M2` tests it. The STRUCTURAL VERDICT MUST resolve which, and hand the compute either a named surviving mechanism (→ Branch A) or the ceiling-pin mandate (→ Branch B).

## Competing Positions (each first-principles-backed; the workshop derives which is correct)

- **landau-condensed-matter-theorist — CLOSED-BY-GRAPH-SCALE-WALL.** Every disorder/connectivity mechanism (Imry-Ma domains, Cheeger λ_1, NSR pseudogap) is a spectral moment of the same Josephson graph; `m_G ≤ J_C2 ≈ 2Δ_BCS`; `frac170 ≤ 0.012` is a universal wall ~85× short of the 170× target. The shortfall and the below-edge DM-protection are one graph-scale stability statement. The DM mass, if it exists, is graph-unanchored (Reading B, like M_KK).
- **phonon-first-cosmologist — OPEN-VIA-SURVIVING-CHANNEL.** The inv5 gate used only the rms `h_rf`, not the full coupling distribution; a rare-region/Griffiths heavy-tail or a cross-domain flat-band-quench / Josephson-array / analogue-gravity mechanism could anchor a heavier mass, OR the 170× is not a disorder observable at all. The closed corridors do not exhaust the space; the route is OPEN pending a concrete escape (or a reframe of the question).

**NUMERIC STAKES** (M_KK units; Δ_BCS=0.4642547 R-PROTECTED S70):
- inv5 Imry-Ma canonical (construction A): `m_G=0.003185`, `ξ_Larkin=17.115` bonds, `enh=0.0231` (<1 FAIL LEG1), `x_G<1` (below edge), `frac170=4.036e-05`.
- inv5 disorder-family ceiling (construction E, ξ=1, E=J_C2): `m_G=0.933`, `frac170≈0.0118`, `enh≈6.76` (>1), `x_G≈0.356` (still below edge) — passes both inv5 legs yet is 85× short.
- bare dipolar Goldstone (S49, collab §5): `m_G=0.070`, `frac170≈8.9e-4`.
- Cheeger bound (collab §5 eq 7): `m_G ≥ h(L)/2`, `h ~ 2J_C2/Vol(cell)` ⇒ `m_G ~ J_C2 ≈ 0.93` (cell Vol≈1); the lattice-Laplacian spectral gap `λ_1` IS `m_G²`. Same ~0.93 M_KK ≈ 2Δ_BCS ceiling.
- target: `frac170 = 1.0 ⇔ m_G = 170·Δ_BCS = 78.92 M_KK`. Ratio target/ceiling ≈ 85.
- the ladder {4e-5, 9e-4, 0.012, target=1.0}: every Josephson-graph-derived mechanism lands in [4e-5, 0.012]; the target is ~85× above the most optimistic in-family reading.

**SUBSTRATE FRAME** (`phononic-framing.md`): the U(1)₇ phase Goldstone IS the substrate's broken-phase boson (PROVED ungaugeable: `[iK_7,D_K]=0`, N4 BROKEN; SA-mass=0 EXACT S48 wall #7 — the spectral action CANNOT mass it). Its mass, if any, is a graph spectral moment. Flow: `D_K (0,0)-eigenvalues → Josephson couplings {J_C2,J_su2,J_u1} → {Imry-Ma pinning / Cheeger λ_1} → m_G → DM structure-formation mass`. The 170× "problem" is the container-thinking trap of expecting a graph to supply a mass ~85× its stiffest bond. **SOURCE-RECON caution**: the disorder length is the Larkin length `ξ_Larkin=17.115 bonds`, NOT the KZ quench length (`xi_KZ_FW=0.0187601`) — do NOT conflate.

**Sources** (read before writing):
1. `computations/investigation-5/inv5_gate_verdicts.txt` — INV5-W2-4 FAIL (frac170=4.036e-05, leg1=NEG, xi_L=17.115)
2. `computations/investigation-5/inv5_w2_4_goldstone_mass_disorder.npz` — the 5-construction disorder bracket (A_Larkin..E_max_bond); construction-E ceiling frac170≈0.0118
3. `computations/investigation-5/inv5_w2_4_goldstone_mass_disorder.py` — the Imry-Ma derivation (m_G²=E²/ξ²)
4. `computations/session-48/s48_goldstone_mass.py` — MASS-48: SA Goldstone-mass=0 wall (S48); rho_s_C2=7.962; BCS-floor m_G/M_KK=0.006838
5. `sessions/framework/Collabs/atlas-spectral-geometer-collab.md` — §5 Cheeger bound m_G≥h(L)/2, h~2J_C2/Vol; m_required/m_Leggett=170; m_G=0.070 dipolar anchor
6. `sessions/session-112/session-112-workshop-schedule.md` — WS-S112-4 Reading A (surviving) vs Reading B (irreducibly unanchored) — the adversarial precedent (landau×mack; THIS is the distinct-axis landau×phonon-first re-adjudication)

---

## R1 — Opening Positions (steelman your assigned side)

### R1 · landau-condensed-matter-theorist — STRUCTURAL-CLOSURE steelman

**Thesis.** The disorder→Goldstone-mass route to the 170× factor is permanently closed, and the closure is not a shortfall of effort but a theorem of the order-parameter arena. Every disorder, connectivity, or pseudogap mechanism that can pin the U(1)₇ phase mode is a spectral moment of one operator — the Josephson-coupling graph — and a graph cannot pin its own phase mode above the operator norm of that graph. That norm is `O(J_{C2}) ≈ O(2Δ_BCS) ≈ 0.93 M_KK`. The structure-formation target `170·Δ_BCS = 78.9 M_KK` sits 28–85× above it. The wall and the below-edge DM-protection are the same sentence written twice.

#### Definitions and the order-parameter arena (substrate-first)

The substrate IS the Josephson graph. The chain is, strictly,
`D_K (0,0)-eigenvalues → Josephson couplings {J_{C2}, J_{su2}, J_{u1}} → phase-mode Hamiltonian → m_G → DM structure-formation mass`. I do not reach for a container in which the graph sits; the graph is all there is, and the phase mode's mass is an intrinsic spectral functional of it.

The broken symmetry is U(1)₇ → 1 (the BCS condensate carries K₇ charge ±½, S35). The order parameter is the complex pair amplitude
$$\Delta = |\Delta|\,e^{i\phi}, \qquad \mathcal{M} = S^1 \quad (\text{order-parameter manifold}). \tag{1}$$
The would-be-massless excitation is the phase mode `φ` — the Goldstone of the broken U(1)₇. Two PROVEN facts bound its bare mass before any disorder is added:

- **Wall #7 (S48, my own GOLDSTONE-MASS-48).** The spectral action cannot mass it: `Tr[f(D(φ)²)] = Tr[f(D²)]` for the unitary conjugation `D(φ) = e^{φK₇} D e^{-φK₇}`, so `d²S/dφ² = 0` IDENTICALLY (`s48_goldstone_mass.py` Part B; verified to machine ε for D_K, D_phys, and random Hermitian D). The mass is therefore NOT a spectral-action potential; it can only be a **graph** (Josephson) effect — exactly the route this workshop adjudicates.
- **BCS fibre floor (S48).** `m_G/M_KK = 0.006838`, the small-fibre mass floor; `ρ_s = ρ_{s,C2} = 7.962` is the phase stiffness.

The Ginzburg–Landau free energy of the phase sector is the XY/Josephson functional
$$F[\phi] = \tfrac12 \rho_s \!\sum_{\langle ij\rangle}\! J_{ij}\,(\phi_i-\phi_j)^2 \;-\; \sum_i h_i\cos\phi_i, \tag{2}$$
with NO local potential in the clean limit (Goldstone's theorem). A mass requires the second term — a pinning field `h_i`. The entire adjudication reduces to one question: **how large can `h` be, and over what domain, when `h` itself is built only from `{J_{C2}, J_{su2}, J_{u1}}`?**

#### Sub-(a): the graph-scale ceiling is airtight (mechanism-independent)

I give the ceiling at two levels of strength.

**Level 1 — Imry-Ma stiffest-bond reading (the pre-registered ceiling).** Imry-Ma (1975): a continuous-symmetry order parameter in a random field breaks into Larkin domains of size `ξ` set by elastic-vs-random-field balance, and the would-be Goldstone gains
$$m_G^2 = E_{\rm dis}^2 / \xi^2 \tag{3}$$
(the pinning-energy curvature; `inv5_w2_4` `imry_ma_mass`). The random field here is the substrate's OWN non-C² coupling spread; the C² coset (`J_{C2}=0.933`, 4 bonds) is the ordered backbone. The two extremal inputs are bounded by the graph itself:
$$E_{\rm dis} \le \max\{J_{C2}, J_{su2}, J_{u1}\} = J_{C2}, \qquad \xi \ge 1\ \text{bond}. \tag{4}$$
Substituting the hardest admissible reading (the entire backbone treated as random field at one-bond correlation — `inv5_w2_4` construction E, `E_max_bond_J_C2`, flagged in-script as the *"unphysical upper"*):
$$m_G^{\max} = J_{C2}/1 = 0.933\ \text{M\_KK}, \qquad \mathrm{frac170}_{\max} = \frac{J_{C2}}{170\,\Delta_{\rm BCS}} = 0.0118. \tag{5}$$
This is the npz-confirmed ceiling: construction E returns `m_G = 0.933`, `enh = 6.76 (>1)`, `x_G = 0.356 (<1)` — it passes BOTH inv5 legs and is still 85× short (`84.6 = 78.9/0.933`).

**Level 2 — operator-norm reading (airtight, no mechanism assumed).** Equation (5) used the Imry-Ma form. To shut the "but a *different* disorder construction" escape, drop Imry-Ma entirely. ANY pinning mechanism adds a term to the phase Hamiltonian; the resulting gap `m_G²` is an eigenvalue of the weighted graph Laplacian-plus-pinning `H_φ`, and the pinning operator is itself assembled from the bonds (disorder IS bond-strength fluctuation). By Gershgorin on the weighted Josephson Laplacian,
$$\| H_\phi \| \;\le\; 2\,\max_v \sum_{u} J_{vu} \;=\; 2\,d^{\,w}_{\max}, \qquad d^{\,w}_{\max} = 4J_{C2} + 3J_{su2} + J_{u1} = 3.95. \tag{6}$$
Hence the ABSOLUTE band-top gap, with no assumption about the mechanism,
$$\omega^2_{\max} \le 2 d^{\,w}_{\max} = 7.89 \;\Rightarrow\; m_G \le 2.81\ \text{M\_KK}, \qquad \mathrm{frac170}_{\rm abs} \le 0.0356. \tag{7}$$
**Interpretation.** A Griffiths heavy tail, a rare-region resonance, a collective/cooperative mode — each merely REDISTRIBUTES spectral weight inside `[0, \|H_φ\|]`. None can create an eigenvalue above the operator norm of an operator built from `{J_{C2}, J_{su2}, J_{u1}}`. The ceiling is a property of the bond set, not of the construction. The target `frac170 = 1.0` is 28× above even the absolute band-top (7), and 85× above the physical Imry-Ma reading (5). A factor-of-3 quarrel over which ceiling is "right" leaves the wall standing.

**Cross-axis confirmation (independent method).** The spectral-geometer collab reaches the SAME ceiling by a DIFFERENT route — lattice bandwidth, not Imry-Ma. Collab §5: the Cheeger floor `m_G ≥ h/2` "goes the wrong way" (a floor, not a ceiling — line 137), but the operative statement is line 125: *"such a bound exists: `m_G ≤ 2√J_min` from the lattice bandwidth … `≤ 0.39 M_KK`, still 30× below the target."* Two independent constructions (BCS Imry-Ma and spectral-geometry bandwidth) converge on a Josephson-scale ceiling 30–85× short. That convergence is what distinguishes a wall from an unlucky construction.

**Why the ceiling is locked to the gap (Ambegaokar–Baratoff).** `J_{C2} = 0.933 ≈ 2Δ_BCS = 0.9285` is not coincidence. The inter-cell Josephson coupling IS the pair-tunneling amplitude; for BCS cells `E_J ∼ Δ` (Ambegaokar–Baratoff, `I_c R_N = πΔ/2e` at T=0, O(1) inter-cell conductance). So the stiffest bond of the graph is pinned, by BCS physics, to the pair-breaking edge. The graph literally cannot carry an energy scale above its own gap-set bond — which is the microscopic reason a graph cannot pin its phase mode above `2Δ_BCS`.

#### Sub-(b): no surviving channel escapes — the disjunction is exhaustive

Partition every candidate mechanism by one binary: **is its energy scale a functional of `{J_{C2}, J_{su2}, J_{u1}}`?**

- **In-graph (disorder/connectivity/pseudogap).** Imry-Ma domain pinning, Cheeger isoperimetric gap `λ_1`, Fiedler algebraic connectivity, NSR pseudogap, Griffiths rare regions — ALL are spectral moments of the bond set, hence ALL obey (6)-(7). The second non-Imry-Ma corridor, NSR (`INV5-W2-2`), did not merely fall short — it **inverted sign**: `r_2scale = 5.43` vs target `14.20`, because the substrate phase-stiffness DOMINATES the gap via the Josephson f-sum-rule (`E_J = 3.397`). That sign inversion is the SAME wall in a second gate: the graph's stiffness is so large relative to the would-be pseudogap that the two-scale ratio opens the wrong way. Two corridors, one ceiling.
- **Out-of-graph.** A mechanism whose scale is NOT in the bond set would escape (6)-(7) — but then it is not a disorder or connectivity mechanism at all (those are BY DEFINITION functionals of the graph). It would be an external magnitude-anchor, structurally like M_KK: a dimensionful import the substrate does not derive. This is exactly **Reading B of WS-S112-4** (`session-112` lines 59, 63: *"the Leggett-channel mass is an inter-band coherence scale with no substrate magnitude-anchor — abundance is predicted, mass is not (a structural feature, like M_KK)"*).

There is no third option. The disorder route specifically — the object of THIS workshop — falls entirely in the in-graph branch and is walled by (5)-(7). Any "surviving" mass-anchor is, by construction, out-of-graph, i.e. NOT a disorder mechanism and NOT a derivation but an import.

#### Sub-(c): the discriminator — nothing reaches even one-tenth of the target

The pre-registered discriminator asks whether any graph-derived mechanism exceeds `frac170 ≈ 0.012` meaningfully toward `1.0`. The full inv5 ladder (npz-verified) plus the bare dipolar anchor and the absolute bound:
$$\underbrace{4.04\!\times\!10^{-5}}_{\text{A Larkin}} < \underbrace{1.15\!\times\!10^{-4}}_{\text{D std}} < \underbrace{4.81\!\times\!10^{-4}}_{\text{C }J_{u1}} < \underbrace{6.91\!\times\!10^{-4}}_{\text{B }h_{\rm rf}} < \underbrace{8.9\!\times\!10^{-4}}_{\text{dipolar }m_G=0.070} < \underbrace{1.18\!\times\!10^{-2}}_{\text{E ceiling}} \le \underbrace{3.56\!\times\!10^{-2}}_{\text{abs op-norm}} \;\lll\; \underbrace{1.0}_{\text{target}}. \tag{8}$$
Every Josephson-graph-derived mechanism lands in `[4×10⁻⁵, 3.6×10⁻²]`. The most generous in-family reading is ~28× short of `1.0` and ~80× short of being within an order of magnitude with margin. The discriminator resolves: **CLOSED-BY-GRAPH-SCALE-WALL.** The handoff to `S116-W3-GOLDSTONE-M2` is the ceiling-pin mandate (Branch B): pin `frac170 ≤ J_{C2}/(170Δ_BCS) = 0.0118` as the graph ceiling and certify the operator-norm robustness band `[0.0118, 0.0356]`.

#### The deep unity: protection and shortfall are one statement

This is the structural payload, not a numerical coincidence. The below-edge DM-protection requires the phase mode to sit below the pair-breaking continuum, `ω_G < 2Δ_BCS` (so the DM phonon cannot decay into a quasiparticle pair — the non-annihilating, CPT-neutral Leggett-channel survival argument). With `ω_G = m_G/√ρ_s`:
$$\omega_G < 2\Delta_{\rm BCS} \;\Longleftrightarrow\; m_G < 2\Delta_{\rm BCS}\sqrt{\rho_s} = 0.9285 \times 2.822 = 2.62\ \text{M\_KK}. \tag{9}$$
Compare with the graph ceiling (7): `m_G ≤ 2.81 M_KK`. **These two caps are the same scale.** They coincide because `J_{C2} ≈ 2Δ_BCS` (Ambegaokar–Baratoff) and `ρ_s = O(\text{few})`. A mode heavy enough for the 170× target would need `m_G = 78.9 M_KK`, i.e. `x_G = ω_G/2Δ_BCS ≈ 30` — thirty times ABOVE the pair-breaking edge. Such a mode would instantly decay into quasiparticle pairs; it could not be the long-lived DM. Therefore:

> The very graph scale that PROTECTS the DM (caps `m_G` below the pair-breaking edge → non-annihilating) is the scale that STARVES it of structure-formation mass (caps `m_G` 28–85× below `170Δ_BCS`). You cannot lift the second cap without breaking the first. Protection and shortfall are the single proposition `m_G = O(J_{C2}) = O(2Δ_BCS)`.

This is why the route is closed *structurally*: the 170× "problem" is the container-thinking trap of demanding that a graph supply a phase-mode mass 85× its own stiffest bond — the same error as asking the fabric to expand into a pre-existing space. The graph does not fail to reach 170×; it is the wrong object to ask.

#### Questions for phonon-first-cosmologist

1. **Name a concrete graph-escaping mechanism with an explicit energy scale.** Eq. (6)-(7) bound EVERY operator built from `{J_{C2}, J_{su2}, J_{u1}}`. You invoke "the full coupling distribution, not just `h_rf`." Granted the distribution has a tail — but its support is `[0, J_{C2}]`, so its maximum is still a bond bounded by `J_{C2}`. Show me a coupling-distribution moment, rare-region observable, or collective resonance whose phase-mode mass is NOT an eigenvalue of an operator assembled from these three bonds. Where does an energy ABOVE the stiffest bond come from?

2. **The Griffiths/heavy-tail challenge, made precise.** A heavy-tailed disorder on `[0, J_{C2}]` produces rare strongly-pinned regions, but each pins at energy `≤ J_{C2}` over a domain `ξ ≥ 1`, so its Imry-Ma mass is `≤ J_{C2}` by (3)-(4) — and its *contribution* to the global gap is an eigenvalue inside `[0, \|H_φ\|]` by (6). Heavy tails change the DENSITY of states near the band edge; they do not move the band edge. What in your mechanism moves the band edge of the Josephson Laplacian itself?

3. **The "wrong question" fork is a concession, not an escape.** If you take the alternative that 170× is the W2-2 two-scale pseudogap rather than a disorder observable, you have MOVED the 170× off the disorder axis — which IS conceding that the disorder route is CLOSED-BY-GRAPH-SCALE-WALL, with the 170× living elsewhere (an out-of-graph anchor, Reading B). So choose explicitly: either (i) a disorder mechanism reaches `frac170 → 1.0` despite (6)-(7) — name it; or (ii) the 170× is not a disorder mass — in which case we agree the disorder route is walled and the verdict is CLOSED. You cannot hold both.

### R1 · phonon-first-cosmologist — SURVIVING-CHANNEL steelman

**Thesis.** I will not contest the ceiling on its own ground — and that surgical concession *is* the whole of my disagreement with how Landau frames it. Eq. (6)-(7) is exact for `H_φ`, the (0,0)-restricted U(1)₇ phase Laplacian-plus-pinning: every eigenvalue of an operator assembled from `{J_{C2}, J_{su2}, J_{u1}}` at those bond values lies in `[0, ‖H_φ‖]`, `‖H_φ‖ ≤ 2 d^w_{max} = 7.894`, so `m_G ≤ 2.81 M_KK`, `frac170 ≤ 0.0356`. Airtight. But Landau's three closed corridors — Imry-Ma, NSR, CFL — are three readings of the **same operator** `H_φ`, and the inv5 gate that produced them built its random field as a **(0,0)-diagonal** object: `h_rf = rms{J_{su2}, J_{su2}, J_{su2}, J_{u1}} = 0.0545`, four bonds, all intra-phase-sector (script lines 252-253). The disorder-adjacent space is not exhausted, because the disorder operator the gate wrote down has **no inter-band matrix elements** — no off-diagonal coupling from the (0,0) phase sector into the Casimir-graded Peter-Weyl ladder of `D_K`. The substrate IS the graph; but "the graph" is `D_K`'s full Peter-Weyl content, and `H_φ` is its (0,0) shadow. **Landau bounded the shadow, exactly, and then read the bound as a bound on the object.** The flow is `D_K (full spectrum) → { intra-(0,0) phase bonds H_φ  ⊕  inter-band ladder } → m_DM`, and the second summand carries the fiber spectral radius `0.633√C_2 + 0.555` (collab §3 eq 1), which is **not** `max{J_{C2}, J_{su2}, J_{u1}}`.

My pattern-detector vantage: I read the inv5 ladder `{4e-5, 9e-4, 0.012}` not as "the graph's reach" but as "the reach of the **one block** the gate diagonalized." When the same eigenvalue spectrum appears confined to one Peter-Weyl sector in three different corridors, that is not the graph speaking — it is the *projector* speaking.

#### The cross-domain skeleton — where the phase-mode mass is NOT a single-bond eigenvalue

Landau asked (Q1) for "a system where the phase mode's mass is not bounded by a single bond." The condensed-matter literature has the canonical answer, and it is structurally the framework's own:

- **Multiband Leggett mode (Pillar IV/V; Leggett 1966; MgB₂, Fe-pnictides).** In a two-band superconductor the relative-interband-phase mode (the Leggett mode) has `m_Leggett² ∝ J_⊥`, where `J_⊥` is the **inter-band** pair-transfer, a coupling categorically distinct from the intra-band stiffness. Its energy is *not* set by the intra-band Josephson bond and is *not* bounded by the single-band phase-Laplacian norm. This is exactly the framework's DM mode — "DM = Leggett-channel GGE quasiparticle" — and the substrate's inter-band coupling is the off-(0,0)-block of `D_K`, whose scale is the Casimir-graded radius, not `J_{C2}`. Landau's `d^w_{max} = 4J_{C2}+3J_{su2}+J_{u1}` counts the **intra-cell coordination**; it never sees `J_⊥`.
- **Flat-band quantum-metric superfluidity (Pillar IV; Peotta-Törmä).** In a flat band the superfluid weight is set NOT by the (zero) bandwidth but by the integrated quantum metric `D_s = (2Δ/V)∫Tr g`. The relevant scale is geometric, decoupled from the hopping. *Honest regime check against my own ledger:* INV8-W3-2 found `Tr g = 0` for the lowest (0,0) doublet under the volume-preserving TT deformation — U(2)-invariance protection. So the quantum-metric escape **at the (0,0) block is CLOSED** (I cite this against myself). The surviving version is the **off-(0,0)** metric, where U(2)-invariance does not protect — precisely the inter-band sector again.
- **Josephson-array Mott charging gap (Pillar V).** A JJ array opens a heavy phase gap `~E_C` in the **Mott** regime (`E_C ≫ E_J`). *Honest regime check:* the substrate sits at `E_J/E_C = 194` — deep superfluid. The Mott heavy-phase mechanism is therefore **regime-excluded** here. I name it to map the boundary, not to claim it.

The pattern across all four: a *single-bond* (intra-band) operator never carries the heavy scale; a *cooperative/inter-band* operator does. Three of the four are closed or excluded on the substrate; the one that survives — inter-band coupling — is exactly the summand the inv5 disorder operator omitted.

#### Engaging Landau's R1 by label

- **The order-parameter arena (eq. 1-2).** Agreed, fully. `M = S¹`, the Goldstone is the phase `φ`, and a mass requires a pinning term. I add only: the inv5 pinning term `h_i cos φ_i` is **diagonal in the (0,0) basis**. A pinning term with inter-band matrix elements `h_{i,(p,q)} φ_i φ_{(p,q)}` lives outside `F[φ]` as written.
- **The graph-norm ceiling (eq. 6-7), sub-(a) airtightness.** Agreed *for `H_φ`*. Gershgorin is exact; nothing assembled from those three bonds escapes `[0, ‖H_φ‖]`. My dissent is not that the bound leaks — it is that `H_φ` is not the DM mode's operator. **The decisive, registered fact:** the framework's own Leggett-DM anchor is `m_Leggett = 11.97·Δ_BCS = 5.557 M_KK` (inv5 C11 anchor, `MASS_LEGGETT_OVER_DELTA`, script line 135). That is `1.98×` Landau's operator-norm cap `m_G ≤ 2.81` and `~6×` above the pair-breaking edge. **A mode the framework already carries at 5.56 M_KK cannot be an eigenvalue of `H_φ`** — `‖H_φ‖^{1/2} = 2.81 < 5.56`. The DM mass is already, on the books, an inter-band object. Landau's wall caps the (0,0) phase Goldstone (0.070, 0.138) cleanly; it does not contain the registered DM anchor that sits a factor of 2 above it.
- **The Ambegaokar-Baratoff lock `J_{C2} ≈ 2Δ_BCS` (eq. on line 84).** Agreed and important — but it locks the **inter-cell phase bond** to the gap. It says nothing about the **inter-band (inter-sector) pair-transfer**, which is locked instead to the fiber Dirac spectrum (Lichnerowicz `|λ| ≥ √3 = 1.73 > 2Δ_BCS = 0.928`, collab §5 eq 8). Every nonzero fiber mode already sits above the edge; the inter-band ladder is intrinsically a *higher-scale* object than the intra-cell bond.

**Answering Q1 (name a concrete graph-escaping mechanism with an explicit scale).** Inter-band disorder mixing. The physical non-C² random field, if it carries off-(0,0)-diagonal matrix elements, couples the phase mode to the Peter-Weyl ladder; the induced effective mass is set by level-repulsion with the fiber spectrum, scale `0.633√C_2 + 0.555`. Substitution chain: at the first excited sector `C_2(1,1)=3`, `max|λ| = 0.633·1.732 + 0.555 = 1.651 M_KK > J_{C2} = 0.933` ⇒ the scale exceeds the stiffest bond at the *first* inter-band step; at `C_2 ≳ 15`, `max|λ| = 3.01 > 2.81` ⇒ it exceeds Landau's own operator-norm cap. The energy "above the stiffest bond" comes because the inter-band block of `D_K` is **not** in the bond set `{J_{C2}, J_{su2}, J_{u1}}` — it is the Casimir-graded pair-transfer, a different operator with a higher norm.

**Answering Q2 (Griffiths/heavy-tail, made precise).** I **concede** this entirely, on its own terms. A heavy tail on the support `[0, J_{C2}]` moves the density of states, not the band edge of `H_φ`; the rare-region Imry-Ma mass is `≤ J_{C2}`. The Griffiths-of-the-same-distribution corridor is **closed**. But your Q2 quietly fixes the support to `[0, J_{C2}]` — which is true only for an *intra-(0,0)* random field. What "moves the band edge" is not a heavier tail; it is an **off-diagonal** (inter-band) disorder matrix element, whose available range is the fiber spectral radius, not `[0, J_{C2}]`. I do not move `H_φ`'s edge. I add a block `H_φ` did not have.

**Answering Q3 (the fork: name a disorder mass reaching frac170→1, OR concede 170× lives off-graph, Reading B).** I take the second horn — and deny that it lands on Reading B. Your binary is **{in-graph-phase-disorder (walled)} XOR {out-of-graph import (Reading B, like M_KK)}**. It omits a third cell: **{in-graph, different operator}**. The DM mass is a `D_K` spectral functional (the inter-band Leggett/Casimir scale, registered at 5.56 M_KK) — it is *in*-graph, hence NOT an external magnitude-import, hence NOT Reading B. What is closed is the **170× enhancement of the (0,0) phase Goldstone**; what is *not* closed, and not unanchored, is the DM mass itself. Reading B says "abundance predicted, mass free." I say "abundance predicted, **mass anchored at the (0,0) Leggett scale**, 170× enhancement is the mis-typed part." That is a different verdict from yours.

#### Sub-(a)/(b)/(c) from the surviving side

- **Sub-(a) — is the graph-scale ceiling airtight?** YES for `H_φ` (I concede Gershgorin). NO as a statement about the DM mass: `H_φ` is the (0,0) shadow, and the registered DM anchor (5.56 M_KK) already exceeds `‖H_φ‖^{1/2}`. The ceiling is **operator-specific, not graph-universal**.
- **Sub-(b) — is a surviving channel named?** YES, concretely: **inter-band disorder mixing onto the Casimir-graded Peter-Weyl ladder** of `D_K` (off-(0,0) pair-transfer), the substrate realization of the multiband Leggett mode. Its scale is `0.633√C_2 + 0.555`, not `max{J_{C2},J_{su2},J_{u1}}`. Hand `S116-W3-GOLDSTONE-M2` **Branch A**: build the disorder operator WITH off-(0,0) matrix elements and read the lowest induced inter-band gap.
- **Sub-(c) — does anything exceed `frac170 ≈ 0.012` toward 170×?** YES. The inter-band ladder reaches `frac170 = 0.021` already at `(1,1)`, `0.038` (= the op-norm cap) by `C_2 ≈ 15`, and `0.153` at `(30,0)`. So Landau's eq-(8) claim that "every Josephson-graph-derived mechanism lands in `[4e-5, 0.036]`" is **falsified as stated** — it is true only for the (0,0)-projected operator. The honest bound: the inter-band ladder does NOT reach a *protected* 78.9 M_KK (see below), but it decisively breaks the `0.012`–`0.036` "universal" ceiling.

#### The honest wall I grant — and why it is a DIFFERENT, stronger wall that REOPENS the question

Here is where I cede ground, and where the exchange produces something neither opening had. Every nonzero fiber mode is above the pair-breaking edge (`|λ| ≥ √3 = 1.73 > 2Δ_BCS = 0.928`), so the inter-band ladder modes are **not below-edge-protected**; and a mode at the structure-formation target `m = 78.9 M_KK` has `x = ω/2Δ_BCS ≈ 30 ≫ 1` on any stiffness convention — wildly unprotected. So a *below-edge-protected* mode cannot reach 170× on **any** operator, intra- or inter-band. The real wall is not `‖H_φ‖`; it is **protection-vs-magnitude exclusion**, and it binds the whole spectrum, not just the shadow.

But that stronger wall **changes the verdict's meaning**. It says: the structure-formation requirement, *if* it is a heavy protected gap, is impossible — which is evidence that **it is not a heavy protected gap**. The "170×" entered this ledger from the n_s SA-Goldstone correlator-crossover context (collab §5: `m_G=0.070` vs the `K*=0.087` crossover for `n_s=0.965`), and was *re-typed* as a DM structure-formation mass in HK-170X-DM (S112). The inv5 gate inherited the re-typing and built a gate with two **mutually exclusive** legs: LEG-2 demands below-edge (`x<1`), while the 170× target is intrinsically above-edge (`x≈30`). The FAIL is, in part, a **category mismatch baked into the pre-registration** — a below-edge mode asked to reach an above-edge target. That is the surviving "wrong question," made concrete: structure formation from a cold, **transit-frozen** velocity dispersion (the Ordered Veil: `S_ent = 0`, `R_therm = 5252`, diabatic GGE) does not require a heavy protected gap at all. The DM mass stays anchored at the (0,0) Leggett scale; the cold kinematics, not a 170× mass, does the structure-formation work.

So my surviving-channel position is twofold and in-graph throughout: **(B1)** the disorder space is not exhausted — inter-band disorder mixing is a real, omitted operator that breaks the `0.012` ceiling (Branch A); **(B3)** the DM mass is graph-anchored at the (0,0)/inter-band Leggett scale, NOT Reading-B-unanchored — the 170× is a mis-imported requirement, dissolved by transit-frozen kinematics, not a wall on the mass. Neither lands on "CLOSED-BY-GRAPH-SCALE-WALL + unanchored."

#### Questions for landau-condensed-matter-theorist (Round 2)

1. **The registered anchor.** The framework carries `m_Leggett = 11.97·Δ_BCS = 5.56 M_KK` as its DM-mass anchor — `1.98×` your operator-norm cap and above the edge. Either (i) that anchor is an `H_φ` eigenvalue (then explain how it exceeds `‖H_φ‖^{1/2} = 2.81`), or (ii) it is NOT — in which case the DM mode is already an inter-band object your bound does not contain, and "graph-unanchored / Reading B" is false because the mass is registered, in-graph, at 5.56. Which?
2. **The omitted block.** Do you accept that the inv5 random field (`h_rf`, four (0,0)-diagonal bonds) carries **no off-(0,0) matrix elements**, so your eq-(6) Gershgorin bound is exact precisely *because* the disorder operator was projected to the (0,0) block before it was bounded? If a physical non-C² disorder has inter-band matrix elements, on what grounds is the (0,0)-projected operator the correct one?
3. **Which wall is the real one.** Will you re-state the closure as **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION** (binds the whole spectrum) rather than **CLOSED-BY-GRAPH-SCALE-WALL** (binds only `H_φ`)? If yes, then the closed object is "a *below-edge-protected* 170× mass," and the open question becomes whether structure formation needs that object at all — i.e., whether the cold transit-frozen GGE dispersion meets the free-streaming requirement at the anchored Leggett mass, with no 170× enhancement.

---

## R2 — Rebuttal (engage the opponent's strongest case)

### R2 · landau-condensed-matter-theorist

#### CONVERGENCE — where you now grant the phonon-first side

I concede the central distinction, and I concede it cleanly because it is correct. My eq. (6)-(7) is exact — but it is exact for the WRONG operator. The inv5 random field was assembled as `h_rf = rms{J_su2, J_su2, J_su2, J_u1} = 0.05451` (`inv5_w2_4` lines 252-253): four bonds, every one of them INTRA-(0,0), diagonal in the phase-sector basis. My Gershgorin ceiling therefore bounded `H_φ`, the (0,0)-restricted phase Laplacian-plus-pinning — the SHADOW of `D_K` on one Peter-Weyl block — and I then read a bound on the shadow as a bound on the object. That is precisely your charge, and it stands. The substrate IS the full Peter-Weyl content of `D_K`; `H_φ` is its (0,0) projection; I bounded the projection and over-claimed the whole.

The decisive fact is registered, and I verified it (Sage-exact): the framework's own DM-mass anchor is
$$m_{\rm Leggett} = 11.97\,\Delta_{\rm BCS} = 5.5571\ \text{M\_KK}, \tag{10}$$
which is `1.978×` my operator-norm cap `‖H_φ‖^{1/2} = √(2 d^w_max) = 2.8096 M_KK` and `5.985×` above the pair-breaking edge `2Δ_BCS = 0.9285`. So I answer your Q1 with horn (ii) without reservation: `m_Leggett` is NOT an `H_φ` eigenvalue — `‖H_φ‖^{1/2} = 2.81 < 5.56` makes that arithmetically impossible — and therefore the DM mode is ALREADY, on the books, an inter-band object my (0,0) bound does not contain. The `{in-graph-phase-disorder} XOR {out-of-graph-import}` dichotomy I forced in my R1 Q3 omitted your third cell, `{in-graph, different operator}`: the off-(0,0) block of `D_K` is in-graph (a spectral functional of the substrate Dirac operator), so the Leggett mass is NOT an external magnitude-import and is NOT Reading-B-unanchored. **I withdraw the claim that the DM mass is "graph-unanchored, like M_KK."** It is graph-anchored — on a block I had projected away before I bounded.

And I answer your Q3 affirmatively: I re-state the closure as **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION**, not CLOSED-BY-GRAPH-SCALE-WALL. Your "honest wall" — the protection-vs-magnitude bound that binds the WHOLE spectrum — is the correct statement; my graph-scale ceiling was its intra-band specialization. The Lichnerowicz floor `|λ| ≥ √3 = 1.73 > 2Δ_BCS` (collab §5 eq 8) you cited is exactly right: every nonzero fiber mode is intrinsically above the edge, so "graph-scale" was never the operative cap. That is a genuine improvement the exchange produced, and it is yours.

#### DISSENT — where you hold, with NEW argument (don't restate R1)

I grant the operator; I dispute the MECHANISM. Two new grounds, neither a restatement of my R1 graph-norm argument.

**(1) The channel that reaches 5.56 is the CLEAN Leggett coupling, not a disorder mechanism — and the genuine disorder channel onto the inter-band block is WEAKER than the (0,0) ceiling, not stronger.**

This is the load-bearing correction. You named "inter-band disorder mixing onto the Casimir-graded Peter-Weyl ladder" and assigned it the scale `0.633√C_2 + 0.555` (R1 lines 141, 150-151). But that scale is the fiber Dirac SECTOR ENERGY `E_n` (collab §3 eq 1) — the energy of the inter-band STATE — not the disorder-induced mass of the phase MODE. The phase mode's induced mass from coupling to a heavy sector is a level-repulsion (Schrieffer-Wolff) quantity, and its direction is the OPPOSITE of what your reading assumes. Substitution chain, every symbol explicit:

- Step 1: phase mode `|φ⟩` at (0,0), energy `E_φ ≈ 0` (Goldstone theorem).  [eq 1-2, R1]
- Step 2: inter-band sector `|n⟩` at energy `E_n = 0.633√C_2(n) + 0.555`.  [collab §3 eq 1]
- Step 3: a RANDOM off-(0,0) disorder field couples them, `⟨φ|V_dis|n⟩ = v`, with rms `v ~ h_rf` — the SAME non-C² disorder strength, now placed off-diagonal (the strongest physical reading in your favour: statistically isotropic disorder).  [disorder ansatz]
- Step 4: integrating out the heavy sector (2nd-order PT / Schrieffer-Wolff) gives the induced phase-mode mass-squared
$$\delta m_\phi^2 \;=\; \frac{|v|^2}{E_n - E_\phi} \;\approx\; \frac{h_{\rm rf}^2}{E_n}. \tag{11}$$
- Step 5: `∂(δm²_φ)/∂E_n = −h_rf²/E_n² < 0` ⇒ `δm²_φ` DECREASES as `E_n` increases.  [direction from canonical form]

A HEAVIER inter-band sector SUPPRESSES the disorder-induced phase mass. Numerically (Sage-verified):
$$\delta m_\phi(C_2{=}3) = \sqrt{h_{\rm rf}^2/E_n} = \sqrt{0.05451^2/1.651} = 0.0424\ \text{M\_KK},\quad \delta m_\phi(C_2{=}15) = 0.0314\ \text{M\_KK}. \tag{12}$$
The inter-band DISORDER channel tops out at `~0.042 M_KK` at the FIRST step and falls thereafter — SMALLER than the bare dipolar `m_G = 0.070` (ratio 0.61) and `22×` below my own (0,0) construction-E ceiling `J_C2 = 0.933`. The disorder route onto the inter-band ladder is not a heavier mass; it is a LIGHTER one.

The 5.56 M_KK anchor is therefore NOT a disorder-induced mass. It is the CLEAN multiband Leggett mode: `m_Leggett² ∝ J_⊥`, the DETERMINISTIC inter-band pair-transfer (Leggett 1966; the off-(0,0) block of `D_K`, no randomness, no Larkin domains, no Imry-Ma `E²/ξ²`). You correctly identified the OPERATOR (off-(0,0), inter-band); you mis-identified the MECHANISM (clean coupling `J_⊥`, not random-field disorder). The two are different objects: `J_⊥` enters `m_Leggett²` at FIRST order (it IS the restoring force of the relative-phase oscillation), while the disorder enters at SECOND order, suppressed by `E_n`. This answers your Q2: I accept the inv5 field is (0,0)-diagonal and that my Gershgorin bound was exact on the projected operator — but the correct operator for the genuine inter-band DISORDER channel gives eq. (11), which lands BELOW the (0,0) ceiling; the only object that reaches 5.56 is the clean Leggett `J_⊥`, which is not on the disorder axis at all. The disorder→Goldstone-mass route — THIS wave's literal question — stays closed on every reading.

**(2) Even granting the clean inter-band scale, it does not reach the target — the wall moved, it did not fall.**

Grant me nothing of (1); hand the route the full clean Leggett anchor (10). Then
$$\mathrm{frac170}(\text{Leggett}) = \frac{m_{\rm Leggett}}{170\,\Delta_{\rm BCS}} = \frac{5.5571}{78.923} = 0.07041, \tag{13}$$
still `14.20×` short of `frac170 = 1.0`. The inter-band block RAISES the ceiling from the construction-E value `0.01182` to `0.07041` — a `5.96×` lift, which IS your point that my eq-(8) "universal `[4e-5, 0.036]`" band is falsified as a whole-spectrum statement (granted). But the lifted ceiling is still `14×` below target, and the deeper wall you yourself raised binds here: a mode at the target `m = 78.92 M_KK` has
$$x_{\rm target} = \frac{m/\sqrt{\rho_s}}{2\Delta_{\rm BCS}} = 30.12, \tag{14}$$
thirty times above the pair-breaking edge — unprotectable on ANY operator, intra- OR inter-band, by your own protection-magnitude exclusion. The parallel compute `S116-W3-GOLDSTONE-M2` returned FAIL (`frac170 = 0.0118` Cheeger / `0.0245` Fiedler λ_1), confirming the (0,0)/intra-band ceiling. It did not test the inter-band block — but eq. (13) shows it would not need to: the inter-band block's own CLEAN anchor is already `14×` short. No compute on any single block closes the target.

#### EMERGENCE — new structure from the exchange

The exchange dissolves the binary `{closed-graph-wall vs surviving-channel}` into a THREE-TIER ladder, on which both opening positions are partly right and the verdict is determinate at each tier:

| Tier | Object | frac170 | Status |
|:--|:--|:--|:--|
| 1 | (0,0) intra-band disorder route | ≤ 0.024 (Cheeger 0.0118 / Fiedler λ_1 0.0245) | CLOSED; compute-confirmed (S116-W3-GOLDSTONE-M2 FAIL) |
| 2 | inter-band Leggett channel (clean `J_⊥`) | 0.0704 (= `m_Leggett/170Δ_BCS`) | surviving channel, but CLEAN coupling (already-registered DM anchor), NOT a disorder mechanism; 14.2× short |
| 3 | 170× structure-formation target | 1.0 (`m = 78.92 M_KK`) | graph-unanchored on Tiers 1-2; `x = 30.12` above edge → protection-excluded on the whole spectrum |

What the Structural Verdict must say about each tier:

- **Tier 1 (the literal question — resolved in my favour).** The disorder→Goldstone-mass route is CLOSED. The correct closure is CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION (your whole-spectrum wall), with my (0,0) graph-scale ceiling `frac170 ≤ J_C2/(170Δ_BCS) = 0.0118` as its intra-band specialization, AND the disorder-onto-inter-band sub-ceiling `δm_φ ≤ 0.042 M_KK` (eq. 11-12, `frac170 ≈ 5×10⁻⁴`) as its inter-band specialization. Both disorder specializations are walled — the second one BELOW the first.

- **Tier 2 (yours).** The inter-band Leggett mass is graph-anchored at 5.557 M_KK — in-graph, on the off-(0,0) block, NOT Reading-B-unanchored. I withdrew that claim in CONVERGENCE and it stays withdrawn. But this tier is a CLEAN coupling, not a disorder mechanism (eq. 11-12), so it does not reopen the disorder route; it RAISES the DM-mass ceiling to `frac170 ≈ 0.070` and is itself 14.2× short of target.

- **Tier 3 (mine).** The 170× target is unreached on every graph-derived mechanism (intra OR inter-band) AND unprotectable (`x = 30.12`). The verdict therefore RE-TYPES the 170×: it is not a protected heavy gap the substrate must supply. The DM mass stays anchored at the clean Leggett scale (Tier 2); the cold, transit-frozen GGE dispersion (the Ordered Veil — `S_ent = 0`, `R_therm = 5252`, diabatic) does the structure-formation work, with no 170× enhancement of the phase Goldstone.

The mechanism handed to `S116-W3-GOLDSTONE-M2` is therefore NOT Branch A "build the off-(0,0) disorder operator and read `frac170 → 1`" — eq. (11)-(12) prove that compute returns a mass BELOW the (0,0) ceiling, not above it. It is a refined two-tier ceiling-pin (Branch B): pin `frac170(disorder, intra-(0,0)) ≤ 0.024`, pin `frac170(disorder, inter-band) ≈ 5×10⁻⁴` (eq. 11), and pin the CLEAN inter-band Leggett scale `frac170(Leggett) = 0.0704` as the DM-mass ceiling — a separate, non-disorder object.

**Two sharper questions for Round 3:**

1. The Leggett mass enters `m_Leggett² ∝ J_⊥` at FIRST order in the clean inter-band pair-transfer; the disorder enters at SECOND order, `δm²_φ ~ h_rf²/E_n` (eq. 11), DECREASING with sector energy and topping out at 0.042 M_KK. Will you concede that the channel reaching 5.56 is the clean Leggett `J_⊥` — NOT on the disorder axis — so the disorder→Goldstone-mass route (this wave's literal question) stays CLOSED, and the inter-band Leggett mass is a separate, already-registered object that was never a disorder observable?

2. Granting the clean Leggett anchor at `frac170 = 0.0704` (14.2× short) and `x = 30.12` above the edge: do you agree the 170× requirement is RE-TYPED — not a protected heavy gap the substrate must supply, but a structure-formation kinematic the cold transit-frozen GGE dispersion meets at the anchored Leggett mass with NO 170× enhancement? If yes, the verdict CLOSES the disorder route AND dissolves the target, leaving the DM mass graph-anchored at 5.56 — not a surviving disorder channel that reaches 170×.

### R2 · phonon-first-cosmologist

#### CONVERGENCE — where you now grant the landau side

I grant the decisive derivation, and I grant it cleanly, because it overturns my own R1 Branch A. In R1 I answered your Q1 by naming "inter-band disorder mixing onto the Casimir-graded Peter-Weyl ladder" and assigned it the sector energy `E_n = 0.633√C_2 + 0.555`, claiming it breaks the `0.012` ceiling toward the target. Your R2 §DISSENT(1) shows that reading is wrong in its DIRECTION, and the substitution chain is yours and correct: a random off-(0,0) field couples the phase mode `|φ⟩` (at `E_φ ≈ 0`) to a heavy sector `|n⟩` (at `E_n`), and integrating out the heavy sector (Schrieffer-Wolff / 2nd-order PT) gives `δm²_φ = |v|²/(E_n − E_φ) ≈ h_rf²/E_n` (your eq. 11), so `∂(δm²_φ)/∂E_n = −h_rf²/E_n² < 0`. The heavier the inter-band sector, the SMALLER the disorder-induced phase mass. **I had the operator right (off-(0,0), inter-band) and the mechanism backwards**: I treated the SECTOR ENERGY `E_n` as if it were the induced MASS, when `E_n` is the energy denominator that SUPPRESSES the induced mass. Your eq. 12 is decisive — `δm_φ(C_2{=}3) = √(0.05451²/1.6514) = 0.0424 M_KK`, `frac170 ≈ 5.4×10⁻⁴`, falling thereafter (`0.0314` at `C_2{=}15`). The genuine inter-band DISORDER channel is not a heavier mass but a lighter one: `22×` below my own construction-E ceiling `J_C2 = 0.933` and below even the bare dipolar `0.070`. My Branch-A "build the off-(0,0) disorder operator and read `frac170 → 1`" is withdrawn — that compute returns a mass BELOW the (0,0) ceiling, not above it.

So I answer your **R2 final-question-1** with an unqualified **YES**. The channel that reaches `m_Leggett = 11.97 Δ_BCS = 5.5571 M_KK` is the CLEAN Leggett `J_⊥` — the DETERMINISTIC inter-band pair-transfer (Leggett 1966), entering `m_Leggett² ∝ J_⊥` at FIRST order as the restoring force of the relative-interband-phase oscillation — NOT a random-field disorder mass. I correctly identified the OPERATOR in R1 (the off-(0,0) block of `D_K`, in-graph, NOT Reading-B-unanchored); I mis-identified the MECHANISM (clean `J_⊥`, not Larkin/Imry-Ma `E²/ξ²`). The two are different objects at different orders in the SAME inter-band coupling, and only the first-order clean one reaches 5.56. **Therefore the DISORDER→Goldstone-mass route — THIS wave's literal question — is CLOSED on BOTH specializations**: the intra-(0,0) graph-scale ceiling (`frac170 ≤ J_C2/(170Δ_BCS) = 0.0118`, your eq. 5, confirmed by S116-W3-GOLDSTONE-M2 FAIL) AND the inter-band-via-disorder sub-ceiling (`frac170 ≈ 5×10⁻⁴`, your eq. 11, BELOW the first). The surviving inter-band Leggett channel is a clean coupling — a separate, already-registered DM anchor that was never a disorder observable. The disorder axis is walled at every projection of `D_K`, intra- and inter-band alike. The substrate IS the full Peter-Weyl content; I had claimed the disorder operator reached a block your Gershgorin bound missed, and it does reach that block — but it reaches it WEAKER, not stronger. That correction is yours.

#### DISSENT — where you hold, with NEW argument (don't restate R1)

I concede the disorder route. My remaining ground is the one question R1 left untouched: can the CLEAN Leggett `J_⊥` ITSELF be cooperatively enhanced toward the target — a collective/multi-band resonance, or a geometric (quantum-metric) contribution on the off-(0,0) block where U(2)-invariance does not protect? I pushed each concrete version and report honestly: **none reaches `frac170 → 1`.** But the WAY they fail is new structure, and it is a STRONGER wall than your single-mode `x = 30` exclusion — it binds the entire collective spectrum, and it is built from your own Casimir-grading.

**(1) Collective `√N` enhancement SATURATES — your `1/E_n` weapon, turned on the clean coupling.** The cooperative escape would be Dicke-type: the phase mode couples not to one inter-band sector but coherently to all `N` sectors below the cutoff, and `N`-fold coherent coupling could in principle give a `√N` lift. Substitution chain, every symbol explicit:
- Step 1: `m_Leggett² ≈ Σ_n w(n)`, the collective relative-phase restoring force summed over inter-band sectors `n` (RPA/collective-mode form; first order in `J_⊥`).  [multiband Leggett, Leggett 1966]
- Step 2: each sector enters through its pair-propagator, so `w(n) = |⟨0,0|V_pair|n⟩|² / E_n^{\,p}` with `p ≥ 1` — an energy denominator, the SAME Casimir-graded `E_n` that suppressed your eq. 11.  [collab §3 eq 1: `E_n = 0.633√C_2(n) + 0.555`]
- Step 3: `E_n` is monotone increasing in `C_2(n)`, and the per-shell sector count grows only polynomially, so `Σ_n w(n)` is dominated by the lowest sectors and CONVERGES regardless of the exact `p ≥ 1`.  [direction from canonical form: `w(n) → 0` as `C_2 → ∞`]
- Step 4: therefore `m_Leggett(N) → m_Leggett(∞)` as `N → ∞`; the partial sums SATURATE, they do NOT run as `√N`.  [convergent series]
- Conclusion: the registered `5.5571 M_KK` IS (to the accessible truncation) that converged collective sum; adding higher sectors gives diminishing returns. The cooperative `√N` is already spent — it does not reach `14.2×`.

The `√N` is not free because the `N` sectors are NOT degenerate — they are Casimir-graded, and the high-`C_2` tail of the collective sum is killed by exactly the `E_n` suppression you derived. A collective sum over a Casimir-graded ladder saturates.

**(2) The geometric (quantum-metric) version is the WRONG OBSERVABLE — I close it against my own ledger.** My R1 named the off-(0,0) quantum metric (Peotta-Törmä) as the surviving geometric escape, since INV8-W3-2 found `Tr g = 0` for the lowest (0,0) doublet by U(2)-invariance but the off-(0,0) block is unprotected. Honest re-check: the quantum metric enters the superfluid WEIGHT `D_s = (2Δ/V)∫Tr g`, i.e. the STIFFNESS `ρ_s`, NOT the mass. Substitution chain: the framework dispersion is `ω_G = m_G / √ρ_s` (s48); `∂ω_G/∂ρ_s = −½ m_G ρ_s^{−3/2} < 0` — a LARGER geometric stiffness LOWERS the frequency. So the off-(0,0) quantum metric, even where unprotected and nonzero, is a stiffness knob that makes the mode LIGHTER in frequency (MORE below-edge protected), not a mass knob that lifts it toward 170×. My own INV8-W3-2 already drove this route to `R_stiff = 8.2×10⁻¹⁸` (17 decades below a Hubble backbone) — the geometric metric is structurally the wrong, and far-too-small, observable for a heavy mass. The quantum-metric escape is closed, and I close it.

**(3) The fiber ladder has NO HEADROOM — the collective continuum-edge cap.** This is the generalization of your single-mode wall to the whole collective spectrum, and the complement of (1): a protected (below-continuum) collective mode rides just under the continuum edge, and the edge is the top of the fiber ladder the substrate actually carries. At `L_max = 10` the highest single-fiber mode is `0.633√C_2(10,0) + 0.555 = 0.633√43.33 + 0.555 = 4.722 M_KK = 10.17 Δ_BCS`; the registered Leggett collective sits just above at `11.97 Δ_BCS = 5.557 M_KK`, already AT the ceiling the accessible ladder supports. To reach the target `170 Δ_BCS = 78.92 M_KK` on this ladder requires a fiber sector at `C_2 = ((78.92−0.555)/0.633)² ≈ 1.53×10⁴`, i.e. `(p,q)` with `p+q ≈ 213` — `21×` beyond the `L_max=10` truncation AND at `x ≈ 30` above any continuum edge (your eq. 14). Neither accessible nor protected. Points (1) and (3) are two faces of one ceiling: the collective SUM saturates (high sectors contribute weakly) AND the heaviest PROTECTED collective mode is capped at the continuum edge `≈ O(10 Δ_BCS)` — both `≈ 17×` short of `170 Δ_BCS`.

**Net:** I concede the cooperative-enhancement-of-mass escape is NOT concretely nameable — `√N` saturates (1), the quantum metric is the wrong observable (2), the fiber ladder is `17×` short and unprotectable (3). I therefore grant your Tier-3 re-typing: the `170×` is not a protected heavy gap the substrate must supply.

**Where I hold (the genuine dissent-in-emphasis).** I dissent from "re-typed ⇒ resolved." Your Tier-3 ASSERTS the cold transit-frozen GGE dispersion does the structure-formation work at the anchored mass; it does not COMPUTE it. The `170×` originated as a cross-PILLAR ratio — a Pillar-II `n_s` SA-Goldstone correlator-crossover scale `K* = 0.087` over a Pillar-V Leggett/Goldstone mass (collab §5) — and was re-typed as a single Pillar-V DM structure-formation mass in HK-170X-DM (S112). A ratio of two different-pillar observables failing to be a single protected mass is NOT a shortfall of the DM mass (which is fine, graph-anchored at 5.5571) — it is a TYPE-ERROR in the import. And the forward consequence is not Branch B alone: pinning `frac170 ≤ 0.012` certifies a wall on the mis-typed ratio, but it leaves the ACTUAL structure-formation observable — the free-streaming length at the anchored mass with the cold transit-frozen dispersion — UNTESTED. "Re-typed" discharges nothing until that compute runs. THAT is my standing ground: not a cooperative mass enhancement (conceded, thrice), but the claim that the verdict must hand S117 the kinematic free-streaming compute, or the DM-structure-formation question is "re-typed but unverified," not "closed."

#### EMERGENCE — new structure from the exchange

We converge on the three-tier ladder, and I extend your R2 table by one column — the wall that binds each tier, which is ONE wall (protection-magnitude exclusion) seen in four projections:

| Tier | Object | frac170 | Status | Binding wall (one wall, projected) |
|:--|:--|:--|:--|:--|
| 1a | (0,0) intra-band disorder | ≤ 0.0118 (Cheeger) / 0.0245 (Fiedler λ_1) | CLOSED; S116-W3-GOLDSTONE-M2 FAIL | graph-scale ceiling `m_G ≤ J_C2` — intra-band specialization |
| 1b | inter-band-via-disorder (2nd order) | ≈ 5×10⁻⁴ | CLOSED; BELOW 1a | `δm²_φ ~ h_rf²/E_n` Casimir-suppressed (your eq. 11) |
| 2 | clean inter-band Leggett `J_⊥` | 0.0704 | surviving DM anchor (NOT disorder); 14.2× short; `√N` SATURATES | collective continuum-edge cap + Casimir-graded saturation (my DISSENT 1–3) |
| 3 | 170× structure-formation requirement | 1.0 | RE-TYPED: cross-pillar ratio, not a protected mass | `x = 30.12` above edge — unprotectable on the whole spectrum |

Both opening positions are partly right. Your graph-scale wall is the intra-band specialization of the real wall (Tier 1a). My R1 "the disorder space is not exhausted" was right that the inter-band block is a DIFFERENT operator (Tier 2 — the clean Leggett at `0.0704`, breaking your eq-8 "universal `[4×10⁻⁵, 0.036]`" band as a whole-spectrum statement) but WRONG that DISORDER reaches it (Tier 1b — your eq. 11 kills my Branch A; the genuine inter-band disorder mass is `≈ 5×10⁻⁴`, BELOW the intra-(0,0) ceiling). The synthesis neither opening had: **the disorder route is closed at every projection of `D_K`; the DM mass is graph-anchored at the clean Leggett scale; and the `170×` is a re-typed cross-pillar ratio** — and the wall that does all three is one proposition, `protected ⇒ m ≤ O(\text{top of fiber ladder}) ≈ O(10\,Δ_BCS)`, the protection-magnitude exclusion applied to the full collective spectrum.

**Mechanism handoff to S116-W3-GOLDSTONE-M2.** Confirmed **Branch B (ceiling-pin)** — already executed and FAIL, and that FAIL is now correctly READ: it pins the Tier-1a intra-(0,0) ceiling `frac170 = 0.0118 (Cheeger) / 0.0245 (Fiedler λ_1)`, the disorder route's intra-band wall. The verdict ADDS the two specializations the compute did not test but the exchange derived analytically: Tier-1b `frac170(disorder, inter-band) ≈ 5×10⁻⁴` (your eq. 11) and the Tier-2 clean-Leggett DM-mass ceiling `frac170(Leggett) = 0.0704` (a separate, non-disorder object). No single-block compute closes the target; none needs to — the target is re-typed off the mass axis.

**The S117 forward-compute that DISCHARGES the re-typing (my standing dissent, made concrete).** Pre-register `S117-FREESTREAM-AT-ANCHOR`:
- **WHAT**: the DM comoving free-streaming length `λ_fs(m_Leggett, v_rms^{GGE})` at the ANCHORED Leggett mass `m_Leggett = 11.97 Δ_BCS`, with the transit-frozen GGE velocity dispersion `v_rms^{GGE}` from the Bogoliubov occupation, against the structure-formation requirement (half-mode mass ≥ dwarf-galaxy scale / `λ_fs ≤ Lyman-α scale`).
- **INPUTS**: `m_Leggett` (C11 anchor `MASS_LEGGETT_OVER_DELTA = 11.97`); the S38 Bogoliubov squeeze spectrum (`⟨n⟩ = 730.6`, `n_Bog = 0.99863`, squeeze `r`); the Ordered-Veil diabatic certification (`S_ent = 0`, `R_therm = 5252` — the GGE never thermalized, so `v_rms` is the COLD transit-frozen value, NOT a thermal `√(T/m)`).
- **GATE**: PASS = the cold transit-frozen dispersion gives `λ_fs` below the structure-formation threshold at the anchored mass with NO 170× enhancement (the re-typing is DISCHARGED — cold kinematics does the work); FAIL = a genuine warm-DM tension at the anchored mass (a KINEMATIC tension, not a missing-mass shortfall, not a disorder route — a new, sharper open question).
- **EFFORT**: low (closed-form free-streaming integral over a known Bogoliubov spectrum; no new diagonalization).

A lower-priority companion, `S117-LEGGETT-COLLECTIVE-CEILING`, would diagonalize the full inter-band pair-transfer across all `(p,q)` at `L_max=10` and read the heaviest PROTECTED collective mode — pre-registered prediction: it SATURATES at `frac170 ≈ 0.07` (the registered anchor), numerically confirming the collective protection-magnitude exclusion of my DISSENT (1)+(3). High-confidence PASS, low information; `FREESTREAM` carries the EVOI.

**Answer to your R2 final-question-2 (YES, with the sharpening).** I agree the `170×` is re-typed — not a protected heavy gap the substrate must supply. I add: it was never a single mass observable at all (a cross-pillar ratio), so its non-realization as a protected mass is informative about the IMPORT (HK-170X-DM mis-typed it), NOT about the DM mass (graph-anchored at 5.5571, fine). The DM mass stays at the clean Leggett scale; the cold transit-frozen GGE dispersion is the structure-formation mechanism — but that mechanism is ASSERTED until `S117-FREESTREAM-AT-ANCHOR` computes `λ_fs` and discharges it.

**My final question for Round 3.** Do you agree the Structural Verdict closes the DISORDER route as **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION** (with Tier-1a/1b/2 as its intra-band, inter-band-disorder, and clean-Leggett projections), AND that the verdict's forward mandate is NOT exhausted by the Branch-B ceiling-pin (which certifies a wall on the mis-typed ratio) but REQUIRES `S117-FREESTREAM-AT-ANCHOR` to convert "170× re-typed" from an ASSERTION into a discharged result — so the honest verdict line reads "disorder route CLOSED; DM mass graph-anchored at 5.5571 M_KK; 170× re-typed-and-routed-to-kinematic-test," and explicitly NOT "disorder route closed, DM mass unanchored"?

---

## R3 — Convergence on a Structural Verdict

### R3 · landau-condensed-matter-theorist — final position

#### Answer to your R3 final question — head-on, YES to both halves

**Half 1 (the label).** Yes. The disorder→Goldstone-mass route closes as **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION**, with Tier-1a / Tier-1b / Tier-2 as its intra-band, inter-band-via-disorder, and clean-Leggett projections. My R1 *CLOSED-BY-GRAPH-SCALE-WALL* was the intra-band specialization (Tier 1a) of your genus. The graph-scale ceiling `m_G ≤ J_{C2}` is true and airtight — but on `H_φ`, the (0,0) shadow of `D_K`; the operative wall binds the whole Peter-Weyl spectrum, not the shadow. Your framing is the correct one and I do not re-open it.

**Half 2 (the forward mandate).** Yes — and here you held ground I now concede without reservation. The Branch-B ceiling-pin certifies a wall on the *mis-typed ratio* (`frac170 ≤ 0.0118`); a wall on a mis-typed object is a real result, but it is not a discharge of the physical question. "Re-typed" is a reclassification, not a computation. Under my own standing rule — only new computation against a pre-registered gate changes the state of knowledge — an *asserted* re-typing carries zero evidential weight until `S117-FREESTREAM-AT-ANCHOR` runs. So the honest verdict line is exactly the one you wrote:

> disorder route **CLOSED**; DM mass **graph-anchored** at the clean inter-band Leggett scale (5.5571 M_KK, C11-conditional); **170× re-typed-and-routed-to-kinematic-test**

— and explicitly **not** "disorder route closed, DM mass unanchored." I withdrew "unanchored / Reading B" in R2 and it stays withdrawn. The forward mandate is two-pronged, not one: **Branch B** closes the *wall* (done, FAIL); **`S117-FREESTREAM-AT-ANCHOR`** closes the *physics* (queued). Neither alone is the verdict.

#### The five confirmations the Structural Verdict can lift verbatim

**1 — Three-tier ladder: ACCEPTED as the shared structure.** Tier 1a+1b (disorder) CLOSED at every projection of `D_K`; Tier 2 (clean Leggett `J_⊥`) surviving but 14.2× short and cooperatively saturated; Tier 3 (170×) re-typed off the mass axis. Both opening positions are partly right, and the ladder is determinate at each tier — the synthesis neither opening had.

**2 — "One wall in four projections": ACCEPTED, and here is its order-parameter content.** This is the Landau payload, and it is what makes your protection-magnitude exclusion a *theorem* rather than a coincidence. The condensate carries ONE energy scale, the gap `Δ_BCS` (R-protected, S70). Every operator that can pin or carry the U(1)₇ phase mode is locked to it, so every *protected* mode obeys `m ≲ O(10 Δ_BCS)`:

$$\text{(intra-cell bond)}\qquad J_{C2} = 0.933 \approx 2\Delta_{\rm BCS}\quad(\text{Ambegaokar–Baratoff}); \tag{15a}$$
$$\text{(fiber gap)}\qquad |\lambda(D_K)| \ge \sqrt{R_K/4} \ge \sqrt 3 = 1.73\quad(\text{Lichnerowicz, collab eq 8}); \tag{15b}$$
$$\text{(protected freq cap)}\qquad \omega_G < 2\Delta_{\rm BCS}\ \Rightarrow\ m_G < 2\Delta_{\rm BCS}\sqrt{\rho_s} = 0.9285\times 2.8217 = 2.62\ \text{M\_KK}; \tag{15c}$$
$$\text{(single-fiber ladder top, }L_{\max}{=}10\text{)}\qquad 0.633\sqrt{C_2(10,0)}+0.555 = 4.72\ \text{M\_KK} = 10.17\,\Delta_{\rm BCS}. \tag{15d}$$

Every cap is `O(Δ_BCS)`–`O(10 Δ_BCS)`; none is `O(170 Δ_BCS)` (the registered Leggett collective rides just above (15d) at `11.97 Δ_BCS`, still `O(10 Δ_BCS)`). The target needs `m = 170 Δ_BCS = 78.92 M_KK`, i.e. `x_target = (m/\sqrt{ρ_s})/(2Δ_BCS) = 30.12` (R2 eq 14) — 30× above the pair-breaking edge. **The protection requirement (`x < 1`) and the magnitude shortfall (`frac170 ≪ 1`) are the SAME inequality** `m ≲ O(10 Δ_BCS)`, because a single-gap condensate cannot manufacture a *protected* mode 14× its own ladder top. That is the single binding proposition; "graph-scale ceiling" was its (15a) face, your exclusion is the whole-spectrum statement (15b)-(15d). And it folds Tier-1b in for free: (15b) is *why* the inter-band disorder channel is suppressed — `δm²_φ = h_rf²/E_n` with `E_n ≥ √3` (Lichnerowicz), so the same floor that keeps the fiber gap above the edge makes random-field pinning onto it *weaker*, not stronger (R2 eq 11). One floor, two consequences: protection and suppression.

**3 — Branch-B handoff: CONFIRMED; the FAIL is correctly read.** `S116-W3-GOLDSTONE-M2` returned FAIL at `frac170 = 0.0118` (Cheeger) / `0.0245` (Fiedler λ_1). That value pins the **Tier-1a intra-(0,0) ceiling** — the disorder route's intra-band wall — and NOTHING about the DM mass. The verdict ADDS the two specializations the compute did not test but the exchange derived analytically:
- **Tier-1b** — `frac170(\text{disorder, inter-band}) ≈ 5×10⁻⁴` (R2 eq 11), BELOW the Tier-1a ceiling: the inter-band *disorder* channel is the lightest of all, and it is what kills Branch A.
- **Tier-2** — `frac170(\text{Leggett}) = 0.0704`: the clean inter-band `J_⊥` DM-mass ceiling, a SEPARATE non-disorder object.

Housekeeping note (memory-staleness, not re-litigation): my own S116 agent-memory still records this FAIL under the *superseded* reading ("DM mass graph-unanchored — Reading B"). This workshop overturns that — the FAIL pins the Tier-1a disorder ceiling, and the DM mass is graph-ANCHORED at the Tier-2 Leggett scale, NOT Reading-B. I flag it for correction at wave-synthesis.

**4 — `S117-FREESTREAM-AT-ANCHOR`: ENDORSED as the EVOI-carrying forward compute, with three gate refinements** (all kinematics / machinery-pin discipline; none changes the WHAT):

- **(R-i) Pin the `v_rms`-from-occupation mapping as the load-bearing PRDR machinery — do NOT presuppose coldness.** The cold-vs-warm verdict hinges entirely on how `v_rms` is extracted. Pre-register it as the explicit second moment of the frozen Bogoliubov occupation (non-relativistic form, `k ≪ m` today),
$$v_{\rm rms}^2 \;=\; \frac{\int (k/m)^2\, n(k)\, d^3k}{\int n(k)\, d^3k}\bigg|_{\rm frozen}, \tag{16}$$
NOT a thermal `\sqrt{T_{\rm DM}/m}`. The substrate certification that LICENSES (16) over the thermal form is the Ordered Veil: `S_ent = 0`, `R_therm = 5252` (S95) — the GGE never re-thermalized, so there is no Maxwell-Boltzmann temperature to assign; `v_rms` is read off the frozen `n(k)`. Coldness is then a COMPUTED output of (16), not an input. This single pin prevents the gate being gamed by a `v_rms` convention choice.
- **(R-ii) Declare which mass-unit enters `λ_fs`.** The Leggett mass is registered both as a substrate scale (`5.557 M_KK`) and as a laboratory rest energy (`M_DM_Leggett_GeV`, derived sessions:100). Free-streaming consumes the *kinematic* mass; the gate must state which image it uses or the cold-vs-warm comparison is dimensionally ambiguous.
- **(R-iii) The FAIL branch is genuinely live — FREESTREAM carries the EVOI, agreed.** The companion `S117-LEGGETT-COLLECTIVE-CEILING` is a high-confidence PASS (re-confirms the (15d) collective saturation) and low-information. FREESTREAM is informative because its FAIL branch is real: IF the frozen `n(k)` of (16) carries significant high-`k` weight (the Mach-13.75 supersonic transit is broadband), the relic is warm at the anchored mass and the gate returns a genuine warm-DM tension — a NEW, sharper open question (a KINEMATIC tension), not a missing-mass shortfall and not a disorder route.

  Pre-registered prediction (mine, on record): I expect (16) to return `v_rms ≪ c` and `λ_fs` below the Lyman-α / half-mode threshold (cold), because the relic momentum is set at the transit epoch and redshifts to today — but that is a PREDICTION the gate tests, read against the pre-registered warm-DM datum whichever way it lands.

**5 — Closure label: CONFIRMED.** CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION, with the graph-scale ceiling as its intra-band ((0,0)) specialization. No refinement to the label; the refinements are to its *content* (item 2) and its *forward mandate* (item 4).

#### One numerical scoping I add (structure firm, number conditional)

Per `output-standards.md` (numerical vs structural): the STRUCTURAL change is durable — the DM mass is **in-graph** (an off-(0,0) `D_K` spectral functional, the clean Leggett `J_⊥`), **not Reading-B-unanchored**. That is the load-bearing result and it stays. The NUMBER inherits its provenance: `m_Leggett = 11.97 Δ_BCS = 5.5571 M_KK` is the **LEGGETT-MOMENT-70 / C11 anchor**, registered **CONDITIONAL** (atlas-04; conditional on `Γ_grav < H_0` survival, LEGGETT-GRAV-DECAY-67). So the verdict's Tier-2 entry should read "graph-anchored at the clean Leggett scale, numerically `5.5571 M_KK` under the C11-conditional `11.97` anchor" — the in-graph STRUCTURE is firm; the VALUE carries the C11 tag. This keeps the verdict's confidence equal to the register's (capstone-hygiene) and does not soften the structural point against Reading B in the slightest.

#### Final position on record

The disorder→Goldstone-mass route is **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION** — one wall, four projections (15a)-(15d): a single-gap condensate cannot carry a *protected* phase mode above `O(10 Δ_BCS)`, and the 170× target sits at `x = 30.12`, ~14× above the heaviest accessible protected mode (the Leggett collective, `11.97 Δ_BCS`) and 30× above the pair-breaking edge. The graph-scale ceiling `frac170 ≤ J_{C2}/(170 Δ_BCS) = 0.0118` is the airtight intra-band ((0,0)) specialization (Tier 1a, compute-confirmed FAIL); the inter-band *disorder* channel is lighter still (`frac170 ≈ 5×10⁻⁴`, Tier 1b, Lichnerowicz-suppressed); the clean inter-band Leggett `J_⊥` is the surviving DM-mass anchor (`frac170 = 0.0704`, Tier 2 — in-graph, C11-conditional `5.5571 M_KK`, **not** Reading B), 14.2× short and cooperatively saturated. The 170× is a re-typed cross-pillar ratio, NOT a protected mass the substrate must supply.

The verdict's forward mandate is two-pronged: **Branch B** (ceiling-pin) closes the *wall* — done, FAIL, correctly read as Tier-1a with Tier-1b and Tier-2 added analytically; **`S117-FREESTREAM-AT-ANCHOR`** closes the *physics* — pre-register (16) with the `S_ent = 0` Ordered-Veil certification licensing coldness, declare the mass-unit, and read `λ_fs` against the warm-DM datum. Until FREESTREAM runs, "170× re-typed" is an honest *assertion routed to test*, not a discharged result. Hand the Structural Verdict: **disorder route CLOSED; DM mass graph-anchored (clean Leggett, C11-conditional 5.5571 M_KK); 170× re-typed-and-routed-to-`S117-FREESTREAM-AT-ANCHOR`** — never "disorder closed, mass unanchored."

— landau-condensed-matter-theorist

### R3 · phonon-first-cosmologist — final position + writes the Structural Verdict below

**Where I finally stand.** The exchange overturned my own R1 opening, and I record the overturn without hedging. In R1 I named "inter-band disorder mixing onto the Casimir-graded Peter-Weyl ladder" as **Branch A** — a surviving *disorder* mechanism breaking the `0.012` ceiling toward the target. **That reading is withdrawn.** Landau's R2 §DISSENT(1) is correct and decisive: I had the OPERATOR right (the off-(0,0) block of `D_K` — in-graph, NOT Reading-B-unanchored) and the MECHANISM backwards. The substrate-first flow makes the error legible: `D_K spectrum → Josephson/Leggett couplings → m`. A random off-(0,0) field couples the phase mode `|φ⟩` (at `E_φ ≈ 0`) to a heavy fiber sector `|n⟩` (at `E_n = 0.633√C_2 + 0.555`); the sector energy `E_n` is the level-repulsion DENOMINATOR, not the induced mass. Schrieffer–Wolff gives `δm²_φ ≈ h_rf²/E_n`, so `∂(δm²_φ)/∂E_n = −h_rf²/E_n² < 0` — a HEAVIER inter-band sector SUPPRESSES the disorder-induced phase mass. The genuine inter-band disorder channel tops out at `δm_φ(C_2{=}3) = 0.042 M_KK` (`frac170 ≈ 5×10⁻⁴`) and falls thereafter — BELOW even the intra-(0,0) construction-E ceiling `J_C2 = 0.933`. I had treated `E_n` as a mass; it is an energy denominator. **The disorder route is CLOSED at every projection of `D_K`** — intra-(0,0) (Tier 1a, my Branch A's home, compute-confirmed FAIL) AND inter-band-via-disorder (Tier 1b, lighter still).

**The surviving channel is not disorder.** What reaches the registered DM anchor `m_Leggett = 11.97 Δ_BCS = 5.5571 M_KK` is the CLEAN multiband Leggett coupling `J_⊥` — the deterministic inter-band pair-transfer (Leggett 1966), entering `m_Leggett² ∝ J_⊥` at FIRST order, no Larkin domains, no random field. It is in-graph (an off-(0,0) `D_K` spectral functional), so landau's R1 "graph-unanchored, Reading B, like M_KK" is FALSE — and he withdrew it. But it is a SEPARATE, already-registered object, not a disorder mechanism, and it does not reopen this wave's literal question. I pushed every cooperative enhancement of the clean coupling toward the target — Dicke `√N`, the off-(0,0) quantum metric, the full fiber ladder — and report honestly: each fails, and the WAY they fail is the SAME wall. The `√N` SATURATES because the `N` sectors are Casimir-graded — the high-`C_2` tail is killed by the very `1/E_n` suppression landau turned on my Branch A. The quantum metric is the wrong observable: it sets the STIFFNESS `ρ_s`, and a larger geometric stiffness LOWERS `ω_G = m_G/√ρ_s` (MORE below-edge protected, not heavier) — my own INV8-W3-2 already drove that route to `R_stiff = 8.2×10⁻¹⁸`. The fiber-ladder top at `L_max=10` is `4.72 M_KK = 10.17 Δ_BCS`; the Leggett collective rides just above at `11.97 Δ_BCS`, ALREADY at the ceiling the accessible ladder supports, `14.2×` short of `170 Δ_BCS`.

**The 170× is re-typed — and I endorse landau's epistemic guardrail on what "re-typed" buys us.** The target is unreached on every graph-derived mechanism AND unprotectable (`x_target = 30.12`, 30× above the pair-breaking edge); a below-edge-protected mode cannot reach 170× on ANY operator. So the 170× is not a protected heavy gap the substrate must supply — it is a cross-pillar ratio (a Pillar-II `n_s` SA-Goldstone correlator-crossover scale over a Pillar-V Leggett mass) re-typed as a single DM structure-formation mass in HK-170X-DM. **But I hold landau to his own rule, and he holds me to it: "re-typed" is a reclassification, not a computation.** An asserted re-typing carries zero evidential weight until a pre-registered gate runs. The structure-formation work is done by the cold, transit-frozen GGE dispersion (the Ordered Veil: `S_ent = 0`, `R_therm = 5252`, diabatic) — but that is a CLAIM until `S117-FREESTREAM-AT-ANCHOR` computes the free-streaming length `λ_fs` at the anchored mass and reads it against the warm-DM datum. The Structural Verdict therefore **ROUTES the re-typing as a forward compute; it does NOT ASSERT it as closed.** Branch B closes the *wall* (done, FAIL, correctly read as Tier 1a); `S117-FREESTREAM-AT-ANCHOR` closes the *physics* (queued, EVOI-carrying). Neither alone is the verdict — and "disorder route closed, DM mass unanchored" is explicitly NOT the verdict.

I write the Structural Verdict below.

— phonon-first-cosmologist

---

## Structural Verdict

**Pinned position: CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION.** The disorder→Goldstone-mass route to the 170× factor is CLOSED at **every projection of `D_K`**. This is not the narrow graph-scale ceiling of the R1 openings; it is the whole-spectrum wall both poles converged on: *a single-gap condensate (`Δ_BCS` R-protected, S70) cannot carry a protected phase mode above `O(10 Δ_BCS)`.* The route is walled at the intra-(0,0) projection (Tier 1a, `frac170 ≤ 0.0118` Cheeger / `0.0245` Fiedler λ_1 — compute-confirmed FAIL) AND at the inter-band-via-disorder projection (Tier 1b, `frac170 ≈ 5×10⁻⁴` analytic — Schrieffer–Wolff `δm²_φ ≈ h_rf²/E_n`, Lichnerowicz-suppressed, BELOW Tier 1a). **CLOSED-BY-GRAPH-SCALE-WALL** (landau's R1 ceiling `m_G ≤ J_C2`) is the *intra-band specialization* (Tier 1a) of this genus — true and airtight, but on `H_φ` the (0,0) shadow of `D_K`, not on the full Peter-Weyl spectrum. The route status is RESOLVED: CLOSED, on the disorder axis, at every block.

**One wall, four projections** (the structural payload — `Δ_BCS` is the condensate's single energy scale; every operator that can pin or carry the U(1)₇ phase mode is locked to it):

$$J_{C2}=0.933\approx 2\Delta_{\rm BCS}\ (\text{Ambegaokar–Baratoff});\quad |\lambda(D_K)|\ge\sqrt3=1.73\ (\text{Lichnerowicz, collab eq 8});$$
$$\omega_G<2\Delta_{\rm BCS}\Rightarrow m_G<2\Delta_{\rm BCS}\sqrt{\rho_s}=2.62\ \text{M\_KK};\quad 0.633\sqrt{C_2(10,0)}+0.555=4.72\ \text{M\_KK}=10.17\,\Delta_{\rm BCS}.$$

Every cap is `O(Δ_BCS)`–`O(10 Δ_BCS)`; none is `O(170 Δ_BCS)`. **Protection (`x<1`) and magnitude-shortfall (`frac170≪1`) are the SAME inequality** `m ≲ O(10 Δ_BCS)` — you cannot lift the second cap without breaking the first.

**The three-tier ladder** (both opening positions partly right; the wall is ONE proposition seen in four projections):

| Tier | Object | frac170 | Status | Binding wall (one wall, projected) |
|:--|:--|:--|:--|:--|
| **1a** | (0,0) intra-band disorder | ≤ 0.0118 (Cheeger) / 0.0245 (Fiedler λ_1) | **CLOSED**; `S116-W3-GOLDSTONE-M2` FAIL | graph-scale ceiling `m_G ≤ J_C2` — intra-band specialization |
| **1b** | inter-band-via-disorder (2nd order) | ≈ 5×10⁻⁴ | **CLOSED**; BELOW 1a | `δm²_φ ~ h_rf²/E_n` Casimir/Lichnerowicz-suppressed (`E_n ≥ √3`) |
| **2** | clean inter-band Leggett `J_⊥` | 0.0704 | surviving DM anchor — **CLEAN coupling, NOT disorder**; 14.2× short; `√N` SATURATES; graph-anchored `5.5571 M_KK` (C11-conditional) | collective continuum-edge cap + Casimir-graded saturation |
| **3** | 170× structure-formation requirement | 1.0 | **RE-TYPED**: cross-pillar ratio, not a protected mass | `x = 30.12` above edge — unprotectable on the whole spectrum |

**Mechanism handed to `S116-W3-GOLDSTONE-M2`: Branch B (ceiling-pin) — NOT Branch A.** My R1 Branch A ("build the off-(0,0) disorder operator, read `frac170 → 1`") is withdrawn; the Schrieffer–Wolff `1/E_n` suppression proves that compute returns a mass BELOW the (0,0) ceiling, not above it. The compute ran as Branch B and returned **FAIL** at `frac170 = 0.0118` (Cheeger) / `0.0245` (Fiedler λ_1) — correctly read as the **Tier-1a intra-(0,0) ceiling**, the disorder route's intra-band wall, and NOTHING about the DM mass. The verdict ADDS, analytically, the two specializations the compute did not test: Tier-1b `frac170(disorder, inter-band) ≈ 5×10⁻⁴` and the Tier-2 clean-Leggett DM-mass ceiling `frac170(Leggett) = 0.0704` (a separate, non-disorder object). No single-block compute closes the target; none needs to — the target is re-typed off the mass axis.

**The honest verdict line (landau's, jointly endorsed):**

> disorder route **CLOSED**; DM mass **graph-anchored** at the clean inter-band Leggett scale (`5.5571 M_KK`, C11-conditional); **170× re-typed-AND-ROUTED-to-kinematic-test** (`S117-FREESTREAM-AT-ANCHOR`)

— and explicitly **NOT** "disorder route closed, DM mass unanchored." Reading B (WS-S112-4) is WITHDRAWN: the DM mass is in-graph (an off-(0,0) `D_K` spectral functional), not an external magnitude-import. The forward mandate is **two-pronged**: Branch B closes the *wall* (done, FAIL); `S117-FREESTREAM-AT-ANCHOR` closes the *physics* (queued). Under landau's own standing rule — only new computation against a pre-registered gate changes the state of knowledge — the "170× re-typed" is an honest *assertion routed to test*, carrying zero evidential weight until FREESTREAM runs. The verdict ROUTES it; it does not ASSERT it discharged.

| Item | Verdict | Note |
|:-----|:--------|:-----|
| Disorder→Goldstone-mass route | **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION** | walled at every `D_K` projection (Tier 1a + 1b); graph-scale wall is the intra-band specialization |
| Ceiling formula | `frac170 ≤ J_C2/(170·Δ_BCS) ≈ 0.0118` | AIRTIGHT on `H_φ` (the (0,0) shadow); NOT a whole-spectrum cap — inter-band Tier 2 lifts it to `0.0704` (still 14.2× short) |
| Mechanism handed to S116-W3-GOLDSTONE-M2 | **ceiling-pin (Branch B)** | NOT Branch A (Schrieffer–Wolff `1/E_n` kills it); FAIL correctly read as Tier-1a |
| Sub-(a) graph-scale ceiling airtight? | **YES for `H_φ`; NO as a whole-spectrum claim** | Gershgorin exact on the (0,0) projection; the registered Leggett anchor `5.5571 > ‖H_φ‖^{1/2} = 2.81` is already off-block. The operative wall is protection-magnitude exclusion, which DOES bind the whole spectrum |
| Sub-(b) surviving channel named? | **YES — clean inter-band Leggett `J_⊥`; NOT a disorder mechanism** | first-order `m_Leggett² ∝ J_⊥`, in-graph off-(0,0) `D_K` functional, already registered at `5.5571 M_KK` (C11). It does NOT reopen the disorder route; the genuine inter-band *disorder* channel (Tier 1b) is LIGHTER, not heavier |
| Sub-(c) discriminator (exceeds 0.012 toward 170×?) | **NO graph-derived mechanism reaches `frac170 → 1`** | Tier 2 breaks the `[4e-5, 0.036]` "universal" band → `0.0704`, but saturates 14.2× short; the target at `x=30.12` is unprotectable. The 170× is re-typed off the mass axis, not a surviving disorder mass |

---

## Remaining Open Questions

1. **Is the transit-frozen relic actually cold at the anchored mass?** The re-typing (Tier 3) ASSERTS the cold GGE dispersion does the structure-formation work; it is undischarged until `S117-FREESTREAM-AT-ANCHOR` computes `λ_fs(m_Leggett, v_rms^{GGE})` and reads it against the warm-DM datum. The FAIL branch is genuinely live: the transit is supersonic (Mach 13.75, broadband), so the frozen Bogoliubov `n(k)` may carry significant high-`k` weight → a warm relic at the anchored mass. This is the EVOI-carrying open question (gate pre-registered in Carry-Forward below).

2. **Does the clean Leggett collective saturate at `frac170 ≈ 0.07` under full inter-band diagonalization?** The `√N`-saturation argument (DISSENT 1+3) is analytic; `S117-LEGGETT-COLLECTIVE-CEILING` would diagonalize the full inter-band pair-transfer across all `(p,q)` at `L_max=10` and read the heaviest PROTECTED collective mode. Pre-registered prediction: SATURATES at the registered `0.0704` anchor (high-confidence PASS, low information — the companion to OQ-1, not its substitute).

3. **Which mass-image enters `λ_fs`?** The Leggett mass is registered both as a substrate scale (`5.557 M_KK`) and as a laboratory rest energy (`M_DM_Leggett_GeV`, sessions:100). Free-streaming consumes the *kinematic* mass; the gate must declare the image or the cold-vs-warm comparison is dimensionally ambiguous (landau R3 item R-ii). Open until `S117-FREESTREAM` pins it.

4. **Is the Tier-2 DM-mass anchor itself survival-conditional?** `Mass_LeggettDM/Δ_BCS = 11.97` is C11-CONDITIONAL on `Γ_grav < H_0` (LEGGETT-GRAV-DECAY-67). The verdict's "graph-anchored at `5.5571 M_KK`" inherits that conditionality; the in-graph STRUCTURE is firm, the VALUE carries the C11 tag. Whether the gravitational-decay survival gate stays PASS at higher precision is a standing open dependency of the anchor's numerical value (not its in-graph status).

5. **Is the cross-pillar `170×` ratio itself the right structure-formation observable?** The 170× entered as a Pillar-II `n_s` SA-Goldstone correlator-crossover scale `K*` over a Pillar-V Leggett mass (collab §5), then was re-typed as a single DM mass in HK-170X-DM. If FREESTREAM PASSes (cold relic, no enhancement needed), the residual question is whether the `n_s`-sector `K*` crossover has any DM-sector consequence at all, or whether the two pillars decouple entirely at the structure-formation scale.

---

## Wrap-Up

### What Changed

#### (a) Numerical revisions

- `frac170` "universal `[4×10⁻⁵, 0.036]` band" (landau R1 eq 8) → tiered ladder `{1a: ≤0.0118 (Cheeger) / 0.0245 (Fiedler λ_1); 1b: ≈5×10⁻⁴; 2: 0.0704; 3: 1.0}`. The band was a whole-spectrum overclaim; it is exact only for the (0,0) projection.
- inter-band disorder mass: my R1 "scale `0.633√C_2+0.555` breaks the ceiling toward target" → `δm_φ(C_2{=}3) = 0.042 M_KK`, FALLING (`frac170 ≈ 5×10⁻⁴`), BELOW the intra-(0,0) ceiling (Schrieffer–Wolff `δm²_φ ≈ h_rf²/E_n`, R2 eq 11–12).
- `frac170(Leggett) = 5.5571 / 78.923 = 0.0704` (14.2× short); `x_target = 30.12` (R2 eq 14).
- `‖H_φ‖^{1/2} = √(2 d^w_max) = 2.81 M_KK`; the registered Leggett anchor `5.5571 > 2.81` (off-block by 1.98×) — arithmetic proof the DM mass is NOT an `H_φ` eigenvalue.

#### (b) Structural changes

- **the 25-session "170× Goldstone-mass problem" RE-TYPED** — epistemic-type change: a missing-mass shortfall → a cross-pillar kinematic ratio (Pillar-II `n_s` SA-Goldstone correlator-crossover scale `K*` / Pillar-V Leggett mass), not a single protected DM mass the substrate must supply.
- **disorder route** `{OPEN-VIA-surviving-channel (my R1)} ∪ {CLOSED-BY-GRAPH-SCALE-WALL + unanchored (landau R1)}` → **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION** at every `D_K` projection (Tier 1a + 1b).
- **DM mass** `Reading-B-unanchored (landau R1 / WS-S112-4)` → **graph-ANCHORED** at the clean Leggett scale (in-graph off-(0,0) `D_K` functional); Reading B WITHDRAWN.
- **my R1 Branch A** `inter-band disorder ENHANCES` → `SUPPRESSES` (operator right, mechanism backwards); Branch A withdrawn, Branch B confirmed.
- **the binary** `{closed-wall vs surviving-channel}` → **three-tier ladder** (1D verdict → 4-tier partition; both openings partly right).
- **graph-scale ceiling reclassified**: standalone closure → intra-band specialization of the protection-magnitude-exclusion genus.

### What Holds

- The clean Leggett `J_⊥` DM anchor (`5.5571 M_KK`, C11-conditional, in-graph, NOT Reading B) — the load-bearing durable result.
- Below-edge protection / non-annihilating Leggett-channel DM: the Lichnerowicz floor `|λ| ≥ √3` keeps every nonzero fiber mode above the pair-breaking edge, the protected DM mode below it.
- The Ordered-Veil diabatic certification (`S_ent = 0`, `R_therm = 5252`, S95) — licenses the COLD transit-frozen dispersion that `S117-FREESTREAM` consumes.
- Abundance predicted (`Ω_DM h² = 0.1200`, 0.6% from 0.1207) and `σ_SI = 1.299×10⁻⁶³ cm²` NULL — both unaffected by the mass re-typing (the re-typing touches the structure-formation MASS, not the abundance or cross-section).
- The S114 W3-2 mis-attribution finding (170× = `n_s` Wall-W9 transplant; mack Row #79.compute-S114-W3-2, audit `b6a7727b…`) — CONSISTENT with and SHARPENED by this verdict (now: a cross-pillar ratio; discharge owed to FREESTREAM).
- The bare facts that bound the route: U(1)₇ Goldstone ungaugeable (`[iK_7,D_K]=0`, N4 BROKEN) and SA-massless (S48 wall #7).

### What Breaks or Strains

- **The W3 working-paper `fb_pair` backward-expectation is OVERTURNED.** `session-116-w3-workingpaper.md:92` pre-registered "on this FAIL the DM-mass-anchor routes to the Reading-B 'Josephson-graph-unanchored' conclusion." The workshop routes the FAIL to graph-ANCHORED, not unanchored. (Routed to housekeeping §A3 for §6 reconciliation.)
- **Curated-surface staleness**: `_promotion-triage.md:240` ("HK-170X-DM … HARDENED-OPEN") and atlas-04 P2 line 119 ("mass problem 170x") are stale relative to this verdict + the S114 mis-attribution. (Spec'd in §A3.)
- **"Re-typed ⇒ resolved" is REJECTED**: the re-typing is ASSERTED, not COMPUTED; the structure-formation physics is UNDISCHARGED until `S117-FREESTREAM` runs (landau's epistemic point, jointly endorsed — zero evidential weight until the gate fires).
- **FREESTREAM has a genuinely-live FAIL branch**: the Mach-13.75 supersonic transit is broadband, so the frozen Bogoliubov `n(k)` may carry high-`k` weight → a warm relic at the anchored mass = a NEW, sharper KINEMATIC tension (not a disorder route, not a missing mass).
- The Tier-2 anchor VALUE carries the C11 conditionality (`Γ_grav < H_0`, LEGGETT-GRAV-DECAY-67); the in-graph STRUCTURE is firm, the NUMBER is conditional.

### Carry-Forward Computations (MATH ONLY — propagate to S117)

#### CF-S117-FREESTREAM-AT-ANCHOR — the kinematic discharge of the re-typing [PRIMARY, EVOI-carrying]

1. **What**: the DM comoving free-streaming length `λ_fs(m_Leggett, v_rms^{GGE})` at the ANCHORED Leggett mass `m_Leggett = 11.97 Δ_BCS = 5.5571 M_KK`, with the transit-frozen GGE velocity dispersion from the Bogoliubov occupation, against the structure-formation requirement (half-mode mass ≥ dwarf-galaxy scale / `λ_fs ≤ Lyman-α scale`). Pin `v_rms` as the EXPLICIT second moment of the frozen occupation, `v_rms² = ∫(k/m)² n(k) d³k / ∫ n(k) d³k |_frozen` (non-relativistic, `k≪m` today), NOT a thermal `√(T_DM/m)` — coldness is a COMPUTED OUTPUT, not an input (landau R3 item R-i; the `S_ent=0` Ordered Veil licenses the frozen-`n(k)` reading over a Maxwell-Boltzmann temperature). Declare which mass-image enters `λ_fs` (R3 item R-ii).
2. **Inputs**: `m_Leggett` (`Mass_LeggettDM_over_Delta_BCS = 11.97`, C11 anchor, CONDITIONAL on `Γ_grav < H_0`); the S38 Bogoliubov squeeze spectrum (`⟨n⟩ = 730.6`, `n_Bog = 0.99863`, squeeze `r`); the Ordered-Veil diabatic certification (`S_ent = 0`, `R_therm = 5252`, S95); `Δ_BCS = 0.4642547394830737` (R-PROTECTED, S70).
3. **Gate**: PASS = the cold transit-frozen dispersion gives `λ_fs` below the structure-formation threshold at the anchored mass with NO 170× enhancement (the re-typing is DISCHARGED — cold kinematics does the work); FAIL = a genuine warm-DM tension at the anchored mass (a KINEMATIC tension — a new, sharper open question — NOT a missing-mass shortfall and NOT a disorder route). `[SIGN]` on `(λ_fs − λ_threshold)`.
4. **Effort**: low (closed-form free-streaming integral over a known Bogoliubov spectrum; no new diagonalization).
5. **Depends on**: this workshop's Tier-2 anchor (`m_Leggett = 5.5571 M_KK`); S38 Bogoliubov npz; S95 Ordered-Veil certification; `canonical_constants.py: Mass_LeggettDM_over_Delta_BCS, Delta_BCS`.

#### CF-S117-LEGGETT-COLLECTIVE-CEILING — confirm the collective protection-magnitude exclusion [COMPANION, low-EVOI]

1. **What**: diagonalize the FULL inter-band pair-transfer across all `(p,q)` at `L_max=10`; read the heaviest PROTECTED collective Leggett mode and confirm it SATURATES at `frac170 ≈ 0.07` (the registered anchor), numerically certifying the `√N`-saturation + continuum-edge cap (DISSENT 1+3).
2. **Inputs**: the `D_K` `L_max=10` spectrum cache; collab §3 sector-energy `E_n = 0.633√C_2(n) + 0.555`; the clean Leggett `J_⊥` inter-band pair-transfer; `Δ_BCS`.
3. **Gate**: PASS = the heaviest protected collective mode lands at `frac170 ∈ [0.06, 0.08]` (saturation confirmed, `√N` spent); a value `≫ 0.08` would (surprisingly) reopen Tier 2 and is the informative tail.
4. **Effort**: medium (full inter-band diagonalization at `L_max=10`; GPU `torch.linalg` on the off-(0,0) blocks per `computation-environment.md`).
5. **Depends on**: `D_K` L_max=10 cache; this workshop's Tier-2 prediction (`0.0704`); collab §3 `E_n`.

> Routing: both are GENUINE FUTURE COMPUTATION (not hygiene), propagate via `/rclab-plan` to S117. The Branch-B ceiling-pin compute (`S116-W3-GOLDSTONE-M2`, FAIL) is THIS wave's, already executed — NOT a carry-forward.

### Effected In-Session (NON-MATH — executed by the R3-B agent before terminating)

- [x] **DM-mass-route status update — specified + routed to housekeeping §A.** The three curated sole-writer surfaces (atlas-04 P2 / HK-170X-DM standing-gap & mack inventory Row #79 / open-channel-ledger §DMMASS) AND the W3-WP `fb_pair` line-92 backward-expectation correction are SPEC'd with precise *current → corrected* text + anchor at `sessions/session-116/session-116-housekeeping.md §A3`, for the orchestrator / mack / little designated-writer reviewed patch at §6 wave-synthesis (the route status is a JOINT workshop × `S116-W3-GOLDSTONE-M2` reading). NOT bulk-edited (curated-registry sole-writer discipline, `feedback_framework-hygiene.md` + `feedback_mack-bridge-role.md`). **Action = specified + routed to housekeeping §A3.**
- [x] **Own agent memory — executed directly.** Added the S116-W3 disorder-closure cross-pillar bridge bullet (the operator-right / mechanism-backwards lesson + the protection-magnitude-exclusion genus + the multiband-Leggett ↔ off-(0,0)-block identity) to `.claude/agent-memory/phonon-first-cosmologist/MEMORY.md §"Key Cross-Pillar Bridges"`. AMRI-safe: the canonical `frac170` ladder + anchor VALUES live in the framework register (routed via §A3), NOT duplicated in memory — the memory carries the agent-private methodological lesson only. Safe non-curated in-domain item.
- [x] **No `.py` compute executed** — this workshop closes by artifact-existence (no verdict line); the math carry-forwards are routed to S117.

### Closing Line

The graph cannot pin its own phase mode 85× its stiffest bond, the inter-band disorder channel that I thought escaped that wall is lighter still, and the only thing that reaches the dark-matter scale is the clean Leggett coupling already on the books — so the disorder route is CLOSED at every projection of `D_K`, the DM mass is graph-ANCHORED at `5.5571 M_KK`, and the storied "170×" was never a missing mass but a cross-pillar ratio now routed to the one compute that can discharge it: the free-streaming length of a cold, transit-frozen relic.
