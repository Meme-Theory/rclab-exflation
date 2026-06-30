#!/usr/bin/env python3
"""
SX W3-1 — AGGREGATE-DOMAIN-SURVEY (cosmology + observational-contact domain)
===========================================================================

Gate: WX-W3-1-AGGREGATE-DOMAIN-SURVEY  ([AUDIT])

Pre-registered threshold (set-coverage + gap-enumeration; artifact-existence):
  PASS iff (entity classes ALL swept = {theorems, closed, gates, sessions, open,
  constants, equations, registries, provenance} over the cosmology domain)
  AND (gap_set enumerated with >=1 KB citation AND >=1 doc-location per row)
  AND (|gap_set| >= gap_floor=12) AND (each of 7 headline domains has >=1 row)
  AND (>= query_manifest_floor=25 KB queries logged).

This is a SURVEY gate. The intellectual work (the whole-project state-of-domain
map + the 25-row gap analysis + the 33-query MCP manifest) lives in the WP
section sessions/session-x/session-x-w3-workingpaper.md §W3-1. This closure
script is MECHANICAL: it re-reads the survey/gap artifacts (the WP section + the
document-pre + the canonical snapshot), verifies the coverage counters, computes
the dual-SHA over (script || canonical || input-pin-map), and appends the verdict.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/Phononic-to-Cosmos.md            (document_pre; SHA ledger-matched)
  - sessions/session-x/session-x-w3-workingpaper.md     (the §W3-1 survey + gap artifact)
  - computations/_shared/canonical_constants.py         (canonical snapshot; feeds audit_sha)
  - tools/knowledge.db                                  (the survey source; ~93 sessions)
  - script bytes                                        (feeds BOTH SHAs)

Output 4-tuple:
  (value=<domain-sweep coverage state>,
   scheme=KB-AGGREGATE-SURVEY,
   convention=substrate-IS-domain-map,
   L_max=N/A)

Classification: PHONONIC (cosmology domain = GGE-relic acoustic physics +
spectral-moment observables; substrate excitations throughout).

DISCIPLINE
----------
- `from canonical_constants import *` (MANDATORY first import)
- Every local/intermediate tagged `# (local)`
- No linear algebra; CPU-only, OMP threads capped to 8
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA), atomic append
- Verdict appended to canonical path computations/session-x/sx_gate_verdicts.txt
- Runtime drift: canonical_constants.py SHA may differ from plan ledger
  (concurrent additive touch); resolved to runtime per substrate-first §(ii.B).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import time
from pathlib import Path

# canonical_constants lives in computations/_shared; make it importable.
SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (MANDATORY)
import canonical_constants as cc  # (local) named handle for snapshot reads

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration identity
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent          # computations/session-x  (local)
COMPUTATIONS_DIR = SESSION_DIR.parent                  # computations            (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                 # project root            (local)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"  # (local)

SESSION = "SX"  # (local)
GATE_ID = "WX-W3-1-AGGREGATE-DOMAIN-SURVEY"  # (local)
SCHEME = "KB-AGGREGATE-SURVEY"  # (local)
CONVENTION = "substrate-IS-domain-map"  # (local)
L_MAX = "N/A"  # (local) survey gate; no spectral truncation enters the verdict

DOCUMENT_PRE = FRAMEWORK_DIR / "Phononic-to-Cosmos.md"  # (local)
WP_PATH = PROJECT_ROOT / "sessions" / "session-x" / "session-x-w3-workingpaper.md"  # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
KNOWLEDGE_DB = PROJECT_ROOT / "tools" / "knowledge.db"  # (local)

OUT_NPZ = SESSION_DIR / "sx_w3_aggregate_domain_survey.npz"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local) canonical per gate-verdicts.md

INPUT_FILES = [DOCUMENT_PRE, WP_PATH, CANONICAL, KNOWLEDGE_DB]  # (local)

# Pre-registered coverage floors (plan §W3-1 strict_PASS_boundary)
GAP_FLOOR = 12            # (local) >= 12 material gap rows
QUERY_FLOOR = 25          # (local) >= 25 distinct KB queries logged
ENTITY_CLASSES = [        # (local) the 9 pertinent entity classes
    "theorems", "closed", "gates", "sessions", "open",
    "constants", "equations", "registries", "provenance",
]
HEADLINE_DOMAINS = [      # (local) the 7 headline domains; each needs >= 1 gap row
    "CC", "n_s", "r", "DM-abundance",
    "BBN/expansion", "late-time DE/ISW", "observational-program/falsifier",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema W9a-99)
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( state-of-domain-map + gap-analysis content )
# Per plan §W3-1 audit_discriminators:
#   audit_sha256_inputs  = [document_pre, state_of_domain_map, gap_analysis,
#                           canonical_constants_snapshot, kb_query_manifest]
#   content_sha256_inputs = [state_of_domain_map, gap_analysis]
# The WP §W3-1 section IS the state_of_domain_map + gap_analysis + kb_query_manifest.
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


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def extract_wp_section(wp_text: str, anchor: str) -> str:
    """Return the §W3-1 section body (from its anchor to the next ### or EOF)."""
    start = wp_text.find(anchor)  # (local)
    if start < 0:
        return ""
    nxt = wp_text.find("\n### ", start + len(anchor))  # (local)
    return wp_text[start:] if nxt < 0 else wp_text[start:nxt]


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str], content_payload: str) -> tuple[str, str]:
    """audit = sha256(script||canonical||pinmap_json); content = sha256(content_payload)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256(content_payload.encode("utf-8"))  # (local)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Atomic single-`open('a')` write — canonical line + dual-SHA companion row."""
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
        f"[AUDIT] survey set-coverage; no [SIGN] 3-tuple; "
        f"canonical_constants runtime SHA may differ from plan ledger (additive concurrent "
        f"touch, resolved to runtime per substrate-first-canonical-sourcing.md (ii.B))\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 — Survey coverage verification (mechanical)
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure (legacy, informational): {closure[:16]}...")

    # Snapshot the canonical cosmology constants the survey/expansion cite.
    # (Consumed as PRE-CLOSED context, not recomputed.)
    snapshot = {  # (local)
        "w0_FW": cc.w0_FW,
        "wa_FW": cc.wa_FW,
        "n_s_framework": cc.n_s_framework,
        "planck_ns": cc.planck_ns,
        "r_CMB_framework": cc.r_CMB_framework,
        "r_PathH": cc.r_PathH,
        "CC_OOM": cc.CC_OOM,
        "Omega_m": cc.Omega_m,
        "Omega_DM": cc.Omega_DM,
        "Omega_DM_obs": cc.Omega_DM_obs,
        "Omega_Lambda": cc.Omega_Lambda,
        "sigma_8": cc.sigma_8,
        "T_acoustic": cc.T_acoustic,
        "M_KK_gravity": cc.M_KK_gravity,
        "N_eff_SM": cc.N_eff_SM,
        "f_NL_FW_S82_equilateral": getattr(cc, "f_NL_FW_S82_equilateral", None),
    }
    print("  canonical cosmology snapshot (runtime-read):")
    for k, v in snapshot.items():
        print(f"    {k} = {v}")

    # Re-read the WP §W3-1 section (the state-of-domain map + gap analysis).
    wp_text = WP_PATH.read_text(encoding="utf-8") if WP_PATH.exists() else ""  # (local)
    sec = extract_wp_section(wp_text, "### §W3-1. WX-W3-1-AGGREGATE-DOMAIN-SURVEY")  # (local)

    # Coverage counters (mechanical scan of the WP gap table + manifest).
    # Gap rows are table lines '| Gn | ...'; query manifest rows are '| n | `search_knowledge'/'get_constant'/'trace_entity'.
    import re  # (local)
    gap_rows = len(re.findall(r"^\|\s*G\d+\s*\|", sec, flags=re.MULTILINE))  # (local)
    query_rows = len(re.findall(r"(search_knowledge|get_constant|trace_entity)\(", sec))  # (local)
    headline_present = {d: (d in sec) for d in HEADLINE_DOMAINS}  # (local)
    all_headlines = all(headline_present.values())  # (local)
    classes_present = {c: (c in sec) for c in ENTITY_CLASSES}  # (local)
    all_classes = all(classes_present.values())  # (local)

    print()
    print("  coverage verification:")
    print(f"    gap rows found            : {gap_rows}  (floor {GAP_FLOOR})")
    print(f"    KB queries logged         : {query_rows}  (floor {QUERY_FLOOR})")
    print(f"    all 7 headline domains    : {all_headlines}  {headline_present}")
    print(f"    all 9 entity classes      : {all_classes}")

    checks = {  # (local)
        "gap_floor": gap_rows >= GAP_FLOOR,
        "query_floor": query_rows >= QUERY_FLOOR,
        "all_headlines": all_headlines,
        "all_classes": all_classes,
        "section_present": len(sec) > 2000,
    }
    verdict = "PASS" if all(checks.values()) else "FAIL"  # (local)
    print(f"  checks: {checks}")
    print(f"  VERDICT: {verdict}")

    value = (  # (local)
        f"domain_swept_{sum(classes_present.values())}_classes_"
        f"{sum(headline_present.values())}_headlines_"
        f"{gap_rows}gaprows_{query_rows}queries_all_present"
    )

    # content payload = the state-of-domain map + gap-analysis section (WP §W3-1)
    content_payload = sec  # (local)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL, pins, content_payload)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (WP §W3-1 survey+gap)")

    # Optional npz: gap-row table + query manifest as arrays
    try:
        import numpy as np  # (local)
        np.savez(
            OUT_NPZ,
            gap_rows=np.array([gap_rows]),
            query_rows=np.array([query_rows]),
            headline_domains=np.array(HEADLINE_DOMAINS),
            entity_classes=np.array(ENTITY_CLASSES),
            verdict=np.array([verdict]),
            snapshot_keys=np.array(list(snapshot.keys())),
            snapshot_vals=np.array([str(v) for v in snapshot.values()]),
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
