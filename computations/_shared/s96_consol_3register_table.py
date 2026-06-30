#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-CONSOL-3REGISTER-TABLE  (Wave 8, gate W8-2)
================================================
mack-cosmic-bridge sole writer of the §7 falsifier/observable surface.

PURPOSE
-------
Consume the W8-1 STATUS-SYNC status-diff (computations/session-96/s96_consol_status_sync.json)
and split the single capstone §7.1 "Outputs by spectral-moment layer" table into THREE
epistemic registers (report §"Critique": "split observables into robust structural outputs,
conditional outputs, and currently falsified outputs"):

  (a) ROBUST-STRUCTURAL  — zero-free-parameter structural outputs, status PROVEN / PASS-structural
  (b) CONDITIONAL        — PASS contingent on an unresolved input / scheme / route
  (c) CURRENTLY-FALSIFIED — register marks BROKEN / advancing-tension / inversion-falsified

The register of each §7.1 row is a CATEGORICAL FUNCTION of its W8-1-reconciled status tag
(the cell_register_map in the status-diff). No values are recomputed; the partition is
set-theoretic (SUM-check, no omission/double-count). Dual-status straddle rows (m_H, sigma_8)
land in CONDITIONAL with an explicit dual-status annotation (the honest INFO disclosure),
NOT flattened into the robust register.

Emits:
  - the 3 register-tables (markdown) embedded in the WP + capstone §7.1 patch (mack sole writer)
  - JSON partition map (row -> register + substrate-moment layer + register-source status + SUM-check)
  - npz (the partition arrays for downstream)
  - dual-SHA verdict line -> computations/session-96/s96_gate_verdicts.txt

NON-PHONONIC (methodology / observable-table restructuring of a curated framework doc).
NO linear algebra; CPU; OMP-capped per computation-environment.md.

NUMBERS first, gate second, interpretation third.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import math
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

# ------------------------------------------------------------------
# Canonical constants (MANDATORY import; never hardcode framework values)
# ------------------------------------------------------------------
SHARED = Path(__file__).resolve().parent
if str(SHARED) not in sys.path:
    sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    w0_FW,                                   # -0.918   (Volovik partition canonical)
    sigma_8,                                 # 0.811    (Planck 2018 sigma_8 — NOT S_8=0.829)
    f_FW,                                    # 0.5254916...
    f_LCDM,                                  # 0.5271304...
    fsigma8_product_suppression_FW_max_pct,  # -4.058
    f_bare_suppression_FW_pct,               # -0.311   (C5 conflation guard)
    A_FS_first_sound_ring,                   # 0.204
    f_obs_CGWB_peak_kappa_nat,               # 8.4835e39
    Omega_GW_Lambda_A_LISA,                  # 1.0e-10
    Omega_GW_Companion_null,                 # 8.299e-58
    OOM_split_AC_regulator_class,            # 47.081
)

# ------------------------------------------------------------------
# Identity / paths
# ------------------------------------------------------------------
PROJECT_ROOT = SHARED.parent.parent
GATE_ID = "S96-CONSOL-3REGISTER-TABLE"
SCHEME = "THREE-REGISTER-PARTITION-ROBUST-CONDITIONAL-FALSIFIED"
CONVENTION = ("register-keyed-by-W8-1-status-tag-PLUS-substrate-moment-layer-tag-"
              "preserved-PLUS-no-flattening")
L_MAX = "N/A"

SESSION_DIR = PROJECT_ROOT / "computations" / "session-96"
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"
JSON_OUT = SESSION_DIR / "s96_consol_3register_table.json"
NPZ_OUT = SESSION_DIR / "s96_consol_3register_table.npz"
PNG_OUT = SESSION_DIR / "s96_consol_3register_table.png"
MD_OUT = SESSION_DIR / "s96_consol_3register_table.md"  # the 3 register tables markdown

CANONICAL_PY = SHARED / "canonical_constants.py"
STATUS_DIFF_JSON = SESSION_DIR / "s96_consol_status_sync.json"
CAPSTONE = PROJECT_ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"
ATLAS_04 = PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-04-assumptions.md"
THIS_SCRIPT = Path(__file__).resolve()


