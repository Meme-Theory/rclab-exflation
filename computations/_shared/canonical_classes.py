#!/usr/bin/env python3
"""
Canonical Classes Module — Constant Groupings for Cross-Cutting Topics
=======================================================================

Created: Session 86 (2026-04-26)
Purpose: Sister module to ``canonical_constants.py``. Defines named groupings
("classes") of constants that share a topical or structural relationship —
e.g. the CC family, the KK scale tower, the alpha_s hierarchy, the fold
transit complex, the Higgs/EW cluster.

Why this exists
---------------
``canonical_constants.py`` is a flat namespace: every constant is a peer.
But the framework constantly references *groups* — "the alpha_s hierarchy",
"all KK variables", "the CC budget". Those groups have no first-class
representation. Topic pages (``summary/topics/``), the visualizer's
Connections view, and the knowledge MCP all need to query constants
*by group*, not just *by name*.

Schema
------
Each class is a dict with these fields:

    id              : short identifier, snake_case (e.g. "CC", "alpha_s")
    name            : human-readable display name
    tier            : nest depth — 0 = root class, 1 = direct sub, 2 = sub-sub, ...
    parent_id       : id of the parent class, or None for root
    description     : 1-3 sentence description of the grouping
    seed_session    : session where this grouping was first formalized (e.g. "S86")

Class membership lives in a separate, edge-shaped structure compatible
with the visualizer's REAL_EDGES schema (so the console can merge them
without special-casing). Each entry in CLASS_EDGES:

    type            : "contains" | "tested_by" | "proven_by" | "developed_in"
                      | "parent_of" | "sibling_of"
    srcType         : "classes" (when class is the source)
    src             : class id
    tgtType         : "constants" | "gates" | "theorems" | "sessions" | "classes"
    tgt             : target id
    role            : 7-axis taxonomy on contains-edges (None for non-contains):
                      INPUTS axis:
                        PRIMARY        — a defining constant of the class
                        PRECONDITION   — a substrate/context property the class
                                         consumes but does not produce
                      OUTPUTS axis (process / emergence):
                        EMERGENT_FROM     — emerges from PRIMARY members via
                                            substrate-level computation (regulators,
                                            schemes, multi-route consistency); not
                                            an algebraic one-liner
                        CONSEQUENCE       — produced by the class's process and
                                            becomes a downstream-class PRIMARY
                        OBSERVABLE_OUTPUT — an external-cosmology observable that
                                            is the class's headline testable
                                            prediction
                      ALGEBRAIC axis:
                        DERIVED        — algebraic / definitional consequence
                                         (unit conversion, ratio of PRIMARY members)
                      CROSS-CUTTING axis:
                        RELATED        — relevant to the class but not native
                                         (kindred observable from a sister class)
    comment         : one-line provenance / context

Consumers
---------
1. The knowledge MCP (``tools/mcp-servers/knowledge``) exposes
   ``list_classes``, ``query_class``, ``get_constant_classes``.
2. The visualizer (``tools/viz/console/build_data.py``) emits
   ``D.CLASSES`` and merges CLASS_EDGES into REAL_EDGES.
3. The topic-page builder (``tools/build_topic_pages.py``) walks each
   class to produce ``summary/topics/<class_id>.md``.

Usage
-----
    from canonical_classes import CLASSES, CLASS_EDGES
    from canonical_classes import get_class, get_class_members, get_classes_for_constant

    cc = get_class("CC")                       # class metadata
    members = get_class_members("CC")          # list of (constant_id, role)
    classes = get_classes_for_constant("CC_ratio")   # ["CC", ...]

Self-validation
---------------
Run ``python canonical_classes.py`` to verify every referenced constant ID
resolves to a real attribute in ``canonical_constants.py``. Missing IDs
exit 1; this catches typos before extract_entities.py / the MCP / the
visualizer ever see the dangling reference.
"""

import sys

# Required by computations/_shared/CLAUDE.md (canonical-constants import rule).
# Sister module: pulls every canonical constant name into this namespace so
# the self-validation block in __main__ can verify class-edge constant
# references via a direct ``name in globals()`` check.
from canonical_constants import *  # noqa: F401, F403

# ==============================================================================
#  SECTION A: Class Definitions
# ==============================================================================
#
# Each class is a top-level dict named ``<ID>_CLASS``. The aggregate
# CLASSES registry (Section C) is built mechanically from these.

# ------------------------------------------------------------------------------
# CC — Cosmological Constant Family
# ------------------------------------------------------------------------------
# The classic 120-orders-of-magnitude problem and the framework's response.
# The CC ratio (spectral / observed) is the headline number; everything else
# is either a derivation, a Planck-2018 anchor, or an effacement coefficient.
CC_CLASS = {
    "id": "CC",
    "name": "Cosmological constant family",
    "tier": 0,
    "parent_id": None,
    "description": (
        "The cosmological-constant problem: the spectral-action zeroth "
        "moment a_0 evaluated against the observed dark-energy density "
        "rho_Lambda. The ratio is ~10^120 in the canonical sign convention. "
        "Class members include the ratio itself, the Planck-2018 anchor, "
        "the dimensionless Lambda/M_Pl^4 form, the spectral-density "
        "estimate, and the effacement-residual coefficient."
    ),
    "seed_session": "S44",
}

# ------------------------------------------------------------------------------
# KK — Kaluza-Klein Scale Tower
# ------------------------------------------------------------------------------
# Two extraction routes (gravity vs Kerner) bracket M_KK at 0.83 decades
# tension. CONST-FREEZE-42 closed the bracket; the alias M_KK = M_KK_gravity
# is the conservative default. OOM_diff_MKK records the inter-route gap.
KK_CLASS = {
    "id": "KK",
    "name": "Kaluza-Klein scale tower",
    "tier": 0,
    "parent_id": None,
    "description": (
        "The internal-geometry mass scale M_KK extracted from the Dirac "
        "spectrum of the Jensen-deformed SU(3) fiber. Two routes — "
        "spectral zeta against Newton's constant (gravity route, ~7.4e16 GeV) "
        "and the Kerner gauge-metric route (~5.0e17 GeV) — bracket the "
        "value at 0.83 decades. CONST-FREEZE-42 (S42) pinned the "
        "convention; the gravity route is the canonical alias."
    ),
    "seed_session": "S42",
}

