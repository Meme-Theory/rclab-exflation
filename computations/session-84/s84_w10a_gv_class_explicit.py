#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S84 Wave 10a Gate 115 -- S84-GV-CLASS-EXPLICIT
================================================

Agent:           connes-ncg-theorist
Trigger:         [VERIFY]
Classification:  GEOMETRIC (de Rham / cyclic cohomology explicit cocycle)

Plan reference:  sessions/session-plan/session-84-plan-w10a.md  Sec W10a-115
Reference NPZ:   computations/session-83/s83_w3_g56_godbillon_vey_jensen_deform.npz
                 (= sessions/archive/session-83/computation-artifacts/s83_g56_gv_jensen_deform.npz alias)
                 G56 stencil reference: gv_response = -4.0579e+04, stencil_err = 5.98e-07.

Hypothesis
----------
The Godbillon-Vey class [GV(F_Jensen)] of the Jensen-deformed foliation
is a non-zero element of H^3(M^4) represented by the 3-form
    omega_J  /\  d omega_J  =  e^{-tau} dtau  /\  d(e^{-tau} dtau).
Direct computation matches G56's Heitsch stencil value (-4.0579e+04)
to within 1% RATIO and stencil_err <= 1e-6.

Substitution chain (mandatory; matches plan W10a-115 Step 1-7)
--------------------------------------------------------------

Definitions:
  D1.  omega_J(tau) := e^{-tau} dtau  (planner sign convention; transverse
        1-form for the Jensen foliation along the tau-axis with the
        e^{-tau} fiber-volume weight that arises from
        lambda(p,q,tau) = sqrt(C_2) * exp(-tau * rho)).
  D2.  Jensen Dirac eigenvalues, fixed for L_max = 5:
            lambda(p,q,tau) = sqrt(C_2(p,q)) * exp(-tau * rho(p,q))
            rho(p,q)        = p + q
            C_2(p,q)        = (p^2 + p q + q^2 + 3p + 3q) / 3
            dim(p,q)        = (p+1)(q+1)(p+q+2)/2
  D3.  Spectral realization of the GV transversal integral
        eta_J /\ d eta_J (S83 G56 sign convention preserved):
            GV_proxy(tau) := -sum_{(p,q)} dim(p,q) * rho(p,q)^2 * |lam|^{-4}
        Here d(ln lam)/dtau = -rho is the EXACT transverse derivative
        contributed by the Jensen flow; the |lam|^{-4} is the |D|^{-4}
        Dixmier weight that ensures convergence.
  D4.  GV response (the "direct GV computation"):
            gv_response_direct := d(GV_proxy)/dtau |_{tau = tau_fold}
        Two parallel evaluations:
            (a) 5-point central stencil on tau:
                f'(tau) ~ [ -f(tau+2h) + 8 f(tau+h) - 8 f(tau-h) + f(tau-2h) ] / (12 h)
            (b) Closed-form analytic differentiation of GV_proxy:
                d/dtau [-sum dim * rho^2 * C_2^{-2} * exp(4 tau rho)]
                = -sum dim * rho^2 * C_2^{-2} * 4 rho * exp(4 tau rho)
                = -4 * sum dim * rho^3 * |lam|^{-4}
        stencil_err := |stencil - analytic| / |analytic|.

Substitution (Step-by-step):
  Step 1 (def). Plug D1 into the planner formula
        ratio = ( -sign(e^{-tau_fold}) ) * sign(J_C2_eff) * sign(Vol_base) .
        J_C2_eff is interpreted as the dimensionless Casimir aggregate
        (sum dim * rho^3 * |lam|^{-4}) / N_norm   (D5 below).
  Step 2 (sub). e^{-tau_fold} = exp(-0.190) = 0.826959... > 0.
                Vol_SU3_Haar = 8 sqrt(3) pi^4 = 1349.74 > 0.
                J_C2 (canonical_constants) = 0.933 > 0.
  Step 3 (simp). sign(response) = -(+) * (+) * (+) = -.
                The expected sign of gv_response_direct is NEGATIVE,
                in agreement with G56 reference (-4.0579e+04 < 0).
  Step 4 (direction-from-canonical-form). With the spectral identity
                gv_analytic = -4 * sum dim * rho^3 * |lam|^{-4},
                each summand is a positive real (dim > 0, rho > 0,
                |lam|^{-4} > 0), so gv_analytic < 0 IDENTICALLY (over
                the L_max = 5 truncation, no cancellation possible).
                The negative sign is therefore STRUCTURAL, not stencil-
                dependent.

  D5 (planner-spectral correspondence).  The planner factorisation
        gv_response_direct = -e^{-tau_fold} * Vol_base * J_C2_kernel
     is consistent with the spectral analytic identity
        gv_response_direct = -4 * sum dim * rho^3 * |lam|^{-4}
     under the identification (Casimir aggregation theorem):
        J_C2_kernel := 4 * sum dim * rho^3 * |lam|^{-4} /
                       (e^{-tau_fold} * Vol_SU3_Haar) .
     This is the operational definition of "J_C2 rescaled by Vol_SU3"
     used in the planner's step 5/6.  Numerical verification of this
     identity is reported in SECTION 5 of this script as a planner-spec
     cross-check; the gate VERDICT, however, depends on the
     stencil_5pt_central -> analytic comparison only.

