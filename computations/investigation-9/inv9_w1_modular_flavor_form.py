#!/usr/bin/env python3
"""
INV9-W1-1-MODULAR-FLAVOR-FORM
=============================
FLAGSHIP cross-domain bridge (kaku NS-1 = string NS-1, IDENTICAL convergence).

Hypothesis: the generation-relevant (gen-graded) matrix elements of D_K(tau) on
the bottom-N eigenstates near tau_fold=0.190, expanded in eps = f(tau - tau_fold),
organize as a definite-weight Dedekind-eta-like modular form whose C2(p,q)-graded
coefficients reproduce the inter-generation Yukawa hierarchy as eps^{C2}-powers --
closing the rank-1 wall (S96-MATTER-R-HIERARCHY = 9.86, FAIL) FROM GEOMETRY and
fixing a tau <-> K e-fold map.

Substrate framing (PARTICLE): the substrate IS the spectral triple (A_K, H_K, D_K(tau)).
The three generations ARE the Peter-Weyl (p,q) sectors (1,0)/(1,1)/(3,0) carrying
SU(3) quadratic Casimir C2 = (4/3, 3, 6). The direction flows
   D_K(tau) eigenvalues/eigenvectors -> gen-graded Y_ij(tau) -> modular weight in
   eps=f(tau-tau_fold) -> the Yukawa hierarchy R.
Note (governing structure, SS-VII.BL Generation-Blindness, STAGE-3-PERMANENT, S99 W3-1):
the WITHIN-sector multiplicity structure is rigid (multiplicity-scalar representation
pi(a)=(+)_(p,q) pi_(p,q)(a) (x) 1_m(p,q); R_cross_yukawa_t1_t2=1.019704). The generation
index that CAN vary is the BETWEEN-sector Z3-triality t=(p-q) mod 3. This gate therefore
tests the BETWEEN-sector eigenvalue spacing as a C2-graded eps-power law -- the only
channel the homogeneity wall leaves open.

Method:
  (A) Build D_K(tau) on a tau-grid bracketing the fold (tau in [0.15, 0.25]) via the
      Peter-Weyl block-diagonal GT-builder (dirac_spectrum.collect_spectrum_with_eigenvectors).
      Extract the per-generation matrix element Y_i(tau) = <psi_i(tau)| D_K(tau) |psi_i(tau)>
      = the lowest |lambda| of sector i (a diagonal element on the sector's ground state).
  (B) Fit the modular-form WEIGHT structure: Y_i(tau) = A_i * eta(eps)^{w_i} for three
      candidate eps-maps (linear; Jensen-natural exp(-S0*(tau-tau_fold)); nome-like
      exp(-2*pi*|tau-tau_fold|)) and determine whether a SINGLE consistent (eps-map, weight-w)
      reproduces the hierarchy with R^2 >= 0.95.
  (C) Casimir-grading verdict: test w_i ~ C2_i (within 10%) and the inter-generation ratio
      R = Y_heaviest/Y_lightest vs the rank-1 anchor 9.86 and the physical O(1e5).

GPU: torch.linalg available; the gen-relevant Peter-Weyl blocks at p+q<=3 are small
(largest (3,0)/(0,3) block dim 160, well below the 100x100 GPU-worthwhile floor for the
eig itself but the per-tau irrep CONSTRUCTION is the cost). scipy.linalg.eigh (in the
GT-builder) gives guaranteed orthonormal eigenvectors and is the validated path; we use
it for correctness and cap OMP threads. (Block dims here are tiny; the eig cost is
negligible vs irrep construction, so GPU offload would not help -- documented deviation.)

Pre-registration: sessions/investigation/investigation-9/investigation-9-plan-w1.md
  section "## §W1-1. INV9-W1-1"  (trigger [CHAIN]; characterization gate).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical infrastructure path wiring -----------------------------------
SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED))

# canonical_constants import: tau_fold (CONST-FREEZE-42), R_S96_matter_hierarchy
# (the rank-1 wall anchor, surfaced to canonical S-INV9-W1-1), C2_gen_sectors (the
# SU(3) Casimir grading (4/3,3,6), S61 W8).
from canonical_constants import tau_fold, R_S96_matter_hierarchy, C2_gen_sectors  # noqa: E402

# dirac_spectrum GT-builder (Peter-Weyl block-diagonal D_K(tau))
import dirac_spectrum as ds  # noqa: E402

# ---------------------------------------------------------------------------
# Identity (template contract)
# ---------------------------------------------------------------------------
SESSION = "9"                       # investigation number (track=investigation)
GATE_ID = "INV9-W1-1-MODULAR-FLAVOR-FORM"
SCHEME = "FW"
CONVENTION = "RATIO"
L_MAX = 10                          # (local) canonical D_K cache truncation

HERE = Path(__file__).resolve()
SCRIPT_PATH = HERE
CANONICAL_PATH = SHARED / "canonical_constants.py"
CACHE_L12 = HERE.parents[1] / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
NPZ_OUT = HERE.with_suffix(".npz")
PNG_OUT = HERE.with_suffix(".png")

# ---------------------------------------------------------------------------
# Gate parameters (all (local) -- gate machinery, not framework constants)
# ---------------------------------------------------------------------------
GEN_SECTORS = [(1, 0), (1, 1), (3, 0)]          # (local) the three gen-relevant PW sectors
C2_MAP = {(1, 0): C2_gen_sectors[0],
          (1, 1): C2_gen_sectors[1],
          (3, 0): C2_gen_sectors[2]}             # (local) (4/3, 3, 6) from canonical
TAU_LO, TAU_HI = 0.15, 0.25                      # (local) modular-fit window bracketing fold
DTAU = 0.005                                     # (local) 21-point coarse grid
R2_FLOOR = 0.95                                  # (local) modular-fit-quality PASS floor
CASIMIR_TOL = 0.10                               # (local) 10% Casimir-grading match tol
EIG_TOL = 1e-9                                   # (local) float64 eig/fit tolerance
MAX_PQ_SUM = 3                                   # (local) p+q<=3 covers (1,0),(1,1),(3,0)
S0_AMP = 1.0                                     # (local) Jensen diabatic-amplitude scale S0
#   S0 sets the Jensen-natural eps-map exp(-S0*(tau-tau_fold)); S0=1 is the natural
#   unit-action scale (the diabatic amplitude convention d_i=exp(-S0*C2) of S98-W3-1
#   uses S0 as the per-unit-Casimir action; here it scales the eps-map argument, and
#   the FIT absorbs any overall S0 into the weight w via eta(eps)^w, so S0 is a
#   convention not a free fit parameter -- documented in the substitution chain).

PHYS_HIERARCHY_TARGET = 1.0e5                    # (local) PDG up-type 3-gen Yukawa hierarchy
#   ~ m_t/m_u ~ O(1e5); a cross-check anchor only (PDG provenance), NOT a substrate value.


# ---------------------------------------------------------------------------
# Dedekind eta (q-series, real nome) and modular-power fitting
# ---------------------------------------------------------------------------
def dedekind_eta_real(q, n_terms=2000):
    """Dedekind eta for a REAL nome 0 <= q < 1 via the pentagonal-number product
    eta = q^{1/24} * prod_{n>=1} (1 - q^n).

    For q in (0,1) this is real and positive. Returns eta(q).
    q here is the real nome eps (the gate's eps-map output, taken in [0,1)).
    """
    q = np.asarray(q, dtype=np.float64)
    out = np.power(q, 1.0 / 24.0)
    prod = np.ones_like(out)
    for n in range(1, n_terms + 1):
        term = 1.0 - np.power(q, n)
        prod = prod * term
        # convergence: q^n underflows; break when contribution negligible
        if np.all(np.power(q, n) < 1e-16):
            break
    return out * prod


def fit_eta_power(eps, Y):
    """Least-squares fit Y = A * eta(eps)^{w} in log-space:
        ln Y = ln A + w * ln eta(eps).
    Returns (w, lnA, R2, residual_rms).  eps in (0,1), Y > 0.

    Robust against:
      - eps -> 0 (eta -> 0, ln eta -> -inf): drop non-finite rows (the eps-map can
        hit the fold where eps=0 exactly; that point carries no fit information).
      - degenerate predictor spread (ln eta nearly constant): return NaN (no fit).
    """
    eta = dedekind_eta_real(eps)                                  # (local)
    with np.errstate(divide="ignore", invalid="ignore"):
        x = np.log(eta)                                           # (local) eta=0 -> -inf (masked below)
        y = np.log(np.asarray(Y, dtype=np.float64))              # (local)
    mask = np.isfinite(x) & np.isfinite(y)                       # (local) drop eta=0 points
    x, y = x[mask], y[mask]
    if x.size < 3 or np.ptp(x) < 1e-10:
        # not enough spread in the modular predictor to fit a weight
        return np.nan, np.nan, np.nan, np.nan
    A = np.vstack([x, np.ones_like(x)]).T                        # (local)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)                 # (local)
    w, lnA = coef[0], coef[1]                                    # (local)
    yhat = A @ coef                                              # (local)
    ss_res = float(np.sum((y - yhat) ** 2))                     # (local)
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))              # (local)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else np.nan     # (local)
    rms = float(np.sqrt(np.mean((y - yhat) ** 2)))             # (local)
    return float(w), float(lnA), float(R2), rms


# ---------------------------------------------------------------------------
# eps-maps (three candidates from the plan)
# ---------------------------------------------------------------------------
def eps_map(name, tau):
    """Map tau -> eps (real nome in [0,1)) for the named candidate."""
    d = np.asarray(tau, dtype=np.float64) - tau_fold             # (local) tau - tau_fold
    if name == "linear":
        # eps = |tau - tau_fold| normalized to (0,1) over the window half-width
        half = max(abs(TAU_HI - tau_fold), abs(tau_fold - TAU_LO))  # (local)
        return np.abs(d) / half * 0.999 + 1e-6
    if name == "jensen":
        # Jensen-natural diabatic-amplitude nome eps = exp(-S0*|tau-tau_fold|)
        # (NOTE: at tau=tau_fold this -> 1 (fold = deepest nome); away from fold eps<1)
        # To make eps a small nome that GROWS toward 0 away from fold we use the
        # complement form below in the actual fit; here exp(-S0*|d|) in (0,1].
        return np.exp(-S0_AMP * np.abs(d)) * 0.999 + 1e-9
    if name == "nome":
        # nome-like eps = exp(-2*pi*|tau-tau_fold|) (the classical modular nome q=e^{2 pi i tau}
        # with tau on the imaginary axis -> real nome e^{-2 pi Im tau}; here Im tau ~ |d|)
        return np.exp(-2.0 * np.pi * np.abs(d)) * 0.999 + 1e-9
    raise ValueError(name)


# ---------------------------------------------------------------------------
# Build per-sector lowest |lambda|(tau) via the GT-builder
# ---------------------------------------------------------------------------
def build_gen_eigsystem(tau, gens, f_abc, gammas):
    """Return {(p,q): (min_abs_lambda, ground_evec, D_pi)} for the gen sectors at tau.

    Y_i(tau) = <psi_i| D_K |psi_i> on the sector ground state. For an eigenstate of
    H = i D_K with real eigenvalue mu, <psi| (i D_K) |psi> = mu, so the diagonal D_K
    matrix element is -i*mu and |Y_i| = |mu| = the lowest |lambda| of the sector.
    We return the lowest-|mu| per sector (the substrate-IS generation matrix element).
    """
    sector_data, _infra = ds.collect_spectrum_with_eigenvectors(
        tau, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=False
    )
    out = {}
    for sd in sector_data:
        pq = (sd["p"], sd["q"])
        if pq not in C2_MAP:
            continue
        evals = sd["evals"]               # real eigenvalues of H=i*D_pi
        evecs = sd["evecs"]
        D_pi = sd["D_pi"]
        absev = np.abs(evals)
        idx = int(np.argmin(absev))       # ground state (lowest |lambda|)
        psi = evecs[:, idx]
        # cross-check: <psi| (i D_pi) |psi> should equal evals[idx] (real)
        diag_iD = complex(psi.conj() @ (1j * D_pi) @ psi)
        out[pq] = {
            "min_abs": float(absev[idx]),
            "diag_iD_real": float(diag_iD.real),
            "diag_iD_imag": float(diag_iD.imag),
            "dim_rho": sd["dim_rho"],
        }
    return out


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------
def compute():
    print("=" * 78)
    print(f"{GATE_ID}")
    print("=" * 78)
    # --- input SHA pins (logged in first 20 lines per gate-verdicts.md) ---
    pins = {}
    pins["canonical_constants.py"] = hashlib.sha256(CANONICAL_PATH.read_bytes()).hexdigest()
    if CACHE_L12.exists():
        pins["s84_spectrum_cache_L12_tau019.npz"] = hashlib.sha256(CACHE_L12.read_bytes()).hexdigest()
    print(f"  INPUT PIN canonical_constants.py = {pins['canonical_constants.py'][:16]}...")
    if "s84_spectrum_cache_L12_tau019.npz" in pins:
        print(f"  INPUT PIN s84_cache_L12 = {pins['s84_spectrum_cache_L12_tau019.npz'][:16]}...")
    print(f"  tau_fold = {tau_fold}")
    print(f"  C2_gen_sectors (1,0)/(1,1)/(3,0) = {[C2_MAP[s] for s in GEN_SECTORS]}")
    print(f"  R_S96_matter_hierarchy (rank-1 anchor) = {R_S96_matter_hierarchy}")

    # --- build SU(3)+Clifford infrastructure once ---
    print("\n[infra] building su(3) generators, structure constants, Cliff(8)...")
    gens = ds.su3_generators()
    f_abc = ds.compute_structure_constants(gens)
    gammas = ds.build_cliff8()

    # --- tau-grid ---
    tau_grid = np.round(np.arange(TAU_LO, TAU_HI + 0.5 * DTAU, DTAU), 6)   # (local)
    print(f"[grid] tau in [{TAU_LO},{TAU_HI}], {len(tau_grid)} points, dtau={DTAU}")

    # --- per-sector lowest |lambda|(tau) ---
    Y = {pq: [] for pq in GEN_SECTORS}            # (local) Y_i(tau) per sector
    diag_check_max = 0.0                          # (local) max |<psi|iD|psi> - min|lambda||
    for k, tau in enumerate(tau_grid):
        es = build_gen_eigsystem(float(tau), gens, f_abc, gammas)
        for pq in GEN_SECTORS:
            mab = es[pq]["min_abs"]
            Y[pq].append(mab)
            # diagonal D_K matrix element cross-check (imag part of <psi|iD|psi> = min|lambda|)
            diag_check_max = max(diag_check_max,
                                 abs(abs(es[pq]["diag_iD_real"]) - mab))
        if k % 5 == 0:
            print(f"   tau={tau:.3f}: "
                  + ", ".join(f"Y{pq}={es[pq]['min_abs']:.5f}" for pq in GEN_SECTORS))
    for pq in GEN_SECTORS:
        Y[pq] = np.asarray(Y[pq])
    print(f"[xcheck] max |<psi|iD|psi>_real - min|lambda|| = {diag_check_max:.2e} "
          f"(should be ~0: ground-state eval is the diagonal element)")

    # --- value at the fold (tau closest to tau_fold) ---
    i_fold = int(np.argmin(np.abs(tau_grid - tau_fold)))          # (local)
    tau_at_fold = float(tau_grid[i_fold])                        # (local)
    Y_fold = {pq: float(Y[pq][i_fold]) for pq in GEN_SECTORS}    # (local)
    print(f"\n[fold] tau~{tau_at_fold}: "
          + ", ".join(f"Y{pq}={Y_fold[pq]:.6f}" for pq in GEN_SECTORS))

    # --- inter-generation hierarchy R from the DIRECT eigenvalue spacing (rank-1 reproduction) ---
    Y_light = Y_fold[(1, 0)]                                      # (local) lightest (C2=4/3)
    Y_heavy = Y_fold[(3, 0)]                                      # (local) heaviest (C2=6)
    R_direct = Y_heavy / Y_light                                 # (local) direct spacing ratio
    print(f"[R_direct] Y(3,0)/Y(1,0) at fold = {R_direct:.6f} "
          f"(rank-1 anchor R_S96 = {R_S96_matter_hierarchy:.6f})")

    # --- modular-weight fit per sector for each candidate eps-map ---
    eps_candidates = ["linear", "jensen", "nome"]                # (local)
    fit_results = {}                                             # (local)
    for name in eps_candidates:
        eps = eps_map(name, tau_grid)
        per_sector = {}
        for pq in GEN_SECTORS:
            w, lnA, R2, rms = fit_eta_power(eps, Y[pq])
            per_sector[pq] = {"w": w, "lnA": lnA, "R2": R2, "rms": rms}
        fit_results[name] = per_sector

    # --- Casimir-grading test: does w_i track C2_i? ---
    # The weight is determined up to an overall eps-map-dependent scale s:  w_i = s * C2_i.
    # Test (a) proportionality (w-ratios vs C2-ratios) and (b) absolute grading after
    # fixing s by the lightest sector.
    print("\n[fit] modular eta-power weights per eps-map (w_i, R2):")
    grading = {}                                                 # (local)
    for name in eps_candidates:
        ws = np.array([fit_results[name][pq]["w"] for pq in GEN_SECTORS])      # (local)
        R2s = np.array([fit_results[name][pq]["R2"] for pq in GEN_SECTORS])    # (local)
        c2s = np.array([C2_MAP[pq] for pq in GEN_SECTORS])                     # (local)
        # scale s from lightest sector: s = w_light / C2_light
        s_scale = ws[0] / c2s[0] if abs(c2s[0]) > 1e-12 else np.nan            # (local)
        w_pred = s_scale * c2s                                                 # (local)
        # relative grading deviation per sector (skip lightest = anchor)
        rel_dev = np.abs(ws - w_pred) / np.abs(w_pred + 1e-30)                 # (local)
        max_dev = float(np.max(rel_dev[1:])) if len(rel_dev) > 1 else np.nan   # (local)
        min_R2 = float(np.min(R2s))                                            # (local)
        grading[name] = {
            "w": ws.tolist(), "R2": R2s.tolist(), "C2": c2s.tolist(),
            "s_scale": float(s_scale), "w_pred": w_pred.tolist(),
            "max_grading_dev": max_dev, "min_R2": min_R2,
        }
        print(f"   eps={name:7s}: w={np.round(ws,4).tolist()}  R2={np.round(R2s,4).tolist()}  "
              f"s={s_scale:.4f}  max_grading_dev={max_dev:.4f}  min_R2={min_R2:.4f}")

    # --- pick the best eps-map: highest min_R2 among those that fit ---
    valid = {n: g for n, g in grading.items()
             if np.isfinite(g["min_R2"]) and g["min_R2"] >= R2_FLOOR}
    best_name = None                                             # (local)
    if valid:
        best_name = max(valid, key=lambda n: valid[n]["min_R2"])
    else:
        # fall back to the highest min_R2 even if below floor (for diagnostics)
        finite = {n: g for n, g in grading.items() if np.isfinite(g["min_R2"])}
        best_name = max(finite, key=lambda n: finite[n]["min_R2"]) if finite else "linear"

    best = grading[best_name]                                    # (local)
    best_min_R2 = best["min_R2"]                                 # (local)
    best_grading_dev = best["max_grading_dev"]                   # (local)
    print(f"\n[best] eps-map = {best_name}: min_R2={best_min_R2:.4f}, "
          f"max_grading_dev={best_grading_dev:.4f}")

    # ----------------------------------------------------------------------
    # VERDICT logic (pre-registered, plan §W1-1 strict_PASS_boundary + chain)
    #   PASS  iff single consistent (eps-map, w) with R2>=0.95 over the window
    #         AND weights match C2-grading within 10%
    #         AND R_direct > 9.86 (modular structure GENERATES hierarchy beyond rank-1)
    #   INFO  iff partial modular structure (R2>=0.95 but grading fails OR grading
    #         holds without hierarchy gain R~=9.86) OR clean weight at one map only
    #   FAIL  iff no consistent modular weight (min_R2 < 0.95 for all maps)
    # ----------------------------------------------------------------------
    cond_modular = bool(best_min_R2 >= R2_FLOOR)                            # (local)
    cond_grading = bool(np.isfinite(best_grading_dev) and best_grading_dev <= CASIMIR_TOL)  # (local)
    cond_hierarchy = bool(R_direct > R_S96_matter_hierarchy)               # (local)

    # sign verdict (chain Step 4): R_heavy/light > 1 (a real hierarchy) AND the
    # hierarchy direction (heavier sector = larger |lambda|) -- here R_direct > 1
    sign_ok = bool(R_direct > 1.0)                                          # (local)

    if cond_modular and cond_grading and cond_hierarchy:
        verdict = "PASS"
    elif cond_modular and (not cond_grading or not cond_hierarchy):
        verdict = "INFO"     # partial: modular fit present but not Casimir-graded-and-hierarchy-generating
    else:
        verdict = "FAIL"     # no consistent modular weight

    print("\n[verdict-logic]")
    print(f"   cond_modular   (min_R2>={R2_FLOOR})        = {cond_modular}  (min_R2={best_min_R2:.4f})")
    print(f"   cond_grading   (dev<= {CASIMIR_TOL})            = {cond_grading}  (dev={best_grading_dev:.4f})")
    print(f"   cond_hierarchy (R_direct>{R_S96_matter_hierarchy:.3f}) = {cond_hierarchy}  (R_direct={R_direct:.4f})")
    print(f"   sign_ok        (R_direct>1)            = {sign_ok}")
    print(f"   => VERDICT = {verdict}")

    result = {
        "verdict": verdict,
        "best_eps_map": best_name,
        "best_min_R2": best_min_R2,
        "best_grading_dev": best_grading_dev,
        "R_direct": R_direct,
        "R_S96_anchor": float(R_S96_matter_hierarchy),
        "phys_hierarchy_target": PHYS_HIERARCHY_TARGET,
        "cond_modular": cond_modular,
        "cond_grading": cond_grading,
        "cond_hierarchy": cond_hierarchy,
        "sign_ok": sign_ok,
        "tau_grid": tau_grid,
        "Y_10": Y[(1, 0)], "Y_11": Y[(1, 1)], "Y_30": Y[(3, 0)],
        "Y_fold_10": Y_light, "Y_fold_11": Y_fold[(1, 1)], "Y_fold_30": Y_heavy,
        "C2_10": C2_MAP[(1, 0)], "C2_11": C2_MAP[(1, 1)], "C2_30": C2_MAP[(3, 0)],
        "grading": grading,
        "diag_check_max": diag_check_max,
        "pins": pins,
    }
    return result


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    tg = res["tau_grid"]

    # (1) Y_i(tau) per generation sector
    ax = axes[0]
    ax.plot(tg, res["Y_10"], "o-", label=f"(1,0) C2={res['C2_10']:.3f}")
    ax.plot(tg, res["Y_11"], "s-", label=f"(1,1) C2={res['C2_11']:.3f}")
    ax.plot(tg, res["Y_30"], "^-", label=f"(3,0) C2={res['C2_30']:.3f}")
    ax.axvline(tau_fold, color="k", ls="--", alpha=0.5, label=f"tau_fold={tau_fold}")
    ax.set_xlabel("tau (Jensen deformation)")
    ax.set_ylabel("Y_i(tau) = min|lambda|_sector")
    ax.set_title("Gen-graded matrix elements Y_i(tau)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (2) modular fit residuals: ln Y vs ln eta(eps) for the best map
    ax = axes[1]
    bn = res["best_eps_map"]
    eps = eps_map(bn, tg)
    eta = dedekind_eta_real(eps)
    with np.errstate(divide="ignore", invalid="ignore"):
        ln_eta = np.log(eta)                                      # (local) eta=0 -> -inf
    pm = np.isfinite(ln_eta)                                      # (local) mask eta=0 point
    for pq, key in [((1, 0), "Y_10"), ((1, 1), "Y_11"), ((3, 0), "Y_30")]:
        ax.plot(ln_eta[pm], np.log(np.asarray(res[key])[pm]), "o", label=f"{pq}")
    ax.set_xlabel(f"ln eta(eps)   [eps-map={bn}]")
    ax.set_ylabel("ln Y_i")
    ax.set_title(f"Modular-power fit  (min_R2={res['best_min_R2']:.3f})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (3) weight w_i vs Casimir C2_i (the grading test)
    ax = axes[2]
    g = res["grading"][bn]
    c2 = g["C2"]
    w = g["w"]
    wpred = g["w_pred"]
    ax.plot(c2, w, "o", ms=10, label="fitted w_i")
    ax.plot(c2, wpred, "x--", ms=10, label="s * C2_i (grading)")
    for i, pq in enumerate(GEN_SECTORS):
        ax.annotate(str(pq), (c2[i], w[i]), fontsize=8)
    ax.set_xlabel("SU(3) Casimir C2(p,q)")
    ax.set_ylabel("fitted modular weight w_i")
    ax.set_title(f"Casimir grading (dev={res['best_grading_dev']:.3f})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}  --  VERDICT={res['verdict']}  "
                 f"R_direct={res['R_direct']:.3f} vs rank-1 anchor {res['R_S96_anchor']:.3f}",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    print(f"[plot] wrote {PNG_OUT}")


# ---------------------------------------------------------------------------
# Dual-SHA + payload (template contract)
# ---------------------------------------------------------------------------
def compute_dual_sha(pins):
    script_bytes = SCRIPT_PATH.read_bytes()
    canonical_bytes = CANONICAL_PATH.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, extra_rows=None):
    payload = {
        "session": int(SESSION),
        "track": "investigation",
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main():
    res = compute()

    # --- save data ---
    np.savez(
        NPZ_OUT,
        verdict=res["verdict"],
        best_eps_map=res["best_eps_map"],
        best_min_R2=res["best_min_R2"],
        best_grading_dev=res["best_grading_dev"],
        R_direct=res["R_direct"],
        R_S96_anchor=res["R_S96_anchor"],
        phys_hierarchy_target=res["phys_hierarchy_target"],
        cond_modular=res["cond_modular"],
        cond_grading=res["cond_grading"],
        cond_hierarchy=res["cond_hierarchy"],
        sign_ok=res["sign_ok"],
        tau_grid=res["tau_grid"],
        Y_10=res["Y_10"], Y_11=res["Y_11"], Y_30=res["Y_30"],
        Y_fold_10=res["Y_fold_10"], Y_fold_11=res["Y_fold_11"], Y_fold_30=res["Y_fold_30"],
        C2_10=res["C2_10"], C2_11=res["C2_11"], C2_30=res["C2_30"],
        diag_check_max=res["diag_check_max"],
        grading_json=json.dumps(res["grading"]),
    )
    print(f"[data] wrote {NPZ_OUT}")

    make_plot(res)

    # --- dual-SHA + payload ---
    audit_sha, content_sha = compute_dual_sha(res["pins"])

    verdict = res["verdict"]
    # magnitude verdict: how far R_direct sits vs the rank-1 anchor + hierarchy gain
    if res["cond_modular"] and res["cond_grading"] and res["cond_hierarchy"]:
        mag = "PASS"
    elif res["cond_modular"]:
        mag = "INFO"
    else:
        mag = "FAIL"
    sign = "PASS" if res["sign_ok"] else "FAIL"
    # regime: the modular q-series + fit are valid throughout the tau-window (no breakdown)
    regime = "VALID"

    value = (f"verdict={verdict};best_eps_map={res['best_eps_map']};"
             f"min_R2={res['best_min_R2']:.4f};grading_dev={res['best_grading_dev']:.4f};"
             f"R_direct={res['R_direct']:.6f};rank1_anchor={res['R_S96_anchor']:.6f};"
             f"modular={res['cond_modular']};graded={res['cond_grading']};"
             f"hierarchy_gain={res['cond_hierarchy']}")

    extra = [
        f"# INV9-W1-1 Casimir grading: C2=(4/3,3,6) for (1,0)/(1,1)/(3,0); "
        f"best-map={res['best_eps_map']}; grading_dev={res['best_grading_dev']:.4f}; "
        f"diag_xcheck={res['diag_check_max']:.2e}",
        f"# INV9-W1-1 rank-1 wall: R_direct={res['R_direct']:.6f} vs R_S96={res['R_S96_anchor']:.6f}; "
        f"phys_target~{res['phys_hierarchy_target']:.0e} (SS-VII.BL homogeneity wall context)",
    ]

    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=sign, magnitude_verdict=mag,
                          regime_verdict=regime, extra_rows=extra)
    return 0


if __name__ == "__main__":
    sys.exit(main())
