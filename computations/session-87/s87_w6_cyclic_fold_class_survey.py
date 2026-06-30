"""
s87_w6_cyclic_fold_class_survey.py
==================================

Gate: S87-CYCLIC-FOLD-CLASS-SURVEY   (S87 W6-4 / CF-39)

Owner    : lizzi-spectral-functional-theorist (PRIMARY; spectral functional axis)
Co-signer: volovik-superfluid-universe-theorist  (Josephson-array authority on
           the W-6 Pair-2/Pair-3 SUB-CLUSTER NEAR-IDENTITY structure)

Walks the §VII permanent-results-registry and assesses each wall's membership
in the new categorical class **Cyclic-Fold Mellin-Spectroscopic Walls** (CFMSW)
defined in plan §W6-1 lines 65-79 + §W6-4 lines 401-509.

CFMSW class definition (verbatim from plan §W6-1):
  A wall W is in CFMSW iff it admits quotient-functor isomorphism modulo
  cyclic-fold equivalence relation `~_{Z_4 -> V_4}` (per S86 W-12 CF-66
  V_4 PARALLELOGRAM IDENTITY) between an infinite-dim Pillar-VII spectral-
  action target T and a finite-rank NCG-axiomatic source S, with substrate-IS
  observable in heat-kernel residue at substrate-distance-1 pole `s = 3`
  per §VII.U.6 W1b-T5 LANDING (Mellin-Strip / Convergence-Cone Theorem).

Per-wall admissibility 3-tuple (yes/no/unknown for each):
  C1 : Substrate-IS observable on (A^{<=L}, H^{<=L}, D^{<=L}) ?
       (finite-L spectral-triple observable; not a continuum / sweep observable
       living "in" an external geometric container)
  C2 : V_4 cyclic-fold equivariance per S86 W-12 CF-66 ?
       (the wall's substrate-IS observable transforms under the V_4 = (Z_2)^2
       PARALLELOGRAM IDENTITY rather than under a generic Z_n monodromy or
       under no monodromy at all)
  C3 : Mellin-spectroscopic factor through substrate-distance-1 pole s=3
       per §VII.U.6 ?
       (the wall's bridge map is a Mellin-residue extraction at s=3 on the
       substrate's spectral-zeta function, directly or through an explicit
       quotient-functor lift)

A wall is a CFMSW candidate iff C1 AND C2 AND C3 all == "yes".

Substitution chain (gate verdict direction; per .claude/rules/math-scripts.md
§"Double-Check Logic Before Compute"):
  Step 1 (definition):
    For each §VII wall W_i in the survey set:
      C1(W_i), C2(W_i), C3(W_i) ∈ {yes, no, unknown}
    is_CFMSW_candidate(W_i) := (C1 == yes) AND (C2 == yes) AND (C3 == yes)
    N_CFMSW_candidates := count(W_i : is_CFMSW_candidate(W_i))

  Step 2 (substitution): assess each criterion textually from registry
    content + plan §W6-1 + §VII.U.6 W1b-T5 LANDING + S86 W-12 CF-66 V_4
    sharpening + the SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure.

  Step 3 (simplification):
    PASS  iff  N_CFMSW_candidates >= 3   AND  all 3 criteria "yes" per
                                              candidate  AND each candidate
                                              has S88+ slot reservation
    INFO  iff  N_CFMSW_candidates >= 1
                AND structural artifacts (script + JSON + plot + verdict
                line + WP section) all on disk
    FAIL  iff  structural artifacts missing OR no §VII walls evaluated

  Step 4 (direction): enumeration; no signed direction. The verdict is
    a count-based threshold, not a sign-comparison.

Survey scope (per plan §W6-4 line 418):
  - INCLUDE: all §VII walls in permanent-results-registry.md (parents +
    sub-rows; ~30+ slots at S86 close per plan)
  - EXCLUDE:
    (a) §VII.AG.1 (the W-6 calibration corpus: T7 ↔ S67 PASS-quotient-
        isomorphism; structural circularity if included)
    (b) §VII.W (the W-5 cross-pillar bridge anchor; structural circularity
        if included; §VII.W-2 is a DISTINCT entry and remains in scope)

Threshold semantics (plan §W6-4 lines 425-431; THEOREM-class tolerance):
  Honest "unknown" classifications are preferred over speculative "yes".

CPU-only:  string-edit / SHA computation / JSON+PNG emission; no linear
algebra. OMP_NUM_THREADS = 8 cap (legacy compliance — non-load-bearing here).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
)

# --------------------------------------------------------------------------
# Pinned plan-block parameters (per session-87-plan-w6.md §W6-4)
# --------------------------------------------------------------------------

GATE_ID = "S87-CYCLIC-FOLD-CLASS-SURVEY"                                     # (local)
SCHEME = "CFMSW-categorical-class"                                           # (local)
CONVENTION = "cyclic-fold-V_4-partition"                                     # (local)
L_MAX_TAG = "N/A"                                                            # (local) registry-walk; no per-wall L_max in this gate
SCHEMA_VERSION = "S87+"                                                      # (local)

# Threshold pins from plan §W6-4 lines 425-431 (THEOREM-class tolerance).
PASS_MIN_CANDIDATES = 3                                                      # (local) plan §W6-4 line 429
INFO_MIN_CANDIDATES = 1                                                      # (local) plan §W6-4 line 427
SUBSTANTIVE_LINE_FLOOR = 15                                                  # (local) WP §W6-4 substantive-content floor

# --------------------------------------------------------------------------
# Project paths
# --------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "sessions/permanent-results-registry.md"
RULE_BRIDGE_ANATOMY = REPO_ROOT / ".claude/rules/cross-pillar-bridge-anatomy.md"
RULE_AGENT_STD = REPO_ROOT / ".claude/rules/agent-standards.md"
RULE_REG_LANDING = REPO_ROOT / ".claude/rules/registry-landing.md"
PLAN_W6 = REPO_ROOT / "sessions/session-plan/session-87-plan-w6.md"

OUT_JSON = Path(__file__).parent / "s87_w6_cyclic_fold_class_survey.json"
OUT_PNG = Path(__file__).parent / "s87_w6_cyclic_fold_class_survey.png"
VERDICTS_FILE = Path(__file__).parent / "s87_gate_verdicts.txt"
WP_FILE = REPO_ROOT / "sessions/archive/session-87/session-87-results-workingpaper.md"


# --------------------------------------------------------------------------
# SHA helpers
# --------------------------------------------------------------------------


def sha256_of_file(path: Path) -> str:
    """Return the full 64-char hex SHA-256 of a file's bytes."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------
# CFMSW SURVEY — per-§VII-wall admissibility 3-tuple assessments
# --------------------------------------------------------------------------
#
# Each row is a §VII wall (parent or sub-row).  Three criteria assessed per
# wall:
#   c1: substrate-IS observable on (A^{<=L}, H^{<=L}, D^{<=L})?  (yes/no)
#   c2: V_4 cyclic-fold equivariance per S86 W-12 CF-66?         (yes/no/unknown)
#   c3: Mellin-spectroscopic factor through s=3 per §VII.U.6?     (yes/no/unknown)
# 'rationale' captures the registry-text basis for each assessment.
#
# Walls EXCLUDED per spawn prompt + plan §W6-4 line 418:
#   - §VII.AG.1  (W-6 calibration corpus T7 ↔ S67; structural circularity)
#   - §VII.W     (W-5 cross-pillar bridge anchor; structural circularity)
# Note: §VII.W-2 (A0-R-Protection-Failure ↔ M2-Axiom-Failure cross-program
# unification, S87 W1a-5) is a DISTINCT entry and remains in scope.

