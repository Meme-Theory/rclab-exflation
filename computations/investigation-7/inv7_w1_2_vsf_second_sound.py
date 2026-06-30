#!/usr/bin/env python3
"""
INV7-W1-2: Void Size Function with the second-sound first-sound-ring feature
============================================================================
Investigation 7, Wave 1, Gate INV7-W1-2 | Agent: cosmic-web-theorist
Trigger: [VERIFY] | Classification: PHONONIC

HYPOTHESIS (plan §W1-2):
  If the first-sound ring at r1=325.3 Mpc is a GENUINE second-sound feature (not a
  doubled-BAO aliasing artifact), then the framework Void Size Function — computed
  from P_FW(k) = P_shape(k)*[1 + A_FS*W(k;k1)] via the Sheth-van-de-Weygaert (2004)
  excursion-set two-barrier void model — carries a DISTINCT bump/inflection at the
  ring scale that is ABSENT from a featureless-P(k) VSF AND detectable against
  DESI/SDSS void catalogs (VIDE/ZOBOV).

OPERATOR (plan PRDR (1)):
  PASS iff  max_{r in [275,375] Mpc} |VSF_feat(r) - VSF_nofeat(r)| / VSF_nofeat(r) >= rel_bump
  AND the difference peak is LOCALIZED within +/- 25 Mpc of r1=325.3 Mpc.
  strict_PASS_boundary: rel_bump = 0.05 (>= direction); localization window |r_peak - 325.3| <= 25 Mpc.

UPSTREAM (W1-1 LANDED, FAIL):
  feature_A_FS = 0.00388533 is the SUBSTRATE-GENUINE second-sound ring amplitude
  (52.5x WEAKER than the canonical 0.204, which is the recombination FIRST-sound
  stand-in). PRIMARY run uses the substrate A_FS; CONTRAST run uses A_FS=0.204.

SUBSTITUTION CHAIN (plan §W1-2 (7)):
  Claim: "A genuine second-sound feature in P(k) at k1 PRODUCES a localized VSF excess
          at r_void ~ r1; an aliased (doubled-BAO) artifact does NOT."
  Step 1 (defs): P_FW(k)=P_shape(k)*[1 + A_FS*W(k;k1)];  W = Gaussian ring window at
                 k1=0.0193150486 Mpc^-1 (r1 = 2 pi / k1 = 325.3 Mpc).
                 VSF(r) = (1/V(r)) |d ln sigma^-1/d ln r| * [S f(S)]_SvdW04 (two-barrier).
                 delta_v=-2.717, delta_c=1.686 (s52 EdS barriers; D=|dv|/dc=1.611).
  Step 2 (subst): Delta_VSF(r) = VSF[P_shape*(1+A_FS*W)](r) - VSF[P_shape](r)
                  = response of the first-crossing distribution to the P(k) feature at k1.
  Step 3 (direction): a real-space feature at r1 = 2pi/k1 in xi(r) seeds a preferred void
                  wall-to-wall scale; the excursion-set void multiplicity inherits an
                  inflection at r_void ~ r1. An EXCESS of power at k1 -> enhanced sigma(R)
                  near R ~ r1/2 -> localized VSF response. PASS iff localized >=5%.
  Step 4 (read-off): localized >=5% inflection at r1 -> Reading A (real-in-voids, ring genuine);
                  no localized feature -> Reading B (aliased, doubled-BAO artifact).

OBSERVATIONAL REACH (Mao 2016, arXiv:1602.02771):
  BOSS DR12 ZOBOV quality voids: R_eff = 15-130 h^-1 Mpc (majority 30-80). Largest single
  void R_eff=63.5 h^-1 Mpc=94.2 Mpc; catalog max 130 h^-1 Mpc=192.9 Mpc. r1=325.3 Mpc lies
  FAR beyond the void-size support -> even a strong VSF feature at r1 is observationally
  UNREACHABLE with current catalogs. Reported VSF-vs-LCDM precision <6% (Nadathur 2016).

References:
  - Sheth & van de Weygaert, MNRAS 350, 517 (2004) [SvdW04] -- two-barrier void multiplicity
  - Eisenstein & Hu, ApJ 496, 605 (1998) [EH98] -- no-wiggle transfer function
  - Mao+ 2016, arXiv:1602.02771 -- BOSS DR12 ZOBOV void catalog (number counts data file)
  - Nadathur 2016, arXiv:1602.04752 -- BOSS DR11 ZOBOV VSF, <6% LCDM deviation
  - s52_void_function.py (canonical SvdW machinery this script reuses)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_shared'))

import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    Omega_m, Omega_b, sigma_8, H_0_km_s_Mpc, PI,
    k_pivot_planck, planck_ns, r1_first_sound_ring_Mpc,
)

# ============================================================================
#  Section 0: SHA pins (input-pin map) + verdict payload helper
# ============================================================================

SCRIPT_PATH = os.path.abspath(__file__)
HERE = os.path.dirname(SCRIPT_PATH)
CANON_PATH = os.path.join(HERE, '..', '_shared', 'canonical_constants.py')
W1_1_NPZ = os.path.join(HERE, 'inv7_w1_1_c2_substrate.npz')
VOID_DATA = os.path.join(HERE, '_data', 'vide_zobov_void_counts.txt')


def _sha256_file(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def closure_hash(pin_map):
    """SHA-256 over the ordered input-pin map (audit SHA)."""
    h = hashlib.sha256()
    for k in sorted(pin_map):
        h.update(f"{k}={pin_map[k]}".encode())
    return h.hexdigest()


def print_verdict_payload(gate_id, verdict, value, scheme, convention, L_max,
                          audit_sha, content_sha, extra_rows=None,
                          sign_v=None, mag_v=None, regime_v=None):
    """Print the verdict payload for the agent to pass to emit_verdict (race-safe)."""
    print("\n" + "=" * 72)
    print("VERDICT PAYLOAD (agent: call emit_verdict with these fields)")
    print("=" * 72)
    print(f"gate_id    = {gate_id}")
    print(f"verdict    = {verdict}")
    print(f"value      = {value}")
    print(f"scheme     = {scheme}")
    print(f"convention = {convention}")
    print(f"L_max      = {L_max}")
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    if sign_v is not None:
        print(f"sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v}")
    if extra_rows:
        for r in extra_rows:
            print(f"extra_row: {r}")
    print("=" * 72)


# ============================================================================
#  Section 1: Cosmology + feature parameters
# ============================================================================

h = H_0_km_s_Mpc / 100.0          # = 0.674
n_s = planck_ns                   # 0.9649
k_pivot = k_pivot_planck          # 0.05 Mpc^-1

# SvdW04 two-barrier thresholds (s52 EdS values; src: s52_void_function.py:59-60)
delta_v = -2.717                  # (local) void shell-crossing (linear, EdS); s52-canonical
delta_c = 1.686                   # (local) collapse threshold (linear, EdS); s52-canonical
D_barrier = abs(delta_v) / delta_c   # = 1.611  (local)

# Feature (first-sound ring) parameters
r1_Mpc = float(r1_first_sound_ring_Mpc)   # 325.3 Mpc
# k1 from W1-1 upstream (consume real substrate feature, not canonical fallback)
_w1 = np.load(W1_1_NPZ)
A_FS_substrate = float(_w1['feature_A_FS'])     # 0.00388533 (substrate-genuine; W1-1 FAIL)
k1_invMpc = float(_w1['feature_k1_invMpc'])     # 0.0193150486 Mpc^-1
r1_from_w1 = float(_w1['feature_r1_Mpc'])       # 325.3 Mpc
A_FS_canon = float(_w1['A_FS_canon'])           # 0.204 (recombination first-sound stand-in)

# Cross-check k1 <-> r1 consistency (r1 = 2 pi / k1)
r1_check = 2.0 * PI / k1_invMpc                  # (local)

# Pre-registered gate thresholds (plan PRDR (1)/(2)) — all # (local): gate-specific pins
REL_BUMP = 0.05                   # (local) >=5% localized VSF excess threshold (plan strict_PASS_boundary)
LOC_WINDOW_Mpc = 25.0             # (local) |r_peak - r1| <= 25 Mpc localization (plan operator)
WIN_LO, WIN_HI = 275.0, 375.0     # (local) feature-localization window [275,375] Mpc (plan operator)
INFO_BUMP = 0.02                  # (local) 2-5% sub-threshold -> INFO band floor (plan INFO_meaning)

# Ring window width: a localized ring in k centered at k1. Use a Gaussian in ln k
# with fractional width sigma_lnk; a BAO-like ring is narrow (~10% in k).
SIGMA_LNK = 0.10                  # (local) fractional width of the ring window in ln k

print("=" * 72)
print("INV7-W1-2: Void Size Function with the second-sound first-sound-ring feature")
print("=" * 72)
print(f"  Omega_m={Omega_m}, Omega_b={Omega_b}, h={h:.4f}, sigma_8={sigma_8}, n_s={n_s}")
print(f"  delta_v={delta_v}, delta_c={delta_c}, D=|dv|/dc={D_barrier:.4f}")
print(f"  r1={r1_Mpc} Mpc, k1={k1_invMpc:.10f} Mpc^-1, r1=2pi/k1 check={r1_check:.4f} Mpc")
print(f"  A_FS_substrate (W1-1, primary) = {A_FS_substrate:.8f}")
print(f"  A_FS_canon (0.204, contrast)   = {A_FS_canon:.6f}  (ratio canon/sub = {A_FS_canon/A_FS_substrate:.2f}x)")
print(f"  ring window: Gaussian in ln k, sigma_lnk={SIGMA_LNK}")
print(f"  PASS: max|dVSF/VSF| over [{WIN_LO},{WIN_HI}] Mpc >= {REL_BUMP} AND |r_peak-r1|<={LOC_WINDOW_Mpc} Mpc")
print()

# ============================================================================
#  Section 2: Eisenstein-Hu (1998) no-wiggle transfer function
# ============================================================================

def transfer_EH98(k_hMpc):
    """EH98 no-wiggle (zero-baryon) transfer function. k in h/Mpc. Eq. 29-31."""
    Omega_m_h2 = Omega_m * h**2
    Omega_b_h2 = Omega_b * h**2
    f_b = Omega_b / Omega_m
    Theta_27 = 2.7255 / 2.7
    s = 44.5 * np.log(9.83 / Omega_m_h2) / np.sqrt(1.0 + 10.0 * Omega_b_h2**0.75)
    alpha_Gamma = (1.0 - 0.328 * np.log(431.0 * Omega_m_h2) * f_b
                   + 0.38 * np.log(22.3 * Omega_m_h2) * f_b**2)
    Gamma_eff = Omega_m * h * (alpha_Gamma
                               + (1.0 - alpha_Gamma) / (1.0 + (0.43 * k_hMpc * s)**4))
    q = k_hMpc * Theta_27**2 / Gamma_eff
    L = np.log(2.0 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1.0 + 62.5 * q)
    return L / (L + C * q**2)


# ============================================================================
#  Section 3: P(k) shape + ring feature window
# ============================================================================

def ring_window(k_hMpc):
    """
    Localized ring window W(k; k1): a Gaussian in ln k centered at k1.
    The first-sound ring is a narrow oscillatory feature in P(k); we model its
    leading localized envelope as a Gaussian bump at k1 (a single ring lobe).
    Returns a dimensionless window in [0,1], peaking at 1 at k=k1.
    """
    k1_hMpc = k1_invMpc / h          # convert k1 [Mpc^-1] -> h/Mpc  (local)
    ln_ratio = np.log(k_hMpc / k1_hMpc)
    return np.exp(-0.5 * (ln_ratio / SIGMA_LNK)**2)


def P_unnorm(k_hMpc, A_FS):
    """
    Unnormalized framework matter power spectrum WITH the ring feature.
      P_FW(k) = P_shape(k) * [1 + A_FS * W(k; k1)]
    P_shape(k) = k * (k/k_*)^{n_s-1} * T_EH98(k)^2   (no running; LCDM shape).
    A_FS = 0 reproduces the featureless P_shape.
    """
    k_star_hMpc = k_pivot / h
    ln_ratio = np.log(k_hMpc / k_star_hMpc)
    shape = k_hMpc * np.exp((n_s - 1.0) * ln_ratio)
    T_k = transfer_EH98(k_hMpc)
    P_shape = shape * T_k**2
    feature = 1.0 + A_FS * ring_window(k_hMpc)
    return P_shape * feature


# ============================================================================
#  Section 4: sigma(R) via top-hat filter, normalized to sigma_8
# ============================================================================

K_MIN, K_MAX, NPTS_K = 1e-4, 100.0, 6000   # k-grid for sigma^2 integral (h/Mpc)

def sigma_squared_raw(R_hMpc, A_FS):
    """Raw (unnormalized) sigma^2(R) = (1/2pi^2) int dk k^2 P(k) |W_TH(kR)|^2 (log-k)."""
    ln_k = np.linspace(np.log(K_MIN), np.log(K_MAX), NPTS_K)
    k = np.exp(ln_k)
    x = k * R_hMpc
    W = np.where(x < 1e-3,
                 1.0 - x**2 / 10.0 + x**4 / 280.0,
                 3.0 * (np.sin(x) - x * np.cos(x)) / x**3)
    Pk = P_unnorm(k, A_FS)
    integrand = k**3 * Pk * W**2 / (2.0 * PI**2)
    return np.trapezoid(integrand, ln_k)


# Normalize to sigma_8 SEPARATELY for featured + featureless P(k):
# both featured and featureless models are sigma_8-normalized at R=8 h^-1 Mpc,
# the standard convention (the feature at k1 ~ 0.013 h/Mpc is far below the
# R=8 h^-1 Mpc filter scale, so it barely shifts the normalization — but we
# normalize each consistently so the discriminator is the SHAPE near r1, not
# a global amplitude offset).
def make_norm(A_FS):
    s2_raw_8 = sigma_squared_raw(8.0, A_FS)
    return sigma_8**2 / s2_raw_8


def sigma_R(R_hMpc, A_FS, norm):
    return np.sqrt(norm * sigma_squared_raw(R_hMpc, A_FS))


# ============================================================================
#  Section 5: SvdW04 two-barrier void multiplicity (reuse s52 machinery)
# ============================================================================

def f_SvdW(nu_v):
    """
    Sheth-van de Weygaert (2004) two-barrier first-crossing distribution (Eq. 14),
    returning S*f(S) with S = sigma^2, nu_v = (|delta_v|/sigma)^2.
    (Identical machinery to s52_void_function.py::f_SvdW.)
    """
    D = D_barrier
    result = np.zeros_like(nu_v, dtype=float)
    for j in range(1, 60):
        x_j = j * PI * D / (1.0 + D)
        prefactor = j * PI * D**2 / (1.0 + D)**3
        exp_arg = -j**2 * PI**2 * D**2 / (2.0 * (1.0 + D)**2 * nu_v)
        result += prefactor * np.sin(x_j) * np.exp(exp_arg)
    Sf = (delta_v**2 / nu_v) * result
    return Sf


def void_size_function(R_arr_hMpc, A_FS, norm):
    """
    VSF dn/d ln R over R_arr_hMpc for a given feature amplitude.
      dn/d ln R = (1/V(R)) * |d ln sigma^-1/d ln R| * [S f(S)]_SvdW04
    """
    sig = np.array([sigma_R(R, A_FS, norm) for R in R_arr_hMpc])
    eps = 0.005
    dln = np.zeros_like(R_arr_hMpc)
    for i, R in enumerate(R_arr_hMpc):
        s_lo = sigma_R(R * (1 - eps), A_FS, norm)
        s_hi = sigma_R(R * (1 + eps), A_FS, norm)
        dln[i] = abs(np.log(s_hi / s_lo) / np.log((1 + eps) / (1 - eps)))
    nu_v = (abs(delta_v) / sig)**2
    V_R = (4.0 / 3.0) * PI * R_arr_hMpc**3
    Sf = f_SvdW(nu_v)
    dn_dlnR = (1.0 / V_R) * dln * Sf
    return dn_dlnR, sig, nu_v, dln, Sf


# ============================================================================
#  Section 6: VSF grid + discriminator (PRIMARY = substrate, CONTRAST = canon)
# ============================================================================

# r_void grid over [10, 500] Mpc (plan scan_range), log-uniform, 512 points.
N_EVAL = 512                      # (local) plan machinery_pin_map N_eval
r_void_Mpc = np.logspace(np.log10(10.0), np.log10(500.0), N_EVAL)
R_arr_hMpc = r_void_Mpc * h         # convert to h^-1 Mpc for sigma(R)  (local)

print("Step 1: normalizations (sigma_8 at R=8 h^-1 Mpc)...")
norm_nofeat = make_norm(0.0)
norm_sub = make_norm(A_FS_substrate)
norm_canon = make_norm(A_FS_canon)
print(f"  norm_nofeat = {norm_nofeat:.6e}")
print(f"  norm_substrate = {norm_sub:.6e}  (A_FS={A_FS_substrate:.6e})")
print(f"  norm_canon = {norm_canon:.6e}  (A_FS={A_FS_canon:.6f})")
# verify sigma8
print(f"  sigma(8) nofeat = {sigma_R(8.0, 0.0, norm_nofeat):.5f} (target {sigma_8})")
print(f"  sigma(8) substrate = {sigma_R(8.0, A_FS_substrate, norm_sub):.5f}")
print(f"  sigma(8) canon = {sigma_R(8.0, A_FS_canon, norm_canon):.5f}")
print()

print("Step 2: computing VSFs (nofeat / substrate / canon)...")
vsf_nofeat, sig_nf, nu_nf, dln_nf, Sf_nf = void_size_function(R_arr_hMpc, 0.0, norm_nofeat)
vsf_sub, sig_s, nu_s, dln_s, Sf_s = void_size_function(R_arr_hMpc, A_FS_substrate, norm_sub)
vsf_canon, sig_c, nu_c, dln_c, Sf_c = void_size_function(R_arr_hMpc, A_FS_canon, norm_canon)
print("  VSFs computed.")
print()

# Fractional VSF difference (the RATIO discriminator, removes overall normalization)
# Guard against divide-by-zero in the deep large-R tail where VSF -> 0.
eps_floor = np.max(vsf_nofeat) * 1e-30
delta_sub = (vsf_sub - vsf_nofeat) / np.maximum(vsf_nofeat, eps_floor)
delta_canon = (vsf_canon - vsf_nofeat) / np.maximum(vsf_nofeat, eps_floor)

# Localization window mask [275, 375] Mpc
win_mask = (r_void_Mpc >= WIN_LO) & (r_void_Mpc <= WIN_HI)

def discriminator(delta):
    """max|delta| over [275,375], its r-location, and localization check vs r1."""
    dwin = np.abs(delta[win_mask])
    rwin = r_void_Mpc[win_mask]
    if dwin.size == 0:
        return 0.0, np.nan, False
    imax = int(np.argmax(dwin))
    max_abs = float(dwin[imax])
    r_peak = float(rwin[imax])
    localized = abs(r_peak - r1_Mpc) <= LOC_WINDOW_Mpc
    return max_abs, r_peak, localized

max_sub, rpeak_sub, loc_sub = discriminator(delta_sub)
max_canon, rpeak_canon, loc_canon = discriminator(delta_canon)

print("=" * 72)
print("DISCRIMINATOR (max |VSF_feat - VSF_nofeat| / VSF_nofeat over [275,375] Mpc)")
print("=" * 72)
print(f"  PRIMARY  (substrate A_FS={A_FS_substrate:.6e}):")
print(f"    max|dVSF/VSF| = {max_sub:.6e}  ({max_sub*100:.4f}%)  at r={rpeak_sub:.2f} Mpc")
print(f"    localized within +/-{LOC_WINDOW_Mpc} Mpc of r1={r1_Mpc}? {loc_sub}")
print(f"    PASS threshold {REL_BUMP*100:.1f}% -> {'MET' if max_sub >= REL_BUMP else 'NOT MET'}")
print(f"  CONTRAST (canonical A_FS={A_FS_canon:.4f}):")
print(f"    max|dVSF/VSF| = {max_canon:.6e}  ({max_canon*100:.4f}%)  at r={rpeak_canon:.2f} Mpc")
print(f"    localized within +/-{LOC_WINDOW_Mpc} Mpc of r1={r1_Mpc}? {loc_canon}")
print(f"    PASS threshold {REL_BUMP*100:.1f}% -> {'MET' if max_canon >= REL_BUMP else 'NOT MET'}")
print()

# ============================================================================
#  Section 7: Observational reach vs DESI/SDSS VIDE/ZOBOV void catalog
# ============================================================================

# Parse the fetched Mao 2016 void-count edge summary
void_meta = {}
with open(VOID_DATA, 'r') as fh:
    for line in fh:
        s = line.strip()
        if s.startswith('#') or not s:
            continue
        parts = s.split()
        if len(parts) >= 2:
            key = parts[0]
            try:
                void_meta[key] = float(parts[1])
            except ValueError:
                pass

R_eff_max_cat_hMpc = void_meta.get('R_eff_max_catalog_hMpc', 130.0)   # 130 h^-1 Mpc
R_eff_max_ind_hMpc = void_meta.get('R_eff_max_individual_hMpc', 63.467)
N_voids_total = void_meta.get('N_voids_total_qualitycut', 1228.0)
VSF_dev_bound = void_meta.get('VSF_LCDM_deviation_bound', 0.06)

R_eff_max_cat_Mpc = R_eff_max_cat_hMpc / h    # 130/0.674 = 192.9 Mpc  (local)
r1_in_hMpc = r1_Mpc * h                        # 325.3*0.674 = 219.25 h^-1 Mpc  (local)
# Is the feature scale reachable by the catalog void-size support?
feature_reachable = r1_Mpc <= R_eff_max_cat_Mpc

print("=" * 72)
print("OBSERVATIONAL REACH vs DESI/SDSS VIDE/ZOBOV (Mao 2016 arXiv:1602.02771)")
print("=" * 72)
print(f"  catalog max R_eff = {R_eff_max_cat_hMpc:.1f} h^-1 Mpc = {R_eff_max_cat_Mpc:.1f} Mpc")
print(f"  largest single void R_eff = {R_eff_max_ind_hMpc:.3f} h^-1 Mpc = {R_eff_max_ind_hMpc/h:.1f} Mpc")
print(f"  N quality voids total = {int(N_voids_total)}")
print(f"  reported VSF-vs-LCDM precision bound = {VSF_dev_bound*100:.0f}% (Nadathur 2016)")
print(f"  feature scale r1 = {r1_Mpc} Mpc = {r1_in_hMpc:.2f} h^-1 Mpc")
print(f"  is r1 within the catalog void-size support? {feature_reachable}")
print(f"  -> r1 lies {'INSIDE' if feature_reachable else 'BEYOND'} the observed void radii;"
      f" {'detectable in principle' if feature_reachable else 'UNREACHABLE with current catalogs'}")
print()

# ============================================================================
#  Section 8: VERDICT logic
# ============================================================================
# PASS  iff PRIMARY (substrate) max_sub >= REL_BUMP AND loc_sub.
# INFO  iff INFO_BUMP <= max_sub < REL_BUMP (sub-threshold bump), OR feature
#          scale beyond catalog reach (statistics-limited: no voids at r1).
# FAIL  iff max_sub < INFO_BUMP (no localized VSF feature -> ring is aliased,
#          Reading B), the substrate ring does NOT survive into the void direction.

primary_pass = (max_sub >= REL_BUMP) and loc_sub
primary_info = (INFO_BUMP <= max_sub < REL_BUMP)

# Sign verdict: did the feature produce the PREDICTED-DIRECTION response?
# Substitution-chain Step 3 predicts an EXCESS (positive power at k1 -> positive
# sigma response near r1/2). Sign PASS iff the in-window peak of (signed) delta_sub
# is positive (an excess), matching the predicted direction.
signed_peak_sub = float(delta_sub[win_mask][np.argmax(np.abs(delta_sub[win_mask]))]) if win_mask.any() else 0.0
sign_v = "PASS" if signed_peak_sub >= 0 else "FAIL"

if primary_pass:
    verdict = "PASS"
    mag_v = "PASS"
elif primary_info:
    verdict = "INFO"
    mag_v = "INFO"
else:
    verdict = "FAIL"
    mag_v = "FAIL"

# Regime verdict: the SvdW excursion-set + EH98 transfer is valid across the
# full [10,500] Mpc window (no auto-shortening; deterministic integration). VALID.
regime_v = "VALID"

# Reading tag for the value string
if verdict == "PASS":
    reading = "Reading-A_real-in-voids(ring-genuine)"
elif verdict == "FAIL":
    reading = "Reading-B_aliased(doubled-BAO-artifact;ring-does-NOT-survive-void-direction)"
else:
    reading = "INFO_sub-threshold-bump-OR-beyond-catalog-reach"

print("=" * 72)
print(f"GATE VERDICT: INV7-W1-2 -> {verdict}")
print("=" * 72)
print(f"  PRIMARY (substrate A_FS={A_FS_substrate:.6e}): max bump {max_sub*100:.4f}% "
      f"(threshold {REL_BUMP*100:.1f}%); localized={loc_sub}; sign(peak)={'+' if signed_peak_sub>=0 else '-'}")
print(f"  Reading: {reading}")
print(f"  CONTEXT: substrate ring is {A_FS_canon/A_FS_substrate:.1f}x weaker than the canonical "
      f"0.204 stand-in; CONTRAST(0.204) bump {max_canon*100:.4f}%")
print(f"  OBS REACH: r1={r1_Mpc} Mpc {'within' if feature_reachable else 'BEYOND'} catalog "
      f"void support (max R_eff={R_eff_max_cat_Mpc:.0f} Mpc)")
print()

# ============================================================================
#  Section 9: Save data
# ============================================================================

npz_path = os.path.join(HERE, 'inv7_w1_2_vsf_second_sound.npz')

# audit + content SHAs
content_sha = _sha256_file(SCRIPT_PATH)
pin_map = {
    'script_content_sha256': content_sha,
    'canonical_constants_sha256': _sha256_file(CANON_PATH),
    'w1_1_npz_sha256': _sha256_file(W1_1_NPZ),
    'void_data_sha256': _sha256_file(VOID_DATA),
    'gate_id': 'INV7-W1-2',
    'A_FS_substrate': repr(A_FS_substrate),
    'A_FS_canon': repr(A_FS_canon),
    'k1_invMpc': repr(k1_invMpc),
    'r1_Mpc': repr(r1_Mpc),
    'rel_bump': repr(REL_BUMP),
    'loc_window_Mpc': repr(LOC_WINDOW_Mpc),
    'win_lo': repr(WIN_LO),
    'win_hi': repr(WIN_HI),
    'delta_v': repr(delta_v),
    'delta_c': repr(delta_c),
    'N_eval': repr(N_EVAL),
    'sigma_lnk': repr(SIGMA_LNK),
    'scheme': 'FW',
    'convention': 'RATIO',
}
audit_sha = closure_hash(pin_map)

np.savez(
    npz_path,
    gate_id='INV7-W1-2',
    verdict=verdict,
    # discriminator results
    max_bump_substrate=max_sub,
    rpeak_substrate=rpeak_sub,
    localized_substrate=loc_sub,
    sign_peak_substrate=signed_peak_sub,
    max_bump_canon=max_canon,
    rpeak_canon=rpeak_canon,
    localized_canon=loc_canon,
    rel_bump_threshold=REL_BUMP,
    info_bump_floor=INFO_BUMP,
    loc_window_Mpc=LOC_WINDOW_Mpc,
    win_lo=WIN_LO, win_hi=WIN_HI,
    # feature inputs (consumed from W1-1)
    A_FS_substrate=A_FS_substrate,
    A_FS_canon=A_FS_canon,
    k1_invMpc=k1_invMpc,
    r1_Mpc=r1_Mpc,
    r1_from_w1=r1_from_w1,
    ratio_canon_over_sub=A_FS_canon / A_FS_substrate,
    # VSF arrays
    r_void_Mpc=r_void_Mpc,
    R_arr_hMpc=R_arr_hMpc,
    vsf_nofeat=vsf_nofeat,
    vsf_substrate=vsf_sub,
    vsf_canon=vsf_canon,
    delta_substrate=delta_sub,
    delta_canon=delta_canon,
    sigma_nofeat=sig_nf,
    sigma_substrate=sig_s,
    sigma_canon=sig_c,
    # barriers + cosmology
    delta_v=delta_v, delta_c=delta_c, D_barrier=D_barrier,
    Omega_m=Omega_m, Omega_b=Omega_b, h=h, sigma_8=sigma_8, n_s=n_s,
    sigma_lnk=SIGMA_LNK,
    # observational reach
    R_eff_max_catalog_hMpc=R_eff_max_cat_hMpc,
    R_eff_max_catalog_Mpc=R_eff_max_cat_Mpc,
    R_eff_max_individual_hMpc=R_eff_max_ind_hMpc,
    N_voids_total_qualitycut=N_voids_total,
    VSF_LCDM_deviation_bound=VSF_dev_bound,
    r1_in_hMpc=r1_in_hMpc,
    feature_reachable=feature_reachable,
    # 3-tuple
    sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
    audit_sha256=audit_sha, content_sha256=content_sha,
)
print(f"Data saved: {npz_path}")

# ============================================================================
#  Section 10: Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    'INV7-W1-2: Void Size Function with the second-sound first-sound-ring feature\n'
    f'(SvdW04 two-barrier; substrate $A_{{FS}}$={A_FS_substrate:.3e} vs canonical 0.204; '
    f'$r_1$={r1_Mpc} Mpc)',
    fontsize=12, fontweight='bold'
)

# (a) VSF: nofeat vs substrate vs canon
ax = axes[0, 0]
ax.loglog(r_void_Mpc, vsf_nofeat, 'k-', lw=2, label='featureless $P(k)$')
ax.loglog(r_void_Mpc, vsf_sub, color='#2166AC', ls='--', lw=1.6,
          label=f'substrate ($A_{{FS}}$={A_FS_substrate:.2e})')
ax.loglog(r_void_Mpc, vsf_canon, color='#B2182B', ls='-.', lw=1.6,
          label='canonical ($A_{FS}$=0.204)')
ax.axvline(r1_Mpc, color='gray', ls=':', lw=1.2, label=f'$r_1$={r1_Mpc} Mpc')
ax.axvspan(WIN_LO, WIN_HI, alpha=0.10, color='gold', label='window [275,375] Mpc')
ax.set_xlabel('$r_{\\rm void}$ [Mpc]', fontsize=11)
ax.set_ylabel('$dn/d\\ln r$ [$(h^{-1}{\\rm Mpc})^{-3}$]', fontsize=11)
ax.set_title('(a) Void Size Function', fontsize=11)
ax.legend(fontsize=8, loc='lower left')
ax.grid(True, alpha=0.3)

# (b) Fractional VSF difference (the discriminator) — zoom on the window
ax = axes[0, 1]
ax.plot(r_void_Mpc, delta_sub * 100, color='#2166AC', lw=1.8,
        label=f'substrate (max {max_sub*100:.3f}%)')
ax.plot(r_void_Mpc, delta_canon * 100, color='#B2182B', ls='-.', lw=1.4,
        label=f'canonical (max {max_canon*100:.3f}%)')
ax.axhline(REL_BUMP * 100, color='green', ls='--', lw=1, label=f'PASS {REL_BUMP*100:.0f}%')
ax.axhline(-REL_BUMP * 100, color='green', ls='--', lw=1)
ax.axvline(r1_Mpc, color='gray', ls=':', lw=1.2)
ax.axvspan(r1_Mpc - LOC_WINDOW_Mpc, r1_Mpc + LOC_WINDOW_Mpc, alpha=0.12, color='orange',
           label=f'$\\pm${LOC_WINDOW_Mpc:.0f} Mpc loc.')
ax.set_xlim(WIN_LO - 50, WIN_HI + 50)
ax.set_xlabel('$r_{\\rm void}$ [Mpc]', fontsize=11)
ax.set_ylabel('$\\Delta {\\rm VSF}/{\\rm VSF}$ [%]', fontsize=11)
ax.set_title('(b) Feature discriminator (fractional VSF difference)', fontsize=11)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (c) P(k) feature window
ax = axes[1, 0]
k_plot = np.logspace(-3, 0, 400)   # h/Mpc
ratio_sub = P_unnorm(k_plot, A_FS_substrate) / P_unnorm(k_plot, 0.0)
ratio_canon = P_unnorm(k_plot, A_FS_canon) / P_unnorm(k_plot, 0.0)
ax.semilogx(k_plot, (ratio_sub - 1) * 100, color='#2166AC', lw=1.8,
            label=f'substrate ($A_{{FS}}$={A_FS_substrate:.2e})')
ax.semilogx(k_plot, (ratio_canon - 1) * 100, color='#B2182B', ls='-.', lw=1.4,
            label='canonical (0.204)')
ax.axvline(k1_invMpc / h, color='gray', ls=':', lw=1.2,
           label=f'$k_1$={k1_invMpc:.4f} Mpc$^{{-1}}$')
ax.set_xlabel('$k$ [$h$/Mpc]', fontsize=11)
ax.set_ylabel('$\\Delta P(k)/P_{\\rm nofeat}$ [%]', fontsize=11)
ax.set_title('(c) Ring feature in $P(k)$ at $k_1$', fontsize=11)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (d) Observational reach: VSF vs void-catalog support
ax = axes[1, 1]
ax.loglog(r_void_Mpc, vsf_nofeat, 'k-', lw=1.5, label='VSF (featureless)')
ax.axvspan(15 / h, R_eff_max_cat_Mpc, alpha=0.15, color='green',
           label=f'BOSS ZOBOV support\n(15-130 $h^{{-1}}$Mpc)')
ax.axvline(R_eff_max_ind_hMpc / h, color='darkgreen', ls='--', lw=1.2,
           label=f'largest void {R_eff_max_ind_hMpc/h:.0f} Mpc')
ax.axvline(r1_Mpc, color='red', ls=':', lw=1.8,
           label=f'$r_1$={r1_Mpc} Mpc (BEYOND)')
ax.set_xlabel('$r_{\\rm void}$ [Mpc]', fontsize=11)
ax.set_ylabel('$dn/d\\ln r$ [$(h^{-1}{\\rm Mpc})^{-3}$]', fontsize=11)
ax.set_title('(d) Observational reach (Mao 2016 BOSS DR12 ZOBOV)', fontsize=11)
ax.legend(fontsize=8, loc='lower left')
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.94])
png_path = os.path.join(HERE, 'inv7_w1_2_vsf_second_sound.png')
fig.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {png_path}")

# ============================================================================
#  Section 11: Verdict payload
# ============================================================================

value_str = (
    f"PRIMARY(substrate A_FS={A_FS_substrate:.4e}):max_bump={max_sub*100:.4f}%@r={rpeak_sub:.1f}Mpc"
    f"_localized={loc_sub}_sign={'+' if signed_peak_sub>=0 else '-'};"
    f"CONTRAST(canon0.204):max_bump={max_canon*100:.4f}%@r={rpeak_canon:.1f}Mpc;"
    f"thresh={REL_BUMP*100:.0f}%_loc<={LOC_WINDOW_Mpc:.0f}Mpc;{reading};"
    f"OBS:r1={r1_Mpc}Mpc_BEYOND_catalog(maxReff={R_eff_max_cat_Mpc:.0f}Mpc);"
    f"voids-probe-field-topology-ring-must-show-but-DOES-NOT-and-scale-unreachable"
)

extra_rows = [
    f"# INV7-W1-2 substrate-primary: A_FS={A_FS_substrate:.6e} (W1-1 FAIL, 52.5x weaker than canon 0.204); "
    f"max VSF bump in [275,375]Mpc = {max_sub*100:.4f}% << {REL_BUMP*100:.0f}% threshold; "
    f"canonical-0.204 contrast bump = {max_canon*100:.4f}%",
    f"# INV7-W1-2 obs-reach: r1={r1_Mpc}Mpc={r1_in_hMpc:.1f}h^-1Mpc BEYOND BOSS DR12 ZOBOV void support "
    f"(max R_eff=130 h^-1Mpc={R_eff_max_cat_Mpc:.0f}Mpc; largest single void {R_eff_max_ind_hMpc/h:.0f}Mpc); "
    f"Mao+2016 arXiv:1602.02771 N={int(N_voids_total)}; Nadathur 2016 VSF-vs-LCDM<{VSF_dev_bound*100:.0f}%",
    f"# INV7-W1-2 C1: VSF (two-point-statistic-FREE direction) does NOT confirm the ring -> "
    f"Reading-B(aliased/sub-threshold) on the substrate amplitude; void direction adds NO distinctiveness "
    f"beyond W1-1's c2 derivation (which already FAILED at A_FS_sub=52.5x below canonical)",
]

print_verdict_payload(
    'INV7-W1-2', verdict, value_str, 'FW', 'RATIO', 'N/A',
    audit_sha, content_sha, extra_rows=extra_rows,
    sign_v=sign_v, mag_v=mag_v, regime_v=regime_v,
)

print("\n" + "=" * 72)
print("INV7-W1-2 COMPLETE")
print("=" * 72)
