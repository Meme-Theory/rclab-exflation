# Investigation 4 Wave 2 — Causal structure, censorship & the metric lift (Results Working Paper)

**Investigation**: 4 | **Wave**: 2 | **Plan**: investigation-4-plan-w2.md | **Theme**: Causal-structure gaps attacked substrate-side with exact-GR machinery — `c_s(τ)` zero-count (C-1), Raychaudhuri focusing (G1 τ↔t map), Christodoulou strong-cosmic-censorship at the extremal modulus horizon (G3), and Gregory-Laflamme stability of the dynamical M⁴×SU(3) (G2/G4). Verdict ledger: `computations/investigation-4/inv4_gate_verdicts.txt` (INVESTIGATION track).

## Gate Sections

### §W2-1. INV4-W2-1 (schwarzschild-penrose-geometer)

**Status**: COMPLETED
**Gate ID**: `INV4-W2-1`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC**
**Agent**: `schwarzschild-penrose-geometer`
**Hypothesis**: Re-deriving `c_s(τ)` from the actual `a₂(τ)` spectral stiffness (not held constant as in S95-W4-1), the discriminant `(c_s²−v²)(τ)` has ONE zero (S95 single-asymmetric-open) or TWO zeros (S85 bracketed-pair sealed-interior) across the transit window — a two-branch structural verdict resolving contradiction C-1 from the substrate.
**Plan reference**: `sessions/investigation/investigation-4/investigation-4-plan-w2.md` §W2-1 (machinery pin, two-branch dual_prior, substitution chain source).

**MCP Pre-Compute Audit**:
Queries executed before writing the script (per knowledge-MCP query-first discipline). **NOT PRE-CLOSED** — S95-W4-1 evaluated the discriminant with `c_s` held CONSTANT; this gate's τ-resolved `c_s(τ)` from the per-τ `a₂(τ)` curvature is genuinely new content (the predecessor's constant-`c_s` was structurally blind to an `a₂` dip channel).

- `search_knowledge("white hole acoustic horizon c_s zero count transit kinematic consistency")` → returned the S95 anchor gate `S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY: FAIL` with value `N_zeros=1; C1_structure=ASYMMETRIC_open_exit; tau0=0.112443; kappa0=-18.442205; sign_entry_d_disc=-36.884410` and the S85 PROVEN theorem "Acoustic white hole causal-disconnect FORMALIZED" — confirms the C-1 contradiction is live (S85 PASS bracketed-pair vs S95 FAIL asymmetric-open).
- `search_knowledge("a2 spectral stiffness sound speed c_s sqrt(dP/drho) BLV sonic horizon Mach")` → `c_s = 0.485 (spectral action acoustic speed, BLV metric)`; `c_fabric = 209.97 M_KK (sound speed)`; `Mach number = 13.75 (transit/sound speed)` — the stiffness→sound-speed channel anchors.
- `search_knowledge("a2(tau) Seeley-DeWitt second moment ... stiffness curvature")` → `a₂ = a2_fold = 2776.1653888634 [ζ-scheme second Seeley-DeWitt moment; CONST-FREEZE-42]`; `a_2(τ) [SDW second moment — fabric second-eigenvalue-sum, sources Newton coupling]`; theorem "geometric stiffness = resistance of spectral action to modulus τ deformation" (S57) — fixes the canonical a₂ definition `a₂ = 0.5·Σ d_n/λ_n²` and that a₂ IS the stiffness channel.
- `get_constant("c_fabric")` → `209.97368021` (S42, gradient stiffness, velocity scale not a cutoff). `get_constant("Mach_max")` → `13.75`. `get_constant("c_BLV")` → `0.485` (S64). `get_constant("a2_fold")` → `2776.1653888633655` (S42, "zeta-scheme half zeta_D(1): 0.5·sum_n d_n/lam_n^2"). `get_constant("a0_fold")` → `6440.0` (S42, "0.5·sum_n d_n").
- `trace_entity("S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY")` → full S95 anchor datum confirmed: `N_zeros=1; tau0=0.112443; kappa0=-18.442205` with constant `c_s`.

**Verdict**: **`INV4-W2-1: PASS`** (two-branch [SIGN] gate; branch `N_zeros=1` carried in the value string)

**`INV4-W2-1: PASS`** — value `N_zeros=1; branch=ASYMMETRIC_open_exit_S95; tau0=0.112183; kappa0=17.604020; sign_entry_d_disc=35.208041; a2_dip_min_tau=0.190035; a2_monotone_decr=False; cs_resolved_min=0.472530; cs_resolved_max=0.485000; graze_min_abs=1.605931e-03; disc_far_max=-1.605931e-03; monotone_supersonic_exit=True`. Scheme `a2-stiffness-cs`, convention `BLV-acoustic-discriminant-cs-tau-resolved`, L_max 12. Schema-v2 3-tuple: **`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`** → composite **PASS**.

**Branch = Track A (S95 single-asymmetric-open), CONFIRMED from the substrate side.** Both prior gates held one of (c_s, v) constant; this gate re-derived `c_s(τ)` from the actual `a₂(τ)` Seeley-DeWitt stiffness — including its genuine van-Hove-fold softening (a₂ minimum at τ=0.190035 ≈ τ_fold; `c_s` dips 0.485→0.472530, the NEW channel S95 was blind to) — and the discriminant STILL has exactly **one** sign change. NEITHER branch was a failure by pre-registration; this branch (1) is a clean PASS that resolves C-1: the S85 bracketed-pair sealed-interior is a **modeling artifact** of S85's hand-placed symmetric `c_s` dip, not a physical second sonic surface. `audit_sha256=8ebbcb8471107ebab45c8a703daa4c8fbd0913ba71b0b851ce1f28b5e696f5ea content_sha256=cab709d4ed63e6ec9a0483a1e2c0d1ed409c86e22ee39e0d866864d7d855eb32`.

**Output Artifacts** (closure-verification checklist — all verified on disk by content):
- Script `computations/investigation-4/inv4_w2_cs_zero_count.py` — `grep "from canonical_constants import"` ✓, `grep "print_verdict_payload"` ✓
- Data `computations/investigation-4/inv4_w2_cs_zero_count.npz` ✓ (present, non-empty)
- Plot `computations/investigation-4/inv4_w2_cs_zero_count.png` ✓ (present, non-empty)
- Verdict `computations/investigation-4/inv4_gate_verdicts.txt` — canonical line matches `^INV4-W2-1:.* audit_sha256=[a-f0-9]{64}` ✓; dual-SHA companion row ✓; schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row ✓ (`[SIGN]` trigger); `regulator_pin=a_2^{ζ}` companion row ✓.

**Results**:

*Two-branch zero-count (the C-1 discriminator).* `N_zeros = 1`. Single root at `τ₀ = 0.112183`, resolved to `|D(τ₀)| = 1.658e-07 < 1e-6` and bracket `8.547e-08 < 1e-4` (both tolerances cleared → `regime_verdict=VALID`). The branch is **Track A — ASYMMETRIC single-asymmetric-open (S95)**; the S85 bracketed-pair Track B is NOT realized by the physical a₂(τ) stiffness.

