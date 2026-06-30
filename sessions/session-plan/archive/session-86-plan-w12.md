# Session 86 Plan — Wave W12: Detector + Fisher inventory

**Wave owner**: `mack-cosmic-bridge`
**Output file**: `sessions/session-plan/session-86-plan-w12.md` (this document)
**Item count**: 5 (C30, C31, C32, C33, C36)
**Theme**: Detector readiness 9-cell + BK-Array 2026 classifier pre-build + Fisher PDF SHA-pin closure + DR3 3-layer L_max sub-tree + CMB-HD α_s forecast quarterly poll
**Source**: mack-cosmic-bridge S-7 §V.3, §V.4, §V.5, §V.6, §V.9 (per partition manifest §1 Wave W12)

---

## §0. Wave W12 Summary

Wave W12 inventories the detector + Fisher infrastructure that the framework's
S86+ predictions depend on. None of the five items computes a new physical
prediction; instead each one PINS the observability landscape against which
prior verdicts (W4-3, W4-6, W1a-5, W1b-6) are interpreted, and pre-builds the
machinery that a 2026-2030 publication-event window will trigger.

The wave splits naturally into:

1. **Detector inventory** (C30) — single 9-detector × 5-field readiness matrix
   that is the backbone all later W12 + W13 + W14 inventory edits cite.
2. **BK-Array 2026 response** (C31) — pre-built decision script that fires the
   moment BK-Array publishes its primordial-tensor result. The 4-branch
   classifier is the framework's pre-registered response to r ∈ R_BK.
3. **Fisher PDF closure** (C32) — 5 forecast PDFs SHA-pinned so that W4-3 +
   W4-6 verdicts reference auditable σ-ledger entries rather than agent-memory
   recall of forecast numbers.
4. **DR3 3-layer L_max sub-tree** (C33) — promotes W1a-5 single 7-cell DR3
   tree to a 21-cell L_max ∈ {8, 10, 12} matrix, gating PASS on full
   determinism + monotonicity (no oscillation).
5. **CMB-HD α_s forecast monitor** (C36) — quarterly poll discipline; on
   publication, SHA-pin + re-fire S85 W1b-6.

All five items are bookkeeping/infrastructure; no GPU-heavy linear algebra.
Output is registry files under `sessions/framework/`, scripts under
`computations/`, and verdict-line appends per `.claude/rules/gate-verdicts.md`.

**Combined effort estimate**: ≈16-18 h.

---

## §0.5. Wave W12 Decision-Point Prerequisites

W12 has NO direct hard plan-write prerequisites — it is a Batch-3 wave whose
items are independent of other-wave physics outputs. The cross-references it
relies on are all S85-resident:

| Item | External reference | Source path |
|:-----|:-------------------|:------------|
| C30 | 9-detector master roster (PIXIE, DESI DR3, CMB-S4, LISA, LiteBIRD, BK-Array, CMB-HD, SKA-1, lab-analogs) | `sessions/framework/registry/baseline-findings-s66.md` + S85 W1b-1 DR3 sub-tree |
| C31 | BK-Array 2026 r-range Path-H/Path-C predictions (r=0.00745 / 0.0117) | `sessions/framework/registry/falsifier-master-inventory.md` + S85 W1b-6 |
| C32 | W4-3 + W4-6 verdict lines requiring Fisher-PDF backing | `computations/s85_gate_verdicts.txt` (W4-3, W4-6) |
| C33 | S85 W1a-5 7-cell DR3 tree (L_max=10 layer only) | `sessions/archive/session-85/working-paper-w1a.md` §W1a-5 |
| C36 | S85 W1b-6 α_s pin (canonical_constants.py `alpha_s_canon_2020`) | `computations/canonical_constants.py` + S85 W1b-6 verdict |

Wave plan-write may proceed in parallel with all other Batch-3 waves (W11,
W13, W14, W15). Compute-time sequencing within W12: C30 → C32 → C33 → C31 →
C36 (C30's 9-cell matrix is the input to C32's verdict re-emission and C33's
DR3 sub-tree row labels; C31 + C36 depend only on C30 detector roster).

---

## §I. Carry-Forward Items Mapping

Per partition manifest §1 Wave W12, the 5 items map to S-7 §V sub-sections:

| §I row | Gate ID | Source (mack S-7) | Effort | Item class |
|:-------|:--------|:------------------|:-------|:-----------|
| 1 | `S86-DETECTOR-READINESS-9-CELL` (C30) | §V.3 | 4 h | META-INFRASTRUCTURE |
| 2 | `S86-BK-ARRAY-CLASSIFIER-PRE-BUILD` (C31) | §V.4 | 4 h | META-INFRASTRUCTURE |
| 3 | `S86-FISHER-PDF-PIN-CLOSURE` (C32) | §V.5 | 2 h | META-INFRASTRUCTURE |
| 4 | `S86-DR3-3-LAYER-SUB-TREE` (C33) | §V.6 | 6 h | PHONONIC (substrate-prediction stability across regulator-layer) |
| 5 | `S86-CMB-HD-ALPHA-S-FORECAST-PIN` (C36) | §V.9 | 0.5 h/poll | META-INFRASTRUCTURE |

---

## §W12-1. S86-DETECTOR-READINESS-9-CELL (C30)

### 1. Gate ID
`S86-DETECTOR-READINESS-9-CELL`

### 2. Trigger
**[AUDIT]** — registry-write audit. The gate produces a 9-detector × 5-field
readiness matrix from canonical sources; the audit confirms each cell is
populated from a citable anchor (no narrative-only rows).

### 3. Classification
**META** (detector-infrastructure registry; not a physical prediction).

### 4. Agent type (runtime)
`mack-cosmic-bridge` (preferred — owns the observational landscape and
detector-priority discipline per `feedback_mack-bridge-role.md`).

Alternate: `sagan-empiricist` if mack is over-allocated (sagan owns the
empiricist anchoring of literature-citable σ-targets). NOT `gen-physicist`.

### 5. Hypothesis
The 9 detectors that drive S86+ framework discriminability are simultaneously
representable as a single status × launch-window × σ-target × framework-prediction
× EVOI-tag matrix — i.e. each detector has at least one framework prediction
above its σ-target within its launch-or-data-window.

### 6. Method (complete dispatch prompt)

