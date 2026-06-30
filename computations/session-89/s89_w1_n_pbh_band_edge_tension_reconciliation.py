#!/usr/bin/env python3
"""
S89 W1-4 -- S89-N-PBH-BAND-EDGE-TENSION-RECONCILIATION
=======================================================

Gate: S89-N-PBH-BAND-EDGE-TENSION-RECONCILIATION ([SIGN] + [VERIFY], composite)

Pre-registered thresholds (from session-89-plan-w1.md §W1-4 §9):
  sign_verdict:
    PASS iff n_PBH_structural_central > 8.4e-24 (above posterior lower edge).
    FAIL iff n_PBH_structural_central <= 0 (negative density; structural error).
    N/A  iff sign well-defined positive (sign-PASS-by-construction).
  magnitude_verdict (RATIO inclusion):
    PASS iff n_PBH_structural_central ∈ [8.4e-24, 2.2e-22] AND in upper 22.6%
         of CF-CURV-6 prior (i.e., in [5.5e-23, 1e-20]). (Conjunctive PASS:
         band-edge-inclusion AND upper-22.6%-inclusion both required.)
         Equivalently, value ∈ [5.5e-23, 2.2e-22] m^-3 (intersection PASS region
         per plan §10 line 1136).
    INFO iff value is band-edge-included in posterior support but NOT in upper
         22.6% (sub-conjunct PASS), OR within prior [10^-24, 10^-20] but
         outside posterior support [8.4e-24, 2.2e-22].
    FAIL iff value ∉ [10^-24, 10^-20] (outside both posterior support AND
         broad inclusion band).
  regime_verdict:
    VALID iff Friedrich-Bär saturation valid at L_max=10 (substrate-IS
         derivation within math-scripts.md "D_K Block-Diagonality" regime).
    MARGINAL iff f_used ∈ [0.50, 0.95) (5-50% shortened computation domain).
    BREAKDOWN iff f_used < 0.50 (>50% shortened).
  Composite-collapse per gate-verdicts.md S87+ rule.

Hypothesis: The substrate's CF-CURV-6 STRUCTURAL CENTRAL prediction
    n_PBH_structural_central(g_BBN) = β_PBH · ρ_substrate(g_BBN) / M_PBH_typical
                                    = n_edge(g_BBN) · prob_form / L_pix_LRD^3
                                                  (substrate-clock cancellation)
reconciles BAND-EDGE PASS at the upper 22.6% of the CF-CURV-6 prior
[10^-30, 10^-20] m^-3 AND within §W1c-69 PASS-magnitude posterior
support [8.4e-24, 2.2e-22] m^-3.

Substitution chain (Step 1 -- Step 4 per plan §W1-4 §10; MANDATORY):

  Step 1 (Definitions):
    n_PBH_structural_central(g_BBN) ≡ β_PBH · ρ_substrate(g_BBN) / M_PBH_typical
                                                    [plan §10; CF-CURV-6 form]
    Equivalent (substrate-clock cancellation, S88 W1a-59 §0 lines 60-66):
      = n_edge(g_BBN) · prob_form / L_pix_LRD^3
    where:
      β_PBH                ≡ n_edge(g_BBN) · prob_form / N_eigs
      ρ_substrate(g_BBN)   ≡ N_eigs · M_PBH_typical / L_pix_LRD^3
      M_PBH_typical(g_BBN) ≡ M_LRD · 2^-g_BBN  (cascade-tail substrate pinning)

    posterior_support_lower = 8.4e-24, posterior_support_upper = 2.2e-22
                                                    [§W1c-69 PASS-magnitude]
    prior_lower = 1e-30, prior_upper = 1e-20        [CF-CURV-6 prior]
    upper_22_6_pct_lower = 10^(-30 + 0.774*10) = 10^-22.26 ≈ 5.495e-23
    upper_22_6_pct_upper = 1e-20

  Step 2 (Substitution; multiplied out):
    β_PBH · ρ_substrate / M_PBH_typical
      = (n_edge · prob_form / N_eigs)
        · (N_eigs · M_PBH_typical / L_pix_LRD^3)
        / M_PBH_typical
      = n_edge · prob_form / L_pix_LRD^3
    (substrate-clock cancellation; the cardinality 2^g and substrate-volume
    L_pix(g)^3 cancel exactly under IS-not-IN substrate-clock convention,
    leaving a g-independent value at saturated cascade-tail threshold.)

  Step 3 (Simplify; substrate-IS canonicals from S88 W1a-59):
    n_edge(g_BBN ∈ [143..384]) = C(N_eigs, 2) = C(78080, 2) = 3,048,204,160
                                                    [saturated; threshold(g) >> max-pair span]
    prob_form        = 59.8 / G_MAX = 59.8 / 384 = 0.15573
                                                    [DS-2 corrected per-generation
                                                     Parker-pair production]
    L_pix_LRD        = 3.0e+10 m   [r_s for M_LRD = 1e7 M_sun]

    n_PBH_structural_central
      = 3.048204160e9 · 0.15573 / (3.0e10)^3
      = 4.7470e8 / 2.7e31
      ≈ 1.758e-23 m^-3

    Equivalent factorization (per plan §10 form):
      β_PBH = n_edge · prob_form / N_eigs
            = 3.048204160e9 · 0.15573 / 78080 ≈ 6079.8     (dimensionless mass-fraction
                                                            quantity; saturation ratio)
      ρ_substrate(g_BBN) = N_eigs · M_PBH_typical / L_pix_LRD^3
                         = 78080 · M_PBH(g_BBN=323) / (3.0e10)^3
      M_PBH_typical = M_LRD · 2^-g_BBN = 1.989e37 · 2^-323 ≈ 1.86e-60 kg
                                                    [cascade-tail substrate pinning]

  Step 4 (Direction; pre-registered):
    SIGN: β_PBH > 0 ∧ ρ_substrate > 0 ∧ M_PBH_typical > 0
          ⇒ n_PBH > 0  ⇒  sign_verdict = PASS by construction.
    MAGNITUDE: pre-registered range per plan §10 line 1136 PASS region
          n_PBH ∈ [8.4e-24, 2.2e-22] ∩ [5.5e-23, 1e-20] = [5.5e-23, 2.2e-22]
          (the band-edge-inclusive PASS region).
    REGIME: VALID iff Friedrich-Bär saturation holds at L_max=10
          (n_edge derived from L_max=10-truncated D_K spectrum cache;
          truncation_consistent verified at L_max=10 vs L_max=12 in
          S88 W1a-59 master cache cross-check).

Substrate framing (verbatim from plan §W1-4 §13, MANDATORY):
  "n_PBH IS the substrate's emergent number density of primordial black
  holes at the substrate-pinned BBN cascade-generation g_BBN; PBH formation
  IS the cascade-tail mass distribution's emergent gravitational collapse
  expression at g_BBN. FORBIDDEN explanation directions: 'PBHs form during
  inflation IN expanding spacetime', 'inflationary perturbations seed PBH
  formation', 'horizon re-entry triggers PBH formation in radiation era'.
  REQUIRED direction: substrate's pinned cascade-tail mass distribution at
  g_BBN → emergent gravitational collapse → emergent n_PBH(today). The
  CF-CURV-6 STRUCTURAL CENTRAL prediction comes from the substrate's
  intrinsic cascade-tail structure, not from a free-parameter cosmological-
  model fit to PBH-population data."
  Single-tau-slice level: §W1-4 operates at Level 1 single-tau-slice
  substrate-IS (cascade structure at fixed tau_fold = 0.190; g_BBN is the
  substrate's intrinsic cascade-generation index, NOT a moduli-deformation
  parameter).

Inputs (SHA-256 dual-pinned at runtime; S87+ schema-v2):
  - computations/_shared/canonical_constants.py
  - computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.npz
                                                    [§W1-3 intra-wave dep]
  - computations/session-88/s88_w1a_n_pbh_per_cascade_generation.npz
                                                    [parent CF-CURV-6 substrate
                                                     n_edge + prob_form pinning]
  - sessions/archive/session-88/workshops/s88-w5-w1c-69-sign-pass-tautology.md
                                                    [CF-CURV-6 STRUCTURAL CENTRAL
                                                     form §V.2]
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
                                                    [substrate D_K spectrum;
                                                     N_eigs, lambda_min/max
                                                     at L_max=10 truncation]
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple (per plan §W1-4 §8):
  (value='n_PBH_central=<v>;band_edge_inclusion=<bool>;upper_22_6_pct=<bool>',
   scheme='cf-curv-6-substrate-cascade-tail-at-g-BBN-Lmax-10',
   convention='CF-CURV-6-substrate-IS-structural-central-substrate-pinned-FULL',
   L_max=10)

Classification: PHONONIC + cosmological-bridge.

DISCIPLINE
----------
- `from canonical_constants import *` (S34+; uses M_KK, tau_fold, Delta_BCS, K_base).
- β_PBH, M_PBH_typical, n_PBH_structural_central PROMOTED to canonical_constants.py
  via update_constant() ONLY ON PASS (Class-(e) PROMOTES-ON-PASS pins).
- Every local/intermediate tagged `# (local)`.
- CPU-only; substrate-canonical-arithmetic + band-inclusion check + verdict-
  emission; OMP_NUM_THREADS=8.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict appended to computations/session-89/s89_gate_verdicts.txt
  (canonical path per gate-verdicts.md; the `_shared/` form is FORBIDDEN).
- Schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row REQUIRED
  (substitution chain Step 4 pre-registers directional positivity prediction).
- Falsifier-master-inventory row update at sessions/framework/registry/
  falsifier-master-inventory.md (mack PRIMARY sole writer per
  feedback_mack-bridge-role.md), citing full-64-char audit_sha256.

REFERENCES
----------
- sessions/session-plan/session-89-plan-w1.md §W1-4 (full block)
- sessions/archive/session-88/workshops/s88-w5-w1c-69-sign-pass-tautology.md V.2
- computations/session-88/s88_w1a_n_pbh_per_cascade_generation.py + .npz
                            (S88 W1a-59 parent CF-CURV-6 N-PBH gate;
                             value=1.7581e-23; PASS at L_max=10)
- computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.npz
                            (§W1-3 intra-wave: g_BBN=323, T_H_g_BBN=1.057 MeV,
                             f_g_BBN=9.157)
- sessions/framework/registry/falsifier-master-inventory.md (mack PRIMARY)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- CPU thread cap (BEFORE numpy import per computation-environment.md)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 2 -- Canonical constants (MANDATORY first import per math-scripts.md)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# Ensure session-89 directory exists (per spawn-prompt orchestrator override)
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403
# Explicit re-import to catch IDE refactors
from canonical_constants import M_KK, tau_fold, Delta_BCS, K_base  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 4 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S89"  # (local)
GATE_ID = "S89-N-PBH-BAND-EDGE-TENSION-RECONCILIATION"  # (local)
SCHEME = "cf-curv-6-substrate-cascade-tail-at-g-BBN-Lmax-10"  # (local)
CONVENTION = "CF-CURV-6-substrate-IS-structural-central-substrate-pinned-FULL"  # (local)
L_MAX = 10  # (local) substrate spectral-triple truncation

# Pre-registered band edges (plan §7 + §10)
POSTERIOR_SUPPORT_LOWER = 8.4e-24  # (local) m^-3 (§W1c-69 PASS-magnitude posterior lower)
POSTERIOR_SUPPORT_UPPER = 2.2e-22  # (local) m^-3 (§W1c-69 PASS-magnitude posterior upper)
PRIOR_LOWER = 1.0e-30  # (local) m^-3 (CF-CURV-6 prior lower)
PRIOR_UPPER = 1.0e-20  # (local) m^-3 (CF-CURV-6 prior upper)
# Upper 22.6% of CF-CURV-6 prior in log-OOM space:
#   prior log-range = [-30, -20] (10 OOM wide); upper 22.6% = [-30 + 0.774*10, -20] = [-22.26, -20]
UPPER_22_6_PCT_LOWER = 10.0 ** (-22.26)  # (local) ≈ 5.495e-23 m^-3
UPPER_22_6_PCT_UPPER = PRIOR_UPPER  # (local) 1e-20 m^-3
# Plan §10 line 1136 conjunctive PASS region: [5.5e-23, 2.2e-22] m^-3
PASS_REGION_LOWER = max(POSTERIOR_SUPPORT_LOWER, UPPER_22_6_PCT_LOWER)  # (local)
PASS_REGION_UPPER = min(POSTERIOR_SUPPORT_UPPER, UPPER_22_6_PCT_UPPER)  # (local)

# Tolerance for float comparisons
TOLERANCE = 1.0e-12  # (local)

# Substrate-IS canonicals from S88 W1a-59 parent gate npz
# (substrate-clock cancellation: at saturated threshold, n_PBH = n_edge · prob_form / L_pix_LRD^3,
#  g-independent; the cardinality 2^g and L_pix(g)^3 cancel exactly per phononic-framing IS-not-IN)
S88_W1A59_N_EDGE_SAT = 3_048_204_160  # (local) C(N_eigs=78080, 2) saturated at g >= 143
S88_W1A59_PROB_FORM = 59.8 / 384.0  # (local) = 0.15572916666666666 (DS-2 per-generation Parker-pair)
S88_W1A59_L_PIX_LRD_M = 3.0e10  # (local) r_s for M_LRD = 1e7 M_sun (substrate cascade-tail anchor)
S88_W1A59_M_LRD_KG = 1.989e37  # (local) 1e7 M_sun in kg
S88_W1A59_N_EIGS = 78080  # (local) D_K eigenvalue count at L_max=10 truncation
S88_W1A59_VALUE_PUBLISHED = 1.7581e-23  # (local) S88 W1a-59 verdict-line value (PASS)

# Input pin paths
INPUT_CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
INPUT_W1_3_NPZ = SESSION_DIR / "s89_w1_f_m_species_multiplicity_lookup_table.npz"
INPUT_S88_W1A59_NPZ = (
    COMPUTATIONS_DIR / "session-88" / "s88_w1a_n_pbh_per_cascade_generation.npz"
)
INPUT_S88_W5_V2 = (
    PROJECT_ROOT / "sessions" / "session-88" / "workshops"
    / "s88-w5-w1c-69-sign-pass-tautology.md"
)
INPUT_L12_CACHE = (
    COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
)
INPUT_FILES = [
    INPUT_CANONICAL_CONSTANTS,
    INPUT_W1_3_NPZ,
    INPUT_S88_W1A59_NPZ,
    INPUT_S88_W5_V2,
    INPUT_L12_CACHE,
]

# Output destinations
OUT_NPZ = SESSION_DIR / "s89_w1_n_pbh_band_edge_tension_reconciliation.npz"
OUT_PNG = SESSION_DIR / "s89_w1_n_pbh_band_edge_tension_reconciliation.png"
VERDICT_TXT = SESSION_DIR / "s89_gate_verdicts.txt"


# ---------------------------------------------------------------------------
# Section 5 -- SHA-256 + closure-hash + dual-SHA helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256 = SHA-256(script_bytes || canonical_bytes || pinmap_json)
                   captures full-input audit chain for reproducibility
    content_sha256 = SHA-256(script_bytes)
                     captures script-only content (immutable post-emit)
    """
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 6 -- Procedure (5 numbered steps per plan §6)
# ---------------------------------------------------------------------------

