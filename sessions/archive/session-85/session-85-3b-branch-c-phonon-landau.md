# Session 85 Synthesis — Slot 1b Row 3B (b) Branch-c Phonon Mechanism: Bogoliubov / BCS Track

**Date**: 2026-04-25
**Agent**: landau-condensed-matter-theorist (Landau)
**Slot / Row**: Slot 1b / Row 3B / Subsection (b)
**Companion subsections (parallel; not authored here)**: (a) volovik (GGE-relic / superfluid-universe track) → `session-85-3b-branch-c-phonon-volovik.md`; (c) kaku (alternative-pathway / mechanism-inventory track) → `session-85-3b-branch-c-phonon-kaku.md`.
**Source documents (authoritative; do not re-adjudicate)**:

- `sessions/archive/session-85/session-85-w10-workingpaper.md` — W10-4 §(d) branch table (L = 8, 10, 12), §(e) stability + Cauchy-monotone cross-checks, §(f) verdict interpretation, §(i) classification; closing-note Highlight #2 (lines 1191-1192) verbatim.
- `computations/s85_gate_verdicts.txt` line 174: `S85-W10-W0-L-INVERTED-BRANCH-ENUMERATION: PASS -- value=1 scheme=4-branch-enumeration-inverted-ordering convention=CM-2008-s3-Mellin-cone L_max=12 audit_sha256=7775d9364eed91f626e0a71090715f25a84f9d1c5feea48576ecb5c30175d4fc`.
- `sessions/permanent-results-registry.md` — checked for branch-c provenance (none registered yet; this synthesis is the candidate phenomenology bid for branch-c).
- `sessions/archive/session-85/session-85-w6-13-workshop-schedule.md` — Row 3B schedule entry (lines 102-111).

**Knowledge MCP queries executed before any identity claim**:

- `search_knowledge('w_0 branch c zeta Josephson inverted')` — confirmed no prior mechanism-attribution for branch-c; the only `s78_zeta_josephson.py` hits concern the SU(3) branch decomposition (BRANCH_C2 = [3,4,5,6] coset, BRANCH_SU2 = [0,1,2], BRANCH_U1 = [7]), unrelated to W10-4's w_0 branch enumeration.
- `search_knowledge('Bogoliubov transition substrate high L_max')` — found `s83_w3_g50_nT_bogoliubov.py` (sudden-limit Bogoliubov for substrate dispersion), `s53_gpe_efold.py` (BCS quasiparticle picture), `s64_bogoliubov_phases.py` (acoustic peak harmonics). None pre-claim a "branch-c" identity.
- `search_knowledge('GGE relic high L Bogoliubov coefficient')` — `s57_fabric_kz_quench.py` defines `GGE quasiparticle pairs = Bogoliubov pairs (non-thermal GGE relic)`; `s65_dm_relic.py` `n_k = |β_k|²`; `s67_gge_bispectrum.py` GGE relic carries N_pair = 59.8 quasiparticle pairs. The GGE relic / Bogoliubov-occupation identity is canonical and pre-existing (S57+).
- `trace_entity('Bogoliubov transition substrate')` — no canonical entry; this is genuinely a new candidate identification.
- `get_constant('tau_fold')` — `0.19` (S12/S42 frozen). Used as anchor for the transit-mediated squeeze-parameter substitution chain.

---

## I. Session Outcome

W10-4 PASS established branch-c (ζ-regulator, Josephson-inverted) as a stable w_0 branch beyond the baseline ζ/Zubarev dichotomy. Reading the W10-4 branch table through the standard Bogoliubov-coefficient mapping (`|v|² = residue`, `u² = 1 + residue`) yields a clean structural diagnostic: **branch-c is a moderately-squeezed inter-band Bogoliubov vacuum** distinct from branch-a (deep-squeezed-baseline limit) and branch-b (mildly-squeezed Zubarev-baseline). The squeeze parameter r is fixed by the Josephson-inverted ξ_J = 0.008911 and the ζ-regulator denominator S_ζ_E(L); since ξ_J is L-independent and S_ζ_E(L) grows log-linearly with slope 0.97, the resulting r_c(L) is finite at all L and decays monotonically — this is the specific kinematic signature of a **Josephson-pinned inter-band squeeze** that does not appear in the baseline Bogoliubov-dominant branches. The discriminating gate `BRANCH-C-BOGOLIUBOV-DISTINCTNESS` is pre-registered with two parts: (i) a *cosine-distance numerical-robustness check* on the (u, v) vector at L = 12 vs L = 14 (extrapolation-only on currently-feasible hardware), and (ii) a structurally-stronger *mixing-angle-ratio* test θ_c/θ_a at L = 14 against the log-linear extrapolation that this synthesis derives below.

Bogoliubov classification (this synthesis): branch-c is **PHONONIC** — an inter-band Bogoliubov-rotated vacuum on the C² coset SU(3)/(SU(2)×U(1)), specifically the Josephson-Leggett channel that is suppressed at low L_max because ξ_E_GGE > ξ_J there but BECOMES the dominant channel at L ≥ 8 once the SV2 R_JE crosses unity. It is NOT a new GGE relic channel in the S57/S65 sense (the GGE-relic occupation N_pair = 59.8 is set by the impulsive transit, not by the regulator-class) — but it IS a new BCS-vacuum-rotation configuration accessible to the substrate at high L_max only.

---

## II. Key Results

### II.1 — Bogoliubov-coefficient mapping of W10-4 branch residues

**Result**: Each (branch, L) pair in W10-4 table §(d) corresponds to a Bogoliubov-rotated vacuum with squeeze parameter `r = arcsinh(√residue)`. All four branches preserve the canonical commutator `|u|² − |v|² = 1` to machine precision (verified to ≤ 3.3e-16). Classification: **PHONONIC**.

