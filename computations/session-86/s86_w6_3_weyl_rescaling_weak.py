"""
S86 W6-3 — WEYL-RESCALING-IMMUNIZATION-WEAK-FORM (C-gamma-WEAK corollary)
========================================================================

Gate: S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM
Owner: lizzi-spectral-functional-theorist
Plan: sessions/session-plan/session-86-plan-w6.md  Section W6-3 (lines 451-736)
Stub: sessions/archive/session-86/session-86-w6-workingpaper.md  Section W6-3 (lines 168-185)

PURPOSE
-------
Test the parametric bound corollary VII.S.D C-gamma-WEAK at L_max=10:

   |Delta S_W / S_W|(Lambda_cut)  <=  b_DK * (Lambda_anom_internal / Lambda_cut)^2 * sigma^2

where:
   - Lambda_anom_internal is computed INTERNALLY from Tr_F(Y^dagger Y)
     plus AC-2010 Section V chiral-anomaly coefficients (NO external Lambda pin)
   - b_DK is the Dirac-operator-determined dimensionless coupling
     b_DK = (1 / 8 pi^2) * Tr_F[(Y^dagger Y)^2] / Tr_F[Y^dagger Y]
   - sigma is a small Weyl-rescaling parameter (PIN: 0.01)
   - Lambda_cut sweeps log-uniformly over [M_KK, 10*M_KK] in 10 steps
   - The actual spectral-action shift Delta S_W is computed at L_max=10
     from the D_K spectrum cache s84_spectrum_cache_L12_tau019.npz
     (filtered to sectors with p+q <= 10).

PASS condition: ratio r(Lambda_cut) = LHS/RHS  <=  1   for ALL 10 sweep values
                AND b_DK > 0
                AND Lambda_anom_internal in [M_KK/100, 10*M_KK]
INFO band:      r in (1, 2] for at most 2 of 10 sweep values
FAIL:           r > 1 for >= 3 sweep values  OR  b_DK <= 0
                OR  Lambda_anom outside physical range

SUBSTITUTION CHAIN  (parametric-bound direction; mandatory per math-scripts.md)
------------------------------------------------------------------------------
Step 1 (definitions):
  S_W^{Lambda_cut, sigma, AC-2010}(Lambda_cut)
            = sum_n  f(lambda_n^2 / Lambda_cut^2)
              with f(x) = exp(-x)   [smooth-cutoff regulator class, finite moments]
  D -> e^{-sigma} D     ::  Weyl rescaling action on Dirac operator
  lambda_n -> e^{-sigma} lambda_n
  Delta S_W = S_W(D -> e^{-sigma} D) - S_W(D)
  Tr_F(Y^dagger Y)    ~  3 * y_t^2     [top-Yukawa-dominant; SM family-flavor sum]
  Tr_F[(Y^dagger Y)^2]~  3 * y_t^4
  y_t = m_t_pole / v_ew = 0.7020
  Lambda_anom_internal^2 = (M_KK^2 / 16 pi^2) * Tr_F(Y^dagger Y)
                                                     [AC-2010 Section V Eq. (5.2)]
  b_DK                   = (1 / 8 pi^2) * Tr_F[(Y^dagger Y)^2] / Tr_F[Y^dagger Y]
                                                     [AC-2010 Section V Eq. (5.3)]

Step 2 (substitute, leading order in sigma):
  f(e^{-2*sigma} x) = f(x) - 2*sigma*x*f'(x)
                            + 2*sigma^2*[x*f'(x) + x^2 * f''(x)] + O(sigma^3)
  Geometric (tree) piece:  Delta S_W^{tree} ~ -2*sigma * sum_n x_n * f'(x_n) + O(sigma^2)
  Anomaly piece (AC-2010): Delta S_W^{anomaly} ~ b_DK*(Lambda_anom/Lambda_cut)^2*sigma^2*S_W^0

Step 3 (simplify; the corollary):
  |Delta S_W / S_W|(Lambda_cut)  <=?  b_DK * (Lambda_anom_internal / Lambda_cut)^2 * sigma^2
  Define r(Lambda_cut) = LHS / RHS.  PASS <=> r <= 1 for all 10 sweep values.

Step 4 (direction):
  RHS > 0 (b_DK > 0 since y_t^2 > 0; (Lambda_anom/Lambda_cut)^2 > 0; sigma^2 > 0).
  LHS = |fractional shift| > 0.
  Both quantities are positive scalars; ratio r is well-defined and orientation
  is r <= 1 = PASS direction (LHS bounded above by parametric RHS).
  Note: the corollary's premise is that the O(sigma^2) anomaly dominates the
  O(sigma) tree-level shift.  If the eigenvalue spectrum has weight at x ~ O(1),
  the tree term DOMINATES and r is much greater than 1.  This is what the gate
  measures: whether the actual D_K spectrum at L_max=10 satisfies the WEAK-form
  bound, or whether the corollary requires a STRONG form (a_4-only / Mellin-
  cone projector that cancels the tree contribution).

INPUTS  (input-pin map; SHA-256 closure)
----------------------------------------
1. canonical_constants.py  (M_KK, v_ew, m_t_pole)
2. s84_spectrum_cache_L12_tau019.npz   (D_K spectrum, filtered p+q <= 10)
3. AC-2010 Section V Eq. (5.2),(5.3) coefficient form
4. lizzi 9A Section E-3 parametric-bound derivation
5. sigma pin = 0.01 (cross-check {0.005, 0.02})
6. Lambda_cut sweep = geomspace(M_KK, 10*M_KK, 10)
7. regulator: smooth-cutoff f(x) = exp(-x)

ENVIRONMENT
-----------
Python:  phonon-exflation-sim/.venv312/Scripts/python.exe
GPU:     not required (cache is pre-diagonalized in Peter-Weyl blocks; the
         L_max=10 cache contains 78,080 eigenvalues across 65 SU(3) sectors;
         no eigvalsh re-diagonalization is performed by this gate).
         The plan envelope expected ~155984x155984 dense diagonalization,
         which the cache makes unnecessary.

DO NOT
------
- Use external Lambda pin (M_GUT, M_Pl, etc.) for Lambda_anom.
- Hardcode b_DK; this script registers it via mcp_knowledge_update_constant.
- Re-run with different sigma until PASS (Class-6 PROHIBITED).
- Conflate Lambda_anom_internal with Lambda_QCD or Lambda_GUT.
"""

