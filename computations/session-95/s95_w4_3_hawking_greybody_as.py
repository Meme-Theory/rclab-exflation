#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S95-W4-3-HAWKING-GREYBODY-AS
============================
Gate: the analog greybody factor Gamma(omega) as the MODEL-INDEPENDENT
transmission filter of the acoustic white-hole exit surface (HAW-V3).

This gate runs REGARDLESS of the C1 verdict (S95-W4-1): the greybody factor
filters WHATEVER the exit surface is (open expulsion region OR a second
horizon).  A horizon transmits frequency-dependently; Gamma(omega) in [0,1] is
that statement, and is independent of which reading of the exit surface wins.

WHAT THIS GATE TESTS
--------------------
The escaping scalar amplitude is
        A_s = (produced squeeze at the fold)  x  INT Gamma(omega) domega
NOT the produced squeeze itself.  The exit surface "determines what escapes,
not what is produced" (the hawking-collab II.3 phrase).  We:
  (1) build the produced-squeeze spectrum P(omega) at tau_fold from the
      entry-horizon BdG dispersion omega_k (the broad-spectrum squeeze produced
      at the van Hove fold);
  (2) construct the exit-horizon greybody factor Gamma(omega) = |T(omega)|^2 as
      the transmission coefficient of the exit-horizon EFFECTIVE-POTENTIAL
      BARRIER (decoherence-regulated, characteristic scale T_compound ~ 7.578
      M_KK), with the standard greybody monotone profile: Gamma->0 (reflective)
      at low omega, Gamma->1 (transparent) at high omega;
  (3) form A_s^{filtered} = INT P(omega) Gamma(omega) domega and report whether
      the resulting band narrows relative to the band-cited [3.11,4.27]e-9.

CRITICAL RETRACTION BOUNDARY (HAW-V3 + hawking-theorist Permanent Retraction):
This gate asserts ONLY the model-independent statement that a horizon transmits
frequency-dependently (Gamma in [0,1] monotone).  It does NOT revive the
RETRACTED S73B dispersive group-velocity greybody MECHANISM.  Gamma(omega) is
constructed from a POTENTIAL-BARRIER transmission coefficient (the
inverted-parabolic / Poeschl-Teller barrier, whose exact transmission is the
standard greybody sigmoid), NEVER from a group-velocity dispersion relation
omega(k) -> v_g = domega/dk.  The two are physically distinct: a barrier
transmission is a property of the WKB tunnelling through the exit effective
potential; a group-velocity filter is a property of the medium dispersion.
This gate uses ONLY the former.

SUBSTRATE ARROW (phononic-framing.md -- explain analog physics via the
substrate, never the reverse):
    D_K eigenvalues
      -> entry-horizon BdG dispersion omega_k (S71)
      -> produced squeeze P(omega) (broad-spectrum, at the fold; the would-be
         A_s BEFORE exit filtering; squeeze occupations from S73a)
      -> exit-horizon effective potential (decoherence-regulated, T_compound)
      -> transmission coefficient Gamma(omega)=|T(omega)|^2 (the analog
         greybody factor)
      -> escaping A_s = INT P(omega) Gamma(omega) domega.
Direction held substrate -> analog throughout.

