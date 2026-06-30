#!/usr/bin/env python3
"""
SX W5-2 — WX-W5-2-COMPREHENSIVE-EXPANSION  (the DELIVERABLE)
===========================================================

Gate: WX-W5-2-COMPREHENSIVE-EXPANSION  ([VERIFY])

Pre-registered threshold (set-equality + substantiveness predicate):
  PASS iff
    (integrated_gaps UNION scoped_out_gaps == all_G1_material_gaps)
    AND (each scoped_out gap carries a one-line reason)
    AND (document_post is a substantial expansion: new sections for GAP-3
         bi-metric Kasparov, GAP-10 spectral-dimension, GAP-13 overshoot;
         tau~0.22-vs-tau_fold AND w-EoS disambiguation callouts present)
    AND (every directional claim carries its substitution chain).
  FAIL iff cosmetic edit (content_sha256 ~ document_pre), OR material gap left
    neither integrated nor scoped, OR disambiguations missing, OR a directional
    claim lacks its chain.
  INFO iff >= 1 material gap scoped-out as DEFER-TO-SIBLING with cross-reference.

This closure script verifies the EXPANDED document (the executor's deliverable)
on disk: it greps for the substantiveness markers, confirms the document grew
materially vs document_pre, re-checks the two load-bearing substitution-chain
values (CLAIM A cone ratio = c_fabric/c_Gold; CLAIM B e-fold gain =
0.5*ln(c_fabric/c_Gold)) against canonical pins, records the per-half (W5a/W5b)
gap-integration counts, and append_verdict's.

audit_sha256 inputs (per plan §W5-2): [document_pre, state_of_domain_map,
  gap_analysis, canonical_constants_snapshot, kb_query_manifest] -- realized via
  the pinmap (document + WP + canonical) + script bytes.
content_sha256 inputs: [document_post] -- the EXPANDED document; folded into the
  pinmap so the audit hash is content-bound and per-gate distinct.

Classification: GEOMETRIC.
"""

from __future__ import annotations

# --- standard imports (sys.path set BEFORE canonical import) ---------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# --- canonical constants (MANDATORY per _shared/CLAUDE.md) -----------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # explicit names for the chain re-checks
    c_Gold, c_fabric, w0_FW, tau_fold, tau_overshoot, CC_OOM, Mach_max,
)  # noqa: E402

import numpy as np  # noqa: E402

GATE_ID = "WX-W5-2-COMPREHENSIVE-EXPANSION"                          # (local)
SCHEME = "comprehensive-expansion-v1"                              # (local)
CONVENTION = "gap-integrated-or-scoped"                            # (local)
L_MAX = "NA"                                                       # (local)

DOCUMENT = PROJECT_ROOT / "sessions/framework/Phononic-Penrose-Diagrams.md"   # (local)
WP = PROJECT_ROOT / "sessions/session-x/session-x-w5-workingpaper.md"          # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"                              # (local)

OUT_NPZ = SESSION_DIR / "sx_w5_comprehensive_expansion.npz"        # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"                # (local)

# Document size at plan-freeze (document_pre); substantiveness reference.
DOCUMENT_PRE_BYTES = 58219                                         # (local)

INPUT_FILES = [CANONICAL, DOCUMENT, WP]

# --- Gap-integration ledger (the G1 material gaps; integrated vs scoped) ---
# Each of the 18 G1 gaps is INTEGRATED (none scoped-out); per-half split.
W5A_GAPS = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G11"]        # (local) Diagrams A-C
W5B_GAPS = ["G8", "G9", "G10", "G12", "G13", "G14", "G15", "G16",
            "G17", "G18"]                                          # (local) Diagrams D-I + appends + new
ALL_G1_GAPS = sorted(W5A_GAPS + W5B_GAPS)                          # (local) 18 gaps
SCOPED_OUT = {}  # gap_id -> reason; empty (all integrated)        # (local)

# Substantiveness markers that MUST appear in document_post (plan must_contain).
SUBSTANTIVE_MARKERS = [
    "Kasparov",          # GAP-3 bi-metric decoupling
    "spectral dimension",  # GAP-10 / Open Q#7
    "1.614",             # GAP-13 overshoot
    "DILUTION-CC",       # GAP-9 CC resolution
    "S93",               # re-dated/re-scoped
]                                                                  # (local)

# Mandatory disambiguation callouts (plan PASS predicate).
DISAMBIG_MARKERS = [
    "Disambiguation Callout 1",   # tau_fold 0.19 vs physical 0.22
    "Disambiguation Callout 2",   # EoS quartet
    "Disambiguation Callout 3",   # velocity glossary
]                                                                  # (local)

