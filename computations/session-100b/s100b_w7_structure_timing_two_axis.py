#!/usr/bin/env python3
"""
S100b W7-3 — S100b-STRUCTURE-TIMING-TWO-AXIS
=============================================
Structure-timing two-axis joint constraint (JWST LRD consistency ceilings, item 19).

Gate: S100b-STRUCTURE-TIMING-TWO-AXIS ([VERIFY])
Plan: sessions/session-plan/session-100b-plan-w7.md SW7-3
Scheme: TWO-AXIS-JOINT-SELECTION-FOLDED
Convention: CONSISTENCY-CEILING-INFO-BY-DESIGN  (EXPECTED verdict: INFO, pre-declared)

WALL LAW (mandatory): `LRD_demographics_not_discriminating` (closed mechanism,
STAGING, sessions/framework/registry/closed-gw-channels.md): LRD/structure
demographics CANNOT discriminate the framework from LCDM at z < 10^28.
PANORAMIC observes z~3-8 and Whitler z~9-16 (~28 OOM below the wall in 1+z).
This gate is a joint constraint / consistency ceiling, INFO-by-design: a PASS
is consistency only (never a framework-vs-LCDM discriminator); a FAIL (an axis
missed by >1 sigma after selection folding, beyond even the eps=1 baryon-budget
ceiling) IS a real constraint on substrate assembly (mack lands the watchlist
row; this gate touches no registry surface).

FOUR AXES (per-paper logical AND, then across papers):
  A1 ABUNDANCE (PANORAMIC Ji arXiv 2604.05022, DECISIVE) — Table-1 gold n(z)
     vs [model-envelope floor (>=1 dex published underprediction at z>~4),
     eps=1 maximal-assembly ceiling n_halo(M_h >= M*/(f_b eps), z)], ST mass
     function on the borrowed Planck-2018 baseline, selection-folded (W7-1).
  A2 CLUSTERING (PANORAMIC, MILD) — sigma_CV = 0.7+-0.3 vs UniverseMachine
     mocks 0.43 (sSFR) / 0.51 (halo-mass); chain 19-1 nearest-edge 0.63 sigma;
     CLUST-43 machinery (growth_factor_ratio + xi_DM, ast-extracted from the
     SHA-pinned s43 script, NOT re-imported as a side-effecting module) for
     the implied-bias inversion. FAIL direction = UNDER-clustering only.
  B1 BOTH-ENDS UV (Whitler arXiv 2501.00984) — rho_UV(z~10) = 2.82e25 (Sch)
     vs rho_UV_max = f_b*eps*rho_dot_Macc/kappa_UV (atomic-cooling-threshold
     collapse-rate ceiling); both-end Phi bins (Table 5) as direction checks.
  B2 STEEP ALPHA (Whitler) — set-membership in [-2.79, -2.16] + direction
     alpha <= -2 (no quantitative substrate alpha: feeds INFO, never PASS).

JOINT 3-TIER: PASS iff all four axes fiducial-hit within 1 sigma (folded);
INFO iff all four axes band-contained (EXPECTED: degenerate-with-LCDM);
FAIL iff any axis > 1 sigma outside the maximal folded band.

Runtime numeral re-verification: pinned values re-extracted from fetched
arXiv text dumps (_s100b_w7_ji_text.txt, _s100b_w7_whitler_text.txt; direct
PDF Read blocked, S99 litrev precedent). Extraction failure on a pinned
numeral = DECLARED PIN GAP routed per-axis to bound-form (litrev SHA-pinned
values stand as bounds), never memory-fill (feedback_research-corpus).

Output 4-tuple:
  (value=<joint tier + per-axis summary>, scheme=TWO-AXIS-JOINT-SELECTION-FOLDED,
   convention=CONSISTENCY-CEILING-INFO-BY-DESIGN, L_max=N/A)

Classification: PHONONIC (assembly IS the GGE interference pattern
self-organizing through the a_2 channel; spatially correlated BY CONSTRUCTION).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (GPU_path: cpu-cap-OMP8;
# scalar/grid integrals, no large linalg -> CPU path per plan pin)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit pins consumed by this gate
    H_0_km_s_Mpc, Omega_m, Omega_b, sigma_8, planck_ns,
    S_capture_floor_LRD_classic, kappa_UV_MadauDickinson,
    G_N_cgs, k_B_SI, M_sun_g, m_proton_g, Mpc_to_cm, c_light_km_s,
)

import ast
import hashlib
import json
import re
import time

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import s100b_selection_fold as selfold  # W7-1 reusable wrapper (HARD input)

# ---------------------------------------------------------------------------
# Section 2 — Identity + pre-registration (plan SW7-3, frozen)
# ---------------------------------------------------------------------------
SESSION = "S100b"                                                  # (local)
GATE_ID = "S100b-STRUCTURE-TIMING-TWO-AXIS"                        # (local)
SCHEME = "TWO-AXIS-JOINT-SELECTION-FOLDED"                         # (local)
CONVENTION = "CONSISTENCY-CEILING-INFO-BY-DESIGN"                  # (local)
L_MAX = "N/A"                                                      # (local) no D_K truncation consumed

# Pre-registered thresholds (plan SW7-3 operator + strict_PASS_boundary)
SIGMA_PER_AXIS = 1.0          # (local) 1 sigma per axis
ONE_DEX = 1.0                 # (local) >=1 dex A1 model-envelope excess criterion
EPS_GRID = np.array([0.1, 0.32, 1.0])   # (local) assembly-efficiency band; eps=1 ceiling
M_STAR_MIN = 1.0e10           # (local) M_sun; PANORAMIC massive threshold
B_SCAN = np.arange(0.5, 12.0 + 1e-9, 0.05)   # (local) bias scan for sigma_CV inversion
ALPHA_BAND = (-2.79, -2.16)   # (local) B2 evaluation band (plan pin)
ALPHA_DIR = -2.0              # (local) substrate fragmentation direction alpha <= -2
N_EVAL_M = 400                # (local) log-spaced M points per z-bin integration
T_VIR_THRESHOLD_K = 1.0e4     # (local) atomic-cooling threshold (B1 ceiling, first-principles)
MU_VIR = 0.6                  # (local) ionized at virialization (plan W7-2 chain 17-3 convention)

OUT_NPZ = SESSION_DIR / "s100b_w7_structure_timing_two_axis.npz"
OUT_PNG = SESSION_DIR / "s100b_w7_structure_timing_two_axis.png"

# Input files (SHA-pinned at runtime; plan-frozen SHAs cross-checked below)
F_CANON = SHARED_DIR / "canonical_constants.py"
F_WRAP = SHARED_DIR / "s100b_selection_fold.py"
F_SELNPZ = SESSION_DIR / "s100b_w7_selection_function_floor.npz"
F_JI_PDF = PROJECT_ROOT / "downloads/research-sweep-s99/jwst-lrd/07_Ji_PANORAMIC-Massive-Quiescent-Number-Density.pdf"
F_WH_PDF = PROJECT_ROOT / "downloads/research-sweep-s99/jwst-lrd/09_Whitler_JADES-z9-UV-Luminosity-Function-Excess.pdf"
F_INDEX = PROJECT_ROOT / "downloads/research-sweep-s99/jwst-lrd/00-INDEX.md"
F_LITLRD = PROJECT_ROOT / "sessions/archive/session-99/session-99-litrev-jwst-lrd-little-red-dots.md"
F_LITMACK = PROJECT_ROOT / "sessions/archive/session-99/session-99-litrev-jwst-lrd-mack.md"
F_S43_PY = PROJECT_ROOT / "computations/session-43/s43_lrd_clustering.py"
F_S43_NPZ = PROJECT_ROOT / "computations/session-43/s43_lrd_clustering.npz"
F_JI_TXT = SESSION_DIR / "_s100b_w7_ji_text.txt"
F_WH_TXT = SESSION_DIR / "_s100b_w7_whitler_text.txt"

INPUT_FILES = [F_CANON, F_WRAP, F_SELNPZ, F_JI_PDF, F_WH_PDF, F_INDEX,
               F_LITLRD, F_LITMACK, F_S43_PY, F_S43_NPZ, F_JI_TXT, F_WH_TXT]

PLAN_SHAS = {                                                      # (local) plan-frozen pins
    "07_Ji": "1c9f1d937463107c294bb981ccd21835bd58beba9e82752180c335425055f5c3",
    "09_Whitler": "ed78172da88ce2329e64d23320bec0b1ce014cc846f3ac11ab24a24737cd8969",
    "00-INDEX": "246bb0c6ff4d4c7885848d12fdb65b227be44312e27d1502a2540f5d33128801",
    "litrev_lrd": "884f99606ba951fa117df98251be0eb3c26a5dfa49d7c5fc35c6764ad352c1fb",
    "litrev_mack": "e83c2a0f42f71de904acbaf3906f7501564c31a44b628ed7b88ee13402460f35",
    "s43_py": "842d8711340d6798b3245512c5393542f68e8ee1bd9305ef1df11e7aabb32429",
    "s43_npz": "13e691e47ecd1ed06e42d20327c3b83c6fca4ab8da8651e548b98d01cce81ccb",
}

MACHINERY_PIN_MAP = {                                              # (local) plan SW7-3 (5)
    "N_eval": "400 log-spaced M points per z-bin; z-bins A {3-3.5,3.5-4,4-5,5-6,6-8}; B {9-12, 12-16}",
    "L_max": "N/A",
    "scan_range": "eps in {0.1, 0.32, 1.0}; b-scan [0.5, 12] step 0.05",
    "step_size": "adaptive (quad) for sigma(M); b-scan 0.05",
    "tolerance": "1 sigma per axis; >=1 dex on A1; band edges as pinned",
    "scheme": SCHEME, "convention": CONVENTION,
    "random_seed": "N/A - deterministic", "GPU_path": "cpu-cap-OMP8",
    "expected_verdict": "INFO (pre-declared; degenerate-with-LCDM below z=1e28)",
    "mass_function": "Sheth-Tormen (A=0.3222, a=0.707, p=0.3); EH98 no-wiggle transfer; top-hat W(kR)",
    "cosmology_baseline": "Planck 2018 canonical imports H_0=67.4, Omega_m=0.315, Omega_b=0.0493, sigma_8=0.811, n_s=0.9649",
    "kappa_UV": "kappa_UV_MadauDickinson = 1.15e-28 (canonical, added-with-provenance S100b)",
    "selection_fold": "s100b_w7_selection_function_floor.npz (HARD; EXTRACTION-LIMITED-BOUND-FORM flat S=[0.25,1.0])",
    "clustering_machinery": "CLUST-43 ast-extracted growth_factor_ratio/xi_DM/wp_DM (S43 SHA-pinned; S43 b=2.0+-0.5 cited as context only)",
    "publication_precision": "per-axis distances 2 sig figs; band edges 3 sig figs; npz float64",
}

# ---------------------------------------------------------------------------
# Section 3 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes()        # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 4 — Runtime numeral extraction (fetched text only; pin gaps declared)
# ---------------------------------------------------------------------------

def extract_ji(txt: str) -> dict:
    """Extract PANORAMIC (Ji) pinned numerals from fetched arXiv text."""
    out = {"status": {}}  # (local)

    # Table 1 (gold + gold+silver, 5 z-bins each): "(3.0, 3.5)\n36\n$1.81\pm 0.53$\n0.06"
    m = re.search(r"Redshift\s*\nN\s*\nNumber density(.*?)Table 1:", txt, re.S)  # (local)
    rows = []  # (local)
    if m:
        rows = re.findall(
            r"\((\d\.\d),\s*(\d\.\d)\)\s*\n(\d+)\s*\n\$([\d.]+)\\pm\s+([\d.]+)\$\s*\n([\d.]+)",
            m.group(1))
    if len(rows) == 10:
        arr = np.array([[float(a), float(b), float(n), float(v), float(e), float(cv)]
                        for a, b, n, v, e, cv in rows])  # (local)
        out["gold"] = arr[:5]          # zlo, zhi, N, n(1e-5), err(1e-5), cv_tilde
        out["goldsilver"] = arr[5:]
        out["status"]["table1"] = "EXTRACTED"
    else:
        out["gold"] = None; out["goldsilver"] = None
        out["status"]["table1"] = f"PIN-GAP({len(rows)} rows)"

    # sigma_CV observed: "sigma_{\rm CV}\approx 0.7\pm 0.3"
    m = re.search(r"\\sigma_\{\\rm CV\}\\approx\s*([\d.]+)\\pm\s*([\d.]+)", txt)
    if m:
        out["sigma_cv_obs"] = (float(m.group(1)), float(m.group(2)))
        out["status"]["sigma_cv_obs"] = "EXTRACTED"
    else:
        out["sigma_cv_obs"] = None; out["status"]["sigma_cv_obs"] = "PIN-GAP"

    # two-estimator detail: 0.71^{+0.20}_{-0.28} bootstrap; 0.65^{+0.25}_{-0.30} MCMC
    est = re.findall(r"\\sigma_\{\\rm CV\}=([\d.]+)\^\{\+([\d.]+)\}_\{-([\d.]+)\}", txt)  # (local)
    out["sigma_cv_estimators"] = [[float(x) for x in t] for t in est[:2]] if est else []

    # mock intrinsic values: "intrinsic cosmic variance ... \sigma_{\rm CV}\sim 0.43 / 0.51"
    mocks = re.findall(r"intrinsic cosmic variance[^$]*?\$\\sigma_\{\\rm CV\}\\sim\s*([\d.]+)\$", txt)  # (local)
    if len(mocks) >= 2:
        vals = sorted(float(x) for x in mocks[:2])  # (local)
        out["mock_ssfr"], out["mock_halo"] = vals[0], vals[1]
        out["status"]["mocks"] = "EXTRACTED"
    else:
        out["mock_ssfr"] = out["mock_halo"] = None
        out["status"]["mocks"] = "PIN-GAP"

    # >=1 dex underprediction claim (z >~ 4)
    out["one_dex_claim"] = bool(re.search(
        r"underpredict the abundance of massive quiescent galaxies at \$z\\gtrsim 4\$ by \$\\gtrsim 1\$\s*dex", txt))
    out["status"]["one_dex"] = "EXTRACTED" if out["one_dex_claim"] else "PIN-GAP"

    # sample counts + sightlines
    m = re.search(r"(\d+) galaxies in a gold sample", txt)
    out["n_gold"] = int(m.group(1)) if m else None
    m = re.search(r"(\d+) in a more inclusive silver sample", txt)
    out["n_silver"] = int(m.group(1)) if m else None
    m = re.search(r"(\d+) independent sightlines", txt)
    out["n_sightlines"] = int(m.group(1)) if m else None
    out["status"]["counts"] = ("EXTRACTED" if all(v is not None for v in
                               (out["n_gold"], out["n_silver"], out["n_sightlines"])) else "PIN-GAP")

    # abstract gold/silver z=3-4 pair "(1.5$ vs. $3.1)\times 10^{-5}"
    out["z34_pair"] = bool(re.search(r"\(1\.5\$\s*vs\.\s*\$3\.1\)\\times 10\^\{-5\}", txt))

    # survey area + pointing-scale anchors (pointing area in arcmin^2 NOT stated
    # numerically in fetched text -> DECLARED PIN GAP; bound-form anchors below)
    m = re.search(r"(\d+)\s*arcmin2 of NIRCam imaging across", txt)
    out["area_arcmin2"] = float(m.group(1)) if m else None
    out["pointing_mpc_anchor"] = bool(re.search(
        r"out to \$\\sim 1\$\s*–\s*\$2\$\s*Mpc, comparable to the size of a single NIRCam pointing", txt))
    out["status"]["pointing_area"] = "PIN-GAP-BOUND-FORM"  # no numeric arcmin^2 for one pointing
    return out


def extract_whitler(txt: str) -> dict:
    """Extract Whitler (JADES z>9 UVLF) pinned numerals from fetched arXiv text."""
    out = {"status": {}}  # (local)
    TRIPLE = r"\$(-?[\d.]+)_\{-([\d.]+)\}\^\{\+([\d.]+)\}\$"  # (local)

    # Table 6 region
    m = re.search(r"Table 6:(.*?)We also note that", txt, re.S)  # (local)
    if m:
        reg = m.group(1)  # (local)
        i115 = reg.find("F115W dropouts"); i150 = reg.find("F150W dropouts")  # (local)
        t115 = re.findall(TRIPLE, reg[i115:i150])  # (local) 9 triples: Sch 4 + DPL 5
        t150 = re.findall(TRIPLE, reg[i150:])      # (local) 7 triples: Sch 3 + DPL 4
        ok = (len(t115) == 9 and len(t150) == 7)  # (local)
        if ok:
            f = lambda t: (float(t[0]), float(t[1]), float(t[2]))  # (local) (val, -err, +err)
            out["sch_z10"] = {"phistar": f(t115[0]), "Mstar": f(t115[1]),
                              "alpha": f(t115[2]), "rho": f(t115[3])}
            out["dpl_z10"] = {"phistar": f(t115[4]), "Mstar": f(t115[5]),
                              "alpha": f(t115[6]), "beta": f(t115[7]), "rho": f(t115[8])}
            out["sch_z13"] = {"phistar": f(t150[0]), "alpha": f(t150[1]), "rho": f(t150[2])}
            out["dpl_z13"] = {"phistar": f(t150[3]), "alpha": f(t150[4]),
                              "beta": f(t150[5]), "rho": f(t150[6])}
            out["status"]["table6"] = "EXTRACTED"
        else:
            out["status"]["table6"] = f"PIN-GAP({len(t115)}/{len(t150)})"
    else:
        out["status"]["table6"] = "PIN-GAP"

    # Table 5 binned LF: "$-21.4\pm 0.5$\n$0.40_{-0.27}^{+0.45}$"
    m = re.search(r"Table 5:(.*?)We calculate the luminosity function", txt, re.S)
    bins = []  # (local)
    if m:
        bins = re.findall(r"\$(-[\d.]+)\\pm\s+([\d.]+)\$\s*\n" + TRIPLE, m.group(1))
    if len(bins) >= 9:
        arr = np.array([[float(x) for x in b] for b in bins])  # (local) MUV, dMUV, phi, -e, +e
        out["bins_z10"] = arr[:5]   # F115W dropouts (z_med 9.8)
        out["bins_z13"] = arr[5:9]  # F150W dropouts (z_med 12.8)
        out["status"]["table5"] = "EXTRACTED"
    else:
        out["bins_z10"] = out["bins_z13"] = None
        out["status"]["table5"] = f"PIN-GAP({len(bins)} bins)"

    # z_medians
    zm = re.findall(r"z_\{\\mathrm\{median\}\}=([\d.]+)", txt)  # (local)
    out["z_medians"] = [float(x) for x in zm[:3]]
    out["status"]["z_medians"] = "EXTRACTED" if len(zm) >= 2 else "PIN-GAP"

    # prose pins: phi* decline ~2.1-2.3; rho_UV 2.82e25 -> 0.93e25 (~three) -> <2.51e24
    out["phistar_decline_prose"] = bool(re.search(r"declines by a factor of \$\\sim 2\.1-2\.3\$", txt))
    out["rho_prose"] = bool(re.search(
        r"\\rho_\{\\textsc\{uv\}\}=2\.82\\times 10\^\{25\}", txt))
    out["rho_z13_prose"] = bool(re.search(r"0\.93\\times 10\^\{25\}", txt))
    out["rho_z16_limit"] = bool(re.search(r"2\.51\\times 10\^\{24\}", txt))
    m = re.search(r"faint limit of \$M_\{\\textsc\{uv\}\}=(-\d+)\$", txt)
    out["MUV_faint_limit"] = float(m.group(1)) if m else None
    # prose z~13 alphas (-2.29 / -2.41) for drift disclosure vs Table 6 (-2.23 / -2.42)
    out["alpha_z13_prose"] = bool(re.search(
        r"\\alpha_\{\\text\{Schechter\}\}=-2\.29\$ and \$\\alpha_\{\\text\{DPL\}\}=-2\.41", txt))
    # both-ends excess direction statements
    out["excess_direction"] = bool(re.search(
        r"number densities at \$z\\sim 10\$ that are slightly higher than many pre-JWST", txt))
    return out


# ---------------------------------------------------------------------------
# Section 5 — CLUST-43 machinery reuse (ast-extracted from SHA-pinned source)
# ---------------------------------------------------------------------------

def load_clust43_machinery(path: Path) -> dict:
    """Extract growth_factor_ratio / xi_DM / wp_DM function defs from the
    SHA-pinned S43 script WITHOUT executing its top-level body (which would
    rewrite the pinned S43 npz/png artifacts). Byte-exact machinery reuse."""
    src = path.read_text(encoding="utf-8")  # (local)
    tree = ast.parse(src)  # (local)
    wanted = {"growth_factor_ratio", "xi_DM", "wp_DM"}  # (local)
    ns = {"np": np, "H0": H_0_km_s_Mpc}  # (local) S43 module globals the funcs reference
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in wanted:
            seg = ast.get_source_segment(src, node)  # (local)
            exec(compile(seg, str(path), "exec"), ns)
    missing = wanted - set(ns)  # (local)
    if missing:
        raise RuntimeError(f"CLUST-43 machinery extraction failed: {missing}")
    return ns


# ---------------------------------------------------------------------------
# Section 6 — Borrowed Planck-2018 baseline: EH98 no-wiggle + Sheth-Tormen
# ---------------------------------------------------------------------------
h_hub = H_0_km_s_Mpc / 100.0                      # (local) dimensionless Hubble
Omega_L = 1.0 - Omega_m                           # (local) flat baseline
f_b = Omega_b / Omega_m                           # (local) cosmic baryon fraction
T_CMB_over_2p7 = 2.7255 / 2.7                     # (local) EH98 Theta_2.7 (FIRAS T_CMB)
delta_c_sc = 3.0 / 20.0 * (12.0 * np.pi) ** (2.0 / 3.0)  # (local) EdS spherical collapse 1.68647
Delta_c_vir = 18.0 * np.pi ** 2                   # (local) EdS virial overdensity (z>=6 valid)
# rho_crit,0 and comoving matter density in M_sun / Mpc^3 (cgs route)
H0_s = H_0_km_s_Mpc * 1.0e5 / Mpc_to_cm           # (local) H0 in s^-1
rho_crit0_cgs = 3.0 * H0_s ** 2 / (8.0 * np.pi * G_N_cgs)   # (local) g/cm^3
rho_crit0 = rho_crit0_cgs * Mpc_to_cm ** 3 / M_sun_g        # (local) M_sun/Mpc^3
rho_m0 = Omega_m * rho_crit0                      # (local) comoving matter density


def E_of_z(z):
    """H(z)/H0, flat LCDM late-epoch (radiation negligible at z<=16, <0.5%)."""
    return np.sqrt(Omega_m * (1.0 + z) ** 3 + Omega_L)


def H_of_z_s(z):
    return H0_s * E_of_z(z)


def Dc_of_z(z):
    """Comoving distance [Mpc]."""
    val, _ = quad(lambda zz: 1.0 / E_of_z(zz), 0.0, z, limit=200)  # (local)
    return (c_light_km_s / H_0_km_s_Mpc) * val


def T_EH98_nowiggle(k_mpc):
    """Eisenstein-Hu 1998 zero-baryon (no-wiggle) transfer function; k in Mpc^-1."""
    om_h2 = Omega_m * h_hub ** 2                  # (local)
    ob_h2 = Omega_b * h_hub ** 2                  # (local)
    s_eh = 44.5 * np.log(9.83 / om_h2) / np.sqrt(1.0 + 10.0 * ob_h2 ** 0.75)  # (local) sound horizon Mpc
    a_g = (1.0 - 0.328 * np.log(431.0 * om_h2) * f_b
           + 0.38 * np.log(22.3 * om_h2) * f_b ** 2)  # (local) alpha_Gamma
    gamma_eff = Omega_m * h_hub * (a_g + (1.0 - a_g) / (1.0 + (0.43 * k_mpc * s_eh) ** 4))  # (local)
    q = (k_mpc / h_hub) * T_CMB_over_2p7 ** 2 / gamma_eff  # (local)
    L0 = np.log(2.0 * np.e + 1.8 * q)             # (local)
    C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)          # (local)
    return L0 / (L0 + C0 * q ** 2)


def _sigma2_integrand(lnk, R):
    k = np.exp(lnk)                               # (local)
    x = k * R                                     # (local)
    W = 3.0 * (np.sin(x) - x * np.cos(x)) / x ** 3  # (local) top-hat
    return k ** 3 * k ** planck_ns * T_EH98_nowiggle(k) ** 2 * W ** 2 / (2.0 * np.pi ** 2)


def sigma_R_unnorm(R):
    val, _ = quad(_sigma2_integrand, np.log(1e-5), np.log(1e3), args=(R,),
                  limit=400, epsrel=1e-7)  # (local)
    return np.sqrt(val)


# Normalize to sigma_8 at R8 = 8/h Mpc, z=0
R8 = 8.0 / h_hub                                  # (local)
A_norm = sigma_8 / sigma_R_unnorm(R8)             # (local) P(k) amplitude factor

# Master lnsigma(lnM) spline (z=0), M in M_sun over 1e5..1e17
_M_tab = np.logspace(5, 17, 481)                  # (local)
_R_tab = (3.0 * _M_tab / (4.0 * np.pi * rho_m0)) ** (1.0 / 3.0)  # (local)
_sig_tab = np.array([A_norm * sigma_R_unnorm(R) for R in _R_tab])  # (local)
_lnsig_spl = CubicSpline(np.log(_M_tab), np.log(_sig_tab))  # (local)


def sigma_M0(M):
    return np.exp(_lnsig_spl(np.log(M)))


def dlnsig_dlnM(M):
    return _lnsig_spl(np.log(M), 1)


# Sheth-Tormen multiplicity (plan pin: A=0.3222, a=0.707, p=0.3)
ST_A, ST_a, ST_p = 0.3222, 0.707, 0.3             # (local) plan-pinned ST parameters


def f_ST(sig):
    nu = delta_c_sc / sig                          # (local)
    return (ST_A * np.sqrt(2.0 * ST_a / np.pi)
            * (1.0 + (1.0 / (ST_a * nu ** 2)) ** ST_p) * nu
            * np.exp(-ST_a * nu ** 2 / 2.0))


def n_halo_above(M_min, z, Dz):
    """Comoving number density of halos with M > M_min [Mpc^-3] (ST)."""
    lnM = np.linspace(np.log(M_min), np.log(1e16), N_EVAL_M)  # (local)
    M = np.exp(lnM)                                # (local)
    sig = sigma_M0(M) * Dz                         # (local)
    integ = (rho_m0 / M) * f_ST(sig) * np.abs(dlnsig_dlnM(M))  # (local) dn/dlnM
    return np.trapezoid(integ, lnM)


def F_coll_above(M_min, z, Dz):
    """Collapsed mass fraction in halos with M > M_min (ST)."""
    lnM = np.linspace(np.log(M_min), np.log(1e16), N_EVAL_M)  # (local)
    M = np.exp(lnM)                                # (local)
    sig = sigma_M0(M) * Dz                         # (local)
    integ = f_ST(sig) * np.abs(dlnsig_dlnM(M))     # (local) M*(dn/dlnM)/rho_m
    return np.trapezoid(integ, lnM)


def M_ACH(z):
    """Atomic-cooling-threshold halo mass [M_sun] from the virial theorem +
    EdS spherical collapse (first-principles; plan W7-2 chain 17-3 form):
      T_vir = (mu m_p / 2 k_B) (G M H(z))^(2/3) (Delta_c/2)^(1/3)
    inverted at T_vir = 1e4 K. cgs internally."""
    kB_cgs = k_B_SI * 1.0e7                        # (local) erg/K
    v2 = 2.0 * kB_cgs * T_VIR_THRESHOLD_K / (MU_VIR * m_proton_g)  # (local) cm^2/s^2
    M_g = v2 ** 1.5 / (G_N_cgs * H_of_z_s(z) * np.sqrt(Delta_c_vir / 2.0))  # (local) g
    return M_g / M_sun_g


# ---------------------------------------------------------------------------
# Section 7 — Pencil-beam matter variance (CLUST-43 xi_DM; deterministic GL)
# ---------------------------------------------------------------------------

def sigma2_box(a_t, L_z, z, xi_func, n_t=24, n_z=64):
    """Count-in-cell matter variance for a box a_t x a_t x L_z [cMpc] at z:
      sigma^2 = 8/(a^4 L^2) Int (a-x)(a-y)(L-w) xi(sqrt(x^2+y^2+w^2)) dx dy dw
    Gauss-Legendre, deterministic (random_seed N/A). Transverse [0,a] x2 axes;
    line-of-sight split [0, min(20a,L)] + log-spaced tail."""
    xg, wg = np.polynomial.legendre.leggauss(n_t)  # (local)
    x = 0.5 * a_t * (xg + 1.0); wx = 0.5 * a_t * wg  # (local)
    w_near_end = min(20.0 * a_t, L_z)              # (local)
    zg, wzg = np.polynomial.legendre.leggauss(n_z)  # (local)
    z1 = 0.5 * w_near_end * (zg + 1.0); wz1 = 0.5 * w_near_end * wzg  # (local)
    if L_z > w_near_end * (1.0 + 1e-12):
        lo, hi = np.log(w_near_end), np.log(L_z)   # (local)
        u = 0.5 * (hi - lo) * (zg + 1.0) + lo      # (local)
        z2 = np.exp(u); wz2 = 0.5 * (hi - lo) * wzg * z2  # (local) log-measure
        zz = np.concatenate([z1, z2]); wzz = np.concatenate([wz1, wz2])  # (local)
    else:
        zz, wzz = z1, wz1                          # (local)
    X, Y, Z = np.meshgrid(x, x, zz, indexing="ij")  # (local)
    WX, WY, WZ = np.meshgrid(wx, wx, wzz, indexing="ij")  # (local)
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)          # (local)
    xi = xi_func(r, z)                             # (local)
    kern = (a_t - X) * (a_t - Y) * (L_z - Z) * xi * WX * WY * WZ  # (local)
    return 8.0 * np.sum(kern) / (a_t ** 4 * L_z ** 2)


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload emission (template script-template.py Section 6)
# ---------------------------------------------------------------------------

def print_verdict_payload(payload: dict) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe, syntax-forced; per
    `.claude/rules/gate-verdicts.md` 'Race-Safe Emission'). The script does
    NOT write the verdict file — a raw open("a") append is NOT atomic across
    processes on Windows (S98 lost 5/8 lines under 8 concurrent writers)."""
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main computation
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    # machinery pin map joins the audit closure (plan SW7-3 audit_discriminators)
    mach_json = json.dumps(MACHINERY_PIN_MAP, sort_keys=True)  # (local)
    pins["__machinery_pin_map__"] = hashlib.sha256(mach_json.encode()).hexdigest()
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, F_CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # CC-PIN: plan-frozen SHA cross-check (static inputs)
    cc_pin = {
        "07_Ji": pins["downloads/research-sweep-s99/jwst-lrd/07_Ji_PANORAMIC-Massive-Quiescent-Number-Density.pdf"] == PLAN_SHAS["07_Ji"],
        "09_Whitler": pins["downloads/research-sweep-s99/jwst-lrd/09_Whitler_JADES-z9-UV-Luminosity-Function-Excess.pdf"] == PLAN_SHAS["09_Whitler"],
        "00-INDEX": pins["downloads/research-sweep-s99/jwst-lrd/00-INDEX.md"] == PLAN_SHAS["00-INDEX"],
        "litrev_lrd": pins["sessions/archive/session-99/session-99-litrev-jwst-lrd-little-red-dots.md"] == PLAN_SHAS["litrev_lrd"],
        "litrev_mack": pins["sessions/archive/session-99/session-99-litrev-jwst-lrd-mack.md"] == PLAN_SHAS["litrev_mack"],
        "s43_py": pins["computations/session-43/s43_lrd_clustering.py"] == PLAN_SHAS["s43_py"],
        "s43_npz": pins["computations/session-43/s43_lrd_clustering.npz"] == PLAN_SHAS["s43_npz"],
    }  # (local)
    print(f"CC-PIN plan-frozen SHA match: {cc_pin} -> {'PASS' if all(cc_pin.values()) else 'FAIL'}")

    # --- W7-1 HARD input: selection band ---
    band = selfold.load_band_npz(F_SELNPZ)  # (local)
    S_lo = float(band["S_band_lo"][0]); S_hi = float(band["S_band_hi"][0])  # (local)
    band_flat = (np.ptp(band["S_band_lo"]) == 0.0 and np.ptp(band["S_band_hi"]) == 0.0)  # (local)
    W_fold = 1.0 / S_lo                            # (local) upward widening factor (=4)
    print(f"\nW7-1 selection band: S=[{S_lo}, {S_hi}] flat={band_flat} "
          f"W={W_fold:.3f} status={band['extraction_status']}")
    # CC5: band sanity + canonical floor consistency
    cc5 = (abs(S_lo - S_capture_floor_LRD_classic) < 1e-12 and S_hi == 1.0 and band_flat)  # (local)
    print(f"CC5 selection-band sanity (S_lo==canonical 0.25, S_hi==1, flat): {'PASS' if cc5 else 'FAIL'}")
    # Fold-invariance of fractional/shape axes under a FLAT multiplicative band:
    # counts N -> S*N has fractional variance sigma_CV unchanged; d ln phi / dM
    # (alpha) unchanged. EXACT given band_flat=True. A1/B1 (densities) widen by W.

    # --- Runtime extraction (fetched text only) ---
    ji = extract_ji(F_JI_TXT.read_text(encoding="utf-8"))
    wh = extract_whitler(F_WH_TXT.read_text(encoding="utf-8"))
    print(f"\nJi extraction status: {ji['status']}")
    print(f"Whitler extraction status: {wh['status']}")

    decisive_ok = (ji["status"]["table1"] == "EXTRACTED"
                   and ji["status"]["sigma_cv_obs"] == "EXTRACTED"
                   and ji["status"]["mocks"] == "EXTRACTED"
                   and wh["status"]["table6"] == "EXTRACTED"
                   and wh["status"]["table5"] == "EXTRACTED")  # (local)

    # Plan-pin re-verification (CC4)
    g = ji["gold"]; gs = ji["goldsilver"]  # (local)
    cc4 = {}  # (local)
    if g is not None:
        cc4["A1_gold_first_1.81"] = abs(g[0, 3] - 1.81) < 1e-9
        cc4["A1_gold_last_0.07"] = abs(g[4, 3] - 0.07) < 1e-9
        cc4["A1_gold_N_sum_101"] = int(g[:, 2].sum()) == 101
        cc4["A1_goldsilver_N_sum_238"] = int(gs[:, 2].sum()) == 238
    cc4["A2_sigma_cv_0.7pm0.3"] = ji["sigma_cv_obs"] == (0.7, 0.3)
    cc4["A2_mocks_0.43_0.51"] = (ji["mock_ssfr"] == 0.43 and ji["mock_halo"] == 0.51)
    cc4["A1_one_dex_claim"] = ji["one_dex_claim"]
    cc4["A1_z34_pair_1.5_3.1"] = ji["z34_pair"]
    if wh["status"]["table6"] == "EXTRACTED":
        cc4["B2_alpha_sch_z10_-2.36"] = abs(wh["sch_z10"]["alpha"][0] + 2.36) < 1e-9
        cc4["B2_alpha_dpl_z10_-2.60"] = abs(wh["dpl_z10"]["alpha"][0] + 2.60) < 1e-9
        cc4["B1_rho_sch_z10_2.82"] = abs(wh["sch_z10"]["rho"][0] - 2.82) < 1e-9
        cc4["B1_rho_errs_-0.33+0.34"] = (abs(wh["sch_z10"]["rho"][1] - 0.33) < 1e-9
                                         and abs(wh["sch_z10"]["rho"][2] - 0.34) < 1e-9)
    cc4["B1_phistar_decline_2.1-2.3"] = wh["phistar_decline_prose"]
    cc4["B1_rho_z13_0.93_prose"] = wh["rho_z13_prose"]
    print(f"CC4 plan-pin re-verification: {cc4} -> {'PASS' if all(cc4.values()) else 'PARTIAL'}")

    # Table-6-vs-prose alpha(z~13) drift disclosure (NOT a pin failure; both recorded)
    alpha_z13_table = (wh["sch_z13"]["alpha"][0], wh["dpl_z13"]["alpha"][0]) \
        if wh["status"]["table6"] == "EXTRACTED" else (np.nan, np.nan)  # (local)
    print(f"alpha(z~13): Table 6 = {alpha_z13_table} | prose -2.29/-2.41 present = {wh['alpha_z13_prose']}"
          f" (plan pin cites prose; both inside evaluation band — disclosed drift)")

    # --- CLUST-43 machinery (ast-extracted) + CC1 fidelity ---
    c43 = load_clust43_machinery(F_S43_PY)
    s43 = np.load(F_S43_NPZ)  # (local)
    wp_re = np.array([c43["wp_DM"](rp, float(s43["z_eff"])) for rp in s43["rp_bins"]])  # (local)
    cc1_rel = float(np.max(np.abs(wp_re - s43["wp_dm"]) / np.abs(s43["wp_dm"])))  # (local)
    cc1 = cc1_rel < 1e-8  # (local)
    print(f"CC1 CLUST-43 machinery fidelity: max rel dev = {cc1_rel:.2e} -> {'PASS' if cc1 else 'FAIL'}")
    print(f"   (S43 context: b_measured = {float(s43['b_measured']):.1f} +- {float(s43['b_err']):.1f}"
          f" is the LRD population — machinery+context only, NOT an A2 datum)")

    # Growth-factor table for speed
    Dz_cache = {}  # (local)

    def Dz(z):
        if z not in Dz_cache:
            Dz_cache[z] = float(c43["growth_factor_ratio"](z))
        return Dz_cache[z]

    # CC6: sigma_8 normalization round-trip
    cc6_val = abs(A_norm * sigma_R_unnorm(R8) - sigma_8)  # (local)
    cc6 = cc6_val < 1e-10  # (local)
    print(f"CC6 sigma_8 round-trip: |sigma(R8)-sigma_8| = {cc6_val:.2e} -> {'PASS' if cc6 else 'FAIL'}")

    # =====================================================================
    # CHAIN 19-2 (pre-registered): eps=1 maximal-assembly ceiling direction
    #   Step 1: M_h_min(eps) = M*/(f_b*eps); f_b = Omega_b/Omega_m
    #   Step 2: eps=1 -> M_h_min = 1e10/f_b
    #   Step 3: n_max(z) = Int_{M_h_min} (dn/dM) dM  [Sheth-Tormen]
    #   Step 4: compare n_obs,folded <= n_max per bin; rho_UV analog
    #   Direction: obs BELOW ceiling = INFO-side; >1 sigma ABOVE = FAIL-side
    # =====================================================================
    M_h_min_eps1 = M_STAR_MIN / (f_b * 1.0)  # (local)
    cc3 = (abs(f_b - 0.1565) / 0.1565 < 0.01) and (abs(M_h_min_eps1 - 6.39e10) / 6.39e10 < 0.01)  # (local)
    print(f"\nCHAIN 19-2: f_b = {f_b:.5f} (plan 0.1565); M_h_min(eps=1) = {M_h_min_eps1:.3e} "
          f"(plan 6.39e10) -> CC3 {'PASS' if cc3 else 'FAIL'}")

    # ---------------- A1 ABUNDANCE (DECISIVE) ----------------
    z_mids = 0.5 * (g[:, 0] + g[:, 1])             # (local) bin midpoints
    n_obs = g[:, 3] * 1e-5                         # (local) Mpc^-3
    n_err = g[:, 4] * 1e-5                         # (local) published 1sigma (incl CV)
    n_max_bins = np.zeros((len(EPS_GRID), len(z_mids)))  # (local)
    for i, eps in enumerate(EPS_GRID):
        Mh = M_STAR_MIN / (f_b * eps)              # (local)
        for j, zm in enumerate(z_mids):
            n_max_bins[i, j] = n_halo_above(Mh, zm, Dz(zm))
    n_max_eps1 = n_max_bins[-1]                    # (local) eps=1 ceiling per bin
    # model envelope from the published >=1 dex underprediction (z>~4 bins)
    env_lo = np.where(z_mids >= 4.0, n_obs / 10 ** ONE_DEX, np.nan)  # (local)
    # folded intrinsic band: [(n-err)/S_hi, (n+err)/S_lo]
    a1_lo = np.maximum(n_obs - n_err, 1e-12) / S_hi  # (local)
    a1_hi = (n_obs + n_err) / S_lo                 # (local)
    a1_contained = a1_lo <= n_max_eps1             # (local) ceiling side (envelope side: a1_hi >= env_lo trivially)
    a1_excluded = (n_obs - SIGMA_PER_AXIS * n_err) / S_hi > n_max_eps1  # (local) >1sig above eps=1 ceiling at most favorable fold
    a1_sigdist = np.where(a1_contained, 0.0, (n_obs / S_hi - n_max_eps1) / n_err)  # (local)
    a1_headroom_dex = np.log10(n_max_eps1 / a1_hi)  # (local) ceiling minus folded UPPER edge
    a1_fid_hit = np.abs(n_max_eps1 - n_obs) <= SIGMA_PER_AXIS * n_err  # (local) maximal-coherence fiducial
    print("\nA1 ABUNDANCE (gold, Table 1 re-extracted):")
    for j, zm in enumerate(z_mids):
        print(f"  z={g[j,0]}-{g[j,1]} (mid {zm}): n={n_obs[j]:.2e}+-{n_err[j]:.2e} "
              f"folded=[{a1_lo[j]:.2e},{a1_hi[j]:.2e}] ceiling(eps=1)={n_max_eps1[j]:.2e} "
              f"headroom={a1_headroom_dex[j]:+.2f}dex contained={a1_contained[j]}")
    print(f"  A1 contained {int(a1_contained.sum())}/5; excluded any: {bool(a1_excluded.any())}; "
          f"fiducial hits: {int(a1_fid_hit.sum())}/5")
    print(f"  envelope (>=1dex published claim, z>~4 bins): env_lo = n_obs/10 -> "
          f"folded upper edge {a1_hi[2]:.2e} >= env {env_lo[2]:.2e} at z=4.5 (floor side trivially inside)")

    # ---------------- A2 CLUSTERING (MILD) ----------------
    # CHAIN 19-1 (pre-registered): MILD-axis significance; direction OVERLAP <1sig
    scv, scv_err = ji["sigma_cv_obs"]              # (local) 0.7, 0.3
    mock_lo, mock_hi = ji["mock_ssfr"], ji["mock_halo"]  # (local) 0.43, 0.51
    obs_int = (scv - scv_err, scv + scv_err)       # (local) [0.4, 1.0]
    overlap = (obs_int[0] <= mock_hi) and (obs_int[1] >= mock_lo)  # (local)
    nearest_edge_sigma = (scv - mock_hi) / scv_err  # (local) (0.7-0.51)/0.3
    cc2 = overlap and abs(nearest_edge_sigma - 0.6333333) < 1e-3 and nearest_edge_sigma < 1.0  # (local)
    print(f"\nCHAIN 19-1: obs 1sig interval [{obs_int[0]:.2f},{obs_int[1]:.2f}] vs mocks "
          f"[{mock_lo},{mock_hi}]: overlap={overlap}; nearest-edge=({scv}-{mock_hi})/{scv_err}"
          f"={nearest_edge_sigma:.4f} sigma < 1 -> MILD -> CC2 {'PASS' if cc2 else 'FAIL'}")
    a2_dir_overclust = scv > mock_hi               # (local) substrate-favorable direction
    a2_underclust_fail = (scv + SIGMA_PER_AXIS * scv_err) < mock_lo  # (local) ONLY FAIL direction
    a2_contained = overlap and not a2_underclust_fail  # (local)
    a2_fid_hit = abs(scv - mock_hi) <= SIGMA_PER_AXIS * scv_err  # (local) fiducial: over-clustering at halo-matched edge
    # geometry-FREE implied bias EXCESS over UniverseMachine (sigma_DM cancels)
    bias_ratio_central = (scv / mock_hi, scv / mock_lo)  # (local) [1.37, 1.63]
    bias_ratio_1sig = (obs_int[0] / mock_hi, obs_int[1] / mock_lo)  # (local) [0.78, 2.33]
    print(f"  A2 fold-invariant under flat S-band (multiplicative capture cancels in fractional CV): exact")
    print(f"  implied bias excess b_obs/b_mock: central [{bias_ratio_central[0]:.2f},"
          f"{bias_ratio_central[1]:.2f}], 1sig [{bias_ratio_1sig[0]:.2f},{bias_ratio_1sig[1]:.2f}]")

    # absolute b inversion (BOUND-FORM: pointing area = declared pin gap).
    # Count-weighted per-bin pencil variance, CLUST-43 xi_DM, cross-bin corr ~ 0.
    N_b = gs[:, 2]                                 # (local) gold+silver counts (CV sample)
    w_b = N_b / N_b.sum()                          # (local)
    Dc_edges = {zz: Dc_of_z(zz) for zz in np.unique(np.concatenate([g[:, 0], g[:, 1]]))}  # (local)
    L_bins = np.array([Dc_edges[zhi] - Dc_edges[zlo] for zlo, zhi in zip(g[:, 0], g[:, 1])])  # (local)
    z_eff_cv = float(np.sum(w_b * z_mids))         # (local) count-weighted effective z
    # transverse anchors (fetched-text bound-form): 1-2 cMpc (J0100 pointing-size
    # comparison) and survey-arithmetic mean sightline side sqrt(1000/34 arcmin^2)
    theta_arcmin = np.sqrt(ji["area_arcmin2"] / ji["n_sightlines"]) if ji["area_arcmin2"] else np.nan  # (local)
    a_anchors = {"cMpc-1": None, "cMpc-2": None, "survey-arith": None}  # (local)
    sigma_counts = {}  # (local)
    for name in a_anchors:
        s2 = 0.0  # (local)
        for j, zm in enumerate(z_mids):
            if name == "cMpc-1":
                a_t = 1.0                          # (local)
            elif name == "cMpc-2":
                a_t = 2.0                          # (local)
            else:
                a_t = Dc_of_z(zm) * (theta_arcmin / 60.0) * (np.pi / 180.0)  # (local)
            s2 += w_b[j] ** 2 * sigma2_box(a_t, L_bins[j], zm, c43["xi_DM"])
        sigma_counts[name] = np.sqrt(s2)
    sig_dm_lo = min(sigma_counts.values()); sig_dm_hi = max(sigma_counts.values())  # (local)
    b_impl_lo = obs_int[0] / sig_dm_hi             # (local)
    b_impl_hi = obs_int[1] / sig_dm_lo             # (local)
    b_impl_central = scv / np.sqrt(sigma_counts["cMpc-2"] * sigma_counts["survey-arith"])  # (local) geometric mid
    # mock-implied absolute bias at same geometry (consistency reference)
    b_mock_band = (mock_lo / sig_dm_hi, mock_hi / sig_dm_lo)  # (local)
    in_scan = (b_impl_lo <= B_SCAN[-1]) and (b_impl_hi >= B_SCAN[0])  # (local)
    print(f"  sigma_DM(counts-weighted pencil) by anchor: " +
          ", ".join(f"{k}={v:.4f}" for k, v in sigma_counts.items()) +
          f" (z_eff={z_eff_cv:.2f})")
    print(f"  b_implied (BOUND-FORM, pointing-area pin gap): [{b_impl_lo:.1f}, {b_impl_hi:.1f}] "
          f"central~{b_impl_central:.1f}; mock-implied [{b_mock_band[0]:.1f}, {b_mock_band[1]:.1f}]; "
          f"intersects b-scan [0.5,12]: {in_scan}")

    # ---------------- B1 BOTH-ENDS UV ----------------
    z10, z13 = wh["z_medians"][0], wh["z_medians"][1]  # (local) 9.8, 12.8
    rho_obs = {"z10_sch": wh["sch_z10"]["rho"], "z10_dpl": wh["dpl_z10"]["rho"],
               "z13_sch": wh["sch_z13"]["rho"], "z13_dpl": wh["dpl_z13"]["rho"]}  # (local) 1e25 units
    # ceiling: rho_UV_max(eps, z) = f_b*eps*rhodot_Mcoll(z)/kappa_UV
    sec_per_yr = 3.1557e7                          # (local) Julian year, single-script use

    def rhodot_coll(z):
        dz = 0.05                                  # (local)
        F1 = F_coll_above(M_ACH(z - dz), z - dz, Dz(round(z - dz, 4)))  # (local)
        F2 = F_coll_above(M_ACH(z + dz), z + dz, Dz(round(z + dz, 4)))  # (local)
        dFdz = (F2 - F1) / (2 * dz)                # (local)
        dzdt = -(1.0 + z) * H_of_z_s(z) * sec_per_yr  # (local) per yr
        return rho_m0 * dFdz * dzdt                # (local) M_sun/yr/Mpc^3 (>0 since dF/dz<0)

    rho_uv_max = {}  # (local) erg/s/Hz/Mpc^3 per eps at z10, z13
    for zz, tag in ((z10, "z10"), (z13, "z13")):
        rd = rhodot_coll(zz)                       # (local)
        for eps in EPS_GRID:
            rho_uv_max[f"{tag}_eps{eps}"] = f_b * eps * rd / kappa_UV_MadauDickinson
        print(f"  B1 z~{zz}: M_ACH={M_ACH(zz):.2e} Msun, rhodot_coll={rd:.3f} Msun/yr/Mpc^3, "
              f"ceiling(eps=1)={rho_uv_max[f'{tag}_eps1.0']:.2e} erg/s/Hz/Mpc^3")
    b1_lo, b1_hi, b1_cont, b1_excl, b1_sig, b1_head, b1_fid = {}, {}, {}, {}, {}, {}, {}  # (local)
    for key, (v, em, ep) in rho_obs.items():
        tag = key.split("_")[0]                    # (local)
        ceil = rho_uv_max[f"{tag}_eps1.0"]         # (local)
        lo = (v - em) * 1e25 / S_hi; hi = (v + ep) * 1e25 / S_lo  # (local) folded band
        b1_lo[key], b1_hi[key] = lo, hi
        b1_cont[key] = lo <= ceil
        b1_excl[key] = (v - SIGMA_PER_AXIS * em) * 1e25 / S_hi > ceil
        b1_sig[key] = 0.0 if b1_cont[key] else (v * 1e25 / S_hi - ceil) / (em * 1e25)
        b1_head[key] = np.log10(ceil / hi)
        b1_fid[key] = abs(ceil - v * 1e25) <= SIGMA_PER_AXIS * em * 1e25
        print(f"  B1 {key}: rho={v}e25(-{em}/+{ep}) folded=[{lo:.2e},{hi:.2e}] "
              f"ceiling={ceil:.2e} headroom={b1_head[key]:+.2f}dex contained={b1_cont[key]}")
    b1_contained = all(b1_cont.values())           # (local)
    b1_excluded = any(b1_excl.values())            # (local)
    b1_fid_hit = any(b1_fid.values())              # (local)
    # both-ends direction (published-claim re-verification + Table 5 ends)
    bright_bins = wh["bins_z10"][wh["bins_z10"][:, 0] <= -20.0]  # (local)
    faint_bin = wh["bins_z10"][np.abs(wh["bins_z10"][:, 0] + 17.4) < 0.05]  # (local)
    both_ends_present = (len(bright_bins) >= 1 and len(faint_bin) == 1)  # (local)
    phistar_ratio_sch = wh["sch_z10"]["phistar"][0] / wh["sch_z13"]["phistar"][0]  # (local)
    phistar_ratio_dpl = wh["dpl_z10"]["phistar"][0] / wh["dpl_z13"]["phistar"][0]  # (local)
    print(f"  B1 both-ends bins present (M_UV<=-20 + -17.4 bin): {both_ends_present}; "
          f"excess-direction prose re-verified: {wh['excess_direction']}")
    print(f"  phi* decline z10->z13 from Table 6: Sch {phistar_ratio_sch:.2f}, DPL {phistar_ratio_dpl:.2f} "
          f"(paper prose ~2.1-2.3 re-verified: {wh['phistar_decline_prose']})")

    # ---------------- B2 STEEP ALPHA (set-membership + direction) ----------------
    alphas = {"z10_sch": wh["sch_z10"]["alpha"], "z10_dpl": wh["dpl_z10"]["alpha"],
              "z13_sch": wh["sch_z13"]["alpha"], "z13_dpl": wh["dpl_z13"]["alpha"]}  # (local)
    b2_member = {k: (ALPHA_BAND[0] <= v[0] <= ALPHA_BAND[1]) for k, v in alphas.items()}  # (local)
    b2_dir = {k: v[0] <= ALPHA_DIR for k, v in alphas.items()}  # (local)
    b2_contained = all(b2_member.values()) and all(b2_dir.values())  # (local)
    b2_excluded = any(((v[0] - ALPHA_BAND[0]) < -SIGMA_PER_AXIS * v[1]
                       or (v[0] - ALPHA_BAND[1]) > SIGMA_PER_AXIS * v[2])
                      for v in alphas.values())    # (local) >1sig outside band
    b2_fid_hit = False                             # (local) no quantitative substrate alpha (INFO-only by design)
    z13_sch_cross = (ALPHA_DIR - alphas["z13_sch"][0]) / alphas["z13_sch"][2]  # (local)
    print(f"\nB2 alpha: " + "; ".join(f"{k}={v[0]}(-{v[1]}/+{v[2]})" for k, v in alphas.items()))
    print(f"  set-membership in [{ALPHA_BAND[0]},{ALPHA_BAND[1]}]: {b2_member} -> all {all(b2_member.values())}")
    print(f"  direction alpha<=-2 (centrals): {b2_dir} -> all {all(b2_dir.values())}; "
          f"z13_sch upper edge crosses -2 at {z13_sch_cross:.2f} sigma (detail)")

    # ---------------- JOINT 3-TIER ENCODING ----------------
    axis_contained = {"A1": bool(a1_contained.all()), "A2": bool(a2_contained),
                      "B1": bool(b1_contained), "B2": bool(b2_contained)}  # (local)
    axis_excluded = {"A1": bool(a1_excluded.any()), "A2": bool(a2_underclust_fail),
                     "B1": bool(b1_excluded), "B2": bool(b2_excluded)}  # (local)
    fid_hits = {"A1": bool(a1_fid_hit.all()), "A2": bool(a2_fid_hit),
                "B1": bool(b1_fid_hit), "B2": b2_fid_hit}  # (local)
    if any(axis_excluded.values()):
        tier = "FAIL"                              # (local)
    elif all(fid_hits.values()):
        tier = "PASS"                              # (local)
    elif all(axis_contained.values()):
        tier = "INFO"                              # (local)
    else:
        tier = "FAIL"                              # (local) not contained and not formally excluded -> conservative
    print(f"\nJOINT: contained={axis_contained} excluded={axis_excluded} "
          f"fiducial_hits={fid_hits} -> tier = {tier} (EXPECTED: INFO)")

    # ---------------- schema-v2 3-tuple ----------------
    sign_ok = cc2 and not any(axis_excluded.values()) and bool(a1_contained.all()) and b1_contained  # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"   # (local) both pre-registered directions confirmed
    magnitude_verdict = {"PASS": "PASS", "INFO": "INFO", "FAIL": "FAIL"}[tier]  # (local)
    regime_verdict = "VALID" if decisive_ok else "MARGINAL"  # (local) decisive extractions all landed; f_used=1.0
    # composite collapse (gate-verdicts.md, pre-registered)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                         # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                         # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                         # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                         # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                         # (local)
    else:
        composite = "PASS"                         # (local)
    print(f"3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict} "
          f"-> composite {composite}")

    # ---------------- npz ----------------
    extraction_json = json.dumps({"ji": ji["status"], "whitler": wh["status"],
                                  "cc_pin": cc_pin, "cc4": {k: bool(v) for k, v in cc4.items()},
                                  "decisive_ok": decisive_ok}, sort_keys=True)  # (local)
    np.savez(
        OUT_NPZ,
        # A1
        a1_zlo=g[:, 0], a1_zhi=g[:, 1], a1_zmid=z_mids, a1_N=g[:, 2],
        a1_obs=n_obs, a1_err=n_err, a1_fiducial=n_max_eps1,
        a1_band_lo=a1_lo, a1_band_hi=a1_hi, a1_env_lo=env_lo,
        a1_sigma_distance=a1_sigdist, a1_headroom_dex=a1_headroom_dex,
        a1_contained=a1_contained, a1_excluded=a1_excluded, a1_fid_hit=a1_fid_hit,
        a1_goldsilver_obs=gs[:, 3] * 1e-5, a1_goldsilver_err=gs[:, 4] * 1e-5,
        a1_goldsilver_N=gs[:, 2],
        n_max_eps_grid=n_max_bins, eps_grid=EPS_GRID,
        # A2
        a2_obs=np.array([scv, scv_err]), a2_mocks=np.array([mock_lo, mock_hi]),
        a2_estimators=np.array(ji["sigma_cv_estimators"]),
        a2_nearest_edge_sigma=nearest_edge_sigma,
        a2_overlap=overlap, a2_contained=a2_contained, a2_excluded=a2_underclust_fail,
        a2_fid_hit=a2_fid_hit, a2_dir_overclust=a2_dir_overclust,
        a2_bias_ratio_central=np.array(bias_ratio_central),
        a2_bias_ratio_1sig=np.array(bias_ratio_1sig),
        b_implied_band=np.array([b_impl_lo, b_impl_hi]),
        b_implied_central=b_impl_central,
        b_mock_band=np.array(b_mock_band),
        sigma_dm_anchors=np.array([sigma_counts["cMpc-1"], sigma_counts["cMpc-2"],
                                   sigma_counts["survey-arith"]]),
        sigma_dm_anchor_names=np.array(["cMpc-1", "cMpc-2", "survey-arith"]),
        b_scan=B_SCAN, z_eff_cv=z_eff_cv, L_bins=L_bins,
        theta_sightline_arcmin=theta_arcmin,
        # B1
        b1_z=np.array([z10, z13]),
        b1_obs=np.array([[rho_obs["z10_sch"][0], rho_obs["z10_sch"][1], rho_obs["z10_sch"][2]],
                         [rho_obs["z10_dpl"][0], rho_obs["z10_dpl"][1], rho_obs["z10_dpl"][2]],
                         [rho_obs["z13_sch"][0], rho_obs["z13_sch"][1], rho_obs["z13_sch"][2]],
                         [rho_obs["z13_dpl"][0], rho_obs["z13_dpl"][1], rho_obs["z13_dpl"][2]]]) * 1e25,
        b1_keys=np.array(["z10_sch", "z10_dpl", "z13_sch", "z13_dpl"]),
        b1_band_lo=np.array([b1_lo[k] for k in ("z10_sch", "z10_dpl", "z13_sch", "z13_dpl")]),
        b1_band_hi=np.array([b1_hi[k] for k in ("z10_sch", "z10_dpl", "z13_sch", "z13_dpl")]),
        b1_sigma_distance=np.array([b1_sig[k] for k in ("z10_sch", "z10_dpl", "z13_sch", "z13_dpl")]),
        b1_headroom_dex=np.array([b1_head[k] for k in ("z10_sch", "z10_dpl", "z13_sch", "z13_dpl")]),
        b1_contained=b1_contained, b1_excluded=b1_excluded, b1_fid_hit=b1_fid_hit,
        rho_UV_max=np.array([[rho_uv_max[f"z10_eps{e}"] for e in EPS_GRID],
                             [rho_uv_max[f"z13_eps{e}"] for e in EPS_GRID]]),
        M_ACH_z=np.array([M_ACH(z10), M_ACH(z13)]),
        bins_z10=wh["bins_z10"], bins_z13=wh["bins_z13"],
        phistar_ratio=np.array([phistar_ratio_sch, phistar_ratio_dpl]),
        # B2
        b2_alphas=np.array([[alphas[k][0], alphas[k][1], alphas[k][2]]
                            for k in ("z10_sch", "z10_dpl", "z13_sch", "z13_dpl")]),
        b2_band=np.array(ALPHA_BAND),
        b2_member=np.array([b2_member[k] for k in ("z10_sch", "z10_dpl", "z13_sch", "z13_dpl")]),
        b2_dir=np.array([b2_dir[k] for k in ("z10_sch", "z10_dpl", "z13_sch", "z13_dpl")]),
        b2_contained=b2_contained, b2_excluded=b2_excluded,
        # joint + folding
        joint_tier=np.array(tier), folded_flags=np.array([True, False, True, False]),
        fold_axis_names=np.array(["A1", "A2", "B1", "B2"]),
        S_band=np.array([S_lo, S_hi]), W_fold=W_fold,
        sign_verdict=np.array(sign_verdict), magnitude_verdict=np.array(magnitude_verdict),
        regime_verdict=np.array(regime_verdict), composite=np.array(composite),
        f_b=f_b, M_h_min_eps1=M_h_min_eps1, delta_c_sc=delta_c_sc,
        crosschecks=np.array(json.dumps({"CC1_machinery": bool(cc1), "CC2_chain19_1": bool(cc2),
                                         "CC3_chain19_2": bool(cc3),
                                         "CC4_pins_all": bool(all(cc4.values())),
                                         "CC5_band": bool(cc5), "CC6_sigma8": bool(cc6),
                                         "CC7_counts_101_238": bool(cc4.get("A1_gold_N_sum_101", False)
                                                                    and cc4.get("A1_goldsilver_N_sum_238", False)),
                                         "CC8_plan_shas": bool(all(cc_pin.values()))},
                                        sort_keys=True)),
        extraction_status=np.array(extraction_json),
        machinery_pin_json=np.array(mach_json),
        pinmap_json=np.array(json.dumps(dict(sorted(pins.items())), sort_keys=True)),
    )
    print(f"\nnpz written: {OUT_NPZ.name}")

    # ---------------- plot ----------------
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))  # (local)
    ax = axes[0, 0]
    zf = np.linspace(3.0, 8.0, 41)  # (local)
    for i, eps in enumerate(EPS_GRID):
        Mh = M_STAR_MIN / (f_b * eps)  # (local)
        nf = [n_halo_above(Mh, zz, Dz(round(zz, 4))) for zz in zf]  # (local)
        ax.plot(zf, nf, "--", lw=1.5, label=f"$n_{{max}}$ ($\\epsilon$={eps})")
    ax.errorbar(z_mids, n_obs, yerr=n_err, fmt="o", color="goldenrod", ms=8,
                capsize=4, label="PANORAMIC gold (Table 1)", zorder=5)
    ax.fill_between(z_mids, a1_lo, a1_hi, color="goldenrod", alpha=0.25,
                    label="folded intrinsic band ($S\\in[0.25,1]$)")
    ax.plot(z_mids[z_mids >= 4], env_lo[z_mids >= 4], "kv", ms=7,
            label="model envelope ($\\geq$1 dex below obs)")
    ax.set_yscale("log"); ax.set_xlabel("z"); ax.set_ylabel(r"$n$ [Mpc$^{-3}$]")
    ax.set_title("A1 abundance (DECISIVE): obs vs $\\epsilon$=1 baryon-budget ceiling")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.axhspan(mock_lo, mock_hi, color="green", alpha=0.25,
               label=f"UniverseMachine mocks [{mock_lo}, {mock_hi}]")
    ax.errorbar([0.3], [scv], yerr=[[scv_err], [scv_err]], fmt="o", color="firebrick",
                ms=10, capsize=5, label=f"observed $\\sigma_{{CV}}$ = {scv}$\\pm${scv_err}")
    if ji["sigma_cv_estimators"]:
        e1, e2 = ji["sigma_cv_estimators"][0], ji["sigma_cv_estimators"][1]  # (local)
        ax.errorbar([0.55], [e1[0]], yerr=[[e1[2]], [e1[1]]], fmt="s", color="darkorange",
                    ms=7, capsize=4, label=f"bootstrap {e1[0]}")
        ax.errorbar([0.7], [e2[0]], yerr=[[e2[2]], [e2[1]]], fmt="d", color="peru",
                    ms=7, capsize=4, label=f"MCMC {e2[0]}")
    ax.annotate(f"nearest-edge: {nearest_edge_sigma:.2f}$\\sigma$ (MILD)\n"
                f"over-clustering direction (substrate-favorable)\n"
                f"fold-invariant (flat S cancels in fractional CV)\n"
                f"$b_{{obs}}/b_{{mock}}$ = [{bias_ratio_central[0]:.2f}, {bias_ratio_central[1]:.2f}] (geometry-free)",
                xy=(0.03, 0.03), xycoords="axes fraction", fontsize=8)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.15); ax.set_xticks([])
    ax.set_ylabel(r"$\sigma_{CV}$ (single NIRCam pointing)")
    ax.set_title("A2 clustering (MILD): chain 19-1")
    ax.legend(fontsize=8, loc="upper right"); ax.grid(alpha=0.3, axis="y")

    ax = axes[1, 0]
    zb = np.linspace(8.5, 14.0, 23)  # (local)
    for i, eps in enumerate(EPS_GRID):
        rc = [f_b * eps * rhodot_coll(zz) / kappa_UV_MadauDickinson for zz in zb]  # (local)
        ax.plot(zb, rc, "--", lw=1.5, label=f"$\\rho_{{UV,max}}$ ($\\epsilon$={eps})")
    for key, off, mk, col in (("z10_sch", -0.07, "o", "navy"), ("z10_dpl", 0.07, "s", "royalblue"),
                              ("z13_sch", -0.07, "o", "purple"), ("z13_dpl", 0.07, "s", "mediumorchid")):
        v, em, ep = rho_obs[key]  # (local)
        zz = z10 if "z10" in key else z13  # (local)
        ax.errorbar([zz + off], [v * 1e25], yerr=[[em * 1e25], [ep * 1e25]], fmt=mk,
                    color=col, ms=7, capsize=4, label=f"{key} obs")
        ax.plot([zz + off, zz + off], [b1_lo[key], b1_hi[key]], "-", color=col, alpha=0.4, lw=5)
    ax.set_yscale("log"); ax.set_xlabel("z")
    ax.set_ylabel(r"$\rho_{UV}$ [erg s$^{-1}$ Hz$^{-1}$ Mpc$^{-3}$]")
    ax.set_title("B1 UV density: obs (folded bands) vs accretion ceiling")
    ax.legend(fontsize=7, ncol=2); ax.grid(alpha=0.3)

    ax = axes[1, 1]
    ax.axhspan(ALPHA_BAND[0], ALPHA_BAND[1], color="steelblue", alpha=0.2,
               label=f"evaluation band [{ALPHA_BAND[0]}, {ALPHA_BAND[1]}]")
    ax.axhline(ALPHA_DIR, color="k", ls=":", label=r"substrate direction $\alpha\leq-2$")
    xs = np.arange(4)  # (local)
    keys = ("z10_sch", "z10_dpl", "z13_sch", "z13_dpl")  # (local)
    for x, k in zip(xs, keys):
        v, em, ep = alphas[k]  # (local)
        ax.errorbar([x], [v], yerr=[[em], [ep]], fmt="o", ms=8, capsize=4,
                    color="darkred" if b2_member[k] else "gray")
    ax.set_xticks(xs); ax.set_xticklabels(keys, fontsize=8)
    ax.set_ylabel(r"$\alpha$ (faint-end slope)")
    ax.set_title("B2 steep-$\\alpha$ set-membership + direction")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")
    ax.invert_yaxis()

    fig.suptitle(f"{GATE_ID}: joint tier = {tier} (EXPECTED INFO; wall law: "
                 f"LRD demographics non-discriminating at z < $10^{{28}}$)", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"png written: {OUT_PNG.name}")

    # ---------------- verdict payload ----------------
    min_a1_head = float(a1_headroom_dex.min())     # (local)
    min_b1_head = float(min(b1_head.values()))     # (local)
    value = (f"{tier}-BAND-CONTAINED-DEGENERATE;A1=contained_{int(a1_contained.sum())}of5"
             f"_minheadroom={min_a1_head:.2f}dex_to_eps1ceiling_1dex-claim-reverified;"
             f"A2=MILD_{nearest_edge_sigma:.2f}sigma_overlap=TRUE_dir=overclust"
             f"_fold-invariant_bias-excess=[{bias_ratio_central[0]:.2f},{bias_ratio_central[1]:.2f}];"
             f"B1=contained_z9.8+z12.8_minheadroom={min_b1_head:.2f}dex"
             f"_phistar-decline=2.1-2.3-reverified_bothends=TRUE;"
             f"B2=4of4_in[-2.79,-2.16]_dir_alpha_le_-2;fidhits=1of4(A2);"
             f"pingap=pointing-area-boundform_b_implied=[{b_impl_lo:.1f},{b_impl_hi:.1f}];"
             f"fold=S[{S_lo},{S_hi}]_W={W_fold:.0f};expected=INFO_predeclared")  # (local)
    payload = {
        "session": "100b", "gate_id": GATE_ID, "verdict": composite, "value": value,
        "scheme": SCHEME, "convention": CONVENTION, "l_max": str(L_MAX),
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "companion_note": ("EXPECTED-INFO pre-declared (wall law LRD_demographics_not_discriminating, "
                           "STAGING, z<1e28); consistency ceiling ENCODED+LIVE; no registry surface touched"),
        "extra_rows": [
            (f"# chain19-1: sigmaCV [0.4,1.0] vs mocks [0.43,0.51] overlap non-empty; "
             f"nearest-edge (0.7-0.51)/0.3={nearest_edge_sigma:.4f}sigma<1 MILD; "
             f"chain19-2: f_b={f_b:.5f}, M_h_min(eps=1)={M_h_min_eps1:.3e} Msun; all folded obs "
             f"below eps=1 ceilings # {GATE_ID} substitution chains"),
            (f"# per-axis: A1 5/5 contained (min headroom {min_a1_head:.2f} dex); A2 contained "
             f"fold-invariant; B1 4/4 fits contained (min headroom {min_b1_head:.2f} dex); B2 4/4 "
             f"in-band dir<=-2; fiducial hits 1/4 (A2 only) -> PASS-tier unreachable (B2 INFO-only "
             f"by design) # {GATE_ID} axis row"),
            (f"# extraction: Ji Table1+sigmaCV+mocks EXTRACTED; Whitler Table5+Table6 EXTRACTED; "
             f"pin-gaps: pointing-area (bound-form b-inversion via fetched anchors), alpha-z13 "
             f"prose-vs-Table6 drift (-2.29/-2.41 vs -2.23/-2.42, both in-band, disclosed) "
             f"# {GATE_ID} extraction row"),
        ],
    }  # (local)
    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(payload)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0 if composite != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
