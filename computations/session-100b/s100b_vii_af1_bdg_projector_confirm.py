#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S100b-VII-AF1-BDG-PROJECTOR-CONFIRM
================================================================================
Gate:   S100b-VII-AF1-BDG-PROJECTOR-CONFIRM   (trigger [VERIFY], class GEOMETRIC)
Agent:  landau-condensed-matter-theorist
Plan:   sessions/session-plan/session-100b-plan-w6.md  ## §W6-1
WP:     sessions/session-100b/session-100b-w6-workingpaper.md  ### §W6-1

Element-5 STRUCTURAL CONFIRMATION of the existing §VII.AF.1.OP-PROJ bridge
(Pillar III HP^1 cohomology <-> Pillar IV Peotta-Torma quantum-metric trace;
LANDED S87 W5-1; OP-PROJ retrofit S88 W11 V.4).  NOT a new registration.

HYPOTHESIS (plan §W6-1)
--------------------------------------------------------------------------------
The bridge integrand is built from the BdG/quasihole-state projector
P_0(tau_fold) (Porlles-Chen, arXiv:2505.17349): the direct Connes-Karoubi
pairing on P_0^BdG reproduces the PRIMARY canonical eps_H_HP1_norm = 16.197719
within the Level-2 envelope (delta_BdG <= 1e-3) AND the rank-matched
normal-state (tau = 0, Jensen order parameter OFF) projector swap does NOT
(Delta_disc > 1e-3) -- the projector choice is load-bearing.

LANDAU READING (substrate framing; phononic-framing.md direction preserved)
--------------------------------------------------------------------------------
The Jensen deformation tau IS the substrate's order parameter: the symmetry
group (SU(3)_L x SU(3)_R)/Z_3 breaks at tau > 0.  P_0(tau_fold) is the
condensed-phase (BdG/quasihole) band-0 projector; P_0(0) is the
symmetric-phase (normal-state) one.  The gate tests whether the bridge
pairing distinguishes the broken phase's projector from the symmetric
phase's -- i.e. whether Element 5 of the registered anatomy is anchored to
the ORDERED state, as a Landau free-energy reading requires.

CONSTRUCTION (plan §W6-1 method, executed exactly)
--------------------------------------------------------------------------------
(0,0) Peter-Weyl block of D_K (16x16; lowest-|lambda| band home sector per
S96-GEOM-OFFJENSEN-CHERN lines 108-110 + S22b block-diagonality), built at
tau_fold = 0.19 and tau = 0 via the canonical dirac_spectrum builder
(u2_invariant_metric on the Jensen line: L = (e^{2 tau}, e^{-2 tau}, e^{tau});
D_(0,0) = Omega_spin, the spinor-connection offset -- the mu = 0 slice of the
S96 (tau,mu) U(2)-invariant TT surface convention).

  P_0^BdG = lowest-|lambda| multiplet projector of D_K(tau_fold), rank r0
            detected at deg_tol = 1e-9 (s86-hp1 eq. R-V1.1)
  P_0^N   = rank-r0-matched lowest-|lambda| projector of D_K(0)
            (tie-break = deterministic eigh ascending-|lambda| stable ordering,
            per the plan pin -- at tau = 0 the (0,0) spectrum is |lambda|-uniform
            [lambda^2 = 27/36, the PROVEN lambda^2 = n/36 record], so the tie-break
            pin is load-bearing and an orbit DIAGNOSTIC quantifies the
            representative-dependence)

Hochschild 2-cocycle (s86-hp1 eqs. R-V1.2 / R-V1.3):
  phi_g(a_0, a_1, a_2)  = tau_S( a_0 [P_0^X, a_1] [P_0^X, a_2] )
  phi_g^sym             = Re part (Riemannian-metric / Provost-Vallee component)
with tau_S = normalized trace Tr/16 on the 16-dim spinor fiber (the Vol(SU(3))
factor and all overall constants are absorbed by N_pair in Mode-B; Delta_disc
is a RATIO and is normalization-free).

