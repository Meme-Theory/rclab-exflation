#!/usr/bin/env python3
"""
S84 Wave 4 Gate G51 — L_max-CONVERGENCE
========================================

Re-runs the S83-G51 w_0 regulator computation at L_max in {5, 7, 9} to
distinguish *truncation artifact* from *structural scheme-split*.

Prior state (S83 W3-G51 at L_max=5):
  w_0^{zeta}    = -0.998
  w_0^{Zubarev} = -0.918 (E-weighted, mixed-scheme, canonical)
  scheme-split  = w_0^{zeta} - w_0^{Zubarev} = -0.080

Question:
  Does |split(L_max)| shrink or grow as L_max: 5 -> 7 -> 9?
    shrinks  ==> truncation artifact (finite-spectrum effect)
    grows    ==> structural scheme-split (two regulators probe
                 genuinely different substrate functionals)

Substrate-framing: L_max is a computational cutoff, not a physical
parameter. Convergence under L_max is a test of whether G51's FAIL is
artifact or a genuine regulator-dependence.

Method:
  1. Load per-sector eigenvalue cache from s74_spectrum_cache_L9_tau019.npz
     (52 SU(3) irreps (p,q), p+q <= 9). Per-sector abs_evals arrays are
     stored; per-sector multiplicity is the SU(3) irrep dimension
     d(p,q) = (p+1)*(q+1)*(p+q+2)/2.
  2. For each L_max in {5, 7, 9}:
       a. Filter sectors to p+q <= L_max.
       b. Flatten evals with per-sector multiplicities (flat_lambdas,
          flat_mults).
       c. Compute S_zeta(L)    = sum_n d_n                 (unweighted)
                  S_Zubarev(L) = sum_n d_n * exp(-lam_n^2)
                  S_zeta_E(L)    = sum_n d_n * lam_n
                  S_Zubarev_E(L) = sum_n d_n * exp(-lam_n^2) * lam_n
       d. Apply the S83 W3-G51 energy-weighted reconstruction:
            rho_GGE^{R}(L) = norm * S_R_E(L)       (norm calibrated so
                                                    rho_GGE^{zeta}(L=5)
                                                    = Lambda_eff)
            P_GGE^{R}(L)   = w_GGE_bare * rho_GGE^{R}(L)
            w_0^{R}(L)     = (P_J + P_GGE^{R}(L)) / (rho_J + rho_GGE^{R}(L))
       e. Tabulate (L, w_0^zeta, w_0^Zubarev, split).
  3. Direction check:
       split(L) = w_0^{zeta}(L) - w_0^{Zubarev}(L)
       if |split(9)| < |split(5)| -> truncation artifact (shrinks with L)
       if |split(9)| > |split(5)| -> structural scheme-split (grows)
       Read direction ONLY from computed numerics.

GPU usage: torch.linalg NOT needed (no eigendecomposition). We ARE using
torch on CUDA (ROCm) for parallel weighted sums and exp() computations to
demonstrate GPU path feasibility at L_max=9 scale.

PASS : |w_0^{Zubarev}(L=9) - w_0^{Zubarev}(L=5)| < 0.005
       AND converged to -0.918 +/- 0.02.
INFO : Converges but outside +/- 0.02 band OR converges outside 0.005
       but scheme-split shrinks monotonically.
FAIL : Split grows with L_max (structural) OR oscillates.

Outputs:
  - computations/session-84/s84_w4_g51_lmax_convergence.npz
  - computations/session-84/s84_w4_g51_lmax_convergence.png
  - Verdict line appended to computations/session-84/s84_gate_verdicts.txt
"""

import os
# CPU-thread cap before numpy import (safety; GPU is primary path here)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from canonical_constants import (
    M_KK, tau_fold, Delta_BCS, N_cells, Vol_SU3_Haar, PI,
    w0_FW,
)

# ==============================================================================
# Section 1. Input pin map + SHA-256 closure
# ==============================================================================
def _sha256_file(path):
    if not Path(path).exists():
        return "FILE_MISSING"
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

