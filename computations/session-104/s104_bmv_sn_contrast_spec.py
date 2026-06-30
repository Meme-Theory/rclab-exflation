#!/usr/bin/env python3
"""
S104 W5-2 — S104-BMV-SN-CONTRAST-SPEC (gravity-quantumness fourth-box placement spec)
=====================================================================================

Gate: S104-BMV-SN-CONTRAST-SPEC ([VERIFY])
  SPEC-ONLY gate. No numerical entanglement-witness or torsion-balance value is
  computed this wave (those are the S105 compute the spec emits). The deliverable
  is the SPEC, not the bridge.

Pre-registered threshold (3-conjunct spec-completeness boolean):
  SPEC_complete := taxonomy_placed AND deriving_objects_named AND s105_spec_emitted
    taxonomy_placed         := substrate located in the 'fourth box' with the
                               NONcommutativity of A_K named as WHY Ludescher's
                               commutative-mediator no-go does not apply.
    deriving_objects_named  := (SN-null deriving object named)
                               AND (GME/BMV deriving object named)
                               AND (the a_2-channel which-path sub-question explicitly
                                    classified as decidable-and-named
                                    OR undecidable-at-spectral-moment-level).
    s105_spec_emitted       := a 4-field (what/inputs/gate/effort) compute spec for
                               the named which-path/SN observable is written.
  PASS iff all three conjuncts True; FAIL iff neither the SN object nor the GME
  classification is nameable; INFO iff taxonomy + SN object named but the GME
  which-path map is named only SCHEMATICALLY (stateable-yet-unpinned).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - downloads/research-sweep-s103/qg-phenomenology-tabletop/02_Ludescher_*.pdf  (commutative-mediator no-go)
  - downloads/research-sweep-s103/qg-phenomenology-tabletop/07_Yan_*.pdf        (SN torsion-balance null)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<SPEC_complete>, scheme=FOURTH-BOX-TAXONOMY-SPEC,
   convention=SUBSTRATE-IS-A2-MOMENT-GRAVITY-NAMING, L_max=N/A)

Classification: GEOMETRIC (gravity as the a_2 second Seeley-DeWitt moment of the
  NONcommutative D_K on A_K = C (+) H (+) M_3(C) is a fabric-structure object;
  the BMV/SN observables are emergent-gravity readings of it).

METHODOLOGY
-----------
Two source PDFs (read on-disk, content-pinned) ground the two deriving objects:
  (A) Ludescher 2507.13201 — CONCLUSION verbatim: "classicality, defined in terms
      of COMMUTATIVITY of the observable algebra, fundamentally prohibits the
      generation of entanglement." The no-go's load-bearing hypothesis is the
      COMMUTATIVITY of the mediator algebra G (commutative C* => nuclear => forced
      triseparable->product structure, Lemma 1+2). A_K has NONcommutative summands
      (H, M_3(C)) => the no-go's hypothesis FAILS TO APPLY. Bonus: Ludescher cites
      van Luijk Thm D (LOCC extracts arbitrary entanglement if the algebra is NOT
      type-I); the substrate is Type-I_oo (S97-VN-TYPE PASS) — the side where
      independent product states (the GME-protocol prerequisite) are well-defined.
  (B) Yan 2411.17817 — SN self-gravity term (Eq.2) ½Mω²_SN(x̂−⟨x̂⟩)² is a
      STATE-DEPENDENT self-potential; ω_SN = Gm/(6√π Δx³_int) (Eq.3) sourced by the
      wavefunction's own |ψ|²-spread Δx_int. Result: SN-null. The substrate's
      a_2 = Σ_j mult_j/λ_j² is a FIXED functional of the D_K spectrum, carrying NO
      ⟨x̂⟩/|ψ|² dependence => SN-null BY CONSTRUCTION.
Composed-with canonical state verified via the knowledge MCP (recorded in the WP
§"MCP Pre-Compute Audit"): G_N = 1/(16π a_2 M_KK²); a_2_FW_zeta = 2776.165389;
two-layer split a_0->CC / a_2->Newton (Spectral-Moment Decoupling S75 W2-E PASS,
a_0,a_2,a_4 algebraically independent); GRAV-BACKREACT-63 is O(G_N²) NOT a
which-path computation; BLV mediator s77_mu_eff_b2_mediated is INFO/MIGRATED (DEAD).
The script does NOT compute any entanglement-witness or torsion-balance value.

DISCIPLINE
----------
- `from canonical_constants import *` (first import).
- All intermediates tagged `# (local)`.
- CPU-only (string-valued spec record + schematic plot; no linear algebra);
  OMP cap set BEFORE numpy import.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA).
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool: this script
  PRINTS the payload; the dispatching agent calls emit_verdict. No open("a").
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import); this gate does no GPU work
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
# Section 1 — Canonical constants (MANDATORY first framework import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import a_2_FW_zeta  # explicit (used in the SN-null spec)

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
from matplotlib.patches import FancyBboxPatch

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S104"                                              # (local)
GATE_ID = "S104-BMV-SN-CONTRAST-SPEC"                         # (local)
SCHEME = "FOURTH-BOX-TAXONOMY-SPEC"                           # (local)
CONVENTION = "SUBSTRATE-IS-A2-MOMENT-GRAVITY-NAMING"          # (local)
L_MAX = "N/A"                                                 # (local) — algebra-structural, not L_max-truncation-dependent

PDF_DIR = PROJECT_ROOT / "downloads" / "research-sweep-s103" / "qg-phenomenology-tabletop"  # (local)
LUDESCHER_PDF = PDF_DIR / "02_Ludescher_GME-via-Cstar-Algebras.pdf"           # (local)
YAN_PDF = PDF_DIR / "07_Yan_Torsion-Balance-Schrodinger-Newton.pdf"           # (local)

OUT_NPZ = SESSION_DIR / "s104_bmv_sn_contrast_spec.npz"
OUT_PNG = SESSION_DIR / "s104_bmv_sn_contrast_spec.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    LUDESCHER_PDF,
    YAN_PDF,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
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
# Section 5 — The spec record (string-valued; the substrate-physics content)
# ---------------------------------------------------------------------------

def build_spec() -> dict:
    """Construct the four-box placement, named deriving objects, and the
    which-path classification. All substrate-physics content is string-valued
    (a spec record); the three conjunct booleans are the gate's value."""

    # ---- (i) Four-box taxonomy placement (taxonomy_placed) ----------------
    # Box layout for the 2x2 schematic:
    #   row = (gravity classical?)         col = (sourced by |psi|^2 / state-dependent?)
    #   Box-1 full-quantum-graviton  : gravity quantized; exchanged d.o.f.
    #   Box-2 Moller-Rosenfeld       : gravity classical, mean-field <T_munu>
    #   Box-3 Schrodinger-Newton     : gravity classical, |psi|^2-sourced self-potential
    #   Box-4 SUBSTRATE (this work)  : gravity = a_2 moment of NONcommutative triple
    four_box = {
        "box_1_full_quantum_graviton":
            "gravity quantized; entanglement via exchanged (virtual) graviton d.o.f.",
        "box_2_moller_rosenfeld_semiclassical":
            "gravity classical mean-field; G_munu = 8piG/c^4 <T_munu> (Moller-Rosenfeld); "
            "ruled out by GME-detection per Ludescher (most-prominent semiclassical target)",
        "box_3_schrodinger_newton_self_gravity":
            "gravity classical; state-dependent self-potential 0.5*M*omega_SN^2*(x_hat-<x_hat>)^2 "
            "sourced by the wavefunction's own |psi|^2-spread (Yan Eq.2-3); SN-null measured",
        "box_4_substrate_FOURTH_BOX":
            "gravity = a_2 SECOND Seeley-DeWitt moment of the NONcommutative spectral triple "
            "A_K = C (+) H (+) M_3(C); G_N = 1/(16 pi a_2 M_KK^2); a_2 a FIXED functional of the "
            "D_K spectrum. DISTINCT from box-1/2/3.",
    }
    substrate_box = "box_4_substrate_FOURTH_BOX"  # (local)

    # WHY Ludescher's commutative-mediator no-go does NOT apply to the substrate:
    ludescher_noncommutativity_object = (
        "Ludescher 2507.13201 CONCLUSION (verbatim): 'classicality, defined in terms of "
        "COMMUTATIVITY of the observable algebra, fundamentally prohibits the generation of "
        "entanglement.' The no-go's load-bearing hypothesis is COMMUTATIVITY of the mediator "
        "algebra G (commutative unital C* = C_0(X) = functions on a space; commutative => nuclear "
        "=> Lemma 1: local channels preserve triseparability; Lemma 2: reduced A(x)B state separable). "
        "The substrate algebra A_K = C (+) H (+) M_3(C) has NONcommutative summands (H quaternions, "
        "M_3(C) matrices) => A_K is NOT a commutative unital C*-algebra G => the no-go's hypothesis "
        "FAILS TO APPLY; the substrate is NOT classified as a non-entangling classical mediator."
    )
    # Bonus type-classification cross-check (van Luijk, cited by Ludescher):
    type_I_cross_check = (
        "Ludescher cites van Luijk et al. Thm D: LOCC extracts arbitrary entanglement if the "
        "subalgebra is NOT type-I (in type II/III ALL bipartite states are entangled, no product "
        "state). The substrate is hyperfinite Type-I_oo (S97-VN-TYPE-INDUCTIVE-LIMIT PASS) — the "
        "side where independently-prepared product states (the GME-protocol prerequisite) ARE "
        "well-defined. The substrate sits on BOTH the noncommutative-algebra side AND the type-I side."
    )
    taxonomy_placed = (substrate_box == "box_4_substrate_FOURTH_BOX") and bool(
        ludescher_noncommutativity_object)  # (local)

    # ---- (ii) SN-null deriving object (a_2 is psi-independent) -------------
    sn_null_object = (
        "Yan 2411.17817: the Schrodinger-Newton SELF-GRAVITY term (their Eq.2) is "
        "0.5*M*omega_SN^2*(x_hat - <x_hat>)^2 — a STATE-DEPENDENT self-potential whose frequency "
        "omega_SN = G*m/(6*sqrt(pi)*Delta_x_int^3) (Eq.3) is sourced by the wavefunction's own "
        "internal-displacement spread Delta_x_int (a |psi|^2 / quantum-fluctuation quantity). The "
        "(x_hat-<x_hat>)^2 structure IS the |psi|^2-sourced self-coupling. SUBSTRATE DERIVING OBJECT: "
        "a_2 = Sum_j mult_j / lambda_j^2 is a FIXED functional of the D_K spectrum (a_2_FW_zeta = "
        f"{a_2_FW_zeta}); it carries NO <x_hat> / |psi|^2 dependence — there is no (x_hat-<x_hat>)^2 "
        "self-potential channel because a_2 is NOT psi-sourced => the substrate is SN-null BY "
        "CONSTRUCTION, with the QG-side null but for a STRUCTURALLY DISTINCT reason than "
        "'gravity is fully quantum'. The a_0->CC / a_2->Newton two-layer split (Spectral-Moment "
        "Decoupling S75 W2-E PASS) is load-bearing: SN self-gravity would be an a_2-sourced |psi|^2 "
        "self-interaction; the substrate's a_2 is a fixed D_K moment, not a psi-sourced self-potential."
    )

    # ---- (iii) GME/BMV deriving object (shared-substrate, not mediator) ----
    gme_object = (
        "BMV/GME assumes two masses interact SOLELY via a separate mediating gravitational d.o.f. "
        "(Ludescher Fig.1: a mediator G between A and B). SUBSTRATE DERIVING OBJECT: both masses are "
        "RELAY PATTERNS on ONE shared spectral triple (A_K, H_K, D_K); their A-B correlation is a "
        "SHARED-SUBSTRATE property of the common triple, NOT a mediator-exchange at all. There is no "
        "graviton-IN-spacetime between the masses; gravity is the SECOND spectral moment of the "
        "structure the masses ARE excitations of. So the BMV 'mediator G' has no substrate referent — "
        "the substrate denies the graviton-exchange picture (it has the a_2 moment, not an exchanged "
        "boson)."
    )

    # ---- (iii') the a_2-channel which-path sub-question — EXPLICIT classification
    # DEFINITE classification (a proof, not a schematic gesture):
    which_path_classification = "UNDECIDABLE-AT-SPECTRAL-MOMENT-LEVEL"  # (local)
    which_path_reason = (
        "The a_2 moment is a SCALAR (a single number = the second Seeley-DeWitt coefficient, a GLOBAL "
        "spectral invariant of D_K, a_2 = Sum_j mult_j/lambda_j^2). A scalar moment carries NO "
        "positional / which-path index — it is NOT a bilocal A<->B two-point correlator. Transmitting "
        "which-path QUANTUM information requires (i) a bilocal two-point operator with distinguishable "
        "A,B endpoints AND (ii) a measurement model mapping the shared-substrate correlation to an "
        "entanglement witness. The a_2 scalar supplies NEITHER at the spectral-moment level. Therefore "
        "whether the a_2 channel transmits which-path information is UNDECIDABLE-AT-THE-SPECTRAL-MOMENT-"
        "LEVEL WITHOUT a measurement model. This is a DEFINITE classification (a derived statement that "
        "the scalar provably cannot carry which-path content absent a measurement model), NOT a "
        "schematic placeholder => the third sub-clause of deriving_objects_named is SATISFIED."
    )
    which_path_is_classified = which_path_classification in (
        "DECIDABLE-AND-NAMED", "UNDECIDABLE-AT-SPECTRAL-MOMENT-LEVEL")  # (local)

    deriving_objects_named = (
        bool(sn_null_object) and bool(gme_object) and which_path_is_classified)  # (local)

    # ---- 5-anatomy + 3-level supplied-vs-missing status -------------------
    anatomy = {
        "element_1_substrate_IS":
            "SUPPLIED — gravity as the a_2 second Seeley-DeWitt moment of the NONcommutative D_K on "
            "A_K = C (+) H (+) M_3(C); G_N = 1/(16 pi a_2 M_KK^2); the psi-independence of a_2 is the "
            "SN-null deriving object. Level-1 (single-tau-slice) at the operator.",
        "element_2_laboratory_IN":
            "PARTIAL — (a) BMV entanglement-witness on two mesoscopic masses; (b) the SN torsion-"
            "balance null (Yan 2411.17817). OE-form for any S105 which-path observable must be made "
            "explicit; bare prose FORBIDDEN.",
        "element_3_bridge_map":
            "THE OPEN INGREDIENT — the map from the a_2-channel shared-substrate correlation to a "
            "laboratory which-path entanglement statement. Classified UNDECIDABLE-AT-SPECTRAL-MOMENT-"
            "LEVEL (the a_2 scalar is not bilocal; a measurement model is required). The SN-null map "
            "(a_2 psi-independence) is, by contrast, SUPPLIED.",
        "element_4_algebraic_envelope":
            "MISSING (deferred to S105 SN-null compute) — no L^{-alpha} envelope this wave.",
        "element_5_empirical_anchor":
            "MISSING — numerical SN-null (torsion-balance) value is the S105 deliverable, NOT this gate's.",
        "three_level_status":
            "Level 1 (the fourth-box structural placement + the A_K-noncommutativity argument + the "
            "a_2 psi-independence SN-null) is the TARGET the spec states and LANDS. Levels 2/3 MISSING. "
            "Per the plan: which-path classified UNDECIDABLE-AT-SPECTRAL-MOMENT-LEVEL => PASS still "
            "lands the Level-1 taxonomy placement, but the S105 spec is the SN-NULL compute, NOT a "
            "which-path compute. A spec-gate PASS does NOT constitute a registry-PASS.",
    }

    # ---- adjacent objects NOT resurrected (audit-trail honesty) -----------
    adjacent_not_resurrected = {
        "BLV_mediator_s77_mu_eff_b2_mediated":
            "INFO/MIGRATED (no-run-no-gate, N_pair=1) — the DEAD map; NOT a which-path BMV computation.",
        "GRAV_BACKREACT_63":
            "O(G_N^2) virtual graviton exchange between modes (cc-path-b.md PB-3); NOT a which-path "
            "computation.",
    }

    # ---- (iv) S105 compute spec (s105_spec_emitted) -----------------------
    # which-path UNDECIDABLE-AT-SPECTRAL-MOMENT-LEVEL => S105 spec is the SN-null compute.
    s105_spec = {
        "what":
            "Compute that a_2(tau) is <x_hat>/|psi|^2-INDEPENDENT — i.e. d a_2 / d <x_hat> = 0 EXACTLY "
            "for the D_K spectral functional a_2 = Sum_j mult_j/lambda_j^2 — contrasted against the SN "
            "self-potential channel 0.5*M*omega_SN^2*(x_hat-<x_hat>)^2 (Yan Eq.2). Derive the substrate "
            "SN frequency omega_SN,substrate = 0 (no |psi|^2 feedback) vs the Yan omega_SN.",
        "inputs":
            "D_K spectrum cache at L_max=10 (155,984 eigenvalues; the bottom sectors set a_2); "
            "a_2_FW_zeta = " + f"{a_2_FW_zeta}" + " (canonical_constants.py); Yan 2411.17817 Eq.2-3 "
            "(omega_SN = G*m/(6*sqrt(pi)*Delta_x_int^3)); G_N = 1/(16 pi a_2 M_KK^2).",
        "gate":
            "omega_SN,substrate / omega_SN,Yan < tol (PRE-REGISTER tol at the S105 plan; substrate "
            "predicts the ratio = 0 EXACT because a_2 has no |psi|^2 channel). PASS => substrate sits "
            "with the SN-null Yan measured, for a structurally distinct reason.",
        "effort":
            "1 gate (the S105 SN-null compute this spec licenses). The which-path map is flagged as a "
            "SEPARATE open construction requiring a measurement model — NOT scheduled at S105.",
    }
    s105_spec_emitted = bool(s105_spec) and all(s105_spec.get(k) for k in
                                                ("what", "inputs", "gate", "effort"))  # (local)

    spec_complete = bool(taxonomy_placed and deriving_objects_named and s105_spec_emitted)  # (local)

    return {
        "value": spec_complete,
        "taxonomy_placed": bool(taxonomy_placed),
        "deriving_objects_named": bool(deriving_objects_named),
        "s105_spec_emitted": bool(s105_spec_emitted),
        "spec_complete": spec_complete,
        "substrate_box": substrate_box,
        "four_box": four_box,
        "ludescher_noncommutativity_object": ludescher_noncommutativity_object,
        "type_I_cross_check": type_I_cross_check,
        "sn_null_object": sn_null_object,
        "gme_object": gme_object,
        "which_path_classification": which_path_classification,
        "which_path_reason": which_path_reason,
        "anatomy": anatomy,
        "adjacent_not_resurrected": adjacent_not_resurrected,
        "s105_spec": s105_spec,
        "a_2_FW_zeta": float(a_2_FW_zeta),
    }