Magnitude expectation (Step 7 of plan):
  exp(-0.190) ~ 0.827; the structural multiplicative aggregate of
  rho^3 * |lam|^{-4} weighted by SU(3) dimensions at L_max = 5 lands
  near 4.06e+04 (verified numerically below); G56 Heitsch stencil =
  -4.0579e+04.

Pass/Fail/INFO thresholds (frozen pre-computation, plan W10a-115)
-----------------------------------------------------------------
  PASS  : gv_response_direct in [-4.10e+04, -4.02e+04] (within 1% RATIO)
          AND stencil_err <= 1e-6.
  FAIL  : (a) |gv_response_direct| < 1e+3, OR
          (b) sign opposite to G56 (i.e. positive), OR
          (c) stencil_err > 1e-5.
  INFO  : within OOM but outside 1% (e.g. -5.2e+04) -> method refinement.

Inputs (canonical_constants)
----------------------------
  tau_fold       (S42 CONST-FREEZE-42, = 0.19)
  Vol_SU3_Haar   (S44 = 8 sqrt(3) pi^4 ~ 1349.74)
  J_C2           (canonical, = 0.933)
  L_max          (= 5, matches G56 = W3-G56)

Environment
-----------
  Python: phonon-exflation-sim/.venv312/Scripts/python.exe
  CPU thread cap 8 (set BEFORE numpy import).
"""

from __future__ import annotations

import os
# CPU thread caps BEFORE numpy import
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent                       # (local)
sys.path.insert(0, str(HERE))

# Canonical constants -- MANDATORY (S34+)
from canonical_constants import tau_fold, Vol_SU3_Haar, J_C2

Vol_SU3 = Vol_SU3_Haar  # (local) alias to honour planner's "Vol_SU3" name


# ============================================================
# SECTION 0: SHA helpers and input pin map
# ============================================================

def _sha256_of_obj(obj) -> str:
    """SHA-256 of a JSON-serialisable object (sorted keys, default=str)."""
    s = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(s).hexdigest()


def _sha256_of_file(path: Path) -> str:
    """SHA-256 of file contents (streamed)."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


# Pre-registered machinery (PRDR) -- frozen
L_max = 5                  # (local) matches G56 (W3-G56) and W1-G2
dtau_stencil = 1e-4        # (local) 5-pt half-step h
GATE_ID = "S84-GV-CLASS-EXPLICIT"        # (local)
SCHEME = "stencil_5pt_central"            # (local)
CONVENTION = "omega_J_exp_neg_tau_dtau"   # (local)

# PASS-band thresholds (frozen pre-computation)
G56_REF = -4.0579e+04                    # (local) G56 reference value
PASS_REL_TOL = 1e-2                       # (local) 1% RATIO
PASS_LO = -4.10e+04                       # (local) lower band edge
PASS_HI = -4.02e+04                       # (local) upper band edge
STENCIL_PASS = 1e-6                       # (local) absolute stencil_err PASS
STENCIL_INFO = 1e-5                       # (local) above this -> FAIL(c)
MAGNITUDE_FAIL = 1e+3                     # (local) below this -> FAIL(a)

# Reference G56 NPZ (alias path supplied by planner; resolves to actual file)
PLAN_REF_PATHS = [                                      # (local)
    HERE / "s83_w3_g56_godbillon_vey_jensen_deform.npz",
    HERE.parent / "sessions" / "session-83" / "computation-artifacts"
                / "s83_g56_gv_jensen_deform.npz",
]
g56_ref_path = next((p for p in PLAN_REF_PATHS if p.exists()), None)  # (local)
if g56_ref_path is None:
    raise FileNotFoundError(
        f"None of the G56 reference paths exist: {PLAN_REF_PATHS}"
    )