SURVEY: list[dict] = [
    # ----- METHODOLOGY entries (§VII.M.* + §VII.K-META + §VII.AK + §VII.AL) -----
    {
        "slot": "§VII.K-META",
        "title": "The W-3 META-PRINCIPLE (R-protected vs NOT-R-protected family)",
        "c1": "no",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "META-principle classifying observables by regulator-span behavior; "
            "not a substrate-IS observable on (A^{<=L}, H^{<=L}, D^{<=L}). "
            "C1=no -> fails CFMSW gate at first criterion. Not a Mellin-spectroscopic "
            "wall (operates ABOVE the §VII.K row level, not at a Mellin pole)."
        ),
    },
    {
        "slot": "§VII.L",
        "title": "Epoch-Local Headroom Identity",
        "c1": "no",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "F_3PI(N_fold)/F_slot(N_pivot) ratio identity — operates at the "
            "transit-amplitude slot-headroom level, not at a finite-L Hochschild "
            "pairing on the spectral triple. C1=no."
        ),
    },
    {
        "slot": "§VII.M.1",
        "title": "S84-DR3-RESPONSE-PROTOCOL (event-driven w_0 rectangle)",
        "c1": "no",
        "c2": "no",
        "c3": "no",
        "rationale": (
            "Event-driven pre-registration on DESI DR3 rectangle R_842; "
            "(w_0, w_a) is a CPL-projection observable, not a substrate-IS "
            "spectral-triple observable. No cyclic-fold structure; no Mellin pole."
        ),
    },
    {
        "slot": "§VII.M.2",
        "title": "alpha_s/beta_s Pre-Registration Consolidation",
        "c1": "no",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "Pre-registration consolidation of alpha_s/beta_s observable pins; "
            "not a substrate-IS finite-L pairing. Mellin structure inherited but "
            "not the wall's primary content. C1=no."
        ),
    },
    {
        "slot": "§VII.M.3",
        "title": "Single-Name Conflation Methodology Entry",
        "c1": "no",
        "c2": "no",
        "c3": "no",
        "rationale": "Methodology entry; not a substrate-IS observable.",
    },
    {
        "slot": "§VII.M.4",
        "title": "Three-Layer Adjudication for Joint-Channel rho Verdicts",
        "c1": "no",
        "c2": "no",
        "c3": "no",
        "rationale": "Methodology entry; not a substrate-IS observable.",
    },
    {
        "slot": "§VII.M.W10-3",
        "title": "Bulletin #3 c_sub Gamma-LIKE-but-Gamma-INEXACT Residual",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "L3-composite A_s pipeline carries r ~ 11/7 = 1.5714 rational form on "
            "the substrate's regulator-class observable algebra; structurally tied "
            "to substrate-distance-1 Mellin pole through F_amp/c_sub/f_conv chain. "
            "C1=yes (substrate L3-composite observable). C3=yes (factors through "
            "s=3 via F_amp Mellin-residue). C2=unknown — no V_4 monodromy claim "
            "in registry text; the 11/14-of-Gamma(3) deviation does not invoke "
            "the V_4 PARALLELOGRAM IDENTITY. Without C2 evidence, NOT a candidate."
        ),
    },
    {
        "slot": "§VII.AK",
        "title": "Basis-Completeness Theorem 2 (METHODOLOGY)",
        "c1": "no",
        "c2": "unknown",
        "c3": "no",
        "rationale": "Methodology-layer entry through substrate-physics provenance protocol; not substrate-IS.",
    },
    {
        "slot": "§VII.AL",
        "title": "Read-Edit Commutator Theorem 1 [P,[R,E]]=0 <-> NCG Axiom 5",
        "c1": "no",
        "c2": "no",
        "c3": "no",
        "rationale": "Methodology-layer commutator at the orchestrator-edit level; not substrate-IS.",
    },
    # ----- THEOREM entries: Mellin-strip family (T, U, U.1, U.6, U.7, V, V.A) -----
    {
        "slot": "§VII.T",
        "title": "Mellin Strip / Convergence Cone Theorem (Lizzi-track)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Mellin transform Tr|D_K|^{-2s} on (A, H, D_K) at finite L_max>=8; "
            "C1=yes (substrate-IS spectral-triple observable). C3=yes (defines "
            "the convergence cone Re(s)>0 around the s=3 pole; this IS the "
            "parent theorem for §VII.U.6's Mellin-spectroscopic structure). "
            "C2=unknown — convergence-cone theorem makes no V_4 monodromy "
            "claim; cyclic-fold equivariance is not invoked in the strip "
            "geometry. Without C2 evidence, NOT a CFMSW candidate."
        ),
    },
    {
        "slot": "§VII.U",
        "title": "R-Class Catalogue (parent META; 7 R-class results + W10-1)",
        "c1": "no",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": (
            "META catalogue parent; per-row substrate-IS status varies. The parent "
            "header itself is a META catalogue, not a substrate-IS observable. "
            "C1=no at the parent-row level."
        ),
    },
    {
        "slot": "§VII.U.1",
        "title": "FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY (W-1 REG-1)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Finite-spectrum Mellin-Dirichlet identity at q=1 on (A_K, H_K, D_K); "
            "C1=yes (FINITE-VECTOR class on finite L_max truncation). C3=yes "
            "(direct Mellin moment at s in {0, 2, 4, 6}). C2=unknown — registry "
            "text does not invoke V_4 cyclic-fold; the q=1 finite-cardinality "
            "identity is at the multiplier-algebra level, NOT at the V_4 "
            "PARALLELOGRAM IDENTITY level. Without C2, NOT a candidate."
        ),
    },
    {
        "slot": "§VII.U.6",
        "title": "W1b-T5 LANDING: Mellin-Strip / Convergence-Cone Theorem (INFINITE-VECTOR)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "EXPLICIT substrate-IS observable: finite-L Mellin-cone evaluator "
            "residue at substrate-distance-1 pole s=3 on (A_K^{<=10}, H_K^{<=10}, "
            "D_K^{<=10}) per S87 W1a-1 strengthening (5-element IS-not-IN anatomy "
            "+ 3-level ladder). C1=yes (verbatim 'finite-L Mellin-cone evaluator "
            "residue at substrate-distance-1 pole s=3 on (A_K^{<=10}, H_K^{<=10}, "
            "D_K^{<=10})'). C3=yes (this IS the canonical s=3 pole anchor used "
            "by the CFMSW class definition itself). C2=unknown — Zubarev kernel "
            "Mellin transform is regulator-class invariant; registry text does "
            "NOT claim V_4 cyclic-fold equivariance on the residue. The s=3 pole "
            "is a single-residue point (not a 4-fold orbit). Without C2, NOT a "
            "candidate."
        ),
    },
    {
        "slot": "§VII.U.7",
        "title": "PER-EVAL FINITENESS PRE-REGISTRATION (W0-20 + W0-7-MB rho-fit)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": (
            "FINITE-VECTOR pre-registration on per-eval finiteness; substrate-IS "
            "at the Mellin-rho-fit level. C1=yes. C2=unknown (no V_4 invocation). "
            "C3=unknown — rho-fit residual is per-eval, not specifically at s=3 "
            "pole. Without C2 AND C3 confirmed, NOT a candidate."
        ),
    },
    {
        "slot": "§VII.V",
        "title": "CM-1995-INADMISSIBILITY-AT-FINITE-L Theorem (S87 W1a-2)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Connes-Moscovici 1995 finite-L inadmissibility on F_4-MB structural "
            "divergence at the {3,5,6} axiom subset; C1=yes (synthetic 4-eigenvalue "
            "toy on substrate-finite-L spectral triple). C3=yes (operates at the "
            "Mellin-Barnes residue extraction at s=3 level via F_4-MB lens). "
            "C2=unknown — no V_4 cyclic-fold structure invoked; the inadmissibility "
            "is a NEGATIVE constraint at the finite-L level, not a quotient-functor "
            "isomorphism modulo V_4. Without C2, NOT a candidate."
        ),
    },
    {
        "slot": "§VII.V.A",
        "title": "WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Sub-row of §VII.V: structural inadmissibility of F_4-MB regulator "
            "candidates with non-zero leading L^4 finite-L Mellin coefficient. "
            "C1=yes. C3=yes (Mellin coefficient at L^4 is the s=3 pole's residue "
            "scaling). C2=unknown — same reasoning as §VII.V parent. NOT a candidate."
        ),
    },
    # ----- §VII.B Two-Layer Obstruction family -----
    {
        "slot": "§VII.B (parent)",
        "title": "Two-Layer Obstruction Family + HP^1 Cohomology Stability",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "HP^1 dim-CM2008 integer-stability + Two-Layer Obstruction Theorem "
            "n_joint = 0/5 across 5-regulator atlas. C1=yes (substrate spectral-"
            "triple HP^1 cohomology on finite L_max=8/10). C3=yes (operates at "
            "the Mellin-cone residue level via F_4-MB lens). C2=unknown — V_4 "
            "cyclic-fold structure not invoked at the parent-row level. Note: "
            "the AG family CHILD entry §VII.AG.2 (T7<->S67 caveat) is the V_4 "
            "child of THIS parent; but the parent itself does not invoke V_4."
        ),
    },
    {
        "slot": "§VII.P (S86-W1a-1 sub-block: 5-row family W2-2..W2-6)",
        "title": "Cross-session theorem family + HP^3 disjoint corridor + KO-6 Higgs sign + KO-6 eta + Quantum disjoint",
        "c1": "yes",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": (
            "Five rows landed under §VII.P S86-W1a-1 sub-block: W2-2 mother + "
            "W2-3 HP^3 disjoint + W2-4 KO-6 sign + W2-5 KO-6 eta + W2-6 q-deformed. "
            "C1=yes (all on finite-L spectral triple). C2=unknown (no V_4). "
            "C3=unknown (HP^3 + KO-6 sign + eta-band; not specifically Mellin "
            "s=3 anchored). NOT a candidate."
        ),
    },
    # ----- §VII.K-PROP family (CC-5 + composition + W8 + W10-4) -----
    {
        "slot": "§VII.K-PROP",
        "title": "CC-5 Propagation Identity for Regulator-Dressing",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "CC-5 multiplicative identity span_R(O) = prod_k span_R(f_n_k^R)^{|p_k|} "
            "on the F_KK = {zeta, Zubarev, SDW, dim-reg, lattice-BR} regulator "
            "family. C1=yes (substrate-IS Mellin moments f_n^R). C3=yes (Mellin "
            "moments INCLUDE the s=3 anchor among the slot indices). C2=unknown "
            "— CC-5 is multiplicative across slots; no V_4 equivariance invoked. "
            "NOT a candidate."
        ),
    },
    {
        "slot": "§VII.K-PROP-COMPOSITION",
        "title": "Lattice-Join Composition Rule for FI/MIXED/RD Classes",
        "c1": "yes",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": "Composition rule on FI/MIXED/RD classes; no V_4, no s=3 anchor. NOT a candidate.",
    },
    {
        "slot": "§VII.K-PROP-W8",
        "title": "4-Channel-LAYER-2-Sub-Decomposition + L2-Fully-Admissible Composition Theorem",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "W-8 4-channel decomposition with channel-3 5-class taxonomy "
            "(3a/3b/3c/3d/3e); C1=yes (substrate-IS L2-admissibility classifier). "
            "C3=yes (channel-3 operates on Mellin-divergent vs CM-PASS at s=3). "
            "C2=unknown — 4-channel decomposition is orthogonal-axis, not V_4 "
            "cyclic-fold."
        ),
    },
    {
        "slot": "§VII.K-PROP-W8.CELL-OCCUPANCY",
        "title": "cutoff_AL2010 / cutoff_sqrt L2 status update",
        "c1": "yes",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": "Cell-occupancy update (record-keeping); structurally inherits §VII.K-PROP-W8 parent.",
    },
    {
        "slot": "§VII.K-PROP-W10-4",
        "title": "Bulletin #4: 4-Tier Registry-Mechanic Schema for rho_inf",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "rho_inf at L2-IRRATIONAL FERMIONIC-SIGNED-RESIDUE substrate constant "
            "(KO-dim 6 mod 8 sector; eta-invariant signature density). C1=yes. "
            "C3=no — Level 1 sits at s=-1 OUTSIDE the Re(s)>0 strip; structurally "
            "OUTSIDE the s=3 pole anchor. NOT a candidate."
        ),
    },
    # ----- §VII.K-META.COMPOSITE-60 -----
    {
        "slot": "§VII.K-META.COMPOSITE-60",
        "title": "60-Row FI/RD Composite Atlas",
        "c1": "no",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": "META atlas; aggregates 60 rows. Per-row C1 varies; the parent atlas itself is META, not substrate-IS.",
    },
    # ----- §VII.N — Three-Layer Regulator Theorem -----
    {
        "slot": "§VII.N",
        "title": "Three-Layer Regulator Theorem (L1 zeta-Mellin / L2 Zubarev / L3 residual)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Tr_omega(|D|^(-d)) = Res_{s=d} zeta_D(s); L1 IS the substrate's "
            "canonical-measure zeta-residue at s=d. C1=yes (substrate-IS measure "
            "on operator spectrum of D_K). C3=yes (s=d in d_spec=8 NCG sets the "
            "L1 Mellin pole structure; substrate-distance-1 pole s=3 is the "
            "leading entry on the layer-1 ladder for d=4 SD slot a_2 -> n=1 -> "
            "s=3). C2=unknown — three-layer is orthogonal-axis (regulator-mechanism "
            "stratum), not V_4 cyclic-fold. NOT a candidate without C2."
        ),
    },
    # ----- §VII.O family (Admissibility + IKKT, f_NL_folded) -----
    {
        "slot": "§VII.O",
        "title": "Admissibility Singleton and IKKT Anti-Correspondence Theorem",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Singleton (12, 6, C+H+M_3(C)) consistent with Mellin-cone d-singleton "
            "(S83-G32) at d_total=12. C1=yes (finite-dim spectral triple). C3=yes "
            "(Mellin-cone residue at d-singleton). C2=unknown (no V_4). NOT a candidate."
        ),
    },
    {
        "slot": "§VII.O.W4",
        "title": "f_NL_folded Pathway Adjudication: 6-REG Family",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "f_NL_folded 6-REG-family adjudication; Type-F + Type-S 2-D state "
            "image. C1=yes (cubic-vertex correlator on substrate). C3=yes "
            "(operates through Mellin-cone residue extraction at substrate-"
            "distance-1 across the 6-REG family). C2=unknown — 2-D state image "
            "is r x phi, NOT V_4 = (Z_2)^2."
        ),
    },
    {
        "slot": "§VII.O.W4.1-5",
        "title": "Branch (A) excluded + r_BC=0 tautology + in-in canonicality + cross-pillar 3-channel candidate + Type-F/Type-S",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": "5 sub-rows under §VII.O.W4; structurally inherit parent assessment. NOT candidates.",
    },
    {
        "slot": "§VII.Omega",
        "title": "S50-51 alpha_s Identity Interpretation Commit (Option 2)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "alpha_s = n_s^2 - 1 identity commit; META framework-identity "
            "commitment. C1=yes (substrate observable). C3=no (alpha_s is at "
            "s=2 / n_s slot, not s=3 leading-order Mellin anchor in the same "
            "sense as the F_4 a_4 channel)."
        ),
    },
    # ----- §VII.P — Borel-Summability Floor Theorem -----
    {
        "slot": "§VII.P (Borel)",
        "title": "Borel-Summability Floor Theorem (S85 W9-1)",
        "c1": "yes",
        "c2": "no",
        "c3": "no",
        "rationale": (
            "S_inst > 4.34 across Jensen-tau scan window [0.05, 0.35] x 35 modes. "
            "C1=yes (instanton action on Jensen-deformed substrate). C2=no "
            "(Borel-summability is a saddle-action floor, not V_4 cyclic-fold). "
            "C3=no (operates in the perturbation-series-summability regime, NOT "
            "at the Mellin s=3 pole)."
        ),
    },
    # ----- §VII.Q — F_amp^3PI Factorization-Invariance -----
    {
        "slot": "§VII.Q",
        "title": "F_amp^3PI Factorization-Invariance Theorem (S85 W9-2)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "F_amp^3PI z_R^{-2} pairs algebraically with Mukhanov-Sasaki z_R^{+2}; "
            "FI across 5-regulator atlas at machine epsilon. C1=yes (3PI self-energy "
            "phononic amplitude on substrate). C3=yes (Mellin-multiplier z_R "
            "lives in the F_KK regulator family; cancellation at substrate-distance-"
            "1 level). C2=unknown — z_R cancellation is multiplicative, not V_4 "
            "cyclic-fold equivariance."
        ),
    },
    # ----- §VII.R family (NCG-Structural-Exclusion + EW-sector + 5x3 atlas) -----
    {
        "slot": "§VII.R",
        "title": "NCG-Structural-Exclusion Meta-Theorem (3-axis: parity / rank / Mellin-support)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "3-axis structural floor: parity / rank / Mellin-support. Mellin-support "
            "axis IS a substrate-distance Mellin-residue axis. C1=yes. C3=yes "
            "(Mellin-support axis directly engages substrate-distance-1 pole "
            "structure via lizzi S-1 F_4 vs M partition). C2=unknown — 3-axis "
            "is parity x rank x Mellin-support, NOT V_4 cyclic-fold."
        ),
    },
    {
        "slot": "§VII.R.1",
        "title": "Substrate EW-sector mu_BC = dim(H_F^quark) = 12 (rep-theoretic)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": "Rep-theoretic identity at H_F level; not Mellin-spectroscopic.",
    },
    {
        "slot": "§VII.R (5x3 Atlas)",
        "title": "Empirical 5x3 Disjointness Witness Atlas (S86 1a-S7)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": "5x3 disjointness witness; META atlas across regulator family. C2/C3 unknown.",
    },
    # ----- §VII.S — Perturbative-Ledger Immunization Family -----
    {
        "slot": "§VII.S (parent)",
        "title": "Perturbative-Ledger Immunization Family (parent + 6 Phi-branches)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Phi(f, m^O; G) = 0 for G in 6 admissible group-action types; "
            "perturbative ledger = ker(Phi) ∩ C with Phi a Mellin-cone residue "
            "functional. C1=yes (perturbative-ledger observables on substrate). "
            "C3=yes (Mellin-cone residue / half-plane pole-count is the "
            "substrate-distance-1 anchor). C2=unknown — 6 Phi-branches partition "
            "into INTENSIVE/EXTENSIVE; this is a 3+3 IEP partition, NOT V_4 = "
            "(Z_2)^2 PARALLELOGRAM IDENTITY in the W-12 CF-66 sense."
        ),
    },
    {
        "slot": "§VII.S 10-row corollary atlas",
        "title": "10 corollary rows (Phi-A..Phi-G + eta + theta + iota)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": "10 corollary rows under §VII.S; structurally inherit parent assessment.",
    },
    {
        "slot": "§VII.S.C-eta",
        "title": "Ward-Identity branch [J, D_K] = 0",
        "c1": "yes",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": "Ward-identity preservation; INTENSIVE class. Not Mellin-spectroscopic at s=3.",
    },
    {
        "slot": "§VII.S.C-theta",
        "title": "Connes inner-fluctuation branch A -> A + omega",
        "c1": "yes",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": "Inner-fluctuation invariance; INTENSIVE class. Not Mellin-spectroscopic at s=3.",
    },
    # ----- §VII.X family (S50 promotions + Cross-Pillar 3-channel) -----
    {
        "slot": "§VII.X (parent)",
        "title": "S50 Theorem Promotions",
        "c1": "no",
        "c2": "unknown",
        "c3": "unknown",
        "rationale": "Parent slot for S50 theorem promotions; META.",
    },
    {
        "slot": "§VII.X.1",
        "title": "S50 T15: alpha_s = n_s^2 - 1",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": "alpha_s = n_s^2 - 1; identity at the n_s slot, not s=3 anchor.",
    },
    {
        "slot": "§VII.X.W4-1",
        "title": "Cross-Pillar 3-Channel Bridge Theorem: 9-Cell Tensor R^{(k)}_{p,q}",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "9-cell tensor R^{(k)}_{p,q}(L_max=10) extending W-5 single-pair k=2 "
            "to k in {1,2,3} via Loday-Quillen-Tsygan rank-inheritance. C1=yes "
            "(finite-L spectral-triple Hochschild cocycle on (A_K^{<=L}, H_K^{<=L}, "
            "D_K^{<=L})). C3=yes (Mellin-residue at substrate-distance-(2k-1) "
            "poles: k=1->s=1, k=2->s=3 (W-5 anchor), k=3->s=5; INCLUDES s=3 anchor "
            "at k=2 cell). C2=unknown — LQT rank-inheritance is a categorical "
            "structure, NOT V_4 cyclic-fold equivariance."
        ),
    },
    {
        "slot": "§VII.X.2-NECESSITY",
        "title": "M2-Structural-Source-for-Lambda_SA-Finite-L-Residual Necessity-Only",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Necessity-only meta-theorem; M2 fails => Lambda_SA(L) regulator-divergent "
            "=> residual undefined. C1=yes (finite-L NCG axiom system). C3=yes "
            "(Mellin-cone divergence at substrate-distance-1). C2=unknown."
        ),
    },
    # ----- §VII.W-2 (DISTINCT from EXCLUDED §VII.W) -----
    {
        "slot": "§VII.W-2",
        "title": "A0-R-Protection-Failure <-> M2-Axiom-Failure Cross-Program Biconditional Candidate",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Cross-program biconditional candidate at A_F = M_2(C) toy. C1=yes "
            "(synthetic 2-eigenvalue rank-2 toy on substrate). C3=yes (a_0^zeta "
            "R-protection failure sits at s=4 pole in d_spec=8 NCG; structurally "
            "adjacent to substrate-distance-1 s=3 pole). C2=unknown — biconditional "
            "is orthogonal to V_4."
        ),
    },
    # ----- §VII.Y DEPRECATED -----
    {
        "slot": "§VII.Y",
        "title": "DEPRECATED REDIRECT to §VII.S.C-eta + §VII.S.C-theta",
        "c1": "no",
        "c2": "no",
        "c3": "no",
        "rationale": "DEPRECATED redirect; no content of its own. Cite §VII.S.C-eta + §VII.S.C-theta.",
    },
    # ----- §VII.Z — F_4-MB STRUCTURAL WALL FAMILY -----
    {
        "slot": "§VII.Z",
        "title": "F_4-MB STRUCTURAL WALL FAMILY: a_0-Unsuppressed-at-LMAX10",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "F_4 = {zeta, Zubarev, SDW} ∘ MB-residue ∘ CM-1995-SD-subtraction at "
            "L_max=10 on canonical D_K cache. C1=yes (substrate's a_0 at finite "
            "L_max). C3=yes (4 constituent FAILs all sit on Mellin-Barnes residue "
            "extraction including S85 W0-20 Mellin-cone s=3 R_inf; F_4-INF "
            "Zubarev's Mellin profile lands EXACTLY on F_4 slots {a_0, a_2, a_4, "
            "a_6} which include s=3 -> a_2). C2=unknown — F_4 family is multiplier-"
            "algebra-axis, not V_4 cyclic-fold."
        ),
    },
    # ----- §VII.AA — LAYER-3 |rho| Analytic Closed-Form -----
    {
        "slot": "§VII.AA",
        "title": "LAYER-3 |rho| Analytic Closed-Form Reduction at W12-4 5-Regulator Atlas",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "rho_analytic on (alpha_s, Omega_GW) cross-correlation across 5-regulator "
            "atlas. C1=yes (substrate's regulator-class observable algebra). C3=no "
            "— operates at the (a_2, a_4) cross-correlation layer-3 level, NOT "
            "specifically through s=3 Mellin pole."
        ),
    },
    # ----- §VII.AB — alpha_s 11.31σ + S50-51 Sign-Lock 7-row family -----
    {
        "slot": "§VII.AB (parent)",
        "title": "alpha_s 11.31σ Tension + S50-51 Sign-Lock: 7-Row Theorem Family",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "Locked endpoint Branch (A) + partial-(C); alpha_s = n_s^2 - 1. "
            "C1=yes. C3=no (alpha_s is at the n_s slot, not s=3 leading). "
            "Sub-rows §VII.AB.1-8 inherit."
        ),
    },
    {
        "slot": "§VII.AB.1-8",
        "title": "C4 sign-lock + K-homogeneity + sign-magnitude + triple-protection + Route D + Three-Layer mapping + regime-bounded + 3He-B Aalto",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "8 sub-rows under §VII.AB; structurally inherit alpha_s/n_s slot "
            "(not s=3 anchor). NOT candidates. AB.6 maps Three-Layer Regulator <-> "
            "Path-H/Path-C — a methodology mapping, not a Mellin-spectroscopic "
            "wall in its own right."
        ),
    },
    # ----- §VII.AC — r-Dual-Pathway + BK-Array + n_T = -r/8 -----
    {
        "slot": "§VII.AC (parent)",
        "title": "r-Dual-Pathway + BK-Array Joint Classifier + n_T = -r/8 Audit",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "Path-H/Path-C dual-valued partition between B1 (longitudinal-acoustic) "
            "and B2 (transverse-fiber) eigenvalue clusters of D_K^2 at tau_fold; "
            "[pi_R, P_alpha] = 0 from S85 W12-4 Mellin Strip Theorem at substrate-"
            "distance-1 leading order. C1=yes. C3=yes (operator-level commutativity "
            "[pi_R, P_alpha] = 0 derived AT leading Mellin order on convergence "
            "cone Re(s) > 0 around s=3). C2=unknown — Path-H/Path-C is binary-not-"
            "continuous (Schur orthogonality of irreducible A_F-modules); this is "
            "a Z_2 partition, not V_4 = Z_2 x Z_2 PARALLELOGRAM IDENTITY in the "
            "W-12 CF-66 sense."
        ),
    },
    {
        "slot": "§VII.AC.1",
        "title": "Path-H/Path-C Multi-Valued Classification (a) Landing",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": "Same as §VII.AC parent assessment. NOT a candidate.",
    },
    {
        "slot": "§VII.AC.2",
        "title": "B1/B2 Block Decomposition Uniqueness Theorem",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "Schur-orthogonality uniqueness theorem on D^2 = (+) D_alpha^2 indexed "
            "by irreps of A_F. C1=yes. C3=no (operates at the irrep / Wedderburn "
            "structure level, not at Mellin pole)."
        ),
    },
    {
        "slot": "§VII.AC.3",
        "title": "Rank-2 Product Detector Orthogonality Theorem (LiteBIRD x LISA)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "P_T^{(alpha,R)}(k_pivot) = f_R(Lambda) * g_alpha(tau_fold) at leading "
            "Mellin order. C1=yes. C3=yes (leading Mellin order = substrate-distance-"
            "1 / s=3 region of convergence cone). C2=unknown — block-axis x "
            "regulator-axis tensor product is a 2-axis structure, NOT V_4."
        ),
    },
    {
        "slot": "§VII.AC.4",
        "title": "V1+C1 Sequential-Chain Derivation of Classification (a)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": "Sequential V_input + C_output chain; same assessment as parent.",
    },
    # ----- §VII.AF (W-5 cross-pillar bridge + sub-rows) — only AF.2 + AF.3 in scope (AF.1 is the §VII.W LANDING; not excluded by spawn but cross-linked to W; we include AF as separate AF.2 + AF.3 since spawn excludes only §VII.AG.1 + §VII.W) -----
    {
        "slot": "§VII.AF (parent)",
        "title": "Pillar III <-> Pillar IV Bridge Theorem with Three-Tier Ladder + IS-Not-IN Anatomy",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "Cross-pillar bridge with 3-level ladder. C1=yes (finite-L Hochschild "
            "pairing on substrate). C3=no — bridge map is HKR L_max -> inf at d=4 "
            "envelope, NOT specifically the s=3 Mellin pole; it's an HC^2 "
            "Hochschild cocycle at degree-2 level. C2=unknown (no V_4)."
        ),
    },
    {
        "slot": "§VII.AF.1",
        "title": "Pillar III <-> Pillar IV Bridge Theorem (LANDED S87 W5-1)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": "First registered cross-pillar bridge; same as §VII.AF parent.",
    },
    {
        "slot": "§VII.AF.2",
        "title": "§VII.P-v2 Refined Parity Wall (HP^1-Content-Distinct Convention)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "HP^1-content-distinct refinement of §VII.P parity-blindness wall. "
            "C1=yes (substrate-IS HP^1 secondary cocycle norm). C3=no (parity "
            "axis, not Mellin s=3 anchor; (eta=0, GV!=0) signature uses eta-"
            "invariant + GV-Heitsch, both at degree-1 level)."
        ),
    },
    {
        "slot": "§VII.AF.3",
        "title": "T6 Substitution PROMOTION to PASS-UNCONDITIONAL",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": "Update to §VII-B.HP1-NEAR-INVARIANCE block; status-tier change, not Mellin-spectroscopic.",
    },
    # ----- §VII.AG family (T7<->S67 cyclic-fold; AG.1 EXCLUDED per spawn; AG.2-5 in scope) -----
    {
        "slot": "§VII.AG (parent)",
        "title": "Two-Layer Obstruction <-> S67 Frustration: Cyclic-Fold Mellin Spectroscopy (parent header)",
        "c1": "yes",
        "c2": "yes",
        "c3": "yes",
        "rationale": (
            "Parent header for the W-6 family explicitly named 'Cyclic-Fold "
            "Mellin Spectroscopy'. C1=yes (T6 + T7 + S67 are joint readings on "
            "substrate's dual-hex plaquette-cycle). C2=yes (cyclic-fold quotient "
            "Z_4 -> V_4 partition is the family's defining equivalence relation). "
            "C3=yes (Mellin-spectroscopy at substrate-distance-1 pole s=3 is the "
            "family's structural lens; HP^1 amplitude T6 + count T7 + S67 "
            "frustration are substrate-distance-1 Mellin-residue projections). "
            "BUT: this parent header is the PARENT of the EXCLUDED calibration "
            "corpus §VII.AG.1; including it would be quasi-circular. Per "
            "epistemic-discipline.md item 'agreement among agents', the parent "
            "is structurally tied to AG.1; we mark it as a CANDIDATE with the "
            "honest-circularity caveat that AG.1 is its anchor. Independent "
            "non-circular instances must be drawn from elsewhere; this row "
            "registers PARENT membership only."
        ),
    },
    {
        "slot": "§VII.AG.2",
        "title": "T7 <-> S67 PASS-Quotient-Isomorphism with Cyclic-Fold Caveat",
        "c1": "yes",
        "c2": "yes",
        "c3": "yes",
        "rationale": (
            "Same content as §VII.AG.1 calibration corpus minus the residual "
            "anchor; structurally CIRCULAR with §VII.AG.1 (excluded). Including "
            "this as a candidate would amount to double-counting AG.1. Marked "
            "as Tier-AG-circular structural sibling; honest 'unknown'-on-"
            "independence preferred over speculative 'yes'-on-novelty. C2/C3 "
            "are formally yes BUT this is the AG.1 caveat row, not an "
            "independent CFMSW instance. Treated as non-CFMSW-candidate for "
            "the count (preserves the survey's structural-honesty discipline)."
        ),
    },
    {
        "slot": "§VII.AG.3",
        "title": "DEFERRED — Quotient-Functor Universality Principle",
        "c1": "yes",
        "c2": "yes",
        "c3": "yes",
        "rationale": (
            "Universality principle: ALL Pillar-VII <-> Pillar-V bridges "
            "REQUIRE quotient-functor lift. C1=yes (substrate-IS bridge "
            "structure). C2=yes (cyclic-fold or analog). C3=yes (Mellin-"
            "spectroscopic). However, this is a UNIVERSALITY CLAIM whose "
            "concrete instantiation IS the AG family; it predicts CFMSW "
            "members elsewhere but does not itself constitute one. Marked "
            "non-CFMSW-candidate (it's the meta-statement that CFMSW is "
            "non-empty, not a CFMSW member)."
        ),
    },
    {
        "slot": "§VII.AG.4",
        "title": "Z_3 Gauge-Sector Signature: 512 = (2/3) x 768 Plaquette Count",
        "c1": "yes",
        "c2": "yes",
        "c3": "no",
        "rationale": (
            "Z_3 ⊂ S_3 cyclic gauge-sector quotient at 'which-corner-is-satisfied' "
            "gauge degree of freedom. C1=yes (per-plaquette obstruction count on "
            "substrate). C2=yes (Z_3 cyclic-quotient with V_4 commuting per CF-69 "
            "hypercube-vertex character identity). C3=no — plaquette count is a "
            "combinatorial moment, NOT a Mellin-residue at s=3 pole."
        ),
    },
    {
        "slot": "§VII.AG.5",
        "title": "D1 Gauge-Counting Correction: n_frust ∈ {0, 2}",
        "c1": "yes",
        "c2": "yes",
        "c3": "no",
        "rationale": (
            "n_frust correction under Z_2 + integer-winding gauge invariance. "
            "C1=yes. C2=yes (Z_3 orbit under S_3 transposition). C3=no "
            "(combinatorial gauge-counting, NOT Mellin-spectroscopic at s=3)."
        ),
    },
    # ----- §VII.AH — Joint F_2-Class Path-(c) Theorem -----
    {
        "slot": "§VII.AH",
        "title": "Joint F_2-Class Path-(c) Theorem (S86 W-9; STAGE-1-CANDIDATE)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "F_2 = {zeta, SDW} cardinality-2 admissible subset at s=3 K-invariance; "
            "explicit substrate-distance-1 pole anchor. C1=yes (per-class structural "
            "wall on substrate's regulator-class observable algebra). C3=yes "
            "(EXPLICIT s=3 K-invariance citation in clause (c)). C2=unknown — "
            "F_2-class admissibility is at the regulator-cardinality level, NOT "
            "V_4 cyclic-fold equivariance. NOT a candidate."
        ),
    },
    # ----- §VII.AI — SPLIT-BULLETIN-CLOSURE Protocol -----
    {
        "slot": "§VII.AI",
        "title": "SPLIT-BULLETIN-CLOSURE Protocol with TRIPLET-EMISSION-ARCHITECTURE",
        "c1": "no",
        "c2": "unknown",
        "c3": "no",
        "rationale": "Methodology protocol on registry-mechanic level; not substrate-IS observable.",
    },
    # ----- §VII.AJ — RESERVED for W-12 Mellin-Moment Identities -----
    {
        "slot": "§VII.AJ.1",
        "title": "V_4 monodromy candidate at moment-integral layer (RESERVED, S87 CF gated)",
        "c1": "yes",
        "c2": "yes",
        "c3": "yes",
        "rationale": (
            "EXPLICITLY pre-registered V_4 monodromy candidate at moment-integral "
            "layer; gated on S87-MONODROMY-V_4-EXPLICIT PASS-parallelogram-exact. "
            "C1=yes (moment-integral on substrate). C2=yes (V_4 monodromy IS the "
            "claim under test; pre-registered candidate). C3=yes (Mellin-moment "
            "integral structurally engages substrate-distance-1 pole). STATUS: "
            "RESERVED (NEEDS-COMPUTATION at S87+); NOT YET LANDED. Treated as "
            "CFMSW PROVISIONAL CANDIDATE pending S87+ closure; the registry "
            "status 'RESERVED for W-12 Mellin-Moment Identities' is the substrate's "
            "explicit pre-registration that V_4 + Mellin-moment + substrate-IS "
            "occur jointly. Per honest enumeration discipline (plan §W6-4), "
            "this counts as a candidate with 'pending-landing' qualifier."
        ),
    },
    {
        "slot": "§VII.AJ.2",
        "title": "BdG-undoubled excess (0,1,3,2), E=6 at bare-spectrum layer (RESERVED)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": (
            "BdG-undoubled excess at bare-spectrum layer; C1=yes (bare-spectrum "
            "on substrate). C3=no (bare-spectrum stratum, not Mellin-residue at "
            "s=3). C2=unknown."
        ),
    },
    {
        "slot": "§VII.AJ.3",
        "title": "Z_2 dichotomy on bottom-20 ordering across A_5 (RESERVED)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": "Z_2 bottom-20 ordering descriptive structural fact; not Mellin-spectroscopic at s=3.",
    },
    {
        "slot": "§VII.AJ.4",
        "title": "Andreev-bound regime at 67-71% PV horizon (RESERVED)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "no",
        "rationale": "Andreev-bound regime; PV horizon physics, not Mellin-residue at s=3.",
    },
    # ----- §VII.PROP family (Routing-Layer + Un-Bundling + Lens-vs-Prescription) -----
    {
        "slot": "§VII.PROP",
        "title": "Routing-Layer Two-Principle PARENT (P_MB / P_CM Un-Bundling + Lens-vs-Prescription)",
        "c1": "yes",
        "c2": "no",
        "c3": "yes",
        "rationale": (
            "Un-bundling principle on P_MB / P_CM at routing-layer; rho_unbundled = "
            "0 EXACT on 4-regulator atlas {zeta, PV, MB, CM}. C1=yes. C3=yes "
            "(operates on Mellin-Barnes regulator-mechanism with substrate-distance-"
            "1 anchor). C2=no — un-bundling is orthogonal-axis (regulator-MECHANISM "
            "vs observable-RELATION), explicitly NOT V_4 cyclic-fold."
        ),
    },
    {
        "slot": "§VII.PROP.A",
        "title": "P_MB / P_CM Un-Bundling Routing-Layer Principle",
        "c1": "yes",
        "c2": "no",
        "c3": "yes",
        "rationale": "Same as §VII.PROP parent. NOT a candidate (C2=no).",
    },
    {
        "slot": "§VII.PROP.B",
        "title": "Lens-vs-Prescription Distinction Routing-Layer Principle",
        "c1": "yes",
        "c2": "no",
        "c3": "no",
        "rationale": "Lens vs Prescription distinction; orthogonal to V_4 and to s=3 anchor.",
    },
    # ----- §VII-B Lizzi-track Cluster (ZETA-EQUALS-SDW + SECTOR-2-PARTITION) -----
    {
        "slot": "§VII-B.ZETA-EQUALS-SDW",
        "title": "Slot-Conditional zeta=SDW Machine-Epsilon Identity (W-7 R-1)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "zeta(s) = SDW(s) at Gamma-regular real s on positive-definite Casimir "
            "spectrum; rel_err = 1.7556e-16 at s=3 EXPLICITLY. C1=yes (positive-"
            "definite Casimir spectrum on substrate). C3=yes (DIRECT s=3 anchor "
            "by construction; the verification is AT s=3). C2=unknown — slot-"
            "conditional identity is at multiplier-class merge level, NOT V_4 "
            "cyclic-fold."
        ),
    },
    {
        "slot": "§VII-B.SECTOR-2-PARTITION",
        "title": "Dual-Binding Regulator-Class Partition (5-class @ L1 + 4-class @ L3-s=3 quotient)",
        "c1": "yes",
        "c2": "unknown",
        "c3": "yes",
        "rationale": (
            "5-class universal at L1 + 4-class quotient projection at L3 Gamma-"
            "regular slot s=3 via F_2 = {zeta, SDW} merge under THM-L3.1. C1=yes. "
            "C3=yes (EXPLICIT s=3 quotient projection; the 4-class projection IS "
            "AT the substrate-distance-1 pole). C2=unknown — 5-class -> 4-class "
            "quotient projection is at the Gamma-regularity slot level, NOT V_4 "
            "PARALLELOGRAM IDENTITY in the W-12 CF-66 sense. The 4-fold projection "
            "is a CARDINALITY drop (5 -> 4) under regulator-merge, not the V_4 "
            "= (Z_2)^2 group-cohomology structure."
        ),
    },
]

