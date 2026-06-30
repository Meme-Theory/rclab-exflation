#!/usr/bin/env python3
"""
S84 Wave 2a Gate W2a-14 -- S84-L1-L2-PROJECTION
================================================

Project 11 framework-target observables onto L1 (zeta-canonical) and
L2 (Zubarev-canonical) at L_max = 5, tau = tau_fold = 0.19. Classify
each observable's |split| = |Q_L1 - Q_L2|/|Q_L1| as DIAGNOSTIC,
INTERMEDIATE, or DEGENERATE.

Substrate framing (mandatory): L1 and L2 are NOT two coordinate systems
for the same observable. They are two distinct strata of the substrate's
self-determination evaluated at the same fold. The split exposes whether
L3 (action-tier) freedom is non-trivial; a small split says the substrate
hides the gap at observable scale, a large split says the substrate
exposes it. Direction:
    D_K spectrum (substrate fact)
        -> L1 canonical-measure stratum / L2 action-minimum stratum
            -> spectral moments a_0, a_2, a_3, a_4
                -> per-observable Q_L1, Q_L2
                    -> split classification

Substitution chain (full per-observable derivations are documented inline
at each Q evaluation; see also the working-paper section §W2-14).

PASS/FAIL/INFO thresholds (pre-registered, plan §W2a-14 §9):
    PASS: n_diagnostic >= 3 AND n_degenerate <= 2.
    FAIL: n_degenerate >= 9 OR n_diagnostic = 0 (all 11 degenerate)
            OR n_diagnostic >= 10 with no inheritance structure (CC1 broken).
    INFO: borderline (n_diagnostic = 2 OR n_degenerate = 3).

Anchors (input pin SHAs):
    W1-G1 Zubarev anchor SHA 227a591307...c96dcdd (L2)
    W1-G3 zeta anchor SHA   2343920a4c...8c99ab5 (L1)
    G46 tensor transfer r=0.011732 SHA e6926a04...95df7765
    G51 w_0 -0.998 SHA       224b7b56...43768d07
    S82 A_s 3.30e-9 SHA       25c3643f...c2fdbaea
    S82 mu 4.98e-10 SHA       dea8a6c7...26b7ed
    canonical_constants SHA computed-at-runtime
    spectrum cache SHA       computed-at-runtime
"""

import os
# CPU fallback: cap threads BEFORE numpy import (GPU used for aggregation)
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
    M_KK, tau_fold, Delta_BCS, m_H_obs, v_ew,
    alpha_s_MZ_obs, w0_FW, planck_ns, PI,
)

np.random.seed(84)

# =============================================================================
# Section 1. Input pin map + SHA-256 closure helper
# =============================================================================

def _sha256_file(path):
    """Return SHA-256 hexdigest of file bytes, or 'FILE_MISSING' if absent."""
    if not Path(path).exists():
        return "FILE_MISSING"
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

INPUT_PINS = {
    "spectrum_cache":  SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz",
    "canonical_const": SCRIPT_DIR / "canonical_constants.py",
    "self_script":     SCRIPT_DIR / "s84_w2a_l1_l2_projection.py",
    # Anchor verdict SHAs (from S83 / S82 verdict files)
    "anchor_W1_G1_sha":  "227a591307f88d2cfdb1c505c6ab4a040f873db4656116c5948ae7ba3c96dcdd",
    "anchor_W1_G3_sha":  "2343920a4c2a807a26bb9740ad6ede1c9d3465bb722d548dbefa978578c99ab5",
    "anchor_G46_sha":    "e6926a04356c97424dad1f7e95420d31aa9eac8b3caa8afb5f8674395df1c765",
    "anchor_G51_sha":    "224b7b5648f5fdf2dfe2f0ff6c1733dfcdb260d2d5515dbc9307fcee43768d07",
    "anchor_S82_AS_sha": "25c3643f7c0c2e949d3d7617957a3cb384e443ba313ec1df359fab1bc2fdbaea",
    "anchor_S82_FIRAS_sha": "dea8a6c73b961acb72ce9122b7306226aadd9d6b319e3b904e1956d68026b7ed",
}

print("=" * 78)
print("S84 W2a-14 -- L1-L2-PROJECTION (zeta vs Zubarev, 11 observables, L_max=5)")
print("=" * 78)
print("\nInput pins:")
pin_hashes = {}
for name, val in INPUT_PINS.items():
    if isinstance(val, Path):
        h = _sha256_file(val)
    else:
        h = val  # already a SHA string
    pin_hashes[name] = h
    print(f"  {name:24s}  sha256={h[:16]}...")

print(f"\nCanonical inputs (from canonical_constants.py):")
print(f"  M_KK             = {M_KK:.6e}")
print(f"  tau_fold         = {tau_fold}")
print(f"  Delta_BCS        = {Delta_BCS:.6f}  (M_KK units)")
print(f"  m_H_obs          = {m_H_obs}  GeV (PDG anchor)")
print(f"  v_ew             = {v_ew}    GeV")
print(f"  w0_FW            = {w0_FW}   (framework w_0)")
print(f"  alpha_s_MZ_obs   = {alpha_s_MZ_obs}")
print(f"  planck_ns        = {planck_ns}")

# =============================================================================
# Section 2. Load D_K spectrum at tau_fold, filter to L_max = 5
# =============================================================================

L_MAX = 5                              # (local) pre-registered truncation
KO_DIM = 6                             # (local) Connes KO-dim of M^4 x SU(3)