```
You are mack-cosmic-bridge executing C30 / S86-DETECTOR-READINESS-9-CELL.

OBJECTIVE: Produce the 9-detector × 5-field readiness matrix at
sessions/framework/registry/detector-readiness-9-cell.md.

ENVIRONMENT:
  - Python: phonon-exflation-sim/.venv312/Scripts/python.exe
  - This task is BOOKKEEPING — no heavy linear algebra, no GPU.
  - from canonical_constants import * — pull σ-target reference values where
    they exist (e.g. r-target via tensor-to-scalar pin entries) rather than
    re-stating from training knowledge.

STEPS:
  1. Construct the 9-row × 5-column matrix:
     ROWS (detector roster, ORDERED):
       (a) PIXIE                     [μ-distortion satellite, ~2030s decadal]
       (b) DESI DR3                  [BAO/RSD release, 2026-04+]
       (c) CMB-S4                    [ground-based CMB, ~2030+]
       (d) LISA                      [space GW interferometer, 2035+]
       (e) LiteBIRD                  [primordial-tensor satellite, 2030+]
       (f) BK-Array                  [BICEP/Keck Array, 2026 publication]
       (g) CMB-HD                    [proposed high-resolution CMB, 2030s]
       (h) SKA-1                     [21cm array Phase 1, 2028+]
       (i) lab-analogs ³He-B + K-STAR [terrestrial substrate analogs, ongoing]

     COLUMNS (5 fields per row):
       (1) status            : ACTIVE / FUNDED-PRE-BUILD / PROPOSED / OPERATIONAL
       (2) launch-or-data-window : year-range string (e.g. "2026-04 (DR3)")
       (3) σ-target          : leading observable + 1σ sensitivity (e.g.
                               "σ(r) = 1e-3 LiteBIRD"; "σ(μ) = 1e-8 PIXIE")
       (4) framework prediction : one citable framework value (e.g.
                               r=0.00745 Path-H from S85 W1b-6; ρ_AC=2.10
                               from S84 W6-50; α_s=+0.0023 from S85 W1b-8)
       (5) EVOI tag          : DECISIVE / DISCRIMINATING / CONFIRMATORY /
                               LAB-FALSIFIER

  2. For EACH cell, cite a source (session/gate/file). NO narrative-only entries.
     If a σ-target is not in canonical_constants.py, cite the literature anchor
     (Hazumi 2022 LiteBIRD; Sehgal 2019 CMB-HD; Ali+ 2018 HERA Memo 54; etc.).
     Mark any cell whose framework prediction is absent or under-determined as
     "TBD-S87" — this is permissible content, not a failure.

  3. Cross-check the matrix against the existing detector mentions in:
       - sessions/framework/registry/falsifier-master-inventory.md
       - sessions/framework/registry/baseline-findings-s66.md
     Flag any inconsistency (e.g. r-target stated as 1e-3 in one file and
     5e-4 in another) inline in the matrix.

  4. Append a substitution-chain (Definition / Substitute / Simplify /
     Direction) at the bottom verifying:
       "9 detectors × 5 fields = 45 cells; each cell either populated with
        cited value or marked TBD-S87."

OUTPUT TARGETS (must all exist on disk before reporting completion):
  - sessions/framework/registry/detector-readiness-9-cell.md (the matrix)
  - computations/s86_gate_verdicts.txt (one verdict line, see §9)

VERDICT:
  PASS iff 45/45 cells populated or explicitly TBD-S87 with citation;
  FAIL if any cell silently missing.

GPU: NONE NEEDED (pure registry construction).
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin |
|:---------------|:----|
| Detector roster (rows)             | 9 detectors enumerated above (closed list — no additions/removals at runtime) |
| Field schema (cols)                | 5 fields enumerated above (status / window / σ-target / prediction / EVOI tag) |
| σ-target source for each detector  | canonical_constants.py if present; else literature citation by author + year |
| Framework prediction citation rule | session ID + gate ID + verdict-file SHA |
| EVOI tag taxonomy                  | {DECISIVE, DISCRIMINATING, CONFIRMATORY, LAB-FALSIFIER} closed set |
| TBD-S87 admissibility              | allowed for cells where no S86-resident framework value exists; counts as "populated" for PASS |

### 8. Expected output 4-tuple
`(value=45_cells_filled, scheme=cited-anchors, convention=detector-readiness-9-cell-md, L_max=NA)`

### 9. PASS/FAIL/INFO thresholds

- **PASS** iff 45/45 cells populated (cited or TBD-S87 with citation), AND
  registry file exists at `sessions/framework/registry/detector-readiness-9-cell.md`.
- **FAIL** if any cell silently missing OR any cell populated by narrative-only
  text without a citation.
- **No INFO band** for this gate (binary registry-completeness).

Tolerance: ABSOLUTE — count of populated cells must equal 45 exactly.

Verdict line:
```
S86-DETECTOR-READINESS-9-CELL: PASS|FAIL -- value=<n_filled> scheme=cited-anchors convention=detector-readiness-9-cell-md L_max=NA sha256=<closure>
```

### 10. Substitution chain
NOT REQUIRED for this gate (pure registry-completeness audit; no
sign/direction/threshold claim involved). The 9×5=45 enumeration in §6 step 4
is bookkeeping arithmetic, not a physics direction claim.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** anchors the entire S86+ observational landscape in a single
  citable matrix. All later gates (C32 Fisher PDFs, C33 DR3 sub-tree, C36
  CMB-HD poll, W13 P11 master inventory, W14 watchlist edits) reference rows
  of this matrix instead of recreating per-detector status from agent memory.
  This is a pre-condition for `feedback_agents-not-authoritative.md`-compliant
  cross-session traceability.
- **FAIL** means a detector is undocumented and downstream gates citing it
  are operating on agent-memory recall rather than registry-pinned anchors —
  the same failure pattern flagged in S78 PRU Class-8 missing-pinnable-machinery.
  Re-dispatch with full citation requirement.

### 12. Effort estimate
**~4 h** (mechanical registry construction; bulk of effort is locating each
σ-target citation and disambiguating inconsistent entries across baseline-findings
and falsifier-master-inventory).

### 13. Substrate-framing reminder
Detectors are passive observers of substrate excitations on the emergent g_M.
They are not "looking at the substrate" — they are catching c_Gold-bounded
relay patterns that propagate from substrate-internal events (BK-Array sees
folded-shape primordial-tensor relay; LISA sees CGWB ρ_AC relay; lab-analogs
see ³He-B / K-STAR projections of the substrate's own internal Bogoliubov
modes). The 9-cell matrix should NOT describe what each detector "looks at"
in container-language; describe what substrate excitation each detector's
σ-target gates against framework prediction.

---

## §W12-2. S86-BK-ARRAY-CLASSIFIER-PRE-BUILD (C31)

### 1. Gate ID
`S86-BK-ARRAY-CLASSIFIER-PRE-BUILD`

### 2. Trigger
**[VERIFY]** — synthetic-test verification. The gate is the script
`computations/s86_bk_array_2026_classifier.py` plus its self-test on
4 synthetic inputs r ∈ {0.003, 0.012, 0.025, 0.040} → expected branches
{1, 2, 3, 4}.

### 3. Classification
**META** (pre-built decision-tree script for a 2026 publication event;
infrastructure rather than substrate physics).

### 4. Agent type (runtime)
`mack-cosmic-bridge` (preferred — owns the framework's observational-response
discipline and the BK-Array Path-H/Path-C r-pin from S85 W1b-6).

Alternate: `cosmic-web-theorist` if mack is over-allocated. NOT `gen-physicist`.

### 5. Hypothesis
The framework's response to BK-Array's 2026 publication of r is fully
specified by a 4-branch decision tree on the observed r value, with
boundaries (0.005, 0.015, 0.030) chosen so that synthetic inputs in each
sub-interval map deterministically to a single branch.

### 6. Method (complete dispatch prompt)

```
You are mack-cosmic-bridge executing C31 / S86-BK-ARRAY-CLASSIFIER-PRE-BUILD.

OBJECTIVE: Pre-build the BK-Array 2026 4-branch classifier at
computations/s86_bk_array_2026_classifier.py and verify the synthetic
self-test r ∈ {0.003, 0.012, 0.025, 0.040} → branches {1, 2, 3, 4}.