# ------------------------------------------------------------------------------
# alpha_s — Strong-coupling family (PARENT — disambiguation root)
# ------------------------------------------------------------------------------
# CRITICAL: "alpha_s" historically conflated TWO different observables:
#   (1) QCD strong coupling alpha_s(mu) at energy scale mu — POSITIVE, ~0.118
#       at M_Z. This is the running gauge coupling.
#   (2) Inflationary alpha_s = d(n_s)/d(ln k) — running of the scalar
#       spectral index. SMALL, NEGATIVE in Planck-2018, ~-0.005.
# These are DIFFERENT physics with DIFFERENT signs and DIFFERENT scales.
# The disambiguation gate is S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-
# DISAMBIGUATION-PATCH (canonical_constants.py line 1229+). The class
# system honors this by making alpha_s a PARENT with two children.
ALPHA_S_CLASS = {
    "id": "alpha_s",
    "name": "alpha_s — running-coupling hierarchy (parent)",
    "tier": 0,
    "parent_id": None,
    "description": (
        "Container class for the two physically distinct alpha_s "
        "observables: QCD strong coupling (running gauge coupling) and "
        "inflationary alpha_s (running of scalar spectral index). "
        "These are NOT the same physics — see children alpha_s_QCD and "
        "alpha_s_inflation. The parent exists to anchor the "
        "disambiguation per canonical_constants.py line 1229+."
    ),
    "seed_session": "S86",  # this disambiguating taxonomy is new
}

# ------------------------------------------------------------------------------
# alpha_s_QCD — QCD strong coupling tower (CHILD of alpha_s, tier 1)
# ------------------------------------------------------------------------------
ALPHA_S_QCD_CLASS = {
    "id": "alpha_s_QCD",
    "name": "alpha_s — QCD strong coupling",
    "tier": 1,
    "parent_id": "alpha_s",
    "description": (
        "QCD running gauge coupling alpha_s(mu) at energy scale mu. "
        "The PDG-anchored value at M_Z is alpha_s(M_Z) = 0.1180. "
        "This is the gauge-theory observable, NOT the inflationary "
        "running of n_s. Tower extends to scales m_tau, m_b, M_Z, "
        "and (framework-side) M_KK via two-loop running."
    ),
    "seed_session": "S85",
}

# ------------------------------------------------------------------------------
# alpha_s_inflation — Inflationary spectral-index running (CHILD, tier 1)
# ------------------------------------------------------------------------------
ALPHA_S_INFLATION_CLASS = {
    "id": "alpha_s_inflation",
    "name": "alpha_s — inflationary running of n_s",
    "tier": 1,
    "parent_id": "alpha_s",
    "description": (
        "Inflationary alpha_s = d(n_s)/d(ln k), the running of the "
        "scalar spectral index. Planck-2018 reports -0.0045 ± 0.0067; "
        "ACT DR4 + Planck combined (Aiola+ 2020) reports +0.0023 ± "
        "0.0063 (post-2018 canonical pin per S86 W13 P12). The "
        "framework prediction is alpha_s_inflation = n_s^2 - 1 (S50 "
        "constant-mass identity). NOT the QCD coupling."
    ),
    "seed_session": "S50",
}

# ------------------------------------------------------------------------------
# fold — Jensen-deformation transit complex
# ------------------------------------------------------------------------------
# The framework's "Big Bang substitute": a first-order phase transition
# at tau = 0.19 through the van Hove fold. dS/dtau = +58,673; the spectral
# action gradient drives supersonic transit (Mach 13.75). Everything from
# the substrate cosmogenesis story lives here.
FOLD_CLASS = {
    "id": "fold",
    "name": "Jensen-deformation transit complex",
    "tier": 0,
    "parent_id": None,
    "description": (
        "Constants describing the fold transit at tau_fold = 0.19 — "
        "the framework's first-order phase transition that replaces "
        "the Big Bang singularity. Includes the spectral action S_fold "
        "and its first/second derivatives, transit timescale, terminal "
        "velocity, and Kibble-Zurek excitation parameters. The "
        "substrate sound speed c_fabric (NOT a propagation cutoff) "
        "sets the Mach number for the supersonic phase."
    ),
    "seed_session": "S38",
}

# ------------------------------------------------------------------------------
# Higgs — Higgs / EW cluster
# ------------------------------------------------------------------------------
# m_H = 131.8 GeV framework prediction (KK threshold, |S|^2 mode);
# m_H_obs = 125.1 GeV observed. v_ew = 246 GeV anchors EW symmetry breaking.
# Top and bottom Yukawas are RELATED (they enter the running but are not
# Higgs-defining).
HIGGS_CLASS = {
    "id": "Higgs",
    "name": "Higgs and EW cluster",
    "tier": 0,
    "parent_id": None,
    "description": (
        "Constants of the Higgs sector: observed Higgs mass, EW VEV, "
        "and the third-generation Yukawa pole masses (top, bottom) "
        "that dominate Higgs-sector running. Framework prediction "
        "m_H = 131.8 GeV (KK threshold corrections to the |S|^2 mode "
        "of the fiber embedding). v_ew = 246 GeV is the EW symmetry-"
        "breaking scale."
    ),
    "seed_session": "S60",
}

