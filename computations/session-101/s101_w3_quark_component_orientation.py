#!/usr/bin/env python3
"""
S101 W2-4 — S101-W3-QUARK-COMPONENT-ORIENTATION  ([SIGN])
=========================================================

Gate: S101-W3-QUARK-COMPONENT-ORIENTATION  ([SIGN])

Pre-registered threshold (orientation gate; set-membership form, no numerical band):
  sign_verdict  = (p-1)-on-D  AND  (p-1)-on-c  AND  (p-2)-at-gen-3
                  (p-1): within EACH quark component the trace-mean ladder
                         <lam^2>_g^{(comp)} is STRICTLY C2-ASCENDING on the tower
                         (1,0)<(1,1)<(3,0)  =>  the mass map is C2-DESCENDING
                         (gen1<->(3,0), gen2<->(1,1), gen3<->(1,0)) — the SAME
                         orientation as the W-2-pinned lepton map.
                  (p-2): up-type envelope > down-type envelope at the heavy
                         generation (gen 3).
  magnitude (crossing test):
                  PASS = generation-dependent crossing realized
                         (m_u/m_d < 1 at gen 1 AND m_t/m_b > 1 at gen 3)
                  INFO = uniform ordering, no crossing (the uniform-kappa
                         sub-reading's pre-declared FAIL stands recorded)
                  FAIL = globally anti-oriented (down > up at gen 3).
  regime:         VALID  iff kappa-triple pre-flight re-grep matches S99 panel
                         AND Omega^D/Omega^c = 2 cross-check holds at 1e-12
                  MARGINAL iff cross-check deviates <= 1e-6
                  BREAKDOWN iff kappa-triple cannot be recovered OR
                         Omega^D/Omega^c != 2 beyond 1e-6.
  Composite via the CANONICAL gate-verdicts.md collapse rule, unmodified.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (the LC spectrum
    cache, re-labeled at W1-1 PASS audit 194b2b3c; cited at FULL CONFIDENCE)
  - sessions/archive/session-99/session-99-fermion-mass-hawking.md  (kappa-triple
    [SPECULATION]-class PARTIAL PRIOR provenance; in-script re-grep)
  - canonical_constants.py  (PDG SECTION E quark anchors + tau_fold + T_acoustic)
  - script bytes

Output 4-tuple:
  (value=<sign chains + crossing scalars>,
   scheme=D-AND-C-COMPONENT-KERNEL-TRACE-MEAN-LADDER,
   convention=RATIO-NORMALIZED-TRACE-MEAN, L_max=12)

Classification: PARTICLE.

METHODOLOGY
-----------
PART 1 ([SIGN] pre-registration) is written into the WP section BEFORE compute.
PART 2 (this script) reuses the existing L12 master cache (NO new diagonalization).

Per Baptista Paper 14 (researchers/Baptista/14_2021_Baptista_HD_Routes_SM_Fermions.md)
eq-(2.17) component table, the 64-component generation spinor decomposes into
components whose vertical profiles read DIFFERENT faces of the same fiber:
  - D-component:  D^P_+(x,h) = h D_+(x) h_bar  (ADJOINT action; NO s(h) scalar).
                  D_+ = [d_R^T, u_L^T, d_L^T] holds the DOWN-type quarks (d_R,d_L).
                  Laplacian mass matrix Omega^D = sum_j e_j e_j + (1/3)Tr(e_j e_j)I3
                  = (8/3) I3   (eq 3.19, e_j = lambda_j/2 Gell-Mann).
  - c-component:  c^P_+(x,h) = s(h) h^dagger c_+(x)  (FUNDAMENTAL with s(h) scalar).
                  c_+ = u_R(x) is the right-handed UP-type quark.
                  Laplacian mass matrix Omega^c proportional to I3 = (4/3) I3
                  (color-Schur, sec 3).
Both kernels inherit the SAME bare D_K spectrum (the cache abs_evals per Peter-Weyl
sector (p,q)); they differ by the per-component overall mass-matrix scalar Omega^{comp}
(a multiplicative prefactor that CANCELS in any within-component ordering test, and
SURVIVES in any cross-component magnitude comparison).

(p-1) the within-component ladder is the multiplicity-normalized trace-mean
<lam^2>_g^{(comp)} = Omega^{comp} * mean(abs_evals(p,q)^2). The Omega^{comp} prefactor
cancels in the strict-ascent test => (p-1) is kernel-INDEPENDENT in SIGN (the freeze-in
direction theorem, W3-9 sign-PASS): deeper freeze at larger C2 => lighter fermion, and
<lam^2> ascends with C2 (3*C2 + 27/4 at tau=0 EXACTLY; persists at tau_fold).

(p-2) the cross-component up/down ordering is realized via the four-lens greybody
envelope m_g^{(comp)} ~ Omega^{comp} * Gamma(omega) * exp(-2*pi*omega_g/kappa_comp) with
omega_g = C2(g)*tau_fold*M_KK (the W-3 graded S0 = 95/56 reading; ordering-only here),
kappa_up = kappa_c = 1.29 > kappa_down = kappa_D = 0.78 (S99 [SPECULATION]-class triple).
Up = c-component (u_R) at kappa_up; down = D-component (d_R/d_L) at kappa_down.

Cross-anchor (machinery cross-check, NON-gating): Omega^D = (8/3)I3 != Omega^c = (4/3)I3,
Omega^D/Omega^c = 2 EXACTLY (Sage-QQ; audit d23c7e99cba96403 of S100a-DUAL-Z3-PHI-POINTS).

DISCIPLINE
----------
- `from canonical_constants import *`
- intermediates tagged `# (local)`
- cache sectors are <= dim 10 (n_abs_evals <= 160): pure CPU, OMP_NUM_THREADS=8 cap.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- 4-tuple printed as the final non-verdict line.
- Gate verdict via emit_verdict MCP tool (race-safe): this script PRINTS the payload
  (print_verdict_payload), the AGENT calls mcp__knowledge__emit_verdict(**payload).
- No Seeley-DeWitt a_n cited => no regulator_pin. No SCHEMATIC helper => no CLASS pin.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit for the linters / provenance
    tau_fold,
    T_acoustic,
    M_KK_gravity,
    m_u_msbar_2GeV,
    m_d_msbar_2GeV,
    m_s_msbar_2GeV,
    m_c_msbar_mc,
    m_b_msbar_mb,
    m_t_pole,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
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
# Section 3 — Paths + pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "S101"  # (local)
GATE_ID = "S101-W3-QUARK-COMPONENT-ORIENTATION"  # (local)
SCHEME = "D-AND-C-COMPONENT-KERNEL-TRACE-MEAN-LADDER"  # (local)
CONVENTION = "RATIO-NORMALIZED-TRACE-MEAN"  # (local)
L_MAX = 12  # (local)

CACHE_NPZ = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
HAWKING_PANEL = (
    PROJECT_ROOT / "sessions" / "session-99" / "session-99-fermion-mass-hawking.md"
)  # (local)
CANON = SHARED_DIR / "canonical_constants.py"  # (local)

OUT_NPZ = SESSION_DIR / "s101_w3_quark_component_orientation.npz"  # (local)
OUT_PNG = SESSION_DIR / "s101_w3_quark_component_orientation.png"  # (local)

INPUT_FILES = [CANON, CACHE_NPZ, HAWKING_PANEL]  # (local)

# The generation tower (Peter-Weyl sectors) and the lepton map orientation pin
# (W-2 landscape: tau=(1,0), mu=(1,1), e=(3,0); heaviest<->lowest-C2).
TOWER = [(1, 0), (1, 1), (3, 0)]  # (local)  in C2-ASCENDING order
# generation index assignment under the C2-DESCENDING mass map:
#   gen3 (heaviest) <-> (1,0)   [lowest C2]
#   gen2            <-> (1,1)
#   gen1 (lightest) <-> (3,0)   [highest C2]
GEN_OF_SECTOR = {(1, 0): 3, (1, 1): 2, (3, 0): 1}  # (local)

# kappa-triple [SPECULATION]-class PARTIAL PRIOR (S99 hawking panel line 74);
# pins (p-2) DIRECTION only, never a magnitude.
KAPPA_LEPTON = 1.89  # (local)
KAPPA_UP = 1.29  # (local)   c-component (u_R)
KAPPA_DOWN = 0.78  # (local)   D-component (d_R, d_L)
# in-script re-grep target string (mismatch => regime BREAKDOWN):
KAPPA_TRIPLE_REGREP = "lepton 1.89, up 1.29, down 0.78"  # (local)

# Omega^{comp} per-component mass-matrix scalar (Baptista eq 3.19 / sec 3).
OMEGA_D = 8.0 / 3.0  # (local)   D-component  (down-type)
OMEGA_C = 4.0 / 3.0  # (local)   c-component  (up-type)
OMEGA_RATIO_TARGET = 2.0  # (local)   Omega^D/Omega^c EXACT (audit d23c7e99cba96403)

# Machinery cross-check bands (NON-gating regime tags).
OMEGA_TOL_VALID = 1e-12  # (local)
OMEGA_TOL_MARGINAL = 1e-6  # (local)


def C2(p: int, q: int) -> float:
    """SU(3) quadratic Casimir, C2(p,q) = (p^2+q^2+pq)/3 + p + q."""
    return (p * p + q * q + p * q) / 3.0 + p + q


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (dual-SHA, S84+)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


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
# Section 5 — Compute
# ---------------------------------------------------------------------------
def kappa_triple_preflight() -> bool:
    """Re-grep the S99 panel for the kappa-triple string. Mismatch => regime
    input invalid (regime_verdict = BREAKDOWN)."""
    try:
        text = HAWKING_PANEL.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError:
        return False
    return KAPPA_TRIPLE_REGREP in text


def component_trace_mean_ladder(se: dict, omega_comp: float) -> dict:
    """Multiplicity-normalized trace-mean ladder for one quark component.

    <lam^2>_g^{(comp)} = Omega^{comp} * mean_over_abs_evals( |lambda|^2 ).
    The mean over abs_evals normalizes by the per-sector multiplicity
    (n/dim = 16.00 for every sector: the C^16 generation factor); this IS the
    RATIO-NORMALIZED-TRACE-MEAN counting convention (state evaluation rho_g =
    P_g/Tr(P_g), W-2 pinned).
    """
    ladder = {}  # (local)
    for (p, q) in TOWER:
        ae = np.asarray(se[(p, q)]["abs_evals"], dtype=np.float64)  # (local)
        bare = float(np.mean(ae * ae))  # (local) multiplicity-normalized <lam^2>
        ladder[(p, q)] = {
            "C2": C2(p, q),
            "dim": int(se[(p, q)]["dim"]),
            "n_abs_evals": int(ae.size),
            "bare_trace_mean_lam2": bare,
            "comp_trace_mean_lam2": omega_comp * bare,  # Omega^{comp}-scaled
            "min_abs_lam": float(np.min(ae)),
        }
    return ladder


def strict_ascending(ladder: dict) -> bool:
    """(p-1) test: strict C2-ascent of the trace-mean ladder on TOWER."""
    seq = [ladder[(p, q)]["comp_trace_mean_lam2"] for (p, q) in TOWER]  # (local)
    return all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))


def greybody_envelope(omega_comp: float, kappa_comp: float) -> dict:
    """Four-lens greybody envelope per generation for one quark component:
        m_g ~ Omega^{comp} * exp(-2*pi*omega_g/kappa_comp),  omega_g = C2(g)*tau_fold*M_KK.
    Gamma(omega) is a common O(1) transmission (cancels in same-component ratios
    and is taken sector-uniform here) — set to 1, since (p-2)/crossing are RATIO
    tests across components at FIXED generation where the C2-graded omega_g is
    the discriminator. Returns m_g per generation (arb units; only RATIOS used).
    """
    env = {}  # (local)
    for (p, q) in TOWER:
        g = GEN_OF_SECTOR[(p, q)]  # (local)
        # omega_g = C2(g)*tau_fold in M_KK UNITS (dimensionless). The kappa-triple
        # (1.29/0.78) is ALSO in M_KK units (S99 panel: "kappa_exit=47.61 M_KK",
        # "kappa_SONIC=0.705 M_KK"), so the M_KK factor CANCELS in 2*pi*omega/kappa.
        # Multiplying omega by M_KK_gravity (~7.4e16) would underflow exp() to 0 for
        # every generation and destroy the envelope discriminator — the units must
        # cancel by construction (the greybody exponent 2*pi*omega/kappa is M_KK-free).
        omega_g = C2(p, q) * tau_fold  # (local) graded S0 reading, M_KK units
        m_g = omega_comp * np.exp(-2.0 * np.pi * omega_g / kappa_comp)  # (local)
        env[g] = {
            "sector": (p, q),
            "C2": C2(p, q),
            "omega_g": omega_g,
            "m_g": float(m_g),
        }
    return env


def compute() -> dict:
    print(f"\n=== {GATE_ID} — PART 2 compute (L12 cache, no new diagonalization) ===")
    data = np.load(CACHE_NPZ, allow_pickle=True)  # (local)
    se = data["sector_evals"].item()  # (local)  dict keyed by (p,q)

    # --- kappa-triple pre-flight (regime gate) ---
    kappa_ok = kappa_triple_preflight()  # (local)
    print(f"kappa-triple re-grep '{KAPPA_TRIPLE_REGREP}' in S99 panel: {kappa_ok}")

    # --- per-component trace-mean ladders (D and c) ---
    ladder_D = component_trace_mean_ladder(se, OMEGA_D)  # (local)
    ladder_c = component_trace_mean_ladder(se, OMEGA_C)  # (local)

    print("\n  D-component ladder (h.D_+.h_bar, adjoint; Omega^D=8/3):")
    for (p, q) in TOWER:
        L = ladder_D[(p, q)]
        print(
            f"    (%d,%d) gen=%d C2=%.4f  bare<lam^2>=%.6f  comp<lam^2>=%.6f"
            % (p, q, GEN_OF_SECTOR[(p, q)], L["C2"], L["bare_trace_mean_lam2"], L["comp_trace_mean_lam2"])
        )
    print("\n  c-component ladder (s(h).h^dag, fundamental; Omega^c=4/3):")
    for (p, q) in TOWER:
        L = ladder_c[(p, q)]
        print(
            f"    (%d,%d) gen=%d C2=%.4f  bare<lam^2>=%.6f  comp<lam^2>=%.6f"
            % (p, q, GEN_OF_SECTOR[(p, q)], L["C2"], L["bare_trace_mean_lam2"], L["comp_trace_mean_lam2"])
        )

    # --- (p-1) strict-ascent tests per component ---
    p1_D = strict_ascending(ladder_D)  # (local)
    p1_c = strict_ascending(ladder_c)  # (local)
    print(f"\n  (p-1) strict C2-ascent  D-component: {p1_D}   c-component: {p1_c}")

    # --- (p-2) cross-component greybody envelopes ---
    env_up = greybody_envelope(OMEGA_C, KAPPA_UP)  # (local)  up = c-component
    env_down = greybody_envelope(OMEGA_D, KAPPA_DOWN)  # (local)  down = D-component

    # up/down ratio per generation (envelope crossing)
    ud_ratio = {}  # (local)
    for g in (1, 2, 3):
        ud_ratio[g] = env_up[g]["m_g"] / env_down[g]["m_g"]  # (local)
    print("\n  envelope up/down ratio per generation (m_up/m_down):")
    for g in (1, 2, 3):
        print(f"    gen{g}: m_up/m_down = %.6e" % ud_ratio[g])

    # (p-2): up envelope > down envelope at gen 3 (heavy)
    p2_gen3 = env_up[3]["m_g"] > env_down[3]["m_g"]  # (local)
    print(f"\n  (p-2) up-envelope > down-envelope at gen 3: {p2_gen3}")

    # --- crossing test (magnitude) ---
    # generation-dependent crossing: up/down < 1 at gen1 AND > 1 at gen3
    cross_gen1 = ud_ratio[1] < 1.0  # (local)
    cross_gen3 = ud_ratio[3] > 1.0  # (local)
    crossing_realized = cross_gen1 and cross_gen3  # (local)
    # globally anti-oriented: down > up at gen 3 (contradicts (p-2))
    globally_anti = not p2_gen3  # (local)
    # uniform ordering (no crossing): up/down on the SAME side of 1 at gen1 and gen3
    uniform_ordering = (
        (ud_ratio[1] > 1.0 and ud_ratio[3] > 1.0)
        or (ud_ratio[1] < 1.0 and ud_ratio[3] < 1.0)
    )  # (local)
    print(
        f"\n  crossing: gen1 m_u/m_d<1: {cross_gen1}  gen3 m_t/m_b>1: {cross_gen3}  "
        f"=> realized: {crossing_realized}"
    )

    # --- PDG held-out reference ratios (gen1 inversion + gen3 ordering) ---
    pdg_mu_md_gen1 = m_u_msbar_2GeV / m_d_msbar_2GeV  # (local)  0.46 < 1 target
    pdg_mt_mb_gen3 = m_t_pole / m_b_msbar_mb  # (local)  >> 1
    pdg_mc_ms_gen2 = m_c_msbar_mc / m_s_msbar_2GeV  # (local)  gen2 up/down (charm/strange)
    print(
        "\n  PDG held-out: gen1 m_u/m_d=%.4f (<1: %s); gen2 m_c/m_s=%.4f; gen3 m_t/m_b=%.4f (>1: %s)"
        % (
            pdg_mu_md_gen1,
            pdg_mu_md_gen1 < 1.0,
            pdg_mc_ms_gen2,
            pdg_mt_mb_gen3,
            pdg_mt_mb_gen3 > 1.0,
        )
    )

    # --- Omega^D/Omega^c machinery cross-check (regime tag) ---
    omega_ratio = OMEGA_D / OMEGA_C  # (local)
    omega_dev = abs(omega_ratio - OMEGA_RATIO_TARGET)  # (local)
    print(f"\n  Omega^D/Omega^c = %.15f (target 2; dev=%.3e)" % (omega_ratio, omega_dev))

    # --- tau=0 analytic ascent backbone (Claim 1 cross-check, exact form) ---
    tau0_form = {(p, q): 3.0 * C2(p, q) + 27.0 / 4.0 for (p, q) in TOWER}  # (local)
    tau0_ascending = all(
        tau0_form[TOWER[i]] < tau0_form[TOWER[i + 1]] for i in range(len(TOWER) - 1)
    )  # (local)
    print(
        "  tau=0 exact form 3*C2+27/4 = "
        + ", ".join("%.3f" % tau0_form[s] for s in TOWER)
        + f"  (ascending: {tau0_ascending})"
    )

    # --- verdict assembly (pre-registered) ---
    sign_pass = bool(p1_D and p1_c and p2_gen3)  # (local)
    if globally_anti:
        magnitude = "FAIL"  # (local)
    elif crossing_realized:
        magnitude = "PASS"  # (local)
    else:
        # directions hold but no crossing -> uniform ordering => INFO
        magnitude = "INFO"  # (local)

    if not kappa_ok:
        regime = "BREAKDOWN"  # (local)
    elif omega_dev <= OMEGA_TOL_VALID:
        regime = "VALID"  # (local)
    elif omega_dev <= OMEGA_TOL_MARGINAL:
        regime = "MARGINAL"  # (local)
    else:
        regime = "BREAKDOWN"  # (local)

    sign_verdict = "PASS" if sign_pass else "FAIL"  # (local)

    # composite collapse (CANONICAL gate-verdicts.md rule, unmodified)
    if regime == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude == "FAIL" and regime == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude == "FAIL" and regime == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    return {
        "ladder_D": ladder_D,
        "ladder_c": ladder_c,
        "p1_D": p1_D,
        "p1_c": p1_c,
        "p2_gen3": p2_gen3,
        "env_up": env_up,
        "env_down": env_down,
        "ud_ratio": ud_ratio,
        "cross_gen1": cross_gen1,
        "cross_gen3": cross_gen3,
        "crossing_realized": crossing_realized,
        "uniform_ordering": uniform_ordering,
        "globally_anti": globally_anti,
        "pdg_mu_md_gen1": pdg_mu_md_gen1,
        "pdg_mc_ms_gen2": pdg_mc_ms_gen2,
        "pdg_mt_mb_gen3": pdg_mt_mb_gen3,
        "omega_ratio": omega_ratio,
        "omega_dev": omega_dev,
        "kappa_ok": kappa_ok,
        "tau0_form": tau0_form,
        "tau0_ascending": tau0_ascending,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude,
        "regime_verdict": regime,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 6 — 4-tuple + verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(
    verdict, value, audit_sha, content_sha,
    sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
    extra_rows=None,
):
    payload = {
        "session": "101",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if sign_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("\n=== VERDICT PAYLOAD (JSON for emit_verdict) ===")
    print("BEGIN_VERDICT_PAYLOAD")
    print(json.dumps(payload, separators=(",", ":")))
    print("END_VERDICT_PAYLOAD")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))  # (local)

    c2 = [C2(*s) for s in TOWER]  # (local)
    gens = [GEN_OF_SECTOR[s] for s in TOWER]  # (local)
    lab = [f"({p},{q})\ngen{GEN_OF_SECTOR[(p,q)]}" for (p, q) in TOWER]  # (local)

    # Panel 1: (p-1) per-component trace-mean ladders vs C2
    ax = axes[0]
    yD = [R["ladder_D"][s]["comp_trace_mean_lam2"] for s in TOWER]  # (local)
    yc = [R["ladder_c"][s]["comp_trace_mean_lam2"] for s in TOWER]  # (local)
    yb = [R["ladder_D"][s]["bare_trace_mean_lam2"] for s in TOWER]  # (local)
    ax.plot(c2, yD, "o-", color="C3", label=r"D-comp $\Omega^D\langle\lambda^2\rangle$ (8/3)")
    ax.plot(c2, yc, "s-", color="C0", label=r"c-comp $\Omega^c\langle\lambda^2\rangle$ (4/3)")
    ax.plot(c2, yb, "^--", color="0.5", label=r"bare $\langle\lambda^2\rangle$")
    ax.set_xlabel(r"$C_2(p,q)$")
    ax.set_ylabel(r"trace-mean $\langle\lambda^2\rangle$ at $\tau_{fold}$")
    ax.set_title(
        "(p-1) within-component C2-ASCENT\n"
        f"D: {R['p1_D']}   c: {R['p1_c']}  => mass map C2-DESCENDING"
    )
    for x, s in zip(c2, TOWER):
        ax.annotate(f"({s[0]},{s[1]})", (x, R["ladder_D"][s]["comp_trace_mean_lam2"]),
                    textcoords="offset points", xytext=(4, 6), fontsize=8)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2: (p-2) greybody envelopes per generation (log scale)
    ax = axes[1]
    g_axis = [1, 2, 3]  # (local)
    mu = [R["env_up"][g]["m_g"] for g in g_axis]  # (local)
    md = [R["env_down"][g]["m_g"] for g in g_axis]  # (local)
    ax.semilogy(g_axis, mu, "s-", color="C0", label=r"up (c-comp, $\kappa$=1.29)")
    ax.semilogy(g_axis, md, "o-", color="C3", label=r"down (D-comp, $\kappa$=0.78)")
    ax.set_xlabel("generation (1=lightest)")
    ax.set_ylabel(r"greybody envelope $m_g$ (arb units)")
    ax.set_xticks(g_axis)
    ax.set_title(
        "(p-2) up vs down envelope\n"
        f"gen3 up>down: {R['p2_gen3']}"
    )
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # Panel 3: crossing — up/down ratio per generation vs PDG
    ax = axes[2]
    ud = [R["ud_ratio"][g] for g in g_axis]  # (local)
    ax.semilogy(g_axis, ud, "D-", color="C2", label="construction $m_{up}/m_{down}$")
    ax.axhline(1.0, color="k", ls=":", lw=1, label="crossing line (=1)")
    pdg = [R["pdg_mu_md_gen1"], R["pdg_mc_ms_gen2"], R["pdg_mt_mb_gen3"]]  # (local)
    ax.semilogy(g_axis, pdg, "*", color="C1", ms=12, label="PDG up/down (u/d, c/s, t/b)")
    ax.set_xlabel("generation")
    ax.set_ylabel(r"$m_{up}/m_{down}$")
    ax.set_xticks(g_axis)
    ax.set_title(
        "crossing test\n"
        f"gen1<1: {R['cross_gen1']}  gen3>1: {R['cross_gen3']}  realized: {R['crossing_realized']}"
    )
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    fig.suptitle(
        f"{GATE_ID}  [SIGN]  composite={R['composite']}  "
        f"(sign={R['sign_verdict']} mag={R['magnitude_verdict']} regime={R['regime_verdict']})",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"\n  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANON, pins)  # (local)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    R = compute()  # (local)

    # --- value payload (single-quote-free per emit_verdict grammar) ---
    udr = R["ud_ratio"]  # (local)
    value = (
        f"p1_D={R['p1_D']};p1_c={R['p1_c']};p2_gen3={R['p2_gen3']};"
        f"ud_g1={udr[1]:.4e};ud_g2={udr[2]:.4e};ud_g3={udr[3]:.4e};"
        f"crossing={R['crossing_realized']};uniform={R['uniform_ordering']};"
        f"OmegaD/Omegac={R['omega_ratio']:.6f};kappa_ok={R['kappa_ok']};"
        f"PDG_u/d_g1={R['pdg_mu_md_gen1']:.4f};PDG_t/b_g3={R['pdg_mt_mb_gen3']:.4f}"
    )  # (local)

    print("\n" + emit_4tuple(value, SCHEME, CONVENTION, L_MAX))

    # --- save npz (full float64) ---
    np.savez(
        OUT_NPZ,
        tower=np.array(TOWER),
        gen_of_sector=np.array([GEN_OF_SECTOR[s] for s in TOWER]),
        C2_tower=np.array([C2(*s) for s in TOWER]),
        bare_trace_mean_lam2=np.array([R["ladder_D"][s]["bare_trace_mean_lam2"] for s in TOWER]),
        comp_trace_mean_lam2_D=np.array([R["ladder_D"][s]["comp_trace_mean_lam2"] for s in TOWER]),
        comp_trace_mean_lam2_c=np.array([R["ladder_c"][s]["comp_trace_mean_lam2"] for s in TOWER]),
        min_abs_lam=np.array([R["ladder_D"][s]["min_abs_lam"] for s in TOWER]),
        n_abs_evals=np.array([R["ladder_D"][s]["n_abs_evals"] for s in TOWER]),
        env_up_mg=np.array([R["env_up"][g]["m_g"] for g in (1, 2, 3)]),
        env_down_mg=np.array([R["env_down"][g]["m_g"] for g in (1, 2, 3)]),
        env_omega_g=np.array([R["env_up"][g]["omega_g"] for g in (1, 2, 3)]),
        ud_ratio=np.array([R["ud_ratio"][g] for g in (1, 2, 3)]),
        p1_D=R["p1_D"],
        p1_c=R["p1_c"],
        p2_gen3=R["p2_gen3"],
        cross_gen1=R["cross_gen1"],
        cross_gen3=R["cross_gen3"],
        crossing_realized=R["crossing_realized"],
        uniform_ordering=R["uniform_ordering"],
        globally_anti=R["globally_anti"],
        omega_D=OMEGA_D,
        omega_c=OMEGA_C,
        omega_ratio=R["omega_ratio"],
        omega_dev=R["omega_dev"],
        kappa_lepton=KAPPA_LEPTON,
        kappa_up=KAPPA_UP,
        kappa_down=KAPPA_DOWN,
        kappa_ok=R["kappa_ok"],
        pdg_mu_md_gen1=R["pdg_mu_md_gen1"],
        pdg_mc_ms_gen2=R["pdg_mc_ms_gen2"],
        pdg_mt_mb_gen3=R["pdg_mt_mb_gen3"],
        tau0_form=np.array([R["tau0_form"][s] for s in TOWER]),
        tau0_ascending=R["tau0_ascending"],
        tau_fold=tau_fold,
        M_KK_gravity=M_KK_gravity,
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        composite=R["composite"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(R)

    # --- per-chain extra-row (A19 extra-row N/A: this is a post-lift dispatch,
    #     S101-TAU0 L4 lift already landed; cross-wave pin 1 satisfied) ---
    extra_rows = [
        (
            f"# p1_D={R['p1_D']} p1_c={R['p1_c']} p2_gen3={R['p2_gen3']} "
            f"crossing={R['crossing_realized']} uniform={R['uniform_ordering']} "
            f"# {GATE_ID} per-chain sign rows"
        ),
        (
            f"# OmegaD/Omegac={R['omega_ratio']:.6f}(target2,dev{R['omega_dev']:.1e}) "
            f"kappa_triple_regrep={R['kappa_ok']} "
            f"# {GATE_ID} machinery cross-check (audit d23c7e99cba96403, non-gating)"
        ),
    ]  # (local)

    payload = print_verdict_payload(
        R["composite"],
        value,
        audit_sha,
        content_sha,
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        extra_rows=extra_rows,
    )

    print(f"\n  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