ENVIRONMENT:
  - Python: phonon-exflation-sim/.venv312/Scripts/python.exe
  - from canonical_constants import * — for any pinned r values referenced
    in branch text (e.g. Path-H r=0.00745, Path-C r=0.0117 if those are in
    canonical_constants.py; if not, cite S85 W1b-6 verdict).
  - No GPU; pure decision-tree logic.
  - Boundary values 0.005, 0.015, 0.030 are gate parameters pinned in §7
    machinery PRDR.

SCRIPT SPEC (s86_bk_array_2026_classifier.py):

  def classify_bk_array_r(r_observed):
      \"\"\"
      4-branch BK-Array 2026 response classifier.

      Boundaries:
        b1_b2 = 0.005  (Path-detection-strong-low / Path-H boundary)
        b2_b3 = 0.015  (Path-H / Path-C boundary)
        b3_b4 = 0.030  (Path-C / framework-falsified boundary)

      Branches:
        1 if r_observed <= 0.005           # detect-strong-low (below both
                                           # Path-H 0.00745 and Path-C 0.0117)
        2 if 0.005 < r_observed <= 0.015   # Path-H confirmed (centered on
                                           # Path-H 0.00745)
        3 if 0.015 < r_observed <= 0.030   # Path-C confirmed (centered on
                                           # Path-C 0.0117 + tail to 0.030)
        4 if r_observed > 0.030            # framework-falsified
      \"\"\"
      ...

  def self_test():
      \"\"\"
      Synthetic-test inputs and expected branches.
      \"\"\"
      cases = [(0.003, 1), (0.012, 2), (0.025, 3), (0.040, 4)]
      for r, expected_branch in cases:
          got = classify_bk_array_r(r)
          assert got == expected_branch, f"r={r}: expected {expected_branch}, got {got}"
      return "PASS"

REQUIREMENTS:
  - All 3 boundary values (0.005, 0.015, 0.030) declared as module-level
    constants AT TOP of script with comment explaining their derivation
    relative to Path-H r=0.00745 and Path-C r=0.0117 from S85 W1b-6.
  - Each boundary tagged with `# (local)` per math-scripts.md §Local Variable
    Tagging — these are gate-design parameters, NOT canonical framework
    constants (Path-H and Path-C r values ARE canonical; the BOUNDARIES
    around them are gate-design choices pinned in §7).
  - Self-test must run as `python s86_bk_array_2026_classifier.py --self-test`
    and exit 0 on all 4 PASS cases.
  - Script must NOT consume real BK-Array data at S86 time — it is dormant,
    awaiting 2026 publication.
  - Append SHA-256 closure of the script to verdict line via `closure_hash`.

OUTPUT TARGETS:
  - computations/s86_bk_array_2026_classifier.py (the script)
  - computations/s86_gate_verdicts.txt (verdict line)

VERDICT:
  PASS iff all 4 synthetic test cases produce expected branches {1,2,3,4};
  FAIL if any mismatch.

GPU: NONE.
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin |
|:---------------|:----|
| Boundary `b1_b2` (branch 1/2 split)         | 0.005 |
| Boundary `b2_b3` (branch 2/3 split)         | 0.015 |
| Boundary `b3_b4` (branch 3/4 split)         | 0.030 |
| Path-H r reference value                     | 0.00745 (S85 W1b-6) |
| Path-C r reference value                     | 0.0117 (S85 W1b-6) |
| Synthetic test inputs (closed set)           | {0.003, 0.012, 0.025, 0.040} |
| Expected branch outputs (closed set)         | {1, 2, 3, 4} (one-to-one with inputs) |
| Comparison operator at each boundary         | left-open / right-closed (`b < r ≤ b'`) — pinned for determinism |

### 8. Expected output 4-tuple
`(value=4_branches_pass, scheme=classifier-pre-build, convention=left-open-right-closed, L_max=NA)`

### 9. PASS/FAIL/INFO thresholds

- **PASS** iff `self_test()` returns "PASS" — all 4 synthetic inputs produce
  the pinned branches exactly. ABSOLUTE tolerance (no numerical tolerance
  band; branch labels are integers).
- **FAIL** if any case mismatches.
- **No INFO band** (binary classifier verification).

Verdict line:
```
S86-BK-ARRAY-CLASSIFIER-PRE-BUILD: PASS|FAIL -- value=<n_pass>/4 scheme=classifier-pre-build convention=left-open-right-closed L_max=NA sha256=<closure>
```

### 10. Substitution chain (REQUIRED — branch-boundary direction)

```
Definition 1: r_obs       = observed primordial tensor-to-scalar ratio (BK-Array 2026)
Definition 2: r_PathH     = 0.00745  (framework Path-H prediction, S85 W1b-6)
Definition 3: r_PathC     = 0.0117   (framework Path-C prediction, S85 W1b-6)
Definition 4: b1_b2       = 0.005    (boundary below Path-H)
Definition 5: b2_b3       = 0.015    (boundary above Path-H, below Path-C tail)
Definition 6: b3_b4       = 0.030    (boundary above Path-C tail)

Substitute into the comparison r_obs vs each boundary:
  Step 1: For r_obs = 0.003:
            r_obs < b1_b2 (0.003 < 0.005), so branch = 1.
            Direction: r_obs strictly LESS THAN b1_b2.
  Step 2: For r_obs = 0.012:
            b1_b2 < r_obs ≤ b2_b3 (0.005 < 0.012 ≤ 0.015), so branch = 2.
            Direction: r_obs strictly GREATER than b1_b2 AND ≤ b2_b3.
            Cross-check: |r_obs - r_PathH| = |0.012 - 0.00745| = 0.00455
            (within Path-H ±60% interval — Path-H confirmed).
  Step 3: For r_obs = 0.025:
            b2_b3 < r_obs ≤ b3_b4 (0.015 < 0.025 ≤ 0.030), so branch = 3.
            Direction: r_obs strictly GREATER than b2_b3 AND ≤ b3_b4.
            Cross-check: |r_obs - r_PathC| = |0.025 - 0.0117| = 0.0133
            (within extended Path-C tail to 0.030).
  Step 4: For r_obs = 0.040:
            r_obs > b3_b4 (0.040 > 0.030), so branch = 4.
            Direction: r_obs strictly GREATER than b3_b4.
            Conclusion: framework-falsified region.

Simplify to canonical form:
  branch(r) = 1 if r ≤ 0.005
              2 if 0.005 < r ≤ 0.015
              3 if 0.015 < r ≤ 0.030
              4 if r > 0.030

Direction (read from canonical form): the branch index is monotone non-decreasing in r;
each boundary partitions r into a unique branch with left-open / right-closed
intervals. The 4 synthetic inputs are positioned one per interval, so the
expected outputs {1, 2, 3, 4} follow deterministically.

Conclusion: the classifier is well-posed and the synthetic test exercises
exactly one input per branch.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** commits the framework's BK-Array 2026 response procedure now,
  before publication. When BK-Array data lands, the response is mechanical:
  feed `r_observed` into the script, read off the branch, fire the
  pre-registered downstream gate (branch 4 → P_falsified update; branch 3 →
  Path-C confirmation entry to falsifier-master-inventory; branch 2 →
  Path-H confirmation; branch 1 → low-r anomaly investigation). This forecloses
  iterate-until-PASS on the post-publication response — the response is fixed
  before the data arrives.
- **FAIL** at any synthetic input is a script-logic bug; fix the boundary
  comparison operator or the branch assignment and re-run. NOT permitted to
  shift boundaries to make the test pass — the boundaries are pinned in §7.

### 12. Effort estimate
**~4 h** (script writing + self-test + boundary-derivation comment block + verdict-line append + dual-SHA closure).

### 13. Substrate-framing reminder
The BK-Array measures r — a relay-mode ratio between transverse (tensor) and
longitudinal (scalar) substrate excitations at the CMB scale. Branches 1-4
represent a discretization of the r-space into "below detection floor",
"Path-H regime (acoustic-route folded-shape relay)", "Path-C regime (cusp-
route relay with extended tail)", and "framework-excluded" — each is a
substrate-state classification, not a container-physics measurement bin.

---

## §W12-3. S86-FISHER-PDF-PIN-CLOSURE (C32)

### 1. Gate ID
`S86-FISHER-PDF-PIN-CLOSURE`

### 2. Trigger
**[AUDIT]** — SHA-pin closure audit on 5 PDFs + verdict re-emission.

### 3. Classification
**META** (Fisher-forecast literature anchoring).

### 4. Agent type (runtime)
`mack-cosmic-bridge` (preferred — owns observational/Fisher-forecast literacy).

Alternate: `little-red-dots-jwst-analyst` (literature-PDF anchoring discipline,
PDF-handling experience). NOT `gen-physicist`.

### 5. Hypothesis
The 5 Fisher-forecast PDFs cited by W4-3 + W4-6 verdicts are stable
literature artifacts (fixed publication versions) whose SHA-256 hashes can be
pinned in a registry, allowing W4-3 + W4-6 verdicts to be re-emitted with
auditable Fisher-PDF backing rather than agent-memory recall.

### 6. Method (complete dispatch prompt)

```
You are mack-cosmic-bridge executing C32 / S86-FISHER-PDF-PIN-CLOSURE.