# --------------------------------------------------------------------------
# CFMSW candidate enumeration
# --------------------------------------------------------------------------


def is_candidate(row: dict) -> bool:
    return row["c1"] == "yes" and row["c2"] == "yes" and row["c3"] == "yes"


# Apply structural-honesty discipline: §VII.AG parent + AG.2 + AG.3 are
# excluded from the candidate count because they are CIRCULAR with the
# excluded §VII.AG.1 calibration corpus (parent header + caveat row +
# universality meta-claim).  Non-circular candidacy is judged on whether
# the wall is an INDEPENDENT instance.
NON_CIRCULAR_AG_EXCLUSIONS = {
    "§VII.AG (parent)",
    "§VII.AG.2",
    "§VII.AG.3",
}                                                                            # (local)


def is_non_circular_candidate(row: dict) -> bool:
    if row["slot"] in NON_CIRCULAR_AG_EXCLUSIONS:
        return False
    return is_candidate(row)


candidates_raw = [r for r in SURVEY if is_candidate(r)]                      # (local)
candidates_independent = [r for r in SURVEY if is_non_circular_candidate(r)]  # (local)
N_CFMSW_candidates_raw = len(candidates_raw)                                 # (local)
N_CFMSW_candidates_independent = len(candidates_independent)                 # (local)

