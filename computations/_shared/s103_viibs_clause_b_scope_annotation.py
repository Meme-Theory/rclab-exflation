#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION
=====================================
Reviewed designated-writer ANNOTATION on the EXISTING §VII.BS entry in
sessions/permanent-results-registry.md.

This is NOT a registry-LANDING (no new §VII slot, no Stage-0 candidate consume).
It is a targeted curated-doc Edit that applies the S-1 connes synthesis §IV.D
verbatim SCOPE ANNOTATION to the §VII.BS ANNOTATION SURFACES ONLY:

  Surface 1 — HEADER parenthetical (§IV.D item (2))
  Surface 2 — INDEX-table row parenthetical (§IV.D item (3))
  Surface 3 — clause-(b) inline (clause-attribution table row)
  Surface 4 — NEW SCOPE-ANNOTATION block after the clause-attribution table
              (§IV.D item (1); out-of-frozen-block, modeled on §VII.BP
               BINDING AMENDMENT pattern)

The FROZEN Stage-0 theorem-tag blockquote (the line
'> **Normalization Non-Universality (N₃=0 corollary, rank-1).**' ... ,
span len 2514, span SHA256 e669ccd2daa5aa5be7396499f59c0636a803eac02e1f7710c2a1fc428d3cdaba)
is BYTE-SHA-IMMUNE: it is located by literal-substring anchor (not line number)
and its SHA is HARD-ASSERTED UNCHANGED (== e669ccd2…) before AND after the write.
A span-SHA mismatch is a FAIL (the most serious — the immune Stage-0 text must
never change). Theorem grade STAGE-3-PERMANENT is UNCHANGED.

NUMBERS first, gate second, interpretation third.

Pattern: build_annotation_text -> write_atomic_with_fsync -> re_read + verify
         -> exactly ONE emit (verdict payload printed for emit_verdict MCP tool).

Substitution chain (the asserted direction relation; plan §W1-6 substitution_chain):
  N3=0 is NECESSARY for the single-cutoff import (BDI vacuum imports the cutoff
  M_KK), but the COUNT (rank-1) requires ALSO bundle-exhaustiveness over the
  dagger-rows (Open Q6) AND rests on FULL BDI triviality (N3=N1=winding=eta=0,
  s44 anchor), NOT N3=0 alone. N3=0 alone is the WEAKER necessary condition;
  the count requires the STRONGER conjunction.

ENV: cpu, OMP 8; string assembly + SHA + file I/O only.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import json
import hashlib
import datetime
from pathlib import Path

import numpy as np

# Canonical constants import (MANDATORY per math-scripts.md; this gate uses none
# numerically, but compliance + runtime SHA disclosure of the file is required).
sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import *  # noqa: F401,F403  (compliance import)

# ----------------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------------
ROOT = Path(".").resolve()
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
S1_SYNTH = ROOT / "sessions" / "session-102" / "session-102-connes-ncg-vii-bs-sufficiency-synthesis.md"
S44_NPZ = ROOT / "computations" / "session-44" / "s44_n3_bdg.npz"
CC_PY = ROOT / "computations" / "_shared" / "canonical_constants.py"
NPZ_OUT = ROOT / "computations" / "session-103" / "s103_viibs_clause_b_scope_annotation.npz"

SCRIPT_PATH = Path(__file__).resolve()

