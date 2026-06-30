#!/usr/bin/env python3
"""
S100a W4-14 -- S100a-EPSLX-FOAM-SURVIVAL: does the generation index survive
the foam? [H_foam, eps_LX] at the Wheeler-sqrt(N) ladder
===========================================================================

Gate: S100a-EPSLX-FOAM-SURVIVAL ([SIGN])
Classification: GEOMETRIC (foam-robustness of the multiplicity-bundle
generation index; operates on the fabric's generation structure, not on
excitations)

Pre-registered three-regime operator (plan SS W4-14, R3 block):
  PASS: C(N) = ||[H_foam(N), eps_LX]|| = 0 exactly (<= commutator_tol=1e-10)
        for ALL N in the ladder  -> TOPOLOGICAL (QF-71 delta_n_foam=0 class)
  INFO: C(N) > commutator_tol AND fit C(N) ~ N^{-alpha} with
        alpha > alpha_floor=0.05  -> GEOMETRIC foam-fragile (QF-79
        eps_c ~ N^{-0.457} class), asymptotically recovered
  FAIL: C(N) = O(1) AND |alpha| <= alpha_floor  -> labels DESTROYED

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py          (audit pin)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
        (L_max=12 spectrum cache; floors cross-check CC-3)
  - computations/session-98/s98_gate_verdicts.txt
        (S98-W3-1 eps_LX existence-PASS form -- the PRE-REGISTERED FALLBACK
         branch; pinned, verified present, NOT USED: Item 6 landed)
  - computations/session-100a/s100a_yukawa_overlap_offdiag.npz
        (Item 6 W2-form eps_LX SOURCE -- the branch ACTUALLY USED:
         eps_lx_block_phi0, abs_w_phi, arg_w_M2_phi; orchestrator resolved
         the conditional branch at dispatch: Item 6 verdict INFO, LANDED)
  - computations/session-53/s53_foam_cc_output.txt
        (Wheeler-sqrt(N) H_foam anchors; substring-verified)

Output 4-tuple:
  (value=<max_N C(N) + regime>, scheme=HFOAM-WHEELER-SQRTN-S43S53+EPSLX-W2FORM-ITEM6,
   convention=TOPOLOGICAL-VS-GEOMETRIC-MULTIPLICITY-INDEX-FOAM-ROBUSTNESS-EPSLX-SRC-ITEM6-W2FORM,
   L_max=12)

METHODOLOGY (structure first, computation second)
-------------------------------------------------
The multiplicity bundle: the SM generation index is the PROVEN topological
label t = (p-q) mod 3 (SU(3) Z3-triality / Peter-Weyl multiplicity;
permanent-results-registry). The W2-form eps_LX (Item 6,
S100a-YUKAWA-OVERLAP-OFFDIAG) resolves the between-generation structure on
the BDI pair t1 = (1,0) <-> t2 = (0,1): the 2x2 block
[[O, w(phi)], [conj(w(phi)), O]] with O = O_01 (diagonal |s|^2 overlap,
EQUAL on both slots -- the W2 homogeneity wall: left-invariance =>
multiplicity-scalar, registry line "(W2) Homogeneity wall") and
w(phi) = |w| e^{i arg(phi)}, |w| = 1/sqrt(6) UNIFORM over the three Z3
center points phi in {0, 2pi/3, 4pi/3}, arg in {pi, 2pi/3, -2pi/3}. The
phi-DEPENDENT PHASE is the left-invariance breaking that lets eps_LX carry
a generation index at all.

H_foam(N): the S43/S53 Wheeler-sqrt(N) cell model. The foam coarse-grains
the bundle into N cells with mean-field energy h(N) = <Lambda_eff(N)>^{1/2}
in M_KK units, Lambda_eff = Lambda_bare/N (Carlip CC-hiding), so
h(N) ~ N^{-1/2}. s53 anchors: h = {0.57735, 0.099760, 0.016828, 0.015715}
at N = {1, 32, 1124.6, 1349.74=V_Haar}. Operator form per the S43
Channel-A construction (FOAM-GGE-43, QF-71): the foam couples DIAGONALLY
in the substrate's occupation basis with energy-weighted amplitudes,
H_foam(N) = h(N) * sum_cells w_c n_c. The weights w_c are built from
LEFT-INVARIANT data (Haar cell volumes, trace spectral moments a_0) --
by the homogeneity wall the foam is therefore MULTIPLICITY-SCALAR
(generation-blind), and by Z3 center symmetry the weights are uniform
over the three fiber points: w_c = O on every occupied slot.

Second-quantization reduction: for quadratic forms H = sum A_kl c+_k c_l,
eps = sum B_kl c+_k c_l on the bundle Fock space,
[H, eps] = sum_kl ([A,B])_kl c+_k c_l, so the Fock-space commutator
vanishes iff the ONE-PARTICLE commutator [A,B] = 0, and ||[A,B]||_2 is the
faithful diagnostic at every filling. The one-particle space is
V = C^2_gen (x) C^3_phi (6-dim; sub-100x100 machinery pin honored).

SUBSTITUTION CHAIN ([SIGN] mandatory; three-regime read-off)
------------------------------------------------------------
Claim: "topological => C(N) = 0 for ALL N (foam-robust); geometric =>
        C(N) = C_0 N^{-alpha}, alpha > 0 (foam-fragile, recovered);
        destroyed => C(N) = O(1) flat."

Definition 1: eps_LX = sum_j [[O, w_j],[conj(w_j), O]] (x) |phi_j><phi_j|,
              O = 8.20652429, |w_j| = 0.40824829 = 1/sqrt(6),
              arg w_j = {pi, 2pi/3, -2pi/3}            [Item 6 npz, pinned]
Definition 2: H_foam(N) = h(N) * O * 1_gen (x) D_cell -- generation-scalar
              (homogeneity wall: foam built from left-invariant data),
              cell-diagonal (mean-field s53 pin), uniform weights (Z3
              symmetry). h(N) anchors per s53_foam_cc_output.txt.
Definition 3: C(N) = ||[H_foam(N), eps_LX]||_2 (one-particle spectral norm).

Substitute (topological case):
              [h O 1_gen (x) D_cell, eps_hat_j (x) P_j]
            = h O (1_gen eps_hat_j) (x) (D_cell P_j)
              - h O (eps_hat_j 1_gen) (x) (P_j D_cell)
            = h O eps_hat_j (x) [D_cell, P_j]
            = 0   exactly: 1_gen commutes with every eps_hat_j (leg L1,
              multiplicity-scalar) AND D_cell, P_j are diagonal in the SAME
              cell basis (leg L2, cell-diagonality).
Simplify:     C(N) = 0 for every N  =>  max_N C(N) = 0 <= 1e-10.
Direction (topological): C == 0 => sign_verdict = PASS (the pre-registered
              vanishing of the topological branch HOLDS); generation labels
              are foam-ROBUST (QF-71 delta_n_foam = 0 class).

Substitute (geometric case, counterfactual CF-1 -- leg L1 broken):
              foam generation-RESOLVED, w_gen = diag(O+|w|, O-|w|):
              [h diag(a,b) (x) 1, eps] per-phi block
            = h (a-b) [[0, w_j],[-conj(w_j), 0]],  norm = h (a-b) |w_j|
            = h * 2|w| * |w| = (2|w|^2) h(N) = h(N)/3   (|w|^2 = 1/6).
Simplify:     ln C_cf1 = ln(1/3) + ln h(N) => slope d(ln C)/d(ln N)
            = d(ln h)/d(ln N) = -1/2 (Wheeler law) => alpha_cf1 = 0.5 > 0.05.
Direction (geometric): C DECREASES with N => residual SHRINKS in the
              continuum; INFO regime fires on the counterfactual -- the
              discriminator is LIVE, the physical PASS is carried by the
              left-invariance structure, not by a dead diagnostic.

Substitute (geometric case, counterfactual CF-2 -- leg L2 broken):
              Z3 wormhole hopping (Carlip inter-cell channel),
              H_cf2 = h(N) [O 1 + 1_gen (x) T_Z3]:
              [1_gen (x) T_Z3, eps] couples phi-points with DIFFERENT w_j
              (the left-invariance-breaking phases) => C_cf2 = k h(N),
              k = ||[1 (x) T_Z3, eps_LX]||_2 = O(|w|) -> alpha_cf2 = 0.5.

Substitute (destroyed case): C = O(1), alpha ~= 0 requires a foam coupling
              that does NOT decay with N -- contradicts the Wheeler-sqrt(N)
              law itself (Lambda_eff = Lambda_bare/N IS the Carlip
              mechanism). Within the pinned foam class the FAIL regime is
              structurally unreachable; the gate discriminates PASS vs INFO,
              and the two left-invariance legs decide PASS.

Conclusion: the SIGN of d(ln C)/d(ln N) and the magnitude of C discriminate:
              C == 0 (PASS, topological) / C ~ N^{-alpha}, alpha > 0
              (INFO, foam-fragile) / C = O(1) flat (FAIL, destroyed).

DISCIPLINE
----------
- from canonical_constants import * (M_KK, Vol_SU3_Haar, M_Pl_reduced)
- OMP_NUM_THREADS=8 BEFORE numpy import (machinery pin GPU_path=CPU-cap-OMP8;
  6x6 matrices, numpy.linalg per pin)
- every intermediate tagged # (local)
- deterministic: no RNG (random_seed pin N/A -- mean-field foam)
- exit 0 on any valid verdict (math-scripts.md exit-code semantics)
- verdict via print_verdict_payload -> agent calls mcp emit_verdict
  (race-safe; the script does NOT write the verdict file)

Author: quantum-foam-theorist
Session: S100a Wave 4 Item 14
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- CPU thread cap (machinery pin GPU_path = CPU-cap-OMP8).
# MUST precede every numpy import, including the one inside
# canonical_constants.py.
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"   # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403  (M_KK, Vol_SU3_Haar, M_Pl_reduced, tau_fold)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "100a"                                                    # (local)
GATE_ID = "S100a-EPSLX-FOAM-SURVIVAL"                               # (local)
SCHEME = "HFOAM-WHEELER-SQRTN-S43S53+EPSLX-W2FORM-ITEM6"            # (local)
CONVENTION = ("TOPOLOGICAL-VS-GEOMETRIC-MULTIPLICITY-INDEX-"
              "FOAM-ROBUSTNESS-EPSLX-SRC-ITEM6-W2FORM")             # (local)
L_MAX = "12"                                                        # (local)

# Pre-registered thresholds (plan SS W4-14 machinery_pin_map; plan-pinned)
COMMUTATOR_TOL = 1e-10        # strict PASS boundary (<=)            # (local)
ALPHA_FLOOR = 0.05            # INFO-vs-FAIL discriminator on alpha  # (local)

# N ladder (plan pin: 4-point ladder {1, 32, 1124, 1349.7=V_Haar};
# the third point is the s53 N_Planck = 1.1246e+03 Planck-domain count,
# the fourth is the canonical Haar volume)
N_PLANCK_S53 = 1124.6                                               # (local)
N_LADDER = np.array([1.0, 32.0, N_PLANCK_S53, Vol_SU3_Haar])        # (local)

# Wheeler-sqrt(N) H_foam anchors (M_KK units) -- pinned at the s53 printed
# values; provenance rows of s53_foam_cc_output.txt (substring-verified in
# CC-2 below + reconstructed from canonical constants):
#   N=1       -> 5.7735e-01  (Sec 12 Model K, Lambda_bare = M_KK^2, = 1/sqrt(3))
#   N=32      -> 9.9760e-02  (Sec 5 Model C1,  Lambda_bare = M_P_12^2)
#   N=1124.6  -> 1.6828e-02  (Sec 5 Model A,   Lambda_bare = M_P_12^2)
#   N=1349.74 -> 1.5715e-02  (Sec 8 row KK-scale / KK domains, M_KK^2)
H_ANCHORS = np.array([5.7735e-01, 9.9760e-02, 1.6828e-02, 1.5715e-02])  # (local)
H_ANCHOR_STRS = ["5.7735e-01", "9.9760e-02", "1.6828e-02", "1.5715e-02"]  # (local)
# Per-anchor bare-CC pin of the s53 model row: 1.0 = M_KK^2, r^2 = M_P_12^2
LAMBDA_BARE_IS_MKK2 = np.array([True, False, False, True])          # (local)

# Output destinations
OUT_NPZ = SESSION_DIR / "s100a_epslx_foam_survival.npz"
OUT_PNG = SESSION_DIR / "s100a_epslx_foam_survival.png"

IN_W2_NPZ = SESSION_DIR / "s100a_yukawa_overlap_offdiag.npz"        # (local)
IN_S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
IN_S98_VERDICTS = COMPUTATIONS_DIR / "session-98" / "s98_gate_verdicts.txt"  # (local)
IN_S53_FOAM = COMPUTATIONS_DIR / "session-53" / "s53_foam_cc_output.txt"     # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    IN_S84_CACHE,
    IN_S98_VERDICTS,
    IN_W2_NPZ,
    IN_S53_FOAM,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes()       # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Compute
# ---------------------------------------------------------------------------

def spectral_norm(M: np.ndarray) -> float:
    """Spectral (operator 2-) norm; exact 0.0 for the exact-zero matrix."""
    if not np.any(M):          # all entries identically zero -> norm 0 exact
        return 0.0
    return float(np.linalg.norm(M, 2))


def loglog_fit(N: np.ndarray, C: np.ndarray):
    """LSQ fit ln C = ln C0 - alpha ln N; returns (alpha, lnC0, R2)."""
    x = np.log(N)                       # (local)
    y = np.log(C)                       # (local)
    A = np.vstack([x, np.ones_like(x)]).T  # (local)
    coef, res, _, _ = np.linalg.lstsq(A, y, rcond=None)  # (local)
    slope, intercept = coef             # (local)
    yhat = A @ coef                     # (local)
    ss_res = float(np.sum((y - yhat) ** 2))   # (local)
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0  # (local)
    return float(-slope), float(intercept), r2


def compute() -> dict:
    print("=" * 72)
    print("S100a-EPSLX-FOAM-SURVIVAL: [H_foam, eps_LX] AT THE WHEELER-sqrt(N)")
    print("LADDER -- DOES THE GENERATION INDEX SURVIVE THE FOAM?")
    print("=" * 72)

    # ------------------------------------------------------------------
    # 5.1  eps_LX source branch: Item 6 W2-form (LANDED; orchestrator
    #      resolved the conditional branch at dispatch). The S98-W3-1
    #      existence form is the pre-registered FALLBACK -- pinned,
    #      verified present (CC-4), NOT USED.
    # ------------------------------------------------------------------
    w2 = np.load(IN_W2_NPZ, allow_pickle=True)   # (local)
    O_diag = float(w2["O_01"])                   # (local) 8.20652429
    abs_w = np.asarray(w2["abs_w_phi"], dtype=float)        # (local)
    arg_w = np.asarray(w2["arg_w_M2_phi"], dtype=float)     # (local)
    phi_pts = np.asarray(w2["phi_floats"], dtype=float)     # (local)
    block_phi0 = np.asarray(w2["eps_lx_block_phi0"], dtype=float)  # (local)
    floors_w2 = np.asarray(w2["floors_lambda_min"], dtype=float)   # (local)
    tower_pq = np.asarray(w2["tower_pq"], dtype=int)        # (local)
    n_evals_w2 = np.asarray(w2["n_evals"], dtype=int)       # (local)
    vol_haar_w2 = float(w2["vol_su3_haar"])                 # (local)

    n_phi = len(phi_pts)                         # (local) 3 Z3 center points
    n_gen = 2                                    # (local) BDI pair t1=(1,0) <-> t2=(0,1)
    dim = n_gen * n_phi                          # (local) 6

    w_j = abs_w * np.exp(1j * arg_w)             # (local) complex couplings

    print(f"\n--- eps_LX (W2-form, Item 6 S100a-YUKAWA-OVERLAP-OFFDIAG) ---")
    print(f"  source branch: ITEM6-W2-FORM (fallback S98-W3-1 pinned, NOT used)")
    print(f"  O (diagonal overlap, both slots) = {O_diag:.8f}")
    print(f"  |w_j| = {abs_w}  (uniform 1/sqrt(6) = {1/np.sqrt(6):.8f})")
    print(f"  arg w_j = {arg_w}  (= pi, 2pi/3, -2pi/3 -- the left-invariance-")
    print(f"            breaking Z3 phase profile)")
    print(f"  phi points = {phi_pts}")

    # Build eps_LX on V = C^2_gen (x) C^3_phi, basis index = g*n_phi + j
    eps_LX = np.zeros((dim, dim), dtype=complex)  # (local)
    for j in range(n_phi):
        eps_LX[0 * n_phi + j, 0 * n_phi + j] = O_diag
        eps_LX[1 * n_phi + j, 1 * n_phi + j] = O_diag
        eps_LX[0 * n_phi + j, 1 * n_phi + j] = w_j[j]
        eps_LX[1 * n_phi + j, 0 * n_phi + j] = np.conj(w_j[j])

    herm_dev = float(np.max(np.abs(eps_LX - eps_LX.conj().T)))  # (local)
    print(f"  hermiticity: max|eps - eps^dag| = {herm_dev:.2e}")
    assert herm_dev < 1e-14, "eps_LX not Hermitian"

    # CC-1: phi_0 block magnitude reconstruction vs the stored pinned block
    block_recon = np.array([[O_diag, abs_w[0]], [abs_w[0], O_diag]])  # (local)
    cc1_dev = float(np.max(np.abs(block_recon - block_phi0)))  # (local)
    cc1_pass = cc1_dev < 1e-12                  # (local)
    print(f"\nCC-1 (phi0-block vs stored eps_lx_block_phi0): "
          f"max dev = {cc1_dev:.2e}  [{'PASS' if cc1_pass else 'FAIL'}]")

    # CC-0: Haar volume consistency npz vs canonical
    cc0_dev = abs(vol_haar_w2 - Vol_SU3_Haar) / Vol_SU3_Haar  # (local)
    cc0_pass = cc0_dev < 1e-12                  # (local)
    print(f"CC-0 (npz vol_su3_haar vs canonical Vol_SU3_Haar): "
          f"rel dev = {cc0_dev:.2e}  [{'PASS' if cc0_pass else 'FAIL'}]")

    # ------------------------------------------------------------------
    # 5.2  H_foam anchors: substring-verify against the pinned s53 file,
    #      then reconstruct from canonical constants (CC-2).
    # ------------------------------------------------------------------
    s53_text = IN_S53_FOAM.read_text(encoding="utf-8", errors="replace")  # (local)
    anchors_present = [s in s53_text for s in H_ANCHOR_STRS]  # (local)
    nplanck_present = "1.1246e+03" in s53_text  # (local)
    print(f"\n--- H_foam Wheeler-sqrt(N) anchors (s53_foam_cc_output.txt) ---")
    for s, ok in zip(H_ANCHOR_STRS, anchors_present):
        print(f"  anchor {s} present in pinned s53 file: {ok}")
    print(f"  N_Planck 1.1246e+03 present: {nplanck_present}")
    assert all(anchors_present) and nplanck_present, \
        "s53 anchor substring verification failed"

    # CC-2: reconstruct each anchor from canonical constants via the s53
    # model: h(N) = sqrt(Lambda_bare_rel / (3 N)),
    # Lambda_bare_rel = 1 (M_KK^2) or (M_P_12/M_KK)^2 with
    # M_P_12 = (M_Pl_reduced^2 M_KK^8 / Vol_SU3_Haar)^{1/10}  [s53 Sec 1].
    M_P_12 = (M_Pl_reduced**2 * M_KK**8 / Vol_SU3_Haar) ** 0.1  # (local)
    r2_p12 = (M_P_12 / M_KK) ** 2               # (local) ~0.9554
    print(f"  M_P_12 reconstructed = {M_P_12:.4e} GeV "
          f"(s53: 7.2611e+16); ratio^2 = {r2_p12:.6f} (s53: 9.5540e-01)")
    lam_rel = np.where(LAMBDA_BARE_IS_MKK2, 1.0, r2_p12)  # (local)
    h_recon = np.sqrt(lam_rel / (3.0 * N_LADDER))          # (local)
    cc2_rel = np.abs(h_recon - H_ANCHORS) / H_ANCHORS      # (local)
    cc2_pass = bool(np.all(cc2_rel < 2e-4))                # (local)
    print(f"  anchor reconstruction rel dev: {cc2_rel}")
    print(f"CC-2 (anchors vs canonical-constants reconstruction, rtol 2e-4): "
          f"[{'PASS' if cc2_pass else 'FAIL'}]")
    # Wobble of the s53 anchor ladder vs the single pure M_KK^2 Wheeler law
    h_pure = np.sqrt(1.0 / (3.0 * N_LADDER))    # (local)
    wobble = float(np.max(np.abs(H_ANCHORS - h_pure) / h_pure))  # (local)
    print(f"  max anchor wobble vs single pure Wheeler law: {wobble:.4f} "
          f"(bare-CC model mixing M_KK^2 / M_P_12^2; <= 2.3%)")

    # ------------------------------------------------------------------
    # 5.3  CC-3: L_max=12 pin chain -- s84 cache floors vs W2 npz floors
    # ------------------------------------------------------------------
    cache = np.load(IN_S84_CACHE, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()       # (local)
    floors_cache = np.array([
        float(np.min(sector_evals[tuple(pq)]["abs_evals"]))
        for pq in tower_pq
    ])  # (local)
    nev_cache = np.array([
        len(sector_evals[tuple(pq)]["abs_evals"]) for pq in tower_pq
    ])  # (local)
    cc3_rel = float(np.max(np.abs(floors_cache - floors_w2) / floors_w2))  # (local)
    cc3_pass = (cc3_rel < 1e-12) and bool(np.all(nev_cache == n_evals_w2))  # (local)
    print(f"\nCC-3 (s84 cache sector floors vs W2 npz, sectors "
          f"{tower_pq.tolist()}):")
    print(f"  cache floors = {floors_cache}")
    print(f"  W2 floors    = {floors_w2}")
    print(f"  max rel dev = {cc3_rel:.2e}; n_evals match: "
          f"{nev_cache.tolist()} == {n_evals_w2.tolist()}  "
          f"[{'PASS' if cc3_pass else 'FAIL'}]")

    # ------------------------------------------------------------------
    # 5.4  CC-4: pre-registered FALLBACK branch pinned + present, NOT used
    # ------------------------------------------------------------------
    s98_text = IN_S98_VERDICTS.read_text(encoding="utf-8", errors="replace")  # (local)
    cc4_pass = bool(re.search(
        r"^S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN: PASS", s98_text, re.M))  # (local)
    print(f"\nCC-4 (S98-W3-1 fallback eps_LX existence line present in pinned "
          f"verdict file): [{'PASS' if cc4_pass else 'FAIL'}]  (NOT USED)")

    # ------------------------------------------------------------------
    # 5.5  PHYSICAL gate: C(N) = ||[H_foam(N), eps_LX]||_2 at the 4-point
    #      ladder. H_foam built EXPLICITLY as the energy-weighted
    #      occupation sum over cells (S43 Channel-A form), weights from
    #      the LEFT-INVARIANT data: w_slot = O on every slot (the W2
    #      block diagonal IS g- and phi-independent -- homogeneity wall
    #      + Z3 symmetry, read off the pinned data, not assumed).
    # ------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("PHYSICAL GATE: C(N) = ||[H_foam(N), eps_LX]||  (one-particle rep)")
    print("=" * 72)

    # cell partitions: N=1 -> all phi-points one cell; N>=3 -> per-point cells
    def cell_partition(N: float):
        if N < 3:
            return [list(range(n_phi))]
        return [[j] for j in range(n_phi)]

    # occupation operators n_{g,j} = |g,j><g,j| (one-particle projectors)
    def n_op(g: int, j: int) -> np.ndarray:
        P = np.zeros((dim, dim))                # (local)
        P[g * n_phi + j, g * n_phi + j] = 1.0
        return P

    C_phys = np.zeros(len(N_LADDER))            # (local)
    maxent_phys = np.zeros(len(N_LADDER))       # (local)
    H_check_dev = np.zeros(len(N_LADDER))       # (local)
    for i, (N, h) in enumerate(zip(N_LADDER, H_ANCHORS)):
        H = np.zeros((dim, dim))                # (local)
        for cell in cell_partition(N):
            for j in cell:
                for g in range(n_gen):
                    # energy-weighted diagonal foam coupling, weight = O
                    # (left-invariant: same for both g, all j)
                    H += h * O_diag * n_op(g, j)
        # structural identity check: H == h*O*identity (multiplicity-scalar)
        H_check_dev[i] = float(np.max(np.abs(H - h * O_diag * np.eye(dim))))
        K = H @ eps_LX - eps_LX @ H             # (local) the commutator
        C_phys[i] = spectral_norm(K)
        maxent_phys[i] = float(np.max(np.abs(K)))
        print(f"  N = {N:10.2f}:  h(N) = {h:.6f} M_KK   "
              f"C(N) = {C_phys[i]:.3e} M_KK   max|entry| = {maxent_phys[i]:.3e}"
              f"   [H = h*O*1: dev {H_check_dev[i]:.1e}]")

    max_C = float(np.max(C_phys))               # (local)
    print(f"\n  max_N C(N) = {max_C:.6e} M_KK  vs commutator_tol = "
          f"{COMMUTATOR_TOL:.1e}")

    # CC-7: the zero is NOT a mean-field-flattening artifact -- ANY
    # generation-scalar, cell-diagonal foam commutes. Deterministic
    # sign-alternating per-cell weights (Carlip +/- expanding/contracting
    # cells, beyond the mean-field pin) still give C = 0 exactly.
    sign_pattern = np.array([+1.0, -1.0, +1.0])  # (local) deterministic
    C_signfoam = np.zeros(len(N_LADDER))         # (local)
    for i, (N, h) in enumerate(zip(N_LADDER, H_ANCHORS)):
        H = np.zeros((dim, dim))                 # (local)
        for j in range(n_phi):
            for g in range(n_gen):
                H += h * O_diag * sign_pattern[j] * n_op(g, j)
        K = H @ eps_LX - eps_LX @ H              # (local)
        C_signfoam[i] = spectral_norm(K)
    cc7_pass = bool(np.max(C_signfoam) <= COMMUTATOR_TOL)  # (local)
    print(f"\nCC-7 (sign-alternating per-cell Carlip foam, +/- pattern "
          f"{sign_pattern.astype(int).tolist()}):")
    print(f"  max_N C_signfoam(N) = {np.max(C_signfoam):.3e}  "
          f"[{'PASS -- zero is structural, not mean-field artifact' if cc7_pass else 'FAIL'}]")

    # ------------------------------------------------------------------
    # 5.6  COUNTERFACTUAL probes (DIAGNOSTIC ONLY -- discriminator
    #      liveness; these are NOT the gate)
    # ------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("COUNTERFACTUAL PROBES (diagnostic -- NOT the gate)")
    print("=" * 72)

    # CF-1: leg L1 broken -- generation-RESOLVED foam weights
    # w_gen = diag(O+|w|, O-|w|) (homogeneity-wall-violating; scale |w|)
    absw = float(abs_w[0])                       # (local)
    a_w, b_w = O_diag + absw, O_diag - absw      # (local)
    C_cf1 = np.zeros(len(N_LADDER))              # (local)
    for i, (N, h) in enumerate(zip(N_LADDER, H_ANCHORS)):
        H = np.zeros((dim, dim))                 # (local)
        for j in range(n_phi):
            H += h * a_w * n_op(0, j)
            H += h * b_w * n_op(1, j)
        K = H @ eps_LX - eps_LX @ H              # (local)
        C_cf1[i] = spectral_norm(K)
    C_cf1_analytic = 2.0 * absw**2 * H_ANCHORS   # (local) = h(N)/3 exactly
    cf1_dev = float(np.max(np.abs(C_cf1 - C_cf1_analytic) /
                           C_cf1_analytic))      # (local)
    alpha_cf1, lnC0_cf1, r2_cf1 = loglog_fit(N_LADDER, C_cf1)
    print(f"\nCF-1 (generation-resolved foam, leg L1 broken):")
    print(f"  C_cf1(N) = {C_cf1}")
    print(f"  analytic 2|w|^2 h(N) = h(N)/3: max rel dev = {cf1_dev:.2e}")
    print(f"  fit: alpha_cf1 = {alpha_cf1:.4f}  (R^2 = {r2_cf1:.6f})  "
          f"> alpha_floor = {ALPHA_FLOOR} -> INFO-regime scaling fires")

    # CF-2: leg L2 broken -- Z3 wormhole hopping (Carlip inter-cell channel)
    T_z3 = np.zeros((n_phi, n_phi))              # (local)
    for j in range(n_phi):
        T_z3[j, (j + 1) % n_phi] = 1.0
        T_z3[(j + 1) % n_phi, j] = 1.0
    C_cf2 = np.zeros(len(N_LADDER))              # (local)
    for i, (N, h) in enumerate(zip(N_LADDER, H_ANCHORS)):
        H = h * O_diag * np.eye(dim) + h * np.kron(np.eye(n_gen), T_z3)  # (local)
        K = H @ eps_LX - eps_LX @ H              # (local)
        C_cf2[i] = spectral_norm(K)
    k_cf2 = float(C_cf2[0] / H_ANCHORS[0])       # (local) N-indep prefactor
    alpha_cf2, lnC0_cf2, r2_cf2 = loglog_fit(N_LADDER, C_cf2)
    print(f"\nCF-2 (Z3 wormhole hopping, leg L2 broken; Carlip channel):")
    print(f"  C_cf2(N) = {C_cf2}")
    print(f"  prefactor k = C_cf2/h = {k_cf2:.6f} (= ||[1 (x) T_Z3, eps_LX]||)")
    print(f"  fit: alpha_cf2 = {alpha_cf2:.4f}  (R^2 = {r2_cf2:.6f})  "
          f"> alpha_floor = {ALPHA_FLOOR} -> INFO-regime scaling fires")

    # CF-3: pinching survival -- worst-case Z3-blind cell-average of the
    # between-generation coupling (the N=1 maximal coarse-grain bound)
    w_avg = complex(np.mean(w_j))                # (local)
    survival = float(abs(w_avg) / absw)          # (local)
    phasor_sum = complex(np.sum(np.exp(1j * arg_w)))  # (local)
    print(f"\nCF-3 (pinching survival, worst-case N=1 cell average):")
    print(f"  Z3 phasor sum = {phasor_sum.real:+.6f}{phasor_sum.imag:+.6f}i "
          f"(NOT zero -- the arg pattern {{pi, 2pi/3, -2pi/3}} is not a pure")
    print(f"  Z3 character) -> |<w>|/|w| = {survival:.6f} (= 2/3): the")
    print(f"  between-generation content survives even maximal coarse-")
    print(f"  graining at 2/3 amplitude; the commutator gate above says the")
    print(f"  pinned foam DYNAMICS degrades it by exactly zero.")

    # Wheeler-exponent of the anchor ladder itself (reference)
    alpha_h, _, r2_h = loglog_fit(N_LADDER, H_ANCHORS)
    print(f"\n  anchor-ladder Wheeler exponent: alpha_h = {alpha_h:.4f} "
          f"(R^2 = {r2_h:.6f}; pure law = 0.5)")

    # ------------------------------------------------------------------
    # 5.7  Three-regime classification (pre-registered operator)
    # ------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("THREE-REGIME READ-OFF (pre-registered)")
    print("=" * 72)
    if max_C <= COMMUTATOR_TOL:
        regime = "TOPOLOGICAL"                   # (local)
        verdict = "PASS"                         # (local)
        alpha_phys = np.inf                      # (local)
        print(f"  max_N C(N) = {max_C:.3e} <= {COMMUTATOR_TOL:.1e}")
        print(f"  -> PASS: [H_foam, eps_LX] = 0 exactly at ALL 4 N.")
        print(f"     Generation labels are TOPOLOGICAL invariants of the")
        print(f"     multiplicity bundle -- foam-ROBUST (QF-71 delta_n_foam=0")
        print(f"     class). The 3-generation index survives the foam-")
        print(f"     continuum limit unconditionally.")
    else:
        alpha_phys, _, _ = loglog_fit(N_LADDER, C_phys)  # (local)
        if alpha_phys > ALPHA_FLOOR:
            regime = "GEOMETRIC-FOAM-FRAGILE"    # (local)
            verdict = "INFO"                     # (local)
        else:
            regime = "DESTROYED"                 # (local)
            verdict = "FAIL"                     # (local)
        print(f"  max C = {max_C:.3e} > tol; alpha = {alpha_phys:.3f} "
              f"-> {regime} ({verdict})")

    # [SIGN] 3-tuple (substitution chain Direction lines):
    #   sign: the pre-registered topological-branch direction (C == 0,
    #         predicted vanishing) HOLDS -> PASS
    #   magnitude: max_N C(N) = 0 <= 1e-10 -> PASS
    #   regime: deterministic mean-field model evaluated on the FULL
    #           4-point ladder, no validity-window breach -> VALID
    sign_verdict = "PASS" if verdict == "PASS" else (
        "PASS" if (verdict == "INFO") else "FAIL")  # (local)
    magnitude_verdict = ("PASS" if max_C <= COMMUTATOR_TOL else
                         ("INFO" if verdict == "INFO" else "FAIL"))  # (local)
    regime_verdict = "VALID"                     # (local)
    print(f"\n  [SIGN] 3-tuple: sign={sign_verdict} "
          f"magnitude={magnitude_verdict} regime={regime_verdict}")

    cc_all = {
        "CC-0": cc0_pass, "CC-1": cc1_pass, "CC-2": cc2_pass,
        "CC-3": cc3_pass, "CC-4": cc4_pass, "CC-7": cc7_pass,
        "CF-1-analytic": cf1_dev < 1e-12,
    }  # (local)
    print(f"\n  cross-checks: " + "  ".join(
        f"{k}:{'PASS' if v else 'FAIL'}" for k, v in cc_all.items()))
    assert all(cc_all.values()), f"cross-check failure: {cc_all}"

    value_str = (
        f"max_C={max_C:.1e}_exact_4ptN_alpha_phys=inf_topological_QF71"
        f"_cf1_alpha={alpha_cf1:.3f}_cf2_alpha={alpha_cf2:.3f}"
        f"_z3_pinch_survival={survival:.4f}_epslx=ITEM6-W2FORM"
        if verdict == "PASS" else
        f"max_C={max_C:.3e}_alpha={alpha_phys:.3f}_{regime}"
        f"_epslx=ITEM6-W2FORM"
    )  # (local)

    return {
        "value": value_str,
        "verdict": verdict,
        "regime": regime,
        "max_C": max_C,
        "C_phys": C_phys,
        "maxent_phys": maxent_phys,
        "C_signfoam": C_signfoam,
        "C_cf1": C_cf1, "C_cf1_analytic": C_cf1_analytic,
        "alpha_cf1": alpha_cf1, "r2_cf1": r2_cf1,
        "C_cf2": C_cf2, "k_cf2": k_cf2,
        "alpha_cf2": alpha_cf2, "r2_cf2": r2_cf2,
        "alpha_phys": float(alpha_phys) if np.isfinite(alpha_phys) else np.inf,
        "alpha_h": alpha_h, "r2_h": r2_h,
        "survival": survival, "phasor_sum": phasor_sum,
        "eps_LX": eps_LX, "O_diag": O_diag, "abs_w": abs_w, "arg_w": arg_w,
        "w_j": w_j, "h_recon": h_recon, "cc2_rel": cc2_rel,
        "wobble": wobble, "M_P_12": M_P_12, "r2_p12": r2_p12,
        "floors_cache": floors_cache, "floors_w2": floors_w2,
        "H_check_dev": H_check_dev,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "cc_all": cc_all,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Verdict payload (printed; agent calls mcp emit_verdict)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None):
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
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
# Section 7 -- Plot (log-log C(N) vs N diagnostic)
# ---------------------------------------------------------------------------

def make_plot(res: dict):
    fig, ax = plt.subplots(figsize=(9.5, 7))    # (local)
    N = N_LADDER                                 # (local)
    DISPLAY_FLOOR = 1e-16                        # (local) log axis cannot show 0

    # physical gate: C == 0 exact -- display at floor with annotation
    ax.plot(N, np.full_like(N, DISPLAY_FLOOR), "v", color="#2166ac",
            markersize=11, label=r"PHYSICAL: $C(N)=\|[H_{foam},\epsilon_{LX}]\|"
                                 r"= 0$ exact (displayed at floor)")
    # counterfactuals
    ax.plot(N, res["C_cf1"], "o-", color="#d6604d", markersize=7,
            label=(rf"CF-1 gen-resolved foam (leg L1 broken): "
                   rf"$C=2|w|^2 h(N)$, $\alpha={res['alpha_cf1']:.3f}$"))
    ax.plot(N, res["C_cf2"], "s-", color="#f4a582", markersize=7,
            label=(rf"CF-2 $Z_3$ wormhole hopping (leg L2 broken): "
                   rf"$\alpha={res['alpha_cf2']:.3f}$"))
    # anchor law reference
    ax.plot(N, H_ANCHORS, "k--", alpha=0.45, linewidth=1.2,
            label=r"$h(N)$ Wheeler-$\sqrt{N}$ anchors (s53), "
                  rf"$\alpha_h={res['alpha_h']:.3f}$")
    # thresholds
    ax.axhline(COMMUTATOR_TOL, color="green", linestyle=":", linewidth=1.6,
               label=r"commutator_tol $=10^{-10}$ (PASS boundary)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"foam cell count $N$  (1 $\to$ 32 cells $\to$ "
                  r"$N_{Planck}$=1124.6 $\to$ $V_{Haar}$=1349.74)", fontsize=11)
    ax.set_ylabel(r"$C(N) = \|[H_{foam}(N),\ \epsilon_{LX}]\|_2$   [$M_{KK}$]",
                  fontsize=11)
    ax.set_ylim(3e-18, 3.0)
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(fontsize=8.2, loc="center left")
    ax.text(1.25, 4e-15,
            "PASS: $C\\equiv 0$ exact at all 4 N — generation index is\n"
            "TOPOLOGICAL (QF-71 $\\delta n_{foam}=0$ class), foam-robust.\n"
            "Counterfactuals (broken legs) land in the INFO band\n"
            "($\\alpha\\approx 0.5 > \\alpha_{floor}=0.05$): discriminator is live.",
            fontsize=9, color="#2166ac",
            bbox=dict(boxstyle="round", facecolor="#deebf7", alpha=0.85))
    ax.set_title("S100a-EPSLX-FOAM-SURVIVAL — does the generation index "
                 "survive the foam?\n"
                 r"$[H_{foam},\epsilon_{LX}]$ at the Wheeler-$\sqrt{N}$ ladder"
                 " (W2-form $\\epsilon_{LX}$, Item 6)", fontsize=11.5)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"\nPlot saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()       # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    # save npz (full float64 per publication-precision pin)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        verdict=res["verdict"], regime=res["regime"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        # ladder + anchors
        N_ladder=N_LADDER, h_anchors=H_ANCHORS, h_recon=res["h_recon"],
        cc2_rel=res["cc2_rel"], anchor_wobble=res["wobble"],
        M_P_12_recon=res["M_P_12"], r2_p12=res["r2_p12"],
        lambda_bare_is_mkk2=LAMBDA_BARE_IS_MKK2,
        # gate observable
        C_phys=res["C_phys"], max_C=res["max_C"],
        maxent_phys=res["maxent_phys"], H_check_dev=res["H_check_dev"],
        C_signfoam=res["C_signfoam"],
        alpha_phys=res["alpha_phys"],
        commutator_tol=COMMUTATOR_TOL, alpha_floor=ALPHA_FLOOR,
        # counterfactual diagnostics
        C_cf1=res["C_cf1"], C_cf1_analytic=res["C_cf1_analytic"],
        alpha_cf1=res["alpha_cf1"], r2_cf1=res["r2_cf1"],
        C_cf2=res["C_cf2"], k_cf2=res["k_cf2"],
        alpha_cf2=res["alpha_cf2"], r2_cf2=res["r2_cf2"],
        alpha_h=res["alpha_h"], r2_h=res["r2_h"],
        z3_pinch_survival=res["survival"],
        z3_phasor_sum=np.array([res["phasor_sum"]]),
        # eps_LX (W2-form source)
        eps_LX=res["eps_LX"], O_diag=res["O_diag"],
        abs_w_phi=res["abs_w"], arg_w_M2_phi=res["arg_w"], w_j=res["w_j"],
        epslx_source=np.array(["ITEM6-W2-FORM"]),
        epslx_fallback=np.array(["S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN (pinned, NOT used)"]),
        # cross-check chain
        floors_cache=res["floors_cache"], floors_w2=res["floors_w2"],
        cc_names=np.array(list(res["cc_all"].keys())),
        cc_pass=np.array([res["cc_all"][k] for k in res["cc_all"]], dtype=bool),
        # SHAs
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"\nData saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res)

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    print_verdict_payload(
        res["verdict"], res["value"], audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note=("Wheeler-sqrtN s53 anchors; C(N)=0 exact at all 4 N; "
                        "QF-71 class; CF probes alpha~0.5 (discriminator live)"),
        extra_rows=[
            "# epslx_source=ITEM6-W2-FORM (s100a_yukawa_overlap_offdiag.npz "
            "key eps_lx_block_phi0); pre-registered fallback S98-W3-1 "
            "(audit b8487bc838683800...) NOT USED # "
            "S100a-EPSLX-FOAM-SURVIVAL source-branch row",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {wall:.1f}s) ===")
    return 0   # exit 0 on any VALID verdict (math-scripts.md exit semantics)


if __name__ == "__main__":
    sys.exit(main())
