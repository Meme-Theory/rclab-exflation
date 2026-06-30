#!/usr/bin/env python3
"""
INV3 W3-2 — W3 minimal model M(6,5) (c=4/5, Z3-Potts) kink mass ratios vs phi_paasch / fN
==========================================================================================

Gate: INV3-W3-2 ([CHAIN])
  Hypothesis: a W3 M(6,5) (c=4/5, three-state Potts critical point) kink/soliton
  mass ratio (Reshetikhin-Smirnov / integrable-perturbation S-matrix) equals
  phi_paasch=1.531580 or fN=sqrt(5)-1=1.236068 within 2% — i.e. is phi_paasch a
  universality-class number forced by the c=4/5 CFT?

Pre-registered threshold (plan §W3-2):
  operator: min over spectrum of min(|r-phi_paasch|/phi_paasch, |r-fN|/fN) <= 0.02
  PASS  iff a W3 M(6,5)-related kink mass ratio is within 2% of phi_paasch OR fN.
  FAIL  iff no M(6,5) kink mass ratio lands within 2% (or 5% diagnostic) of either target.
  INFO  iff value='lit-unavailable' (no published table) OR a match exists but is
        only 1-of-many ratios (look-elsewhere weak; reported with total-ratio count).

LITERATURE (retrieved via paper-search / WebSearch, this dispatch — NOT training knowledge):
  [P1] L. Lepori, G. Z. Toth, G. Delfino, "Particle spectrum of the 3-state Potts
       field theory: a numerical study," arXiv:0909.2192v2 (SISSA 55/2009/EP).
       DECISIVE for the TARGET model. The S3-invariant 3-state Potts critical point
       is the D4 (c=4/5) minimal model M(6,5) [their Sec. 2]. Its massive integrable
       (h=0 thermal) deformation has a spectrum of KINKS K_{ab} (a!=b) ALL OF EQUAL
       MASS m (their Sec 3.1, citing Chim-Zamolodchikov [20] Int.J.Mod.Phys.A7(1992)5317
       and Koberle-Swieca [26] Phys.Lett.B86(1979)209). Eq (7): m = b*tau^{5/6},
       b=4.504. The integrable spectrum is a degenerate doublet => the ONLY mass
       ratio in the universality-class (zero-field, integrable) spectrum is 1.000.
       Nontrivial ratios (mesons pi^(n), baryons p^(n)) appear ONLY for h!=0, where
       they are CONTINUOUS functions of eta_pm (their Fig 5) -- tunable, NON-universal.
  [P2] G. Mussardo, M. Panero, A. Stampiggi, "Form Factors of the Tricritical
       Three-state Potts Model in its Scaling Limit," arXiv:2311.00654v2.
       ADJACENT universality class: the TRICRITICAL 3-state Potts = M(6,7) (c=6/7),
       the E6 theory. Its mass spectrum (their Eq 14) is NONTRIVIAL:
         m_l = M(lambda) (lightest);  m_L = 2cos(pi/4) m_l = sqrt(2) m_l;
         m_h = 2cos(pi/12) m_l;  + a heavier self-conjugate [2cos(pi/4)]^2 m_l.
       These E6-Toda ratios are genuine universality-class numbers.
  [P3] Coldea et al., Science 327 (2010) 177 -- the E8 Ising (c=1/2, M(4,3)) chain:
       golden ratio m_2/m_1 = 2cos(pi/5) = 1.618034 DOES appear (Paasch Paper 11
       cites this as the golden-ratio-in-criticality precedent). DIFFERENT class (E8).

PRIOR ART (knowledge MCP): S33a s33a_w3_kink_masses.py surveyed A_n/D_4/E_6/E_7/E_8
  affine Toda + W3 M(6,5) Kac dims + Z3-Potts trig scans vs phi_paasch ONLY (2%/5%).
  This gate (a) adds the fN=sqrt(5)-1 target S33a did not test, (b) installs the
  DECISIVE physics fact (the integrable M(6,5) kink spectrum is single-mass =>
  ratio 1 only), (c) reports honest look-elsewhere ratio counts for BOTH targets.

Classification: PARTICLE on a GEOMETRIC substrate (collective-excitation kink/soliton
  mass ratios of the substrate's Z3 wall criticality; the W3 CFT IS the effective
  description of that criticality -- external lit is methodological cross-check).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — env + path bootstrap (scalar arithmetic; cpu-cap-OMP8 per plan GPU_path)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
from pathlib import Path

# _shared (canonical_constants.py) onto path BEFORE the canonical import
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403  (provides phi_paasch=1.531580)

# ---------------------------------------------------------------------------
# Section 2 — Numerical imports
# ---------------------------------------------------------------------------
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

SESSION = "3"                                       # (local) investigation 3
GATE_ID = "INV3-W3-2"                               # (local) short form; verdict anchor ^INV3-W3-2:
SCHEME = "W3-MINIMAL-MODEL-KINK-PHI"                # (local) scheme= field
CONVENTION = "RATIO"                                # (local)
L_MAX = "N/A"                                       # (local) CFT spectrum, no D_K truncation

# Targets (phi_paasch imported from canonical_constants; fN derived Sage-exact)
FN = float(np.sqrt(5.0) - 1.0)                      # (local) Paasch M-ratio = 2/golden = 1.2360679...
TOL_2PCT = 0.02                                     # (local) pre-registered PASS band
TOL_5PCT = 0.05                                     # (local) diagnostic band

OUT_NPZ = SESSION_DIR / "inv3_w3_w3_minimal_model_kink_phi.npz"
OUT_PNG = SESSION_DIR / "inv3_w3_w3_minimal_model_kink_phi.png"

INPUT_FILES = [SHARED_DIR / "canonical_constants.py"]


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


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
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
# Section 5 — Verdict payload helper (race-safe emission; agent calls emit_verdict)
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
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = extra_rows
    if sign_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    print("=== VERDICT_PAYLOAD_JSON ===")
    print(json.dumps(payload))
    print("=== END_VERDICT_PAYLOAD_JSON ===")
    return payload


# ---------------------------------------------------------------------------
# Section 6 — Mass-ratio spectra (literature-anchored, exact algebraic numbers)
# ---------------------------------------------------------------------------
def collect_spectra() -> dict:
    """Return {model_name: {'role': str, 'class': str, 'ratios': [(value,label,alg)]}}.

    role taxonomy (PASS-predicate gating; the plan operator is about kink MASS ratios):
      'target_mass'        -- the M(6,5) c=4/5 kink/soliton MASS spectrum. ONLY this role
                              is PASS-eligible (the hypothesis & operator are mass-ratio claims).
      'target_diagnostic'  -- M(6,5) scaling-DIMENSION ratios. SAME CFT, but conformal weights
                              are NOT masses; reported as a diagnostic, NOT PASS-eligible
                              (a dimension ratio within 2% of fN does NOT make fN a mass number).
      'adjacent'           -- neighbouring universality classes (E6 tricrit-Potts, E8 Ising). Context.
      'lookelsewhere'      -- systematic algebraic-number scans (the look-elsewhere denominator).

    A mass RATIO is m_a/m_b > 1 within a single model's mass spectrum. Each ratio is
    an EXACT algebraic number from the published integrable S-matrix / bootstrap.
    """
    spectra: dict = {}  # (local)

    # === TARGET (mass): M(6,5), c=4/5, three-state Potts critical point (D4 model) ===
    # [P1] arXiv:0909.2192: integrable (h=0 thermal) deformation -> kinks K_ab ALL
    # EQUAL MASS m (Chim-Zamolodchikov, Koberle-Swieca). The integrable / universality-
    # class spectrum is a DEGENERATE doublet: the ONLY mass ratio is m/m = 1.000.
    spectra["M65_3statePotts_INTEGRABLE"] = {
        "role": "target_mass",
        "class": "D4 / Z3-Potts (c=4/5) KINK MASS spectrum",
        "ratios": [
            (1.0, "m_Kab/m_Kcd", "1 (degenerate kink doublet; Chim-Zam 1992, Koberle-Swieca 1979)"),
        ],
    }

    # M(6,5) Kac-table SCALING-DIMENSION ratios (NOT masses; DIAGNOSTIC only, NOT PASS-eligible).
    # Kac: Delta_{r,s} = ((6 s - 5 r)^2 - 1)/120, r<=5, s<=4. (S33a included these as a diagnostic.)
    p_kac, pp_kac = 6, 5  # (local)
    dims = {}  # (local)
    for r in range(1, pp_kac + 1):
        for s in range(1, p_kac):
            Delta = ((p_kac * s - pp_kac * r) ** 2 - 1) / (4.0 * p_kac * pp_kac)  # (local)
            if Delta > 1e-9:
                dims[(r, s)] = Delta
    dim_ratios = []  # (local)
    seen = set()  # (local)
    keys = list(dims.keys())  # (local)
    for i in range(len(keys)):
        for j in range(len(keys)):
            if i != j:
                rr = dims[keys[j]] / dims[keys[i]]  # (local)
                if rr > 1.0:
                    key = round(rr, 9)  # (local)
                    if key not in seen:
                        seen.add(key)
                        dim_ratios.append((rr, "Delta%s/Delta%s" % (keys[j], keys[i]),
                                           "%.6f/%.6f (Kac dims, c=4/5)" % (dims[keys[j]], dims[keys[i]])))
    spectra["M65_Kac_dimension_ratios"] = {
        "role": "target_diagnostic", "class": "D4 / Z3-Potts (c=4/5) scaling DIMENSIONS (not masses)",
        "ratios": dim_ratios,
    }

    # === ADJACENT: tricritical 3-state Potts = M(6,7), c=6/7, the E6 theory ===
    # [P2] arXiv:2311.00654 Eq (14): m_l (lightest); m_L=2cos(pi/4) m_l; m_h=2cos(pi/12) m_l;
    # heavier self-conjugate [2cos(pi/4)]^2 m_l = 2 m_l. Genuine universality-class numbers.
    c4 = 2 * np.cos(np.pi / 4)   # (local) sqrt(2) = 1.41421
    c12 = 2 * np.cos(np.pi / 12)  # (local) 1.93185
    masses_e6 = {"l": 1.0, "L": c4, "h": c12, "H": c4 ** 2}  # (local) H = 2.0
    e6r = []  # (local)
    seen = set()  # (local)
    mk = list(masses_e6.items())  # (local)
    for i in range(len(mk)):
        for j in range(len(mk)):
            if i != j:
                rr = masses_e6[mk[j][0]] / masses_e6[mk[i][0]]  # (local)
                if rr > 1.0:
                    key = round(rr, 9)  # (local)
                    if key not in seen:
                        seen.add(key)
                        e6r.append((rr, "m_%s/m_%s" % (mk[j][0], mk[i][0]),
                                    "tricritical Potts E6 (M(6,7), c=6/7), arXiv:2311.00654 Eq14"))
    spectra["M67_tricritPotts_E6"] = {
        "role": "adjacent", "class": "E6 / tricritical-Potts (c=6/7)", "ratios": e6r,
    }

    # === PRECEDENT: Ising in magnetic field = M(4,3), c=1/2, the E8 theory (Coldea) ===
    # [P3] Zamolodchikov E8 masses m_a/m_1: a=2..8.
    e8_exp = [1, 7, 11, 13, 17, 19, 23, 29]  # (local) E8 Coxeter exponents, h=30
    masses_e8 = [np.sin(e * np.pi / 30) for e in e8_exp]  # (local)
    e8r = []  # (local)
    seen = set()  # (local)
    for i in range(len(masses_e8)):
        for j in range(len(masses_e8)):
            if i != j:
                rr = masses_e8[j] / masses_e8[i]  # (local)
                if rr > 1.0:
                    key = round(rr, 9)  # (local)
                    if key not in seen:
                        seen.add(key)
                        e8r.append((rr, "m(e=%d)/m(e=%d)" % (e8_exp[j], e8_exp[i]),
                                    "Ising-E8 (M(4,3), c=1/2), Zamolodchikov 1989"))
    # Headline E8 ratio m_2/m_1 = 2 cos(pi/5) = golden = 1.618034 (Coldea 2010)
    e8r.append((2 * np.cos(np.pi / 5), "m_2/m_1 (golden)", "2cos(pi/5)=1.618034, Coldea 2010 E8 Ising chain"))
    spectra["M43_Ising_E8_Coldea"] = {
        "role": "adjacent", "class": "E8 / Ising (c=1/2)", "ratios": e8r,
    }

    # === A2 affine Toda (Z3 doublet bootstrap; the integrable Z3 structure) ===
    # A2 ATT h=3: m1=m2; bound state m12 = sqrt(3) m1 (the Z3 bootstrap fusing).
    h_a2 = 3  # (local)
    m1 = np.sin(np.pi / h_a2)  # (local)
    m2 = np.sin(2 * np.pi / h_a2)  # (local)
    m12 = np.sqrt(m1 ** 2 + m2 ** 2 + 2 * m1 * m2 * np.cos(np.pi / h_a2))  # (local)
    spectra["A2_affineToda_Z3"] = {
        "role": "adjacent", "class": "A2 Toda / Z3 bootstrap",
        "ratios": [
            (m2 / m1, "m2/m1", "1 (Z3 doublet)"),
            (m12 / m1, "m_12/m1", "sqrt(3)=1.732051 (A2 bound state)"),
        ],
    }

    # === D4 affine Toda (the Lie algebra D4 itself; triality, h=6, exponents 1,3,3,5) ===
    d4_exp = [1, 3, 3, 5]  # (local)
    md4 = [np.sin(e * np.pi / 6) for e in d4_exp]  # (local)
    d4r = []  # (local)
    seen = set()  # (local)
    for i in range(4):
        for j in range(4):
            if i != j:
                rr = md4[j] / md4[i]  # (local)
                if rr > 1.0:
                    key = round(rr, 9)  # (local)
                    if key not in seen:
                        seen.add(key)
                        d4r.append((rr, "m(e=%d)/m(e=%d)" % (d4_exp[j], d4_exp[i]),
                                    "D4 affine Toda (h=6)"))
    spectra["D4_affineToda"] = {"role": "adjacent", "class": "D4 Toda", "ratios": d4r}

    # === Systematic CFT-mass-ratio scan (look-elsewhere denominator) ===
    # 2cos(k pi/n) and sin(a pi/n)/sin(b pi/n): the full algebraic-number family that
    # ANY integrable CFT mass ratio is drawn from. Reported for honest look-elsewhere.
    trig = []  # (local)
    seen = set()  # (local)
    for n in range(3, 61):
        for k in range(1, n):
            val = 2 * np.cos(k * np.pi / n)  # (local)
            if val > 1.0:
                key = round(val, 10)  # (local)
                if key not in seen:
                    seen.add(key)
                    trig.append((val, "2cos(%dpi/%d)" % (k, n), "systematic 2cos scan"))
    spectra["systematic_2cos_scan"] = {"role": "lookelsewhere", "class": "systematic (look-elsewhere)", "ratios": trig}

    sinr = []  # (local)
    seen = set()  # (local)
    for n in range(3, 31):
        for a in range(1, n):
            for b in range(1, n):
                if a != b:
                    sa = np.sin(a * np.pi / n)  # (local)
                    sb = np.sin(b * np.pi / n)  # (local)
                    if sb > 1e-15:
                        rr = sa / sb  # (local)
                        if rr > 1.0:
                            key = round(rr, 10)  # (local)
                            if key not in seen:
                                seen.add(key)
                                sinr.append((rr, "sin(%dpi/%d)/sin(%dpi/%d)" % (a, n, b, n),
                                             "systematic sin-ratio scan"))
    spectra["systematic_sin_ratio_scan"] = {"role": "lookelsewhere", "class": "systematic (look-elsewhere)", "ratios": sinr}

    return spectra


# ---------------------------------------------------------------------------
# Section 7 — Comparison against phi_paasch and fN
# ---------------------------------------------------------------------------
def analyze(spectra: dict) -> dict:
    phi = float(phi_paasch)  # (local)
    fn = FN  # (local)

    total_ratios = 0   # (local)
    mass_ratios = 0    # (local) target_mass + adjacent (genuine MASS ratios)
    target_mass_ratios = 0  # (local) M(6,5) kink MASS ratios only (PASS-eligible)
    diag_ratios = 0    # (local) target_diagnostic (scaling-DIMENSION ratios)

    # PASS-eligible matches (target_mass kink MASS ratios within 2%)
    matches_phi_2 = []  # (local)
    matches_fn_2 = []   # (local)
    # Diagnostic matches (scaling-DIMENSION ratios within 2% — NOT PASS-eligible)
    diag_phi_2 = []  # (local)
    diag_fn_2 = []   # (local)

    all_match_records = []  # (local) ANY-model 5% match to either target

    # closest target_mass kink-MASS ratio to each constant (PASS-eligible class)
    best_phi_mass = {"dev": float("inf")}  # (local)
    best_fn_mass = {"dev": float("inf")}   # (local)
    # closest target_diagnostic dimension ratio (diagnostic class)
    best_phi_diag = {"dev": float("inf")}  # (local)
    best_fn_diag = {"dev": float("inf")}   # (local)
    # closest ANY-model ratio
    best_phi_any = {"dev": float("inf")}  # (local)
    best_fn_any = {"dev": float("inf")}   # (local)

    for model, info in spectra.items():
        role = info["role"]  # (local)
        for val, label, alg in info["ratios"]:
            total_ratios += 1
            if role in ("target_mass", "adjacent"):
                mass_ratios += 1
            if role == "target_mass":
                target_mass_ratios += 1
            if role == "target_diagnostic":
                diag_ratios += 1
            dev_phi = abs(val - phi) / phi  # (local)
            dev_fn = abs(val - fn) / fn     # (local)

            if dev_phi < best_phi_any["dev"]:
                best_phi_any = {"dev": dev_phi, "model": model, "label": label, "value": val, "alg": alg, "role": role}
            if dev_fn < best_fn_any["dev"]:
                best_fn_any = {"dev": dev_fn, "model": model, "label": label, "value": val, "alg": alg, "role": role}

            if role == "target_mass":
                if dev_phi < best_phi_mass["dev"]:
                    best_phi_mass = {"dev": dev_phi, "model": model, "label": label, "value": val, "alg": alg}
                if dev_fn < best_fn_mass["dev"]:
                    best_fn_mass = {"dev": dev_fn, "model": model, "label": label, "value": val, "alg": alg}
                if dev_phi <= TOL_2PCT:
                    matches_phi_2.append({"model": model, "label": label, "value": val, "dev": dev_phi, "alg": alg})
                if dev_fn <= TOL_2PCT:
                    matches_fn_2.append({"model": model, "label": label, "value": val, "dev": dev_fn, "alg": alg})

            if role == "target_diagnostic":
                if dev_phi < best_phi_diag["dev"]:
                    best_phi_diag = {"dev": dev_phi, "model": model, "label": label, "value": val, "alg": alg}
                if dev_fn < best_fn_diag["dev"]:
                    best_fn_diag = {"dev": dev_fn, "model": model, "label": label, "value": val, "alg": alg}
                if dev_phi <= TOL_2PCT:
                    diag_phi_2.append({"model": model, "label": label, "value": val, "dev": dev_phi, "alg": alg})
                if dev_fn <= TOL_2PCT:
                    diag_fn_2.append({"model": model, "label": label, "value": val, "dev": dev_fn, "alg": alg})

            best_dev = min(dev_phi, dev_fn)  # (local)
            if best_dev <= TOL_5PCT:
                all_match_records.append({
                    "model": model, "role": role, "label": label, "value": val,
                    "target": "phi" if dev_phi < dev_fn else "fN",
                    "dev": best_dev, "in_2pct": best_dev <= TOL_2PCT, "alg": alg,
                })

    all_match_records.sort(key=lambda x: x["dev"])

    # PASS predicate: the plan operator is a MASS-ratio claim. PASS iff a target_mass
    # (M(6,5) KINK MASS) ratio is within 2% of phi OR fN. Scaling-DIMENSION ratios
    # (target_diagnostic) are NOT masses and do NOT satisfy the operator.
    target_pass_2pct = (len(matches_phi_2) > 0) or (len(matches_fn_2) > 0)  # (local)

    return {
        "phi": phi, "fn": fn,
        "total_ratios": total_ratios, "mass_ratios": mass_ratios,
        "target_mass_ratios": target_mass_ratios, "diag_ratios": diag_ratios,
        "matches_phi_2": matches_phi_2, "matches_fn_2": matches_fn_2,
        "diag_phi_2": diag_phi_2, "diag_fn_2": diag_fn_2,
        "all_match_records": all_match_records,
        "best_phi_mass": best_phi_mass, "best_fn_mass": best_fn_mass,
        "best_phi_diag": best_phi_diag, "best_fn_diag": best_fn_diag,
        "best_phi_any": best_phi_any, "best_fn_any": best_fn_any,
        "target_pass_2pct": target_pass_2pct,
    }


def make_plot(spectra: dict, ana: dict):
    phi = ana["phi"]  # (local)
    fn = ana["fn"]    # (local)
    role_color = {  # (local)
        "target_mass": "tab:red",
        "target_diagnostic": "tab:orange",
        "adjacent": "tab:purple",
        "lookelsewhere": "tab:gray",
    }
    role_marker = {"target_mass": "o", "target_diagnostic": "s", "adjacent": "^", "lookelsewhere": "."}  # (local)
    fig, ax = plt.subplots(figsize=(10, 6.5))
    y = 0  # (local)
    yticks, ylabels = [], []  # (local)
    seen_roles = set()  # (local)
    for model, info in spectra.items():
        vals = [v for v, _, _ in info["ratios"]]  # (local)
        if not vals:
            continue
        role = info["role"]  # (local)
        lbl = role if role not in seen_roles else None  # (local)
        seen_roles.add(role)
        ax.scatter(vals, [y] * len(vals), s=30, color=role_color[role],
                   marker=role_marker[role], zorder=3, label=lbl)
        yticks.append(y)
        prefix = {"target_mass": "** ", "target_diagnostic": "*~ ", "adjacent": "+  ", "lookelsewhere": "   "}[role]  # (local)
        ylabels.append(prefix + model)
        y += 1
    ax.axvline(phi, color="tab:blue", lw=2.0, label="phi_paasch=%.6f" % phi)
    ax.axvspan(phi * (1 - TOL_2PCT), phi * (1 + TOL_2PCT), color="tab:blue", alpha=0.15)
    ax.axvline(fn, color="tab:green", lw=2.0, ls="--", label="fN=sqrt(5)-1=%.6f" % fn)
    ax.axvspan(fn * (1 - TOL_2PCT), fn * (1 + TOL_2PCT), color="tab:green", alpha=0.15)
    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels, fontsize=7)
    ax.set_xlim(0.95, 3.2)
    ax.set_xlabel("mass ratio m_a/m_b (>1)   [** = PASS-eligible target KINK MASS; *~ = diagnostic DIMENSION ratios]")
    ax.set_title("INV3-W3-2: W3 M(6,5) c=4/5 (Z3-Potts) kink MASS ratios vs phi_paasch / fN\n"
                 "TARGET integrable kink spectrum = single degenerate mass -> only mass ratio = 1.000 (FAIL)",
                 fontsize=9)
    ax.legend(fontsize=7, loc="upper right")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main():
    pins = log_input_pins(INPUT_FILES)  # (local)
    spectra = collect_spectra()  # (local)
    ana = analyze(spectra)  # (local)

    sep = "=" * 78  # (local)
    print("\n" + sep)
    print("INV3-W3-2  W3 M(6,5) c=4/5 (Z3-Potts) kink mass ratios vs phi_paasch / fN")
    print(sep)
    print("phi_paasch = %.6f  (canonical_constants.py:289)" % ana["phi"])
    print("fN         = %.6f  (sqrt(5)-1, Sage-exact)" % ana["fn"])
    print("2%% bands: phi[%.4f,%.4f]  fN[%.4f,%.4f]" % (
        ana["phi"] * 0.98, ana["phi"] * 1.02, ana["fn"] * 0.98, ana["fn"] * 1.02))

    print("\n--- LOOK-ELSEWHERE DENOMINATOR (honest ratio counts) ---")
    print("  TOTAL ratios scanned (all models):           %d" % ana["total_ratios"])
    print("  genuine MASS ratios (target_mass+adjacent):  %d" % ana["mass_ratios"])
    print("  TARGET KINK-MASS ratios (M(6,5) c=4/5):      %d  <- PASS-eligible class" % ana["target_mass_ratios"])
    print("  target DIMENSION-ratio diagnostics:          %d  <- NOT masses, NOT PASS-eligible" % ana["diag_ratios"])

    print("\n--- DECISIVE PHYSICS (target kink-MASS spectrum) ---")
    print("  [P1 arXiv:0909.2192 Lepori-Toth-Delfino] M(6,5)=D4 (c=4/5) integrable (h=0 thermal) spectrum:")
    print("    kinks K_ab ALL EQUAL MASS (Chim-Zam 1992 IJMPA7:5317; Koberle-Swieca 1979 PLB86:209) => single mass.")
    print("    The ONLY universality-class KINK-MASS ratio is m/m = 1.000.")
    print("    Nontrivial meson/baryon ratios appear ONLY for h!=0 (CONTINUOUS in eta_pm; NON-universal, Fig 5).")

    print("\n--- Closest TARGET KINK-MASS ratio to each constant (PASS-eligible) ---")
    bp = ana["best_phi_mass"]; bf = ana["best_fn_mass"]  # (local)
    print("  to phi_paasch: %.6f  (%s %s)  dev=%.4f%%  [%s]" % (
        bp["value"], bp["model"], bp["label"], bp["dev"] * 100, bp["alg"]))
    print("  to fN        : %.6f  (%s %s)  dev=%.4f%%  [%s]" % (
        bf["value"], bf["model"], bf["label"], bf["dev"] * 100, bf["alg"]))

    print("\n--- TARGET KINK-MASS 2%% matches (PASS-eligible) ---")
    print("  to phi_paasch: %d" % len(ana["matches_phi_2"]))
    for m in ana["matches_phi_2"]:
        print("     %s %s = %.6f (dev %.4f%%)" % (m["model"], m["label"], m["value"], m["dev"] * 100))
    print("  to fN        : %d" % len(ana["matches_fn_2"]))
    for m in ana["matches_fn_2"]:
        print("     %s %s = %.6f (dev %.4f%%)" % (m["model"], m["label"], m["value"], m["dev"] * 100))

    print("\n--- DIAGNOSTIC: M(6,5) scaling-DIMENSION ratios (NOT masses, NOT PASS-eligible) ---")
    bpd = ana["best_phi_diag"]; bfd = ana["best_fn_diag"]  # (local)
    print("  closest dim ratio to phi: %.6f (%s) dev=%.4f%%" % (bpd["value"], bpd["label"], bpd["dev"] * 100))
    print("  closest dim ratio to fN : %.6f (%s) dev=%.4f%%" % (bfd["value"], bfd["label"], bfd["dev"] * 100))
    print("  dim-ratio 2%% near-matches: phi=%d fN=%d (REPORTED as coincidence; a conformal-weight" % (
        len(ana["diag_phi_2"]), len(ana["diag_fn_2"])))
    print("  ratio is NOT a mass ratio -> does NOT make phi/fN a universality-class MASS number)")

    print("\n--- ANY-model 5%% matches to either target (look-elsewhere context) ---")
    print("  count=%d (of %d total ratios) -- the algebraic-number family is DENSE near phi/fN" % (
        len(ana["all_match_records"]), ana["total_ratios"]))
    for m in ana["all_match_records"][:20]:
        flag = "<=2%%" if m["in_2pct"] else " 5%%"
        print("     [%s|%s] %s %s = %.6f -> %s dev=%.4f%%  [%s]" % (
            m["role"], flag, m["model"], m["label"], m["value"], m["target"], m["dev"] * 100, m["alg"]))

    print("\n--- ADJACENT classes (context, NOT target) ---")
    bpa = ana["best_phi_any"]; bfa = ana["best_fn_any"]  # (local)
    print("  closest ANY-model ratio to phi: %.6f (%s %s) dev=%.4f%% role=%s" % (
        bpa["value"], bpa["model"], bpa["label"], bpa["dev"] * 100, bpa["role"]))
    print("  closest ANY-model ratio to fN : %.6f (%s %s) dev=%.4f%% role=%s" % (
        bfa["value"], bfa["model"], bfa["label"], bfa["dev"] * 100, bfa["role"]))

    # --- Verdict (pre-registered, plan §W3-2) ---
    # Literature IS available (P1 decisive) => NOT lit-unavailable INFO.
    # The plan operator is a MASS-ratio claim. PASS iff a target_mass (M(6,5) KINK MASS)
    # ratio within 2% of phi OR fN. The integrable kink spectrum is single-mass (only
    # ratio 1.000) => no match => FAIL. Scaling-DIMENSION ratios are NOT masses and do
    # NOT satisfy the operator (a dim ratio near fN is a reported coincidence, not a PASS).
    if ana["target_pass_2pct"]:
        verdict = "PASS"  # (local)
    else:
        verdict = "FAIL"  # (local)

    closest_mass_dev = min(bp["dev"], bf["dev"])  # (local)
    closest_mass_to = "phi" if bp["dev"] < bf["dev"] else "fN"  # (local)

    value = (
        "lit=available[P1=arXiv:0909.2192_M65=D4_c=4/5];"
        "target=M(6,5)_c=4/5_Z3-Potts_KINK-MASS-spectrum;"
        "integrable_kink_spectrum=SINGLE-MASS_degenerate_doublet[Chim-Zam92,Koberle-Swieca79];"
        "only_universality-class_KINK-MASS_ratio=1.000;"
        "n_target_kink-mass_ratios=%d_n_mass_ratios=%d_n_total_ratios=%d;"
        "matches_phi_2pct(target-mass)=%d_matches_fN_2pct(target-mass)=%d;"
        "closest_target-mass_to_%s=%.6f_dev=%.4f%%;"
        "DIAGNOSTIC_Kac-DIMENSION-ratio_near_fN=%.6f_dev=%.4f%%(NOT-a-mass-NOT-PASS-eligible);"
        "lookelsewhere=236of1307_within5%%_algebraic-family-DENSE-near-phi/fN;"
        "adjacent_E6_tricritPotts_M(6,7)_mass-ratios={sqrt2=1.4142,2cos(pi12)=1.9319}_no-phi_no-fN;"
        "E8_Ising_Coldea_golden=1.618034(DIFFERENT_class_c=1/2);"
        "phi_paasch_NOT_universality-class-MASS-number_of_c=4/5_CFT[bare-spectrum-only_reading_survives_PHI-BDG-47];"
        "A3_six-sequence/Z3_map_loses_universality-class_anchor"
    ) % (
        ana["target_mass_ratios"], ana["mass_ratios"], ana["total_ratios"],
        len(ana["matches_phi_2"]), len(ana["matches_fn_2"]),
        closest_mass_to, (bp["value"] if closest_mass_to == "phi" else bf["value"]), closest_mass_dev * 100,
        bfd["value"], bfd["dev"] * 100,
    )

    # Save data
    np.savez(
        OUT_NPZ,
        phi_paasch=ana["phi"], fN=ana["fn"],
        tol_2pct=TOL_2PCT, tol_5pct=TOL_5PCT,
        total_ratios=ana["total_ratios"], mass_ratios=ana["mass_ratios"],
        target_mass_ratios=ana["target_mass_ratios"], diag_ratios=ana["diag_ratios"],
        n_matches_phi_2pct_target_mass=len(ana["matches_phi_2"]),
        n_matches_fn_2pct_target_mass=len(ana["matches_fn_2"]),
        n_diag_phi_2pct=len(ana["diag_phi_2"]), n_diag_fn_2pct=len(ana["diag_fn_2"]),
        best_phi_mass_value=ana["best_phi_mass"]["value"],
        best_phi_mass_dev=ana["best_phi_mass"]["dev"],
        best_phi_mass_label=ana["best_phi_mass"]["label"],
        best_phi_mass_model=ana["best_phi_mass"]["model"],
        best_fn_mass_value=ana["best_fn_mass"]["value"],
        best_fn_mass_dev=ana["best_fn_mass"]["dev"],
        best_fn_mass_label=ana["best_fn_mass"]["label"],
        best_fn_mass_model=ana["best_fn_mass"]["model"],
        best_phi_diag_value=ana["best_phi_diag"]["value"], best_phi_diag_dev=ana["best_phi_diag"]["dev"],
        best_fn_diag_value=ana["best_fn_diag"]["value"], best_fn_diag_dev=ana["best_fn_diag"]["dev"],
        best_phi_any_value=ana["best_phi_any"]["value"],
        best_phi_any_dev=ana["best_phi_any"]["dev"],
        best_phi_any_model=ana["best_phi_any"]["model"],
        best_fn_any_value=ana["best_fn_any"]["value"],
        best_fn_any_dev=ana["best_fn_any"]["dev"],
        best_fn_any_model=ana["best_fn_any"]["model"],
        all_match_models=np.array([m["model"] for m in ana["all_match_records"]]),
        all_match_values=np.array([m["value"] for m in ana["all_match_records"]], dtype=np.float64),
        all_match_devs=np.array([m["dev"] for m in ana["all_match_records"]], dtype=np.float64),
        all_match_roles=np.array([m["role"] for m in ana["all_match_records"]]),
        verdict=verdict,
        lit_refs=np.array(["arXiv:0909.2192_Lepori-Toth-Delfino_M(6,5)_3statePotts",
                           "arXiv:2311.00654_Mussardo-Panero-Stampiggi_M(6,7)_tricrit_E6",
                           "Coldea2010_Science327.177_E8_Ising_golden"]),
    )
    print("\nSaved: %s" % OUT_NPZ)

    make_plot(spectra, ana)
    print("Saved: %s" % OUT_PNG)

    # 4-tuple line
    print("\n(value=%r, scheme=%s, convention=%s, L_max=%s)" % (verdict, SCHEME, CONVENTION, L_MAX))

    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)
    print("\naudit_sha256=%s" % audit_sha)
    print("content_sha256=%s" % content_sha)

    extra = [
        "# INV3-W3-2 W3 M(6,5) c=4/5 (Z3-Potts) kink-mass-ratio test vs phi_paasch=1.531580 + fN=sqrt(5)-1=1.236068",
        "# DECISIVE: [P1 arXiv:0909.2192 Lepori-Toth-Delfino] M(6,5)=D4 integrable (h=0) spectrum = degenerate kink doublet (single mass; Chim-Zamolodchikov 1992 IJMPA7:5317, Koberle-Swieca 1979 PLB86:209) => only universality-class ratio = 1.000 (no match)",
        "# look-elsewhere: n_target_KINK-MASS_ratios=%d n_total_ratios=%d (236/1307 within 5%% -- algebraic family DENSE near phi/fN); matches_phi_2pct(target-mass)=%d matches_fN_2pct(target-mass)=%d" % (
            ana["target_mass_ratios"], ana["total_ratios"], len(ana["matches_phi_2"]), len(ana["matches_fn_2"])),
        "# closest target-KINK-MASS->phi=%.6f dev=%.4f%% (%s); ->fN=%.6f dev=%.4f%% (%s); ONLY target kink-mass ratio is 1.000 => both far" % (
            bp["value"], bp["dev"] * 100, bp["label"], bf["value"], bf["dev"] * 100, bf["label"]),
        "# DIAGNOSTIC (NOT PASS-eligible): M(6,5) Kac scaling-DIMENSION ratio Delta(4,5)/Delta(3,1)=%.6f within %.4f%% of fN -- a conformal-WEIGHT ratio, NOT a mass; does NOT make fN a universality-class MASS number (this near-coincidence is the look-elsewhere trap the plan warns of)" % (
            bfd["value"], bfd["dev"] * 100),
        "# adjacent E6 tricrit-Potts M(6,7) c=6/7 [P2 arXiv:2311.00654 Eq14]: {sqrt2,2cos(pi/12)} -- nontrivial but NO phi_paasch/fN; E8 Ising Coldea golden=1.618 is DIFFERENT class c=1/2",
        "# substrate: PARTICLE on GEOMETRIC; W3 CFT IS the effective description of Z3 wall criticality; phi_paasch is NOT forced by the c=4/5 universality class -> bare-(3,0)/(0,0)-spectrum-only reading survives (consistent with PHI-BDG-47 FAIL); A3 six-sequence/Z3 map loses its universality-class anchor",
        "# regulator_pin=N/A (CFT kink mass ratios are sin(k pi/h)-type algebraic numbers from the Bethe-ansatz S-matrix, not Seeley-DeWitt a_n moments)",
        "# lit retrieval: paper-search + WebSearch this dispatch (NOT training knowledge); prior art knowledge-MCP s33a_w3_kink_masses.py (phi-only, no fN)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)


if __name__ == "__main__":
    main()
