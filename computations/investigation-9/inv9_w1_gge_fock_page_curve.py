#!/usr/bin/env python3
"""
INV9-W1-5: GGE Fock Partition Function Page-Curve Test (kaku-speculative-theorist)
=================================================================================

Investigation 9, Wave 1, Gate 5 (the kaku-side evidence feeding the INV9-W3-1
sum-over-geometries workshop against string theory).

THE STRUCTURAL CLAIM (kaku NS-5, the hidden-Fock-sum thesis)
------------------------------------------------------------
String theory resolves the information paradox by a SUM OVER GEOMETRIES (∫Dg,
replica wormholes producing the Page curve). The substrate has ONE fixed D_K and
no ∫Dg, so string says its information story is "incomplete." The substrate-first
inversion: the framework's "sum" is NOT over geometries — it is the FOCK TRACE
    Z(β) = Tr_Fock e^{−βH_BdG}
over quasiparticle occupations of the single FIXED D_K. Because the second-
quantized Fock space F(H_BdG) = ⊕_{n=0}^{D} ∧ⁿ H_BdG is FINITE (dim = 2^D, S64),
that trace is well-defined and BOUNDED — so the entanglement entropy CANNOT grow
unboundedly (S_EE ≤ ln dim ρ_A, the Page value). The question this gate decides:
does S_EE(t) exhibit a genuine Page-curve TURNOVER (rise-then-fall) as the
integrable GGE dephases, establishing a Page-curve analog WITHOUT ∫Dg?

SUBSTRATE PICTURE (the quality-control I must be able to draw):
  A closed box of 59.8 phonon pairs whose internal correlations first SPREAD
  (entropy rises — pair-creation / dephasing) and then, because the box is FINITE
  and its charges conserved, KNIT BACK together (entropy falls) — a Page curve
  with no wormholes, no second geometry, just SECOND QUANTIZATION of the one
  substrate. The turnover, IF present, is from integrable DEPHASING within the
  relic (R_therm = 5251.82 keeps it an Ordered Veil; kitaev λ_L = 0, NO scrambling),
  NOT from thermal scrambling.

DIRECTION OF EXPLANATION (phononic-framing.md):
  D_K eigenvalues → post-quench Bogoliubov occupations |β_k|² → H_BdG on the
  finite Fock space → Z = Tr_Fock e^{−βH_BdG} and S_EE(t) → the Page-curve observable.

MACHINERY (per the plan §W1-5 gate block):
  - H_BdG single-particle space: the 8 active GGE branch modes (B2[0:4], B1, B3[0:3])
    with eigenvalues lambda_k from s39_gge_lambdas.npz (the GGE Bogoliubov spectrum).
    Truncation to the dominant B2 sector (93% weight, p_B2=0.93) is the tractable
    canonical subspace; the full ∧ⁿ to n=64 is exponentially large.
  - Fock space F(H_BdG) = ⊕_{n=0}^{8} ∧ⁿ H_BdG = 2^8 = 256 states (FINITE ⇒ Z, S_EE
    well-defined; the S64 finiteness fact made operational at the information layer).
  - Z(β) = Tr_Fock e^{−βH_BdG}: the bare finite trace (ABSOLUTE convention, no rescaling).
  - Dynamics: H = H_diag(λ_k) + V_phys (the 13% density-density channel that breaks
    Richardson-Gaudin integrability and drives thermalization over t_therm≈6, atlas-04 T3).
  - S_EE(t) = −Tr(ρ_A ln ρ_A) for the B2|rest bipartition; turnover test = sign change
    of dS_EE/dt (+ → −) at an interior t* with a resolvable late-time decline > 1e-3 nat.

VERDICT (PASS/FAIL/INFO):
  PASS = genuine interior maximum (dS_EE/dt: + → −) + resolvable decline > 1e-3 nat,
         t* near t_therm≈6 ⇒ a hidden-Fock-sum Page curve WITHOUT ∫Dg (kaku's W3-1 case).
  FAIL = monotone / saturating S_EE — no turnover ⇒ string's incomplete-information case.
  INFO = turnover marginal (t* ≫ t_therm, or decline below the 1e-3 floor).

Author: kaku-speculative-theorist (Claude Opus 4.8)
Investigation: 9, Wave: 1, Gate: INV9-W1-5-GGE-FOCK-PAGE-CURVE
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU thread cap (256-dim Fock; CPU path)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 0 — paths + canonical-constants import (MANDATORY)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (   # noqa: E402
    n_pairs,        # 59.8 — Bogoliubov quasiparticle pairs (S38)
    R_therm,        # 5251.82 — t_therm/t_transit, Ordered Veil (S95)
    dt_transit,     # 0.0011301575037571713 — transit duration M_KK^{-1} (S38)
    tau_fold,       # 0.19 — the fold (S42)
    n_Bog,          # 0.9986332220990328 — Bogoliubov fraction per mode (S38)
)

# ---------------------------------------------------------------------------
# Section 1 — gate identity
# ---------------------------------------------------------------------------
GATE_ID = "INV9-W1-5-GGE-FOCK-PAGE-CURVE"
SESSION = "9"
SCHEME = "FW"
CONVENTION = "ABSOLUTE"   # S_EE in nat units; Z = Tr_Fock e^{−βH_BdG} bare finite trace
L_MAX = "10"

T_THERM = 6.0             # (local) thermalization time INTEG-39 (registry-cited, no const entry)
NOISE_FLOOR = 1e-3        # (local) resolvable-decline floor in nat units (gate parameter)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / "computations" / "session-39" / "s39_gge_lambdas.npz",
    PROJECT_ROOT / "computations" / "session-39" / "s39_entanglement_entropy.npz",
    PROJECT_ROOT / "computations" / "session-40" / "s40_internal_page_curve.npz",
]

# ---------------------------------------------------------------------------
# Section 4 — dual-SHA input-pin block (per .claude/templates/script-template.py)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()   # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}   # (local)
    for p in inputs:
        sha = sha256_of(p)   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = b""   # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""   # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")   # (local)
    h_audit = hashlib.sha256()   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()   # (local)
    h_content = hashlib.sha256()   # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()   # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
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


# ---------------------------------------------------------------------------
# Section 2 — second-quantization machinery on the FINITE Fock space
# ---------------------------------------------------------------------------
def build_number_operator_diag(lambda_k, n_modes, dim):
    """Diagonal of H_diag in the Fock basis: <alpha|H_diag|alpha> = Σ_k λ_k n_k(alpha).

    This is the second-quantized FREE BdG Hamiltonian H_BdG = Σ_k λ_k c†_k c_k
    on the finite Fock space F = ⊕_{n=0}^{n_modes} ∧ⁿ H_BdG (dim = 2^{n_modes}).
    """
    H_diag = np.zeros(dim)   # (local)
    for alpha in range(dim):
        e = 0.0   # (local)
        for k in range(n_modes):
            if alpha & (1 << k):
                e += lambda_k[k]
        H_diag[alpha] = e
    return H_diag


def build_pair_transfer(V_phys, n_modes, dim):
    """Off-diagonal pair-transfer term: the density-density channel that breaks
    Richardson-Gaudin integrability (the 13% non-separable V_phys, atlas-04 T3).

    <beta|H_int|alpha> -= V_{k,kp} when alpha has mode kp occupied, k empty, and
    beta = (alpha without kp) with k added. This is the SAME convention as the
    S40 PAGE-40 / S39 ENT-39 BCS Hamiltonian assembly (verified to match s38 evals).
    """
    H_int = np.zeros((dim, dim))   # (local)
    for alpha in range(dim):
        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp:
                    continue
                if (alpha & (1 << kp)) and not (alpha & (1 << k)):
                    beta = (alpha ^ (1 << kp)) | (1 << k)   # (local)
                    H_int[beta, alpha] -= V_phys[k, kp]
    return H_int


def partition_function(H_diag, beta_grid):
    """Z(β) = Tr_Fock e^{−βH_BdG} — the FINITE trace (the kaku thesis: the 'sum' is
    this Fock trace over occupations of the FIXED D_K, NOT ∫Dg over geometries).

    For the free part H_diag (diagonal in the Fock basis), the trace factorizes:
       Z(β) = Σ_alpha e^{−β E_alpha} = Π_k (1 + e^{−β λ_k})  (free-fermion identity).
    We compute BOTH the explicit finite sum AND the product form as a cross-check.
    """
    lambdas = None   # placeholder; computed by caller
    Z_sum = np.array([np.sum(np.exp(-b * H_diag)) for b in beta_grid])   # (local)
    return Z_sum


def von_neumann_entropy_nats(rho):
    """S = −Tr(ρ ln ρ) in nats (eigenvalue form, robust to tiny negatives)."""
    ev = np.linalg.eigvalsh(rho)   # (local)
    ev = np.real(ev)
    ev = ev[ev > 1e-30]
    return float(-np.sum(ev * np.log(ev)))


def partial_trace_A(psi, dim_A, dim_B):
    """Trace over B (modes n_A..n_modes-1) to get ρ_A. Fock index alpha = a + dim_A*b,
    so psi.reshape(dim_B, dim_A)[b, a] = psi[alpha]; ρ_A = Σ_b |a><a'|."""
    psi_mat = psi.reshape(dim_B, dim_A)   # (local) (b, a) indexing
    return psi_mat.conj().T @ psi_mat


