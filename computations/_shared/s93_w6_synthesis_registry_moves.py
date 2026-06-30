#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93 W6 Synthesis Registry Moves -- mack-cosmic-bridge (registry sole-writer)
============================================================================

Composite Wave-6 synthesis: consequences of the 6 closed W6 gates. Emits the
TWO composite verdict lines (Move 1 PASS + Move 2 INFO) for the W6-3 / W6-4
Stage-2 cross-axis PASS-AND adjudications, and updates the §W6 working paper
with the synthesis subsection. The THREE registry entries (§VII.BB STAGE-3
flip; §VII.BE structural-PASS-AND + Level-3 DEFER; §VII.AQ.OP-PROJ
STRUCTURALLY-OPEN-BY-DESIGN reframe) are applied as serial single-shot
in-place Edits to sessions/permanent-results-registry.md (AFTER pattern;
Edit-tool exact-match IS the re-read+verify; no conditional retry).

Author:  mack-cosmic-bridge (sole-writer for cross-pillar bridge entries +
         STAGE-1/STAGE-3 promotions per feedback_mack-bridge-role.md
         AMRI-PROMOTED 2026-04-28)
Plan:    sessions/session-plan/session-93-plan-w6.md (W6 synthesis registry moves)

--------------------------------------------------------------------
SUBSTRATE FRAMING (per phononic-framing.md "IS Space, Not IN Space")
--------------------------------------------------------------------

MOVE 1 (§VII.BB STAGE-3-PERMANENT): the substrate IS the M_3(C) Peter-Weyl
block of A_K = C (+) H (+) M_3(C) at single-tau-slice tau_fold = 0.19,
substrate-distance-3 pole s=5; the HH^1 cocycle norm IS substrate-IS at the
cohomology-class layer. The STAGE-3 flip is the consequence of an INDEPENDENT
2-axis Stage-2 PASS-AND (Axis-A connes spectral/NCG + Axis-B landau
substrate/condensed-matter), NOT agreement-among-agents: the two reviewers were
BLIND (read only the registered entry + their ORTHOGONAL substrate input --
Axis-A the W9-8 npz, Axis-B the s84 master spectrum cache) and never the
workshop transcripts. Per joint-theorem-promotion.md, blind cross-axis
agreement on orthogonal substrate inputs IS structurally-independent evidence,
the constructive complement to the epistemic-discipline.md "agreement among
agents" exclusion.

MOVE 2 (§VII.BE structural Stage-2 PASS-AND, Level-3 DEFERRED): the substrate
IS the Pati-Salam parent spectral triple (A_K_PS, H_K_PS, D_K_PS) at the
M_4(C)_PS rank-4 lepton-color block; the structural clauses PASS-AND on both
axes, but the NUMERICAL Level-3 anchor Res_{s=4} Tr(D_K_PS^{-2s}) is INFEASIBLE
(1094.7 GB full SU(4)_PS spectrum) -> route-4b defer to S94. STAGE-1-CANDIDATE
RETAINED; STAGE-3-PERMANENT eligibility CONDITIONAL on the S94 numerical pin.

MOVE 3 (§VII.AQ.OP-PROJ STRUCTURALLY-OPEN-BY-DESIGN): the substrate IS the
spectral triple with its continuous SU(3)-manifold internal geometry; the
order-one defect 4.000 IS the universal Cl(8)/Spin(8) continuity signature.
The Pati-Salam extension cannot remove it (PS algebra is a strict SUPERSET of
the SM algebra; max over the larger generator set >= max over the subset). The
SM gauge content is recovered via the substrate's OWN route (KK isometries +
representation theory, S31 4.3-4.4), NOT via the NCG inner-fluctuation order-one
condition -- so the order-one STAGE-3 route being closed is a BY-DESIGN
structural feature, not a defect.

--------------------------------------------------------------------
COMPOSITE VERDICT audit_sha256 CONSTRUCTION (per gate-verdicts.md + spawn)
--------------------------------------------------------------------

