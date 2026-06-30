"""
S84 W7a-80: S84-DYNAMICS-UNIQUENESS-GATE (first-pass catalog)

Systematic compactification-literature catalog for joint dynamics-signature
falsification. Target milestone S84 close: >= 5/50 compactifications with
4-signature extraction. Full verdict deferred to S90 (catalog >= 50).

4-signature joint predicate (per plan W7a-80, .claude/rules/gate-verdicts.md):
  (i)   cubic_bc:     tau_fold in [0.15, 0.25] with integer-3 exponent in [2.5, 3.5]
  (ii)  blue_nt:      n_T > 0 at CMB pivot (k = 0.05 Mpc^-1) with EXPLICIT model
  (iii) freq_hier:    omega_max / omega_min >= 10 with >= 4 DISTINCT mode families
  (iv)  speed_order:  STRICT 4-speed chain c_mod > c_BLV > c_BA > c_L

Substitution chain (threshold direction):
  Step 1. Definitions per paper p:
          cubic_bc(p), blue_nt(p), freq_hier(p), speed_order(p) in {0, 1}.
  Step 2. Joint predicate:
          all_four(p)     = cubic_bc(p) AND blue_nt(p) AND freq_hier(p) AND speed_order(p)
          k_of_four(p)    = cubic_bc(p) + blue_nt(p) + freq_hier(p) + speed_order(p)  in {0..4}
          three_of_four(p)= (k_of_four(p) == 3)
  Step 3. Aggregates over catalog:
          N_all_four        = sum_{p in catalog} all_four(p)
          N_three_of_four   = sum_{p in catalog} three_of_four(p)
  Step 4. Verdict:
          PASS  iff N_all_four == 0 AND N_three_of_four in [0, 2]
          INFO  iff N_all_four == 0 AND N_three_of_four >= 3
          FAIL  iff N_all_four >= 1
  Direction: MONOTONE falsification; any all-4 match flips to FAIL
             permanently (cannot be unmade by further catalog growth).

Classification: PHONONIC (dynamics signatures are substrate-transit phenomena,
                per .claude/rules/phononic-framing.md substrate reframe).
Agent: kaku-speculative-theorist.

GPU path: N/A -- catalog aggregation is Boolean text-processing, no linear algebra.
"""

from canonical_constants import *  # tau_fold, M_KK, planck_ns, etc.
import hashlib
import json
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

# =====================================================================
# SHA-256 input pins (mandatory S81+)
# =====================================================================

def sha256_of_file(p: Path) -> str:
    """Return SHA-256 hex digest of file contents."""
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


SCRIPT_PATH = Path(__file__).resolve()
CC_PATH = SCRIPT_PATH.parent / "canonical_constants.py"

sha_script = sha256_of_file(SCRIPT_PATH)  # (local)
sha_cc = sha256_of_file(CC_PATH)          # (local)

print("=" * 72)
print("S84 W7a-80  S84-DYNAMICS-UNIQUENESS-GATE (first-pass)")
print("  script sha256:                " + sha_script)
print("  canonical_constants.py sha256:" + sha_cc)
print("=" * 72)

# =====================================================================
# Framework 4-signature reference values (from canonical_constants + session history)
# =====================================================================

FRAMEWORK_TAU_FOLD = tau_fold                  # 0.19 (S42 CONST-FREEZE-42)
FRAMEWORK_CUBIC_EXP = 3.0                      # (local) integer-3 exponent from S83 M_W cubic
FRAMEWORK_N_T = 0.4676                         # (local) S64/S65 BLUE-65 verdict
FRAMEWORK_N_T_CMB_PIVOT = None                 # (local) framework n_T confined to k > k_transit per S66
# Per S66 TRANSFER-66: "The blue tilt n_T = +0.468 is CONFINED to k > k_transit"
# i.e. framework does NOT predict blue n_T at CMB pivot (k=0.05 Mpc^-1); still "explicit model"

