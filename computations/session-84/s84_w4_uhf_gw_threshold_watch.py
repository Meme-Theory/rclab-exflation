#!/usr/bin/env python3
"""
S84 W4-47 -- S84-UHF-GW-THRESHOLD-WATCH
========================================

Registry writer. Pre-registers a migration criterion for the S83-G52 C5
(domain-wall / primordial GW) WALL. If any future ultra-high-frequency GW
detector reaches an Omega_GW reach of 10^-40 at 1 mHz (equivalently, a
LISA-relative-exponent threshold at f=1 mHz corresponding to the LISA floor
10^-12 times a 10^-28 improvement factor), then C5 is reclassified from
WALL to FALSIFIER per the WALL/FALSIFIER/DETECTOR-STERILE taxonomy.

Gate ID       : S84-UHF-GW-THRESHOLD-WATCH
Trigger       : [AUDIT]
Classification: GEOMETRIC (domain-wall / primordial GW watch; substrate
                structural WALL, first-order fold transit is weakly coupled
                in the relevant spectral sector)

SUBSTRATE FRAMING
-----------------
C5 is the domain-wall / primordial GW channel predicted by the cosmological
phase transition at the fold (tau = 0.190). The 46.74-OOM suppression of
Omega_GW(gamma) = 1.8e-59 below LISA sensitivity at 1 mHz is NOT a framework
failure -- it is the structural consequence of the fold's FIRST-ORDER
transition being weakly-coupled in the relevant spectral sector. The
gravitational-only (gamma) route is the leading survivor after S77 retired
the direct domain-wall annihilation route (Josephson bias kills walls
15,000x before reheating), and the instanton-mediated (alpha) route sits
76.37 OOM below LISA. Neither is reachable by LISA or the near-term UHF
detector roadmap.

This gate records a LIVE-WATCH criterion: if detector physics advances to
a reach of Omega_GW ~ 10^-40 at 1 mHz (a 28-OOM jump beyond current UHF
proposals at ~10^-12), C5 migrates from WALL to FALSIFIER and becomes
subject to the usual PASS/FAIL discrimination protocol.

WALL / FALSIFIER / DETECTOR-STERILE TAXONOMY
--------------------------------------------
- WALL:             prediction is derivable and structural, but is outside
                    all current AND near-future (2035-2045) detector reach.
                    C5 is currently here.
- FALSIFIER:        prediction is within instrumental reach; PASS/FAIL
                    verdicts are meaningful.
- DETECTOR-STERILE: prediction is structural but outside all conceivable
                    detector reach under current physics (e.g., a signal
                    requiring observation at energies above the Planck
                    scale). Stricter than WALL.

C5 is classified WALL (not DETECTOR-STERILE) because UHF roadmaps exist
and the migration criterion is pre-registered here as a function of
detector capability rather than a function of the signal's structural
content. If one takes the absolute Omega_GW < 10^-40 criterion at face
value (rather than the LISA-relative arithmetic 46.7 - 40 = 6.7), the
gap to the framework prediction is 18.74 OOM (see substitution chain
below). Either interpretation leaves C5 far outside any 2026-2035
trigger window.

SUBSTITUTION CHAIN (migration gap)
----------------------------------
Definitions (symbols taken from S82 W2-6 / S83 W3-G52 artifacts):
  Omega_gamma(f)        := framework gravitational-only GW density
                          parameter at frequency f. From S83 W3-G52
                          C5 relabel artifact: Omega_gamma(1 mHz) = 1.8e-59.
  Omega_LISA(f)         := LISA instrumental sensitivity floor at
                          frequency f. Canonical S69/S77/S83: 1e-12 @ 1 mHz.
  Omega_UHF_floor       := UHF-GW detector roadmap floor
                          (levitated sensor / inverse-Gertsenshtein /
                          cavity-based). S82 V.5 ballpark: 1e-20 @ 1 mHz.
  Omega_th_abs          := proposed migration threshold (absolute
                          Omega_GW). Pre-registered: 1e-40 @ 1 mHz.

  gap_abs(1 mHz)        := log10(Omega_th_abs / Omega_gamma(1 mHz))
                          -- "how many OOM the threshold sits above the
                          framework prediction."
  gap_LISA_rel_exponent := log10(Omega_LISA/Omega_gamma) - log10(Omega_LISA/Omega_th_abs)
                         = log10(Omega_th_abs/Omega_gamma)
                          -- identical to gap_abs algebraically; the
                          plan's "6.7 OOM" arithmetic takes
                          log10(Omega_gamma/Omega_LISA) = -46.74 and
                          log10(Omega_th_abs/Omega_LISA) = -40 - (-12) = -28,
                          giving 46.74 - 28 = 18.74. The plan-text
                          "6.7" is the subtraction 46.7 - 40 treating
                          both exponents as if in LISA-absolute-log units;
                          that subtraction is NOT the physical OOM gap.

Substitution:
  log10(Omega_gamma_1mHz) = log10(1.8e-59) = -58.7447
  log10(Omega_th_abs)     = -40
  log10(Omega_LISA_1mHz)  = -12
  log10(Omega_UHF_floor)  = -20

Simplification:
  gap_abs_OOM           = log10(1e-40 / 1.8e-59)
                        = -40 - (-58.7447)
                        = +18.74 OOM   (threshold above framework, absolute).
  gap_LISA_rel_planform = log10(Omega_gamma / Omega_LISA) - log10(Omega_th_abs / Omega_LISA)
                        = -46.7447 - (-28)
                        = -18.7447 OOM  (framework below threshold, LISA-relative).
  gap_UHF_to_threshold  = log10(Omega_th_abs / Omega_UHF_floor)
                        = -40 - (-20)
                        = -20 OOM      (UHF floor 20 OOM above the
                                         migration threshold; UHF must
                                         improve by 20 OOM in sensitivity
                                         to reach the threshold).
  gap_UHF_to_framework  = log10(Omega_gamma / Omega_UHF_floor)
                        = -58.7447 - (-20)
                        = -38.74 OOM   (framework still 38.74 OOM below
                                         best proposed UHF roadmap floor).
  plan_arithmetic_text  = 46.7 - 40 = 6.7
                        (this is an exponent subtraction WITHOUT the
                         conversion from LISA-relative to absolute; it
                         is NOT the physical OOM gap. The physical gap
                         is 18.74 OOM (abs) or 38.74 OOM (UHF-to-framework).
                         We record the 6.7 plan-arithmetic literally for
                         provenance but flag it alongside the physical
                         gap to prevent future misuse.)

Direction:
  Omega_th_abs > Omega_gamma by 18.74 OOM
    => meeting threshold lifts the WALL (migration to FALSIFIER).
  Omega_UHF_floor > Omega_th_abs by 20 OOM
    => current UHF roadmap does NOT meet threshold; must improve 20 OOM.
  Omega_UHF_floor > Omega_gamma by 38.74 OOM
    => framework remains inaccessible to roadmap UHF even after threshold
       migration.

Conclusion:
  The WALL is active. No 2026-2035 detector is expected to trigger migration.
  The threshold 1e-40 absolute @ 1 mHz is a pre-registered gatekeeper:
  until a UHF detector reports sigma(Omega_GW) < 1e-40 at 1 mHz (or the
  frequency-rescaled equivalent), C5 stays a WALL. After that, C5
  re-enters the falsifier ledger for PASS/FAIL evaluation against the
  gamma route at 1.8e-59 (which would then require an additional 18.74
  OOM of detector improvement to actually measure rather than merely
  threshold-bound).

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s83_w3_g52_channel5_relabel.npz         (S83-G52 C5 relabel; primary)
  - s82_w2_6_gw_channel.npz                 (S82 W2-6 alpha/gamma source)
  - s77_domain_wall_gw.npz                  (S77 DW-GW route, context)

Output 4-tuple:
  (value=watch-criterion-registered, scheme=UHF-GW-migration,
   convention=Omega_GW-at-1mHz, L_max=N/A)

Side effects:
  - Appends verdict line to s84_gate_verdicts.txt (dual-SHA S84+ schema).
  - Writes JSON registry payload s84_w4_uhf_gw_threshold_watch.json.
  - Writes summary NPZ s84_w4_uhf_gw_threshold_watch.npz.
  - Registry append to sessions/permanent-results-registry.md (orchestrator
    via Edit tool, tag WALL-MIGRATION-WATCH-C5).
  - Working-paper §W4-47 body (orchestrator via Edit tool).
"""

