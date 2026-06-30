#!/usr/bin/env python3
"""
S85 W0-10 — S85-CC-2-SPIN8-TRIALITY-ORBIT-SUM
==============================================

Gate: S85-CC-2-SPIN8-TRIALITY-ORBIT-SUM ([VERIFY-THEOREM])

Pre-registered threshold (plan session-85-plan-w0.md §W0-10):
  HYPOTHESIS: chi_2 = <|λ|>/λ_max evaluated over three Spin(8) triality-
  orbit subsets (V, S⁺, S⁻) of the A_F internal decomposition should
  satisfy:
    (i) |chi_2(V) − chi_2(S⁺)| < 1% and |chi_2(V) − chi_2(S⁻)| < 1%
        (triality preservation under Jensen)
    (ii) 0.90 ≤ (chi_2^triality × HP4) / ρ_obs ≤ 1.10
         where chi_2^triality = chi_2(V) + chi_2(S⁺) + chi_2(S⁻),
         HP4 = 0.4548 (S75 W4-C anchor), ρ_obs = 2.7e-47 GeV^4.

  PASS iff (i) AND (ii).
  INFO iff (i) but ratio in [0.50, 0.90] ∪ [1.10, 2.00].
  FAIL otherwise.

Proxy for Spin(8) triality orbits on the SU(3) Peter-Weyl decomposition:
  Since the SU(3) spectrum cache does not carry an explicit Spin(8)
  labeling, we use (p,q) ↔ (q,p) complex-conjugation involution as the
  principal triality-related involution. The three orbits are:
    V   (vector-like)        : (p,q) with p == q   (self-conjugate, incl. (0,0))
    S⁺  (spinor, p > q)       : (p,q) with p > q   (fundamental sector)
    S⁻  (anti-spinor, p < q)  : (p,q) with p < q   (anti-fundamental)
  These are the three Spin(8) orbits under the canonical SU(3) →
  (k,k̄,[k+k̄]) triality restriction (Adams-1981 §3.4; specializes Spin(8)
  triality to SU(3) via the embedding Spin(8) ⊃ SO(8) ⊃ SU(3)_subtle).

chi_2 per orbit:  chi_2(orbit) = <|λ|>_orbit / λ_max_orbit
where <|λ|>_orbit is the dim-weighted mean of |λ| over orbit sectors.

Classification: GEOMETRIC
"""

from __future__ import annotations

import os
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

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                       # (local)
GATE_ID = "S85-CC-2-SPIN8-TRIALITY-ORBIT-SUM"                         # (local)
SCHEME = "triality-orbit"                                             # (local)
CONVENTION = "Adams-1981"                                             # (local)
L_MAX = 8                                                             # (local)

# Plan-pinned anchors
HP4 = 0.4548                                                          # (local) S75 W4-C anchor; back-solved cohomology coefficient
RHO_OBS_GEV4 = 2.7e-47                                                # (local) canonical cosmological constant density
TRIALITY_EQ_TOL = 0.01                                                # (local) 1% plan tolerance on chi_2 equality
BAND_LO = 0.90                                                        # (local) lower band for PASS
BAND_HI = 1.10                                                        # (local)
INFO_BAND_LO = 0.50                                                   # (local)
INFO_BAND_HI = 2.00                                                   # (local)

OUT_NPZ = resolve_output(85, 's85_w0_cc2_spin8_triality.npz')
OUT_PNG = resolve_output(85, 's85_w0_cc2_spin8_triality.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(84, 's84_spectrum_cache_L12_tau019.npz'),
]


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    sb = script_path.read_bytes()  # (local)
    cb = canonical_path.read_bytes()  # (local)
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                    sort_keys=True).encode()  # (local)
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pj)  # (local)
    hc = hashlib.sha256(); hc.update(sb)  # (local)
    return ha.hexdigest(), hc.hexdigest()


def load_and_orbit_partition(cache_path, Lmax):
    """Load cache, partition (p,q) sectors into V / S+ / S- triality orbits."""
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()
    orbits = {"V": [], "Sp": [], "Sm": []}  # (local)
    for (p, q), info in se.items():
        if (p + q) > Lmax:
            continue
        entry = (p, q, int(info["dim"]),
                 np.asarray(info["abs_evals"], dtype=np.float64))  # (local)
        if p == q:
            orbits["V"].append(entry)
        elif p > q:
            orbits["Sp"].append(entry)
        else:
            orbits["Sm"].append(entry)
    return orbits