cache = np.load(INPUT_PINS["spectrum_cache"], allow_pickle=True)
sector_evals = cache['sector_evals'].item()

filtered_sectors = {}                  # (local)
flat_lambdas = []                      # (local)
flat_mults = []                        # (local)
for (p, q), info in sector_evals.items():
    lev = info['level']
    if lev > L_MAX:
        continue
    dim = info['dim']
    evals = np.asarray(info['abs_evals'])
    filtered_sectors[(p, q)] = {'dim': dim, 'evals': evals, 'level': lev}
    for lam in evals:
        flat_lambdas.append(float(lam))
        flat_mults.append(int(dim))

flat_lambdas = np.asarray(flat_lambdas, dtype=np.float64)  # (local)
flat_mults   = np.asarray(flat_mults,   dtype=np.float64)  # (local)

N_sectors_kept = len(filtered_sectors)                      # (local)
N_modes_mult = float(flat_mults.sum())                      # (local) sum d_k * n_k
N_flat = flat_lambdas.size                                  # (local) flat sector-list length

print(f"\n[L_MAX={L_MAX}] sector filter (level = p+q <= {L_MAX}):")
print(f"  num sectors kept           = {N_sectors_kept}")
print(f"  num flat eigenvalue rows   = {N_flat}")
print(f"  sum(d_k * n_k) [mult-wtd]  = {int(N_modes_mult)}")
print(f"  lambda range               = [{flat_lambdas.min():.4f}, {flat_lambdas.max():.4f}]")

# =============================================================================
# Section 3. L1 and L2 weight functions
# =============================================================================
# L1 = zeta-canonical: Connes-Moscovici zeta_D(s=0); literal counting.
# L2 = Zubarev-canonical: heat-kernel mollifier with Lambda_Z = M_KK.
# In M_KK units, Lambda_Z = 1.

def w_L1(lam):
    """L1 zeta weight: w(lambda) = 1 (literal mode count)."""
    return np.ones_like(lam, dtype=np.float64)

def w_L2(lam, Lambda_Z=1.0):
    """L2 Zubarev weight: exp(-lambda^2 / Lambda_Z^2)."""
    return np.exp(-(lam / Lambda_Z) ** 2)

# =============================================================================
# Section 4. Spectral moments under L1 and L2
# =============================================================================
# a_n_R = sum_n d_k * w_R(lambda_n) * lambda_n^n
# n = 0, 2, 3, 4 are needed for the 11 observables.

# GPU aggregation path
GPU_USED = False                       # (local) flag for diagnostic print
try:
    import torch
    if torch.cuda.is_available():
        device = 'cuda'
        t_lam  = torch.tensor(flat_lambdas, device=device, dtype=torch.float64)
        t_mult = torch.tensor(flat_mults,   device=device, dtype=torch.float64)

        def moment_gpu(weights_np, n_pow):
            """Compute sum d_k * w(lambda) * lambda^n via GPU."""
            t_w = torch.tensor(weights_np, device=device, dtype=torch.float64)
            t_pow = t_lam ** n_pow
            return float((t_mult * t_w * t_pow).sum().cpu().item())

        def moment(w_fn, n_pow):
            return moment_gpu(w_fn(flat_lambdas), n_pow)

        GPU_USED = True
        print(f"\n[GPU]: torch.cuda available ({torch.cuda.get_device_name(0)}), "
              f"using GPU for spectral-moment aggregation.")
    else:
        raise RuntimeError("no cuda")
except Exception as e:
    print(f"\n[CPU fallback]: {e}")
    def moment(w_fn, n_pow):
        w = w_fn(flat_lambdas)
        return float((flat_mults * w * (flat_lambdas ** n_pow)).sum())

# Compute a_0, a_2, a_3, a_4 under L1 and L2
a0_L1 = moment(w_L1, 0)
a2_L1 = moment(w_L1, 2)
a3_L1 = moment(w_L1, 3)
a4_L1 = moment(w_L1, 4)

a0_L2 = moment(w_L2, 0)
a2_L2 = moment(w_L2, 2)
a3_L2 = moment(w_L2, 3)
a4_L2 = moment(w_L2, 4)

# Cross-check: L1 a_0 must equal sum d_k = N_modes_mult exactly
assert abs(a0_L1 - N_modes_mult) < 1e-6, "L1 a_0 must equal mult-weighted mode count"

print(f"\nSpectral moments at tau = tau_fold = {tau_fold}, L_max = {L_MAX}:")
print(f"  L1 (zeta, w=1):       a_0 = {a0_L1:.6e}  a_2 = {a2_L1:.6e}  "
      f"a_3 = {a3_L1:.6e}  a_4 = {a4_L1:.6e}")
print(f"  L2 (Zubarev, w=exp):  a_0 = {a0_L2:.6e}  a_2 = {a2_L2:.6e}  "
      f"a_3 = {a3_L2:.6e}  a_4 = {a4_L2:.6e}")

# =============================================================================
# Section 5. Per-observable Q_L1 and Q_L2 evaluation
# =============================================================================
# Each observable is computed under both regulators using the relevant
# spectral moments. The substitution chain for each is documented inline.

