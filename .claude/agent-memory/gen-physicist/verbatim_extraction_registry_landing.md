---
name: verbatim-extraction-registry-landing
description: Single-shot AFTER-pattern §VII registry landing of a frozen Stage-0 candidate — programmatic byte-exact span extraction, header-anchor symmetry, binary-append no-flatten, byte-restoration on a script-bug FAIL.
metadata:
  type: feedback
---

Landing a frozen Stage-0 STAGE-1-CANDIDATE (or exact-result/structural-theorem) into `permanent-results-registry.md` §VII.X via the single-shot AFTER pattern. Recurs across the whole W6/W7 registry-landing chain (S101 W6-1..W6-8 were six such landings).

**Why:** the binding-text rule forbids re-deriving any clause — the candidate's own every-step proofs (L0/T1/T2/P/U + LaTeX `$$\tag{En}$$` blocks + witness table) must land byte-for-byte. Manual transcription of a 14k-char markdown+LaTeX span WILL drift; extract it programmatically from the SHA-pinned synthesis instead.

**How to apply:**

1. **Verify the source SHA matches the plan `input_files:` pin FIRST**, then extract spans by literal-substring anchors (`text.find(START)` → `text.rfind('\n\n', clause_idx, next_section_idx)` for the end). HARD-assert each span's SHA + char-length (a `# (local)`-tagged length pin) at runtime; a drift → `sys.exit(4)` (script breakage, exit≠0, NOT a verdict) BEFORE any disk write. Compute the span SHAs/lengths in a throwaway Bash probe at plan-prep and pin them as constants.

2. **HEADER-ANCHOR SYMMETRY (the bug that cost a re-run on S101 W6-6).** The plan's MANDATORY HEADER (a) text often quotes `## §VII.X — …`, but the on-disk registry convention is `### §VII.X — …` (THREE hashes; check the §VII.B* neighbors). Your `re_read_section` anchor (`text.rfind("### §VII.X ")`, trailing space + em-dash) MUST match the header `build_promotion_text` actually writes. A double-prefix (`### ## §VII.X`) lands the section but makes `re_read_section` return `""` → `content_sha256 = e3b0c44298fc1c14…` (the empty-string SHA) → spurious FAIL. Build `parts[0] = "### " + header` where `header` carries NO leading hashes.

3. **write_atomic_with_fsync = binary-append, mode `'ab'`, bytes already LF-terminated, NO neighbor flatten** (the W6-3 lesson). The registry mixes LF + a few CRLF lines (S101: 20 CRLF); a text-mode `'w'`/CRLF-preserving r/w round-trip re-encodes neighbor line-endings and corrupts prior entries. Binary-append touches ONLY the added bytes — confirm `CRLF count unchanged` post-append.

4. **Idempotency + PD-2/PD-3.** All-header-level scan (`^#{2,4}\s*§VII\.X\b`) for occupancy. If occupied by the gate's OWN byte-identical prior landing → SKIP append (NO-OP). If FOREIGN → PD-3 reroute next-free letter + emit FAIL-with-remediation. Pin the FROZEN run-1 registry PRE-SHA (= the prior wave's POST-SHA) in the audit-pin map so `audit_sha256` is reproducible across re-runs.

5. **Script-bug FAIL ⇒ byte-restore, then fix, then re-run (NOT convention-shopping).** A FAIL from a broken predicate (anchor mismatch) is a CORRECT report, not a physics FAIL. The malformed append still landed: surgically restore the registry to the prior POST byte-length (`b[:PRE_LEN]`; verify SHA equality on disk) — note the end-marker `\n\n###…` can eat the prior trailing `\n`, so truncate by KNOWN byte-length, not by marker-find. Fix the script, re-run; emitted SHAs are the post-fix bytes. Disclose the deviation in the WP §Methodology (v3-closure-recovery Class-1 boundary; honest disclosure = in-session script-health correction).

6. **Promotion-text wrapper = the ONLY authored prose.** Around the verbatim span(s): header (a); Stage-0-authorship blockquote + authorship/Stage-2-routing (c); forward-gate pointer (d, CITED not a clause); registry-anatomy block (e: 5-anatomy N/A-with-reason for intra-pillar theorems; SINGLE-READING operator/projector-side when only functional-of-P clauses exist → bare slot admissible; Level-1 single-τ vs Level-2 moduli-deformation tag). Stage-2 EXCLUDES the Stage-0 author INCLUDING successor spawns (downstream-inheritance reach via the author's memory file).

7. **Verdict predicate = section-match boolean ∧ caveat-grep==1 ∧ STAGE-1-CANDIDATE-present**, all RE-READ from disk (not in-memory). For STAGE-1 landings carrying a MANDATORY caveat, grep its exact marker on the re-read section (hit count == 1). Related: [[wp_shell_generation]] (the WP shell this fills), [[register_sourced_gate_machinery_recovery]] (recovering machinery when the source is a register not a frozen synthesis).
