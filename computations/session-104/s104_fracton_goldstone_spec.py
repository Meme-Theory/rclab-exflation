#!/usr/bin/env python3
"""
S104 W5-3 — S104-FRACTON-GOLDSTONE-SPEC (fracton higher-moment-charge spec)
==========================================================================

Gate: S104-FRACTON-GOLDSTONE-SPEC ([VERIFY])
  SPEC-ONLY gate. NO Ward identity is numerically closed this wave (that is the
  S105 compute the spec would license). The deliverable is the SPEC, not the bridge.

Question (the gem, Argurio 2107.03073 applied to the Leggett-channel DM mode):
  Is the substrate's non-annihilating, non-translating Leggett-channel DM coherence
  mode (inter-band phase Goldstone of the B2-B3 sector; LEGGETT-MOMENT-70 PROVEN)
  governed by a NAMEABLE higher-moment (fracton/dipole) conservation law?
    (i)   is Q_dipole = INTEGRAL x.rho(x) CONSTRUCTIBLE on (A_K, H_K, D_K)?
    (ii)  WHICH broken-symmetry current of the
            (SU(3)_L x SU(3)_R)/Z_3 -> (SU(3)_L x SU(2)_R x U(1)_R)/Z_6
          pattern does it close on?
    (iii) the substrate-IS reading: fracton immobility == internal spectral
          reorganization, NOT through-container translation.

Pre-registered threshold (3-conjunct spec-completeness boolean):
  SPEC_complete := conservation_law_named AND current_named AND s105_spec_emitted
    conservation_law_named := Q_dipole = INTEGRAL x.rho(x) is named AND its
                              constructibility on (A_K, H_K, D_K) is EXPLICITLY
                              CLASSIFIED *constructible* (constructible -> GEM-COMPUTE-ready)
                              -- note the PASS clause requires the classification to be
                              CONSTRUCTIBLE, not merely "made".
    current_named          := the specific broken-symmetry current of the breaking
                              pattern the dipole moment closes on is named by explicit generator.
    s105_spec_emitted      := a 4-field (what/inputs/gate/effort) compute spec for the
                              dipole-charge Ward-identity test is written.

  PASS iff (Q_dipole named AND constructibility classified CONSTRUCTIBLE) AND
           (current named by explicit generator) AND s105_spec_emitted.
  FAIL iff Q_dipole NOT well-defined on the spectral triple OR no broken-symmetry
           current admits the higher-moment closure -> the fracton reading closes
           honestly at spec level (the Leggett Goldstone is an ordinary type-I/II
           Goldstone; mobility is NOT an independent identity-protection handle).
  INFO iff the higher-moment identity is STATEABLE but constructibility is UNDECIDED
           pending Nambu-Goldstone counting, OR the closing current is named only by
           symmetry-class (not by explicit generator).

THE DETERMINATION (this script's substrate-physics finding):
  Q_dipole = INTEGRAL x.rho(x) is NOT CONSTRUCTIBLE on (A_K, H_K, D_K).
  Reason (structural, decided -- not pending NG counting):
    A fracton dipole charge Q_dipole = INTEGRAL x.rho(x) is the conserved charge of an
    EMERGENT COORDINATE-DEPENDENT SHIFT of the Nambu-Goldstone field,
        delta(chi) = a_i x^i             [Argurio Eq.2.52, 2.60, 2.72]
    "Symmetry under shifts by linear terms imply that the DIPOLE MOMENT of the charge
     is conserved ... characteristic of models of fractons that are immobile" (Eq.2.60).
    This construction REQUIRES a spatial POSITION operator x^i acting as a multiplication
    operator on the field -- AND it is the NG mode of SPONTANEOUSLY BROKEN SPATIAL
    TRANSLATIONS (Argurio's helical background Phi=rho.e^{ikx} breaks P_x; the unbroken
    generator is P~_i = P_i - k_{ia} Q^a, Argurio intro p.3).
    On the substrate:
      (a) D_K lives on the COMPACT INTERNAL fiber SU(3) (Jensen-deformed). It is
          BLOCK-DIAGONAL in Peter-Weyl, D_K = (+)_{(p,q)} D_{(p,q)} (PROVEN, 8.4e-15,
          any left-invariant metric). A compact Lie group has NO position operator x:
          the Peter-Weyl Hilbert space is labelled by (p,q) IRREPS, not by a continuous
          coordinate, and a compact group carries no translation<->position canonical
          pair (P_i with conjugate x^i). There is NO x^i to integrate INTEGRAL x.rho
          against. The dipole charge is not an operator on (A_K, H_K, D_K).
      (b) The substrate's broken symmetry is INTERNAL: SU(3) -> U(1)_7 via the Kosmann
          derivative K_7 (atlas-04 N4 / W8 PROVEN: "K_7 is a Kosmann derivative
          (diffeomorphism), not an inner automorphism (gauge); [D_K, K_7]=0 at all
          orders"). K_7 is a DIFFEOMORPHISM OF THE FIBER, NOT a spatial translation P_i
          on an emergent base. The Argurio dipole charge needs the SPATIAL P_i (broken)
          and its conjugate x^i; the Leggett Goldstone lives on the INTERNAL U(1)_7
          breaking, which has neither.
    => conservation_law_named FAILS the PASS clause (constructibility classified
       NOT-CONSTRUCTIBLE, not constructible). This is a DECIDED FAIL (a structural wall,
       the no-position-operator-on-a-compact-fiber fact), NOT an INFO-pending-NG-counting:
       the constructibility is settled, and the current IS named by explicit generator
       (K_7). Per the rubric, the FAIL is the honest corridor-closure the wave was built
       to surface.

  SUBSTRATE-IS reading (the phononic-framing payoff, INVERTED from the gem hope):
    The fracton hope was that immobility would be a SECOND identity-protection handle
    (alongside Z_2-odd-forbidden non-annihilation). It is NOT -- but the REASON is the
    deepest possible statement of IS-space-not-IN-space: the Leggett mode has no dipole
    charge BECAUSE there is no container coordinate x to take a moment of. The mode IS a
    reorganization of D_K spectral weight (an inter-band phase rotation between the B2-B3
    Peter-Weyl sectors), not an excitation that could translate through a pre-existing
    geometry. "Immobility" is VACUOUS for the substrate Goldstone: there is no
    through-space motion to forbid, because space is emergent and the mode is internal.
    The Leggett mode's non-propagating character is ALREADY accounted for by its being a
    massless internal Goldstone (S48: spectral action blind to Goldstone mass by cyclic
    invariance) + Z_2-odd non-annihilation (S67/s73a) + Gamma_grav < H_0 stability
    (LEGGETT-GRAV-DECAY-67/CONDITIONAL). It does NOT need, and cannot carry, a
    fracton dipole-conservation handle.

Inputs (SHA-256 dual-pinned at runtime -- S84+ schema):
  - downloads/research-sweep-s103/topological-matter-exotics/06_Argurio_*.pdf
        (Fractons-GinzburgLandau-Broken-Translations; read on-disk, content-pinned)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<verdict-payload string>, scheme=FRACTON-HIGHER-MOMENT-CHARGE-SPEC,
   convention=SUBSTRATE-IS-INTERNAL-REORGANIZATION-NAMING, L_max=10)

Classification: PHONONIC (the Leggett-channel DM mode is an inter-band phase
  excitation of the B2-B3 substrate sector -- a phononic excitation of the fabric).

DISCIPLINE
----------
- `from canonical_constants import *` (first framework import).
- All intermediates tagged `# (local)`.
- CPU-only (string-valued spec record + schematic plot; no linear algebra);
  OMP cap set BEFORE numpy import.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA).
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool: this script PRINTS
  the payload; the dispatching agent calls emit_verdict. No open("a") (S98 race).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- CPU thread cap (BEFORE numpy import); this gate does no GPU work
#   + put computations/_shared on sys.path so canonical_constants imports
#     when the script is run from computations/session-104/.
# ---------------------------------------------------------------------------
import os
import sys
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")
_HERE = os.path.dirname(os.path.abspath(__file__))                 # (local)
_SHARED = os.path.join(os.path.dirname(_HERE), "_shared")          # (local)
if _SHARED not in sys.path:
    sys.path.insert(0, _SHARED)

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first framework import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import Mass_LeggettDM_over_Delta_BCS, tau_fold  # explicit

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S104"                                                   # (local)
GATE_ID = "S104-FRACTON-GOLDSTONE-SPEC"                            # (local)
SCHEME = "FRACTON-HIGHER-MOMENT-CHARGE-SPEC"                       # (local)
CONVENTION = "SUBSTRATE-IS-INTERNAL-REORGANIZATION-NAMING"        # (local)
L_MAX = "10"                                                       # (local) -- canonical truncation an S105 NG-counting compute would run at

PDF_DIR = PROJECT_ROOT / "downloads" / "research-sweep-s103" / "topological-matter-exotics"  # (local)
ARGURIO_PDF = PDF_DIR / "06_Argurio_Fractons-GinzburgLandau-Broken-Translations.pdf"          # (local)

OUT_NPZ = SESSION_DIR / "s104_fracton_goldstone_spec.npz"
OUT_PNG = SESSION_DIR / "s104_fracton_goldstone_spec.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    ARGURIO_PDF,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
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
    script_bytes = b""        # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""     # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()    # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 -- The spec record (string-valued; the substrate-physics content)
# ---------------------------------------------------------------------------

def build_spec() -> dict:
    """Construct the dipole-charge constructibility determination, the named
    broken-symmetry current, and the substrate-IS reading. All substrate-physics
    content is string-valued (a spec record); the conjunct booleans set the verdict."""

    # ---- (ii) WHICH broken-symmetry current the dipole moment WOULD close on ----
    # Named by EXPLICIT GENERATOR (not merely symmetry-class): the residual U(1)_7
    # inside the breaking pattern, generated by the Kosmann derivative K_7.
    breaking_pattern = "(SU(3)_L x SU(3)_R)/Z_3 -> (SU(3)_L x SU(2)_R x U(1)_R)/Z_6"  # (local)
    current_generator = "K_7"  # (local) -- the explicit generator
    current_named_object = (
        "The Leggett-channel DM mode is the Nambu-Goldstone boson of the residual "
        "U(1)_7 inside the breaking pattern " + breaking_pattern + ". The relevant "
        "broken-symmetry current is the U(1)_7 current j^mu_7 generated by the EXPLICIT "
        "generator K_7 (the unique surviving generator under SU(3) -> U(1)_7, S34 PROVEN). "
        "The BCS condensate breaks U(1)_7 SPONTANEOUSLY (atlas-04 B6 PROVEN: Cooper pairs "
        "carry K_7 charge +/-1/2; V(q_7=+1/4, q_7=-1/4)=0 to 9.5e-29, atlas-07 PERMANENT); "
        "the Leggett inter-band phase between the B2-B3 sectors IS the U(1)_7 phase boson "
        "(S80: 'Goldstone mass is the phase-boson mass from U(1)_7 breaking'). So the "
        "current the dipole moment WOULD have to close on is named by explicit generator: "
        "j^mu_7 = the conserved current of K_7. NAMED (by explicit generator, not "
        "symmetry-class) => the current_named conjunct is SATISFIED."
    )
    # K_7 is a DIFFEOMORPHISM of the fiber, NOT a spatial translation -- load-bearing for (i):
    current_is_internal_not_spatial = (
        "CRITICAL for constructibility (i): K_7 is a KOSMANN DERIVATIVE (a diffeomorphism "
        "of the INTERNAL SU(3) fiber), NOT an inner automorphism and NOT a SPATIAL "
        "translation P_i on an emergent base (atlas-04 N4 / W8 PROVEN: '[D_K, K_7]=0 at all "
        "orders; K_7 is a diffeomorphism, not a gauge'). The fracton dipole charge "
        "Q_dipole = INTEGRAL x.rho requires the SPATIAL translation P_i (broken) and its "
        "conjugate position x^i. The substrate breaking is INTERNAL (U(1)_7 on the fiber); "
        "it provides NEITHER a broken spatial P_i NOR a position x^i."
    )
    current_named = bool(current_named_object) and current_generator == "K_7"  # (local)

    # ---- (i) Q_dipole constructibility on (A_K, H_K, D_K) -- THE GATING QUESTION ----
    # Argurio's dipole charge is the conserved charge of delta(chi)=a_i x^i (Eq.2.52/2.60/2.72).
    argurio_construction = (
        "Argurio 2107.03073: a fracton arises from SPONTANEOUSLY BROKEN SPATIAL "
        "TRANSLATIONS (+ dilatations), via a gradient-Mexican-hat order parameter (Eq.2.1; "
        "helical background Phi = rho.e^{ikx} breaks P_x, Eq.2.5). The conserved higher-moment "
        "charge is the charge of an EMERGENT COORDINATE-DEPENDENT SHIFT of the NG field: "
        "delta(chi) = a_i x^i + c_ij x^i x^j + f(y) (Eq.2.60) [and delta(u_i)=a_i+b_ij x^j+"
        "c_ijk x^j x^k (Eq.2.72) for the meta-fluid]. Argurio Eq.2.60 verbatim: 'Symmetry "
        "under shifts by LINEAR terms imply that the DIPOLE MOMENT of the charge is conserved "
        "... characteristic of models of fractons that are immobile.' The unbroken generator "
        "is the diagonal P~_i = P_i - k_{ia} Q^a (intro p.3): a SPATIAL translation P_i locked "
        "to an internal charge Q^a. The dipole charge is thus Q_dipole = INTEGRAL d^d x . x^i . "
        "rho(x), with rho the density of the spatial-translation/shift charge -- it is "
        "INTRINSICALLY a FIRST SPATIAL MOMENT of a charge density and REQUIRES the position "
        "operator x^i."
    )
    # The substrate structural facts that decide constructibility:
    no_position_operator = (
        "D_K lives on the COMPACT INTERNAL fiber SU(3) (Jensen-deformed; tau_fold = "
        + f"{float(tau_fold)}" + "). It is BLOCK-DIAGONAL in the Peter-Weyl decomposition, "
        "D_K = (+)_{(p,q)} D_{(p,q)} (PROVEN to 8.4e-15, any left-invariant metric). The "
        "Peter-Weyl Hilbert space H_K = (+)_{(p,q)} V_{(p,q)} (x) V*_{(p,q)} is labelled by "
        "IRREP quantum numbers (p,q), NOT by a continuous spatial coordinate. A COMPACT Lie "
        "group carries NO position operator x: there is no translation<->position canonical "
        "pair (no P_i with conjugate x^i) because the group is compact (translations close "
        "into a torus, not a line; momenta are discrete Peter-Weyl labels). Consequently "
        "there is NO operator x^i on (A_K, H_K, D_K) to form INTEGRAL x.rho against."
    )
    breaking_is_internal_not_translational = (
        "The substrate's spontaneously broken symmetry is INTERNAL (U(1)_7 on the fiber, "
        "broken by the BCS condensate), NOT spatial translations. Argurio's fracton REQUIRES "
        "broken SPATIAL translations P_x (the gradient-Mexican-hat / helical mechanism). The "
        "substrate has NO broken spatial translation generator in the internal sector -- the "
        "Leggett Goldstone is the phase of an INTERNAL U(1)_7 condensate, an inter-band phase "
        "rotation, not a displacement field in an emergent base. The Argurio map "
        "P~_i = P_i - k_{ia} Q^a has no substrate referent because there is no internal P_i."
    )
    # => the determination:
    Q_dipole_constructible = False  # (local) -- DECIDED not-constructible
    constructibility_classification = "NOT-CONSTRUCTIBLE"  # (local)
    constructibility_is_decided = True  # (local) -- settled by a structural wall, NOT pending NG counting
    conservation_law_named_object = (
        "Q_dipole = INTEGRAL x.rho(x) is NAMED (the fracton dipole charge, Argurio Eq.2.60). "
        "Its constructibility on (A_K, H_K, D_K) is EXPLICITLY CLASSIFIED: NOT-CONSTRUCTIBLE. "
        "Reason (DECIDED -- a structural wall, not pending Nambu-Goldstone counting): (a) there "
        "is NO position operator x^i on the compact internal fiber SU(3) (Peter-Weyl labels "
        "are (p,q) irreps, not a continuous coordinate; a compact group has no P_i<->x^i "
        "canonical pair) -- so INTEGRAL x.rho is not an operator on the triple; (b) the "
        "substrate's broken symmetry is INTERNAL U(1)_7 (generator K_7, a fiber "
        "diffeomorphism), NOT broken spatial translations, so the gradient-Mexican-hat / "
        "helical fracton mechanism (which is what produces the conserved dipole moment) has no "
        "substrate realization. The current j^mu_7 IS named by explicit generator (K_7), but "
        "the DIPOLE MOMENT of that current is not a well-defined charge because there is no x."
    )
    # PASS clause requires the classification to be CONSTRUCTIBLE. It is NOT-CONSTRUCTIBLE.
    conservation_law_named_PASS_clause = bool(
        conservation_law_named_object) and (constructibility_classification == "CONSTRUCTIBLE")  # (local)

    # ---- (iii) the substrate-IS reading (named, not numerically verified) ----
    substrate_is_reading = (
        "The fracton HOPE was that immobility would be a SECOND DM-identity-protection handle "
        "(alongside Z_2-odd-forbidden non-annihilation). It is NOT -- and the REASON is the "
        "DEEPEST statement of IS-space-not-IN-space. The Leggett mode has no conserved dipole "
        "moment BECAUSE there is no container coordinate x to take a moment of: the substrate "
        "IS space (emergent), so an INTERNAL Goldstone has no through-space position to be "
        "immobile IN. The mode IS a redistribution of D_K spectral weight -- an inter-band "
        "phase rotation between the B2-B3 Peter-Weyl sectors -- not a relay pattern that could "
        "translate across a pre-existing geometry. Argurio's fracton immobility is a property "
        "of a DISPERSION RELATION in real space (omega^2 ~ 2A q_x^2, the 'lineon', Eq.2.30); "
        "the substrate Leggett mode has no real-space dispersion of that kind because it does "
        "not live in real space -- it lives in the internal Peter-Weyl spectrum. So 'immobility' "
        "is VACUOUS for the substrate Goldstone: there is no through-space motion to forbid. "
        "The mode's non-propagating, non-annihilating character is FULLY accounted for WITHOUT "
        "a fracton handle: massless internal Goldstone (S48, spectral action blind by cyclic "
        "invariance) + Z_2-odd non-annihilation (S67/s73a) + Gamma_grav < H_0 stability "
        "(LEGGETT-GRAV-DECAY-67/CONDITIONAL, Gamma_grav/H_0 ~ 8.85e-66). The fracton reading "
        "closes HONESTLY at spec level: the Leggett Goldstone is an ordinary (internal, "
        "type-B / massless) Goldstone; mobility is NOT an independent identity-protection handle."
    )

    # ---- 5-anatomy + 3-level supplied-vs-missing status -------------------
    anatomy = {
        "element_1_substrate_IS":
            "SUPPLIED -- the Leggett-channel DM mode (inter-band phase Goldstone of the B2-B3 "
            "sector) on (A_K, H_K, D_K); single-tau-slice level at tau_fold = "
            + f"{float(tau_fold)}" + ". Mass_LeggettDM/Delta_BCS = "
            + f"{float(Mass_LeggettDM_over_Delta_BCS)}" + " (LEGGETT-MOMENT-70 PROVEN).",
        "element_2_laboratory_IN":
            "PARTIAL -- the fracton immobility / subdimensional-Goldstone observable as realized "
            "in helical superfluids (Argurio's lab class: gradient-Mexican-hat order parameter, "
            "lineon dispersion omega^2 ~ 2A q_x^2). OE-form for any S105 Ward-identity observable "
            "would have to be made explicit -- but see element_3.",
        "element_3_bridge_map":
            "THE OPEN INGREDIENT -- CLOSED NEGATIVE. The higher-moment (dipole) Ward-Takahashi "
            "map requires Q_dipole = INTEGRAL x.rho, which is NOT constructible on (A_K, H_K, D_K) "
            "(no position operator x on the compact fiber; internal U(1)_7 breaking is not broken "
            "spatial translations). The bridge map does NOT exist => the cross-pillar bridge "
            "candidate is REJECTED at the constructibility gate.",
        "element_4_algebraic_envelope":
            "MISSING / MOOT -- no L^{-alpha} envelope; the S105 Ward-identity compute the bridge "
            "would have licensed is NOT dispatchable (Q_dipole not constructible).",
        "element_5_empirical_anchor":
            "MISSING / MOOT -- no numerical Ward-identity closure; there is no operator to close.",
        "three_level_status":
            "Level 1 (the higher-moment conservation structural identity) is the TARGET the spec "
            "would have stated -- but it CANNOT be stated as a substrate identity because Q_dipole "
            "is not an operator on the triple. Levels 2/3 are MOOT. The corridor closes at the "
            "SPEC level: NO registry slot, NO S105 compute. This is the honest S103-W4-style "
            "NOT-DISPATCHABLE declaration the gem CAVEAT flagged as the risk, here REALIZED.",
    }

    # ---- adjacent objects (audit-trail honesty) ---------------------------
    adjacent_objects = {
        "HIGHER-MOMENT-74":
            "FAIL in S74 (archive-harvested). DISTINCT object: HIGHER-MOMENT-74 tested SEELEY-DEWITT "
            "moments a_8, a_10 ('SDW expansion past a_4 has no structural meaning in project "
            "convention'). That is a CURVATURE-degree higher moment of D_K, NOT the fracton "
            "FIRST SPATIAL MOMENT Q_dipole = INTEGRAL x.rho of a charge density. The two 'higher "
            "moments' are categorically different (curvature-grade n vs spatial-coordinate first "
            "moment). Noted to prevent conflation; HIGHER-MOMENT-74 does NOT itself decide Q_dipole.",
        "massless_Goldstone_S48":
            "Spectral action blind to Goldstone mass by cyclic invariance (wall #7). The Leggett "
            "Goldstone is massless internally; this is the EXISTING account of its softness -- no "
            "fracton handle needed.",
        "Z2_odd_non_annihilation_S67_s73a":
            "The Leggett mode is CPT-neutral / Z_2-odd-forbidden non-annihilating "
            "(LEGGETT-GRAV-DECAY-67, s73a confirm). This is the EXISTING DM-identity-protection "
            "handle; the fracton spec asked whether mobility is a SECOND, INDEPENDENT handle -- "
            "the answer is NO.",
    }

    # ---- (iv) S105 spec -- on FAIL there is NO S105 compute spec -----------
    # The PASS routing (4-field S105 dipole-charge Ward-identity compute spec) is NOT emitted,
    # because Q_dipole is not constructible. We record the NULL S105 routing explicitly + the
    # FAIL-routing per the plan's Wave 5 -> Session-Close table (no CF; documented closure).
    s105_spec = {
        "emitted": False,
        "reason":
            "NO S105 dipole-charge Ward-identity compute spec is emitted: Q_dipole = INTEGRAL "
            "x.rho is NOT constructible on (A_K, H_K, D_K), so there is no operator whose Ward "
            "identity could be tested. Per the plan Wave-5 -> Session-Close routing (W5-3 FAIL "
            "row): corridor closed at spec level; the Leggett Goldstone is an ordinary "
            "(internal/massless) Goldstone; mobility is NOT an identity handle -- DOCUMENTED, NO "
            "carry-forward. (Contrast the PASS routing, NOT taken: a 4-field S105 dipole-charge "
            "Ward-identity compute making the item GEM-COMPUTE-ready.)",
    }
    s105_spec_emitted = bool(s105_spec.get("emitted"))  # (local) -- False on FAIL

    # ---- composite verdict (3-conjunct boolean) ---------------------------
    # PASS iff conservation_law_named (constructibility CONSTRUCTIBLE) AND current_named AND s105_spec_emitted.
    spec_complete_PASS = bool(
        conservation_law_named_PASS_clause and current_named and s105_spec_emitted)  # (local)
    # Verdict logic per rubric:
    #   FAIL iff Q_dipole NOT well-defined (constructibility NOT-CONSTRUCTIBLE), DECIDED.
    #   INFO iff stateable-but-constructibility-UNDECIDED, or current named only by symmetry-class.
    if (not Q_dipole_constructible) and constructibility_is_decided:
        verdict = "FAIL"  # (local)
    elif (not constructibility_is_decided) or (not current_named):
        verdict = "INFO"  # (local)
    elif spec_complete_PASS:
        verdict = "PASS"  # (local)
    else:
        verdict = "FAIL"  # (local)

    return {
        "verdict": verdict,
        "spec_complete_PASS": spec_complete_PASS,
        "conservation_law_named_PASS_clause": bool(conservation_law_named_PASS_clause),
        "current_named": bool(current_named),
        "s105_spec_emitted": bool(s105_spec_emitted),
        "Q_dipole_constructible": bool(Q_dipole_constructible),
        "constructibility_classification": constructibility_classification,
        "constructibility_is_decided": bool(constructibility_is_decided),
        "breaking_pattern": breaking_pattern,
        "current_generator": current_generator,
        "current_named_object": current_named_object,
        "current_is_internal_not_spatial": current_is_internal_not_spatial,
        "argurio_construction": argurio_construction,
        "no_position_operator": no_position_operator,
        "breaking_is_internal_not_translational": breaking_is_internal_not_translational,
        "conservation_law_named_object": conservation_law_named_object,
        "substrate_is_reading": substrate_is_reading,
        "anatomy": anatomy,
        "adjacent_objects": adjacent_objects,
        "s105_spec": s105_spec,
        "Mass_LeggettDM_over_Delta_BCS": float(Mass_LeggettDM_over_Delta_BCS),
        "tau_fold": float(tau_fold),
    }


# ---------------------------------------------------------------------------
# Section 6 -- schematic of the proposed higher-moment conservation on the
#   broken-symmetry pattern (and WHY it fails to close on the substrate)
# ---------------------------------------------------------------------------

def make_plot(spec: dict, out_png: Path) -> None:
    fig, ax = plt.subplots(figsize=(12.0, 8.6))  # (local)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title(
        "S104-FRACTON-GOLDSTONE-SPEC  --  verdict: " + spec["verdict"] + "\n"
        "Does the Leggett-channel DM Goldstone carry a fracton dipole charge "
        "Q$_{dipole}=\\int x\\,\\rho(x)$ on (A$_K$, H$_K$, D$_K$)?",
        fontsize=12.0, fontweight="bold")

    red = "#b3402e"      # (local) -- FAIL / broken-bridge color
    green = "#2e7d4f"    # (local)
    blue = "#3a5f9e"     # (local)
    grey = "#555555"     # (local)

    # ---- LEFT column: the Argurio fracton (lab side) ----
    lab = FancyBboxPatch((0.5, 5.3), 5.0, 3.9,
                         boxstyle="round,pad=0.10,rounding_size=0.18",
                         linewidth=1.8, edgecolor=blue, facecolor="#e8eef7", zorder=2)  # (local)
    ax.add_patch(lab)
    ax.text(3.0, 8.85, "Argurio 2107.03073  (lab / EFT side)", ha="center", va="top",
            fontsize=10.5, fontweight="bold", color=blue)
    ax.text(3.0, 8.25,
            "Broken SPATIAL translations P$_x$\n"
            "(gradient-Mexican-hat; $\\Phi=\\rho e^{ikx}$, Eq.2.5)\n"
            "$\\Rightarrow$ emergent shift  $\\delta\\chi = a_i x^i$  (Eq.2.60)\n"
            "$\\Rightarrow$ DIPOLE moment conserved:\n"
            "$Q_{dipole}=\\int d^dx\\; x^i\\,\\rho(x)$\n"
            "$\\Rightarrow$ fracton / lineon immobility\n"
            "($\\omega^2\\!\\simeq\\!2A q_x^2$, moves on a line)",
            ha="center", va="top", fontsize=8.8, color="#1a1a1a")

    # ---- RIGHT column: the substrate (IS side) ----
    sub = FancyBboxPatch((6.5, 5.3), 5.0, 3.9,
                         boxstyle="round,pad=0.10,rounding_size=0.18",
                         linewidth=1.8, edgecolor=green, facecolor="#e3f2e8", zorder=2)  # (local)
    ax.add_patch(sub)
    ax.text(9.0, 8.85, "Substrate  (IS side -- internal fiber)", ha="center", va="top",
            fontsize=10.5, fontweight="bold", color=green)
    ax.text(9.0, 8.25,
            "Broken INTERNAL  SU(3)$\\to$U(1)$_7$\n"
            "(BCS condensate; generator K$_7$, a\n"
            "Kosmann DIFFEOMORPHISM of the fiber)\n"
            "Leggett mode = U(1)$_7$ phase Goldstone\n"
            "(inter-band B2-B3 phase)\n"
            "D$_K=\\bigoplus_{(p,q)}$D$_{(p,q)}$  (Peter-Weyl;\n"
            "labels are (p,q) IRREPS, no coordinate x)",
            ha="center", va="top", fontsize=8.8, color="#1a1a1a")

    # ---- the bridge attempt (middle), STRUCK THROUGH ----
    arr = FancyArrowPatch((5.55, 7.25), (6.45, 7.25),
                          arrowstyle="-|>", mutation_scale=18,
                          linewidth=2.2, color=grey, zorder=3)  # (local)
    ax.add_patch(arr)
    # red X over the arrow
    ax.plot([5.85, 6.15], [7.05, 7.45], color=red, linewidth=3.0, zorder=4)
    ax.plot([5.85, 6.15], [7.45, 7.05], color=red, linewidth=3.0, zorder=4)
    ax.text(6.0, 7.7, "bridge map", ha="center", va="bottom", fontsize=8.0,
            color=grey, style="italic")

    # ---- the decisive obstruction box (center-bottom) ----
    obstruction = FancyBboxPatch((1.3, 2.2), 9.4, 2.5,
                                 boxstyle="round,pad=0.12,rounding_size=0.18",
                                 linewidth=2.6, edgecolor=red, facecolor="#f7e8e6", zorder=2)  # (local)
    ax.add_patch(obstruction)
    ax.text(6.0, 4.45, "OBSTRUCTION (decided structural wall)  -->  Q$_{dipole}$ NOT constructible",
            ha="center", va="top", fontsize=10.5, fontweight="bold", color=red)
    ax.text(6.0, 3.75,
            "(a) NO position operator x on the COMPACT fiber SU(3): Peter-Weyl labels are (p,q) irreps,\n"
            "      not a continuous coordinate; a compact group has no P$_i\\!\\leftrightarrow\\!x^i$ canonical pair.\n"
            "(b) Substrate breaking is INTERNAL U(1)$_7$ (K$_7$ = fiber diffeomorphism), NOT broken spatial P$_i$;\n"
            "      the gradient-Mexican-hat / helical fracton mechanism has no substrate realization.\n"
            "Current j$^\\mu_7$ IS named (generator K$_7$); its DIPOLE moment is not a charge -- there is no x.",
            ha="center", va="top", fontsize=8.7, color="#1a1a1a")

    # ---- substrate-IS reading footer ----
    ax.text(6.0, 1.45,
            "Substrate-IS reading: 'immobility' is VACUOUS for an INTERNAL Goldstone -- the mode IS a "
            "reorganization of D$_K$ spectral weight\n(inter-band B2-B3 phase), not a relay pattern that "
            "could translate through a container.  IS space, not IN space.\n"
            "Non-propagation already accounted for: massless internal Goldstone (S48) + Z$_2$-odd "
            "non-annihilation (S67/s73a) + $\\Gamma_{grav}\\!<\\!H_0$.",
            ha="center", va="top", fontsize=8.3, color=green, style="italic")

    ax.text(6.0, 0.18,
            "Conclusion: mobility is NOT an independent DM-identity-protection handle. "
            "Corridor closed at SPEC level (honest NOT-DISPATCHABLE). No registry slot, no S105 compute.",
            ha="center", va="bottom", fontsize=8.6, fontweight="bold", color=red)

    fig.tight_layout()
    fig.savefig(out_png, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] wrote {out_png}")


# ---------------------------------------------------------------------------
# Section 7 -- npz record (named symmetry/current strings + constructibility bool)
# ---------------------------------------------------------------------------

def write_npz(spec: dict, out_npz: Path) -> None:
    np.savez(
        out_npz,
        gate_id=GATE_ID,
        verdict=spec["verdict"],
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        # --- the three conjunct booleans + the gating boolean ---
        spec_complete_PASS=bool(spec["spec_complete_PASS"]),
        conservation_law_named_PASS_clause=bool(spec["conservation_law_named_PASS_clause"]),
        current_named=bool(spec["current_named"]),
        s105_spec_emitted=bool(spec["s105_spec_emitted"]),
        # --- the gating constructibility boolean (the gem's decisive question) ---
        Q_dipole_constructible=bool(spec["Q_dipole_constructible"]),
        constructibility_classification=spec["constructibility_classification"],
        constructibility_is_decided=bool(spec["constructibility_is_decided"]),
        # --- named symmetry / current strings ---
        breaking_pattern=spec["breaking_pattern"],
        current_generator=spec["current_generator"],
        current_named_object=spec["current_named_object"],
        current_is_internal_not_spatial=spec["current_is_internal_not_spatial"],
        # --- the construction + obstruction strings ---
        argurio_construction=spec["argurio_construction"],
        no_position_operator=spec["no_position_operator"],
        breaking_is_internal_not_translational=spec["breaking_is_internal_not_translational"],
        conservation_law_named_object=spec["conservation_law_named_object"],
        substrate_is_reading=spec["substrate_is_reading"],
        # --- anatomy + adjacency + S105 routing as JSON blobs ---
        anatomy_json=json.dumps(spec["anatomy"]),
        adjacent_objects_json=json.dumps(spec["adjacent_objects"]),
        s105_spec_json=json.dumps(spec["s105_spec"]),
        # --- composed-with canonical anchors ---
        Mass_LeggettDM_over_Delta_BCS=spec["Mass_LeggettDM_over_Delta_BCS"],
        tau_fold=spec["tau_fold"],
    )
    print(f"[npz]  wrote {out_npz}")


# ---------------------------------------------------------------------------
# Section 8 -- main: build spec, write artifacts, compute dual-SHA, PRINT payload
# ---------------------------------------------------------------------------

def print_verdict_payload(payload: dict) -> None:
    """Print the emit_verdict payload between sentinels so the dispatching agent
    can lift it and call the race-safe `emit_verdict` knowledge-MCP tool."""
    print("<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")


def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ({SCHEME}) ===")
    print(f"    session={SESSION}  convention={CONVENTION}  L_max={L_MAX}")

    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"=== audit_sha256={audit_sha}")
    print(f"=== content_sha256={content_sha}")

    spec = build_spec()  # (local)
    write_npz(spec, OUT_NPZ)
    make_plot(spec, OUT_PNG)

    # ---- concise verdict value payload (no single-quote chars; emit_verdict wraps it) ----
    value = (
        "verdict=" + spec["verdict"]
        + ";Q_dipole_constructible=" + str(spec["Q_dipole_constructible"])
        + ";constructibility=" + spec["constructibility_classification"] + "_DECIDED"
        + ";conservation_law_named=Q_dipole=INT_x.rho_NAMED_but_NOT_CONSTRUCTIBLE"
        + ";current_named=j^mu_7_generator_K_7_EXPLICIT"
        + ";reason=no_position_op_x_on_compact_fiber_SU(3)_PeterWeyl_(p,q)_labels__AND__"
        + "internal_U(1)_7_breaking_not_broken_spatial_P_i"
        + ";s105_spec_emitted=False_NO_compute(corridor_closed_no_CF)"
        + ";substrate_IS=immobility_VACUOUS_internal_Goldstone_IS_DK_spectral_reorg_not_thru_container"
        + ";Leggett_softness_already=massless_S48+Z2odd_S67/s73a+Gamma_grav<H_0"
        + ";HIGHER-MOMENT-74_DISTINCT(a_8,a_10_SDW_not_x.rho)"
    )  # (local)

    print(f"=== OUTPUT 4-tuple: (value=<{spec['verdict']}-payload>, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"=== verdict={spec['verdict']}  spec_complete_PASS={spec['spec_complete_PASS']}  "
          f"Q_dipole_constructible={spec['Q_dipole_constructible']}")

    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": spec["verdict"],
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "companion_note": (
            "SPEC-gate FAIL: Q_dipole=INT x.rho NOT constructible on (A_K,H_K,D_K) "
            "(no position op x on compact fiber SU(3); internal U(1)_7 breaking via K_7 "
            "diffeo, not broken spatial P_i). Current j^mu_7 named by explicit generator K_7. "
            "Corridor closed at spec level (honest NOT-DISPATCHABLE); Leggett Goldstone is "
            "ordinary internal/massless; mobility NOT an identity handle; no CF, no registry slot."
        ),
    }  # (local)
    print_verdict_payload(payload)

    print(f"=== done in {time.time() - t0:.2f}s ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
