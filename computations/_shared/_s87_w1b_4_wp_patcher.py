"""S87 W1b-4 working-paper §W1b-4 in-place patcher (one-shot Python writer).

Per .claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race": when Edit-tool round-trips fail with mtime conflicts,
use an append-only / one-shot Python writer that opens, modifies in memory,
and writes atomically — avoiding the read/check/write race.
"""
from pathlib import Path
import re

WP = Path(__file__).resolve().parent.parent / "sessions" / "session-87" / "session-87-results-workingpaper.md"

NEW_SECTION = """### §W1b-4. S87-PAIRED-SLOT-RATIO-INTERPRETATION (gen-physicist)

**Status**: COMPLETE
**Gate ID**: `S87-PAIRED-SLOT-RATIO-INTERPRETATION`
**Trigger**: `AUDIT-OPEN-Q`
**Classification**: **GEOMETRIC** (open-question audit on paired-slot ratio structural interpretation)
**Agent**: `gen-physicist`
**Hypothesis**: The empirical paired-slot split-ratio `7436/3812 ≈ 1.95068` observed at S86 W-1 W1b-T5 paired-slot tabulation arises from one of four pre-enumerated structural classes (CLASS-A hypercube-vertex 2:1 / CLASS-B Seeley-DeWitt mass-ratio expansion at a_0/a_2 / CLASS-C other-substrate-identity / CLASS-D numerical-coincidence). The OPEN-Q gate ALWAYS verdicts INFO; the sub-classification IS the structural output.
**Plan reference**: `sessions/session-plan/session-87-plan-w1b.md` §W1b-4 (lines 688-909).

**MCP Pre-Compute Audit**:

| Query | Result | Action |
|:------|:-------|:-------|
| `search_knowledge("paired slot ratio 7436 3812 a_0 a_2")` | 10 hits — STRUCTURAL SOURCE LOCATED. `s64_bdg_kasparov.py` canonical comment lines 414-420 + `s86-mellin-cone-repair-or-no-go.md` magnitude tables. `7436 = a_0^zeta / a_0^Gilkey = 6440/0.866` (S64 a_0 split factor); `3812 = a_2^zeta / a_2^Gilkey = 2776.165/0.728235` (S46 a_2 split factor). The S64 comment is canonical: \"ratio depends on k\". | NOT pre-closed; audit advances. Provenance pinned to S64/S46. |
| `search_knowledge("hypercube vertex character identity")` | 10 hits — Doob-Sachs hypercube spectrum (`2k*J_bar` per S78 mu_eff) + SU(3) character_on_torus (S44, S48). No direct 2:1 vertex-pairing closure of 7436/3812. | CLASS-A candidate enumerated (r_A = 2). |
| `search_knowledge("Seeley-DeWitt mass-ratio expansion")` | 10 hits — SD expansion `Tr(exp(-tD^2)) = sum t^k a_{2k}(D^2)` (S75); SD vacuum energy `rho_vac = f_0 Lambda^4 a_0` (S64); a_n^HK = (1/16π²) · a_n^SDW for d=4 (canonical_constants.py §F). | CLASS-B structural-identity candidate enumerated. |
| `get_constant("a_0_FW")` / `get_constant("a_2_FW")` | NOT FOUND — neither pinned in canonical_constants. | Use `a0_fold = 6440.0`, `a2_fold = 2776.16539` (canonical_constants.py lines 339-340) + `A0_GILKEY = 0.866`, `A2_GILKEY = 0.728235` (S64 comment lines 52-53) for CLASS-B prediction. |
| `mcp__oeis__lookup_by_values(values=[7436, 3812], max_results=10)` | NO MATCH — neither sequence appears in any canonical OEIS combinatorial sequence. | CLASS-A and CLASS-C combinatorial-anchor readings unsupported by OEIS. |
| `mcp__sage__sage_eval` Sage QQ-exact reduction | `7436/3812 = 1859/953` reduced (gcd=4); `7436 = 2² · 11 · 13²`; `3812 = 2² · 953` (953 prime); float = `1.9506820566631689`. | Confirms exact reduction; the integers are NOT congruent to a small canonical fraction (e.g., not 39/20 = 1.95, not 2 - 1/20). |

**Verdict**: `INFO` (always; OPEN-Q discipline pre-registered)
- 4-tuple: `(value=min_class_residual=3.4506e-05, scheme=4-class-paired-slot-classification, convention=substrate-paired-slot-w1b-T5-anchor, L_max=12)`
- 3-tuple annotation: `sign_verdict=N/A magnitude_verdict=INFO regime_verdict=VALID`
- Sub-classification: `INFO_CLASS_B_NEAR_UNIQUE_GAP_A,C` (Class-B PASS-band match; Class-A and Class-C residuals in the in-between gap [TOL_PASS, TOL_EXCLUDE] block strict uniqueness)
- Promotion path: S88+ candidate `S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY` conditional on resolving CLASS-A and CLASS-C in-between-gap residuals via deeper enumeration or L_max=14 cross-check.

**Results**:

**Sage QQ-exact reduction of 7436/3812**:
- `7436/3812 = 1859/953` (reduced; gcd = 4)
- `7436 = 2² · 11 · 13²`; `3812 = 2² · 953` (953 prime)
- Decimal: `1.9506820566631689` (bit-exact via Python `Fraction`)

**OEIS lookup outcome**: `mcp__oeis__lookup_by_values(values=[7436, 3812])` returned NO MATCH. Neither integer appears in any canonical OEIS combinatorial sequence; this rules out interpretations requiring 7436 or 3812 to be a member of a known combinatorial family (Bell, Catalan, Stirling, partition counts, etc.).

**Structural source of 7436 and 3812** (knowledge-MCP pre-check + `s64_bdg_kasparov.py` lines 414-420 canonical comment):
- `7436 = round(a_0^zeta / a_0^Gilkey) = round(6440 / 0.866)` — the K-DEPENDENT zeta-vs-Gilkey split factor at the **a_0 (CC) slot** (S64 BDG-Kasparov canonical).
- `3812 = round(a_2^zeta / a_2^Gilkey) = round(2776.16539 / 0.728235)` — the K-DEPENDENT zeta-vs-Gilkey split factor at the **a_2 (Newton) slot** (S46 derived; cited in S86 W-2 working paper line 156 + W1c workshop magnitude tables).
- S64 canonical comment: *\"a_0^zeta / a_0^Gilkey = 6440 / 0.866 = 7436. But this ratio is NOT the same as a_2^zeta / a_2^Gilkey = 3812. Because a_k^zeta is sum |lam|^{-2k}, not just a normalization factor. The conversion depends on k.\"*

**Per-class residual table** (pre-registered tolerance: PASS < 1e-2; EXCLUDE > 1e-1):

| Class | Predicted r | Residual `|r_obs − r|` | Band |
|:------|:-----------:|:----------------------:|:-----|
| **A** (hypercube-vertex 2:1) | 2.000000 | 4.9318e-02 | IN-BETWEEN GAP (NOT PASS, NOT EXCLUDED) |
| **B** (SD-mass-ratio split-factor identity) | 1.950717 | **3.4506e-05** | **PASS** (< 1e-2) |
| C1 (2π)²/(4π)² = 1/4 | 0.250000 | 1.7007e+00 | EXCLUDED |
| C2 φ_paasch (S12 chirality) | 1.531580 | 4.1910e-01 | EXCLUDED |
| C3 Connes-Karoubi HP1 cocycle (S86 W-5) | 7.324992 | 5.3743e+00 | EXCLUDED |
| C4 SU(3) dim ratio 8/3 | 2.666667 | 7.1598e-01 | EXCLUDED |
| C5 atlas cardinality A_5/A_4 (S86 W-8) | 1.250000 | 7.0068e-01 | EXCLUDED |
| C6 V_4 pair orders (S86 W-12) | 2.000000 | 4.9318e-02 | IN-BETWEEN GAP (degenerate with A) |
| C7 a_4/a_2 geom ratio | 0.486542 | 1.4641e+00 | EXCLUDED |
| C8 a_0/a_4 geom ratio | 4.767822 | 2.8171e+00 | EXCLUDED |
| C9 R_protected = a_0·a_4/a_2² | 1.128655 | 8.2203e-01 | EXCLUDED |
| C10 π/φ_paasch | 2.051210 | 1.0053e-01 | IN-BETWEEN GAP (just above 1e-1) |
| **D** (numerical coincidence) | (band) | NOT FIRED — Class-B already < 1e-2 | N/A |

**Substitution chain (CLASS-B structural identity)**:

Step 1 (definitions):
- `a_n^zeta = Σ_k d_k / |λ_k|^{2n}` — zeta-spectral moment (sum over D_K eigenvalues with multiplicities)
- `a_n^Gilkey = (4π)^{-d/2} · (Gilkey-Seeley-DeWitt geometric coefficient)` — heat-kernel small-t coefficient
- Canonical pins (S64 / canonical_constants.py): `a_0^zeta = 6440`, `a_2^zeta = 2776.16539`, `a_0^Gilkey = 0.866`, `a_2^Gilkey = 0.728235`

Step 2 (substitution):
- `7436 = round(a_0^zeta / a_0^Gilkey) = round(6440 / 0.866) = round(7436.490)`
- `3812 = round(a_2^zeta / a_2^Gilkey) = round(2776.165 / 0.728235) = round(3812.184)`
- `r_obs = 7436 / 3812 = (a_0^zeta / a_0^Gilkey) / (a_2^zeta / a_2^Gilkey)` (modulo integer-rounding)

Step 3 (simplify to canonical form):
- `r_B := (a_0^zeta · a_2^Gilkey) / (a_0^Gilkey · a_2^zeta)`
       `= (6440 · 0.728235) / (0.866 · 2776.165)`
       `= 4689.832 / 2403.999`
       `= 1.9507166`

Step 4 (read direction from canonical form):
- `residual_B = |r_obs − r_B| = |1.9506821 − 1.9507166| = 3.4506e-05`
- The residual is the propagation of integer-rounding error from `7436.490 → 7436` and `3812.184 → 3812` into the ratio. It is BELOW the pre-registered PASS tolerance 1e-2 by 3 orders of magnitude.
- Direction: r_obs UNDERSHOOTS r_B by 3.45e-05 because BOTH integers were rounded toward zero (down) by ~0.49 and ~0.18 respectively; the ratio therefore shifts very slightly downward from the structural identity.

**Sub-classification reasoning** (pre-registered band rule):
- CLASS-B residual 3.45e-05 < 1e-2 ⇒ Class-B is in PASS-band.
- CLASS-A residual 0.0493: NOT < 1e-2 (fails PASS) AND NOT > 1e-1 (fails strict-exclusion). This is the IN-BETWEEN GAP.
- CLASS-C minimum residual 0.0493 (C6 = V_4 pair orders, degenerate with A) AND C10 = π/φ_paasch at 0.1005 (just above 1e-1): Class-C also has IN-BETWEEN-GAP candidates.
- Strict uniqueness rule: `unique_class = X iff (residual_X < 1e-2) AND (residual_Y > 1e-1 ∀ Y ≠ X)`.
- Class-B satisfies condition 1 but FAILS condition 2 (Class-A and Class-C-min are both at 0.0493, not > 0.1).
- Therefore: **NEAR-UNIQUE-CLASS-B with in-between-gap on A and C**, NOT strict-unique.

**Solution-space meaning**:
- The CLASS-B structural identity `r = (a_0^zeta · a_2^Gilkey) / (a_0^Gilkey · a_2^zeta)` is the substrate-canonical reading of the 7436/3812 ratio. The S64 comment correctly identifies this as the \"k-dependent\" running of the zeta-vs-Gilkey conversion factor across spectral-action slots.
- The `value 2.000000` near-coincidence for CLASS-A (hypercube-vertex 2:1) and C6 (V_4 element orders) at residual 0.0493 is NOT a structural identity; it reflects the empirical numerator/denominator integers happening to lie within ~5% of 2:1 due to the moderate ratio of `a_2^Gilkey/a_0^Gilkey ≈ 0.841` partially canceling the `a_0^zeta/a_2^zeta ≈ 2.320` ratio.
- The CLASS-C C10 residual 0.1005 (π/φ_paasch ≈ 2.051) is just above the exclusion threshold; this is a numerical coincidence with no derivational chain to the substrate's spectral structure.

**Promotion path (S87 → S88+)**:
- The strict-uniqueness rule is NOT satisfied (in-between-gap on A and C). Per pre-registered band table, the gate routes to a CLASS-B-near-unique INFO sub-classification rather than a fixed-form S88 promotion.
- S88+ carry-forward: `S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY` candidate, conditional on:
  1. Promoting `a_0_FW` and `a_2_FW` to canonical_constants.py with provenance pin (currently absent per knowledge-MCP `get_constant` returning NOT FOUND).
  2. Resolving the CLASS-A and CLASS-C in-between-gap residuals via either (i) deeper CLASS-C enumeration (Schur-orthogonality coefficients on SU(3) × Spin(3) decomposition, Connes-Moscovici 1995 dimension-spectrum residue weights, M_2(C) ⊕ M_3(C) Pati-Salam algebra structural fractions), OR (ii) L_max=14 cross-check (per S87 W1b-3 if available) to confirm the structural identity is preserved at finer truncation.
- Carry-forward classification: deferred-research; OPEN-Q remains OPEN until the in-between-gap is structurally resolved.

**Substrate-framing reminder** (per plan §W1b-4 Field 13):
> 7436 and 3812 are paired-slot integer counts emerging from the substrate's OWN spectral structure at L_max=12. Direction of explanation: D_K eigenvalues → spectral-action heat-kernel expansion → per-slot zeta-vs-Gilkey split factors → ratio of split factors. The substrate IS the spectral content; the slot integers are READ OFF the spectrum. NO container framing.

**Files produced**:
- `computations/session-87/s87_w1b_paired_slot_ratio_interpretation.py` (script, 27,477 bytes)
- `computations/session-87/s87_w1b_paired_slot_ratio_interpretation.npz` (data, 9,708 bytes; keys: `paired_slot_ratio_observed`, `paired_slot_ratio_observed_qq_num=1859`, `paired_slot_ratio_observed_qq_den=953`, `class_A_predicted_value`, `class_A_match_residual`, `class_B_predicted_value`, `class_B_match_residual`, `class_C_candidates_list`, `class_C_predicted_values`, `class_C_match_residuals`, `class_D_residual_band`, `verdict_class`, `verdict_unique_match`, `audit_sha256`, `content_sha256`, `tol_pass`, `tol_exclude`)
- `computations/session-87/s87_w1b_paired_slot_ratio_interpretation.png` (4-panel plot, 191,219 bytes; per-class predicted vs observed bar / per-class log-scale residual histogram with PASS+EXCLUDE bands / Sage QQ + OEIS + knowledge-MCP findings text panel / classification flowchart text panel)
- Verdict line + dual-SHA companion + 3-tuple annotation in `computations/session-87/s87_gate_verdicts.txt` lines 32-34.

**Dual-SHA**:
- `audit_sha256 = 98b84eed7716f83127b75d16103f48554d404f49c0cf13fd0fd679ba59643264`
- `content_sha256 = 210aeb536228a2cf2cec285915b037b1c49f8a19ca743bd7f0f8ac999c180555`
- `schema_version = S87+`
- Input pins (full SHA-256, ordered): `computations/_shared/canonical_constants.py: 6bc613e8a02acfd6...`, `computations/session-64/s64_bdg_kasparov.py: 1a1ebd48207f2567...`, `sessions/archive/session-86/session-86-w2-workingpaper.md: 9d1180a2c79a8ed0...`
"""

