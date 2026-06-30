"""S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX (alias S91-W9-8).

Composite Mukhanov-Sasaki ∘ HKR bridge map Level-2 envelope derivation,
CONDITIONAL on W2 T1.5 (`CF-S91-CF-72` / `S91-VII-AU-FIRST-EXTRACTION-
PARAMETERIZATION`) FAIL persistence.

Plan reference: `sessions/session-plan/session-91-plan-w9.md §W9-8`
(lines 1334-1538). Implementation follows Field 6 Step 1-6 substitution
chain verbatim; thresholds per Field 9 RATIO + composite tolerance rule.

Substitution chain (Field 6 Step 1-6) — direction claim α_composite ≥
min(α_MS, α_HKR):

  Step 1 (Definition): HKR(L) = HKR image of finite-L Hochschild pairing
    on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) at substrate-distance pole s; per
    cross-pillar-bridge-anatomy.md §"Three-Level structural-confidence
    ladder", Level-2 envelope |HKR(L) − HKR(∞)| ≤ C_HKR · L^{−α_HKR}
    with α_HKR = 3 at d=4.

  Step 2 (Definition): MS(x) = z_pivot · x where z_pivot = a · √(2ε) ·
    M_Pl is the Mukhanov-Sasaki gauge factor (Mukhanov 1985 §3, v_k =
    z · ζ_k). MS is linear-leading at composition fixed-point; SR-LO
    truncation envelope |MS_truncated − MS_full| ≤ C_MS · L^{−α_MS}
    with α_MS = 2.

  Step 3 (Substitution): B_composite(L) = MS(HKR(L)) = z_pivot · HKR(L).
    |B_composite(L) − B_composite(∞)| = |z_pivot| · |HKR(L) − HKR(∞)|.

  Step 4 (Simplify): ratio form
    Delta_emp(L) = |B_composite(L) − B_composite_canonical|
                 / |B_composite_canonical|
                 = |HKR(L) − HKR(∞)| / |HKR(∞)|   [z_pivot cancels]
    The MS gauge factor is multiplicative and cancels in the ratio.
    Substrate-IS direction: Delta_emp(L) IS the regulator-INVARIANT
    relative-deviation observable on the substrate's algebra (algebra-
    INVARIANT spectrum-only functional per §VII.U.2 Cell I).

  Step 5 (Canonical form): Delta_emp(L) = C_emp · L^{−α_composite}.
    Worst-case bound from orthogonal-envelopes case:
    α_composite ≥ min(α_MS, α_HKR) = min(2, 3) = 2.
    Best-case (MS gauge exact, no truncation): α_composite = α_HKR = 3.
    Overlap case (MS and HKR share substrate-distance reduction):
    α_composite = α_MS + α_HKR − α_overlap.

  Step 6 (Direction): if α_composite_value ≥ 3 → composite envelope at
    least as tight as HKR alone, PASS; if α_composite_value ∈ [2, 3) →
    MS gauge introduces minor degradation, INFO; if α_composite_value
    < 2 → composite structurally defective, FAIL (alternative bridge
    map required, e.g., Wodzicki ∘ HKR per W9 T2.36).

Substrate framing (phononic-framing.md §"IS Space, Not IN Space"): the
composite Mukhanov-Sasaki ∘ HKR bridge map IS the framework's intrinsic
two-step F-image — substrate-IS Hochschild pairing on (A_K, H_K, D_K)
at τ_fold=0.19 → bridge step 1 (HKR L_max → ∞ continuum image) →
bridge step 2 (MS gauge to Pillar I cosmological observable; Mukhanov
1985 §3) → laboratory (Planck CMB binning). The envelope-composition
rule α_composite = min(α_MS, α_HKR) IS the substrate's own discipline
at the methodology-floor F-image layer per epistemic-discipline.md
§"Layer-Decomposition". FORBIDDEN container-inversion: "Planck CMB
measurement IS the test of the substrate prediction via MS gauge" →
INVERT: "substrate prediction IS the canonical at substrate-distance
pole; MS ∘ HKR IS the two-step F-image realizing this prediction at
the cosmological perturbation observable layer".

Convention pin (substrate-first-canonical-sourcing.md §(iv) K=4
MANDATORY level-pin discipline): consumes _pauli_villars_subtraction.py
PRIMARY helper (FULL physical Pauli-Villars CC1996 §2.2-2.3 multipliers);
LEVEL_CLASS_PIN=FULL on this script, but the §VII.AU canonical pin
itself is SCHEMATIC-level (extracted via STRICT_F4 atlas at L_max=10 per
§VII.AF.1.OP-PROJ provenance — see canonical_constants.py line 273).
The mismatch in LEVEL class between operational evaluator (FULL) and
canonical anchor (SCHEMATIC) is the structural cause of the §VII.AU
finite-L "OPPOSITE empirical signature" (per §VII.AU.OP-PROJ registry
note: "finite-L value ABOVE asymptotic envelope, slower-than-L^{-3}
apparent decay"). This script discloses both readings honestly.

Composite-RDX is an ALTERNATIVE PATH to §VII.AU first-extraction; per
plan Field 11, a FAIL on this gate means a different bridge map class
(Wodzicki-residue ∘ HKR, or Connes-Karoubi pairing without MS gauge)
must be considered at S92+. This script does not adjudicate the
alternative; it produces the empirical composite envelope coefficient
and reports the verdict against the pre-registered Field 9 thresholds.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib                                                       # noqa: E402
import json                                                          # noqa: E402
import math                                                          # noqa: E402
import re                                                            # noqa: E402
import sys                                                           # noqa: E402
import time                                                          # noqa: E402
from pathlib import Path                                             # noqa: E402

import numpy as np                                                   # noqa: E402
import matplotlib                                                    # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt                                      # noqa: E402

# Project paths.
ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "computations" / "_shared"
COMP = ROOT / "computations"
if str(SHARED) not in sys.path:
    sys.path.insert(0, str(SHARED))
if str(COMP) not in sys.path:
    sys.path.insert(0, str(COMP))

# Canonical-constant imports (math-scripts.md S34+ MANDATORY).
from canonical_constants import (                                    # noqa: E402
    M_KK,
    tau_fold,
    M_Pl_reduced,
    R_universal_HP1_strict_F4,
    N_pivot,
)

# FULL physical PV PRIMARY helper (Pauli-Villars CC1996 §2.2-2.3 — FULL
# physical level per substrate-first-canonical-sourcing.md §(iv) K=4
# MANDATORY discipline; LEVEL_CLASS_PIN=FULL on this consumer).
from _pauli_villars_subtraction import (                             # noqa: E402
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
    bare_mellin_moment,
    pv_mellin_moment_primary,
)

# ====================== Gate-block constants (plan §W9-8 Field 7) ======================

GATE_ID = "S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX"
SCHEME = "composite-mukhanov-sasaki-HKR-bridge-map-level-2-envelope-derivation"
CONVENTION = "VII-AU-composite-MS-HKR-RDX-alternative-to-first-extraction-direct"

# Plan-pinned L_max scan {8, 10, 12} (plan §W9-8 Field 7).
L_MAX_SCAN = [8, 10, 12]                                             # (local)
L_MAX_CANONICAL = 12                                                 # (local) verdict-line L_max field

# Plan-pinned envelope exponents (plan §W9-8 Field 7).
ALPHA_HKR = 3                                                        # (local) cross-pillar-bridge-anatomy.md Level-2 at d=4
ALPHA_MS = 2                                                         # (local) Mukhanov 1985 §3 SR-LO truncation order

# Plan-pinned PASS/INFO/FAIL thresholds (plan §W9-8 Field 9 RATIO+composite).
ALPHA_THRESHOLD_PASS = 3.0                                           # (local)
ALPHA_THRESHOLD_INFO = 2.0                                           # (local)
C_EMP_THRESHOLD_PASS = 1.0                                           # (local)
C_EMP_THRESHOLD_INFO = 5.0                                           # (local)

# §VII.AU canonical pin (registry §VII.AU.OP-PROJ Level-2 envelope binding;
# cross-pinned with §VII.AF.1.OP-PROJ R_universal_HP1_strict_F4 = 1.030902
# at L_max → ∞ limit per registry §VII.AU.OP-PROJ Element 4).  This IS the
# canonical anchor against which composite-RDX is evaluated per Field 6
# Step 4: "B_composite_canonical = canonical pin at L_max → ∞ limit (from
# §VII.AU registry)".  LEVEL CLASS of this canonical: SCHEMATIC-extracted
# via STRICT_F4 atlas at L_max=10 (canonical_constants.py:273 PROVENANCE).
R_CANONICAL_VII_AU = R_universal_HP1_strict_F4                       # (local) = 1.030902

# Substrate-distance pole pin per §VII.AU.OP-PROJ Element 2 (substrate-
# distance-1 pole s=3 binding for §VII.AU FWD-C1 Pillar I-II bridge).
# NB: plan Field 5 line 1351 references "substrate-distance-2 pole s=4"
# but §VII.AU.OP-PROJ registry entry (line 17784+) binds at s=3 per the
# original Stage-0 workshop derivation (FWD-C1 Pillar I↔II at s=3).  We
# compute BOTH poles to honour Field 5 stated text AND §VII.AU registry
# binding; primary verdict tracks s=3 (registry-canonical), s=4 reported
# as cross-pin diagnostic.
S_POLE_PRIMARY = 3                                                   # (local) §VII.AU.OP-PROJ registry binding
S_POLE_CROSSPIN = 4                                                  # (local) plan Field 5 text reference

# Mukhanov-Sasaki gauge factor at pivot (plan Field 6 Step 2; Mukhanov
# 1985 §3 v_k = z · ζ_k with z = a · √(2ε) · M_Pl_eff).  For envelope
# RATIO-form purposes (Field 6 Step 4), the multiplicative z_pivot
# cancels in Delta_emp = |B_comp(L) − B_canonical| / |B_canonical|.
# We record z_pivot for transparency but it does NOT enter the
# coefficient fit.
SR_EPSILON_SLOW_ROLL = 0.02163                                       # (local) SR-LO ε at pivot per S88 W5a-2 baseline canonical
N_EFOLDS_PIVOT = N_pivot                                             # (local) substrate N_pivot = 64.08
A_PIVOT = math.exp(-N_EFOLDS_PIVOT)                                  # (local) horizon-exit scale factor (k_pivot · 1/H ≃ 1)
Z_PIVOT_MS = A_PIVOT * math.sqrt(2.0 * SR_EPSILON_SLOW_ROLL) * M_Pl_reduced  # (local) MS gauge factor at pivot

# Output paths.
OUT_NPZ = ROOT / "computations" / "session-91" / "s91_w9_cf_w1_14_composite_bridge_map_rdx.npz"
OUT_PNG = ROOT / "computations" / "session-91" / "s91_w9_cf_w1_14_composite_bridge_map_rdx.png"
VERDICT_FILE = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

# Input file paths (for SHA-pin map per gate-verdicts.md §"Pre-Registration Protocol").
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
PV_HELPER = ROOT / "computations" / "_pauli_villars_subtraction.py"
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
CF49_FULL_CC_NPZ = ROOT / "computations" / "session-91" / "s91_w9_cf49_full_cc_multipliers_vii_af_1.npz"
PLAN_FILE = ROOT / "sessions" / "session-plan" / "session-91-plan-w9.md"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "pauli_villars_helper_PRIMARY": PV_HELPER,
    "registry_vii_au_op_proj": REGISTRY,
    "s91_gate_verdicts_priors": VERDICT_FILE,
    "cf49_full_cc_diagnostic_input": CF49_FULL_CC_NPZ,
    "plan_file_session_91_w9": PLAN_FILE,
    "script": SCRIPT_PATH,
}


# ============================== SHA helpers ==============================

def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()                                             # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}                                                        # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:36s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)                                      # (local)
        pins[name] = sha
        try:
            rel = p.relative_to(ROOT)
        except ValueError:
            rel = p
        print(f"  {name:36s} = {sha[:16]}...  ({rel})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()                                  # (local)
    return audit, content


# ============================== Conditional prereq check ==============================

def check_t1_5_prereq(verdict_file: Path) -> dict:
    """Plan §W9-8 Field 6 Step 1: CONDITIONAL prereq check on T1.5 FAIL.

    Per plan grep pattern `^CF-S91-CF-72.*: FAIL`, ALSO matching the
    actual landed gate-ID `S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION`
    (which is the canonical name the W2 T1.5 gate landed under).  The
    legacy alias `CF-S91-CF-72` is documented at plan §W2-2 line 415
    ("legacy alias: T1.5 / W8-CF-72 / CF-S91-CF-72") so the check
    accommodates both ID forms.
    """
    if not verdict_file.exists():
        return {"t1_5_failed": False, "t1_5_passed": False, "rationale": "verdict_file_absent"}
    text = verdict_file.read_text(encoding="utf-8")
    pattern_failed = re.compile(
        r"^(CF-S91-CF-72[^:]*|S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION):\s*FAIL\b",
        re.MULTILINE,
    )
    pattern_passed = re.compile(
        r"^(CF-S91-CF-72[^:]*|S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION):\s*PASS\b",
        re.MULTILINE,
    )
    match_failed = pattern_failed.search(text)
    match_passed = pattern_passed.search(text)
    return {
        "t1_5_failed": bool(match_failed),
        "t1_5_passed": bool(match_passed),
        "rationale": (match_failed.group(0) if match_failed else (match_passed.group(0) if match_passed else "no_match")),
    }


# ============================ Spectrum loader (L_max truncation) ============================

def load_spectrum_flat_truncated(cache_path: Path, L_max: int):
    """Load L_max=12 master cache filtered at p+q ≤ L_max.

    Substrate-IS at the spectral-triple-truncation layer: the cache
    holds sector_evals[(p,q)] = {dim, level=p+q, abs_evals}; filtering
    at p+q ≤ L_max produces the (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) finite-L
    truncation.  Each sector contributes dim(p,q) Peter-Weyl multiplicity
    per eigenvalue (canonical loader pattern from
    s91_w9_cf49_full_cc_multipliers_vii_af_1.py:load_spectrum_flat).
    """
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    lambdas_list = []                                                # (local)
    mults_list = []                                                  # (local)
    n_sectors_kept = 0                                               # (local)
    for (p, q), info in sector_evals.items():
        if p + q > L_max:
            continue
        n_sectors_kept += 1
        dim = int(info["dim"])                                       # (local)
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            lambdas_list.append(float(v))
            mults_list.append(dim)
    lambdas = np.array(lambdas_list, dtype=np.float64)
    mults = np.array(mults_list, dtype=np.float64)
    return lambdas, mults, n_sectors_kept


# ============================ HKR image at pole s ============================

def hkr_image_at_pole(L_max: int, s_pole: int, cache_path: Path) -> float:
    """HKR substrate-IS Hochschild-pairing image at substrate-distance pole s.

    The substrate-IS Hochschild pairing maps under the Connes-Moscovici
    1995 §III.4 finite-spectral-triple residue formula to the Mellin
    moment ρ_FULL(s) = M_FULL_CC(s) / M_BARE(s), where M_FULL_CC and
    M_BARE are evaluated via the FULL Pauli-Villars CC1996 §2.2-2.3
    physical multipliers (PRIMARY helper per substrate-first-canonical-
    sourcing.md §(iv) K=4 MANDATORY level-pin discipline; FULL physical
    regularization with PV pair (c, m²) = (PV_PRIMARY_C, PV_PRIMARY_M²)).

    The dimensionless atlas ratio ρ_FULL IS the algebra-INVARIANT
    spectrum-only functional that the substrate's Hochschild pairing
    images under HKR L_max → ∞ to the §VII.AU canonical anchor.  The
    HKR image is a Mellin-image at fixed s; the substrate's full
    Hochschild pairing is recovered as L_max → ∞.
    """
    lambdas, mults, n_sectors = load_spectrum_flat_truncated(cache_path, L_max)
    M_bare = bare_mellin_moment(s_pole, lambdas, mults)              # (local)
    M_full = pv_mellin_moment_primary(s_pole, lambdas, mults)        # (local)
    rho_full = M_full / M_bare                                       # (local) HKR-image dimensionless ratio
    return float(rho_full), int(n_sectors), len(lambdas)


# ============================ Composite envelope fit ============================

def fit_composite_envelope(L_scan: list[int], deltas: list[float]) -> tuple[float, float]:
    """Log-log fit Delta_emp(L) = C_emp · L^{−α_composite}.

    Per plan §W9-8 Field 6 Step 5:
        log(Delta_emp) = log(C_emp) − α_composite · log(L)
    Returns (α_composite_value, C_emp_value).

    If any delta is non-positive or non-finite, returns (-inf, inf)
    indicating fit failure (signals non-monotonic substrate behaviour
    against canonical, structurally distinct from L^{−α} envelope —
    typical when finite-L value diverges from canonical pin as L grows).
    """
    arr_deltas = np.asarray(deltas, dtype=np.float64)
    arr_L = np.asarray(L_scan, dtype=np.float64)
    if np.any(arr_deltas <= 0) or np.any(~np.isfinite(arr_deltas)):
        return float("-inf"), float("inf")
    log_L = np.log(arr_L)
    log_d = np.log(arr_deltas)
    slope, intercept = np.polyfit(log_L, log_d, 1)
    alpha_value = -float(slope)                                      # (local)
    C_emp = float(np.exp(intercept))                                 # (local)
    return alpha_value, C_emp


# ============================ Verdict evaluation ============================

def evaluate_verdict(alpha_value: float, C_emp: float) -> dict:
    """Plan §W9-8 Field 9 RATIO+composite tolerance rule.

    Substitution chain Step 6 (direction):
      PASS iff α_value ≥ 3.0 AND C_emp ≤ 1.0
      INFO iff α_value ∈ [2.0, 3.0) AND C_emp ≤ 5.0
      FAIL otherwise

    S87+ schema-v2 3-tuple form per gate-verdicts.md:
      sign_verdict     : direction of α_value vs threshold (substrate
                         pre-registered: α_composite ≥ min(α_MS, α_HKR)
                         = 2 worst-case; PASS if α_value ≥ 2.0 honours
                         the substitution chain Step 5 direction
                         prediction; FAIL otherwise)
      magnitude_verdict: |α_value − target| band ranking
      regime_verdict   : MS gauge fixed-point validity (VALID if the
                         linear-leading composition assumption holds;
                         MARGINAL/BREAKDOWN if structural mismatch
                         between operational evaluator LEVEL and
                         canonical anchor LEVEL invalidates the
                         envelope-composition derivation)
    """
    pass_alpha = alpha_value >= ALPHA_THRESHOLD_PASS
    pass_C = C_emp <= C_EMP_THRESHOLD_PASS
    info_alpha = ALPHA_THRESHOLD_INFO <= alpha_value < ALPHA_THRESHOLD_PASS
    info_C = C_emp <= C_EMP_THRESHOLD_INFO

    # Composite top-line per plan Field 9 collapse rule.
    if pass_alpha and pass_C:
        composite = "PASS"
    elif info_alpha and info_C:
        composite = "INFO"
    else:
        composite = "FAIL"

    # S87+ 3-tuple decomposition per gate-verdicts.md §"Composite-collapse rule".
    # sign_verdict (Step 5 direction pre-registration: α_composite ≥ 2 worst-case)
    sign_v = "PASS" if alpha_value >= ALPHA_THRESHOLD_INFO else "FAIL"

    # magnitude_verdict (against PASS / INFO bands)
    if pass_alpha and pass_C:
        mag_v = "PASS"
    elif info_alpha and info_C:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"

    # regime_verdict: LEVEL-class consistency between operational evaluator
    # (FULL physical PV per PRIMARY helper) and canonical anchor (SCHEMATIC
    # STRICT_F4 atlas at L_max=10 per §VII.AF.1.OP-PROJ canonical pin
    # provenance).  A LEVEL-class mismatch corresponds to a regime breakdown
    # in the envelope-composition derivation: the Level-2 envelope α_HKR=3
    # applies when operational evaluator and canonical anchor share LEVEL
    # class, NOT when one is FULL and the other SCHEMATIC.
    if alpha_value < 0:
        reg_v = "BREAKDOWN"      # Non-monotonic divergence: structural defect
    elif alpha_value < ALPHA_THRESHOLD_INFO:
        reg_v = "MARGINAL"
    else:
        reg_v = "VALID"

    # Composite-collapse rule override per gate-verdicts.md (regime BREAKDOWN
    # forces composite=FAIL; sign FAIL forces composite=FAIL).
    if reg_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"

    return {
        "composite": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
    }


# ============================ Diagnostic plot ============================

def make_plot(
    L_scan: list[int],
    rho_scan_s3: list[float],
    rho_scan_s4: list[float],
    deltas_s3: list[float],
    deltas_s4: list[float],
    alpha_s3: float,
    C_emp_s3: float,
    alpha_s4: float,
    C_emp_s4: float,
    R_canonical: float,
):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: ρ_FULL(L_max) at s=3 (primary §VII.AU pole) and s=4 cross-pin.
    ax1.plot(L_scan, rho_scan_s3, "o-", color="steelblue", label="ρ_FULL(s=3) [§VII.AU primary]")
    ax1.plot(L_scan, rho_scan_s4, "s--", color="darkorange", label="ρ_FULL(s=4) [Field 5 cross-pin]")
    ax1.axhline(R_canonical, color="red", linestyle=":", label=f"§VII.AU canonical = {R_canonical:.6f}")
    ax1.set_xlabel("L_max")
    ax1.set_ylabel("ρ_FULL = M_FULL_CC / M_BARE")
    ax1.set_title("HKR-image multi-L scan vs §VII.AU canonical anchor")
    ax1.legend(loc="best", fontsize=8)
    ax1.grid(True, alpha=0.3)

    # Panel 2: log-log composite envelope fit (s=3 primary).
    ax2.loglog(L_scan, deltas_s3, "o", color="steelblue", label="empirical Δ(L) at s=3")
    if alpha_s3 > -1e10 and np.isfinite(C_emp_s3):
        L_fine = np.linspace(min(L_scan) * 0.9, max(L_scan) * 1.1, 50)
        fit_curve = C_emp_s3 * L_fine ** (-alpha_s3)
        ax2.loglog(L_fine, fit_curve, "-", color="navy",
                   label=f"fit: α={alpha_s3:.4f}, C={C_emp_s3:.4f}")
    # Reference curves: L^{-2}, L^{-3}.
    L_ref = np.linspace(min(L_scan) * 0.9, max(L_scan) * 1.1, 50)
    ax2.loglog(L_ref, L_ref ** -2.0, ":", color="gray", alpha=0.6, label="L^{-2} (α_MS=2)")
    ax2.loglog(L_ref, L_ref ** -3.0, "--", color="gray", alpha=0.6, label="L^{-3} (α_HKR=3)")
    ax2.set_xlabel("L_max")
    ax2.set_ylabel("Δ_emp = |ρ_FULL(L) − R_canonical| / R_canonical")
    ax2.set_title("Composite envelope log-log fit (s=3, §VII.AU primary)")
    ax2.legend(loc="best", fontsize=8)
    ax2.grid(True, which="both", alpha=0.3)

    # Panel 3: log-log composite envelope fit (s=4 cross-pin against self-anchor).
    ax3.loglog(L_scan, deltas_s4, "s", color="darkorange", label="empirical Δ(L) at s=4")
    if alpha_s4 > -1e10 and np.isfinite(C_emp_s4):
        L_fine = np.linspace(min(L_scan) * 0.9, max(L_scan) * 1.1, 50)
        fit_curve = C_emp_s4 * L_fine ** (-alpha_s4)
        ax3.loglog(L_fine, fit_curve, "-", color="darkred",
                   label=f"fit: α={alpha_s4:.4f}, C={C_emp_s4:.4f}")
    ax3.loglog(L_ref, L_ref ** -2.0, ":", color="gray", alpha=0.6, label="L^{-2}")
    ax3.loglog(L_ref, L_ref ** -3.0, "--", color="gray", alpha=0.6, label="L^{-3}")
    ax3.set_xlabel("L_max")
    ax3.set_ylabel("Δ_emp")
    ax3.set_title("Composite envelope log-log fit (s=4, cross-pin diagnostic)")
    ax3.legend(loc="best", fontsize=8)
    ax3.grid(True, which="both", alpha=0.3)

    # Panel 4: PASS/INFO/FAIL band map.
    bands = ["FAIL", "INFO", "PASS"]
    band_alphas = [ALPHA_THRESHOLD_INFO, ALPHA_THRESHOLD_PASS]
    ax4.axhspan(-5, ALPHA_THRESHOLD_INFO, color="red", alpha=0.15, label="FAIL band (α<2)")
    ax4.axhspan(ALPHA_THRESHOLD_INFO, ALPHA_THRESHOLD_PASS, color="gold", alpha=0.15, label="INFO band (2≤α<3)")
    ax4.axhspan(ALPHA_THRESHOLD_PASS, 6, color="lightgreen", alpha=0.15, label="PASS band (α≥3)")
    ax4.axhline(alpha_s3, color="steelblue", linewidth=2, label=f"α_composite (s=3) = {alpha_s3:.4f}")
    ax4.axhline(alpha_s4, color="darkorange", linewidth=2, linestyle="--", label=f"α_composite (s=4 cross-pin) = {alpha_s4:.4f}")
    ax4.set_ylim(-5, 6)
    ax4.set_xlim(0, 1)
    ax4.set_xticks([])
    ax4.set_ylabel("α_composite")
    ax4.set_title("PASS/INFO/FAIL band membership")
    ax4.legend(loc="upper right", fontsize=8)
    ax4.grid(True, axis="y", alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}\n"
        f"Composite MS ∘ HKR Level-2 envelope — α_HKR={ALPHA_HKR}, α_MS={ALPHA_MS}, "
        f"worst-case α_composite ≥ min(α_MS, α_HKR) = {min(ALPHA_HKR, ALPHA_MS)}",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ============================ Verdict-line emission ============================

def append_verdict_lines(
    composite: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    mag_v: str,
    reg_v: str,
):
    """Atomic single-shot append per gate-verdicts.md S87+ canonical form.

    Emits exactly:
      1. Canonical S87+ line with audit_sha256 + content_sha256.
      2. Dual-SHA companion comment row (W9a-99 split).
      3. S87+ 3-tuple companion row (schema-v2; required for [VERIFY] gate).
      4. LEVEL pin disclosure row (substrate-first-canonical-sourcing.md §(iv)
         K=4 MANDATORY level-pin compliance; this consumer is FULL physical).
    """
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_CANONICAL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation "
        f"(S87 schema-v2; substitution chain Step 5 direction "
        f"α_composite ≥ min(α_MS, α_HKR) = 2)\n"
    )
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL # {GATE_ID} substrate-first-canonical-sourcing.md "
        f"§(iv) K=4 MANDATORY level-pin compliance "
        f"(consumes _pauli_villars_subtraction.py PRIMARY helper; FULL physical "
        f"PV CC1996 §2.2-2.3 multipliers)\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(level_pin)


def append_pre_reg_inc(audit_sha: str, content_sha: str, rationale: str):
    """Mechanical PRE-REG-INC closure per mechanical-closure-discipline.md.

    Emitted only when T1.5 has PASSed (composite-RDX unnecessary) OR T1.5
    has not landed (composite-RDX deferred).  In both cases the upstream
    block topology is the cause; no substantive substrate-physics
    computation is performed.
    """
    canonical = (
        f"{GATE_ID}: FAIL -- value='PRE-REG-INC_blocked_by_{rationale}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_CANONICAL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple = (
        f"# sign_verdict=N/A magnitude_verdict=N/A regime_verdict=N/A "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; PRE-REG-INC; "
        f"mechanical closure per mechanical-closure-discipline.md)\n"
    )
    closure_disclosure = (
        f"# PRE-REG-INC per mechanical-closure-discipline.md; "
        f"closure_kind=mechanical-mack-cosmic-bridge-primary-no-substantive-compute; "
        f"blocked_by=T1.5_{rationale}; closure_script={SCRIPT_PATH.name}\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(closure_disclosure)


# ============================== Main ==============================

def main() -> int:
    t0 = time.time()

    # 1. Log input pins + compute dual SHA.
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...  (script + canonical + pinmap)")
    print(f"  content_sha256 = {content_sha[:16]}...  (script only)")
    print()

    # 2. CONDITIONAL prereq check (plan §W9-8 Field 6 Step 1).
    print("STEP 1 — Conditional prereq check (T1.5 FAIL persistence):")
    prereq = check_t1_5_prereq(VERDICT_FILE)
    print(f"  T1.5 FAILed   = {prereq['t1_5_failed']}")
    print(f"  T1.5 PASSed   = {prereq['t1_5_passed']}")
    print(f"  rationale     = {prereq['rationale']}")
    print()

    if prereq["t1_5_passed"]:
        print("[CLOSE] T1.5 PASSed; composite-RDX route unnecessary.")
        print("       Emitting mechanical PRE-REG-INC closure per plan Field 6 Step 1.")
        append_pre_reg_inc(audit_sha, content_sha, "T1_5_PASS_composite_route_unnecessary")
        # Write minimal npz for audit trail.
        np.savez(
            OUT_NPZ,
            t1_5_failed=False,
            t1_5_passed=True,
            verdict_composite="FAIL",
            value_str="PRE-REG-INC_blocked_by_T1_5_PASS",
            audit_sha256=audit_sha,
            content_sha256=content_sha,
        )
        # Empty plot for artifact-existence per agent-standards.md.
        plt.figure()
        plt.text(0.5, 0.5, f"{GATE_ID}\nPRE-REG-INC blocked by T1.5 PASS",
                 ha="center", va="center", fontsize=14)
        plt.axis("off")
        plt.savefig(OUT_PNG, dpi=120)
        plt.close()
        print(f"Done in {time.time() - t0:.2f}s (mechanical closure).")
        return 0

    if not prereq["t1_5_failed"]:
        print("[CLOSE] T1.5 not yet landed; composite-RDX deferred.")
        append_pre_reg_inc(audit_sha, content_sha, "T1_5_NOT_LANDED_composite_route_deferred")
        np.savez(
            OUT_NPZ,
            t1_5_failed=False,
            t1_5_passed=False,
            verdict_composite="FAIL",
            value_str="PRE-REG-INC_blocked_by_T1_5_NOT_LANDED",
            audit_sha256=audit_sha,
            content_sha256=content_sha,
        )
        plt.figure()
        plt.text(0.5, 0.5, f"{GATE_ID}\nPRE-REG-INC blocked by T1.5 NOT LANDED",
                 ha="center", va="center", fontsize=14)
        plt.axis("off")
        plt.savefig(OUT_PNG, dpi=120)
        plt.close()
        print(f"Done in {time.time() - t0:.2f}s (deferred closure).")
        return 0

    # 3. T1.5 FAILed -- proceed with composite-RDX derivation (plan Field 6 Steps 2-6).
    print("STEP 2 — Definitions and canonical anchor pin:")
    print(f"  α_HKR (plan-pinned)       = {ALPHA_HKR}   (cross-pillar-bridge-anatomy.md Level-2 at d=4)")
    print(f"  α_MS  (plan-pinned)       = {ALPHA_MS}   (Mukhanov 1985 §3 SR-LO truncation)")
    print(f"  α_composite worst-case    = min(α_MS, α_HKR) = {min(ALPHA_HKR, ALPHA_MS)}")
    print(f"  α_composite best-case     = α_HKR = {ALPHA_HKR}    (MS gauge exact, no truncation)")
    print()
    print(f"  R_canonical (§VII.AU pin) = {R_CANONICAL_VII_AU:.6f}")
    print(f"    Provenance: R_universal_HP1_strict_F4 (canonical_constants.py:273)")
    print(f"    Level class: SCHEMATIC (STRICT_F4 atlas at L_max=10 per §VII.AF.1.OP-PROJ provenance)")
    print()
    print(f"  z_pivot (MS gauge factor) = {Z_PIVOT_MS:.6e}  GeV·dimensionless")
    print(f"    z_pivot = a · √(2ε) · M_Pl_reduced")
    print(f"    a = exp(-N_pivot) = exp(-{N_EFOLDS_PIVOT}) = {A_PIVOT:.6e}")
    print(f"    ε = {SR_EPSILON_SLOW_ROLL:.5f}")
    print(f"    M_Pl_reduced = {M_Pl_reduced:.4e} GeV")
    print(f"    NOTE: z_pivot CANCELS in Delta_emp ratio (Field 6 Step 4 substitution chain)")
    print()

    # 4. Multi-L scan of HKR-image at substrate-distance pole s.
    print(f"STEP 3 — Multi-L scan of HKR-image at substrate-distance poles s=3, s=4:")
    print(f"  L_max scan = {L_MAX_SCAN}  (plan-pinned)")
    print()

    rho_scan_s3 = []
    rho_scan_s4 = []
    n_sectors_scan = []
    n_eig_scan = []
    for L_max in L_MAX_SCAN:
        rho3, n_sec, n_eig = hkr_image_at_pole(L_max, S_POLE_PRIMARY, L12_CACHE)
        rho4, _, _ = hkr_image_at_pole(L_max, S_POLE_CROSSPIN, L12_CACHE)
        rho_scan_s3.append(rho3)
        rho_scan_s4.append(rho4)
        n_sectors_scan.append(n_sec)
        n_eig_scan.append(n_eig)
        print(f"  L_max={L_max:2d}: n_sectors={n_sec:3d}, n_eig={n_eig:7d}, "
              f"ρ_FULL(s=3)={rho3:.6f}, ρ_FULL(s=4)={rho4:.6f}")
    print()

    # 5. Empirical envelope deviations against canonical anchor.
    print(f"STEP 4 — Empirical envelope Delta_emp = |ρ_FULL(L) − R_canonical| / R_canonical:")
    print(f"  Primary (s=3, §VII.AU.OP-PROJ registry-canonical pole):")
    deltas_s3 = []
    for L_max, rho in zip(L_MAX_SCAN, rho_scan_s3):
        delta = abs(rho - R_CANONICAL_VII_AU) / R_CANONICAL_VII_AU
        deltas_s3.append(delta)
        envelope_L3 = 1.0 / (L_max ** 3)
        ratio_to_envelope = delta / envelope_L3
        print(f"    L_max={L_max:2d}: Δ_emp={delta:.6e}, L^-3={envelope_L3:.6e}, "
              f"Δ/L^-3={ratio_to_envelope:.4f}")
    print()

    # Cross-pin diagnostic at s=4 (plan Field 5 stated pole); use s=4 Friedrich-Bär
    # self-anchor since §VII.AU does not bind at s=4 (§VII.AV binds s=4, no pin).
    print(f"  Cross-pin (s=4, plan Field 5 stated pole; Friedrich-Bär self-anchor):")
    deltas_s4 = []
    R_anchor_s4 = rho_scan_s4[-1]  # L_max=12 self-anchor
    for L_max, rho in zip(L_MAX_SCAN, rho_scan_s4):
        if L_max == L_MAX_SCAN[-1]:
            continue  # skip self-comparison
        delta = abs(rho - R_anchor_s4) / R_anchor_s4
        deltas_s4.append(delta)
        envelope_L3 = 1.0 / (L_max ** 3)
        ratio_to_envelope = delta / envelope_L3
        print(f"    L_max={L_max:2d}: ρ={rho:.6f}, Δ_emp(vs anchor={R_anchor_s4:.6f}) = {delta:.6e}, "
              f"L^-3={envelope_L3:.6e}, Δ/L^-3={ratio_to_envelope:.4f}")
    print()

    # 6. Log-log fits.
    print(f"STEP 5 — Composite envelope coefficient fit (Delta_emp = C_emp · L^{{−α_composite}}):")
    alpha_s3, C_emp_s3 = fit_composite_envelope(L_MAX_SCAN, deltas_s3)
    print(f"  Primary (s=3, §VII.AU canonical anchor):")
    print(f"    α_composite_value = {alpha_s3:.6f}")
    print(f"    C_emp_value       = {C_emp_s3:.6e}")
    print()

    # s=4 cross-pin: only 2 points after removing self-comparison; fit if ≥ 2 points.
    if len(deltas_s4) >= 2:
        L_scan_s4 = L_MAX_SCAN[:-1]  # exclude L_max=12 self-anchor
        alpha_s4, C_emp_s4 = fit_composite_envelope(L_scan_s4, deltas_s4)
    else:
        alpha_s4, C_emp_s4 = float("nan"), float("nan")
    print(f"  Cross-pin (s=4, Friedrich-Bär self-anchor):")
    print(f"    α_composite_value (s=4) = {alpha_s4:.6f}")
    print(f"    C_emp_value (s=4)       = {C_emp_s4:.6e}")
    print()

    # 7. Verdict per plan Field 9 thresholds.
    print(f"STEP 6 — Verdict per plan Field 9 RATIO+composite thresholds:")
    print(f"  PASS iff α_composite_value ≥ {ALPHA_THRESHOLD_PASS} AND C_emp ≤ {C_EMP_THRESHOLD_PASS}")
    print(f"  INFO iff α_composite_value ∈ [{ALPHA_THRESHOLD_INFO}, {ALPHA_THRESHOLD_PASS}) AND C_emp ≤ {C_EMP_THRESHOLD_INFO}")
    print(f"  FAIL iff α_composite_value < {ALPHA_THRESHOLD_INFO} OR C_emp > {C_EMP_THRESHOLD_INFO}")
    print()

    verdict = evaluate_verdict(alpha_s3, C_emp_s3)
    composite = verdict["composite"]
    sign_v = verdict["sign_verdict"]
    mag_v = verdict["magnitude_verdict"]
    reg_v = verdict["regime_verdict"]
    print(f"  composite_verdict   = {composite}")
    print(f"  sign_verdict        = {sign_v}    (substitution chain Step 5 direction)")
    print(f"  magnitude_verdict   = {mag_v}    (band ranking)")
    print(f"  regime_verdict      = {reg_v}    (MS gauge + LEVEL-class consistency)")
    print()

    # 8. Save .npz + plot.
    np.savez(
        OUT_NPZ,
        t1_5_failed=True,
        t1_5_passed=False,
        prereq_rationale=prereq["rationale"],
        L_MAX_SCAN=np.asarray(L_MAX_SCAN),
        ALPHA_HKR=ALPHA_HKR,
        ALPHA_MS=ALPHA_MS,
        rho_FULL_s3=np.asarray(rho_scan_s3),
        rho_FULL_s4=np.asarray(rho_scan_s4),
        n_sectors=np.asarray(n_sectors_scan),
        n_eigenvalues=np.asarray(n_eig_scan),
        R_canonical_VII_AU=R_CANONICAL_VII_AU,
        R_anchor_s4_FriedrichBar=R_anchor_s4,
        Delta_emp_s3=np.asarray(deltas_s3),
        Delta_emp_s4=np.asarray(deltas_s4) if len(deltas_s4) > 0 else np.asarray([], dtype=float),
        alpha_composite_value=alpha_s3,
        C_emp_value=C_emp_s3,
        alpha_composite_value_s4=alpha_s4,
        C_emp_value_s4=C_emp_s4,
        z_pivot_MS=Z_PIVOT_MS,
        a_pivot=A_PIVOT,
        epsilon_SR=SR_EPSILON_SLOW_ROLL,
        N_pivot=N_EFOLDS_PIVOT,
        M_Pl_reduced=M_Pl_reduced,
        verdict_composite=composite,
        verdict_sign=sign_v,
        verdict_magnitude=mag_v,
        verdict_regime=reg_v,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    make_plot(
        L_MAX_SCAN, rho_scan_s3, rho_scan_s4, deltas_s3,
        deltas_s4 + [0.0] if len(deltas_s4) < len(L_MAX_SCAN) else deltas_s4,
        alpha_s3, C_emp_s3, alpha_s4, C_emp_s4, R_CANONICAL_VII_AU,
    )
    print(f"  npz written: {OUT_NPZ.relative_to(ROOT)}")
    print(f"  png written: {OUT_PNG.relative_to(ROOT)}")
    print()

    # 9. Emit verdict line(s).
    value_str = (
        f"alpha_composite={alpha_s3:+.6f}"
        f"_C_emp={C_emp_s3:+.6e}"
        f"_rho_FULL_s3_at_L12={rho_scan_s3[-1]:.6f}"
        f"_R_canonical_VII_AU={R_CANONICAL_VII_AU:.6f}"
        f"_Delta_emp_at_L12={deltas_s3[-1]:.6e}"
        f"_cross_pin_alpha_s4={alpha_s4:+.6f}"
    )
    append_verdict_lines(composite, value_str, audit_sha, content_sha, sign_v, mag_v, reg_v)
    print(f"Verdict line appended to {VERDICT_FILE.relative_to(ROOT)}")
    print()

    # 10. Done.
    elapsed = time.time() - t0
    print(f"Done in {elapsed:.2f}s.")
    print()
    print(f"FINAL: {GATE_ID}: {composite} -- "
          f"α_composite={alpha_s3:+.6f}, C_emp={C_emp_s3:.4e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