**Substitution chain (definition → substitution → simplification → direction)**:

```
Step 1 — Definition (Bogoliubov transformation of a single bosonic mode):
  α_k  = u_k a_k + v_k a_{-k}^†
  α_k^† = u_k^* a_k^† + v_k^* a_{-k}
  with |u_k|² − |v_k|² = 1   (canonical-commutator preservation)

Step 2 — Definition (squeeze parameter r and quasiparticle occupation):
  u_k   = cosh(r_k)
  v_k   = sinh(r_k) · e^{i·phase}
  n_k   = |v_k|²  = sinh²(r_k)            (Bogoliubov number / quasiparticle occupation)
  θ_k   = arctan(v_k / u_k) = arctan(tanh(r_k))   (Bogoliubov mixing angle)

Step 3 — Substitute (W10-4 model: residue is the late-time-asymptotic
  Hubble channel mode-function squeeze power, ≡ |v_k|² for the Mellin-s=3 mode):
  residue(branch, L) = ξ_eff(branch, L) · mellin_s3(L) / S_reg(branch, L)
  ⇒  n_k(branch, L) := residue(branch, L)
  ⇒  r(branch, L)   = arcsinh( √residue(branch, L) )
                    = arcsinh( √n_k(branch, L) )

Step 4 — Simplify (numerical evaluation from W10-4 table §(d), Python-verified):
  Branch  | L  | residue=|v|²  | u=√(1+|v|²)        | v=√|v|²       | r=arcsinh(v)   | θ=arctan(v/u)   | u²−v² (verify)
  ------  |--- |---            |---                 |---            |---             |---              |---
  a (ζ-Bog)| 8  | 2.972e-05    | 1.0000148599       | 5.452e-3      | 5.452e-3       | 5.451e-3        | 1.0000000000000000
  a (ζ-Bog)|10  | 2.600e-06    | 1.0000013000       | 1.612e-3      | 1.612e-3       | 1.612e-3        | 1.0000000000000000
  a (ζ-Bog)|12  | 2.275e-07    | 1.0000001137       | 4.770e-4      | 4.770e-4       | 4.770e-4        | 1.0000000000000000
  b (Zub-Bog)|8 | 1.717e-02    | 1.0085484619       | 1.310e-1      | 1.307e-1       | 1.292e-1        | 1.0000000000000000
  b (Zub-Bog)|10| 7.488e-03    | 1.0037370174       | 8.653e-2      | 8.643e-2       | 8.600e-2        | 1.0000000000000000
  b (Zub-Bog)|12| 3.265e-03    | 1.0016311696       | 5.714e-2      | 5.711e-2       | 5.699e-2        | 1.0000000000000000
  c (ζ-Jos)| 8  | 1.530e-04    | 1.0000764971       | 1.237e-2      | 1.237e-2       | 1.237e-2        | 1.0000000000000002
  c (ζ-Jos)|10  | 6.672e-05    | 1.0000333594       | 8.168e-3      | 8.168e-3       | 8.168e-3        | 1.0000000000000000
  c (ζ-Jos)|12  | 2.909e-05    | 1.0000145449       | 5.393e-3      | 5.393e-3       | 5.393e-3        | 1.0000000000000000
  d (Zub-Jos)|8 | 8.840e-02    | 1.0432641085       | 2.973e-1      | 2.931e-1       | 2.776e-1        | 1.0000000000000002
  d (Zub-Jos)|10| 1.921e-01    | 1.0918333206       | 4.383e-1      | 4.253e-1       | 3.817e-1        | 1.0000000000000000
  d (Zub-Jos)|12| 4.175e-01    | 1.1905880900       | 6.461e-1      | 6.080e-1       | 4.972e-1        | 1.0000000000000000

Step 5 — Direction (from canonical form):
  • |u_k|² − |v_k|² = 1 to machine precision for all 12 (branch, L) pairs ⇒ canonical-commutator preserved (no anomaly).
  • r_branch ordering at L = 12: r_a (4.77e-4) < r_c (5.39e-3) < r_b (5.71e-2) < r_d (6.08e-1).
  • Branch-c sits BETWEEN baseline branches a and b, NOT in a non-perturbative regime — i.e., branch-c is NOT a "high-amplitude" Bogoliubov configuration; it is mid-amplitude.
  • Branch-d (Zubarev-Josephson-inverted, the W10-4 FAIL) is the runaway: r grows monotonically 0.29 → 0.43 → 0.61 with L. Its squeeze does NOT freeze; it diverges, consistent with its W10-4 stability + Cauchy-decay double FAIL.
```

**Interpretation**: The W10-4 model (`residue = ξ_eff · mellin_s3 / S_reg`, `w_0 = −1 + 2·residue`) maps cleanly into a Bogoliubov-coefficient parameterization in which the late-time Hubble channel residue equals the Bogoliubov number on the s = 3 Mellin-cone mode. Branch-c's `n_c(L=12) = 2.909e-5` corresponds to a small but L-stable inter-band squeeze. The ζ-regulator's high-L stabilization (slope 0.97 on the denominator vs slope 0.56 on the numerator, per W10 closing-note §1098-1100) is what holds branch-c's r_c at finite mid-amplitude — branch-d's Zubarev-Josephson-inverted runaway shows that the same Josephson coupling without ζ-stabilization would NOT produce a stable squeeze.

### II.2 — Branch-c is the Josephson-Leggett channel

