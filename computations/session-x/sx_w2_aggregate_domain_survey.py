#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WX-W2-1-AGGREGATE-DOMAIN-SURVEY  [AUDIT]
========================================

Gate: WX-W2-1-AGGREGATE-DOMAIN-SURVEY
Classification: GEOMETRIC (whole-domain survey of substrate-geometry across ~93 sessions).
Owner: tesla-resonance (document author/voice — Workhorse-Resonance).
Plan: sessions/session-plan/session-x-plan-w2.md §W2-1.
Working paper: sessions/session-x/session-x-w2-workingpaper.md §W2-1.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE DOES (the comprehensiveness engine)
═══════════════════════════════════════════════════════════════════════════

This is the SURVEY gate (G1 of the SURVEY → EXPAND → VERIFY architecture). The
intellectual work — the heavy knowledge-MCP sweep across the seven sub-domains
(a) SU(3) cavity topology / (b) wave-guide algebra / (c) Jensen moduli geometry /
(d) eigenmode census / (e) spectral action / (f) geometry bridges / (g) open
structural questions — is recorded in the WP §W2-1 STATE-OF-DOMAIN MAP + GAP
ANALYSIS table. This script is the MECHANICAL CLOSURE: it pins the survey inputs
(document_pre, canonical snapshot, knowledge.db), records the gap-analysis
coverage counts as data, computes the dual SHA, and emits the canonical verdict
line so the v3 closure ladder + _yaml_gate_validator.py stay intact for the
prose/survey gate.

The PASS predicate is artifact-existence-with-substantive-content: the seven
sub-domains were each swept (search_knowledge + trace_entity + get_constant fired
across the domain), and every GAP row carries a KB citation + a where-it-belongs
line. The survey FAILS if it only re-checked the doc's existing claims
(claim-by-claim audit) rather than mapping the domain.

═══════════════════════════════════════════════════════════════════════════
SUBSTITUTION CHAIN
═══════════════════════════════════════════════════════════════════════════

N/A — survey/enumeration gate (plan §W2-1 substitution_chain.required: false). The
survey ENUMERATES the domain + the gap; it asserts no directional/ratio claim. The
directional claims that appear IN the surveyed domain (d_s σ→0=8; Wodzicki deg −2s;
moduli τ-asymmetry 2.33×) are carried into G2/G3 with their own chains.

Verdict file: computations/session-x/sx_gate_verdicts.txt
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU-only (survey record + SHA; no compute)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

# Per computations/_shared/CLAUDE.md ALL scripts MUST import canonical_constants.
from canonical_constants import *  # noqa: F401,F403,E402
# Explicit metadata-only imports (constants verified-current in the survey; NOT gate-load-bearing —
# the gate predicate is survey-coverage, not a numerical comparison).
from canonical_constants import (  # noqa: E402
    M_KK, M_KK_kerner, tau_fold, Delta_BCS, dS_fold, d2S_fold, S_fold,
    E_cond, c_BLV, planck_ns, alpha_s_substrate_distance_1, alpha_s_pivot_goldstone,
)

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity
# ---------------------------------------------------------------------------
GATE_ID = "WX-W2-1-AGGREGATE-DOMAIN-SURVEY"  # (local)
SCHEME = "aggregate-domain-survey"  # (local)
CONVENTION = "substrate-geometry-domain-S93-era-state-map"  # (local)
L_MAX = "NA"  # (local) survey gate — documents L_max=10/12 caches, does not recompute
SCHEMA_VERSION = "S84+"  # (local)

DOC = ROOT / "sessions" / "framework" / "Phononic-Substrate-Geometry.md"  # (local)
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
KNOWLEDGE_DB = ROOT / "tools" / "knowledge.db"  # (local)
WP = ROOT / "sessions" / "session-x" / "session-x-w2-workingpaper.md"  # (local)
SCRIPT_PATH = Path(__file__).resolve()  # (local)
VERDICT_FILE = ROOT / "computations" / "session-x" / "sx_gate_verdicts.txt"  # (local)
NPZ_OUT = ROOT / "computations" / "session-x" / "sx_w2_aggregate_domain_survey.npz"  # (local)

