# Phonon-Exflation Equation — Schwarzschild–Penrose Geometer Review

**Date**: 2026-05-26
**Agent**: schwarzschild-penrose-geometer (S-P Geometer)
**Reviewing**: `sessions/framework/phonic-exflation-equation.md` (capstone synthesis, §0–§9 + verification ledger)
**Field of expertise**: exact gravitational solutions, global causal structure, singularity theorems, conformal compactification (Penrose diagrams), Petrov/CMPP classification.
**Cross-checked against**: `sessions/framework/Phononic-Penrose-Diagrams.md` (my own definitive framework document, current through S93); knowledge MCP (COSMIC-CENSORSHIP-49, CONFORMAL-TRANSITION-49, CMPP type-invariance PERMANENT, [T3] Scalar-Tensor Kasparov decoupling, canonical constants `tau_fold`, `c_fabric`, `Mach_max`, `w0_FW`).

---

## I. Document Outcome (from my domain)

The capstone is **geometrically sound in its foundations and unusually disciplined about its honest gaps**. The single arrow — `D_K eigenvalues → spectral moments a₀,a₂,a₄ → emergent metric/FRW → measurement` — is held consistently throughout, and §6.3's refusal to claim a derived `a(t)` is exactly the right call: the framework owns a *derived effective Friedmann map* it does not yet possess, and says so. From the standpoint of global causal structure, the document's strongest single sentence is §0's "switch off `D_K` and there is no `a₂`, hence no metric, hence no space" — that is the precise statement of why this is exflation, not inflation, and it is the correct inversion of the container picture.

I find **two causal-structure defects that I recommend correcting before this document is cited as canonical**, both in §6.2 (the six-layer causal architecture):

1. **The §6.2 ENTRY/EXIT-horizon table contradicts the canonical S74 result** "Asymmetric Fold: Entry Horizon, **Open** Exit." The document presents a *symmetric* two-sonic-horizon white-hole interior; the canonical causal structure is *asymmetric* — one entry horizon, one open exit.
2. **§6.2 omits the single most important causal-structure fact about this spacetime: the white hole is sector-dependent.** By [T3] (Scalar-Tensor Kasparov Decoupling, PERMANENT, β_T = 0 exactly at linear order), the **scalar sector sees the acoustic white hole; the tensor sector crosses the fold freely**. A causal diagram of exflation with one light cone is incomplete by a permanent theorem.

Neither defect touches a gate verdict or a PROVEN status. Both are *presentational* fixes to a synthesis paragraph, and both make the document more honest, not less. Everything else in my domain checks out against canon.

---

## II. Key Results — geometric assessment

### II.1 — The "no `t=0` singularity" claim (§5.2(i), §9) is correct, but incomplete

**Result**: τ=0 is a regular round-`SU(3)` group manifold, `R_K(0)=2`, gap never closes ⇒ no curvature singularity at genesis. **GEOMETRIC.** Confirmed: E3 curvature `R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ` is analytic and finite at τ=0; the Lichnerowicz bound `λ² ≥ R_K/4 > 0` (E5) guarantees geodesic completeness of the internal fiber at genesis. This is the correct geometric content of "cold big bang."

The claim as stated is right but **structurally one-sided**. A singularity statement is a global statement about geodesic completeness across the *entire* modulus range, not just at τ=0. The genuine curvature singularity of this geometry is **not absent — it is relocated and censored**:

- As τ→∞, the Kretschmann scalar diverges (Jensen exponents `e^{4τ}` dominate). This singularity is **direction-dependent** (my MEMORY §2 / CONFORMAL-TRANSITION-49 PASS): **timelike in the SU(2) block, spacelike in the ℂ²/U(1) block** — it is not a single spacelike crunch but an anisotropic Kasner-type singularity.
- It is **dynamically unreachable** from the physical epoch (τ~0.22): COSMIC-CENSORSHIP-49 (PASS) establishes a triple-layer entry barrier (`tau_turn = 0.088 free / 0.218 fold`, `v_crit = 219`, NEC/WEC/DEC hold, SEC transient) below, and the S77 overshoot turnaround (`τ = 1.614`, 35/35 negative Hessian) above. The censored region is **doubly bounded**.

