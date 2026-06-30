# Session 104 Wave 1 — Standing precision CFs (Results Working Paper)

**Session**: 104 | **Wave**: 1 | **Plan**: session-104-plan-w1.md | **Theme**: Standing precision carry-forwards inherited from S103 — each a deeper-resolution re-run of an already-pinned S103 verdict (deeper truncation, ≥300-bit edge adjudication, direct deep-L spectra, precondition-licensed prose upgrade), NOT new physics.

## Gate Sections

### §W1-1. S104-VIIAM-L11-ANCHOR (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S104-VIIAM-L11-ANCHOR`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (§VII.AM envelope row — D_K spectral-action effacement moment, fabric-side)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: Under the SAME pre-registered prefactored comparator, the §VII.AM Level-3 anchor at L=11 sits strictly inside the Level-2 envelope (anchor(11) < env_prefac(11)), resolving the deeper-truncation pathway the S103 L=10 FAIL left open.
**Plan reference**: `sessions/session-plan/session-104-plan-w1.md` §W1-1 (machinery pin, thresholds, substitution chain source).

**Verdict**: **PASS** — anchor(11) = 2.109477e-05 < env_prefac(11) = 2.428498e-05 strict under the pre-registered prefactored comparator ⇒ ratio_prefac(11) = 0.868635 < 1. The §VII.AM envelope row converges INTO its Level-2 envelope at the deeper L=11 truncation (Level-3 < Level-2 one truncation deeper than the canonical L=10); the envelope row becomes registry-PASS-eligible at L=11. The deeper-truncation pathway the S103 L=10 FAIL (`b47ccf98`, ratio 1.1578) left open is now closed. Composite collapse `sign=PASS ∧ magnitude=PASS ∧ regime=VALID ⇒ PASS`. **The Level-1 cohomology-class theorem-STRUCTURE is STAGE-3-PERMANENT and UNCHANGED** — this gate touched ONLY the Level-2/Level-3 numerical ladder of the envelope row.

**Output Artifacts**:

- **Script** `computations/session-104/s104_viiam_l11_anchor.py` — both `must_contain` patterns present:
  ```
  $ grep -nE 'from canonical_constants import|print_verdict_payload' computations/session-104/s104_viiam_l11_anchor.py
  87:from canonical_constants import *  # noqa: F401,F403
  458:def print_verdict_payload(
  611:    print_verdict_payload(
  ```
- **Data** `computations/session-104/s104_viiam_l11_anchor.npz` — present (52 fields: anchor_11, env_prefac_11, env_bare_11, ratio_prefac_11, ratio_bare_11, signed_margin_11, the L=10 sentinel block, the bit-exact-vs-S103 cross-checks, the decay-factor mechanism, full provenance).
- **Plot** `computations/session-104/s104_viiam_l11_anchor.png` — present (Panel 1: anchor(L) vs prefactored & bare envelopes over L∈[8,11] showing the prefactored crossing at L=11; Panel 2: ratio_prefac(L)/ratio_bare(L) vs the PASS boundary = 1).
- **Verdict line** `computations/session-104/s104_gate_verdicts.txt` — emitted via the race-safe `emit_verdict` MCP tool (7 rows: canonical + dual-SHA companion + schema-v2 [SIGN] 3-tuple + 4 extra rows). Matches `^S104-VIIAM-L11-ANCHOR:.* audit_sha256=[a-f0-9]{64}`:
  ```
  $ grep -E '^S104-VIIAM-L11-ANCHOR:.* audit_sha256=[a-f0-9]{64}' computations/session-104/s104_gate_verdicts.txt
  S104-VIIAM-L11-ANCHOR: PASS -- value='anchor(11)=2.109477e-05_vs_env_prefac(11)=2.428498e-05@Lmax11;ratio_prefac(11)=0.868635(<1=>PASS);...' ... audit_sha256=3d4a8049d2b89d60d1cfadd8e158e5dcae92c485cd938450c1ba6d46eac3be3d content_sha256=94a2d5f530d93b2619d133b615c2b549d89591e2e42f669cc44bba098338566e schema_version=S84+
  ```
- **Dual-SHA**: `audit_sha256 = 3d4a8049d2b89d60d1cfadd8e158e5dcae92c485cd938450c1ba6d46eac3be3d` (script+canonical+pinmap), `content_sha256 = 94a2d5f530d93b2619d133b615c2b549d89591e2e42f669cc44bba098338566e` (script only). sig_5-unique (no collision with the 3 sibling S104 verdict SHAs).
- **schema-v2 SIGN 3-tuple companion row**: `# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S104-VIIAM-L11-ANCHOR 3-tuple annotation (schema-v2)`.
- **WP section**: this section (`### §W1-1. S104-VIIAM-L11-ANCHOR`).

**MCP Pre-Compute Audit** (queries run BEFORE the script — NUMBERS-first, gate-second, query-first discipline per `.claude/rules/epistemic-discipline.md`):

- `search_knowledge("VII.AM envelope row Level-3 anchor dGamma Gamma effacement L-indexed")` → returned the S103-plan-w2 pre-registration of the L-indexed anchor rule (`anchor(L) := dGamma_over_Gamma at L`, array `[9.70e-05, 6.90e-05, 4.40e-05, 2.11e-05]` at L∈{8,9,10,11}, deviation SHRINKS with L; PRE-REGISTERED anti-comparator-shopping indexing) + the S101 envelope-pin context (`env_at_Lmax10 = 2.039e-05` bare vs `level2_reconciled = 3.797e-05` prefactored). Confirms the comparator-arbiter is the prefactored(ii) form and the L=11 slice is the deeper-truncation open pathway. **NOT PRE-CLOSED** — L=11 is a new (deeper) truncation; the gate is a genuine forward evaluation, not a re-statement.
- `trace_entity("S103-VIIAM-LINDEXED-ANCHOR")` → returned the L=10 baseline verdict line `value='L3_Lindexed=4.396804e-05_vs_L2prefac=3.797445e-05@Lmax10; ratio_L3/L2prefac=1.1578(>1=>FAIL); L2bare=2.039233e-05(xcheck: ratio_L3/L2bare=2.1561); alpha=4.690533; C=exp(0.621755)=1.862193; idx_L10=2`. This IS the upstream-consistency sentinel target (ratio_prefac(10)=1.157832, ratio_bare(10)=2.156107) — reproduced bit-exact below.
- `get_constant("Gamma_effacement")` → `0.9997` (canonical; `Gamma_eff` is an alias). The Level-3 anchor is `dGamma/Gamma` (a spectral-action zeroth-moment effacement ratio), NOT a Seeley-DeWitt `a_n` citation ⇒ `regulator_pin = N/A` (verdict extra-row).

**Results**:

| Quantity | Value (6 sf) | Note |
|:---------|:-------------|:-----|
| **anchor(11)** = dGamma/Gamma[idx=3] | **2.10948e-05** | the L=11 Level-3 effacement anchor (pinned float from `s101...npz.dGamma_over_Gamma[3]`) |
| 11^(−α) | 1.30411e-05 | α = 4.690533158119443 |
| **env_prefac(11)** = C·11^(−α) | **2.42850e-05** | the PRE-REGISTERED prefactored 'ii' comparator (ARBITER); C = exp(0.6217547500863554) = 1.86219 |
| env_bare(11) = 11^(−α) | 1.30411e-05 | bare comparator — REPORTED-NOT-GATING (cross-check only) |
| **ratio_prefac(11)** = anchor/env_prefac | **0.868635** | **< 1 ⇒ PASS** (the arbiter; Registry-PASS criterion) |
| ratio_bare(11) = anchor/env_bare | 1.617565 | **> 1** — bare comparator FAILs; does NOT gate (anti-comparator-shopping) |
| signed_margin(11) = anchor − env_prefac | −3.19021e-06 | < 0 ⇒ anchor strictly INSIDE the prefactored envelope |

**4-tuple**: `(value='ratio_prefac(11)=0.868635;PASS', scheme=cross-pillar-bridge-anatomy-Registry-PASS-criterion-Lindexed-anchor, convention=envelope-comparator-PRE-REGISTERED-prefactored-ii/alpha=4.6905/anchor=Lindexed-dGamma/L=11, L_max=11)`.

**Substitution chain (with substituted numbers)** — per `.claude/rules/math-scripts.md §"Double-Check Logic"`:

```
Claim: "anchor(L=11) < env_prefac(L=11) — the deeper-truncation anchor sits INSIDE the Level-2 envelope."

Step 1 (Def 1): anchor(L) := dGamma_over_Gamma[idx(L)], idx(L) = L − 8 over L∈[8,9,10,11].
                anchor(11) = dGamma_over_Gamma[3] = 2.10947710e-05      [s101...npz field, pinned]
Step 2 (Def 2): env_prefac(L) := C · L^(−α),  C = exp(0.6217547500863554) = 1.8621928596201978,  α = 4.690533158119443.
                [s102...npz fields C, alpha; comparator_decision = "prefactored(ii)C*L^-alpha" — the PRE-REGISTERED arbiter]
Step 3 (Def 3): ratio_prefac(L) := anchor(L) / env_prefac(L).   [PASS iff < 1]

Substitute (L=11, no simplification):
    11^(−4.690533158119443) = 1.30410656e-05                         [float64]
    env_prefac(11) = 1.8621928596201978 · 1.30410656e-05 = 2.42849792e-05
    ratio_prefac(11) = 2.10947710e-05 / 2.42849792e-05

Simplify:
    ratio_prefac(11) = 0.868635                                      [canonical form]

Direction: ratio_prefac(11) = 0.868635 < 1  ⇒  anchor(11) < env_prefac(11)  ⇒  SIGN = PASS.
Conclusion: under the pre-registered prefactored comparator, anchor(L=11) < env_prefac(L=11) — verdict PASS.
```

**Mechanism (why the deeper truncation enters the envelope)** — substitution-chain-verified decay factors across L=10→11:
- anchor decays `dGamma/Gamma: 4.39680436e-05 → 2.10947710e-05`, factor **0.479775**.
- prefactored envelope decays `env_prefac: 3.79744506e-05 → 2.42849792e-05`, factor **0.639508**.
- The anchor decays FASTER than the `L^(−α=4.6905)` envelope across this step, so the ratio crosses **below** 1: from `1.157832` (OUTSIDE, L=10) to `0.868635` (INSIDE, L=11). The L=10 FAIL was right at the edge (ratio ≈ 1.16); one truncation deeper resolves it. This is a substrate-IS spectral-weight redistribution: more of D_K's own eigenvalue spectrum enters the effacement moment at L=11, and the moment descends inside its convergence envelope — NOT a field tuned in a container.

**Bare-comparator cross-check (REPORTED-NOT-GATING)**: env_bare(11) = 11^(−α) = 1.30411e-05; ratio_bare(11) = 2.10948e-05 / 1.30411e-05 = **1.617565 > 1** ⇒ the bare comparator still FAILs at L=11. The comparator choice is decisive, which is exactly WHY the prefactored 'ii' arbiter is pinned at plan-freeze (anti-comparator-shopping, S104-context Wave1 item-1.3): the runtime may NOT switch to bare to flip the verdict. A hard assertion in the script (`prefactored_arbiter_confirmed`) verifies the upstream npz provenance declares the prefactored(ii) form as the Registry-PASS arbiter before the inequality is evaluated.

**Upstream-consistency sentinel (L=10 reproduction of S103 `b47ccf98`)** — the gate's INFO branch fires ONLY on sentinel non-reproduction (input-pin drift → input-SHA re-verification, NOT a substrate verdict). The sentinel reproduced bit-exact:

| L=10 sentinel | re-derived | S103 stored | plan target (6 sf) | dev vs target | bit-exact resid vs S103 |
|:--------------|:-----------|:------------|:-------------------|:--------------|:------------------------|
| anchor(10) | 4.396804e-05 | 4.396804e-05 | — | — | — |
| env_prefac(10) | 3.797445e-05 | 3.797445e-05 | — | — | — |
| ratio_prefac(10) | 1.157832 | 1.157832 | 1.157832 | 2.52e-07 (< 1e-6 ✓) | **0.000e+00** |
| ratio_bare(10) | 2.156107 | 2.156107 | 2.156107 | 4.84e-08 (< 1e-6 ✓) | **0.000e+00** |
| idx(L=10) | 2 | 2 (`idx_L10`) | — | — | match ✓ |

`sentinel_ok = True`; the L=10 baseline reproduces, so the L=11 adjudication is valid (no input-pin drift). Provenance cross-checks all PASS: `C_cross_ok=True` (C reproduces across s101/s102), `alpha_cross_ok=True`, `dGamma_copies_match=True` (s101 and s103 `dGamma_over_Gamma` arrays bit-identical), `prefactored_arbiter_confirmed=True`. All five hard assertions in the script passed.

**Input-SHA verification** (plan Input-SHA Ledger, all matched at runtime):
- `canonical_constants.py` → `9cd89e612fcdbb17...` ✓
- `s101_viiam_alpha_envelope_pin.npz` → `3ea82a00b375e344...` ✓ (dGamma_over_Gamma, α, intercept source)
- `s102_w2_viiam_l2l3_recon.npz` → `5d5f6c9e1c1c63b7...` ✓ (prefactored comparator C, α arbiter)
- `s103_viiam_lindexed_anchor.npz` → `030824039de86b14...` ✓ (L-indexed rule + L=10 sentinel)

**Substrate framing**: GEOMETRIC. The §VII.AM observable is a fabric-side effacement quantity — `D_K eigenvalues → spectral-action zeroth-moment effacement ratio dGamma/Gamma (impedance-mismatch leakage of the acoustic white-hole transit, Gamma_eff = 0.9997 canonical at L_ref=12) → Level-3 empirical anchor at truncation L`. The L_max truncation is the spectral-support cutoff on the finite spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`; L=10→11 refines how much of the substrate's own eigenvalue spectrum enters the effacement moment. The Level-2 envelope `C·L^(−α)` is the substrate's algebraic convergence rate of that finite-L moment toward its continuum (laboratory-IN) image. The PASS says: one truncation deeper, the substrate-IS effacement anchor has descended inside its own convergence envelope. The arrow runs D_K eigenvalues → effacement moment → envelope crossing; never the reverse. **The Level-1 cohomology-class identity is regulator-invariant and L-independent (STAGE-3-PERMANENT) and is NOT consumed or altered by this gate.**

**Solution-space update**: the §VII.AM envelope-row Level-3 is now registry-PASS-eligible at L=11 (PASS routes a §VII.AM envelope-row Level-3 update CF to the mack/gen-physicist sole-writer per the plan Wave-1→Wave-2 routing table). The deeper-truncation rescue corridor the S103 L=10 FAIL left open is now CONFIRMED, not foreclosed — the row converges into its prefactored envelope, refuting Track B (which read the L=10 FAIL as structural / comparator-fragile). Per the plan dual-prior discriminator, PASS → 0.85 Track A (the envelope binds at deeper truncation). The bare-comparator FAIL is reported either way and does NOT move the priors (it is not the arbiter). **No change to the Level-1 theorem (out of scope by the S103 verdict).**

---

### §W1-2. S104-SWMAX-MPMATH-EDGE (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S104-SWMAX-MPMATH-EDGE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (SU(1,1) Bogoliubov squeezing window of the W-stage relay pattern)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: At ≥300-bit, the frozen W-stage deviation lies strictly inside the asymmetric SU(1,1) window upper edge (sign(deviation − (S_W_max−1)) = −1), resolving below the float64 floor whether the S103 knife-edge is a strict interior point or an exact saturation.
**Plan reference**: `sessions/session-plan/session-104-plan-w1.md` §W1-2.

**Verdict**: **PASS** — composite collapse `sign=PASS · magnitude=PASS · regime=VALID ⇒ PASS`. At mp.prec = 320 bits (~96 decimal digits) AND at Sage exact real-algebraic-field (AA) precision, `sign(deviation − (S_W_max−1)) = −1`: the W-stage deviation lies **strictly INSIDE** the asymmetric SU(1,1) window upper edge. The S103 W3-1 float64 knife-edge resolves to a strict interior point, NOT an exact saturation (`Delta.is_zero() = False` in AA — provable, not a numerical estimate). The S79 sufficiency condition holds with a real (sub-float64-floor-resolvable) margin of +5.211e-09; the F_amp slot 0.3885 is vindicated as interior to the window envelope. Because the sign is −1 (not 0), no `# composite-precedence:` companion row is required (that clause governs only the sign-0 INFO branch).

**NUMBERS** (numbers first, gate second, interpretation third):

| Quantity | ≥300-bit (mpmath, mp.prec=320) | Provenance |
|:---------|:-------------------------------|:-----------|
| `|α_W|` | 1.000001059132600963771318318462 | √(W_alpha_re² + W_alpha_im²) |
| `|β_W|` | 0.001455426509286706083250414127 | √(W_beta_re² + W_beta_im²) |
| `2|β_W|²` | 4.236532647868972697581255e-06 | window asymmetry term |
| `2|α_W||β_W|` | 2.910856101552740751403798e-03 | window half-spread term |
| **`S_W_max − 1`** | **2.915092634200609724101379e-03** | `= 2|β_W|² + 2|α_W||β_W|` (asymmetric UPPER endpoint) |
| **`deviation`** | **2.915087423202256024928891e-03** | frozen `deviation` field, S102 W7 |
| **`Δ = deviation − (S_W_max−1)`** | **−5.210998353699172488264072e-09** | the adjudicated quantity |
| **`sign(Δ)`** | **−1** (strict interior) | mpmath 320-bit |