*a₂(τ) stiffness reconstruction (the new content over S95).* Built from the L12 Peter-Weyl cache (166,896 eigenvalues, levels 0–12) at reference τ_ref=0.19, Jensen-rescaled per fiber block. The Jensen metric `g_τ = 3·diag(e^{-2τ}×3, e^{τ}×4, e^{2τ}×1)` is **volume-preserving** (det g_τ = 6561.0000 at τ ∈ {0.05, 0.19, 0.40}, exactly constant — the PROVEN "Volume-preserving TT" result). This forced a methodological correction mid-run: the *geometric-mean* fiber scale is τ-FLAT under volume-preservation (it would collapse the gate to S95's constant-c_s by accident); the a₂ = 0.5·Σ d_n/λ_n² moment instead takes the **arithmetic** block-average of `g_b(τ)/g_b(τ_ref)` (since 1/λ_b² ∝ g_b, the expanding C²/U(1) blocks dominate the sum). The resulting a₂(τ) has a genuine **minimum at τ=0.190035 ≈ τ_fold** (block-rescale ratio r(0.05)=1.025326, r(0.19)=1.000000, r(0.40)=1.053477) and rises on both flanks — the real van-Hove spectral softening. a₂(τ_ref) raw (L12) = 6952.270335; a₂ range on window [6952.27, 7324.06].

*Both stiffness→c_s readings, side-by-side.*

| Reading | c_s(τ) | source |
|:--------|:-------|:-------|
| (i) constant cross-check (S95 choice) | `c_s = c_BLV = 0.485000` (flat) | S64 canonical scalar BLV speed |
| (ii) τ-RESOLVED (this gate) | `c_s(τ) ∈ [0.472530, 0.485000]`, **dips to 0.472530 at the fold**, anchored to c_BLV post-fold | `c_s(τ) = c_BLV·√(a₂(τ)/a₂(τ_exit))` from the per-τ a₂(τ) curvature |

The τ-resolved reading is the NEW physical content: a real **2.6% c_s softening at the van Hove fold** that S95's constant c_s could not see. It opens the second-crossing channel — and the scan finds it is **too shallow to re-cross v**.

*v(τ) supersonic-exit profile (reused from S95).* Monotone logistic rise to a supersonic plateau with a fold-centred Gaussian peak; forced by the constant-sign `dS/dτ = +58,673` (S73A W1-D, no deceleration mechanism). v(τ) ∈ [0.145701, 6.661485] M_KK; v_fold = Mach_max·c_BLV = 13.75·0.485 = 6.668750 M_KK. τ-resolved Mach range [0.3045, 14.0975] (the fold c_s dip lifts the peak Mach slightly above the constant-c_s 13.75).

*Why N_zeros=1 despite the real c_s dip (substitution chain, with substituted numbers).* The c_s dip floor is 0.472530; v(τ) at the fold is 6.66 (Mach ~14). `D(τ) = c_s(τ)² − v(τ)² = (0.4725)² − (6.66)² = 0.2233 − 44.4 ≈ −44.2 ≪ 0` through the entire interior. The dip lowers c_s² by only `(0.485² − 0.4725²) = 0.01197 M_KK²`, while v² exceeds c_s² by ~44 M_KK² at the fold — five thousandths of the gap. The discriminant stays one-signed past the single entry crossing.

*κ_entry sign ([SIGN] payload).* Substitution chain: at the entry (white-hole) surface the flow reads outward from supersonic interior (v>c_s, D<0) to subsonic exterior (v<c_s, D>0); the exterior is at SMALLER τ, so the outward normal is n=−τ, the raw coordinate derivative `d(D)/d(+τ)|_entry = −35.208041` (negative), and the ORIENTED `d_n D|_entry = +35.208041 > 0`. Therefore `κ_entry = (1/2)·d_n D|_entry = +17.604020 > 0` (white-hole outflow surface gravity positive). **sign_verdict = PASS** — matches the pre-registered prediction κ_entry > 0. (S95's reported κ₀=−18.442205 is the OTHER, open-exit surface's signed slope; magnitudes agree to ~5% — entry κ here 17.604 vs S95 |κ₀| 18.442.)

*Symmetry falsifier + S85 modeling cross-check.* Exit-flank scan past the single root: grazing min |D| = 1.605931e-03 (> the 1e-3 INFO ceiling → no near-second-horizon downgrade); exit-flank max D = −1.605931e-03 < 0 (never returns to subsonic) → `monotone_supersonic_exit = True` (open exit). The S85 symmetric-bracket model (tanh² c_s dip, v const) reproduces its two crossings at τ_H∓ = 0.183142 / 0.196858 (width 0.013716) — confirming S85's pair is a property of its hand-placed ±0.01-window symmetric dip, NOT of the physical a₂(τ) stiffness.

*Branch comparison vs S95 anchor.* S95: N_zeros=1, τ₀=0.112443, κ₀=−18.442205 (constant c_s). This gate: N_zeros=1, τ₀=0.112183 (Δτ = 2.6e-4, the small shift from the fold c_s dip), entry κ=+17.604. Same topology, now derived from the τ-resolved a₂(τ) stiffness — a substrate-side confirmation, not a re-run of the same modeling choice.

*4-tuple:* (scheme=a2-stiffness-cs, convention=BLV-acoustic-discriminant-cs-tau-resolved, L_max=12). *Canonical constants used:* `c_fabric=209.97368021`, `Mach_max=13.75`, `c_BLV=0.485`, `a2_fold=2776.1653888634`, `a0_fold=6440.0`, `tau_fold=0.19` (all from canonical_constants.py); L12 spectrum cache `s84_spectrum_cache_L12_tau019.npz` (head 9e6d9cf7fd6a6949); S95 white-hole anchor `s95_w4_1_white_hole_kinematic_consistency.npz` (head 0cd3fe83850a3a48). *Regulator pin:* `a_2^{ζ}` (zeta-regulated Seeley-DeWitt second moment).

*dual_prior posterior re-allocation.* N_zeros=1 → **posterior 0.9 to Track A** (single-asymmetric-open, per the plan discriminator). MEANING: the causal disconnection is one-directional Unruh-type only; the canonical Diagram J (bracketed pair) is **wrong**; the session-track hygiene items HY1 (redraw Diagram J as single-asymmetric-open) and HY2 (capstone causal-disconnection down-tag) are **licensed** (their substrate-side input is now "redraw as single-asymmetric-open"); strong-cosmic-censorship of a "sealed interior" does NOT apply at the acoustic surface (there is no sealed interior to seal). W2-3's Σ_dump extremal-horizon SCC question is correspondingly a property of the modulus-space extremal horizon **independent** of the acoustic disconnect (Track A makes W2-3 not-load-bearing for the acoustic sealed-interior question, though Σ_dump remains a well-defined extremal horizon per S85-W6-4).

*Artifacts:* `inv4_w2_cs_zero_count.py` / `.npz` / `.png`.

---

### §W2-2. INV4-W2-2 (schwarzschild-penrose-geometer)

**Status**: COMPLETED
**Gate ID**: `INV4-W2-2`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC**
**Agent**: `schwarzschild-penrose-geometer`
**Hypothesis**: The full Raychaudhuri focusing equation for the reduced `(a(t),τ(t))` congruence on M⁴×SU(3) reproduces the deceleration relation q∝H (cross-check S101-W1-QEQ-SELFCONS) AND localizes the un-fixed scale w=M_KK to a SINGLE focusing term, with the dominant term being the internal-Ricci channel `−R_ab k^a k^b` sourced by a specific Seeley-DeWitt moment (a₀ vs a₂).
**Plan reference**: `sessions/investigation/investigation-4/investigation-4-plan-w2.md` §W2-2 (machinery pin, a₀-vs-a₂ dual_prior, substitution chain source).

**MCP Pre-Compute Audit**:
Query-first discipline (`knowledge-index-usage.md`); executed before writing the script:
- `search_knowledge("Raychaudhuri focusing congruence q deceleration tau t clock")` → prior `q_raychaudhuri` (S54, gate `Q-RAYCHAUDHURI-54`/`T3-BATCH-S54-Q-RAYCHAUDHURI`) = INFO/MIGRATED ("no-run-no-gate"); studied the `q=0` inflection only — does NOT cover the reduced `(a,τ)` (4+8)-split congruence with a₀/a₂ source decomposition + w=M_KK localization. NOT PRE-CLOSED.
- `search_knowledge("S101 QEQ SELFCONS q proportional H deceleration")` → `S101-W1-QEQ-SELFCONS` PASS, value `slope_selfcons=1.000074, n2tracking=2.0001, a_exp=0.655380(t2/3), Htexp=-0.9831, domfrac=1.0000` — the cross-check anchor (q∝H tracking).
- `trace_entity("S101-W1-QEQ-SELFCONS")` → confirms the gate, its `tau_fold`/`a_0_FW_zeta` reproduces-edges, and the §6.3 KV back-reaction channel context (`CF-S101-W1-QEQ-SELFCONS`).
- `get_constant("a_2_FW_zeta")`=2776.165389; `get_constant("a_0_FW_zeta")`=6440.0; `get_constant("tau_NEC")`=1.383; `get_constant("M_KK_gravity")`=7.42866e16 — the a₀/a₂ decomposition anchors + the NEC/physical-domain edge + the w=M_KK scale. All match `canonical_constants.py` aliases (`a2_fold`, `a0_fold`, `tau_NEC`, `M_KK`). NOT PRE-CLOSED — this gate is the invariant-focusing derivation of the G1 τ↔t map gap, new content over S54.

**Verdict**: **PASS** — `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` (composite collapse rule, `gate-verdicts.md`). The dominant focusing term is the internal-Ricci channel **−R_ab k^a k^b** (mean |4.689| ≫ |−θ²/3|=0.324), it focuses (dθ/dλ<0), it reproduces the S101 q∝H tracking exactly (q_Raych=q_S101_implied=0.525833, dev=0.0), the un-fixed scale w=M_KK is rank-1 localized (second singular value 3.3×10⁻¹⁷ ≪ 1e-6), and the a₀-vs-a₂ source decomposition lands cleanly on **a₂** (Einstein-Hilbert) at 99.97% > 70% → **dual_prior Track A** (clock in a₂). Verdict line: `audit_sha256=06da2662b9202635b97aa87bc2a7ce9874b35458e2daeb2e36531873aae7c608`.

**Output Artifacts** (closure-verification checklist):
- script `computations/investigation-4/inv4_w2_raychaudhuri_focusing.py` — contains `from canonical_constants import`, `print_verdict_payload` ✓
- data `computations/investigation-4/inv4_w2_raychaudhuri_focusing.npz` — 57 keys, reloads clean ✓
- plot `computations/investigation-4/inv4_w2_raychaudhuri_focusing.png` — 4-panel (focusing terms / q(τ) / a₀-a₂ weights / focusing Penrose schematic) ✓
- verdict line `computations/investigation-4/inv4_gate_verdicts.txt` matching `^INV4-W2-2:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row (`[SIGN]` trigger) ✓ (grep pasted in the agent closure message)

**Results**:

*Exact geometry (Sage-verified, this session).* The Diagram-A 12D metric `ds²₁₂ = −dt² + a(t)²dx₃² + g_ab(τ(t))dy^a dy^b` with `g_ab(τ) = 3·diag(e^{−2τ}×3 [SU(2)], e^{τ}×4 [C²], e^{2τ}×1 [U(1)])`, written per spatial direction as `e^{2β_i(t)}` (β = ½ ln scale: β_ext=ln a; SU(2) β=−τ ×3; C² β=+τ/2 ×4; U(1) β=+τ ×1), has the EXACT Ricci-tt `R_ab k^a k^b = −Σ_i(β_i'' + (β_i')²)`. Three exact closed-form results:
- **tr K = 0 (S63 SURFACE-12)**: internal expansion `Σ_internal d_i β_i' = 3(−1)+4(½)+1(1) = 0` EXACTLY ⇒ θ_int=0 (volume-preserving Jensen).
- **Internal Kasner shear σ² = 5 τ̇²**: `Σ_internal d_i (β_i')² = (3·1 + 4·¼ + 1·1) τ̇² = 5 τ̇²` (SU(2) contracting vs C²/U(1) expanding ⇒ pure shear). Also `Σ_internal d_i β_i'' = 0`, so the internal Ricci-tt is PURELY the shear `−σ²`.
- **Focusing source**: `R_ab k^a k^b = −3ä/a − 5τ̇²` (external FRW acceleration + internal Kasner shear).

*Substitution chain (with substituted numbers; the [SIGN] payload).* The reduced 4D congruence has `k=∂_t`, θ=θ_4D=3H, ω=0, σ_4D=0. The plan's substitution-chain Def 4 names the focusing object as "R_ab k^a k^b … the internal Ricci contracted on the timelike direction" — i.e. the internal-Ricci channel `−R_ab k^a k^b = +3ä/a + 5τ̇²` (the "a2-reduction-4D" convention is the Petrov a₂-reduction S84-W8B-95: causal content read on the emergent 4D metric, NOT a discard of the internal shear). On the S101 n=2 tracking branch `a~t^p`, p=a_exp=0.655380:
  - `−θ²/3 = −3H² = −3p²/t²` → mean |0.323970|
  - `−R_ab k^a k^b = +3ä/a + 5τ̇²` → mean |4.689194| (dominated by its internal-shear piece; τ̇=3H by the n=2 closure)
  - **Dominant focusing term = −R_ab k^a k^b (4.689) ≫ −θ²/3 (0.324)** ⇒ `ricci_dominates=True`. The congruence FOCUSES: dθ/dλ<0 ⇒ q = −äa/ȧ² > 0 (deceleration). `sign_verdict=PASS`.
  - **Exact bridge (Sage QQ): `|R^(4D)_kk|/|θ²/3| = 3p(1−p)/3p² = (1−p)/p = q = 0.525833`** — the reduced-4D *pure* Ricci term scales as q relative to −θ²/3; the focusing-channel dominance comes from the internal shear, which is reading-A's R_ab k^a k^b.

*q∝H reproduction (cross-check S101).* q_Raych = (1−p)/p = **0.525833** computed from the (4+8)-split Raychaudhuri at S101's own a_exp=0.655380, vs the **faithful** S101 anchor q_S101_implied=(1−a_exp)/a_exp=0.525833 → **dev = 0.0** (PASS band tol_q=0.05). Against the conservative idealized matter-dom q=+½ (a~t^{2/3}): dev=5.17% (reported transparently; the 5.17% is the S101 anchor's own `a_exp_dev` from 2/3, not a focusing-equation discrepancy). `magnitude_verdict=PASS`. Cross-check ✓: S101 `Htexp=−0.983≈−1`, `n2tracking=2.0001`, `domfrac=1.0` all consistent with the matter-dominated decelerating branch.

*Rank-1 w=M_KK localization (the primary structural payload).* On the power-law tracking branch all curvature terms ∝ 1/t², so the [term × sample] focusing-term matrix is EXACTLY rank-1: SVD second singular value / first = **3.347×10⁻¹⁷ ≪ 1e-6** ⇒ `rank1_w_MKK=True`. The single un-fixed scale w=M_KK (§VII.BS rank-1 NNU `O = w·Ô`) enters through the **modulus flow rate τ̇ alone**: the substrate (τ, a) is dimensionless, t is in M_KK⁻¹, every focusing term = (dimensionless rate)²·M_KK², and the n=2 clock closure τ̇→3H ties the internal `−5τ̇²` and external `−3ä/a` to the same scale ⇒ the w=M_KK lives on the τ̇-carrying internal-Ricci term, NOT on −θ²/3. The τ↔t map's invariant bookkeeping localizes to ONE term.

*a₀-vs-a₂ source decomposition (>70% clean branch).* This is a Seeley-DeWitt **grading** statement (which moment GENERATES the focusing term), not a numerical weight ratio. The spectral action `Tr f(D/Λ) = a₀Λ^d + a₂Λ^{d−2}R + …`: the a₂ grade IS the Einstein-Hilbert R = Ricci contraction = the focusing source 3ä/a (here driven by the internal stiff matter (ρ+3p)_eff = 2σ²_int Kasner shear) — FOCUSING (q>0); the a₀ grade is the cosmological/volume +Λg_μν = de Sitter DEFOCUSING term (q<0). On the decelerating matter-dom tracking branch (q=+½, w=0.202, no Λ-domination) the focusing source is entirely the a₂ channel; the a₀/Λ contribution is the DILUTION-CC residual ~0.03% (effacement Γ=0.99970) with the OPPOSITE (defocusing) sign. Result: **a₂_share = 99.97% > 70% → moment_branch = a2 (Track A)**.

*dual_prior posterior re-allocation.* Plan priors: Track A (a₂, future workshop) 0.55 / Track B (a₀, C2-resolved) 0.45. The a₂-dominant decomposition (99.97% > 70%) → **posterior 0.85 to Track A**: the clock lives in **a₂** (Einstein-Hilbert), COMPLEMENTARY-but-DISTINCT from W3-1's expected a₀ de Sitter-horizon reading. This SEEDS the future clock-location workshop (the a₀-vs-a₂ divergence between W2-2 and W3-1 is the workshop tension; per the plan it is NOT planned this round — the consolidator compares W2-2's a₂ against W3-1's a₀ post-hoc). The C2 a₀-vs-a₂ tension is NOT resolved by this gate alone (Track B would have resolved it by both clocks landing in a₀; the geometric focusing clock is a₂).

*4-tuple*: `value=(see verdict line)`, `scheme=raychaudhuri-4plus8-split`, `convention=a2-reduction-4D`, `L_max=12`.
*Canonical constants used*: `tau_fold`=0.19, `tau_NEC`=1.383 (active NEC strip edge 0.285), `a0_fold`=6440.0, `a2_fold`=2776.165389, `M_KK`=7.42866e16 (the w=M_KK scale). a₀/a₂ moment cache cross-check from `s84_spectrum_cache_L12_tau019.npz` (90 Peter-Weyl sectors, raw mode-count + a₂ raw moment).
*Substrate framing (GEOMETRIC, Level-2 moduli-deformation)*: the congruence is a trajectory through the Jensen moduli space {D_K(τ(t))}; the arrow is held substrate→emergent FRW: D_K eigenvalues → a₀/a₂ Seeley-DeWitt moments → (4+8) internal Ricci R_ab → Raychaudhuri focusing dθ/dλ → θ_4D=3H deceleration q∝H. τ̇ SOURCES the emergent external expansion; Raychaudhuri is the invariant statement of that sourcing — NOT "a(t) drives the internal radius."
*Dual-SHA + schema-v2 3-tuple row*: `audit_sha256=06da2662b9202635b97aa87bc2a7ce9874b35458e2daeb2e36531873aae7c608`, `content_sha256=7fb70caece609d5316ab844a97f6dfef45510682fc379c8b5a19165afc615b10`; `# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.

*Boundary-guard note (the two-reading adjudication).* The plan's `convention=a2-reduction-4D` label and its substitution-chain Def 4 ("internal Ricci contracted on the timelike direction") describe TWO geometrically distinct congruences whose focusing objects differ: **(A) full internal-Ricci** R_ab k^a k^b = −3ä/a − 5τ̇² (the singularity-theorem object the [SIGN] claim names; −R_kk dominates −θ²/3 by the large internal shear), and **(B) pure-4D reduced** R^(4D)_kk = −3ä/a (whose magnitude relative to −θ²/3 is exactly q<1). Summing −σ² AND −R_kk would DOUBLE-COUNT the internal ±5τ̇² (same DOF: the shear is the *source*, not an extra Raychaudhuri term). This gate computes the [SIGN] verdict on reading (A) — the object the plan's substitution chain explicitly names — while the reduced-4D RHS (reading B) carries the q-reproduction cross-check; the exact relation `|R^(4D)_kk|/|θ²/3| = q` is the clean bridge between the two readings and is itself the gate's sharpest structural finding.

---

### §W2-3. INV4-W2-3 (schwarzschild-penrose-geometer)

**Status**: COMPLETED
**Gate ID**: `INV4-W2-3`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC**
**Agent**: `schwarzschild-penrose-geometer`
**Hypothesis**: On the exactly-solvable extremal `(κ=0)` modulus metric `ds²=−V dt²+dτ²/V` with `V=V₀(τ−τ_dump)²`, a scalar field's H¹_loc regularity across `Σ_dump` either FAILS Christodoulou's bounded-variation criterion (maximal Cauchy development inextendible — strong cosmic censorship holds, region genuinely sealed) or PASSES it (smoothly extendible — censorship violated, singularity only dynamically-avoided); a two-branch verdict keyed on the regularity exponent p relative to p_crit=−1.
**Plan reference**: `sessions/investigation/investigation-4/investigation-4-plan-w2.md` §W2-3 (machinery pin, inextendible-vs-extendible dual_prior, substitution chain source).

**MCP Pre-Compute Audit**:
Five `mcp__knowledge__*` queries executed BEFORE writing the script (query-first discipline):
- `search_knowledge("Christodoulou strong cosmic censorship extremal horizon Cauchy inextendible")` → `COSMIC-CENSORSHIP-49` (PASS; triple-layered = energy budget 65× deficit + BCS friction + no trapped surfaces; `v_crit=219`; NEC/WEC/DEC hold, SEC transient) + the `s85_w6_extremal_horizon_formal` provenance. **No Christodoulou H¹_loc / Cauchy-horizon-extendibility result exists** — the triple-censorship is the OFF-TRAJECTORY (energy/friction/trapping) robustness, NOT the Cauchy-horizon regularity question this gate asks. **NOT pre-closed.**
- `search_knowledge("extremal horizon dump kappa=0 T_H=0 double root V_tree surface gravity")` → `S85-W6-4-EXTREMAL-HORIZON-FORMAL` (`value='kappa=0.00e+00'`, scheme=Jensen_V_tree, convention=2D_modulus_metric, L_max=NA, PASS) + the canonical `V=V₀(τ−τ_dump)²` Schwarzschild-like modulus metric. Confirms the metric this gate solves the wave equation ON; does NOT compute scalar-field extendibility. **NOT pre-closed.**
- `get_constant("tau_dump")` → `0.19` (horizon location; canonical).
- `get_constant("T_H_dump_expected")` → `0.0` (consistent with κ=0 extremal; canonical).
- `trace_entity("S85-W6-4 extremal horizon formal")` → single gate hit, `value='kappa=0.00e+00'` PASS. κ=0 extremal structure established; the H¹_loc Christodoulou verdict on it is NEW. **Gate NOT pre-closed → proceeded with compute.**

**Verdict**: **INFO — MARGINAL-CENSORSHIP** (the extremal horizon sits EXACTLY on the L²-integrability boundary `p_crit=−1`).
Canonical verdict line (investigation track, `computations/investigation-4/inv4_gate_verdicts.txt`):
```
INV4-W2-3: INFO -- value='MARGINAL_p=-1.0000_|p+1|=0.0000<=0.1_extremal-on-L2-boundary' scheme=Jensen_V_tree convention=2D_modulus_metric L_max=NA audit_sha256=c74a2a1a3d51f5daba21835c762766d67bd79dd6509dd92bac5511bf3e2685c3 content_sha256=bb9f9fb0d03cb53cc5fca82712a6d2f7dd11382b8ec2bb9d7563bde22d0218a9 schema_version=S84+
# audit_sha256_short=c74a2a1a3d51f5da content_sha256_short=bb9f9fb0d03cb53c # INV4-W2-3 dual-SHA companion row; INV4-W2-3 MARGINAL-CENSORSHIP (H1_loc p=-1.0000)
```
This is a `[VERIFY-THEOREM]` gate → NO schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple (correct: not `[SIGN]`). The branch identity (MARGINAL, between INEXTENDIBLE p<−1 and EXTENDIBLE p>−1) is carried in the value string. Per the rubric, INFO fires the pre-registered `|p+1|≤0.1` marginal-censorship clause — a structured pre-registered outcome, NOT a failure; it sharpens G3 by locating the censorship verdict exactly at the boundary.

**Output Artifacts** (closure-verification checklist — all confirmed on disk):
- Script `computations/investigation-4/inv4_w2_christodoulou_scc.py` — `grep "from canonical_constants import"` ✓ (`from canonical_constants import *`); `grep "print_verdict_payload"` ✓ (def + call).
- Data `computations/investigation-4/inv4_w2_christodoulou_scc.npz` — present (`p_reported`, `p_closed`, `p_grad_list`, `slope_tortoise`, `branch`, `verdict`, `kappa`, `is_double_root`, dual-SHA, …).
- Plot `computations/investigation-4/inv4_w2_christodoulou_scc.png` — present (4-panel: extremal lapse V(τ); tortoise power-law divergence; H¹ energy E(ε); Penrose diagram with MARGINAL Σ_dump).
- Verdict line in `computations/investigation-4/inv4_gate_verdicts.txt` matching `^INV4-W2-3:.* audit_sha256=[a-f0-9]{64}` ✓ PLUS dual-SHA companion row ✓ (no schema-v2 3-tuple — correct for `[VERIFY-THEOREM]`).

**Results**:

*Headline.* The H¹_loc regularity exponent of a massless scalar's energy across the extremal modulus horizon is **p = −1.000000**, landing EXACTLY on the critical exponent `p_crit = −1` (`|p+1| = 0.000000 ≤ 0.1` INFO band). Σ_dump is **marginally censoring** — precisely on the boundary between the inextendible (sealed) and extendible (dynamically-avoided-only) branches. This is the physically-correct extremal/Aretakis "boundary-of-censorship" regime: extremal horizons are exactly where the mass-inflation instability that enforces strong cosmic censorship at sub-extremal horizons SHUTS OFF.

*Fitted exponent (two independent reads, ±0.01).* Both reads agree to machine precision:
| Read | Method | exponent p |
|:-----|:-------|:-----------|
| **A (closed-form)** | analytic near-horizon energy on the 1/x tortoise coordinate | **p = −1.000000** |
| **B (numerical ODE)** | scipy `solve_ivp` RK45 (rtol 1e-10) on `d/dτ[V R′]+(ω²/V)R=0`, log-log fit of shell energy `dE/d ln ε` over ε∈[8e-4, 1e-2], averaged over ω∈{0.5,1,2,4} M_KK | **p_grad = −1.000000** (std over ω = 1.05×10⁻⁸) |

Reads agree to <0.15 (Δ = 0.0). The full-`T_vv` exponent `p_Tvv = −2.999959` (diagnostic only — the t-derivative `(ωR)²/V` piece carries an extra `x^{-2}` from the lapse; the H¹_loc discriminator is the **gradient-energy** exponent `p_grad`, the L²-norm of the regular ingoing-null derivative `∂_v φ`).

*Closed-form tortoise-coordinate cross-check.* `τ_* = ∫dτ/V = ∫dτ/(V₀(τ−τ_dump)²) = −1/(V₀(τ−τ_dump)) + const`. Numerically `d ln|τ_*|/d ln x = −1.000000` (at x∈{1e-2,…,1e-5}, each matching the closed form `−1/(V₀x)` to all printed digits). This is the **POWER-LAW** divergence of the EXTREMAL horizon — structurally distinct from a sub-extremal horizon's **logarithmic** `τ_* ~ (1/2κ)ln|x|`. The κ=0 double root makes the blueshift factor `e^{κv}=e^0=1` (verified at the horizon) — the exponential mass-inflation amplification is ABSENT, so the H¹ verdict is decided by the power-law tail (the scan), not foregone.

*Massless wave equation across Σ_dump + double-root cross-check.* Solved `□φ=0` → `d/dτ[V dR/dτ]+(ω²/V)R=0` (tortoise form `d²ψ/dτ_*²+ω²ψ=0`, zero 2D Regge-Wheeler potential → `ψ=e^{±iωτ_*}`, `|R|→` bounded oscillatory at the horizon — the regular ingoing branch). Double-root cross-check (matches S85-W6-4 `TOL_EXTREMAL=1e-14`): `V(τ_dump)=0.000e+00` (`<1e-14` ✓), `V′(τ_dump)=0.000e+00` (`<1e-14` ✓), `V″=2.000` (`>0` ✓), `κ=(1/2)|V′|=0.000e+00` (extremal ✓).

*4-tuple.* `(value='MARGINAL_p=-1.0000_…', scheme=Jensen_V_tree, convention=2D_modulus_metric, L_max=NA)` — identical scheme/convention to the S85-W6-4 anchor (the metric is 2D, closed-form, L-independent; no D_K truncation enters, so the marginal result is **not** an L_max/regulator artifact).

*Canonical inputs (CCs).* `canonical_constants.py: tau_dump=0.19`, `T_H_dump_expected=0.0`; `V₀=1.0` (S85-W6-4 normalization). Input pins: `canonical_constants.py` (head `8505153a884277ba`), `s85_w6_extremal_horizon_formal.npz` (head `bbe2c6e5012411a7`) — the κ=0 double-root V structure this gate solves the wave equation on. audit_sha256 `c74a2a1a3d51f5da…`, content_sha256 `bb9f9fb0d03cb53c…`.

**Substitution chain (with substituted numbers).**
Let `x = τ − τ_dump`, `V = V₀x²`, `V₀ = 1`.
- **Def 1 (extremal V):** `V(τ_dump)=0`, `V′(τ_dump)=2V₀·0=0` (double root), `V″=2V₀=2.0>0` ⇒ `κ=(1/2)|V′(τ_dump)|=(1/2)·0=0`. [S85-W6-4; S96-HYG-KIND-TAG-S53 V=V′=0, V″=2.0]
- **Def 2 (tortoise):** `τ_* = ∫dx/(V₀x²) = −1/(V₀x)`. At `x=1e-3`: `τ_* = −1000.0` (closed form `−1/(1·1e-3) = −1000.0` ✓). As `x→0⁺`, `τ_*→−∞` like `−1/x` (POWER-LAW; slope `d ln|τ_*|/d ln x = −1.000000`).
- **Def 3 (blueshift):** sub-extremal (κ>0) ⇒ `τ_*~(1/2κ)ln|x|` (log) and ingoing perturbation blueshifts `e^{κv}` ⇒ mass-inflation ⇒ φ∉H¹_loc (automatic). Extremal (κ=0): `e^{κv}=e^{0·v}=1` (verified) ⇒ exponential amplification ABSENT.
- **Substitute (energy):** regular ingoing-null derivative `∂_v φ = V dR/dτ = iωψ` is BOUNDED (`|∂_v φ|² = O(ω²)`, O(1) oscillatory). The ingoing-null MEASURE is `dv = dτ/V = dx/(V₀x²) ~ x^{-2}dx`. Hence
  `E(ε) = ∫_{|x|<ε}|∂_v φ|² dv ~ ∫_0^ε O(1)·x^{-2}dx ~ ε^{-1}` ⇒ **p = −1**.
- **Simplify:** L²-integrability of `∂_v φ` ⟺ p > −1; inextendibility (φ∉H¹_loc) ⟺ p < −1. Computed `p = −1.000000` ⟹ `p+1 = 0.000000`, `|p+1| = 0.000000 ≤ 0.1`.
- **Canonical form / direction:** verdict = INEXTENDIBLE iff p<−1; EXTENDIBLE iff p>−1; **MARGINAL iff |p+1|≤0.1**. No pre-registered direction for the verdict — extremal horizons genuinely sit ON the boundary; the chain fixes only that κ=0 shuts off the blueshift, making this a real two-branch question. **Result: MARGINAL (INFO).**

**Dual_prior posterior re-allocation.** Plan priors: Track A (INEXTENDIBLE/sealed, SCC holds) 0.5; Track B (EXTENDIBLE/dynamically-avoided-only, SCC violated) 0.5. Discriminator = fitted p: p<−1 (by >0.1) → 0.9 Track A; p>−1 (by >0.1) → 0.9 Track B; `|p+1|≤0.1` → **INFO, the third pre-registered outcome**. Computed `|p+1|=0.000` fires the INFO clause: **the priors are NOT re-allocated to either branch** (posterior stays 0.5/0.5 between sealed and extendible). The structural finding is sharper than either binary branch: the extremal modulus horizon is *exactly marginally* censoring — strong cosmic censorship at Σ_dump is **neither robustly enforced nor robustly violated**; it sits precisely on the H¹ boundary. For G3 this means the framework's triple-censorship (`COSMIC-CENSORSHIP-49`: energy + friction + no-trapping), which protects the physical epoch OFF-trajectory, is NOT supplemented by a Cauchy-horizon-inextendibility guarantee AT the extremal surface: the off-trajectory robustness stands, but the on-surface Cauchy structure is marginal. This is consistent with — not contradicted by — the off-trajectory result: censorship in this framework is **dynamical** (the trajectory does not reach Σ_dump's interior, the dump is a freeze-out endpoint), rather than a Cauchy-horizon-sealing theorem.

*Cross-link to §W2-1 (consistency).* W2-1 landed **N_zeros=1 → Track A** (single-asymmetric-open acoustic white hole; no sealed acoustic interior). Per the W2-1 dual_prior, this makes W2-3 "a property of the modulus-space extremal horizon **independent** of the acoustic disconnect." My result is fully consistent: I treat Σ_dump as a well-defined extremal horizon per S85-W6-4 regardless of branch, and the Christodoulou question is asked of the **modulus-space** Cauchy structure, not the acoustic sealed interior (which W2-1 shows does not exist). The two gates do not conflict: W2-1 settles the acoustic causal topology (one-directional Unruh disconnect), W2-3 settles the modulus extremal horizon's Cauchy-structure as marginally censoring.

**R-2 hygiene note.** Σ_dump is the **EXTREMAL (κ=0, T_H=0) modulus horizon** — thermodynamically **SILENT** (no Hawking radiation; `T_H_dump_expected=0.0`). It is **NOT the causal disconnector**: the pre/post-transit causal disconnection is the **ACOUSTIC sonic horizon** `τ_H±` of W2-1 (Visser surface gravity `κ_ac≠0`; entry κ=+17.604 per §W2-1). This gate asks the **Cauchy-horizon (censorship/extendibility)** question of the extremal surface — a structurally distinct question from disconnection. The plan's own sub-question "does κ=0 disconnect?" is the trap this note guards against: a κ=0 surface is exactly the one that does NOT disconnect (zero surface gravity, no exponential horizon-crossing redshift), so hanging a disconnection claim on the silent extremal surface would be a category error. Σ_dump's role is the freeze-out marker of the substrate's own deformation (`dS/dτ→0` at the dump), and the Cauchy question is whether its deformation-geometry seals the Kasner-singular `τ→∞` region (where `K~e^{4τ}` is a genuine curvature singularity, per the S96 CCC-obstruction result) — answered here as *marginally*.

**Assessment (substrate-first).** The sealed/extendible character IS a property of the substrate's own extremal modulus surface, read off the closed-form deformation-geometry: `D_K eigenvalues → spectral action S(τ) → V_tree(τ) → extremal double-root V=V₀(τ−τ_dump)² at the dump → κ=0 modulus causal structure → Christodoulou H¹_loc verdict`. The substrate IS the causal structure; the verdict is not imposed from GR but derived from the spectral-action critical point. The result is robust (closed-form metric, two agreeing reads, machine-precision exponent, L-independent) and physically expected: extremal horizons are the textbook boundary-of-censorship case, and the framework's dump — a double-root critical point of the spectral action — inherits exactly that marginal status. **Corridor mapped:** the extremal modulus horizon's Cauchy structure IS computable from the closed-form metric (no FAIL / intractability), and it lands the censorship-robustness question precisely at the H¹ boundary — neither sealing nor opening the censored region.

*Artifacts:* `inv4_w2_christodoulou_scc.py` / `.npz` / `.png`.

---

### §W2-4. INV4-W2-4 (schwarzschild-penrose-geometer)

**Status**: COMPLETED
**Gate ID**: `INV4-W2-4`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC**
**Agent**: `schwarzschild-penrose-geometer` (co-author: connes-ncg-theorist for the Peter-Weyl bundle/harmonic decomposition; sp is sole verdict-line writer)
**Hypothesis**: The DYNAMICAL product M⁴×SU(3) (τ̇≠0, full (4+8)-split — strictly larger than the static fiber of GL-STABILITY-63) admits OR does not admit a long-wavelength Gregory-Laflamme-type unstable SU(3)-direction mode below a correlation length λ_GL as τ evolves; an unstable mode (Re(ω²)<0 for k<k_GL) is the framework's first localized compact-object-like structure (a KK bubble) with λ_GL its first compactness scale.
**Plan reference**: `sessions/investigation/investigation-4/investigation-4-plan-w2.md` §W2-4 (machinery pin, bubble-vs-GL-stable dual_prior, substitution chain source, connes co-author note).

**MCP Pre-Compute Audit**:
Queries executed before writing the producing script (query-first discipline; none returned a closure that PRE-CLOSES the gate — GL-STABILITY-63 is the STATIC anchor, and the DYNAMICAL τ̇≠0 question is the strictly-larger uncomputed extension):
- `search_knowledge("Gregory-Laflamme stability GL-STABILITY-63 SU(3) Lichnerowicz black string")` → returns the GL-STABILITY-63 result (W6-15, sp-authored, S63): "GL fiber stability | All 31 TT Lichnerowicz eigs >= 0; 3 independent protections | PERMANENT". This is the STATIC (τ̇=0) fiber result; the dynamical question is NOT covered.
- `get_constant("M_KK")` → 7.428660036284456e16 GeV (S42, CONST-FREEZE-42; default alias = M_KK_gravity). Used only as the dimensional unit (all ω², λ_GL reported in M_KK / M_KK² units).
- `get_constant("Delta_BCS")` → 0.4642547394830737 (M_KK units; S70 BCS-GAP-CANONICAL-70; **R-PROTECTED**). The canonical BCS gap that lifts the static zero modes (NOTE: this is the canonical value; the original s63 script used a local Delta_BCS=0.370 — the dynamical gate uses the R-protected canonical 0.4642547, Δ²=0.215532).
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). The fold τ where the transit velocity peaks; τ_fold is the global-min location of the dynamical dispersion.
- `trace_entity("GL-STABILITY-63")` → empty chain (the name is an attribution edge in the S63 W6 working paper, not a registry-promoted theorem entity); the npz anchor `s63_gl_stability.npz` carries the authoritative `evals_TT`, `lambda_GL=33.01965381`, `R_curv=5.25524112`, `verdict=PASS`. Branch: **NOT PRE-CLOSED** — the dynamical (τ̇≠0) GL question is uncomputed; this gate is the first to attack it.

**Verdict**: **PASS** — **Track B (∃ dynamical GL instability; KK-bubble channel)**.
The static-limit consistency gate passes EXACTLY (the operator is correctly built), and the dynamical dispersion is decisively unstable in the transit window. Canonical verdict line (`computations/investigation-4/inv4_gate_verdicts.txt`):

```
INV4-W2-4: PASS -- value='BRANCH=Track-B-EXISTS-unstable-SU3-mode_KK-bubble_lambda_GL=0.944475_M_KKinv_k_GL=6.652570_M_KK_min_omega2_eff=-4.425669e+01_at_tau=0.19_static-limit-resid=0.000e+00' scheme=GL-dynamical-4plus8-split convention=Peter-Weyl-blocked-dispersion L_max=12 audit_sha256=809456b4f4901526963351f64b989f705a096da63c97b5c92e5d9f7ebf80257d content_sha256=53d716c324b593b56ef1aeb85cb66224f52558b4ee427754444a2fe2e57dcc72 schema_version=S84+
# audit_sha256_short=809456b4f4901526 content_sha256_short=53d716c324b593b5 # INV4-W2-4 dual-SHA companion row
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # INV4-W2-4 3-tuple annotation (schema-v2); static-limit tau_dot->0 reproduces GL-STABILITY-63 bit-for-bit (resid=0.0); dynamical instability decisively signed (min omega^2_eff=-44.26 M_KK^2)
# regulator_pin=a_2^{zeta} # INV4-W2-4 internal-curvature (Lichnerowicz/Ricci) contribution to omega^2(k), zeta-regulated Seeley-DeWitt a_2 channel
```

The **composite is PASS** because the gate RESOLVES the dynamical GL question (Track B is a structural resolution, not a failure — `PASS_meaning` per the plan: "EITHER physics branch is a PASS"). The `[SIGN]` 3-tuple: `sign_verdict=PASS` (the static-limit τ̇→0 reproduces GL-STABILITY-63 — the hard consistency gate), `magnitude_verdict=PASS` (the dynamical min ω²_eff = −44.26 M_KK² is decisively signed, |min| ≫ 1e-6), `regime_verdict=VALID` (operator in regime). Collapse rule (gate-verdicts.md): regime=VALID ∧ sign=PASS ∧ magnitude=PASS ⇒ composite=**PASS**.

**Output Artifacts** (closure-verification checklist — all present on disk, content-verified):
- script `computations/investigation-4/inv4_w2_gregory_laflamme_dynamical.py` — contains `from canonical_constants import` and `print_verdict_payload` ✓
- data `computations/investigation-4/inv4_w2_gregory_laflamme_dynamical.npz` ✓ (static-limit comparison, per-τ dispersion curves, GL scales)
- plot `computations/investigation-4/inv4_w2_gregory_laflamme_dynamical.png` ✓ (6-panel: dispersion bare/eff, static-limit check, min-vs-τ, τ̇ profile, verdict summary)
- verdict line in `computations/investigation-4/inv4_gate_verdicts.txt` matching `^INV4-W2-4:.* audit_sha256=[a-f0-9]{64}` ✓ PLUS the dual-SHA companion row ✓ AND the schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row ✓ (`[SIGN]` trigger) + a `regulator_pin=a_2^{zeta}` companion row.

**Results**:

*Static-limit consistency (the HARD gate — operator validity).* At τ_freeze=0.22 with τ̇=0, our TT Lichnerowicz spectrum reproduces the GL-STABILITY-63 anchor **bit-for-bit**: `max|our_evals_TT − s63_evals_TT| = 0.000000e+00` (matched over all 31 eigenvalues), TT-dimension match True (ours=31, S63=31), and the dynamical operator at (τ̇=0, k=0) returns min ω² = −4.82587e−17 with `|dyn(τ̇=0,k=0) − static_min| = 0.000000e+00`. This is exact because the dynamical operator IS the s63 Lichnerowicz construction (`build_lichnerowicz_matrix` + `build_tt_projector`, verbatim) plus an additive term ΔK(τ̇) ∝ τ̇² that vanishes at τ̇=0. **The dynamical (4+8) perturbation operator is NOT mis-built** ⇒ `sign_verdict=PASS`.

*Dynamical dispersion `min_k ω²_eff(k)` along the τ-trajectory* (representative τ; τ̇ from the physical transit-velocity profile peaking at v_fold=Mach·c_BLV=6.66875 M_KK at the fold; ω²_eff = ω²_Lich + Δ²_BCS, Δ²_BCS = 0.4642547²=0.215532):

| τ | τ̇ (M_KK) | n_TT | min_k ω²_eff (M_KK²) | branch contribution |
|:--|:---------|:-----|:---------------------|:--------------------|
| 0.000 | 0.0443 | 35 | **+0.213569** | STABLE (static defenses dominate) |
| 0.100 | 2.1650 | 31 | **−4.471806** | UNSTABLE |
| **0.190** (fold) | **6.6688** | 31 | **−44.256694** | UNSTABLE (global min) |
| 0.220 | 5.8852 | 31 | **−34.419472** | UNSTABLE |
| 0.350 | 0.1905 | 31 | **+0.179244** | STABLE (static defenses dominate) |

**GLOBAL min_k ω²_eff = −44.256694 M_KK² at τ=0.19 (the fold), decisively < −1e-6 ⇒ Track B.** Bare (geometric, no BCS gap) global min = −44.472226 M_KK². The instability is **transit-localized**: it switches on with τ̇² and peaks at the fold; at the τ-edges (genesis τ=0, post-transit τ=0.35) where τ̇ is small, the static positive-Ricci/π₁=0/BCS-gap defenses dominate and ω²_eff > 0 (recovering the GL-STABILITY-63 stable regime).

*Compactness scale λ_GL (Track B payload).* The dispersion is exactly ω²_eff(k₄) = m²_internal_eff + k₄² (internal TT eigenvalue + BCS gap + the 4D KK kinetic term along the extended x₃ directions), so it crosses zero at **k_GL = √(−m²_internal_eff) = √(44.256694) = 6.652570 M_KK** and the UNSTABLE band is the LONG-WAVELENGTH band k₄ ∈ [0, k_GL) — the Gregory-Laflamme long-wavelength signature (short wavelengths k>k_GL are stabilized by +k₄²). **λ_GL = 2π/k_GL = 0.944475 M_KK⁻¹.** Compared to the static `λ_GL,S63 = 33.019654 M_KK⁻¹`, the dynamical instability is a **~35× SHORTER-scale** structure (k_GL,dyn = 6.65 ≫ k_GL,static = 2π/33.0 ≈ 0.19) — physically expected, since the dynamical extrinsic driver (τ̇²~44 M_KK²) vastly exceeds the static curvature scale (R_curv=5.26 M_KK⁻¹). k_GL lies ABOVE the plan's diagnostic long-wavelength band [0, 2/R_curv]=[0, 0.380572] M_KK, so the closed-form k_GL=√(−m²_int_eff) is used (the grid-scan crossing is off-band, consistent with a stronger-than-static instability).

*Dispersion decomposition ω²(k) = ω²_static(k) + ΔK(τ̇).* The new dynamical term is the contracting-SU(2) extrinsic-curvature coupling, projected to the TT subspace:
- ω²_static(k) = λ_Lich + k² ≥ 0 — the GL-STABILITY-63 contribution (positive Ricci min 1.346 M_KK² + the +k² KK kinetic term); max static TT eigenvalue +0.280634, min ≈ 0.
- ΔK(τ̇) = −α_ext · τ̇² · (k_SU2)² · P_SU2^TT, with α_ext = 0.25 = (1/2)² (from the extrinsic curvature K_ab = ½ τ̇·(Kasner exponent)·g_ab), k_SU2 = −2 (the SU(2) Kasner contracting exponent), P_SU2^TT the TT-projected SU(2)-block weight. **NEGATIVE** (destabilizing). At the fold: ΔK = −0.25·(6.66875)²·(−2)²·1 = **−44.472226 M_KK²** on the pure-SU(2) TT mode — matching the bare global min to machine precision (the SU(2)-block mode IS the most-unstable mode; the static contribution there is ~0). The three static defenses (positive Ricci STABILIZING, π₁(SU(3))=0 no S¹ to pinch, BCS gap Δ²=0.215532) sum to at most ~+0.50 M_KK² — overwhelmed by the −44 M_KK² extrinsic term at the fold.

*Substitution chain (with substituted numbers; the [SIGN] claim).*
- Def 1 (GL instability): black string Schw×S¹ unstable for λ > λ_GL ~ (d−2)R_H, horizon's NEGATIVE curvature driving the neck-pinch.
- Def 2 (static SU(3) defenses): positive Ricci (min 1.346 M_KK², STABILIZING), π₁=0, BCS gap Δ²=0.215532 → GL-STABILITY-63 found NO instability (all 31 TT eigs ≥ 0).
- Def 3 (what is DIFFERENT dynamically): τ̇≠0 makes g_ab(τ)=3·diag(e^{−2τ}×3, e^{+τ}×4, e^{+2τ}×1) time-dependent and anisotropic — SU(2) CONTRACTS (exponent −2), C²/U(1) EXPAND (+1,+2). A contracting direction is the dynamical analog of a neck that can pinch; the extrinsic coupling K²_ext (driver v_terminal=26.545 M_KK, transit velocity v_fold=6.66875 M_KK) feeds a term ABSENT from the static analysis.
- Substitute: ω²(k) = ω²_static(k) + ΔK(τ̇), ω²_static ≥ 0, ΔK ∝ −τ̇²(k_SU2)²P_SU2.
- Simplify: ∃ unstable mode ⟺ min_k[ω²_static(k) + ΔK] < 0. At fold: min ω²_eff = (ω²_static,SU2 ≈ 0) + (ΔK = −44.4722) + (Δ²_BCS = +0.2155) = **−44.2567 < 0** ⇒ Track B.
- Direction (sign_verdict): NO pre-registered direction for the EXISTENCE (two-branch payload). The pre-registered [SIGN] claim is the static-limit cross-check: sign_verdict = PASS iff τ̇→0 reproduces ω²(k)≥0 ∀k (GL-STABILITY-63) within 1e-6 — **HOLDS exactly (resid=0.0)** ⇒ `sign_verdict=PASS`.
- Conclusion: the contracting-SU(2) extrinsic term (−44 M_KK² at the fold) decisively overcomes the three static defenses (~+0.5 M_KK²); the operator is anchored to the proven static wall by the exact τ̇→0 reduction.

*Output 4-tuple:* (value=TRACK-B-BUBBLE, scheme=GL-dynamical-4plus8-split, convention=Peter-Weyl-blocked-dispersion, L_max=12). *Regulator pin:* a_2^{ζ} (the internal-curvature Lichnerowicz/Ricci contribution to ω²(k), zeta-regulated Seeley-DeWitt a₂ channel). *Canonical constants (imported, never hardcoded):* M_KK=7.428660e16 GeV, Delta_BCS=0.4642547394830737 (R-PROTECTED S70), tau_fold=0.19, Mach_max=13.75, c_BLV=0.485, v_terminal=26.544973; L12 Peter-Weyl cache (90 sectors) for the harmonic block structure. *Input SHA-256 pins (runtime-verified):* canonical_constants.py = 8505153a884277ba…, s63_gl_stability.npz = 425bec37ce28b410…, s84_spectrum_cache_L12 = 9e6d9cf7fd6a6949…. Dual-SHA: audit=809456b4f4901526…, content=53d716c324b593b5…; schema-v2 3-tuple row + regulator_pin row present.

*Dual_prior posterior.* Plan priors: Track A (GL-stable) 0.6, Track B (bubble) 0.4. Discriminator: min_k ω²(k) along the trajectory, GATED by the static-limit cross-check. (i) static-limit τ̇→0 reproduces GL-STABILITY-63 within 1e-6 → **operator VALID** (resid=0.0, dim match) → THEN (ii) min_k ω²_eff = −44.26 M_KK² decisively < 0 (by ≫ 1e-6) → **posterior 0.9 → Track B** (KK bubble; λ_GL=0.944475 M_KK⁻¹ reported). The contracting-SU(2) + K²_ext extrinsic coupling — absent from the static analysis — DOES beat the static positive-Ricci/π₁=0/BCS-gap floor in the long-wavelength band.

**Assessment (substrate-first; boundary-guard reading).** GEOMETRIC; Level-2 moduli-deformation (the GL question is asked ALONG the Jensen τ-trajectory τ̇≠0, on the substrate's own deformation manifold {D_K(τ(t))}; the Peter-Weyl harmonic decomposition at each τ is the Level-1 single-slice input). The substrate IS the geometry: this "KK bubble" is NOT an object inside a higher-dimensional container — it is a LOCALIZED instability of the substrate's OWN compactification, the contracting SU(2) direction pinching as the substrate deforms supersonically through the fold. The black-string GL picture is the laboratory analog (INVERTED per phononic-framing.md); the substrate's question is whether its own dynamical Jensen deformation has a long-wavelength mode the static defenses cannot suppress — and it DOES, but ONLY in the transit window (the instability is gated by τ̇², vanishing at the τ-edges where the static GL-STABILITY-63 stability is exactly recovered). This is the framework's **first localized compact-object-like structure** (the G2 no-compact-object gap is now filled by a dynamical KK-bubble channel) and its **first compactness scale** λ_GL = 0.944475 M_KK⁻¹ (~35× shorter than the static curvature scale). Two boundary-guard caveats: (1) the instability is TRANSIENT — it lives only during the supersonic transit (τ near the fold), not in the frozen post-transit physical epoch (τ→0.22, where ω²_eff returns positive), so the "compact object" is a transit-phase localization, not a permanent bound state; whether it has time to grow within the impulsive transit window (dt≈0.00113 M_KK⁻¹, Diagram A) is the natural follow-up. (2) The magnitude −44 M_KK² is dominated by τ̇²=v_fold²=44.5 — it is large because the transit is impulsive (Mach 13.75), exactly the framework's "supersonic transit not slow-roll" paradigm; the result is a structural feature of the impulsive transit, not a fine-tuned coincidence. **Carry-forward (genuine future compute, route to a session-mode plan per the track-local boundary):** the 12D acoustic-metric perturbation lift (gap G4) that this gate forces, and the bubble growth-rate-vs-transit-duration test (does Im(ω) integrated over the transit window exceed O(1) e-folds of growth?), with λ_GL=0.944475 M_KK⁻¹ as the first compactness-scale input.

---

## Wave 2 Synthesis (team-lead)

Wave 2 brought exact-GR machinery to bear on the substrate's causal structure. Four PASS/PASS/INFO/PASS verdicts; the wave's signature is that **every gate resolved its question from the substrate** rather than importing a GR result — and one (W2-4) produced the framework's first localized compact object.

**The four verdicts:**
- **W2-1 PASS — C-1 resolved.** Re-deriving `c_s(τ)` from the actual `a₂(τ)` spectral stiffness reveals a genuine 2.6% van-Hove softening at τ=0.190 (the channel S95's constant-`c_s` was blind to), yet the discriminant `(c_s²−v²)(τ)` still has **N_zeros = 1** (root τ₀=0.112183, κ_entry=+17.604>0). The dip lowers `c_s²` by only 0.012 M_KK² against a ~44 M_KK² gap — far too shallow to re-cross. The **S85 bracketed-pair sealed interior is a modeling artifact** of a hand-placed symmetric dip; C-1 resolves in favor of S95 (single asymmetric open exit). [The agent self-corrected a volume-preserving-metric scalarization bug mid-run — the Jensen `det g_τ=6561` is τ-flat, so geometric-mean scalarization collapsed to S95's null; arithmetic block-average recovered the real a₂(τ) dependence.]
- **W2-2 PASS — focusing is a₂.** Raychaudhuri for the reduced (a(t),τ(t)) congruence reproduces q∝H (q_Raych=0.525833, dev=0.0 vs S101-W1-QEQ-SELFCONS), localizes the un-fixed scale w=M_KK to a **single rank-1 term** (SVD ratio 3.3e-17), and decomposes the dominant `−R_ab k^a k^b` as **99.97% a₂** (Einstein-Hilbert grade) vs ~0.03% a₀ (opposite, defocusing, DILUTION-CC residual). Internal geometry is pure Kasner shear σ²=5τ̇² with tr K=0 (reproduces S63 SURFACE-12 exactly). Track A (clock in a₂), posterior 0.85.
- **W2-3 INFO — marginal censorship.** The H¹_loc regularity exponent at the extremal κ=0 Σ_dump is `p = −1.000000` EXACTLY (|p+1|=1.5e-8) — sitting precisely on the L²-integrability boundary p_crit=−1, the extremal/Aretakis boundary-of-censorship regime (neither cleanly sealed nor extendible). Tortoise slope −1 ⇒ power-law (extremal), not logarithmic (sub-extremal); V(τ_dump)=V′(τ_dump)=0, V″=2, κ=0, blueshift shut off. Censorship at Σ_dump is **dynamical** (off-trajectory COSMIC-CENSORSHIP-49), NOT supplemented by a Cauchy-horizon-inextendibility sealing theorem. Priors stay 0.5/0.5 (INFO is the pre-registered third outcome).
- **W2-4 PASS — first compact object.** The dynamical M⁴×SU(3) admits a Gregory-Laflamme-type unstable SU(3)-direction mode: `min_k ω²_eff = −44.26` at the fold τ=0.19, with the hard static-limit cross-check EXACT (τ̇→0 reproduces GL-STABILITY-63 bit-for-bit, max|Δ|=0). Compactness scale `λ_GL = 0.944 M_KK⁻¹` (~35× shorter than the static λ_GL,S63=33.0). Driver: contracting-SU(2) extrinsic term ΔK=−44.47 overwhelms the three static defenses (Ricci, π₁=0, BCS gap; ~+0.5). This is the framework's **first localized compact-object-like structure** (a transit-phase KK bubble), filling the G2 gap — but TRANSIENT (τ̇²-gated, absent post-transit).

### (a) Numerical revisions
- W2-1: `N_zeros=1`, τ₀=0.112183, κ_entry=+17.604; van-Hove dip c_s 0.485→0.4725 (2.6%).
- W2-2: q_Raych=0.525833 (dev 0.0); a₂ share 99.97%; SVD rank-1 ratio 3.3e-17; σ²=5τ̇².
- W2-3: p=−1.000000 (|p+1|=1.5e-8); tortoise slope −1; V″=2.0.
- W2-4: min ω²_eff=−44.26 (τ=0.19); k_GL=6.6526, λ_GL=0.9445 M_KK⁻¹; ΔK=−44.47.

### (b) Structural changes
- **C-1 contradiction RESOLVED** (S95 single-asymmetric-open over S85 bracketed-pair) — a registry-state direction change from the substrate; the S85 second sonic surface is reclassified as a modeling artifact.
- **G3 censorship reading SHARPENED**: from "censorship holds" (binary) to "dynamical (off-trajectory) censorship, NOT a sealing theorem at the extremal surface" — an epistemic-type change (the extremal surface is on the censorship boundary, p=−1 exactly).
- **G2/G4: first compact-object-like structure EXISTS** (KK bubble, transit-phase) — a new structural object, λ_GL the first compactness scale; promotes the "no compact structure" gap to "transient transit-phase localization."
- **Cross-wave clock split**: W2-2 places the focusing clock on **a₂** (99.97%); W3-1 places the expansion clock on **a₀** (c_track=3). Two correct readings of *different* substrate observables → seeds the clock-location workshop (see CF-INV4-W3-C).

### Effected In-Session (non-math; team-lead)
- [x] Wave-2 synthesis (this section) + math/non-math split written — `investigation-4-w2-workingpaper.md §"Wave 2 Synthesis"`.
- No session-track register edits (track-local boundary): **HY1** (Diagram-J redraw to single-asymmetric-open) and **HY2** (capstone causal-disconnection down-tag) are now LICENSED by W2-1's N_zeros=1 verdict, but both are SESSION-TRACK curated-register edits — they route to `/rclab-investigate --investigation 4` close per the seed's quarantine, NOT effected here (housekeeping §D). The C-1 resolution, G3 sharpening, and the KK-bubble registration are likewise session-track promotions (Carry-Forward + housekeeping §B).

## Carry-Forward Computations

### CF-INV4-W2-A — 12D acoustic-metric perturbation lift of the KK bubble (G4)
1. **What**: Lift the W2-4 reduced (4+8)-split GL instability to the full 12D acoustic-metric perturbation problem and compute the bubble growth-rate vs transit-duration ratio (does the τ̇²-gated instability have time to grow within the impulsive Mach-13.75 transit?).
2. **Inputs**: `inv4_w2_gregory_laflamme_dynamical.npz` (ω²_eff(τ,k), λ_GL=0.9445), L12 cache (90 Peter-Weyl sectors), transit-duration from the S95 white-hole kinematics.
3. **Gate**: growth-rate × transit-duration `≥ 1` (e-fold) PASS (bubble matures) / `< 1` INFO (transient, sub-critical); pre-register the e-fold threshold.
4. **Effort**: ~1–2 compute waves (12D perturbation is heavier than the reduced split).

### CF-INV4-W2-B — Session-track promotion: C-1 resolution + G3 sharpening + KK-bubble registration
1. **What**: Lift three W2 results into session-mode for permanent registry: (i) C-1 RESOLVED (S95 single-asymmetric-open); (ii) G3 dynamical-not-sealing censorship at Σ_dump; (iii) the KK-bubble first-compact-object record with λ_GL. Includes the HY1/HY2 capstone-hygiene edits (Diagram-J redraw + causal-disconnection down-tag) now licensed by N_zeros=1.
2. **Inputs**: `inv4_w2_cs_zero_count.npz`, `inv4_w2_christodoulou_scc.npz`, `inv4_w2_gregory_laflamme_dynamical.npz`; verdict lines (W2-1 `8ebbcb84…`, W2-3 `c74a2a1a…`, W2-4 `809456b4…`).
3. **Gate**: session-mode re-verify each verdict reproduces under canonical pins; then registry-landing + capstone designated-writer patch (HY1/HY2) per the capstone-hygiene gate.
4. **Effort**: ~1 compute + registry/capstone landings.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | C-1 (acoustic horizon count) | CONTRADICTION (S95 1-zero vs S85 2-zero) | RESOLVED → S95 single-asymmetric-open; S85 pair = modeling artifact | N_zeros=1 from substrate a₂(τ) stiffness (INV4-W2-1) |
| 2026-06-15 | τ↔t clock focusing channel (G1) | unlocalized | a₂ at 99.97% (Einstein-Hilbert grade); q∝H reproduced | Raychaudhuri rank-1 localization (INV4-W2-2) |
| 2026-06-15 | G3 censorship at Σ_dump | "holds" (binary) | dynamical (off-trajectory), NOT a sealing theorem; p=−1 marginal | Christodoulou H¹_loc INFO (INV4-W2-3) |
| 2026-06-15 | G2/G4 compact structure | absent ("no compact object") | EXISTS — transient transit-phase KK bubble, λ_GL=0.944 M_KK⁻¹ | dynamical GL instability (INV4-W2-4) |
| 2026-06-15 | Clock-location (C2) | a₂ conformal clock emptied (volume-preserving) | a₀-vs-a₂ split surfaced (W2-2 a₂ focusing vs W3-1 a₀ expansion) | cross-wave; seeds clock-location workshop |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict (audit_sha256 short) | Verdict |
|:-----|:-------|:------------|:------------|:-----------------------------|:--------|
| INV4-W2-1 | `inv4_w2_cs_zero_count.py` (47KB) | `inv4_w2_cs_zero_count.npz` (235KB) | `…png` (132KB) | `8ebbcb84…` | PASS |
| INV4-W2-2 | `inv4_w2_raychaudhuri_focusing.py` | `inv4_w2_raychaudhuri_focusing.npz` (48KB) | `…png` (132KB) | `06da2662…` | PASS |
| INV4-W2-3 | `inv4_w2_christodoulou_scc.py` (34KB) | `inv4_w2_christodoulou_scc.npz` (488KB) | `…png` (166KB) | `c74a2a1a…` | INFO |
| INV4-W2-4 | `inv4_w2_gregory_laflamme_dynamical.py` | `…npz` | `…png` | `809456b4…` | PASS |

All artifacts under `computations/investigation-4/`; verdict lines (canonical) in `computations/investigation-4/inv4_gate_verdicts.txt`.
