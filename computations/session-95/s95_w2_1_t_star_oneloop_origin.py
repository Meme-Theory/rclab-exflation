#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S95-W2-1-T-STAR-ONELOOP-ORIGIN
================================================================================
Gate:   S95-W2-1-T-STAR-ONELOOP-ORIGIN   (trigger [CHAIN], classification GEOMETRIC)
Agent:  feynman-theorist (one-loop effective action Gamma_1loop = (1/2) Tr ln(D^2/Lambda^2))
Plan:   sessions/session-plan/session-95-plan-w2.md  ## §W2-1
WP:     sessions/archive/session-95/session-95-w2-workingpaper.md  ### §W2-1

HYPOTHESIS (kaku §IV.4(1), §V.1)
--------------------------------------------------------------------------------
The single empirical functional coupling t* = 0.08832 (the e^{-x} admixture weight
in the near-canonical regulator f*(x) = (1-t*)*sqrt(x) + t**exp(-x), with
(1-t*) = 0.9117, t* = 0.08832; gate SPECTRAL-FUNCTIONAL-FIT-72 PASS at 1.3e-14)
is the coefficient FORCED by the one-loop threshold correction
    Gamma_1loop = (1/2) Tr ln(D_K(tau_fold)^2 / Lambda^2)
projected onto the f_0 Mellin-moment channel, i.e. t* is computable from the
L_max=10 D_K spectrum, NOT empirically fitted to the CMB tilt n_s.

PASS de-empiricizes the framework's free-parameter ledger to {tau, Lambda, f0, f2, f4}
(drops the ONLY empirical functional coupling). FAIL confirms t* is genuinely empirical.
NEUTRAL by pre-registration -- both outcomes are physics results.

--------------------------------------------------------------------------------
SUBSTITUTION CHAIN ([CHAIN] trigger; magnitude + sign claim) -- math-scripts.md
                  §"Double-Check Logic Before Compute"
--------------------------------------------------------------------------------
Claim: "t*_predicted (the one-loop-forced e^{-x} admixture coefficient in the f_0
        channel) equals the empirical t* = 0.08832 to within 5%."

Step 1 -- Definitions:
  f*(x)        = (1 - t*)*sqrt(x) + t**exp(-x);  (1-t*)=0.9117, t*=0.08832
                 [canonical_constants.py:536-539; SPECTRAL-FUNCTIONAL-FIT-72 PASS 1.3e-14]
  t*_canonical = mellin_f_star_f0 = 0.08832  [canonical_constants.py:539, S78 W2-D].
                 In the Chamseddine-Connes convention the f_0 Mellin moment is
                 f_0[g] = g(0) (S78 s78_f_conv_anomaly.py line 158,160,187:
                 mellin_f_star_f0 := f_star(0.0)). Hence:
                     f_0[sqrt(x)] = sqrt(0) = 0  (EXACT; tree term vanishes at f_0)
                     f_0[e^{-x}]  = e^{0}   = 1  (EXACT; one-loop carrier at f_0)
                     f_0[f*]      = (1-t*)*0 + t**1 = t*  (EXACT; WHY the canonical = t*)
  x_k          = |lambda_k|^2 / Lambda^2,  Lambda = M_KK,  {lambda_k} = D_K(tau_fold) spectrum,
                 L_max=10 (78,080 modes; sectors p+q<=10). The cached abs_evals are ALREADY
                 in M_KK units (max|lambda|=4.67, min|lambda|=0.8197>0), so x_k = |lambda_k|^2
                 with Lambda=M_KK absorbed into the unit. min|lambda|=0.8197 => x_k>0 forall k
                 => ln(x_k) finite forall k (no zero mode at tau_fold).
                 [s84_spectrum_cache_L12_tau019.npz]
  Gamma_1loop  = (1/2) Tr ln(D_K^2/Lambda^2) = (1/2) Sum_k ln(x_k)
                 = -(1/2) zeta'_D(0)  [equivalent S54 form; both verified equal in this script]
                 [§1.3a; S62 einstein-baptista; S54 nazarewicz-connes]
  chi_2 (tree) = Sum_k sqrt(x_k) = Sum_k |lambda_k|   (the tree bosonic spectral action sum;
                 per-mode <sqrt(x)> IS the S77-lizzi "spectral action per mode with f(x)=sqrt(x)")