# Anchor values (from prior verdicts) — used for normalization where the
# absolute scale enters as a calibration constant in front of the spectral ratio.
ANCHOR = {
    'A_s_L2':       3.30e-9,           # S82-UNIFIED-AS-79-FULL-A
    'm_H_L2':       m_H_obs,           # PDG anchor (regulator-universal a_2)
    'n_s_L2':       0.9561,            # framework value (S50-51)
    'alpha_s_L2':   0.9561**2 - 1.0,   # alpha_s = n_s^2 - 1 identity
    'mu_L2':        4.98e-10,          # S82-FIRAS-CHLUBA-FULL
    'r_L2':         0.0117,            # S83-G46
    'f_NL_L2':      1.0,               # framework O(1) at SKA-2 threshold
    'w_0_L2':       -0.998,            # S83-G51 primary
    'sigma_8_L2':   0.811,             # framework target (Planck-anchored)
    'H_0_L2':       67.4,              # km/s/Mpc, framework target
    'Omega_GW_L2':  1.0e-30,           # at LISA band, ~29.6 OOM below LISA threshold
}

observables = []  # (local) list of (name, Q_L1, Q_L2, split, classification, chain)

# -----------------------------------------------------------------------------
# (1) A_s -- primordial scalar amplitude
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. A_s ∝ H_tilde^2 / eps_H * (1/M_Pl^2).
#   Step 2. H_tilde^2 ∝ a_2 (Einstein-Hilbert moment, gravity sector).
#   Step 3. eps_H, M_Pl are layer-independent slow-roll parameters
#           (set by Mukhanov mode equation IC, regulator-blind ratios).
#   Step 4. Ratio: A_s_L1 / A_s_L2 = (H_tilde_L1 / H_tilde_L2)^2
#                                  = a_2_L1 / a_2_L2 (both H_tilde^2 scale a_2).
#   Step 5. Anchor: A_s_L2 = 3.30e-9 (S82). A_s_L1 = A_s_L2 * (a_2_L1/a_2_L2).
A_s_L2 = ANCHOR['A_s_L2']
A_s_L1 = A_s_L2 * (a2_L1 / a2_L2)
split_A_s = abs(A_s_L1 - A_s_L2) / abs(A_s_L1)  # (local)
chain_A_s = (
    "A_s ∝ H_tilde^2/eps_H * (1/M_Pl^2); H_tilde^2 ∝ a_2 (Einstein-Hilbert); "
    f"A_s_L1/A_s_L2 = a_2_L1/a_2_L2 = {a2_L1:.3e}/{a2_L2:.3e} "
    f"= {a2_L1/a2_L2:.4f}; with A_s_L2 = {A_s_L2:.3e} -> A_s_L1 = {A_s_L1:.3e}; "
    f"|split| = {split_A_s:.4f}."
)
observables.append(('A_s', A_s_L1, A_s_L2, split_A_s, '', chain_A_s))

# -----------------------------------------------------------------------------
# (2) m_H -- Higgs mass at M_Z
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. m_H^2 ∝ a_2 in NCG spectral action (Connes-Chamseddine 2007 §3).
#   Step 2. Connes-Chamseddine 2007 Thm 3.1: a_2 is regulator-universal at
#           leading order f_2; differs only at SUBLEADING f_4 corrections.
#   Step 3. Ratio: m_H_L1 / m_H_L2 = sqrt(a_2_L1 / a_2_L2). The leading
#           universal term cancels — but we measure the FULL ratio here
#           (no separate subtraction available without re-deriving the
#           full f_2/f_4 NCG expansion). We record the FULL spectral ratio
#           and flag the universality fact in the chain.
#   Step 4. Expected NEAR-DEGENERATE per CC4 (Connes-Chamseddine universality
#           of the leading a_2 piece). Our "raw" m_H ratio includes the
#           non-universal correction; if this is also small, m_H is degenerate.
m_H_L2 = ANCHOR['m_H_L2']
m_H_L1 = m_H_L2 * np.sqrt(a2_L1 / a2_L2)
split_m_H = abs(m_H_L1 - m_H_L2) / abs(m_H_L1)  # (local)
chain_m_H = (
    "m_H^2 ∝ a_2 (Connes-Chamseddine 2007 §3); a_2 universal at leading "
    f"order -> m_H_L1/m_H_L2 = sqrt(a_2_L1/a_2_L2) = sqrt({a2_L1/a2_L2:.4f}) "
    f"= {np.sqrt(a2_L1/a2_L2):.4f}; m_H_L1 = {m_H_L1:.4f} GeV; "
    f"|split| = {split_m_H:.4f}. NOTE: full ratio shown; CC4 universality "
    "predicts the leading f_2 term cancels and the residue is f_4-suppressed."
)
observables.append(('m_H', m_H_L1, m_H_L2, split_m_H, '', chain_m_H))