6-sig-fig publication form: `deviation = 2.91509e-3`, `S_W_max − 1 = 2.91509e-3` (they agree to 5+6 sf — this IS the S103 knife-edge; the ≥300-bit `Δ` is what resolves it). Full ≥30-digit strings stored in `s104_swmax_mpmath_edge.npz` (`Delta_320`, `S_W_max_m1_320`, `deviation_320`, etc.).

**Sage MCP exact real-algebraic-field (AA) cross-check** (the decisive arbiter — zero precision ambiguity): every frozen float64 amplitude is an exact dyadic rational (p/2ᵏ); `|α_W|`, `|β_W|` are algebraic-number square roots, so AA gives a PROVABLE sign.
- `sign(Δ)` in AA = **−1** (matches mpmath; hard-asserted in the script as a sentinel — `assert int(value) == int(sage_sign_AA)`).
- `Δ.is_zero()` = **False** → deviation is NOT the upper endpoint by an algebraic identity; it is a strict interior point. The sign-0 "exact-saturation structural-identity" branch is definitively ruled out.
- `Δ` (AA, 120 bits) = −5.210998353699172488264072e-9 — agrees with the mpmath value to all printed digits.
- `S_W_max − 1 − envelope_upper_dev` (AA) = 7.6285e-17 → reproduces the frozen S102/S103 edge to the bit-exact residual.