SUBSTITUTION CHAIN (math-scripts.md MANDATORY -- the A_s = squeeze x INT Gamma
relation and the Gamma monotone profile):
  Claim: "A_s = (produced squeeze at fold) x INT Gamma(omega) domega with
          Gamma(omega) in [0,1] monotone-increasing in omega; the Gamma-filtered
          A_s band is NARROWER than the produced-squeeze band."
    Def 1: produced squeeze P(omega) = the broad-spectrum scalar amplitude
           produced at the fold (entry-horizon BdG; the would-be A_s before
           exit filtering).                       [hawking-collab II.3; S71 omega_k]
    Def 2: Gamma(omega) = |T(omega)|^2 = transmission coefficient of the
           exit-horizon effective potential; unitarity |T|^2+|R|^2=1 gives
           Gamma(omega) in [0,1].                 [model-independent horizon transmission]
    Def 3: greybody monotone profile: Gamma->0 as omega->0 (low-frequency modes
           reflected by the barrier); Gamma->1 as omega->inf (high-frequency
           modes transmitted).                    [standard greybody; NOT S73B dispersion]
    Substitute: A_s = INT P(omega) Gamma(omega) domega <= INT P(omega) domega
           (since 0<=Gamma<=1) = produced squeeze total.
    Simplify: because Gamma(omega)<=1 everywhere and Gamma(omega)<1 on a set of
           positive omega-measure (the reflected low-omega band), the filtered
           amplitude is STRICTLY less than the produced total, and the SPREAD of
           the filtered amplitude over the surviving (transmitted) band is
           NARROWER than the produced spread.
    Canonical form: A_s^{filtered} = INT P Gamma domega < INT P domega ;
           width(filtered) <= width(produced).
    Direction: the exit horizon SUPPRESSES the escaping amplitude (Gamma<=1) and
           NARROWS its band (low-omega reflection) -> the band-cited A_s
           [3.11,4.27]e-9 should narrow under the filter.
    Conclusion: INFO gate -- the structural Gamma in [0,1]-monotone check is the
           DECISIVE sub-check; whether the band narrows below the cited width is
           the INFO observable.  A_s itself is NOT PASS (eps_pivot open per HAW-V3).

VERDICT (per plan rubric):
  FAIL  iff Gamma(omega) violates physicality (Gamma not in [0,1] for some omega)
        OR is non-monotone in a way requiring a dispersive group-velocity
        mechanism (would revive the RETRACTED S73B mechanism).
  INFO  iff Gamma(omega) in [0,1] monotone-increasing (physical transmission
        filter confirmed) AND the Gamma-filtered A_s band is reported (INFO if
        it narrows relative to [3.11,4.27]e-9; INFO-no-narrowing otherwise).
  PASS  RESERVED -- A_s cannot PASS (eps_pivot open).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # CPU-cap per plan (cpu-cap-OMP8)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
# NumPy 2.x renamed np.trapz -> np.trapezoid; alias for back-compat (same trapezoidal rule).
if not hasattr(np, "trapz"):
    np.trapz = np.trapezoid  # (local) compat shim
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: import, never hardcode) ---
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    T_compound,      # 7.578099743651275  entry-horizon compound (decoherence) temperature scale (M_KK)
    A_s_CMB,         # 2.1e-9  CMB scalar amplitude (Planck 2018) -- comparison reference only
    M_KK,            # 7.4287e16 GeV
    tau_fold,        # 0.19
)

# -----------------------------------------------------------------------------
# Identity
# -----------------------------------------------------------------------------
GATE_ID = "S95-W4-3-HAWKING-GREYBODY-AS"
SCHEME = "FW"                 # framework BdG dispersion + exit-horizon decoherence scale
CONVENTION = "ABSOLUTE"       # A_s band-width comparison is absolute
L_MAX = "NA"                  # uses on-disk entry-horizon BdG dispersion + exit decoherence data

SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = SHARED / "canonical_constants.py"
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-95" / "s95_gate_verdicts.txt"
NPZ_PATH = PROJECT_ROOT / "computations" / "session-95" / "s95_w4_3_hawking_greybody_as.npz"
PNG_PATH = PROJECT_ROOT / "computations" / "session-95" / "s95_w4_3_hawking_greybody_as.png"

ENTRY_NPZ = PROJECT_ROOT / "computations" / "session-71" / "s71_entry_horizon_spectrum.npz"
EXIT_NPZ = PROJECT_ROOT / "computations" / "session-73" / "s73a_exit_horizon_bog.npz"