# -----------------------------------------------------------------------------
# (3) n_s -- scalar spectral tilt
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. n_s - 1 = -2 eps_H + ... (slow-roll relation).
#   Step 2. eps_H = -d ln H / dN; in substrate framework eps_H = (a_4/a_2)
#           propagation kernel ratio modulated by Jensen-flow rate.
#   Step 3. n_s_L1 - 1 = -2 (a_4/a_2)_L1 * c_norm; same for L2.
#           c_norm is fixed by anchor n_s_L2 = 0.9561.
#   Step 4. Compute (a_4/a_2)_L1 vs (a_4/a_2)_L2 ratio, project onto n_s split.
n_s_L2 = ANCHOR['n_s_L2']
ratio_a4_a2_L2 = a4_L2 / a2_L2                     # (local)
ratio_a4_a2_L1 = a4_L1 / a2_L1                     # (local)
# Anchor: (1 - n_s_L2) = 2 * eps_H_L2 -> eps_H_L2 = (1 - 0.9561)/2 = 0.02195
eps_H_L2 = (1.0 - n_s_L2) / 2.0                    # (local)
c_norm_n_s = eps_H_L2 / ratio_a4_a2_L2             # (local) calibration
eps_H_L1 = c_norm_n_s * ratio_a4_a2_L1             # (local)
n_s_L1 = 1.0 - 2.0 * eps_H_L1
split_n_s = abs(n_s_L1 - n_s_L2) / abs(n_s_L1)  # (local)
chain_n_s = (
    f"n_s - 1 = -2 eps_H; eps_H ∝ a_4/a_2; "
    f"(a_4/a_2)_L1 = {ratio_a4_a2_L1:.4e}, (a_4/a_2)_L2 = {ratio_a4_a2_L2:.4e}; "
    f"calibrated via n_s_L2 = {n_s_L2:.4f} -> "
    f"n_s_L1 = 1 - 2*{c_norm_n_s:.3e}*{ratio_a4_a2_L1:.4e} = {n_s_L1:.4f}; "
    f"|split| = {split_n_s:.4f}."
)
observables.append(('n_s', n_s_L1, n_s_L2, split_n_s, '', chain_n_s))

# -----------------------------------------------------------------------------
# (4) alpha_s -- running of n_s = n_s^2 - 1 (S50-51 atlas identity)
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. alpha_s = n_s^2 - 1 (S50-51 atlas identity, framework relation).
#   Step 2. Substitute n_s_L1, n_s_L2 from observable (3).
#   Step 3. CC1 inheritance: |split(alpha_s)| ≈ 2*n_s*|split(n_s)|/|alpha_s|
#           when expressed as RELATIVE split. Verified inline below.
alpha_s_L2 = ANCHOR['alpha_s_L2']
alpha_s_L1 = n_s_L1 ** 2 - 1.0
split_alpha_s = abs(alpha_s_L1 - alpha_s_L2) / abs(alpha_s_L1)  # (local)
# CC1 cross-check (5% relative tolerance per plan):
abs_split_n_s_pred_alpha = abs(2.0 * n_s_L1 * (n_s_L1 - n_s_L2) / alpha_s_L1)  # (local)
CC1_rel_err = abs(split_alpha_s - abs_split_n_s_pred_alpha) / max(split_alpha_s, 1e-30)  # (local)
CC1_pass = (CC1_rel_err < 0.05)                    # (local) per plan §6 CC1
chain_alpha_s = (
    f"alpha_s = n_s^2 - 1 (S50-51 atlas); "
    f"alpha_s_L1 = {n_s_L1:.4f}^2 - 1 = {alpha_s_L1:.6f}; alpha_s_L2 = {alpha_s_L2:.6f}; "
    f"|split| = {split_alpha_s:.4f}. CC1 inheritance check: "
    f"predicted from 2*n_s*|delta(n_s)|/|alpha_s| = {abs_split_n_s_pred_alpha:.4f}; "
    f"relative error = {CC1_rel_err:.4f}; CC1 PASS = {CC1_pass}."
)
observables.append(('alpha_s', alpha_s_L1, alpha_s_L2, split_alpha_s, '', chain_alpha_s))

# -----------------------------------------------------------------------------
# (5) mu -- FIRAS spectral distortion (Chluba 2012)
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. mu ∝ ∫ dk k^2 P_zeta(k) over dissipation window
#           (Silk damping up to last scattering).
#   Step 2. P_zeta inherits A_s scaling: P_zeta ∝ A_s.
#           Within the dissipation window the spectral shape is fixed
#           by transfer functions (regulator-blind to leading order).
#   Step 3. Ratio: mu_L1/mu_L2 = A_s_L1/A_s_L2 = a_2_L1/a_2_L2.
mu_L2 = ANCHOR['mu_L2']
mu_L1 = mu_L2 * (a2_L1 / a2_L2)
split_mu = abs(mu_L1 - mu_L2) / abs(mu_L1)  # (local)
chain_mu = (
    "mu ∝ ∫ k^2 P_zeta dk over dissipation window; P_zeta ∝ A_s; "
    f"mu_L1/mu_L2 = A_s_L1/A_s_L2 = a_2_L1/a_2_L2 = {a2_L1/a2_L2:.4f}; "
    f"mu_L1 = {mu_L1:.3e}; |split| = {split_mu:.4f}."
)
observables.append(('mu', mu_L1, mu_L2, split_mu, '', chain_mu))

# -----------------------------------------------------------------------------
# (6) r -- tensor-to-scalar ratio
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. r = P_T / P_S; in substrate framework P_T traces tensor-mode
#           transfer through the fold (S83-G46). r = 16 eps_H is CLASSICAL;
#           in substrate r depends on transit dynamics + c_T(k) tensor speed.
#   Step 2. P_T ∝ a_4 (Yang-Mills + tensor moment of D_K^2 spectral action);
#           P_S ∝ a_2 (Einstein-Hilbert).
#   Step 3. r ∝ a_4/a_2 (modulated by tensor transfer factor that is
#           regulator-blind at leading order to the substrate transit).
r_L2 = ANCHOR['r_L2']
r_L1 = r_L2 * (a4_L1 / a4_L2) * (a2_L2 / a2_L1)
split_r = abs(r_L1 - r_L2) / abs(r_L1)  # (local)
chain_r = (
    "r = P_T/P_S; P_T ∝ a_4 (Yang-Mills moment), P_S ∝ a_2 (Einstein-Hilbert); "
    f"r_L1/r_L2 = (a_4_L1/a_4_L2)*(a_2_L2/a_2_L1) "
    f"= ({a4_L1/a4_L2:.4f})*({a2_L2/a2_L1:.4f}) = {(a4_L1/a4_L2)*(a2_L2/a2_L1):.4f}; "
    f"r_L1 = {r_L1:.4e}; |split| = {split_r:.4f}."
)
observables.append(('r', r_L1, r_L2, split_r, '', chain_r))

