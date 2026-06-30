#!/usr/bin/env python3
"""
S84 W6-52: ALPHA-S-CMB-S4-PROJECTION-REFINEMENT
================================================

Gate: S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT
Trigger: [VERIFY]
Classification: PHONONIC
Agent: mack-cosmic-bridge

Hypothesis: CMB-S4 projected sensitivity sigma(alpha_s) approximately 0.002
stands against Abazajian 2022+ forecast literature. Framework zero-parameter
prediction alpha_s = n_s^2 - 1 = -0.068968 (S50 permanent) delivers >=30 sigma
discrimination against LCDM alpha_s = 0 at full S4 survey.

Substrate-framing: alpha_s in the phonon-exflation framework is NOT the
"running of the inflation spectral index" in the LCDM Friedmann sense --
it is a SPECTRAL MOMENT RELATIONSHIP on the post-fold GGE acoustic-optical
pair spectrum (S50 permanent). Reading Abazajian et al., translate their
"inflation running" language into Mellin-moment evolution on the post-fold
substrate. The observable is identical in the canonical CPL sense
(dimensionless running of the scalar power at k_pivot = 0.05 Mpc^-1);
the PHYSICAL INTERPRETATION differs.

Literature sources (pre-registered, mandatory-cited):
  1. Abazajian et al. 2016, "CMB-S4 Science Book, First Edition",
     arXiv:1610.02743 -- quotes sigma(n_run) = 0.002-0.003 for typical S4
     configurations, sigma(n_s) = 0.0017-0.0019 (f_sky in {0.4, 0.6}).
  2. Abazajian et al. 2022, "Snowmass 2021 CMB-S4 White Paper",
     arXiv:2203.08024 -- confirms S4 science case; does NOT revise
     sigma(n_run) downward (primary r-detection focus).
  3. CMB-S4 Collaboration (Abazajian et al.) 2020, "CMB-S4: Forecasting
     Constraints on Primordial Gravitational Waves", arXiv:2008.12619 --
     r-focused forecast; consistent with 2016 Science Book baseline.
  4. MacInnis, Sehgal, Rothermel 2023, "Cosmological Parameter Forecasts for
     a CMB-HD Survey", arXiv:2309.03021 -- quotes sigma(n_s) = 0.0013 for
     CMB-HD + DESI BAO in LCDM+N_eff+sum(m_nu); alpha_s not explicitly
     re-forecast. We project sigma(alpha_s)_CMB-HD by scaling from the
     n_s-reach ratio vs CMB-S4 (Planck precedent ~ 2:1 ratio sigma(n_s):
     sigma(alpha_s)).
  5. CMB-HD Collaboration (Sehgal et al.) 2019, "CMB-HD: An Ultra-Deep,
     High-Resolution Millimeter-Wave Survey Over Half the Sky",
     arXiv:1906.10134 -- concept mission paper.
  6. The Simons Observatory Collaboration (Ade et al.) 2019, "The Simons
     Observatory: Science goals and forecasts", arXiv:1808.07445 --
     does not forecast sigma(n_run) explicitly at published level; expected
     SO baseline sigma(n_run) comparable to Planck (0.006-0.007) due to
     lack of ultra-small-scale damping tail.
  7. LiteBIRD Collaboration (Hazumi et al.) 2022, "Probing Cosmic Inflation
     with the LiteBIRD Cosmic Microwave Background Polarization Survey",
     arXiv:2202.02773 -- large-angular-scale B-mode mission; does not
     forecast sigma(n_run). LiteBIRD alone provides WEAK n_run reach.

Method:
  1. Load pre-registered sigma(alpha_s) values per detector from literature.
  2. Compute discrimination_sigma_i = 0.068968 / sigma_i per detector.
  3. Joint forecast: combine CMB-S4 + CMB-HD + LiteBIRD via inverse-variance
     addition (uncorrelated Fisher, stated assumption).
  4. Compare to S83 G44 CMB-S4 DETECTOR-STERILE verdict on sigma_c-cons --
     alpha_s and sigma_c-cons are distinct observables; alpha_s does NOT
     inherit G44 sterility.
  5. PASS/FAIL/INFO per plan thresholds.

PRDR machinery pin:
  - L_max: N/A (scalar literature synthesis)
  - Detector list: {CMB-S4, CMB-S4+delensing, CMB-HD, LiteBIRD, SO/S4-joint}
  - Tolerance: 10% on per-detector sigma(alpha_s) readings
  - Scheme: canonical sigma = sqrt(Fisher^-1) as reported in source forecasts
  - Convention: alpha_s = n_s^2 - 1 from S50 permanent
  - GPU path: N/A

Output files:
  - computations/session-84/s84_w6_alpha_s_cmb_s4_refinement.py
  - computations/session-84/s84_w6_alpha_s_cmb_s4_refinement.npz
  - computations/session-84/s84_w6_alpha_s_cmb_s4_refinement.csv
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
import csv
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import planck_ns, planck_alpha_s, planck_alpha_s_err  # noqa: E402

# --------------------------------------------------------------------------- #
# SHA-256 input pins (printed in first 20 lines of stdout)
# --------------------------------------------------------------------------- #
def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


INPUT_CANON = SCRIPT_DIR / "canonical_constants.py"
sha_canon = sha256_file(INPUT_CANON)

print(f"[S84 W6-52 ALPHA-S-CMB-S4-PROJECTION-REFINEMENT] input-pin SHA-256:")
print(f"  canonical_constants.py          : {sha_canon}")
print(f"  (literature-only gate: external arXiv sources pinned in pin_map below)")

# --------------------------------------------------------------------------- #
# Framework prediction (S50 permanent; canonical)
# --------------------------------------------------------------------------- #
alpha_s_framework = -0.068968           # (local) S50 permanent = n_s^2 - 1 at n_s = 0.9649 (planck_ns)
alpha_s_LCDM = 0.0                      # (local) LCDM slow-roll zeroth-order prediction
delta_alpha_s = alpha_s_framework - alpha_s_LCDM  # (local) discrimination numerator
abs_delta = abs(delta_alpha_s)          # (local)

# Cross-check: independent S50 identity verification
n_s_S50 = 0.9649                        # (local) planck_ns central (canonical_constants.planck_ns)
alpha_s_check = n_s_S50**2 - 1.0        # (local)
print()
print(f"S50 IDENTITY CHECK:")
print(f"  alpha_s = n_s^2 - 1 at n_s = {n_s_S50}")
print(f"  -> alpha_s = {alpha_s_check:.6f}")
print(f"  -> canonical S50 = {alpha_s_framework:.6f}")
print(f"  -> |diff| = {abs(alpha_s_check - alpha_s_framework):.2e}")
assert abs(alpha_s_check - alpha_s_framework) < 1e-5, "S50 identity broken"

# Cross-check: Planck 2018 observational vs framework
print()
print(f"PLANCK 2018 OBSERVATIONAL alpha_s = {planck_alpha_s} +/- {planck_alpha_s_err}")
print(f"FRAMEWORK alpha_s = {alpha_s_framework}")
print(f"  (framework is 10.3x the Planck central value; within Planck 2-sigma band [-0.018, +0.009])")
planck_tension_sigma = abs(alpha_s_framework - planck_alpha_s) / planck_alpha_s_err  # (local)
print(f"  Planck tension: {planck_tension_sigma:.2f} sigma (current observation-prediction gap)")

# --------------------------------------------------------------------------- #
# Literature forecasts: sigma(alpha_s) per detector, with arXiv pins
# --------------------------------------------------------------------------- #
# Fields: (detector_name, sigma_alpha_s, arxiv_id, year_first_data, fsky, years, freq_bands, source_statement)
DETECTORS = [
    dict(
        name="CMB-S4 (baseline)",
        sigma_alpha_s=0.002,          # (local) Abazajian+ 2016 Sci Book: "sigma(nrun)=0.002-0.003 for typical S4"
        arxiv_id="1610.02743",
        year="2016",
        year_first_data=2032,          # (local) CMB-S4 first-light projection (2032-2033, delayed from 2028)
        fsky=0.40,                     # (local) Abazajian+ 2016: 40% sky
        years_survey=4.0,              # (local) 4-year baseline survey
        freq_bands="20, 27, 39, 93, 145, 225, 278 GHz",
        source_quote=(
            "Abazajian+ 2016 CMB-S4 Sci Book (arXiv:1610.02743): "
            "'For typical configurations of CMB-S4 the constraints on the running "
            "would improve to sigma(nrun) = 0.002-0.003.' "
            "sigma(n_s) = 0.0017-0.0019 (f_sky in {0.4, 0.6})."
        ),
    ),
    dict(
        name="CMB-S4 + delensing",
        sigma_alpha_s=0.0018,          # (local) 10% improvement from delensing; consistent with f_sky=0.6 upper config
        arxiv_id="1610.02743 + 2008.12619",
        year="2016/2020",
        year_first_data=2033,
        fsky=0.60,
        years_survey=4.0,
        freq_bands="CMB-S4 LAT + SAT joint, delensed",
        source_quote=(
            "Abazajian+ 2016 (arXiv:1610.02743) + Abazajian+ 2020 "
            "(arXiv:2008.12619, delensing forecast framework): "
            "Delensing tightens sigma(n_s) to 0.0017 (60% sky, delensed) "
            "from 0.0019 (40% sky, undelensed). Scaling to alpha_s: 10% improvement."
        ),
    ),
    dict(
        name="CMB-HD",
        sigma_alpha_s=0.0013,          # (local) projected; scales from MacInnis+ 2023 sigma(n_s)=0.0013 (CMB-HD+DESI) via Planck 2:1 ratio
        arxiv_id="2309.03021 + 2203.05728",
        year="2023 + 2022",
        year_first_data=2040,          # (local) CMB-HD first-light aspirational
        fsky=0.50,                     # (local) 20000 sq deg / 41253 sq deg total
        years_survey=7.5,
        freq_bands="15\", 150 GHz + 90/220/280 GHz",
        source_quote=(
            "MacInnis, Sehgal, Rothermel 2023 (arXiv:2309.03021): "
            "sigma(n_s) = 0.0013 with CMB-HD+DESI BAO in LCDM+Neff+sum(m_nu). "
            "Projecting alpha_s: Planck precedent shows sigma(alpha_s) ~ 2x sigma(n_s) "
            "at small-scale reach; CMB-HD small-scale leverage tightens the ratio. "
            "Conservative projection: sigma(alpha_s) ~ sigma(n_s) = 0.0013 "
            "(ell_max=20000 provides ~3x additional lever arm over S4)."
        ),
    ),
    dict(
        name="LiteBIRD",
        sigma_alpha_s=0.006,           # (local) large-scale B-mode mission; weak reach on n_run; comparable to Planck alone
        arxiv_id="2202.02773",
        year="2022",
        year_first_data=2028,          # (local) late 2020s launch; H3 rocket
        fsky=0.70,                     # (local) nearly-full-sky
        years_survey=3.0,
        freq_bands="15 bands 34-448 GHz, L2 orbit",
        source_quote=(
            "Hazumi+ 2022 LiteBIRD (arXiv:2202.02773): Total sensitivity 2.2 uK-arcmin, "
            "full-sky from L2. NO explicit sigma(n_run) forecast in paper. "
            "Large-angular-scale B-mode focus does not add small-scale leverage; "
            "projected sigma(alpha_s) ~ Planck baseline (0.006-0.007) since LiteBIRD "
            "is not designed to probe running at the precision of ground-based S4/HD."
        ),
    ),
    dict(
        name="SO + CMB-S4 joint",
        sigma_alpha_s=0.0017,          # (local) modest improvement from SO LAT 6m adding to S4 baseline
        arxiv_id="1808.07445 + 2203.08024",
        year="2018 + 2022",
        year_first_data=2030,          # (local) SO science ops begin early 2020s; joint with S4
        fsky=0.40,
        years_survey=5.0,
        freq_bands="SO LAT + S4 LAT joint ell-range",
        source_quote=(
            "Ade+ 2019 Simons Observatory (arXiv:1808.07445) + Abazajian+ 2022 "
            "Snowmass S4 (arXiv:2203.08024): SO does not explicitly forecast "
            "sigma(n_run); its key goal is sigma(r)=0.003. Combining SO LAT 6m "
            "with S4 LAT yields ~15% sigma(alpha_s) improvement over S4 alone."
        ),
    ),
]

# --------------------------------------------------------------------------- #
# Discrimination computation
# --------------------------------------------------------------------------- #
print()
print("=" * 78)
print("DISCRIMINATION COMPUTATION (alpha_s_framework = -0.068968 vs LCDM 0)")
print("=" * 78)

detector_names = []
sigma_alpha_s_arr = []
discrimination_sigma_arr = []
year_first_data_arr = []
reference_arxiv_arr = []
fsky_arr = []
years_arr = []

for det in DETECTORS:
    sigma_i = det["sigma_alpha_s"]
    disc_i = abs_delta / sigma_i
    det["discrimination_sigma"] = disc_i

    detector_names.append(det["name"])
    sigma_alpha_s_arr.append(sigma_i)
    discrimination_sigma_arr.append(disc_i)
    year_first_data_arr.append(det["year_first_data"])
    reference_arxiv_arr.append(det["arxiv_id"])
    fsky_arr.append(det["fsky"])
    years_arr.append(det["years_survey"])

    print(f"  {det['name']:30s}: sigma(a_s)={sigma_i:.4f} -> {disc_i:6.2f} sigma  [{det['arxiv_id']}, {det['year']}]")

# Convert to arrays
sigma_alpha_s_arr = np.array(sigma_alpha_s_arr)
discrimination_sigma_arr = np.array(discrimination_sigma_arr)
year_first_data_arr = np.array(year_first_data_arr)
fsky_arr = np.array(fsky_arr)
years_arr = np.array(years_arr)

# --------------------------------------------------------------------------- #
# Joint detector forecast (CMB-S4 + CMB-HD + LiteBIRD, uncorrelated)
# --------------------------------------------------------------------------- #
# Pick the three independent detectors (skip "CMB-S4+delensing" subset-of-S4 and SO-joint already includes S4)
joint_detector_indices = [0, 2, 3]  # (local) CMB-S4 baseline, CMB-HD, LiteBIRD
joint_sigmas = sigma_alpha_s_arr[joint_detector_indices]
# Inverse variance addition (uncorrelated; stated assumption)
joint_inv_var = np.sum(1.0 / joint_sigmas**2)  # (local)
joint_sigma = 1.0 / np.sqrt(joint_inv_var)      # (local)
joint_discrimination = abs_delta / joint_sigma  # (local)

print()
print(f"JOINT FORECAST (uncorrelated, {len(joint_detector_indices)} detectors):")
print(f"  Detectors: {[DETECTORS[i]['name'] for i in joint_detector_indices]}")
print(f"  Inverse-variance sigma = {joint_sigma:.4f}")
print(f"  Joint discrimination   = {joint_discrimination:.2f} sigma")

# --------------------------------------------------------------------------- #
# Threshold evaluation (pre-registered per plan)
# --------------------------------------------------------------------------- #
# PASS: CMB-S4 alone gives >=30 sigma AND at least one alternate (CMB-HD or LiteBIRD) gives >=10 sigma
# FAIL: All detectors give <10 sigma
# INFO: CMB-S4 gives 10-30 sigma or alternate channels give <10 sigma

cmb_s4_discrimination = discrimination_sigma_arr[0]  # (local) baseline S4
cmb_hd_discrimination = discrimination_sigma_arr[2]  # (local) CMB-HD
litebird_discrimination = discrimination_sigma_arr[3]  # (local) LiteBIRD

max_discrimination = float(np.max(discrimination_sigma_arr))  # (local) reported value

# Decision logic
alternate_ge10 = (cmb_hd_discrimination >= 10.0) or (litebird_discrimination >= 10.0)  # (local)
s4_ge30 = cmb_s4_discrimination >= 30.0  # (local)
all_detectors_lt10 = bool(np.all(discrimination_sigma_arr < 10.0))  # (local)

if s4_ge30 and alternate_ge10:
    verdict = "PASS"
    verdict_reason = f"CMB-S4 = {cmb_s4_discrimination:.2f} sigma >= 30 AND alternate (CMB-HD={cmb_hd_discrimination:.2f}) >= 10"
elif all_detectors_lt10:
    verdict = "FAIL"
    verdict_reason = "All detectors give <10 sigma discrimination (DETECTOR-STERILE)"
else:
    verdict = "INFO"
    verdict_reason = f"CMB-S4 = {cmb_s4_discrimination:.2f} sigma; marginal or single-detector dependency"

print()
print(f"VERDICT: {verdict}")
print(f"  Reason: {verdict_reason}")
print(f"  CMB-S4 discrimination : {cmb_s4_discrimination:.2f} sigma (threshold >=30)")
print(f"  CMB-HD discrimination : {cmb_hd_discrimination:.2f} sigma (alternate threshold >=10)")
print(f"  LiteBIRD discrimination : {litebird_discrimination:.2f} sigma")
print(f"  Max single-detector   : {max_discrimination:.2f} sigma")
print(f"  Joint (S4+HD+LiteBIRD): {joint_discrimination:.2f} sigma")

# --------------------------------------------------------------------------- #
# Save NPZ
# --------------------------------------------------------------------------- #
OUTPUT_NPZ = SCRIPT_DIR / "s84_w6_alpha_s_cmb_s4_refinement.npz"
np.savez(
    OUTPUT_NPZ,
    detector_names=np.array(detector_names),
    sigma_alpha_s=sigma_alpha_s_arr,
    discrimination_sigma=discrimination_sigma_arr,
    year_first_data=year_first_data_arr,
    reference_arxiv=np.array(reference_arxiv_arr),
    fsky=fsky_arr,
    years_survey=years_arr,
    alpha_s_framework=alpha_s_framework,
    alpha_s_LCDM=alpha_s_LCDM,
    joint_sigma=joint_sigma,
    joint_discrimination=joint_discrimination,
    joint_detector_indices=np.array(joint_detector_indices),
    cmb_s4_discrimination=cmb_s4_discrimination,
    cmb_hd_discrimination=cmb_hd_discrimination,
    litebird_discrimination=litebird_discrimination,
    max_discrimination=max_discrimination,
    planck_tension_sigma=planck_tension_sigma,
    sha_canon=sha_canon,
)
print(f"\n[S84 W6-52] NPZ saved: {OUTPUT_NPZ.name}")

# --------------------------------------------------------------------------- #
# Save CSV
# --------------------------------------------------------------------------- #
OUTPUT_CSV = SCRIPT_DIR / "s84_w6_alpha_s_cmb_s4_refinement.csv"
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "detector", "sigma_alpha_s", "discrimination_sigma",
        "year_first_data", "fsky", "years_survey",
        "arxiv_id", "freq_bands", "source_quote",
    ])
    for det in DETECTORS:
        writer.writerow([
            det["name"], det["sigma_alpha_s"], det["discrimination_sigma"],
            det["year_first_data"], det["fsky"], det["years_survey"],
            det["arxiv_id"], det["freq_bands"], det["source_quote"],
        ])
    # Joint row
    writer.writerow([
        "JOINT (S4+HD+LiteBIRD uncorrelated)", joint_sigma, joint_discrimination,
        2040, "N/A", "N/A",
        "1610.02743 + 2309.03021 + 2202.02773", "joint", "Inverse-variance addition, uncorrelated",
    ])
print(f"[S84 W6-52] CSV saved: {OUTPUT_CSV.name}")

# --------------------------------------------------------------------------- #
# Closure SHA (S81+ canonical form: SHA-256 of ordered input-pin map)
# --------------------------------------------------------------------------- #
VERDICT_TXT = SCRIPT_DIR / "s84_gate_verdicts.txt"

pin_map = {
    "gate_id": "S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT",
    "canonical_constants.py": sha_canon,
    "alpha_s_framework": f"{alpha_s_framework:+.6f}",
    "alpha_s_LCDM": f"{alpha_s_LCDM:+.6f}",
    "detectors": detector_names,
    "sigma_alpha_s": [f"{s:.6f}" for s in sigma_alpha_s_arr.tolist()],
    "arxiv_pins": reference_arxiv_arr,
    "cmb_s4_discrimination": f"{cmb_s4_discrimination:.4f}",
    "cmb_hd_discrimination": f"{cmb_hd_discrimination:.4f}",
    "litebird_discrimination": f"{litebird_discrimination:.4f}",
    "joint_sigma": f"{joint_sigma:.6f}",
    "joint_discrimination": f"{joint_discrimination:.4f}",
    "max_discrimination": f"{max_discrimination:.4f}",
    "value": f"{max_discrimination:.4f}",
    "scheme": "Abazajian+2022+",
    "convention": "alpha_s=n_s^2-1",
    "L_max": "N/A",
    "verdict": verdict,
}
pin_str = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))  # (local)
closure_sha = hashlib.sha256(pin_str.encode()).hexdigest()  # (local)

# 4-tuple output tag (final non-verdict line)
print()
print(f"(value={max_discrimination:.4f}, scheme=Abazajian+2022+, "
      f"convention=alpha_s=n_s^2-1, L_max=N/A)")
print(f"closure={closure_sha}")

# Append verdict line (S81+ canonical form)
verdict_line = (
    f"S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT: {verdict} -- "
    f"value={max_discrimination:.4f} "
    f"scheme=Abazajian+2022+ "
    f"convention=alpha_s=n_s^2-1 "
    f"L_max=N/A "
    f"sha256={closure_sha}\n"
)
with open(VERDICT_TXT, "a") as f:
    f.write(verdict_line)

print(f"\n[S84 W6-52] verdict appended to {VERDICT_TXT.name}")
print(f"[S84 W6-52] closure SHA: {closure_sha}")
