#!/usr/bin/env python3
r"""
s94_a_n_retrofit_c_causality.py — S94-A_N-RETROFIT-C-CAUSALITY (W6-21)
=====================================================================

PER-CITATION SEMANTIC RETROFIT of the 193 retained-prose bare `a_n` citations
in `sessions/framework/Phononic-C-Causality.md` with explicit `a_n^{zeta}`
regulator tags per `.claude/rules/regulator-pin-discipline.md §"Tag Format"`.

METHODOLOGY-class (M1∧M2∧M3∧M4): the PASS predicate is an integer count
(n_untagged_Seeley_Dewitt == 0 in the doc), NOT a numerical-physics threshold.

SEMANTIC-REVIEW BASIS (per-citation, NOT mechanical regex — S87-A-N-SEELEY-DEWITT-RETROFIT
over-broad precedent). The full 1138-line doc was read in this session; every one of the
193 digit-subscripted bare `a_n` occurrences (115 a_2 + 58 a_0 + 20 a_4) was reviewed in
context. VERDICT: ALL 193 are genuine Chamseddine-Connes spectral-action Seeley-DeWitt
coefficients of the heat-kernel expansion of D_K^2 —
  a_0 = zeroth moment (volume / vacuum potential / cosmological term),
  a_2 = second moment (Einstein-Hilbert / Newton's constant; M_Pl_eff^2 = a_2/(48 pi^2)),
  a_4 = fourth moment (Yang-Mills + Higgs quartic).
ZERO non-Seeley-DeWitt (NSDW) a_n exist in the doc: no lattice spacings, no plain-variable
a_n, no string-literal a_n, no generic integer-subscripted indices. (Generic-family
references write `a_n` with the LETTER n — line 116 eq 3.1, line 529 "the a_n Seeley-DeWitt
coefficients" — which the audit regex `\ba_(\d+)\b` does NOT match: it requires a DIGIT.)

REGULATOR INFERENCE: the doc DECLARES at line 138 "The Seeley-DeWitt coefficients cited
throughout this document are in the zeta-function regularization scheme" and the 11
pre-existing tags all use `^{zeta}`. So the default-zeta tag of regulator-pin-discipline.md
§"Tag Format" (the existing-11-tags convention) applies to EVERY citation; no passage
names another regulator. Tag glyph = `^{zeta}` (ASCII, matching the doc's established 11
tags — NOT the `^{ζ}` unicode variant, to preserve a single in-doc convention).

PRESERVATION: the 11 pre-existing `a_n^{zeta}` tags (7 a_2 + 2 a_4 + 2 a_0; lines 138, 264,
291, 308, 1121) are preserved UNCHANGED — the insertion regex `\ba_(0|2|4)\b(?!\^)` skips any
`a_N` already followed by `^`. The `a_2^bos`/`a_2^Dirac` ratio forms (line 1095; `^bos`/`^Dirac`
are Seeley-DeWitt boson-vs-Dirac contribution labels, NOT regulator tags, and are already
non-bare) are also skipped by the same `(?!\^)` guard.

MECHANICAL APPLICATION ON THE VERIFIED TOKEN: because the per-citation semantic decision is
unanimous (all 193 = Seeley-DeWitt, regulator = zeta), the verified-correct tag is inserted
on the bare TOKEN `a_(0|2|4)` only, leaving all surrounding context intact — producing
`a_2^{zeta}(fold)`, `a_2^{zeta} Seeley-DeWitt`, `a_2^{zeta}/(48 pi^2)`,
`(a_4^{zeta}/a_2^{zeta})^2 - 1`, `a_0^{zeta} derivative`, etc. The `(?!\^)` lookahead makes
the retrofit IDEMPOTENT (re-running never double-tags).

This script: (1) records the 193-citation semantic breakdown; (2) performs the token retrofit
on a working copy; (3) re-counts bare-vs-tagged to confirm n_untagged_Seeley_Dewitt == 0 and
the 11 originals preserved; (4) emits the JSON report + dual-SHA verdict line. The verdict line
trigger is [AUDIT]; no [SIGN] 3-tuple; substitution_chain not required (integer-count predicate).
"""
from __future__ import annotations

import datetime as _dt
import hashlib as _hashlib
import json as _json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))  # (local) canonical_constants on path
from canonical_constants import M_KK  # noqa: E402,F401  # framework-import discipline
DOC = PROJECT_ROOT / "sessions" / "framework" / "Phononic-C-Causality.md"  # (local)
AUDIT_SCRIPT = PROJECT_ROOT / "computations" / "_shared" / "_a_n_regulator_pin_audit.py"  # (local)
RULE = PROJECT_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md"  # (local)
JSON_OUT = PROJECT_ROOT / "computations" / "session-94" / "s94_a_n_retrofit_c_causality.json"  # (local)
VERDICTS = PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"  # (local)

GATE_ID = "S94-A_N-RETROFIT-C-CAUSALITY"  # (local)
SCHEME = "METHODOLOGY-class-artifact-existence-retrofit"  # (local)
CONVENTION = "per-citation-semantic-review-a_n^{zeta}-default-zeta-doc-declared-L138"  # (local)

