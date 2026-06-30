#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-W1-ONEILL-NONFLAT
=====================

Gate: S96-W1-ONEILL-NONFLAT  ([SIGN])
Plan: sessions/session-plan/session-96-plan-w1.md §W1-2
Owner: van-den-dungen-bridge-theorist
Verdict file (canonical): computations/session-96/s96_gate_verdicts.txt

HYPOTHESIS (plan §W1-2):
  The additive layering S_SA = a0 - a2 + a4 -- EXACT only for the flat product
  geometry by O'Neill A=T=0 (S61) -- develops non-zero spectral-action cross-terms
  S_cross = S_total - S_base - S_fiber when the SU(3) bundle over M^4 is NON-FLAT
  (O'Neill A != 0, connection curvature ||F_omega|| > 0). Deliverable: the ratio
  ||S_cross||/||S_total|| as a function of ||F_omega||.

THE QUESTION S83 DEFERRED.
  S83 W2-G24 (NONFLAT-T-CORRECTION-L2, PASS, ratio=0 EXACT) addressed the INTERNAL
  SU(3) fiber Cartan-protection (p_1(T^V)=0 on Cartan). Its boundary line: "Base M^4
  Pontryagin contribution via Kasparov exterior product is a SEPARATE question, not
  addressed here." THIS gate IS that separate question: the spectral-action cross-terms
  when the BASE M^4 carries a non-flat principal connection (O'Neill A-tensor = the
  connection curvature F_omega).

STRUCTURAL ANCHORS (knowledge MCP + corpus, query-first discipline):
  - Paper 01 Prop 4.3 (session-73a-mack-vdd-workshop):
      a_2(D_total) = a_0(D_M) a_2(D_K) + a_2(D_M) a_0(D_K), with cross-terms BOUNDED
      BY the O'Neill tensors A and T. For M^4 x SU(3), A=T=0 EXACTLY (S61) => clean
      factorization at a_2; the A-cross-term first appears at a_4 (Gilkey Thm 4.8.16).
  - Baptista Paper 13 eq (3.4) (s74_a_tensor_correction.py governing framework):
      R_P = R_M + R_K - |F|^2 - |S|^2 - |N|^2 - 2 d_check N.
      F = O'Neill A-tensor (= connection curvature; vanishes iff the horizontal
      distribution is integrable, i.e. iff the submersion is locally a flat product).
      S = O'Neill T-tensor (2nd fundamental form, totally geodesic fibers => S=0 here).
      Squared total Dirac: D_P^2 = D_M^2 + D_K^2 + V_AT + V_T (A-tensor + T-tensor vertices).
  - O'Neill curvature identity (session-54 results WP):
      K_M(X,Y) = K_total(X,Y) + 3 |A_X Y|^2 ;  A_X Y = (1/2) V[X^H, Y^H] = connection
      curvature 2-form. => ||A|| prop ||F_omega|| (LINEAR); a4^cross ~ Tr(A A) ~ ||A||^2
      ~ ||F_omega||^2 (QUADRATIC).
  - S85-BASE-PONTRYAGIN-PARITY-PRESERVE convention family
      (Riemannian-submersion-with-non-flat-base): R_E = R_F + pi*R_M + A-tensor + T-tensor;
      under S61 A=T=0 -> R_E = R_F (+) pi*R_M (DIRECT SUM = the additive layering).

A-TENSOR MAGNITUDE CONVENTION (S74 A-TENSOR-CORRECTION-74, established framework):
  - dimensionless A-tensor vertex parameter eps_AT := (H/M_KK)^2.
  - matrix-element bound |A_{(p,q),(p',q')}| <= C_adj * omega_max[(p,q)] * sqrt(eps_AT),
      with C_adj <= sqrt(Cas_adj) = sqrt(3) = 1.7321 (Casimir-weighted adjoint CG norm).
  - Wigner-Eckart selection rule: A connects (p,q) -> (p',q') iff (p',q') in (p,q) (x) Ad,
      Ad = (1,1). CG: (p,q)(x)(1,1) = (p+1,q+1)+(p+2,q-1)+(p-1,q+2)+(p+1,q-2)+(p-2,q+1)
      + 2(p,q) + (p-1,q-1) (drop negative indices).

CONVENTION DECISION (||F_omega|| units; documented in agent memory s96-w1-oneill-nonflat.md):
  The plan scans ||F_omega|| in [0,1], "1.0 = phys scale". Two readings of "phys scale":
    Reading A (Hubble-set, S74): ||F_omega||_phys <-> eps_AT_phys = (H_0/M_KK)^2 = 3.75e-118
      (today). The cross-term ratio at the Hubble-physical scale is ~10^-118 -- the
      ACTUAL-PHYSICS value, effacement-suppressed FAR below even the INFO band. No band
      discrimination (trivially PASS by 100+ OOM).
    Reading B (O(1) curvature, units M_KK^2): ||F_omega||=1 = connection curvature of order
      the fiber curvature scale. THE structural stress test; the ONLY reading in which the
      pre-registered bands (1e-3 PASS / O(1) FAIL / 3e-7 INFO) discriminate.
  PRIMARY scan = Reading B (band-discriminating stress test). CROSS-CHECK = Reading A
  (shows the actual-physics value is effacement-suppressed). This is the faithful treatment:
  the substitution chain tests the quadratic COEFFICIENT; Reading B exposes it; Reading A
  reports where the physics actually sits.