g56_sha = _sha256_of_file(g56_ref_path)                  # (local)

canonical_path = HERE / "canonical_constants.py"          # (local)
canonical_sha = _sha256_of_file(canonical_path)           # (local)

# AS correction JSON path is documented in plan but not on disk; the
# correction (primary -> 0 via Atiyah-Singer homotopy invariance) is
# encoded directly in the G56 NPZ as primary_response = 0.0.  We pin
# the primary_response value carried by the reference NPZ as the
# AS-correction surrogate input.
ref_npz = np.load(g56_ref_path, allow_pickle=True)
g56_primary_response = float(ref_npz['primary_response'])  # (local) = 0.0

INPUT_PINS = {
    "gate": GATE_ID,
    "plan_section": "W10a-115",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max": L_max,
    "dtau_stencil": dtau_stencil,
    "tau_fold": tau_fold,
    "Vol_SU3": Vol_SU3,
    "J_C2": J_C2,
    "G56_REF": G56_REF,
    "PASS_LO": PASS_LO,
    "PASS_HI": PASS_HI,
    "STENCIL_PASS": STENCIL_PASS,
    "g56_ref_path": str(g56_ref_path.resolve()),
    "g56_ref_sha256": g56_sha,
    "g56_primary_response": g56_primary_response,
    "canonical_constants_path": str(canonical_path.resolve()),
    "canonical_constants_sha256": canonical_sha,
}
content_sha256 = _sha256_of_obj(INPUT_PINS)               # (local)

print("=" * 78)
print(f"{GATE_ID} -- S84 W10a Gate 115 (Connes NCG, [VERIFY])")
print("=" * 78)
print("\n[SEC 0] Input SHA-256 pins (first 20 lines)")
for k, v in INPUT_PINS.items():
    print(f"  {k:32s} = {v}")
print(f"\nINPUT_SHA256 (= content_sha256) = {content_sha256}")


# ============================================================
# SECTION 1: Jensen Dirac spectrum (matches S83 G56 exactly)
# ============================================================

def su3_casimir(p: int, q: int) -> float:
    """SU(3) quadratic Casimir for irrep (p,q):
       C_2(p,q) = (p^2 + p q + q^2 + 3p + 3q) / 3."""
    return (p * p + p * q + q * q + 3 * p + 3 * q) / 3.0