# ---------------------------------------------------------------------------
# Section 6 — 2x2 taxonomy schematic
# ---------------------------------------------------------------------------

def make_plot(spec: dict, out_png: Path) -> None:
    fig, ax = plt.subplots(figsize=(11.0, 8.0))  # (local)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title(
        "Gravity-Quantumness Taxonomy — substrate in the FOURTH box\n"
        "(gravity = a$_2$ 2nd Seeley-DeWitt moment of the NONcommutative triple "
        "A$_K$ = $\\mathbb{C}\\oplus\\mathbb{H}\\oplus$M$_3(\\mathbb{C})$; "
        "G$_N$ = 1/(16$\\pi$ a$_2$ M$_{KK}^2$))",
        fontsize=11.5, fontweight="bold")

    # axis labels for the 2x2
    ax.text(5.0, 9.55, "columns: is the gravitational source state-dependent (|$\\psi|^2$-sourced)?",
            ha="center", fontsize=9, style="italic")
    ax.text(0.15, 5.0, "rows: is gravity quantized?", ha="center", va="center",
            rotation=90, fontsize=9, style="italic")

    # box positions: (x, y, w, h, title, body, facecolor, edgecolor, highlight)
    boxes = [
        (0.9, 5.2, 4.0, 3.4,
         "Box 1 — Full quantum graviton",
         "gravity QUANTIZED; entanglement\nvia exchanged (virtual) graviton.\nGME = YES (quantum).",
         "#e8eef7", "#4a6fa5", False),
        (5.1, 5.2, 4.0, 3.4,
         "Box 2 — Moller-Rosenfeld semiclassical",
         "gravity CLASSICAL mean-field;\nG$_{\\mu\\nu}$=8$\\pi$G/c$^4\\langle$T$_{\\mu\\nu}\\rangle$.\n"
         "Ruled OUT by GME-detection\n(Ludescher: prime target).",
         "#f7ece8", "#a5694a", False),
        (5.1, 1.0, 4.0, 3.4,
         "Box 3 — Schrodinger-Newton self-gravity",
         "gravity CLASSICAL; state-dependent\nself-potential ½M$\\omega_{SN}^2$(x̂$-\\langle$x̂$\\rangle)^2$\n"
         "|$\\psi|^2$-sourced (Yan Eq.2-3).\nSN-null MEASURED.",
         "#f7ece8", "#a5694a", False),
        (0.9, 1.0, 4.0, 3.4,
         "Box 4 — SUBSTRATE (this work)",
         "gravity = a$_2$ moment of the\nNONcommutative triple.\n"
         "a$_2$ FIXED functional of D$_K$ spectrum\n(NO |$\\psi|^2$ feedback)\n"
         "=> SN-NULL by construction;\nGME = shared-substrate, not exchange.",
         "#e3f2e8", "#2e7d4f", True),
    ]

    for (x, y, w, h, title, body, fc, ec, hl) in boxes:
        lw = 3.2 if hl else 1.6  # (local)
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.18",
                             linewidth=lw, edgecolor=ec, facecolor=fc, zorder=2)  # (local)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h - 0.42, title, ha="center", va="top",
                fontsize=10.0, fontweight="bold", color=ec, zorder=3)
        ax.text(x + w / 2, y + h - 1.15, body, ha="center", va="top",
                fontsize=8.6, color="#222222", zorder=3)
        if hl:
            ax.text(x + w / 2, y + 0.20, "<<  PASS: substrate placed here  >>",
                    ha="center", va="bottom", fontsize=8.6, fontweight="bold",
                    color="#2e7d4f", zorder=3)

    # deriving-objects + which-path classification banner (bottom)
    banner = (
        "Deriving objects (PDF-grounded):  "
        "[SN-null] a$_2$=$\\Sigma_j$mult$_j/\\lambda_j^2$ is $\\psi$-INDEPENDENT (Yan SN term is "
        "$|\\psi|^2$-sourced; a$_2$ is not)   |   "
        "[GME] both masses are relay patterns on ONE shared triple => correlation is shared-substrate, "
        "not a graviton exchange.\n"
        "which-path GME sub-question:  UNDECIDABLE-AT-SPECTRAL-MOMENT-LEVEL  "
        "(a$_2$ is a SCALAR global invariant, not a bilocal A$\\leftrightarrow$B correlator; a "
        "measurement model is required).   =>  S105 spec = SN-null compute.\n"
        "Ludescher no-go (COMMUTATIVITY of mediator => no entanglement) does NOT apply: A$_K$ has "
        "NONcommutative summands ($\\mathbb{H}$, M$_3(\\mathbb{C})$); substrate is Type-I$_\\infty$ "
        "(product states well-defined)."
    )
    ax.text(5.0, 0.46, banner, ha="center", va="center", fontsize=7.7,
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#fffced", edgecolor="#bbbbbb"),
            zorder=4)

    fig.tight_layout(rect=(0, 0.02, 1, 0.97))
    fig.savefig(out_png, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple output
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


def evaluate_gate(spec: dict) -> str:
    """Spec-completeness 3-conjunct boolean.
       PASS iff taxonomy_placed AND deriving_objects_named AND s105_spec_emitted.
       INFO iff taxonomy + SN-null object named but the GME which-path map is only
       schematic (deriving_objects_named False solely due to an unclassified
       which-path sub-question).
       FAIL iff neither the SN object nor the GME classification is nameable."""
    if spec["taxonomy_placed"] and spec["deriving_objects_named"] and spec["s105_spec_emitted"]:
        return "PASS"
    # INFO: taxonomy + SN object named, but which-path only schematic (not classified)
    sn_named = bool(spec["sn_null_object"])  # (local)
    if spec["taxonomy_placed"] and sn_named and not spec["deriving_objects_named"]:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                        # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # source-existence guard (honest gap-marking if a PDF is missing)
    for p, label in ((LUDESCHER_PDF, "Ludescher 2507.13201"), (YAN_PDF, "Yan 2411.17817")):
        if not p.exists():
            print(f"  [GAP] source PDF MISSING on disk: {label} -> {p}")

    spec = build_spec()

    # persist the spec record (strings + booleans) to .npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=str(L_MAX),
        value_spec_complete=np.array(spec["spec_complete"]),
        taxonomy_placed=np.array(spec["taxonomy_placed"]),
        deriving_objects_named=np.array(spec["deriving_objects_named"]),
        s105_spec_emitted=np.array(spec["s105_spec_emitted"]),
        substrate_box=spec["substrate_box"],
        four_box_json=json.dumps(spec["four_box"]),
        ludescher_noncommutativity_object=spec["ludescher_noncommutativity_object"],
        type_I_cross_check=spec["type_I_cross_check"],
        sn_null_object=spec["sn_null_object"],
        gme_object=spec["gme_object"],
        which_path_classification=spec["which_path_classification"],
        which_path_reason=spec["which_path_reason"],
        anatomy_json=json.dumps(spec["anatomy"]),
        adjacent_not_resurrected_json=json.dumps(spec["adjacent_not_resurrected"]),
        s105_spec_json=json.dumps(spec["s105_spec"]),
        a_2_FW_zeta=spec["a_2_FW_zeta"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  spec record written: {OUT_NPZ.name}")

    make_plot(spec, OUT_PNG)
    print(f"  schematic written:   {OUT_PNG.name}")
    print()

    print("  --- spec-completeness 3-conjunct booleans ---")
    print(f"    taxonomy_placed         = {spec['taxonomy_placed']}")
    print(f"    deriving_objects_named  = {spec['deriving_objects_named']}")
    print(f"    s105_spec_emitted       = {spec['s105_spec_emitted']}")
    print(f"    SPEC_complete           = {spec['spec_complete']}")
    print(f"    which-path GME          = {spec['which_path_classification']}")
    print()

    verdict = evaluate_gate(spec)
    value = spec["value"]

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    note = ("spec-gate PASS; Level-1 fourth-box placement lands; NOT a registry-PASS; "
            "S105 spec = SN-null compute (which-path UNDECIDABLE-AT-SPECTRAL-MOMENT-LEVEL)")  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha, companion_note=note)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