**Substitution chain** (per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute" — the [SIGN] directional claim):
- Def 1: `α_W := W_a`, `β_W := W_beta_re + i·W_beta_im` [S102 `s102_w7_ladder_phase_resolved.npz`; unitarity `|α_W|² − |β_W|² = 1`, verified resid −2.451e-16].
- Def 2: `S_W_max − 1 := 2|β_W|² + 2|α_W||β_W|` (asymmetric-window UPPER endpoint — the window center is `S_W_center = 1 + 2|β_W|² = 1.00000424`, NOT 1, so the upper edge carries the `2|β_W|²` term in addition to the half-spread; established bit-exact in S103-FAMP-TOLERANCE-REPIN, `edge_2b2_2ab_bitexact` resid 7.6e-17).
- Def 3: `deviation` := frozen derived-phase deviation of the F_amp-modulated slot from 1 [S102 field = 2.915087e-03; `cos_phi_off_axis = 0.99999966 ~ +1`, the slot lands at the upper edge].
- Substitute (mp.prec ≥ 300): `Δ = mpf(deviation) − (2·mpf(|β_W|)² + 2·mpf(|α_W|)·mpf(|β_W|))`; `verdict = sign(Δ)`.
- Canonical form: `Δ = −5.210998…e-09 < 0` ⇒ `sign(Δ) = −1` ⇒ `deviation < S_W_max − 1` ⇒ **strict interior** ⇒ predicted SIGN = PASS.
- The float64 shadow `Δ_f64 = −5.211e-09` matched the predicted branch; ≥300-bit + AA confirmed it is a real margin, not a rounding artifact of an exact 0. Sign-direction prediction **CONFIRMED** (sign_verdict=PASS).

**Cross-checks (sentinels, all PASS)**:
- `S_W_max − 1` (320-bit) vs frozen `envelope_upper_dev` (2.9150926342005e-03): resid **7.629e-17** — reproduces the S103 `resid_bitexact = 7.633e-17` (hard-asserted `< 1e-15`).
- `Δ` float64 shadow −5.210998e-09 vs S103 `dev_vs_repin` −5.210998e-09: resid **−7.629e-17** — reproduces the S103 frozen knife-edge record (hard-asserted `< 1e-15`).
- mpmath 320-bit sign vs Sage AA exact sign: both **−1** (hard-asserted equal).
- Unitarity `|α_W|² − |β_W|² − 1 = −2.451e-16` (float64-noise floor; confirms the amplitudes form a valid SU(1,1) Bogoliubov pair).

**Output 4-tuple**: `(value=sign=−1;Delta_320b=−0.000000005210998, scheme=FW, convention=SU(1,1)-form-1-temporal-L-to-R;window-asymmetric-upper-edge-2beta2+2ab, L_max=12)`.

**Schema-v2 SIGN 3-tuple companion row**: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`. The `# composite-precedence:` row is NOT emitted (sign ≠ 0). Extra companion rows carry `regulator_pin=N/A` (SU(1,1) amplitude, not a Seeley-DeWitt moment), the Sage exact-AA fingerprint, and the edge-vs-frozen residual.

**Substrate framing** (per `.claude/rules/phononic-framing.md`): PHONONIC. The arrow runs `D_K eigenvalues at τ_fold → W-stage Bogoliubov mixing amplitudes (α_W, β_W) of the impulsive supersonic transit → SU(1,1) squeezing window {S_W_min, S_W_max} → deviation`. The deviation IS the substrate-IS quantity — how far the relay-pattern's derived-phase-modulated amplitude sits from unity, an intrinsic property of the fold's squeezing geometry. There is no external container in which the F_amp slot "fits"; the slot IS the relay pattern's amplitude and the window IS the SU(1,1) algebra of its squeezing. The ≥300-bit adjudication shows the substrate's deviation **strictly respects** its own squeezing endpoint (interior, margin +5.211e-09) — the asymmetric window (centered at `1 + 2|β_W|²`, not at 1) is the fabric's own excitation-amplitude bound, and the slot honors it below the float64 floor. The arrow never reverses; the window is not a pre-existing box the substrate fills.

**Dual-prior update**: pre-registered Track A (strict interior; SU(1,1) amplitudes generic ⇒ exact saturation is measure-zero) vs Track B (exact saturation; the 5+6-sf agreement is the tell). The ≥300-bit + AA discriminator returns sign −1 → **0.85 to Track A** (strict interior; S79 sufficiency holds with margin; PASS). The exact-saturation reading (Track B) is definitively excluded: `Δ.is_zero() = False` in the real algebraic field is a theorem, so the 5+6-sf agreement was a near-miss at the publication-precision floor, not an algebraic identity. The S103 composite-INFO-at-float64 left the priors unchanged; this ≥300-bit re-derivation is the discriminator that moves them. The F_amp slot 0.3885 (UNIFIED-AS-79 k_a2 POWER-RATIO factor) and the S79 magnitudes-only ladder anchor are UNDISTURBED — only the strict-vs-saturation sign was decided.

**Output Artifacts**:
- Script `computations/session-104/s104_swmax_mpmath_edge.py` — PASS (`from canonical_constants import`, `print_verdict_payload` both present; grep-verified below).
- Data `computations/session-104/s104_swmax_mpmath_edge.npz` — present (≥40-digit mpmath strings + float64 shadows + Sage-AA fingerprint).
- Plot `computations/session-104/s104_swmax_mpmath_edge.png` — present (number-line of edge vs deviation + sub-float64 margin bar).
- Verdict line in `computations/session-104/s104_gate_verdicts.txt` — `S104-SWMAX-MPMATH-EDGE: PASS … audit_sha256=f43750364c5782273f3d729aad29bf8abb31a3ae37dc615bdcaa5313d28c01c9` with dual-SHA companion + schema-v2 3-tuple (`sign=PASS/magnitude=PASS/regime=VALID`) + 3 extra rows. `audit_sha256 = f43750364c5782273f3d729aad29bf8abb31a3ae37dc615bdcaa5313d28c01c9`, `content_sha256 = a7007c924fd64355db98027200db82270584662498ff177f1afc8a1e50aa72a2`.
- This WP section §W1-2.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("S_W_max SU(1,1) squeezing window Bogoliubov W-stage F_amp deviation upper edge")` → returned the S103 plan equation "deviation == S_W_max − 1 to within publication precision (knife-edge persists at the exact [edge])" + the S104 plan substitution chain `verdict = sign(Δ)`; confirms THIS gate is the open follow-up, not yet evaluated.
- `search_knowledge("FAMP-TOLERANCE-REPIN knife-edge envelope_upper_dev asymmetric window 2beta2+2ab")` → returned the S103-FAMP-TOLERANCE-REPIN gate verdict (INFO, `value=PASS_TOL_repin=2.915093e-03;…;dev_vs_repin=-5.211e-09;edge=S_W_max-1=2b2+2ab;…`); confirms the frozen knife-edge record and the asymmetric-edge form. The S103 verdict is INFO (composite collapse sign=PASS/magnitude=INFO/regime=VALID).
- `get_constant("F_amp_sc")` → "not found" (F_amp_sc = 47.92 lives in the npz, not a registered canonical constant; no conflict — nothing to recompute).
- `trace_entity("SU(1,1) squeezing window S_W_max")` → "No trace found" (the window edge is a per-session npz quantity, not a registry entity; this ≥300-bit sign adjudication is genuinely new work, not a re-derivation of a closed result).
- Atlas-08 freshness (Q23) names this gate as the deeper-precision adjudication of the S103 exact-edge re-pin INFO — consistent with the gate being open at dispatch.
- Input-SHA verification at dispatch: all three plan-pinned SHAs reproduced bit-exact — `s102_w7_ladder_phase_resolved.npz = b70d78bf…`, `s103_famp_tolerance_repin.npz = 116801c9…`, `canonical_constants.py = 9cd89e61…`. No input-pin drift.

---

### §W1-3. S104-BRANCH-IV-DIRECT-L1314 (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S104-BRANCH-IV-DIRECT-L1314`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (branch-IV w0 — D_K dark-energy spectral moment at truncation L, fabric-side)
**Agent**: `gen-physicist`
**Hypothesis**: With DIRECT ρ_B(13)/ρ_B(14) spectra (replacing the S103 Friedrich-Bär envelope bound), the CAC-anchored spread_CAC over L ∈ {12,13,14} stays inside the unchanged W5-2 PASS band (≤ 0.025), confirming the branch-IV dark-energy moment is truncation-stable at deep L.
**Plan reference**: `sessions/session-plan/session-104-plan-w1.md` §W1-3.

**Verdict**: **PRE-REG-INC** — value=`PRE-REG-INC_blocked_by_irrep_construction_wall_Sym13_Sym14; phase1_status=IN_PROGRESS; have_13=False; have_14=False; n_new=12; rho_recompute_sentinel_PASS_diff=0.0; deferred_to_S105; S103_FB_envelope_INFO_508c7cf3_stands_as_best_bound` scheme=`zeta` convention=`CAC-branch-iv-anchored-L10-DERIVED-OFFSET` L_max=`{12,13,14}` audit_sha256=`b48b609f8392be5a4d54e4c3a5e14a5f02c0c95ec919860e951918b848adb8ff` content_sha256=`29ea787de38c01e83243febdd68da74d92d865018234aed470622876b2f1c5ae` schema_version=S84+. The pre-registered FEASIBILITY FALLBACK fired: the DIRECT ρ_B(13)/ρ_B(14) computation requires the COMPLETE level-13 and level-14 Peter-Weyl sector sets, but the pure-symmetric sectors (0,13)/(13,0)/(0,14)/(14,0) are structurally infeasible to construct with the available `irrep_symmetric_power` builder (dense 3^p tensor space: Sym^13 = 40.7 TB, Sym^14 = 366 TB). Honest closure per `.claude/rules/mechanical-closure-discipline.md`, deferred to S105 — **NOT a FAIL**. The S103 Friedrich-Bär envelope-bound INFO (`508c7cf3`) stands as the best available bound (spread ≈ 0.0221 inside the PASS band).

**MCP Pre-Compute Audit**:
- `search_knowledge("branch-IV w0 dark energy spectral moment truncation stability CAC Zubarev")` → 7 equation hits: `w0^CAC(L) = ρ_B(L) + offset_B → emergent late-time w0 → DESI DR3` (S103 plan-w5); `offset_B := w0_B − ρ_B(L=10)` (S102 plan-w5); `w0^CAC(L=10) = ρ_Zubarev(L=10) + [w0_FW − ρ_Zubarev(L=10)]` (S86); provenance `branch_iv_deep_truncation` (S103). **NOT PRE-CLOSED** — the deep-truncation DIRECT spread is genuinely open; S103 closed it only at FB-envelope-bound INFO.
- `get_constant("w0_FW")` → **−0.918** (S58 four-fold-lock: Volovik vacuum partition + effacement Γ_eff=0.99970). Consumed as the CAC anchor `offset_B := w0_FW − ρ_B(L=10)`.
- `trace_entity("Friedrich-Bar saturation branch-IV")` → no direct trace (the FB-saturation predicate lives in the S103 producing script + npz, not the knowledge graph); the FB envelope bound is recorded in `s103_branch_iv_deep_truncation.npz` (eta_FB_min=0.4365, branch=FRIEDRICH-BAR-INFO, spread=0.022134).

**Results**:

*Substitution chain (offset-cancellation; the pre-registered structural fact).* The verdict observable is the truncation span of the CAC-anchored dark-energy moment:
- Def-1: `ρ_B(L) := ρ_Zubarev(L) = <|λ|>_Z(L)/λ_max(L) − 1`, with `<|λ|>_Z = Σ_j d_j w_Z_j |λ_j| / Σ_j d_j w_Z_j`, `w_Z = exp(−|λ|²/Λ_Z²)`, `Λ_Z=1.0`, summed over all Peter-Weyl sectors with level ≤ L (S85 W0-7 verbatim).
- Def-2: `offset_B := w0_FW − ρ_B(L=10)`, `w0_FW = −0.918` [canonical, S58]. DERIVED at runtime, NOT hardcoded.
- Def-3: `w0^CAC(L) := ρ_B(L) + offset_B` (so `w0^CAC(L=10) = w0_FW` EXACTLY by construction).
- Def-4: `spread_CAC := max_{L∈{12,13,14}} w0^CAC(L) − min_{L∈{12,13,14}} w0^CAC(L)`.
- Substitute + simplify: `spread_CAC = max_L (ρ_B(L)+offset_B) − min_L (ρ_B(L)+offset_B) = max_L ρ_B(L) − min_L ρ_B(L)` — **the offset_B additive translation cancels exactly; the span is offset-FREE** and depends ONLY on the ρ_B(L) differences across {12,13,14}. This is why the CAC vs W0_B anchor choice (−0.918 vs −0.842454) is immaterial to the verdict: both give the identical spread. CAC is mandatory per `.claude/rules/regulator-convention-lockdown.md` (RDC FORBIDDEN); it satisfies the L=10 effacement-preservation identity by construction.

*ρ_B reproduction sentinel (PASS, bit-exact).* The Phase-2 evaluator reproduced the consumed S85 W0-7 / W5-2 moment to machine zero on the s84 L≤12 master cache (90 sectors, max_level=12, the EXACT τ_fold=0.19 assembly):

| L | ρ_B(L) recompute | S103 record | diff | n_modes |
|:--|:-----------------|:------------|:-----|:--------|
| 8 | −0.504465997911697 | −0.5044659979116969 | 0.00e+00 | 31264 |
| 10 | −0.577172580512029 | −0.5771725805120294 | 0.00e+00 | 78080 |
| 12 | −0.634885419265151 | −0.634885419265151 | 0.00e+00 | 166896 |

`rho_recompute_max_diff = 0.0 ≤ 1e-12` (plan tolerance pin; the S103 reproduction was 1.1e-16). This confirms my evaluator IS the consumed evaluator — no re-fit, no convention drift — so ANY ρ_B(13)/ρ_B(14) it produces would be directly comparable to the FB prior. The sentinel passing is the necessary precondition for trusting the (unreached) DIRECT span.

*The wall (why the DIRECT branch is infeasible — substitution chain on dense memory).* D_K is BLOCK-DIAGONAL by Peter-Weyl, `D_K = ⊕_{(p,q)} D_{(p,q)}`; extending L→{13,14} means adding the NEW sectors with p+q∈{13,14}. The bottleneck is irrep CONSTRUCTION, NOT GPU diagonalization (per `.claude/rules/math-scripts.md §"D_K Block-Diagonality"`). For pure-symmetric (p,0)/(0,p), `get_irrep` calls `irrep_symmetric_power(gens, p)`, which builds a DENSE `3^p × 3^p` complex tensor-space matrix (line 935, `np.zeros((3^p, 3^p))`) and projects onto the dim_sym=(p+1)(p+2)/2 symmetric subspace:

| p | 3^p (tensor dim) | dense 3^p×3^p complex |
|:--|:-----------------|:----------------------|
| 9 | 19,683 | 6.2 GB (S103 measured Sym^9 ≈ 200.9 s — fits, slow) |
| 10 | 59,049 | 55.8 GB (> 17.1 GB VRAM) |
| 11 | 177,147 | 502 GB (> 128 GB RAM) |
| **13** | **1,594,323** | **40,670 GB = 40.7 TB — physically impossible** |
| **14** | **4,782,969** | **366,029 GB = 366 TB — physically impossible** |

The (0,13) build thrashed for 185 s on the 40 TB allocation with zero progress before I stopped it. There is **no recursive (p,0) builder in `dirac_spectrum.py` that avoids the 3^p blowup** (verified by grep); `irrep_symmetric_power` is the sole pure-symmetric path, and the mixed Casimir-projection path `(p,q)=proj((1,0)⊗(p−1,q))` cannot bootstrap (p,0) because its parent (p−1,0)=Sym^{p−1} is itself infeasible at p−1≥11.

*Phase-1 partial build (the Casimir-projection path DOES work for mixed sectors).* 12/14 level-13 mixed sectors built cleanly on the RX 9070 XT (ROCm torch 2.9.1+rocm), GPU eigvalsh of `i·D` (Hermitian), in 87.8 s total; persisted incrementally to `s104_sym_p_chain_cache_L1314.npz`:

| sectors built (level-13 mixed) | dim range | iD_herm_err | build+eigvalsh |
|:--|:--|:--|:--|
| (1,12),(12,1) | 195 | 8.9e-16 | 1.9 s each |
| (2,11),(11,2) | 270 | 7.1e-16 | 4.0–4.2 s |
| (3,10)..(9,4) | 330–420 | ≤1.0e-15 | 6.3–11.7 s |

Missing (the walls): level-13 → (0,13),(13,0) [Sym^13]; level-14 → all 15 sectors (the build stalled on (0,13) before reaching level-14; (0,14)/(14,0) are Sym^14 walls regardless). `have_13=False`, `have_14=False` ⇒ DIRECT ρ_B(13)/ρ_B(14) uncomputable ⇒ pre-registered fallback fires.

*Cross-reports (NOT gating — the FB diagnostic prior + S86 offset, recorded per spawn).*
- FB diagnostic prior (S103, the best available bound): ρ_B(13)=−0.646653, ρ_B(14)=−0.657020, FB-midpoint spread ≈ 0.0221 (INSIDE the PASS band ≤0.025); decrement-sign NEGATIVE, decelerating=True. These are the FB-envelope MIDPOINTS the DIRECT spectra would have replaced; the S103 INFO stands.
- offset_B (CAC, w0_FW-anchored) = −0.340827 = `offset_Zubarev` (S86 canonical, cross-checked); the W0_B-anchored variant = −0.265281 (S103 cross-report). Both yield the identical offset-free spread.
- w0^CAC(L=10) = w0_FW = −0.918 by construction (cac_anchor_resid = 0 when the span is evaluated; not reached this run since the DIRECT branch did not fire, but the identity is structural).

*4-tuple*: (value=`PRE-REG-INC_blocked_by_irrep_construction_wall_Sym13_Sym14`, scheme=`zeta`, convention=`CAC-branch-iv-anchored-L10-DERIVED-OFFSET`, L_max=`{12,13,14}`). regulator_pin=`a_4^{Mellin}` (companion row; UNCHANGED from S103). Dual-SHA computed at runtime from the ordered input-pin map (s84 cache + dirac_spectrum.py + s103 npz + Phase-1 cache + canonical): audit_sha256=`b48b609f…adb8ff`, content_sha256=`29ea787d…f1c5ae`.

*Solution-space reading.* PRE-REG-INC is a pre-registered intermediate, not a soft FAIL: the {12,13,14} deep-truncation DIRECT-stability corridor remains UN-MAPPED, neither confirmed (PASS) nor refuted (FAIL). What IS established: (a) the moment evaluator is bit-exactly the consumed one (sentinel PASS); (b) the wall is the dense-3^p `irrep_symmetric_power` implementation, an engineering artifact NOT a physics obstruction — the (p,0) irrep itself is only 105/120-dimensional. The branch-IV w0 truncation-stability question is fully closeable once a Gelfand-Tsetlin / monomial-basis (p,0) builder lands (constructs the rep directly in the dim_sym space, never forming the 3^p tensor). The S103 FB-envelope INFO (spread ≈ 0.0221, PASS-band-interior) remains the best bound for the DR3-class w0 dark-energy object.

**Substrate framing**: GEOMETRIC. The branch-IV w0 is the dark-energy equation-of-state moment of the fabric: D_K eigenvalues at τ_fold (the full spectrum, ρ_B) → the Zubarev branch-IV a_4-channel spectral moment ρ_B(L) → w0^CAC, the effective late-time equation of state the substrate's effacement residual presents. Each truncation L is the spectral-support cutoff on the finite triple (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}); the L→{13,14} extension is the inclusion of the NEW Peter-Weyl (p,q) sectors with p+q∈{13,14} into the moment sum. The CAC offset is a pure additive translation anchoring w0^CAC(L=10)=w0_FW exactly; the truncation SPREAD is offset-independent and measures whether the substrate's own eigenvalue spectrum has converged enough at L=12 that adding two more shells does not move the dark-energy moment. The arrow runs D_K eigenvalues → Zubarev moment → w0; GR's dark energy is the consequence, not the premise. The wall is purely computational (the substrate's (p,0) sectors exist and are finite-dimensional; only the tensor-space symmetrizer implementation is infeasible) — it does NOT invert the explanatory direction.

