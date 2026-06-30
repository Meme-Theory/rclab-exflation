#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
S101 W6-6 — S101-SCHUR-RIGIDITY-STAGE1-REGISTRATION
====================================================

Single-shot bridge-landing (AFTER pattern, own script per PD-5) of the frozen
S-2 Stage-0 candidate text:

    "Band-Selective Schur Rigidity and the Symmetry-Undecidability of
     Abelian-vs-Non-Abelian Band Geometry on G-Invariant Deformation Families"

as a STAGE-1-CANDIDATE entry at the reserved registry slot **§VII.BR**
(`sessions/permanent-results-registry.md`), per `joint-theorem-promotion.md`
Stage-1. LAST letter-slot (6 of 7) in the S101 W6 single-writer registry chain.

DISCIPLINE (mirrors `.claude/rules/registry-landing.md §"Bridge-Landing Script
Architecture (single-shot pattern)"` + `computations/_bridge_landing_script_template.py`
+ the S101 W6-1..W6-5 precedents):

  build_promotion_text(...)   # PURE — no I/O before write; the verbatim span is
                              #        extracted byte-exact from the SHA-pinned
                              #        synthesis and wrapped with the MANDATORY
                              #        promotion-text wrapper (header, Stage-0
                              #        blockquote, authorship/Stage-2 routing,
                              #        forward-gate pointer, anatomy block).
  write_atomic_with_fsync(..) # binary-append, newline='\n', NO neighbor flatten
                              #        (the W6-3 lesson: a CRLF-preserving r/w
                              #        round-trip altered §VII.BM line endings;
                              #        binary-append in mode 'ab' touches ONLY the
                              #        added bytes — the 20 pre-existing CRLF lines
                              #        are NEVER re-encoded).
  re_read + verify_section_matches(...)   # ONE strict-equality boolean over the
                              #        re-read §VII.BR tail; the caveat-paragraph
                              #        grep (hit count == 1) runs on the RE-READ
                              #        section, not in-memory alone.
  emit ONCE                   # exactly one print_verdict_payload; the agent then
                              #        calls the race-safe emit_verdict MCP tool.

NO conditional corrective-rewrite branch exists (the BEFORE-pattern double-trio
is absent by construction). Idempotent: a re-run finds the §VII.BR section
byte-identical → NO-OP (no duplicate append, no neighbor flatten); audit_sha256 is
reproducible via the FROZEN run-1 registry PRE-SHA pinned in the input-pin map.