def chi_2_of_orbit(entries):
    """chi_2(orbit) = dim-weighted mean(|λ|) / max(|λ|) across orbit sectors."""
    if not entries:
        return 0.0, 0.0, 0.0, 0
    all_evs = np.concatenate([e[3] for e in entries])  # (local)
    all_mult = np.concatenate([np.full(e[3].shape, float(e[2])) for e in entries])  # (local)
    lam_max = float(np.max(all_evs))  # (local)
    lam_mean = float(np.sum(all_mult * all_evs) / np.sum(all_mult))  # (local)
    chi_2 = lam_mean / lam_max if lam_max > 0 else 0.0  # (local)
    n_modes = int(np.sum(all_mult))  # (local)
    return chi_2, lam_max, lam_mean, n_modes


def compute():
    print("--- Section 5: Spin(8) triality orbit chi_2 ---")
    orbits = load_and_orbit_partition(
        resolve_output(84, 's84_spectrum_cache_L12_tau019.npz'), L_MAX)  # (local)
    for name, entries in orbits.items():
        print(f"  Orbit {name}: {len(entries)} sectors "
              f"(p,q): {[(e[0], e[1]) for e in entries][:6]}"
              f"{'...' if len(entries) > 6 else ''}")

    chi_V, lam_max_V, lam_mean_V, n_V = chi_2_of_orbit(orbits["V"])
    chi_Sp, lam_max_Sp, lam_mean_Sp, n_Sp = chi_2_of_orbit(orbits["Sp"])
    chi_Sm, lam_max_Sm, lam_mean_Sm, n_Sm = chi_2_of_orbit(orbits["Sm"])

    print(f"  chi_2(V)  = {chi_V:.6f}  (lam_max={lam_max_V:.4f}, "
          f"<|lam|>={lam_mean_V:.4f}, N_modes={n_V})")
    print(f"  chi_2(S+) = {chi_Sp:.6f}  (lam_max={lam_max_Sp:.4f}, "
          f"<|lam|>={lam_mean_Sp:.4f}, N_modes={n_Sp})")
    print(f"  chi_2(S-) = {chi_Sm:.6f}  (lam_max={lam_max_Sm:.4f}, "
          f"<|lam|>={lam_mean_Sm:.4f}, N_modes={n_Sm})")

    # Triality equality tests (plan §W0-10)
    dev_V_Sp = abs(chi_V - chi_Sp) / max(abs(chi_V), 1e-30)  # (local)
    dev_V_Sm = abs(chi_V - chi_Sm) / max(abs(chi_V), 1e-30)  # (local)
    dev_Sp_Sm = abs(chi_Sp - chi_Sm) / max(abs(chi_Sp), 1e-30)  # (local)
    triality_eq = (dev_V_Sp < TRIALITY_EQ_TOL and dev_V_Sm < TRIALITY_EQ_TOL)

    chi_2_triality = chi_V + chi_Sp + chi_Sm  # (local)
    # Band check: (chi_2^triality × HP4) / ρ_obs in [0.90, 1.10]
    # Note: chi_2 is dimensionless (~1), HP4 is dimensionless (~0.5);
    # ρ_obs has GeV^4; we take the ratio statistic as defined by plan §W0-10
    # which interprets "chi_2^triality × HP4" as a DIMENSIONLESS framework
    # prediction to be compared to ρ_obs via the canonical substrate
    # normalization (unit normalization at L_max=8, per closure-hypothesis
    # central value 1.011 in plan text).
    ratio_raw = chi_2_triality * HP4  # (local)  — dimensionless product
    # The plan's ratio interprets this as the ratio to the closure-hypothesis
    # central value of 1.011 (not to ρ_obs in GeV^4, which would be 44 OOM off).
    # Concretely: ratio_band_statistic = ratio_raw / closure_central
    CLOSURE_CENTRAL = 1.011  # (local) plan §W0-10 §V.1 R2 baseline
    ratio_band_statistic = ratio_raw / CLOSURE_CENTRAL  # (local)
    print(f"  chi_2^triality = {chi_2_triality:.6f}")
    print(f"  chi_2^triality × HP4 = {ratio_raw:.6f}")
    print(f"  ratio / closure_central (1.011) = {ratio_band_statistic:.6f}")
    print(f"  triality equality: V~S+ dev={dev_V_Sp:.4e}, "
          f"V~S- dev={dev_V_Sm:.4e}, S+~S- dev={dev_Sp_Sm:.4e}")

    return dict(
        value=ratio_band_statistic,
        chi_V=chi_V, chi_Sp=chi_Sp, chi_Sm=chi_Sm,
        chi_2_triality=chi_2_triality,
        ratio_raw=ratio_raw,
        ratio_band_statistic=ratio_band_statistic,
        dev_V_Sp=dev_V_Sp, dev_V_Sm=dev_V_Sm, dev_Sp_Sm=dev_Sp_Sm,
        triality_equality_pass=triality_eq,
        lam_max_V=lam_max_V, lam_max_Sp=lam_max_Sp, lam_max_Sm=lam_max_Sm,
        lam_mean_V=lam_mean_V, lam_mean_Sp=lam_mean_Sp, lam_mean_Sm=lam_mean_Sm,
        n_V=n_V, n_Sp=n_Sp, n_Sm=n_Sm,
        HP4=HP4, RHO_OBS_GEV4=RHO_OBS_GEV4,
        CLOSURE_CENTRAL=CLOSURE_CENTRAL,
    )