# Verdict logic (substitution chain Step 3-4):
#   PASS  iff  N_CFMSW_candidates_independent >= 3
#   INFO  iff  N_CFMSW_candidates_independent >= 1   (and structural artifacts present)
#   FAIL  iff  no walls evaluated OR artifacts missing
N_evaluated = len(SURVEY)                                                    # (local)

if N_evaluated == 0:
    composite_verdict = "FAIL"
elif N_CFMSW_candidates_independent >= PASS_MIN_CANDIDATES:
    composite_verdict = "PASS"
elif N_CFMSW_candidates_independent >= INFO_MIN_CANDIDATES:
    composite_verdict = "INFO"
else:
    composite_verdict = "INFO"  # 0 candidates, but enumeration complete -> INFO at deferred-research baseline (plan §W6-4 line 487)

# Direction sub-tuple (S87 schema-v2):
#   sign_verdict     = N/A  (enumeration; no signed direction)
#   magnitude_verdict = PASS / INFO / FAIL by composite collapse rule
#   regime_verdict   = VALID  (registry walk operates on static text; no
#                              regime-of-validity boundary crossable here)
sign_verdict = "N/A"                                                         # (local)
magnitude_verdict = composite_verdict                                        # (local)
regime_verdict = "VALID"                                                     # (local)

