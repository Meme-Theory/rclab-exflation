# Session 104 — Planning Context (mechanical gather; canonical scope for per-wave planners)

**Generated**: 2026-06-10 by `/rclab-plan --session 104 --extra "§7 of the assay"`
**Prior session**: S103 (4 dispatched waves, 15/15 gates closed; W4 honestly NOT-DISPATCHABLE; EMPTY workshop campaign)
**Planning corpus** = S103 WP carry-forwards (1b) ∪ S103-era gem-triage candidates (register/`--extra`-sourced, 1c-REGISTERS.CONSUME). EVOI re-stamped S104 (lag 0, audit PASS); atlas-08/atlas-04/open-channel-ledger maintained this pass (backing audit: `sessions/framework/registry/atlas-08-freshness-S103.md`); mack falsifier-surface dispatch IN FLIGHT (plan-time maintenance — Row #85 multi-anchor σ-table, LIV-null row mint, saddle guard, area-quantum WATCH, X(2370)/g-2 notes, atlas-04 §IX Item-3 refresh). Planners: those surface items are NOT plan gates — do not duplicate them.

## Source manifest

| Source | Items |
|:-------|:------|
| `sessions/session-103/session-103-w1-workingpaper.md §"Carry-Forward Computations"` | 0 (explicit none; HK-1 mirrored in w2) |
| `sessions/session-103/session-103-w2-workingpaper.md §"Carry-Forward Computations"` | CF-S104-W2-VIIAM-L11-ANCHOR, CF-S104-HK-1 |
| `sessions/session-103/session-103-w3-workingpaper.md §"Carry-Forward Computations"` | CF-S104-W3-SWMAX-MPMATH-EDGE |
| `sessions/session-103/session-103-w5-workingpaper.md §"Carry-Forward Computations"` | CF-S104-W5-BRANCH-IV-DIRECT-L1314 |
| `sessions/session-103/workshops/` | no workshop wrap-ups (EMPTY campaign — honest zero) |
| `downloads/research-sweep-s103/GEM-TRIAGE.md` (`--extra`; register-sourced candidates) | 10 gem gates (5 GEM-COMPUTE + 5 GEM-BRIDGE) + 3 workshop-track items + mack-surface set |
| `sessions/evoi-framework.md` §6 (S104 re-stamp) | the composed queue below (authoritative wave order) |

**Dedupe check**: zero overlap between the 4 WP-CFs and the 16 gems (GEM-TRIAGE §7 "Composition note", verified); the ONE adjacency is Rank 15 ↔ the Wave-1 L_max CFs (joint-consideration flag, carried in the Wave-5 item notes).

---

## Carry-forward table (4-field specs)

### Wave 1 — Standing precision CFs (owner: gen-physicist)

#### S104-VIIAM-L11-ANCHOR (from CF-S104-W2-VIIAM-L11-ANCHOR; verbatim spec at `session-103-w2-workingpaper.md` §CF)
1. **What**: §VII.AM envelope-row Level-3-vs-Level-2 evaluation at L=11 under the SAME pre-registered L-indexed rule (anchor(L) := dGamma_over_Gamma at the L-slice) — the deeper-truncation pathway the S103 W2-3 FAIL (`b47ccf98`, ratio 1.1578 at L=10) leaves open.
2. **Inputs**: `computations/session-101/s101_viiam_alpha_envelope_pin.npz` (dGamma_over_Gamma[L=11] = 2.11e-05; α = 4.690533), `computations/session-102/s102_w2_viiam_l2l3_recon.npz` (envelope prefactor C = 1.8622), `computations/session-103/s103_viiam_lindexed_anchor.npz` (L=10 baseline).
3. **Gate**: anchor(L=11) < envelope(L=11) strict, BOTH envelope candidates re-evaluated at L=11, comparator PRE-REGISTERED at plan-freeze BEFORE evaluation (anti-comparator-shopping; the L=11-slice rule pinned in the plan, not chosen at runtime).
4. **Effort**: 0.25 gate (~1 h; scalar inequality on pinned floats).

#### S104-SWMAX-MPMATH-EDGE (from CF-S104-W3-SWMAX-MPMATH-EDGE; verbatim spec at `session-103-w3-workingpaper.md` §CF)
1. **What**: ≥300-bit (mpmath/Sage) re-derivation of S_W_max from the frozen W-stage Bogoliubov pair (α_W, β_W) to adjudicate `deviation < S_W_max−1` vs `== S_W_max−1` below the float64 floor (the S103 W3-1 knife-edge).
2. **Inputs**: `computations/session-102/s102_w7_ladder_phase_resolved.npz` (frozen; W_beta_re/W_beta_im/abs_beta_W full float64, deviation, envelope_upper_dev), `computations/session-103/s103_famp_tolerance_repin.npz` (the re-pin record).
3. **Gate**: sign(deviation − (S_W_max−1)) at ≥300-bit ∈ {−1 strict interior → PASS; 0 exact saturation → structural-identity finding; +1 breach → re-opens the S79 sufficiency question} — three pre-registered branches, each a distinct registry state.
4. **Effort**: 0.25 gate (~1 h; mpmath scalar evaluation of the SU(1,1) window algebra).

#### S104-BRANCH-IV-DIRECT-L1314 (from CF-S104-W5-BRANCH-IV-DIRECT-L1314; verbatim spec at `session-103-w5-workingpaper.md` §CF)
1. **What**: direct ρ_B(13), ρ_B(14) spectra via cache-assisted recursive irrep construction (pre-build the Sym^p parent chain offline / across timeslots, then sector-eigvalsh on GPU), closing spread_CAC({12,13,14}) with DIRECT spectra the S103 FB-envelope INFO (`508c7cf3`) could only bound.
2. **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (L≤12 sectors), `computations/_shared/dirac_spectrum.py` (get_irrep recursive Casimir projection), `computations/session-103/s103_branch_iv_deep_truncation.npz` (FB envelope + offset_B + feasibility record).
3. **Gate**: spread_CAC = max−min of w₀^CAC(L) over {12,13,14} with direct spectra, against the UNCHANGED W5-2 band (PASS ≤ 0.025 | INFO (0.025, 0.050] | FAIL > 0.050); FB mid-point diagnostic prior ρ_B(13) = −0.646653 / ρ_B(14) = −0.657020, spread ≈ 0.0221.
4. **Effort**: 1 gate (multi-hour offline irrep build is the wall — schedule the build first, eigvalsh after).

#### S104-VIIBS-CLAUSE-B-WORDING (from CF-S104-HK-1; verbatim spec at `session-103-w2-workingpaper.md` §CF + housekeeping §B) — METHODOLOGY-class candidate
1. **What**: upgrade the §VII.BS clause-(b) scope annotation's bundle-exhaustiveness characterization "separate standing premise (Open Q6)" → "result" (both preconditions hold: W1-6 annotation `2c27b197…`; W2-1 rank-1 PASS `ac1dbb28…`).
2. **Inputs**: `sessions/permanent-results-registry.md` §VII.BS annotation surfaces (4); `computations/session-103/s103_nnu_bundle_exhaustiveness.npz` (rank-1 certificate).
3. **Gate**: artifact-existence + content-marker (upgraded wording present; frozen Stage-0 blockquote `e669ccd2…` byte-SHA UNCHANGED; theorem grade UNCHANGED) — designated-writer reviewed patch. M1–M4 check at plan-freeze: if classified METHODOLOGY, the gate-ID needs an orchestrator allowlist append (flag it in the plan block; do NOT self-append).
4. **Effort**: 0.1 gate (single reviewed prose patch; no compute).

### Waves 2–5 — gem-sourced gates (specs at `downloads/research-sweep-s103/GEM-TRIAGE.md` §3; READ YOUR RANK BLOCK — each carries the verified 4-field spec, canonical-state check (verbatim MCP keys), leverage, and suggested owner)

| Wave | Gate ID | GEM rank (assay line) | Class | One-line scope | Effort |
|:-----|:--------|:----------------------|:------|:---------------|:-------|
| W2 | S104-EULER-CLASS-J-DOUBLET | Rank 3 (line 74) | GEM-COMPUTE | Pfaffian/Euler invariant on the J-degenerate real doublet (Kwon-Yang two-real-band class); reuses S96 eigenvector machinery; the invariant the S96 Chern (≡0 by reality) could not see | 1 |
| W2 | S104-PAULI-G9-SUBCURVATURE | Rank 16 (line 239) | GEM-COMPUTE | γ9-graded spin-resolved sub-curvature: does the BDI Ω=0 null strengthen or crack; bundled with Rank 3 (same eigenvector path); feasibility-gated on γ9-machinery pinnability | 0.5–1 |
| W3 | S104-KRYLOV-KCP | Rank 11 (line 174) | GEM-COMPUTE | Lanczos b_n + Krylov-complexity-peak height on the cached D_K fold spectrum vs pinned Brody anchors (β=0.633 single-cell / β→0 CG(24)); rubric carries the saddle-dominated-scrambling caution (Rank 12) | 1 |
| W3 | S104-LOG-PERIODIC-IMS | Rank 13 (line 200) | GEM-COMPUTE | FFT of the on-disk HK-OSCILLATION-61 heat-trace oscillatory residual in ln t — complex-dimension Im(s) frequency test, orthogonal to the closed magnitude question | 0.5 |
| W4 | S104-NONLINEAR-MEMORY-IR-SLOPE | Rank 4 (line 89) | GEM-COMPUTE | Universal memory-tail IR slope Ω∝f^{3−2\|(3w−1)/(3w+1)\|} on the pinned w=1 stiff transit EOS, cross-checked vs blue n_T=+0.468; pre-registered INTERNAL-CONSISTENCY (NOT detectability — Row #7.audit-3 retirement honored) | 1–1.5 |
| W4 | S104-TYPEIV-EMT-BRIDGE-SPEC | Rank 5 (line 104) | GEM-BRIDGE | Proton-core Hawking-Ellis type-IV EMT ↔ substrate acoustic white-hole-interior signature; spec-first | 1 (after spec) |
| W5 | S104-AREA-MODULAR-GENERATOR-SPEC | Rank 6 (line 116) | GEM-BRIDGE | G_τ ≟ Δ^{it} operator identity on the emergent-horizon subalgebra (Connes-cocycle reading) | 1 (after spec) |
| W5 | S104-BMV-SN-CONTRAST-SPEC | Rank 9 (line 152) | GEM-BRIDGE | Substrate's derivable prediction for the gravitationally-mediated-entanglement / Schrödinger-Newton fork (the unmapped fourth box) | 1 (after spec) |
| W5 | S104-FRACTON-GOLDSTONE-SPEC | Rank 14 (line 215) | GEM-BRIDGE | Higher-moment-charge (fracton) reading of the immobile Leggett-DM Goldstone sector | 1 (after spec) |
| W5 | S104-LOOP-COUNTING-ENVELOPE-SPEC | Rank 15 (line 227) | GEM-BRIDGE | Lab-anchored loop-counting sibling of the L^{−α} truncation envelope; Level-2-binding-vs-identity discriminator; ADJACENT to the Wave-1 L_max CFs (joint-consideration flag) | 1 (after spec) |

**Bridge-spec discipline (Wave 4 item 2 + all Wave 5)**: each spec-gate names its construction at plan-freeze or the gate's PASS criterion is the honest NOT-DISPATCHABLE declaration (the S103 W4 lesson; `mechanical-closure-discipline.md` honesty discipline). A spec-gate's PASS = "construction nameable + 4-field compute spec emitted for S105"; FAIL = "construction unnameable — corridor documented closed at the spec level"; INFO per pre-registered intermediate.

---

## NOT plan gates (routed elsewhere this pass — do not duplicate)

- **Workshop track** (via `/rclab-workshop`, user-dispatched): (1) the W4 flip — modular-flavor 2506.23343 ↦ Missing-ingredient-#1, `neutrino-detection-specialist` × `connes-ncg-theorist`, R1/R2/R3 (GEM-TRIAGE §4); (2) κ-NCG opposite-sign n_s discriminator; (3) birefringence Berry-null vs emergent-channel. 
- **mack surface set** (dispatched): Row #85 multi-anchor σ-table; LIV-null row; saddle guard; area-quantum WATCH; X(2370)/g-2 notes; atlas-04 §IX Item-3.
- **Frontier notes** (held in atlas-08/EVOI; leverage ≠ tractability): arithmetic-Stokes/L-values; octonionic J₃(O)/E₇; Nahm-Bloch modularity; cosmic-dipole/sky-mode machinery gap.

## `--extra` fold: GEM-TRIAGE §7 routing summary (verbatim)

> The standing S104 forward set (from `session-103-workshop-schedule.md §"Planning Input Checklist"` + EVOI §6) is: **4 WP-CF computes** (CF-S104-W2-VIIAM-L11-ANCHOR, CF-S104-W3-SWMAX-MPMATH-EDGE, CF-S104-W5-BRANCH-IV-DIRECT-L1314, CF-S104-HK-1) + **the W4 fermion-mass item** (S103-NU-DELTA-A-FIBRE-GEOMETRY, was Q1-NO) + **the §6 standing gaps** (M_KK-DERIVATION, K_pivot/atlas-04 C2, τ_fold-RELAXATION, M8(c) likelihood-independence). This campaign adds the following, explicitly NON-DUPLICATING: [§7-A compute candidates Ranks 3/4/11/13/16 + bridge Ranks 5/6/9/14/15 — bucketed into the waves above] [§7-B workshops ×3 — workshop track above] [§7-C mack set — dispatched] [§7-D frontier notes — held]. **Composition note**: NONE of the 16 ranked gems duplicates the 4 standing WP-CFs; the ONE point of contact is Rank 15 ↔ the L_max-envelope CFs (adjacency, flagged for joint consideration, not duplication). The W4 flip does not duplicate the standing W4 item — it is the candidate construction that UNLOCKS it.

*(Full §7 text: `downloads/research-sweep-s103/GEM-TRIAGE.md` lines 378–407. Planners read their §3 rank blocks directly.)*