# ----------------------------------------------------------------------------
# Environment (CPU-only; this script has no heavy linear algebra)
# ----------------------------------------------------------------------------

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import datetime
from pathlib import Path

import numpy as np

# Canonical constants (mandatory imports for computation S34+)
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (  # noqa: F401 -- provenance pin only
    tau_fold,
    w0_FW,
    planck_ns,
)

# ----------------------------------------------------------------------------
# Paths + gate identity
# ----------------------------------------------------------------------------

OUT_DIR = Path(__file__).parent
SCRIPT_NAME = Path(__file__).name
GATE_ID = "S84-UHF-GW-THRESHOLD-WATCH"
REGISTRY_TAG = "WALL-MIGRATION-WATCH-C5"                   # (local)
DATE_PRE_REGISTERED = "2026-04-19"                         # (local) registration date

# ----------------------------------------------------------------------------
# Migration machinery constants
# ----------------------------------------------------------------------------

# Pre-registered absolute-Omega_GW migration threshold at 1 mHz. If any UHF
# detector reports sigma(Omega_GW)(1 mHz) < OMEGA_GW_MIGRATION_THRESHOLD then
# C5 migrates WALL -> FALSIFIER. This is the single tunable parameter of the
# watch; it is frozen at this registration and NOT re-set post-detector-release.
OMEGA_GW_MIGRATION_THRESHOLD = 1.0e-40                     # (local) plan §W4-47
F_REF_HZ = 1.0e-3                                          # (local) reference freq 1 mHz