import os, sys, json, hashlib
from pathlib import Path
import numpy as np

# ----- Imports & paths ------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))
from canonical_constants import M_KK, v_ew, m_t_pole

CACHE_PATH   = SCRIPT_DIR / "s84_spectrum_cache_L12_tau019.npz"
DATA_OUT     = SCRIPT_DIR / "_artifacts" / "s86_w6_3_weyl_rescaling_weak.npz"
PLOT_OUT     = SCRIPT_DIR / "_artifacts" / "s86_w6_3_weyl_rescaling_weak.png"
JSON_OUT     = SCRIPT_DIR / "_artifacts" / "s86_w6_3_weyl_rescaling_weak.json"
VERDICT_FILE = SCRIPT_DIR / "s86_gate_verdicts.txt"
DATA_OUT.parent.mkdir(parents=True, exist_ok=True)

GATE_ID = "S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM"

# ----- Helpers --------------------------------------------------------------

def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def sha256_str(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# ----- Banner / input pin map (first 20 lines of stdout) -------------------
print("=" * 78)
print(f"GATE: {GATE_ID}")
print(f"SCRIPT: {Path(__file__).name}")
print(f"L_max: 10  (from L=12 cache, sectors filtered p+q <= 10)")
print(f"scheme: W6-3-Weyl-AC-2010-internal")
print(f"convention: parametric-bound-Lambda_anom_internal")
print("-" * 78)
INPUT_PIN_MAP = {
    "canonical_constants.M_KK"     : float(M_KK),
    "canonical_constants.v_ew"     : float(v_ew),
    "canonical_constants.m_t_pole" : float(m_t_pole),
    "spectrum_cache_path"          : str(CACHE_PATH.name),
    "spectrum_cache_sha256"        : sha256_file(CACHE_PATH),
    "AC2010_eq_5_2"                : "Lambda_anom^2 = (M_KK^2 / 16 pi^2) * Tr_F(Y^dagger Y)",
    "AC2010_eq_5_3"                : "b_DK = (1 / 8 pi^2) * Tr_F[(Y^dagger Y)^2] / Tr_F[Y^dagger Y]",
    "sigma_perturbation"           : 0.01,
    "sigma_cross_check"            : [0.005, 0.02],
    "Lambda_cut_sweep_npts"        : 10,
    "Lambda_cut_sweep_range"       : "[M_KK, 10*M_KK]  (logarithmic)",
    "regulator_f"                  : "exp(-x)  smooth-cutoff",
    "regulator_pin_tag"            : "S_W^{Lambda_cut, sigma, AC-2010}",
}
for k, v in INPUT_PIN_MAP.items():
    print(f"  {k}: {v}")
INPUT_PIN_SHA = sha256_str(json.dumps(INPUT_PIN_MAP, sort_keys=True, default=str))
print(f"INPUT-PIN-MAP SHA256: {INPUT_PIN_SHA}")
print("=" * 78)

# ----- M.0 :: Compute b_DK from AC-2010 Section V Eq. (5.3) ----------------
print()
print("Section M.0  Compute b_DK from AC-2010 Section V Eq. (5.3)")
print("-" * 78)

y_t   = m_t_pole / v_ew                                    # (local) top Yukawa
TrYY  = 3.0 * y_t**2                                       # (local) Tr Y^dagger Y; 3-color top dominates
TrYY2 = 3.0 * y_t**4                                       # (local) Tr (Y^dagger Y)^2; 3-color top dominates
b_DK  = (1.0 / (8.0 * np.pi**2)) * TrYY2 / TrYY            # (local) AC-2010 Section V Eq. (5.3)

print(f"  y_t = m_t_pole/v_ew    = {y_t:.10f}")
print(f"  Tr_F(Y^dagger Y)       = {TrYY:.10e}")
print(f"  Tr_F[(Y^dagger Y)^2]   = {TrYY2:.10e}")
print(f"  b_DK                   = {b_DK:.10e}")
print(f"  b_DK > 0:              {b_DK > 0}")

# Register b_DK to canonical_constants.py if absent.  This script does the
# numeric computation here, and the orchestrator will mirror via
# mcp__knowledge__update_constant after verifying b_DK.
B_DK_VALUE = b_DK
B_DK_PROVENANCE = {
    "session"      : "S86",
    "source"       : "AC-2010 Section V Eq. (5.3) + W6-3 internal computation (s86_w6_3_weyl_rescaling_weak.py)",
    "comment"      : "Dirac-operator-determined dimensionless constant for Weyl-rescaling weak-form parametric bound",
    "formula"      : "b_DK = (1 / 8 pi^2) * Tr_F[(Y^dagger Y)^2] / Tr_F[Y^dagger Y]",
    "anchor_inputs": {"v_ew": v_ew, "m_t_pole": m_t_pole, "y_t": y_t},
    "value"        : B_DK_VALUE,
}
print(f"  b_DK registration provenance prepared (orchestrator will mirror to canonical_constants.py via MCP).")

# ----- M.1 :: Compute Lambda_anom_internal from AC-2010 Section V Eq. (5.2) -
print()
print("Section M.1  Compute Lambda_anom_internal from AC-2010 Section V Eq. (5.2)")
print("-" * 78)
Lambda_anom_sq      = (M_KK**2 / (16.0 * np.pi**2)) * TrYY                  # (local)
Lambda_anom_internal = float(np.sqrt(Lambda_anom_sq))                       # (local)
print(f"  Lambda_anom_internal       = {Lambda_anom_internal:.6e}  GeV")
print(f"  Lambda_anom_internal/M_KK  = {Lambda_anom_internal/M_KK:.6e}")
PHYS_LO = M_KK / 100.0                                                      # (local)
PHYS_HI = M_KK * 10.0                                                       # (local)
in_phys_range = (PHYS_LO <= Lambda_anom_internal <= PHYS_HI)                # (local)
print(f"  In physical range [M_KK/100, 10*M_KK]:  {in_phys_range}")

# ----- M.2 :: Lambda_cut sweep, logarithmic [M_KK, 10*M_KK] in 10 steps ----
print()
print("Section M.2  Lambda_cut sweep")
print("-" * 78)
Lambda_cut_sweep = np.geomspace(M_KK, 10.0 * M_KK, 10)                      # (local)
for i, L in enumerate(Lambda_cut_sweep):
    print(f"  Lambda_cut[{i}] = {L:.6e}  GeV   (log10/M_KK = {np.log10(L/M_KK):+.3f})")

# ----- Load spectrum cache (L_max=10 filter) -------------------------------
print()
print("Load D_K spectrum cache, filter to L_max=10 (p+q <= 10)")
print("-" * 78)
d = np.load(CACHE_PATH, allow_pickle=True)
sev = d["sector_evals"].item()
abs_evals_chunks = []                                                       # (local)
n_sectors = 0                                                               # (local)
for (p, q), wrapper in sev.items():
    if p + q > 10:
        continue
    inner = wrapper.item() if isinstance(wrapper, np.ndarray) else wrapper
    abs_evals_chunks.append(np.asarray(inner["abs_evals"]))
    n_sectors += 1
lam_dimless = np.concatenate(abs_evals_chunks)                              # (local) eigenvalues in M_KK units
n_eigs = lam_dimless.size                                                   # (local)
print(f"  L_max=10 sectors:                  {n_sectors}")
print(f"  L_max=10 total eigenvalues:        {n_eigs}")
print(f"  lambda (M_KK units): min/max/mean = {lam_dimless.min():.6f} / {lam_dimless.max():.6f} / {lam_dimless.mean():.6f}")
lam_phys = lam_dimless * M_KK                                               # (local) physical eigenvalues, GeV

# ----- M.3 :: Per-Lambda_cut spectral-action evaluation under Weyl rescaling
print()
print("Section M.3  Per-Lambda_cut S_W evaluation; Weyl rescaling D -> exp(-sigma)*D")
print("-" * 78)

def S_spectral_action(lam_phys_arr, Lcut):
    """S_W = sum_n f(lambda_n^2 / Lcut^2) with f(x) = exp(-x)."""
    x = (lam_phys_arr / Lcut)**2
    return float(np.sum(np.exp(-x)))

SIGMA_PIN = 0.01                                                            # (local) plan PIN
SIGMA_CC  = [0.005, 0.02]                                                   # (local) cross-check pins

# Primary sweep at sigma_pin = 0.01
LHS_arr   = np.empty_like(Lambda_cut_sweep)                                 # (local)
RHS_arr   = np.empty_like(Lambda_cut_sweep)                                 # (local)
ratio_arr = np.empty_like(Lambda_cut_sweep)                                 # (local)
S0_arr    = np.empty_like(Lambda_cut_sweep)                                 # (local)
Ssig_arr  = np.empty_like(Lambda_cut_sweep)                                 # (local)
for i, Lcut in enumerate(Lambda_cut_sweep):
    S0   = S_spectral_action(lam_phys,                       Lcut)
    Ssig = S_spectral_action(lam_phys * np.exp(-SIGMA_PIN),  Lcut)
    LHS  = abs((Ssig - S0) / S0)
    RHS  = b_DK * (Lambda_anom_internal / Lcut)**2 * SIGMA_PIN**2
    r    = LHS / RHS
    S0_arr[i], Ssig_arr[i], LHS_arr[i], RHS_arr[i], ratio_arr[i] = S0, Ssig, LHS, RHS, r
    print(f"  Lcut={Lcut:.3e}  S_W={S0:.6e}  |dS/S|={LHS:.6e}  RHS={RHS:.6e}  r={r:.6e}")

max_r = float(ratio_arr.max())                                              # (local)
n_above_1     = int(np.sum(ratio_arr > 1.0))                                # (local)
n_in_info     = int(np.sum((ratio_arr > 1.0) & (ratio_arr <= 2.0)))         # (local)
n_above_2     = int(np.sum(ratio_arr > 2.0))                                # (local)
print(f"  max r over sweep:               {max_r:.6e}")
print(f"  count r > 1.0:                  {n_above_1}")
print(f"  count r in (1.0, 2.0]:          {n_in_info}")
print(f"  count r > 2.0:                  {n_above_2}")

# ----- Cross-check: sigma sensitivity at Lcut = M_KK ------------------------
print()
print("Cross-check  sigma scaling at Lcut=M_KK")
print("-" * 78)
sigma_grid    = np.array([0.005, 0.01, 0.02])                               # (local)
LHS_sigma     = np.empty_like(sigma_grid)                                   # (local)
LHS_over_sig  = np.empty_like(sigma_grid)                                   # (local)
LHS_over_sig2 = np.empty_like(sigma_grid)                                   # (local)
S0_ref = S_spectral_action(lam_phys, M_KK)                                  # (local)
for i, sg in enumerate(sigma_grid):
    Ssg = S_spectral_action(lam_phys * np.exp(-sg), M_KK)
    LHS_sigma[i] = abs((Ssg - S0_ref) / S0_ref)
    LHS_over_sig[i]  = LHS_sigma[i] / sg
    LHS_over_sig2[i] = LHS_sigma[i] / sg**2
    print(f"  sigma={sg:.3f}  |dS/S|={LHS_sigma[i]:.6e}  LHS/sigma={LHS_over_sig[i]:.6e}  LHS/sigma^2={LHS_over_sig2[i]:.6e}")

# Diagnostic: LHS/sigma roughly constant means LINEAR (tree-level dominates);
# LHS/sigma^2 roughly constant means QUADRATIC (anomaly dominates).
linear_var = float(np.std(LHS_over_sig)  / np.mean(LHS_over_sig))           # (local)
quad_var   = float(np.std(LHS_over_sig2) / np.mean(LHS_over_sig2))          # (local)
sigma_scaling_dominant = "LINEAR (tree)" if linear_var < quad_var else "QUADRATIC (anomaly)"
print(f"  rel-var LHS/sigma   = {linear_var:.4e}")
print(f"  rel-var LHS/sigma^2 = {quad_var:.4e}")
print(f"  Dominant sigma scaling: {sigma_scaling_dominant}")

# ----- Cross-check: Lambda_anom independence of any external Lambda pin -----
print()
print("Cross-check  Lambda_anom_internal expression has NO external Lambda pin")
print("-" * 78)
print("  Lambda_anom_internal^2 = (M_KK^2 / 16 pi^2) * Tr_F(Y^dagger Y)")
print("  Inputs: M_KK (canonical), v_ew (canonical), m_t_pole (canonical)")
print("  No M_GUT, no M_Pl, no M_KK_2 from other channels, no Lambda_cut feedback.")

# ----- PASS / INFO / FAIL classification ------------------------------------
print()
print("Pre-registered classification  (per plan Section T)")
print("-" * 78)
b_DK_positive       = bool(b_DK > 0)                                        # (local)
Lambda_anom_OK      = bool(in_phys_range)                                   # (local)
all_r_le_1          = bool(np.all(ratio_arr <= 1.0))                        # (local)
fail_count_ge_3     = bool(n_above_1 >= 3)                                  # (local)
info_band_holds     = bool((n_above_1 <= 2) and (n_above_2 == 0))           # (local)

if (all_r_le_1 and b_DK_positive and Lambda_anom_OK):
    verdict = "PASS"
elif info_band_holds and b_DK_positive and Lambda_anom_OK:
    verdict = "INFO"
elif (fail_count_ge_3 or (not b_DK_positive) or (not Lambda_anom_OK)):
    verdict = "FAIL"
else:
    verdict = "INFO"  # default to INFO band when not strictly PASS or FAIL

print(f"  b_DK > 0                  : {b_DK_positive}")
print(f"  Lambda_anom in [M_KK/100, 10*M_KK]: {Lambda_anom_OK}")
print(f"  All 10 r values <= 1      : {all_r_le_1}")
print(f"  Count r > 1.0  (3 = FAIL) : {n_above_1}")
print(f"  Count r > 2.0  (>0 ⇒ NOT INFO): {n_above_2}")
print(f"  VERDICT: {verdict}")

# ----- Save .npz / .json artifacts ------------------------------------------
np.savez_compressed(
    DATA_OUT,
    Lambda_cut_sweep=Lambda_cut_sweep,
    LHS=LHS_arr,
    RHS=RHS_arr,
    ratio_r=ratio_arr,
    S_W_unrescaled=S0_arr,
    S_W_rescaled=Ssig_arr,
    sigma_pin=np.array([SIGMA_PIN]),
    sigma_cross_check=np.array(SIGMA_CC),
    sigma_grid=sigma_grid,
    LHS_sigma=LHS_sigma,
    LHS_over_sigma=LHS_over_sig,
    LHS_over_sigma2=LHS_over_sig2,
    b_DK=np.array([b_DK]),
    Lambda_anom_internal=np.array([Lambda_anom_internal]),
    M_KK=np.array([float(M_KK)]),
    v_ew=np.array([float(v_ew)]),
    m_t_pole=np.array([float(m_t_pole)]),
    n_eigenvalues_Lmax10=np.array([n_eigs]),
    n_sectors_Lmax10=np.array([n_sectors]),
    max_r=np.array([max_r]),
)
print()
print(f"  Saved: {DATA_OUT.name}")

# ----- Plot -----------------------------------------------------------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
ax.loglog(Lambda_cut_sweep / M_KK, LHS_arr, "o-", label="LHS = |Delta S_W / S_W| (actual)")
ax.loglog(Lambda_cut_sweep / M_KK, RHS_arr, "s--", label="RHS = b_DK*(L_anom/L_cut)^2*sigma^2 (parametric bound)")
ax.set_xlabel(r"$\Lambda_{\rm cut} / M_{\rm KK}$")
ax.set_ylabel(r"$|\Delta S_W / S_W|$  /  parametric bound")
ax.set_title(f"S86 W6-3  Weyl-Rescaling Weak-Form (sigma={SIGMA_PIN}, L_max=10)\n"
             f"max r = {max_r:.3e}  ⇒  VERDICT = {verdict}")
ax.legend(loc="best", fontsize=9)
ax.grid(True, which="both", alpha=0.3)
ax2 = ax.twinx()
ax2.semilogx(Lambda_cut_sweep / M_KK, ratio_arr, "rx-", alpha=0.7, label="ratio r = LHS/RHS")
ax2.axhline(1.0, color="k", linestyle=":", alpha=0.5, label="PASS threshold (r=1)")
ax2.axhline(2.0, color="orange", linestyle=":", alpha=0.5, label="INFO ceiling (r=2)")
ax2.set_yscale("log")
ax2.set_ylabel("ratio r (log scale)", color="r")
ax2.tick_params(axis='y', labelcolor='r')
ax2.legend(loc="lower left", fontsize=8)
plt.tight_layout()
plt.savefig(PLOT_OUT, dpi=110)
plt.close(fig)
print(f"  Saved: {PLOT_OUT.name}")

# ----- JSON summary ---------------------------------------------------------
summary = {
    "gate_id": GATE_ID,
    "verdict": verdict,
    "value_max_r": max_r,
    "scheme": "W6-3-Weyl-AC-2010-internal",
    "convention": "parametric-bound-Lambda_anom_internal",
    "L_max": 10,
    "b_DK": b_DK,
    "b_DK_provenance": B_DK_PROVENANCE,
    "Lambda_anom_internal_GeV": Lambda_anom_internal,
    "Lambda_anom_over_M_KK": Lambda_anom_internal / float(M_KK),
    "in_physical_range": in_phys_range,
    "sigma_pin": SIGMA_PIN,
    "sigma_cross_check": SIGMA_CC,
    "Lambda_cut_sweep": [float(x) for x in Lambda_cut_sweep],
    "LHS": [float(x) for x in LHS_arr],
    "RHS": [float(x) for x in RHS_arr],
    "ratio_r": [float(x) for x in ratio_arr],
    "n_above_1": n_above_1,
    "n_above_2": n_above_2,
    "n_in_info_band": n_in_info,
    "sigma_scaling_dominant": sigma_scaling_dominant,
    "LHS_over_sigma_relvar": linear_var,
    "LHS_over_sigma2_relvar": quad_var,
    "n_eigenvalues_Lmax10": int(n_eigs),
    "n_sectors_Lmax10": int(n_sectors),
    "input_pin_sha256": INPUT_PIN_SHA,
}
with open(JSON_OUT, "w") as f:
    json.dump(summary, f, indent=2, default=str)
print(f"  Saved: {JSON_OUT.name}")

# ----- Dual-SHA closure -----------------------------------------------------
content_basis = json.dumps({
    "max_r": max_r, "verdict": verdict, "b_DK": b_DK,
    "Lambda_anom_internal": Lambda_anom_internal,
    "ratio_r": [float(x) for x in ratio_arr],
    "LHS": [float(x) for x in LHS_arr],
    "RHS": [float(x) for x in RHS_arr],
}, sort_keys=True)
content_sha = sha256_str(content_basis)
audit_sha   = sha256_str(json.dumps({
    **INPUT_PIN_MAP,
    "b_DK_value_pinned_at_runtime": b_DK,
    "Lambda_anom_internal_value": Lambda_anom_internal,
    "script_path": str(SCRIPT_DIR / "s86_w6_3_weyl_rescaling_weak.py"),
    "gate_id": GATE_ID,
}, sort_keys=True, default=str))

# ----- Append verdict line + dual-SHA companion row -------------------------
verdict_line  = (f"{GATE_ID}: {verdict} -- value={max_r:.6e} "
                 f"scheme=W6-3-Weyl-AC-2010-internal "
                 f"convention=parametric-bound-Lambda_anom_internal "
                 f"L_max=10 sha256={audit_sha}")
companion_row = (f"# content_sha256={content_sha}  audit_sha256={audit_sha}  "
                 f"script=s86_w6_3_weyl_rescaling_weak.py  "
                 f"input_pin_map_sha256={INPUT_PIN_SHA}")

with open(VERDICT_FILE, "a", encoding="utf-8") as f:
    f.write("\n" + verdict_line + "\n")
    f.write(companion_row + "\n")
print()
print("Appended to verdict file:")
print(f"  {verdict_line}")
print(f"  {companion_row}")

# ----- 4-tuple banner -------------------------------------------------------
print()
print("4-tuple OUTPUT:")
print(f"  (value={max_r:.6e}, scheme=W6-3-Weyl-AC-2010-internal, "
      f"convention=parametric-bound-Lambda_anom_internal, L_max=10)")
print(f"VERDICT: {verdict}")

sys.exit(0)
