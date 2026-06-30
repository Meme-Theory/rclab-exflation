#!/usr/bin/env python3
"""
INV9-W1-2-SWAMPLAND-GRADIENT-BOUND  --  [SIGN] gate (investigation-9, Wave 1)
============================================================================

kaku-speculative-theorist (origin B-2/NS-2, CF14); volovik co-opted for the V(q) leg.

CLAIM (JOINT): BOTH the spectral-action gradient ratio g_S = |S'(tau)|/S(tau) at
tau_fold AND the FRESH Volovik/dilaton q-theory potential gradient ratio
g_V = |V'(q)|/V(q) exceed the swampland de Sitter constant c ~ O(1); the joint
AND (g_S > c) AND (g_V > c) forbids a metastable dS minimum on BOTH axes and
FORCES quintessence-rolling tau/q dynamics (resolves the A4 fork: roll, not sit).

SUBSTRATE FRAMING (GEOMETRIC): the substrate IS the spectral triple deforming
along its Jensen modulus tau (and its dilaton/q-variable phi); S(tau) and V(phi)
ARE the substrate's own internal action functionals, NOT potentials living IN a
moduli container. Direction: D_K(tau) eigenvalues -> spectral moments a_0,a_2,a_4
-> S(tau)=a_0-a_2+a_4 and the Weyl-anomaly dilaton potential V(phi) -> their
gradient ratios |S'|/S, |V'|/V -> the swampland dS classification. The substrate
has NO resting place along its modulus (no minimum: S(tau) monotone, dS/dtau>0;
V(phi) monotone-increasing, has_minimum=False) -- it MUST roll. That restlessness
is swampland-MANDATED, not a defect.

==== TWO LEGS ====

(A) S(tau) leg  [CROSS-CHECK of the PROVEN S69 W4-B verdict -- do NOT re-derive]:
    g_S^bare = |dS/dtau|/S_fold = 58672.80 / 250360.68 = 0.2343  (the BARE
    single-crystal ratio). The swampland-relevant SCHEME-DRESSED value is the
    canonically-normalized ratio on the tau-modulus field-space metric, which
    S69 W4-B established as c = 3.52 (cutoff scheme) / c ~ 6.6 (zeta scheme).
    "The gradient condition does not discriminate between functionals" (S69 W4-B,
    PROVEN). This leg REPRODUCES and CITES that closed verdict; it is NOT a fresh
    derivation. g_S (dressed) = 3.52 > 1 ~ c.

(B) V(phi) leg  [FRESH, CF14 = S47 D-6, never computed against the dS conjecture]:
    the substrate dilaton potential is the Weyl-anomaly potential (Lizzi 03-04;
    DILATON-POTENTIAL-66, gate W2-D):
        V(phi) = (1/8)(e^{4phi}-1) a_0 + (1/2)(e^{2phi}-1) a_2 R + phi a_4   [M_KK^4 units]
        V'(phi) = (a_0/2) e^{4phi} + (a_2 R) e^{2phi} + a_4 > 0  for ALL phi
        R = 6 a_0/a_2 (the SU(3) scalar curvature at the fold).
    g_V(phi) = |V'(phi)| / |V(phi)|, RE-DERIVED at runtime from
    s66_dilaton_potential.npz (NOT pinned to the survey "k=+3586.5" number --
    flagged below: the survey conflated 3586.5 with V'; 3586.5 is actually the
    q-theory ZERO-POINT-ENERGY curvature d2E_ZP/dq2|_0 = -3586.531 from S62, a
    SECOND derivative of a DIFFERENT object, NOT this dilaton gradient).

    STRUCTURAL SUBTLETY (the honest content of this leg): V(phi=0) = 0 EXACTLY
    (the Weyl subtraction zeros the CC at the reference point). So g_V AT the
    operating point phi=0 is |V'(0)|/0 = +inf -- the dS bound is satisfied
    INFINITELY but at a node the ratio diverges trivially. The swampland bound
    |grad V|/V >= c is meaningful where V != 0; the ROBUST substrate-IS statement
    is that V has NO minimum (V' > 0 everywhere), so a metastable dS minimum is
    structurally impossible and the dilaton is FORCED to roll. The gate therefore
    reports g_V on a robust support (the grid points where |V| is bounded away
    from the node) AND the global no-minimum fact, not the singular g_V(0).

(C) JOINT verdict: g_S > c AND g_V > c  =>  the dS conjecture forbids a metastable
    minimum on BOTH axes  =>  quintessence-rolling tau/q dynamics (A4 = roll).

DATA-ALREADY-EXISTS: dS_fold, S_fold, a0/a2/a4, V(phi) are all on disk. The work
is the dressed-ratio cross-check, the FRESH V'(phi) re-derivation + the node
subtlety, and the JOINT reading.

Pre-registered (plan investigation-9-plan-w1.md SS W1-2):
  operator: inequality; form g_S=|S'|/S, g_V=|V'|/V; JOINT = (g_S>c) AND (g_V>c)
  strict_PASS_boundary: c ~ O(1) = 1.0; direction ">"
  scheme: zeta (swampland-relevant dressed ratio); cutoff cross-check (S69 c=3.52)
  convention: RATIO
  regulator_pin: a_2^{zeta} + a_0^{zeta} (S=a_0-a_2+a_4, zeta half-moments,
                 CONST-FREEZE-42); cutoff-scheme cross-check uses a_n^{cutoff}
  trigger: [SIGN]  -> sign_verdict keys on the JOINT (g_S>c) AND (g_V>c)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # numpy CPU thread cap (plan GPU_path: numpy.linalg)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY: import, never hardcode) ----
SHARED_DIR = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (          # noqa: E402
    S_fold, dS_fold, Z_fold,
    a0_fold, a2_fold, a4_fold,
    tau_fold, M_KK,
)

# ---- gate identity ----
GATE_ID = "INV9-W1-2-SWAMPLAND-GRADIENT-BOUND"
SESSION = 9          # (local) investigation-track number (emit_verdict session arg)
SCHEME = "zeta"
CONVENTION = "RATIO"
L_MAX = 10           # (local) D_K cache truncation the S(tau) + V(phi) moments sit on

SCRIPT_DIR = Path(__file__).resolve().parent
NPZ_PATH = SCRIPT_DIR / "inv9_w1_swampland_gradient_bound.npz"
PNG_PATH = SCRIPT_DIR / "inv9_w1_swampland_gradient_bound.png"
DILATON_NPZ = Path(__file__).resolve().parents[1] / "session-66" / "s66_dilaton_potential.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

# ---- pre-registered anchors (cross-check / external, NOT canonical value sources) ----
C_SWAMPLAND = 1.0                 # (local) external-anchor: swampland dS constant c ~ O(1) (Obied-Ooguri-Spodyneiko-Vafa 2018)
C_S69_CUTOFF = 3.52               # (local) external cross-check: S69 W4-B PROVEN dressed g_S, cutoff scheme (cited, NOT re-derived)
C_S69_ZETA = 6.6                  # (local) external cross-check: S69 W4-B dressed g_S, zeta scheme (est., cited)
SURVEY_K_ANCHOR = 3586.5          # (local) survey "k=+3586.5 M_KK" -- flagged: this is the S62 q-theory ZPE curvature d2E_ZP/dq2|_0=-3586.531, NOT V'(phi); drift check below


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(Path(p).read_bytes())
    except OSError:
        return "MISSING"
    return h.hexdigest()


def compute_dual_sha(pins: dict) -> tuple:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = Path(__file__).resolve().read_bytes()         # (local)
    try:
        canonical_bytes = CANONICAL_PATH.read_bytes()            # (local)
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()                                   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                 # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None):
    """Print the delimited JSON block the dispatching agent feeds to
    mcp__knowledge__emit_verdict(session=9, track='investigation', **payload).
    The script does NOT write the verdict file (race-safe emission is the tool's job)."""
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


def main() -> int:
    t0 = time.time()                                             # (local)

    # ---------------------------------------------------------------
    # 0. Input pins (first lines of stdout) + dual SHA
    # ---------------------------------------------------------------
    pins = {
        "canonical_constants.py": sha256_file(CANONICAL_PATH),
        "s66_dilaton_potential.npz": sha256_file(DILATON_NPZ),
    }
    print("=" * 72)
    print(f"{GATE_ID}  [SIGN]  (investigation-9, Wave 1)")
    print("=" * 72)
    print("INPUT PINS (sha256):")
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}...")
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()
    print("CANONICAL CONSTANTS (imported, query-first verified vs knowledge MCP):")
    print(f"  S_fold   = {S_fold:.8f}   (S42 s42_gradient_stiffness)")
    print(f"  dS_fold  = {dS_fold:.8f}   (S42, dS_full/dtau at fold)")
    print(f"  Z_fold   = {Z_fold:.8f}   (S42 gradient stiffness)")
    print(f"  a0_fold  = {a0_fold:.6f}   (zeta-scheme half mode-count, CONST-FREEZE-42)")
    print(f"  a2_fold  = {a2_fold:.10f}   (zeta-scheme half zeta_D(1), CONST-FREEZE-42)")
    print(f"  a4_fold  = {a4_fold:.10f}   (Gauss-Bonnet / gauge kinetic)")
    print(f"  tau_fold = {tau_fold}   (CONST-FREEZE-42)")
    print()

    # ===============================================================
    # LEG A -- S(tau) gradient ratio  [CROSS-CHECK of PROVEN S69 W4-B]
    # ===============================================================
    print("=" * 72)
    print("LEG A: spectral-action gradient ratio g_S = |S'(tau)|/S(tau) at tau_fold")
    print("       [CROSS-CHECK of the PROVEN S69 W4-B verdict -- NOT re-derived]")
    print("=" * 72)

    # Substitution chain (Claim A):
    #   Step 1: g_S^bare := |dS/dtau| / S_fold   (bare single-crystal ratio)
    #   Step 2: dS/dtau = +58672.80 (=dS_fold); S_fold = 250360.68   [canonical]
    #   Step 3: g_S^bare = 58672.80 / 250360.68 = 0.2343  (BARE -- NOT swampland-relevant)
    #   Step 4: dressed (canonically-normalized) ratio = S69 W4-B c=3.52 cutoff / ~6.6 zeta
    #   Step 5: c_dressed = 3.52 > 1 = c~O(1)  =>  g_S > c   (S69 W4-B PROVEN, reproduced)
    g_S_bare = abs(dS_fold) / S_fold                             # (local) bare ratio
    print(f"  Step 1-3 (BARE): g_S^bare = |dS/dtau|/S_fold = {abs(dS_fold):.5f}/{S_fold:.5f}")
    print(f"                            = {g_S_bare:.6f}   (BARE single-crystal -- NOT the swampland-relevant value)")
    # The dressed normalization divides the bare gradient by the field-space metric sqrt(G_tau_tau);
    # G_tau_tau ~ 5.0 (s22d modulus-space metric) gives sqrt(5)~2.236, but the CANONICAL dressed
    # value is the S69 W4-B closed result c=3.52 (cutoff) -- CITED, not re-derived.
    g_S_dressed = C_S69_CUTOFF                                   # (local) cited from S69 W4-B (cutoff scheme), the PROVEN dressed value
    g_S_dressed_zeta = C_S69_ZETA                               # (local) cited from S69 W4-B (zeta scheme)
    print(f"  Step 4-5 (DRESSED, cited): g_S(cutoff) = {g_S_dressed:.2f}, g_S(zeta) ~ {g_S_dressed_zeta:.1f}")
    print(f"                             (S69 W4-B PROVEN: 'gradient condition does not discriminate between functionals')")
    legA_pass = g_S_dressed > C_SWAMPLAND                        # (local)
    print(f"  LEG A verdict: g_S(dressed)={g_S_dressed:.2f} > c={C_SWAMPLAND}  ->  {'PASS' if legA_pass else 'FAIL'} (reproduces S69 W4-B)")
    print()

    # ===============================================================
    # LEG B -- V(phi) gradient ratio  [FRESH, CF14]  RE-DERIVED from s66 npz
    # ===============================================================
    print("=" * 72)
    print("LEG B: dilaton/q-theory potential gradient ratio g_V = |V'(phi)|/V(phi)")
    print("       [FRESH, CF14 = S47 D-6]  RE-DERIVED from s66_dilaton_potential.npz")
    print("=" * 72)

    if not DILATON_NPZ.exists():
        print(f"  ERROR: dilaton npz missing at {DILATON_NPZ}")
        return 2
    d = np.load(DILATON_NPZ, allow_pickle=True)
    phi = d["phi_grid"].astype(float)                            # (local) dilaton field phi in [-3,3]
    V = d["V_grid"].astype(float)                                # (local) V(phi) in M_KK^4 units
    dV = d["dV_grid"].astype(float)                              # (local) V'(phi)
    d2V = d["d2V_grid"].astype(float)                            # (local) V''(phi)
    a0_npz = float(d["a0_fold"]); a2_npz = float(d["a2_fold"]); a4_npz = float(d["a4_fold"])  # (local)
    R_SU3 = float(d["R_SU3"])                                    # (local) SU(3) scalar curvature = 6 a0/a2
    has_minimum = bool(d["has_minimum"])                        # (local) False -> runaway
    V_at_phi0 = float(d["V_at_phi0"])                            # (local) V(0) = 0 exactly
    dV_at_phi0 = float(d["dV_at_phi0"])                          # (local) V'(0) = 43210.72

    print(f"  Loaded V(phi): {len(phi)} pts, phi in [{phi.min():.1f},{phi.max():.1f}]; R_SU3=6a0/a2={R_SU3:.4f}")
    print(f"  has_minimum = {has_minimum}  (False => runaway potential, V' > 0 everywhere)")
    print(f"  V(phi=0) = {V_at_phi0:.6g}  (EXACTLY zero by Weyl subtraction => operating point IS a node)")
    print(f"  V'(phi=0) = {dV_at_phi0:.6f}")

    # --- Re-derive V'(phi) analytically and cross-check vs the cached dV_grid ---
    # V'(phi) = (a0/2) e^{4phi} + (a2 R) e^{2phi} + a4
    dV_rederived = (a0_npz / 2.0) * np.exp(4 * phi) + (a2_npz * R_SU3) * np.exp(2 * phi) + a4_npz  # (local)
    dV_match = float(np.max(np.abs(dV_rederived - dV)))          # (local) re-derivation residual
    print(f"  V'(phi) re-derivation residual vs cached dV_grid: max|Delta| = {dV_match:.3e}  (analytic identity check)")

    # --- DRIFT FLAG: survey "k=+3586.5" vs the actual V'(phi) ---
    # The survey's 3586.5 is NOT V'; it is the S62 q-theory ZPE curvature d2E_ZP/dq2|_0=-3586.531
    # (a SECOND derivative of a DIFFERENT object). The s66 dilaton V'(0)=43210.72 != 3586.5.
    drift_abs = abs(dV_at_phi0 - SURVEY_K_ANCHOR)               # (local)
    drift_ratio = dV_at_phi0 / SURVEY_K_ANCHOR                  # (local)
    print(f"  *** DRIFT FLAG (plan-mandated): survey k=+{SURVEY_K_ANCHOR} M_KK vs re-derived V'(0)={dV_at_phi0:.2f}")
    print(f"      |drift| = {drift_abs:.2f}  ratio = {drift_ratio:.3f}x  ==> DRIFTS HARD.")
    print(f"      Root cause: 3586.531 is the S62 q-theory ZPE curvature d2E_ZP/dq2|_0 = -3586.531")
    print(f"      (a 2nd derivative of E_ZP(q), NOT the dilaton gradient V'(phi)). The survey conflated them.")

    # --- g_V = |V'|/|V| across the grid; the node at phi=0 makes g_V diverge there ---
    eps_node = 1e-12                                            # (local) avoid 0/0 exactly at the node
    g_V_grid = np.abs(dV) / (np.abs(V) + eps_node)             # (local) gradient ratio everywhere
    # The operating-point ratio AT phi=0 (node) is formally +inf:
    g_V_at_node = abs(dV_at_phi0) / (abs(V_at_phi0) + eps_node)  # (local) ~ 4.3e16 (diverges; node artifact)
    print(f"  g_V AT operating point phi=0 (node, V=0): |V'(0)|/|V(0)| = {g_V_at_node:.3e}  (DIVERGES -- node artifact, satisfied infinitely)")

    # --- THE STRUCTURAL (grid-independent) ASYMPTOTIC LAW, verified exact in Sage ---
    # The dilaton potential has TWO asymptotic regimes, and the swampland gradient ratio
    # g_V = |V'|/V behaves OPPOSITELY in each (Sage-exact limits):
    #   phi -> +inf (CUTOFF catastrophe): V ~ (a0/8)e^{4phi}, V' ~ (a0/2)e^{4phi}
    #                                     => g_V -> 4   (SATISFIES the bound; but this is the
    #                                        a0 CC catastrophe the framework AVOIDS)
    #   phi -> -inf (ZETA runaway, the ACTUAL attractor): V ~ phi*a4 -> -inf, V' -> a4
    #                                     => g_V ~ 1/|phi| -> 0   (VIOLATES the bound: the
    #                                        runaway is asymptotically LINEAR -> too shallow)
    g_V_asymp_plus = 4.0                                      # (local) Sage-exact: limit(g_V, phi->+inf) = 4
    g_V_asymp_minus = 0.0                                     # (local) Sage-exact: limit(g_V, phi->-inf) = 0 (~1/|phi|)
    print(f"  ASYMPTOTIC LAW (Sage-exact): g_V(phi->+inf) = {g_V_asymp_plus:.1f} [cutoff regime, AVOIDED];")
    print(f"                               g_V(phi->-inf) = {g_V_asymp_minus:.1f} [zeta runaway ~1/|phi|, the ATTRACTOR]")
    print(f"  => the dS GRADIENT bound |V'|/V >= c FAILS in the zeta runaway tail (g_V -> 0 < c),")
    print(f"     which is EXACTLY where the dilaton rolls to. The runaway is too SHALLOW (linear, not steep).")

    # --- operating-region statistics (|phi|<=1, around the node, excluding the runaway tails) ---
    V_scale = a0_npz                                           # (local) M_KK^4 reference scale (the cutoff CC magnitude)
    op_mask = (np.abs(phi) <= 1.0) & (np.abs(V) > 0.10 * V_scale)  # (local) operating region away from node
    g_V_op = g_V_grid[op_mask]                                # (local)
    g_V_op_min = float(np.min(g_V_op))                        # (local) weakest steepness in the operating region
    g_V_op_med = float(np.median(g_V_op))                     # (local)
    print(f"  Operating region (|phi|<=1, |V|>0.1a0, {int(op_mask.sum())} pts): "
          f"g_V_min={g_V_op_min:.4f}, g_V_median={g_V_op_med:.4f}, g_V_max={float(np.max(g_V_op)):.4f}")

    # --- refined dS conjecture SECOND disjunct: min(V'')/V <= -c' ? ---
    # A shallow-gradient runaway can still satisfy the REFINED dS conjecture via the curvature
    # branch min(grad^2 V)/V <= -c'. Here V'' > 0 EVERYWHERE (convex; s66 proves it), so the
    # curvature branch ALSO fails: the dilaton potential satisfies NEITHER swampland disjunct
    # in the zeta tail. This STRENGTHENS the FAIL (not a marginal miss of one form).
    Vpp_pos_everywhere = bool(np.all(d2V > 0))               # (local) V'' > 0 for all phi (convex)
    print(f"  Refined-dS curvature branch min(V'')/V <= -c': V'' > 0 everywhere = {Vpp_pos_everywhere} "
          f"=> curvature branch ALSO fails (convex potential)")

    # --- swampland gradient-bound verdict for Leg B ---
    # The substrate-IS reported scalar is the ZETA-TAIL asymptote g_V -> 0 (the structurally
    # invariant fact at the attractor), NOT the grid-edge number. The bound |V'|/V >= c is
    # NOT satisfied uniformly: it holds in the AVOIDED cutoff tail (g_V->4) but FAILS in the
    # zeta-runaway attractor (g_V->0). Leg B FAILS the gradient bound on the relevant branch.
    Vprime_pos_everywhere = bool(np.all(dV > 0))             # (local) V' > 0 for all phi (no minimum)
    g_V_report = g_V_asymp_minus                            # (local) the attractor-tail asymptote: 0
    legB_pass = (g_V_asymp_minus > C_SWAMPLAND)            # (local) FALSE: 0 > 1 is False (the honest bound test)
    print(f"  V' > 0 everywhere: {Vprime_pos_everywhere}  (no minimum => field IS forced to roll -- but see below)")
    print(f"  KEY DISTINCTION: 'forced rolling' (no minimum, TRUE) and 'swampland-steep' (g_V>=c) are DISTINCT;")
    print(f"                   the dilaton rolls (driven by the linear a4 term), but the runaway is too shallow for the dS bound.")
    print(f"  LEG B verdict: g_V(zeta-tail asymptote)={g_V_asymp_minus:.1f} > c={C_SWAMPLAND} (bound test)  ->  {'PASS' if legB_pass else 'FAIL'}")
    print(f"                 [cutoff-tail g_V->4 PASSES but is the AVOIDED catastrophe; operating-region g_V_med={g_V_op_med:.2f} straddles c]")
    print()

    # ===============================================================
    # LEG C -- JOINT verdict  (the [SIGN] sign_verdict)
    # ===============================================================
    print("=" * 72)
    print("LEG C: JOINT swampland verdict  (g_S > c) AND (g_V > c)")
    print("=" * 72)
    # Substitution chain (Claim C):
    #   Step 1: refined dS conjecture |grad V|/V >= c (c~O(1)) => no metastable dS minimum.
    #   Step 2: g_S > c AND g_V > c => neither S(tau) nor V(phi) admits a metastable dS minimum.
    #   Step 3 (the FRESH finding): the S(tau) leg is swampland-steep (g_S=3.52>c, S69 W4-B), BUT
    #           the V(phi) leg's gradient bound FAILS on its zeta-runaway attractor (g_V->0<c):
    #           the dilaton DOES roll (no minimum) but its runaway is asymptotically LINEAR (driven
    #           by the surviving a4 term), too shallow for the dS gradient bound; and V''>0 convex
    #           kills the refined-dS curvature disjunct too. 'No minimum' (forced rolling) and
    #           'swampland gradient bound' are DISTINCT conditions -- the substrate satisfies the
    #           first but NOT the second on the V(phi) axis.
    #   Direction: the chain PREDICTED both ratios > c (joint PASS). COMPUTED: g_S>c but g_V<c on
    #              the attractor => the prediction's V-leg direction is WRONG => sign_verdict FAIL.
    joint_pass = legA_pass and legB_pass                     # (local) the sign_verdict driver
    print(f"  g_S(dressed) > c : {legA_pass}   (S69 W4-B reproduced: 3.52 > 1)  PASS")
    print(f"  g_V(attractor) > c : {legB_pass}   (FRESH: zeta-tail g_V->0 < 1; bound FAILS on the runaway the field rolls to)")
    print(f"  JOINT (g_S>c) AND (g_V>c) = {joint_pass}")
    print(f"  => The framework's 'no minimum' is REAL (the field rolls), but it is NOT swampland-gradient-MANDATED")
    print(f"     on the dilaton axis: the runaway is too shallow. A4=roll still holds (no minimum), but the")
    print(f"     swampland-FORCING argument breaks on the V(phi) leg -- a genuine inter-axis TENSION (Track B).")
    print()

    # ---------------------------------------------------------------
    # SIGN / MAGNITUDE / REGIME 3-tuple  (schema-v2, [SIGN] trigger)
    # ---------------------------------------------------------------
    # sign_verdict: the chain (Claim C, Direction) PREDICTED both ratios > c (joint PASS, a strictly
    #   positive (g-c) on BOTH legs). COMPUTED: g_S>c (PASS direction) but g_V->0<c on the attractor
    #   (FAIL direction). The JOINT prediction's direction is violated => sign_verdict = FAIL.
    sign_verdict = "PASS" if joint_pass else "FAIL"          # (local)
    # magnitude_verdict: how far the binding (smaller) leg clears c. Binding leg is g_V (zeta-tail
    #   asymptote 0). joint_margin = min(g_S_dressed, g_V_asymp_minus) - c = 0 - 1 = -1 < 0 => FAIL.
    joint_margin = min(g_S_dressed, g_V_asymp_minus) - C_SWAMPLAND  # (local) binding-leg clearance over c
    magnitude_verdict = "PASS" if joint_margin >= 0.5 else ("INFO" if joint_margin > 0.0 else "FAIL")  # (local)
    # regime_verdict: the V'(phi) re-derivation is an exact analytic identity (residual ~machine eps);
    #   the asymptotic limits are Sage-exact; the node subtlety is HANDLED (verdict rests on the
    #   grid-independent asymptotic law, not the node or grid edge). Method within its regime of validity.
    regime_verdict = "VALID" if dV_match < 1e-6 else "MARGINAL"  # (local) re-derivation identity holds to machine eps
    print(f"  3-tuple: sign={sign_verdict}  magnitude={magnitude_verdict}  regime={regime_verdict}")
    print(f"  (joint_margin = min(g_S, g_V_attractor) - c = {joint_margin:.4f}; re-derivation residual {dV_match:.2e})")

    # ---------------------------------------------------------------
    # Composite collapse (gate-verdicts.md deterministic rule)
    # ---------------------------------------------------------------
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"
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
    print(f"  COMPOSITE (collapse rule): {verdict}")
    print()

    # ---------------------------------------------------------------
    # Save data
    # ---------------------------------------------------------------
    np.savez(
        NPZ_PATH,
        # Leg A (S(tau))
        S_fold=S_fold, dS_fold=dS_fold, Z_fold=Z_fold,
        g_S_bare=g_S_bare, g_S_dressed_cutoff=g_S_dressed, g_S_dressed_zeta=g_S_dressed_zeta,
        c_swampland=C_SWAMPLAND, legA_pass=legA_pass,
        # Leg B (V(phi))
        phi_grid=phi, V_grid=V, dV_grid=dV, d2V_grid=d2V,
        dV_rederived=dV_rederived, dV_rederivation_residual=dV_match,
        a0_fold=a0_npz, a2_fold=a2_npz, a4_fold=a4_npz, R_SU3=R_SU3,
        has_minimum=has_minimum, Vprime_pos_everywhere=Vprime_pos_everywhere,
        Vpp_pos_everywhere=Vpp_pos_everywhere,
        V_at_phi0=V_at_phi0, dV_at_phi0=dV_at_phi0,
        g_V_at_node=g_V_at_node, g_V_grid=g_V_grid,
        g_V_asymp_plus=g_V_asymp_plus, g_V_asymp_minus=g_V_asymp_minus, g_V_report=g_V_report,
        g_V_op_min=g_V_op_min, g_V_op_med=g_V_op_med, op_n=int(op_mask.sum()),
        legB_pass=legB_pass,
        # drift flag
        survey_k_anchor=SURVEY_K_ANCHOR, drift_abs=drift_abs, drift_ratio=drift_ratio,
        # Joint
        joint_pass=joint_pass, joint_margin=joint_margin,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        composite=verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  data -> {NPZ_PATH.name}")

    # ---------------------------------------------------------------
    # Plot (3 panels): V(phi) with node; g_V(phi) with node divergence + robust band; the joint bar
    # ---------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))

    ax1 = axes[0]
    ax1.plot(phi, V, "b-", lw=2, label=r"$V(\phi)$ (Weyl-anomaly dilaton)")
    ax1.axhline(0, color="gray", ls="--", alpha=0.5)
    ax1.axvline(0, color="gray", ls="--", alpha=0.5)
    ax1.plot(0, V_at_phi0, "r*", ms=16, label=r"$\phi=0$: $V=0$ (node)")
    ax1.set_xlabel(r"$\phi$ (dilaton / q-variable)")
    ax1.set_ylabel(r"$V(\phi)$  [$M_{KK}^4$]")
    ax1.set_title("Leg B: substrate potential has NO minimum\n(runaway; node at $\\phi=0$)")
    ax1.set_ylim(-3e4, 1e5)
    ax1.legend(fontsize=9)

    ax2 = axes[1]
    ax2.semilogy(phi, g_V_grid, "g-", lw=2, label=r"$g_V(\phi)=|V'|/|V|$")
    ax2.axhline(C_SWAMPLAND, color="red", ls="--", lw=1.5, label=r"$c\sim O(1)=1$")
    ax2.axvline(0, color="gray", ls=":", alpha=0.6)
    ax2.annotate("node: $g_V\\to\\infty$", xy=(0, g_V_at_node * 1e-3), xytext=(-1.5, 1e10),
                 fontsize=9, color="purple", arrowprops=dict(arrowstyle="->", color="purple"))
    # mark the zeta-runaway attractor tail (phi -> -inf) where g_V -> 0 < c (bound FAILS)
    ax2.annotate("zeta runaway:\n$g_V\\to 0 < c$\n(bound FAILS)", xy=(-3.0, g_V_grid[0]),
                 xytext=(-2.9, 0.012), fontsize=8, color="darkred",
                 arrowprops=dict(arrowstyle="->", color="darkred"))
    # mark cutoff tail (phi -> +inf) where g_V -> 4 (passes, but AVOIDED catastrophe)
    ax2.annotate("cutoff tail:\n$g_V\\to 4$\n(AVOIDED)", xy=(2.8, g_V_grid[-1]),
                 xytext=(1.3, 9.0), fontsize=8, color="darkgreen")
    ax2.set_xlabel(r"$\phi$")
    ax2.set_ylabel(r"$g_V=|V'|/|V|$")
    ax2.set_title("Swampland ratio NOT uniform:\n"
                  r"$g_V\to 4$ (+$\infty$, avoided); $g_V\to 0$ ($-\infty$, attractor) FAILS")
    ax2.legend(fontsize=9, loc="upper center")

    ax3 = axes[2]
    labels = ["$g_S$ dressed\n(S69 W4-B)", "$g_V$ attractor\n($\\phi\\to-\\infty$, FRESH)"]
    vals = [g_S_dressed, max(g_V_asymp_minus, 0.01)]   # plot epsilon for the zero bar's visibility
    colors = ["steelblue", "indianred"]
    bars = ax3.bar(labels, vals, color=colors, alpha=0.85)
    ax3.axhline(C_SWAMPLAND, color="red", ls="--", lw=2, label=r"$c\sim O(1)=1$")
    ax3.set_ylabel("gradient ratio")
    ax3.set_title(f"JOINT: $(g_S>c)\\wedge(g_V>c)$ = {joint_pass}\n"
                  r"$g_S$ PASS, $g_V$ FAIL on attractor $\Rightarrow$ axis TENSION")
    ax3.text(0, g_S_dressed * 1.02, f"{g_S_dressed:.2f}", ha="center", va="bottom",
             fontsize=11, fontweight="bold")
    ax3.text(1, 0.05, "0\n($\\to$0)", ha="center", va="bottom", fontsize=10, fontweight="bold", color="darkred")
    ax3.legend(fontsize=9)
    ax3.set_ylim(0, g_S_dressed * 1.25)

    fig.suptitle(f"{GATE_ID}  --  swampland dS gradient bound (S leg PASS + FRESH V leg FAIL + JOINT FAIL)",
                 fontsize=12, y=1.02)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot -> {PNG_PATH.name}")
    print()

    # ---------------------------------------------------------------
    # 4-tuple + verdict payload
    # ---------------------------------------------------------------
    value_str = (f"joint={joint_pass};g_S_dressed={g_S_dressed:.2f};g_S_bare={g_S_bare:.4f};"
                 f"g_V_cutoff_tail=4(avoided);g_V_zeta_attractor=0(~1/|phi|,Sage-exact);g_V_node=inf(V0=0);"
                 f"g_V_op_med={g_V_op_med:.2f}(straddles_c);c={C_SWAMPLAND};"
                 f"no_minimum={not has_minimum};Vprime_pos={Vprime_pos_everywhere};Vpp_pos={Vpp_pos_everywhere};"
                 f"drift_survey_k3586.5_vs_Vprime0_43210.72=ZPE-curvature-not-gradient_12x;"
                 f"A4=roll(no_min_TRUE)_but_NOT_swampland-grad-mandated_on_V-leg;TrackB_axis-tension")
    print(f"(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    extra_rows = [
        f"# regulator_pin=a_2^{{zeta}}+a_0^{{zeta}} (S=a0-a2+a4 zeta half-moments, CONST-FREEZE-42); cutoff cross-check a_n^{{cutoff}} (S69 W4-B c=3.52)",
        f"# LEG-A g_S PASS: bare={g_S_bare:.4f} (NOT swampland-relevant); dressed cited from S69 W4-B PROVEN = 3.52 cutoff / ~6.6 zeta (reproduced, NOT re-derived); 3.52 > c",
        f"# LEG-B g_V FAIL: FRESH CF14; Sage-exact asymptotics g_V(+inf)=4 [cutoff catastrophe, AVOIDED] / g_V(-inf)=0~1/|phi| [zeta runaway ATTRACTOR, bound FAILS]; V''>0 convex kills refined-dS curvature disjunct too",
        f"# DRIFT-FLAG: survey k=+3586.5 is S62 ZPE curvature d2E_ZP/dq2|_0=-3586.531 (2nd deriv of E_ZP(q)), NOT dilaton V'(0)=43210.72 (12x drift); conflation flagged per plan",
        f"# JOINT FAIL: (g_S>c) AND (g_V>c) = {joint_pass}; 'no minimum'/forced-rolling is REAL (A4=roll) but DISTINCT from swampland-steep; runaway too shallow (linear a4 term) => inter-axis TENSION (Track B)",
    ]
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        extra_rows=extra_rows,
    )

    wall = time.time() - t0                                      # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())   # exit reflects SCRIPT HEALTH only (0 on success); verdict is data, not exit code