# ------------------------------------------------------------------------------
# GR — Emergent General Relativity (a_2 channel)
# ------------------------------------------------------------------------------
# GR is NOT fundamental in this framework: the Einstein-Hilbert action arises
# as the second Seeley-DeWitt coefficient a_2 of the spectral action on the
# Jensen-deformed SU(3) Dirac operator D_K. Newton's constant and the Planck
# mass are EMERGENT_FROM the spectral machinery via the Sakharov dictionary
# (S44 SAKHAROV-GN-44 PASS); the cosmological-standard-model anchors (Omega_m,
# H_0, T_CMB, ...) are RELATED — boundary conditions of the emergent theory,
# not native to the emergence. This is the FIRST class to use the EMERGENT_FROM
# role; the substrate-first commitment is structurally honored.
GR_CLASS = {
    "id": "GR",
    "name": "Emergent General Relativity (a_2 channel)",
    "tier": 0,
    "parent_id": None,
    "description": (
        "Constants of substrate-emergent General Relativity. GR is NOT "
        "fundamental in this framework: the Einstein-Hilbert action arises "
        "as the second Seeley-DeWitt coefficient a_2 of the spectral action "
        "on the Jensen-deformed SU(3) Dirac operator. Newton's constant "
        "satisfies 1/(16 pi G_N) = f_2 * a_2 * M_KK^2 (Sakharov / "
        "Chamseddine-Connes); the Planck mass and Planck units inherit. "
        "Members partition into (i) PRIMARY emergence machinery "
        "(a2_fold, M_KK, f_2, c_S_canon, Lambda_Planck, d_spec, "
        "R_protected_fold), (ii) EMERGENT_FROM observables (G_N, M_Pl_*, "
        "l_Planck, t_Planck, rho_crit_GeV4), (iii) DERIVED unit conversions "
        "and slow-roll proxies, and (iv) RELATED Friedmann boundary "
        "conditions. CC and KK are SISTER classes (different spectral "
        "moments — a_0 and M_KK extraction respectively)."
    ),
    "seed_session": "S44",
}

# ------------------------------------------------------------------------------
# Exflation — substrate cosmogenesis (acoustic white hole)
# ------------------------------------------------------------------------------
# The framework's cosmogenesis process — the supersonic transit through the
# Jensen fold that REPLACES inflation. Spans pre-fold cascade ignition,
# fold-event kinematics, Parker / Kibble-Zurek pair production, and post-fold
# GGE relic dynamics. PRIMARY members are the cascade drivers + kinematics +
# impedance. CONSEQUENCE captures the n_pairs relic count (becomes downstream
# PRIMARY in any future GGE-relic class). OBSERVABLE_OUTPUT captures the
# headline cosmological predictions (w0_FW, n_s_framework). Substantial
# overlap with the fold class — fold is the geometric event at tau=0.19;
# Exflation is the WHOLE cascade through that event.
EXFLATION_CLASS = {
    "id": "Exflation",
    "name": "Exflation — substrate cosmogenesis (acoustic white hole)",
    "tier": 0,
    "parent_id": None,
    "description": (
        "The framework's cosmogenesis process end-to-end: the Jensen "
        "deformation parameter tau cascading from an unstable maximum at "
        "tau=0 through the van-Hove fold (tau_fold=0.19) into the post-fold "
        "GGE relic plateau. Replaces inflation with a first-order phase "
        "transition driven by dS/dtau=+58,672; replaces the Big Bang "
        "singularity with a supersonic transit (Mach=13.75). What "
        "cosmologists call 'particle creation' IS the eigenvalue spectrum "
        "reorganization at the fold — n_pairs=59.8 Bogoliubov pairs, "
        "P_exc_kz=1 exactly. Post-fold dynamics are an acoustic white hole "
        "with impedance Gamma_effacement=0.99970 transmitting structure "
        "and (1-Gamma)=3e-4 residual constituting dark-energy-like leakage. "
        "Headline predictions: w0_FW = -0.918, n_s_framework = 0.9561."
    ),
    "seed_session": "S38",
}


# ==============================================================================
#  SECTION B: Class Edge Definitions
# ==============================================================================
#
# Each class has a list ``<ID>_EDGES`` of edge-shaped membership records.
# Schema mirrors REAL_EDGES in tools/viz/console/data.js — at console-build
# time these get merged so the radial-spin renderer is class-aware for free.
#
# role field — 7-axis taxonomy (S86; expanded from the original 3-role schema
# after the GR + Exflation classes surfaced structural friction):
#   INPUTS:
#     PRIMARY           = a defining constant of the class (you cannot describe
#                         the class without this constant; e.g. CC_ratio for CC)
#     PRECONDITION      = a substrate / context property the class CONSUMES but
#                         does not produce (e.g. c_fabric is the substrate sound
#                         speed against which Mach is defined; the cascade does
#                         not produce c_fabric, it consumes it)
#   OUTPUTS (process / emergence):
#     EMERGENT_FROM     = emerges from PRIMARY members via substrate-level
#                         computation requiring regulators, schemes, multi-route
#                         consistency — NOT an algebraic one-liner. (e.g. G_N
#                         from {a_2_fold, M_KK, f_2} via the Sakharov dictionary;
#                         the framework's deepest commitment that GR is NOT
#                         fundamental is honored structurally by this role.)
#     CONSEQUENCE       = produced by the class's process and becomes a
#                         downstream-class PRIMARY (e.g. n_pairs from Exflation
#                         is the headline post-fold-relic observable)
#     OBSERVABLE_OUTPUT = an external-cosmology observable that IS the class's
#                         headline testable prediction (e.g. w0_FW, n_s_framework
#                         from Exflation — measured by Planck/DESI/Euclid)
#   ALGEBRAIC:
#     DERIVED           = algebraic / definitional consequence — unit conversion,
#                         ratio of PRIMARY members (e.g. Lambda_obs_MP4 =
#                         rho_Lambda_obs / M_Pl^4; G_N_cgs = G_N * 1000)
#   CROSS-CUTTING:
#     RELATED           = relevant to the class but not native — kindred
#                         observable from a sister class, or boundary condition
#                         (e.g. m_t_pole RELATED to Higgs because it dominates
#                         Higgs running but isn't Higgs-defining)
#   None    = used for non-membership edge types (tested_by, proven_by, parent_of)
#
# AXIS GUIDANCE — when classifying a constant:
#   • Does the class POSIT this constant? PRIMARY.
#   • Does the class CONSUME this constant pre-existingly? PRECONDITION.
#   • Does the class PRODUCE this constant via substrate computation (not algebra)?
#       EMERGENT_FROM.
#   • Does the class PRODUCE this constant and pass it as PRIMARY downstream?
#       CONSEQUENCE.
#   • Does the class predict this OBSERVABLE for cosmology to test? OBSERVABLE_OUTPUT.
#   • Is this an algebraic consequence (unit conversion, ratio)? DERIVED.
#   • Is this a kindred observable from a sister class? RELATED.

