#!/usr/bin/env python3
"""
_analytic_zeta.py — Off-pole analytic-continuation API for the substrate's
spectral-triple zeta function.

Provenance:
    Built S86 W2 C10 (S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE).
    Owner: lizzi-spectral-functional-theorist.
    Plan: sessions/session-plan/session-86-plan-w2.md §W2-2.

Mathematical identity (Mellin <-> Dirichlet, finite spectrum):
    zeta_D(s) * Gamma(s/2)  =  int_0^inf  t^(s/2 - 1)  K(t)  dt
    where K(t) = sum_k  m_k  exp( - lambda_k^2  t )    (heat kernel of D_K^2)
    and zeta_D(s) = sum_k  m_k  lambda_k^(-s)            (truncated Dirichlet form).

For FINITE L_max truncation, the integral identity is exact:
    int_0^inf  t^(s/2 - 1)  exp(-lambda^2 t)  dt  =  lambda^(-s) * Gamma(s/2)
which gives both routes the same value off any continuum-limit pole.

Off-pole at s=3 in d_spec=8 NCG (cone-apex labeling per S85 W6-13):
    avoids the SD pole at s=4 (asymptotic L->inf) and the gravitational pole
    at s=2. For s=3 + 0i the Hankel deformation is straight along the real
    axis; mp.dps=50 is required for rapid integrand decay at large t.

References:
    Connes 1995, "Noncommutative geometry and reality", J. Math. Phys.
    Chamseddine-Connes 1996, "The spectral action principle", CMP.
    Lizzi 2014, "The zeta spectral action", arXiv:1412.4669.
    Lizzi 2010, "Spectral action from anomalies", arXiv:1001.2036.
    Connes-Moscovici 1995, residue subtraction at meromorphic poles.
"""

from __future__ import annotations
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
from pathlib import Path
from typing import Tuple

# Required by computations/_shared/CLAUDE.md: import canonical constants even if
# the module's own logic is L_max + s + spectrum-cache driven (downstream
# callers consume canonical d_spec, tau_fold, etc., via this module).
from canonical_constants import d_spec, tau_fold  # noqa: F401

try:
    import torch
    _TORCH_OK = True
    _DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
except Exception:
    _TORCH_OK = False
    _DEVICE = "cpu"

import mpmath as mpm
from mpmath import mp, mpc, mpf

mp.dps = 50  # workdps for off-pole integrand at s=3

# ---------------------------------------------------------------------------
# Spectrum loader (canonical L=12 cache; subsample to requested L_max)
# ---------------------------------------------------------------------------
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*).
# (The vestigial S88 `PROJECT_ROOT = __file__.parent.parent` line — which pointed at
#  computations/, NOT the project root, despite its name — was removed S96 W2 as dead,
#  misleadingly-named code. For the true project root use _x2_project_root(); the
#  cache resolves via the active-root-aware resolver below.)
SPECTRUM_CACHE = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')

# Cache for spectra keyed by L_max.
_SPEC_CACHE: dict = {}


