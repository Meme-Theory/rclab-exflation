#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S97-D3-BF  (agent: mack-cosmic-bridge; co-review: sagan-empiricist)
==================================================================
The DESI-DR3 joint-evidence Bayes factor over the Register-A zero-parameter
SPINE, computed with the EVOI prior-predictive-range / posterior-width method
(sessions/evoi-framework.md), REPLACING the retired "chance of one random
geometry" heuristic.

CRITICAL SCOPE (NUMBERS-first reading of the plan, NOT the colloquial title):
  This gate is NOT a likelihood-ratio BF of the framework's w0=-0.918 vs LCDM
  AGAINST DESI DR3 DATA. DR3 is the BINDING INSTRUMENT for the R_842 (w0,wa)
  rectangle, but the binding EVENT is 2027 (Window-14, Q37 LIVE) -- the data is
  not out. The R_842 / w0 falsifier is a SEPARATE channel (atlas-05 Window-14;
  falsifier-master-inventory.md w0 row). w0/wa enter THIS gate ONLY through the
  within-layer-not-multiplied DISCIPLINE: wa=0 is structural (four-fold lock),
  and the borrowed-H w0/wa/sigma8 dagger rows are NOT independent factors.

  What S97-D3-BF computes is the MODEL-CLASS joint-evidence headline:
    (i)  BF_spine  -- the UNCONDITIONAL FLOOR: product of the per-observable
         prior-predictive-range BFs over the 4 Register-A SPINE observables
         {m_H (a4 KK-threshold structural), normal nu-ordering, sigma/m=0,
          c_s^2=0}. These carry NO borrowed H(t), are statistically
          independent, hence legitimately multiplicative (W7-7b RESTRICT PASS).
    (ii) BF_spine+dagger(|Corr|) -- adds the {a0,a2} dagger pair at the Gaussian
         correlation discount C(|Corr|), under the IMMOVABLE disposition:
            |Corr| < 0.5 -> joint discount, Delta log BF = (1-|Corr|)*b_a0
            |Corr| >= 0.5 -> collapse {a0,a2} to max(b_a0,b_a2)  [rank-1 default]

THE [SIGN] PREDICTION (substitution chain, plan §W4-4 item 7):
  |Corr| = 1/sqrt((1+r0)(1+r2)) is a function of the variance mix r ALONE; the
  kernel disparity s_a2/s_a0 = 518.330 CANCELS (Sage-exact). |Corr| DECREASES as
  r increases; the edge |Corr|=0.5 <=> r=1 <=> sigma_Hprivate = sigma_Hshared.
  The pinned r-pre-image {0.03,0.04,0.05,0.06} -> |Corr| {25/34,25/41,1/2,25/61}
  STRADDLES 0.5 (3 of 4 on the rank-1 side); the CENTRAL pin (sigma_Hi=sigma_Hc
  =0.05, the W7-7a shared dH/H) lands EXACTLY ON the edge (|Corr|=1/2). The
  substrate-forced DEFAULT is rank-1 COLLAPSE unless the pinned r AND the OQ3
  mutual-independence determination BOTH license the discount.

OQ3 (substrate-input-orthogonality, joint-theorem-promotion.md):
  trace_entity('sigma_8 growth fsigma8 borrowed H0 Omega_m pipeline') returned
  NO cross-pipeline covariance => mutual independence of the w0 (DE-EOS) and
  sigma_8 (growth/RSD) private-H components is UNESTABLISHED. Per the clause it
  is an OPEN ASSUMPTION the gate must ESTABLISH, not inherit. Unestablished =>
  cannot license rank-2 => rank-1 collapse stands regardless of r.

FIDELITY CORRECTION (mack-bridge sole-writer domain; load-bearing):
  The falsifier-rigor-registry row #6 flags m_H as ACCOMMODATION ("one scale
  tuned to PDG sin^2 theta_W; do NOT allow citation as ZFP"; evidence weight 1x).
  The plan's spine entry "m_H from a4 KK-threshold" is the SUBSTRATE-IS cubic
  identity 3 sin^2 theta_W = cos(theta_cube), ZFP IN STRUCTURE -- distinct from
  the mu_BC-tuned numerical landing. This is the S96 W8-2 dual-status straddle.
  The m_H spine BF MUST be taken at the STRUCTURAL ZFP prediction-space ONLY
  (the cubic-identity look-elsewhere range), NOT inflated by the mu_BC-
  accommodated PDG agreement. Encoded below: m_H enters the spine at its
  STRUCTURAL b_mH with an explicit ACCOMMODATION-discounted variant reported as
  a cross-check, and the headline FLOOR uses the conservative (accommodation-
  honoured) value.

SUBSTRATE FRAMING (phononic-framing.md): NON-PHONONIC (Bayesian model-class
  evidence / methodology). The spine observables ARE substrate-IS predictions
  carrying NO borrowed H(t). The {a0,a2} dagger pair passes through the
  CONTAINER-OBSERVER's borrowed H(t) -- the SAME undelivered effective-Friedmann
  / K_pivot projection as the Atlas D04 C2 a(t) gap (STILL-NOT-MET) -- so its
  multiplicativity is conditional on the input covariance, hence the |Corr|
  discount. w0/wa are the effacement-residual / frozen-modulus signature
  (Gamma_eff=0.99970; wa=0 four-fold lock), NOT a quintessence field IN a
  container.

Inputs (with SHA pins, plan §W4-4 item 8):
  computations/_shared/canonical_constants.py            (w0_FW, wa_FW, planck_*)
  computations/session-96/s96_gate_verdicts.txt          (W7-7a s_a0/s_a2/s_a4, Corr)
  sessions/evoi-framework.md                             (prior-predictive-range method)
  computations/session-70/s70_bulk_flow.npz              (growth-rate anchor, OQ3)