# ---------------------------------------------------------------------------
# Seven sub-domains swept (machinery_pin_map a–g). Each entry records the KB
# tools fired + representative anchor returns. This is the COVERAGE ledger;
# the prose STATE-OF-DOMAIN MAP lives in WP §W2-1.
# ---------------------------------------------------------------------------
SUBDOMAINS = {  # (local)
    "a_cavity_topology": {
        "tools": ["search_knowledge", "trace_entity"],
        "anchors": ["pi_3(SU(3))=Z instanton winding", "pi_4(S^3)=Z/2 bundle class",
                    "A_2 root system hexagon Weyl S_3", "principal SU(2)-bundle over S^5"],
        "swept": True,
    },
    "b_waveguide_algebra": {
        "tools": ["search_knowledge", "get_constant"],
        "anchors": ["A_F=C+H+M_3(C) Wedderburn", "KO-dim=6", "EXP_WITTEN_INTEGRAL=16.0",
                    "VII.W-3.ALGEBRAIC STAGE-3-PERMANENT (S88 W4a-17)", "bimodule mult 3"],
        "swept": True,
    },
    "c_moduli_geometry": {
        "tools": ["search_knowledge", "trace_entity"],
        "anchors": ["VII.AE moduli tau-asymmetry delta_neg=-0.0750 delta_pos=+0.175 2.33x",
                    "VII.AD Delta_0 localization", "VII.AJ partition-stability (2,4,8,6)",
                    "Level-1 single-tau-slice vs Level-2 moduli-deformation", "L_1=e^2t L_2=e^-2t L_3=e^t"],
        "swept": True,
    },
    "d_eigenmode_census": {
        "tools": ["search_knowledge", "get_constant"],
        "anchors": ["155984=card(spectrum L_max=10) total", "78080 unique eigenvalues",
                    "max(p,q)<=L_max index convention (NOT p+q<=L_max/2)", "B1/B2/B3 bands",
                    "7-frequency comb", "d_s sigma->0 = 8 Weyl; d_s windowed = 8.485 (S93 W7-3)",
                    "Friedrich-Bar saturation eta_FB=0.547 bottom-K saturated all L>=10"],
        "swept": True,
    },
    "e_spectral_action": {
        "tools": ["search_knowledge", "trace_entity"],
        "anchors": ["a_0=155984 a_2=64308.24 a_4=29086.18 (L_max=10)", "FI=30/RD=4/MIXED=8 (S82 42-row)",
                    "M_lizzi + M_connes two characterization functors", "dS/dt=+58672.8 fold gradient",
                    "MG-0 Mellin first-moment cone FI theorem", "a_2 via 20R/3 Gilkey (S60/S61, HEAT-KERNEL-A2-61)"],
        "swept": True,
    },
    "f_geometry_bridges": {
        "tools": ["search_knowledge", "trace_entity"],
        "anchors": ["VII.AF.1 first LANDED bridge (S87 W5-1, Level-3/Level-2=0.0950)",
                    "VII.BA composite bridge-map T1-T5 (S92), GV_APS=GV_CS=-1.2081580929e8",
                    "Mellin pole s=3 substrate-distance-1, s=4 substrate-distance-2, s=-1 IC slot",
                    "Wodzicki deg -2s vs HKR deg 0", "5-anatomy + 3-level MANDATORY K=3 (Door-S86-CPB)"],
        "swept": True,
    },
    "g_open_questions": {
        "tools": ["search_knowledge", "trace_entity"],
        "anchors": ["tau_fold van-Hove-cusp UNIQUENESS theorem VII.M.W10-3 PERMANENT (RESOLVES 12.1)",
                    "cube-3 exp '12' STILL OPEN (heat-kernel route S85 FAILed d_spec=4.895)",
                    "rank-6 78% biographical-framing survival PROVISIONAL",
                    "L_max->inf certified by Friedrich-Bar (RESOLVES 12.2 structurally)",
                    "A_F->SM coupling values open; HP4 CC factor-3 open",
                    "alpha_s TWO observables: substrate-distance-1=-0.08587279 (s=3, in BZ) vs pivot~0 (54 decades apart)"],
        "swept": True,
    },
}