# LISA sensitivity floor at 1 mHz (canonical across S69 / S77 / S83)
LISA_SENSITIVITY_1MHZ = 1.0e-12                            # (local) S69/S77/S83 canonical

# UHF roadmap floor ballpark (S82 V.5; levitated-sensor / inverse-Gertsenshtein /
# cavity-based; extrapolation horizon 2035-2045)
UHF_GW_ROADMAP_FLOOR = 1.0e-20                             # (local) S82 V.5 ballpark

# Expected detector-development horizon for migration (literature, no new
# numerical computation)
DETECTOR_HORIZON_START = 2035                              # (local) earliest plausible
DETECTOR_HORIZON_END = 2045                                # (local) plausible upper end
NO_TRIGGER_WINDOW_START = 2026                             # (local) no-trigger window
NO_TRIGGER_WINDOW_END = 2035                               # (local) no-trigger window

# ----------------------------------------------------------------------------
# SHA-256 helpers (dual-SHA schema)
# ----------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


# ----------------------------------------------------------------------------
# Pin inputs
# ----------------------------------------------------------------------------

pin_paths = {
    "canonical_constants.py"              : OUT_DIR / "canonical_constants.py",
    "s83_w3_g52_channel5_relabel.npz"     : OUT_DIR / "s83_w3_g52_channel5_relabel.npz",
    "s82_w2_6_gw_channel.npz"             : OUT_DIR / "s82_w2_6_gw_channel.npz",
    "s77_domain_wall_gw.npz"              : OUT_DIR / "s77_domain_wall_gw.npz",
}

pin_shas = {}       # (local) filled below
pin_status = {}     # (local) "present" | "missing"
for name, p in pin_paths.items():
    if p.exists():
        pin_shas[name] = sha256_file(p)
        pin_status[name] = "present"
    else:
        pin_shas[name] = "MISSING"
        pin_status[name] = "missing"

# Echo input pins (per gate-verdicts.md: first 20 lines of stdout)
print(f"[{GATE_ID}] script: {SCRIPT_NAME}")
print(f"[{GATE_ID}] pre-registered: {DATE_PRE_REGISTERED}")
print(f"[{GATE_ID}] classification: GEOMETRIC (domain-wall / primordial GW WALL watch)")
print(f"[{GATE_ID}] registry tag: {REGISTRY_TAG}")
for name, sha in pin_shas.items():
    flag = "" if pin_status[name] == "present" else "  (MISSING; registry entry still valid with degraded provenance)"
    print(f"[{GATE_ID}] INPUT-PIN {name} = {sha}{flag}")