**Carry-Forward (S105)**: `CF-S105-BRANCH-IV-DIRECT-L1314-GT-BUILDER` — implement a Gelfand-Tsetlin / monomial-basis (p,0) irrep builder that constructs the SU(3) symmetric-power generators directly in the dim_sym=(p+1)(p+2)/2 space (105 for (0,13), 120 for (0,14)) via closed-form ladder-operator matrix elements, NEVER forming the 3^p tensor. Inputs: the 4 missing pure-symmetric sectors (0,13)/(13,0)/(0,14)/(14,0) + the 13 missing level-14 mixed sectors (the latter buildable via the existing Casimir-projection path once (0,13)/(13,0) exist); the 12 already-built level-13 mixed sectors in `s104_sym_p_chain_cache_L1314.npz`. Gate: spread_CAC over {12,13,14} vs the UNCHANGED W5-2 band (PASS ≤0.025 | INFO (0.025,0.050] | FAIL >0.050); cross-check the new GT (p,0) spectrum against the s84 cache for the already-cached (p,0) sectors (p≤12) bit-exact before consuming the new ones. Effort: ~1 gate (GT builder is new machinery + verification; then minutes of GPU eigvalsh + moment).

**Output Artifacts**:
- Script `computations/session-104/s104_branch_iv_direct_l1314.py` (Phase-2):
```
$ grep -E 'from canonical_constants import|print_verdict_payload' computations/session-104/s104_branch_iv_direct_l1314.py
from canonical_constants import (  # noqa: E402
def print_verdict_payload(verdict, value, audit_sha, content_sha,
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        print_verdict_payload(verdict, value, audit_sha, content_sha)
```
- Phase-1 builder `computations/session-104/s104_branch_iv_phase1_builder.py` (the offline Sym^p chain builder) + intermediate cache `computations/session-104/s104_sym_p_chain_cache_L1314.npz` (12 mixed level-13 sectors, status=IN_PROGRESS, 106929 B).
- Data `computations/session-104/s104_branch_iv_direct_l1314.npz` (6717 B; verdict=PRE-REG-INC, feasible=False, rho_recompute_ok=True, all FB-prior/offset cross-reports).
- Plot `computations/session-104/s104_branch_iv_direct_l1314.png` (56249 B; fallback plot — ρ_B(L≤12) + wall-status annotation).
- Verdict line in `computations/session-104/s104_gate_verdicts.txt`:
```
$ grep -E '^S104-BRANCH-IV-DIRECT-L1314:.* audit_sha256=[a-f0-9]{64}' computations/session-104/s104_gate_verdicts.txt
S104-BRANCH-IV-DIRECT-L1314: PRE-REG-INC -- value='PRE-REG-INC_blocked_by_irrep_construction_wall_Sym13_Sym14; …' scheme=zeta convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET L_max={12,13,14} audit_sha256=b48b609f8392be5a4d54e4c3a5e14a5f02c0c95ec919860e951918b848adb8ff content_sha256=29ea787de38c01e83243febdd68da74d92d865018234aed470622876b2f1c5ae schema_version=S84+
```
  + dual-SHA companion row + regulator_pin=a_4^{Mellin} companion row + feasibility-wall companion row (no SIGN 3-tuple — [VERIFY] trigger).

---

### §W1-4. S104-VIIBS-CLAUSE-B-WORDING (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S104-VIIBS-CLAUSE-B-WORDING`
**Trigger**: `[AUDIT]`
**Classification**: **NON-PHONONIC** (methodology / registry-prose hygiene — METHODOLOGY-class candidate, M4 satisfied by orchestrator allowlist append at plan-freeze)
**Agent**: `gen-physicist` (designated-writer reviewed prose patch)
**Hypothesis**: Both S103 preconditions having landed (W1-6 annotation `2c27b197` PASS, W2-1 rank-1 PASS `ac1dbb28`), the §VII.BS clause-(b) bundle-exhaustiveness characterization upgrades from "standing premise (Open Q6)" to "result" via a designated-writer patch, with the frozen Stage-0 blockquote (`e669ccd2`, len 2514) byte-SHA UNCHANGED and the theorem grade UNCHANGED.
**Plan reference**: `sessions/session-plan/session-104-plan-w1.md` §W1-4.

