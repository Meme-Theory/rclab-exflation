#!/usr/bin/env python
"""
s101_w8b_methodology_verify.py — shared METHODOLOGY-class verify driver for the
three W8b orchestrator-direct rule-landing gates:

  --gate S101-HK-SELECTION-RULE-PREFLIGHT-RULE     (math-scripts.md §22 corpus)
  --gate S101-HK-SUFFIX-DISCIPLINE                 (regulator-pin-discipline.md §23 corpus)
  --gate S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION  (gate-verdicts.md §24 corpus)

METHODOLOGY-class M1 predicate (wave-classification.md §"Dispatch consequences"):
PASS iff the rule sub-section + corpus section carry all their must_contain markers
AND (W8b-3 only) the pre-registered composite-collapse pseudo-code block in
gate-verdicts.md is BYTE-UNCHANGED (additive-only diff; modifying it would be the
Class-3 violation the directive avoids).

Dual-SHA (wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"):
  content_sha256 = sha256( applied rule-section text || landed corpus-section text )
  audit_sha256   = closure_hash( input-pin map of source documents incl _gate_id )
Both are full 64-hex; audit is unique per gate (distinct _gate_id + source set).

The driver prints the verdict PAYLOAD (print_verdict_payload); the orchestrator
calls the knowledge-MCP emit_verdict tool (session 101). The script does NOT write
the verdict file.

Source-citation (DERIVATIVE OUTPUT): per-gate specs transcribe the output_artifacts
must_contain + input_files SHAs from session-101-plan-w8.md §W8b-1 (:796-840),
§W8b-2 (:1044-1090), §W8b-3 (:1322-1368); the firewall block is the pre-edit
gate-verdicts.md §"Composite-collapse rule" pseudo-code (lines 178-188).
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402  import-only compliance

SCHEME = "METHODOLOGY-DIRECTIVE-LANDING"
L_MAX = "N/A"

# Byte-frozen composite-collapse pseudo-code block (gate-verdicts.md §"Composite-collapse
# rule"); the W8b-3 firewall asserts this exact substring survives the additive-only diff.
COLLAPSE_FIREWALL = """if regime_verdict == BREAKDOWN:
    composite = FAIL
elif sign_verdict == FAIL:
    composite = FAIL
elif magnitude_verdict == FAIL and regime_verdict == VALID:
    composite = FAIL
elif magnitude_verdict == FAIL and regime_verdict == MARGINAL:
    composite = INFO  # SIGN-correct, MAGNITUDE-wrong-but-out-of-regime
elif magnitude_verdict == INFO:
    composite = INFO