Step 2 -- Substitution (PRIMARY operationalization, f_0-moment channel):
  The f_0 channel weights the e^{-x} one-loop generator (f_0=1) against the sqrt(x)
  tree generator (f_0=0). Because f_0[sqrt]=0 EXACTLY, the f_0 GENERATOR channel fixes
  f_0[f*]=t* by construction but does NOT independently PREDICT t*. A one-loop PREDICTION
  of t* therefore requires matching the one-loop CONTENT Gamma_1loop, carried by the e^{-x}
  generator, against the tree spectral action chi_2 -- the f_0-channel admixture is the
  one-loop FRACTION of the tree-plus-one-loop spectral action:
      t*_predicted = M_f0[oneloop] / ( M_f0[tree] + M_f0[oneloop] )
                   = |Gamma_1loop| / ( chi_2_sum + |Gamma_1loop| )
  evaluated on the SAME 78,080-mode spectrum {x_k}. (Lambda cancels in the ratio;
  x_k dimensionless.)

Step 3 -- Simplification (algebra; one step per line):
  = ratio_f0 := |Gamma_1loop| / ( chi_2_sum + |Gamma_1loop| )        [f_0-channel ratio]
  = a continuous, dimensionless functional of {x_k}
  Relative-deviation operator:  R := |ratio_f0 - 0.08832| / 0.08832.

Step 4 -- Direction / sign read-off:
  sign_verdict keys on sign(ratio_f0 - 0.08832). The conjecture predicts ratio_f0 ~ 0.08832
  (a SMALL admixture, 0.088 << 0.912 tree). ratio_f0 is a moment ratio of POSITIVE generators
  => ratio_f0 > 0 always (a negative value would be structurally impossible). PASS requires
  ratio_f0 > 0 AND R < 0.05. A wrong SIGN (ratio_f0 < 0) OR wrong OOM (R > 0.30) => t* genuinely
  empirical. DIAG-1 (additive reading) ~0.001 is the FALSE operationalization whose 2-OOM miss
  proves the PRIMARY test is non-trivial (verdict not pre-baked).

Conclusion (NEUTRAL): R < 0.05 in the PRIMARY channel => t* one-loop-computable (ledger drops
  to {tau, Lambda, f0, f2, f4}). R > 0.30 => t* genuinely empirical (the single empirical coupling
  survives). INFO (0.05-0.30) => right OOM, residual scheme-gap. The plan ASSERTS neither outcome.

--------------------------------------------------------------------------------
THREE OPERATIONALIZATIONS (audit_discriminators.operationalization_enumeration)
--------------------------------------------------------------------------------
PRIMARY (verdict): f_0-Mellin-moment ratio
    t*_pred = |Gamma_1loop| / (chi_2_sum + |Gamma_1loop|)
DIAG-1 (diagnostic): additive-weight reading
    t = Sum e^{-x_k} / (Sum sqrt(x_k) + Sum e^{-x_k})       (plan pre-flight ~0.001)
DIAG-2 (diagnostic): leading-log matching (tau-derivative under Jensen scaling)
    t = |dGamma_1loop/dlnr| / (|dchi_2/dlnr| + |dGamma_1loop/dlnr|) = N/(chi_2_sum + N)
The PRIMARY determines the verdict; DIAG-1/DIAG-2 are emitted in the npz sidecar.
No SCHEMATIC helper is consumed; CLASS=FULL (trace-log computed DIRECTLY on the cached
full D_K spectrum), per substrate-first-canonical-sourcing.md §(iv).

--------------------------------------------------------------------------------
PRE-REGISTERED VERDICT RUBRIC (NEUTRAL)
--------------------------------------------------------------------------------
operator: ratio  ->  R = |t*_predicted - t*_canonical| / t*_canonical
strict_PASS_boundary: R < 0.05  (RATIO-class tolerance, W0-9; looser 5% per kaku §V.1
                                 O(few%) scheme-gap)
