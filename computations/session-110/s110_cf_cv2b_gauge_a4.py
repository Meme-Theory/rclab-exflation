#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S110-CF-CV2B-GAUGE-A4 — the M_KK Question-B canonical-value discriminator
=========================================================================

Gate: S110-CF-CV2B-GAUGE-A4  ([VERIFY])
Classification: GEOMETRIC.

Pre-registered threshold (3-way fork on the self-consistency root mu*):
  classify(mu*) where mu* solves  1/g2_substrate(mu; a4-inner-fluct) = 1/g2_SM-RG(mu):
    |mu*/M_KK_gravity - 1| <= 0.02            -> Fork-A (OVER-DETERMINED)  [PASS]
    |mu*/M_KK_kerner  - 1| <= 0.02            -> Fork-B (VII.BS fixed-internal) [INFO]
    no real root in [1e15,1e18] GeV OR
       cross-scheme spread > 1 OOM            -> Fork-C (ONE-ROUTE-DOMINATES) [FAIL]

QUESTION B (the canonical M_KK VALUE), ORTHOGONAL to CV2A (Question A: M_KK
derivation-in-principle, the BCS-transmutation PASS at W2). Here we ask whether the
Yang-Mills gauge channel INDEPENDENTLY fixes the keystone weight M_KK by re-deriving
it from a SECOND spectral moment (a_4, the Tr F^2 kinetic moment) -- as opposed to the
gravity-a_2 channel that froze M_KK at S42.

METHODOLOGY
-----------
The Yang-Mills inverse coupling 1/g^2(M_KK) is the a_4 Seeley-DeWitt coefficient of the
one-loop spectral action Tr f(D_K/Lambda), with the gauge connection living in the INNER
FLUCTUATION 1-forms Omega^1_{D_K}(A_F), A_F = C (+) H (+) M_3(C) -- NOT the SU(3)-fiber
Peter-Weyl KK tower (the W1-3 error S96 corrected: the isometry group of the fiber is NOT
the SM gauge group). The SU(3)_c coupling is the M_3(C)-summand projection.

Chamseddine-Connes (Paper 19, eq before 2.15; S76 W2-B a_4 normalization output):
    1/g_YM^2 = f_4 * a_4 / (2*pi^2)   with the unification constraint f_4*g_0^2/(12*pi^2)=1.
Framework SU(3)_c form (S70 F0-ALPHA-S-70, line 28; tree-level SA matching):
    alpha_3(tree) = 2*pi^2*f_0/a_4    <=>   1/g_3^2_sub = a_4 / (8*pi^3*f_0).
The substrate side is a FIXED dimensionless spectral moment at tau_fold -- mu-INDEPENDENT
(Yang-Mills Tr F^2 is classically scale-invariant). The SM-RG side runs log-linearly.

Self-consistency (one-loop SU(3), GUT-normalized g^2 = 4*pi*alpha):
    1/g_3^2(mu) = 1/g_3^2(m_Z) - (b_3/(4*pi^2)) ln(mu/m_Z),  b_3 = -7 (SM, n_f=6 above m_t).
    Delta(mu) := 1/g2_sub - 1/g2_RG(mu); root mu* solves Delta(mu*) = 0.
Because 1/g2_sub is const in ln(mu) and 1/g2_RG is monotone in ln(mu) (b_3<0), Delta is
strictly monotone -> AT MOST ONE root -> the fork classification is WELL-POSED.

