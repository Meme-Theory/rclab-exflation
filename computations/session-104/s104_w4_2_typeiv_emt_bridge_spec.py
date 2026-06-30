#!/usr/bin/env python3
"""
S104 W4-2 — TYPE-IV EMT ↔ ACOUSTIC-WHITE-HOLE-INTERIOR BRIDGE SPEC
=================================================================

Gate: S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC ([VERIFY])

SPEC-FIRST bridge gate. NO physics number is computed this session. The
deliverable is a NAMED construction (Gamma_sub object + restoration-radius
surface + a 4-field S105 compute spec) OR an honest NOT-DISPATCHABLE
declaration, per the bridge-spec discipline.

Pre-registered threshold (set-membership / artifact-existence; NOT numerical):
  PASS  iff (a) Gamma_sub NAMEABLE in a_2-channel acoustic-EMT variables
            AND (b) restoration-radius surface NAMEABLE (relay acoustic
            horizon / Mach=1) AND (c) a 4-field S105 compute spec EMITTED.
  FAIL  iff the construction is UNNAMEABLE (the localized-relay acoustic-EMT
            object does not exist) -> corridor closed at spec level.
  INFO  iff the identity is STATEABLE but exactly ONE ingredient is unpinned
            -> NAME it.

The bridge (the candidate identity the spec states):
  Dumitru-Noronha (2505.09720 v3, eq. 5):  Gamma = (P_t + T00)^2 - 4 |M_vec|^2
    Gamma > 0 -> Hawking-Ellis type I  (timelike eigenvector; STATIC frame exists)
    Gamma = 0 -> type II               (degenerate null eigenvectors; radiation)
    Gamma < 0 -> type IV               (complex eigenvalue pair; NO causal
                 eigenvector; NEC violated; "cannot be static" -- no
                 hypersurface-orthogonal timelike Killing vector, PDF p.4)
    type-IV->type-I "restoration" at the gravitational radius (1-2 lambda_C).
  Substrate (S52/S63 acoustic metric; S85-W6-1-AWH-FORMAL PROVEN):
    ds^2 = (rho/c_s)[ -(c_s^2 - v^2) dt^2 - 2 v dt dtau + dtau^2 ]
    g_tt ∝ (v^2 - c_s^2); Killing vector d_t timelike iff v < c_s (subsonic,
    STATIC frame exists); spacelike iff v > c_s (supersonic white-hole
    interior, NO static frame). Acoustic horizon = Mach=1 surface.

  CANDIDATE Gamma_sub :=  c_s^2 - v^2  =  c_s^2 (1 - Mach^2)   [a_2-channel g_tt]
    Gamma_sub > 0 (subsonic)  <->  type I   (Gamma > 0)
    Gamma_sub = 0 (Mach = 1)  <->  type II  (Gamma = 0)   [restoration radius]
    Gamma_sub < 0 (supersonic)<->  type IV  (Gamma < 0)   [white-hole interior]
  Sage-verified sign correspondence (this plan-freeze):
    Gamma_sub(v = Mach c_s) = -(Mach+1)(Mach-1) c_s^2 = c_s^2 (1 - Mach^2).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/session-85/s85_w6_acoustic_white_hole_formal.npz  (S85-W6-1 PROVEN)
  - downloads/research-sweep-s103/qcd-hadron-oddities/
      05_Dumitru_Proton-EnergyCondition-Violation-GravRadius.pdf   (documentary)
  - canonical_constants.py                                         (feeds audit_sha)
  - script bytes                                                   (both SHAs)

Output 4-tuple:
  (value=<nameability outcome>, scheme=DUMITRU-NORONHA-2505.09720-typeIV-
   discriminant <-> S85-W6-1-AWH-FORMAL, convention=BRIDGE-SPEC, L_max=N/A)

Classification: PHONONIC. A hadron is a localized relay pattern ON the fabric;
the acoustic white-hole interior is a substrate transit signature. Direction:
substrate transit mathematics is logically prior -- "transit mathematics
inside a proton", NOT proton physics explaining the substrate.

DISCIPLINE
----------
- `from canonical_constants import *`
- intermediates tagged `# (local)`
- SPEC-EMITTER: CPU only (OMP_NUM_THREADS=8 before numpy); no GPU, no eigen-solve.
- dual-SHA (audit + content) emitted; 4-tuple printed; verdict via print_verdict_payload
  -> the dispatching agent calls mcp__knowledge__emit_verdict (race-safe).
- bridge map is a GENUINE acoustic-limit map (both sides reduce to the
  same eigenvector-causality question: does d_t stay timelike / does a static
  rest frame exist), NOT "analogous" / "corresponds to".
- dead_map_exclusion: the BLV map is DEAD at N_pair=1 (it is the COSMOLOGICAL
  single-transit flow); the localized-relay acoustic-EMT MUST source from the
  post-transit acoustic-EMT / a_2 channel only.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU cap + path setup + canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

# Put computations/_shared on the path so `from canonical_constants import *` resolves
# (scripts live at computations/session-104/; canonical_constants.py is in _shared/).
_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: E402,F401,F403

import numpy as np  # noqa: E402  (npz load only)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S104"                                                    # (local)
GATE_ID = "S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC"                        # (local)
SCHEME = "DUMITRU-NORONHA-2505.09720-typeIV-discriminant<->S85-W6-1-AWH-FORMAL"  # (local)
CONVENTION = "BRIDGE-SPEC"                                          # (local)
L_MAX = "N/A"                                                       # (local)

S85_NPZ = COMPUTATIONS_DIR / "session-85" / "s85_w6_acoustic_white_hole_formal.npz"  # (local)
DUMITRU_PDF = (
    PROJECT_ROOT
    / "downloads"
    / "research-sweep-s103"
    / "qcd-hadron-oddities"
    / "05_Dumitru_Proton-EnergyCondition-Violation-GravRadius.pdf"
)  # (local)

OUT_NPZ = SESSION_DIR / "s104_w4_2_typeiv_emt_bridge_spec.npz"      # (local)
OUT_PNG = SESSION_DIR / "s104_w4_2_typeiv_emt_bridge_spec.png"      # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S85_NPZ,
    DUMITRU_PDF,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
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


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
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

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Spec construction (no physics number; nameability evaluation)
# ---------------------------------------------------------------------------
def build_spec() -> dict:
    """Build the bridge spec. Returns structured fields for the npz + verdict.

    Three nameability bits drive the verdict:
      gamma_sub_object_named      -- is the substrate Gamma_sub object named?
      restoration_radius_named    -- is the type-IV->type-I surface named?
      s105_spec_emitted           -- is a 4-field S105 compute spec emitted?
    Plus the unpinned-ingredient count that distinguishes PASS from INFO.
    """
    # --- Load the PROVEN white-hole side (documentary; pins the horizon surface) ---
    s85 = np.load(S85_NPZ, allow_pickle=True)  # (local)
    s85_value = float(s85["min_causal_sep"])  # (local) = 0.016857840535543706
    s85_scheme = str(s85["scheme"])  # (local) EF_null
    s85_convention = str(s85["convention"])  # (local) mostly_minus
    tau_H_minus = float(s85["tau_H_minus"])  # (local) 0.1831 (entry/exit horizon)
    tau_H_plus = float(s85["tau_H_plus"])  # (local) 0.1969
    mach_at_fold = float(s85["mach_at_fold"])  # (local) 13.75

    # --- (a) The Gamma_sub object (a_2-channel acoustic-EMT variables) ---
    # Acoustic metric (S52/S63): g_tt ∝ (v^2 - c_s^2). The type-discriminant analog
    # is the SIGN of the g_tt component (timelike-Killing test). Define Gamma_sub as
    # the type-I-positive analog (matching Dumitru's Gamma sign convention):
    #   Gamma_sub := c_s^2 - v^2 = c_s^2 (1 - Mach^2)   [a_2-channel g_tt, sign-flipped to type-I>0]
    # Sage-verified (plan-freeze + this script's docstring):
    #   Gamma_sub(v=Mach*c_s) = -(Mach+1)(Mach-1) c_s^2 = c_s^2 (1 - Mach^2).
    gamma_sub_object = (
        "Gamma_sub(r) := c_s^2 - v(r)^2 = c_s^2 (1 - Mach(r)^2)  "
        "[a_2-channel acoustic-EMT g_tt component, sign-normalized to type-I>0]"
    )  # (local)
    gamma_sub_object_named = True  # (local)
    # Structural map to Dumitru's discriminant (the genuine acoustic-limit map):
    #   (P_t + T00)^2 vs 4|M_vec|^2   <->   c_s^2 vs v^2
    # Dumitru: Gamma<0 driven by 4|M_vec|^2 > (P_t+T00)^2, i.e. the energy-flux
    # (momentum-density T^0i, set by the J/angular-momentum GFF) dominating the
    # diagonal-stress combination. Acoustic analog: the flow momentum-density term
    # (the -2 v dt dtau cross term / v^2) dominating c_s^2 -> g_tt flips sign.
    gamma_sub_to_dumitru_map = (
        "4|M_vec|^2 > (P_t+T00)^2  (energy-flux T^0i from the J/ang-mom GFF dominates)  "
        "<->  v^2 > c_s^2  (flow momentum-density dominates sound speed; g_tt flips). "
        "Both are the SAME eigenvector-causality question: does the timelike Killing "
        "vector d_t stay timelike / does a static rest frame exist."
    )  # (local)

    # --- (b) The restoration-radius surface ---
    # type-IV -> type-II (Gamma=0) -> type-I  at the gravitational radius (1-2 lambda_C).
    # Substrate analog: Gamma_sub = 0  <=>  v(r_g) = c_s  <=>  Mach(r_g) = 1
    #   = the relay's ACOUSTIC HORIZON (Mach=1 surface), the localized-relay analog of
    #   the S85 fold/exit horizon (tau_H_minus=0.1831, tau_H_plus=0.1969 bracketing tau_fold=0.19).
    restoration_radius_surface = (
        "r_g : Mach(r) = 1  (the relay's acoustic horizon / Mach=1 surface, where "
        "Gamma_sub crosses 0 = type-II crossover). Localized-relay analog of the S85 "
        f"fold/exit horizon (tau_H_minus={tau_H_minus:.4f}, tau_H_plus={tau_H_plus:.4f} "
        f"bracketing tau_fold={tau_fold}; mach_at_fold={mach_at_fold:.3f})."
    )  # (local)
    restoration_radius_named = True  # (local)

    # --- (c) The 4-field S105 compute spec ---
    # The spec IS emittable. But it carries exactly ONE unpinned ingredient (below):
    # the localized-relay internal acoustic-flow profile v(r)/Mach(r) -- the analog of
    # the proton's J-GFF-sourced T^0i(r) radial profile. The substrate's relay-pattern
    # is currently a STANDING-WAVE superposition (Psi = sum c_{(p,q),n} psi_{(p,q),n};
    # S40/S63), which has NO constructed internal flow profile; and the only constructed
    # flow (the global transit Mach=13.75, N_pair=1) is the dead-BLV COSMOLOGICAL profile,
    # EXCLUDED for a localized relay. So the small-r Gamma_sub<0 region and the crossover
    # radius r_g cannot be evaluated until v(r) for a localized relay is constructed.
    unpinned_ingredients = [
        "localized-relay internal acoustic-flow profile v(r) / Mach(r) "
        "(the a_2-channel analog of the proton's J/angular-momentum-GFF-sourced "
        "T^0i(r) energy-flux radial profile). The relay-pattern is currently a "
        "standing-wave superposition (Psi = sum c psi; S40/S63) with NO constructed "
        "internal flow; the dead-BLV global transit flow (Mach 13.75, N_pair=1) is the "
        "COSMOLOGICAL profile, EXCLUDED for a localized relay."
    ]  # (local)
    n_unpinned = len(unpinned_ingredients)  # (local)

    s105_spec = {
        "what": (
            "Construct the localized-relay internal acoustic-flow profile v(r)/Mach(r) "
            "on the a_2 emergent-metric channel for a localized relay pattern (hadron "
            "analog = localized fiber-excitation overlap), then evaluate "
            "sign(Gamma_sub(r)) = sign(c_s^2 - v(r)^2) at small r vs large r, extract the "
            "crossover radius r_g where Mach(r_g)=1 (type-IV->type-II->type-I restoration), "
            "and operationalize the model-independent ANEC wall on the emergent GFFs."
        ),
        "inputs": (
            "S85-W6-1-AWH-FORMAL (acoustic metric / horizon machinery, PROVEN); the a_2 "
            "emergent-metric acoustic-EMT (s67_acoustic_tensor.py, a2_fold=2776.165); the "
            "localized-relay standing-wave construction (S40/S63 Psi=sum c psi) PLUS the "
            "new v(r) flow profile [THE PREREQUISITE]; the Dumitru-Noronha ANEC inequality "
            "(eq. 12: int_{-inf}^0 dt [m A(t) - (t/4m)(A(t)-2J(t))] >= 0) transcribed to the "
            "substrate emergent GFFs; canonical_constants.py (c_s, Mach, tau_fold)."
        ),
        "gate": (
            "PASS iff sign(Gamma_sub) < 0 at small r (type-IV core: no static acoustic rest "
            "frame) AND sign(Gamma_sub) > 0 at large r (type-I exterior) AND a finite "
            "crossover r_g (Mach=1) exists AND the emergent-GFF ANEC wall holds; the "
            "crossover-radius and Gamma_sub-sign tolerances pinned at the S105 plan-freeze. "
            "convention=mostly_minus (matching S85-W6-1). [SIGN] trigger (signed small-r vs "
            "large-r prediction)."
        ),
        "effort": (
            "1-2 gates. Construct v(r) for a localized relay (the prerequisite; the open "
            "construction); evaluate the radial sign test on the a_2 acoustic-EMT; extract "
            "r_g; transcribe + test the ANEC wall. CPU-scale unless the relay construction "
            "needs the L_max-truncated D_K spectrum (then pin L_max per the Casimir-bound "
            "pre-check)."
        ),
    }
    # The spec block is fully emitted -> True (it NAMES the small-r/large-r sign test +
    # crossover + ANEC wall, and names its own prerequisite).
    s105_spec_emitted = True  # (local)

    # --- Bridge anatomy (pre-named; this is a SPEC gate, NOT a registry-landing gate) ---
    bridge_anatomy = {
        "pillars": "Pillar I (acoustic) <-> Pillar VI (Hawking transit) <-> Pillar IV (a_2 emergent metric)",
        "substrate_IS": "the a_2-channel acoustic-EMT Hawking-Ellis type of a localized relay (sign of Gamma_sub)",
        "laboratory_IN": "the Breit-frame proton Wigner EMT Hawking-Ellis type (sign of Dumitru-Noronha Gamma)",
        "bridge_map": (
            "GENUINE acoustic-limit map: the a_2 emergent Einstein equation "
            "G_{mu nu} = 8 pi G_N <T_{mu nu}> links the acoustic-metric g_tt sign to the "
            "effective-EMT eigenvector causality; both reduce to the timelike-Killing / "
            "static-frame-existence question. NOT 'analogous' / 'corresponds to'."
        ),
        "note": (
            "SPEC only -- no §VII slot landed. A future §VII promotion adopts the 5-anatomy "
            "+ 3-level discipline (cross-pillar-bridge-anatomy.md) and the Stage-0 "
            "authoring-exclusion (NOT the S85/S97 authors)."
        ),
    }

    # --- Verdict logic (set-membership; pre-registered) ---
    # PASS iff (a) AND (b) AND (c) all nameable AND ZERO unpinned ingredients.
    # INFO iff identity stateable (a AND b) AND spec emittable (c) BUT exactly ONE unpinned.
    # FAIL iff any of (a)/(b)/(c) unnameable.
    if not (gamma_sub_object_named and restoration_radius_named and s105_spec_emitted):
        verdict = "FAIL"  # (local)
    elif n_unpinned == 0:
        verdict = "PASS"  # (local)
    elif n_unpinned == 1:
        verdict = "INFO"  # (local)
    else:
        # >1 unpinned: the identity is stateable but more than one ingredient is missing.
        # Per the rubric INFO is "exactly ONE"; >1 routes to FAIL (construction not yet
        # dispatchable as a single named compute). Not reached here (n_unpinned==1).
        verdict = "FAIL"  # (local)

    value = (
        f"nameability=(gamma_sub_named={gamma_sub_object_named},"
        f"restoration_radius_named={restoration_radius_named},"
        f"s105_spec_emitted={s105_spec_emitted});"
        f"n_unpinned={n_unpinned};"
        f"unpinned=localized-relay_acoustic-flow_profile_v(r);"
        f"verdict={verdict}"
    )  # (local)

    return {
        "value": value,
        "verdict": verdict,
        "gamma_sub_object_named": gamma_sub_object_named,
        "restoration_radius_named": restoration_radius_named,
        "s105_spec_emitted": s105_spec_emitted,
        "n_unpinned": n_unpinned,
        "gamma_sub_object": gamma_sub_object,
        "gamma_sub_to_dumitru_map": gamma_sub_to_dumitru_map,
        "restoration_radius_surface": restoration_radius_surface,
        "unpinned_ingredients": unpinned_ingredients,
        "s105_spec": s105_spec,
        "bridge_anatomy": bridge_anatomy,
        "s85_value": s85_value,
        "s85_scheme": s85_scheme,
        "s85_convention": s85_convention,
        "tau_H_minus": tau_H_minus,
        "tau_H_plus": tau_H_plus,
        "mach_at_fold": mach_at_fold,
        # Dumitru paper structural anchors (read from the on-disk PDF, full text):
        "dumitru_discriminant": "Gamma = (P_t + T00)^2 - 4|M_vec|^2  (eq. 5, p.3)",
        "dumitru_type_rule": "Gamma>0 type I; Gamma=0 type II; Gamma<0 type IV",
        "dumitru_typeIV": (
            "type IV: complex-conjugate eigenvalue pair, NO causal eigenvector, NEC "
            "violated, 'cannot be static' (no hypersurface-orthogonal timelike Killing "
            "vector, p.4); driven by M_vec=T^0i from the J/angular-momentum GFF."
        ),
        "dumitru_restoration": (
            "type-IV->type-I at the gravitational radius (1-2 Compton wavelengths), via "
            "type-II (Gamma=0) at the crossover; in the tail M_vec,P_t->0 so Gamma->T00^2>0."
        ),
        "dumitru_anec_wall": (
            "ANEC: int_{-inf}^0 dt [m A(t) - (t/4m)(A(t)-2J(t))] >= 0  (eq. 12) -- a "
            "model-independent, non-perturbative QFT constraint on the A,J GFFs."
        ),
    }


# ---------------------------------------------------------------------------
# Section 6 — Optional schematic plot
# ---------------------------------------------------------------------------
def make_plot(spec: dict) -> bool:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt  # (local)
    except Exception as exc:  # pragma: no cover
        print(f"  [plot skipped: {exc}]")
        return False

    # Schematic: Gamma_sub(r) = c_s^2 (1 - Mach(r)^2) for an ILLUSTRATIVE monotone-
    # decreasing Mach(r) (SCHEMATIC ONLY -- the real v(r) is the S105 prerequisite).
    r = np.linspace(0.0, 3.0, 400)  # (local) radius in units of relay Compton scale
    cs = 1.0  # (local) schematic c_s normalized
    # Illustrative core-peaked Mach profile crossing 1 near r_g ~ 1.3 (S85-style):
    mach_r = 2.6 * np.exp(-(r ** 2) / 1.6)  # (local) SCHEMATIC, not the substrate v(r)
    gamma_sub = cs ** 2 * (1.0 - mach_r ** 2)  # (local)
    rg_idx = int(np.argmin(np.abs(gamma_sub)))  # (local)
    rg = r[rg_idx]  # (local)

    fig, ax = plt.subplots(figsize=(8.2, 5.0))
    ax.axhline(0.0, color="0.4", lw=1.0)
    ax.plot(r, gamma_sub, color="#1f4e79", lw=2.2,
            label=r"$\Gamma_{\rm sub}(r)=c_s^2(1-\mathrm{Mach}(r)^2)$  [SCHEMATIC $v(r)$]")
    ax.fill_between(r, gamma_sub, 0, where=(gamma_sub < 0), color="#c00000", alpha=0.18)
    ax.fill_between(r, gamma_sub, 0, where=(gamma_sub > 0), color="#2e7d32", alpha=0.14)
    ax.axvline(rg, color="black", ls="--", lw=1.4)
    ax.annotate("type-IV core\n($\\Gamma_{\\rm sub}<0$, supersonic,\nNO static frame\n= white-hole interior)",
                xy=(0.15, gamma_sub[5]), xytext=(0.18, -4.6), fontsize=9, color="#7a0000")
    ax.annotate("type-I exterior\n($\\Gamma_{\\rm sub}>0$, subsonic,\nstatic frame = type I)",
                xy=(2.5, gamma_sub[-30]), xytext=(2.0, 0.35), fontsize=9, color="#1b5e20")
    ax.annotate(f"$r_g$: Mach$=1$\n(restoration radius\n= relay acoustic horizon)",
                xy=(rg, 0.0), xytext=(rg + 0.12, -2.4), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black"))
    ax.set_xlabel(r"relay radius $r$  (units of relay Compton scale; SCHEMATIC)")
    ax.set_ylabel(r"$\Gamma_{\rm sub}(r)$  (schematic units)")
    ax.set_title("S104-W4-2 SPEC: type-IV core / type-I exterior / Mach=1 crossover\n"
                 "Dumitru-Noronha $\\Gamma<0$ proton core  $\\leftrightarrow$  "
                 "S85-W6-1 acoustic white-hole interior  (SCHEMATIC $v(r)$ = S105 prerequisite)")
    ax.legend(loc="lower right", fontsize=8)
    ax.set_ylim(-6.0, 1.2)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  [plot written: {OUT_PNG.name}; SCHEMATIC v(r) ONLY]")
    return True


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(
    verdict: str, value, audit_sha: str, content_sha: str,
    companion_note: str = "", extra_rows: list[str] | None = None,
) -> dict:
    payload: dict = {
        "session": 104,
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

    spec = build_spec()
    verdict = spec["verdict"]

    # Console summary (NUMBERS/structure first)
    print("=== BRIDGE SPEC (no physics number computed this session) ===")
    print(f"  (a) Gamma_sub object NAMED: {spec['gamma_sub_object_named']}")
    print(f"      {spec['gamma_sub_object']}")
    print(f"      map->Dumitru: {spec['gamma_sub_to_dumitru_map']}")
    print(f"  (b) restoration-radius surface NAMED: {spec['restoration_radius_named']}")
    print(f"      {spec['restoration_radius_surface']}")
    print(f"  (c) S105 4-field spec EMITTED: {spec['s105_spec_emitted']}")
    print(f"      n_unpinned ingredient(s): {spec['n_unpinned']}")
    for u in spec["unpinned_ingredients"]:
        print(f"        UNPINNED: {u}")
    print(f"  S85-W6-1 white-hole side: value={spec['s85_value']:.6f} "
          f"scheme={spec['s85_scheme']} convention={spec['s85_convention']} "
          f"(PROVEN; horizon tau in [{spec['tau_H_minus']:.4f},{spec['tau_H_plus']:.4f}])")
    print(f"  bridge map: {spec['bridge_anatomy']['bridge_map']}")
    print()

    # Persist the full structured spec to npz (the required boolean fields + prose)
    np.savez(
        OUT_NPZ,
        gamma_sub_object_named=bool(spec["gamma_sub_object_named"]),
        restoration_radius_named=bool(spec["restoration_radius_named"]),
        s105_spec_emitted=bool(spec["s105_spec_emitted"]),
        n_unpinned=int(spec["n_unpinned"]),
        verdict=str(verdict),
        value=str(spec["value"]),
        gamma_sub_object=str(spec["gamma_sub_object"]),
        gamma_sub_to_dumitru_map=str(spec["gamma_sub_to_dumitru_map"]),
        restoration_radius_surface=str(spec["restoration_radius_surface"]),
        unpinned_ingredients=json.dumps(spec["unpinned_ingredients"]),
        s105_spec=json.dumps(spec["s105_spec"]),
        bridge_anatomy=json.dumps(spec["bridge_anatomy"]),
        dumitru_discriminant=str(spec["dumitru_discriminant"]),
        dumitru_type_rule=str(spec["dumitru_type_rule"]),
        dumitru_typeIV=str(spec["dumitru_typeIV"]),
        dumitru_restoration=str(spec["dumitru_restoration"]),
        dumitru_anec_wall=str(spec["dumitru_anec_wall"]),
        s85_value=float(spec["s85_value"]),
        s85_scheme=str(spec["s85_scheme"]),
        s85_convention=str(spec["s85_convention"]),
        tau_H_minus=float(spec["tau_H_minus"]),
        tau_H_plus=float(spec["tau_H_plus"]),
        mach_at_fold=float(spec["mach_at_fold"]),
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=str(L_MAX),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  [npz written: {OUT_NPZ.name}]")
    make_plot(spec)
    print()

    tag = emit_4tuple(spec["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        verdict,
        spec["value"],
        audit_sha,
        content_sha,
        companion_note=(
            "SPEC gate (no physics number); INFO = identity stateable, exactly ONE "
            "unpinned ingredient: localized-relay acoustic-flow profile v(r). "
            "Bridge Pillar I<->VI<->IV; dead-BLV (N_pair=1) EXCLUDED."
        ),
        extra_rows=[
            "# bridge_anatomy=Pillar-I-acoustic<->Pillar-VI-Hawking-transit<->Pillar-IV-a2-emergent-metric "
            "(genuine acoustic-limit map: g_tt sign = timelike-Killing/static-frame test, NOT analogous)",
            "# dead_map_exclusion=BLV-map-DEAD-at-N_pair=1 (cosmological single-transit flow); "
            "localized-relay acoustic-EMT MUST source from post-transit a_2 channel only",
            "# s105_prerequisite=construct localized-relay internal acoustic-flow profile v(r)/Mach(r) "
            "(a_2-channel analog of the J/ang-mom-GFF-sourced T^0i(r)); standing-wave Psi=sum c psi has no flow",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # spec gate: verdict is data; exit 0 on a clean run regardless of PASS/INFO/FAIL


if __name__ == "__main__":
    sys.exit(main())