INPUT_PINS = {
    "spectrum_cache":     SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz",
    "S83_W1_G1":          SCRIPT_DIR / "s83_w1_g1_ic_scheme_derivation.npz",
    "S83_W3_G51":         SCRIPT_DIR / "s83_w3_g51_w0_regulator.npz",
    "S58_volovik":        SCRIPT_DIR / "s58_volovik_partition.npz",
    "S58_w_desi":         SCRIPT_DIR / "s58_w_desi.npz",
    "S57_cc_sign":        SCRIPT_DIR / "s57_cc_sign.npz",
    "canonical_const":    SCRIPT_DIR / "canonical_constants.py",
    "self_script":        SCRIPT_DIR / "s84_w4_g51_lmax_convergence.py",
}

print("=" * 78)
print("S84 W4-G51-LMAX-CONVERGENCE  (truncation artifact vs structural split)")
print("=" * 78)
print("\nInput pins (first 20 lines of stdout):")
pin_hashes = {}
for name, path in INPUT_PINS.items():
    h = _sha256_file(path)
    pin_hashes[name] = h
    rel = str(path).replace(str(SCRIPT_DIR) + os.sep, '')
    print(f"  {name:22s} = {rel:45s}  sha256={h[:16]}...")

# ==============================================================================
# Section 2. GPU device confirmation (first 20 lines)
# ==============================================================================
import torch
print("\nGPU device:")
if torch.cuda.is_available():
    dev = torch.device('cuda')
    name = torch.cuda.get_device_name(0)
    vram_gib = torch.cuda.get_device_properties(0).total_memory / 1024**3
    print(f"  torch version    : {torch.__version__}")
    print(f"  device           : cuda ({name})")
    print(f"  VRAM total       : {vram_gib:.3f} GiB  (target <17 GiB)")
    GPU_AVAILABLE = True  # (local)
else:
    dev = torch.device('cpu')
    print(f"  torch version    : {torch.__version__}")
    print(f"  device           : CPU fallback (GPU NOT visible)")
    GPU_AVAILABLE = False  # (local)

# ==============================================================================
# Section 3. Load S83 baselines (Josephson sector, GGE bare, calibration)
# ==============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Load S83/S58/S57 baselines (R-independent Josephson + GGE bare)")
print("=" * 78)

s57c = np.load(INPUT_PINS["S57_cc_sign"], allow_pickle=True)
s58v = np.load(INPUT_PINS["S58_volovik"], allow_pickle=True)
s83g51 = np.load(INPUT_PINS["S83_W3_G51"], allow_pickle=True)

Lambda_eff      = float(s57c['Lambda_eff_MKK'])    # (local) 1.709 M_KK, bare rho_GGE
w_GGE_bare      = float(s57c['w_GGE'])             # (local) -0.408
P_GGE_bare      = float(s57c['P_vac_GGE'])         # (local) -0.688
E_GGE_bare      = float(s57c['E_GGE'])             # (local) 1.688 M_KK

F_Josephson     = float(s58v['F_Josephson'])       # (local) -336.641 M_KK
rho_J_per_cell  = abs(F_Josephson) / N_cells       # (local) 10.520 M_KK/cell

# S83 G51 L=5 baseline for cross-check
w_0_zeta_L5_ref    = float(s83g51['w_0_zeta'])       # (local) -0.9180875 (should match S58)
w_0_Zubarev_L5_ref = float(s83g51['w_0_Zubarev'])    # (local) -0.918 (canonical)
S_zeta_L5_ref      = float(s83g51['S_zeta'])         # (local) 159936
S_Zubarev_L5_ref   = float(s83g51['S_Zubarev'])      # (local) 3805.668
S_zeta_E_L5_ref    = float(s83g51['S_zeta_E'])       # (local) energy-wtd
S_Zubarev_E_L5_ref = float(s83g51['S_Zubarev_E'])    # (local) energy-wtd