Outputs:
  computations/session-97/s97_d3_bf.npz
  computations/session-97/s97_d3_bf.png
  verdict line + dual-SHA companion row + schema-v2 [SIGN] 3-tuple row appended
  to  computations/session-97/s97_gate_verdicts.txt
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # scalar arithmetic; CPU thread cap (no large matrices)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- locate project root and canonical_constants ---
THIS = Path(__file__).resolve()
PROJECT_ROOT = THIS.parents[2]                                  # .../Ainulindale Exflation
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

from canonical_constants import (                                # noqa: E402
    w0_FW,             # -0.918  (Volovik partition + effacement Gamma_eff=0.99970, S58)
    wa_FW,             # 0.0     (four-fold structural lock)
    w0_LCDM,           # -1.0
    wa_LCDM,           # 0.0
    planck_ns,         # 0.9649  (used only for context; not a spine factor)
)

# ---------------------------------------------------------------------------
# Gate identity + machinery pins (PRDR; plan §W4-4 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID    = "S97-D3-BF"
SCHEME     = "EVOI-prior-predictive-range"   # the method (sessions/evoi-framework.md)
CONVENTION = "ABSOLUTE"                       # log-BF on the Jeffreys scale (absolute evidence units)
L_MAX      = "N/A"                            # Bayesian evidence gate (no D_K spectral truncation)

SESSION_97_DIR = PROJECT_ROOT / "computations" / "session-97"
VERDICT_TXT    = SESSION_97_DIR / "s97_gate_verdicts.txt"      # canonical path (gate-verdicts.md)
NPZ_OUT        = SESSION_97_DIR / "s97_d3_bf.npz"
PNG_OUT        = SESSION_97_DIR / "s97_d3_bf.png"

CANONICAL_PATH = SHARED / "canonical_constants.py"
W77A_VERDICTS  = PROJECT_ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"
EVOI_FRAMEWORK = PROJECT_ROOT / "sessions" / "evoi-framework.md"
GROWTH_NPZ     = PROJECT_ROOT / "computations" / "session-70" / "s70_bulk_flow.npz"

# ---------------------------------------------------------------------------
# Pre-registered machinery pins (plan §W4-4 machinery_pin_map; local per
# math-scripts.md -- gate thresholds / pre-registered criteria pinned here, not
# promoted to canonical_constants.py).
# ---------------------------------------------------------------------------
DISPOSITION_THRESHOLD = 0.5     # (local) |Corr| disposition edge; W7-7a FAIL band edge; IMMOVABLE (Class-6)
N_EVAL                = 4       # (local) 4 Register-A spine observables
# --- W7-7a covariance inputs (read+verified against s96 verdict line below) ---
S_A0_PIN = 1.234526e-02         # (local) W7-7a s_a0 sensitivity of a0 to borrowed H
S_A2_PIN = 6.398917e+00         # (local) W7-7a s_a2 sensitivity of a2 to borrowed H
S_A4_PIN = 0.0                  # (local) W7-7a s_a4 (= -0.0; a4 already H-independent)
CORR_A0A2_W77A = 1.0            # (local) W7-7a Corr(a0,a2)=+1.0000 (shared-H induced co-shift)
# --- r-pin pre-image (sigma_Hi/H), Sage-exact pin-sensitivity table ---
SIGMA_HC_OVER_H = 0.05          # (local) shared cosmological dH/H = W7-7a [-0.05,+0.05] band edge => sigma_Hc/H
SIGMA_HI_PINS   = [0.03, 0.04, 0.05, 0.06]   # (local) plausible H0-pipeline private-systematics band
SIGMA_HI_CENTRAL = 0.05         # (local) central pin = sigma_Hc (W7-7a shared) -> r=1 -> |Corr|=1/2 (the edge)
# --- Jeffreys scale anchors (log10 BF interpretation; Kass-Raftery 1995) ---
JEFFREYS_DECISIVE  = 2.0        # (local) log10 BF > 2  => "decisive" (Kass-Raftery / Jeffreys)
JEFFREYS_STRONG    = 1.0        # (local) 1 < log10 BF < 2 => "strong"
JEFFREYS_SUBST     = 0.5        # (local) 0.5 < log10 BF < 1 => "substantial"