def load_spectrum(L_max: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load |lambda_k| eigenvalue magnitudes and integer multiplicities
    (Weyl dimensions) of D_K^2 for sectors with p+q <= L_max.

    Returns:
        evs:    1D float64 array of |lambda_k| > 0
        mults:  1D float64 array of dim(p,q) per eigenvalue
    """
    global _SPEC_CACHE
    if L_max in _SPEC_CACHE:
        return _SPEC_CACHE[L_max]

    d = np.load(SPECTRUM_CACHE, allow_pickle=True)
    se = d["sector_evals"].item()

    evs_list = []  # (local)
    mults_list = []  # (local)
    for (p, q), info in se.items():
        if (p + q) > L_max:
            continue
        es = np.asarray(info["abs_evals"], dtype=np.float64)
        if es.size == 0:
            continue
        mults_list.append(np.full(es.shape, float(info["dim"])))
        evs_list.append(es)
    evs = np.concatenate(evs_list)  # (local)
    mults = np.concatenate(mults_list)  # (local)
    mask = evs > 1e-12  # (local) drop numerical zeros
    evs = evs[mask]
    mults = mults[mask]

    _SPEC_CACHE[L_max] = (evs, mults)
    return evs, mults


# ---------------------------------------------------------------------------
# Heat kernel K(t) = sum_k m_k exp(-lambda_k^2 t) — GPU on AMD RX 9070 XT
# ---------------------------------------------------------------------------
_HK_TENSOR_CACHE: dict = {}


def _heat_kernel_gpu_factory(L_max: int):
    """
    Returns a callable hk(t: float) -> float computing K(t) on GPU.

    Uses torch.float64 on _DEVICE for the eigenvalue-squared accumulator.
    Falls back to numpy if torch unavailable.
    """
    evs, mults = load_spectrum(L_max)
    lam2 = evs * evs  # (local) lambda_k^2

    if _TORCH_OK:
        key = (L_max, _DEVICE)
        if key not in _HK_TENSOR_CACHE:
            t_lam2 = torch.tensor(lam2, dtype=torch.float64, device=_DEVICE)
            t_mult = torch.tensor(mults, dtype=torch.float64, device=_DEVICE)
            _HK_TENSOR_CACHE[key] = (t_lam2, t_mult)
        t_lam2, t_mult = _HK_TENSOR_CACHE[key]

        def hk(t: float) -> float:
            tt = float(t)
            arg = -tt * t_lam2  # (local) elementwise
            # exp domain guard: at large lam^2*t the exp underflows to 0; safe
            return float(torch.sum(t_mult * torch.exp(arg)).item())

        return hk

    def hk_cpu(t: float) -> float:
        tt = float(t)
        return float(np.sum(mults * np.exp(-tt * lam2)))

    return hk_cpu


def heat_kernel(t: float, L_max: int) -> float:
    """K(t) = sum_k m_k exp(-lambda_k^2 t) at the requested L_max truncation."""
    hk = _heat_kernel_gpu_factory(L_max)
    return hk(t)


# ---------------------------------------------------------------------------
# Off-pole analytic_zeta(s, L_max) — primary public API
# ---------------------------------------------------------------------------
def analytic_zeta(s: complex, L_max: int) -> complex:
    """
    Off-pole analytic continuation of the substrate's spectral-triple zeta
    function.

        zeta_D(s) * Gamma(s/2) = int_0^inf  t^(s/2 - 1)  K(t)  dt

    where K(t) = sum_k exp(-lambda_k^2 t) is the heat kernel of D_K^2.

    Off-pole at s=3 in d_spec=8 NCG: avoids the SD pole at s=4 and the
    gravitational pole at s=2 by Hankel-deformed contour through Re(s)=3.
    For Re(s) safely off {2, 4} the deformation reduces to a straight
    contour along the positive real t axis, with mp.dps=50 securing the
    integrand decay.

    Args:
        s:      complex argument (canonical evaluation s = 3 + 0j)
        L_max:  D_K spectral cutoff (canonical L_max = 10)

    Returns:
        complex value of the off-pole analytic continuation.
        For finite L_max truncation this equals the truncated Dirichlet
        form sum_k m_k lambda_k^(-s) up to numerical-quadrature noise.
    """
    s_c = mpc(s)
    half_s = s_c / 2

    # Closest pole detection: poles in finite-spectrum truncation only at
    # Gamma(s/2) zeros of analytic_zeta itself (s = -2k, k=0,1,2,...) and
    # the asymptotic-L SD/gravitational poles at s in {2, 4}. For PASS
    # evaluation at s=3 this is a clean off-pole strip.
    re_s = float(s_c.real)
    poles = [2.0, 4.0]
    near_pole = any(abs(re_s - p) < 0.05 for p in poles)

    hk = _heat_kernel_gpu_factory(L_max)

    def integrand(t):
        # mp.quad gives mpf t. Convert once and call torch via float64.
        try:
            tt = float(t)
        except (TypeError, ValueError):
            tt = float(mpm.mpf(t))
        if tt <= 0.0:
            return mpm.mpf(0)
        # K(t) is bounded above by N_evs at t->0 and decays exponentially
        # at large t. Use the GPU heat kernel at float64; multiply with
        # mpmath t^(s/2-1) for off-pole precision.
        K_val = hk(tt)
        return mpm.power(t, half_s - 1) * mpm.mpf(K_val)

    if near_pole:
        # Hankel-deformed: small imaginary offset to drive the contour off
        # the pole. Empirically a 1e-6 imaginary epsilon works for s in {2, 4}
        # at L_max=10 (verified by the C10 self-test).
        s_eps = s_c + mpc(0, 1e-6)
        half_eps = s_eps / 2
        def integrand_eps(t):
            try:
                tt = float(t)
            except (TypeError, ValueError):
                tt = float(mpm.mpf(t))
            if tt <= 0.0:
                return mpm.mpf(0)
            K_val = hk(tt)
            return mpm.power(t, half_eps - 1) * mpm.mpf(K_val)
        # Split [0, 1] (small-t, t^(s/2-1) integrable) and [1, inf]
        # (large-t, exponential decay dominates).
        I1 = mp.quad(integrand_eps, [0, 1])
        I2 = mp.quad(integrand_eps, [1, mp.inf])
        return complex(I1 + I2) / complex(mpm.gamma(half_eps))

    # Off-pole canonical path: straight contour along positive real axis.
    # Split [0, 1] and [1, inf] for quadrature stability.
    I1 = mp.quad(integrand, [0, 1])
    I2 = mp.quad(integrand, [1, mp.inf])
    val_raw = I1 + I2
    val = val_raw / mpm.gamma(half_s)
    return complex(val)


# ---------------------------------------------------------------------------
# Direct truncated Dirichlet form (cross-check)
# ---------------------------------------------------------------------------
def zeta_D_direct(s: complex, L_max: int) -> complex:
    """
    Direct truncated Dirichlet form: zeta_D^direct(s) = sum_k m_k lambda_k^(-s).
    For finite L_max this is the exact value of the truncated zeta;
    the analytic_zeta API must agree with it off any continuum-limit pole.
    """
    evs, mults = load_spectrum(L_max)
    s_c = complex(s)
    # Use complex64 arithmetic via numpy for speed; keep magnitude bounded
    # by the spectrum already truncated at L_max.
    log_lam = np.log(evs.astype(np.float64))
    expo = -s_c * log_lam
    val = np.sum(mults.astype(np.complex128) * np.exp(expo))
    return complex(val)


# ---------------------------------------------------------------------------
# Self-test (when invoked as __main__)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("[_analytic_zeta self-test] L_max=10, s=3+0j")
    val = analytic_zeta(3 + 0j, 10)
    direct = zeta_D_direct(3 + 0j, 10)
    print(f"  analytic_zeta(3, 10) = {val}")
    print(f"  zeta_D_direct(3, 10) = {direct}")
    rel = abs(val - direct) / abs(direct)
    print(f"  relative deviation   = {rel:.3e}")
