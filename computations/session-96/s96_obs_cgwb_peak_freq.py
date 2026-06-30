r"""
S96-OBS-CGWB-PEAK-FREQ  —  Wave 6, gate 3  [SIGN]

D4 resolution: derive the CGWB peak OBSERVED frequency via the substrate redshift
chain, and decide whether acoustic dispersion moves the (A)-class acoustic peak from
the naive GHz GUT-transition expectation into the LISA mHz band, or whether the LISA
peak-frequency flagship evaporates.

SUBSTRATE-FIRST FRAMING (PHONONIC, tensor sector)
-------------------------------------------------
The CGWB is NOT a primordial GW background in expanding space. It is squeezed-graviton
production at the van Hove fold — the GGE-acoustic excitation transduced into the tensor
sector (which crosses freely per [T3]). The EMISSION frequency is the fold's characteristic
ACOUSTIC frequency, set by the van Hove DOS scale and c_fabric in M_KK units — NOT a thermal
GUT-transition frequency. The redshift to observation is the readout of the substrate's
spectral-complexity growth: a(tau) GROWS from the fold (a_fold/a_now < 1), so f_obs < f_emit.

The chain (substrate -> emergent):
  D_K eigenvalues  ->  van Hove fold DOS / group-velocity-zero  ->  fold characteristic
  acoustic angular frequency (M_KK units)  ->  physical f_emit [Hz] via the M_KK^-1->s
  normalization kappa  ->  redshift by a(tau_fold)/a(tau_now)  ->  f_obs [Hz]  ->  detector band.

THE OPEN KNOB
-------------
The single open dimensionful piece is M_KK^-1 -> seconds (kappa), the SAME gap blocking
the derived a(t) (flagged in W6-5 / gate-5). At the substrate-natural value
kappa_nat = hbar/M_KK = 8.860440e-42 s (= canonical M_KK_inv_seconds), M_KK in s^-1 is
~1.13e41 s^-1, so the fold acoustic emission is f_emit ~ M_KK/(2pi) ~ 1.8e40 Hz. Where kappa
cannot be otherwise pinned, the verdict is reported as a function of it over gate-5's swept
band kappa in [1e-20, 1e-10] s/M_KK^-1.

REDSHIFT-CHAIN SUBSTITUTION CHAIN (sign + the ~12-decade question)
------------------------------------------------------------------
  Claim: the substrate scale factor REDSHIFTS the CGWB peak (f_obs < f_emit); the question
         is whether redshift + acoustic dispersion is large enough (~12 decades) to move a
         GHz emission into the LISA mHz band.
  Def 1: f_obs = f_emit * a(tau_fold)/a(tau_now)                      [cosmological redshift chain]
  Def 2: a(tau_fold)/a(0) = 2.1173 (gate-5, DIRECTLY RESOLVED)  => a_now > a_fold
  Step:  a_fold/a_now = 1/2.1173 = 0.47229 < 1                        [Sage-QQ exact, this gate]
  Canon: f_obs = f_emit * (a_fold/a_now); a_fold/a_now < 1 => f_obs < f_emit  (REDSHIFT;
         sign PASS iff computed ratio < 1).
  Def 3: f_emit = fold characteristic ACOUSTIC freq (van Hove DOS scale; M_KK-unit ang. freq
         omega_tilde * M_KK), NOT a thermal GUT-transition frequency.
  Def 4: naive thermal GUT route (S58 Method-3): f_0 ~ T_* T_0 / M_Pl with T_*~M_KK=7.43e16 GeV
         => f_0 ~ 1.7 GHz  (the naive expectation the plan calls FAIL).
  Decades: log10(1e9 Hz / 1e-3 Hz) = 12.0 decades of redshift needed to reach LISA mHz.
  Direction: ACOUSTIC dispersion (c_fabric, not c) is the proposed extra-suppression mechanism;
             whether it delivers ~12 decades is the OPEN question this gate resolves.
  Conclusion: f_obs in [0.1,100] mHz -> PASS (LISA flagship stands); PTA/DECIGO -> INFO; GHz+ -> FAIL.

[SIGN] 3-tuple (gate-verdicts.md schema-v2)
  sign_verdict : direction f_obs < f_emit (redshift). PASS iff computed a_fold/a_now < 1.
  magnitude    : band placement of f_obs at kappa_nat vs the LISA mHz band. PASS iff in [1e-4,1e-1] Hz;
                 INFO iff PTA(nHz)/DECIGO(0.1-10 Hz) OR normalization-conditional;
                 FAIL iff GHz+ (>= 1e8 Hz).
  regime       : the kappa knob. VALID iff the band placement is stable across the swept kappa band
                 (i.e. the verdict does not flip inside [1e-20,1e-10]); MARGINAL/BREAKDOWN iff the
                 verdict is entirely normalization-set and flips within the band.

Author: little-red-dots-jwst-analyst (detector-band confrontation; transit-dynamics supplies the
        dispersion; mack-cosmic-bridge writes the falsifier-inventory row per canonical write-order).
Env: phonon-exflation-sim/.venv312/Scripts/python.exe ; CPU.
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

sys.path.insert(0, "computations/_shared")
from canonical_constants import (
    M_KK,                 # 7.428660036284456e16 GeV
    M_KK_inv_seconds,     # 8.860439881925477e-42 s  (= hbar/M_KK; the substrate-natural kappa)
    c_fabric,             # 209.97368021 (M_KK units; substrate sound speed)
    Mach_max,             # 13.75 (van Hove fold velocity ratio)
    M_Pl_reduced,         # 2.435e18 GeV
    hbar_GeV_s,           # 6.582119569e-25 GeV*s
    omega_L1,             # 0.138 M_KK  (Leggett-1; a fold acoustic mode)
    omega_PV,             # 0.791658919261384 M_KK  (pair-vibration)
    omega_tau,            # 8.27 M_KK
    v_g_B2_fold,          # 0.022699323 M_KK  (B2 group velocity -> 0 at fold)
    f_LISA_pivot,         # 0.003 Hz  (LISA peak-sensitivity pivot)
    tau_fold,             # 0.19
)

# -----------------------------------------------------------------------------
# Paths / identity
# -----------------------------------------------------------------------------
SCRIPT_PATH   = Path("computations/session-96/s96_obs_cgwb_peak_freq.py")
CANONICAL     = Path("computations/_shared/canonical_constants.py")
LRD_CLOCK_NPZ = Path("computations/session-96/s96_obs_lrd_assembly_clock.npz")
S54_NPZ       = Path("computations/session-54/s54_scale_factor.npz")
OUT_NPZ       = Path("computations/session-96/s96_obs_cgwb_peak_freq.npz")
OUT_PNG       = Path("computations/session-96/s96_obs_cgwb_peak_freq.png")
VERDICT_TXT   = Path("computations/session-96/s96_gate_verdicts.txt")

GATE_ID    = "S96-OBS-CGWB-PEAK-FREQ"
SCHEME     = "acoustic-dispersion-redshift-(A)-class"
CONVENTION = "substrate-fold-characteristic-frequency-NOT-relativistic-GW-redshift"
L_MAX      = "N/A"

# -----------------------------------------------------------------------------
# Detector bands (Hz)  — same partition as S58 s58_gw_frequency_check.py
# -----------------------------------------------------------------------------
LISA_LO, LISA_HI = 1e-4, 1e-1     # (local) LISA-PLS band [0.1, 100] mHz
PTA_LO,  PTA_HI  = 1e-9, 1e-7     # (local) PTA nHz band
DECIGO_LO, DECIGO_HI = 1e-1, 10.0 # (local) DECIGO / BBO band [0.1, 10] Hz
GHZ_FLOOR = 1e8                   # (local) "GHz+" = high-freq gap and above (FAIL)


def detector_band(f_Hz: float) -> str:
    """Classify f into detector sensitivity band (S58 partition)."""
    if f_Hz < 1e-9:  return "sub-PTA"
    if f_Hz < 1e-7:  return "PTA(nHz)"
    if f_Hz < 1e-4:  return "gap(PTA-LISA)"
    if f_Hz < 1e-1:  return "LISA(mHz)"
    if f_Hz < 10.0:  return "DECIGO(0.1-10Hz)"
    if f_Hz < 1e4:   return "LIGO/ET"
    if f_Hz < 1e8:   return "high-freq-gap"
    return "GHz+"


def band_class(f_Hz: float) -> str:
    """Verdict-relevant 3-way placement: LISA / PTA-DECIGO / GHZ-or-OTHER."""
    if LISA_LO <= f_Hz < LISA_HI:
        return "LISA"
    if (PTA_LO <= f_Hz < PTA_HI) or (DECIGO_LO <= f_Hz < DECIGO_HI):
        return "PTA-DECIGO"
    if f_Hz >= GHZ_FLOOR:
        return "GHZ+"
    return "OTHER"   # gap regions (PTA-LISA gap, LISA-DECIGO gap, LIGO/ET)


# -----------------------------------------------------------------------------
# SHA / dual-SHA helpers (replicate s96_w1_taudot_profile.py exactly)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256). audit = sha(script||canonical||pinmap_json); content = sha(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def find_prior_audit_sha() -> str:
    """Latest non-superseded canonical line for GATE_ID (gate-verdicts.md 'Option A')."""
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local)
    if not shas:
        return ""
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   f_obs_nat: float, kappa_nat: float, a_ratio: float,
                   supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion + schema-v2 3-tuple row (atomic single open('a'))."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = f_obs = f_emit * a_fold/a_now with a_fold/a_now = {a_ratio:.5f} < 1 => REDSHIFT (f_obs<f_emit); "
        f"mag = at substrate-natural kappa_nat={kappa_nat:.3e}s the fold acoustic peak redshifts to "
        f"f_obs={f_obs_nat:.3e}Hz = {np.log10(f_obs_nat/LISA_LO):.1f} decades ABOVE LISA-band-lo (FAIL=GHz+); "
        f"regime = band placement GHz+ across the ENTIRE swept kappa band [1e-20,1e-10] (verdict does NOT flip "
        f"to LISA anywhere in the physically-swept normalization range)\n"
    )
    anchor_row = (
        f"# ANCHOR=f_emit_is_van_Hove_fold_ACOUSTIC_freq_NOT_thermal_GUT "
        f"# {GATE_ID} substrate-first: emission scale = M_KK/(2pi) in s^-1 (~1.8e40 Hz at kappa_nat); "
        f"redshift a_fold/a_now=0.47229 (gate-5 S96-OBS-LRD-ASSEMBLY-CLOCK a_fold_over_a0=2.1173, DIRECTLY RESOLVED); "
        f"naive thermal-GUT route (S58 Method-3, T_*~M_KK) gives only ~1.7 GHz; acoustic dispersion moves the peak "
        f"~31 decades the WRONG way (UP, not into mHz) => D4 resolved AGAINST mHz; CGWB-peak LISA flagship EVAPORATES; "
        f"kappa to reach LISA = 25 s/M_KK^-1 (42.5 OOM from kappa_nat, 11.4 OOM beyond swept-band upper edge); "
        f"DISTINCT from the Omega_GW AMPLITUDE flagship at gate-4 (chosen LISA pivot, separate observable)\n"
    )
    rows = [line, companion, schema_v2_row, anchor_row]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md \"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write("".join(rows))


# =============================================================================
# 1. LOAD UPSTREAM  (NUMBERS FIRST)
# =============================================================================
print("=" * 86)
print(f"{GATE_ID} — CGWB peak observed frequency via the substrate redshift chain (D4)")
print("=" * 86)

# Input-pin SHAs (audit trail)
sha_canonical = sha256_of(CANONICAL)
sha_lrd_clock = sha256_of(LRD_CLOCK_NPZ)
sha_s54       = sha256_of(S54_NPZ)
print(f"  SHA canonical_constants.py        = {sha_canonical[:16]}")
print(f"  SHA s96_obs_lrd_assembly_clock    = {sha_lrd_clock[:16]}")
print(f"  SHA s54_scale_factor              = {sha_s54[:16]}")

# --- the redshift anchor (gate-5, DIRECTLY RESOLVED — no extrapolation) ---
if LRD_CLOCK_NPZ.exists():
    clk = np.load(LRD_CLOCK_NPZ, allow_pickle=True)
    a_fold_over_a0 = float(np.asarray(clk["a_fold_over_a0_computed"]).ravel()[0])  # (local) 2.1173
    kappa_sweep = np.asarray(clk["kappa_sweep"], dtype=float).ravel()              # (local) 121 pts [1e-20,1e-10]
    kappa_nat_g5 = float(np.asarray(clk["kappa_nat"]).ravel()[0])                  # (local) 8.86e-42
    upstream_source = "gate-5 s96_obs_lrd_assembly_clock.npz (DIRECTLY RESOLVED anchor)"  # (local)
else:
    # honest-close fallback per mechanical-closure-discipline (same upstream input via s54)
    s54 = np.load(S54_NPZ, allow_pickle=True)
    a_fold_over_a0 = float(np.asarray(s54["a_at_fold"]).ravel()[0])                # (local) 2.1173
    kappa_sweep = np.logspace(-20, -10, 121)                                       # (local) reconstruct knob
    kappa_nat_g5 = float(M_KK_inv_seconds)                                          # (local)
    upstream_source = "s54_scale_factor.npz a_at_fold (gate-5 npz absent; same upstream input)"  # (local)

a_fold_over_a_now = 1.0 / a_fold_over_a0      # (local) < 1  => redshift
print()
print(f"  redshift anchor: a(tau_fold)/a(0) = {a_fold_over_a0:.6f}  ({upstream_source})")
print(f"  => a_fold/a_now = 1/{a_fold_over_a0:.4f} = {a_fold_over_a_now:.6f}  (<1 => REDSHIFT, f_obs<f_emit)")

# --- substrate-natural M_KK^-1 -> s normalization (the open knob's natural value) ---
kappa_nat = float(M_KK_inv_seconds)           # (local) 8.860440e-42 s  = hbar/M_KK
M_KK_per_sec = 1.0 / kappa_nat                 # (local) M_KK in s^-1  (angular-freq scale)
# cross-check kappa_nat == hbar/M_KK and == gate-5 kappa_nat
kappa_from_hbar = hbar_GeV_s / M_KK            # (local)
print(f"  kappa_nat (M_KK_inv_seconds)      = {kappa_nat:.6e} s ;  hbar/M_KK = {kappa_from_hbar:.6e} s "
      f"(rel {abs(kappa_nat-kappa_from_hbar)/kappa_nat:.2e})")
print(f"  gate-5 kappa_nat                  = {kappa_nat_g5:.6e} s  (consistency)")
print(f"  M_KK in s^-1 (=1/kappa_nat)       = {M_KK_per_sec:.6e} s^-1")

# =============================================================================
# 2. EMISSION FREQUENCY — fold characteristic ACOUSTIC frequency (substrate-first)
# =============================================================================
# omega_tilde (dimensionless, in M_KK units) -> physical angular freq = omega_tilde * M_KK[s^-1]
# ordinary f_emit = omega_phys / (2 pi)  [Hz]
TWO_PI = 2.0 * np.pi   # (local)

def f_emit_from_mode(omega_tilde: float, kappa: float) -> float:
    """Physical emission frequency [Hz] for an M_KK-unit angular-frequency mode at normalization kappa."""
    return omega_tilde * (1.0 / kappa) / TWO_PI

# Candidate fold characteristic modes (M_KK units). The CANONICAL choice is the M_KK
# characteristic scale itself (omega_tilde = 1: the only intrinsic frequency scale of the
# fold); the named acoustic modes bracket it and are reported as the emission-scale spread.
modes = {
    "M_KK_char(omega~=1)": 1.0,            # canonical fold characteristic acoustic scale
    "omega_L1":            float(omega_L1),
    "omega_PV":            float(omega_PV),
    "omega_tau":           float(omega_tau),
    "v_g_B2_fold":         float(v_g_B2_fold),
    "c_fabric":            float(c_fabric),
}
OMEGA_TILDE_CANON = 1.0   # (local) canonical emission scale = M_KK characteristic frequency

print()
print("  EMISSION + OBSERVED frequency at substrate-natural kappa_nat (per fold acoustic mode):")
print(f"  {'mode':22s} {'omega~(M_KK)':>14s} {'f_emit[Hz]':>14s} {'f_obs[Hz]':>14s} {'band(obs)':>16s}")
print("  " + "-" * 84)
f_emit_nat = {}
f_obs_nat = {}
for name, wt in modes.items():
    fe = f_emit_from_mode(wt, kappa_nat)            # (local)
    fo = fe * a_fold_over_a_now                      # (local)
    f_emit_nat[name] = fe
    f_obs_nat[name] = fo
    print(f"  {name:22s} {wt:>14.6g} {fe:>14.4e} {fo:>14.4e} {detector_band(fo):>16s}")

f_emit_canon_nat = f_emit_nat["M_KK_char(omega~=1)"]   # (local)
f_obs_canon_nat  = f_obs_nat["M_KK_char(omega~=1)"]    # (local) the canonical peak observed freq at kappa_nat

# =============================================================================
# 3. NAIVE THERMAL-GUT ROUTE  (S58 Method-3 dimensional analysis; the FAIL baseline)
# =============================================================================
k_B_GeV_per_K = 8.617333262e-14   # (local) GeV/K
T0_K          = 2.7255            # (local) K (Fixsen 2009)
T0_GeV        = T0_K * k_B_GeV_per_K              # (local)
GeV_to_Hz     = 1.0 / (TWO_PI * hbar_GeV_s)       # (local) ordinary-freq conversion 1 GeV -> Hz
# Method 3:  f_0 ~ T_* * T_0 / M_Pl  with T_* ~ M_KK
f_GUT_naive = M_KK * T0_GeV / M_Pl_reduced * GeV_to_Hz   # (local)
decades_GHz_to_mHz = np.log10(1e9 / 1e-3)                 # (local) = 12.0

print()
print("  NAIVE THERMAL-GUT route (S58 Method-3 dim. analysis, T_* ~ M_KK):")
print(f"    f_GUT_naive = M_KK*T_0/M_Pl * GeV->Hz = {f_GUT_naive:.4e} Hz  [{detector_band(f_GUT_naive)}]")
print(f"    decades GHz->mHz needed (log10(1e9/1e-3)) = {decades_GHz_to_mHz:.1f}")

# =============================================================================
# 4. SCAN OVER THE OPEN NORMALIZATION KNOB kappa  (the load-bearing free parameter)
# =============================================================================
# f_obs(kappa) for the canonical mode across the swept band; classify each point.
f_obs_sweep = f_emit_from_mode(OMEGA_TILDE_CANON, kappa_sweep) * a_fold_over_a_now   # (local)
bands_sweep = np.array([band_class(f) for f in f_obs_sweep])                         # (local)
n_lisa   = int(np.sum(bands_sweep == "LISA"))        # (local)
n_ptadec = int(np.sum(bands_sweep == "PTA-DECIGO"))  # (local)
n_ghz    = int(np.sum(bands_sweep == "GHZ+"))        # (local)
n_other  = int(np.sum(bands_sweep == "OTHER"))       # (local)
any_lisa_in_band = bool(n_lisa > 0)                  # (local)

# kappa values that WOULD hit each target band (canonical mode, after redshift):
#   f_target = omega~ /(kappa*2pi) * (a_fold/a_now)  =>  kappa = omega~ *(a_fold/a_now)/(2pi*f_target)
def kappa_for_target(f_target: float) -> float:
    return OMEGA_TILDE_CANON * a_fold_over_a_now / (TWO_PI * f_target)  # (local)

kappa_LISA   = kappa_for_target(f_LISA_pivot)   # (local) ~25 s/M_KK^-1
kappa_GHz    = kappa_for_target(1e9)            # (local)
kappa_DECIGO = kappa_for_target(0.3)            # (local)
kappa_PTA    = kappa_for_target(3e-8)           # (local)
kappa_band_lo, kappa_band_hi = float(kappa_sweep.min()), float(kappa_sweep.max())  # (local)
OOM_kappa_LISA_vs_nat   = np.log10(kappa_LISA / kappa_nat)        # (local)
OOM_kappa_LISA_vs_bandhi = np.log10(kappa_LISA / kappa_band_hi)   # (local)

print()
print("  NORMALIZATION-KNOB SCAN (canonical mode, over gate-5 swept band [%.0e, %.0e] s/M_KK^-1):"
      % (kappa_band_lo, kappa_band_hi))
print(f"    f_obs(kappa_lo={kappa_band_lo:.0e}) = {f_obs_sweep[0]:.4e} Hz  [{detector_band(f_obs_sweep[0])}]")
print(f"    f_obs(kappa_hi={kappa_band_hi:.0e}) = {f_obs_sweep[-1]:.4e} Hz  [{detector_band(f_obs_sweep[-1])}]")
print(f"    band counts over sweep: LISA={n_lisa}  PTA-DECIGO={n_ptadec}  GHZ+={n_ghz}  OTHER={n_other}  (N={len(kappa_sweep)})")
print(f"    kappa needed for LISA pivot ({f_LISA_pivot} Hz) = {kappa_LISA:.4e} s/M_KK^-1")
print(f"      => {OOM_kappa_LISA_vs_nat:.2f} OOM from kappa_nat ; {OOM_kappa_LISA_vs_bandhi:.2f} OOM beyond swept-band upper edge")
print(f"    decades f_obs(kappa_nat, canonical) ABOVE LISA-band-lo = {np.log10(f_obs_canon_nat/LISA_LO):.3f}")
print(f"    decades f_obs(kappa_nat, canonical) ABOVE GHz floor    = {np.log10(f_obs_canon_nat/GHZ_FLOOR):.3f}")

# =============================================================================
# 5. GATE EVALUATION (pre-registered set-membership + [SIGN] 3-tuple)
# =============================================================================
# SIGN: redshift direction f_obs < f_emit  <=>  a_fold/a_now < 1
sign_v = "PASS" if a_fold_over_a_now < 1.0 else "FAIL"

# MAGNITUDE: band placement of the canonical f_obs at the substrate-natural kappa_nat.
band_nat = band_class(f_obs_canon_nat)   # (local)
if band_nat == "LISA":
    mag_v = "PASS"
elif band_nat == "PTA-DECIGO":
    mag_v = "INFO"
else:  # GHZ+ or OTHER (gap regions, all far from LISA)
    mag_v = "FAIL"

# REGIME: is the verdict normalization-set (does the band placement flip across the swept band)?
# VALID iff the placement does NOT reach LISA anywhere in the physically-swept band
# (the FAIL is robust to the knob within its physical range); MARGINAL/BREAKDOWN reserved for
# a knob-flipped verdict. Across [1e-20,1e-10] the canonical mode is GHZ+ at every point.
if not any_lisa_in_band:
    reg_v = "VALID"   # FAIL is stable across the entire swept normalization band
else:
    # some kappa in-band reaches LISA: the verdict is normalization-conditional
    frac_lisa = n_lisa / len(kappa_sweep)  # (local)
    reg_v = "MARGINAL" if frac_lisa <= 0.5 else "BREAKDOWN"

# Composite collapse (gate-verdicts.md PRE-REGISTERED rule)
if reg_v == "BREAKDOWN":
    composite = "FAIL"
elif sign_v == "FAIL":
    composite = "FAIL"
elif mag_v == "FAIL" and reg_v == "VALID":
    composite = "FAIL"
elif mag_v == "FAIL" and reg_v == "MARGINAL":
    composite = "INFO"
elif mag_v == "INFO":
    composite = "INFO"
else:
    composite = "PASS"

print()
print("  === Verdict 3-tuple ===")
print(f"    sign_verdict      = {sign_v}   (a_fold/a_now={a_fold_over_a_now:.5f} < 1 => redshift f_obs<f_emit)")
print(f"    magnitude_verdict = {mag_v}   (canonical f_obs(kappa_nat) band = {band_nat}; LISA=PASS/PTA-DECIGO=INFO/GHZ+=FAIL)")
print(f"    regime_verdict    = {reg_v}   (LISA reachable in swept band? {any_lisa_in_band}; VALID=stable-FAIL)")
print(f"    COMPOSITE         = {composite}")

# D4 resolution string
if composite == "PASS":
    d4 = "D4 resolved IN FAVOR of mHz: acoustic dispersion delivers the shift; LISA CGWB-peak flagship STANDS."
elif composite == "INFO":
    d4 = ("D4 normalization-conditional / detector-reassigned: f_obs band is set by the open M_KK^-1->s knob; "
          "report which band and pin kappa before claiming LISA.")
else:
    d4 = ("D4 resolved AGAINST mHz: the fold ACOUSTIC emission scale is ~M_KK/(2pi) (~1.8e40 Hz at kappa_nat); "
          "redshift (factor 0.472) is negligible; acoustic dispersion moves the peak ~31 decades the WRONG way (UP). "
          "The LISA CGWB-PEAK-FREQUENCY flagship EVAPORATES (distinct from the Omega_GW AMPLITUDE flagship, gate-4). "
          "GHz+ across the ENTIRE physically-swept normalization band.")
print()
print("  D4:", d4)

# =============================================================================
# 6. PLOT
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# (a) f_obs vs kappa knob, with detector bands shaded
ax = axes[0]
ax.loglog(kappa_sweep, f_obs_sweep, "-", color="crimson", lw=2.0, label=r"$f_{\rm obs}(\kappa)$ canonical fold mode")
ax.axhspan(LISA_LO, LISA_HI, color="green", alpha=0.18, label="LISA [0.1,100] mHz (PASS band)")
ax.axhspan(PTA_LO, PTA_HI, color="blue", alpha=0.14, label="PTA (nHz)")
ax.axhspan(DECIGO_LO, DECIGO_HI, color="purple", alpha=0.14, label="DECIGO [0.1,10] Hz")
ax.axhspan(GHZ_FLOOR, 1e44, color="grey", alpha=0.20, label="GHz+ (FAIL)")
ax.axhline(f_GUT_naive, color="orange", ls="--", lw=1.3, label=f"naive thermal-GUT {f_GUT_naive:.1e} Hz")
ax.axvline(kappa_nat, color="black", ls=":", lw=1.6, label=fr"$\kappa_{{\rm nat}}=\hbar/M_{{KK}}={kappa_nat:.2e}$ s")
ax.axvline(kappa_LISA, color="green", ls=":", lw=1.3, label=fr"$\kappa$ for LISA $={kappa_LISA:.1e}$ s")
ax.scatter([kappa_nat], [f_obs_canon_nat], color="black", s=70, zorder=6,
           label=fr"$f_{{\rm obs}}(\kappa_{{\rm nat}})={f_obs_canon_nat:.2e}$ Hz")
ax.set_xlabel(r"$\kappa$  (M$_{KK}^{-1}\to$ s normalization knob)")
ax.set_ylabel(r"$f_{\rm obs}$  [Hz]")
ax.set_title(f"{GATE_ID}: observed CGWB peak vs the open normalization knob\n"
             f"COMPOSITE = {composite}  (D4 {'IN FAVOR' if composite=='PASS' else ('CONDITIONAL' if composite=='INFO' else 'AGAINST')} mHz)")
ax.legend(fontsize=7, loc="upper right")
ax.grid(True, which="both", alpha=0.25)

# (b) emission-scale spread across fold acoustic modes (at kappa_nat) + redshift
ax = axes[1]
names = list(modes.keys())
fe_vals = [f_emit_nat[n] for n in names]   # (local)
fo_vals = [f_obs_nat[n] for n in names]    # (local)
ypos = np.arange(len(names))               # (local)
ax.barh(ypos - 0.18, np.log10(fe_vals), height=0.34, color="steelblue", label=r"$\log_{10} f_{\rm emit}$")
ax.barh(ypos + 0.18, np.log10(fo_vals), height=0.34, color="crimson", label=r"$\log_{10} f_{\rm obs}$ (redshifted)")
ax.axvline(np.log10(LISA_LO), color="green", ls="--", lw=1.2)
ax.axvline(np.log10(LISA_HI), color="green", ls="--", lw=1.2, label="LISA band edges")
ax.axvline(np.log10(f_GUT_naive), color="orange", ls=":", lw=1.3, label="naive GUT (GHz)")
ax.set_yticks(ypos)
ax.set_yticklabels(names, fontsize=8)
ax.set_xlabel(r"$\log_{10}(f\ /\ {\rm Hz})$  at $\kappa_{\rm nat}$")
ax.set_title("Fold acoustic emission-scale spread\n(all ~30-45 decades above LISA at the natural normalization)")
ax.legend(fontsize=8, loc="lower right")
ax.grid(True, axis="x", alpha=0.25)

plt.tight_layout()
fig.savefig(OUT_PNG, dpi=130)
print(f"\n  Plot -> {OUT_PNG}")

# =============================================================================
# 7. SAVE DATA
# =============================================================================
value_str = (
    f"composite={composite};"
    f"f_obs_kappa_nat={f_obs_canon_nat:.4e}Hz_band={band_nat};"
    f"f_emit_kappa_nat={f_emit_canon_nat:.4e}Hz;"
    f"a_fold_over_a_now={a_fold_over_a_now:.5f}_REDSHIFT;"
    f"a_fold_over_a0={a_fold_over_a0:.4f}_gate5_DIRECTLY_RESOLVED;"
    f"kappa_nat={kappa_nat:.4e}s_=hbar/M_KK;"
    f"decades_above_LISA={np.log10(f_obs_canon_nat/LISA_LO):.2f};"
    f"decades_above_GHz={np.log10(f_obs_canon_nat/GHZ_FLOOR):.2f};"
    f"naive_thermal_GUT={f_GUT_naive:.3e}Hz_{detector_band(f_GUT_naive)};"
    f"GHz->mHz_decades_needed={decades_GHz_to_mHz:.1f};"
    f"sweep_band[{kappa_band_lo:.0e},{kappa_band_hi:.0e}]_LISA_pts={n_lisa}_PTAdec={n_ptadec}_GHz={n_ghz}_other={n_other};"
    f"any_LISA_in_sweep={any_lisa_in_band};"
    f"kappa_for_LISA={kappa_LISA:.3e}s_{OOM_kappa_LISA_vs_nat:.1f}OOM_from_nat_{OOM_kappa_LISA_vs_bandhi:.1f}OOM_beyond_bandhi;"
    f"f_emit=van_Hove_fold_ACOUSTIC_NOT_thermal_GUT;flagship=CGWB-PEAK-EVAPORATES_distinct_from_OmegaGW_amplitude_gate4"
)

# input-pin map for the audit SHA
pins = {
    "M_KK": float(M_KK),
    "M_KK_inv_seconds": float(M_KK_inv_seconds),
    "c_fabric": float(c_fabric),
    "Mach_max": float(Mach_max),
    "f_LISA_pivot": float(f_LISA_pivot),
    "a_fold_over_a0": float(a_fold_over_a0),
    "omega_tilde_canon": float(OMEGA_TILDE_CANON),
    "scheme": SCHEME,
    "convention": CONVENTION,
    "sha_canonical": sha_canonical,
    "sha_lrd_clock": sha_lrd_clock,
    "sha_s54": sha_s54,
}

np.savez(
    OUT_NPZ,
    # core results
    composite=np.array([composite]),
    f_obs_kappa_nat=np.array([f_obs_canon_nat]),
    f_emit_kappa_nat=np.array([f_emit_canon_nat]),
    a_fold_over_a0=np.array([a_fold_over_a0]),
    a_fold_over_a_now=np.array([a_fold_over_a_now]),
    kappa_nat=np.array([kappa_nat]),
    M_KK_per_sec=np.array([M_KK_per_sec]),
    # mode spread
    mode_names=np.array(list(modes.keys())),
    mode_omega_tilde=np.array([modes[k] for k in modes]),
    f_emit_modes=np.array([f_emit_nat[k] for k in modes]),
    f_obs_modes=np.array([f_obs_nat[k] for k in modes]),
    # normalization-knob sweep
    kappa_sweep=kappa_sweep,
    f_obs_sweep=f_obs_sweep,
    bands_sweep=bands_sweep,
    n_lisa=np.array([n_lisa]), n_ptadec=np.array([n_ptadec]),
    n_ghz=np.array([n_ghz]), n_other=np.array([n_other]),
    any_lisa_in_sweep=np.array([any_lisa_in_band]),
    # target-band kappas
    kappa_LISA=np.array([kappa_LISA]), kappa_GHz=np.array([kappa_GHz]),
    kappa_DECIGO=np.array([kappa_DECIGO]), kappa_PTA=np.array([kappa_PTA]),
    OOM_kappa_LISA_vs_nat=np.array([OOM_kappa_LISA_vs_nat]),
    OOM_kappa_LISA_vs_bandhi=np.array([OOM_kappa_LISA_vs_bandhi]),
    # naive baseline
    f_GUT_naive=np.array([f_GUT_naive]),
    decades_GHz_to_mHz=np.array([decades_GHz_to_mHz]),
    decades_obs_above_LISA=np.array([np.log10(f_obs_canon_nat/LISA_LO)]),
    decades_obs_above_GHz=np.array([np.log10(f_obs_canon_nat/GHZ_FLOOR)]),
    # 3-tuple
    sign_verdict=np.array([sign_v]),
    magnitude_verdict=np.array([mag_v]),
    regime_verdict=np.array([reg_v]),
    value_str=np.array([value_str]),
    d4_resolution=np.array([d4]),
    scheme=np.array([SCHEME]),
    convention=np.array([CONVENTION]),
    upstream_source=np.array([upstream_source]),
)
print(f"  Data -> {OUT_NPZ}")

# =============================================================================
# 8. EMIT VERDICT LINE (canonical + dual-SHA + schema-v2 3-tuple)
# =============================================================================
audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL, pins)
prior_sha = find_prior_audit_sha()
supersedes_sha = prior_sha if (prior_sha and prior_sha != audit_sha) else ""

print()
print("  === Closure ===")
print(f"    audit_sha256   = {audit_sha}")
print(f"    content_sha256 = {content_sha}")
if supersedes_sha:
    print(f"    supersedes     = {supersedes_sha}  (Option A corrective re-emission)")

append_verdict(
    composite, value_str, audit_sha, content_sha,
    sign_v, mag_v, reg_v,
    f_obs_canon_nat, kappa_nat, a_fold_over_a_now,
    supersedes_sha=supersedes_sha,
)
print(f"  Verdict appended -> {VERDICT_TXT}")
print()
print("=" * 86)
print(f"COMPLETE — {GATE_ID}: {composite}  (sign={sign_v} mag={mag_v} regime={reg_v})")
print("=" * 86)