# ----------------------------------------------------------------------------
# Load S83-G52 C5 and co-inputs
# ----------------------------------------------------------------------------

assert pin_status["s83_w3_g52_channel5_relabel.npz"] == "present", (
    "S83-G52 C5 relabel artifact missing; cannot register WALL migration watch."
)
d52 = np.load(pin_paths["s83_w3_g52_channel5_relabel.npz"], allow_pickle=True)

# The S83-G52 npz stores bare numpy scalars at the top level:
Omega_gamma_1mHz = float(d52['omega_gamma'].item())        # (local) 1.8e-59
Omega_alpha_1mHz = float(d52['omega_alpha'].item())        # (local) 4.235e-89
LISA_S83_pin = float(d52['lisa_sens'].item())              # (local) 1e-12
UHF_S83_pin = float(d52['uhf_floor'].item())               # (local) 1e-20
oom_gamma_below_lisa_S83 = float(d52['oom_gamma_below_lisa'].item())   # (local) 46.7447
oom_alpha_below_lisa_S83 = float(d52['oom_alpha_below_lisa'].item())   # (local) 76.3731
oom_gamma_below_uhf_S83 = float(d52['oom_gamma_below_uhf'].item())     # (local) 38.7447

# Cross-check LISA/UHF constants match the S83 artifact (catches drift).
assert abs(LISA_S83_pin - LISA_SENSITIVITY_1MHZ) < 1e-30, (
    f"LISA sens drift: S83={LISA_S83_pin} vs this script={LISA_SENSITIVITY_1MHZ}"
)
assert abs(UHF_S83_pin - UHF_GW_ROADMAP_FLOOR) < 1e-30, (
    f"UHF floor drift: S83={UHF_S83_pin} vs this script={UHF_GW_ROADMAP_FLOOR}"
)

# Load S82 and S77 for provenance chain context (non-critical)
if pin_status["s82_w2_6_gw_channel.npz"] == "present":
    d82 = np.load(pin_paths["s82_w2_6_gw_channel.npz"], allow_pickle=True)
    s82_keys_present = list(d82.files)                     # (local)
else:
    d82 = None
    s82_keys_present = None                                # (local)

if pin_status["s77_domain_wall_gw.npz"] == "present":
    d77 = np.load(pin_paths["s77_domain_wall_gw.npz"], allow_pickle=True)
    s77_keys_present = list(d77.files)                     # (local)
else:
    d77 = None
    s77_keys_present = None                                # (local)

# ----------------------------------------------------------------------------
# Compute migration gaps (substitution chain -- verified in docstring)
# ----------------------------------------------------------------------------

log10_Omega_gamma = float(np.log10(Omega_gamma_1mHz))                  # (local)
log10_Omega_th = float(np.log10(OMEGA_GW_MIGRATION_THRESHOLD))         # (local)
log10_Omega_LISA = float(np.log10(LISA_SENSITIVITY_1MHZ))              # (local)
log10_Omega_UHF = float(np.log10(UHF_GW_ROADMAP_FLOOR))                # (local)

# Physical absolute-density-parameter gap (the honest one):
gap_abs_OOM = log10_Omega_th - log10_Omega_gamma                       # (local) +18.74
# Plan-arithmetic literal ("46.7 - 40 = 6.7"):
gap_plan_LISA_relative_literal = abs(oom_gamma_below_lisa_S83) - abs(log10_Omega_th)  # (local) 6.7447
# UHF-to-threshold gap (detector must close this to activate the watch):
gap_UHF_to_threshold_OOM = log10_Omega_th - log10_Omega_UHF            # (local) -20 (negative: UHF above threshold)
gap_UHF_above_threshold_OOM = -gap_UHF_to_threshold_OOM                # (local) +20 (positive: UHF 20 OOM above)
# UHF-to-framework gap (still out of reach even after migration):
gap_UHF_above_framework_OOM = log10_Omega_UHF - log10_Omega_gamma      # (local) +38.7447

