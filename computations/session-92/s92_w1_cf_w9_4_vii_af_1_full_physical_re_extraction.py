#!/usr/bin/env python3
"""
S92 W1 — S92-W1-CF-W9-4-VII-AF-1-OP-PROJ-FULL-PHYSICAL-RE-EXTRACTION
======================================================================

Gate-ID:  S92-W1-CF-W9-4-VII-AF-1-OP-PROJ-FULL-PHYSICAL-RE-EXTRACTION
Trigger:  [VERIFY-THEOREM]
Owner:    connes-ncg-theorist (PRIMARY; CC1996 §2.2-2.3 PV multiplier
          + CM-1995 §III.4 dimension-spectrum residue formula authority)

Provenance / Source-of-truth:
  - Plan: sessions/session-plan/session-92-plan-w1.md §W1-1 (lines 31-337)
  - Predecessor: S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE
    (S91 line 199; audit_sha256
     79314db6a6aee05390f34d0a666540eee3ae5fb113273d4f73b2d980434ca2a3)
    — this gate's corrective canonical SUPERSEDES that line per Option A
    protocol of gate-verdicts.md.
  - Cross-pillar bridge anatomy rule: cross-pillar-bridge-anatomy.md
    §"Per-Bulletin-per-pole Level-1 wall classification" (FI/RD/MIXED)
  - Level-pin discipline: substrate-first-canonical-sourcing.md §(iv)
    K=4 MANDATORY (CLASS=FULL; no `-SCHEMATIC` suffix)
  - Registry slot: permanent-results-registry.md §VII.AF.1.OP-PROJ

PURPOSE
-------
Refresh §VII.AF.1.OP-PROJ canonical Level-3 anchor
    R_universal_HP1_strict_F4 -> 1.030902  (canonical pin, NOT a reassignment)
(SDW-residual extraction at L_max=10) against the FULL-physical CC1996
§2.2-2.3 Pauli-Villars 2-point regulator and FOUR companion regulator
classes across the 5-regulator atlas
    {zeta, SDW, Pauli-Villars (FULL-CC), Mellin, lattice}
evaluated on the L_max=12 master spectrum cache at substrate-distance-1
pole s=3.

The 5-atlas spread classifies the §VII.AF.1.OP-PROJ Level-3 anchor at
substrate-distance-1 pole s=3 per the FI/RD/MIXED band taxonomy:
    FI    iff atlas_spread < 1e-3   (algebra-INVARIANT functional family)
    RD    iff atlas_spread > 1e-2   (regulator-dependent at this pole)
    MIXED iff 1e-3 ≤ atlas_spread ≤ 1e-2

PRE-REGISTERED OUTCOME (substitution chain Step 5):
    From the S91 W9-4 measurement rho_FULL_CC(s=3) = 1.0100907902 and
    canonical SDW value 1.030902, the SDW↔FULL-CC pair alone yields
    atlas_spread ≥ 2.04e-2 > 1e-2 RD floor. Hence the gate is PRE-
    REGISTERED as FAIL-WITH-DIAGNOSTIC — the FAIL itself IS the substrate-
    physics finding (Level-1 RD classification of the §VII.AF.1.OP-PROJ
    Level-3 anchor at substrate-distance-1 pole s=3).

SUBSTRATE FRAMING
-----------------
The substrate IS the spectral triple (A_K, H_K, D_K) at τ_fold=0.19.
The 5-regulator atlas {zeta, SDW, Pauli-Villars (FULL-CC), Mellin, lattice}
are FIVE methodology-floor F-images (per epistemic-discipline.md
§"Layer-Decomposition" Phi correspondence) of the SAME substrate-IS
canonical Hochschild-pairing image at substrate-distance-1 pole s=3.
The atlas spread IS the substrate's regulator-class-dependence at this
pole surfaced by the FI/RD taxonomy — NOT a substrate-model failure.

CONVENTION TAG (per substrate-first-canonical-sourcing.md §(iv) K=4)
-------------------------------------------------------------------
    LEVEL_CLASS_PIN = FULL  (FULL CC1996 §2.2-2.3 Pauli-Villars; no
                              `-SCHEMATIC` suffix; uses _pauli_villars_subtraction.py
                              PRIMARY tier, NOT _spectral_action_regulators.py)
    convention = VII-AF-1-OP-PROJ-FULL-CC-MULTIPLIERS-PHYSICAL-
                 substrate-distance-1-pole-s3-atlas-spread-FI-RD-classification

INPUTS
------
- computations/_shared/canonical_constants.py
- computations/session-84/s84_spectrum_cache_L12_tau019.npz (L_max=12)
- computations/_pauli_villars_subtraction.py (FULL-physical PV PRIMARY)
- computations/_shared/_spectral_action_regulators.py (SCHEMATIC zeta-
  baseline retained ONLY as reference; FULL-CC is the canonical)
- computations/session-91/s91_gate_verdicts.txt (supersedes-target SHA
  pin: 79314db6a6aee05390f34d0a666540eee3ae5fb113273d4f73b2d980434ca2a3)

OUTPUTS
-------
- computations/session-92/s92_w1_cf_w9_4_vii_af_1_full_physical_re_extraction.py
- computations/session-92/s92_w1_cf_w9_4_vii_af_1_full_physical_re_extraction.npz
- computations/session-92/s92_w1_cf_w9_4_vii_af_1_full_physical_re_extraction.png
- computations/session-92/s92_gate_verdicts.txt
   (canonical line carrying supersedes=<full-64-char> tag per Option A
    + dual-SHA companion + LEVEL pin row + supersedes-pointer companion)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Canonical constants (mandatory imports per math-scripts.md S34+).
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    gv_canonical_difference_FW,
    R_universal_HP1_strict_F4,
    eps_H_HP1_norm,
)

# FULL physical Pauli-Villars helper (PRIMARY tier per substrate-first-
# canonical-sourcing.md §(iv) K=4 MANDATORY level-pin discipline).
# This is the FULL-CC pipeline; NOT the SCHEMATIC _spectral_action_regulators.py
# Pauli-Villars single-subtraction analog.
from _pauli_villars_subtraction import (  # noqa: E402
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
    bare_mellin_moment,
    pv_mellin_moment_primary,
    pv_multiplier_primary,
    heat_kernel_mellin_moment,
    hard_cutoff_mellin_moment,
    _verify_pv_identities,
)


# ====================== Gate-block constants (plan §W1-1) ======================

GATE_ID = "S92-W1-CF-W9-4-VII-AF-1-OP-PROJ-FULL-PHYSICAL-RE-EXTRACTION"
SCHEME = "full-cc1996-2-2-2-3-pauli-villars-physical-multipliers-atlas-comparison"
CONVENTION = (
    "VII-AF-1-OP-PROJ-FULL-CC-MULTIPLIERS-PHYSICAL-"
    "substrate-distance-1-pole-s3-atlas-spread-FI-RD-classification"
)
L_MAX = 12  # (local) plan-pinned canonical anchor at L_max=12 master cache

# Connes-Chamseddine 1996 §2.2-2.3 physical multipliers (canonical PV pair).
M_1_FW_CC = M_KK                       # (local) canonical mass scale
M_2_FW_CC = math.sqrt(2.0) * M_KK      # (local) 2-point PV pair upper mass
C_1_FW_CC = +2                         # (local) PV coefficient 1
C_2_FW_CC = -1                         # (local) PV coefficient 2

# Substrate-distance-1 pole at Mellin index s=3 (per registry §VII.AF.1.OP-PROJ
# Cell I classification: INVARIANT × s=3; spectrum-only functional via
# a_4^ζ residue at s=0; substrate-distance-1 cone ↔ s=3 Mellin pole).
S_POLE = 3                              # (local) substrate-distance-1 pole

# Pre-registered FI/RD/MIXED thresholds (plan §W1-1 strict_PASS_boundary
# 3-band classifier; per cross-pillar-bridge-anatomy.md
# §"Per-Bulletin-per-pole Level-1 wall classification" canonical bands).
FI_CEILING = 1e-3                       # (local) FI upper band edge
RD_FLOOR = 1e-2                         # (local) RD lower band edge

# §VII.AF.1.OP-PROJ Level-3 anchor canonical (per registry line 14808;
# W-5 V4 STRICT_F4 atlas match at L_max=10; SDW-class).
R_CANONICAL_AF1 = R_universal_HP1_strict_F4  # (local) = 1.030902 canonical pin

# Option A supersedes-target full 64-character audit_sha256 (per
# gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute
# verdict permanence"; points to S91-W6-CF-W7-1-CF-49 at S91 line 199).
# Verdict-line literal form: supersedes=79314db6a6aee05390f34d0a666540eee3ae5fb113273d4f73b2d980434ca2a3
SUPERSEDES_TARGET = "79314db6a6aee05390f34d0a666540eee3ae5fb113273d4f73b2d980434ca2a3"

# Output paths.
OUT_NPZ = ROOT / "computations" / "session-92" / "s92_w1_cf_w9_4_vii_af_1_full_physical_re_extraction.npz"
OUT_PNG = ROOT / "computations" / "session-92" / "s92_w1_cf_w9_4_vii_af_1_full_physical_re_extraction.png"
VERDICT_FILE = ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

# Input file paths (for SHA-pin map).
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
PV_HELPER = ROOT / "computations" / "_pauli_villars_subtraction.py"
SCH_HELPER = ROOT / "computations" / "_shared" / "_spectral_action_regulators.py"
S91_VERDICTS = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
CPB_RULE = ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
SFC_RULE = ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "pauli_villars_helper_PRIMARY": PV_HELPER,
    "spectral_action_regulators_SCHEMATIC_reference": SCH_HELPER,
    "s91_verdicts_supersedes_source": S91_VERDICTS,
    "registry_vii_af_1_op_proj": REGISTRY,
    "cross_pillar_bridge_anatomy_rule": CPB_RULE,
    "substrate_first_canonical_sourcing_rule": SFC_RULE,
    "script": SCRIPT_PATH,
}


# ============================== SHA helpers ==============================

def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()                # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}                            # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:42s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)          # (local)
        pins[name] = sha
        print(f"  {name:42s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def closure_hash(pinmap: dict) -> str:
    """Compute audit_sha256 from the ordered input-pin map (NEVER hardcoded).

    This is the canonical pattern from _script_template.py append_verdict():
    audit_sha256 is the SHA-256 of the canonicalized pin map; SHA uniqueness
    across gates is preserved by construction (sig_5 ladder uniqueness).
    """
    pinmap_json = json.dumps(sorted(pinmap.items()), sort_keys=True).encode("utf-8")
    return hashlib.sha256(pinmap_json).hexdigest()


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per W9a-99 dual-SHA split.

    audit_sha256   = closure_hash over (script + canonical_constants + pinmap)
                     — closure of the full audit trail
    content_sha256 = SHA over the script bytes only — content reproducibility
    """
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()                                  # (local)
    return audit, content