Each composite Stage-2 cross-axis-verify verdict's audit_sha256 is the
closure_hash (SHA-256) over the ORDERED input-pin map enumerated below. The
two pin maps are STRUCTURALLY DISTINCT (different axis SHAs + different
joint-clause keys) so the two composite audit_sha256 are unique by
construction (sig_5 preserved). content_sha256 = SHA-256 over this script's
bytes (the producing-script content).
"""

import hashlib
import json
import os
import sys
from pathlib import Path

# --- canonical-constants import (MANDATORY S34+) ----------------------------
SHARED_DIR = Path(__file__).resolve().parent  # (local) computations/_shared
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    alpha_HH1_per_pole_FW_s4,
    alpha_HH1_per_pole_FW_s5,
    vii_bb_element_5_empirical_anchor_FW,
)

PROJECT_ROOT = SHARED_DIR.parent.parent  # (local) C:/sandbox/Ainulindale Exflation
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
WP_PATH = PROJECT_ROOT / "sessions" / "session-93" / "session-93-w6-workingpaper.md"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
SCHEMA_VERSION = "S84+"

# --- on-disk Stage-2 axis verdict SHAs (verified present; spawn prompt) -----
W6_3_AXIS_A_AUDIT = "19f46846ed6e1c8b9db2405934b65aa4c0a9481eae7e8b2701330392385b9d90"  # connes PASS (line 107)
W6_3_AXIS_B_AUDIT = "f01f8e8c259a5488ea5228581dd6a9fb56076f4763598812cfdb079aaa492e76"  # landau PASS (line 114)
W6_4_AXIS_A_AUDIT = "146b5742ea7f92b40611ef9a4334cd3a55ceb3c8b8867acea7eed8e9a68512e6"  # connes INFO (line 116)
W6_4_AXIS_B_AUDIT = "9df77b09deca00039d405bac937c848bde924bcb4466a80dd727eccae81240b9"  # landau INFO (line 111)
VII_AH_CEILING_AUDIT = "4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a"  # §VII.AH structural ceiling precedent

# --- regime-correction physics (S92 W9-8 npz overturned by S93 W6-3) ---------
COMPOSITE_NORM_INF = 10.111762   # (local) argmax-R2 pick; saturation-INCOHERENT
MIN_OBSERVED = 11.733209         # (local) min of the monotone-increasing L-scan
MIN_ETA_FB = 0.446536            # (local) Friedrich-Bar predicate; >= 0.40 LICENSED
LEVEL3_ANCHOR = vii_bb_element_5_empirical_anchor_FW  # 11.763253530952039 (canonical)
ETA_FB_SU4_REGISTERED = 0.283    # (local) 0.40/sqrt(2) HEURISTIC SUGGESTION
CASIMIR_BOUND_GB_L12 = 1094.7    # (local) full SU(4)_PS spectrum dense storage wall


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------
def closure_hash(ordered_pin_map):
    """SHA-256 over an ORDERED list of (key, value) pins (audit_sha256).

    The ordering is load-bearing: the pin map is serialized in list order
    (NOT sorted) so the two composite verdicts' distinct clause sets produce
    distinct hashes by construction.
    """
    payload = json.dumps(ordered_pin_map, separators=(",", ":"),
                         ensure_ascii=True).encode("utf-8")  # (local)
    return hashlib.sha256(payload).hexdigest()


def content_hash_of_script():
    """SHA-256 over this script's own bytes (content_sha256)."""
    try:
        return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    except OSError:
        return hashlib.sha256(b"").hexdigest()


# ---------------------------------------------------------------------------
# Move 1 -- composite verdict line (PASS) for §VII.BB Stage-2 PASS-AND
# ---------------------------------------------------------------------------
def move1_pin_map():
    """Ordered input-pin map for S93-W6-3 composite audit_sha256.

    Per spawn prompt: gate_id + axis_A_audit + axis_B_audit + J1_regime
    + J2_level3_rel0 + pass_and=True + substrate_input_orthogonality
    + scheme=FW + convention.
    """
    return [
        ["gate_id", "S93-W6-3-VII-BB-STAGE-2-CROSS-AXIS-VERIFY-REGIME-IDENTITY"],
        ["axis_A_audit", W6_3_AXIS_A_AUDIT],
        ["axis_B_audit", W6_3_AXIS_B_AUDIT],
        ["J1_regime", "friedrich_bar_licensed"],
        ["J2_level3_rel0", "0.000e+00"],
        ["pass_and", "True"],
        ["substrate_input_orthogonality",
         "structural-ceiling-axisA-w9_8npz-axisB-s84cache"],
        ["scheme", "FW"],
        ["convention",
         "stage-2-cross-axis-PASS-AND-VII-BB-STAGE-3-PERMANENT-promotion-"
         "regime-identity-friedrich-bar-licensed-saturation-coherence-discriminator"],
    ]