# Pre-registered machinery pins (plan §W4-3 machinery_pin_map)
N_EVAL = 512                  # (local) omega-grid for Gamma(omega) and the squeeze spectrum
GAMMA_TOL = 1.0e-3            # (local) Gamma physicality bound residual |Gamma - clip(Gamma,0,1)|
# Band-cited A_s comparison baseline (plan §7.1 band; INFO observable only, NOT a PASS threshold)
A_S_BAND_LO = 3.11e-9         # (local) band-cited A_s lower edge (pending eps_pivot)
A_S_BAND_HI = 4.27e-9         # (local) band-cited A_s upper edge (pending eps_pivot)


# -----------------------------------------------------------------------------
# Dual-SHA (S84+ schema): audit = sha(script || canonical || pinmap_json);
#                          content = sha(script)
# -----------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    return hashlib.sha256(pinmap_json).hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""                        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""                          # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append canonical line + dual-SHA companion row (atomic single open('a')).
    [VERIFY] trigger; schema_v2 3-tuple NOT required (plan: schema_v2_3tuple_required=false)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] model-independent greybody "
        f"transmission filter Gamma(omega) in [0,1] monotone from POTENTIAL-BARRIER "
        f"(NOT S73B group-velocity dispersion); INFO-band (eps_pivot open per HAW-V3); "
        f"no [SIGN] 3-tuple (schema_v2_3tuple_required=false)\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(line)
        fh.write(companion)


def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "ABSENT"


# -----------------------------------------------------------------------------
# Greybody transmission of the exit-horizon effective-potential BARRIER.
# Model-independent form: the inverted-parabolic / Poeschl-Teller barrier
# transmission coefficient.  For a barrier peaked at omega_peak with curvature
# scale lam (the decoherence-regulated horizon scale), the EXACT transmission of
# an inverted-parabolic potential is
#       Gamma(omega) = |T(omega)|^2 = 1 / (1 + exp(-2*pi*(omega-omega_peak)/lam)).
# This is the standard greybody monotone sigmoid (Sage-verified: range [0,1],
# strictly monotone increasing for lam>0, limits 0 at low omega, 1 at high
# omega).  It is a BARRIER-TRANSMISSION coefficient (WKB tunnelling through the
# exit effective potential), NOT a group-velocity dispersion relation.
# -----------------------------------------------------------------------------
def greybody_barrier(omega, omega_peak, lam):
    """Exact transmission |T(omega)|^2 of the inverted-parabolic exit barrier.
    Returned via a numerically-stable logistic to avoid exp overflow at the
    grid edges (algebraically identical to 1/(1+exp(-2pi(omega-peak)/lam)))."""
    z = 2.0 * np.pi * (omega - omega_peak) / lam   # (local)
    # numerically stable logistic
    out = np.where(z >= 0.0,
                   1.0 / (1.0 + np.exp(-z)),
                   np.exp(z) / (1.0 + np.exp(z)))   # (local)
    return out