# ------------------------------------------------------------------------------
# CC — edges
# ------------------------------------------------------------------------------
CC_EDGES = [
    {"type": "contains", "srcType": "classes", "src": "CC",
     "tgtType": "constants", "tgt": "CC_ratio", "role": "PRIMARY",
     "comment": "Headline ratio rho_Lambda_spectral / rho_Lambda_obs (~10^120)"},
    {"type": "contains", "srcType": "classes", "src": "CC",
     "tgtType": "constants", "tgt": "rho_Lambda_obs", "role": "PRIMARY",
     "comment": "Observed CC density (Planck 2018, GeV^4)"},
    {"type": "contains", "srcType": "classes", "src": "CC",
     "tgtType": "constants", "tgt": "R_protected_fold", "role": "PRIMARY",
     "comment": "L_max-invariant ratio a_0*a_4/a_2^2; SOLE Chamseddine-Connes observable tying CC (a_0) to GR (a_2) and YM (a_4); Vol(SU(3)) cancels (Baptista B2). S73B/S74."},
    {"type": "contains", "srcType": "classes", "src": "CC",
     "tgtType": "constants", "tgt": "Lambda_obs_MP4", "role": "DERIVED",
     "comment": "Dimensionless Lambda/M_Pl^4 form (= rho_Lambda_obs scaled)"},
    {"type": "contains", "srcType": "classes", "src": "CC",
     "tgtType": "constants", "tgt": "Omega_Lambda", "role": "RELATED",
     "comment": "Dark-energy density parameter (Planck 2018)"},
    {"type": "contains", "srcType": "classes", "src": "CC",
     "tgtType": "constants", "tgt": "Omega_DE_obs", "role": "RELATED",
     "comment": "Planck 2020 DR2 update of Omega_Lambda"},
    {"type": "contains", "srcType": "classes", "src": "CC",
     "tgtType": "constants", "tgt": "Gamma_effacement", "role": "RELATED",
     "comment": "Acoustic-white-hole impedance; (1-Gamma) = effacement residual"},
]

# ------------------------------------------------------------------------------
# KK — edges
# ------------------------------------------------------------------------------
KK_EDGES = [
    {"type": "contains", "srcType": "classes", "src": "KK",
     "tgtType": "constants", "tgt": "M_KK", "role": "PRIMARY",
     "comment": "Canonical alias = M_KK_gravity (conservative route)"},
    {"type": "contains", "srcType": "classes", "src": "KK",
     "tgtType": "constants", "tgt": "M_KK_gravity", "role": "PRIMARY",
     "comment": "Gravity route: spectral zeta / Newton's constant (S42)"},
    {"type": "contains", "srcType": "classes", "src": "KK",
     "tgtType": "constants", "tgt": "M_KK_kerner", "role": "PRIMARY",
     "comment": "Kerner route: gauge-metric extraction (S42)"},
    {"type": "contains", "srcType": "classes", "src": "KK",
     "tgtType": "constants", "tgt": "OOM_diff_MKK", "role": "DERIVED",
     "comment": "log10(M_KK_kerner / M_KK_gravity) = 0.83 decades"},
]

# ------------------------------------------------------------------------------
# alpha_s — edges (parent class; no direct constant members — see children)
# ------------------------------------------------------------------------------
# The parent class has NO contains-edges to constants. All actual member
# constants live in the two child classes. The parent only carries
# parent_of edges to the children.
ALPHA_S_EDGES = [
    {"type": "parent_of", "srcType": "classes", "src": "alpha_s",
     "tgtType": "classes", "tgt": "alpha_s_QCD", "role": None,
     "comment": "QCD strong coupling subtree"},
    {"type": "parent_of", "srcType": "classes", "src": "alpha_s",
     "tgtType": "classes", "tgt": "alpha_s_inflation", "role": None,
     "comment": "Inflationary spectral-index running subtree"},
]

# ------------------------------------------------------------------------------
# alpha_s_QCD — edges
# ------------------------------------------------------------------------------
ALPHA_S_QCD_EDGES = [
    {"type": "contains", "srcType": "classes", "src": "alpha_s_QCD",
     "tgtType": "constants", "tgt": "alpha_s_MZ_obs", "role": "PRIMARY",
     "comment": "PDG 2024 anchor: alpha_s(M_Z) = 0.1180"},
]

# ------------------------------------------------------------------------------
# alpha_s_inflation — edges
# ------------------------------------------------------------------------------
ALPHA_S_INFLATION_EDGES = [
    {"type": "contains", "srcType": "classes", "src": "alpha_s_inflation",
     "tgtType": "constants", "tgt": "planck_alpha_s", "role": "PRIMARY",
     "comment": "Planck 2018 central value (legacy, superseded by alpha_s_canon_2020)"},
    {"type": "contains", "srcType": "classes", "src": "alpha_s_inflation",
     "tgtType": "constants", "tgt": "planck_alpha_s_err", "role": "DERIVED",
     "comment": "Planck 2018 1-sigma on alpha_s"},
    {"type": "contains", "srcType": "classes", "src": "alpha_s_inflation",
     "tgtType": "constants", "tgt": "alpha_s_canon_2020", "role": "PRIMARY",
     "comment": "ACT DR4 + Planck combined (Aiola+ 2020); post-2018 canonical pin"},
    {"type": "contains", "srcType": "classes", "src": "alpha_s_inflation",
     "tgtType": "constants", "tgt": "alpha_s_canon_2020_err", "role": "DERIVED",
     "comment": "Aiola+ 2020 1-sigma on alpha_s"},
    {"type": "contains", "srcType": "classes", "src": "alpha_s_inflation",
     "tgtType": "constants", "tgt": "alpha_s_inflation_framework", "role": "PRIMARY",
     "comment": "Framework prediction: n_s^2 - 1 (S50 identity)"},
    {"type": "contains", "srcType": "classes", "src": "alpha_s_inflation",
     "tgtType": "constants", "tgt": "alpha_s_framework_central", "role": "DERIVED",
     "comment": "Canonical handle alias for alpha_s_inflation_framework (S85 W1c-1)"},
    {"type": "contains", "srcType": "classes", "src": "alpha_s_inflation",
     "tgtType": "constants", "tgt": "alpha_s_cmb_central", "role": "RELATED",
     "comment": "CMB-pivot identity using planck_ns=0.9649 (S50/S85 W13-2)"},
    {"type": "contains", "srcType": "classes", "src": "alpha_s_inflation",
     "tgtType": "constants", "tgt": "planck_ns", "role": "RELATED",
     "comment": "n_s anchor that the framework's alpha_s prediction depends on"},
]