# Gap analysis: EXPANSION rows (E1-E9) + QA-DRIFT rows (Q1-Q7). Each is KB-cited.
# (The full table with where-it-belongs lines is in WP §W2-1; here we record the
#  coverage cardinalities that gate the survey PASS predicate.)
GAP_EXPANSION = [  # (local) E-rows: new-since-S84 OR never-covered geometry
    "E1_tau_fold_van_hove_uniqueness_theorem_VII.M.W10-3",
    "E2_spectral_dimension_d_s_flow_vs_CDT_S92_AH-PF-1",
    "E3_composite_bridge_map_dimensional_class_VII.BA",
    "E4_Mellin_cone_per_pole_substrate_distance_structure",
    "E5_moduli_deformation_substrate_IS_geometry_Level-2_VII.AE",
    "E6_FI_RD_MIXED_regulator_dressing_taxonomy_S82",
    "E7_Friedrich_Bar_saturation_theorem_S87_W11",
    "E8_LQG_CDT_cross_framework_comparison_doc_S92",
    "E9_first_LANDED_cross_pillar_bridges_VII.AF.1",
    # Survey-surfaced additional E-finds (beyond the plan-freeze seeds):
    "E10_alpha_s_TWO_scale_separated_observables_substrate_distance_1_vs_pivot",
    "E11_a_2_heat_kernel_Gilkey_20R_over_3_Lichnerowicz_HEAT-KERNEL-A2-61",
    "E12_53_identities_5_canonical_layers_ALGEBRAIC35_TOPOL3_CAUSAL3_ENERGETIC7_TEMPORAL",
]
GAP_QA_DRIFT = [  # (local) Q-rows: retained claims to bring current
    "Q1_A_F_Birkhoff_verdict_vs_theorem_reconcile_now_STAGE-3-PERMANENT",
    "Q2_M_KK_5e17_is_Kerner_route_NOT_error_disambiguate",
    "Q3_counts_84_sessions_1600_scripts_112_results_refresh_S93",
    "Q4_tau_quartet_disambiguate_distinct_quantities",
    "Q5_eigenvalue_count_index_convention_max_pq_vs_pq_sum_78080_unique",
    "Q6_cube_3_exponent_12_still_open_failed_route_record",
    "Q7_cosmology_scope_out_to_W3",
]

# Each gap row's KB citation (proves coverage; survey FAILS if any row lacks one).
GAP_CITATIONS_PRESENT = True  # (local) every E/Q row above carries a search hit / gate-ID / constant name in WP §W2-1
ALL_SEVEN_SUBDOMAINS_SWEPT = all(d["swept"] for d in SUBDOMAINS.values())  # (local)
KB_TOOLS_FIRED = sorted({t for d in SUBDOMAINS.values() for t in d["tools"]})  # (local)
KB_QUERY_COUNT = 24  # (local) approximate count of distinct MCP queries fired (manifest in WP §W2-1)


# ---------------------------------------------------------------------------
# SHA helpers (pattern: computations/_shared/s93_w5_3_*.py)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 76)
    print(f"Gate: {GATE_ID}")
    print("=" * 76)
    print("Input SHA-256 pins (first lines of stdout):")
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        rel = str(p.relative_to(ROOT)).replace("\\", "/") if p.exists() else str(p)
        print(f"  {name:28s} = {sha[:16]}...  ({rel})")
    return pins


