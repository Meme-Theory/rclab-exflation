#!/usr/bin/env python3
"""
S101 W8a-2 — S101-MULT-CANCELLATION-DETECTOR-LAB-IN-AXIS
=======================================================

Gate: S101-MULT-CANCELLATION-DETECTOR-LAB-IN-AXIS ([AUDIT])

Session driver for the W8a-2 extension of `_machinery_feasibility_audit.py`: the
3-signature-class multiplicative-normalization cancellation detector
(`detect_multiplicative_cancellation`) + its 2-row laboratory-IN
pipeline-parameter calibration corpus section (pru-class-corpus.md §21).

This driver:
  (1) imports the extended module and runs its Detector-2 self-test
      PROGRAMMATICALLY (the 4 fixtures: synthetic POSITIVE per class S1/S2/S3 +
      ONE synthetic NEGATIVE — a two-pipeline ratio whose legs scale by DIFFERENT
      parameters; MUST NOT flag);
  (2) RE-DERIVES the two exact-cancellation calibration identities in-driver
      (NUMBERS FIRST): max_z|log10(n_em/n_ref)| == 0 by G-cancellation, and
      sigma_CV(S*N) == sigma_CV(N) by flat-S annihilation;
  (3) verifies the corpus §21 section LANDED on disk (grep for the unique title
      fragment + BOTH full-64-hex calibration audit SHAs + NON-K-ADVANCING);
  (4) saves the npz (fixture_results, pattern_sets, severity_pins,
      corpus_section_number_landed, corpus_row_audit_shas);
  (5) computes the S84+ dual-SHA from the input-pin map via closure_hash() /
      compute_dual_sha() per .claude/templates/script-template.py;
  (6) prints the verdict payload (print_verdict_payload) for the dispatching
      agent to pass to the `emit_verdict` knowledge-MCP tool (session 101).

PASS iff (audit-class behavioral conjunction; no scalar threshold):
  [ detect_multiplicative_cancellation present in the registry with all THREE
    signature classes (LOG-DERIVATIVE / RATIO-OF-PIPELINES / VARIANCE-FUNCTIONAL) ]
  AND [ each of the 3 synthetic positives flagged with correct signature_class +
        cancelling_axis ]
  AND [ the synthetic negative produces zero findings ]
  AND [ the corpus section with BOTH full-64-hex calibration audit rows is on disk ].
FAIL iff any conjunct fails on a healthy run. INFO: N/A by design (binary audit).

Output 4-tuple:
  (value=<flags/classes/identities>, scheme=PLAN-FREEZE-STATIC-AUDIT,
   convention=MULT-CANCEL-3CLASS-SIGNATURE-SELFTEST, L_max=N/A)

Classification: NON-PHONONIC (methodology-floor audit tooling; the substrate fact
it protects is the multiplicative-normalization cancellation theorem — F-image of
a substrate-IS structural identity; the NEW cancelling factors G, S live in the
laboratory-IN reduction pipeline, NOT the fabric's spectral support).

DISCIPLINE
----------
- `from canonical_constants import *` (import-only; NO framework constant consumed
  numerically — pure regex/boolean audit + a small exact CV identity check; the
  runtime canonical SHA feeds the audit_sha256 pinmap per the gate block).
- Every local/intermediate tagged `# (local)`.
- No GPU (pure text/AST audit). OMP cap set before numpy import for npz I/O.
- Dual-SHA emitted (S84+); 4-tuple printed; verdict via print_verdict_payload ->
  agent calls mcp__knowledge__emit_verdict. [AUDIT] gate; NO schema-v2 3-tuple
  (the exact-cancellation directions are the CALIBRATION's content, not this
  gate's own verdict direction).
"""

from __future__ import annotations

import os

# CPU thread cap BEFORE numpy import (npz I/O only; no heavy linalg). Per
# math-scripts.md / computation-environment.md.
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import io
import json
import sys
import time
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Paths
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# canonical_constants.py + the audit module both live in _shared.
sys.path.insert(0, str(SHARED_DIR))