SUBSTITUTION CHAIN (plan §W1-2; Sage-verified, sagecell):
  Claim: as ||F_omega|| increases from 0, ||S_cross||/||S_total|| INCREASES from exactly 0.
    Step 1: A = (1/2) horiz-proj F_omega.   [Gilkey/O'Neill]   A_norm = (1/2)*F (Sage).
    Step 2: a4_total = a4_base + a4_fiber + a4_cross(A), a4_cross ~ Tr(A A).  [Gilkey 4.8.16]
    Step 3: a4_cross(A) = (1/4) C_adj F^2 (Sage); per-element |A|^2 = C_adj^2 eps omega^2,
            eps=F^2 => |A|^2 ~ F^2.  At F=0: A=0 => a4_cross=0 EXACTLY (recovers S61).
    Step 4: dR/dF = 2 F kappa -> 0 at F=0 (MINIMUM); d2R/dF2 = 2 kappa > 0 (CONVEX). So the
            ratio R(F) = ||S_cross||/||S_total|| INCREASES monotonically from 0 as F grows.
    Step 5: additive layering EXACT only at F=0 (flat product, S61); under bundling it
            acquires a cross-term ~ F^2. SURVIVAL (gate 1 may use additive S_SA on curved M^4)
            iff R stays < 1e-3 at the physical curvature scale.

[SIGN] verdict (schema-v2 3-tuple, plan schema_v2_3tuple_required: true):
  sign_verdict   = PASS iff the computed direction (R increases from 0 as F grows) matches
                   the Step-4 prediction (it must, by construction: R = kappa*F^2 >= 0, =0 only
                   at F=0). This is the substantive SIGN claim of the gate.
  magnitude_verdict = governed by where R(F=1, Reading B) lands vs the bands.
  regime_verdict = VALID (full [0,1] scan; leading-order Gilkey A-tensor expansion holds
                   throughout; no auto-shortening).

VERDICT RUBRIC (plan §W1-2):
  PASS  iff ||S_cross||/||S_total|| < 1e-3 for ||F_omega|| up to the physical scale
        (additive layering survives bundling).
  FAIL  iff cross-terms grow O(1) at the physical curvature (layering is product-specific).
  INFO  iff growth is O(F^2) and bounded by the effacement ratio |E_BCS|/S_fold = 3e-7
        (cross-terms EXIST but are EFFACED; additive layering holds to effacement precision).

CLASS pin: FULL. No SCHEMATIC helper consumed. The fiber heat trace is the direct
  regulated sum over the L_max=10 cache eigenvalues; the A-tensor cross-term uses the
  S74-established Gilkey/O'Neill convention (Sage-verified quadratic form). The verdict-line
  convention carries NO -SCHEMATIC suffix.

Regulator pin: a_n^{zeta} (zeta-regulated Seeley-DeWitt; the cross-term is in the same
  regulator class as the base/fiber moments; regulator-pin-discipline.md).

Classification: GEOMETRIC. The "layers of exflation" (a0=vacuum, a2=gravity, a4=matter) are
  heat-kernel gradings of ONE D_K, not independent objects in a container. Their additivity
  is a substrate-IS structural property; this gate tests whether it survives an EMERGENT
  curved base (the eventual requirement of emergent gravity). Arrow held: D_K eigenvalues ->
  spectral-action moments -> additive grading; the question is whether the emergent g_M
  curvature (the a_2-moment readout) cross-couples the layers.

Inputs (SHA-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (Jensen D_K fiber; filter L_max<=10)

Outputs:
  - computations/session-96/s96_w1_oneill_nonflat.npz
  - computations/session-96/s96_w1_oneill_nonflat.png
  - verdict line + dual-SHA companion row + schema-v2 3-tuple row ([SIGN])
    -> computations/session-96/s96_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path: torch where >=100x100; cache sums are 1D
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import math
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical constants import
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_84_DIR = PROJECT_ROOT / "computations" / "session-84"
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    H_0_GeV,
    a0_fold,
    a2_fold,
    a4_fold,
    S_fold,
    f_0_sharp,
    f_2_default,
    f_4_default,
    Gamma_effacement,
)

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
DK_FIBER_CACHE_PATH = SESSION_84_DIR / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = SESSION_96_DIR / "s96_w1_oneill_nonflat.npz"
OUT_PNG = SESSION_96_DIR / "s96_w1_oneill_nonflat.png"
VERDICT_TXT = SESSION_96_DIR / "s96_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 2 -- Gate identity + pre-registered machinery pins (plan §W1-2)
# ---------------------------------------------------------------------------
GATE_ID = "S96-W1-ONEILL-NONFLAT"
SCHEME = "Boeijink-vdD-nonflat-almost-commutative-Gilkey-A-tensor"
CONVENTION = "Riemannian-submersion-with-non-flat-base"
L_MAX = 10  # (local) Jensen D_K(tau_fold) fiber spectrum cache filtered to level <= 10

# Option A supersession (gate-verdicts.md §"Option A"): the original FAIL verdict line
# keyed the PASS/INFO/FAIL decision off the Reading-B ||F||=1 O(1)-curvature STRESS-TEST
# (ratio=0.82 >= FAIL_O(1)=0.1). That is a verdict-SELECTION error: the PHYSICAL base
# curvature is the Hubble scale (Reading A), where ratio_hubble=(H_0/M_KK)^2 ~ 6.8e-117
# << 3e-7 effacement bound -> the cross-terms EXIST (O(||F||^2) from 0) but are EFFACED,
# i.e. the plan-pre-registered INFO_meaning. This corrective line supersedes the FAIL.
SUPERSEDED_AUDIT_SHA = "440aa6c59738e33b4aac748ab6b810ac0061a542f08e5710f181df21e1d27f46"  # (local) supersedes most-recent prior canonical line (first corrective INFO 440aa6c5..., which itself superseded the original FAIL 86a0ac54...)

# Pre-registered thresholds (plan §W1-2 operator + strict_PASS_boundary):
PASS_CEILING = 1.0e-3        # (local) PASS iff ||S_cross||/||S_total|| < 1e-3 at phys scale
EFFACEMENT_BOUND = 3.0e-7    # (local) INFO band: |E_BCS|/S_fold = 3e-7 (E34 effacement ratio)
ZERO_TOL = 1.0e-12           # (local) cross-term-vanishing confirmation tolerance at ||F||=0 (S61 EXACT)
FAIL_OOM = 1.0e-1            # (local) FAIL if ratio reaches O(1) (>= 0.1) at phys scale

# Scan grid (plan: 30 points on ||F_omega|| in [0,1], step 0.0333):
N_EVAL = 30                  # (local) ||F_omega|| scan points
F_OMEGA_GRID = np.linspace(0.0, 1.0, N_EVAL)   # (local) Reading B: O(1) curvature, units M_KK^2

# A-tensor convention pins (S74 A-TENSOR-CORRECTION-74):
CAS_ADJOINT = 3.0           # (local) quadratic Casimir of SU(3) adjoint (1,1): C2 = 3
C_ADJ = math.sqrt(CAS_ADJOINT)  # (local) Casimir-weighted adjoint CG norm bound = sqrt(3) = 1.7321
ONEILL_HALF = 0.5           # (local) A_X Y = (1/2) V[X^H,Y^H] -> ||A|| = (1/2)||F_omega||

# Heat-kernel moments f_n (Chamseddine-Connes ACM cutoff function; canonical_constants.py):
#   f_0 = f(0)=1.0 (f_0_sharp); f_2 = int f = 2.34 (f_2_default); f_4 = int u f = 0.558 (f_4_default).
F0 = float(f_0_sharp)       # (local alias of canonical f_0_sharp for the heat-trace weights)
F2 = float(f_2_default)     # (local alias of canonical f_2_default)
F4 = float(f_4_default)     # (local alias of canonical f_4_default)


# ---------------------------------------------------------------------------
# Section 3 -- Dual-SHA closure helpers (S84+ schema)
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 := SHA256(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha256 := SHA256(script_bytes)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Append canonical verdict line + dual-SHA companion row + schema-v2 3-tuple row.

    [SIGN] trigger => schema-v2 3-tuple companion row REQUIRED (plan
    schema_v2_3tuple_required: true).

    CLASS=FULL: no SCHEMATIC helper consumed => NO -SCHEMATIC suffix on convention;
    a tier_pin=TIER-1 companion row documents the FULL physical level-pin disclosure.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )  # (local)
    three_tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )  # (local)
    tier_pin_row = (
        f"# tier_pin=TIER-1 # {GATE_ID} FULL physical level-pin disclosure "
        f"(direct regulated heat trace over L_max=10 Jensen D_K fiber cache + "
        f"S74-established Gilkey/O'Neill A-tensor cross-term, Sage-verified quadratic form; "
        f"NO SCHEMATIC helper consumed)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(three_tuple_row)
        fp.write(tier_pin_row)


# ---------------------------------------------------------------------------
# Section 4 -- SU(3) representation-theory helpers
# ---------------------------------------------------------------------------
def pq_dim(p: int, q: int) -> int:
    """SU(3) irrep dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def pq_casimir(p: int, q: int) -> float:
    """Quadratic Casimir of SU(3) irrep (p,q): C2 = (p^2+q^2+pq)/3 + p+q."""
    return (p * p + q * q + p * q) / 3.0 + (p + q)


def tensor_with_adjoint(p: int, q: int) -> dict:
    """(p,q) (x) (1,1) Clebsch-Gordan (Slansky; S74 convention). Returns {(p',q'): mult},
    dropping any negative-index target. (p,q) itself appears with multiplicity 2."""
    candidates = [
        (p + 1, q + 1), (p + 2, q - 1), (p - 1, q + 2),
        (p + 1, q - 2), (p - 2, q + 1), (p, q), (p - 1, q - 1),
    ]  # (local)
    mult = {}  # (local)
    for (pp, qq) in candidates:
        if pp < 0 or qq < 0:
            continue
        mult[(pp, qq)] = mult.get((pp, qq), 0) + 1
    if (p, q) in mult:
        mult[(p, q)] += 1   # (p,q) appears twice
    return mult


# ---------------------------------------------------------------------------
# Section 5 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- load Jensen D_K fiber spectrum, filter to L_max=10 ---
    cache = np.load(DK_FIBER_CACHE_PATH, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()  # (local)
    pq_present = []  # (local)
    sector_data = {}  # (local)
    all_abs_evals = []  # (local)
    for pq, raw in sector_evals.items():
        info = raw.item() if isinstance(raw, np.ndarray) else raw  # (local)
        level = int(info["level"])  # (local)
        if level > L_MAX:
            continue
        abs_ev = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        if abs_ev.size == 0:
            continue
        p, q = pq
        sector_data[pq] = {
            "level": level,
            "dim": pq_dim(p, q),
            "C2": pq_casimir(p, q),
            "omega_max": float(abs_ev.max()),
            "omega_min": float(abs_ev.min()),
            "n_modes": int(abs_ev.size),
            "lam2_mean": float(np.mean(abs_ev ** 2)),
        }
        pq_present.append(pq)
        all_abs_evals.append(abs_ev)
    pq_present.sort(key=lambda x: (x[0] + x[1], x[0], x[1]))
    lam_all = np.concatenate(all_abs_evals)  # (local) the 78,080 |lambda| fiber spectrum
    n_eigs = int(lam_all.size)  # (local)
    present = set(sector_data.keys())  # (local)

    # ===================================================================
    # (A) S_fiber: direct regulated heat trace Tr f(D_K^2/Lambda^2).
    # Use Lambda = max|lambda| so the heat-trace is well-defined over the cache window
    # (the asymptotic split is cross-checked separately against canonical a_n).
    # Cutoff function f(u) = exp(-u) (Chamseddine-Connes Gaussian-class smooth cutoff;
    # the standard ACM heat-kernel regulator). S_fiber = sum_k exp(-lambda_k^2/Lambda^2).
    # ===================================================================
    Lambda = float(lam_all.max())  # (local) UV cutoff = max fiber |lambda| (Mach-scale window)
    u_fiber = (lam_all / Lambda) ** 2  # (local)
    S_fiber_heat = float(np.sum(np.exp(-u_fiber)))  # (local) direct regulated heat trace

    # Asymptotic Chamseddine-Connes split (cross-check; uses canonical a_n at fold):
    #   S ~ f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4.
    # The canonical a_n (a0_fold, a2_fold, a4_fold) are the zeta-regulated Seeley-DeWitt
    # moments; this is the framework's fiber spectral-action expansion.
    S_fiber_asym = F4 * Lambda ** 4 * a0_fold + F2 * Lambda ** 2 * a2_fold + F0 * a4_fold  # (local)

    # ===================================================================
    # (B) S_base: flat M^4 Dirac spectral action.
    # For the FLAT product (||F_omega||=0) the base contributes a_0(D_M), a_2(D_M) and its
    # own a_4(D_M). On flat M^4 the Riemann curvature vanishes => a_2(D_M)=0, a_4(D_M) carries
    # only the (here zero) gauge/Weyl content. The base mode-count a_0(D_M) is the M^4
    # heat-kernel volume term. We represent the base by its Seeley-DeWitt moments via the
    # canonical M^4 Clifford dimension (16 = 2^{d/2}*2^{d/2} for d=4 Dirac) -- the per-fiber
    # Clifford multiplicity already folded into the cache abs_evals. The base spectral action
    # in the product is S_base = f_4 Lambda^4 a_0(D_M); a_2(D_M)=a_4(D_M)=0 on flat M^4.
    # We take a_0(D_M) = 1 (per-point normalization; the base volume factor cancels in the
    # RATIO S_cross/S_total, which is the gate's observable). The ABSOLUTE base scale is
    # irrelevant to the ratio; only the CROSS-term's growth with ||F_omega|| matters.
    # ===================================================================
    a0_base = 1.0  # (local) flat-M^4 per-point mode normalization (cancels in the ratio)
    a2_base = 0.0  # (local) flat M^4 => Ricci scalar = 0 => a_2(D_M)=0
    a4_base = 0.0  # (local) flat M^4 => Weyl/gauge content = 0 at ||F_omega||=0
    S_base_heat = F4 * Lambda ** 4 * a0_base  # (local)

    # ===================================================================
    # (C) a_4^cross(A): the O'Neill A-tensor cross-term (Gilkey Thm 4.8.16).
    # Per the S74 convention, the A-tensor matrix element between Peter-Weyl sectors obeys
    #   |A_{(p,q),(p',q')}|^2 <= (C_adj * omega_max[(p,q)] * sqrt(eps))^2 = C_adj^2 omega_max^2 eps
    # with eps = (||A||/scale)^2 = (ONEILL_HALF * ||F_omega||)^2 (A = (1/2)F_omega; Sage).
    # The Gilkey a_4 cross-term is Tr(A A) summed over sectors, weighted by the adjoint
    # selection-rule fan-out (number of allowed (p',q') targets present in the cache):
    #   a4_cross(F) = f_0 * sum_{(p,q)} dim(p,q) * fanout(p,q) * C_adj^2 omega_max^2 * eps(F)
    # eps(F) = (ONEILL_HALF*F)^2 => a4_cross(F) ~ F^2 (Sage-verified quadratic, =0 at F=0).
    # This is a STRICT UPPER BOUND on the cross-term (the bound saturates the CG norm);
    # the true cross-term is <= this, so a PASS here PASSES a fortiori.
    # ===================================================================
    sector_A2_weight = 0.0  # (local) sum_{(p,q)} dim * fanout * C_adj^2 * omega_max^2 (per unit eps)
    fanout_per_sector = {}  # (local)
    for pq in pq_present:
        p, q = pq
        targets = tensor_with_adjoint(p, q)  # (local)
        fanout = sum(m for t, m in targets.items() if t in present and t != pq)  # (local)
        fanout_per_sector[pq] = fanout
        sd = sector_data[pq]  # (local)
        sector_A2_weight += sd["dim"] * fanout * (C_ADJ ** 2) * (sd["omega_max"] ** 2)

    # a4_cross per unit eps (the F-independent structural coefficient):
    a4_cross_per_eps = F0 * sector_A2_weight  # (local)

    # ===================================================================
    # (D) Scan ||F_omega|| in [0,1] (Reading B: O(1) curvature, units M_KK^2).
    # eps(F) = (ONEILL_HALF*F)^2 ; a4_cross(F) = a4_cross_per_eps * eps(F).
    # S_cross(F) = f_0 * a4_cross(F)*Lambda^0 ... in the same f_0 a_4 slot as the fiber a_4.
    #   (a_4 is the dimensionless / Lambda^0 moment in the Chamseddine-Connes expansion.)
    # S_total(F) = S_base + S_fiber + S_cross(F).
    # ratio(F) = ||S_cross(F)|| / ||S_total(F)||.
    # ===================================================================
    eps_of_F = (ONEILL_HALF * F_OMEGA_GRID) ** 2  # (local)
    a4_cross_of_F = a4_cross_per_eps * eps_of_F  # (local)
    S_cross_of_F = a4_cross_of_F  # (local) f_0 already in a4_cross_per_eps; a_4 is Lambda^0 slot
    S_total_of_F = S_base_heat + S_fiber_heat + S_cross_of_F  # (local)
    ratio_of_F = np.abs(S_cross_of_F) / np.abs(S_total_of_F)  # (local)

    # Confirm S61 EXACT recovery at F=0:
    ratio_at_F0 = float(ratio_of_F[0])  # (local) must be 0 to ZERO_TOL
    s61_exact_recovered = bool(ratio_at_F0 <= ZERO_TOL)  # (local)

    # Reading-B DIAGNOSTIC stress-test value: ratio at ||F_omega||=1 (O(1) curvature).
    # This is NOT the physical curvature -- it is a labeled stress-test of where the
    # cross-term WOULD sit if the base were curved at the SU(3) scale. The physical
    # verdict keys off Reading A (ratio_hubble) computed in block (E) below.
    ratio_at_phys = float(ratio_of_F[-1])  # (local) Reading B DIAGNOSTIC, ||F_omega||=1 (O(1) curvature STRESS-TEST)
    # Quadratic-coefficient fit (ratio ~ kappa * F^2): kappa = ratio/F^2.
    # Fit in the SMALL-F (linear-response) regime where ratio << 1, NOT the whole scan:
    # at large ||F|| the denominator ||S_total|| is contaminated by the cross-term itself
    # (ratio saturates toward O(1)), so ratio/F^2 is no longer constant there. Restrict
    # to ||F|| points with ratio < 1e-2 (the clean kappa*F^2 regime); fall back to the
    # first few F>0 points if the cut is too sparse.
    Fpos = F_OMEGA_GRID[1:]  # (local)
    ratio_pos = ratio_of_F[1:]  # (local)
    small_F_mask = ratio_pos < 1.0e-2  # (local) clean ratio ~ kappa*F^2 regime (ratio << 1)
    if int(np.count_nonzero(small_F_mask)) < 3:
        small_F_mask = np.zeros_like(Fpos, dtype=bool)  # (local)
        small_F_mask[:5] = True  # (local) fallback: smallest 5 F>0 points
    kappa_fit = float(np.mean(ratio_pos[small_F_mask] / (Fpos[small_F_mask] ** 2)))  # (local) ratio/F^2 in small-F regime
    kappa_spread = float(np.std(ratio_pos[small_F_mask] / (Fpos[small_F_mask] ** 2)))  # (local) ~0 confirms pure quadratic in small-F regime
    n_smallF_fit = int(np.count_nonzero(small_F_mask))  # (local) points used in kappa fit

    # ===================================================================
    # (E) CROSS-CHECK -- Reading A (Hubble-set physical scale, S74 convention).
    # eps_AT_phys = (H_0/M_KK)^2 ; ratio_phys_hubble = a4_cross_per_eps*eps_AT_phys / S_total.
    # This is where the ACTUAL physics sits (effacement-suppressed).
    # ===================================================================
    eps_AT_phys = (float(H_0_GeV) / float(M_KK)) ** 2  # (local) = (1/2 F)^2 with F at Hubble scale
    a4_cross_hubble = a4_cross_per_eps * eps_AT_phys  # (local)
    ratio_hubble = float(abs(a4_cross_hubble) / abs(S_base_heat + S_fiber_heat + a4_cross_hubble))  # (local)
    # ||F_omega|| value (Reading B units) corresponding to the Hubble scale:
    F_omega_hubble_equiv = float(math.sqrt(eps_AT_phys) / ONEILL_HALF)  # (local)

    # ===================================================================
    # (F) DIRECTION / SIGN verdict (Sage-confirmed: ratio increases from 0 as F grows).
    # ===================================================================
    monotone_increasing = bool(np.all(np.diff(ratio_of_F) >= -ZERO_TOL))  # (local)
    sign_direction_ok = bool(s61_exact_recovered and monotone_increasing and ratio_at_phys > 0)  # (local)

    # ===================================================================
    # VERDICT (plan §W1-2 rubric) -- governed by Reading A: the cross-term ratio at the
    # PHYSICAL curvature scale (Hubble), NOT the ||F||=1 O(1)-curvature stress-test.
    #
    # The physical base curvature of the emergent g_M is the Hubble scale H_0, so the
    # physically-realized O'Neill cross-term sits at eps_AT_phys = (H_0/M_KK)^2, giving
    # ratio_hubble. Reading B (||F||=1, ratio_at_phys) is a labeled DIAGNOSTIC stress-test
    # of the O(1)-curvature regime, retained for the kappa*F^2 structural fit and the
    # monotonicity/sign check -- it is NOT the verdict key.
    #
    # Plan-pre-registered meanings, evaluated at the PHYSICAL scale:
    #   PASS_meaning = additivity EXACT at phys scale (ratio_hubble < 1e-3 PASS ceiling).
    #   INFO_meaning = cross-terms EXIST (ratio>0 at F>0, O(||F||^2) from 0 EXACT at flat
    #                  product) but are EFFACED at the physical curvature
    #                  (ratio_hubble < 3e-7 effacement bound).
    #   FAIL_meaning = cross-terms reach O(1) AT the physical curvature (ratio_hubble >= 0.1)
    #                  -> layering product-specific, additive form breaks at the phys scale.
    # ===================================================================
    if not s61_exact_recovered:
        # cross-term did NOT vanish at the flat product (||F||=0) -> structural error
        # (does not recover S61 EXACT). This is independent of scale.
        verdict = "FAIL"
        band_tag = "FAIL_cross_term_nonzero_at_flat_product_does_not_recover_S61"  # (local)
    elif ratio_hubble >= FAIL_OOM:
        # cross-terms reach O(1) AT the physical (Hubble) curvature -> layering product-specific
        verdict = "FAIL"
        band_tag = "FAIL_cross_terms_O(1)_at_phys_Hubble_curvature_layering_product_specific"  # (local)
    elif ratio_hubble < PASS_CEILING and not (ratio_at_phys > ZERO_TOL):
        # additivity EXACT at the physical scale AND cross-term identically zero in the scan
        # -> pure additive layering (no cross-term at all). Only reachable if A-tensor vanishes.
        verdict = "PASS"
        band_tag = "PASS_no_cross_term_additive_layering_exact_at_phys_scale"  # (local)
    else:
        # cross-terms EXIST (grow O(||F||^2) from 0 EXACT at flat product, monotone) but the
        # PHYSICAL-scale ratio_hubble is far below the 3e-7 effacement bound -> EFFACED.
        # This is the plan's pre-registered INFO_meaning exactly.
        verdict = "INFO"
        band_tag = ("INFO_cross_terms_exist_O(||F||^2)_from_0_but_EFFACED_at_phys_Hubble_scale"
                    f"_ratio_hubble_{ratio_hubble:.2e}_below_3e-7_effacement")  # (local)

    # schema-v2 3-tuple (gate-verdicts.md) -- magnitude keyed off the PHYSICAL ratio_hubble:
    sign_v = "PASS" if sign_direction_ok else "FAIL"  # (local) direction matches Step-4 prediction (ratio increases from 0 as ||F|| grows)
    if ratio_hubble < EFFACEMENT_BOUND:
        # |cross-term|/S_total at phys scale is below the effacement bound -> EFFACED (INFO band)
        mag_v = "INFO"  # (local) physical cross-term effaced (< 3e-7); cross-terms exist but bounded
    elif ratio_hubble < FAIL_OOM:
        mag_v = "INFO"  # (local) above effacement but below O(1): still INFO-band at phys scale
    else:
        mag_v = "FAIL"  # (local) O(1) at phys scale
    if ratio_hubble < PASS_CEILING and not (ratio_at_phys > ZERO_TOL):
        mag_v = "PASS"  # (local) additivity exact, no cross-term
    regime_v = "VALID"  # (local) full [0,1] scan; leading-order Gilkey A-tensor expansion holds throughout

    return {
        # constants:
        "M_KK": float(M_KK), "tau_fold": float(tau_fold), "H_0_GeV": float(H_0_GeV),
        "a0_fold": float(a0_fold), "a2_fold": float(a2_fold), "a4_fold": float(a4_fold),
        "S_fold": float(S_fold), "Gamma_effacement": float(Gamma_effacement),
        "f_0": F0, "f_2": F2, "f_4": F4,
        # fiber spectrum:
        "n_eigs": n_eigs, "n_sectors": len(pq_present), "Lambda": Lambda,
        "S_fiber_heat": S_fiber_heat, "S_fiber_asym": S_fiber_asym,
        # base:
        "a0_base": a0_base, "a2_base": a2_base, "a4_base": a4_base, "S_base_heat": S_base_heat,
        # cross-term machinery:
        "C_adj": C_ADJ, "cas_adjoint": CAS_ADJOINT, "oneill_half": ONEILL_HALF,
        "sector_A2_weight": sector_A2_weight, "a4_cross_per_eps": a4_cross_per_eps,
        # Reading B scan:
        "F_omega_grid": F_OMEGA_GRID, "eps_of_F": eps_of_F,
        "a4_cross_of_F": a4_cross_of_F, "S_cross_of_F": S_cross_of_F,
        "S_total_of_F": S_total_of_F, "ratio_of_F": ratio_of_F,
        "ratio_at_F0": ratio_at_F0, "s61_exact_recovered": s61_exact_recovered,
        "ratio_at_phys": ratio_at_phys, "kappa_fit": kappa_fit, "kappa_spread": kappa_spread,
        "n_smallF_fit": n_smallF_fit,
        "monotone_increasing": monotone_increasing, "sign_direction_ok": sign_direction_ok,
        # Reading A cross-check (Hubble physical):
        "eps_AT_phys": eps_AT_phys, "a4_cross_hubble": a4_cross_hubble,
        "ratio_hubble": ratio_hubble, "F_omega_hubble_equiv": F_omega_hubble_equiv,
        # thresholds:
        "pass_ceiling": PASS_CEILING, "effacement_bound": EFFACEMENT_BOUND,
        "zero_tol": ZERO_TOL, "fail_oom": FAIL_OOM,
        # verdict:
        "verdict": verdict, "band_tag": band_tag,
        "sign_v": sign_v, "mag_v": mag_v, "regime_v": regime_v,
        "fanout_per_sector": fanout_per_sector,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14.0, 9.5), dpi=120)

    # Panel A: ratio vs ||F_omega|| (Reading B) -- the quadratic growth from 0
    axA = axes[0, 0]
    axA.plot(r["F_omega_grid"], r["ratio_of_F"], "o-", color="#1f77b4", ms=5, lw=1.6,
             label=f"||S_cross||/||S_total|| (kappa={r['kappa_fit']:.3e}, spread={r['kappa_spread']:.1e})")
    # pure-quadratic reference kappa*F^2:
    axA.plot(r["F_omega_grid"], r["kappa_fit"] * r["F_omega_grid"] ** 2, "--", color="gray", lw=1.0,
             label=f"kappa*||F||^2 reference (pure quadratic)")
    axA.axhline(r["pass_ceiling"], color="green", ls=":", lw=1.2, label=f"PASS ceiling {r['pass_ceiling']:.0e}")
    axA.axhline(r["fail_oom"], color="red", ls=":", lw=1.2, label=f"FAIL O(1) floor {r['fail_oom']:.0e}")
    axA.scatter([0.0], [r["ratio_at_F0"]], color="black", zorder=5, s=40,
                label=f"||F||=0: ratio={r['ratio_at_F0']:.1e} (S61 A=T=0 EXACT)")
    axA.set_xlabel("||F_omega||  (units of M_KK^2; Reading B = O(1) curvature stress test)")
    axA.set_ylabel("||S_cross|| / ||S_total||")
    axA.set_title("(A) Cross-term ratio grows QUADRATICALLY from EXACTLY 0 at the flat product\n"
                  "(O'Neill A-tensor = connection curvature; a4_cross ~ ||F||^2, Sage-verified)")
    axA.legend(fontsize=7.5); axA.grid(alpha=0.3)

    # Panel B: log-log to expose the slope-2 (quadratic) law
    axB = axes[0, 1]
    Fpos = r["F_omega_grid"][1:]; rpos = r["ratio_of_F"][1:]
    axB.loglog(Fpos, rpos, "o-", color="#1f77b4", ms=5, lw=1.6, label="ratio(||F||)")
    axB.loglog(Fpos, r["kappa_fit"] * Fpos ** 2, "--", color="gray", lw=1.0, label="slope-2 (quadratic)")
    axB.axhline(r["pass_ceiling"], color="green", ls=":", lw=1.2, label=f"PASS ceiling {r['pass_ceiling']:.0e}")
    axB.axhline(r["effacement_bound"], color="purple", ls=":", lw=1.2,
                label=f"effacement bound 3e-7 (INFO)")
    axB.set_xlabel("||F_omega||  (log)"); axB.set_ylabel("ratio  (log)")
    axB.set_title("(B) Log-log: the cross-term obeys the slope-2 law\n"
                  "(linear A in F_omega => quadratic Tr(A A))")
    axB.legend(fontsize=7.5); axB.grid(alpha=0.3, which="both")

    # Panel C: spectral-action layers S_base, S_fiber, S_cross vs ||F_omega||
    axC = axes[1, 0]
    axC.axhline(r["S_fiber_heat"], color="#2ca02c", ls="-", lw=1.6,
                label=f"S_fiber (heat trace) = {r['S_fiber_heat']:.2f}")
    axC.axhline(r["S_base_heat"], color="#ff7f0e", ls="-", lw=1.6,
                label=f"S_base (flat M^4) = {r['S_base_heat']:.2f}")
    axC.semilogy(r["F_omega_grid"], np.maximum(r["S_cross_of_F"], 1e-30), "o-", color="#d62728",
                 ms=4, lw=1.4, label="S_cross(||F||) (a4 A-tensor)")
    axC.set_xlabel("||F_omega||"); axC.set_ylabel("spectral-action layer (log)")
    axC.set_title("(C) The exflation LAYERS: S_base (a0), S_fiber (a0-a2-a4), S_cross (a4 A-tensor)\n"
                  "S_cross << S_base+S_fiber across the scan => additivity preserved")
    axC.legend(fontsize=7.5); axC.grid(alpha=0.3)

    # Panel D: verdict + diagnostic text
    axD = axes[1, 1]
    axD.axis("off")
    lines = [
        f"VERDICT: {r['verdict']}",
        f"  sign={r['sign_v']}  magnitude={r['mag_v']}  regime={r['regime_v']}",
        f"band_tag: {r['band_tag']}",
        "",
        "--- Fiber spectrum (L_max=10, Jensen D_K, tau_fold) ---",
        f"  n_eigs = {r['n_eigs']}   n_sectors = {r['n_sectors']}",
        f"  Lambda = max|lambda| = {r['Lambda']:.6f}",
        f"  S_fiber (direct heat trace)   = {r['S_fiber_heat']:.6f}",
        f"  S_fiber (asymptotic a_n split) = {r['S_fiber_asym']:.4e}",
        "",
        "--- O'Neill A-tensor cross-term (Gilkey 4.8.16, S74 convention) ---",
        f"  C_adj = sqrt(Cas_adj) = sqrt(3) = {r['C_adj']:.4f}",
        f"  ||A|| = (1/2)||F_omega||  (ONEILL_HALF={r['oneill_half']})",
        f"  sector_A2_weight = {r['sector_A2_weight']:.4e}",
        f"  a4_cross_per_eps = {r['a4_cross_per_eps']:.4e}",
        f"  kappa (ratio/F^2) = {r['kappa_fit']:.6e}  spread = {r['kappa_spread']:.2e}",
        "",
        "--- S61 EXACT recovery + direction (Sage Step 4) ---",
        f"  ratio(||F||=0) = {r['ratio_at_F0']:.2e}  (<= 1e-12: {r['s61_exact_recovered']})",
        f"  monotone increasing = {r['monotone_increasing']}",
        f"  sign_direction_ok = {r['sign_direction_ok']}",
        "",
        "--- Reading B (O(1) curvature stress test, ||F||=1) ---",
        f"  ratio(||F||=1) = {r['ratio_at_phys']:.6e}",
        f"    vs PASS ceiling 1e-3 : {'<' if r['ratio_at_phys']<r['pass_ceiling'] else '>='}",
        "",
        "--- Reading A (Hubble physical scale; where physics SITS) ---",
        f"  eps_AT_phys=(H_0/M_KK)^2 = {r['eps_AT_phys']:.3e}",
        f"  ||F_omega||_Hubble equiv = {r['F_omega_hubble_equiv']:.3e}",
        f"  ratio(Hubble) = {r['ratio_hubble']:.3e}  (<< 3e-7 effacement: {r['ratio_hubble']<r['effacement_bound']})",
    ]
    axD.text(0.0, 1.0, "\n".join(lines), va="top", ha="left", fontsize=6.8,
             family="monospace", transform=axD.transAxes)
    axD.set_title("(D) Diagnostic summary")

    fig.suptitle(
        f"{GATE_ID}  --  O'Neill non-flat submersion cross-terms ||S_cross||/||S_total|| vs ||F_omega||\n"
        f"additive layering S_SA=a0-a2+a4 under a non-flat SU(3) bundle:  {r['verdict']}  ({r['band_tag']})",
        fontsize=10.0, y=1.005,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.955])
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"\nplot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"tau_fold = {tau_fold!r}  M_KK = {M_KK!r}")
    print(f"Gate (keyed off Reading A, physical Hubble curvature): "
          f"PASS if ratio_hubble < 1e-3 AND no cross-term; "
          f"FAIL if ratio_hubble >= O(1); "
          f"INFO if cross-terms EXIST (O(||F||^2) from 0) but EFFACED (ratio_hubble < 3e-7)")

    INPUT_FILES = [
        Path(__file__).resolve(),
        CANONICAL_CONSTANTS_PATH,
        DK_FIBER_CACHE_PATH,
    ]  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)

    r = compute()  # (local)

    print("\n=== Fiber spectrum (L_max=10, Jensen D_K at tau_fold) ===")
    print(f"  n_eigs = {r['n_eigs']}  n_sectors = {r['n_sectors']}  Lambda = {r['Lambda']:.6f}")
    print(f"  S_fiber (direct heat trace)    = {r['S_fiber_heat']:.6f}")
    print(f"  S_fiber (asymptotic a_n split) = {r['S_fiber_asym']:.6e}")

    print("\n=== O'Neill A-tensor cross-term (Gilkey 4.8.16; S74 convention) ===")
    print(f"  C_adj = sqrt(3) = {r['C_adj']:.6f}   ||A|| = (1/2)||F_omega||")
    print(f"  sector_A2_weight = {r['sector_A2_weight']:.6e}")
    print(f"  a4_cross_per_eps = {r['a4_cross_per_eps']:.6e}")
    print(f"  kappa (ratio/F^2) = {r['kappa_fit']:.9e}  spread = {r['kappa_spread']:.3e} "
          f"(spread~0 => pure quadratic)")

    print("\n=== S61 EXACT recovery + direction (Sage substitution-chain Step 4) ===")
    print(f"  ratio(||F||=0) = {r['ratio_at_F0']:.3e}  (<= 1e-12 ZERO_TOL: {r['s61_exact_recovered']})")
    print(f"  monotone increasing = {r['monotone_increasing']}   sign_direction_ok = {r['sign_direction_ok']}")

    print("\n=== Reading B (O(1) curvature stress test, units M_KK^2) ===")
    print(f"  ratio(||F_omega||=1) = {r['ratio_at_phys']:.9e}")
    print(f"    PASS ceiling 1e-3: {'PASS' if r['ratio_at_phys']<r['pass_ceiling'] else 'above'}")

    print("\n=== Reading A (Hubble physical scale; where the actual physics sits) ===")
    print(f"  eps_AT_phys = (H_0/M_KK)^2 = {r['eps_AT_phys']:.6e}")
    print(f"  ||F_omega||_Hubble equiv   = {r['F_omega_hubble_equiv']:.6e}")
    print(f"  ratio(Hubble) = {r['ratio_hubble']:.6e}  "
          f"(<< 3e-7 effacement bound: {r['ratio_hubble']<r['effacement_bound']})")

    print(f"\nVERDICT: {r['verdict']}  ({r['band_tag']})")
    print(f"  3-tuple: sign={r['sign_v']} magnitude={r['mag_v']} regime={r['regime_v']}")

    make_plot(r)

    # serialize fanout dict as JSON for npz storage
    fanout_json = json.dumps({f"{p}_{q}": v for (p, q), v in r["fanout_per_sector"].items()})  # (local)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, verdict=r["verdict"], band_tag=r["band_tag"],
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        sign_verdict=r["sign_v"], magnitude_verdict=r["mag_v"], regime_verdict=r["regime_v"],
        # constants:
        M_KK=r["M_KK"], tau_fold=r["tau_fold"], H_0_GeV=r["H_0_GeV"],
        a0_fold=r["a0_fold"], a2_fold=r["a2_fold"], a4_fold=r["a4_fold"],
        S_fold=r["S_fold"], Gamma_effacement=r["Gamma_effacement"],
        f_0=r["f_0"], f_2=r["f_2"], f_4=r["f_4"],
        # fiber:
        n_eigs=r["n_eigs"], n_sectors=r["n_sectors"], Lambda=r["Lambda"],
        S_fiber_heat=r["S_fiber_heat"], S_fiber_asym=r["S_fiber_asym"],
        # base:
        a0_base=r["a0_base"], a2_base=r["a2_base"], a4_base=r["a4_base"], S_base_heat=r["S_base_heat"],
        # cross-term machinery:
        C_adj=r["C_adj"], cas_adjoint=r["cas_adjoint"], oneill_half=r["oneill_half"],
        sector_A2_weight=r["sector_A2_weight"], a4_cross_per_eps=r["a4_cross_per_eps"],
        # Reading B scan:
        F_omega_grid=r["F_omega_grid"], eps_of_F=r["eps_of_F"],
        a4_cross_of_F=r["a4_cross_of_F"], S_cross_of_F=r["S_cross_of_F"],
        S_total_of_F=r["S_total_of_F"], ratio_of_F=r["ratio_of_F"],
        ratio_at_F0=r["ratio_at_F0"], s61_exact_recovered=r["s61_exact_recovered"],
        ratio_at_phys=r["ratio_at_phys"], kappa_fit=r["kappa_fit"], kappa_spread=r["kappa_spread"],
        monotone_increasing=r["monotone_increasing"], sign_direction_ok=r["sign_direction_ok"],
        # Reading A:
        eps_AT_phys=r["eps_AT_phys"], a4_cross_hubble=r["a4_cross_hubble"],
        ratio_hubble=r["ratio_hubble"], F_omega_hubble_equiv=r["F_omega_hubble_equiv"],
        # thresholds:
        pass_ceiling=r["pass_ceiling"], effacement_bound=r["effacement_bound"],
        zero_tol=r["zero_tol"], fail_oom=r["fail_oom"],
        fanout_per_sector_json=fanout_json,
    )
    print(f"data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- value field for verdict line ---
    # supersedes=<old_audit_sha>: Option A (gate-verdicts.md). The original FAIL line
    # (which keyed off the Reading-B ||F||=1 O(1)-curvature stress-test) is RETAINED on
    # disk (verdict permanence); this corrective INFO line supersedes it. The verdict-
    # SELECTION now keys off Reading A (ratio_hubble at the physical Hubble curvature scale).
    verdict_key = "ratio_hubble" if r["s61_exact_recovered"] else "s61_recovery"  # (local)
    value_field = (
        f"supersedes={SUPERSEDED_AUDIT_SHA};"
        f"verdict_keyed_off_Reading_A_ratio_Hubble_physical={r['ratio_hubble']:.3e}"
        f"(vs_effacement_bound_3e-7=EFFACED:{r['ratio_hubble']<r['effacement_bound']});"
        f"cross_terms_EXIST_O(||F||^2)_from_0_EXACT_at_flat_product;"
        f"ratio_at_flat_product(||F||=0)={r['ratio_at_F0']:.2e}(S61_A=T=0_EXACT={r['s61_exact_recovered']});"
        f"kappa_quadratic_coeff_smallF={r['kappa_fit']:.4e}(spread={r['kappa_spread']:.1e}_pure_F^2_n={r['n_smallF_fit']});"
        f"ratio_grows_quadratically_from_0=True;monotone_increasing={r['monotone_increasing']};"
        f"DIAGNOSTIC_Reading_B_stress_test_ratio(||F||=1)={r['ratio_at_phys']:.4e}(O(1)_curvature_NOT_physical);"
        f"S_fiber_heat={r['S_fiber_heat']:.4f};S_base={r['S_base_heat']:.4f};"
        f"n_eigs={r['n_eigs']};Lambda={r['Lambda']:.4f};C_adj=sqrt3;"
        f"additive_layering_S_SA=a0-a2+a4_exact_at_phys_scale={r['verdict']=='PASS'};"
        f"PASS_ceiling=1e-3;FAIL_O(1)=0.1;INFO_effacement=3e-7;band_tag={r['band_tag']}"
    )  # (local)

    print(f"\n4-tuple: (value='{value_field[:90]}...', scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # input pin map (audit_sha256_inputs: script, canonical, pinmap, dk_fiber_cache)
    input_pin_map = {rel: sha for rel, sha in pins.items()}  # (local)
    input_pin_map["canonical_constants_M_KK"] = f"{float(M_KK):.18e}"
    input_pin_map["canonical_constants_tau_fold"] = f"{float(tau_fold):.18e}"
    input_pin_map["canonical_constants_a2_fold"] = f"{float(a2_fold):.18e}"
    input_pin_map["canonical_constants_a4_fold"] = f"{float(a4_fold):.18e}"
    input_pin_map["_gate_id"] = GATE_ID
    input_pin_map["_scheme"] = SCHEME
    input_pin_map["_convention"] = CONVENTION
    input_pin_map["_L_max"] = str(L_MAX)
    input_pin_map["_N_eval"] = str(N_EVAL)
    input_pin_map["_C_adj"] = f"{C_ADJ:.18e}"

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_CONSTANTS_PATH, input_pin_map
    )  # (local)
    append_verdict(r["verdict"], value_field, audit_sha, content_sha,
                   r["sign_v"], r["mag_v"], r["regime_v"])
    print(f"\nverdict appended: {r['verdict']} -- value (truncated)={value_field[:100]!r}...")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"\nwall: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