PASS : R < 0.05            -> t* is the one-loop coefficient; ledger -> {tau, Lambda, f0, f2, f4}
INFO : 0.05 <= R <= 0.30   -> right OOM, residual scheme-gap (forward gate: tighter Mellin-cone)
                              OR regulator-class spread > 20%
FAIL : R > 0.30 OR impossible sign -> t* genuinely empirical; corridor "t* is one-loop" CLOSES

3-tuple companion (schema-v2, [CHAIN] directional pre-reg):
  sign_verdict     PASS iff sign(ratio_f0) matches predicted (+; positive moment ratio)
  magnitude_verdict PASS/INFO/FAIL on R vs (0.05 / 0.30)
  regime_verdict   VALID iff trace-log well-defined (min|lambda|>0, all ln finite, no
                   regulator-class breakdown) across the evaluation
Composite collapse per gate-verdicts.md.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # (local) CPU thread cap; trace-log is a vector reduction, not a matrix op
os.environ.setdefault("MKL_NUM_THREADS", "8")     # (local)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: from canonical_constants import ...) ---
SHARED = Path(__file__).resolve().parents[1] / "_shared"      # (local) computations/_shared
sys.path.insert(0, str(SHARED))
from canonical_constants import M_KK, tau_fold, mellin_f_star_f0   # noqa: E402

# ---------------------------------------------------------------------------
# Paths + identity
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                    # (local) project root
GATE_ID = "S95-W2-1-T-STAR-ONELOOP-ORIGIN"                    # (local)
SCHEME = "SA"                                                 # (local) spectral-action one-loop
CONVENTION = "ONELOOP-TRACE-LOG-f0-MOMENT-CHANNEL"            # (local) plan-pinned f_0 Mellin-moment channel
L_MAX = "10"                                                  # (local) operational truncation (p+q<=10)
SCHEMA_VERSION = "S84+"                                       # (local)

SCRIPT_PATH = Path(__file__).resolve()                                            # (local)
CANONICAL_CONSTANTS = SHARED / "canonical_constants.py"                            # (local)
SPECTRUM_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
VERDICT_FILE = ROOT / "computations" / "session-95" / "s95_gate_verdicts.txt"     # (local)
NPZ_OUT = SCRIPT_PATH.with_suffix(".npz")                                         # (local)
PNG_OUT = SCRIPT_PATH.with_suffix(".png")                                         # (local)

# Plan-pinned static SHA of the spectrum cache (machinery_pin_map / input_files)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # (local)

# Pre-registered tolerances (RATIO-class, W0-9 / kaku §V.1)
PASS_BAND = 0.05    # (local) PASS iff R < 0.05
INFO_BAND = 0.30    # (local) INFO iff 0.05 <= R <= 0.30; FAIL iff R > 0.30
TOL_NUM = 1e-12     # (local) numerical convergence floor on the trace-log sum