# -----------------------------------------------------------------------------
# (7) f_NL -- non-Gaussianity amplitude
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. f_NL ∝ B(k1,k2,k3) / [P(k)^2] (bispectrum-to-power ratio).
#           In substrate GGE bispectrum, B ∝ a_3 (third spectral moment).
#   Step 2. P^2 ∝ a_2^2.
#   Step 3. f_NL ∝ a_3 / a_2^2.
f_NL_L2 = ANCHOR['f_NL_L2']
f_NL_L1 = f_NL_L2 * (a3_L1 / a3_L2) * (a2_L2 ** 2 / a2_L1 ** 2)
split_f_NL = abs(f_NL_L1 - f_NL_L2) / abs(f_NL_L1)  # (local)
chain_f_NL = (
    "f_NL ∝ a_3 / a_2^2 (GGE bispectrum / power-spectrum); "
    f"f_NL_L1/f_NL_L2 = (a_3_L1/a_3_L2)*(a_2_L2/a_2_L1)^2 "
    f"= ({a3_L1/a3_L2:.4f})*({a2_L2/a2_L1:.4f})^2 = "
    f"{(a3_L1/a3_L2)*(a2_L2/a2_L1)**2:.4f}; f_NL_L1 = {f_NL_L1:.4f}; "
    f"|split| = {split_f_NL:.4f}."
)
observables.append(('f_NL', f_NL_L1, f_NL_L2, split_f_NL, '', chain_f_NL))

# -----------------------------------------------------------------------------
# (8) w_0 -- dark-energy EoS today
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. w_0 = -1 + chi * (a_0/a_2 residual modulation).
#   Step 2. chi_L2 = +1 (KO=6 chirality alignment, W1-G1).
#           chi_L1 = 0 (zeta has no Lambda dependence; d^2 S/d(log Lambda)^2 = 0
#           structurally, so the chirality-modulation factor vanishes).
#   Step 3. w_0_L2 = -0.998 (G51 anchor). w_0_L1 = -1 + 0 * (a_0/a_2)_L1 = -1.000.
#   Step 4. |split| = |-1.000 - (-0.998)| / |-1.000| = 0.002.
#   Sign consistency: |w_0_L1| > |w_0_L2| (1.000 > 0.998) per plan §10.
w_0_L2 = ANCHOR['w_0_L2']
chi_L1 = 0.0                                       # (local) zeta has no Lambda
chi_L2 = +1.0                                      # (local) KO=6 alignment (W1-G1)
w_0_residual_L2 = w_0_L2 - (-1.0)                  # (local) +0.002
# w_0_L1 = -1 + chi_L1 * residual; residual_L1 derived from same physics
# but chi_L1 = 0 forces leading-order vanishing.
w_0_L1 = -1.0 + chi_L1 * w_0_residual_L2 * (a0_L1 / a0_L2) * (a2_L2 / a2_L1)
split_w_0 = abs(w_0_L1 - w_0_L2) / abs(w_0_L1)  # (local)
chain_w_0 = (
    "w_0 = -1 + chi * (a_0/a_2 residual); chi_L2 = +1 (KO=6 alignment); "
    "chi_L1 = 0 (zeta Lambda-blind, d^2S/d(logLambda)^2 = 0); "
    f"w_0_L2 = {w_0_L2:.4f}, w_0_L1 = -1 + 0 = {w_0_L1:.4f}; "
    f"|split| = {split_w_0:.4f}; sign check |w_0_L1| > |w_0_L2|: "
    f"{abs(w_0_L1) > abs(w_0_L2)}."
)
observables.append(('w_0', w_0_L1, w_0_L2, split_w_0, '', chain_w_0))

# -----------------------------------------------------------------------------
# (9) sigma_8 -- RMS matter fluctuation on 8 Mpc/h
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. sigma_8^2 ∝ ∫ A_s * T(k)^2 * W(k R_8)^2 dk.
#   Step 2. T(k), W(k R_8) regulator-blind (transfer functions at fixed k).
#   Step 3. sigma_8 ∝ sqrt(A_s); sigma_8_L1/sigma_8_L2 = sqrt(A_s_L1/A_s_L2)
#                                                     = sqrt(a_2_L1/a_2_L2).
sigma_8_L2 = ANCHOR['sigma_8_L2']
sigma_8_L1 = sigma_8_L2 * np.sqrt(a2_L1 / a2_L2)
split_sigma_8 = abs(sigma_8_L1 - sigma_8_L2) / abs(sigma_8_L1)  # (local)
chain_sigma_8 = (
    "sigma_8^2 ∝ ∫ A_s T^2 W^2 dk; T, W regulator-blind; "
    f"sigma_8_L1/sigma_8_L2 = sqrt(A_s_L1/A_s_L2) = sqrt({a2_L1/a2_L2:.4f}) "
    f"= {np.sqrt(a2_L1/a2_L2):.4f}; sigma_8_L1 = {sigma_8_L1:.4f}; "
    f"|split| = {split_sigma_8:.4f}."
)
observables.append(('sigma_8', sigma_8_L1, sigma_8_L2, split_sigma_8, '', chain_sigma_8))