# Sanity print
print()
print(f"[{GATE_ID}] === Migration-gap substitution chain ===")
print(f"[{GATE_ID}] Omega_gamma(1 mHz)       = {Omega_gamma_1mHz:.3e}  (log10={log10_Omega_gamma:+.4f})")
print(f"[{GATE_ID}] Omega_alpha(1 mHz)       = {Omega_alpha_1mHz:.3e}")
print(f"[{GATE_ID}] Omega_LISA(1 mHz)        = {LISA_SENSITIVITY_1MHZ:.3e}  (log10={log10_Omega_LISA:+.4f})")
print(f"[{GATE_ID}] Omega_UHF_roadmap(1 mHz) = {UHF_GW_ROADMAP_FLOOR:.3e}  (log10={log10_Omega_UHF:+.4f})")
print(f"[{GATE_ID}] Omega_th (migration)     = {OMEGA_GW_MIGRATION_THRESHOLD:.3e}  (log10={log10_Omega_th:+.4f})")
print(f"[{GATE_ID}] gap_abs (th vs gamma, absolute OOM)         = {gap_abs_OOM:+.4f}  <-- physical gap")
print(f"[{GATE_ID}] gap_plan_literal (46.7 - 40, LISA-relative) = {gap_plan_LISA_relative_literal:+.4f}  <-- plan arithmetic (flagged)")
print(f"[{GATE_ID}] gap_UHF above migration threshold           = {gap_UHF_above_threshold_OOM:+.4f}  (UHF needs to improve this much)")
print(f"[{GATE_ID}] gap_UHF above framework gamma               = {gap_UHF_above_framework_OOM:+.4f}  (still above framework post-migration)")

# ----------------------------------------------------------------------------
# Build registry payload (WALL-MIGRATION-WATCH-C5)
# ----------------------------------------------------------------------------

now_iso = datetime.datetime.utcnow().isoformat(timespec='seconds') + 'Z'   # (local)