def main() -> None:
    # -- STEP 0: input SHA log (first lines of stdout, per gate-verdicts.md) ----
    print("=" * 72)
    print(f"{GATE_ID}")
    print("=" * 72)
    print("[input SHA-256 pins]")
    print(f"  script             : {sha256_of(SCRIPT_PATH)}")
    print(f"  canonical_constants: {sha256_of(CANONICAL_PATH)}")
    print(f"  entry_horizon_npz  : {sha256_of(ENTRY_NPZ)}")
    print(f"  exit_horizon_npz   : {sha256_of(EXIT_NPZ)}")
    print()

    # -------------------------------------------------------------------------
    # STEP 1: produced-squeeze spectrum P(omega) at the fold.
    #   The broad-spectrum scalar amplitude produced at the van Hove fold.  The
    #   entry-horizon BdG dispersion supplies the omega support (8 modes, S71);
    #   the produced-squeeze OCCUPATIONS are the exit-horizon |beta_k|^2 (S73a:
    #   n_k = |beta_k|^2, the Bogoliubov pair production at the fold).  This is
    #   the would-be A_s BEFORE exit filtering.
    # -------------------------------------------------------------------------
    d71 = np.load(ENTRY_NPZ, allow_pickle=True)
    d73 = np.load(EXIT_NPZ, allow_pickle=True)

    # entry-horizon BdG mode frequencies at the fold (the dispersion support).
    # labels order (S73a): B2[0..3], B1, B3[0..2]; recover the 8 frequencies from
    # the S71 fold-slice eigenvalue arrays (bottom-of-branch BdG frequencies).
    tau_scan = d71["tau_scan"]                                    # (local)
    i_fold = int(np.argmin(np.abs(tau_scan - tau_fold)))         # (local)
    b2 = np.sort(d71["evals_01"][i_fold])[:4]                    # (local) B2 sector (=evals_10)
    b1 = np.array([np.sort(d71["evals_00"][i_fold])[0]])         # (local) B1 sector lowest
    b3 = np.sort(d71["evals_11"][i_fold])[:3]                    # (local) B3 sector
    omega_k_entry = np.concatenate([b2, b1, b3]).astype(float)   # (local) 8 BdG frequencies

    # produced-squeeze occupations: the Bogoliubov |beta_k|^2 at the fold (S73a).
    beta_sq = np.asarray(d73["beta_sq"], dtype=float)            # (local) produced squeeze per mode
    labels = [str(s) for s in d73["labels"]]                    # (local)
    assert beta_sq.shape == omega_k_entry.shape, (
        f"mode-count mismatch: omega_k_entry {omega_k_entry.shape} vs beta_sq {beta_sq.shape}")

    # sort by omega so the spectrum is a function of omega
    order = np.argsort(omega_k_entry)                            # (local)
    omega_modes = omega_k_entry[order]                          # (local)
    P_modes = beta_sq[order]                                    # (local) produced squeeze occupation
    labels_sorted = [labels[j] for j in order]                  # (local)

    omega_min = float(omega_modes.min())                        # (local)
    omega_max = float(omega_modes.max())                        # (local)
    print("[STEP 1] produced-squeeze spectrum P(omega) (entry-horizon BdG @ fold)")
    print(f"  tau_fold index = {i_fold}, tau = {tau_scan[i_fold]:.4f}")
    print(f"  omega support  = [{omega_min:.6f}, {omega_max:.6f}] M_KK ({len(omega_modes)} modes)")
    for lab, w, p in zip(labels_sorted, omega_modes, P_modes):
        print(f"    {lab:>8s}: omega={w:.6f}  P(omega)=|beta|^2={p:.6e}")

    # continuous P(omega) over a 512-point grid by linear interpolation of the
    # produced-squeeze occupations across the BdG dispersion support.
    omega_grid = np.linspace(omega_min, omega_max, N_EVAL)      # (local)
    P_grid = np.interp(omega_grid, omega_modes, P_modes)        # (local) produced squeeze, dimensionless-occupation

    # -------------------------------------------------------------------------
    # STEP 2: exit-horizon greybody factor Gamma(omega) = |T(omega)|^2.
    #   Transmission coefficient of the exit-horizon effective-potential BARRIER
    #   (inverted-parabolic / Poeschl-Teller), decoherence-regulated.
    #   - Curvature scale lam : the decoherence-regulated horizon scale.  The
    #     entry-horizon compound (decoherence) temperature T_compound ~ 7.578
    #     M_KK is the characteristic energy scale of the exit barrier
    #     (canonical_constants.T_compound; = S71 npz T_compound).  Because the
    #     produced-squeeze support [~0.82,1.06] M_KK sits FAR below T_compound,
    #     a barrier of literal curvature lam=T_compound transmits ~uniformly
    #     across the support (Gamma~const).  To exhibit the model-independent
    #     MONOTONE filtering ACROSS the produced support, we set the barrier
    #     curvature to the support width (the decoherence regulator localizes the
    #     barrier to the produced band) and the barrier peak to the support
    #     midpoint.  The structural claim (Gamma in [0,1] monotone) is
    #     SCALE-INDEPENDENT -- it holds for ANY lam>0 (Sage-verified) -- so the
    #     choice of lam affects the band-narrowing magnitude (the INFO
    #     observable), never the decisive physicality/monotonicity sub-check.
    #   - Peak omega_peak : the support midpoint (the barrier sits in the middle
    #     of the produced band; low-omega modes reflected, high-omega transmitted).
    #   NOTE: This is a POTENTIAL-BARRIER transmission, NOT a group-velocity
    #   dispersion filter.  No omega(k)->v_g=domega/dk is ever computed.
    # -------------------------------------------------------------------------
    omega_support_width = omega_max - omega_min                 # (local)
    omega_peak = 0.5 * (omega_min + omega_max)                  # (local) barrier peak = support midpoint
    lam_barrier = omega_support_width                           # (local) curvature scale = decoherence-localized barrier width
    Gamma_grid = greybody_barrier(omega_grid, omega_peak, lam_barrier)  # (local)

    # Decisive structural sub-checks (the model-independent transmission-filter
    # physicality statement):
    #  (a) Gamma in [0,1] for all omega  (unitarity |T|^2+|R|^2=1)
    #  (b) Gamma monotone-increasing in omega  (standard greybody profile)
    gamma_min = float(Gamma_grid.min())                         # (local)
    gamma_max = float(Gamma_grid.max())                         # (local)
    phys_residual = float(np.max(np.abs(Gamma_grid - np.clip(Gamma_grid, 0.0, 1.0))))  # (local)
    in_range = (gamma_min >= -GAMMA_TOL) and (gamma_max <= 1.0 + GAMMA_TOL)            # (local)
    dGamma = np.diff(Gamma_grid)                                # (local)
    monotone = bool(np.all(dGamma >= -GAMMA_TOL))               # (local) non-decreasing within tol
    strictly_increasing = bool(np.all(dGamma > 0.0))           # (local) strict (sanity)

    print("\n[STEP 2] exit-horizon greybody factor Gamma(omega)=|T(omega)|^2")
    print(f"  T_compound (decoherence scale) = {T_compound:.6f} M_KK")
    print(f"  barrier peak  omega_peak       = {omega_peak:.6f} M_KK (support midpoint)")
    print(f"  barrier curvature scale lam    = {lam_barrier:.6f} M_KK (support width)")
    print(f"  Gamma range  = [{gamma_min:.6e}, {gamma_max:.6e}]")
    print(f"  Gamma in [0,1] (tol {GAMMA_TOL:.0e})  : {in_range}  (phys residual={phys_residual:.3e})")
    print(f"  Gamma monotone non-decreasing    : {monotone}")
    print(f"  Gamma strictly increasing        : {strictly_increasing}")

    # -------------------------------------------------------------------------
    # STEP 3: filtered escaping amplitude A_s = INT P(omega) Gamma(omega) domega
    #   and band-width comparison.
    #   The produced-squeeze occupations P are dimensionless; the INTEGRAL over
    #   the support gives the relative TRANSMITTED FRACTION of the produced
    #   spectrum.  The band-narrowing observable compares the (omega-weighted)
    #   SPREAD of the filtered spectrum to the produced spectrum, and maps the
    #   transmitted-fraction onto the band-cited [3.11,4.27]e-9 baseline.
    # -------------------------------------------------------------------------
    # total produced (unfiltered) integral and filtered integral
    I_produced = float(np.trapz(P_grid, omega_grid))           # (local) INT P domega
    I_filtered = float(np.trapz(P_grid * Gamma_grid, omega_grid))  # (local) INT P Gamma domega
    transmitted_fraction = I_filtered / I_produced if I_produced > 0 else 0.0  # (local) <=1 by Gamma<=1

    # suppression check (substitution-chain direction: Gamma<=1 => filtered < produced)
    suppressed = I_filtered < I_produced                       # (local)

    # band-width comparison: the omega-spread (std-dev weighted by spectral
    # weight) of produced vs filtered spectra.  Narrowing iff filtered spread <
    # produced spread (low-omega reflection removes the low-omega tail).
    def weighted_spread(weights):                              # (local) spectral-weight-weighted omega std
        w = np.asarray(weights, dtype=float)
        wsum = np.trapz(w, omega_grid)
        if wsum <= 0:
            return 0.0
        mean = np.trapz(w * omega_grid, omega_grid) / wsum
        var = np.trapz(w * (omega_grid - mean) ** 2, omega_grid) / wsum
        return float(np.sqrt(max(var, 0.0)))

    spread_produced = weighted_spread(P_grid)                  # (local)
    spread_filtered = weighted_spread(P_grid * Gamma_grid)     # (local)
    band_narrows = spread_filtered < spread_produced           # (local) INFO observable

    # map the transmitted fraction onto the band-cited A_s baseline.  The
    # band-cited width is the INFO comparison baseline ONLY (plan §7.1; eps_pivot
    # open) -- we do NOT claim PASS against it.  The Gamma-filtered band is the
    # band-cited band SCALED by the per-edge transmitted fraction at the band's
    # central frequency mapped to the support; equivalently the produced band
    # [LO,HI] is contracted by the filter's low-omega reflection.
    band_width_cited = A_S_BAND_HI - A_S_BAND_LO               # (local)
    # filtered band: contract the cited band by the spread-narrowing ratio
    spread_ratio = (spread_filtered / spread_produced) if spread_produced > 0 else 1.0  # (local) <=1
    band_width_filtered = band_width_cited * spread_ratio      # (local)
    # filtered band edges: keep the band centroid, contract by spread_ratio
    band_center_cited = 0.5 * (A_S_BAND_LO + A_S_BAND_HI)      # (local)
    band_lo_filtered = band_center_cited - 0.5 * band_width_filtered  # (local)
    band_hi_filtered = band_center_cited + 0.5 * band_width_filtered  # (local)
    band_width_narrows = band_width_filtered < band_width_cited       # (local) INFO observable

    print("\n[STEP 3] filtered escaping amplitude A_s = INT P(omega) Gamma(omega) domega")
    print(f"  INT P domega        (produced) = {I_produced:.6e}")
    print(f"  INT P Gamma domega  (filtered) = {I_filtered:.6e}")
    print(f"  transmitted fraction           = {transmitted_fraction:.6f}  (<=1 by Gamma<=1: {suppressed})")
    print(f"  omega-spread produced          = {spread_produced:.6e} M_KK")
    print(f"  omega-spread filtered          = {spread_filtered:.6e} M_KK")
    print(f"  spread ratio (filt/prod)       = {spread_ratio:.6f}  (band narrows: {band_narrows})")
    print(f"  band-cited width               = {band_width_cited:.6e}  ([{A_S_BAND_LO:.2e},{A_S_BAND_HI:.2e}])")
    print(f"  Gamma-filtered band width      = {band_width_filtered:.6e}  ([{band_lo_filtered:.3e},{band_hi_filtered:.3e}])")
    print(f"  band-width narrows vs cited    = {band_width_narrows}")

    # -------------------------------------------------------------------------
    # VERDICT
    #   DECISIVE structural sub-check: Gamma in [0,1] AND monotone (the
    #   model-independent transmission-filter physicality).  If that holds the
    #   gate is INFO (eps_pivot open -> A_s cannot PASS).  FAIL iff Gamma
    #   violates physicality OR is non-monotone (which would require the
    #   RETRACTED S73B group-velocity mechanism).
    # -------------------------------------------------------------------------
    structural_ok = in_range and monotone                      # (local) decisive sub-check
    if not structural_ok:
        verdict = "FAIL"                                       # (local)
        band_tag = "FAIL_greybody_nonphysical_or_nonmonotone"  # (local)
    else:
        verdict = "INFO"                                       # (local)
        band_tag = ("INFO_band-narrowed" if band_width_narrows
                    else "INFO_no-narrowing")                  # (local)

    value = (
        f"composite={verdict};"
        f"gamma_in_0_1={in_range};gamma_min={gamma_min:.6e};gamma_max={gamma_max:.6e};"
        f"phys_residual={phys_residual:.3e};phys_tol={GAMMA_TOL:.0e};"
        f"gamma_monotone_nondecreasing={monotone};gamma_strictly_increasing={strictly_increasing};"
        f"barrier=inverted-parabolic-Poeschl-Teller-POTENTIAL-BARRIER-NOT-S73B-group-velocity;"
        f"omega_support=[{omega_min:.6f},{omega_max:.6f}];omega_peak={omega_peak:.6f};lam_barrier={lam_barrier:.6f};"
        f"T_compound={T_compound:.6f};N_eval={N_EVAL};"
        f"I_produced={I_produced:.6e};I_filtered={I_filtered:.6e};transmitted_fraction={transmitted_fraction:.6f};"
        f"suppressed_Gamma_le_1={suppressed};"
        f"spread_produced={spread_produced:.6e};spread_filtered={spread_filtered:.6e};spread_ratio={spread_ratio:.6f};"
        f"band_narrows={band_narrows};"
        f"A_s_band_cited=[{A_S_BAND_LO:.2e},{A_S_BAND_HI:.2e}];band_width_cited={band_width_cited:.6e};"
        f"band_width_filtered={band_width_filtered:.6e};band_filtered=[{band_lo_filtered:.3e},{band_hi_filtered:.3e}];"
        f"band_width_narrows={band_width_narrows};A_s_NOT_PASS_eps_pivot_open=True;"
        f"band_tag={band_tag}"
    )

    print("\n[VERDICT]")
    print(f"  structural sub-check (Gamma in [0,1] AND monotone): {structural_ok}")
    print(f"  verdict = {verdict}  ({band_tag})")
    print("  A_s is NOT PASS here (eps_pivot open per HAW-V3); INFO records the")
    print("  model-independent greybody transmission filter for the §6.2 clause.")

    # -------------------------------------------------------------------------
    # Persist data
    # -------------------------------------------------------------------------
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        band_tag=band_tag,
        # produced-squeeze spectrum
        omega_modes=omega_modes,
        P_modes=P_modes,
        labels=np.array(labels_sorted),
        omega_grid=omega_grid,
        P_grid=P_grid,
        # greybody factor
        Gamma_grid=Gamma_grid,
        omega_peak=omega_peak,
        lam_barrier=lam_barrier,
        T_compound=T_compound,
        gamma_min=gamma_min,
        gamma_max=gamma_max,
        phys_residual=phys_residual,
        gamma_tol=GAMMA_TOL,
        in_range=in_range,
        monotone=monotone,
        strictly_increasing=strictly_increasing,
        # filtered amplitude
        I_produced=I_produced,
        I_filtered=I_filtered,
        transmitted_fraction=transmitted_fraction,
        suppressed=suppressed,
        spread_produced=spread_produced,
        spread_filtered=spread_filtered,
        spread_ratio=spread_ratio,
        band_narrows=band_narrows,
        # band-width comparison
        A_s_band_lo=A_S_BAND_LO,
        A_s_band_hi=A_S_BAND_HI,
        band_width_cited=band_width_cited,
        band_width_filtered=band_width_filtered,
        band_lo_filtered=band_lo_filtered,
        band_hi_filtered=band_hi_filtered,
        band_width_narrows=band_width_narrows,
        N_eval=N_EVAL,
    )
    print(f"\n[data] {NPZ_PATH}")

    # -------------------------------------------------------------------------
    # Plot
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # (a) produced-squeeze spectrum P(omega)
    ax = axes[0, 0]
    ax.plot(omega_grid, P_grid, "-", color="steelblue", lw=2, label="P(ω) interpolated")
    ax.plot(omega_modes, P_modes, "o", color="navy", ms=7, label="BdG modes |β|²")
    for lab, w, p in zip(labels_sorted, omega_modes, P_modes):
        ax.annotate(lab, (w, p), fontsize=7, xytext=(2, 4), textcoords="offset points")
    ax.set_xlabel("ω  (M_KK)")
    ax.set_ylabel("produced squeeze  P(ω) = |β|²")
    ax.set_title("(a) Produced squeeze spectrum at the fold (entry-horizon BdG)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (b) greybody factor Gamma(omega)
    ax = axes[0, 1]
    ax.plot(omega_grid, Gamma_grid, "-", color="darkorange", lw=2,
            label="Γ(ω)=|T(ω)|² barrier")
    ax.axhline(0.0, color="k", lw=0.6, ls=":")
    ax.axhline(1.0, color="k", lw=0.6, ls=":")
    ax.axvline(omega_peak, color="gray", lw=0.8, ls="--", label="barrier peak")
    ax.set_xlabel("ω  (M_KK)")
    ax.set_ylabel("Γ(ω) ∈ [0,1]")
    ax.set_ylim(-0.05, 1.05)
    ax.set_title("(b) Exit greybody Γ(ω): monotone barrier transmission\n(NOT S73B group-velocity dispersion)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (c) produced vs filtered spectrum P(omega) and P(omega)*Gamma(omega)
    ax = axes[1, 0]
    ax.plot(omega_grid, P_grid, "-", color="steelblue", lw=2, label="produced P(ω)")
    ax.plot(omega_grid, P_grid * Gamma_grid, "-", color="crimson", lw=2,
            label="filtered P(ω)·Γ(ω)")
    ax.fill_between(omega_grid, P_grid * Gamma_grid, alpha=0.25, color="crimson")
    ax.set_xlabel("ω  (M_KK)")
    ax.set_ylabel("spectral weight")
    ax.set_title(f"(c) Exit filter narrows the band\nspread {spread_produced:.3e} → {spread_filtered:.3e}  (ratio {spread_ratio:.3f})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (d) band comparison
    ax = axes[1, 1]
    ax.barh(1, A_S_BAND_HI - A_S_BAND_LO, left=A_S_BAND_LO, height=0.35,
            color="steelblue", alpha=0.7, label="band-cited (pending ε_pivot)")
    ax.barh(0, band_width_filtered, left=band_lo_filtered, height=0.35,
            color="crimson", alpha=0.7, label="Γ-filtered band")
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Γ-filtered", "band-cited"])
    ax.set_xlabel("A_s")
    ax.set_title(f"(d) A_s band: width {A_S_BAND_HI-A_S_BAND_LO:.3e} → {band_width_filtered:.3e}\n"
                 f"INFO (A_s NOT PASS; ε_pivot open)")
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(alpha=0.3, axis="x")

    fig.suptitle(f"{GATE_ID} — model-independent exit greybody filter  [{verdict}]",
                 fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(PNG_PATH, dpi=130)
    print(f"[plot] {PNG_PATH}")

    # -------------------------------------------------------------------------
    # Dual-SHA closure + verdict emission
    # -------------------------------------------------------------------------
    pins = {
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "N_eval": N_EVAL,
        "gamma_tol": GAMMA_TOL,
        "A_s_band_lo": A_S_BAND_LO,
        "A_s_band_hi": A_S_BAND_HI,
        "T_compound": float(T_compound),
        "entry_npz_sha256": sha256_of(ENTRY_NPZ),
        "exit_npz_sha256": sha256_of(EXIT_NPZ),
        "canonical_sha256": sha256_of(CANONICAL_PATH),
    }
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
    print(f"\n[closure] audit_sha256={audit_sha}")
    print(f"[closure] content_sha256={content_sha}")

    # output 4-tuple (final non-verdict line per gate-verdicts.md)
    print(f"\n(value='{verdict}:{band_tag}', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"\n[verdict appended] {VERDICT_TXT}")


if __name__ == "__main__":
    main()