# ----------------------------------------------------------------------------
# Frozen-span guard (the IMMUNE Stage-0 theorem-tag blockquote)
# ----------------------------------------------------------------------------
FROZEN_BLOCKQUOTE_ANCHOR = "> **Normalization Non-Universality (N₃=0 corollary, rank-1).**"
FROZEN_SPAN_LEN = 2514                                                       # (local) len pin
FROZEN_SPAN_SHA_PIN = "e669ccd2daa5aa5be7396499f59c0636a803eac02e1f7710c2a1fc428d3cdaba"


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def print_verdict_payload(payload: dict) -> dict:
    """Canonical template helper (`.claude/templates/script-template.py` §4):
    PRINT the delimited verdict PAYLOAD block to stdout for the dispatching AGENT
    to pass to the knowledge-MCP `emit_verdict` tool. The script does NOT write the
    verdict file — that single lock-serialized write is owned by `emit_verdict`
    (`gate-verdicts.md §"Race-Safe Emission"`). The script computes the dual-SHA
    (it alone holds the input-pin map + content target); the agent reads this block
    and calls `mcp__knowledge__emit_verdict(**payload)`. Returns the payload dict."""
    print("\n<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload, ensure_ascii=False) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def extract_frozen_span(text: str) -> str:
    """Locate the frozen Stage-0 blockquote span by literal anchor (NOT line number).
    The span is the full blockquote LINE (incl. the leading '> ' marker) up to the
    terminating newline. len == 2514 by construction."""
    i = text.find(FROZEN_BLOCKQUOTE_ANCHOR)
    if i < 0:
        raise RuntimeError("FROZEN blockquote anchor not found in registry")
    end = text.find("\n", i)
    if end < 0:
        end = len(text)
    return text[i:end]


# ----------------------------------------------------------------------------
# Surface anchors (each must be UNIQUE in the registry)
# ----------------------------------------------------------------------------
# Surface 1 — HEADER parenthetical (line ~21379). Full distinguishing context so the
# blockquote occurrence of '(N₃=0 corollary, rank-1)' is NOT matched.
HEADER_OLD = "### §VII.BS — Normalization Non-Universality (N₃=0 corollary, rank-1): the substrate"
HEADER_NEW = "### §VII.BS — Normalization Non-Universality (N₃=0 corollary; single-cutoff COUNT for the a_n dagger-row bundle, rank-1): the substrate"

# Surface 2 — INDEX-table row parenthetical (line 157). §IV.D item (3) appends to the
# existing parenthetical. Anchor on the index-row head (distinct from header / blockquote).
INDEX_OLD = "| §VII.BS | THM | Normalization Non-Universality (N₃=0 corollary, rank-1) — the substrate determines the conformal class"
INDEX_NEW = "| §VII.BS | THM | Normalization Non-Universality (N₃=0 corollary, rank-1; single-cutoff COUNT for the dagger-row bundle, bundle-exhaustiveness a standing premise [Open Q6]) — the substrate determines the conformal class"

# Surface 3 — clause-(b) inline (the clause-attribution VERBATIM table row, line ~21392).
# The annotation surface is the per-clause table; the FROZEN blockquote's clause text is
# IMMUNE and untouched. This row is a Stage-0-transcribed annotation surface; per the plan
# it carries the clause-(b) scope inline marker. Anchor on the full row (unique).
CLAUSEB_OLD = "| (b) | N₃=0 → BDI single-cutoff count / Half B | **volovik-side** (superfluid-universe-topology axis, S44) |"
CLAUSEB_NEW = "| (b) | N₃=0 → BDI single-cutoff count / Half B *(scope: single-cutoff COUNT confirmed for the current dagger-row bundle; N₃=0 necessary, not sufficient; bundle exhaustiveness a separate standing premise — Open Q6; rests on FULL BDI triviality N₃=N₁=winding=η=0, see SCOPE ANNOTATION below)* | **volovik-side** (superfluid-universe-topology axis, S44) |"

# Surface 4 — NEW SCOPE-ANNOTATION block, inserted immediately AFTER the clause-attribution
# table (after the clause-(g) row), out-of-frozen-block, modeled on §VII.BP BINDING AMENDMENT.
# Insert anchor = the clause-(g) row (unique); insert the block on the line after it.
INSERT_AFTER_ANCHOR = "| (g) | moment-decoupling caveat (rank-1 covariance ≠ single-compute closure; F₋₁ vs F₊₁) | **phonon-first-side** (Re:V2/Q-PF3; volovik DISSENT confirmed) |"

# The SCOPE ANNOTATION block text — S-1 connes synthesis §IV.D item (1) VERBATIM, with a
# dated W2-1 cross-reference appended (optional per plan; no restructuring). The S44 second
# finding (FULL BDI triviality) is embedded verbatim in the §IV.D source text.
SCOPE_ANNOTATION_BLOCK = (
    "\n"
    "**SCOPE ANNOTATION — clause (b) single-cutoff COUNT (authoritative grade for downstream "
    "consumers; S103 W1-6 reviewed designated-writer annotation, S-1 connes synthesis §IV.D verbatim; "
    "out-of-frozen-block per the §VII.BP BINDING AMENDMENT precedent — the FROZEN Stage-0 blockquote "
    "above [theorem-tag span SHA `e669ccd2…`] is byte-IMMUNE and transcribed UNALTERED; theorem grade "
    "UNCHANGED STAGE-3-PERMANENT).** The W1-3 + W1-4 evidence establishes clause (b) as a "
    "**single-cutoff COUNT confirmed for the current dagger-row bundle** `p = (−1, +2, +4, +1, −1)` "
    "(the channels fixed by the a_n Seeley-DeWitt grading: gamma_unit, 1/G_induced, absolute_V0, "
    "M0_from_mH, sigma_over_m). It does NOT establish \"no second protected dimensional invariant in "
    "principle\": (i) the rank-1 covariance SVD is blind to a second scale confined to observables "
    "OUTSIDE the enumerated bundle (a genuinely rank-2 global covariance reads rank-1 on the enumerated "
    "sub-block) — **exhaustiveness of the dagger-row bundle is a separate standing premise**, with Open "
    "Question 6 (m_H / EW-VEV entering the induced action independently of M_KK) the named untested "
    "channel; (ii) the S44 anchor's single-cutoff conclusion rests on the FULL BDI topological triviality "
    "`N₃ = N₁ = BDI_winding = η_spectral = 0` (all measured, `s44_n3_bdg.npz`), of which N₃=0 is the most "
    "salient but not the sole ingredient. The N₃=0 ⇒ no-Fermi-point-protection-of-the-induced-metric "
    "statement is NECESSARY and dimension-count-robust (`spatial_dim = 0 < N_3_required_dim = 3`); the "
    "SUFFICIENCY-for-no-second-invariant reading is the standing premise above. The Stage-2 Axis-A "
    "clause-(b) PASS verified the BDI single-cutoff COUNT, not the no-second-invariant-in-principle claim. "
    "**Standing-premise → result (dated cross-reference, S103 W2-1):** the bundle-exhaustiveness premise "
    "Open Q6 names was tested this session by `S103-NNU-BUNDLE-EXHAUSTIVENESS` (W2-1, PASS, audit "
    "`ac1dbb2892cef172…`): the augmented borrowed-H shift-covariance with the second candidate scale "
    "`w2 = m_H/v_ew` returns `rank(Cov_aug) = 1` (second relative singular value `1.07e-17`, machine "
    "zero) ⇒ m_H factors through M_KK, the augmented bundle is exhaustive, and the clause-(b) sufficiency "
    "premise is CONFIRMED for the augmented bundle. The upgrade of this SCOPE ANNOTATION from "
    "standing-premise to result (re-wording clause (b)'s grade) is an S104 follow-up per the plan's "
    "Wave 1→2 decision point; the annotation lands as-worded here regardless. This narrowing changes ZERO "
    "gate verdicts and does NOT demote the theorem from STAGE-3-PERMANENT — it scopes one clause's claim "
    "to its evidence per `epistemic-discipline.md §\"Pole-Scope sub-clause\"` / `§\"Resolution-Specificity "
    "Scoping\"`.\n"
)


def build_annotation_text(pre_text: str) -> str:
    """Apply the 4 surface edits to a copy of the registry text, leaving the frozen
    blockquote span byte-identical. Returns the annotated text. Raises if any anchor
    is not unique or not found."""
    edits = [
        ("HEADER", HEADER_OLD, HEADER_NEW),
        ("INDEX", INDEX_OLD, INDEX_NEW),
        ("CLAUSEB", CLAUSEB_OLD, CLAUSEB_NEW),
    ]
    txt = pre_text
    for name, old, new in edits:
        n = txt.count(old)
        if n != 1:
            raise RuntimeError(f"surface {name}: anchor count {n} != 1 (old-text not unique/found)")
        txt = txt.replace(old, new, 1)

    # Surface 4 — insert the SCOPE-ANNOTATION block on the line after the clause-(g) row.
    n_ins = txt.count(INSERT_AFTER_ANCHOR)
    if n_ins != 1:
        raise RuntimeError(f"INSERT anchor (clause-g row) count {n_ins} != 1")
    ins_end = txt.find(INSERT_AFTER_ANCHOR) + len(INSERT_AFTER_ANCHOR)
    # the clause-(g) row is followed by '\n'; insert the block after that newline.
    nl = txt.find("\n", ins_end)
    if nl < 0:
        raise RuntimeError("no newline after clause-(g) row")
    txt = txt[: nl + 1] + SCOPE_ANNOTATION_BLOCK + txt[nl + 1 :]
    return txt


def write_atomic_with_fsync(path: Path, text: str) -> None:
    """Write the full annotated text atomically with fsync. The registry is read +
    written as UTF-8 text (the edits are interior-substring replacements + one block
    insertion on existing LF-terminated lines; no neighbor line-ending re-encode beyond
    the edited regions — we re-write the whole file in UTF-8, preserving the original
    newline bytes everywhere we did not edit because Python str read/write with
    newline='' round-trips LF and CRLF verbatim)."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def main():
    # ------------------------------------------------------------------ inputs
    pre_bytes = REGISTRY.read_bytes()
    pre_text = pre_bytes.decode("utf-8")
    pre_registry_file_sha = sha256_bytes(pre_bytes)                          # (local)

    s1_bytes = S1_SYNTH.read_bytes()
    s1_synth_file_sha = sha256_bytes(s1_bytes)                               # (local)

    cc_bytes = CC_PY.read_bytes()
    cc_runtime_sha = sha256_bytes(cc_bytes)                                  # (local)

    # FULL BDI triviality second-finding cross-check (s44 anchor; numeric witness).
    s44 = np.load(S44_NPZ, allow_pickle=True)
    n3 = int(s44["N_3"]); n1 = int(s44["N_1"])                               # (local)
    winding = int(s44["BDI_winding"]); eta = float(s44["eta_spectral"])      # (local)
    spatial_dim = int(s44["spatial_dimension"])                             # (local)
    n3_req = int(s44["N_3_required_dim"])                                    # (local)
    full_bdi_trivial = (n3 == 0 and n1 == 0 and winding == 0 and eta == 0.0)  # (local)
    dim_count_robust = (spatial_dim < n3_req)                               # (local)

    # The S-1 §IV.D annotation-text source SHA (the patch text we transcribe). We pin the
    # SHA of the verbatim §IV.D item-(1) blockquote line in the synthesis (line 91) as the
    # annotation-text provenance for the audit pinmap.
    s1_text = s1_bytes.decode("utf-8")
    IVD_ITEM1_ANCHOR = "**SCOPE ANNOTATION — clause (b) single-cutoff COUNT (authoritative grade for downstream consumers).**"
    i_ivd = s1_text.find(IVD_ITEM1_ANCHOR)
    if i_ivd < 0:
        raise RuntimeError("S-1 §IV.D item-(1) SCOPE ANNOTATION anchor not found")
    ivd_end = s1_text.find("\n", i_ivd)
    if ivd_end < 0:
        ivd_end = len(s1_text)
    s1_ivd_annotation_text = s1_text[i_ivd:ivd_end]
    s1_ivd_annotation_text_sha = sha256_text(s1_ivd_annotation_text)        # (local)

    # ------------------------------------------------ frozen-span PRE (immutability)
    frozen_pre = extract_frozen_span(pre_text)
    frozen_pre_sha = sha256_text(frozen_pre)                                # (local)
    frozen_pre_len = len(frozen_pre)                                        # (local)
    if frozen_pre_len != FROZEN_SPAN_LEN:
        raise RuntimeError(f"PRE frozen span len {frozen_pre_len} != pin {FROZEN_SPAN_LEN}")
    if frozen_pre_sha != FROZEN_SPAN_SHA_PIN:
        # HARD breakage: the frozen Stage-0 text on disk no longer matches the pin BEFORE
        # we even edit — script-health failure (exit != 0), NOT a verdict.
        raise RuntimeError(
            f"PRE frozen span SHA {frozen_pre_sha} != pin {FROZEN_SPAN_SHA_PIN} "
            "(frozen Stage-0 text drifted before annotation)"
        )

    # SHA log (first 20 lines of stdout per gate-verdicts.md)
    print("=== INPUT SHA LOG (s103_viibs_clause_b_scope_annotation) ===")
    print(f"registry_pre_file_sha256       = {pre_registry_file_sha}")
    print(f"s1_synthesis_file_sha256       = {s1_synth_file_sha}")
    print(f"s1_ivd_annotation_text_sha256  = {s1_ivd_annotation_text_sha}")
    print(f"canonical_constants_runtime_sha= {cc_runtime_sha}")
    print(f"s44_npz: N3={n3} N1={n1} winding={winding} eta={eta} "
          f"spatial_dim={spatial_dim} N3_req={n3_req}")
    print(f"FULL_BDI_TRIVIAL               = {full_bdi_trivial}")
    print(f"dim_count_robust(spatial<req)  = {dim_count_robust}")
    print(f"frozen_span_len                = {frozen_pre_len} (pin {FROZEN_SPAN_LEN})")
    print(f"frozen_span_sha256             = {frozen_pre_sha}")
    print(f"frozen_span_matches_pin        = {frozen_pre_sha == FROZEN_SPAN_SHA_PIN}")

    # Idempotency: detect already-annotated state. If the HEADER_NEW surface is already
    # present (and HEADER_OLD absent), the registry was annotated by a prior run of THIS
    # gate (e.g. a re-run after a script-compliance fix). SKIP the write (NO-OP), verify
    # against the on-disk state. (Pattern: verbatim-extraction memory lesson #4 idempotency
    # + #5 script-bug-fix re-run; the emitted SHAs are the post-fix script bytes.)
    already_annotated = (HEADER_NEW in pre_text) and (HEADER_OLD not in pre_text)  # (local)

    # Plan-text-drift disclosure (substrate-first-canonical-sourcing.md §(ii.B)):
    # the plan cites §VII.BS at :21375-21388; on-disk the header is at a drifted line
    # (registry gained rows this session). We anchor by literal substring, so line drift
    # does NOT affect correctness; disclose it. (Anchor on whichever header form is present.)
    hdr_probe = HEADER_OLD if (HEADER_OLD in pre_text) else HEADER_NEW       # (local)
    header_line_no = pre_text[: pre_text.find(hdr_probe)].count("\n") + 1    # (local)
    plan_cited_line = 21375                                                  # (local)
    line_drift = header_line_no - plan_cited_line                            # (local)
    print(f"already_annotated              = {already_annotated}")
    print(f"header_on_disk_line            = {header_line_no} "
          f"(plan cited :{plan_cited_line}; drift={line_drift:+d}, anchored-by-substring)")

    # ----------------------------------------------------------- build + write (or NO-OP)
    if already_annotated:
        # NO-OP: registry already carries the annotation; do not re-edit.
        post_registry_file_sha = pre_registry_file_sha                      # (local)
        print("WRITE                          = SKIPPED (idempotent NO-OP; already annotated)")
    else:
        post_text = build_annotation_text(pre_text)
        write_atomic_with_fsync(REGISTRY, post_text)
        print("WRITE                          = APPLIED (annotation surfaces written + fsync)")

    # --------------------------------------------------- re-read + verify (from disk)
    rr_bytes = REGISTRY.read_bytes()
    rr_text = rr_bytes.decode("utf-8")
    post_registry_file_sha = sha256_bytes(rr_bytes)                         # (local)

    # (a) frozen-span immutability (HARD)
    frozen_post = extract_frozen_span(rr_text)
    frozen_post_sha = sha256_text(frozen_post)                              # (local)
    frozen_unchanged = (frozen_post_sha == FROZEN_SPAN_SHA_PIN) and (frozen_post == frozen_pre)

    # (b) the 4 surfaces present (RE-READ from disk)
    surf_header = (HEADER_NEW in rr_text)                                   # (local)
    surf_index = (INDEX_NEW in rr_text)                                     # (local)
    surf_clauseb = (CLAUSEB_NEW in rr_text)                                 # (local)
    surf_block = ("SCOPE ANNOTATION — clause (b) single-cutoff COUNT (authoritative grade for downstream" in rr_text)  # (local)
    four_surfaces = surf_header and surf_index and surf_clauseb and surf_block

    # (c) FULL-BDI-triviality second finding present in the annotation block
    full_bdi_finding_present = ("FULL BDI topological triviality `N₃ = N₁ = BDI_winding = η_spectral = 0`" in rr_text)  # (local)

    # (d) theorem grade STAGE-3-PERMANENT unchanged (the grade markers still present;
    #     and no down-tag introduced — count of the bold grade marker preserved or higher).
    grade_marker = "**STAGE-3-PERMANENT**"
    grade_pre_count = pre_text.count(grade_marker)                          # (local)
    grade_post_count = rr_text.count(grade_marker)                          # (local)
    grade_unchanged = (grade_post_count >= grade_pre_count) and (grade_post_count >= 1)

    # (e) narrowed-wording markers (the WP/registry must_contain set)
    has_open_q6 = ("Open Q6" in rr_text) or ("Open Question 6" in rr_text)  # (local)
    has_count_confirmed = ("single-cutoff COUNT confirmed" in rr_text)      # (local)

    # (f) frozen blockquote occurrence count unchanged (immune block still present once)
    bq_count = rr_text.count(FROZEN_BLOCKQUOTE_ANCHOR)                      # (local)
    bq_count_ok = (bq_count == pre_text.count(FROZEN_BLOCKQUOTE_ANCHOR))    # (local)

    verify = bool(
        frozen_unchanged
        and four_surfaces
        and full_bdi_finding_present
        and grade_unchanged
        and has_open_q6
        and has_count_confirmed
        and bq_count_ok
    )

    verdict = "PASS" if verify else "FAIL"

    print("\n=== VERIFY (re-read from disk) ===")
    print(f"frozen_span_post_sha256        = {frozen_post_sha}")
    print(f"frozen_span_UNCHANGED          = {frozen_unchanged}  (== e669ccd2… HARD)")
    print(f"surface_header                 = {surf_header}")
    print(f"surface_index                  = {surf_index}")
    print(f"surface_clause_b_inline        = {surf_clauseb}")
    print(f"surface_scope_annotation_block = {surf_block}")
    print(f"four_surfaces                  = {four_surfaces}")
    print(f"full_bdi_triviality_finding    = {full_bdi_finding_present}")
    print(f"grade STAGE-3-PERMANENT count  = {grade_pre_count} -> {grade_post_count} "
          f"(unchanged={grade_unchanged})")
    print(f"has 'Open Q6'                  = {has_open_q6}")
    print(f"has 'single-cutoff COUNT confirmed' = {has_count_confirmed}")
    print(f"frozen blockquote count        = {bq_count} (ok={bq_count_ok})")
    print(f"VERIFY                         = {verify}")

    # ----------------------------------------------------------- npz output
    NPZ_OUT.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        NPZ_OUT,
        gate_id="S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION",
        verdict=verdict,
        verify=verify,
        # frozen-span immutability
        frozen_span_sha_pin=FROZEN_SPAN_SHA_PIN,
        frozen_span_pre_sha=frozen_pre_sha,
        frozen_span_post_sha=frozen_post_sha,
        frozen_span_len=frozen_pre_len,
        frozen_unchanged=frozen_unchanged,
        # 4-surface booleans
        surface_header=surf_header,
        surface_index=surf_index,
        surface_clause_b_inline=surf_clauseb,
        surface_scope_annotation_block=surf_block,
        four_surfaces=four_surfaces,
        # second finding
        full_bdi_triviality_finding=full_bdi_finding_present,
        s44_N3=n3, s44_N1=n1, s44_BDI_winding=winding, s44_eta_spectral=eta,
        s44_spatial_dim=spatial_dim, s44_N3_required_dim=n3_req,
        full_bdi_trivial=full_bdi_trivial, dim_count_robust=dim_count_robust,
        # grade + narrowed-wording markers
        grade_pre_count=grade_pre_count, grade_post_count=grade_post_count,
        grade_unchanged=grade_unchanged,
        has_open_q6=has_open_q6, has_count_confirmed=has_count_confirmed,
        # registry file SHAs
        registry_pre_file_sha=pre_registry_file_sha,
        registry_post_file_sha=post_registry_file_sha,
        # source provenance
        s1_synthesis_file_sha=s1_synth_file_sha,
        s1_ivd_annotation_text_sha=s1_ivd_annotation_text_sha,
        canonical_constants_runtime_sha=cc_runtime_sha,
        # line-drift disclosure
        header_on_disk_line=header_line_no, plan_cited_line=plan_cited_line,
        line_drift=line_drift,
        # W2-1 cross-reference
        w2_1_gate="S103-NNU-BUNDLE-EXHAUSTIVENESS",
        w2_1_audit="ac1dbb2892cef172a6383f33652d110e53b7815316c4eefa1c0aa1360def3257",
    )

    # ----------------------------------------------------------- dual-SHA
    # content_sha256 inputs = [script]  (per plan audit_discriminators)
    script_sha = sha256_bytes(SCRIPT_PATH.read_bytes())                    # (local)
    content_sha256 = script_sha

    # audit_sha256 inputs (ordered) = [script, s1_ivd_annotation_text_sha,
    #   registry_pre_annotation_file_sha, frozen_blockquote_span_sha_assertion, pinmap]
    pinmap = {
        "gate_id": "S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION",
        "scheme": "CURATED-DOC-REVIEWED-DESIGNATED-WRITER-ANNOTATION",
        "convention": ("ANNOTATION-SURFACES-ONLY-FROZEN-BLOCKQUOTE-IMMUNE;"
                       "OUT-OF-FROZEN-BLOCK-AMENDMENT-PER-VIIBP-PRECEDENT;"
                       "THEOREM-GRADE-UNCHANGED-STAGE-3-PERMANENT"),
        "L_max": "N/A",
        "frozen_span_sha_assertion": FROZEN_SPAN_SHA_PIN,
        "s1_synthesis_file_sha": s1_synth_file_sha,
        "s44_npz_full_bdi": f"N3={n3};N1={n1};winding={winding};eta={eta}",
        "canonical_constants_runtime_sha": cc_runtime_sha,
        "verify": verify,
    }
    audit_inputs = (
        script_sha
        + "|" + s1_ivd_annotation_text_sha
        + "|" + pre_registry_file_sha
        + "|" + FROZEN_SPAN_SHA_PIN
        + "|" + json.dumps(pinmap, sort_keys=True, ensure_ascii=False)
    )
    audit_sha256 = sha256_text(audit_inputs)

    value = (
        f"verify={verify};frozen_span_UNCHANGED={frozen_unchanged}(==e669ccd2);"
        f"4surfaces={four_surfaces};full_BDI_triviality_finding={full_bdi_finding_present};"
        f"grade=STAGE-3-PERMANENT_unchanged;OpenQ6+single-cutoff-COUNT-confirmed;"
        f"line_drift={line_drift:+d}_anchored-by-substring"
    )

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    print(f"\n4-tuple: (value={value}, "
          f"scheme={pinmap['scheme']}, convention={pinmap['convention']}, L_max=N/A)")

    # ----------------------------------------------------------- verdict payload
    payload = {
        "session": 103,
        "gate_id": "S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION",
        "verdict": verdict,
        "value": value,
        "scheme": pinmap["scheme"],
        "convention": pinmap["convention"],
        "l_max": "N/A",
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "schema_version": "S84+",
        "companion_note": ("frozen Stage-0 blockquote span SHA e669ccd2…(len 2514) HARD-asserted "
                           "UNCHANGED; annotation surfaces ONLY; theorem grade STAGE-3-PERMANENT unchanged"),
        "extra_rows": [
            (f"# canonical_constants_runtime_sha={cc_runtime_sha} "
             f"# plan pinned <computed-at-runtime>; no drift-vs-pin (append-only extension disclosed per substrate-first §(ii.B))"),
            (f"# W2-1 cross-ref: S103-NNU-BUNDLE-EXHAUSTIVENESS PASS audit ac1dbb2892cef172… "
             f"rank(Cov_aug)=1 (Open Q6 bundle-exhaustiveness CONFIRMED for augmented bundle; "
             f"standing-premise->result upgrade is S104 follow-up)"),
        ],
    }

    print_verdict_payload(payload)

    # Exit 0 regardless of PASS/FAIL (verdict is data, not exit code).
    sys.exit(0)


if __name__ == "__main__":
    main()