else:
    composite = PASS"""

CORPUS = "sessions/framework/registry/pru-class-corpus.md"

GATE_SPECS = {
    "S101-HK-SELECTION-RULE-PREFLIGHT-RULE": {
        "convention": "DIRECTIVE-ONLY-RULE-PLUS-CORPUS",
        "rule_file": ".claude/rules/math-scripts.md",
        "rule_start": "#### Selection-rule pre-flight for pre-registered nonzero matrix elements",
        "rule_stop_re": r"(?m)^### Enforcement\b",
        "rule_markers": [
            "#### Selection-rule pre-flight for pre-registered nonzero matrix elements",
            "center-character / triality CG-admissibility check",
            "NECESSARY condition only",
            "detect_selection_rule_preflight",
        ],
        "corpus_start": "## §22. Selection-rule pre-flight",
        "corpus_stop_re": r"(?m)^## §23\.",
        "corpus_markers": [
            "Selection-rule pre-flight",
            "871573da729c59722ee060b37c70741f8d917e2560fe11ef74910f6be3bd2925",
            "K=1",
        ],
        "static_pins": {
            "housekeeping_100a": ("sessions/session-100a/session-100a-housekeeping.md",
                                  "07b164c185ffd724d3495d27561c3a67f6796381010503b76a41ad31b39f8571"),
            "s100a_verdict": ("computations/session-100a/s100a_gate_verdicts.txt",
                              "446cef5501daa6bf4d485756506d8a41d1fb3455e26d59a5d6c1bac26b492030"),
        },
        "base_pins": {
            "math_scripts_pre_edit": "ed062fc5bfcd1fd8b999f55b331cfb3fde6430fd642282b5c921bb4ea141cc48",
            "corpus_pre_append": "2ad4cf7cc9cdcfd7c21f895da3360d3cc03c6630c3d88eb50365feb7e9869562",
        },
        "firewall": None,
        "value_tag": "rule_markers=4/4;corpus_markers=3/3;K=1;W2-2_calib;audithook=detect_selection_rule_preflight",
    },
    "S101-HK-SUFFIX-DISCIPLINE": {
        "convention": "DIRECTIVE-ONLY-VERBATIM-TRANSCRIPTION",
        "rule_file": ".claude/rules/regulator-pin-discipline.md",
        "rule_start": "## Extension: Channel-Scope Suffix Discipline",
        "rule_stop_re": None,  # last section -> EOF
        "rule_markers": [
            "Channel-Scope Suffix Discipline",
            "scope inside the citation token itself",
            "T-channel S_F^Connes = 0; channel-scoped per S56 W4 Correction 1",
            "the K-counter advances on distinct theorems, not repeat citations of S41",
        ],
        "corpus_start": "## §23. Channel-scope suffix discipline",
        "corpus_stop_re": r"(?m)^## §24\.",
        "corpus_markers": [
            "Channel-scope suffix discipline",
            "five-surface census",
            "s100a-w5-d5-seesaw-adjudication-workshop",
            "K=1",
        ],
        "static_pins": {
            "housekeeping_100a": ("sessions/session-100a/session-100a-housekeeping.md",
                                  "07b164c185ffd724d3495d27561c3a67f6796381010503b76a41ad31b39f8571"),
            "workshop": ("sessions/session-100a/workshops/s100a-w5-d5-seesaw-adjudication-workshop.md",
                         "d7632f2c6e4e455d02e0640182933fcbac301a8fea2b082218abb2b2d67f0ca5"),
        },
        "base_pins": {
            "regulator_pin_pre_edit": "4eb42d634e591d5cd21f0cde0c0f5fd25483d317a2663c5ac6b1f88799cf8f25",
            "corpus_pre_append": "2ad4cf7cc9cdcfd7c21f895da3360d3cc03c6630c3d88eb50365feb7e9869562",
        },
        "firewall": None,
        "value_tag": "rule_markers=4/4_verbatim;corpus_markers=4/4;K=1;W-4_five_surface_census",
    },
    "S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION": {
        "convention": "DIRECTIVE-ONLY-COMPOSES-WITH-COLLAPSE",
        "rule_file": ".claude/rules/gate-verdicts.md",
        "rule_start": "#### Plan-frozen gate-block operator precedence (applicability guards)",
        "rule_stop_re": r"(?m)^### Auto-shortening clause discipline\b",
        "rule_markers": [
            "#### Plan-frozen gate-block operator precedence (applicability guards)",
            "pre-declared disclosure extra-row",
            "applicability is a guard, not the hypothesis",
            "COMPOSES WITH the collapse rule; it does not modify it",
        ],
        "corpus_start": "## §24. Plan-frozen gate-block operator precedence",
        "corpus_stop_re": None,  # last section -> EOF
        "corpus_markers": [
            "Plan-frozen gate-block operator precedence",
            "273a0dc45a1e9f2500db5b7548fefed70ab6e7d82c3f4c945dcf9562f945d7ba",
            "a hollow PASS was REFUSED",
            "§19",
        ],
        "static_pins": {
            "housekeeping_100b": ("sessions/session-100b/session-100b-housekeeping.md",
                                  "461f1063fe93b8e1d076f0d463ba315c8fd67dd9d855ab74a16ff6a2ae3db6b7"),
            "w4_wp_cf_mirror": ("sessions/session-100b/session-100b-w4-workingpaper.md",
                                "371f74ecf31a4e0bdc60a1ce8f3b4dcb667cc1170c2861768cb409d009ce42d8"),
            "closeout": ("sessions/session-100b/session-100b-campaign-closeout-synthesis.md",
                         "8d3c8876b56aec6a52744d3564a017bfa01456db91817f6343a72e46b006b429"),
            "s100b_verdict": ("computations/session-100b/s100b_gate_verdicts.txt",
                              "95d7447adbf8684dc1dd6848946409e2a7e50681ad3c036722e9aefa569b89a4"),
        },
        "base_pins": {
            "gate_verdicts_pre_edit": "08659d979409c1a8226bf611d98005bf44bd473bd47c48d2bad1ec1144956b39",
            "corpus_pre_append": "2ad4cf7cc9cdcfd7c21f895da3360d3cc03c6630c3d88eb50365feb7e9869562",
        },
        "firewall": COLLAPSE_FIREWALL,
        "value_tag": "rule_markers=4/4;corpus_markers=4/4;firewall_collapse_byte_intact=True;K=1;W4-1_calib",
    },
}


def sha256_file(rel: str) -> str:
    p = ROOT / rel  # (local)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else "MISSING"


def closure_hash(pins: dict) -> str:
    """Stable hash over the sorted input-pin map (script-template.py Section 4)."""
    h = hashlib.sha256()  # (local)
    for k, v in sorted(pins.items()):
        h.update(("%s=%s\n" % (k, v)).encode("utf-8"))
    return h.hexdigest()


def extract_section(text: str, start: str, stop_re):
    """Return the substring from `start` (literal) to the next heading matching
    stop_re (or EOF if stop_re is None). Empty string if start not found."""
    i = text.find(start)  # (local)
    if i < 0:
        return ""
    if stop_re is None:
        return text[i:]
    m = re.search(stop_re, text[i + len(start):])  # (local)
    return text[i:] if not m else text[i: i + len(start) + m.start()]


def print_verdict_payload(gate_id, convention, verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    payload = {
        "session": 101,
        "gate_id": gate_id,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": convention,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", required=True, choices=sorted(GATE_SPECS))
    args = ap.parse_args()
    spec = GATE_SPECS[args.gate]
    t0 = time.time()  # (local)

    print("=== S101 W8b METHODOLOGY verify: %s ===" % args.gate)

    # 1. Rule-file markers.
    rule_text = (ROOT / spec["rule_file"]).read_text(encoding="utf-8")  # (local)
    rule_missing = [m for m in spec["rule_markers"] if m not in rule_text]  # (local)
    print("[rule markers] %d/%d present in %s" %
          (len(spec["rule_markers"]) - len(rule_missing), len(spec["rule_markers"]), spec["rule_file"]))
    for m in rule_missing:
        print("   MISSING rule marker: %r" % m)

    # 2. Corpus markers.
    corpus_text = (ROOT / CORPUS).read_text(encoding="utf-8")  # (local)
    corpus_missing = [m for m in spec["corpus_markers"] if m not in corpus_text]  # (local)
    print("[corpus markers] %d/%d present in %s" %
          (len(spec["corpus_markers"]) - len(corpus_missing), len(spec["corpus_markers"]), CORPUS))
    for m in corpus_missing:
        print("   MISSING corpus marker: %r" % m)

    # 3. Firewall (W8b-3 only): collapse pseudo-code block byte-present.
    firewall_ok = True  # (local)
    if spec["firewall"] is not None:
        firewall_ok = spec["firewall"] in rule_text
        print("[firewall] composite-collapse block byte-intact: %s" % firewall_ok)

    # 4. Static-source drift guard (binding-source SHAs vs plan pins).
    drift = []  # (local)
    static_runtime = {}  # (local)
    for key, (rel, pin) in spec["static_pins"].items():
        rt = sha256_file(rel)  # (local)
        static_runtime["src_%s" % key] = rt
        if rt != pin:
            drift.append((key, rel, rt, pin))
    print("[drift guard] static binding-source SHAs match plan pins: %s" % (not drift))
    for key, rel, rt, pin in drift:
        print("   DRIFT %s (%s): runtime %s... vs pin %s..." % (key, rel, rt[:16], pin[:16]))

    # 5. Dual-SHA.
    rule_section = extract_section(rule_text, spec["rule_start"], spec["rule_stop_re"])  # (local)
    corpus_section = extract_section(corpus_text, spec["corpus_start"], spec["corpus_stop_re"])  # (local)
    content_sha = hashlib.sha256(
        rule_section.encode("utf-8") + b"\n---CORPUS---\n" + corpus_section.encode("utf-8")
    ).hexdigest()  # (local)

    driver_content_sha = hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()  # (local)
    pins = {"_gate_id": args.gate, "_scheme": SCHEME, "_convention": spec["convention"],
            "_driver_content_sha": driver_content_sha}  # (local)
    pins.update(static_runtime)
    pins.update({"base_%s" % k: v for k, v in spec["base_pins"].items()})
    audit_sha = closure_hash(pins)

    print("  rule_section_len=%d  corpus_section_len=%d" % (len(rule_section), len(corpus_section)))
    print("  audit_sha256:   %s" % audit_sha)
    print("  content_sha256: %s" % content_sha)

    # 6. Verdict.
    rule_ok = not rule_missing and len(rule_section) > 0  # (local)
    corpus_ok = not corpus_missing and len(corpus_section) > 0  # (local)
    ok = rule_ok and corpus_ok and firewall_ok and not drift  # (local)
    verdict = "PASS" if ok else "FAIL"  # (local)

    value = spec["value_tag"]  # (local)
    if not ok:
        value = "FAIL_remediation;" + value + (";rule_missing=%d" % len(rule_missing)) \
            + (";corpus_missing=%d" % len(corpus_missing)) \
            + (";firewall_ok=%s" % firewall_ok) + (";drift=%d" % len(drift))

    extra = None  # (local)
    if spec["firewall"] is not None:
        extra = ["# composite-collapse pseudo-code block BYTE-UNCHANGED (additive-only diff); "
                 "modifying it would be the Class-3 violation this directive avoids"]

    print_verdict_payload(args.gate, spec["convention"], verdict, value,
                          audit_sha, content_sha, extra_rows=extra)
    print("  elapsed %.2fs" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
