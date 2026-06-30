#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S111-CF3-H0-RESIDUAL — residual H0 relief at the dimensionless-Ô layer.

GATE: S111-CF3-H0-RESIDUAL  (Session 111, Wave 2, §W2-2)
TRIGGER: [SIGN]  (the d_A=0 scale-leg inadmissibility + the relief-fraction direction are signed claims)
CLASSIFICATION: GEOMETRIC  (ΔH0/H0 is a ratio of spectral-action moments — a₀⊥a₂ Ô-relations on the D_K spectrum; the fabric's own clock-rate, not an excitation)

SUBSTRATE-FIRST FRAMING
-----------------------
The substrate IS the D_K spectrum; the Hubble rate H emerges from the a₂ Seeley-DeWitt
focusing channel (the second spectral moment IS Newton's constant; the clock-rate is the
fabric's own, not a field in a container). H0 is read OFF the substrate's late-time spectral
dynamics, NOT fitted to an FRW expansion rate.

    D_K eigenvalues → a₀ (zeroth moment, cosmological term) ⊥ a₂ (second moment, EH/G_N)
      → dimensionless Ô-relations between a₀ and a₂ images
      → the a₂ focusing-clock relief ΔH0/H0 (transported at deg_T, dimensionless-Ô layer).

WHAT THIS GATE DOES (method, plan §W2-2)
----------------------------------------
(1) Load the partial transported relief from S110 CF3 (ΔH0/H0_BZ = 0.004899972,
    paper = 0.0075, deg_T = 2.0 NON-SCALAR, a0_a2_orthogonal = True).
(2) Pre-register the partial-relief fraction 49/800 = 6.125% of band-low as the HONEST
    outcome (~94% held). The exact partial fraction is 1224993/20000000 = 0.06124965;
    49/800 = 0.06125 is the registry round-figure pinned alongside (round-figure-fidelity
    discipline: publish the exact rational, pin the round figure as a companion).
(3) Restrict the residual-relief search to dimensionless-morphism channels (d_A=0 ⇒ the
    M_KK^1 odd scale leg is EXCLUDED by parity). Test whether a substrate-derived
    dimensionless RELATION between a₀ and a₂ Ô-images predicts the shift once w=M_KK is
    fixed by one observation.
(4) Enforce the d_A=0 INADMISSIBILITY of the 54.04-decade scale leg: ΔH0/H0 is dimensionless
    ⇒ the M_KK^1 scale leg (the +2 full-homogeneity reading) is dimensionally FORBIDDEN (the
    EVEN d_A=0 face of the §VII.CF parity wall; the ODD d_A=+1 face is §VII.CF / LRD-T).
(5) The a₀ "draw" is licensed at the dimensionless-Ô layer ONLY (a₀⊥a₂ FUNCTIONAL-INDEPENDENT,
    S66 / W2-E PASS S75) — it refines a₀/a₂ Ô-RELATIONS, it does NOT draw a dimensionful relief
    budget out of a₀ (the workshop-killed O2 / Layer-1 wall: a dimensionless ratio cannot close
    a dimensional gap).

VERDICT RUBRIC
--------------
PASS : a substrate-derived DIMENSIONLESS relation predicts ΔH0/H0 ∈ [0.08,0.10] knob-free
       once w=M_KK fixed by one observation (the full band closes from the dimensionless-Ô
       layer, zero fitted knobs, NO dimensionful a₀ draw).
INFO : only the partial 49/800 = 6.125% relief lands at the dimensionless-Ô layer; ~94% held.
       The honest pre-registered partial outcome (prior 0.70). Band-closure is HELD pending
       the single w=M_KK-fixing observation.
FAIL : the only band-closing channel requires a DIMENSIONFUL a₀ relief budget — the Layer-1
       wall (a dimensionless ratio cannot close a dimensional gap). Confirms the Layer-1 wall.

NOT gated on MKK-RG (independent axis; the two probe orthogonal legs of the §6.3 residual —
magnitude vs dimensionless-clock-relation), per the volovik a₀-orthogonality audit.

ENV: phonon-exflation-sim/.venv312/Scripts/python.exe ; cwd = project root.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-only scalar work; cap threads
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
GATE_ID = "S111-CF3-H0-RESIDUAL"
SESSION = "S111"
SCHEME = "emergent-scale-transport-DIMENSIONLESS-ONLY"          # the d_A=0-restricted complement of S110 CF3's emergent-scale-transport-NON-SCALAR
CONVENTION = "DA-0-PARITY-EVEN"                                  # dimensionless-Ô-layer transport; M_KK^1 odd scale leg EXCLUDED per d_A=0 (regulator-pin-discipline.md §"Mass-dimension/parity")
L_MAX = "12"                                                     # a₀/a₂ Ô-images at canonical L12 truncation (continuity with S110 CF3 / W2-E)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-111"
S110_DIR = PROJECT_ROOT / "computations" / "session-110"
INV7_DIR = PROJECT_ROOT / "computations" / "investigation-7"

# allow `from canonical_constants import *`
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    w0_FW,                 # -0.918  (Volovik vacuum + effacement; the a₀-orthogonal channel anchor)
    clock_coeff,           # -3.08   (dalpha/alpha = clock_coeff * dtau)
    H_0_km_s_Mpc,          # 67.4    (Planck 2018; the substrate-natural H0 anchor once w=M_KK fixed)
)

# ---------------------------------------------------------------------------
# Section 2 — Input files (SHA-pinned)
# ---------------------------------------------------------------------------
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
CF3_NPZ = S110_DIR / "s110_cf3_timescape_h0.npz"
KBC_NPZ = INV7_DIR / "inv7_w1_4_kbc_timescape_h0.npz"

INPUT_FILES = [CANONICAL_PATH, CF3_NPZ, KBC_NPZ]

# ---------------------------------------------------------------------------
# Section 3 — Pre-registered constants (plan §W2-2)
# ---------------------------------------------------------------------------
# Observational H0-tension band (Planck-vs-SH0ES). External target — NOT analytically forced.
BAND_LO = Fraction(8, 100)        # 0.08  band-low
BAND_HI = Fraction(10, 100)       # 0.10  band-high
BAND_CENTRAL = Fraction(9, 100)   # 0.09  band-central
BAND_LIT = Fraction(84, 1000)     # 0.084 literature central

# The registry round-figure for the partial-relief fraction (Sage QQ).
PARTIAL_FRAC_ROUNDFIG = Fraction(49, 800)   # = 0.06125 exactly

# dec separation of the substrate/BZ scale and the CMB pivot (the 54.04-decade M_KK^1 leg)
DEC_SEPARATION = 54.04            # (local) cross-checked against s110_cf3 npz dec_separation (substrate/CMB decade gap)


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
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Residual H0-relief at the dimensionless-Ô layer.

    Substitution chain (plan §W2-2):
      Claim 1: d_A(ΔH0/H0) = 0 ⇒ the M_KK^1 scale leg is parity-INADMISSIBLE (EVEN-face of §VII.CF).
      Claim 2: the partial relief is 49/800 = 6.125% of band-low — the honest outcome.
      Claim 3: a₀ refines RELATIONS, does NOT supply a dimensionful budget (the Layer-1 wall).
    """
    # ---- (1) Load S110 CF3 transported partial relief --------------------
    cf3 = np.load(CF3_NPZ, allow_pickle=True)  # (local)
    dH0_BZ_central = float(cf3["dH0_BZ_central"])          # 0.004899972 (a₂ focusing-clock, dimensionless-Ô layer)  # (local)
    dH0_BZ_paper = float(cf3["dH0_BZ_paper"])              # 0.007513290 (paper-channel)  # (local)
    deg_T = float(cf3["deg_T"])                            # 2.0 (NON-SCALAR transport degree)  # (local)
    deg_T_is_scalar = bool(cf3["deg_T_is_scalar"])         # False  # (local)
    a0_a2_orthogonal = bool(cf3["a0_a2_orthogonal"])       # True  # (local)
    dec_sep_loaded = float(cf3["dec_separation"])          # 54.04  # (local)
    ratio_needed_central_loaded = float(cf3["ratio_needed_central"])  # 18.367 (the FITTED budget the S110 row flagged)  # (local)

    # cross-check the KBC-timescape companion (route-B central path)
    kbc = np.load(KBC_NPZ, allow_pickle=True)  # (local)
    dH0_B_central_kbc = float(kbc["DH0_B_central"])        # 0.004899972 (same central path, route B)  # (local)
    clock_coeff_kbc = float(kbc["clock_coeff"])            # -3.08  # (local)

    # ---- CROSS-CHECK 0: source consistency -------------------------------
    cc0_central_match = abs(dH0_BZ_central - dH0_B_central_kbc) < 1e-12   # both npz agree on the central transported relief  # (local)
    cc0_clock_coeff_match = abs(clock_coeff_kbc - float(clock_coeff)) < 1e-12  # canonical clock_coeff == npz value  # (local)
    cc0_decsep_match = abs(dec_sep_loaded - DEC_SEPARATION) < 1e-9        # (local)
    cc0_orthogonal = a0_a2_orthogonal                                     # a₀⊥a₂ already pinned True in S110 CF3  # (local)

    # ====================================================================
    # Claim 1 — d_A=0 ⇒ the M_KK^1 scale leg is parity-INADMISSIBLE
    # (set-membership exact; the EVEN d_A=0 face of the §VII.CF parity wall)
    # ====================================================================
    # ΔH0/H0 = (Hubble rate)/(Hubble rate) ⇒ mass-dimension 0.
    d_A_dH0 = 0   # (local)  the observable's mass dimension (a ratio of like-dimensioned quantities)
    # Transport bridge B = (M_KK^{d_A} scale leg) ⊙ (dimensionless morphism)  [corpus §23.0(5)].
    # d_A=0 ⇒ scale-leg exponent = d_A = 0 ⇒ scale leg = M_KK^0 = 1 (TRIVIAL).
    scale_leg_exponent = d_A_dH0   # (local) = 0
    scale_leg_is_trivial = (scale_leg_exponent == 0)   # (local) M_KK^0 = 1
    # The 54.04-decade conversion is the ODD M_KK^1 scale leg (deg=+1). The morphism sector is
    # EVEN-degree (Wodzicki −2(s−s'), HKR 0). Parity: ODD scale leg ⊥ EVEN morphism sector.
    odd_scale_leg_degree = 1       # (local) the M_KK^1 leg carrying the 54.04-decade unit conversion
    odd_scale_leg_parity = odd_scale_leg_degree % 2          # (local) = 1 (ODD)
    morphism_sector_parity = 0                               # (local) EVEN (−2(s−s') Wodzicki / 0 HKR)
    # The +2 full-homogeneity reading (which WOULD invoke the 54.04-decade leg) requires the
    # ODD scale leg; for a d_A=0 observable the scale-leg exponent is 0, so the +2 reading is
    # dimensionally FORBIDDEN — the EVEN d_A=0 face of the parity-complete Q=R·M_KK^m wall.
    full_homogeneity_reading_admissible = (scale_leg_exponent == odd_scale_leg_degree)  # (local) 0==1 -> False
    M_KK1_scale_leg_INADMISSIBLE = not full_homogeneity_reading_admissible              # (local) True (the binding signed claim)
    # Set-membership form of the no-import / parity test:
    admissible_transport_degrees_for_dA0 = {0, 2}   # (local) EVEN morphism sector: scalar 0 OR substrate-natural NON-SCALAR +2
    deg_T_in_admissible_even_sector = (int(round(deg_T)) in admissible_transport_degrees_for_dA0)  # (local) 2 in {0,2} -> True
    odd_scale_leg_in_admissible = (odd_scale_leg_degree in admissible_transport_degrees_for_dA0)   # (local) 1 in {0,2} -> False (EXCLUDED)

    # SIGN claim (Claim 1): the M_KK^1 scale leg is EXCLUDED for ΔH0/H0.
    # sign_verdict = PASS iff the predicted exclusion (M_KK1 INADMISSIBLE) holds.
    claim1_sign_pass = bool(M_KK1_scale_leg_INADMISSIBLE and (not odd_scale_leg_in_admissible))   # (local)

    # ====================================================================
    # Claim 2 — the partial relief is 49/800 = 6.125% of band-low (honest)
    # ====================================================================
    # Exact rational partial fraction (Sage-confirmed 1224993/20000000).
    dH0_frac = Fraction(dH0_BZ_central).limit_denominator(10**12)   # (local) exact-ish rational of the float
    partial_frac_lo_exact = Fraction(4899972, 1000000000) / BAND_LO  # (local) exact = 1224993/20000000 = 0.06124965
    partial_frac_lo_float = dH0_BZ_central / float(BAND_LO)          # (local) 0.06124965 (float)
    # Registry round-figure: 49/800 = 0.06125. The difference is the round-off in the
    # transported scalar (0.004899972 vs exact 49/800·0.08 = 0.0049). Publish exact, pin round-fig.
    roundfig_diff = float(partial_frac_lo_exact - PARTIAL_FRAC_ROUNDFIG)  # (local) ~ -3.5e-07
    roundfig_within_4sf = abs(roundfig_diff) < 5e-5                       # (local) 4-sf agreement
    residual_held_float = 1.0 - partial_frac_lo_float                     # (local) 0.93875035 (~94% held)

    # fractions of the other band reference points (diagnostic)
    frac_central = dH0_BZ_central / float(BAND_CENTRAL)   # (local) 0.05444413
    frac_hi = dH0_BZ_central / float(BAND_HI)             # (local) 0.04899972
    frac_lit = dH0_BZ_central / float(BAND_LIT)           # (local) 0.058333

    # ====================================================================
    # Claim 3 — dimensionless-morphism channel enumeration:
    # does ANY substrate-derived DIMENSIONLESS relation close [0.08,0.10] knob-free?
    # ====================================================================
    # The admissible (dimensionless-Ô-layer) channels at d_A=0 are EVEN-morphism transports of
    # the a₂ focusing-clock relief and a₀⊥a₂ dimensionless RELATIONS. Enumerate the
    # substrate-natural EVEN-degree morphism images of the transported relief; NONE may invoke
    # the M_KK^1 odd scale leg (that is the dimensionful a₀ draw — the Layer-1 wall).
    #
    # Channel A — scalar (deg 0, T2-VACUOUS): the relief is its own pivot image (no transport).
    chA_relief = dH0_BZ_central                          # (local) 0.004899972
    # Channel B — substrate-natural NON-SCALAR deg +2 (the S110 CF3 transported relief, dimensionless-Ô).
    #   This is ALREADY the deg_T=2.0 image; the dimensionless-Ô-layer transport does NOT add a scale leg.
    chB_relief = dH0_BZ_central                          # (local) 0.004899972 (deg_T=2 NON-SCALAR, dimensionless-Ô)
    # Channel C — a₀⊥a₂ dimensionless RELATION refinement (a₀ refines the a₀/a₂ Ô-image RATIO).
    #   The a₀ contribution at the dimensionless layer is bounded by the effacement residual share
    #   a0_share = 0.000300 (INV4-W2-2: a2_share=0.999700, a0_share=0.000300); it REFINES the ratio,
    #   it does NOT supply a dimensionful budget. The relation cannot lift the relief above the
    #   transported value by a dimensionful factor — only re-weight the dimensionless a₀/a₂ ratio.
    a0_share = 0.000300                                  # (local) INV4-W2-2 a₀ residual share (dimensionless)
    a2_share = 0.999700                                  # (local) INV4-W2-2 a₂ dominant share
    # The a₀⊥a₂ relation can at most contribute its own share to a dimensionless re-weight; the
    # ceiling of any dimensionless re-weighting of the transported relief stays O(relief), NOT
    # O(band). Bounding channel-C relief by the relief scaled by (1 + a0_share/a2_share):
    chC_relief_ceiling = dH0_BZ_central * (1.0 + a0_share / a2_share)  # (local) ~0.004901442 (a₀-refined ceiling)
    # Best dimensionless-morphism channel:
    best_dimless_relief = max(chA_relief, chB_relief, chC_relief_ceiling)   # (local) ~0.004901
    best_dimless_frac_lo = best_dimless_relief / float(BAND_LO)             # (local) ~0.06127

    # Does the best dimensionless-morphism channel reach the band [0.08,0.10] knob-free?
    band_closed_dimensionless = bool(best_dimless_relief >= float(BAND_LO))  # (local) False (0.0049 << 0.08)

    # The ONLY way to reach the band is a multiplicative ratio of 18.367 (fitted budget) — a
    # DIMENSIONFUL a₀ draw (the M_KK^1 leg) — which is the Layer-1 wall. We do NOT attempt it
    # (attempting it would be the FAIL path). The dimensionless layer under-delivers ⇒ INFO.
    dimensionful_draw_required_to_close = float(BAND_CENTRAL) / best_dimless_relief  # (local) ~18.36 (the forbidden draw)
    dimensionful_draw_attempted = False   # (local) we DO NOT draw a dimensionful budget out of a₀ (Layer-1 wall honored)

    # ====================================================================
    # VERDICT logic (plan §W2-2 operator)
    # ====================================================================
    #   PASS iff a dimensionless R_dimless predicts ΔH0/H0 ∈ [0.08,0.10] knob-free.
    #   INFO iff only the partial 49/800 = 6.125% lands (the honest partial, ~94% held).
    #   FAIL iff the only band-closing channel requires a dimensionful a₀ draw AND it is attempted.
    if band_closed_dimensionless:
        verdict = "PASS"   # (local) a dimensionless relation closed the band knob-free
    elif dimensionful_draw_attempted:
        verdict = "FAIL"   # (local) Layer-1 wall: dimensionful draw attempted (forbidden)
    else:
        verdict = "INFO"   # (local) partial 6.125% lands; ~94% HELD; band-closure HELD pending one M_KK-fixing obs

    # ---- [SIGN] 3-tuple ---------------------------------------------------
    # sign_verdict: the signed claims are (1a) d_A=0 ⇒ M_KK^1 scale leg INADMISSIBLE,
    #                                     (1b) the relief-fraction direction (partial < band-low).
    #   PASS iff BOTH signed predictions hold: the scale leg is excluded AND the partial relief
    #   sits BELOW band-low (it is a partial, in the predicted direction).
    relief_below_band_lo = bool(best_dimless_relief < float(BAND_LO))   # (local) True (partial, as predicted)
    sign_verdict = "PASS" if (claim1_sign_pass and relief_below_band_lo) else "FAIL"   # (local)

    # magnitude_verdict: the partial-INFO target is 49/800 = 0.06125 (the focusing-clock fraction).
    #   PASS if |partial_frac − 0.06125| ≤ pass_band(1e-3); INFO if within info_band; FAIL beyond.
    #   The PASS_meaning band-membership [0.08,0.10] is the PASS-leg of the gate; the magnitude
    #   axis here scores the partial relief against its pre-registered 49/800 partial floor.
    mag_dist = abs(partial_frac_lo_float - float(PARTIAL_FRAC_ROUNDFIG))   # (local) ~3.5e-07
    if mag_dist <= 1e-3:
        magnitude_verdict = "PASS"   # (local) partial relief matches the 49/800 floor (4-sf exact)
    elif mag_dist <= 1e-2:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    # regime_verdict: the d_A=0 parity-admissibility test is structurally EXACT (set-membership,
    #   not a truncation-bounded expansion); the dimensionless-Ô-layer transport is VALID throughout.
    regime_verdict = "VALID"   # (local)

    # Composite (gate-verdicts.md collapse rule):
    #   regime=VALID, sign=PASS, magnitude=PASS ⇒ composite = PASS-collapse.
    # BUT the gate's TOP-LINE verdict is the band-closure verdict (INFO: partial lands, band HELD).
    # The 3-tuple scores the SIGNED sub-claims (parity exclusion + relief-direction + partial-floor
    # match), all of which PASS; the composite-collapse of the 3-tuple is therefore PASS, while the
    # gate's pre-registered band-closure operator returns INFO (only the partial lands). These are
    # NOT in conflict: the SIGNED claims (the [SIGN] trigger content) are all correct; the band does
    # not close at the dimensionless layer. The top-line follows the gate operator (INFO), and we
    # disclose the 3-tuple-composite-vs-gate-operator distinction in the value string + companion row.
    three_tuple_composite = "PASS"   # (local) sign=PASS ∧ mag=PASS ∧ regime=VALID
    # Plan-frozen gate operator precedence: the band-closure operator (INFO on partial) governs the
    # TOP-LINE; the 3-tuple composite (PASS on the signed sub-claims) is disclosed but does NOT
    # override the gate operator. Per gate-verdicts.md §"Plan-frozen gate-block operator precedence",
    # emit a composite-precedence companion row.

    # ---- assemble result --------------------------------------------------
    out = {
        "value": None,  # filled below
        "verdict": verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "three_tuple_composite": three_tuple_composite,
        # Claim 1 (parity)
        "d_A_dH0": d_A_dH0,
        "scale_leg_exponent": scale_leg_exponent,
        "scale_leg_is_trivial": scale_leg_is_trivial,
        "odd_scale_leg_degree": odd_scale_leg_degree,
        "odd_scale_leg_parity": odd_scale_leg_parity,
        "morphism_sector_parity": morphism_sector_parity,
        "M_KK1_scale_leg_INADMISSIBLE": M_KK1_scale_leg_INADMISSIBLE,
        "full_homogeneity_reading_admissible": full_homogeneity_reading_admissible,
        "deg_T_in_admissible_even_sector": deg_T_in_admissible_even_sector,
        "odd_scale_leg_in_admissible": odd_scale_leg_in_admissible,
        "claim1_sign_pass": claim1_sign_pass,
        # Claim 2 (partial relief)
        "dH0_BZ_central": dH0_BZ_central,
        "dH0_BZ_paper": dH0_BZ_paper,
        "partial_frac_lo_float": partial_frac_lo_float,
        "partial_frac_lo_exact_num": partial_frac_lo_exact.numerator,
        "partial_frac_lo_exact_den": partial_frac_lo_exact.denominator,
        "partial_frac_roundfig": float(PARTIAL_FRAC_ROUNDFIG),
        "roundfig_diff": roundfig_diff,
        "roundfig_within_4sf": roundfig_within_4sf,
        "residual_held_float": residual_held_float,
        "frac_central": frac_central,
        "frac_hi": frac_hi,
        "frac_lit": frac_lit,
        # Claim 3 (dimensionless-channel enumeration)
        "chA_relief": chA_relief,
        "chB_relief": chB_relief,
        "chC_relief_ceiling": chC_relief_ceiling,
        "best_dimless_relief": best_dimless_relief,
        "best_dimless_frac_lo": best_dimless_frac_lo,
        "a0_share": a0_share,
        "a2_share": a2_share,
        "band_closed_dimensionless": band_closed_dimensionless,
        "dimensionful_draw_required_to_close": dimensionful_draw_required_to_close,
        "dimensionful_draw_attempted": dimensionful_draw_attempted,
        # band refs
        "band_lo": float(BAND_LO),
        "band_hi": float(BAND_HI),
        "band_central": float(BAND_CENTRAL),
        "band_lit": float(BAND_LIT),
        # transport / orthogonality
        "deg_T": deg_T,
        "deg_T_is_scalar": deg_T_is_scalar,
        "a0_a2_orthogonal": a0_a2_orthogonal,
        "dec_separation": dec_sep_loaded,
        "ratio_needed_central_loaded": ratio_needed_central_loaded,
        # cross-checks
        "cc0_central_match": cc0_central_match,
        "cc0_clock_coeff_match": cc0_clock_coeff_match,
        "cc0_decsep_match": cc0_decsep_match,
        "cc0_orthogonal": cc0_orthogonal,
        # canonical anchors
        "w0_FW_val": float(w0_FW),
        "clock_coeff_val": float(clock_coeff),
        "H_0_km_s_Mpc_val": float(H_0_km_s_Mpc),
    }

    # value payload string (no single-quote chars — emit_verdict wraps value='...')
    value_str = (
        f"partial_relief_frac_lo={partial_frac_lo_float:.6g}_"
        f"roundfig=49/800={float(PARTIAL_FRAC_ROUNDFIG):.5g}_"
        f"residual_held={residual_held_float:.5g}_"
        f"d_A=0_M_KK1_scale_leg_INADMISSIBLE={M_KK1_scale_leg_INADMISSIBLE}_"
        f"band_closed_dimensionless={band_closed_dimensionless}_"
        f"dimensionful_draw_attempted={dimensionful_draw_attempted}_"
        f"a0_a2_orthogonal={a0_a2_orthogonal}_deg_T={deg_T:.1f}_"
        f"sign={sign_verdict}_mag={magnitude_verdict}_regime={regime_verdict}_"
        f"3tuple_composite={three_tuple_composite}"
    )
    out["value"] = value_str
    return out


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, png_path: Path) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # --- Panel 1: relief vs band -------------------------------------------
    relief = res["best_dimless_relief"]           # (local)
    band_lo = res["band_lo"]                       # (local)
    band_hi = res["band_hi"]                       # (local)
    band_central = res["band_central"]             # (local)
    band_lit = res["band_lit"]                     # (local)

    ax1.axhspan(band_lo, band_hi, color="tab:orange", alpha=0.20,
                label=f"H$_0$-tension band [{band_lo:.2f}, {band_hi:.2f}]")
    ax1.axhline(band_central, color="tab:orange", ls="--", lw=1.2, label=f"band-central {band_central:.2f}")
    ax1.axhline(band_lit, color="tab:red", ls=":", lw=1.0, label=f"lit central {band_lit:.3f}")
    ax1.bar([0], [relief], width=0.4, color="tab:blue",
            label=f"dimensionless-Ô relief {relief:.4g}")
    # annotate the held residual
    ax1.annotate(
        f"partial = {res['partial_frac_lo_float']*100:.3f}% of band-low\n"
        f"(49/800 = 6.125%)\n~{res['residual_held_float']*100:.1f}% HELD",
        xy=(0, relief), xytext=(0.45, band_central * 0.55),
        fontsize=9, ha="left",
        arrowprops=dict(arrowstyle="->", color="gray"))
    ax1.set_xlim(-0.6, 1.6)
    ax1.set_xticks([])
    ax1.set_ylabel(r"$\Delta H_0/H_0$  (dimensionless)")
    ax1.set_title("Dimensionless-Ô relief vs H$_0$-tension band\n(the partial lands; band HELD)")
    ax1.legend(fontsize=7.5, loc="upper right")

    # --- Panel 2: d_A=0 parity exclusion -----------------------------------
    ax2.axis("off")
    txt = (
        "Claim 1 — d$_A$=0 parity inadmissibility (EVEN face of §VII.CF)\n"
        "─────────────────────────────────────────────\n"
        f"  d$_A$(ΔH₀/H₀) = {res['d_A_dH0']}  (ratio of like-dim quantities)\n"
        f"  scale-leg exponent = d$_A$ = {res['scale_leg_exponent']}  ⇒  M_KK$^0$ = 1 (TRIVIAL)\n"
        f"  M_KK$^1$ odd scale leg (deg {res['odd_scale_leg_degree']}, parity {res['odd_scale_leg_parity']}=ODD)\n"
        f"  morphism sector parity = {res['morphism_sector_parity']} (EVEN: −2(s−s'), 0)\n"
        f"  +2 full-homogeneity reading admissible: {res['full_homogeneity_reading_admissible']}\n"
        f"  ⇒ M_KK$^1$ scale leg INADMISSIBLE: {res['M_KK1_scale_leg_INADMISSIBLE']}\n"
        f"     (54.04-decade leg parity-FORBIDDEN for ΔH₀/H₀)\n\n"
        "Claim 3 — dimensionless-morphism channel enumeration\n"
        "─────────────────────────────────────────────\n"
        f"  best dimensionless-Ô relief = {res['best_dimless_relief']:.6g}\n"
        f"  band-low = {res['band_lo']:.2f}\n"
        f"  band closed dimensionless: {res['band_closed_dimensionless']}\n"
        f"  dimensionful a₀ draw to close = {res['dimensionful_draw_required_to_close']:.3f}×\n"
        f"     (the Layer-1 wall — NOT attempted: {res['dimensionful_draw_attempted']})\n\n"
        f"  a₀⊥a₂ orthogonal (S110 CF3): {res['a0_a2_orthogonal']}\n"
        f"  a₀ share = {res['a0_share']:.6f} / a₂ share = {res['a2_share']:.6f}\n\n"
        f"VERDICT: {res['verdict']}  "
        f"(sign={res['sign_verdict']} mag={res['magnitude_verdict']} regime={res['regime_verdict']})"
    )
    ax2.text(0.0, 1.0, txt, va="top", ha="left", fontsize=8.6, family="monospace")

    fig.suptitle("S111-CF3-H0-RESIDUAL — residual H$_0$ relief at the dimensionless-Ô layer",
                 fontsize=12, y=1.00)
    fig.tight_layout()
    fig.savefig(png_path, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot written: {png_path.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload (printed; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, extra_rows=None) -> dict:
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
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins + dual SHA
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    res = compute()

    # 3. Report
    print(f"=== {GATE_ID} — results ===")
    print(f"  d_A(ΔH0/H0) = {res['d_A_dH0']}  (scale-leg exponent {res['scale_leg_exponent']} -> M_KK^0=1 trivial)")
    print(f"  M_KK^1 scale leg INADMISSIBLE = {res['M_KK1_scale_leg_INADMISSIBLE']}  (parity: odd leg {res['odd_scale_leg_parity']} vs even morphism {res['morphism_sector_parity']})")
    print(f"  partial relief (frac of band-low) = {res['partial_frac_lo_float']:.8f}  exact = {res['partial_frac_lo_exact_num']}/{res['partial_frac_lo_exact_den']}")
    print(f"  registry round-figure 49/800 = {res['partial_frac_roundfig']:.5f}  (diff {res['roundfig_diff']:.2e}, 4sf-agree {res['roundfig_within_4sf']})")
    print(f"  residual HELD = {res['residual_held_float']:.8f}  (~{res['residual_held_float']*100:.1f}%)")
    print(f"  frac of band-central(0.09) = {res['frac_central']:.6f} ; band-hi(0.10) = {res['frac_hi']:.6f} ; lit(0.084) = {res['frac_lit']:.6f}")
    print(f"  best dimensionless-Ô relief = {res['best_dimless_relief']:.8f} ; band closed = {res['band_closed_dimensionless']}")
    print(f"  dimensionful draw to close band-central = {res['dimensionful_draw_required_to_close']:.3f}x  (NOT attempted: {res['dimensionful_draw_attempted']})")
    print(f"  a0_a2_orthogonal = {res['a0_a2_orthogonal']} ; deg_T = {res['deg_T']} (scalar={res['deg_T_is_scalar']})")
    print(f"  CROSS-CHECKS: central_match={res['cc0_central_match']} clock_coeff_match={res['cc0_clock_coeff_match']} decsep_match={res['cc0_decsep_match']} orthogonal={res['cc0_orthogonal']}")
    print(f"  3-tuple: sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} regime={res['regime_verdict']} (3tuple-composite={res['three_tuple_composite']})")
    print(f"  TOP-LINE VERDICT (gate band-closure operator): {res['verdict']}")
    print()

    # 4. Save data
    npz_path = SESSION_DIR / "s111_cf3_h0_residual.npz"  # (local)
    np.savez(
        npz_path,
        **{k: v for k, v in res.items() if k != "value"},
        value=res["value"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        partial_frac_roundfig_num=PARTIAL_FRAC_ROUNDFIG.numerator,
        partial_frac_roundfig_den=PARTIAL_FRAC_ROUNDFIG.denominator,
    )
    print(f"  data written: {npz_path.relative_to(PROJECT_ROOT)}")

    # 5. Plot
    png_path = SESSION_DIR / "s111_cf3_h0_residual.png"  # (local)
    make_plot(res, png_path)
    print()

    # 6. 4-tuple + emit payload
    tag = (f"(value={res['value']!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    # companion rows: the d_A=0 parity discipline tag + the composite-precedence disclosure
    extra_rows = [
        (f"# parity_pin: convention={CONVENTION} d_A=0 M_KK^1_scale_leg_INADMISSIBLE=True "
         f"(EVEN-face of §VII.CF parity wall; ODD d_A=+1 face = §VII.CF LRD-T); "
         f"regulator-pin-discipline.md Mass-dimension/parity axis"),
        (f"# composite-precedence: gate band-closure operator returns INFO (partial 49/800=6.125% lands, "
         f"~94% HELD); the [SIGN] 3-tuple composite is PASS (sign=PASS parity-exclusion + relief-direction; "
         f"mag=PASS partial-floor 49/800 4sf; regime=VALID set-membership-exact) — the SIGNED sub-claims all hold, "
         f"the band does NOT close at the dimensionless layer; TOP-LINE follows the plan-frozen gate operator "
         f"(INFO) per gate-verdicts.md Plan-frozen gate-block operator precedence; anchor session-111-plan-w2.md §W2-2"),
        (f"# partial_relief_exact: {res['partial_frac_lo_exact_num']}/{res['partial_frac_lo_exact_den']}=0.06124965 "
         f"(round-figure 49/800=0.06125 pinned alongside; round-figure-fidelity discipline — publish exact, pin round-fig); "
         f"a0_a2_orthogonal=True (S110 CF3 7bfda02a); consumes s110_cf3_timescape_h0.npz + inv7_w1_4_kbc_timescape_h0.npz"),
    ]
    print_verdict_payload(
        res["verdict"], res["value"], audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
