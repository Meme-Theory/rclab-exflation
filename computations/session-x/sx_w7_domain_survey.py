"""
sx_w7_domain_survey.py
======================

WX-W7-1 — AGGREGATE-DOMAIN-SURVEY (the SURVEY engine for the G2 expansion)

Maps the WHOLE framework <-> Landau-condensed-matter DOMAIN across S45 -> S93
against the knowledge base, producing TWO artifacts that drive G2:

  (1) sx_w7_state_of_domain_map.json  — every existing §I row's current S93 fate
      (CURRENT / SUPERSEDED / SUPERSEDED-by-mechanism-shift / SUPERSEDED-context /
       STALE-by-precision / CONTRADICTED / CONDITIONAL / PROMOTED) + KB citation;
      every §§II-VII prose seed-claim's current value.

  (2) sx_w7_gap_analysis.json  — the gap between "what the project knows in this
      domain" and "what the S44 document covers": every NEW-since-S44 correspondence
      {correspondence, cm_concept, session_gate_citation, landau_paper, doc_placement,
       proposed_status_tag}, PLUS every existing-row refresh row.

SUBSTRATE FRAMING (PHONONIC; phononic-framing.md §"IS Space, Not IN Space")
---------------------------------------------------------------------------
The domain IS the substrate's condensed-matter STRUCTURE. The eigenvalue spectrum
of D_K on Jensen-deformed SU(3) IS the order-parameter manifold (tau); the BCS gap
Delta(tau) IS the superconducting order parameter on the fiber; the Leggett inter-band
mode IS a phason of the B2-B3 sector; the GGE IS the post-transit integrable relic.
The survey reads the substrate's spectral content (D_K eigenvalues -> spectral moments
-> Landau free energy / two-fluid partition -> observable) and asks WHICH Landau-
classification structures the project has established since S44. Direction flows FROM
the spectral triple TOWARD the CM classification — never "the substrate behaves like a
superconductor"; rather "the substrate IS a spectral triple whose BCS sector is in the
3D-Ising universality class".

GATE LOGIC (coverage-by-enumeration; no numerical threshold)
------------------------------------------------------------
PASS iff: (i) every existing §I row has a fate-verdict row with a KB citation;
          (ii) every §§II-VII prose seed-claim has a current value;
          (iii) the new-correspondence set contains >= the 14-row table-B seed,
                each with a KB citation + doc_placement;
          (iv) the kb_query_manifest contains >= 25 distinct queries spanning
               >= 5 entity classes.
A survey that only re-checks existing claims (empty new-correspondence set) FAILS.

This is a SURVEY/SYNTHESIS gate (math-scripts.md): boundary_reachable_analytically
via coverage-by-enumeration; no eigenvalue compute; closure = load inputs -> serialize
JSON -> dual SHA -> append_verdict. The intellectual work (the survey itself) is the
KB sweep recorded in the WP MCP Pre-Compute Audit block + the two JSON artifacts.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE — use absolute paths)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants).
# G1 reads canonical values to currency-stamp the survey; G2/G3 consume them.
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,
    Delta_BCS,
    E_cond,
    Q_Leggett,
    omega_L1,
    c_Gold,
    M_max_thouless,
    xi_BCS,
    CC_OOM,
    n_s_framework,
    planck_ns,
    alpha_s_cmb_central,
    eps_H_W6,
    Omega_DM_obs,
    Omega_DE_obs,
    cocycle_norm_phi67,
    cocycle_norm_phi88,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan §W7-1 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "WX-W7-1"
SCHEME = "AGGREGATE-DOMAIN-SURVEY"
CONVENTION = "substrate-IS-direction-per-phononic-framing"
L_MAX = "NA"  # survey gate — no eigenvalue truncation

VERDICT_TXT = PROJECT_ROOT / "computations" / "session-x" / "sx_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
DOCUMENT_PATH = PROJECT_ROOT / "sessions" / "framework" / "Classification-of-phonon-exflation.md"
KNOWLEDGE_DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"

OUT_STATE_MAP = PROJECT_ROOT / "computations" / "session-x" / "sx_w7_state_of_domain_map.json"
OUT_GAP = PROJECT_ROOT / "computations" / "session-x" / "sx_w7_gap_analysis.json"


# -----------------------------------------------------------------------------
# SHA helpers (per s93_w2_1 / _script_template.py precedent)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    """SHA-256 of a UTF-8 string (for in-memory JSON artifacts)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compute_dual_sha(audit_inputs: dict, content_inputs: dict) -> tuple[str, str]:
    """(audit_sha256, content_sha256).

    audit_sha256 over {document_pre, state_of_domain_map, gap_analysis,
                       canonical_constants_snapshot, kb_query_manifest};
    content_sha256 over {state_of_domain_map, gap_analysis}
    per plan §W7-1 audit_discriminators.
    """
    audit_json = json.dumps(dict(sorted(audit_inputs.items())),
                            separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    content_json = json.dumps(dict(sorted(content_inputs.items())),
                              separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    return (hashlib.sha256(audit_json).hexdigest(),
            hashlib.sha256(content_json).hexdigest())


# -----------------------------------------------------------------------------
# KB query manifest (entity-class-tagged; recorded in WP MCP Pre-Compute Audit).
# Each entry: (tool, query, entity_class, salient_return). >= 25 queries, >= 5
# entity classes per plan strict_PASS_boundary (iv).
# -----------------------------------------------------------------------------
KB_QUERY_MANIFEST = [
    # ---- search_knowledge (FTS5 across all entity types) ----
    ["search_knowledge", "BCS Cooper pairing gap condensation energy", "multi",
     "E_cond=-0.136851 (ED-8mode); F[Delta]=sum F_BCS+E_J(1-cos); BCS=1D theorem D6"],
    ["search_knowledge", "superfluid two-fluid Leggett dark matter collective mode", "theorem/registry",
     "LEGGETT-MOMENT-70 atlas-10 #23 (first Type-F DM mass anchor); framework-dm-properties registry"],
    ["search_knowledge", "Landau free energy phase transition universality class", "theorem/equation",
     "V_eff(s)=Tr f(D^2/L^2) IS Landau F(eta) (S20b); F_GL=-a^2/4b at min (S54)"],
    ["search_knowledge", "Fermi liquid Pomeranchuk effective mass quasiparticle", "closed/theorem",
     "Resolvent-Fermi-liquid correspondence (S63 framework-cc-oom); Pomeranchuk f_0=-4.687; LANDAU-4 S61"],
    ["search_knowledge", "Kibble-Zurek quench n_s spectral tilt geometric", "equation/theorem",
     "n_s=1-2 eps_H (S64); Mode-Independent Occupation Theorem S57; NS-TILT-42 superseded"],
    ["search_knowledge", "GGE Richardson-Gaudin Ordered Veil integrability level statistics", "theorem/researcher",
     "Ordered Veil S38 #8; Gamma_q(BCS)=0 exact; 8 Richardson-Gaudin integrals; Landau researcher index"],
    ["search_knowledge", "Ginzburg-Landau coherence penetration BKT vortex unbinding", "equation/provenance",
     "T_BKT=(pi/2) rho_s_eff (S56/S74); lambda/xi GL; bkt_sector_resolved RESOLVED-74"],
    ["search_knowledge", "3He-B BDI inheritance morphism falsifier cocycle Caroli-Matricon", "gate/theorem",
     "S87-W11-C5-LAB-FALSIFIER PASS value=7.324992; Door-S86-3HeB; Window-11; chi:C+H+M3->M2"],
    ["search_knowledge", "Volovik free-energy partition condensation Josephson vacuum matter", "theorem",
     "Volovik Partition baseline #27: F_Josephson=-336.6 (95.9% vacuum); F_BCS+BA+Leggett=14.411 matter"],
    ["search_knowledge", "second sound Mott transition OES gap observational horizon", "theorem/provenance",
     "Mott transition CC S65: E_J/E_C=194 (571x above critical, inaccessible); OBS-68 second sound; Delta_0_OES"],
    ["search_knowledge", "BCS-BEC crossover GPE Gross-Pitaevskii regime", "equation/theorem",
     "BEC-61 N-scan: N=1 BEC, N=2 BEC-crossover, N=4 BCS-crossover; E_vac/E_cond=28.8 g*N=2.18"],
    ["search_knowledge", "Kohn anomaly modulus softening Ginzburg number fabric fluctuation", "equation/provenance",
     "Gi_fluct=0.9401 (d_eff=8) / 0.506; Kohn->backaction-drag reclass (S53 baptista-volovik)"],
    ["search_knowledge", "Leggett Goldstone mass phason inter-band phase mode U(1)_7", "theorem/equation",
     "m_L1=0.070 (local, U(1)_7 breaking); rho_s(C^2)=7.96 vs rho_s(u(1))=0.33; c_L=0.025; MASS-48"],
    ["search_knowledge", "alpha_s running Mellin residue n_s squared minus one scale channel", "equation/class",
     "alpha_s=n_s^2-1=-8587279/1e8; TWO canonical_classes (QCD vs inflationary); S50/S84/S89"],
    ["search_knowledge", "DILUTION-CC universality class mismatch tracking vacuum cosmological constant", "constant/theorem",
     "CC_OOM=115.5 (S66 DILUTION-CC, rho_vac/rho_obs=1.032); C10 Volovik tracking rho_vac~M_Pl^2 H^2"],
    ["search_knowledge", "OCC-SPEC occupied state spectral action monotone decreasing S45", "theorem/gate",
     "OCC-SPEC-45 = FAIL: S_occ monotone decreasing, 28th equilibrium closure (atlas-07 #42)"],
    ["search_knowledge", "DM DE ratio specific heat exponent alpha Omega flat-band partition", "theorem/equation",
     "DM/DE OPEN (2.7x); C_GGE=sum (dE/dT_k)(dT_k/dT_eff) open computation; flat-band alpha=1 -> 1.06"],
    ["search_knowledge", "level statistics Poisson Brody Thouless time Cayley graph Laplacian", "equation/theorem",
     "t_Th=1/(E_J lambda_1(L_graph)) CG(24); <r>=0.321-0.367 Poisson; Brody beta=0.001 (2,1) sector"],
    ["search_knowledge", "superfluid stiffness anisotropy tensor Lie algebra response S47", "theorem/equation",
     "[NEW S47] rho_s 24x anisotropic rho_s(C^2)=7.96 rho_s(u(1))=0.33; curvature-stiffness r=-0.906 p=0.002"],
    ["search_knowledge", "multi-instanton effective mass liquid Sakharov induced gravity G_N", "theorem/edge",
     "C8 Sakharov G_N CONDITIONAL: 2.29 (0.36 OOM) at L=10 M_KK; 26.8 (1.43 OOM) at M_Pl; SAKHAROV-PHONON-53"],
    ["search_knowledge", "Landau collab workshop phonon session classification BCS gap", "registry/session",
     "Landau-collab corpus S20b/S22c/S28/S49/S54/S57/S58/S59/S71; reviews nazarewicz/einstein/qa/tesla; S82-XI PASS"],
    ["search_knowledge", "effacement wall ODLRO off-diagonal long range order invisible spectral action", "theorem/equation",
     "Effacement wall 0.002% (S44 W5-4); BDG-SA-61 condensate invisible 1.36e-4; kappa_kl=<c_-l c_k> anomalous"],
    # ---- trace_entity (evidence chain across entity types) ----
    ["trace_entity", "LEGGETT-MOMENT", "theorem/gate/provenance",
     "Door-S70 Type-F single-summand trace; Omega_DM h^2=0.1200 (Leggett-only 0.03985 x 3.010); Q=670000"],
    ["trace_entity", "Volovik partition", "gate/provenance/equation",
     "PARTITION-58/62; euclidean_volovik S59; w0_FW=-0.918 (effacement Gamma_eff=0.99970)"],
    ["trace_entity", "GGE permanence", "theorem/equation",
     "RETRACTED at FULL-isometry S39 (V_phys 13% non-sep, t_therm~6); PERMANENT in BCS sector (Door-S62-Meissner, RG-integrability)"],
    ["trace_entity", "3He-B inheritance", "theorem/gate/equation",
     "Door-S86-3HeB rank-2 ker(iota_*); S88-CARTESIAN-CONFIRM (chi_M3 residual 0); S90 watchlist 50/50 PASS"],
    ["trace_entity", "OCC-SPEC", "theorem/gate/equation",
     "OCC-SPEC-45 FAIL (S_occ monotone decr, 28th closure); S_occ=sum d_k n_k(tau) f(lambda^2/L^2) eq (1)"],
    ["trace_entity", "Pomeranchuk", "theorem/gate/open",
     "f_0=-4.687<-3 g*N(0)=3.24 PERMANENT (S22c); POMERANCHUK-GGE-58 FAIL; ROBUST at L=5,7 (W3-A)"],
    # ---- get_constant (canonical value + Superseded flag; the currency layer) ----
    ["get_constant", "tau_fold", "constant", "0.19; CONST-FREEZE-42; Superseded=False"],
    ["get_constant", "Delta_BCS", "constant", "0.4642547394830737; R-PROTECTED; alias Delta_0_OES; BCS-GAP-CANONICAL-70"],
    ["get_constant", "E_cond", "constant", "-0.13685055970476342; alias E_cond_ED_8mode; ED-CONV-36; Superseded=False"],
    ["get_constant", "Q_Leggett", "constant", "670000.0 (=6.7e5; S50 LEGGETT-DAMPING-50)"],
    ["get_constant", "omega_L1", "constant", "0.138 (Leggett-1 frequency, M_KK)"],
    ["get_constant", "m_L1", "constant", "NOT a canonical constant — # (local) 0.070 M_KK (S80 WP; S49 DIPOLAR-CATALOG)"],
    ["get_constant", "c_Gold", "constant", "0.915 (Goldstone sound speed, M_KK units)"],
    ["get_constant", "M_max_thouless", "constant", "1.674 (Thouless criterion, S35 RPA)"],
    ["get_constant", "n_s_framework", "constant", "0.9561 (S84 T6 const-eps pivot); n_s_FW_exact=9561/10000 supersedes 0.9567/0.9557/0.9595"],
    ["get_constant", "alpha_s_cmb_central", "constant", "-0.06896799 (=n_s^2-1 with planck_ns=0.9649, S50); substrate-distance Mellin=-0.08587279"],
    ["get_constant", "Omega_DM", "constant", "0.2657 (Omega_m-Omega_b); Omega_DM_obs=0.264 Planck 2020 DR2"],
    ["get_constant", "eps_H", "constant", "eps_H_W6=0.02163 (slow-roll bound, S80 dS/dtau at fold; the value that gives correct tilt); doc old '3.0' STALE"],
    ["get_constant", "CC_OOM", "constant", "115.5; S66-W1-A-DILUTION-CC; Superseded=False (rho_vac/rho_obs=1.032)"],
    ["get_constant", "xi_BCS", "constant", "0.8083468753837275; S37 instanton_mc; Superseded=False"],
    ["get_constant", "planck_ns", "constant", "0.9649 (Planck 2018 TT,TE,EE+lowE+lensing); err 0.0042"],
    ["get_constant", "cocycle_ratio_phi67_phi88", "constant",
     "NOT a single canonical; cocycle_norm_phi67=0.793346 / cocycle_norm_phi88=0.108307; ratio=7.3249917525961665 (substrate_cocycle_ratio_67_88, F2-faithful)"],
    ["get_constant", "Omega_DE_obs", "constant", "0.685 (Planck 2020 DR2)"],
]

ENTITY_CLASSES_SURVEYED = sorted({
    "theorems", "closed", "gates", "open", "constants", "equations",
    "sessions", "provenance", "registries",
})


def build_state_of_domain_map() -> dict:
    """Every existing §I row's current S93 fate + every §§II-VII prose seed-claim's
    current value. verdict_class in {CURRENT, SUPERSEDED, SUPERSEDED-by-mechanism-shift,
    SUPERSEDED-context, STALE-by-precision, CONTRADICTED, CONDITIONAL, PROMOTED}."""
    # The ~33 existing §I rows of the S44 document, each with current fate + KB cite.
    existing_rows = [
        {"row": "Jensen deformation tau -> Order parameter eta", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Order parameter unchanged; tau_fold=0.19 CONST-FREEZE-42.",
         "citation": "get_constant(tau_fold)=0.19 Superseded=False; S17a Paper 04"},
        {"row": "SU(3) -> U(1)_7 -> Symmetry breaking G -> H", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "[iK_7,D_K]=0 exact (S34); SU(3)_L x SU(2)_R x U(1)_R / Z_6 surviving.",
         "citation": "MEMORY framework-constants; S34 Paper 04"},
        {"row": "Spectral action S(tau) -> Landau free energy F(eta)", "s44_status": "STRUCTURAL",
         "verdict_class": "CURRENT", "current_state": "V_eff(s)=Tr f(D_K^2/L^2) IS Landau F(eta) reaffirmed S20b, S54.",
         "citation": "search_knowledge 'V_eff(s) ... IS the Landau free energy' (session-20b-landau-collab); S17a Paper 04"},
        {"row": "V'''(0)=-7.2 -> Cubic term forces first-order", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Perturbative Exhaustion Theorem (baseline #12, S22c): F_pert not true free energy; first-order.",
         "citation": "baseline-findings-s66 #12; Paper 04 sec.8"},
        {"row": "d_int=8 > d_uc=4 -> Mean-field exact above d_uc", "s44_status": "STRUCTURAL",
         "verdict_class": "CURRENT", "current_state": "Mean-field exact for internal moduli (d_eff=8) unchanged.",
         "citation": "S17a Paper 04 sec.7"},
        {"row": "Transit tau=0 to fold -> First-order phase transition", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "First-order at fold; transit paradigm (instanton gas, not potential well).",
         "citation": "atlas-10 Ordered Veil S38; S37-38 Paper 04,09"},
        {"row": "BCS condensation at fold -> Superconducting transition", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "BCS at fold; universality class 3D Ising PERMANENT (S43).",
         "citation": "search_knowledge BCS-CLASS; S35 Paper 08,15"},
        {"row": "BCS instanton gas -> Giant pair vibration (GPV)", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Instanton paradigm permanent (atlas-07 #4).",
         "citation": "atlas-07 #4; S37 Paper 23,24,25"},
        {"row": "S_inst=0.069 -> Quantum critical point", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "S_inst=0.069, P_exc=1.000, E_exc/|E_cond|=443 (atlas-03).",
         "citation": "atlas-03-equation-flow; S38 Paper 29"},
        {"row": "Post-transit GGE -> Normal component at rest", "s44_status": "STRUCTURAL",
         "verdict_class": "CURRENT", "current_state": "GGE normal component; two-fluid grounding deepened (S67 GGE-TWO-FLUID).",
         "citation": "S67 FLUID-67; S38 Paper 05,20"},
        {"row": "Dark energy -> Superfluid condensation energy", "s44_status": "OPEN",
         "verdict_class": "CURRENT", "current_state": "Still OPEN as condensation energy; Volovik partition assigns F_Josephson->vacuum; effacement-residual route.",
         "citation": "search_knowledge Volovik Partition (baseline #27); S44 W6-4 Paper 05"},
        {"row": "Dark matter -> Quasiparticle energy at rest", "s44_status": "PROVEN",
         "verdict_class": "PROMOTED", "current_state": "PROMOTED: Leggett-channel gives first Type-F DM MASS anchor Mass/Delta_BCS=11.97; Omega_DM h^2=0.1200 Leggett-only.",
         "citation": "trace_entity LEGGETT-MOMENT (atlas-10 #23, Door-S70); S70; Paper 05,11,20"},
        {"row": "DM/DE ratio -> Specific heat exponent alpha", "s44_status": "OPEN (2.7x)",
         "verdict_class": "CURRENT", "current_state": "Still OPEN; flat-band partition 1.060 (2.74x over-prediction); GGE C_GGE=sum (dE/dT_k)(dT_k/dT_eff) open computation.",
         "citation": "search_knowledge DM-DE-RATIO-44; C_GGE eqn (s44-quicklook-volovik); Paper 04,05"},
        {"row": "G_N -> Effective mass / response coeff.", "s44_status": "PROVEN (factor 2.3)",
         "verdict_class": "CONDITIONAL", "current_state": "PROVEN-CONDITIONAL: ratio 2.29 (0.36 OOM) at Lambda=10 M_KK; 26.8 (1.43 OOM) at M_Pl; cutoff not fixed by framework. SAKHAROV-PHONON-53, SAKHAROV-GN-DIRAC (S75).",
         "citation": "atlas-04 C8 (CONDITIONAL); theorem_closure_edges proven_1071; S44 W1-1 Paper 11"},
        {"row": "Spectral triple dissolution -> Effective theory emergence", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Dissolution scaling eps_c ~ 1/sqrt(N) (DISSOLUTION-44).",
         "citation": "S44 W6-7 Paper 04 (universality)"},
        {"row": "CC fine-tuning -> Universality class mismatch", "s44_status": "STRUCTURAL",
         "verdict_class": "SUPERSEDED-context", "current_state": "Mismatch real, but cosmological resolution = Volovik tracking vacuum (DILUTION-CC-66 closes 114->0.01 OOM; CC_OOM=115.5). Not a CM-internal mechanism.",
         "citation": "get_constant(CC_OOM)=115.5 S66-W1-A; atlas-04 C10; S44 W5-5 Paper 04 sec.7"},
        {"row": "n_s=0.965 -> Quench dynamics / Kibble-Zurek", "s44_status": "OPEN",
         "verdict_class": "SUPERSEDED-by-mechanism-shift", "current_state": "Resolution moved OFF Kibble-Zurek ONTO geometry: n_s=1-2 eps_H, Mode-Independent Occupation Theorem (S57), COMPOUND-NS-73a, substrate Mellin-tilt (S86 W1c-8); cutoff-INDEPENDENT. Doc §VI.C KZ-too-red prediction CONFIRMED.",
         "citation": "baseline #21 Mode-Independent Occupation Theorem; n_s_framework=0.9561; S57/S73a/S86 Paper 04,09,21"},
        {"row": "epsilon_H=3.0 -> Ratio invariance (intensive)", "s44_status": "PROVEN (theorem)",
         "verdict_class": "STALE-by-precision", "current_state": "eps_H invariance theorem holds; the tilt-relevant slow-roll bound is eps_H_W6=0.02163 (S80 dS/dtau at fold). The '3.0' was the Lifshitz-eta route value (different quantity).",
         "citation": "get_constant eps_H_W6=0.02163 (S85 W9-2); S44 W4-3 Paper 04"},
        {"row": "Van Hove singularities -> Phase transition classification", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "12 van Hove trajectories; band topology (VAN-HOVE-TRACK-44).",
         "citation": "S44 W6-8 Paper 27"},
        {"row": "Block-diagonal theorem -> Selection rules (Schur)", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "D_K block-diagonal by Peter-Weyl PERMANENT (S22b wall).",
         "citation": "MEMORY permanent walls #2; S22b Paper 04 rep theory"},
        {"row": "8-temperature GGE -> Non-Fermi liquid", "s44_status": "STRUCTURAL",
         "verdict_class": "CURRENT", "current_state": "8-temperature GGE; non-Fermi-liquid character; Resolvent-Fermi-liquid correspondence (S63).",
         "citation": "framework-cc-oom Resolvent-Fermi-liquid; S44 W6-5 Paper 11,20"},
        {"row": "Negative heat capacities -> Saddle directions in F", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "3/8 negative heat-capacity eigenvalues (MULTI-T-JACOBSON-44).",
         "citation": "S44 W6-5 Paper 04,11"},
        {"row": "Euler deficit = E_cond -> Gibbs-Duhem violation", "s44_status": "OPEN",
         "verdict_class": "CURRENT", "current_state": "Still OPEN; generalized Gibbs-Duhem for GGE remains open (ties to q-theory equilibrium identity).",
         "citation": "S44 W6-5 Paper 05; VI.B caveat"},
        {"row": "Effacement wall (0.002%) -> Off-diagonal LRO invisible", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Effacement wall confirmed; BDG-SA-61 condensate invisible at 1.36e-4; S75 effacement_rebuild.",
         "citation": "search_knowledge BDG-SA-61; S44 W5-4 Paper 11,15"},
        {"row": "K_7 Cooper pairs -> BCS order parameter", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Cooper pairs carry K_7 charge +/-1/2; gap block-diagonal in K_7.",
         "citation": "session-35 connes workshop; S35 Paper 08,15"},
        {"row": "Pomeranchuk f_0=-4.687 -> Fermi surface instability", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "f_0=-4.687<-3, g*N(0)=3.24 PERMANENT; ROBUST at L=5,7 (W3-A). POMERANCHUK-GGE-58 FAIL (GGE has no Fermi surface).",
         "citation": "trace_entity Pomeranchuk; S22c Paper 11"},
        {"row": "B2 flat band -> Infinite-order Van Hove", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "B2 flat band; acoustic B1 dominates by ~37x (flat-bands-squeeze-less).",
         "citation": "MEMORY project insights; S22c Paper 27"},
        {"row": "M_max=1.674 -> Thouless criterion", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "M_max_thouless=1.674 canonical.",
         "citation": "get_constant(M_max_thouless)=1.674; S35 Paper 15"},
        {"row": "L/xi_GL=0.031 -> Ultrasmall grain limit", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Ultrasmall grain; xi_BCS=0.8083468753837275 canonical.",
         "citation": "get_constant(xi_BCS); S38 Paper 17,36"},
        {"row": "E_vac/E_cond=28.8 -> BEC regime of crossover", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "BCS-BEC crossover refined S61 (BEC-61 N-scan: BEC at N=1->BCS-crossover at N=4); E_vac/E_cond=28.8, g*N=2.18.",
         "citation": "search_knowledge BEC-61; atlas-07 #4; S37 Paper 22"},
        {"row": "omega_att=1.430 -> Pair vibration frequency", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Pair vibration frequency unchanged.",
         "citation": "S37 Paper 23"},
        {"row": "Schwinger-instanton duality -> WKB tunneling = pair creation", "s44_status": "PROVEN (1%)",
         "verdict_class": "CURRENT", "current_state": "Schwinger-instanton duality holds at 1%.",
         "citation": "S37 Paper 29"},
        {"row": "Second sound Q=75,989 -> Undamped two-fluid mode", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Undamped second sound; observational horizon computed (OBS-68, l_second_sound=720.9); GGE two-fluid (S67).",
         "citation": "search_knowledge OBS-68/CMB-53; S44 W6-2 Paper 05"},
        {"row": "12 Van Hove trajectories -> Band structure topology", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "12 trajectories; T3/T4/T5 near-crossing at tau=0.19.",
         "citation": "S44 W6-8 Paper 27"},
        {"row": "Gap stability (-1.63%) -> Fully gapped spectrum", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Fully gapped; min|lambda|=0.8197 > Delta_BCS=0.4642 (S93 W2-1 cross-check).",
         "citation": "S44 W5-3 Paper 08"},
        {"row": "BDI class, T^2=+1 -> Altland-Zirnbauer symmetry", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "AZ class BDI, KO-dim=6 PERMANENT; S88 AZ-BDI-DIII-INHERITANCE-CONFIRM.",
         "citation": "MEMORY; S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2; S17c Paper 15"},
        {"row": "g_1/g_2=e^{-2tau} -> Geometric running coupling", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "Geometric running coupling PERMANENT.",
         "citation": "MEMORY PROVEN results; S17a Paper 10"},
        {"row": "CDM T^{0i}=0 -> Pressureless dust / normal fluid", "s44_status": "PROVEN",
         "verdict_class": "CURRENT", "current_state": "CDM by construction T^{0i}=0 algebraic.",
         "citation": "S44 W1-2 Paper 05"},
        {"row": "OCC-SPEC-45 (proposed) -> Landau free energy at phys. state", "s44_status": "UNCOMPUTED",
         "verdict_class": "CONTRADICTED", "current_state": "RAN + FAILED at S45: OCC-SPEC-45 = FAIL, S_occ MONOTONE DECREASING, the '28th equilibrium closure'. Directly CONTRADICTS the §VI.A standing prediction of a non-monotone minimum near tau=0.19. BCS off-diagonal content (effaced 0.002%) too small to overturn Weyl-law monotonicity. The one-body/many-body partition confirms itself.",
         "citation": "gate OCC-SPEC-45 FAIL (session-45-results-workingpaper); atlas-07 #42; S45 Paper 04,15,08"},
    ]

    # §§II-VII prose seed-claims, each with its current value.
    prose_claims = [
        {"claim": "§II.B BCS transition = 3D Ising (Z_2, n=1)", "current_value":
         "PERMANENT (S43 BCS-CLASS-43): nu=0.6301, beta=0.3265, gamma=1.2372, alpha=0.110; z=2.024 (Model A)."},
        {"claim": "§II.B Lifshitz transition Type I at tau~0", "current_value":
         "32-fold degeneracy -> 8.27-fold residual; far above d_uc=3; mean-field exact."},
        {"claim": "§II.B transit completion = sudden quench P_exc=1.000", "current_value":
         "P_exc=1.000 (Landau-Zener); GGE with 8 Richardson-Gaudin integrals; NOT thermal."},
        {"claim": "§II.C dual dimensionality d_int=8 vs d_ext=3", "current_value":
         "Gi=0.25 (S43) / Gi_fluct=0.9401, 0.506 (S53 fabric): fluctuations dominate near T_c for BCS."},
        {"claim": "§III.A successes one-body / failures many-body", "current_value":
         "Partition holds; G_N CONDITIONAL; OCC-SPEC now a CLOSED many-body FAIL that VINDICATES the partition."},
        {"claim": "§III.B spectral action is one-body diagonal functional", "current_value":
         "Confirmed; BDG-SA-61 condensate invisible at 1.36e-4; ODLRO in off-diagonal sector no diagonal trace accesses."},
        {"claim": "§IV DM/DE = O(1) specific heat exponent alpha_eff~0.39", "current_value":
         "alpha_eff~0.39 not an equilibrium exponent; GGE C_GGE open; Leggett-channel gives the actual DM mass anchor."},
        {"claim": "§V/§VI OCC-SPEC the single most important open computation", "current_value":
         "CLOSED: OCC-SPEC-45 FAIL, S_occ monotone decreasing (28th closure). §VI.A non-monotone prediction CONTRADICTED."},
        {"claim": "§VI.C KZ Bogoliubov n_s too red", "current_value":
         "CONFIRMED (KZ gives n_s~-0.7 to 0.44); resolution moved to geometry n_s=1-2 eps_H = 0.9561."},
        {"claim": "§VII.A1 no laboratory", "current_value":
         "PARTIALLY LIFTED: 3He-B inheritance bridge is a real lab falsifier (Lancaster MCT-3 / Helsinki ROTA; S87-W11-C5 PASS)."},
        {"claim": "§VII.A4 BCS-BEC crossover position E_vac/E_cond=28.8 (BEC regime)", "current_value":
         "Refined S61 (BEC-61): N-dependent regime BEC(N=1)->BCS-crossover(N=4); GP formalism appropriate deep in BEC."},
        {"claim": "§VII.A7 CC problem = universality class mismatch", "current_value":
         "REFRAMED by DILUTION-CC: mismatch real, resolution is Volovik tracking vacuum CC_OOM=115.5, not CM-internal."},
    ]

    return {
        "gate_id": GATE_ID,
        "domain": "framework <-> Landau-condensed-matter mapping, S45 -> S93",
        "substrate_framing": "D_K eigenvalues -> spectral moments -> Landau free energy / two-fluid partition -> observable",
        "entity_classes_surveyed": ENTITY_CLASSES_SURVEYED,
        "existing_row_count": len(existing_rows),
        "existing_rows": existing_rows,
        "prose_claim_count": len(prose_claims),
        "prose_claims": prose_claims,
        "canonical_currency_snapshot": {
            "tau_fold": float(tau_fold),
            "Delta_BCS": float(Delta_BCS),
            "E_cond": float(E_cond),
            "Q_Leggett": float(Q_Leggett),
            "omega_L1": float(omega_L1),
            "c_Gold": float(c_Gold),
            "M_max_thouless": float(M_max_thouless),
            "xi_BCS": float(xi_BCS),
            "CC_OOM": float(CC_OOM),
            "n_s_framework": float(n_s_framework),
            "planck_ns": float(planck_ns),
            "alpha_s_cmb_central": float(alpha_s_cmb_central),
            "eps_H_W6": float(eps_H_W6),
            "Omega_DM_obs": float(Omega_DM_obs),
            "Omega_DE_obs": float(Omega_DE_obs),
            "cocycle_norm_phi67": float(cocycle_norm_phi67),
            "cocycle_norm_phi88": float(cocycle_norm_phi88),
            "cocycle_ratio_phi67_phi88": float(cocycle_norm_phi67) / float(cocycle_norm_phi88),
            "m_L1_NOTE": "0.070 M_KK is # (local), NOT a canonical constant (S80 WP)",
        },
    }


def build_gap_analysis() -> dict:
    """The NEW-since-S44 correspondence set (the EXPANSION engine) + the existing-row
    refresh set. Each new-correspondence row carries {correspondence, cm_concept,
    session_gate_citation, landau_paper, doc_placement, proposed_status_tag}."""
    new_correspondences = [
        {"correspondence": "Leggett-channel dark matter (Mass_LeggettDM/Delta_BCS=11.97; Omega_DM h^2=0.1200 Leggett-only)",
         "cm_concept": "Leggett inter-band collective mode as DM mass anchor; Type-F single-summand-projection trace",
         "session_gate_citation": "S70 LEGGETT-MOMENT-70 (atlas-10 #23; Door-S70; trace_entity LEGGETT-MOMENT)",
         "landau_paper": "05, 11, 20; Leggett 1975", "doc_placement": "new §I rows + new prose §VIII (Leggett DM)",
         "proposed_status_tag": "PROVEN-CONDITIONAL"},
        {"correspondence": "Leggett mode = undamped collective mode (Q_Leggett=670,000)",
         "cm_concept": "Two-fluid undamped collective oscillation (second-sound class)",
         "session_gate_citation": "S70 LEGGETT-MOMENT; atlas-04 P2; get_constant Q_Leggett=670000",
         "landau_paper": "05", "doc_placement": "new §I row + §VIII", "proposed_status_tag": "PROVEN-CONDITIONAL"},
        {"correspondence": "Leggett Goldstone mass (m_L1=0.070 M_KK; omega_L1=0.138; c_Gold=0.915)",
         "cm_concept": "Phason/Goldstone gap from U(1)_7 breaking; inter-band B2-B3 phase excitation",
         "session_gate_citation": "S48 MASS-48, S66 goldstone_gap, S80 (session-80 WP)",
         "landau_paper": "08, 11", "doc_placement": "new §I row + §VIII", "proposed_status_tag": "PROVEN"},
        {"correspondence": "Volovik free-energy partition (F_Josephson=-336.6 M_KK -> 95.9% vacuum; F_BCS+F_BA+F_Leggett=14.411 -> matter)",
         "cm_concept": "Condensation-energy partition between vacuum and quasiparticle sectors",
         "session_gate_citation": "S58/S62 PARTITION-58/62 (baseline #27; trace_entity Volovik partition)",
         "landau_paper": "04, 05; Volovik q-theory", "doc_placement": "new §I row + new prose §IX (Volovik partition)",
         "proposed_status_tag": "PROVEN"},
        {"correspondence": "GGE two-fluid / generalized Landau-Khalatnikov",
         "cm_concept": "Two-fluid model with GGE normal component; LK relaxation generalized to non-equilibrium GGE",
         "session_gate_citation": "S67 GGE-TWO-FLUID-67 / FLUID-67",
         "landau_paper": "05, 09, 20", "doc_placement": "new §I row + §X (GGE permanence)", "proposed_status_tag": "STRUCTURAL"},
        {"correspondence": "Superfluid-stiffness anisotropy tensor (rho_s(C^2)=7.96, rho_s(u(1))=0.33; 24x anisotropic)",
         "cm_concept": "GL phase stiffness tensor on the Lie algebra; curvature-stiffness anti-correlation r=-0.906",
         "session_gate_citation": "S47 TENSOR-47 / RESPONSE-47 (atlas-07 NEW S47)",
         "landau_paper": "08", "doc_placement": "new §I row + new prose §XI (BKT / stiffness)", "proposed_status_tag": "STRUCTURAL"},
        {"correspondence": "BKT on the finite graph (T_BKT=(pi/2)*rho_s_eff; sector-resolved)",
         "cm_concept": "Berezinskii-Kosterlitz-Thouless transition; vortex-unbinding on discrete fabric",
         "session_gate_citation": "S56 TEST-56, S58 KUBO-58, S74 RESOLVED-74",
         "landau_paper": "21 (KZ-adjacent); BKT", "doc_placement": "new §I row + §XI + §II.B phase-table row", "proposed_status_tag": "PROVEN"},
        {"correspondence": "GGE permanence = Richardson-Gaudin integrability (Ordered Veil; <r>~0.33 Poisson, Brody beta~0; t_Th from Cayley-graph Laplacian)",
         "cm_concept": "Non-thermalizing integrable system; absence of level repulsion. RETRACTED at FULL-isometry (S39), PERMANENT in BCS sector (S62).",
         "session_gate_citation": "S38/S39/S53/S60/S61/S62 (atlas-04 T3 retraction; Door-S62-Meissner; trace_entity GGE permanence)",
         "landau_paper": "16, 20", "doc_placement": "new §I row + new prose §X (Ordered Veil) + §II.B integrable-fixed-point row", "proposed_status_tag": "STRUCTURAL"},
        {"correspondence": "3He-B inheritance morphism + 4-gate falsifier (cocycle ratio phi67/phi88=7.324992; Caroli-Matricon vortex ladder)",
         "cm_concept": "BDI 3He-B -> laboratory child via inheritance morphism chi:C+H+M_3(C)->M_2(C); momentum-space topology",
         "session_gate_citation": "S86/S87/S90 (Door-S86-3HeB, Window-11; S87-W11-C5-LAB-FALSIFIER PASS; S90 watchlist 50/50)",
         "landau_paper": "15, 19; Volovik QFL", "doc_placement": "new §I row + new prose §XII (3He-B cross-pillar bridge, 5-anatomy + 3-level)", "proposed_status_tag": "PROVEN"},
        {"correspondence": "DILUTION-CC reframes universality-class-mismatch (114->0.01 OOM via tracking vacuum; CC_OOM=115.5)",
         "cm_concept": "Why zeroth/second moments differ; resolution NOT a CM-internal phenomenon",
         "session_gate_citation": "S66 DILUTION-CC-66 PASS (get_constant CC_OOM=115.5)",
         "landau_paper": "04 (universality); Volovik 25/35", "doc_placement": "new §I row + §VII.A7 refresh", "proposed_status_tag": "SUPERSEDED-context"},
        {"correspondence": "Kohn-anomaly modulus softening / Ginzburg number on fabric (Gi~0.5-0.94; backaction-drag reclass)",
         "cm_concept": "Phonon softening at a deformation parameter; fluctuation criterion",
         "session_gate_citation": "S53 FABRIC-53 (s53_ginzburg_fabric; baptista-volovik reclass)",
         "landau_paper": "04 (Ginzburg), 11", "doc_placement": "new §I row + §II.C deepen", "proposed_status_tag": "STRUCTURAL"},
        {"correspondence": "n_s geometric tilt (n_s=1-2*eps_H; Mode-Independent Occupation Theorem)",
         "cm_concept": "Tilt from spectral geometry, NOT quench dynamics (REPLACES the KZ row)",
         "session_gate_citation": "S57 (baseline #21), S73a COMPOUND-NS-73a, S86 W1c-8",
         "landau_paper": "04, 09, 21", "doc_placement": "new §I row + §VI.C rewrite", "proposed_status_tag": "SUPERSEDED-by-mechanism-shift"},
        {"correspondence": "alpha_s = n_s^2 - 1 (substrate-distance Mellin running -0.08587279; pivot running ~0)",
         "cm_concept": "Running coupling as Mellin-residue; scale-and-channel-tagged (two scale-separated observables)",
         "session_gate_citation": "S50/S84/S86/S89 (canonical_classes alpha_s x2; S92 AH-TR-1 scale-channel)",
         "landau_paper": "framework-specific; Landau-pole heritage", "doc_placement": "new §I row + §IV note", "proposed_status_tag": "PROVEN"},
        {"correspondence": "Resolvent-Fermi-liquid correspondence",
         "cm_concept": "Resolvent of D_K <-> Fermi-liquid quasiparticle propagator",
         "session_gate_citation": "S63 VdD-Vol workshop (framework-cc-oom closed mechanism)",
         "landau_paper": "11", "doc_placement": "new §I row + §III.B deepen", "proposed_status_tag": "STRUCTURAL"},
        {"correspondence": "Dedicated Landau-collab workshop corpus (S20b, S22c, S28, S49, S54, S57, S58, S59, S71, S73a, S75; + DIA-W2 Casimir S91)",
         "cm_concept": "(meta: where the new framework<->Landau-CM physics was derived)",
         "session_gate_citation": "S20b/S22c/S28/S49/S54/S57/S58/S59/S71 landau-collab workshops; reviews nazarewicz/einstein/qa/tesla",
         "landau_paper": "multiple", "doc_placement": "Appendix B gate cross-reference extension + Appendix C", "proposed_status_tag": "CURRENT"},
        # Further correspondences the sweep surfaced beyond the 14-row table-B seed:
        {"correspondence": "Pomeranchuk-on-GGE (POMERANCHUK-GGE-58 FAIL: GGE has no Fermi surface to destabilize)",
         "cm_concept": "Pomeranchuk instability evaluated on the post-transit GGE (no quasiparticle Fermi surface)",
         "session_gate_citation": "S58 POMERANCHUK-GGE-58 FAIL (trace_entity Pomeranchuk)",
         "landau_paper": "11", "doc_placement": "§I Pomeranchuk row note + §III refresh", "proposed_status_tag": "CURRENT"},
        {"correspondence": "Mott-transition CC inaccessibility (E_J/E_C=194, 571x above critical ratio)",
         "cm_concept": "Mott insulator transition on the Josephson array; the fabric sits deep in the superfluid (Josephson-dominated) regime",
         "session_gate_citation": "S65 (constraint-mega-matrix Mott transition CC; s65_vortex_cc; s74_mott_*)",
         "landau_paper": "08 (GL), 22 (BEC)", "doc_placement": "new §I row + §II.C note", "proposed_status_tag": "PROVEN"},
        {"correspondence": "Second-sound observational horizon (l_second_sound=720.9 = pi*c_fabric/c_Gold)",
         "cm_concept": "Two-sound CMB hierarchy: geometric horizon (full sky) vs pair-acoustic horizon",
         "session_gate_citation": "S53 CMB-53, S68 OBS-68/FLUID-67",
         "landau_paper": "05, 09", "doc_placement": "§I second-sound row refresh + §VIII note", "proposed_status_tag": "CURRENT"},
        {"correspondence": "Multi-instanton effective-mass / instanton liquid (V_eff monotonic; S76-C4-INST-LIQUID FAIL)",
         "cm_concept": "Dilute-instanton-gas -> instanton-liquid crossover; effective mass of the modulus",
         "session_gate_citation": "S75 multi_instanton, S76 instanton_liquid (S76-C4-INST-LIQUID FAIL)",
         "landau_paper": "29; 23,24,25", "doc_placement": "§I instanton-gas row note", "proposed_status_tag": "CURRENT"},
        {"correspondence": "GL kappa = lambda/xi classification (Paasch-potential Landau collab)",
         "cm_concept": "Type-I vs Type-II superconductor classification via the GL parameter kappa = lambda/xi_BCS",
         "session_gate_citation": "framework-paasch-potential-landau-collab; S38 L/xi_GL=0.031",
         "landau_paper": "08, 17, 36", "doc_placement": "§I L/xi row refresh + Appendix A kappa eqn", "proposed_status_tag": "CURRENT"},
    ]

    existing_row_refresh = [
        {"row": r["row"], "s44_status": r["s44_status"], "verdict_class": r["verdict_class"],
         "current_state": r["current_state"], "citation": r["citation"]}
        for r in build_state_of_domain_map()["existing_rows"]
        if r["verdict_class"] != "CURRENT"
    ]

    return {
        "gate_id": GATE_ID,
        "new_correspondence_count": len(new_correspondences),
        "table_b_seed_floor": 14,
        "new_correspondences": new_correspondences,
        "existing_row_refresh_count": len(existing_row_refresh),
        "existing_row_refresh": existing_row_refresh,
        "doc_section_plan": {
            "refresh": "all ~33 §I rows -> current fate; §§II-VII deepened",
            "new_table_rows": ">= 14 (the new_correspondences set)",
            "new_prose_sections": ["VIII Leggett-channel DM", "IX Volovik free-energy partition",
                                   "X GGE permanence / Ordered Veil (Richardson-Gaudin)",
                                   "XI BKT / superfluid-stiffness", "XII 3He-B inheritance cross-pillar bridge"],
            "occ_spec": "§V/§VI rewritten to closed FAIL verdict (S_occ monotone, 28th closure)",
            "appendices": "A new key eqns (Leggett dispersion, Volovik partition, GGE Gibbs-Duhem, GL kappa); B gate cross-ref extension; C extended",
        },
    }


def main() -> int:
    document_pre_sha = sha256_of(DOCUMENT_PATH)  # (local)
    canonical_sha = sha256_of(CANONICAL_CONSTANTS_PATH)  # (local)
    knowledge_db_sha = sha256_of(KNOWLEDGE_DB_PATH)  # (local)

    state_map = build_state_of_domain_map()  # (local)
    gap = build_gap_analysis()  # (local)

    # Serialize the two REQUIRED artifacts (deterministic; sort_keys for SHA stability).
    state_map_text = json.dumps(state_map, indent=2, sort_keys=True)  # (local)
    gap_text = json.dumps(gap, indent=2, sort_keys=True)  # (local)
    OUT_STATE_MAP.write_text(state_map_text, encoding="utf-8")
    OUT_GAP.write_text(gap_text, encoding="utf-8")

    manifest_text = json.dumps(KB_QUERY_MANIFEST, separators=(",", ":"), sort_keys=True)  # (local)

    # ---- Coverage-by-enumeration verdict logic (plan §W7-1 strict_PASS_boundary) ----
    n_queries = len(KB_QUERY_MANIFEST)  # (local)
    n_entity_classes_in_manifest = len({row[2] for row in KB_QUERY_MANIFEST})  # (local) distinct tagged classes
    n_existing_rows = state_map["existing_row_count"]  # (local)
    n_prose = state_map["prose_claim_count"]  # (local)
    n_new_corr = gap["new_correspondence_count"]  # (local)
    all_existing_have_citation = all(bool(r.get("citation")) for r in state_map["existing_rows"])  # (local)
    all_new_have_citation = all(bool(r.get("session_gate_citation")) and bool(r.get("doc_placement"))
                                for r in gap["new_correspondences"])  # (local)

    cond_i = all_existing_have_citation and n_existing_rows >= 30  # (local) (i) every existing row fated + cited
    cond_ii = n_prose >= 10  # (local) (ii) §§II-VII prose seed-claims valued
    cond_iii = (n_new_corr >= 14) and all_new_have_citation  # (local) (iii) new-corr set >= table-B seed, all cited
    cond_iv = (n_queries >= 25) and (n_entity_classes_in_manifest >= 5)  # (local) (iv) >=25 queries, >=5 classes

    passed = cond_i and cond_ii and cond_iii and cond_iv  # (local)
    verdict = "PASS" if passed else "FAIL"  # (local)

    value = (f"domain_survey_complete={passed};queries={n_queries};entity_classes_tagged={n_entity_classes_in_manifest};"
             f"entity_classes_surveyed={len(ENTITY_CLASSES_SURVEYED)};existing_rows_fated={n_existing_rows};"
             f"prose_claims={n_prose};new_correspondences={n_new_corr}(floor=14);"
             f"cond_i={cond_i};cond_ii={cond_ii};cond_iii={cond_iii};cond_iv={cond_iv}")  # (local)

    # ---- dual SHA per plan §W7-1 audit_discriminators ----
    audit_inputs = {
        "document_pre": document_pre_sha,
        "state_of_domain_map": sha256_of_text(state_map_text),
        "gap_analysis": sha256_of_text(gap_text),
        "canonical_constants_snapshot": canonical_sha,
        "kb_query_manifest": sha256_of_text(manifest_text),
        "knowledge_db": knowledge_db_sha,
    }  # (local)
    content_inputs = {
        "state_of_domain_map": sha256_of_text(state_map_text),
        "gap_analysis": sha256_of_text(gap_text),
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(audit_inputs, content_inputs)  # (local)

    # ---- append verdict (canonical line + dual-SHA companion row; no [SIGN] 3-tuple) ----
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); AGGREGATE-DOMAIN-SURVEY; "
        f"state_of_domain_map + gap_analysis JSON; substrate-IS direction\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)

    # ---- stdout (first 20 lines log input SHAs per gate-verdicts.md §2) ----
    print("=" * 78)
    print(f"{GATE_ID} — AGGREGATE-DOMAIN-SURVEY")
    print("=" * 78)
    print(f"INPUT document_pre   sha256 = {document_pre_sha}")
    print(f"INPUT canonical      sha256 = {canonical_sha}")
    print(f"INPUT knowledge.db   sha256 = {knowledge_db_sha}")
    print(f"state_of_domain_map  sha256 = {audit_inputs['state_of_domain_map']}")
    print(f"gap_analysis         sha256 = {audit_inputs['gap_analysis']}")
    print(f"kb_query_manifest    sha256 = {audit_inputs['kb_query_manifest']}")
    print("-" * 78)
    print(f"KB queries            = {n_queries}  (>= 25 required)")
    print(f"entity classes tagged = {n_entity_classes_in_manifest}  (>= 5 required)")
    print(f"existing §I rows fated = {n_existing_rows}")
    print(f"§§II-VII prose claims  = {n_prose}")
    print(f"new correspondences    = {n_new_corr}  (>= 14 table-B seed)")
    print(f"cond_i/ii/iii/iv       = {cond_i}/{cond_ii}/{cond_iii}/{cond_iv}")
    print("-" * 78)
    print(f"VERDICT = {verdict}")
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    print(f"artifacts: {OUT_STATE_MAP.name}, {OUT_GAP.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