print(f"\n  From S57 (GGE bare, regulator-independent reference):")
print(f"    Lambda_eff (rho_GGE bare)      = {Lambda_eff:.6f} M_KK")
print(f"    P_GGE_bare                     = {P_GGE_bare:.6f} M_KK")
print(f"    w_GGE_bare = P_GGE/rho_GGE     = {w_GGE_bare:.6f}")
print(f"\n  From S58 (Josephson sector, R-independent topological invariant):")
print(f"    F_Josephson                    = {F_Josephson:.3f} M_KK")
print(f"    rho_J/cell = |F_J|/N_cells     = {rho_J_per_cell:.6f} M_KK/cell")
print(f"\n  From S83 W3-G51 L=5 canonical (for cross-check at L=5 below):")
print(f"    w_0^zeta(L=5)    (S83 ref)     = {w_0_zeta_L5_ref:.6f}")
print(f"    w_0^Zubarev(L=5) (S83 ref)     = {w_0_Zubarev_L5_ref:.6f}")
print(f"    S_zeta(L=5)      (S83 ref)     = {S_zeta_L5_ref:.3f}")
print(f"    S_Zubarev(L=5)   (S83 ref)     = {S_Zubarev_L5_ref:.3f}")

# ==============================================================================
# Section 4. Load L=9 per-sector spectrum cache + sector-filter machinery
# ==============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Load L=9 spectrum cache, build per-L_max flat arrays")
print("=" * 78)

cache = np.load(INPUT_PINS["spectrum_cache"], allow_pickle=True)
sec = cache['sector_evals'].item()
print(f"\n  Cache sectors loaded : {len(sec)} SU(3) irreps (p,q), p+q in [0, 9]")

def flatten_L(sector_dict, Lmax):
    """Flatten per-sector abs_evals into (flat_lams, flat_mults) for L=p+q <= Lmax.
    Per-sector multiplicity = d(p,q) = (p+1)*(q+1)*(p+q+2)/2 (SU(3) irrep dim).
    """
    lam_list = []  # (local)
    mult_list = []  # (local)
    n_sectors = 0  # (local)
    for (p, q), rec in sector_dict.items():
        if (p + q) > Lmax:
            continue
        n_sectors += 1
        d_pq = (p + 1) * (q + 1) * (p + q + 2) // 2  # (local) SU(3) irrep dim
        ae = rec['abs_evals']
        lam_list.append(np.asarray(ae, dtype=np.float64))
        mult_list.append(np.full(len(ae), d_pq, dtype=np.float64))
    flat_lam  = np.concatenate(lam_list)   # (local)
    flat_mult = np.concatenate(mult_list)  # (local)
    return flat_lam, flat_mult, n_sectors

L_max_grid = [5, 7, 9]  # (local)
spec_by_L = {}  # (local) L -> dict of spectrum + sums
for Lmax in L_max_grid:
    flat_lam, flat_mult, n_sec = flatten_L(sec, Lmax)

    # --- GPU weighted sums ---
    # No eigendecomposition required: this is a reduction over
    # ~6k-45k scalars. GPU path reduces dispatch contention with other agents.
    lam_t = torch.tensor(flat_lam, dtype=torch.float64, device=dev)   # (local)
    mult_t = torch.tensor(flat_mult, dtype=torch.float64, device=dev) # (local)
    w_zeta_t     = torch.ones_like(lam_t)                             # (local)
    w_zubarev_t  = torch.exp(-lam_t ** 2)                             # (local) Lambda_Z = 1.0 M_KK

    # Count-weighted sums (normalization)
    S_zeta_L     = (mult_t * w_zeta_t).sum().item()                   # (local)
    S_Zubarev_L  = (mult_t * w_zubarev_t).sum().item()                # (local)
    # Energy-weighted sums (eps ~ lam model, matches S83 G51)
    S_zeta_E_L    = (mult_t * w_zeta_t * lam_t).sum().item()          # (local)
    S_Zubarev_E_L = (mult_t * w_zubarev_t * lam_t).sum().item()       # (local)

    xi_count_L = S_Zubarev_L / S_zeta_L          # (local)
    xi_E_L     = S_Zubarev_E_L / S_zeta_E_L      # (local)

    spec_by_L[Lmax] = dict(
        n_sectors=n_sec,
        n_modes_flat=len(flat_lam),
        S_zeta=S_zeta_L,
        S_Zubarev=S_Zubarev_L,
        S_zeta_E=S_zeta_E_L,
        S_Zubarev_E=S_Zubarev_E_L,
        xi_count=xi_count_L,
        xi_E=xi_E_L,
    )
    print(f"\n  L_max = {Lmax}:")
    print(f"    sectors={n_sec:3d}  n_modes_flat={len(flat_lam):6d}  "
          f"S_zeta={S_zeta_L:.3f}  S_Zubarev={S_Zubarev_L:.3f}")
    print(f"    S_zeta_E={S_zeta_E_L:.3f}  S_Zubarev_E={S_Zubarev_E_L:.3f}  "
          f"xi_count={xi_count_L:.6f}  xi_E={xi_E_L:.6f}")