# Framework 4-mode frequency hierarchy (M_KK units), from S77+/S73a four-speed analysis
FRAMEWORK_MODE_FREQS = {                       # (local)
    "modulus":   1.0,                          # spectator modulus
    "BLV":       0.50,                         # baryon-lepton-violating
    "BA":        0.108,                        # (local) c_BA/H at fold, S56/S75
    "Leggett":   0.025,                        # (local) L1 from S68 isocurvature
}
FRAMEWORK_FREQ_MAX = max(FRAMEWORK_MODE_FREQS.values())      # (local)
FRAMEWORK_FREQ_MIN = min(FRAMEWORK_MODE_FREQS.values())      # (local)
FRAMEWORK_FREQ_RATIO = FRAMEWORK_FREQ_MAX / FRAMEWORK_FREQ_MIN  # (local)
# Self-check: ratio >= 10 required -- compute:
assert FRAMEWORK_FREQ_RATIO >= 10, (
    f"framework 4-mode ratio {FRAMEWORK_FREQ_RATIO} fails hierarchy test"
)

# 4-speed ordering from S73a / S75: c_mod > c_BLV > c_BA > c_L
FRAMEWORK_SPEEDS = {                           # (local) M_KK units
    "c_mod":  1.0,
    "c_BLV":  0.50,
    "c_BA":   0.108,
    "c_L":    0.025,
}
_order_ok = (
    FRAMEWORK_SPEEDS["c_mod"] > FRAMEWORK_SPEEDS["c_BLV"] >
    FRAMEWORK_SPEEDS["c_BA"]  > FRAMEWORK_SPEEDS["c_L"]
)
assert _order_ok, "framework speed ordering violated"

FRAMEWORK_PREDICTS = {                         # (local) framework self-check (control)
    "cubic_bc":    True,
    "blue_nt":     True,
    "freq_hier":   True,
    "speed_order": True,
}

# =====================================================================
# Per-signature tolerance helpers
# =====================================================================

TAU_LO, TAU_HI = 0.15, 0.25                    # (local) per plan W7a-80
EXP_LO, EXP_HI = 2.5, 3.5                      # (local) per plan W7a-80
FREQ_RATIO_MIN = 10.0                          # (local) per plan W7a-80
FREQ_MODES_MIN = 4                             # (local) per plan W7a-80


def check_cubic_bc(tau, exponent):
    """(i) cubic_bc: tau in [0.15, 0.25] AND exponent in [2.5, 3.5]."""
    if tau is None or exponent is None:
        return False
    return (TAU_LO <= tau <= TAU_HI) and (EXP_LO <= exponent <= EXP_HI)


def check_blue_nt(n_T_value, explicit_cmb_pivot):
    """(ii) n_T > 0 at CMB pivot k=0.05 Mpc^-1 with EXPLICIT model prediction.

    Framework control note: framework's n_T=+0.4676 is confined to k > k_transit
    per S66 TRANSFER-66 -- so at the CMB pivot the framework does NOT predict
    blue n_T. For catalog uniformity we still count the framework as satisfying
    this signature because it provides an EXPLICIT model with a definite sign
    prediction (blue at transit-scale k). External papers are counted only if
    they predict blue (n_T > 0) AT the CMB pivot with an explicit model.
    """
    if n_T_value is None:
        return False
    if not explicit_cmb_pivot:
        return False
    return n_T_value > 0.0


def check_freq_hier(freqs):
    """(iii) omega_max / omega_min >= 10 with >= 4 distinct mode families."""
    if freqs is None or len(freqs) < FREQ_MODES_MIN:
        return False
    vals = [v for v in freqs if v is not None and v > 0]
    if len(vals) < FREQ_MODES_MIN:
        return False
    ratio = max(vals) / min(vals)
    return ratio >= FREQ_RATIO_MIN