# -----------------------------------------------------------------------------
# (10) H_0 -- Hubble today
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. H_0^2 ∝ G_N * Lambda_cosm + matter; via spectral action,
#           G_N ∝ 1/a_2 (gravity sector), Lambda_cosm ∝ a_0 / a_2.
#   Step 2. H_0^2 = (Lambda_cosm + Omega_M * H^2) ; in the substrate-compaction
#           timescape framework, the LEADING ratio is H_0^2 ∝ a_0 / a_2.
#   Step 3. H_0_L1/H_0_L2 = sqrt((a_0_L1/a_2_L1) / (a_0_L2/a_2_L2))
#                        = sqrt((a_0_L1/a_0_L2) * (a_2_L2/a_2_L1)).
#   Step 4. CC2 prediction: a_0 is exactly tau-independent and (more weakly)
#           regulator-robust at the spectral-moment ZEROTH order: split < 0.001.
#           Because a_0_L1 = N_modes_mult and a_0_L2 = sum d_k * exp(-lambda^2),
#           they are NOT exactly equal numerically; CC2 expects only the RATIO
#           a_0/a_2 to be near-degenerate. Verify.
H_0_L2 = ANCHOR['H_0_L2']
ratio_a0_a2_L1 = a0_L1 / a2_L1                     # (local)
ratio_a0_a2_L2 = a0_L2 / a2_L2                     # (local)
H_0_L1 = H_0_L2 * np.sqrt(ratio_a0_a2_L1 / ratio_a0_a2_L2)
split_H_0 = abs(H_0_L1 - H_0_L2) / abs(H_0_L1)  # (local)
chain_H_0 = (
    "H_0^2 ∝ a_0/a_2 (Lambda_cosm/G_N spectral-moment ratio); "
    f"(a_0/a_2)_L1 = {ratio_a0_a2_L1:.4e}, (a_0/a_2)_L2 = {ratio_a0_a2_L2:.4e}; "
    f"H_0_L1/H_0_L2 = sqrt({ratio_a0_a2_L1/ratio_a0_a2_L2:.4f}) "
    f"= {np.sqrt(ratio_a0_a2_L1/ratio_a0_a2_L2):.4f}; "
    f"H_0_L1 = {H_0_L1:.4f}; |split| = {split_H_0:.4f}. "
    f"CC2 expects a_0 robustness; observed split direction = "
    f"{'a_0/a_2 robust' if split_H_0 < 0.05 else 'a_0/a_2 NOT robust at this L_max'}."
)
observables.append(('H_0', H_0_L1, H_0_L2, split_H_0, '', chain_H_0))

# -----------------------------------------------------------------------------
# (11) Omega_GW -- stochastic GW energy density at LISA band
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1. Omega_GW ∝ (Yang-Mills + tensor moment) ∝ a_4 in the substrate
#           Parker-pair-production channel.
#   Step 2. Direct projection: Omega_GW_L1/Omega_GW_L2 = a_4_L1 / a_4_L2.
Omega_GW_L2 = ANCHOR['Omega_GW_L2']
Omega_GW_L1 = Omega_GW_L2 * (a4_L1 / a4_L2)
split_Omega_GW = abs(Omega_GW_L1 - Omega_GW_L2) / abs(Omega_GW_L1)  # (local)
chain_Omega_GW = (
    "Omega_GW ∝ a_4 (tensor + Yang-Mills + Parker pair production); "
    f"Omega_GW_L1/Omega_GW_L2 = a_4_L1/a_4_L2 = {a4_L1/a4_L2:.4f}; "
    f"Omega_GW_L1 = {Omega_GW_L1:.3e}; |split| = {split_Omega_GW:.4f}."
)
observables.append(('Omega_GW', Omega_GW_L1, Omega_GW_L2, split_Omega_GW, '', chain_Omega_GW))

# =============================================================================
# Section 6. Classification (DIAGNOSTIC / INTERMEDIATE / DEGENERATE)
# =============================================================================
DIAG_THRESH = 0.05                     # (local) plan §7
DEGEN_THRESH = 0.001                   # (local) plan §7

def classify(split):
    if split > DIAG_THRESH:
        return 'DIAGNOSTIC'
    elif split < DEGEN_THRESH:
        return 'DEGENERATE'
    else:
        return 'INTERMEDIATE'

# Re-build observables list with classifications filled in
classified = []                        # (local)
for (name, qL1, qL2, split, _, chain) in observables:
    cls = classify(split)
    classified.append((name, qL1, qL2, split, cls, chain))

# Tally
n_diagnostic = sum(1 for o in classified if o[4] == 'DIAGNOSTIC')      # (local)
n_intermediate = sum(1 for o in classified if o[4] == 'INTERMEDIATE')  # (local)
n_degenerate = sum(1 for o in classified if o[4] == 'DEGENERATE')      # (local)

print(f"\n{'-' * 78}")
print(f"PER-OBSERVABLE TABLE")
print(f"{'-' * 78}")
print(f"{'Obs':10s} | {'Q_L1':>14s} | {'Q_L2':>14s} | {'|split|':>10s} | Class")
print(f"{'-' * 78}")
for (name, qL1, qL2, split, cls, _) in classified:
    print(f"{name:10s} | {qL1:14.6e} | {qL2:14.6e} | {split:10.6f} | {cls}")
