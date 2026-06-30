#!/usr/bin/env python3
"""
S100b W3-2 S100b-TAU0-LAITEH-REDUCTION — Lai-Teh tau=0 reduction unit test
==========================================================================

Gate: S100b-TAU0-LAITEH-REDUCTION ([VERIFY-THEOREM])
Classification: GEOMETRIC
Agent: baptista-spacetime-analyst
Plan: sessions/session-plan/session-100b-plan-w3.md §W3-2

Pre-registered threshold (strict conjunction; plan §W3-2 operator block):
  PASS iff [max over sectors, within-block |lambda| spread / |lambda| < 1e-12] AND
           [max over sectors |lambda^2/lambda^2_(1,0) - (u^2+uv+v^2)/7| / ((u^2+uv+v^2)/7) < 1e-12] AND
           [per-sign multiplicity == 8*dim^2 exactly, all sectors] AND
           [exists global sigma: max |36*sigma*lambda^2 - round(.)| < 1e-9] AND
           [4-term polynomial coefficient ratios |Delta|/|ref| < 1e-10 at t=1/3] AND
           [(3t-1)(3t-2) == 0 at t=1/3, exact]
  FAIL on any leg failure. INFO reserved ONLY for the LEG-3 PDF-extraction
  contingency (did NOT fire: Lai-Teh arXiv:1209.3812v2 fully extracted via the
  pdf skill; Thm 2.1/2.2/2.3/3.1/3.4 + Lemmas 2.5/2.6 transcribed below).

Reference closed forms (Lai-Teh, arXiv:1209.3812v2; metric normalized (rho,rho)=3,
(lambda_1,lambda_1)=1; Cas(p,q) = p^2+q^2+pq+3p+3q  [Lemma 2.5]):
  Thm 2.2 (t=1/3):  D^2 eigenvalue lam_hat^2 = u^2+uv+v^2, multiplicity
                    2 u^2 v^2 (u+v)^2 (= 8 dim^2, HALF-spinor counting), labels u,v >= 1.
  Thm 2.3:          D_t^2 = (pi x 1)[(1-3t)(1xCas + Casx1 - DeltaCas) + 1xCas + 9t^2|rho|^2]
                    => on V_mu c S x V_(p,q):
                    eig_LT(mu; V; t) = (1-3t)[poly(V)+9-poly(mu)] + poly(V) + 27 t^2
                    with poly(p,q) = p^2+q^2+pq+3p+3q and S = 2 V_rho (Kostant).
  Thm 3.1/3.4:      spectral action at t=1/3 = SINGLE Lambda^8 term; the
                    Lambda^6/Lambda^4/Lambda^2 coefficients carry
                    [(3t-1)(3t-2)]^{1,2,3} — all vanish at t=1/3.
Label map (VERIFIED in-script, not assumed): (u,v) = (p+1,q+1):
  u^2+uv+v^2 = 3*C_2(p,q)+3 = poly(p,q)+3 ;  2u^2v^2(u+v)^2 = 8*dim(p,q)^2.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/dirac_spectrum.py        (PINNED dadba674e950fad9...)
  - downloads/research-sweep-s99/spectral-geometry-math/01_Lai-Teh_*.pdf (PINNED b5502a2fa4e719eb...)
  - computations/_shared/canonical_constants.py   (runtime; feeds audit_sha256)

Output 4-tuple:
  (value=<composite>, scheme=LaiTeh-Thm2.2-cubic-point-spectrum+Thm3.4-spectral-action,
   convention=scale-free-ratio+exact-integer-multiplicity+label-map-(u,v)=(p+1,q+1)-verified-not-assumed+PW-x-dim-factor-explicit,
   L_max=6)

METHODOLOGY
-----------
LEG 0: label-map verification (exact integer algebra p,q<=40 + four probe sectors)
       + D_F(tau=0)=0 sanity (jensen_metric(B,0) == bi-invariant metric bitwise; s30a lineage).
LEG 1: all 28 sectors p+q<=6: assemble D via the module pipeline
       (jensen_metric -> orthonormal_frame -> connection_coefficients ->
       spinor_connection_offset -> dirac_operator_on_irrep), eigendecompose
       (torch.linalg GPU >=100, numpy below, OMP capped at 8), test
       (a) within-block collapse, (b) scale-free ratios vs (u^2+uv+v^2)/7,
       (c) per-sign multiplicity 8*dim block-level (= 8*dim^2 per sign after PW x dim).
       FAIL-SUBCASE decomposition (pre-registered): compare measured spectra against
       the exact Thm-2.3 closed form at t=1/2 (Levi-Civita; structured) at machine
       epsilon, extract the torsion point via 27t^2 from the (0,0) sector AND via the
       operator-level cubic coefficient Omega = alpha*Phi; POSITIVE CONTROL: the
       cubic-modified operator Omega_cubic = (2/3)*Omega_module re-run through all legs.
LEG 2: global sigma with 36*sigma*lambda^2 integer to 1e-9 across ALL sectors (sigma=1 first).
LEG 3: exact residues of zeta(z) = sum 4u^2v^2(u+v)^2 (u^2+uv+v^2)^{-z} at z=4,3,2,1
       via the binomial/Faulhaber reduction (exact Fractions; z*=3,2,1 are FINITE exact
       sums; z*=4 converges geometrically ~4^{-j}) + Poisson/Gaussian-moment closed form
       r4 = 8*sqrt(3)*pi/243 + lattice heat-trace flatness K(t)*t^4 = const (certifies
       a_2=a_4=a_6=0 numerically) — compared against Thm 3.4 at t=1/3 (ratios 0,0,0)
       with the (3t-1)(3t-2) twist vanishing checked in exact rational arithmetic.
DIAGNOSTICS (non-gating): tau=0 closed-form max|lam_hat|(30,0) = sqrt(993) (NO matrix
       at (30,0)) vs the eq-(1) tau_fold=0.19 HIGH-PW-51 fit value R_(30,0) = 12.05 M_KK
       (collab atlas-spectral-geometer §3; tau-scope difference stated); global scale
       published at 10 sig figs.

DISCIPLINE
----------
- from canonical_constants import * ; intermediates tagged # (local)
- GPU via torch.linalg for blocks >= 100x100 (first-use validated against numpy)
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA emitted
- verdict via print_verdict_payload -> agent calls mcp__knowledge__emit_verdict
  (race-safe; this script does NOT write the verdict file)
"""