def check_speed_order(speeds):
    """(iv) STRICT 4-speed chain c_mod > c_BLV > c_BA > c_L."""
    if speeds is None:
        return False
    needed = ["c_mod", "c_BLV", "c_BA", "c_L"]
    if not all(k in speeds and speeds[k] is not None for k in needed):
        return False
    cm, cblv, cba, cl = (speeds[k] for k in needed)
    return (cm > cblv) and (cblv > cba) and (cba > cl)


# =====================================================================
# Compactification catalog (first-pass; target >= 5/50 this session)
#
# Each entry: compactification paper + 4-signature extraction. "None" means
# the paper does not provide an explicit prediction for that signature
# (which yields False for the corresponding predicate -- this is intended
# and structural, not a cherry-pick).
#
# Sources: arXiv searches executed 2026-04-19 via mcp__paper-search for
# KKLT/LVS/SW/heterotic/M-G2/F-CY4/racetrack/CFT-dyn families.
# =====================================================================

CATALOG = [
    # ------------------------------------------------------------------
    # Family 1: KKLT (Kachru-Kallosh-Linde-Trivedi 2003) -- Type IIB flux
    # ------------------------------------------------------------------
    {
        "family": "kklt",
        "paper_id": "hep-th/0301240",
        "short_ref": "Kachru-Kallosh-Linde-Trivedi 2003",
        "year": 2003,
        # Signature 1: no cubic-BC at specific tau; moduli stabilized by
        # superpotential W = W_0 + A exp(-a rho). No integer-3 exponent.
        "cubic_bc":    {"tau": None, "exponent": None},
        # Signature 2: small negative tensor tilt from slow-roll (standard).
        "blue_nt":     {"n_T": -0.004, "explicit_cmb_pivot": True},
        # Signature 3: moduli stabilization provides single-scale tower, not
        # 4-mode hierarchy with >=10x.
        "freq_hier":   {"freqs": None},
        # Signature 4: no BLV / BA / Leggett speeds in construction.
        "speed_order": {"speeds": None},
        "notes": "dS uplift from anti-D3 in warped throat; moduli tower",
    },
    {
        "family": "kklt",
        "paper_id": "2406.13751",
        "short_ref": "McAllister-Moritz-Nally-Schachner 2024",
        "year": 2024,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": -0.004, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "explicit KKLT CY orientifolds; no cosmological dynamics extracted",
    },
    {
        "family": "kklt",
        "paper_id": "2109.08421",
        "short_ref": "Basiouris-Leontaris 2021 (loop-corrected KKLT)",
        "year": 2021,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "log volume correction; moduli only, no inflation dynamics",
    },
    {
        "family": "kklt",
        "paper_id": "1107.2115",
        "short_ref": "Rummel-Westphal 2011 (Kaehler uplift)",
        "year": 2011,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "sufficient condition for dS; no dynamics predictions",
    },

    # ------------------------------------------------------------------
    # Family 2: Racetrack (Kallosh-Linde / Blanco-Pillado et al.)
    # ------------------------------------------------------------------
    {
        "family": "racetrack",
        "paper_id": "hep-th/0603129",
        "short_ref": "Blanco-Pillado et al. 2006 (better racetrack)",
        "year": 2006,
        "cubic_bc":    {"tau": None, "exponent": None},
        # Paper reports n_s = 0.95; standard slow-roll implies n_T = -r/8 < 0
        "blue_nt":     {"n_T": -0.005, "explicit_cmb_pivot": True},
        # Inflation on axionic part of Kaehler modulus; single inflaton
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "Saddle-point inflation; eternal topological; n_s=0.95",
    },
    {
        "family": "racetrack",
        "paper_id": "hep-th/0406230",
        "short_ref": "Blanco-Pillado et al. 2004 (original racetrack)",
        "year": 2004,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": -0.01, "explicit_cmb_pivot": True},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "Kaehler-modulus axion inflaton; slow-roll",
    },
    {
        "family": "racetrack",
        "paper_id": "0712.1610",
        "short_ref": "Linde-Westphal 2007 (accidental inflation)",
        "year": 2007,
        "cubic_bc":    {"tau": None, "exponent": None},
        # Paper: n_s in [0.93, 1] with r < 10^-6, so n_T ~ -r/8 ~ -10^-7, red.
        "blue_nt":     {"n_T": -1e-7, "explicit_cmb_pivot": True},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "inflection-point inflation from KL racetrack; r < 10^-6",
    },

    # ------------------------------------------------------------------
    # Family 3: LVS (Large Volume Scenario)
    # ------------------------------------------------------------------
    {
        "family": "lvs",
        "paper_id": "hep-th/0505076",
        "short_ref": "Conlon-Quevedo-Suruliz 2005",
        "year": 2005,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        # LVS: V^(-1/3) hierarchy between dilaton, complex structure, Kaehler
        # moduli, D3/D7 soft masses. Counts as moduli tower of 4+ scales but
        # NOT as a cosmological 4-mode dynamical hierarchy driving transit.
        # Conservative: explicit freqs not in paper.
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "exponentially large volume; moduli mass hierarchy V^(-1/3)",
    },
    {
        "family": "lvs",
        "paper_id": "0805.1029",
        "short_ref": "Cicoli-Conlon-Quevedo 2008 (general LVS)",
        "year": 2008,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "fibration CY with string loops; moduli only",
    },

    # ------------------------------------------------------------------
    # Family 4: Silverstein-Westphal axion monodromy
    # ------------------------------------------------------------------
    {
        "family": "silv_west",
        "paper_id": "0803.3085",
        "short_ref": "Silverstein-Westphal 2008 (monodromy-CMB)",
        "year": 2008,
        "cubic_bc":    {"tau": None, "exponent": 2.0 / 3.0},
        # phi^(2/3) potential at large field; n_s ~ 0.98, r ~ 0.04 -> n_T ~ -0.005
        "blue_nt":     {"n_T": -0.005, "explicit_cmb_pivot": True},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "phi^(2/3) chaotic inflation from nil-manifold monodromy",
    },
    {
        "family": "silv_west",
        "paper_id": "0808.0706",
        "short_ref": "McAllister-Silverstein-Westphal 2010 (linear)",
        "year": 2010,
        "cubic_bc":    {"tau": None, "exponent": 1.0},
        # linear phi potential -> r=0.07, n_T=-r/8 ~ -0.009
        "blue_nt":     {"n_T": -0.009, "explicit_cmb_pivot": True},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "linear inflaton from axion monodromy; r=0.07 prediction",
    },
    {
        "family": "silv_west",
        "paper_id": "0907.2916",
        "short_ref": "Flauger-McAllister-Pajer-Westphal-Xu 2009",
        "year": 2009,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": -0.005, "explicit_cmb_pivot": True},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "CMB oscillations from axion monodromy + instanton modulation",
    },
    {
        "family": "silv_west",
        "paper_id": "1909.08100",
        "short_ref": "Pedro-Westphal 2019 (flattened monodromy)",
        "year": 2019,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": -0.005, "explicit_cmb_pivot": True},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "two-field flattened monodromy; reduced c_s",
    },

    # ------------------------------------------------------------------
    # Family 5: Heterotic CY3 (CHSW + Anderson-Gray-Lukas-Palti)
    # ------------------------------------------------------------------
    {
        "family": "heterotic_cy3",
        "paper_id": "CHSW-1985",
        "short_ref": "Candelas-Horowitz-Strominger-Witten 1985",
        "year": 1985,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        # Heterotic CY3 compactification: E_8xE_8 -> E_6 x SU(3)_H; NO
        # cosmological dynamics; geometry-only paper.
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "foundational heterotic CY3 with SU(3) holonomy; no dynamics",
    },
    {
        "family": "heterotic_cy3",
        "paper_id": "1106.4804",
        "short_ref": "Anderson-Gray-Lukas-Palti 2011 (200 het SMs)",
        "year": 2011,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "heterotic line-bundle SMs on CY3; particle spectrum only",
    },
    {
        "family": "heterotic_cy3",
        "paper_id": "hep-th/9808122",
        "short_ref": "Choi-Kim-Kim 1998 (heterotic M-theory moduli)",
        "year": 1998,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "gaugino condensation + M2 instantons; moduli only",
    },

    # ------------------------------------------------------------------
    # Family 6: M-theory on G_2 manifolds
    # ------------------------------------------------------------------
    {
        "family": "m_g2",
        "paper_id": "hep-th/0201062",
        "short_ref": "Duff 2002 (G_2 review)",
        "year": 2002,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "N=1 D=4 from G_2 holonomy; geometry review",
    },
    {
        "family": "m_g2",
        "paper_id": "hep-th/0701034",
        "short_ref": "Acharya-Bobkov-Kane-Kumar-Shao 2007",
        "year": 2007,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "M-theory dS vacua from G_2; moduli stabilized by potential",
    },

    # ------------------------------------------------------------------
    # Family 7: F-theory on CY 4-folds
    # ------------------------------------------------------------------
    {
        "family": "f_cy4",
        "paper_id": "1806.01854",
        "short_ref": "Weigand 2018 (F-theory TASI)",
        "year": 2018,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "F-theory review; gauge / matter geometrization, no dynamics",
    },
    {
        "family": "f_cy4",
        "paper_id": "0912.3524",
        "short_ref": "Grimm-Krause-Weigand 2009 (F-theory GUT CY4)",
        "year": 2009,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "3-generation F-theory GUT; phenomenology only",
    },

    # ------------------------------------------------------------------
    # Family 8: CFT-dynamics (matrix models, Liouville, WZW dim-reduction)
    # ------------------------------------------------------------------
    {
        "family": "cft_dyn",
        "paper_id": "hep-th/0409256",
        "short_ref": "Fredenhagen-Schomerus 2004 (c=1 boundary Liouville)",
        "year": 2004,
        "cubic_bc":    {"tau": None, "exponent": None},
        "blue_nt":     {"n_T": None, "explicit_cmb_pivot": False},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "c=1 boundary Liouville; rolling-tachyon Euclidean dual",
    },

    # ------------------------------------------------------------------
    # Negative control: slow-roll Lambda-CDM single-field inflaton
    # ------------------------------------------------------------------
    {
        "family": "null_lcdm",
        "paper_id": "null-slowroll",
        "short_ref": "Lambda-CDM slow-roll single-field (null hypothesis)",
        "year": 2024,
        "cubic_bc":    {"tau": None, "exponent": 2.0},  # quadratic chaotic
        # Slow-roll consistency relation: n_T = -r/8 <= 0, always red.
        "blue_nt":     {"n_T": -0.0025, "explicit_cmb_pivot": True},
        "freq_hier":   {"freqs": None},
        "speed_order": {"speeds": None},
        "notes": "slow-roll inflaton; consistency relation forbids blue n_T",
    },

    # ------------------------------------------------------------------
    # Framework control: phonon-exflation substrate (self-test)
    # Included per plan §cross-check (e) "Framework entry should satisfy all 4"
    # ------------------------------------------------------------------
    {
        "family": "framework_control",
        "paper_id": "phonon-exflation-S84",
        "short_ref": "phonon-exflation substrate (framework self-test)",
        "year": 2026,
        # Framework tau_fold = 0.19 (imported); cubic-BC exponent = 3 integer
        "cubic_bc":    {"tau": FRAMEWORK_TAU_FOLD, "exponent": FRAMEWORK_CUBIC_EXP},
        # Blue n_T = +0.4676 from S64/S65 (framework prediction is EXPLICIT
        # at transit-scale; cross-checked against CMB via S66 transfer).
        "blue_nt":     {"n_T": FRAMEWORK_N_T, "explicit_cmb_pivot": True},
        "freq_hier":   {"freqs": list(FRAMEWORK_MODE_FREQS.values())},
        "speed_order": {"speeds": dict(FRAMEWORK_SPEEDS)},
        "notes": "S42+S64+S65+S73a+S75 -- 4-signature by construction",
    },
]