# ------------------------------------------------------------------------------
# fold — edges
# ------------------------------------------------------------------------------
FOLD_EDGES = [
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "tau_fold", "role": "PRIMARY",
     "comment": "Jensen deformation parameter at the fold (= 0.19)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "S_fold", "role": "PRIMARY",
     "comment": "Spectral action at the fold (S42)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "dS_fold", "role": "PRIMARY",
     "comment": "dS/dtau at the fold = +58,672 (drives transit)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "d2S_fold", "role": "PRIMARY",
     "comment": "d^2 S/dtau^2 at the fold (curvature of action)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "Z_fold", "role": "DERIVED",
     "comment": "Gradient stiffness at fold (= G_DeWitt-weighted)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "H_fold", "role": "DERIVED",
     "comment": "Hubble parameter at fold (M_KK units)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "v_terminal", "role": "DERIVED",
     "comment": "Terminal velocity of modulus during transit"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "dt_transit", "role": "DERIVED",
     "comment": "Transit duration (M_KK^-1 units)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "P_exc_kz", "role": "DERIVED",
     "comment": "Kibble-Zurek excitation probability (= 1 exactly)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "n_Bog", "role": "DERIVED",
     "comment": "Bogoliubov fraction per mode"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "n_pairs", "role": "DERIVED",
     "comment": "Bogoliubov quasiparticle pairs from transit (= 59.8)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "c_fabric", "role": "RELATED",
     "comment": "Substrate sound speed (sets Mach number for transit)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "phi_paasch", "role": "RELATED",
     "comment": "Paasch spectral ratio at s=0.15 (PROVEN, related to fold geometry)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "m_tau", "role": "RELATED",
     "comment": "Modulus mass at the fold (M_KK units)"},
    {"type": "contains", "srcType": "classes", "src": "fold",
     "tgtType": "constants", "tgt": "omega_tau", "role": "RELATED",
     "comment": "Transit frequency d(tau)/dt"},
]

# ------------------------------------------------------------------------------
# Higgs — edges
# ------------------------------------------------------------------------------
HIGGS_EDGES = [
    {"type": "contains", "srcType": "classes", "src": "Higgs",
     "tgtType": "constants", "tgt": "m_H_obs", "role": "PRIMARY",
     "comment": "Observed Higgs mass (PDG 2024, 125.1 GeV)"},
    {"type": "contains", "srcType": "classes", "src": "Higgs",
     "tgtType": "constants", "tgt": "v_ew", "role": "PRIMARY",
     "comment": "Electroweak VEV (= 246 GeV)"},
    {"type": "contains", "srcType": "classes", "src": "Higgs",
     "tgtType": "constants", "tgt": "m_t_pole", "role": "RELATED",
     "comment": "Top pole mass (PDG 2024); dominates Higgs-sector running"},
    {"type": "contains", "srcType": "classes", "src": "Higgs",
     "tgtType": "constants", "tgt": "m_b_pole", "role": "RELATED",
     "comment": "Bottom pole mass (PDG 2024); secondary Yukawa contributor"},
]

# ------------------------------------------------------------------------------
# GR — edges (29 members: 7 PRIMARY + 6 EMERGENT_FROM + 4 DERIVED + 12 RELATED)
# ------------------------------------------------------------------------------
# Source: einstein-theorist research-agent proposal (sessions/archive/session-86/
# c1_GR_proposal.md). PRIMARY = the spectral-action emergence machinery that
# EMITS GR. EMERGENT_FROM = the substrate-emergent observables (G_N + cousins;
# substrate-level computation, NOT algebraic one-liners). DERIVED = pure unit
# conversions and the eps_baseline algebraic form. RELATED = Friedmann
# boundary conditions of the emerged 4D theory.
GR_EDGES = [
    # PRIMARY — emergence machinery
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "a2_fold", "role": "PRIMARY",
     "comment": "Second Seeley-DeWitt coefficient at fold; sole source of EH action 1/(16 pi G_N) = f_2 a_2 M_KK^2 (S44 SAKHAROV-GN-44)"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "M_KK", "role": "PRIMARY",
     "comment": "KK scale fixes dimensional anchor of a_2 channel; KK class owns extraction, GR uses as input"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "f_2_default", "role": "PRIMARY",
     "comment": "f_2 spectral cutoff moment (S62 W1 Gaussian-cutoff = 2.34); regulator-pinned prefactor in EH dictionary"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "c_S_canon", "role": "PRIMARY",
     "comment": "Canonical spectral-action scale normalization (Chamseddine-Connes 1997)"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "Lambda_Planck", "role": "PRIMARY",
     "comment": "Planck-scale regulator in M_KK units (= 1.0 default, S85 W6-3)"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "d_spec", "role": "PRIMARY",
     "comment": "Classical spectral dimension of D_K = 3 (Connes-Moscovici); gates which SDW term carries EH content"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "R_protected_fold", "role": "PRIMARY",
     "comment": "L_max-invariant ratio a_0*a_4/a_2^2; ties GR (a_2) to CC (a_0) and YM (a_4) channels"},
    # EMERGENT_FROM — substrate-emergent observables (Sakharov dictionary, regulators)
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "G_N", "role": "EMERGENT_FROM",
     "comment": "Newton's constant from 1/(16 pi G_N) = f_2 a_2 M_KK^2; substrate-level emergence (S44 SAKHAROV-GN-44 PASS, 3-route check)"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "M_Pl_reduced", "role": "EMERGENT_FROM",
     "comment": "Reduced Planck mass = 1/sqrt(8 pi G_N); inherits substrate-emergence from G_N"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "M_Pl_unreduced", "role": "EMERGENT_FROM",
     "comment": "Unreduced Planck mass = sqrt(hbar c / G_N); inherits substrate-emergence"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "l_Planck", "role": "EMERGENT_FROM",
     "comment": "Planck length sqrt(hbar G_N / c^3); inherits substrate-emergence"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "t_Planck", "role": "EMERGENT_FROM",
     "comment": "Planck time sqrt(hbar G_N / c^5); inherits substrate-emergence"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "rho_crit_GeV4", "role": "EMERGENT_FROM",
     "comment": "Critical density 3 H_0^2 / (8 pi G); equation-of-motion of emergent EH action"},
    # DERIVED — algebraic / pure unit conversions
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "G_N_cgs", "role": "DERIVED",
     "comment": "G_N in CGS units (= G_N * 1000); pure unit conversion"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "l_Planck_cm", "role": "DERIVED",
     "comment": "Planck length in cm (= l_Planck * 100); pure unit conversion"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "rho_crit_cgs", "role": "DERIVED",
     "comment": "Critical density in CGS (= rho_crit_GeV4 in g/cm^3); pure unit conversion"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "eps_baseline", "role": "DERIVED",
     "comment": "Substrate slow-roll-equivalent = (1 - planck_ns)/2; algebraic from Planck n_s"},
    # RELATED — boundary conditions / cosmological-standard-model anchors
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "tau_fold", "role": "RELATED",
     "comment": "Jensen evaluation point of a_2; PRIMARY in fold class, RELATED here (per user-confirmed taxonomy)"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "H_0_km_s_Mpc", "role": "RELATED",
     "comment": "Hubble constant 67.4 km/s/Mpc (Planck 2018); Friedmann observational anchor"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "H_0_GeV", "role": "RELATED",
     "comment": "H_0 in GeV; unit conversion of H_0_km_s_Mpc"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "H_0_inv_s", "role": "RELATED",
     "comment": "H_0 in s^-1; unit conversion"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "Omega_m", "role": "RELATED",
     "comment": "Matter density 0.315 (Planck 2018); Friedmann boundary condition"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "Omega_b", "role": "RELATED",
     "comment": "Baryon density 0.0493 (Planck 2018); matter-sector BC"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "Omega_DM", "role": "RELATED",
     "comment": "Dark matter density 0.266; BC (S44 CDM-CONSTRUCT-44 gives DM by construction)"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "Omega_Lambda", "role": "RELATED",
     "comment": "Dark-energy density 0.685; value lives in CC class (a_0), Friedmann observable here"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "Omega_r", "role": "RELATED",
     "comment": "Radiation density 9.15e-5; cosmological boundary condition"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "T_CMB", "role": "RELATED",
     "comment": "CMB temperature 2.7255 K (COBE/FIRAS); BC for Friedmann-radiation era"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "t_universe_s", "role": "RELATED",
     "comment": "Age of universe 4.35e17 s (Planck 2018); Friedmann observable"},
    {"type": "contains", "srcType": "classes", "src": "GR",
     "tgtType": "constants", "tgt": "clock_coeff", "role": "RELATED",
     "comment": "Atomic-clock variation coefficient -3.08 (S22d); tests emergent equivalence-principle behavior"},
]