print(f"{'-' * 78}")
print(f"Tally: n_diagnostic = {n_diagnostic}, n_intermediate = {n_intermediate}, "
      f"n_degenerate = {n_degenerate}")

# =============================================================================
# Section 7. Verdict (PASS/FAIL/INFO per plan §9)
# =============================================================================
# PASS: n_diagnostic >= 3 AND n_degenerate <= 2.
# FAIL: n_degenerate >= 9 OR n_diagnostic = 0 OR (n_diagnostic >= 10 AND CC1 broken).
# INFO: borderline (n_diagnostic = 2 OR n_degenerate = 3).
fail_reason = ''                       # (local)
info_reason = ''                       # (local)
if n_degenerate >= 9:
    verdict = 'FAIL'
    fail_reason = f'n_degenerate = {n_degenerate} >= 9 (layers indistinguishable at observable level)'
elif n_diagnostic == 0:
    verdict = 'FAIL'
    fail_reason = 'n_diagnostic = 0 (no observable exposes layer-gap)'
elif n_diagnostic >= 10 and not CC1_pass:
    verdict = 'FAIL'
    fail_reason = f'n_diagnostic = {n_diagnostic} >= 10 with CC1 broken (alpha_s does not inherit n_s)'
elif n_diagnostic >= 3 and n_degenerate <= 2:
    verdict = 'PASS'
elif n_diagnostic == 2 or n_degenerate == 3:
    verdict = 'INFO'
    info_reason = (f'n_diagnostic = {n_diagnostic} or n_degenerate = {n_degenerate} '
                   f'is at borderline; refine boundaries in W2c.')
else:
    verdict = 'INFO'
    info_reason = (f'Distribution ({n_diagnostic},{n_intermediate},{n_degenerate}) '
                   'does not meet PASS but is not a FAIL category; classify as INFO.')

print(f"\nVerdict: {verdict}")
if fail_reason:
    print(f"  reason: {fail_reason}")
if info_reason:
    print(f"  note:   {info_reason}")
print(f"  CC1 inheritance check (alpha_s vs n_s, 5% rel): "
      f"{'PASS' if CC1_pass else 'FAIL'} (rel_err = {CC1_rel_err:.4f})")

# =============================================================================
# Section 8. Closure SHA-256 over input-pin map and per-observable values
# =============================================================================
closure_map = {
    'gate_id': 'S84-L1-L2-PROJECTION',
    'verdict': verdict,
    'value': {
        'n_diagnostic': n_diagnostic,
        'n_intermediate': n_intermediate,
        'n_degenerate': n_degenerate,
    },
    'scheme': 'L1-L2-projection',
    'convention': 'zeta-vs-Zubarev',
    'tau_fold': tau_fold,
    'L_max': L_MAX,
    'KO_dim': KO_DIM,
    'M_KK': M_KK,
    'Delta_BCS': Delta_BCS,
    'N_modes_mult': int(N_modes_mult),
    'N_flat': int(N_flat),
    'spectral_moments_L1': {'a_0': a0_L1, 'a_2': a2_L1, 'a_3': a3_L1, 'a_4': a4_L1},
    'spectral_moments_L2': {'a_0': a0_L2, 'a_2': a2_L2, 'a_3': a3_L2, 'a_4': a4_L2},
    'observables': {
        name: {'Q_L1': qL1, 'Q_L2': qL2, 'split': split, 'class': cls}
        for (name, qL1, qL2, split, cls, _) in classified
    },
    'CC1_alpha_s_vs_n_s_rel_err': CC1_rel_err,
    'CC1_pass': CC1_pass,
    'thresholds': {'diagnostic': DIAG_THRESH, 'degenerate': DEGEN_THRESH},
    'input_pin_hashes': pin_hashes,
}
closure_str = json.dumps(closure_map, sort_keys=True, default=str)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()
print(f"\nClosure SHA-256: {closure_sha}")

# =============================================================================
# Section 9. Save outputs (.npz, .png)
# =============================================================================
out_npz = SCRIPT_DIR / 's84_w2a_l1_l2_projection.npz'
out_png = SCRIPT_DIR / 's84_w2a_l1_l2_projection.png'

# Build arrays for npz
obs_names = np.array([o[0] for o in classified])
obs_L1 = np.array([o[1] for o in classified], dtype=np.float64)
obs_L2 = np.array([o[2] for o in classified], dtype=np.float64)
obs_split = np.array([o[3] for o in classified], dtype=np.float64)
obs_class = np.array([o[4] for o in classified])
obs_chain = np.array([o[5] for o in classified])

np.savez(out_npz,
    # Pins
    M_KK=M_KK, tau_fold=tau_fold, Delta_BCS=Delta_BCS,
    L_max=L_MAX, KO_dim=KO_DIM,
    N_modes_mult=N_modes_mult, N_flat=N_flat,
    N_sectors_kept=N_sectors_kept,
    # Spectrum
    flat_lambdas=flat_lambdas, flat_mults=flat_mults,
    # Spectral moments
    a0_L1=a0_L1, a2_L1=a2_L1, a3_L1=a3_L1, a4_L1=a4_L1,
    a0_L2=a0_L2, a2_L2=a2_L2, a3_L2=a3_L2, a4_L2=a4_L2,
    # Per-observable 11-row table
    obs_names=obs_names, obs_L1=obs_L1, obs_L2=obs_L2,
    obs_split=obs_split, obs_class=obs_class, obs_chain=obs_chain,
    # Tally
    n_diagnostic=n_diagnostic, n_intermediate=n_intermediate, n_degenerate=n_degenerate,
    # CC1
    CC1_rel_err=CC1_rel_err, CC1_pass=CC1_pass,
    # Verdict
    verdict=verdict, fail_reason=fail_reason, info_reason=info_reason,
    # SHA
    closure_sha=closure_sha,
)
print(f"\nData saved: {out_npz}")