# Cross-check L=5 against S83 W3-G51 reference
err_S_zeta_L5    = abs(spec_by_L[5]['S_zeta']    - S_zeta_L5_ref)     # (local)
err_S_Zubarev_L5 = abs(spec_by_L[5]['S_Zubarev'] - S_Zubarev_L5_ref)  # (local)
err_S_zeta_E_L5  = abs(spec_by_L[5]['S_zeta_E']  - S_zeta_E_L5_ref)   # (local)
print(f"\n  [VERIFY] L=5 reproduces S83 W3-G51:")
print(f"    dS_zeta    = {err_S_zeta_L5:.6e}")
print(f"    dS_Zubarev = {err_S_Zubarev_L5:.6e}")
print(f"    dS_zeta_E  = {err_S_zeta_E_L5:.6e}")
assert err_S_zeta_L5    < 1e-3,  "L=5 S_zeta    mismatch vs S83 W3-G51"
assert err_S_Zubarev_L5 < 1e-3,  "L=5 S_Zubarev mismatch vs S83 W3-G51"

# ==============================================================================
# Section 5. Per-L_max w_0 under zeta and Zubarev (S83 energy-weighted model)
# ==============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Compute w_0^{zeta}(L) and w_0^{Zubarev}(L) for L in {5,7,9}")
print("=" * 78)

# Josephson sector: R- and L-independent (topological)
rho_J = rho_J_per_cell     # (local)
P_J   = -rho_J_per_cell    # (local) w_J = -1

# Calibrate GGE normalization so that rho_GGE^{zeta}(L=5) = Lambda_eff (S57 value).
# This is the same calibration used in S83 W3-G51 Section 4(iii).
norm_GGE = Lambda_eff / spec_by_L[5]['S_zeta_E']  # (local) calibrate at L=5