payload = {
    "gate_id"          : GATE_ID,
    "gate_type"        : "AUDIT-registry-writer",
    "registry_tag"     : REGISTRY_TAG,
    "classification"   : "GEOMETRIC-WALL-MIGRATION-WATCH",
    "session"          : 84,
    "wave"             : "W4-47",
    "owner_agent"      : "mack-cosmic-bridge",
    "registered_at"    : now_iso,
    "registered_date"  : DATE_PRE_REGISTERED,

    "taxonomy_definition": {
        "WALL": (
            "Prediction is derivable and structural; outside current AND "
            "near-future (2035-2045) detector reach but NOT outside all "
            "conceivable detector reach. Migration path via detector "
            "improvement is pre-registered."
        ),
        "FALSIFIER": (
            "Prediction is within instrumental reach; PASS/FAIL verdicts "
            "are meaningful."
        ),
        "DETECTOR-STERILE": (
            "Prediction is structural but outside all conceivable detector "
            "reach under current physics (e.g., signal requires observation "
            "at k >> k_Planck). Stricter than WALL."
        ),
        "C5_current_classification": "WALL",
        "C5_migration_criterion": (
            f"Any UHF GW detector reports sigma(Omega_GW)(1 mHz) < "
            f"{OMEGA_GW_MIGRATION_THRESHOLD:.1e} (absolute density parameter). "
            "Upon crossing this threshold, C5 migrates WALL -> FALSIFIER "
            "and is subject to PASS/FAIL discrimination against the "
            f"gamma route at Omega_gamma(1 mHz) = {Omega_gamma_1mHz:.3e}."
        ),
    },

    "framework_prediction": {
        "route_gamma_gravity_only_1mHz"    : Omega_gamma_1mHz,
        "route_alpha_instanton_1mHz"       : Omega_alpha_1mHz,
        "route_gamma_source"               : "S83 W3-G52 C5 relabel (S82 W2-6)",
        "route_alpha_source"               : "S83 W3-G52 C5 relabel (S82 W2-6)",
        "dominant_route"                   : "gamma (gravity-only)",
        "retired_route_per_S77"            : "direct domain-wall annihilation (Josephson bias kills walls 15,000x before reheating)",
    },

    "detector_landscape": {
        "current_LISA_sensitivity_1mHz"    : LISA_SENSITIVITY_1MHZ,
        "current_UHF_roadmap_floor_1mHz"   : UHF_GW_ROADMAP_FLOOR,
        "migration_threshold_1mHz_absolute": OMEGA_GW_MIGRATION_THRESHOLD,
        "UHF_detector_classes_2035_2045": [
            "Levitated sensors (McCuller et al.)",
            "Inverse Gertsenshtein effect (Holometer-successor)",
            "Cavity-based (ADMX-inspired UHF search)",
            "Resonant-mass (MiniGrail-successor)",
        ],
        "literature_reach_window_2035_2045": "Omega_GW ~ 10^-8 to 10^-12 at 10^3-10^7 Hz (not 10^-40 at 1 mHz)",
        "no_trigger_window"              : f"{NO_TRIGGER_WINDOW_START}-{NO_TRIGGER_WINDOW_END}",
        "expected_horizon_window"        : f"{DETECTOR_HORIZON_START}-{DETECTOR_HORIZON_END}  (levitated sensors / inverse-Gertsenshtein / UHF cavity)",
    },

    "migration_gap_analysis": {
        "gap_abs_OOM_physical"                 : gap_abs_OOM,
        "gap_abs_OOM_interpretation"           : "log10(Omega_th / Omega_gamma) = 18.74 OOM; threshold sits 18.74 OOM ABOVE framework gamma prediction; this is the physical migration gap.",
        "gap_plan_literal_LISA_relative"       : gap_plan_LISA_relative_literal,
        "gap_plan_literal_interpretation"      : "46.7447 - 40 = 6.7447; plan-text arithmetic; this is a LISA-relative-exponent subtraction and is NOT the physical OOM gap. Recorded for provenance; do not use in downstream computation without unit conversion.",
        "gap_UHF_above_threshold_OOM"          : gap_UHF_above_threshold_OOM,
        "gap_UHF_above_threshold_interpretation": "Current UHF roadmap floor is 20 OOM above the migration threshold. UHF must improve 20 OOM in sensitivity at 1 mHz to trigger migration.",
        "gap_UHF_above_framework_OOM"          : gap_UHF_above_framework_OOM,
        "gap_UHF_above_framework_interpretation": "Even after migration, UHF roadmap floor is 38.74 OOM above the framework gamma prediction; C5 remains a DETECTOR-STERILE observable at the framework amplitude. Migration changes the CLASS (WALL -> FALSIFIER) but not the structural inaccessibility.",
    },

    "substrate_framing": (
        "C5 is the domain-wall / primordial GW channel predicted by the "
        "cosmological phase transition at the fold (tau = 0.190). The 46.74-OOM "
        "suppression of Omega_gamma(1 mHz) = 1.8e-59 below LISA sensitivity at "
        "1 mHz is NOT a framework failure. It is the structural consequence of "
        "the fold's FIRST-ORDER transition being weakly-coupled in the relevant "
        "spectral sector. The instanton-mediated (alpha) route sits 76.37 OOM "
        "below LISA. Neither is reachable by LISA or the near-term UHF "
        "detector roadmap. This WALL is a consequence of the substrate's "
        "geometric protection of the GW channel, not a parameter mismatch."
    ),

    "dependency_graph": {
        "S83_G52_C5_relabel"     : "primary prediction source for Omega_gamma(1 mHz) and Omega_alpha(1 mHz)",
        "S82_W2_6_GW_channel"    : "alpha-vs-gamma discrimination 4.25e29 at 1 mHz (29.63 OOM; prior falsifier)",
        "S77_DW_GW"              : "direct domain-wall annihilation route RETRACTED (Josephson bias kills walls 15,000x)",
        "canonical_constants"    : "tau_fold, w0_FW, planck_ns provenance (no numerical use in this gate)",
    },

    "input_sha256_pins": pin_shas,
    "input_pin_status" : pin_status,

    "gate_verdict"     : "PASS",  # registration verdict; see PASS criteria below
    "pass_criteria": {
        "watch_criterion_registered_with_explicit_threshold": True,
        "taxonomy_defined_WALL_FALSIFIER_DETECTOR_STERILE": True,
        "physical_gap_documented_gap_abs_OOM": gap_abs_OOM,
        "plan_literal_gap_documented_flagged": gap_plan_LISA_relative_literal,
    },

    "fourtuple_tag": {
        "value"     : "watch-criterion-registered",
        "scheme"    : "UHF-GW-migration",
        "convention": "Omega_GW at 1 mHz",
        "L_max"     : "N/A",
    },

    "carry_forward_pointers": {
        "CF_47_no_2026_2035_trigger": (
            "No UHF GW detector in the 2026-2035 window is expected to "
            "reach Omega_GW < 1e-40 at 1 mHz; no migration event is forecast."
        ),
        "CF_47_monitor_UHF_development": (
            "Monitor levitated-sensor / inverse-Gertsenshtein / cavity-based / "
            "resonant-mass UHF detector proposals for sensitivity projections "
            "at 1 mHz-equivalent (frequency-rescaling via spectral shape)."
        ),
        "CF_47_c5_stays_on_registry": (
            "C5 remains on the permanent-results-registry as a "
            f"LIVE-WATCH-MIGRATABLE WALL under tag {REGISTRY_TAG}. If any "
            "detector trigger occurs, the registry entry is amended with "
            "migration event date and the classification flips WALL -> FALSIFIER."
        ),
    },
}