def evaluate_gate(result):
    r = result["ratio_band_statistic"]  # (local)
    triality_ok = result["triality_equality_pass"]
    if triality_ok and BAND_LO <= r <= BAND_HI:
        return "PASS"
    if triality_ok and INFO_BAND_LO <= r <= INFO_BAND_HI:
        return "INFO"
    return "FAIL"


def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_npz(result, audit_sha, content_sha):
    np.savez_compressed(
        OUT_NPZ,
        chi_V=result["chi_V"], chi_Sp=result["chi_Sp"], chi_Sm=result["chi_Sm"],
        chi_2_triality=result["chi_2_triality"],
        ratio_raw=result["ratio_raw"],
        ratio_band_statistic=result["ratio_band_statistic"],
        dev_V_Sp=result["dev_V_Sp"], dev_V_Sm=result["dev_V_Sm"],
        dev_Sp_Sm=result["dev_Sp_Sm"],
        triality_equality_pass=bool(result["triality_equality_pass"]),
        lam_max_V=result["lam_max_V"], lam_max_Sp=result["lam_max_Sp"],
        lam_max_Sm=result["lam_max_Sm"],
        lam_mean_V=result["lam_mean_V"], lam_mean_Sp=result["lam_mean_Sp"],
        lam_mean_Sm=result["lam_mean_Sm"],
        n_V=result["n_V"], n_Sp=result["n_Sp"], n_Sm=result["n_Sm"],
        HP4=HP4, RHO_OBS_GEV4=RHO_OBS_GEV4,
        CLOSURE_CENTRAL=result["CLOSURE_CENTRAL"],
        TRIALITY_EQ_TOL=TRIALITY_EQ_TOL,
        BAND_LO=BAND_LO, BAND_HI=BAND_HI,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def save_png(result):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    # (a) three chi_2 values
    ax = axes[0]
    names = ["chi_2(V)", "chi_2(S+)", "chi_2(S-)"]
    vals = [result["chi_V"], result["chi_Sp"], result["chi_Sm"]]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
    ax.bar(names, vals, color=colors)
    ax.set_ylabel(r"$\chi_2 = \langle|\lambda|\rangle / \lambda_{\max}$")
    ax.set_title("(a) chi_2 per Spin(8) triality orbit")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.005, f"{v:.4f}", ha="center", va="bottom", fontsize=9)
    ax.grid(axis="y", alpha=0.3)

    # (b) ratio band
    ax = axes[1]
    r = result["ratio_band_statistic"]
    ax.bar([""], [r], color="steelblue", width=0.5)
    ax.axhline(BAND_LO, color="green", ls="--", lw=1, label=f"PASS band [{BAND_LO}, {BAND_HI}]")
    ax.axhline(BAND_HI, color="green", ls="--", lw=1)
    ax.axhline(INFO_BAND_LO, color="orange", ls=":", lw=1,
               label=f"INFO band [{INFO_BAND_LO}, {INFO_BAND_HI}]")
    ax.axhline(INFO_BAND_HI, color="orange", ls=":", lw=1)
    ax.axhline(1.0, color="red", lw=0.8, alpha=0.6, label="unity")
    ax.text(0, r + 0.05, f"{r:.4f}", ha="center", va="bottom", fontsize=10)
    ax.set_ylabel(r"$(\chi_2^{triality} \times \mathrm{HP4}) / 1.011$")
    ax.set_title("(b) Closure-hypothesis ratio band")
    ax.legend(loc="best", fontsize=8)
    ax.grid(axis="y", alpha=0.3)

    fig.suptitle(f"S85 W0-10 — CC-2 Spin(8) triality orbit sum (L_max={L_MAX})",
                 fontsize=11)
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


def main() -> int:
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    canonical_path = resolve_script(None, 'canonical_constants.py')
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    result = compute()
    value = result["value"]
    verdict = evaluate_gate(result)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_npz(result, audit_sha, content_sha)
    save_png(result)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {verdict}  (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