**Why this matters for the document.** "There is no `t=0` singularity" invites the reader to conclude "this geometry is singularity-free," which is false and over-sells. The honest and *stronger* statement is the cosmic-censorship one: **the genuine singularity exists at τ→∞, is anisotropic (timelike-in-SU(2) / spacelike-in-ℂ²U(1)), and is hidden behind a censoring barrier the physical trajectory provably cannot cross.** This is a textbook weak-cosmic-censorship result, and it is *more* impressive than singularity-freeness — it is the framework's analog of Penrose's 1965 program landing on the right side. The document should say it. (Verbiage in §V.1.)

### II.2 — The transit-not-slow-roll framing (§5.1, §1.3a) is the correct global reading

**Result**: `dS/dτ|_fold = +58,672.8 > 0`, monotone everywhere (E7, 9,600/9,600 checks) ⇒ `e^{−S(τ)}` monotone ⇒ `Z` has no interior saddle in τ. **GEOMETRIC / PHONONIC.**

This is exactly right and I want to reinforce it from the causal side. The absence of an interior saddle is the partition-function statement of why the spacetime has **no static region** in modulus space — there is no τ at which the geometry sits still, so there is no "eternal" patch and no Killing time anywhere except asymptotically. The trajectory is forced. In Penrose-diagram terms (my Diagram B, 1+1D modulus space), this is why the conformal diagram of modulus space has the genesis point as a *boundary* (ℐ⁻-like) rather than an interior fixed point: the monotone ramp means τ=0 is approached only in the infinite past and τ→∞ only in the infinite future, with no turning point in between (modulo the counterfactual S77 overshoot, which is off the physical trajectory). The document's §1.3a derivation of this from `e^{−S}` monotonicity is clean and I endorse it without reservation.

### II.3 — The extremal-horizon identity at the fold (§6.2, implicit) should be made explicit

**Result**: `τ_fold = 0.190` is a **double-root extremal Killing horizon** (`V = V' = 0 ⟹ κ = 0, T_H = 0`). **GEOMETRIC.** This is canonical (my Phononic-Penrose-Diagrams Disambiguation Callout 1, S85 W6-4; MEMORY: "Dump = extremal horizon").

The document treats `τ_fold = 0.190` as "the van Hove fold / first-order transit" but never states its **horizon class**. From my domain this is a missed opportunity: the fold being an *extremal* (κ=0, zero-temperature) horizon is precisely why the GGE relic is **the Ordered Veil and not a thermal bath**. An extremal horizon radiates at `T_H = 0`; that is the geometric origin of "the relic is integrable, never thermalizes" (§5.3). The document currently motivates the Ordered Veil purely from the *integrability* of the GGE (Bogoliubov, `S_ent=0`) — which is correct — but the *geometric* corroboration (extremal horizon ⇒ zero Hawking temperature ⇒ no thermal channel) is independent and strengthens the claim. The two readings (integrable-relic and extremal-horizon-zero-T) are the same physics seen from the spectral and the causal sides, exactly as the document does so well elsewhere. Recommend folding in (§V.2).

> Disambiguation guard the document already gets right and should keep: `τ_fold = 0.190` (the extremal horizon / boundary) vs `τ ~ 0.22` (the physical epoch, just *inside* the surviving region). The document's §5.2/§6.2 hold this distinction; the reading-convention box at the top (`τ_fold = 0.190` operating point) is consistent with canon.

---

## III. Causal-structure check — claim-by-claim