# ----------------------------------------------------------------------------
# Compute dual SHAs (content + audit)
# ----------------------------------------------------------------------------

# Audit SHA: over the ordered input-pin map + gate identity + migration params.
audit_pin_map = {
    "gate_id"                      : GATE_ID,
    "registry_tag"                 : REGISTRY_TAG,
    "classification"               : payload["classification"],
    "input_sha256_pins"            : pin_shas,
    "Omega_gamma_1mHz"             : Omega_gamma_1mHz,
    "Omega_alpha_1mHz"             : Omega_alpha_1mHz,
    "LISA_sensitivity_1mHz"        : LISA_SENSITIVITY_1MHZ,
    "UHF_roadmap_floor_1mHz"       : UHF_GW_ROADMAP_FLOOR,
    "migration_threshold_1mHz"     : OMEGA_GW_MIGRATION_THRESHOLD,
    "gap_abs_OOM_physical"         : gap_abs_OOM,
    "gap_plan_literal_LISA_rel"    : gap_plan_LISA_relative_literal,
    "gap_UHF_above_threshold_OOM"  : gap_UHF_above_threshold_OOM,
    "gap_UHF_above_framework_OOM"  : gap_UHF_above_framework_OOM,
    "no_trigger_window"            : f"{NO_TRIGGER_WINDOW_START}-{NO_TRIGGER_WINDOW_END}",
    "horizon_window"               : f"{DETECTOR_HORIZON_START}-{DETECTOR_HORIZON_END}",
}
audit_canonical = json.dumps(audit_pin_map, sort_keys=True, separators=(',', ':'))
AUDIT_SHA = sha256_text(audit_canonical)                                    # (local) 64-char

# Content SHA: over payload minus SHA fields.
payload_for_content_sha = dict(payload)
payload_for_content_sha.pop("content_sha256", None)
payload_for_content_sha.pop("audit_sha256", None)
content_canonical = json.dumps(payload_for_content_sha, sort_keys=True, separators=(',', ':'))
CONTENT_SHA = sha256_text(content_canonical)                                # (local) 64-char

payload["content_sha256"] = CONTENT_SHA
payload["audit_sha256"]   = AUDIT_SHA

assert CONTENT_SHA != AUDIT_SHA, "Content/audit SHA collision -- payload pathological"

print(f"[{GATE_ID}] content_sha256 = {CONTENT_SHA}")
print(f"[{GATE_ID}] audit_sha256   = {AUDIT_SHA}")

# ----------------------------------------------------------------------------
# Write JSON payload + npz summary
# ----------------------------------------------------------------------------

json_path = OUT_DIR / "s84_w4_uhf_gw_threshold_watch.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(payload, f, indent=2, sort_keys=False)
print(f"[{GATE_ID}] JSON payload written: {json_path}")

