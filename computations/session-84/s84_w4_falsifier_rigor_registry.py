#!/usr/bin/env python3
"""
S84 W4-48 — FALSIFIER-RIGOR-REGISTRY
=====================================

Gate: S84-FALSIFIER-RIGOR-REGISTRY ([AUDIT])

Pre-registered threshold:
  PASS: N_flagged / N_total = 1.0  AND  ZFP count >= 3  AND  no un-tagged channel.
  INFO: 0.80 <= N_flagged / N_total < 1.0
  FAIL: N_flagged / N_total < 0.80

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - sessions/framework/registry/pre-registered-observations.md
  - sessions/permanent-results-registry.md
  - computations/session-82/s82_gate_verdicts.txt
  - computations/session-83/s83_gate_verdicts.txt
  - computations/session-84/s84_gate_verdicts.txt

Output 4-tuple:
  (value="<N_flagged>/<N_total>", scheme="4-flag-taxonomy",
   convention="S84 rigor registry", L_max="N/A")

Classification: NON-PHONONIC (methodology / registry audit)

METHODOLOGY
-----------
Meta-registry: tag every framework falsifier channel with exactly one of four
rigor flags {ZERO-FREE-PARAMETER, ACCOMMODATION, SCHEME-DEPENDENT,
DETECTOR-STERILE}. No numerical physics re-computation; channel entries are
inherited from S60-S83 gates. This gate closes a methodological gap in S83
sagan-synthesis V (three-axis distinction) by preventing evidence-inflation
across the Wave 4 -> Wave 5 synthesis. Serializes to JSON + markdown registry.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU only (no numerics; pure table + I/O). OMP threads capped below.
- SHA-256 of all input files logged in first 20 lines of stdout
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to `s84_gate_verdicts.txt` with SHA pin
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (no heavy linalg; avoid contention)
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "4")
os.environ.setdefault("MKL_NUM_THREADS", "4")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S84"                                       # (local)
GATE_ID = "S84-FALSIFIER-RIGOR-REGISTRY"              # (local)
SCHEME = "4-flag-taxonomy"                            # (local)
CONVENTION = "S84 rigor registry"                     # (local)
L_MAX = "N/A"                                         # (local)

PASS_RATIO_THRESHOLD = 1.0                            # (local)
INFO_RATIO_THRESHOLD = 0.80                           # (local)
MIN_ZFP_COUNT = 3                                     # (local)

OUT_JSON = resolve_output(84, 's84_w4_falsifier_rigor_registry.json')
OUT_MD = PROJECT_ROOT / "sessions" / "framework" / "falsifier-rigor-registry.md"
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "sessions" / "framework" / "pre-registered-observations.md",
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
    resolve_output(82, 's82_gate_verdicts.txt'),
    resolve_output(83, 's83_gate_verdicts.txt'),
    resolve_output(84, 's84_gate_verdicts.txt'),
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                         # (local)
    for p in inputs:
        sha = sha256_of(p)                            # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                      # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — The 4-flag taxonomy
# ---------------------------------------------------------------------------

RIGOR_FLAGS = {
    "ZERO-FREE-PARAMETER": (
        "Prediction derived from substrate eigenvalue problem with NO free "
        "parameter; LCDM-match is genuine evidence (BF > 1)."
    ),
    "ACCOMMODATION": (
        "Framework is consistent with data but one or more parameters were "
        "tuned to match; evidence weight is 1x, not >1x."
    ),
    "SCHEME-DEPENDENT": (
        "Prediction magnitude or sign depends on regulator/scheme choice that "
        "has not been canonicalized; in data-agreement column but flagged for "
        "resolution."
    ),
    "DETECTOR-STERILE": (
        "Prediction is structural but outside all current and near-future "
        "(2030-2040) detector reach; no discrimination possible in window."
    ),
}

# Exactly-one-flag requirement — every channel's primary tag is its
# adjudicated HONOR-flag. Secondary observations (e.g., a ZFP prediction that
# is ALSO detector-sterile) are logged in the justification text but only the
# adjudicated flag goes in the registry column.


# ---------------------------------------------------------------------------
# Section 6 — Channel registry (inherited from S60-S83 gates; see plan W4-48)
# ---------------------------------------------------------------------------

def build_channel_registry():
    """Return the list of channel records with flags, justifications,
    dependent gates and registry locations."""
    channels = []                                     # (local)

    # 1. n_s
    channels.append({
        "channel_id": "n_s",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "0.9590 (S65 collab, Bogoliubov-inversion triple)",
        "observational_value": "0.9649 +/- 0.0042 (Planck 2018)",
        "tension": "1.40 sigma",
        "justification": (
            "n_s is a zero-free-parameter substrate prediction: "
            "Bogoliubov-inversion over three regulators (S60 cross-scheme "
            "triple; S65 collab). No tunable cutoff; the regulator-invariant "
            "triple survived the S66 cutoff-sensitivity audit."
        ),
        "dependent_gates": ["S63-RUNNING-NS-63", "S65-collab", "S83-G48"],
        "registry_location": "pre-registered-observations.md (CMB-S4)",
    })

    # 2. r
    channels.append({
        "channel_id": "r",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "0.01173 (S83 G46 tensor-transfer)",
        "observational_value": "< 0.036 (95% CL, BK18)",
        "tension": "PASS (headroom 3.07x below 95% CL)",
        "justification": (
            "r derives from tensor-to-scalar ratio through G46 transfer "
            "kernel with c_T, c_S from spectral moments a_0, a_2. Pre-fold "
            "value inherits from epsilon_H fold geometry (S83 PASS). No "
            "adjustable slow-roll potential tuning."
        ),
        "dependent_gates": ["S83-G46-TENSOR-TRANSFER",
                            "S84-BICEP-KECK-2026-PRE-REGISTER"],
        "registry_location": "pre-registered-observations.md (LiteBIRD/BK)",
    })

    # 3. n_T (transit) — ZFP vs DETECTOR-STERILE adjudication
    channels.append({
        "channel_id": "n_T (transit, k ~ M_KK)",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "+0.468 (BLUE, S65/S83 G50)",
        "observational_value": "inaccessible (k_transit 54 decades above CMB)",
        "tension": "N/A (no detector reach 2026-2040)",
        "justification": (
            "ADJUDICATION: two flags apply (ZFP derivation + detector-"
            "sterile reach). Taxonomy requires exactly one. HONOR-FLAG = "
            "ZERO-FREE-PARAMETER because the value +0.468 is pinned by "
            "Jensen-curvature (single substrate number, no tunable "
            "parameter). Detector-sterility is a SEPARATE PROPERTY recorded "
            "in the justification, not the primary tag. Rationale: the "
            "taxonomy honors the epistemic strength of the prediction first; "
            "detector reach is a state-of-the-art fact about instruments, "
            "not a property of the framework. Per S84 BLUE-TRANSIT-TILT-"
            "INACCESSIBILITY (EVOI=0), channel is flagged sterile-for-"
            "discrimination in the EVOI table, but the rigor-registry "
            "reflects the PREDICTION strength."
        ),
        "dependent_gates": ["S65-NT-BLUE-65", "S83-G50",
                            "S84-BLUE-TRANSIT-TILT-INACCESSIBILITY"],
        "registry_location": "pre-registered-observations.md (LiteBIRD/BK)",
    })

    # 4. n_T (CMB) — ZFP vs SCHEME-DEPENDENT adjudication (NEW INFO #1)
    channels.append({
        "channel_id": "n_T (CMB, k = 0.05 Mpc^-1)",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "-3.024e-3 (S84 W4-39)",
        "observational_value": "not yet measured; sigma_LB_3yr = 0.0654 (S84 W4-37)",
        "tension": "DETECTOR-STERILE for discrimination; PREDICTION is ZFP",
        "justification": (
            "ADJUDICATION (NEW INFO 1 from batch-A): S68 reported Delta(n_T) "
            "= 0 under STANDARD slow-roll (c_T = c_S = 1). S84 W4-39 "
            "established generalized consistency n_T = -(r * c_T)/(8 * c_S) "
            "with framework c_T = 1.000, c_S = 0.485 (from a_2 and a_0 "
            "moments). Substitution chain: n_T^FW - n_T^SR = -(r/8) * "
            "(c_T/c_S - 1) = -(0.01173/8)(2.062 - 1) = -1.557e-3 (NEGATIVE, "
            "machine-epsilon reproduced at 1.30e-18 in W4-39). HONOR-FLAG = "
            "ZERO-FREE-PARAMETER: the c_T/c_S = 2.062 ratio is pinned by "
            "spectral moments (not scheme-shopping). The S68-vs-W4-39 "
            "Delta != 0 is NOT a scheme choice -- it is a derived "
            "framework prediction that REPLACES standard single-field "
            "consistency. Framework authors must cite modified consistency "
            "as the canonical comparison."
        ),
        "dependent_gates": ["S68-LITEB-R-FORECAST-68", "S66-TENSOR-TRANSFER-66",
                            "S84-N_T-CMB-TRANSFER", "S83-G46"],
        "registry_location": "pre-registered-observations.md (LiteBIRD)",
    })

    # 5. alpha_s
    channels.append({
        "channel_id": "alpha_s",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "-0.0690 (S84 ALPHA-S-PRE-REGISTRATION)",
        "observational_value": "-0.0045 +/- 0.0067 (Planck 2018)",
        "tension": "TENSION (framework is off central by 9.6 sigma using "
                   "Planck err only; CMB-S4 projected sigma ~ 0.003 => 22 sigma)",
        "justification": (
            "alpha_s is derived from GGE running through single-parameter "
            "framework identity (S84 PASS at pre-registration). Zero free "
            "parameters. Framework's alpha_s = -0.069 is in TENSION with "
            "Planck (a PASS of a different kind: framework commits to a "
            "specific number and data will discriminate). The 'PASS' at "
            "pre-registration reflects completion of registration, not "
            "data agreement; the S50 identity alpha_s = n_s^2 - 1 is the "
            "load-bearing structural result."
        ),
        "dependent_gates": ["S50 permanent", "S84-ALPHA-S-PRE-REGISTRATION"],
        "registry_location": "pre-registered-observations.md (CMB-S4)",
    })

    # 6. m_H — ACCOMMODATION (NEW INFO #5)
    channels.append({
        "channel_id": "m_H (Higgs mass)",
        "rigor_flag": "ACCOMMODATION",
        "prediction_value": "188.19 GeV at mu_BC from S84-MU-BC-GEOMETRIC PASS "
                            "(via bi-criterion mu_BC fit; earlier S83 quote 132 GeV)",
        "observational_value": "125.25 +/- 0.17 GeV (PDG)",
        "tension": "ACCOMMODATION-FLAGGED (mu_BC fit pins the scale)",
        "justification": (
            "ADJUDICATION (NEW INFO 5): m_H is derived THROUGH mu_BC, which "
            "is itself tuned to match PDG sin^2(theta_W) via the bi-"
            "criterion procedure (S83 W3-G47, S84-MU-BC-GEOMETRIC). "
            "Although the substrate cubic identity is ZFP, the mu_BC "
            "fit introduces one tunable scale (matched to PDG sin^2). "
            "HONOR-FLAG = ACCOMMODATION per user directive: 'one scale "
            "tuned to PDG sin^2(theta_W); do NOT allow citation as ZFP'. "
            "Evidence weight is 1x."
        ),
        "dependent_gates": ["S83-W3-G47-sin2-thetaW-2loop-mu-BC",
                            "S84-MU-BC-GEOMETRIC",
                            "S84-YUKAWA-OOM-ESTIMATOR"],
        "registry_location": "permanent-results-registry.md (Higgs)",
    })

    # 7. sin^2 theta_W
    channels.append({
        "channel_id": "sin^2(theta_W)",
        "rigor_flag": "ACCOMMODATION",
        "prediction_value": "0.23480 (at mu_BC = 188.44 GeV, fit)",
        "observational_value": "0.23121 +/- 0.00004 (PDG, MSbar at M_Z)",
        "tension": "ACCOMMODATION-FLAGGED (mu_BC tuned to match)",
        "justification": (
            "sin^2(theta_W) at M_Z is matched to PDG through mu_BC "
            "accommodation. Geometric cubic identity 3*sin^2(theta_W) = "
            "cos(theta_cube) is ZFP in structure but the tuning of mu_BC "
            "to land on PDG at M_Z makes the data-match accommodation, not "
            "evidence. Flag aligned with m_H row."
        ),
        "dependent_gates": ["S83-W3-G47", "S82-W3-10-CUBIC-SIN2-W-EW"],
        "registry_location": "permanent-results-registry.md (EW)",
    })

    # 8. A_s (amplitude of scalar perturbations)
    channels.append({
        "channel_id": "A_s",
        "rigor_flag": "SCHEME-DEPENDENT",
        "prediction_value": "5.078e-9 (S84 AS-PIN-MAP-COMMIT, TD-canonical)",
        "observational_value": "2.099e-9 (Planck 2018)",
        "tension": "0.384 OOM above Planck (TD-canonical); scheme-dependent",
        "justification": (
            "A_s is scheme-dependent across the regulator atlas (zeta vs "
            "Zubarev vs SDW) documented in S84 LEDGER-LINEARITY-ATLAS. "
            "The canonical TD (G10 PASS via 3PI) sits at 5.08e-9; other "
            "regulators shift the number. Until the regulator is canonic-"
            "alized for A_s with a structural argument (not posterior "
            "selection), the channel remains SCHEME-DEPENDENT. Note: S69 "
            "synthesis noted A_s gap = 0.485 OOM; S84 A_s gap recalibrated "
            "to 0.384 OOM under current pin."
        ),
        "dependent_gates": ["S63-AS-AMPLITUDE-63", "S84-AS-PIN-MAP-COMMIT",
                            "S84-LEDGER-LINEARITY-ATLAS"],
        "registry_location": "permanent-results-registry.md (primordial)",
    })

    # 9. f_NL (equilateral + folded + multi; shape)
    channels.append({
        "channel_id": "f_NL (total, with folded-shape template)",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "f_NL^total = 1.03 (S67 GGE-BISPECTRUM)",
        "observational_value": "-26 +/- 47 (Planck equilateral)",
        "tension": "0.57 sigma",
        "justification": (
            "f_NL is computed from GGE bispectrum 3-point function (S67 "
            "GGE-BISPECTRUM-67) with channel decomposition (equil=0.853, "
            "folded=0.129, multi=0.56). No free parameter: each channel's "
            "amplitude is fixed by GGE occupation numbers + sound speeds "
            "from spectral moments. The FOLDED-TRIANGLE SHAPE is a "
            "substrate-unique prediction (Bogoliubov pair production has "
            "no scalar-field analog)."
        ),
        "dependent_gates": ["S67-GGE-BISPECTRUM-67", "S68-CMBS4-FNL-FORECAST-68"],
        "registry_location": "pre-registered-observations.md (21cm/CMB-S4)",
    })

    # 10. alpha_f_NL (amplitude running) — DETECTOR-STERILE (NEW INFO #2)
    channels.append({
        "channel_id": "alpha_f_NL (bispectrum amplitude running)",
        "rigor_flag": "DETECTOR-STERILE",
        "prediction_value": "-0.143 +/- 0.044 (S84 W4-38 FAIL)",
        "observational_value": "sigma_SKA-2 ~ 3.0 on alpha",
        "tension": "SNR ~ 0.05 at SKA-2; sub-1 sigma at CVL 21cm",
        "justification": (
            "ADJUDICATION (NEW INFO 2 -- sub-channel split): the "
            "AMPLITUDE-RUNNING alpha_f_NL itself is DETECTOR-STERILE "
            "(framework's |alpha| = 0.143 vs SKA-2 sigma 3.0 => SNR 0.05; "
            "21cm CVL at best 7x above framework). The UNDERLYING SHAPE "
            "(folded-triangle template existence) is a substrate-unique "
            "prediction and is covered in the f_NL row (ZFP). This row "
            "tags only the AMPLITUDE-RUNNING CHANNEL which is what W4-38 "
            "computed."
        ),
        "dependent_gates": ["S84-ALPHA-F-NL-FRAMEWORK-PRED",
                            "S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR"],
        "registry_location": "pre-registered-observations.md (SKA)",
    })

    # 11. w_0 — SCHEME-DEPENDENT pending W4-46 (NEW INFO #4)
    channels.append({
        "channel_id": "w_0",
        "rigor_flag": "SCHEME-DEPENDENT",
        "prediction_value": "-0.918 (canonical, S58) OR -0.842 (S83 branch-iv, "
                            "S84 W0-REGULATOR-RESOLUTION-SV1 PASS at L=5)",
        "observational_value": "-0.752 +/- 0.057 (DESI DR2 + DESY5)",
        "tension": "2.91 sigma (branch -0.918); ~1.58 sigma (branch -0.842)",
        "justification": (
            "ADJUDICATION (NEW INFO 4): post-S83 W0-workshop, explicit "
            "scheme split (zeta vs Zubarev vs SDW, split 0.08 at L=5) "
            "makes w_0 SCHEME-DEPENDENT. CANONICAL = -0.918 (branch iv "
            "W0_FW in canonical_constants.py); S83 branch-(iv) adjudication "
            "promoted -0.842 at L=5 but the W4-46 L_max convergence test "
            "remains UNCOMPUTED in this batch. Per user directive: 'flag "
            "SCHEME-DEPENDENT even though canonical -- the rigor-registry "
            "exists precisely to flag scheme-dependent predictions.' "
            "Upgrade path: if W4-46 returns PASS (split shrinks with "
            "L_max), upgrade to ZERO-FREE-PARAMETER in S85; if W4-46 "
            "returns FAIL, keep SCHEME-DEPENDENT."
        ),
        "dependent_gates": ["S83-W3-G51-W0-REGULATOR",
                            "S84-W0-REGULATOR-RESOLUTION-SV1/SV2/SV5",
                            "S84-G51-LMAX-CONVERGENCE (pending)",
                            "S84-DR3-RESPONSE-PROTOCOL"],
        "registry_location": "pre-registered-observations.md (DESI)",
    })

    # 12. w_a
    channels.append({
        "channel_id": "w_a",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "0 (exactly; four-fold locked)",
        "observational_value": "-0.73 +/- 0.25 (DESI DR2 + DESY5)",
        "tension": "2.92 sigma (pending DR3 resolution)",
        "justification": (
            "w_a = 0 is structurally locked by four independent mechanisms "
            "(GGE integrability + Josephson phase + frozen texture + "
            "thermalization barrier, 59 OOM gap, S68 workshop). It cannot "
            "be adjusted. Zero free parameters; decisive DR3 test in "
            "2026-2027."
        ),
        "dependent_gates": ["S68-Volovik-Mack-workshop",
                            "S84-DR3-CONTINGENCY-FINE-GRAINED"],
        "registry_location": "pre-registered-observations.md (DESI)",
    })

    # 13. mu (FIRAS spectral distortion)
    channels.append({
        "channel_id": "mu (FIRAS spectral distortion)",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "4.976e-10 (S82 FIRAS-CHLUBA-FULL PASS, "
                            "Planck-tilt) / 6.169e-10 (flat)",
        "observational_value": "|mu| < 9e-5 (FIRAS 95% CL)",
        "tension": "5.26 OOM below FIRAS (PASS)",
        "justification": (
            "mu derives from Chluba y-kernel evaluated on framework "
            "primordial amplitude (A_s pin). Zero tunable parameters; "
            "96% of signal from k = 10-100 Mpc^-1 IR shoulder. S82 FULL "
            "PASS reproduced S79 flat-pivot exactly and Planck-tilt with "
            "ratio 0.806."
        ),
        "dependent_gates": ["S82-FIRAS-CHLUBA-FULL"],
        "registry_location": "permanent-results-registry.md (FIRAS)",
    })

    # 14. Omega_GW (domain walls / LISA)
    channels.append({
        "channel_id": "Omega_GW (domain walls, LISA f)",
        "rigor_flag": "DETECTOR-STERILE",
        "prediction_value": "~ 10^-10 at 1 mHz (S59 LISA-GW); migration "
                            "threshold 10^-40 (S83 Channel-5)",
        "observational_value": "LISA sensitivity ~ 10^-12 at 1 mHz",
        "tension": "46.7 OOM below LISA reach; gamma-WALL re-label PASS (S83)",
        "justification": (
            "Omega_GW from domain walls predicted ~10^-10, but S83 "
            "CHANNEL-5-RELABEL established gamma-WALL is 46.7 OOM BELOW "
            "LISA reach at 1 mHz. Channel moved from FALSIFIER to "
            "DETECTOR-STERILE under S83 re-label. Prediction is "
            "structural (ZFP in derivation) but inaccessible for "
            "discrimination -- honor-flag is DETECTOR-STERILE for the "
            "2025-2050 window per plan W4-47 UHF-GW-THRESHOLD-WATCH."
        ),
        "dependent_gates": ["S59-LISA-GW-PREDICTION", "S83-CHANNEL-5-RELABEL",
                            "S84-UHF-GW-THRESHOLD-WATCH (pending)"],
        "registry_location": "pre-registered-observations.md (LISA)",
    })

    # 15. sigma_8
    channels.append({
        "channel_id": "sigma_8",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "0.793-0.799 (S69 PVD-FSIG8 PASS, f*sigma8 chi2/"
                            "dof=0.761)",
        "observational_value": "0.811 +/- 0.006 (Planck) / 0.766 +/- 0.03 (lensing)",
        "tension": "between both (S8 tension amelioration, 0.8 sigma eased)",
        "justification": (
            "sigma_8 derives from framework linear growth through substrate-"
            "compaction-modulated transfer function. Zero free parameters. "
            "S69 PVD-FSIG8 PASS: framework beat LCDM chi2/dof on RSD data. "
            "S70 FULL-COV-RSD halved the advantage under full covariance "
            "but FW still preferred robustly."
        ),
        "dependent_gates": ["S69-PVD-FSIG8-69", "S70-FULL-COV-RSD"],
        "registry_location": "pre-registered-observations.md (Euclid)",
    })

    # 16. C_cons (cosmological consistency / clock constraint)
    channels.append({
        "channel_id": "C_cons (consistency-count aggregate)",
        "rigor_flag": "DETECTOR-STERILE",
        "prediction_value": "G44 FAIL at 23x above PASS",
        "observational_value": "Structural internal-consistency gate",
        "tension": "No external detector counterpart",
        "justification": (
            "C_cons is an INTERNAL framework-consistency gate (S83 G44 "
            "FAIL at 23x above PASS threshold). It is not an observational "
            "falsifier -- no external detector measures this aggregate. "
            "Classified DETECTOR-STERILE because no observational channel "
            "can probe the internal consistency quantity; discrimination "
            "collapses to a different entity (internal framework audit)."
        ),
        "dependent_gates": ["S83-G44"],
        "registry_location": "permanent-results-registry.md (internal)",
    })

    # 17. ISW tracking (c_s^2 DE = 0 signature)
    channels.append({
        "channel_id": "ISW tracking (c_s^2_DE = 0)",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "+7.6% vs quintessence (substrate-specific); "
                            "+12.3% vs LCDM total",
        "observational_value": "A_ISW = 1.00 +/- 0.25 (Planck); SNR Euclid 1.58",
        "tension": "0.49 sigma from LCDM (current data cannot discriminate)",
        "justification": (
            "ISW tracking signature c_s^2_DE = 0 is the UNIQUE discriminant "
            "against quintessence. Volovik tracking vacuum + Mack ISW-"
            "galaxy cross-correlation (S68 ISW-TRACKING-68 PASS, S69 PVD-"
            "ISW-69, S70 CLASS-ISW-70 PASS). Zero free parameters. "
            "Near-detector-sterile at Euclid DR1 (SNR 1.58 marginal); "
            "definitive at 21cm purpose-built (SNR 7.9). Flagged ZFP "
            "because the PREDICTION is zero-parameter; Euclid marginal "
            "discrimination means it is NOT sterile in the full "
            "2030-2040 window."
        ),
        "dependent_gates": ["S68-ISW-TRACKING-68", "S69-PVD-ISW-69",
                            "S70-CLASS-ISW-70", "S84-21CM-ISW-PRE-REG (S71)"],
        "registry_location": "pre-registered-observations.md (Euclid/21cm)",
    })

    # 18. Mass ordering (JUNO/DUNE)
    channels.append({
        "channel_id": "Neutrino mass ordering",
        "rigor_flag": "ZERO-FREE-PARAMETER",
        "prediction_value": "Normal (B1 < B2 < B3; machine epsilon "
                            "S8/S34-36/S52/S56)",
        "observational_value": "NO preferred at ~2.5 sigma (NuFit-6.0)",
        "tension": "consistent",
        "justification": (
            "NO is a structural prediction: Jensen-deformed SU(3) fiber "
            "spectrum B1 < B2 < B3 at all tau > 0, proven to machine "
            "epsilon across S8, S34-36, S52, S56. IO observation would "
            "invalidate the spectral geometry. Decisive DUNE 5-sigma "
            "test in 2032."
        ),
        "dependent_gates": ["S56 Workshop 4", "S41 W1-2 (seesaw = 0)"],
        "registry_location": "pre-registered-observations.md (JUNO/DUNE)",
    })

    return channels


# ---------------------------------------------------------------------------
# Section 7 — Compute (assemble, tally, verdict)
# ---------------------------------------------------------------------------

def tally_flags(channels):
    tally = {k: 0 for k in RIGOR_FLAGS}
    untagged = 0                                     # (local)
    for c in channels:
        flag = c.get("rigor_flag")                   # (local)
        if flag in tally:
            tally[flag] += 1
        else:
            untagged += 1
    return tally, untagged


def compute():
    channels = build_channel_registry()
    tally, untagged = tally_flags(channels)
    n_total = len(channels)                          # (local)
    n_flagged = n_total - untagged                   # (local)
    ratio = n_flagged / n_total                      # (local)
    zfp_count = tally["ZERO-FREE-PARAMETER"]         # (local)

    result = {
        "channels": channels,
        "tally": tally,
        "n_total": n_total,
        "n_flagged": n_flagged,
        "untagged": untagged,
        "ratio": ratio,
        "zfp_count": zfp_count,
    }
    return result


def determine_verdict(result):
    ratio = result["ratio"]
    zfp = result["zfp_count"]
    untagged = result["untagged"]
    if ratio >= PASS_RATIO_THRESHOLD and zfp >= MIN_ZFP_COUNT and untagged == 0:
        return "PASS"
    if ratio >= INFO_RATIO_THRESHOLD:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 8 — Serialize: JSON + markdown registry
# ---------------------------------------------------------------------------

def write_json(result, closure_sha):
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "taxonomy": RIGOR_FLAGS,
        "ratio": result["ratio"],
        "n_total": result["n_total"],
        "n_flagged": result["n_flagged"],
        "untagged": result["untagged"],
        "tally": result["tally"],
        "channels": result["channels"],
        "closure_sha256": closure_sha,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=True))
    return payload


def write_markdown(result, closure_sha):
    lines = []                                       # (local)
    lines.append("# Falsifier-Rigor Registry\n")
    lines.append("")
    lines.append(f"**Gate**: {GATE_ID}  ")
    lines.append(f"**Scheme**: {SCHEME}  ")
    lines.append(f"**Convention**: {CONVENTION}  ")
    lines.append(f"**Closure SHA-256**: `{closure_sha}`  ")
    lines.append(f"**Generated by**: `s84_w4_falsifier_rigor_registry.py` "
                 f"(S84 W4-48)  ")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "Every falsifier channel carries EXACTLY ONE rigor flag. The "
        "registry exists to prevent evidence-inflation: a SCHEME-DEPENDENT "
        "prediction cannot be cited alongside a ZERO-FREE-PARAMETER "
        "prediction as if they carried the same evidentiary weight."
    )
    lines.append("")
    lines.append("## 4-Flag Legend")
    lines.append("")
    for k, v in RIGOR_FLAGS.items():
        lines.append(f"- **{k}** -- {v}")
    lines.append("")
    lines.append(
        "EXACTLY-ONE-FLAG RULE: each channel receives the HONOR-FLAG that "
        "best captures the strongest epistemic property of the prediction. "
        "Secondary properties (e.g., a ZFP prediction that is also "
        "detector-sterile) are recorded in the justification text."
    )
    lines.append("")
    lines.append("## Tally")
    lines.append("")
    lines.append(f"- Total channels: **{result['n_total']}**")
    lines.append(f"- Flagged: **{result['n_flagged']}** "
                 f"(audit completeness: {100*result['ratio']:.1f}%)")
    lines.append(f"- Un-flagged: **{result['untagged']}**")
    lines.append("")
    for k, n in result["tally"].items():
        lines.append(f"  - {k}: **{n}**")
    lines.append("")
    lines.append("## Channel Table")
    lines.append("")
    header = ("| # | Channel | Flag | Prediction | Observational | "
              "Tension | Dependent Gates | Registry |")
    sep = ("|:-:|:--------|:-----|:-----------|:--------------|"
           ":--------|:----------------|:---------|")
    lines.append(header)
    lines.append(sep)
    for i, c in enumerate(result["channels"], 1):
        gates = ", ".join(c["dependent_gates"])      # (local)
        lines.append(
            f"| {i} | **{c['channel_id']}** | `{c['rigor_flag']}` | "
            f"{c['prediction_value']} | {c['observational_value']} | "
            f"{c['tension']} | {gates} | {c['registry_location']} |"
        )
    lines.append("")
    lines.append("## Justification Detail")
    lines.append("")
    for i, c in enumerate(result["channels"], 1):
        lines.append(f"### {i}. {c['channel_id']} -- `{c['rigor_flag']}`")
        lines.append("")
        lines.append(c["justification"])
        lines.append("")
        lines.append(f"- **Dependent gates**: "
                     f"{', '.join(c['dependent_gates'])}")
        lines.append(f"- **Registry**: {c['registry_location']}")
        lines.append("")
    lines.append("## Adjudication Notes (S84 W4-48)")
    lines.append("")
    lines.append(
        "Five cases required explicit adjudication beyond the default "
        "assignment algorithm; they are flagged in the channel table and "
        "the justifications carry `ADJUDICATION (NEW INFO #)` markers."
    )
    lines.append("")
    lines.append(
        "1. **n_T (CMB) Delta-inconsistency (S68 vs W4-39)** -- resolved "
        "ZFP; modified consistency n_T = -r*c_T/(8*c_S) with c_T/c_S = "
        "2.062 derived from spectral moments replaces standard -r/8.")
    lines.append(
        "2. **alpha_f_NL sub-channel split** -- amplitude running is "
        "DETECTOR-STERILE; folded-SHAPE prediction lives on the f_NL row "
        "(ZFP).")
    lines.append(
        "3. **n_T (transit)** -- dual property (ZFP derivation + sterile "
        "reach); HONOR-FLAG = ZFP; sterility recorded in EVOI table and "
        "justification.")
    lines.append(
        "4. **w_0 SCHEME-DEPENDENT pending W4-46** -- canonical -0.918 "
        "vs S83 branch-(iv) -0.842, scheme split 0.08 at L=5; upgrade to "
        "ZFP if W4-46 L_max convergence PASS, else stay SCHEME-DEPENDENT.")
    lines.append(
        "5. **m_H via mu_BC bi-criterion** -- ACCOMMODATION (one scale "
        "tuned to PDG sin^2 theta_W); cannot be cited as ZFP.")
    lines.append("")
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines))
    return str(OUT_MD)


# ---------------------------------------------------------------------------
# Section 9 — Verdict emission
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max!r})")


def append_verdict(verdict, value, closure_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as f:
        f.write(line)
    return line.rstrip()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"=== {GATE_ID} ===")
    print(f"session={SESSION} scheme={SCHEME} convention={CONVENTION} "
          f"L_max={L_MAX}")
    print()

    # --- input pins ---
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                    # (local)
    print(f"closure_sha256={closure}")
    print()

    # --- compute ---
    result = compute()

    print("--- Tally ---")
    for k, n in result["tally"].items():
        print(f"  {k}: {n}")
    print(f"  total={result['n_total']} "
          f"flagged={result['n_flagged']} "
          f"untagged={result['untagged']} "
          f"ratio={result['ratio']:.4f} "
          f"ZFP={result['zfp_count']}")
    print()

    # --- verdict ---
    verdict = determine_verdict(result)             # (local)
    value_str = (f"{result['n_flagged']}/{result['n_total']} "
                 f"(ZFP={result['zfp_count']})")    # (local)
    print(f"verdict: {verdict}")
    print(f"value: {value_str}")
    print()

    # --- serialize ---
    write_json(result, closure)
    print(f"wrote JSON: {OUT_JSON.relative_to(PROJECT_ROOT)}")

    md_path = write_markdown(result, closure)       # (local)
    print(f"wrote MD:   {Path(md_path).relative_to(PROJECT_ROOT)}")

    # --- append verdict ---
    line = append_verdict(verdict, value_str, closure)
    print(f"verdict line:")
    print(f"  {line}")

    # --- final 4-tuple ---
    print()
    print(emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX))

    return 0


if __name__ == "__main__":
    sys.exit(main())