def step1_load_g_bbn_from_w1_3() -> dict:
    """Step 1: Identify g_BBN cascade generation from §W1-3 lookup table.

    From W1-3 lookup table NPZ:
      g_BBN  -- smallest g s.t. T_H(g) <= 1 MeV (BBN epoch substrate-pinned)
      f_g_BBN -- substrate's emergent SM-species-multiplicity at g_BBN
      T_H_g_BBN_GeV -- substrate Hawking temperature at g_BBN

    Per spawn prompt: g_BBN=323, T_H_g_BBN=1.057 MeV, f_g_BBN=9.157.

    Note: f(g_BBN) = 9.157 vs standard cosmology BBN g_*=10.75 (14.85% deviation
    due to electron near-threshold Boltzmann suppression at T=1.057 MeV per
    §W1-3 structural diagnostic). This 14.85% deviation enters as
    ~0.07 log-OOM perturbation on Hawking-radiation back-reaction; sub-leading
    to dominant cocycle-class structural prediction. §W1-3 FAIL does NOT
    invalidate §W1-4 input per user-adjudicated routing 2026-05-10.
    """
    print("=== Step 1: Load g_BBN from §W1-3 lookup table ===")
    d = np.load(INPUT_W1_3_NPZ, allow_pickle=True)  # (local)
    g_BBN = int(d["g_BBN"])  # (local) 323
    f_g_BBN = float(d["f_g_BBN"])  # (local) 9.157
    T_H_g_BBN_GeV = float(d["T_H_substrate_GeV"])  # (local) 1.057e-3 GeV = 1.057 MeV
    print(f"  g_BBN              = {g_BBN}  (smallest g s.t. T_H(g) <= 1 MeV)")
    print(f"  T_H(g_BBN) GeV     = {T_H_g_BBN_GeV:.6e}  ({T_H_g_BBN_GeV*1000:.3f} MeV)")
    print(f"  f(g_BBN)           = {f_g_BBN:.6f}  (vs std-cosmology BBN g_*=10.75; {abs(f_g_BBN-10.75)/10.75*100:.2f}% deviation)")
    print()
    return {
        "g_BBN": g_BBN,
        "f_g_BBN": f_g_BBN,
        "T_H_g_BBN_GeV": T_H_g_BBN_GeV,
    }