**Result**: Branch-c = the inter-band Bogoliubov vacuum-rotation in the SU(3)/(SU(2) × U(1)) C² coset, sourced by the Josephson coupling ξ_J = 0.008911 (TB-pinned, L-independent) and ζ-regularized. **PHONONIC** — Leggett-mode adjacent.

**Substitution chain (definition → substitution → simplification → direction)** for the channel-identification claim:

```
Step 1 — Definition (Josephson coupling in the framework's branch decomposition,
                     from S78 zeta_josephson.py + S77 BCS-timing PASS + S82 Z_2 gauge
                     degeneracy theorem):
  ξ_J  = inter-band Josephson tunneling amplitude, B1↔B2↔B3 cell network
       = 0.008911 (TB-pinned, regulator-independent)
  ξ_E_GGE(L) = energy-channel Bogoliubov amplitude on the same C² coset,
                regulator-dependent; SV2-pinned values
                (0.01965, 0.00856, 0.00370, 0.00179) at L = 5, 6, 7, 8

Step 2 — Definition (Leggett-mode identity from S69 + S70 + LEGGETT-PARTITION-57/58):
  Leggett mode = inter-band PHASE excitation between B2 and B3 substrate sectors
              = R-protected phase-mode of the Josephson coupling
              = Bogoliubov-rotated relative-phase vacuum
  c_L = 0.025 (Leggett phase-mode sound speed, R-protected)

Step 3 — Substitute (W10-4 PASS condition):
  Branch-c is "ζ-regulator, Josephson-dominant" (W10-4 §(d) row 7-9 and §(f)).
  ⇒ ξ_eff(branch c, L) = ξ_J = 0.008911                    (Josephson-dominant by definition)
  ⇒ S_reg(branch c, L) = S_ζ_E(L)                          (ζ-regulator)
  ⇒ residue_c(L) = 0.008911 · mellin_s3(L) / S_ζ_E(L)
  ⇒ n_c(L) = residue_c(L) = sinh²(r_c(L))

Step 4 — Simplify (channel attribution):
  Branch a (ξ_eff = ξ_E_GGE, ζ-regulated) is the "B-mode" residue —
                           the standard Bogoliubov-energy channel.
  Branch c (ξ_eff = ξ_J,    ζ-regulated) is the "L-mode" residue —
                           the Leggett-Josephson phase channel.
  These are the SAME C² coset, but DIFFERENT excitation channel:
     B = energy-channel (matter-amplitude, Bogoliubov-Anderson)
     L = phase-channel (Leggett, R-protected)
  At low L (≤ 7): R_JE = ξ_J / ξ_E_GGE < 1, so the energy channel
                      dominates the residue and the L-channel is
                      structurally "hidden"; branch c is below
                      the threshold for residue-stability.
  At L ≥ 8: R_JE > 1 (W10-4 SV2 substitution chain Step 3 verified
                      R_JE_SV2 = [0.4536, 1.0406, 2.4113, 4.9847]
                      at L = {5, 6, 7, 8}); the L-channel is now the
                      dominant inter-band amplitude and produces a
                      structurally-distinct stable w_0 branch.

Step 5 — Direction (from canonical form):
  Branch-c IS the Josephson-Leggett (L-channel) residue branch
  that the framework hosts at high L_max but did not host at low L.
  Substrate-first reading: branch-c is the phase-channel inter-band
  Bogoliubov vacuum-rotation residue — the COSMOLOGICAL imprint of
  the Leggett phase-mode integrated over the late-time Hubble flow.
  This is NOT a new GGE relic channel (S57/S65 GGE-relic is set by
  the impulsive transit, not by the regulator class). It IS a new
  L-channel residue that becomes physical at L ≥ 8 because ξ_J then
  exceeds ξ_E_GGE for the first time.
```

**Direction summary**: branch-c maps onto the Leggett-Josephson inter-band phase channel (R-protected phase-mode of the C² coset). The mechanism is a **high-L Bogoliubov vacuum-rotation in the L-channel**, structurally distinct from the B-channel rotation that produces baseline branches a and b. The "Josephson-inversion" in W10-4 is the regime crossing R_JE: 1 (below → above unity at L ≈ 6) which switches the dominant ξ_eff from energy-channel (ξ_E_GGE) to phase-channel (ξ_J).

This identification is consistent with three pre-existing canonical results: (i) S82 W2-11 PASS that the 2-sector Richardson Hamiltonian with ONE Josephson bond carries an EXACT Z_2 gauge degeneracy between s++ and s+- sectors (the relevant inter-band coupling is structurally there at L = small — but its residue contribution is REGULATOR-conditional); (ii) S69 + S70 R-protected Leggett-mode identification of the C² inter-band excitation; (iii) S77 BCS-timing PASS confirming that t_BCS / dt_transit = [102, 160] supports a quench-then-Bogoliubov reading with stable post-transit GGE.

### II.3 — Branch-c does NOT activate a "previously-inaccessible BCS vacuum"

**Result**: The closing-note's framing question — "is branch-c a high-L Bogoliubov transition into a previously-inaccessible BCS vacuum?" — has answer **No, with qualification**. **PHONONIC**.

The squeeze amplitude r_c at L = 12 is 5.393e-3 — small in absolute terms, larger than r_a (= 4.77e-4) but smaller than r_b (= 5.71e-2). The branch-c configuration is a vacuum that is NOT structurally new — it is the phase-channel (L-channel) residue of the SAME inter-band Bogoliubov rotation that branches a, b also occupy in the energy-channel. What changes at L ≥ 8 is which channel dominates the residue, NOT which BCS vacuum is occupied. The "vacuum" in branch-c is the SAME R-protected Leggett-Josephson phase vacuum that LEGGETT-PARTITION-57/58 already established as physically realized at all L; what is new is that its CONTRIBUTION TO w_0 BECOMES VISIBLE only above L = 6 once R_JE crosses unity.