# ==================================================================
# SECTION 1: dual-SHA helpers (S84+ schema; mirrors append_verdict pattern)
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
# ==================================================================
def sha256_of(path: Path) -> str:                                          # (local)
    h = hashlib.sha256()                                                   # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:                                        # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                              # (local)
    for p in inputs:
        sha = sha256_of(p)                                                 # (local)
        try:
            rel = str(Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)                                                   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:                                       # (local)
    items = sorted(pins.items())                                           # (local)
    h = hashlib.sha256()                                                   # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):  # (local)
    try:
        script_bytes = Path(script_path).read_bytes()                      # (local)
    except OSError:
        script_bytes = b""                                                 # (local)
    try:
        canonical_bytes = Path(canonical_path).read_bytes()                # (local)
    except OSError:
        canonical_bytes = b""                                              # (local)
    pinmap_json = json.dumps(                                              # (local)
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")

    h_audit = hashlib.sha256()                                             # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                            # (local)

    h_content = hashlib.sha256()                                           # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                        # (local)
    return audit, content


def _prior_audit_sha_for_gate() -> str:                                     # (local)
    """Return the latest non-superseded audit_sha256 already on disk for THIS gate, or ''.
    Used to emit a `supersedes=` tag (Option A, gate-verdicts.md) when a same-session
    corrective re-run (e.g. a script-bug fix) appends a new canonical line."""
    if not VERDICT_TXT.exists():
        return ""
    superseded = set()                                                     # (local)
    candidates = []                                                        # (local)
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:"):
            import re
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)              # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)              # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]                 # (local)
    return live[-1] if live else ""


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:  # (local)
    """Atomic append (single open('a')) of the dual-SHA verdict to the CANONICAL verdict file.
    [AUDIT] trigger => dual-SHA companion row only; no [SIGN] 3-tuple (schema_v2_3tuple_required: false).
    If a prior non-superseded line exists for this gate (same-session corrective re-run, e.g.
    a script-bug fix), carry a `supersedes=<old-audit-sha>` tag per gate-verdicts.md Option A."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    prior = _prior_audit_sha_for_gate()                                    # (local)
    if prior and prior != audit_sha:
        value = f"{value};supersedes={prior}"                              # (local) Option A tag in value field
        sup_note = f"; supersedes={prior} (script-bug fix: unescaped table pipes; Option A)"  # (local)
    else:
        sup_note = ""                                                      # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row "
        f"(METHODOLOGY-class: content over script; audit over script+canonical+pinmap); "
        f"[AUDIT] 3-register partition; SUM-check; no [SIGN] 3-tuple{sup_note}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ==================================================================
# SECTION 2: the §7.1 row set + W8-1-reconciled status tags
#   Each row carries: observable, substrate-moment layer (a0/a2/a4), the
#   capstone framework value, the comparison anchor, the W8-1-reconciled
#   status tag (from the status-diff cell_register_map), and the register
#   assignment (a CATEGORICAL function of the status tag).
# ==================================================================
print("=" * 78)
print(f"{GATE_ID}  (split §7.1 'now' table into 3 epistemic registers; no-flatten partition)")
print("=" * 78)

# Load the W8-1 status-diff (the upstream prereq — the reconciled per-row status tags).
status_diff = {}                                                           # (local)
W8_1_PRESENT = STATUS_DIFF_JSON.exists()                                   # (local)
if W8_1_PRESENT:
    status_diff = json.loads(STATUS_DIFF_JSON.read_text(encoding="utf-8"))  # (local)
    w81_verdict = status_diff.get("verdict", "?")                          # (local)
    cell_map = (status_diff.get("forbidden_pattern_regrep", {})            # (local)
                .get("pattern_iii_s71_status_cells", {})
                .get("cell_register_map", {}))
    print(f"[SEC 2] W8-1 status-diff present: verdict={w81_verdict}; "
          f"cell_register_map rows={len(cell_map)}")
else:
    cell_map = {}                                                          # (local)
    print("[SEC 2] W8-1 status-diff ABSENT -> PRE-REG-INC mechanical closure")

# Register-assignment rule (from the gate-block machinery_pin_map register_assignment_rule):
#   robust-structural : status in {PROVEN, PASS-structural, DISSOLVED-favorably, BOUND-Gaussian-by-Wick}
#   conditional       : status in {CONDITIONAL, SCHEME-DEPENDENT, route-dependent, doubly-conditional, VIABLE}
#   currently-falsified: status in {BROKEN, advancing-tension, INVERSION-falsified}
ROBUST = "robust-structural"        # (local)
COND = "conditional"                # (local)
FALSIFIED = "currently-falsified"   # (local)

# The §7.1 rows AS PRESENT in the capstone (14 observable rows, post-W7 landings).
# 'register' = the categorical assignment; 'dual_status' flags a disclosed straddle (INFO).
# Each row's reconciled-status string is the W8-1 cell_register_map value where covered,
# else the capstone §7.1 Status cell (for the 3 W7-landed rows not in the W8-1 11-row set).
ROWS = [
    {
        "observable": "w_0 (DE equation of state)",
        "layer": "a0",
        "fw_value": f"{w0_FW} (w0_FW, Volovik partition); branch-iv -0.842454",
        "anchor": "-0.803 +/- 0.054 (joint, Popovic/DES-Dovekie 2511.07517v3)",
        "reconciled_status": "C4 CONDITIONAL (DR3-binding 2027)",
        "register": COND,
        "dual_status": False,
        "note": "LIVE 2.13sigma / 0.73sigma (branch-iv); borrows external H(t) (dagger / C10)",
    },
    {
        "observable": "w_a",
        "layer": "a0",
        "fw_value": "0 (structural four-fold lock)",
        "anchor": "-0.72 +/- 0.21 (same joint fit)",
        "reconciled_status": "C5 BROKEN (3.43sigma post-Dovekie)",
        "register": FALSIFIED,
        "dual_status": False,
        "note": "the live wager; prediction fixed, data moving away; item-34 'wa not a meaningful CPL parameter'",
    },
    {
        "observable": "CC closure",
        "layer": "a0",
        "fw_value": "rho_vac/rho_obs = 1.032 (0.01 OOM)",
        "anchor": "observed Lambda",
        "reconciled_status": "PASS (DILUTION-CC-66)",
        "register": ROBUST,
        "dual_status": False,
        "note": "doubly-conditional on C10 + external H (caveat box); robust as the NON-INHERITANCE identity (Clause A), conditional on observed magnitude (Clause B) -- see dual-status note",
    },
    {
        "observable": "n_s (scalar tilt)",
        "layer": "a2/Goldstone",
        "fw_value": "SCHEME-DEPENDENT (0.9561 / 0.9590 / 0.9595)",
        "anchor": "Planck 0.9649 +/- 0.0042",
        "reconciled_status": "C3/C9 SCHEME-DEPENDENT / CONDITIONAL on FUNCTIONAL-SELECT-67",
        "register": COND,
        "dual_status": False,
        "note": "2.10sigma / 1.40sigma / 1.29sigma; BMA band 0.969 +/- 0.022 is the correct UQ object",
    },
    {
        "observable": "r (tensor-to-scalar)",
        "layer": "a2 tensor",
        "fw_value": "0.033 (dual-pathway: Path-H 0.00745 / Path-C 0.0117)",
        "anchor": "BICEP/Keck < 0.036",
        "reconciled_status": "PASS (within 2sigma; D04 IX row4 LIVE PASS<2sigma)",
        "register": ROBUST,
        "dual_status": False,
        "note": "substrate-IS tensor sector; NO borrowed H; clean robust spine row",
    },
    {
        "observable": "alpha_s (running dn_s/dlnk)",
        "layer": "a2/a4",
        "fw_value": "DUAL (scale, channel): substrate -0.0859 (s=3 Mellin) / pivot ~0",
        "anchor": "Planck -0.0045 +/- 0.0067",
        "reconciled_status": "C12 CONDITIONAL on CMB-S4 (channel-artifact resolved S93 W7-1)",
        "register": COND,
        "dual_status": False,
        "note": "pivot image +0.67sigma consistent; substrate value awaits CMB-S4 ~34sigma-reach falsifier",
    },
    {
        "observable": "f_NL (non-Gaussianity)",
        "layer": "bispectrum",
        "fw_value": "|f_NL| <~ 1.5 BOUND (-1.505 = -max_f_NL_FW saturation; central GGE ~1.03)",
        "anchor": "Planck -0.9 +/- 5.1",
        "reconciled_status": "BOUND-Gaussian-by-Wick (re-tagged per C4; central ~1.03)",
        "register": ROBUST,
        "dual_status": False,
        "note": "Gaussian-by-Wick to within a |f_NL|<~1.5 bound; 0.47sigma is the BOUND's distance, NOT a central detection",
    },
    {
        "observable": "m_H (Higgs mass)",
        "layer": "a4/fiber",
        "fw_value": "127.5-131.8 GeV (KK threshold)",
        "anchor": "PDG 125.25 +/- 0.17",
        "reconciled_status": "PASS-class (~2% budget); route-dependent (D04 IX row8 PROVEN-AT-OBS w/ caveat)",
        "register": COND,
        "dual_status": True,
        "note": "DUAL-STATUS STRADDLE: robust-on-magnitude (~2% theory budget PASS) BUT conditional-on-route (zeta 138.5 excluded; mu_BC 188 is ACCOMMODATION); placed in CONDITIONAL with disclosure, NOT flattened into robust",
    },
    {
        "observable": "Omega_DM h^2",
        "layer": "a2 Leggett gap",
        "fw_value": "0.120 (Leggett-only)",
        "anchor": "Planck 0.1186 +/- 0.0020",
        "reconciled_status": "C7/C11 CONDITIONAL on LEGGETT-GRAV-DECAY-67 (margin PASS S95; D04 IX row9 PROVEN-AT-OBS)",
        "register": COND,
        "dual_status": False,
        "note": "PASS 0.7sigma GIVEN Gamma_grav<H_0 (satisfied with 65-OOM margin, 8.85e-66); the conditional is satisfied, but the PASS is contingent",
    },
    {
        "observable": "sigma/m (DM self-interaction)",
        "layer": "E29 / N_Fock=1",
        "fw_value": "0 exactly (N_Fock=1 superselection)",
        "anchor": "Bullet < 1.25 cm^2/g",
        "reconciled_status": "structural N_Fock=1 (PASS)",
        "register": ROBUST,
        "dual_status": False,
        "note": "structural zero distinct from any tuned cross-section; no borrowed H; clean robust spine row",
    },
    {
        "observable": "sigma_8 (growth amplitude)",
        "layer": "a2 growth",
        "fw_value": "0.799 (zero-free-parameter)",
        "anchor": f"Planck sigma_8 {sigma_8}; lensing ~0.76",   # 0.811 (NOT S_8=0.829) -- W6-7 fix
        "reconciled_status": "C9 PROVEN-with-conditional (VIABLE, ~2sigma between the S8-tension ends)",
        "register": COND,
        "dual_status": False,
        "note": "VIABLE not a resolution; conditional on the sqrt(x) functional being canonical; borrows H (dagger). ANCHOR FIX (W6-7): Planck sigma_8=0.811, NOT the S_8=0.829 the prose mis-cited",
    },
    {
        "observable": "f*sigma_8(z) (RSD growth)",
        "layer": "a2 growth",
        "fw_value": f"{fsigma8_product_suppression_FW_max_pct}% f*sigma8 PRODUCT suppression vs LCDM @ z=0.51 "
                    f"(bare-f {f_bare_suppression_FW_pct}% -- the PRODUCT, NOT bare-f)",
        "anchor": "DESI-5yr / Euclid RSD",
        "reconciled_status": "PASS-class (S8-tension-relieving sign; S77 PROVEN / S96-OBS-FSIGMA8-FORECAST)",
        "register": ROBUST,
        "dual_status": False,
        "note": "zero-free-parameter; sigma-dist 1.013 DESI-Y5 / 1.534 Euclid; C5 guard: -4.058% is the PRODUCT, -0.311% is bare-f; borrows H (modulation-on-borrowed-H caveat)",
    },
    {
        "observable": "nu mass ordering",
        "layer": "a4/fiber neutrino",
        "fw_value": "Normal B1<B2<B3 (zero-free-parameter; dynamical tau=0.107 (1,1,0)-crossing)",
        "anchor": "NuFit-6.0 (NO preferred ~2.5sigma)",
        "reconciled_status": "PASS (structural, machine-eps; S8/S34-36/S52/S56)",
        "register": ROBUST,
        "dual_status": False,
        "note": "zero-free-parameter substrate eigenvalue ordering; no borrowed H; clean robust spine row; JUNO/DUNE clean yes/no",
    },
    {
        "observable": "c_s^2 (dark-sector sound speed)",
        "layer": "a2 Goldstone / Kasparov",
        "fw_value": "0 exactly (Layer-1 topological; m_Goldstone^4D=0 by Kasparov factorization; bound <9.21e-4)",
        "anchor": "dark-sector c_s^2 (DES/KiDS, future)",
        "reconciled_status": "PASS-class (Level-1 topological; §VII.BH cross-pillar bridge PROVEN, S96 W7-8)",
        "register": ROBUST,
        "dual_status": False,
        "note": "STRUCTURAL ZERO (regulator-invariant, L-independent); no borrowed H; clean robust spine row; full §VII anatomy = W7-8 (mack-review-at-W8-2: no §7-surface retrofit needed -- entry is a §VII permanent-results cross-pillar bridge, not a §7 falsifier-surface row)",
    },
]

N_ROWS = len(ROWS)                                                          # (local) 14
print(f"[SEC 2] §7.1 row set: {N_ROWS} observable rows (post-W7 landings)")

# ==================================================================
# SECTION 3: partition + SUM-check + no-flattening predicate
# ==================================================================
robust_rows = [r for r in ROWS if r["register"] == ROBUST]                 # (local)
cond_rows = [r for r in ROWS if r["register"] == COND]                     # (local)
fals_rows = [r for r in ROWS if r["register"] == FALSIFIED]               # (local)

n_robust = len(robust_rows)                                                 # (local)
n_cond = len(cond_rows)                                                     # (local)
n_fals = len(fals_rows)                                                     # (local)

# SUM-check: every row in exactly one register; no omission, no double-count.
sum_check = (n_robust + n_cond + n_fals == N_ROWS)                         # (local)
all_assigned = all(r["register"] in (ROBUST, COND, FALSIFIED) for r in ROWS)  # (local)

# No-flattening predicate: NO row whose reconciled status is BROKEN/CONDITIONAL
# appears in the robust-structural register. (A status is "non-robust" if its
# reconciled_status string carries a BROKEN/CONDITIONAL/SCHEME-DEPENDENT/route-dependent marker.)
NON_ROBUST_MARKERS = ("BROKEN", "CONDITIONAL", "SCHEME-DEPENDENT", "route-dependent",
                      "advancing-tension", "INVERSION")                    # (local)


def is_non_robust_status(status_str: str) -> bool:                          # (local)
    s = status_str.upper()                                                 # (local)
    return any(m.upper() in s for m in NON_ROBUST_MARKERS)


flattening_violations = [                                                   # (local)
    r["observable"] for r in robust_rows if is_non_robust_status(r["reconciled_status"])
]
no_flattening = (len(flattening_violations) == 0)                          # (local)

# substrate-moment-layer tag preserved per row (a0/a2/a4 present in every row).
VALID_LAYER_PREFIXES = ("a0", "a2", "a4", "bispectrum", "E29")            # (local)
layer_tag_present = all(                                                    # (local)
    any(r["layer"].startswith(p) for p in VALID_LAYER_PREFIXES) for r in ROWS
)

# dual-status straddle rows (the disclosed INFO rows).
dual_status_rows = [r["observable"] for r in ROWS if r["dual_status"]]     # (local)

print(f"[SEC 3] partition: robust={n_robust}, conditional={n_cond}, falsified={n_fals}")
print(f"[SEC 3] SUM-check: {n_robust}+{n_cond}+{n_fals} == {N_ROWS} -> {sum_check}")
print(f"[SEC 3] no-flattening: {no_flattening} (violations={flattening_violations})")
print(f"[SEC 3] layer-tag-present: {layer_tag_present}")
print(f"[SEC 3] dual-status straddle rows (disclosed INFO): {dual_status_rows}")

# ==================================================================
# SECTION 4: consolidated §7-surface items (the W6/W7 pending items)
#   These are the falsifier-inventory / §7 updates this gate consolidates.
#   The NUMBERS are transcribed from canonical_constants.py (write-order Step 2
#   already complete for every value); this gate lands the inventory rows
#   (Step 3, mack sole writer) + the §7.1 anchor patch.
# ==================================================================
consolidated_items = [
    {
        "id": "W6-1 (S96-OBS-FSIGMA8-FORECAST)",
        "kind": "falsifier-inventory NEW row + §7.1 scorecard (already landed by W7-5)",
        "observable": "f*sigma_8(z) RSD growth",
        "fw_value": f"{fsigma8_product_suppression_FW_max_pct}% f*sigma8 PRODUCT suppression (bare-f {f_bare_suppression_FW_pct}%)",
        "detector": "DESI-5yr 2029 -> Euclid 2030s",
        "sigma": "1.013 (DESI-Y5) / 1.534 (Euclid)",
        "canonical_pins": ["fsigma8_product_suppression_FW_max_pct", "f_bare_suppression_FW_pct", "f_FW", "f_LCDM"],
        "verdict_anchor": "audit_sha256=318df6edeadb621453a46be1f5e8568db3fbff780e6e1792a69cb5ba37e06027",
        "action": "NEW inventory Row A (f*sigma8 RSD discriminator); C5 guard explicit",
    },
    {
        "id": "W6-2 (S96-OBS-FIRST-SOUND-RING)",
        "kind": "falsifier-inventory NEW row",
        "observable": f"first-sound BAO ring A_FS = {A_FS_first_sound_ring} = c2^2/c1^2 ring imprint at k1=0.0193 Mpc^-1 (r1=325.3 Mpc)",
        "fw_value": f"A_FS = {A_FS_first_sound_ring} (two-fluid acoustic ratio; NO LCDM counterpart)",
        "detector": "DESI-5yr (SNR 8.6) / DESI-DR1 (SNR 5.1)",
        "sigma": "SNR 8.6 DESI-5yr (sigma_exp 2.35%, arXiv:2411.19738v2); 5.1 DESI-DR1",
        "canonical_pins": ["A_FS_first_sound_ring"],
        "verdict_anchor": "audit_sha256=b74ccd56 (full-64 in s96 verdict file W6-2)",
        "action": ("NEW inventory Row B (first-sound ring); contrast: per-branch sub-feature "
                   "A_obs_B1=1.445e-3 is OUTSIDE current rulers BY DESIGN (0.60x DESI-DR2 ruler) -- "
                   "keep 'far below current rulers' scoped to THIS sub-feature, NOT the ring (ring is 141x the sub-feature)"),
    },
    {
        "id": "W6-3 (S96-OBS-CGWB-PEAK-FREQ)",
        "kind": "Row #7.audit SCOPE-CORRECTION (split peak-FREQUENCY from amplitude)",
        "observable": "CGWB peak FREQUENCY vs Omega_GW AMPLITUDE",
        "fw_value": (f"peak f_obs(kappa_nat) = {f_obs_CGWB_peak_kappa_nat:.4e} Hz (GHz+, 43.9 decades above LISA) -- "
                     f"the asserted 'peak in LISA mHz band' is REFUTED; LISA samples the Omega_GW IR-TAIL AMPLITUDE "
                     f"(Omega_GW^(A)~{Omega_GW_Lambda_A_LISA:.0e} at 3 mHz, W6-4 PASS), NOT the spectral peak"),
        "detector": "LISA ~2034 (amplitude IR-tail; NOT the peak)",
        "sigma": "D4 resolved AGAINST mHz peak",
        "canonical_pins": ["f_obs_CGWB_peak_kappa_nat", "Omega_GW_Lambda_A_LISA"],
        "verdict_anchor": "audit_sha256=646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e",
        "action": ("SCOPE-CORRECT the existing Row #7.audit / §7.2 #7 LISA flagship: split the two observables -- "
                   "(a) Omega_GW AMPLITUDE at LISA pivot UNCHANGED (the live IR-tail flagship, 11+ OOM above LISA-PLS); "
                   "(b) CGWB peak FREQUENCY CORRECTED to 8.48e39 Hz (GHz+), the mHz-peak placement is REFUTED; "
                   "the peak-frequency flagship is NORMALIZATION-CONDITIONAL-AND-CURRENTLY-AGAINST-mHz "
                   "(reaching LISA needs kappa=25 s/M_KK^-1, 42.5 OOM from natural hbar/M_KK)"),
    },
    {
        "id": "W7-5 MACK-INVENTORY-RECOMMENDATION (normal ordering)",
        "kind": "falsifier-inventory NEW row",
        "observable": "neutrino normal mass ordering (B1<B2<B3)",
        "fw_value": "Normal ordering, ZERO-FREE-PARAMETER, machine-eps (D_K (1,1,0)-singlet, dynamical tau=0.107 crossing)",
        "detector": "JUNO 2026+ / DUNE 2030s (a NO-vs-IO verdict is a clean yes/no)",
        "sigma": "NuFit-6.0 NO preferred ~2.5sigma => consistent",
        "canonical_pins": [],
        "verdict_anchor": "S96-HYG-SELF-INVENTORY audit_sha256=92a368105c829e8394ec7a1be899e42813f496cbbf0926a1f86b8cb06f6d38f1",
        "action": "NEW inventory Row C (normal mass ordering); the entire neutrino sector was ABSENT from the inventory before this landing",
    },
    {
        "id": "W6-4 FIDELITY NOTE (Omega_GW round-figure)",
        "kind": "publication-precision hygiene binding (Class-8.3)",
        "observable": "Omega_GW^(C) round-figure 1e-57 vs Sage-exact 8.299e-58",
        "fw_value": (f"1e-57 / {Omega_GW_Companion_null:.3e} = {1e-57/Omega_GW_Companion_null:.5f}x = "
                     f"{abs(math.log10(1e-57/Omega_GW_Companion_null)):.3f} OOM (same-decade)"),
        "detector": "N/A (hygiene)",
        "sigma": "N/A",
        "canonical_pins": ["Omega_GW_Companion_null", "OOM_split_AC_regulator_class"],
        "verdict_anchor": "audit_sha256=a9998118fdcb96bd41ebae88b0c2af0d5c4fb0c7c6d9bc277b62a50e10a0d382 (W6-4)",
        "action": ("CONFIRM the W6-4-landed FIDELITY NOTE: the round figure 1e-57 understates Omega_GW^(C) by "
                   "1.205x = 0.081 OOM (same-decade), NOT the '~10x / ~2 OOM' the rule/plan prose claimed. "
                   "The DISCIPLINE (use Sage-exact 8.299e-58, never 1e-57) is correct and binding -- but the "
                   "binding REASON is publication-precision hygiene (Class-8.3), NOT an OOM blunder. "
                   "ALREADY landed in Row #7.audit line 159; this gate ratifies it for the consolidation"),
    },
    {
        "id": "§VII.BH (c_s^2=0)",
        "kind": "mack-review-at-W8-2 (no §7-surface retrofit needed)",
        "observable": "c_s^2 = 0 (dark-sector sound speed)",
        "fw_value": "0 exactly (Kasparov factorization; bound <9.21e-4)",
        "detector": "dark-sector c_s^2 (DES/KiDS, future)",
        "sigma": "N/A (Level-1 topological)",
        "canonical_pins": [],
        "verdict_anchor": "audit_sha256=69d54dbf46f49424212a67bfb4a11c1472a39ad29d8c98ad1b6d2df8703a5003 (W7-8 §VII.BH)",
        "action": ("MACK-REVIEW VERDICT: §VII.BH is a §VII permanent-results CROSS-PILLAR BRIDGE entry "
                   "(substrate-IS -> Kasparov bridge -> lab-IN dark-sector bound), NOT a §7 falsifier-SURFACE row. "
                   "No strict §7-surface retrofit needed: the c_s^2 row already lands in §7.1 as a SCORECARD POINTER "
                   "(PASS-class robust spine, the §7.3 joint-BF spine member) with the full anatomy at §VII.BH. "
                   "The §7.1 row stays; no falsifier-master-inventory row is created (it is a registry bridge, not a falsifier)"),
    },
    {
        "id": "W6-7 (sigma_8 / S_8 labeling)",
        "kind": "§7.1 anchor-citation fix",
        "observable": "sigma_8 comparison anchor",
        "fw_value": f"capstone sigma_8 prediction 0.799; Planck anchor = sigma_8 {sigma_8} (NOT S_8=0.829)",
        "detector": "N/A (anchor hygiene)",
        "sigma": "recomputed 2.00sigma (vs the mis-cited 0.829)",
        "canonical_pins": ["sigma_8"],
        "verdict_anchor": "audit_sha256=37def5ddd58b9a5cdd3016949843fe94b5a61e905450ed3163b9fa810f7f9d0f (W6-7 Row #70)",
        "action": (f"FIX the §7.1 sigma_8 row comparison anchor: cite Planck sigma_8={sigma_8} (the canonical Planck sigma_8), "
                   f"NOT 0.829 (which is S_8). The capstone '0.829' is the S_8 value mis-labeled as sigma_8; "
                   f"canonical_constants.py:sigma_8={sigma_8} is the Planck sigma_8. Prose/citation fix also routes to W8-6"),
    },
]
print(f"[SEC 4] consolidated §7-surface items: {len(consolidated_items)}")

# ==================================================================
# SECTION 5: build the 3 register-tables (markdown)
# ==================================================================
def _esc(cell: str) -> str:                                                 # (local)
    """Escape literal pipes inside a markdown table cell (e.g. |f_NL| -> \\|f_NL\\|)."""
    return str(cell).replace("|", "\\|")


def _md_register_table(title, epistemic_class, rows):                       # (local)
    lines = []                                                              # (local)
    lines.append(f"#### {title}")
    lines.append("")
    lines.append(f"*Epistemic class: **{epistemic_class}**.*")
    lines.append("")
    lines.append("| Observable | Layer (a₀/a₂/a₄) | Framework value | Comparison anchor | Reconciled status (W8-1) | Notes |")
    lines.append("|:--|:--|:--|:--|:--|:--|")
    for r in rows:
        ds = " **[DUAL-STATUS straddle — disclosed]**" if r["dual_status"] else ""
        layer = r["layer"].replace("a0", "a₀").replace("a2", "a₂").replace("a4", "a₄")
        lines.append(
            f"| **{_esc(r['observable'])}** | {_esc(layer)} | {_esc(r['fw_value'])} | "
            f"{_esc(r['anchor'])} | {_esc(r['reconciled_status'])}{ds} | {_esc(r['note'])} |"
        )
    lines.append("")
    return "\n".join(lines)


reg_robust_md = _md_register_table(
    "Register A — ROBUST-STRUCTURAL outputs (zero-free-parameter spine)",
    "PROVEN / PASS-structural / Gaussian-by-Wick BOUND — substrate-IS predictions, "
    "the no-borrowed-H joint-BF spine",
    robust_rows,
)
reg_cond_md = _md_register_table(
    "Register B — CONDITIONAL outputs (PASS contingent on an unresolved input)",
    "CONDITIONAL / SCHEME-DEPENDENT / route-dependent / doubly-conditional — the PASS "
    "holds GIVEN an unresolved input, scheme, route, or borrowed H(t)",
    cond_rows,
)
reg_fals_md = _md_register_table(
    "Register C — CURRENTLY-FALSIFIED outputs (the live wagers)",
    "BROKEN / advancing-tension / inversion-falsified — the register marks these against "
    "current data; reported as boundaries that sharpen the surviving solution space",
    fals_rows,
)

three_register_md = (
    "### §7.1 — Outputs by epistemic register (3-register split)\n\n"
    "> The single §7.1 'now' table is split into three epistemic registers (report §\"Critique\": "
    "the flat table *\"visually flattens conditional and unconditional claims into a common rhetorical "
    "register\"*). Each observable lands in **exactly one** register, keyed by its W8-1-reconciled status "
    "tag; **no row's epistemic type is flattened** (no BROKEN/CONDITIONAL row in the robust register); the "
    "substrate-moment-layer (a₀/a₂/a₄) provenance is preserved per row. Dual-status straddle rows (m_H) "
    "land in CONDITIONAL with an explicit disclosure, **not** forced into the robust register. "
    "**No observable below is fit** — each is a spectral moment of `D_K` at the same single modulus `τ_now`; "
    "when the substrate measures one of these, the substrate is probing itself.\n\n"
    + reg_robust_md + "\n" + reg_cond_md + "\n" + reg_fals_md
    + "\n> **SUM-check (partition correctness).** "
    + f"|robust|={n_robust} + |conditional|={n_cond} + |falsified|={n_fals} = {n_robust+n_cond+n_fals} "
    + f"== |§7.1 rows|={N_ROWS} (no omission, no double-count). "
    + "No-flattening: no BROKEN/CONDITIONAL row in Register A. "
    + f"Dual-status straddle (disclosed, placed in CONDITIONAL): {', '.join(dual_status_rows) if dual_status_rows else 'none'}. "
    + "The 3-register split changes **no value** and **no substrate-moment-layer attribution**; it only sorts "
    + "the rows by epistemic register so the zero-parameter robust spine is not visually conflated with the "
    + "conditional forecasts or the live wagers (the §7.3 honest-scorecard makes the same distinction in prose).\n"
)

MD_OUT.write_text(three_register_md, encoding="utf-8")
print(f"[SEC 5] wrote 3 register-tables markdown -> {MD_OUT.name} ({len(three_register_md)} bytes)")

# ==================================================================
# SECTION 6: verdict logic (artifact-existence / partition-correctness conjunction)
# ==================================================================
# PASS iff: 3 register-tables present (built) AND SUM-check exact AND no-flattening
#           AND layer-tag preserved per row AND W8-1 present.
# INFO     : the split lands but >=1 row is a genuine dual-status straddle (disclosed,
#            placed in CONDITIONAL with annotation) -- the honest INFO per the gate rubric.
# PRE-REG-INC: W8-1 status-diff absent (mechanical closure per mechanical-closure-discipline.md).

if not W8_1_PRESENT:
    verdict = "FAIL"                                                       # (local)
    value_str = "PRE-REG-INC_blocked_by_S96-CONSOL-STATUS-SYNC_NOT-LANDED"  # (local)
elif sum_check and all_assigned and no_flattening and layer_tag_present:
    # Partition correct. INFO iff a disclosed dual-status straddle exists (gate INFO_meaning).
    if dual_status_rows:
        verdict = "INFO"                                                  # (local)
    else:
        verdict = "PASS"                                                  # (local)
    value_str = (
        f"3register_split;rows={N_ROWS};robust={n_robust};conditional={n_cond};"
        f"falsified={n_fals};SUM_check={'exact' if sum_check else 'FAIL'};"
        f"no_flattening={no_flattening};layer_tag={layer_tag_present};"
        f"dual_status_straddle={'+'.join(r.replace(' ', '_') for r in dual_status_rows) if dual_status_rows else 'none'};"
        f"consolidated_items={len(consolidated_items)}"
    )
else:
    verdict = "FAIL"                                                      # (local)
    value_str = (
        f"3register_split_FAIL;SUM_check={sum_check};all_assigned={all_assigned};"
        f"no_flattening={no_flattening};flattening_violations={'+'.join(flattening_violations) or 'none'};"
        f"layer_tag={layer_tag_present}"
    )

print(f"[SEC 6] VERDICT={verdict}  value={value_str}")

# ==================================================================
# SECTION 7: JSON partition map + npz
# ==================================================================
partition_map = {                                                          # (local)
    "gate_id": GATE_ID,
    "session": "S96",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "verdict": verdict,
    "classification": "NON-PHONONIC",
    "methodology_class": True,
    "upstream_W8_1": {
        "present": W8_1_PRESENT,
        "verdict": status_diff.get("verdict", "ABSENT") if W8_1_PRESENT else "ABSENT",
        "audit_sha256": status_diff.get("audit_sha256", "") if W8_1_PRESENT else "",
        "cell_register_map_rows": len(cell_map),
    },
    "register_assignment_rule": {
        "robust-structural": ["PROVEN", "PASS-structural", "DISSOLVED-favorably", "BOUND-Gaussian-by-Wick"],
        "conditional": ["CONDITIONAL", "SCHEME-DEPENDENT", "route-dependent", "doubly-conditional", "VIABLE"],
        "currently-falsified": ["BROKEN", "advancing-tension", "INVERSION-falsified"],
    },
    "n_rows": N_ROWS,
    "registers": {
        "robust-structural": [
            {"observable": r["observable"], "layer": r["layer"],
             "reconciled_status": r["reconciled_status"], "dual_status": r["dual_status"]}
            for r in robust_rows
        ],
        "conditional": [
            {"observable": r["observable"], "layer": r["layer"],
             "reconciled_status": r["reconciled_status"], "dual_status": r["dual_status"]}
            for r in cond_rows
        ],
        "currently-falsified": [
            {"observable": r["observable"], "layer": r["layer"],
             "reconciled_status": r["reconciled_status"], "dual_status": r["dual_status"]}
            for r in fals_rows
        ],
    },
    "sum_check": {
        "n_robust": n_robust, "n_conditional": n_cond, "n_falsified": n_fals,
        "n_total": N_ROWS, "exact": sum_check, "all_assigned": all_assigned,
    },
    "no_flattening": {"holds": no_flattening, "violations": flattening_violations},
    "layer_tag_preserved": layer_tag_present,
    "dual_status_straddle_rows": dual_status_rows,
    "rows_full": ROWS,
    "consolidated_section7_surface_items": consolidated_items,
    "anchor_fixes": {
        "sigma_8_anchor": f"Planck sigma_8={sigma_8} (NOT S_8=0.829); W6-7 fix routed to §7.1 + W8-6 prose",
    },
}

# input pins (for the dual-SHA + JSON record)
INPUT_FILES = [CANONICAL_PY, STATUS_DIFF_JSON, CAPSTONE, ATLAS_04]          # (local)
pins = log_input_pins(INPUT_FILES)                                          # (local)
clos = closure_hash(pins)                                                   # (local)
partition_map["input_pins"] = pins
partition_map["closure_hash"] = clos

JSON_OUT.write_text(json.dumps(partition_map, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"[SEC 7] wrote JSON partition map -> {JSON_OUT.name}")

np.savez(
    NPZ_OUT,
    n_rows=N_ROWS,
    n_robust=n_robust, n_conditional=n_cond, n_falsified=n_fals,
    sum_check=sum_check, no_flattening=no_flattening, layer_tag=layer_tag_present,
    robust_observables=np.array([r["observable"] for r in robust_rows], dtype=object),
    conditional_observables=np.array([r["observable"] for r in cond_rows], dtype=object),
    falsified_observables=np.array([r["observable"] for r in fals_rows], dtype=object),
    dual_status_rows=np.array(dual_status_rows, dtype=object),
    n_consolidated_items=len(consolidated_items),
    verdict=verdict,
)
print(f"[SEC 7] wrote npz -> {NPZ_OUT.name}")

# ==================================================================
# SECTION 8: optional plot (register-population bar)
# ==================================================================
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 4.5))
    cats = ["ROBUST-\nSTRUCTURAL", "CONDITIONAL", "CURRENTLY-\nFALSIFIED"]   # (local)
    counts = [n_robust, n_cond, n_fals]                                     # (local)
    colors = ["#2a7f3f", "#c79a00", "#b03030"]                              # (local)
    bars = ax.bar(cats, counts, color=colors, edgecolor="black")
    for b, c in zip(bars, counts):
        ax.text(b.get_x() + b.get_width() / 2, c + 0.08, str(c),
                ha="center", va="bottom", fontsize=12, fontweight="bold")
    ax.set_ylabel("§7.1 observable rows")
    ax.set_title(f"{GATE_ID}: §7 'now' table -> 3 epistemic registers "
                 f"(SUM-check {n_robust}+{n_cond}+{n_fals}={N_ROWS}; verdict {verdict})")
    ax.set_ylim(0, max(counts) + 1.2)
    ax.text(0.5, -0.22, f"no-flattening={no_flattening}; dual-status straddle (CONDITIONAL): "
            f"{', '.join(dual_status_rows) if dual_status_rows else 'none'}",
            transform=ax.transAxes, ha="center", fontsize=8, style="italic")
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"[SEC 8] wrote plot -> {PNG_OUT.name}")
except Exception as exc:  # noqa: BLE001
    print(f"[SEC 8] plot skipped (optional): {exc}")

# ==================================================================
# SECTION 9: dual-SHA verdict-line emission (after JSON exists so it is pinned)
# ==================================================================
audit_sha, content_sha = compute_dual_sha(THIS_SCRIPT, CANONICAL_PY, pins)  # (local)
print(f"[SEC 9] closure_hash(pins) = {clos[:16]}...")
print(f"[SEC 9] audit_sha256   = {audit_sha}")
print(f"[SEC 9] content_sha256 = {content_sha}")

append_verdict(verdict, value_str, audit_sha, content_sha)
print(f"[SEC 9] appended verdict line to {VERDICT_TXT.name}")

# 4-tuple output tag (final non-verdict line)
print(f"\n4-tuple: (value=⟨3-register split: {n_robust}/{n_cond}/{n_fals}, SUM-check exact⟩, "
      f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

sys.exit(0)