VERBATIM-EXTRACTION (binding-text rule; re-derive NOTHING). Two byte-pinned spans
are extracted from the SHA-pinned synthesis (`session-100b-berry-geometric-phase-
synthesis.md` §II.2, file SHA d2506ad5...):
  span_2 = "#### Candidate statement (frozen text for Stage-1 registration at S101)"
           through the end of the "Clause attribution (Stage-0 form)." paragraph
           (Title; Setting/definitions E1-E2; Hypotheses H1-H6 + realizations;
            Lemma L0 (E3)+proof; Theorem T1 (E4)+derivation; Theorem T2 (E5)+
            derivation + commutant remark; sub-lemma P (E6)+proof; Corollary U+
            derivation; Release condition R; numerical-witness table LC-lineage-
            conditional incl. defect-excluded I_NA(B2)=2.591e-02 vs pair-channel
            floor 2.602e-24 [22 OOM]; the MANDATORY Lineage caveat verbatim;
            the Clause attribution (a)-(g) paragraph).
  span_1 = the §II.2-head Stage-0-authorship blockquote ("Stage-0 authorship and
           Stage-2 exclusion (stated up front, per the S99 E1 lesson).") — the
           berry Stage-0-author exclusion INCLUDING successor berry spawns.
Each span is verified against a pinned SHA + length at runtime; a drift aborts
with sys.exit(4) (script breakage, exit != 0, NOT a verdict) BEFORE any disk write.

Audit-trail observation context: `computations/_bridge_landing_audit_trail_observation_S87_W5.md`.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import pathlib

# --- canonical-constants compliance import (math-scripts.md MANDATORY) ----------
_SHARED = pathlib.Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403  (compliance import)

# ------------------------------------------------------------------------------
# Pins (static; plan input_files: block + the lockfile RESERVED-FOR)
# ------------------------------------------------------------------------------
ROOT = pathlib.Path(__file__).resolve().parents[2]

GATE_ID = "S101-SCHUR-RIGIDITY-STAGE1-REGISTRATION"
SLOT = "§VII.BR"
SCHEME = "STAGE1-REGISTRATION-AFTER-PATTERN"
CONVENTION = "SINGLE-SHOT-VERBATIM-EXTRACTION"
SERIALIZATION_ORDER = "6 of 7 in the W6 single-writer registry chain"

SYNTH = ROOT / "sessions/session-100b/session-100b-berry-geometric-phase-synthesis.md"
SYNTH_SHA_PIN = "d2506ad5d88bb25394a2d8acebfcf65405f1fe6e80cc7a951e108985ff0c3551"

CLOSEOUT = ROOT / "sessions/session-100b/session-100b-campaign-closeout-synthesis.md"
CLOSEOUT_SHA_PIN = "8d3c8876b56aec6a52744d3564a017bfa01456db91817f6343a72e46b006b429"

BRIDGE_TMPL = ROOT / "computations/_bridge_landing_script_template.py"
BRIDGE_TMPL_SHA_PIN = "876c018fafea84742d06934a2061eb765ef41a042cb87ba0f4138caffbe9a68c"

LOCKFILE = ROOT / "sessions/framework/s101-slot-pre-allocation-lockfile.md"
LOCKFILE_RESERVED_FOR = "RESERVED-FOR-S101-W6-6-SCHUR-RIGIDITY"

REGISTRY = ROOT / "sessions/permanent-results-registry.md"
# FROZEN run-1 registry PRE state = the W6-5 POST state (§VII.BQ landed). Pinned so
# the audit_sha256 is REPRODUCIBLE across idempotent re-runs (binding-text rule).
REGISTRY_PRE_SHA_FROZEN = "88043156078854d7e964ebacb4f22774ce5fc2bd303968f859a00223c9d60008"

CANON = _SHARED / "canonical_constants.py"

# Byte-pinned extraction spans (computed at plan-prep; HARD-asserted at runtime).
SPAN1_ANCHOR = "> **Stage-0 authorship and Stage-2 exclusion (stated up front, per the S99 E1 lesson).**"
SPAN1_SHA_PIN = "dcfba371fe0fee2721041896deaef3c750837c77d1be2100b80fc5bad3c0648a"
SPAN1_LEN_PIN = 904  # (local) — byte-extraction length pin (Stage-0 blockquote span)

SPAN2_ANCHOR = "#### Candidate statement (frozen text for Stage-1 registration at S101)"
SPAN2_CLAUSE = "**Clause attribution (Stage-0 form).**"
SPAN2_NEXT = "### II.3 Corrected interpretive scope"
SPAN2_SHA_PIN = "a61ae8079958d2a5bfb4284b12283efabf6dcd8d0d737996c58c1c3c3924670a"
SPAN2_LEN_PIN = 14542  # (local) — byte-extraction length pin (candidate-statement span)

CAVEAT_GREP_MARKER = "Lineage caveat (MANDATORY; carried verbatim into any Stage-1 registration)"

# Defect-excluded structural-witness pair (RECORDED; transcribed, never re-derived)
I_NA_B2 = "2.591e-02"
PAIR_FLOOR = "2.602e-24"

W6_2_AUDIT = "4a03497c43a97335"  # S100b W6-2 witness-table audit (short, per the synthesis table header)


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: pathlib.Path) -> str:
    return sha256_bytes(p.read_bytes())


def closure_hash(pin_map: dict) -> str:
    """audit_sha256 = sha256 over the canonical-JSON of the ordered input-pin map."""
    return sha256_bytes(json.dumps(pin_map, sort_keys=True, ensure_ascii=False).encode("utf-8"))