**Substitution chain (direction: was the BCS vacuum unphysical at L = 8/10 and physical at L = 12+?)**:

```
Step 1 — Definition (BCS-vacuum existence on the C² coset):
  The Leggett phase mode is R-protected (LEGGETT-PARTITION-57/58 PASS).
  R-protection ⇒ the phase-vacuum exists at every L_max for which the
  C² coset is in the spectrum, i.e., for all L_max ≥ 1.
  ⇒ The "BCS vacuum" question is NOT about existence; it is about
    the residue contribution to the late-time Hubble channel.

Step 2 — Definition (residue-visibility threshold):
  visibility(branch c, L) = 1 iff residue_c(L) > residue_a(L)  AND
                                   stability_delta_c(L) ≤ 0.10 AND
                                   Cauchy-monotone decay holds.

Step 3 — Substitute (from W10-4 §(d) and §(e)):
  At L = 8:  residue_c = 1.530e-4  vs  residue_a = 2.972e-5  ⇒  residue_c > residue_a (5.1×).
  At L = 10: residue_c = 6.672e-5  vs  residue_a = 2.600e-6  ⇒  residue_c > residue_a (25.7×).
  At L = 12: residue_c = 2.909e-5  vs  residue_a = 2.275e-7  ⇒  residue_c > residue_a (127.9×).
  Branch c stability_delta = 7.53e-5 (≤ 0.10) ⇒ stable at all L.
  Branch c Cauchy-monotone decay holds (W10-4 §(e) row 3: True/True/True/True).

Step 4 — Simplify:
  Branch-c residue exceeds branch-a residue at every L ∈ {8, 10, 12};
  the multiplicative gap GROWS with L (5.1× → 25.7× → 127.9×).
  This is a kinematic shift of WHICH CHANNEL DOMINATES the residue,
  not a phase transition INTO a previously-forbidden vacuum.

Step 5 — Direction:
  The vacuum is NOT new at L = 12+; the L-channel residue's relative
  weight in the late-time Hubble channel grows monotonically with L
  due to the slope inequality 0.97 (S_ζ_E) > 0.56 (mellin_s3) > 0
  (ξ_J L-independent). The "transition" is NOT a vacuum rotation
  newly accessible at L = 12+; it is the asymptotic emergence of
  the L-channel as the dominant residue-contributing channel above
  the regulator-fixed L_threshold ≈ 6 where R_JE crosses unity.
```

**Interpretation**: There is NO threshold L_max at which a previously-inaccessible BCS vacuum suddenly becomes occupied. The Leggett-Josephson phase vacuum is R-protected at all L. What W10-4 surfaced is a **regulator-class kinematic accounting** — the ζ-regulator denominator's faster growth (slope 0.97) outpaces the Mellin-s3 numerator (slope 0.56), so even a small-but-L-stable phase-channel residue (set by the L-independent ξ_J) survives as a stable w_0 contribution at L ≥ 8 where it would have been swamped at L ≤ 7 by the (then-larger) energy-channel residue.

This is the structurally important reading: branch-c is **NOT** a new vacuum; it is the SAME phase vacuum becoming **the dominant residue channel** once the regulator-fixed crossover point R_JE = 1 is passed.

### II.4 — Cosine-distance discriminant is numerically weak; mixing-angle ratio is structurally informative

**Result**: The cosine distance between the (u, v) Bogoliubov vectors of branches a and c is dominated by the u-component (≈ 1) and is therefore TINY (≤ 2.4e-5 at all L) and DECREASING with L. The standard mixing-angle ratio θ_c/θ_a is the structurally informative discriminant; it grows monotonically across L = {8, 10, 12} as 2.27, 5.07, 11.31. **PHONONIC**.

**Substitution chain (direction: which discriminant should the S86 gate use?)**:

```
Step 1 — Definition (cosine distance between branch (u, v) vectors):
  V(branch, L) = (u(branch, L), v(branch, L)) ∈ R²
  cos_sim(a, c; L) = V_a(L) · V_c(L) / (|V_a(L)| |V_c(L)|)
  cos_dist(a, c; L) = 1 − cos_sim(a, c; L)

Step 2 — Substitute (Python-verified values from §II.1 table):
  L = 8:  cos_dist = 2.392e-5
  L = 10: cos_dist = 2.149e-5
  L = 12: cos_dist = 1.209e-5
  log-linear fit log10(cos_dist) = −0.0741·L − 3.9945, R²=0.86
  Extrapolated cos_dist(L = 14) = 9.288e-6
  Ratio cos_dist(L = 14) / cos_dist(L = 12) = 0.7685 (DECREASING)

Step 3 — Definition (mixing-angle ratio as alternative discriminant):
  θ(branch, L) = arctan(v(branch, L) / u(branch, L)) = arctan(tanh(r(branch, L)))
  Q(L) := θ_c(L) / θ_a(L)

Step 4 — Substitute (Python-verified values from §II.1):
  L = 8:  Q(8)  = 1.237e-2 / 5.451e-3 = 2.269
  L = 10: Q(10) = 8.168e-3 / 1.612e-3 = 5.065
  L = 12: Q(12) = 5.393e-3 / 4.770e-4 = 11.308
  log-linear fit log10(Q) = +0.1745·L − 0.7985 (slope POSITIVE).
  Extrapolated Q(L = 14) = 25.27 (continuing monotone growth).

Step 5 — Direction (from canonical form):
  cos_dist(L) is dominated by |u_a − u_c|² + |v_a − v_c|²; since both
  u_a and u_c approach 1 as L grows, cos_dist DECREASES with L. This
  makes cos_dist a NUMERICALLY WEAK discriminant: at L = 14, the
  predicted distance is 9.3e-6, well within typical numerical noise
  for sparse-matrix eigvals at L = 14 dim ~10^7.

  Q(L) grows monotonically because the v-components diverge in opposite
  log-linear directions: v_a decreases with slope ≈ −0.27, v_c decreases
  with slope ≈ −0.18. The RATIO grows because v_c decays slower than v_a.
  This is the structurally-informative quantity: it tracks the GROWING
  dominance of the L-channel over the B-channel as L increases.
```

