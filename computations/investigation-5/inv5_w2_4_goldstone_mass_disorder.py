#!/usr/bin/env python3
"""
INV5 W2-4 — INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER
===================================================

Gate: INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER  ([SIGN])

Pre-registered threshold (plan §W2-4, operator=inequality, two conjoined AND conditions):
  (i)  ENHANCEMENT : m_Goldstone / m_L1_bare > 1  (strict; the disorder mass exceeds the
                     bare Leggett-Goldstone anchor m_L1 = omega_L1 = 0.138 M_KK; target
                     DIRECTION = toward the structure-formation 170x Delta_BCS scale).
  (ii) PROTECTION  : x_Goldstone = omega_Goldstone / (2*Delta_BCS) < 1  (strict; the
                     disordered Goldstone mode stays BELOW the pair-breaking edge, like the
                     bare L1 mode at x_L1 = 0.1486 -- preserving the U-3 below-edge
                     DM-survival argument).
  PASS iff (i) AND (ii)  [logical AND: mass enhancement AND below-edge protection survive].

  [SIGN] sub-tests (load-bearing; substitution chain plan §W2-4 (7)):
    LEG 1 sign: (m_Goldstone - m_L1_bare) > 0   (Imry-Ma term positive-definite => predicted)
    LEG 2 sign: (x_Goldstone - 1)         < 0   (below-edge)
    Composite sign_verdict PASSes iff BOTH legs hold.
  The NUMBERS decide the sign -- no presupposition. The substrate's own non-C^2 Josephson
  disorder strength sets xi_disorder; whether it lands the mass in the non-empty window
  between "large enough to matter for the 170x shortfall" and "below the edge" IS the gate.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only; substrate pins)
  - computations/session-48/s48_goldstone_mass.npz  (rho_s_C2 phase stiffness; the BCS-floor
        Goldstone-mass estimate m_G_over_MKK_BCS; the SA Goldstone-mass=0 theorem record)
  - computations/session-29/s29b_josephson_coupling.npz  (Josephson-coupling provenance;
        tau_fold-epoch J-matrix Frobenius norm cross-check)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<enhancement + x_Goldstone + sign>, scheme=IMRY-MA-RANDOM-FIELD-GOLDSTONE-MASS,
   convention=DISORDER-LENGTH-FROM-NON-C2-JOSEPHSON-COUPLINGS, L_max=10)

Classification: PHONONIC.

METHODOLOGY
-----------
The U(1)_7 Goldstone IS the phase boson of the substrate's broken-U(1)_7 sector (PROVED
ungaugeable: [iK_7, D_K]=0, N4 BROKEN). It is the would-be-massless phase mode. Two PROVEN
facts about its bare mass bound this gate:
  - Spectral-action Goldstone mass = 0 EXACTLY (S48 GOLDSTONE-MASS-48 FAIL; wall:
    Tr[f(D(phi)^2)] = Tr[f(D^2)] under unitary conjugation -- the SA cannot mass the
    Goldstone). So the bare mass is NOT from the spectral action.
  - The BCS-floor estimate m_G_over_MKK_BCS = 0.006838 (s48) is the small fibre-mass floor.
  - The bare Leggett-Goldstone FREQUENCY anchor is omega_L1 = 0.138 M_KK (S49 DIPOLAR).

Imry-Ma (1975): a continuous-symmetry order parameter in a RANDOM FIELD breaks into domains
of size xi_disorder set by elastic-vs-random-field competition; the would-be Goldstone gains
a pinning mass m_Goldstone^2 ~ (disorder energy)^2 / xi_disorder^2. The random field HERE is
the substrate's OWN non-C^2 Josephson coupling spread -- the C^2 coset (J_C2=0.933, 4 bonds)
is the ORDERED/dominant backbone; the non-C^2 directions (su(2): J_su2=0.059, 3 bonds; u(1):
J_u1=0.038, 1 bond, softest) are the disorder RELATIVE to that backbone.

xi_disorder (LARKIN length, the substrate-natural construction):
  xi_L = J_stiff / h_rf   (bond units; weak-disorder continuum RF formula)
  J_stiff = J_C2 = 0.933   (ordered backbone elastic stiffness)
  h_rf    = rms non-C^2 coupling = sqrt(mean(J_su2^2,J_su2^2,J_su2^2,J_u1^2)) = 0.05451
  => xi_L = 17.11 bond units (LONG: backbone is ~17x stiffer than the random field).
The Goldstone GAP follows the framework dispersion omega_G(k) = sqrt(J k^2 + m^2)/sqrt(rho_s)
(S48 tesla-collab) => at k=0, omega_Goldstone = sqrt(m_Goldstone^2)/sqrt(rho_s),
rho_s = rho_s_C2 = 7.962 (s48).

The gate brackets FIVE physically-motivated xi_disorder constructions (A weak-disorder
Larkin [CANONICAL]; B/C/D saturated strong-disorder; E max-bond hardest reading) so the
verdict is robust to the construction choice and the .npz records the full bracket.

DISCIPLINE
----------
- `from canonical_constants import *`-style explicit imports
- every intermediate tagged `# (local)`
- numpy.linalg (scalar Imry-Ma + ratios; OMP capped at 8 per math-scripts.md CPU fallback)
- SHA-256 of all inputs logged in first 20 lines of stdout
- dual-SHA (audit + content) emitted (S84+)
- 4-tuple printed as final non-verdict line
- verdict via print_verdict_payload -> agent calls emit_verdict (race-safe)
- SOURCE-RECON: J_u1 pinned CANONICAL 0.038 (seed's 0.034 is STALE; D_max=0.048 NO-ACTION
  band; canonical_constants is the import-target, not survey prose). omega_L1=0.138 is the
  FREQUENCY anchor; the S49 DIPOLAR mass m_L1=0.070 is reported as the alt mass-anchor.

Author: landau-condensed-matter-theorist (Investigation 5, Wave 2, gate W2-4)
Date: 2026-06-15
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-fallback thread cap (math-scripts.md)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

t0 = time.time()  # (local)

# ---------------------------------------------------------------------------
# Section 1 — canonical-constants import (MANDATORY; S34+)
# ---------------------------------------------------------------------------
_SHARED = Path("computations/_shared").resolve()  # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import (  # noqa: E402
    J_C2,        # 0.933  C^2 coset, 4 bonds (dominant/ordered backbone)
    J_su2,       # 0.059  su(2), 3 bonds
    J_u1,        # 0.038  u(1), 1 bond (softest) -- CANONICAL (seed's 0.034 is stale)
    omega_L1,    # 0.138  bare Leggett-Goldstone FREQUENCY anchor
    Delta_BCS,   # 0.4642547394830737  R-PROTECTED gap; edge = 2*Delta_BCS
    M_KK,        # 7.42866e16 (gravity route); for GeV reporting only
)

# ---------------------------------------------------------------------------
# Section 2 — identity / scheme / convention pins
# ---------------------------------------------------------------------------
SESSION = 5  # (local) investigation number (track="investigation")
GATE_ID = "INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER"
SCHEME = "IMRY-MA-RANDOM-FIELD-GOLDSTONE-MASS"
CONVENTION = "DISORDER-LENGTH-FROM-NON-C2-JOSEPHSON-COUPLINGS"
L_MAX = "10"
TRIGGER = "[SIGN]"

# Bond multiplicities on the substrate gauge directions (S53 ginzburg fabric).
N_C2, N_SU2, N_U1 = 4, 3, 1   # (local) C^2 (4), su(2) (3), u(1) (1)

# Non-canonical comparison targets (plan §W2-4; survey/atlas-collab derived, NOT pins):
M_REQUIRED_OVER_M_LEGGETT = 170.0  # (local) structure-formation target factor (m_struct/m_Leggett)
MASS_LEGGETT_OVER_DELTA = 11.97    # (local) C11 Leggett anchor (mass_LeggettDM/Delta_BCS)
M_L1_DIPOLAR = 0.070               # (local) S49 DIPOLAR bare Goldstone MASS (alt anchor; mass-vs-freq)
J_U1_SEED_STALE = 0.034            # (local) seed/survey value -- STALE; canonical is 0.038

# ---------------------------------------------------------------------------
# Section 3 — input paths
# ---------------------------------------------------------------------------
P_CANON = _SHARED / "canonical_constants.py"
P_GMASS = Path("computations/session-48/s48_goldstone_mass.npz").resolve()
P_JOSEPH = Path("computations/session-29/s29b_josephson_coupling.npz").resolve()

OUT_NPZ = Path("computations/investigation-5/inv5_w2_4_goldstone_mass_disorder.npz")
OUT_PNG = Path("computations/investigation-5/inv5_w2_4_goldstone_mass_disorder.png")


def _sha256_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def _scalar(d, k, default=None):
    """Robust 0-D / 1-D scalar field extraction from an npz."""
    try:
        return float(np.asarray(d[k]).flat[0])
    except (KeyError, ValueError, TypeError):
        return default


# ---------------------------------------------------------------------------
# Section 4 — dual-SHA
# ---------------------------------------------------------------------------
def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — print_verdict_payload (template-faithful)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "track": "investigation",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 6 — compute
# ---------------------------------------------------------------------------
def imry_ma_mass(xi_bond, disorder_energy, rho_s):
    """Imry-Ma Goldstone mass and gap for a given (xi_disorder, disorder-energy).
    m_Goldstone^2 = disorder_energy^2 / xi_bond^2  (pinning energy density, M_KK^2);
    omega_Goldstone = m_Goldstone / sqrt(rho_s)    (framework dispersion at k=0)."""
    m_G = disorder_energy / xi_bond                      # (local) M_KK
    omega_G = m_G / np.sqrt(rho_s)                        # (local) M_KK gap frequency
    return m_G, omega_G


def compute() -> dict:
    # --- input SHAs logged first (discipline) ---
    sha_canon = _sha256_file(P_CANON)    # (local)
    sha_gmass = _sha256_file(P_GMASS)    # (local)
    sha_joseph = _sha256_file(P_JOSEPH)  # (local)
    print("[INPUT SHA-256]")
    print(f"  canonical_constants.py     = {sha_canon}")
    print(f"  s48_goldstone_mass.npz     = {sha_gmass}")
    print(f"  s29b_josephson_coupling    = {sha_joseph}")

    # --- load caches (substrate provenance) ---
    d_g = np.load(P_GMASS, allow_pickle=True)
    d_j = np.load(P_JOSEPH, allow_pickle=True)

    rho_s = _scalar(d_g, "rho_s_C2", default=7.962)          # (local) phase stiffness
    m_G_BCS_floor = _scalar(d_g, "m_G_over_MKK_BCS", default=0.006838)  # (local) BCS fibre-mass floor
    sa_goldstone_mass = 0.0                                  # (local) SA mass = 0 EXACT (S48 wall #7)
    j_frob_fold = _scalar(d_j, "tau3_J_matrix_frobenius", default=None)  # (local) tau~0.2 J-matrix norm

    # --- pair-breaking edge (exact from canonical gap) ---
    edge = 2.0 * Delta_BCS                                   # (local) M_KK two-quasiparticle continuum edge

    # === RANDOM-FIELD STRENGTH from the non-C^2 Josephson couplings ===
    # The C^2 coset (J_C2, 4 bonds) is the ORDERED elastic backbone (stiffness).
    # The non-C^2 directions (su(2) 3 bonds + u(1) 1 bond) ARE the random field.
    J_nonC2 = np.array([J_su2] * N_SU2 + [J_u1] * N_U1)      # (local) non-C^2 disorder bonds
    h_rf = float(np.sqrt(np.mean(J_nonC2 ** 2)))            # (local) rms non-C^2 coupling (random field)
    std_nonC2 = float(np.std(J_nonC2, ddof=0))             # (local) spread of non-C^2 couplings
    J_stiff = float(J_C2)                                   # (local) ordered backbone elastic stiffness

    # === xi_disorder (LARKIN, the substrate-natural / CANONICAL construction) ===
    # Weak-disorder continuum RF formula: xi_L = J_stiff / h_rf (bond units).
    xi_Larkin = J_stiff / h_rf                              # (local) LONG (backbone >> random field)

    # === BRACKET of xi_disorder constructions (robustness) ===
    # Each: (name, xi_bond, disorder_energy). Imry-Ma m^2 = E^2 / xi^2.
    constructions = [
        ("A_Larkin_weak",   xi_Larkin, h_rf),    # CANONICAL: weak-disorder, long xi
        ("B_saturated_hrf", 1.0,       h_rf),    # strong-disorder saturated, xi=1 bond
        ("C_saturated_Ju1", 1.0,       J_u1),    # saturated, softest direction only
        ("D_std_nonC2",     1.0,       std_nonC2),  # variance/spread-driven
        ("E_max_bond_J_C2", 1.0,       J_C2),    # hardest reading: whole backbone as RF (unphysical upper)
    ]
    bracket = {}  # (local)
    for name, xi_b, E_d in constructions:
        m_G, omega_G = imry_ma_mass(xi_b, E_d, rho_s)        # (local)
        enh = m_G / omega_L1                                 # (local) LEG 1 enhancement
        x_G = omega_G / edge                                 # (local) LEG 2 below-edge ratio
        enh_dipolar = m_G / M_L1_DIPOLAR                      # (local) alt enhancement vs S49 mass anchor
        bracket[name] = dict(xi_bond=xi_b, E_disorder=E_d, m_G=m_G,
                             omega_G=omega_G, enh=enh, x_G=x_G, enh_dipolar=enh_dipolar)

    # === CANONICAL verdict on construction A (Larkin weak-disorder) ===
    A = bracket["A_Larkin_weak"]                             # (local)
    m_Goldstone = A["m_G"]                                   # (local) canonical disorder mass
    omega_Goldstone = A["omega_G"]                           # (local) canonical gap
    enhancement = A["enh"]                                   # (local) LEG 1: m_G / omega_L1
    x_Goldstone = A["x_G"]                                   # (local) LEG 2: omega_G / 2Delta_BCS

    # Bare-mode below-edge reference (cross-check the bare L1 is below-edge as the U-3 arg claims)
    x_L1_bare = omega_L1 / edge                              # (local) ~0.1486 (matches 0.149 plan ref)

    # === SIGN tests (NUMBERS decide; substitution chain plan §W2-4 (7)) ===
    # LEG 1 predicted POSITIVE: (m_Goldstone - m_L1_bare) > 0.   m_L1_bare = omega_L1.
    sign_leg1_delta = m_Goldstone - omega_L1                 # (local)
    sign_leg1_pass = sign_leg1_delta > 0                     # (local) enhancement > 1 ?
    # LEG 2 predicted NEGATIVE: (x_Goldstone - 1) < 0  (below edge).
    sign_leg2_delta = x_Goldstone - 1.0                      # (local)
    sign_leg2_pass = sign_leg2_delta < 0                     # (local) below edge ?
    # Composite sign PASSes iff BOTH legs hold.
    sign_pass = bool(sign_leg1_pass and sign_leg2_pass)      # (local)

    # === MAGNITUDE: how far toward the 170x structure shortfall ===
    # Target enhancement to reach 170*Delta_BCS from omega_L1:
    target_enh_170 = (M_REQUIRED_OVER_M_LEGGETT * Delta_BCS) / omega_L1  # (local) ~571.9
    # Target two-scale factor (170/11.97 = 14.20) the companion W2-2 gate uses:
    target_r_14 = M_REQUIRED_OVER_M_LEGGETT / MASS_LEGGETT_OVER_DELTA    # (local) ~14.20
    # Magnitude bands (plan §W2-4 INFO_meaning): >1x but << 14x => INFO partial; >=1x close
    # to 14x => PASS-strong; <1x => no enhancement (FAIL on LEG 1).
    frac_of_170 = m_Goldstone / (M_REQUIRED_OVER_M_LEGGETT * Delta_BCS)  # (local) fraction of structure mass
    frac_of_14x = enhancement / target_r_14                              # (local) fraction toward 14.2x

    return {
        # substrate inputs
        "rho_s": rho_s, "m_G_BCS_floor": m_G_BCS_floor, "sa_goldstone_mass": sa_goldstone_mass,
        "j_frob_fold": j_frob_fold if j_frob_fold is not None else float("nan"),
        "J_C2": J_C2, "J_su2": J_su2, "J_u1": J_u1, "omega_L1": omega_L1,
        "Delta_BCS": Delta_BCS, "edge": edge, "M_KK": M_KK,
        "N_C2": N_C2, "N_SU2": N_SU2, "N_U1": N_U1,
        # random field
        "h_rf": h_rf, "std_nonC2": std_nonC2, "J_stiff": J_stiff, "xi_Larkin": xi_Larkin,
        # canonical (construction A) outputs
        "m_Goldstone": m_Goldstone, "omega_Goldstone": omega_Goldstone,
        "enhancement": enhancement, "x_Goldstone": x_Goldstone, "x_L1_bare": x_L1_bare,
        # sign tests
        "sign_leg1_delta": sign_leg1_delta, "sign_leg1_pass": bool(sign_leg1_pass),
        "sign_leg2_delta": sign_leg2_delta, "sign_leg2_pass": bool(sign_leg2_pass),
        "sign_pass": sign_pass,
        # magnitude / targets
        "target_enh_170": target_enh_170, "target_r_14": target_r_14,
        "frac_of_170": frac_of_170, "frac_of_14x": frac_of_14x,
        # comparison targets (non-canonical)
        "M_REQUIRED_OVER_M_LEGGETT": M_REQUIRED_OVER_M_LEGGETT,
        "MASS_LEGGETT_OVER_DELTA": MASS_LEGGETT_OVER_DELTA,
        "M_L1_DIPOLAR": M_L1_DIPOLAR, "J_U1_SEED_STALE": J_U1_SEED_STALE,
        # bracket (flattened for npz)
        **{f"br_{name}_{k}": v for name, sub in bracket.items() for k, v in sub.items()},
        # input shas
        "sha_canon": sha_canon, "sha_gmass": sha_gmass, "sha_joseph": sha_joseph,
        "_bracket": bracket,
    }


def evaluate_gate(r) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Pre-registered (plan §W2-4 strict_PASS_boundary, operator=inequality, AND):
      PASS  iff  enhancement > 1  AND  x_Goldstone < 1.
      LEG 1 (enhancement) is the load-bearing directional prediction; LEG 2 (below-edge)
      is the protection prediction. sign_verdict PASSes iff BOTH legs hold.
    """
    sign_v = "PASS" if r["sign_pass"] else "FAIL"            # (local)

    # MAGNITUDE: how large is the enhancement.
    #   PASS-strong  : enhancement within 20% of the 14.2x two-scale factor (closes shortfall).
    #   INFO         : enhancement > 1 but << 14x (partial -- works, protected, doesn't close 170x).
    #   FAIL         : enhancement <= 1 (Imry-Ma gives NO useful enhancement; LEG 1 fails).
    enh = r["enhancement"]                                   # (local)
    target_r = r["target_r_14"]                              # (local) 14.20
    if enh <= 1.0:
        mag_v = "FAIL"   # (local) no enhancement -- LEG 1 fails the parametric criterion
    elif abs(enh - target_r) / target_r <= 0.20:
        mag_v = "PASS"   # (local) reaches ~14x (closes the two-scale shortfall)
    else:
        mag_v = "INFO"   # (local) enhancement >1 but off-target (partial, complements B-3)

    # REGIME: deterministic single-point at tau_fold; Imry-Ma closed-form; weak-disorder
    # continuum formula valid (h_rf << J_stiff => RF perturbative; xi_L > 1 bond). VALID.
    regime_v = "VALID"   # (local)

    # Composite collapse (gate-verdicts.md deterministic rule):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Section 7 — plot