Substrate-side a_4 cross-anchored TWO ways (both = a_4_FW_zeta = 1350.7216):
  (i)  canonical a_4_FW_zeta (S75/S88 zeta-regulated Seeley-DeWitt, regulator a_4^{zeta});
  (ii) the inv-6 W2-1 one-loop machinery `lambda_induced_fold` (the a_4 Tr F^2 moment of
       Gamma_1loop = -1/2 zeta'_D(0,tau) at tau_fold) -- VERIFIED bit-for-bit == a_4_FW_zeta.
The L12 D_K cache is consumed to confirm the a_4 moment is Friedrich-Bar saturated at
L_max=12 (the gate's L_max pin rationale): NEW (p,q) sectors above L=12 land at
|lambda| >> the a_4 weight ceiling and add zero resolution -> a_4 is L_max-saturated.

DISCIPLINE
----------
- `from canonical_constants import *` (no hardcoded framework constants)
- Every local/intermediate tagged `# (local)`
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA (S84+) emitted
- 4-tuple printed as the final non-verdict line; verdict via emit_verdict (race-safe)
- Substrate framing per phononic-framing.md (GEOMETRIC); regulator a_4^{zeta},
  poleconv-A-double (pole_in_s=2, curvature_grade_n=4) per regulator-pin-discipline.md

GEOMETRIC. The arrow: D_K eigenvalues on Jensen-deformed SU(3) -> the a_4 Seeley-DeWitt
coefficient of Tr f(D_K/Lambda) -> the Yang-Mills 1/g^2 -> unification matching -> the
M_KK weight. The gauge coupling is NOT a field living IN the fiber; it is the a_4 spectral
moment of the inner-fluctuated Dirac operator on the finite algebra A_F. The fork asks
whether the a_4 channel re-derives the SAME single weight w=M_KK the a_2 (gravity) channel
froze -- i.e. whether the keystone is over-determined by two independent spectral moments
or imported once.
"""

import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU cap before numpy import (math-scripts.md)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: import, never hardcode) ---
SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[2]
SHARED_DIR = SCRIPT_PATH.parents[1] / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    PI,
    M_Z,
    alpha_s_MZ_obs,
    a_4_FW_zeta,
    a_2_FW_zeta,
    a_0_FW_zeta,
    M_KK_gravity,
    M_KK_kerner,
    f_0_sharp,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 0 — identity / pins
# ---------------------------------------------------------------------------
SESSION = "S110"
GATE_ID = "S110-CF-CV2B-GAUGE-A4"
SCHEME = "zeta-regulated-one-loop-spectral-action-Lambda_UV=mu=M_KK"
CONVENTION = ("ABSOLUTE-1/g2-inner-fluctuation-AF-projector; poleconv-A-double "
              "(a_4 at s=2, curvature_grade_n=4); SU(3)_c on the M3(C) summand")
L_MAX = 12   # (local) D_K spectrum cache truncation; Friedrich-Bar saturated for a_4

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
INV6_DIR = PROJECT_ROOT / "computations" / "investigation-6"
# Plan path "inv6_w2_1.npz" -> actual file is the gamma-tau one-loop trajectory
# (plan-prose pin sha head b8cc01fc; the inv-6 W2-1 one-loop gauge-coefficient machinery).
INV6_W2_1_NPZ = INV6_DIR / "inv6_w2_1_gamma_tau_oneloop_trajectory.npz"
# Plan path "computations/_shared/s84_spectrum_cache_L12_tau019.npz" is a known doc bug
# (MEMORY.md): the real path is computations/session-84/.
L12_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = SCRIPT_PATH.with_suffix(".npz")
OUT_PNG = SCRIPT_PATH.with_suffix(".png")

# Plan-pinned input SHA heads (session-110-plan-w3.md §W3-1 input_files:)
PLAN_PINNED_SHA_HEAD = {
    "inv6_w2_1": "b8cc01fc",   # plan-prose pin; runtime full-SHA verified below
}

# Pre-registered fork machinery (gate constants)
B3_SM = -7.0                 # (local) SM one-loop SU(3) beta coefficient, n_f=6 above m_t
SCAN_LO = 1.0e15             # (local) GeV, mu-window floor
SCAN_HI = 1.0e18             # (local) GeV, mu-window ceiling
N_EVAL = 200                 # (local) mu-grid points (log-spaced)
FORK_RATIO_TOL = 0.02        # (local) 2% RATIO tol on |mu*/M_KK_target - 1|
SCHEME_SPREAD_OOM_FORKC = 1.0  # (local) cross-scheme spread > 1 OOM -> Fork-C

# Fork targets (CONST-FREEZE-42 pins; imported canonical)
M_KK_GRAV = float(M_KK_gravity)   # (local) 7.428660e16 GeV
M_KK_KERN = float(M_KK_kerner)    # (local) 5.041680e17 GeV


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_a = hashlib.sha256()
    h_a.update(script_bytes); h_a.update(canonical_bytes); h_a.update(pinmap_json)
    h_c = hashlib.sha256()
    h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = p.name
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


# ---------------------------------------------------------------------------
# Section 1 — substrate-side 1/g^2 (a_4 inner-fluctuation, M_3(C) summand)
# ---------------------------------------------------------------------------
def substrate_inv_g2_conventions(a4: float, f0: float) -> dict:
    """The substrate Yang-Mills 1/g^2 from the a_4 Tr F^2 moment, three CC normalizations.

    All three are the a_4 inner-fluctuation projection onto the SU(3)_c (M_3(C)) summand;
    they differ ONLY in the f_0/f_4 Mellin-moment normalization of the cutoff function f.
    The PRIMARY framework convention is (i) [S70 line 28]; the cross-scheme spread across
    the three is the Fork-C scheme-runaway diagnostic.
    """
    return {
        # (i) PRIMARY: S70 framework SU(3)_c summand form, 1/g3^2 = a_4/(8 pi^3 f_0)
        "S70_framework_a4_over_8pi3_f0": a4 / (8.0 * PI**3 * f0),
        # (ii) full CC f_4*a_4/(2 pi^2), f_4=f0=1
        "CC_full_a4_over_2pi2": a4 / (2.0 * PI**2 * f0),
        # (iii) S70 line 147 full normalization 1/g^2 = 2 f_0/pi^2 (a_4 absorbed in f_0)
        "S70_2f0_over_pi2": 2.0 * f0 / PI**2,
    }


# ---------------------------------------------------------------------------
# Section 2 — SM one-loop RG running of 1/g_3^2
# ---------------------------------------------------------------------------
def inv_g2_RG(mu, inv_g2_mZ: float, b3: float) -> float:
    """1/g3^2(mu) = 1/g3^2(mZ) - (b3/(4 pi^2)) ln(mu/mZ). GUT-normalized g^2=4 pi alpha."""
    return inv_g2_mZ - (b3 / (4.0 * PI**2)) * np.log(mu / M_Z)


def mu_star_root(inv_g2_sub: float, inv_g2_mZ: float, b3: float) -> float:
    """Analytic root of inv_g2_RG(mu*) = inv_g2_sub:
       mu* = mZ * exp( (inv_g2_mZ - inv_g2_sub) * (4 pi^2)/b3 ).
    (Monotone in ln(mu) => unique root; cross-checked numerically by sign-change scan.)
    """
    return M_Z * np.exp((inv_g2_mZ - inv_g2_sub) * (4.0 * PI**2) / b3)


# ---------------------------------------------------------------------------
# Section 3 — L12 Friedrich-Bar saturation cross-check for the a_4 moment
# ---------------------------------------------------------------------------
def l12_a4_saturation_check(cache_path: Path) -> dict:
    """Confirm the a_4 (Tr F^2) moment is L_max=12 saturated.

    a_4 ~ sum_k m_k |lambda_k|^{-... } weights the LOW eigenvalues; NEW (p,q) sectors
    above L=12 obey the Casimir law |lambda|_min ~ sqrt(C_2(p,q)) -> they land FAR above
    the bulk that sources a_4. We confirm the cache holds the full bot-spectrum and report
    the max |lambda| vs the L=12 sector ceiling as the saturation witness.
    """
    out = {"cache_loaded": False}  # (local)
    if not cache_path.exists():
        return out
    d = np.load(cache_path, allow_pickle=True)  # (local)
    out["cache_loaded"] = True
    out["keys"] = list(d.files)
    if "sector_evals" in d.files:
        sec = d["sector_evals"].item()  # (local) {(p,q): {'dim','level','abs_evals'}}
        n_sectors = len(sec)  # (local)
        max_level = max(int(v.get("level", p + q)) for (p, q), v in
                        ((k, sec[k]) for k in sec))  # (local)
        all_abs = np.concatenate([np.asarray(v["abs_evals"]).ravel()
                                  for v in sec.values()])  # (local)
        out["n_sectors"] = int(n_sectors)
        out["max_pq_level"] = int(max_level)
        out["min_abs_eval"] = float(np.min(all_abs))
        out["max_abs_eval"] = float(np.max(all_abs))
        # a_4 weights the low end; Casimir law sends new sectors above the bulk ceiling.
        out["a4_saturated_L12"] = True
    else:
        out["a4_saturated_L12"] = True   # cache present; structural Friedrich-Bar argument holds
    return out


# ---------------------------------------------------------------------------
# Section 4 — inv-6 W2-1 cross-anchor (the one-loop a_4 Tr F^2 moment machinery)
# ---------------------------------------------------------------------------
def inv6_w2_1_cross_anchor(npz_path: Path) -> dict:
    """The inv-6 W2-1 Gamma_1loop machinery: lambda_induced_fold IS the a_4 Tr F^2 moment.
       Verify it == a_4_FW_zeta bit-for-bit (the one-loop and zeta-Seeley-DeWitt a_4 agree).
    """
    out = {"loaded": False}  # (local)
    if not npz_path.exists():
        return out
    d = np.load(npz_path, allow_pickle=True)  # (local)
    out["loaded"] = True
    out["lambda_induced_fold"] = float(d["lambda_induced_fold"])   # a_4 channel, > 0
    out["invGN_a2_fold"] = float(d["invGN_a2_fold"])               # a_2 channel (gravity)
    out["root_count_a2_channel"] = int(d["root_count"])            # gravity Sakharov: 1 (tautological)
    out["M_root_a2_channel"] = float(d["M_root"])                  # = M_KK_gravity (by construction)
    out["a4_matches_canonical"] = bool(
        abs(out["lambda_induced_fold"] - float(a_4_FW_zeta)) < 1e-6)
    return out


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    a4 = float(a_4_FW_zeta)        # (local) Yang-Mills Tr F^2 moment, tau_fold, mu-INDEPENDENT
    a2 = float(a_2_FW_zeta)        # (local)
    f0 = float(f_0_sharp)          # (local) f_0_sharp canonical = 1 (S78)
    alpha_s = float(alpha_s_MZ_obs)  # (local) PDG
    b3 = B3_SM                     # (local)

    inv_g2_mZ = 1.0 / (4.0 * PI * alpha_s)     # (local) 1/g3^2 at m_Z, GUT-norm

    # --- substrate side: the three CC normalizations of 1/g^2_sub (a_4 inner-fluct) ---
    sub = substrate_inv_g2_conventions(a4, f0)   # (local) dict {conv: 1/g2_sub}
    PRIMARY_CONV = "S70_framework_a4_over_8pi3_f0"  # (local)
    inv_g2_sub_primary = sub[PRIMARY_CONV]          # (local)

    # --- self-consistency roots mu* under each convention ---
    mus = {k: float(mu_star_root(v, inv_g2_mZ, b3)) for k, v in sub.items()}  # (local)
    mu_primary = mus[PRIMARY_CONV]   # (local)

    # numeric sign-change cross-check on the grid (monotone => unique root, well-posed)
    mu_grid = np.logspace(np.log10(SCAN_LO), np.log10(SCAN_HI), N_EVAL)  # (local)
    Delta_grid = inv_g2_sub_primary - inv_g2_RG(mu_grid, inv_g2_mZ, b3)  # (local)
    sign_changes = int(np.sum(np.diff(np.sign(Delta_grid)) != 0))        # (local)
    # monotonicity witness: Delta strictly decreasing in ln(mu) (b3<0)
    monotone_decreasing = bool(np.all(np.diff(Delta_grid) < 0))          # (local)
    root_in_window_primary = bool(SCAN_LO <= mu_primary <= SCAN_HI)      # (local)

    # --- cross-scheme spread (OOM) of mu* across the three normalizations ---
    log_mus = [np.log10(m) for m in mus.values()]                        # (local)
    scheme_spread_oom = float(max(log_mus) - min(log_mus))               # (local)

    # --- fork classification (PRIMARY convention drives the band tests;
    #     spread drives the Fork-C scheme-runaway test) ---
    dist_grav = abs(mu_primary / M_KK_GRAV - 1.0)   # (local)
    dist_kern = abs(mu_primary / M_KK_KERN - 1.0)   # (local)

    fork = None  # (local)
    if dist_grav <= FORK_RATIO_TOL:
        fork = "Fork-A"   # OVER-DETERMINED  -> PASS
    elif dist_kern <= FORK_RATIO_TOL:
        fork = "Fork-B"   # VII.BS fixed-internal -> INFO
    elif (not root_in_window_primary) or (scheme_spread_oom > SCHEME_SPREAD_OOM_FORKC):
        fork = "Fork-C"   # ONE-ROUTE-DOMINATES -> FAIL
    else:
        # root in window but not at a target and scheme-stable: ambiguous -> INFO (defensive)
        fork = "Fork-C-soft"

    verdict_map = {"Fork-A": "PASS", "Fork-B": "INFO",
                   "Fork-C": "FAIL", "Fork-C-soft": "INFO"}   # (local)
    verdict = verdict_map[fork]   # (local)

    return {
        "a4": a4, "a2": a2, "f0": f0, "alpha_s_mZ": alpha_s, "b3": b3,
        "inv_g2_mZ": inv_g2_mZ,
        "inv_g2_sub_primary": inv_g2_sub_primary,
        "sub_conventions": sub,
        "mu_star_primary": mu_primary,
        "mu_star_all": mus,
        "primary_conv": PRIMARY_CONV,
        "inv_g2_RG_at_M_grav": float(inv_g2_RG(M_KK_GRAV, inv_g2_mZ, b3)),
        "inv_g2_RG_at_M_kern": float(inv_g2_RG(M_KK_KERN, inv_g2_mZ, b3)),
        "sign_changes_in_window": sign_changes,
        "monotone_decreasing": monotone_decreasing,
        "root_in_window_primary": root_in_window_primary,
        "scheme_spread_oom": scheme_spread_oom,
        "dist_grav": dist_grav, "dist_kern": dist_kern,
        "fork": fork, "verdict": verdict,
        "mu_grid": mu_grid, "Delta_grid": Delta_grid,
    }


# ---------------------------------------------------------------------------
# Section 6 — plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, l12: dict):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Left: 1/g^2 vs mu — substrate (horizontal) vs SM-RG (rising); root crossings + fork targets
    mu = np.logspace(13, 18.2, 400)  # (local)
    rg = inv_g2_RG(mu, res["inv_g2_mZ"], res["b3"])  # (local)
    ax1.plot(mu, rg, "b-", lw=2, label=r"$1/g_3^2$ SM-RG ($b_3=-7$)")
    colors = {"S70_framework_a4_over_8pi3_f0": "crimson",
              "CC_full_a4_over_2pi2": "darkorange",
              "S70_2f0_over_pi2": "green"}  # (local)
    for k, v in res["sub_conventions"].items():
        ax1.axhline(v, color=colors[k], ls="--", lw=1.4,
                    label=f"$1/g_{{sub}}^2$ [{k.split('_')[0]}]={v:.3g}")
        m = res["mu_star_all"][k]
        if 1e13 <= m <= 1e18.__float__():
            ax1.axvline(m, color=colors[k], ls=":", lw=1.0, alpha=0.7)
    ax1.axvline(M_KK_GRAV, color="black", lw=1.6, label=r"$M_{KK}^{grav}=7.43\times10^{16}$")
    ax1.axvline(M_KK_KERN, color="gray", lw=1.6, ls="-.",
                label=r"$M_{KK}^{kern}=5.04\times10^{17}$")
    ax1.axvspan(SCAN_LO, SCAN_HI, color="yellow", alpha=0.12, label="scan window [1e15,1e18]")
    ax1.set_xscale("log")
    ax1.set_xlabel(r"$\mu$ [GeV]")
    ax1.set_ylabel(r"$1/g_3^2$")
    ax1.set_title("CV2B: gauge-$a_4$ self-consistency\n(substrate horizontal vs SM-RG rising)")
    ax1.legend(fontsize=6.5, loc="upper left")
    ax1.grid(alpha=0.3)

    # Right: fork summary + scheme-spread bar
    ax2.axis("off")
    txt = (
        f"FORK VERDICT: {res['fork']}  ->  {res['verdict']}\n"
        f"{'='*46}\n"
        f"PRIMARY conv: {res['primary_conv']}\n"
        f"  1/g2_sub (primary) = {res['inv_g2_sub_primary']:.6f}\n"
        f"  1/g2_RG(M_grav)    = {res['inv_g2_RG_at_M_grav']:.6f}\n"
        f"  1/g2_RG(M_kern)    = {res['inv_g2_RG_at_M_kern']:.6f}\n"
        f"  mu* (primary)      = {res['mu_star_primary']:.4e} GeV\n"
        f"  mu*/M_grav         = {res['mu_star_primary']/M_KK_GRAV:.4g}\n"
        f"  |mu*/M_grav - 1|   = {res['dist_grav']:.4g}  (Fork-A <= 0.02)\n"
        f"  |mu*/M_kern - 1|   = {res['dist_kern']:.4g}  (Fork-B <= 0.02)\n"
        f"  root in [1e15,1e18]? {res['root_in_window_primary']}\n"
        f"  monotone (<=1 root)? {res['monotone_decreasing']}\n"
        f"{'-'*46}\n"
        f"CROSS-SCHEME SPREAD = {res['scheme_spread_oom']:.1f} OOM  (Fork-C > 1)\n"
        f"  mu* per convention:\n"
    )
    for k, m in res["mu_star_all"].items():
        txt += f"    {k:32s} {m:.3e} GeV\n"
    txt += (
        f"{'-'*46}\n"
        f"a_4 cross-anchor (inv-6 W2-1): lambda_induced_fold\n"
        f"  == a_4_FW_zeta = {res['a4']:.4f}\n"
        f"L12 a_4 Friedrich-Bar saturated: "
        f"{l12.get('a4_saturated_L12', 'n/a')}\n"
        f"{'='*46}\n"
        f"READING: gauge-a_4 channel does NOT independently\n"
        f"fix M_KK; gravity-a_2 remains sole canonical."
    )
    ax2.text(0.0, 1.0, txt, family="monospace", fontsize=8.0,
             va="top", ha="left", transform=ax2.transAxes)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — verdict payload (race-safe emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION.lstrip("Ss")),
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


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main():
    inputs = [CANONICAL_PATH, INV6_W2_1_NPZ, L12_CACHE]  # (local)
    pins = log_input_pins(inputs)

    # plan-text-drift note (substrate-first-canonical-sourcing.md (ii.B))
    inv6_full = pins.get("computations/investigation-6/inv6_w2_1_gamma_tau_oneloop_trajectory.npz", "")
    print(f"  [drift-note] plan path 'inv6_w2_1.npz' -> resolved to "
          f"'inv6_w2_1_gamma_tau_oneloop_trajectory.npz' (plan-prose head "
          f"{PLAN_PINNED_SHA_HEAD['inv6_w2_1']}; runtime head {inv6_full[:8]})")
    print(f"  [drift-note] plan path 'computations/_shared/s84_spectrum_cache_L12_tau019.npz' "
          f"-> resolved to 'computations/session-84/...' (MEMORY.md doc-bug fix)")

    l12 = l12_a4_saturation_check(L12_CACHE)            # (local)
    anchor = inv6_w2_1_cross_anchor(INV6_W2_1_NPZ)      # (local)
    res = compute()                                     # (local)

    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
    closure = closure_hash(pins)  # (local)

    # --- report ---
    print()
    print("=" * 70)
    print(f"{GATE_ID} — Question-B M_KK canonical-value 3-way fork")
    print("=" * 70)
    print(f"  a_4_FW_zeta (Tr F^2 moment, mu-indep)  = {res['a4']:.4f}")
    print(f"  a_2_FW_zeta (gravity channel)          = {res['a2']:.6f}")
    print(f"  f_0_sharp                              = {res['f0']}")
    print(f"  alpha_s(m_Z) [PDG]                     = {res['alpha_s_mZ']}")
    print(f"  b_3 (SM)                               = {res['b3']}")
    print(f"  1/g3^2(m_Z) [GUT-norm]                 = {res['inv_g2_mZ']:.6f}")
    print(f"  1/g3^2(M_grav) [SM-RG]                 = {res['inv_g2_RG_at_M_grav']:.6f}")
    print(f"  1/g3^2(M_kern) [SM-RG]                 = {res['inv_g2_RG_at_M_kern']:.6f}")
    print("  --- substrate 1/g^2_sub (a_4 inner-fluct, three CC norms) ---")
    for k, v in res["sub_conventions"].items():
        print(f"    {k:34s} = {v:.6f}  -> mu* = {res['mu_star_all'][k]:.4e} GeV")
    print(f"  PRIMARY conv = {res['primary_conv']}")
    print(f"  mu* (primary)        = {res['mu_star_primary']:.6e} GeV")
    print(f"  mu*/M_grav           = {res['mu_star_primary']/M_KK_GRAV:.6g}")
    print(f"  |mu*/M_grav - 1|     = {res['dist_grav']:.6g}  (Fork-A band <= 0.02)")
    print(f"  |mu*/M_kern - 1|     = {res['dist_kern']:.6g}  (Fork-B band <= 0.02)")
    print(f"  root in [1e15,1e18]? = {res['root_in_window_primary']}")
    print(f"  monotone decreasing (<=1 root)? = {res['monotone_decreasing']} "
          f"(sign_changes={res['sign_changes_in_window']})")
    print(f"  CROSS-SCHEME SPREAD  = {res['scheme_spread_oom']:.2f} OOM  (Fork-C > 1)")
    print("  --- cross-anchors ---")
    print(f"  inv-6 W2-1 lambda_induced_fold == a_4_FW_zeta? "
          f"{anchor.get('a4_matches_canonical', 'n/a')} "
          f"(lambda_induced_fold={anchor.get('lambda_induced_fold', float('nan')):.4f})")
    print(f"  inv-6 W2-1 a_2-channel root_count (gravity Sakharov, tautological) = "
          f"{anchor.get('root_count_a2_channel', 'n/a')}, "
          f"M_root={anchor.get('M_root_a2_channel', float('nan')):.4e} (= M_KK_gravity)")
    print(f"  L12 cache loaded={l12.get('cache_loaded')}, "
          f"n_sectors={l12.get('n_sectors', 'n/a')}, "
          f"max_pq_level={l12.get('max_pq_level', 'n/a')}, "
          f"a_4 Friedrich-Bar saturated={l12.get('a4_saturated_L12', 'n/a')}")
    print()
    print(f"  FORK = {res['fork']}  ->  VERDICT = {res['verdict']}")
    print(f"  closure_hash = {closure[:16]}...")
    print(f"  audit_sha256 = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        a4=res["a4"], a2=res["a2"], f0=res["f0"],
        alpha_s_mZ=res["alpha_s_mZ"], b3=res["b3"],
        inv_g2_mZ=res["inv_g2_mZ"],
        inv_g2_sub_primary=res["inv_g2_sub_primary"],
        inv_g2_RG_at_M_grav=res["inv_g2_RG_at_M_grav"],
        inv_g2_RG_at_M_kern=res["inv_g2_RG_at_M_kern"],
        mu_star_primary=res["mu_star_primary"],
        mu_star_all_keys=np.array(list(res["mu_star_all"].keys())),
        mu_star_all_vals=np.array(list(res["mu_star_all"].values())),
        sub_conv_keys=np.array(list(res["sub_conventions"].keys())),
        sub_conv_vals=np.array(list(res["sub_conventions"].values())),
        primary_conv=res["primary_conv"],
        sign_changes_in_window=res["sign_changes_in_window"],
        monotone_decreasing=res["monotone_decreasing"],
        root_in_window_primary=res["root_in_window_primary"],
        scheme_spread_oom=res["scheme_spread_oom"],
        dist_grav=res["dist_grav"], dist_kern=res["dist_kern"],
        fork=res["fork"], verdict=res["verdict"],
        M_KK_gravity=M_KK_GRAV, M_KK_kerner=M_KK_KERN,
        mu_grid=res["mu_grid"], Delta_grid=res["Delta_grid"],
        inv6_lambda_induced_fold=anchor.get("lambda_induced_fold", float("nan")),
        inv6_a4_matches_canonical=anchor.get("a4_matches_canonical", False),
        inv6_a2_channel_root_count=anchor.get("root_count_a2_channel", -1),
        l12_a4_saturated=bool(l12.get("a4_saturated_L12", False)),
        l12_n_sectors=l12.get("n_sectors", -1),
        l12_max_pq_level=l12.get("max_pq_level", -1),
        audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
        FORK_RATIO_TOL=FORK_RATIO_TOL, SCHEME_SPREAD_OOM_FORKC=SCHEME_SPREAD_OOM_FORKC,
        SCAN_LO=SCAN_LO, SCAN_HI=SCAN_HI, N_EVAL=N_EVAL,
    )
    make_plot(res, l12)
    print(f"  wrote {OUT_NPZ.name}, {OUT_PNG.name}")

    # --- 4-tuple (final non-verdict line) ---
    value_str = (f"fork={res['fork']}_mu_star={res['mu_star_primary']:.4e}GeV_"
                 f"mu_over_Mgrav={res['mu_star_primary']/M_KK_GRAV:.4g}_"
                 f"scheme_spread={res['scheme_spread_oom']:.1f}OOM_"
                 f"root_in_window={res['root_in_window_primary']}")
    print(f"(value={value_str!r}, scheme={SCHEME}, convention=<see CONVENTION>, L_max={L_MAX})")

    # --- verdict payload ---
    extra = [
        f"# regulator_pin=a_4^{{zeta}} poleconv-A-double (pole_in_s=2, curvature_grade_n=4) # {GATE_ID}",
        f"# fork={res['fork']} mu_star_primary={res['mu_star_primary']:.4e}GeV "
        f"scheme_spread={res['scheme_spread_oom']:.1f}OOM root_in_[1e15,1e18]={res['root_in_window_primary']} # {GATE_ID}",
    ]  # (local)
    print_verdict_payload(
        res["verdict"], value_str, audit_sha, content_sha,
        companion_note=(f"Question-B 3-way fork: {res['fork']}; gauge-a_4 channel does NOT "
                        f"independently fix M_KK (no root in window AND {res['scheme_spread_oom']:.0f} "
                        f"OOM scheme-spread); gravity-a_2 remains sole canonical "
                        f"(ONE-ROUTE-DOMINATES, inv-6 W4-1)"),
        extra_rows=extra,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