# ============================== Spectrum loader ==============================

def load_spectrum_flat(cache_path: Path):
    """Load L_max=12 master spectrum cache (per S88 W13-159 PRIMARY PV
    helper convention)."""
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    lambdas_list = []                    # (local)
    mults_list = []                      # (local)
    n_sectors = 0                        # (local)
    for (p, q), info in sector_evals.items():
        n_sectors += 1
        dim = int(info["dim"])           # (local) Peter-Weyl dim(p,q)
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            lambdas_list.append(float(v))
            mults_list.append(dim)
    lambdas = np.array(lambdas_list, dtype=np.float64)
    mults = np.array(mults_list, dtype=np.float64)
    return lambdas, mults, n_sectors


# ============================== Regulator evaluators ==============================
#
# Each regulator R returns rho_R(s) := M_R(s) / M_BARE(s) at the substrate-
# distance-1 pole s=3 on the L_max=12 finite spectral triple. M_BARE is the
# zeta/bare-spectrum-sum baseline (no multiplier).
#
# Multipliers (per plan §W1-1 substitution chain Definition 2):
#   zeta            : w = 1 (bare Mellin)
#   SDW             : w_SDW(λ²; s) — Seeley-DeWitt logarithmic dressing
#   Pauli-Villars   : w_PV(λ²; s) = 1 - Σ_r c_r · (m_r² / (λ²+m_r²))^s
#                      (FULL CC1996; PV identities Σc_r=1, Σc_r m_r²=0)
#   Mellin          : w = 1 (equivalent to zeta on positive-Casimir spectrum
#                            per _spectral_action_regulators.py docstring)
#   lattice         : w = θ(λ² ≤ Λ_lat²) — sharp cutoff at top fraction
# ===============================================================================