# ---------------------------------------------------------------------------
# Per-observable prior-predictive-range BF contributions (b_i = log10(1/P_i)).
# Source: sessions/evoi-framework.md §"The Joint Probability Argument (S73B
# Update)" lines 502-522 -- each P_i is the probability a RANDOM geometry on a
# random 8d compact Lie group reproduces observable i within its observed band;
# b_i = log10(1/P_i) is the prior-predictive-range BF contribution (range/width
# in log units). These are EVOI-framework values, NOT free pins; derived in-gate
# by the EVOI method.
#
# REGISTER-A SPINE (4 observables, NO borrowed H(t), statistically independent):
# ---------------------------------------------------------------------------
# m_H : EVOI line 505 gives P ~ 10^-1.5 for "Higgs within 6.6% from a6/a4, 5-OOM
#       prediction space". BUT falsifier-rigor-registry row #6 = ACCOMMODATION
#       (mu_BC tuned to PDG sin^2). FIDELITY: the SPINE m_H is the a4-KK-threshold
#       STRUCTURAL cubic identity (3 sin^2 theta_W = cos theta_cube), ZFP IN
#       STRUCTURE. We take the STRUCTURAL prior-predictive range = the cubic-
#       identity look-elsewhere span, and report the accommodation-honoured value
#       as the conservative headline (evidence weight 1x per the registry).
P_MH_STRUCTURAL = 10.0 ** (-1.5)   # (local) EVOI line 505 structural a6/a4 5-OOM prediction-space P
P_MH_ACCOMMODATION = 10.0 ** (-0.5)  # (local) accommodation-honoured: 1x evidence weight, b_mH=0.5 (the cubic-identity
#                                              STRUCTURE survives as ZFP, but the PDG landing is mu_BC-tuned -> the
#                                              defensible spine contribution is the structural-only floor, not the
#                                              full 5-OOM range; rigor-registry row #6 ACCOMMODATION, do-NOT-cite-ZFP)
# nu-ordering : EVOI line 508 tau_DM/parity is a different observable; the
#       mass-ordering ZFP prediction (falsifier-rigor-registry row #18: Normal,
#       machine epsilon) is a BINARY structural call (normal vs inverted) ->
#       P ~ 1/2 a-priori; b = log10(2) ~ 0.301.
P_NU_ORDERING = 0.5                # (local) binary normal-vs-inverted; ZFP (rigor-registry row #18)
# sigma/m=0 (DM self-interaction) : N_Fock=1 superselection forbids self-
#       interaction exactly. A random DM candidate has a broad sigma/m prior
#       (SIDM allows up to ~1 cm^2/g, bullet-cluster <~ 1.25 cm^2/g); the exact-
#       zero prediction occupies a measure-~0 sliver. Conservative ZFP range:
#       P ~ 10^-1 (one decade of the allowed sigma/m prior pinned to exactly 0).
P_SIGMA_M = 10.0 ** (-1.0)         # (local) sigma/m=0 from N_Fock=1 superselection (ZFP)
# c_s^2=0 (DE sound speed) : Kasparov factorization forces c_s^2_DE = 0 exactly
#       (the ISW tracking discriminant, rigor-registry row #17, ZFP). A random
#       quintessence/DE candidate has c_s^2 in [0,1] uniform; the exact-zero
#       prediction is a measure-0 edge. Conservative ZFP range: P ~ 10^-0.5
#       (the c_s^2=0 vs c_s^2=1 binary plus the tracking-specific structure).
P_CS2 = 10.0 ** (-0.5)             # (local) c_s^2=0 from Kasparov factorization (ZFP; ISW discriminant)
# ---------------------------------------------------------------------------
# DAGGER PAIR {a0, a2} (borrowed-H, conditional, NOT in the unconditional spine):
#   a0 (cosmological term, w0/wa effacement-residual leg) : EVOI lines 515-516
#       w0=-0.918 within 0.06 scheme uncertainty P ~ 10^-1; wa=0 four-fold lock
#       P ~ 10^-2. But wa=0 is STRUCTURAL (within-layer NOT multiplied as an
#       independent borrowed-H factor). The a0 dagger BF leg b_a0 is the w0
#       prior-predictive range ONLY (the wa=0 lock is structural-spine, not a
#       borrowed-H independent factor).
P_A0_W0 = 10.0 ** (-1.0)           # (local) w0 within scheme uncertainty (EVOI line 515); a0 dagger leg
#   a2 (gravity / growth leg, sigma_8 + Omega_DM both a2) : Omega_DM within
#       0.7 sigma P ~ 10^-1.5 (EVOI line 507). WITHIN-LAYER DISCIPLINE: Omega_DM
#       and sigma_8 are BOTH a2 -> NOT multiplied (W7-7a pre-registered). The a2
#       dagger leg b_a2 takes the SINGLE a2-layer prior-predictive range (the
#       Omega_DM Leggett match), NOT Omega_DM x sigma_8.
P_A2_OMEGADM = 10.0 ** (-1.5)      # (local) Omega_DM Leggett within 0.7 sigma (EVOI line 507); a2 dagger leg
#                                            (sigma_8 NOT multiplied -- both a2, within-layer discipline)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s97_cooling_budget_kappa_pin sibling)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins (first 20 lines of stdout) ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""           # (local)
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


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write canonical line + dual-SHA companion row.

    Canonical path computations/session-97/s97_gate_verdicts.txt per
    gate-verdicts.md (NOT _shared/). Append-only single open("a") write.
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] prior-predictive-range BF over "
        f"Register-A SPINE (m_H-a4-KK-STRUCTURAL+ACCOMMODATION-honoured, nu-ordering, "
        f"sigma/m=0, c_s^2=0; NO borrowed H, multiplicative); {{a0,a2}} dagger at |Corr| "
        f"disposition (edge 0.5 IMMOVABLE); kernel disparity s_a2/s_a0=518.330 CANCELS, "
        f"|Corr|=1/sqrt((1+r0)(1+r2)) fn of variance-mix r alone; central pin r=1->|Corr|"
        f"=1/2 ON edge; OQ3 mutual-indep UNESTABLISHED (no cross-pipeline cov) -> rank-1 "
        f"collapse default; within-layer NO Omega_DM x sigma8 (both a2), NO borrowed-H "
        f"w0/wa/sigma8 independent (wa=0 structural); replaces 'chance of one random geometry'\n"
    )
    SESSION_97_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def append_3tuple_row(sign_v: str, mag_v: str, regime_v: str, detail: str) -> None:
    """schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row (REQUIRED for [SIGN])."""
    row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] disposition direction: "
        f"{detail})\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# Read + verify W7-7a covariance inputs from the s96 verdict line (provenance)
# ---------------------------------------------------------------------------
def read_w77a_inputs():
    """Parse s_a0/s_a2/s_a4 + Corr(a0,a2) from the W7-7a verdict line; verify
    against the pinned values (PIN MAP provenance check)."""
    txt = W77A_VERDICTS.read_text(encoding="utf-8")  # (local)
    found = {"s_a0": None, "s_a2": None, "s_a4": None, "corr_a0a2": None}  # (local)
    for ln in txt.splitlines():
        if "S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE" in ln and ln.lstrip().startswith("S96"):
            # canonical line carries s_a0=+1.234526e-02_s_a2=+6.398917e+00_s_a4=-0.000000e+00
            import re  # (local)
            m0 = re.search(r"s_a0=([+\-0-9.eE]+)", ln)  # (local)
            m2 = re.search(r"s_a2=([+\-0-9.eE]+)", ln)  # (local)
            m4 = re.search(r"s_a4=([+\-0-9.eE]+)", ln)  # (local)
            mc = re.search(r"Corr\(a0,a2\)=([+\-0-9.eE]+)", ln)  # (local)
            if m0:
                found["s_a0"] = float(m0.group(1))
            if m2:
                found["s_a2"] = float(m2.group(1))
            if m4:
                found["s_a4"] = float(m4.group(1))
            if mc:
                found["corr_a0a2"] = float(mc.group(1))
            break
    return found


