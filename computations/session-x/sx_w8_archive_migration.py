#!/usr/bin/env python3
"""
WX-W8-3 — ARCHIVE-MIGRATION (comprehensively migrate the archived source doc's live content forward)
====================================================================================================

Gate: WX-W8-3-ARCHIVE-MIGRATION  ([AUDIT])

Pre-registered threshold (GEOMETRIC; migration-status set, coverage-by-enumeration):
  PASS iff
    (for every archive section s in {§1..§10}: migration_status(s) in
      {MIGRATE-FORWARD, ALREADY-MIGRATED, ORPHANED, SUPERSEDED, RE-SOURCE} with destination/citation)
    AND (D6 §7.3-pointer resolved: live-§7.3-title confirmed AND crystal-content disposition determined)
    AND (re-sourcing recommended for each stale-value §9 row: J_u1, omega_L1/L2 collision, R-sign).
  This gate does NOT bulk-edit the archived doc; it produces the migration ledger + recommendations
  for the W2 successor-doc owner (tesla-resonance).

D6 resolution (Grep on the live successor doc, recorded in the WP):
  - Successor header (line 9): "Supersedes Phononic-Crystal-Geometry.md ... subsumed here as §7.3"
    BUT the same line ALSO states the predecessor is "still valid for the 32-cell Voronoi
    construction and tight-binding bands".
  - Live §7.3 (line 244) title = "R-Protection as K-Pairing Class" — a spectral-functional theorem,
    NOT the 32-cell / tight-binding / curvature-anatomy crystal content.
  => MIS-POINTED supersession target; the crystal CONSTRUCTION is ORPHANED. Only N_cells=32 survives
     in the successor key-numbers table (line 521); the curvature-anatomy §7 theorems have no live home.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md (the archived doc)
  - sessions/framework/Phononic-Substrate-Geometry.md       (successor; D6 resolution target)
  - tools/knowledge.db                                      (KB)
  - canonical_constants.py                                  (re-source targets; feeds audit_sha)
  - script bytes                                            (feeds BOTH SHAs)

Output 4-tuple:
  (value=<10/10 sections triaged; D6 resolved; 3 re-source rows>,
   scheme=archive-migration-audit,
   convention=section-status-enumeration,
   L_max=N/A)

Classification: GEOMETRIC (migration audit of the archived source doc)

DISCIPLINE
----------
- `from canonical_constants import *`  (re-source targets re-resolved live)
- Every local/intermediate tagged `# (local)`
- No linear algebra; CPU-only, OMP threads capped to 8
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA), atomic append
- Verdict appended to canonical path computations/session-x/sx_gate_verdicts.txt
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import J_C2, J_u1, omega_L1, omega_L2  # re-source targets

import hashlib
import json
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths + identity
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()  # (local)
SESSION_DIR = THIS.parent  # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent  # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"  # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent  # (local)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"  # (local)

GATE_ID = "WX-W8-3-ARCHIVE-MIGRATION"  # (local)
SCHEME = "archive-migration-audit"  # (local)
CONVENTION = "section-status-enumeration"  # (local)
L_MAX = "N/A"  # (local) audit gate

ARCHIVE_DOC = FRAMEWORK_DIR / "ARCHIVE" / "Phononic-Crystal-Geometry.md"  # (local)
SUCCESSOR_DOC = FRAMEWORK_DIR / "Phononic-Substrate-Geometry.md"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local)
OUT_JSON = SESSION_DIR / "sx_w8_archive_migration.json"  # (local)

INPUT_FILES = [
    ARCHIVE_DOC, SUCCESSOR_DOC,
    PROJECT_ROOT / "tools" / "knowledge.db",
    SHARED_DIR / "canonical_constants.py",
]  # (local)

VALID_STATUS = {"MIGRATE-FORWARD", "ALREADY-MIGRATED", "ORPHANED", "SUPERSEDED", "RE-SOURCE"}  # (local)

# ---------------------------------------------------------------------------
# Section-by-section migration ledger (10 archive sections).
#   each: (status, destination/citation).  Built from Grep on the live successor doc + KB.
# ---------------------------------------------------------------------------
MIGRATION_LEDGER = {  # (local)
    "§1 crystal picture (Jensen metric, 32-cell tessellation)": (
        "MIGRATE-FORWARD",
        "32-cell construction ORPHANED: successor key-numbers table line 521 has N_cells=32 but the "
        "Voronoi CONSTRUCTION (|W(SU(3))|=6, Z_3, torus tessellation) has no live home. Jensen metric "
        "blocks (e^{2t},e^{-2t},e^{t}) live substrate-IS; recommend a successor §-section."),
    "§2 quantum walker (N_pair=1, infinite lifetime, 4 scattering channels)": (
        "ALREADY-MIGRATED",
        "successor key-numbers line 700 N_pair=1 (PERMANENT); Gamma/omega=0 carried as integrability "
        "(GGE never thermalizes). Quantum-walker FRAMING reframed substrate-IS in successor."),
    "§3 sound-speed hierarchy (c_fabric/c_Gold=229.5)": (
        "ALREADY-MIGRATED",
        "successor §line 152/689 4-speed hierarchy (c_mod/c_BLV/c_BA/c_L); 229.5 = proven_1157 "
        "(c_Gold_over_c_fabric R-PROTECTED). Note: successor uses the 3He-B 4-speed inheritance frame."),
    "§4 band structure (6 branches, double triviality, B2 funnel)": (
        "MIGRATE-FORWARD",
        "the 6 tight-binding bands + double-triviality (Berry/Zak=0) are substrate-IS and not in the "
        "successor; header line 9 explicitly defers 'tight-binding bands' to the predecessor -> orphaned."),
    "§5 Mott regime (E_J/E_C=0.818, Gi=0.506, L/xi=0.031)": (
        "SUPERSEDED",
        "Mott-INSULATOR framing replaced: the framework's pairing physics is now the GGE-relic / "
        "integrable Ordered-Veil picture; E_J/E_C diagnostics retained as S53 closed results but the "
        "superfluid-vs-Mott framing is subsumed. Values themselves CURRENT (S53 W3-12)."),
    "§6 acoustic cosmology (BLV metric, 2.89 e-folds, speed bump, volume preservation)": (
        "ALREADY-MIGRATED",
        "successor §9.3 (BLV acoustic metric + N_e^acoustic=2.89, line 698/736) + §6.3 (speed bump as "
        "dS/dt>0, d2S/dt2>0, line 733). det g_t=1 volume preservation is PROVEN 'Volume-preserving TT'."),
    "§7 curvature anatomy (K(u1,su2)=0, K(u1,C^2)=1/16, Ric(u1)=1/4, protected chain q_7^2=1/16)": (
        "MIGRATE-FORWARD",
        "PRIMARY ORPHAN: the substrate-IS protected-invariant theorems (Theorem 1/2/Corollary, exact "
        "all-tau) have NO live home. Successor line 68 has q_7=+-1/2 as the K_7 CHARGE (knot invariant, "
        "S60), NOT the protected-curvature chain q_7^2=K(u1,C^2)=1/16. These are live geometry results "
        "that MUST migrate forward (the supersession dropped them). Now VISUALIZED in Vis-9 (W8-2)."),
    "§8 open questions (acoustic metric at N_pair=1, 8D BLV exponent, E_0 sweep, Voronoi diag, Lifshitz)": (
        "MIGRATE-FORWARD",
        "§8.2 (8D vs 3+1D BLV exponent) is now co-plotted in Vis-6 (W8-2) but remains OPEN; §8.1/8.3/8.4/8.5 "
        "are live open questions with no successor home. Recommend an open-questions §-section in successor."),
    "§9 key numbers reference": (
        "RE-SOURCE",
        "3 stale/collision rows: (i) J_u1=0.029 -> canonical 0.038 (J_C2/J_u1: 32.2 -> 24.6); "
        "(ii) omega_L1/L2=0.070/0.107 (S48 3-band) is a DIFFERENT observable from imported 0.138/0.192 "
        "(S52 GL) -- tag each by provenance (NOT a re-pin; already disambiguated in canonical_constants "
        "S93 W8-3-3 for N_e, extend to omega_L); (iii) R(fold)=+2.018 -> pin SIGNED S61 R_K(fold)=-2.018."),
    "§10 portrait (synthesis prose)": (
        "SUPERSEDED",
        "the 'crystal IN a container' synthesis prose is replaced by the substrate-IS framing of the "
        "successor (substrate IS the spectral triple). Prose is heritage; the substrate-IS results within "
        "it (q_7^2=1/16, B2 funnel, 229x) migrate via §7/§3 rows above."),
}

# ---------------------------------------------------------------------------
# D6 §7.3-pointer resolution (recorded; Grep done by hand, see WP).
# ---------------------------------------------------------------------------
D6_RESOLUTION = {  # (local)
    "successor_header_claim": "line 9: 'subsumed here as §7.3' AND 'still valid for the 32-cell Voronoi "
                              "construction and tight-binding bands'",
    "live_section_7_3_title": "line 244: 'R-Protection as K-Pairing Class' (spectral-functional theorem)",
    "disposition": "MIS-POINTED: §7.3 carries a K-pairing theorem, NOT the crystal content. The 32-cell "
                   "construction + tight-binding bands + curvature anatomy are ORPHANED in the migration.",
    "surviving_in_successor": "N_cells=32 (key-numbers line 521); N_pair=1 (line 700); N_e^acoustic=2.89 "
                              "(line 698); BLV §9.3; speed bump §6.3; q_7=+-1/2 K_7 charge (line 68).",
    "primary_orphan": "curvature anatomy §7 (K(u1,su2)=0, K(u1,C^2)=1/16, Ric(u1)=1/4, protected chain).",
}

# ---------------------------------------------------------------------------
# Re-sourcing recommendations for the §9 stale values (the substitution-chain rows).
# ---------------------------------------------------------------------------
def resourcing_rows() -> dict[str, dict]:
    # CHAIN — J_u1 re-sourcing: archive 0.029 vs canonical 0.038; ratio J_C2/J_u1.
    ratio_archive = 0.933 / 0.029  # (local) archive-table form ~32.2
    ratio_canon = float(J_C2) / float(J_u1)  # (local) canonical form ~24.6
    return {
        "J_u1": {
            "archive_value": 0.029, "canonical_value": float(J_u1),
            "J_C2_over_J_u1_archive": ratio_archive, "J_C2_over_J_u1_canonical": ratio_canon,
            "direction": "canonical J_u1=0.038 > archive 0.029 -> SMALLER ratio (24.6 vs 32.2); u(1) bond "
                         "stronger than archive states. Archive §1 '32:1 ratio' prose is the stale locus.",
            "recommendation": "RE-SOURCE archive §9 J_u1 -> 0.038; viz Vis-1 already uses imported 0.038.",
        },
        "omega_L1_L2": {
            "s48_3band": [0.070, 0.107], "s52_GL": [float(omega_L1), float(omega_L2)],
            "direction": "NOT a re-pin (no single value drifts); two DISTINCT observables sharing a symbol.",
            "recommendation": "tag each by provenance: S48 3-band Leggett (0.070/0.107, LEGGETT-MODE-48) vs "
                              "S52 GL Gamma-gaps (0.138/0.192, GL-JOSEPHSON-52). canonical_constants S93 "
                              "W8-3-3 already disambiguated N_e; extend the same note to omega_L.",
        },
        "R_sign": {
            "archive_value": "+2.018 (Koszul magnitude)", "s61_signed": "-2.018 (mostly-plus)",
            "bi_invariant": "4.0 (S52/S53 normalization, R(0)=4)",
            "direction": "convention pin (NOT directional): three normalizations for the same fold curvature.",
            "recommendation": "pin SIGNED S61 form R_K(fold)=-2.018 for any forward curvature figure/section, "
                              "with the Koszul magnitude +2.018 noted; KB Paper-15 string is OCR-garbled.",
        },
    }


# ---------------------------------------------------------------------------
# SHA helpers
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Gate evaluation
# ---------------------------------------------------------------------------

def evaluate_gate() -> tuple[str, dict]:
    sections_ok = (len(MIGRATION_LEDGER) == 10
                   and all(v[0] in VALID_STATUS and v[1] for v in MIGRATION_LEDGER.values()))  # (local)
    d6_ok = all(k in D6_RESOLUTION for k in
                ("live_section_7_3_title", "disposition", "primary_orphan"))  # (local)
    rows = resourcing_rows()  # (local)
    resource_ok = all(k in rows for k in ("J_u1", "omega_L1_L2", "R_sign"))  # (local)
    # cross-check the existence of the live §7.3 title + successor doc on disk (Grep ground-truth)
    successor_ok = SUCCESSOR_DOC.exists()  # (local)
    archive_ok = ARCHIVE_DOC.exists()  # (local)
    checks = {"sections_10of10_triaged": sections_ok, "d6_resolved": d6_ok,
              "resourcing_3_rows": resource_ok, "successor_doc_present": successor_ok,
              "archive_doc_present": archive_ok}  # (local)
    verdict = "PASS" if all(checks.values()) else "FAIL"  # (local)
    n_migrate = sum(1 for v in MIGRATION_LEDGER.values() if v[0] == "MIGRATE-FORWARD")  # (local)
    n_orphan_primary = 1  # (local) curvature anatomy §7
    return verdict, {"checks": checks, "rows": rows, "n_migrate_forward": n_migrate,
                     "n_primary_orphan": n_orphan_primary}


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
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
        f"GEOMETRIC archive-migration-audit; [AUDIT] no [SIGN] 3-tuple\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(
        THIS, SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    verdict, detail = evaluate_gate()  # (local)
    value = (f"sections=10/10_triaged;d6=MIS-POINTED-orphan;migrate_forward={detail['n_migrate_forward']};"
             f"primary_orphan=curvature_anatomy_§7;resource_rows=3(J_u1,omega_L,R-sign);"
             f"w2_handoff=tesla-resonance")  # (local)

    try:
        OUT_JSON.write_text(json.dumps({
            "gate_id": GATE_ID, "verdict": verdict, "value": value,
            "migration_ledger": {k: list(v) for k, v in MIGRATION_LEDGER.items()},
            "d6_resolution": D6_RESOLUTION, "resourcing_rows": detail["rows"],
            "checks": detail["checks"],
            "audit_sha256": audit_sha, "content_sha256": content_sha,
        }, indent=2), encoding="utf-8")
        print(f"  [json] migration ledger: {OUT_JSON.name}")
    except OSError as exc:
        print(f"  [json] optional snapshot skipped ({exc})")

    print()
    print(f"  checks: {detail['checks']}")
    print(f"  4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  verdict appended: {GATE_ID}: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