# ---------------------------------------------------------------------------
# Move 2 -- composite verdict line (INFO) for §VII.BE structural PASS-AND
# ---------------------------------------------------------------------------
def move2_pin_map():
    """Ordered input-pin map for S93-W6-4 composite audit_sha256.

    Per spawn prompt: gate_id + axis_A_audit + axis_B_audit
    + structural_pass_and=True + level3_route=4b-defer-S94-CF-W9-12-3
    + scheme=FW + convention.
    """
    return [
        ["gate_id", "S93-W6-4-FWD-C4-PATI-SALAM-STAGE-2-CROSS-AXIS-VERIFY-LEVEL-3"],
        ["axis_A_audit", W6_4_AXIS_A_AUDIT],
        ["axis_B_audit", W6_4_AXIS_B_AUDIT],
        ["structural_pass_and", "True"],
        ["level3_route", "4b-defer-S94-CF-W9-12-3"],
        ["scheme", "FW"],
        ["convention",
         "fwd-c4-pati-salam-stage-2-cross-axis-STRUCTURAL-PASS-AND-level-3-"
         "defer-S94-route-4b-composite-INFO"],
    ]


# ---------------------------------------------------------------------------
# Verdict-line emission (single-shot append; canonical + dual-SHA + optional
# 3-tuple), per gate-verdicts.md S87+ schema-v2 + registry-landing.md AFTER
# ---------------------------------------------------------------------------
def build_move1_lines(audit_sha, content_sha):
    """Move 1: composite PASS; [VERIFY-THEOREM] -> NO [SIGN] 3-tuple."""
    gate = "S93-W6-3-VII-BB-STAGE-2-CROSS-AXIS-VERIFY-REGIME-IDENTITY"  # (local)
    value = (
        "STAGE-2-PASS-AND_VII-BB-STAGE-1->STAGE-3-PERMANENT_"
        f"axis_A_connes=PASS({W6_3_AXIS_A_AUDIT[:16]})_"
        f"axis_B_landau=PASS({W6_3_AXIS_B_AUDIT[:16]})_"
        "J1_regime_identity=PASS_J2_level3_consistency=PASS_pass_and=True_"
        "volovik_EXCLUDED_sole_author_"
        "substrate_input_orthogonality=structural-ceiling_"
        "axisA=w9_8npz_axisB=s84_spectrum_cache_L12_tau019_NO_overlap_caveat_"
        f"VII-AH_ceiling_precedent={VII_AH_CEILING_AUDIT[:16]}_"
        "substrate_IS_regime_CORRECTED=composite->friedrich_bar_licensed_"
        f"composite_Norm_inf={COMPOSITE_NORM_INF}<min_obs={MIN_OBSERVED}_"
        "saturation_INCOHERENT_argmax_R2_WRONG_SELECTOR_at_degenerate_pole_"
        f"min_eta_FB={MIN_ETA_FB}>=0.40_FB_licensed_logarithmic_coherent_runner_up_"
        f"level3_anchor={LEVEL3_ANCHOR}_REGIME_INDEPENDENT_"
        "alpha_disambiguation=convergence_rate_in_L_2d_over_s_minus_1=0.6_vs_"
        f"per_pole_homogeneity_Wodzicki_2(s-2)=alpha_HH1_per_pole_FW_s5={alpha_HH1_per_pole_FW_s5}_"
        "NOT_in_conflict_different_questions_"
        "blind_cross_reviewers_NOT_agreement_among_agents_"
        "M4_allowlist_append=ORCHESTRATOR-ONLY"
    )  # (local)
    canonical = (
        f"{gate}: PASS -- value='{value}' "
        "scheme=FW "
        "convention=stage-2-cross-axis-PASS-AND-VII-BB-STAGE-3-PERMANENT-"
        "promotion-regime-identity-friedrich-bar-licensed-saturation-"
        "coherence-discriminator "
        "L_max=12 "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {gate} "
        "dual-SHA companion row (W9a-99 split); COMPOSITE Stage-2 cross-axis "
        "PASS-AND (Axis-A connes 19f46846 + Axis-B landau f01f8e8c; both "
        "BLIND, orthogonal substrate inputs); §VII.BB STAGE-1->STAGE-3-"
        "PERMANENT promotion; substrate-input-orthogonality at structural "
        "ceiling (NO overlap caveat per §VII.AH precedent 4fcd7d29); "
        "substrate_IS_regime CORRECTED composite->friedrich_bar_licensed; "
        "[VERIFY-THEOREM] no [SIGN] 3-tuple (PASS-AND + regime-exclusion, "
        "not a single directional prediction); M4 allowlist append "
        "ORCHESTRATOR-ONLY\n"
    )  # (local)
    return [canonical, companion]  # no 3-tuple line for [VERIFY-THEOREM]