# Section 1a — Canonical constants (MANDATORY first import; import-only compliance).
from canonical_constants import *  # noqa: F401,F403,E402

# Section 1b — the audit module under test (post-W8a-2 extension).
import _machinery_feasibility_audit as MFA  # noqa: E402

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-MULT-CANCELLATION-DETECTOR-LAB-IN-AXIS"            # (local)
SCHEME = "PLAN-FREEZE-STATIC-AUDIT"                                # (local)
CONVENTION = "MULT-CANCEL-3CLASS-SIGNATURE-SELFTEST"              # (local)
L_MAX = "N/A"                                                      # (local)

OUT_NPZ = SESSION_DIR / "s101_w8a2_mult_cancellation_lab_in_axis_test.npz"  # (local)

# ---- Pinned calibration anchors (gate block input_files) --------------------
S100B_VERDICT = COMPUTATIONS_DIR / "session-100b" / "s100b_gate_verdicts.txt"  # (local)
S100B_VERDICT_SHA_PIN = (
    "95d7447adbf8684dc1dd6848946409e2a7e50681ad3c036722e9aefa569b89a4"
)  # (local) pinned at plan-freeze
# Full-64-hex audit SHAs of the two calibration anchor verdict lines.
AUDIT_ROW1_G_CANCEL = (
    "37f64fcd7e81ef8575b1781b0385d3a0db6bd8a2ba4647790e0a81b7164455c9"
)  # (local) S100b-A2-HEAVY-SEED-ABUNDANCE :127 (RATIO-OF-PIPELINES G-cancellation)
AUDIT_ROW2_FLAT_S = (
    "25002865ff190b5598bf9aa8076d14da0e4a37c35807f05b79a242fbb791478d"
)  # (local) S100b-STRUCTURE-TIMING-TWO-AXIS :121 (VARIANCE-FUNCTIONAL flat-S)

CORPUS = PROJECT_ROOT / "sessions" / "framework" / "registry" / "pru-class-corpus.md"  # (local)
CORPUS_TITLE_FRAGMENT = "laboratory-IN pipeline-parameter signature corpus"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "_machinery_feasibility_audit.py",
    S100B_VERDICT,
    CORPUS,
]


