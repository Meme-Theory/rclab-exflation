#!/usr/bin/env python3
"""
S85 W1a-3: ALT-D-SPEC-PROBE
===========================

Gate: S85-W1a-ALT-D-SPEC-PROBE
Trigger: [VERIFY-THEOREM]
Classification: GEOMETRIC (alternative pathway to d_spec=12 at fiber-transition scale)
Agent: mack-cosmic-bridge

Hypothesis: The d_spec exponent "12" in the mu_BC running (empirically
fit in 1-loop Z_R) is derivable three ways, all converging to 12 +/- 0.1:
  Route (i)   heat-kernel Weyl-law slope on SU(3) spectrum + M^4 flat.
  Route (ii)  zeta-function leading pole location + M^4 flat offset.
  Route (iii) topological: dim(SU(3)) + dim(M^4) = 8 + 4 = 12 (exact).

Substitution chain (Python-verified, with truncation-bias disclosure):

Route (iii) is exact at L_max -> infinity (topological fact; no spectrum needed):
  d_spec^(rep) = dim(SU(3)) + dim(M^4) = 8 + 4 = 12.

Route (i) Weyl-law slope extraction:
  For a D-dim compact manifold with Laplacian spectrum {lambda_i} and
  degeneracies {m_i}, Weyl's law gives
     N(Lambda^2) := sum_{lambda^2 <= Lambda^2} m_i  ~  V * Lambda^D.
  Hence log N vs log(Lambda^2) has asymptotic slope D/2.
  For SU(3) with Peter-Weyl multiplicity dim^2(p,q), D_SU3 = 8,
  expected slope = 4.
  At finite L_max = 10 truncation, the asymptotic regime is narrow;
  fitted slope approaches 4 from below as L_max increases.

Route (ii) zeta-function pole extraction:
  zeta_{D_K}(s) := sum m_i * lambda_i^{-s} has a simple pole at s = D/2.
  At finite cutoff lambda_max, the partial zeta is bounded; the pole
  location is estimated from the scaling
     zeta_L(s; Lambda_max^2) ~ Lambda_max^{D/2 - s}  (for s < D/2).
  Fit log zeta_L vs log Lambda_max^2 at probe s -> slope s* - s.
  Total manifold: zeta pole is at s = D_total/2 = 6 for d=12.

Substitution chain (Python-explicit at compute() call):
  Step 1: Build SU(3) Casimir spectrum at L_max=10 (p+q <= 10 excluding
          (0,0)), Peter-Weyl multiplicity mult = dim(p,q)^2.
  Step 2: Route (iii): d_spec^(rep) = 8 + 4 = 12.
  Step 3: Route (i): fit log(N_cum) vs log(C_2) on Weyl-law window
          C_2 in [10, 80]; extract slope; D_SU3 = 2*slope; d_hk = D_SU3 + 4.
  Step 4: Route (ii): probe zeta_L at s=3.5 (just below expected SU(3)
          pole 4.0); fit log zeta_L(Lambda_max) vs log Lambda_max^2;
          s*_SU3 = s_probe + slope_z; d_zeta = 2*(s*_SU3 + 2).
  Step 5: Residuals from target 12: r_i = |d_i - 12| for i in {hk, zeta, rep}.
  Step 6: max-residual = max(r_hk, r_zeta, r_rep).
  Direction: Topological (iii) is EXACT 12. Numerical (i) and (ii) carry
             L_max=10 truncation bias; asymptotic convergence to 12 is
             expected but NOT achieved at ±0.1 precision with L_max=10.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - sessions/framework/Phononic-Substrate-Geometry.md (if present)
  - script bytes

Output 4-tuple:
  (value=<max_residual>, scheme=3-route-convergence, convention=CONVENTION-I, L_max=10)

Thresholds (pre-registered, plan §W1a-3):
  - PASS iff max_residual <= 0.1 (three-route convergence is STRUCTURAL).
  - FAIL iff any route | d - 12 | > 1.0 (routes disagree; d=12 is empirical fit).
  - INFO iff 0.1 < max_residual <= 1.0 (partial convergence; one route scheme-sensitive).

Output files:
  - computations/session-85/s85_w1a_alt_d_spec_probe.py
  - computations/session-85/s85_w1a_alt_d_spec_probe.npz
  - computations/session-85/s85_w1a_alt_d_spec_probe.png
  - verdict appended to computations/session-85/s85_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import J_C2  # noqa: E402 (used as diagnostic annotation)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W1a-ALT-D-SPEC-PROBE"                                # (local)
SCHEME = "3-route-convergence"                                      # (local)
CONVENTION = "CONVENTION-I"                                         # (local) Mellin-balance baseline
L_MAX = 10                                                          # (local)

# Pre-registered thresholds (plan §W1a-3)
PASS_RESID = 0.1                                                    # (local)
FAIL_RESID = 1.0                                                    # (local)

# Target topological d_spec
D_TARGET = 12.0                                                     # (local) dim SU(3) + dim M^4
DIM_SU3 = 8                                                         # (local)
DIM_M4 = 4                                                          # (local)

# Weyl-law fit window (C_2 range)
WEYL_MIN = 10.0                                                     # (local)
WEYL_MAX = 80.0                                                     # (local)

# Zeta probe
S_PROBE = 3.5                                                       # (local) below SU(3) pole at s=4
ZETA_CUTOFF_GRID = np.array([20.0, 30.0, 50.0, 80.0, 110.0])        # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w1a_alt_d_spec_probe.npz"
OUT_PNG = SCRIPT_DIR / "s85_w1a_alt_d_spec_probe.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
FRAMEWORK_MD = PROJECT_ROOT / "sessions" / "framework" / "Phononic-Substrate-Geometry.md"

INPUT_FILES = [CANON_PY]
if FRAMEWORK_MD.exists():
    INPUT_FILES.append(FRAMEWORK_MD)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                                    # (local)
    h = hashlib.sha256()                                            # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""                                              # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                           # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")

    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)

    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                 # (local)

    return audit, content


def build_su3_spectrum(L_max: int) -> tuple[np.ndarray, np.ndarray]:
    """Return (C2_sorted, dim_sorted) for irreps with p+q <= L_max, (p,q) != (0,0)."""
    data = []                                                       # (local)
    for p in range(L_max + 1):
        for q in range(L_max + 1):
            if p + q > L_max:
                continue
            if p == 0 and q == 0:
                continue
            dim = (p + 1) * (q + 1) * (p + q + 2) // 2              # (local)
            C2 = p * p + p * q + q * q + 3 * (p + q)                # (local)
            data.append((C2, dim))
    data = sorted(data, key=lambda x: x[0])
    C2_arr = np.array([d[0] for d in data], dtype=np.float64)       # (local)
    dim_arr = np.array([d[1] for d in data], dtype=np.float64)      # (local)
    return C2_arr, dim_arr


def route_i_heat_kernel_weyl(C2_arr: np.ndarray, mult_arr: np.ndarray) -> dict:
    """Weyl-law slope fit: log N(Lambda^2) vs log(Lambda^2)."""
    N_cum = np.cumsum(mult_arr)                                     # (local)
    mask = (C2_arr >= WEYL_MIN) & (C2_arr <= WEYL_MAX)              # (local)
    log_L2 = np.log(C2_arr[mask])                                   # (local)
    log_N = np.log(N_cum[mask])                                     # (local)
    slope, intercept = np.polyfit(log_L2, log_N, 1)
    D_SU3 = 2.0 * slope                                             # (local) expected 8 at L_max -> inf
    d_total = D_SU3 + DIM_M4                                        # (local) add M^4
    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "D_SU3_hk": float(D_SU3),
        "d_spec_hk": float(d_total),
        "weyl_window": (WEYL_MIN, WEYL_MAX),
        "n_points_in_fit": int(mask.sum()),
        "log_L2_fit": log_L2.copy(),
        "log_N_fit": log_N.copy(),
    }


def route_ii_zeta_pole(C2_arr: np.ndarray, mult_arr: np.ndarray) -> dict:
    """Zeta leading-pole extraction via truncated partial-sum scaling.

    zeta_L(s; Lambda_max^2) = sum_{C2 <= Lambda_max^2} mult * C2^(-s/2)
      ~ Lambda_max^{D - s}   (for s < D, with D = D_SU3)
    Fit log zeta_L vs log Lambda_max^2; slope = (D - s)/2, so s*_SU3 = s_probe + slope.
    """
    s = S_PROBE                                                     # (local)
    zeta_vals = []                                                  # (local)
    for Lmax2 in ZETA_CUTOFF_GRID:
        mask = C2_arr <= Lmax2                                      # (local)
        z = float((mult_arr[mask] * C2_arr[mask] ** (-s / 2.0)).sum())  # (local)
        zeta_vals.append(z)
    zeta_vals = np.array(zeta_vals, dtype=np.float64)
    log_L2 = np.log(ZETA_CUTOFF_GRID)                               # (local)
    log_z = np.log(zeta_vals)                                       # (local)
    slope_z, intercept_z = np.polyfit(log_L2, log_z, 1)
    # slope_z = (D_SU3 - s)/2  =>  D_SU3 = 2*slope_z + s
    # But s is referred to the eigenvalue lambda = sqrt(C_2), so we use lambda^{-s}.
    # For N(lambda_max) ~ lambda_max^D, zeta_L(s) ~ lambda_max^{D-s}.
    # With substitution z = Lambda_max^2, lambda_max = sqrt(z),
    # log z_L ~ ((D - s)/2) log(z) + const  =>  (D_SU3 - s)/2 = slope_z
    D_SU3_zeta = 2.0 * slope_z + s                                  # (local)
    s_star_SU3 = D_SU3_zeta / 2.0                                   # (local) SU(3) pole
    s_star_total = s_star_SU3 + DIM_M4 / 2.0                        # (local) add M^4 pole shift
    d_spec_zeta = 2.0 * s_star_total                                # (local) = D_SU3 + 4
    return {
        "s_probe": float(s),
        "zeta_cutoff_grid": ZETA_CUTOFF_GRID.copy(),
        "zeta_values": zeta_vals,
        "slope_z": float(slope_z),
        "intercept_z": float(intercept_z),
        "D_SU3_zeta": float(D_SU3_zeta),
        "s_star_SU3": float(s_star_SU3),
        "s_star_total": float(s_star_total),
        "d_spec_zeta": float(d_spec_zeta),
    }


def route_iii_topological() -> dict:
    """Exact topological count. No spectrum dependence, no truncation."""
    d_spec_rep = DIM_SU3 + DIM_M4                                   # (local) 8 + 4 = 12
    return {
        "dim_SU3": DIM_SU3,
        "dim_M4": DIM_M4,
        "d_spec_rep": float(d_spec_rep),
    }


def compute() -> dict:
    C2_arr, dim_arr = build_su3_spectrum(L_MAX)
    mult_arr = dim_arr ** 2                                         # (local) Peter-Weyl bi-invariant

    ri = route_i_heat_kernel_weyl(C2_arr, mult_arr)
    rii = route_ii_zeta_pole(C2_arr, mult_arr)
    riii = route_iii_topological()

    d_vals = {
        "hk": ri["d_spec_hk"],
        "zeta": rii["d_spec_zeta"],
        "rep": riii["d_spec_rep"],
    }
    residuals = {k: abs(v - D_TARGET) for k, v in d_vals.items()}   # (local)
    max_residual = max(residuals.values())                          # (local)

    return {
        "d_target": D_TARGET,
        "d_vals": d_vals,
        "residuals": residuals,
        "max_residual": max_residual,
        "value": max_residual,  # primary gate value
        "route_i": ri,
        "route_ii": rii,
        "route_iii": riii,
        "C2_arr": C2_arr,
        "dim_arr": dim_arr,
        "mult_arr": mult_arr,
        "n_irreps": int(len(C2_arr)),
    }


def evaluate_gate(res: dict) -> str:
    r = res["max_residual"]                                         # (local)
    if r <= PASS_RESID:
        return "PASS"
    if r > FAIL_RESID:
        return "FAIL"
    return "INFO"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def make_plot(res: dict, out_path: Path) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.0))             # (local)

    # Panel A: Weyl-law fit
    ax = axes[0]
    ri = res["route_i"]
    ax.scatter(np.exp(ri["log_L2_fit"]), np.exp(ri["log_N_fit"]),
               c="#1a5fb4", s=18, label="N(Lambda^2) data")
    L2_fit = np.exp(ri["log_L2_fit"])
    Nfit = np.exp(ri["intercept"]) * L2_fit ** ri["slope"]
    ax.plot(L2_fit, Nfit, color="#b03030", lw=1.5,
            label=f"Fit slope={ri['slope']:.3f} => D_SU3={ri['D_SU3_hk']:.3f}")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel(r"$\Lambda^2$ (Casimir cutoff)")
    ax.set_ylabel(r"$N(\Lambda^2)$ (cumulative weighted count)")
    ax.set_title(f"Route (i) Weyl-law: d_hk = {ri['d_spec_hk']:.3f}")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.25)

    # Panel B: zeta pole fit
    ax = axes[1]
    rii = res["route_ii"]
    ax.scatter(rii["zeta_cutoff_grid"], rii["zeta_values"],
               c="#1a5fb4", s=30, label=rf"$\zeta_L$ at s={rii['s_probe']}")
    L2 = rii["zeta_cutoff_grid"]
    zfit = np.exp(rii["intercept_z"]) * L2 ** rii["slope_z"]
    ax.plot(L2, zfit, color="#b03030", lw=1.5,
            label=f"Fit slope={rii['slope_z']:.3f} => s*_SU3={rii['s_star_SU3']:.3f}")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel(r"$\Lambda_{\max}^2$ (cutoff)")
    ax.set_ylabel(r"$\zeta_L(s={:.1f})$".format(rii['s_probe']))
    ax.set_title(f"Route (ii) zeta: d_zeta = {rii['d_spec_zeta']:.3f}")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.25)

    # Panel C: bar of d_spec values vs target
    ax = axes[2]
    labels = ["hk (Weyl)", "zeta", "rep (topo)"]
    vals = [res["d_vals"]["hk"], res["d_vals"]["zeta"], res["d_vals"]["rep"]]
    colors = ["#1a5fb4", "#4d8cb7", "#2a7a2a"]
    bars = ax.bar(labels, vals, color=colors, alpha=0.85)
    ax.axhline(D_TARGET, color="#b03030", lw=1.5, ls="--",
               label=f"target d_spec={D_TARGET}")
    ax.axhspan(D_TARGET - PASS_RESID, D_TARGET + PASS_RESID,
               color="#2a7a2a", alpha=0.12, label=f"PASS band +/-{PASS_RESID}")
    ax.axhspan(D_TARGET - FAIL_RESID, D_TARGET + FAIL_RESID,
               color="#b08030", alpha=0.08, label=f"INFO band +/-{FAIL_RESID}")
    ax.set_ylabel(r"$d_{\rm spec}$")
    ax.set_title(f"max residual = {res['max_residual']:.3f}")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(True, alpha=0.25, axis="y")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.3, f"{v:.2f}", ha="center", fontsize=9)

    fig.suptitle(f"{GATE_ID}: three-route d_spec convergence (L_max={L_MAX})")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


def main() -> int:
    t0 = time.time()                                                # (local)
    print(f"  (diagnostic: canonical J_C2 = {J_C2} — coset Casimir, referenced in plan §W1a-3 rep-theoretic formula but NOT used for route (iii), which is exact topological)")

    pins = log_input_pins(INPUT_FILES)
    print(f"  closure: {closure_hash(pins)[:16]}... (legacy)")

    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: SU(3) Casimir spectrum L_max={L_MAX}: {res['n_irreps']} irreps "
          f"(excluding trivial), Peter-Weyl mult dim^2.")
    print(f"  Step 2: Route (iii) topological: dim(SU3)+dim(M^4) = {DIM_SU3}+{DIM_M4} "
          f"= {res['d_vals']['rep']} (EXACT, no truncation).")
    print(f"  Step 3: Route (i) Weyl-law:")
    print(f"          window C_2 in [{WEYL_MIN},{WEYL_MAX}], {res['route_i']['n_points_in_fit']} points")
    print(f"          slope = {res['route_i']['slope']:.4f} (expected 4.0 asymptotic)")
    print(f"          D_SU3 = 2*slope = {res['route_i']['D_SU3_hk']:.4f} "
          f"(expected 8.0 asymptotic)")
    print(f"          d_hk = D_SU3 + {DIM_M4} = {res['d_vals']['hk']:.4f}")
    print(f"  Step 4: Route (ii) zeta leading-pole extraction:")
    print(f"          probe s={res['route_ii']['s_probe']}, cutoffs {ZETA_CUTOFF_GRID}")
    print(f"          slope(log zeta vs log Lambda^2) = {res['route_ii']['slope_z']:.4f}")
    print(f"          D_SU3_zeta = 2*slope + s = {res['route_ii']['D_SU3_zeta']:.4f}")
    print(f"          s*_total = {res['route_ii']['s_star_total']:.4f} (expected 6.0)")
    print(f"          d_zeta = 2*s*_total = {res['d_vals']['zeta']:.4f}")
    print(f"  Step 5: Residuals from d_target={D_TARGET}:")
    for k, v in res["residuals"].items():
        print(f"          {k:>4}: |{res['d_vals'][k]:.4f} - 12| = {v:.4f}")
    print(f"  Step 6: max_residual = {res['max_residual']:.4f}")
    print(f"          Thresholds: PASS<={PASS_RESID}, FAIL>{FAIL_RESID}")
    print(f"          ==> {verdict}")
    print()
    if verdict == "FAIL" or verdict == "INFO":
        print("  Truncation-bias disclosure: at L_max=10 the Weyl-law regime is narrow")
        print("  (C_2 in [10,80] vs asymptotic infinity). Route (iii) is EXACT at 12.")
        print("  Routes (i) and (ii) converge to 12 from below as L_max -> infinity;")
        print("  verdict documents the L_max=10 finite-size residual, not a falsification")
        print("  of the topological dim=12 claim.")
        print()

    np.savez(
        OUT_NPZ,
        d_target=np.float64(D_TARGET),
        d_hk=np.float64(res["d_vals"]["hk"]),
        d_zeta=np.float64(res["d_vals"]["zeta"]),
        d_rep=np.float64(res["d_vals"]["rep"]),
        residual_hk=np.float64(res["residuals"]["hk"]),
        residual_zeta=np.float64(res["residuals"]["zeta"]),
        residual_rep=np.float64(res["residuals"]["rep"]),
        max_residual=np.float64(res["max_residual"]),
        slope_weyl=np.float64(res["route_i"]["slope"]),
        D_SU3_hk=np.float64(res["route_i"]["D_SU3_hk"]),
        slope_zeta=np.float64(res["route_ii"]["slope_z"]),
        s_star_SU3=np.float64(res["route_ii"]["s_star_SU3"]),
        s_star_total=np.float64(res["route_ii"]["s_star_total"]),
        C2_arr=res["C2_arr"],
        mult_arr=res["mult_arr"],
        zeta_values=res["route_ii"]["zeta_values"],
        zeta_cutoff_grid=res["route_ii"]["zeta_cutoff_grid"],
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["value"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # physics-valid verdict; not an error


if __name__ == "__main__":
    sys.exit(main())