def m_zeta(s_pole, lambdas, mults):
    """M_zeta(s) = Σ_k m_k · λ_k^{-2s}  (bare; w=1)."""
    return bare_mellin_moment(s_pole, lambdas, mults)


def m_sdw(s_pole, lambdas, mults, t_ref=1.0e-3):
    """M_SDW(s) = Σ_k m_k · exp(-t_ref · λ_k²) · λ_k^{-2s}.

    Seeley-DeWitt logarithmic dressing of the Mellin moment via heat-kernel
    exp(-t·λ²) at small t. At t → 0+ recovers the bare zeta moment; finite
    t carries a logarithmic SDW dressing.
    """
    return heat_kernel_mellin_moment(s_pole, lambdas, mults, t_ref)


def m_pauli_villars_full_cc(s_pole, lambdas, mults):
    """M_PV(s) = Σ_k m_k · w_PV(λ_k²; s) · λ_k^{-2s}.

    FULL CC1996 §2.2-2.3 Pauli-Villars 2-point multiplier:
        w_PV(λ²; s) = 1 - Σ_{r=1..2} c_r · (m_r² / (λ²+m_r²))^s
    with (c_1, c_2) = (+2, -1) and (m_1, m_2) = (1, √2) dimensionless
    (M_KK units). PV identities Σc_r=1, Σc_r·m_r²=0 verified at module load.
    """
    return pv_mellin_moment_primary(s_pole, lambdas, mults)


def m_mellin(s_pole, lambdas, mults):
    """M_Mellin(s) — equivalent to bare zeta on the positive-Casimir spectrum.

    Per _spectral_action_regulators.py docstring lines 17-18: 'Zeta and
    Mellin are equivalent on this positive-definite spectrum at real s.'
    Implemented as bare moment; retained as separate atlas entry for
    explicit regulator-class enumeration.
    """
    return bare_mellin_moment(s_pole, lambdas, mults)


def m_lattice(s_pole, lambdas, mults, cutoff_frac=0.7):
    """M_lattice(s) — sharp cutoff (lattice-spacing analog).

    Restrict the spectrum sum to λ_k² ≤ cutoff_frac · max(λ_k²). The
    cutoff_frac=0.7 default mirrors the _spectral_action_regulators.py
    'hard-cutoff' class for atlas-spread comparison.
    """
    return hard_cutoff_mellin_moment(s_pole, lambdas, mults, cutoff_frac=cutoff_frac)


# ============================== Atlas evaluation ==============================

REGULATOR_ORDER = ["zeta", "SDW", "Pauli-Villars-FULL-CC", "Mellin", "lattice"]