# ------------------------------------------------------------------------------
# Verbatim span extraction (byte-exact; drift -> sys.exit(4) BEFORE any write)
# ------------------------------------------------------------------------------
def extract_spans():
    synth_sha = sha256_file(SYNTH)
    if synth_sha != SYNTH_SHA_PIN:
        print(f"FATAL: synthesis SHA drift {synth_sha} != pin {SYNTH_SHA_PIN}", file=sys.stderr)
        sys.exit(4)
    text = SYNTH.read_text(encoding="utf-8")

    # span_1: the §II.2-head Stage-0 blockquote (one blockquote line), ending
    # '...only the exclusion.' immediately before the '\n\n---' separator.
    i_a1 = text.find(SPAN1_ANCHOR)
    if i_a1 < 0:
        print("FATAL: span_1 anchor not found", file=sys.stderr)
        sys.exit(4)
    sep1 = text.find("\n\n---", i_a1)
    span1 = text[i_a1:sep1]

    # span_2: '#### Candidate statement ...' through end of the
    # 'Clause attribution (Stage-0 form).' paragraph (the blank line before II.3).
    i_a2 = text.find(SPAN2_ANCHOR)
    i_clause = text.find(SPAN2_CLAUSE)
    i_next = text.find(SPAN2_NEXT)
    if min(i_a2, i_clause, i_next) < 0:
        print("FATAL: span_2 anchors not all found", file=sys.stderr)
        sys.exit(4)
    end2 = text.rfind("\n\n", i_clause, i_next)
    span2 = text[i_a2:end2]

    # HARD-assert length + SHA on both spans (zero transcription drift).
    for name, span, sha_pin, len_pin in (
        ("span_1", span1, SPAN1_SHA_PIN, SPAN1_LEN_PIN),
        ("span_2", span2, SPAN2_SHA_PIN, SPAN2_LEN_PIN),
    ):
        got_len = len(span)
        got_sha = sha256_bytes(span.encode("utf-8"))
        if got_len != len_pin or got_sha != sha_pin:
            print(
                f"FATAL: {name} drift len {got_len}!={len_pin} or sha {got_sha}!={sha_pin}",
                file=sys.stderr,
            )
            sys.exit(4)

    # span_2 must carry every structural marker (defensive; re-grep on extracted text).
    required = [
        "**Title**", r"\tag{E1}", r"\tag{E2}", "(H1)", "(H6)",
        "Lemma L0", r"\tag{E3}", "Theorem part T1", r"\tag{E4}",
        "Theorem part T2", r"\tag{E5}", "Commutant remark (rigor honesty)",
        "Sub-lemma P", r"\tag{E6}", "Corollary U",
        "Release condition R", "Numerical witnesses",
        CAVEAT_GREP_MARKER, "Clause attribution (Stage-0 form)",
        I_NA_B2, PAIR_FLOOR,
    ]
    missing = [m for m in required if m not in span2]
    if missing:
        print(f"FATAL: span_2 missing structural markers: {missing}", file=sys.stderr)
        sys.exit(4)

    return span1, span2