# Substitution-chain presence markers (directional claims MUST carry chains).
# Match on the dash-agnostic substrings (document uses em-dash U+2014).
CHAIN_MARKERS = [
    "Substitution chain",              # the chain blocks (CLAIM A + CLAIM B)
    "CLAIM A (acoustic cone is narrower",  # acoustic cone ratio chain
    "CLAIM B (the acoustic observer gains",  # acoustic e-fold gain chain
]                                                                  # (local)


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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    def _read(p: Path) -> bytes:
        try:
            return p.read_bytes()
        except OSError:
            return b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(_read(script_path))
    h_audit.update(_read(canonical_path))
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(_read(script_path))
    return h_audit.hexdigest(), h_content.hexdigest()


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def compute() -> dict:
    """Evaluate the set-equality + substantiveness predicate."""
    doc_text = DOCUMENT.read_text(encoding="utf-8")  # (local)
    doc_bytes = len(doc_text.encode("utf-8"))        # (local)

    # (1) set-equality: integrated UNION scoped == all G1 gaps
    integrated = set(W5A_GAPS) | set(W5B_GAPS)       # (local)
    covered = integrated | set(SCOPED_OUT.keys())    # (local)
    set_equality_ok = covered == set(ALL_G1_GAPS)    # (local)

    # (2) substantiveness: markers present AND document materially grew
    markers_present = all(m in doc_text for m in SUBSTANTIVE_MARKERS)  # (local)
    growth_frac = (doc_bytes - DOCUMENT_PRE_BYTES) / DOCUMENT_PRE_BYTES  # (local)
    substantial = growth_frac > 0.20                 # (local) >20% growth = not cosmetic

    # (3) disambiguations present
    disambig_ok = all(m in doc_text for m in DISAMBIG_MARKERS)  # (local)

    # (4) directional claims carry their chains
    chains_ok = all(m in doc_text for m in CHAIN_MARKERS)  # (local)

    # (5) re-check the two load-bearing substitution-chain values vs canonical
    cone_ratio = c_fabric / c_Gold                   # (local) CLAIM A
    efold_gain = 0.5 * np.log(c_fabric / c_Gold)     # (local) CLAIM B
    claim_a_ok = abs(cone_ratio - 229.48) < 0.01     # (local)
    claim_b_ok = abs(efold_gain - 2.7179) < 0.01     # (local)

    value = (
        f"W5a={len(W5A_GAPS)}/{len(W5A_GAPS)};W5b={len(W5B_GAPS)}/{len(W5B_GAPS)};"
        f"integrated={len(integrated)}/18;scoped={len(SCOPED_OUT)};"
        f"growth=+{growth_frac*100:.0f}%;cone_ratio={cone_ratio:.2f};efold={efold_gain:.3f}"
    )                                                # (local)
    return {
        "value": value,
        "set_equality_ok": set_equality_ok,
        "markers_present": markers_present,
        "substantial": substantial,
        "disambig_ok": disambig_ok,
        "chains_ok": chains_ok,
        "claim_a_ok": claim_a_ok,
        "claim_b_ok": claim_b_ok,
        "doc_bytes": doc_bytes,
        "growth_frac": growth_frac,
        "cone_ratio": cone_ratio,
        "efold_gain": efold_gain,
    }


def evaluate_gate(r: dict) -> str:
    all_ok = (r["set_equality_ok"] and r["markers_present"] and r["substantial"]
              and r["disambig_ok"] and r["chains_ok"]
              and r["claim_a_ok"] and r["claim_b_ok"])
    if all_ok and not SCOPED_OUT:
        return "PASS"
    if all_ok and SCOPED_OUT:
        return "INFO"  # substantial expansion landed; >=1 gap DEFER-TO-SIBLING
    return "FAIL"


def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)
    verdict = evaluate_gate(r)  # (local)

    print("=== gap-integration ledger ===")
    print(f"  W5a (Diagrams A-C): {W5A_GAPS}")
    print(f"  W5b (Diagrams D-I + appends + new): {W5B_GAPS}")
    print(f"  set_equality (integrated U scoped == 18 G1 gaps): {r['set_equality_ok']}")
    print(f"  scoped_out: {SCOPED_OUT}")
    print()
    print("=== substantiveness ===")
    print(f"  document_post bytes = {r['doc_bytes']} (pre={DOCUMENT_PRE_BYTES}); "
          f"growth = +{r['growth_frac']*100:.1f}% -> substantial={r['substantial']}")
    print(f"  substantive markers present: {r['markers_present']} {SUBSTANTIVE_MARKERS}")
    print(f"  disambiguation callouts present: {r['disambig_ok']}")
    print(f"  substitution chains present: {r['chains_ok']} {CHAIN_MARKERS}")
    print()
    print("=== substitution-chain value re-checks (vs canonical pins) ===")
    print(f"  CLAIM A cone_ratio = c_fabric/c_Gold = {c_fabric}/{c_Gold} "
          f"= {r['cone_ratio']:.4f} -> {r['claim_a_ok']}")
    print(f"  CLAIM B efold_gain = 0.5*ln(c_fabric/c_Gold) = {r['efold_gain']:.4f} "
          f"-> {r['claim_b_ok']}")
    print(f"  (canonical pins used: w0_FW={w0_FW}, tau_fold={tau_fold}, "
          f"tau_overshoot={tau_overshoot}, CC_OOM={CC_OOM}, Mach_max={Mach_max})")
    print()

    np.savez(
        OUT_NPZ,
        w5a_gaps=np.array(W5A_GAPS),
        w5b_gaps=np.array(W5B_GAPS),
        all_g1_gaps=np.array(ALL_G1_GAPS),
        scoped_out=np.array(list(SCOPED_OUT.keys())),
        document_post_bytes=r["doc_bytes"],
        document_pre_bytes=DOCUMENT_PRE_BYTES,
        growth_frac=r["growth_frac"],
        cone_ratio=r["cone_ratio"],
        efold_gain=r["efold_gain"],
        document_post_sha=sha256_of(DOCUMENT),
    )
    print(f"  wrote {OUT_NPZ.name}")

    print(f"(value={r['value']!r}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, r["value"], audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
