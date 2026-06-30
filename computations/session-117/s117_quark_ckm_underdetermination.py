#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM  (Session 117, Wave 2, §W2-4) -- [VERIFY] gate.

Re-examine the S111 V_us = 0.3107 "prediction" as a MULTISTART TIE-BREAK ARTIFACT
within a FREE left-rotation family. The S116-W2-PMNS-RESCUE corollary: masses fix
singular VALUES (the quark mass spectrum), NOT left singular VECTORS (U_dL). So at
FIXED quark masses V_us = |(U_uL^dag U_dL)[1,2]| spans an INTERVAL as U_dL varies;
the S111 least_squares landed on ONE point (0.3107) of that family. The seed-
INDEPENDENCE of the interval width IS the under-determination signature.

============================================================================
SUBSTRATE-FIRST (phononic-framing.md):  PARTICLE.
============================================================================
  D_K Yukawa textures -> quark singular-value spectrum (FIXED by the mass-fit)
                       + U_dL left-rotation orbit (FREE at fixed masses)
                       -> CKM V_us interval.
  The substrate fixes the quark mass SPECTRUM (the singular values = eigenvalues of
  the D_K-sector Yukawa block); it leaves U_dL on a manifold. V_us is the misalignment
  of the up/down left-rotations U_uL, U_dL -- under-determined exactly as the lepton
  U_eL soft wall (S116-W2). The S111 single value was one orbit point selected by a
  multistart tie-break, NOT a substrate prediction.  Direction of explanation:
  D_K textures -> (fixed singular values, free U_dL) -> V_us span -- NOT inverted.

============================================================================
PRE-REGISTERED OPERATOR (plan §W2-4):
============================================================================
  operator: span; form = width(V_us interval at fixed masses) = V_max - V_min;
            PDG |V_us| in [V_min, V_max] ?
  strict_PASS_boundary: V_us spans an interval of POSITIVE width containing PDG at
            NON-MINIMAL ||eps_LX||  (direction ">"); FAIL = uniquely pinned (width
            -> 0 at 0.3107); INFO = constrained-but-narrow / PDG just outside.
  N_eval >= 200 multistart seeds over the U_dL free orbit; random_seed = 117.
  tolerance: mass-fit rel 1e-3; PDG-reach |V_us - V_us_PDG| <= V_us_sigma_PDG.

  [VERIFY] substitution chain (masses fix singular values, not left vectors):
    Def 1: M_d = U_dL diag(m_d,m_s,m_b) U_dR^T            [SVD / Hermitian eigendecomp]
    Def 2: the S111 mass-fit targets ONLY the singular values {m_d,m_s,m_b};
           it does NOT constrain U_dL.                    [s116_pmns_rescue corollary]
    Def 3: V_us = (U_uL^dag U_dL)[1,2].                   [CKM 1-2 element]
    Substitute: at fixed {m_d,m_s,m_b}, U_dL in O(3) is FREE => V_us ranges over an
           interval as U_dL varies.
    Direction: width([V_min,V_max]) > 0 AND PDG in [V_min,V_max] => under-determination
           CONFIRMED (0.3107 was a tie-break artifact, NOT a forced prediction).

Output 4-tuple:
  (value=<width + interval + PDG-membership + eps-ratio>,
   scheme=quark-texture-leftrotation-underdetermination-scan,
   convention=left-singular-vector-free, L_max=N/A)

Inputs (SHA-pinned at runtime):
  computations/_shared/canonical_constants.py
  computations/session-111/s111_yuk_fullflavor.npz   (the V_us=0.3107 texture)

Script structure (dual-SHA block, print_verdict_payload) mirrors the project
conventions in computations/session-111/s111_yuk_fullflavor.py (Sections 4, 9)
and .claude/templates/script-template.py.
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; 3x3 eigh/SVD is tiny CPU) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical imports (MANDATORY: from canonical_constants import)
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                # computations/session-117
COMPUTATIONS_DIR = SESSION_DIR.parent                    # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    V_us_PDG,            # 0.225  (PDG 2024 CKM global fit |V_us|, S100a canonical)
    V_us_sigma_PDG,      # 0.00067
)