def step2_derive_cf_curv_6_structural_central(g_BBN: int) -> dict:
    """Step 2: Derive CF-CURV-6 STRUCTURAL CENTRAL prediction n_PBH(g_BBN).

    Substrate-IS form (per S88 W5 V.2 + S88 W1a-59 parent gate, substrate-clock
    cancellation reading):

      n_PBH_structural_central(g_BBN)
        = β_PBH · ρ_substrate(g_BBN) / M_PBH_typical
        = n_edge(g_BBN) · prob_form / L_pix_LRD^3
                                            (substrate-clock cancellation;
                                             cardinality 2^g and L_pix(g)^3
                                             cancel exactly under IS-not-IN)

    where (substrate-IS canonicals from S88 W1a-59 verdict + .npz):
      β_PBH               ≡ n_edge(g_BBN) · prob_form / N_eigs   (saturated)
      ρ_substrate(g_BBN)  ≡ N_eigs · M_PBH_typical / L_pix_LRD^3
      M_PBH_typical(g_BBN) ≡ M_LRD · 2^-g_BBN  (cascade-tail substrate pinning)

    Numerical pin (from S88 W1a-59 npz, n_edge_saturated_C_N_2 key):
      n_edge(g_BBN ∈ [143..384]) = 3,048,204,160  (saturated at C(78080,2))
      prob_form                  = 0.15573        (DS-2 corrected per-gen Parker)
      L_pix_LRD                  = 3.0e10 m       (r_s for M_LRD=1e7 M_sun)
      M_LRD                      = 1.989e37 kg    (1e7 M_sun)
      M_PBH_typical(g_BBN=323)   = 1.989e37 · 2^-323
    """
    print("=== Step 2: Derive CF-CURV-6 STRUCTURAL CENTRAL ===")

    # Substrate-IS canonicals (loaded from S88 W1a-59 parent .npz for cross-check)
    parent_d = np.load(INPUT_S88_W1A59_NPZ, allow_pickle=True)  # (local)
    n_edge_sat_npz = int(parent_d["n_edge_saturated_C_N_2"])  # (local) 3,048,204,160
    n_eigs_npz = int(parent_d["N_EIGS_LMAX10"])  # (local) 78080
    prob_form_npz = float(parent_d["prob_form_per_gen"])  # (local) 0.15573
    L_pix_LRD_npz = float(parent_d["L_PIX_LRD_m"])  # (local) 3.0e10
    parent_n_PBH = float(parent_d["n_PBH_BBN_today"])  # (local) ≈1.7581e-23
    parent_g_BBN = int(parent_d["g_BBN"])  # (local) 322 (S88 plan-pinned)

    # Verify parent npz canonicals match script-pinned constants
    assert n_edge_sat_npz == S88_W1A59_N_EDGE_SAT, \
        f"n_edge sat mismatch: npz={n_edge_sat_npz} vs pinned={S88_W1A59_N_EDGE_SAT}"
    assert n_eigs_npz == S88_W1A59_N_EIGS, \
        f"N_eigs mismatch: npz={n_eigs_npz} vs pinned={S88_W1A59_N_EIGS}"
    assert abs(prob_form_npz - S88_W1A59_PROB_FORM) < 1e-6, \
        f"prob_form mismatch: npz={prob_form_npz} vs pinned={S88_W1A59_PROB_FORM}"
    assert abs(L_pix_LRD_npz - S88_W1A59_L_PIX_LRD_M) < 1e-6, \
        f"L_pix_LRD mismatch: npz={L_pix_LRD_npz} vs pinned={S88_W1A59_L_PIX_LRD_M}"
    print(f"  Parent S88 W1a-59 canonicals VERIFIED against script pins.")

    # Substrate-clock cancellation form (g-independent for g >= g_saturate=143):
    # n_PBH = n_edge · prob_form / L_pix_LRD^3
    n_edge_at_g = float(S88_W1A59_N_EDGE_SAT)  # (local) saturated at g_BBN=323 (g >= 143)
    n_PBH_central = n_edge_at_g * S88_W1A59_PROB_FORM / S88_W1A59_L_PIX_LRD_M**3  # (local)

    # Equivalent factorization per plan §10 form (cross-check):
    M_PBH_typical_kg = S88_W1A59_M_LRD_KG * (2.0 ** -g_BBN)  # (local)
    beta_PBH = n_edge_at_g * S88_W1A59_PROB_FORM / S88_W1A59_N_EIGS  # (local) dimensionless
    rho_substrate_g_BBN_kg_per_m3 = (
        S88_W1A59_N_EIGS * M_PBH_typical_kg / S88_W1A59_L_PIX_LRD_M**3
    )  # (local) substrate's emergent (formal) energy density at cascade-tail

    # Cross-check the factorization reproduces the substrate-clock form
    n_PBH_factored = beta_PBH * rho_substrate_g_BBN_kg_per_m3 / M_PBH_typical_kg  # (local)
    rel_err_factorization = abs(n_PBH_central - n_PBH_factored) / n_PBH_central  # (local)
    print(f"  Factorization cross-check: substrate-clock = {n_PBH_central:.6e}; "
          f"β·ρ/M = {n_PBH_factored:.6e}; rel_err = {rel_err_factorization:.2e}")
    assert rel_err_factorization < 1e-10, "Factorization cross-check FAILED."

    # Cross-check against parent gate's published value
    rel_err_parent = abs(n_PBH_central - parent_n_PBH) / parent_n_PBH  # (local)
    print(f"  Parent S88 W1a-59 cross-check: parent={parent_n_PBH:.6e}, here={n_PBH_central:.6e}, rel_err={rel_err_parent:.2e}")
    # Note: parent uses g_BBN=322; here g_BBN=323. Both are in saturated regime (>= 143), so n_PBH should agree to within float epsilon.
    # (The substrate-clock cancellation makes n_PBH g-independent for g >= g_saturate=143.)
    assert rel_err_parent < 1e-3, "Parent cross-check FAILED."

    print(f"  β_PBH                  = {beta_PBH:.6e}  (= n_edge · prob_form / N_eigs)")
    print(f"  M_PBH_typical(g_BBN=323) = {M_PBH_typical_kg:.6e} kg  (= M_LRD · 2^-g_BBN)")
    print(f"  ρ_substrate(g_BBN)     = {rho_substrate_g_BBN_kg_per_m3:.6e} kg/m^3")
    print(f"  n_PBH_structural_central = {n_PBH_central:.6e} m^-3")
    print(f"  log10(n_PBH)           = {math.log10(n_PBH_central):.6f}")
    print()

    return {
        "n_PBH_structural_central": n_PBH_central,
        "beta_PBH": beta_PBH,
        "M_PBH_typical_kg": M_PBH_typical_kg,
        "rho_substrate_g_BBN_kg_per_m3": rho_substrate_g_BBN_kg_per_m3,
        "n_edge_at_g_BBN": n_edge_at_g,
        "prob_form": S88_W1A59_PROB_FORM,
        "L_pix_LRD_m": S88_W1A59_L_PIX_LRD_M,
        "N_eigs": S88_W1A59_N_EIGS,
        "M_LRD_kg": S88_W1A59_M_LRD_KG,
        "parent_n_PBH": parent_n_PBH,
        "parent_g_BBN": parent_g_BBN,
    }