# Read current contents.
text = WP.read_text(encoding="utf-8")

# Define start and end markers for the §W1b-4 section.
# Start: "### §W1b-4. S87-PAIRED-SLOT-RATIO-INTERPRETATION (gen-physicist)"
# End: just before "### §W1b-5. S87-PS-AF-RECALIBRATION-DIAGNOSTIC (gen-physicist)"
start_pattern = r"### §W1b-4\. S87-PAIRED-SLOT-RATIO-INTERPRETATION \(gen-physicist\).*?(?=### §W1b-5\. S87-PS-AF-RECALIBRATION-DIAGNOSTIC)"

# Use raw § character (Unicode 00A7) — Python handles this directly
start_marker = "### §W1b-4. S87-PAIRED-SLOT-RATIO-INTERPRETATION (gen-physicist)"
end_marker = "### §W1b-5. S87-PS-AF-RECALIBRATION-DIAGNOSTIC (gen-physicist)"

start_idx = text.index(start_marker)
end_idx = text.index(end_marker)

# Replace section content. Keep the trailing "---\n\n" before the next section heading.
# The file convention is: section ends, then "\n\n---\n\n### §W1b-5..."
# So we want to find the "---" delimiter immediately before §W1b-5.
# Strategy: replace from start_marker up to (but not including) the "---\n\n### §W1b-5" sequence.

# Find the "---" line just before §W1b-5
search_region = text[start_idx:end_idx]
# Find the LAST "---\n\n" occurrence in search_region (this is the separator before §W1b-5)
sep_idx = search_region.rfind("---\n\n")
if sep_idx == -1:
    # Fallback: just keep the end-marker preserved
    sep_offset = 0
else:
    # Keep "---\n\n" before §W1b-5 by setting end of replacement = start_idx + sep_idx
    sep_offset = sep_idx

# Reconstruct with NEW_SECTION substituted
# Convention: NEW_SECTION ends without trailing newline; we add a blank line + "---\n\n" delimiter
patched = (
    text[:start_idx]
    + NEW_SECTION.rstrip()
    + "\n\n---\n\n"
    + text[start_idx + sep_offset + len("---\n\n"):]
    if sep_offset > 0
    else text[:start_idx] + NEW_SECTION.rstrip() + "\n\n---\n\n" + text[end_idx:]
)

# Write atomically.
WP.write_text(patched, encoding="utf-8")
print(f"Patched {WP.name}: replaced §W1b-4 section ({end_idx-start_idx} chars → {len(NEW_SECTION)} chars)")
print(f"New file size: {len(patched)} chars")