OBJECTIVE:
  (a) Fetch + SHA-pin 5 Fisher-forecast PDFs.
  (b) Append registry rows at sessions/framework/registry/fisher-pdf-registry.md.
  (c) Re-emit S85 W4-3 + W4-6 verdicts under the Fisher-PDF map.

ENVIRONMENT:
  - Python: phonon-exflation-sim/.venv312/Scripts/python.exe
  - WebFetch (if available) or paper-search MCP (mcp__paper-search__download_arxiv,
    mcp__paper-search__search_google_scholar) for PDF retrieval.
  - For PDFs >10 pages, use the `pdf` skill (read-only verification of
    correct fetch — do not re-process content; SHA only).

THE 5 PDFs (closed list):
  (1) CMB-S4 Science Book v2 — Abazajian et al. 2022, "CMB-S4 Science Case,
      Reference Design, and Project Plan", arXiv:2203.08024
  (2) DESI 2025 BAO forecast — DESI Collaboration 2025 BAO survey forecast
      paper (latest official forecast accompanying Y3 release)
  (3) LiteBIRD Hazumi 2022 — Hazumi et al. 2022 "LiteBIRD satellite mission
      for primordial gravitational wave search", PTEP / SPIE
  (4) CMB-HD Sehgal 2019 — Sehgal et al. 2019 "CMB-HD: An Ultra-Deep,
      High-Resolution Millimeter-Wave Survey", arXiv:1906.10134
  (5) HERA Memo 54 — Ali et al. 2018, HERA collaboration internal memo
      on 21cm Fisher forecast (cite local copy SHA if memo is paywalled)

STEPS:
  1. For each PDF in the list:
     (a) Fetch via WebFetch / paper-search MCP. Save to a staging path
         under computations/_fisher_pdf_cache/ (do NOT commit PDFs
         to git; the SHA-pin registry is the persistent record).
     (b) Compute SHA-256 of the binary PDF.
     (c) Record the (URL, fetch date, SHA-256, citation) tuple.

  2. Append rows to sessions/framework/registry/fisher-pdf-registry.md:
     | # | Citation | URL | SHA-256 | Fetched | Used by gates |
     |:--|:---------|:----|:--------|:--------|:--------------|
     | 1 | Abazajian+ 2022 CMB-S4 SB v2 | arXiv:2203.08024 | <sha> | 2026-04-25 | W4-3, W4-6 |
     | ... |

     If the registry file does not exist, create it with a header section
     pointing to .claude/templates/synthesis.md or the existing
     sessions/framework/registry/falsifier-master-inventory.md style.

  3. Re-emit S85 W4-3 + W4-6 verdicts:
     (a) Read the original W4-3 + W4-6 verdict lines from
         computations/s85_gate_verdicts.txt.
     (b) Cite the original closure SHAs in a comment row above the new
         re-emission lines.
     (c) Append new verdict lines to s86_gate_verdicts.txt with the SAME
         pre-registered VALUE / SCHEME / CONVENTION / L_max — only the
         input-pin map changes (now references Fisher-PDF SHAs from §6 step 2
         registry rather than agent-memory σ recall).
     (d) Each re-emission line gets a comment row with audit_sha256 per the
         S81+ dual-SHA template (.claude/rules/gate-verdicts.md + W9a-99 split).

  4. Substitution-chain at bottom of registry file confirming:
       "5 PDFs SHA-pinned; W4-3 + W4-6 re-emitted with Fisher-PDF map; original
        verdicts preserved unchanged in s85_gate_verdicts.txt."

OUTPUT TARGETS:
  - sessions/framework/registry/fisher-pdf-registry.md (5 rows + header)
  - computations/s86_gate_verdicts.txt (3 verdict lines: this gate +
    W4-3 re-emission + W4-6 re-emission)

VERDICT:
  PASS iff (5/5 PDFs SHA-pinned) AND (W4-3 + W4-6 re-emitted with new
    audit_sha256 dual-SHA companion rows);
  FAIL if any PDF unfetchable (mark TBD-S87 only as fallback) OR re-emission
    skipped.

GPU: NONE.
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin |
|:---------------|:----|
| PDF list (closed)              | 5 enumerated above |
| Registry file path             | `sessions/framework/registry/fisher-pdf-registry.md` |
| Hash algorithm                 | SHA-256 (full 64-char hex) |
| Re-emission target gates       | W4-3, W4-6 (S85 verdict file) |
| Re-emission verdict-file path  | `computations/s86_gate_verdicts.txt` |
| Original-verdict citation rule | comment row with original closure SHA above each re-emission line |
| Fallback for unfetchable PDF   | mark "TBD-S87 — paywalled/withdrawn" with citation; counts as PASS-with-defect for that row |
| Companion-row template         | `.claude/rules/gate-verdicts.md` S81+ dual-SHA + W9a-99 split |

### 8. Expected output 4-tuple
`(value=5_pinned_2_reemitted, scheme=fisher-pdf-sha-pin, convention=sha256-full-64char, L_max=NA)`

### 9. PASS/FAIL/INFO thresholds

- **PASS** iff (5 PDFs SHA-pinned with citation rows) AND (W4-3 + W4-6
  re-emitted with new audit_sha256 dual-SHA companion rows).
- **FAIL** if any registry row missing OR either re-emission skipped.
- **INFO** band: if 1-2 PDFs unfetchable (paywalled / withdrawn), mark those
  rows TBD-S87 with citation and emit INFO for the gate. ≥3 unfetchable PDFs
  is FAIL.

Tolerance: ABSOLUTE (registry-completeness + re-emission verdict-file presence).