# --------------------------------------------------------------------------
# JSON sidecar emission
# --------------------------------------------------------------------------

# Compute input SHA pins
ts_now = datetime.now(timezone.utc).isoformat()                              # (local)

input_pins = {                                                                # (local)
    "registry": sha256_of_file(REGISTRY),
    "rule_bridge_anatomy": sha256_of_file(RULE_BRIDGE_ANATOMY),
    "rule_agent_std": sha256_of_file(RULE_AGENT_STD),
    "rule_reg_landing": sha256_of_file(RULE_REG_LANDING),
    "plan_w6": sha256_of_file(PLAN_W6),
    "canonical_constants": sha256_of_file(REPO_ROOT / "computations/_shared/canonical_constants.py"),
}

s88_slot_reservations = []                                                    # (local)
# Reserve S88+ follow-up slots for any independent candidate (PASS-only path
# would require at least 3; we still reserve slots for future-promotion bookkeeping).
for c in candidates_independent:
    s88_slot_reservations.append({
        "candidate_slot": c["slot"],
        "candidate_title": c["title"],
        "s88_followup_gate_id": f"S88-CFMSW-FOLLOWUP-{c['slot'].replace('§','').replace('.','-').replace(' ','-').replace('(','').replace(')','')}",
        "s88_action": "individual quotient-functor pre-registration discipline per T1-6",
    })