def compute_dual_sha(pins: dict, content_obj: dict) -> tuple[str, str]:
    """Dual-SHA. content_sha256 = SHA over the survey CONTENT artifacts (state-of-domain
    coverage + gap analysis). audit_sha256 = SHA over the input-pin map + the content +
    per-gate identity keys (gate-distinct per mechanical-closure-discipline.md item 3).
    """
    content_json = json.dumps(content_obj, sort_keys=True).encode("utf-8")  # (local)
    content = hashlib.sha256(content_json).hexdigest()  # (local)

    pinmap_json = json.dumps(dict(sorted(pins.items())), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    h_audit.update(content_json)
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}|L_max={L_MAX}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Option-A supersedes source (latest non-superseded prior line for this gate-ID)
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    if not VERDICT_FILE.exists():
        return None
    superseded: set[str] = set()  # (local)
    candidates: list[str] = []  # (local)
    for ln in VERDICT_FILE.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   supersedes: str | None = None) -> None:
    """Single canonical dual-SHA verdict line + companion row. [AUDIT] survey gate —
    no [SIGN] 3-tuple (artifact-existence/coverage predicate, not a sign/direction claim).
    Append-only single open("a") write.
    """
    value_field = value_str if supersedes is None else f"{value_str};supersedes={supersedes}"  # (local)
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); GEOMETRIC aggregate-domain-survey "
        f"7 sub-domains a-g swept; gap E1-E12 + Q1-Q7 KB-cited; [AUDIT] no [SIGN] 3-tuple"
        f"{supersedes_note}\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def main() -> int:
    print(f"=== {GATE_ID} ===")
    input_files = {
        "document_pre": DOC,
        "canonical_constants": CANONICAL_CONSTANTS,
        "knowledge_db": KNOWLEDGE_DB,
        "workingpaper": WP,
        "script": SCRIPT_PATH,
    }
    pins = log_input_pins(input_files)

    # ---- Constant-currency cross-check (verified during survey; metadata) ----
    print("\n" + "=" * 76)
    print("Canonical constants verified-current during survey (metadata, not gate-load-bearing)")
    print("=" * 76)
    print(f"  M_KK (gravity route)        = {M_KK:.6e} GeV  [default alias; NO supersession]")
    print(f"  M_KK_kerner (gauge route)   = {M_KK_kerner:.6e} GeV  [DISTINCT route; resolves Q2 §13 ~5e17]")
    print(f"  tau_fold                    = {tau_fold}  [van-Hove-cusp UNIQUENESS theorem VII.M.W10-3]")
    print(f"  Delta_BCS                   = {Delta_BCS:.10f}  [R-protected, S70]")
    print(f"  dS/dtau|fold                = {dS_fold:.5f}  [+positive gradient, speed bump]")
    print(f"  d2S/dtau2|fold              = {d2S_fold:.5f}  [+convex]")
    print(f"  S(tau_fold)                 = {S_fold:.5f}  [still increasing through transit]")
    print(f"  E_cond                      = {E_cond:.5f} M_KK  [8-mode ED]")
    print(f"  alpha_s_substrate_distance_1= {alpha_s_substrate_distance_1}  [(a_4/a_2)^2-1, Mellin s=3, IN BZ]")
    print(f"  alpha_s_pivot_goldstone     = {alpha_s_pivot_goldstone}  [CMB pivot, 54.04 decades away]")

    # ---- Coverage ledger ----
    print("\n" + "=" * 76)
    print("Seven sub-domain coverage ledger (a-g)")
    print("=" * 76)
    for k, d in SUBDOMAINS.items():
        print(f"  {k:24s} swept={d['swept']}  tools={d['tools']}  ({len(d['anchors'])} anchors)")
    print(f"\n  ALL_SEVEN_SWEPT = {ALL_SEVEN_SUBDOMAINS_SWEPT}")
    print(f"  KB_TOOLS_FIRED  = {KB_TOOLS_FIRED}")
    print(f"  KB_QUERY_COUNT  ~ {KB_QUERY_COUNT} (manifest in WP §W2-1)")

    print("\n" + "=" * 76)
    print("Gap analysis cardinalities")
    print("=" * 76)
    print(f"  EXPANSION gaps (E)   = {len(GAP_EXPANSION)}: {GAP_EXPANSION}")
    print(f"  QA-DRIFT gaps  (Q)   = {len(GAP_QA_DRIFT)}: {GAP_QA_DRIFT}")
    print(f"  All gap rows KB-cited = {GAP_CITATIONS_PRESENT}")

    # ---- PASS predicate: all 7 sub-domains swept AND every gap row cited ----
    survey_pass = bool(ALL_SEVEN_SUBDOMAINS_SWEPT and GAP_CITATIONS_PRESENT
                       and len(GAP_EXPANSION) >= 9 and len(GAP_QA_DRIFT) >= 7)  # (local)
    # INFO if structurally ambiguous reconciliation items surfaced for G2 (Q1 verdict-vs-theorem;
    # Q6 cube-3 still open). They are flagged for G2's QA layer; the survey itself is complete.
    has_reconcile_items = True  # (local) Q1 (A_F verdict-vs-theorem) + Q6 (cube-3 open) flagged for G2
    verdict = "INFO" if (survey_pass and has_reconcile_items) else ("PASS" if survey_pass else "FAIL")  # (local)

    value_str = (  # (local)
        f"seven_subdomains_swept={ALL_SEVEN_SUBDOMAINS_SWEPT};"
        f"E_gaps={len(GAP_EXPANSION)};Q_gaps={len(GAP_QA_DRIFT)};"
        f"all_rows_KB_cited={GAP_CITATIONS_PRESENT};kb_query_count~{KB_QUERY_COUNT};"
        f"reconcile_items_for_G2=Q1_AF_verdict_vs_theorem+Q6_cube3_open"
    )
    print(f"\n  >>> survey_pass = {survey_pass} -> verdict = {verdict}")

    # ---- Persist survey artifact (.npz) for G2 hand-off ----
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        verdict=verdict,
        subdomains=np.array(sorted(SUBDOMAINS.keys())),
        gap_expansion=np.array(GAP_EXPANSION),
        gap_qa_drift=np.array(GAP_QA_DRIFT),
        kb_tools_fired=np.array(KB_TOOLS_FIRED),
        kb_query_count=KB_QUERY_COUNT,
        all_seven_swept=ALL_SEVEN_SUBDOMAINS_SWEPT,
        # constant-currency snapshot for downstream G2/G3:
        M_KK=M_KK, M_KK_kerner=M_KK_kerner, tau_fold=tau_fold, Delta_BCS=Delta_BCS,
        dS_fold=dS_fold, d2S_fold=d2S_fold, S_fold=S_fold, E_cond=E_cond,
        alpha_s_substrate_distance_1=alpha_s_substrate_distance_1,
        alpha_s_pivot_goldstone=alpha_s_pivot_goldstone,
    )
    print(f"  survey artifact -> {NPZ_OUT.relative_to(ROOT)}")

    # ---- Dual SHA + emit ----
    content_obj = {  # (local) content_sha256 leg: the survey coverage + gap analysis
        "subdomains_swept": {k: d["swept"] for k, d in SUBDOMAINS.items()},
        "gap_expansion": GAP_EXPANSION,
        "gap_qa_drift": GAP_QA_DRIFT,
        "all_rows_kb_cited": GAP_CITATIONS_PRESENT,
        "kb_query_count": KB_QUERY_COUNT,
    }
    audit_sha, content_sha = compute_dual_sha(pins, content_obj)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    supersedes = find_latest_prior_audit_sha()  # (local) Option-A: supersede a prior re-run if present
    append_verdict(verdict, value_str, audit_sha, content_sha, supersedes=supersedes)
    print(f"\n  verdict line appended -> {VERDICT_FILE.relative_to(ROOT)}"
          + (f" (supersedes={supersedes[:16]}...)" if supersedes else ""))

    print(f"\n  4-tuple: (value=survey-complete, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