# ------------------------------------------------------------------------------
# Exflation — edges (34 members: 12 PRIMARY + 8 DERIVED + 1 CONSEQUENCE
#                    + 2 OBSERVABLE_OUTPUT + 11 RELATED)
# ------------------------------------------------------------------------------
# Source: volovik-superfluid-universe-theorist research-agent proposal
# (sessions/archive/session-86/c1_exflation_proposal.md). PRIMARY = the cascade
# drivers + kinematics + impedance. CONSEQUENCE = n_pairs (process-output
# becoming downstream-class PRIMARY). OBSERVABLE_OUTPUT = the headline
# cosmological predictions w0_FW + n_s_framework (external-cosmology testable).
# RELATED = substrate / GGE-relic kindred quantities. tau_fold and c_fabric
# follow user-confirmed taxonomy (#3, #5): tau_fold PRIMARY in fold, RELATED
# in Exflation; c_fabric PRIMARY in Exflation, RELATED in fold.
EXFLATION_EDGES = [
    # PRIMARY — cascade drivers + kinematics + impedance
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "dS_fold", "role": "PRIMARY",
     "comment": "Spectral action gradient at fold = +58,672; substrate-driver of cascade (the 'inflaton field' in container language)"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "S_fold", "role": "PRIMARY",
     "comment": "Spectral action at fold = 250,360.7; absolute energy scale of cascade event"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "Mach_max_framework", "role": "PRIMARY",
     "comment": "Mach number at fold = 13.75; defining property — supersonic transit IS the acoustic white hole"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "v_terminal", "role": "PRIMARY",
     "comment": "Terminal velocity of modulus = 26.545 (M_KK units); kinematic state at fold"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "dt_transit", "role": "PRIMARY",
     "comment": "Transit duration = 1.13e-3 M_KK^-1; impulsiveness defines KZ freezing window"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "H_fold", "role": "PRIMARY",
     "comment": "Hubble parameter at fold = 586.5 (M_KK units); expansion rate during transit"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "P_exc_kz", "role": "PRIMARY",
     "comment": "Kibble-Zurek excitation probability = 1.0 exactly; saturation (no Landau-Zener adiabaticity)"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "n_Bog", "role": "PRIMARY",
     "comment": "Bogoliubov fraction per mode = 0.9986; pins per-mode GGE distribution shape"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "T_acoustic", "role": "PRIMARY",
     "comment": "GGE acoustic temperature = 0.112 M_KK; relic's effective acoustic temperature on substrate (algebraic GGE permanence)"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "Gamma_effacement", "role": "PRIMARY",
     "comment": "Acoustic-white-hole impedance = 0.99970; (1-Gamma)=3e-4 = effacement residual"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "c_fabric", "role": "PRIMARY",
     "comment": "Substrate sound speed = 209.97; Mach denominator (Mach=v_terminal/c_fabric)"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "c_BLV", "role": "PRIMARY",
     "comment": "BLV post-fold scalar sound speed = 0.485 (S64); GGE-relic phonon sector"},
    # DERIVED — algebraic consequences
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "d2S_fold", "role": "DERIVED",
     "comment": "Curvature of spectral action at fold; characterizes width of fold transit"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "Z_fold", "role": "DERIVED",
     "comment": "Gradient stiffness at fold; G_DeWitt-weighted moduli-space stiffness"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "omega_tau", "role": "DERIVED",
     "comment": "Transit frequency d(tau)/dt; algebraic from v_terminal + modulus mass"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "omega_att", "role": "DERIVED",
     "comment": "Post-fold attractor frequency = 1.430; geometric from spectral action curvature at attractor"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "E_exc_ratio", "role": "DERIVED",
     "comment": "Excitation/condensation ratio = 443.0; Schwinger-instanton-duality measure"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "E_exc", "role": "DERIVED",
     "comment": "Total excitation energy from BCS transit quench (= E_exc_ratio * |E_cond|)"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "T_compound", "role": "DERIVED",
     "comment": "Microcanonical post-fold compound temperature (= E_exc / 8 across BCS Fock modes)"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "N_pivot", "role": "DERIVED",
     "comment": "CMB pivot e-fold count = 64.08 = 55 + ln(c/c_s); substrate-c_s correction to LCDM"},
    # CONSEQUENCE — process output becoming downstream PRIMARY
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "n_pairs", "role": "CONSEQUENCE",
     "comment": "Bogoliubov pairs from transit = 59.8; produced BY cascade, becomes PRIMARY in any future GGE-relic class"},
    # OBSERVABLE_OUTPUT — external-cosmology testable predictions
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "w0_FW", "role": "OBSERVABLE_OUTPUT",
     "comment": "Framework dark-energy EOS w_0 = -0.918 (Volovik vacuum + effacement); DESI/Euclid testable"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "n_s_framework", "role": "OBSERVABLE_OUTPUT",
     "comment": "Framework scalar spectral index at CMB pivot = 0.9561 (S84 T6); Planck/CMB-S4 testable"},
    # RELATED — substrate / GGE-relic kindred quantities
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "tau_fold", "role": "RELATED",
     "comment": "Cascade transits THROUGH this tau locus; PRIMARY in fold, RELATED here (per user-confirmed taxonomy)"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "phi_paasch", "role": "RELATED",
     "comment": "Paasch spectral ratio (PROVEN, S12); substrate-static identity pre-dating cascade"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "m_tau", "role": "RELATED",
     "comment": "Modulus mass at fold = 2.062; inertial response to dS_fold gradient"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "Q_Leggett", "role": "RELATED",
     "comment": "Leggett mode quality factor 6.7e5 (S50); cascade-survivor DM candidate"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "T_BCS", "role": "RELATED",
     "comment": "BCS canonical temperature 0.640; substrate-pairing scale partially surviving transit"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "T_c_BCS", "role": "RELATED",
     "comment": "BCS critical temperature 0.083; post-fold residual-pairing scale"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "kappa_BCS", "role": "RELATED",
     "comment": "BCS surface-gravity analog 4.019 (S69); white-hole side characterization"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "tau_phase_trans", "role": "RELATED",
     "comment": "C^2 sectional K=0 phase transition (S48); second tau-landmark beyond tau_fold"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "tau_overshoot", "role": "RELATED",
     "comment": "Overshoot turnaround at K=53.35 (S77); post-fold modulus dynamics first turnaround"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "v_crit", "role": "RELATED",
     "comment": "Censorship critical velocity = 219.3; transit just barely satisfies v_terminal < v_crit"},
    {"type": "contains", "srcType": "classes", "src": "Exflation",
     "tgtType": "constants", "tgt": "eps_H_W6", "role": "RELATED",
     "comment": "Slow-roll bound from S80 dS/dtau at fold; interface between substrate and slow-roll-equivalent observables"},
]


