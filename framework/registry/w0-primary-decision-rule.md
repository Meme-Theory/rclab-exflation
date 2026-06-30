# w_0_FW PRIMARY Designation — Decision Rule

> **Origin**: Created S86 W13-3 by sagan-empiricist as adjudication output for
> `S86-W0-PRIMARY-VALUE-RESOLVE` (plan §W13-3). Self-blacklist: mack-cosmic-bridge
> cannot run this gate (own carry-forward source, mack 9A §VI.7).
>
> **Substrate framing**: w_0_FW IS the substrate's late-time spectral-action
> gradient projected onto observational coordinates. The two candidates are
> NOT competing models; they are TWO METHODOLOGICALLY-DISTINCT projections of
> the same substrate observable (Volovik-partition averaging vs substrate-
> compaction direct evaluation). PRIMARY designation is OBSERVATIONAL-CITATION
> discipline (which value downstream gates cite as canonical), not a physics
> ranking. The DR3 reversibility protocol is the substrate's external falsifier.

**Status**: LANDED via `S86-W0-PRIMARY-VALUE-RESOLVE` (W13-3, S86).
**Producing script**: `computations/s86_w13_p9_w0_primary_value_resolve.py`
**Verdict file**: `computations/s86_gate_verdicts.txt`
**Dual-SHA**: audit_sha256=8893fbc2ee44af27585268b01481eff5560817013ec3e60ae47ee0821ccaaf0a; content_sha256=51b5584d5d807bc3bdb1b73954f2dcf36768f50b094fc34e50b078f46ffa5f7e

---

## §1. Both candidates documented (provenance, method, value, audit_sha256)

### §1.1 Candidate A — w_0_A = -0.918 (Volovik partition)

| Field | Value |
|:---|:---|
| Value | -0.918 |
| Source | S5 row #1 (`session-85-s5-falsifier-inventory-mack.md` §III.1) |
| Method | Volovik-partition projection of spectral-action gradient at fold, integrated over post-fold expansion history |
| Origin gate | S58 Volovik effacement Γ=0.99970; canonical-constants pin `w0_FW = -0.918` |
| Cross-check verdict | `S85-S5-CONVERGENCE-AUDIT: PASS` (audit_sha256=6920eaefe192f72d399ba7185224b6a0cc1aa50ad2fabdca0310551a865a24d8) |
| W4-7 NULL-ELIM-MAP SHA | content_sha256 head `bf8135bf...` |
| Sigma-distance vs LCDM (S5 §III.1) | +3.28σ at DR3 fiducial σ(w_0)=0.025 |
| ZFP/TD tag | ZFP (S58 Volovik partition; no free parameters) |
| Registry sessions of citation | 28+ sessions (S58 → S85) |

### §1.2 Candidate B — w_0_B = -0.842454 (substrate-compaction, branch-(iv))

| Field | Value |
|:---|:---|
| Value | -0.842454 |
| Source | S85 W10-2 branch-(iv) (`session-85-w10-workingpaper.md` lines 287-289, 313, 337, 341, 386) |
| Method | substrate-compaction-derived w(z) via fiber-tau density tracking, evaluated at z=0 |
| Origin gate | S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT: PASS (audit_sha256=8de72cde7d635949f45716191288da6656f8a9fe05411532ab848fdb93fd04e8; content_sha256=b9a6a3014218386add94df8fef1034df5e17feb467c4d4b9cecacadfb133cd09) |
| R_842 offset from center (-0.842) | 0.000454 = 0.45% of mack-9A half-width |
| Sigma-distance vs LCDM | +6.30σ at DR3 fiducial σ(w_0)=0.025 |
| ZFP/TD tag | ZFP (substrate-compaction direct, no fitting) |
| Registry sessions of citation | 0-1 sessions (S85 W10-2 → S86 W13) |

---

## §2. 4-criterion adjudication table

| # | Criterion | A=-0.918 | B=-0.842454 | Verdict |
|:-:|:----------|:---------|:------------|:--------|
| 1 | theoretical-priority (more-fundamental substrate construction) | post-fold integral over expansion history | direct fiber-tau density at z=0 | **tie** (both first-principles) |
| 2 | DR3-rectangle-membership (mack-9A R_842 = [-0.942, -0.742]) | inside (offset 0.076, 76.0% of hw) | inside (offset 0.000454, 0.45% of hw) | **both inside** (neither excluded) |
| 3 | falsifiability (distance from LCDM, in σ-units of DR3 fiducial 0.025) | d=0.082, n_σ=3.28 | d=0.157546, n_σ=6.30 | **B more discriminable** by Δn_σ=+3.022 |
| 4 | registry-history (canonical-pin longevity) | 28+ sessions (S58 → S85) | 0-1 sessions (S85 → S86) | **A long-standing** |

**Score**: A wins Criterion 4; B wins Criterion 3; ties on Criteria 1 and 2.

**Substitution chain** (per plan §W13-3.10; [SIGN] trigger):