Verdict line:
```
S86-FISHER-PDF-PIN-CLOSURE: PASS|FAIL|INFO -- value=<n_pinned>/5+<n_reemit>/2 scheme=fisher-pdf-sha-pin convention=sha256-full-64char L_max=NA sha256=<closure>
```

### 10. Substitution chain
NOT REQUIRED for this gate (registry-write + verdict-re-emission audit; no
sign/direction/threshold claim). The PASS/INFO/FAIL boundary is a count
threshold (5 vs ≤4 vs ≤2 PDFs pinned), explicitly enumerated in §9.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** anchors the σ-targets used in S85 W4-3 + W4-6 (LiteBIRD n_T
  observability boundary; CMB-S4 / LiteBIRD joint marginalization) in
  literature-citable Fisher-PDF artifacts. Future-session gates citing those
  σ values can audit-trace through the registry rather than relying on
  agent-memory recall — directly addresses the failure pattern in
  `feedback_agents-not-authoritative.md`.
- **FAIL** means W4-3 / W4-6 σ values are agent-memory-only; downstream
  gates (W4-37 LB-CMBS4 joint, W4-41 LiteBIRD n_T boundary) are operating
  on un-audited σ-targets. Re-dispatch with explicit PDF-fetch verification.

### 12. Effort estimate
**~2 h** (5 PDF fetches + 5 SHA computations + 5 registry rows + 2 verdict
re-emission lines + dual-SHA companion rows).

### 13. Substrate-framing reminder
Fisher forecasts are observability-window predictions for detectors; they
quantify how narrowly a detector can constrain a substrate-prediction value
once data lands. The Fisher-PDF registry pins the OBSERVABILITY side of the
substrate prediction → relay propagation → detector resolution chain;
substrate physics is upstream and unchanged by SHA-pinning Fisher PDFs.

---

## §W12-4. S86-DR3-3-LAYER-SUB-TREE (C33)

### 1. Gate ID
`S86-DR3-3-LAYER-SUB-TREE`

### 2. Trigger
**[VERIFY]** — 21-cell determinism + monotonicity verification.

### 3. Classification
**PHONONIC** (substrate-prediction stability across regulator-layer L_max
∈ {8, 10, 12} — DR3 sub-tree probes whether the framework's BAO/RSD
prediction varies coherently with cutoff-axis L_max in the sense of
W3-G42 rectangle migration).

### 4. Agent type (runtime)
`mack-cosmic-bridge` (DR3-owner per `feedback_mack-bridge-role.md`; the
DR3 7-cell tree was authored by mack in S85 W1a-5 and the L_max sub-tree
extension is mack-territory).

NOT `gen-physicist`.

### 5. Hypothesis
The S85 W1a-5 DR3 7-cell decision tree (single L_max=10 layer) extends
cleanly to a 21-cell L_max ∈ {8, 10, 12} matrix in which (a) every cell is
deterministic (one verdict per cell, no ambiguity), (b) every column
(fixed cell across L_max) is monotone (cell-status changes only in one
direction across L_max — no oscillation A → B → A).

### 6. Method (complete dispatch prompt)

```
You are mack-cosmic-bridge executing C33 / S86-DR3-3-LAYER-SUB-TREE.

OBJECTIVE: Generate the DR3 7-cell × 3-layer = 21-cell sub-tree matrix and
verify determinism + monotonicity.

ENVIRONMENT:
  - Python: phonon-exflation-sim/.venv312/Scripts/python.exe
  - from canonical_constants import * — pull L_max=10 baseline values from
    canonical_constants.py and from sessions/archive/session-85/working-paper-w1a.md
    §W1a-5 7-cell DR3 tree.
  - GPU: torch.linalg if any matrix re-computation is required at L=8 or
    L=12; default is to read pre-computed cached values where they exist
    in computations/_dk_cache/.
  - Cap OMP_NUM_THREADS = 8 if CPU-fallback path is used (per
    feedback_compute-environment.md).

INPUTS:
  - The S85 W1a-5 7-cell DR3 decision tree:
      cells: {C1, C2, C3, C4, C5, C6, C7}  (7 DR3 outcome cells from S85 W1a-5)
      each cell at L_max=10 has a verdict V_{cell, L=10} ∈ {PASS, FAIL, INFO}
  - The L_max=8 and L_max=12 D_K eigenvalue caches in computations/_dk_cache/.

STEPS:
  1. For each L_max ∈ {8, 10, 12}:
     (a) Re-evaluate the 7 DR3 cells under that L_max regulator layer
         using the same decision rule as S85 W1a-5 (cite the decision-rule
         specification from working-paper-w1a.md §W1a-5).
     (b) Record the verdict V_{cell, L} for all 7 × 3 = 21 cells.

  2. Construct the 21-cell matrix:

         |       | L=8         | L=10        | L=12        |
         |:------|:------------|:------------|:------------|
         | C1    | V_{C1,8}    | V_{C1,10}   | V_{C1,12}   |
         | C2    | V_{C2,8}    | V_{C2,10}   | V_{C2,12}   |
         | ...   | ...         | ...         | ...         |
         | C7    | V_{C7,8}    | V_{C7,10}   | V_{C7,12}   |

  3. Determinism check (per cell):
       For each (cell, L_max) entry, verify exactly ONE verdict is assigned
       (no ambiguity, no "PASS or INFO" mixed-state cells).
       PASS iff 21/21 cells have unique verdict.

  4. Monotonicity check (per cell across L_max):
       For each cell C_i, examine the sequence (V_{C_i, 8}, V_{C_i, 10}, V_{C_i, 12}).
       PASS iff the sequence is monotone in the partial order
         FAIL < INFO < PASS    (strict; no oscillation A → B → A).
       Equivalently: NO pattern (PASS, FAIL, PASS) or (FAIL, PASS, FAIL) or
       (INFO, FAIL, INFO) or any other A → B → A oscillation across the
       3-layer L_max axis.

  5. Construct the failure-classification list:
       For any cell that fails determinism, log "AMBIGUOUS-{cell}".
       For any cell that oscillates, log "OSCILLATION-{cell}-{seq}" e.g.
       "OSCILLATION-C3-(PASS,FAIL,PASS)".

  6. Output the matrix + classification list to a markdown table at
     computations/_artifacts/s86_dr3_3layer_subtree.md and append the
     verdict line.

OUTPUT TARGETS:
  - computations/_artifacts/s86_dr3_3layer_subtree.md (21-cell table)
  - computations/s86_w12_dr3_3layer_subtree.py (the producing script)
  - computations/s86_gate_verdicts.txt (verdict line)

VERDICT:
  PASS iff (21/21 cells deterministic) AND (7/7 cells monotone across L_max);
  FAIL if any cell ambiguous OR any cell oscillates.

GPU: torch.linalg ONLY if L_max=8 or L_max=12 D_K matrix re-evaluation
     required (matrices exceed 100×100 at L=8: ~1024 dim; L=12: ~270K dim
     — definitely GPU territory). Default is to read pre-computed cached
     verdicts.
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin |
|:---------------|:----|
| Cell roster (7 cells)             | C1-C7 from S85 W1a-5 DR3 7-cell decision tree |
| L_max layer axis                   | {8, 10, 12} closed set |
| Decision rule per cell            | INHERITED from S85 W1a-5 §W1a-5 decision-rule spec (no re-design at S86) |
| Determinism criterion             | exactly one verdict per (cell, L_max) entry |
| Monotonicity partial order         | FAIL < INFO < PASS (strict) |
| Oscillation pattern definition     | any sequence (X, Y, X) with X ≠ Y across the 3-layer axis |
| Verdict-cache source              | computations/_dk_cache/ (read-only) |
| GPU pin                           | torch.linalg for L=12 D_K matrix ops if required; else CPU OMP=8 |
| Random seed                       | NOT APPLICABLE (deterministic decision tree from D_K eigenvalues) |

### 8. Expected output 4-tuple
`(value=<n_det>/21+<n_mono>/7, scheme=21-cell-3-layer-DR3-subtree, convention=monotone-FAIL-INFO-PASS, L_max=8,10,12)`

### 9. PASS/FAIL/INFO thresholds

- **PASS** iff (21/21 cells deterministic) AND (7/7 cells monotone — no
  A → B → A oscillation across the L_max ∈ {8, 10, 12} axis).
- **FAIL** if any cell ambiguous OR any cell oscillates.
- **INFO** band: if 21/21 deterministic but 1-2 cells exhibit (X, Y, Y) or
  (X, X, Y) "step-monotone" patterns rather than strict monotonicity, emit
  INFO with explicit cell list. ≥3 step-monotone cells is FAIL (indicates
  systematic L_max sensitivity warranting cutoff_axis re-pin per W4 / R3).

Tolerance: ABSOLUTE (cell-count and oscillation-pattern matching).

Verdict line:
```
S86-DR3-3-LAYER-SUB-TREE: PASS|FAIL|INFO -- value=<n_det>/21,<n_mono>/7 scheme=21-cell-3-layer-DR3-subtree convention=monotone-FAIL-INFO-PASS L_max=8,10,12 sha256=<closure>
```

### 10. Substitution chain (REQUIRED — monotonicity direction)

```
Definition 1: V_{C, L}    = verdict of cell C ∈ {C1..C7} at layer L ∈ {8, 10, 12}
Definition 2: P            = partial order on verdicts: FAIL < INFO < PASS
Definition 3: monotone(C)  = (V_{C,8} ≤_P V_{C,10} ≤_P V_{C,12}) OR
                             (V_{C,8} ≥_P V_{C,10} ≥_P V_{C,12})