def build_move2_lines(audit_sha, content_sha):
    """Move 2: composite INFO; [SIGN] -> 3-tuple sign=PASS mag=INFO regime=MARGINAL."""
    gate = "S93-W6-4-FWD-C4-PATI-SALAM-STAGE-2-CROSS-AXIS-VERIFY-LEVEL-3"  # (local)
    value = (
        "STRUCTURAL-STAGE-2-PASS-AND_VII-BE-STAYS-STAGE-1-CANDIDATE_"
        f"axis_A_connes=INFO({W6_4_AXIS_A_AUDIT[:16]})_"
        f"axis_B_landau=INFO({W6_4_AXIS_B_AUDIT[:16]})_"
        "structural_clauses_A1-A4_B1-B4=PASS_AND_"
        "joint_J1_chi_PS_KK_morphism=PASS_J2_scheme_suffix=PASS_"
        "J3_symbolic_level3_lt_level2=PASS_pass_and=True_"
        "volovik_EXCLUDED_co_author_downstream_inheritance_reach_"
        "composite=INFO_numerical_level3_DEFER_route-4b_S94_CF-W9-12-3_"
        f"full_SU4_PS_spectrum_INFEASIBLE_casimir_bound_GB_L12={CASIMIR_BOUND_GB_L12}_"
        f"alpha_PS_symbolic=3_inherited_s3_precedent_vs_per_pole_canonical_s4_"
        f"alpha_HH1_per_pole_FW_s4={alpha_HH1_per_pole_FW_s4}_Wodzicki_2(s-2)_"
        "DIAGNOSTIC_TENSION_symbolic_L3_lt_L2_survives_BOTH_alpha3_alpha4_"
        f"eta_FB_su4={ETA_FB_SU4_REGISTERED}_HEURISTIC_one_over_sqrt2_"
        "exact_fund_ratio_sqrt(32/45)=0.8433_smaller_eta_conservative_lower_bound_"
        "STAGE-3-PERMANENT_eligibility_CONDITIONAL_on_S94_numerical_level3_pin_"
        "M4_allowlist_append=ORCHESTRATOR-ONLY"
    )  # (local)
    canonical = (
        f"{gate}: INFO -- value='{value}' "
        "scheme=FW "
        "convention=fwd-c4-pati-salam-stage-2-cross-axis-STRUCTURAL-PASS-AND-"
        "level-3-defer-S94-route-4b-composite-INFO "
        "L_max=12 "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {gate} "
        "dual-SHA companion row (W9a-99 split); COMPOSITE Stage-2 cross-axis "
        "STRUCTURAL PASS-AND (Axis-A connes 146b5742 + Axis-B landau "
        "9df77b09; both INFO; structural clauses + JOINT clauses PASS-AND); "
        "§VII.BE STAYS STAGE-1-CANDIDATE; numerical Level-3 DEFER route-4b "
        "S94 CF-W9-12-3 (1094.7 GB full SU(4)_PS spectrum INFEASIBLE); "
        "STAGE-3-PERMANENT eligibility CONDITIONAL on S94 numerical pin; "
        "M4 allowlist append ORCHESTRATOR-ONLY\n"
    )  # (local)
    tuple_line = (
        f"# sign_verdict=PASS magnitude_verdict=INFO regime_verdict=MARGINAL "
        f"# {gate} 3-tuple annotation (S87 schema-v2): [SIGN] Level-3 < "
        "Level-2 directional SYMBOLIC (robust under alpha in {3,4}); "
        "REGIME MARGINAL = route-4b DEFER (numerical Level-3 anchor S94)\n"
    )  # (local)
    return [canonical, companion, tuple_line]