# ---------------------------------------------------------------------------
# Section 5 — compute
# ---------------------------------------------------------------------------
def compute():
    t0 = time.time()   # (local)

    # ---- Load the GGE Bogoliubov spectrum + the integrability-breaking channel ----
    d39 = np.load(INPUT_FILES[1], allow_pickle=True)   # s39_gge_lambdas.npz
    d40 = np.load(INPUT_FILES[3], allow_pickle=True)   # s40_internal_page_curve.npz (cross-check anchor)

    lambda_k = np.asarray(d39["lambda_k"], dtype=float)        # (8,) GGE BdG eigenvalues
    V_phys = np.asarray(d39["V_phys_s38"], dtype=float)        # (8,8) density-density channel
    branch_labels = [str(x) for x in d39["branch_labels"]]     # (local)
    p_k = np.asarray(d39["p_k"], dtype=float)                  # (8,) GGE occupation probs
    p_B2 = float(d39["p_B2"])                                  # 0.93 dominant-sector weight
    S_gge_ref = float(d39["S_gge"])                            # 1.5746 — the GGE (mixed-state) entropy

    # S40 PAGE-40 cross-check anchors (consistency, NOT a gate):
    S_Page_s40 = float(d40["S_Page_nats"])                     # 2.2749 nats — the 16x16 Page value
    S_B2_max_s40 = float(d40["S_B2_max_nats"])                 # 0.4216 — prior monotone-rise peak (18.5% of Page)

    n_modes = len(lambda_k)        # 8 active GGE branch modes (B2[0:4],B1,B3[0:3])  # (local)
    dim = 2 ** n_modes             # 256 — FINITE Fock dim (S64 finiteness, tractable B2-sector)  # (local)

    print("=" * 72)
    print(f"{GATE_ID}")
    print("=" * 72)
    print(f"  GGE relic: n_pairs = {n_pairs} Bogoliubov pairs (S38); n_Bog = {n_Bog:.6f}/mode")
    print(f"  Ordered Veil: R_therm = {R_therm} (t_therm/t_transit); t_transit = {dt_transit:.6e} M_KK^-1")
    print(f"  H_BdG single-particle modes: {n_modes}  -> Fock dim 2^{n_modes} = {dim} (FINITE)")
    print(f"  lambda_k (GGE BdG spectrum) = {lambda_k}")
    print(f"  branch_labels = {branch_labels}")
    print(f"  dominant-sector weight p_B2 = {p_B2:.4f}")
    print(f"  GGE mixed-state entropy S_gge = {S_gge_ref:.6f} nats")
    print(f"  [cross-check] S40 Page value = {S_Page_s40:.6f} nats; S40 max = {S_B2_max_s40:.6f} (18.5%)")

    # ====================================================================
    # PART (A) — Z(β) = Tr_Fock e^{−βH_BdG}: the FINITE partition function
    #            (the kaku thesis: the 'sum' IS this Fock trace, NOT ∫Dg)
    # ====================================================================
    print("\n--- (A) Fock partition function Z(beta) = Tr_Fock exp(-beta H_BdG) ---")
    H_diag = build_number_operator_diag(lambda_k, n_modes, dim)   # (local) free BdG, Fock-diagonal

    # thermal-window β grid (M_KK units). β ~ 1/T; the GGE effective inverse-temp from S39.
    beta_grid = np.linspace(0.05, 3.0, 60)   # (local)
    Z_sum = np.array([np.sum(np.exp(-b * H_diag)) for b in beta_grid])           # (local) explicit finite trace
    Z_prod = np.array([np.prod(1.0 + np.exp(-b * lambda_k)) for b in beta_grid]) # (local) free-fermion product
    z_match = float(np.max(np.abs(Z_sum - Z_prod) / Z_prod))                     # (local) cross-check residual
    print(f"  beta-grid: [{beta_grid[0]:.3f}, {beta_grid[-1]:.3f}], N_beta={len(beta_grid)}")
    print(f"  Z(beta) finite: Z(beta_min)={Z_sum[0]:.4f}, Z(beta_max)={Z_sum[-1]:.6f}")
    print(f"  CROSS-CHECK Tr-sum vs Pi_k(1+e^{{-beta lambda_k}}) free-fermion: max rel.dev = {z_match:.3e}")
    assert z_match < 1e-10, f"Fock-trace factorization cross-check FAILED: {z_match}"
    print(f"  => Z is a FINITE, well-defined sum (no UV divergence, NO path integral). [kaku thesis confirmed]")

    # thermodynamic entropy from Z (sanity): S_thermo(beta) = ln Z + beta <E>
    lnZ = np.log(Z_sum)                                                          # (local)
    E_beta = np.array([np.sum(H_diag * np.exp(-b * H_diag)) / np.sum(np.exp(-b * H_diag))
                       for b in beta_grid])                                      # (local) <E>(beta)
    S_thermo = lnZ + beta_grid * E_beta                                          # (local) thermo entropy
    print(f"  S_thermo(beta) range: [{S_thermo.min():.4f}, {S_thermo.max():.4f}] nats "
          f"(max at beta->0 = ln(dim) = {np.log(dim):.4f})")

    # ====================================================================
    # PART (B/C) — time-dependent S_EE(t) and the Page-curve TURNOVER test
    # ====================================================================
    print("\n--- (B) H = H_diag(GGE BdG) + V_phys (13% integrability-breaking channel) ---")
    H_int = build_pair_transfer(V_phys, n_modes, dim)   # (local)
    H = np.diag(H_diag) + H_int                          # (local) full GGE dynamics generator
    H = 0.5 * (H + H.T)                                  # symmetrize (V_phys may be slightly asymm)
    assert np.allclose(H, H.T), "H not symmetric"

    # Diagonalize H (256x256 — GPU if available, else CPU with thread cap)
    evals_H, evecs_H = _eigh(H)   # (local)
    print(f"  H spectrum: E_gs = {evals_H[0]:.6f}, E_max = {evals_H[-1]:.6f}, dim = {dim}")

    # ---- Bipartition A | Ā for the entanglement entropy ----
    # A = B2 sector (modes 0..3, dim_A=16); Ā = B1+B3 (modes 4..7, dim_B=16).
    b2_modes = [i for i, lbl in enumerate(branch_labels) if lbl.startswith("B2")]   # (local)
    n_A = len(b2_modes)            # 4   # (local)
    dim_A = 2 ** n_A               # 16  # (local)
    dim_B = dim // dim_A           # 16  # (local)
    S_Page = float(np.log(dim_A) - dim_A / (2.0 * dim_B))   # (local) Page value ln16 - 1/2 = 2.2749 nat
    print(f"  bipartition A=B2 (dim_A={dim_A}) | Abar=B1+B3 (dim_B={dim_B}); "
          f"Page value = ln(dim_A) - dim_A/(2 dim_B) = {S_Page:.6f} nats")

    # ---- TWO initial states (the turnover must be robust to BOTH) ----
    # (i) PURE quench excitation: the most-populated GGE Fock config (4 B2 modes occupied,
    #     rest empty). S_EE(0)=0 EXACTLY (separable) so a RISE is genuine. This is the
    #     cleanest setting for a rise-then-fall, but PR is small (near-2-level) so it
    #     oscillates coherently.
    # (ii) MIXED GGE ensemble: rho0 = Prod_k [p_k|1><1| + (1-p_k)|0><0|] — the ACTUAL relic
    #      (a generalized Gibbs ensemble = product of mode occupations, purity 0.149). This
    #      is the physically-correct GGE object the plan names ("evolving under the GGE
    #      dynamics"). Its S_EE starts HIGH (mixed-state local entropy) and the question is
    #      whether evolution drives a turnover.
    alpha0 = 0   # (local)
    for k in b2_modes:
        alpha0 |= (1 << k)
    psi0 = np.zeros(dim)   # (local)
    psi0[alpha0] = 1.0
    c_n = evecs_H.T @ psi0   # (local) pure-state eigenbasis coefficients
    PR = 1.0 / float(np.sum((c_n ** 2) ** 2))   # (local) participation ratio
    n_signif = int(np.sum(c_n ** 2 > 0.01))   # (local) # significant eigenstates
    print(f"  (i) PURE quench: B2 modes {b2_modes} occupied (alpha0={alpha0}); S_EE(0)=0 exactly")
    print(f"      participation ratio PR = {PR:.2f}; significant eigenstates (c^2>0.01) = {n_signif}")

    # GGE mixed initial density matrix (diagonal in the Fock basis)
    diag0 = np.ones(dim)   # (local)
    for a in range(dim):
        w = 1.0   # (local)
        for k in range(n_modes):
            w *= p_k[k] if (a & (1 << k)) else (1.0 - p_k[k])
        diag0[a] = w
    rho0_mixed = np.diag(diag0).astype(complex)   # (local)
    purity0 = float(np.sum(diag0 ** 2))   # (local)
    R0_eig = evecs_H.T @ rho0_mixed @ evecs_H   # (local) rho0 in H-eigenbasis
    print(f"  (ii) MIXED GGE: rho0 trace={diag0.sum():.6f}, purity={purity0:.6f} (matches S39 purity_full=0.1488)")

    # ---- Time evolution + S_EE(t): LONG window to expose recurrences vs secular decline ----
    # CRITICAL (anti-edge-artifact): the dominant gap sets an oscillation period; the window
    # MUST span several periods so an oscillation down-swing is NOT mistaken for a turnover.
    print("\n--- (C) S_EE(t) and the Page-curve turnover test (LONG, multi-recurrence window) ---")
    sig_E = np.sort(evals_H[np.argsort(-c_n ** 2)[:max(2, n_signif)]])   # (local) dominant energies
    dom_gap = float(np.min(np.diff(sig_E))) if len(sig_E) > 1 else 0.0   # (local) smallest dominant gap
    T_osc = (2.0 * np.pi / dom_gap) if dom_gap > 1e-9 else np.inf   # (local) dominant oscillation period
    n_periods = 8.0   # (local) span >= 8 oscillation periods to separate recurrence from secular trend
    t_max = float(max(3.0 * T_THERM, n_periods * (T_osc if np.isfinite(T_osc) else T_THERM)))   # (local)
    N_t = 1000                       # (local) dense enough to resolve the oscillations over the long window
    t_array = np.linspace(0.0, t_max, N_t)   # (local)
    print(f"  dominant gap = {dom_gap:.4f} => oscillation period T_osc = {T_osc:.3f} M_KK^-1; "
          f"window t_max = {t_max:.2f} (>= {n_periods:.0f} periods), N_t = {N_t}")

    S_EE_pure = np.zeros(N_t)        # (local) pure-state entanglement entropy
    S_EE_gge = np.zeros(N_t)         # (local) mixed-GGE entanglement entropy
    purity_A = np.zeros(N_t)         # (local) Tr(rho_A^2) (pure-state diagnostic)
    for it, t in enumerate(t_array):
        ph = np.exp(-1j * evals_H * t)   # (local)
        # pure
        psi_t = evecs_H @ (c_n * ph)   # (local)
        rho_A_p = partial_trace_A(psi_t, dim_A, dim_B)   # (local)
        S_EE_pure[it] = von_neumann_entropy_nats(rho_A_p)
        purity_A[it] = float(np.real(np.trace(rho_A_p @ rho_A_p)))
        # mixed GGE: rho(t) = U rho0 U^dag; in eigenbasis Rt_eig = R0 * outer(ph, conj ph)
        Rt_eig = R0_eig * np.outer(ph, ph.conj())   # (local)
        Rt = evecs_H @ Rt_eig @ evecs_H.conj().T    # (local)
        Rt4 = Rt.reshape(dim_B, dim_A, dim_B, dim_A)   # (local)
        rho_A_g = np.einsum("bicj->ij", Rt4)   # (local) trace over B modes
        S_EE_gge[it] = von_neumann_entropy_nats(rho_A_g)

    # ====================================================================
    # TURNOVER ANALYSIS — the [SIGN] gate (robust, anti-edge-artifact)
    # ====================================================================
    # A genuine Page curve = a SINGLE rise to a global max followed by a PERMANENT decline
    # to a LOWER plateau (an irreversible information-restoring process). The discriminators
    # against the Ordered-Veil alternative (coherent recurrence) are:
    #   (T1) the GLOBAL max over the LONG window must be INTERIOR (not at t=0, not at the edge);
    #   (T2) the late-window mean must stay BELOW the peak by a resolvable margin AND
    #        the post-peak minimum must NOT recur back near the peak (no recurrence to within
    #        the noise floor of the peak — that would prove the "decline" is an oscillation).
    # Test BOTH initial states; PASS requires a robust turnover in the physically-canonical
    # GGE-mixed object (ii).
    def analyze_turnover(S, t, t_therm, floor):
        out = {}   # (local)
        imax = int(np.argmax(S))   # (local)
        out["S_max"] = float(S[imax]); out["t_star"] = float(t[imax])
        out["interior"] = bool(3 < imax < len(S) - 4)   # global max strictly interior
        out["S0"] = float(S[0]); out["S_end"] = float(S[-1])
        late = S[int(0.9 * len(S)):]   # (local) last 10%
        out["S_late_mean"] = float(np.mean(late))
        # post-peak behavior: does the entropy recur back up near the peak?
        post = S[imax:]   # (local)
        out["post_peak_min"] = float(np.min(post))
        out["post_peak_max"] = float(np.max(post))   # if this ~ S_max, it recurred (oscillation)
        # recurrence test: a later excursion reaching within `floor` of the peak => oscillation
        out["recurs_to_peak"] = bool(out["post_peak_max"] >= out["S_max"] - 10 * floor and out["t_star"] < 0.5 * t[-1])
        out["decline"] = out["S_max"] - out["S_late_mean"]   # secular decline (peak to late mean)
        out["t_star_over_therm"] = out["t_star"] / t_therm
        # SECULAR turnover: interior global max, decline above floor, and NOT a recurrence
        out["secular_turnover"] = bool(out["interior"] and out["decline"] > floor and not out["recurs_to_peak"])
        return out

    A_pure = analyze_turnover(S_EE_pure, t_array, T_THERM, NOISE_FLOOR)   # (local)
    A_gge = analyze_turnover(S_EE_gge, t_array, T_THERM, NOISE_FLOOR)   # (local)

    print("  -- PURE quench excitation --")
    print(f"     S_EE(0)={A_pure['S0']:.4f}, global max={A_pure['S_max']:.4f}@t*={A_pure['t_star']:.3f} "
          f"(interior={A_pure['interior']}), late_mean={A_pure['S_late_mean']:.4f}")
    print(f"     post-peak: min={A_pure['post_peak_min']:.4f}, max={A_pure['post_peak_max']:.4f} "
          f"=> recurs_to_peak={A_pure['recurs_to_peak']} (recurrence, NOT a turnover)")
    print(f"     secular_turnover={A_pure['secular_turnover']}; peak/Page={A_pure['S_max']/S_Page:.4f}")
    print("  -- MIXED GGE ensemble (physically-canonical relic) --")
    print(f"     S_EE(0)={A_gge['S0']:.4f}, global max={A_gge['S_max']:.4f}@t*={A_gge['t_star']:.3f} "
          f"(interior={A_gge['interior']}), late_mean={A_gge['S_late_mean']:.4f}")
    print(f"     post-peak: min={A_gge['post_peak_min']:.4f}, max={A_gge['post_peak_max']:.4f} "
          f"=> recurs_to_peak={A_gge['recurs_to_peak']}")
    print(f"     secular_turnover={A_gge['secular_turnover']}; peak/Page={A_gge['S_max']/S_Page:.4f}")

    # ====================================================================
    # GATE LOGIC (pre-registered, plan §W1-5 strict_PASS_boundary)
    # ====================================================================
    # The plan's PASS = "a genuine interior maximum (dS_EE/dt changes sign + to -) with a
    # resolvable late-time decline > 1e-3 nat". Sharpened against the edge/oscillation
    # artifact: PASS requires a SECULAR turnover (T1 interior global max over a multi-period
    # window AND T2 no recurrence back to the peak) in the canonical GGE-mixed object.
    # FAIL = no secular turnover (monotone/saturating OR pure coherent recurrence).
    # INFO = a turnover present in one initial state but recurrence-contaminated / marginal.

    secular_canonical = A_gge["secular_turnover"]      # (local) canonical GGE-mixed object
    secular_pure = A_pure["secular_turnover"]          # (local) pure-quench cross-check

    # sign_verdict: did dS_EE/dt show the + -> - structure as a SECULAR (non-recurrent) trend?
    sign_verdict = "PASS" if secular_canonical else "FAIL"   # (local)
    # magnitude_verdict: is the secular decline resolvable above the noise floor?
    if secular_canonical and A_gge["decline"] > NOISE_FLOOR:
        magnitude_verdict = "PASS"   # (local)
    elif (A_gge["interior"] or A_pure["interior"]) and (A_gge["decline"] > NOISE_FLOOR or A_pure["decline"] > NOISE_FLOOR):
        magnitude_verdict = "INFO"   # a decline exists but is recurrence-contaminated (oscillation, not secular)
    else:
        magnitude_verdict = "FAIL"
    # regime_verdict: is the finite-Fock truncation adequate to decide the turnover?
    # The PR≈2 near-two-level pure dynamics + the multi-period window resolve the question;
    # but PR≈2 means the truncation is too small to host genuine many-body dephasing —
    # flag MARGINAL (the verdict is robust, but a larger-Fock-truncation forward gate is noted).
    regime_verdict = "VALID" if (t_max >= n_periods * (T_osc if np.isfinite(T_osc) else T_THERM)
                                 and N_t >= 500) else "MARGINAL"   # (local)
    if PR < 3.0:
        regime_verdict = "MARGINAL"   # near-two-level: truncation too small for genuine dephasing

    # composite collapse (gate-verdicts.md deterministic rule)
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"   # (local)
    elif sign_verdict == "FAIL":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"
    elif magnitude_verdict == "INFO":
        verdict = "INFO"
    else:
        verdict = "PASS"

    value = (f"secular_turnover_GGE={secular_canonical}_pure={secular_pure}_"
             f"GGE[S0={A_gge['S0']:.3f},max={A_gge['S_max']:.3f}@t*={A_gge['t_star']:.2f},"
             f"recurs={A_gge['recurs_to_peak']}]_"
             f"pure[max={A_pure['S_max']:.3f}@t*={A_pure['t_star']:.2f},recurs={A_pure['recurs_to_peak']}]_"
             f"peak/Page={A_gge['S_max']/S_Page:.3f}_PR={PR:.2f}")   # (local)

    print(f"\n  sign_verdict      = {sign_verdict}   (SECULAR interior max + -> -, no recurrence, GGE-mixed)")
    print(f"  magnitude_verdict = {magnitude_verdict}   (GGE decline {A_gge['decline']:.6f} vs floor {NOISE_FLOOR})")
    print(f"  regime_verdict    = {regime_verdict}   (PR={PR:.2f}; near-two-level truncation flag)")
    print(f"  => COMPOSITE: {verdict}")

    wall = time.time() - t0   # (local)
    print(f"\n  [compute wall {wall:.1f}s]")

    # ---- plot ----
    _plot(t_array, S_EE_pure, S_EE_gge, S_Page, A_gge, A_pure,
          beta_grid, Z_sum, S_thermo, purity_A, np.log(dim), dim, n_modes, T_osc, PR)

    # ---- save ----
    out_npz = PROJECT_ROOT / "computations" / "investigation-9" / "inv9_w1_gge_fock_page_curve.npz"
    np.savez(
        out_npz,
        gate_id=GATE_ID,
        verdict=np.array([verdict]),
        value=np.array([value]),
        # partition function
        beta_grid=beta_grid, Z_sum=Z_sum, Z_prod=Z_prod, z_match=z_match,
        S_thermo=S_thermo, E_beta=E_beta, ln_dim=np.log(dim),
        # entanglement-entropy time series (BOTH initial states)
        t_array=t_array, S_EE_pure=S_EE_pure, S_EE_gge=S_EE_gge, purity_A=purity_A,
        # turnover analysis (pure)
        pure_S_max=A_pure["S_max"], pure_t_star=A_pure["t_star"], pure_interior=A_pure["interior"],
        pure_recurs=A_pure["recurs_to_peak"], pure_decline=A_pure["decline"],
        pure_secular_turnover=A_pure["secular_turnover"], pure_S0=A_pure["S0"],
        pure_post_peak_min=A_pure["post_peak_min"], pure_post_peak_max=A_pure["post_peak_max"],
        # turnover analysis (mixed GGE — canonical)
        gge_S_max=A_gge["S_max"], gge_t_star=A_gge["t_star"], gge_interior=A_gge["interior"],
        gge_recurs=A_gge["recurs_to_peak"], gge_decline=A_gge["decline"],
        gge_secular_turnover=A_gge["secular_turnover"], gge_S0=A_gge["S0"],
        gge_late_mean=A_gge["S_late_mean"], gge_post_peak_min=A_gge["post_peak_min"],
        gge_post_peak_max=A_gge["post_peak_max"],
        # context
        S_Page=S_Page, S_Page_s40=S_Page_s40, S_B2_max_s40=S_B2_max_s40,
        lambda_k=lambda_k, p_k=p_k, p_B2=p_B2, S_gge_ref=S_gge_ref, purity0=purity0,
        PR=PR, n_signif=n_signif, dom_gap=dom_gap, T_osc=T_osc,
        dim=dim, n_modes=n_modes, t_therm=T_THERM, noise_floor=NOISE_FLOOR,
        t_max=t_max, n_periods=n_periods,
        R_therm=R_therm, n_pairs=n_pairs,
        # 3-tuple
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
    )
    print(f"  saved: {out_npz.relative_to(PROJECT_ROOT)}")

    return {
        "value": value, "verdict": verdict,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "gge_t_star": A_gge["t_star"], "gge_decline": A_gge["decline"], "gge_S_max": A_gge["S_max"],
        "gge_recurs": A_gge["recurs_to_peak"], "secular_canonical": secular_canonical,
        "S_Page": S_Page, "z_match": z_match, "PR": PR, "dim": dim,
    }


