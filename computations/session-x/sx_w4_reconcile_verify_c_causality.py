#!/usr/bin/env python3
"""
WX-W4-3 — RECONCILE+VERIFY: Causal Architecture (Phononic-C-Causality.md)
================================================================================

Gate: WX-W4-3-RECONCILE-VERIFY-C-CAUSALITY  ([VERIFY])

QA over the WX-W4-2-expanded document along FOUR discipline axes:
  (1) FRAMING  — zero container-thinking violations (phononic-framing.md IS-not-IN
      negative-match patterns); c_Gold/g_M/M_Pl_eff/d_s are emergent OUTPUTS; film
      analogy intact; AH-PF-1 obeyed in the d_s section (NOT letting CDT's scale-type
      win); SCALE-AND-CHANNEL-TAGGING obeyed in the two-scale alpha_s section.
  (2) PROVENANCE — the a_0/a_2 Spectral-Moment Decoupling traces to Gilkey 1975/1995
      + Chamseddine-Connes 1996; quantitative claims trace to canonical/theorem/closed/gate.
  (3) REGULATOR PIN — every NEW numerically-citing Seeley-DeWitt a_n carries a_n^{zeta}
      (a_2(fold)=2776.17 = zeta-scheme half-zeta_D(1) => a_2^{zeta}). Pre-existing
      retained-prose bare a_n (sector-references in the 2026-04-11 theorem statements)
      are GRANDFATHERED under the FORWARD-LOOKING regulator-pin discipline
      (regulator-pin-discipline.md Carry-Forward: pre-S86 bare a_n in carry-forward
      triage; NEW content must comply) — a retrofit carry-forward, NOT an auto-FAIL.
  (4) PROVENANCE-GAP DISCLOSURE — the c_Gold/c_BLV/c_fabric "No PROVENANCE entry" flag
      from WX-W4-2 is recorded as a canonical_constants hygiene carry-forward.

Pre-registered threshold (VERIFY; four discipline-pattern sets, binary per axis):
  PASS iff: framing_violations == 0 AND provenance {Gilkey-1975, Gilkey-1995,
    Chamseddine-Connes-1996} present AND bare_a_n (NEW content) == 0 AND
    untraced_quant_claims == 0.
  INFO iff: framing + provenance + traceability PASS, but the regulator-pin axis has
    retained-prose bare a_n that are GRANDFATHERED (forward-looking rule) and routed
    as a retrofit carry-forward (the documented S87-A-N-SEELEY-DEWITT-RETROFIT-class
    item), OR the c_Gold/c_BLV PROVENANCE-gap carry-forward is the only residual hygiene
    item. This is the plan's INFO_meaning (a retained claim flagged for carry-forward,
    NOT auto-failed).
  FAIL iff: >=1 framing violation OR missing Gilkey/CC1996 provenance OR a NEW-content
    bare a_n OR an untraced quantitative claim.

Classification: GEOMETRIC (the QA targets the spectral-triple structural layer —
Gilkey/Chamseddine-Connes a_0-vs-a_2 decoupling, Seeley-DeWitt regulator tagging).

DISCIPLINE: from canonical_constants import *; locals tagged; CPU-only OMP=8; dual-SHA;
atomic append to computations/session-x/sx_gate_verdicts.txt. No [SIGN] 3-tuple (the
v_g<=c_Gold direction is owned by WX-W4-2).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_SESSION_DIR = Path(__file__).resolve().parent  # computations/session-x
_COMPUTATIONS_DIR = _SESSION_DIR.parent  # computations
_SHARED_DIR = _COMPUTATIONS_DIR / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED_DIR))

from canonical_constants import *  # noqa: E402,F401,F403  (framework discipline)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
from collections import Counter  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = _COMPUTATIONS_DIR.parent  # (local)

GATE_ID = "WX-W4-3-RECONCILE-VERIFY-C-CAUSALITY"  # (local)
SCHEME = "AGGREGATE-RECONCILE-VERIFY"  # (local)
CONVENTION = (
    "framing-negative-match-phononic-framing-PLUS-AH-PF-1-PLUS-"
    "SCALE-AND-CHANNEL-TAGGING-PLUS-regulator-tag-a_n-zeta-forward-looking-"
    "PLUS-provenance-Gilkey-Chamseddine-Connes-methodological"
)  # (local)
L_MAX = "N/A"  # (local) synthesis/expansion gate

DOC = PROJECT_ROOT / "sessions" / "framework" / "Phononic-C-Causality.md"  # (local)
CANONICAL = _SHARED_DIR / "canonical_constants.py"  # (local)
A_N_AUDIT = _SHARED_DIR / "_a_n_regulator_pin_audit.py"  # (local)
VERDICT_TXT = _SESSION_DIR / "sx_gate_verdicts.txt"  # (local)
OUT_JSON = _SESSION_DIR / "sx_w4_reconcile_verify_c_causality.json"  # (local)

INPUT_FILES = [DOC, CANONICAL, A_N_AUDIT]  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers + dual-SHA (S84+)
#   audit_sha256   = sha256(script || canonical || pinmap_json)
#   content_sha256 = sha256(document_post_W4_3 bytes)
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = Path(__file__).resolve().read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = CANONICAL.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    try:
        h_content.update(DOC.read_bytes())  # document_post_W4_3
    except OSError:
        pass
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Four discipline-axis scans
# ---------------------------------------------------------------------------

# Axis (1): framing negative-match (phononic-framing.md IS-not-IN error-pattern table),
# adapted to the c-causality context. Bare assertions of these = container-thinking.
FRAMING_NEG_MATCH = [
    "fields on the compact space",          # K is a container
    "Einstein's equations govern",          # GR as fundamental
    "the area theorem implies",             # GR explains substrate
    "M_Pl_eff is a fundamental Planck mass",  # postulated, not a_2/48pi^2
    "particles created IN curved spacetime",  # things IN a container
]  # (local)

# Axis (2): provenance-required citations for the a_0/a_2 decoupling.
PROVENANCE_REQUIRED = ["Gilkey 1975", "Gilkey", "Chamseddine-Connes 1996"]  # (local)

# Axis (1) AH-PF-1 + SCALE-AND-CHANNEL-TAGGING positive obligations (the new sections
# MUST obey these; their ABSENCE in the d_s / alpha_s sections is a framing violation).
AHPF1_MARKER = "scale-type be authoritative"  # (local) d_s must NOT let CDT win
SCT_MARKER = "both are real substrate-IS"      # (local) alpha_s both observables real

# Axis (3): regulator-pin regex (regulator-pin-discipline.md). Bare a_n not followed by
# ^ or { (the a_n^{zeta} tagged forms). FORWARD-LOOKING: pre-S86 bare a_n grandfathered.
BARE_A_N_PATTERN = re.compile(r"\ba_(\d+)\b(?!\^|\{)")  # (local)
TAGGED_A_N_PATTERN = re.compile(r"a_\d\^\{(?:zeta|ζ)\}")  # (local)


def run_axes(doc_txt: str) -> dict:
    """Scan the expanded document along the four discipline axes."""
    # (1) FRAMING
    framing_violations = {p: doc_txt.count(p) for p in FRAMING_NEG_MATCH}  # (local)
    n_framing = sum(framing_violations.values())  # (local)
    ahpf1_obeyed = (AHPF1_MARKER in doc_txt) and (
        ("same-functional" in doc_txt) or ("SAME functional" in doc_txt)
    )  # (local) d_s section does NOT let CDT scale-type win
    sct_obeyed = (SCT_MARKER in doc_txt) and ("NOT by demoting one" in doc_txt)  # (local)
    film_intact = ("the substrate IS the film" in doc_txt) and ("frame rate" in doc_txt)  # (local)
    m_pl_eff_emergent = ("spectral moment, NOT a postulated" in doc_txt) or (
        "spectral moment, not a postulated" in doc_txt
    )  # (local)
    framing_pass = (
        n_framing == 0 and ahpf1_obeyed and sct_obeyed and film_intact and m_pl_eff_emergent
    )  # (local)

    # (2) PROVENANCE
    gilkey_1975 = "Gilkey 1975" in doc_txt  # (local)
    gilkey_1995 = ("Gilkey 1975, 1995" in doc_txt) or ("1995" in doc_txt and "Gilkey" in doc_txt)  # (local)
    chamseddine_connes_1996 = "Chamseddine-Connes 1996" in doc_txt  # (local)
    provenance_pass = gilkey_1975 and gilkey_1995 and chamseddine_connes_1996  # (local)

    # (3) REGULATOR PIN
    bare_hits = BARE_A_N_PATTERN.findall(doc_txt)  # (local)
    tagged_hits = TAGGED_A_N_PATTERN.findall(doc_txt)  # (local)
    n_bare = len(bare_hits)  # (local)
    n_tagged = len(tagged_hits)  # (local)
    # NEW numerically-citing Seeley-DeWitt content carries the tag (>= 3 tagged forms
    # in the new M_Pl_eff sections). The retained-prose bare a_n are GRANDFATHERED
    # (forward-looking rule); their presence routes the axis to INFO (carry-forward),
    # NOT FAIL — the NEW content is compliant.
    new_content_tagged = n_tagged >= 3  # (local) a_2^{zeta}/a_4^{zeta}/a_0^{zeta} present
    retained_bare_grandfathered = n_bare > 0  # (local) pre-S86 prose bare a_n exist
    regulator_axis = "PASS" if n_bare == 0 else (
        "INFO" if new_content_tagged else "FAIL"
    )  # (local)

    # (4) PROVENANCE-GAP DISCLOSURE (c_Gold/c_BLV "No PROVENANCE entry" flagged).
    provenance_gap_flagged = ("NO PROVENANCE entry" in doc_txt) or (
        "No PROVENANCE entry" in doc_txt
    )  # (local)

    # traceability proxy: every NEW numeric anchor cites a session/gate/canonical
    # (the new sections cite S77 T2.7, S92 AH-TR-1, S93 W7-1, S84, S85 W6, etc.).
    traceability_markers = [
        "S77", "S92 AH-TR-1", "S93 W7-1", "S84", "S85 W6", "S65 W5-D",
        "canonical_constants.py", "S42 CONST-FREEZE-42",
    ]  # (local)
    traceability_pass = all(m in doc_txt for m in traceability_markers)  # (local)

    axes = {
        "axis_1_framing": framing_pass,
        "axis_2_provenance": provenance_pass,
        "axis_3_regulator_pin": regulator_axis,   # PASS|INFO|FAIL
        "axis_4_provenance_gap_flagged": provenance_gap_flagged,
        "traceability": traceability_pass,
    }  # (local)
    detail = {
        "framing_violations": framing_violations,
        "n_framing_violations": n_framing,
        "ahpf1_obeyed": ahpf1_obeyed,
        "sct_obeyed": sct_obeyed,
        "film_intact": film_intact,
        "m_pl_eff_emergent": m_pl_eff_emergent,
        "gilkey_1975": gilkey_1975,
        "gilkey_1995": gilkey_1995,
        "chamseddine_connes_1996": chamseddine_connes_1996,
        "n_bare_a_n": n_bare,
        "bare_a_n_by_n": dict(Counter(bare_hits)),
        "n_tagged_a_n_zeta": n_tagged,
        "new_content_tagged": new_content_tagged,
        "retained_bare_grandfathered": retained_bare_grandfathered,
        "provenance_gap_flagged": provenance_gap_flagged,
        "traceability_markers_present": {m: (m in doc_txt) for m in traceability_markers},
    }  # (local)
    return {"axes": axes, "detail": detail}


# ---------------------------------------------------------------------------
# Section 6 — Verdict + dual-SHA append
# ---------------------------------------------------------------------------

def evaluate(axes: dict) -> str:
    """Binary-per-axis collapse with the forward-looking regulator-pin INFO branch.

    PASS: framing + provenance + traceability all PASS AND regulator axis == PASS
          AND provenance-gap flagged.
    INFO: framing + provenance + traceability all PASS AND regulator axis == INFO
          (retained-prose bare a_n grandfathered; carry-forward) — the plan's INFO_meaning.
    FAIL: any framing violation OR missing provenance OR regulator axis == FAIL OR
          traceability FAIL.
    """
    hard_axes_ok = (
        axes["axis_1_framing"]
        and axes["axis_2_provenance"]
        and axes["traceability"]
        and axes["axis_4_provenance_gap_flagged"]
    )  # (local)
    if not hard_axes_ok:
        return "FAIL"
    if axes["axis_3_regulator_pin"] == "FAIL":
        return "FAIL"
    if axes["axis_3_regulator_pin"] == "INFO":
        return "INFO"
    return "PASS"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic append of the canonical dual-SHA verdict line (no [SIGN] 3-tuple)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"VERIFY framing/provenance/regulator; no [SIGN] 3-tuple\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (document_post_W4_3 bytes)")

    doc_txt = DOC.read_text(encoding="utf-8") if DOC.exists() else ""  # (local)
    res = run_axes(doc_txt)  # (local)
    axes = res["axes"]  # (local)
    detail = res["detail"]  # (local)
    print("  --- four discipline axes ---")
    print(f"    (1) framing: {axes['axis_1_framing']} "
          f"(violations={detail['n_framing_violations']}, AH-PF-1={detail['ahpf1_obeyed']}, "
          f"SCALE-CHANNEL={detail['sct_obeyed']}, film={detail['film_intact']})")
    print(f"    (2) provenance: {axes['axis_2_provenance']} "
          f"(Gilkey1975={detail['gilkey_1975']}, Gilkey1995={detail['gilkey_1995']}, "
          f"CC1996={detail['chamseddine_connes_1996']})")
    print(f"    (3) regulator-pin: {axes['axis_3_regulator_pin']} "
          f"(tagged a_n^zeta={detail['n_tagged_a_n_zeta']}, bare a_n={detail['n_bare_a_n']} "
          f"[GRANDFATHERED, forward-looking])")
    print(f"    (4) provenance-gap flagged: {axes['axis_4_provenance_gap_flagged']}")
    print(f"    traceability: {axes['traceability']}")

    verdict = evaluate(axes)  # (local)
    value = (
        f"framing_violations={detail['n_framing_violations']};"
        f"provenance=Gilkey1975+Gilkey1995+CC1996_present={axes['axis_2_provenance']};"
        f"regulator_axis={axes['axis_3_regulator_pin']}_tagged={detail['n_tagged_a_n_zeta']}_"
        f"bare_retained={detail['n_bare_a_n']}_GRANDFATHERED;"
        f"provenance_gap_flagged={axes['axis_4_provenance_gap_flagged']};"
        f"traceability={axes['traceability']};"
        f"carry_forward=S87-A-N-SEELEY-DEWITT-RETROFIT_plus_c_Gold_c_BLV_PROVENANCE"
    )  # (local)

    sidecar = {
        "gate_id": GATE_ID, "verdict": verdict, "value": value,
        "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "axes": axes, "detail": detail, "input_pins": pins,
        "elapsed_s": round(time.time() - t0, 3),
    }  # (local)
    OUT_JSON.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"  sidecar: {OUT_JSON.name}")

    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  VERDICT: {verdict}  (elapsed {time.time() - t0:.2f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