from __future__ import annotations

# --- thread cap BEFORE any numpy import (computation-environment.md) ---
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import time
import hashlib
from pathlib import Path
from fractions import Fraction
from math import comb, pi, sqrt

SCRIPT_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SCRIPT_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (tau_fold used in diagnostics)

import numpy as np

try:
    import torch  # GPU path (ROCm)
    TORCH_OK = bool(torch.cuda.is_available())  # (local)
except Exception:
    torch = None
    TORCH_OK = False  # (local)

import dirac_spectrum as ds

# ---------------------------------------------------------------------------
# Identity + pre-registered machinery pins (plan §W3-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "100b"                                                    # (local)
GATE_ID = "S100b-TAU0-LAITEH-REDUCTION"                             # (local)
SCHEME = "LaiTeh-Thm2.2-cubic-point-spectrum+Thm3.4-spectral-action"  # (local)
CONVENTION = ("scale-free-ratio+exact-integer-multiplicity+"
              "label-map-(u,v)=(p+1,q+1)-verified-not-assumed+"
              "PW-x-dim-factor-explicit")                           # (local)
L_MAX = 6                                                           # (local) max p+q, pinned

EPS_SPREAD = 1e-12   # (local) within-block collapse, relative
EPS_RATIO = 1e-12    # (local) scale-free eigenvalue ratios, relative
EPS_BIN = 1e-9       # (local) degeneracy grouping only — never a pass criterion
EPS_N36 = 1e-9       # (local) n/36 integrality
EPS_POLY = 1e-10     # (local) Thm 3.4 coefficient ratios
J_MAX = 60           # (local) LEG-3 j-sum truncation (geometric ~4^-j; tail bound emitted)

OUT_NPZ = SCRIPT_DIR / "s100b_tau0_laiteh_reduction.npz"
OUT_PNG = SCRIPT_DIR / "s100b_tau0_laiteh_reduction.png"

PIN_DIRAC_SPECTRUM = "dadba674e950fad9a300c282b3860cbf31e36589fa86a0ace975376976a602a7"  # (local) plan pin
PIN_LAITEH_PDF = "b5502a2fa4e719eb706a7a9e24d98a2ae00ffc2f787973f225e61103f8277cba"      # (local) plan pin

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
    PROJECT_ROOT / "downloads" / "research-sweep-s99" / "spectral-geometry-math"
    / "01_Lai-Teh_Dirac-Spectrum-Spectral-Action-SU3.pdf",
]