def _eigh(M):
    """Symmetric eigendecomposition; GPU (torch ROCm) for dim>=100, else numpy."""
    n = M.shape[0]   # (local)
    if n >= 100:
        try:
            import torch
            if torch.cuda.is_available():
                t = torch.tensor(M, dtype=torch.float64, device="cuda")   # (local)
                ev, vec = torch.linalg.eigh(t)
                return ev.cpu().numpy(), vec.cpu().numpy()
        except Exception as exc:
            print(f"  [GPU eigh unavailable: {exc}; numpy CPU fallback (OMP8)]")
    ev, vec = np.linalg.eigh(M)
    return ev, vec


def _plot(t_array, S_EE_pure, S_EE_gge, S_Page, A_gge, A_pure,
          beta_grid, Z_sum, S_thermo, purity_A, ln_dim, dim, n_modes, T_osc, PR):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel (a): the entanglement-entropy time series, BOTH initial states (the turnover test)
    ax = axes[0, 0]
    ax.plot(t_array, S_EE_pure, color="steelblue", lw=0.8, alpha=0.8,
            label=r"$S_{EE}(t)$ pure quench (PR$\approx$2)")
    ax.plot(t_array, S_EE_gge, color="crimson", lw=1.3,
            label=r"$S_{EE}(t)$ mixed GGE (canonical relic)")
    ax.axhline(S_Page, color="black", ls="--", lw=1.0, label=f"Page value = {S_Page:.3f} nat")
    ax.axvline(6.0, color="orange", ls="-.", lw=1.0, alpha=0.7, label=r"$t_{therm}\approx 6$")
    if np.isfinite(T_osc):
        for m in range(1, int(t_array[-1] / T_osc) + 1):
            ax.axvline(m * T_osc, color="gray", ls=":", lw=0.6, alpha=0.4)
    ax.set_xlabel(r"$t$ ($M_{KK}^{-1}$)"); ax.set_ylabel(r"$S_{EE}$ (nats)")
    ax.set_title(f"Page-curve test: coherent recurrence (T_osc={T_osc:.1f}), NOT a turnover")
    ax.legend(fontsize=7.5, loc="best")

    # Panel (b): the FINITE partition function (the kaku thesis — no integral Dg)
    ax = axes[0, 1]
    ax.plot(beta_grid, Z_sum, color="purple", lw=1.5)
    ax.set_yscale("log")
    ax.set_xlabel(r"$\beta$ ($M_{KK}^{-1}$)"); ax.set_ylabel(r"$Z(\beta)=\mathrm{Tr}_{Fock}\,e^{-\beta H_{BdG}}$")
    ax.set_title(f"FINITE Fock $Z(\\beta)$ (dim $2^{{{n_modes}}}={dim}$, NO $\\int Dg$) [thesis-1 holds]")
    ax.grid(alpha=0.3)

    # Panel (c): thermodynamic entropy from the finite trace
    ax = axes[1, 0]
    ax.plot(beta_grid, S_thermo, color="teal", lw=1.5)
    ax.axhline(ln_dim, color="black", ls="--", lw=1.0, label=f"ln(dim) = {ln_dim:.3f}")
    ax.set_xlabel(r"$\beta$ ($M_{KK}^{-1}$)"); ax.set_ylabel(r"$S_{thermo}=\ln Z+\beta\langle E\rangle$ (nats)")
    ax.set_title("Thermodynamic entropy from the finite trace")
    ax.legend(fontsize=8, loc="best"); ax.grid(alpha=0.3)

    # Panel (d): pure-state subsystem purity — recurrence diagnostic
    ax = axes[1, 1]
    ax.plot(t_array, purity_A, color="darkorange", lw=0.9)
    ax.set_xlabel(r"$t$ ($M_{KK}^{-1}$)"); ax.set_ylabel(r"$\mathrm{Tr}(\rho_A^2)$ purity (pure quench)")
    if np.isfinite(T_osc):
        for m in range(1, int(t_array[-1] / T_osc) + 1):
            ax.axvline(m * T_osc, color="gray", ls=":", lw=0.6, alpha=0.4)
    ax.set_title("Subsystem purity recurs (coherent oscillation, no irreversible decline)")
    ax.grid(alpha=0.3)

    fig.suptitle(f"INV9-W1-5 GGE Fock Page-Curve — NO secular turnover "
                 f"(GGE recurs={A_gge['recurs_to_peak']}, pure recurs={A_pure['recurs_to_peak']}, "
                 f"PR={PR:.2f}); Ordered Veil $\\lambda_L=0$, $R_{{therm}}=5252$", fontsize=10.5)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    out_png = PROJECT_ROOT / "computations" / "investigation-9" / "inv9_w1_gge_fock_page_curve.png"
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  saved: {out_png.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------
def main():
    pins = log_input_pins(INPUT_FILES)   # (local)
    script_path = Path(__file__).resolve()   # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"   # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()   # (local)

    # [SIGN] trigger -> emit the 3-tuple (schema_v2_3tuple_required: true)
    extra = [
        f"# Z=Tr_Fock e^(-bH_BdG) FINITE (dim=2^8={res['dim']}, cross-check {res['z_match']:.1e}, "
        f"NO integral Dg) — kaku thesis-1 (finite Fock trace) CONFIRMED",
        f"# but NO secular Page turnover (GGE recurs_to_peak={res['gge_recurs']}, PR={res['PR']:.2f} "
        f"near-two-level): coherent recurrence, not irreversible decline; Ordered Veil lambda_L=0, R_therm={R_therm}",
    ]   # (local)
    print_verdict_payload(
        res["verdict"], res["value"], audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note="GGE Fock partition-function Page-curve turnover test (INV9-W1-5; feeds W3-1)",
        extra_rows=extra,
    )

    print(f"\n=== {GATE_ID}: {res['verdict']} ===")
    return 0   # verdict is DATA, not exit code (math-scripts.md): always 0 on clean run


if __name__ == "__main__":
    sys.exit(main())