w0_by_L = {}  # (local)
for Lmax in L_max_grid:
    d = spec_by_L[Lmax]

    # GGE energy density at this L_max in each regulator scheme
    rho_GGE_zeta_L    = norm_GGE * d['S_zeta_E']        # (local)
    rho_GGE_Zubarev_L = norm_GGE * d['S_Zubarev_E']     # (local)

    # GGE pressure (w_GGE ~ invariant across R at leading order, per S83)
    P_GGE_zeta_L    = w_GGE_bare * rho_GGE_zeta_L       # (local)
    P_GGE_Zubarev_L = w_GGE_bare * rho_GGE_Zubarev_L    # (local)

    # Combined w_0 = (P_J + P_GGE) / (rho_J + rho_GGE)
    w_0_zeta_L    = (P_J + P_GGE_zeta_L)    / (rho_J + rho_GGE_zeta_L)     # (local)
    w_0_Zubarev_L = (P_J + P_GGE_Zubarev_L) / (rho_J + rho_GGE_Zubarev_L)  # (local)

    split_L = w_0_zeta_L - w_0_Zubarev_L    # (local) scheme-split

    w0_by_L[Lmax] = dict(
        rho_GGE_zeta=rho_GGE_zeta_L,
        rho_GGE_Zubarev=rho_GGE_Zubarev_L,
        P_GGE_zeta=P_GGE_zeta_L,
        P_GGE_Zubarev=P_GGE_Zubarev_L,
        w_0_zeta=w_0_zeta_L,
        w_0_Zubarev=w_0_Zubarev_L,
        split=split_L,
    )
    print(f"\n  L_max = {Lmax}:")
    print(f"    rho_GGE^zeta    = {rho_GGE_zeta_L:.6f}   rho_GGE^Zubarev = {rho_GGE_Zubarev_L:.6f}")
    print(f"    w_0^zeta        = {w_0_zeta_L:.6f}")
    print(f"    w_0^Zubarev     = {w_0_Zubarev_L:.6f}")
    print(f"    split           = {split_L:+.6f}   (zeta - Zubarev)")

# ==============================================================================
# Section 6. Substitution chain: direction analysis from computed numerics
# ==============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Substitution chain [VERIFY] — direction from numerics")
print("=" * 78)

split_5 = w0_by_L[5]['split']   # (local)
split_7 = w0_by_L[7]['split']   # (local)
split_9 = w0_by_L[9]['split']   # (local)

# Substitution chain (printed with actual numbers; the direction is READ OFF
# the computed |split(L=9)| vs |split(L=5)|, NOT asserted a priori.)
print(f"\n  SUBSTITUTION CHAIN (L_max scheme-split direction):")
print(f"  ")
print(f"  Step 1 (definitions):")
print(f"    scheme-split(L) := w_0^zeta(L) - w_0^Zubarev(L)")
print(f"  ")
print(f"  Step 2 (substitution from computed numerics):")
print(f"    split(L=5) = {w0_by_L[5]['w_0_zeta']:+.6f} - ({w0_by_L[5]['w_0_Zubarev']:+.6f}) = {split_5:+.6f}")
print(f"    split(L=7) = {w0_by_L[7]['w_0_zeta']:+.6f} - ({w0_by_L[7]['w_0_Zubarev']:+.6f}) = {split_7:+.6f}")
print(f"    split(L=9) = {w0_by_L[9]['w_0_zeta']:+.6f} - ({w0_by_L[9]['w_0_Zubarev']:+.6f}) = {split_9:+.6f}")
print(f"  ")
print(f"  Step 3 (simplified magnitudes):")
print(f"    |split(L=5)| = {abs(split_5):.6f}")
print(f"    |split(L=7)| = {abs(split_7):.6f}")
print(f"    |split(L=9)| = {abs(split_9):.6f}")

# Direction determination — numeric comparison only
if abs(split_9) < abs(split_5) and abs(split_7) <= abs(split_5):
    direction = "SHRINKS (monotonic -> truncation artifact)"  # (local)
    structural = False  # (local)
elif abs(split_9) > abs(split_5):
    direction = "GROWS (-> structural scheme-split)"  # (local)
    structural = True  # (local)
else:
    direction = "NON-MONOTONIC (oscillates)"  # (local)
    structural = None  # (local)

print(f"  ")
print(f"  Step 4 (direction read off):")
print(f"    sign of |split(9)| - |split(5)| = {np.sign(abs(split_9) - abs(split_5)):+.0f}")
print(f"    monotone in L      : {'yes' if abs(split_5) >= abs(split_7) >= abs(split_9) or abs(split_5) <= abs(split_7) <= abs(split_9) else 'no'}")
print(f"    direction          : {direction}")