# ------------------------------------------------------------------------------
# build_promotion_text — PURE (no I/O); the §VII.BR entry, fully in memory
# ------------------------------------------------------------------------------
def build_promotion_text(span1: str, span2: str) -> str:
    header = (
        "§VII.BR — Band-Selective Schur Rigidity and the Symmetry-Undecidability "
        "of Abelian-vs-Non-Abelian Band Geometry on G-Invariant Deformation Families "
        "(STAGE-1-CANDIDATE per joint-theorem-promotion.md; S100b S-2 berry synthesis "
        "§II.2 frozen Stage-0 text, transcribed VERBATIM; S101 W6-6 landing — "
        "gen-physicist; Stage-0 author berry-geometric-phase-theorist EXCLUDED from "
        "Stage-2 INCLUDING successor berry spawns)"
    )

    authorship = (
        "**AUTHORSHIP + STAGE-2 ROUTING (binding).** `berry-geometric-phase-theorist` "
        "is the Stage-0 author of this candidate and is therefore EXCLUDED from any "
        "Stage-2 cross-review — INCLUDING future berry spawns whose agent memory "
        "(`s100b-band-selective-rigidity.md`) inherits this reading path and fires the "
        "downstream-inheritance test (`joint-theorem-promotion.md §\"Stage-2 Axis-B "
        "Selection Protocol\"` condition 2; S99 E1 Stage-0-authorship hardening). "
        "Stage-2 gate = **S101-SCHUR-RIGIDITY-STAGE2-VERIFY** (S102, Wave-7 gate 2): "
        "Axis-A re-derives L0/T1/T2/P/U from THIS registered text alone; Axis-B "
        "re-checks the witness table from the `s100b_nonabelian_metric_fraction.py` "
        "npz WITHOUT consuming the S-2 synthesis. The Axis-B Selection Protocol "
        "(axis-distinctness + original-author exclusion with downstream-inheritance "
        "reach + audit-coverage adequacy) AND `joint-theorem-promotion.md` audit item 6 "
        "(no reviewer may be sole author of the verdict-layer machinery they apply) "
        "BOTH apply."
    )

    fwd_gate = (
        "**FORWARD-GATE POINTER (cited, NOT a clause of this entry).** Release "
        "condition R's discriminator gate is **S101-B2-ISOTROPY-BREAKING** (Wave-5 "
        "gate 4; dual-prior pre-registered there): isotropy-breaking deformations "
        "along the C² coset directions λ₄..λ₇ are both the release condition of the "
        "no-go and the discriminator the no-go licenses. R is registered here as a "
        "regime-of-validity clause; the affirmative non-Abelian question transfers, "
        "whole, to that forward gate."
    )

    anatomy = (
        "**REGISTRY-ANATOMY COMPLIANCE.** "
        "(i) Entry class = **intra-pillar structural-theorem complex** (single-axis "
        "GEOMETRIC with cited cross-axis PROVEN inputs per the clause attribution: "
        "S22b block-diagonality for the (H1) fiber realization; the S25 "
        "reality-mechanism class for (H6)). This is **NOT a cross-pillar bridge**, so "
        "the 5-anatomy IS-not-IN elements + the 3-level ladder are declared "
        "**N/A-with-reason**: there is no laboratory-IN observable and no "
        "HKR / K-theory / Connes-Karoubi bridge map is claimed (a Schur-rigidity no-go "
        "intrinsic to the spectral triple `(A_K, H_K, D_K)`); the \"Level-3 < Level-2\" "
        "registry-PASS inequality is vacuously N/A (no continuum-image envelope). The "
        "clause-attribution routing note is carried verbatim: this landing takes the "
        "**standard structural-theorem route** (a joint-theorem route would apply only "
        "if an NCG-side co-author independently lands the (H1)/(H2) spectral-triple "
        "realization clauses); Stage-2 independent verification applies under BOTH "
        "routes with the berry exclusion stated above. "
        "(ii) Projection-side = **SINGLE-READING, operator/projector-side**: the "
        "theorem complex quantifies over G-invariant FUNCTIONALS of the spectral-"
        "projector families P(b) (Corollary U is precisely a statement about that "
        "functional class); no state-pair functional clause exists in the candidate, so "
        "the bare slot `§VII.BR` (no `.OP-PROJ`/`.STATE-PROJ` suffix) is admissible "
        "under `registry-landing.md` Reading-A naming hygiene PRECISELY because this "
        "explicit single-reading sentence is carried. "
        "(iii) No state-history labels in the candidate text (Class-(h) parse-tree "
        "N/A; \"Bogoliubov\" does not appear). "
        "(iv) Substrate-IS level tag = **Level 2** (moduli-deformation per "
        "`phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS "
        "levels\"`): the base B is the substrate's OWN (τ, μ) deformation manifold on "
        "the U(2)-invariant volume-preserving TT surface — not a coordinate container."
    )

    provenance = (
        "**Provenance.** Binding source = `sessions/session-100b/"
        "session-100b-berry-geometric-phase-synthesis.md` §II.2 (file SHA "
        f"`{SYNTH_SHA_PIN}`), the frozen Stage-0 candidate text, transcribed VERBATIM "
        f"(span_2 SHA `{SPAN2_SHA_PIN}`, {SPAN2_LEN_PIN} chars; Stage-0-authorship "
        f"blockquote span_1 SHA `{SPAN1_SHA_PIN}`, {SPAN1_LEN_PIN} chars). Numerical "
        f"witnesses originate at S100b W6-2 (audit `{W6_2_AUDIT}…`) and are "
        "LC-lineage-conditional per the MANDATORY caveat carried in the span. "
        "Lockfile reservation: `s101-slot-pre-allocation-lockfile.md` "
        f"`{LOCKFILE_RESERVED_FOR}` (§VII.BR, last of the BM–BR block). "
        "Closure SHA pin = the W6-6 verdict-line audit_sha256."
    )

    # Assemble. The two verbatim spans are reproduced byte-for-byte; only the
    # wrapper paragraphs above are authored (per the plan's MANDATORY promotion-text
    # wrapper (a)/(c)/(d)/(e)). span_1 (the Stage-0 blockquote) is placed first per
    # the plan (PLUS the head blockquote), then the candidate statement span_2.
    parts = [
        "### " + header,
        "",
        span1,
        "",
        authorship,
        "",
        fwd_gate,
        "",
        span2,
        "",
        anatomy,
        "",
        provenance,
        "",
    ]
    body = "\n".join(parts)
    # Prepend a clean separator so the entry docks after §VII.BQ with one blank line.
    return "\n" + body