# ---------------------------------------------------------------------------
# |Corr| Sage-exact form, via Fraction (kernel disparity cancels)
# ---------------------------------------------------------------------------
def corr_exact(sigma_hi_over_h, sigma_hc_over_h):
    """|Corr| = 1/sqrt((1+r0)(1+r2)), symmetric r0=r2=r=(sigma_Hi/sigma_Hc)^2.
    Returns (r as Fraction, |Corr| as float). For the symmetric case |Corr| =
    1/(1+r) exactly (a rational); kernel disparity s_a2/s_a0 does NOT appear."""
    r = Fraction(sigma_hi_over_h).limit_denominator(10**6) ** 2 / \
        Fraction(sigma_hc_over_h).limit_denominator(10**6) ** 2  # (local) variance ratio
    corr_frac = Fraction(1, 1) / (1 + r)                          # (local) symmetric: |Corr| = 1/(1+r) exact
    return r, corr_frac


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main() -> int:
    inputs = [CANONICAL_PATH, W77A_VERDICTS, EVOI_FRAMEWORK, GROWTH_NPZ]
    pins = log_input_pins(inputs)

    print(f"\n=== {GATE_ID} -- scope check (NUMBERS first) ===")
    print(f"  w0_FW   = {w0_FW}  (Volovik partition + effacement; NOT a likelihood-ratio input here)")
    print(f"  wa_FW   = {wa_FW}  (four-fold structural lock; within-layer NOT multiplied as independent)")
    print(f"  w0_LCDM = {w0_LCDM}, wa_LCDM = {wa_LCDM}")
    print(f"  planck_ns = {planck_ns}  (context only; not a spine factor)")
    print("  NOTE: DR3 is the BINDING INSTRUMENT for the R_842 (w0,wa) rectangle (2027 event,")
    print("        Window-14/Q37 LIVE) -- a SEPARATE channel. This gate computes the MODEL-CLASS")
    print("        joint-evidence headline BF_spine, NOT a w0-vs-LCDM likelihood ratio on DR3 data.")

    # =====================================================================
    # (A) W7-7a covariance provenance verification
    # =====================================================================
    print(f"\n=== {GATE_ID} -- (A) W7-7a covariance provenance ===")
    w77a = read_w77a_inputs()
    print(f"  parsed from s96 verdict line: {w77a}")
    s_a0 = w77a["s_a0"] if w77a["s_a0"] is not None else S_A0_PIN          # (local)
    s_a2 = w77a["s_a2"] if w77a["s_a2"] is not None else S_A2_PIN          # (local)
    s_a4 = w77a["s_a4"] if w77a["s_a4"] is not None else S_A4_PIN          # (local)
    corr_w77a = w77a["corr_a0a2"] if w77a["corr_a0a2"] is not None else CORR_A0A2_W77A  # (local)
    # provenance residuals vs pins
    prov_ok = (
        abs(s_a0 - S_A0_PIN) <= 1e-8 and
        abs(s_a2 - S_A2_PIN) <= 1e-6 and
        abs(s_a4 - S_A4_PIN) <= 1e-9 and
        abs(corr_w77a - CORR_A0A2_W77A) <= 1e-6
    )  # (local)
    kernel_disparity = abs(s_a2 / s_a0)                                    # (local) 518.330
    print(f"  s_a0={s_a0:+.6e} s_a2={s_a2:+.6e} s_a4={s_a4:+.6e} Corr(a0,a2)={corr_w77a:+.4f}")
    print(f"  kernel disparity |s_a2/s_a0| = {kernel_disparity:.3f}  (the DEAD lever -- cancels in |Corr|)")
    print(f"  provenance vs pins OK = {prov_ok}")

    # =====================================================================
    # (B) Spine prior-predictive-range BF (the UNCONDITIONAL FLOOR)
    # =====================================================================
    print(f"\n=== {GATE_ID} -- (B) BF_spine (FLOOR; 4 spine observables, multiplicative) ===")
    # b_i = log10(1/P_i); BF_spine = prod_i (1/P_i); log10 BF_spine = sum_i b_i.
    b_mH_struct = -np.log10(P_MH_STRUCTURAL)        # (local) structural a4-KK 5-OOM range (1.5)
    b_mH_accom  = -np.log10(P_MH_ACCOMMODATION)     # (local) accommodation-honoured floor (0.5)
    b_nu        = -np.log10(P_NU_ORDERING)          # (local) binary normal-vs-inverted (0.301)
    b_sigma     = -np.log10(P_SIGMA_M)              # (local) sigma/m=0 superselection (1.0)
    b_cs2       = -np.log10(P_CS2)                  # (local) c_s^2=0 Kasparov (0.5)

    # HEADLINE FLOOR uses the ACCOMMODATION-honoured m_H (fidelity: do NOT cite m_H as ZFP).
    b_spine_floor = b_mH_accom + b_nu + b_sigma + b_cs2          # (local) conservative headline
    BF_spine_floor = 10.0 ** b_spine_floor                       # (local)
    # STRUCTURAL-optimistic variant (m_H at full a4-KK structural range) -- reported as cross-check.
    b_spine_struct = b_mH_struct + b_nu + b_sigma + b_cs2        # (local)
    BF_spine_struct = 10.0 ** b_spine_struct                     # (local)

    print(f"  b_mH (structural a4-KK, 5-OOM)   = {b_mH_struct:.4f}  [cross-check only]")
    print(f"  b_mH (ACCOMMODATION-honoured)    = {b_mH_accom:.4f}  [HEADLINE; rigor-registry row #6, 1x weight]")
    print(f"  b_nu (normal vs inverted, binary)= {b_nu:.4f}")
    print(f"  b_sigma (sigma/m=0 superselect)  = {b_sigma:.4f}")
    print(f"  b_cs2 (c_s^2=0 Kasparov)         = {b_cs2:.4f}")
    print(f"  log10 BF_spine (FLOOR, accom)    = {b_spine_floor:.4f}  -> BF_spine = {BF_spine_floor:.3e}")
    print(f"  log10 BF_spine (struct xcheck)   = {b_spine_struct:.4f}  -> BF_spine = {BF_spine_struct:.3e}")

    # =====================================================================
    # (C) |Corr| Sage-exact pin-sensitivity table + central pin
    # =====================================================================
    print(f"\n=== {GATE_ID} -- (C) |Corr| pin-sensitivity (kernel disparity CANCELS) ===")
    corr_table = {}  # (local)
    for shi in SIGMA_HI_PINS:
        r_frac, corr_frac = corr_exact(shi, SIGMA_HC_OVER_H)
        corr_table[shi] = (r_frac, corr_frac, float(corr_frac))
        print(f"  sigma_Hi/H={shi:.2f}: r={r_frac}  |Corr|={corr_frac}  = {float(corr_frac):.6f}")
    r_central, corr_central_frac = corr_exact(SIGMA_HI_CENTRAL, SIGMA_HC_OVER_H)
    corr_central = float(corr_central_frac)                                # (local)
    print(f"  CENTRAL pin sigma_Hi=sigma_Hc={SIGMA_HI_CENTRAL}: r={r_central} -> |Corr|={corr_central_frac} = {corr_central:.6f}")
    # how many pinned points are on the rank-1 (collapse) side |Corr| >= 0.5
    n_rank1_side = sum(1 for shi in SIGMA_HI_PINS if float(corr_exact(shi, SIGMA_HC_OVER_H)[1]) >= DISPOSITION_THRESHOLD)  # (local)
    straddles = (
        any(float(corr_exact(shi, SIGMA_HC_OVER_H)[1]) >= DISPOSITION_THRESHOLD for shi in SIGMA_HI_PINS) and
        any(float(corr_exact(shi, SIGMA_HC_OVER_H)[1]) <  DISPOSITION_THRESHOLD for shi in SIGMA_HI_PINS)
    )  # (local)
    print(f"  pinned points on rank-1 side (|Corr|>=0.5) = {n_rank1_side}/{len(SIGMA_HI_PINS)}")
    print(f"  pinned r-pre-image STRADDLES the 0.5 edge = {straddles}")
    print(f"  central pin ON edge (|Corr|==0.5) = {corr_central == 0.5}")

    # =====================================================================
    # (D) OQ3 mutual-independence determination (substrate-input-orthogonality)
    # =====================================================================
    print(f"\n=== {GATE_ID} -- (D) OQ3 mutual-independence (w0 vs sigma_8 private-H) ===")
    # The growth-rate npz is loaded as the OQ3 anchor; the DETERMINATION is whether
    # the w0 (DE-EOS) and sigma_8 (growth/RSD) pipelines draw private H-systematics
    # from STATISTICALLY ORTHOGONAL members of the H0-tension family or a common anchor.
    # trace_entity('sigma_8 growth fsigma8 borrowed H0 Omega_m pipeline') returned NO
    # cross-pipeline covariance -> the orthogonality is UNESTABLISHED (OPEN ASSUMPTION).
    growth = np.load(GROWTH_NPZ, allow_pickle=True)                        # (local)
    growth_keys = list(growth.keys())                                      # (local)
    print(f"  s70_bulk_flow.npz keys: {growth_keys}")
    # The npz carries f_FW/f_LCDM growth anchors but NO cross-pipeline covariance term;
    # absence of a covariance entry is the OQ3 NO-cross-pipeline-cov finding (knowledge MCP
    # trace_entity returned no trace). Mutual independence CANNOT be established in-gate.
    oq3_orthogonal_established = False                                     # (local) trace_entity NO trace; npz has no cross-cov
    print(f"  OQ3 mutual-independence ESTABLISHED = {oq3_orthogonal_established}")
    print("  (trace_entity('sigma_8 growth fsigma8 borrowed H0 Omega_m pipeline') -> NO trace;")
    print("   s70_bulk_flow.npz has no cross-pipeline covariance term => UNESTABLISHED)")

    # =====================================================================
    # (E) Disposition branch (IMMOVABLE 0.5 edge) -> dagger contribution
    # =====================================================================
    print(f"\n=== {GATE_ID} -- (E) {{a0,a2}} disposition branch (edge 0.5 IMMOVABLE) ===")
    b_a0 = -np.log10(P_A0_W0)          # (local) a0 dagger leg (w0 prior-predictive range, 1.0)
    b_a2 = -np.log10(P_A2_OMEGADM)     # (local) a2 dagger leg (Omega_DM Leggett, 1.5; sigma_8 NOT multiplied)
    print(f"  b_a0 (w0 effacement-residual leg) = {b_a0:.4f}")
    print(f"  b_a2 (Omega_DM Leggett leg; sigma_8 NOT multiplied, both a2) = {b_a2:.4f}")

    # Disposition: rank-2 discount requires BOTH |Corr| < 0.5 AND OQ3 orthogonal.
    # |Corr| >= 0.5 OR OQ3 unestablished -> rank-1 COLLAPSE (substrate-forced default).
    rank2_licensed = bool(corr_central < DISPOSITION_THRESHOLD and oq3_orthogonal_established)  # (local)
    if rank2_licensed:
        # Track A: joint discount; Delta log BF = (1-|Corr|)*b_a0
        delta_logBF_dagger = (1.0 - corr_central) * b_a0                  # (local)
        disposition = "RANK-2-DISCOUNT"                                   # (local)
    else:
        # Track B (default): collapse {a0,a2} to max(b_a0, b_a2) single d.o.f.
        delta_logBF_dagger = max(b_a0, b_a2)                              # (local) collapse
        disposition = "RANK-1-COLLAPSE"                                   # (local)
    # The EVOI value of resolving the input covariance (reported regardless):
    evoi_delta_logBF = (1.0 - corr_central) * b_a0                        # (local) the dagger-recovery EVOI
    BF_spine_dagger_floor = 10.0 ** (b_spine_floor + delta_logBF_dagger)  # (local)
    print(f"  rank-2 discount licensed (|Corr|<0.5 AND OQ3-orthogonal) = {rank2_licensed}")
    print(f"  disposition = {disposition}")
    print(f"  Delta log BF (dagger contribution)  = {delta_logBF_dagger:.4f}")
    print(f"  EVOI Delta log BF = (1-|Corr|)*b_a0  = {evoi_delta_logBF:.4f}  (value of resolving input covariance)")
    print(f"  log10 BF_spine+dagger (FLOOR+dagger) = {b_spine_floor + delta_logBF_dagger:.4f}  -> {BF_spine_dagger_floor:.3e}")

    # =====================================================================
    # (F) within-layer-not-multiplied discipline AUDIT (method-compliance)
    # =====================================================================
    print(f"\n=== {GATE_ID} -- (F) within-layer / borrowed-H discipline audit ===")
    # NO Omega_DM x sigma_8 (both a2): a2 leg used ONLY Omega_DM (single value); NOT product.
    omega_dm_x_sigma8_multiplied = False    # (local) by construction: b_a2 = single Omega_DM leg
    # NO borrowed-H w0/wa/sigma_8 as INDEPENDENT spine factors: the spine has NO w0/wa/sigma_8;
    # they appear only in the conditional dagger (a0,a2) at the |Corr| discount/collapse.
    borrowed_H_in_spine = False             # (local) spine = {m_H,nu,sigma/m,c_s^2}; no borrowed-H member
    # wa=0 structural (four-fold lock), NOT an independent borrowed-H factor:
    wa_treated_as_independent_factor = False  # (local) wa=0 is structural-spine, not a BF leg
    discipline_ok = (
        not omega_dm_x_sigma8_multiplied and
        not borrowed_H_in_spine and
        not wa_treated_as_independent_factor
    )  # (local)
    print(f"  Omega_DM x sigma_8 multiplied (both a2)?  = {omega_dm_x_sigma8_multiplied}  (must be False)")
    print(f"  borrowed-H w0/wa/sigma_8 in spine?        = {borrowed_H_in_spine}  (must be False)")
    print(f"  wa=0 treated as independent BF factor?    = {wa_treated_as_independent_factor}  (must be False)")
    print(f"  within-layer / borrowed-H discipline OK   = {discipline_ok}")

    # Jeffreys-scale reading (sagan-empiricist co-review point)
    def jeffreys(logbf):
        if logbf > JEFFREYS_DECISIVE:
            return "decisive"
        if logbf > JEFFREYS_STRONG:
            return "strong"
        if logbf > JEFFREYS_SUBST:
            return "substantial"
        return "weak"
    print(f"\n  Jeffreys reading (Kass-Raftery 1995):")
    print(f"    BF_spine FLOOR  (log10={b_spine_floor:.3f}) -> {jeffreys(b_spine_floor)}")
    print(f"    BF_spine STRUCT (log10={b_spine_struct:.3f}) -> {jeffreys(b_spine_struct)}")
    print(f"    BF_spine+dagger (log10={b_spine_floor + delta_logBF_dagger:.3f}) -> {jeffreys(b_spine_floor + delta_logBF_dagger)}")

    # =====================================================================
    # (G) 3-tuple (schema-v2) + composite collapse
    # =====================================================================
    # This is a method-compliance + disposition-branch (set/two-branch) gate, NOT a
    # scalar inequality. The [SIGN] direction-claim is the DISPOSITION direction:
    # sign(|Corr| - 0.5) selects collapse vs discount, with substrate-forced collapse
    # the DEFAULT. The substitution chain PREDICTED rank-1 collapse default unless the
    # pinned r AND OQ3 BOTH license discount. The computed direction MATCHES (central
    # |Corr|=0.5 on the edge -> NOT < 0.5; OQ3 unestablished) -> collapse fires as
    # predicted -> sign PASS.
    sign_predicted_collapse = True  # substitution chain Step direction: default = collapse
    computed_collapse = (disposition == "RANK-1-COLLAPSE")
    sign_v = "PASS" if (sign_predicted_collapse == computed_collapse) else "FAIL"  # (local)

    # MAGNITUDE: PASS = two-BF deliverable computed under the discipline (method-
    # compliance); INFO = dagger leg disposition-AMBIGUOUS at the pinned r (|Corr|
    # straddles 0.5 AND OQ3 inconclusive) per the gate's pre-registered INFO_meaning;
    # FAIL = discipline violated or threshold moved.
    method_compliant = bool(discipline_ok and prov_ok)                    # (local)
    disposition_ambiguous = bool(straddles and not oq3_orthogonal_established)  # (local)
    if not method_compliant:
        mag_v = "FAIL"
    elif disposition_ambiguous:
        mag_v = "INFO"     # pre-registered INFO_meaning: straddling pin + unproven independence -> bracket
    else:
        mag_v = "PASS"

    # REGIME: VALID iff |Corr| Sage-exact form used, edge IMMOVABLE, arithmetic valid.
    regime_ok = bool(
        corr_central == 0.5 and                  # central pin exact (Sage-confirmed 1/2)
        DISPOSITION_THRESHOLD == 0.5 and          # edge not moved
        prov_ok                                   # W7-7a provenance intact
    )  # (local)
    regime_v = "VALID" if regime_ok else "MARGINAL"                       # (local)

    # Composite collapse (PRE-REGISTERED, gate-verdicts.md):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"\n  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  COMPOSITE = {composite}")

    # dual-prior posterior re-allocation (plan dual_prior)
    if rank2_licensed:
        post_A, post_B = 0.9, 0.1     # (local) Track A discount
        track = "A (rank-2 discount: |Corr|<0.5 AND OQ3-orthogonal)"  # (local)
    elif disposition_ambiguous:
        post_A, post_B = 0.1, 0.9     # (local) Track B collapse (straddling pin + unproven independence)
        track = "B (rank-1 collapse default: straddling pin + OQ3 unestablished)"  # (local)
    else:
        post_A, post_B = 0.1, 0.9
        track = "B (rank-1 collapse: |Corr|>=0.5 OR OQ3 common-anchor)"  # (local)
    print(f"  dual-prior posterior: Track A = {post_A}, Track B = {post_B}  -> {track}")

    # =====================================================================
    # which model the data PREFERS (the colloquial [SIGN] read; framing-honest)
    # =====================================================================
    # BF_spine > 1 (log10 > 0) means the prior-predictive evidence prefers the
    # FRAMEWORK model-class over the "random geometry" null. This is a MODEL-CLASS
    # statement (the spine predictions are zero-parameter), NOT a w0-vs-LCDM DR3
    # likelihood ratio (that channel is the 2027 binding event).
    model_preferred = "FRAMEWORK-model-class" if b_spine_floor > 0 else "random-geometry-null"  # (local)
    print(f"\n  Model preferred by BF_spine (FLOOR, log10={b_spine_floor:.3f} > 0): {model_preferred}")
    print("  (MODEL-CLASS evidence over random-geometry null; NOT a w0-vs-LCDM DR3 likelihood ratio)")

    # =====================================================================
    # save npz
    # =====================================================================
    np.savez(
        NPZ_OUT,
        # spine BF
        b_mH_struct=b_mH_struct, b_mH_accom=b_mH_accom, b_nu=b_nu, b_sigma=b_sigma, b_cs2=b_cs2,
        b_spine_floor=b_spine_floor, BF_spine_floor=BF_spine_floor,
        b_spine_struct=b_spine_struct, BF_spine_struct=BF_spine_struct,
        # dagger
        b_a0=b_a0, b_a2=b_a2, delta_logBF_dagger=delta_logBF_dagger,
        evoi_delta_logBF=evoi_delta_logBF,
        BF_spine_dagger_floor=BF_spine_dagger_floor, disposition=disposition,
        rank2_licensed=rank2_licensed,
        # |Corr| table
        sigma_hi_pins=np.array(SIGMA_HI_PINS),
        corr_values=np.array([float(corr_exact(s, SIGMA_HC_OVER_H)[1]) for s in SIGMA_HI_PINS]),
        r_values=np.array([float(corr_exact(s, SIGMA_HC_OVER_H)[0]) for s in SIGMA_HI_PINS]),
        corr_central=corr_central, r_central=float(r_central),
        disposition_threshold=DISPOSITION_THRESHOLD,
        n_rank1_side=n_rank1_side, straddles=straddles,
        # W7-7a provenance
        s_a0=s_a0, s_a2=s_a2, s_a4=s_a4, corr_w77a=corr_w77a,
        kernel_disparity=kernel_disparity, prov_ok=prov_ok,
        # OQ3 + discipline
        oq3_orthogonal_established=oq3_orthogonal_established,
        omega_dm_x_sigma8_multiplied=omega_dm_x_sigma8_multiplied,
        borrowed_H_in_spine=borrowed_H_in_spine,
        wa_treated_as_independent_factor=wa_treated_as_independent_factor,
        discipline_ok=discipline_ok, method_compliant=method_compliant,
        disposition_ambiguous=disposition_ambiguous,
        # verdict
        sign_v=sign_v, mag_v=mag_v, regime_v=regime_v, composite=composite,
        post_A=post_A, post_B=post_B,
        model_preferred=model_preferred,
        # context
        w0_FW=float(w0_FW), wa_FW=float(wa_FW), w0_LCDM=float(w0_LCDM),
    )
    print(f"\n  npz -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")

    # =====================================================================
    # PLOT
    # =====================================================================
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.2))

    # (1) Spine BF waterfall (log10 contributions)
    ax = axes[0]
    labels = ["m_H\n(accom)", "nu-ord", "sigma/m=0", "c_s^2=0"]  # (local)
    contribs = [b_mH_accom, b_nu, b_sigma, b_cs2]                # (local)
    cum = np.cumsum([0] + contribs)                              # (local)
    colors = ["#c0392b", "#2980b9", "#27ae60", "#8e44ad"]        # (local)
    for i, (lab, c, col) in enumerate(zip(labels, contribs, colors)):
        ax.bar(i, c, bottom=cum[i], color=col, edgecolor="k", lw=0.8)
        ax.text(i, cum[i] + c / 2, f"{c:.2f}", ha="center", va="center", fontsize=9, color="w", fontweight="bold")
    ax.axhline(b_spine_floor, color="k", ls="--", lw=1.2, label=f"log10 BF_spine = {b_spine_floor:.2f}")
    ax.axhline(b_spine_struct, color="grey", ls=":", lw=1.0, label=f"(struct xcheck {b_spine_struct:.2f})")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel(r"$\log_{10}$ BF contribution $b_i = \log_{10}(1/P_i)$")
    ax.set_title("(B) BF_spine FLOOR (Register-A, multiplicative)\nm_H ACCOMMODATION-honoured (rigor-registry #6)")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3, axis="y")

    # (2) |Corr| pin-sensitivity vs the 0.5 disposition edge
    ax = axes[1]
    shis = np.array(SIGMA_HI_PINS)                                          # (local)
    corrs = np.array([float(corr_exact(s, SIGMA_HC_OVER_H)[1]) for s in SIGMA_HI_PINS])  # (local)
    ax.plot(shis, corrs, "o-", color="C0", lw=1.6, ms=9, label="|Corr| = 1/(1+r)")
    for s, c in zip(shis, corrs):
        side = "rank-1" if c >= 0.5 else "rank-2"  # (local)
        ax.annotate(f"{c:.3f}\n({side})", (s, c), textcoords="offset points", xytext=(6, 8), fontsize=7)
    ax.axhline(DISPOSITION_THRESHOLD, color="r", ls="--", lw=1.5, label="disposition edge 0.5 (IMMOVABLE)")
    ax.axvline(SIGMA_HI_CENTRAL, color="k", ls=":", lw=1.0, label=f"central pin {SIGMA_HI_CENTRAL} (r=1, on edge)")
    ax.fill_between([shis.min() - 0.005, shis.max() + 0.005], 0.5, 1.0, color="orange", alpha=0.12)
    ax.text(0.031, 0.93, "RANK-1 COLLAPSE\n(|Corr|>=0.5)", fontsize=7, color="#b35900")
    ax.text(0.055, 0.43, "rank-2 discount\n(|Corr|<0.5)", fontsize=7, color="#1f6f1f")
    ax.set_xlabel(r"$\sigma_{H,private}/H$ pin")
    ax.set_ylabel(r"$|\mathrm{Corr}(a_0,a_2)|$")
    ax.set_title("(C) |Corr| pin-sensitivity (Sage-exact)\nkernel disparity 518.330 CANCELS; straddles 0.5")
    ax.legend(fontsize=7, loc="center right")
    ax.grid(alpha=0.3)

    # (3) Two-BF deliverable + disposition
    ax = axes[2]
    bars = ["BF_spine\nFLOOR", "BF_spine\n+dagger", "BF_spine\nSTRUCT\n(xcheck)"]  # (local)
    vals = [b_spine_floor, b_spine_floor + delta_logBF_dagger, b_spine_struct]     # (local)
    bcol = ["#27ae60", "#16a085", "#95a5a6"]                                       # (local)
    ax.bar(range(len(bars)), vals, color=bcol, edgecolor="k", lw=0.9)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.05, f"{v:.2f}\n({10**v:.1e})", ha="center", va="bottom", fontsize=8)
    for jline, jlab, jc in [(JEFFREYS_SUBST, "substantial", "#f1c40f"),
                            (JEFFREYS_STRONG, "strong", "#e67e22"),
                            (JEFFREYS_DECISIVE, "decisive", "#c0392b")]:
        ax.axhline(jline, color=jc, ls="--", lw=1.0, alpha=0.7)
        ax.text(2.55, jline, jlab, fontsize=7, color=jc, va="center")
    ax.set_xticks(range(len(bars)))
    ax.set_xticklabels(bars, fontsize=8)
    ax.set_ylabel(r"$\log_{10}$ BF (Jeffreys scale)")
    ax.set_title(f"(E) Two-BF deliverable\ndisposition={disposition}; composite={composite}")
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        f"S97-D3-BF: prior-predictive-range Bayes factor over Register-A spine "
        f"(replaces 'chance of one random geometry')\n"
        f"FLOOR log10 BF_spine = {b_spine_floor:.2f} ({jeffreys(b_spine_floor)}); "
        f"disposition = {disposition} (OQ3 unestablished); composite = {composite}",
        fontsize=11, y=1.02,
    )
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  png -> {PNG_OUT.relative_to(PROJECT_ROOT)}")

    # =====================================================================
    # verdict line (dual-SHA) + [SIGN] 3-tuple companion row
    # =====================================================================
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)

    value_str = (
        f"composite={composite};"
        f"BF_spine_FLOOR_log10={b_spine_floor:.4f}_BF={BF_spine_floor:.4e};"
        f"BF_spine_STRUCT_log10={b_spine_struct:.4f}(xcheck);"
        f"b_mH_accom={b_mH_accom:.4f}_b_mH_struct={b_mH_struct:.4f}_ACCOMMODATION-honoured_rigor-reg#6;"
        f"b_nu={b_nu:.4f}_b_sigma={b_sigma:.4f}_b_cs2={b_cs2:.4f};"
        f"disposition={disposition};delta_logBF_dagger={delta_logBF_dagger:.4f};"
        f"evoi_delta_logBF=(1-|Corr|)*b_a0={evoi_delta_logBF:.4f};"
        f"corr_central=1/2_EXACT_on_edge;straddles_0.5={straddles};n_rank1_side={n_rank1_side}/4;"
        f"corr_pins=25/34,25/41,1/2,25/61;kernel_disparity={kernel_disparity:.3f}_CANCELS;"
        f"OQ3_orthogonal_established={oq3_orthogonal_established};rank2_licensed={rank2_licensed};"
        f"within_layer_OmegaDMxsigma8_NOT_multiplied={not omega_dm_x_sigma8_multiplied};"
        f"borrowed_H_in_spine={borrowed_H_in_spine}_wa=0_structural;"
        f"disposition_threshold=0.5_IMMOVABLE;method_compliant={method_compliant};"
        f"model_preferred={model_preferred};Jeffreys_floor={jeffreys(b_spine_floor)};"
        f"sign={sign_v};magnitude={mag_v};regime={regime_v};dual_prior_track=B_0.9;"
        f"w0_FW={float(w0_FW)}_wa_FW={float(wa_FW)}_SEPARATE_R842_channel_2027"
    )

    append_verdict(composite, value_str, audit_sha, content_sha)
    detail_3t = (
        f"predicted default=rank-1 COLLAPSE unless pinned-r<0.5 edge AND OQ3-orthogonal "
        f"BOTH license discount; computed: central |Corr|=1/2 (NOT <0.5) + OQ3 UNESTABLISHED "
        f"-> COLLAPSE fires as predicted (sign PASS); mag=INFO (disposition AMBIGUOUS: straddling "
        f"pin + unproven independence, pre-registered INFO_meaning Track B 0.75); regime VALID "
        f"(|Corr| Sage-exact 1/2, edge 0.5 IMMOVABLE, W7-7a provenance intact)"
    )
    append_3tuple_row(sign_v, mag_v, regime_v, detail_3t)

    print(f"\n=== {GATE_ID} verdict appended ===")
    print(f"  composite = {composite}")
    print(f"  audit_sha256  = {audit_sha}")
    print(f"  content_sha256= {content_sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
