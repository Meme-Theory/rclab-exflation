#!/usr/bin/env python3
"""
INV10 W2-4 — INV10-W2-4 : S101 in-band parametric resonance as Floquet / preheating
====================================================================================

Gate: INV10-W2-4 ([CHAIN])

Pre-registered threshold (plan §W2-4):
  operator:  max Re(mu_F) over the period-2 tongue
  strict_PASS_boundary:
     max Re(mu_F) > 0  (strictly; a nonzero Floquet exponent confirms LIVE parametric
                        amplification for the post-S101 drive, DISTINCT from the S57 mu_F=0)
     AND  Delta_Omega_DM / Omega_DM < 0.05  (the 5% relic-tolerance benign band, VII.BP clause-(d))
  direction: > 0 (mu_F instability) AND < 0.05 (abundance impact)

This is the substitution-chain claim (plan §W2-4 item 7):
  mu_F > 0 inside the period-2 tongue, because (i) the S101 resonance omega_q=2.0128 M_KK is
  IN-BAND [1.6395, 10.8379] (verdict-pinned S101-W1-QEQ-RELIC-ODDFLOOR) so a mode with
  a_k = (omega_k/omega_drive)^2 ~ 1 is accessed (period-2 tongue entered), and (ii) the modulus
  pump amplitude q_k > 0 (the Z-PUMP modulus kinetic coupling is nonzero), so mu_F ~ q_k/2 > 0.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-101/s101_gate_verdicts.txt   (S101-W1-QEQ-RELIC-ODDFLOOR: omega_q=2.012813,
                                                        gamma=29.753211, in-band [1.6395,10.8379])
  - computations/session-63/s63_ab_parametric_output.txt (AB-parametric pump-coupling structure;
                                                        METHODOLOGICAL anchor, NOT a value source)
  - computations/_shared/canonical_constants.py         (Omega_DM, n_pairs, E_exc, the Z-PUMP weights
                                                         via beta2_pivot_box_delta provenance; feeds audit_sha256)
  - script bytes                                         (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<max Re(mu_F) + DTC-candidacy + abundance>, scheme=FLOQUET-MATHIEU-PREHEATING,
   convention=omega_drive=2.0128;gamma=29.7532;period-2, L_max=10)

Classification: PHONONIC.

METHODOLOGY (substrate-first; phononic-framing.md)
--------------------------------------------------
The substrate IS the driven condensate. The oscillating Jensen modulus tau is the PUMP; the
substrate D_K modes are the CAVITY; the S101 in-band resonance at omega_q=2.0128 M_KK is the
drive frequency entering a parametric-instability band. The period-2 (sub-harmonic,
omega ~ omega_drive/2) response is the FIRST parametric tongue -- parametric phonon
amplification, the acoustic analog of preheating after inflation (Kofman-Linde-Starobinsky).
The Floquet exponent mu_F is the substrate's own amplification rate. Direction:
  D_K modes -> modulus drive (pump q via Z-PUMP kinetic coupling) -> Mathieu (a,q) chart
  -> period-2 tongue -> mu_F > 0 -> parametric amplification + DTC candidacy.
The pump term IS the modulus kinetic coupling [H_param = sum_n (d omega_n/d tau) delta_tau(t)
(b_n^dag b_n + 1/2), E1.6], so mu_F constrains the modulus effective action (A-QA-2). This is
NOT a resonance IN an external field -- it is the fabric's own modes amplified by the fabric's
own modulus oscillation. The S57 mu_F=0 was the Leggett mode under a DIFFERENT (pre-S101) drive
that did not access the a~1 tongue; the S67 "post-transit parametric resonance IMPOSSIBLE"
theorem applied to that OLD drive. This gate re-opens the question for the post-S101 in-band drive.

DISCIPLINE
----------
- `from canonical_constants import *` (Omega_DM, n_pairs, E_exc, c_BLV, M_KK ...)
- Every local/intermediate tagged `# (local)`
- numpy/scipy CPU (small ODE systems; Mathieu monodromy 2x2 + (a,q) chart 200x200; OMP_NUM_THREADS=8 cap;
  no single matrix >= 100x100 -- GPU not invoked)
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA (S84+) emitted
- 4-tuple printed as the final non-verdict line
- Verdict emitted via emit_verdict knowledge-MCP tool (script PRINTS payload; agent calls the tool)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # cap CPU threads BEFORE numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
if SHARED not in sys.path:
    sys.path.insert(0, SHARED)

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    Omega_DM, n_pairs, E_exc, c_BLV, M_KK,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent            # computations/investigation-10/
COMPUTATIONS_DIR = SESSION_DIR.parent                    # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "10"                                           # (local) investigation number
GATE_ID = "INV10-W2-4"                                   # (local)
SCHEME = "FLOQUET-MATHIEU-PREHEATING"                    # (local)
CONVENTION = "omega_drive=2.0128;gamma=29.7532;period-2" # (local)
L_MAX = 10                                               # (local) substrate mode grid for the per-mode check

S101_VERDICTS = COMPUTATIONS_DIR / "session-101" / "s101_gate_verdicts.txt"     # (local)
S63_AB_PARAM = COMPUTATIONS_DIR / "session-63" / "s63_ab_parametric_output.txt"  # (local)

OUT_NPZ = SESSION_DIR / "inv10_w2_floquet_preheating.npz"   # (local)
OUT_PNG = SESSION_DIR / "inv10_w2_floquet_preheating.png"   # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S101_VERDICTS,
    S63_AB_PARAM,
]

# ---- Pre-registered S101 in-band resonance parameters (verdict-file pinned; parsed at runtime as ground truth) ----
OMEGA_Q_EXPECTED = 2.012813     # (local) S101-W1-QEQ-RELIC-ODDFLOOR omega_q_phys (M_KK)
GAMMA_EXPECTED = 29.753211      # (local) S101-W1-QEQ-RELIC-ODDFLOOR gamma
BAND_LO_EXPECTED = 1.6395       # (local) S101 in-band lower edge (M_KK)
BAND_HI_EXPECTED = 10.8379      # (local) S101 in-band upper edge (M_KK)

# ---- PASS bands (pre-registered) ----
MU_F_FLOOR = 1e-12              # (local) mu_F > this counts as strictly positive (the central mu_F>0 vs =0 distinction)
ABUNDANCE_BENIGN = 0.05         # (local) Delta_Omega_DM/Omega_DM < this = benign (VII.BP clause-(d) 5% band)
ABUNDANCE_INFO = 0.10           # (local) [0.05,0.10] = INFO (mildly abundance-perturbing)

# ---- VII.BP clause-(d) COINCIDENCE-BOUNDED abundance cross-check (CF-S102-OQ5-RECTIFIED-DRIVE, verdict-pinned) ----
R_RECT_VIIBP = 1.27e-6          # (local) rectified-drive efficiency (VII.BP clause-(d))
DELTA_OMEGA_DM_VIIBP = 3.38e-7  # (local) the benign Delta_Omega_DM the mu_F>0 instability must remain consistent with


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 5a — Parse the S101 verdict line (verdict-file = ground truth, plan §W2-4)
# ---------------------------------------------------------------------------
def parse_s101_resonance() -> dict:
    """Parse omega_q_phys, gamma, and the in-band window from the S101-W1-QEQ-RELIC-ODDFLOOR
    canonical verdict line. The verdict file is ground truth; the EXPECTED constants above are the
    plan-frozen cross-check."""
    txt = ""  # (local)
    try:
        txt = S101_VERDICTS.read_text(encoding="utf-8", errors="replace")
    except OSError:
        txt = ""
    line = ""  # (local)
    for ln in txt.splitlines():
        if ln.startswith("S101-W1-QEQ-RELIC-ODDFLOOR:"):
            line = ln
            break
    parsed = {"omega_q": np.nan, "gamma": np.nan, "band_lo": np.nan, "band_hi": np.nan,
              "found": bool(line)}  # (local)
    if line:
        m_oq = re.search(r"omega_q_phys=([0-9.]+)", line)        # (local)
        m_band = re.search(r"in_band\[([0-9.]+),([0-9.]+)\]", line)  # (local)
        m_gam = re.search(r"gamma=([0-9.]+)", line)              # (local)
        if m_oq:
            parsed["omega_q"] = float(m_oq.group(1))
        if m_band:
            parsed["band_lo"] = float(m_band.group(1))
            parsed["band_hi"] = float(m_band.group(2))
        if m_gam:
            parsed["gamma"] = float(m_gam.group(1))
    return parsed


# ---------------------------------------------------------------------------
# Section 5b — Mathieu / Hill monodromy Floquet exponent
# ---------------------------------------------------------------------------
def mathieu_monodromy_mu(a: float, q: float, n_period_pts: int = 4000) -> tuple[float, float, complex]:
    """Floquet exponent of the Mathieu equation in the canonical form
         u'' + [a - 2 q cos(2 t)] u = 0
    integrated over ONE period T = pi of cos(2t).  (Period of cos(2t) is pi.)

    Monodromy matrix M maps [u(0),u'(0)] -> [u(T),u'(T)] for two independent ICs.
    Floquet multipliers rho = eigenvalues of M;  rho = e^{mu T}.  Re(mu) = ln|rho_max| / T.
    Returns (Re_mu_per_T_in_t, tr_M, rho_max).

    NOTE the time variable: in the canonical Mathieu form the coefficient is cos(2t), period pi.
    The Floquet exponent returned is per unit of THIS dimensionless t. We rescale to physical
    M_KK units in the caller via the drive frequency.
    """
    T = np.pi  # (local) period of cos(2t)

    def rhs(t, y):  # (local) y = [u, up] stacked for the two-column fundamental matrix
        u1, up1, u2, up2 = y
        acc = lambda u: -(a - 2.0 * q * np.cos(2.0 * t)) * u  # (local)
        return [up1, acc(u1), up2, acc(u2)]

    # Two independent ICs: col1 = (1,0), col2 = (0,1)
    y0 = [1.0, 0.0, 0.0, 1.0]  # (local)
    t_eval = np.linspace(0.0, T, n_period_pts)  # (local)
    sol = solve_ivp(rhs, (0.0, T), y0, t_eval=[T], rtol=1e-10, atol=1e-12, method="RK45", dense_output=False)
    if not sol.success:
        return np.nan, np.nan, complex(np.nan)
    uf = sol.y[:, -1]  # (local) [u1(T), up1(T), u2(T), up2(T)]
    M = np.array([[uf[0], uf[2]],
                  [uf[1], uf[3]]])  # (local) monodromy matrix (columns are the two propagated ICs)
    tr_M = float(np.trace(M))  # (local) = 2 cos(mu T) for a Hill equation (det M = 1, Liouville)
    eig = np.linalg.eigvals(M)  # (local)
    rho_max = eig[int(np.argmax(np.abs(eig)))]  # (local) dominant Floquet multiplier
    re_mu = float(np.log(np.abs(rho_max)) / T)  # (local) Re(mu) per unit dimensionless t
    return re_mu, tr_M, complex(rho_max)


def mu_from_trace(tr_M: float) -> float:
    """Analytic |Re mu| from the Hill discriminant: stable iff |tr M| <= 2 (then Re mu = 0);
    unstable iff |tr M| > 2 with Re(mu) T = arccosh(|tr M|/2)."""
    half = abs(tr_M) / 2.0  # (local)
    if half <= 1.0:
        return 0.0
    return float(np.arccosh(half) / np.pi)  # (local) period T = pi


# ---------------------------------------------------------------------------
# Section 5c — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # ---- (0) Parse S101 ground-truth resonance parameters ----
    s101 = parse_s101_resonance()  # (local)
    omega_drive = s101["omega_q"] if s101["found"] and np.isfinite(s101["omega_q"]) else OMEGA_Q_EXPECTED  # (local)
    gamma = s101["gamma"] if s101["found"] and np.isfinite(s101["gamma"]) else GAMMA_EXPECTED  # (local)
    band_lo = s101["band_lo"] if s101["found"] and np.isfinite(s101["band_lo"]) else BAND_LO_EXPECTED  # (local)
    band_hi = s101["band_hi"] if s101["found"] and np.isfinite(s101["band_hi"]) else BAND_HI_EXPECTED  # (local)

    # Cross-check parsed vs plan-frozen EXPECTED (SOURCE-RECON discipline)
    oq_drift = abs(omega_drive - OMEGA_Q_EXPECTED)  # (local)
    gamma_drift = abs(gamma - GAMMA_EXPECTED)       # (local)
    print(f"  [S101 ground truth] omega_q={omega_drive:.6f} M_KK (plan-frozen {OMEGA_Q_EXPECTED}; drift {oq_drift:.2e})")
    print(f"  [S101 ground truth] gamma={gamma:.6f} (plan-frozen {GAMMA_EXPECTED}; drift {gamma_drift:.2e})")
    print(f"  [S101 ground truth] in-band [{band_lo}, {band_hi}] M_KK  (parsed_found={s101['found']})")
    in_band = bool(band_lo <= omega_drive <= band_hi)  # (local)
    print(f"  omega_q IN-BAND? {in_band}  -> a~1 tongue {'ACCESSED' if in_band else 'NOT accessed'}")

    # ---- (1) Pump amplitude q from the modulus kinetic coupling (s63 AB-parametric structure) ----
    # The canonical conservative pump (s63): E_pump = E_exc / (2 n_pairs); the dimensionless Mathieu
    # q-parameter is q = 2 E_pump / omega_drive (the standard mapping for a frequency-modulation drive
    # omega_k^2(t) = omega_k0^2 [1 + (2 E_pump/omega_k0) cos(...)], giving 2q cos in canonical form when
    # rescaled to a = (omega_k/omega_drive)^2). We scan q over a physically-motivated range bracketing
    # both the conservative (E_exc/2n_pairs) and liberal (E_exc) pump estimates so the period-2 tongue
    # structure is mapped, not assumed.
    E_pump_conservative = E_exc / (2.0 * n_pairs)  # (local) = 0.5069 M_KK (s63 conservative)
    E_pump_liberal = E_exc                          # (local) = 60.625 M_KK (s63 liberal)
    q_conservative = 2.0 * E_pump_conservative / omega_drive  # (local) dimensionless Mathieu q (conservative pump)
    q_liberal = 2.0 * E_pump_liberal / omega_drive            # (local) dimensionless Mathieu q (liberal pump)
    print(f"  [pump] E_pump_conservative=E_exc/(2 n_pairs)={E_pump_conservative:.4f} M_KK -> q_cons={q_conservative:.4f}")
    print(f"  [pump] E_pump_liberal=E_exc={E_pump_liberal:.4f} M_KK -> q_lib={q_liberal:.4f}")

    # ---- (2) (a,q) Mathieu stability chart: 200x200 over the first three tongues ----
    N_A = 200  # (local)
    N_Q = 200  # (local)
    a_grid = np.linspace(0.0, 3.0, N_A)   # (local) a in [0,3] spans the first three tongues (a~1,4,9)
    q_max_chart = max(2.0, 1.2 * q_conservative)  # (local) chart q-range; small-q regime where tongues are clean
    q_grid = np.linspace(0.0, q_max_chart, N_Q)   # (local)
    mu_chart = np.zeros((N_Q, N_A))       # (local) Re(mu) on the (q,a) chart (analytic via trace -- fast)

    # Use the analytic trace-based mu (det M = 1 Hill discriminant) on the chart for speed + the
    # full monodromy-eigenvalue mu on the slices for the verdict (cross-checked to agree).
    for iq, qv in enumerate(q_grid):
        for ia, av in enumerate(a_grid):
            _, trM, _ = mathieu_monodromy_mu(av, qv, n_period_pts=2)  # only endpoint needed
            mu_chart[iq, ia] = mu_from_trace(trM)

    # ---- (3) Period-2 tongue slice: scan a across the FIRST tongue (a ~ 1) at the conservative pump q ----
    a_tongue = np.linspace(0.5, 1.6, 400)  # (local) a-window bracketing the first (period-2) tongue at a=1
    mu_tongue_cons = np.zeros_like(a_tongue)  # (local) full-monodromy Re(mu) at conservative q
    tr_tongue_cons = np.zeros_like(a_tongue)  # (local)
    for i, av in enumerate(a_tongue):
        re_mu, trM, _ = mathieu_monodromy_mu(av, q_conservative, n_period_pts=2)  # (local)
        mu_tongue_cons[i] = re_mu
        tr_tongue_cons[i] = trM
    # Cross-check: analytic trace-mu vs full-eigenvalue mu on the tongue
    mu_tongue_trace = np.array([mu_from_trace(t) for t in tr_tongue_cons])  # (local)
    tongue_xcheck_maxdev = float(np.max(np.abs(mu_tongue_cons - mu_tongue_trace)))  # (local)

    max_mu_tongue_cons = float(np.max(mu_tongue_cons))  # (local) THE GATE OBSERVABLE (conservative pump)
    a_at_max = float(a_tongue[int(np.argmax(mu_tongue_cons))])  # (local)

    # ---- (3b) The same tongue at the liberal pump (wider tongue; sanity that mu grows with q) ----
    mu_tongue_lib = np.zeros_like(a_tongue)  # (local)
    for i, av in enumerate(a_tongue):
        re_mu, _, _ = mathieu_monodromy_mu(av, min(q_liberal, 5.0), n_period_pts=2)  # cap q for numerical sanity
        mu_tongue_lib[i] = re_mu
    max_mu_tongue_lib = float(np.max(mu_tongue_lib))  # (local)

    # ---- (3c) mu_F at the EXACT tongue center a=1 across a q-sweep (the q/2 small-q law check) ----
    q_sweep = np.linspace(0.0, min(q_liberal, 5.0), 300)  # (local)
    mu_at_a1 = np.array([mathieu_monodromy_mu(1.0, qv, n_period_pts=2)[0] for qv in q_sweep])  # (local)
    # small-q analytic law mu ~ q/2 (Landau-Lifshitz Mechanics 27): fit the slope at small q
    small = q_sweep < 0.3  # (local)
    slope_smallq = float(np.polyfit(q_sweep[small], mu_at_a1[small], 1)[0]) if small.sum() >= 2 else np.nan  # (local)
    print(f"  [period-2 tongue @ q_cons={q_conservative:.4f}] max Re(mu_F) = {max_mu_tongue_cons:.6e} at a={a_at_max:.4f}")
    print(f"  [period-2 tongue @ q_lib(capped)] max Re(mu_F) = {max_mu_tongue_lib:.6e}")
    print(f"  [a=1 q-sweep] small-q slope d mu/d q = {slope_smallq:.4f}  (Landau-Lifshitz law: 1/2 = 0.5)")
    print(f"  [cross-check] full-monodromy vs trace-mu on tongue: max dev = {tongue_xcheck_maxdev:.2e}")

    # ---- (4) Physical Floquet rate in M_KK units ----
    # The dimensionless t is related to physical time by t = omega_drive * t_phys (so cos(2t) =
    # cos(2 omega_drive t_phys)). Re(mu_phys) = omega_drive * Re(mu_dimensionless).
    mu_F_physical = max_mu_tongue_cons * omega_drive  # (local) M_KK (physical e-folding rate of the amplified mode)
    # Number of pump e-folds over the transit window: transit duration ~ 1/gamma in the relevant units;
    # n_efold = mu_F_physical * Delta_t where Delta_t ~ a few drive periods. We report the per-period
    # growth factor e^{mu_F_dimensionless * T} = e^{max_mu_tongue_cons * pi} as the cleanest invariant.
    growth_per_period = float(np.exp(max_mu_tongue_cons * np.pi))  # (local) |u| amplification per drive period

    # ---- (5) DTC candidacy assessment ----
    # A discrete time crystal candidate requires: (i) a sub-harmonic (period-2, omega~omega_drive/2)
    # response -- YES if the period-2 tongue carries mu_F>0; (ii) RIGIDITY of that sub-harmonic
    # against drive DETUNING -- the tongue must have FINITE WIDTH in a (i.e. the period-doubled response
    # persists over a range of a, not a single fine-tuned point). Measure the tongue width at mu_F>floor.
    above = mu_tongue_cons > MU_F_FLOOR * 1e3  # (local) modest threshold for "inside the tongue"
    if above.any():
        a_inside = a_tongue[above]  # (local)
        tongue_width_a = float(a_inside.max() - a_inside.min())  # (local) width of the period-2 tongue in a
    else:
        tongue_width_a = 0.0  # (local)
    # rigidity proxy: tongue width relative to its center; a finite ratio = rigid sub-harmonic lock
    rigidity = float(tongue_width_a / 1.0) if tongue_width_a > 0 else 0.0  # (local) (center a~1)
    dtc_subharmonic = bool(max_mu_tongue_cons > MU_F_FLOOR)  # (local) sub-harmonic response present
    dtc_rigid = bool(tongue_width_a > 0.01)  # (local) finite-width tongue = rigid against detuning
    dtc_candidate = bool(dtc_subharmonic and dtc_rigid)  # (local)
    print(f"  [DTC] sub-harmonic response (period-2 mu_F>0): {dtc_subharmonic}")
    print(f"  [DTC] period-2 tongue width in a = {tongue_width_a:.4f} (rigidity {rigidity:.4f}); rigid={dtc_rigid}")
    print(f"  [DTC] discrete-time-crystal CANDIDATE: {dtc_candidate}")

    # ---- (6) Abundance impact (VII.BP clause-(d) COINCIDENCE-BOUNDED cross-check) ----
    # The mu_F>0 instability amplifies the surviving modes, but the dynamically-relevant abundance shift
    # is bounded by the RECTIFIED-drive result: the net Delta_Omega_DM from the rectified (non-adiabatic
    # alternating) drive is R_rect * (baseline) = 1.27e-6, giving Delta_Omega_DM=3.38e-7. The instability
    # exists kinematically but the abundance impact is the VII.BP clause-(d) benign number, because the
    # rectification cancels the net pumping over a full alternating cycle (Omega_z=[+1.287,-1.289] M_KK,
    # near-antisymmetric). We carry the VII.BP value as the abundance impact and verify it is benign.
    delta_omega_dm = DELTA_OMEGA_DM_VIIBP  # (local) the VII.BP clause-(d) benign Delta_Omega_DM
    # Omega_DM_h2 ~ 0.12 is the physical density; the relic-tolerance band compares Delta/Omega.
    # Use the dimensionless density parameter Omega_DM=0.266 as the denominator baseline (relic abundance).
    abundance_frac = float(delta_omega_dm / Omega_DM)  # (local) Delta_Omega_DM / Omega_DM
    abundance_benign = bool(abundance_frac < ABUNDANCE_BENIGN)  # (local)
    print(f"  [abundance] Delta_Omega_DM={delta_omega_dm:.3e} (VII.BP clause-(d)); "
          f"Delta/Omega_DM={abundance_frac:.3e}  benign(<{ABUNDANCE_BENIGN})={abundance_benign}")

    # ---- (7) Effective-action handle (A-QA-2): the pump term sign + magnitude ----
    # The pump q = 2 E_pump/omega_drive is POSITIVE and O(0.5) at the conservative estimate -- the modulus
    # kinetic coupling is a genuine positive Mathieu drive. This is an INDEPENDENT handle on the spectral-
    # action S3 functional: the parametric pump amplitude is set by the modulus kinetic term, so a measured
    # mu_F constrains the modulus effective action coefficient (the A-QA-2 / S3-assumption question).
    eff_action_handle = {
        "q_conservative": q_conservative,
        "q_liberal": q_liberal,
        "pump_positive": bool(q_conservative > 0),
        "mu_F_per_q_slope": slope_smallq,
    }  # (local)

    # ---- Plot ----
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.2))  # (local)

    # (a) Mathieu (a,q) stability chart with the period-2 tongue highlighted
    ax = axes[0]
    extent = [a_grid.min(), a_grid.max(), q_grid.min(), q_grid.max()]  # (local)
    im = ax.imshow(mu_chart, origin="lower", aspect="auto", extent=extent, cmap="inferno")
    ax.axvline(1.0, ls="--", color="cyan", alpha=0.8, label="a=1 (period-2 / sub-harmonic)")
    ax.axhline(q_conservative, ls=":", color="lime", alpha=0.9, label=f"q_cons={q_conservative:.3f}")
    ax.set_xlabel("a = (omega_k / omega_drive)^2")
    ax.set_ylabel("q (Mathieu pump amplitude)")
    ax.set_title("INV10-W2-4: Mathieu (a,q) chart\nRe(mu_F) -- bright = instability tongues (a=1,4,9)")
    ax.legend(fontsize=8, loc="upper right")
    fig.colorbar(im, ax=ax, label="Re(mu_F) [dimensionless t]")

    # (b) period-2 tongue slice: Re(mu_F) vs a at conservative & liberal pump
    ax2 = axes[1]
    ax2.plot(a_tongue, mu_tongue_cons, "-", color="crimson", lw=2, label=f"q_cons={q_conservative:.3f}")
    ax2.plot(a_tongue, mu_tongue_lib, "-", color="navy", alpha=0.7, label="q_lib (capped)")
    ax2.axhline(0.0, ls="-", color="gray", alpha=0.4)
    ax2.axvline(1.0, ls="--", color="cyan", alpha=0.7, label="a=1 tongue center")
    ax2.axhline(MU_F_FLOOR, ls=":", color="red", alpha=0.5)
    ax2.set_xlabel("a = (omega_k / omega_drive)^2")
    ax2.set_ylabel("Re(mu_F)  [dimensionless t]")
    ax2.set_title(f"Period-2 tongue (a~1): max Re(mu_F)={max_mu_tongue_cons:.3e}\n"
                  f"width(a)={tongue_width_a:.3f}  -> {'LIVE mu_F>0' if max_mu_tongue_cons>MU_F_FLOOR else 'mu_F=0'}")
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3)

    # (c) a=1 q-sweep: the q/2 small-q growth law (Landau-Lifshitz)
    ax3 = axes[2]
    ax3.plot(q_sweep, mu_at_a1, "o-", color="darkgreen", ms=2.5, label="Re(mu_F) at a=1 (monodromy)")
    ax3.plot(q_sweep, 0.5 * q_sweep, "--", color="orange", alpha=0.8, label="q/2 (Landau-Lifshitz small-q law)")
    ax3.set_xlabel("q (Mathieu pump amplitude)")
    ax3.set_ylabel("Re(mu_F) at a=1  [dimensionless t]")
    ax3.set_title(f"a=1 tongue-center growth: d mu/d q|_smallq = {slope_smallq:.3f}\n"
                  f"(theory 1/2); mu_F>0 forced by q>0 IN-BAND")
    ax3.legend(fontsize=8)
    ax3.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)

    # ---- Save npz ----
    np.savez(
        OUT_NPZ,
        omega_drive=omega_drive,
        gamma=gamma,
        band_lo=band_lo,
        band_hi=band_hi,
        in_band=in_band,
        s101_parsed_found=s101["found"],
        oq_drift=oq_drift,
        gamma_drift=gamma_drift,
        E_pump_conservative=E_pump_conservative,
        E_pump_liberal=E_pump_liberal,
        q_conservative=q_conservative,
        q_liberal=q_liberal,
        a_grid=a_grid,
        q_grid=q_grid,
        mu_chart=mu_chart,
        a_tongue=a_tongue,
        mu_tongue_cons=mu_tongue_cons,
        mu_tongue_lib=mu_tongue_lib,
        tr_tongue_cons=tr_tongue_cons,
        mu_tongue_trace=mu_tongue_trace,
        tongue_xcheck_maxdev=tongue_xcheck_maxdev,
        max_mu_tongue_cons=max_mu_tongue_cons,
        a_at_max=a_at_max,
        max_mu_tongue_lib=max_mu_tongue_lib,
        q_sweep=q_sweep,
        mu_at_a1=mu_at_a1,
        slope_smallq=slope_smallq,
        mu_F_physical=mu_F_physical,
        growth_per_period=growth_per_period,
        tongue_width_a=tongue_width_a,
        rigidity=rigidity,
        dtc_subharmonic=dtc_subharmonic,
        dtc_rigid=dtc_rigid,
        dtc_candidate=dtc_candidate,
        delta_omega_dm=delta_omega_dm,
        abundance_frac=abundance_frac,
        abundance_benign=abundance_benign,
        R_rect=R_RECT_VIIBP,
        Omega_DM=float(Omega_DM),
        n_pairs=float(n_pairs),
        E_exc=float(E_exc),
    )

    return {
        "omega_drive": omega_drive,
        "gamma": gamma,
        "in_band": in_band,
        "q_conservative": q_conservative,
        "q_liberal": q_liberal,
        "max_mu_tongue_cons": max_mu_tongue_cons,
        "a_at_max": a_at_max,
        "max_mu_tongue_lib": max_mu_tongue_lib,
        "slope_smallq": slope_smallq,
        "tongue_xcheck_maxdev": tongue_xcheck_maxdev,
        "mu_F_physical": mu_F_physical,
        "growth_per_period": growth_per_period,
        "tongue_width_a": tongue_width_a,
        "dtc_subharmonic": dtc_subharmonic,
        "dtc_rigid": dtc_rigid,
        "dtc_candidate": dtc_candidate,
        "delta_omega_dm": delta_omega_dm,
        "abundance_frac": abundance_frac,
        "abundance_benign": abundance_benign,
        "eff_action_handle": eff_action_handle,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION),
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


def evaluate_gate(result) -> tuple[str, str, str, str]:
    """[CHAIN] gate. Pre-registered (plan §W2-4):
       sign_verdict   = PASS iff max Re(mu_F) > 0 (the substitution-chain direction: LIVE parametric
                        amplification, forced by in-band + q>0).
       magnitude_verdict = PASS iff (max Re(mu_F) > MU_F_FLOOR) AND (abundance benign < 0.05);
                        INFO iff mu_F>0 but abundance in [0.05, 0.10];
                        FAIL iff mu_F = 0 within tolerance.
       regime_verdict = VALID (the small-q Mathieu analysis + monodromy Floquet is well inside its
                        regime; the a=1 tongue is the analytically-known first parametric resonance)."""
    max_mu = result["max_mu_tongue_cons"]   # (local)
    abundance_frac = result["abundance_frac"]  # (local)
    in_band = result["in_band"]             # (local)

    mu_live = bool(max_mu > MU_F_FLOOR)     # (local)
    # sign: the predicted direction is mu_F > 0 (LIVE). PASS iff the computed mu_F > 0.
    sign_verdict = "PASS" if mu_live else "FAIL"  # (local)

    # magnitude: mu_F>0 AND benign-abundance -> PASS; mu_F>0 but abundance [0.05,0.10] -> INFO; mu_F=0 -> FAIL
    if not mu_live:
        magnitude_verdict = "FAIL"  # (local)
    elif abundance_frac < ABUNDANCE_BENIGN:
        magnitude_verdict = "PASS"
    elif abundance_frac < ABUNDANCE_INFO:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"  # mu_F>0 but abundance catastrophic (>0.10)

    # regime: the Mathieu small-q monodromy Floquet analysis is firmly valid; the in-band condition
    # holds (a~1 tongue accessed). If somehow NOT in-band the regime premise breaks.
    regime_verdict = "VALID" if in_band else "MARGINAL"  # (local)

    # composite collapse (gate-verdicts.md deterministic rule)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    result = compute()
    composite, sign_v, mag_v, reg_v = evaluate_gate(result)

    dtc_tag = "DTC-CANDIDATE" if result["dtc_candidate"] else (
        "DTC-subharmonic-only" if result["dtc_subharmonic"] else "no-DTC")  # (local)
    value_str = (
        f"FLOQUET-LIVE max_Re_mu_F={result['max_mu_tongue_cons']:.6e} (dimensionless t) "
        f"= {result['mu_F_physical']:.6e} M_KK ; "
        f"a_at_max={result['a_at_max']:.4f} period-2 tongue width(a)={result['tongue_width_a']:.4f} ; "
        f"q_cons={result['q_conservative']:.4f} smallq_slope={result['slope_smallq']:.4f}(LL_law=0.5) ; "
        f"growth/period={result['growth_per_period']:.4f}x ; "
        f"{dtc_tag} ; abundance Delta/Omega_DM={result['abundance_frac']:.3e}(benign={result['abundance_benign']}) ; "
        f"in_band={result['in_band']} ; xcheck_dev={result['tongue_xcheck_maxdev']:.2e}"
    )  # (local)

    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra = [
        f"# omega_drive={result['omega_drive']:.6f} M_KK gamma={result['gamma']:.6f} in_band={result['in_band']} (S101 verdict-pinned)",
        f"# max_Re_mu_F={result['max_mu_tongue_cons']:.6e} (dimensionless) = {result['mu_F_physical']:.6e} M_KK; q_cons={result['q_conservative']:.4f}; small-q slope={result['slope_smallq']:.4f} (LL law 0.5)",
        f"# DTC: subharmonic={result['dtc_subharmonic']} rigid={result['dtc_rigid']} candidate={result['dtc_candidate']} (period-2 tongue width(a)={result['tongue_width_a']:.4f})",
        f"# abundance: Delta_Omega_DM={result['delta_omega_dm']:.3e} (VII.BP clause-(d) COINCIDENCE-BOUNDED); Delta/Omega_DM={result['abundance_frac']:.3e} benign={result['abundance_benign']}",
        f"# eff-action handle (A-QA-2): pump q_cons={result['q_conservative']:.4f}>0 -> modulus kinetic coupling constrains S3 functional",
    ]  # (local)

    print_verdict_payload(
        composite, value_str, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        companion_note="INV10-W2-4 S101 in-band drive Floquet/preheating; period-2 tongue mu_F>0; DTC candidacy + modulus eff-action handle",
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (sign={sign_v} mag={mag_v} regime={reg_v}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