# ------------------------------------------------------------------------------
# write_atomic_with_fsync — binary-append, newline='\n', NO neighbor flatten
# ------------------------------------------------------------------------------
def write_atomic_with_fsync(append_text: str, path: pathlib.Path) -> None:
    data = append_text.encode("utf-8")  # LF terminators already in the string
    with open(path, "ab") as fh:        # APPEND BINARY — touches ONLY added bytes
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())


def re_read_section(path: pathlib.Path) -> str:
    """Return the on-disk §VII.BR block tail (from the §VII.BR header to EOF)."""
    text = path.read_text(encoding="utf-8")
    i = text.rfind("### §VII.BR ")
    if i < 0:
        return ""
    return text[i:]


def verify_section_matches(actual_tail: str, expected_append: str) -> bool:
    """Strict equality: the re-read §VII.BR tail equals the appended block stripped
    of its leading separator newline(s)."""
    expected_section = expected_append.lstrip("\n")
    return actual_tail.rstrip("\n") == expected_section.rstrip("\n")


def slot_free_on_disk(path: pathlib.Path) -> tuple:
    """PD-2: all-header-level (## / ### / ####) scan for §VII.BR occupancy."""
    import re
    text = path.read_text(encoding="utf-8")
    hdr = re.findall(r"^#{2,4}\s*§VII\.BR\b", text, re.M)
    any_br = text.count("§VII.BR")
    return (len(hdr) == 0 and any_br == 0), len(hdr), any_br


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          scheme, convention, l_max="N/A",
                          schema_version="S84+", extra_rows=None):
    payload = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": scheme,
        "convention": convention,
        "L_max": l_max,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": schema_version,
        "session": "101",
    }
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, ensure_ascii=False))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------
def main():
    # 0) Static input SHA cross-check (runtime vs plan pin); log in first lines.
    synth_sha = sha256_file(SYNTH)
    closeout_sha = sha256_file(CLOSEOUT)
    bridge_sha = sha256_file(BRIDGE_TMPL)
    lockfile_sha = sha256_file(LOCKFILE)
    canon_sha = sha256_file(CANON)
    print(f"[input-SHA] synthesis    = {synth_sha} (pin {SYNTH_SHA_PIN})")
    print(f"[input-SHA] closeout     = {closeout_sha} (pin {CLOSEOUT_SHA_PIN})")
    print(f"[input-SHA] bridge_tmpl  = {bridge_sha} (pin {BRIDGE_TMPL_SHA_PIN})")
    print(f"[input-SHA] lockfile     = {lockfile_sha}")
    print(f"[input-SHA] canonical    = {canon_sha}")
    assert synth_sha == SYNTH_SHA_PIN, "synthesis SHA drift"
    assert closeout_sha == CLOSEOUT_SHA_PIN, "closeout SHA drift"
    assert bridge_sha == BRIDGE_TMPL_SHA_PIN, "bridge-template SHA drift"
    assert LOCKFILE_RESERVED_FOR in LOCKFILE.read_text(encoding="utf-8"), "lockfile RESERVED-FOR missing"

    # 1) Extract the two byte-pinned verbatim spans (drift -> exit 4 before any write).
    span1, span2 = extract_spans()
    print(f"[extract] span_1 len={len(span1)} sha={sha256_bytes(span1.encode())[:16]}…")
    print(f"[extract] span_2 len={len(span2)} sha={sha256_bytes(span2.encode())[:16]}…")

    # 2) build_promotion_text — PURE (no I/O before write).
    promotion = build_promotion_text(span1, span2)

    # 3) Registry PRE-state. Idempotency: if §VII.BR already landed byte-identical
    #    (own prior run), SKIP append; if a FOREIGN occupant, PD-3 reroute+FAIL.
    registry_pre_sha = sha256_file(REGISTRY)
    free, hdr_count, any_count = slot_free_on_disk(REGISTRY)
    expected_section = promotion.lstrip("\n").rstrip("\n")

    rerouted = False
    if not free:
        existing_tail = re_read_section(REGISTRY)
        if existing_tail and existing_tail.rstrip("\n") == expected_section:
            # (A) idempotent own re-run — keep slot, SKIP append.
            print("[idempotent] §VII.BR already landed byte-identical; SKIP append.")
            actual_tail = existing_tail
        else:
            # (B) FOREIGN collision — PD-3 reroute + FAIL-with-remediation.
            rerouted = True
            value = (
                f"FAIL_slot_reroute_§VII.BR_occupied_by_FOREIGN_hdr={hdr_count}_any={any_count}"
                "_remediation=next-free-letter_BS-BW_per_epistemic-discipline_RegistryWriteHygiene_item3"
            )
            audit_pins = _audit_pin_map(registry_pre_sha, "FAIL", rerouted, "")
            audit_sha = closure_hash(audit_pins)
            content_sha = sha256_bytes(b"")
            _emit_and_record(
                "FAIL", value, audit_sha, content_sha, registry_pre_sha,
                registry_pre_sha, rerouted, False, 0, span1, span2,
            )
            print("VERDICT: FAIL (slot reroute — foreign occupant)")
            sys.exit(0)
    else:
        # 4) write_atomic_with_fsync — binary-append, NO neighbor flatten.
        write_atomic_with_fsync(promotion, REGISTRY)
        actual_tail = re_read_section(REGISTRY)

    # 5) re_read + verify_section_matches — single point of decision.
    section_match = verify_section_matches(actual_tail, promotion)

    # 5b) caveat-paragraph grep on the RE-READ section (hit count == 1).
    caveat_count = actual_tail.count(CAVEAT_GREP_MARKER)
    caveat_ok = caveat_count == 1

    # 5c) STAGE-1-CANDIDATE present on the re-read section.
    stage1_present = "STAGE-1-CANDIDATE" in actual_tail

    registry_post_sha = sha256_file(REGISTRY)
    content_sha = sha256_bytes(actual_tail.rstrip("\n").encode("utf-8"))

    verdict = "PASS" if (section_match and caveat_ok and stage1_present) else "FAIL"

    value = (
        f"landed_VII.BR_SCHUR-RIGIDITY-STAGE-1-CANDIDATE_section_byte_match_{section_match}"
        f"_caveat_grep_count={caveat_count}_STAGE-1-CANDIDATE_present_{stage1_present}"
        f"_span2_verbatim_SHA_{SPAN2_SHA_PIN[:16]}_span1_stage0_excl_SHA_{SPAN1_SHA_PIN[:16]}"
        f"_L0+T1+T2+commutant+P+U+R_every-step_carried_I_NA(B2)={I_NA_B2}_vs_pair_floor_{PAIR_FLOOR}_22OOM"
        f"_LC-lineage-conditional_NUMBERS_operator-independent_L0/T1/T2/P/U/R_BOTH-tau0-branches"
        f"_berry_Stage-0_EXCLUDED_incl_successor_spawns_Stage-2=S101-SCHUR-RIGIDITY-STAGE2-VERIFY_W7-2"
        f"_AxisB-Protocol+audit_item6_fwd_gate=S101-B2-ISOTROPY-BREAKING_W5-4_CITED-not-clause"
        f"_5anatomy_NA_with_reason_standard-structural-theorem-route_SINGLE-READING_operator/projector-side"
        f"_level2_moduli-deformation_U(2)-TT(tau,mu)-surface_rerouted_{rerouted}"
    )

    audit_pins = _audit_pin_map(registry_pre_sha, verdict, rerouted, content_sha)
    audit_sha = closure_hash(audit_pins)

    _emit_and_record(
        verdict, value, audit_sha, content_sha, registry_pre_sha,
        registry_post_sha, rerouted, section_match, caveat_count, span1, span2,
    )

    print(f"VERDICT: {verdict}")
    print(f"  section_match={section_match}  caveat_count={caveat_count}  stage1_present={stage1_present}")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")
    sys.exit(0)