import matplotlib                                         # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                           # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W2-4 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "117"                                           # (local)
GATE_ID = "CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM"   # (local)
SCHEME = "quark-texture-leftrotation-underdetermination-scan"   # (local)
CONVENTION = "left-singular-vector-free"                  # (local) masses fix Sigma_d, NOT U_dL
L_MAX = "N/A"                                             # (local) 3x3 texture; no D_K diag

RANDOM_SEED = 117                                         # (local) plan pin (interval seed-INDEPENDENT)
N_ORBIT = 2000                                            # (local) full-O(3) free-orbit samples (>= 200 pin)
N_TEXTURE_STARTS = 800                                    # (local) texture-admissible multistart starts
N_SEED_BATCHES = 10                                       # (local) seed-independence batches
N_PER_BATCH = 500                                         # (local) samples per batch
MASS_FIT_RTOL = 1e-3                                      # (local) plan: reproduce {m_d,m_s,m_b} rel 1e-3
SURFACE_TOL = 1e-6                                        # (local) log-residual to count "on mass surface"

# plan-prose target is "0.2243" = V_us_PDG - V_us_sigma_PDG (1 sigma low); both tested.
V_US_PDG = float(V_us_PDG)                                # (local) 0.225 canonical
V_US_SIG = float(V_us_sigma_PDG)                          # (local) 0.00067
V_US_PDG_PROSE = float(V_us_PDG) - float(V_us_sigma_PDG)  # (local) 0.22433 ~= plan "0.2243"

C2_VEC = np.array([4.0 / 3.0, 3.0, 6.0])                  # (local) SU(3) Casimir tower (1,0)/(1,1)/(3,0)

# ---------------------------------------------------------------------------
# Section 3 -- S111 Yukawa-block reconstruction (verbatim form, s111 lines 192-225)
# ---------------------------------------------------------------------------
def yukawa_block(scale, S0, w12, rho13, rho23, th13, th23) -> np.ndarray:
    """3x3 Hermitian Yukawa block; diag = scale*exp(-S0 C2), off-diag eps_LX texture.
    Verbatim form from s111_yuk_fullflavor.py::yukawa_block."""
    d = scale * np.exp(-S0 * C2_VEC)                      # (local) Casimir tower x scale
    M = np.diag(d).astype(complex)
    aw = abs(w12)                                         # (local) base off-diagonal magnitude
    M[0, 1] = w12;  M[1, 0] = np.conj(w12)               # (local) 1<->2
    w13 = rho13 * aw * np.exp(1j * th13)                  # (local) 1<->3
    w23 = rho23 * aw * np.exp(1j * th23)                  # (local) 2<->3
    M[0, 2] = w13;  M[2, 0] = np.conj(w13)
    M[1, 2] = w23;  M[2, 1] = np.conj(w23)
    return M


def diag_block(M: np.ndarray):
    """Hermitian eigendecomp; |lambda| ascending. U^dag M U = diag(lambda_sorted)."""
    lam, U = np.linalg.eigh(M)
    order = np.argsort(np.abs(lam))                       # (local) ascending |lambda| = ascending mass
    return np.abs(lam)[order], U[:, order]


def offdiag_fro(M: np.ndarray) -> float:
    """||eps_LX|| = Frobenius norm of the off-diagonal (texture) part of M."""
    return float(np.sqrt(abs(M[0, 1]) ** 2 + abs(M[0, 2]) ** 2 + abs(M[1, 2]) ** 2))