# Plot: 11-row bar chart of split, color-coded by classification
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# (a) Bar chart, log-y
ax = axes[0]
class_color = {'DIAGNOSTIC': '#dc3912', 'INTERMEDIATE': '#ff9900', 'DEGENERATE': '#109618'}
colors = [class_color[c] for c in obs_class]
bars = ax.bar(obs_names, obs_split, color=colors, alpha=0.75, edgecolor='black', linewidth=0.7)
ax.axhline(DIAG_THRESH, color='#dc3912', linestyle='--', linewidth=1.2, label=f'DIAGNOSTIC threshold ({DIAG_THRESH})')
ax.axhline(DEGEN_THRESH, color='#109618', linestyle='--', linewidth=1.2, label=f'DEGENERATE threshold ({DEGEN_THRESH})')
ax.set_ylabel(r'$|Q_{L1} - Q_{L2}| / |Q_{L1}|$  (relative split)')
ax.set_title(f'L1-L2 split per observable (L_max = {L_MAX}, tau = {tau_fold})')
ax.set_yscale('log')
ax.set_ylim(max(obs_split.min() * 0.5, 1e-12), max(obs_split.max() * 2, 10.0))
ax.grid(alpha=0.3, which='both')
ax.legend(loc='upper right', fontsize=9)
for bar, val, cls in zip(bars, obs_split, obs_class):
    ax.text(bar.get_x() + bar.get_width()/2, val * 1.3,
            f'{val:.2e}\n[{cls[:4]}]', ha='center', fontsize=7,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.7))
plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

# (b) Verdict + tally banner
ax = axes[1]
ax.axis('off')
banner = (
    f"S84 W2a-14 -- L1-L2-PROJECTION\n\n"
    f"Verdict: {verdict}\n"
    f"  4-tuple: (value=({n_diagnostic},{n_intermediate},{n_degenerate}), "
    f"scheme=L1-L2-projection,\n"
    f"           convention=zeta-vs-Zubarev, L_max={L_MAX})\n\n"
    f"Tally:\n"
    f"  DIAGNOSTIC   : {n_diagnostic} (>{DIAG_THRESH})  [PASS needs >=3]\n"
    f"  INTERMEDIATE : {n_intermediate} ({DEGEN_THRESH}..{DIAG_THRESH})\n"
    f"  DEGENERATE   : {n_degenerate} (<{DEGEN_THRESH})  [PASS needs <=2]\n\n"
    f"Spectral moments (L_max={L_MAX}, tau={tau_fold}):\n"
    f"  L1 (zeta):    a_0={a0_L1:.3e}  a_2={a2_L1:.3e}  a_4={a4_L1:.3e}\n"
    f"  L2 (Zubarev): a_0={a0_L2:.3e}  a_2={a2_L2:.3e}  a_4={a4_L2:.3e}\n\n"
    f"Cross-check CC1 (alpha_s inherits n_s): "
    f"{'PASS' if CC1_pass else 'FAIL'}\n"
    f"  rel err = {CC1_rel_err:.4f} (5% threshold)\n\n"
    f"Modes (mult-weighted): {int(N_modes_mult)} on {N_sectors_kept} sectors\n"
    f"GPU used: {GPU_USED}\n\n"
    f"Closure SHA (head 16):\n  {closure_sha[:16]}...\n\n"
    f"Per-obs classification:\n"
)
for (name, qL1, qL2, split, cls, _) in classified:
    banner += f"  {name:10s}: split={split:10.4e}  -> {cls}\n"

ax.text(0.02, 0.98, banner, family='monospace', fontsize=8.5,
        verticalalignment='top', transform=ax.transAxes)

plt.tight_layout()
plt.savefig(out_png, dpi=120, bbox_inches='tight')
print(f"Plot saved: {out_png}")

# =============================================================================
# Section 10. Verdict line (append to s84_gate_verdicts.txt)
# =============================================================================
verdict_line = (
    f"S84-L1-L2-PROJECTION: {verdict} -- "
    f"value=({n_diagnostic},{n_intermediate},{n_degenerate}) "
    f"scheme=L1-L2-projection convention=zeta-vs-Zubarev "
    f"L_max={L_MAX} sha256={closure_sha}\n"
)
verdicts_path = SCRIPT_DIR / 's84_gate_verdicts.txt'
with open(verdicts_path, 'a', encoding='utf-8') as f:
    f.write(verdict_line)
print(f"\nVerdict appended to: {verdicts_path}")
print(f"  >> {verdict_line.strip()}")

# =============================================================================
# Section 11. Final 4-tuple
# =============================================================================
print("\n" + "=" * 78)
print(f"4-tuple: (value=({n_diagnostic},{n_intermediate},{n_degenerate}), "
      f"scheme=L1-L2-projection, convention=zeta-vs-Zubarev, L_max={L_MAX})")
print("=" * 78)
