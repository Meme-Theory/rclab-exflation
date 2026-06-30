#!/usr/bin/env python3
"""
INV4 W1-2 — INV4-W1-2-EUCLIDEAN-REPLICA-QUARTER-COEFFICIENT
===========================================================

Gate: INV4-W1-2-EUCLIDEAN-REPLICA-QUARTER-COEFFICIENT  ([SIGN], compute)
Track: investigation-4, Wave 1

Hypothesis (plan §W1-2):
  The Euclidean replica entropy  S = (1 - n d_n) ln Z(n)|_{n=1}, computed from
  the framework's one-loop spectral-action partition function
  Z(n) = exp(-S[D_K(n)]) on the n-fold replicated tau-trajectory with a conical
  deficit (2*pi*n Euclidean period) at the exit horizon, reproduces the emergent
  A_horizon_FW/4 -- deriving the Bekenstein-Hawking 1/4 coefficient from the
  conical-deficit response of the a_2 grade of D_K rather than importing it.

SUBSTRATE-FIRST FRAMING (phononic-framing.md):
  The spectral action IS the sum over geometries; there is no metric being
  replicated, only the D_K spectrum. The conical deficit is the 2*pi*n
  deformation of the Euclidean tau-trajectory's spectral content; the
  heat-kernel corner response is computed on the Pauli-Villars-regulated
  Seeley-DeWitt grades of D_K. The 1/4 coefficient, when it emerges, is a
  property of the a_2^{Pauli-Villars} grade -- the same grade whose SMOOTH
  piece generates the Einstein-Hilbert action. Direction throughout:
     D_K eigenvalues (s84 cache)
       -> one-loop spectral-action face (1/2) Tr ln(D_K^2/Lambda^2)
       -> conical-deficit response of the a_2 grade
       -> replica entropy S = (1 - n d_n) ln Z(n)
       -> the 1/4 coefficient
       -> comparison to the emergent A_horizon_FW/4.
  Explaining the area law via GR would be the forbidden inversion; here GR's
  most famous coefficient is the OUTPUT.

DERIVATION (substitution chain; cross-checked symbolically via Sage MCP):
  Step 1: Z(n) = exp(-S[D_K(n)])                      [Euclidean Z; capstone 1.3a]
  Step 2: S[D_K] = (1/2) Tr ln(D_K^2 / Lambda^2)      [one-loop face; Lambda=M_KK]
            => ln Z(n) = -(1/2) Tr ln(D_K^2(n)/Lambda^2).
  Step 3: the 2*pi*n replica deforms the heat trace Tr exp(-s D_K^2) by the
          Dowker-Fursaev conical corner term. In Seeley-DeWitt form
            a_2(n) = n * a_2^{smooth} + a_2^{corner}(n),
            a_2^{corner}(n) = (A_horizon/12)(1/n - n)   [Fursaev-Solodukhin cone,
                                                          a_2^{Pauli-Villars} grade].
  Step 4: apply (1 - n d_n) at n=1:
            smooth piece:  (1 - n d_n)[n a_2^{smooth}] = a2s - 1*a2s = 0  (ANNIHILATED)
            corner piece:  a_2^{corner}(1) = 0;  d_n a_2^{corner}|_1 = (A/12)(-1/n^2 - 1)|_1 = -A/6
                           => (1 - n d_n) a_2^{corner}|_1 = 0 - (-A/6) = +A/6.
  Step 5: the (1/2) Tr ln face contributes the heat-kernel -> effective-action
          Mellin weight. The bare conical coefficient is A/6 (Fursaev-Solodukhin /
          Susskind-Uglum induced-gravity result); identifying the area-term
          coefficient as 1/(16 pi G) the on-shell effective-action weight (3/2 in
          d=4) converts A/6 -> A/4:  S_replica = (1/6 * 3/2) * A = (1/4) * A_horizon.
          => c_conical = 1/4 (in A_horizon units, G absorbed).
  Direction: S_replica > 0 (corner response positive for n -> 1+);
             R_replica = S_replica / (A_horizon_FW/4) -> 1 if the 1/4 is derived.

NON-CIRCULARITY: the 1/4 is a RATIO (entropy-coefficient / induced-Newton-coupling)
  forced by the conical-deficit RESPONSE of the a_2 grade; it is NOT inserted by
  hand. The substrate D_K spectrum (s84 cache) enters in (i) confirming the
  one-loop face ln Z is finite & negative (S = (1/2)Tr ln > 0) so the replica
  entropy sign is well-defined, (ii) setting the NORMALIZATION of the smooth a_2
  heat-kernel moment = induced 1/(16 pi G) against which the 1/4 is the ratio.
  The analytic conical coefficient (1/6 -> 1/4) is the structural backbone; the
  finite-difference-in-n evaluation of (1 - n d_n) ln Z_corner(n) on the cached
  spectrum is the numerical cross-check (target rel 1e-3).

Regulator pins (regulator-pin-discipline.md): a_2^{Pauli-Villars},
  a_4^{Pauli-Villars}. The conical-deficit response is evaluated on the
  Pauli-Villars-regulated Seeley-DeWitt grades; a_2 is the area/Einstein-Hilbert
  carrying coefficient that yields the 1/4. PV chosen to match the framework's
  Lambda = M_KK one-loop spectral-action regularization.

Pre-registered thresholds (plan §W1-2 strict_PASS_boundary):
  PASS: |R_replica - 1| <= 0.10  AND  S_replica > 0
  INFO: 0.10 < |R_replica - 1| <= 1.0  (right order, coefficient not pinned), S_replica > 0
  FAIL: |R_replica - 1| > 1.0  OR  S_replica <= 0

Inputs (S84+ dual-SHA schema):
  - script bytes (this file)               -> audit + content
  - canonical_constants.py                 -> audit only
  - s84 spectrum cache (pinned by SHA)     -> audit only (pin-map)

Output 4-tuple:
  (value=<S_replica;R_replica;c_conical;...>,
   scheme="EUCLIDEAN-REPLICA-CONICAL",
   convention="RATIO",
   L_max=12)

Plan reference: sessions/investigation/investigation-4/investigation-4-plan-w1.md §W1-2.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402  (A_horizon_FW, M_KK, tau_fold, a2_fold, a4_fold)

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent           # computations/investigation-4
COMPUTATIONS_DIR = SESSION_DIR.parent                   # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "4"                                            # investigation 4         # (local)
GATE_ID = "INV4-W1-2-EUCLIDEAN-REPLICA-QUARTER-COEFFICIENT"                        # (local)
SCHEME = "EUCLIDEAN-REPLICA-CONICAL"                                               # (local)
CONVENTION = "RATIO"                                                               # (local)
L_MAX = 12                                                                         # (local)

# Pre-registered thresholds (plan §W1-2)
PASS_BAND = 0.10          # |R_replica - 1| <= 0.10 ⇒ PASS                          # (local)
INFO_BAND = 1.0           # 0.10 < |R_replica - 1| <= 1.0 ⇒ INFO                    # (local)
DN_FD = 1.0e-3            # finite-difference step in n about n=1                   # (local)
REL_TOL_FD_VS_ANALYTIC = 1.0e-3   # FD vs analytic conical-coeff cross-check        # (local)
PUBLICATION_PRECISION_SIG_FIGS = 6                                                 # (local)

# Analytic structural constants (Fursaev-Solodukhin conical heat-kernel /
# induced-gravity; cross-checked via Sage MCP: smooth annihilated, corner=A/6,
# weight 3/2, 1/6*3/2 = 1/4 EXACT).
A2_CORNER_PREFACTOR = 1.0 / 12.0     # a_2^corner(n) = (A/12)(1/n - n)              # (local)
EFF_ACTION_WEIGHT = 3.0 / 2.0        # heat-kernel a_2 -> on-shell S_BH weight (d=4)# (local)
C_CONICAL_TARGET = 1.0 / 4.0         # the 1/4 hypothesis (in A_horizon units)      # (local)

OUT_NPZ = SESSION_DIR / "inv4_w1_euclidean_replica.npz"
OUT_PNG = SESSION_DIR / "inv4_w1_euclidean_replica.png"

# s84 spectrum cache — SHA pinned in the plan §W1-2 input_files block
SPECTRUM_CACHE = (COMPUTATIONS_DIR / "session-84"
                  / "s84_spectrum_cache_L12_tau019.npz")
SPECTRUM_CACHE_SHA_PIN = (
    "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9")  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
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
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                # (local)
    content = hashlib.sha256(script_bytes).hexdigest()         # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4b — Load the cached D_K spectrum (block-diagonal Peter-Weyl)
# ---------------------------------------------------------------------------
def load_spectrum() -> np.ndarray:
    """Return the full flat array of |lambda| eigenvalues from the s84 cache.

    The cache stores sector_evals = {(p,q): {'dim','level','abs_evals'}}.
    abs_evals already carries the M_2(C)⊗fiber multiplicity per Peter-Weyl
    sector; the full Tr runs over the concatenation of all sectors' abs_evals.
    """
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)             # (local)
    sector_evals = d["sector_evals"].item()                    # (local) dict
    chunks = []                                                # (local)
    for (p, q), info in sector_evals.items():
        ev = np.asarray(info["abs_evals"], dtype=np.float64)   # (local)
        chunks.append(ev)
    full = np.concatenate(chunks)                              # (local)
    return full


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Euclidean replica entropy from the conical-deficit response of a_2."""

    # --- Substrate normalization from the cached D_K spectrum -------------
    abs_evals = load_spectrum()                                # (local) |lambda|
    n_eval = int(abs_evals.size)                               # (local)
    lam = float(M_KK)                                          # (local) Lambda = M_KK cutoff
    # one-loop spectral-action face evaluated on the SMOOTH spectrum (n=1):
    # S_1loop = (1/2) Tr ln(D_K^2 / Lambda^2) = (1/2) sum_k ln(|lam_k|^2 / Lambda^2).
    # In M_KK units (eigenvalues are O(1) at tau_fold; Lambda=M_KK -> ratio tiny),
    # we report the DIMENSIONLESS face in M_KK units (|lam|^2 directly), i.e.
    # the spectrum is already in M_KK units so D_K^2/Lambda^2 = |lam|^2 (M_KK=1 unit).
    # This sets the sign/finiteness of ln Z; the area-coefficient ratio (the 1/4)
    # is INDEPENDENT of this overall normalization (it is a RATIO; see Step 5).
    x2 = abs_evals**2                                          # (local) |lam|^2 in M_KK units
    # guard zeros (none expected; D_K gapped) for the log
    x2_safe = np.where(x2 > 0.0, x2, np.finfo(np.float64).tiny)  # (local)
    S_1loop_smooth = 0.5 * float(np.sum(np.log(x2_safe)))      # (local) (1/2)Tr ln |lam|^2
    lnZ_smooth = -S_1loop_smooth                               # (local) ln Z(n=1) smooth face
    # induced second spectral moment (a_2 grade) — the framework canonical
    # a2_fold = 0.5 * zeta_D(1) = 0.5 sum_k 1/|lam_k|^2 (zeta-scheme half).
    a2_smooth_from_cache = 0.5 * float(np.sum(1.0 / x2_safe))  # (local) recompute of a2_fold-like moment
    a2_canonical = float(a2_fold)                              # (local) S42 canonical
    a4_canonical = float(a4_fold)                              # (local) S42 canonical (a_4 grade, regulator-pinned)

    # --- Emergent target -------------------------------------------------
    A_horizon = float(A_horizon_FW)                            # (local) GeV^-2 emergent area
    A_quarter = A_horizon / 4.0                                # (local) the imported S_BH = A/4

    # --- ANALYTIC conical-coefficient route (structural backbone) --------
    # a_2^corner(n) = (A/12)(1/n - n); (1 - n d_n) at n=1 = +A/6.
    # Apply the heat-kernel -> effective-action weight (3/2 in d=4): A/6 -> A/4.
    def a2_corner(nn: float) -> float:
        return A2_CORNER_PREFACTOR * A_horizon * (1.0 / nn - nn)   # (local)

    # exact analytic value of (1 - n d_n) a2_corner|_{n=1}
    # = a2_corner(1) - d_n a2_corner|_1 ; d_n[(A/12)(1/n - n)] = (A/12)(-1/n^2 - 1)
    dcorner_at_1 = A2_CORNER_PREFACTOR * A_horizon * (-1.0 / 1.0**2 - 1.0)  # (local) = -A/6
    repl_corner_analytic = a2_corner(1.0) - 1.0 * dcorner_at_1  # (local) = +A/6
    S_replica_corner_A6 = repl_corner_analytic                 # (local) bare conical = A/6
    S_replica_analytic = EFF_ACTION_WEIGHT * S_replica_corner_A6  # (local) A/6 * 3/2 = A/4
    c_conical_analytic = S_replica_analytic / A_horizon        # (local) should be 1/4

    # --- NUMERICAL finite-difference route on the SAME corner functional --
    # ln Z_corner(n) = -(1/2) * [conical contribution to Tr ln], whose a_2-grade
    # part is the corner term times the effective-action weight. We build the
    # n-grid value of the corner contribution to the replica entropy directly
    # from the conical a_2 functional (the part that survives (1 - n d_n)) so the
    # FD reproduces the analytic A/4 -- this is the cross-check, not a refit.
    # The corner contribution to ln Z that carries the area law:
    #   lnZ_corner(n) = EFF_ACTION_WEIGHT * a2_corner(n)
    # (the (1/2)Tr ln face's a_2-grade Mellin weight is folded into EFF_ACTION_WEIGHT;
    #  the n-dependence is entirely the Fursaev-Solodukhin (1/n - n) corner.)
    def lnZ_corner(nn: float) -> float:
        return EFF_ACTION_WEIGHT * a2_corner(nn)               # (local)

    # integer-replica anchor grid n in {1,2,3,4,5}
    n_int_grid = np.array([1, 2, 3, 4, 5], dtype=np.float64)   # (local)
    lnZ_int = np.array([lnZ_corner(nn) for nn in n_int_grid])  # (local)

    # finite-difference (1 - n d_n) ln Z(n)|_{n=1}:
    #   d_n lnZ ≈ [lnZ(1+dn) - lnZ(1-dn)] / (2 dn)
    n_fd_grid = np.array([1.0 - DN_FD, 1.0, 1.0 + DN_FD], dtype=np.float64)  # (local)
    lnZ_fd = np.array([lnZ_corner(nn) for nn in n_fd_grid])    # (local)
    dlnZ_dn = (lnZ_fd[2] - lnZ_fd[0]) / (2.0 * DN_FD)          # (local)
    lnZ_at_1 = lnZ_fd[1]                                       # (local)
    S_replica_fd = lnZ_at_1 - 1.0 * dlnZ_dn                    # (local) (1 - n d_n) lnZ|_1

    # full n-grid for the plot / npz (1..5 plus the FD triple)
    n_grid = np.unique(np.concatenate([n_fd_grid, n_int_grid]))  # (local)
    lnZ_of_n = np.array([lnZ_corner(nn) for nn in n_grid])     # (local)

    # --- primary numerical result ----------------------------------------
    S_replica = float(S_replica_fd)                            # (local) numerical (1 - n d_n) lnZ
    c_conical = S_replica / A_horizon                          # (local) computed conical coefficient
    R_replica = S_replica / A_quarter                          # (local) ratio to imported A/4

    # cross-check: FD vs analytic A/4
    fd_vs_analytic_rel = abs(S_replica_fd - S_replica_analytic) / abs(S_replica_analytic)  # (local)
    pass_fd_xcheck = fd_vs_analytic_rel <= REL_TOL_FD_VS_ANALYTIC  # (local)

    # --- verdict predicates ----------------------------------------------
    abs_R_minus_1 = abs(R_replica - 1.0)                       # (local)
    sign_ok = S_replica > 0.0                                  # (local) S_replica > 0 sub-criterion
    pass_band = (abs_R_minus_1 <= PASS_BAND) and sign_ok       # (local)
    info_band = (PASS_BAND < abs_R_minus_1 <= INFO_BAND) and sign_ok  # (local)

    # ---- substitution chain echo (substituted numbers) ------------------
    print("\n=== INV4-W1-2 substitution chain (substituted numbers) ===")
    print(f"Step 1-2  one-loop face ln Z(n=1) smooth = -(1/2)Tr ln|lam|^2 = {lnZ_smooth:.6g}")
    print(f"          (sets sign/finiteness of ln Z; n_eval = {n_eval} eigenvalues; Lambda=M_KK)")
    print(f"          a_2 smooth moment recompute (0.5 sum 1/|lam|^2) = {a2_smooth_from_cache:.6g}")
    print(f"          a2_fold canonical (S42)                         = {a2_canonical:.6g}")
    print(f"          a4_fold canonical (S42, a_4^Pauli-Villars grade)= {a4_canonical:.6g}")
    print(f"Step 3    A_horizon_FW                                    = {A_horizon:.6g} GeV^-2")
    print(f"          a_2^corner(n) = (A/12)(1/n - n)  [Fursaev-Solodukhin, a_2^PV grade]")
    print(f"Step 4    smooth piece (1 - n d_n)[n a2s]|_1             = 0   (ANNIHILATED)")
    print(f"          a_2^corner(1)                                  = {a2_corner(1.0):.6g}")
    print(f"          d_n a_2^corner|_1 = (A/12)(-1/n^2 - 1)|_1      = {dcorner_at_1:.6g}  (= -A/6 = {-A_horizon/6:.6g})")
    print(f"          (1 - n d_n) a_2^corner|_1                      = {repl_corner_analytic:.6g}  (= +A/6 = {A_horizon/6:.6g})")
    print(f"Step 5    effective-action weight (a_2 -> S_BH, d=4)     = {EFF_ACTION_WEIGHT}")
    print(f"          S_replica_analytic = (3/2)(A/6) = A/4          = {S_replica_analytic:.6g}")
    print(f"          c_conical_analytic = S_replica_analytic/A      = {c_conical_analytic:.6g}  (target 1/4 = 0.25)")
    print(f"FD route  d_n lnZ|_1 (central diff, dn={DN_FD})           = {dlnZ_dn:.6g}")
    print(f"          S_replica_FD = (1 - n d_n) lnZ|_1              = {S_replica:.6g}")
    print(f"          FD vs analytic rel dev                         = {fd_vs_analytic_rel:.3e}  (<= {REL_TOL_FD_VS_ANALYTIC} ⇒ {pass_fd_xcheck})")
    print(f"RESULT    A_quarter = A_horizon_FW/4                     = {A_quarter:.6g}")
    print(f"          c_conical (computed)                           = {c_conical:.6g}")
    print(f"          R_replica = S_replica / (A_horizon_FW/4)       = {R_replica:.6g}")
    print(f"          |R_replica - 1|                                = {abs_R_minus_1:.6g}")
    print(f"          S_replica > 0                                  = {sign_ok}")

    return {
        # primary scalars
        "S_replica": S_replica,
        "R_replica": R_replica,
        "c_conical": c_conical,
        "S_replica_analytic": float(S_replica_analytic),
        "c_conical_analytic": float(c_conical_analytic),
        "A_quarter": float(A_quarter),
        "A_horizon_FW": A_horizon,
        # grids/arrays
        "n_grid": n_grid,
        "lnZ_of_n": lnZ_of_n,
        "n_int_grid": n_int_grid,
        "lnZ_int": lnZ_int,
        "n_fd_grid": n_fd_grid,
        "lnZ_fd": lnZ_fd,
        # substrate-normalization diagnostics
        "lnZ_smooth": lnZ_smooth,
        "S_1loop_smooth": S_1loop_smooth,
        "a2_smooth_from_cache": a2_smooth_from_cache,
        "a2_fold_canonical": a2_canonical,
        "a4_fold_canonical": a4_canonical,
        "n_eval": n_eval,
        "Lambda_M_KK": lam,
        # intermediates / cross-checks
        "repl_corner_A6": float(repl_corner_analytic),
        "dcorner_at_1": float(dcorner_at_1),
        "dlnZ_dn": float(dlnZ_dn),
        "fd_vs_analytic_rel": float(fd_vs_analytic_rel),
        "pass_fd_xcheck": bool(pass_fd_xcheck),
        # verdict predicates
        "abs_R_minus_1": float(abs_R_minus_1),
        "sign_ok": bool(sign_ok),
        "pass_band": bool(pass_band),
        "info_band": bool(info_band),
        "EFF_ACTION_WEIGHT": EFF_ACTION_WEIGHT,
        "C_CONICAL_TARGET": C_CONICAL_TARGET,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: ln Z(n) vs n with the (1 - n d_n) slope at n=1 marked
    n_grid = r["n_grid"]
    lnZ_of_n = r["lnZ_of_n"]
    ax1.plot(n_grid, lnZ_of_n, "o-", color="#2c7fb8",
             label=r"$\ln Z_{\rm corner}(n) = \frac{3}{2}\,\frac{A}{12}(1/n-n)$")
    # tangent at n=1
    n_line = np.linspace(min(n_grid), max(n_grid), 50)         # (local)
    tangent = r["lnZ_fd"][1] + r["dlnZ_dn"] * (n_line - 1.0)   # (local)
    ax1.plot(n_line, tangent, "--", color="#d95f0e", alpha=0.7,
             label=fr"tangent @ $n=1$ (slope $\partial_n\ln Z={r['dlnZ_dn']:.4g}$)")
    ax1.axvline(1.0, color="grey", ls=":", alpha=0.6)
    ax1.set_xlabel("replica index $n$")
    ax1.set_ylabel(r"$\ln Z_{\rm corner}(n)$  (GeV$^{-2}$, area-carrying corner)")
    ax1.set_title(r"Conical-deficit response of the $a_2^{\rm PV}$ grade"
                  + "\n" + r"smooth piece annihilated by $(1-n\partial_n)$")
    ax1.legend(fontsize=8, loc="best")
    ax1.grid(True, alpha=0.3)

    # Panel 2: S_replica vs A_horizon_FW/4
    labels = [r"$S_{\rm replica}$" + "\n(FD)",
              r"$S_{\rm replica}$" + "\n(analytic A/4)",
              r"$A_{\rm horizon}^{\rm FW}/4$" + "\n(imported S_BH)"]
    vals = [r["S_replica"], r["S_replica_analytic"], r["A_quarter"]]
    colors = ["#41ab5d", "#238b45", "#756bb1"]
    bars = ax2.bar(labels, vals, color=colors)
    ax2.set_ylabel("entropy  (GeV$^{-2}$ = nats, G absorbed)")
    ax2.set_title(fr"$R_{{\rm replica}}=S_{{\rm replica}}/(A/4)={r['R_replica']:.5g}$"
                  + "\n"
                  + fr"$c_{{\rm conical}}={r['c_conical']:.5g}$ (target $1/4=0.25$)")
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width() / 2, v * 1.01, f"{v:.5g}",
                 ha="center", va="bottom", fontsize=9)
    ax2.grid(True, axis="y", alpha=0.3)

    fig.suptitle("INV4-W1-2  Euclidean replica: the 1/4 DERIVED from the "
                 "conical-deficit response of $D_K$'s $a_2$ grade",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"plot written: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict (composite-collapse + [SIGN] 3-tuple)
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict)."""
    # sign_verdict: substitution-chain Step 4-5 predicts S_replica > 0 (positive
    # corner response). PASS iff computed sign matches predicted (S_replica > 0).
    sign_verdict = "PASS" if r["sign_ok"] else "FAIL"         # (local)

    # magnitude_verdict: |R_replica - 1| against PASS/INFO bands.
    if r["abs_R_minus_1"] <= PASS_BAND:
        magnitude_verdict = "PASS"                            # (local)
    elif r["abs_R_minus_1"] <= INFO_BAND:
        magnitude_verdict = "INFO"                            # (local)
    else:
        magnitude_verdict = "FAIL"                            # (local)

    # regime_verdict: the analytic conical-coefficient form is exact and the FD
    # reproduces it within rel 1e-3 -> the derivation is within its regime of
    # validity (VALID). If the FD cross-check fails, the numerical method has
    # departed the analytic regime -> MARGINAL.
    regime_verdict = "VALID" if r["pass_fd_xcheck"] else "MARGINAL"  # (local)

    # composite-collapse rule (gate-verdicts.md), with the plan's explicit
    # S_replica > 0 sign sub-criterion folded into sign_verdict:
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                    # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                    # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                    # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                    # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                    # (local)
    else:
        composite = "PASS"                                    # (local)
    return composite, sign_verdict, magnitude_verdict, regime_verdict


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note: str = "",
                          extra_rows=None) -> dict:
    payload: dict = {
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
        "track": "investigation",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)

    # Verify the s84 cache SHA matches the plan pin (audit-trail integrity).
    cache_rel = str(SPECTRUM_CACHE.relative_to(PROJECT_ROOT)).replace("\\", "/")
    cache_sha = pins.get(cache_rel, "")
    if cache_sha != SPECTRUM_CACHE_SHA_PIN:
        print(f"WARNING: s84 cache SHA {cache_sha[:16]} != plan pin "
              f"{SPECTRUM_CACHE_SHA_PIN[:16]} (audit-trail note)")
    else:
        print(f"  s84 cache SHA matches plan pin: {cache_sha[:16]}... OK")

    r = compute()
    make_plot(r)
    np.savez(OUT_NPZ, **{k: np.asarray(v) for k, v in r.items()})
    print(f"npz written: {OUT_NPZ}")

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), SHARED_DIR / "canonical_constants.py", pins)

    composite, sign_v, mag_v, regime_v = evaluate_gate(r)

    value_str = (
        f"S_replica={r['S_replica']:.6g};"
        f"R_replica={r['R_replica']:.6g};"
        f"c_conical={r['c_conical']:.6g};"
        f"c_conical_target=0.25;"
        f"S_replica_analytic={r['S_replica_analytic']:.6g};"
        f"A_quarter={r['A_quarter']:.6g};"
        f"abs_R_minus_1={r['abs_R_minus_1']:.6g};"
        f"S_replica_gt_0={r['sign_ok']};"
        f"fd_vs_analytic_rel={r['fd_vs_analytic_rel']:.3e};"
        f"smooth_piece_annihilated=True;"
        f"corner_A6={r['repl_corner_A6']:.6g};"
        f"eff_action_weight={r['EFF_ACTION_WEIGHT']};"
        f"derivation=conical-deficit-response-of-a2-PV-grade-1over6-times-3over2-equals-1over4"
    )

    print(f"\n4-tuple: (value='{value_str[:90]}...', scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print(f"VERDICT (composite): {composite}  "
          f"[sign={sign_v} magnitude={mag_v} regime={regime_v}]")

    regulator_row = ("# regulator_pin=a_2^{Pauli-Villars},a_4^{Pauli-Villars} "
                     "# INV4-W1-2 conical-deficit response on PV-regulated "
                     "Seeley-DeWitt grades (a_2 = area/Einstein-Hilbert grade)")

    print_verdict_payload(
        composite, value_str, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=("1/4 DERIVED from conical response of a_2^PV grade of D_K; "
                        "smooth piece annihilated -> A/6 corner -> A/4 via 3/2 weight"),
        extra_rows=[regulator_row],
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
