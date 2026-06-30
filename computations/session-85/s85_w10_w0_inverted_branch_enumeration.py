#!/usr/bin/env python3
"""
S85 W10-4 — S85-W10-W0-L-INVERTED-BRANCH-ENUMERATION ([VERIFY])
================================================================

Enumerate 4 branches × 3 L_max in the Josephson-dominant inverted
regime and test whether any inverted branch produces a stable w_0 with
Cauchy-monotone decaying Mellin-cone residues.

PLAN CONTEXT
------------
S84-W1a-3 SV2 recorded R_JE drift 0.45 → 4.99 over L ∈ {5, 6, 7, 8}.
Baseline branches (a, b) are Bogoliubov-dominant (R_JE < 1, only
applicable at low L where ξ_E_GGE > ξ_J). Target inverted branches
(c, d) are Josephson-dominant (R_JE > 1, applicable at L >= 6 per the
SV2 axis).

The plan's pre-registration expects L_max ∈ {8, 10, 12}. L = 10, 12
dense D_K diagonalization at matrix dim ~1e7 × 1e7 is INFEASIBLE on
the 17 GB GPU (storage would be ~8 PB). Therefore L = 10, 12 values
are obtained by log-linear EXTRAPOLATION from the SV2 L = {5, 6, 7, 8}
trajectory — honest extrapolation with the fit diagnostics reported.

COMPUTATIONAL MODEL (definitional, documented)
-----------------------------------------------
For each branch (b) in {a, b, c, d} at each L_max:

  * xi_E_GGE(L) : loaded from SV2 for L <= 8; log-linear extrapolated
                  to L = 10, 12.
  * mellin_s3(L): loaded from SV2 for L <= 8; log-linear extrapolated.
  * S_zeta_E(L), S_Zubarev_E(L): loaded from SV2 for L <= 8;
                  log-linear extrapolated.
  * xi_J : 0.008911 (TB-pinned, L-independent; from SV2 anchor).

  w_0 per branch per L (definitional model):
    w_0(branch, L) = -1 + 2 * xi_effective(branch, L) * mellin_s3(L)
                              / denom_regulator(branch, L)
    where xi_effective = xi_E_GGE(L) for Bogoliubov-dominant (a, b),
                       = xi_J         for Josephson-dominant (c, d),
          denom_regulator = S_zeta_E(L)    for ζ-regulator (a, c),
                          = S_Zubarev_E(L) for Zubarev-regulator (b, d).

  Branch-specific Mellin residue:
    residue(branch, L) = xi_effective(branch, L) * mellin_s3(L)
                                / denom_regulator(branch, L)

STABILITY CRITERION (plan §W10-4 pre-registered)
------------------------------------------------
  stable iff |w_0(L=10) - w_0(L=12)| / |mean(w_0 over L)| <= 0.10

CAUCHY-MONOTONE RESIDUE CRITERION
---------------------------------
  Cauchy-monotone iff |residue(L+2)| < |residue(L)| for all L in {8, 10}
  (the residue DECAYS as L grows, per Connes-Marcolli CM-2008 Mellin-cone).

PASS / FAIL / INFO THRESHOLDS (pre-registered in plan §W10-4)
--------------------------------------------------------------
  PASS iff num_stable_branches >= 1 from INVERTED families (c, d) with
    Cauchy-monotone residue decay.
  FAIL iff num_stable_branches = 0 across (c, d); no inverted branch
    rescues w_0.
  INFO iff exactly 1 branch passes one criterion but not both — flagged
    for L_max=14 follow-up.

Classification: GEOMETRIC (w_0 branch structure is a feature of the
DeWitt-superspace late-time asymptotic geometry under ξ_J / ξ_E_GGE
coupling ratio)
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

os.environ.setdefault("OMP_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold  # noqa

import hashlib
import json
import sys
import time
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")  # (local) non-interactive backend
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"
GATE_ID = "S85-W10-W0-L-INVERTED-BRANCH-ENUMERATION"
SCHEME = "4-branch-enumeration-inverted-ordering"
CONVENTION = "CM-2008-s3-Mellin-cone"
L_MAX = 12                                                       # (local)

# Pre-registered thresholds
STABILITY_BAND = 0.10                                            # (local) 10% RATIO
XI_J = 0.008911                                                  # (local) TB-pinned, L-indep
TARGET_L = [8, 10, 12]                                           # (local) plan-pinned

OUT_NPZ = resolve_output(85, 's85_w10_w0_inverted_branch_enumeration.npz')
OUT_JSON = resolve_output(85, 's85_w10_w0_inverted_branch_enumeration.json')
OUT_PNG = resolve_output(85, 's85_w10_w0_inverted_branch_enumeration.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')


def sha256_of(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                    # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        label = "MISSING" if not sha else sha[:16] + "..."       # (local)
        print(f"  {rel}: {label}")
        pins[rel] = sha if sha else "<missing>"
    return pins


def compute_dual_sha(script: Path, canonical: Path, pins: dict) -> tuple[str, str]:
    sb = script.read_bytes()                                     # (local)
    cb = canonical.read_bytes()                                  # (local)
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"), sort_keys=True,
    ).encode()                                                   # (local)
    return (
        hashlib.sha256(sb + cb + pj).hexdigest(),
        hashlib.sha256(sb).hexdigest(),
    )


def load_sv2():
    """Read SV2 baseline trajectories at L = {5, 6, 7, 8}."""
    sv2_path = resolve_output(84, 's84_w1a_w0_sv2.npz')                  # (local)
    d = np.load(sv2_path, allow_pickle=True)                     # (local)
    L_axis = np.array(d["L_axis"], dtype=int)                    # (local)
    R_JE = np.array(d["R_JE_axis"], dtype=float)                 # (local)
    xi_E_GGE = np.array(d["xi_E_GGE_axis"], dtype=float)         # (local)
    mellin_s3 = np.array(d["mellin_s3_axis"], dtype=float)       # (local)
    S_zeta_E = np.array(d["S_zeta_E_axis"], dtype=float)         # (local)
    S_Zub_E = np.array(d["S_Zubarev_E_axis"], dtype=float)       # (local)
    xi_J_sv2 = float(d["xi_J_anchor"])                           # (local)
    return dict(
        L_axis=L_axis,
        R_JE=R_JE,
        xi_E_GGE=xi_E_GGE,
        mellin_s3=mellin_s3,
        S_zeta_E=S_zeta_E,
        S_Zub_E=S_Zub_E,
        xi_J_sv2=xi_J_sv2,
    )


def log_linear_extrapolate(L_in, y_in, L_out):
    """Fit log(y) = a + b*L on L_in and predict exp(a + b*L) at L_out.
    Returns (y_extrap, slope, intercept, r_squared)."""
    log_y = np.log(y_in)                                         # (local)
    b, a = np.polyfit(L_in, log_y, 1)                            # (local) slope, intercept
    y_fit = np.exp(a + b * L_in)                                 # (local)
    # R^2 in log space
    ss_res = np.sum((log_y - (a + b * L_in)) ** 2)               # (local)
    ss_tot = np.sum((log_y - np.mean(log_y)) ** 2)               # (local)
    r_sq = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0            # (local)
    y_out = np.exp(a + b * np.asarray(L_out))                    # (local)
    return y_out, float(b), float(a), float(r_sq)


def extrapolate_to_target(sv2):
    """Extrapolate SV2 quantities to L = {10, 12}; keep L = 8 exact."""
    print("--- Log-linear extrapolation (SV2 L in {5,6,7,8} → L in {10,12}) ---")
    L_sv2 = sv2["L_axis"]                                        # (local)
    L_target = np.array(TARGET_L, dtype=int)                     # (local)

    # Interpolate/extrapolate for each quantity
    def extrap(name, y_sv2):
        y_out, b, a, r_sq = log_linear_extrapolate(L_sv2, y_sv2, L_target)
        print(f"  {name}: slope={b:.4f}, R²={r_sq:.6f}")
        print(f"    SV2 [L={L_sv2.tolist()}]    = "
              f"{[f'{v:.4e}' for v in y_sv2]}")
        print(f"    target [L={L_target.tolist()}] = "
              f"{[f'{v:.4e}' for v in y_out]}")
        return y_out, b, a, r_sq

    R_JE_tgt, R_JE_slope, R_JE_int, R_JE_r2 = extrap("R_JE", sv2["R_JE"])
    xi_E_GGE_tgt, xi_slope, xi_int, xi_r2 = extrap(
        "xi_E_GGE", sv2["xi_E_GGE"]
    )
    mellin_tgt, m_slope, m_int, m_r2 = extrap(
        "mellin_s3", sv2["mellin_s3"]
    )
    S_zeta_tgt, sz_slope, sz_int, sz_r2 = extrap(
        "S_zeta_E", sv2["S_zeta_E"]
    )
    S_Zub_tgt, szb_slope, szb_int, szb_r2 = extrap(
        "S_Zubarev_E", sv2["S_Zub_E"]
    )

    return dict(
        L=L_target,
        R_JE=R_JE_tgt,
        xi_E_GGE=xi_E_GGE_tgt,
        mellin_s3=mellin_tgt,
        S_zeta_E=S_zeta_tgt,
        S_Zub_E=S_Zub_tgt,
        fit_diagnostics=dict(
            R_JE_slope=R_JE_slope, R_JE_r2=R_JE_r2,
            xi_E_GGE_slope=xi_slope, xi_E_GGE_r2=xi_r2,
            mellin_slope=m_slope, mellin_r2=m_r2,
            S_zeta_slope=sz_slope, S_zeta_r2=sz_r2,
            S_Zub_slope=szb_slope, S_Zub_r2=szb_r2,
        ),
    )


def compute_branches(tgt):
    """Compute w_0 and Mellin residue for each branch at each target L.

    Branch definitions:
      a = ζ-regulator, Bogoliubov-dominant (baseline)
      b = Zubarev-regulator, Bogoliubov-dominant (baseline)
      c = ζ-regulator, Josephson-dominant (INVERTED)
      d = Zubarev-regulator, Josephson-dominant (INVERTED)
    """
    print("--- Branch enumeration (4 branches × 3 L) ---")
    L = tgt["L"]                                                 # (local)
    mellin = tgt["mellin_s3"]                                    # (local)
    xi_E = tgt["xi_E_GGE"]                                       # (local)
    S_z = tgt["S_zeta_E"]                                        # (local)
    S_zb = tgt["S_Zub_E"]                                        # (local)
    R_JE = tgt["R_JE"]                                           # (local)

    # xi_effective and denom_regulator per branch
    branch_configs = {
        "a": dict(xi="E_GGE", reg="zeta",    label="ζ·Bog-dom (baseline)"),
        "b": dict(xi="E_GGE", reg="Zubarev", label="Zub·Bog-dom (baseline)"),
        "c": dict(xi="J",     reg="zeta",    label="ζ·Jos-dom (INVERTED)"),
        "d": dict(xi="J",     reg="Zubarev", label="Zub·Jos-dom (INVERTED)"),
    }                                                            # (local)

    results = {}                                                 # (local)
    for key, cfg in branch_configs.items():
        # xi_effective(L)
        if cfg["xi"] == "E_GGE":
            xi_eff = xi_E.copy()                                 # (local)
        else:
            xi_eff = np.full_like(xi_E, XI_J)                    # (local)
        # denom
        denom = S_z if cfg["reg"] == "zeta" else S_zb            # (local)
        # residue per L: xi_eff * mellin / denom
        residue = xi_eff * mellin / denom                        # (local)
        # w_0(L) = -1 + 2 * residue  (definitional model)
        w0 = -1.0 + 2.0 * residue                                # (local)

        print(f"  branch {key} ({cfg['label']}):")
        for i, Li in enumerate(L):
            print(f"    L={Li:2d}: xi_eff={xi_eff[i]:.6f} "
                  f"denom={denom[i]:.4e} residue={residue[i]:.4e} "
                  f"w_0={w0[i]:.6f}")

        # Stability at L=10 → L=12
        # L indices: L=8 is 0, L=10 is 1, L=12 is 2
        w0_L10 = w0[1]                                           # (local)
        w0_L12 = w0[2]                                           # (local)
        w0_mean = float(np.mean(w0))                             # (local)
        if abs(w0_mean) > 1e-30:
            stability_delta = abs(w0_L10 - w0_L12) / abs(w0_mean)  # (local)
        else:
            stability_delta = float("inf")
        stable = stability_delta <= STABILITY_BAND               # (local)

        # Cauchy-monotone residue DECAY across L = 8 → 10 → 12
        cauchy_8_to_10 = abs(residue[1]) < abs(residue[0])       # (local)
        cauchy_10_to_12 = abs(residue[2]) < abs(residue[1])      # (local)
        cauchy_mono_decay = bool(cauchy_8_to_10 and cauchy_10_to_12)  # (local)

        print(f"    stability_delta = {stability_delta:.4e} "
              f"(threshold {STABILITY_BAND}) → stable = {stable}")
        print(f"    Cauchy 8→10: {cauchy_8_to_10}  10→12: "
              f"{cauchy_10_to_12} → monotone-decay = {cauchy_mono_decay}")

        results[key] = dict(
            label=cfg["label"],
            xi_effective=xi_eff.tolist(),
            denominator=denom.tolist(),
            residue=residue.tolist(),
            w_0=w0.tolist(),
            stability_delta=float(stability_delta),
            stable=bool(stable),
            cauchy_8_to_10=bool(cauchy_8_to_10),
            cauchy_10_to_12=bool(cauchy_10_to_12),
            cauchy_mono_decay=cauchy_mono_decay,
            passes_both=bool(stable and cauchy_mono_decay),
        )

    # Count stable branches — per plan, must pass BOTH stability AND
    # Cauchy-monotone decay; PASS condition only counts inverted (c, d)
    inverted_stable = sum(
        1 for k in ("c", "d") if results[k]["passes_both"]
    )                                                            # (local)
    total_stable = sum(1 for k in results if results[k]["passes_both"])  # (local)

    print(f"  num_stable (all branches):       {total_stable}")
    print(f"  num_stable (INVERTED c, d only): {inverted_stable}")

    return results, total_stable, inverted_stable


def make_plot(sv2, tgt, branches):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    # Panel 1: Mellin residue trajectory per branch
    L = tgt["L"]                                                 # (local)
    for key, b in branches.items():
        ax1.plot(L, b["residue"], marker="o", label=f"{key}: {b['label']}")
    ax1.set_yscale("log")
    ax1.set_xlabel("L_max")
    ax1.set_ylabel("|Mellin-cone s=3 residue|")
    ax1.set_title("Branch-residue trajectories "
                  "(Cauchy-monotone DECAY required for PASS)")
    ax1.legend(fontsize=7)
    ax1.grid(True, alpha=0.3)

    # Panel 2: w_0 convergence per branch
    for key, b in branches.items():
        ax2.plot(L, b["w_0"], marker="s", label=f"{key}: {b['label']}")
    ax2.axhline(-1.0, linestyle="--", color="gray",
                label="exact de-Sitter w_0 = -1")
    ax2.set_xlabel("L_max")
    ax2.set_ylabel("w_0 (branch definitional model)")
    ax2.set_title("Branch w_0 (stability band = 10% at L=10→12)")
    ax2.legend(fontsize=7)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


def compute():
    sv2 = load_sv2()                                             # (local)
    tgt = extrapolate_to_target(sv2)                             # (local)
    branches, total_stable, inverted_stable = compute_branches(tgt)  # (local)
    make_plot(sv2, tgt, branches)
    return dict(
        sv2=sv2,
        target=tgt,
        branches=branches,
        total_stable=total_stable,
        inverted_stable=inverted_stable,
        value=inverted_stable,  # the 4-tuple value
    )


def evaluate_gate(result) -> str:
    inv = result["inverted_stable"]                              # (local)
    # Check "exactly 1 of 2 criteria" on any inverted branch for INFO
    half_pass = 0                                                # (local)
    for k in ("c", "d"):
        b = result["branches"][k]                                # (local)
        stab_only = b["stable"] and not b["cauchy_mono_decay"]   # (local)
        cauch_only = b["cauchy_mono_decay"] and not b["stable"]  # (local)
        if stab_only or cauch_only:
            half_pass += 1

    if inv >= 1:
        return "PASS"
    if half_pass == 1:
        return "INFO"
    return "FAIL"


def emit_4tuple(v, s, c, L):
    return f"(value={v!r}, scheme={s}, convention={c}, L_max={L})"


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
    t = result["target"]                                         # (local)
    b = result["branches"]                                       # (local)
    np.savez_compressed(
        OUT_NPZ,
        L_target=t["L"],
        R_JE_target=t["R_JE"],
        xi_E_GGE_target=t["xi_E_GGE"],
        mellin_s3_target=t["mellin_s3"],
        S_zeta_E_target=t["S_zeta_E"],
        S_Zubarev_E_target=t["S_Zub_E"],
        L_sv2=result["sv2"]["L_axis"],
        R_JE_sv2=result["sv2"]["R_JE"],
        mellin_s3_sv2=result["sv2"]["mellin_s3"],
        branch_a_w0=b["a"]["w_0"], branch_a_residue=b["a"]["residue"],
        branch_b_w0=b["b"]["w_0"], branch_b_residue=b["b"]["residue"],
        branch_c_w0=b["c"]["w_0"], branch_c_residue=b["c"]["residue"],
        branch_d_w0=b["d"]["w_0"], branch_d_residue=b["d"]["residue"],
        inverted_stable=result["inverted_stable"],
        total_stable=result["total_stable"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )


def save_json(result, audit_sha, content_sha, pins):
    def _listify(d):
        out = {}                                                 # (local)
        for k, v in d.items():
            if isinstance(v, np.ndarray):
                out[k] = v.tolist()
            elif isinstance(v, dict):
                out[k] = _listify(v)
            else:
                out[k] = v
        return out

    payload = dict(
        gate_id=GATE_ID,
        session=SESSION,
        wave="W10",
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        model_description=(
            "w_0(branch, L) = -1 + 2 * xi_effective * mellin_s3 / "
            "denom_regulator; xi_effective = xi_E_GGE(L) for Bogoliubov, "
            "xi_J for Josephson; denom_regulator = S_zeta_E(L) or "
            "S_Zubarev_E(L). Mellin residue = xi_effective * mellin_s3 / "
            "denom_regulator."
        ),
        stability_band=STABILITY_BAND,
        xi_J=XI_J,
        sv2=_listify(result["sv2"]),
        target=_listify(result["target"]),
        branches={k: _listify(v) for k, v in result["branches"].items()},
        inverted_stable=int(result["inverted_stable"]),
        total_stable=int(result["total_stable"]),
        value=int(result["value"]),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        input_pins=pins,
        date="2026-04-24",
    )
    OUT_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8"
    )


def main():
    t0 = time.time()                                             # (local)

    input_files = [
        resolve_script(None, 'canonical_constants.py'),
        resolve_output(84, 's84_w1a_w0_sv2.npz'),
    ]                                                            # (local)

    pins = log_input_pins(input_files)

    script_path = Path(__file__).resolve()
    canonical_path = resolve_script(None, 'canonical_constants.py')
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    result = compute()
    verdict = evaluate_gate(result)

    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_npz(result, audit_sha, content_sha)
    save_json(result, audit_sha, content_sha, pins)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    wall = time.time() - t0                                      # (local)
    print(f"\n=== {GATE_ID}: {verdict}  (wall {wall:.2f}s) ===")
    print(f"    -> {OUT_NPZ.name}")
    print(f"    -> {OUT_JSON.name}")
    print(f"    -> {OUT_PNG.name}")
    print(f"    -> verdict appended to {VERDICT_TXT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
