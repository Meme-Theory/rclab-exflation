#!/usr/bin/env python
"""
CF-S95-VII-BE-TIER2-REANCHOR
============================

Re-anchor the §VII.BE FWD-C4 Pati-Salam cross-pillar-bridge numerical Level-3 at
the SUBSTRATE-SINGLED-OUT CONVERGENT Mellin pole s>=5 (candidate s=6). The S94 W3-9
finding (gate S94-VII-PS-FULL-SPECTRUM-LEVEL-3, FAIL): the inherited substrate-
distance-2 pole s=4 DIVERGES for SU(4)_PS because the rank-4 (A_3 = 6 positive
roots) Weyl dimension grows as L^6 and there are ~L^2 Peter-Weyl sectors per shell,
so the full-spectrum Mellin-cone residue shell-sum scales L^{8-2s}, converging IFF
8-2s < -1, i.e. s > 9/2 = 4.5 (Sage-exact). The SU(3) base scales L^{3-2s} = L^{-5}
at s=4 and converges -- which is why the SM-gauge child anchors Level-3 at s=4. The
SU(4)_PS PARENT triple does NOT anchor at the child's convergent pole; its own
convergent pole sits at s >= 5.

This gate (the lizzi-spectral-functional-theorist's forward route per the §VII.BE
S94 W3-9 FAIL annotation, registry line 20645): re-pin the Level-3 anchor to s=6.
The choice s=4 -> s=6 is NOT a convention -- it is FORCED by the SU(4)_PS spectral
dimension (the rank-4 algebra shifts the Mellin convergence threshold UP by exactly
one unit, 9/2 vs SU(3)'s 3/2). The inherited s=4 pole was a CHILD-ALGEBRA artifact;
re-anchoring to the parent's OWN convergent pole is substrate-first correction.

NUMBERS first, gate second, interpretation third.

Substrate framing (GEOMETRIC; IS-not-IN): the substrate IS the Pati-Salam parent
spectral triple (A_K_PS = C (+) M_2(C)_L (+) M_2(C)_R (+) M_4(C)_PS, H_K_PS, D_K_PS)
at tau_fold = 0.19. D_K_PS is BLOCK-DIAGONAL by Peter-Weyl over SU(4) irreps (a,b,c);
each block's eigenvalue |lam_PS(a,b,c)| = sqrt(C2(a,b,c))*exp(-tau*rho)/r(tau) is
ANALYTIC (the (C2+1) Casimir ladder), so the CM-1995 §III.4 Mellin-cone residue at
finite L_max reduces ALGEBRAICALLY to the direct Peter-Weyl sector sum -- NO operator
matrix is ever formed (dense storage at L=12 = 1094.7 GB >> 17.1 GB VRAM INFEASIBLE).
The Level-3 spectral-action residue Res_{s} Tr(D_K_PS^{-2s}) is a spectral moment
read OFF the eigenvalues, NOT a field on an internal container. Direction of
explanation: D_K_PS spectrum (rank-4 Peter-Weyl, dim ~ L^6) -> Mellin-cone residue at
pole s -> convergent only at s > 9/2 -> re-anchor to s=6 -> Level-3 < Level-2.

CAUTION (the exact error this agent is built to catch): the Level-2 envelope is the
EMPIRICAL L^{-2.804} truncation tail of the SU(4)_PS SPECTRAL-ACTION residue (the
substrate's own truncation envelope at the convergent pole), NOT the HH^1 cocycle-
family Wodzicki envelope alpha_HH1_per_pole_FW_s6 = 2(s-2) = 8 (a DIFFERENT
observable: the HH^1 cocycle norm). Conflating them would substitute one spectral
functional for another. The gate pins the empirical 2.804, NOT 8.

Tier-1/Tier-2 gate (cross-pillar-bridge-anatomy.md §"Registry-PASS criterion" ->
"Tier-1/Tier-2 dimensional-re-anchorability gate"; corpus §25):
  Tier-1 (registry-PASS-ELIGIBLE): residual-to-c_continuum SHRINKS with L_max
          (convergent => a substrate-singled-out L* exists) AND Level-3 < Level-2 at
          canonical L_max. The s=6 SU(4)_PS residue IS convergent (shell exp -4 < -1).
  Tier-2 fallback: if Tier-1 does not anchor cleanly, re-anchor to a DIMENSIONLESS
          truncation-invariant functional (residue log-derivative d ln Res/d ln L,
          which annihilates any multiplicative L-divergent prefactor per
          math-scripts.md §"Multiplicative-normalization cancellation invariants").
  Contrast (dimension-keyed): §VII.AV L_emp is Tier-1-CONVERGENT + Tier-2-dimensionless
          (RE-ANCHOR available; STAGE-3-PERMANENT earned); §VII.AX n_PBH is Tier-1-FAIL
          + Tier-2-DIMENSIONFUL (HELD). The s=6 SU(4)_PS residue is the §VII.AV pattern.

Operationalization of the registry-PASS predicate (Level-3 < Level-2 at canonical
L_max=12), matching the on-disk S94 W3-9 ratio_s6_L12_inside_envelope = 7.6869e-4 and
the §VII.AV/§VII.AX Friedrich-Bar envelope precedent:
  Level-3(s=6, L=12) = the substrate-IS truncation residual at the canonical L_max --
          the relative distance |Res(L=12) - Res(L->inf)| / |Res(L->inf)| of the L=12
          truncated partial sum from its continuum (L->inf) image. This IS the
          substrate-IS distance from the laboratory-IN continuum observable.
  Level-2(s=6, L=12) = the Friedrich-Bar truncation envelope C_FB(s=6) * 12^{-alpha},
          with alpha and C_FB FITTED on the ASYMPTOTIC TAIL (L >= 16, EXCLUDING the
          canonical L=12 test point so the L=12 comparison is a genuine test, not a
          self-fit). alpha is the empirical SPECTRAL-ACTION residue tail (~2.804), NOT
          the HH^1 Wodzicki 8.
  PASS iff Level-3 < Level-2 (ratio < 1): the L=12 anchor sits INSIDE the envelope.

Regulator pin: a_n^{Mellin} (CM-1995 §III.4 Mellin-transform residue class).
Element-3 bridge map (5-anatomy): Wodzicki o HKR composite, scheme suffix
-Bismut-Cheeger (adiabatic-limit eta-form at boundary).

Owner: lizzi-spectral-functional-theorist.
Plan: sessions/session-plan/session-95-plan-w1.md §W1-3.
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
    alpha_HH1_per_pole_FW_s4,   # canonical s=4 envelope exponent (=4; Wodzicki 2(s-2))
    alpha_HH1_per_pole_FW_s6,   # canonical s=6 HH^1 Wodzicki exponent (=8); NOT used as Level-2 (different observable)
)

mp.mp.prec = 120  # ~36 decimal digits for residue cross-check

# ===========================================================================
# Identity
# ===========================================================================
GATE_ID = "CF-S95-VII-BE-TIER2-REANCHOR"
SCHEME = "SU(4)_PS-Mellin-cone-residue-convergent-pole-s6"
CONVENTION = "VII-BE-TIER2-REANCHOR-convergent-pole-s6-Tier-1-OR-dimensionless-Tier-2"
SCHEMA_VERSION = "S87+"

L_MAX = 12            # (local) canonical SU(4)_PS truncation (the §W3-9 cache ceiling)
L_INF_PROXY = 200     # (local) analytic L->inf residue proxy (per S94 W3-9)
TOL_RATIO = 1e-3      # (local) PASS-band tolerance for the Level-3/Level-2 ratio convergence floor
INFO_BAND = 1.10      # (local) ratio in [1, info_band] => INFO (borderline); > info_band => FAIL
RESIDUE_S6_TARGET = 9.39363958e-4  # (local) S94 W3-9 residue(L->inf) at s=6 -- CONFIRMED here, not assumed
ALPHA_S6_OBSERVED = 2.804          # (local) S94 W3-9 observed spectral-action residue tail (NOT HH^1 alpha=8)

SESSION_DIR = ROOT / "computations" / "session-95"
VERDICT_FILE = SESSION_DIR / "s95_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
NPZ_PATH = SESSION_DIR / "s95_w1_3_vii_be_tier2_reanchor.npz"
PNG_PATH = SESSION_DIR / "s95_w1_3_vii_be_tier2_reanchor.png"

# Input files
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
PS_SPECTRUM_NPZ = ROOT / "computations" / "session-94" / "s94_vii_ps_full_spectrum_level_3.npz"
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
CM_1995_RESIDUE = ROOT / "computations" / "_shared" / "_cm_1995_residue_formula.py"

# Structural Stage-2 PASS-AND provenance (S93 W6-4; on disk; UNAFFECTED by this gate)
S93_W6_4_AXIS_A_SHA = "146b5742"   # connes axis-A INFO (structural PASS-AND)
S93_W6_4_AXIS_B_SHA = "9df77b09"   # landau axis-B INFO (structural PASS-AND)
S94_W3_9_FAIL_SHA = "697fe532"     # S94 W3-9 s=4-diverges FAIL (the SETTLED finding this gate forwards from)

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "ps_spectrum_npz": PS_SPECTRUM_NPZ,
    "registry_be_entry": REGISTRY,
    "cm_1995_residue": CM_1995_RESIDUE,
    "script": SCRIPT_PATH,
}

# ===========================================================================
# SU(4) = A_3 representation theory (EXACT; re-used VERBATIM from S94 W3-9
# s94_vii_ps_full_spectrum_level_3.py lines 159-210 -- NO fresh derivation;
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
    """Exact SU(4) quadratic Casimir C2 = <lambda, lambda+2rho>, long-root^2=2
    normalization (fundamental 4 -> 15/4; adjoint 15 -> 8). Conjugation-symmetric."""
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


def residue_su4(L_max: int, s: float) -> float:
    """Res_{s} Tr(D_K_PS^{-2s}) Mellin-cone form: Sigma_{(a,b,c)!=0} dim_PS*(C2+1)^{-s}.
    The substrate-distance-2 pole observable (S92 W9-3 O_3 convention). Re-used from
    S94 W3-9; the SU(4)_PS spectrum IS the analytic (C2+1) Casimir ladder -- no diag."""
    tot = 0.0  # (local)
    for d, C2, rho, abc in enumerate_sectors(L_max):
        tot += float(d) * (C2 + 1.0) ** (-s)
    return tot


def residue_su4_mp(L_max: int, s: int) -> float:
    """High-precision (mpmath 120-bit) cross-check of residue_su4."""
    tot = mp.mpf(0)  # (local)
    for d, C2, rho, abc in enumerate_sectors(L_max):
        tot += mp.mpf(int(d)) * (mp.mpf(C2) + 1) ** (-s)
    return float(tot)


# ===========================================================================
# SHA helpers (canonical dual-SHA pattern; matches S94 W3-9)
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
        print(f"  {name:24s} = {sha[:16]}...  ({rel})")
    return pins


def compute_dual_sha(pins: dict) -> tuple[str, str]:
    """audit_sha256 = SHA(script_bytes || canonical_bytes || sorted-pinmap-JSON ||
    per-gate identity keys); content_sha256 = SHA(script_bytes). audit inputs =
    [script, canonical, pinmap, ps_spectrum_npz_sha, registry_be_text_sha] per the
    gate-block audit_discriminators."""
    script_bytes = SCRIPT_PATH.read_bytes()  # (local)
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}|L_max={L_MAX}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Canonical dual-SHA verdict line + dual-SHA companion row + S87 schema-v2
    3-tuple companion row ([SIGN] trigger: convergence sign of (8-2s+1) + Level-3 <
    Level-2 directional inequality). Atomic single open('a') append."""
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] §VII.BE FWD-C4 Level-3 RE-ANCHOR to convergent pole s=6; "
        f"SU(4)_PS shell scaling L^(8-2s) converges iff s>9/2 (Sage-exact); s=4 DIVERGES (S94 W3-9 {S94_W3_9_FAIL_SHA}...); "
        f"s=6 residue(L->inf) CONFIRMED ~9.39363958e-4 tail L^-2.804 (NOT HH^1 alpha=8); "
        f"Tier-1 convergent-pole route (Tier-2-dimensionless fallback ready, the §VII.AV pattern); "
        f"struct Stage-2 PASS-AND on disk (S93 W6-4 axis-A {S93_W6_4_AXIS_A_SHA}.../axis-B {S93_W6_4_AXIS_B_SHA}...) UNAFFECTED; "
        f"mack lands registry STAGE-3 review on PASS\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2): SIGN = (8-2s+1 < 0 at s=6 => residue CONVERGES; "
        f"Level-3 truncation residual < Level-2 Friedrich-Bar envelope => ratio < 1); "
        f"MAG = |ratio - 0| vs PASS-band (ratio<1 PASS); "
        f"REGIME = s=6 INSIDE SU(4)_PS convergent regime (s>4.5; shell exp -4 < -1); composite per collapse rule\n"
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
def make_plot(d: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11), dpi=110)

    # Panel 1: residue(L) at poles s in {5,6,7} + s=4 (diverges)
    ax = axes[0, 0]
    Lg = d["L_grid"]
    ax.plot(Lg, d["res_s4"], "o-", color="crimson", label="s=4 (DIVERGES; inherited pole)")
    ax.plot(Lg, d["res_s5"], "s-", color="darkorange", label="s=5 (converges; shell L^-2)")
    ax.plot(Lg, d["res_s6"], "^-", color="seagreen", label="s=6 (converges; shell L^-4)")
    ax.plot(Lg, d["res_s7"], "v-", color="navy", label="s=7 (converges; shell L^-6)")
    ax.axvline(L_MAX, color="k", ls=":", lw=1.0, label=f"canonical L_max={L_MAX}")
    ax.set_xlabel("L_max (Peter-Weyl truncation)")
    ax.set_ylabel("Res_s Tr(D_K_PS^{-2s}) (Mellin-cone)")
    ax.set_yscale("log")
    ax.set_title("SU(4)_PS Level-3 residue vs L_max\n"
                 "s=4 DIVERGES (shell L^{8-2s}=L^0); converges iff s>9/2")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2: shell-scaling exponent 8-2s vs convergence boundary
    ax = axes[0, 1]
    sgrid = np.linspace(3.0, 7.5, 200)  # (local)
    ax.plot(sgrid, 8 - 2 * sgrid, color="crimson", lw=2, label="SU(4)_PS shell: 8-2s")
    ax.plot(sgrid, 3 - 2 * sgrid, color="steelblue", lw=2, label="SU(3) base shell: 3-2s")
    ax.axhline(-1.0, color="k", ls="--", lw=1.2, label="convergence boundary (exp = -1)")
    ax.axvline(4.5, color="crimson", ls=":", lw=1.2, label="SU(4)_PS threshold s=9/2")
    ax.axvline(4.0, color="purple", ls=":", lw=1.0, label="inherited pole s=4 (DIVERGES)")
    ax.scatter([4.0], [0.0], color="red", s=80, marker="X", zorder=5)
    ax.scatter([6.0], [8 - 12], color="seagreen", s=80, marker="o", zorder=5,
               label="re-anchor s=6 (exp -4)")
    ax.set_xlabel("Mellin pole s")
    ax.set_ylabel("shell-sum scaling exponent")
    ax.set_title("Shell scaling: SU(4)_PS converges iff s>9/2\n"
                 "s=6 exp = -4 (CONVERGES); re-anchor pole")
    ax.legend(fontsize=7.2)
    ax.grid(alpha=0.3)

    # Panel 3: s=6 relative truncation residual vs L + L^{-alpha} tail fit (Level-2 envelope)
    ax = axes[1, 0]
    Lf = d["L_grid"].astype(float)
    ax.loglog(Lf, d["s6_resid_rel"], "o", color="seagreen", ms=8,
              label="s=6 rel. truncation residual |Res(L)-Res(inf)|/Res(inf)")
    Lfit = np.linspace(Lf.min(), Lf.max(), 100)  # (local)
    env = d["C_FB"] * Lfit ** (-d["alpha_tail"])  # (local)
    ax.loglog(Lfit, env, "-", color="crimson", lw=1.8,
              label=f"Level-2 envelope C_FB·L^-{d['alpha_tail']:.3f} (tail fit L>=16; EMPIRICAL, NOT HH^1 alpha=8)")
    ax.axvline(L_MAX, color="k", ls=":", lw=1.0)
    ax.scatter([float(L_MAX)], [d["level3_rel_L12"]], color="purple", s=110, marker="*",
               zorder=6, label=f"Level-3(L=12) rel resid = {d['level3_rel_L12']:.3e}")
    ax.scatter([float(L_MAX)], [d["level2_rel_L12"]], color="red", s=90, marker="D",
               zorder=6, label=f"Level-2(L=12) envelope = {d['level2_rel_L12']:.3e}")
    ax.set_xlabel("L_max")
    ax.set_ylabel("relative truncation residual / envelope")
    ax.set_title(f"Tier-1 Level-3 < Level-2 at L=12: ratio = {d['ratio_L3_L2']:.4f} "
                 f"({'PASS <1' if d['ratio_L3_L2'] < 1 else 'NOT <1'})")
    ax.legend(fontsize=6.8)
    ax.grid(alpha=0.3, which="both")

    # Panel 4: Tier-2 dimensionless functional -- residue log-derivative d ln Res/d ln L -> 0
    ax = axes[1, 1]
    ax.plot(d["logderiv_L"], d["logderiv_s6"], "^-", color="seagreen",
            label="s=6 d ln Res / d ln L (Tier-2 dimensionless)")
    ax.plot(d["logderiv_L"], d["logderiv_s4"], "o-", color="crimson",
            label="s=4 d ln Res / d ln L (DIVERGES; -> +const > 0)")
    ax.axhline(0.0, color="k", ls="--", lw=1.0, label="convergent => log-deriv -> 0")
    ax.set_xlabel("L_max")
    ax.set_ylabel("d ln Res_s / d ln L")
    ax.set_title("Tier-2 dimensionless functional (residue log-derivative)\n"
                 "s=6 -> 0 (DIMENSIONLESS, re-anchorable; §VII.AV pattern); s=4 stays > 0")
    ax.legend(fontsize=7.5)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}: §VII.BE FWD-C4 Level-3 RE-ANCHOR to convergent pole s=6  |  "
        f"residue(inf)={d['res_s6_inf']:.6e} tail L^-{d['alpha_tail']:.3f}  |  "
        f"Tier-1 ratio={d['ratio_L3_L2']:.4f}",
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
    print(f"alpha_HH1_per_pole_FW_s4 (canonical s=4 HH^1 exponent) = {alpha_HH1_per_pole_FW_s4}")
    print(f"alpha_HH1_per_pole_FW_s6 (canonical s=6 HH^1 exponent) = {alpha_HH1_per_pole_FW_s6}  "
          f"<-- NOT used as Level-2 (HH^1 cocycle observable, DISTINCT from spectral-action residue tail)")

    pins = log_input_pins(INPUT_FILES)

    # -----------------------------------------------------------------
    # STEP 0 -- cross-check the SU(4) Casimir ladder against S94 W3-9 (Sage-verified)
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 0 -- SU(4) Casimir ladder self-check (Sage-verified; conjugation-symmetric)")
    print("=" * 78)
    seeds = {"1": (0, 0, 0), "4": (1, 0, 0), "4b": (0, 0, 1), "6": (0, 1, 0),
             "15": (1, 0, 1), "10": (2, 0, 0), "10b": (0, 0, 2)}  # (local)
    plan_ladder = {"1": "0", "4": "15/4", "4b": "15/4", "6": "5", "15": "8", "10": "9", "10b": "9"}  # (local)
    ladder_ok = True  # (local)
    for nm, abc in seeds.items():
        c2 = su4_casimir(abc); dd = su4_dim(abc)  # (local)
        match = (str(c2) == plan_ladder[nm])  # (local)
        ladder_ok = ladder_ok and match
        print(f"    {nm:4s} {abc}: dim={dd:3d}  C2={c2}  (plan={plan_ladder[nm]}, match={match})")
    conj_ok = bool(su4_casimir((1, 0, 0)) == su4_casimir((0, 0, 1))
                   and su4_casimir((2, 0, 0)) == su4_casimir((0, 0, 2)))  # (local)
    print(f"    Casimir ladder matches plan: {ladder_ok}; conjugation-symmetric: {conj_ok}")

    # -----------------------------------------------------------------
    # STEP 1 -- pole-scan s in {4,5,6,7}: confirm shell exponent 8-2s convergence
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 1 -- pole-scan s in {4,5,6,7}: shell exponent 8-2s; converges iff s>9/2 (Sage-exact)")
    print("=" * 78)
    L_grid = np.array([10, 12, 16, 20, 30, 50, 80, 120])  # (local) matches S94 W3-9 scan
    res_s4 = np.array([residue_su4(int(L), 4) for L in L_grid])  # (local) inherited pole (DIVERGES)
    res_s5 = np.array([residue_su4(int(L), 5) for L in L_grid])  # (local) convergent
    res_s6 = np.array([residue_su4(int(L), 6) for L in L_grid])  # (local) deeply convergent (re-anchor)
    res_s7 = np.array([residue_su4(int(L), 7) for L in L_grid])  # (local) deeply convergent
    print("  L_max :   s=4 (inherited)    s=5            s=6 (re-anchor)   s=7")
    for i, L in enumerate(L_grid):
        print(f"  {int(L):4d}  : {res_s4[i]:.8e}   {res_s5[i]:.8e}   {res_s6[i]:.10e}   {res_s7[i]:.10e}")

    # Sage-exact shell exponent table (mirrors the Sage MCP verification this session)
    s_conv_threshold = Fraction(9, 2)  # (local) Sage-exact: 8-2s < -1 => s > 9/2
    pole_conv = {}  # (local)
    print(f"\n  Sage-exact: SU(4)_PS shell exponent = 8-2s; converges iff 8-2s < -1 i.e. s > {s_conv_threshold} = 4.5")
    for sv in [4, 5, 6, 7]:
        exp_shell = 8 - 2 * sv  # (local)
        conv = bool(exp_shell < -1)  # (local)
        pole_conv[sv] = conv
        print(f"    s={sv}: shell exponent 8-2s = {exp_shell:+d}, converges? {conv}")

    # Divergence diagnostic at s=4 (the SETTLED S94 W3-9 finding)
    s4_diverges = bool(res_s4[-1] > 3.0 * res_s4[0])  # (local)
    print(f"\n  s=4 residue L=10->120: {res_s4[0]:.6f} -> {res_s4[-1]:.6f} "
          f"(ratio {res_s4[-1]/res_s4[0]:.2f}x; DIVERGES = {s4_diverges}) -- SETTLED S94 W3-9, not re-litigated")

    # -----------------------------------------------------------------
    # STEP 2 -- CONFIRM the s=6 convergent anchor: residue(L->inf) + truncation tail
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 2 -- CONFIRM s=6 convergent anchor (residue(L->inf) ~ 9.39363958e-4, tail L^-2.804)")
    print("=" * 78)
    res_s6_inf = residue_su4(L_INF_PROXY, 6)  # (local) analytic L->inf proxy
    res_s6_inf_mp = residue_su4_mp(L_INF_PROXY, 6)  # (local) 120-bit cross-check
    delta_target = abs(res_s6_inf - RESIDUE_S6_TARGET)  # (local)
    print(f"  residue(L->inf, s=6) = {res_s6_inf:.12e}")
    print(f"    mpmath 120-bit cross-check  = {res_s6_inf_mp:.12e}  (|delta_f64_mp| = {abs(res_s6_inf-res_s6_inf_mp):.2e})")
    print(f"    S94 W3-9 target 9.39363958e-4: |delta| = {delta_target:.3e}  "
          f"(CONFIRMED: {delta_target < 1e-8})")

    # relative truncation residual at each L (distance from continuum L->inf image)
    s6_resid_rel = np.abs(res_s6 - res_s6_inf) / abs(res_s6_inf)  # (local) Level-3 candidate per L
    # full-grid tail exponent (matches S94 W3-9 alpha_s6_tail = 2.8035709624)
    mask_full = s6_resid_rel > 0  # (local)
    alpha_full = float(-np.polyfit(np.log(L_grid[mask_full].astype(float)),
                                   np.log(s6_resid_rel[mask_full]), 1)[0])  # (local)
    print(f"\n  s=6 relative truncation residual per L:")
    for i, L in enumerate(L_grid):
        print(f"    L={int(L):4d}: rel_resid = {s6_resid_rel[i]:.6e}")
    print(f"  full-grid tail exponent alpha = {alpha_full:.6f}  (S94 W3-9 = 2.8035709624; EMPIRICAL spectral-action residue tail)")
    print(f"  NOTE: alpha = {alpha_full:.3f} is the SU(4)_PS SPECTRAL-ACTION residue truncation tail; "
          f"the HH^1 Wodzicki exponent alpha_HH1_per_pole_FW_s6 = {alpha_HH1_per_pole_FW_s6} is a DIFFERENT observable -- NOT used.")

    # -----------------------------------------------------------------
    # STEP 3 -- Tier-1 registry-PASS predicate: Level-3 < Level-2 at canonical L_max=12
    #   Level-2 envelope fit on the ASYMPTOTIC TAIL (L >= 16, EXCLUDING the L=12 test
    #   point) so the L=12 comparison is a genuine test, NOT a self-fit.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 3 -- Tier-1: Level-3(s=6, L=12) < Level-2 envelope C_FB·12^-alpha (tail fit L>=16)")
    print("=" * 78)
    tail_mask = L_grid >= 16  # (local) EXCLUDE the canonical L=12 test point
    A = np.polyfit(np.log(L_grid[tail_mask].astype(float)),
                   np.log(s6_resid_rel[tail_mask]), 1)  # (local)
    alpha_tail = float(-A[0])  # (local) Friedrich-Bar envelope exponent (tail-only)
    C_FB = float(np.exp(A[1]))  # (local) Friedrich-Bar envelope constant
    # Level-3 = the substrate-IS relative truncation residual at canonical L_max=12
    L12_idx = int(np.where(L_grid == L_MAX)[0][0])  # (local)
    level3_rel_L12 = float(s6_resid_rel[L12_idx])  # (local)
    # Level-2 = Friedrich-Bar envelope at L=12 (tail-fit; L=12 EXCLUDED from fit)
    level2_rel_L12 = float(C_FB * float(L_MAX) ** (-alpha_tail))  # (local)
    ratio_L3_L2 = level3_rel_L12 / level2_rel_L12  # (local)
    print(f"  tail-only fit (L >= 16, EXCLUDING canonical L=12 test point):")
    print(f"    alpha_tail = {alpha_tail:.6f}   C_FB = {C_FB:.6f}   (alpha = EMPIRICAL spectral-action tail)")
    print(f"  Level-3(s=6, L=12) = relative truncation residual = {level3_rel_L12:.6e}  (substrate-IS distance from continuum)")
    print(f"  Level-2(s=6, L=12) = C_FB·12^-{alpha_tail:.3f}     = {level2_rel_L12:.6e}  (Friedrich-Bar envelope)")
    print(f"  ratio Level-3/Level-2 = {ratio_L3_L2:.6f}   (PASS iff < 1; matches §VII.AV/§VII.AX precedent)")
    # absolute-form cross-check (S94 W3-9 ratio_s6_L12_inside_envelope = 7.6869e-4 is the
    # relative residual at L=12 against the L^-3 envelope -- reproduce for provenance)
    print(f"  [provenance cross-check] s6 rel residual at L=12 (S94 W3-9 ratio_s6_L12_inside_envelope=7.6869e-4): "
          f"{level3_rel_L12:.4e}  (match: {abs(level3_rel_L12-7.6869e-4)<1e-7})")

    # -----------------------------------------------------------------
    # STEP 4 -- Tier-2 fallback: dimensionless functional (residue log-derivative)
    #   d ln Res_s / d ln L -> 0 for a CONVERGENT pole (the multiplicative L-divergent
    #   prefactor is annihilated per math-scripts.md §"Multiplicative-normalization
    #   cancellation invariants"). DIMENSIONLESS => re-anchorable (the §VII.AV pattern).
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 4 -- Tier-2 fallback: dimensionless residue log-derivative d ln Res/d ln L")
    print("=" * 78)
    logderiv_L = L_grid[1:].astype(float)  # (local) centered between successive L
    lnR_s6 = np.log(res_s6)  # (local)
    lnR_s4 = np.log(res_s4)  # (local)
    lnL = np.log(L_grid.astype(float))  # (local)
    logderiv_s6 = np.diff(lnR_s6) / np.diff(lnL)  # (local) d ln Res / d ln L (s=6)
    logderiv_s4 = np.diff(lnR_s4) / np.diff(lnL)  # (local) (s=4; stays > 0 => divergent)
    tier2_s6_final = float(logderiv_s6[-1])  # (local) -> 0 for convergent
    tier2_s4_final = float(logderiv_s4[-1])  # (local) > 0 for divergent
    tier2_dimensionless = True   # (local) a log-derivative is dimensionless by construction
    tier2_converges = bool(abs(tier2_s6_final) < TOL_RATIO)  # (local) |Delta/DeltaL| -> 0
    tier2_reanchorable = bool(tier2_dimensionless and tier2_converges)  # (local) the §VII.AV pattern
    print(f"  s=6 d ln Res/d ln L (L=80->120) = {tier2_s6_final:.6e}  (-> 0 => CONVERGENT, Tier-2-DIMENSIONLESS)")
    print(f"  s=4 d ln Res/d ln L (L=80->120) = {tier2_s4_final:.6e}  (> 0 => DIVERGENT; s=4 NOT re-anchorable)")
    print(f"  Tier-2 dimensionless functional re-anchorable? {tier2_reanchorable}  "
          f"(DIMENSIONLESS log-derivative; the §VII.AV L_emp pattern, NOT §VII.AX n_PBH DIMENSIONFUL)")

    # -----------------------------------------------------------------
    # STEP 5 -- substitution chain + verdict construction ([SIGN] 3-tuple)
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 5 -- substitution chain + verdict ([SIGN]: convergence sign + Level-3<Level-2 direction)")
    print("=" * 78)
    print("  Step 1 (shell scaling): dim_PS ~ L^6 (A_3 = 6 pos roots), ~L^2 sectors/shell")
    print("          => shell exponent of Sigma_L L^6 · L^-2s · L^(2-1) ... = 8-2s (Sage-exact, S94 W3-9).")
    print(f"  Step 2 (convergence): Sigma_L L^(8-2s) converges iff 8-2s < -1 iff s > 9/2 = 4.5.")
    print(f"          s=4 -> exp 0 (DIVERGES); s=5 -> -2 (conv); s=6 -> -4 (conv); s=7 -> -6 (conv).")
    print(f"  Step 3 (s=6 anchor): residue(L->inf) = {res_s6_inf:.8e} (CONFIRMED ~9.39363958e-4),")
    print(f"          truncation tail alpha = {alpha_tail:.3f} (EMPIRICAL spectral-action; NOT HH^1 alpha=8).")
    print(f"  Step 4 (Level-3 < Level-2): ratio = {ratio_L3_L2:.4f} at L=12 ({'< 1 PASS' if ratio_L3_L2 < 1 else 'NOT < 1'}).")
    print(f"  Step 5 (Tier-2 fallback): dimensionless log-deriv -> {tier2_s6_final:.2e} (re-anchorable: {tier2_reanchorable}).")

    # [SIGN] 3-tuple:
    #   sign_verdict: the predicted DIRECTION is (8-2s+1 < 0 at s=6 => residue converges)
    #     AND (Level-3 truncation residual < Level-2 Friedrich-Bar envelope => ratio < 1).
    sign_predicted_convergent = bool((8 - 2 * 6 + 1) < 0)  # (local) shell+1 < 0 at s=6 => finite sum
    sign_predicted_ratio_lt1 = bool(ratio_L3_L2 < 1.0)  # (local)
    sign_verdict = "PASS" if (sign_predicted_convergent and sign_predicted_ratio_lt1) else "FAIL"
    # magnitude_verdict: ratio < 1 (PASS) / borderline [1, info_band] (INFO) / > info_band (FAIL)
    if ratio_L3_L2 < 1.0:
        magnitude_verdict = "PASS"
    elif ratio_L3_L2 <= INFO_BAND:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    # regime_verdict: is s=6 INSIDE the SU(4)_PS convergent regime (s > 4.5)? full window VALID
    regime_verdict = "VALID" if pole_conv[6] else "BREAKDOWN"

    # Composite-collapse (gate-verdicts.md; PRE-REGISTERED)
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

    print("\n" + "=" * 78)
    print("VERDICT CONSTRUCTION")
    print("=" * 78)
    print(f"  sign_verdict      = {sign_verdict}   (convergent s=6 [8-2s+1<0] AND Level-3<Level-2 [ratio<1])")
    print(f"  magnitude_verdict = {magnitude_verdict}   (ratio {ratio_L3_L2:.4f} vs PASS<1 / INFO<={INFO_BAND})")
    print(f"  regime_verdict    = {regime_verdict}   (s=6 INSIDE convergent regime s>4.5; shell exp -4 < -1)")
    print(f"  COMPOSITE         = {verdict}  (per gate-verdicts.md collapse rule)")
    if verdict == "PASS":
        print(f"  => Tier-1 convergent-pole route CLOSES the §VII.BE numerical Level-3 at s=6.")
        print(f"     §VII.BE STAGE-3-PERMANENT review now LICENSED (mack lands registry; structural")
        print(f"     Stage-2 PASS-AND on disk S93 W6-4 UNAFFECTED). Tier-2 dimensionless route also re-anchors.")

    # -----------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------
    d = {
        "L_grid": L_grid, "res_s4": res_s4, "res_s5": res_s5, "res_s6": res_s6, "res_s7": res_s7,
        "res_s6_inf": res_s6_inf, "s6_resid_rel": s6_resid_rel,
        "alpha_tail": alpha_tail, "C_FB": C_FB,
        "level3_rel_L12": level3_rel_L12, "level2_rel_L12": level2_rel_L12, "ratio_L3_L2": ratio_L3_L2,
        "logderiv_L": logderiv_L, "logderiv_s6": logderiv_s6, "logderiv_s4": logderiv_s4,
    }  # (local)
    make_plot(d)
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
    value_str = (  # (local)
        f"VII_BE_Level3_REANCHORED_to_convergent_pole_s6;"
        f"shell_scaling=L^(8-2s)_converges_iff_s_gt_9/2;"
        f"s4_DIVERGES_ratio_{res_s4[-1]/res_s4[0]:.2f}x_SETTLED_S94W3_9;"
        f"s5_conv_exp-2_s6_conv_exp-4_s7_conv_exp-6;"
        f"residue_s6_Linf={res_s6_inf:.8e}_CONFIRMED_target_9.39363958e-4_delta={delta_target:.2e};"
        f"tail_alpha_fullgrid={alpha_full:.6f}_tailonly_L_ge16={alpha_tail:.6f}_EMPIRICAL_NOT_HH1_alpha8;"
        f"Tier1_Level3_relresid_L12={level3_rel_L12:.6e}_lt_Level2_env_C_FB_{C_FB:.4f}_L12^-{alpha_tail:.3f}={level2_rel_L12:.6e};"
        f"ratio_L3_L2={ratio_L3_L2:.6f}_{'lt_1_PASS' if ratio_L3_L2 < 1 else 'NOT_lt_1'};"
        f"Tier2_dimensionless_logderiv_s6={tier2_s6_final:.4e}_to_0_reanchorable={tier2_reanchorable}_VII_AV_pattern;"
        f"Tier2_s4_logderiv={tier2_s4_final:.4e}_gt_0_divergent;"
        f"L_max={L_MAX};"
        f"struct_Stage2_PASS_AND_on_disk_S93W6_4_axisA_{S93_W6_4_AXIS_A_SHA}_axisB_{S93_W6_4_AXIS_B_SHA}_UNAFFECTED;"
        f"VII_BE_STAGE3_review_licensed_on_PASS;mack_lands_registry"
    )
    append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict)
    print(f"\n  verdict line appended -> {VERDICT_FILE}")

    # -----------------------------------------------------------------
    # npz
    # -----------------------------------------------------------------
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        # Casimir ladder self-check
        casimir_ladder_matches_plan=ladder_ok,
        casimir_conjugation_symmetric=conj_ok,
        # pole-scan + residues
        L_grid=L_grid,
        residue_s4=res_s4, residue_s5=res_s5, residue_s6=res_s6, residue_s7=res_s7,
        shell_scaling_exponent="8-2s",
        s_conv_threshold=float(s_conv_threshold),
        pole_conv_s4=pole_conv[4], pole_conv_s5=pole_conv[5],
        pole_conv_s6=pole_conv[6], pole_conv_s7=pole_conv[7],
        s4_diverges=s4_diverges,
        # s=6 confirmed anchor
        residue_s6_Linf=res_s6_inf,
        residue_s6_Linf_mp=res_s6_inf_mp,
        residue_s6_target=RESIDUE_S6_TARGET,
        residue_s6_target_delta=delta_target,
        s6_resid_rel=s6_resid_rel,
        alpha_s6_tail_fullgrid=alpha_full,
        alpha_s6_observed_S94=ALPHA_S6_OBSERVED,
        alpha_HH1_s6_NOT_used=float(alpha_HH1_per_pole_FW_s6),
        # Tier-1 Level-3 < Level-2
        alpha_tail_L_ge_16=alpha_tail,
        C_FB_tail=C_FB,
        level3_rel_L12=level3_rel_L12,
        level2_rel_L12=level2_rel_L12,
        ratio_L3_L2=ratio_L3_L2,
        tier1_pass=bool(ratio_L3_L2 < 1.0),
        # Tier-2 dimensionless fallback
        logderiv_L=logderiv_L, logderiv_s6=logderiv_s6, logderiv_s4=logderiv_s4,
        tier2_s6_final=tier2_s6_final, tier2_s4_final=tier2_s4_final,
        tier2_dimensionless=tier2_dimensionless,
        tier2_converges=tier2_converges,
        tier2_reanchorable=tier2_reanchorable,
        # bridge / registry
        vii_be_stage3_review_licensed=bool(verdict == "PASS"),
        struct_stage2_pass_and_on_disk=True,
        s93_w6_4_axis_a_sha=S93_W6_4_AXIS_A_SHA,
        s93_w6_4_axis_b_sha=S93_W6_4_AXIS_B_SHA,
        s94_w3_9_fail_sha=S94_W3_9_FAIL_SHA,
        # provenance
        tau_fold=tau_fold, M_KK=M_KK, M_Pl_reduced=M_Pl_reduced,
        regulator_pin="a_n^{Mellin}",
        element3_bridge_map="Wodzicki-HKR-composite-Bismut-Cheeger-adiabatic-limit",
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  npz -> {NPZ_PATH.name}")

    wall = time.time() - t0  # (local)
    print("\n" + "=" * 78)
    print(f"4-tuple: (value={verdict}_s6_reanchor_ratio_{ratio_L3_L2:.4f}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"  composite={verdict} (sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict})")
    print(f"  wall: {wall:.2f}s")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