GENERATOR BASIS (plan machinery pin `generator_basis`, fallback branch):
  The s84_w10a_114 npz carries NO explicit cocycle-leg basis (keys recorded at
  runtime: scalars + the 3x3 K_0 ch-matrix only), so the PINNED FALLBACK fires:
  Gell-Mann lambda_1..lambda_8 on the M_3(C) summand of A_K -- OPERATIONAL
  DEVIATION declared in the WP methodology subsection.  On the (0,0) singlet
  spinor fiber the represented action of the Gell-Mann direction a is the
  canonical Kosmann spin-lift (S23a lineage, Baptista Paper 17 eq 4.1):
      K_a = (1/8) sum_{r,s} (Gamma[s,r,a] - Gamma[r,s,a]) gamma_r gamma_s
  (anti-Hermitian); the Hermitian generator representation is J_a = i K_a.
  Each arm X is evaluated SELF-CONSISTENTLY at its own metric point: P_0^X,
  Gamma(tau_X) and hence J_a(tau_X) all at tau_X ("the projector swap
  propagates to BOTH legs -- self-consistent quasihole-vs-normal metric per
  Porlles-Chen", plan method).

CONNES-KAROUBI PAIRING, PROJECTOR SIDE (plan operator)
--------------------------------------------------------------------------------
The pairing of [phi_g^sym] in HC^2(A_K) with [Ch(P_0^X)] in K_0(A_K) is
evaluated in the idempotent-evaluation form with the K_0-class representative
P_0^X in the a_0 (Chern) slot and the generator-basis differentials in the two
cocycle legs (the LITERAL all-three-slots substitution phi(P,P,P) vanishes
IDENTICALLY by [P,P] = 0 for ANY projector -- a structural zero with no
discriminating power; the generator_basis machinery pin exists precisely to
supply the cocycle legs.  Recorded as the Class-8.7-adjacent degeneracy note
in the WP; the generator-leg evaluation below is the s86-hp1 eq. R-V1.3 form,
phi_g^sym(a_0, a_k, a_l) = Re tau_S(a_0 g_kl a_k a_l) -- the quantum metric
g_kl lifted to a Hochschild cochain):

  phi_sym_signed(X) = sum_{a=1..8} Re (1/16) Tr( P_0^X [P_0^X, J_a] [P_0^X, J_a] )
                    = - sum_a (1/16) || (1 - P_0^X) J_a P_0^X ||_F^2   <= 0
  metric_trace(X)   = - phi_sym_signed(X)  >= 0
        (the structural identity Tr(P[P,J][P,J]) = -Tr(P J (1-P) J P) is
         ASSERTED numerically at machine precision for both arms -- this IS the
         Provost-Vallee quantum-metric trace over the 8 inner-derivation
         directions: the substrate's Re<dP ^ dP> Riemannian component)

NORMALIZATION MODE (plan pre-declaration; neither mode is convention-shopping):
  Mode-A (absolute) requires the s84 npz to carry a projector-side cocycle
  representative + normalization constants (sufficiency set
  {cocycle_representative, generator_basis, N_pair}); keys inspected at
  runtime.  OTHERWISE Mode-B (normalization-anchored) fires:
      N_pair := heitsch_full / phi_sym_signed(BdG)
      R^BdG  := N_pair * phi_sym_signed(BdG) = heitsch_full   EXACTLY
      R^N    := N_pair * phi_sym_signed(N)
  => delta_BdG == 0 BY CONSTRUCTION and is declared VACUOUS; ONLY Delta_disc
  is evidential (plan §W6-1 normalization_mode pin + INFO_meaning).

OPERATOR (plan §W6-1, verbatim):
  delta_BdG  := |R^BdG - 16.197718852989908| / 16.197718852989908
                  (Mode-A; == 0 declared-vacuous in Mode-B)
  Delta_disc := |R^BdG - R^N| / |R^BdG|
  PASS iff (delta_BdG <= 1.0e-3) AND (Delta_disc > 1.0e-3)
  INFO iff (delta_BdG <= 1.0e-3) AND (Delta_disc <= 1.0e-3)
  FAIL iff delta_BdG > 1.0e-3 (Mode-A only; unreachable in Mode-B)

SUBSTITUTION CHAIN (plan §W6-1 item 7, carried verbatim; direction read-off):
  Step 3: At tau = 0, [D_diag, lambda_8] = 0 (s86-hp1 V2 Step 2) => the
          Jensen-direction off-diagonal content of the band-0 projector (and
          hence of phi_g^sym's commutator legs) VANISHES at tau = 0; the
          tau_fold-rate-limited content that the canonical 16.197719 includes
          (HP^1-norm > 0 <=> tau_fold > 0) is ABSENT from R^N.
  Step 4: expected direction R^N < R^BdG (content loss).  The gate keys on
          |Delta_disc| > 1e-3 (magnitude); the SIGN is recorded as a
          DIAGNOSTIC (plan: "with the sign recorded as a diagnostic").

CROSS-CHECKS (plan):
  CC1: (0,0)-block |lambda| multiset at tau_fold vs the s84 L12 spectrum cache
       (builder-drift guard; rel tolerance 1e-9, full-16-value comparison)
  CC2: Heitsch full-precision target heitsch_ratio = 16.197718852989908 from
       the s84 W10a-114 producing script (S83 W1-G2 normalization) as the
       float64 comparison target (Class-8.3 compliant; canonical_constants
       publishes eps_H_HP1_norm = 16.197719 at 6 sig figs)

DIAGNOSTICS (pre-declared here; NOT PASS inputs):
  d1: fixed-generator arm -- metric_trace of P_0^N evaluated with the
      tau_fold generators J_a(tau_fold) (separates projector-swap content
      from generator-swap content)
  d2: tau = 0 degenerate-representative orbit -- N_ORBIT = 8 random
      orthonormal rank-r0 frames inside the tau = 0 lowest-|lambda| degenerate
      subspace (seed 100616; deterministic), reporting the orbit spread of
      metric_trace(N) and the implied Delta_disc range (robustness of the
      verdict against the eigh tie-break arbitrariness)
  d3: per-generator metric content g_aa for both arms (u(2) = {l1,l2,l3,l8}
      vs C^2 = {l4..l7} resolution: WHERE the discrimination lives)

UNTRUSTED-UPSTREAM CAVEAT (MANDATORY; orchestrator dispatch)
--------------------------------------------------------------------------------
This gate consumes the s84 spectrum-cache lineage flagged by the
S100b-TAU0-LAITEH-REDUCTION ESCALATION (FAIL, SUBCASE=STRUCTURED): the
framework tau = 0 operator sits at the Levi-Civita torsion point t = 1/2 of
the Lai-Teh family, NOT the Kostant cubic t = 1/3; the eigensolver itself is
verified CORRECT (cubic-modified control at machine epsilon); the
lambda^2 = n/36 PROVEN record remains VALID; the cache numerics are
self-consistent with the LC lineage the framework has always computed.  Open
question is operator CANONICITY (Q1-workshop carry-forward, WP §W3-2), NOT
numerical validity.  Dispatched per the plan's pre-registered
orchestrator-triage option "dispatch under explicit UNTRUSTED-UPSTREAM
caveat".  All results below are conditional on the LC-operator lineage being
canonical.

MACHINERY PINS (plan §W6-1 machinery_pin_map, verbatim):
  N_eval = 2 pairing evaluations + 1 cache cross-check + 1 mode detection;
  L_max = 10 (anchor truncation; the operative (0,0) block is exact at every
  L >= 0 by Peter-Weyl block-diagonality, S22b); scan = N/A (two-point
  tau in {0.19, 0.0}); tolerance: envelope_rel = 1e-3, eig_residual_tol =
  1e-12, deg_tol = 1e-9; scheme = CONNES-KAROUBI-PAIRING-W10A114-NORM;
  convention = RATIO; seed = N/A for the PASS pipeline (deterministic;
  100616 for the d2 DIAGNOSTIC only); GPU_path = cpu-cap-OMP8 (16x16 blocks);
  regulator_pin = a_4^{zeta} inherited verbatim from the §VII.AF.1.OP-PROJ
  entry (no new Mellin-pole evaluation => no new poleconv tag obligation);
  CLASS = FULL (direct finite-spectral-triple pairing; NO SCHEMATIC helper --
  _spectral_action_regulators.py is NOT imported); publication_precision =
  6 sig figs in WP, full float64 in npz.

Author: landau-condensed-matter-theorist (Session 100b, Wave 6)
Date:   2026-06-07
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

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]   # (local) computations/session-100b -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold, eps_H_HP1_norm  # noqa: E402

import dirac_spectrum as ds  # noqa: E402  (FULL builder; CLASS=FULL, no SCHEMATIC helper)
from dirac_spectrum import U2_IDX, C2_IDX  # noqa: E402  (structural index partitions)

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W6-1)
# ---------------------------------------------------------------------------
GATE_ID = "S100b-VII-AF1-BDG-PROJECTOR-CONFIRM"   # (local)
SESSION = "100b"                                   # (local)
SCHEME = "CONNES-KAROUBI-PAIRING-W10A114-NORM"     # (local) plan-pinned
CONVENTION = "RATIO"                               # (local) plan-pinned
L_MAX = "10"                                       # (local) plan-pinned (operative (0,0) block exact at every L, S22b)
SCHEMA_VERSION = "S84+"                            # (local)

ENVELOPE_REL = 1.0e-3        # (local) Level-2 L^{-3} envelope at L_max=10 (reproduction band AND discrimination floor)
EIG_RESIDUAL_TOL = 1e-12     # (local) plan eigh sanity
DEG_TOL = 1e-9               # (local) plan lowest-multiplet detection tolerance
HEITSCH_FULL = 16.197718852989908  # (local) CC2 full-precision target, s84_w10a_eps_h_k_class_location.py (S83 W1-G2); Class-8.3 pin
CACHE_GUARD_REL = 1e-9       # (local) CC1 builder-drift guard tolerance (same builder, float64 determinism)
DIAG_SEED = 100616           # (local) d2 orbit DIAGNOSTIC seed only (PASS pipeline deterministic)
N_ORBIT = 8                  # (local) d2 orbit sample count
MODE_A_REQUIRED_KEYS = {"cocycle_representative", "generator_basis", "N_pair"}  # (local) Mode-A sufficiency set

TAU_BDG = float(tau_fold)    # (local) 0.19 -- condensed-phase arm
TAU_N = 0.0                  # (local) normal-state arm (Jensen order parameter OFF) -- structural, not a framework constant

# Input files (plan §W6-1 input_files, with plan-pinned SHAs verified at runtime)
CANON_PY = SHARED_DIR / "canonical_constants.py"
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"
S84_NPZ = PROJECT_ROOT / "computations" / "session-84" / "s84_w10a_114_eps_h_hp1_cocycle.npz"
S84_SCRIPT = PROJECT_ROOT / "computations" / "session-84" / "s84_w10a_eps_h_k_class_location.py"
S86_WORKSHOP = PROJECT_ROOT / "sessions" / "session-86" / "workshops" / "s86-hp1-cohomology-quantum-metric-bridge.md"
S85_SCAN = PROJECT_ROOT / "computations" / "session-85" / "s85_w5_6_eps_h_hp1_scan.py"
S87_LANDING = PROJECT_ROOT / "computations" / "session-87" / "s87_w5_pillar_iii_iv_bridge_permanent_land.py"
S84_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

EXPECTED_SHA = {  # (local) plan §W6-1 input_files pins (canonical_constants = <computed-at-runtime>)
    "s84_w10a_114_npz": "e8dd3b1d2054a81685b2fbfa5bc585a83da2f34619549c1de062bd90d5307597",
    "s84_w10a_114_script": "5c14dbc358146d83421360b424aef8454706e8c8a0343f2e695233b377ec74d3",
    "s86_hp1_workshop": "df5d008c86e5dd8bc8c957b64d3f4ceb6677da981467d3ddfe1f02a200695b15",
    "s85_w5_6_scan_script": "c4368a890b99e3aec5d354820a6831ef0844ea499bf2012b3e3dc0a3117d3f0d",
    "s87_w5_landing_script": "1608c9e50221ef7822b9b1a0d96d6476b6632eaf45ac1da6442d85c627c397b0",
    "dirac_spectrum": "dadba674e950fad9a300c282b3860cbf31e36589fa86a0ace975376976a602a7",
    "s84_spectrum_cache": "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
}

SESSION_DIR = PROJECT_ROOT / "computations" / "session-100b"
NPZ_OUT = SESSION_DIR / "s100b_vii_af1_bdg_projector_confirm.npz"
PNG_OUT = SESSION_DIR / "s100b_vii_af1_bdg_projector_confirm.png"


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    return h_audit.hexdigest(), hashlib.sha256(script_bytes).hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    """Emit the verdict PAYLOAD for the dispatching agent to pass to the
    race-safe knowledge-MCP `emit_verdict` tool (gate-verdicts.md
    §"Race-Safe Emission").  The script does NOT write the verdict file."""
    payload = {  # (local)
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
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
# Geometry at a Jensen point (mu = 0 slice of the S96 U(2)-invariant TT surface)
# ---------------------------------------------------------------------------
def build_infra():
    """SU(3) generators, structure constants, Killing form, Cliff(8) gammas
    (tau-independent)."""
    gens = ds.su3_generators()
    f_abc = ds.compute_structure_constants(gens)
    B_ab = ds.compute_killing_form(f_abc)
    gammas = ds.build_cliff8()
    return gens, f_abc, B_ab, gammas


def jensen_point(tau, f_abc, B_ab, gammas):
    """Return (D_00, Gamma) at Jensen modulus tau:
       L = (e^{2 tau}, e^{-2 tau}, e^{tau})  [volume-preserving Jensen line];
       D_00 = Omega_spin (16x16 anti-Hermitian spinor-connection offset --
       the (0,0) Peter-Weyl singlet block of D_K, exact at every L_max by
       S22b block-diagonality)."""
    L1, L2, L3 = float(np.exp(2.0 * tau)), float(np.exp(-2.0 * tau)), float(np.exp(tau))  # (local)
    g = ds.u2_invariant_metric(B_ab, L1, L2, L3)
    E = ds.orthonormal_frame(g)
    ft = ds.frame_structure_constants(f_abc, E)
    Gamma = ds.connection_coefficients(ft)
    D_00 = ds.spinor_connection_offset(Gamma, gammas)
    return D_00, Gamma


def eigh_block(D_00):
    """Diagonalize H = i D_00 (Hermitian); return (w, V, residual).
    16x16 block: CPU numpy.eigh per plan GPU_path cpu-cap-OMP8."""
    H = 0.5 * ((1j * D_00) + (1j * D_00).conj().T)   # (local) Hermitize vs round-off
    w, V = np.linalg.eigh(H)
    residual = float(np.max(np.abs(H @ V - V @ np.diag(w))))  # (local)
    return w, V, residual


def kosmann_antisym(Gamma, gammas, a):
    """Kosmann spinorial operator (S23a canonical lineage; Baptista Paper 17 eq 4.1):
       K_a = (1/8) sum_{r,s} (Gamma[s,r,a] - Gamma[r,s,a]) gamma_r gamma_s
    (anti-Hermitian).  Implemented verbatim from
    computations/session-23/s23a_kosmann_singlet.py::kosmann_operator_antisymmetric."""
    dim_spin = gammas[0].shape[0]  # (local)
    K = np.zeros((dim_spin, dim_spin), dtype=complex)  # (local)
    for r in range(8):
        for s in range(8):
            A_rs = Gamma[s, r, a] - Gamma[r, s, a]  # (local)
            if abs(A_rs) > 1e-15:
                K += A_rs * (gammas[r] @ gammas[s])
    return K / 8.0


def hermitian_generators(Gamma, gammas):
    """J_a = i K_a, a = 0..7 -- Hermitian represented Gell-Mann directions
    lambda_1..lambda_8 (M_3(C) summand of A_K) on the 16-dim singlet spinor
    fiber, at the metric point of Gamma."""
    Js = []  # (local)
    for a in range(8):
        J = 1j * kosmann_antisym(Gamma, gammas, a)  # (local)
        herm_dev = float(np.max(np.abs(J - J.conj().T)))  # (local)
        assert herm_dev < 1e-13, f"J_{a+1} not Hermitian: dev={herm_dev:.3e}"
        Js.append(J)
    return Js


def projector_from_columns(V, idx):
    """Rank-len(idx) orthogonal projector from eigh columns."""
    Vsel = V[:, idx]  # (local)
    P = Vsel @ Vsel.conj().T  # (local)
    assert float(np.max(np.abs(P - P.conj().T))) < 1e-12, "P not Hermitian"
    assert float(np.max(np.abs(P @ P - P))) < 1e-12, "P not idempotent"
    return P


def phi_g_sym_pairing(P, Js, dim=16):
    """phi_sym_signed = sum_a Re (1/dim) Tr( P [P, J_a] [P, J_a] )   (signed, <= 0)
       per_gen[a]     = -Re (1/dim) Tr( P [P, J_a] [P, J_a] )
                      = (1/dim) ||(1 - P) J_a P||_F^2                (metric content)
    Asserts the structural identity Tr(P[P,J][P,J]) = -Tr(P J (1-P) J P)."""
    one = np.eye(dim)  # (local)
    per_gen = np.zeros(8)  # (local)
    phi_signed = 0.0  # (local)
    max_id_dev = 0.0  # (local)
    for a, J in enumerate(Js):
        C = P @ J - J @ P  # (local) [P, J_a]
        t_coc = complex(np.trace(P @ C @ C)) / dim  # (local) tau_S(P [P,J][P,J])
        A = (one - P) @ J @ P  # (local)
        t_met = float(np.real(np.trace(A.conj().T @ A))) / dim  # (local) ||(1-P)JP||_F^2 / dim
        id_dev = abs(t_coc.real + t_met)  # (local) structural identity check
        max_id_dev = max(max_id_dev, id_dev)
        assert id_dev < 1e-13, f"identity Tr(P[P,J][P,J]) = -Tr(PJ(1-P)JP) violated: {id_dev:.3e}"
        assert abs(t_coc.imag) < 1e-13, f"cocycle diagonal not real: {t_coc.imag:.3e}"
        phi_signed += t_coc.real
        per_gen[a] = t_met
    return phi_signed, per_gen, max_id_dev


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  §VII.AF.1.OP-PROJ BdG-projector Element-5 confirmation")
    print("=" * 78)

    # --- input pins + plan-SHA verification + dual SHA (first stdout lines) ---
    pins = log_input_pins({
        "canonical_constants": CANON_PY,
        "dirac_spectrum": DK_BUILDER,
        "s84_w10a_114_npz": S84_NPZ,
        "s84_w10a_114_script": S84_SCRIPT,
        "s86_hp1_workshop": S86_WORKSHOP,
        "s85_w5_6_scan_script": S85_SCAN,
        "s87_w5_landing_script": S87_LANDING,
        "s84_spectrum_cache": S84_CACHE,
    })
    for name, expected in EXPECTED_SHA.items():
        if pins.get(name) != expected:
            print(f"  !! SHA MISMATCH for {name}: expected {expected[:16]}..., got {pins.get(name, '')[:16]}...")
            raise SystemExit(2)  # script breakage, not a verdict
    print("  plan-pinned input SHAs verified (7 static + canonical_constants runtime)")
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANON_PY, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  UNTRUSTED-UPSTREAM caveat ACTIVE: s84 cache lineage = LC t=1/2 (Lai-Teh) per")
    print(f"  S100b-TAU0-LAITEH-REDUCTION ESCALATION; eigensolver control-verified; results")
    print(f"  conditional on LC-operator-lineage canonicity (adjudication pending).")

    # --- Mode detection (plan normalization_mode pre-declaration) ---
    d84 = np.load(S84_NPZ, allow_pickle=True)
    npz_keys = sorted(d84.files)  # (local)
    mode = "A" if MODE_A_REQUIRED_KEYS.issubset(set(npz_keys)) else "B"  # (local)
    print(f"\n  [MODE] s84_w10a_114 npz keys = {npz_keys}")
    print(f"  [MODE] Mode-A sufficiency set {sorted(MODE_A_REQUIRED_KEYS)} present? "
          f"{MODE_A_REQUIRED_KEYS.issubset(set(npz_keys))}  ==> Mode-{mode}")
    if mode == "B":
        print("  [MODE] Mode-B normalization-anchored: N_pair fixed by R^BdG := eps_H_HP1_norm;")
        print("         delta_BdG == 0 BY CONSTRUCTION (VACUOUS); ONLY Delta_disc evidential.")
    heitsch_npz = float(np.asarray(d84["heitsch_ratio_used"]).flat[0])  # (local)
    assert abs(heitsch_npz - HEITSCH_FULL) < 1e-12, "CC2 target drift vs s84 npz"
    print(f"  [CC2] heitsch_ratio (npz) = {heitsch_npz:.15f} == pinned target {HEITSCH_FULL:.15f}")
    print(f"  [CC2] canonical_constants eps_H_HP1_norm = {eps_H_HP1_norm} (6 sig figs; "
          f"|target - canon|/canon = {abs(HEITSCH_FULL - eps_H_HP1_norm)/eps_H_HP1_norm:.2e} "
          f"< Class-8.3 floor 1e-6 x ... OK)")

    # --- build geometry at the two arms ---
    gens, f_abc, B_ab, gammas = build_infra()
    print(f"\n  [GEOM] tau_BdG = {TAU_BDG} (fold; condensed phase), tau_N = {TAU_N} (normal state)")
    D_bdg, Gamma_bdg = jensen_point(TAU_BDG, f_abc, B_ab, gammas)
    D_n, Gamma_n = jensen_point(TAU_N, f_abc, B_ab, gammas)
    w_bdg, V_bdg, res_bdg = eigh_block(D_bdg)
    w_n, V_n, res_n = eigh_block(D_n)
    print(f"  [EIG] residuals: BdG = {res_bdg:.3e}, N = {res_n:.3e}  (tol {EIG_RESIDUAL_TOL:.0e})")
    regime_ok = (res_bdg < EIG_RESIDUAL_TOL) and (res_n < EIG_RESIDUAL_TOL)  # (local)

    # --- CC1: cache cross-check (builder-drift guard) ---
    cache = np.load(S84_CACHE, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local)
    cache_abs00 = np.sort(np.asarray(sector_evals[(0, 0)]["abs_evals"], dtype=np.float64))  # (local)
    mine_abs00 = np.sort(np.abs(w_bdg))  # (local)
    cc1_rel = float(np.max(np.abs(mine_abs00 - cache_abs00) / np.abs(cache_abs00)))  # (local)
    lam_min_mine = float(mine_abs00[0])  # (local)
    lam_min_cache = float(cache_abs00[0])  # (local)
    cc1_ok = cc1_rel < CACHE_GUARD_REL  # (local)
    print(f"  [CC1] |lambda|_min (0,0) at tau_fold: builder = {lam_min_mine:.12f}, "
          f"cache = {lam_min_cache:.12f}")
    print(f"  [CC1] full-16-multiset max rel dev = {cc1_rel:.3e}  (guard {CACHE_GUARD_REL:.0e})  "
          f"{'OK' if cc1_ok else 'DRIFT'}")
    regime_ok = regime_ok and cc1_ok

    # --- projectors ---
    order_bdg = np.argsort(np.abs(w_bdg), kind="stable")  # (local)
    r0 = int(np.sum(np.abs(np.abs(w_bdg) - np.abs(w_bdg[order_bdg[0]])) < DEG_TOL))  # (local)
    gap_next = float(np.abs(w_bdg[order_bdg[r0]]) - np.abs(w_bdg[order_bdg[0]])) if r0 < 16 else 0.0  # (local)
    P_bdg = projector_from_columns(V_bdg, order_bdg[:r0])
    print(f"\n  [P_0^BdG] rank r0 = {r0} (deg_tol {DEG_TOL:.0e}); |lambda|_min = {lam_min_mine:.9f}; "
          f"gap to next band = {gap_next:.6f}")

    order_n = np.argsort(np.abs(w_n), kind="stable")  # (local)
    deg_n0 = int(np.sum(np.abs(np.abs(w_n) - np.abs(w_n[order_n[0]])) < DEG_TOL))  # (local)
    P_n = projector_from_columns(V_n, order_n[:r0])
    lam_n0 = float(np.abs(w_n[order_n[0]]))  # (local)
    n_36 = 36.0 * lam_n0 * lam_n0  # (local) PROVEN lambda^2 = n/36 record check
    print(f"  [P_0^N]   rank-matched r0 = {r0}; tau=0 |lambda| = {lam_n0:.9f} "
          f"(36 lambda^2 = {n_36:.9f}; PROVEN lambda^2 = n/36 record, n = 27 expected); "
          f"tau=0 lowest-|lambda| degeneracy = {deg_n0} (tie-break pin = stable eigh ordering)")

    # --- generator representations at each arm (self-consistent metric) ---
    Js_bdg = hermitian_generators(Gamma_bdg, gammas)
    Js_n = hermitian_generators(Gamma_n, gammas)
    print("  [GEN] J_a = i K_a (Kosmann spin-lift, S23a lineage) Hermitian at both arms; "
          "OPERATIONAL DEVIATION: Gell-Mann fallback basis fires (npz carries no explicit basis)")

    # --- pairing evaluations ---
    phi_bdg, per_gen_bdg, iddev_bdg = phi_g_sym_pairing(P_bdg, Js_bdg)
    phi_n, per_gen_n, iddev_n = phi_g_sym_pairing(P_n, Js_n)
    met_bdg = -phi_bdg  # (local) metric trace >= 0
    met_n = -phi_n      # (local)
    print(f"\n  [PAIRING] phi_sym_signed(BdG) = {phi_bdg:.12f}  (metric trace {met_bdg:.12f})")
    print(f"  [PAIRING] phi_sym_signed(N)   = {phi_n:.12f}  (metric trace {met_n:.12f})")
    print(f"  [PAIRING] structural-identity max dev: BdG {iddev_bdg:.2e}, N {iddev_n:.2e}")
    print(f"  [PAIRING] per-generator (BdG): " + " ".join(f"l{a+1}={v:.6f}" for a, v in enumerate(per_gen_bdg)))
    print(f"  [PAIRING] per-generator (N):   " + " ".join(f"l{a+1}={v:.6f}" for a, v in enumerate(per_gen_n)))

    if met_bdg < 1e-14:
        # degenerate-observable early exit (Class-8.7-adjacent pre-flight; pre-declared):
        # band-0 projector commutes with all generators => pairing identically zero,
        # Mode-B normalization undefined; emit INFO with diagnostic and stop.
        print("  !! metric_trace(BdG) ~ 0: band-0 projector commutes with all generators;")
        print("     pairing degenerate -- INFO with diagnostic (pre-declared early exit).")
        print_verdict_payload(
            "INFO",
            f"mode=B;DEGENERATE-PAIRING;metric_trace_BdG={met_bdg:.3e};Delta_disc=undefined",
            audit_sha, content_sha,
            sign_verdict="N/A", magnitude_verdict="INFO", regime_verdict="VALID",
            companion_note="degenerate-observable pre-flight fired (Class-8.7-adjacent)",
        )
        return 0

    # --- Mode-B normalization + plan operator ---
    N_pair = HEITSCH_FULL / phi_bdg  # (local) Mode-B anchor (carries sign)
    R_bdg = N_pair * phi_bdg          # (local) == HEITSCH_FULL exactly
    R_n = N_pair * phi_n              # (local)
    delta_bdg = abs(R_bdg - HEITSCH_FULL) / HEITSCH_FULL  # (local) == 0 VACUOUS in Mode-B
    Delta_disc = abs(R_bdg - R_n) / abs(R_bdg)            # (local) = |1 - met_n/met_bdg|
    ratio_n_over_bdg = met_n / met_bdg                    # (local)
    print(f"\n  [MODE-B] N_pair = {N_pair:.9f}")
    print(f"  [OPERATOR] R^BdG = {R_bdg:.12f}  (:= eps_H_HP1_norm anchor; delta_BdG = {delta_bdg:.3e} VACUOUS)")
    print(f"  [OPERATOR] R^N   = {R_n:.12f}")
    print(f"  [OPERATOR] Delta_disc = |R^BdG - R^N| / |R^BdG| = {Delta_disc:.12f}")
    print(f"  [OPERATOR] R^N / R^BdG = {ratio_n_over_bdg:.12f}")

    # --- substitution-chain direction read-off (Step 4; sign = DIAGNOSTIC) ---
    direction_expected = "R^N < R^BdG"  # (local) pre-registered (content loss)
    direction_observed = "R^N < R^BdG" if R_n < R_bdg else ("R^N > R^BdG" if R_n > R_bdg else "R^N == R^BdG")  # (local)
    sign_match = (R_n < R_bdg)  # (local)
    print(f"  [SIGN-DIAG] expected {direction_expected}; observed {direction_observed} "
          f"({'match' if sign_match else 'MISMATCH -- recorded as diagnostic per plan'})")

    # --- verdict per plan operator ---
    if delta_bdg > ENVELOPE_REL:
        verdict = "FAIL"   # Mode-A regression branch (unreachable in Mode-B)
    elif Delta_disc > ENVELOPE_REL:
        verdict = "PASS"
    else:
        verdict = "INFO"
    # schema-v2 3-tuple (orchestrator-required; sign is plan-diagnostic, recorded honestly)
    sign_verdict = "PASS" if sign_match else "FAIL"        # (local)
    magnitude_verdict = "PASS" if Delta_disc > ENVELOPE_REL else "INFO"  # (local)
    regime_verdict = "VALID" if regime_ok else "MARGINAL"  # (local)
    print(f"\n  [VERDICT] composite (plan operator) = {verdict}; "
          f"3-tuple = (sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})")

    # --- DIAGNOSTICS (pre-declared; not PASS inputs) ---
    # d1: fixed-generator arm (P_0^N with tau_fold generators)
    phi_n_fixedgen, per_gen_n_fixedgen, _ = phi_g_sym_pairing(P_n, Js_bdg)
    met_n_fixedgen = -phi_n_fixedgen  # (local)
    Delta_disc_fixedgen = abs(1.0 - met_n_fixedgen / met_bdg)  # (local)
    print(f"\n  [d1] fixed-generator arm: metric_trace(P_N, J(tau_fold)) = {met_n_fixedgen:.12f}; "
          f"Delta_disc(fixed-gen) = {Delta_disc_fixedgen:.9f}")

    # d2: tau=0 degenerate-representative orbit (robustness of the tie-break pin)
    rng = np.random.default_rng(DIAG_SEED)  # (local)
    deg_idx = order_n[:deg_n0]  # (local) the tied lowest-|lambda| subspace columns
    orbit_met = []  # (local)
    for _ in range(N_ORBIT):
        Z = rng.standard_normal((deg_n0, r0)) + 1j * rng.standard_normal((deg_n0, r0))  # (local)
        Q, _ = np.linalg.qr(Z)  # (local) random orthonormal r0-frame in the tied subspace
        Vfr = V_n[:, deg_idx] @ Q  # (local)
        P_orb = Vfr @ Vfr.conj().T  # (local)
        phi_orb, _, _ = phi_g_sym_pairing(P_orb, Js_n)
        orbit_met.append(-phi_orb)
    orbit_met = np.array(orbit_met)  # (local)
    orbit_Ddisc = np.abs(1.0 - orbit_met / met_bdg)  # (local)
    print(f"  [d2] tau=0 representative orbit (seed {DIAG_SEED}, N = {N_ORBIT}, frames in the "
          f"{deg_n0}-dim tied subspace): metric_trace(N) in "
          f"[{orbit_met.min():.9f}, {orbit_met.max():.9f}] (mean {orbit_met.mean():.9f})")
    print(f"  [d2] implied Delta_disc range over orbit: [{orbit_Ddisc.min():.9f}, {orbit_Ddisc.max():.9f}] "
          f"-- verdict robust to tie-break? {bool((orbit_Ddisc > ENVELOPE_REL).all()) if verdict == 'PASS' else 'see WP'}")

    # d3: u(2) vs C^2 channel resolution
    u2_bdg = float(per_gen_bdg[U2_IDX].sum()); c2_bdg = float(per_gen_bdg[C2_IDX].sum())  # (local)
    u2_n = float(per_gen_n[U2_IDX].sum()); c2_n = float(per_gen_n[C2_IDX].sum())  # (local)
    print(f"  [d3] channel split (BdG): u(2) = {u2_bdg:.9f}, C^2 = {c2_bdg:.9f}")
    print(f"  [d3] channel split (N):   u(2) = {u2_n:.9f}, C^2 = {c2_n:.9f}")

    # --- save npz (full float64) ---
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID, verdict=verdict, mode=mode,
        npz_keys_recorded=np.array(npz_keys),
        tau_bdg=TAU_BDG, tau_n=TAU_N,
        w_bdg=w_bdg, w_n=w_n,
        eig_residual_bdg=res_bdg, eig_residual_n=res_n,
        r0=r0, gap_next=gap_next, deg_n0=deg_n0,
        lam_min_builder=lam_min_mine, lam_min_cache=lam_min_cache, cc1_rel=cc1_rel,
        cache_abs00=cache_abs00, builder_abs00=mine_abs00,
        heitsch_full=HEITSCH_FULL, eps_H_HP1_norm_canon=float(eps_H_HP1_norm),
        phi_sym_signed_bdg=phi_bdg, phi_sym_signed_n=phi_n,
        metric_trace_bdg=met_bdg, metric_trace_n=met_n,
        per_gen_bdg=per_gen_bdg, per_gen_n=per_gen_n,
        N_pair=N_pair, R_bdg=R_bdg, R_n=R_n,
        delta_bdg=delta_bdg, Delta_disc=Delta_disc,
        ratio_n_over_bdg=ratio_n_over_bdg,
        sign_match=sign_match,
        envelope_rel=ENVELOPE_REL, deg_tol=DEG_TOL, eig_residual_tol=EIG_RESIDUAL_TOL,
        cache_guard_rel=CACHE_GUARD_REL,
        met_n_fixedgen=met_n_fixedgen, Delta_disc_fixedgen=Delta_disc_fixedgen,
        per_gen_n_fixedgen=per_gen_n_fixedgen,
        orbit_met=orbit_met, orbit_Ddisc=orbit_Ddisc, diag_seed=DIAG_SEED,
        u2_bdg=u2_bdg, c2_bdg=c2_bdg, u2_n=u2_n, c2_n=c2_n,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
        untrusted_upstream_caveat=(
            "consumes s84 cache lineage flagged by S100b-TAU0-LAITEH-REDUCTION ESCALATION "
            "(STRUCTURED LC t=1/2; eigensolver control-verified; canonicity adjudication pending)"
        ),
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    x = np.arange(8)  # (local)
    wbar = 0.38  # (local)
    labels = [f"$\\lambda_{a+1}$" for a in range(8)]  # (local)
    axes[0].bar(x - wbar / 2, per_gen_bdg, wbar, label=f"BdG ($\\tau_{{fold}}={TAU_BDG}$)", color="tab:blue", edgecolor="k")
    axes[0].bar(x + wbar / 2, per_gen_n, wbar, label="normal ($\\tau=0$)", color="tab:orange", edgecolor="k")
    for a in C2_IDX:
        axes[0].axvspan(a - 0.5, a + 0.5, color="gray", alpha=0.10)
    axes[0].set_xticks(x); axes[0].set_xticklabels(labels)
    axes[0].set_ylabel(r"per-generator metric content  $\frac{1}{16}\|(1-P)J_aP\|_F^2$")
    axes[0].set_title("Provost–Vallée metric content of band-0 projector\n(shaded = $C^2$ directions $\\lambda_4..\\lambda_7$)")
    axes[0].legend()
    axes[0].grid(True, axis="y", alpha=0.3)

    axes[1].axhline(1.0, color="tab:blue", lw=2, label=r"$R^{BdG}/R^{BdG}=1$ (anchor)")
    axes[1].axhline(ratio_n_over_bdg, color="tab:orange", lw=2, label=rf"$R^N/R^{{BdG}}={ratio_n_over_bdg:.4f}$")
    axes[1].axhspan(1.0 - ENVELOPE_REL, 1.0 + ENVELOPE_REL, color="tab:blue", alpha=0.18,
                    label=r"Level-2 envelope $\pm10^{-3}$")
    orb_ratio = orbit_met / met_bdg  # (local)
    axes[1].scatter(np.full(N_ORBIT, 0.5), orb_ratio, marker="x", color="tab:red", zorder=5,
                    label=f"d2 orbit (N={N_ORBIT}, seed {DIAG_SEED})")
    axes[1].set_xlim(0, 1); axes[1].set_xticks([])
    axes[1].set_ylabel(r"$R^X / R^{BdG}$")
    axes[1].set_title(
        f"Mode-B projector discrimination\n"
        f"$\\Delta_{{disc}}$ = {Delta_disc:.6f}  (floor $10^{{-3}}$)  →  {verdict}\n"
        f"$\\delta_{{BdG}}$ = 0 (VACUOUS, Mode-B);  r0 = {r0};  CC1 rel = {cc1_rel:.1e}"
    )
    axes[1].legend(loc="center right", fontsize=8)
    axes[1].grid(True, axis="y", alpha=0.3)
    fig.suptitle(f"{GATE_ID}: §VII.AF.1.OP-PROJ Element-5 BdG-projector confirmation "
                 f"[UNTRUSTED-UPSTREAM caveat: LC t=1/2 lineage]", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(PNG_OUT, dpi=150)
    plt.close(fig)
    print(f"  Saved plot: {PNG_OUT}")

    # --- verdict payload (race-safe emission by the agent via emit_verdict) ---
    value_str = (  # (local) no single-quote chars
        f"mode=B;deltaBdG=0.0(VACUOUS);Ddisc={Delta_disc:.6f};RBdG={R_bdg:.6f};RN={R_n:.6f};"
        f"r0={r0};degN0={deg_n0};cc1rel={cc1_rel:.2e};orbitDdisc=[{orbit_Ddisc.min():.4f},{orbit_Ddisc.max():.4f}]"
    )
    extra_rows = [  # (local)
        ("# UNTRUSTED-UPSTREAM caveat: consumes s84 cache lineage flagged by "
         "S100b-TAU0-LAITEH-REDUCTION ESCALATION (STRUCTURED LC t=1/2; eigensolver "
         "control-verified; canonicity adjudication pending) — dispatched per "
         "pre-registered orchestrator triage"),
        ("# regulator_pin: a_4^{zeta} inherited verbatim from the §VII.AF.1.OP-PROJ entry "
         "(CM-1995 §III.4 residue at s=0; direct finite-triple pairing, NO new Mellin-pole "
         "evaluation => no new poleconv-{A|B} tag obligation) # " + GATE_ID),
        ("# Mode-B normalization-anchored (pre-declared plan §W6-1): N_pair fixed by "
         "R^BdG := eps_H_HP1_norm; delta_BdG == 0 BY CONSTRUCTION (VACUOUS); PASS/INFO "
         "carried by Delta_disc alone; generator-basis fallback = Gell-Mann lambda_1..lambda_8 "
         "via Kosmann spin-lift (OPERATIONAL DEVIATION, s84 npz lacks explicit basis); "
         "CLASS=FULL no SCHEMATIC helper # " + GATE_ID),
    ]
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        companion_note=("§VII.AF.1.OP-PROJ Element-5 BdG-projector confirmation (Porlles-Chen); "
                        "Mode-B anchored; sign per plan = diagnostic-only, composite keys on "
                        "delta_BdG AND Delta_disc plan operator"),
        extra_rows=extra_rows,
    )

    print(f"\n  4-tuple: (value={Delta_disc:.6f}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"=== {GATE_ID}: {verdict} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