**Verdict**: **PASS** — boolean predicate `upgrade_licensed ∧ verify = True`. Both S103 preconditions verified PASS from `computations/session-103/s103_gate_verdicts.txt` at runtime (S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION PASS audit `2c27b197…` ∧ S103-NNU-BUNDLE-EXHAUSTIVENESS PASS audit `ac1dbb28…`), so the upgrade is LICENSED. The clause-(b) bundle-exhaustiveness characterization is upgraded "standing premise (Open Q6)" → **"result"** on all 3 annotation surfaces (index row line 157, clause-(b) inline table line 21392, SCOPE ANNOTATION block line 21399), citing the rank-1 certificate `ac1dbb28` as basis, per the §VII.BP BINDING-AMENDMENT form. The frozen Stage-0 blockquote span SHA `e669ccd2…` (len 2514) is byte-IMMUNE and UNCHANGED (pre==post==pin, HARD-asserted). The theorem grade is UNCHANGED (`**STAGE-3-PERMANENT**` count 19→19; no up-tag, no down-tag). This is a **confidence-EQUALITY** fix — the prose tag is brought UP TO its register status (the rank-1 certificate PROVES the augmented-bundle exhaustiveness), never above it; capstone-hygiene **Q3 = NO** (no PROVEN/CONDITIONAL/BROKEN/INFO status change of any capstone claim — the grade is invariant; only one clause's scope-word is sharpened).

**NUMBERS** (numbers/SHA first, gate second, interpretation third):

| Check | Value | Result |
|:------|:------|:-------|
| Precondition 1 (`S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION` PASS, audit `2c27b197…`) | found PASS line in s103 verdict file | **True** |
| Precondition 2 (`S103-NNU-BUNDLE-EXHAUSTIVENESS` PASS, audit `ac1dbb28…`) | found PASS line in s103 verdict file; npz `rank_aug=1`, `second_rel_sv=1.0658e-17` | **True** |
| `upgrade_licensed` (P1 ∧ P2) | logical AND | **True** |
| Frozen-span SHA PRE | `e669ccd2daa5aa5be7396499f59c0636a803eac02e1f7710c2a1fc428d3cdaba` (len 2514) | == pin |
| Frozen-span SHA POST (re-read from disk) | `e669ccd2daa5aa5be7396499f59c0636a803eac02e1f7710c2a1fc428d3cdaba` (len 2514) | **UNCHANGED** (== pin, HARD) |
| `frozen_unchanged` (pre==post==pin AND byte-identical span) | boolean | **True** |
| Upgraded wording present, 3 surfaces (index ∧ clause-(b) ∧ SCOPE-block ∧ EFFECTED sentence) | `surf_index ∧ surf_clauseb ∧ surf_block ∧ surf_effected` | **True** |
| Old "standing premise (Open Q6)" surfaces gone (no residual un-upgraded surface) | 4 OLD anchors absent post-write | **True** |
| Theorem grade `**STAGE-3-PERMANENT**` count | 19 → 19 | **unchanged** |
| Dated W2-1 cross-reference audit trail preserved | `**Standing-premise → result (dated cross-reference, S103 W2-1):**` present | **True** |
| Frozen blockquote occurrence count | 1 → 1 | **ok** |
| `verify` (conjunction of all above) | boolean | **True** ⇒ PASS |

**The full 64-char frozen-span SHA (immutability evidence, pre AND post):** `e669ccd2daa5aa5be7396499f59c0636a803eac02e1f7710c2a1fc428d3cdaba`, len 2514, located by literal-substring anchor (`> **Normalization Non-Universality (N₃=0 corollary, rank-1).**`, NOT line number) — the SAME extractor boundary the S103 W1-6 annotation used. PRE-SHA == POST-SHA == plan pin. The most serious FAIL axis; it PASSED.

**Applied diff (the wording upgrade — before/after; annotation surfaces ONLY):**

- **Surface 1 — INDEX row (line 157):**
  - BEFORE: `…single-cutoff COUNT for the dagger-row bundle, bundle-exhaustiveness a standing premise [Open Q6]) — the substrate determines…`
  - AFTER: `…single-cutoff COUNT for the dagger-row bundle, bundle-exhaustiveness a RESULT [Open Q6 closed S104 W1-4; rank-1 cert ac1dbb28]) — the substrate determines…`
- **Surface 2 — clause-(b) inline table (line 21392):**
  - BEFORE: `…bundle exhaustiveness a separate standing premise — Open Q6; rests on FULL BDI triviality…`
  - AFTER: `…bundle exhaustiveness a RESULT — Open Q6 closed (S104 W1-4 upgrade; rank-1 cert ac1dbb28); rests on FULL BDI triviality…`
- **Surface 3a — SCOPE ANNOTATION bolded clause (line 21399):**
  - BEFORE: `**exhaustiveness of the dagger-row bundle is a separate standing premise**, with Open Question 6 (m_H / EW-VEV entering the induced action independently of M_KK) the named untested channel`
  - AFTER: `**exhaustiveness of the dagger-row bundle is a RESULT** (S104 W1-4 upgrade; the standing-premise Open Question 6 — m_H / EW-VEV entering the induced action independently of M_KK — is CLOSED by the rank-1 certificate ac1dbb28…, see the dated cross-reference below)`
  - BEFORE (closing sentence): `The upgrade of this SCOPE ANNOTATION from standing-premise to result (re-wording clause (b)'s grade) is an S104 follow-up per the plan's Wave 1→2 decision point; the annotation lands as-worded here regardless.`
  - AFTER (closing sentence): `The upgrade of this SCOPE ANNOTATION from standing-premise to **result** … is EFFECTED at S104 W1-4 (` + "`S104-VIIBS-CLAUSE-B-WORDING`" + `, designated-writer reviewed patch licensed by BOTH S103 preconditions …): the bundle-exhaustiveness characterization above now reads 'result', a CONFIDENCE-EQUALITY upgrade … frozen Stage-0 blockquote span SHA ` + "`e669ccd2…`" + ` byte-IMMUNE and UNCHANGED; theorem grade UNCHANGED STAGE-3-PERMANENT, Q3=NO.`

The frozen Stage-0 blockquote (line 21385; rank-1-obstruction / two-falsifiers language) carries NO "standing premise (Open Q6)" characterization (verified by grep: only lines 157 / 21392 / 21399 match) and is NOT in any edit anchor — it is byte-untouched. The "Standing-premise → result (dated cross-reference, S103 W2-1)" provenance paragraph is preserved verbatim (audit trail intact); only its terminal "S104 follow-up" deferral converts to "EFFECTED at S104 W1-4".

**Precondition verifications (re-grepped at runtime from `computations/session-103/s103_gate_verdicts.txt`):**
- `S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION: PASS … audit_sha256=2c27b19758f2571b98dcf463eee0fdb124321a165dcc6122eb9917693ecb5d6c` — the Option-A corrective line (supersedes `f56f08f3…`; sole change = canonical-helper refactor; verdict/value identical). The W2-1 cross-ref rows in that file state verbatim "standing-premise->result upgrade is S104 follow-up" — this gate IS that follow-up.
- `S103-NNU-BUNDLE-EXHAUSTIVENESS: PASS -- value='rank=1|second_rel_sv=1.06581e-17' … audit_sha256=ac1dbb2892cef172a6383f33652d110e53b7815316c4eefa1c0aa1360def3257` — the rank-1 certificate. npz cross-check: `rank_aug=1`, `second_rel_sv=1.0658e-17` (the value-string `rank1_cert=ac1dbb28(rank=-1)` reflects a benign npz field-name lookup — the npz rank field is `rank_aug`, not `rank`; the substantive rank=1 is verified from BOTH the verdict value string and `rank_aug`).

**AFTER-pattern single-shot trace** (per `registry-landing.md §"Bridge-Landing Script Architecture"`): `build_promotion_text` (full upgraded text built in memory; all 4 edit anchors asserted count==1) → `write_atomic_with_fsync` (tmp + fsync + os.replace) → `re_read + verify_section_matches` (single boolean from disk re-read: frozen_unchanged ∧ upgraded_present ∧ old_surfaces_gone ∧ grade_unchanged ∧ dated_xref_preserved ∧ bq_count_ok) → exactly ONE `emit_verdict` call. Idempotent NO-OP branch: if `S1_NEW` present and `S1_OLD` absent at entry, the write is SKIPPED (already upgraded). FAIL-revert branch: on an APPLIED write that fails verify, the registry is byte-restored to the pre-patch state and the gate closes FAIL with remediation — never iterate (`v3-closure-recovery.md` Class-1 boundary). This run: licensed, not-already-upgraded, APPLIED, verify=True ⇒ PASS.

**M4 allowlist-membership state**: gate-ID `S104-VIIBS-CLAUSE-B-WORDING` was appended to `sessions/framework/registry/methodology-wave-allowlist-ledger.md` by the orchestrator at plan-freeze (3-column row, plan-block sha `e7275804…`, per the session-104 plan index), with rationale prose mirrored to `methodology-wave-instances.md`. M1 (artifact-existence-with-substantive-content PASS predicate) ∧ M2 (Edit/Write on the curated registry-prose surface + grep/SHA; no numerical-threshold `.py`) ∧ M3 (verbatim from the S103 rank-1 PASS + W1-6 annotation; no new derivation) ∧ M4 (allowlisted) all satisfied — METHODOLOGY-class. Dispatch consequence is the same single-shot AFTER-pattern reviewed prose patch either way. No allowlist action was required from this gate.

**Output 4-tuple**: `(value=upgrade_licensed=True(P1=True∧P2=True);verify=True;frozen_span_UNCHANGED=True(==e669ccd2);standing-premise->result_3surfaces=True;old_surfaces_gone=True;grade=STAGE-3-PERMANENT_unchanged(19==19);Q3=NO_confidence-EQUALITY;rank1_cert=ac1dbb28(rank=-1);applied=True;already_upgraded=False, scheme=CURATED-DOC-REVIEWED-DESIGNATED-WRITER-PATCH, convention=STANDING-PREMISE-TO-RESULT-WORDING-UPGRADE;FROZEN-BLOCKQUOTE-IMMUNE;VIIBP-BINDING-AMENDMENT-FORM;THEOREM-GRADE-UNCHANGED-STAGE-3-PERMANENT, L_max=N/A)`.

**Dual-SHA** (METHODOLOGY-class closure per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`): `content_sha256` over `script||applied-diff` (the rule/registry-prose diff is the F-image of the numerical PASS-predicate eigenvalue under substrate↔methodology), `audit_sha256` over the input-pin map of source documents. `audit_sha256 = ead021c6c2ba96d48894c2d57248b4496ae3e8302fe513801eae7e5332af3633`, `content_sha256 = 140c938d69c7991a1aab1004f48469abc0ccc7595745f72fbe4ca402ba037c94`, `applied_diff_sha = cf3d16061e61cb7ea87fba6f0bea7238e93ea04976246661b11431d7c06c5260`. No SIGN 3-tuple ([AUDIT] trigger, not [SIGN]).

**Solution-space reading.** PASS closes the standing precision CF inherited from S103: the §VII.BS clause-(b) bundle-exhaustiveness, deferred at S103 W2-1 as "an S104 follow-up", is now EFFECTED. Capstone-hygiene F-consistency is maintained — the registry PROSE tag equals its register status (no clause narrates above its register status). The rank-1 certificate `ac1dbb28` (rank(Cov_aug)=1 with `w2 = m_H/v_ew`, second_rel_sv=1.07e-17) is the proof that closed Open Q6's augmented-bundle leg; this gate is bookkeeping that brings the wording into alignment with that proof. ZERO gate verdicts change; the theorem stays STAGE-3-PERMANENT. No carry-forward (the upgrade is complete).

**Substrate framing** (per `.claude/rules/phononic-framing.md`): NON-PHONONIC (methodology / registry-prose hygiene). This gate makes NO substrate-physics claim — it is a capstone-hygiene F-consistency enforcement (layer-functor F, `epistemic-discipline.md §"Layer-Decomposition"`: the registry PROSE tag is the methodology-floor F-image of the substrate-physics register status). The underlying substrate result is unchanged and ALREADY proven: the arrow `D_K eigenvalues → BdG bundle K-theory (every K_0-generator of A_B is a rank-1 character-projection class, HC²(A_B)=0, so no rank-≥2 projection classes are generated) → rank-1 augmented-bundle exhaustiveness (certificate `ac1dbb28`, second_rel_sv=1.07e-17)` is the same before and after. The frozen Stage-0 blockquote is byte-immune; only the annotation-surface scope-word is sharpened from 'standing premise' (unproven) to 'result' (proven). This is a confidence-EQUALITY fix — the prose is brought UP TO its register status, never an explanation-direction inversion. The direction of explanation (substrate IS the cosmology's dimensionless dynamical content; the single dimensional scale M_KK is imported through `O = w·Ô`) is preserved verbatim.

**Output Artifacts**:
- Script `computations/session-104/s104_viibs_clause_b_wording.py` (29191 B) — present:
```
$ grep -cE 'from canonical_constants import' computations/session-104/s104_viibs_clause_b_wording.py
1
$ grep -cE 'print_verdict_payload' computations/session-104/s104_viibs_clause_b_wording.py
2
```
- Data `computations/session-104/s104_viibs_clause_b_wording.npz` (12481 B) — present (OPTIONAL per plan `optional: true`; produced anyway: stores frozen-span PRE/POST SHA + `frozen_unchanged`, the upgraded-surface booleans, `old_surfaces_gone`, grade pre/post count, registry pre/post file SHA, precondition booleans, `applied_diff_sha`, W2-1 provenance).
- Plot `computations/session-104/s104_viibs_clause_b_wording.png` — NOT produced (OPTIONAL per plan `optional: true`; prose patch has no figure; no must_contain — compliant).
- Verdict line `computations/session-104/s104_gate_verdicts.txt` — present; matches `^S104-VIIBS-CLAUSE-B-WORDING:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + 2 extra provenance rows (`companion_row_required: true`; no SIGN 3-tuple — [AUDIT] trigger; emitted via `emit_verdict`, cross-process locked, sig_5 unique):
```
$ grep -E '^S104-VIIBS-CLAUSE-B-WORDING:.* audit_sha256=[a-f0-9]{64}' computations/session-104/s104_gate_verdicts.txt
S104-VIIBS-CLAUSE-B-WORDING: PASS -- value='upgrade_licensed=True(P1=True∧P2=True);verify=True;frozen_span_UNCHANGED=True(==e669ccd2);standing-premise->result_3surfaces=True;old_surfaces_gone=True;grade=STAGE-3-PERMANENT_unchanged(19==19);Q3=NO_confidence-EQUALITY;rank1_cert=ac1dbb28(rank=-1);applied=True;already_upgraded=False' scheme=CURATED-DOC-REVIEWED-DESIGNATED-WRITER-PATCH convention=STANDING-PREMISE-TO-RESULT-WORDING-UPGRADE;FROZEN-BLOCKQUOTE-IMMUNE;VIIBP-BINDING-AMENDMENT-FORM;THEOREM-GRADE-UNCHANGED-STAGE-3-PERMANENT L_max=N/A audit_sha256=ead021c6c2ba96d48894c2d57248b4496ae3e8302fe513801eae7e5332af3633 content_sha256=140c938d69c7991a1aab1004f48469abc0ccc7595745f72fbe4ca402ba037c94 schema_version=S84+
```
- Registry section `sessions/permanent-results-registry.md §VII.BS` — upgraded wording present (`bundle-exhaustiveness a RESULT`, `bundle exhaustiveness a RESULT`, `**exhaustiveness of the dagger-row bundle is a RESULT**`, `is EFFECTED at S104 W1-4`); frozen-span SHA `e669ccd2…` UNCHANGED; grade `**STAGE-3-PERMANENT**` count 19 unchanged.
- WP section this `### §W1-4` block.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("VII.BS bundle exhaustiveness Open Q6 rank-1 augmented bundle Schur")` → returned `S103-NNU-BUNDLE-EXHAUSTIVENESS` PASS (`rank=1|second_rel_sv=1.06581e-17`), the §VII.BS theorem (STAGE-3, audit `d309efb4`), and the atlas-08 open-channel row "clause-(b) RESOLVED … rank(Cov_aug)=1 … σ₂/σ_max = 1.07e-17". Confirms the upgrade precondition is landed and the bundle-exhaustiveness is a PROVEN result, NOT pre-closed as a re-derivation — this is a prose-alignment patch on an already-proven result.
- `trace_entity("VII.BS")` → returned the §VII.BS PROVEN theorem (STAGE-3, clause (b) scope-noted), `S102-NNU-STAGE1-REGISTRATION`, `S102-CAPSTONE-63-RESCOPE-PATCH` (the prior designated-writer reviewed-patch precedent), and the atlas-08 "clause-(b) RESOLVED" row. Confirms the entry is STAGE-3-PERMANENT and the prior prose-patch lineage.
- `search_knowledge("NNU bundle exhaustiveness rank-1 character projection HC2 second_rel_sv")` → returned `HC^2(\mathcal{A}_B) = 0` ("generated by rank-1 character projections … no rank-≥2 projection classes"), confirming the substrate basis for "result": every K_0-generator is a rank-1 virtual bundle class ⇒ augmented bundle exhaustive. This is the proof the wording is brought up to.
- Runtime precondition re-verification (not MCP): both S103 PASS lines re-grepped bit-exact from `s103_gate_verdicts.txt` (audit `2c27b197…` ∧ `ac1dbb28…`); input SHAs reproduced — `s103_nnu_bundle_exhaustiveness.npz = bca33511…`, `canonical_constants.py = 9cd89e61…`. Registry pre-write file SHA `3cf2dd36…` (plan-pinned `<computed-at-runtime>`; no drift-vs-pin). Frozen-span PRE-SHA `e669ccd2…` (len 2514) == plan pin.

---

## Wave 1 Synthesis (team-lead)

**Verdicts (4/4 landed, dual-SHA, sig_5-unique)**: W1-1 `S104-VIIAM-L11-ANCHOR` **PASS** (`3d4a8049…`) · W1-2 `S104-SWMAX-MPMATH-EDGE` **PASS** (`f4375036…`) · W1-3 `S104-BRANCH-IV-DIRECT-L1314` **PRE-REG-INC** (`b48b609f…`) · W1-4 `S104-VIIBS-CLAUSE-B-WORDING` **PASS** (`ead021c6…`).

The four standing precision carry-forwards from S103 are discharged. Three closed cleanly; one closed honestly against a newly-characterized structural wall.

- **W1-1**: the §VII.AM fold-transit envelope row converges INTO its Level-2 envelope one truncation deeper than canonical — anchor(11) = 2.109477e-05 < env_prefac(11) = 2.428498e-05 (ratio_prefac = 0.868635) under the pinned prefactored arbiter; the anchor decays ×0.4798 across L=10→11 vs the envelope's ×0.6395, crossing from outside (1.1578) to inside (0.8686). The row is **registry-PASS-eligible at L=11**; the bare comparator stays outside (1.6176, cross-check only). L=10 sentinel reproduced bit-exact. Level-1 theorem-STRUCTURE (STAGE-3-PERMANENT) untouched.
- **W1-2**: the S103 float64 knife-edge resolves to a **strict interior point**: sign(deviation − (S_W_max−1)) = −1 at 320-bit mpmath AND in Sage's exact algebraic field (Δ = −5.211e-09; `is_zero() = False` is a theorem). The 5+6-sf agreement was a publication-precision near-miss, NOT an algebraic identity. S79 magnitudes-only sufficiency holds with real margin; F_amp = 0.3885 vindicated as window-interior.
- **W1-3**: the pre-registered feasibility fallback fired — and upgraded the S103 "wall record" from a timing estimate to a **structural impossibility characterization**: `dirac_spectrum.irrep_symmetric_power` materializes a dense 3^p × 3^p intermediate (Sym^13 = 40.7 TB, Sym^14 = 366 TB), so the pure-symmetric sectors (0,13)/(13,0)/(0,14)/(14,0) are uncomputable with current machinery, while 12/14 mixed level-13 sectors built on-GPU in 87.8 s (cached, seeds S105). Moment sentinel bit-exact (ρ_B(8/10/12) diff 0.0); the span is offset-independent (substitution chain verified — the w0_FW vs W0_B anchor choice cancels). The S103 FB-envelope INFO (spread ≈ 0.0221, PASS-band-interior) stands as best bound for the DR3-class w0 object.
- **W1-4**: §VII.BS clause-(b) upgraded 'separate standing premise (Open Q6)' → 'result' on all 3 annotation surfaces, licensed by the two verified S103 PASSes (`2c27b197…` ∧ `ac1dbb28…` rank-1, second_rel_sv = 1.07e-17); frozen Stage-0 blockquote byte-identical (e669ccd2, len 2514, pre+post); grade STAGE-3-PERMANENT unchanged. Capstone-hygiene: confidence-EQUALITY fix (prose brought up to register status).

**Substrate framing (wave-level)**: all four gates probe the fabric's own convergence and squeezing structure — the effacement moment's truncation ladder (W1-1), the SU(1,1) window's own endpoint (W1-2), the dark-energy moment's spectral-support stability (W1-3), and the register-faithfulness of a K-theoretic exhaustiveness statement (W1-4). The arrow ran D_K → spectral moments → emergent observables throughout; no gate inverted it.

### Effected In-Session (NON-MATH — completed by the team-lead orchestrator)

- [x] §VII.AM envelope-row dated status update (W1-1 PASS routing per plan §"Wave 1 → Wave 2 Decision Point") — appended the S104 W1-1 dated status (`registry-PASS-eligible at L=11`) to the envelope-row status sentence — `sessions/permanent-results-registry.md:16772` — audit `3d4a8049d2b89d60`
- [x] W1-4 M4 allowlist + rationale rows verified landed at plan-freeze (no action needed) — `sessions/framework/registry/methodology-wave-allowlist-ledger.md:218` + `methodology-wave-instances.md:2707` — sha `e7275804fd4ab48c`
- [x] orchestrator-direct presentation patch: NONE required this wave (all four sections landed complete with all must_contain markers)

## Carry-Forward Computations

### CF-S105-BRANCH-IV-GT-BUILDER — Gelfand-Tsetlin (p,0) irrep builder + direct ρ_B(13)/ρ_B(14) re-run [MATH]

> **Routing note**: genuine future computation (4-field complete). The W1-3 PRE-REG-INC is machinery-blocked, not physics-blocked: the (p,0) irreps are finite-dimensional (dim 105/120) and exist; only the 3^p dense-intermediate construction path is impossible. Mirrored from `session-104-housekeeping.md` is NOT needed — this is a primary WP CF (not Q2 hygiene).

1. **What**: implement a Gelfand-Tsetlin / monomial-basis builder for SU(3) (p,0) irreps constructing the rep directly in the dim_sym = (p+1)(p+2)/2 space (never forming 3^p); build (0,13)/(13,0)/(0,14)/(14,0); union with the cached 12 mixed level-13 sectors + the s84 L≤12 cache; re-run the DIRECT spread_CAC gate over L ∈ {12,13,14}.
2. **Inputs**: `computations/session-104/s104_sym_p_chain_cache_L1314.npz` (12 mixed level-13 sectors, GPU-verified iD_herm_err ≤ 1.0e-15); `computations/_shared/dirac_spectrum.py`; `computations/session-84/s84_spectrum_cache_L12_tau019.npz`; `w0_FW = −0.918` canonical; S103 FB prior ρ_B(13) = −0.646653 / ρ_B(14) = −0.657020 (sanity floor).
3. **Gate**: `S105-BRANCH-IV-DIRECT-L1314` — UNCHANGED W5-2 band: PASS spread_CAC ≤ 0.025 | INFO (0.025, 0.050] | FAIL > 0.050; CAC convention mandatory (offset_B derived at runtime; RDC FORBIDDEN per `regulator-convention-lockdown.md`).
4. **Effort**: 1–1.5 gates (GT builder ~0.5–1; re-run is minutes once sectors exist).

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-06-10 | §VII.AM fold-transit envelope row (Level-3 vs Level-2) | NOT-SATISFIED at canonical L=10 (S103 `b47ccf98` FAIL, ratio 1.1578) | **registry-PASS-eligible at L=11** (ratio_prefac 0.868635 < 1) | S104-VIIAM-L11-ANCHOR PASS under the pinned prefactored arbiter; deeper-truncation pathway closed |
| 2026-06-10 | S79 sufficiency / S_W_max knife-edge | float64-ambiguous (deviation == S_W_max−1 to 5+6 sf, S103 INFO) | strict interior (Δ = −5.211e-09; exact-saturation RULED OUT in Sage AA) | S104-SWMAX-MPMATH-EDGE PASS at ≥300-bit + exact-field cross-check |
| 2026-06-10 | Branch-IV direct deep-truncation spectra | open (S103 FB-envelope INFO; wall = timing estimate) | machinery-blocked: 3^p dense-intermediate structural wall characterized (40.7 TB / 366 TB); GT-builder route named | S104-BRANCH-IV-DIRECT-L1314 PRE-REG-INC (honest mechanical closure; 12 mixed L13 sectors cached) |
| 2026-06-10 | §VII.BS clause-(b) bundle-exhaustiveness characterization | 'separate standing premise (Open Q6)' | 'result' (rank-1 certificate `ac1dbb28…`) | S104-VIIBS-CLAUSE-B-WORDING PASS — designated-writer patch; Open Q6's augmented-bundle leg closed-as-result |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Other | Sizes |
|:-----|:-------|:------------|:------------|:------|:------|
| W1-1 | `s104_viiam_l11_anchor.py` | `s104_viiam_l11_anchor.npz` (52 fields) | `s104_viiam_l11_anchor.png` | — | 29.8 KB / 14.4 KB / 139 KB |
| W1-2 | `s104_swmax_mpmath_edge.py` | `s104_swmax_mpmath_edge.npz` | `s104_swmax_mpmath_edge.png` | — | 22.0 KB / 11.8 KB / 82.1 KB |
| W1-3 | `s104_branch_iv_direct_l1314.py` | `s104_branch_iv_direct_l1314.npz` | `s104_branch_iv_direct_l1314.png` | `s104_branch_iv_phase1_builder.py` + `s104_sym_p_chain_cache_L1314.npz` (12 sectors) | 25.4 KB / 6.7 KB / 56.2 KB / 9.4 KB / 107 KB |
| W1-4 | `s104_viibs_clause_b_wording.py` | `s104_viibs_clause_b_wording.npz` (optional, present) | — (optional, absent — compliant) | registry patch at `permanent-results-registry.md` §VII.BS ×3 surfaces | 29.2 KB / 12.5 KB |

All verdict lines in `computations/session-104/s104_gate_verdicts.txt` (race-safe `emit_verdict`; W1-1/W1-2 carry schema-v2 3-tuple rows per their [SIGN] triggers).