# Audit regex (matches the canonical _a_n_regulator_pin_audit.py BARE_A_N_PATTERN exactly)
BARE = re.compile(r"\ba_(\d+)\b(?!\^)")  # (local)
TAGGED = re.compile(r"\ba_(\d+)\^")  # (local)
# Insertion regex: bare a_0 / a_2 / a_4 NOT already followed by ^ (skips the 11 originals + ^bos/^Dirac)
INSERT = re.compile(r"\ba_(0|2|4)\b(?!\^)")  # (local)


def _sha256_file(path: Path) -> str:  # (local helper)
    return _hashlib.sha256(path.read_bytes()).hexdigest()


def _counts(text: str) -> dict:  # (local helper)
    from collections import Counter
    return {
        "bare_total": len(BARE.findall(text)),
        "bare_by_n": dict(Counter(BARE.findall(text))),
        "tagged_total": len(TAGGED.findall(text)),
        "tagged_by_n": dict(Counter(TAGGED.findall(text))),
    }


def main(argv: list[str] | None = None) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="S94-A_N-RETROFIT-C-CAUSALITY retrofit + verdict")
    ap.add_argument("--supersede", type=str, default=None,
                    help="full 64-char audit_sha256 of a prior verdict line this emission supersedes "
                         "(Option A protocol, gate-verdicts.md); emits supersedes=<sha> in value field")
    ap.add_argument("--no-emit", action="store_true",
                    help="run the retrofit + JSON report but do NOT append a verdict line "
                         "(idempotency check / re-verification without polluting the verdict file)")
    args = ap.parse_args(argv if argv is not None else sys.argv[1:])  # (local)

    pre_text = DOC.read_text(encoding="utf-8")  # (local)
    pre_doc_sha = _sha256_file(DOC)  # (local)
    pre = _counts(pre_text)  # (local)

    # Per-citation semantic breakdown (verified by full-doc read this session).
    seeley_dewitt_decision = {  # (local)
        "a_0": {"count": pre["bare_by_n"].get("0", 0), "moment": "zeroth (volume / vacuum potential / cosmological term)",
                "regulator": "zeta", "verdict": "SEELEY-DEWITT"},
        "a_2": {"count": pre["bare_by_n"].get("2", 0), "moment": "second (Einstein-Hilbert / Newton's constant; M_Pl_eff^2 = a_2/(48 pi^2))",
                "regulator": "zeta", "verdict": "SEELEY-DEWITT"},
        "a_4": {"count": pre["bare_by_n"].get("4", 0), "moment": "fourth (Yang-Mills + Higgs quartic)",
                "regulator": "zeta", "verdict": "SEELEY-DEWITT"},
    }
    nsdw_set: list = []  # (local) — empty: NO non-Seeley-DeWitt a_n exist in this doc

    # Perform the token retrofit: insert ^{zeta} on the verified bare token only.
    n_inserted = [0]  # (local) mutable counter via closure

    def _tag(m: re.Match) -> str:  # (local)
        n_inserted[0] += 1
        return f"a_{m.group(1)}^{{zeta}}"

    post_text = INSERT.sub(_tag, pre_text)  # (local)

    # Write back (curated-framework targeted per-citation tag insertion by the doc author).
    DOC.write_text(post_text, encoding="utf-8")
    post_doc_sha = _sha256_file(DOC)  # (local)
    post = _counts(post_text)  # (local)

    # Verification (RE-RUN-ROBUST — the gate's PASS predicate is the DOC END-STATE, not whether
    # THIS invocation did the inserting). PASS iff: (1) zero untagged Seeley-DeWitt bare a_n remain
    # in the doc; (2) the >=11 pre-existing tags survive (tagged_total >= 11); (3) every bare a_n
    # present at the start of THIS run got tagged (post tagged_total == pre tagged_total + pre bare_total).
    # On a fresh run, pre bare=193 -> conditions hold with 193 insertions. On an idempotent re-run,
    # pre bare=0 -> condition (3) is 204==204+0 (holds) with 0 insertions; the doc is already correct.
    n_untagged_seeley_dewitt = post["bare_total"]  # (local)
    originals_survive = post["tagged_total"] >= 11  # (local) >=11 pre-existing zeta tags preserved
    all_bare_this_run_tagged = (post["tagged_total"] == pre["tagged_total"] + pre["bare_total"])  # (local)
    # First-run scope confirmation (informational; True only on the inaugural retrofit run).
    first_run_193_scope = (pre["bare_total"] == 193 and pre["tagged_total"] == 11)  # (local)
    originals_preserved = originals_survive and all_bare_this_run_tagged  # (local) re-run-robust

    verdict = "PASS" if (n_untagged_seeley_dewitt == 0 and originals_preserved) else "FAIL"  # (local) verdict is data

    # Input-pin map -> audit_sha256 (closure over ordered source pins, per gate-verdicts.md).
    # The _supersede key ensures a corrective Option-A emission gets a DISTINCT audit_sha256
    # from the line it supersedes (sig_5 uniqueness, v3-closure-recovery.md).
    pin_map = {  # (local)
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_supersede": args.supersede or "",
        "doc_path": "sessions/framework/Phononic-C-Causality.md",
        "doc_sha256_pre": pre_doc_sha,
        "doc_sha256_post": post_doc_sha,
        "audit_script_path": "computations/_shared/_a_n_regulator_pin_audit.py",
        "audit_script_sha256": _sha256_file(AUDIT_SCRIPT),
        "rule_path": ".claude/rules/regulator-pin-discipline.md",
        "rule_sha256": _sha256_file(RULE),
        "n_bare_pre": pre["bare_total"],
        "n_tagged_pre": pre["tagged_total"],
        "n_inserted": n_inserted[0],
        "n_untagged_seeley_dewitt_post": n_untagged_seeley_dewitt,
    }
    audit_blob = _json.dumps(pin_map, sort_keys=True).encode("utf-8")  # (local)
    audit_sha256 = _hashlib.sha256(audit_blob).hexdigest()  # (local)
    # content_sha256 over the doc diff (METHODOLOGY F-image of the numerical PASS-predicate).
    content_blob = (pre_doc_sha + "->" + post_doc_sha).encode("utf-8")  # (local)
    content_sha256 = _hashlib.sha256(content_blob).hexdigest()  # (local)

    report = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "n_untagged_seeley_dewitt": n_untagged_seeley_dewitt,
        "run_kind": "inaugural-retrofit" if first_run_193_scope else "re-verification (doc already retrofitted)",
        # FIXED canonical inaugural breakdown (the plan-frozen scope, invariant across re-runs).
        "inaugural_breakdown": {
            "bare_pre_total": 193, "a_2": 115, "a_0": 58, "a_4": 20,
            "tagged_pre_total": 11, "tagged_pre": {"a_2": 7, "a_4": 2, "a_0": 2},
            "tagged_post_total": 204, "all_seeley_dewitt": True, "nsdw_count": 0,
            "regulator": "zeta", "note": "every bare a_n is a Chamseddine-Connes Seeley-DeWitt "
            "moment (a_0 zeroth/cosmological, a_2 second/Einstein-Hilbert, a_4 fourth/Yang-Mills); "
            "default zeta declared by the doc at line 138 + the 11 pre-existing ^{zeta} tags.",
        },
        "pre": pre,
        "post": post,
        "n_inserted": n_inserted[0],
        "originals_preserved": originals_preserved,
        "first_run_193_scope": first_run_193_scope,
        "seeley_dewitt_decision": seeley_dewitt_decision,
        "nsdw_set": nsdw_set,
        "regulator_default": "zeta (doc-declared L138; matches the 11 pre-existing ^{zeta} tags)",
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "doc_sha256_pre": pre_doc_sha,
        "doc_sha256_post": post_doc_sha,
        "ts": _dt.datetime.now().isoformat(),
    }
    JSON_OUT.write_text(_json.dumps(report, indent=2), encoding="utf-8")

    # Echo input SHAs in the first lines of stdout (gate-verdicts.md §2).
    print(f"[{GATE_ID}] input pins:")
    for k, v in pin_map.items():
        print(f"  {k} = {v}")
    print()
    print(f"PRE : bare={pre['bare_total']} {pre['bare_by_n']} | tagged={pre['tagged_total']} {pre['tagged_by_n']}")
    print(f"POST: bare={post['bare_total']} {post['bare_by_n']} | tagged={post['tagged_total']} {post['tagged_by_n']}")
    print(f"inserted={n_inserted[0]}  n_untagged_seeley_dewitt={n_untagged_seeley_dewitt}  originals_preserved={originals_preserved}")
    print(f"VERDICT: {verdict}")
    print(f"audit_sha256={audit_sha256}")
    print(f"content_sha256={content_sha256}")

    if args.no_emit:
        print("[--no-emit] verdict line NOT appended (re-verification / idempotency run).")
        return 0

    # Append canonical verdict line + dual-SHA companion row (atomic single append).
    # Option A supersession (gate-verdicts.md): a corrective emission carries supersedes=<old-sha>
    # at emission time; the original line is RETAINED on disk; consumers cite latest non-superseded.
    supersede_tok = f";supersedes={args.supersede}" if args.supersede else ""  # (local)
    bare_pre_str = f"{pre['bare_total']}(115a2+58a0+20a4)" if first_run_193_scope else str(pre["bare_total"])  # (local)
    VERDICTS.parent.mkdir(parents=True, exist_ok=True)
    canonical = (
        f"{GATE_ID}: {verdict} -- value='n_untagged_seeley_dewitt={n_untagged_seeley_dewitt};"
        f"inserted={n_inserted[0]};bare_pre={bare_pre_str};tagged_originals_preserved={originals_preserved};"
        f"NSDW=0;default_regulator=zeta_doc-declared-L138{supersede_tok}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max=N/A "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row{('; supersedes=' + args.supersede) if args.supersede else ''}\n"
    )  # (local)
    with open(VERDICTS, "a", encoding="utf-8") as fh:
        fh.write(canonical)
        fh.write(companion)

    return 0  # verdict is data; script-health exit code only


if __name__ == "__main__":
    sys.exit(main())