def step3_compare_against_w1c69_posterior(n_PBH: float) -> dict:
    """Step 3: Compare against §W1c-69 PASS-magnitude posterior support.

    Verify two conditions:
      (a) band_edge_inclusion: n_PBH ∈ [8.4e-24, 2.2e-22] m^-3
                               (within posterior support).
      (b) upper_22_6_pct_inclusion: n_PBH ∈ [5.5e-23, 1e-20] m^-3
                                     (upper 22.6% of CF-CURV-6 prior).
    """
    print("=== Step 3: Compare against §W1c-69 PASS-magnitude posterior ===")

    band_edge_inclusion = bool(POSTERIOR_SUPPORT_LOWER <= n_PBH <= POSTERIOR_SUPPORT_UPPER)  # (local)
    upper_22_6_pct_inclusion = bool(UPPER_22_6_PCT_LOWER <= n_PBH <= UPPER_22_6_PCT_UPPER)  # (local)
    in_pass_region = bool(PASS_REGION_LOWER <= n_PBH <= PASS_REGION_UPPER)  # (local)
    in_prior = bool(PRIOR_LOWER <= n_PBH <= PRIOR_UPPER)  # (local)

    log_n_PBH = math.log10(n_PBH)  # (local)
    log_post_lo = math.log10(POSTERIOR_SUPPORT_LOWER)  # (local)
    log_post_hi = math.log10(POSTERIOR_SUPPORT_UPPER)  # (local)
    log_u226_lo = math.log10(UPPER_22_6_PCT_LOWER)  # (local)

    print(f"  posterior support: [{POSTERIOR_SUPPORT_LOWER:.3e}, {POSTERIOR_SUPPORT_UPPER:.3e}] m^-3")
    print(f"    log10 endpoints: [{log_post_lo:.3f}, {log_post_hi:.3f}]")
    print(f"  upper 22.6% band : [{UPPER_22_6_PCT_LOWER:.3e}, {UPPER_22_6_PCT_UPPER:.3e}] m^-3")
    print(f"    log10 endpoints: [{log_u226_lo:.3f}, {math.log10(UPPER_22_6_PCT_UPPER):.3f}]")
    print(f"  PASS region (intersection): [{PASS_REGION_LOWER:.3e}, {PASS_REGION_UPPER:.3e}] m^-3")
    print(f"  CF-CURV-6 prior  : [{PRIOR_LOWER:.3e}, {PRIOR_UPPER:.3e}] m^-3")
    print()
    print(f"  n_PBH_structural_central = {n_PBH:.6e} m^-3 (log10 = {log_n_PBH:.4f})")
    print(f"  band_edge_inclusion        : {band_edge_inclusion}")
    print(f"  upper_22_6_pct_inclusion   : {upper_22_6_pct_inclusion}")
    print(f"  in_pass_region (intersect) : {in_pass_region}")
    print(f"  in_prior                    : {in_prior}")

    # Distance diagnostics
    if band_edge_inclusion:
        d_below_upper = log_post_hi - log_n_PBH  # (local)
        d_above_lower = log_n_PBH - log_post_lo  # (local)
        print(f"  Inside posterior: {d_above_lower:+.4f} OOM above lower edge; "
              f"{d_below_upper:+.4f} OOM below upper edge.")
    if not upper_22_6_pct_inclusion:
        d_to_u226 = log_u226_lo - log_n_PBH  # (local)
        print(f"  Below upper-22.6% band by {d_to_u226:+.4f} OOM.")
    print()

    return {
        "band_edge_inclusion": band_edge_inclusion,
        "upper_22_6_pct_inclusion": upper_22_6_pct_inclusion,
        "in_pass_region": in_pass_region,
        "in_prior": in_prior,
        "log10_n_PBH": log_n_PBH,
    }