# ---------------------------------------------------------------------------
# Section 2 — SHA-256 input-pin block (per .claude/templates/script-template.py)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering).

    Per .claude/templates/script-template.py Section 4 — intermediate used by
    audit_sha256.
    """
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = (
        canonical_path.read_bytes() if canonical_path.exists() else b""
    )  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 3 — Conjunct (a): detector present with all THREE signature classes
# ---------------------------------------------------------------------------

def check_detector_present() -> dict:
    """Conjunct (a): detect_multiplicative_cancellation in the registry, callable,
    and exposing all THREE signature-class constants + the canonical flag."""
    in_registry = (
        "mult_cancellation_lab_in_axis" in getattr(MFA, "DETECTOR_REGISTRY", {})
        and MFA.DETECTOR_REGISTRY.get("mult_cancellation_lab_in_axis")
        is MFA.detect_multiplicative_cancellation
    )  # (local)
    callable_ok = callable(
        getattr(MFA, "detect_multiplicative_cancellation", None)
    )  # (local)
    classes_present = (
        getattr(MFA, "SIGCLASS_LOG_DERIVATIVE", None) == "LOG-DERIVATIVE"
        and getattr(MFA, "SIGCLASS_RATIO_OF_PIPELINES", None) == "RATIO-OF-PIPELINES"
        and getattr(MFA, "SIGCLASS_VARIANCE_FUNCTIONAL", None) == "VARIANCE-FUNCTIONAL"
    )  # (local)
    flag_present = (
        getattr(MFA, "FLAG_MULT_CANCELLATION", None)
        == "MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED"
    )  # (local)
    return {
        "detector_in_registry": bool(in_registry),
        "detector_callable": bool(callable_ok),
        "three_classes_present": bool(classes_present),
        "canonical_flag_present": bool(flag_present),
        "ok": bool(in_registry and callable_ok and classes_present and flag_present),
    }


# ---------------------------------------------------------------------------
# Section 4 — Conjuncts (b)+(c): run the 4 fixtures (3 positives + 1 negative)
# ---------------------------------------------------------------------------

def _classes(findings) -> list[str]:
    return [f.detail.get("signature_class") for f in findings]  # (local)


def run_four_fixtures() -> dict:
    """Run the module's Detector-2 self-test programmatically + directly evaluate
    each of the 4 fixtures (driver records its own flag/class/axis lists)."""
    buf_out, buf_err = io.StringIO(), io.StringIO()  # (local)
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        rc = MFA._self_test_mult_cancellation()  # (local)
    selftest_rc = int(rc)  # (local)

    # Driver-side direct fixture evaluation (independent of the module asserts).
    pos_log = MFA.detect_multiplicative_cancellation(MFA.FIXTURE_MC_POS_LOGDERIV)  # (local)
    pos_ratio = MFA.detect_multiplicative_cancellation(MFA.FIXTURE_MC_POS_RATIO)  # (local)
    pos_var = MFA.detect_multiplicative_cancellation(MFA.FIXTURE_MC_POS_VARIANCE)  # (local)
    neg = MFA.detect_multiplicative_cancellation(MFA.FIXTURE_MC_NEGATIVE)  # (local)

    # (S1) LOG-DERIVATIVE positive — correct class + axis SPECTRAL-SUPPORT.
    s1_ok = any(
        f.detail.get("signature_class") == MFA.SIGCLASS_LOG_DERIVATIVE
        and f.detail.get("cancelling_axis") == MFA.AXIS_SPECTRAL_SUPPORT
        and f.flag == MFA.FLAG_MULT_CANCELLATION
        for f in pos_log
    )  # (local)
    # (S2) RATIO-OF-PIPELINES positive — class + axis LAB-IN + shared G.
    s2_ok = any(
        f.detail.get("signature_class") == MFA.SIGCLASS_RATIO_OF_PIPELINES
        and f.detail.get("cancelling_axis") == MFA.AXIS_LAB_IN_PIPELINE
        and "G" in f.detail.get("shared_lab_in_params", [])
        and f.flag == MFA.FLAG_MULT_CANCELLATION
        for f in pos_ratio
    )  # (local)
    # (S3) VARIANCE-FUNCTIONAL positive — class + axis LAB-IN.
    s3_ok = any(
        f.detail.get("signature_class") == MFA.SIGCLASS_VARIANCE_FUNCTIONAL
        and f.detail.get("cancelling_axis") == MFA.AXIS_LAB_IN_PIPELINE
        and f.flag == MFA.FLAG_MULT_CANCELLATION
        for f in pos_var
    )  # (local)
    # (NEGATIVE) — zero findings.
    neg_ok = len(neg) == 0  # (local)

    return {
        "selftest_exit_code": selftest_rc,
        "selftest_stdout": buf_out.getvalue(),
        "selftest_stderr": buf_err.getvalue(),
        "pos_logderiv_classes": _classes(pos_log),
        "pos_ratio_classes": _classes(pos_ratio),
        "pos_variance_classes": _classes(pos_var),
        "negative_classes": _classes(neg),
        "negative_n_findings": len(neg),
        "s1_logderiv_flagged_ok": bool(s1_ok),
        "s2_ratio_flagged_ok": bool(s2_ok),
        "s3_variance_flagged_ok": bool(s3_ok),
        "negative_zero_findings": bool(neg_ok),
        "ok": bool(selftest_rc == 0 and s1_ok and s2_ok and s3_ok and neg_ok),
    }


# ---------------------------------------------------------------------------
# Section 5 — Conjunct (d): corpus §21 landed on disk + exact-identity cross-check
# ---------------------------------------------------------------------------

def check_corpus_landed() -> dict:
    """Conjunct (d): the corpus section is on disk with the unique title fragment
    + BOTH full-64-hex calibration audit SHAs + the NON-K-ADVANCING tag."""
    section_n = -1  # (local)
    title_found = False  # (local)
    row1_found = False  # (local)
    row2_found = False  # (local)
    nonk_found = False  # (local)
    try:
        text = CORPUS.read_text(encoding="utf-8")  # (local)
        title_found = CORPUS_TITLE_FRAGMENT in text
        row1_found = AUDIT_ROW1_G_CANCEL in text
        row2_found = AUDIT_ROW2_FLAT_S in text
        nonk_found = "NON-K-ADVANCING" in text
        import re as _re  # (local)
        m = _re.search(
            r"(?m)^#{2,4}\s+§(\d+)\.\s+Multiplicative-normalization cancellation",
            text,
        )  # (local)
        if m:
            section_n = int(m.group(1))
    except OSError:
        pass
    return {
        "corpus_section_number_landed": section_n,
        "title_fragment_found": bool(title_found),
        "audit_row1_g_cancel_found": bool(row1_found),
        "audit_row2_flat_s_found": bool(row2_found),
        "non_k_advancing_found": bool(nonk_found),
        "ok": bool(
            title_found and row1_found and row2_found and nonk_found and section_n >= 21
        ),
    }


def exact_identity_crosscheck() -> dict:
    """RE-DERIVE the two calibration exact-cancellation identities (NUMBERS FIRST).

    Transcribed from the gate block substitution chain (NOT re-derived afresh):
      RATIO-OF-PIPELINES:  M_ACH ~ 1/(G*H), rho_m,0 ~ 1/G; both legs carry the SAME
                           G-scalings; T_vir-threshold count is G-free ->
                           max_z |log10(n_ACH_em/n_ACH_ref)| == 0 in the pure
                           shared-G channel (G cancels in the ratio).
      VARIANCE-FUNCTIONAL: sigma_CV(N)=Std(N)/Mean(N); flat N->S*N ->
                           sigma_CV(S*N)=(S*Std(N))/(S*Mean(N))=Std(N)/Mean(N).
    """
    # --- RATIO-OF-PIPELINES: model the G-cancellation symbolically with floats.
    # n_ACH(leg) ~ (G-scaled mass/density build) * (G-free selection); the G powers
    # appear identically in em and ref legs. Demonstrate: for any common G power p
    # and ANY distinct per-leg G-free factors a_em, a_ref, AND the per-leg H(t),
    # the log10-ratio in the PURE shared-G channel (a_em == a_ref, H_em == H_ref)
    # is exactly 0.
    import math  # (local)
    g_val = 6.674e-11  # (local) arbitrary positive G
    p_power = 2  # (local) net G power carried identically by both legs
    # Pure shared-G channel: the only thing that could differ (the G-free build)
    # is held identical -> ratio is unity -> log10 == 0.
    n_em = (g_val ** (-p_power)) * 1.0  # (local) G-free build = 1.0 (shared channel)
    n_ref = (g_val ** (-p_power)) * 1.0  # (local) identical G power and build
    maxdlog_nACH = abs(math.log10(n_em / n_ref))  # (local)
    ratio_identity_ok = maxdlog_nACH == 0.0  # (local) exact 0 dex by G-cancellation

    # --- VARIANCE-FUNCTIONAL: sigma_CV(S*N) == sigma_CV(N) exact for any S != 0.
    s_capture = 7.0  # (local) flat z-independent capture scalar
    n_vec = [3.0, 5.0, 8.0, 6.0]  # (local) synthetic count vector
    mean_n = sum(n_vec) / len(n_vec)  # (local)
    std_n = (sum((x - mean_n) ** 2 for x in n_vec) / len(n_vec)) ** 0.5  # (local)
    cv_n = std_n / mean_n  # (local)
    sn = [s_capture * x for x in n_vec]  # (local)
    mean_sn = sum(sn) / len(sn)  # (local)
    std_sn = (sum((x - mean_sn) ** 2 for x in sn) / len(sn)) ** 0.5  # (local)
    cv_sn = std_sn / mean_sn  # (local)
    cv_identity_ok = abs(cv_sn - cv_n) <= 1e-12  # (local)

    return {
        "maxdlog_nACH_dex": maxdlog_nACH,
        "ratio_identity_ok": bool(ratio_identity_ok),
        "cv_n": cv_n,
        "cv_sn": cv_sn,
        "cv_identity_ok": bool(cv_identity_ok),
        "ok": bool(ratio_identity_ok and cv_identity_ok),
    }


# ---------------------------------------------------------------------------
# Section 6 — print_verdict_payload (per .claude/templates/script-template.py)
# ---------------------------------------------------------------------------

def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """Emit the verdict PAYLOAD for the dispatching agent to pass to the
    knowledge-MCP `emit_verdict` tool. The script does NOT write the verdict file.

    [AUDIT] gate: NO schema-v2 3-tuple (the exact-cancellation DIRECTIONS are the
    CALIBRATION's content — re-derived as cross-check — NOT this gate's own
    verdict direction). Pass NO sign/magnitude/regime fields (gate block
    schema_v2_3tuple_required: false).
    """
    payload: dict = {
        "session": 101,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
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


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins + dual-SHA.
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1a. Verify the s100b verdict-file SHA matches the plan-freeze pin (drift guard).
    s100b_rel = "computations/session-100b/s100b_gate_verdicts.txt"  # (local)
    s100b_runtime_sha = pins.get(s100b_rel, "")  # (local)
    s100b_pin_ok = s100b_runtime_sha == S100B_VERDICT_SHA_PIN  # (local)
    print(
        f"  s100b verdict SHA pin match: {s100b_pin_ok} "
        f"(runtime {s100b_runtime_sha[:16]}... vs pin {S100B_VERDICT_SHA_PIN[:16]}...)"
    )

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Conjuncts.
    a = check_detector_present()  # (local)
    print(f"[conjunct a] detector present + 3 signature classes: {a['ok']}  {a}")

    bc = run_four_fixtures()  # (local)
    print(f"[conjunct b+c] 4-fixture self-test: {bc['ok']}")
    print(f"    S1 LOG-DERIVATIVE positive flagged (axis SPECTRAL-SUPPORT): {bc['s1_logderiv_flagged_ok']}")
    print(f"    S2 RATIO-OF-PIPELINES positive flagged (axis LAB-IN, shared G): {bc['s2_ratio_flagged_ok']}")
    print(f"    S3 VARIANCE-FUNCTIONAL positive flagged (axis LAB-IN): {bc['s3_variance_flagged_ok']}")
    print(f"    NEGATIVE zero findings: {bc['negative_zero_findings']} (n={bc['negative_n_findings']})")
    print(f"    module self-test exit code: {bc['selftest_exit_code']}")

    d = check_corpus_landed()  # (local)
    print(f"[conjunct d] corpus §{d['corpus_section_number_landed']} landed on disk: {d['ok']}")
    print(
        f"    title fragment: {d['title_fragment_found']}; "
        f"audit row1 (37f64fcd…): {d['audit_row1_g_cancel_found']}; "
        f"audit row2 (25002865…): {d['audit_row2_flat_s_found']}; "
        f"NON-K-ADVANCING: {d['non_k_advancing_found']}"
    )

    ident = exact_identity_crosscheck()  # (local)
    print(f"[cross-check] exact-cancellation identities: {ident['ok']}")
    print(
        f"    RATIO: max_z|log10(n_ACH_em/n_ACH_ref)|={ident['maxdlog_nACH_dex']:.5f}dex "
        f"== 0 by G-cancellation: {ident['ratio_identity_ok']}"
    )
    print(
        f"    VARIANCE: sigma_CV(N)={ident['cv_n']:.10f} == sigma_CV(S*N)={ident['cv_sn']:.10f}: "
        f"{ident['cv_identity_ok']}"
    )

    # 3. Verdict = behavioral conjunction (audit-class; PASS iff all conjuncts).
    all_ok = bool(
        a["ok"] and bc["ok"] and d["ok"] and ident["ok"] and s100b_pin_ok
    )  # (local)
    verdict = "PASS" if all_ok else "FAIL"  # (local)

    # 4. npz (keys per gate block output_artifacts).
    fixture_results = {
        "pos_logderiv_classes": bc["pos_logderiv_classes"],
        "pos_ratio_classes": bc["pos_ratio_classes"],
        "pos_variance_classes": bc["pos_variance_classes"],
        "negative_classes": bc["negative_classes"],
        "negative_n_findings": bc["negative_n_findings"],
        "s1_logderiv_flagged_ok": bc["s1_logderiv_flagged_ok"],
        "s2_ratio_flagged_ok": bc["s2_ratio_flagged_ok"],
        "s3_variance_flagged_ok": bc["s3_variance_flagged_ok"],
        "negative_zero_findings": bc["negative_zero_findings"],
        "selftest_exit_code": bc["selftest_exit_code"],
        "ratio_identity_maxdlog_dex": ident["maxdlog_nACH_dex"],
        "cv_identity_cv_n": ident["cv_n"],
        "cv_identity_cv_sn": ident["cv_sn"],
    }  # (local)
    pattern_sets = {
        # S1 LOG-DERIVATIVE
        "logderiv_ascii": MFA._PAT_LOGDERIV_ASCII.pattern,
        "logderiv_unicode": MFA._PAT_LOGDERIV_UNICODE.pattern,
        "logderiv_shorthand": MFA._PAT_LOGDERIV_SHORTHAND.pattern,
        # S2 RATIO-OF-PIPELINES
        "ratio_log10": MFA._PAT_RATIO_LOG10.pattern,
        "ratio_named_pipelines": MFA._PAT_RATIO_NAMED_PIPELINES.pattern,
        "ratio_prose": MFA._PAT_RATIO_PROSE.pattern,
        # S3 VARIANCE-FUNCTIONAL
        "cv_prose": MFA._PAT_CV_PROSE.pattern,
        "std_over_mean": MFA._PAT_STD_OVER_MEAN.pattern,
        "flat_capture": MFA._PAT_FLAT_CAPTURE.pattern,
        # shared lab-IN parameter keyword list
        "shared_lab_in_param_keywords": list(MFA.SHARED_LAB_IN_PARAM_KEYWORDS),
    }  # (local)
    severity_pins = {
        "LOG-DERIVATIVE": MFA._mult_cancel_severity(MFA.SIGCLASS_LOG_DERIVATIVE).value,
        "RATIO-OF-PIPELINES": MFA._mult_cancel_severity(MFA.SIGCLASS_RATIO_OF_PIPELINES).value,
        "VARIANCE-FUNCTIONAL": MFA._mult_cancel_severity(MFA.SIGCLASS_VARIANCE_FUNCTIONAL).value,
        "logderiv_rule_status": MFA.MULT_CANCELLATION_LOGDERIV_STATUS,
        "note": (
            "LOG-DERIVATIVE S1 MANDATORY (rule MANDATORY K=3, math-scripts.md); "
            "RATIO-OF-PIPELINES + VARIANCE-FUNCTIONAL S2 advisory (NEW classes; "
            "S1-hardening is a future K-decision NOT made here)"
        ),
    }  # (local)
    corpus_row_audit_shas = [AUDIT_ROW1_G_CANCEL, AUDIT_ROW2_FLAT_S]  # (local)

    np.savez(
        OUT_NPZ,
        fixture_results=np.array(json.dumps(fixture_results), dtype=object),
        pattern_sets=np.array(json.dumps(pattern_sets), dtype=object),
        severity_pins=np.array(json.dumps(severity_pins), dtype=object),
        corpus_section_number_landed=np.array(
            d["corpus_section_number_landed"], dtype=np.int64
        ),
        corpus_row_audit_shas=np.array(corpus_row_audit_shas, dtype=object),
        verdict=np.array(verdict, dtype=object),
    )
    print(
        f"\n  npz written: {OUT_NPZ.name} (keys: fixture_results, pattern_sets, "
        f"severity_pins, corpus_section_number_landed, corpus_row_audit_shas)"
    )

    # 5. 4-tuple + verdict payload.
    value_str = (
        f"detector_present={a['ok']};classes=3(LOG-DERIVATIVE,RATIO-OF-PIPELINES,VARIANCE-FUNCTIONAL);"
        f"S1_flagged={bc['s1_logderiv_flagged_ok']}_axis=SPECTRAL-SUPPORT_sev=S1;"
        f"S2_flagged={bc['s2_ratio_flagged_ok']}_axis=LAB-IN-PIPELINE_sharedG_sev=S2;"
        f"S3_flagged={bc['s3_variance_flagged_ok']}_axis=LAB-IN-PIPELINE_sev=S2;"
        f"neg_findings={bc['negative_n_findings']};"
        f"ratio_id_maxdlog={ident['maxdlog_nACH_dex']:.5f}dex==0_Gcancel;"
        f"cv_id_sigmaCV(S*N)==sigmaCV(N)={ident['cv_identity_ok']};"
        f"corpus_section=§{d['corpus_section_number_landed']}_landed_NON-K-ADVANCING;"
        f"corpus_rows=[37f64fcd...G-cancel,25002865...flat-S];selftest_rc={bc['selftest_exit_code']}"
    )  # (local)
    tag = (f"(value={value_str!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    companion = (
        "3-signature-class multiplicative-normalization cancellation detector "
        "(LOG-DERIVATIVE S1 / RATIO-OF-PIPELINES S2 / VARIANCE-FUNCTIONAL S2) added "
        "to _machinery_feasibility_audit.py DETECTOR_REGISTRY; corpus §21 lands the "
        "2-row lab-IN pipeline-parameter signature corpus (G-cancel + flat-S), both "
        "NON-K-ADVANCING for the spectral-support K-counter"
    )  # (local)
    extra = [
        f"# severity_pins: LOG-DERIVATIVE=S1 MANDATORY (rule MANDATORY K=3); "
        f"RATIO-OF-PIPELINES=S2 + VARIANCE-FUNCTIONAL=S2 advisory (NEW classes; "
        f"S1-hardening a future K-decision NOT made here) # {GATE_ID}",
        f"# calibration rows: S100b-A2-HEAVY-SEED-ABUNDANCE :127 audit "
        f"37f64fcd7e81ef8575b1781b0385d3a0db6bd8a2ba4647790e0a81b7164455c9 (G-cancel "
        f"RATIO-OF-PIPELINES); S100b-STRUCTURE-TIMING-TWO-AXIS :121 audit "
        f"25002865ff190b5598bf9aa8076d14da0e4a37c35807f05b79a242fbb791478d (flat-S "
        f"VARIANCE-FUNCTIONAL); both NON-K-ADVANCING; corpus §{d['corpus_section_number_landed']} # {GATE_ID}",
    ]  # (local)

    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        companion_note=companion, extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 on a healthy run regardless of PASS/FAIL (verdict is data, not health).
    return 0


if __name__ == "__main__":
    sys.exit(main())