def _audit_pin_map(registry_pre_sha, verdict, rerouted, content_sha):
    """Ordered input-pin map -> audit_sha256. Frozen run-1 PRE for reproducibility."""
    return {
        "gate_id": GATE_ID,
        "slot": SLOT,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "serialization_order": SERIALIZATION_ORDER,
        "lockfile_reserved_for": LOCKFILE_RESERVED_FOR,
        "lockfile_sha": sha256_file(LOCKFILE),
        "synthesis_sha": SYNTH_SHA_PIN,
        "closeout_sha": CLOSEOUT_SHA_PIN,
        "bridge_template_sha": BRIDGE_TMPL_SHA_PIN,
        "canonical_constants_sha": sha256_file(CANON),
        "span1_sha": SPAN1_SHA_PIN,
        "span1_len": SPAN1_LEN_PIN,
        "span2_sha": SPAN2_SHA_PIN,
        "span2_len": SPAN2_LEN_PIN,
        "caveat_grep_marker": CAVEAT_GREP_MARKER,
        "registry_pre_sha_frozen": REGISTRY_PRE_SHA_FROZEN,
        "registry_pre_sha_runtime": registry_pre_sha,
        "stage2_gate": "S101-SCHUR-RIGIDITY-STAGE2-VERIFY (S102 W7-2; berry+successors EXCLUDED)",
        "forward_gate": "S101-B2-ISOTROPY-BREAKING (W5-4; cited, not a clause)",
        "verdict": verdict,
        "rerouted": rerouted,
        "content_sha256": content_sha,
    }