# ==============================================================================
#  SECTION C: Aggregated Registries
# ==============================================================================

# All classes — built mechanically from the per-class dicts above.
# Order is significant for downstream consumers (root-tier classes first).
CLASSES = {
    "CC":                CC_CLASS,
    "KK":                KK_CLASS,
    "alpha_s":           ALPHA_S_CLASS,
    "alpha_s_QCD":       ALPHA_S_QCD_CLASS,
    "alpha_s_inflation": ALPHA_S_INFLATION_CLASS,
    "fold":              FOLD_CLASS,
    "Higgs":             HIGGS_CLASS,
    "GR":                GR_CLASS,
    "Exflation":         EXFLATION_CLASS,
}

# All edges concatenated in a single list — matches REAL_EDGES schema for
# the visualizer's consumption.
CLASS_EDGES = (
    CC_EDGES
    + KK_EDGES
    + ALPHA_S_EDGES
    + ALPHA_S_QCD_EDGES
    + ALPHA_S_INFLATION_EDGES
    + FOLD_EDGES
    + HIGGS_EDGES
    + GR_EDGES
    + EXFLATION_EDGES
)


# ==============================================================================
#  SECTION D: Helper Functions
# ==============================================================================

def get_class(class_id):
    """Return the class metadata dict for ``class_id``, or None."""
    return CLASSES.get(class_id)


def get_class_members(class_id):
    """Return a list of (constant_id, role) tuples for the class.

    Only includes ``contains`` edges whose tgtType is ``constants``.
    Returns an empty list if the class has no constant members
    (e.g. a parent class whose members live in children).
    """
    out = []
    for e in CLASS_EDGES:
        if e["src"] == class_id and e["type"] == "contains" and e["tgtType"] == "constants":
            out.append((e["tgt"], e["role"]))
    return out


def get_classes_for_constant(constant_id):
    """Return the list of class IDs that contain ``constant_id``."""
    out = []
    for e in CLASS_EDGES:
        if (e["type"] == "contains"
                and e["tgtType"] == "constants"
                and e["tgt"] == constant_id):
            out.append(e["src"])
    return out


def get_class_edges(class_id, edge_type=None):
    """Return all CLASS_EDGES rows where ``src == class_id``.

    Optional filter on ``edge_type`` (e.g. "contains", "parent_of").
    """
    out = []
    for e in CLASS_EDGES:
        if e["src"] != class_id:
            continue
        if edge_type is not None and e["type"] != edge_type:
            continue
        out.append(e)
    return out


def get_subclasses(class_id):
    """Return the list of class IDs that have ``class_id`` as parent."""
    return [
        cid for cid, c in CLASSES.items()
        if c.get("parent_id") == class_id
    ]


def get_root_classes():
    """Return all class IDs with tier == 0 (no parent)."""
    return [cid for cid, c in CLASSES.items() if c.get("tier") == 0]