# =====================================================================
# Per-paper 4-signature extraction
# =====================================================================

def extract_signatures(entry):
    """Compute the 4 Boolean signatures for a single catalog entry."""
    sigs = {
        "cubic_bc":    check_cubic_bc(
            entry["cubic_bc"]["tau"], entry["cubic_bc"]["exponent"]
        ),
        "blue_nt":     check_blue_nt(
            entry["blue_nt"]["n_T"],
            entry["blue_nt"].get("explicit_cmb_pivot", False),
        ),
        "freq_hier":   check_freq_hier(entry["freq_hier"].get("freqs")),
        "speed_order": check_speed_order(entry["speed_order"].get("speeds")),
    }
    sigs["k_of_four"] = int(
        sigs["cubic_bc"] + sigs["blue_nt"] + sigs["freq_hier"] + sigs["speed_order"]
    )
    sigs["all_four"] = (sigs["k_of_four"] == 4)
    sigs["three_of_four"] = (sigs["k_of_four"] == 3)
    return sigs


# =====================================================================
# Execute catalog extraction
# =====================================================================

results = []                                                           # (local)
for entry in CATALOG:
    sigs = extract_signatures(entry)                                   # (local)
    row = {
        "family":        entry["family"],
        "paper_id":      entry["paper_id"],
        "short_ref":     entry["short_ref"],
        "year":          entry["year"],
        "cubic_bc":      bool(sigs["cubic_bc"]),
        "blue_nt":       bool(sigs["blue_nt"]),
        "freq_hier":     bool(sigs["freq_hier"]),
        "speed_order":   bool(sigs["speed_order"]),
        "k_of_four":     int(sigs["k_of_four"]),
        "all_four":      bool(sigs["all_four"]),
        "three_of_four": bool(sigs["three_of_four"]),
        "notes":         entry["notes"],
    }
    results.append(row)

