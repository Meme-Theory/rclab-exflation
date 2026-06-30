#!/usr/bin/env python3
"""
S104 W5-1 S104-AREA-MODULAR-GENERATOR-SPEC — area-operator <-> modular-generator BRIDGE SPEC
============================================================================================

Gate: S104-AREA-MODULAR-GENERATOR-SPEC ([VERIFY])
  SPEC-ONLY gate. Decides whether the substrate's spectral-monotonicity generator
  G_tau = d/dtau on the tau-indexed D_K(tau) spectral-action-moment family is NAMEABLE
  as a candidate horizon modular (Connes-cocycle) flow generator Ad(Delta_omega^{it})
  on a NAMED emergent-horizon subalgebra A_hor with a NAMED GGE state omega.

  This script computes NO operator-norm agreement (that is the S105 compute). It records
  the named ingredients (as strings), the 3-conjunct spec-completeness booleans, and a
  one-panel schematic of the proposed identity G_tau <-> Delta^{it}.

Pre-registered SPEC-completeness predicate (3-conjunct boolean; NOT a numerical threshold):
  SPEC_complete := construction_named AND ingredients_pinned AND s105_spec_emitted
    construction_named  := (A_hor named as an algebra) AND (omega named) AND
                           (G_tau named as an explicit operator on the moment family)
    ingredients_pinned  := every symbol in G_tau ?= Ad(Delta_omega^{it})|_{A_hor} resolves
                           to a substrate object with NO free/unnamed factor
    s105_spec_emitted   := a 4-field (what/inputs/gate/effort) S105 compute spec is written
  PASS iff all three True; FAIL iff construction unnameable; INFO iff stateable but
  >= 1 named ingredient unpinned (pre-registered intermediate: A_hor schematic OR
  omega|_{A_hor} not yet well-defined).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (feeds audit_sha256 only)
  - downloads/research-sweep-s103/holography-bh-information/ (Chandrasekaran-Flanagan
    2601.07915 primary; Kudler-Flam 2309.15897; Geng-Jiang-Xu 2506.12127; Liu 2510.07017)
    -- read-only source, content-pinned at runtime
  - computations/session-97/s97_ds_area_law_monotonicity.npz (composed-with INFO data:
    a2_cancels, dS/d(a0a2) sign; read for the named-ingredient cross-check, NOT recomputed)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<spec-completeness record>, scheme=MODULAR-CONNES-COCYCLE-SPEC,
   convention=SUBSTRATE-IS-HORIZON-SUBALGEBRA-NAMING, L_max=10)

Classification: GEOMETRIC. The arrow flows FROM the substrate TOWARD emergent gravity:
  D_K(tau) eigenvalues -> spectral-action moments {a_0,a_2,a_4} -> the dS/dtau monotonicity
  generator G_tau -> (candidate) emergent-horizon modular flow -> area law. A_hor is a
  sub-structure of the fabric algebra A_K, NOT a surface embedded IN a pre-existing spacetime.

METHODOLOGY
-----------
Read the four holography PDFs (on-disk INDEX-verified content). The Chandrasekaran-Flanagan
2601.07915 result supplies the laboratory-IN side: the area operator IS the bulk implementation
of the Connes cocycle flow [Domega : Domega_0]_t on a Type-II_oo horizon subalgebra (a crossed
product by the half-sided modular automorphism group), with vN entropy = generalized entropy.
The Kudler-Flam 2309.15897 structure theorem gives the Type-II_oo-horizon x Type-I_oo-asymptotic
factorization needing only a STATIONARY (not KMS) state; Geng-Jiang-Xu 2506.12127 give the
Goldstone-dressed observer as the Type-I -> Type-II promotion mechanism.

Substrate side (verified via knowledge MCP, NOT recomputed):
  - S97-VN-TYPE-INDUCTIVE-LIMIT PASS: the substrate triple is hyperfinite Type-I_oo.
  - S97-DS-AREA-LAW-MONOTONICITY INFO: a2_cancels=True (spread 2.19e-16), dS/d(a0a2) sign=-1,
    p_exponent=-1 (the S63 area_SA = a_2_fold/N_edges exponent), reproduces=True,
    independent=False (the WEAK "both routes give S=A/4G" form -- the DUPLICATE this gate
    must NOT re-emit). This gate goes further: name the ALGEBRAIC operator identity.
  - sigma_1^omega = Ad(Delta_omega^i) EXISTS (tesla-connes-addendum A.9), with thermal-time
    sigma_t^{omega}(a) = e^{iHt} a e^{-iHt} (A3.1) and the GGE product flow
    sigma_t^{GGE} = sigma_t^{(1)} * ... * sigma_t^{(8)} (eq 26, S64). NEVER connected to a
    horizon area operator before (search returned ZERO horizon-algebra hits).

Decisive structural fact (Sage-verified, Connes-Takesaki): a crossed product
A_K rtimes_{sigma^omega} R of the Type-I_oo substrate by its modular flow is Type-II_oo,
matching paper-01. A bare finite SUMMAND M_n(C) of A_K = C (+) H (+) M_3(C) is Type-I_n --
it CANNOT be the Type-II_oo horizon algebra. Therefore A_hor is NAMEABLE as the emergent
crossed product, NOT as a sub-summand/projection of the bare A_K. The construction is named;
the UNPINNED ingredient is the GGE-state restriction omega|_{A_hor} as a faithful normal
stationary state (INTEG-39 contests full stationarity; the Goldstone-dressing structure-theorem
ingredient is named only schematically) -> the pre-registered INFO condition.

DISCIPLINE
----------
- from canonical_constants import *
- every intermediate tagged # (local)
- CPU only (no linear algebra); OMP capped at 8 BEFORE numpy import
- SHA-256 of all input files logged in first 20 lines of stdout
- dual-SHA (audit + content) emitted (S84+)
- verdict emitted via emit_verdict MCP tool (the script PRINTS the payload; the agent calls it)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import; no GPU / no linear algebra)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S104"                                                   # (local)
GATE_ID = "S104-AREA-MODULAR-GENERATOR-SPEC"                       # (local)
SCHEME = "MODULAR-CONNES-COCYCLE-SPEC"                             # (local)
CONVENTION = "SUBSTRATE-IS-HORIZON-SUBALGEBRA-NAMING"             # (local)
L_MAX = 10                                                        # (local)

HOLO_DIR = (PROJECT_ROOT / "downloads" / "research-sweep-s103"
            / "holography-bh-information")                        # (local)
S97_NPZ = (COMPUTATIONS_DIR / "session-97"
           / "s97_ds_area_law_monotonicity.npz")                 # (local)

OUT_NPZ = SESSION_DIR / "s104_area_modular_generator_spec.npz"
OUT_PNG = SESSION_DIR / "s104_area_modular_generator_spec.png"

# Input files for the dual-SHA closure. The holography PDFs are large; we pin the
# curated on-disk INDEX (00-INDEX.md), which is the verified-content reading of the
# four source PDFs, plus the four PDF byte-hashes themselves for provenance.
HOLO_INDEX = HOLO_DIR / "00-INDEX.md"                             # (local)
HOLO_PDFS = [                                                     # (local)
    HOLO_DIR / "01_Chandrasekaran-Flanagan_Subregion-Algebras-Classical-Quantum-Gravity.pdf",
    HOLO_DIR / "07_Kudler-Flam_Generalized-BH-Entropy-is-vN-Entropy.pdf",
    HOLO_DIR / "08_Geng_Algebras-Entanglement-Islands-Observers.pdf",
    HOLO_DIR / "03_Liu_Lectures-vN-Algebras-Emergence-Spacetime.pdf",
]

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    HOLO_INDEX,
    S97_NPZ,
] + HOLO_PDFS


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Spec construction (NO operator-norm agreement; that is S105)
# ---------------------------------------------------------------------------

def load_s97_crosscheck() -> dict:
    """Read the composed-with S97 area-law INFO data for the named-ingredient
    cross-check. We do NOT recompute it -- we read the pinned fields that the
    spec names (a2_cancels, dS/d(a0a2) sign, the area-per-edge exponent p, and
    the entropy-value reproduction that is the DUPLICATE this gate must exceed).
    """
    cc: dict = {}  # (local)
    try:
        d = np.load(S97_NPZ, allow_pickle=True)  # (local)
        cc["composite"] = str(d["composite"])
        cc["a2_cancels"] = bool(d["a2_cancels"])
        cc["S_fixed_r_spread"] = float(d["S_fixed_r_spread"])
        cc["dS_dr_sign"] = float(d["dS_dr_sign"])
        cc["p_exponent"] = float(d["p_exponent"])
        cc["reproduces"] = bool(d["reproduces"])
        cc["independent"] = bool(d["independent"])
        cc["ratio_a0_a2"] = float(d["ratio_a0_a2"])
        cc["a2_fold"] = float(d["a2_fold"])
        cc["a0_fold"] = float(d["a0_fold"])
        cc["S_dS_fold"] = float(d["S_dS_fold"])
    except (OSError, KeyError) as exc:
        cc["error"] = f"S97 npz read failed: {exc!r}"
    return cc


def build_spec(cc: dict) -> dict:
    """Construct the spec record: named ingredients (strings) + 3-conjunct booleans.

    Substitution chain (plan §W5-1), with the named substrate objects substituted:
      Step 1: G_tau := d/dtau on {a_0(tau), a_2(tau), a_4(tau)} of D_K(tau); the dS/dtau
              gradient driving EM.3. [SUPPLIED -- Element 1]
      Step 2: Delta_omega^{it} := modular automorphism group of the GGE state omega
              restricted to A_hor; sigma_t^omega = Ad(Delta_omega^{it}). [named]
      Step 3: A_hor := emergent crossed product A_K rtimes_{sigma^omega} R (Type-II_oo by
              Connes-Takesaki), NOT a sub-summand of the bare A_K (which is Type-I_oo, S97;
              a finite summand M_n(C) is Type-I_n and CANNOT be the Type-II_oo horizon).
      Step 4: identity to make explicit: G_tau ?= Ad(Delta_omega^{it})|_{A_hor}, with the
              area operator A-hat := the a_2-channel spectral moment (S63: area_SA =
              a_2_fold / N_edges, exponent p=-1) ?= the Connes cocycle [Domega:Domega_0]_t.
      Step 5: PASS asserts ONLY that every symbol resolves to a named substrate object AND
              an S105 operator-agreement compute spec is written; it does NOT assert numerical
              agreement. INFO if >= 1 ingredient (A_hor schematic OR omega|_{A_hor}) unpinned.
    """
    # ----- Named ingredients (Element-by-element) -----
    named = {}  # (local)

    named["G_tau"] = (
        "G_tau = d/dtau on the tau-indexed spectral-action-moment family "
        "{a_0(tau), a_2(tau), a_4(tau)} of D_K(tau); the dS/dtau monotonicity gradient "
        "driving EM.3 (substrate spectral monotonicity -> BCS coherence suppression -> "
        "vacuum-energy reduction -> area theorem). S97: dS/d(a0/a2) sign=-1, "
        "p_exponent=-1 (the S63 area_SA = a_2_fold/N_edges exponent)."
    )

    named["omega"] = (
        "omega = the GGE relic state (8 Richardson-Gaudin conserved quantities, "
        "S_GGE=3.542 bits; sigma_t^{GGE} = sigma_t^{(1)} * ... * sigma_t^{(8)}, eq 26 S64), "
        "restricted to A_hor. The modular automorphism is sigma_t^omega = Ad(Delta_omega^{it}) "
        "(tesla-connes-addendum A.9, A3.1)."
    )

    named["A_hor"] = (
        "A_hor = the EMERGENT crossed product A_K rtimes_{sigma^omega} R "
        "(Type-II_oo by Connes-Takesaki), NOT a sub-summand / minimal-central-projection of "
        "the bare A_K = C (+) H (+) M_3(C). Structural reason: A_K is hyperfinite Type-I_oo "
        "(S97-VN-TYPE PASS); a finite summand M_n(C) is Type-I_n and CANNOT be the Type-II_oo "
        "horizon algebra of Chandrasekaran-Flanagan 2601.07915. The Type-I -> Type-II promotion "
        "is the Geng-Jiang-Xu 2506.12127 Goldstone-dressing of the transit's broken symmetry; "
        "the trace is the Kudler-Flam 2309.15897 stationary-state (NON-KMS) structure-theorem trace."
    )

    named["A_hat"] = (
        "A-hat (area operator) = the a_2-channel spectral moment (Einstein-Hilbert / 2nd "
        "Seeley-DeWitt). S63 substrate identity: area_SA = a_2_fold / N_edges (a_2_fold="
        f"{cc.get('a2_fold', float('nan')):.6f}); A_horizon_FW=71226.26 GeV^-2 (S92). "
        "Paper-01: A-hat IS the bulk implementation of the Connes cocycle flow "
        "[Domega:Domega_0]_t for one-sided observables in excited states."
    )

    named["bridge_object"] = (
        "Bridge map (Element 3, THE OPEN INGREDIENT) = the Connes cocycle / modular flow "
        "[Domega : Domega_0]_t on A_hor. Well-defined IFF omega|_{A_hor} is a faithful normal "
        "state on the emergent crossed product. This is the structural identity the S105 "
        "operator-agreement compute would test: G_tau ?= Ad(Delta_omega^{it})|_{A_hor}."
    )

    # ----- Element-2 OE-form (integration domain + trace + named projector; bare prose FORBIDDEN) -----
    named["element_2_OE_form"] = (
        "Laboratory-IN observable (OE-form): S_gen(cut) = Tr_{A_hor}( -rho_omega log rho_omega ) "
        "with A_hor = A_K rtimes_{sigma^omega} R the Type-II_oo crossed product; trace = the "
        "Kudler-Flam semifinite Type-II trace tau_II; named projector = P_cut (the half-sided "
        "modular-inclusion projector onto the one-sided horizon-cut subalgebra). vN entropy of "
        "the semifinite state = generalized entropy A/4G + S_ext (Chandrasekaran-Flanagan 2601.07915). "
        "Integration domain: the one-parameter nested family {A_hor(cut)} along the horizon "
        "(the GSL nesting), NOT an integral over a spacetime region IN a container."
    )

    # ----- 3-conjunct spec-completeness booleans -----
    # Conjunct A: construction_named
    A_hor_named = True            # (local) named as the emergent crossed product
    omega_named = True            # (local) named as the GGE relic state (restricted)
    G_tau_named = True            # (local) named as d/dtau on the moment family
    construction_named = bool(A_hor_named and omega_named and G_tau_named)  # (local)

    # Conjunct B: ingredients_pinned -- does EVERY symbol resolve with NO free/unnamed factor?
    # G_tau: PINNED (explicit operator on the S97 moment trajectories).
    # A_hat: PINNED (the a_2-channel moment; S63 exponent p=-1; A_horizon_FW canonical).
    # A_hor: NAMED as the crossed product, but the crossed-product algebra's faithful-normal-
    #        STATE structure depends on omega|_{A_hor}.
    # omega|_{A_hor}: NOT PINNED -- the GGE relic's restriction to the emergent crossed product
    #        as a faithful normal STATIONARY state is not yet well-defined. INTEG-39 (S96/S100b)
    #        contests full thermalization-protection (Brody beta=0.633 = 63% GOE; t_therm~6 M_KK^-1;
    #        ORDERED-VEIL-SUBSTRATE-CLOCK FAIL). The Kudler-Flam structure theorem needs a
    #        STATIONARY (not necessarily KMS) state to yield the Type-II_oo trace; the GGE's
    #        stationarity-on-A_hor is the unpinned ingredient.
    G_tau_pinned = True           # (local)
    A_hat_pinned = True           # (local)
    omega_restriction_pinned = False  # (local) THE unpinned ingredient
    A_hor_state_structure_pinned = bool(omega_restriction_pinned)  # (local) inherits the gap
    ingredients_pinned = bool(
        G_tau_pinned and A_hat_pinned and omega_restriction_pinned
        and A_hor_state_structure_pinned
    )  # (local)

    # Conjunct C: s105_spec_emitted -- a 4-field compute spec is written (see WP + below)
    s105_spec_emitted = True      # (local)

    spec_complete = bool(construction_named and ingredients_pinned and s105_spec_emitted)  # (local)

    # ----- Verdict (pre-registered rubric, plan §W5-1) -----
    # PASS  := spec_complete (all three True)
    # FAIL  := NOT construction_named (unnameable -> corridor closed; re-route to GEM-WORKSHOP)
    # INFO  := construction_named AND s105_spec_emitted AND NOT ingredients_pinned
    #          (identity STATEABLE but >= 1 named ingredient unpinned: omega|_{A_hor})
    if spec_complete:
        verdict = "PASS"  # (local)
    elif not construction_named:
        verdict = "FAIL"  # (local)
    else:
        verdict = "INFO"  # (local)

    # ----- The 4-field S105 compute spec (emitted on PASS or INFO) -----
    s105_spec = {  # (local)
        "what": (
            "Operator-agreement test: construct the emergent crossed product "
            "A_hor = A_K rtimes_{sigma^omega} R at L_max=10, restrict the GGE relic state to "
            "A_hor as a faithful normal state omega|_{A_hor}, form the Connes cocycle "
            "[Domega : Domega_0]_t, and verify G_tau = Ad(Delta_omega^{it})|_{A_hor} on the "
            "(0,0)+horizon-sector Peter-Weyl blocks to a pre-registered operator-norm tolerance, "
            "with A-hat = the a_2-channel moment matched to the cocycle generator."
        ),
        "inputs": (
            "S97 a2_tau / a0_tau trajectories (the moment family G_tau acts on); the L_max=10 "
            "D_K Peter-Weyl block decomposition (the (0,0)+horizon-sector blocks); the GGE "
            "occupation distribution {n_k^{GGE}} (8 R-G conserved quantities); the Kudler-Flam "
            "2309.15897 stationary-state structure-theorem construction of the Type-II_oo trace; "
            "the Geng-Jiang-Xu 2506.12127 Goldstone-dressing of the broken-symmetry observer. "
            "PREREQUISITE (the unpinned ingredient this INFO flags): a well-defined faithful "
            "normal STATIONARY omega|_{A_hor} on the crossed product."
        ),
        "gate": (
            "[SIGN]+[VERIFY] operator-agreement gate. PASS iff ||G_tau - Ad(Delta_omega^{it})|"
            "_{A_hor}||_op on the (0,0)+horizon-sector blocks < pre-registered tol (set at S105 "
            "plan-freeze); the area-operator/cocycle-generator sign must match the S97 "
            "dS/d(a0a2) sign=-1 chain. NON-binding outcome (G_tau merely co-monotone with, not "
            "equal to, the modular generator) routes to the GEM-WORKSHOP Q1 adjudication."
        ),
        "effort": (
            "1 gate. Half the cost is constructing omega|_{A_hor} as a faithful normal state "
            "(the unpinned ingredient); the (0,0)+horizon-sector block test is low-sector "
            "(small matrices, CPU-feasible). PRECONDITION: settle omega|_{A_hor} stationarity "
            "(the INFO ingredient) before the operator-agreement compute is dispatchable."
        ),
    }

    # ----- Cross-pillar 5-anatomy + 3-level supplied-vs-missing status -----
    anatomy = {  # (local)
        "element_1_substrate_IS": (
            "SUPPLIED -- G_tau = d/dtau on the moment family of D_K(tau) on (A_K^{<=L}, H_K^{<=L}, "
            "D_K^{<=L}); Level 1 (single-tau-slice) at the operator, lifting to Level 2 "
            "(moduli-deformation) under the tau-flow."
        ),
        "element_2_laboratory_IN": (
            "SUPPLIED (OE-form) -- S_gen(cut) = Tr_{A_hor}(-rho_omega log rho_omega), trace = "
            "Type-II_oo semifinite tau_II, projector P_cut (half-sided modular-inclusion onto the "
            "one-sided horizon cut). [previously PARTIAL; now OE-form explicit]"
        ),
        "element_3_bridge_map": (
            "OPEN INGREDIENT -- the Connes cocycle [Domega:Domega_0]_t. Well-defined iff "
            "omega|_{A_hor} faithful normal. This is the spec-completeness pivot."
        ),
        "element_4_algebraic_envelope": "MISSING (deferred to S105) -- no L^{-alpha} envelope this wave.",
        "element_5_empirical_anchor": "MISSING (deferred to S105) -- numerical (0,0)+horizon-block agreement is the S105 deliverable.",
        "three_level_status": (
            "Level 1 (cohomology-class identity G_tau = Ad(Delta_omega^{it})|_{A_hor}) is the TARGET "
            "the spec STATES; Level 2 (envelope) + Level 3 (anchor) explicitly MISSING. A spec-gate "
            "PASS/INFO does NOT constitute a registry-PASS -- it licenses (PASS) or scopes (INFO) the "
            "S105 compute that would supply Levels 2/3."
        ),
    }

    # ----- DUPLICATE-avoidance witness: this gate is NOT the S97 weak form -----
    duplicate_witness = {  # (local)
        "S97_weak_form": (
            "S97-DS-AREA-LAW-MONOTONICITY INFO: both routes reproduce S=A/4G "
            f"(reproduces={cc.get('reproduces')}, independent={cc.get('independent')}, "
            f"a2_cancels={cc.get('a2_cancels')}). This is the ENTROPY-VALUE coincidence."
        ),
        "this_gate_goes_further": (
            "This gate names the ALGEBRAIC OPERATOR identity G_tau = Ad(Delta_omega^{it})|_{A_hor} "
            "(area op = Connes cocycle on a Type-II_oo crossed product) -- a STRUCTURE not present "
            "in the S97 weak form. NOT a duplicate of the 'both routes give S=A/4G' INFO."
        ),
    }

    return {
        "verdict": verdict,
        "named": named,
        "construction_named": construction_named,
        "ingredients_pinned": ingredients_pinned,
        "s105_spec_emitted": s105_spec_emitted,
        "spec_complete": spec_complete,
        "G_tau_pinned": G_tau_pinned,
        "A_hat_pinned": A_hat_pinned,
        "omega_restriction_pinned": omega_restriction_pinned,
        "A_hor_state_structure_pinned": A_hor_state_structure_pinned,
        "s105_spec": s105_spec,
        "anatomy": anatomy,
        "duplicate_witness": duplicate_witness,
        "s97_crosscheck": cc,
    }


# ---------------------------------------------------------------------------
# Section 6 — Schematic plot (one panel: proposed G_tau <-> Delta^{it} identity)
# ---------------------------------------------------------------------------

def make_schematic(spec: dict) -> None:
    fig, ax = plt.subplots(figsize=(11, 7.5))  # (local)
    ax.axis("off")
    ax.set_title(
        "S104-AREA-MODULAR-GENERATOR-SPEC  —  proposed identity  "
        "G_tau =? Ad(Delta_omega^{it})|_A_hor"
        f"   [verdict: {spec['verdict']}]",
        fontsize=12.5, pad=14,
    )

    # Left column: substrate-IS side (Type-I_oo)
    ax.text(0.02, 0.93, "SUBSTRATE-IS side  (Type-I_oo, S97 PASS)",
            fontsize=11, fontweight="bold", color="#13476b")
    ax.text(0.02, 0.85,
            "D_K(tau) eigenvalues\n"
            "  -> moments {a_0, a_2, a_4}(tau)\n"
            "  -> G_tau = d/dtau   (the dS/dtau gradient, EM.3)\n"
            "  A-hat = a_2-channel moment\n"
            "       (S63: area_SA = a_2 / N_edges, p = -1)",
            fontsize=9.5, va="top", family="monospace",
            bbox=dict(boxstyle="round", fc="#eaf3fb", ec="#13476b"))

    # Right column: laboratory-IN side (Type-II_oo)
    ax.text(0.55, 0.93, "LABORATORY-IN side  (Type-II_oo horizon)",
            fontsize=11, fontweight="bold", color="#6b1313")
    ax.text(0.55, 0.85,
            "Chandrasekaran-Flanagan 2601.07915:\n"
            "  area op A-hat = Connes cocycle [Dw:Dw_0]_t\n"
            "  on A_hor (crossed product, half-sided modular)\n"
            "  S_gen = Tr_A_hor(-rho_w log rho_w) = A/4G + S_ext",
            fontsize=9.5, va="top", family="monospace",
            bbox=dict(boxstyle="round", fc="#fbeaea", ec="#6b1313"))

    # Center bridge arrow + the OPEN ingredient
    ax.annotate("", xy=(0.54, 0.66), xytext=(0.46, 0.66),
                arrowprops=dict(arrowstyle="<->", lw=2.0, color="#444"))
    ax.text(0.50, 0.70, "BRIDGE\n(Element 3)", ha="center", va="bottom",
            fontsize=9, fontweight="bold")

    # The decisive Type bookkeeping (Connes-Takesaki)
    ax.text(0.02, 0.52,
            "DECISIVE TYPE BOOKKEEPING (Connes-Takesaki, Sage-verified):",
            fontsize=10, fontweight="bold", color="#222")
    ax.text(0.02, 0.46,
            "bare summand M_n(C) of A_K   :  Type-I_n   => NOT II_oo\n"
            "A_K (inductive limit)        :  Type-I_oo  (S97 PASS)\n"
            "A_K |X|_sigma^omega R        :  Type-II_oo => MATCHES paper-01\n"
            "=> A_hor = EMERGENT crossed product, NOT a projection of A_K",
            fontsize=9.5, va="top", family="monospace",
            bbox=dict(boxstyle="round", fc="#f3f0e8", ec="#8a7a4a"))

    # 3-conjunct spec-completeness booleans
    cn = spec["construction_named"]   # (local)
    ip = spec["ingredients_pinned"]   # (local)
    se = spec["s105_spec_emitted"]    # (local)
    def mark(b):  # (local)
        return ("YES" if b else "NO")
    ax.text(0.55, 0.52, "SPEC-COMPLETENESS (3-conjunct):",
            fontsize=10, fontweight="bold", color="#222")
    ax.text(0.55, 0.46,
            f"construction_named  = {mark(cn)}\n"
            f"ingredients_pinned  = {mark(ip)}   <-- omega|A_hor UNPINNED\n"
            f"s105_spec_emitted   = {mark(se)}\n"
            f"------------------------------------\n"
            f"SPEC_complete = {mark(spec['spec_complete'])}   =>  {spec['verdict']}",
            fontsize=9.5, va="top", family="monospace",
            bbox=dict(boxstyle="round",
                      fc=("#e7f6e7" if spec["spec_complete"] else "#fdf3e0"),
                      ec="#888"))

    # The unpinned-ingredient call-out (the INFO reason)
    ax.text(0.02, 0.20,
            "UNPINNED INGREDIENT (the INFO reason):",
            fontsize=10, fontweight="bold", color="#8a4a13")
    ax.text(0.02, 0.155,
            "omega|_A_hor = GGE relic restricted to the crossed product, as a FAITHFUL\n"
            "NORMAL STATIONARY state. Kudler-Flam structure theorem needs STATIONARY (non-KMS);\n"
            "INTEG-39 contests full stationarity (Brody beta=0.633=63% GOE; t_therm ~ 6 M_KK^-1).\n"
            "=> identity STATEABLE, one named ingredient UNPINNED => INFO; S105 prerequisite.",
            fontsize=9, va="top",
            bbox=dict(boxstyle="round", fc="#fbf1e3", ec="#8a4a13"))

    # Footer: NOT the S97 weak-form duplicate
    ax.text(0.02, 0.02,
            "NOT a duplicate of S97-DS-AREA-LAW (entropy-value coincidence, independent=False): "
            "this names the ALGEBRAIC operator identity area-op = Connes-cocycle on Type-II_oo.",
            fontsize=8.5, style="italic", color="#555")

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)
    print(f"  schematic written: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 1. Read the composed-with S97 INFO data (cross-check, NOT recomputed)
    cc = load_s97_crosscheck()
    print("=== S97 composed-with cross-check (read, NOT recomputed) ===")
    for k in ("composite", "a2_cancels", "dS_dr_sign", "p_exponent",
              "reproduces", "independent", "ratio_a0_a2", "a2_fold"):
        print(f"  {k} = {cc.get(k)}")
    print()

    # 2. Build the spec (NO operator-norm agreement -- that is S105)
    spec = build_spec(cc)
    verdict = spec["verdict"]  # (local)

    print("=== Named ingredients ===")
    for k, v in spec["named"].items():
        print(f"  [{k}]")
        print(f"    {v}")
    print()
    print("=== 3-conjunct spec-completeness ===")
    print(f"  construction_named = {spec['construction_named']}")
    print(f"  ingredients_pinned = {spec['ingredients_pinned']}  "
          f"(omega|A_hor pinned = {spec['omega_restriction_pinned']})")
    print(f"  s105_spec_emitted  = {spec['s105_spec_emitted']}")
    print(f"  SPEC_complete      = {spec['spec_complete']}  =>  verdict {verdict}")
    print()

    # 3. Schematic
    make_schematic(spec)

    # 4. Persist the spec record (.npz) -- named ingredients as strings + booleans
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        # named ingredients (strings)
        named_G_tau=spec["named"]["G_tau"],
        named_omega=spec["named"]["omega"],
        named_A_hor=spec["named"]["A_hor"],
        named_A_hat=spec["named"]["A_hat"],
        named_bridge_object=spec["named"]["bridge_object"],
        named_element_2_OE_form=spec["named"]["element_2_OE_form"],
        # 3-conjunct booleans
        construction_named=spec["construction_named"],
        ingredients_pinned=spec["ingredients_pinned"],
        s105_spec_emitted=spec["s105_spec_emitted"],
        spec_complete=spec["spec_complete"],
        G_tau_pinned=spec["G_tau_pinned"],
        A_hat_pinned=spec["A_hat_pinned"],
        omega_restriction_pinned=spec["omega_restriction_pinned"],
        A_hor_state_structure_pinned=spec["A_hor_state_structure_pinned"],
        # S105 spec (4-field) as JSON string
        s105_spec_json=json.dumps(spec["s105_spec"], sort_keys=True),
        # anatomy + duplicate witness as JSON strings
        anatomy_json=json.dumps(spec["anatomy"], sort_keys=True),
        duplicate_witness_json=json.dumps(spec["duplicate_witness"], sort_keys=True),
        # S97 cross-check
        s97_crosscheck_json=json.dumps(spec["s97_crosscheck"], sort_keys=True),
        # dual-SHA for provenance
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  spec record written: {OUT_NPZ.name}")
    print()

    # 5. 4-tuple + emit_verdict payload
    value = (
        f"verdict={verdict};construction_named={spec['construction_named']};"
        f"ingredients_pinned={spec['ingredients_pinned']}_UNPINNED=omega|A_hor;"
        f"s105_spec_emitted={spec['s105_spec_emitted']};"
        f"A_hor=A_K_rtimes_sigma^omega_R_TypeII_oo_NOT_summand;"
        f"A_hat=a_2-channel_moment_p=-1;bridge=Connes_cocycle_[Domega:Domega0]_t;"
        f"NOT_S97_weak_form_independent=False"
    )  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    companion = (
        "SPEC-gate INFO: identity G_tau=Ad(Delta_omega^{it})|_{A_hor} STATEABLE; "
        "A_hor=crossed product (Type-II_oo, Connes-Takesaki) NAMED; omega|_{A_hor} faithful-normal-"
        "stationary state UNPINNED (the S105 prerequisite). NOT the S97 weak entropy-value form."
    )  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=companion)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
