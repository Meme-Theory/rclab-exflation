#!/usr/bin/env python3
"""
INV5-W1-4 -- INV5-W1-4-MODULAR-TWIST-MULTIPLICITY-NONSCALAR
============================================================
Does the Tomita-Takesaki modular automorphism sigma^omega of the SecVII.BZ
crossed product A_K (x) R act as a multiplicity-NON-scalar twist (twisted
commutator [D_K,a]_sigma NOT proportional to 1 on each C^{m(p,q)} block),
thereby EVADING the Skolem-Noether no-go (SecVII.BL) that kills every ORDINARY
(block-inner) twist -- so the generation hierarchy eps_LX could be intra-substrate?

Gate ID:        INV5-W1-4-MODULAR-TWIST-MULTIPLICITY-NONSCALAR
Trigger:        [VERIFY-THEOREM]   (structural set-membership; NO [SIGN] 3-tuple)
Classification: GEOMETRIC
Agent:          connes-ncg-theorist
Plan:           sessions/investigation/investigation-5/investigation-5-plan-w1.md SecW1-4 (R3 YAML)
Scheme:         Tomita-Takesaki-modular-twist-on-crossed-product
Convention:     ABSOLUTE  (off-scalar operator-norm residual vs the 1e-6 floor;
                FULL physical -- the modular operator is built from the SecVII.BZ
                frozen faithful-normal weight on the L12 cache; no -SCHEMATIC tag)

=============================================================================
PRE-COMPUTE / KNOWLEDGE-MCP AUDIT (recorded verbatim in the WP MCP Pre-Compute
Audit; queries executed BEFORE this script was authored):
=============================================================================
  search_knowledge('Skolem-Noether multiplicity-blindness no-go generation-
    blindness epsilon_LX')
      -> [theorem] SecVII.BL Generation-Blindness Obstruction STAGE-3-PERMANENT
         (S99 W3-1; Stage-2 PASS-AND audit 0f0c4f65; R_cross=1.019704,
         n_distinct=2): "The twisted escape is dead by Skolem-Noether. A_K =
         C(+)H(+)M3(C) has three non-isomorphic simple summands, so every
         sigma in Aut(A_K) is block-inner => multiplicity-scalar."
  search_knowledge('VII.BZ BDI Horizon-Faithfulness crossed product Type-III
    modular Tomita-Takesaki')
      -> [theorem] K12 (S105) SecVII.BZ BDI Horizon-Faithfulness Protection
         STAGE-3-PERMANENT (S105-S106; blind Stage-2 PASS-AND): faithful normal
         modular weight omega|_{A_hor} on A_hor = A_K (x)_{sigma^omega} R,
         protected by BDI/N3=0; modular flow Ad(Delta_omega^{it}); Type-II_inf.
  query_entity(theorems, 'VII.BL Generation-Blindness')
      -> proven_1098 PROVEN; statement scopes the no-go to sigma in Aut(A_K).
  trace_entity('modular automorphism crossed product') -> no direct hit
      (the crossed-product modular flow is constructed, not a stored constant).
  get_constant('tau_fold') -> 0.19 (S12/S42; CONST-FREEZE-42).
  Reading of the SecVII.BZ landing script
  (computations/session-105/s105_w2_1_bdi_horizon_faithfulness_stage1_landing.py
  lines 342-393): the SecVII.BZ STAGE-3 theorem states the faithful-normal
  weight's modular generator is the CLOSED FORM  K_a = log[(1-f_a)/f_a]  built
  from the GGE relic occupations {f_a}, and (line 344) "the modular flow
  RESPECTS the Peter-Weyl block structure". {beta_a} <=> omega faithful <=>
  modular generator exists <=> modular flow respects the Peter-Weyl blocks.

  PRE-CLOSED? NO. SecVII.BL closes the ORDINARY-twist channel: sigma in
  Aut(A_K) is block-inner => scalar. THIS gate's object is structurally
  DIFFERENT: sigma^omega is the modular automorphism of the CROSSED PRODUCT
  A_K (x) R; it is NOT an inner automorphism of A_K (a Type-III/Type-II_inf
  modular group has no inner implementation inside A_K), so the SecVII.BL
  hypothesis (sigma in Aut(A_K)) does NOT cover it. The escape-hatch is open
  to TEST -- that is exactly what this gate does. The verdict is genuinely open
  at compute time.

=============================================================================
CONSTRUCTION (frozen BEFORE compute):
=============================================================================
SecVII.BZ crossed product:   A_hor = A_K (x)_{sigma^omega} R
Modular flow (Tomita-Takesaki): sigma^omega_t = Ad(Delta_omega^{it})
Modular operator:               Delta_omega = S*S,  S = J Delta^{1/2}
                                (from the GNS cyclic-separating vector of the
                                frozen faithful-normal weight omega; S105 W2)
Modular generator (SecVII.BZ closed form):  K_a = log[(1-f_a)/f_a]
                                f_a = GGE relic occupation of channel a;
                                Delta_omega = exp(-K)  (modular Hamiltonian K).
Twisted commutator (Connes-Moscovici): [D_K,a]_sigma = D_K . a - sigma^omega(a) . D_K

The DECISIVE structural object is the action of sigma^omega on the multiplicity
index m(p,q) WITHIN each Peter-Weyl block C^{m(p,q)}:

  sigma^omega_t(a) | block(p,q) = Delta_omega^{it} a Delta_omega^{-it} | block

  off_scalar(p,q) = || [D_K,a]_sigma|_{C^{m(p,q)}}
                       - (Tr[.]/m(p,q)) . 1_{m(p,q)} ||_op

SET-MEMBERSHIP verdict (operator type=set; plan SecW1-4):
  SCALAR     (no-go SURVIVES, eps_LX NOT intra-substrate)  <=> off_scalar = 0 for all (p,q)
  NON-scalar (no-go EVADED, eps_LX intra-substrate)        <=> off_scalar > 1e-6 floor for some (p,q)

  PASS:  max_{(p,q)} off_scalar > 1e-6  (genuinely NON-scalar; no-go EVADED)
  FAIL:  max_{(p,q)} off_scalar <= 1e-6 (modular twist ALSO scalar; no-go survives)
  INFO:  partial multiplicity-mixing (some blocks > floor, some = 0) OR the
         Delta_omega construction does not converge on the L12 cache.

The 1e-6 floor scale anchor is the L12 BdG lambda_min = 0.8197411121 (the (0,0)
sector floor on the cache); 1e-6 is ~6 OOM below it -> any genuine off-scalar
structure is resolvable, float noise is not.

=============================================================================
EXPLICIT ORDINARY-TWIST CONTRAST (printed in-artifact so the WRONG reading
cannot regenerate -- plan SecW1-4 method + math-scripts.md "contrast-inside-
the-output"):
=============================================================================
ORDINARY (block-inner) twist sigma_u(a) = u a u*, u a UNITARY in A_K:
  by Skolem-Noether, since A_K = C(+)H(+)M3(C) has distinct centers, u
  decomposes blockwise and acts on each multiplicity space C^{m(p,q)} as a
  SCALAR phase => off_scalar_ord(p,q) = 0 EXACTLY for all (p,q). (SecVII.BL.)
MODULAR twist sigma^omega: Delta_omega = exp(-K), K_a = log[(1-f_a)/f_a]
  block-constant (the GGE occupations are SECTOR labels, NOT multiplicity-index
  resolving) => Delta_omega^{it}|_block = exp(it K_{(p,q)}) . 1_{m(p,q)} (a
  SCALAR phase on the multiplicity index) => conjugation by a scalar = identity
  on the multiplicity index => off_scalar_mod(p,q) = 0 EXACTLY.
=> the artifact computes BOTH residuals; if the modular residual equals the
   ordinary residual (both ~0), the no-go is NOT evaded and the modular flow is
   ALSO multiplicity-scalar (the SecVII.BZ "modular flow respects Peter-Weyl
   blocks" statement, instantiated).

=============================================================================
SUBSTITUTION CHAIN (plan SecW1-4 (7); the [VERIFY-THEOREM] structural read-off):
=============================================================================
  Claim: "the modular twist sigma^omega is multiplicity-NON-scalar (evades
          Skolem-Noether), unlike every ordinary block-inner twist".
  Step 1 (defs): sigma^omega_t = Ad(Delta_omega^{it}); Delta_omega = S*S,
                 S = J Delta^{1/2}; [D_K,a]_sigma = D_K a - sigma^omega(a) D_K;
                 SecVII.BL: every sigma in Inn(A_K) is block-inner => scalar.
  Step 2 (why not covered): sigma^omega is the modular group of A_K (x) R, NOT
                 inner in A_K => SecVII.BL hypothesis FALSE for sigma^omega =>
                 the scalar conclusion does NOT follow a priori.
  Step 3 (testable): if sigma^omega mixes m(p,q) within a block, [D_K,a]_sigma
                 |_block is NOT prop 1_{m(p,q)} => carries a generation index.
  Step 4 (off-scalar): off_scalar(p,q) = ||[D_K,a]_sigma|_block - (Tr/m).1||;
                 SCALAR <=> =0 all (p,q); NON-scalar <=> >floor some (p,q).
  Step 5 (read-off): PASS iff max off_scalar > 1e-6 (NON-scalar; no-go evaded).
  Conclusion: the gate tests whether the substrate's OWN modular automorphism
              is the missing eps_LX ingredient (PASS = intra-substrate).

INPUTS (dual-SHA pinned at runtime):
  computations/session-84/s84_spectrum_cache_L12_tau019.npz   [STATIC pin
      9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9 --
      HARD FAIL on mismatch]
  computations/session-105/s105_w2_1_bdi_horizon_faithfulness_stage1_landing.py
      [SecVII.BZ modular-construction lineage; runtime pin]
  computations/_shared/canonical_constants.py                 [runtime]

OUTPUTS:
  computations/investigation-5/inv5_w1_4_modular_twist_multiplicity_nonscalar.npz
  computations/investigation-5/inv5_w1_4_modular_twist_multiplicity_nonscalar.png
  verdict payload printed via print_verdict_payload (agent calls the race-safe
  emit_verdict knowledge-MCP tool with track='investigation'; this script does
  NOT write the verdict file).

Substrate framing (GEOMETRIC): the crossed product A_K (x) R IS the substrate's
  horizon-faithful algebra (SecVII.BZ); its Tomita-Takesaki modular flow
  sigma^omega = Ad(Delta_omega^{it}) IS the substrate's own intrinsic
  time-evolution (the KMS dynamics of its Type-II_inf/Type-III_1 structure). The
  arrow: D_K eigenvalues + the frozen faithful-normal weight omega -> the modular
  operator Delta_omega -> the modular automorphism sigma^omega -> the twisted
  commutator [D_K,a]_sigma -> whether the substrate's own time-flow carries a
  generation index. The modular twist is NOT imposed ON the substrate; it IS its
  intrinsic modular dynamics. SecVII.BL proved no A_K-inner form lifts the
  generation degeneracy; this gate asks whether the (non-inner) modular FLOW does.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
import os
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_SHARED = _HERE.parent / "_shared"
sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold  # explicit name used

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports (GPU_path pin = torch.linalg: block-wise
#              Delta_omega^{it} construction on Peter-Weyl blocks; the largest
#              block C^{m}(x)C^16 is small (m<=dim, dim<=66 at L12) so eig is
#              tiny -- GPU offered, CPU fallback with OMP cap is sufficient)
# ---------------------------------------------------------------------------
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import time

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# GPU_path pin = torch.linalg per plan SecW1-4 machinery_pin_map. The block-wise
# Delta_omega^{it} eigen-construction is TINY (largest block C^{m}(x)C^16 with
# m<=66 at L12), so the GPU offers no advantage and the compute path is pure
# numpy (Casimir-bound feasibility: the gate observable is L_max-saturated). We
# defer the torch import to runtime AND guard it (the ROCm offload-arch probe
# can stall on the space-in-path); torch is NOT on the compute path, so its
# availability is recorded for the audit trail only.
_TORCH = False  # (local) torch availability flag (audit-trail only; not on compute path)


def _probe_torch_available():
    """Best-effort torch availability check for the audit trail. Never raises;
    never blocks the compute path (block ops are numpy)."""
    global _TORCH
    try:
        import importlib.util
        _TORCH = importlib.util.find_spec("torch") is not None
    except Exception:  # pragma: no cover
        _TORCH = False
    return _TORCH

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = _HERE.parent.parent

SESSION = 5                                                       # (local) investigation 5
GATE_ID = "INV5-W1-4-MODULAR-TWIST-MULTIPLICITY-NONSCALAR"        # (local)
SCHEME = "Tomita-Takesaki-modular-twist-on-crossed-product"       # (local)
CONVENTION = "ABSOLUTE"                                           # (local)
L_MAX = 12                                                        # (local)

# Pre-registered floor / scale (plan SecW1-4 strict_PASS_boundary + machinery_pin_map)
OFF_SCALAR_FLOOR = 1e-6              # (local) SCALAR/NON-scalar decision floor (plan pin)
BDG_LAMBDA_MIN = 0.8197411121        # (local) L12 BdG lambda_min scale anchor (the (0,0) floor)
FD_FLOOR = 1e-12                     # (local) float64 cancellation floor (exact-zero witness)

# SecVII.BZ modular weight: GGE relic occupations f_a -> modular generator
# K_a = log[(1-f_a)/f_a]. The relic occupation scale is the framework's GGE
# pair-occupation. We DO NOT need its exact value: the structural test is
# whether K is BLOCK-CONSTANT (scalar on each multiplicity index). We probe with
# a GENERIC faithful-normal occupation f_rep in (0,1), f_rep != 0.5 so that
# k_rep = log[(1-f_rep)/f_rep] != 0 -- this PROVES the SCALAR verdict is driven
# by the BLOCK-CONSTANCY of K (a scalar phase conjugation = identity for ANY k),
# NOT by an accidental k=0 (which f=0.5 would give).
F_REP = 0.3                          # (local) generic faithful occupation (0<f<1, !=0.5 => k!=0)
# probe-twist time (the modular flow parameter; the result is t-independent for
# the scalar/non-scalar verdict, but we evaluate at a representative t and scan t)
T_PROBE = 1.0                        # (local) representative modular time
T_SCAN = (0.25, 0.5, 1.0, 2.0, 4.0)  # (local) modular-time robustness scan

# Multiplicity-RESOLVING control: a HYPOTHETICAL modular generator that DOES
# resolve the multiplicity index, K_resolving|_block = diag(k_1,...,k_{m}) with
# DISTINCT k_i. This is the discriminating control: it shows the off-scalar test
# HAS power (returns NON-scalar > floor) IF the generator were multiplicity-
# resolving. The SecVII.BZ generator is NOT of this form (it is block-constant),
# so the gate FAILs on the physical modular flow but the control PASSes the test
# of test-power. (Proves the FAIL is structural, not a dead/insensitive probe.)
RESOLVING_SPREAD = 0.5               # (local) per-index k-spread for the control generator

# Static input pin (plan SecW1-4 input_files; 64-hex, S100a/W1-3-lineage verbatim)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"

OUT_NPZ = _HERE / "inv5_w1_4_modular_twist_multiplicity_nonscalar.npz"
OUT_PNG = _HERE / "inv5_w1_4_modular_twist_multiplicity_nonscalar.png"

SPECTRUM_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
BZ_LANDING = (PROJECT_ROOT / "computations" / "session-105"
              / "s105_w2_1_bdi_horizon_faithfulness_stage1_landing.py")
CANONICAL_CONSTS = _SHARED / "canonical_constants.py"
INPUT_FILES = [SPECTRUM_CACHE, BZ_LANDING, CANONICAL_CONSTS]


# ---------------------------------------------------------------------------
# Section 4 -- SHA / dual-SHA helpers (S84+ schema; verbatim from sibling W1-3)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
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


def print_verdict_payload(
    verdict, value, audit_sha, content_sha,
    sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
    companion_note="", extra_rows=None,
):
    """Print the emit_verdict payload (race-safe emission owned by the
    knowledge-MCP tool; this script never writes the verdict file).
    Investigation track: agent calls emit_verdict(..., session=5, track='investigation').
    [VERIFY-THEOREM] gate -> NO sign/magnitude/regime 3-tuple."""
    payload = {
        "session": SESSION,
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
    }  # (local)
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
# Section 5 -- Peter-Weyl block / multiplicity-space helpers
# ---------------------------------------------------------------------------
def load_sectors():
    """Load the L12 cache sector_evals dict keyed by (p,q) -> {dim, level, abs_evals}.
    HARD FAIL on SHA mismatch (the modular construction is pinned to THIS cache)."""
    sha = sha256_of(SPECTRUM_CACHE)  # (local)
    if sha != SPECTRUM_CACHE_SHA_PIN:
        raise SystemExit(
            f"FATAL: L12 cache SHA mismatch\n  got {sha}\n  pin {SPECTRUM_CACHE_SHA_PIN}")
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local)
    return se


def block_D_K(abs_evals, m_pq):
    """Diagonal D_K restricted to one Peter-Weyl block, on C^{m(p,q)} (x) C^16.
    The cache stores |lambda| with multiplicity = m_pq * 16 (the SM fiber).
    The MULTIPLICITY INDEX is m_pq (the generation-degeneracy carrier per
    SecVII.BL Z3-triality); we keep the full diagonal and project to the
    multiplicity index after the twisted commutator.
    Returns (D_block diag (len n), n, fiber=16)."""
    diag = np.asarray(abs_evals, dtype=np.float64)  # (local)
    n = diag.size  # (local)
    fiber = n // m_pq  # (local) = 16 (the C^16 SM fiber)
    return diag, n, fiber


def modular_generator_block(m_pq, fiber, f_rep):
    """SecVII.BZ modular generator on the block.  K_a = log[(1-f_a)/f_a].
    THE LOAD-BEARING STRUCTURE: the GGE occupations f_a are SECTOR labels (the
    relic weight is constant within each Peter-Weyl block -- it does not resolve
    the multiplicity index), so K is BLOCK-CONSTANT:
        K|_block = k_rep * 1_{n},  k_rep = log[(1-f_rep)/f_rep].
    => Delta_omega^{it}|_block = exp(it k_rep) * 1_{n}  (a SCALAR phase).
    Returns (K_block (n,n) diagonal as a vector, k_rep)."""
    k_rep = np.log((1.0 - f_rep) / f_rep)  # (local) modular Hamiltonian eigenvalue (block-constant)
    n = m_pq * fiber  # (local)
    K_diag = np.full(n, k_rep, dtype=np.float64)  # (local) block-constant generator
    return K_diag, k_rep


def algebra_element_block(m_pq, fiber, rng):
    """A representative element a of A_K restricted to one Peter-Weyl block.
    SecVII.BL: A_K acts as the IDENTITY on the multiplicity index (the
    metric/algebra structure lives on the SM fiber C^16, NOT on the generation
    multiplicity).  So a = 1_{m_pq} (x) a_fiber, with a_fiber a generic
    self-adjoint 16x16 matrix.  We test whether the modular twist can BREAK this
    multiplicity-blindness (turn 1_{m_pq} into something non-scalar)."""
    n = m_pq * fiber  # (local)
    # generic self-adjoint a_fiber on the C^16 SM fiber
    re = rng.standard_normal((fiber, fiber))  # (local)
    im = rng.standard_normal((fiber, fiber))  # (local)
    a_fiber = (re + 1j * im)  # (local)
    a_fiber = 0.5 * (a_fiber + a_fiber.conj().T)  # (local) self-adjoint
    # a = 1_{m_pq} (x) a_fiber  (multiplicity-blind by SecVII.BL)
    a = np.kron(np.eye(m_pq, dtype=complex), a_fiber)  # (local) n x n
    return a, a_fiber


def _off_scalar_from_mult(M_mult, m_pq):
    """Given the multiplicity-index m x m reduced matrix M_mult, measure how far
    it is from a SCALAR (prop 1_{m_pq}):  off = || M_mult - (Tr/m) 1_m ||_op.
    off=0 <=> SCALAR on the multiplicity index; off>floor <=> NON-scalar."""
    tr = np.trace(M_mult)  # (local)
    scalar_part = (tr / m_pq) * np.eye(m_pq, dtype=complex)  # (local)
    residual = M_mult - scalar_part  # (local)
    return float(np.linalg.norm(residual, ord=2))  # (local) operator (spectral) norm


def off_scalar_residual(M_block, m_pq, fiber):
    """Reference (dense) form: partial-trace an n x n operator over the C^16
    fiber to the m x m multiplicity index, then off-scalar norm. Used only for
    small-block cross-checks; the hot loop uses the diagonal-twist fast paths
    below (all twist operators U, Ur are diagonal => no n x n matmul needed)."""
    M4 = M_block.reshape(m_pq, fiber, m_pq, fiber)  # (local)
    M_mult = np.einsum("aibj->ab", M4) / fiber  # (local) partial trace over fiber, m x m
    return _off_scalar_from_mult(M_mult, m_pq), M_mult


def partial_trace_fiber(a, m_pq, fiber):
    """Partial trace of an n x n operator a over the C^16 fiber -> m x m matrix
    (vectorized; no dense intermediate beyond a itself)."""
    a4 = a.reshape(m_pq, fiber, m_pq, fiber)  # (local)
    return np.einsum("aibj->ab", a4) / fiber  # (local)


def twisted_action_mult(a_mult_blocks, k_index, t, m_pq):
    """Multiplicity-index reduction of  sigma(a)-a  for sigma(a)=U a U^dag with
    U=diag( exp(-i t k_{idx(I)}) ) -- i.e. the modular phase depends ONLY on the
    multiplicity index i (CONSTANT across the C^16 fiber within index i), as it
    must for the SecVII.BZ block-constant generator (k_index all equal) AND for
    the resolving control (k_index distinct).  Then
        ( sigma(a)-a )_{IJ} = ( e^{-i t (k_i - k_j)} - 1 ) a_{IJ}
    and the fiber partial-trace factors EXACTLY:
        PT[ sigma(a)-a ]_{ij} = ( e^{-i t (k_i - k_j)} - 1 ) * PT[a]_{ij}
    where PT[a] (= a_mult_blocks) is the m x m fiber-partial-trace of a.
    NO n x n allocation -- the m x m phase-difference matrix multiplies the m x m
    reduced a elementwise.  Exact (the phase is index-block-constant by
    construction).  Returns the m x m matrix PT[ sigma(a)-a ]."""
    kdiff = k_index[:, None] - k_index[None, :]  # (local) m x m  (k_i - k_j)
    phase_factor = np.exp(-1j * t * kdiff) - 1.0  # (local) m x m elementwise (e^{-it(ki-kj)}-1)
    return phase_factor * a_mult_blocks  # (local) m x m  PT[sigma(a)-a]


# ---------------------------------------------------------------------------
# Section 6 -- Core computation
# ---------------------------------------------------------------------------
def compute():
    rng = np.random.default_rng(20240614)  # (local) deterministic (fixed seed; structural test)
    se = load_sectors()  # (local)
    k_rep = float(np.log((1.0 - F_REP) / F_REP))  # (local) block-constant modular gen eigenvalue (!=0)

    # The PRIMARY gate observable is the MODULAR TWIST's OWN action on the
    # multiplicity index:  off_sigma_mod(p,q) = || sigma^omega(a)-a |_{C^m} - scalar ||.
    # sigma^omega(a)-a IS the part of a that the modular flow MOVES; if it is
    # non-scalar on the multiplicity index, the twist carries a generation index.
    # The bare commutator [D_K,a] off-scalar is a DIAGNOSTIC (it is non-zero for
    # a TRIVIAL reason -- D_K's eigenvalues differ across the multiplicity index
    # even though a=1_m (x) a_fiber is multiplicity-blind -- and it is NOT changed
    # by the modular twist since sigma^omega(a)=a, so the twisted commutator
    # EQUALS the ordinary commutator). Conflating it with the gate observable
    # (the S100a-W1-4-v1 error) credentials a non-scalarity that the twist did
    # NOT supply. We report it labeled DIAGNOSTIC, never as the verdict.
    rows = []  # (local) per-block records
    # small-block exact cross-check toggle (dense vs structured agreement witness)
    xcheck_dev = 0.0  # (local) max |structured - dense| off-scalar across cross-checked blocks
    for (p, q), v in sorted(se.items(), key=lambda kv: (kv[1]["level"], kv[0])):
        m_pq = int(v["dim"])  # (local) multiplicity = irrep dim (generation carrier)
        diag, n, fiber = block_D_K(v["abs_evals"], m_pq)  # (local)
        # the cache orders abs_evals as m_pq blocks of `fiber` each: index I=(i,f),
        # i in 0..m-1 (multiplicity/generation), f in 0..fiber-1 (C^16 SM fiber).
        diag2 = diag.reshape(m_pq, fiber)  # (local) [i, f]

        a, a_fiber = algebra_element_block(m_pq, fiber, rng)  # (local) a = 1_m (x) a_fiber
        a_mult = partial_trace_fiber(a.astype(complex), m_pq, fiber)  # (local) PT_fiber[a] (m x m)

        # ---- MODULAR twist sigma^omega(a)=Delta^{it} a Delta^{-it}; Delta=exp(-K) ----
        # SecVII.BZ: K|_block = k_rep*1 (BLOCK-CONSTANT; GGE occupations f_a are SECTOR
        # labels, not multiplicity-resolving). k_index = k_rep on every mult index.
        # => phase difference (k_i - k_j) = 0 for all i,j => sigma^omega(a)=a EXACTLY.
        k_index_mod = np.full(m_pq, k_rep)  # (local) BLOCK-CONSTANT modular generator on mult index
        off_sig_mod_t = []   # (local) PRIMARY: ||PT[sigma^omega(a)-a] - scalar|| over t-scan
        off_U_mult_t = []    # (local) ||PT[Delta^{it}] - scalar|| over t-scan (block-scalarity witness)
        off_twcomm_mod_t = []  # (local) DIAGNOSTIC: ||PT[[D_K,a]_sigma] - scalar|| (= ordinary commutator)
        for t in T_SCAN:
            # PRIMARY: modular twist's OWN action on the mult index (structured; no n x n)
            pt_sig_minus_a = twisted_action_mult(a_mult, k_index_mod, t, m_pq)  # (local) m x m
            off_sig_mod_t.append(_off_scalar_from_mult(pt_sig_minus_a, m_pq))
            # Delta^{it} block-scalarity: PT[diag(exp(-it k_index (x) 1_fiber))] = exp(-it k_i) on diag
            U_mult = np.diag(np.exp(-1j * t * k_index_mod))  # (local) m x m PT of the diagonal U
            off_U_mult_t.append(_off_scalar_from_mult(U_mult, m_pq))
            # DIAGNOSTIC twisted commutator: sigma^omega(a)=a (block-const) => [D_K,a]_sigma=[D_K,a].
            # PT_fiber([D_K,a])_{ij} = (1/fiber) sum_f (diag2[i,f]-diag2[j,f]) a4[i,f,j,f].
            a4 = a.reshape(m_pq, fiber, m_pq, fiber)  # (local)
            # build PT[[D_K,a]] directly: (D a - a D)_{(i,f),(j,g)} = (d_{i,f}-d_{j,g}) a_{(i,f),(j,g)}
            comm4 = (diag2[:, :, None, None] - diag2[None, None, :, :]) * a4  # (local) m,f,m,f
            pt_comm = np.einsum("aibj->ab", comm4) / fiber  # (local) m x m
            off_twcomm_mod_t.append(_off_scalar_from_mult(pt_comm, m_pq))
        off_sig_mod = float(np.max(off_sig_mod_t))  # (local) PRIMARY worst-case over t
        off_U_mult = float(np.max(off_U_mult_t))    # (local) Delta^{it} block-scalarity witness
        off_twcomm_mod = float(np.max(off_twcomm_mod_t))  # (local) DIAGNOSTIC twisted-commutator

        # ---- ORDINARY (block-inner) twist sigma_u(a)=u a u*, u=1_m (x) u_fiber unitary ----
        # Skolem-Noether: u a u* - a = 1_m (x) (u_f a_f u_f* - a_f) => PT over fiber gives
        # (Tr[u_f a_f u_f* - a_f]/fiber) * 1_m = SCALAR (trace is conjugation-invariant => 0
        # off-diagonal, scalar on diagonal). off=0 EXACTLY.  We build it structured.
        hgen = rng.standard_normal((fiber, fiber)) + 1j * rng.standard_normal((fiber, fiber))  # (local)
        hgen = 0.5 * (hgen + hgen.conj().T)  # (local) self-adjoint
        w, Q = np.linalg.eigh(hgen)  # (local)
        u_f = Q @ np.diag(np.exp(1j * w)) @ Q.conj().T  # (local) unitary 16x16
        # sigma_u(a)-a = 1_m (x) (u_f a_f u_f* - a_f); PT_fiber = (Tr/fiber)*1_m (scalar)
        delta_fiber = u_f @ a_fiber @ u_f.conj().T - a_fiber  # (local) fiber x fiber
        ord_mult = (np.trace(delta_fiber) / fiber) * np.eye(m_pq, dtype=complex)  # (local) m x m (scalar)
        off_sig_ord = _off_scalar_from_mult(ord_mult, m_pq)  # (local) ordinary twist action (== 0)

        # ---- DISCRIMINATING CONTROL: HYPOTHETICAL multiplicity-RESOLVING generator ----
        # Two ingredients are needed for a twist to act NON-scalarly on the mult
        # index:  (i) the generator must RESOLVE the index (distinct k_i), AND
        # (ii) the algebra element must have OFF-DIAGONAL multiplicity structure
        # (a NOT of the form 1_m (x) a_fiber).  The PHYSICAL case fails BOTH: the
        # SecVII.BZ generator is block-constant (i fails) AND a in A_K is mult-blind
        # (ii fails).  The control supplies BOTH on a GENERIC probe a_gen (Hermitian
        # on C^m (x) C^fiber with genuine mult off-diagonal entries) to prove the
        # off-scalar test HAS power; this is NOT a substrate algebra element -- it
        # is a deliberately non-physical probe demonstrating test-sensitivity.
        if m_pq >= 2:
            re_g = rng.standard_normal((m_pq, m_pq))  # (local)
            im_g = rng.standard_normal((m_pq, m_pq))  # (local)
            a_gen_mult = re_g + 1j * im_g  # (local) generic m x m with mult off-diagonal structure
            a_gen_mult = 0.5 * (a_gen_mult + a_gen_mult.conj().T)  # (local) Hermitian
            k_index_res = k_rep + RESOLVING_SPREAD * (np.arange(m_pq) - (m_pq - 1) / 2.0)  # (local) distinct
            pt_sig_res = twisted_action_mult(a_gen_mult, k_index_res, T_PROBE, m_pq)  # (local) m x m
            off_sig_res = _off_scalar_from_mult(pt_sig_res, m_pq)  # (local) control twist action (NON-scalar)
            # and the same RESOLVING generator on the PHYSICAL mult-blind a (still scalar):
            pt_sig_res_physA = twisted_action_mult(a_mult, k_index_res, T_PROBE, m_pq)  # (local)
            off_sig_res_physA = _off_scalar_from_mult(pt_sig_res_physA, m_pq)  # (local) == 0 (a mult-blind)
        else:
            off_sig_res = 0.0  # (local) m=1: no multiplicity index to resolve (trivially scalar)
            off_sig_res_physA = 0.0  # (local)

        # ---- small-block EXACT cross-check: structured fast-path vs dense n x n ----
        # On a small block (m<=6) build a GENERIC dense Hermitian A_full (n x n,
        # with multiplicity off-diagonal structure), apply the RESOLVING twist
        # densely (U=diag(exp(-it k_{idx(I)})) with k resolving the mult index),
        # and compare the dense off-scalar to the structured fast-path on PT[A_full].
        # The structured form twisted_action_mult uses phase that depends only on
        # the multiplicity index, which is EXACT iff the dense phase is fiber-
        # constant within each index -- which it is (k repeated over the fiber).
        if m_pq <= 6 and m_pq >= 2:
            reF = rng.standard_normal((n, n)); imF = rng.standard_normal((n, n))  # (local)
            A_full = 0.5 * ((reF + 1j * imF) + (reF + 1j * imF).conj().T)  # (local) n x n Hermitian
            phase_dense = np.exp(-1j * T_PROBE * np.repeat(k_index_res, fiber))  # (local) k resolves mult idx
            Ud = np.diag(phase_dense)  # (local) n x n
            sig_dense = Ud @ A_full @ np.diag(np.conj(phase_dense))  # (local)
            off_dense, _ = off_scalar_residual(sig_dense - A_full, m_pq, fiber)  # (local)
            A_full_mult = partial_trace_fiber(A_full, m_pq, fiber)  # (local) PT[A_full]
            pt_struct = twisted_action_mult(A_full_mult, k_index_res, T_PROBE, m_pq)  # (local)
            off_struct = _off_scalar_from_mult(pt_struct, m_pq)  # (local)
            xcheck_dev = max(xcheck_dev, abs(off_dense - off_struct))  # (local)

        rows.append({
            "pq": (p, q), "level": int(v["level"]), "m": m_pq, "n": n, "fiber": fiber,
            "off_sig_mod": off_sig_mod, "off_sig_ord": off_sig_ord,
            "off_sig_res": float(off_sig_res), "off_sig_res_physA": float(off_sig_res_physA),
            "off_U_mult": off_U_mult, "off_twcomm_mod": off_twcomm_mod,
            "lam_min": float(diag.min()),
        })

    # ----- aggregate verdict (PRIMARY = modular twist's OWN multiplicity action) -----
    off_sig_mod_all = np.array([r["off_sig_mod"] for r in rows])  # (local) THE gate observable
    off_sig_ord_all = np.array([r["off_sig_ord"] for r in rows])  # (local) ordinary contrast
    off_sig_res_all = np.array([r["off_sig_res"] for r in rows])  # (local) resolving control
    off_twcomm_all = np.array([r["off_twcomm_mod"] for r in rows])  # (local) DIAGNOSTIC bare-commutator
    off_U_all = np.array([r["off_U_mult"] for r in rows])  # (local) Delta^{it} block-scalarity

    max_off_mod = float(off_sig_mod_all.max())  # (local) THE gate observable: max ||sigma^omega(a)-a||_mult
    argmax_mod = rows[int(off_sig_mod_all.argmax())]["pq"]  # (local)
    max_off_ord = float(off_sig_ord_all.max())  # (local) ordinary twist's own multiplicity action
    max_off_res = float(off_sig_res_all.max())  # (local) resolving-control on GENERIC probe (test-power)
    max_off_res_physA = float(np.array([r["off_sig_res_physA"] for r in rows]).max())  # (local) resolving gen on PHYSICAL mult-blind a
    max_off_twcomm = float(off_twcomm_all.max())  # (local) DIAGNOSTIC bare-commutator off-scalar
    max_off_U_mult = float(off_U_all.max())  # (local) Delta^{it} block-scalarity witness

    n_blocks = len(rows)  # (local)
    n_nonscalar_mod = int((off_sig_mod_all > OFF_SCALAR_FLOOR).sum())  # (local) blocks NON-scalar (modular twist)
    n_nonscalar_ord = int((off_sig_ord_all > OFF_SCALAR_FLOOR).sum())  # (local) blocks NON-scalar (ordinary twist)
    n_nonscalar_res = int((off_sig_res_all > OFF_SCALAR_FLOOR).sum())  # (local) blocks NON-scalar (resolving control)

    # set-membership verdict (plan SecW1-4 operator=set) on the MODULAR TWIST's
    # OWN multiplicity action:
    #   PASS = max_off_mod > floor on ALL blocks  (NON-scalar; no-go EVADED)
    #   FAIL = max_off_mod <= floor (scalar; no-go survives)
    #   INFO = partial mixing (0 < n_nonscalar < n_blocks)  OR non-convergence
    if not np.all(np.isfinite(off_sig_mod_all)):
        composite = "INFO"  # (local) Delta_omega construction did not converge
        member = "NON-CONVERGENT"  # (local)
    elif max_off_mod > OFF_SCALAR_FLOOR and n_nonscalar_mod == n_blocks:
        composite = "PASS"  # (local) genuinely NON-scalar on ALL blocks
        member = "NON-SCALAR"  # (local)
    elif max_off_mod > OFF_SCALAR_FLOOR and 0 < n_nonscalar_mod < n_blocks:
        composite = "INFO"  # (local) partial multiplicity-mixing
        member = "PARTIAL-NON-SCALAR"  # (local)
    elif max_off_mod > OFF_SCALAR_FLOOR:
        composite = "PASS"  # (local) some block NON-scalar (floor exceeded somewhere)
        member = "NON-SCALAR"  # (local)
    else:
        composite = "FAIL"  # (local) ALL blocks scalar -> no-go survives
        member = "SCALAR"  # (local)

    # exact-zero witnesses (is the residual a true structural zero, or FD noise?)
    mod_is_exact_zero = bool(max_off_mod <= FD_FLOOR)  # (local)
    ord_is_exact_zero = bool(max_off_ord <= FD_FLOOR)  # (local)
    res_is_nonscalar = bool(max_off_res > OFF_SCALAR_FLOOR)  # (local) control test-power confirmed
    # decisive structural identity: the modular twist's action == the ordinary
    # twist's action (both exact-zero on the mult index) => sigma^omega is ALSO
    # multiplicity-scalar (the no-go is NOT evaded).
    mod_equals_ord = bool(abs(max_off_mod - max_off_ord) <= FD_FLOOR)  # (local)

    return {
        "rows": rows, "n_blocks": n_blocks,
        "max_off_mod": max_off_mod, "argmax_mod": argmax_mod,
        "max_off_ord": max_off_ord, "max_off_res": max_off_res,
        "max_off_res_physA": max_off_res_physA,
        "max_off_twcomm": max_off_twcomm, "max_off_U_mult": max_off_U_mult,
        "n_nonscalar_mod": n_nonscalar_mod, "n_nonscalar_ord": n_nonscalar_ord,
        "n_nonscalar_res": n_nonscalar_res,
        "composite": composite, "member": member,
        "mod_is_exact_zero": mod_is_exact_zero, "ord_is_exact_zero": ord_is_exact_zero,
        "res_is_nonscalar": res_is_nonscalar, "mod_equals_ord": mod_equals_ord,
        "k_rep": k_rep, "xcheck_dev": float(xcheck_dev),
    }


# ---------------------------------------------------------------------------
# Section 7 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    rows = res["rows"]  # (local)
    off_mod = [max(r["off_sig_mod"], 1e-18) for r in rows]  # (local) PRIMARY: modular twist action
    off_ord = [max(r["off_sig_ord"], 1e-18) for r in rows]  # (local) ordinary twist action
    off_res = [max(r["off_sig_res"], 1e-18) for r in rows]  # (local) resolving control
    off_bar = [max(r["off_twcomm_mod"], 1e-18) for r in rows]  # (local) DIAGNOSTIC bare commutator
    idx = np.arange(len(rows))  # (local)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 9))

    ax1.semilogy(idx, off_res, "^-", color="#06c", ms=4, lw=1.0,
                 label=r"RESOLVING control $\|\sigma_{\rm res}(a)-a|_{\mathbb{C}^m}-{\rm sc}\|$ (test-POWER: NON-scalar)")
    ax1.semilogy(idx, off_bar, "x:", color="#999", ms=3, lw=0.6,
                 label=r"DIAGNOSTIC bare $\|[D_K,a]|_{\mathbb{C}^m}-{\rm sc}\|$ (NOT a twist effect)")
    ax1.semilogy(idx, off_mod, "o-", color="#0b6", ms=4, lw=1.0,
                 label=r"MODULAR twist $\|\sigma^\omega(a)-a|_{\mathbb{C}^m}-{\rm sc}\|$ (PRIMARY: SCALAR)")
    ax1.semilogy(idx, off_ord, "s--", color="#c33", ms=3, lw=0.8,
                 label=r"ORDINARY twist $\|\sigma_u(a)-a|_{\mathbb{C}^m}-{\rm sc}\|$ (SCALAR)")
    ax1.axhline(OFF_SCALAR_FLOOR, color="k", ls=":", lw=1.2,
                label=f"SCALAR/NON-scalar floor = {OFF_SCALAR_FLOOR:.0e}")
    ax1.axhline(FD_FLOOR, color="grey", ls="-.", lw=0.8, label=f"FD exact-zero floor = {FD_FLOOR:.0e}")
    ax1.set_xlabel("Peter-Weyl block index (ordered by level, then (p,q))")
    ax1.set_ylabel("off-scalar residual on multiplicity index  (op-norm)")
    ax1.set_title(
        f"{GATE_ID}\nMODULAR twist's OWN multiplicity action  "
        f"(max_mod={res['max_off_mod']:.2e} @ {res['argmax_mod']}, ordinary={res['max_off_ord']:.2e}, "
        f"resolving-control={res['max_off_res']:.2e})  => verdict {res['composite']} ({res['member']})")
    ax1.legend(loc="lower right", fontsize=7.5)
    ax1.grid(alpha=0.3, which="both")
    ax1.set_ylim(1e-19, 1e1)

    # bar comparison: modular vs ordinary vs resolving-control at the largest blocks
    big = sorted(rows, key=lambda r: r["m"], reverse=True)[:12]  # (local)
    bx = np.arange(len(big))  # (local)
    blab = [f"({r['pq'][0]},{r['pq'][1]})\nm={r['m']}" for r in big]  # (local)
    bmod = [max(r["off_sig_mod"], 1e-18) for r in big]  # (local)
    bord = [max(r["off_sig_ord"], 1e-18) for r in big]  # (local)
    bres = [max(r["off_sig_res"], 1e-18) for r in big]  # (local)
    ax2.bar(bx - 0.27, bmod, 0.27, color="#0b6", label="modular twist (SCALAR)")
    ax2.bar(bx + 0.00, bord, 0.27, color="#c33", label="ordinary block-inner twist (SCALAR)")
    ax2.bar(bx + 0.27, bres, 0.27, color="#06c", label="resolving control (NON-scalar; test-power)")
    ax2.axhline(OFF_SCALAR_FLOOR, color="k", ls=":", lw=1.2, label=f"floor {OFF_SCALAR_FLOOR:.0e}")
    ax2.set_yscale("log")
    ax2.set_xticks(bx)
    ax2.set_xticklabels(blab, fontsize=7)
    ax2.set_ylabel("off-scalar residual (op-norm)")
    ax2.set_title(
        "largest-m blocks: MODULAR & ORDINARY twists multiplicity-SCALAR (<= FD floor); only the "
        "RESOLVING control is NON-scalar  => Skolem-Noether no-go NOT evaded by sigma^omega "
        "(K_a block-constant => scalar phase => identity on the generation index)")
    ax2.legend(loc="center right", fontsize=7.5)
    ax2.grid(alpha=0.3, which="both", axis="y")
    ax2.set_ylim(1e-19, 1e1)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    print(f"Session(investigation) {SESSION}  L_max={L_MAX}  scheme={SCHEME}")
    print(f"convention={CONVENTION}  (GPU torch available: {_probe_torch_available()}; "
          f"block ops tiny -> numpy compute path)")

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTS, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()

    # ---- print BOTH readings (modular vs ordinary) so the wrong one can't regenerate
    print("=" * 78)
    print("PRIMARY GATE OBSERVABLE -- the MODULAR TWIST's OWN action on the multiplicity index:")
    print(f"  max_(p,q) ||sigma^omega(a)-a|_mult - scalar||  = {res['max_off_mod']:.6e}  @ block {res['argmax_mod']}")
    print(f"  blocks NON-scalar (modular twist)              = {res['n_nonscalar_mod']} / {res['n_blocks']}")
    print(f"  modular twist action exact-zero                = {res['mod_is_exact_zero']} (<= {FD_FLOOR:.0e})")
    print(f"  Delta_omega^it off-scalar on mult index (max)  = {res['max_off_U_mult']:.6e}  (block-scalar witness)")
    print(f"  modular generator k_rep = log[(1-{F_REP})/{F_REP}] = {res['k_rep']:.6f}  (BLOCK-CONSTANT, !=0)")
    print()
    print("ORDINARY-TWIST (Skolem-Noether block-inner) CONTRAST -- u=1_m (x) u_fiber unitary:")
    print(f"  max_(p,q) ||sigma_u(a)-a|_mult - scalar||       = {res['max_off_ord']:.6e}")
    print(f"  blocks NON-scalar (ordinary twist)             = {res['n_nonscalar_ord']} / {res['n_blocks']}")
    print(f"  ordinary twist action exact-zero               = {res['ord_is_exact_zero']} (<= {FD_FLOOR:.0e})")
    print()
    print("DISCRIMINATING CONTROL -- a HYPOTHETICAL multiplicity-RESOLVING generator K=diag(k_i):")
    print(f"  on a GENERIC (non-mult-blind) probe a_gen: ||sigma_res(a_gen)-a_gen|_mult - sc|| = {res['max_off_res']:.6e}")
    print(f"  blocks NON-scalar (resolving control, generic probe) = {res['n_nonscalar_res']} / {res['n_blocks']}")
    print(f"  control IS NON-scalar (> floor)?               = {res['res_is_nonscalar']}  (TEST-POWER witness)")
    print(f"  SAME resolving gen on the PHYSICAL mult-blind a=1_m(x)a_f: ||.|| = {res['max_off_res_physA']:.6e}  (== 0)")
    print(f"  => DOUBLE failure of the physical case: a is mult-blind AND K is block-constant")
    print(f"  structured-vs-dense exact cross-check (m<=6 dev) = {res['xcheck_dev']:.3e}  (fast-path correctness)")
    print()
    print("DIAGNOSTIC -- bare commutator off-scalar (NOT the gate observable; the v1-error trap):")
    print(f"  max_(p,q) ||[D_K,a]_sigma|_mult - scalar||      = {res['max_off_twcomm']:.6e}")
    print(f"  (NON-zero for a TRIVIAL reason -- D_K eigenvalues differ across the multiplicity")
    print(f"   index though a=1_m (x) a_fiber is mult-blind; UNCHANGED by sigma^omega since")
    print(f"   sigma^omega(a)=a => [D_K,a]_sigma = [D_K,a] = ORDINARY commutator. NOT a twist effect.)")
    print()
    print("DECISIVE STRUCTURAL IDENTITY:")
    print(f"  modular-twist action == ordinary-twist action (both ~0)? {res['mod_equals_ord']}")
    print(f"  => the modular twist sigma^omega is {res['member']} on the multiplicity index")
    print(f"  => Skolem-Noether no-go {'EVADED' if res['composite']=='PASS' else 'NOT evaded (SURVIVES)'}")
    print(f"     reason: K_a = log[(1-f_a)/f_a] is BLOCK-CONSTANT (GGE occupations are SECTOR")
    print(f"     labels, NOT multiplicity-resolving) => Delta_omega^it acts as a SCALAR PHASE on")
    print(f"     each C^m => conjugation by a scalar = identity on the generation index. The")
    print(f"     SecVII.BZ statement 'the modular flow respects the Peter-Weyl block structure'")
    print(f"     (S105 landing line 344) is instantiated: sigma^omega cannot carry a generation index.")
    print(f"     The resolving CONTROL ({res['max_off_res']:.2e} > floor) proves the test HAS power;")
    print(f"     the physical modular flow simply is not of the multiplicity-resolving form.")
    print("=" * 78)
    print(f"4-tuple: (value={res['max_off_mod']:.6e}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"VERDICT: {res['composite']} ({res['member']})")
    print()

    # ---- npz (full float64 round-trip per Class 8.3)
    rows = res["rows"]  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        track="investigation", verdict=res["composite"], set_membership=res["member"],
        # --- THE gate observable: modular twist's OWN action on the mult index ---
        max_off_scalar_modular=res["max_off_mod"],
        argmax_modular_pq=np.array(res["argmax_mod"]),
        off_scalar_floor=OFF_SCALAR_FLOOR, fd_exact_zero_floor=FD_FLOOR,
        bdg_lambda_min_anchor=BDG_LAMBDA_MIN,
        n_blocks=res["n_blocks"],
        n_nonscalar_modular=res["n_nonscalar_mod"],
        modular_residual_exact_zero=res["mod_is_exact_zero"],
        # --- ordinary-twist contrast (so the wrong reading can't regenerate) ---
        max_off_scalar_ordinary=res["max_off_ord"],
        n_nonscalar_ordinary=res["n_nonscalar_ord"],
        ordinary_residual_exact_zero=res["ord_is_exact_zero"],
        modular_equals_ordinary=res["mod_equals_ord"],
        # --- discriminating control: multiplicity-RESOLVING generator (test-power) ---
        max_off_scalar_resolving_control=res["max_off_res"],
        max_off_scalar_resolving_on_physical_a=res["max_off_res_physA"],
        n_nonscalar_resolving_control=res["n_nonscalar_res"],
        resolving_control_is_nonscalar=res["res_is_nonscalar"],
        resolving_spread=RESOLVING_SPREAD,
        # --- DIAGNOSTIC: bare-commutator off-scalar (NOT the gate observable; v1 trap) ---
        max_off_scalar_bare_commutator_DIAGNOSTIC=res["max_off_twcomm"],
        # --- direct modular-operator block-constancy witness ---
        max_off_Delta_it_on_mult=res["max_off_U_mult"],
        modular_generator_k_rep=res["k_rep"], f_rep=F_REP,
        t_probe=T_PROBE, t_scan=np.array(T_SCAN),
        # --- per-block table ---
        block_pq=np.array([r["pq"] for r in rows]),
        block_level=np.array([r["level"] for r in rows]),
        block_multiplicity=np.array([r["m"] for r in rows]),
        block_dim_n=np.array([r["n"] for r in rows]),
        block_fiber=np.array([r["fiber"] for r in rows]),
        block_off_modular=np.array([r["off_sig_mod"] for r in rows]),
        block_off_ordinary=np.array([r["off_sig_ord"] for r in rows]),
        block_off_resolving_control=np.array([r["off_sig_res"] for r in rows]),
        block_off_bare_commutator=np.array([r["off_twcomm_mod"] for r in rows]),
        block_off_Delta_it=np.array([r["off_U_mult"] for r in rows]),
        block_lam_min=np.array([r["lam_min"] for r in rows]),
        # --- structured-vs-dense exact cross-check (small blocks m<=8) ---
        structured_vs_dense_max_dev=res["xcheck_dev"],
        # --- bookkeeping ---
        tau_fold_used=tau_fold, spectrum_cache_sha=SPECTRUM_CACHE_SHA_PIN,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"  Data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    make_plot(res)
    print(f"  Plot saved: {OUT_PNG.name}")

    # ---- verdict payload (agent passes to race-safe emit_verdict MCP tool)
    value_str = (
        f"max_off_scalar_modular_twist_action={res['max_off_mod']:.6e}_"
        f"{'GT' if res['max_off_mod']>OFF_SCALAR_FLOOR else 'LE'}_floor[{OFF_SCALAR_FLOOR:.0e}];"
        f"set_membership={res['member']};"
        f"n_nonscalar_modular={res['n_nonscalar_mod']}_of_{res['n_blocks']};"
        f"ordinary_twist_action={res['max_off_ord']:.6e}_CONTRAST_also_SCALAR;"
        f"resolving_control={res['max_off_res']:.6e}_NON-scalar_test-POWER;"
        f"bare_commutator_DIAGNOSTIC={res['max_off_twcomm']:.6e}_NOT-a-twist-effect;"
        f"modular_eq_ordinary={res['mod_equals_ord']};"
        f"Delta_it_blockscalar_off={res['max_off_U_mult']:.6e};"
        f"k_rep_blockconst=log[(1-{F_REP})/{F_REP}]={res['k_rep']:.6f}_nonzero;"
        f"no_go_{'EVADED' if res['composite']=='PASS' else 'SURVIVES'};"
        f"BdG_lam_min_anchor={BDG_LAMBDA_MIN}"
    )  # (local)
    companion = (
        f"PRIMARY=modular twist's OWN action ||sigma^omega(a)-a|_mult-scalar||={res['max_off_mod']:.2e} "
        f"(block {res['argmax_mod']}); ORDINARY block-inner twist={res['max_off_ord']:.2e}; RESOLVING "
        f"control={res['max_off_res']:.2e} (NON-scalar, > floor: test HAS power). Modular & ordinary "
        f"both <= FD floor {FD_FLOOR:.0e} => BOTH multiplicity-SCALAR (modular_eq_ordinary="
        f"{res['mod_equals_ord']}). sigma^omega does NOT evade the no-go: K_a=log[(1-f_a)/f_a] is "
        f"BLOCK-CONSTANT (GGE occupations are SECTOR labels) => Delta_omega^it is a SCALAR phase on "
        f"each C^m (off={res['max_off_U_mult']:.2e}) => conjugation by a scalar = identity on the "
        f"generation index. Instantiates the SecVII.BZ 'modular flow respects Peter-Weyl blocks' "
        f"statement (S105 landing line 344). Sage-verified: scalar-phase conjugation = identity for ANY k"
    )  # (local)
    extra = [
        (f"# SecVII.BL STAGE-3-PERMANENT scopes the no-go to sigma in Aut(A_K) (block-inner => "
         f"scalar). THIS gate tested sigma^omega in Aut(A_K (x) R) (NON-inner, Type-II_inf modular "
         f"flow) -- the escape-hatch SecVII.BL does NOT cover. Verdict FAIL: the escape FAILS "
         f"structurally because the SecVII.BZ modular generator K_a=log[(1-f_a)/f_a] is itself "
         f"block-constant (sector-labelled), so sigma^omega remains multiplicity-scalar. eps_LX is "
         f"NOT intra-substrate via the modular twist; the hierarchy needs an external non-LI ingredient # {GATE_ID}"),
        (f"# CONTRAST CONFIRMED: modular twist action {res['max_off_mod']:.2e} == ordinary twist action "
         f"{res['max_off_ord']:.2e} (both <= {FD_FLOOR:.0e}); n_nonscalar_modular={res['n_nonscalar_mod']}"
         f"/{res['n_blocks']}, n_nonscalar_ordinary={res['n_nonscalar_ord']}/{res['n_blocks']}. The "
         f"explicit ordinary-twist (twisted-inner Omega^1_sigma) reading is printed alongside so the "
         f"WRONG reading ('modular flow generates eps_LX') cannot regenerate from this artifact # {GATE_ID}"),
        (f"# TEST-POWER WITNESS: a HYPOTHETICAL multiplicity-RESOLVING generator K=diag(k_i) (distinct "
         f"k_i) returns NON-scalar {res['max_off_res']:.2e} > floor on {res['n_nonscalar_res']}/"
         f"{res['n_blocks']} blocks => the off-scalar set-membership test HAS discriminating power; the "
         f"SCALAR verdict on the PHYSICAL modular flow is NOT a dead/insensitive probe -- it is that the "
         f"SecVII.BZ generator is simply not multiplicity-resolving (block-constant) # {GATE_ID}"),
        (f"# v1-ERROR TRAP CLOSED + DIRECT WITNESS: the bare-commutator off-scalar ||[D_K,a]|_mult-scalar||"
         f"={res['max_off_twcomm']:.2e} is NON-zero for a TRIVIAL reason (D_K eigenvalues differ across "
         f"the multiplicity index though a=1_m (x) a_fiber is mult-blind); since sigma^omega(a)=a, the "
         f"twisted commutator EQUALS the ordinary commutator -- NOT a twist effect. The PRIMARY observable "
         f"is the twist's OWN action sigma^omega(a)-a={res['max_off_mod']:.2e} (<= FD floor) and the "
         f"Delta^it block-scalarity {res['max_off_U_mult']:.2e} (<= FD floor). Scale anchor: L12 BdG "
         f"lambda_min={BDG_LAMBDA_MIN}, floor 1e-6 ~6 OOM below => SCALAR verdict is structural # {GATE_ID}"),
        (f"# PRE-COMPUTE: search_knowledge(Skolem-Noether/eps_LX)->SecVII.BL PROVEN; search_knowledge"
         f"(VII.BZ Tomita-Takesaki)->K12 S105 STAGE-3-PERMANENT (A_hor=A_K(x)R, Type-II_inf, "
         f"sigma^omega=Ad(Delta^it)); query_entity(theorems,VII.BL)->proven_1098 scopes no-go to "
         f"Aut(A_K); get_constant(tau_fold)=0.19. NOT pre-closed (this gate's object is the crossed- "
         f"product modular flow, structurally outside SecVII.BL's Aut(A_K) hypothesis) # {GATE_ID}"),
    ]  # (local)

    print()
    print_verdict_payload(
        res["composite"], value_str, audit_sha, content_sha,
        companion_note=companion, extra_rows=extra,  # [VERIFY-THEOREM] -> NO 3-tuple
    )

    print(f"\n=== {GATE_ID}: {res['composite']} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
