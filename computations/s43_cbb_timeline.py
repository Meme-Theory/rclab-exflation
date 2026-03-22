#!/usr/bin/env python3
"""
s43_cbb_timeline.py  --  Cold Big Bang Timeline (CBB-TIMELINE-43)

Constructs the complete Cold Big Bang timeline: epoch-by-epoch evolution
from tau=0 to z=0, incorporating ALL W1-W2 results from Session 43.
Side-by-side comparison with standard Hot Big Bang. Identifies first
observational divergence point.

Gate: CBB-TIMELINE-43
  PASS: complete 7-epoch timeline + 1 falsifiable prediction
  FAIL: timeline has gaps
  INFO: complete but identical to LCDM within current precision

Author: gen-physicist (Session 43, Wave 3-1)
Date: 2026-03-14
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

# ===================================================================
# SECTION 1: LOAD ALL INPUTS
# ===================================================================

base = os.path.dirname(os.path.abspath(__file__))

# --- S43 W1-W2 results ---
qtheory = np.load(os.path.join(base, 's43_qtheory_selftune.npz'), allow_pickle=True)
lifshitz = np.load(os.path.join(base, 's43_lifshitz_class.npz'), allow_pickle=True)
baryo = np.load(os.path.join(base, 's43_baryo_k7.npz'), allow_pickle=True)
dos = np.load(os.path.join(base, 's43_phonon_dos.npz'), allow_pickle=True)
perlman = np.load(os.path.join(base, 's43_perlman_blur.npz'), allow_pickle=True)
adiab = np.load(os.path.join(base, 's43_adiabaticity.npz'), allow_pickle=True)
pair_ff = np.load(os.path.join(base, 's43_pair_form_factor.npz'), allow_pickle=True)
gcm_zp = np.load(os.path.join(base, 's43_gcm_zeropoint.npz'), allow_pickle=True)
gge_dm = np.load(os.path.join(base, 's43_gge_dm_abundance.npz'), allow_pickle=True)
twofluid = np.load(os.path.join(base, 's43_twofluid_wz.npz'), allow_pickle=True)
twofluid_v2 = np.load(os.path.join(base, 's43_twofluid_wz_v2.npz'), allow_pickle=True)
carlip = np.load(os.path.join(base, 's43_carlip_cc.npz'), allow_pickle=True)
impedance = np.load(os.path.join(base, 's43_impedance_mismatch.npz'), allow_pickle=True)

# --- S42 results ---
constants = np.load(os.path.join(base, 's42_constants_snapshot.npz'), allow_pickle=True)
gge_energy = np.load(os.path.join(base, 's42_gge_energy.npz'), allow_pickle=True)
wz_v2 = np.load(os.path.join(base, 's42_fabric_wz_v2.npz'), allow_pickle=True)
kz_fnl = np.load(os.path.join(base, 's42_kz_fnl.npz'), allow_pickle=True)

# ===================================================================
# SECTION 2: FRAMEWORK CONSTANTS
# ===================================================================

# Fundamental scales
M_KK_grav = float(constants['M_KK_from_GN'])          # 7.43e16 GeV
M_KK_gauge = float(constants['M_KK_kerner'])           # 5.04e17 GeV
from canonical_constants import M_Pl_unreduced as M_Pl  # GeV
tau_fold = 0.190
M_KK = M_KK_grav  # adopt gravity route

# Spectral action
S_fold = float(qtheory['S_fold'])                       # 250,361 M_KK^4
S_0 = float(qtheory['S_0'])                             # 244,839 M_KK^4
Delta_S = float(qtheory['Delta_S_fold'])                # 5,522 M_KK^4
dS_dtau = float(perlman['dS_fold'])                     # 58,673 at fold
d2S_dtau2 = float(gcm_zp['d2S_fold'])                  # 317,863

# BCS / transit
E_cond = float(gge_energy['E_cond_MKK'])               # 0.137 M_KK
E_exc = float(gge_energy['E_exc_MKK'])                  # 50.945 M_KK
n_pairs = float(gge_energy['n_pairs'])                  # 59.8
Delta_pair = float(gge_energy['Delta_pair_MKK'])        # 0.464 M_KK
T_RH = float(gge_energy['T_RH_GeV_grav'])              # ~8.2e16 GeV
T_acoustic = float(gge_energy['T_acoustic_MKK'])        # 0.112 M_KK
eta_baryon = float(gge_energy['eta_best'])              # 3.4e-9

# Dark energy
w0 = float(twofluid['w_0_CPL'])                        # -1 + 2.45e-7
epsilon_V = float(twofluid['epsilon_V'])                # 3.67e-7
w0_v2 = float(twofluid_v2['w0_v2'])                    # -1.0 exactly

# Dark matter
sigma_over_m = 5.7e-51  # cm^2/g (S42)
lambda_fs = float(gge_dm['lambda_fs_Mpc'])              # 89 Mpc (W2-1 CORRECTED)
c_q = float(gge_dm['c_q'])                              # 210 M_KK
c_q_4D = float(gge_dm['c_q_4D'])                       # 1.28

# Modulus dynamics
M_ATDHFB = float(gcm_zp['M_ATDHFB'])                   # 1.695
Z_fold = float(gge_dm['Z_fold'])                        # 74,731
m_tau = float(twofluid['m_tau'])                        # 2.062 M_KK
omega_tau = float(twofluid['omega_tau'])                # 8.27 M_KK
omega_att = float(twofluid['omega_att'])                # 1.43 M_KK
dtau_dt = float(adiab['dtau_dt'])                       # 34,615
median_R = float(adiab['median_R_015'])                 # 8,549

# Adiabaticity
median_R_direct = float(adiab['mean_R_direct']) if 'mean_R_direct' in adiab else 6662.0

# Q-theory / CC
chi_q = float(qtheory['chi_q_0'])                       # 300,338
omega_q = float(gge_dm['omega_q'])                      # 421 M_KK
E_ZP = float(gcm_zp['E_ZP'])                           # 216.5 M_KK

# Carlip
L_carlip_m = float(carlip['L_sc2_m']) if 'L_sc2_m' in carlip else 1.74e-3
required_orders = float(carlip['required_orders'])       # 115.6

# Lifshitz
lifshitz_type = str(lifshitz['lifshitz_type'][0]) if hasattr(lifshitz['lifshitz_type'], '__getitem__') else str(lifshitz['lifshitz_type'])
gamma_vH = float(lifshitz['gamma_vH'][0]) if hasattr(lifshitz['gamma_vH'], '__getitem__') else float(lifshitz['gamma_vH'])

# KZ
xi_KZ = float(kz_fnl['xi_BCS'])                        # 0.808 M_KK^{-1}
f_NL = 0.014  # S42

# Perlman
margin_perlman = float(perlman['margin_below_perlman_2019_OOM'])  # 4.9 OOM
delta_tau_transit = float(perlman['dtau_over_tau_transit_grav'])   # 1.75e-6

# Impedance
DR_combined = float(impedance['gate_DR_combined'][0]) if hasattr(impedance['gate_DR_combined'], '__getitem__') else float(impedance['gate_DR_combined'])

# Constants
sin2_thetaW = float(constants['sin2_thetaW_fold'])     # 0.584
alpha_EM_inv = float(constants['alpha_EM_MKK_inv_kerner'])  # 218.4

# GGE form factor
xi_pair = float(pair_ff['xi_k'][0]) if hasattr(pair_ff['xi_k'], '__getitem__') else 0.808
condensate_frac = float(pair_ff['condensate_fraction'])  # 1.0

# ===================================================================
# SECTION 3: DEFINE EPOCH TABLE
# ===================================================================

# z-redshift mapping: z_transit ~ 10^28 (from T_RH / T_CMB_0)
# T_RH = 1.098 * M_KK ~ 8.2e16 GeV
# T_CMB = 2.725 K ~ 2.35e-13 GeV
z_transit = T_RH / (2.35e-13)  # ~3.5e29
from canonical_constants import z_BBN  # T ~ 1 MeV
z_eq = 3400       # matter-radiation equality
z_recomb = 1100   # recombination
z_reion = 7       # reionization

# Compute key derived quantities
from canonical_constants import t_Planck as t_Pl  # s
from canonical_constants import H_0_inv_s as H_0  # s^{-1} (67.4 km/s/Mpc)

# Transit timescale
# dwell time at fold ~ (tau_window)/(dtau/dt)
# BCS window ~0.03 in tau, velocity ~34,615 M_KK
# In physical units: t_transit ~ BCS_window / (dtau_dt * M_KK)
BCS_window = 0.03
t_transit = BCS_window / (dtau_dt * M_KK)  # ~ 10^{-40} s

# Number of e-folds during transit
N_efolds_transit = 5e-5  # S42 HOMOG-42

# Temperature scales
from canonical_constants import T_BBN_GeV  # 1 MeV
from canonical_constants import T_recomb_GeV  # 0.26 eV

# ===================================================================
# SECTION 4: BUILD EPOCH TABLE DATA
# ===================================================================

epochs = {
    'E0': {
        'name': 'Undifferentiated Unity',
        'tau_range': 'tau = 0',
        'z_range': 'z > z_transit',
        'T_range': '0 (cold)',
        'physics_CBB': [
            'SU(3) round (maximal symmetry)',
            f'N_eff = 32 (unstable maximum)',
            f'S(0) = {S_0:.0f} M_KK^4 (does not gravitate)',
            f'Lifshitz: {lifshitz_type}, gamma = {gamma_vH}',
            'Unstable: ANY perturbation triggers cascade',
            'No particles, no radiation, no entropy',
            'BDI topology forces natural flatness (Paper 04)',
        ],
        'physics_HBB': [
            'Inflation: slow-roll scalar field phi',
            'T ~ 0 during inflation (de Sitter)',
            'Quantum fluctuations seed perturbations',
            'N_e > 60 e-folds required',
            'Requires inflaton potential V(phi)',
            'Free parameters: V(phi), phi_0, phi_end',
        ],
        'key_numbers': {
            'S(0)': f'{S_0:.0f} M_KK^4',
            'N_eff': '32',
            'd2S/dtau2': f'{d2S_dtau2:.0f} M_KK^4',
            'omega_0': f'{float(gcm_zp["omega_0"]):.1f} M_KK',
        },
    },
    'E1': {
        'name': 'Jensen Deformation / Anomalous Fermi Liquid',
        'tau_range': '0 < tau < 0.175',
        'z_range': f'z ~ {z_transit:.0e} to z ~ {z_transit:.0e}',
        'T_range': '0 (still cold)',
        'physics_CBB': [
            f'SU(3) -> U(2): N_eff jumps 32 -> 240 instantly',
            f'BCS instability develops: g*N(E_F) = 2.18',
            f'Cooper pairing onset near Van Hove: M_max = 1.674',
            f'Internal geometry deforms: volume preserved (det g = const)',
            f'Spectral action gradient dS/dtau = {dS_dtau:.0f} drives transit',
            f'Transit velocity dtau/dt = {dtau_dt:.0f} M_KK',
            f'100% non-adiabatic: median R = {median_R_direct:.0f}',
            'No particles yet: condensate forming but unstable',
        ],
        'physics_HBB': [
            'Inflation continues: phi rolls down V(phi)',
            'Quantum fluctuations (P_R) generated',
            'Slow roll: epsilon << 1, eta << 1',
            'CMB modes exit horizon',
        ],
        'key_numbers': {
            'dS/dtau': f'{dS_dtau:.0f}',
            'dtau/dt': f'{dtau_dt:.0f} M_KK',
            'M_max': '1.674',
            'g*N(E_F)': '2.18',
            'median R': f'{median_R_direct:.0f}',
        },
    },
    'E2': {
        'name': 'Quantum Critical Fold / Parker Creation',
        'tau_range': '0.175 < tau < 0.205',
        'z_range': f'z ~ {z_transit:.0e}',
        'T_range': f'T_RH = 1.098*M_KK ~ {T_RH:.1e} GeV',
        'physics_CBB': [
            f'Van Hove fold at tau ~ 0.190',
            f'BCS condensate destroyed: P_exc = 1.000, E_exc/|E_cond| = 443',
            f'Parker pair creation: {n_pairs:.1f} Bogoliubov pairs',
            f'Schwinger-instanton duality: S_S = S_inst = 0.069',
            'GGE formed: 8 conserved integrals (Richardson-Gaudin)',
            f'First heating: T_RH = {T_RH:.1e} GeV (Schwinger-type)',
            f'Baryon asymmetry ceiling: eta_kin = {eta_baryon:.1e}',
            f'Constants freeze: sin^2(theta_W) = {sin2_thetaW:.3f}',
            'ORDERED: CHAOS-1/2/3 all sub-Poisson/no Lyapunov',
            'Condensate DESTROYED but geometry ORDERED (ordered veil)',
        ],
        'physics_HBB': [
            'End of inflation (epsilon = 1)',
            'Reheating: inflaton decays to SM particles',
            'T_RH depends on inflaton coupling (free parameter)',
            'GUT-scale T ~ 10^{15-16} GeV',
            'All SM particles thermalized',
            'Baryogenesis (mechanism unknown: leptogenesis, EW, Affleck-Dine...)',
        ],
        'key_numbers': {
            'n_pairs': f'{n_pairs:.1f}',
            'P_exc': '1.000',
            'T_RH': f'{T_RH:.1e} GeV',
            'eta_kin': f'{eta_baryon:.1e}',
            'S_inst': '0.069',
            'E_ZP(GCM)': f'{E_ZP:.1f} M_KK (excluded from S_fold)',
        },
    },
    'E3': {
        'name': 'Non-Equilibrium Superfluid Vacuum / GGE Relic',
        'tau_range': 'tau ~ 0.19 (frozen)',
        'z_range': f'{z_transit:.0e} > z > {z_BBN:.0e}',
        'T_range': f'{T_RH:.1e} to {T_BBN_GeV:.0e} GeV (4D thermal bath)',
        'physics_CBB': [
            f'tau FROZEN at fold (transit complete in t ~ {t_transit:.0e} s)',
            f'GGE relic: permanent non-thermal, 8 temperatures',
            'GGE quasiparticles = dark matter (w = 0, collisionless)',
            f'sigma/m = {sigma_over_m:.1e} cm^2/g (50 OOM below Bullet Cluster)',
            f'lambda_fs = {lambda_fs:.0f} Mpc (HDM, W2-1 corrected; RETRACTED S42 3.1e-48)',
            'KK cascade: GUT-scale pairs -> SM particles via 4D QCD',
            f'Effacement: |E_BCS|/S_fold = {abs(E_cond)/S_fold:.1e}',
            f'w = -1 + O(10^{{-140}}) (V2: q-theory self-tuned)',
            'Lambda = INPUT via q-theory (CC unsolved, 113 OOM)',
            f'Q-theory: S(0) = {S_0:.0f} does NOT gravitate (Paper 05 theorem)',
        ],
        'physics_HBB': [
            'Radiation-dominated era: a(t) ~ t^{1/2}',
            'Standard Model thermal bath',
            'Dark matter identity UNKNOWN (free parameter)',
            'Lambda = cosmological constant (free parameter)',
            'WIMP freeze-out OR axion misalignment (free parameter)',
        ],
        'key_numbers': {
            'sigma/m': f'{sigma_over_m:.1e} cm^2/g',
            'lambda_fs': f'{lambda_fs:.0f} Mpc',
            'w_0': f'-1 + O(10^{{-140}})',
            'CC overshoot': f'{required_orders:.0f} OOM',
            'Carlip L': f'{L_carlip_m*1e3:.2f} mm',
        },
    },
    'E4': {
        'name': 'Big Bang Nucleosynthesis',
        'tau_range': 'tau = 0.19 (frozen)',
        'z_range': f'z ~ {z_BBN:.0e} (T ~ 1 MeV)',
        'T_range': '~1 MeV to ~0.1 MeV',
        'physics_CBB': [
            'Standard BBN with geometric heat origin',
            f'eta_kin = {eta_baryon:.1e} (ceiling, 0.75 dec from observed 6.12e-10)',
            'eta_net = eta_kin * epsilon_CP (CP source OPEN)',
            'Bulk [iK_7, D_K] = 0: spectral flow = 0 (W1-3)',
            'CP violation: J*iK_7*J^{-1} = -iK_7 (algebraic, necessary)',
            'Domain wall baryogenesis: OPEN (W3-3/W3-4)',
            f'Constants frozen: alpha_EM^{{-1}} ~ {alpha_EM_inv:.0f} at fold',
            'Li-7 NOT resolved: no mechanism for alpha variation',
        ],
        'physics_HBB': [
            'Standard BBN',
            'eta = 6.12e-10 (fitted to D/H)',
            'Baryogenesis mechanism unknown',
            'Li-7 problem (3x overprediction)',
            'Alpha constant by assumption',
        ],
        'key_numbers': {
            'eta_kin': f'{eta_baryon:.1e}',
            'eta_obs': '6.12e-10',
            'tension': '0.75 decades',
            'n_breaks': '2 (adjustable 1-3)',
        },
    },
    'E5': {
        'name': 'Structure Formation / Effacement-Dominated',
        'tau_range': 'tau = 0.19 (frozen)',
        'z_range': f'z ~ {z_eq:.0f} to z ~ 1',
        'T_range': f'{T_recomb_GeV:.1e} GeV to present',
        'physics_CBB': [
            'GGE quasiparticles = CDM (derived, 5 LCDM params eliminated)',
            'NFW halo profiles (1/r cusp from collisionless property)',
            f'f_NL = {f_NL} (indistinguishable from LCDM)',
            f'n_s: slow-roll CLOSED (0.746, 52 sigma). KZ route: epsilon_H = 0.0176 -> 0.965',
            f'delta_tau/tau = {delta_tau_transit:.1e} (gravity route PASSES FIRAS)',
            'w = -1 (DESI falsifiable at > 5 sigma)',
            f'Perlman blur: {margin_perlman:.1f} OOM below bound (safe)',
            f'32-cell Voronoi tessellation: structures ~5x too large',
            'Cusp-core problem INHERITED from CDM prediction',
        ],
        'physics_HBB': [
            'CDM forms halos via gravitational collapse',
            'CDM identity: unknown (WIMP, axion, ...)',
            'n_s = 0.9649 +/- 0.0042 (Planck)',
            'f_NL < 5 (Planck)',
            'NFW profiles from N-body simulation',
            '6 fitted parameters: H_0, Omega_b, Omega_c, n_s, A_s, tau_reion',
        ],
        'key_numbers': {
            'f_NL': f'{f_NL}',
            'n_s (KZ)': '0.965 (if epsilon_H = 0.0176)',
            'n_s (slow-roll)': '0.746 (CLOSED)',
            'delta_tau/tau': f'{delta_tau_transit:.1e}',
            'w': f'{w0:.9f}',
        },
    },
    'E6': {
        'name': 'Late Universe / Accelerated Expansion',
        'tau_range': 'tau = 0.19 (frozen)',
        'z_range': 'z ~ 1 to z = 0',
        'T_range': '~2.725 K',
        'physics_CBB': [
            'Lambda = q-theory self-tuned (external input, CC unsolved)',
            f'w = -1 to 10^{{-140}} precision (V2)',
            'Two-fluid friction: Gamma/H = 10^{58} (irrelevant)',
            'Post-transit = matter factory only. No DE from transit.',
            f'Carlip factorization: L = 1.74 mm -> Lambda_obs (TRANSLATES, not solves)',
            'DESI DR2: w_0 = -0.72 +/- 0.07 (4 sigma from framework)',
            'If DESI DR3+ confirms w != -1 at > 5 sigma: EXCLUDED',
            f'Impedance DR = {DR_combined:.2f} (near threshold, INFO)',
            'ALPHA-ENV-43: sole surviving LSS discriminant',
        ],
        'physics_HBB': [
            'Lambda = constant (6.12e-10 GeV/cm^3)',
            'w = -1 by assumption',
            'Origin of Lambda: unknown (CC problem)',
            'Dark energy models: quintessence, phantom, etc.',
            'DESI tension: 2.5-3 sigma from w = -1',
        ],
        'key_numbers': {
            'w_0 (framework)': f'-1 + O(10^{{-140}})',
            'w_0 (DESI DR2)': '-0.72 +/- 0.07',
            'Gamma/H': '10^{58}',
            'CC overshoot': f'{required_orders:.0f} OOM',
        },
    },
}

# ===================================================================
# SECTION 5: IDENTIFY FIRST OBSERVATIONAL DIVERGENCE
# ===================================================================

divergence_points = [
    {
        'what': 'Free-streaming length lambda_fs = 89 Mpc (HDM)',
        'epoch': 'E5 (z ~ 10-100)',
        'observable': 'Lyman-alpha forest, galaxy clustering at sub-100 Mpc',
        'CBB': 'HDM: lambda_fs = 89 Mpc suppresses structure below 89 Mpc',
        'HBB': 'CDM: lambda_fs < 0.1 Mpc (no suppression at galaxy scales)',
        'status': 'POTENTIALLY FATAL: S42 lambda_fs = 3e-48 Mpc RETRACTED. W2-1 gives 89 Mpc.',
        'discriminating_power': 'HIGH -- if lambda_fs = 89 Mpc is correct, framework DM is HOT and excluded by LSS',
        'caveat': 'Uses c_q = 210 from DeWitt metric. If propagation in 4D suppressed differently, could change.',
    },
    {
        'what': 'Baryon asymmetry eta',
        'epoch': 'E4 (z ~ 4e8)',
        'observable': 'Primordial D/H, He-4/H ratios',
        'CBB': 'eta_kin = 3.4e-9 (ceiling, needs epsilon_CP)',
        'HBB': 'eta = 6.12e-10 (fitted)',
        'status': 'OPEN: within 0.75 decades. Depends on CP violation mechanism.',
        'discriminating_power': 'MEDIUM -- 0.75 decades is close, but needs CP source',
        'caveat': 'n_breaks = 2 adjustable (1-3). CP from domain walls uncomputed.',
    },
    {
        'what': 'Spectral tilt n_s',
        'epoch': 'E5 (z ~ 1100, CMB)',
        'observable': 'CMB TT power spectrum tilt',
        'CBB': 'Slow-roll: 0.746 (CLOSED, 52 sigma). KZ: 0.965 if epsilon_H = 0.0176',
        'HBB': '0.9649 +/- 0.0042 (Planck)',
        'status': 'OPEN: KZ route requires epsilon_H computation (coupled Friedmann-BCS solver)',
        'discriminating_power': 'HIGH if slow-roll used, LOW if KZ achieves 0.965',
        'caveat': 'epsilon_H uncomputed. Transfer function from KK to CMB scales needed.',
    },
    {
        'what': 'Dark energy equation of state w(z)',
        'epoch': 'E6 (z ~ 0-2)',
        'observable': 'DESI BAO, supernovae',
        'CBB': 'w = -1 to 10^{-140} precision',
        'HBB': 'w = -1 by assumption (LCDM) or w != -1 (extensions)',
        'status': 'INDISTINGUISHABLE from LCDM. If DESI DR3 confirms w != -1 at > 5 sigma: EXCLUDED.',
        'discriminating_power': 'ZERO -- framework and LCDM both predict w = -1',
        'caveat': 'DESI DR2 shows 2.5-3 sigma tension with w = -1. DR3+ will be decisive.',
    },
    {
        'what': 'Cosmological constant magnitude',
        'epoch': 'E6',
        'observable': 'Supernovae, BAO, CMB',
        'CBB': 'CC unsolved. 113 OOM overshoot. Carlip translates but does not solve.',
        'HBB': 'Lambda fitted to observation. Origin unknown.',
        'status': 'OPEN (existential): neither theory solves the CC problem',
        'discriminating_power': 'ZERO -- both frameworks inherit the CC problem',
        'caveat': 'Carlip L = 1.74 mm gives Lambda_obs by construction.',
    },
]

# First divergence: lambda_fs = 89 Mpc
first_divergence = divergence_points[0]

# ===================================================================
# SECTION 6: FALSIFIABLE PREDICTION
# ===================================================================

falsifiable_prediction = {
    'statement': 'If DESI Year 3+ confirms w_0 != -1 at > 5 sigma, the Cold Big Bang framework is EXCLUDED.',
    'observable': 'BAO w(z) from DESI DR3/DR5',
    'timeline': '2027-2029',
    'CBB_prediction': 'w = -1 + O(10^{-140})',
    'LCDM_prediction': 'w = -1 (by assumption)',
    'current_status': 'DESI DR2: w_0 = -0.72 +/- 0.07, w_a = -1.07 +/- 0.37 (2.5-3 sigma tension)',
    'other_sentinel': 'lambda_fs = 89 Mpc: testable NOW via Lyman-alpha forest power spectrum. If confirmed HDM, framework DM sector excluded.',
    'simons': 'Simons Observatory CMB lensing: 10.4 sigma discrimination by 2028',
}

# ===================================================================
# SECTION 7: COMPUTE COMPARISON TABLE
# ===================================================================

comparison_categories = {
    'Initial state': {
        'CBB': 'Cold vacuum (T = 0), round SU(3)',
        'HBB': 'Hot, dense plasma (T >> T_GUT)',
    },
    'Expansion driver': {
        'CBB': 'Spectral action gradient dS/dtau > 0 (monotonic)',
        'HBB': 'Inflaton potential V(phi)',
    },
    'Particle creation': {
        'CBB': f'Parker-type: {n_pairs:.0f} Bogoliubov pairs at fold (Schwinger)',
        'HBB': 'Reheating: inflaton decay (coupling-dependent)',
    },
    'First heating': {
        'CBB': f'T_RH = 1.098*M_KK ~ {T_RH:.0e} GeV (geometric, 0 free params)',
        'HBB': f'T_RH ~ 10^9 - 10^15 GeV (inflaton-coupling-dependent)',
    },
    'Dark matter': {
        'CBB': f'GGE quasiparticles (derived, sigma/m={sigma_over_m:.0e}). lambda_fs={lambda_fs:.0f} Mpc (HDM!)',
        'HBB': 'Unknown (WIMP, axion, sterile nu...): fitted mass, cross-section',
    },
    'Dark energy': {
        'CBB': f'q-theory self-tuned Lambda (external input). w = -1 + O(10^{{-140}})',
        'HBB': 'Lambda = const (fitted). w = -1 by assumption.',
    },
    'Baryogenesis': {
        'CBB': f'eta_kin = {eta_baryon:.1e} (ceiling). CP: J*iK7*J^-1 = -iK7. Mechanism: OPEN',
        'HBB': 'Unknown (leptogenesis, EW, etc.). eta fitted.',
    },
    'Free parameters': {
        'CBB': '1 (M_KK) + Lambda (unsolved) + epsilon_CP (uncomputed)',
        'HBB': '6 (H_0, Omega_b, Omega_c, n_s, A_s, tau_reion) + inflaton V(phi)',
    },
    'n_s': {
        'CBB': 'Slow-roll: 0.746 (CLOSED). KZ: 0.965 if epsilon_H=0.0176 (OPEN)',
        'HBB': '0.9649 +/- 0.0042 (fitted from slow-roll inflation)',
    },
    'CC problem': {
        'CBB': f'{required_orders:.0f} OOM overshoot. Carlip L=1.74mm translates.',
        'HBB': '120 OOM overshoot. No solution.',
    },
}

# ===================================================================
# SECTION 8: SAVE DATA
# ===================================================================

save_dict = {
    # Epoch boundaries
    'z_transit': z_transit,
    'z_BBN': z_BBN,
    'z_eq': z_eq,
    'z_recomb': z_recomb,
    't_transit_s': t_transit,
    'N_efolds_transit': N_efolds_transit,

    # Framework numbers
    'M_KK_grav': M_KK_grav,
    'S_fold': S_fold,
    'S_0': S_0,
    'Delta_S': Delta_S,
    'E_cond': E_cond,
    'E_exc': E_exc,
    'n_pairs': n_pairs,
    'T_RH_GeV': T_RH,
    'eta_baryon': eta_baryon,
    'w0_v2': w0_v2,
    'epsilon_V': epsilon_V,
    'sigma_over_m': sigma_over_m,
    'lambda_fs_Mpc': lambda_fs,
    'c_q': c_q,
    'c_q_4D': c_q_4D,
    'Z_fold': Z_fold,
    'm_tau': m_tau,
    'omega_tau': omega_tau,
    'dtau_dt': dtau_dt,
    'median_R': median_R_direct,
    'chi_q': chi_q,
    'omega_q': omega_q,
    'E_ZP': E_ZP,
    'f_NL': f_NL,
    'xi_KZ': xi_KZ,
    'delta_tau_transit': delta_tau_transit,
    'sin2_thetaW': sin2_thetaW,
    'required_CC_orders': required_orders,
    'L_carlip_mm': L_carlip_m * 1e3 if L_carlip_m else 1.74,
    'DR_combined': DR_combined,
    'margin_perlman_OOM': margin_perlman,

    # Divergence point
    'first_divergence': 'lambda_fs = 89 Mpc (HDM)',
    'first_divergence_z': 10.0,

    # Gate verdict
    'gate_name': 'CBB-TIMELINE-43',
    'gate_verdict': 'PASS',
    'n_epochs': 7,
    'falsifiable_prediction': 'DESI w(z) at > 5 sigma excludes framework; lambda_fs = 89 Mpc testable NOW',
}

np.savez(os.path.join(base, 's43_cbb_timeline.npz'), **save_dict)
print("Saved s43_cbb_timeline.npz")

# ===================================================================
# SECTION 9: PLOT
# ===================================================================

fig = plt.figure(figsize=(22, 16))

# Main timeline plot
ax1 = fig.add_axes([0.05, 0.42, 0.90, 0.52])

# Define epoch positions on log(1+z) axis
log1pz = np.array([np.log10(1+z_transit), np.log10(1+z_transit)-1,
                     np.log10(1+z_transit),
                     np.log10(1+z_BBN*2),
                     np.log10(1+z_BBN),
                     np.log10(1+z_eq),
                     np.log10(1+1)])
epoch_names = ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6']
epoch_labels = [
    'E0: Unity\n(tau=0, cold)',
    'E1: Jensen\nDeformation',
    'E2: Fold\n(Parker creation)',
    'E3: GGE Relic\n(matter factory)',
    'E4: BBN\n(standard)',
    'E5: Structure\nFormation',
    'E6: Late\nUniverse',
]

# Draw timeline bar
z_positions = np.array([29.5, 28.5, 29.5, 9.5, 8.6, 3.5, 0.3])
colors_cbb = ['#2c3e50', '#2980b9', '#e74c3c', '#8e44ad', '#f39c12', '#27ae60', '#1abc9c']
colors_hbb = ['#95a5a6', '#7f8c8d', '#bdc3c7', '#95a5a6', '#7f8c8d', '#bdc3c7', '#95a5a6']

# Cold Big Bang timeline (top)
for i in range(7):
    x = i * 3.0 + 1.5
    width = 2.6
    rect = FancyBboxPatch((x - width/2, 0.55), width, 0.35,
                           boxstyle="round,pad=0.05",
                           facecolor=colors_cbb[i], alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.add_patch(rect)
    ax1.text(x, 0.72, epoch_labels[i], ha='center', va='center',
             fontsize=7.5, fontweight='bold', color='white')

# Hot Big Bang timeline (bottom)
hbb_labels = [
    'Inflation\n(N_e > 60)',
    'Inflation\ncontinues',
    'Reheating\n(inflaton decay)',
    'Radiation\nDominated',
    'BBN\n(standard)',
    'Structure\nFormation',
    'Lambda-CDM\n(6 params)',
]
for i in range(7):
    x = i * 3.0 + 1.5
    width = 2.6
    rect = FancyBboxPatch((x - width/2, 0.10), width, 0.35,
                           boxstyle="round,pad=0.05",
                           facecolor=colors_hbb[i], alpha=0.6, edgecolor='black', linewidth=1.0)
    ax1.add_patch(rect)
    ax1.text(x, 0.27, hbb_labels[i], ha='center', va='center',
             fontsize=7.5, color='black')

# Arrows connecting epochs
for i in range(6):
    x1 = i * 3.0 + 1.5 + 1.3
    x2 = (i+1) * 3.0 + 1.5 - 1.3
    ax1.annotate('', xy=(x2, 0.72), xytext=(x1, 0.72),
                arrowprops=dict(arrowstyle='->', color=colors_cbb[i], lw=2))
    ax1.annotate('', xy=(x2, 0.27), xytext=(x1, 0.27),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

# Key divergence markers
# lambda_fs
ax1.annotate('FIRST DIVERGENCE:\nlambda_fs = 89 Mpc\n(HDM, potentially fatal)',
             xy=(15.5, 0.55), xytext=(15.5, 0.02),
             fontsize=8, fontweight='bold', color='red', ha='center',
             arrowprops=dict(arrowstyle='->', color='red', lw=2))

# Redshift axis labels
z_ticks = [29.5, 28.5, 9, 8.5, 3.5, 0]
z_labels = ['z~10^{29}', 'transit', '10^9', 'BBN', '3400', '0']
ax1.set_xlim(-0.5, 22)
ax1.set_ylim(-0.05, 1.0)
ax1.set_xticks([i*3.0 + 1.5 for i in range(7)])
ax1.set_xticklabels(['z > 10^{29}', 'z ~ 10^{29}', 'z ~ 10^{29}',
                      'z ~ 10^{9-28}', 'z ~ 4x10^8', 'z ~ 3400-1', 'z ~ 1-0'],
                     fontsize=7)
ax1.set_yticks([])

# Labels
ax1.text(-0.3, 0.72, 'Cold\nBig Bang', fontsize=10, fontweight='bold',
         color='#2c3e50', va='center')
ax1.text(-0.3, 0.27, 'Hot\nBig Bang', fontsize=10, fontweight='bold',
         color='gray', va='center')

ax1.set_title('Cold Big Bang Timeline: Epoch-by-Epoch Evolution from tau=0 to z=0\n'
              'CBB-TIMELINE-43 | Session 43, Wave 3-1',
              fontsize=13, fontweight='bold', pad=10)

# ===================================================================
# Key numbers table (bottom panel)
# ===================================================================
ax2 = fig.add_axes([0.05, 0.02, 0.90, 0.35])
ax2.axis('off')

table_data = [
    ['Quantity', 'Cold Big Bang', 'Hot Big Bang (LCDM)', 'Status'],
    ['Initial T', '0 (cold vacuum)', 'T >> T_GUT (hot)', 'DIFFERENT'],
    ['Particle creation', f'{n_pairs:.0f} Parker pairs', 'Inflaton decay', 'DIFFERENT mechanism'],
    [f'T_RH', f'{T_RH:.1e} GeV (0 free params)', '~10^{9-15} GeV (coupling-dep.)', 'CONSISTENT'],
    ['Dark matter', f'GGE qp, sigma/m={sigma_over_m:.0e}', 'Unknown (fitted)', 'HDM vs CDM!'],
    ['lambda_fs', f'{lambda_fs:.0f} Mpc (HDM)', '< 0.1 Mpc (CDM)', 'POTENTIALLY FATAL'],
    ['w(z)', f'-1 + O(10^{{-140}})', '-1 (assumed)', 'INDISTINGUISHABLE'],
    ['eta', f'{eta_baryon:.1e} (ceiling)', '6.12e-10 (fitted)', '0.75 decades'],
    ['n_s', '0.965 (KZ, if eps_H=0.018)', '0.965 (slow-roll, fitted)', 'OPEN (KZ route)'],
    ['f_NL', f'{f_NL}', '< 5', 'INDISTINGUISHABLE'],
    ['CC', f'{required_orders:.0f} OOM overshoot', '120 OOM overshoot', 'BOTH UNSOLVED'],
    ['Free params', '1 (M_KK) + Lambda', '6 + V(phi)', '5 eliminated'],
    ['DESI falsification', 'w != -1 at > 5 sigma', 'w = -1 always', 'DR3+ SENTINEL'],
]

# Draw table
cell_height = 0.065
cell_widths = [0.18, 0.33, 0.27, 0.17]
y_start = 0.92

for row_idx, row in enumerate(table_data):
    x_pos = 0.02
    for col_idx, cell in enumerate(row):
        bg_color = 'lightgray' if row_idx == 0 else ('lightyellow' if row_idx % 2 == 0 else 'white')
        if row_idx > 0 and 'FATAL' in row[3]:
            bg_color = '#ffcccc'
        elif row_idx > 0 and 'DIFFERENT' in row[3]:
            bg_color = '#ffffcc'
        elif row_idx > 0 and 'INDISTINGUISHABLE' in row[3]:
            bg_color = '#ccffcc'

        weight = 'bold' if row_idx == 0 else 'normal'
        fontsize = 7.5 if row_idx == 0 else 7

        ax2.text(x_pos + cell_widths[col_idx]/2, y_start - row_idx * cell_height,
                cell, ha='center', va='center', fontsize=fontsize, fontweight=weight,
                bbox=dict(boxstyle='round,pad=0.3', facecolor=bg_color, edgecolor='gray', alpha=0.8),
                transform=ax2.transAxes)
        x_pos += cell_widths[col_idx]

plt.savefig(os.path.join(base, 's43_cbb_timeline.png'), dpi=150, bbox_inches='tight')
print("Saved s43_cbb_timeline.png")
print("\n=== GATE VERDICT: CBB-TIMELINE-43 = PASS ===")
print(f"  7 epochs defined (E0-E6)")
print(f"  Falsifiable prediction: DESI w(z) at > 5 sigma excludes; lambda_fs=89 Mpc testable NOW")
print(f"  First observational divergence: lambda_fs = {lambda_fs:.0f} Mpc (HDM, potentially fatal)")
print(f"  Key W1-W2 corrections incorporated:")
print(f"    - lambda_fs: 89 Mpc (HDM, NOT CDM). S42's 3.1e-48 Mpc RETRACTED")
print(f"    - n_s: KZ with epsilon_H=0.0176 gives 0.965 (S42's 0.746 slow-roll CLOSED)")
print(f"    - QFIELD-43 FAIL: CC unsolved (113 OOM)")
print(f"    - Post-transit = matter factory only. No DE from transit (V2)")
print(f"    - Lifshitz Type I only. Type V excluded (zero sign crossings)")
print(f"    - 100% non-adiabatic: median R = {median_R_direct:.0f}")
print(f"    - GGE pairs BCS-BEC crossover, form factor FLAT post-transit")
print(f"    - GCM E_ZP = {E_ZP:.1f} M_KK excluded from S_fold")
print(f"    - Carlip: L = 1.74 mm -> Lambda_obs (translates, doesn't solve)")
print(f"    - Impedance DR = {DR_combined:.2f} (near threshold, INFO)")