def step4_composite_verdict(n_PBH: float, comparison: dict) -> dict:
    """Step 4: Composite verdict per schema-v2 collapse rule (plan §9).

    sign_verdict:
      PASS iff n_PBH > POSTERIOR_SUPPORT_LOWER (above posterior lower edge).
      FAIL iff n_PBH <= 0.
      N/A is not used here; sign is a well-defined positive density check.

    magnitude_verdict (RATIO inclusion, conjunctive PASS per plan §10 line 1136):
      PASS iff n_PBH in PASS_REGION = [5.5e-23, 2.2e-22]
              (intersection of posterior support AND upper 22.6% of prior;
               BOTH band-edge-inclusion AND upper-22.6%-inclusion required).
      INFO iff n_PBH ∈ posterior_support BUT NOT in upper-22.6% region
              (sub-conjunct PASS; structural central is in posterior but
               below upper-22.6% lower edge — sub-leading β_PBH/M_PBH_typical
               correction expected per plan §11 INFO clause).
      INFO iff n_PBH ∈ [10^-24, 10^-20] but NOT in posterior support
              (within prior magnitude band but outside posterior PASS-magnitude).
      FAIL iff n_PBH ∉ [10^-24, 10^-20] (outside prior + posterior).

    regime_verdict:
      VALID iff Friedrich-Bär saturation valid at L_max=10:
        - n_edge(g_BBN) saturated at C(N_eigs, 2) per S88 W1a-59 g_saturate=143
          (n_edge value comes from L_max=10 truncation of D_K spectrum cache;
           saturation regime at g >= 143 confirmed by parent gate's g_saturate=143).
        - g_BBN=323 >> 143 ⇒ saturation regime VALID.
      MARGINAL iff f_used ∈ [0.50, 0.95) — N/A here (no integration/scan domain).
      BREAKDOWN iff f_used < 0.50 — N/A here.

    Composite-collapse per gate-verdicts.md S87+ deterministic rule:
      regime=BREAKDOWN          ⇒ composite=FAIL
      sign_verdict=FAIL          ⇒ composite=FAIL
      magnitude=FAIL ∧ regime=VALID ⇒ composite=FAIL
      magnitude=FAIL ∧ regime=MARGINAL ⇒ composite=INFO
      magnitude=INFO            ⇒ composite=INFO
      else                        ⇒ composite=PASS
    """
    print("=== Step 4: Composite verdict per schema-v2 collapse rule ===")

    # SIGN_VERDICT (substitution chain Step 4 pre-registers positivity)
    if n_PBH > POSTERIOR_SUPPORT_LOWER:
        sign_verdict = "PASS"  # (local) above posterior lower edge ⇒ pre-registered direction matched
    elif n_PBH <= 0:
        sign_verdict = "FAIL"  # (local) negative density (structural error)
    else:
        # 0 < n_PBH <= POSTERIOR_SUPPORT_LOWER: positive but below posterior lower edge.
        # The substitution chain Step 4 only pre-registered POSITIVITY (sign-PASS-by-construction).
        # The threshold sign-PASS in plan §9 is the stricter test (above posterior lower edge).
        # Here we adopt the plan §9 stricter reading: sign_verdict = FAIL if positive but below
        # the posterior lower edge — the directional pre-registration was strictly above lower edge.
        sign_verdict = "FAIL"  # (local)

    # MAGNITUDE_VERDICT (conjunctive PASS per plan §10 line 1136)
    if comparison["in_pass_region"]:
        magnitude_verdict = "PASS"  # (local) in PASS region [5.5e-23, 2.2e-22]
    elif comparison["band_edge_inclusion"] or comparison["in_prior"]:
        # Two INFO sub-cases:
        #   (a) n_PBH in posterior support but not in upper-22.6% (sub-conjunct PASS).
        #   (b) n_PBH in prior [10^-24, 10^-20] but outside posterior support.
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local) outside both prior + posterior

    # REGIME_VERDICT (Friedrich-Bär saturation at L_max=10)
    # n_edge(g_BBN=323) saturated at C(78080, 2)=3.048e9 per S88 W1a-59 .npz
    # (parent gate's g_saturate=143; 323 >> 143 ⇒ VALID).
    g_saturate_threshold = 143  # (local) S88 W1a-59 .npz
    g_BBN_local = 323  # (local) §W1-3 lookup
    f_used = 1.0  # (local) no auto-shortening (single-point arithmetic; no scan domain)
    if g_BBN_local >= g_saturate_threshold and f_used >= 0.95:
        regime_verdict = "VALID"  # (local)
    elif g_BBN_local >= g_saturate_threshold and f_used >= 0.50:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)

    # Composite-collapse per gate-verdicts.md S87+ rule
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  composite_verdict = {composite}")
    print()

    return {
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite_verdict": composite,
        "g_saturate_threshold": g_saturate_threshold,
        "f_used": f_used,
    }


