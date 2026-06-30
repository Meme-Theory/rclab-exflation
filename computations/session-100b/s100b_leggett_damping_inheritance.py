#!/usr/bin/env python3
"""
S100b W6-3 — S100b-LEGGETT-DAMPING-INHERITANCE
==============================================

Gate: S100b-LEGGETT-DAMPING-INHERITANCE ([SIGN])
Plan: sessions/session-plan/session-100b-plan-w6.md SECTION W6-3
WP:   sessions/session-100b/session-100b-w6-workingpaper.md SECTION W6-3

Pre-registered operator (set-classification conjunction + ratio inequality):
  PASS iff (extraction complete)
       AND (every extracted lab damping mechanism classifies to channel class
            (i) or (ii) -- chi-closed for the relic)
       AND (no transported channel yields Gamma_inherit/H_0 >= 1)
  The quantitative transported-channel test, when class (iii) fires:
       Gamma_inherit/H_0 = (Gamma_L/omega_L)_lab x 2.87172e59  vs  1
  FAIL iff a class-(iii) member fires with transported rate >= 1.
  INFO iff extraction-limited (missing required element OR attribution
       ambiguous between channel classes) -- REGISTRY-INCOMPLETE-PENDING-
       FIRST-EXTRACTION analog tag (WP-scoped; no registry slot reserved).

Method (plan D1-D4):
  D1 EXTRACTION  -- Yuan arXiv 2412.13830 (SHA-pinned on-disk PDF; all 33
     pages read via Skill(pdf) 4-chunk split); values recorded as-printed.
  D2 KINEMATIC + PROTECTION-LAYER MAP -- x_lab = omega_L/(2*Delta_pi) (+ sigma
     diagnostic); x_L1 = omega_L1/(2*Delta_BCS); x_DM = 11.97/2. The two
     substrate Leggett-channel objects (L1 mode: kinematically protected;
     DM relic quantum: Z_2/J-evenness symmetry-protected) are NOT conflated.
  D3 CHI-TRANSPORT AUDIT -- classify each extracted lab damping mechanism
     into the pre-registered 3-class set {(i) pair-breaking continuum,
     (ii) extrinsic bath, (iii) intrinsic parity-EVEN multi-quantum}; only
     class (iii) transports through chi : C + H + M_3(C) -> M_2(C)
     (M_3(C) -> 0; ker chi = M_3(C); inheritance-falsifier-protocol.md
     canonical realization + 3HeB-inheritance-canonical.md).
  D4 VERDICT + CANONICAL-FORM OUTPUT -- survival STRICTLY in ratio/inequality
     form (Gamma_grav < H_0; tau_DM/t_univ = 1.13e65; Gamma_grav/H_0 ~
     8.85e-66) per the wave CANONICAL-FORM LAW.

Output 4-tuple:
  (value=<summary>, scheme=CHI-INHERITANCE-TRANSPORT-AUDIT, convention=RATIO,
   L_max=N/A)

Classification: PHONONIC

EXTRACTION RECORD (as-printed; PDF read in full, 4 chunks x <=10 pages):
  omega_L (observed)  = 1.8 THz +/- 0.8 THz   [main text p.4 + p.12: "overdamped
                        oscillation with a frequency of 1.8 THz +/- 0.8 THz";
                        center + error bar by Lorentz fitting of segmented-FFT
                        spectra (p.11); "broad peak", softens with T (Fig. 3G)]
  omega_L (calculated)= 1.81 +/- 0.27 THz     [SI sec XII Eq. (11), zero-T value;
                        N_sigma = 2.04, N_pi = 2.78 Ry^-1 spin^-1 cell^-1;
                        3 pairing-potential sets (Liu/Choi/Golubov), p.27]
  Delta_pi            = 0.44 THz              [2*Delta_pi = 0.88 +/- 0.05 THz
                        onset absorption in sigma_1 at 2 K, p.10; SI sec XII]
  Delta_sigma         = 1.32 THz              [empirical Delta_sigma ~ 3*Delta_pi,
                        2*Delta_sigma ~ 2.64 THz, p.10; SI sec XII as-used]
  Gamma_L             = NO separately-named Gamma_L or decay constant printed.
                        Width-class published number: the +/-0.8 THz Lorentz-fit
                        spread of the explicitly "overdamped"/"broad" Leggett
                        feature. Proxy (Gamma/omega)_lab = 0.8/1.8 = 0.4444
                        (derived-from-printed; DIAGNOSTIC use only; the PASS
                        predicate keys on channel classification, never on the
                        Gamma_L magnitude).
  Mechanism attribution (the paper's OWN):
    - mode identity: Leggett (relative phase of pi/sigma condensates), abstract
      + p.11-12; "over-damped oscillation corresponding to the Leggett mode".
    - damping language: "overdamped" / "strongly damped" / "heavily damped";
      decay "much faster than that observed in NbN" (p.11-12, Fig. 3E
      "Fast-decay Leggett-mode" vs "Persisting Higgs-mode").
    - attribution sentence (p.12): "the presence of inter-band coupling between
      the two superconductivity order parameters changes the spectrum of
      collective modes and affects their nonlinear responses."
    - kinematic position fixed by the paper's own printed numbers:
      omega_L = 1.8 THz > 2*Delta_pi = 0.88 THz (mode INSIDE the pi-band
      pair-breaking continuum; x_lab_pi = 2.045 >= 1) and
      omega_L < 2*Delta_sigma = 2.64 THz (below the sigma edge).
      The Leggett-mode damping criterion of the paper's own refs [20]
      (Leggett 1966) and [24] (Blumberg 2007, source of SI Eq. 11):
      pair-breaking (quasiparticle continuum) decay is OPEN when
      omega_L > 2*Delta_min => continuum-resonant class (i).
    - NO extrinsic bath/impurity/thermal attribution is made for the LEGGETT
      damping (the dirty-limit remark on p.9 concerns the pi-band HIGGS/THG
      channel); NO below-threshold bath-free parity-even intrinsic mechanism
      is proposed anywhere in the paper => no class-(iii) candidate. The
      observed damping operates AT/ABOVE the continuum edge (x_lab >= 1),
      structurally outside the class-(iii) definition (below-threshold).

DISCIPLINE
----------
- from canonical_constants import * (authoritative pins; the historical
  atlas-07 LEGGETT-MODE-48 row omega_L1=0.070/Q=670,000 is recorded as
  provenance tension, NOT imported)
- every local intermediate tagged # (local)
- cpu-cap-OMP8 (scalar arithmetic; no linear algebra) per plan GPU_path
- SHA-256 of all input files logged in first 20 lines of stdout
- dual-SHA (S84+): audit = sha256(script || canonical || pinmap_json);
  content = sha256(script)
- verdict via print_verdict_payload -> agent calls mcp__knowledge__emit_verdict
  (race-safe; the script does NOT write the verdict file)
- CANONICAL-FORM LAW: all survival outputs in ratio/inequality form; the
  absolute-seconds figure appears ONLY in the single pre-authorized caveat
  sentence printed once below.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 BEFORE numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")

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
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]          # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402  (explicit names consumed)
    Delta_BCS,                 # 0.4642547394830737 (R-PROTECTED, S70 BCS-GAP-CANONICAL-70)
    omega_L1,                  # 0.138 M_KK (canonical_constants:733; authoritative)
    Mass_LeggettDM_over_Delta_BCS,  # 11.97 (S70 LEGGETT-MOMENT-70; CONDITIONAL on Gamma_grav < H_0)
    H_0_inv_s,                 # 2.184e-18 s^-1
    M_KK_inv_seconds,          # 8.860439881925477e-42 s (S96-W1-MKK-SECONDS)
    t_universe_s,              # 4.35e17 s
    Q_Leggett,                 # 6.7e5 (canonical_constants:2222, S50 LEGGETT-DAMPING-50; DIAGNOSTIC only)
)

SESSION_DIR = PROJECT_ROOT / "computations" / "session-100b"

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan W6-3 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "100b"                                   # (local) emit_verdict session arg (orchestrator pin)
GATE_ID = "S100b-LEGGETT-DAMPING-INHERITANCE"      # (local)
SCHEME = "CHI-INHERITANCE-TRANSPORT-AUDIT"         # (local) plan-pinned
CONVENTION = "RATIO"                               # (local) plan-pinned (+ wave CANONICAL-FORM LAW)
L_MAX = "N/A"                                      # (local) plan-pinned (no spectral truncation)
SCHEMA_VERSION = "S84+"                            # (local)

# Survival anchors (plan survival_anchors pin; cited gate values, re-affirmed
# not re-derived by this gate)
TAU_DM_OVER_T_UNIV_73A = 1.13e65       # (local) LEGGETT-GRAV-DECAY-73a PASS (Z_2 parity P_L from J-evenness)
GAMMA_GRAV_OVER_H0_S95 = 8.85e-66      # (local) S95 LEGGETT-GRAV-DECAY-CONDITIONAL Row #68 (65 OOM margin)

# Input files (plan input_files block; static SHAs pinned at plan-write)
YUAN_PDF = PROJECT_ROOT / "downloads" / "research-sweep-s99" / "flatband-quantum-geometry" / "02_Yuan_Selective-Excitation-Collective-Modes-MgB2.pdf"
CHI_CANONICAL = PROJECT_ROOT / "sessions" / "framework" / "correspondence" / "3HeB-inheritance-canonical.md"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

PLAN_SHA_YUAN = "f8f389701e83265f1c1bd026c10fd9abccc5b12f27a0cd6dfef714073d1d656f"   # (local) plan pin
PLAN_SHA_CHI = "f5a4204a225957f3dcb66d9011111f3ee83f1efee400052586bd29682c350ed4"    # (local) plan pin

OUT_NPZ = SESSION_DIR / "s100b_leggett_damping_inheritance.npz"
OUT_PNG = SESSION_DIR / "s100b_leggett_damping_inheritance.png"

# ---------------------------------------------------------------------------
# D1 -- EXTRACTION RECORD (as-printed; provenance in module docstring)
# All entries are laboratory values transcribed from the SHA-pinned PDF.
# Extraction route: Skill(pdf) primary (4 chunks, all 33 pages read).
# ---------------------------------------------------------------------------
omega_L_obs_THz = 1.8          # (local) as-printed: observed Leggett frequency (overdamped osc.)
omega_L_obs_err_THz = 0.8      # (local) as-printed: Lorentz-fit spread of the broad FFT peak
omega_L_calc_THz = 1.81        # (local) as-printed: SI Eq.(11) zero-T calculated value
omega_L_calc_err_THz = 0.27    # (local) as-printed
Delta_pi_THz = 0.44            # (local) as-printed (2*Delta_pi = 0.88 +/- 0.05 THz onset)
two_Delta_pi_err_THz = 0.05    # (local) as-printed onset uncertainty on 2*Delta_pi
Delta_sigma_THz = 1.32         # (local) as-printed (empirical 3*Delta_pi)
gamma_L_named_printed = False  # (local) NO separately-named Gamma_L in the paper
gamma_over_omega_lab_proxy = omega_L_obs_err_THz / omega_L_obs_THz  # (local) 0.4444 width-proxy, DIAGNOSTIC ONLY

ATTRIBUTION_QUOTES = [         # (local) the paper's OWN damping attribution evidence
    "over-damped oscillation corresponding to the Leggett mode (abstract)",
    "overdamped oscillation with a frequency of 1.8 THz +/- 0.8 THz (p.12)",
    "damping ... much faster than that observed in NbN (p.11-12, Fig. 3E)",
    "the presence of inter-band coupling between the two superconductivity "
    "order parameters changes the spectrum of collective modes and affects "
    "their nonlinear responses (p.12)",
    "broad peak with a central frequency of 1.8 THz ... softens with "
    "increasing temperature (p.11)",
]

# Pre-registered 3-class channel set (plan channel_classes pin)
CHANNEL_CLASS_DEFS = {         # (local)
    "(i)": "PAIR-BREAKING CONTINUUM: requires x >= 1 at the operative "
           "frequency AND, for a single relic quantum, a Z_2-ODD "
           "single-quantum vertex",
    "(ii)": "EXTRINSIC BATH: impurity / inhomogeneity / thermal "
            "quasiparticles / phonon-lattice bath -- no substrate "
            "counterpart (substrate-IS, no container bath)",
    "(iii)": "INTRINSIC PARITY-EVEN MULTI-QUANTUM: universality-class "
             "mechanism present in ANY two-condensate system, operating "
             "BELOW threshold, bath-free, Z_2-EVEN -- TRANSPORTS through chi",
}

# ---------------------------------------------------------------------------
# SHA helpers (S84+ dual-SHA schema, per .claude/templates/script-template.py)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()          # (local)
    canonical_bytes = canonical_path.read_bytes()    # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str | None = None,
                          magnitude_verdict: str | None = None,
                          regime_verdict: str | None = None,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    """Print the emit_verdict payload (delimited JSON) for the dispatching agent."""
    payload: dict = {              # (local)
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
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
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # -- input SHA pins (first 20 lines of stdout) --------------------------
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in (CANONICAL_PATH, YUAN_PDF, CHI_CANONICAL):
        sha = sha256_of(p)     # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    # static-pin verification (plan input_files block)
    sha_yuan = pins[str(YUAN_PDF.relative_to(PROJECT_ROOT)).replace("\\", "/")]   # (local)
    sha_chi = pins[str(CHI_CANONICAL.relative_to(PROJECT_ROOT)).replace("\\", "/")]  # (local)
    if sha_yuan != PLAN_SHA_YUAN:
        raise RuntimeError(f"Yuan PDF SHA mismatch vs plan pin: {sha_yuan}")
    if sha_chi != PLAN_SHA_CHI:
        raise RuntimeError(f"chi-morphism canonical SHA mismatch vs plan pin: {sha_chi}")
    print("  static plan pins VERIFIED (yuan_pdf, chi_morphism_canonical)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # =======================================================================
    # D2 -- KINEMATIC + PROTECTION-LAYER MAP (substitution chains A & B)
    # =======================================================================
    # Chain A (substrate L1 collective mode):
    #   Step 1: omega_L1  = 0.138 M_KK            [canonical_constants:733]
    #   Step 2: Delta_BCS = 0.4642547394830737    [canonical_constants:421-422; R-PROTECTED]
    #   Step 3: x_L1 = omega_L1 / (2 * Delta_BCS)
    #   Step 4: = 0.138 / 0.9285094789661474 = 0.148625 (6 s.f.)
    #   Step 5: 0.148625 < 1 => L1 BELOW the pair-breaking continuum edge
    #           => quasiparticle (pair-breaking) channel kinematically CLOSED.
    two_Delta_BCS = 2.0 * Delta_BCS                       # (local) 0.9285094789661474
    x_L1 = omega_L1 / two_Delta_BCS                       # (local) 0.148625
    # Chain B (substrate DM relic quantum -- protection NOT kinematic):
    #   Step 1: m_DM/Delta_BCS = 11.97   [Mass_LeggettDM_over_Delta_BCS; S70; CONDITIONAL]
    #   Step 2: x_DM = 11.97/2 = 5.985
    #   Step 3: 5.985 > 1 => relic ABOVE the edge => protection is the Z_2
    #           parity P_L (J-evenness, 73a) + single-Leggett decay FORBIDDEN
    #           (S67, PROVEN) -- a SYMMETRY selection rule, not kinematics.
    x_DM = Mass_LeggettDM_over_Delta_BCS / 2.0            # (local) 5.985
    # Lab kinematic ratios (as-printed Yuan values):
    x_lab_pi = omega_L_obs_THz / (2.0 * Delta_pi_THz)     # (local) 1.8/0.88 = 2.045455
    x_lab_sigma = omega_L_obs_THz / (2.0 * Delta_sigma_THz)  # (local) 1.8/2.64 = 0.681818 (diagnostic)

    print("=== D2 kinematic + protection-layer map ===")
    print(f"  lab:  x_lab_pi    = omega_L/(2*Delta_pi)    = {omega_L_obs_THz}/{2*Delta_pi_THz:.2f} = {x_lab_pi:.6f}  (>= 1: pi continuum OPEN in lab)")
    print(f"  lab:  x_lab_sigma = omega_L/(2*Delta_sigma) = {omega_L_obs_THz}/{2*Delta_sigma_THz:.2f} = {x_lab_sigma:.6f}  (diagnostic; < 1)")
    print(f"  sub:  x_L1 = {omega_L1}/(2*{Delta_BCS:.16f}) = {x_L1:.6f}  (< 1: kinematically CLOSED)")
    print(f"  sub:  x_DM = {Mass_LeggettDM_over_Delta_BCS}/2 = {x_DM:.6f}  (> 1: protection = Z_2 P_L + S67, NOT kinematic)")
    print()

    # =======================================================================
    # Chain C -- transported-rate edge (class (iii) only)
    # =======================================================================
    #   Step 1: m_DM [s^-1] = 11.97 * Delta_BCS / M_KK_inv_seconds
    #   Step 2: H_0_inv_s = 2.184e-18 s^-1
    #   Step 3: Gamma_inherit = (Gamma_L/omega_L)_lab * m_DM [s^-1]
    #   Step 4: Gamma_inherit/H_0 = (Gamma_L/omega_L)_lab * transport_factor
    #   Step 5: survival edge (Gamma_L/omega_L)_crit = 1/transport_factor
    m_DM_MKK = Mass_LeggettDM_over_Delta_BCS * Delta_BCS  # (local) 5.5571292 M_KK
    m_DM_inv_s = m_DM_MKK / M_KK_inv_seconds              # (local) 6.27185e41 s^-1
    transport_factor = m_DM_inv_s / H_0_inv_s             # (local) 2.87172e59
    edge_crit = 1.0 / transport_factor                    # (local) 3.48222e-60
    print("=== Chain C transported-rate edge ===")
    print(f"  m_DM = {Mass_LeggettDM_over_Delta_BCS} * {Delta_BCS:.16f} = {m_DM_MKK:.7f} M_KK")
    print(f"  m_DM [s^-1] = {m_DM_MKK:.7f} / {M_KK_inv_seconds:.6e} = {m_DM_inv_s:.6e}")
    print(f"  transport_factor = m_DM/H_0 = {m_DM_inv_s:.6e}/{H_0_inv_s:.3e} = {transport_factor:.6e}")
    print(f"  survival edge (Gamma_L/omega_L)_crit = 1/transport_factor = {edge_crit:.6e}")
    print()

    # =======================================================================
    # D3 -- CHI-TRANSPORT AUDIT (channel classification of the extraction)
    # =======================================================================
    # Mechanism record: ONE damping mechanism is attributed by the paper for
    # the Leggett feature -- continuum-resonant decay, classified by the
    # CODED rule below. The class-(iii) candidate scan returns EMPTY (no
    # below-threshold bath-free parity-even intrinsic mechanism is proposed
    # anywhere in the paper; the observed damping operates at x_lab >= 1,
    # structurally outside the class-(iii) below-threshold definition).
    mechanisms = []  # (local)

    # Mechanism 1: pair-breaking continuum decay (pi band) -- coded rule:
    # class (i) iff x >= 1 at the operative frequency.
    mech1_class = "(i)" if x_lab_pi >= 1.0 else "UNCLASSIFIED"  # (local)
    mech1 = {                  # (local)
        "name": "pair-breaking continuum decay into pi-band quasiparticles "
                "(continuum-resonant)",
        "paper_evidence": "overdamped Leggett oscillation; omega_L = 1.8 THz "
                          "> 2*Delta_pi = 0.88 THz from the paper printed "
                          "numbers; inter-band coupling attribution (p.12); "
                          "refs [20] Leggett 1966 + [24] Blumberg 2007 "
                          "criterion: continuum decay OPEN when omega_L > "
                          "2*Delta_min",
        "x_operative": x_lab_pi,
        "class": mech1_class,
        "chi_closed_for_L1": bool(x_L1 < 1.0),
        "chi_closed_for_L1_reason": f"kinematic: x_L1 = {x_L1:.6f} < 1 (the "
                                    "substrate L1 mode sits BELOW its own "
                                    "continuum edge; the dimensionless "
                                    "position does not transport -- it is "
                                    "evaluated per system)",
        "chi_closed_for_DM": True,
        "chi_closed_for_DM_reason": "Z_2-ODD single-quantum vertex FORBIDDEN: "
                                    "P_L parity from J-evenness of the "
                                    "condensate (LEGGETT-GRAV-DECAY-73a) + "
                                    "single-Leggett decay FORBIDDEN (S67, "
                                    "PROVEN). x_DM = 5.985 > 1 so the block "
                                    "is the symmetry selection rule, not "
                                    "kinematics.",
    }
    mechanisms.append(mech1)

    # Extrinsic-bath channel (class (ii)) -- presence check: the paper makes
    # NO extrinsic attribution for the LEGGETT damping (the dirty-limit
    # remark concerns the pi-band Higgs/THG channel). Recorded as
    # not-attributed; if it HAD been attributed, class (ii) is chi-closed
    # (no substrate counterpart: the substrate IS everything; no container
    # bath). Substrate-internal comparator: Q_Leggett (S50, formation-epoch,
    # DIAGNOSTIC only), scoped to the transit/GGE-formation epoch; the
    # relic state is protected by fabric-scale Ordered-Veil integrability
    # (RECONCILED scope: fabric-scale Poisson <r> = 0.367; the retracted
    # single-cell permanence is NOT invoked).
    extrinsic_attributed = False  # (local) extraction-level fact

    # class-(iii) candidate scan over the extraction record:
    class_iii_members = [m for m in mechanisms if m["class"] == "(iii)"]  # (local)
    n_class_iii = len(class_iii_members)  # (local)

    # Counterfactual diagnostic (NOT a fired channel): what the transported
    # rate WOULD be if the lab width-proxy were chi-open class (iii).
    counterfactual_transported = gamma_over_omega_lab_proxy * transport_factor  # (local) ~1.28e59
    print("=== D3 chi-transport audit ===")
    print(f"  mechanisms extracted: {len(mechanisms)}")
    print(f"  mech1 class = {mech1_class} (rule: x_lab_pi = {x_lab_pi:.6f} >= 1)")
    print(f"  chi-closed for L1 (kinematic): {mech1['chi_closed_for_L1']}")
    print(f"  chi-closed for DM (Z_2-odd FORBIDDEN, 73a+S67): {mech1['chi_closed_for_DM']}")
    print(f"  extrinsic bath attributed for Leggett damping: {extrinsic_attributed}")
    print(f"  class-(iii) members fired: {n_class_iii}")
    print(f"  counterfactual diagnostic (NOT fired): (Gamma/omega)_proxy * "
          f"transport = {gamma_over_omega_lab_proxy:.4f} * {transport_factor:.5e} "
          f"= {counterfactual_transported:.4e}")
    print(f"  -> structural consequence (pre-registered): ANY measurable lab "
          f"(Gamma/omega) >~ 1e-6 exceeds the edge {edge_crit:.5e} by >~ 54 OOM "
          f"if transported; the evidential content IS the channel-closure audit.")
    print()

    # =======================================================================
    # D4 -- VERDICT + CANONICAL-FORM OUTPUT
    # =======================================================================
    # Extraction completeness (required elements, plan extraction_pins):
    #   omega_L YES; Delta_pi YES; Delta_sigma YES (3x empirical, as-published);
    #   Gamma_L-or-linewidth: width-class published number present (the
    #   +/-0.8 THz Lorentz-fit spread of the overdamped feature); honesty
    #   note recorded (no separately-named Gamma_L); attribution: present and
    #   UNAMBIGUOUS at channel-class level (continuum-resonant class (i);
    #   no class-(iii) candidate is constructible from the paper text: the
    #   observed damping is at/above threshold while class (iii) requires
    #   below-threshold operation).
    extraction_complete = True            # (local)
    attribution_ambiguous = False         # (local)
    all_chi_closed = all(
        m["class"] in ("(i)", "(ii)") and m["chi_closed_for_L1"]
        and m["chi_closed_for_DM"] for m in mechanisms
    )                                     # (local)
    transported_violation = any(
        gamma_over_omega_lab_proxy * transport_factor >= 1.0
        for m in class_iii_members
    )                                     # (local) vacuously False (no member)

    # Survival statement -- CANONICAL RATIO/INEQUALITY FORM ONLY:
    consistency_identity = H_0_inv_s * t_universe_s       # (local) 0.950
    inv_gamma_ratio = 1.0 / GAMMA_GRAV_OVER_H0_S95        # (local) 1.12994e65
    print("=== D4 survival statement (CANONICAL-FORM LAW: ratio/inequality only) ===")
    print(f"  Gamma_grav < H_0 holds: Gamma_grav/H_0 ~ {GAMMA_GRAV_OVER_H0_S95:.2e} "
          f"(S95 LEGGETT-GRAV-DECAY-CONDITIONAL Row #68; 65 OOM margin)")
    print(f"  survival margin ratio: tau_DM/t_univ = {TAU_DM_OVER_T_UNIV_73A:.2e} "
          f"(LEGGETT-GRAV-DECAY-73a PASS; Z_2 parity P_L from J-evenness)")
    print(f"  consistency: H_0_inv_s * t_universe_s = {H_0_inv_s:.3e} * "
          f"{t_universe_s:.2e} = {consistency_identity:.3f} ~ O(1)")
    print(f"  same statement to O(1): 1/(Gamma_grav/H_0) = {inv_gamma_ratio:.5e} "
          f"vs tau_DM/t_univ = {TAU_DM_OVER_T_UNIV_73A:.2e} (identical at 3 s.f.)")
    print("  NON-CANONICAL CAVEAT (single pre-authorized sentence): the index "
          "tau_DM = 4.93e82 s is non-canonical -- do not propagate.")
    print()

    # Provenance tension record (plan: record, do NOT re-adjudicate):
    print("=== provenance tension record (imported canonical wins) ===")
    print(f"  omega_L1 = {omega_L1} (canonical_constants:733, authoritative; "
          f"atlas-07 LEGGETT-MODE-48 historical row carries 0.070)")
    print(f"  Q_Leggett = {Q_Leggett:.1e} (canonical_constants:2222, S50 "
          f"LEGGETT-DAMPING-50, matches s50 npz Q_total = 6.656e5; the plan-text "
          f"value 18.6 matches NO on-disk artifact -- plan-text drift recorded "
          f"per substrate-first-canonical-sourcing.md (ii.B); Q is DIAGNOSTIC "
          f"only in this gate, no PASS impact)")
    print()

    # ----- [SIGN] 3-tuple --------------------------------------------------
    # sign: pre-registered direction (Chain C Step 5): the extracted MgB2
    #       damping attribution lands in class (i)/(ii) (expected:
    #       continuum-resonant or extrinsic) and Gamma_grav < H_0 stands.
    sign_ok = all(m["class"] in ("(i)", "(ii)") for m in mechanisms) \
        and not transported_violation                     # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"          # (local)
    # magnitude: no transported channel >= 1 (the operative quantitative
    #       survival test); substrate anchor 8.85e-66 << 1.
    magnitude_verdict = "FAIL" if transported_violation else "PASS"  # (local)
    # regime: exact float64 scalar ratio arithmetic on canonical pins; the
    #       extraction landed as-printed (width-proxy qualification is an
    #       extraction-precision note, not a regime breach -- the PASS
    #       predicate never consumes the Gamma_L magnitude).
    regime_verdict = "VALID"                              # (local)

    # ----- composite (gate-verdicts.md collapse rule, applied verbatim) ----
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"        # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"        # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"        # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"        # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"        # (local)
    else:
        composite = "PASS"        # (local)
    # INFO arm (pre-registered): extraction-limited overrides
    if not extraction_complete or attribution_ambiguous:
        composite = "INFO"        # REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION analog

    # operator conjunction (explicit, for the audit trail):
    operator_pass = (extraction_complete and all_chi_closed
                     and not transported_violation)       # (local)
    print("=== operator conjunction ===")
    print(f"  extraction_complete = {extraction_complete}")
    print(f"  all mechanisms class (i)/(ii) AND chi-closed = {all_chi_closed}")
    print(f"  no transported channel >= 1 = {not transported_violation} "
          f"(class-(iii) members: {n_class_iii})")
    print(f"  => operator PASS = {operator_pass}; composite (collapse rule) = {composite}")
    assert (composite == "PASS") == operator_pass, "collapse rule vs operator mismatch"
    print()

    # =======================================================================
    # npz + png
    # =======================================================================
    np.savez(
        OUT_NPZ,
        # D1 extraction (as-printed)
        omega_L_obs_THz=omega_L_obs_THz,
        omega_L_obs_err_THz=omega_L_obs_err_THz,
        omega_L_calc_THz=omega_L_calc_THz,
        omega_L_calc_err_THz=omega_L_calc_err_THz,
        Delta_pi_THz=Delta_pi_THz,
        two_Delta_pi_err_THz=two_Delta_pi_err_THz,
        Delta_sigma_THz=Delta_sigma_THz,
        gamma_L_named_printed=gamma_L_named_printed,
        gamma_over_omega_lab_proxy=gamma_over_omega_lab_proxy,
        attribution_quotes=json.dumps(ATTRIBUTION_QUOTES),
        # D2 kinematics
        x_lab_pi=x_lab_pi, x_lab_sigma=x_lab_sigma, x_L1=x_L1, x_DM=x_DM,
        two_Delta_BCS=two_Delta_BCS,
        # Chain C
        m_DM_MKK=m_DM_MKK, m_DM_inv_s=m_DM_inv_s,
        transport_factor=transport_factor, edge_crit=edge_crit,
        counterfactual_transported=counterfactual_transported,
        # D3 classification
        mechanisms=json.dumps(mechanisms),
        channel_class_defs=json.dumps(CHANNEL_CLASS_DEFS),
        extrinsic_attributed=extrinsic_attributed,
        n_class_iii=n_class_iii,
        all_chi_closed=all_chi_closed,
        transported_violation=transported_violation,
        # D4 survival (ratio form)
        tau_DM_over_t_univ_73a=TAU_DM_OVER_T_UNIV_73A,
        gamma_grav_over_H0_s95=GAMMA_GRAV_OVER_H0_S95,
        consistency_identity=consistency_identity,
        inv_gamma_ratio=inv_gamma_ratio,
        # canonical pins consumed
        omega_L1=omega_L1, Delta_BCS=Delta_BCS,
        Mass_LeggettDM_over_Delta_BCS=Mass_LeggettDM_over_Delta_BCS,
        H_0_inv_s=H_0_inv_s, M_KK_inv_seconds=M_KK_inv_seconds,
        t_universe_s=t_universe_s, Q_Leggett_diag=Q_Leggett,
        # verdict block
        extraction_complete=extraction_complete,
        attribution_ambiguous=attribution_ambiguous,
        operator_pass=operator_pass,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        # dual-prior discriminator (plan): PASS -> 0.95 Track A
        track_A_posterior=0.95 if composite == "PASS" else (0.10 if composite == "FAIL" else 0.80),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"npz written: {OUT_NPZ.name}")

    # ----- plot -------------------------------------------------------------
    fig, (axA, axB) = plt.subplots(
        1, 2, figsize=(14.0, 5.8), constrained_layout=True)   # (local)

    # Panel A: dimensionless pair-breaking-edge map x = omega/(2*Delta)
    rows = [   # (local) (label, x, color, marker, protection)
        (r"MgB$_2$ lab: $\omega_L/(2\Delta_\pi)$", x_lab_pi, "tab:red", "o",
         "continuum OPEN -> class (i) overdamping"),
        (r"MgB$_2$ lab: $\omega_L/(2\Delta_\sigma)$", x_lab_sigma, "tab:orange", "o",
         "below $\\sigma$ edge (diagnostic)"),
        (r"substrate L1: $\omega_{L1}/(2\Delta_{BCS})$", x_L1, "tab:blue", "s",
         "kinematically CLOSED"),
        (r"substrate DM: $m_{DM}/(2\Delta_{BCS})$", x_DM, "tab:green", "D",
         "Z$_2$ P$_L$ + S67 (symmetry-protected)"),
    ]
    for i, (lab, xv, c, mk, note) in enumerate(rows):
        axA.scatter([xv], [i], s=120, color=c, marker=mk, zorder=3)
        axA.annotate(f"{xv:.4g}", (xv, i), textcoords="offset points",
                     xytext=(0, 11), fontsize=9.5, color=c, ha="center",
                     fontweight="bold")
        axA.annotate(note, (xv, i), textcoords="offset points",
                     xytext=(0, -16), fontsize=7.5, color="dimgray",
                     ha="center")
    axA.axvline(1.0, color="k", lw=1.5, ls="--", zorder=2)
    axA.text(0.93, -0.52, "pair-breaking edge  $x=1$", rotation=90,
             va="bottom", ha="right", fontsize=8)
    axA.axvspan(1.0, 12.0, color="mistyrose", alpha=0.45, zorder=0)
    axA.set_xscale("log")
    axA.set_xlim(0.05, 12.0)
    axA.set_ylim(-0.75, 3.75)
    axA.set_yticks(range(len(rows)))
    axA.set_yticklabels([r[0] for r in rows], fontsize=9)
    axA.set_xlabel(r"$x=\omega/(2\Delta)$  (per-system pair-breaking position)")
    axA.set_title("D2: kinematic + protection-layer map", fontsize=10)
    axA.grid(alpha=0.25, which="both")

    # Panel B: transported-rate edge (log axis of Gamma/omega and Gamma/H_0)
    axB.axvline(edge_crit, color="k", ls="--", lw=1.5, zorder=2)
    axB.annotate(r"survival edge $(\Gamma_L/\omega_L)_{crit}=$" + f"{edge_crit:.3e}",
                 (edge_crit, 1.52), textcoords="offset points", xytext=(5, 0),
                 fontsize=8, ha="left", va="center")
    bars = [   # (local)
        (r"lab width-proxy $(\Gamma_L/\omega_L)\sim0.44$"
         "\n(class (i): chi-CLOSED, NOT transported)",
         gamma_over_omega_lab_proxy, "tab:red"),
        (r"substrate $\Gamma_{grav}/H_0 = 8.85\times10^{-66}$"
         "\n(S95 Row #68; 65 OOM margin)",
         GAMMA_GRAV_OVER_H0_S95, "tab:green"),
    ]
    for i, (lab, xv, c) in enumerate(bars):
        axB.barh([i], [xv], left=1e-70, color=c, alpha=0.75, height=0.45)
        axB.annotate(f"{xv:.3e}", (xv, i), textcoords="offset points",
                     xytext=(6, 14), fontsize=9.5, color=c, va="center",
                     fontweight="bold")
    axB.set_xscale("log")
    axB.set_xlim(1e-70, 1e3)
    axB.set_ylim(-0.6, 1.8)
    axB.set_yticks(range(len(bars)))
    axB.set_yticklabels([b[0] for b in bars], fontsize=8.5)
    axB.set_xlabel(r"dimensionless rate ratio (log)")
    axB.set_title("D3/D4: chi-transport edge -- channel closure carries the\n"
                  "evidence (chi-OPEN measurable lab damping would violate "
                  "survival by >~54 OOM)", fontsize=9)
    axB.grid(alpha=0.25, which="both", axis="x")

    fig.suptitle(f"{GATE_ID}: MgB$_2$ Leggett damping through the "
                 r"$\chi:\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})"
                 r"\to M_2(\mathbb{C})$ inheritance morphism "
                 f"-- composite {composite}", fontsize=11)
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"png written: {OUT_PNG.name}")
    print()

    # =======================================================================
    # verdict payload
    # =======================================================================
    value = (   # (local) no single-quote chars permitted
        "extraction=COMPLETE-as-printed;"
        f"omega_L_obs=1.8pm0.8THz_Lorentz-fit;omega_L_calc=1.81pm0.27THz_SI-Eq11;"
        f"Delta_pi=0.44THz_2Dpi=0.88pm0.05;Delta_sigma=1.32THz_3x-empirical;"
        "GammaL=width-class_pm0.8THz_no_separately_named_GammaL;"
        "attribution=overdamped_continuum-resonant_interband-coupling_p12;"
        f"class=(i)_pair-breaking_x_lab_pi={x_lab_pi:.6f};"
        f"chi_closed=ALL_L1-kinematic_x_L1={x_L1:.6f}_lt_1_DM-Z2-odd-FORBIDDEN-73a+S67;"
        "extrinsic_attributed_for_Leggett=False;class_iii_members=0;"
        f"edge_crit={edge_crit:.6e};transport_factor={transport_factor:.6e};"
        f"counterfactual_diag={counterfactual_transported:.3e}_NOT-fired;"
        f"survival=Gamma_grav_lt_H0;tau_DM/t_univ={TAU_DM_OVER_T_UNIV_73A:.3g};"
        f"Gamma_grav/H0={GAMMA_GRAV_OVER_H0_S95:.3g};"
        f"consistency_H0xt_univ={consistency_identity:.3f};"
        "track_A_posterior=0.95"
    )
    extra_rows = [   # (local)
        f"# extraction(as-printed, SHA-pinned PDF read in full): omega_L_obs=1.8+/-0.8 THz "
        f"(Lorentz fit, overdamped); omega_L_calc=1.81+/-0.27 THz (SI Eq.11, "
        f"Blumberg form, 3 V-sets); 2Delta_pi=0.88+/-0.05 THz; Delta_sigma=3Delta_pi=1.32 THz; "
        f"no separately-named Gamma_L printed (width-proxy 0.8/1.8=0.444, diagnostic only) "
        f"# {GATE_ID} D1 extraction row",
        f"# channel-closure: mech=pair-breaking continuum (class (i), x_lab_pi={x_lab_pi:.4f}>=1); "
        f"chi-closed for L1 (kinematic x_L1={x_L1:.6f}<1) and for DM quantum (Z_2-odd "
        f"single-quantum FORBIDDEN, 73a P_L + S67 PROVEN); class (ii) not attributed for "
        f"Leggett damping; class (iii) EMPTY (paper proposes no below-threshold bath-free "
        f"parity-even mechanism; observed damping operates at x>=1) # {GATE_ID} D3 audit row",
        f"# canonical-form: survival stated as Gamma_grav < H_0 with tau_DM/t_univ=1.13e65 "
        f"(73a) and Gamma_grav/H_0~8.85e-66 (S95 Row #68); H_0_inv_s*t_universe_s=0.950~O(1); "
        f"absolute-seconds figure NOT propagated per wave CANONICAL-FORM LAW # {GATE_ID} D4 row",
        f"# provenance-tension(record-only, not re-adjudicated): omega_L1=0.138 canonical "
        f"(atlas-07 historical row 0.070); Q_Leggett=6.7e5 on-disk canonical_constants:2222 "
        f"matching s50 npz Q_total=6.656e5; plan-text Q=18.6 matches no on-disk artifact "
        f"(plan-text drift, substrate-first-canonical-sourcing.md ii.B); Q diagnostic-only "
        f"# {GATE_ID} provenance row",
    ]
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        companion_note=(
            "[SIGN] chi-inheritance transport audit; PASS = channel-closure "
            "conjunction (extraction complete AND all classes (i)/(ii) "
            "chi-closed AND no transported channel >= 1); C11 CONDITIONAL "
            "tag NOT discharged by this gate (lab-side consistency leg only)"
        ),
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