# ---------------------------------------------------------------------------
def make_plot(r):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    bracket = r["_bracket"]
    names = list(bracket.keys())

    # Panel A: enhancement (m_G/omega_L1) across xi_disorder constructions vs the >1 line.
    ax = axes[0]
    enh_vals = [bracket[n]["enh"] for n in names]            # (local)
    colors = ["#1f77b4", "#2ca02c", "#17becf", "#9467bd", "#d62728"]
    ax.bar(range(len(names)), enh_vals, color=colors)
    ax.axhline(1.0, color="k", ls="--", lw=1.5, label="enhancement = 1 (LEG-1 PASS boundary)")
    ax.axhline(r["target_r_14"], color="orange", ls=":", lw=1.5,
               label=f"14.2x two-scale target")
    ax.set_yscale("log")
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=30, ha="right", fontsize=7)
    ax.set_ylabel("enhancement  m_Goldstone / omega_L1  (log)")
    ax.set_title("LEG 1: disorder-mass enhancement vs bare anchor\n(CANONICAL = A_Larkin_weak)")
    ax.legend(fontsize=7, loc="best")
    ax.grid(True, alpha=0.3, axis="y")

    # Panel B: below-edge ratio x_Goldstone across constructions vs the <1 edge.
    ax = axes[1]
    xg_vals = [bracket[n]["x_G"] for n in names]             # (local)
    ax.bar(range(len(names)), xg_vals, color=colors)
    ax.axhline(1.0, color="r", ls="--", lw=1.8, label="x = 1 (pair-breaking edge 2*Delta_BCS)")
    ax.axhline(r["x_L1_bare"], color="green", ls=":", lw=1.5,
               label=f"x_L1 bare = {r['x_L1_bare']:.4f}")
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=30, ha="right", fontsize=7)
    ax.set_ylabel("x_Goldstone = omega_Goldstone / 2*Delta_BCS")
    ax.set_ylim(0, 1.15)
    ax.set_title("LEG 2: below-edge PROTECTION (all constructions << 1)")
    ax.legend(fontsize=7, loc="best")
    ax.grid(True, alpha=0.3, axis="y")

    fig.suptitle("INV5-W2-4 — Imry-Ma Goldstone mass from non-C^2 Josephson disorder "
                 f"(enh_A={r['enhancement']:.3f}, x_G_A={r['x_Goldstone']:.4f})", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    r = compute()
    composite, sign_v, mag_v, regime_v = evaluate_gate(r)

    print("\n[SUBSTRATE INPUTS]")
    print(f"  rho_s (phase stiffness, s48)     = {r['rho_s']:.4f}")
    print(f"  SA Goldstone mass (S48 wall)     = {r['sa_goldstone_mass']:.1f}  (EXACT 0; Tr[f(D(phi)^2)]=Tr[f(D^2)])")
    print(f"  BCS-floor m_G/M_KK (s48)         = {r['m_G_BCS_floor']:.6f}")
    print(f"  J_C2 (backbone, 4 bonds)         = {r['J_C2']:.4f}")
    print(f"  J_su2 (3 bonds) / J_u1 (1 bond)  = {r['J_su2']:.4f} / {r['J_u1']:.4f}  (J_u1 CANONICAL; seed 0.034 STALE)")
    print(f"  omega_L1 (bare anchor, FREQ)     = {r['omega_L1']:.4f} M_KK")
    print(f"  Delta_BCS / edge=2*Delta_BCS     = {r['Delta_BCS']:.6f} / {r['edge']:.6f} M_KK")

    print("\n[RANDOM FIELD from non-C^2 Josephson couplings]")
    print(f"  h_rf (rms non-C^2 coupling)      = {r['h_rf']:.6f} M_KK")
    print(f"  std(non-C^2)                     = {r['std_nonC2']:.6f} M_KK")
    print(f"  J_stiff (C^2 backbone)           = {r['J_stiff']:.4f} M_KK")
    print(f"  xi_Larkin = J_stiff/h_rf         = {r['xi_Larkin']:.4f} bond units (LONG => weak disorder)")

    print("\n[CANONICAL construction A (Larkin weak-disorder)]")
    print(f"  m_Goldstone                      = {r['m_Goldstone']:.6f} M_KK")
    print(f"  omega_Goldstone = m_G/sqrt(rho_s)= {r['omega_Goldstone']:.6f} M_KK")
    print(f"  LEG 1 enhancement m_G/omega_L1   = {r['enhancement']:.6f}  (>1 ? {r['sign_leg1_pass']})")
    print(f"  LEG 2 x_Goldstone = w_G/2Delta   = {r['x_Goldstone']:.6f}  (<1 ? {r['sign_leg2_pass']})")
    print(f"  x_L1 bare cross-check            = {r['x_L1_bare']:.6f}  (plan ref 0.149)")

    print("\n[BRACKET of xi_disorder constructions]")
    print(f"  {'construction':<18}{'xi(bond)':>10}{'E_dis':>10}{'m_G':>11}{'omega_G':>11}{'enh':>10}{'x_G':>10}")
    for name, sub in r["_bracket"].items():
        print(f"  {name:<18}{sub['xi_bond']:>10.4f}{sub['E_disorder']:>10.4f}"
              f"{sub['m_G']:>11.5f}{sub['omega_G']:>11.5f}{sub['enh']:>10.4f}{sub['x_G']:>10.5f}")

    print("\n[MAGNITUDE vs shortfall targets]")
    print(f"  target enh to reach 170*Delta    = {r['target_enh_170']:.3f}")
    print(f"  target two-scale 170/11.97        = {r['target_r_14']:.4f}")
    print(f"  frac of 170x reached (A)          = {r['frac_of_170']:.6e}")
    print(f"  frac of 14.2x reached (A)         = {r['frac_of_14x']:.6e}")

    print("\n[3-TUPLE]")
    print(f"  sign_verdict      = {sign_v}  (LEG1 enh>1: {r['sign_leg1_pass']}  AND  LEG2 below-edge: {r['sign_leg2_pass']})")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {regime_v}")
    print(f"  composite         = {composite}")

    # --- save npz ---
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    save = {k: v for k, v in r.items() if k != "_bracket"}  # (local) drop nested dict
    np.savez(
        OUT_NPZ,
        **{k: np.asarray(v) for k, v in save.items()},
        composite=np.asarray(composite),
        sign_verdict=np.asarray(sign_v),
        magnitude_verdict=np.asarray(mag_v),
        regime_verdict=np.asarray(regime_v),
        gate_id=np.asarray(GATE_ID),
        scheme=np.asarray(SCHEME),
        convention=np.asarray(CONVENTION),
        sourcerecon_J_u1_canonical=np.asarray(0.038),
        sourcerecon_J_u1_seed_stale=np.asarray(0.034),
        sourcerecon_D_max=np.asarray(abs(np.log10(0.038) - np.log10(0.034))),
    )
    make_plot(r)

    # --- dual-SHA pin map (5-class file-pin) ---
    pins = {
        "canonical_constants.py": r["sha_canon"],
        "s48_goldstone_mass.npz": r["sha_gmass"],
        "s29b_josephson_coupling.npz": r["sha_joseph"],
    }
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), P_CANON, pins)
    print(f"\n[audit closure hash inputs] {json.dumps(dict(sorted(pins.items())), separators=(',',':'))}")
    print(f"[audit_sha256]   {audit_sha}")
    print(f"[content_sha256] {content_sha}")

    # --- 4-tuple (final non-verdict line) ---
    value_str = (f"enh={r['enhancement']:.4f}|x_G={r['x_Goldstone']:.4f}|"
                 f"m_G={r['m_Goldstone']:.5f}|xi_L={r['xi_Larkin']:.3f}|"
                 f"leg1={'POS' if r['sign_leg1_pass'] else 'NEG'}|"
                 f"leg2_belowedge={r['sign_leg2_pass']}|frac170={r['frac_of_170']:.3e}")
    print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # --- verdict payload ---
    note = (f"xi_Larkin={r['xi_Larkin']:.3f}bond h_rf={r['h_rf']:.5f} m_G={r['m_Goldstone']:.5f}M_KK "
            f"enh={r['enhancement']:.4f}(LEG1 {'>1' if r['sign_leg1_pass'] else '<=1 FAIL'}) "
            f"x_G={r['x_Goldstone']:.4f}(LEG2 below-edge {r['sign_leg2_pass']}) "
            f"weak-disorder regime: backbone J_C2>>h_rf => long xi => suppressed mass; "
            f"window EMPTY (protected but no 170x enhancement)")
    print_verdict_payload(
        composite, value_str, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=note,
    )

    print(f"\n[done in {time.time()-t0:.2f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