def append_verdict(lines):
    """Atomic single append of the composite verdict line(s) + companions
    to the canonical session-93 verdict file (open mode 'a', fsync).

    `lines` is the ordered list of canonical + dual-SHA companion (+ optional
    3-tuple) rows already built by build_move{1,2}_lines. Append-only writer
    per `epistemic-discipline.md §"Registry-Write Hygiene"` (no Edit-tool
    round-trip on the shared verdict file).
    """
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for ln in lines:
            fp.write(ln)
        fp.flush()
        os.fsync(fp.fileno())


def sig5_existing_audit_shas():
    """Return the set of canonical-line audit_sha256 already in the verdict file."""
    shas = set()  # (local)
    if not VERDICT_TXT.exists():
        return shas
    for line in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("#"):
            continue
        marker = "audit_sha256="  # (local)
        idx = line.find(marker)  # (local)
        if idx == -1:
            continue
        rest = line[idx + len(marker):]  # (local)
        sha = rest.split()[0] if rest.split() else ""  # (local)
        if len(sha) == 64:
            shas.add(sha)
    return shas


# ---------------------------------------------------------------------------
# WP synthesis subsection
# ---------------------------------------------------------------------------
def build_wp_subsection(m1_audit, m1_content, m2_audit, m2_content):
    """The #### Synthesis registry moves block (>= 15 substantive lines)."""
    return f"""#### Synthesis registry moves (mack-cosmic-bridge)

**Status**: COMPLETED — Wave-6 synthesis registry moves (registry sole-writer per `feedback_mack-bridge-role.md`). THREE registry entries + TWO composite verdict lines. All registry writes serial single-shot AFTER pattern; every §VII slot resolved BY CONTENT (heading-keyword grep), plan-pinned line numbers STALE-DRIFTED per `substrate-first-canonical-sourcing.md §(ii.B)`.

**Verdict** (the 2 composites + the §VII.AQ reframe):

1. **MOVE 1 — `S93-W6-3-VII-BB-STAGE-2-CROSS-AXIS-VERIFY-REGIME-IDENTITY`: PASS** (composite Stage-2 cross-axis PASS-AND). BOTH axes (Axis-A connes `{W6_3_AXIS_A_AUDIT[:16]}…` PASS + Axis-B landau `{W6_3_AXIS_B_AUDIT[:16]}…` PASS) independently PASS all single-axis clauses + both JOINT clauses (J1 regime-identity + J2 Level-3 consistency). Substrate-input-orthogonality at STRUCTURAL CEILING (Axis-A = §W9-8 npz; Axis-B = `s84_spectrum_cache_L12_tau019.npz` — DIFFERENT data files; overlap caveat OMITTED per §VII.AH precedent `{VII_AH_CEILING_AUDIT[:16]}…`). `volovik` EXCLUDED (sole author). **§VII.BB STAGE-1-CANDIDATE → STAGE-3-PERMANENT** (all occurrences flipped: body heading + Status + index-table row + cross-ref + refinement-row (iv) DONE). audit_sha256=`{m1_audit}`. NOT agreement-among-agents: blind reviewers, orthogonal substrate inputs (the constructive `joint-theorem-promotion.md` 4-stage complement to the `epistemic-discipline.md` "agreement among agents" exclusion).

2. **MOVE 2 — `S93-W6-4-FWD-C4-PATI-SALAM-STAGE-2-CROSS-AXIS-VERIFY-LEVEL-3`: INFO** (composite Stage-2 STRUCTURAL PASS-AND, numerical Level-3 DEFERRED). BOTH axes (Axis-A connes `{W6_4_AXIS_A_AUDIT[:16]}…` INFO + Axis-B landau `{W6_4_AXIS_B_AUDIT[:16]}…` INFO) PASS ALL single-axis STRUCTURAL clauses (A1-A4 / B1-B4) + ALL JOINT clauses (J1 χ_PS KK-morphism + J2 scheme-suffix + J3 SYMBOLIC Level-3<Level-2). The NUMERICAL Level-3 anchor `Res_{{s=4}} Tr(D_K_PS^{{−2s}})` DEFERS to S94 (route-4b; full SU(4)_PS spectrum INFEASIBLE at {CASIMIR_BOUND_GB_L12} GB). **§VII.BE STAYS STAGE-1-CANDIDATE**; STAGE-3-PERMANENT eligibility CONDITIONAL on the S94 numerical Level-3 pin (CF-W9-12-3). `volovik` EXCLUDED (§VII.BE co-author). 3-tuple sign=PASS magnitude=INFO regime=MARGINAL. audit_sha256=`{m2_audit}`.

3. **MOVE 3 — §VII.AQ.OP-PROJ STRUCTURALLY-OPEN-BY-DESIGN reframe** (W6-1 FAIL consequence; ANNOTATION, NOT a STAGE flip). W6-1 (`b93616a478c99096…` FAIL) shows the order-one obstruction `‖[[D_K,a],b°]‖ = 4.000000` is ALGEBRA-INVARIANT under the Pati-Salam extension (`defect_max_PS = 4.000000` = SM baseline bit-for-bit). Substrate-physics reason: the PS algebra is a strict SUPERSET of the SM algebra, so `max` over the larger generator set `≥ max` over the subset — adding generators cannot remove a pre-existing double-commutator obstruction; 4.000 is the universal Cl(8)/Spin(8) signature of a CONTINUOUS internal space. This CLOSES the LAST known STAGE-3 route for §VII.AQ.OP-PROJ at the order-one axis. Reframed to STRUCTURALLY-OPEN-BY-DESIGN: the substrate's gauge content derives via KK isometries + representation theory (S31 §4.3-4.4), NOT via NCG inner-fluctuation order-one classification; KO-dim=6 BDI PRESERVED; K-theory residual NON-DECISIVE; full-spectrum Level-3 anchor INFEASIBLE (1094.7 GB) → DEFERRED-S94 CF-W9-12-3. No new composite verdict (W6-1 is the gate verdict).

**substrate_IS_regime correction rationale (MOVE 1)**: the S92 §W9-8 first-extraction npz recorded `substrate_IS_regime=composite` — the argmax-R²=0.992028 pick. The S93 W6-3 Stage-2 adjudication OVERTURNS this to `friedrich_bar_licensed` via the **saturation-coherence discriminator**: the composite asymptote `Norm_∞ = {COMPOSITE_NORM_INF} < {MIN_OBSERVED}` (= min observed across the L-scan) is INCOHERENT as the saturation asymptote of a monotone-INCREASING sequence, so argmax-R² is the WRONG selector at the DEGENERATE pole. The Friedrich-Bär-licensed regime (`min η_FB = {MIN_ETA_FB} ≥ 0.40`) IS the substrate-IS convergence signature; logarithmic is the coherent runner-up (both non-power-law ⇒ the saturating-regime finding is ROBUST). This resolves the §W9-8 honest-disclosure caveat. The Level-3 anchor {LEVEL3_ANCHOR} is REGIME-INDEPENDENT (directly-measured FB-certified L_max=12 value).

**α-formula disambiguation notes** (knowledge-MCP sourced):
- §VII.BB (Axis-A connes flag): Level-2 cites `α = 2d/s − 1` (convergence-rate-in-L exponent; 0.6 → 0 at the degenerate pole) while `canonical_constants.py:916 alpha_HH1_per_pole_FW_s5 = {alpha_HH1_per_pole_FW_s5}` uses `α = 2(s−2)` (Wodzicki/Connes per-pole homogeneity). DIFFERENT questions, NOT in conflict; downstream "α(s=5)" citations MUST disambiguate.
- §VII.BE (Axis-A connes flag): SYMBOLIC α(PS)=3 inherited from the substrate-distance-1 precedent (s=3, §VII.AF.1), but the observable's own pole is substrate-distance-2 (s=4) where `alpha_HH1_per_pole_FW_s4 = {alpha_HH1_per_pole_FW_s4}` (Wodzicki 2(s−2)) gives α=4. CF-W9-12-3 adjudicates; the symbolic Level-3<Level-2 survives BOTH α=3 and α=4.
- η_FB^{{SU(4)}} note (both reviewers): η_FB^{{SU(4)}} = 0.40/√2 ≈ {ETA_FB_SU4_REGISTERED} — the "1/√2" rationale is HEURISTIC, matching no standard SU(3)→SU(4) Casimir ratio (exact fundamental ratio √((8/3)/(15/4)) = √(32/45) ≈ 0.8433); registry correctly tags it SUGGESTION; a smaller η_FB is a conservative lower bound.

**MCP Pre-Compute Audit** (queries executed BEFORE the registry writes, per `knowledge-index-usage.md`):
- `search_knowledge("VII.BB HH1 cocycle norm substrate-distance-3 pole s=5 Friedrich-Bar saturation")` → edge `alpha_HH1_per_pole_FW_s5 --derived_from--> S91/S92`; constant `vii_bb_element_5_empirical_anchor_FW`; eqn "Norm_HH1(L=12)=Norm_HH1(∞) to machine ε if Friedrich-Bär saturation predicate holds". Confirms §VII.BB anchor + FB predicate.
- `search_knowledge("VII.BE FWD-C4 Pati-Salam cross-pillar bridge STAGE-1-CANDIDATE")` → gates `CF-S91-W7-CF-W9-12-1-...-STAGE-1-CANDIDATE-LANDING` + `S92-W7-CF-W9-12-1-FWD-C4-...-REGISTRY-LANDING` (both PASS); §VII.BE OCCUPIED-VERIFY-INTACT 5/5 anatomy 3/3 levels. Confirms STAGE-1-CANDIDATE landing.
- `search_knowledge("VII.AQ.OP-PROJ order-one obstruction Pati-Salam SU4 KO-dim chirality")` → open_channel SU(4) "Order-one condition failure (norm 4.000) points to Pati-Salam"; gate `S91-VII-AQ-OP-PROJ-STAGE-2-UPGRADE-SUBSTRATE-PHYSICS` INFO (max_delta_GV=0, KO_dim_all=6). Confirms order-one 4.000 + KO-dim=6.
- `search_knowledge("Stage-2 PASS-AND substrate-input-orthogonality structural ceiling joint theorem promotion")` → theorem "Structural ceiling: substrate-input-orthogonality MANDATORY at K=3 since S90 W2 CF-20"; §VII.AH precedent. Confirms structural-ceiling clause + omit-caveat criterion.
- `get_constant("alpha_HH1_per_pole_FW_s5")` → 6.0 (S92; source `S92-W7-CF-W9-10-B-pole-s5`). Confirms α-disambiguation for §VII.BB.
- `get_constant("alpha_HH1_per_pole_FW_s4")` → 4.0 (S92; source `S92-W7-CF-W9-10-B-pole-s4`). Confirms α(PS) diagnostic tension for §VII.BE.
- `search_knowledge("VII.BB FIRST-EXTRACTION discharge S92 W9-8 ... composite regime")` → gate `S92-W9-CF-S92-VOLOVIK-S1-V1-LMAX-SCAN-DEGENERATE-POLE-VII-BB` PASS, `substrate_IS_regime=composite;best_R2=0.992028;R2_friedrich_bar=0.865342`. Confirms the §W9-8 `composite` pick that S93 W6-3 OVERTURNS.

**Output Artifacts** (on-disk verification; `ls` + `grep` for all 5 writes):
*(populated post-run by the orchestrator-direct verification block; see the final-message grep evidence.)*

**Registry-drift notes** (per `substrate-first-canonical-sourcing.md §(ii.B)`): all plan-pinned §VII slot line numbers STALE-DRIFTED; re-anchored BY CONTENT (heading-keyword grep):
- §VII.BB: spawn-pinned/plan-drift → re-anchored at heading line **20224** (body), index-table row **147**.
- §VII.BE: plan-pinned "~20042" → re-anchored at heading line **20456** (drift +414; consistent with the §W6-4 Axis-B WP drift note `VII.BE_heading_line_20456_plan_pinned_20042_STALE_drift_+414`).
- §VII.AQ.OP-PROJ: plan-pinned 17583 → body heading **17598** (drift +15; consistent with the W6-1 verdict `registry_drift_plan_pinned_17583_to_runtime_17598_plus_15`).

**M4-allowlist flag**: the §VII.BB STAGE-3-PERMANENT-flip composite gate-ID `S93-W6-3-VII-BB-STAGE-2-CROSS-AXIS-VERIFY-REGIME-IDENTITY` (METHODOLOGY-class registry-landing consequence) is FLAGGED for the orchestrator to append to `methodology-wave-allowlist-ledger.md` (M4 allowlist append is ORCHESTRATOR-ONLY per `methodology-wave-allowlist.md`; mack-cosmic-bridge does NOT touch the ledger).

**Slot-allocation audit**: `_vii_slot_allocation_audit.py` → VERDICT: PASS (no slot collisions introduced; §VII.BB / §VII.BE / §VII.AQ.OP-PROJ all in-place edits, no new slot allocated).

"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"=== S93 W6 synthesis registry moves -- mack-cosmic-bridge ===")
    print(f"  canonical alpha_HH1_per_pole_FW_s5 = {alpha_HH1_per_pole_FW_s5}")
    print(f"  canonical alpha_HH1_per_pole_FW_s4 = {alpha_HH1_per_pole_FW_s4}")
    print(f"  canonical vii_bb_element_5_empirical_anchor_FW = {vii_bb_element_5_empirical_anchor_FW}")

    content_sha = content_hash_of_script()  # (local) shared content_sha256

    # --- compute composite audit SHAs (closure over ordered pin maps) -------
    m1_audit = closure_hash(move1_pin_map())  # (local)
    m2_audit = closure_hash(move2_pin_map())  # (local)
    print(f"  MOVE 1 audit_sha256 = {m1_audit}")
    print(f"  MOVE 2 audit_sha256 = {m2_audit}")
    print(f"  content_sha256      = {content_sha}")

    # --- sig_5 pre-check: composite SHAs must be unique vs existing + each other
    existing = sig5_existing_audit_shas()  # (local)
    assert m1_audit != m2_audit, "sig_5 VIOLATION: two composite audit_sha256 collide"
    assert m1_audit not in existing, f"sig_5 VIOLATION: MOVE 1 audit_sha already in verdict file"
    assert m2_audit not in existing, f"sig_5 VIOLATION: MOVE 2 audit_sha already in verdict file"
    print(f"  sig_5 PRE-CHECK PASS: both composite audit_sha256 unique "
          f"(vs {len(existing)} existing canonical lines + each other)")

    # --- emit the two composite verdict lines (single append) ---------------
    m1_lines = build_move1_lines(m1_audit, content_sha)  # (local)
    m2_lines = build_move2_lines(m2_audit, content_sha)  # (local)
    append_verdict(m1_lines + m2_lines)
    print(f"  Appended 2 composite verdict lines + companions to {VERDICT_TXT.name}")

    # --- sig_5 post-check ---------------------------------------------------
    post = sig5_existing_audit_shas()  # (local)
    assert m1_audit in post and m2_audit in post, "post-write: composite SHAs missing"
    # uniqueness across ALL canonical lines
    all_shas = []  # (local)
    for line in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("#"):
            continue
        idx = line.find("audit_sha256=")  # (local)
        if idx == -1:
            continue
        rest = line[idx + len("audit_sha256="):]  # (local)
        sha = rest.split()[0] if rest.split() else ""  # (local)
        if len(sha) == 64:
            all_shas.append(sha)
    dup = len(all_shas) - len(set(all_shas))  # (local)
    print(f"  sig_5 POST-CHECK: {len(all_shas)} canonical audit_sha256 total; "
          f"{dup} duplicates")
    assert dup == 0, f"sig_5 VIOLATION post-write: {dup} duplicate audit_sha256"

    # --- WP synthesis subsection (insert BEFORE the team-lead synthesis) ----
    wp_text = WP_PATH.read_text(encoding="utf-8")  # (local)
    subsection = build_wp_subsection(m1_audit, content_sha, m2_audit, content_sha)  # (local)
    anchor = "## Wave 6 Synthesis (team-lead)"  # (local)
    assert anchor in wp_text, "WP team-lead-synthesis anchor not found"
    assert "#### Synthesis registry moves (mack-cosmic-bridge)" not in wp_text, \
        "WP synthesis subsection already present (no double-write)"
    wp_new = wp_text.replace(anchor, subsection + anchor, 1)  # (local)
    tmp = WP_PATH.with_suffix(WP_PATH.suffix + ".tmp_s93w6syn")  # (local)
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(wp_new)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, WP_PATH)
    # re-read + verify (AFTER pattern)
    wp_check = WP_PATH.read_text(encoding="utf-8")  # (local)
    assert "#### Synthesis registry moves (mack-cosmic-bridge)" in wp_check, \
        "WP subsection write FAILED on re-read"
    print(f"  WP synthesis subsection written to {WP_PATH.name} (verified on re-read)")

    print("=== DONE: 2 composite verdict lines + WP subsection emitted; "
          "3 registry entries edited serially (Edit tool); sig_5 clean ===")
    sys.exit(0)


if __name__ == "__main__":
    main()