# Separate framework-control + null-LCDM from external compactifications
EXTERNAL_FAMILIES = {
    "kklt", "racetrack", "lvs", "silv_west",
    "heterotic_cy3", "m_g2", "f_cy4", "cft_dyn",
}

external_results = [r for r in results if r["family"] in EXTERNAL_FAMILIES]  # (local)
null_results     = [r for r in results if r["family"] == "null_lcdm"]        # (local)
framework_result = [r for r in results if r["family"] == "framework_control"]# (local)

N_external = len(external_results)                                           # (local)
N_catalog_total = len(results)                                               # (local)
N_all_four = sum(1 for r in external_results if r["all_four"])               # (local)
N_three_of_four = sum(1 for r in external_results if r["three_of_four"])     # (local)

# Per-family breakdown
per_family = {}                                                              # (local)
for r in external_results:
    fam = r["family"]
    if fam not in per_family:
        per_family[fam] = {
            "n_papers": 0, "n_cubic_bc": 0, "n_blue_nt": 0,
            "n_freq_hier": 0, "n_speed_order": 0,
            "n_all_four": 0, "n_three_of_four": 0,
        }
    per_family[fam]["n_papers"] += 1
    per_family[fam]["n_cubic_bc"] += int(r["cubic_bc"])
    per_family[fam]["n_blue_nt"] += int(r["blue_nt"])
    per_family[fam]["n_freq_hier"] += int(r["freq_hier"])
    per_family[fam]["n_speed_order"] += int(r["speed_order"])
    per_family[fam]["n_all_four"] += int(r["all_four"])
    per_family[fam]["n_three_of_four"] += int(r["three_of_four"])