| §6.2 claim (as written) | Canonical status | Verdict |
|:--|:--|:--|
| Acoustic white hole; pre/post-fold causally disconnected | PROVEN (S85, acoustic white hole causal-disconnect FORMALIZED) | **CONFIRMED** |
| `Mach = v_transit/c_fabric = 13.75`, `c_fabric = 209.97 M_KK` | `Mach_max = 13.75` canonical; `c_fabric = 209.97368021` canonical | **CONFIRMED** (number-exact) |
| ENTRY horizon at `τ ≈ 0.2195`, controlled by `a₂` (kinematic) | Censorship `tau_turn(fold) = 0.218` (CENSORSHIP-49); entry-barrier reading is canonical | **CONFIRMED** (entry side) |
| EXIT horizon at `τ ∼ 0.16`, controlled by `a₄` (BCS) — i.e. a **second horizon** | Canonical S74 result is "Entry Horizon, **OPEN** Exit"; the BCS exit at `τ≈0.235` is a *window edge*, not a sonic horizon symmetric to entry | **CONFLICT — see III.A** |
| Symmetric "supersonic white-hole interior" between two horizons | Asymmetric one-directional acoustic disconnect (S74) | **CONFLICT — see III.A** |
| (sector dependence of the white hole) | [T3] PERMANENT: scalar sees white hole, tensor (β_T=0) crosses freely | **OMITTED — see III.B** |
| Causal flow `subsonic → supersonic → subsonic` | Consistent with one-directional acoustic disconnect IF read along increasing τ | **CONFIRMED with caveat** (III.A) |
| Resolves horizon problem as acoustic white hole, not inflationary stretching | Canonical | **CONFIRMED** |

### III.A — The two-horizon symmetry conflicts with the canonical asymmetric fold

The document's §6.2 table is built as a *symmetric* pair: an entry horizon (`a₂`, τ≈0.2195) and an exit horizon (`a₄`, τ∼0.16) bracketing a white-hole interior. The canonical causal-structure result is **asymmetric**:

> *S74 open-channel "Asymmetric Fold: Entry Horizon, Open Exit"; `s74_s70_s72_exit_horizon_audit`, AUDIT-74. The supersonic transit creates a* **one-directional** *acoustic causal disconnect: ingoing null rays toward the fold stall (the entry horizon, the white-hole surface), while the exit toward the post-transit GGE epoch is* **open**.

This is the defining property of a **white** hole, not a black hole. A white hole has one horizon you cannot enter from outside (ingoing rays stall) and an interior from which everything is expelled (the exit is open by construction — that is what "white" means). The document's own §6.2 prose half-says this ("the horizon determines what escapes, not what is produced"), but the *table* contradicts it by giving the exit a horizon symmetric to the entry. The acoustic metric reading is unambiguous: there is **one** sonic horizon (the white-hole surface, the entry barrier near τ≈0.22 for the trajectory running *toward* decreasing τ / ingoing rays); the post-fold side is the open expulsion region where the GGE relic streams out.

Two distinct objects are being conflated under "exit horizon" in the table:
- The **BCS window edge** at `τ ≈ 0.235` (the upper boundary of the BCS condensation window `[0.143, 0.235]`, my Diagram G) — this is a *thermodynamic* boundary (where the gap closes / condensate ceases), not a sonic horizon.
- A genuine *second sonic horizon* at τ∼0.16 — which the canonical asymmetric-fold result says **does not exist as a causal twin of the entry horizon**; the exit is open.

**Recommendation (§V.3): redraw §6.2 as an asymmetric white hole.** Keep the entry horizon (τ≈0.22, `a₂`-controlled, kinematic, `T_H ≈ 72.8 M_KK`); replace "EXIT horizon τ∼0.16 controlled by a₄" with "**open exit** / expulsion region; the BCS window edge at τ≈0.235 and the decoherence-regulation scale at τ∼0.16 are *thermodynamic* features inside the open region, not a second sonic horizon." This is not a downgrade — an asymmetric white hole is the *correct and more interesting* object, and it is what the framework's own causal-disconnect theorem proves.

A subsidiary causal-ordering note: the table lists EXIT at τ∼0.16 (*lower* τ) and ENTRY at τ≈0.22 (*higher* τ), while the physical trajectory runs from genesis (τ=0) *up* through the fold to the physical epoch (τ~0.22). For ingoing null rays (the ones that define the white-hole surface), "entry" is at the higher-τ barrier the rays cannot penetrate going *down* toward the fold — which is internally consistent with the table's τ-values — but the document never states the ray direction, so a reader cannot reconstruct the causal orientation. State it explicitly (a one-line "ingoing rays run toward decreasing τ" fixes it).

