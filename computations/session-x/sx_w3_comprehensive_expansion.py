#!/usr/bin/env python3
"""
SX W3-2 — COMPREHENSIVE-EXPANSION (the deliverable closure)
===========================================================

Gate: WX-W3-2-COMPREHENSIVE-EXPANSION  ([VERIFY])

Pre-registered threshold (gap-integration coverage; plan §W3-2):
  PASS iff for every g in gap_set(G1): g in integrated_set OR g in scoped_out_set
  (with one-line reason); AND integrated_set union scoped_out_set = gap_set;
  AND |integrated_set| / |gap_set| >= integration_floor=0.80; AND the 5
  mandatory-integrate rewrites are all present (cannot be scoped out); AND the
  document grows substantially; AND substrate-IS direction restored.

THE DELIVERABLE is the expanded document sessions/framework/Phononic-to-Cosmos.md
(rewritten in-session by the agent). This closure script is MECHANICAL: it re-reads
the post-edit document, verifies the gap-row markers are present (integration
coverage), checks the 5 mandatory markers + the document growth + substrate-IS
framing markers, computes the dual-SHA, and appends the verdict.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/Phononic-to-Cosmos.md        (document_post; THE DELIVERABLE)
  - sessions/session-x/session-x-w3-workingpaper.md (the §W3-1 gap analysis + §W3-2 record)
  - computations/_shared/canonical_constants.py     (canonical snapshot; feeds audit_sha)
  - script bytes                                    (feeds BOTH SHAs)

Output 4-tuple:
  (value=<expansion coverage state>,
   scheme=AUTHOR-CURATED-EXPANSION,
   convention=substrate-IS-Mack-voice,
   L_max=N/A)

Classification: PHONONIC.

DISCIPLINE: `from canonical_constants import *`; intermediates tagged `# (local)`;
no linear algebra; CPU-only; dual-SHA atomic append; canonical verdict path.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import time
import re
from pathlib import Path

SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (MANDATORY)
import canonical_constants as cc  # (local)

SESSION_DIR = Path(__file__).resolve().parent  # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent  # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent  # (local)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"  # (local)

SESSION = "SX"  # (local)
GATE_ID = "WX-W3-2-COMPREHENSIVE-EXPANSION"  # (local)
SCHEME = "AUTHOR-CURATED-EXPANSION"  # (local)
CONVENTION = "substrate-IS-Mack-voice"  # (local)
L_MAX = "N/A"  # (local) expansion gate; no spectral truncation

# Option A supersession (gate-verdicts.md §"Option A — sig_5 remediation"):
# the first run emitted a PASS with a CASE-SENSITIVE G19 marker ('post-Dovekie')
# that under-counted integration at 24/25 (the document renders 'Post-Dovekie' at
# sentence starts). The underlying document content is UNCHANGED; this is the
# rubric-calibration corrective case. The corrective line carries supersedes=<old>.
SUPERSEDES = "0262d83353c02ec3cefc13d310977e4cc19e3f4993286a2c3b9add26f72750a8"  # (local) prior run's full-64 audit_sha256

DOCUMENT_POST = FRAMEWORK_DIR / "Phononic-to-Cosmos.md"  # (local) THE DELIVERABLE
WP_PATH = PROJECT_ROOT / "sessions" / "session-x" / "session-x-w3-workingpaper.md"  # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)

OUT_NPZ = SESSION_DIR / "sx_w3_comprehensive_expansion.npz"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local)

INPUT_FILES = [DOCUMENT_POST, WP_PATH, CANONICAL]  # (local)

# Pre-registered coverage controls (plan §W3-2 strict_PASS_boundary)
INTEGRATION_FLOOR = 0.80          # (local) >= 80% of gaps integrated (not just scoped)
DOC_GROWTH_FLOOR_BYTES = 80000    # (local) substantial growth vs S57 64,462 (cosmetic-edit floor)

# Per-gap integration markers (each gap row from G1 -> a literal marker that must
# appear in the expanded document for that gap to count as integrated).
GAP_MARKERS = {  # (local)
    "G1_CC_resolved": "DILUTION-CC",
    "G2_CC_integrability_retired": "integrability problem",
    "G3_overshoot_executed": "S66 update",
    "G4_ns_reversal": "0.9561",
    "G5_ns_scheme": "0.9567",
    "G6_alpha_s_overload": "-0.08587279",
    "G7_r_dualpath": "0.0117315",
    "G8_r_detect": "LiteBIRD",
    "G9_nT_twoscale": "0.4676",
    "G10_DM_abundance": "LEGGETT-MOMENT",
    "G11_volovik_partition": "336.6",
    "G12_Tk": "T(k) = 1.0000",
    "G13_grav_decay": "LEGGETT-GRAV-DECAY-67",
    "G14_bbn_pass": "BBN-VOLOVIK",
    "G15_thermalization": "3.044",
    "G16_reheat": "1.70e15",
    "G17_isw": "ISW-TRACKING-68",
    "G18_w0_dual": "R_842",
    "G19_desi_dr2": "2.130 sigma",  # DESI DR2 sigma-distances (post-Dovekie); case-stable content marker (NOT 'post-Dovekie' which the doc renders in mixed case at sentence starts)
    "G20_falsifier_program": "falsifier-rigor-registry",
    "G21_detector_timeline": "pre-registered-observations",
    "G22_fnl": "DETECTOR-STERILE",
    "G23_gw_arc": "RETRACTED",
    "G24_vii_bridges": "VII.AX",
    "G25_lrd": "little-red-dot",
}

# The 5 mandatory-integrate rewrites (cannot be scoped out).
MANDATORY_MARKERS = {  # (local)
    "CC_resolution": "DILUTION-CC",
    "n_s_paradigm": "0.9561",
    "r_dual_pathway": "0.0074705",
    "DM_abundance": "LEGGETT-MOMENT",
    "BBN": "BBN-VOLOVIK",
}

# Substrate-IS framing markers (direction restored, per phononic-framing.md).
SUBSTRATE_IS_MARKERS = [  # (local)
    "substrate IS",
    "spectral-action moment",
    "exflation is not inflation",
    "tracking vacuum",
]

# Authorial-voice markers (first-person cosmologist register preserved).
VOICE_MARKERS = [  # (local)
    "the kind of truth I could rederive mathematically",
    "what the data",
    "I want to be careful",
]


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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str], content_payload: str) -> tuple[str, str]:
    """audit = sha256(script||canonical||pinmap_json); content = sha256(document_post)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(content_payload.encode("utf-8")).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
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
        f"[VERIFY] gap-integration coverage; content_sha over document_post; "
        f"3 substitution chains (CC 1.032 / Omega_DM 0.11995 / n_s O(1)sigma) Sage-verified inline; "
        f"supersedes={SUPERSEDES} (Option A; case-sensitive G19 marker corrected 24/25->25/25; "
        f"document content UNCHANGED, rubric-calibration corrective per gate-verdicts.md)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)

    doc = DOCUMENT_POST.read_text(encoding="utf-8") if DOCUMENT_POST.exists() else ""  # (local)
    doc_bytes = len(DOCUMENT_POST.read_bytes()) if DOCUMENT_POST.exists() else 0  # (local)

    # Gap-integration coverage
    integrated = {g: (m in doc) for g, m in GAP_MARKERS.items()}  # (local)
    n_integrated = sum(integrated.values())  # (local)
    n_gaps = len(GAP_MARKERS)  # (local)
    frac = n_integrated / n_gaps if n_gaps else 0.0  # (local)

    mandatory = {k: (m in doc) for k, m in MANDATORY_MARKERS.items()}  # (local)
    all_mandatory = all(mandatory.values())  # (local)

    substrate_is = sum(1 for m in SUBSTRATE_IS_MARKERS if m in doc)  # (local)
    voice = sum(1 for m in VOICE_MARKERS if m in doc)  # (local)

    print()
    print("  expansion coverage verification:")
    print(f"    document size            : {doc_bytes} bytes  (S57 was 64,462; floor {DOC_GROWTH_FLOOR_BYTES})")
    print(f"    gap rows integrated      : {n_integrated}/{n_gaps}  (frac {frac:.3f}; floor {INTEGRATION_FLOOR})")
    missing = [g for g, ok in integrated.items() if not ok]  # (local)
    if missing:
        print(f"    NOT integrated           : {missing}")
    print(f"    5 mandatory rewrites     : {all_mandatory}  {mandatory}")
    print(f"    substrate-IS markers     : {substrate_is}/{len(SUBSTRATE_IS_MARKERS)}")
    print(f"    authorial-voice markers  : {voice}/{len(VOICE_MARKERS)}")

    checks = {  # (local)
        "doc_growth": doc_bytes >= DOC_GROWTH_FLOOR_BYTES,
        "integration_floor": frac >= INTEGRATION_FLOOR,
        "all_mandatory": all_mandatory,
        "substrate_is": substrate_is >= 3,
        "voice_preserved": voice >= 2,
    }
    verdict = "PASS" if all(checks.values()) else "FAIL"  # (local)
    print(f"  checks: {checks}")
    print(f"  VERDICT: {verdict}")

    value = (  # (local)
        f"expanded_64462_to_{doc_bytes}_bytes_{n_integrated}of{n_gaps}_gaps_integrated_"
        f"frac{frac:.2f}_{sum(mandatory.values())}of5_mandatory_voice_preserved_substrate_IS"
        f"_supersedes={SUPERSEDES}"
    )

    # content payload = the document_post (per plan content_sha256_inputs=[document_post])
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL, pins, doc)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (document_post)")

    try:
        import numpy as np  # (local)
        np.savez(
            OUT_NPZ,
            doc_bytes=np.array([doc_bytes]),
            n_integrated=np.array([n_integrated]),
            n_gaps=np.array([n_gaps]),
            integration_frac=np.array([frac]),
            gap_keys=np.array(list(GAP_MARKERS.keys())),
            gap_integrated=np.array([integrated[g] for g in GAP_MARKERS]),
            mandatory_keys=np.array(list(MANDATORY_MARKERS.keys())),
            mandatory_present=np.array([mandatory[k] for k in MANDATORY_MARKERS]),
            verdict=np.array([verdict]),
        )
        print(f"  npz written: {OUT_NPZ}")
    except Exception as exc:  # noqa: BLE001
        print(f"  [npz] optional artifact skipped ({exc})")

    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  verdict appended -> {VERDICT_TXT}")
    print(f"  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