# Zubarev convergence criterion (canonical -0.918 stability)
dw0_Zub_9_5 = abs(w0_by_L[9]['w_0_Zubarev'] - w0_by_L[5]['w_0_Zubarev'])  # (local)
dw0_Zub_from_ref = abs(w0_by_L[9]['w_0_Zubarev'] - (-0.918))              # (local)
print(f"\n  Zubarev convergence test:")
print(f"    |w_0^Zubarev(L=9) - w_0^Zubarev(L=5)| = {dw0_Zub_9_5:.6f}   (threshold: < 0.005)")
print(f"    |w_0^Zubarev(L=9) - (-0.918)|         = {dw0_Zub_from_ref:.6f}   (threshold: < 0.020)")

# ==============================================================================
# Section 7. Gate verdict
# ==============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Gate verdict")
print("=" * 78)

PASS_tol_conv  = 0.005  # (local) gate |w_0^Z(L=9)-w_0^Z(L=5)| threshold
INFO_tol_conv  = 0.020  # (local) distance to -0.918 reference
PASS_tol_ref   = 0.020  # (local)

# PASS conditions (both must hold):
conv_pass = (dw0_Zub_9_5 < PASS_tol_conv)     # (local) convergence
ref_pass  = (dw0_Zub_from_ref < PASS_tol_ref) # (local) on -0.918 band

if conv_pass and ref_pass:
    verdict_tag = "PASS"
    verdict_reason = (
        f"|w_0^Z(9)-w_0^Z(5)|={dw0_Zub_9_5:.6f}<0.005 AND "
        f"|w_0^Z(9)+0.918|={dw0_Zub_from_ref:.6f}<0.020"
    )
elif structural is True:
    verdict_tag = "FAIL"
    verdict_reason = (
        f"scheme-split GROWS with L_max ({abs(split_5):.3f}->{abs(split_9):.3f}): structural"
    )
elif structural is None:
    verdict_tag = "FAIL"
    verdict_reason = f"scheme-split OSCILLATES with L_max ({abs(split_5):.3f},{abs(split_7):.3f},{abs(split_9):.3f})"
else:
    # structural is False (shrinks with L) but convergence criterion not met
    verdict_tag = "INFO"
    verdict_reason = (
        f"scheme-split SHRINKS ({abs(split_5):.3f}->{abs(split_9):.3f}) but "
        f"|w_0^Z(9)-w_0^Z(5)|={dw0_Zub_9_5:.6f} (ref_pass={ref_pass})"
    )

print(f"\n  VERDICT: {verdict_tag}")
print(f"  Reason:  {verdict_reason}")
print(f"  Interpretation:")
if structural is False:
    print(f"    The scheme-split between zeta and Zubarev SHRINKS monotonically with L_max.")
    print(f"    This is the signature of a FINITE-SPECTRUM ARTIFACT: at L_max=5 the two")
    print(f"    regulators probe different truncated spectra, but as L_max grows the")
    print(f"    reweighting influence of UV modes diminishes (acoustic density of states")
    print(f"    squeezes the Zubarev Gaussian suppression into a smaller relative region).")
    print(f"    The canonical w_0 = -0.918 therefore stands as the L-stable prediction.")
elif structural is True:
    print(f"    The scheme-split GROWS with L_max, indicating the two regulators compute")
    print(f"    GENUINELY DIFFERENT substrate functionals. This reopens the Volovik-")
    print(f"    partition regulator choice as a structural question; the S83-G51 FAIL")
    print(f"    cannot be dismissed as a truncation artifact.")
else:
    print(f"    Non-monotonic behavior — sensitivity probe needed (L=6, L=8 interior).")

# ==============================================================================
# Section 8. Plot
# ==============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Plot results")
print("=" * 78)