Definition 4: oscillation(C) = ∃ X, Y ∈ {PASS, INFO, FAIL}, X ≠ Y, such that
                              the sequence (V_{C,8}, V_{C,10}, V_{C,12}) = (X, Y, X)

Substitute into the gate criterion:
  Step 1: PASS iff for ALL C ∈ {C1..C7}, monotone(C) AND NOT oscillation(C)
  Step 2: monotone(C) AND NOT oscillation(C) ⟺ the 3-element sequence
          (V_{C,8}, V_{C,10}, V_{C,12}) is sorted (weakly increasing or
          weakly decreasing) in the partial order P.
  Step 3: For 7 cells: 7 monotone checks; PASS-count = # monotone cells.

Simplify to canonical form:
  PASS iff #{C : monotone(C) AND NOT oscillation(C)} = 7

Direction (read from canonical form):
  As L_max increases (8 → 10 → 12), the cutoff-axis tightens. A cell that
  is FAIL at L=8 and PASS at L=12 indicates a truncation-resolution
  signature (PASS direction is "more eigenmodes captured"). A cell that
  is PASS at L=8 and FAIL at L=12 indicates a cutoff-induced spurious-PASS
  at low L (FAIL direction is "spurious PASS revealed by tighter cutoff").
  Either monotone direction is admissible — the gate forbids ONLY oscillation.

Conclusion: monotonicity is direction-agnostic; oscillation is the
falsifying signature. The 7-cell × 3-layer structure tests for
L_max-stability of the substrate prediction; oscillation indicates
the prediction is regulator-layer dependent (a violation of
spectral-prediction independence from cutoff axis).
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** strengthens the DR3 prediction substantially: the framework's
  BAO/RSD response to DR3 data is L_max-stable, meaning the substrate-prediction
  values flowing into the W3-G42 r=R_842 rectangle are not artifacts of
  the L=10 truncation. This is a substrate-prediction-independence
  certification — analogous to spectral-prediction independence from
  cutoff convention (per `.claude/rules/phononic-framing.md` substrate-not-c-limited
  framework). Promotes DR3 to a stable carry-forward to S87+ DR3 live-watch.
- **FAIL** indicates regulator-layer sensitivity in the DR3 prediction —
  specifically that one or more 7-cell DR3 outcomes oscillates across L_max.
  Triggers W4-style cutoff_axis re-pin (R3 YAML schema re-evaluation, per
  W0a R3) and downgrades the DR3 prediction from "stable" to "L=10-conditional"
  in the carry-forward inventory. The OSCILLATION-{cell}-{seq} log identifies
  exactly which DR3 cell needs cutoff_axis investigation.
- **INFO** (1-2 step-monotone cells): monotonicity holds but with a step
  pattern; cells in question warrant a single-layer follow-up at S87+ DR3
  live-watch to disambiguate whether the step is genuine convergence or
  a sub-threshold oscillation.

### 12. Effort estimate
**~6 h** (largest single effort in W12; involves 7 cells × 3 L_max layers
= 21 verdict re-evaluations, with potential D_K eigenvalue cache reads at
L=8 and L=12 if the cached verdicts are absent — D_K cache lookup is fast
once the cache exists, but cache-construction at L=12 is GPU-bound).

### 13. Substrate-framing reminder
The DR3 7-cell decision tree gates the framework's BAO/RSD prediction
against DR3-published (w_0, w_a) values; the L_max axis is the spectral
cutoff regulating how many D_K eigenmodes are summed in the prediction.
PASS = the prediction is independent of the regulator (the framework's
substrate prediction is intrinsic to the spectral triple, not to the
truncation level). FAIL = the prediction is regulator-induced — the
substrate-prediction story would then be misframing a cutoff-induced
artifact as a substrate signal. Container thinking would describe DR3
cells as "BAO measurements"; substrate framing describes them as
substrate-spectral-prediction stability tests against an observed-data
rectangle (R_842 from S83 W3-G42).

---

## §W12-5. S86-CMB-HD-ALPHA-S-FORECAST-PIN (C36)

### 1. Gate ID
`S86-CMB-HD-ALPHA-S-FORECAST-PIN`

### 2. Trigger
**[AUDIT]** — quarterly poll-status audit. The gate fires every quarter
through 2026-2030 to check for explicit CMB-HD σ(α_s) forecast publication
and pin/re-fire on hit.

### 3. Classification
**META** (forecast-monitoring discipline; not a substrate prediction).

### 4. Agent type (runtime)
`mack-cosmic-bridge` (forecast-monitoring discipline; mack owns the
α_s constraint landscape per `feedback_mack-bridge-role.md` and S85 W1b
α_s pin canonical-update history).

NOT `gen-physicist`.

### 5. Hypothesis
By quarterly polling 3 source streams (Abazajian + companion publications;
CMB-HD SciBook code release; CMB-S4/CMB-HD joint forecast literature),
the framework will detect publication of an explicit CMB-HD σ(α_s) forecast
within the 2026-2030 window. On detection, the forecast PDF is SHA-pinned
and S85 W1b-6 α_s prediction (1-σ band [+0.0023 ± 0.0063] from S85 W1b-8
canonical-update) is re-fired against the new σ.

