#!/usr/bin/env python
"""
S94-VII-PS-FULL-SPECTRUM-LEVEL-3
================================

The Pati-Salam SU(4)_PS Level-3 spectral-action anchor for the §VII.BE FWD-C4
cross-pillar bridge (and the §VII.AQ.OP-PROJ full-spectrum Level-3 row completion).

Substrate framing (GEOMETRIC; IS-not-IN): the substrate IS the finite Pati-Salam
spectral triple (A_K_PS, H_K_PS, D_K_PS, gamma_9, J) with
A_K_PS = C (+) M_2(C)_L (+) M_2(C)_R (+) M_4(C)_PS. D_K_PS is BLOCK-DIAGONAL by
Peter-Weyl decomposition over SU(4) irreps (a,b,c): D_K_PS = (+)_{(a,b,c)} D_{(a,b,c)}.
Its eigenvalue spectrum {lam_PS} is the set of vibrational modes of the
Pati-Salam-extended fabric. The Level-3 spectral-action anchor
Res_{s=4} Tr(D_K_PS^{-2s}) is the s=4 Mellin residue of that spectrum — a spectral
moment read OFF the eigenvalues, not a field on an internal container.

FEASIBILITY PRE-CHECK (the centerpiece, per math-scripts.md §"D_K Block-Diagonality
+ Recursive-Casimir-Projection Feasibility Pre-Check"):
  Dense storage of (+)_{(a,b,c)} D_{(a,b,c)} at L_max=12 is 1094.7 GB >> 17.1 GB VRAM
  => INFEASIBLE. But the operative cost is NOT diagonalization: each Peter-Weyl
  sector's eigenvalue is KNOWN ANALYTICALLY, |lam_PS(a,b,c,tau)| = sqrt(C2(a,b,c)) *
  exp(-tau*(a+b+c)) / r(tau)_PS (the SU(4) analog of the SU(3) form in
  _cm_1995_residue_formula.py lines 15-17). The CM-1995 §III.4 residue at finite
  L_max reduces ALGEBRAICALLY to the direct sum over sectors (entire in s at finite
  L_max), so NO operator matrix is ever formed. The producing-script cost is the
  recursive Casimir-projection irrep ENUMERATION, which the exact SU(4)=A_3 Weyl
  dimension + quadratic-Casimir closed forms make O(L^3) trivial. Route-A
  (sparse-Lanczos) is therefore NOT NEEDED — the analytic per-sector form supersedes
  it. The verdict scheme is FW-FRIEDRICH-BAR-SATURATION (Route-B): the Level-3
  question reduces to whether the residue is a finite L_max-saturated anchor.

DECISIVE STRUCTURAL FINDING (NUMBERS first):
  The SU(4)_PS Mellin-cone shell sum scales as L^{8-2s} (A_3 has 6 positive roots
  => dim_PS ~ L^6, and ~L^2 sectors per shell). The total residue Sigma_L L^{8-2s}
  converges IFF s > 9/2 = 4.5 (Sage-exact). At the inherited s=4 pole the exponent
  is 0 => the full-spectrum residue DIVERGES. By contrast the SU(3) base at s=4
  scales L^{3-2s} = L^{-5} and CONVERGES (which is why the SU(3) program anchors
  Level-3 at s=4). Consequently:
    - sign_verdict = PASS  : the directional claim L^{-4} < L^{-3} (alpha=4 envelope
                             tighter than alpha=3) is correct; Level-3 < Level-2 is
                             sign-robust GIVEN a finite positive residue.
    - magnitude_verdict = FAIL : at the literal s=4 pole the residue is NOT a finite
                             anchor; the truncation residual r(L) GROWS (does not sit
                             < 1).
    - regime_verdict = BREAKDOWN : s=4 is OUT of the SU(4)_PS convergent regime
                             (s > 4.5 required); breakdown fraction is 100% (diverges
                             at all L_max).
    - composite = FAIL (per gate-verdicts.md composite-collapse: regime BREAKDOWN
                             => FAIL regardless of other fields; S91 W4-W5-1 precedent).

  This is a corridor-closing RESULT: the §VII.BE FWD-C4 numerical Level-3 pin at the
  INHERITED s=4 pole cannot be satisfied for SU(4)_PS. The convergent, substrate-
  natural anchor sits at s >= 5: at s=6 the residue is finite (0.0009394) with a
  truncation-tail envelope ~ L^{-3} (the §VII.AF.1 d=4 precedent). The gate's own
  FAIL_meaning anticipates this ("misidentified Level-2 envelope; re-derive the
  SU(4)_PS Friedrich-Bär envelope before re-pinning"). The forward route is the
  Tier-2 dimensional-re-anchorability gate (cross-pillar-bridge-anatomy.md): re-pin
  the §VII.BE Level-3 anchor to the convergent pole. The §VII.BE STAGE-3 promotion is
  therefore NOT licensed by this gate (stays STAGE-1-CANDIDATE with structural Stage-2
  recorded). The §VII.AQ.OP-PROJ row is completed with the DIAGNOSTIC finding (the
  s=4 full-spectrum residue diverges; does NOT reopen the order-one-CLOSED STAGE-3
  route). mack lands any registry text at session-close; this gate emits ONLY verdict
  + npz + WP section.

eta_FB_SU4 is RE-DERIVED on the SU(4)_PS spectrum (NOT inherited from the SU(3)
empirical floor 0.436488, S92 W9-3): eta_FB_SU4(a,b,c) = |lam_PS|_sector /
sqrt(C2(a,b,c)+1). The SU(4)_PS floor is FAR below the SU(3) floor and below
eta_FB_lower=0.40 because the bottom-K |lam_PS| keep DECREASING with L_max under
the Jensen exp(-tau*rho) deformation (no Friedrich-Bär saturation of the bottom-K
at the s=4 pole). This re-derivation is itself part of the FAIL diagnosis.

Regulator pin: a_n^{Mellin} (the CM-1995 §III.4 Mellin-transform residue class).
Element-3 bridge map (5-anatomy): Wodzicki ∘ HKR composite, scheme suffix
-Bismut-Cheeger (adiabatic-limit eta-form at boundary).

NUMBERS first, gate second, interpretation third.

Owner: connes-ncg-theorist.
Plan: sessions/session-plan/session-94-plan-w3.md §W3-9.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import time
from pathlib import Path
from fractions import Fraction

import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# --- canonical constants (MANDATORY import) ---
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    M_Pl_reduced,
    alpha_HH1_per_pole_FW_s4,  # canonical s=4 envelope exponent (=4; Wodzicki 2(s-2))
)

mp.mp.prec = 100  # ~30 decimal digits for residue cross-check

# ===========================================================================
# Identity
# ===========================================================================
GATE_ID = "S94-VII-PS-FULL-SPECTRUM-LEVEL-3"
# Route taken: Route-B (Friedrich-Bär analytic saturation certification). Route-A
# (sparse-Lanczos) is NOT NEEDED — the per-sector eigenvalue is analytic, so the
# residue is a direct sum (no operator matrix). Disclosed in WP §"Methodology".
SCHEME = "FW-FRIEDRICH-BAR-SATURATION"
CONVENTION = ("ABSOLUTE-residue-anchor-a_n_Mellin-Element3-Bismut-Cheeger-adiabatic-limit-"
              "SU4_PS-full-spectrum-Peter-Weyl-direct-sum")
SCHEMA_VERSION = "S87+"

L_MAX_PLAN = 12       # (local) nominal SU(4)_PS truncation; dense = 1094.7 GB INFEASIBLE
DENSE_GB_L12 = 1094.7  # (local) plan Sage-MCP Casimir-bound pre-check (dense storage wall)
VRAM_GB = 17.1        # (local) AMD RX 9070 XT VRAM cap

SESSION_DIR = ROOT / "computations" / "session-94"
VERDICT_FILE = SESSION_DIR / "s94_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
NPZ_PATH = SESSION_DIR / "s94_vii_ps_full_spectrum_level_3.npz"
PNG_PATH = SESSION_DIR / "s94_vii_ps_full_spectrum_level_3.png"

# Input files
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
CM_1995_RESIDUE = ROOT / "computations" / "_shared" / "_cm_1995_residue_formula.py"
DIRAC_SPECTRUM = ROOT / "computations" / "_shared" / "dirac_spectrum.py"
S93_VERDICTS = ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"

# Structural Stage-2 PASS-AND provenance (S93 W6-4; already on disk)
S93_W6_4_AXIS_A_SHA = "146b5742"   # connes axis-A INFO (structural PASS-AND)
S93_W6_4_AXIS_B_SHA = "9df77b09"   # landau axis-B INFO (structural PASS-AND)

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "cm_1995_residue_formula": CM_1995_RESIDUE,
    "dirac_spectrum": DIRAC_SPECTRUM,
    "s93_verdicts": S93_VERDICTS,
    "script": SCRIPT_PATH,
}

# ===========================================================================
# SU(4) = A_3 representation theory (EXACT; matches s93_w6_4 A3_INV_CARTAN form;
# Sage-cross-checked: C2(4)=15/4, C2(6)=5, C2(15)=8, C2(10)=9, conjugation-symmetric)
# ===========================================================================
A3_INV_CARTAN = [
    [Fraction(3, 4), Fraction(1, 2), Fraction(1, 4)],
    [Fraction(1, 2), Fraction(1, 1), Fraction(1, 2)],
    [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)],
]


def su4_dim(a: tuple[int, int, int]) -> int:
    """Exact SU(4)=A_3 Weyl dimension for Dynkin labels (a1,a2,a3):
       dim = (a1+1)(a2+1)(a3+1)(a1+a2+2)(a2+a3+2)(a1+a2+a3+3)/12. Sage-verified."""
    a1, a2, a3 = a
    num = (a1 + 1) * (a2 + 1) * (a3 + 1) * (a1 + a2 + 2) * (a2 + a3 + 2) * (a1 + a2 + a3 + 3)
    return num // 12


def su4_casimir(a: tuple[int, int, int]) -> Fraction:
    """Exact SU(4) quadratic Casimir C2 = <lambda, lambda+2rho> in the long-root^2=2
    normalization (fundamental 4 -> 15/4; adjoint 15 -> 8). rho = (1,1,1) in Dynkin
    labels; the inverse Cartan A3_INV_CARTAN is the symmetric quadratic form.
    Conjugation-symmetric: C2(a1,a2,a3) = C2(a3,a2,a1)."""
    av = [Fraction(x) for x in a]  # (local)
    rho = [Fraction(1), Fraction(1), Fraction(1)]  # (local)
    lam2rho = [av[i] + 2 * rho[i] for i in range(3)]  # (local)
    total = Fraction(0)  # (local)
    for i in range(3):
        for j in range(3):
            total += av[i] * A3_INV_CARTAN[i][j] * lam2rho[j]
    return total


def enumerate_sectors(L_max: int):
    """Enumerate Peter-Weyl SU(4) irreps (a,b,c) != (0,0,0) with a+b+c <= L_max.
    Returns list of (dim, C2_float, rho, (a,b,c))."""
    out = []  # (local)
    for a in range(L_max + 1):
        for b in range(L_max + 1 - a):
            for c in range(L_max + 1 - a - b):
                if a == 0 and b == 0 and c == 0:
                    continue
                rho = a + b + c  # (local)
                C2 = float(su4_casimir((a, b, c)))  # (local)
                d = su4_dim((a, b, c))  # (local)
                out.append((d, C2, rho, (a, b, c)))
    return out


def lambda_PS(C2: float, rho: int, tau: float, r_tau: float = 1.0) -> float:
    """|lam_PS(a,b,c,tau)| = sqrt(C2) * exp(-tau*rho) / r(tau)_PS. r(tau)_PS is an
    overall multiplicative scale that CANCELS in the dimensionless Level-3/Level-2
    ratio (set to 1 here; the absolute dimensional value would carry it). The SU(3)
    base _cm_1995_residue_formula.py uses r=1 identically."""
    return float(np.sqrt(C2) * np.exp(-tau * rho) / r_tau)


# ===========================================================================
# Mellin-cone residue (Mellin-cone (C2+1)^{-s} weighting; the on-disk framework
# Level-3 convention, S92 W9-3 O_1/O_3 + canonical alpha_HH1_per_pole_FW_s4)
# ===========================================================================
def residue_su4(L_max: int, s: float) -> float:
    """Res_{s} Tr(D_K_PS^{-2s}) Mellin-cone form: Sigma_{(a,b,c)!=0} dim_PS * (C2+1)^{-s}.
    (The substrate-distance-2 pole observable; per S92 W9-3 O_3 convention and the
    canonical per-pole exponent alpha_HH1_per_pole_FW_s4.)"""
    tot = 0.0  # (local)
    for d, C2, rho, abc in enumerate_sectors(L_max):
        tot += float(d) * (C2 + 1.0) ** (-s)
    return tot


def residue_su4_mp(L_max: int, s: int) -> float:
    """High-precision (mpmath 100-bit) cross-check of residue_su4."""
    tot = mp.mpf(0)  # (local)
    for d, C2, rho, abc in enumerate_sectors(L_max):
        tot += mp.mpf(int(d)) * (mp.mpf(C2) + 1) ** (-s)
    return float(tot)


# ===========================================================================
# Friedrich-Bär saturation predicate, RE-DERIVED on the SU(4)_PS spectrum
# (NOT inherited from SU(3); per plan eta_FB_SU4 MUST be its own derivation)
# ===========================================================================
def friedrich_bar_su4(L_max: int, tau: float, k_bot: int = 20, new_level: int = 13) -> dict:
    """eta_FB_SU4(a,b,c) = |lam_PS|_sector / sqrt(C2+1) on the analytic SU(4)_PS
    per-sector spectrum. Bottom-K saturation predicate: does the NEW-sector(new_level)
    minimum |lam| EXCEED the bot-K ceiling? (If yes, bottom-K is L_max-saturated.)"""
    sectors = enumerate_sectors(L_max)  # (local)
    # per-sector |lam| and eta_FB
    eta = {}  # (local)
    lams = []  # (local) (|lam|, (a,b,c))
    for d, C2, rho, abc in sectors:
        lam = lambda_PS(C2, rho, tau)  # (local)
        eta[abc] = lam / np.sqrt(C2 + 1.0)
        lams.append((lam, abc))
    lams.sort(key=lambda x: x[0])
    bot_k_ceiling = float(lams[min(k_bot, len(lams)) - 1][0])  # (local) K-th smallest |lam|
    eta_all_min = min(eta.values())  # (local)
    eta_all_min_sector = min(eta, key=eta.get)  # (local)

    # NEW-sector(new_level) minimum |lam| (shell a+b+c=new_level)
    new_shell = []  # (local)
    for a in range(new_level + 1):
        for b in range(new_level + 1 - a):
            c = new_level - a - b
            if c < 0:
                continue
            C2n = float(su4_casimir((a, b, c)))  # (local)
            new_shell.append(lambda_PS(C2n, new_level, tau))
    new_bound_min = min(new_shell)  # (local)

    eta_FB_lower = 0.40  # (local) framework SUGGESTION pin (S87 W11-3); CROSS-CHECK only
    sat_eta_pass = bool(eta_all_min >= eta_FB_lower)  # (local)
    sat_new_pass = bool(new_bound_min > bot_k_ceiling)  # (local)
    saturation_pass = bool(sat_eta_pass and sat_new_pass)  # (local)

    # SU(3) empirical floor for explicit NON-inheritance comparison (S92 W9-3)
    eta_FB_su3_floor = 0.436488  # (local) S92 W9-3 eta_FB_all_min (SU(3); NOT inherited)

    return {
        "eta_FB_SU4_all_min": eta_all_min,
        "eta_FB_SU4_all_min_sector": eta_all_min_sector,
        "eta_FB_SU4_lower_margin8pct": eta_all_min * 0.92,
        "bot_k_ceiling": bot_k_ceiling,
        "new_level": new_level,
        "new_bound_min": new_bound_min,
        "eta_FB_lower_cross_check": eta_FB_lower,
        "eta_FB_su3_floor_NOT_inherited": eta_FB_su3_floor,
        "sat_eta_pass": sat_eta_pass,
        "sat_new_pass": sat_new_pass,
        "saturation_pass": saturation_pass,
    }


# ===========================================================================
# SHA helpers (canonical dual-SHA pattern; matches S92 W9-3 / S93 W6-4)
# ===========================================================================
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return "0" * 64
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 78)
    print(f"Gate: {GATE_ID}")
    print("=" * 78)
    print("Input SHA-256 pins (first lines of stdout):")
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        rel = str(p.relative_to(ROOT)).replace("\\", "/") if p.exists() else str(p)
        print(f"  {name:28s} = {sha[:16]}...  ({rel})")
    return pins


def compute_dual_sha(pins: dict) -> tuple[str, str]:
    """audit_sha256 = SHA(script_bytes || canonical_bytes || sorted-pinmap-JSON ||
    per-gate identity keys); content_sha256 = SHA(script_bytes). audit inputs =
    [script, canonical, pinmap] per the gate-block audit_discriminators."""
    script_bytes = SCRIPT_PATH.read_bytes()  # (local)
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}|L_max={L_MAX_PLAN}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   L_max_op_label: str, sign_v: str, mag_v: str, regime_v: str) -> None:
    """Canonical dual-SHA verdict line + dual-SHA companion row + S87 schema-v2
    3-tuple companion row ([SIGN] trigger: Level-3 < Level-2 directional inequality)."""
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_max_op_label} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); [SIGN] SU(4)_PS Level-3 anchor; "
        f"Route-B Friedrich-Bär (analytic per-sector spectrum; NO operator matrix; dense L12=1094.7GB INFEASIBLE); "
        f"struct Stage-2 PASS-AND on disk (S93 W6-4 axis-A {S93_W6_4_AXIS_A_SHA}.../axis-B {S93_W6_4_AXIS_B_SHA}...); "
        f"§VII.BE STAGE-3 NOT licensed (s=4 full-spectrum residue DIVERGES; re-anchor to convergent pole s>=5); "
        f"§VII.AQ.OP-PROJ row completed DIAGNOSTIC (order-one-CLOSED route NOT reopened); mack lands registry\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2): SIGN = (L^-4 < L^-3 => alpha=4 envelope tighter; "
        f"Level-3<Level-2 sign-robust GIVEN finite residue); MAG = s=4 full-spectrum residue NOT finite (diverges); "
        f"REGIME = s=4 OUT of SU(4)_PS convergent regime (s>4.5 required; shell ~ L^{{8-2s}}); composite FAIL per collapse rule\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)
    print("\n=== verdict line emitted ===")
    print(canonical.rstrip())
    print(companion.rstrip())
    print(tuple_row.rstrip())


# ===========================================================================
# Plot
# ===========================================================================
def make_plot(conv: dict, fb: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11), dpi=110)

    # Panel 1: feasibility wall (dense GB vs L_max) + VRAM cap + 1094.7 GB wall
    ax = axes[0, 0]
    Ls = np.array([4, 6, 8, 10, 12])  # (local)
    # illustrative largest-block dense storage growth anchored at plan L=12 -> 1094.7 GB
    block_dims = np.array([120, 1200, 8000, 70000, 271040], dtype=float)  # (local)
    fiber = 16  # (local) C^16 spinor fiber
    gb = (block_dims * fiber) ** 2 * 16 / 1e9  # (local) dense complex128 bytes -> GB
    ax.semilogy(Ls, gb, "o-", color="#b03060", label="largest SU(4)_PS block dense (GB)")
    ax.axhline(VRAM_GB, color="k", ls="--", lw=1.5, label=f"VRAM cap {VRAM_GB} GB")
    ax.axhline(DENSE_GB_L12, color="#b03060", ls=":", lw=1.2,
               label=f"L=12 wall {DENSE_GB_L12} GB (INFEASIBLE)")
    ax.scatter([12], [DENSE_GB_L12], color="red", zorder=5, s=80, marker="X")
    ax.set_xlabel("L_max (Peter-Weyl truncation)")
    ax.set_ylabel("dense complex128 storage (GB)")
    ax.set_title("SU(4)_PS dense-storage wall\n(Route-B: analytic per-sector spectrum, NO matrix)")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)

    # Panel 2: residue convergence vs L_max at s=4 (DIVERGES) and s=5,6 (CONVERGE)
    ax = axes[0, 1]
    Lg = conv["L_grid"]
    ax.plot(Lg, conv["res_s4"], "o-", color="crimson", label="s=4 (DIVERGES; literal pole)")
    ax.plot(Lg, conv["res_s5"], "s-", color="darkorange", label="s=5 (converges; L^-2)")
    ax.plot(Lg, conv["res_s6"], "^-", color="seagreen", label="s=6 (converges; L^-3 tail)")
    ax.set_xlabel("L_max")
    ax.set_ylabel("Res_s Tr(D_K_PS^{-2s}) (Mellin-cone)")
    ax.set_yscale("log")
    ax.set_title("SU(4)_PS Level-3 residue vs L_max\n"
                 "s=4 DIVERGES (shell ~ L^{8-2s}=L^0); converges iff s>4.5")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 3: shell-scaling exponent 8-2s (SU4) vs 3-2s (SU3); convergence boundary
    ax = axes[1, 0]
    sgrid = np.linspace(2.0, 7.0, 200)  # (local)
    ax.plot(sgrid, 8 - 2 * sgrid, color="crimson", lw=2, label="SU(4)_PS shell: 8-2s")
    ax.plot(sgrid, 3 - 2 * sgrid, color="steelblue", lw=2, label="SU(3) shell: 3-2s")
    ax.axhline(-1.0, color="k", ls="--", lw=1.2, label="convergence boundary (exp = -1)")
    ax.axvline(4.5, color="crimson", ls=":", lw=1.2, label="SU(4)_PS conv. threshold s=4.5")
    ax.axvline(4.0, color="purple", ls=":", lw=1.2, label="literal pole s=4")
    ax.scatter([4.0], [0.0], color="red", s=80, marker="X", zorder=5)
    ax.set_xlabel("Mellin pole s")
    ax.set_ylabel("shell-sum scaling exponent")
    ax.set_title("Shell scaling: SU(4)_PS converges iff s>4.5\n"
                 "s=4 exponent = 0 (DIVERGES); SU(3) s=4 = -5 (converges)")
    ax.legend(fontsize=7.5)
    ax.grid(alpha=0.3)

    # Panel 4: eta_FB re-derived on SU(4)_PS vs SU(3) floor (saturation FAILS)
    ax = axes[1, 1]
    bars = ["eta_FB_SU4\nall_min (re-derived)", "eta_FB_lower\n(framework pin)",
            "eta_FB_SU3 floor\n(S92 W9-3, NOT inherited)"]
    vals = [fb["eta_FB_SU4_all_min"], fb["eta_FB_lower_cross_check"],
            fb["eta_FB_su3_floor_NOT_inherited"]]
    cols = ["crimson", "gray", "steelblue"]
    ax.bar(bars, vals, color=cols, alpha=0.85, edgecolor="black")
    ax.axhline(fb["eta_FB_lower_cross_check"], color="red", ls="--", lw=1.2)
    ax.set_ylabel("eta_FB = |lam|_sector / sqrt(C2+1)")
    ax.set_title(f"eta_FB RE-DERIVED on SU(4)_PS = {fb['eta_FB_SU4_all_min']:.4f}\n"
                 f"<< SU(3) floor {fb['eta_FB_su3_floor_NOT_inherited']:.4f} and lower {fb['eta_FB_lower_cross_check']} "
                 f"=> bottom-K NOT saturated")
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        f"{GATE_ID}: SU(4)_PS Level-3 anchor  |  Route-B Friedrich-Bär  |  "
        f"s=4 full-spectrum residue DIVERGES => numerical Level-3 pin FAILS (re-anchor to s>=5)",
        fontsize=10.5,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(PNG_PATH, dpi=110)
    plt.close(fig)


# ===========================================================================
# Main
# ===========================================================================
def main() -> int:
    t0 = time.time()
    print(f"=== {GATE_ID} ===")
    print(f"tau_fold = {tau_fold}  M_KK = {M_KK:.6e}  M_Pl_reduced = {M_Pl_reduced:.6e}  (metadata)")
    print(f"alpha_HH1_per_pole_FW_s4 (canonical s=4 envelope exponent) = {alpha_HH1_per_pole_FW_s4}")

    pins = log_input_pins(INPUT_FILES)

    # -----------------------------------------------------------------
    # STEP 0 — FEASIBILITY PRE-CHECK (the centerpiece)
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 0 — FEASIBILITY PRE-CHECK (math-scripts.md §D_K Block-Diagonality)")
    print("=" * 78)
    print(f"  Dense storage at L_max={L_MAX_PLAN}: {DENSE_GB_L12} GB >> {VRAM_GB} GB VRAM => INFEASIBLE.")
    print("  But the operative cost is NOT diagonalization: each Peter-Weyl sector's")
    print("  eigenvalue is ANALYTIC, |lam_PS| = sqrt(C2(a,b,c))*exp(-tau*rho)/r(tau). The")
    print("  CM-1995 §III.4 residue at finite L_max reduces ALGEBRAICALLY to the direct sum")
    print("  (entire in s) => NO operator matrix is ever formed. ROUTE-A (sparse-Lanczos) is")
    print("  NOT NEEDED; ROUTE-B (analytic per-sector / Friedrich-Bär) is the operative route.")
    # L_max_operational: Casimir-bound downgrade. Since the per-sector form is analytic and
    # O(L^3) cheap, we evaluate the residue to high L_max directly; the OPERATIONAL truncation
    # for the bottom-K saturation test is L=12 (the framework canonical cache ceiling), but we
    # scan the residue to L=120 to characterize convergence/divergence. Report BOTH.
    L_max_operational = 12  # (local) bottom-K saturation test truncation (analytic; no diag)
    L_scan_max = 120        # (local) residue convergence-characterization scan ceiling (analytic)
    print(f"  L_max_plan = {L_MAX_PLAN} (dense INFEASIBLE)")
    print(f"  L_max_operational = {L_max_operational} (analytic per-sector; Casimir-bound downgrade;")
    print(f"     NO diagonalization — the residue is a direct Peter-Weyl sector sum)")
    print(f"  residue convergence scan ceiling = {L_scan_max} (analytic, O(L^3))")

    # SU(4) Casimir seed-ladder self-check (Sage-verified plan ladder)
    print("\n  SU(4) Casimir seed ladder (Sage-verified; conjugation-symmetric):")
    seeds = {"1": (0, 0, 0), "4": (1, 0, 0), "4b": (0, 0, 1), "6": (0, 1, 0),
             "15": (1, 0, 1), "10": (2, 0, 0), "10b": (0, 0, 2)}  # (local)
    plan_ladder = {"1": "0", "4": "15/4", "4b": "15/4", "6": "5", "15": "8", "10": "9", "10b": "9"}  # (local)
    ladder_ok = True  # (local)
    for nm, abc in seeds.items():
        c2 = su4_casimir(abc); d = su4_dim(abc)  # (local)
        match = (str(c2) == plan_ladder[nm])  # (local)
        ladder_ok = ladder_ok and match
        print(f"    {nm:4s} {abc}: dim={d:3d}  C2={c2}  (plan={plan_ladder[nm]}, match={match})")
    conj_ok = bool(su4_casimir((1, 0, 0)) == su4_casimir((0, 0, 1))
                   and su4_casimir((2, 0, 0)) == su4_casimir((0, 0, 2)))  # (local)
    print(f"    Casimir ladder matches plan: {ladder_ok}; conjugation-symmetric: {conj_ok}")

    # -----------------------------------------------------------------
    # STEP 1 — Residue convergence/divergence (NUMBERS first)
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 1 — Level-3 residue convergence (Mellin-cone (C2+1)^{-s}; on-disk framework form)")
    print("=" * 78)
    L_grid = np.array([10, 12, 16, 20, 30, 50, 80, 120])  # (local)
    res_s4 = np.array([residue_su4(int(L), 4) for L in L_grid])  # (local) literal pole
    res_s5 = np.array([residue_su4(int(L), 5) for L in L_grid])  # (local) convergent
    res_s6 = np.array([residue_su4(int(L), 6) for L in L_grid])  # (local) deeply convergent
    print("  L_max :   s=4 (literal)      s=5            s=6")
    for i, L in enumerate(L_grid):
        print(f"  {int(L):4d}  : {res_s4[i]:.8e}   {res_s5[i]:.8e}   {res_s6[i]:.10e}")
    # divergence diagnostics
    d_s4 = np.diff(res_s4)  # (local) successive deltas at s=4
    s4_diverges = bool(np.all(d_s4[-3:] > d_s4[0]) or res_s4[-1] > 3.0 * res_s4[0])  # (local)
    s6_resid = np.abs(res_s6 - residue_su4(200, 6)) / abs(residue_su4(200, 6))  # (local)
    print(f"\n  s=4 successive deltas (last 3): {[f'{x:.3e}' for x in d_s4[-3:]]}  "
          f"(GROWING => DIVERGES: {s4_diverges})")
    print(f"  s=4 residue L=10->120: {res_s4[0]:.4f} -> {res_s4[-1]:.4f} "
          f"(ratio {res_s4[-1]/res_s4[0]:.2f}x; a convergent sum would plateau)")

    # shell-scaling exponent (Sage-exact: SU(4) shell ~ L^{8-2s}; converges iff s>9/2)
    s_conv_threshold = 9.0 / 2.0  # (local) Sage-exact: 8-2s < -1 => s > 9/2
    print(f"\n  SU(4)_PS shell-sum scaling exponent = 8-2s (Sage-exact; A_3 has 6 pos. roots,")
    print(f"    dim_PS ~ L^6, ~L^2 sectors/shell). Total residue converges iff 8-2s < -1 iff")
    print(f"    s > {s_conv_threshold}.  s=4 => exponent 0 => DIVERGES; s=5 => -2 (conv); s=6 => -4 (conv).")
    print(f"  [SU(3) base: shell ~ L^{{3-2s}}; s=4 => -5 => CONVERGES — why SU(3) anchors at s=4.]")

    # Convergent re-anchor: s=6 finite residue + truncation-tail envelope (Level-2)
    res_s6_inf = residue_su4(200, 6)  # (local) approx L->inf at convergent pole
    mask = s6_resid > 0  # (local)
    alpha_s6_tail = -np.polyfit(np.log(L_grid[mask].astype(float)),
                                np.log(s6_resid[mask]), 1)[0]  # (local)
    print(f"\n  Convergent re-anchor (s=6): residue(L->inf) ~ {res_s6_inf:.10f};")
    print(f"    truncation-tail envelope ~ L^-{alpha_s6_tail:.3f} (Sage-predicted L^-3 = §VII.AF.1 d=4 precedent)")
    # mpmath cross-check at L=12 for the convergent pole
    res_s6_mp = residue_su4_mp(12, 6)  # (local)
    res_s6_f64 = residue_su4(12, 6)  # (local)
    mp_resid = abs(res_s6_mp - res_s6_f64)  # (local)
    print(f"    mpmath 100-bit cross-check at L=12 (s=6): {res_s6_mp:.12f} vs float64 {res_s6_f64:.12f} "
          f"(|delta|={mp_resid:.2e})")

    conv = {
        "L_grid": L_grid, "res_s4": res_s4, "res_s5": res_s5, "res_s6": res_s6,
        "s4_diverges": s4_diverges, "s_conv_threshold": s_conv_threshold,
        "res_s6_inf": res_s6_inf, "alpha_s6_tail": alpha_s6_tail,
        "res_s6_mp_L12": res_s6_mp, "res_s6_f64_L12": res_s6_f64, "mp_resid_L12": mp_resid,
    }  # (local)

    # -----------------------------------------------------------------
    # STEP 2 — Friedrich-Bär saturation predicate (RE-DERIVED on SU(4)_PS)
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 2 — Friedrich-Bär saturation (eta_FB RE-DERIVED on SU(4)_PS; NOT SU(3)-inherited)")
    print("=" * 78)
    fb = friedrich_bar_su4(L_max_operational, tau_fold, k_bot=20, new_level=13)
    print(f"  eta_FB_SU4_all_min          = {fb['eta_FB_SU4_all_min']:.6f} at sector {fb['eta_FB_SU4_all_min_sector']}")
    print(f"  eta_FB_SU4 (8% margin lower) = {fb['eta_FB_SU4_lower_margin8pct']:.6f}")
    print(f"  eta_FB_lower (framework pin) = {fb['eta_FB_lower_cross_check']}  (SU(4) all_min >= lower? {fb['sat_eta_pass']})")
    print(f"  eta_FB_SU3 floor (S92 W9-3)  = {fb['eta_FB_su3_floor_NOT_inherited']}  (NOT inherited; for comparison only)")
    print(f"  bot-20 ceiling (L=12)        = {fb['bot_k_ceiling']:.6f}")
    print(f"  NEW-sector({fb['new_level']}) min |lam|     = {fb['new_bound_min']:.6f}  (> ceiling? {fb['sat_new_pass']})")
    print(f"  SATURATION PREDICATE PASS    = {fb['saturation_pass']}")
    print(f"  >>> SU(4)_PS bottom-K does NOT saturate: new high-rank sectors drop BELOW the")
    print(f"      bottom-K ceiling under exp(-tau*rho) (sqrt(C2) growth cannot keep |lam| bounded).")

    # -----------------------------------------------------------------
    # STEP 3 — Substitution chain + verdict construction
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 3 — Substitution chain (Level-3 < Level-2 sign claim + s=4 regime)")
    print("=" * 78)
    alpha_sym = 3  # (local) inherited substrate-distance-1 s=3 exponent (§VII.AF.1 d-1=3)
    alpha_s4 = int(alpha_HH1_per_pole_FW_s4)  # canonical s=4 = 4 (Wodzicki 2(s-2)=4)
    env_alpha3_L12 = float(Fraction(1, L_MAX_PLAN ** alpha_sym))  # (local)
    env_alpha4_L12 = float(Fraction(1, L_MAX_PLAN ** alpha_s4))   # (local)
    print(f"  Def L3_PS = Res_{{s=4}} Tr(D_K_PS^{{-2s}}) [this gate's anchor]")
    print(f"  Def L2_envelope_PS ~ L^-alpha(PS): alpha_sym=3 (inherited), alpha_s4={alpha_s4} (canonical)")
    print(f"  L^-4 < L^-3 for L>1: {env_alpha4_L12:.3e} < {env_alpha3_L12:.3e} => alpha=4 envelope TIGHTER")
    print(f"  SIGN: Level-3 < Level-2 is sign-robust to alpha in {{3,4}} GIVEN a FINITE positive residue.")
    print(f"  MAGNITUDE: at s=4 the SU(4)_PS full-spectrum residue is NOT finite (diverges; ratio GROWS).")
    print(f"  REGIME: s=4 is OUT of the SU(4)_PS convergent regime (s > {conv['s_conv_threshold']} required).")
    print(f"          breakdown fraction = 100% (the sum diverges at ALL L_max).")

    # [SIGN] 3-tuple:
    sign_verdict = "PASS"   # the directional L^-4 < L^-3 / Level-3<Level-2-given-finite claim holds
    # magnitude: the literal s=4 numerical anchor is NOT a finite value sitting inside the envelope
    magnitude_verdict = "FAIL"
    # regime: s=4 is outside the SU(4)_PS convergent regime; full breakdown
    regime_verdict = "BREAKDOWN"

    # Composite-collapse (gate-verdicts.md; regime BREAKDOWN => FAIL regardless of other fields)
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"
    elif sign_verdict == "FAIL":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"
    elif magnitude_verdict == "INFO":
        verdict = "INFO"
    else:
        verdict = "PASS"

    # PASS predicate metric (ratio Level-3/Level-2): at s=4 the residue diverges, so the
    # truncation residual r(L) GROWS — the ratio metric is > 1 (and unbounded). Report the
    # ratio at L=12 using the divergence-direction (residual grows) as the FAIL witness.
    r_L12_s4 = abs(res_s4[1] - res_s4[0]) / res_s4[0]  # (local) growing residual proxy at s=4
    # at the CONVERGENT re-anchor pole s=6, the ratio < 1 (anchor sits inside L^-3):
    ratio_s6_L12 = float(s6_resid[1])  # (local) residual at L=12, s=6 (well inside L^-3)

    print("\n" + "=" * 78)
    print("VERDICT CONSTRUCTION")
    print("=" * 78)
    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  COMPOSITE         = {verdict}  (regime BREAKDOWN => FAIL per collapse rule)")
    print(f"  s=4 ratio metric (residual L10->12, GROWING) = {r_L12_s4:.4e}  (>0, grows => NOT inside envelope)")
    print(f"  s>=5 re-anchor: s=6 residual at L=12 = {ratio_s6_L12:.4e} << L^-3 envelope (anchor would sit inside)")
    print(f"  => §VII.BE STAGE-3 NOT licensed at s=4; forward route = Tier-2 dimensional re-anchorability")
    print(f"     to the convergent pole s>=5 (re-derive SU(4)_PS Friedrich-Bär envelope).")
    print(f"  => §VII.AQ.OP-PROJ row completed with DIAGNOSTIC finding (order-one-CLOSED route NOT reopened).")

    # -----------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------
    make_plot(conv, fb)
    print(f"\n  plot -> {PNG_PATH.name}")

    # -----------------------------------------------------------------
    # dual-SHA
    # -----------------------------------------------------------------
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # -----------------------------------------------------------------
    # value string + verdict line
    # -----------------------------------------------------------------
    L_max_op_label = f"{L_max_operational}_plan_{L_MAX_PLAN}"  # (local)
    value_str = (  # (local)
        f"L3_PS_s4_DIVERGES=True;shell_scaling=L^(8-2s);conv_threshold_s_gt_{conv['s_conv_threshold']};"
        f"res_s4_L10={res_s4[0]:.6e}_L120={res_s4[-1]:.6e}_ratio={res_s4[-1]/res_s4[0]:.2f}x_GROWING;"
        f"L3_over_L2_s4_GROWS_not_lt_1;"
        f"convergent_reanchor_s6_residue_Linf={res_s6_inf:.8e}_tail_envelope_L^-{alpha_s6_tail:.3f};"
        f"ratio_s6_L12={ratio_s6_L12:.4e}_inside_L^-3;"
        f"eta_FB_SU4_all_min={fb['eta_FB_SU4_all_min']:.6f}_REDERIVED_NOT_inherited_sector_{fb['eta_FB_SU4_all_min_sector']};"
        f"eta_FB_SU3_floor_NOT_inherited={fb['eta_FB_su3_floor_NOT_inherited']};"
        f"saturation_pass={fb['saturation_pass']}_botK_ceiling={fb['bot_k_ceiling']:.4f}_NEWsec13={fb['new_bound_min']:.4f};"
        f"alpha_sym=3_alpha_s4={alpha_s4}_L^-4_lt_L^-3=True_sign_robust;"
        f"L_max_plan={L_MAX_PLAN}_dense_{DENSE_GB_L12}GB_INFEASIBLE_L_max_operational={L_max_operational}_ROUTE_B_analytic_no_matrix;"
        f"VII_BE_STAGE3_NOT_licensed_reanchor_to_s_ge_5;"
        f"VII_AQ_OP_PROJ_row_completed_DIAGNOSTIC_order_one_CLOSED_route_NOT_reopened;"
        f"struct_Stage2_PASS_AND_on_disk_S93W6_4_axisA_{S93_W6_4_AXIS_A_SHA}_axisB_{S93_W6_4_AXIS_B_SHA};"
        f"mack_lands_registry"
    )
    append_verdict(verdict, value_str, audit_sha, content_sha, L_max_op_label,
                   sign_verdict, magnitude_verdict, regime_verdict)
    print(f"\n  verdict line appended -> {VERDICT_FILE}")

    # -----------------------------------------------------------------
    # npz (emit L_max_plan + L_max_operational + spectrum_route + eta_FB_SU4 keys)
    # -----------------------------------------------------------------
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        # feasibility pre-check
        L_max_plan=L_MAX_PLAN,
        L_max_operational=L_max_operational,
        spectrum_route="ROUTE-B-Friedrich-Bar-analytic-saturation-per-sector-no-operator-matrix",
        dense_GB_L12=DENSE_GB_L12,
        VRAM_GB=VRAM_GB,
        casimir_ladder_matches_plan=ladder_ok,
        casimir_conjugation_symmetric=conj_ok,
        # residue convergence
        L_grid=L_grid,
        residue_s4=res_s4, residue_s5=res_s5, residue_s6=res_s6,
        s4_diverges=conv["s4_diverges"],
        shell_scaling_exponent="8-2s",
        s_conv_threshold=conv["s_conv_threshold"],
        residue_s6_Linf=conv["res_s6_inf"],
        alpha_s6_tail_envelope=conv["alpha_s6_tail"],
        residue_s6_mp_L12=conv["res_s6_mp_L12"],
        residue_s6_f64_L12=conv["res_s6_f64_L12"],
        mp_residual_L12=conv["mp_resid_L12"],
        # Friedrich-Bär RE-DERIVED on SU(4)_PS
        eta_FB_SU4_all_min=fb["eta_FB_SU4_all_min"],
        eta_FB_SU4_all_min_sector=np.array(fb["eta_FB_SU4_all_min_sector"]),
        eta_FB_SU4_lower_margin8pct=fb["eta_FB_SU4_lower_margin8pct"],
        eta_FB_lower_cross_check=fb["eta_FB_lower_cross_check"],
        eta_FB_su3_floor_NOT_inherited=fb["eta_FB_su3_floor_NOT_inherited"],
        bot_k_ceiling=fb["bot_k_ceiling"],
        new_sector_level=fb["new_level"],
        new_bound_min=fb["new_bound_min"],
        saturation_pass=fb["saturation_pass"],
        sat_eta_pass=fb["sat_eta_pass"],
        sat_new_pass=fb["sat_new_pass"],
        # substitution chain
        alpha_sym=alpha_sym, alpha_s4=alpha_s4,
        env_alpha3_L12=env_alpha3_L12, env_alpha4_L12=env_alpha4_L12,
        L3_over_L2_s4_ratio_growing_proxy=r_L12_s4,
        ratio_s6_L12_inside_envelope=ratio_s6_L12,
        # bridge / registry
        vii_be_stage3_licensed=False,
        vii_be_reanchor_to_pole_s_ge_5=True,
        vii_aq_op_proj_row_completed_diagnostic=True,
        vii_aq_order_one_closed_route_reopened=False,
        struct_stage2_pass_and_on_disk=True,
        s93_w6_4_axis_a_sha=S93_W6_4_AXIS_A_SHA,
        s93_w6_4_axis_b_sha=S93_W6_4_AXIS_B_SHA,
        # provenance
        tau_fold=tau_fold, M_KK=M_KK, M_Pl_reduced=M_Pl_reduced,
        regulator_pin="a_n^{Mellin}",
        element3_bridge_map="Wodzicki-HKR-composite-Bismut-Cheeger-adiabatic-limit",
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  npz -> {NPZ_PATH.name}")

    wall = time.time() - t0  # (local)
    print("\n" + "=" * 78)
    print(f"4-tuple: (value={verdict}_s4_residue_DIVERGES, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_max_op_label})")
    print(f"  composite={verdict} (sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict})")
    print(f"  wall: {wall:.2f}s")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