```
Step 1 — Definitions:
  w_0_A = -0.918                  (Volovik partition; canonical pin)
  w_0_B = -0.842454             (substrate-compaction; W10-2 branch-(iv))
  w_0_LCDM = -1.0                (LCDM cosmological constant)
  d(X) := |X - w_0_LCDM|        (Euclidean distance from LCDM in 1-D w-space)

Step 2 — Substitute (Python + Sage exact-rational verified):
  d(w_0_A) = |-0.918 - (-1.0)| = |0.08199999999999996| = 0.082000    (= 41/500 exact)
  d(w_0_B) = |-0.842454 - (-1.0)| = |0.15754599999999996| = 0.157546    (= 78773/500000 exact)

Step 3 — Simplify:
  Δd := d(w_0_B) - d(w_0_A) = 0.157546 - 0.082000 = +0.075546    (= 37773/500000 exact)

Step 4 — Direction:
  Δd > 0 → d(w_0_B) > d(w_0_A) → w_0_B is FURTHER from LCDM than w_0_A.

Falsifiability corollary (DR3 σ(w_0) = 0.025 fiducial, S69 master):
  n_σ(A) = d(A)/σ = 0.082000/0.025 = 3.280000    (= 82/25 exact)
  n_σ(B) = d(B)/σ = 0.157546/0.025 = 6.301840    (= 78773/12500 exact)
  Δn_σ = n_σ(B) - n_σ(A) = +3.021840    (= 37773/12500 exact)

  Direction: Δn_σ > 0 → DR3 will discriminate B from LCDM at +3.022σ MORE
  than it discriminates A from LCDM (under fiducial σ(w_0)=0.025).
```

**DR3 scenario tension table** (σ-distance of FW from each scenario):

| Scenario | DR3 returns w_0 | n_σ for A=-0.918 | n_σ for B=-0.842454 |
|:---|:---:|:---:|:---:|
| A_LCDM | -1.0000 | 3.2800 | 6.3018 |
| B_w095 | -0.9500 | 1.2800 | 4.3018 |
| C_w086 | -0.8600 | 2.3200 | 0.7018 |
| B_precise_w091 | -0.9100 | 0.3200 | 2.7018 |

---

## §3. Pre-registered decision rule

**Rule** (deterministic, no post-hoc tuning):

> PRIMARY = candidate that satisfies (registry-history-priority AND
> DR3-rectangle-membership) = CANDIDATE A unless and until a structural
> argument promotes B.

**Components of the rule**:

1. **Registry-history-priority** (Criterion 4): the candidate with longer canonical-pin
   citation history wins, because downstream gates have already been written
   citing that value as canonical. Re-pinning to a different value would invalidate
   28+ sessions of σ-distance, joint-BF, and EVOI computations.

2. **DR3-rectangle-membership**: the candidate must sit inside the registered DR3
   falsifier rectangle R_842 (mack-9A canonical, center -0.842, half-widths
   (0.100, 0.200)). Both A and B satisfy this; the criterion is non-discriminating
   here but is included for falsifiability hygiene.

3. **No invocation of post-hoc data-fitting**: the rule was authored at plan-freeze
   (S86 W13 plan §W13-3) BEFORE the script ran. The decision is mechanical.

**The rule does NOT use** (and explicitly rejects):
- Falsifiability (Criterion 3) as PRIMARY-selection rule. Reason: more-discriminable
  is a virtue but does not override 28+ sessions of registry citation. Falsifiability
  enters via the REVERSIBILITY trigger (§5), not the PRIMARY designation.
- Theoretical-priority (Criterion 1) as discriminator. Reason: tie.

---

## §4. PRIMARY designation

**PRIMARY = w_0_A = -0.918** (Volovik partition; canonical_constants.py `w0_FW`).

Per §3 decision rule: Candidate A wins on registry-history-priority (28+ sessions)
AND satisfies DR3-rectangle-membership (inside mack-9A R_842 at 76% of half-width).
Candidate B is preserved as the SECONDARY-with-reversibility candidate.

**Downstream-citation discipline** (effective S86 onward):
- Master inventory Row #1 (w_0): cite `w_0 = -0.918, +3.28σ vs LCDM under DR3`
  with footnote `[*]` pointing to this file.
- DR3 sub-tree (W13-4, S86-DR3-SUB-TREE-3-ROW-PIN): both regulator-conditional
  L_max = 8/10/12 cells use A as the framework w_0 prediction; the substrate-
  compaction branch (B) is recorded as a parallel-pathway annotation.
- Future BF, EVOI, and joint-detector computations: A is the canonical framework w_0.
- canonical_constants.py: `w0_FW = -0.918` UNCHANGED (no canonical-constant
  re-emission from this gate).

**SECONDARY-with-reversibility candidate**: w_0_B = -0.842454
- Documented as the substrate-compaction direct-evaluation pathway.
- Cross-referenced from this file (§1.2) and from the master inventory
  Row #1 footnote.
- Will be promoted to PRIMARY automatically if the §5 reversibility trigger fires.

---

## §5. Reversibility protocol (DR3-trigger conditions)

**Trigger**: DR3 (DESI Data Release 3, window opened 2026-04-23 per S84 W1b-9 DR3-RESPONSE-PROTOCOL).

