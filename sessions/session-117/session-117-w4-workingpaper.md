# Session 117 Wave 4 — Leggett DM Kinematics (Results Working Paper)

**Session**: 117 | **Wave**: 4 | **Plan**: session-117-plan-w4.md | **Theme**: Leggett-channel DM kinematics — discharge the 170× re-typing on three orthogonal axes (free-streaming coldness, protected-collective-mode ceiling, inter-band edge/sharpness). NONE of the three touches relic SURVIVAL (settled Reading A: CPT + GGE integrability S_ent=0 + Γ_grav<H_0, atlas-04 C11-conditional); all three are kinematic/sharpness statements at the graph-anchored mass m_Leggett = 11.97·Δ_BCS = 5.5571 M_KK.

**Wave composition**: 3 × `gate_type: compute` gates, parallel-dispatchable (independent of one another per the plan's Decision-Point Prerequisites — two soft upstream couplings, neither a hard block). Each closes via a verdict line in `computations/session-117/s117_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`), emitted through the race-safe `emit_verdict` knowledge-MCP tool. 4-1 and 4-3 are `[SIGN]` (MANDATORY sign/magnitude/regime 3-tuple companion row); 4-2 is `[CHAIN]` (substitution chain, no 3-tuple row).

## Gate Sections

### §W4-1. CF-S117-FREESTREAM-AT-ANCHOR (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-FREESTREAM-AT-ANCHOR`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (free-streaming kinematics of the Leggett GGE relic at the graph-anchored mass; EVOI-carrying PRIMARY of the Q3 leg)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: At the graph-anchored Leggett DM mass m_Leggett = 5.5571 M_KK the comoving free-streaming length λ_fs is below the structure-formation threshold with NO 170× enhancement — coldness sourced by the ALGEBRAIC v_fs^4D = T^{0i}_4D/T^00 = 0 (CDM-CONSTRUCT-44, 5 proofs S44), with the transit-frozen Bogoliubov occupation 2nd moment carried as a SEPARATE substrate-internal momentum-spread diagnostic, explicitly NOT the 4D velocity (expected direction: PASS / cold).
**Plan reference**: `sessions/session-plan/session-117-plan-w4.md` §W4-1 (which-velocity pre-registration, FREE-STREAMING-58 re-anchor, dual_prior Track-A/Track-B, substitution chain Steps 1–5).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` — verify by content presence via regex, NEVER by line/byte counts, per `feedback_max-effort-full-fidelity.md` + `.claude/rules/agent-standards.md §"Completion Verification"`):
All artifacts verified on disk by content (`grep -E`), never by line/byte count:
- `computations/session-117/s117_w4_freestream_at_anchor.py` — `from canonical_constants import` (L83) ✓; `print_verdict_payload` (def L492, call L596) ✓
- `computations/session-117/s117_w4_freestream_at_anchor.npz` (61,930 B; 47 keys) ✓
- `computations/session-117/s117_w4_freestream_at_anchor.png` (193,919 B; 4-panel: n(k), internal v_g vs k/m, z_tr(v_prod) robustness, λ_fs bar) ✓
- verdict line in `computations/session-117/s117_gate_verdicts.txt` (L44) matching `^CF-S117-FREESTREAM-AT-ANCHOR:.* audit_sha256=[a-f0-9]{64}` ✓; dual-SHA companion row (L45) ✓; MANDATORY `[SIGN]` 3-tuple row `sign=PASS magnitude=PASS regime=VALID` (L46) ✓; 2 extra annotation rows (L47–48) ✓
- this WP section: `**Status**: COMPLETED`, `**Verdict**: PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present ✓

**MCP Pre-Compute Audit** (`mcp__knowledge__*` queries run BEFORE writing the script):
- `search_knowledge("free-streaming length DM Leggett anchor CDM-CONSTRUCT-44 v_fs")` → CDM-CONSTRUCT-44 (`T^{0i}=0 exact`, atlas-07); `[NEW S42] S42 λ_fs DM = 3.1e-48 Mpc (CDM)` RETRACTED → 89 Mpc (HDM) → **CDM-CONSTRUCT-44 supersedes** (the exact Track-A/Track-B history); `z_tr` free-streaming horizon = 6.75e29, 22-OOM margin; equation `λ_fs = v_prod·a_prod·∫da/(a³H)`. **NOT pre-closed at the anchored mass** — FREE-STREAMING-58 is the lighter B2-fold anchor; this gate re-anchors at m_Leggett with the which-velocity guard.
- `get_constant("Mass_LeggettDM_over_Delta_BCS")` → 11.97 (S70 LEGGETT-MOMENT-70; C11-conditional on Γ_grav<H_0).
- `get_constant("Delta_BCS")` → 0.4642547394830737 (R-PROTECTED; S70 BCS-GAP-CANONICAL-70).
- `get_constant("M_DM_Leggett_GeV")` → 4.128202383934713e17 (S100a; cross-check pin, reproduced bit-exact).
- `get_constant("n_Bog")` → 0.9986332220990328; `get_constant("Omega_DM")` → 0.2657 (Planck; COMPARISON-ONLY); `get_constant("OOM_diff_MKK")` → 0.831664779390838.
- Anchored mass reproduced: m_Leggett = 11.97 × 0.4642547395 = **5.557129 M_KK = 4.128202e17 GeV** (= canonical M_DM_Leggett_GeV bit-exact); r_squeeze = arctanh(√n_Bog) = 3.990455, n_peak = (W_BG−1)/2 = 730.65 (both derived from canonical n_Bog/W_BG, not hardcoded).

**Verdict**: **PASS** (composite) — `[SIGN]` 3-tuple **sign=PASS, magnitude=PASS, regime=VALID**.
4-tuple: `(value='λ_fs^4D=0(EXACT,v_fs^4D=3.04e-17); z_tr=6.754e+29>>z_thr=6.2e+07 (22.0OOM); λ_fs<0.1Mpc by ~21dec; v_rms_int(v_g)=0.733c[NOT-4D]; cold;170x-DISCHARGED', scheme=FREESTREAM-ANCHOR, convention=WHICH-VELOCITY-PREREG, L_max=N/A)`.
dual-SHA: `audit_sha256=409637d4373418082bf855ab8e6146b0006ba8d16334fc5497f5698255ca43b8`, `content_sha256=dbc30c3a238549892e0f12ed426b92c332d02babe41ba3af4cb22427c8606387`.

**Results**:

*Substitution chain (the `[SIGN]` claim, with substituted numbers — `math-scripts.md §"Double-Check Logic Before Compute"`).* Claim: `(λ_fs − λ_threshold) < 0` (cold; below the structure-formation threshold) at the graph-anchored `m_Leggett = 5.5571 M_KK`, with NO 170× enhancement.
- **Step 1 (definition).** `λ_fs = ∫ v_fs(t)/a(t) dt` — the comoving free-streaming length; `v_fs` = the 4D streaming velocity that enters the 4D stress-energy current.
- **Step 2 (load-bearing, Track A).** `v_fs^4D = T^{0i}_4D / T^{00}`. The squeeze creates Leggett quasiparticles in (k, −k) pairs ⇒ the frozen occupation `n(k)=n(−k)` is EVEN; the momentum-density integrand `k·n(k)` is ODD ⇒ `T^{0i} = ∫ k n(k) d³k = 0` EXACTLY by parity (CDM-CONSTRUCT-44, 5 proofs S44; CONSTRUCT-43; w=0). Computed: `T^{0i}(1D, (k,−k) cancellation) = −5.33e-15`, angular `∫cosθ sinθ dθ = −5.55e-17`, energy density `T^{00} = 1.755e2 > 0` ⇒ **`v_fs^4D = |T^{0i}|/T^{00} = 3.04e-17` (machine zero)**.
- **Step 3 (substitute Step 2 → Step 1).** `λ_fs^4D = ∫ 0/a dt = 0` Mpc (EXACT).
- **Step 4 (read off the sign).** `λ_threshold = 0.1 Mpc > 0` ⇒ `(λ_fs^4D − λ_threshold) = (0 − 0.1) < 0` — **sign NEGATIVE (cold)**.
- **Step 5 (Track-B cross-check, internal diagnostic, NOT the 4D velocity).** The internal momentum spread of the frozen Bogoliubov occupation (BdG dispersion `E_k=√(k²+m_L²)` + sudden-quench squeeze capped at the canonical peak `n_peak=730.65`): `⟨k⟩=9.755 M_KK`, `⟨k²⟩=189.64 M_KK²`. The PHYSICAL (bounded) reading `v_rms_internal = √⟨v_g²⟩ = √⟨k²/(k²+m²)⟩ = 0.733c` (≤ c by construction; quad cross-check relerr 1.0e-6). The plan's literal NR form `√⟨(k/m)²⟩ = 2.48 > c` is UV-sensitive — the category-error signature that makes the algebraic Track A load-bearing. Even plugged NAIVELY as an effective production velocity, the relic was created at `z_prod≈1.05e29` (GUT-scale transit) ⇒ Track-B `z_tr = 3.21e29` (margin 21.7 OOM) and `λ_fs^naive = 2.85e-22 Mpc ≪ 0.1 Mpc` (~21 decades below).
- **Conclusion.** `(λ_fs − λ_threshold) < 0` under BOTH the load-bearing 4D reading AND the internal-diagnostic cross-check ⇒ **sign_verdict = PASS**; cold; the 170× re-typing is DISCHARGED on the free-streaming axis.

*z_tr re-anchor (FREE-STREAMING-58 reproduction at the graph-anchored mass).* Reproduced the s58 metric: `z_prod(grav)=1.0529e29`, `z_tr(grav)=6.7541e29`, `z_tr(kern)=4.5839e30` vs `z_threshold=6.2e7` ⇒ **margin 22.0 OOM**. The reproduction matches the s58 npz `z_tr_grav` to **relerr = 0.0 (EXACT)**. s58 Step-7 mass-independence (at fixed v_prod, z_tr depends on v_prod=c_Gold=0.915c, not m) confirmed; the heavier-mass *fixed-momentum* reading gives `v_prod(m_Leggett)=0.283c` (a heavier mass is LESS relativistic ⇒ colder), z_tr robust over the full v∈[0.1, 0.999] range (panel 3). WDM-equivalent mass `m_WDM_equiv = 3.40e23 keV` (≫ 5.3 keV Lyman-α bound).

*Two-velocity separation (the W-2 workshop refinement).* Track A (`v_fs^4D`, bulk current / energy density) and Track B (`v_rms_internal`, variance of the single-mode occupation) are ORTHOGONAL observables: the relic has zero bulk 4-momentum (cold) AND a finite internal momentum spread (a fiber-spectrum property). Reading the internal spread AS the 4D free-streaming velocity is the IS-not-IN container error (`phononic-framing.md`); the which-velocity pre-registration is exactly that guard. This reproduces the S42 history: the S42 `89 Mpc (HDM)` was the internal-spread-as-velocity reading, which **CDM-CONSTRUCT-44 supersedes** (T^{0i}=0 EXACT ⇒ the CDM reading, λ_fs→0, is correct).

*Solution-region mapping.* PASS maps the region: the Leggett DM anchor is kinematically COLD for structure formation WITHOUT any 170× enhancement — the 170× target is a cross-pillar ratio re-typed OFF the mass axis (S116-W3-DISORDER-CLOSURE), DISCHARGED here on the free-streaming axis. This gate does NOT touch relic SURVIVAL (settled Reading A: CPT + GGE integrability S_ent=0 + Γ_grav<H_0, atlas-04 C11-conditional). The ONLY honest FAIL branch would be a decay product with `T^{0i}_4D ≠ 0` contradicting the 5-proof theorem — NOT observed.

*Substrate framing.* Substrate-first (D_K eigenvalues → spectral moments → observable). The DM relic IS the conserved Leggett-channel quasiparticle number `N_DM = Σ_k n(k)` (a GGE relic of the transit, S38 Bogoliubov squeeze frozen by the Ordered Veil S_ent=0). Its mass is the graph-anchored inter-band Leggett scale `m_Leggett = 11.97·Δ_BCS = 5.5571 M_KK` (a D_K inter-band spectral functional), NOT a quantity IN a thermal bath. The free-streaming length is NOT measured IN a pre-existing FRW container expanding around the particle — it is the comoving distance the substrate excitation's emergent 4D stress-energy current would carry it, and that current's momentum part T^{0i}_4D vanishes ALGEBRAICALLY (CDM-CONSTRUCT-44): the relic is cold because the emergent stress-energy is dust-like (w=0), not because a thermal velocity is small. The transit-frozen Bogoliubov 2nd moment is a substrate-INTERNAL momentum spread (a fiber-excitation-spectrum property), which container-thinking mis-reads as a 4D free-streaming velocity — the which-velocity pre-registration is the IS-not-IN guard.

*Output Artifacts.* `s117_w4_freestream_at_anchor.py` / `.npz` / `.png`; verdict L44–48 in `s117_gate_verdicts.txt`.

---

### §W4-2. CF-S117-LEGGETT-COLLECTIVE-CEILING (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-LEGGETT-COLLECTIVE-CEILING`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (inter-band collective-mode ceiling; low-EVOI COMPANION confirming the re-typing from the collective-spectrum side)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: The heaviest PROTECTED inter-band collective Leggett mode — read from the full inter-band pair-transfer diagonalization across all Peter-Weyl (p,q) sectors at L_max=10 — SATURATES at frac170 = m_heaviest_protected/(170·Δ_BCS) ∈ [0.06, 0.08] (√N-saturation + continuum-edge cap), so the protected collective spectrum cannot reach the 170× structure-formation target (expected: frac170 ≈ 11.97/170 = 0.0704, PASS).
**Plan reference**: `sessions/session-plan/session-117-plan-w4.md` §W4-2 (block-diagonal per-(p,q) diagonalization, HIGH-PW-51 ladder cap E_n = 0.633·√C_2 + 0.555, substitution chain Steps 1–5).

**Output Artifacts** (closure-verification checklist; verified by content presence via regex, NEVER by line/byte counts):
- ✅ `computations/session-117/s117_w4_leggett_collective_ceiling.py` (30429 B) — `grep -nE 'from canonical_constants import|print_verdict_payload'` → L112 `from canonical_constants import *`; L231 `def print_verdict_payload(`; L588 call site.
- ✅ `computations/session-117/s117_w4_leggett_collective_ceiling.npz` (11724 B; data, not optional).
- ✅ `computations/session-117/s117_w4_leggett_collective_ceiling.png` (102859 B; plot, not optional — left: per-sector continuum-edge ceiling vs C₂ with √C₂ envelope + cap + anchor; right: frac170 bar vs the [0.06,0.08] band and the 170× line).
- ✅ verdict line in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-LEGGETT-COLLECTIVE-CEILING:.* audit_sha256=[a-f0-9]{64}` (audit_sha256 `2714a45ab512…0e5e`) + dual-SHA companion row + recheck companion row. NO 3-tuple row (`schema_v2_3tuple_required: false`; [CHAIN] band-membership verdict). sig_5: audit_sha256 unique (0 prior hits; emit_verdict reported sig_5-unique).
- ✅ this WP section: Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit present.

**MCP Pre-Compute Audit** (queries run BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("Leggett collective mode inter-band pair-transfer ceiling protected")` → Ω_DM h²=0.1200 PROVEN (S70, Leggett inter-band coherence); eq (15d) `protected^⊥ ⟺ ω_G < E_edge^⊥`; eq (8) inter-band `m ≲ (Δ_BCS+√3)√ρ_s = 13.35·Δ_BCS` (S116 W2). NOT pre-closed — the frac170 protected-ceiling is a fresh computation.
- `search_knowledge("HIGH-PW-51 single-fiber ladder scaling Casimir 0.633 sqrt C_2")` → collab eq 1 `max|λ| = 0.633√C_2(p,q)+0.555`, `C_2=(p²+q²+pq+3p+3q)/3`; s116-w3 eq 15d ladder top at (10,0)=4.72 M_KK=10.17·Δ_BCS. Machinery confirmed.
- `get_constant("Mass_LeggettDM_over_Delta_BCS")` → 11.97 (LEGGETT-MOMENT-70; C11-conditional Γ_grav<H_0).
- `get_constant("Delta_BCS")` → 0.4642547394830737 (R-PROTECTED, BCS-GAP-CANONICAL-70).
- Conclusion: result NOT pre-closed; the gate computes the protected-ceiling frac170 fresh against the S84 master spectrum (the cache IS the canonical block-diagonal diagonalization).

**Verdict**: **PASS** — frac170 = 0.070412 ∈ [0.06, 0.08].

**Results** (numbers first):

| quantity | value | source |
|:---|:---|:---|
| off-(0,0) sectors, p+q≤10 | 64 | S84 cache filtered |
| global ladder top max\|λ\| | 4.670218 M_KK at (0,10)/(10,0) = 10.0596·Δ_BCS | S84 cache (L=12 → p+q≤10) |
| HIGH-PW-51 ladder-top prediction | 4.721916 M_KK (rel dev 1.09%) | 0.633√C₂(10,0)+0.555 |
| lightest fiber gap min\|λ\| | 0.835894 M_KK at (0,1) | Jensen-deformed (below τ=0 √3 — the §W4-3 channel question, not this ceiling) |
| continuum-edge cap E_edge^⊥,cap (cache) | 5.134473 M_KK = 11.0596·Δ_BCS | Δ_BCS + ladder top |
| continuum-edge cap (HIGH-PW-51) | 5.186171 M_KK = 11.1710·Δ_BCS | Δ_BCS + 0.633√C₂+0.555 |
| registered Leggett DM anchor | 5.557129 M_KK = 11.97·Δ_BCS | LEGGETT-MOMENT-70 |
| **frac170 (anchor, PRIMARY)** | **0.070412 ∈ [0.06, 0.08]** | 11.97/170 |
| frac170 (cap cache, confirm) | 0.065056 ∈ [0.06, 0.08] | 11.06/170 |
| frac170 (cap HIGH-PW-51) | 0.065712 ∈ [0.06, 0.08] | 11.17/170 |
| √N-saturation: 170× needs | C₂≈15147 ⇒ p+q≈212 | structurally unreachable at L_max=10 |

**4-tuple**: `(value=0.070412, scheme=INTER-BAND-PAIR-TRANSFER, convention=PROTECTED-CEILING-frac170, L_max=10)`. **Dual-SHA**: audit_sha256 `2714a45ab512271158f599303931b2c2dab115c5059447d633727078934d0e5e`, content_sha256 `26f8ab6a0e269a7a16ac83fc20b97821378f85ae155d63e4efdd85e4b4ff3052`.

**Independent diagonalization cross-check (truncation-consistency / faithfulness)**: one off-(0,0) sector (1,0) re-diagonalized from scratch via `dirac_spectrum.collect_spectrum(τ_fold, …, max_pq_sum=1)` — `max|Δ|λ|| = 2.44e-15` vs the S84 cache over 48 eigenvalues (machine precision). The S84 master cache (L_max=12) filtered to p+q≤10 IS the faithful block-diagonal D_K(τ_fold) diagonalization (wall #2, D_K = ⊕₍ₚ,q₎ D₍ₚ,q₎); L_max_operational=10 = L_max_plan=10 — the ceiling lives at (10,0), constructed cleanly (no high-(p,q) stall; Casimir/Friedrich-Bär guard not triggered).

**Substitution chain** (Steps 1–5, substituted numbers):
- **S1** — m_heaviest_protected = the heaviest inter-band collective Leggett mode below its two-quasiparticle continuum edge E_edge^⊥ (protected/sharp, not a continuum resonance).
- **S2** — continuum-edge cap E_edge^⊥ = Δ_BCS + |λ|_fib; the L_max=10 single-fiber ladder top is max|λ| = 0.633√C₂(10,0)+0.555 = **4.7219 M_KK = 10.17·Δ_BCS** (HIGH-PW-51), cache value **4.6702 M_KK** (1.09% below the empirical scaling — the cache is the exact diagonalization, the scaling the empirical fit).
- **S3** — √N-saturation: J_⊥ is bounded by the fiber-gap scale (Lichnerowicz |λ|≥√3 at τ=0), so the collective mass m ∝ √J_⊥ does NOT grow without bound — it saturates at the continuum-edge-capped band O(11·Δ_BCS). The ladder top grows only as √C₂ ~ √N, so reaching 170·Δ_BCS would require C₂≈15147 ⇒ p+q≈**212** (unreachable; L_max=10 truncation, even L_max=15 reaches only p+q=15).
- **S4** — the graph-anchored Leggett mode IS the heaviest protected collective mode: m_heaviest_protected = m_Leggett = **11.97·Δ_BCS**, sitting at the saturated cap (computed cache cap 11.06·Δ_BCS / HIGH-PW-51 11.17·Δ_BCS; the anchor is ≈0.8·Δ_BCS above the cache cap — consistent with §W4-3's above-edge finite-linewidth finding x^⊥=2.53). frac170 = 11.97/170 = **0.07041**.
- **S5** — read off: 0.07041 ∈ [0.06, 0.08] ⇒ frac170 ≤ 0.08 ⇒ **PASS**. The 170× target is UNREACHABLE by the protected collective spectrum.

**Substrate framing (PHONONIC)**: The collective Leggett mode IS the inter-band relative phase φ₋ = φ₁ − φ₂ between the (0,0) BCS condensate and a (p,q) fiber sector of the block-diagonal D_K — a relative-phase collective coordinate of the substrate's two-band Ginzburg–Landau phase functional, NOT a mode propagating IN a lattice. The inter-band Josephson coupling J_⊥ breaks the relative U(1)₋ and gives φ₋ a mass (the Leggett gap ω_Leg²=J_⊥/χ₋); φ₊ stays the massless Anderson–Bogoliubov Goldstone. Block-diagonality (wall #2) both makes the per-(p,q) diagonalization tractable AND caps the protected spectrum: a sharp collective mode above its inter-band two-quasiparticle continuum edge is Landau-damped into that continuum, and the highest edge at L_max=10 is the fiber-ladder top + Δ_BCS ≈ 11·Δ_BCS, not a runaway scale. The 170× structure-formation target is a cross-pillar RATIO re-typed OFF the mass axis (S116-W3-DISORDER-CLOSURE) — a quantity the substrate spectrum is NOT obliged to produce; the protected collective spectrum, by these substrate caps (continuum-edge + √N-saturation), cannot reach it. The MgB₂/Fe-pnictide two-band Leggett mode is the laboratory ANALOG of this substrate inter-band mode. Direction substrate → emergent: D_K inter-band eigenvalues → ladder top + continuum edge → protected-mode ceiling → frac170. This is a KINEMATIC ceiling verdict — it does NOT touch relic SURVIVAL, which is settled by Reading A (CPT non-annihilation + GGE integrability S_ent=0 + Γ_grav<H_0, atlas-04 C11-conditional), independent of every kinematic verdict in this wave.

---

### §W4-3. CF-S117-LEGGETT-EDGE-AND-STIFFNESS (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-LEGGETT-EDGE-AND-STIFFNESS`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (direct inter-band read of (ω_Leg, ρ_s^⊥, E_edge^⊥); convention + sharpness adjudication, NOT a survival verdict)
**Agent**: `landau-condensed-matter-theorist` (PRIMARY compute owner; `volovik-superfluid-universe-theorist` co-routes the survival-vs-sharpness interpretation — the S116 W-2 workshop was landau × volovik; the producing script is single-author landau)
**Hypothesis**: The DIRECT inter-band read of (ω_Leg, ρ_s^⊥, E_edge^⊥) at L_max=10 confirms Convention M — ω_Leg ≈ m_Leggett = 5.5571 M_KK sits ABOVE the √ρ_s-free SHARP-MODE ceiling E_edge^⊥ = Δ_BCS + √3 = 4.73·Δ_BCS (x^⊥ = ω_Leg/E_edge^⊥ = 2.53 > 1, finite-linewidth, eq(15c) WITHDRAWN) — a CONVENTION + SHARPNESS verdict, NOT a survival verdict (survival is Reading A on either reading; expected: PASS-A above-edge).
**Plan reference**: `sessions/session-plan/session-117-plan-w4.md` §W4-3 (Convention-M vs restoring-scale discriminator, Lichnerowicz |λ|≥√3 edge, rho_s_C2 cross-check baseline soft-coupled to Wave-0, substitution chain Steps 1–5).

**Output Artifacts** (closure-verification checklist; verified by content presence via `grep -E`, NEVER by line/byte counts, per `feedback_max-effort-full-fidelity.md` + `.claude/rules/agent-standards.md §"Completion Verification"`):
- ✅ `computations/session-117/s117_w4_leggett_edge_and_stiffness.py` (40,801 B) — `grep -nE 'from canonical_constants import|print_verdict_payload'` → L125 `from canonical_constants import *`; L238 `def print_verdict_payload(`; L715 call site.
- ✅ `computations/session-117/s117_w4_leggett_edge_and_stiffness.npz` (13,918 B; data, not optional).
- ✅ `computations/session-117/s117_w4_leggett_edge_and_stiffness.png` (113,579 B; plot, not optional — left: energy-level diagram (ω_Leg vs the 4 edge variants + the light ω_L1 mode + the two sharp/above-edge zones); right: x^⊥ bar across conventions/channels vs the x^⊥=1 edge line + the restoring-scale lower bound).
- ✅ verdict line in `computations/session-117/s117_gate_verdicts.txt` (L78) matching `^CF-S117-LEGGETT-EDGE-AND-STIFFNESS:.* audit_sha256=[a-f0-9]{64}` (audit_sha256 `ba745a655acbec1a…f678`) + dual-SHA companion row (L79) + MANDATORY `[SIGN]` 3-tuple row `sign=PASS magnitude=PASS regime=VALID` (L80) + 2 extra annotation rows (L81–82). sig_5: audit_sha256 unique (count=1; emit_verdict reported sig_5-unique).
- ✅ this WP section: Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit present.

**MCP Pre-Compute Audit** (queries run BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("Leggett mode inter-band edge protection DM survival sharpness rho_s")` → S116 workshop `s116-leggett-dm-edge-protection.md` (eq 1244–1252); eq (8) inter-band `m ≲ (Δ_BCS+√3)√ρ_s = 13.35·Δ_BCS` and eq (15d) `protected^⊥ ⟺ ω_G < E_edge^⊥ ⟺ m_Leggett < E_edge^⊥·√ρ_s^⊥` (the registered S116 forms, BOTH carrying the √ρ_s this gate strips per the latest-synthesis-wins W-2 refinement); Ω_DM h²=0.1200 PROVEN (S70, Leggett inter-band coherence). NOT pre-closed — the direct (ω_Leg, ρ_s^⊥, E_edge^⊥) read + the convention adjudication is the fresh deliverable.
- `get_constant("rho_s_C2")` → 7.962 (S48 MASS-48; canonical, **importable** post Wave-0 CF-S117-HK-RHOS-C2-PROMOTE — the soft-coupling is satisfied, NOT PRE-REG-INC).
- `get_constant("Mass_LeggettDM_over_Delta_BCS")` → 11.97 (S70 LEGGETT-MOMENT-70; C11-conditional on Γ_grav<H_0).
- `get_constant("Delta_BCS")` → 0.4642547394830737 (R-PROTECTED; S70 BCS-GAP-CANONICAL-70).
- Sage (`sage_eval`) cross-checked every exact ratio: E_edge^⊥(mixed,√3)/Δ_BCS = 4.730820, x^⊥ = 11.97·Δ_BCS/(Δ_BCS+√3) = 2.530217, and the reduced-susceptibility bound χ_- = ρ_s·f(1−f) ≤ ρ_s/4 (max at f=1/2).

**Verdict**: **PASS** (composite) — `[SIGN]` 3-tuple **sign=PASS, magnitude=PASS, regime=VALID**. Convention M confirmed: ω_Leg = 5.5571 M_KK sits ABOVE its √ρ_s-free inter-band SHARP-mode ceiling on every channel; x^⊥ = 2.530 (mixed Lichnerowicz, headline) matches the pre-registered 2.5302 to dev 0.0e+00.
4-tuple: `(value=2.530217, scheme=LEGGETT-DIRECT-READ, convention=CONVENTION-M-vs-RESTORING-SCALE, L_max=10)`.
dual-SHA: `audit_sha256=ba745a655acbec1a499e5a0bffd613940667a30ccdc65058eac8f056db90f678`, `content_sha256=a8b47dd9c9a22559c6133f168ad10e1f73d53332e26eba6a9ce6a2bc1053b625`.

**Results** (numbers first):

| quantity | value | source / channel |
|:---|:---|:---|
| **(i) ω_Leg (Leggett gap, Convention M)** | **5.557129 M_KK = 11.97·Δ_BCS** | LEGGETT-MOMENT-70; ω_Leg²=J_⊥/χ_- already inertia-dressed |
| **(ii) ρ_s^⊥ = χ_- (reduced susceptibility)** | **≤ ρ_s/4 = 1.9905** (rigorous upper bound) | χ_- = ρ_s·f(1−f), max at f=1/2; ρ_s = χ_+ = 7.962 (canonical) |
| overall ρ_s = χ_+ = χ_1+χ_2 (cross-check baseline) | 7.962 | canonical `rho_s_C2` (post Wave-0 promotion) |
| **(iii) E_edge^⊥ mixed, Lichnerowicz √3 (PRE-REG)** | **2.196306 M_KK = 4.730820·Δ_BCS** | Δ_BCS + √3 (one (0,0) qp + one fiber qp) |
| E_edge^⊥ mixed, τ_fold direct | 1.300148 M_KK = 2.8005·Δ_BCS | Δ_BCS + |λ|_fib(τ_fold)=0.835894 (cache (0,1)/(1,0)) |
| E_edge^⊥ pure-fiber, Lichnerowicz 2√3 | 3.464102 M_KK = 7.4616·Δ_BCS | 2√3 |
| E_edge^⊥ pure-fiber, τ_fold direct | 1.671787 M_KK = 3.6010·Δ_BCS | 2·|λ|_fib(τ_fold) |
| **x^⊥ = ω_Leg/E_edge^⊥ (mixed Lichnerowicz, HEADLINE)** | **2.530217 > 1** (above-edge) | matches pre-reg 2.5302 (dev 0.0e+00) |
| x^⊥ (mixed τ_fold direct) | 4.274227 > 1 | LOWER edge ⇒ MORE above-edge |
| x^⊥ (pure-fiber Lichnerowicz / τ_fold) | 1.604205 / 3.324065 > 1 | above-edge on every channel |
| ω_Leg − E_edge^⊥ (the [SIGN] quantity) | +3.360824 M_KK > 0 | sign POSITIVE ⇒ above-edge |
| restoring-scale x^⊥ LOWER bound (all χ_- ≤ ρ_s/4) | ≥ 1.7934 > 1 | even PASS-B stays above-edge for ALL band splits |
| (0,0) BCS raw Dirac floor |λ|_min | 0.819741 M_KK | NOT the pairing gap (Δ_BCS=0.4643 is) |
| fiber ladder top (cross-ref §W4-2) | 4.670218 M_KK at (10,0) | S84 cache |

**Convention sub-verdict — PASS-A (Convention M).** Convention M is the consistent reading: ω_Leg² = J_⊥/χ_- is ALREADY inertia-dressed (the reduced susceptibility sits in the denominator), so 5.5571 M_KK IS the gap/rest-energy consumed in Ω_DM h²=0.120 / σ_SI — an additional ÷√χ_- double-counts. The restoring-scale alternative (PASS-B, ω_Leg=√J_⊥ pending ÷√χ_-) is NOT needed; even if adopted it stays above-edge (x^⊥ ≥ 1.7934 for ALL admissible χ_- ≤ ρ_s/4).

**Independent diagonalization cross-check (cache faithfulness, wall #2)**: one off-(0,0) sector (1,0) re-diagonalized from scratch via `dirac_spectrum.collect_spectrum(τ_fold, …, max_pq_sum=1)` — `max|Δ|λ|| = 2.44e-15` vs the S84 cache over 48 eigenvalues (machine precision). The cache IS the faithful block-diagonal D_K(τ_fold) diagonalization (D_K = ⊕₍ₚ,q₎ D₍ₚ,q₎), so the edge read is a genuine diagonalization result.

**Substitution chain** (Steps 1–5, substituted numbers — `math-scripts.md §"Double-Check Logic Before Compute"`). Claim: `(ω_Leg − E_edge^⊥) > 0` (above-edge; Convention M) — the registered anchor is heavy, above its inter-band pair-breaking edge, finite-linewidth; NOT below-edge protected.
- **S1 (ω_Leg, Convention M).** ω_Leg = m_Leggett = 11.97·Δ_BCS = **5.557129 M_KK** (ω_Leg²=J_⊥/χ_- inertia-dressed, so no further ÷√χ_-).
- **S2 (E_edge^⊥).** Lowest inter-band 2-qp continuum edge = one (0,0) BCS qp (Δ_BCS) + one fiber qp (|λ|_fib). Lichnerowicz τ=0 floor |λ|_fib=√3 ⇒ E_edge^⊥ = 0.464255 + 1.732051 = **2.196306 M_KK = 4.730820·Δ_BCS** (mixed, the pre-reg). Block-diagonality (wall #2) forbids the pure-(0,0) channel (single-particle bound; the inter-band relative-phase mode must produce ≥1 fiber qp). Pure-fiber channel: 2√3 = 3.4641 M_KK.
- **S3 (substitute, NO √ρ_s).** ω_Leg − E_edge^⊥ = 5.5571 − 2.1963 = **+3.3608 M_KK > 0** (mixed); 5.5571 − 3.4641 = +2.0930 > 0 (pure-fiber). The kinematic SHARPNESS threshold is energy-vs-energy — the eq(15c)/(15d) √ρ_s is a restoring-curvature→frequency conversion mis-installed into an energy comparison; STRIPPED, the SHARP-mode ceiling IS the bare edge.
- **S4 (read off the ratio).** x^⊥ = ω_Leg/E_edge^⊥ = 5.5571/2.1963 = **2.530** (mixed); 1.604 (pure-fiber). DIRECT τ_fold edge (|λ|_fib=0.836<√3, Jensen-deformed — NOT a bug): x^⊥ = 4.274 (mixed), 3.324 (pure-fiber) — the deformed (operating-point) edge is LOWER, so the anchor is EVEN MORE above-edge; the √3 pre-reg is the conservative (higher) choice.
- **S5 (direction).** POSITIVE (above-edge) on every channel AND under restoring-scale (x^⊥ ≥ 1.7934 for ALL χ_- ≤ ρ_s/4) ⇒ **sign_verdict = PASS**. The lone below-edge corner from my S116 opener (x_G^⊥=0.8967) required χ_-=ρ_s (the FULL overall stiffness), which is **mathematically impossible** for a reduced susceptibility (f(1−f) ≤ ¼ ⇒ χ_- ≤ ρ_s/4). The "below-edge" reading was a convention error, not a physical regime.
- **Conclusion.** The heavy anchor is ABOVE its inter-band pair-breaking edge (Convention M) — a SHARPNESS characterization (finite-linewidth lab Leggett mode), NOT an exclusion. Eq(15c) `m < 2Δ_BCS√ρ_s = 5.64·Δ_BCS` is WITHDRAWN and re-typed as a CHARACTERIZATION; the √ρ_s-free SHARP-mode ceiling E_edge^⊥ = 4.73·Δ_BCS *characterizes* (no longer *excludes*) the anchor.

**Survival ⊥ sharpness separation (load-bearing, from the W-2 workshop).** This is a CONVENTION + SHARPNESS verdict ONLY. Relic SURVIVAL is the conserved-number question `N_DM = Σ_k n(k)`, settled by **Reading A** (CPT non-annihilation + GGE integrability S_ent=0 + Γ_grav<H_0, atlas-04 C11-conditional) — UNCHANGED on either convention verdict here (pair-breaking of a collective mode is number-conserving: `[H_BCS, N_pair]=0`, so a finite Leggett linewidth reshuffles the carrier without depleting the relic). Below-edge SHARPNESS belongs to the LIGHT mode ω_L1 ≈ 0.30·Δ_BCS (below its INTRA-band edge 2Δ_BCS, S48 `proven_1792`), a DISTINct object 21× lighter than this heavy anchor; the S48 below-edge proof does NOT inherit to the 5.5571 anchor (volovik's DE-inheritance, conceded S116).

**Substrate framing (PHONONIC)**: The Leggett mode IS the inter-band relative phase φ₋ = φ₁ − φ₂ between the (0,0) BCS condensate and the fiber sector of the block-diagonal D_K — a relative-phase collective coordinate of the substrate's two-band Ginzburg–Landau phase functional, NOT a mode IN a two-band superconductor. Its three defining quantities are intrinsic D_K data: the gap ω_Leg (the inter-band pair-transfer √J_⊥ scale, inertia-dressed by χ_-), the relative-phase stiffness ρ_s^⊥ = χ_- (the reduced susceptibility, rigorously ≤ ρ_s/4 = ¼ of the overall-phase Goldstone stiffness — the relative-phase inertia can never reach the in-phase one), and the continuum edge E_edge^⊥ (the fiber-gap continuum Δ_BCS+√3 set by the Lichnerowicz floor, with block-diagonality forbidding the pure-(0,0) channel). The √ρ_s that S116 eq(15c) carried was a frequency-conversion factor mis-installed into an energy-vs-energy kinematic threshold; stripped, the SHARP-mode ceiling is the bare inter-band edge 4.73·Δ_BCS, and the heavy anchor sits above it. This is a SHARPNESS (lab Leggett-linewidth) statement measured IN the laboratory as a finite-width Raman/IR peak (MgB₂, Fe-pnictide); it is ORTHOGONAL to relic SURVIVAL, the substrate IS-fact that the conserved quasiparticle number N_DM persists (Reading A). Direction substrate → emergent: the D_K inter-band spectrum sets ω_Leg, ρ_s^⊥, E_edge^⊥; the lab measures the linewidth.

*Output Artifacts.* `s117_w4_leggett_edge_and_stiffness.py` / `.npz` / `.png`; verdict L78–82 in `s117_gate_verdicts.txt`.

---

## Wave 4 Synthesis (team-lead)

All three Wave-4 gates PASS. The collective output: **the 170× re-typing is discharged on three orthogonal kinematic axes** — free-streaming coldness (4-1), protected-collective-mode ceiling (4-2), inter-band edge-sharpness (4-3) — at the graph-anchored Leggett mass m_Leggett = 11.97·Δ_BCS = 5.5571 M_KK (4.128e17 GeV). **NONE of the three touches relic SURVIVAL**, which the S116 W-2 workshop settled is Reading A (CPT non-annihilation + GGE integrability S_ent=0 + Γ_grav<H_0, atlas-04 C11-conditional) — every Wave-4 verdict is kinematic/sharpness, orthogonal to the conserved-number survival question.

### (a) Numerical revisions
- 4-1: v_fs^4D = **3.04e-17** (machine zero); z_tr = 6.754e29 ≫ z_thr=6.2e7 (22.0 OOM margin); reproduces FREE-STREAMING-58 at relerr=0.0; WDM-equiv 3.40e23 keV.
- 4-2: frac170 = **0.0704** ∈ [0.06, 0.08]; ladder top 4.670 M_KK at (10,0); 170× would need C₂≈15147 ⇒ p+q≈212 (structurally unreachable at L_max=10).
- 4-3: x^⊥ = ω_Leg/E_edge^⊥ = **2.530** > 1 (above-edge, Convention M); restoring-scale lower bound x^⊥ ≥ 1.793 (above-edge for ALL admissible χ_- ≤ ρ_s/4).

### (b) Structural changes
- **4-1 coldness is a parity EXACTNESS, not a numerical smallness** (epistemic-TYPE): the (k,−k) squeeze pairing makes n(k) even ⇒ T^{0i} odd integrand ⇒ vanishes EXACTLY ⇒ λ_fs^4D = 0 (CDM-CONSTRUCT-44). The "internal momentum spread v_rms=0.733c" is correctly demoted to a substrate-internal diagnostic (the IS-not-IN which-velocity guard), superseding the S42 "89 Mpc HDM" internal-spread-as-velocity reading.
- **4-3 eq(15c) WITHDRAWN → re-typed as a CHARACTERIZATION**: the √ρ_s in the S116 eq(15c)/(15d) inter-band sharp-mode ceiling was a frequency-conversion factor mis-installed into an energy-vs-energy threshold. Stripped, the bare edge E_edge^⊥ = 4.73·Δ_BCS *characterizes* (no longer *excludes*) the anchor — the heavy mode is finite-linewidth (lab Leggett-mode-like), not below-edge protected. The S116 below-edge corner was a convention error (it required the impossible χ_- = ρ_s for a reduced susceptibility ≤ ρ_s/4).

### Cross-cutting (the wave's load-bearing frame)
The 170× target is a cross-pillar RATIO re-typed OFF the mass axis (S116-W3-DISORDER-CLOSURE) — a quantity the substrate spectrum is not obliged to produce. All three axes independently confirm it is not reached, by distinct substrate mechanisms (parity-exact w=0 dust; √N-saturation + continuum-edge cap; above-edge finite linewidth). The Q3 Leggett-DM leg is kinematically clean and viable; survival stays Reading A (untouched).

## Carry-Forward Computations

No carry-forwards: all wave outcomes closed in-session. All three gates PASS as expected; the plan's two contingent forward items did not trigger (4-3 confirmed Convention M, so the PASS-B restoring-scale re-run is unnecessary — and it stays above-edge regardless; 4-1's CDM-CONSTRUCT re-exam was gated on a surprise T^{0i}≠0 FAIL that did not occur). Per `workingpaper.md` Rule 4.

### Investigator-surfaced carry-forwards (S117 `/rclab-investigate` consolidation; append-only)

One NEW first-surfaced Q2 gate-finalization item: the wave-close disposition correctly noted the eq(15c) re-scope needed no new registry edit (already landed as the S116-W2 corrigendum), but did NOT address that the S116 Row #79 family still carries an explicit "discharge owed" status that the now-PASSED W4 gates should flip. Absent from `session-117-housekeeping.md §A`.

#### CF-W4-1 — Row #79 "discharge owed" reconciliation + EVOI "170× DM-mass" §5-fold (Q2 — registry-hygiene / gate-finalization carry-forward)

| Field | Spec |
|:------|:-----|
| **What** | The S116 Row #79 family in `falsifier-master-inventory.md` pre-registered all three S117 W4 gates as forward/owed discharge gates and explicitly states "the discharge gate is owed" (L2698, Row #79.compute-S116-W3-DISORDER-CLOSURE, "NOT asserted-closed") for `CF-S117-FREESTREAM-AT-ANCHOR`, plus pre-registered x^⊥=2.530217 (L2712 → `CF-S117-LEGGETT-EDGE-AND-STIFFNESS`). All three W4 gates have now PASSED (x^⊥=2.530217 to dev 0.0e+00; cold λ_fs^4D=0; frac170=0.0704), but no S117 confirmation/discharge sub-row was landed — the inventory still reads "discharge owed / NOT asserted-closed." Reconcile: land a `Row #79.audit-S117-W4` discharge-confirmation sub-row flipping "discharge owed" → "discharged on three orthogonal axes," OR record the explicit latest-synthesis-wins decision that confirming-compute PASSes mint no new sub-row (the S116-W2 corrigendum already carries the x^⊥ number 4-3 confirms). Pairs with the EVOI §5-fold (same closure, two surfaces): mark the "170× DM-mass" standing gap (`evoi-framework.md` L240/L280) RESOLVED at the S118 re-stamp. |
| **Inputs** | The three S117 W4 verdict lines (`s117_gate_verdicts.txt` L44/L49/L78); WP §W4 synthesis; `falsifier-master-inventory.md` Row #79 family (L2690-2720); `sessions/evoi-framework.md` L240/L280. |
| **Gate** | Artifact-existence: a Row #79 discharge-confirmation sub-row present OR an explicit no-row latest-synthesis-wins decision recorded in the inventory's S117 audit trail, AND the EVOI "170× DM-mass" gap marked RESOLVED. `mack-cosmic-bridge` sole writer (registry); `/rclab-plan` Step 1c-REGISTERS (EVOI fold). LOW-STAKES (survival stays Reading A; the substantive re-scope was landed at S116). |
| **Effort** | low (single mack registry decision + 1 EVOI §5 fold). |

## Effected In-Session / routed to session-close

- Wave-0 soft-coupling SATISFIED in-session: 4-3 consumed `rho_s_C2 = 7.962` as a canonical import (the W0-1 promotion this session made it importable) — no PRE-REG-INC. Recorded; no further action.
- atlas-08 Q3 (Leggett DM kinematics): 170× re-typing DISCHARGED on three orthogonal axes (free-streaming / collective-ceiling / edge-sharpness); survival stays Reading A. Routed to the session-close capstone-hygiene pass (Q3 status reconcile; the DM leg is an atlas-04 assumption + atlas-08 dashboard item).
- The eq(15c) WITHDRAWAL → characterization (4-3) is documented in §W4-3 and is internal to the S116-workshop equation lineage; no separate registry edit required (the registered S116 forms carry the √ρ_s the W-2 refinement strips, latest-synthesis-wins).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-28 | Leggett DM free-streaming (4-1) | re-typed 170× open (S116-W3) | COLD, λ_fs^4D=0 EXACT; 170× discharged (free-streaming axis) | 4-1 PASS (parity-exact w=0) |
| 2026-06-28 | Leggett protected collective ceiling (4-2) | 170× open | frac170=0.0704 ∈ band; 170× unreachable (p+q≈212) | 4-2 PASS (√N-saturation + edge cap) |
| 2026-06-28 | Leggett inter-band edge eq(15c) (4-3) | eq(15c) below-edge exclusion (S116) | WITHDRAWN→characterization; x^⊥=2.530 above-edge (Conv. M) | 4-3 PASS; √ρ_s frequency-factor mis-install corrected |
| 2026-06-28 | relic SURVIVAL | Reading A (atlas-04 C11-conditional) | UNCHANGED (no Wave-4 verdict touches it) | kinematic axes orthogonal to conserved-number survival |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| 4-1 | `s117_w4_freestream_at_anchor.py` | `.npz` (47 keys) | `.png` (4-panel) | PASS (+[SIGN] 3-tuple) |
| 4-2 | `s117_w4_leggett_collective_ceiling.py` | `.npz` | `.png` | PASS ([CHAIN]) |
| 4-3 | `s117_w4_leggett_edge_and_stiffness.py` | `.npz` | `.png` | PASS (+[SIGN] 3-tuple) |
