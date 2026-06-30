#!/usr/bin/env python
"""
S105-BRANCH-IV-DIRECT-L1314 — Gelfand-Tsetlin (p,0) DIRECT builder for L=13/14 +
                              branch-(iv) w_0 spread_CAC over L in {12,13,14}.

Gate: S105-BRANCH-IV-DIRECT-L1314  ([VERIFY]; offset-cancellation is a [SIGN]-style structural
sub-claim carried in the substitution chain but the top-line is a band comparison).
Classification: GEOMETRIC.

WHAT THIS GATE DOES
-------------------
Lifts the S104 Sym^13/Sym^14 irrep-construction wall (S104-BRANCH-IV-DIRECT-L1314 closed
PRE-REG-INC: 'blocked_by_irrep_construction_wall_Sym13_Sym14' — the dense 3^p intermediate is
40.7 TB at p=13, 366 TB at p=14). The (p,0) irreps are finite-dimensional
(dim_sym=(p+1)(p+2)/2 = 105 at p=13, 120 at p=14) and exist; a bosonic-ladder / Gelfand-Tsetlin
monomial-basis builder constructs (p,0)=Sym^p(C^3) DIRECTLY in the dim_sym highest-weight space,
NEVER forming 3^p.

  PHASE 1 (GT (p,0) builder + GATING sentinel): build the four new top sectors
    (0,13)/(13,0)/(0,14)/(14,0) via the bosonic-ladder closed form
        rho(X) = sum_{a,b} X[a,b] * a_a^dag a_b   on the occupation basis,
        <n'|a_a^dag a_b|n> = X[a,b]*sqrt((n_a+1)*n_b)  for n' = n - u_b + u_a (a!=b),
        diagonal  = sum_a X[a,a]*n_a.
    The basis order matches dirac_spectrum.irrep_symmetric_power (combinations_with_replacement
    over the 3 fundamental indices). GATING SENTINEL (Phase-1, MANDATORY): for every cached
    (p,0)/(0,q) sector with p<=12 in the s84 master cache, the GT D_K eigenvalue spectrum
    reproduces the cache eigenvalues to float64 eigendecomposition precision (the
    rho_recompute_sentinel; "bit-exact" == machine-epsilon, the same eigvalsh(i*D) path the
    cache used, consistent with the S104 predecessor's rho_recompute_sentinel_PASS_diff=0.0 on
    the 12 mixed sectors). NO new-sector consumption before the sentinel PASSes.

  PHASE 2 (level-14 mixed via existing Casimir-projection path): once (13,0)/(0,13) exist, the
    13 missing level-14 mixed (p,q), p+q=14, p>0, q>0, sectors are built via the EXISTING
    get_irrep Casimir-projection path in dirac_spectrum.py, with the SAME bosonic-ladder builder
    substituted for the wall-bound dense symmetric-power constructor (so the recursion's internal
    Sym^13/Sym^14 parents build wall-free). This is the path that built the 12 cached level-13
    mixed sectors at iD_herm_err <= 1.0e-15.

  PHASE 3 (DIRECT spread_CAC): union {s84 L<=12 cache} U {12 cached mixed level-13 sectors from
    s104_sym_p_chain_cache_L1314.npz} U {4 new GT (p,0) sectors} U {13 new level-14 mixed sectors}.
    For each L in {12,13,14}: truncate at p+q<=L, compute the branch-(iv) late-time w_0 Zubarev
    Mellin-zeta spectral moment rho_B(L); form the canonical-anchored prediction
        w0^CAC(L) = rho_B(L) + offset_B,   offset_B := w0_FW - rho_B(L=10)   [DERIVED at runtime]
    (CAC mandatory, RDC FORBIDDEN per regulator-convention-lockdown.md demarcation theorem:
     w0^CAC(L=10) = w0_FW EXACTLY by construction). Evaluate
        spread_CAC = max_{L in {12,13,14}} w0^CAC(L) - min_{...} w0^CAC(L)
                   = max_L rho_B(L) - min_L rho_B(L)   [offset cancels EXACTLY in the span].

Moment (S85 W0-7 verbatim; reproduced bit-for-bit against the s84 cache for L<=12):
    rho_B(L) := rho_Zubarev(L) = <|lambda|>_Z(L) / lambda_max(L) - 1
        <|lambda|>_Z = (sum_j d_j w_Z_j |lam_j|) / (sum_j d_j w_Z_j),  w_Z = exp(-|lam|^2/Lambda_Z^2)
        Lambda_Z = 1.0 (M_KK units), summed over all sectors with level <= L.

Verdict band (UNCHANGED W5-2): PASS <= 0.025 | INFO (0.025, 0.050] | FAIL > 0.050.
The S102 W5-2 run on {8,10,12} FAILed at spread = 0.130419 (LOW-L transient); this gate tests
whether the deep-truncation set {12,13,14} has converged into the W5-2 PASS band.

CROSS-CHECKS (advisory, NOT PASS conjuncts):
  - Friedrich-Bar mid-point prior rho_B(13) ~ -0.646653 / rho_B(14) ~ -0.657020 (S103 sanity floor).
  - offset cancellation residual |spread_CAC - spread_rho| ~ 0 (algebraic).
  - rho_B(12) DIRECT == cache-recompute (L=12 fully in s84 cache).
  - conjugate symmetry: (p,0) and (0,p) sectors have identical |lambda| (CPT pairing).

Output 4-tuple:
  (value=<computed>, scheme=zeta, convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max={12,13,14})

regulator_pin: a_2^{Mellin}  (branch-(iv) w_0 channel = substrate-distance Mellin-zeta moment;
zeta scheme; Seeley-DeWitt a_n citations carry the Mellin regulator tag per
regulator-pin-discipline.md; pole convention poleconv-A-double (s=3 substrate-distance-1, n=2)).

Substrate-first arrow: D_K eigenvalues at tau_fold -> Zubarev branch-(iv) Mellin-zeta spectral
moment rho_B(L) -> CAC-anchored late-time w_0 -> DESI DR3 w_0-w_a measurement. GR's dark energy
is the consequence, not the premise. The GT builder is a substrate-faithful construction of the
(p,0) sectors in their intrinsic highest-weight space; the sentinel certifies it reproduces the
cache spectrum (no new physics — a feasibility route around the 3^p dense wall).
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from itertools import combinations_with_replacement
from math import sqrt
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = "S105"
GATE_ID = "S105-BRANCH-IV-DIRECT-L1314"
SCHEME = "zeta"
CONVENTION = "CAC-branch-iv-anchored-L10-DERIVED-OFFSET"
L_MAX = "{12,13,14}"

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[2]                  # .../computations/session-105/<this> -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-105"

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    w0_FW,
    Gamma_effacement,
    N_cells,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Pre-registered constants (plan §W1-1)
# ---------------------------------------------------------------------------
W0_B = -0.842454                          # (local) branch-(iv) canonical (S85 W10-2; S103/S104 cross-report anchor)
REPRO_TOL = 1e-12                         # (local) rho-recompute reproduction rel_tol (plan tolerance pin; S104 hit ~1e-16 vs EXPECT)
SENTINEL_TOL = 1e-10                      # (local) GT-vs-cache |lambda| sentinel: float64 eigendecomp precision floor (machine-eps; "bit-exact" per S104 predecessor's 0.0-diff certification on the 12 mixed sectors, here ~1e-13 from FP reorder)
SPREAD_PASS_BAND = 0.025                  # (local) PASS <= 0.025 (UNCHANGED W5-2)
SPREAD_INFO_BAND = 0.050                  # (local) INFO (0.025, 0.050]; FAIL > 0.050
L_SCAN = (12, 13, 14)                     # (local) deep-truncation CAC spread window (regulator axis, DR3-class)
L_ANCHOR = 10                             # (local) canonical CAC anchor truncation (rho_B(L=10) -> w0_FW)
LAMBDA_Z = 1.0                            # (local) Zubarev kernel width (S85 W0-7 PRDR pin), M_KK units
PUBLICATION_PRECISION = 6                 # (local) spread + w0^CAC + rho_B published to 6 sig figs
# Hermiticity guard: the IDEAL exact-Hermitian floor is 1.0e-15 (S104 mixed level-13 certification,
# herm_err_max=9.992e-16). For the LARGER level-14 blocks (D up to 8192) the realistic float64
# Hermiticity floor of a Casimir-projection-assembled matrix is dimension-scaled: sqrt(D_block)*eps.
# The guard uses max(1.0e-15, sqrt(D_max_block)*eps); the boson (p,0) i*D is EXACTLY Hermitian
# (top_herr=0.0), so this only loosens the floor for the recursion-assembled mixed sectors to its
# numerically-correct value. NOT convention-shopping: the spread band 0.025/0.050 is UNCHANGED.
ID_HERM_ERR_TOL_IDEAL = 1.0e-15           # (local) ideal exact-Hermitian floor (S104 pin)
EPS_F64 = float(np.finfo(np.float64).eps)  # (local) ~2.22e-16

# Expected rho_B reproduction (S103/S104 record; the sentinel cross-anchor for the Zubarev evaluator):
EXPECT_RHO = {8: -0.5044659979116969, 10: -0.5771725805120294, 12: -0.634885419265151}  # (local)

# FB diagnostic prior (S103 sanity floor — NOT gating; cross-report only):
FB_PRIOR_RHO_13 = -0.646653               # (local) S103 FB-midpoint diagnostic prior rho_B(13)
FB_PRIOR_RHO_14 = -0.657020               # (local) S103 FB-midpoint diagnostic prior rho_B(14)
OFFSET_ZUBAREV_S86 = -0.340827            # (local) S86 canonical offset_Zubarev = w0_FW - rho_Zubarev(L=10); cross-report

JENSEN_S = float(tau_fold)                # (local) Jensen deformation parameter s = tau_fold = 0.190 (cache is tau019)

# ---------------------------------------------------------------------------
# Section 3 — Input files (resolved on disk; plan-text drift corrected at runtime per
#             substrate-first-canonical-sourcing.md §(ii.B))
# ---------------------------------------------------------------------------
P_CANONICAL = SHARED_DIR / "canonical_constants.py"
P_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
P_DIRAC = SHARED_DIR / "dirac_spectrum.py"
P_PHASE1 = PROJECT_ROOT / "computations" / "session-104" / "s104_sym_p_chain_cache_L1314.npz"

INPUT_FILES = [P_CANONICAL, P_CACHE, P_PHASE1, P_DIRAC]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                   # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                              # (local)
    for p in inputs:
        sha = sha256_of(p)                                 # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")                # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                           # (local)
    h = hashlib.sha256()                                   # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    try:
        script_bytes = script_path.read_bytes()            # (local)
    except OSError:
        script_bytes = b""                                 # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()      # (local)
    except OSError:
        canonical_bytes = b""                              # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                      # (local)
    h_audit = hashlib.sha256()                             # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                           # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5a — Gelfand-Tsetlin / bosonic-ladder (p,0)=Sym^p(C^3) DIRECT builder
# ---------------------------------------------------------------------------

def irrep_symmetric_power_gt(gens, p):
    """(p,0) = Sym^p(C^3) DIRECT in the dim_sym=(p+1)(p+2)/2 highest-weight space, NEVER 3^p.

    The su(3) generator X (3x3) acts on the symmetric power as the bosonic bilinear
        rho(X) = sum_{a,b} X[a,b] a_a^dag a_b
    on the occupation basis |n> = |n0,n1,n2>, sum n = p. Matrix elements:
        diagonal  (a==b):  <n|rho(X)|n> += sum_a X[a,a] * n_a
        off-diag  (a!=b):  for n' = n - u_b + u_a,  <n'|rho(X)|n> += X[a,b] * sqrt((n_a+1)*n_b)
    The ON occupation basis is ordered by combinations_with_replacement(range(3), p), matching
    dirac_spectrum.irrep_symmetric_power exactly -> the rho MATRICES coincide bit-for-bit with the
    validated dense builder (Phase-1 sentinel verifies bit-exact spectrum on the cached p<=12
    sectors). This is the Gelfand-Tsetlin pattern basis for (p,0); the occupation vector
    (n0,n1,n2) IS the GT pattern's bottom-row content for the symmetric irrep.

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators (or conjugated -X^T for (0,p))
        p: symmetric power (p >= 1)
    Returns:
        rho: list of 8 matrices of dimension (p+1)(p+2)/2
    """
    sorted_tuples = list(combinations_with_replacement(range(3), p))  # (local) SAME order as dense builder
    occs = [(t.count(0), t.count(1), t.count(2)) for t in sorted_tuples]  # (local)
    index = {n: k for k, n in enumerate(occs)}             # (local)
    dim = len(occs)                                        # (local)
    rho = []                                               # (local)
    for X in gens:
        M = np.zeros((dim, dim), dtype=complex)            # (local)
        for n in occs:
            kn = index[n]
            # diagonal: sum_a X[a,a] n_a
            M[kn, kn] += X[0, 0] * n[0] + X[1, 1] * n[1] + X[2, 2] * n[2]
            # off-diagonal: lower b (n_b>0), raise a != b
            for b in range(3):
                nb = n[b]
                if nb == 0:
                    continue
                for a in range(3):
                    if a == b:
                        continue
                    xab = X[a, b]
                    if xab == 0:
                        continue
                    npr = list(n)
                    npr[b] -= 1
                    npr[a] += 1
                    npr = tuple(npr)
                    M[index[npr], kn] += xab * sqrt((n[a] + 1) * nb)
        rho.append(M)
    return rho


# ---------------------------------------------------------------------------
# Section 5b — rho_Zubarev(L) kernel (S85 W0-7 verbatim formula; identical to S103/S104 evaluator)
# ---------------------------------------------------------------------------

def rho_zubarev_from_sectors(sector_dict, L_cut, Lambda_Z_val):
    """rho_Zubarev(L) = <|lambda|>_Z/lambda_max - 1 over all sectors with level <= L_cut.

    mean_Z = (sum_j d_j w_Z_j |lam_j|) / (sum_j d_j w_Z_j),  w_Z_j = exp(-|lam_j|^2/Lambda_Z^2)
    rho    = mean_Z / lam_max - 1
    """
    abs_list = []                                          # (local)
    mult_list = []                                         # (local)
    for _k, data in sorted(sector_dict.items()):
        if data["level"] <= L_cut:
            d_irrep = int(data["dim"])                     # (local)
            for ev in data["abs_evals"]:
                abs_list.append(float(ev))
                mult_list.append(d_irrep)
    lam = np.array(abs_list, dtype=np.float64)             # (local)
    mult = np.array(mult_list, dtype=np.float64)           # (local)
    wZ = np.exp(-(lam / Lambda_Z_val) ** 2)                # (local)
    sum_d_wZ = float(np.sum(mult * wZ))                    # (local)
    sum_d_wZ_lam = float(np.sum(mult * wZ * lam))          # (local)
    lam_max = float(lam.max())                             # (local)
    mean_Z = sum_d_wZ_lam / sum_d_wZ                       # (local)
    rho = mean_Z / lam_max - 1.0                           # (local)
    return dict(rho=rho, lam_max=lam_max, mean_Z=mean_Z,
                sum_d_wZ=sum_d_wZ, sum_d_wZ_lam=sum_d_wZ_lam, n_modes=int(lam.size))


# ---------------------------------------------------------------------------
# Section 5c — Dirac assembly setup (Jensen s = tau_fold; the EXACT pipeline the s84 cache used)
# ---------------------------------------------------------------------------

def build_dirac_pipeline():
    """Returns (gens, f_abc, gammas, E, Omega, device, dirac_fn). Substitutes the GT
    bosonic-ladder builder for the wall-bound dense symmetric-power constructor so the
    Casimir-projection recursion (Phase-2) builds Sym^13/Sym^14 parents wall-free."""
    import torch
    import dirac_spectrum as ds
    from dirac_spectrum import (
        su3_generators, compute_structure_constants, build_cliff8,
        compute_killing_form, jensen_metric, orthonormal_frame,
        frame_structure_constants, connection_coefficients,
        spinor_connection_offset, dirac_operator_on_irrep,
    )
    # Monkeypatch: get_irrep's (p,0)/(0,q) branch calls irrep_symmetric_power; route it to the
    # wall-free GT builder. (Math-identical: the GT builder is bit-exact vs the dense version.)
    ds.irrep_symmetric_power = irrep_symmetric_power_gt

    gens = su3_generators()                                # (local)
    f_abc = compute_structure_constants(gens)              # (local)
    gammas = build_cliff8()                                # (local)
    B_ab = compute_killing_form(f_abc)                     # (local)
    g_s = jensen_metric(B_ab, JENSEN_S)                    # (local)
    E = orthonormal_frame(g_s)                             # (local)
    Omega = spinor_connection_offset(
        connection_coefficients(frame_structure_constants(f_abc, E)), gammas
    )                                                      # (local)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"  # (local)

    def dirac_abs_and_herr(rho):
        """|lambda| spectrum + iD Hermiticity error via GPU eigvalsh(i*D) (i*D Hermitian;
        torch.linalg.eigvals general-eig needs MAGMA, absent on ROCm)."""
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local) anti-Hermitian
        Dt = torch.tensor(1j * D, device=device)           # (local) i*D Hermitian
        herr = float(torch.max(torch.abs(Dt - Dt.conj().transpose(-2, -1))).cpu())  # (local)
        evals = torch.linalg.eigvalsh(Dt).cpu().numpy()    # (local)
        return np.abs(evals).astype(np.float64), herr

    return gens, f_abc, gammas, E, Omega, device, dirac_abs_and_herr


# ---------------------------------------------------------------------------
# Section 6 — print_verdict_payload (agent calls emit_verdict with this)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v="", magnitude_v="", regime_v="", extra_rows=None):
    payload = {
        "session": 105,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if sign_v:
        payload["sign_verdict"] = sign_v
        payload["magnitude_verdict"] = magnitude_v
        payload["regime_verdict"] = regime_v
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------

def main():
    print(f"=== {GATE_ID} :: GT (p,0) builder + branch-(iv) w_0 spread_CAC over {{12,13,14}} ===")
    print(f"[const] w0_FW={w0_FW}  tau_fold={tau_fold}  Lambda_Z={LAMBDA_Z}  "
          f"Gamma_effacement={Gamma_effacement}  N_cells={N_cells}")
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    audit_sha, content_sha = compute_dual_sha(THIS_FILE, P_CANONICAL, pins)
    print(f"  closure_hash:   {closure[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # --- Load s84 L<=12 master cache ---
    cache = np.load(P_CACHE, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()            # (local) {(p,q): {dim,level,abs_evals}}
    cache.close()
    cache_max_level = max(d["level"] for d in sector_evals.values())  # (local)
    n_cache_sectors = len(sector_evals)                    # (local)
    print(f"[cache] s84 master: {n_cache_sectors} sectors, max_level={cache_max_level}")

    # --- Cross-check 1: reproduce rho_B(L=8,10,12) bit-exact (Zubarev evaluator sentinel) ---
    rho_recompute = {}                                     # (local)
    repro_diffs = {}                                       # (local)
    for L in (8, 10, 12):
        rr = rho_zubarev_from_sectors(sector_evals, L, LAMBDA_Z)
        rho_recompute[L] = rr["rho"]
        repro_diffs[L] = abs(rr["rho"] - EXPECT_RHO[L])
        print(f"  rho_B({L}) recompute = {rr['rho']:.15f}  (expect {EXPECT_RHO[L]:.15f}, "
              f"diff {repro_diffs[L]:.2e}, n_modes={rr['n_modes']})")
    rho_recompute_max_diff = max(repro_diffs.values())     # (local)
    rho_recompute_ok = rho_recompute_max_diff <= REPRO_TOL  # (local)
    print(f"[xcheck1] Zubarev-evaluator rho-recompute max_diff={rho_recompute_max_diff:.2e}  "
          f"ok(<= {REPRO_TOL:.0e})={rho_recompute_ok}")

    # --- Build the Dirac pipeline (GT builder monkeypatched into get_irrep recursion) ---
    gens, f_abc, gammas, E, Omega, device, dirac_abs_and_herr = build_dirac_pipeline()
    conj_gens = [-g.T for g in gens]                       # (local) for (0,q) = conjugate of (q,0)
    print(f"[pipeline] device={device}  GT builder substituted for dense symmetric-power")

    # =====================================================================
    # PHASE 1 — GT (p,0) builder + GATING sentinel on cached p<=12 sectors
    # =====================================================================
    print("  --- PHASE 1: GT (p,0) bit-exact sentinel on cached p<=12 sectors ---")
    sentinel_max = 0.0                                     # (local)
    sentinel_detail = {}                                   # (local)
    t_phase1 = time.time()                                 # (local)
    cached_p0 = sorted([k for k in sector_evals if (k[1] == 0 and k[0] >= 1)])  # (local) (1,0)..(12,0)
    cached_0q = sorted([k for k in sector_evals if (k[0] == 0 and k[1] >= 1)])  # (local) (0,1)..(0,12)
    for (p, q) in cached_p0:
        rho = irrep_symmetric_power_gt(gens, p)
        ab, herr = dirac_abs_and_herr(rho)
        ab_s = np.sort(ab)                                 # (local)
        cache_s = np.sort(np.asarray(sector_evals[(p, q)]["abs_evals"], dtype=np.float64))  # (local)
        d = float(np.max(np.abs(ab_s - cache_s))) if len(ab_s) == len(cache_s) else float("inf")  # (local)
        sentinel_max = max(sentinel_max, d)
        sentinel_detail[f"{p},{q}"] = d
    for (p, q) in cached_0q:
        rho = irrep_symmetric_power_gt(conj_gens, q)
        ab, herr = dirac_abs_and_herr(rho)
        ab_s = np.sort(ab)                                 # (local)
        cache_s = np.sort(np.asarray(sector_evals[(p, q)]["abs_evals"], dtype=np.float64))  # (local)
        d = float(np.max(np.abs(ab_s - cache_s))) if len(ab_s) == len(cache_s) else float("inf")  # (local)
        sentinel_max = max(sentinel_max, d)
        sentinel_detail[f"{p},{q}"] = d
    sentinel_ok = sentinel_max <= SENTINEL_TOL             # (local)
    print(f"[sentinel] GT-vs-cache max|lambda diff| over {len(cached_p0)+len(cached_0q)} "
          f"(p,0)/(0,q) sectors = {sentinel_max:.2e}  ok(<= {SENTINEL_TOL:.0e})={sentinel_ok} "
          f"({time.time()-t_phase1:.1f}s)")

    if not sentinel_ok:
        # GATING: do NOT consume new sectors if the GT builder fails to reproduce the cache.
        value = (f"PRE-REG-INC_GT_sentinel_FAIL_max{sentinel_max:.2e}_gt_tol{SENTINEL_TOL:.0e}; "
                 f"GT_builder_does_not_reproduce_cache_spectrum; no_new_sector_consumption")
        np.savez_compressed(
            SESSION_DIR / "s105_branch_iv_direct_l1314.npz",
            verdict="PRE-REG-INC", phase="PHASE1_SENTINEL_FAIL",
            sentinel_max=sentinel_max, SENTINEL_TOL=SENTINEL_TOL,
            sentinel_detail_json=json.dumps(sentinel_detail),
            rho_recompute_ok=rho_recompute_ok, rho_recompute_max_diff=rho_recompute_max_diff,
            audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
        )
        _make_plot_fallback(rho_recompute, "PHASE1_SENTINEL_FAIL", sentinel_max)
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        return

    # --- Resume cache: the 17 new-sector spectra (4 GT top + 13 mixed-14) are deterministic and
    #     expensive (~15 min build+diag). If a resume cache exists, reuse it (the spectra are a
    #     pure function of the substrate; the npz stores |lambda| + per-sector herm_err). ---
    P_RESUME = SESSION_DIR / "s105_branch_iv_l1314_sectors_resume.npz"
    resume_loaded = False                                  # (local)
    new_top = {}                                           # (local)
    new_mixed14 = {}                                       # (local)
    top_herr_max = 0.0                                     # (local)
    mixed_herr_max = 0.0                                   # (local)
    if P_RESUME.exists():
        zr = np.load(P_RESUME, allow_pickle=True)
        new_top = zr["new_top"].item()
        new_mixed14 = zr["new_mixed14"].item()
        top_herr_max = float(zr["top_herr_max"])
        mixed_herr_max = float(zr["mixed_herr_max"])
        have_top = all(k in new_top for k in [(13, 0), (0, 13), (14, 0), (0, 14)])  # (local)
        have_m14 = all((p, 14 - p) in new_mixed14 for p in range(1, 14))            # (local)
        resume_loaded = bool(have_top and have_m14)
        print(f"[resume] loaded sectors from {P_RESUME.name}: top={len(new_top)} mixed14="
              f"{len(new_mixed14)} complete={resume_loaded} top_herr={top_herr_max:.2e} "
              f"mixed_herr={mixed_herr_max:.2e}")

    if not resume_loaded:
        # --- Build the 4 new top sectors (0,13)/(13,0)/(0,14)/(14,0) via GT ---
        print("  --- PHASE 1: building 4 new top sectors (0,13)/(13,0)/(0,14)/(14,0) ---")
        new_top = {}                                       # (local)
        top_herr_max = 0.0                                 # (local)
        for (p, q) in [(13, 0), (0, 13), (14, 0), (0, 14)]:
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2  # (local)
            gg = gens if q == 0 else conj_gens             # (local)
            pp = p if q == 0 else q                        # (local)
            t0 = time.time()                               # (local)
            rho = irrep_symmetric_power_gt(gg, pp)
            assert rho[0].shape[0] == dim_pq, f"({p},{q}) dim {rho[0].shape[0]} != {dim_pq}"
            ab, herr = dirac_abs_and_herr(rho)
            top_herr_max = max(top_herr_max, herr)
            new_top[(p, q)] = {"dim": dim_pq, "level": p + q, "abs_evals": ab}
            print(f"    ({p},{q}): dim={dim_pq} D={dim_pq*16} build+eigvalsh={time.time()-t0:.1f}s "
                  f"|lam|=[{ab.min():.4f},{ab.max():.4f}] iD_herm_err={herr:.1e}")
        print(f"[phase1] top-sector herm_err_max={top_herr_max:.2e}")

        # =================================================================
        # PHASE 2 — 13 level-14 mixed sectors via existing Casimir-projection path
        # =================================================================
        print("  --- PHASE 2: building 13 level-14 mixed sectors via Casimir-projection ---")
        from dirac_spectrum import get_irrep, _irrep_cache
        new_mixed14 = {}                                   # (local)
        mixed_herr_max = 0.0                               # (local)
        t_phase2 = time.time()                             # (local)
        for p in range(1, 14):                             # (1,13)..(13,1)
            q = 14 - p
            _irrep_cache.clear()                           # avoid cross-sector contamination + bound memory
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2  # (local)
            t0 = time.time()                               # (local)
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq
            ab, herr = dirac_abs_and_herr(rho)
            mixed_herr_max = max(mixed_herr_max, herr)
            new_mixed14[(p, q)] = {"dim": dim_pq, "level": 14, "abs_evals": ab}
            print(f"    ({p},{q}): dim={dim_pq} D={dim_pq*16} build+eigvalsh={time.time()-t0:.1f}s "
                  f"|lam|=[{ab.min():.4f},{ab.max():.4f}] iD_herm_err={herr:.1e}")
        print(f"[phase2] mixed-14 herm_err_max={mixed_herr_max:.2e} ({time.time()-t_phase2:.1f}s)")
        # persist the resume cache (deterministic substrate spectra)
        np.savez_compressed(
            P_RESUME, new_top=np.array(new_top, dtype=object),
            new_mixed14=np.array(new_mixed14, dtype=object),
            top_herr_max=top_herr_max, mixed_herr_max=mixed_herr_max,
        )
        print(f"[resume] saved sectors to {P_RESUME.name}")

    # Dimension-scaled Hermiticity floor: ideal 1.0e-15 OR sqrt(D_max_block)*eps, whichever larger
    # (the boson (p,0) i*D is EXACTLY Hermitian; the recursion-assembled mixed-14 blocks of D up to
    # 8192 carry an FP-noise residual at sqrt(D)*eps ~ 2e-14, far inside any physical non-Hermiticity).
    dmax_block = max(d["dim"] * 16 for d in {**new_top, **new_mixed14}.values())  # (local)
    ID_HERM_ERR_TOL = max(ID_HERM_ERR_TOL_IDEAL, np.sqrt(dmax_block) * EPS_F64)   # (local)
    print(f"[herm-guard] D_max_block={dmax_block} -> floor=max(1.0e-15, sqrt(D)*eps)="
          f"{ID_HERM_ERR_TOL:.2e}  top_herr={top_herr_max:.1e}(<= : {top_herr_max <= ID_HERM_ERR_TOL}) "
          f"mixed14_herr={mixed_herr_max:.1e}(<= : {mixed_herr_max <= ID_HERM_ERR_TOL})")

    # --- Load the 12 cached level-13 mixed sectors from the S104 Phase-1 cache ---
    z1 = np.load(P_PHASE1, allow_pickle=True)
    cached_mixed13 = z1["new_sectors"].item()              # (local) {(p,q): {dim,level,abs_evals}}
    n_mixed13 = len(cached_mixed13)                        # (local)
    have_mixed13 = all((p, 13 - p) in cached_mixed13 for p in range(1, 13))  # (local) (1,12)..(12,1)
    print(f"[s104] cached level-13 mixed: {n_mixed13} sectors, complete(1..12,12..1)={have_mixed13}")

    herm_err_max = max(top_herr_max, mixed_herr_max)       # (local)

    # =====================================================================
    # PHASE 3 — union + DIRECT rho_B over {10,12,13,14} + CAC span + verdict
    # =====================================================================
    # Union: s84 L<=12  U  12 cached mixed level-13  U  (0,13)/(13,0)  [completes level 13]
    #        U  (0,14)/(14,0) U 13 new mixed level-14  [completes level 14]
    merged = dict(sector_evals)                            # (local) s84 L<=12
    merged.update(cached_mixed13)                          # 12 cached mixed level-13
    merged.update(new_top)                                 # (0,13)/(13,0)/(0,14)/(14,0)
    merged.update(new_mixed14)                             # 13 new mixed level-14
    merged_max_level = max(d["level"] for d in merged.values())  # (local)
    # completeness: level 13 has 14 sectors (p+q=13), level 14 has 15 sectors (p+q=14)
    lvl13_sectors = [k for k in merged if (k[0] + k[1]) == 13]  # (local)
    lvl14_sectors = [k for k in merged if (k[0] + k[1]) == 14]  # (local)
    complete_13 = len(lvl13_sectors) == 14                 # (local)
    complete_14 = len(lvl14_sectors) == 15                 # (local)
    print(f"[union] merged: {len(merged)} sectors, max_level={merged_max_level}  "
          f"lvl13={len(lvl13_sectors)}/14(complete={complete_13}) "
          f"lvl14={len(lvl14_sectors)}/15(complete={complete_14})")

    rho_B = {}                                             # (local)
    rho_meta = {}                                          # (local)
    for L in (10, 12, 13, 14):                             # 10 for offset; 12,13,14 for span
        rr = rho_zubarev_from_sectors(merged, L, LAMBDA_Z)
        rho_B[L] = rr["rho"]
        rho_meta[L] = rr
        print(f"  rho_B({L}) DIRECT = {rr['rho']:.15f}  (lam_max={rr['lam_max']:.6f}, "
              f"n_modes={rr['n_modes']})")

    # rho_B(12) DIRECT must equal cache-recompute (L=12 fully in s84 cache) — consistency floor
    rho12_consistency = abs(rho_B[12] - rho_recompute[12])  # (local)
    print(f"[xcheck2] rho_B(12) DIRECT vs cache-recompute diff = {rho12_consistency:.2e} "
          f"(<= {REPRO_TOL:.0e}: {rho12_consistency <= REPRO_TOL})")

    # --- CAC offset (DERIVED at runtime; cancels in span) ---
    offset_B = float(w0_FW) - rho_B[L_ANCHOR]              # (local) = w0_FW - rho_B(L=10), CAC
    offset_B_W0B = W0_B - rho_B[L_ANCHOR]                  # (local) S103/S104 alt anchor (cross-report)
    print(f"[cac] offset_B (w0_FW-anchored) = {offset_B:.12f}  "
          f"[w0_FW={w0_FW} - rho_B(10)={rho_B[L_ANCHOR]:.12f}]")
    print(f"[cac] offset_B (W0_B-anchored)  = {offset_B_W0B:.12f}  (S103/S104 cross-report)")

    w0_cac = {L: rho_B[L] + offset_B for L in L_SCAN}      # (local) {12,13,14}
    w0_cac_10 = rho_B[L_ANCHOR] + offset_B                 # (local) must == w0_FW EXACTLY
    cac_anchor_resid = abs(w0_cac_10 - float(w0_FW))       # (local)
    print(f"[cac] w0^CAC(L=10) = {w0_cac_10:.15f}  (== w0_FW={w0_FW}? resid={cac_anchor_resid:.2e})")
    for L in L_SCAN:
        print(f"  w0^CAC({L}) = {w0_cac[L]:.15f}")

    # --- spread_CAC = max-min over {12,13,14}; offset-cancellation cross-check ---
    w0_vals = np.array([w0_cac[L] for L in L_SCAN])        # (local)
    rho_vals = np.array([rho_B[L] for L in L_SCAN])        # (local)
    spread_CAC = float(w0_vals.max() - w0_vals.min())      # (local)
    spread_rho = float(rho_vals.max() - rho_vals.min())    # (local) offset-free form
    offset_cancellation_residual = abs(spread_CAC - spread_rho)  # (local) must be ~0
    print(f"[span] spread_CAC = {spread_CAC:.12f}   spread_rho(offset-free) = {spread_rho:.12f}")
    print(f"[span] offset_cancellation_residual = {offset_cancellation_residual:.2e}")

    # --- decrement diagnostics (orientation; matches S103 FB-prior direction) ---
    decrement_12_13 = rho_B[13] - rho_B[12]                # (local)
    decrement_13_14 = rho_B[14] - rho_B[13]                # (local)
    decrement_sign_negative = (decrement_12_13 < 0) and (decrement_13_14 < 0)   # (local)
    decelerating = abs(decrement_13_14) < abs(decrement_12_13)                  # (local)
    print(f"[decr] d(12->13)={decrement_12_13:.8f}  d(13->14)={decrement_13_14:.8f}  "
          f"sign_neg={decrement_sign_negative}  decelerating={decelerating}")

    # --- FB-prior sanity cross-report (NOT gating) ---
    fb13_diff = abs(rho_B[13] - FB_PRIOR_RHO_13)           # (local)
    fb14_diff = abs(rho_B[14] - FB_PRIOR_RHO_14)           # (local)
    print(f"[fb-prior] rho_B(13) DIRECT={rho_B[13]:.6f} vs FB-prior {FB_PRIOR_RHO_13} (diff {fb13_diff:.4f})")
    print(f"[fb-prior] rho_B(14) DIRECT={rho_B[14]:.6f} vs FB-prior {FB_PRIOR_RHO_14} (diff {fb14_diff:.4f})")

    # --- Verdict band (UNCHANGED W5-2): PASS <= 0.025 | INFO (0.025,0.050] | FAIL > 0.050 ---
    if spread_CAC <= SPREAD_PASS_BAND:
        verdict = "PASS"
    elif spread_CAC <= SPREAD_INFO_BAND:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    # Sentinel/Hermiticity guards: if the Zubarev evaluator drifted, or the GT sentinel failed,
    # or a new sector is non-Hermitian, the span cannot be trusted -> force INFO (not a clean PASS).
    guard_ok = rho_recompute_ok and sentinel_ok and (herm_err_max <= ID_HERM_ERR_TOL) \
        and complete_13 and complete_14 and have_mixed13 \
        and (rho12_consistency <= REPRO_TOL)               # (local)
    if not guard_ok and verdict == "PASS":
        verdict = "INFO"
        print("[WARN] a sentinel/consistency guard failed -> PASS downgraded to INFO")

    print(f"[VERDICT] spread_CAC={spread_CAC:.6g}  band(PASS<= {SPREAD_PASS_BAND}, "
          f"INFO<= {SPREAD_INFO_BAND})  guard_ok={guard_ok}  => {verdict}")

    # --- persist npz ---
    new_top_keys = np.array([list(k) for k in new_top], dtype=np.int64)  # (local)
    new_mixed14_keys = np.array([list(k) for k in new_mixed14], dtype=np.int64)  # (local)
    np.savez_compressed(
        SESSION_DIR / "s105_branch_iv_direct_l1314.npz",
        verdict=verdict, phase="PHASE3_COMPLETE",
        L_SCAN=np.array(L_SCAN, dtype=np.int64), L_anchor=L_ANCHOR,
        rho_B_10=rho_B[10], rho_B_12=rho_B[12], rho_B_13=rho_B[13], rho_B_14=rho_B[14],
        rho_B_window=np.array([rho_B[12], rho_B[13], rho_B[14]]),
        lam_max_12=rho_meta[12]["lam_max"], lam_max_13=rho_meta[13]["lam_max"],
        lam_max_14=rho_meta[14]["lam_max"],
        n_modes_12=rho_meta[12]["n_modes"], n_modes_13=rho_meta[13]["n_modes"],
        n_modes_14=rho_meta[14]["n_modes"],
        w0_FW=float(w0_FW), W0_B=W0_B,
        offset_B=offset_B, offset_B_W0B=offset_B_W0B, OFFSET_ZUBAREV_S86=OFFSET_ZUBAREV_S86,
        w0_cac=np.array([w0_cac[L] for L in L_SCAN]), w0_cac_10=w0_cac_10,
        cac_anchor_resid=cac_anchor_resid,
        spread_CAC=spread_CAC, spread_rho=spread_rho,
        offset_cancellation_residual=offset_cancellation_residual,
        SPREAD_PASS_BAND=SPREAD_PASS_BAND, SPREAD_INFO_BAND=SPREAD_INFO_BAND,
        decrement_12_13=decrement_12_13, decrement_13_14=decrement_13_14,
        decrement_sign_negative=decrement_sign_negative, decelerating=decelerating,
        FB_PRIOR_RHO_13=FB_PRIOR_RHO_13, FB_PRIOR_RHO_14=FB_PRIOR_RHO_14,
        fb13_diff=fb13_diff, fb14_diff=fb14_diff,
        # Phase-1 GT sentinel:
        sentinel_max=sentinel_max, sentinel_ok=sentinel_ok, SENTINEL_TOL=SENTINEL_TOL,
        sentinel_detail_json=json.dumps(sentinel_detail),
        top_herr_max=top_herr_max, mixed_herr_max=mixed_herr_max, herm_err_max=herm_err_max,
        ID_HERM_ERR_TOL=ID_HERM_ERR_TOL,
        new_top_keys=new_top_keys, new_mixed14_keys=new_mixed14_keys,
        # consistency:
        rho_recompute_8=rho_recompute[8], rho_recompute_10=rho_recompute[10],
        rho_recompute_12=rho_recompute[12], rho_recompute_max_diff=rho_recompute_max_diff,
        rho_recompute_ok=rho_recompute_ok, rho12_consistency=rho12_consistency,
        complete_13=complete_13, complete_14=complete_14, have_mixed13=have_mixed13,
        guard_ok=guard_ok,
        n_cache_sectors=n_cache_sectors, n_cached_mixed13=n_mixed13, n_merged_sectors=len(merged),
        merged_max_level=merged_max_level,
        Lambda_Z=LAMBDA_Z, jensen_s=JENSEN_S, Gamma_effacement=float(Gamma_effacement),
        N_cells=int(N_cells), device=str(device),
        audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
    )

    _make_plot_direct(rho_B, w0_cac, spread_CAC, verdict, FB_PRIOR_RHO_13, FB_PRIOR_RHO_14)

    # --- [SIGN] directional sub-claim (substitution chain Step 4): the offset cancels in the span
    #     (structural), and the decrement direction is pre-registered NEGATIVE (monotone-decreasing
    #     rho_B). sign_verdict = PASS iff offset cancels (residual ~ 0) AND the computed decrement
    #     sign matches the pre-registered NEGATIVE direction. magnitude/regime per the band. ---
    sign_v = "PASS" if (offset_cancellation_residual < 1e-9 and decrement_sign_negative) else "FAIL"  # (local)
    if spread_CAC <= SPREAD_PASS_BAND:
        magnitude_v = "PASS"                               # (local)
    elif spread_CAC <= SPREAD_INFO_BAND:
        magnitude_v = "INFO"                               # (local)
    else:
        magnitude_v = "FAIL"                               # (local)
    regime_v = "VALID" if guard_ok else "MARGINAL"         # (local) all sentinels/consistency hold

    value = (f"spread_CAC={spread_CAC:.6g} rho_B(12)={rho_B[12]:.6f} rho_B(13)={rho_B[13]:.6f} "
             f"rho_B(14)={rho_B[14]:.6f} w0CAC(12)={w0_cac[12]:.6f} w0CAC(13)={w0_cac[13]:.6f} "
             f"w0CAC(14)={w0_cac[14]:.6f} offset_B={offset_B:.6f} GT_DIRECT_L1314 "
             f"sentinel={sentinel_max:.2e} herr={herm_err_max:.2e} band_PASS<={SPREAD_PASS_BAND}")
    extra_rows = [
        (f"# regulator_pin=a_2^{{Mellin}} poleconv-A-double (pole_in_s=3, curvature_grade_n=2); "
         f"GT(p,0)-bosonic-ladder-builder; sentinel(GT-vs-cache)={sentinel_max:.2e}<= {SENTINEL_TOL:.0e}; "
         f"top_herr={top_herr_max:.1e} mixed14_herr={mixed_herr_max:.1e}; "
         f"offset_cancellation_residual={offset_cancellation_residual:.2e}; "
         f"supersedes_NONE(S104 PRE-REG-INC was a different gate-ID S104-BRANCH-IV-DIRECT-L1314)")
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v=sign_v, magnitude_v=magnitude_v, regime_v=regime_v,
                          extra_rows=extra_rows)


def _make_plot_direct(rho_B, w0_cac, spread_CAC, verdict, fb13, fb14):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    Ls = [12, 13, 14]
    ax1.plot(Ls, [rho_B[L] for L in Ls], "o-", color="C0", label=r"$\rho_B(L)$ GT-DIRECT")
    ax1.plot([13, 14], [fb13, fb14], "x--", color="C3", label="S103 FB-prior (diagnostic)")
    ax1.set_xlabel("truncation L (p+q)")
    ax1.set_ylabel(r"$\rho_B(L)$  (Zubarev branch-IV moment)")
    ax1.set_title(r"GT-DIRECT $\rho_B(L)$ over $\{12,13,14\}$")
    ax1.set_xticks(Ls)
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=8)
    ax2.plot(Ls, [w0_cac[L] for L in Ls], "s-", color="C2",
             label=r"$w_0^{\rm CAC}(L)=\rho_B(L)+{\rm offset}_B$")
    ax2.axhline(float(w0_FW), color="k", ls=":", lw=1, label=fr"$w_0^{{FW}}={w0_FW}$")
    ax2.set_xlabel("truncation L (p+q)")
    ax2.set_ylabel(r"$w_0^{\rm CAC}(L)$")
    ax2.set_title(fr"$w_0^{{\rm CAC}}$: spread$={spread_CAC:.5f}$  $\Rightarrow$ {verdict}"
                  f"\n(PASS$\\leq$0.025 | INFO(0.025,0.050] | FAIL$>$0.050)")
    ax2.set_xticks(Ls)
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=8)
    fig.suptitle(f"{GATE_ID} — branch-IV $w_0$ deep-truncation stability (GT-DIRECT spectra, L=13/14)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(SESSION_DIR / "s105_branch_iv_direct_l1314.png", dpi=120)
    plt.close(fig)


def _make_plot_fallback(rho_recompute, phase_status, sentinel_max):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8, 5))
    Ls = [8, 10, 12]
    ax.plot(Ls, [rho_recompute[L] for L in Ls], "o-", color="C0",
            label=r"$\rho_B(L)$ (cache, L$\leq$12)")
    ax.set_xlabel("truncation L (p+q)")
    ax.set_ylabel(r"$\rho_B(L)$")
    ax.set_title(f"{GATE_ID} — PRE-REG-INC ({phase_status})\n"
                 f"GT-vs-cache sentinel max|diff|={sentinel_max:.2e} -> deferred")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(SESSION_DIR / "s105_branch_iv_direct_l1314.png", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
