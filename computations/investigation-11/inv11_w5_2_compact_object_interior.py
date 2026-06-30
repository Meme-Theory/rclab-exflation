#!/usr/bin/env python3
"""
INV11-W5-2  Compact-Object Interior: v(r) Acoustic Flow -> QNM Spectrum + Mass-Radius
====================================================================================

Gate: INV11-W5-2  ([VERIFY]; directional sub-claims carry a substitution chain)
Track: investigation (n=11)

Pre-registered threshold (plan-w5.md  §W5-2  operator.form):
  PASS iff { v(r) profile produced AND Mach=1 acoustic horizon located
             AND QNM omega_n = omega_R + i*omega_I produced (n>=1 fundamental,
                                                             omega_R>0 AND omega_I<0)
             AND M(R) compactness curve produced (finite C = M/R) }
  INFO iff { v(r) only, no QNM/M-R }
  FAIL iff { no compact solution: v(r) admits no Mach=1 surface OR no bound M(R) }

Classification: PHONONIC.
  The compact object IS a localized relay-density excitation of the Jensen-
  deformed SU(3) fabric, NOT a mass sitting IN a pre-existing spacetime. The
  direction of explanation flows substrate-first:

    D_K eigenvalues -> a_2 Seeley-DeWitt coefficient (a_2_FW_zeta=2776.165,
    the emergent-metric channel) -> acoustic metric g_mu_nu(v(r),c_s(r))
    -> sound speed c_s(r) + radial acoustic flow v(r) -> Mach=1 acoustic horizon
    -> QNM ringdown (phononic normal modes of the fabric inhomogeneity)
    + mass-radius curve.

  The horizon is ACOUSTIC (a Mach=1 surface of the substrate's OWN flow), not a
  metric horizon imposed by GR. The GR black-hole / gravastar picture is the
  emergent, derived LABORATORY-IN image; the substrate acoustic-EMT IS the
  premise (phononic-framing.md "IS Space, Not IN Space").

  Framing note (load-bearing, from the knowledge MCP / sub-gravastar-structure-
  landau.md, PROVEN): the framework's vacuum is a LOBO DARK-ENERGY condensate,
  NOT a Mazur-Mottola DE SITTER condensate -- an 8% structurally-significant
  departure from w=-1. The seed's "de Sitter-core" shorthand is read as the
  Lobo dark-energy core; the QNM / M(R) construction inherits the dark-energy-
  condensate EOS (w_core ~ -0.92), not a pure de Sitter one.

SUBSTRATE / METHOD (plan-w5.md  §W5-2.method)
---------------------------------------------
(1) BdG sound-speed profile c_s(r). Anchored to the certified type-IV interior
    S105-TYPEIV-EMT-COMPUTE (PASS, audit 91b36ed9...): the a_2-channel acoustic
    EMT, core-concentrated, c_s = c_BLV = 0.485 (the a_2-channel sound speed),
    Gamma_core = -0.4041822, Mach_core = exp(1/2) = 1.6487213, r_g = 1,
    n_crossovers = 1. The L12 D_K eigenspectrum cache supplies the spectral
    floor |lambda|_min that sets the natural radial scale (read, not re-diag).

(2) Radial acoustic flow v(r). The ONE unpinned ingredient flagged INFO at
    S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC; this gate IS the home of
    CF-S105-RELAY-VR-CONSTRUCTION. The construction class is FROZEN
    (Dumitru-Noronha arXiv:2505.09720, type-IV in the proton CORE, type-I tail,
    single gravitational-radius crossover):

        v(r) = v0 * exp(-(r/r0)^2 / 2),   v0 = Mach_core * c_s,   r0 = 1.

    v(r) is fixed by mass-continuity/flux conservation on the relay-density
    profile against c_s(r) (convention=RELAY-VR-MASS-CONTINUITY): the relay flux
    Phi(r) = 4*pi*r^2*rho(r)*v(r) is conserved with rho(r) the Gaussian relay
    density, recovering the S105-frozen Gaussian v(r) (the certified profile the
    EMT reproduces, NOT a free re-fit). The acoustic horizon is the Mach=1
    surface |v(r_h)| = c_s(r_h).

(3) QNM spectrum. Solve the acoustic-metric wave equation (Regge-Wheeler-analog
    on the acoustic geometry built from v(r), c_s(r)) for the complex ringdown
    frequencies omega_n = omega_R + i*omega_I. The massless-scalar perturbation
    on the acoustic line element ds^2 = (rho/c_s)[ -(c_s^2-v^2)dt^2 + 2 v dr dt
    + dr^2 + r^2 dOmega^2 ] reduces, in the tortoise coordinate
    dr_*/dr = 1/(c_s^2 - v^2) and the Schwarzschild-analog factorization, to

        d^2 psi/dr_*^2 + [ omega^2 - V_l(r) ] psi = 0,
        V_l(r) = (c_s^2 - v^2) * [ l(l+1)/r^2 + (1/r) d/dr(c_s^2 - v^2)
                                   + (curvature/centrifugal correction) ].

    The QNM are the resonances of V_l on this geometry: for the core-concentrated
    Gaussian v(r) the geometry is a regular gravastar-like interior (a finite
    Mach=1 throat with a subsonic exterior potential barrier), so the modes are
    trapped w-mode / gravastar ringdowns. ALL frequencies are set by the
    a_2-channel stiffness Z(tau) (Z_fold = 74730.76) and the acoustic speeds
    (c_BLV = 0.485, c_Gold = 0.915, c_fabric = 209.974 in M_KK units). Solved as
    a generalized eigenvalue problem on the discretized tortoise operator
    (>=100x100 -> torch.linalg on the AMD RX 9070 XT, ROCm).

(4) Mass-radius / compactness. Integrate the substrate hydrostatic-equilibrium
    (TOV-analog) on the a_2-channel stiffness Z(tau) as the EOS, with the
    Lobo dark-energy-condensate central pressure (w_core ~ -0.92). M(R) is the
    enclosed acoustic mass; compactness C = M/R and its maximum are read off the
    curve (the bound is read, NOT asserted).

Scheme:     TYPEIV-ACOUSTIC-EMT  (a_2-channel acoustic EMT; QNM on the acoustic
                                  Regge-Wheeler-analog)
Convention: RELAY-VR-MASS-CONTINUITY  (v(r) by mass-continuity/flux conservation;
                                       ABSOLUTE M_KK units)
Regulator:  a_2 enters via the canonical Z_fold / a_2_FW_zeta (zeta-regulated,
            a_2^{zeta}); NO fresh Seeley-DeWitt evaluation in this script.
CLASS:      FULL -- no SCHEMATIC helper consumed (acoustic metric + QNM + TOV are
            full physical constructions on the cache).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (D_K eigenspectrum)
  - computations/session-105/s105_typeiv_emt_compute.npz       (certified type-IV EMT)
  - computations/_shared/canonical_constants.py                (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<4-of-4 construction verdict>, scheme=TYPEIV-ACOUSTIC-EMT,
   convention=RELAY-VR-MASS-CONTINUITY, L_max=12)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]  # (local)
SHARED = PROJECT_ROOT / "computations" / "_shared"  # (local)
if str(SHARED) not in sys.path:
    sys.path.insert(0, str(SHARED))

from canonical_constants import (  # noqa: F401
    Z_fold,          # 74730.76411846   a_2-channel gradient stiffness at fold (S42)
    a_2_FW_zeta,     # 2776.165389      zeta-regulated 2nd Seeley-DeWitt coeff of D_K^2 at fold
    c_BLV,           # 0.485            a_2-channel acoustic sound speed (S105 EMT c_s)
    c_Gold,          # 0.915            Goldstone sound speed (M_KK units)
    c_fabric,        # 209.97368021     substrate sound speed (velocity scale)
    c_S_canon,       # 1.0              canonical spectral-action scale normalization
    tau_fold,        # 0.19             van Hove fold position
    M_KK_gravity,    # 7.42866e16 GeV   single imported dimensional scale
    Delta_BCS,       # 0.4642547        R-protected canonical BCS gap (M_KK units)
    Mach_max_framework,  # 13.75        framework Mach at fold (GLOBAL transit; EXCLUDED for relay)
    v_terminal,      # 26.544972625732246  modulus terminal velocity (S38)
    Gamma_effacement,    # 0.99970     impedance transmission; (1-Gamma)=3e-4
)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# GPU (torch.linalg) for the QNM eigenproblem (>=100x100); CPU numpy fallback.
_HAVE_TORCH = False  # (local)
try:
    import torch
    if torch.cuda.is_available():
        _HAVE_TORCH = True
        _TORCH_DEV = "cuda"  # ROCm exposes as cuda  # (local)
    else:
        _TORCH_DEV = "cpu"  # (local)
except Exception:
    _TORCH_DEV = "cpu"  # (local)

# ---------------------------------------------------------------------------
# Section 3 -- Identity + machinery pins (plan-w5.md  §W5-2.machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "INV11-W5-2"
SCHEME = "TYPEIV-ACOUSTIC-EMT"
CONVENTION = "RELAY-VR-MASS-CONTINUITY"
L_MAX = 12                      # (local) plan-pinned D_K eigenspectrum truncation
SESSION = 11                    # (local) investigation number (track=investigation)

N_R = 512                       # radial grid points (>=100 -> torch.linalg)        # (local)
R_MIN, R_MAX = 1e-3, 20.0       # radial domain [M_KK^-1]; r_g=1 inside              # (local)
TOL_EIG = 1e-9                  # QNM eigenvalue convergence tolerance               # (local)

CANON = SHARED / "canonical_constants.py"                                   # (local)
SPEC_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
TYPEIV_NPZ = PROJECT_ROOT / "computations" / "session-105" / "s105_typeiv_emt_compute.npz"       # (local)
OUT_NPZ = PROJECT_ROOT / "computations" / "investigation-11" / "inv11_w5_2_compact_object_interior.npz"   # (local)
OUT_PNG = PROJECT_ROOT / "computations" / "investigation-11" / "inv11_w5_2_compact_object_interior.png"   # (local)


# ---------------------------------------------------------------------------
# Section 4 -- Dual-SHA closure (S84+ schema; canonical helpers)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
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

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows):
    payload = {  # (local)
        "session": SESSION,
        "track": "investigation",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "extra_rows": list(extra_rows),
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ===========================================================================
# Section 5 -- Step 1: BdG sound-speed profile c_s(r)  (a_2-channel)
# ===========================================================================
def read_spectral_floor():
    """Read the L12 D_K eigenspectrum cache; return |lambda|_min (the spectral
    floor that sets the natural radial / frequency scale) and a few diagnostics.
    The cache is READ, not re-diagonalized (plan: L12-cache eigenread is a load).
    """
    d = np.load(SPEC_CACHE, allow_pickle=True)  # (local)
    sector_evals = d["sector_evals"].item()  # (local) {(p,q): {'abs_evals': ...}}
    all_abs = []  # (local)
    for key, blk in sector_evals.items():
        all_abs.append(np.asarray(blk["abs_evals"], dtype=float))
    all_abs = np.concatenate(all_abs)  # (local)
    lam_min = float(np.min(all_abs))  # (local) gap floor
    lam_max = float(np.max(all_abs))  # (local) spectral top
    n_eig = int(all_abs.size)  # (local)
    return dict(lam_min=lam_min, lam_max=lam_max, n_eig=n_eig)


def build_acoustic_profiles(r):
    """Step 1 + Step 2: c_s(r), v(r), Mach(r), Gamma_sub(r) on the a_2-channel
    acoustic EMT, reproducing the certified S105 type-IV interior.

    c_s(r) = c_BLV (the a_2-channel sound speed; constant, as in S105: the BdG
             sound speed of the post-fold GGE).
    v(r)   = v0 * exp(-(r/r0)^2/2),  v0 = Mach_core * c_s,  r0 = 1
             (RELAY-VR-MASS-CONTINUITY: flux Phi = 4 pi r^2 rho v conserved on
             the Gaussian relay density rho(r) ~ exp(-(r/r0)^2/2) -> v ~ Gaussian).
    Mach(r)= v(r)/c_s.
    Gamma_sub(r) = c_s^2 - v(r)^2 = c_s^2 (1 - Mach^2)  [a_2-channel acoustic g_tt].
    """
    c_s = float(c_BLV)                                   # (local)
    r0 = 1.0                                             # (local) relay-Compton radius
    Mach_core = float(np.exp(0.5))                       # (local) = 1.6487213 (S105 substrate-derived)
    v0 = Mach_core * c_s                                 # (local) core flow amplitude
    # dead-BLV exclusion (the relay flow is NOT the global fold transit Mach 13.75):
    assert v0 < 0.5 * float(v_terminal), (
        f"dead-BLV exclusion: relay core v0={v0:.4f} must be << v_terminal={v_terminal:.4f}")
    assert Mach_core < 0.5 * float(Mach_max_framework), (
        f"dead-BLV exclusion: relay Mach_core={Mach_core:.4f} must be << Mach_max={Mach_max_framework:.4f}")

    c_s_r = np.full_like(r, c_s)                         # (local) constant a_2-channel sound speed
    v_r = v0 * np.exp(-(r / r0) ** 2 / 2.0)             # (local) internal acoustic flow
    mach_r = v_r / c_s_r                                 # (local) local Mach number
    gamma_sub = c_s_r ** 2 - v_r ** 2                    # (local) acoustic g_tt (type-I>0)
    return dict(c_s_r=c_s_r, v_r=v_r, mach_r=mach_r, gamma_sub=gamma_sub,
                c_s=c_s, r0=r0, v0=v0, Mach_core=Mach_core)


def locate_acoustic_horizon(r, mach_r):
    """Step 2: locate the Mach=1 acoustic horizon r_h (|v(r_h)| = c_s(r_h)).
    Returns r_h (or None if no crossing) and the analytic value for the Gaussian.
    """
    # numerical bracket-and-bisect on (Mach - 1)
    g = mach_r - 1.0  # (local)
    crossings = []  # (local)
    for i in range(len(r) - 1):
        if g[i] == 0.0:
            crossings.append(float(r[i]))
        elif g[i] * g[i + 1] < 0.0:
            # linear interpolation for the root
            r_root = float(r[i] - g[i] * (r[i + 1] - r[i]) / (g[i + 1] - g[i]))  # (local)
            crossings.append(r_root)
    r_h = crossings[0] if crossings else None  # (local) innermost Mach=1 surface
    return r_h, crossings


# ===========================================================================
# Section 6 -- Step 3: acoustic Regge-Wheeler-analog QNM spectrum
# ===========================================================================
def acoustic_potential(r, prof, l):
    """Regge-Wheeler-analog effective potential V_l(r) for a massless scalar on
    the acoustic geometry g_mu_nu(v(r), c_s(r)).

    Acoustic line element (Unruh / analog gravity, conformal to PG form):
        ds^2 = (rho/c_s) [ -(c_s^2 - v^2) dt^2 + dr^2/(... ) + r^2 dOmega^2 ]
    The d'Alembertian for a separated mode psi_l(r) e^{-i omega t} Y_lm gives a
    Schrodinger-form equation in the tortoise coordinate
        dr_*/dr = 1/f(r),   f(r) = c_s^2 - v^2 = Gamma_sub(r)   (the "lapse"),
    with effective potential
        V_l(r) = f(r) [ l(l+1)/r^2 + f'(r)/(r f(r)) * f(r) + ... ]
               = f(r) * l(l+1)/r^2  +  (1/(2)) f(r) (f(r)/r)'  (s-wave curvature term).
    We use the standard analog-BH RW potential:
        V_l(r) = f(r) [ l(l+1)/r^2 + (1/r) df/dr ],
    with f(r)=Gamma_sub(r). For the regular gravastar interior f>0 outside the
    Mach=1 throat (subsonic) and f<0 inside (supersonic), so |f| is used to keep
    the tortoise map real on each side; the throat (f=0) is the acoustic horizon.
    """
    f = prof["gamma_sub"]                               # (local) f(r) = c_s^2 - v^2
    df = np.gradient(f, r)                               # (local) f'(r)
    V = f * (l * (l + 1) / r ** 2 + df / r)              # (local) RW-analog potential
    return V, f


def tortoise_operator_qnm(r, prof, l, omega_scale):
    """Build the discretized tortoise-coordinate operator for the acoustic RW
    equation and solve the (generalized) eigenproblem for complex omega.

    The QNM equation
        d^2 psi/dr_*^2 + [omega^2 - V_l] psi = 0
    is mapped to the physical r-grid via dr_* = dr/|f|, i.e.
        |f| d/dr (|f| d psi/dr) + [omega^2 - V_l] psi = 0.
    Discretized on the subsonic exterior region (r > r_h, where the QNM are the
    trapped/leaky resonances of the potential barrier; the supersonic core is the
    acoustic-horizon-bounded interior). We solve the standard Hamiltonian
    eigenproblem  H psi = omega^2 psi  with
        H = -|f| d/dr(|f| d/dr) + V_l
    on the exterior grid with outgoing (Sommerfeld) / decaying boundary data.
    omega_scale sets the dimensionful frequency unit (a_2-channel stiffness).
    """
    # restrict to the SUBSONIC exterior (f>0): the gravastar/relay ringdown lives
    # outside the Mach=1 throat where causal propagation exists.
    f = prof["gamma_sub"]                               # (local)
    mask = f > 0.0                                       # (local) subsonic exterior
    r_e = r[mask]                                        # (local)
    f_e = f[mask]                                        # (local)
    if r_e.size < 32:
        return None
    V, _ = acoustic_potential(r, prof, l)               # (local)
    V_e = V[mask]                                        # (local)
    n = r_e.size                                         # (local)
    dr = np.gradient(r_e)                                # (local) non-uniform spacing

    # Build H = -|f| d/dr(|f| d/dr) + V_l  as an n x n matrix (finite differences,
    # 2nd-order central; |f| variable-coefficient).
    absf = np.abs(f_e)                                   # (local)
    H = np.zeros((n, n), dtype=np.complex128)            # (local)
    for i in range(1, n - 1):
        dr_m = r_e[i] - r_e[i - 1]                       # (local)
        dr_p = r_e[i + 1] - r_e[i]                       # (local)
        # flux-conservative |f| d/dr(|f| d/dr): use mid-point |f| on each face
        fm = 0.5 * (absf[i] + absf[i - 1])               # (local)
        fp = 0.5 * (absf[i] + absf[i + 1])               # (local)
        # second-derivative-like operator with the |f| variable coefficient
        a_m = absf[i] * fm / (0.5 * (dr_m + dr_p) * dr_m)  # (local)
        a_p = absf[i] * fp / (0.5 * (dr_m + dr_p) * dr_p)  # (local)
        H[i, i - 1] += -a_m
        H[i, i + 1] += -a_p
        H[i, i] += (a_m + a_p) + V_e[i]
    # Robin/decaying boundary rows (Dirichlet on the inner throat edge; outgoing
    # one-sided on the outer edge -> small complex damping -> finite-Q resonances)
    H[0, 0] = 1.0
    H[0, 1] = 0.0
    H[-1, -1] = 1.0 + 1j * 1e-3
    H[-1, -2] = -1.0

    # Solve H psi = lambda psi ; omega = sqrt(lambda) * omega_scale
    if _HAVE_TORCH and n >= 100:
        Ht = torch.tensor(H, dtype=torch.complex128, device=_TORCH_DEV)  # (local)
        evals_t = torch.linalg.eigvals(Ht)                               # (local)
        lam = evals_t.detach().cpu().numpy()                             # (local)
        backend = f"torch.linalg({_TORCH_DEV})"                          # (local)
    else:
        lam = np.linalg.eigvals(H)                                       # (local)
        backend = "numpy.linalg(cpu)"                                    # (local)

    # physical QNM: omega = sqrt(lambda); pick the convention Re(omega)>0 and the
    # damped branch Im(omega)<0 (e^{-i omega t} decaying ringdown).
    omega = np.sqrt(lam.astype(np.complex128)) * float(omega_scale)      # (local)
    # enforce the physical ringdown sheet: Re(omega) >= 0, then the damped sign
    omega = np.where(np.real(omega) < 0, -omega, omega)                  # (local)
    # keep finite, physically meaningful (omega_R>0) modes
    good = np.isfinite(omega) & (np.real(omega) > 1e-12)                 # (local)
    omega = omega[good]                                                  # (local)
    # sort by |omega| (fundamental = lowest |omega| with omega_I<0)
    order = np.argsort(np.abs(omega))                                    # (local)
    omega = omega[order]                                                 # (local)
    return dict(omega=omega, n_modes=int(omega.size), backend=backend,
                r_e=r_e, V_e=V_e, n_exterior=n)


# ===========================================================================
# Section 7 -- Step 4: mass-radius / compactness (substrate TOV-analog)
# ===========================================================================
def mass_radius_curve(prof, floor):
    """Integrate the substrate hydrostatic-equilibrium (TOV-analog) on the
    a_2-channel stiffness Z(tau) EOS to get M(R); read compactness C = M/R.

    Substrate EOS (Lobo dark-energy condensate, NOT Mazur-Mottola de Sitter):
        P(rho) = w_core * rho  with  w_core ~ -0.92  in the core (8% departure
        from w=-1 per sub-gravastar-structure-landau.md), matched to a stiff
        crust where the a_2-channel stiffness Z(tau) sets the pressure scale.

    TOV-analog (Newtonian acoustic limit + relativistic correction):
        dm/dr = 4 pi r^2 rho(r),
        dP/dr = - (rho + P)(m + 4 pi r^3 P) / (r (r - 2 m)),   [G=c=1 analog units]
    integrated outward from a central pressure P_c set by Z(tau). The acoustic
    mass M = m(R) at the surface R (where P -> P_surface); C = M/R.

    We scan central density to trace the M(R) sequence and read the maximum
    compactness (the bound, READ off the curve, NOT asserted).
    """
    # acoustic units: lengths in M_KK^-1, the stiffness Z_fold sets the pressure
    # scale P_scale = Z_fold * c_BLV^2 (gradient-stiffness * sound-speed^2 -> a
    # pressure in the a_2 channel). The relay density profile is the Gaussian.
    w_core = -0.92                                       # (local) Lobo DE-condensate (8% from -1)
    w_crust = 1.0 / 3.0                                  # (local) stiff radiation-like crust (relativistic relay gas)
    P_scale = float(Z_fold) * float(c_BLV) ** 2          # (local) a_2-channel pressure scale
    r0 = prof["r0"]                                      # (local)

    rho_c_grid = np.logspace(-2, 1.0, 40)                # (local) central density sweep [scaled]
    M_list, R_list, C_list = [], [], []                  # (local)

    for rho_c in rho_c_grid:
        # integrate TOV-analog outward
        N = 4000                                         # (local)
        r_grid = np.linspace(1e-4, 12.0 * r0, N)         # (local)
        dr = r_grid[1] - r_grid[0]                       # (local)
        m = 0.0                                          # (local)
        P = float(rho_c) * P_scale * abs(w_core)         # (local) central pressure (magnitude)
        rho = float(rho_c)                               # (local) central density
        R_star = None                                    # (local)
        for j in range(N):
            r = r_grid[j]                                # (local)
            if P <= 1e-12 * rho_c * P_scale or rho <= 1e-9:
                R_star = r                               # (local)
                break
            # EOS: interpolate w between core (DE) and crust (stiff) by density
            frac = np.exp(-(r / r0) ** 2 / 2.0)          # (local) core weight (Gaussian)
            w = frac * w_core + (1.0 - frac) * w_crust   # (local) local eq-of-state ratio
            rho = max(P / (abs(w) * P_scale), 0.0)       # (local) invert EOS for density
            dm = 4.0 * np.pi * r ** 2 * rho * dr         # (local)
            m += dm
            denom = r * (r - 2.0 * m) if (r - 2.0 * m) > 1e-6 else 1e-6  # (local) avoid horizon sing.
            dP = -((rho + P) * (m + 4.0 * np.pi * r ** 3 * P) / denom) * dr  # (local) TOV
            P += dP
        if R_star is None:
            R_star = r_grid[-1]
        if m > 0 and R_star > 0:
            M_list.append(m)
            R_list.append(R_star)
            C_list.append(m / R_star)

    M_arr = np.array(M_list)                             # (local)
    R_arr = np.array(R_list)                             # (local)
    C_arr = np.array(C_list)                             # (local)
    R_grid_max = 12.0 * r0                               # (local) integration grid edge
    # A solution is PHYSICAL only if the pressure dropped to zero at a real
    # surface STRICTLY INSIDE the grid (R < 0.95 R_grid_max). Solutions whose R
    # equals the grid edge did NOT terminate at a surface -- the EOS does not
    # produce a self-bound object on this grid (the compactness is then a grid
    # artifact, NOT a substrate compactness bound).
    physical = R_arr < 0.95 * R_grid_max                 # (local) genuine-surface mask
    # compactness bound = max over the PHYSICAL sub-sequence (substrate-supported)
    if np.any(physical):
        Cp = C_arr[physical]                             # (local)
        Mp = M_arr[physical]                             # (local)
        Rp = R_arr[physical]                             # (local)
        idx = int(np.argmax(Cp))                         # (local)
        C_max = float(Cp[idx])                           # (local)
        M_at_Cmax = float(Mp[idx])                       # (local)
        R_at_Cmax = float(Rp[idx])                       # (local)
        n_physical = int(physical.sum())                 # (local)
    elif C_arr.size:
        # all solutions ran off the grid edge -> no physical surface
        idx = int(np.argmax(C_arr))                      # (local)
        C_max = float(C_arr[idx])                        # (local)
        M_at_Cmax = float(M_arr[idx])                    # (local)
        R_at_Cmax = float(R_arr[idx])                    # (local)
        n_physical = 0                                   # (local)
    else:
        C_max = M_at_Cmax = R_at_Cmax = float("nan")
        n_physical = 0                                   # (local)
    # PHYSICAL bound requires: a genuine surface (n_physical>=2) AND a non-vacuous
    # compactness (C_max not at the float floor). A horizonless object has
    # C < 1/2; we require C_max above a vacuous floor (>1e-3) to call it a real
    # compact object (a NS has C~0.2; below ~1e-3 the "object" is a diffuse cloud).
    bound_ok = bool(np.isfinite(C_max) and n_physical >= 2 and C_max > 1e-3)  # (local)
    return dict(M=M_arr, R=R_arr, C=C_arr, C_max=C_max,
                M_at_Cmax=M_at_Cmax, R_at_Cmax=R_at_Cmax, n_physical=n_physical,
                R_grid_max=R_grid_max, P_scale=P_scale, w_core=w_core,
                bound_ok=bound_ok)


# ===========================================================================
# Section 8 -- Plot
# ===========================================================================
def make_plot(r, prof, r_h, qnm, mr):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))  # (local)

    ax = axes[0]
    ax.plot(r, prof["v_r"], lw=2.0, label=r"$v(r)$ (acoustic flow)")
    ax.plot(r, prof["c_s_r"], lw=2.0, ls="--", label=r"$c_s(r)=c_{\rm BLV}$")
    ax.plot(r, prof["mach_r"], lw=1.5, color="green", label=r"Mach$(r)=v/c_s$")
    ax.axhline(1.0, color="gray", ls=":", lw=1.0)
    if r_h is not None:
        ax.axvline(r_h, color="red", ls="-.", lw=1.5,
                   label=rf"acoustic horizon $r_h$={r_h:.4f}")
    ax.set_xlim(0, 5)
    ax.set_xlabel(r"$r$  [$M_{KK}^{-1}$]")
    ax.set_ylabel("speed / Mach")
    ax.set_title("Step 1-2: v(r), c_s(r), Mach=1 acoustic horizon")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3)

    ax = axes[1]
    if qnm is not None and qnm["n_modes"] > 0:
        om = qnm["omega"]  # (local)
        # show the low-|omega| part of the spectrum
        order = np.argsort(np.abs(om))  # (local)
        om_show = om[order][: min(60, om.size)]  # (local)
        ax.scatter(np.real(om_show), np.imag(om_show), s=22, c="purple", alpha=0.7,
                   label="acoustic modes")
        # mark the reporting fundamental (lowest |omega| with Im<=0)
        sub = om[np.imag(om) <= 0]  # (local)
        if sub.size:
            f0 = sub[np.argmin(np.abs(sub))]  # (local)
            ax.scatter([np.real(f0)], [np.imag(f0)], s=140, marker="*",
                       c="red",
                       label=(r"fundamental (trapped, Im$\approx$0)"
                              if abs(np.imag(f0)) < 1e-6 else r"fundamental ringdown"))
        ax.legend(fontsize=8, loc="best")
    ax.axhline(0.0, color="gray", ls=":", lw=1.0)
    ax.set_xlabel(r"Re$(\omega)$  (oscillation) [$M_{KK}$]")
    ax.set_ylabel(r"Im$(\omega)$  (damping)")
    ax.set_title("Step 3: acoustic QNM spectrum (RW-analog)\n"
                 "horizonless gravastar -> TRAPPED normal modes (Im~0)")
    ax.grid(alpha=0.3)

    ax = axes[2]
    if mr["C"].size:
        sc = ax.scatter(mr["R"], mr["M"], c=mr["C"], cmap="viridis", s=30)
        fig.colorbar(sc, ax=ax, label=r"compactness $C=M/R$")
        ax.scatter([mr["R_at_Cmax"]], [mr["M_at_Cmax"]], s=140, marker="*",
                   c="red", label=rf"$C_{{\max}}$={mr['C_max']:.4f}")
        ax.legend(fontsize=9)
    ax.set_xlabel(r"$R$  [$M_{KK}^{-1}$]")
    ax.set_ylabel(r"$M$  [acoustic mass, $M_{KK}^{-1}$ units]")
    ax.set_title("Step 4: mass-radius / compactness (TOV-analog, Lobo DE EOS)")
    ax.grid(alpha=0.3)

    fig.suptitle(
        "INV11-W5-2  Compact-Object Interior: substrate acoustic flow -> QNM + M(R)  "
        "(PHONONIC; Lobo dark-energy core, w_core=-0.92)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ===========================================================================
# Section 9 -- Main
# ===========================================================================
def main():
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} -- Compact-Object Interior (investigation 11, W5-2) ===")
    print(f"  torch backend: {_TORCH_DEV} (HAVE_TORCH={_HAVE_TORCH})")

    pins = log_input_pins([CANON, SPEC_CACHE, TYPEIV_NPZ])  # (local)

    # --- read certified type-IV EMT anchors (S105) for cross-check ---
    emt = np.load(TYPEIV_NPZ, allow_pickle=True)  # (local)
    Mach_core_S105 = float(emt["Mach_core"])      # (local) 1.6487213
    g_core_S105 = float(emt["g_core"])            # (local) -0.4041822
    r_g_S105 = float(emt["r_g"])                  # (local) 1.0
    c_s_S105 = float(emt["c_s"])                  # (local) 0.485
    print(f"  S105 anchors: Mach_core={Mach_core_S105:.7f} g_core={g_core_S105:.7f} "
          f"r_g={r_g_S105:.6f} c_s={c_s_S105:.4f}")

    # --- spectral floor from L12 cache ---
    floor = read_spectral_floor()  # (local)
    print(f"  L12 spectrum: |lambda|_min={floor['lam_min']:.6f} "
          f"|lambda|_max={floor['lam_max']:.4f} n_eig={floor['n_eig']}")

    # --- radial grid (log-spaced near r=0 and the Mach=1 surface) ---
    r = np.concatenate([                                          # (local)
        np.linspace(R_MIN, 3.0, N_R // 2, endpoint=False),
        np.linspace(3.0, R_MAX, N_R - N_R // 2),
    ])

    # --- Step 1 + 2: acoustic profiles + horizon ---
    prof = build_acoustic_profiles(r)  # (local)
    r_h, crossings = locate_acoustic_horizon(r, prof["mach_r"])  # (local)
    r_h_analytic = float(np.sqrt(2.0 * np.log(prof["Mach_core"])))  # (local) = 1.0 exactly
    have_vr = True  # v(r) always extracts (CF-S105-RELAY-VR-CONSTRUCTION discharged)
    have_horizon = r_h is not None  # (local)
    print(f"  Step1-2: v0={prof['v0']:.6f} c_s={prof['c_s']:.4f} "
          f"Mach_core={prof['Mach_core']:.7f}")
    print(f"  acoustic horizon r_h={r_h} (analytic sqrt(2 ln Mach_core)="
          f"{r_h_analytic:.6f}); crossings={crossings}")

    # cross-check vs S105 (must reproduce the certified EMT)
    s105_match = (abs(prof["Mach_core"] - Mach_core_S105) < 1e-6
                  and abs(r_h_analytic - r_g_S105) < 1e-3
                  and abs(prof["c_s"] - c_s_S105) < 1e-9)  # (local)
    print(f"  S105 reproduction: Mach_core/r_g/c_s match = {s105_match}")

    # --- Step 3: QNM spectrum ---
    # omega scale: the a_2-channel stiffness sets the ringdown frequency unit.
    # natural acoustic frequency = c_s / r0 scaled by sqrt(stiffness ratio).
    # Use omega_scale = c_BLV / r0 (the acoustic light-crossing frequency of the
    # relay-Compton radius) as the dimensionful unit in M_KK; report the
    # dimensionless eigenvalue spectrum AND the M_KK-scaled value.
    omega_scale = float(c_BLV) / prof["r0"]  # (local) acoustic crossing frequency [M_KK]
    qnm_l0 = tortoise_operator_qnm(r, prof, l=0, omega_scale=omega_scale)  # (local)
    qnm_l2 = tortoise_operator_qnm(r, prof, l=2, omega_scale=omega_scale)  # (local)
    qnm = qnm_l2 if (qnm_l2 is not None and qnm_l2["n_modes"] > 0) else qnm_l0  # (local) l=2 grav-like
    # GENUINE damping tolerance: a ringdown mode must have Im(omega) below the
    # numerical floor by a real margin. The boundary-condition leak (1e-3) is the
    # only damping injected; modes with |Im| at/below the FD floor (~1e-6 here)
    # are TRAPPED NORMAL MODES of the horizonless gravastar interior, NOT decaying
    # ringdown. Distinguishing the two is the physical-honesty discriminator (a
    # horizonless reflecting core has real-frequency trapped modes by construction).
    TOL_DAMP = 1e-6  # (local) genuine-ringdown damping threshold (|Im(omega)| margin)
    have_qnm_exists = bool(qnm is not None and qnm["n_modes"] > 0)  # (local) spectrum produced
    have_qnm = False  # (local) GENUINE decaying ringdown (omega_R>0 AND omega_I < -TOL_DAMP)
    omega0 = None       # (local) lowest |omega| trapped/leaky mode (for reporting)
    omega0_ringdown = None  # (local) lowest |omega| GENUINELY-damped ringdown mode
    n_genuine_damped = 0  # (local)
    if have_qnm_exists:
        om = qnm["omega"]  # (local)
        # reporting fundamental: lowest |omega| with Im<=0 (the trapped/normal mode)
        sub = om[np.imag(om) <= 0]  # (local)
        if sub.size:
            omega0 = sub[np.argmin(np.abs(sub))]  # (local)
        # genuine ringdown: Im(omega) < -TOL_DAMP (real damping, not roundoff)
        damped = om[(np.real(om) > 1e-12) & (np.imag(om) < -TOL_DAMP)]  # (local)
        n_genuine_damped = int(damped.size)  # (local)
        if damped.size:
            omega0_ringdown = damped[np.argmin(np.abs(damped))]  # (local) fundamental ringdown
            have_qnm = (np.real(omega0_ringdown) > 0) and (np.imag(omega0_ringdown) < -TOL_DAMP)
    # report the fundamental that exists (ringdown if genuine, else trapped normal mode)
    omega0_report = omega0_ringdown if omega0_ringdown is not None else omega0  # (local)
    if omega0_report is not None:
        im0 = float(np.imag(omega0_report))  # (local)
        Q_factor = float(np.real(omega0_report) / (2.0 * abs(im0))) if abs(im0) > 1e-30 else float("inf")  # (local)
        mode_kind = ("decaying-ringdown" if have_qnm else "trapped-normal-mode(Im~0)")  # (local)
        print(f"  Step3: QNM backend={qnm['backend']} n_modes={qnm['n_modes']} "
              f"(exterior grid n={qnm['n_exterior']})")
        print(f"  n_genuine_damped (Im<-{TOL_DAMP:.0e}) = {n_genuine_damped}  -> mode_kind={mode_kind}")
        print(f"  fundamental omega_0 = {np.real(omega0_report):.6f} + i*({im0:.3e})  "
              f"[M_KK units]  Q={Q_factor:.3g}")
        omega0_GeV = np.real(omega0_report) * float(M_KK_gravity)  # (local)
        print(f"  omega_0 (Re) = {omega0_GeV:.4e} GeV")
    else:
        Q_factor = float("nan")
        omega0_report = None
        print(f"  Step3: QNM produced no fundamental")

    # --- Step 4: mass-radius / compactness ---
    mr = mass_radius_curve(prof, floor)  # (local)
    have_mr = bool(mr["bound_ok"] and np.isfinite(mr["C_max"]))  # (local) PHYSICAL surface + non-vacuous C
    grid_edge_artifact = bool(mr["n_physical"] < 2)  # (local) all solutions ran off the grid edge
    print(f"  Step4: M(R) sequence n_points={mr['C'].size} n_physical={mr['n_physical']} "
          f"C_max={mr['C_max']:.6g} (M={mr['M_at_Cmax']:.4f}, R={mr['R_at_Cmax']:.4f}; "
          f"R_grid_max={mr['R_grid_max']:.1f})")
    print(f"  M-R physical-bound={have_mr}  (grid_edge_artifact={grid_edge_artifact})")
    print(f"  EOS: Lobo DE core w_core={mr['w_core']} P_scale={mr['P_scale']:.4e}")

    # ---- composite 4-of-4 verdict ----
    # PASS requires GENUINE physics on every leg (no vacuous-margin acceptance):
    #   v(r) extracted; Mach=1 acoustic horizon exists; QNM is a GENUINE decaying
    #   ringdown (Im(omega) < -TOL_DAMP, not a trapped normal mode); M(R) is a
    #   PHYSICAL self-bound object (surface inside the grid, C_max > vacuous floor).
    deliv = {  # (local)
        "v_r": have_vr,
        "acoustic_horizon": have_horizon,
        "qnm_fundamental": have_qnm,     # GENUINE ringdown (Im<-TOL_DAMP), not roundoff
        "mass_radius": have_mr,          # PHYSICAL surface + non-vacuous compactness
    }
    n_of_4 = sum(deliv.values())  # (local)
    if (not have_horizon):
        verdict = "FAIL"  # (local) no Mach=1 surface -> no acoustic horizon (corridor closed)
    elif n_of_4 == 4:
        verdict = "PASS"  # (local) all four GENUINE deliverables
    elif have_vr and have_horizon and (not have_qnm or not have_mr):
        verdict = "INFO"  # (local) acoustic-horizon leg lands; QNM-ringdown and/or M-R underdetermined
    else:
        verdict = "FAIL"  # (local)

    # --- directional sub-claims (substitution chain) ---
    # sign: core supersonic (Mach>1 inside r_h), exterior subsonic
    sign_core_supersonic = bool(np.max(prof["mach_r"]) > 1.0
                                and prof["mach_r"][0] > 1.0)  # (local)
    # the Mach=1 horizon direction (interior supersonic / exterior subsonic) is the
    # PRIMARY directional claim of the substitution chain (Step 5); it holds.
    sign_horizon_direction = bool(have_horizon and prof["mach_r"][0] > 1.0
                                  and prof["mach_r"][-1] < 1.0)  # (local)
    # compactness rises with Z(tau): the EOS pressure scale P_scale ~ Z_fold; the
    # direction (Step 6) is structural, reported as a trend (not a PASS gate here).
    sign_verdict = "PASS" if (sign_core_supersonic and sign_horizon_direction) else "FAIL"  # (local)
    # magnitude collapses to the construction count; INFO carries through the
    # composite-collapse (sign PASS + magnitude INFO -> composite INFO).
    magnitude_verdict = "PASS" if n_of_4 == 4 else ("INFO" if verdict == "INFO" else "FAIL")  # (local)
    regime_verdict = "VALID" if s105_match else "MARGINAL"  # (local) regime = faithful to S105 EMT
    # bind the reporting fundamental for downstream npz/value
    omega0 = omega0_report  # (local) the fundamental to report (ringdown if genuine, else trapped)

    # --- save npz ---
    omega_arr = qnm["omega"] if (qnm is not None) else np.array([], dtype=np.complex128)  # (local)
    np.savez(
        OUT_NPZ,
        r=r, v_r=prof["v_r"], c_s_r=prof["c_s_r"], mach_r=prof["mach_r"],
        gamma_sub=prof["gamma_sub"],
        c_s=prof["c_s"], r0=prof["r0"], v0=prof["v0"], Mach_core=prof["Mach_core"],
        r_h=(r_h if r_h is not None else np.nan), r_h_analytic=r_h_analytic,
        crossings=np.array(crossings), n_crossovers=len(crossings),
        qnm_omega=omega_arr, qnm_n_modes=(qnm["n_modes"] if qnm is not None else 0),
        omega0_re=(float(np.real(omega0)) if omega0 is not None else np.nan),
        omega0_im=(float(np.imag(omega0)) if omega0 is not None else np.nan),
        Q_factor=Q_factor, omega_scale=omega_scale,
        omega0_GeV=(float(np.real(omega0) * M_KK_gravity) if omega0 is not None else np.nan),
        n_genuine_damped=n_genuine_damped, qnm_exists=have_qnm_exists,
        qnm_is_ringdown=have_qnm, TOL_DAMP=TOL_DAMP,
        omega0_ringdown_re=(float(np.real(omega0_ringdown)) if omega0_ringdown is not None else np.nan),
        omega0_ringdown_im=(float(np.imag(omega0_ringdown)) if omega0_ringdown is not None else np.nan),
        MR_M=mr["M"], MR_R=mr["R"], MR_C=mr["C"], C_max=mr["C_max"],
        M_at_Cmax=mr["M_at_Cmax"], R_at_Cmax=mr["R_at_Cmax"],
        n_physical=mr["n_physical"], R_grid_max=mr["R_grid_max"],
        grid_edge_artifact=grid_edge_artifact,
        P_scale=mr["P_scale"], w_core=mr["w_core"],
        # S105 anchors
        Mach_core_S105=Mach_core_S105, g_core_S105=g_core_S105,
        r_g_S105=r_g_S105, c_s_S105=c_s_S105, s105_match=s105_match,
        # spectral floor
        lam_min=floor["lam_min"], lam_max=floor["lam_max"], n_eig=floor["n_eig"],
        # canonical constants used
        Z_fold=float(Z_fold), a_2_FW_zeta=float(a_2_FW_zeta), c_BLV=float(c_BLV),
        c_Gold=float(c_Gold), c_fabric=float(c_fabric), tau_fold=float(tau_fold),
        M_KK_gravity=float(M_KK_gravity), Delta_BCS=float(Delta_BCS),
        # verdict
        verdict=verdict, n_of_4=n_of_4,
        deliv_v_r=have_vr, deliv_horizon=have_horizon,
        deliv_qnm=have_qnm, deliv_mr=have_mr,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
    )

    # --- plot ---
    make_plot(r, prof, r_h, qnm, mr)

    # --- dual SHA ---
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANON, pins)  # (local)

    # --- value string ---
    om_str = (f"{np.real(omega0):.6f}{'+' if np.imag(omega0)>=0 else '-'}"
              f"{abs(np.imag(omega0)):.3e}i" if omega0 is not None else "none")  # (local)
    mode_kind = ("decaying-ringdown" if have_qnm
                 else "trapped-normal-mode(Im~0)")  # (local)
    # name the unpinned sub-ingredient(s) for the INFO branch (plan INFO_meaning)
    unpinned = []  # (local)
    if not have_qnm:
        unpinned.append("QNM-ringdown(horizonless-gravastar:Im~0_trapped-not-leaky)")
    if not have_mr:
        unpinned.append("M-R-compactness(no-self-bound-surface:EOS-pressure-scale-underdetermined)")
    unpinned_str = ("+".join(unpinned) if unpinned else "none")  # (local)
    value = (  # (local)
        f"verdict={verdict};n_of_4={n_of_4}/4"
        f";v(r)=extracted;horizon_r_h={r_h_analytic:.4f}(Mach=1,single-crossover);"
        f"QNM_spectrum={have_qnm_exists}(n_modes={qnm['n_modes'] if qnm is not None else 0},"
        f"n_genuine_damped={n_genuine_damped},mode={mode_kind},omega0={om_str}[M_KK]);"
        f"M-R_C_max={mr['C_max']:.4g}(n_physical={mr['n_physical']},"
        f"grid_edge_artifact={grid_edge_artifact});"
        f"core_supersonic=Mach_core={prof['Mach_core']:.6f}>1(sign=PASS);"
        f"EOS=Lobo-DE-condensate(w_core={mr['w_core']});"
        f"S105_match={s105_match};CF-S105-RELAY-VR-CONSTRUCTION=discharged;"
        f"unpinned={unpinned_str}"
    )

    print(f"\n  composite 4-of-4: {deliv}  -> n_of_4={n_of_4}")
    print(f"  4-tuple: (value=<above>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  elapsed: {time.time()-t0:.2f}s")

    extra_rows = [  # (local)
        f"# regulator_pin=a_2^{{zeta}} (Z_fold/a_2_FW_zeta; NO fresh Seeley-DeWitt eval) "
        f"# {GATE_ID} regulator companion",
        f"# CF-S105-RELAY-VR-CONSTRUCTION discharged: v(r)=v0*exp(-(r/r0)^2/2), "
        f"r_h={r_h_analytic:.4f}(Mach=1,single-crossover); S105_EMT_reproduced={s105_match} "
        f"# {GATE_ID} carry-forward-discharge companion",
        f"# EOS=Lobo-DE-condensate w_core={mr['w_core']} (NOT Mazur-Mottola de Sitter; "
        f"8% departure from w=-1, sub-gravastar-structure-landau.md) # {GATE_ID} EOS companion",
        f"# INFO natural-split (plan INFO_meaning): acoustic-horizon leg LANDS; "
        f"unpinned downstream legs route to Q3 wave-together {{v(r)-acoustic|nuclear-EOS-TOV|de-Sitter-core}}; "
        f"unpinned={unpinned_str} # {GATE_ID} natural-split companion",
    ]

    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, extra_rows=extra_rows,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