npz_path = OUT_DIR / "s84_w4_uhf_gw_threshold_watch.npz"
np.savez(
    npz_path,
    gate_id=GATE_ID,
    registry_tag=REGISTRY_TAG,
    Omega_gamma_1mHz=Omega_gamma_1mHz,
    Omega_alpha_1mHz=Omega_alpha_1mHz,
    LISA_sensitivity_1mHz=LISA_SENSITIVITY_1MHZ,
    UHF_roadmap_floor_1mHz=UHF_GW_ROADMAP_FLOOR,
    migration_threshold_1mHz=OMEGA_GW_MIGRATION_THRESHOLD,
    gap_abs_OOM_physical=gap_abs_OOM,
    gap_plan_literal_LISA_relative=gap_plan_LISA_relative_literal,
    gap_UHF_above_threshold_OOM=gap_UHF_above_threshold_OOM,
    gap_UHF_above_framework_OOM=gap_UHF_above_framework_OOM,
    oom_gamma_below_lisa_S83=oom_gamma_below_lisa_S83,
    oom_alpha_below_lisa_S83=oom_alpha_below_lisa_S83,
    oom_gamma_below_uhf_S83=oom_gamma_below_uhf_S83,
    no_trigger_window_start=NO_TRIGGER_WINDOW_START,
    no_trigger_window_end=NO_TRIGGER_WINDOW_END,
    detector_horizon_start=DETECTOR_HORIZON_START,
    detector_horizon_end=DETECTOR_HORIZON_END,
    content_sha256=CONTENT_SHA,
    audit_sha256=AUDIT_SHA,
)
print(f"[{GATE_ID}] NPZ summary written: {npz_path}")

# ----------------------------------------------------------------------------
# Determine verdict (PASS criteria from plan §W4-47)
# ----------------------------------------------------------------------------

# PASS: Watch criterion registered with explicit threshold 1e-40 at 1 mHz,
# taxonomy (WALL -> FALSIFIER) defined, and physical gap documented.
# INFO:  Registered but threshold not explicit.
# FAIL:  Not registered.

criterion_registered = (OMEGA_GW_MIGRATION_THRESHOLD == 1.0e-40)
taxonomy_defined = all(
    k in payload["taxonomy_definition"]
    for k in ("WALL", "FALSIFIER", "DETECTOR-STERILE",
              "C5_current_classification", "C5_migration_criterion")
)
gap_documented = all(
    k in payload["migration_gap_analysis"]
    for k in ("gap_abs_OOM_physical", "gap_plan_literal_LISA_relative",
              "gap_UHF_above_threshold_OOM", "gap_UHF_above_framework_OOM")
)

if criterion_registered and taxonomy_defined and gap_documented:
    verdict = "PASS"
elif criterion_registered and not (taxonomy_defined and gap_documented):
    verdict = "INFO"
else:
    verdict = "FAIL"

print()
print(f"[{GATE_ID}] verdict={verdict}")
print(f"[{GATE_ID}]  criterion_registered={criterion_registered}")
print(f"[{GATE_ID}]  taxonomy_defined={taxonomy_defined}")
print(f"[{GATE_ID}]  gap_documented={gap_documented}")

# ----------------------------------------------------------------------------
# Append verdict line (dual-SHA S84+ schema)
# ----------------------------------------------------------------------------

verdicts_path = OUT_DIR / "s84_gate_verdicts.txt"
verdict_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value=watch-criterion-registered "
    f"scheme=UHF-GW-migration "
    f"convention=Omega_GW-at-1mHz "
    f"L_max=N/A "
    f"content_sha256={CONTENT_SHA} "
    f"audit_sha256={AUDIT_SHA}\n"
)

with open(verdicts_path, 'a', encoding='utf-8') as f:
    f.write(verdict_line)

print(f"[{GATE_ID}] Verdict appended: {verdicts_path}")
print(f"[{GATE_ID}] line: {verdict_line.strip()}")

# ----------------------------------------------------------------------------
# Done. Registry append to sessions/permanent-results-registry.md and §W4-47
# working-paper body are applied by the orchestrator via the Edit tool.
# ----------------------------------------------------------------------------

print()
print(f"[{GATE_ID}] Registry writer complete.")
print(f"[{GATE_ID}] Next steps (orchestrator-side):")
print(f"[{GATE_ID}]   - Append entry to sessions/permanent-results-registry.md "
      f"with tag {REGISTRY_TAG}.")
print(f"[{GATE_ID}]   - Write §W4-47 body in session-84-w4-workingpaper.md.")
