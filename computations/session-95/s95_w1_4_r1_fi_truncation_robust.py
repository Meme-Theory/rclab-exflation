#!/usr/bin/env python3
"""
S95 W1-4 — TES-R1-FI-TRUNCATION-ROBUST
======================================

Gate: TES-R1-FI-TRUNCATION-ROBUST  ([SIGN])
Classification: GEOMETRIC

Pre-registered threshold (session-95-plan-w1.md §W1-4):
  R_1 = a_0 a_4 / a_2^2 is claimed FUNCTIONAL-INVARIANT (FI) under truncation.
  PASS iff:
    (i)   |R_1(L_max) - 1.128655| is MONOTONE-DECREASING over L_max in {6,8,10,12}
    (ii)  |R_1(12) - 1.128655| / 1.128655 < 0.01  (1% band; tesla V.5 FAIL ceiling)
    (iii) each individual a_n^raw(L) strictly INCREASES with L_max (moments diverge)
  FAIL iff R_1(12) drifts > 1% from 1.128655 OR the |R_1(L)-c| sequence is non-monotone.
  INFO iff |R_1(L)-c| monotone-decreasing but in [0.01, info_band] at L_max=12.

Substitution chain (plan §W1-4 (7)):
  R_1(L) = a_0^raw(L) a_4^raw(L) / (a_2^raw(L))^2.
  If a_n^raw(L) = w(L) g_n [1 + b_n L^{-1} + O(L^{-2})] with w(L) the common
  L-divergent spectral-support weight, then
    R_1(L) = (g_0 g_4 / g_2^2) [1 + (b_0 + b_4 - 2 b_2) L^{-1} + O(L^{-2})],
  i.e. w(L) cancels EXACTLY (two factors up, two down) — the
  multiplicative-normalization-cancellation invariant (math-scripts.md, K=3).
  CLAIM: moments INCREASE while |R_1(L)-c| DECREASES (opposite directions = FI signature).

RAW MODE-COUNT MOMENT DEFINITION (recovered from S66 s66_cutoff_ns.py:512-521,
the producing script for the tesla V.5 §8.2 triple a0=155984, a2=64308.24,
a4=29086.18 stored in s66_cutoff_ns.npz a0_computed/a2_computed/a4_computed):
    a_0^raw = Sum_{(p,q): p+q<=L}  d(p,q)^2 * N_modes(p,q)        # mode count, PW-weighted
    a_2^raw = Sum_{(p,q): p+q<=L}  d(p,q)^2 * Sum_j |lambda_j|^{-2}
    a_4^raw = Sum_{(p,q): p+q<=L}  d(p,q)^2 * Sum_j |lambda_j|^{-4}
  d(p,q) = dim_su3_irrep(p,q) Peter-Weyl irrep dimension; |lambda_j| are the
  per-sector abs_evals from the L12 D_K spectrum cache at tau_fold.
  CONVENTION NOTE: the tesla "L_max=10" anchor reproduces EXACTLY at the PW
  truncation p+q<=3 (NOT p+q<=10) under this d^2 weighting — confirmed
  bit-for-bit (a0=155984.0, a2=64308.2438882544, a4=29086.17667962735).
  The s66 script used MAX_PQ_SUM=3; the legacy "155,984-eigenvalue / L=10"
  corpus label is the d^2-weighted mode count at p+q<=3, NOT a p+q<=10 count.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
  - computations/_shared/canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<R_1(L_max=12) raw>, scheme=raw-mode-count-Seeley-DeWitt-moments,
   convention=FI-RATIO-truncation-robust, L_max=12)

DISCIPLINE: `from canonical_constants import *`; every intermediate `# (local)`;
CPU-cap-OMP8 (moment sums on cached spectrum, no dense eig); dual-SHA emitted;
[SIGN] trigger -> schema-v2 3-tuple companion row appended.

REGULATOR-PIN (regulator-pin-discipline.md): a_n^{raw-mode-count} for the
truncation-scan moments; a_n^{zeta} for the SDW canonical comparison. The FI
result is tagged FI per regulator-pin-discipline.md §"beta_shell FI Classification"
inheritance (F_traj a_2-ratio FI theorem parent).
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Paths + canonical imports
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_95_DIR = PROJECT_ROOT / "computations" / "session-95"
SRC_DIR = PROJECT_ROOT / "phonon-exflation-sim" / "src"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(SRC_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    R_protected_fold,
    Lizzi_signature,
    a_0_FW_zeta,
    a_2_FW_zeta,
    a_4_FW_zeta,
)
from spectral_action import dim_su3_irrep  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins
# ---------------------------------------------------------------------------
GATE_ID = "TES-R1-FI-TRUNCATION-ROBUST"
SCHEME = "raw-mode-count-Seeley-DeWitt-moments"
CONVENTION = "FI-RATIO-truncation-robust"
L_MAX = 12                         # (local) gate L_max pin (plan §W1-4 machinery)

L_GRID = [6, 8, 10, 12]            # (local) pre-registered truncation scan (plan §W1-4)
TESLA_PQ = 3                       # (local) PW truncation reproducing the tesla §8.2 anchor
PASS_BAND = 0.01                   # (local) 1% gate band (tesla V.5 FAIL ceiling)
INFO_BAND = 0.05                   # (local) monotone-but-not-1% INFO band

CANONICAL_R1 = float(R_protected_fold)            # 1.1286545967627695
TESLA_A0, TESLA_A2, TESLA_A4 = 155984.0, 64308.2438882544, 29086.17667962735

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
L12_CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
INPUT_FILES = [L12_CACHE_PATH, CANONICAL_CONSTANTS_PATH]

VERDICT_TXT = SESSION_95_DIR / "s95_gate_verdicts.txt"
OUT_NPZ = SESSION_95_DIR / "s95_w1_4_r1_fi_truncation_robust.npz"
OUT_PNG = SESSION_95_DIR / "s95_w1_4_r1_fi_truncation_robust.png"

# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors .claude/templates/script-template.py)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write canonical line + dual-SHA companion + (since [SIGN]) 3-tuple row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    SESSION_95_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def append_3tuple_row(sign_v: str, mag_v: str, regime_v: str) -> None:
    """schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row ([SIGN] trigger; gate-verdicts.md)."""
    row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# Raw mode-count Seeley-DeWitt moments (S66 s66_cutoff_ns.py:512-521 definition)
# ---------------------------------------------------------------------------
def raw_moments(sector_evals: dict, pq_cut: int):
    """a_n^raw = Sum_{p+q<=pq_cut} d(p,q)^2 * Sum_j |lambda_j|^{-2n}, n=0,2,4.

    n=0 term is the PW-weighted mode count Sum d^2 * N_modes.
    Returns (a0, a2, a4) as float64.
    """
    a0 = 0.0  # (local)
    a2 = 0.0  # (local)
    a4 = 0.0  # (local)
    for (p, q), v in sector_evals.items():
        level = v["level"]  # (local) = p+q
        if level > pq_cut:
            continue
        d_pq = dim_su3_irrep(p, q)  # (local) Peter-Weyl irrep dimension
        om = np.asarray(v["abs_evals"], dtype=float)  # (local)
        om = om[om > 1e-12]  # (local) drop numerical zero-modes (matches S66)
        a0 += d_pq ** 2 * len(om)
        a2 += d_pq ** 2 * np.sum(om ** -2)
        a4 += d_pq ** 2 * np.sum(om ** -4)
    return a0, a2, a4


def compute() -> dict:
    cache = np.load(L12_CACHE_PATH, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local) dict keyed by (p,q)

    # --- Cross-check 1: reproduce the tesla V.5 §8.2 anchor at p+q<=3 ---
    a0_t, a2_t, a4_t = raw_moments(sector_evals, TESLA_PQ)  # (local)
    tesla_match = (
        abs(a0_t - TESLA_A0) < 1.0
        and abs(a2_t - TESLA_A2) < 1e-3
        and abs(a4_t - TESLA_A4) < 1e-3
    )  # (local)
    R1_tesla = a0_t * a4_t / a2_t ** 2  # (local) = 1.097068 (tesla anchor ratio)

    # --- Cross-check 2: SDW-zeta canonical triple reproduces R_protected_fold ---
    R1_sdw = a_0_FW_zeta * a_4_FW_zeta / a_2_FW_zeta ** 2  # (local)

    # --- Main scan: raw R_1(L) over the pre-registered grid {6,8,10,12} ---
    a0_arr, a2_arr, a4_arr, R1_arr, dev_arr = [], [], [], [], []  # (local)
    for L in L_GRID:
        a0, a2, a4 = raw_moments(sector_evals, L)  # (local)
        r1 = a0 * a4 / a2 ** 2  # (local)
        a0_arr.append(a0); a2_arr.append(a2); a4_arr.append(a4)
        R1_arr.append(r1); dev_arr.append(abs(r1 - CANONICAL_R1))

    a0_arr = np.array(a0_arr); a2_arr = np.array(a2_arr); a4_arr = np.array(a4_arr)
    R1_arr = np.array(R1_arr); dev_arr = np.array(dev_arr)

    # --- Directional predicates (substitution-chain Step 5) ---
    # (i) deviation monotone-decreasing toward canonical
    dev_deltas = np.diff(dev_arr)  # (local)
    dev_monotone_decreasing = bool(np.all(dev_deltas < 0))  # (local)
    # (ii) within 1% at L_max=12
    rel_dev_12 = dev_arr[-1] / CANONICAL_R1  # (local)
    within_1pct = bool(rel_dev_12 < PASS_BAND)  # (local)
    # (iii) each moment strictly increasing (divergence)
    a0_increasing = bool(np.all(np.diff(a0_arr) > 0))  # (local)
    a2_increasing = bool(np.all(np.diff(a2_arr) > 0))  # (local)
    a4_increasing = bool(np.all(np.diff(a4_arr) > 0))  # (local)
    moments_diverge = a0_increasing and a2_increasing and a4_increasing  # (local)

    return {
        "value": float(R1_arr[-1]),                 # R_1(L_max=12) raw
        "R1_arr": R1_arr,
        "dev_arr": dev_arr,
        "dev_deltas": dev_deltas,
        "a0_arr": a0_arr, "a2_arr": a2_arr, "a4_arr": a4_arr,
        "rel_dev_12": float(rel_dev_12),
        "dev_monotone_decreasing": dev_monotone_decreasing,
        "within_1pct": within_1pct,
        "moments_diverge": moments_diverge,
        "a0_increasing": a0_increasing,
        "a2_increasing": a2_increasing,
        "a4_increasing": a4_increasing,
        "R1_tesla": float(R1_tesla),
        "tesla_a0": a0_t, "tesla_a2": a2_t, "tesla_a4": a4_t,
        "tesla_match": tesla_match,
        "R1_sdw": float(R1_sdw),
    }


# ---------------------------------------------------------------------------
# Gate evaluation (pre-registered; no post-hoc edits)
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict):
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    PASS_meaning (plan): |R_1(L)-c| monotone-decreasing over {6,8,10,12},
    within 1% at L=12, while each a_n^raw individually diverges.
    """
    mono = res["dev_monotone_decreasing"]  # (local)
    within = res["within_1pct"]            # (local)
    diverge = res["moments_diverge"]       # (local)
    rel12 = res["rel_dev_12"]              # (local)

    # SIGN verdict: substitution-chain Step 5 predicts moments-UP / ratio-deviation-DOWN
    # (opposite directions). sign PASS iff BOTH directions hold as predicted.
    sign_v = "PASS" if (diverge and mono) else "FAIL"  # (local)

    # MAGNITUDE verdict: |R_1(12)-c|/c vs the 1% / 5% bands
    if rel12 < PASS_BAND:
        mag_v = "PASS"  # (local)
    elif rel12 <= INFO_BAND:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"

    # REGIME verdict: the moment-divergence direction (the regime-of-validity
    # half of the FI signature) IS confirmed across the full window -> VALID;
    # the convergence half failing is a magnitude/sign matter, not a regime breach.
    regime_v = "VALID" if diverge else "BREAKDOWN"  # (local)

    # Composite-collapse rule (gate-verdicts.md; PRE-REGISTERED):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: R_1(L_max) vs L_max with canonical asymptote + tesla anchor
    ax = axes[0]
    ax.plot(L_GRID, res["R1_arr"], "o-", color="C0", lw=2, label=r"$R_1^{\rm raw}(L_{\max})$")
    ax.axhline(CANONICAL_R1, color="C3", ls="--", lw=2,
               label=rf"canonical $R_1={CANONICAL_R1:.6f}$ (SDW-$\zeta$)")
    ax.axhline(res["R1_sdw"], color="C2", ls=":", lw=1.5,
               label=rf"SDW-$\zeta$ triple $={res['R1_sdw']:.6f}$")
    ax.plot([TESLA_PQ], [res["R1_tesla"]], "s", color="C1", ms=10,
            label=rf"tesla anchor (p+q<=3) = {res['R1_tesla']:.6f}")
    ax.set_xlabel(r"$L_{\max}$ (PW truncation $p+q$)")
    ax.set_ylabel(r"$R_1 = a_0 a_4 / a_2^2$")
    ax.set_title("Raw mode-count $R_1$ vs truncation\n(does NOT converge to SDW-$\\zeta$ canonical)")
    ax.legend(fontsize=7, loc="best")
    ax.grid(alpha=0.3)

    # Panel 2: |R_1(L)-c| deviation (the FI convergence claim)
    ax = axes[1]
    ax.plot(L_GRID, res["dev_arr"] / CANONICAL_R1 * 100, "o-", color="C0", lw=2)
    ax.axhline(PASS_BAND * 100, color="C3", ls="--", lw=1.5, label="1% PASS band")
    ax.set_xlabel(r"$L_{\max}$")
    ax.set_ylabel(r"$|R_1(L)-c|/c$ (%)")
    mono_txt = "monotone-down" if res["dev_monotone_decreasing"] else "NOT monotone-down (GROWS)"  # (local)
    ax.set_title(f"Ratio-deviation vs $L_{{\\max}}$\n({mono_txt})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 3: individual a_n^raw(L) divergence (log scale)
    ax = axes[2]
    ax.semilogy(L_GRID, res["a0_arr"], "o-", label=r"$a_0^{\rm raw}$")
    ax.semilogy(L_GRID, res["a2_arr"], "s-", label=r"$a_2^{\rm raw}$")
    ax.semilogy(L_GRID, res["a4_arr"], "^-", label=r"$a_4^{\rm raw}$")
    ax.set_xlabel(r"$L_{\max}$")
    ax.set_ylabel(r"$a_n^{\rm raw}(L_{\max})$ (log)")
    ax.set_title("Individual moments DIVERGE with $L_{\\max}$\n(monotone increasing)")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, which="both")

    fig.suptitle(
        f"{GATE_ID}: R_1 truncation-robustness — raw mode-count moments "
        f"(scheme={SCHEME})", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    print("=== Cross-checks ===")
    print(f"  tesla anchor reproduce (p+q<=3): a0={res['tesla_a0']:.1f} "
          f"a2={res['tesla_a2']:.10f} a4={res['tesla_a4']:.11f}")
    print(f"    tesla triple (155984, 64308.2438882544, 29086.17667962735) match: {res['tesla_match']}")
    print(f"    R_1^raw(tesla, p+q<=3) = {res['R1_tesla']:.6f}  (plan target 1.09707)")
    print(f"  SDW-zeta R_1 = {res['R1_sdw']:.10f}  (canonical R_protected_fold = {CANONICAL_R1:.10f})")
    print(f"  Lizzi_signature = {float(Lizzi_signature):.10f}")
    print()

    print("=== Raw R_1(L_max) scan over {6,8,10,12} ===")
    for i, L in enumerate(L_GRID):
        print(f"  L={L:2d}: a0={res['a0_arr'][i]:.4e} a2={res['a2_arr'][i]:.4e} "
              f"a4={res['a4_arr'][i]:.4e} | R1={res['R1_arr'][i]:.6f} | "
              f"|R1-c|/c={res['dev_arr'][i]/CANONICAL_R1*100:.3f}%")
    print()
    print(f"  (i)   deviation monotone-DECREASING: {res['dev_monotone_decreasing']}  "
          f"(deltas: {[f'{x:+.6f}' for x in res['dev_deltas']]})")
    print(f"  (ii)  |R1(12)-c|/c = {res['rel_dev_12']*100:.3f}%  -> within 1%? {res['within_1pct']}")
    print(f"  (iii) moments diverge (each a_n increasing): {res['moments_diverge']}  "
          f"(a0 {res['a0_increasing']}, a2 {res['a2_increasing']}, a4 {res['a4_increasing']})")
    print()

    composite, sign_v, mag_v, regime_v = evaluate_gate(res)

    make_plot(res)
    print(f"plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")

    np.savez(
        OUT_NPZ,
        L_grid=np.array(L_GRID),
        R1_raw=res["R1_arr"],
        dev=res["dev_arr"],
        dev_deltas=res["dev_deltas"],
        a0_raw=res["a0_arr"], a2_raw=res["a2_arr"], a4_raw=res["a4_arr"],
        rel_dev_12=res["rel_dev_12"],
        dev_monotone_decreasing=res["dev_monotone_decreasing"],
        within_1pct=res["within_1pct"],
        moments_diverge=res["moments_diverge"],
        a0_increasing=res["a0_increasing"],
        a2_increasing=res["a2_increasing"],
        a4_increasing=res["a4_increasing"],
        R1_tesla=res["R1_tesla"],
        tesla_a0=res["tesla_a0"], tesla_a2=res["tesla_a2"], tesla_a4=res["tesla_a4"],
        tesla_match=res["tesla_match"],
        R1_sdw=res["R1_sdw"],
        canonical_R1=CANONICAL_R1,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=composite,
    )
    print(f"data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    tup = (f"(value={res['value']!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(f"\n4-tuple: {tup}")

    append_verdict(composite, res["value"], audit_sha, content_sha)
    append_3tuple_row(sign_v, mag_v, regime_v)

    print(f"\nGATE VERDICT: {composite}  "
          f"(sign={sign_v}, magnitude={mag_v}, regime={regime_v})")
    print(f"elapsed {time.time()-t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