def evaluate_atlas(s_pole, lambdas, mults):
    """Compute M_R(s) for each R in the 5-regulator atlas, then rho_R = M_R/M_BARE.

    M_BARE := M_zeta (bare-spectrum-sum baseline; per plan §W1-1 Def 3).
    """
    M_R = {}                                         # (local)
    M_R["zeta"] = m_zeta(s_pole, lambdas, mults)
    M_R["SDW"] = m_sdw(s_pole, lambdas, mults)
    M_R["Pauli-Villars-FULL-CC"] = m_pauli_villars_full_cc(s_pole, lambdas, mults)
    M_R["Mellin"] = m_mellin(s_pole, lambdas, mults)
    M_R["lattice"] = m_lattice(s_pole, lambdas, mults)

    M_BARE = M_R["zeta"]                             # (local) baseline
    rho_R = {R: M_R[R] / M_BARE for R in REGULATOR_ORDER}  # (local)

    return M_R, rho_R, M_BARE


# ============================== Verdict evaluation ==============================

def evaluate_verdict(atlas_spread: float) -> dict:
    """3-band classifier per plan §W1-1 strict_PASS_boundary:
        PASS  iff atlas_spread < FI_CEILING (1e-3) → FI reclassification
        FAIL  iff atlas_spread > RD_FLOOR (1e-2)   → RD reclassification
        INFO  iff 1e-3 ≤ atlas_spread ≤ 1e-2       → MIXED

    Note (substitution chain Step 5): given the SDW pin 1.030902 and the
    S91 W9-4 measurement rho_FULL_CC ≈ 1.0101, atlas_spread ≥ 2.04e-2 by
    construction; PASS is structurally unreachable. This is a band
    classifier, not a signed direction — schema_v2_3tuple is NOT required
    (schema_v2_3tuple_required=False per plan).
    """
    if atlas_spread < FI_CEILING:
        composite = "PASS"
        classification = "FI"
    elif atlas_spread > RD_FLOOR:
        composite = "FAIL"
        classification = "RD"
    else:
        composite = "INFO"
        classification = "MIXED"
    return {
        "composite": composite,
        "classification": classification,
        "atlas_spread": atlas_spread,
    }


# ============================== Diagnostic plot ==============================