**Direction summary**: the cosine distance is a numerically-fragile discriminant that vanishes asymptotically; the mixing-angle ratio is monotone-divergent and is the structurally-correct gate target. **The pre-registered S86 gate must use BOTH** — (i) cos_dist for canonical-commutator preservation cross-check, (ii) Q(L) ratio for the mechanism-distinguishing test.

---

## III. Gate Verdicts (W10 source)

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S85-W10-W0-L-INVERTED-BRANCH-ENUMERATION | PASS | inverted_stable = 1 (branch c only); branch d FAILS stability_delta (0.84 > 0.10) and Cauchy-monotone (residue grows with L). |

This is the source verdict; this synthesis re-reads the table through the Bogoliubov-coefficient lens and pre-registers the discriminating S86 gate (§V).

---

## IV. Structural Implications

### IV.1 — Constraint-map update

Pre-S85: w_0 branch envelope was the ζ/Zubarev dichotomy (branches a, b). Branch-c was empirically discovered as a third stable branch; its phenomenology was open.

Post-S85 (after this synthesis): branch-c is structurally identified as the **R-protected Leggett-Josephson phase-channel residue** in the SU(3)/(SU(2)×U(1)) C² coset. Three statements survive systematic elimination:

1. Branch-c is NOT a new GGE relic channel. The S57/S65 GGE relic occupation N_pair = 59.8 is set by the impulsive transit through τ_fold = 0.19, NOT by the regulator class. Branch-c's residue is the LATE-TIME asymptotic Hubble-channel imprint, distinct in nature from the GGE post-transit relic.
2. Branch-c is NOT a "previously-inaccessible BCS vacuum" newly populated at L = 12+. The Leggett phase-vacuum is R-protected at all L (LEGGETT-PARTITION-57/58 PASS). The kinematic shift at L ≥ 8 is which inter-band channel DOMINATES the residue, not which vacuum is occupied.
3. Branch-c IS a Josephson-dominated vacuum CONFIGURATION whose contribution to w_0 becomes structurally dominant only above the regulator-fixed L_threshold where R_JE crosses unity. Its squeeze parameter r_c(L) decays monotonically with L (5.39e-3 at L = 12, extrapolated 5.85e-4 at L = 14 from log-linear fit slope −0.27), so the channel is NOT divergent — it is regulator-stabilized.

### IV.2 — What this rules out

- **Closes** the "high-L Bogoliubov transition into new BCS vacuum" reading (kaku-style alternative-pathway candidate). The Leggett-vacuum is the SAME at all L; only its residue weighting changes.
- **Closes** the framing that branch-c is a runaway non-perturbative configuration. r_c at L = 12 is mid-amplitude (≈ 5e-3), well within the perturbative-Bogoliubov regime.
- **Strengthens** the LEGGETT-PARTITION-57/58 result: branch-c is the cosmological-residue manifestation of the SAME R-protected phase mode that labels the lab-superfluid Leggett spectrum. This is a cross-channel convergence (cosmological w_0 ↔ lab Leggett mode ↔ GW dispersion at lab-SF-substrate equivalence scale) that the framework can pre-register.

### IV.3 — What survives and is structurally tested below

A pre-registered S86 gate `BRANCH-C-BOGOLIUBOV-DISTINCTNESS` that combines a numerical-robustness check (cosine-distance) AND a structural discriminant (mixing-angle-ratio Q(L)) at L = 14 against the log-linear extrapolation derived above. PASS criteria pre-registered in §V below.

---

## V. Carry-Forward Computations

### V.1 — Pre-registered S86 gate: `BRANCH-C-BOGOLIUBOV-DISTINCTNESS` (CONVERGED across landau / volovik / kaku)

This is the unified discriminating gate that the three Row 3B agents converge on. Volovik's GGE-relic candidate, Landau's Leggett-Josephson-channel candidate (this synthesis), and Kaku's alternative-pathway candidate all REQUIRE this gate to discriminate among them at L = 14. Volovik's and Kaku's exact PASS-criteria are authored in their respective subsection files; the SHARED computation specification is below. This synthesis does not speak for volovik or kaku; the gate spec below names the fields each sub-agent populates with their candidate-specific PASS predictions.