### III.B — The white hole is sector-dependent; §6.2 must say so

This is, from my field, the **single most important omission** in the document. By [T3] Scalar-Tensor Kasparov Decoupling (atlas-07 PERMANENT, Exact, S63; `U_total = 1_M ⊗ U_K ⟹ β_T = 0 exactly at linear order`), there are **two causal structures**, not one:

- **Scalar sector** sees the **acoustic metric** `g_acoustic = g_geom·√(ρ_s/c_s)` and therefore sees the white hole — pre/post-fold causally disconnected. This is the sector that carries `A_s`, the GGE acoustic excitations, the CMB signature.
- **Tensor sector** sees the **`a₂`-emergent gravitational metric** `g_M` and has **β_T = 0 — no white hole, crosses the fold freely.**

A Penrose diagram of exflation therefore has **two null cones at every point** (my Diagram C, bi-metric). The horizon problem is resolved for the scalar sector (which is what we observe in the CMB); the tensor sector never had a horizon problem because it never had a horizon. This is not a footnote — it is *why* `r` and `n_T` (the tensor observables, falsifier #2) behave so differently from `n_s` and `A_s` (the scalar observables): they propagate on different cones. The document discusses `r = 0.033` and `n_s` at length in §7 without ever telling the reader they live on **different causal structures**, which is the geometric root of the dual-pathway `r` and the scheme-dependent `n_s`.

**Recommendation (§V.4): add a bi-metric sentence to §6.2 and cross-link [T3].** One sentence — "the acoustic white hole is a *scalar-sector* structure; by [T3] the tensor sector (β_T=0) crosses the fold freely on the `a₂`-emergent metric `g_M`, so exflation carries two null cones and the horizon problem is resolved for the observed scalar sector only" — closes the gap and ties §6.2 to §7's tensor/scalar split.

### III.C — Petrov/CMPP framing (not in the document, but should be available)

The document never states the algebraic (Petrov/CMPP) type of the emergent spacetime, which is fine for a capstone — but if a future revision adds a causal-structure box, the canonical content is:

- **CMPP type of the emergent 4D Lorentzian spacetime** (the causally meaningful one): **static `τ̇=0` → Type D at all τ; dynamic `τ̇>0` → Type G; post-freeze → Type D restored.** This is `S84-W8B-95-CMPP-PETROV-TYPE-INVARIANCE` (PASS, PERMANENT), a *type-invariance theorem* on a dense 171-point grid (S85 W6-2): the type does not flow within either branch — it is a structural invariant of the product geometry (WAND-in-the-flat-factor).
- **Do NOT cite the 8D Riemannian fiber Petrov type as the causal type.** The bare-fiber classification (atlas-07 A3: Type D at τ=0 Einstein manifold, algebraically general at τ>0) is a *separate statement about the internal geometry*, not the causal type of the spacetime. Applying the Lorentzian CMPP scheme to the Euclidean fiber is a category error that artificially produces Type II (the corrected S49 `CMPP-TRANSITION-49` artifact). My MEMORY currently abbreviates this as "8D Type II all tau," which is the *Riemannian artifact*; the *causal* type is the a₂-reduced D/G. I note this so the document does not inherit the abbreviation.

The transit signature `D → G → D` is itself a clean causal statement: the spacetime is algebraically special (Type D, two double principal null directions, a "static-like" causal structure) before and after transit, and algebraically general (Type G, no special null alignment) *only during* the diabatic sweep. That is the algebraic fingerprint of "transit, not equilibrium," and it is independent corroboration of §5.1's monotone-ramp picture.

---

## IV. Structural Implications

**The document's honest-gap discipline is its greatest strength and I want to defend it from one direction.** §6.3 ("there is no derived FRW scale factor `a(t)`") will read to some as the framework's weakness. From my domain it is the opposite: it is the framework correctly identifying which of its objects is **fundamental** (the substrate spectral triple) and which is **emergent and not-yet-derived** (the 4D metric `g_M`, hence `a(t)`). A geometer reads §6.3 as: *the causal structure of modulus space is derived (E7 monotone clock, COSMIC-CENSORSHIP-49, the acoustic white hole), but the map from modulus-space causal structure to 4D-spacetime causal structure is the open bridge.* That is a precise, bounded, well-posed gap — exactly the kind of gap a singularity theorem leaves open before the global-hyperbolicity hypotheses are checked. The §6.3 phrasing "right about the fundamental level, wrong about the effective level — both must be said" is the correct epistemic stance and should not be softened.

**What the two §6.2 corrections do to the constraint map.** Neither correction changes a verdict. Both *tighten* the causal-structure region:
- The asymmetric-fold correction (III.A) eliminates a spurious "second horizon" object from the framework's causal vocabulary, replacing it with the canonical one-horizon white hole. This removes a potential source of downstream confusion (a future agent building on a "two-horizon" reading would derive wrong things about what escapes the interior).
- The sector-dependence addition (III.B) makes explicit that the framework has been carrying **two causal structures** all along (the bi-metric is in my Diagram C and in [T3]), which the capstone had implicitly collapsed to one. Surfacing this is necessary for any future treatment of why scalar and tensor observables diverge.

**On the `a(t)` bridge and my domain's contribution to closing it.** §6.3 lists the bridge as three coupled problems: (i) derived `S_SA(τ) →` 4D gravitational action, (ii) `K_pivot` paradox (C2), (iii) `M_KK⁻¹ →` seconds. From the causal side, the missing object is a **map from the modulus-space conformal structure (which IS derived) to the 4D conformal structure**. The framework already has the modulus-space Penrose diagram (Diagram B) and the 4D product diagram (Diagram A) as *separate* objects; what is undelivered is the conformal embedding relating them. This is a concrete geometric target, not a vague "derive Friedmann" — and it is the same bridge §6.3 names. I flag it as a carry-forward (§V.5) because it is genuinely my domain's piece of the load-bearing gap.

---

## V. Carry-Forward Recommendations (verbiage + computation)

These are recommendations to the document authors and to the framework. The first four are **verbiage / presentational** (fix the synthesis paragraph); the last two are **genuine computations** in my domain.

```
V.1. Restate the genesis-singularity claim as a cosmic-censorship statement
   - What: Replace "There is no t=0 singularity" (§5.2(i), §9) with the two-sided statement:
     "Genesis at τ=0 is a regular maximally-symmetric configuration (no singularity); the
     genuine curvature singularity is at τ→∞, is anisotropic (timelike in SU(2), spacelike
     in ℂ²/U(1)), and is censored — provably unreachable from the physical epoch by the
     triple-layer barrier (COSMIC-CENSORSHIP-49) below and the overshoot turnaround (τ=1.614)
     above. This is weak cosmic censorship realized in modulus space."
   - Inputs: CONFORMAL-TRANSITION-49 (PASS), COSMIC-CENSORSHIP-49 (PASS, tau_turn=0.088/0.218,
     v_crit=219), S77 overshoot (τ=1.614, 35/35 neg Hessian). No new compute.
   - Gate: none (verbiage); strengthens §5.2 / §9 honesty.
   - Effort: 30 min, editorial.

V.2. Add the extremal-horizon (κ=0, T_H=0) origin of the Ordered Veil
   - What: In §5.3 (or §6.2), state that τ_fold=0.190 is a double-root extremal Killing horizon
     (V=V'=0 ⟹ κ=0, T_H=0), and that zero Hawking temperature is the geometric corroboration of
     "the GGE relic never thermalizes" — independent of the integrability (Bogoliubov, S_ent=0)
     argument the document already gives.
   - Inputs: S85 W6-4 extremal-horizon result; Phononic-Penrose-Diagrams Disambiguation Callout 1.
     No new compute.
   - Gate: none (verbiage); adds an independent leg under the Ordered Veil.
   - Effort: 30 min, editorial.

V.3. Redraw §6.2 as an ASYMMETRIC white hole (entry horizon + open exit)
   - What: Replace the symmetric two-horizon table with the canonical asymmetric structure:
     ONE sonic entry horizon (τ≈0.22, a₂-kinematic, T_H≈72.8 M_KK); an OPEN exit / expulsion
     region (the white-hole interior streams the GGE relic out); the BCS window edge (τ≈0.235)
     and decoherence regulation (τ∼0.16) are THERMODYNAMIC features inside the open region, NOT a
     second sonic horizon. State the ingoing-null-ray direction explicitly.
   - Inputs: S74 open-channel "Entry Horizon, Open Exit"; AUDIT-74 (s74_s70_s72_exit_horizon_audit);
     BCS window [0.143, 0.235] (Diagram G). No new compute — this is a re-reading of canonical data.
   - Gate: none (verbiage); resolves the III.A conflict with canon.
   - Effort: 1 hour, editorial (table redraw + one orientation sentence).

V.4. Add the bi-metric (sector-dependent) sentence to §6.2 and cross-link [T3]
   - What: State that the acoustic white hole is a SCALAR-sector structure; by [T3]
     (β_T=0 exactly), the tensor sector crosses the fold freely on the a₂-emergent metric g_M.
     Exflation carries TWO null cones; the horizon problem is resolved for the observed scalar
     sector only. Cross-link to §7's tensor (r, n_T) vs scalar (n_s, A_s) split.
   - Inputs: [T3] atlas-07 PERMANENT (U_total = 1_M ⊗ U_K ⟹ β_T=0); Phononic-Penrose-Diagrams
     Diagram C (bi-metric). No new compute.
   - Gate: none (verbiage); closes the III.B omission, the highest-value causal-structure fix.
   - Effort: 30 min, editorial.

V.5. Compute the conformal embedding modulus-space-diagram (B) → 4D-diagram (A)
   - What: Construct the explicit conformal map relating the derived 1+1D modulus-space causal
     structure (Diagram B: genesis ℐ⁻-boundary, fold extremal horizon, τ→∞ censored singularity)
     to the 4D product-spacetime causal structure (Diagram A). This is the causal-geometry piece
     of the §6.3 a(t) / K_pivot bridge: a(t) follows once the conformal factor relating the two
     conformal structures is pinned. Output: Ω(τ) the conformal factor + the embedding map.
   - Inputs: E3 R_K(τ); a₂(τ) (a_2_FW_zeta=2776.165389); a_eff(τ)=(a₂(τ)/a₂(today))^{1/2} PROXY;
     SCALE-FACTOR-54 a(τ) from Connes distance (q: −0.97→+0.81); C2/K_pivot paradox statement.
   - Gate: NEW gate SP-CONFORMAL-EMBED — PASS if Ω(τ) reproduces a_eff(τ) to within the SCALE-
     FACTOR-54 q-range AND the embedding maps the fold extremal horizon to a 4D causal feature;
     INFO if conformal factor is derivable but a(t) normalization (M_KK⁻¹→s) remains open;
     FAIL if no consistent conformal embedding exists (would indicate the bi-metric structures
     are conformally inequivalent, a deeper obstruction).
   - Effort: 1 agent-session (geometric construction + Sage verification of Ω(τ)).

V.6. Verify the anisotropic (timelike/spacelike) character of the τ→∞ singularity and its censoring at the level of the FULL 12D metric
   - What: Confirm, on the exact 12D metric ds²₁₂ = −dt² + a(t)²dx₃² + g_ab(τ(t))dyᵃdyᵇ, that the
     Kretschmann scalar divergence as τ→∞ is timelike-in-SU(2) / spacelike-in-ℂ²U(1) (currently a
     fiber-only result, MEMORY §2 / CONFORMAL-TRANSITION-49), and that the censoring barrier (NEC
     along the trajectory) is computed on the 12D metric, not just the 8D fiber. This upgrades the
     genesis-singularity claim (V.1) from a fiber statement to a full-spacetime statement.
   - Inputs: 12D metric (Diagram A); E3 curvature; COSMIC-CENSORSHIP-49 NEC/WEC/DEC data;
     Jensen exponents (2,−6,4)/8.
   - Gate: NEW gate SP-12D-SINGULARITY-CENSOR — PASS if 12D Kretschmann divergence is direction-
     dependent with the SU(2)/ℂ²U(1) signature AND NEC holds along the physical trajectory up to
     the overshoot turnaround; INFO if signature confirmed but censoring is only fiber-level;
     FAIL if the 12D NEC is violated on the physical trajectory (would open a naked-singularity
     pathway — directly contradicts CONFORMAL-TRANSITION-49, so a FAIL would itself need adjudication).
   - Effort: 1 agent-session (12D curvature-invariant + energy-condition computation, Sage/torch).
```

---

## VI. Summary Table

| # | Item | Classification | Verdict / Status | Implication |
|:--|:--|:--|:--|:--|
| 1 | Single arrow `D_K → a_n → metric → measurement` held throughout | GEOMETRIC | **ENDORSED** | Correct inversion of the container picture; §0 is the document's strongest geometric statement |
| 2 | "No t=0 singularity" (§5.2, §9) | GEOMETRIC | **CORRECT but one-sided** | Recommend restating as cosmic censorship: genuine singularity at τ→∞, anisotropic, censored (V.1) |
| 3 | Transit-not-slow-roll from `e^{−S}` monotone, no interior saddle (§1.3a, §5.1) | GEOMETRIC/PHONONIC | **ENDORSED** | No static region in modulus space; forced trajectory; matches D→G→D Petrov fingerprint |
| 4 | τ_fold=0.190 horizon class (extremal, κ=0, T_H=0) | GEOMETRIC | **OMITTED — add (V.2)** | Zero Hawking temperature is an independent geometric leg under the Ordered Veil |
| 5 | §6.2 ENTRY/EXIT two-horizon symmetric table | GEOMETRIC | **CONFLICT with S74 canon (III.A)** | Canonical structure is asymmetric: one entry horizon + OPEN exit; redraw (V.3) |
| 6 | §6.2 sector-dependence of the white hole | GEOMETRIC | **OMITTED — highest-value fix (III.B)** | [T3] PERMANENT: scalar sees white hole, tensor crosses freely; two null cones; add sentence (V.4) |
| 7 | CMPP causal type (D/G/D) vs 8D Riemannian fiber type | GEOMETRIC | **CONFIRMED canon; not in doc** | If a causal box is added, cite a₂-reduced D/G (PERMANENT), never the Euclidean-fiber Type II artifact (III.C) |
| 8 | §6.3 honest `a(t)` gap as a category statement | GEOMETRIC | **ENDORSED — do not soften** | Correctly identifies fundamental (substrate) vs emergent-not-derived (g_M); well-posed bridge |
| 9 | `Mach_max=13.75`, `c_fabric=209.97`, `w0_FW=−0.918` | (numbers) | **CONFIRMED canonical** | Document's causal/EoS numbers match the knowledge MCP exactly |
| 10 | Verification-ledger flag: `M_KK`, `w0_FW` lack PROVENANCE | (hygiene) | **CONFIRMED accurate** | Both confirmed PROVENANCE-less in the MCP; the document's own flag is correct |

---

### Closing note (substrate-first)

Every correction above runs the framework's own arrow. The causal structure of exflation is not a stage the equation plays on — it is *read off* the spectrum: the white hole is `a_acoustic` from `√(ρ_s/c_s)`; the tensor cone is `g_M` from `a₂`; the extremal horizon at the fold is the double-root of the spectral-action driver; the censored singularity at τ→∞ is the divergence of `R_K(τ)` in the Jensen exponents. The document gets the direction right. My two flagged defects (the symmetric-vs-asymmetric fold, and the missing sector-dependence) are places where the *causal-structure read-off* was abbreviated, not inverted — and both are one-paragraph fixes that make the global picture match what `D_K`'s spectrum already implies.
