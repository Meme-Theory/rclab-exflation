"""
S96-OBS-LRD-ASSEMBLY-CLOCK  —  LRD assembly-clock proxy t(z) from the
SCALE-FACTOR-54 Connes-distance a(tau)
=============================================================================

Session 96, Wave 6, Gate 5  —  little-red-dots-jwst-analyst

[SIGN] GATE (GEOMETRIC).  Build the LRD-epoch cosmic-time proxy t(z) from the
SCALE-FACTOR-54 Connes-distance a(tau) (the proxy carrying the REAL deceleration
band q: -0.97 -> +0.81, NOT a_eff whose q_Omega diverges / is near-flat), and
report the assembly-clock ratio R_clock(z=6) = t_proxy(z=6)/t_LCDM(z=6) AS A
FUNCTION of the open M_KK^-1 -> seconds normalization knob.

SUBSTRATE-FIRST FRAMING (GEOMETRIC):
  The assembly clock is the READOUT of the substrate's spectral-complexity
  growth.  a(tau) is the Connes-distance scale factor (the mean distance between
  states on the spectral triple grows as the Jensen deformation proceeds), and
  t(z) is the elapsed-time integral of that growth.  This is NOT "cosmic time in
  an expanding container": the substrate IS the growing spectral complexity, and
  "the LRD assembly timeline" is how much of that growth has happened by a given
  redshift.

  Chain:  D_K eigenvalues -> Jensen deformation tau -> Connes distance <d_D>(tau)
          -> a(tau) (SCALE-FACTOR-54) -> H_proxy = dln(a)/dtau -> t(z) integral.

THE TWO OPEN PIECES (per substrate-first-canonical-sourcing.md: do NOT invent
them; SWEEP/DECLARE and report the verdict as a function of them):
  (K) M_KK^-1 -> seconds : kappa = seconds per M_KK^-1.  The OVERALL multiplicative
      scale on t_proxy.  Swept over [1e-20, 1e-10] s/M_KK^-1 (log-decade), per
      the plan machinery pin.  The natural-units value kappa_nat = hbar/(M_KK c^2)
      = 8.86e-42 s is reported for context (it lies FAR below the swept band).
  (A) a_now (the z=0 anchor) : 1+z = a_now/a(tau).  The proxy a-grid only spans
      a in [1, 3.494] (tau in [0, 0.347]); it does NOT internally reach z=4,6,8.
      a_now is a DECLARED anchor; a(tau) is extended along the FITTED exponential
      a = A_exp exp(B_exp tau) (R^2=0.997) to reach the LRD a-values.  Two anchor
      readings reported (grid-endpoint and fold-anchored); the verdict driver is
      the multiplicative kappa knob, which is anchor-independent up to an O(1)
      Delta-tau factor.

ELAPSED-TIME INTEGRAL (the key identity):
  H_proxy(tau) = dln(a)/dtau   [the s54 'H' array, per-tau units]
  =>  dtau = dln(a)/H_proxy   =>  Delta-tau(a1->a2) = int_{a1}^{a2} dln(a)/H_proxy
  (this is DIMENSIONLESS elapsed-tau; cross-checked to recover the tau-grid span)
  tau -> M_KK^-1:  dt = dtau / omega_tau   (omega_tau = dtau/dt = 8.27, M_KK units)
  M_KK^-1 -> s:    t_proxy[s] = kappa * dt[M_KK^-1] = (kappa/omega_tau) * Delta-tau

OPERATOR (pre-registered, plan W6-5):
  R_clock = t_proxy(z=6) / t_LCDM(z=6) ;  PASS iff R_clock in [0.5, 2.0] for SOME
  normalization (kappa in the swept band) ; INFO if [0.1,0.5]u[2,10] ; FAIL if
  >10x or <0.1x at ALL normalizations.

ANCHORS (knowledge MCP, query-first; verified 2026-05-29):
  - SCALE-FACTOR-54 (PASS, little-red-dots-synthesis): q -27% -> +81% Connes-distance
    proxy; carries the deceleration band; NOT a_eff (II.1).  a(tau_fold)/a(0)=2.117.
  - s54_scale_factor.npz: a, H(=dln a/dtau), q, tau, a_at_fold=2.1173, q_at_fold=-0.786.
  - omega_tau = 8.27 (dtau/dt, M_KK units, S38 attractor).
  - dt_transit = 1.1302e-3 M_KK^-1 (transit duration, S38; the only derived rate).
  - Planck 2018: H_0 = 67.4 km/s/Mpc, Omega_m = 0.315.

OUTPUT to W6-3 (CGWB-PEAK-FREQ, dispatched AFTER this gate):
  npz keys for the a(tau)->z map + normalization knob are EXPLICIT (see header
  comment on the np.savez block).  a_fold_over_a_now and kappa_sweep are the
  load-bearing exports.

Author: little-red-dots-jwst-analyst
Date:   2026-05-29
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # (local) CPU-cap; O(500) quadrature, no GPU
os.environ.setdefault("MKL_NUM_THREADS", "8")     # (local)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np

# --- paths ------------------------------------------------------------------
THIS = Path(__file__).resolve()                                    # (local)
SESS_DIR = THIS.parent                                             # (local) computations/session-96
SHARED_DIR = (SESS_DIR.parent / "_shared").resolve()              # (local) computations/_shared
PROJECT_ROOT = SESS_DIR.parent.parent.resolve()                   # (local)
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (                                  # noqa: E402  framework constants
    tau_fold, M_KK, omega_tau, dt_transit,
    H_0_inv_s, H_0_km_s_Mpc, Omega_m,
)

GATE_ID = "S96-OBS-LRD-ASSEMBLY-CLOCK"
SCHEME = "Connes-distance-a(tau)-proxy-NOT-a_eff"
CONVENTION = "substrate-fold-rate-tau-dot-local-NOT-borrowed-H"
L_MAX = "NA"                                                       # (local) scale-factor integral, no spectral truncation

S54_NPZ = SESS_DIR.parent / "session-54" / "s54_scale_factor.npz"  # (local)
CANON = SHARED_DIR / "canonical_constants.py"                      # (local)
OUT_NPZ = SESS_DIR / "s96_obs_lrd_assembly_clock.npz"             # (local)
OUT_PNG = SESS_DIR / "s96_obs_lrd_assembly_clock.png"            # (local)
VERDICT_TXT = SESS_DIR / "s96_gate_verdicts.txt"                  # (local)

# ---- pre-registered machinery pins (plan W6-5) -----------------------------
N_EVAL = 500                                                       # (local) a-grid points for the t(z) integral
KAPPA_LO = 1e-20                                                   # (local) M_KK^-1 -> s sweep lower (s/M_KK^-1)
KAPPA_HI = 1e-10                                                   # (local) M_KK^-1 -> s sweep upper
N_KAPPA = 121                                                      # (local) log-decade sweep points over [1e-20,1e-10]
TOL = 1e-6                                                         # (local) quadrature tol
LRD_REDSHIFTS = (4.0, 6.0, 8.0)                                    # (local) the LRD epoch
R_CLOCK_PASS = (0.5, 2.0)                                          # (local) PASS band on R_clock(z=6)
R_CLOCK_INFO_LO = (0.1, 0.5)                                       # (local) INFO band (low side)
R_CLOCK_INFO_HI = (2.0, 10.0)                                      # (local) INFO band (high side)

# physical constants for kappa_nat (M_KK^-1 -> s in natural units), CONTEXT ONLY
HBAR_GEV_S = 6.582119569e-25                                       # (local) hbar [GeV s] (PDG)


# ---------------------------------------------------------------------------
# SHA-256 dual-pin block  (S84+ schema; mirrors the S96 canonical idiom)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                        # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                            # (local)
    h_audit = hashlib.sha256()                                   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                  # (local)
    h_content = hashlib.sha256()                                 # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                              # (local)
    return audit, content


def _prior_audit_sha() -> str:
    """audit_sha256 of the most-recent prior canonical line for GATE_ID (Option A
    supersedes tag), or '' if none.  Verdict permanence: never edit the prior line."""
    if not VERDICT_TXT.exists():
        return ""
    prior = ""                                                   # (local)
    try:
        for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
            if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
                prior = ln.split("audit_sha256=", 1)[1].split()[0]  # (local)
    except OSError:
        return ""
    return prior


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str,
                   supersedes: str = "") -> None:
    sup = f" supersedes={supersedes}" if supersedes else ""       # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r}{sup} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                            # (local)
    comp = (f"# audit_sha256_short={audit_sha[:16]} "
            f"content_sha256_short={content_sha[:16]} "
            f"# {GATE_ID} dual-SHA companion row"
            + (f" supersedes={supersedes}" if supersedes else "")
            + "\n")                                              # (local)
    tuple_row = (f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
                 f"regime_verdict={regime_v} "
                 f"# {GATE_ID} 3-tuple annotation (schema-v2)\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comp)
        fp.write(tuple_row)


# ---------------------------------------------------------------------------
# LCDM cosmic-time anchor  t_LCDM(z) = (1/H0) int_z^inf dz'/((1+z') E(z'))
# ---------------------------------------------------------------------------
def lcdm_age(z: float) -> float:
    """LCDM age at redshift z [seconds]; Planck 2018 H_0, Omega_m (flat)."""
    from scipy import integrate
    OL = 1.0 - Omega_m                                           # (local) flat closure
    def E(zp):
        return np.sqrt(Omega_m * (1.0 + zp) ** 3 + OL)          # (local)
    f = lambda zp: 1.0 / ((1.0 + zp) * E(zp))                    # (local)
    val, _ = integrate.quad(f, z, np.inf)                       # (local)
    return val / H_0_inv_s


# ---------------------------------------------------------------------------
# Proxy elapsed-tau integral and the a(tau)->z map
# ---------------------------------------------------------------------------
def build_proxy():
    """Load SCALE-FACTOR-54 a(tau), H_proxy(tau)=dln a/dtau, q(tau).
    Return the grid, the exponential fit, and the cross-check that the
    int dln(a)/H_proxy recovers the tau-span (validates H = dln a/dtau)."""
    d = np.load(S54_NPZ)                                         # (local)
    tau = d["tau"].astype(float)                                # (local) [0, 0.347]
    a = d["a"].astype(float)                                    # (local) [1, 3.494]
    H = d["H"].astype(float)                                    # (local) = dln a/dtau (per-tau)
    q = d["q"].astype(float)                                    # (local) -0.973 -> +0.814
    a_at_fold = float(d["a_at_fold"])                           # (local) 2.1173
    q_at_fold = float(d["q_at_fold"])                           # (local) -0.786
    A_exp = float(d["A_exp"])                                   # (local) 1.0493
    B_exp = float(d["B_exp"])                                   # (local) 3.5322
    R2_exp = float(d["R2_exp"])                                 # (local) 0.9973

    # cross-check: int dln(a)/H_proxy over the full grid == tau-span?
    lna = np.log(a)                                             # (local)
    dtau_recovered = float(np.trapezoid(1.0 / H, lna))         # (local)
    tau_span = float(tau[-1] - tau[0])                          # (local)
    recover_err = abs(dtau_recovered - tau_span) / tau_span     # (local)

    return {
        "tau": tau, "a": a, "H": H, "q": q,
        "a_at_fold": a_at_fold, "q_at_fold": q_at_fold,
        "A_exp": A_exp, "B_exp": B_exp, "R2_exp": R2_exp,
        "lna": lna, "dtau_recovered": dtau_recovered,
        "tau_span": tau_span, "recover_err": recover_err,
    }


def a_of_tau_fit(tau, A_exp, B_exp):
    return A_exp * np.exp(B_exp * tau)                          # (local) fitted scale factor


def tau_of_a_fit(a_val, A_exp, B_exp):
    return np.log(a_val / A_exp) / B_exp                        # (local) inverse fit


def Hproxy_of_tau_interp(tau_query, tau_grid, H_grid, B_exp):
    """H_proxy(tau) = dln a/dtau.  Inside the grid: linear interp of the s54 H.
    Outside (tau<0 LRD extrapolation): the exponential-fit asymptote dln a/dtau
    -> B_exp (since a = A exp(B tau) => dln a/dtau = B_exp exactly).  We blend by
    using the grid where covered and B_exp where extrapolated."""
    tq = np.atleast_1d(np.asarray(tau_query, dtype=float))      # (local)
    out = np.empty_like(tq)                                     # (local)
    inside = (tq >= tau_grid[0]) & (tq <= tau_grid[-1])         # (local)
    out[inside] = np.interp(tq[inside], tau_grid, H_grid)       # (local)
    out[~inside] = B_exp                                        # (local) fit asymptote dln a/dtau = B
    return out


def delta_tau_integral(a_lo, a_hi, prox, n=N_EVAL):
    """Delta-tau(a_lo -> a_hi) = int_{a_lo}^{a_hi} dln(a)/H_proxy(a) [dimensionless].
    H_proxy is mapped via tau(a) from the exponential fit, then evaluated against
    the s54 grid where covered (and the B_exp asymptote where extrapolated)."""
    lna_grid = np.linspace(np.log(a_lo), np.log(a_hi), n)       # (local) uniform in ln a
    a_grid = np.exp(lna_grid)                                   # (local)
    tau_grid_q = tau_of_a_fit(a_grid, prox["A_exp"], prox["B_exp"])  # (local)
    Hq = Hproxy_of_tau_interp(tau_grid_q, prox["tau"], prox["H"], prox["B_exp"])  # (local)
    integrand = 1.0 / Hq                                        # (local) dln(a)/H_proxy density
    return float(np.trapezoid(integrand, lna_grid))            # (local) elapsed tau (dimensionless)


def lna_path_covered_fraction(a_lo, a_hi, prox):
    """Fraction of the ln-a integration path [ln a_lo, ln a_hi] that lies INSIDE
    the measured s54 grid [ln a_grid_lo, ln a_grid_hi] (the rest is exp-fit
    extrapolation).  Drives the regime verdict."""
    seg_lo, seg_hi = np.log(a_lo), np.log(a_hi)                 # (local)
    g_lo, g_hi = np.log(prox["a"][0]), np.log(prox["a"][-1])    # (local)
    overlap = max(0.0, min(seg_hi, g_hi) - max(seg_lo, g_lo))   # (local)
    total = seg_hi - seg_lo                                     # (local)
    return overlap / total if total > 0 else 0.0               # (local)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    INPUT_FILES = [CANON, S54_NPZ]                              # (local)
    print("=" * 78)
    print(f"  {GATE_ID}  —  LRD assembly-clock t(z) from SCALE-FACTOR-54 a(tau)")
    print("=" * 78)
    pins = log_input_pins(INPUT_FILES)                          # (local)
    audit_sha, content_sha = compute_dual_sha(THIS, CANON, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print(f"  tau_fold={tau_fold}  M_KK={M_KK:.6e} GeV  omega_tau={omega_tau} (dtau/dt, M_KK units)")
    print(f"  dt_transit={dt_transit:.6e} M_KK^-1  Planck H_0={H_0_km_s_Mpc} km/s/Mpc  Omega_m={Omega_m}")
    print()

    # ---- (1) proxy load + validation --------------------------------------
    prox = build_proxy()                                        # (local)
    print("  --- (1) SCALE-FACTOR-54 a(tau) proxy ---")
    print(f"  tau in [{prox['tau'][0]:.4f}, {prox['tau'][-1]:.4f}]  "
          f"a in [{prox['a'][0]:.4f}, {prox['a'][-1]:.4f}]  "
          f"q in [{prox['q'].min():.4f}, {prox['q'].max():.4f}]")
    print(f"  a_at_fold={prox['a_at_fold']:.6f} (tau_fold)  q_at_fold={prox['q_at_fold']:.6f}")
    print(f"  exp fit a=A exp(B tau): A={prox['A_exp']:.6f} B={prox['B_exp']:.6f} R^2={prox['R2_exp']:.6f}")
    print(f"  CROSS-CHECK int dln(a)/H_proxy = {prox['dtau_recovered']:.6f} vs tau-span "
          f"{prox['tau_span']:.6f} (rel.err {prox['recover_err']:.2e})  "
          f"[validates H_proxy = dln a/dtau]")
    print()

    # ---- (2) LCDM anchors --------------------------------------------------
    t_lcdm = {z: lcdm_age(z) for z in (0.0,) + LRD_REDSHIFTS}   # (local) seconds
    GYR = 3.15576e16                                            # (local) s per Gyr
    print("  --- (2) LCDM cosmic-time anchors (Planck 2018) ---")
    for z in (0.0,) + LRD_REDSHIFTS:
        print(f"  t_LCDM(z={z:.0f}) = {t_lcdm[z]:.4e} s = {t_lcdm[z]/GYR:.4f} Gyr")
    print()

    # ---- (3) AGE-at-z definition + a_now anchor (z=0 placement) -------------
    # CORRECTED clock definition: t_age(z) = elapsed proxy time from the
    # COSMOGENESIS ORIGIN (a=1 at tau=0, the cold big bang) UP TO a(z):
    #   t_age(z) = (kappa/omega_tau) * int_{a=1}^{a(z)} dln(a)/H_proxy
    # Both t_age(z) and t_LCDM(z) are AGES (origin -> z), so both DECREASE with z
    # (apples-to-apples; the prior draft integrated lookback time, which is the
    # WRONG comparison vs the LCDM age).
    #
    # Redshift map 1+z = a_now/a(z) => a(z) = a_now/(1+z).  The a-grid spans a
    # FACTOR 3.494 in a, but the LRD ladder from cosmogenesis (a=1) to now needs
    # a factor (1+z_now-to-z) >= 9 to host z=8 -- this RANGE DEFICIT is the open
    # piece.  We choose a_now so the HIGHEST LRD redshift maps near the origin and
    # the z=4,6 integrals stay INSIDE the measured grid [1, 3.494]; a_now is itself
    # an exp-fit EXTRAPOLATION of the now-anchor (openly declared, NOT invented).
    a0_origin = float(prox["a"][0])                            # (local) 1.0 at tau=0 (cosmogenesis)
    a_end = float(prox["a"][-1])                               # (local) 3.494 (grid endpoint)
    a_fold = float(prox["a_at_fold"])                          # (local) 2.117 (fold)
    z_max = max(LRD_REDSHIFTS)                                 # (local) 8.0
    # PRIMARY anchor: a_now places z_max=8 just ABOVE the origin so its age integral
    # is non-degenerate and all LRD a(z) sit inside the grid.  a_now = (1+z_max)*a_lo
    # with a_lo = a_fold/(1+z_max-... ) -> choose a(z=8)=a_fold/?... cleanest: set
    # a(z=8) = a_fold (the fold) => a_now = (1+8)*a_fold = 9*2.117 = 19.06.  Then
    # a(z=6)=2.723, a(z=4)=3.812 -- z=6 inside grid, z=4 just outside endpoint.
    a_now_primary = (1.0 + z_max) * a_fold                    # (local) 19.06; z=8 -> the fold
    # COMPANION anchor: a(z=8)=origin a=1 => a_now=9; a(z=6)=1.286, a(z=4)=1.8 (all
    # inside grid, but age(z=8)=0 degenerate).  Reported as a sensitivity bracket.
    a_now_companion = (1.0 + z_max) * a0_origin               # (local) 9.0; z=8 -> origin

    anchors = {                                                # (local) name -> a_now
        "A_zmax_at_fold": a_now_primary,
        "A_zmax_at_origin": a_now_companion,
    }
    PRIMARY_ANCHOR = "A_zmax_at_fold"                          # (local)

    # ---- (4) AGE integral t_age(z) (origin -> a(z)) for each anchor, each z --
    print("  --- (3+4) a_now anchors + AGE integral t_age(z)=int_{a=1}^{a(z)} ---")
    results = {}                                               # (local) anchor -> {z -> dict}
    for aname, a_now in anchors.items():
        results[aname] = {}
        print(f"  [anchor {aname}: a_now={a_now:.4f}  (z=0 placement)]")
        for z in LRD_REDSHIFTS:
            a_z = a_now / (1.0 + z)                            # (local) scale factor at z
            tau_z = tau_of_a_fit(a_z, prox["A_exp"], prox["B_exp"])  # (local)
            if a_z <= a0_origin:
                # a(z) at/below cosmogenesis origin -> age ~ 0 (degenerate edge)
                age_dtau = 0.0                                # (local)
                frac_in = 1.0                                 # (local) trivial
            else:
                age_dtau = delta_tau_integral(a0_origin, a_z, prox)  # (local) origin -> a(z)
                frac_in = lna_path_covered_fraction(a0_origin, a_z, prox)  # (local)
            results[aname][z] = {"a_z": a_z, "tau_z": tau_z,
                                 "age_dtau": age_dtau, "frac_in": frac_in}
            print(f"    z={z:.0f}: a(z)={a_z:.4f} tau(z)={tau_z:+.4f} "
                  f"age_dtau(origin->z)={age_dtau:.6f} covered_frac={frac_in:.3f}")
    print()

    # ---- (5) kappa sweep: t_age(z) = (kappa/omega_tau)*age_dtau, R_clock -----
    kappa_nat = HBAR_GEV_S / M_KK                              # (local) s per M_KK^-1 (natural; context)
    kappa_sweep = np.logspace(np.log10(KAPPA_LO), np.log10(KAPPA_HI), N_KAPPA)  # (local)

    print("  --- (5) kappa sweep + R_clock(z=6) ---")
    print(f"  kappa_nat = hbar/M_KK = {kappa_nat:.4e} s/M_KK^-1 (natural units; CONTEXT)")
    print(f"  kappa swept [{KAPPA_LO:.0e}, {KAPPA_HI:.0e}] s/M_KK^-1 ({N_KAPPA} pts)")
    print()

    age6_primary = results[PRIMARY_ANCHOR][6.0]["age_dtau"]    # (local) dimensionless age at z=6
    # R_clock(z=6) = t_age_proxy(z=6)/t_LCDM(z=6) = (kappa/omega_tau)*age6 / t_lcdm6
    t_age6 = (kappa_sweep / omega_tau) * age6_primary          # (local) seconds, vs kappa
    R_clock6 = t_age6 / t_lcdm[6.0]                           # (local) ratio vs kappa
    # kappa* that lands R_clock(z=6)=1:  kappa* = omega_tau*t_lcdm6/age6
    kappa_star = omega_tau * t_lcdm[6.0] / age6_primary        # (local) s/M_KK^-1 for R_clock=1
    kappa_for_Rlo = R_CLOCK_PASS[0] * omega_tau * t_lcdm[6.0] / age6_primary  # (local)
    kappa_for_Rhi = R_CLOCK_PASS[1] * omega_tau * t_lcdm[6.0] / age6_primary  # (local)

    in_pass = (R_clock6 >= R_CLOCK_PASS[0]) & (R_clock6 <= R_CLOCK_PASS[1])  # (local)
    any_pass = bool(np.any(in_pass))                          # (local)
    in_info = (((R_clock6 >= R_CLOCK_INFO_LO[0]) & (R_clock6 < R_CLOCK_INFO_LO[1]))
               | ((R_clock6 > R_CLOCK_INFO_HI[0]) & (R_clock6 <= R_CLOCK_INFO_HI[1])))  # (local)
    any_info = bool(np.any(in_info))                          # (local)
    kappa_star_in_band = bool(KAPPA_LO <= kappa_star <= KAPPA_HI)  # (local)
    R_clock6_at_lo = float(R_clock6[0])                       # (local)
    R_clock6_at_hi = float(R_clock6[-1])                      # (local)

    print(f"  [PRIMARY anchor {PRIMARY_ANCHOR}] age_dtau(z=6)={age6_primary:.6f}")
    print(f"  kappa* (R_clock(z=6)=1) = {kappa_star:.4e} s/M_KK^-1  "
          f"(in swept band [{KAPPA_LO:.0e},{KAPPA_HI:.0e}]? {kappa_star_in_band})")
    print(f"  kappa band for R_clock in [0.5,2.0]: "
          f"[{kappa_for_Rlo:.4e}, {kappa_for_Rhi:.4e}] s/M_KK^-1")
    print(f"  R_clock(z=6) at kappa=KAPPA_LO={KAPPA_LO:.0e}: {R_clock6_at_lo:.4e}")
    print(f"  R_clock(z=6) at kappa=KAPPA_HI={KAPPA_HI:.0e}: {R_clock6_at_hi:.4e}")
    print(f"  ANY kappa in swept band -> R_clock in [0.5,2.0]? {any_pass}")
    print(f"  ANY kappa in swept band -> R_clock in INFO band?  {any_info}")
    print(f"  kappa_nat={kappa_nat:.3e} gives R_clock(z=6) = "
          f"{(kappa_nat/omega_tau)*age6_primary/t_lcdm[6.0]:.4e} (natural-units; far below band)")
    print()

    Rclock_at_star = {}                                       # (local)
    print("  --- R_clock(z) at kappa* (primary anchor), all LRD z ---")
    for z in LRD_REDSHIFTS:
        agz = results[PRIMARY_ANCHOR][z]["age_dtau"]          # (local)
        tpz = (kappa_star / omega_tau) * agz                  # (local)
        Rclock_at_star[z] = tpz / t_lcdm[z]                   # (local)
        print(f"  z={z:.0f}: t_age_proxy={tpz:.4e}s  t_LCDM={t_lcdm[z]:.4e}s  "
              f"R_clock={Rclock_at_star[z]:.4f}")
    print()

    # ---- (6) verdict (pre-registered) -------------------------------------
    # SIGN: a GROWS from the fold; AGE from cosmogenesis (a=1) up to a(z)
    #   DECREASES with z (lower z = more elapsed age).  Substitution chain:
    #     t_age(z) = int_{1}^{a(z)} dln(a)/H_proxy ; a(z)=a_now/(1+z) DECREASES with z
    #     => shorter integration path => SMALLER age at higher z.
    #   Direction claim PASS iff age(z=4) > age(z=6) > age(z=8).
    age4 = results[PRIMARY_ANCHOR][4.0]["age_dtau"]           # (local)
    age6 = results[PRIMARY_ANCHOR][6.0]["age_dtau"]           # (local)
    age8 = results[PRIMARY_ANCHOR][8.0]["age_dtau"]           # (local)
    clock_orders = bool(age4 > age6 > age8)                   # (local) lower z -> larger age
    sign_v = "PASS" if clock_orders else "FAIL"              # (local) matches standard cosmology direction

    # MAGNITUDE: does SOME normalization land R_clock(z=6) in [0.5,2.0]?
    if any_pass:
        mag_v = "PASS"                                        # (local)
    elif any_info:
        mag_v = "INFO"                                        # (local)
    else:
        mag_v = "FAIL"                                        # (local)

    # REGIME: covered fraction of the z=6 AGE integral path [a=1, a(z=6)] inside the
    # measured grid (the rest is exp-fit extrapolation; the OPEN a_now anchor pushes
    # a(z=6) toward/past the grid endpoint).
    frac_inside = results[PRIMARY_ANCHOR][6.0]["frac_in"]    # (local)
    if frac_inside >= 0.95:
        regime_v = "VALID"                                   # (local)
    elif frac_inside >= 0.50:
        regime_v = "MARGINAL"                                # (local)
    else:
        regime_v = "BREAKDOWN"                               # (local) >50% extrapolated

    # composite collapse (pre-registered rule, gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"                                   # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"                                   # (local) sign-correct, mag-wrong-out-of-regime
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print("  --- (6) verdict 3-tuple (pre-registered) ---")
    print(f"  clock orders age(z=4)>age(z=6)>age(z=8): {age4:.4f}>{age6:.4f}>{age8:.4f} = {clock_orders}")
    print(f"  SIGN     = {sign_v}  (a grows from cosmogenesis => lower z = larger age)")
    print(f"  MAGNITUDE= {mag_v}  (some swept kappa -> R_clock(z=6) in [0.5,2.0]? {any_pass}; INFO-band? {any_info})")
    print(f"  REGIME   = {regime_v}  (z=6 age-integral covered fraction = {frac_inside:.3f}; "
          f"extrapolated = {1-frac_inside:.3f})")
    print(f"  COMPOSITE= {composite}")
    print()

    value_str = (
        f"R_clock(z=6)_normalization-conditional:kappa*={kappa_star:.3e}s/M_KK^-1_"
        f"in_swept_band[1e-20,1e-10]={kappa_star_in_band}_any_kappa_PASS={any_pass}_"
        f"R_clock(KAPPA_LO)={R_clock6_at_lo:.2e}_R_clock(KAPPA_HI)={R_clock6_at_hi:.2e}_"
        f"kappa_nat={kappa_nat:.2e}_clock_orders={clock_orders}_NOT_a_eff_q-band=[-0.97,+0.81]"
    )                                                          # (local)

    # ---- save data (EXPLICIT keys for W6-3 CGWB-PEAK-FREQ consumer) --------
    # W6-3 needs: the a(tau)->z redshift factor + the M_KK^-1->s normalization knob.
    #   a_fold_over_a0_computed : the DIRECTLY-resolved redshift factor a_fold/a(0)=2.117
    #   kappa_sweep             : the M_KK^-1->s normalization knob (s/M_KK^-1)
    #   kappa_star              : the knob value that makes R_clock(z=6)=1
    #   kappa_nat               : natural-units knob hbar/M_KK (context)
    #   omega_tau_used, a_fold, a_now_primary : the chain pieces
    a_fold_over_a_now_primary = a_fold / anchors[PRIMARY_ANCHOR]  # (local) redshift factor a_fold/a_now
    np.savez(
        OUT_NPZ,
        # --- proxy grid ---
        tau=prox["tau"], a=prox["a"], H_proxy=prox["H"], q=prox["q"],
        a_at_fold=np.array([prox["a_at_fold"]]),
        q_at_fold=np.array([prox["q_at_fold"]]),
        A_exp=np.array([prox["A_exp"]]), B_exp=np.array([prox["B_exp"]]),
        R2_exp=np.array([prox["R2_exp"]]),
        dtau_recovered=np.array([prox["dtau_recovered"]]),
        recover_err=np.array([prox["recover_err"]]),
        # --- LCDM anchors ---
        z_lrd=np.array(LRD_REDSHIFTS),
        t_lcdm_z0=np.array([t_lcdm[0.0]]),
        t_lcdm_lrd=np.array([t_lcdm[z] for z in LRD_REDSHIFTS]),
        # --- a_now anchors + AGE integral age_dtau(origin->z) ---
        anchor_names=np.array(list(anchors.keys()), dtype=object),
        anchor_a_now=np.array(list(anchors.values())),
        primary_anchor=np.array([PRIMARY_ANCHOR]),
        age_dtau_z_primary=np.array([results[PRIMARY_ANCHOR][z]["age_dtau"] for z in LRD_REDSHIFTS]),
        a_z_primary=np.array([results[PRIMARY_ANCHOR][z]["a_z"] for z in LRD_REDSHIFTS]),
        tau_z_primary=np.array([results[PRIMARY_ANCHOR][z]["tau_z"] for z in LRD_REDSHIFTS]),
        frac_in_z_primary=np.array([results[PRIMARY_ANCHOR][z]["frac_in"] for z in LRD_REDSHIFTS]),
        age_dtau_z_companion=np.array([results["A_zmax_at_origin"][z]["age_dtau"] for z in LRD_REDSHIFTS]),
        # === W6-3 (CGWB-PEAK-FREQ) CONSUMER KEYS (explicit) ===
        kappa_sweep=kappa_sweep,                  # M_KK^-1 -> s normalization knob (s/M_KK^-1)
        kappa_star=np.array([kappa_star]),        # knob value for R_clock(z=6)=1
        kappa_nat=np.array([kappa_nat]),          # natural-units knob hbar/M_KK (context)
        kappa_lo=np.array([KAPPA_LO]), kappa_hi=np.array([KAPPA_HI]),
        omega_tau_used=np.array([omega_tau]),     # dtau/dt (M_KK units)
        a_fold_over_a_now_primary=np.array([a_fold_over_a_now_primary]),  # redshift factor a_fold/a_now
        a_fold_value=np.array([a_fold]),
        a_now_primary=np.array([anchors[PRIMARY_ANCHOR]]),
        # the COMPUTED-window redshift factor a_fold/a(0)=2.117 (DIRECTLY resolved; W6-3 anchor)
        a_fold_over_a0_computed=np.array([prox["a_at_fold"] / float(prox["a"][0])]),
        # --- R_clock vs kappa (primary anchor, z=6) ---
        R_clock6_vs_kappa=R_clock6,
        R_clock6_at_kappa_lo=np.array([R_clock6_at_lo]),
        R_clock6_at_kappa_hi=np.array([R_clock6_at_hi]),
        kappa_star_in_band=np.array([kappa_star_in_band]),
        any_kappa_pass=np.array([any_pass]),
        any_kappa_info=np.array([any_info]),
        Rclock_at_star_z=np.array([Rclock_at_star[z] for z in LRD_REDSHIFTS]),
        # --- verdict ---
        clock_orders=np.array([clock_orders]),
        frac_inside_z6=np.array([frac_inside]),
        sign_verdict=np.array([sign_v]),
        magnitude_verdict=np.array([mag_v]),
        regime_verdict=np.array([regime_v]),
        composite=np.array([composite]),
        value_str=np.array([value_str]),
        scheme=np.array([SCHEME]), convention=np.array([CONVENTION]),
    )
    print(f"  [data saved: {OUT_NPZ.name}]")

    make_plot(prox, results, anchors, PRIMARY_ANCHOR, kappa_sweep, R_clock6,
              kappa_star, kappa_nat, t_lcdm, LRD_REDSHIFTS)

    # ---- emit verdict ------------------------------------------------------
    supersedes = _prior_audit_sha()                            # (local)
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, regime_v, supersedes=supersedes)
    print()
    print("=" * 78)
    print(f"  {GATE_ID}: {composite}  (sign={sign_v}, mag={mag_v}, regime={regime_v})")
    print(f"  R_clock(z=6) is NORMALIZATION-CONDITIONAL on the open M_KK^-1->s knob kappa.")
    print(f"  kappa*={kappa_star:.3e} s/M_KK^-1 lands R_clock=1; in swept band? {kappa_star_in_band}")
    print(f"  value = {value_str}")
    if supersedes:
        print(f"  supersedes = {supersedes[:16]}...")
    print("=" * 78)
    return 0


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(prox, results, anchors, primary, kappa_sweep, R_clock6,
              kappa_star, kappa_nat, t_lcdm, lrd_z):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:                                    # noqa: BLE001
        print(f"  [plot skipped: {exc}]")
        return
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(r"S96-OBS-LRD-ASSEMBLY-CLOCK: $t(z)$ from SCALE-FACTOR-54 "
                 r"$a(\tau)$ Connes-distance proxy (NOT $a_{\rm eff}$)",
                 fontsize=12, fontweight="bold")

    # (a) a(tau) proxy + exp fit + fold
    ax = axes[0, 0]
    ax.plot(prox["tau"], prox["a"], "bo-", lw=1.5, ms=4, label=r"$a(\tau)$ (SCALE-FACTOR-54)")
    tt = np.linspace(prox["tau"][0], prox["tau"][-1], 200)     # (local)
    ax.plot(tt, prox["A_exp"] * np.exp(prox["B_exp"] * tt), "r--", lw=1.2,
            label=r"fit $a=A e^{B\tau}$")
    ax.axvline(tau_fold, color="orange", ls=":", lw=1.2, label=r"$\tau_{fold}$")
    ax.axhline(prox["a_at_fold"], color="orange", ls=":", lw=0.8, alpha=0.6)
    ax.set_xlabel(r"$\tau$ (Jensen deformation)"); ax.set_ylabel(r"$a(\tau)$ (Connes distance)")
    ax.set_title(r"(a) Connes-distance scale factor grows from the fold")
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # (b) q(tau) deceleration band
    ax = axes[0, 1]
    ax.plot(prox["tau"], prox["q"], "g-o", lw=1.5, ms=4)
    ax.axhline(0.0, color="k", ls="--", lw=1, label=r"$q=0$ (accel/decel transition)")
    ax.axvline(tau_fold, color="orange", ls=":", lw=1.2, label=r"$\tau_{fold}$")
    ax.fill_between(prox["tau"], prox["q"].min(), prox["q"].max(), alpha=0.05, color="green")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$q(\tau)$ deceleration")
    ax.set_title(r"(b) Deceleration band $q:-0.97\to+0.81$ (the REAL band; $a_{\rm eff}$ near-flat)")
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # (c) R_clock(z=6) vs kappa (the open normalization knob)
    ax = axes[1, 0]
    ax.loglog(kappa_sweep, R_clock6, "b-", lw=2, label=r"$R_{\rm clock}(z{=}6)$ vs $\kappa$")
    ax.axhspan(0.5, 2.0, color="green", alpha=0.18, label=r"PASS band $[0.5,2.0]$")
    ax.axhspan(0.1, 0.5, color="gold", alpha=0.12)
    ax.axhspan(2.0, 10.0, color="gold", alpha=0.12, label=r"INFO band")
    ax.axhline(1.0, color="k", ls=":", lw=1)
    ax.axvline(kappa_star, color="red", ls="--", lw=1.3,
               label=fr"$\kappa^*={kappa_star:.1e}$ ($R{{=}}1$)")
    if kappa_nat > 0:
        ax.axvline(kappa_nat, color="purple", ls=":", lw=1.2,
                   label=fr"$\kappa_{{\rm nat}}={kappa_nat:.0e}$ (natural)")
    ax.set_xlabel(r"$\kappa$ = seconds per $M_{KK}^{-1}$ (OPEN knob)")
    ax.set_ylabel(r"$R_{\rm clock}(z{=}6)=t_{\rm proxy}/t_{\Lambda CDM}$")
    ax.set_title(r"(c) Assembly-clock ratio is normalization-conditional on $\kappa$")
    ax.legend(fontsize=7, loc="best"); ax.grid(True, which="both", alpha=0.25)

    # (d) age_dtau(origin->z) + R_clock at kappa* across LRD z
    ax = axes[1, 1]
    age_p = [results[primary][z]["age_dtau"] for z in lrd_z]   # (local) dimensionless age
    Rstar = [(kappa_star / 8.27) * results[primary][z]["age_dtau"] / t_lcdm[z] for z in lrd_z]  # (local)
    axb = ax.twinx()
    l1 = ax.plot(lrd_z, age_p, "ms-", lw=1.8, ms=7,
                 label=r"age $\int_{a=1}^{a(z)}d\ln a/H_{\rm proxy}$")
    l2 = axb.plot(lrd_z, Rstar, "c^--", lw=1.8, ms=7, label=r"$R_{\rm clock}(z)$ at $\kappa^*$")
    axb.axhspan(0.5, 2.0, color="green", alpha=0.12)
    ax.set_xlabel(r"redshift $z$ (LRD epoch)")
    ax.set_ylabel(r"proxy age $\Delta\tau$ (dimensionless)", color="m")
    axb.set_ylabel(r"$R_{\rm clock}(z)$ at $\kappa^*$", color="c")
    ax.set_title(r"(d) Clock orders: larger age at lower $z$ (cosmogenesis $a{=}1$)")
    lns = l1 + l2; ax.legend(lns, [ln.get_label() for ln in lns], fontsize=8, loc="best")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [plot saved: {OUT_PNG.name}]")


if __name__ == "__main__":
    sys.exit(main())