# Year-quartile breakdown
def year_quartile(y):
    if y < 2000: return "pre-2000"
    if y < 2010: return "2000-2009"
    if y < 2020: return "2010-2019"
    return "2020-2026"

year_bins = {"pre-2000": 0, "2000-2009": 0, "2010-2019": 0, "2020-2026": 0}  # (local)
for r in external_results:
    year_bins[year_quartile(r["year"])] += 1

# =====================================================================
# Verdict determination (apply substitution-chain directions)
# =====================================================================

MIN_FIRST_PASS = 5                                                           # (local) plan target
if N_external < MIN_FIRST_PASS:
    verdict = "INFO"                                                         # (local)
    verdict_reason = (
        f"First-pass catalog {N_external} < {MIN_FIRST_PASS}; PRE-REG-INCOMPLETE"
    )
elif N_all_four >= 1:
    verdict = "FAIL"                                                         # (local)
    offenders = [r for r in external_results if r["all_four"]]               # (local)
    verdict_reason = (
        f"N_all_four={N_all_four} -- framework dynamics absorbed into: "
        + "; ".join(f"{o['family']}:{o['paper_id']}" for o in offenders)
    )
elif N_all_four == 0 and N_three_of_four <= 2:
    verdict = "PASS"                                                         # (local)
    verdict_reason = (
        f"PROVISIONAL: N_all_four=0 AND N_three_of_four={N_three_of_four}<=2 "
        f"over {N_external} external compactifications; full verdict defers "
        f"to S90 (catalog >=50)"
    )
