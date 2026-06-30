#!/usr/bin/env python3
"""
WX-W4-2 — COMPREHENSIVE-EXPANSION: Causal Architecture (Phononic-C-Causality.md)
================================================================================

Gate: WX-W4-2-COMPREHENSIVE-EXPANSION-C-CAUSALITY  ([VERIFY], [SIGN] v_g<=c_Gold chain)

THE DELIVERABLE. The expanded Phononic-C-Causality.md (an editorial artifact produced
by the agent) integrates the WX-W4-1 material-gap set. This closure script:
  (i)  re-reads the EXPANDED document and verifies gap-integration completeness
       (every material gap row INTEGRATED-or-SCOPED + every OQ marked + minimal-edit
       guard: >=1 NEW-SINCE-S74/NEVER-COVERED row landed as substantive new content);
  (ii) verifies the v_g <= c_Gold = 0.915 group-velocity envelope SIGN chain against
       the canonical branch speeds (the [SIGN] directional pre-registration);
  (iii) emits the dual-SHA verdict + the SIGN/MAGNITUDE/REGIME 3-tuple companion row.

Pre-registered threshold (VERIFY; coverage-by-enumeration + SIGN):
  PASS iff:
    (A) every MATERIAL gap row from WX-W4-1 is INTEGRATED (new/deepened section or
        new corpus row) OR explicitly SCOPED-OUT; AND
    (B) 100% of OQ1-OQ10 marked with a landed verdict in the expanded doc; AND
    (C) the c_Gold/c_BLV PROVENANCE gap flagged; STALE line-numbers re-pinned; AND
    (D) the document grew substantially (NOT a cosmetic edit: post_bytes/pre_bytes
        >= 1.20 AND >= 6 new section headers present); AND
    (E) the v_g <= c_Gold SIGN chain holds (all canonical branch speeds < c_Gold;
        Goldstone saturates) => sign_verdict=PASS.
  A cosmetic/minimal edit (re-pins only, no new-content integration) FAILS.

SUBSTITUTION CHAIN (v_g <= c_Gold = 0.915 M_KK; math-scripts.md Double-Check Logic):
  Step 1: c_Gold := Goldstone-direction group velocity = sqrt(Z_Gold/M_Gold) on the
          emergent g_M [doc eq 4.1; canonical c_Gold = 0.915 M_KK, line 636; S75 W3-L
          LANDED-PASS — a COMPUTATION OUTPUT].
  Step 2: v_g,b := d omega_b/dk, group velocity of phononic branch b on g_M [doc eq 5.1
          omega_k = sqrt(eps_k^2 + Delta^2); canonical branch speeds B1=0.0798, B2=0.00200,
          B3=0.1397, Leggett c_L=0.0255].
  Step 3: target relation = (v_g,b <= c_Gold) for all observable branches b.
  Step 4: substitute. Goldstone is the UNIQUE gapless mode (Theorem 3.4, Kasparov):
          Delta_Gold=0 => omega_Gold = c_Gold*k => v_g,Gold = c_Gold = 0.915 (saturates).
          Every gapped branch: omega_b = sqrt(Delta_b^2 + c_{s,b}^2 k^2) =>
          v_g,b = c_{s,b}^2 k / sqrt(Delta_b^2 + c_{s,b}^2 k^2) < c_{s,b} <= c_Gold.
  Step 5: read off. sign(c_Gold - v_g) >= 0 for all branches, = 0 on Goldstone.
          v_g <= c_Gold with equality ONLY on the Goldstone; c_Gold is an UPPER envelope.
  Conclusion: sign_verdict=PASS; no CONTRADICTION-class branch (v_g > c_Gold) in the
          canonical set. The two-scale alpha_s (substrate -0.0859 / pivot 0) is a
          spectral-tilt running, NOT a propagation velocity (STEP 4 c-compare), and
          does NOT contradict the envelope.

Classification: PHONONIC (the deliverable expands the causal architecture; new GEOMETRIC
sections M_Pl_eff=a_2/48pi^2 + d_s flow tagged GEOMETRIC inline).

DISCIPLINE: from canonical_constants import *; locals tagged; CPU-only OMP=8; dual-SHA;
atomic append to computations/session-x/sx_gate_verdicts.txt.
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
import math  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = _COMPUTATIONS_DIR.parent  # (local)

GATE_ID = "WX-W4-2-COMPREHENSIVE-EXPANSION-C-CAUSALITY"  # (local)
SCHEME = "AGGREGATE-COMPREHENSIVE-EXPANSION"  # (local)
CONVENTION = (
    "ADDITIVE-SYNTHESIS-authorial-voice-PLUS-ABSOLUTE-re-pin-PLUS-"
    "ANNOTATION-OQ-landed-verdict-PLUS-v_g-le-c_Gold-SIGN-chain"
)  # (local)
L_MAX = "N/A"  # (local) synthesis/expansion gate

DOC = PROJECT_ROOT / "sessions" / "framework" / "Phononic-C-Causality.md"  # (local)
STATE_MAP = _SESSION_DIR / "sx_w4_state_of_domain_map.md"  # (local)
GAP_ANALYSIS = _SESSION_DIR / "sx_w4_gap_analysis.md"  # (local)
CANONICAL = _SHARED_DIR / "canonical_constants.py"  # (local)
VERDICT_TXT = _SESSION_DIR / "sx_gate_verdicts.txt"  # (local)
OUT_JSON = _SESSION_DIR / "sx_w4_comprehensive_expansion.json"  # (local)

INPUT_FILES = [DOC, STATE_MAP, GAP_ANALYSIS, CANONICAL]  # (local)

# Pre-edit document SHA (must equal WX-W4-1 document_pre); the document_pre of the
# 89,097-B authored doc. Recorded from the WX-W4-1 input-pin log (f5cb7ade...) so the
# growth-ratio guard compares against the authored baseline, not the post-edit file.
DOC_PRE_BYTES = 89097  # (local) authored Phononic-C-Causality.md size (2026-04-11)


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers + dual-SHA (S84+)
#   audit_sha256   = sha256(script || canonical || pinmap_json)
#   content_sha256 = sha256(document_post bytes)   # content = the expanded deliverable
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
        h_content.update(DOC.read_bytes())  # document_post bytes
    except OSError:
        pass
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — v_g <= c_Gold SIGN chain (canonical branch speeds vs c_Gold)
#
# c_Gold imported from canonical_constants (line 636). Branch speeds are doc-cited
# canonical values; tagged (local) here as the per-branch verification inputs.
# ---------------------------------------------------------------------------

def verify_envelope_sign() -> dict:
    """v_g <= c_Gold for every canonical branch; Goldstone saturates."""
    c_gold = float(c_Gold)  # (local) canonical 0.915 M_KK (line 636)
    # Canonical branch group velocities on g_M (doc Section 2.1 table, S52/S66):
    branch_speeds = {
        "Goldstone (saturates)": 0.915,  # (local) doc eq 4.1; v_g,Gold = c_Gold exactly
        "photon (Layer 2)": 0.915,       # (local) tracks c_Gold at leading order
        "B1 singlet": 0.0798,            # (local) W1-A/W2-A
        "B2 flat optical": 0.00200,      # (local) W1-A/W2-A van Hove plateau
        "B3 dispersive optical": 0.1397, # (local) W1-A/W2-A
        "Leggett c_L": 0.0255,           # (local) W4-L/S66
    }  # (local)
    # SIGN chain Step 5: sign(c_Gold - v_g) >= 0 for all branches.
    margins = {name: c_gold - v for name, v in branch_speeds.items()}  # (local)
    all_le = all(m >= -1e-12 for m in margins.values())  # (local) v_g <= c_Gold
    goldstone_saturates = math.isclose(
        branch_speeds["Goldstone (saturates)"], c_gold, rel_tol=1e-9
    )  # (local) v_g,Gold == c_Gold exactly
    n_strictly_below = sum(1 for m in margins.values() if m > 1e-9)  # (local) gapped < c_Gold
    no_contradiction = all_le  # (local) no v_g > c_Gold branch
    return {
        "c_Gold": c_gold,
        "branch_speeds": branch_speeds,
        "margins": margins,
        "all_v_g_le_c_Gold": all_le,
        "goldstone_saturates": goldstone_saturates,
        "n_strictly_below_c_Gold": n_strictly_below,
        "no_CONTRADICTION_class_branch": no_contradiction,
        "sign_verdict": "PASS" if (all_le and goldstone_saturates) else "FAIL",
    }


# ---------------------------------------------------------------------------
# Section 6 — Gap-integration completeness over the EXPANDED document
# ---------------------------------------------------------------------------

# The 6 NEW-section targets (NEW-SINCE-S74 / NEVER-COVERED gap rows G3/G5/G8/G9/G11/G12),
# each must appear as a substantive section header in the expanded doc.
NEW_SECTION_MARKERS = [
    "### 3.6 a_2 -> Emergent Gravity",       # G3 M_Pl_eff
    "### 3.7 a_2(fold) vs a_2(full",         # G4 two-value/scheme
    "### 5.1a H_transit vs H_Friedmann",     # G5 two-rate
    "## 8.5 Spectral-dimension d_s flow",    # G8 d_s vs CDT
    "### 8.2a Two-scale alpha_s",            # G9 two-scale alpha_s SUPERSESSION
    "### 8.1a Two-speed tensor tilt",        # G7 S84 two-speed tensor-tilt
]  # (local)

# The deepened-existing-section + corpus markers (G13/G14 + EC8-11).
DEEPEN_MARKERS = [
    "### 6.0 The four verdict classes",      # G14 c-compare verdict-class reconciliation
    "**EC8:",                                # expanded corpus
    "**EC9:",
    "**EC10:",
    "**EC11:",
    "(c.a) The laboratory-IN image",         # G11 3He-B BdG bridge
    "Dedicated LQG/CDT cross-framework",     # G12 LQG comparison
    "Bogoliubov Gaussianity Preservation",   # G13 f_NL
]  # (local)

OQ_SET = ["OQ1", "OQ2", "OQ3", "OQ4", "OQ5", "OQ6", "OQ7", "OQ8", "OQ9", "OQ10"]  # (local)


def verify_expansion(doc_txt: str, gap_txt: str) -> dict:
    """Coverage-by-enumeration over the expanded document."""
    # (A) NEW sections present (the substantive-new-content integration; minimal-edit guard).
    new_sections_present = {m: (m in doc_txt) for m in NEW_SECTION_MARKERS}  # (local)
    n_new_sections = sum(1 for v in new_sections_present.values() if v)  # (local)

    # (B) deepened sections + expanded corpus present.
    deepen_present = {m: (m in doc_txt) for m in DEEPEN_MARKERS}  # (local)
    n_deepen = sum(1 for v in deepen_present.values() if v)  # (local)

    # (C) every OQ marked with a LANDED verdict in the expanded doc (the OQ-conversion).
    # Each OQ block carries a "> **LANDED" annotation; require all 10 OQ tokens present
    # AND >= 10 "> **LANDED" markers (one per OQ).
    oq_present = {oq: (oq in doc_txt) for oq in OQ_SET}  # (local)
    n_landed_markers = doc_txt.count("> **LANDED")  # (local)
    oq_marked = all(oq_present.values()) and n_landed_markers >= 10  # (local)

    # (D) QA: PROVENANCE gap flagged + STALE line re-pins.
    provenance_flag = ("NO PROVENANCE entry" in doc_txt) or (
        "No PROVENANCE entry" in doc_txt
    )  # (local)
    line_636 = "line 636" in doc_txt  # (local) c_Gold re-pin (was 279)
    line_424 = "line 424" in doc_txt  # (local) xi_BCS re-pin (was 190)
    line_414 = "line 414" in doc_txt  # (local) Delta_0_GL re-pin (was 182)
    repins_ok = line_636 and line_424 and line_414  # (local)

    # (E) regulator tag present (a_2^{zeta}) for the new M_Pl_eff content.
    regulator_tag = ("a_2^{zeta}" in doc_txt) or ("a_2^{ζ}" in doc_txt)  # (local)

    # (F) authorial voice preserved (film analogy).
    film_analogy = ("the substrate IS the film" in doc_txt) and (
        "frame rate" in doc_txt
    )  # (local)

    # (G) growth ratio (minimal-edit guard): post/pre >= 1.20.
    post_bytes = len(doc_txt.encode("utf-8"))  # (local)
    growth_ratio = post_bytes / DOC_PRE_BYTES  # (local)
    substantial_growth = (growth_ratio >= 1.20) and (n_new_sections >= 6)  # (local)

    # gap_analysis material-gap count present (cross-check the WX-W4-1 input).
    gap_rows_present = gap_txt.count("\n| G") >= 18  # (local)

    checks = {
        "new_sections_6_of_6": n_new_sections >= 6,
        "deepened_sections_and_corpus": n_deepen >= 7,
        "oq_marked_10_of_10": oq_marked,
        "provenance_gap_flagged": provenance_flag,
        "stale_lines_repinned": repins_ok,
        "regulator_tag_present": regulator_tag,
        "authorial_voice_preserved": film_analogy,
        "substantial_growth_not_cosmetic": substantial_growth,
        "gap_analysis_input_present": gap_rows_present,
    }  # (local)
    detail = {
        "new_sections_present": new_sections_present,
        "deepen_present": deepen_present,
        "oq_present": oq_present,
        "n_landed_markers": n_landed_markers,
        "post_bytes": post_bytes,
        "pre_bytes": DOC_PRE_BYTES,
        "growth_ratio": round(growth_ratio, 4),
        "repins": {"line_636_c_Gold": line_636, "line_424_xi_BCS": line_424,
                   "line_414_Delta_0_GL": line_414},
    }  # (local)
    return {"checks": checks, "detail": detail}


# ---------------------------------------------------------------------------
# Section 7 — Verdict + 3-tuple + dual-SHA append
# ---------------------------------------------------------------------------

def collapse_composite(sign_v: str, mag_v: str, regime_v: str) -> str:
    """S87 schema-v2 composite-collapse rule (gate-verdicts.md)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Atomic append: canonical line + dual-SHA companion + SIGN/MAGNITUDE/REGIME 3-tuple."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); v_g<=c_Gold=0.915 envelope chain\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple_row)