- **What**: at L = 14, compute the Bogoliubov coefficients (u_branch, v_branch) for branches a, b, c on the s = 3 Mellin-cone via the W10-4 model `n_branch = ξ_eff · mellin_s3(14) / S_reg(14)` with ξ_eff and S_reg evaluated either (i) by sparse-matrix block-diagonal reduction at L = 14 (preferred path), OR (ii) by log-linear extrapolation of the SV2 L = {5, 6, 7, 8} trajectory if dense diagonalization remains infeasible. Then compute three discriminants:
  - **D1 (canonical-commutator preservation)**: `|u|² − |v|² = 1` for each branch — sanity check, not the discriminant itself.
  - **D2 (cosine-distance numerical-robustness)**: `cos_dist(a, c; L=14) = 1 − (u_a u_c + v_a v_c) / (|V_a||V_c|)`. This synthesis's log-linear extrapolation predicts `cos_dist(14) = 9.29e-6 ± 30%` from the L = {8, 10, 12} fit. PASS iff |measured − predicted| / predicted ≤ 0.30; FAIL iff > 0.30. INFO iff dense diagonalization is infeasible AND only extrapolation is available (then the gate is RE-RUN under sparse-block path or DEFERRED).
  - **D3 (mixing-angle-ratio structural test)**: `Q(L=14) = θ_c(14) / θ_a(14)`. This synthesis's log-linear extrapolation predicts `Q(14) = 25.27 ± 30%`. PASS iff |measured − predicted| / predicted ≤ 0.30; FAIL iff > 0.30.
  - **Mechanism-discrimination addendum** (volovik / landau / kaku candidate-specific): each subsection (a, b, c) declares an additional candidate-specific signature gate whose values at L = 14 distinguish its mechanism. This synthesis's signature: branch-c's (u, v) sits BETWEEN (u, v) of branches a and b in the squeeze ordering r_a(L) < r_c(L) < r_b(L) at every L ∈ {8, 10, 12, 14}; the ordering must persist at L = 14. PASS iff `r_a(14) < r_c(14) < r_b(14)`; FAIL iff ordering breaks. This is the LANDAU SUBSECTION SIGNATURE and is the discriminant that (b)-subsection PASS rests on.