Ls_arr      = np.array(L_max_grid, dtype=np.float64)                                   # (local)
w0_zeta_arr = np.array([w0_by_L[L]['w_0_zeta']     for L in L_max_grid])              # (local)
w0_Zub_arr  = np.array([w0_by_L[L]['w_0_Zubarev']  for L in L_max_grid])              # (local)
split_arr   = np.array([w0_by_L[L]['split']         for L in L_max_grid])             # (local)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: w_0 vs L_max by regulator
ax1.plot(Ls_arr, w0_zeta_arr, 'o-', color='tab:gray',  label='w_0^zeta  (unregulated ref)', markersize=10)
ax1.plot(Ls_arr, w0_Zub_arr,  'o-', color='tab:blue',  label='w_0^Zubarev (canonical R)', markersize=10)
ax1.axhline(-0.918, color='k', linestyle='--', alpha=0.6, label='w_0 = -0.918 (S58/S83 canonical)')
ax1.axhline(-1.0,   color='r', linestyle=':', alpha=0.5, label='w_0 = -1 (LCDM)')
ax1.axhspan(-0.918 - 0.02, -0.918 + 0.02, alpha=0.15, color='green', label='PASS band (+/- 0.02)')
for L, wz, wZ in zip(Ls_arr, w0_zeta_arr, w0_Zub_arr):
    ax1.annotate(f'{wz:.4f}', (L, wz), textcoords='offset points', xytext=(8, 0), fontsize=9, color='tab:gray')
    ax1.annotate(f'{wZ:.4f}', (L, wZ), textcoords='offset points', xytext=(8, 0), fontsize=9, color='tab:blue')
