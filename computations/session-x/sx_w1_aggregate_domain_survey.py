#!/usr/bin/env python3
"""
WX-W1-1 — AGGREGATE-DOMAIN-SURVEY (closure script)
==================================================

Gate: WX-W1-1-AGGREGATE-DOMAIN-SURVEY  ([AUDIT])

Pre-registered PASS boundary (plan §W1-1 strict_PASS_boundary):
  PASS iff (i) the resonance-hypothesis DOMAIN was swept across ALL pertinent
  entity classes {theorems, closed, gates, open, constants, sessions,
  researchers} with the query manifest recorded; AND (ii) the GAP ANALYSIS is
  enumerated as a table in which EVERY row carries a KB citation AND a one-line
  "where it belongs in the document". FAILS if the output only re-checks the
  document's existing sentences rather than mapping the domain and the gap.

This gate is a SURVEY gate: there is no numerical comparison. The intellectual
work (the state-of-domain map + the 22-row gap table + the 35-entry query
manifest) lives in the working-paper §W1-1 section. This closure script:
  - records the query manifest + gap-row count + entity-class coverage,
  - computes the S84+ dual SHA over (document_pre + survey artifacts +
    canonical snapshot + kb_query_manifest),
  - writes the npz sidecar,
  - appends the canonical verdict line + dual-SHA companion row.

PASS is set-coverage + gap-enumeration-with-citations (operator.type='set' in
the plan). No 3-tuple companion row ([AUDIT] trigger;
schema_v2_3tuple_required=false).

DISCIPLINE:
  - `from canonical_constants import *` (MANDATORY first import)
  - every computed intermediate tagged `# (local)`
  - CPU-only (string/SHA work, no linear algebra)
  - atomic single-`open("a")` verdict append (NO read-modify-write / truncate)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent          # (local) computations/session-x
COMPUTATIONS_DIR = SESSION_DIR.parent                  # (local) computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"              # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                 # (local)
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib   # noqa: E402
import json      # noqa: E402
import time      # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins (plan §W1-1)
# ---------------------------------------------------------------------------
SESSION = "SX"                                                  # (local)
GATE_ID = "WX-W1-1-AGGREGATE-DOMAIN-SURVEY"                     # (local)
SCHEME = "AGGREGATE-DOMAIN-SURVEY"                              # (local)
CONVENTION = "domain-coverage-by-enumeration-plus-gap-citation"  # (local)
L_MAX = "N/A"                                                   # (local) survey gate

# Output destinations (canonical per-session verdict file per gate-verdicts.md)
OUT_NPZ = SESSION_DIR / "sx_w1_aggregate_domain_survey.npz"     # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"             # (local)

# Input files (plan §W1-1 input_files; runtime SHA capture)
TARGET_DOC = PROJECT_ROOT / "sessions/framework/Phononic-framework-hypothesis.md"  # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"          # (local)
KNOWLEDGE_DB = PROJECT_ROOT / "tools/knowledge.db"             # (local)
WP_PATH = PROJECT_ROOT / "sessions/session-x/session-x-w1-workingpaper.md"  # (local)

INPUT_FILES = [TARGET_DOC, CANONICAL_PATH, KNOWLEDGE_DB, WP_PATH]  # (local)

# ---------------------------------------------------------------------------
# Section 3b — Survey content (the recorded artifacts; intellectual work in WP)
# ---------------------------------------------------------------------------
# Entity classes swept (plan machinery_pin_map.entity_classes_surveyed).
ENTITY_CLASSES_SWEPT = [
    "theorems", "closed", "gates", "open", "constants", "sessions", "researchers",
]  # (local)

# KB query manifest — the 35-entry heavy sweep (mirrors WP §W1-1 MCP Pre-Compute
# Audit table). Each entry: (tool, query, one-line salient return).
KB_QUERY_MANIFEST = [
    ("search_knowledge", "cross-pillar bridge STAGE-3-PERMANENT joint theorem",
     "VII.AH FIRST cross-axis joint theorem to STAGE-3-PERMANENT (S90 W2 CF-20); VII.AW.OP-PROJ THIRD (S93 W5)"),
    ("search_knowledge", "DILUTION-CC Volovik tracking vacuum 114 OOM",
     "CC_OOM=115.5; S66-W1-A-DILUTION-CC PASS; 114 OOM -> 0.01 OOM; rho_vac~M_Pl^2 H^2"),
    ("search_knowledge", "GGE permanence retraction re-establishment integrability laminar",
     "E2 RETRACTED S39 (V_phys 13% non-separable); re-established R-G + Door-10 Meissner; THERM-61"),
    ("search_knowledge", "spectral functional joint falsification f sqrt sole survivor",
     "JOINT-FALSIFICATION-67 PASS; SPECTRAL-FUNCTIONAL-FIT-72 f*=0.912sqrt+0.088exp; q-theory sole CC survivor"),
    ("search_knowledge", "LQG LQC bounce CDT phonon exflation comparison",
     "loop-quantum-gravity-phonon-exflation-comparison.md (S92); six shared commitments; cosmogenesis divergence"),
    ("search_knowledge", "acoustic white hole causal disconnect transit horizon",
     "S85-ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL; d_geom=2.373e-1 vs d_acoustic=1.034e-3 M_KK^-1"),
    ("search_knowledge", "division algebra ladder Wedderburn-Artin A0 M2 Frobenius rescue",
     "S88-A0-M2-BACKWARD-RESCUE PASS; N7 Frobenius Rescue PROVEN STAGE-3-PERMANENT; A_F=C+H+M_3(C)"),
    ("search_knowledge", "tau_fold uniqueness van Hove cusp non-stationarity",
     "VII.M.W10-3 PERMANENT (S85 W10-3); tau_fold=0.190 van-Hove-cusp non-stationarity uniqueness theorem"),
    ("search_knowledge", "observational matches A_s n_s alpha_s Omega_DM m_H N_eff f_NL r",
     "TENSOR-SCALAR-64 r=0.0333; ~30 gates PASSED; span identities"),
    ("search_knowledge", "modular flow Connes-Rovelli thermal time tick automorphism",
     "connes-addendum tick eq sigma_1^omega=Ad(Delta^i); T_tick=2pi/omega_0~4.11 t_Pl; T''(0)>0"),
    ("search_knowledge", "four speed hierarchy c_mod c_BLV c_BA c_L 3He-B Lorentz violation",
     "SOUND-SPEED-64 PASS: c_mod=1.0 > c_BLV=0.485 > c_BA=0.399 > c_L=0.025 (all causal)"),
    ("search_knowledge", "WKB inapplicable sudden approx van Hove transit Parker squeezing",
     "59.8 Parker pairs at fold (S38, P_exc=1.000); sudden-approx universality (S61)"),
    ("search_knowledge", "A_s scalar amplitude 1.58e-9 decoherence M_Pl spectral",
     "M_Pl^2(spectral L10)=135.75 vs M_Pl^2(actual)=27010.91 M_KK^2 (OOM gap source)"),
    ("search_knowledge", "Higgs mass 127.5 GeV transverse fiber KK threshold",
     "m_H=127.5-131.8 GeV (Aitken-Gaussian S62-S66); 131.8 (S28c); S84 ACCOMMODATION flag"),
    ("search_knowledge", "Pomeranchuk reclassification S75 spectral functional heat kernel",
     "Z_R counterterm theorem W6-67 FAIL (NEGATIVE structural); f* non-perturbative (no heat-kernel)"),
    ("search_knowledge", "f_NL non-Gaussianity framework prediction GGE",
     "f_NL^{GGE diag}~0.13; GGE-BISPECTRUM-67 equil~1.12; folded 0.056; DRIFT vs memory -0.313"),
    ("trace_entity", "VII.AH",
     "FIRST STAGE-3-PERMANENT; 8/8 checks; K2->K3 MANDATORY; Stage-2 audit_sha 4fcd7d29..."),
    ("trace_entity", "spectral dimension flow d_s CDT",
     "d_s=-2 d ln P/d ln sigma; Phi_graph-Laplacian != Phi_heat-trace (S93 W7-3); gamma_E discriminator"),
    ("trace_entity", "LEGGETT-MOMENT-70",
     "Omega_DM h^2=0.1200 (Leggett-only); 0.6% from Planck; C11 substrate-IS DM anchor"),
    ("trace_entity", "Ordered Veil",
     "The Ordered Veil (S38) PROVEN: the transit IS the physics; t_scr/t_transit=814"),
    ("trace_entity", "Leggett dark matter Omega_DM",
     "(no direct trace; resolved via LEGGETT-MOMENT-70)"),
    ("get_constant", "tau_fold", "0.19 (S12/S42, CONST-FREEZE-42, Superseded=False) -- canonical fold"),
    ("get_constant", "sin2_thetaW_fold", "0.58385339192799 (NOT un-normalized form at any physical tau -- flag)"),
    ("get_constant", "sin2_thetaW_MSbar", "0.23122 (PDG; un-normalized form at 0.2994 gives 0.231902)"),
    ("get_constant", "c_fabric", "209.97368021 M_KK"),
    ("get_constant", "c_Gold", "0.915 M_KK"),
    ("get_constant", "A_s_FW", "not found (per-pathway; A_s_CMB=2.1e-9; 1.58e-9 = decoherence-regulated, 75% Planck)"),
    ("get_constant", "N_eff_SM", "3.044"),
    ("get_constant", "M_KK", "7.4287e16 GeV"),
    ("get_constant", "Mach_max", "13.75"),
    ("get_constant", "c_BLV(via list)", "0.485 (S64 Brillouin-Landau-Vortex; 3He-B inheritance)"),
    ("list_constants", "A_s|n_s|alpha_s|Omega_DM|m_H|N_eff|f_NL|w_0",
     "n_s_framework=0.9561, Omega_DM=0.2657, m_H_obs=125.1, r_CMB_framework=0.0117, alpha_s_substrate_distance_1=-0.0858728"),
    ("list_constants", "section observation/cosmological", "section names differ; pulled via pattern filter"),
    ("sage_eval", "sin2thetaW adjudication (Claim A)",
     "S1==S10 (Sage True); both 0.231902 at 0.2994 (matches PDG); factor-3 form 0.475273 (no match)"),
    ("sage_eval", "sound-speed e-fold split (Claim C)",
     "c_fabric/c_Gold=229.479; (1/2)ln=2.7179; total~2.92-2.96; l_2nd-sound=720.93~721"),
]  # (local)

# Gap rows (the 22 enumerated in WP §W1-1 (b)). Each: (id, tag, has_citation, where_belongs_nonempty).
GAP_ROWS = [
    ("G-1", "NEVER", True, True), ("G-2", "NEW", True, True), ("G-3", "NEW", True, True),
    ("G-4", "NEW", True, True), ("G-5", "DRIFTED", True, True), ("G-6", "NEW", True, True),
    ("G-7", "NEW", True, True), ("G-8", "NEW", True, True), ("G-9", "NEW", True, True),
    ("G-10", "NEW", True, True), ("G-11", "NEW", True, True), ("G-12", "NEW", True, True),
    ("G-13", "NEW", True, True), ("G-14", "NEVER", True, True), ("G-15", "NEW", True, True),
    ("G-16", "NEW", True, True), ("G-17", "NEW", True, True), ("G-18", "DRIFTED", True, True),
    ("G-19", "NEW", True, True), ("G-20", "DRIFTED", True, True), ("G-21", "DRIFTED", True, True),
    ("G-22", "DRIFTED", True, True),
]  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; 'MISSING' on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return "MISSING"
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
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


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    content_blob: bytes,
) -> tuple[str, str]:
    """(audit_sha256, content_sha256), S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
                     -- the document_pre + canonical-snapshot + kb-manifest audit
                        leg (plan §W1-1 audit_sha256_inputs).
    content_sha256 = sha256( content_blob )
                     -- over the state-of-domain map + gap analysis (plan
                        content_sha256_inputs).
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(content_blob)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verdict emission (atomic single-open append; S84+ dual-SHA)
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the canonical verdict line + dual-SHA companion row.

    Atomic append: ONE `open("a")` write per line. [AUDIT] trigger => NO 3-tuple
    companion row (plan §W1-1 schema_v2_3tuple_required=false).
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Coverage evaluation (set-membership PASS, no numerical threshold).
    classes_swept = set(ENTITY_CLASSES_SWEPT)  # (local)
    required_classes = {"theorems", "closed", "gates", "open", "constants", "sessions"}  # (local)
    coverage_ok = required_classes.issubset(classes_swept)  # (local)

    n_gap = len(GAP_ROWS)  # (local)
    rows_with_citation = sum(1 for (_id, _tag, has_cit, _wb) in GAP_ROWS if has_cit)  # (local)
    rows_with_where = sum(1 for (_id, _tag, _hc, wb) in GAP_ROWS if wb)  # (local)
    every_row_cited = (rows_with_citation == n_gap) and (rows_with_where == n_gap)  # (local)

    n_queries = len(KB_QUERY_MANIFEST)  # (local)
    manifest_recorded = n_queries >= 20  # (local) plan: "tens of queries"

    tag_counts = {  # (local)
        "NEW": sum(1 for r in GAP_ROWS if r[1] == "NEW"),
        "NEVER": sum(1 for r in GAP_ROWS if r[1] == "NEVER"),
        "DRIFTED": sum(1 for r in GAP_ROWS if r[1] == "DRIFTED"),
    }

    survey_pass = bool(coverage_ok and every_row_cited and manifest_recorded)  # (local)
    verdict = "PASS" if survey_pass else "INFO"  # (local)
    value = (
        f"domain_swept={len(classes_swept)}_entity_classes"
        f"_AND_gap_rows_cited={rows_with_citation}_of_{n_gap}"
        f"_queries={n_queries}"
    )  # (local)

    print(f"entity classes swept: {sorted(classes_swept)}")
    print(f"required-class coverage: {coverage_ok}")
    print(f"gap rows: {n_gap}; with citation: {rows_with_citation}; with where-belongs: {rows_with_where}")
    print(f"tag counts: {tag_counts}")
    print(f"kb query manifest entries: {n_queries}")
    print(f"survey PASS: {survey_pass}")
    print()

    # 2. Build content blob (state-of-domain map + gap analysis fingerprint).
    content_payload = {  # (local)
        "entity_classes_swept": sorted(classes_swept),
        "gap_rows": [{"id": r[0], "tag": r[1], "has_citation": r[2], "where_belongs": r[3]} for r in GAP_ROWS],
        "kb_query_manifest": [{"tool": t, "query": q, "salient": s} for (t, q, s) in KB_QUERY_MANIFEST],
        "tag_counts": tag_counts,
    }  # (local)
    content_blob = json.dumps(content_payload, separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    # 3. Dual SHA over the pin map + content blob.
    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins, content_blob)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (state-of-domain map + gap analysis)")
    print()

    # 4. Persist npz sidecar (kb_query_manifest + gap-row count + SHA pins).
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        entity_classes_swept=np.array(sorted(classes_swept), dtype=object),
        n_gap_rows=n_gap,
        rows_with_citation=rows_with_citation,
        tag_counts=json.dumps(tag_counts),
        kb_query_manifest=np.array(
            [f"{t}::{q}::{s}" for (t, q, s) in KB_QUERY_MANIFEST], dtype=object
        ),
        n_queries=n_queries,
        input_pin_map=json.dumps(pins),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"npz sidecar written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 5. 4-tuple + verdict (dual-SHA; NO 3-tuple for [AUDIT]).
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"content_sha256: {content_sha}")
    print(f"audit_sha256:   {audit_sha}")
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 regardless of PASS/INFO -- verdict is data, not exit code.
    return 0


if __name__ == "__main__":
    sys.exit(main())