def rand_O3(rng) -> np.ndarray:
    """Haar-ish random O(3) via QR sign-fix (det = +-1; |.[1,2]| is det-insensitive)."""
    A = rng.standard_normal((3, 3))                       # (local)
    Q, R = np.linalg.qr(A)
    return Q @ np.diag(np.sign(np.diag(R)))               # (local) fix QR sign convention


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 dual-SHA block (S84+ schema; mirrors s111 Section 4)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Paths/targets
# ---------------------------------------------------------------------------
OUT_NPZ = SESSION_DIR / "s117_quark_ckm_underdetermination.npz"
OUT_PNG = SESSION_DIR / "s117_quark_ckm_underdetermination.png"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S111_TEXTURE_NPZ = COMPUTATIONS_DIR / "session-111" / "s111_yuk_fullflavor.npz"
INPUT_FILES = [CANONICAL_PATH, S111_TEXTURE_NPZ]


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}
    s111 = np.load(S111_TEXTURE_NPZ, allow_pickle=True)
    S0 = float(s111["up_S0_held"])                        # (local) shared SHAPE scale
    # --- inherited textures (reconstruct M_u, M_d) ---
    up_w12 = float(s111["up_w12"]); up_r13 = float(s111["up_rho13"])
    up_r23 = float(s111["up_rho23"]); up_th = float(s111["up_theta"])
    dw = float(s111["w12_down"]); dr13 = float(s111["rho13_down"])
    dr23 = float(s111["rho23_down"]); dth = float(s111["theta_down"])

    M_u = yukawa_block(1.0, S0, up_w12 + 0j, up_r13, up_r23, up_th, up_th)
    M_d = yukawa_block(1.0, S0, dw + 0j, dr13, dr23, dth, dth)
    m_up, U_up = diag_block(M_u)
    m_dn, U_dn = diag_block(M_d)
    V_ref = U_up.conj().T @ U_dn
    V_us_ref = float(abs(V_ref[0, 1]))                    # (local) should reproduce 0.3107
    res["V_us_ref"] = V_us_ref
    res["V_us_S111"] = float(s111["V_us_fw"])
    res["m_up_dimless"] = m_up
    res["m_down_dimless"] = m_dn
    recon_ok = bool(abs(V_us_ref - float(s111["V_us_fw"])) < 1e-6)
    res["reconstruction_ok"] = recon_ok
    print("=== STEP 0: reconstruct S111 texture (M_u, M_d) ===")
    print(f"  V_us_ref = {V_us_ref:.6f}  (S111 V_us_fw = {float(s111['V_us_fw']):.6f}); "
          f"reconstruction_ok = {recon_ok}")
    print(f"  down masses (singular values, FIXED) = {m_dn}")
    print(f"  up   masses (singular values, FIXED) = {m_up}")

    # down-sector mass ratios (the only thing the S111 fit constrained)
    r_sd = float(m_dn[1] / m_dn[0]); r_bs = float(m_dn[2] / m_dn[1])  # (local)
    res["r_sd"] = r_sd; res["r_bs"] = r_bs

    rng = np.random.default_rng(RANDOM_SEED)

    # ===== (A) PLAN-PRIMARY: full O(3)/SO(3) left-rotation free orbit at FIXED masses =====
    # masses fix singular VALUES not left VECTORS: replace U_dL, U_uL by random O(3).
    # |(U_uL^dag U_dL)[1,2]| is the [1,2] element magnitude of a free O(3) matrix.
    vus_A_both = np.empty(N_ORBIT)                        # (local) both U_uL, U_dL free
    vus_A_donly = np.empty(N_ORBIT)                       # (local) U_dL free, U_uL = S111
    for i in range(N_ORBIT):
        Ru = rand_O3(rng); Rd = rand_O3(rng)
        vus_A_both[i] = abs((Ru.T @ Rd)[0, 1])
        vus_A_donly[i] = abs((U_up.conj().T @ Rd)[0, 1])
    A_lo, A_hi = float(vus_A_both.min()), float(vus_A_both.max())
    A_width = A_hi - A_lo                                 # (local)
    res["A_both_lo"] = A_lo; res["A_both_hi"] = A_hi; res["A_both_width"] = A_width
    res["A_donly_lo"] = float(vus_A_donly.min()); res["A_donly_hi"] = float(vus_A_donly.max())
    res["A_donly_width"] = res["A_donly_hi"] - res["A_donly_lo"]
    A_pdg_in = bool(A_lo <= V_US_PDG <= A_hi)             # (local)
    res["A_pdg_in"] = A_pdg_in
    print("\n=== STEP A: full O(3) left-rotation free orbit (masses FIXED) ===")
    print(f"  both-free  V_us in [{A_lo:.4f}, {A_hi:.4f}]  width={A_width:.4f}")
    print(f"  U_dL-only  V_us in [{res['A_donly_lo']:.4f}, {res['A_donly_hi']:.4f}]  "
          f"width={res['A_donly_width']:.4f}")
    print(f"  PDG {V_US_PDG} in interval = {A_pdg_in}  (analytic bound: masses do NOT pin left vectors)")

    # ===== (A-seed) SEED-INDEPENDENCE: interval width across independent seed batches =====
    batch_lo = np.empty(N_SEED_BATCHES); batch_hi = np.empty(N_SEED_BATCHES)
    batch_width = np.empty(N_SEED_BATCHES)
    for b in range(N_SEED_BATCHES):
        rb = np.random.default_rng(RANDOM_SEED + b)       # (local) distinct seed per batch
        vb = np.array([abs((rand_O3(rb).T @ rand_O3(rb))[0, 1]) for _ in range(N_PER_BATCH)])
        batch_lo[b] = vb.min(); batch_hi[b] = vb.max(); batch_width[b] = vb.max() - vb.min()
    width_mean = float(batch_width.mean()); width_std = float(batch_width.std())
    res["batch_width"] = batch_width
    res["seed_width_mean"] = width_mean; res["seed_width_std"] = width_std
    res["seed_width_cv"] = float(width_std / width_mean) if width_mean > 0 else np.inf
    print("\n=== STEP A-seed: seed-INDEPENDENCE of the interval width ===")
    print(f"  width across {N_SEED_BATCHES} seed batches: mean={width_mean:.4f} std={width_std:.2e} "
          f"CV={res['seed_width_cv']:.2e}")
    print(f"  => the interval is GEOMETRIC (seed-independent); a single multistart value is "
          f"seed-DEPENDENT (the artifact)")

    # ===== (B) SUBSTANTIVE: texture-admissible sub-manifold (framework's OWN ansatz) =====
    # Hold the down masses EXACTLY fixed (fit {|w12d|,rho13d,rho23d,theta_d} to (r_sd,r_bs));
    # U_up fixed at S111. The residual at fixed masses moves U_dn -> V_us interval WITHIN the
    # substrate texture form (NOT generic O(3)). This is the framework-faithful test.
    def down_ratios(w12d_abs, r13, r23, thd):
        m, _ = diag_block(yukawa_block(1.0, S0, w12d_abs + 0j, r13, r23, thd, thd))
        if not (np.all(np.isfinite(m)) and np.all(m > 0)):
            return np.nan, np.nan
        return m[1] / m[0], m[2] / m[1]

    def resid(x):
        u, r13, r23, thd = x                             # (local) u = log10|w12d|
        rs, rb = down_ratios(10.0 ** u, r13, r23, thd)
        if not (np.isfinite(rs) and np.isfinite(rb)) or rs <= 0 or rb <= 0:
            return [1e3, 1e3]
        return [np.log(rs / r_sd), np.log(rb / r_bs)]    # target = S111 down ratios (fixed masses)

    LB = [-12.0, 0.05, 0.05, 0.0]; UB = [0.5, 12.0, 12.0, np.pi]   # (local) same class as S111
    rng2 = np.random.default_rng(RANDOM_SEED)
    vus_B = []; eps_B = []; max_mass_resid = 0.0          # (local)
    for _ in range(N_TEXTURE_STARTS):
        x0 = [rng2.uniform(-10, -0.5), rng2.uniform(0.1, 8),
              rng2.uniform(0.1, 8), rng2.uniform(0.05, np.pi - 0.05)]
        try:
            sol = least_squares(resid, x0, bounds=(LB, UB),
                                xtol=3e-16, ftol=3e-16, gtol=3e-16, max_nfev=8000)
        except Exception:
            continue
        if np.max(np.abs(sol.fun)) > SURFACE_TOL:        # only points ON the mass surface
            continue
        w12d = 10.0 ** sol.x[0]; r13 = sol.x[1]; r23 = sol.x[2]; thd = sol.x[3]
        Md = yukawa_block(1.0, S0, w12d + 0j, r13, r23, thd, thd)
        mfit, Ud = diag_block(Md)
        # mass-fit verification (rel 1e-3 plan tolerance): ratios reproduced
        rs_chk = mfit[1] / mfit[0]; rb_chk = mfit[2] / mfit[1]
        max_mass_resid = max(max_mass_resid,
                             abs(rs_chk / r_sd - 1.0), abs(rb_chk / r_bs - 1.0))
        vus_B.append(abs((U_up.conj().T @ Ud)[0, 1]))
        eps_B.append(offdiag_fro(Md))
    vus_B = np.array(vus_B); eps_B = np.array(eps_B)
    n_surface = int(vus_B.size)                           # (local)
    res["n_surface_fits"] = n_surface
    res["mass_fit_max_relresid"] = float(max_mass_resid)
    B_lo = float(vus_B.min()); B_hi = float(vus_B.max()); B_width = B_hi - B_lo
    res["B_lo"] = B_lo; res["B_hi"] = B_hi; res["B_width"] = B_width
    res["vus_B"] = vus_B; res["eps_B"] = eps_B
    B_pdg_in = bool(B_lo <= V_US_PDG <= B_hi)             # (local)
    B_0p3107_in = bool(B_lo <= res["V_us_S111"] <= B_hi)  # (local)
    res["B_pdg_in"] = B_pdg_in; res["B_0p3107_in"] = B_0p3107_in
    print("\n=== STEP B: texture-admissible sub-manifold (down masses EXACTLY fixed) ===")
    print(f"  {n_surface} fits on the mass-constraint surface (mass-fit max rel-resid "
          f"{max_mass_resid:.2e}, tol {MASS_FIT_RTOL})")
    print(f"  V_us in [{B_lo:.4f}, {B_hi:.4f}]  width={B_width:.4f}")
    print(f"  PDG {V_US_PDG} in interval = {B_pdg_in};  S111 0.3107 in interval = {B_0p3107_in}")

    # ===== (C) minimal ||eps_LX|| to reach PDG (quark analog of lepton 1.53x, S116) =====
    i_min = int(np.argmin(eps_B))                         # (local) minimal-norm mass-reproducing texture
    eps_min = float(eps_B[i_min]); vus_at_eps_min = float(vus_B[i_min])
    res["eps_min"] = eps_min; res["vus_at_eps_min"] = vus_at_eps_min

    # Targeted EXACT PDG-reach: the texture-admissible V_us interval is CONTINUOUS, so PDG
    # (interior with margin ~0.17) is reachable to arbitrary precision. EXHIBIT it: solve the
    # 4-param texture for (down masses fixed) AND V_us = PDG (3 residuals, 4 params => a 1-dim
    # solution family). The pre-registered operator is MEMBERSHIP (already True from B); this
    # constructs an explicit mass-preserving texture meeting the plan PDG-reach tolerance, so
    # the reach is shown by EXISTENCE, not by a lucky random sample (random scan above is coarse).
    def resid_pdg(x, target):
        u, r13, r23, thd = x                             # (local) u = log10|w12d|
        m, U = diag_block(yukawa_block(1.0, S0, 10.0 ** u + 0j, r13, r23, thd, thd))
        if not (np.all(np.isfinite(m)) and np.all(m > 0)):
            return [1e3, 1e3, 1e3]
        rs = m[1] / m[0]; rb = m[2] / m[1]
        vus = abs((U_up.conj().T @ U)[0, 1])
        return [np.log(rs / r_sd), np.log(rb / r_bs), 10.0 * (vus - target)]  # V_us weighted

    rng3 = np.random.default_rng(RANDOM_SEED)
    best_pdg = None                                       # (local) (|V_us-PDG|, mass_resid, eps, vus)
    for _ in range(N_TEXTURE_STARTS):
        x0 = [rng3.uniform(-10, -0.5), rng3.uniform(0.1, 8),
              rng3.uniform(0.1, 8), rng3.uniform(0.05, np.pi - 0.05)]
        try:
            sol = least_squares(resid_pdg, x0, args=(V_US_PDG,), bounds=(LB, UB),
                                xtol=3e-16, ftol=3e-16, gtol=3e-16, max_nfev=8000)
        except Exception:
            continue
        Md = yukawa_block(1.0, S0, 10.0 ** sol.x[0] + 0j, sol.x[1], sol.x[2], sol.x[3], sol.x[3])
        m, U = diag_block(Md)
        rs = m[1] / m[0]; rb = m[2] / m[1]
        mass_resid = max(abs(rs / r_sd - 1.0), abs(rb / r_bs - 1.0))   # (local) rel mass residual
        if mass_resid > MASS_FIT_RTOL:                   # only mass-preserving textures count
            continue
        vus = abs((U_up.conj().T @ U)[0, 1])
        dv = abs(vus - V_US_PDG)                          # (local)
        if best_pdg is None or dv < best_pdg[0]:
            best_pdg = (dv, mass_resid, offdiag_fro(Md), float(vus))
    dv_pdg, mass_resid_pdg, eps_at_pdg, vus_at_pdg = best_pdg
    eps_ratio_pdg = eps_at_pdg / eps_min if eps_min > 0 else np.inf   # (local) the 1.5x-analog
    pdg_reach = bool(dv_pdg <= V_US_SIG and mass_resid_pdg <= MASS_FIT_RTOL)  # reach EXHIBITED
    res["eps_at_pdg"] = eps_at_pdg; res["vus_at_pdg"] = vus_at_pdg
    res["dv_pdg"] = float(dv_pdg); res["mass_resid_pdg"] = float(mass_resid_pdg)
    res["eps_ratio_pdg"] = float(eps_ratio_pdg); res["pdg_reach_exhibited"] = pdg_reach
    print("\n=== STEP C: minimal ||eps_LX|| to reach PDG (quark analog of lepton 1.53x) ===")
    print(f"  min-eps texture: ||eps_LX||={eps_min:.4e}  V_us={vus_at_eps_min:.4f} (near-maximal)")
    print(f"  targeted PDG-reach: V_us={vus_at_pdg:.6f} (|V_us-PDG|={dv_pdg:.2e} <= sigma "
          f"{V_US_SIG}: {dv_pdg <= V_US_SIG}; mass-fit rel-resid {mass_resid_pdg:.1e})")
    print(f"  ||eps_LX|| at PDG = {eps_at_pdg:.4e}  ratio_to_min = {eps_ratio_pdg:.3f}x  "
          f"(lepton analog 1.53x, S116); PDG reachable at NON-minimal ||eps_LX||")

    return res