# ==============================================================================
#  SECTION E: Self-Validation
# ==============================================================================

if __name__ == "__main__":
    # Validate that every constant ID referenced in CLASS_EDGES resolves to
    # a real name in this module's globals (populated by the module-level
    # ``from canonical_constants import *``). Catches typos at the source
    # level before extract_entities / the MCP / the visualizer ever see
    # the dangling reference.
    print("=" * 78)
    print(f"CANONICAL CLASSES VALIDATION ({len(CLASSES)} classes, "
          f"{len(CLASS_EDGES)} edges)")
    print("=" * 78)

    # 1. Every class has the required schema fields
    schema_required = {"id", "name", "tier", "parent_id", "description", "seed_session"}
    schema_failed = 0  # (local) validation counter
    for cid, c in CLASSES.items():
        missing = schema_required - set(c.keys())
        if missing:
            print(f"  FAIL  class '{cid}' missing fields: {missing}")
            schema_failed += 1
        if c["id"] != cid:
            print(f"  FAIL  class registry key '{cid}' != class['id'] '{c['id']}'")
            schema_failed += 1
    if schema_failed == 0:
        print(f"  PASS  schema:    all {len(CLASSES)} classes have required fields")

    # 2. parent_id resolution — every non-None parent_id refers to a real class
    parent_failed = 0  # (local) validation counter
    for cid, c in CLASSES.items():
        pid = c.get("parent_id")
        if pid is None:
            continue
        if pid not in CLASSES:
            print(f"  FAIL  class '{cid}' parent_id='{pid}' does not exist")
            parent_failed += 1
    if parent_failed == 0:
        print(f"  PASS  parent_id: all parent references resolve")

    # 3. tier consistency — root classes have computation; children have tier
    #    parent.tier + 1.
    tier_failed = 0  # (local) validation counter
    for cid, c in CLASSES.items():
        pid = c.get("parent_id")
        if pid is None:
            if c.get("tier") != 0:
                print(f"  FAIL  class '{cid}' has no parent but tier={c.get('tier')} != 0")
                tier_failed += 1
        else:
            expected = CLASSES[pid].get("tier", 0) + 1
            if c.get("tier") != expected:
                print(f"  FAIL  class '{cid}' tier={c.get('tier')} but parent "
                      f"'{pid}' tier={CLASSES[pid].get('tier')} (expected "
                      f"tier={expected})")
                tier_failed += 1
    if tier_failed == 0:
        print(f"  PASS  tier:      all classes have consistent nest depth")

    # 4. Constant-ID resolution — every constant referenced in a contains
    #    edge with tgtType='constants' must exist as a name in this module's
    #    globals (populated by the canonical_constants wildcard import).
    _module_globals = set(globals().keys())  # (local) snapshot for resolution check
    const_failed = 0   # (local) validation counter
    const_checked = 0  # (local) validation counter
    for e in CLASS_EDGES:
        if e["type"] != "contains" or e["tgtType"] != "constants":
            continue
        const_checked += 1
        if e["tgt"] not in _module_globals:
            print(f"  FAIL  edge {e['src']} -> {e['tgt']} : constant not in "
                  f"canonical_constants")
            const_failed += 1
    if const_failed == 0:
        print(f"  PASS  constants: all {const_checked} referenced constants "
              f"exist in canonical_constants")

    # 5. Class-target resolution — every parent_of / sibling_of edge with
    #    tgtType='classes' must resolve to a real class.
    classref_failed = 0   # (local) validation counter
    classref_checked = 0  # (local) validation counter
    for e in CLASS_EDGES:
        if e["tgtType"] != "classes":
            continue
        classref_checked += 1
        if e["tgt"] not in CLASSES:
            print(f"  FAIL  edge {e['src']} -> {e['tgt']} : class reference "
                  f"does not exist")
            classref_failed += 1
    if classref_failed == 0:
        print(f"  PASS  classref: all {classref_checked} class-to-class "
              f"references resolve")

    # 6. Role-field validity — contains-edges with tgtType='constants' must
    #    have role in the 7-axis taxonomy; non-contains edges have role=None.
    role_failed = 0  # (local) validation counter
    valid_roles = {"PRIMARY", "PRECONDITION",
                   "EMERGENT_FROM", "CONSEQUENCE", "OBSERVABLE_OUTPUT",
                   "DERIVED", "RELATED"}
    for e in CLASS_EDGES:
        if e["type"] == "contains" and e["tgtType"] == "constants":
            if e["role"] not in valid_roles:
                print(f"  FAIL  edge {e['src']} -> {e['tgt']} role={e['role']} "
                      f"not in {valid_roles}")
                role_failed += 1
        else:
            if e["role"] is not None:
                print(f"  FAIL  edge {e['src']} -> {e['tgt']} type={e['type']} "
                      f"role should be None, got {e['role']}")
                role_failed += 1
    if role_failed == 0:
        print(f"  PASS  roles:     all roles match edge-type schema")

    # 7. Class-membership cross-check — for each root-tier class, print
    #    member counts so a human can sanity-check.
    print("\n--- Class membership summary ---")
    for cid in get_root_classes():
        c = CLASSES[cid]
        members = get_class_members(cid)
        subs = get_subclasses(cid)
        print(f"  {cid:<20s}  members={len(members):>2d}  subclasses={len(subs)}")
        for sub_id in subs:
            sub_members = get_class_members(sub_id)
            print(f"    └─ {sub_id:<16s}  members={len(sub_members):>2d}")

    # ── Summary ──
    total_failed = (schema_failed + parent_failed + tier_failed
                    + const_failed + classref_failed + role_failed)
    print(f"\n{'=' * 78}")
    if total_failed == 0:
        print(f"PASS — all checks succeeded")
        print(f"  classes:      {len(CLASSES)}")
        print(f"  edges:        {len(CLASS_EDGES)}")
        print(f"  constants:    {const_checked} resolved")
        print(f"  class refs:   {classref_checked} resolved")
        print(f"{'=' * 78}")
        sys.exit(0)
    else:
        print(f"FAIL — {total_failed} validation failure(s)")
        print(f"{'=' * 78}")
        sys.exit(1)