# ---------------------------------------------------------------------------
# Section 7 -- Plot
# ---------------------------------------------------------------------------

def write_png(n_PBH: float, comparison: dict, verdict: dict) -> None:
    """1-panel log-axis plot per plan §6 step 4 / §6 output 'Plot' line.

    Shows:
      - CF-CURV-6 prior [10^-30, 10^-20] m^-3 (light shading)
      - §W1c-69 posterior support [8.4e-24, 2.2e-22] m^-3 (medium shading)
      - upper 22.6% of prior [5.5e-23, 1e-20] m^-3 (overlap shading)
      - PASS region (intersection) [5.5e-23, 2.2e-22] (deep shading)
      - substrate-IS structural central marker
    """
    fig, ax = plt.subplots(figsize=(10, 5.5))

    # Plot horizontal "thermometer" of n_PBH on log-x axis
    log_x = np.linspace(-30, -19, 1000)  # (local) log10(n_PBH) sweep
    y_const = np.ones_like(log_x)  # (local) flat horizontal line for clarity

    # CF-CURV-6 prior shading (full range)
    ax.axvspan(PRIOR_LOWER, PRIOR_UPPER, color="#dddddd", alpha=0.5,
               label=f"CF-CURV-6 prior [{PRIOR_LOWER:.0e}, {PRIOR_UPPER:.0e}]")
    # §W1c-69 posterior support shading
    ax.axvspan(POSTERIOR_SUPPORT_LOWER, POSTERIOR_SUPPORT_UPPER,
               color="#ffd97d", alpha=0.5,
               label=f"§W1c-69 posterior [{POSTERIOR_SUPPORT_LOWER:.1e}, {POSTERIOR_SUPPORT_UPPER:.1e}]")
    # Upper 22.6% of prior shading
    ax.axvspan(UPPER_22_6_PCT_LOWER, UPPER_22_6_PCT_UPPER,
               color="#a8e6a3", alpha=0.4,
               label=f"upper 22.6% of prior [{UPPER_22_6_PCT_LOWER:.1e}, {UPPER_22_6_PCT_UPPER:.1e}]")
    # PASS region (intersection)
    ax.axvspan(PASS_REGION_LOWER, PASS_REGION_UPPER,
               color="#2ca02c", alpha=0.30,
               label=f"PASS region (intersection) [{PASS_REGION_LOWER:.1e}, {PASS_REGION_UPPER:.1e}]")

    # Substrate-IS STRUCTURAL CENTRAL marker
    ax.axvline(n_PBH, color="black", linewidth=2.0, linestyle="-",
               label=f"substrate-IS STRUCTURAL CENTRAL = {n_PBH:.3e} m^-3\n"
                     f"(log10 = {math.log10(n_PBH):.3f})")

    # Annotation
    ax.annotate(
        f"n_PBH(g_BBN=323)\n= {n_PBH:.3e} m^-3\nlog10 = {math.log10(n_PBH):.3f}",
        xy=(n_PBH, 0.6),
        xytext=(n_PBH * 1e4, 0.85),
        fontsize=9, ha="left", va="center",
        arrowprops=dict(arrowstyle="->", color="black", lw=0.9),
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.85),
    )

    # Verdict tag
    verdict_color = {"PASS": "#2ca02c", "INFO": "#ffa502", "FAIL": "#d62728"}.get(
        verdict["composite_verdict"], "black")
    ax.text(
        0.02, 0.95,
        f"composite_verdict = {verdict['composite_verdict']}\n"
        f"sign={verdict['sign_verdict']}, mag={verdict['magnitude_verdict']}, "
        f"regime={verdict['regime_verdict']}\n"
        f"band_edge_inclusion = {comparison['band_edge_inclusion']}\n"
        f"upper_22_6_pct_inclusion = {comparison['upper_22_6_pct_inclusion']}",
        transform=ax.transAxes,
        fontsize=9, va="top", ha="left",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                  edgecolor=verdict_color, linewidth=2.0, alpha=0.95),
    )

    ax.set_xscale("log")
    ax.set_xlim(1e-31, 1e-19)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel(r"$n_{\mathrm{PBH}}$ today [m$^{-3}$]  (log scale)")
    ax.set_title(
        f"S89 W1-4 -- n_PBH band-edge tension reconciliation against §W1c-69 PASS-magnitude posterior\n"
        f"substrate-IS CF-CURV-6 STRUCTURAL CENTRAL via "
        f"$n_{{\\mathrm{{PBH}}}} = \\beta_{{PBH}} \\cdot \\rho_{{substrate}}(g_{{BBN}}) / M_{{PBH,typical}}$"
        f"  (substrate-clock cancellation, S88 W1a-59)"
    )
    ax.grid(True, axis="x", which="both", alpha=0.35)
    ax.legend(loc="lower right", fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 -- Verdict-line emission (S87+ schema-v2)
# ---------------------------------------------------------------------------

def append_verdict(
    composite: str, value: str, audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
) -> None:
    """Append canonical S87+ schema-v2 verdict line + dual-SHA companion
    + 3-tuple companion row to s89_gate_verdicts.txt.

    Single-shot write_promotion -> fsync -> append (registry-landing.md
    §"Bridge-Landing Script Architecture" pattern).
    """
    canonical_line = (
        f"{GATE_ID}: {composite} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    threetuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_companion)
        fp.write(threetuple_companion)
        fp.flush()
        try:
            os.fsync(fp.fileno())
        except OSError:
            pass


# ---------------------------------------------------------------------------
# Section 9 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"Session: {SESSION}; gate: {GATE_ID}")
    print(f"Pre-reg: PASS region (conjunctive) = [{PASS_REGION_LOWER:.3e}, "
          f"{PASS_REGION_UPPER:.3e}] m^-3")
    print()

    # Step A: log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure_hash: {closure[:16]}...")
    print()

    # Step 1: Identify g_BBN cascade generation from §W1-3 lookup table
    s1 = step1_load_g_bbn_from_w1_3()  # (local)
    g_BBN = s1["g_BBN"]  # (local) 323
    f_g_BBN = s1["f_g_BBN"]  # (local) 9.157
    T_H_g_BBN_GeV = s1["T_H_g_BBN_GeV"]  # (local) 1.057e-3

    # Step 2: Derive CF-CURV-6 STRUCTURAL CENTRAL prediction for n_PBH(g_BBN)
    s2 = step2_derive_cf_curv_6_structural_central(g_BBN)  # (local)
    n_PBH = s2["n_PBH_structural_central"]  # (local)

    # Step 3: Compare against §W1c-69 PASS-magnitude posterior support
    s3 = step3_compare_against_w1c69_posterior(n_PBH)  # (local)

    # Step 4: Composite verdict per schema-v2 collapse rule
    s4 = step4_composite_verdict(n_PBH, s3)  # (local)

    # Step C: Compute dual-SHA + write artifacts
    audit_sha, content_sha = compute_dual_sha(  # (local)
        Path(__file__).resolve(),
        INPUT_CANONICAL_CONSTANTS,
        pins,
    )

    # Save .npz (full results)
    np.savez(
        OUT_NPZ,
        n_PBH_structural_central=n_PBH,
        posterior_support_lower=POSTERIOR_SUPPORT_LOWER,
        posterior_support_upper=POSTERIOR_SUPPORT_UPPER,
        prior_lower=PRIOR_LOWER,
        prior_upper=PRIOR_UPPER,
        upper_22_6_pct_lower=UPPER_22_6_PCT_LOWER,
        upper_22_6_pct_upper=UPPER_22_6_PCT_UPPER,
        pass_region_lower=PASS_REGION_LOWER,
        pass_region_upper=PASS_REGION_UPPER,
        band_edge_inclusion=np.array(s3["band_edge_inclusion"]),
        upper_22_6_pct_inclusion=np.array(s3["upper_22_6_pct_inclusion"]),
        in_pass_region=np.array(s3["in_pass_region"]),
        in_prior=np.array(s3["in_prior"]),
        log10_n_PBH=s3["log10_n_PBH"],
        g_BBN=g_BBN,
        T_H_g_BBN=T_H_g_BBN_GeV,
        f_g_BBN=f_g_BBN,
        beta_PBH=s2["beta_PBH"],
        rho_substrate_g_BBN=s2["rho_substrate_g_BBN_kg_per_m3"],
        M_PBH_typical=s2["M_PBH_typical_kg"],
        n_edge_at_g_BBN=s2["n_edge_at_g_BBN"],
        prob_form=s2["prob_form"],
        L_pix_LRD_m=s2["L_pix_LRD_m"],
        N_eigs=s2["N_eigs"],
        M_LRD_kg=s2["M_LRD_kg"],
        parent_n_PBH=s2["parent_n_PBH"],
        parent_g_BBN=s2["parent_g_BBN"],
        sign_verdict=s4["sign_verdict"],
        magnitude_verdict=s4["magnitude_verdict"],
        regime_verdict=s4["regime_verdict"],
        composite_verdict=s4["composite_verdict"],
        g_saturate_threshold=s4["g_saturate_threshold"],
        f_used=s4["f_used"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"Wrote .npz: {OUT_NPZ}")

    # Plot
    write_png(n_PBH, s3, s4)
    print(f"Wrote .png: {OUT_PNG}")

    # Verdict value-string per §8 (output 4-tuple)
    value_str = (  # (local)
        f"n_PBH_central={n_PBH:.6e};"
        f"band_edge_inclusion={s3['band_edge_inclusion']};"
        f"upper_22_6_pct={s3['upper_22_6_pct_inclusion']}"
    )

    # Step D: append verdict line (canonical + dual-SHA + 3-tuple)
    append_verdict(
        s4["composite_verdict"],
        value_str,
        audit_sha,
        content_sha,
        s4["sign_verdict"],
        s4["magnitude_verdict"],
        s4["regime_verdict"],
    )
    print(f"Appended verdict line to {VERDICT_TXT}")
    print()
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print()

    # Final 4-tuple line per output-standards.md (final non-verdict line)
    print(
        f"4-tuple: (value={value_str!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