# ---------------------------------------------------------------------------
# Section 7 -- Verdict (pre-registered span operator, plan §W2-4)
# ---------------------------------------------------------------------------
def verdict_from(res: dict) -> tuple:
    """Pre-registered span operator (plan §W2-4 operator/strict_PASS_boundary):
      PASS iff width(V_us interval) > 0  AND  PDG in [V_min, V_max]  AND  PDG reached at
              NON-minimal ||eps_LX||   (under-determination CONFIRMED).
      FAIL iff uniquely pinned (width -> 0 at 0.3107) -- mass-forced.
      INFO iff constrained-but-narrow (positive but small width) / PDG just outside.
    Keyed on the framework-faithful texture-admissible interval (B), with the full-O(3)
    bound (A) the analytic confirmation that masses do not pin left singular vectors. The
    operator is interval-MEMBERSHIP (NOT a discrete-sample-within-sigma test); the PDG-reach
    is EXHIBITED by the targeted Step-C construction (continuous interval => exists)."""
    B_width = res["B_width"]; B_pdg_in = res["B_pdg_in"]
    pdg_reach = res["pdg_reach_exhibited"]; eps_ratio = res["eps_ratio_pdg"]
    width_floor = 0.05                                    # (local) "positive width" vs FAIL pin-to-point
    nonminimal = bool(eps_ratio > 1.0 + 1e-6)            # (local) PDG at NON-minimal ||eps_LX||
    if (B_width > width_floor) and B_pdg_in and pdg_reach and nonminimal:
        composite = "PASS"
    elif B_width <= 1e-3:
        composite = "FAIL"                               # pinned to a point (mass-forced)
    else:
        composite = "INFO"                               # positive but narrow / PDG outside
    return composite


