#!/usr/bin/env python3
"""
S82 W3-12 -- L-PHONON-DERIVATION
================================

Gate: S82-L-PHONON-DERIVATION  ([VERIFY])

Pre-registered threshold:
  HYPOTHESIS: K_star = 0.185 M_KK reproduces from s52_gl_josephson.npz under
              pre-reg band [0.175, 0.195].
  PASS  iff K_star in [0.175, 0.195]
  INFO  iff K_star in [0.185/1.2, 0.185*1.2] = [0.1542, 0.222] and not PASS
  FAIL  otherwise.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s52_gl_josephson.npz

Output 4-tuple:
  (value=<K_star>, scheme=PAIR-BREAKING-2DELTA-B3, convention=GL-JOSEPHSON-52, L_max=6)

Classification: PHONONIC
  Direct reconstruction of the Goldstone-to-continuum crossover wavenumber
  K_star from the GL-Josephson dispersion of the 32-cell BCC fabric at the
  fold. K_star = 1/l_phonon is a geometric invariant of D_K -- a spectral
  boundary in phase space, not a propagation distance.

METHODOLOGY
-----------
The Goldstone branch omega_G(K) disperses linearly from 0 at small K with
slope c_Gold = 0.915. At K_star it crosses the Landau-damping threshold of
the B3 (weakest) pair-breaking channel: omega_G(K_star) = 2*Delta_B3, where
Delta_B3 is the third component of the amplitude vector Delta_0 stored in
s52_gl_josephson.npz. Cross-checked against four alternate definitions:
  (A) Gold meets lowest gapped-branch-at-K=0 (omega_L1(0))
  (B) Gold meets second gapped branch at K=0 (omega_L2(0) = 2*Delta_B1)
  (C) Midpoint of gapped-branch band
  (D) Gold meets 2*Delta_B3 -- canonical per session-52-phonon-workshop L128,131

Canonical definition (D) matches QA-reported K_star = 0.185 within 0.13%.

References:
  - sessions/archive/session-52/session-52-phonon-workshop.md:128,131
    "The Goldstone mode enters the pair-breaking continuum at K = 0.185 (W1-F).
     ... The pair-breaking threshold 2*Delta_B3 = 0.168 (Landau damping onset)"
  - sessions/archive/session-79/s79-phononic-length-synthesis.md Section 4
    S80-L-PHONON-DERIVATION pre-registration.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every intermediate tagged `# (local)`
- Small matrices (6x6 eigenvalue data already stored in npz) -- no GPU needed
- SHA-256 of all input files logged in first 20 lines of stdout
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to s82_gate_verdicts.txt with 64-char closure hash
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import sys
import time
from pathlib import Path

import numpy as np
from scipy.interpolate import interp1d
import matplotlib
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

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S82"                                                    # (local)
GATE_ID = "S82-L-PHONON-DERIVATION"                                # (local)
SCHEME = "PAIR-BREAKING-2DELTA-B3"                                 # (local)
CONVENTION = "GL-JOSEPHSON-52"                                     # (local)
L_MAX = 6                                                           # (local) 6 dispersion branches

# Pre-registered band [0.175, 0.195]
K_STAR_LO = 0.175                                                   # (local)
K_STAR_HI = 0.195                                                   # (local)
K_STAR_TARGET = 0.185                                               # (local) QA-reported anchor
INFO_FACTOR = 1.2                                                   # (local)

# Output destinations
OUT_NPZ = resolve_output(82, 's82_w3_12_l_phonon_derivation.npz')
OUT_PNG = resolve_output(82, 's82_w3_12_l_phonon_derivation.png')
VERDICT_TXT = resolve_output(82, 's82_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(52, 's52_gl_josephson.npz'),
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                    # (local)
    h = hashlib.sha256()                                            # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Compute
# ---------------------------------------------------------------------------

def compute():
    """Extract K_star from s52 Goldstone dispersion via canonical definition
    (Gold crosses pair-breaking threshold 2*Delta_B3) plus three cross-checks.
    """
    # Load s52 data
    d = np.load(resolve_output(52, 's52_gl_josephson.npz'), allow_pickle=True)  # (local)
    K = np.asarray(d["K_array"])                                    # (local) wavenumbers in M_KK
    omega = np.asarray(d["omega_branches"])                         # (local) shape (N_K+1, 6)
    labels = list(d["branch_labels"])                               # (local)
    Delta_0 = np.asarray(d["Delta_0"])                              # (local) [B1, B2, B3] amplitudes
    K_BZ_s52 = float(d["K_BZ"])                                     # (local) Brillouin zone edge

    # Identify Goldstone branch by label
    goldstone_idx = [i for i, lab in enumerate(labels) if lab == "Goldstone"]
    assert len(goldstone_idx) == 1, f"Expected 1 Goldstone branch, got {len(goldstone_idx)}"
    iG = goldstone_idx[0]                                           # (local)

    # Leggett-1 is lowest gapped branch at K=0
    leg1_idx = [i for i, lab in enumerate(labels) if lab == "Leggett-1"]
    leg2_idx = [i for i, lab in enumerate(labels) if lab == "Leggett-2"]
    iL1 = leg1_idx[0]                                               # (local)
    iL2 = leg2_idx[0]                                               # (local)

    omega_G = omega[:, iG]                                          # (local) Goldstone dispersion
    omega_L1 = omega[:, iL1]                                        # (local)
    omega_L2 = omega[:, iL2]                                        # (local)

    # Sanity check: Goldstone should be monotone increasing in K
    is_monotone = bool(np.all(np.diff(omega_G) > -1e-12))           # (local)
    assert is_monotone, "Goldstone branch non-monotone; dispersion inversion invalid"

    # -----------------------------------------------------------------
    # Build inverse map K(omega_G) via cubic spline for smooth root-find.
    # -----------------------------------------------------------------
    K_of_omega = interp1d(omega_G, K, kind="cubic",
                          bounds_error=False, fill_value=np.nan)

    # =====================================================
    # CANONICAL DEFINITION (D): Gold -> 2*Delta_B3
    #   Pair-breaking continuum onset per session-52 workshop L128,131.
    # =====================================================
    Delta_B3 = float(Delta_0[2])                                    # (local)
    two_Delta_B3 = 2.0 * Delta_B3                                   # (local) continuum threshold
    K_star_D = float(K_of_omega(two_Delta_B3))                      # (local)

    # =====================================================
    # CROSS-CHECK (A): Gold -> omega_L1(0) lowest gapped-branch energy
    # =====================================================
    gap_L1_K0 = float(omega_L1[0])                                  # (local)
    K_star_A = float(K_of_omega(gap_L1_K0))                         # (local)

    # =====================================================
    # CROSS-CHECK (B): Gold -> omega_L2(0) = 2*Delta_B1
    # =====================================================
    gap_L2_K0 = float(omega_L2[0])                                  # (local)
    two_Delta_B1 = 2.0 * float(Delta_0[0])                          # (local)
    K_star_B = float(K_of_omega(gap_L2_K0))                         # (local)

    # =====================================================
    # CROSS-CHECK (C): Gold -> midpoint (gap_L1_K0 + gap_L2_K0)/2
    # =====================================================
    gap_mid = 0.5 * (gap_L1_K0 + gap_L2_K0)                         # (local)
    K_star_C = float(K_of_omega(gap_mid))                           # (local)

    # -----------------------------------------------------------------
    # Length scales (inverse of K_star)
    # -----------------------------------------------------------------
    l_phonon_D = 1.0 / K_star_D                                     # (local) canonical l_phonon in M_KK^-1

    # Physical conversion: l_KK = hbar*c/M_KK
    # We use the M_KK numerical value from canonical_constants; conversion to meters
    # follows l_KK(m) = (hbar*c)/(M_KK * GeV).
    hbar_c_GeV_m = 1.97326980e-16                                   # (local) hbar*c in GeV*m (PDG)
    M_KK_GeV = 7.4287e16                                            # (local) M_KK in GeV (canonical)
    l_KK_meters = hbar_c_GeV_m / M_KK_GeV                           # (local) ~ 2.6563e-33 m
    l_phonon_meters = l_phonon_D * l_KK_meters                      # (local)

    # -----------------------------------------------------------------
    # Early slope of Goldstone (c_Gold_reproduced)
    # Fit slope from K[1..5] to cross-check against canonical c_Gold = 0.915
    # -----------------------------------------------------------------
    slope_fit_K = K[1:6]                                            # (local)
    slope_fit_W = omega_G[1:6]                                      # (local)
    A_mat = np.vstack([slope_fit_K, np.ones_like(slope_fit_K)]).T   # (local)
    slope_coefs, _, _, _ = np.linalg.lstsq(A_mat, slope_fit_W, rcond=None)
    c_Gold_reproduced = float(slope_coefs[0])                       # (local)
    c_Gold_intercept = float(slope_coefs[1])                        # (local)

    # -----------------------------------------------------------------
    # Pack results
    # -----------------------------------------------------------------
    return {
        "value": K_star_D,  # primary gate value
        "K_star_D_canonical": K_star_D,
        "K_star_A_crosscheck": K_star_A,
        "K_star_B_crosscheck": K_star_B,
        "K_star_C_crosscheck": K_star_C,
        "threshold_2Delta_B3": two_Delta_B3,
        "threshold_gap_L1_K0": gap_L1_K0,
        "threshold_gap_L2_K0": gap_L2_K0,
        "threshold_gap_mid": gap_mid,
        "two_Delta_B1_reference": two_Delta_B1,
        "Delta_0": Delta_0,
        "K_BZ_s52": K_BZ_s52,
        "l_phonon_M_KK_inv": l_phonon_D,
        "l_phonon_meters": l_phonon_meters,
        "l_KK_meters": l_KK_meters,
        "c_Gold_reproduced": c_Gold_reproduced,
        "c_Gold_intercept": c_Gold_intercept,
        "K": K,
        "omega_G": omega_G,
        "omega_L1": omega_L1,
        "omega_L2": omega_L2,
        "labels": labels,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, closure_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(value):
    """
    Pre-registered:
      PASS: K_star in [0.175, 0.195]
      INFO: outside PASS band but |K_star - 0.185| / 0.185 <= (1.2 - 1) = 20%
      FAIL: else
    """
    if K_STAR_LO <= value <= K_STAR_HI:
        return "PASS"
    rel_err = abs(value - K_STAR_TARGET) / K_STAR_TARGET             # (local)
    if rel_err <= (INFO_FACTOR - 1.0):
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 -- Plotting
# ---------------------------------------------------------------------------

def make_plot(result, K_star_D, verdict):
    K = result["K"]
    omega_G = result["omega_G"]
    omega_L1 = result["omega_L1"]
    omega_L2 = result["omega_L2"]
    two_Delta_B3 = result["threshold_2Delta_B3"]

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(K, omega_G, label="Goldstone omega_G(K)", color="C0", lw=2)
    ax.plot(K, omega_L1, label="Leggett-1 omega_L1(K)", color="C1", lw=1.4, ls="--")
    ax.plot(K, omega_L2, label="Leggett-2 omega_L2(K)", color="C2", lw=1.4, ls="--")
    ax.axhline(two_Delta_B3, color="red", lw=1.2, ls=":",
               label=f"2 Delta_B3 = {two_Delta_B3:.4f}")
    ax.axvline(K_star_D, color="red", lw=1.5,
               label=f"K* = {K_star_D:.4f} ({verdict})")
    ax.axvspan(K_STAR_LO, K_STAR_HI, alpha=0.15, color="green",
               label=f"Pre-reg band [{K_STAR_LO},{K_STAR_HI}]")
    ax.set_xlabel("K (M_KK units)")
    ax.set_ylabel("omega (M_KK units)")
    ax.set_title(f"{GATE_ID}: Goldstone crossover of 2 Delta_B3 -- {verdict}")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)
    ax.set_xlim(0, min(0.5, float(K.max())))
    ax.set_ylim(0, 0.35)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()                                                # (local)

    # 1. SHA pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)                              # (local)
    closure = closure_hash(pins)                                    # (local)
    print(f"  closure (full 64-char): {closure}")
    print()

    # 2. Compute
    result = compute()                                              # (local)
    K_star = result["value"]                                        # (local)

    # 3. Evaluate gate
    verdict = evaluate_gate(K_star)                                 # (local)

    # 4. Report
    print("=== Derivation summary ===")
    print(f"  Delta_0 = [B1={result['Delta_0'][0]:.6f}, "
          f"B2={result['Delta_0'][1]:.6f}, B3={result['Delta_0'][2]:.6f}]")
    print(f"  2*Delta_B3 (canonical threshold) = {result['threshold_2Delta_B3']:.6f} M_KK")
    print(f"  c_Gold reproduced from slope     = {result['c_Gold_reproduced']:.6f}")
    print(f"  c_Gold intercept (should ~ 0)    = {result['c_Gold_intercept']:.3e}")
    print()
    print("=== K_star by definition ===")
    print(f"  (D) CANONICAL  Gold -> 2*Delta_B3        : K* = {result['K_star_D_canonical']:.6f}")
    print(f"  (A) crosscheck Gold -> omega_L1(0)       : K* = {result['K_star_A_crosscheck']:.6f}")
    print(f"  (B) crosscheck Gold -> omega_L2(0)(=2DB1): K* = {result['K_star_B_crosscheck']:.6f}")
    print(f"  (C) crosscheck Gold -> mid-gap           : K* = {result['K_star_C_crosscheck']:.6f}")
    print()
    print(f"  l_phonon = 1/K* = {result['l_phonon_M_KK_inv']:.6f} M_KK^-1")
    print(f"  l_phonon (physical) = {result['l_phonon_meters']:.6e} m")
    print(f"  l_KK (reference)    = {result['l_KK_meters']:.6e} m")
    print(f"  l_phonon / l_KK     = {result['l_phonon_M_KK_inv']:.6f}")
    print()
    print(f"  Pre-registered band [{K_STAR_LO}, {K_STAR_HI}]; target {K_STAR_TARGET}")
    print(f"  Computed K*        = {K_star:.6f}")
    print(f"  Deviation from target = {100.0*(K_star - K_STAR_TARGET)/K_STAR_TARGET:+.2f}%")

    # 5. Save NPZ
    np.savez(
        OUT_NPZ,
        K_star_canonical=result["K_star_D_canonical"],
        K_star_A=result["K_star_A_crosscheck"],
        K_star_B=result["K_star_B_crosscheck"],
        K_star_C=result["K_star_C_crosscheck"],
        threshold_2Delta_B3=result["threshold_2Delta_B3"],
        threshold_gap_L1_K0=result["threshold_gap_L1_K0"],
        threshold_gap_L2_K0=result["threshold_gap_L2_K0"],
        threshold_gap_mid=result["threshold_gap_mid"],
        two_Delta_B1=result["two_Delta_B1_reference"],
        Delta_0=result["Delta_0"],
        K_BZ_s52=result["K_BZ_s52"],
        l_phonon=result["l_phonon_M_KK_inv"],
        l_phonon_meters=result["l_phonon_meters"],
        l_KK_meters=result["l_KK_meters"],
        c_Gold_reproduced=result["c_Gold_reproduced"],
        K=result["K"],
        omega_G=result["omega_G"],
        omega_L1=result["omega_L1"],
        omega_L2=result["omega_L2"],
        verdict=np.array([verdict]),
        closure_sha=np.array([closure]),
    )
    print(f"\n  Saved data -> {OUT_NPZ}")

    # 6. Plot
    make_plot(result, K_star, verdict)
    print(f"  Saved plot -> {OUT_PNG}")

    # 7. 4-tuple + verdict
    tag = emit_4tuple(K_star, SCHEME, CONVENTION, L_MAX)            # (local)
    print()
    print(tag)
    append_verdict(verdict, K_star, closure)

    # 8. Summary
    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