def _emit_and_record(verdict, value, audit_sha, content_sha, pre_sha, post_sha,
                     rerouted, section_match, caveat_count, span1, span2):
    # Landing-record npz.
    try:
        import numpy as np
        out = pathlib.Path(__file__).with_suffix("").as_posix() + ".npz"
        np.savez(
            out,
            gate_id=GATE_ID,
            slot=SLOT,
            verdict=verdict,
            value=value,
            audit_sha256=audit_sha,
            content_sha256=content_sha,
            registry_pre_sha=pre_sha,
            registry_post_sha=post_sha,
            registry_pre_sha_frozen=REGISTRY_PRE_SHA_FROZEN,
            rerouted=bool(rerouted),
            section_byte_match=bool(section_match),
            caveat_grep_count=int(caveat_count),
            span1_sha=SPAN1_SHA_PIN,
            span1_len=SPAN1_LEN_PIN,
            span2_sha=SPAN2_SHA_PIN,
            span2_len=SPAN2_LEN_PIN,
            i_na_b2=I_NA_B2,
            pair_floor=PAIR_FLOOR,
            synthesis_sha=SYNTH_SHA_PIN,
            lockfile_reserved_for=LOCKFILE_RESERVED_FOR,
            stage2_gate="S101-SCHUR-RIGIDITY-STAGE2-VERIFY",
            stage2_excludes="berry-geometric-phase-theorist+successor-spawns",
            forward_gate="S101-B2-ISOTROPY-BREAKING",
            level_tag="Level-2-moduli-deformation",
            single_reading="operator/projector-side",
        )
        print(f"[npz] wrote {out}")
    except Exception as exc:  # npz is a record, not the gate predicate
        print(f"[npz] WARNING: could not write npz: {exc}", file=sys.stderr)

    # PRINT the verdict payload (the agent then calls emit_verdict — race-safe MCP).
    extra = [
        f"# regulator_pin=N/A (Schur-rigidity no-go; no Seeley-DeWitt a_n citation in entry) "
        f"# caveat_grep_count={caveat_count} span2_sha={SPAN2_SHA_PIN[:16]} stage2_excludes=berry+successors",
    ]
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        SCHEME, CONVENTION, l_max="N/A", schema_version="S84+", extra_rows=extra,
    )


if __name__ == "__main__":
    main()
