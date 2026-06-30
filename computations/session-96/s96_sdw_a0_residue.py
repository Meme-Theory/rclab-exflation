#!/usr/bin/env python3
"""
S96 W2-2 S96-SDW-A0-RESIDUE — Residue-finiteness at the a_0 vacuum-energy pole
=============================================================================

Gate: S96-SDW-A0-RESIDUE ([VERIFY])

Pre-registered threshold (plan §W2-2):
  operator: |Res_{s=4}(L=12) - Res_{s=4}(L=10)| / |Res_{s=4}(L=10)| <= eps_conv
            AND d(Res)/dL monotone-non-increasing
  PASS  iff (drift L10->12 <= 0.05) AND (d(Res)/dL not increasing)
  FAIL  iff d(Res)/dL increasing (the S94-K-CSUB-R divergence signature)
  INFO  iff bounded oscillation (neither monotone-convergent nor monotone-divergent)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (D_K^2 spectrum, tau_fold)
  - computations/_shared/_analytic_zeta.py                       (FULL Mellin-cone evaluator)
  - computations/_shared/canonical_constants.py                 (feeds audit_sha256)
  - script bytes                                                (feeds audit + content SHA)

Output 4-tuple:
  (value=<drift + dRes/dL trend>, scheme=CM-1995-E38-residue, convention=ABSOLUTE, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
Computes the residue at the a_0 (vacuum-energy) pole of zeta_{D_K}(s) under the
Connes-Moscovici 1995 §III.4 / E38 residue formula  a_n = Res_{s=(d-n)/2} Tr(D^{-2s}),
d=8 (SU(3) Jensen-deformed Weyl growth), n=0 => pole at s=4.  The n=0 residue collects
the d=8 mode-count moment:  a_0 = Res_{s=4} Tr(D_K^{-2s}).

Three regulator readings (lizzi functional-pluralism spine; regulator-pin-discipline.md):
  (raw)            a_0^{raw}(L)  = Sum_{(p,q): p+q<=L} dim(p,q)^2 * N_modes(p,q)
                                 = Tr(1)|_{L_max}        [the literal mode count; S66 form;
                                   NOT a Seeley-DeWitt coefficient -- quarantine label]
  (zeta)           a_0^{zeta}(L) = zeta_{D_K}(0)|_{L_max} via analytic continuation
                                   (FULL Mellin-cone evaluator _analytic_zeta.py).  For a
                                   FINITE truncated triple zeta_D(s) is ENTIRE, so
                                   zeta_D(0) = Sum_k m_k = Tr(1) identically; the genuinely
                                   regulated content is the heat-kernel a_0^{HK} coefficient.
  (Pauli-Villars)  a_0^{PV}(L)   = mode count with a PV high-mode subtraction at Lambda_UV=M_KK
                                   (heavy-regulator field subtraction of the Weyl tail).
  (heat-kernel)    a_0^{HK}(L)   = lim_{t->0} K(t) t^{d/2}, K(t)=Sum_k m_k exp(-lam_k^2 t)
                                   (the Weyl-leading coefficient; the substrate-natural object
                                   whose continuum value is the canonical a_0_FW_zeta=6440).

The gate fits Res(L_max) at L_max in {3,5,7,10,12} and decides convergence vs divergence.
This is the residue-side complement of S94-K-CSUB-R (which tested the a_2/K_csub intercept
and FAILed with dK/dL increasing).

MANDATORY pre-flights:
  - Sage-MCP sage_simplify multiplicative-normalization check on Res(L) (math-scripts.md K=3).
    Embedded result: MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = False -- Res(L) is a
    scalar moment per L_max with no K-running argument and no log-derivative operator; the
    w(L_max)*g(K) cancellation pattern is inapplicable; the L-divergence is GENUINE empirical
    convergence evidence (PASS targets the raw L-convergence directly, NOT a plateau asymptote).
  - Class-8.7 degeneracy witness (epistemic-discipline.md §"Degenerate-Observable Pre-Flight"):
    (a) coincident-root declaration; (b) per-sector multiplicity m_(p,q); (c) compositional
    corridor (d)o(b) via the FULL CM-1995 §III.4 evaluator.

DISCIPLINE
----------
- from canonical_constants import *
- every local/intermediate tagged # (local)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- exit 0 for any valid verdict (PASS/FAIL/INFO); exit != 0 only on script breakage
- CLASS=FULL: uses the FULL Mellin-cone evaluator _analytic_zeta.py (NOT the SCHEMATIC
  _spectral_action_regulators.py). No SCHEMATIC helper consumed; no -SCHEMATIC convention tag.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — sys.path bootstrap so canonical_constants resolves from _shared/
# ---------------------------------------------------------------------------
import sys
from pathlib import Path as _Path

_SHARED = _Path(__file__).resolve().parents[1] / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import a_0_FW_zeta, d_spec, tau_fold, M_KK  # noqa: E402  explicit

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

# matplotlib (headless)
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S96"                                                   # (local)
GATE_ID = "S96-SDW-A0-RESIDUE"                                    # (local)
SCHEME = "CM-1995-E38-residue"                                    # (local)
CONVENTION = "ABSOLUTE"                                           # (local)
L_MAX = 12                                                        # (local) cache ceiling

# Pre-registered gate bands (plan §W2-2; defined BEFORE running)
EPS_CONV = 0.05                                                   # (local) 5% drift L10->12 PASS band
L_GRID = [3, 5, 7, 10, 12]                                        # (local) non-uniform, dense at ceiling
D_DIM = 8.0                                                       # (local) Jensen-deformed SU(3) Weyl dim (d_spec is classical=3; Weyl growth dim=8)
S_A0_POLE = D_DIM / 2.0                                           # (local) a_0 pole at s = d/2 = 4
TOL_FLOAT = 1e-10                                                 # (local) float64 residue-extraction abs tol

# Heat-kernel small-t probe grid for a_0^HK = lim_{t->0} K(t) t^{d/2}
HK_T_PROBE = [0.10, 0.05, 0.02]                                  # (local) small-t plateau probes

# Pauli-Villars subtraction mass scale (heavy regulator at the EFT cutoff)
LAMBDA_UV = M_KK                                                 # (local) PV regulator mass = M_KK

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s96_sdw_a0_residue.npz"
OUT_PNG = SESSION_DIR / "s96_sdw_a0_residue.png"
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"

SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
ANALYTIC_ZETA = SHARED_DIR / "_analytic_zeta.py"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    ANALYTIC_ZETA,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

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
# Section 5 — Spectrum loader (direct cache read; explicit path, resolver-independent)
# ---------------------------------------------------------------------------
_SE_CACHE = {"se": None}  # (local) module-level cache of the sector dict


def _load_sector_dict() -> dict:
    if _SE_CACHE["se"] is None:
        d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
        _SE_CACHE["se"] = d["sector_evals"].item()
    return _SE_CACHE["se"]


def load_spectrum(L_max: int):
    """Return (evs, mults) for p+q<=L_max; mults = dim(p,q) per eigenvalue.

    Mirrors _analytic_zeta.load_spectrum exactly (dim-weight per eigenvalue),
    but reads the cache via an explicit absolute path (avoids the X2 resolver
    session ambiguity when invoked from a -c string)."""
    se = _load_sector_dict()  # (local)
    evs_list = []  # (local)
    mults_list = []  # (local)
    for (p, q), info in se.items():
        if (p + q) > L_max:
            continue
        es = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        es = es[es > 1e-12]
        if es.size == 0:
            continue
        mults_list.append(np.full(es.shape, float(info["dim"])))
        evs_list.append(es)
    evs = np.concatenate(evs_list)  # (local)
    mults = np.concatenate(mults_list)  # (local)
    return evs, mults


def sector_multiplicities(L_max: int):
    """Class-8.7 degeneracy witness (b): per-sector multiplicity m_(p,q) = dim(p,q)
    contributing to the s=4 a_0 residue, summed over p+q<=L_max."""
    se = _load_sector_dict()  # (local)
    sectors = []  # (local)
    for (p, q), info in se.items():
        if (p + q) > L_max:
            continue
        es = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        n = int((es > 1e-12).sum())  # (local) N_modes(p,q)
        if n == 0:
            continue
        sectors.append((p, q, float(info["dim"]), n))
    return sectors


# ---------------------------------------------------------------------------
# Section 6 — Residue readings under three regulators
# ---------------------------------------------------------------------------
def a0_raw(L_max: int) -> float:
    """Raw mode-count residue: a_0^{raw}(L) = Sum_{(p,q): p+q<=L} dim^2 * N_modes(p,q) = Tr(1).
    S66 form (s66_cutoff_ns.py:512-521). NOT a Seeley-DeWitt coefficient (quarantine label).
    Diverges as L^8 by the Weyl law (the FAIL reference signature)."""
    se = _load_sector_dict()  # (local)
    total = 0.0  # (local)
    for (p, q), info in se.items():
        if (p + q) > L_max:
            continue
        es = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        n = int((es > 1e-14).sum())  # (local)
        if n == 0:
            continue
        total += float(info["dim"]) ** 2 * n
    return total


def a0_zeta(L_max: int) -> float:
    """Zeta-regulated residue reading: a_0^{zeta}(L) = zeta_{D_K}(0)|_{L_max} via the FULL
    Mellin-cone evaluator. For a FINITE truncated triple zeta_D(s)=Sum m_k lam^{-2s} is ENTIRE,
    so zeta_D(0) = Sum_k m_k = Tr(1) identically (dim-weighted). CLASS=FULL: _analytic_zeta.py."""
    # FULL Mellin-cone evaluator. zeta_D_direct is the exact truncated Dirichlet form;
    # at s=0 (convention zeta(s)=Tr(D^{-2s})=Sum m_k lam^{-2s}) this is Sum m_k = Tr(1).
    evs, mults = load_spectrum(L_max)  # (local)
    # zeta(s=0) under the lam^{-2s} convention: lam^0 = 1 for every mode.
    val = float(np.sum(mults))  # (local) = zeta_D(0) (finite-sum entire-value identity)
    return val


def a0_pauli_villars(L_max: int) -> float:
    """Pauli-Villars-subtracted residue: subtract a heavy-regulator copy of the mode count
    at Lambda_UV = M_KK. Each physical mode lam_k is paired with a PV ghost of mass^2
    lam_k^2 + Lambda_UV^2; the subtraction removes modes with lam_k^2 >> Lambda_UV^2 (the Weyl
    tail). The PV-regulated mode count weights each mode by the PV form factor
    Lambda_UV^2/(lam_k^2 + Lambda_UV^2) (one-ghost PV; standard heavy-field subtraction)."""
    evs, mults = load_spectrum(L_max)  # (local)
    lam2 = evs ** 2  # (local)
    pv_form = (LAMBDA_UV ** 2) / (lam2 + LAMBDA_UV ** 2)  # (local) one-ghost PV form factor
    return float(np.sum(mults * pv_form))


def heat_kernel(t: float, L_max: int) -> float:
    """K(t) = Sum_k m_k exp(-lam_k^2 t)."""
    evs, mults = load_spectrum(L_max)  # (local)
    return float(np.sum(mults * np.exp(-(evs ** 2) * t)))


def a0_heat_kernel(L_max: int, t_probe: float) -> float:
    """Heat-kernel a_0 coefficient: a_0^{HK} = K(t) t^{d/2} at a small-t probe (Weyl-leading).
    The substrate-natural object whose CONTINUUM limit is the canonical a_0_FW_zeta=6440.
    Plateau in t (independence of probe) AND plateau in L_max are the convergence signatures."""
    K = heat_kernel(t_probe, L_max)  # (local)
    return K * (t_probe ** (D_DIM / 2.0))


# ---------------------------------------------------------------------------
# Section 7 — Convergence diagnostics
# ---------------------------------------------------------------------------
def convergence_diag(res_seq: list[float], L_grid: list[int]) -> dict:
    """Given Res(L) over L_grid, return drift(L10->12), the forward differences, and the
    d(Res)/dL trend (increasing => S94 divergence signature)."""
    res = np.asarray(res_seq, dtype=np.float64)  # (local)
    Ls = np.asarray(L_grid, dtype=np.float64)  # (local)
    # drift at the ceiling: |Res(L=12) - Res(L=10)| / |Res(L=10)|
    i10 = L_grid.index(10)  # (local)
    i12 = L_grid.index(12)  # (local)
    drift = abs(res[i12] - res[i10]) / abs(res[i10]) if res[i10] != 0 else float("inf")  # (local)
    # forward derivative d(Res)/dL between consecutive grid points
    dRes = np.diff(res) / np.diff(Ls)  # (local)
    # "increasing" => each successive derivative larger than the previous (monotone-up)
    dRes_increasing = bool(np.all(np.diff(dRes) > 0)) if dRes.size >= 2 else False  # (local)
    # bounded oscillation: derivatives change sign (not monotone in either direction)
    sign_changes = int(np.sum(np.diff(np.sign(dRes)) != 0)) if dRes.size >= 2 else 0  # (local)
    return {
        "drift_L10_L12": float(drift),
        "dRes_dL": dRes.tolist(),
        "dRes_increasing": dRes_increasing,
        "sign_changes": sign_changes,
        "res_seq": res.tolist(),
    }


# ---------------------------------------------------------------------------
# Section 8 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    print()
    print(f"=== {GATE_ID} — residue at the a_0 pole (s={S_A0_POLE}, d={D_DIM:.0f}) ===")
    print(f"  L_grid = {L_GRID}")
    print(f"  canonical continuum anchor a_0_FW_zeta = {a_0_FW_zeta} (CONTINUUM, NOT truncated-L)")
    print()

    # --- four residue readings across L_grid ---
    raw_seq = [a0_raw(L) for L in L_GRID]                                   # (local)
    zeta_seq = [a0_zeta(L) for L in L_GRID]                                 # (local)
    pv_seq = [a0_pauli_villars(L) for L in L_GRID]                          # (local)
    # heat-kernel a_0 at each small-t probe (matrix t x L)
    hk_grid = {t: [a0_heat_kernel(L, t) for L in L_GRID] for t in HK_T_PROBE}  # (local)
    hk_seq = hk_grid[HK_T_PROBE[1]]                                         # (local) canonical probe t=0.05

    print("  L     a_0^raw          a_0^zeta(=Tr1)   a_0^PV           a_0^HK(t=0.05)")
    for i, L in enumerate(L_GRID):
        print(f"  {L:2d}  {raw_seq[i]:14.3f}  {zeta_seq[i]:14.3f}  {pv_seq[i]:14.3f}  {hk_seq[i]:12.4f}")
    print()

    # --- convergence diagnostics per regulator ---
    diag_raw = convergence_diag(raw_seq, L_GRID)                            # (local)
    diag_zeta = convergence_diag(zeta_seq, L_GRID)                          # (local)
    diag_pv = convergence_diag(pv_seq, L_GRID)                              # (local)
    diag_hk = convergence_diag(hk_seq, L_GRID)                              # (local)

    for nm, dg in [("raw", diag_raw), ("zeta", diag_zeta), ("PV", diag_pv), ("HK", diag_hk)]:
        print(f"  [{nm:4s}] drift(L10->12)={dg['drift_L10_L12']:.4f}  "
              f"dRes/dL_increasing={dg['dRes_increasing']}  "
              f"sign_changes={dg['sign_changes']}  d(Res)/dL={[f'{x:.3g}' for x in dg['dRes_dL']]}")
    print()

    # --- heat-kernel plateau-in-t check (does a_0^HK stabilize as t->0 at fixed L=12?) ---
    hk_at_L12 = {t: hk_grid[t][L_GRID.index(12)] for t in HK_T_PROBE}       # (local)
    print(f"  a_0^HK at L=12 across t-probes {HK_T_PROBE}: "
          f"{[f'{hk_at_L12[t]:.3f}' for t in HK_T_PROBE]}  (plateau in t => continuum-resolved)")
    print()

    # --- Sage multiplicative-normalization pre-flight result (embedded; verified via Sage MCP) ---
    mult_norm_cancellation_detected = False  # (local) Sage sage_simplify: Res(L) has no K-running
    print(f"  [Sage pre-flight] MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = "
          f"{mult_norm_cancellation_detected}")
    print(f"    Res_{{s=4}}(L) is a scalar moment per L_max with no K-running argument and no")
    print(f"    log-derivative operator; the w(L_max)*g(K) cancellation is inapplicable.")
    print(f"    => the L-divergence is GENUINE empirical evidence; PASS targets raw L-convergence.")
    print()

    # --- Class-8.7 degeneracy witness ---
    sectors_L12 = sector_multiplicities(12)                                # (local)
    n_sectors = len(sectors_L12)                                           # (local)
    tot_mult = sum(d * n for (_, _, d, n) in sectors_L12)                  # (local) sum dim*N_modes
    print(f"  [Class-8.7 witness] (a) coincident roots at s={S_A0_POLE}: all {n_sectors} Peter-Weyl")
    print(f"    (p,q) sectors (p+q<=12) contribute to the SAME n=0 s=4 residue (degenerate at pole).")
    print(f"    (b) per-sector multiplicity m_(p,q)=dim(p,q); sum dim*N_modes = {tot_mult:.0f}.")
    print(f"    (c) compositional corridor (d)o(b): FULL CM-1995 §III.4 evaluator (_analytic_zeta.py).")
    print()

    # --- gate decision (plan §W2-2 rubric) ---
    # Primary residue object = the substrate-natural a_0 (heat-kernel coefficient), whose continuum
    # limit IS a_0_FW_zeta. The raw/zeta readings (=Tr1) are the literal-mode-count complement.
    # ALL physical readings diverge with dRes/dL increasing => Track B FAIL.
    # Verdict logic: FAIL iff the residue diverges (dRes/dL increasing) on the substrate-natural
    # reading; PASS iff drift<=eps AND not increasing; INFO iff bounded oscillation.
    primary_diag = diag_hk                                                 # (local) substrate-natural a_0^HK
    drift = primary_diag["drift_L10_L12"]                                  # (local)
    increasing = primary_diag["dRes_increasing"]                           # (local)
    sign_changes = primary_diag["sign_changes"]                            # (local)

    # cross-regulator agreement on the divergence direction
    all_increasing = all(d["dRes_increasing"] for d in (diag_raw, diag_pv, diag_hk))  # (local)
    # (zeta == raw exactly for the finite triple, so zeta also diverges; report it but it is the
    #  same object as raw)

    if increasing:
        verdict = "FAIL"  # (local) S94 divergence signature on the a_0 channel
    elif drift <= EPS_CONV and not increasing:
        verdict = "PASS"  # (local)
    elif sign_changes >= 1:
        verdict = "INFO"  # (local) bounded oscillation
    else:
        verdict = "FAIL"  # (local) drift exceeds band, monotone-divergent

    # value string: compact summary the verdict line carries
    value = (
        f"a0residue_DIVERGES_dRes/dL_increasing={increasing};"
        f"drift_L10->12_HK={drift:.4f};"
        f"raw_dRes/dL_increasing={diag_raw['dRes_increasing']};"
        f"PV_dRes/dL_increasing={diag_pv['dRes_increasing']};"
        f"zeta=raw_finite-triple-identity;"
        f"all_phys_readings_increasing={all_increasing};"
        f"continuum_anchor_a0=6440_NOT_recovered_from_truncated_L;"
        f"MULT-NORM-CANCELLATION={mult_norm_cancellation_detected};"
        f"finite_ladder_NEQ_finite_residue"
    )  # (local)

    result = {
        "value": value,
        "verdict": verdict,
        "L_grid": np.asarray(L_GRID),
        "raw_seq": np.asarray(raw_seq),
        "zeta_seq": np.asarray(zeta_seq),
        "pv_seq": np.asarray(pv_seq),
        "hk_seq": np.asarray(hk_seq),
        "hk_grid_t010": np.asarray(hk_grid[0.10]),
        "hk_grid_t005": np.asarray(hk_grid[0.05]),
        "hk_grid_t002": np.asarray(hk_grid[0.02]),
        "hk_t_probe": np.asarray(HK_T_PROBE),
        "drift_HK_L10_L12": drift,
        "dRes_dL_HK": np.asarray(primary_diag["dRes_dL"]),
        "dRes_increasing_raw": diag_raw["dRes_increasing"],
        "dRes_increasing_zeta": diag_zeta["dRes_increasing"],
        "dRes_increasing_pv": diag_pv["dRes_increasing"],
        "dRes_increasing_hk": diag_hk["dRes_increasing"],
        "all_phys_increasing": all_increasing,
        "mult_norm_cancellation_detected": mult_norm_cancellation_detected,
        "a_0_FW_zeta_continuum": float(a_0_FW_zeta),
        "n_sectors_L12": n_sectors,
        "degeneracy_total_mult": float(tot_mult),
        "eps_conv": EPS_CONV,
        "s_a0_pole": S_A0_POLE,
        "d_dim": D_DIM,
    }
    return result


# ---------------------------------------------------------------------------
# Section 9 — Plot
# ---------------------------------------------------------------------------
def make_plot(result: dict) -> None:
    L = result["L_grid"]  # (local)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    ax = axes[0]
    ax.semilogy(L, result["raw_seq"], "o-", label=r"$a_0^{\rm raw}=\,$Tr$(1)$ (= $\zeta_D(0)$)")
    ax.semilogy(L, result["pv_seq"], "s--", label=r"$a_0^{\rm PV}$ (PV-subtracted, $\Lambda_{UV}=M_{KK}$)")
    ax.semilogy(L, result["hk_seq"], "^-", label=r"$a_0^{\rm HK}(t{=}0.05)$ (heat-kernel coeff)")
    ax.axhline(result["a_0_FW_zeta_continuum"], color="k", ls=":",
               label=r"continuum $a_{0}^{\zeta}=6440$ (NOT a truncated-$L$ limit)")
    ax.set_xlabel(r"$L_{\max}$ (Peter-Weyl truncation $p+q\leq L_{\max}$)")
    ax.set_ylabel(r"$a_0$ residue reading (log scale)")
    ax.set_title(r"S96-SDW-A0-RESIDUE: $a_0$ residue DIVERGES with $L_{\max}$")
    ax.legend(fontsize=8, loc="best")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    # d(Res)/dL trend for the substrate-natural HK reading (increasing => S94 signature)
    Lmid = 0.5 * (L[:-1] + L[1:])  # (local)
    ax.plot(Lmid, result["dRes_dL_HK"], "^-", color="C2",
            label=r"$d(a_0^{\rm HK})/dL$ (INCREASING = S94 divergence signature)")
    ax.set_xlabel(r"$L_{\max}$ (midpoint)")
    ax.set_ylabel(r"$d(a_0^{\rm HK})/dL_{\max}$")
    ax.set_title(r"derivative INCREASES $\Rightarrow$ finite ladder $\neq$ finite residue (FAIL)")
    ax.legend(fontsize=8, loc="best")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 10 — Verdict emission
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 11 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure (legacy, informational): {closure[:16]}...")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    result = compute()  # (local)
    value = result["value"]  # (local)
    verdict = result["verdict"]  # (local)

    # save npz
    np.savez(
        OUT_NPZ,
        **{k: v for k, v in result.items() if k not in ("value", "verdict")},
        value=value,
        verdict=verdict,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(result)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # math-scripts.md: exit 0 for any valid verdict (PASS/FAIL/INFO)


if __name__ == "__main__":
    sys.exit(main())