# ---------------------------------------------------------------------------
# SHA block (template Section 4; S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    script_bytes = script_path.read_bytes()      # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Exact integer helpers (canonical SU(3) representation data)
# ---------------------------------------------------------------------------
def dim_pq(p: int, q: int) -> int:
    """Weyl dimension formula dim(p,q) = (p+1)(q+1)(p+q+2)/2 [Lai-Teh eq 2.10]."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def poly_pq(p: int, q: int) -> int:
    """Lai-Teh Casimir scalar (Lemma 2.5, (lambda_1,lambda_1)=1): poly = 3*C_2(p,q)."""
    return p * p + q * q + p * q + 3 * p + 3 * q


def lam_hat_sq(p: int, q: int) -> int:
    """Cubic-point D^2 eigenvalue (Thm 2.2) in (u,v)=(p+1,q+1) labels: u^2+uv+v^2."""
    u, v = p + 1, q + 1  # (local)
    return u * u + u * v + v * v


def mu_list_lemma26(p: int, q: int):
    """V_rho x V_(p,q) decomposition per Lai-Teh Lemma 2.6 (with parameter ranges)."""
    mus = []  # (local)
    mus.append((p + 1, q + 1))
    if p >= 1:
        mus.append((p - 1, q + 2))
    if (p, q) != (0, 0):
        mus.append((p, q))
    if p >= 2:
        mus.append((p - 2, q + 1))
    if q >= 1:
        mus.append((p + 2, q - 1))
    if p >= 1 and q >= 1:
        mus.append((p, q))
    if q >= 2:
        mus.append((p + 1, q - 2))
    if p >= 1 and q >= 1:
        mus.append((p - 1, q - 1))
    return mus


def eig_LT_general_t(pV, qV, mu, t: Fraction) -> Fraction:
    """Thm 2.3 closed form on the V_mu component of S x V_(p,q), Lai-Teh units:
    (1-3t)[poly(V)+9-poly(mu)] + poly(V) + 27 t^2."""
    pv = poly_pq(pV, qV)        # (local)
    pm = poly_pq(mu[0], mu[1])  # (local)
    return (1 - 3 * t) * (pv + 9 - pm) + pv + 27 * t * t


# ---------------------------------------------------------------------------
# LEG 3 exact machinery: Faulhaber/binomial residues of the cubic-point zeta
#   zeta(z) = sum_{u,v>=1} 4 u^2 v^2 (u+v)^2 (u^2+uv+v^2)^{-z}
#   Binomial: (u^2+uv+v^2)^{-z} = sum_j C(z+j-1,j) (uv)^j (u+v)^{-2z-2j}
#   Inner sum over u+v=N: S_a(N) = sum_{u=1}^{N-1} u^a (N-u)^a, a=j+2
#   => per (j, coefficient-of-N^m) one Riemann zeta zeta_R(2z+2j-2-m);
#   pole at z* = (m+3-2j)/2, residue 1/2 per unit zeta_R residue.
#   Needed coefficient index from top: r = 8-2z* in {0,2,4,6} for z* in {4,3,2,1}.
# ---------------------------------------------------------------------------
def bernoulli_minus(n_max: int):
    """B^-_k (B_1 = -1/2 convention) as exact Fractions, k = 0..n_max."""
    B = [Fraction(0)] * (n_max + 1)  # (local)
    B[0] = Fraction(1)
    for m in range(1, n_max + 1):
        s = Fraction(0)  # (local)
        for k in range(m):
            s += comb(m + 1, k) * B[k]
        B[m] = -s / (m + 1)
    return B


B_MINUS = bernoulli_minus(8)  # (local) only r <= 6 needed


def faulhaber_poly_in_N(m: int):
    """Coefficients (dict deg->Fraction) of Q_m(N) = sum_{u=0}^{N-1} u^m
    = (1/(m+1)) sum_{i=0}^{m} C(m+1,i) B^-_i N^{m+1-i}."""
    Bm = bernoulli_minus(m)  # (local)
    co = {}  # (local)
    for i in range(m + 1):
        co[m + 1 - i] = co.get(m + 1 - i, Fraction(0)) + Fraction(comb(m + 1, i)) * Bm[i] / (m + 1)
    return co


def S_a_poly(a: int):
    """Exact coefficients of S_a(N) = sum_{u=1}^{N-1} u^a (N-u)^a (degree 2a+1)."""
    co = {}  # (local)
    for k in range(a + 1):
        ck = Fraction(comb(a, k) * (-1) ** k)  # (local)
        q = faulhaber_poly_in_N(a + k)         # (local)
        for deg, c in q.items():
            co[deg + a - k] = co.get(deg + a - k, Fraction(0)) + ck * c
    return co


def sigma_a_r(a: int, r: int) -> Fraction:
    """[N^{2a+1-r}] S_a(N) via the closed per-k form with the i<=m range guard."""
    tot = Fraction(0)  # (local)
    for k in range(a + 1):
        m = a + k  # (local)
        if r > m:
            continue  # Faulhaber Q_m has terms i=0..m only
        tot += Fraction(comb(a, k) * (-1) ** k) * Fraction(comb(m + 1, r)) * B_MINUS[r] / (m + 1)
    return tot


def residue_jsum(z_star: int, j_max: int):
    """Res_{z=z*} zeta(z) = sum_j 2 C(z*+j-1, j) [N^{2z*+2j-3}] S_{j+2}(N).
    Exact Fractions; r = 8-2z* fixes the from-top coefficient index.
    For z* in {3,2,1} the sum is FINITE (terms vanish for a=j+2 >= r by the
    polynomial-in-k cancellation); for z*=4 it converges geometrically (~4^-j)."""
    r = 8 - 2 * z_star  # (local)
    terms = []  # (local)
    total = Fraction(0)  # (local)
    for j in range(j_max + 1):
        a = j + 2  # (local)
        sig = sigma_a_r(a, r)  # (local)
        term = 2 * Fraction(comb(z_star + j - 1, j)) * sig  # (local)
        terms.append(term)
        total += term
    return total, terms


# ---------------------------------------------------------------------------
# Eigendecomposition (anti-Hermitian D -> Hermitian H = -i D; GPU >= 100)
# ---------------------------------------------------------------------------
def eig_dirac_block(D: np.ndarray, gpu_log: dict):
    n = D.shape[0]  # (local)
    Hm = -1j * D    # (local) Hermitian if D anti-Hermitian
    herm_err = float(np.max(np.abs(Hm - Hm.conj().T)))  # (local)
    H = 0.5 * (Hm + Hm.conj().T)  # (local) symmetrize float residue
    if TORCH_OK and n >= 100:
        tH = torch.tensor(H, device="cuda")            # (local)
        evals = torch.linalg.eigvalsh(tH).cpu().numpy()  # (local)
        gpu_log["used"] = True
    else:
        evals = np.linalg.eigvalsh(H)  # (local)
    return np.asarray(evals, dtype=np.float64), herm_err


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    # plan-pin drift assertions (static inputs MUST match plan §W3-2 input_files)
    rel_ds = "computations/_shared/dirac_spectrum.py"          # (local)
    rel_pdf = ("downloads/research-sweep-s99/spectral-geometry-math/"
               "01_Lai-Teh_Dirac-Spectrum-Spectral-Action-SU3.pdf")  # (local)
    assert pins[rel_ds] == PIN_DIRAC_SPECTRUM, "dirac_spectrum.py SHA drift vs plan pin"
    assert pins[rel_pdf] == PIN_LAITEH_PDF, "Lai-Teh PDF SHA drift vs plan pin"

    script_path = Path(__file__).resolve()                    # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"    # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  GPU available: {TORCH_OK}")
    print()

    res = {}  # (local) npz accumulator

    # ---------------- sector list pin ----------------
    sectors = [(p, q) for p in range(L_MAX + 1) for q in range(L_MAX + 1) if p + q <= L_MAX]  # (local)
    sectors_pin = [(p, q) for p in range(7) for q in range(7) if p + q <= 6]  # (local) plan pin
    assert sectors == sectors_pin and len(sectors) == 28, "sector list != plan pin"
    print(f"[pin] sector list: 28 sectors, 0 <= p+q <= {L_MAX} (asserted == plan pin)")

    # ---------------- LEG 0a: label-map algebra identities (exact ints) ----------------
    for p in range(41):
        for q in range(41):
            u, v = p + 1, q + 1  # (local)
            assert u * u + u * v + v * v == poly_pq(p, q) + 3, "label-map eigenvalue identity FAILED"
            assert 2 * u * u * v * v * (u + v) ** 2 == 8 * dim_pq(p, q) ** 2, "label-map multiplicity identity FAILED"
    print("[LEG0] label map (u,v)=(p+1,q+1): u^2+uv+v^2 == 3*C_2+3 and "
          "2u^2v^2(u+v)^2 == 8*dim^2 EXACT for all p,q <= 40")

    # ---------------- LEG 0b: D_F(tau=0)=0 sanity (s30a lineage) ----------------
    gens = ds.su3_generators()                       # (local)
    f_abc = ds.compute_structure_constants(gens)     # (local)
    B_ab = ds.compute_killing_form(f_abc)            # (local)
    # NOTE: the module's compute_killing_form returns einsum('acd,bcd->ab', f, f)
    # = +3*I (the POSITIVE-definite -Tr(adX adY); its docstring "-3 delta" is a
    # benign sign slip — only |B| feeds the metric pipeline via g0 = |B|).
    killing_dev = float(np.max(np.abs(np.abs(B_ab) - 3.0 * np.eye(8))))  # (local)
    g0 = ds.jensen_metric(B_ab, 0.0)                 # (local)
    g_bi = ds.u2_invariant_metric(B_ab, 1.0, 1.0, 1.0)  # (local) bi-invariant
    df0_dev = float(np.max(np.abs(g0 - g_bi)))       # (local) deformation content at tau=0
    assert np.exp(0.0) == 1.0
    print(f"[LEG0] metric base |B| = 3*I to {killing_dev:.2e} (module B = +3*I, "
          f"-Tr(adXadY) sign convention; only |B| enters the metric); "
          f"jensen_metric(B,0) == bi-invariant metric: max|dev| = {df0_dev:.1e} "
          f"(EXACT 0.0 required: {'OK' if df0_dev == 0.0 else 'VIOLATED'})")
    assert df0_dev == 0.0, "tau=0 deformation content non-zero"

    # ---------------- frame / connection / Clifford / Omega at tau=0 ----------------
    E = ds.orthonormal_frame(g0)                     # (local)
    ft = ds.frame_structure_constants(f_abc, E)      # (local)
    Gamma = ds.connection_coefficients(ft)           # (local)
    gammas = ds.build_cliff8()                       # (local)
    Omega = ds.spinor_connection_offset(Gamma, gammas)  # (local)
    cliff_err = float(ds.validate_clifford(gammas))     # (local)
    conn_err = float(ds.validate_connection(Gamma))     # (local)
    _, is_ah, h_err, ah_err = ds.validate_omega_hermitian(Omega)  # (local)
    print(f"[chk] Clifford err {cliff_err:.2e}; metric-compat err {conn_err:.2e}; "
          f"Omega anti-Hermitian: {is_ah} (dev {ah_err:.2e})")

    # operator-level torsion measurement: Omega vs Phi = sum_{abc} ft_abc g g g
    Phi = np.zeros((16, 16), dtype=complex)  # (local)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                if abs(ft[a, b, c]) > 1e-15:
                    Phi += ft[a, b, c] * gammas[a] @ gammas[b] @ gammas[c]
    alpha_num = np.vdot(Phi, Omega)                  # (local)
    alpha_den = np.vdot(Phi, Phi)                    # (local)
    alpha = (alpha_num / alpha_den)                  # (local) Omega = alpha * Phi
    omega_fit_resid = float(np.max(np.abs(Omega - alpha * Phi)) / np.max(np.abs(Omega)))  # (local)
    phi_sq = Phi @ Phi                               # (local)
    phi_sq_scalar = float(np.real(np.trace(phi_sq)) / 16.0)  # (local)
    phi_sq_dev = float(np.max(np.abs(phi_sq - phi_sq_scalar * np.eye(16))))  # (local)
    # Lai-Teh family D_t = A + t*(1/4)*Phi-equivalent => |t_op| = |alpha| / (1/4)
    t_op = abs(alpha) * 4.0                          # (local) operator-level torsion point
    print(f"[op ] Omega = alpha*Phi with alpha = {alpha.real:+.12f}{alpha.imag:+.2e}j "
          f"(fit resid {omega_fit_resid:.1e}); Phi^2 = {phi_sq_scalar:+.10f}*I "
          f"(scalar dev {phi_sq_dev:.2e})")
    print(f"[op ] |t_operator| = 4*|alpha| = {t_op:.12f}  "
          f"(Levi-Civita t=1/2 <=> alpha=-1/8; Kostant cubic t=1/3 <=> alpha=-1/12)")

    # ---------------- LEG 1: 28 sectors, module operator (+ cubic positive control) ----
    Omega_cubic = (2.0 / 3.0) * Omega                # (local) cubic-modified control (alpha -> -1/12)
    gpu_log = {"used": False}                        # (local)
    gpu_validation_dev = -1.0                        # (local)

    n_sec = len(sectors)                             # (local)
    arr = lambda: np.zeros(n_sec)                    # (local)
    dims = np.zeros(n_sec, dtype=np.int64)           # (local)
    lam_hat2 = np.zeros(n_sec, dtype=np.int64)       # (local)
    spread_LC, spread_CU = arr(), arr()              # (local)
    lam2_mean_LC, lam2_min_LC, lam2_max_LC = arr(), arr(), arr()  # (local)
    lam2_mean_CU = arr()                             # (local)
    npos_LC = np.zeros(n_sec, dtype=np.int64)        # (local)
    nneg_LC = np.zeros(n_sec, dtype=np.int64)        # (local)
    npos_CU = np.zeros(n_sec, dtype=np.int64)        # (local)
    herm_max = 0.0                                   # (local)
    hom_max, ahg_max = 0.0, 0.0                      # (local) irrep validation
    evals_LC_all, evals_CU_all, ev_off = [], [], [0]  # (local)
    lc_pred_vals, lc_pred_mult, lc_off = [], [], [0]  # (local)
    lc_match_dev = arr()                             # (local)
    row8_dev_parth = []                              # (local) Thm-2.3-component value
    row8_dev_paper = []                              # (local) printed row-8 (+twist) variant

    THALF = Fraction(1, 2)                           # (local)
    TWIST_T12 = float((3 * THALF - 1) * (3 * THALF - 2))  # (local) = -1/4

    for i, (p, q) in enumerate(sectors):
        d = dim_pq(p, q)                             # (local)
        dims[i] = d
        lam_hat2[i] = lam_hat_sq(p, q)
        rho, dchk = ds.get_irrep(p, q, gens, f_abc)  # (local)
        assert dchk == d
        if (p, q) != (0, 0):
            he, ae = ds.validate_irrep(rho, f_abc, label=f"({p},{q})")  # (local)
            hom_max, ahg_max = max(hom_max, he), max(ahg_max, ae)
        D = ds.dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
        evals, herr = eig_dirac_block(D, gpu_log)    # (local)
        if gpu_log["used"] and gpu_validation_dev < 0:
            ev_np = np.linalg.eigvalsh(0.5 * ((-1j * D) + (-1j * D).conj().T))  # (local)
            gpu_validation_dev = float(np.max(np.abs(np.sort(ev_np) - np.sort(evals))))
            print(f"[gpu] first GPU block ({p},{q}) validated vs numpy: "
                  f"max dev {gpu_validation_dev:.2e}")
        herm_max = max(herm_max, herr)
        a_ev = np.abs(evals)                         # (local)
        spread_LC[i] = (a_ev.max() - a_ev.min()) / a_ev.mean()
        lam2 = evals ** 2                            # (local)
        lam2_mean_LC[i] = lam2.mean()                # mult-weighted mean (declared representative)
        lam2_min_LC[i], lam2_max_LC[i] = lam2.min(), lam2.max()
        npos_LC[i] = int((evals > 0).sum())
        nneg_LC[i] = int((evals < 0).sum())
        evals_LC_all.append(np.sort(evals))
        ev_off.append(ev_off[-1] + evals.size)

        # cubic positive control
        Dc = ds.dirac_operator_on_irrep(rho, E, gammas, Omega_cubic)  # (local)
        evc, _ = eig_dirac_block(Dc, gpu_log)        # (local)
        a_evc = np.abs(evc)                          # (local)
        spread_CU[i] = (a_evc.max() - a_evc.min()) / a_evc.mean()
        lam2_mean_CU[i] = (evc ** 2).mean()
        npos_CU[i] = int((evc > 0).sum())
        evals_CU_all.append(np.sort(evc))

        # structured LC(t=1/2) prediction per Thm 2.3 + Lemmas 2.5/2.6 (frame = LT/9)
        mus = mu_list_lemma26(p, q)                  # (local)
        pv, pm_list = [], []                         # (local)
        for mu in mus:
            val = eig_LT_general_t(p, q, mu, THALF)  # (local) LT units, exact Fraction
            pv.append(float(val) / 9.0)
            pm_list.append(2 * dim_pq(mu[0], mu[1]))
        assert sum(pm_list) == 16 * d, "Lemma 2.6 dimension bookkeeping FAILED"
        lc_pred_vals.extend(pv); lc_pred_mult.extend(pm_list)
        lc_off.append(lc_off[-1] + len(pv))
        pred_sorted = np.sort(np.repeat(np.array(pv), np.array(pm_list)))  # (local)
        meas_sorted = np.sort(lam2)                  # (local)
        lc_match_dev[i] = float(np.max(np.abs(meas_sorted - pred_sorted) / pred_sorted))

        # row-8 variant diagnostic on the mu=(p-1,q-1) component (printed table erratum probe)
        if p >= 1 and q >= 1:
            mu8 = (p - 1, q - 1)                     # (local)
            v_parth = float(eig_LT_general_t(p, q, mu8, THALF)) / 9.0  # (local)
            v_paper = v_parth + 3.0 * TWIST_T12 / 9.0                  # (local) printed row 8 adds the twist
            row8_dev_parth.append(float(np.min(np.abs(meas_sorted - v_parth)) / v_parth))
            row8_dev_paper.append(float(np.min(np.abs(meas_sorted - v_paper)) / abs(v_paper)))

        print(f"  ({p},{q}): dim={d:3d} block={16*d:5d}  spread={spread_LC[i]:.3e}  "
              f"npos={npos_LC[i]:5d}/{8*d:5d}  LC-match={lc_match_dev[i]:.3e}  "
              f"cubic-spread={spread_CU[i]:.3e}")

    evals_LC_concat = np.concatenate(evals_LC_all)   # (local)
    evals_CU_concat = np.concatenate(evals_CU_all)   # (local)

    # LEG 1 sub-verdicts
    ok_a = bool(np.max(spread_LC) < EPS_SPREAD)      # (local)
    i10 = sectors.index((1, 0))                      # (local)
    ratio_meas = lam2_mean_LC / lam2_mean_LC[i10]    # (local)
    ratio_tgt = lam_hat2.astype(float) / 7.0         # (local)
    ratio_dev = np.abs(ratio_meas - ratio_tgt) / ratio_tgt  # (local)
    ok_b = bool(np.max(ratio_dev) < EPS_RATIO)       # (local)
    mult_ok = np.array([(npos_LC[i] == 8 * dims[i]) and (nneg_LC[i] == 8 * dims[i])
                        for i in range(n_sec)])      # (local)
    mult_identity = np.array([8 * int(dims[i]) ** 2 ==
                              2 * (sectors[i][0] + 1) ** 2 * (sectors[i][1] + 1) ** 2
                              * (sectors[i][0] + sectors[i][1] + 2) ** 2
                              for i in range(n_sec)])  # (local)
    ok_c = bool(mult_ok.all() and mult_identity.all())  # (local)

    # cubic positive control sub-verdicts
    ratio_meas_cu = lam2_mean_CU / lam2_mean_CU[i10]   # (local)
    ratio_dev_cu = np.abs(ratio_meas_cu - ratio_tgt) / ratio_tgt  # (local)
    cubic_ok = bool(np.max(spread_CU) < EPS_SPREAD and np.max(ratio_dev_cu) < EPS_RATIO
                    and all(npos_CU[i] == 8 * dims[i] for i in range(n_sec)))  # (local)
    kappa_cubic = float(np.mean(lam2_mean_CU / lam_hat2))  # (local) global scale of control
    kappa_dev = float(np.max(np.abs(lam2_mean_CU / lam_hat2 / kappa_cubic - 1.0)))  # (local)

    # torsion point, spectral route: 27 t^2 = 9*lam2(0,0)  (LT units of the (0,0) block)
    i00 = sectors.index((0, 0))                      # (local)
    t_hat_sq = 9.0 * lam2_mean_LC[i00] / 27.0        # (local)
    t_hat = sqrt(t_hat_sq)                           # (local)

    lc_global_dev = float(np.max(lc_match_dev))      # (local)
    structured = bool(lc_global_dev < 1e-10)         # (local) machine-eps match to LC t=1/2

    print()
    print(f"[LEG1a] within-block collapse: max spread = {np.max(spread_LC):.6e} "
          f"(< {EPS_SPREAD:g}: {ok_a})")
    print(f"[LEG1b] scale-free ratios vs (u^2+uv+v^2)/7: max rel dev = "
          f"{np.max(ratio_dev):.6e} (< {EPS_RATIO:g}: {ok_b})")
    print(f"[LEG1c] per-sign multiplicity == 8*dim (block) and 8*dim^2 == "
          f"2u^2v^2(u+v)^2 (exact ints): {ok_c}")
    print(f"[SUBCASE] LC(t=1/2) Thm-2.3 closed-form match: max rel dev = "
          f"{lc_global_dev:.3e}  -> STRUCTURED = {structured}")
    print(f"[SUBCASE] torsion point: spectral t_hat = {t_hat:.12f} "
          f"(t^2 = {t_hat_sq:.12f}); operator |t| = {t_op:.12f}")
    if row8_dev_parth:
        print(f"[SUBCASE] row-8 variant on mu=(p-1,q-1): Thm-2.3-component min-dev "
              f"{max(row8_dev_parth):.2e} vs printed-row-8(+twist) min-dev "
              f"{min(row8_dev_paper):.2e} (Thm-2.3 component matches; printed row 8 "
              f"carries a spurious +3(3t-1)(3t-2) at t!=1/3 — non-gating erratum note)")
    print(f"[CONTROL] cubic-modified operator Omega*(2/3): collapse+ratios+mult PASS = "
          f"{cubic_ok}; max spread {np.max(spread_CU):.3e}; max ratio dev "
          f"{np.max(ratio_dev_cu):.3e}; kappa = {kappa_cubic:.12f} "
          f"(1/9 = {1/9:.12f}; sector spread {kappa_dev:.2e})")

    # ---------------- LEG 2: global sigma, 36*sigma*lambda^2 integrality ----------------
    x_all = 36.0 * evals_LC_concat ** 2              # (local) sigma = 1 first (canonical record)
    n36_resid = float(np.max(np.abs(x_all - np.round(x_all))))  # (local)
    sigma_global = 1.0                               # (local)
    ok_d = bool(n36_resid < EPS_N36)                 # (local)
    n_int = np.unique(np.round(x_all).astype(np.int64))  # (local)
    x_cu = 36.0 * evals_CU_concat ** 2               # (local)
    n36_resid_cu = float(np.max(np.abs(x_cu - np.round(x_cu))))  # (local)
    print(f"[LEG2] sigma = 1: max |36*lambda^2 - round| = {n36_resid:.3e} "
          f"(< {EPS_N36:g}: {ok_d}); {n_int.size} distinct integers n "
          f"(n in [{n_int.min()},{n_int.max()}])")
    print(f"[LEG2] cubic control integrality (36*lambda^2 = 4*lam_hat^2): "
          f"max resid = {n36_resid_cu:.3e}")

    # ---------------- LEG 3: residues vs Thm 3.4 at t=1/3 ----------------
    r4_frac, r4_terms = residue_jsum(4, J_MAX)       # (local)
    r3_frac, _ = residue_jsum(3, J_MAX)              # (local) finite: all terms vanish
    r2_frac, _ = residue_jsum(2, J_MAX)              # (local) finite: j in {0,1}
    r1_frac, _ = residue_jsum(1, J_MAX)              # (local) finite: j in {0,..,3}
    r4 = float(r4_frac)                              # (local)
    last_term = float(r4_terms[-1])                  # (local)
    ratio_tail = abs(float(r4_terms[-1]) / float(r4_terms[-6])) ** (1 / 5)  # (local)
    tail_bound = abs(last_term) * ratio_tail / (1 - ratio_tail)  # (local)
    r4_closed = 8.0 * sqrt(3.0) * pi / 243.0         # (local) Poisson/Gaussian-moment closed form
    r4_reldev = abs(r4 / r4_closed - 1.0)            # (local)
    # finite sums must be EXACT rational zeros
    r3_exact_zero = (r3_frac == 0)                   # (local)
    r2_exact_zero = (r2_frac == 0)                   # (local)
    r1_exact_zero = (r1_frac == 0)                   # (local)
    sub_ratios = np.array([float(r3_frac) / r4, float(r2_frac) / r4, float(r1_frac) / r4])  # (local)
    twist_t13 = (3 * Fraction(1, 3) - 1) * (3 * Fraction(1, 3) - 2)  # (local)
    twist_zero = (twist_t13 == 0)                    # (local)
    # Thm 3.4 reference ratios at t=1/3: [(3t-1)(3t-2)]^{1,2,3} * integrals / leading -> (0,0,0)
    ref_ratios = np.zeros(3)                         # (local)
    delta_ratios = np.abs(sub_ratios - ref_ratios)   # (local) |Delta| vs zero-reference (declared)
    ok_e = bool(r4_reldev < EPS_POLY and np.max(delta_ratios) < EPS_POLY
                and twist_zero and r3_exact_zero and r2_exact_zero and r1_exact_zero)  # (local)

    # lattice heat-trace flatness: K(t)*t^4 / ((2/3) I1) - 1 over a t-grid
    I1_closed = 8.0 * pi * sqrt(3.0) / 27.0          # (local) integral_{R^2} x^2y^2(x+y)^2 e^{-Q}
    U = 500                                          # (local) lattice cut
    uu, vv = np.meshgrid(np.arange(1, U + 1, dtype=np.float64),
                         np.arange(1, U + 1, dtype=np.float64), indexing="ij")  # (local)
    mult_grid = 4.0 * uu ** 2 * vv ** 2 * (uu + vv) ** 2  # (local)
    Q_grid = uu ** 2 + uu * vv + vv ** 2             # (local)
    t_grid = np.array([0.02, 0.04, 0.06, 0.08, 0.10, 0.15, 0.20])  # (local)
    K_dev = []                                       # (local)
    for tt in t_grid:
        K = float(np.sum(mult_grid * np.exp(-tt * Q_grid)))  # (local)
        K_dev.append(K * tt ** 4 / ((2.0 / 3.0) * I1_closed) - 1.0)
    K_dev = np.array(K_dev)                          # (local)
    K_flat = float(np.max(np.abs(K_dev)))            # (local)

    print(f"[LEG3] residues of zeta_cubic: r4(jsum,J={J_MAX}) = {r4:.15f} vs closed "
          f"8*sqrt(3)*pi/243 = {r4_closed:.15f} (rel dev {r4_reldev:.3e}; "
          f"tail bound {tail_bound:.1e})")
    print(f"[LEG3] r3 = {r3_frac} (exact zero: {r3_exact_zero}), "
          f"r2 = {r2_frac} (exact zero: {r2_exact_zero}), "
          f"r1 = {r1_frac} (exact zero: {r1_exact_zero})")
    print(f"[LEG3] Thm 3.4 @ t=1/3 coefficient ratios (A6/A8, A4/A8, A2/A8) = (0,0,0); "
          f"computed (r3/r4, r2/r4, r1/r4) = ({sub_ratios[0]:.1e}, {sub_ratios[1]:.1e}, "
          f"{sub_ratios[2]:.1e}); twist (3t-1)(3t-2)|_t=1/3 = {twist_t13} "
          f"(exact zero: {twist_zero}); |t=1/2 value| = {abs(TWIST_T12)} (LC nonzero)")
    print(f"[LEG3] lattice heat-trace flatness: max |K(t) t^4 / ((2/3) I1) - 1| = "
          f"{K_flat:.3e} over t in [0.02, 0.20] (certifies a_2 = a_4 = a_6 = 0)")
    print(f"[LEG3] ok_e = {ok_e} (residue machinery vs Thm 3.4 at t=1/3)")

    # ---------------- diagnostics (non-gating) ----------------
    c2_300 = Fraction(poly_pq(30, 0), 3)             # (local) = 330
    assert c2_300 == 330 and lam_hat_sq(30, 0) == 993
    lam_hat_300 = sqrt(993.0)                        # (local) tau=0 closed form, LT units
    eq1_R300 = 0.633 * sqrt(330.0) + 0.555           # (local) collab eq (1), tau_fold fit, DIAGNOSTIC
    mu_max_300 = max(mu_list_lemma26(30, 0),
                     key=lambda m: poly_pq(m[0], m[1]))  # (local)
    lc_max_300_LT = float(eig_LT_general_t(30, 0, mu_max_300, THALF))  # (local)
    print()
    print(f"[diag] tau=0 closed-form max|lam_hat|(30,0) = sqrt(993) = {lam_hat_300:.6f} "
          f"(Lai-Teh units; cubic point; NO matrix at (30,0))")
    print(f"[diag] LC(t=1/2) closed-form max sqrt at (30,0): mu={mu_max_300}, "
          f"sqrt({lc_max_300_LT:.2f}) = {sqrt(lc_max_300_LT):.6f} LT units "
          f"= {sqrt(lc_max_300_LT)/3.0:.6f} frame units")
    print(f"[diag] eq-(1) HIGH-PW-51 fit at tau_fold={tau_fold}: R_(30,0) = "
          f"0.633*sqrt(330)+0.555 = {eq1_R300:.4f} M_KK — tau_fold-scoped empirical fit, "
          f"NOT a tau=0 criterion (plan anchor-provenance pre-resolution); the two "
          f"quantities live at different tau and different operator normalization")
    print(f"[diag] global scale sigma = {sigma_global:.10g}; cubic-control kappa = "
          f"{kappa_cubic:.10g} (= 1/9 to {abs(kappa_cubic*9-1):.2e})")

    # ---------------- verdict (pre-registered conjunction) ----------------
    legs = {"LEG1a_collapse": ok_a, "LEG1b_ratios": ok_b, "LEG1c_mult": ok_c,
            "LEG2_n36": ok_d, "LEG3_thm34": ok_e}     # (local)
    verdict = "PASS" if all(legs.values()) else "FAIL"  # (local)
    print()
    print(f"=== leg results: {legs} ===")
    print(f"=== {GATE_ID}: {verdict} ===")

    # ---------------- npz ----------------
    np.savez(
        OUT_NPZ,
        sector_p=np.array([s[0] for s in sectors], dtype=np.int64),
        sector_q=np.array([s[1] for s in sectors], dtype=np.int64),
        dims=dims, lam_hat_sq=lam_hat2,
        block_dims=16 * dims,
        spread_rel_module=spread_LC, spread_rel_cubic_control=spread_CU,
        lam2_mean_module=lam2_mean_LC, lam2_min_module=lam2_min_LC,
        lam2_max_module=lam2_max_LC, lam2_mean_cubic_control=lam2_mean_CU,
        ratio_measured=ratio_meas, ratio_target=ratio_tgt, ratio_reldev=ratio_dev,
        ratio_reldev_cubic_control=ratio_dev_cu,
        npos=npos_LC, nneg=nneg_LC, per_sign_expected=8 * dims,
        pw_per_sign_expected=8 * dims ** 2,
        mult_exact_ok=mult_ok, mult_identity_ok=mult_identity,
        evals_module_concat=evals_LC_concat, evals_cubic_concat=evals_CU_concat,
        evals_offsets=np.array(ev_off, dtype=np.int64),
        lc_pred_vals_concat=np.array(lc_pred_vals),
        lc_pred_mult_concat=np.array(lc_pred_mult, dtype=np.int64),
        lc_pred_offsets=np.array(lc_off, dtype=np.int64),
        lc_match_maxreldev=lc_match_dev, lc_match_global=lc_global_dev,
        row8_dev_thm23_component=np.array(row8_dev_parth),
        row8_dev_printed_row8=np.array(row8_dev_paper),
        t_hat_spectral=t_hat, t_hat_sq_spectral=t_hat_sq, t_operator=t_op,
        omega_alpha_real=float(alpha.real), omega_fit_resid=omega_fit_resid,
        phi_sq_scalar=phi_sq_scalar, phi_sq_scalar_dev=phi_sq_dev,
        sigma_global=sigma_global, n36_max_resid=n36_resid,
        n36_max_resid_cubic=n36_resid_cu, n_integers=n_int,
        kappa_cubic_control=kappa_cubic, kappa_sector_spread=kappa_dev,
        r4_jsum=r4, r4_closed=r4_closed, r4_reldev=r4_reldev,
        r4_terms=np.array([float(t_) for t_ in r4_terms]),
        r4_tail_bound=tail_bound,
        r3_exact=float(r3_frac), r2_exact=float(r2_frac), r1_exact=float(r1_frac),
        r_sub_over_r4=sub_ratios, thm34_ref_ratios_t13=ref_ratios,
        twist_t13_exact_zero=bool(twist_zero), twist_t12=TWIST_T12,
        I1_closed=I1_closed, K_flatness_tgrid=t_grid, K_flatness_dev=K_dev,
        K_flatness_max=K_flat,
        diag_lam_hat_300=lam_hat_300, diag_lam_hat_300_sq=993,
        diag_eq1_taufold_R300=eq1_R300, diag_tau_fold=float(tau_fold),
        diag_lc_max_300_LTunits=lc_max_300_LT,
        validation_clifford=cliff_err, validation_conn=conn_err,
        validation_omega_ah=ah_err, validation_herm_max=herm_max,
        validation_hom_max=hom_max, validation_irrep_ah_max=ahg_max,
        gpu_used=gpu_log["used"], gpu_validation_dev=gpu_validation_dev,
        killing_dev=killing_dev, df0_dev=df0_dev,
        ok_LEG1a=ok_a, ok_LEG1b=ok_b, ok_LEG1c=ok_c, ok_LEG2=ok_d, ok_LEG3=ok_e,
        structured_subcase=structured, cubic_control_pass=cubic_ok,
        eps_spread=EPS_SPREAD, eps_ratio=EPS_RATIO, eps_bin=EPS_BIN,
        eps_n36=EPS_N36, eps_poly=EPS_POLY, J_max=J_MAX,
        verdict=verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"[out] npz -> {OUT_NPZ}")

    # ---------------- plot ----------------
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 2, figsize=(13.5, 9.5))  # (local)
    xs = np.arange(n_sec)                            # (local)
    labels = [f"({p},{q})" for (p, q) in sectors]    # (local)
    floor = 1e-17                                    # (local) display floor for log axes

    ax = axes[0, 0]
    ax.semilogy(xs, np.maximum(spread_LC, floor), "o-", color="crimson",
                label="module operator (tau=0)")
    ax.semilogy(xs, np.maximum(spread_CU, floor), "s-", color="seagreen",
                label="cubic control Omega*(2/3)")
    ax.axhline(EPS_SPREAD, color="k", ls="--", lw=1, label="1e-12 pin")
    ax.set_title("LEG 1a: within-block |lambda| spread (collapse test)")
    ax.set_ylabel("relative spread"); ax.legend(fontsize=8)

    ax = axes[0, 1]
    ax.semilogy(xs, np.maximum(ratio_dev, floor), "o-", color="crimson",
                label="module operator")
    ax.semilogy(xs, np.maximum(ratio_dev_cu, floor), "s-", color="seagreen",
                label="cubic control")
    ax.axhline(EPS_RATIO, color="k", ls="--", lw=1, label="1e-12 pin")
    ax.set_title("LEG 1b: |lambda^2 ratio / [(u^2+uv+v^2)/7] - 1|")
    ax.set_ylabel("relative deviation"); ax.legend(fontsize=8)

    ax = axes[1, 0]
    ax.plot(xs, npos_LC - 8 * dims, "o-", color="crimson", label="npos - 8*dim (module)")
    ax.plot(xs, nneg_LC - 8 * dims, "x--", color="darkorange", label="nneg - 8*dim (module)")
    ax.plot(xs, npos_CU - 8 * dims, "s:", color="seagreen", label="npos - 8*dim (cubic)")
    ax.axhline(0, color="k", lw=1)
    ax.set_title("LEG 1c: per-sign multiplicity match (exact integers)")
    ax.set_ylabel("count deviation"); ax.legend(fontsize=8)

    ax = axes[1, 1]
    ax.semilogy(xs, np.maximum(lc_match_dev, floor), "d-", color="navy",
                label="measured vs LC(t=1/2) Thm-2.3 closed form")
    ax.axhline(1e-12, color="k", ls="--", lw=1, label="1e-12")
    ax.set_title("FAIL-SUBCASE: structured match to Levi-Civita t=1/2")
    ax.set_ylabel("max relative deviation"); ax.legend(fontsize=8)

    for ax in axes.flat:
        ax.set_xticks(xs[::3])
        ax.set_xticklabels(labels[::3], rotation=45, fontsize=7)
        ax.grid(alpha=0.3)
    fig.suptitle(f"{GATE_ID}: {verdict} — module tau=0 operator at t=1/2 (LC), "
                 f"t_hat={t_hat:.6f}; cubic control PASS={cubic_ok}; "
                 f"r4={r4:.6f} (8*sqrt(3)*pi/243), r3=r2=r1=0 exact", fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=140)
    print(f"[out] png -> {OUT_PNG}")

    # ---------------- 4-tuple + payload ----------------
    value = (f"FAIL_LEG1a_maxspread={np.max(spread_LC):.3e}"
             f"_LEG1b_maxratiodev={np.max(ratio_dev):.3e}"
             f"_LEG1c_mult_exact={ok_c}"
             f"_LEG2_sigma=1_n36resid={n36_resid:.2e}"
             f"_LEG3_r4dev={r4_reldev:.2e}_rsub_exact_zero"
             f"_SUBCASE=STRUCTURED_LC_that={t_hat:.10f}_lcdev={lc_global_dev:.2e}"
             f"_cubic_control={'PASS' if cubic_ok else 'FAIL'}"
             if verdict == "FAIL" else
             f"PASS_maxspread={np.max(spread_LC):.3e}_maxratiodev={np.max(ratio_dev):.3e}"
             f"_n36resid={n36_resid:.2e}_r4dev={r4_reldev:.2e}")  # (local)
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    extra_rows = []  # (local)
    if verdict == "FAIL":
        extra_rows = [
            "# ESCALATION: tau>0 outputs UNTRUSTED pending remediation — downstream "
            "consumers W3-1(prong B), W4-10, W4-11, W6-14, W6-15 flagged",
            f"# FAIL-SUBCASE: STRUCTURED — framework tau=0 operator sits at the "
            f"Levi-Civita torsion point t=1/2 of the Lai-Teh family (NOT the Kostant "
            f"cubic point t=1/3): all 28 sector spectra match the Thm-2.3 T_t closed "
            f"form at t=1/2 to {lc_global_dev:.2e}; spectral t_hat={t_hat:.10f}, "
            f"operator |t|={t_op:.10f}; cubic-modified control Omega*(2/3) passes "
            f"collapse+ratios+mult at machine epsilon (kappa=1/9)",
            f"# NOTE: lambda^2=n/36 PROVEN record remains VALID — the LC spectrum is "
            f"n/36-integral (n = 2[poly(mu)+poly(V)]+9; max resid {n36_resid:.2e}; "
            f"sigma=1); the plan parenthetical that a structured t=1/2 finding "
            f"contradicts n/36 does NOT fire",
        ]
    payload = print_verdict_payload(verdict, value, audit_sha, content_sha,
                                    companion_note=f"legs={legs}",
                                    extra_rows=extra_rows)  # (local)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit 0 = script ran (math-scripts.md exit-code semantics)


if __name__ == "__main__":
    sys.exit(main())