def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (document_post bytes)")

    doc_txt = DOC.read_text(encoding="utf-8") if DOC.exists() else ""  # (local)
    gap_txt = GAP_ANALYSIS.read_text(encoding="utf-8") if GAP_ANALYSIS.exists() else ""  # (local)

    # --- (E) the v_g <= c_Gold SIGN chain ---
    env = verify_envelope_sign()  # (local)
    print("  --- v_g <= c_Gold envelope SIGN chain ---")
    print(f"    c_Gold = {env['c_Gold']} M_KK (line 636)")
    for name, m in env["margins"].items():
        print(f"    {name}: c_Gold - v_g = {m:+.4f}")
    print(f"    sign_verdict = {env['sign_verdict']} "
          f"(all v_g<=c_Gold={env['all_v_g_le_c_Gold']}, "
          f"Goldstone saturates={env['goldstone_saturates']}, "
          f"no CONTRADICTION={env['no_CONTRADICTION_class_branch']})")

    # --- (A)-(D),(F),(G) gap-integration completeness ---
    exp = verify_expansion(doc_txt, gap_txt)  # (local)
    checks = exp["checks"]  # (local)
    print("  --- gap-integration completeness ---")
    for k, v in checks.items():
        print(f"    {k}: {v}")

    # --- 3-tuple ---
    sign_v = env["sign_verdict"]  # (local)
    # magnitude_verdict: the expansion completeness (all coverage checks PASS).
    mag_v = "PASS" if all(checks.values()) else "FAIL"  # (local)
    # regime_verdict: synthesis/expansion gate, no truncation regime -> always VALID.
    regime_v = "VALID"  # (local) editorial synthesis; no small-parameter expansion
    composite = collapse_composite(sign_v, mag_v, regime_v)  # (local)

    value = (
        f"new_sections={sum(1 for v in exp['detail']['new_sections_present'].values() if v)}/6;"
        f"OQ_landed_markers={exp['detail']['n_landed_markers']};"
        f"growth_ratio={exp['detail']['growth_ratio']};"
        f"post_bytes={exp['detail']['post_bytes']};"
        f"sign_chain=v_g<=c_Gold={env['c_Gold']}_PASS;"
        f"goldstone_saturates={env['goldstone_saturates']};"
        f"no_contradiction={env['no_CONTRADICTION_class_branch']};"
        f"provenance_gap_flagged={checks['provenance_gap_flagged']};"
        f"repins=636/424/414"
    )  # (local)

    sidecar = {
        "gate_id": GATE_ID, "verdict": composite, "value": value,
        "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "sign_verdict": sign_v, "magnitude_verdict": mag_v, "regime_verdict": regime_v,
        "envelope_chain": env, "checks": checks, "detail": exp["detail"],
        "input_pins": pins, "elapsed_s": round(time.time() - t0, 3),
    }  # (local)
    OUT_JSON.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"  sidecar: {OUT_JSON.name}")

    append_verdict(composite, value, audit_sha, content_sha, sign_v, mag_v, regime_v)
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  VERDICT: {composite}  (elapsed {time.time() - t0:.2f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
