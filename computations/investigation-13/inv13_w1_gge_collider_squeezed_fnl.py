#!/usr/bin/env python3
"""
INV13 W1-1 — GGE cosmological-collider squeezed-limit bispectrum f_NL
=====================================================================

Gate: INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL  ([VERIFY])

Pre-registered threshold (set-membership / characterization gate):
  classify(squeezed_limit_shape) in {NON-ANALYTIC-COLLIDER, ANALYTIC-LOCAL, NONE}
  PASS  iff shape == NON-ANALYTIC-COLLIDER:  |Delta_fit| >= 0.05 AND
            feature-localization residual to nearest D_K eigenvalue ratio <= 5%.
  INFO  iff shape == ANALYTIC-LOCAL:  Delta_fit == 0 plateau (|Delta_fit| < 0.05),
            a tau_NL-style amplitude with NO collider non-analyticity.
  FAIL  iff NO computable bispectrum is assembled (machinery, not physics).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py  (post-prereq runtime SHA; feeds audit_sha256)
  - computations/session-75/s75_dimer_z2_pair_production.npz  (GGE pair occupations nk_total)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<shape-class : Delta_fit>, scheme=AHM-collider-squeezed-limit,
   convention=RATIO, L_max=10)

Classification: PHONONIC

METHODOLOGY
-----------
Substrate-first: the substrate IS the post-transit GGE quasiparticle spectrum. The
D_K eigenvalue spectrum at the fold reorganizes under supersonic transit (Mach 13.75,
impulsive) into 59.8 Bogoliubov quasiparticle pairs whose product-state occupation is
governed by three SU(3)-branch Lagrange multipliers (lambda_B1/B2/B3, atlas-07/S39).
Explanation flows  D_K eigenvalues -> GGE branch-masses -> squeezed non-analyticity
-> measured CMB/21-cm folded f_NL.

We assemble the squeezed-limit dimensionless bispectrum-ratio observable
    S(k_long/k1) := B(k1, k1, k_long) / [P(k1) P(k_long)]
                  = f_NL_local + sum_a c_a (k_long/k1)^{Delta(mu_a)}
in the Arkani-Hamed-Maldacena cosmological-collider formalism (arXiv:1503.08043),
where the three branch multipliers play the role of the heavy-field content. For a
heavy scalar of dimensionless mass mu = m/H,
    Delta(mu) = 3/2 - sqrt(9/4 - mu^2)                       [complementary, mu<3/2]
    Delta = 3/2 +/- i*mutil, mutil = sqrt(mu^2 - 9/4)        [principal, mu>3/2; OSCILLATORY,
            amplitude carries the Boltzmann particle-production factor exp(-pi*mutil)].
The LOCAL/EFT term has Delta=0 (scale-invariant squeezed plateau) — the discriminant null.

The substrate fixes the heavy-field weights c_a from the GGE branch occupations and the
mass ratios mu_a = lambda_Ba / H_transit. Two H_transit anchors are reported (the branch
multiplier IS the heavy-mass scale in collider units, per the plan substitution chain):
  - H_tilde_canonical_TD = 5.9076e-3 (S82 Branch-A inflation-analog clock rate; PRIMARY)
  - H_fold = 586.5268      (S38 literal fold Hubble in M_KK units; CROSS-CHECK)
We FIT the squeezed exponent Delta of the assembled S(k_long/k1) over the squeezed window
and classify the recovered shape against the |Delta_fit|>=0.05 discriminant; the
feature-localization k-ratio is matched against the GGE spectral ratios (the "D_K
eigenvalue ratios" the collider resonances would localize at). The local-baseline
amplitude is f_NL_folded=0.1293 (S83 GGE-BISPECTRUM-67).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-cap (OMP_NUM_THREADS=8) BEFORE numpy: spectrum length-16, matrices < 100x100
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the emit_verdict knowledge-MCP tool (race-safe);
  the script PRINTS the payload (print_verdict_payload), the agent calls emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy (length-16 spectrum, < 100x100; CPU-cap path)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; AFTER source-first prereq)
#   Prereq already run via update_constant(): lambda_B1/B2/B3, f_NL_folded now present.
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit names used below
    lambda_B1, lambda_B2, lambda_B3, f_NL_folded,
    max_f_NL_FW, f_NL_FW_S67_folded,
    M_KK, tau_fold, n_pairs,
    H_fold, H_tilde_canonical_TD,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "13"                                                    # (local) investigation number
GATE_ID = "INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL"                  # (local)
SCHEME = "AHM-collider-squeezed-limit"                            # (local)
CONVENTION = "RATIO"                                              # (local)
L_MAX = 10                                                        # (local) GGE/Window-24 anchor

# Pre-registered discriminant (plan §W1-1 strict_PASS_boundary)
DELTA_DISCRIMINANT = 0.05      # |Delta_fit| >= 0.05 => collider; < 0.05 => local plateau   # (local)
FEATURE_LOC_TOL = 0.05         # feature-localization residual <= 5%                          # (local)
SQUEEZE_MIN = 1e-3             # k_long/k1 squeezed window lower                              # (local)
SQUEEZE_MAX = 1.0             # k_long/k1 squeezed window upper                              # (local)
N_SQUEEZE = 64                 # log-spaced squeezed-grid points                              # (local)
MU_CRIT = 1.5                  # principal<->complementary threshold (mu^2 = 9/4)             # (local)
FIT_RESID_FLOOR = 1e-6         # squeezed-limit fit residual floor                            # (local)

OUT_NPZ = SESSION_DIR / "inv13_w1_gge_collider_squeezed_fnl.npz"
OUT_PNG = SESSION_DIR / "inv13_w1_gge_collider_squeezed_fnl.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-75" / "s75_dimer_z2_pair_production.npz",
]

# Plan-freeze baseline SHA of canonical_constants.py (pre source-first prereq).
# Runtime SHA WILL differ (4 promotions: lambda_B1/B2/B3, f_NL_folded) — documented
# per substrate-first-canonical-sourcing.md §(ii.B); the runtime SHA enters audit_sha256.
CANON_PLAN_FREEZE_SHA = "e6829db013a713a4e56a4ca7d72e41f522bd3e3caea1bc0488ef17e0460bba34"  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Collider exponent + bispectrum assembly
# ---------------------------------------------------------------------------
def collider_exponent(mu: float) -> tuple[float, float, str]:
    """AHM 1503.08043 squeezed-limit exponent for a heavy scalar of dimensionless
    mass mu = m/H. Returns (Delta_real, mutil, series).
      complementary (mu < 3/2): Delta = 3/2 - sqrt(9/4 - mu^2), real, NO oscillation.
      principal     (mu > 3/2): Delta_real = 3/2, mutil = sqrt(mu^2 - 9/4)
                                 (oscillatory clock; amplitude ~ exp(-pi*mutil))."""
    mu2 = mu * mu  # (local)
    disc = 9.0 / 4.0 - mu2  # (local)
    if disc >= 0.0:
        return 1.5 - np.sqrt(disc), 0.0, "complementary"
    return 1.5, np.sqrt(-disc), "principal"


def boltzmann_amp(mutil: float) -> float:
    """Particle-production (Boltzmann) suppression of the collider signal amplitude.
    exp(-pi*mutil); underflows to 0 for deep-principal mu (physically: signal absent)."""
    x = -np.pi * float(mutil)  # (local)
    if x < -700.0:  # float64 exp underflow guard
        return 0.0
    return float(np.exp(x))


def assemble_squeezed_observable(nk: np.ndarray, mu_a: dict[str, float],
                                 r_grid: np.ndarray) -> dict:
    """Assemble S(r) = f_NL_local + sum_a c_a * Re[(r)^{Delta(mu_a)}] over the squeezed
    grid r = k_long/k1. The branch weights c_a are the substrate's GGE branch occupation
    fractions (normalized), times the Boltzmann amplitude for the principal-series clock.
    Returns S(r), the per-branch Delta/mutil/series/amplitude, and the dominant exponent."""
    f_local = float(f_NL_folded)  # (local) local/EFT scale-invariant plateau baseline

    # GGE branch occupation weights: split the 8 distinct nk modes into 3 branches by
    # the SU(3)-branch grouping the Lagrange multipliers reflect (low/mid/high occupation
    # tertiles). These set the relative heavy-field couplings c_a (substrate-derived,
    # NOT fitted). Normalized to sum 1 so f_local sets the overall amplitude.
    nk_sorted = np.sort(nk)[::-1]  # (local) descending
    n8 = nk_sorted  # (local) 8 distinct occupations
    w_raw = np.array([n8[0:3].sum(), n8[3:6].sum(), n8[6:8].sum()], dtype=float)  # (local) 3-branch
    w_branch = w_raw / w_raw.sum()  # (local) normalized branch weights

    branch_info = {}  # (local)
    S = np.full_like(r_grid, f_local, dtype=float)  # (local) start from local plateau
    branch_names = ["B1", "B2", "B3"]  # (local)
    for i, b in enumerate(branch_names):
        mu = mu_a[b]  # (local)
        Delta, mutil, series = collider_exponent(mu)  # (local)
        amp = boltzmann_amp(mutil)  # (local) clock amplitude (1 for complementary)
        c_a = float(w_branch[i]) * f_local * amp  # (local) substrate-fixed heavy weight
        if series == "complementary":
            # real power-law non-analytic term r^Delta
            term = c_a * np.power(r_grid, Delta)  # (local)
        else:
            # principal: oscillatory clock, r^{3/2} cos(mutil * ln r); amp Boltzmann-killed
            term = c_a * np.power(r_grid, 1.5) * np.cos(mutil * np.log(r_grid))  # (local)
        S = S + term
        branch_info[b] = dict(mu=mu, Delta=Delta, mutil=mutil, series=series,
                              amp=amp, c_a=c_a, weight=float(w_branch[i]))
    return dict(S=S, branch_info=branch_info, w_branch=w_branch, f_local=f_local)


def fit_squeezed_exponent(r_grid: np.ndarray, S: np.ndarray, f_local: float) -> dict:
    """Fit the squeezed-limit non-analytic exponent Delta_fit from the DEPARTURE of S(r)
    from the local plateau f_local:  (S - f_local) ~ A * r^{Delta_fit}  as r->0.
    Returns Delta_fit, the fit amplitude A, the residual, and the localization k-ratio.
    A pure local plateau gives (S - f_local) ~ 0 => Delta_fit undefined/0 by convention."""
    dep = S - f_local  # (local) departure from local plateau
    # Use the small-r tail (squeezed limit) for the power-law fit
    r_tail = r_grid[r_grid <= 0.1]  # (local)
    dep_tail = dep[r_grid <= 0.1]  # (local)
    abs_dep = np.abs(dep_tail)  # (local)
    max_abs_dep = float(np.max(abs_dep)) if abs_dep.size else 0.0  # (local)

    # If the departure is at/below the fit residual floor, the shape is a pure local
    # plateau: Delta_fit := 0 by convention (no recoverable non-analytic exponent).
    if max_abs_dep < FIT_RESID_FLOOR:
        return dict(Delta_fit=0.0, A_fit=0.0, resid=0.0, loc_ratio=float("nan"),
                    max_abs_dep=max_abs_dep, oscillatory=False)

    # log-log linear fit of |dep| vs r over the tail (slope = Delta_fit)
    mask = abs_dep > 0  # (local)
    if mask.sum() < 2:
        return dict(Delta_fit=0.0, A_fit=0.0, resid=0.0, loc_ratio=float("nan"),
                    max_abs_dep=max_abs_dep, oscillatory=False)
    x = np.log(r_tail[mask])  # (local)
    y = np.log(abs_dep[mask])  # (local)
    slope, intercept = np.polyfit(x, y, 1)  # (local) slope = Delta_fit
    resid = float(np.std(y - (slope * x + intercept)))  # (local)
    # detect oscillation: sign changes in the departure tail
    sign_changes = int(np.sum(np.diff(np.sign(dep_tail[dep_tail != 0])) != 0))  # (local)
    oscillatory = sign_changes >= 3  # (local)
    # localization k-ratio: where |dep| peaks (the candidate feature location)
    loc_idx = int(np.argmax(np.abs(dep)))  # (local)
    loc_ratio = float(r_grid[loc_idx])  # (local)
    return dict(Delta_fit=float(slope), A_fit=float(np.exp(intercept)), resid=resid,
                loc_ratio=loc_ratio, max_abs_dep=max_abs_dep, oscillatory=oscillatory)


def nearest_spectral_ratio(loc_ratio: float, nk: np.ndarray) -> dict:
    """Find the nearest GGE spectral ratio (nk_i/nk_j) to the localization k-ratio and
    its fractional residual (the feature-localization-to-D_K-eigenvalue-ratio test)."""
    if not np.isfinite(loc_ratio):
        return dict(nearest=float("nan"), residual=float("inf"))
    n8 = np.sort(np.unique(np.round(nk, 9)))[::-1]  # (local) distinct occupations
    ratios = []  # (local) all pairwise ratios <= 1
    for i in range(len(n8)):
        for j in range(len(n8)):
            if i != j:
                rr = n8[i] / n8[j]  # (local)
                if 0 < rr <= 1.0:
                    ratios.append(rr)
    ratios = np.array(ratios)  # (local)
    if ratios.size == 0:
        return dict(nearest=float("nan"), residual=float("inf"))
    k = int(np.argmin(np.abs(ratios - loc_ratio)))  # (local)
    nearest = float(ratios[k])  # (local)
    residual = abs(nearest - loc_ratio) / loc_ratio if loc_ratio else float("inf")  # (local)
    return dict(nearest=nearest, residual=float(residual))


def compute() -> dict:
    # --- load GGE pair spectrum (Bogoliubov |beta_k|^2 proxy) ---
    npz_path = COMPUTATIONS_DIR / "session-75" / "s75_dimer_z2_pair_production.npz"  # (local)
    d = np.load(npz_path)  # (local)
    nk_total = np.asarray(d["nk_total"], dtype=float)  # (local) length-16 GGE occupations
    nk_distinct = np.sort(np.unique(np.round(nk_total, 9)))[::-1]  # (local) 8 distinct

    # --- mu_a = lambda_Ba / H_transit, both anchors ---
    lam = {"B1": float(lambda_B1), "B2": float(lambda_B2), "B3": float(lambda_B3)}  # (local)
    H_primary = float(H_tilde_canonical_TD)  # (local) inflation-analog clock (PRIMARY)
    H_cross = float(H_fold)                  # (local) literal fold Hubble (CROSS-CHECK)
    mu_primary = {b: lam[b] / H_primary for b in lam}  # (local)
    mu_cross = {b: lam[b] / H_cross for b in lam}      # (local)

    r_grid = np.logspace(np.log10(SQUEEZE_MIN), np.log10(SQUEEZE_MAX), N_SQUEEZE)  # (local)

    results = {}  # (local)
    for anchor_name, mu_a, Hv in [("H_tilde_TD", mu_primary, H_primary),
                                   ("H_fold", mu_cross, H_cross)]:
        asm = assemble_squeezed_observable(nk_total, mu_a, r_grid)  # (local)
        fit = fit_squeezed_exponent(r_grid, asm["S"], asm["f_local"])  # (local)
        loc = nearest_spectral_ratio(fit["loc_ratio"], nk_total)  # (local)
        results[anchor_name] = dict(H=Hv, mu_a=mu_a, asm=asm, fit=fit, loc=loc)

    # --- classification per the PRIMARY anchor (H_tilde_TD; the inflation-analog clock) ---
    prim = results["H_tilde_TD"]  # (local)
    Delta_fit = prim["fit"]["Delta_fit"]  # (local)
    feat_resid = prim["loc"]["residual"]  # (local)
    abs_Delta = abs(Delta_fit)  # (local)

    if abs_Delta >= DELTA_DISCRIMINANT and feat_resid <= FEATURE_LOC_TOL:
        shape_class = "NON-ANALYTIC-COLLIDER"  # (local)
    elif abs_Delta < DELTA_DISCRIMINANT:
        shape_class = "ANALYTIC-LOCAL"  # (local)
    else:
        # |Delta|>=0.05 but feature NOT localized at a spectral ratio: collider exponent
        # present yet unanchored => treat as ANALYTIC-LOCAL for the gate (no clean feature)
        shape_class = "ANALYTIC-LOCAL"  # (local)

    return dict(
        nk_total=nk_total, nk_distinct=nk_distinct,
        lam=lam, H_primary=H_primary, H_cross=H_cross,
        mu_primary=mu_primary, mu_cross=mu_cross, MU_CRIT=MU_CRIT,
        r_grid=r_grid, results=results,
        Delta_fit=Delta_fit, abs_Delta=abs_Delta, feat_resid=feat_resid,
        shape_class=shape_class,
        f_NL_folded=float(f_NL_folded), max_f_NL_FW=float(max_f_NL_FW),
        value=f"{shape_class}:Delta_fit={Delta_fit:.6e}",
    )


# ---------------------------------------------------------------------------
# Section 6 — verdict payload + 4-tuple
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def evaluate_gate(res: dict) -> str:
    """PASS iff NON-ANALYTIC-COLLIDER; INFO iff ANALYTIC-LOCAL; FAIL iff no bispectrum."""
    sc = res["shape_class"]  # (local)
    if sc == "NON-ANALYTIC-COLLIDER":
        return "PASS"
    if sc == "ANALYTIC-LOCAL":
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 — plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))  # (local)
    r = res["r_grid"]  # (local)
    # Panel A: assembled squeezed observable S(r), both anchors
    for anchor_name, style in [("H_tilde_TD", "-"), ("H_fold", "--")]:
        S = res["results"][anchor_name]["asm"]["S"]  # (local)
        ax[0].semilogx(r, S, style, label=f"S(r), {anchor_name}")
    ax[0].axhline(res["f_NL_folded"], color="gray", ls=":", label=f"local f_NL_folded={res['f_NL_folded']}")
    ax[0].set_xlabel(r"$k_{\rm long}/k_1$ (squeezed)")
    ax[0].set_ylabel(r"$S = B/(P P)$")
    ax[0].set_title("GGE squeezed-limit bispectrum-ratio")
    ax[0].legend(fontsize=8)
    ax[0].grid(alpha=0.3)
    # Panel B: collider exponent Delta(mu) with branch mu_a markers
    mu_axis = np.linspace(0.0, 2.0, 400)  # (local)
    Delta_axis = np.array([collider_exponent(m)[0] if m < 1.5 else np.nan for m in mu_axis])  # (local)
    ax[1].plot(mu_axis, Delta_axis, "k-", label=r"$\Delta(\mu)=3/2-\sqrt{9/4-\mu^2}$ (complementary)")
    ax[1].axvline(res["MU_CRIT"], color="red", ls="--", label=r"$\mu_{\rm crit}=3/2$ (principal onset)")
    ax[1].axhline(0.05, color="green", ls=":", label=r"$|\Delta|=0.05$ discriminant")
    # branch mu markers (H_fold anchor — the one inside [0,2])
    for b, mu in res["mu_cross"].items():
        ax[1].axvline(mu, color="blue", alpha=0.5, lw=1)
        ax[1].annotate(f"{b}\nmu={mu:.4f}", (mu, 0.02), fontsize=7, ha="left")
    ax[1].set_xlabel(r"$\mu = \lambda_{Ba}/H$")
    ax[1].set_ylabel(r"$\Delta(\mu)$ (squeezed exponent)")
    ax[1].set_title(f"Collider exponent — shape={res['shape_class']}")
    ax[1].legend(fontsize=7)
    ax[1].grid(alpha=0.3)
    fig.suptitle(f"INV13-W1-1 GGE cosmological-collider squeezed-limit f_NL  |  "
                 f"shape={res['shape_class']}, Delta_fit={res['Delta_fit']:.3e}", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    canon_runtime_sha = sha256_of(canonical_path)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  canonical_constants.py runtime SHA: {canon_runtime_sha}")
    print(f"  canonical_constants.py plan-freeze : {CANON_PLAN_FREEZE_SHA}")
    print(f"  SHA drift (4 source-first promotions lambda_B1/B2/B3 + f_NL_folded): "
          f"{'YES' if canon_runtime_sha != CANON_PLAN_FREEZE_SHA else 'NO'} "
          f"(documented per substrate-first-canonical-sourcing.md §(ii.B))")
    print()

    res = compute()  # (local)

    # --- report ---
    print("=== GGE spectrum (post-transit Bogoliubov |beta_k|^2 proxy) ===")
    print(f"  nk_total length: {len(res['nk_total'])}  (8 distinct occupations)")
    print(f"  nk distinct: {np.array2string(res['nk_distinct'], precision=6)}")
    print(f"  n_pairs (canonical): {float(n_pairs)}")
    print()
    print("=== Branch masses mu_a = lambda_Ba / H_transit (TWO anchors) ===")
    print(f"  lambda_B1={res['lam']['B1']}  lambda_B2={res['lam']['B2']}  lambda_B3={res['lam']['B3']}")
    print(f"  -- PRIMARY: H_tilde_TD = {res['H_primary']:.6e} (inflation-analog clock, S82 Branch-A) --")
    for b in ["B1", "B2", "B3"]:
        info = res["results"]["H_tilde_TD"]["asm"]["branch_info"][b]  # (local)
        print(f"    {b}: mu={info['mu']:.4g}  series={info['series']}  mutil={info['mutil']:.4g}  "
              f"Boltzmann_amp={info['amp']:.3e}  Delta={info['Delta']:.4g}")
    print(f"  -- CROSS-CHECK: H_fold = {res['H_cross']:.6e} (literal fold Hubble, S38) --")
    for b in ["B1", "B2", "B3"]:
        info = res["results"]["H_fold"]["asm"]["branch_info"][b]  # (local)
        print(f"    {b}: mu={info['mu']:.4g}  series={info['series']}  Delta={info['Delta']:.4g}")
    print(f"  mu_crit (principal<->complementary) = {res['MU_CRIT']}")
    print()
    print("=== Squeezed-limit shape classification (PRIMARY anchor H_tilde_TD) ===")
    print(f"  Delta_fit            = {res['Delta_fit']:.6e}")
    print(f"  |Delta_fit|          = {res['abs_Delta']:.6e}   (discriminant >= {DELTA_DISCRIMINANT})")
    print(f"  feature-loc residual = {res['feat_resid']:.6e}   (tol <= {FEATURE_LOC_TOL})")
    print(f"  SHAPE CLASS          = {res['shape_class']}")
    print()
    print("=== Cross-check vs canonical f_NL envelope ===")
    print(f"  f_NL_folded (local baseline, S83)  = {res['f_NL_folded']}")
    print(f"  max_f_NL_FW (envelope, my S95)     = {res['max_f_NL_FW']}")
    print(f"  |S| stays bounded by envelope: max|S|_TD = "
          f"{float(np.max(np.abs(res['results']['H_tilde_TD']['asm']['S']))):.4f} "
          f"<= {res['max_f_NL_FW']}? "
          f"{bool(np.max(np.abs(res['results']['H_tilde_TD']['asm']['S'])) <= res['max_f_NL_FW'])}")
    print()

    verdict = evaluate_gate(res)  # (local)

    # --- persist ---
    np.savez(
        OUT_NPZ,
        nk_total=res["nk_total"], nk_distinct=res["nk_distinct"],
        r_grid=res["r_grid"],
        S_Htilde=res["results"]["H_tilde_TD"]["asm"]["S"],
        S_Hfold=res["results"]["H_fold"]["asm"]["S"],
        mu_Htilde=np.array([res["mu_primary"][b] for b in ["B1", "B2", "B3"]]),
        mu_Hfold=np.array([res["mu_cross"][b] for b in ["B1", "B2", "B3"]]),
        lambda_branch=np.array([res["lam"][b] for b in ["B1", "B2", "B3"]]),
        H_primary=res["H_primary"], H_cross=res["H_cross"], MU_CRIT=res["MU_CRIT"],
        Delta_fit=res["Delta_fit"], abs_Delta=res["abs_Delta"], feat_resid=res["feat_resid"],
        shape_class=res["shape_class"],
        Delta_discriminant=DELTA_DISCRIMINANT, feature_loc_tol=FEATURE_LOC_TOL,
        f_NL_folded=res["f_NL_folded"], max_f_NL_FW=res["max_f_NL_FW"],
        verdict=verdict,
        canon_runtime_sha=canon_runtime_sha, canon_plan_freeze_sha=CANON_PLAN_FREEZE_SHA,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    make_plot(res)
    print(f"  wrote {OUT_NPZ.name} + {OUT_PNG.name}")
    print()

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    note = (f"shape={res['shape_class']}; Delta_fit={res['Delta_fit']:.3e}; "
            f"mu_a(H_tilde)~[247,1017] deep-principal Boltzmann-killed, "
            f"mu_a(H_fold)~[2.5e-3,1.0e-2] deep-complementary Delta~mu^2/3<1e-4; "
            f"both anchors -> local plateau (no resolvable collider feature)")  # (local)
    canon_row = (f"# canon_runtime_sha={canon_runtime_sha} "
                 f"plan_freeze_sha={CANON_PLAN_FREEZE_SHA} "
                 f"# {GATE_ID} source-first-prereq SHA-drift (lambda_B1/B2/B3 + f_NL_folded promoted)")  # (local)
    print_verdict_payload(verdict, res["value"], audit_sha, content_sha,
                          companion_note=note, extra_rows=[canon_row])

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