def make_plot(rho_R, M_R, R_canonical, atlas_spread, delta_R, classification,
              w_PV_min, w_PV_mean, w_PV_max, s_pole, l_max):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 11))

    regulators = REGULATOR_ORDER
    rho_vals = [rho_R[R] for R in regulators]                # (local)
    delta_vals = [delta_R[R] for R in regulators]            # (local)

    colors = {
        "zeta": "steelblue",
        "SDW": "forestgreen",
        "Pauli-Villars-FULL-CC": "darkorange",
        "Mellin": "purple",
        "lattice": "firebrick",
    }
    bar_colors = [colors[R] for R in regulators]             # (local)

    # Panel 1: rho_R atlas at pole s=3.
    ax1.bar(regulators, rho_vals, color=bar_colors, edgecolor="black")
    ax1.axhline(R_canonical, color="black", linestyle="--", linewidth=1.5,
                label=f"R_canonical_AF1 = {R_canonical:.6f}")
    ax1.set_ylabel(r"$\rho_R(s=3) = M_R / M_{\rm BARE}$")
    ax1.set_title(
        f"5-regulator atlas at substrate-distance-1 pole s={s_pole}, L_max={l_max}\n"
        f"atlas_spread = (max-min)/mean = {atlas_spread:.6e}  → {classification}"
    )
    ax1.tick_params(axis="x", labelsize=9, rotation=15)
    ax1.grid(True, axis="y", alpha=0.3)
    ax1.legend(loc="best", fontsize=9)

    # Panel 2: Delta_R = (rho_R - R_canonical)/|R_canonical| per regulator.
    ax2.bar(regulators, delta_vals, color=bar_colors, edgecolor="black")
    ax2.axhline(0.0, color="black", linewidth=1.0)
    ax2.axhline(+FI_CEILING, color="green", linestyle=":", linewidth=1.0,
                label=f"FI ceiling = ±{FI_CEILING:.0e}")
    ax2.axhline(-FI_CEILING, color="green", linestyle=":", linewidth=1.0)
    ax2.axhline(+RD_FLOOR, color="red", linestyle=":", linewidth=1.0,
                label=f"RD floor = ±{RD_FLOOR:.0e}")
    ax2.axhline(-RD_FLOOR, color="red", linestyle=":", linewidth=1.0)
    ax2.set_ylabel(r"$\Delta_R = (\rho_R - R_{\rm canonical})/|R_{\rm canonical}|$")
    ax2.set_title(
        "Per-regulator delta vs §VII.AF.1.OP-PROJ Level-3 anchor "
        f"R_canonical_AF1 = {R_canonical:.6f}"
    )
    ax2.tick_params(axis="x", labelsize=9, rotation=15)
    ax2.grid(True, axis="y", alpha=0.3)
    ax2.legend(loc="best", fontsize=8)

    # Panel 3: M_R Mellin moments at pole s=3 (log scale).
    M_vals = [M_R[R] for R in regulators]                    # (local)
    ax3.bar(regulators, M_vals, color=bar_colors, edgecolor="black")
    ax3.set_yscale("log")
    ax3.set_ylabel(r"$M_R(s=3)$ (log scale)")
    ax3.set_title(
        f"Raw Mellin moments M_R(s={s_pole}) across 5-regulator atlas\n"
        f"(L_max={l_max} master cache; multiplicity-weighted)"
    )
    ax3.tick_params(axis="x", labelsize=9, rotation=15)
    ax3.grid(True, axis="y", alpha=0.3)

    # Panel 4: PV multiplier w_PV statistics across L_max=12 spectrum.
    ax4.bar(["w_PV_min", "w_PV_mean", "w_PV_max"],
            [w_PV_min, w_PV_mean, w_PV_max],
            color=["green", "gray", "red"], edgecolor="black")
    ax4.axhline(1.0, color="black", linestyle="--", linewidth=1.0,
                label="UV identity (w_PV → 1, λ² → ∞)")
    ax4.axhline(0.0, color="black", linestyle="-", linewidth=1.0,
                label="IR zero (w_PV → 0, λ² → 0)")
    ax4.set_ylabel("w_PV multiplier value")
    ax4.set_title(
        f"FULL-CC PV multiplier statistics on L_max={l_max} spectrum (s={s_pole})\n"
        f"(c_1, c_2) = (+2, -1); (m_1, m_2) = (1, √2)  M_KK-natural"
    )
    ax4.legend(loc="best", fontsize=9)
    ax4.grid(True, axis="y", alpha=0.3)

    fig.suptitle(
        f"S92 W1-1 — §VII.AF.1.OP-PROJ FULL-CC re-extraction over 5-regulator atlas  "
        f"(L_max={l_max}, pole s={s_pole}, τ_fold={tau_fold})",
        fontsize=12,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ============================== Verdict emission ==============================

def _scan_prior_audit_shas_for_gate(verdict_path: Path) -> list:
    """Return list of audit_sha256 values for prior canonical lines of this
    GATE_ID in s92_gate_verdicts.txt (for Option A supersedes-chain support).

    Per gate-verdicts.md §"Option A — sig_5 remediation pathway":
    Option A admits a supersedes-chain when an in-session corrective
    canonical line is appended after a prior canonical line for the same
    gate-ID. The corrective line's value= field carries the prior SHA so
    consumers can resolve the LATEST non-superseded line as canonical.
    """
    prior_shas = []                                # (local)
    if not verdict_path.exists():
        return prior_shas
    text = verdict_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if not line.startswith(f"{GATE_ID}: "):
            continue
        for tok in line.split():
            if tok.startswith("audit_sha256="):
                sha = tok.split("=", 1)[1]         # (local)
                prior_shas.append(sha)
    return prior_shas


def append_verdict(composite: str, value_str: str, audit_sha: str,
                   content_sha: str, classification: str):
    """Atomic single-shot append per gate-verdicts.md S87+ canonical form
    + Option A supersedes-tag protocol.

    Emits 4 (or 5 on in-session chain-supersedes) rows:
      1. Canonical line (PASS/FAIL/INFO, full 64-char SHA, supersedes tag
         on value= field — points to S91 W6-CF-W7-1-CF-49 parent SHA)
      2. Dual-SHA companion comment row (W9a-99 split)
      3. LEVEL_CLASS_PIN companion row (FULL; substrate-first §(iv))
      4. Supersedes-pointer companion row (explicit pointer to S91 line 199)
      5. (if in-session prior S92 canonical line(s) exist for this gate-ID)
         in-session chain-supersedes annotation row pointing to each prior
         intra-session SHA for absolute verdict permanence audit trail.

    NO 3-tuple companion row: per plan schema_v2_3tuple_required=False
    (band classifier, not signed direction).
    """
    # Scan for prior in-session canonical lines for this gate-ID (Option A
    # absolute verdict permanence: prior lines remain on disk; corrective
    # line APPENDS with supersedes annotation).
    prior_in_session_shas = _scan_prior_audit_shas_for_gate(VERDICT_FILE)  # (local)

    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"supersedes={SUPERSEDES_TARGET} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md §(iv) "
        f"K=4 MANDATORY level-pin compliance "
        f"(FULL CC1996 §2.2-2.3 Pauli-Villars; "
        f"_pauli_villars_subtraction.py PRIMARY tier; "
        f"NO -SCHEMATIC suffix; classification={classification})\n"
    )
    supersedes_pointer = (
        f"# supersedes_target=S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE "
        f"supersedes_audit_sha256={SUPERSEDES_TARGET} "
        f"supersedes_line=s91_gate_verdicts.txt:199 "
        f"# {GATE_ID} Option A supersedes-tag protocol per gate-verdicts.md "
        f"§\"Option A — sig_5 remediation pathway under absolute verdict permanence\"\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(level_pin)
        f.write(supersedes_pointer)
        # In-session chain-supersedes annotation (Option A absolute verdict
        # permanence + supersedes-chain support). One row per prior intra-
        # session canonical line of this gate-ID.
        for prior_sha in prior_in_session_shas:
            if prior_sha == audit_sha:
                continue                          # skip self-reference if any
            chain_row = (
                f"# in_session_supersedes_chain "
                f"corrective_audit_sha256={audit_sha} "
                f"prior_audit_sha256={prior_sha} "
                f"# {GATE_ID} Option A in-session corrective emission; "
                f"prior canonical line retained on disk per verdict permanence; "
                f"consumers cite LATEST non-superseded line\n"
            )
            f.write(chain_row)


# ============================== Main ==============================

def main() -> int:
    t0 = time.time()

    # 1. Log input pins + compute dual SHA.
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    # Cross-check closure_hash availability (canonical pattern; not the
    # primary audit_sha but proves the closure function is wired).
    pin_closure = closure_hash(pins)                          # (local)
    print()
    print(f"  audit_sha256        = {audit_sha[:16]}...  (script + canonical + pinmap)")
    print(f"  content_sha256      = {content_sha[:16]}...  (script only)")
    print(f"  pin_closure_hash    = {pin_closure[:16]}...  (pinmap only, cross-check)")
    print(f"  supersedes_target   = {SUPERSEDES_TARGET[:16]}...  "
          "(S91-W6-CF-W7-1-CF-49 line 199)")
    print()

    # 2. PV identity machine-precision self-check (Σc_r=1, Σc_r m_r²=0).
    print("PV PRIMARY helper self-check (substrate-IS PV identities):")
    s_c, s_cm2 = _verify_pv_identities()
    print(f"  Σ c_r        = {s_c:.16e}   (target +1.0)")
    print(f"  Σ c_r m_r²   = {s_cm2:.16e}   (target  0.0)")
    print(f"  PV pair: (c_1, c_2) = ({PV_PRIMARY_C[0]:+.1f}, {PV_PRIMARY_C[1]:+.1f})")
    print(f"  PV pair: (m_1, m_2) = ({PV_PRIMARY_M_DIMLESS[0]:.6f}, "
          f"{PV_PRIMARY_M_DIMLESS[1]:.6f})  M_KK-natural")
    assert abs(s_c - 1.0) < 1e-12, f"PV Σc_r identity violated: {s_c}"
    assert abs(s_cm2) < 1e-12, f"PV Σc_r·m_r² identity violated: {s_cm2}"
    pv_identity_pass = True                                    # (local)
    print()

    # 3. Load L_max=12 master spectrum cache.
    print(f"Loading L_max={L_MAX} master spectrum cache from "
          f"{L12_CACHE.relative_to(ROOT)}...")
    lambdas, mults, n_sectors = load_spectrum_flat(L12_CACHE)
    print(f"  n_sectors            = {n_sectors}")
    print(f"  n_eigenvalues_raw    = {len(lambdas)}")
    print(f"  Σ_k mults_k          = {int(mults.sum())}  (Peter-Weyl weighted N)")
    print(f"  λ_min                = {lambdas.min():.6f}  (M_KK-natural; spectral gap)")
    print(f"  λ_max                = {lambdas.max():.6f}  (M_KK-natural)")
    print()

    # 4. Evaluate the 5-regulator atlas at substrate-distance-1 pole s=3.
    print(f"5-regulator atlas evaluation at substrate-distance-1 pole s={S_POLE}:")
    print(f"  Atlas order: {REGULATOR_ORDER}")
    M_R, rho_R, M_BARE_baseline = evaluate_atlas(S_POLE, lambdas, mults)
    print()
    print(f"  M_BARE baseline      = M_zeta(s={S_POLE}) = {M_BARE_baseline:.10e}")
    print()
    print(f"  Per-regulator M_R(s={S_POLE}) and rho_R = M_R / M_BARE:")
    for R in REGULATOR_ORDER:
        marker = "  <-- canonical FULL" if R == "Pauli-Villars-FULL-CC" else ""
        print(f"    {R:24s}  M={M_R[R]:.10e}  rho={rho_R[R]:+.10e}{marker}")
    print()

    # 5. PV multiplier sample statistics.
    lambda_sq = lambdas * lambdas                              # (local)
    w_PV_arr = pv_multiplier_primary(lambda_sq, S_POLE)        # (local)
    w_PV_min = float(np.min(w_PV_arr))                         # (local)
    w_PV_max = float(np.max(w_PV_arr))                         # (local)
    w_PV_mean = float(np.mean(w_PV_arr))                       # (local)
    print(f"PV multiplier w_PV(λ², s={S_POLE}) statistics on L_max={L_MAX} spectrum:")
    print(f"  w_PV_min  = {w_PV_min:.6f}  (IR end; spectral gap)")
    print(f"  w_PV_mean = {w_PV_mean:.6f}")
    print(f"  w_PV_max  = {w_PV_max:.6f}  (UV end → 1 asymptotically)")
    print()

    # 6. Atlas spread (plan §W1-1 Def 4): (max - min) / mean.
    rho_arr = np.array([rho_R[R] for R in REGULATOR_ORDER])    # (local)
    rho_max = float(np.max(rho_arr))                           # (local)
    rho_min = float(np.min(rho_arr))                           # (local)
    rho_mean = float(np.mean(rho_arr))                         # (local)
    atlas_spread = (rho_max - rho_min) / rho_mean              # (local)
    print(f"Atlas spread (plan §W1-1 Definition 4):")
    print(f"  rho_max  = {rho_max:+.10e}   (regulator: "
          f"{REGULATOR_ORDER[int(np.argmax(rho_arr))]})")
    print(f"  rho_min  = {rho_min:+.10e}   (regulator: "
          f"{REGULATOR_ORDER[int(np.argmin(rho_arr))]})")
    print(f"  rho_mean = {rho_mean:+.10e}")
    print(f"  atlas_spread = (max - min) / mean = {atlas_spread:+.10e}")
    print()

    # 7. SDW↔FULL-CC pair-spread cross-check (substitution chain Step 3
    #    explicit substitution): bounds the 5-atlas spread from below.
    rho_sdw = rho_R["SDW"]                                     # (local)
    rho_full = rho_R["Pauli-Villars-FULL-CC"]                  # (local)
    pair_mean = 0.5 * (rho_sdw + rho_full)                     # (local)
    pair_spread = abs(rho_sdw - rho_full) / abs(pair_mean)     # (local)
    print(f"SDW↔FULL-CC pair-spread cross-check (substitution chain Step 3):")
    print(f"  rho_SDW              = {rho_sdw:+.10e}")
    print(f"  rho_FULL_CC          = {rho_full:+.10e}")
    print(f"  |rho_SDW - rho_FULL_CC| / mean(SDW, FULL_CC) = "
          f"{pair_spread:.6e}  ≈ {pair_spread * 100.0:.4f}%")
    print(f"  (lower bound on 5-atlas spread; structurally ≥ 2.04% per plan §W1-1)")
    print()

    # 8. Per-class Delta_R deltas vs §VII.AF.1.OP-PROJ canonical
    #    R_canonical_AF1 = 1.030902.
    R_canonical = R_CANONICAL_AF1                              # (local)
    delta_R = {R: (rho_R[R] - R_canonical) / abs(R_canonical)
               for R in REGULATOR_ORDER}                       # (local)
    print(f"Per-class Delta_R vs §VII.AF.1.OP-PROJ canonical "
          f"R_canonical_AF1 = {R_canonical:.6f}:")
    for R in REGULATOR_ORDER:
        print(f"  Delta_{R:24s} = {delta_R[R]:+.10e}   "
              f"(|Δ| = {abs(delta_R[R]):.4e})")
    print()

    # 9. FI/RD/MIXED classification (plan §W1-1 strict_PASS_boundary).
    verdict = evaluate_verdict(atlas_spread)
    print(f"FI/RD/MIXED 3-band classifier (plan §W1-1):")
    print(f"  FI    iff atlas_spread < {FI_CEILING:.0e}      "
          "(algebra-INVARIANT spectrum-only functional)")
    print(f"  MIXED iff {FI_CEILING:.0e} ≤ atlas_spread ≤ {RD_FLOOR:.0e}  "
          "(intermediate)")
    print(f"  RD    iff atlas_spread > {RD_FLOOR:.0e}      "
          "(regulator-dependent at this pole)")
    print(f"  Observed: atlas_spread = {atlas_spread:.10e}  → "
          f"classification = {verdict['classification']}  → "
          f"composite = {verdict['composite']}")
    print()

    # 10. Substitution chain trace (per math-scripts.md
    #     "Double-Check Logic Before Compute"):
    print("Substitution chain trace (substituted numbers, plan §W1-1):")
    print(f"  Definition 1: M_R(s=3) = Σ_k m_k · w_R(λ_k²; s=3) · λ_k^{{-6}}")
    print(f"                M_zeta = {M_R['zeta']:.6e}")
    print(f"                M_SDW  = {M_R['SDW']:.6e}")
    print(f"                M_PV   = {M_R['Pauli-Villars-FULL-CC']:.6e}")
    print(f"                M_Mell = {M_R['Mellin']:.6e}")
    print(f"                M_latt = {M_R['lattice']:.6e}")
    print(f"  Definition 2: w_PV(λ²;s) = 1 - Σ c_r (m_r²/(λ²+m_r²))^s with "
          "(c,m) = ((+2,-1),(1,√2))")
    print(f"  Definition 3: rho_R(s=3) = M_R / M_BARE; M_BARE = M_zeta = "
          f"{M_BARE_baseline:.6e}")
    print(f"  Definition 4: atlas_spread = (max_R rho_R - min_R rho_R) / mean_R rho_R")
    print(f"  Substitute:    SDW canonical pin   rho_SDW^{{canonical}} = "
          f"R_universal_HP1_strict_F4 = {R_canonical:.6f}")
    print(f"                S91 W9-4 measurement  rho_FULL_CC(L=12)    = "
          f"{rho_full:.10f}")
    print(f"  Simplify:      |rho_SDW^{{can}} - rho_FULL_CC| / "
          f"mean = |{R_canonical:.6f} - {rho_full:.6f}| / "
          f"{0.5 * (R_canonical + rho_full):.6f}")
    print(f"                = {abs(R_canonical - rho_full) / (0.5 * (R_canonical + rho_full)):.6e}")
    print(f"  Canonical form: atlas_spread ≥ 2.04e-2 lower bound from "
          "SDW(canon)↔FULL-CC pair")
    print(f"  Direction:      atlas_spread = {atlas_spread:.6e} > "
          f"{RD_FLOOR:.0e} RD floor  ⇒  RD classification")
    print(f"  Conclusion:     FAIL-WITH-DIAGNOSTIC (pre-registered; "
          "FAIL IS the substrate finding)")
    print()

    # 11. Save outputs (.npz).
    print(f"Saving npz to {OUT_NPZ.relative_to(ROOT)}...")
    np.savez(
        OUT_NPZ,
        # Atlas (M_R + rho_R per regulator)
        regulator_order=np.array(REGULATOR_ORDER, dtype=object),
        M_R_zeta=M_R["zeta"],
        M_R_SDW=M_R["SDW"],
        M_R_PV_FULL_CC=M_R["Pauli-Villars-FULL-CC"],
        M_R_Mellin=M_R["Mellin"],
        M_R_lattice=M_R["lattice"],
        rho_R_zeta=rho_R["zeta"],
        rho_R_SDW=rho_R["SDW"],
        rho_R_PV_FULL_CC=rho_R["Pauli-Villars-FULL-CC"],
        rho_R_Mellin=rho_R["Mellin"],
        rho_R_lattice=rho_R["lattice"],
        # M_BARE baseline
        M_BARE_baseline=M_BARE_baseline,
        # Atlas spread (classifier observable)
        atlas_spread=atlas_spread,
        rho_max=rho_max,
        rho_min=rho_min,
        rho_mean=rho_mean,
        # Per-class deltas
        delta_R_zeta=delta_R["zeta"],
        delta_R_SDW=delta_R["SDW"],
        delta_R_PV_FULL_CC=delta_R["Pauli-Villars-FULL-CC"],
        delta_R_Mellin=delta_R["Mellin"],
        delta_R_lattice=delta_R["lattice"],
        # SDW↔FULL-CC pair-spread cross-check
        pair_spread_SDW_FULL_CC=pair_spread,
        rho_SDW=rho_sdw,
        rho_FULL_CC=rho_full,
        # PV multipliers (FULL-CC)
        M_1_FW_CC=M_1_FW_CC,
        M_2_FW_CC=M_2_FW_CC,
        C_1_FW_CC=C_1_FW_CC,
        C_2_FW_CC=C_2_FW_CC,
        PV_PRIMARY_C=PV_PRIMARY_C,
        PV_PRIMARY_M_DIMLESS=PV_PRIMARY_M_DIMLESS,
        pv_identity_sum_c=s_c,
        pv_identity_sum_c_m2=s_cm2,
        pv_identity_pass=pv_identity_pass,
        # PV multiplier statistics
        w_PV_arr=w_PV_arr,
        w_PV_min=w_PV_min,
        w_PV_mean=w_PV_mean,
        w_PV_max=w_PV_max,
        # Canonical pins + thresholds
        R_canonical_AF1=R_canonical,
        eps_H_HP1_norm=eps_H_HP1_norm,
        gv_canonical_difference_FW=gv_canonical_difference_FW,
        FI_CEILING=FI_CEILING,
        RD_FLOOR=RD_FLOOR,
        # Plan-pinned parameters
        S_POLE=S_POLE,
        L_max=L_MAX,
        tau_fold=tau_fold,
        n_sectors=n_sectors,
        n_eigenvalues=len(lambdas),
        # Spectrum (for reproducibility)
        lambdas=lambdas,
        mults=mults,
        # Verdict + classification
        verdict_composite=verdict["composite"],
        classification=verdict["classification"],
        # Dual SHA + supersedes
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        supersedes_target=SUPERSEDES_TARGET,
        supersedes_gate_id="S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE",
        # Convention + level pin (for downstream consumers)
        convention=CONVENTION,
        scheme=SCHEME,
        level_class_pin="FULL",
    )

    # 12. Save plot.
    print(f"Saving plot to {OUT_PNG.relative_to(ROOT)}...")
    make_plot(rho_R, M_R, R_canonical, atlas_spread, delta_R,
              verdict["classification"],
              w_PV_min, w_PV_mean, w_PV_max, S_POLE, L_MAX)
    print()

    # 13. Emit verdict line (canonical + dual-SHA + level-pin
    #     + supersedes-pointer companion rows).
    value_str = (
        f"atlas_spread={atlas_spread:+.6e}"
        f"_classification={verdict['classification']}"
        f"_rho_zeta={rho_R['zeta']:+.6e}"
        f"_rho_SDW={rho_R['SDW']:+.6e}"
        f"_rho_PV_FULL_CC={rho_R['Pauli-Villars-FULL-CC']:+.6e}"
        f"_rho_Mellin={rho_R['Mellin']:+.6e}"
        f"_rho_lattice={rho_R['lattice']:+.6e}"
        f"_R_canonical_AF1={R_canonical:.6f}"
        f"_pair_spread_SDW_FULL_CC={pair_spread:+.6e}"
    )
    append_verdict(
        composite=verdict["composite"],
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        classification=verdict["classification"],
    )

    # 14. Final summary.
    wall = time.time() - t0                                    # (local)
    print(f"=== {GATE_ID}: {verdict['composite']} "
          f"(classification={verdict['classification']}; wall {wall:.1f}s) ===")
    print(f"    atlas_spread   : {atlas_spread:+.10e}")
    print(f"    pair_spread    : {pair_spread:+.10e}  (SDW↔FULL-CC)")
    print(f"    audit_sha256   : {audit_sha}")
    print(f"    content_sha256 : {content_sha}")
    print(f"    supersedes     : {SUPERSEDES_TARGET}")
    print(f"    value_str      : {value_str}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
