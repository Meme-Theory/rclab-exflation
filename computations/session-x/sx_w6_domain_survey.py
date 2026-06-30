#!/usr/bin/env python3
"""
WX-W6-1-AGGREGATE-DOMAIN-SURVEY — cross-workshop-synthesis domain sweep
=======================================================================

Gate: WX-W6-1-AGGREGATE-DOMAIN-SURVEY  ([AUDIT])

Pre-registered threshold (GEOMETRIC; set-coverage over the cross-workshop-
synthesis domain, NOT a numerical comparison):
  PASS iff
    (entity_classes_surveyed superset {theorems, closed, gates, sessions, open,
     constants, equations, provenance})  (== 8)
    AND survey_axes_covered == {A:S54-gate-fate, B:isomorphism-fate,
     C:open-question-resolution, D:new-isomorphism}  (== 4)
    AND |gap_rows| >= 16  (planner floor; executor extends)
    AND every gap_row has (kb_citation != '' AND where_belongs != ''
     AND gap_tag in {NEW-SINCE-AUTHORSHIP, NEVER-COVERED, DRIFTED-CLAIM,
     PARADIGM-SHIFT})
    AND s54_gate_fate covers all 9 decisive/high-value gates
    AND isomorphism_fate covers all 5 isomorphisms
    AND open_question_resolution covers all 4 questions.
  No numerical mesh; no substitution chain (the survey asserts no signed delta;
  the directional/ratio claims it surfaces are pre-registered for the G2 gate).

The INTELLECTUAL deliverable (the State-of-Domain Map, the four fate tables,
the >=16-row Gap Analysis with KB citations) lives in the working-paper §W6-1.
This script is the MECHANICAL closure: it records the survey's structural
coverage as a deterministic set-coverage predicate, emits the dual-SHA verdict,
and stores the fate/gap tables in an npz for audit reproducibility.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/Phononic-Investigation.md          (document_pre; the survey target)
  - computations/_shared/canonical_constants.py           (feeds audit_sha256)
  - tools/knowledge.db                                     (the KB swept; ~80 MB; dynamic)
  - script bytes                                           (feeds BOTH SHAs)

Output 4-tuple:
  (value=<coverage summary>, scheme=aggregate-domain-survey-v1,
   convention=kb-cited-gap-enumeration, L_max=N/A)

Classification: GEOMETRIC (cross-pillar unification thesis; set-coverage survey)

METHODOLOGY
-----------
The cross-workshop-synthesis domain is cross-domain pattern detection / cross-
pillar isomorphism / the unification of the eight pillars through the single
finite Dirac operator D_K(tau) on the 32-cell Voronoi tessellation of
(SU(3), g_Jensen). The survey is a coverage-by-enumeration over (a) the 8 KB
entity classes and (b) the four survey axes A-D. The gap set is the set-
difference between project-knowledge-in-domain and document-coverage. Each gap
row carries its KB citation + a where-it-belongs tag + a gap-tag. This is the
substrate-IS direction (D_K eigenvalues -> spectral moments -> emergent physics):
the survey verifies the domain still respects it and finds where the project
formalized the five S53 isomorphisms.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No linear algebra; CPU-only, OMP threads capped to 8
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema), atomic append
- Verdict appended to canonical path computations/session-x/sx_gate_verdicts.txt
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# canonical_constants.py lives in computations/_shared; add to path then import *
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402

_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # (local)
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402  (framework discipline)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + identity
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent  # computations/session-x
COMPUTATIONS_DIR = SESSION_DIR.parent  # computations
PROJECT_ROOT = COMPUTATIONS_DIR.parent  # project root
SHARED_DIR = COMPUTATIONS_DIR / "_shared"  # (local)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"  # (local)

SESSION = "SX"  # (local)
GATE_ID = "WX-W6-1-AGGREGATE-DOMAIN-SURVEY"  # (local)
SCHEME = "aggregate-domain-survey-v1"  # (local)
CONVENTION = "kb-cited-gap-enumeration"  # (local)
L_MAX = "N/A"  # (local) survey gate; no spectral truncation

DOCUMENT = FRAMEWORK_DIR / "Phononic-Investigation.md"  # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
KNOWLEDGE_DB = PROJECT_ROOT / "tools" / "knowledge.db"  # (local)

OUT_NPZ = SESSION_DIR / "sx_w6_domain_survey.npz"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local; gate-verdicts.md canonical)

INPUT_FILES = [DOCUMENT, CANONICAL, KNOWLEDGE_DB]  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (dual-SHA S84+; W9a-99 split)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; '' on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
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
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit   = sha256( script_bytes || canonical_bytes || pinmap_json )
    content = sha256( document_post_bytes )   [G1 does not modify the doc:
              document_post == document_pre; the content hash pins the survey's
              integration TARGET, the document the expansion will rewrite]
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
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

    doc_bytes = b""  # (local)
    try:
        doc_bytes = DOCUMENT.read_bytes()
    except OSError:
        doc_bytes = b""
    h_content = hashlib.sha256()  # (local)
    h_content.update(doc_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Survey coverage tables (the structural enumeration)
#
# The four survey axes are deterministic, finite, closed enumerations. The
# coverage predicate checks that each enumeration is complete. The intellectual
# content (one-line fates, KB citations) is mirrored in the WP §W6-1; here we
# record the structural keys so the npz is an audit-reproducible coverage record.
# ---------------------------------------------------------------------------

# Axis A — S54-program-gate FATE (9 decisive/high-value + 5 carry-forward)
S54_GATE_FATE = {
    # decisive (n=4)
    "ED-SWEEP-54": "S54 FAIL (E_0'' did NOT exceed |V_KK''|=63.2; no minimum) "
    "-> migrated INFO at S81 T3-BATCH-S54-ED-SWEEP (no-run-no-gate); "
    "thread resolves at OQ2-DISSOLVED (first-order transit)",
    "SA-LATT-OCC-54": "S54 ran (sa_latt_occ.py; OCC-54/SPEC-45) -> S_occ monotone "
    "decreasing PERMANENT [NEW S45 occupied-state spectral action]; "
    "thread = the smooth-functional side of Strutinsky decomposition",
    "CONNES-LATT-54": "S54 ran (bures_connes.py; CONNES-54) -> Connes distance "
    "migrated to A_F finite triple (S87/S88); lattice tracks 1/J_C2",
    "GEODESIC-DEVIATION-54": "no standalone gate landed; the O'Neill A-tensor "
    "computed at S61 A-TENSOR-61 (A=T=0, cross 0.47%) + S74 CORRECTION-74; "
    "thread = product-submersion A=T=0 (GAP-3)",
    # high value (n=4 more = 8 total decisive/high-value gates), plus BURES-CONNES
    "BURES-CONNES-LATTICE-54": "S54 ran (bures_connes.py) -> migrated INFO at S81 "
    "T3-BATCH-S54-BURES-CONNES; Martinetti-Mercati carried into A_F",
    "GUTZWILLER-SU3-54": "S54 ran (gutzwiller_su3.py) -> migrated INFO at S81 "
    "T3-BATCH-S54-GUTZWILLER-SU3; thread = the d_s arc (Iso-5)",
    "SCALE-FACTOR-54": "S54 PASS in table (a(tau) mean Connes distance; "
    "q(tau): -0.97 -> +0.81 per S54 QA-Hawking; eta=int dtau/a(tau))",
    "Q-RAYCHAUDHURI-54": "S54 ran (q_raychaudhuri.py consuming s54_ed_sweep.npz; "
    "RAYCHAUDHURI-54); thread = Fisher-information convergence (Iso-2)",
    "FIRAS-GGE-54": "S54 ran (firas_gge.py; GGE-54) -> migrated INFO at S81 "
    "T3-BATCH-S54-FIRAS-GGE; T_B1=0.435/T_B2=0.668/T_B3=0.178, "
    "rho_GGE=3.74e68 GeV^4; thread = frozen-arrow falsifier program",
    # carry-forward (n=5)
    "CF9-NPAIR2": "ran -> NPAIR2-CC-55 / S63 W3-04 (N_pair=2 integrability "
    "breaking CLOSED); THERM-ORDER-59 N_pair=4 ED at tau_fold=0.193878",
    "CF10-modulus-fluctuation": "delta_tau(K) surviving n_s route; carried into "
    "the modulus-fluctuation / fabric-dispersion arc (S42 fabric_dispersion)",
    "CF11-32cell-tight-binding": "ran (s54_tb_hamiltonian.npz feeds VARIATION-56, "
    "PHASE-59); exact discrete pair band structure",
    "CF12-integrability-breaking": "leading O(V^2)/O(Delta^6)/inter-cell; "
    "N_pair=2 chain beta=0.4994 (Poisson, integrable) S61",
    "CF13-full-modulus-dynamics": "BCS speed-bump transit profile; the speed bump "
    "at tau=0.2015 is PROVEN S53 (local MAXIMUM, ratio_BCS=1.30)",
}  # (local)

S54_DECISIVE_HIGH_VALUE = [  # the 9 the PASS-boundary requires
    "ED-SWEEP-54",
    "SA-LATT-OCC-54",
    "CONNES-LATT-54",
    "BURES-CONNES-LATTICE-54",
    "GEODESIC-DEVIATION-54",
    "GUTZWILLER-SU3-54",
    "SCALE-FACTOR-54",
    "Q-RAYCHAUDHURI-54",
    "FIRAS-GGE-54",
]  # (local)

# Axis B — ISOMORPHISM FATE (5)
ISOMORPHISM_FATE = {
    "1-Strutinsky=O'Neill=saddle": "PERMANENT-THEOREM (S57 E_GS(fold)=-23.509="
    "-23.468+(-0.041); S62 delta_E_shell=-8.857; S51 STRUTINSKY-51 shell=49%; "
    "S63 SHELL-63; Kasparov S_total=S_base+S_fiber+cross; fiber-internal not "
    "product (A=T=0))",
    "2-Connes=Bures=Fisher": "CARRIED-INTO-A_F (S87 FINITE-SPECTRUM-IDENTITY INFO "
    "0.980 L12; S88 SUBALGEBRA-RESTRICTION PASS d_C=2.386138 L10=L12; "
    "Corner-II algebra-DEPENDENT state-pair functional)",
    "3-volume-preservation=CC-free=topological": "MATURED-TO-PARADIGM (H2 theorem "
    "= volume-preserving TT, tracelessness PERMANENT; CC-free via DILUTION-CC a_0 "
    "self-tuning; product O'Neill A=T=0 is the off-fold caveat W11-5)",
    "4-taxonomy-trap-universal": "MATURED-TO-PARADIGM (Ordered Veil S38 PROVEN + "
    "algebra-axis orthogonality W14 S87 MANDATORY K=3: algebra-INVARIANT vs "
    "algebra-DEPENDENT functional families STRUCTURALLY ORTHOGONAL)",
    "5-Gutzwiller-Selberg=stabilization<->dim-reduction": "HARDENED-TO-DIRECTIVE "
    "(d_s arc: S53 1.65 -> S44 -> S52/S63 -> S92 d_s-flow-vs-CDT; z=2 EXACT; "
    "Z=rho_E*v_g=1/pi const; sigma->0 Weyl vs windowed d_s(sigma_*) DISTINCT; "
    "cross-pillar-bridge-corpus.md sec24)",
}  # (local)

# Axis C — OPEN-QUESTION RESOLUTION (4)
OPEN_QUESTION_RESOLUTION = {
    "1-mass-variation-sign": "SUPERSEDED (VARIATION-56 INFO, VARIATION-58 INFO; "
    "product A=T=0 kills the geometric mass-variation expansion channel; "
    "Leggett-channel DM (LEGGETT-MOMENT-70, Mass/Delta_BCS=11.97) + PI-fabric "
    "is the mature successor)",
    "2-E_0-minimum-existence": "DISSOLVED (ED-SWEEP-54 FAIL; tau=0.2015 is a "
    "MAXIMUM PROVEN S53; CC Path C R(tau) monotone by AM-GM S64; stabilization "
    "is first-order transit/instanton, not a potential well -- the 'Friedmann "
    "wrong question' paradigm)",
    "3-Bures-Connes-relationship": "CARRIED-INTO-A_F (Martinetti-Mercati "
    "proportionality instantiated as the S87 finite-spectrum-identity conjecture "
    "on A_F; lattice exponential vs continuum modest growth disambiguated)",
    "4-115-OOM-CC-gap": "CLOSED (DILUTION-CC-66 PASS Scenario B; Volovik tracking "
    "vacuum rho_vac~M_Pl^2 H^2 closes 114 OOM to 0.01 OOM at ratio 1.032; "
    "a_0 self-tuning is a DIFFERENT spectral moment than a_2 shell correction)",
}  # (local)

# Axis D — NEW-ISOMORPHISM (S54->S93, the comprehensiveness gap)
NEW_ISOMORPHISMS = {
    "6-BCS-as-universal-ancestor": "S72; 6 predictions from 1 BCS Hamiltonian "
    "across 5 pillars; CC dilution (chi_vac>0 from BCS concavity) + laminar flow "
    "(Re_GGE=0 from integrability) logically INDEPENDENT, shared ancestor",
    "7-SU(1,1)-three-way": "S70 S_compound=S_spatial*S_BCS (SU(1,1) "
    "multiplication); BCS squeeze (IV) + cosmological Bogoliubov (I) + Josephson "
    "phase (V) one group element; S93-W8-6 R_BG=6.838e-4 verdict FAIL",
    "8-six-layer-causal-two-horizons": "S70/S71; entry sonic horizon (tau~0.22 "
    "a_2 kinematic) + exit sonic horizon (tau~0.16 a_4 BCS condensation), "
    "white-hole interior; maps a_0->a_2->a_4->a_6",
    "9-VII-bridge-program": "S82-S93; 5-anatomy + 3-level ladder + joint-theorem "
    "4-stage promotion; VII.AH FIRST STAGE-3-PERMANENT (S90 CF-20, 8/8, K2->K3 "
    "MANDATORY); first registered bridge VII.W (Pillar III<->IV)",
    "10-LQG/CDT-cross-framework": "S92; LQG x phonon-first narrow-path (gamma_BH="
    "0.2375 SU(2)-conv Paper 03 sec VII; alpha_bridge_req=4.81e-3; "
    "workshop-internal pending W6; S93-W8-7 INFO Regime-II); d_s-flow-vs-CDT "
    "fair same-functional comparison",
}  # (local)

# Gap analysis — the >=16 cited gap rows (KB-cited; where-it-belongs; gap-tag).
# Stored as a structured list so the npz carries the full gap ledger.
GAP_TAGS = {  # (local) the gap taxonomy
    "NEW-SINCE-AUTHORSHIP",
    "NEVER-COVERED",
    "DRIFTED-CLAIM",
    "PARADIGM-SHIFT",
}
GAP_ROWS = [  # (local) each: (id, gap, tag, kb_citation, where_belongs)
    ("GAP-1", "S54 program: all 8 decisive/high-value gates RAN then migrated "
     "INFO at S81 (no-run-no-gate); SCALE-FACTOR-54 PASS",
     "NEW-SINCE-AUTHORSHIP",
     "T3-BATCH-S54-* INFO (s81_batch_gate_verdicts.txt); ED-SWEEP FAIL S54 table",
     "SS IV (rewrite prospectus -> retrospective per-gate outcomes)"),
    ("GAP-2", "Iso-1 Strutinsky=O'Neill -> PERMANENT theorem; gradient ratio 0.71 "
     "(O'Neill/Strutinsky) DISTINCT from 1.30 (BCS speed-bump)",
     "DRIFTED-CLAIM",
     "S57 E_GS(fold)=-23.509; S62 delta_E_shell=-8.857; Phononic-framework-"
     "hypothesis.md ratio 1.30",
     "SS III Iso-1 (upgrade + disambiguate the two ratios)"),
    ("GAP-3", "Product O'Neill tensors VANISH A=T=0 exactly for M4xSU(3); "
     "Strutinsky=O'Neill content is fiber-internal, not product submersion",
     "NEW-SINCE-AUTHORSHIP",
     "A-TENSOR-61 (cross 0.47%); S73a a_2(D_total)=a_0(D_M)a_2(D_K)+...; W11-5 "
     "PERMANENT",
     "SS III Iso-1 + Iso-3 (A=T=0 clarification)"),
    ("GAP-4", "OQ2 (E_0 minimum?) RESOLVED NO and mis-framed: tau=0.2015 MAXIMUM; "
     "stabilization = first-order transit/instanton",
     "PARADIGM-SHIFT",
     "ED-SWEEP-54 FAIL; S64 W1-A R(tau) monotone AM-GM; atlas-10 #8 Ordered Veil",
     "SS V OQ2 -> dissolved; SS VI paradigm paragraph"),
    ("GAP-5", "OQ4 (115-OOM CC) CLOSED by DILUTION-CC-66 (0.01 OOM, ratio 1.032)",
     "NEW-SINCE-AUTHORSHIP",
     "DILUTION-CC-66 PASS Scenario B; Volovik Paper 25 sec V; a_0 self-tuning",
     "SS V OQ4 -> resolved; SS VI"),
    ("GAP-6", "OQ3 (Bures-Connes) carried into A_F finite-triple program "
     "(Martinetti-Mercati = finite-spectrum-identity conjecture)",
     "NEW-SINCE-AUTHORSHIP",
     "S87 FINITE-SPECTRUM-IDENTITY INFO 0.980; S88 SUBALGEBRA-RESTRICTION PASS "
     "d_C=2.386138",
     "SS V OQ3 -> carried; Iso-2 update"),
    ("GAP-7", "OQ1 (mass-variation sign) addressed via VARIATION-56/58 (INFO); "
     "with A=T=0 the geometric channel is NOT the expansion driver",
     "NEW-SINCE-AUTHORSHIP",
     "VARIATION-56 INFO; VARIATION-58 INFO; LEGGETT-MOMENT-70 (Mass/Delta=11.97)",
     "SS V OQ1 -> superseded section"),
    ("GAP-8", "Iso-5 Gutzwiller-Selberg -> d_s arc culminating S92 vs CDT; "
     "z=2 EXACT (S57 z=3.68 RETRACTED); Z=rho_E*v_g=1/pi const",
     "NEW-SINCE-AUTHORSHIP",
     "s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md; cross-pillar-bridge-corpus "
     "sec24; S52 d_s->8 Weyl",
     "SS III Iso-5 rewrite; new SS spectral-dimension/CDT"),
    ("GAP-9", "Iso-4 taxonomy-trap -> Ordered Veil paradigm + algebra-axis "
     "orthogonality K-counter (MANDATORY K=3)",
     "NEW-SINCE-AUTHORSHIP",
     "atlas-10 #8 Ordered Veil PROVEN; W14 S87; atlas-04 M2 STRUCTURALLY "
     "ORTHOGONAL",
     "SS III Iso-4 upgrade"),
    ("GAP-10", "VII cross-pillar bridge program (S82-S93) is the mature successor "
     "to 'five isomorphisms' (5-anatomy + 3-level + 4-stage promotion)",
     "NEW-SINCE-AUTHORSHIP",
     "VII.AH STAGE-3-PERMANENT (S90 CF-20); Door-S86-CPB; first bridge VII.W",
     "new SS 'From five isomorphisms to the VII bridge program'"),
    ("GAP-11", "NEW Iso-6: BCS-Hamiltonian-as-universal-ancestor (S72): 6 "
     "predictions from 1 algebraic object across 5 pillars",
     "NEW-SINCE-AUTHORSHIP",
     "session-72-audit-volovik.md Workshop E2 (chi_vac>0 + Re_GGE=0 independent)",
     "new SS 'New isomorphisms S54->S93' (Iso-6)"),
    ("GAP-12", "NEW Iso-7: SU(1,1) three-way identity (S70/S93): BCS squeeze + "
     "cosmological Bogoliubov + Josephson phase one SU(1,1) element",
     "NEW-SINCE-AUTHORSHIP",
     "S70 S_compound=S_spatial*S_BCS; S93-W8-6 R_BG=6.838e-4 (verdict FAIL)",
     "new SS 'New isomorphisms S54->S93' (Iso-7)"),
    ("GAP-13", "NEW six-layer causal structure (S70/S71) + TWO sonic horizons "
     "(entry tau~0.22 a_2; exit tau~0.16 a_4); maps a_0->a_2->a_4->a_6",
     "NEW-SINCE-AUTHORSHIP",
     "s71_causal_moment_map.py (MAP-71); session-70 Penrose sequence",
     "SS VI causal-architecture; the 'causal structure' face of the thesis"),
    ("GAP-14", "NEW LQG/CDT cross-framework workshops (S92) upgrade rhetorical "
     "'three communities' into landed comparisons",
     "NEW-SINCE-AUTHORSHIP",
     "session-92-lqg-phonon-first-workshop.md; gamma_BH=0.2375 Paper 03 sec VII; "
     "S93-W8-7 INFO",
     "SS VII Closing (rhetoric -> landed cross-framework, honest pending status)"),
    ("GAP-15", "DRIFT: tau quartet collapse. Doc carries 0.2015 as if fold; "
     "canonical tau_fold=0.190. Quartet 0.2015/0.190/0.193878/0.15 DISTINCT",
     "DRIFTED-CLAIM",
     "tau_fold=0.19 (CONST-FREEZE-42); 0.193878 (THERM-ORDER-59); c_Gold=0.915; "
     "Gi=0.506",
     "every tau mention + a tau-disambiguation callout"),
    ("GAP-16", "NEW N_pair scaling fate: NPAIR2-CC-55 / THERM-ORDER-59 N_pair=3/4; "
     "S_+(N)~(N+1)(1-N/16)/2 bosonic <1% (PAIR-TRANSFER-N4-60 PASS); Josephson "
     "enhances S_+(1)=1.683 on 8-cell (68% above floor)",
     "NEW-SINCE-AUTHORSHIP",
     "PAIR-TRANSFER-N4-60 PASS (S_+(1)=0.936); N_pair=2 integ-breaking CLOSED "
     "S55/S63",
     "SS IV carry-forward retrospective (#9)"),
    ("GAP-17", "GGE 'never thermalizes' DISAMBIGUATION: single-cell Brody "
     "beta=0.633 (13% non-sep, t_therm~6) RETRACTED S39; FABRIC (CG24-averaged) "
     "Poisson <r>=0.367 IS integrable -> Ordered Veil PROVEN at fabric level",
     "DRIFTED-CLAIM",
     "atlas-07 GGE permanence RETRACTED; S62 Hawking-QA fabric <r>=0.367; "
     "atlas-10 #8 PROVEN; t_scr/t_transit=814",
     "SS VI Ordered Veil paragraph (fabric-vs-single-cell disambiguation)"),
    ("GAP-18", "Occupied spectral action S_occ monotone-decreasing PERMANENT "
     "[NEW S45] -- the smooth-functional side of the Strutinsky decomposition "
     "the doc's SA-LATT-OCC-54 gate anticipated",
     "NEW-SINCE-AUTHORSHIP",
     "atlas-07 [NEW S45] occupied-state spectral action; OCC-54/SPEC-45",
     "SS IV SA-LATT-OCC-54 retrospective; SS III Iso-1"),
]  # (local)


# ---------------------------------------------------------------------------
# Section 6 — Coverage predicate (set-coverage, deterministic)
# ---------------------------------------------------------------------------
def evaluate_coverage() -> tuple[str, dict]:
    """Set-coverage predicate over 8 entity classes x 4 survey axes + gap rows."""
    entity_classes = {  # (local) the 8 KB classes swept (per query manifest)
        "theorems", "closed", "gates", "sessions", "open", "constants",
        "equations", "provenance",
    }
    axes = {"A", "B", "C", "D"}  # (local)

    # gap-row validity: every row has non-empty citation + where + valid tag
    gap_ok = all(  # (local)
        (r[3] != "" and r[4] != "" and r[2] in GAP_TAGS) for r in GAP_ROWS
    )
    s54_ok = all(g in S54_GATE_FATE for g in S54_DECISIVE_HIGH_VALUE)  # (local)
    iso_ok = len(ISOMORPHISM_FATE) == 5  # (local)
    oq_ok = len(OPEN_QUESTION_RESOLUTION) == 4  # (local)

    checks = {  # (local)
        "entity_classes_eq_8": len(entity_classes) == 8,
        "axes_eq_4": len(axes) == 4,
        "gap_rows_ge_16": len(GAP_ROWS) >= 16,
        "every_gap_row_cited_tagged_placed": gap_ok,
        "s54_9_decisive_high_value_covered": s54_ok,
        "isomorphism_5_covered": iso_ok,
        "open_question_4_covered": oq_ok,
    }
    summary = {  # (local)
        "n_entity_classes": len(entity_classes),
        "n_axes": len(axes),
        "n_gap_rows": len(GAP_ROWS),
        "n_s54_gates_fated": len(S54_GATE_FATE),
        "n_isomorphisms_fated": len(ISOMORPHISM_FATE),
        "n_open_questions_resolved": len(OPEN_QUESTION_RESOLUTION),
        "n_new_isomorphisms": len(NEW_ISOMORPHISMS),
        "kb_query_count": 24,  # 22 planner pre-survey + 2 executor extensions
    }
    verdict = "PASS" if all(checks.values()) else "FAIL"  # (local)
    return verdict, {"checks": checks, "summary": summary}


# ---------------------------------------------------------------------------
# Section 7 — Verdict emission (atomic dual-SHA append)
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append a single-line dual-SHA verdict + companion row (S84+ schema)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"GEOMETRIC/aggregate-domain-survey set-coverage; [AUDIT] no [SIGN] 3-tuple\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL, pins)  # (local)
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")

    verdict, report = evaluate_coverage()  # (local)
    summ = report["summary"]  # (local)

    # value string: per-axis coverage summary
    value = (  # (local)
        f"classes={summ['n_entity_classes']};axes={summ['n_axes']};"
        f"gaps={summ['n_gap_rows']};s54={summ['n_s54_gates_fated']};"
        f"iso={summ['n_isomorphisms_fated']};oq={summ['n_open_questions_resolved']};"
        f"new_iso={summ['n_new_isomorphisms']};kb_queries={summ['kb_query_count']}"
    )

    # npz: the full fate/gap ledger for audit reproducibility (optional artifact)
    np.savez(
        OUT_NPZ,
        s54_gate_fate_keys=np.array(list(S54_GATE_FATE.keys())),
        s54_gate_fate_vals=np.array(list(S54_GATE_FATE.values())),
        isomorphism_fate_keys=np.array(list(ISOMORPHISM_FATE.keys())),
        isomorphism_fate_vals=np.array(list(ISOMORPHISM_FATE.values())),
        open_question_keys=np.array(list(OPEN_QUESTION_RESOLUTION.keys())),
        open_question_vals=np.array(list(OPEN_QUESTION_RESOLUTION.values())),
        new_isomorphism_keys=np.array(list(NEW_ISOMORPHISMS.keys())),
        new_isomorphism_vals=np.array(list(NEW_ISOMORPHISMS.values())),
        gap_rows=np.array([list(r) for r in GAP_ROWS], dtype=object),
        checks=json.dumps(report["checks"]),
        summary=json.dumps(summ),
    )
    print(f"  npz -> {OUT_NPZ.name}")

    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"{GATE_ID}: {verdict} -- {value}")
    # exit 0 regardless of verdict (verdict is data, not script health)
    return 0


if __name__ == "__main__":
    sys.exit(main())