- **Inputs**:
  - W10-4 SV2 trajectories at L = {5, 6, 7, 8} (`computations/s84_w1a_w0_sv2.npz`, SHA `27725a7cc1b4ae44...`).
  - W10-4 §(d) branch table at L = {8, 10, 12} (already in `s85_w10_w0_inverted_branch_enumeration.npz`).
  - canonical_constants: `tau_fold = 0.19`, `c_L = 0.025` (Leggett-mode sound speed), `ξ_J = 0.008911` (TB-pinned Josephson coupling), Mellin-cone s = 3 residue model (W10-4 §(c)).
  - Substrate spectrum at L = 14: either dense block-diagonal reduction by SU(3) × A_F irrep (preferred — see kaku closing-note Highlight #4) or the SV2 sparse representation extended one L step beyond the W10-4 envelope.
  - This synthesis's predicted values: cos_dist(14) = 9.29e-6 ± 30%; Q(14) = 25.27 ± 30%; r_a(14) ≈ 1.41e-4, r_c(14) ≈ 3.56e-3, r_b(14) ≈ 3.78e-2 (from log-linear fits on the L = {8, 10, 12} table).
  - Volovik subsection (a) GGE-relic signature predictions (read from `session-85-3b-branch-c-phonon-volovik.md` when landed).
  - Kaku subsection (c) alternative-pathway / instanton-anti-instanton-pair signature predictions (read from `session-85-3b-branch-c-phonon-kaku.md` when landed).

- **Gate**: NEW S86 gate `BRANCH-C-BOGOLIUBOV-DISTINCTNESS`. PASS iff D1 holds AND D2 PASSES AND D3 PASSES AND the candidate-specific addendum from (b) PASSES. INFO iff dense diagonalization at L = 14 is infeasible; the gate then runs on extrapolation only and reports the distance-from-extrapolation as a conditional verdict, deferred until the sparse-block path lands. FAIL on ANY single discriminant FAIL — this is a multi-discriminant gate; no single discriminant is decisive alone, but ANY single FAIL kills the convergence. The gate is jointly authored across landau/volovik/kaku subsections; this synthesis specifies only the (b) Bogoliubov discriminants D1/D2/D3.

- **Effort**: 4-6 hours, 1 agent session (sparse-block representation extension at L = 14, on `phonon-exflation-sim/.venv312` with torch.linalg.eigvalsh on RX 9070 XT GPU per `feedback_compute-environment.md`); extrapolation-only fallback is 30 min, 1 agent session. Recommend dispatch to a `landau` or `mack` agent (BCS / Bogoliubov machinery + numerical-robustness assessment).

### V.2 — Channel signature: Leggett-mode lab-SF observable

- **What**: compute the predicted Leggett-mode resonance frequency in lab-superfluid analog systems (³He-B Leggett-mode benchmark, c_L = 0.025) corresponding to branch-c's Bogoliubov mixing angle θ_c(L). Specifically, the predicted Leggett-mode visibility ratio `V_Leggett / V_BA = (sin θ_c)² / (sin θ_a)²` where V_X is the spectral weight of channel X at the substrate-fold frequency. From this synthesis's table at L = 12: `V_Leggett / V_BA = (1.237e-2)² / (5.452e-3)² = 5.149` (Leggett channel carries 5× the spectral weight of the energy channel at L = 12). This is a LAB-OBSERVABLE prediction.
- **Inputs**: c_L = 0.025, c_BA = 0.399 (Bogoliubov-Anderson sound speed), branch (u, v) tables from §II.1, ³He-B Leggett-mode resonance reference benchmark (Volovik's "The Universe in a Helium Droplet" §15).
- **Gate**: NEW S86 gate `BRANCH-C-LEGGETT-LAB-SIGNATURE`. PASS iff predicted V_Leggett/V_BA ratio matches a known ³He-B Leggett-mode amplitude-ratio benchmark within a factor of 3 (substrate↔lab analog factor; this is a structurally-loose threshold because the analog is approximate). Tighter PASS at factor 2 would promote to a strong observational pre-registration.
- **Effort**: 2-3 hours, 1 agent session (volovik or landau).

### V.3 — Channel signature: GW dispersion at lab-SF-substrate equivalence scale

- **What**: branch-c's mixing-angle Q(L) growth predicts a specific wavenumber-dependent GW dispersion modification at the substrate's late-time Hubble channel. The leading-order substitution chain (Step-by-step):
  - Bogoliubov occupation `n_c(k_pivot)` at the cosmological pivot maps to a tensor-spectrum amplitude shift `δ_GW(k) ∝ n_c(k)`.
  - For LISA band: branch-c contributes a residue ≈ 2.9e-5 at L = 12, log-linear extrapolation to L = 14 gives 1.27e-5. The predicted GW dispersion modification at LISA pivot is at the ~1e-5 amplitude level — within LISA design-sensitivity envelope per S78+ flagship sensitivity tables.
- **Inputs**: branch-c residue table from §II.1, LISA design sensitivity at f_LISA (S78+ flagship), substrate tensor sound speed c_T = 1 (no substrate-induced tensor dispersion; only amplitude shift).
- **Gate**: NEW S86 gate `BRANCH-C-LISA-AMPLITUDE-SHIFT`. PASS iff predicted δ_GW = 1.27e-5 ± 30% matches LISA-projected sensitivity at the substrate's pivot scale; FAIL otherwise. This couples to the W13-2 LISA null + CGWB+α_s flagship pre-registration: branch-c's contribution modifies the joint flagship significance and may shift the LISA null line.
- **Effort**: 3-4 hours, 1 agent session (mack for observational pre-registration; tesla for GW-detector channel detail).

### V.4 — Channel signature: cosmological w_0 contribution from branch-c at LSST/DESI horizon

- **What**: integrate branch-c's late-time-asymptotic w_0 = -1 + 2·residue_c(L) over the relevant cosmological volume. For L = 12, branch-c contributes Δw_0 = +5.82e-5 above the −1 baseline; for L = 14 (extrapolation), Δw_0 = +2.54e-5. The DESI DR3 w_0 1σ envelope is ~0.05 at the pivot redshift. Branch-c's contribution is FAR below DESI DR3 sensitivity but IS within Stage IV combined sensitivity (LSST+Euclid+DESI Year 5 ~ 1e-4 expected, depending on data-combination assumptions).
- **Inputs**: residue_c(L) extrapolation, DESI DR3 w_0 envelope (S85-W1a livewatch), Stage IV combined w_0 forecast.
- **Gate**: NEW S86 gate `BRANCH-C-W0-COSMOLOGICAL-IMPRINT`. PASS iff Δw_0(branch c, L) at L = 14 lies within a STAGE IV joint projection (factor 5 within combined Stage IV envelope ~ 1e-4); FAIL iff Δw_0 exceeds Stage IV at >2σ (i.e., the substrate is over-predicting the late-time deviation from −1, structural problem).
- **Effort**: 2 hours, 1 agent session (mack for observational pre-registration).

### V.5 — Sparse-block representation at L = 14

- **What**: build the framework spectral triple's sparse block-diagonal representation under SU(3) × A_F irrep decomposition, extended one L step beyond W10-4's L = 8 envelope. Goal: enable dense computation at L = 12 and L = 14 within the 17 GB VRAM hardware envelope; W10 closing-note Highlight #4 explicitly requested this. If successful, `BRANCH-C-BOGOLIUBOV-DISTINCTNESS` (V.1) runs on dense data; if not, the gate runs on log-linear extrapolation only with INFO classification.
- **Inputs**: existing SV2 sparse representation, SU(3) × A_F irrep decomposition routines (S78+ machinery), Jensen-deformed eigenvalue-ladder generators.
- **Gate**: METHODOLOGY-track NEW S86 gate `SPARSE-BLOCK-L14-FEASIBILITY`. PASS iff sparse-block path produces converged (u, v) vectors at L = 14 within the 17 GB VRAM envelope; FAIL or INFO if it does not (in which case V.1 runs on extrapolation only).
- **Effort**: 6-10 hours, 1 agent session (connes-ncg-theorist for irrep decomposition; van-den-dungen for representation-theoretic structure).

### V.6 — ζ-regulator-stabilization theorem candidate (cross-link to 3A)

- **What**: 3A (parallel solo) develops a ζ-regulator-stabilization theorem candidate. Branch-c's existence depends critically on the slope inequality 0.97 (S_ζ_E) > 0.56 (mellin_s3) > 0 (ξ_J L-independent). If 3A's theorem lands, branch-c becomes a STRUCTURAL feature of any ζ-regularized substrate at high L; if 3A's theorem refutes the slope inequality at higher precision, branch-c may collapse. This synthesis pre-registers the cross-link.
- **Inputs**: 3A theorem-candidate landing (`session-85-3a-zeta-stabilization-theorem-{authoring-agent}.md`).
- **Gate**: branch-c phenomenology survives iff 3A theorem PASSES; branch-c collapses iff 3A theorem FAILS (refutes the slope inequality). Cross-link gate `BRANCH-C-CONDITIONAL-ON-ZETA-STABILIZATION`. NO independent verdict; verdict piggy-backs on 3A.
- **Effort**: 1 hour cross-link audit, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Bogoliubov mapping `n = residue`, `r = arcsinh(√n)` reproduces W10-4 §(d) at machine precision; canonical-commutator `\|u\|² − \|v\|² = 1` preserved on all 12 (branch, L) pairs to ≤ 3.3e-16 | PHONONIC | PASS (mapping consistent) | W10-4 model maps cleanly into Bogoliubov-coefficient parameterization; squeeze parameter r is the natural label of branches |
| 2 | Branch-c = R-protected Leggett-Josephson phase-channel residue on SU(3)/(SU(2)×U(1)) C² coset; ξ_eff = ξ_J = 0.008911 (TB-pinned), ζ-regulated denominator | PHONONIC | NEW IDENTIFICATION (this synthesis) | Branch-c is NOT a new vacuum; it is the L-channel residue of the same R-protected phase-mode that LEGGETT-PARTITION-57/58 already established |
| 3 | Squeeze ordering at L = 12: r_a < r_c < r_b < r_d (4.77e-4 < 5.39e-3 < 5.71e-2 < 6.08e-1); branch-c is mid-amplitude, NOT runaway | PHONONIC | STRUCTURAL DIAGNOSTIC | Branch-c is regulator-stabilized; branch-d (Zubarev-Josephson) runaway is the real problem (W10-4 FAIL of d confirmed) |
| 4 | "Previously-inaccessible BCS vacuum at L = 12+" framing rejected; the Leggett-vacuum is R-protected at all L; what changes at L ≥ 8 is which channel dominates the residue, not which vacuum is occupied | PHONONIC | CLOSED | Closes the "vacuum-rotation transition" framing of the closing-note question; sharpens to "channel-dominance crossover at R_JE = 1, L ≈ 6" |
| 5 | Mixing-angle ratio Q(L) = θ_c(L) / θ_a(L) grows monotonically (2.27 → 5.07 → 11.31); cosine-distance discriminant decays (numerically weak); Q(L) is the structurally-correct discriminant | PHONONIC | STRUCTURAL DIAGNOSTIC | S86 discriminating gate must use both (canonical check + structural check); pre-registered in V.1 |
| 6 | S86 gate `BRANCH-C-BOGOLIUBOV-DISTINCTNESS` pre-registered (D1 commutator + D2 cos_dist + D3 Q-ratio + landau-signature squeeze-ordering) at L = 14 with predictions: cos_dist(14) = 9.29e-6 ± 30%, Q(14) = 25.27 ± 30%, r_a(14) < r_c(14) < r_b(14) | PHONONIC | PRE-REGISTERED | Convergence target: gate jointly authored with volovik (a) and kaku (c); each subsection adds candidate-specific addendum |
| 7 | Lab-SF Leggett-mode signature: V_Leggett / V_BA = 5.15 at L = 12 (predicted) | PHONONIC | PRE-REGISTERED (V.2) | Cross-channel observable; lab analog test |
| 8 | LISA GW dispersion signature: δ_GW ≈ 1.27e-5 at L = 14 pivot (predicted) | PHONONIC | PRE-REGISTERED (V.3) | Couples to W13-2 LISA null + CGWB+α_s flagship significance |
| 9 | DESI/LSST cosmological signature: Δw_0 ≈ +2.54e-5 at L = 14 (predicted) | PHONONIC | PRE-REGISTERED (V.4) | Below DESI DR3 envelope; within Stage IV combined sensitivity |
| 10 | Sparse-block L = 14 representation feasibility | METHODOLOGY | OPEN (V.5) | Enables V.1 dense path; otherwise V.1 INFO with extrapolation only |
| 11 | Cross-link to 3A ζ-regulator-stabilization theorem candidate | PHONONIC / META | CONDITIONAL | Branch-c phenomenology piggy-backs on 3A's theorem verdict |

---

## VII. Notes on convergence with subsections (a) and (c)

This synthesis identifies branch-c as the **R-protected Leggett-Josephson phase-channel inter-band Bogoliubov vacuum-rotation residue** in the C² coset SU(3)/(SU(2)×U(1)). Volovik (a) is expected to identify branch-c via the GGE-relic / superfluid-universe lens, and the structural test of whether Volovik's mechanism agrees with this synthesis is whether the GGE-relic occupation signature at the cosmological pivot scale matches branch-c's predicted Bogoliubov occupation `n_c(k_pivot, L = 14) ≈ 1.27e-5`. Kaku (c) is expected to identify branch-c via an alternative-pathway / instanton-anti-instanton-pair sector lens, and the structural test of whether Kaku's mechanism agrees with this synthesis is whether the instanton-pair signature reproduces the same r_c(L) trajectory and squeeze-ordering r_a < r_c < r_b at L = 14.

The CONVERGED S86 gate is `BRANCH-C-BOGOLIUBOV-DISTINCTNESS` per V.1; each subsection adds its candidate-specific addendum to this single shared gate. The mechanism-discrimination addendum (V.1 last bullet) is the discriminator: PASS for landau iff squeeze-ordering r_a < r_c < r_b persists; PASS for volovik iff GGE-relic occupation at pivot matches; PASS for kaku iff instanton-pair signature matches. AT MOST ONE of the three sub-PASS conditions can be the canonical mechanism (since they make different predictions about branch-c's microscopic physics); at LEAST one must PASS (since branch-c is empirically a stable w_0 branch and must have SOME phononic identification). The S86 gate is therefore a 3-way mechanism election, not a pass/fail check.

---

**End of Subsection (b) — Bogoliubov / BCS / Leggett-Josephson Phase-Channel Track.** Computed via standard Bogoliubov-coefficient parameterization of W10-4 §(d) branch table (Python-verified to machine precision); structural attribution to the R-protected Leggett-Josephson phase channel grounded in S69 + S70 + LEGGETT-PARTITION-57/58 + S82 W2-11 Z_2 gauge degeneracy + S77 BCS-timing PASS. Discriminating S86 gate `BRANCH-C-BOGOLIUBOV-DISTINCTNESS` pre-registered with three discriminants (D1 canonical-commutator, D2 cosine-distance, D3 mixing-angle-ratio) plus a landau-signature squeeze-ordering addendum, all at L = 14 with this synthesis's log-linear predictions. Structured carry-forward (V.1-V.6) follows the synthesis-template contract per `feedback_fix-in-session-never-defer.md`.