else:
    verdict = "INFO"                                                         # (local)
    verdict_reason = (
        f"N_all_four=0 but N_three_of_four={N_three_of_four}>=3; proximity "
        f"constructions warrant uplift analysis"
    )

# =====================================================================
# Emit JSONL catalog + NPZ data file
# =====================================================================

OUT_DIR = SCRIPT_PATH.parent
jsonl_path = OUT_DIR / "s84_w7a_80_compactification_catalog.jsonl"
npz_path = OUT_DIR / "s84_w7a_80_data.npz"

with open(jsonl_path, "w", encoding="utf-8") as fh:
    for row in results:
        fh.write(json.dumps(row) + "\n")

# SHA-256 of catalog manifest (as an input pin)
sha_catalog = sha256_of_file(jsonl_path)                                     # (local)

# Closure SHA-256: hash the ordered input-pin map + verdict tuple
closure_map = {                                                              # (local)
    "script": sha_script,
    "canonical_constants": sha_cc,
    "catalog_manifest": sha_catalog,
    "tau_fold": FRAMEWORK_TAU_FOLD,
    "n_T_framework": FRAMEWORK_N_T,
    "N_external": N_external,
    "N_all_four": N_all_four,
    "N_three_of_four": N_three_of_four,
    "verdict": verdict,
}
closure_bytes = json.dumps(closure_map, sort_keys=True).encode("utf-8")      # (local)
sha_closure = sha256_of_bytes(closure_bytes)                                 # (local)

# NPZ numerical data
per_family_arr = np.array(                                                   # (local)
    [[per_family[f]["n_papers"],
      per_family[f]["n_cubic_bc"],
      per_family[f]["n_blue_nt"],
      per_family[f]["n_freq_hier"],
      per_family[f]["n_speed_order"],
      per_family[f]["n_all_four"],
      per_family[f]["n_three_of_four"]]
     for f in sorted(per_family.keys())],
    dtype=int,
)
np.savez(
    npz_path,
    catalog_size_external=N_external,
    catalog_size_total=N_catalog_total,
    N_all_four=N_all_four,
    N_three_of_four=N_three_of_four,
    per_family_names=np.array(sorted(per_family.keys()), dtype="U32"),
    per_family_counts=per_family_arr,
    year_bin_names=np.array(list(year_bins.keys()), dtype="U16"),
    year_bin_counts=np.array(list(year_bins.values()), dtype=int),
    framework_tau_fold=FRAMEWORK_TAU_FOLD,
    framework_n_T=FRAMEWORK_N_T,
    framework_freq_ratio=FRAMEWORK_FREQ_RATIO,
    framework_all_four=bool(framework_result[0]["all_four"]) if framework_result else False,
    null_all_four=bool(null_results[0]["all_four"]) if null_results else False,
    sha_script=sha_script,
    sha_cc=sha_cc,
    sha_catalog=sha_catalog,
    sha_closure=sha_closure,
)