# ---------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema; matches s93 reference implementation)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    """Log SHA-256 of every input file in the first stdout lines; return pinmap."""
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(ROOT))  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)"""
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
    audit = h_audit.hexdigest()  # (local)

    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_v, mag_v, regime_v):
    """Single canonical dual-SHA verdict line + dual-SHA companion row + schema-v2
    3-tuple companion row ([CHAIN] directional pre-reg). Append-only single open('a')."""
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [CHAIN] f_0-Mellin-moment one-loop t* origin; "
        f"PRIMARY t*_pred=|Gamma_1loop|/(chi2_sum+|Gamma_1loop|); CLASS=FULL (trace-log on cached "
        f"D_K spectrum, NO SCHEMATIC helper); regulator_pin=a_n^{{zeta}} (heat-kernel-log class)\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [CHAIN] §W2-1 Step-4 directional pre-reg: "
        f"SIGN=positive moment ratio (ratio_f0>0 required); MAG=R vs 0.05/0.30; "
        f"REGIME=min|lambda|>0 + all ln finite + no regulator breakdown)\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ---------------------------------------------------------------------------
# Spectrum loader (L_max=10 restriction of the L=12 cache)
# ---------------------------------------------------------------------------
def load_abs_evals_Lmax10(cache_path: Path):
    """Return concatenated |lambda_k| over all Peter-Weyl sectors with p+q<=10.
    The cache key 'sector_evals' is a dict {(p,q): {'dim','level','abs_evals'}}.
    abs_evals ALREADY carries the full sector multiplicity (e.g. (5,5): dim=216,
    n_evals=3456=216*16)."""
    d = np.load(cache_path, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local) dict
    chunks = []  # (local)
    n_sectors_used = 0  # (local)
    for k, v in se.items():
        rec = v.item() if isinstance(v, np.ndarray) else v  # (local)
        p, q = k
        if p + q <= 10:
            chunks.append(np.asarray(rec["abs_evals"], dtype=float).ravel())
            n_sectors_used += 1
    absv = np.concatenate(chunks)  # (local)
    return absv, n_sectors_used


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"=== {GATE_ID} ===")
    print("=" * 78)

    # ---- (1) input pins (SHA-256 of every input in the first stdout lines) ----
    input_files = {
        "script": SCRIPT_PATH,
        "canonical": CANONICAL_CONSTANTS,
        "spectrum_cache": SPECTRUM_CACHE,
    }
    print("\nINPUT SHA-256 PINS:")
    pins = log_input_pins(input_files)

    # ---- static-cache SHA verification (mechanical-closure honesty) ----
    cache_sha = pins["spectrum_cache"]  # (local)
    cache_sha_ok = (cache_sha == SPECTRUM_CACHE_SHA_PIN)  # (local)
    print(f"\n  spectrum_cache SHA pin match = {cache_sha_ok}")
    print(f"    plan-pinned : {SPECTRUM_CACHE_SHA_PIN}")
    print(f"    runtime     : {cache_sha}")
    if not cache_sha_ok:
        print("  !! spectrum cache SHA MISMATCH -> mechanical closure (PRE-REG-INC) per "
              "mechanical-closure-discipline.md")
        # honest closure path; but we expect a match (verified at plan-freeze)

    print(f"\n  canonical constants imported:")
    print(f"    M_KK            = {M_KK:.6e}")
    print(f"    tau_fold        = {tau_fold}")
    print(f"    mellin_f_star_f0 (t*_canonical) = {mellin_f_star_f0}")

    # ---- (2) load spectrum, restrict to L_max=10 ----
    print("\n" + "-" * 78)
    print("Load D_K(tau_fold) spectrum (L_max=10 restriction, p+q<=10)")
    print("-" * 78)
    absv, n_sectors = load_abs_evals_Lmax10(SPECTRUM_CACHE)
    N = absv.size  # (local) number of eigenvalues
    lam_min = float(absv.min())  # (local)
    lam_max = float(absv.max())  # (local)
    print(f"  sectors used (p+q<=10)        = {n_sectors}")
    print(f"  N (eigenvalues, L_max=10)     = {N}        (plan pin: 78080)")
    print(f"  min|lambda|                   = {lam_min:.10f}  (>0 => no zero mode => ln finite)")
    print(f"  max|lambda|                   = {lam_max:.10f}")

    # ---- dimensionless x_k = |lambda_k|^2 / Lambda^2 with Lambda=M_KK ----
    # cached abs_evals are ALREADY in M_KK units => x_k = |lambda_k|^2 (Lambda absorbed in unit).
    x = absv ** 2  # (local) x_k = |lambda_k|^2 (M_KK units; Lambda=M_KK cancels in the moment RATIO)
    x_min = float(x.min())  # (local)
    x_max = float(x.max())  # (local)
    assert x_min > 0.0, "x_min must be > 0 for ln(x_k) finite"
    log_x = np.log(x)  # (local) ln(x_k), finite forall k
    sqrt_x = np.sqrt(x)  # (local) = |lambda_k|
    exp_negx = np.exp(-x)  # (local) one-loop heat-kernel generator per mode
    print(f"  x_k = |lambda|^2 : min={x_min:.6f}  max={x_max:.6f}  mean={float(x.mean()):.6f}")

    # ---- (3) one-loop effective-action generator Gamma_1loop = (1/2) Sum ln x_k ----
    print("\n" + "-" * 78)
    print("One-loop effective action  Gamma_1loop = (1/2) Tr ln(D^2/Lambda^2) = (1/2) Sum ln x_k")
    print("-" * 78)
    Gamma_1loop = 0.5 * float(np.sum(log_x))  # (local)
    # Cross-check via the spectral zeta form:  Gamma_1loop = -(1/2) zeta'(0),  zeta'(0) = Sum -ln x_k
    zeta_prime_0 = float(np.sum(-log_x))  # (local) zeta'(0) = d/ds Sum x^{-s} |_0 = Sum(-ln x)
    Gamma_1loop_zeta = -0.5 * zeta_prime_0  # (local)
    zeta_0 = float(np.sum(x ** 0.0))  # (local) zeta(0) = N (mode count)
    print(f"  Gamma_1loop = (1/2)Sum ln x_k        = {Gamma_1loop:.10f}")
    print(f"  Gamma_1loop = -(1/2)zeta'(0) (S54)   = {Gamma_1loop_zeta:.10f}")
    print(f"  |difference| (cross-check, must ~0)  = {abs(Gamma_1loop - Gamma_1loop_zeta):.3e}")
    print(f"  zeta(0) = Sum x^0 = N (sanity)       = {zeta_0:.1f}")
    g1_crosscheck_ok = abs(Gamma_1loop - Gamma_1loop_zeta) < TOL_NUM  # (local)

    # ---- (4) tree spectral action in the sqrt channel (S77-lizzi chi_2) ----
    print("\n" + "-" * 78)
    print("Tree spectral action (sqrt channel):  chi_2_sum = Sum sqrt(x_k) = Sum |lambda_k|")
    print("-" * 78)
    chi2_sum = float(np.sum(sqrt_x))  # (local) tree bosonic spectral action sum
    chi2_per_mode = float(np.mean(sqrt_x))  # (local) S77 chi_2 = spectral action PER MODE
    print(f"  chi_2_sum (Sum sqrt x)               = {chi2_sum:.10f}")
    print(f"  chi_2 per mode (<sqrt x>, S77)       = {chi2_per_mode:.10f}")

    # ---- (5) f_0 Mellin moments (Chamseddine-Connes convention f_0[g]=g(0)) ----
    print("\n" + "-" * 78)
    print("f_0 Mellin moments (Chamseddine-Connes: f_0[g] = g(0); S78 s78_f_conv_anomaly.py)")
    print("-" * 78)
    f0_sqrt = float(np.sqrt(0.0))  # (local) f_0[sqrt(x)] = sqrt(0) = 0 EXACT
    f0_exp = float(np.exp(-0.0))   # (local) f_0[e^-x]   = e^0   = 1 EXACT
    f0_fstar = (1.0 - mellin_f_star_f0) * f0_sqrt + mellin_f_star_f0 * f0_exp  # (local) = t* EXACT
    print(f"  f_0[sqrt(x)] = sqrt(0)               = {f0_sqrt}  (tree vanishes at f_0)")
    print(f"  f_0[e^-x]    = e^0                   = {f0_exp}  (one-loop carrier at f_0)")
    print(f"  f_0[f*] = (1-t*)*0 + t**1            = {f0_fstar}  (== t*_canonical; WHY S78 pin = t*)")
    print(f"  t*_canonical (mellin_f_star_f0)      = {mellin_f_star_f0}")

    # ---- (6) THE THREE OPERATIONALIZATIONS ----
    print("\n" + "=" * 78)
    print("THREE OPERATIONALIZATIONS (PRIMARY determines verdict; DIAG-1/DIAG-2 sidecar)")
    print("=" * 78)
    tstar = float(mellin_f_star_f0)  # (local)

    # PRIMARY: f_0-Mellin-moment ratio = one-loop fraction of (tree + one-loop) spectral action.
    #   f_0[sqrt]=0 makes the f_0 GENERATOR channel degenerate (cannot independently predict t*);
    #   a one-loop PREDICTION requires the one-loop CONTENT Gamma_1loop carried by the e^{-x}
    #   generator, normalized against the tree spectral action chi_2_sum.
    M_f0_oneloop = abs(Gamma_1loop)  # (local) one-loop content
    M_f0_tree = chi2_sum             # (local) tree spectral action content
    t_primary = M_f0_oneloop / (M_f0_tree + M_f0_oneloop)  # (local) PRIMARY ratio_f0
    R_primary = abs(t_primary - tstar) / tstar  # (local)

    # DIAG-1: additive-weight reading (plan pre-flight ~0.001; the FALSE operationalization).
    sum_exp = float(np.sum(exp_negx))  # (local)
    t_diag1 = sum_exp / (chi2_sum + sum_exp)  # (local)
    R_diag1 = abs(t_diag1 - tstar) / tstar  # (local)

    # DIAG-2: leading-log matching (tau-derivative under Jensen scaling x_k ~ r^{-2}).
    #   d ln x_k / d ln r = -2 (same forall k) => dGamma_1loop/dlnr = (1/2)*N*(-2) = -N.
    #   d sqrt(x_k)/d ln r = -sqrt(x_k) => dchi_2/dlnr = -chi_2_sum.
    #   t_diag2 = |dGamma_1loop/dlnr| / (|dchi_2/dlnr| + |dGamma_1loop/dlnr|) = N/(chi_2_sum + N).
    dG1_dlnr = float(N)          # (local) |dGamma_1loop/dlnr|
    dchi_dlnr = chi2_sum         # (local) |dchi_2/dlnr|
    t_diag2 = dG1_dlnr / (dchi_dlnr + dG1_dlnr)  # (local)
    R_diag2 = abs(t_diag2 - tstar) / tstar  # (local)

    for nm, tval, Rval in [
        ("PRIMARY f_0-channel |G1|/(chi2_sum+|G1|)", t_primary, R_primary),
        ("DIAG-1  additive Sum e^-x/(Sum sqrt+Sum e^-x)", t_diag1, R_diag1),
        ("DIAG-2  leading-log N/(chi2_sum+N)", t_diag2, R_diag2),
    ]:
        band = "PASS" if Rval < PASS_BAND else ("INFO" if Rval <= INFO_BAND else "FAIL")  # (local)
        print(f"  {nm:48s} = {tval:.6f}  R={Rval:.4f}  [{band}]")
    print(f"  {'t*_canonical':48s} = {tstar:.6f}")

    # ---- (7) regulator-class spread cross-check (a_n^zeta vs a_n^Pauli-Villars) ----
    # INFO_meaning fires if regulator-class spread > 20%. The PRIMARY uses the zeta/heat-kernel-log
    # one-loop Gamma_1loop. A Pauli-Villars one-loop subtracts a massive-regulator log:
    #   Gamma_1loop^PV = (1/2) Sum [ln(x_k) - ln(x_k + m_reg^2/M_KK^2)] with m_reg = M_KK (Lambda_UV).
    print("\n" + "-" * 78)
    print("Regulator-class spread cross-check (zeta vs Pauli-Villars one-loop)")
    print("-" * 78)
    m_reg2 = 1.0  # (local) (m_reg/M_KK)^2 = 1 at Lambda_UV = M_KK (eigenvalues in M_KK units)
    Gamma_1loop_PV = 0.5 * float(np.sum(log_x - np.log(x + m_reg2)))  # (local) PV-subtracted one-loop
    t_primary_PV = abs(Gamma_1loop_PV) / (chi2_sum + abs(Gamma_1loop_PV))  # (local)
    R_primary_PV = abs(t_primary_PV - tstar) / tstar  # (local)
    reg_spread = abs(t_primary - t_primary_PV) / max(abs(t_primary), 1e-30)  # (local) relative regulator spread
    print(f"  Gamma_1loop^zeta                     = {Gamma_1loop:.6f}")
    print(f"  Gamma_1loop^PV (Lambda_UV=M_KK)      = {Gamma_1loop_PV:.6f}")
    print(f"  t_primary^zeta                       = {t_primary:.6f}  (R={R_primary:.4f})")
    print(f"  t_primary^PV                         = {t_primary_PV:.6f}  (R={R_primary_PV:.4f})")
    print(f"  regulator-class spread (rel)         = {reg_spread:.4f}  (INFO trigger if >0.20)")
    reg_spread_gt_20 = reg_spread > 0.20  # (local)

    # ---- (8) VERDICT (composite collapse rule; gate-verdicts.md) ----
    print("\n" + "=" * 78)
    print("VERDICT (PRIMARY f_0-channel; composite collapse rule)")
    print("=" * 78)
    R = R_primary  # (local) verdict keys on PRIMARY

    # sign_verdict: predicted direction is a POSITIVE moment ratio (ratio_f0 > 0).
    #   A negative ratio_f0 would be structurally impossible (moment ratio of positive generators).
    sign_v = "PASS" if t_primary > 0.0 else "FAIL"  # (local)

    # magnitude_verdict
    if R < PASS_BAND:
        mag_v = "PASS"  # (local)
    elif R <= INFO_BAND:
        mag_v = "INFO"  # (local)
    else:
        mag_v = "FAIL"  # (local)
    # regulator-spread INFO escalation: if PRIMARY would PASS/INFO but spread>20%, mark INFO (not below FAIL).
    if reg_spread_gt_20 and mag_v == "PASS":
        mag_v = "INFO"

    # regime_verdict: VALID iff trace-log well-defined (min|lambda|>0, all ln finite,
    #   G1 cross-check ok). No auto-shortening; single-slice deterministic eval.
    all_ln_finite = bool(np.all(np.isfinite(log_x)))  # (local)
    regime_v = "VALID" if (x_min > 0.0 and all_ln_finite and g1_crosscheck_ok and cache_sha_ok) else "BREAKDOWN"  # (local)

    # composite collapse rule (PRE-REGISTERED; gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
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

    print(f"  R (PRIMARY relative deviation)       = {R:.6f}   (PASS<{PASS_BAND}; INFO<={INFO_BAND}; else FAIL)")
    print(f"  ratio_f0 - t*                        = {t_primary - tstar:+.6f}  (overshoot direction)")
    print(f"  sign_verdict                         = {sign_v}   (ratio_f0={t_primary:.4f} > 0 required)")
    print(f"  magnitude_verdict                    = {mag_v}")
    print(f"  regime_verdict                       = {regime_v}")
    print(f"  COMPOSITE                            = {composite}")

    # ---- physics statement ----
    print("\n" + "-" * 78)
    if composite == "PASS":
        print("  t* IS the one-loop threshold coefficient -> ledger drops to {tau, Lambda, f0, f2, f4}.")
    elif composite == "INFO":
        print("  t* reproduced to the right OOM but not 5%: residual scheme-gap (forward gate: "
              "tighter Mellin-cone) OR regulator-class spread.")
    else:
        print("  t* is GENUINELY EMPIRICAL: under the parameter-free f_0-channel one-loop "
              "operationalization the one-loop content")
        print(f"  Gamma_1loop={Gamma_1loop:.1f} is ~{100*t_primary:.1f}% of the tree+one-loop spectral "
              f"action -- ~{t_primary/tstar:.1f}x too large to BE t*={tstar}.")
        print("  Corridor 't* is one-loop' CLOSES. The framework retains exactly one empirical "
              "functional coupling (CF-52 empirical-realization half).")

    # ---- (9) data file ----
    value_str = (  # (local) compact, audit-greppable
        f"composite={composite};t_primary={t_primary:.8f};R_primary={R_primary:.6f};"
        f"t_diag1={t_diag1:.8f};R_diag1={R_diag1:.6f};t_diag2={t_diag2:.8f};R_diag2={R_diag2:.6f};"
        f"t_star_canonical={tstar:.8f};Gamma_1loop={Gamma_1loop:.6f};chi2_sum={chi2_sum:.6f};"
        f"N={N};min_lambda={lam_min:.6f};f0_sqrt={f0_sqrt};f0_exp={f0_exp};f0_fstar={f0_fstar:.8f};"
        f"t_primary_PV={t_primary_PV:.8f};reg_spread={reg_spread:.6f};"
        f"sign_verdict={sign_v};magnitude_verdict={mag_v};regime_verdict={regime_v};"
        f"PASS_band={PASS_BAND};INFO_band={INFO_BAND};CLASS=FULL;regulator_pin=a_n_zeta;"
        f"operationalization=PRIMARY_f0_mellin_moment_ratio"
    )

    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        N=N, n_sectors=n_sectors, L_max=10,
        lam_min=lam_min, lam_max=lam_max, x_min=x_min, x_max=x_max,
        M_KK=M_KK, tau_fold=tau_fold, t_star_canonical=tstar,
        Gamma_1loop=Gamma_1loop, Gamma_1loop_zeta=Gamma_1loop_zeta, zeta_prime_0=zeta_prime_0, zeta_0=zeta_0,
        chi2_sum=chi2_sum, chi2_per_mode=chi2_per_mode,
        f0_sqrt=f0_sqrt, f0_exp=f0_exp, f0_fstar=f0_fstar,
        t_primary=t_primary, R_primary=R_primary,
        t_diag1=t_diag1, R_diag1=R_diag1,
        t_diag2=t_diag2, R_diag2=R_diag2,
        Gamma_1loop_PV=Gamma_1loop_PV, t_primary_PV=t_primary_PV, R_primary_PV=R_primary_PV, reg_spread=reg_spread,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
        PASS_band=PASS_BAND, INFO_band=INFO_BAND,
        operationalization="PRIMARY_f0_mellin_moment_ratio",
    )
    print(f"\n  npz  -> {NPZ_OUT.relative_to(ROOT)}")

    # ---- (10) plot: 3 operationalizations vs canonical t* band ----
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    labels = ["PRIMARY\n|G1|/(chi2+|G1|)", "DIAG-1\nadditive", "DIAG-2\nleading-log", "PRIMARY-PV\n(reg x-check)"]  # (local)
    vals = [t_primary, t_diag1, t_diag2, t_primary_PV]  # (local)
    Rs = [R_primary, R_diag1, R_diag2, R_primary_PV]  # (local)
    colors = []  # (local)
    for Rv in Rs:
        colors.append("tab:green" if Rv < PASS_BAND else ("tab:orange" if Rv <= INFO_BAND else "tab:red"))
    xpos = np.arange(len(vals))  # (local)
    ax.bar(xpos, vals, color=colors, alpha=0.85, edgecolor="k", zorder=3)
    for xi, vi, Ri in zip(xpos, vals, Rs):
        ax.annotate(f"{vi:.4f}\nR={Ri:.3f}", (xi, vi), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=8.5)
    # canonical t* band: [0.95 t*, 1.05 t*] (PASS region)
    ax.axhline(tstar, color="k", lw=1.6, ls="-", zorder=2, label=f"t*_canonical = {tstar}")
    ax.axhspan(tstar * (1 - PASS_BAND), tstar * (1 + PASS_BAND), color="green", alpha=0.18, zorder=1,
               label=f"PASS band (+/-{int(PASS_BAND*100)}%)")
    ax.axhspan(tstar * (1 - INFO_BAND), tstar * (1 + INFO_BAND), color="orange", alpha=0.10, zorder=0,
               label=f"INFO band (+/-{int(INFO_BAND*100)}%)")
    ax.set_xticks(xpos)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel(r"$t^{*}_{\rm predicted}$  (e$^{-x}$ admixture coefficient)")
    ax.set_title(f"{GATE_ID}\nf_0-Mellin-moment one-loop origin of t*  (composite: {composite})", fontsize=10.5)
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(axis="y", ls=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  png  -> {PNG_OUT.relative_to(ROOT)}")

    # ---- (11) dual-SHA + verdict line ----
    print("\n" + "-" * 78)
    print("Dual-SHA closure + verdict-line emission")
    print("-" * 78)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v)
    print(f"\n  verdict line appended -> {VERDICT_FILE.relative_to(ROOT)}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md §"During computation")
    print(f"\n4-TUPLE OUTPUT TAG: (value={composite}/{t_primary:.6f}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