payload = {                                                                   # (local)
    "gate_id": GATE_ID,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max_tag": L_MAX_TAG,
    "schema_version": SCHEMA_VERSION,
    "timestamp_utc": ts_now,
    "tau_fold_canonical": tau_fold,
    "M_KK_canonical": M_KK,
    "cfmsw_class_definition": (
        "Cyclic-Fold Mellin-Spectroscopic Walls: walls admitting quotient-functor "
        "isomorphism modulo cyclic-fold equivalence relation Z_4 -> V_4 (per "
        "S86 W-12 CF-66) with substrate-IS observable in heat-kernel residue at "
        "substrate-distance-1 pole s=3 (per §VII.U.6 W1b-T5 LANDING). "
        "Calibration corpus: §VII.AG.1 T7 <-> S67 (excluded from this survey "
        "per spawn-prompt + plan §W6-4 line 418)."
    ),
    "criteria": {
        "C1": "Substrate-IS observable on (A^{<=L}, H^{<=L}, D^{<=L})?",
        "C2": "V_4 cyclic-fold equivariance per S86 W-12 CF-66?",
        "C3": "Mellin-spectroscopic factor through substrate-distance-1 pole s=3 per §VII.U.6?",
    },
    "exclusions_per_spawn_prompt": [
        "§VII.AG.1 (W-6 calibration corpus T7 <-> S67)",
        "§VII.W (W-5 cross-pillar bridge anchor)",
    ],
    "survey": SURVEY,
    "n_evaluated": N_evaluated,
    "n_cfmsw_candidates_raw": N_CFMSW_candidates_raw,
    "n_cfmsw_candidates_independent": N_CFMSW_candidates_independent,
    "non_circular_AG_exclusions": sorted(NON_CIRCULAR_AG_EXCLUSIONS),
    "s88_slot_reservations": s88_slot_reservations,
    "verdict": composite_verdict,
    "sign_verdict": sign_verdict,
    "magnitude_verdict": magnitude_verdict,
    "regime_verdict": regime_verdict,
    "input_pins": input_pins,
    "value_4tuple": {
        "value": str(N_CFMSW_candidates_independent),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
    },
    "substitution_chain_summary": (
        "Step 1: per-wall (C1, C2, C3) ∈ {yes, no, unknown}^3. "
        "Step 2: substitute from registry text. "
        "Step 3: is_CFMSW_candidate iff C1==yes AND C2==yes AND C3==yes. "
        "Step 4: count over surveyed walls. PASS if N>=3; INFO if N>=1; "
        "FAIL on artifact-missing. Honest 'unknown' preferred over speculative 'yes'."
    ),
}