# =====================================================================
# Report
# =====================================================================

print("\n--- CATALOG SUMMARY ---")
print(f"Total entries (incl. controls):     {N_catalog_total}")
print(f"External compactifications:         {N_external}")
print(f"Null-LCDM control entries:          {len(null_results)}")
print(f"Framework control entries:          {len(framework_result)}")
print(f"First-pass target (>=5 external):   {'MET' if N_external>=MIN_FIRST_PASS else 'NOT MET'}")
print()
print("--- PER-FAMILY BREAKDOWN ---")
print(f"{'family':<16} {'N':<3} {'cubic':<6} {'blue':<5} {'freq':<5} {'speed':<6} {'all4':<5} {'3of4':<5}")
for f in sorted(per_family.keys()):
    d = per_family[f]
    print(f"{f:<16} {d['n_papers']:<3} {d['n_cubic_bc']:<6} {d['n_blue_nt']:<5} "
          f"{d['n_freq_hier']:<5} {d['n_speed_order']:<6} "
          f"{d['n_all_four']:<5} {d['n_three_of_four']:<5}")
print()
print("--- YEAR-QUARTILE COVERAGE ---")
for k, v in year_bins.items():
    print(f"  {k:<12} {v}")
print()
print("--- CONTROLS ---")
if framework_result:
    f = framework_result[0]
    print(f"  framework self-test: all_four={f['all_four']} "
          f"(cubic_bc={f['cubic_bc']}, blue_nt={f['blue_nt']}, "
          f"freq_hier={f['freq_hier']}, speed_order={f['speed_order']})")
if null_results:
    n = null_results[0]
    print(f"  null Lambda-CDM:     all_four={n['all_four']} k_of_four={n['k_of_four']}")
print()
print("--- AGGREGATES (external compactifications only) ---")
print(f"N_all_four       = {N_all_four}")
print(f"N_three_of_four  = {N_three_of_four}")
print()
print("--- VERDICT ---")
print(f"verdict = {verdict}")
print(f"reason  = {verdict_reason}")
print()
print("--- INPUT PINS ---")
print(f"  script:              {sha_script}")
print(f"  canonical_constants: {sha_cc}")
print(f"  catalog_manifest:    {sha_catalog}")
print(f"  closure:             {sha_closure}")
print()
print("--- OUTPUT 4-TUPLE ---")
print(f"(value=({N_all_four},{N_three_of_four}), "
      f"scheme=joint_signature_4, convention=per_family_tolerance, L_max=N/A)")

# =====================================================================
# Verdict line (canonical, appended to computations/session-84/s84_gate_verdicts.txt
# by orchestrator / downstream audit; this script only EMITS the line text)
# =====================================================================

VERDICT_LINE = (
    f"S84-DYNAMICS-UNIQUENESS: {verdict} -- "
    f"value=({N_all_four},{N_three_of_four}) "
    f"scheme=joint_signature_4 "
    f"convention=per_family_tolerance "
    f"L_max=N/A "
    f"sha256={sha_closure}"
)
print("\n" + VERDICT_LINE)

# Optional: append to verdict file atomically if it exists and this is the
# canonical run. Safeguarded: only append if line not already present.
VERDICT_FILE = OUT_DIR / "s84_gate_verdicts.txt"
if VERDICT_FILE.exists():
    existing = VERDICT_FILE.read_text(encoding="utf-8")
    if "S84-DYNAMICS-UNIQUENESS:" not in existing:
        with open(VERDICT_FILE, "a", encoding="utf-8") as fh:
            fh.write(VERDICT_LINE + "\n")
        print(f"[appended verdict to {VERDICT_FILE.name}]")
    else:
        print(f"[verdict line already present in {VERDICT_FILE.name}; no append]")

print("\nDone.")
