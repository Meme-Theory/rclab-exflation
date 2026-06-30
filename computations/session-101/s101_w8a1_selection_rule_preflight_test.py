#!/usr/bin/env python3
"""
S101 W8a-1 — S101-HK-SELECTION-RULE-PREFLIGHT-AUDIT
===================================================

Gate: S101-HK-SELECTION-RULE-PREFLIGHT-AUDIT ([AUDIT])

Session driver for the inaugural `_machinery_feasibility_audit.py` module. This
driver:
  (1) imports the new module and runs its `--self-test` PROGRAMMATICALLY (the two
      pinned fixtures + their flag/no-flag assertions);
  (2) RE-DERIVES the W2-2 mod-3 calibration arithmetic in-driver as a cross-check
      against the pinned companion row at s100a_gate_verdicts.txt:40
      ('literal (1,0)<->(1,1) |s|^2 element=0 exact (center-Z3/triality selection)',
      canonical line :36 audit 871573da729c5972...);
  (3) saves the npz (fixture_results, triality_table, pattern_set, severity_pin);
  (4) computes the S84+ dual-SHA from the input-pin map via closure_hash() /
      compute_dual_sha() per .claude/templates/script-template.py;
  (5) prints the verdict payload (print_verdict_payload) for the dispatching agent
      to pass to the `emit_verdict` knowledge-MCP tool (session 101).

PASS iff (audit-class behavioral conjunction; no scalar threshold):
  [ module file exists with detect_selection_rule_preflight in its registry ]
  AND [ synthetic POSITIVE fixture flagged SELECTION-RULE-PREFLIGHT-VIOLATION ]
  AND [ synthetic NEGATIVE fixture produces zero findings ]
  AND [ in-driver W2-2 mod-3 cross-check reproduces element=0 EXACTLY (1 != 0 mod 3) ].
FAIL iff any conjunct fails on a healthy run. INFO: N/A by design (no band).

Output 4-tuple:
  (value=<flags/trialities>, scheme=PLAN-FREEZE-STATIC-AUDIT,
   convention=SELECTION-RULE-CG-ADMISSIBILITY-SELFTEST, L_max=N/A)

Classification: NON-PHONONIC (methodology-floor audit tooling; the substrate fact
it protects is PARTICLE-class — SU(3) center-Z3 / triality selection rule).

DISCIPLINE
----------
- `from canonical_constants import *` (import-only; NO framework constant consumed
  numerically — pure mod-3 integer arithmetic + a registry self-test; the runtime
  canonical SHA feeds the audit_sha256 pinmap per the gate block input_files).
- Every local/intermediate tagged `# (local)`.
- No GPU (pure text/AST audit). OMP cap set before numpy import for npz I/O.
- Dual-SHA emitted (S84+); 4-tuple printed; verdict via print_verdict_payload ->
  agent calls mcp__knowledge__emit_verdict.
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

# canonical_constants.py + the new audit module both live in _shared.
sys.path.insert(0, str(SHARED_DIR))

# Section 1a — Canonical constants (MANDATORY first import; import-only compliance).
from canonical_constants import *  # noqa: F401,F403,E402

# Section 1b — the inaugural audit module under test.
import _machinery_feasibility_audit as MFA  # noqa: E402

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-HK-SELECTION-RULE-PREFLIGHT-AUDIT"                 # (local)
SCHEME = "PLAN-FREEZE-STATIC-AUDIT"                                # (local)
CONVENTION = "SELECTION-RULE-CG-ADMISSIBILITY-SELFTEST"           # (local)
L_MAX = "N/A"                                                      # (local)

OUT_NPZ = SESSION_DIR / "s101_w8a1_selection_rule_preflight_test.npz"  # (local)

# Pinned calibration anchor (gate block input_files).
S100A_VERDICT = COMPUTATIONS_DIR / "session-100a" / "s100a_gate_verdicts.txt"  # (local)
S100A_VERDICT_SHA_PIN = (
    "446cef5501daa6bf4d485756506d8a41d1fb3455e26d59a5d6c1bac26b492030"
)  # (local) pinned at plan-freeze
S100A_CANON_AUDIT_SHA = (
    "871573da729c59722ee060b37c70741f8d917e2560fe11ef74910f6be3bd2925"
)  # (local) S100a-YUKAWA-OVERLAP-OFFDIAG canonical line :36 audit_sha256

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "_machinery_feasibility_audit.py",
    S100A_VERDICT,
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
# Section 3 — Conjunct (a): module exists + detector in registry
# ---------------------------------------------------------------------------

def check_module_present() -> dict:
    """Conjunct (a): module file exists with detect_selection_rule_preflight in
    its detector registry."""
    module_path = SHARED_DIR / "_machinery_feasibility_audit.py"  # (local)
    file_exists = module_path.exists()  # (local)
    in_registry = (
        "selection_rule_preflight" in getattr(MFA, "DETECTOR_REGISTRY", {})
        and MFA.DETECTOR_REGISTRY.get("selection_rule_preflight")
        is MFA.detect_selection_rule_preflight
    )  # (local)
    callable_ok = callable(getattr(MFA, "detect_selection_rule_preflight", None))  # (local)
    return {
        "file_exists": bool(file_exists),
        "detector_in_registry": bool(in_registry),
        "detector_callable": bool(callable_ok),
        "ok": bool(file_exists and in_registry and callable_ok),
    }


# ---------------------------------------------------------------------------
# Section 4 — Conjunct (b)+(c): run the module's --self-test programmatically
# ---------------------------------------------------------------------------

def run_module_selftest() -> dict:
    """Invoke MFA._self_test() programmatically; capture stdout/stderr + exit code.

    Also directly re-checks the two fixtures so the driver records the fixture
    flag lists itself (not only the module's internal asserts)."""
    buf_out, buf_err = io.StringIO(), io.StringIO()  # (local)
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        rc = MFA._self_test()  # (local)
    selftest_rc = int(rc)  # (local)

    # Driver-side direct fixture evaluation (independent of the module's asserts).
    pos_findings = MFA.detect_selection_rule_preflight(MFA.FIXTURE_POSITIVE)  # (local)
    neg_findings = MFA.detect_selection_rule_preflight(MFA.FIXTURE_NEGATIVE)  # (local)
    pos_flags = [f.flag for f in pos_findings]  # (local)
    neg_flags = [f.flag for f in neg_findings]  # (local)

    positive_flagged_violation = (
        MFA.FLAG_SELECTION_RULE_VIOLATION in pos_flags
    )  # (local)
    negative_zero_findings = len(neg_findings) == 0  # (local)

    return {
        "selftest_exit_code": selftest_rc,
        "selftest_stdout": buf_out.getvalue(),
        "selftest_stderr": buf_err.getvalue(),
        "positive_flags": pos_flags,
        "negative_flags": neg_flags,
        "positive_flagged_violation": bool(positive_flagged_violation),
        "negative_zero_findings": bool(negative_zero_findings),
        "ok": bool(
            selftest_rc == 0
            and positive_flagged_violation
            and negative_zero_findings
        ),
    }


# ---------------------------------------------------------------------------
# Section 5 — Conjunct (d): in-driver W2-2 mod-3 calibration cross-check
# ---------------------------------------------------------------------------

def w2_2_mod3_crosscheck() -> dict:
    """RE-DERIVE the W2-2 calibration arithmetic in-driver (NUMBERS FIRST).

    Transcribed from the gate block substitution chain (NOT re-derived afresh):
      t(p,q) := (p - q) mod 3
      a=(1,0): t=1 ; b=(1,1): t=0 ; O=|s(h)|^2: t=0 (center-invariant always)
      center selection: <a|O|b> != 0 REQUIRES t(a) == (t(b) + t(O)) mod 3
        -> 1 == (0 + 0) mod 3 -> 1 == 0  -> FALSE
        -> the center average annihilates the element: element = 0 EXACTLY.
      s(h) itself is in (2,0): t(s)=2 (== -1 mod 3) and CAN connect t-adjacent
        sectors: t(1,1)=0 == t(1,0)+t(s) = (1+2) mod 3 = 0 (the connecting property
        belongs to s(h), NOT to |s(h)|^2). This is the NEGATIVE fixture.
    Cross-checked against the pinned companion row s100a_gate_verdicts.txt:40:
      'literal (1,0)<->(1,1) |s|^2 element=0 exact (center-Z3/triality selection)'.
    """
    # Use the module's own triality helper so the driver and detector agree.
    t = MFA._triality  # (local)

    t_10 = t(1, 0)  # (local) -> 1
    t_11 = t(1, 1)  # (local) -> 0
    # |s(h)|^2 center character: s in (2,0) -> t=2; conj(s) in (0,2) -> t=(0-2)%3=1;
    # t(|s|^2) = (2 + 1) % 3 = 0 (and the module recognises mod-squared -> 0).
    t_s = t(2, 0)  # (local) -> 2
    t_s_conj = t(0, 2)  # (local) -> 1
    t_mod_sq_arith = (t_s + t_s_conj) % 3  # (local) -> 0
    t_mod_sq_module = MFA._operator_center_character("|s(h)|^2")  # (local) -> 0

    # Center selection predicate for the calibration element <(1,0)| |s|^2 |(1,1)>.
    lhs = t_10  # (local) -> 1
    rhs = (t_11 + t_mod_sq_arith) % 3  # (local) -> 0
    predicate_holds = (lhs == rhs)  # (local) -> False
    element_is_zero_exact = not predicate_holds  # (local) -> True (1 != 0 mod 3)

    # NEGATIVE fixture predicate <(1,1)| s(h) |(1,0)> with s in (2,0).
    neg_lhs = t_11  # (local) -> 0
    neg_rhs = (t_10 + t_s) % 3  # (local) -> (1+2)%3 = 0
    neg_admissible = (neg_lhs == neg_rhs)  # (local) -> True

    # Cross-check anchor presence on disk (companion row :40).
    anchor_line = ""  # (local)
    anchor_phrase = "element=0 exact (center-Z3/triality selection)"  # (local)
    try:
        for ln in S100A_VERDICT.read_text(encoding="utf-8").splitlines():
            if anchor_phrase in ln and "literal (1,0)<->(1,1)" in ln:
                anchor_line = ln.strip()
                break
    except OSError:
        anchor_line = ""
    anchor_phrase_found = bool(anchor_line)  # (local)
    canon_audit_found = S100A_CANON_AUDIT_SHA in S100A_VERDICT.read_text(
        encoding="utf-8"
    )  # (local)

    return {
        "t_10": int(t_10),
        "t_11": int(t_11),
        "t_s_20": int(t_s),
        "t_s_conj_02": int(t_s_conj),
        "t_mod_sq_arith": int(t_mod_sq_arith),
        "t_mod_sq_module": int(t_mod_sq_module),
        "calib_lhs": int(lhs),
        "calib_rhs": int(rhs),
        "calib_predicate_holds": bool(predicate_holds),
        "element_is_zero_exact": bool(element_is_zero_exact),
        "neg_lhs": int(neg_lhs),
        "neg_rhs": int(neg_rhs),
        "neg_admissible": bool(neg_admissible),
        "anchor_phrase_found": anchor_phrase_found,
        "anchor_line": anchor_line,
        "canon_audit_sha_found": bool(canon_audit_found),
        # The pinned cross-check: reproduces element=0 EXACTLY (1 != 0 mod 3),
        # module agrees t(|s|^2)=0, and the negative is center-admissible.
        "ok": bool(
            element_is_zero_exact
            and (t_mod_sq_arith == 0 == t_mod_sq_module)
            and neg_admissible
            and anchor_phrase_found
        ),
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

    [AUDIT] gate: NO schema-v2 3-tuple (no directional pre-registration of its
    own — the zero-claim in the substitution chain is the CALIBRATION's content,
    re-derived as cross-check). Pass NO sign/magnitude/regime fields.
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

    # 1a. Verify the s100a verdict-file SHA matches the plan-freeze pin (drift guard).
    s100a_rel = "computations/session-100a/s100a_gate_verdicts.txt"  # (local)
    s100a_runtime_sha = pins.get(s100a_rel, "")  # (local)
    s100a_pin_ok = s100a_runtime_sha == S100A_VERDICT_SHA_PIN  # (local)
    print(
        f"  s100a verdict SHA pin match: {s100a_pin_ok} "
        f"(runtime {s100a_runtime_sha[:16]}... vs pin {S100A_VERDICT_SHA_PIN[:16]}...)"
    )

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Conjuncts.
    a = check_module_present()  # (local)
    print(f"[conjunct a] module present + detector in registry: {a['ok']}  {a}")
    bc = run_module_selftest()  # (local)
    print(f"[conjunct b+c] module --self-test programmatic: {bc['ok']}")
    print(f"    positive flags: {bc['positive_flags']}")
    print(f"    negative flags: {bc['negative_flags']} (expect [])")
    print(f"    selftest exit code: {bc['selftest_exit_code']}")
    d = w2_2_mod3_crosscheck()  # (local)
    print(f"[conjunct d] W2-2 mod-3 cross-check: {d['ok']}")
    print(
        f"    t(1,0)={d['t_10']} t(1,1)={d['t_11']} t(|s|^2)={d['t_mod_sq_arith']} "
        f"(module {d['t_mod_sq_module']}); calib {d['calib_lhs']} != {d['calib_rhs']} "
        f"mod 3 -> element=0 exact: {d['element_is_zero_exact']}"
    )
    print(
        f"    neg fixture: t(1,1)={d['neg_lhs']} == (t(1,0)+t_s) mod 3 = {d['neg_rhs']} "
        f"-> admissible: {d['neg_admissible']}"
    )
    print(f"    anchor companion row :40 found on disk: {d['anchor_phrase_found']}")

    # 3. Verdict = behavioral conjunction (audit-class; PASS iff all conjuncts).
    all_ok = bool(a["ok"] and bc["ok"] and d["ok"] and s100a_pin_ok)  # (local)
    verdict = "PASS" if all_ok else "FAIL"  # (local)

    # 4. npz (keys: fixture_results, triality_table, pattern_set, severity_pin).
    fixture_results = {
        "positive_flags": bc["positive_flags"],
        "negative_flags": bc["negative_flags"],
        "positive_flagged_violation": bc["positive_flagged_violation"],
        "negative_zero_findings": bc["negative_zero_findings"],
        "selftest_exit_code": bc["selftest_exit_code"],
    }  # (local)
    triality_table = {
        # calibration element <(1,0)| |s(h)|^2 |(1,1)>
        "calib_t_bra_10": d["t_10"],
        "calib_t_ket_11": d["t_11"],
        "calib_t_op_modsq": d["t_mod_sq_arith"],
        "calib_lhs": d["calib_lhs"],
        "calib_rhs": d["calib_rhs"],
        "calib_predicate_holds": d["calib_predicate_holds"],
        "calib_element_zero_exact": d["element_is_zero_exact"],
        # operator |s(h)|^2 character provenance: s in (2,0), conj(s) in (0,2)
        "op_t_s_20": d["t_s_20"],
        "op_t_s_conj_02": d["t_s_conj_02"],
        # positive fixture (same as calibration)
        "pos_t_bra_10": d["t_10"],
        "pos_t_ket_11": d["t_11"],
        "pos_t_op_modsq": d["t_mod_sq_arith"],
        # negative fixture <(1,1)| s(h) |(1,0)>, s in (2,0)
        "neg_t_bra_11": d["neg_lhs"],
        "neg_t_ket_10": d["t_10"],
        "neg_t_op_s20": d["t_s_20"],
        "neg_lhs": d["neg_lhs"],
        "neg_rhs": d["neg_rhs"],
        "neg_admissible": d["neg_admissible"],
    }  # (local)
    pattern_set = {
        "braket_ascii": MFA._PAT_BRAKET_ASCII.pattern,
        "braket_unicode": MFA._PAT_BRAKET_UNICODE.pattern,
        "prose": MFA._PAT_PROSE.pattern,
        "op_declared_irrep": MFA._PAT_OP_DECLARED_IRREP.pattern,
        "op_mod_squared": MFA._PAT_OP_MOD_SQUARED.pattern,
        "sector_label": MFA._PAT_SECTOR_LABEL.pattern,
    }  # (local)
    severity_pin = {
        "rule_status": MFA.SELECTION_RULE_PREFLIGHT_STATUS,
        "severity_under_status": MFA._current_severity().value,
        "note": "S2 advisory under SUGGESTION K=1; S1 only on rule K=3 MANDATORY promotion (NOT auto-promoted)",
    }  # (local)

    np.savez(
        OUT_NPZ,
        fixture_results=np.array(json.dumps(fixture_results), dtype=object),
        triality_table=np.array(json.dumps(triality_table), dtype=object),
        pattern_set=np.array(json.dumps(pattern_set), dtype=object),
        severity_pin=np.array(json.dumps(severity_pin), dtype=object),
        # convenience plain-int copies for direct numeric inspection
        triality_calib=np.array(
            [d["t_10"], d["t_11"], d["t_mod_sq_arith"], d["calib_lhs"], d["calib_rhs"]],
            dtype=np.int64,
        ),
        verdict=np.array(verdict, dtype=object),
    )
    print(f"\n  npz written: {OUT_NPZ.name} "
          f"(keys: fixture_results, triality_table, pattern_set, severity_pin)")

    # 5. 4-tuple + verdict payload.
    value_str = (
        f"module_present={a['ok']};pos_flag=SELECTION-RULE-PREFLIGHT-VIOLATION;"
        f"neg_findings={len(bc['negative_flags'])};"
        f"t(1,0)={d['t_10']},t(1,1)={d['t_11']},t(|s|^2)={d['t_mod_sq_arith']};"
        f"calib {d['calib_lhs']}!={d['calib_rhs']}mod3=>element=0_exact={d['element_is_zero_exact']};"
        f"neg_admissible={d['neg_admissible']};selftest_rc={bc['selftest_exit_code']};"
        f"severity={severity_pin['severity_under_status']}_K1_SUGGESTION;"
        f"calib_anchor=s100a:40_audit871573da729c5972"
    )  # (local)
    tag = (f"(value={value_str!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    companion = (
        "inaugural _machinery_feasibility_audit.py created (queued-entity PRU Class-8 fix-now); "
        "detect_selection_rule_preflight in registry; W2-2 center-Z3/triality screen; "
        "calibration s100a:36 audit 871573da729c5972, companion :40 element=0 exact"
    )  # (local)
    extra = [
        f"# triality: t(1,0)=1 t(1,1)=0 t(|s(h)|^2)=0 -> center selection 1 != (0+0) mod 3 "
        f"=> <(1,0)| |s|^2 |(1,1)> = 0 EXACTLY; s(h) in (2,0) t=2 connects (NEG fixture admissible) "
        f"# {GATE_ID}",
        f"# severity_pin=S2 advisory under SUGGESTION K=1 (rule W8b-1); S1 only on K=3 MANDATORY; "
        f"NOT auto-promoted # {GATE_ID}",
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