### 6. Method (complete dispatch prompt)

```
You are mack-cosmic-bridge executing C36 / S86-CMB-HD-ALPHA-S-FORECAST-PIN.

OBJECTIVE: Quarterly poll discipline for CMB-HD σ(α_s) forecast publication;
on publication, SHA-pin + re-fire S85 W1b-6 verdict.

ENVIRONMENT:
  - Python: phonon-exflation-sim/.venv312/Scripts/python.exe
  - WebSearch / WebFetch / paper-search MCP for publication monitoring.
  - from canonical_constants import * — pull alpha_s_canon_2020 = +0.0023
    ± 0.0063 (S85 W1b-8 update from Aiola+ 2020 ACT DR4) and S85 W1b-6
    framework prediction value.

POLL SOURCES (quarterly check, 3 streams):
  (1) Abazajian + CMB-HD-companion publication stream — check arXiv astro-ph
      for new CMB-HD-tagged papers since last poll.
  (2) CMB-HD SciBook code release tracker — monitor https://cmb-hd.org/
      and any associated GitHub repos for explicit σ(α_s) forecast file.
  (3) CMB-S4 / CMB-HD joint forecast paper stream — check Google Scholar
      for "CMB-S4 CMB-HD joint" or "CMB-HD α_s forecast" hits since last
      poll.

POLL CADENCE: quarterly (every 3 months). S86 instance covers 2026-Q2.

PER-POLL STEPS:
  1. Run 3 source-stream queries; record returned hits.
  2. For each hit, classify:
     - DOES IT publish an explicit σ(α_s) value? (numeric forecast for the
       running of the spectral index from CMB-HD baseline detector spec)
     - If YES → SHA-pin the publication PDF (per C32 protocol):
         (a) Fetch PDF.
         (b) Compute SHA-256.
         (c) Append registry row to sessions/framework/registry/fisher-pdf-registry.md
             (extending C32 registry with CMB-HD row).
         (d) Update canonical_constants.py with `sigma_alpha_s_CMB_HD` entry
             (provenance: publication citation + SHA + S86-W12-5 gate).
         (e) Re-fire S85 W1b-6 verdict: read original W1b-6 verdict line,
             compute new sigma-distance under updated σ, append re-emission
             line to s86_gate_verdicts.txt with dual-SHA companion row.
     - If NO → log "NO-EXPLICIT-FORECAST-{poll-date}" to
       sessions/framework/registry/cmb-hd-alpha-s-poll-log.md and emit INFO verdict.

  3. If poll cadence is missed (no quarterly run), emit FAIL.

OUTPUT TARGETS:
  - sessions/framework/registry/cmb-hd-alpha-s-poll-log.md (per-poll log entry,
    appended chronologically)
  - sessions/framework/registry/fisher-pdf-registry.md (additional row IF publication
    detected)
  - computations/canonical_constants.py (sigma_alpha_s_CMB_HD entry IF
    publication detected)
  - computations/s86_gate_verdicts.txt (verdict line for this gate +
    re-emission line for W1b-6 IF publication detected)

VERDICT:
  PASS iff publication detected AND SHA-pinned AND W1b-6 re-fired;
  INFO if poll completed AND no publication available (publication has not
       yet been issued — poll continues at next quarter);
  FAIL if poll skipped (cadence violation).

GPU: NONE.
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin |
|:---------------|:----|
| Poll source streams (closed)        | {Abazajian-companion arXiv, CMB-HD SciBook code release, CMB-S4/CMB-HD joint forecast literature} |
| Poll cadence                         | quarterly (every 3 months) |
| Detection criterion                  | publication contains explicit numeric σ(α_s) forecast for CMB-HD detector |
| SHA-pin protocol                     | inherits C32 protocol (SHA-256 full 64-char hex, registry append) |
| Re-fire target                       | S85 W1b-6 verdict |
| Canonical-constants entry name      | `sigma_alpha_s_CMB_HD` (added on detection only) |
| Poll-log path                        | `sessions/framework/registry/cmb-hd-alpha-s-poll-log.md` |
| Cadence-missed verdict               | FAIL (skipped poll = gate failure) |

### 8. Expected output 4-tuple
`(value=<poll_status>, scheme=quarterly-cmb-hd-alpha-s-poll, convention=3-stream-detection, L_max=NA)`

where `<poll_status>` ∈ {PUBLISHED-PINNED, NO-PUBLICATION-YET, SKIPPED}.

### 9. PASS/FAIL/INFO thresholds

- **PASS** iff publication detected within poll AND SHA-pinned AND W1b-6
  re-fired with dual-SHA companion row.
- **INFO** if poll completed AND no publication available (next quarterly
  poll continues; this is the expected outcome at S86-Q2 and likely
  S87-Q3, S88-Q4, etc., until publication occurs).
- **FAIL** if quarterly poll cadence missed (no poll run for >3 months
  since prior poll OR S86 first-poll skipped entirely).

Tolerance: ABSOLUTE (poll cadence is binary; publication detection is
binary).

Verdict line:
```
S86-CMB-HD-ALPHA-S-FORECAST-PIN: PASS|INFO|FAIL -- value=<poll_status> scheme=quarterly-cmb-hd-alpha-s-poll convention=3-stream-detection L_max=NA sha256=<closure>
```

### 10. Substitution chain
NOT REQUIRED for this gate (poll-status audit; no sign/direction/threshold
claim involved). The PASS/INFO/FAIL boundary is enumerated qualitatively in §9.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** updates the framework's α_s observability landscape: CMB-HD
  σ(α_s) becomes the binding constraint (likely much tighter than
  current Planck/ACT DR4 σ=0.0063), and the framework's α_s prediction
  (S85 W1b-6) is re-evaluated against the new sensitivity. The re-emission
  may convert W1b-6 from PASS to TENSION or even FAIL if the framework's
  α_s value lies outside the new CMB-HD 1σ band.
- **INFO** (the expected S86-Q2 outcome): no publication yet; quarterly
  poll continues. This is NOT a failure — it is correct discipline-execution
  recording the absence of publication.
- **FAIL** (cadence violation) means the framework lost its forecast-monitoring
  discipline and the α_s landscape may have shifted unmonitored. Re-establish
  poll cadence in S87.

### 12. Effort estimate
**~0.5 h per quarterly poll** (3 source-stream queries + classification +
log entry). On detection, additional ~1 h for SHA-pin + W1b-6 re-emission.

S86 first poll: 0.5 h (no publication expected in 2026-Q2).

### 13. Substrate-framing reminder
CMB-HD σ(α_s) is a Fisher-forecast observability bound — it pins how
narrowly a future detector will be able to constrain the running of the
spectral index, an observable derived from substrate-spectral-prediction
of inflationary-equivalent quantities. The forecast itself is detector
specification, not substrate physics; the framework's α_s prediction
(S85 W1b-6 = +0.0023 ± framework-σ) is the substrate-side quantity. The
poll-and-pin discipline ensures that when the detector specification
publishes, the framework's substrate-side prediction is immediately
re-tested against it without iterate-until-PASS post-hoc adjustment.

---

## §X. Wave W12 → Downstream Decision Point

W12 outputs feed two downstream landings:

1. **W13 P11 master inventory** — C30 9-cell detector matrix is the
   row-source for P11's 6 PAIR-enrichments + 1 NEW row class promotion to
   `sessions/framework/registry/falsifier-master-inventory.md`. Without C30 PASS,
   P11 is operating on agent-memory-recall rows. C32 Fisher-PDF SHA-pins
   provide the σ-target audit-trail for P11's NEW row class entries.

2. **S88 BK-Array ingest gate** (from C25 external-clock scaffold W0c-i) —
   C31 BK-Array 2026 classifier is the SCRIPT-side commit that the C25
   scaffold-gate references as its computational ingest path. When BK-Array
   publishes (expected 2026-mid), the S88 ingest gate fires the C31
   classifier on the published `r_observed` value and routes the framework
   response per the 4-branch decision tree.

3. **S87+ DR3 live-watch** — C33 PASS converts DR3 from "L_max=10 conditional
   prediction" to "L_max-stable substrate prediction"; the live-watch then
   gates against the W3-G42 R_842 rectangle with full regulator-layer
   stability. C33 FAIL would force a cutoff_axis re-pin at S87 (R3 YAML
   schema follow-up).

4. **S86+ α_s monitoring (S87, S88, ... — quarterly)** — C36 establishes
   the cadence; S87 W12-equivalent will re-fire as the next quarterly poll.
   This is a perpetual carry-forward until CMB-HD publishes its forecast.

---

## §0.10. Wave W12 Machinery-Enumeration Pin (PRDR)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, every
free parameter that drives a W12 gate is enumerated below. Each row is the
GATE × PARAMETER × PIN-VALUE triplet that PRDR mandates BEFORE plan-freeze.

| Gate | Parameter | Pin |
|:-----|:----------|:----|
| C30 | detector roster (9 names) | {PIXIE, DESI DR3, CMB-S4, LISA, LiteBIRD, BK-Array, CMB-HD, SKA-1, lab-analogs ³He-B + K-STAR} |
| C30 | field schema (5 columns) | {status, launch-or-data-window, σ-target, framework prediction, EVOI tag} |
| C30 | EVOI tag taxonomy | {DECISIVE, DISCRIMINATING, CONFIRMATORY, LAB-FALSIFIER} |
| C30 | TBD-S87 admissibility | YES (cited cell, no current value) |
| C31 | b1_b2 | 0.005 |
| C31 | b2_b3 | 0.015 |
| C31 | b3_b4 | 0.030 |
| C31 | r_PathH | 0.00745 (S85 W1b-6) |
| C31 | r_PathC | 0.0117 (S85 W1b-6) |
| C31 | synthetic test inputs | {0.003, 0.012, 0.025, 0.040} |
| C31 | comparison operator | left-open / right-closed at every boundary |
| C32 | PDF list (5) | {CMB-S4 SB v2 2022, DESI 2025 BAO forecast, LiteBIRD Hazumi 2022, CMB-HD Sehgal 2019, HERA Memo 54 Ali+ 2018} |
| C32 | hash algorithm | SHA-256 full 64-char hex |
| C32 | re-emission targets | S85 W4-3, W4-6 |
| C32 | INFO band | 1-2 unfetchable PDFs (TBD-S87 with citation) |
| C32 | FAIL threshold | ≥3 unfetchable PDFs OR re-emission skipped |
| C33 | cell roster | {C1, C2, C3, C4, C5, C6, C7} from S85 W1a-5 DR3 7-cell tree |
| C33 | L_max layer axis | {8, 10, 12} |
| C33 | decision rule | INHERITED from S85 W1a-5 §W1a-5 (no re-design) |
| C33 | partial order | FAIL <_P INFO <_P PASS (strict) |
| C33 | oscillation pattern | sequence (X, Y, X) with X ≠ Y across 3-layer axis |
| C33 | INFO band | 1-2 step-monotone cells (X, Y, Y) or (X, X, Y) |
| C33 | GPU pin | torch.linalg for L=12 D_K (~270K dim); CPU OMP=8 fallback |
| C36 | poll source streams (3) | {Abazajian-companion arXiv, CMB-HD SciBook code release, CMB-S4/CMB-HD joint forecast literature} |
| C36 | poll cadence | quarterly (every 3 months) |
| C36 | detection criterion | publication contains explicit numeric σ(α_s) forecast for CMB-HD |
| C36 | re-fire target | S85 W1b-6 |
| C36 | cadence-missed verdict | FAIL |

PRDR-cardinality target: D_PRU_raw = 0 across all 5 W12 gates. No free
parameter unpinned at plan-freeze.

---

## §0.11. Wave W12 Input-SHA Ledger

| Input file (read-only by W12 scripts) | Computed-at-runtime SHA-256 marker | Notes |
|:--------------------------------------|:-----------------------------------|:------|
| `sessions/framework/registry/baseline-findings-s66.md` | `<runtime>` | C30 row-source for status/window/EVOI cells |
| `sessions/framework/registry/falsifier-master-inventory.md` | `<runtime>` | C30 row-source; C31 r-pin reference |
| `computations/canonical_constants.py` | `<runtime>` | C30 σ-target source where canonical; C31 Path-H/C r values; C36 alpha_s_canon_2020 |
| `computations/s85_gate_verdicts.txt` | `<runtime>` | C32 W4-3/W4-6 source; C36 W1b-6 source |
| `sessions/archive/session-85/working-paper-w1a.md` | `<runtime>` | C33 §W1a-5 DR3 7-cell tree decision rule |
| `computations/_dk_cache/L8/...`         | `<runtime>` | C33 L=8 verdict cache (read-only) |
| `computations/_dk_cache/L10/...`        | `<runtime>` | C33 L=10 verdict cache (read-only) |
| `computations/_dk_cache/L12/...`        | `<runtime>` | C33 L=12 verdict cache (read-only) |

External literature-PDF SHA-pins (computed by C32 + C36 at runtime, recorded
in `sessions/framework/registry/fisher-pdf-registry.md`):
- Abazajian+ 2022 CMB-S4 SB v2 PDF SHA — `<computed-at-runtime>`
- DESI 2025 BAO forecast PDF SHA — `<computed-at-runtime>`
- LiteBIRD Hazumi 2022 PDF SHA — `<computed-at-runtime>`
- CMB-HD Sehgal 2019 PDF SHA — `<computed-at-runtime>`
- HERA Memo 54 Ali+ 2018 PDF SHA — `<computed-at-runtime>`
- (C36 IF publication detected) CMB-HD σ(α_s) forecast PDF SHA — `<computed-at-runtime>`

Each W12 verdict line MUST include the `sha256=<closure>` 64-char hex
closure-SHA per `.claude/rules/gate-verdicts.md` S81+ canonical form, with
audit_sha256 dual-SHA companion row per W9a-99 split.

---

**End of Wave W12 plan.** 5 gate blocks at full 13-field spec; runtime owner
`mack-cosmic-bridge` (alternates assigned per gate); combined effort
~16-18 h; output: `sessions/framework/registry/detector-readiness-9-cell.md`,
`sessions/framework/registry/fisher-pdf-registry.md`,
`sessions/framework/registry/cmb-hd-alpha-s-poll-log.md`,
`computations/s86_bk_array_2026_classifier.py`,
`computations/s86_w12_dr3_3layer_subtree.py`,
`computations/_artifacts/s86_dr3_3layer_subtree.md`,
`computations/s86_gate_verdicts.txt` (5 verdict lines + 2 re-emission
lines for W4-3/W4-6 + 1 re-emission line for W1b-6 IF C36 detects publication).