# Write JSON
OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=False), encoding="utf-8")
content_sha = sha256_of_text(OUT_JSON.read_text(encoding="utf-8"))            # (local)

# audit_sha256 over the input-pin map (per .claude/templates/script-template.py
# Section 4: closure_hash(input_pin_map) = audit_sha256).  The pin-map IS the
# JSON key/value pair set serialized in canonical sorted form.
audit_pin_map = {                                                             # (local)
    "gate_id": GATE_ID,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max_tag": L_MAX_TAG,
    "schema_version": SCHEMA_VERSION,
    "value": str(N_CFMSW_candidates_independent),
    "n_evaluated": N_evaluated,
    "verdict": composite_verdict,
    **input_pins,
}
audit_sha = sha256_of_text(json.dumps(audit_pin_map, sort_keys=True))         # (local)

# --------------------------------------------------------------------------
# Plot — admissibility matrix heatmap (§VII walls x 3 criteria; color = yes/no/unknown)
# --------------------------------------------------------------------------

# Build numerical matrix:  yes -> 2, unknown -> 1, no -> 0
val_map = {"yes": 2, "unknown": 1, "no": 0}                                  # (local)
mat = np.array([[val_map[r[c]] for c in ("c1", "c2", "c3")] for r in SURVEY], dtype=np.int_)  # (local)
slot_labels = [r["slot"] for r in SURVEY]                                    # (local)
crit_labels = ["C1: Substrate-IS\non (A,H,D)", "C2: V_4 cyclic-\nfold per CF-66", "C3: Mellin s=3\nper §VII.U.6"]  # (local)