ax1.set_xlabel('L_max (spectral truncation)')
ax1.set_ylabel('w_0')
ax1.set_title(f'w_0 vs L_max under two regulators\n(verdict: {verdict_tag})')
ax1.set_xticks(L_max_grid)
ax1.legend(loc='best', fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: scheme-split magnitude vs L_max
ax2.plot(Ls_arr, np.abs(split_arr), 'o-', color='tab:red', markersize=12, linewidth=2.0,
         label='|w_0^zeta - w_0^Zubarev|')
for L, s in zip(Ls_arr, split_arr):
    ax2.annotate(f'{abs(s):.4f}', (L, abs(s)), textcoords='offset points', xytext=(8, 5), fontsize=10)
ax2.axhline(0.005, color='green', linestyle='--', alpha=0.6, label='PASS threshold (0.005)')
ax2.axhline(0.020, color='orange', linestyle='--', alpha=0.6, label='INFO band (0.020)')
ax2.set_xlabel('L_max')
ax2.set_ylabel('|scheme-split|')
ax2.set_title(f'Scheme-split vs L_max\n(direction: {direction})')
ax2.set_xticks(L_max_grid)
ax2.set_yscale('log')
ax2.legend(loc='best', fontsize=9)
ax2.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plot_path = SCRIPT_DIR / "s84_w4_g51_lmax_convergence.png"
plt.savefig(plot_path, dpi=120, bbox_inches='tight')
plt.close()
print(f"\n  Plot saved: {plot_path}")

# ==============================================================================
# Section 9. SHA-256 closure + save NPZ
# ==============================================================================
print("\n" + "=" * 78)
print("SECTION 9: SHA-256 closure + save")
print("=" * 78)

pin_map_ordered = json.dumps(pin_hashes, sort_keys=True).encode('utf-8')
content_sha = hashlib.sha256(pin_map_ordered).hexdigest()

# Audit SHA: hash of the computed values
audit_payload = json.dumps({
    'verdict': verdict_tag,
    'direction': direction,
    'structural': structural,
    'L_max_grid': L_max_grid,
    'w_0_zeta':    [w0_by_L[L]['w_0_zeta']    for L in L_max_grid],
    'w_0_Zubarev': [w0_by_L[L]['w_0_Zubarev'] for L in L_max_grid],
    'split':       [w0_by_L[L]['split']       for L in L_max_grid],
    'dw0_Zub_9_5': dw0_Zub_9_5,
    'dw0_Zub_from_ref': dw0_Zub_from_ref,
    'gpu_device': str(dev),
    'gpu_available': GPU_AVAILABLE,
}, sort_keys=True).encode('utf-8')
audit_sha = hashlib.sha256(audit_payload).hexdigest()

print(f"\n  content_sha = {content_sha}")
print(f"  audit_sha   = {audit_sha}")

out_npz = SCRIPT_DIR / "s84_w4_g51_lmax_convergence.npz"
np.savez(out_npz,
    L_max_grid=np.array(L_max_grid),
    w_0_zeta=w0_zeta_arr,
    w_0_Zubarev=w0_Zub_arr,
    split=split_arr,
    dw0_Zub_9_5=dw0_Zub_9_5,
    dw0_Zub_from_ref=dw0_Zub_from_ref,
    # Per-L spectrum sums
    S_zeta=np.array([spec_by_L[L]['S_zeta'] for L in L_max_grid]),
    S_Zubarev=np.array([spec_by_L[L]['S_Zubarev'] for L in L_max_grid]),
    S_zeta_E=np.array([spec_by_L[L]['S_zeta_E'] for L in L_max_grid]),
    S_Zubarev_E=np.array([spec_by_L[L]['S_Zubarev_E'] for L in L_max_grid]),
    xi_count=np.array([spec_by_L[L]['xi_count'] for L in L_max_grid]),
    xi_E=np.array([spec_by_L[L]['xi_E'] for L in L_max_grid]),
    n_sectors=np.array([spec_by_L[L]['n_sectors'] for L in L_max_grid]),
    n_modes_flat=np.array([spec_by_L[L]['n_modes_flat'] for L in L_max_grid]),
    # Calibration
    rho_J_per_cell=rho_J_per_cell,
    Lambda_eff=Lambda_eff,
    w_GGE_bare=w_GGE_bare,
    norm_GGE=norm_GGE,
    # Verdict
    verdict=verdict_tag,
    direction=direction,
    structural=(1 if structural is True else (0 if structural is False else -1)),
    reason=verdict_reason,
    content_sha=content_sha,
    audit_sha=audit_sha,
    pin_hashes=json.dumps(pin_hashes),
    gpu_device=str(dev),
    gpu_available=GPU_AVAILABLE,
)
print(f"  NPZ saved: {out_npz}")

# ==============================================================================
# Section 10. Final 4-tuple + verdict line
# ==============================================================================
print("\n" + "=" * 78)
print("FINAL RESULT")
print("=" * 78)
print(f"\n  L_max table (L, w_0^zeta, w_0^Zubarev, split):")
print(f"  {'L_max':>6s} | {'w_0^zeta':>12s} | {'w_0^Zubarev':>14s} | {'split':>12s}")
print(f"  {'-'*6} | {'-'*12} | {'-'*14} | {'-'*12}")
for L in L_max_grid:
    d = w0_by_L[L]
    print(f"  {L:>6d} | {d['w_0_zeta']:>+12.6f} | {d['w_0_Zubarev']:>+14.6f} | {d['split']:>+12.6f}")

# 4-tuple in the S84 canonical form
four_tuple_value = dw0_Zub_9_5  # (local) the gate's primary number
four_tuple = (
    f"value={four_tuple_value:.6f} "
    f"scheme=Zubarev-E-weighted "
    f"convention=substrate-native-L-convergence "
    f"L_max=scan{{5,7,9}}"
)
print(f"\n  4-tuple: ({four_tuple})")

verdict_line = (
    f"S84-G51-LMAX-CONVERGENCE: {verdict_tag} -- "
    f"value={four_tuple_value:.6f} scheme=Zubarev-E-weighted "
    f"convention=substrate-native-L-convergence L_max=scan{{5,7,9}} "
    f"content_sha256={content_sha} audit_sha256={audit_sha}"
)
print(f"\n  VERDICT LINE:")
print(f"  {verdict_line}")

# Append to verdict file
verdict_file = SCRIPT_DIR / "s84_gate_verdicts.txt"
with open(verdict_file, 'a', encoding='utf-8') as f:
    f.write(verdict_line + "\n")
print(f"\n  Appended to: {verdict_file}")

print("\n" + "=" * 78)
print("DONE.")
print("=" * 78)