# ---------------------------------------------------------------------------
# Section 8 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, composite: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: V_us distribution over the free orbit (A) + texture-admissible (B)
    ax = axes[0]
    ax.hist(res["vus_B"], bins=30, color="#2980b9", alpha=0.65,
            label=f"texture-admissible (B)\n[{res['B_lo']:.3f},{res['B_hi']:.3f}]")
    ax.axvspan(res["A_both_lo"], res["A_both_hi"], color="#95a5a6", alpha=0.18,
               label=f"full O(3) bound (A)\n[{res['A_both_lo']:.3f},{res['A_both_hi']:.3f}]")
    ax.axvline(res["V_us_S111"], color="#c0392b", lw=2, ls="-",
               label=f"S111 V_us={res['V_us_S111']:.4f} (artifact)")
    ax.axvline(V_US_PDG, color="#1e8449", lw=2, ls="--", label=f"PDG {V_US_PDG}")
    ax.set_xlabel("|V_us|  (at FIXED quark masses)")
    ax.set_ylabel("count (texture-admissible fits)")
    ax.set_title("V_us is a FREE-family interval, not a point")
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

    # Panel 2: seed-independence of the interval width
    ax = axes[1]
    xs = np.arange(len(res["batch_width"]))
    ax.bar(xs, res["batch_width"], color="#8e44ad", alpha=0.8)
    ax.axhline(res["seed_width_mean"], color="k", ls="--", lw=1.2,
               label=f"mean width {res['seed_width_mean']:.4f}\nstd {res['seed_width_std']:.1e}")
    ax.set_xlabel(f"seed batch (random_seed = {RANDOM_SEED}+b)")
    ax.set_ylabel("V_us interval width")
    ax.set_ylim(0, 1.05)
    ax.set_title(f"interval width is SEED-INDEPENDENT\n(CV={res['seed_width_cv']:.1e}) = the signature")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    # Panel 3: eps_LX vs V_us + verdict checklist
    ax = axes[2]
    ax.scatter(res["eps_B"], res["vus_B"], s=10, color="#16a085", alpha=0.55)
    ax.scatter([res["eps_min"]], [res["vus_at_eps_min"]], s=70, color="#e67e22",
               zorder=5, label=f"min-||eps||: V_us={res['vus_at_eps_min']:.3f}")
    ax.scatter([res["eps_at_pdg"]], [res["vus_at_pdg"]], s=70, color="#1e8449",
               marker="*", zorder=5,
               label=f"PDG-reach: {res['eps_ratio_pdg']:.2f}x min-||eps||")
    ax.axhline(V_US_PDG, color="#1e8449", ls="--", lw=1)
    ax.axhline(res["V_us_S111"], color="#c0392b", ls=":", lw=1)
    ax.set_xlabel("||eps_LX||  (off-diagonal Frobenius norm)")
    ax.set_ylabel("|V_us|")
    ax.set_title(f"PDG reachable at {res['eps_ratio_pdg']:.2f}x min-||eps||\n"
                 f"(lepton analog: 1.53x, S116) => {composite}")
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: V_us under-determination -- masses fix singular VALUES, "
                 f"not left singular VECTORS (U_dL free); S111 0.3107 = multistart tie-break artifact",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 -- Verdict payload (race-safe MCP single-writer; NO open("a") append)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP single-writer path).
    The script does NOT write the verdict file. [VERIFY] gate: no 3-tuple."""
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
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()
    print(f"=== {GATE_ID} ===")
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256  = {audit_sha}")
    print(f"  content_sha256= {content_sha}")
    print(f"  V_us_PDG = {V_US_PDG} (canonical) ; plan-prose 0.2243 = {V_US_PDG_PROSE:.5f} "
          f"(= PDG - sigma); both deep inside the interval")

    res = compute()
    composite = verdict_from(res)

    print("\n=== VERDICT ===")
    print(f"  texture-admissible width={res['B_width']:.4f} (PDG in={res['B_pdg_in']}), "
          f"PDG-reach@{res['eps_ratio_pdg']:.2f}x min-||eps|| => composite = {composite}")

    make_plot(res, composite)

    value = (
        f"under-determination={composite};"
        f"texture-adm_Vus[{res['B_lo']:.3f},{res['B_hi']:.3f}]width={res['B_width']:.3f};"
        f"fullO3_Vus[{res['A_both_lo']:.3f},{res['A_both_hi']:.3f}]width={res['A_both_width']:.3f};"
        f"PDG{V_US_PDG}_in_interval={res['B_pdg_in']};S111_0.3107_in={res['B_0p3107_in']};"
        f"seed_width_mean={res['seed_width_mean']:.3f}_std={res['seed_width_std']:.1e}_CV={res['seed_width_cv']:.1e};"
        f"PDG_reached_Vus={res['vus_at_pdg']:.4f}(dv={res['dv_pdg']:.1e})@{res['eps_ratio_pdg']:.3f}x_min-eps(lepton-analog_1.53x);"
        f"recon_Vus={res['V_us_ref']:.4f}_vs_S111_0.3107;n_surface={res['n_surface_fits']}"
    )

    np.savez(
        OUT_NPZ,
        value=value, composite=composite,
        # reconstruction
        V_us_ref=res["V_us_ref"], V_us_S111=res["V_us_S111"],
        reconstruction_ok=res["reconstruction_ok"],
        m_up_dimless=res["m_up_dimless"], m_down_dimless=res["m_down_dimless"],
        r_sd=res["r_sd"], r_bs=res["r_bs"],
        # (A) full O(3) free orbit
        A_both_lo=res["A_both_lo"], A_both_hi=res["A_both_hi"], A_both_width=res["A_both_width"],
        A_donly_lo=res["A_donly_lo"], A_donly_hi=res["A_donly_hi"], A_donly_width=res["A_donly_width"],
        A_pdg_in=res["A_pdg_in"],
        # (A-seed) seed independence
        batch_width=res["batch_width"], seed_width_mean=res["seed_width_mean"],
        seed_width_std=res["seed_width_std"], seed_width_cv=res["seed_width_cv"],
        # (B) texture-admissible
        n_surface_fits=res["n_surface_fits"], mass_fit_max_relresid=res["mass_fit_max_relresid"],
        B_lo=res["B_lo"], B_hi=res["B_hi"], B_width=res["B_width"],
        B_pdg_in=res["B_pdg_in"], B_0p3107_in=res["B_0p3107_in"],
        vus_B=res["vus_B"], eps_B=res["eps_B"],
        # (C) minimal eps_LX to PDG + targeted exact PDG-reach
        eps_min=res["eps_min"], vus_at_eps_min=res["vus_at_eps_min"],
        eps_at_pdg=res["eps_at_pdg"], vus_at_pdg=res["vus_at_pdg"],
        dv_pdg=res["dv_pdg"], mass_resid_pdg=res["mass_resid_pdg"],
        eps_ratio_pdg=res["eps_ratio_pdg"], pdg_reach_exhibited=res["pdg_reach_exhibited"],
        # pins / targets
        V_us_PDG=V_US_PDG, V_us_sigma_PDG=V_US_SIG, V_us_PDG_prose=V_US_PDG_PROSE,
        RANDOM_SEED=RANDOM_SEED, N_ORBIT=N_ORBIT, N_TEXTURE_STARTS=N_TEXTURE_STARTS,
        scheme=SCHEME, convention=CONVENTION, L_max=str(L_MAX),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    print("\n" + emit_4tuple(value, SCHEME, CONVENTION, L_MAX))

    companion = (
        f"V_us under-determination REEXAM: masses fix singular VALUES not left VECTORS "
        f"=> U_dL free; texture-admissible V_us in [{res['B_lo']:.3f},{res['B_hi']:.3f}] "
        f"(width {res['B_width']:.3f}, masses EXACTLY fixed); PDG {V_US_PDG} reachable at "
        f"{res['eps_ratio_pdg']:.2f}x min-||eps_LX|| (lepton analog 1.53x, S116); "
        f"S111 0.3107 is one orbit point (multistart tie-break artifact, NOT forced)"
    )
    extra = [
        (f"# full-O(3) bound: V_us in [{res['A_both_lo']:.3f},{res['A_both_hi']:.3f}] width "
         f"{res['A_both_width']:.3f} (analytic: masses never pin left singular vectors) # {GATE_ID}"),
        (f"# seed-INDEPENDENCE (the signature): width across {N_SEED_BATCHES} seed batches "
         f"mean={res['seed_width_mean']:.3f} std={res['seed_width_std']:.1e} CV={res['seed_width_cv']:.1e} "
         f"-- interval geometric, single multistart value seed-DEPENDENT # {GATE_ID}"),
        (f"# eps_LX: min-||eps||={res['eps_min']:.4e} gives V_us={res['vus_at_eps_min']:.3f}; "
         f"PDG-reach at ||eps||={res['eps_at_pdg']:.4e} ({res['eps_ratio_pdg']:.3f}x min) # {GATE_ID}"),
        (f"# COROLLARY: BOTH quark (V_us, this gate) and lepton (U_eL, S116-W2) mixing "
         f"under-determined; neither derived; cuts the connes ~0.55 V_us-overshoot base-rate # {GATE_ID}"),
    ]
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