**Reversal condition**: if DR3 returns measured w_0 inside the band:

```
    w_0^{DR3}  ∈  [-0.86, -0.83]
```

then the PRIMARY designation REVERSES from A → B automatically. The justification
is structural: a measured w_0 in [-0.86, -0.83] sits at most 0.018 from B (n_σ < 0.72
at fiducial σ_obs = 0.025) and at least 0.058 from A (n_σ > 2.32). At that point the
registry-history priority of A is overridden by direct empirical preference for B.

Substitution chain for the reversal threshold:

```
Step 1 — Definitions:
  w_R_lo = -0.86   (upper edge of reversal band, closer to LCDM)
  w_R_hi = -0.83   (lower edge of reversal band, further from LCDM)
  σ_DR3 = 0.025    (DR3 fiducial sigma)

Step 2 — Substitute (max-tension within reversal band):
  max |A - w_R| = max(|-0.918 - (-0.86)|, |-0.918 - (-0.83)|)
                = max(0.058, 0.088) = 0.088 → n_σ(A,worst) = 0.088/0.025 = 3.52
  min |A - w_R| = min(0.058, 0.088) = 0.058 → n_σ(A,best)  = 2.32
  max |B - w_R| = max(|-0.842454 - (-0.86)|, |-0.842454 - (-0.83)|)
                = max(0.017546, 0.012454) = 0.017546 → n_σ(B,worst) = 0.70
  min |B - w_R| = 0.012454 → n_σ(B,best) = 0.50

Step 3 — Simplify:
  Within [-0.86, -0.83], B is always at most 0.70σ from the measurement,
  while A is at least 2.32σ from the measurement. The empirical preference
  for B is decisive (Bayes factor B/A ≥ exp((2.32^2 - 0.70^2)/2) ≥ 11.1).

Step 4 — Direction:
  n_σ(A) > n_σ(B) by ≥ 1.62 in the reversal band → B is the empirically
  preferred candidate → PRIMARY = B by re-pin protocol.
```

**Anti-reversal condition** (DR3 does NOT trigger reversal):
- If DR3 returns w_0 closer to A's band (e.g., [-0.95, -0.88]) or closer to LCDM
  (e.g., [-1.05, -0.95]), PRIMARY remains A.
- If DR3 returns w_0 outside the entire R_842 rectangle [-0.942, -0.742], the
  framework branch fails the binary containment test (independent issue, handled
  by S84 W1b-9 LOCKOUT-C protocol, not by this PRIMARY designation).

**Locked machinery** (cannot be retroactively re-tuned):
- Reversal band edges: -0.86 / -0.83 (pre-registered in this file at S86 W13-3 freeze).
- σ_DR3 = 0.025 fiducial (S69 master synthesis).
- Registry-history-priority weight: dominant. Falsifiability secondary unless reversal triggers.

---

## §6. Cross-references

**Inbound references** (files that point AT this decision rule):
- `sessions/framework/registry/falsifier-master-inventory.md` Row #1 (w_0): footnote citing
  this file as the primary-pin authority. (To be updated by P11 PAIR-1 in §W13-1.)
- `computations/canonical_constants.py` `w0_FW = -0.918` entry: provenance comment
  cites this file for the PRIMARY-decision provenance.
- `sessions/framework/registry/dr3-3row-7cell-subtree.md` (P8/W13-4 NEW): cites A=-0.918 as the
  pinned framework w_0 across the 21-cell decision matrix.

**Outbound references** (files this decision rule cites as evidence):
- `computations/s85_gate_verdicts.txt`:
  - `S85-S5-CONVERGENCE-AUDIT: PASS` (audit_sha256=6920eaefe192f72d39...) — A's S5 anchor.
  - `S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT: PASS` (audit_sha256=8de72cde7d63594...) — B's W10-2 anchor.
- `sessions/archive/session-85/session-85-mack-synthesis-w6-13.md` §VI.7 — original carry-forward.
- `sessions/archive/session-85/session-85-w10-workingpaper.md` §10.2 lines 287-289, 313, 337,
  341, 386 — W10-2 branch-(iv) value -0.842454 with R_842 offset 0.000454.
- `sessions/archive/session-85/session-85-s5-falsifier-inventory-mack.md` §III.1 row #1 — A's master-inventory record.
- S84 W1b-9 DR3-RESPONSE-PROTOCOL (R_842 lockout, content_sha256 head 9cc7f47e) — reversibility-trigger provenance.

**Reverse-trigger linkage**: §5 reversal rule at -0.86 ≤ w_0^{DR3} ≤ -0.83 is the
automatic re-pin condition. If DR3 publication satisfies this band, a follow-up
session must:
1. Update `canonical_constants.py` w0_FW from -0.918 to -0.842454.
2. Re-emit affected verdict lines (P11 master inventory Row #1 σ-distance recomputation).
3. Re-cross-reference this file's PRIMARY tag from A → B.
4. Append a verdict line `S{N}-W0-PRIMARY-REVERSED: PASS` with new dual-SHA.

---

**End of decision rule. Reversibility hot-trigger: DR3 publication, target window 2026-Q3 / 2027-Q1.**