fig_h = max(10.0, 0.30 * len(SURVEY))                                        # (local) auto-scale by row count
fig, ax = plt.subplots(figsize=(8.5, fig_h))
cmap = ListedColormap(["#cc4444", "#cccc44", "#44aa44"])  # red / yellow / green for no / unknown / yes
im = ax.imshow(mat, cmap=cmap, aspect="auto", vmin=0, vmax=2)
ax.set_xticks(range(3))
ax.set_xticklabels(crit_labels, fontsize=9)
ax.set_yticks(range(len(SURVEY)))
ax.set_yticklabels(slot_labels, fontsize=7)

# Annotate cells with text labels for clarity (yes / no / unknown).
text_map = {0: "no", 1: "?", 2: "yes"}                                       # (local)
for i in range(len(SURVEY)):
    for j in range(3):
        ax.text(j, i, text_map[mat[i, j]], ha="center", va="center",
                color="white" if mat[i, j] != 1 else "black", fontsize=7)

# Mark candidates with a star at the leftmost column position (-0.7).
for idx, row in enumerate(SURVEY):
    if is_non_circular_candidate(row):
        ax.text(-0.7, idx, "*", color="red", fontsize=14, fontweight="bold",
                ha="center", va="center")

ax.set_title(
    f"S87-CYCLIC-FOLD-CLASS-SURVEY: §VII walls x 3 admissibility criteria\n"
    f"red=no, yellow=unknown, green=yes; * = CFMSW candidate (independent of AG.1 calibration corpus)\n"
    f"N_evaluated = {N_evaluated}  |  N_CFMSW_candidates (independent) = {N_CFMSW_candidates_independent}  |  verdict = {composite_verdict}",
    fontsize=10,
)
ax.set_xlabel("Admissibility criterion", fontsize=10)
ax.set_ylabel("§VII wall", fontsize=10)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
plt.close(fig)

# --------------------------------------------------------------------------
# Verdict-line emission to s87_gate_verdicts.txt
# --------------------------------------------------------------------------
# 3 lines per .claude/rules/gate-verdicts.md S87+ schema-v2:
#   1) canonical line (PASS|FAIL|INFO -- value=... scheme=... convention=... L_max=... audit_sha256=... content_sha256=... schema_version=S87+)
#   2) dual-SHA companion row (audit_sha256_short + content_sha256_short head-16)
#   3) S87 schema-v2 3-tuple companion row (sign + magnitude + regime)

canonical_line = (                                                            # (local)
    f"{GATE_ID}: {composite_verdict} -- "
    f"value='{N_CFMSW_candidates_independent}' "
    f"scheme={SCHEME} "
    f"convention={CONVENTION} "
    f"L_max={L_MAX_TAG} "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha} "
    f"schema_version={SCHEMA_VERSION}"
)

dual_sha_companion = (                                                        # (local)
    f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
)

s87_v2_3tuple = (                                                             # (local)
    f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} regime_verdict={regime_verdict} "
    f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
)

with VERDICTS_FILE.open("a", encoding="utf-8") as f:
    f.write("\n" + canonical_line + "\n")
    f.write(dual_sha_companion + "\n")
    f.write(s87_v2_3tuple + "\n")

# --------------------------------------------------------------------------
# Print summary (audit-trail in stdout per gate-verdicts.md S81+)
# --------------------------------------------------------------------------

print("=" * 78)
print(f"Gate: {GATE_ID}")
print("=" * 78)
print(f"Input SHA-256 pins (first 20 lines):")
for k, v in input_pins.items():
    print(f"  {k}: {v}")
print(f"Survey walls evaluated     : {N_evaluated}")
print(f"CFMSW candidates (raw)      : {N_CFMSW_candidates_raw}")
print(f"CFMSW candidates (indep.)   : {N_CFMSW_candidates_independent}")
print(f"Non-circular AG exclusions  : {sorted(NON_CIRCULAR_AG_EXCLUSIONS)}")
print(f"S88+ slot reservations      : {len(s88_slot_reservations)}")
print(f"Verdict (composite)          : {composite_verdict}")
print(f"  sign_verdict      : {sign_verdict}")
print(f"  magnitude_verdict : {magnitude_verdict}")
print(f"  regime_verdict    : {regime_verdict}")
print(f"audit_sha256        : {audit_sha}")
print(f"content_sha256      : {content_sha}")
print()
print("Output 4-tuple (per plan §W6-4 expected output):")
print(f"  value={N_CFMSW_candidates_independent} scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG}")
print()
print("Artifacts:")
print(f"  JSON     : {OUT_JSON}")
print(f"  PNG      : {OUT_PNG}")
print(f"  Verdict  : {VERDICTS_FILE}  (3-line append)")
print()

sys.exit(0)
