#!/usr/bin/env python3
"""
INV3 W3-4 — Casimir-graded N(j)=7n test on the L12 fold spectrum
=================================================================

Gate: INV3-W3-4-CASIMIR-GRADED-NJ-7N ([CHAIN])

Pre-registered threshold (plan §W3-4):
  operator type = set.
  PASS iff there EXISTS an SU(3) Casimir-graded mode-counting function N(p,q)
       built from {dim(p,q), C2(p,q), p+q} on the L_max=12 fold cache that
       reproduces Paasch's integer SET {7,35,42,98,150} as 7n (N(j)/7 integer)
       for >= 4 of the 5 particles (exact integer 7n match).
  INFO iff 2-3 of the 5 are reproduced (the dim-coincidence: 35,42 ARE SU(3)
       dims; the rest are not).
  FAIL iff < 2 of the 5 are reproduced.

Plan-freeze Sage pre-flight (substitution chain, plan §W3-4 item 7):
  Paasch N(j) = {7,35,42,98,150};  N(j)/7 = {1,5,6,14,150/7=21.43}.
  SU(3) dims (p+q<=5) = {1,3,6,8,10,15,21,24,27,35,42,...}.
  7 NOT a dim; 35,42 ARE dims; 98,150 NOT dims.  => a pure-dim map reproduces
  AT MOST 2-of-5 -> cannot PASS -> EXPECTED outcome INFO-partial.
  M(j)=sqrt(N(j)) successive ratios = {2.236,1.095,1.528,1.237}; fN=sqrt(5)-1
  matches ONLY kaon->proton (1.2372).  N(p)/N(K)=150/98=1.5306 vs phi_paasch
  =1.531580 (0.063%).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
       (sector_evals[(p,q)] = {dim:int, level:int, abs_evals:ndarray}; 90 sectors)
  - canonical_constants.py (feeds audit_sha256 only; supplies phi_paasch, tau_fold)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<n_matched_7n>, scheme=CASIMIR-GRADED-NJ-7N, convention=ABSOLUTE, L_max=12)

Classification: PARTICLE (Paasch's mass-number integers N(j) as a
  representation-theoretic mode count of D_K) on a GEOMETRIC substrate
  (the Casimir ladder / Peter-Weyl mode geometry).

METHODOLOGY
-----------
Direction of explanation (phononic-framing.md, substrate-first):
  D_K eigenvalues (the L12 fold cache) -> Peter-Weyl (p,q) sector content +
  Casimir grading C2(p,q) -> a mode-count integer N(p,q) -> Paasch's
  mass-number integers.  The mass IS the Higgs-overlap of a Peter-Weyl mode
  in the Jensen metric; the integers ARE the mode-counting structure of the
  Peter-Weyl decomposition, NOT particles placed "in" a container at integer
  mass numbers.

The script:
 (1) Loads the L12 cache. For each (p,q) sector computes the EXACT
     C2(p,q)=(p^2+q^2+pq+3p+3q)/3, dim(p,q)=(p+1)(q+1)(p+q+2)/2, and the
     bottom-of-band |lambda|_min from the cached abs_evals.  Verifies the
     S21c/S22 bridge lambda^2 = C2(p,q) + 3/4 (bi-invariant tau=0 form) as a
     diagnostic.
 (2) Builds the partial-coincidence diagnostic: which of {7,35,42,98,150}
     equal an SU(3) dim(p,q)?  (Pre-flight: 35,42 yes; 7,98,150 no.)
 (3) Tests a family of Casimir-graded mode-counting functions N(p,q):
       (A) cumulative count of MODES (dim-weighted, sum of dim over sectors
           with C2 <= ceiling) below a Casimir ceiling — scanned over every
           distinct C2 value.
       (B) cumulative count of SECTORS (unweighted) below a Casimir ceiling.
       (C) rank-graded count p+q.
       (D) the single dim(p,q) itself.
       (E) Casimir-level integer round(C2*3) = p^2+q^2+pq+3p+3q.
       (F) bottom-of-band level index (cache 'level' field).
     For each candidate, count how many of {7,35,42,98,150} are reproduced
     EXACTLY as 7n (integer N/7), and how many are reproduced as the raw
     integer (a looser match used only as a diagnostic).
 (4) Reports the M(j)=sqrt(N(j)) successive-ratio vs fN diagnostic and the
     N(p)/N(K)=150/98 vs phi_paasch diagnostic.
 (5) Emits the full sector table (p,q,dim,C2,|lambda|_min,candidate-N) + the
     best-fit mode-counting function + the partial-coincidence diagnostic +
     the candidate prefactor m0 tying electron (N=7) to M_KK + verdict.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only (counting + small arithmetic; cache pre-diagonalized) — OMP cap 8
- SHA-256 of all input files logged in first 20 lines of stdout
- dual-SHA (audit + content) emitted (S84+)
- 4-tuple printed as the final non-verdict line
- verdict PAYLOAD printed for the agent to pass to emit_verdict (race-safe)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Path setup + OMP cap (BEFORE canonical import and numpy)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_THIS = Path(__file__).resolve()
_SHARED = _THIS.parent.parent / "_shared"          # computations/_shared
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402  (supplies phi_paasch, tau_fold, M_KK)
from canonical_constants import phi_paasch, tau_fold, M_KK  # noqa: E402  (explicit)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-3
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "3"                                                       # (local) investigation number
GATE_ID = "INV3-W3-4"                                               # (local) short form per orchestrator override
SCHEME = "CASIMIR-GRADED-NJ-7N"                                     # (local)
CONVENTION = "ABSOLUTE"                                             # (local) integer counts, not ratios
L_MAX = 12                                                          # (local)

# Pre-registered PASS/INFO/FAIL boundaries (plan §W3-4)
PASS_MIN_MATCH_7N = 4          # (local) PASS iff >= 4-of-5 reproduced as 7n
INFO_MIN_MATCH = 2             # (local) INFO iff 2-3 reproduced; FAIL iff < 2
REL_TOL_DIAG = 0.02            # (local) 2% relative tol for the M-ratio / phi_paasch diagnostics

# Paasch mass-number integers N(j) = (m_j/m_e)^{2/3} (Paper 03, Eq 5.2)
PAASCH_PARTICLES = ["electron", "muon", "pion", "kaon", "proton"]   # (local)
PAASCH_NJ = [7, 35, 42, 98, 150]                                   # (local)

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

# Output destinations
OUT_NPZ = SESSION_DIR / "inv3_w3_casimir_graded_nj_7n.npz"
OUT_PNG = SESSION_DIR / "inv3_w3_casimir_graded_nj_7n.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block
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


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — SU(3) representation arithmetic
# ---------------------------------------------------------------------------
def su3_dim(p: int, q: int) -> int:
    """SU(3) irrep dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2 (exact integer)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_casimir_frac(p: int, q: int) -> Fraction:
    """Exact quadratic Casimir C2(p,q) = (p^2+q^2+pq+3p+3q)/3 (Fraction)."""
    return Fraction(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def su3_casimir_int(p: int, q: int) -> int:
    """Casimir-level INTEGER = 3*C2 = p^2+q^2+pq+3p+3q (the numerator)."""
    return p * p + q * q + p * q + 3 * p + 3 * q


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # fN = Paasch golden-ratio M-value successive ratio = sqrt(5)-1 = 2/golden
    fN = np.sqrt(5.0) - 1.0  # (local) 1.2360679...

    # ---- 6.1 Load the L12 fold cache -------------------------------------
    data = np.load(CACHE_PATH, allow_pickle=True)  # (local)
    sector_evals = data["sector_evals"].item()  # (local) dict {(p,q): {dim,level,abs_evals}}
    n_sectors = len(sector_evals)  # (local)
    print(f"  cache sectors: {n_sectors}")

    # ---- 6.2 Per-sector table -------------------------------------------
    # Each row: (p, q, dim_cache, dim_formula, C2_float, C2_int, level, lam_min, lam_min_sq)
    rows = []  # (local)
    bridge_residuals = []  # (local) |lam_min^2 - (C2 + 3/4)|
    for (p, q), entry in sector_evals.items():
        dim_cache = int(entry["dim"])  # (local)
        dim_formula = su3_dim(p, q)  # (local)
        c2 = su3_casimir_frac(p, q)  # (local)
        c2_f = float(c2)  # (local)
        c2_int = su3_casimir_int(p, q)  # (local)
        level = int(entry["level"])  # (local)
        abs_evals = np.asarray(entry["abs_evals"], dtype=float)  # (local)
        # bottom-of-band |lambda|_min: smallest NONZERO |eval| (zero modes excluded
        # from the band floor; if all zero, use 0.0)
        nz = abs_evals[abs_evals > 1e-12]  # (local)
        lam_min = float(nz.min()) if nz.size else 0.0  # (local)
        rows.append(
            dict(
                p=p, q=q, dim_cache=dim_cache, dim_formula=dim_formula,
                C2=c2_f, C2_int=c2_int, level=level, lam_min=lam_min,
                lam_min_sq=lam_min * lam_min,
            )
        )
        # S21c/S22 bridge diagnostic: lambda^2 = C2 + 3/4 (bi-invariant tau=0 form)
        bridge_residuals.append(abs(lam_min * lam_min - (c2_f + 0.75)))

    rows.sort(key=lambda r: (r["C2"], r["p"], r["q"]))  # (local) order by Casimir
    bridge_resid_arr = np.array(bridge_residuals)  # (local)

    # dim self-consistency (cache vs formula)
    dim_mismatch = sum(1 for r in rows if r["dim_cache"] != r["dim_formula"])  # (local)

    # ---- 6.3 Partial-coincidence diagnostic: N(j) vs SU(3) dims ----------
    all_dims = sorted({su3_dim(p, q) for p in range(0, L_MAX + 1)
                       for q in range(0, L_MAX + 1) if p + q <= L_MAX})  # (local)
    dim_set = set(all_dims)  # (local)
    nj_is_dim = {nj: (nj in dim_set) for nj in PAASCH_NJ}  # (local)
    # which (p,q) realize the matching dims
    nj_dim_realizers = {}  # (local)
    for nj in PAASCH_NJ:
        if nj in dim_set:
            nj_dim_realizers[nj] = [
                (p, q) for p in range(0, L_MAX + 1) for q in range(0, L_MAX + 1)
                if p + q <= L_MAX and su3_dim(p, q) == nj
            ]
    n_nj_are_dims = sum(1 for v in nj_is_dim.values() if v)  # (local)

    # ---- 6.4 Candidate mode-counting functions --------------------------
    # Build cumulative-count structures over distinct Casimir ceilings.
    distinct_c2 = sorted({r["C2"] for r in rows})  # (local)
    # cumulative dim-weighted count below each ceiling (<=)
    cum_dim_at_ceiling = {}  # (local)
    cum_sec_at_ceiling = {}  # (local)
    for c2v in distinct_c2:
        cum_dim_at_ceiling[c2v] = sum(r["dim_formula"] for r in rows if r["C2"] <= c2v + 1e-9)
        cum_sec_at_ceiling[c2v] = sum(1 for r in rows if r["C2"] <= c2v + 1e-9)

    # Candidate generators -> set of integers each can produce
    # (A) cumulative dim-weighted mode count below a ceiling
    cand_A = sorted(set(cum_dim_at_ceiling.values()))  # (local)
    # (B) cumulative sector count below a ceiling
    cand_B = sorted(set(cum_sec_at_ceiling.values()))  # (local)
    # (C) rank-graded count p+q  (a small integer mesh)
    cand_C = sorted({r["p"] + r["q"] for r in rows})  # (local)
    # (D) the single dim(p,q)
    cand_D = sorted({r["dim_formula"] for r in rows})  # (local)
    # (E) Casimir-level integer 3*C2 = p^2+q^2+pq+3p+3q
    cand_E = sorted({r["C2_int"] for r in rows})  # (local)
    # (F) bottom-of-band level index
    cand_F = sorted({r["level"] for r in rows})  # (local)

    candidate_sets = {
        "A_cumulative_dim_below_C2_ceiling": cand_A,
        "B_cumulative_sector_below_C2_ceiling": cand_B,
        "C_rank_p_plus_q": cand_C,
        "D_single_dim_pq": cand_D,
        "E_casimir_level_integer_3C2": cand_E,
        "F_band_level_index": cand_F,
    }

    # For each candidate, count exact 7n matches and raw-integer matches.
    def count_matches(produced_set, targets):
        produced = set(int(x) for x in produced_set)  # (local)
        raw_hits = {t: (t in produced) for t in targets}  # (local)
        # 7n match: N(j) must be in the produced set AND be a multiple of 7
        seven_n_hits = {t: ((t in produced) and (t % 7 == 0)) for t in targets}  # (local)
        return raw_hits, seven_n_hits

    candidate_report = {}  # (local)
    best_name = None  # (local)
    best_n7n = -1  # (local)
    best_raw = -1  # (local)
    for name, pset in candidate_sets.items():
        raw_hits, seven_n_hits = count_matches(pset, PAASCH_NJ)
        n_raw = sum(1 for v in raw_hits.values() if v)  # (local)
        n_7n = sum(1 for v in seven_n_hits.values() if v)  # (local)
        candidate_report[name] = dict(
            n_raw_match=n_raw, n_7n_match=n_7n,
            raw_hits=raw_hits, seven_n_hits=seven_n_hits,
            set_size=len(pset),
        )
        # best = max 7n matches, tie-break on raw matches
        if (n_7n > best_n7n) or (n_7n == best_n7n and n_raw > best_raw):
            best_n7n, best_raw, best_name = n_7n, n_raw, name

    # ---- 6.5 M(j)=sqrt(N(j)) successive-ratio vs fN diagnostic -----------
    M_vals = [float(np.sqrt(nj)) for nj in PAASCH_NJ]  # (local)
    M_ratios = [M_vals[i + 1] / M_vals[i] for i in range(len(M_vals) - 1)]  # (local)
    M_ratio_vs_fN = [abs(r - fN) / fN for r in M_ratios]  # (local) relative dev
    n_M_ratio_match_fN = sum(1 for d in M_ratio_vs_fN if d <= REL_TOL_DIAG)  # (local)

    # ---- 6.6 N(p)/N(K) = 150/98 vs phi_paasch diagnostic -----------------
    Np_over_NK = PAASCH_NJ[4] / PAASCH_NJ[3]  # (local) 150/98
    phi_dev = abs(Np_over_NK - phi_paasch) / phi_paasch  # (local) relative dev
    # also the other adjacent N-ratios vs phi_paasch
    N_ratios = [PAASCH_NJ[i + 1] / PAASCH_NJ[i] for i in range(len(PAASCH_NJ) - 1)]  # (local)
    N_ratio_vs_phi = [abs(r - phi_paasch) / phi_paasch for r in N_ratios]  # (local)

    # ---- 6.7 Candidate prefactor m0 tying electron (N=7) to M_KK ---------
    # In Paasch m*(j) = N(j)^{3/2} m_e, so the electron anchors the absolute
    # scale. If N(electron)=7 were a substrate mode count, the prefactor m0
    # that sets m_e is the single imported scale M_KK (dimensional tie).
    # m_e (PDG) = 0.51099895 MeV; M_KK ~ 7.43e16 GeV. The ratio m_e/M_KK is the
    # 14-OOM scale separation the framework documents (content lives in ratios,
    # not absolute eigenvalues).
    m_e_MeV = 0.51099895000  # (local) PDG electron mass, MeV (diagnostic only)
    M_KK_MeV = float(M_KK) * 1.0e3  # (local) M_KK in MeV (M_KK is in GeV)
    m_e_over_M_KK = m_e_MeV / M_KK_MeV  # (local) ~6.9e-17 (14-OOM separation)

    # ---- 6.8 Verdict -----------------------------------------------------
    # PASS iff best candidate reproduces >= 4-of-5 as 7n.
    # INFO iff 2-3 reproduced (raw or 7n, whichever the structure present).
    # FAIL iff < 2 reproduced.
    # Per pre-flight: pure-dim (candidate D) reproduces 35,42 -> 2-of-5 raw.
    n_match_for_verdict_7n = best_n7n  # (local) strict 7n count of best candidate
    # the dim-coincidence partial structure (raw, not necessarily 7n) is the
    # INFO floor: how many N(j) ARE SU(3) dims
    n_match_for_verdict_struct = max(best_raw, n_nj_are_dims)  # (local)

    if n_match_for_verdict_7n >= PASS_MIN_MATCH_7N:
        verdict = "PASS"  # (local)
    elif n_match_for_verdict_struct >= INFO_MIN_MATCH:
        verdict = "INFO"  # (local)
    else:
        verdict = "FAIL"  # (local)

    return dict(
        value=n_match_for_verdict_7n,
        verdict=verdict,
        fN=fN,
        n_sectors=n_sectors,
        rows=rows,
        bridge_resid_max=float(bridge_resid_arr.max()),
        bridge_resid_mean=float(bridge_resid_arr.mean()),
        dim_mismatch=dim_mismatch,
        all_dims=all_dims,
        nj_is_dim=nj_is_dim,
        nj_dim_realizers=nj_dim_realizers,
        n_nj_are_dims=n_nj_are_dims,
        candidate_report=candidate_report,
        best_candidate=best_name,
        best_n7n=best_n7n,
        best_raw=best_raw,
        M_vals=M_vals,
        M_ratios=M_ratios,
        M_ratio_vs_fN=M_ratio_vs_fN,
        n_M_ratio_match_fN=n_M_ratio_match_fN,
        Np_over_NK=Np_over_NK,
        phi_dev=phi_dev,
        N_ratios=N_ratios,
        N_ratio_vs_phi=N_ratio_vs_phi,
        m_e_over_M_KK=m_e_over_M_KK,
        m_e_MeV=m_e_MeV,
        M_KK_MeV=M_KK_MeV,
        n_struct=n_match_for_verdict_struct,
    )


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # (a) Casimir ladder: dim(p,q) vs C2(p,q), with N(j) dim-coincidence overlay
    ax = axes[0, 0]
    c2s = [r["C2"] for r in res["rows"]]  # (local)
    dims = [r["dim_formula"] for r in res["rows"]]  # (local)
    ax.scatter(c2s, dims, s=18, c="steelblue", alpha=0.7, label="SU(3) sectors (p,q), L<=12")
    for nj, isd in res["nj_is_dim"].items():
        col = "green" if isd else "red"  # (local)
        ax.axhline(nj, color=col, ls="--", lw=1.1, alpha=0.8)
        ax.text(max(c2s) * 0.7, nj * 1.02, f"N={nj}" + (" (IS dim)" if isd else " (NOT dim)"),
                color=col, fontsize=8)
    ax.set_xlabel("C2(p,q)")
    ax.set_ylabel("dim(p,q)")
    ax.set_yscale("log")
    ax.set_title("(a) SU(3) Casimir ladder vs Paasch N(j); 35,42 ARE dims (green), 7,98,150 NOT (red)")
    ax.legend(fontsize=8, loc="upper left")

    # (b) candidate mode-counting functions: number of 7n / raw matches
    ax = axes[0, 1]
    names = list(res["candidate_report"].keys())  # (local)
    n7 = [res["candidate_report"][n]["n_7n_match"] for n in names]  # (local)
    nr = [res["candidate_report"][n]["n_raw_match"] for n in names]  # (local)
    y = np.arange(len(names))  # (local)
    ax.barh(y - 0.2, nr, height=0.4, color="orange", label="raw-integer matches")
    ax.barh(y + 0.2, n7, height=0.4, color="darkred", label="exact 7n matches")
    ax.axvline(4, color="green", ls="--", lw=1.2, label="PASS boundary (>=4-of-5 as 7n)")
    ax.axvline(2, color="gray", ls=":", lw=1.0, label="INFO floor (>=2)")
    ax.set_yticks(y)
    ax.set_yticklabels([n.replace("_", "\n") for n in names], fontsize=7)
    ax.set_xlabel("# of {7,35,42,98,150} reproduced (of 5)")
    ax.set_xlim(0, 5.3)
    ax.set_title(f"(b) Candidate counts; best={res['best_candidate']} ({res['best_n7n']} as 7n)")
    ax.legend(fontsize=7, loc="lower right")

    # (c) M(j)=sqrt(N(j)) successive ratios vs fN
    ax = axes[1, 0]
    labels = [f"{PAASCH_PARTICLES[i]}->{PAASCH_PARTICLES[i+1]}" for i in range(4)]  # (local)
    x = np.arange(4)  # (local)
    ax.bar(x, res["M_ratios"], color="slateblue", alpha=0.8)
    ax.axhline(res["fN"], color="crimson", ls="--", lw=1.4, label=f"fN=sqrt(5)-1={res['fN']:.4f}")
    ax.axhline(np.sqrt(5.0), color="gray", ls=":", lw=1.0, label="sqrt(5)=2.236")
    for i, r in enumerate(res["M_ratios"]):
        ax.text(i, r + 0.03, f"{r:.4f}", ha="center", fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=20, fontsize=8)
    ax.set_ylabel("M(j+1)/M(j),  M=sqrt(N)")
    ax.set_title(f"(c) sqrt(N) successive ratios vs fN; only kaon->proton matches (n={res['n_M_ratio_match_fN']}/4)")
    ax.legend(fontsize=8)

    # (d) N-ratios vs phi_paasch  (highlight 150/98)
    ax = axes[1, 1]
    x = np.arange(4)  # (local)
    ax.bar(x, res["N_ratios"], color="teal", alpha=0.8)
    ax.axhline(phi_paasch, color="crimson", ls="--", lw=1.4, label=f"phi_paasch={phi_paasch:.5f}")
    for i, r in enumerate(res["N_ratios"]):
        dev = res["N_ratio_vs_phi"][i]  # (local)
        col = "green" if dev <= 0.01 else "black"  # (local)
        ax.text(i, r + 0.05, f"{r:.4f}\n({dev*100:.2f}%)", ha="center", fontsize=8, color=col)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=20, fontsize=8)
    ax.set_ylabel("N(j+1)/N(j)")
    ax.set_title(f"(d) N-ratios vs phi_paasch; 150/98={res['Np_over_NK']:.5f} (dev {res['phi_dev']*100:.3f}%)")
    ax.legend(fontsize=8)

    fig.suptitle(
        f"INV3-W3-4 Casimir-graded N(j)=7n test (L_max=12, tau_fold=0.19) — "
        f"VERDICT {res['verdict']}: {res['best_n7n']}-of-5 as 7n, "
        f"{res['n_nj_are_dims']}-of-5 ARE SU(3) dims",
        fontsize=12,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload
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


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    # ---- Reporting -------------------------------------------------------
    print(f"phi_paasch = {phi_paasch}  fN = sqrt(5)-1 = {res['fN']:.10f}")
    print(f"Paasch N(j) = {dict(zip(PAASCH_PARTICLES, PAASCH_NJ))}")
    print(f"N(j)/7      = {[round(nj/7, 4) for nj in PAASCH_NJ]}")
    print()
    print(f"L12 cache: {res['n_sectors']} sectors; dim(cache vs formula) mismatches = {res['dim_mismatch']}")
    print(f"S21c/S22 bridge lambda^2 = C2 + 3/4 (tau=0 bi-invariant) diagnostic: "
          f"max|resid|={res['bridge_resid_max']:.4f}, mean|resid|={res['bridge_resid_mean']:.4f} "
          f"(NONZERO at tau_fold=0.19 — Jensen deformation moved the spectrum off the bi-invariant form)")
    print()
    print("=== PARTIAL-COINCIDENCE DIAGNOSTIC: which N(j) ARE SU(3) dims? ===")
    for nj in PAASCH_NJ:
        isd = res["nj_is_dim"][nj]  # (local)
        realizers = res["nj_dim_realizers"].get(nj, [])  # (local)
        print(f"  N={nj:4d}: {'IS an SU(3) dim' if isd else 'NOT an SU(3) dim'}"
              + (f"  realized by (p,q)={realizers}" if realizers else ""))
    print(f"  => {res['n_nj_are_dims']}-of-5 of Paasch's N(j) coincide with SU(3) irrep dimensions.")
    print()
    print("=== CANDIDATE MODE-COUNTING FUNCTIONS (exact 7n / raw matches of 5) ===")
    for name, rep in res["candidate_report"].items():
        hit7 = [t for t, v in rep["seven_n_hits"].items() if v]  # (local)
        hitr = [t for t, v in rep["raw_hits"].items() if v]  # (local)
        print(f"  {name}: 7n={rep['n_7n_match']} {hit7}  raw={rep['n_raw_match']} {hitr}  (set size {rep['set_size']})")
    print(f"  BEST candidate: {res['best_candidate']} -> {res['best_n7n']}-of-5 as 7n, {res['best_raw']}-of-5 raw")
    print()
    print("=== M(j)=sqrt(N(j)) successive ratios vs fN ===")
    print(f"  M = {[round(m,4) for m in res['M_vals']]}")
    print(f"  ratios = {[round(r,4) for r in res['M_ratios']]}  (fN={res['fN']:.4f})")
    print(f"  rel-dev vs fN = {[round(d,4) for d in res['M_ratio_vs_fN']]} -> {res['n_M_ratio_match_fN']}/4 within 2%")
    print()
    print("=== N-ratios vs phi_paasch ===")
    print(f"  N-ratios = {[round(r,5) for r in res['N_ratios']]}")
    print(f"  N(p)/N(K) = 150/98 = {res['Np_over_NK']:.7f} vs phi_paasch={phi_paasch} -> dev {res['phi_dev']*100:.4f}%")
    print()
    print("=== Prefactor m0 (electron N=7) tie to M_KK ===")
    print(f"  m_e = {res['m_e_MeV']} MeV; M_KK = {res['M_KK_MeV']:.4e} MeV; "
          f"m_e/M_KK = {res['m_e_over_M_KK']:.4e} (14-OOM scale separation — content lives in ratios)")
    print()

    make_plot(res)

    # ---- Save npz --------------------------------------------------------
    table_pq = np.array([(r["p"], r["q"]) for r in res["rows"]], dtype=int)  # (local)
    table_dim = np.array([r["dim_formula"] for r in res["rows"]], dtype=int)  # (local)
    table_C2 = np.array([r["C2"] for r in res["rows"]], dtype=float)  # (local)
    table_C2int = np.array([r["C2_int"] for r in res["rows"]], dtype=int)  # (local)
    table_level = np.array([r["level"] for r in res["rows"]], dtype=int)  # (local)
    table_lammin = np.array([r["lam_min"] for r in res["rows"]], dtype=float)  # (local)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=res["verdict"],
        value=res["value"],
        paasch_particles=np.array(PAASCH_PARTICLES),
        paasch_Nj=np.array(PAASCH_NJ),
        fN=res["fN"],
        phi_paasch=float(phi_paasch),
        n_sectors=res["n_sectors"],
        dim_mismatch=res["dim_mismatch"],
        bridge_resid_max=res["bridge_resid_max"],
        bridge_resid_mean=res["bridge_resid_mean"],
        all_su3_dims=np.array(res["all_dims"]),
        nj_is_dim=np.array([res["nj_is_dim"][nj] for nj in PAASCH_NJ]),
        n_nj_are_dims=res["n_nj_are_dims"],
        best_candidate=res["best_candidate"],
        best_n7n=res["best_n7n"],
        best_raw=res["best_raw"],
        candidate_names=np.array(list(res["candidate_report"].keys())),
        candidate_n7n=np.array([res["candidate_report"][n]["n_7n_match"]
                                for n in res["candidate_report"]]),
        candidate_raw=np.array([res["candidate_report"][n]["n_raw_match"]
                                for n in res["candidate_report"]]),
        M_vals=np.array(res["M_vals"]),
        M_ratios=np.array(res["M_ratios"]),
        M_ratio_vs_fN=np.array(res["M_ratio_vs_fN"]),
        n_M_ratio_match_fN=res["n_M_ratio_match_fN"],
        Np_over_NK=res["Np_over_NK"],
        phi_dev=res["phi_dev"],
        N_ratios=np.array(res["N_ratios"]),
        N_ratio_vs_phi=np.array(res["N_ratio_vs_phi"]),
        m_e_over_M_KK=res["m_e_over_M_KK"],
        table_pq=table_pq,
        table_dim=table_dim,
        table_C2=table_C2,
        table_C2int=table_C2int,
        table_level=table_level,
        table_lammin=table_lammin,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print()

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    note = (f"best_candidate={res['best_candidate']}; 7n_match={res['best_n7n']}of5; "
            f"struct_match={res['n_struct']}of5; Nj_are_SU3_dims={res['n_nj_are_dims']}of5"
            f"(35,42_yes;7,98,150_no); 150/98={res['Np_over_NK']:.6f}_vs_phi_paasch_dev"
            f"{res['phi_dev']*100:.3f}pct; only_kaon-proton_M-ratio~fN")
    extra = [
        f"# INV3-W3-4 partial-coincidence: N(j)_are_SU3_dims={res['n_nj_are_dims']}of5 "
        f"(muon35,pion42 ARE dims; electron7,kaon98,proton150 NOT); "
        f"best_graded_count={res['best_candidate']} reproduces {res['best_n7n']}of5 as_7n; "
        f"7_is_mode-MULTIPLICITY_unit_not_irrep_dim; "
        f"N(p)/N(K)=150/98={res['Np_over_NK']:.6f}_dev_phi_paasch_{res['phi_dev']*100:.3f}pct"
    ]
    print_verdict_payload(res["verdict"], note, audit_sha, content_sha,
                          companion_note=f"best={res['best_candidate']}_7n{res['best_n7n']}of5",
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
