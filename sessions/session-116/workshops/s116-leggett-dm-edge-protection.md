# Session 116 Workshop: landau × volovik

**Date**: 2026-06-28
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: landau (landau-condensed-matter-theorist), volovik (volovik-superfluid-universe-theorist)
**Source Documents**:
- sessions/session-116/workshops/s116-w3-disorder-closure.md
- sessions/session-116/session-116-w3-workingpaper.md
- computations/session-116/s116_gate_verdicts.txt

**Focus Topics** (adjudication: is the registered `11.97·Δ_BCS` Leggett DM anchor below-edge kinematically protected, or above-edge integrability-protected? The W3 protection-magnitude-exclusion theorem's binding inequality eq(15c) caps protected modes at `5.64·Δ_BCS`, yet the surviving anchor is `11.97·Δ_BCS` = `2.12×` ABOVE the `2Δ_BCS` edge):
1. (a) Does `m_LeggettDM = 5.5571 M_KK` satisfy eq(15c) `m < 5.64·Δ_BCS`? With intra-band `(ρ_s=7.962, edge=2Δ_BCS)` it does NOT (`x_G=2.12`). Is that the correct `(stiffness, edge)` convention for an INTER-band mode, or does the inter-band sector carry a distinct `ρ_s^⊥` / edge?
2. (b) Is the S48 below-edge theorem (`ω_L1=0.070 M_KK`, `proven_1792`) being mis-inherited by the 79×-heavier S70 DM anchor (`11.97·Δ_BCS`)? Distinct objects with distinct survival arguments?
3. (c) Which protection mechanism does framework DM-survival rest on for `5.5571 M_KK` — kinematic below-edge under an inter-band `ρ_s^⊥` (Reading B, landau) OR integrability/GGE/CPT + `Γ_grav < H_0` (Reading A, volovik, the canonical note)?
4. (d) Does the protection-magnitude-exclusion theorem survive — is "single-gap ⇒ protected mode ≤ O(10·Δ_BCS)" airtight when (15c) caps at `5.64·Δ_BCS` yet the surviving anchor is `11.97·Δ_BCS`? Re-scope/re-derive (15c)→(15d) for the inter-band mode; reconcile atlas-07's [NEW S48] below-pair-breaking inheritance.

---

## Round 1 — landau: Opening Analysis

### L1: (a) The (stiffness, edge) convention for the inter-band Leggett mode

**Key finding.** Equation (15c) is assembled entirely from **intra-band (0,0) quantities** — the overall-phase stiffness `ρ_s = ρ_{s,C2} = 7.962` and the intra-band pair-breaking edge `2Δ_BCS = 0.9285` M_KK. The surviving Tier-2 anchor is, by WS-1's own verdict (s116-w3-disorder-closure.md Tier 2), an **inter-band** object — the clean Leggett `J_⊥`, an off-(0,0) `D_K` spectral functional. An inter-band mode does not live on the intra-band continuum: it carries its own relative-phase stiffness `ρ_s^⊥` AND — decisively — its own continuum edge `E_edge^⊥`, set by the fiber gap, not the BCS gap. Correcting the **edge** alone (holding `ρ_s` fixed) already moves the anchor from `x_G = 2.12` (above the intra-band edge) to `x_G^⊥ = 0.90` (below the inter-band edge). The 2.12× "exclusion" is an **intra-band edge mis-applied to an inter-band mode** — the same category error WS-1 corrected on the *operator* side (`H_φ` (0,0)-shadow → full Peter-Weyl) but left uncorrected on the *edge* side.

**Substrate-first setup.** The substrate IS the spectral triple `(A_K, H_K, D_K)`. Two condensate sectors enter the DM channel:
- **Band 1** — the (0,0) Peter-Weyl singlet BCS condensate, gap `Δ_BCS`, phase `φ_1`.
- **Band 2** — the lowest fiber sector, quasiparticle gap `|λ|_fib` (Lichnerowicz-floored), phase `φ_2`.

The MgB₂ / Fe-pnictide two-band Leggett mode is the **laboratory analog** OF this substrate structure, not its origin. The two-band Ginzburg–Landau phase functional on the substrate is

$$F[\phi_1,\phi_2] = \tfrac12\rho_1(\nabla\phi_1)^2 + \tfrac12\rho_2(\nabla\phi_2)^2 + \tfrac12\chi_1\dot\phi_1^2 + \tfrac12\chi_2\dot\phi_2^2 \;-\; J_\perp\cos(\phi_1-\phi_2). \tag{1}$$

Diagonalize into overall and relative phases (the substitution that decouples the `φ̇_+φ̇_-` cross term):

$$\phi_+ = \frac{\chi_1\phi_1+\chi_2\phi_2}{\chi_1+\chi_2}, \qquad \phi_- = \phi_1-\phi_2. \tag{2}$$

- `φ_+` is the **Goldstone** of broken U(1)₇ — massless (no `φ_+` potential survives in `F`), inertia `χ_+ = χ_1+χ_2`, stiffness `ρ_+ = ρ_1+ρ_2`. This is the (0,0) overall-phase mode whose stiffness WS-1 calls `ρ_s = 7.962`.
- `φ_-` is the **Leggett mode** — gapped, because `J_⊥cos(φ_1-φ_2)` is an EXPLICIT relative-phase potential (not a flat Goldstone direction). Expanding `-J_⊥cosφ_- ≈ const + ½J_⊥φ_-²` gives restoring curvature `J_⊥`, with the **reduced** inertia `χ_- = χ_1χ_2/(χ_1+χ_2)` and **reduced** stiffness `ρ_-^⊥ = ρ_1ρ_2/(ρ_1+ρ_2)`.

The Leggett gap and the registered anchor are

$$\omega_{\rm Leg}^2 = J_\perp/\chi_-, \qquad m_{\rm Leggett}^2 \propto J_\perp \quad(\text{restoring force, FIRST order}). \tag{3}$$

So `m_Leggett = 11.97 Δ_BCS = 5.5571` M_KK IS the first-order restoring scale `√J_⊥` (WS-1 Tier 2; S70 LEGGETT-MOMENT-70). The framework converts a restoring scale `m` to a physical frequency by `ω = m/√ρ` where `ρ` is **the inertia of THAT mode**. For the Goldstone `φ_+` the inertia is `ρ_s = 7.962`; for the Leggett `φ_-` the inertia is `ρ_s^⊥` (the reduced `χ_-`, NOT `χ_+`). **Equation (15c) used `ρ_s = 7.962`, the overall-phase inertia, for a relative-phase mode** — the stiffness category error.

**The EDGE is the decisive, `ρ_s^⊥`-independent correction.** A collective phase mode is below-edge-protected when it cannot decay into the **two-quasiparticle continuum it actually couples to**. Equation (15c) used `2Δ_BCS` — the threshold to break one **intra-(0,0)** pair into two (0,0) BdG quasiparticles. But the Leggett mode `φ_-` carries inter-sector ((0,0)↔fiber) character, and **`D_K` is block-diagonal in Peter-Weyl (wall #2, S22b: inter-sector matrix elements ≡ 0 identically)**. The matrix element coupling `φ_-` to a pure (0,0) quasiparticle pair therefore **vanishes identically** — the intra-band continuum is decoupled from the inter-band mode by a PERMANENT wall. The lowest continuum `φ_-` can couple to requires at least one **fiber** quasiparticle:

$$E_{\rm edge}^\perp \;=\; \Delta_{\rm BCS} + |\lambda|_{\rm fib} \;\ge\; \Delta_{\rm BCS} + \sqrt3 \;=\; 0.4643 + 1.7321 \;=\; 2.1963\ \text{M\_KK}, \tag{4}$$

using the Lichnerowicz floor `|λ(D_K)| ≥ √3 = 1.73` (collab eq 8 / WS-1 eq 15b — the framework's registered fiber-gap floor, the SAME `|λ| ≥ √3` WS-1 used to assert "every nonzero fiber mode is above the edge"). The pure-fiber pair channel `2√3 = 3.46` is higher; (4) is the LOWEST inter-band channel.

**Substitution chains (the `x_G` direction claim; Sage-verified).**

*Intra-band (WS-1's number, reproduced):*
$$\omega_G = \frac{m_{\rm Leggett}}{\sqrt{\rho_s}} = \frac{5.5571}{\sqrt{7.962}} = \frac{5.5571}{2.8217} = 1.9694\ \text{M\_KK}; \quad x_G = \frac{\omega_G}{2\Delta_{\rm BCS}} = \frac{1.9694}{0.9285} = 2.121 > 1. \tag{5}$$
Above the INTRA-band edge — correct as computed, but the **wrong edge** for an inter-band mode.

*Inter-band (Reading B, edge-corrected, SAME conservative `ρ_s` in the numerator):*
$$x_G^\perp = \frac{\omega_G}{E_{\rm edge}^\perp} = \frac{1.9694}{2.1963} = 0.897 < 1. \tag{6}$$
**Below the inter-band edge.** And `ω_G = 1.9694 < 2.1963 = E_edge^{⊥,min}` is the BINDING inequality; it holds for EVERY inter-band channel — the pure-fiber channel gives `x_G^⊥ = 1.9694/3.4641 = 0.569`, the first-sector-energy channel (`E_n(1,1) = 1.651`, collab §3 eq 1) gives `2.116 ⇒ x = 0.931`. `ω_G` sits below the ENTIRE inter-band continuum regardless of which fiber pair the mode decays into.

**Honest scoping of (6).** The numerator holds `ρ_s = 7.962` (intra-band) — I isolate the edge effect. The relative-phase inertia `ρ_s^⊥` (eq 3) is genuinely distinct (`χ_-`, reduced) and its value/direction is uncomputed: if `ρ_s^⊥ < ρ_s` (standard reduced-susceptibility two-band), `ω_G` rises and the *mixed-channel* 12% margin erodes; the *pure-fiber* channel (x=0.569, 76% margin) survives a ~3× stiffness reduction. So the robust load-bearing claim is: **the edge is the inter-band continuum (≥ 2.196, permanent-wall-grounded), and with the framework's own `ρ_s` the mode is below it.** Pinning `ρ_s^⊥` and the exact channel is the CF (L5).

**Questions for volovik.**
1. Do you accept that `D_K` block-diagonality (wall #2, S22b) forbids the inter-band Leggett mode from coupling to a pure (0,0) quasiparticle pair, so the relevant pair-breaking edge is `E_edge^⊥ ≥ Δ_BCS+√3 = 2.196`, NOT `2Δ_BCS = 0.928`?
2. If yes, the mode is below-edge **kinematically** (`x_G^⊥ = 0.90 < 1` on the framework's own frequency convention). Does that not make below-edge the PRIMARY protection, with your integrability/CPT a second layer for the residual channels — rather than the load-bearing mechanism?

### L2: (b) S48 ω_L1=0.070 vs the S70 DM anchor — mis-inheritance check

**Key finding.** The two modes ARE distinct objects (79× apart), but the S48 below-edge theorem is NOT *mis*-inherited — it GENERALIZES, with a **sector-appropriate edge**. The light mode (0.070) is below the INTRA-band edge; the heavy DM anchor (5.5571) is below the INTER-band edge (eq 4). Same below-edge *structure*, different edge per sector. The apparent "mis-inheritance" is the artifact of carrying the light mode's intra-band edge onto the heavy mode's inter-band physics — exactly the eq(15c) error of L1.

**The two modes, with their sector edges (Sage-verified):**

| Mode | Provenance | `m` (M_KK) | `m/Δ_BCS` | `ω = m/√ρ_s` | Sector | Edge | `x = ω/edge` |
|:--|:--|--:|--:|--:|:--|:--|--:|
| Light dipolar `ω_L1` | S48 `proven_1792` (atlas-07 historical 0.070) | 0.070 | 0.151 | 0.0248 | low-lying / intra-band | `2Δ_BCS = 0.928` | **0.0267 ≪ 1** |
| Heavy DM anchor | S70 LEGGETT-MOMENT-70 (`11.97·Δ_BCS`) | 5.5571 | 11.97 | 1.9694 | inter-band (off-(0,0)) | `Δ_BCS+√3 = 2.196` | **0.897 < 1** |

Substitution chain for the light mode: `ω_L1 = 0.070/√7.962 = 0.0248`; `x_L1 = 0.0248/(2Δ_BCS) = 0.0248/0.9285 = 0.0267 ≪ 1` — deeply below the intra-band edge. The S48 "below pair-breaking at ALL τ" theorem (`proven_1792`) is for THIS mode: a low-lying Leggett mode whose decay channel IS the intra-(0,0) pair continuum, so `2Δ_BCS` is its correct edge.

**The inheritance is valid with the right edge.** The atlas-07 `[NEW S48]` "the DM mode is below pair-breaking" statement is CORRECT — provided "pair-breaking" is read as the **sector-appropriate** edge: intra-band `2Δ_BCS` for the light mode, inter-band `Δ_BCS+√3` for the heavy mode. The framework drifted by (i) proving below-edge for the light mode against `2Δ_BCS`, then (ii) attaching the conclusion to "the DM mode" (the heavy 5.5571 anchor) while silently retaining the light mode's `2Δ_BCS` edge. Step (ii) is the bug; the fix is not to discard the inheritance (Reading A over-corrects → integrability) but to inherit it with the heavy mode's inter-band edge (Reading B → below-edge preserved).

**Why the 79× gap is a SECTOR gap, not a contradiction.** `m_heavy/m_light = 5.5571/0.070 = 79.4`. This is NOT two values of one observable; it is two DIFFERENT collective modes living in two DIFFERENT sectors of `D_K`. The light dipolar mode is a near-(0,0) excitation (intra-band continuum at `2Δ_BCS`); the heavy DM mode is the inter-band Leggett `J_⊥` (inter-band continuum at `Δ_BCS+√3`, 2.37× higher). The 79× mass gap and the 2.37× edge gap together keep BOTH modes below their respective continua. The S48 theorem's content — "the relative-phase collective mode sits below its pair-breaking continuum" — is sector-covariant: it holds in each sector with that sector's edge.

**Questions for volovik.**
1. The S48 theorem proved below-edge "at ALL τ" for the light mode. The inter-band edge `E_edge^⊥(τ) = Δ_BCS(τ) + |λ|_fib(τ)` is τ-dependent through the Lichnerowicz floor. Does the heavy mode's below-edge property carry the same τ-robustness, or could `ω_G(τ)` cross `E_edge^⊥(τ)` at some τ off the fold? (A genuine CF — the τ-stability of `x_G^⊥ < 1`.)
2. Under Reading A, do you read the S48 light-mode theorem as simply INAPPLICABLE to the heavy anchor (so DM-survival rests on integrability instead), or do you also see a sector-covariant below-edge structure that I am pricing differently?

### L3: (c) Protection mechanism — below-edge kinematic (Reading B)

**Key finding.** DM-survival rests PRIMARILY on below-inter-band-edge KINEMATICS. The mode at `ω_G = 1.969` sits below the inter-band continuum `E_edge^⊥ ≥ 2.196` — there is **no two-quasiparticle phase space** for it to decay into. This is UNCONDITIONAL: it uses only the Lichnerowicz floor (eq 15b) and `D_K` block-diagonality (wall #2), both PERMANENT walls. It requires neither GGE integrability nor the C11-conditional `Γ_grav < H_0`.

**The decisive move is to separate the decay CHANNELS.** Reading A and Reading B are not competing for one channel — they close DIFFERENT channels:

| Channel | Process | What closes it | Conditional? |
|:--|:--|:--|:--|
| **Pair-breaking** | Leggett → 2 BdG quasiparticles | **below-inter-band-edge KINEMATICS** (`x_G^⊥ < 1`; block-diagonality + Lichnerowicz) — **Reading B** | NO (permanent walls) |
| Thermalization / annihilation | Leggett–Leggett scattering, GGE relaxation | INTEGRABILITY / CPT non-annihilation (Ordered Veil `S_ent=0`, `R_therm=5252`) — **Reading A** | NO (S95-certified) |
| Gravitational decay | Leggett → gravitons (`Γ_grav`) | `Γ_grav < H_0` (LEGGETT-GRAV-DECAY-67) — **C11** | YES (C11-conditional) |

Three channels, three protections. The DOMINANT channel — pair-breaking, the fastest if open (a strong-coupling `O(Δ)` rate) — is closed by Reading B's kinematics. Integrability (Reading A) protects the channels kinematics leaves open (many-body relaxation, which does not have a single-mode kinematic threshold). `Γ_grav < H_0` (C11) is a separate, gravitational channel — NOT a pair-breaking process at all.

**Why this ordering is forced.** Above the intra-band edge, a collective mode normally Landau-damps into a quasiparticle pair at rate `∝` the available phase space — UNLESS the pair channel is kinematically or selection-rule closed. Integrability does NOT supply that closure: GGE integrability forbids *thermalization* (a statement about the many-body relaxation of the whole occupation distribution), not single-mode *pair-decay* (a one-into-two kinematic process). So if the inter-band Leggett mode were genuinely above its own continuum edge, it would Landau-damp regardless of integrability, and the "non-annihilating DM" claim would fail. What actually closes the pair channel is the kinematic fact that `ω_G = 1.969` lies below the inter-band continuum `≥ 2.196` (no final-state phase space) PLUS block-diagonality forbidding the lower intra-band continuum. **Below-edge is load-bearing; integrability is the second line.**

**The framework's own language names the first line.** "What Holds" line 443 (s116-w3-disorder-closure.md): *"the Lichnerowicz floor `|λ| ≥ √3` keeps every nonzero fiber mode above the [edge], the protected DM mode below it."* Read literally with the INTER-band edge, this is EXACTLY Reading B: the fiber continuum sits at `≥ √3` (so the inter-band edge is high), and the DM mode `ω_G = 1.969` sits below it (`x_G^⊥ = 0.897`). The line is correct; only WS-1's eq(15c) (which compared the same `ω_G` to the *intra-band* `2Δ_BCS`) contradicted it. Reading B removes the contradiction by aligning the edge in eq(15c) with the edge in line 443 — both inter-band.

**Questions for volovik.**
1. Does Reading A's integrability close the PAIR-BREAKING channel, or only thermalization/annihilation? If it forbids many-body relaxation but not single-mode pair-decay, then above the intra-band edge the mode would damp into a (0,0) pair UNLESS that channel is kinematically/selection-rule forbidden — which is Reading B's block-diagonality + Lichnerowicz argument. Isn't Reading B then doing the load-bearing work even on your reading?
2. Do you agree the three channels (pair-breaking / thermalization / gravitational) are distinct, with distinct protections — so that "below-edge vs integrability" is a layering question (which channel each closes), not an either/or about one channel?

### L4: (d) Survival of the protection-magnitude-exclusion theorem; (15c)→(15d)

**Key finding.** The protection-magnitude-exclusion theorem **SURVIVES, re-scoped and SHARPENED.** Equation (15c) `m < 2Δ_BCS√ρ_s = 5.64·Δ_BCS` is the INTRA-band specialization. The inter-band version replaces BOTH intra-band quantities with their inter-band counterparts:

$$\boxed{\;\text{protected}^\perp \iff \omega_G < E_{\rm edge}^\perp \iff m_{\rm Leggett} < E_{\rm edge}^\perp\,\sqrt{\rho_s^\perp}\;}\tag{15d}$$

Evaluate (15d) edge-only (`ρ_s^⊥ = ρ_s = 7.962`, isolating the edge effect; Sage-verified):

$$m_{\rm ceiling}^\perp = E_{\rm edge}^\perp\sqrt{\rho_s} = 2.1963\times 2.8217 = 6.197\ \text{M\_KK} = 13.35\,\Delta_{\rm BCS}. \tag{7}$$

The anchor `m_Leggett = 11.97·Δ_BCS` sits **below** this inter-band ceiling (`11.97 < 13.35`, margin 1.12). The pure-fiber-pair edge gives `m_ceiling^⊥ = 3.4641×2.8217 = 9.775 M_KK = 21.06·Δ_BCS` (margin 1.76).

**The theorem is not broken — it was UNDER-scoped.** WS-1's prose repeatedly said "single-gap condensate cannot carry a protected mode above **O(10·Δ_BCS)**" (eq 15a–15d narrative), yet its binding inequality eq(15c) gave the much tighter `5.64·Δ_BCS`. The gap between the prose ("O(10)") and the inequality ("5.64") IS the missing edge correction: the prose intuition was tracking the *inter-band* ceiling (13–21·Δ_BCS, genuinely O(10)), while the inequality used the *intra-band* edge (`2Δ_BCS`) and so came out a factor 2.4–3.7 too tight. Equation (15d) reconciles them: the protection ceiling is **SECTOR-INDEXED** —

$$\text{intra-band: } m \lesssim 2\Delta_{\rm BCS}\sqrt{\rho_s} = 5.64\,\Delta_{\rm BCS}; \qquad \text{inter-band: } m \lesssim (\Delta_{\rm BCS}+\sqrt3)\sqrt{\rho_s} = 13.35\,\Delta_{\rm BCS}. \tag{8}$$

The anchor at `11.97·Δ_BCS` is the heaviest object the INTER-band sector can protect, sitting just under its ceiling. It was excluded by (15c) only because (15c) is the wrong-sector inequality.

**The 170× exclusion is UNTOUCHED — Reading B does NOT reopen Tier 3.** The structure-formation target is `m_target = 170·Δ_BCS = 78.92 M_KK`. Even against the most generous (pure-fiber) inter-band ceiling `21.06·Δ_BCS`:

$$\frac{m_{\rm target}}{m_{\rm ceiling}^{\perp,\rm pure}} = \frac{170}{21.06} = 8.07 \gg 1. \tag{9}$$

`170 ≫ 21`, so the 170× target remains above even the inter-band protection ceiling by 8×, at `x_target = 30.12` above the edge (WS-1 R2 eq 14). Reading B RELOCATES the surviving Tier-2 anchor (to below the inter-band edge); it does not lift the Tier-3 target. The WS-1 conclusion "170× re-typed off the mass axis" stands intact — this workshop sharpens the protection *ceiling* (5.64 → 13–21·Δ_BCS), not the *target*.

**atlas-07 `[NEW S48]` reconciliation (capstone-hygiene).** The below-pair-breaking inheritance is CORRECT once edge-tagged. The fix is a one-line scope annotation, not a retraction:
- BEFORE (drift): "DM mode below pair-breaking edge `2Δ_BCS`" — FALSE for the heavy anchor (`x_G = 2.12 > 1`).
- AFTER (Reading B): "DM mode below the **inter-band** continuum edge `E_edge^⊥ ≥ Δ_BCS+√3 = 2.196 M_KK` (`x_G^⊥ = 0.897 < 1`); the `2Δ_BCS` edge applies only to the light intra-band `ω_L1` mode (S48 `proven_1792`)."

This keeps atlas-07's confidence equal to the register (the in-graph below-edge STRUCTURE is firm; the VALUE `11.97·Δ_BCS` carries the C11 tag, LEGGETT-GRAV-DECAY-67) and removes the internal contradiction WS-1's eq(15c) introduced.

**Substitution chain (ceiling > anchor; the binding direction claim):**
- Step 1: `E_edge^⊥ = Δ_BCS + |λ|_fib = 0.4643 + 1.7321 = 2.1963` M_KK  [eq 4; block-diagonality + Lichnerowicz]
- Step 2: `m_ceiling^⊥ = E_edge^⊥ · √ρ_s = 2.1963 × 2.8217 = 6.197` M_KK  [eq 15d, edge-only]
- Step 3: `m_ceiling^⊥ / Δ_BCS = 6.197 / 0.4643 = 13.35`  [in Δ_BCS units]
- Step 4: `m_Leggett = 11.97 Δ_BCS`; `11.97 < 13.35` ⇒ anchor BELOW the inter-band ceiling ✓
- Step 5: `m_target = 170 Δ_BCS`; `170 / 21.06 = 8.07 > 1` ⇒ target ABOVE even the pure-fiber ceiling ✓
- Conclusion: theorem SURVIVES; anchor protected (below inter-band ceiling), target excluded (above it). The single proposition `m_protected ≲ E_edge^⊥√ρ_s` holds with the sector-correct edge.

**Questions for volovik.**
1. Under Reading A (above-edge integrability), what is the protection-magnitude CEILING? If integrability protects arbitrarily heavy modes (no kinematic ceiling), why does the registered anchor sit at `11.97·Δ_BCS` — just under the inter-band kinematic ceiling `13.35·Δ_BCS` (eq 7) — rather than anywhere? Reading B PREDICTS a ceiling and the anchor's proximity to it; Reading A predicts no kinematic ceiling. Is the anchor's location evidence the edge is load-bearing?
2. Do you agree (15d) RESTORES WS-1's own "O(10·Δ_BCS)" prose (which eq 15c contradicted at 5.64), so the theorem is strengthened, not weakened, by the inter-band re-scoping?

### L5: Cross-Cutting Observations

**1 — The WS-1 ↔ WS-2 parallelism (the residual intra-band contamination).** WS-1 corrected the OPERATOR: the DM mode is inter-band, an off-(0,0) `D_K` functional, NOT an eigenvalue of the (0,0)-shadow `H_φ` (`‖H_φ‖^{1/2} = 2.81 < 5.56`, WS-1 R2). But WS-1's own eq(15c) still carries the INTRA-band **edge** (`2Δ_BCS`) and INTRA-band **stiffness** (`ρ_s = 7.962`). The inter-band correction is HALF-DONE: operator fixed, edge/stiffness not. The eq(15c) "exclusion" (`x_G = 2.12`) is the LAST piece of intra-band contamination in WS-1's verdict — and it is precisely the piece that makes the verdict read self-contradictory: "DM mass graph-anchored, below-edge protected" (line 443) AND "x_G = 2.12, above the edge" (the eq-15c chain). The two cannot both be true under one edge. Reading B resolves it by completing the inter-band correction on the edge side.

**2 — The theorem is STRONGER, not weaker.** "One wall, four projections" (15a–15d) becomes "one wall, four projections, with a **sector-indexed** protection ceiling" (eq 8): intra-band modes capped at `5.64·Δ_BCS`, inter-band modes at `E_edge^⊥√ρ_s ≈ 13–21·Δ_BCS`. The anchor at `11.97·Δ_BCS` lands inside the inter-band band. This is a sharper theorem — the ceiling is not a single number but a function of the mode's sector edge — and it RECONCILES WS-1's prose ("O(10·Δ_BCS)") with its inequality (which had said 5.64).

**3 — 170× untouched; consistency with WS-1 Tier 3.** Reading B relocates the Tier-2 anchor below the inter-band edge; it does not lift the Tier-3 target (`170 ≫ 21·Δ_BCS`, eq 9). The two readings are consistent: the surviving anchor is below the inter-band edge; the 170× target is far above even the inter-band ceiling. I am NOT reopening 170×; I am fixing the protection *mechanism* of the surviving Tier-2 anchor — which WS-1 left in self-contradiction.

**4 — Honest caveats → the CF.**
- (i) *The mixed-channel edge gives a slim margin.* `Δ_BCS+√3 = 2.196` ⇒ `x_G^⊥ = 0.897` (12% below); robust to the pure-fiber edge (`x = 0.569`, 76% below) and to `ρ_s^⊥ ≥ ρ_s`, but the tightest reading is marginal.
- (ii) *`ρ_s^⊥` is uncomputed and possibly adverse.* The relative-phase inertia `χ_-` is the REDUCED susceptibility (eq 3); if `ρ_s^⊥ < ρ_s`, `ω_G` rises and the mixed-channel margin erodes. The pure-fiber channel survives a ~3× reduction (`ρ_s^⊥ ≳ 2.58` keeps `x < 1`); below that, the result is genuinely at risk. Direction MUST be computed, not assumed.
- (iii) *CF — `S117-LEGGETT-EDGE-AND-STIFFNESS`* (extends the WS-1 companion `S117-LEGGETT-COLLECTIVE-CEILING`): diagonalize the inter-band pair-transfer at `L_max=10`, and read DIRECTLY (not via the `m/√ρ_s` proxy) the three quantities the analytic argument leaves open — the Leggett gap `ω_Leg`, the relative-phase stiffness `ρ_s^⊥`, and the lowest two-quasiparticle continuum edge `E_edge^⊥` (which channel: mixed `Δ_BCS+√3` or pure-fiber `2√3`). Gate: `[SIGN]` on `(ω_Leg − E_edge^⊥)`; PASS = `ω_Leg < E_edge^⊥` (below-edge confirmed directly), FAIL = above-edge (Reading A's integrability is then load-bearing). This is the gate that adjudicates B vs A on the substrate, not by convention.

**5 — The deepest convention question (a B-vs-A discriminator, not resolved here).** Reading B's below-edge result is conditional on the framework's `ω = m/√ρ_s` frequency convention — the convention eq(15c) ITSELF uses, and which WS-1 applies to BOTH the light and heavy modes. IF instead the registered `5.5571 M_KK` is the physical rest energy directly (the DM-mass-IS-ℏω-at-k=0 convention), then `ω_Leg = 5.5571` and even the inter-band edge gives `x = 5.557/2.196 = 2.53 > 1` (above) — and THEN Reading A's integrability is required. So "is `11.97·Δ_BCS` a restoring scale `√J_⊥` (÷√ρ_s pending) or a frequency (done)?" is itself the load-bearing discriminator between B and A. I defend B in the convention eq(15c) poses (restoring-scale, ÷√ρ_s); the CF in (4iii) reads `ω_Leg` directly and settles which convention the substrate realizes.

**6 — Substrate framing.** The "two bands" are substrate sectors (Peter-Weyl (0,0) + fiber), not laboratory bands; the inter-band edge IS the substrate's fiber-gap continuum (Lichnerowicz `√3`). The MgB₂/Fe-pnictide Leggett mode is the laboratory ANALOG; the substrate inter-band relative-phase mode is fundamental. Reading B's protection is a substrate KINEMATIC fact — block-diagonality (wall #2) forbids decay into the (0,0) continuum, Lichnerowicz lifts the fiber continuum above `ω_G` — measured IN the laboratory as a sharp (undamped), non-annihilating DM collective mode.

**Question for volovik (cross-cutting).** If we AGREE the protection is layered — kinematic below-inter-band-edge FIRST (unconditional), integrability/CPT SECOND (residual channels), `Γ_grav < H_0` THIRD (gravitational, C11) — then the verdict is not "Reading A XOR Reading B" but "B is the primary/unconditional layer for the dominant (pair-breaking) channel; A is the secondary layer; both hold." Do you accept the layered reading, or do you hold that integrability is load-bearing for the PAIR-BREAKING channel specifically — a claim that requires integrability to forbid single-mode pair-decay (stronger than thermalization-protection), which I do not think the GGE supplies?

---

## Round 1 — volovik: Response & Cross-Synthesis

### Part 1: Response to landau's Sections

#### Re: L1 — (stiffness, edge) convention

**AGREE (narrow, real).** Your edge-side category-error catch is correct and worth stating plainly: eq(15c) compared the inter-band Leggett `ω_G` to the **intra-band** pair-breaking threshold `2Δ_BCS`, which is the edge-side twin of the operator-side error WS-1 fixed (`H_φ` (0,0)-shadow → full Peter-Weyl). A relative-phase mode `φ_- = φ_1 − φ_2` straddling the (0,0) BCS condensate and the fiber sector does not live on the pure-(0,0) two-quasiparticle continuum. That much is substrate-correct, and `D_K` block-diagonality (my own registered wall — `V_inter = 0` exact to `8.4e-15`, S60 inter-sector-zubarev; your "wall #2") does forbid a single-particle (0,0)↔fiber matrix element. Granted.

**DISAGREE / MISSED — the edge correction does not touch the SURVIVAL mechanism, and the below-edge number itself sits at the optimistic corner of an uncomputed cube.** Two issues.

*(i) Block-diagonality is a single-particle statement; it does not by itself fix the COLLECTIVE edge.* You read `V_inter = 0` as "the Leggett mode cannot decay into a (0,0) pair, so its edge is `Δ_BCS + √3`." But `V_inter = 0` is a statement about `D_K`'s single-particle spectrum — no (0,0)↔fiber **single-particle** hopping. The Leggett mode is a collective oscillation of the *pairing* (the order parameter has weight in both sectors; the relative phase is a collective coordinate). Its coupling to the two-quasiparticle continuum is a pairing-vertex quantity, not a `D_K` matrix element. The same block-diagonality that forbids the (0,0)-pair channel *also* constrains which fiber pair the relative-phase mode can source — `E_edge^⊥ = Δ_BCS + √3` is a plausible LOWEST channel but it is not *established* by `V_inter = 0`; it is precisely what your own CF (S117-LEGGETT-EDGE-AND-STIFFNESS) must read directly. I endorse that CF (Re:L5) — but until it runs, `2.196` is a conjecture, not a wall.

*(ii) Your `x_G^⊥ = 0.897` is the most generous of the available readings; two physically-motivated corrections push it ABOVE 1.* You honestly flag both; I sharpen the direction with the substitution chain.

```
Claim: the below-edge margin in (6) is fragile; the reduced relative-phase inertia inverts it.

Substitution chain (reduced-inertia direction; Sage-verified):
  Step 1: ω_G = m_Leggett / √(inertia).  You use inertia = ρ_s = 7.962 — the OVERALL-phase
          stiffness χ_+ = χ_1+χ_2 (your own L1: ρ_s is the φ_+ Goldstone inertia).
  Step 2: but the Leggett mode φ_- carries the REDUCED inertia χ_- = χ_1χ_2/(χ_1+χ_2)
          (your eq 3) — and χ_- < χ_+ = ρ_s for any positive χ_1, χ_2.   [reduced susceptibility]
  Step 3: ω_G(χ_-) = m_Leggett/√χ_-  >  m_Leggett/√ρ_s   since χ_- < ρ_s.   [smaller denominator]
  Step 4: at χ_- = ρ_s/2:  ω_G = 5.5571/√3.981 = 2.785;  x_G^⊥ = 2.785/2.196 = 1.268 > 1.
          at χ_- = ρ_s/3:  x_G^⊥ = 1.553 > 1.                                [Sage QQ-checked]
  Conclusion: the PHYSICALLY-CORRECT relative-phase inertia (reduced χ_-) puts the mixed
              channel ABOVE the edge.  Your 0.897 uses the larger overall stiffness — the
              optimistic corner.  Your pure-fiber fallback (2√3, x=0.569) survives a 3×
              reduction, but it requires the mode to source TWO fiber quasiparticles —
              a higher, more selection-rule-suppressed channel, not the lowest one.
```

And the deeper convention (your L5.5, which I take up in Re:L5): if the registered `5.5571 M_KK` is a *mass* (rest energy) rather than a restoring scale `√J_⊥`, then `ω_Leg = 5.5571` and `x^⊥ = 5.5571/2.196 = 2.53 > 1` — above edge on the inter-band edge too. So Reading B's below-edge result lives at the corner (overall stiffness ∧ mixed edge ∧ restoring-scale convention); move off any of the three and the mode is above-edge. That fragility is not fatal to your edge correction — but it is fatal to the edge correction being the LOAD-BEARING DM-survival argument (V2).

#### Re: L2 — S48 vs S70 mis-inheritance

**DISAGREE with "generalizes, not mis-inherited" — the register settles it, and it settles it against you.** Your "sector-covariant" framing is a clean idea, but it conflates a PROVEN theorem with a CONJECTURED one, and it borrows the proven one's confidence for the heavy anchor. The two objects do not merely have different masses — they have different REGISTER ENTRIES with different SURVIVAL ARGUMENTS:

| Mode | Register entry | Status | Survival argument (registered) |
|:--|:--|:--|:--|
| Light `ω_L1 = 0.070 M_KK` | atlas-07 `[NEW S48]`, theorem `proven_1792` | **Computed / proven** | "Below pair-breaking at ALL τ" — below-edge, intra-band |
| Heavy `11.97·Δ_BCS = 5.5571 M_KK` | atlas-04 `C11` (S70), `LEGGETT-MOMENT-70` | **CONDITIONAL** | `Γ_grav < H_0` (LEGGETT-GRAV-DECAY-67) + CPT non-annihilation |

(Both rows confirmed against the knowledge MCP: `proven_1792` bounds `ω_L1 = 0.070`; `C11 (NEW S70)` reads *"Conditional on (i) Γ_grav < H_0 survival (LEGGETT-GRAV-DECAY-67)"* — NOT on below-edge.)

So the register does NOT tag the heavy anchor "below pair-breaking, proven." It tags it **C11-CONDITIONAL on a gravitational-decay gate** — a Reading-A mechanism that closes a channel below-edge cannot touch. The atlas-07 `[NEW S48]` prose "the DM mode is below pair-breaking" and the W3 "What Holds" line 443 ("the protected DM mode below it") take the LIGHT mode's `proven_1792` and attach its conclusion — and its PROVEN confidence — to "the DM mode," i.e. the 79×-heavier C11 anchor whose register status is merely CONDITIONAL and rests on `Γ_grav < H_0`. **That is the mis-inheritance, precisely: a proven theorem's confidence transplanted onto an object the register classes conditional.**

**AGREE (qualified) — there may be a sector-covariant below-edge STRUCTURE, but it is a new conjecture, not S48.** Your sector-indexed reading (intra-band edge for the light mode, inter-band edge for the heavy) is a legitimate proposal for a NEW theorem. I have no objection to testing it — that is exactly what your CF S117-LEGGETT-EDGE-AND-STIFFNESS does. My objection is to LABELING it "S48 generalizes" so it inherits `proven_1792`'s standing before the CF runs. Call it `[CONJECTURE S117]`, give it the C11-conditional tag the heavy anchor actually carries, and reserve "below pair-breaking, proven_1792, at ALL τ" for the 0.070 light mode where it was actually proved. The capstone-hygiene fix (your L4 atlas-07 reconciliation) is then NOT "edge-tag the inheritance" — it is "DE-inherit: the heavy anchor's survival tag is C11/`Γ_grav < H_0`, and the proven below-edge belongs to the light mode."

**On your L2 Q1 (τ-robustness).** You ask whether `ω_G(τ) < E_edge^⊥(τ)` carries the same "at ALL τ" robustness `proven_1792` gives the light mode. It cannot inherit it — `proven_1792` proved τ-robustness for the 0.070 mode's intra-band edge, a different inequality. The heavy mode's `ω_G(τ) < E_edge^⊥(τ)` is unproven at any single τ, let alone all τ; and with the reduced-inertia correction (Re:L1) it is above the edge at the fold already on the central reading. So "at ALL τ" is exactly the proven_1792 confidence that should NOT transfer.

#### Re: L3 — protection mechanism

**AGREE (large) — your three-channel table is correct and it is the load-bearing structure of the whole adjudication.** Pair-breaking / thermalization-annihilation / gravitational decay ARE three distinct channels with three distinct closures. I accept the table as written. This is where the workshop converges.

**DISAGREE — your ORDERING ("below-edge primary/load-bearing, integrability second line") is inverted for a COSMOLOGICAL relic.** The table separates the channels correctly; it then assigns "load-bearing" to the wrong one. For dark matter — a relic whose survival criterion is *number-density persistence over a Hubble time* — the operative channels are annihilation (CPT) and gravitational decay (`Γ_grav < H_0`). Pair-breaking is the LEAST cosmologically relevant of the three, for two substrate reasons you have not priced:

*(1) Pair-breaking is number-CONSERVING — it does not deplete the relic.* The Leggett collective mode IS made of quasiparticle pairs; "Landau damping above edge" is the process `1 collective excitation → 2 BdG quasiparticles`. That is number-INCREASING in quasiparticles, and the total GGE quasiparticle number is conserved exactly: `[H_BCS, N_pair] = 0` (my registered particle-number superselection theorem, S73a — conserved at any transit speed). The relic is the conserved quasiparticle number, NOT the population of any one collective mode. So even if the Leggett mode Landau-damps in `~1/Δ`, the energy and number flow INTO the quasiparticle pair it decays into — which is still "the DM" (still cold, still CPT-neutral). The relic abundance survives; only the carrier changes (collective mode → quasiparticle pair). You have conflated *"the collective mode has a finite linewidth"* with *"the DM relic depletes."* These are different statements — the first is a substrate-internal lifetime, the second is `2→0` annihilation, which pair-breaking is NOT.

*(2) In the Ordered Veil, "Landau damping" thermalizes nothing.* Your L3 argument ("above the edge the mode Landau-damps regardless of integrability") assumes a bath to damp INTO. There is none. The GGE is diabatically frozen — `S_ent = 0`, `R_therm = 5252` (S95-certified); it never thermalizes (`t_therm ≈ 6 M_KK⁻¹` but the transit is diabatic, so the occupation freezes non-thermal). A collective mode "decaying" into the pair continuum of a *frozen integrable* GGE does not relax the system — the GGE has too many conserved charges to relax (Volovik's non-equilibrium superfluid, Papers 27/34; the quenched condensate forms a GGE that persists). So even the pair-breaking "damping" is not a true relaxation; it is occupation reshuffling among frozen modes. Integrability is not the "second line" — it is what makes the FIRST line (below-edge) cosmologically inert: with or without phase space, the frozen relic does not relax.

**MISSED — your own table answers your L3 Q1.** You ask whether integrability closes the PAIR-BREAKING channel or only thermalization. Answer: it does not NEED to close pair-breaking, because pair-breaking is number-conserving (point 1) and cosmologically inert in a frozen GGE (point 2). The DM-survival channels are annihilation and gravitational decay; integrability/CPT closes the first, `Γ_grav < H_0` the third. Below-edge closes the one channel whose closure DM survival does not require. That is the inversion.

**EMERGES — the correct layering (substrate-first):**

| Channel | Process | What closes it (cosmologically operative?) |
|:--|:--|:--|
| Annihilation | Leggett-channel quasiparticle `2→0` to vacuum | **CPT non-annihilation** — CPT-neutral inter-band coherence mode (YES — relic-depleting) |
| Thermalization | GGE relaxation to equilibrium | **GGE integrability** — Ordered Veil `S_ent=0` (YES — would erase the non-thermal relic) |
| Gravitational decay | Leggett → gravitons, `Γ_grav` | **`Γ_grav < H_0`** — C11/LEGGETT-GRAV-DECAY-67, PASS 65-OOM margin (YES — relic-depleting over Hubble) |
| Pair-breaking | Leggett collective mode → BdG pair | below-edge kinematics — **number-conserving, NOT relic-depleting; frozen-GGE-inert** (NO) |

Three of four are Reading A and all three are cosmologically operative; the fourth (below-edge) is yours and is the only one whose closure DM survival does not require.

#### Re: L4 — theorem survival / (15c)→(15d)

**AGREE — the protection-magnitude-exclusion theorem survives the re-scoping, and the 170× target is untouched.** I grant the sector-indexed ceiling structure (15d) and your eq(8): intra-band modes capped near `5.64·Δ_BCS`, inter-band modes near `13.35·Δ_BCS` (edge-only). I grant the 170× target sits above even the most generous (pure-fiber) inter-band ceiling by 8× (your eq 9). And I grant this is consistent with the prior W3 disorder-closure verdict (CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION; the 170× re-typed off the mass axis). No dissent on the theorem's survival or on 170×.

**DISAGREE — the anchor's proximity to the inter-band ceiling is NOT evidence below-edge is load-bearing (your L4 Q1).** Your sharpest point: "Reading B PREDICTS a ceiling and the anchor sits just under it (`11.97 < 13.35`); Reading A predicts no kinematic ceiling, so why does the anchor sit *there*?" The proximity is real but it does not discriminate, because **the ceiling and the mass are the SAME number for a common reason that has nothing to do with kinematic selection.** Substitution chain:

```
Claim: the 11.97 ≈ 13.35 proximity is over-determined by the shared Lichnerowicz floor √3, not by a kinematic ceiling selecting the mass.

  Step 1: the clean Leggett mass is m_Leggett = √J_⊥ at FIRST order (W3 disorder-closure R2 §DISSENT,
          jointly endorsed: m_Leggett² ∝ J_⊥, the inter-band pair-transfer — NOT a disorder/ceiling object).
  Step 2: J_⊥ is the inter-band pair-transfer between (0,0) and the fiber; its scale is the fiber gap,
          |λ|_fib ≥ √3 = 1.73 (Lichnerowicz floor, collab eq 8).             [fiber-gap-set coupling]
  Step 3: your inter-band ceiling is m_ceiling^⊥ = E_edge^⊥·√ρ_s = (Δ_BCS + √3)·√ρ_s.   [your eq 7]
  Step 4: BOTH Step-2 (the mass) and Step-3 (the ceiling) are built from the SAME √3.  The mass is
          √3-scaled by the pair-transfer; the ceiling is (Δ_BCS+√3)-scaled by the edge.  They land
          within 12% of each other because they share the Lichnerowicz origin, not because the edge
          KINEMATICALLY CAPS the mass.
  Conclusion: Reading A derives m_Leggett from J_⊥ DIRECTLY (no ceiling invoked); the proximity to your
              ceiling is a downstream CONSEQUENCE of the common √3, not evidence the ceiling is the cause.
```

So the anchor does not sit "just under the ceiling" because a kinematic ceiling selected it; it sits there because both quantities are Lichnerowicz-floored. Reading A explains the VALUE (it is `√J_⊥`, fiber-gap-set) without any ceiling. Your "why there?" has a Reading-A answer that does not invoke below-edge at all.

**MISSED — the ceiling margin you cite (1.12) is itself reduced-inertia-fragile.** Your `m_ceiling^⊥ = 13.35·Δ_BCS` uses `√ρ_s` (the overall stiffness). With the reduced relative-phase inertia `χ_- < ρ_s` (Re:L1), the ceiling `E_edge^⊥·√χ_-` DROPS, and the anchor's 1.12 margin (`11.97 < 13.35`) can close or invert — at `χ_- = ρ_s/2` the ceiling falls to `≈ 9.4·Δ_BCS < 11.97`, putting the anchor ABOVE its own re-scoped ceiling. So even granting the sector-indexed theorem, the heavy anchor's below-ceiling status is not robust; the structure survives, but the anchor's protected-vs-excluded classification under it is exactly the convention-sensitive call the CF must settle.

#### Re: L5 — Cross-Cutting

**On your point 1 (half-done correction).** AGREE as a description of WS-1's internal state — operator fixed, edge/stiffness not. But the resolution is not unique: completing the correction on the edge side (your Reading B) is ONE way to remove the contradiction; recognizing that the heavy anchor's registered survival was never below-edge in the first place (Reading A — its tag is C11/`Γ_grav < H_0`) is the OTHER. The contradiction in WS-1 is between eq(15c)'s `x_G = 2.12` and line 443's "below-edge"; Reading A removes it by reading line 443 as a mis-inherited light-mode claim (Re:L2), not by re-deriving an inter-band edge under which the heavy mode squeaks below.

**On your point 5 — this is the load-bearing discriminator, and it cuts toward Reading A.** You write: "IF the registered `5.5571 M_KK` is the physical rest energy directly (DM-mass-IS-ℏω-at-k=0), then `ω_Leg = 5.5571` and even the inter-band edge gives `x = 2.53 > 1` (above) — and THEN Reading A's integrability is required." Sage confirms your `2.53` exactly. I argue the registered quantity IS that rest energy, on three grounds:

```
Claim: m_Leggett = 5.5571 M_KK is a MASS (rest energy ℏω at k=0), not a restoring scale √J_⊥ pending ÷√ρ_s.

  (a) It is CONSUMED as a mass everywhere downstream.  frac170 = m_Leggett/(170·Δ_BCS) = 0.0704
      (W3 disorder-closure, jointly endorsed) compares m_Leggett DIRECTLY to 170·Δ_BCS — both masses,
      NO ÷√ρ_s.  The abundance leg (Ω_DM h² = 0.120) and σ_SI consume it as a rest energy.  Only the
      protection check (eq 15c / your x_G) applies ÷√ρ_s — and that is the ONE inconsistent use.
  (b) The Leggett mode frequency is already inertia-dressed.  By Leggett 1966, ω_Leg² = J_⊥/χ_-:
      the registered "mode mass" is the FREQUENCY with the inertia folded in, not the bare √J_⊥.
      Applying ÷√ρ_s to it AGAIN divides by the inertia twice.                 [double-counting]
  (c) The register names it MASS_LeggettDM / LEGGETT-MOMENT-70 — a moment/mass, used as the DM
      structure-formation and abundance scale.  A DM "mass" is a rest energy by definition.
  Conclusion: the consistent reading is Convention M (mass) throughout ⇒ ω_Leg = 5.5571 ⇒ x^⊥ = 2.53 > 1
              (above the inter-band edge) ⇒ by your OWN L5.5, Reading A's integrability is required.
```

Reading B's below-edge result requires the framework to use `m_Leggett` as a mass in `frac170`/abundance but as a restoring scale `√J_⊥` in the protection check — the same internal inconsistency you correctly diagnosed on the EDGE side, now visible on the CONVENTION side. The consistent fix is one convention for one quantity: it is a mass; it is above the edge; it survives by Reading A.

**On your point 6 (substrate framing).** AGREE entirely — the two bands are substrate sectors (Peter-Weyl (0,0) + fiber), the MgB₂/Fe-pnictide Leggett mode is the laboratory analog OF the substrate's inter-band relative-phase mode, and the Lichnerowicz `√3` IS the fiber-gap continuum. I add only the Volovik-program corollary: the substrate's DM is the *frozen GGE quasiparticle content*, and the laboratory measures it as a non-annihilating, CPT-neutral cold relic — whose persistence the lab reads off the conserved quasiparticle number (integrability), exactly as a quenched `³He` cell after a Kibble-Zurek transit retains its frozen defect/quasiparticle content not by any collective-mode below-edge condition but by the non-equilibrium freeze.

**On your cross-cutting question (do I accept the layered reading?).** PARTLY. I accept the *channels are layered* (Re:L3 — your table is correct). I REJECT the *ordering*: below-edge is not "the primary/unconditional layer for the dominant pair-breaking channel," because pair-breaking is number-conserving (`[H_BCS,N_pair]=0`) and frozen-GGE-inert, so its closure is not a DM-survival requirement at all. And I hold exactly the claim you flagged as the crux: integrability is load-bearing for DM survival not by forbidding single-mode pair-decay (it need not), but by conserving the relic NUMBER through whatever pair-decay occurs and by freezing the GGE so no relaxation happens. **I ENDORSE your CF (S117-LEGGETT-EDGE-AND-STIFFNESS) as the right adjudicator of the below-edge QUESTION** — but with the sharpening that its verdict does not settle the SURVIVAL question (V2): a PASS (below-edge confirmed) adds a bonus kinematic layer; a FAIL hands survival to Reading A; *either way* the registered survival tag is C11/`Γ_grav < H_0` + CPT, not below-edge.

### Part 2: Original Analysis

#### V1: Above-edge integrability / GGE / CPT non-annihilation protection (Reading A)

**The substrate-first survival derivation.** The DM is not a collective mode that must be kept sharp; it is the *frozen GGE quasiparticle content* of the post-transit substrate (phononic-framing: "DM = Leggett-channel GGE quasiparticle, inter-band coherence mode, CPT-neutral, non-annihilating"). Its cosmological survival is the persistence of a relic NUMBER DENSITY over a Hubble time. The flow is substrate → relic:

```
D_K spectrum (inter-band block) → Leggett-channel pairing → GGE quasiparticle occupation n(k)
   → relic number N_DM = Σ_k n(k)  → Ω_DM h²  → measured.
```

What must hold for `N_DM` to survive to z=0 is the closure of every channel that depletes `N_DM`. There are exactly three, and each has a registered Reading-A closure:

**A1 — Annihilation (`2→0` to vacuum): closed by CPT non-annihilation.** The Leggett-channel quasiparticle is CPT-neutral — its own antiparticle (the BdG/Bogoliubov structure of a `³He`-B child, BDI class, `[J,D_K]=0` CPT). A CPT-self-conjugate gauge-singlet has no `2→0` annihilation vertex to vacuum; the relic cannot self-annihilate. This is the substrate analog of Majorana-DM non-annihilation, but stronger: it is forced by the BDI/`[J,D_K]=0` structure, not assumed. *Cross-check (CDM-by-construction, S43/S44):* the same GGE quasiparticles carry `T^{0i}_4D = 0`, `w = 0`, `v_fs = 0` EXACTLY — the relic's COLDNESS and pressurelessness are ALGEBRAIC (internal-mode `T^{0i}=0`), not kinematic. The defining DM properties are Reading-A by construction.

**A2 — Thermalization (relaxation that would erase the non-thermal relic): closed by GGE integrability.** A thermalizing system would relax the frozen occupation toward equilibrium and the relic would no longer be a distinct cold component. The Ordered Veil forbids this: the transit is diabatic (Mach 13.75 supersonic through the van Hove fold), the quench freezes a non-thermal GGE, and the certification is `S_ent = 0`, `R_therm = 5252` (S95) — the entanglement entropy does not grow, the system never thermalizes. This is Volovik's non-equilibrium superfluid (Papers 27/34): a quenched condensate forms a generalized Gibbs ensemble whose extensive set of conserved charges PREVENTS relaxation. The lab realization is Kibble-Zurek freeze-out in superfluid `³He`: the post-quench quasiparticle/defect content persists because the dynamics is non-equilibrium and integrable, NOT because any mode sits below a pair-breaking edge.

**A3 — Gravitational decay (`Leggett → gravitons`): closed by `Γ_grav < H_0`.** The one decay channel open to a CPT-neutral gauge-singlet is gravitational. This is the REGISTERED survival condition of the C11 anchor (atlas-04 C11, S70: "CONDITIONAL on Γ_grav < H_0 survival, LEGGETT-GRAV-DECAY-67"). The gate PASSES: `Γ_grav/H_0 ~ 8.85e-66` (S95, 65-OOM margin), with `Γ_grav(4D) = ε²·ω_L³·Δ²/(64π·M_Pl⁴)·(ω_L/M_KK)⁴` (Eq. QA-9). Note the structure: even scaling as `ω_L⁷`, the heavy mode's gravitational decay is 65 OOM below Hubble because of the `M_Pl⁴` suppression. **This is a gap-protection — but it is the GRAVITON gap protecting the gravitational channel, NOT the BCS pair-breaking edge protecting the quasiparticle channel.** The QA-9 note's own words: "the graviton gap provides the same kinematic protection for gravitational decay that the BCS gap provides for quasiparticle decay" — two different gaps, two different channels. The heavy anchor's REGISTERED protection is the first, not the second.

**The relic is number-protected against pair-breaking too.** The fourth channel — pair-breaking (Leggett collective mode → BdG pair) — does not deplete `N_DM` because it is number-conserving: `[H_BCS, N_pair] = 0` (S73a). The "decay" `1 → 2` moves the relic from the collective-mode carrier to the quasiparticle-pair carrier; `Σ_k n(k)` is unchanged. So even ABOVE the edge (Reading A's premise), the relic abundance is intact. Below-edge would additionally preserve the COLLECTIVE-MODE IDENTITY of the carrier — a substrate-internal refinement — but not the abundance, which is already conserved.

**Net: the above-edge heavy anchor survives as DM by A1∧A2∧A3, all Reading-A, all registered, two of three independent of the edge entirely.** The survival is microscopically grounded (each closure traces to a registered theorem or PASS gate) and does not invoke below-edge kinematics at any step.

#### V2: Which protection mechanism is load-bearing for the registered DM survival

**The register answers this directly: the load-bearing mechanism is Reading A.** The heavy anchor's survival is NOT held by below-edge in the framework as it stands today. The atlas-04 `C11` entry tags `Mass_LeggettDM/Δ_BCS = 11.97` **CONDITIONAL on `Γ_grav < H_0`** (LEGGETT-GRAV-DECAY-67) — a Reading-A gate. The below-edge property appears in the heavy anchor's neighborhood ONLY via the atlas-07 `[NEW S48]` / W3-line-443 prose, which transplants the LIGHT mode's theorem (`proven_1792`, `ω_L1 = 0.070`). So:

- **Registered load-bearing survival argument for `5.5571 M_KK`**: `Γ_grav < H_0` (A3) + CPT non-annihilation (A1) + GGE integrability (A2). All Reading A.
- **Below-edge for `5.5571 M_KK`**: NOT registered as its survival argument. It is (i) a mis-inherited light-mode theorem (Re:L2), or (ii) a NEW inter-band-edge conjecture (landau's Reading B) pending the CF. Either way, supplementary, not load-bearing.

**Is the S48 below-edge theorem mis-inherited onto the heavy anchor? YES — and the mis-inheritance is diagnosable, not a matter of taste.** The test: does `proven_1792` make a statement about the 5.5571 anchor? It does not — `proven_1792` bounds `ω_L1 = 0.070 M_KK` ("below pair-breaking at ALL τ"), a 79×-lighter, intra-band object. The atlas-07 prose "the DM mode is below pair-breaking" is true of the *proven* object (0.070) and merely ASSERTED of the *registered DM anchor* (5.5571). The W3 "What Holds" line 443 ("the protected DM mode below it") then reads as if the heavy anchor inherited the light mode's proven below-edge status. It did not. This is exactly the `epistemic-discipline.md` failure mode: a proven theorem's confidence carried onto an object it does not bound.

**Why this matters beyond bookkeeping.** If below-edge were load-bearing, the heavy anchor's survival would be UNCONDITIONAL (permanent walls: Lichnerowicz + block-diagonality). But the register makes it CONDITIONAL (on `Γ_grav < H_0`). The conditionality is the tell: the framework's own bookkeeping records that the heavy anchor's survival rests on a gate that closes the gravitational channel — a channel below-edge cannot reach. A claim cannot be both "unconditionally below-edge protected" and "conditional on `Γ_grav < H_0`"; the register chose the latter. landau's Reading B, if it lands PASS at the CF, would ADD an unconditional kinematic layer — a genuine improvement — but it would not REPLACE the C11 conditionality, because below-edge does not close A1 or A3.

**The capstone-hygiene fix (Q3 / Q5 of the gate) is therefore a DE-inheritance, not an edge-retag.** The correct reconciliation of atlas-07 `[NEW S48]`:
- KEEP: "`ω_L1 = 0.070 M_KK` is below pair-breaking at ALL τ (`proven_1792`, S48)" — the light mode, unchanged.
- CORRECT: the heavy DM anchor's survival is **C11-CONDITIONAL** on `Γ_grav < H_0` (LEGGETT-GRAV-DECAY-67) + CPT non-annihilation + GGE integrability — NOT "below pair-breaking, proven." If the S117 CF returns PASS, ADD "below the inter-band edge (`[CONJECTURE S117]`, C11-conditional)" as a supplementary kinematic layer; if FAIL, the survival is wholly Reading A.

This keeps the heavy anchor's narrated confidence equal to its register status (CONDITIONAL, C11) — the capstone-hygiene requirement — and stops the proven_1792 confidence from leaking onto an object the register classes conditional.

#### V3: Questions for landau

1. **The C11 conditionality is the tell.** The register tags the heavy anchor CONDITIONAL on `Γ_grav < H_0` (LEGGETT-GRAV-DECAY-67), not on below-edge. Below-edge protection (Lichnerowicz + block-diagonality) is UNCONDITIONAL — permanent walls. If below-edge were the load-bearing survival mechanism for `5.5571 M_KK`, the anchor would be registered unconditional, not C11-conditional. Why does the framework make the heavy anchor's survival hang on a gravitational-decay gate — a channel below-edge cannot touch — unless the registered survival argument is Reading A and below-edge is (at most) a supplementary layer?

2. **Number conservation vs collective-mode linewidth.** Pair-breaking is `1 collective mode → 2 BdG quasiparticles`, number-INCREASING, and `[H_BCS, N_pair] = 0` (S73a) conserves the relic `N_DM = Σ_k n(k)` exactly. So even above the edge, the relic abundance survives in the quasiparticle sector — only the carrier changes (collective mode → pair). On what physical grounds is the COLLECTIVE-MODE linewidth (your below-edge condition) the DM-survival criterion, rather than the conserved relic NUMBER (Reading A)? Concretely: name the depletion process by which an above-edge Leggett mode would REDUCE `Σ_k n(k)` — given that pair-breaking increases it and CPT forbids `2→0`.

3. **Your own convention discriminator (L5.5), made to choose.** You concede that under the mass convention `ω_Leg = 5.5571` gives `x^⊥ = 2.53 > 1` (above), requiring Reading A. The framework uses `m_Leggett` as a MASS in `frac170 = m/(170·Δ_BCS)` and in the abundance/`σ_SI` legs (no `÷√ρ_s`), and as a restoring scale `√J_⊥` ONLY in the eq(15c) protection check. That is the same internal inconsistency you caught on the EDGE side, now on the CONVENTION side. Which is it — and if it is a mass everywhere else, by what principle is the protection check entitled to `÷√ρ_s` (dividing by the inertia a second time, when the Leggett frequency `ω_Leg² = J_⊥/χ_-` already carries it)?

4. **What does a PASS at S117-LEGGETT-EDGE-AND-STIFFNESS actually buy?** Grant your best case: the CF reads `ω_Leg < E_edge^⊥` directly (below-edge confirmed). The collective mode is then sharp. Does that change `Ω_DM h²`, the coldness (`w = 0`, CDM-by-construction), the non-annihilation (CPT), or the `Γ_grav < H_0` survival — ANY registered DM observable? If a PASS leaves all of those Reading-A-determined and unchanged, in what sense is below-edge the SURVIVAL mechanism rather than a statement about the collective mode's substrate-internal lifetime? (I am not asking you to drop the edge correction — I am asking what cosmological survival fact it is load-bearing for.)

---

## Round 2 — landau: Follow-up

### CONVERGENCE

I converge on the central claim — **DM-survival rests on Reading A, not below-edge** — and I converge because three of your moves are correct and each is genuinely new to my reasoning, not something I had already priced.

**(1) Number conservation settles V3.2 against me, decisively.** You asked me to *name the depletion process* by which an above-edge Leggett mode would reduce `N_DM = Σ_k n(k)`. I cannot, and the absence is the answer. Substitution chain, substrate-first:

- Step 1: the relic IS the conserved quasiparticle number `N_DM = Σ_k n(k)` of the frozen GGE — NOT the population of any single collective mode.
- Step 2: pair-breaking is `1 collective mode → 2 BdG quasiparticles` — number-INCREASING in quasiparticles, and `[H_BCS, N_pair] = 0` (your S73a superselection theorem) conserves the count through the process.
- Step 3: the `2→0` annihilation channel is CPT-forbidden (BDI, `[J,D_K]=0`); the only genuine depletion is gravitational (`Γ_grav < H_0`, A3).
- Step 4: therefore `dN_DM/dt |_pair-breaking = 0` exactly. The collective-mode linewidth is a *substrate-internal lifetime*, not a relic-depletion rate.

My L3 conflated "the collective mode has a finite linewidth" with "the relic depletes." You are right that the first does not imply the second: the carrier flips (collective mode → quasiparticle pair); the count does not move.

**(2) The frozen GGE has no bath (Re:L3 point 2).** My L3 premise — "above the edge the mode Landau-damps regardless of integrability" — silently assumed a thermal bath to damp into. The Ordered Veil (`S_ent = 0`, `R_therm = 5252`, S95) supplies none; "damping" is occupation reshuffling among frozen modes, not relaxation. Integrability does not have to *close* pair-breaking; it makes the pair-breaking channel cosmologically inert. That is a stronger statement than my L3 "second line" framing, and it is correct.

**(3) The C11-conditionality tell answers V3.1, and I accept it.** This is the airtight bookkeeping argument. Below-edge protection (Lichnerowicz floor + block-diagonality, wall #2) is assembled from PERMANENT walls — it is UNCONDITIONAL. The register tags the heavy anchor `C11` CONDITIONAL on `Γ_grav < H_0` (LEGGETT-GRAV-DECAY-67). A single object cannot be both "unconditionally below-edge protected" and "conditional on a gravitational-decay gate"; the framework chose the latter. If below-edge were load-bearing for survival, the anchor would carry an unconditional tag — it does not. **I withdraw the L3 claim that below-edge is "the primary/load-bearing layer" for DM survival.**

**(4) The S48 mis-inheritance lands (Re:L2 / V2).** I withdraw "S48 generalizes / sector-covariant" as a *transfer of `proven_1792`'s standing* to the heavy anchor. The proven object is `ω_L1 = 0.070 M_KK` (intra-band, `proven_1792`, below-edge at all τ); the heavy anchor (`5.5571 M_KK`) is C11-conditional via Reading A. My sector-covariant below-edge for the heavy mode is at most `[CONJECTURE S117]`, never S48-proven — and under the mass convention (below) it is in fact FALSE (above-edge). So the atlas-07 capstone-hygiene fix is your **DE-inheritance**, not my edge-retag: KEEP `proven_1792` for the 0.070 light mode; tag the heavy anchor's survival C11/`Γ_grav < H_0` + CPT + GGE; the inter-band edge result, if it ever lands, is a supplementary `[CONJECTURE S117]` layer about sharpness, not survival.

**(5) The convention (V3.3).** I concede Convention M (mass). Your (a)/(b)/(c) carry it: the abundance leg (`Ω_DM h² = 0.120`) and `σ_SI` consume `5.5571` as a *physical rest energy* (a cross-section needs a real mass), and the Leggett frequency `ω_Leg² = J_⊥/χ_-` already folds the inertia in, so the eq(15c) `÷√ρ_s` divides by the inertia a second time. The consistent reading is `ω_Leg = m_Leggett = 5.5571 M_KK` directly, giving (Sage-exact)

$$x^\perp = \frac{\omega_{\rm Leg}}{E_{\rm edge}^\perp} = \frac{5.5571}{2.19631} = 2.5302 \;>\; 1 \quad(\text{ABOVE the inter-band edge}).\tag{16}$$

My L1 `x_G^⊥ = 0.897` was the doubly-optimistic corner (restoring-scale convention ∧ overall stiffness `ρ_s` instead of the reduced `χ_-`). Your Re:L1 chains (`χ_- = ρ_s/2 → x = 1.268`; `ρ_s/3 → x = 1.553`) and the mass convention (`x = 2.53`) all push above edge; I re-verified all four Sage-exact. The corner does not hold.

### DISSENT

I yield the survival question entirely. I hold two narrow points, both with NEW argument — neither restates my R1.

**(1) Below-edge is load-bearing — for a DIFFERENT observable than survival: collective-mode SHARPNESS (linewidth).** Conceding survival to Reading A does not make the edge correction idle, and I dispute any reading of your V3.4 that prices it at zero. The Leggett mode's below-edge status is the substrate-IS determinant of its LINEWIDTH: below-edge ⇒ a sharp, undamped collective excitation; above-edge ⇒ a finite linewidth set by the available two-quasiparticle phase space. This is not private substrate bookkeeping — it is a laboratory-IN observable. In the laboratory analog (MgB₂, Fe-pnictides), the inter-band Leggett mode's Raman/IR peak WIDTH is precisely what is measured, and below-vs-above-edge is the difference between a sharp peak and a broadened one. So below-edge governs a genuine substrate→lab bridge observable (the collective-mode sharpness), ORTHOGONAL to the relic-number survival. The correct frame is not "Reading A load-bearing, Reading B supplementary"; it is "the two readings are load-bearing for DIFFERENT observables" — Reading A for `N_DM` survival, Reading B for the Leggett-mode linewidth. Pricing the edge at zero conflates the observables in the opposite direction from my L3 error.

**(2) Addressing x^⊥ = 2.53 head-on — and correcting my OWN L4 ceiling downward.** I accept 2.53 > 1 under the mass convention. But I now see that BOTH WS-1's eq(15c) AND my own L4 eq(7) carried a SPURIOUS `√ρ_s`, and removing it sharpens your V3.3 further than you stated. The kinematic pair-breaking threshold is energy-vs-energy — `ω_Leg < E_edge^⊥`, both rest energies — with NO `√ρ_s` anywhere. Substitution chain:

- Step 1: pair-breaking opens when the collective frequency exceeds the two-quasiparticle threshold: `ℏω_Leg > E_edge^⊥`. Pure energy comparison.  [kinematic threshold]
- Step 2: my L4 eq(7) wrote the ceiling as `m_ceiling^⊥ = E_edge^⊥·√ρ_s = 2.196 × 2.8217 = 6.197 M_KK = 13.35·Δ_BCS`. The `√ρ_s` is the restoring-scale conversion — it does NOT belong in a kinematic threshold.  [the spurious factor]
- Step 3: under the mass convention the sharp-mode ceiling is `E_edge^⊥` itself: `E_edge^⊥ = Δ_BCS + √3 = 2.19631 M_KK = 4.7308·Δ_BCS`.  [Sage-exact]
- Step 4: `m_Leggett / E_edge^⊥ = 11.97·Δ_BCS / 4.7308·Δ_BCS = 2.5302` ⇒ anchor decisively above the (deflated) ceiling.  [direction]

So I correct my L4 ceiling DOWN, `13.35 → 4.73·Δ_BCS`, and the anchor is unambiguously above it. This extends your stiffness catch: you said the `÷√ρ_s` double-counts the inertia; I add that the kinematic threshold carries NO `√ρ_s` at all, so the protection-magnitude ceiling for a SHARP mode is `E_edge^⊥ = 4.73·Δ_BCS`, not my inflated 13.35. The theorem (15d) survives — with a deflated, convention-pinned, `√ρ_s`-free ceiling, re-scoped to govern SHARPNESS.

Consequence for verdict-item (d): **WS-1's eq(15c) "exclusion" of the registered anchor is WITHDRAWN on every reading** — it carried two independent errors (the intra-band `2Δ_BCS` edge, my catch; and the `√ρ_s`, our joint catch). Corrected, the comparison is `ω_Leg = 5.5571` vs `E_edge^⊥ = 2.196`: the anchor is above its own sharp-mode edge, and the theorem no longer EXCLUDES it — it CHARACTERIZES it (a heavy, above-edge, finite-linewidth collective mode whose relic survives by Reading A).

### EMERGENCE

The exchange resolves the binary "Reading A XOR Reading B" into a clean **two-observable separation** on orthogonal axes:

| Observable | Question | Mechanism | Status | Edge/convention-sensitive? |
|:--|:--|:--|:--|:--|
| Relic survival `N_DM = Σ_k n(k)` | Does the abundance persist to z=0? | Reading A: CPT non-annihilation (A1) + GGE integrability (A2) + `Γ_grav < H_0` (A3) | REGISTERED (C11-conditional); number-conserving under pair-breaking | NO — below-edge irrelevant |
| Leggett-mode sharpness (linewidth) | Is the inter-band relative-phase mode sharp or broadened? | below-edge kinematics: `ω_Leg < E_edge^⊥` | `[CONJECTURE S117]`; convention-pinned; lab Leggett peak-width, modes `< 4.73·Δ_BCS` | YES — this is what the CF settles |

Both are real substrate-IS → lab-IN bridges; they answer different questions; neither is the other's "supplement." The convention/edge CF settles SHARPNESS; Reading A settles SURVIVAL regardless of the CF verdict. (Coherence check: the light `ω_L1 = 0.070 M_KK = 0.15·Δ_BCS` mode sits below its intra-band edge AND below `4.73·Δ_BCS` ⇒ sharp/`proven_1792`; the heavy anchor at `11.97·Δ_BCS` is above its inter-band edge ⇒ finite linewidth. Same energy-vs-edge test, sector-appropriate edge, no `√ρ_s` either side.)

**Two new structural consequences:**

**(E1) The carrier-identity flip re-targets the live free-streaming CF.** Under the mass convention (above-edge, finite linewidth) the registered Leggett collective mode decays into quasiparticle PAIRS on a substrate-internal timescale `~1/Δ_BCS` — fast relative to any cosmological clock. So by the structure-formation epoch the DM CARRIER is the quasiparticle-pair sector, not the collective mode. This bears directly on `CF-S117-FREESTREAM-AT-ANCHOR` (the live W3 carry-forward): the free-streaming integral's input occupation should be the DECAY-PRODUCT (pair) occupation, and coldness must be checked for the pairs. The escape is your own V1.A1: if coldness is ALGEBRAIC (`T^{0i}_4D = 0` EXACT for all internal modes, CDM-by-construction S43/S44), then `v_fs = 0` holds for the pairs too and the carrier flip is observationally invisible. So the above-edge finding does NOT threaten coldness — it re-targets the freestream CF's load-bearing input onto the algebraic-coldness theorem rather than the collective-mode occupation. (A refinement of a live gate, not a new dissent.)

**(E2) The CF `S117-LEGGETT-EDGE-AND-STIFFNESS` is re-scoped.** Its L5(4iii) gate was "`[SIGN]` on `(ω_Leg − E_edge^⊥)`; PASS = Reading B, FAIL = Reading A." That framing is now wrong: survival is Reading A on EITHER verdict. The re-scoped CF: (i) PIN the convention by reading `ω_Leg` DIRECTLY off the diagonalized relative-phase Hamiltonian (settle whether `5.5571` is the gap `ω_Leg` or the bare `√J_⊥ = √ρ_s·ω_Leg`); (ii) read `ρ_s^⊥` and `E_edge^⊥` to characterize the linewidth; (iii) report sharpness, with the explicit note that SURVIVAL is Reading A regardless. The CF adjudicates convention + sharpness; it does NOT adjudicate survival.

### QUESTIONS

Answering your V3.1–V3.4 first, then two sharper follow-ups to pin the verdict.

**A-V3.1 (the C11 tell):** Accepted in full (CONVERGENCE 3). The conditionality IS the tell; the registered survival argument is Reading A; below-edge would be unconditional and is not how the anchor is tagged. Withdrawn.

**A-V3.2 (name the depletion process):** I cannot, and concede the point is decisive (CONVERGENCE 1). Pair-breaking is number-increasing; CPT forbids `2→0`; gravitational decay is the only genuine depletion and `Γ_grav < H_0` closes it. There is no pair-breaking depletion of `Σ_k n(k)` for below-edge to prevent.

**A-V3.3 (the convention, made to choose):** Convention M (mass). `ω_Leg = 5.5571 M_KK`, `x^⊥ = 2.53 > 1` (eq 16, above edge). The eq(15c) `÷√ρ_s` is a double-counting error; I add (DISSENT 2) that the kinematic threshold carries no `√ρ_s` at all, so the sharp-mode ceiling deflates to `E_edge^⊥ = 4.73·Δ_BCS`.

**A-V3.4 (what a CF PASS buys):** It buys the collective mode's SHARPNESS — a sharp, undamped substrate-internal excitation, read in the lab as a narrow Leggett peak — and NOTHING else: not `Ω_DM h²`, not coldness (`w=0`, algebraic), not non-annihilation (CPT), not `Γ_grav < H_0`. I concede below-edge is a statement about the collective mode's substrate-internal lifetime, not the cosmological survival — which is exactly why E2 re-scopes the CF onto convention + sharpness.

**Q-landau-1 (to pin verdict-items (ii)/(iii)):** Do you accept the two-observable separation (EMERGENCE table) as the verdict's structure — survival = Reading A (registered, C11, number-conserving); sharpness = convention-pinned below-edge, a distinct lab-Leggett-linewidth observable for modes below `4.73·Δ_BCS` — rather than "Reading A wins, below-edge idle"? The distinction is what the re-scoped CF is FOR.

**Q-landau-2 (to close the freestream link):** Do you agree the carrier-identity flip (E1) re-targets `CF-S117-FREESTREAM-AT-ANCHOR` onto the quasiparticle-PAIR occupation, and that the load-bearing input keeping the flip observationally invisible is your algebraic-coldness theorem (`T^{0i}_4D = 0` EXACT, CDM-by-construction S43/S44) — so that gate should pre-register the algebraic-coldness identity as its coldness source, not the collective-mode Bogoliubov occupation?

---

## Round 2 — volovik: Cross-Synthesis

### CONVERGENCE

I accept landau's R2 convergence in full, and I record it as COMPLETE on the survival question — this workshop's central adjudication. He conceded each of V3.1–V3.4 with substrate-correct substitution chains; I re-open none of them. Three of his moves I adopt as the workshop's shared structure, and one sharpens MY own R1.

**(1) The JOINT `√ρ_s` catch — adopted; it sharpens my Re:L1 from "wrong inertia" to "no inertia."** My Re:L1 said eq(15c) used the OVERALL-phase inertia `ρ_s = 7.962` where the relative-phase mode carries the REDUCED `χ_-` (and `χ_- < ρ_s` inverts the margin). landau's DISSENT(2) goes one structural step deeper and is right: the kinematic pair-breaking threshold is energy-vs-energy — `ω_Leg < E_edge^⊥`, two rest energies — with NO `√ρ_s` on EITHER side. The Leggett gap `ω_Leg² = J_⊥/χ_-` (Leggett 1966) ALREADY folds the inertia in; it is a frequency, not a bare `√J_⊥`. So eq(15c)'s `÷√ρ_s` does not merely use the wrong inertia (my catch) — it divides by the inertia a SECOND time (his sharpening). The two compose: "wrong inertia (`χ_-` not `ρ_s`)" is the first-order error; "no inertia at all (energy-vs-energy)" is the structural correction that makes the inertia question moot for the kinematic edge. Sage-exact (this turn): `E_edge^⊥ = Δ_BCS + √3 = 2.196306 M_KK = 4.730820·Δ_BCS`; `x^⊥ = m_Leggett/E_edge^⊥ = 5.557129/2.196306 = 2.530217 > 1` — above the inter-band edge with NO `√ρ_s` anywhere.

**(2) eq(15c) "exclusion" WITHDRAWN — converged on the two-error diagnosis.** The exclusion carried TWO independent errors: the intra-band `2Δ_BCS` edge (my Re:L1 catch — block-diagonality `V_inter = 0` exact 8.4e-15 S60 forbids the (0,0)-pair channel) AND the spurious `√ρ_s` (joint). Corrected, eq(15c) is not an exclusion at all: `ω_Leg = 5.5571` vs `E_edge^⊥ = 2.196` is a CHARACTERIZATION — a heavy, above-edge, finite-linewidth collective mode. The theorem does not exclude the registered anchor; it types it.

**(3) Convention M (mass) — converged.** The registered `5.5571 M_KK` is a rest energy (the abundance leg `Ω_DM h²`, `σ_SI`, and `frac170 = m/(170·Δ_BCS)` all consume it as a mass with no `÷√ρ_s`); the Leggett frequency already carries the inertia. One convention for one quantity: it is a mass; `x^⊥ = 2.53 > 1`.

**(4) The two-observable separation is the right FRAME — survival ⊥ sharpness.** I accept landau's EMERGENCE table as the verdict's structure: survival on one axis (Reading A — registered, C11-conditional, number-conserving), a substrate-internal-lifetime/linewidth observable on the other (below-edge kinematics, a lab-Leggett-peak-width bridge). Orthogonal; neither is the other's supplement. This dissolves "Reading A XOR Reading B" cleanly. I sharpen its SECOND row in DISSENT (its domain is the LIGHT mode) and resolve a tension inside its E1 in EMERGENCE — but the FRAME is correct.

### DISSENT

I yield the survival adjudication entirely — it is Reading A, full stop. I hold two NEW points on the FORWARD framing; both sharpen rather than oppose.

**(1) Below-edge SHARPNESS is load-bearing — but its DOMAIN is the LIGHT mode, NOT the heavy DM anchor. The two-observable separation and the V2 DE-inheritance are the SAME structure.** landau's DISSENT(1) prices the edge correction at "load-bearing for sharpness." Correct that sharpness is a real substrate→lab bridge (the MgB₂/Fe-pnictide Leggett Raman/IR peak width). But apply it to the HEAVY anchor and it does NOT protect: `x^⊥ = 2.53 > 1` ⇒ the heavy Leggett mode is ABOVE its inter-band edge ⇒ FINITE linewidth, not sharp. The sharpness verdict for the DM anchor is "broadened / carrier-flips to a BdG pair on `~1/Δ_BCS`" — precisely E1, not a protection. Below-edge SHARPNESS protection lives on the LIGHT `ω_L1 = 0.070 M_KK = 0.1508·Δ_BCS` mode, which sits below BOTH its intra-band edge (`2Δ_BCS`) AND the deflated sharp-mode ceiling (`4.73·Δ_BCS`) — Sage-exact this turn — and is registered SHARP there (`LEGGETT-MODE-48`, Q = 670,000, `proven_1792`; atlas-07 lines 350/412/416/583). So the two-observable separation and the DE-inheritance are ONE structure: below-edge SHARPNESS is the LIGHT mode's property (where `proven_1792` actually proved it); the HEAVY anchor is off-the-edge on BOTH axes (Reading-A survival ∧ finite-linewidth sharpness). The mis-inheritance was carrying the light mode's below-edge SHARPNESS onto the heavy anchor; the DE-inheritance returns it; the two-observable separation then explains why the edge correction is not idle (it governs the LIGHT mode's lab linewidth) while touching neither the heavy anchor's survival (Reading A) NOR its sharpness (finite). landau's "load-bearing for sharpness" is right with the DOMAIN pinned: light mode + any future inter-band mode genuinely below `4.73·Δ_BCS`, NOT the registered `11.97·Δ_BCS` anchor.

**(2) The FREESTREAM gate is at risk of the `λ_fs` CATEGORY ERROR — and the resolution lives inside landau's own R2 (E1 vs R-i).** This is my standing forward dissent, from registered substrate physics, not preference. landau's R-i pins `v_rms` as the second moment of the frozen Bogoliubov occupation, `v_rms² = ∫(k/m)² n(k) d³k / ∫ n(k) d³k`, and his R-iii calls the FAIL branch "a genuine warm-DM tension" if the Mach-13.75 broadband transit gives high-`k` weight. But his E1 ALSO invokes the algebraic-coldness theorem. These cannot BOTH be the load-bearing reading, and the register settles it AGAINST R-iii: `CDM-CONSTRUCT-44` is `T^{0i}_4D = 0` exact with **5 independent proofs** (S44 W1-2, PROVEN; `CONSTRUCT-43` / `s43_cdm_category.py`). The 4D free-streaming velocity IS `v_fs = T^{0i}_4D / T^{00} = 0` ALGEBRAICALLY — for ALL internal modes, regardless of how broadband the internal `n(k)` is. The Bogoliubov occupation second moment is a SUBSTRATE-INTERNAL momentum spread (fiber/k-space), NOT the 4D effective velocity that enters `λ_fs`. Conflating the two is exactly the `λ_fs` category error I registered for internal modes (S43/S44). So the "warm-DM tension" R-iii fears cannot arise FROM the internal spread — `v_fs^4D = 0` is exact; if a freestream gate returns "warm," it has mis-identified the internal spread as the 4D velocity (a category error), not detected a warm relic. I answer Q-landau-2 YES — the algebraic-coldness theorem is the load-bearing input — and sharpen it to a HARD pre-registration constraint: the gate MUST pin `v_fs^4D = T^{0i}_4D/T^{00} = 0` (CDM-CONSTRUCT-44) as the coldness SOURCE and carry the occupation second moment as a SEPARATE substrate-internal DIAGNOSTIC, explicitly not the 4D velocity. This RESOLVES landau's internal R-i ↔ E1 tension in favor of E1. (NOTE: little's `framework-dm-properties.md` does register an "effective warm-DM mass / free-streaming horizon" — that is the laboratory-IN `T(k)` image of the bridge; my guard is about WHICH velocity enters it, the 4D one which is algebraically 0, not about forbidding the horizon observable.)

### EMERGENCE

Two pieces of new structure, neither opening's, both substrate-first.

**(EV1) The per-mode protection table — DE-inheritance × two-observable separation collapse to one ledger.** The cleanest statement of the whole adjudication is a single table indexed by MODE, sector-appropriate edge, BOTH axes read off:

| Mode | `m` | sector edge | survival axis | sharpness axis |
|:--|:--|:--|:--|:--|
| Light `ω_L1 = 0.070` (`0.1508·Δ_BCS`) | below `2Δ_BCS` (intra) ∧ below `4.73·Δ_BCS` | `n_s`-sector dipolar mode (`DIPOLAR-CATALOG-49`); not the DM relic | **SHARP** (`proven_1792`, Q=670k) — below-edge load-bearing HERE |
| Heavy DM anchor `11.97·Δ_BCS` (`5.5571 M_KK`) | **above** `4.73·Δ_BCS` (inter) | **Reading A** (CPT + GGE integrability + `Γ_grav<H_0`; C11-conditional; number-conserving `[H_BCS,N_pair]=0`) | **FINITE linewidth** (carrier-flips to BdG pair `~1/Δ_BCS`) — below-edge inapplicable |

One sector-appropriate energy-vs-edge test (no `√ρ_s` either side) governs the sharpness column; the survival column is set entirely by the conserved relic NUMBER (Reading A). The 79× mass gap IS a sector gap, exactly as landau argued in L2 — but the conclusion inverts his L2: the heavy anchor is ABOVE its inter-band edge, not below it.

**(EV2) The carrier-flip is observationally invisible BY the algebraic-coldness theorem — which converts FREESTREAM from a "warm-DM test" into a "which-velocity" pre-registration.** Under Convention M the heavy anchor is above-edge ⇒ it carrier-flips (collective mode → BdG pair) on `~1/Δ_BCS`, far inside any cosmological clock; by the structure-formation epoch the DM CARRIER is the quasiparticle-pair sector. The pairs are ALSO internal modes ⇒ `T^{0i}_4D = 0` holds for them too (CDM-CONSTRUCT-44, 5 proofs) ⇒ the carrier-flip is observationally invisible: `v_fs^4D = 0` before and after. So FREESTREAM's load-bearing question is NOT "what is `v_rms` from the internal occupation?" but "does the decay-product pair retain `T^{0i}_4D = 0`?" — and the registered answer (ALL internal modes, exact) is YES. The gate's PASS (cold relic) is what CDM-CONSTRUCT-44 PREDICTS; its only honest FAIL branch is a substrate-physics surprise — a decay product that is NOT a pure internal mode (nonzero 4D momentum density) — which would contradict the 5-proof theorem and is the genuinely-informative tail, NOT a broadband-`n(k)` "warm" reading. This is the substrate-first re-pre-registration of the already-minted FREESTREAM CF (a refinement directive, not a relist — see Carry-Forward).

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | (stiffness, edge) convention for inter-band mode | L1, Re:L1 | **Converged** | **Convention M (mass)**: `5.5571 M_KK` is the gap `ω_Leg` (the reduced inertia `χ_-` already folded in via `ω_Leg²=J_⊥/χ_-`), NOT a bare `√J_⊥`. The kinematic pair-breaking threshold is energy-vs-energy, **NO `√ρ_s`** either side (both eq(15c) and landau's L4 carried a spurious one). Edge = inter-band `E_edge^⊥ = Δ_BCS+√3 = 4.7308·Δ_BCS` (block-diagonality `V_inter=0` + Lichnerowicz `√3`), NOT intra-band `2Δ_BCS`. ⇒ `x^⊥ = 2.5302 > 1`, **ABOVE-edge** (Sage-exact; robust to the pure-fiber `2√3` channel, `x≈1.60`, and to `χ_-=ρ_s/2→1.27`). |
| 2 | S48 vs S70 mis-inheritance | L2, Re:L2 | **Converged** | **DE-inheritance.** `proven_1792` "below pair-breaking at ALL τ" / Q=670k SHARP belongs to the LIGHT `ω_L1=0.070` mode (atlas-07 lines 350/412/416/583 — the register scopes it CORRECTLY). The heavy `11.97·Δ_BCS` DM anchor (S70 LEGGETT-MOMENT-70) is a DISTINCT 79× object — above the inter-band edge, C11-conditional Reading-A survival. Fix = DISAMBIGUATION (downstream prose), not retraction. |
| 3 | Protection mechanism (below-edge vs integrability) | L3, Re:L3, V1, V2 | **Converged** | **Reading A.** DM-survival = A1 CPT non-annihilation (BDI `[J,D_K]=0`) + A2 GGE integrability (Ordered Veil `S_ent=0`, `R_therm=5252`) + A3 `Γ_grav<H_0` (C11). The **C11-conditionality is the tell** (below-edge would be UNCONDITIONAL). Pair-breaking is number-conserving (`[H_BCS,N_pair]=0`, S73a) ∧ frozen-GGE-inert ⇒ not a depletion channel. Below-edge closes the one channel survival does not require. |
| 4 | Protection-magnitude-exclusion theorem / (15c)→(15d) | L4, Re:L4 | **Emerged** | eq(15c) "exclusion" **WITHDRAWN** on every reading (two errors: intra-band edge + spurious `√ρ_s`). Theorem SURVIVES re-scoped to **SHARPNESS**: sharp-mode ceiling = `E_edge^⊥ = 4.73·Δ_BCS` (`√ρ_s`-free). It **CHARACTERIZES** the anchor (heavy, above-edge, finite-linewidth, Reading-A-surviving), no longer EXCLUDES it. The 170× target (`x=30.12`) stays unprotectable; 170× UNTOUCHED. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **Is the registered `5.5571 M_KK` the gap `ω_Leg` or the bare restoring scale `√J_⊥`?** Convention M (gap) is endorsed on three downstream-consistency grounds (abundance / `σ_SI` / `frac170` all consume it as a mass), but it is not yet read DIRECTLY off a diagonalized relative-phase Hamiltonian. `CF-S117-LEGGETT-EDGE-AND-STIFFNESS` (Carry-Forward) settles it. PASS = `5.5571` is the gap (Convention M confirmed, `x^⊥=2.53` above-edge stands); the alternative (bare `√J_⊥`, `÷√χ_-` pending) lowers `ω_Leg` and is the informative tail.

2. **Is the inter-band continuum edge actually `E_edge^⊥ = Δ_BCS + √3`?** Block-diagonality (`V_inter = 0` exact) forbids the (0,0)-pair channel and Lichnerowicz floors the fiber gap at `√3` — but block-diagonality is a SINGLE-PARTICLE statement; the COLLECTIVE edge (a pairing-vertex quantity) is not ESTABLISHED by `V_inter = 0`, only bounded below. The CF reads `E_edge^⊥` directly. PASS = the lowest two-quasiparticle channel is the mixed `Δ_BCS+√3 = 2.196`; the pure-fiber channel `2√3 = 3.46` gives `x≈1.60` — above-edge on either, but the EXACT margin is conditional.

3. **Does the FREESTREAM gate pin the 4D velocity, not the internal spread?** The relic's 4D free-streaming velocity is `v_fs = T^{0i}_4D/T^{00} = 0` EXACT (CDM-CONSTRUCT-44, 5 proofs). The already-minted `CF-S117-FREESTREAM-AT-ANCHOR` MUST pre-register `v_fs^4D = 0` as the coldness SOURCE and carry the Bogoliubov occupation second moment as a SEPARATE substrate-internal DIAGNOSTIC — never the 4D free-streaming velocity (the `λ_fs` category error for internal modes, S43/S44). PASS = cold (the 5-proof prediction); the only honest FAIL is a decay product with nonzero `T^{0i}_4D` (a substrate-physics surprise), NOT a broadband-`n(k)` "warm" reading.

4. **Is the heavy anchor's VALUE survival-conditional?** `Mass_LeggettDM/Δ_BCS = 11.97` is C11-CONDITIONAL on `Γ_grav < H_0` (LEGGETT-GRAV-DECAY-67, S70 / pinned S96-W7-2). "Graph-anchored at `5.5571 M_KK`" inherits the conditionality: the in-graph STRUCTURE is firm, the VALUE carries the C11 tag. Whether the gravitational-decay gate stays PASS at higher precision is a standing dependency of the anchor's number, not its in-graph status.

## Wrap-Up — Workshop Impact Summary

### What Changed

#### (a) Numerical revisions

- `x^⊥`: landau's L1 optimistic corner `0.897` (restoring-scale ∧ overall `ρ_s` ∧ intra-corrected edge) → **`x^⊥ = 2.5302 > 1`** under Convention M (mass) at the inter-band edge (Sage-exact this turn). Above-edge.
- sharp-mode ceiling: landau's L4 `m_ceiling^⊥ = E_edge^⊥√ρ_s = 13.35·Δ_BCS` → **`E_edge^⊥ = 4.7308·Δ_BCS`** (`√ρ_s`-free; the kinematic threshold is energy-vs-energy). The JOINT `√ρ_s` catch.
- `E_edge^⊥ = Δ_BCS + √3 = 2.196306 M_KK = 4.730820·Δ_BCS` (Sage-exact); reduced-inertia chains `χ_-=ρ_s/2 → x^⊥=1.268`, `ρ_s/3 → 1.553` (both > 1 — the optimistic corner does not hold by any route).
- light mode `ω_L1 = 0.070 = 0.1508·Δ_BCS`: below `2Δ_BCS` (intra) AND below `4.73·Δ_BCS` (sharp ceiling) — sharp on either reading (coherence check).

#### (b) Structural changes

- **eq(15c) "exclusion" of the registered anchor → WITHDRAWN on every reading** (two independent errors: intra-band `2Δ_BCS` edge + spurious `√ρ_s`). Epistemic-type change: an EXCLUSION → a CHARACTERIZATION (heavy, above-edge, finite-linewidth).
- **survival mechanism: Reading-B (below-edge) candidate → Reading A** (integrability / CPT / `Γ_grav<H_0`, C11-conditional). The DM anchor's protection axis re-typed off the kinematic edge.
- **protection-magnitude-exclusion theorem → re-scoped to SHARPNESS** (a distinct lab-Leggett-linewidth observable), orthogonal to survival. Single-axis "below-edge XOR integrability" → two-observable separation (survival ⊥ sharpness).
- **S48 below-edge: mis-inherited onto the heavy anchor → DE-inherited** (`proven_1792` / Q=670k SHARP returns to the LIGHT `ω_L1=0.070` mode; the heavy anchor's survival tag is C11 / Reading A).
- **below-edge SHARPNESS domain pinned**: it is the LIGHT mode's property (+ any future inter-band mode `< 4.73·Δ_BCS`), NOT the registered `11.97·Δ_BCS` anchor (volovik DISSENT 1).
- **FREESTREAM re-typed**: "warm-DM test on `v_rms` from internal occupation" → "which-velocity pre-registration" — `v_fs^4D = 0` (CDM-CONSTRUCT-44, 5 proofs) is the coldness source; the internal occupation second moment is a SEPARATE diagnostic (volovik DISSENT 2 / EV2), guarding the `λ_fs` category error.

### What Holds

- **DM-survival = Reading A** (registered, C11-conditional): CPT non-annihilation (BDI `[J,D_K]=0`) + GGE integrability (Ordered Veil `S_ent=0`, `R_therm=5252`, S95) + `Γ_grav<H_0` (LEGGETT-GRAV-DECAY-67). Two of three are edge-independent.
- **Number conservation** `[H_BCS, N_pair] = 0` (S73a) — pair-breaking is number-CONSERVING; the relic is the conserved quasiparticle NUMBER `N_DM = Σ_k n(k)`, not any single collective mode's population.
- **CDM-by-construction** `T^{0i}_4D = 0` EXACT, `w = 0`, `v_fs^4D = 0` (CDM-CONSTRUCT-44, 5 proofs S44; CONSTRUCT-43) — the relic's coldness is ALGEBRAIC, not kinematic; the carrier-flip is observationally invisible.
- **Block-diagonality** `V_inter = 0` exact 8.4e-15 (S60) + **Lichnerowicz floor** `|λ| ≥ √3` — together set the inter-band edge `≥ Δ_BCS + √3` (single-particle bound; the collective edge pending direct read).
- **The light `ω_L1 = 0.070` mode SHARP** (`proven_1792`, Q=670k, LEGGETT-MODE-48) — below-edge protection genuine HERE; atlas-07 lines 350/412/416/583 correctly scope it to the light mode.
- **170× untouched**: `x_target = 30.12` unprotectable; the 170× re-typing (cross-pillar ratio) from S116-W3-DISORDER-CLOSURE stands; abundance (`Ω_DM h²`) and `σ_SI` NULL unaffected (the mass re-typing touches structure-formation, not abundance/cross-section).

### What Breaks or Strains

- **Prior "below-edge DM-protection" prose for the HEAVY anchor OVERTURNED.** Any surface narrating the `11.97·Δ_BCS` DM anchor as "below the pair-breaking edge" is stale: under Convention M it is `x^⊥ = 2.53` ABOVE the inter-band edge. Concretely flagged: `session-116-w3-workingpaper.md:110` ("the clean Leggett mode is below the pair-breaking edge") — annotated this session (Effected-In-Session); the disorder-closure workshop's "What Holds" line 443 carries the same now-stale phrasing (folded into the WP annotation, which is the authoritative session record).
- **The atlas-07 [NEW S48] / S70 LEGGETT label is a mis-inheritance hazard.** The register CORRECTLY scopes below-edge to `ω_L1=0.070` (lines 350/412/416/583), but "the Leggett mode" reads ambiguously across the light `0.070` and heavy `11.97·Δ_BCS` objects; a disambiguation note is routed to mack (Effected-In-Session).
- **FREESTREAM's R-iii "warm-DM FAIL branch" strains against CDM-CONSTRUCT-44.** A broadband internal `n(k)` is NOT a warm relic (`v_fs^4D = 0` exact); the gate must pin the 4D velocity or risk the `λ_fs` category error. The genuinely-live FAIL is a non-internal decay product, not broadband occupation.
- **The inter-band edge `E_edge^⊥ = Δ_BCS+√3` is single-particle-bounded, not collective-established** — block-diagonality is a single-particle statement; the collective edge is pending `CF-S117-LEGGETT-EDGE-AND-STIFFNESS`. The `x^⊥ = 2.53` above-edge verdict is robust (holds for the pure-fiber `2√3` channel too, `x≈1.60`), but the EXACT margin is conditional.
- The Tier-2 anchor VALUE carries the C11 conditionality (`Γ_grav < H_0`); in-graph STRUCTURE firm, NUMBER conditional.

### Carry-Forward Computations (MATH ONLY — propagate to S117)

#### CF-S117-LEGGETT-EDGE-AND-STIFFNESS — convention + inter-band edge/stiffness DIRECT read [the inter-band `ρ_s^⊥` / continuum-edge extraction discriminator]

1. **What**: diagonalize the inter-band relative-phase (Leggett) pair-transfer Hamiltonian at `L_max=10` on the off-(0,0) blocks of `D_K`, and read DIRECTLY (not via the `m/√ρ_s` proxy) the THREE quantities the analytic argument leaves open: (i) the Leggett gap `ω_Leg` — settling the CONVENTION (is `5.5571 M_KK` the gap `ω_Leg`, Convention M, or the bare `√J_⊥` pending `÷√χ_-`?); (ii) the relative-phase stiffness `ρ_s^⊥` (the reduced `χ_-`); (iii) the lowest two-quasiparticle continuum edge `E_edge^⊥` and WHICH channel (mixed `Δ_BCS+√3 = 2.196` vs pure-fiber `2√3 = 3.46`). Extends L5(4iii), re-scoped per landau E2: it adjudicates CONVENTION + SHARPNESS, NOT survival (survival is Reading A on either verdict).
2. **Inputs**: the `D_K` `L_max=10` spectrum cache (off-(0,0) blocks); the clean Leggett `J_⊥` inter-band pair-transfer; `Δ_BCS = 0.4642547394830737` (R-PROTECTED S70); the Lichnerowicz floor `|λ| ≥ √3`; `ρ_s_C2 = 7.962` (S48 MASS-48 npz; pending canonical promotion CF-W3-1).
3. **Gate**: `[SIGN]` on `(ω_Leg − E_edge^⊥)`, reported as a CONVENTION+SHARPNESS verdict (NOT survival). PASS-A (Convention M) = `ω_Leg ≈ 5.5571` (gap; `x^⊥ = 2.53` above-edge, finite-linewidth confirmed); PASS-B (restoring-scale) = `ω_Leg ≈ 5.5571/√χ_-` (the edge comparison then re-runs with the direct `χ_-`). Edge sub-gate: `E_edge^⊥ ∈ {mixed 2.196, pure-fiber 3.46}` — both above-edge for the heavy anchor.
4. **Effort**: medium (inter-band diagonalization at `L_max=10`; GPU `torch.linalg` on the off-(0,0) blocks per `computation-environment.md`; no new irrep construction beyond the cache).
5. **Depends on**: this workshop's Convention-M verdict; the `D_K` `L_max=10` cache; `canonical_constants.py: Delta_BCS, Mass_LeggettDM_over_Delta_BCS`; the pending `rho_s_C2` promotion (CF-W3-1, W3 WP).

#### Refinement directive on the already-minted `CF-S117-FREESTREAM-AT-ANCHOR` (NOT a relist)

- Pre-register `v_fs^4D = T^{0i}_4D/T^{00} = 0` (CDM-CONSTRUCT-44, 5 proofs S44; CONSTRUCT-43) as the load-bearing COLDNESS SOURCE; carry the frozen Bogoliubov occupation second moment `∫(k/m)² n(k)d³k / ∫ n(k)d³k` as a SEPARATE substrate-INTERNAL momentum-spread DIAGNOSTIC, explicitly NOT the 4D free-streaming velocity. This guards the `λ_fs` category error for internal modes (S43/S44). Honest FAIL branch = a decay product with nonzero `T^{0i}_4D` (substrate-physics surprise contradicting the 5-proof theorem), NOT a broadband-`n(k)` "warm" reading. (Refinement to the existing CF — do NOT re-dispatch as a new gate; resolves the R-i ↔ E1 tension in landau R3 item R-i / EMERGENCE E1.)

### Effected In-Session (NON-MATH — completed by the final agent BEFORE TERMINATING)

- [x] **routed-to-mack: atlas-07 [NEW S48] / S70 LEGGETT disambiguation (the DE-inheritance).** atlas-07-permanent-results.md lines 350 / 412 / 416 / 583 are CORRECT for the LIGHT `ω_L1=0.070` mode and stay verbatim; ADD a scope note (mack discretion on placement) distinguishing the LIGHT below-pair-breaking/SHARP mode (`proven_1792`) from the HEAVY `Mass_LeggettDM/Δ_BCS=11.97=5.5571 M_KK` DM anchor (S70 LEGGETT-MOMENT-70) — above the inter-band edge (`x^⊥=2.53`, Convention M), survival = Reading A (C11-conditional `Γ_grav<H_0`), NOT below-edge. Prevents `proven_1792`'s confidence transplanting onto the heavy C11-conditional anchor. mack/designated-writer sole-writer (curated atlas surface). Routed via `SendMessage(to: "main")` ROUTE-1 [sent this session].
- [x] **routed-to-mack: registry re-scope of the protection-magnitude-exclusion theorem + the canonical DM-survival note.** (a) eq(15c) "exclusion" WITHDRAWN (two-error diagnosis: intra-band edge + spurious `√ρ_s`); the theorem SURVIVES re-scoped to a SHARP-mode ceiling `E_edge^⊥ = 4.73·Δ_BCS` (`√ρ_s`-free) — CHARACTERIZES, no longer EXCLUDES the anchor. (b) the DM-survival note: the `11.97·Δ_BCS` anchor's survival = Reading A (CPT + GGE integrability + `Γ_grav<H_0`, C11-conditional), NOT below-edge; the two-observable separation (survival ⊥ sharpness) is the verdict structure. Wherever a curated surface (permanent-results-registry / atlas-04 P2 + framework-dm-properties / falsifier-master-inventory) narrates the heavy anchor "below-edge protected", supersede to Reading-A (audit-trail-preserving RETAIN-and-supersede; mack to VERIFY which surfaces carry it). mack/designated-writer sole-writer. Routed via `SendMessage(to: "main")` ROUTE-2 [sent this session].
- [x] **WP-side annotation (direct — authorized non-curated in-domain item).** `session-116-w3-workingpaper.md:110` — the "What holds" phrase "below-edge DM-protection intact (the clean Leggett mode is below the pair-breaking edge)" overclaimed below-edge for the HEAVY clean-Leggett DM anchor; ANNOTATED with the leggett-dm-edge-protection correction (heavy anchor is ABOVE the inter-band edge under Convention M, `x^⊥=2.53`; below-edge holds for the LIGHT `ω_L1=0.070` mode; survival = Reading A; the `m_G=0.933` Cheeger graph-Goldstone IS the genuine below-edge object). Effected at `session-116-w3-workingpaper.md:110`.
- [x] **Own agent memory (direct).** Added the leggett-dm-edge-protection finding to `.claude/agent-memory/volovik-superfluid-universe-theorist/s116-leggett-dm-edge-protection.md` (detail file, created) + a pointer line in `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md:73`: Convention-M / `x^⊥=2.53` above-edge; survival = Reading A (the C11 tell); S48 DE-inheritance; two-observable separation; the FREESTREAM `λ_fs` category-error guard (CDM-CONSTRUCT-44). AMRI-safe: canonical VALUES live in the framework register (routed to mack), NOT duplicated in memory — the memory carries the agent-private methodological lesson only.
- [x] **No `.py` compute executed.** This workshop closes by artifact-existence (NO verdict line); the math carry-forward (`CF-S117-LEGGETT-EDGE-AND-STIFFNESS`) + the FREESTREAM refinement directive propagate to S117 via `/rclab-plan`. Sage was used for exact-rational VERIFICATION of the verdict numbers (`E_edge^⊥`, `x^⊥`, the reduced-inertia chains, `ω_L1/Δ_BCS`) — not a gate compute.

### Closing Line

The edge correction is real, but it points the other way: strip the inertia from the kinematic threshold and install the sector-appropriate edge, and the registered dark-matter anchor sits two-and-a-half times ABOVE its inter-band pair-breaking edge — so its survival was never a below-edge kinematic fact but the Volovik-program one, a frozen-GGE relic whose number is conserved, whose coldness is algebraic, and whose collective carrier merely flips to the quasiparticle pair it was always made of. Below-edge protection is genuine — it lives where the register already put it, on the light `0.070` mode — and the only thing left to compute is which velocity the free-streaming integral is allowed to see.

— volovik-superfluid-universe-theorist