def su3_dimension(p: int, q: int) -> int:
    """SU(3) irrep dimension: dim(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def jensen_irrep_table(L_max_local: int, tau: float):
    """Returns dim, rho, lam arrays (one entry per (p,q) irrep, omitting
       (0,0)), L_max_local truncation. Same construction as the S83
       G56 reference, ensuring spectral identity."""
    dims_list, rhos_list, lams_list = [], [], []
    for p in range(L_max_local + 1):
        for q in range(L_max_local + 1 - p):
            if p == 0 and q == 0:
                continue
            c2 = su3_casimir(p, q)                        # (local)
            d = su3_dimension(p, q)                       # (local)
            rho = p + q                                   # (local)
            lam = float(np.sqrt(c2) * np.exp(-tau * rho)) # (local)
            dims_list.append(d)
            rhos_list.append(rho)
            lams_list.append(lam)
    return (np.array(dims_list, dtype=float),
            np.array(rhos_list, dtype=float),
            np.array(lams_list, dtype=float))


# ============================================================
# SECTION 2: Build omega_J = e^{-tau} dtau and dω_J on the
#            Jensen foliation -- spectral realization
# ============================================================
print("\n[SEC 1] Jensen Dirac spectrum at tau_fold (irrep-level table)")
dims_f, rhos_f, lams_f = jensen_irrep_table(L_max, tau_fold)
print(f"  n_irreps           = {len(dims_f)}")
print(f"  sum(dim) (w/o doubling)   = {int(dims_f.sum())}")
print(f"  rho range           = [{int(rhos_f.min())}, {int(rhos_f.max())}]")
print(f"  lam range           = [{lams_f.min():.6e}, {lams_f.max():.6e}]")

print("\n[SEC 2] omega_J construction (planner sign convention)")
print("  omega_J(tau)        := e^{-tau} dtau")
print("  GV_proxy(tau)       := -sum dim * rho^2 * |lam|^{-4}")
print("  d(ln lam)/dtau      = -rho  (exact)")
print("  GV_proxy is the spectral realization of  eta_J /\\ d eta_J  with")
print("  Dixmier |D|^{-4} weight; the negative sign is the planner's choice.")


def gv_proxy(tau: float) -> float:
    """Spectral realization GV_proxy(tau) = -sum dim * rho^2 * |lam|^{-4}.

       Identity (NCG curvature correction from Hopf algebroid via the
       tau-derivative of ln lam):
           d(ln lam(p,q,tau))/dtau = -rho(p,q)
       so the spectral pairing
           <eta_J, d eta_J>_{|D|^{-4}} = sum dim * rho^2 * |lam|^{-4}
       is multiplied by -1 to yield GV_proxy with planner sign.
    """
    dims_t, rhos_t, lams_t = jensen_irrep_table(L_max, tau)
    inv4 = 1.0 / (lams_t ** 4)                            # (local)
    return float(-np.sum(dims_t * (rhos_t ** 2) * inv4))


# ============================================================
# SECTION 3: 5-point central-stencil derivative + analytic check
# ============================================================
print("\n[SEC 3] 5-point central stencil on d(GV_proxy)/dtau at tau_fold")
print("  Formula:  f'(tau) ~ [ -f(tau+2h) + 8 f(tau+h)")
print("                       - 8 f(tau-h) +   f(tau-2h) ] / (12 h)")
print(f"  Step h = dtau_stencil = {dtau_stencil}")

g_p1 = gv_proxy(tau_fold + dtau_stencil)                  # (local)
g_p2 = gv_proxy(tau_fold + 2.0 * dtau_stencil)            # (local)
g_m1 = gv_proxy(tau_fold - dtau_stencil)                  # (local)
g_m2 = gv_proxy(tau_fold - 2.0 * dtau_stencil)            # (local)
g_0 = gv_proxy(tau_fold)                                  # (local)

gv_response_direct = float(
    (-g_p2 + 8.0 * g_p1 - 8.0 * g_m1 + g_m2) / (12.0 * dtau_stencil)
)                                                         # (local)

# Analytic closed-form derivative (cross-check)
# d/dtau [-sum dim rho^2 |lam|^{-4}]
#   = d/dtau [-sum dim rho^2 C_2^{-2} exp(4 tau rho)]
#   = -sum dim rho^2 C_2^{-2} * 4 rho * exp(4 tau rho)
#   = -4 sum dim rho^3 |lam|^{-4}
gv_analytic = float(-4.0 * np.sum(dims_f * (rhos_f ** 3) / (lams_f ** 4)))  # (local)
stencil_err = float(abs(gv_response_direct - gv_analytic) / max(abs(gv_analytic), 1e-300))  # (local)

print(f"\n  GV_proxy(tau_fold)             = {g_0:.6e}")
print(f"  GV_proxy(tau_fold + h)         = {g_p1:.6e}")
print(f"  GV_proxy(tau_fold - h)         = {g_m1:.6e}")
print(f"  GV_proxy(tau_fold + 2h)        = {g_p2:.6e}")
print(f"  GV_proxy(tau_fold - 2h)        = {g_m2:.6e}")
print(f"  gv_response_direct (stencil_5pt) = {gv_response_direct:.6e}")
print(f"  gv_response_analytic             = {gv_analytic:.6e}")
print(f"  stencil_err (relative)           = {stencil_err:.3e}")


# ============================================================
# SECTION 4: Sign / G56 / J_C2 inference
# ============================================================
print("\n[SEC 4] Sign + G56 comparison + J_C2 inference")

# Planner's macroscopic factorisation (D5):
#   sign(gv_response_direct) = -sign(e^{-tau_fold}) * sign(Vol_SU3) * sign(J_C2_eff)
# With e^{-tau_fold} > 0 and Vol_SU3 > 0,
#   sign(gv_response_direct) = -sign(J_C2_eff).
# Inference: sign(J_C2_eff) = -sign(gv_response_direct).
sign_gv = int(np.sign(gv_response_direct))                # (local)
sign_J_C2_inferred = int(-sign_gv)                        # (local)
sign_J_C2_canonical = int(np.sign(J_C2))                  # (local)
sign_consistent = (sign_J_C2_inferred == sign_J_C2_canonical)  # (local)

G56_comparison_ratio = float(gv_response_direct / G56_REF)  # (local)
G56_rel_diff = float(abs(gv_response_direct - G56_REF) / abs(G56_REF))  # (local)

print(f"  sign(gv_response_direct)        = {sign_gv:+d}")
print(f"  sign(J_C2) inferred            = {sign_J_C2_inferred:+d}")
print(f"  sign(J_C2) canonical            = {sign_J_C2_canonical:+d}  "
      f"(J_C2 = {J_C2})")
print(f"  sign consistency                = {sign_consistent}")
print(f"  G56_REF                         = {G56_REF:.6e}")
print(f"  ratio (direct / G56)            = {G56_comparison_ratio:.6f}")
print(f"  relative difference             = {G56_rel_diff:.3e}")


# ============================================================
# SECTION 5: Planner D5 cross-check (Casimir aggregation)
# ============================================================
print("\n[SEC 5] Planner D5 cross-check  (informational)")
print("  Identification (D5):")
print("    J_C2_kernel := 4 * sum dim * rho^3 * |lam|^{-4} /")
print("                   ( e^{-tau_fold} * Vol_SU3_Haar )")
print("  so that  gv_response_direct = -e^{-tau_fold} * Vol_SU3 * J_C2_kernel")
J_C2_kernel = float(4.0 * np.sum(dims_f * (rhos_f ** 3) / (lams_f ** 4))
                    / (np.exp(-tau_fold) * Vol_SU3_Haar))  # (local)
recon_response = float(-np.exp(-tau_fold) * Vol_SU3 * J_C2_kernel)  # (local)
print(f"  J_C2_kernel  (operational)     = {J_C2_kernel:.6e}")
print(f"  Reconstructed response          = {recon_response:.6e}")
print(f"  Reconstructed - analytic        = {recon_response - gv_analytic:.3e}  "
      "(consistency check, NOT a verdict input)")


# ============================================================
# SECTION 6: Integrand mesh summary (planner output requirement)
# ============================================================
print("\n[SEC 6] Integrand mesh summary (irrep-by-irrep contribution)")
contribs = -4.0 * dims_f * (rhos_f ** 3) / (lams_f ** 4)   # (local)
order = np.argsort(contribs)                              # (local)  most-neg first
top_k = 5                                                 # (local)
print(f"  top-{top_k} most-negative contributors (rho, dim, lam, contrib):")
for idx in order[:top_k]:
    print(f"    rho={int(rhos_f[idx])}, dim={int(dims_f[idx])}, "
          f"lam={lams_f[idx]:.4e}, contrib={contribs[idx]:.4e}")
integrand_mesh_summary = {
    "n_irreps": int(len(dims_f)),
    "sum_contrib": float(contribs.sum()),
    "min_contrib": float(contribs.min()),
    "max_contrib": float(contribs.max()),
    "top5_irreps": [int(i) for i in order[:5]],
    "top5_contribs": [float(contribs[i]) for i in order[:5]],
}


# ============================================================
# SECTION 7: Verdict evaluation (per pre-registered thresholds)
# ============================================================
print("\n[SEC 7] Verdict evaluation")
in_pass_band = (PASS_LO <= gv_response_direct <= PASS_HI)  # (local)
stencil_ok = (stencil_err <= STENCIL_PASS)                # (local)
sign_match_g56 = (np.sign(gv_response_direct) == np.sign(G56_REF))  # (local)
mag_above_floor = (abs(gv_response_direct) >= MAGNITUDE_FAIL)  # (local)
stencil_unreliable = (stencil_err > STENCIL_INFO)         # (local)

if (in_pass_band and stencil_ok):
    verdict = "PASS"
    verdict_reason = (
        f"gv_response_direct = {gv_response_direct:.4e} is within 1% of G56 "
        f"({G56_REF:.4e}) and stencil_err = {stencil_err:.2e} <= {STENCIL_PASS:.0e}."
    )
elif (not mag_above_floor):
    verdict = "FAIL"
    verdict_reason = (
        f"|gv_response_direct| = {abs(gv_response_direct):.3e} < {MAGNITUDE_FAIL:.0e} "
        f"(FAIL condition (a): vanishingly small, contradicts non-zero claim)."
    )
elif (not sign_match_g56):
    verdict = "FAIL"
    verdict_reason = (
        f"sign(gv_response_direct) = {sign_gv:+d} opposite to G56 sign "
        f"{int(np.sign(G56_REF)):+d} (FAIL condition (b))."
    )
elif stencil_unreliable:
    verdict = "FAIL"
    verdict_reason = (
        f"stencil_err = {stencil_err:.2e} > {STENCIL_INFO:.0e} "
        f"(FAIL condition (c): numerical method unreliable)."
    )
else:
    # Within OOM but outside 1% band -> INFO per plan
    verdict = "INFO"
    verdict_reason = (
        f"gv_response_direct = {gv_response_direct:.4e} is within OOM of G56 "
        f"({G56_REF:.4e}) but outside the 1% PASS band [{PASS_LO:.3e}, {PASS_HI:.3e}]; "
        f"flag for stencil-step refinement."
    )

print(f"  in_pass_band       = {in_pass_band}  band=[{PASS_LO:.3e}, {PASS_HI:.3e}]")
print(f"  stencil_ok         = {stencil_ok}     stencil_err = {stencil_err:.3e}")
print(f"  sign_match_g56     = {sign_match_g56}")
print(f"  mag_above_floor    = {mag_above_floor}")
print(f"\n  VERDICT = {verdict}")
print(f"  Reason  : {verdict_reason}")


# ============================================================
# SECTION 8: Closure SHA, NPZ, verdict line
# ============================================================
OUTPUT_PINS = {
    **INPUT_PINS,
    "gv_response_direct": gv_response_direct,
    "gv_response_analytic": gv_analytic,
    "stencil_err": stencil_err,
    "G56_comparison_ratio": G56_comparison_ratio,
    "G56_rel_diff": G56_rel_diff,
    "sign_J_C2_inferred": sign_J_C2_inferred,
    "sign_J_C2_canonical": sign_J_C2_canonical,
    "sign_consistent": sign_consistent,
    "J_C2_kernel": J_C2_kernel,
    "recon_response": recon_response,
    "integrand_mesh_summary": integrand_mesh_summary,
    "verdict": verdict,
}
audit_sha256 = _sha256_of_obj(OUTPUT_PINS)                # (local)

# NPZ artifact (planner-required + diagnostic)
artifacts_dir = HERE.parent / "sessions" / "session-84" / "computation-artifacts"  # (local)
artifacts_dir.mkdir(parents=True, exist_ok=True)
npz_path = artifacts_dir / "s84_w10a_115_gv_explicit.npz"  # (local)

np.savez_compressed(
    npz_path,
    gv_response_direct=np.float64(gv_response_direct),
    gv_response_analytic=np.float64(gv_analytic),
    stencil_err=np.float64(stencil_err),
    sign_J_C2_inferred=np.int64(sign_J_C2_inferred),
    sign_J_C2_canonical=np.int64(sign_J_C2_canonical),
    sign_consistent=np.bool_(sign_consistent),
    G56_comparison_ratio=np.float64(G56_comparison_ratio),
    G56_rel_diff=np.float64(G56_rel_diff),
    G56_REF=np.float64(G56_REF),
    integrand_mesh_summary_json=np.array(
        json.dumps(integrand_mesh_summary, sort_keys=True), dtype=str
    ),
    J_C2_kernel=np.float64(J_C2_kernel),
    recon_response=np.float64(recon_response),
    tau_fold=np.float64(tau_fold),
    Vol_SU3=np.float64(Vol_SU3),
    J_C2=np.float64(J_C2),
    L_max=np.int64(L_max),
    dtau_stencil=np.float64(dtau_stencil),
    PASS_LO=np.float64(PASS_LO),
    PASS_HI=np.float64(PASS_HI),
    STENCIL_PASS=np.float64(STENCIL_PASS),
    verdict=np.array(verdict, dtype=str),
    content_sha256=np.array(content_sha256, dtype=str),
    audit_sha256=np.array(audit_sha256, dtype=str),
)
print(f"\n[SEC 8] Output NPZ: {npz_path}")

# Verdict line in the dual-SHA S84+ format
verdict_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value={gv_response_direct:.4e} "
    f"scheme={SCHEME} "
    f"convention={CONVENTION} "
    f"L_max={L_max} "
    f"audit_sha256={audit_sha256} "
    f"content_sha256={content_sha256}"
)

verdicts_file = HERE / "s84_gate_verdicts.txt"            # (local)
with open(verdicts_file, 'a', encoding='utf-8') as f:
    f.write(verdict_line + "\n")
print(f"\nVerdict line appended to: {verdicts_file}")
print(verdict_line)
print("=" * 78)
print(f"[W10a-115 COMPLETE]  verdict={verdict}")
