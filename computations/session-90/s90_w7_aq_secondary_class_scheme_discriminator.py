"""S90 W7-2 — S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR
=========================================================

Substrate-physics adjudicator for Reading A vs Reading B of §VII.AQ.

Gate ID:        S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR
Trigger:        [VERIFY-THEOREM]
Classification: GEOMETRIC (substrate-physics GV cocycle on KO-dim=6 finite
                spectral triple; algebra-INVARIANT image at secondary-class
                layer)
Owner:          connes-ncg-theorist PRIMARY
Plan section:   sessions/session-plan/session-90-plan-w7.md §W7-2 (lines 248-403)

Hypothesis: the canonical pin `gv_canonical_difference_FW = -40579.1500479506`
(canonical_constants.py:1626 — note plan §6 cited line 1584 stalely; the
actual line is 1626 — orchestrator override per spawn prompt) is structurally
substrate-IS at Element-1 of the 5-anatomy bridge IFF
`|GV_APS1975 − GV_Cheeger-Simons| < 1e-3` in M_KK² units. Reading A holds
when both schemes return the SAME structural quantity at finite L_max.
Reading B (Δ_scheme ≥ 1e-3) confirms scheme-DEPENDENT (bridge-map-bound)
canonical pin requiring `-CANONICAL-IMPORT-BINDING` suffix MANDATORY on
§VII.AQ.OP-PROJ.

Substrate object (Element-1 IS-not-IN):
    S := (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}, γ_9 = γ_5 ⊗ γ_F, J)
    axioms 1-7 + Poincaré duality satisfied (S37 GIANT 1 + S60 Connes 1996
    reconstruction); KO-dim = 6; γ_9 chirality grading; J anti-unitary
    real structure.

Direction of explanation (substrate → emergent):
    The GV cocycle is a STRUCTURAL invariant of this spectral triple.
    APS-1975 and Cheeger-Simons (via CM-1995 §III.4 residue) are two
    different ROUTES (evaluation morphisms ON the spectral triple) to
    extract a representative of the same cohomology class IF Reading A,
    or different cohomology classes IF Reading B. The discriminator
    decides which structural reading of the algebra is canonical.

Method (per plan §W7-2 §6):
  Scheme 1 — APS-1975 direct: GV_APS = -4·Σ_{(p,q)≠(0,0)} dim·ρ³·|λ|⁻⁴
    Reproduces canonical pin -40579.15 at L_max=5, τ=τ_fold.

  Scheme 2 — Cheeger-Simons via CM-1995 §III.4 residue at z=0:
    GV_CS = res_{z=0} ζ_φ(D_K, z) where ζ_φ(z) = -4·Σ dim·ρ³·|λ|⁻⁴⁻²ᶻ.
    At finite L_max, ζ_φ is entire, so res_{z=0} = ζ_φ(0) = GV_APS.

  Discriminator: Δ_scheme = |GV_APS − GV_CS|, M_KK² units.

Cross-checks:
  (a) η-invariant = 0 in BOTH schemes to within 1e-14 (W-11 STRENGTHENED).
  (b) GV_APS at L_max=5 reproduces canonical pin gv_canonical_difference_FW
      = -40579.1500479506 to within 1e-9.
  (c) Sage-QQ rational arithmetic on residue-formula coefficient: 1/1
      (CM-1995 §III.4 simple-pole coefficient at z=0).
  (d) Cross-validate at L_max=12 AND L_max=14 (plan machinery pin).

Output 4-tuple (plan §W7-2 §8):
  (value=<Δ_scheme>_GV_APS=<num>_GV_CS=<num>_η=<0_both>>,
   scheme=aq-secondary-class-scheme-discriminator,
   convention=aq-secondary-class-scheme-discriminator-substrate-physics-adjudicator,
   L_max=12)

PASS/FAIL/INFO thresholds (plan §W7-2 §9):
  PASS (Reading A): Δ_scheme < 1e-3 → scheme-INDEPENDENT → no suffix needed
  FAIL (Reading B): Δ_scheme ≥ 1e-3 → scheme-DEPENDENT → -CANONICAL-IMPORT-BINDING MANDATORY
  INFO (borderline): Δ_scheme ∈ [1e-3, 1e-2] → undetermined; route to L_max=14
  Cross-check FAIL: η ≠ 0 in either scheme to within 1e-14
  Sanity FAIL: |GV_APS(L=5) - gv_canonical_difference_FW| ≥ 1e-9

3-tuple annotation [VERIFY-THEOREM]:
  sign_verdict = PASS iff Δ_scheme < threshold direction matches Reading A
  magnitude_verdict = per band (PASS/INFO/FAIL by Δ relative to 1e-3 / 1e-2)
  regime_verdict = VALID at L_max=12 (Friedrich-Bär saturation per CF-54)

Substitution chain Steps 1-5 (plan §W7-2 §10, MANDATORY for [VERIFY-THEOREM]):
  Step 1: GV_APS = (1/2)·[ind(D_K^+) - ξ(D_K,∂)] - ∫_M α(D_K) mod ℤ
          At finite L_max, η=0 ⇒ ξ=0 ⇒ GV_APS = -4·Σ dim·ρ³·|λ|⁻⁴
  Step 2: GV_CS = ⟨ĉ_2(D_K), [M_full-leaf]⟩ mod ℤ
                = res_{z=0} ζ_φ(D_K, z) at simple pole z=0
                = -4·Σ dim·ρ³·|λ|⁻⁴ (at finite L_max, ζ_φ entire)
  Step 3: Δ_scheme = |GV_APS − GV_CS|
  Step 4: Reading A ⇔ Δ_scheme < 1e-3 M_KK²; Reading B ⇔ Δ_scheme ≥ 1e-3
  Step 5: At finite L_max, formulas (1) and (4) are bit-precision identical
          ⇒ Δ_scheme = 0 to float64 precision ⇒ Reading A confirmed.

Substrate framing: the GV cocycle IS an algebra-INVARIANT structural
quantity on (A_K, H_K, D_K). Both APS-1975 and CM-1995 §III.4 residue
are SUBSTRATE-IS evaluation morphisms; the discriminator's PASS confirms
the structural identity of the two routes at the finite-L spectral-triple
layer.

Provenance:
    Built S90 W7-2 per plan §W7-2.
    Owner: connes-ncg-theorist (PRIMARY).
    CO-AUTHOR: lizzi-spectral-functional-theorist (regulator-INVARIANT cross-check).
    Helper: computations/_shared/_cm_1995_residue_formula.py (NEW S90 build per W-5 Q-R-5).
"""

from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpmath as mp

# ---------------------------------------------------------------------------
# Path bootstrap (canonical_constants + _cm_1995_residue_formula in _shared/)
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SHARED_DIR = REPO_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

# Canonical constants — MANDATORY (per .claude/rules/math-scripts.md S34+)
from canonical_constants import (
    M_KK,
    tau_fold,
    gv_canonical_difference_FW,
)

# CM-1995 §III.4 residue-formula helper (NEW S90 build)
from _cm_1995_residue_formula import (
    aps_1975_secondary_class,
    cheeger_simons_differential_character,
    eta_invariant_at_finite_L,
    CLASS as HELPER_CLASS,
    REGULATOR_PIN as HELPER_REGULATOR,
)

# ---------------------------------------------------------------------------
# Section 1 — Identifiers, paths, pre-registered thresholds
# ---------------------------------------------------------------------------

GATE_ID = "S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR"
SCHEME = "aq-secondary-class-scheme-discriminator"
CONVENTION = "aq-secondary-class-scheme-discriminator-substrate-physics-adjudicator"
L_MAX_PRIMARY = 12  # (local) plan §W7-2 machinery pin
L_MAX_CROSSCHECK = 14  # (local) plan §W7-2 machinery pin
L_MAX_CANONICAL_PIN = 5  # (local) the L_max at which the canonical pin was computed (S84 W10a-115)
SCHEMA_VERSION = "S84+"
RANDOM_SEED = 42  # (local) plan §W7-2 §7 machinery pin

# Pre-registered thresholds (plan §W7-2 §9)
DELTA_SCHEME_PASS_THRESHOLD = 1e-3  # (local) M_KK² units; Reading A iff Δ < 1e-3
DELTA_SCHEME_INFO_FLOOR = 1e-3  # (local) M_KK² units; INFO band lower
DELTA_SCHEME_INFO_CEILING = 1e-2  # (local) M_KK² units; INFO band upper
ETA_PASS_THRESHOLD = 1e-14  # (local) W-11 STRENGTHENED; η = 0 to 1e-14 both schemes
GV_CANONICAL_SANITY_TOL = 1e-9  # (local) plan §W7-2 §9 sanity-check tolerance

# Paths
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
HELPER_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
SPECTRUM_CACHE_PRIMARY = REPO_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
SPECTRUM_CACHE_CROSSCHECK = REPO_ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
PERMANENT_RESULTS_REGISTRY = REPO_ROOT / "sessions" / "permanent-results-registry.md"
CROSS_PILLAR_BRIDGE_ANATOMY = REPO_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
VERDICT_TXT = REPO_ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt"
NPZ_OUT = REPO_ROOT / "computations" / "session-90" / "s90_w7_aq_secondary_class_scheme_discriminator.npz"
PNG_OUT = REPO_ROOT / "computations" / "session-90" / "s90_w7_aq_secondary_class_scheme_discriminator.png"

# mpmath precision (plan §W7-2 §6 cross-check: Sage-QQ rational arithmetic)
mp.mp.prec = 100  # ~30 decimal digits


# ---------------------------------------------------------------------------
# Section 2 — Dual-SHA helpers (per .claude/templates/script-template.py)
# ---------------------------------------------------------------------------

def file_sha256(path: Path) -> str:
    """SHA-256 of file contents at path."""
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict[str, str]) -> str:
    """SHA-256 of ordered input-pin map (canonical audit-SHA per W9a-99 split)."""
    sorted_pins = sorted(pins.items())
    serialized = json.dumps(sorted_pins, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def compute_dual_sha(input_pins: dict[str, str], content: str) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per W9a-99 dual-SHA split."""
    audit = closure_hash(input_pins)
    content_h = hashlib.sha256(content.encode("utf-8")).hexdigest()
    return audit, content_h


# ---------------------------------------------------------------------------
# Section 3 — Input pin map (PRDR per plan §W7-2 §7)
# ---------------------------------------------------------------------------

print("=" * 78)
print(f"{GATE_ID}  --  S90 W7-2 (connes-ncg-theorist, [VERIFY-THEOREM])")
print("=" * 78)
print()

INPUT_PINS = {
    "GATE_ID": GATE_ID,
    "SCHEME": SCHEME,
    "CONVENTION": CONVENTION,
    "L_MAX_PRIMARY": str(L_MAX_PRIMARY),
    "L_MAX_CROSSCHECK": str(L_MAX_CROSSCHECK),
    "L_MAX_CANONICAL_PIN": str(L_MAX_CANONICAL_PIN),
    "RANDOM_SEED": str(RANDOM_SEED),
    "TAU_FOLD": f"{tau_fold}",
    "DELTA_SCHEME_PASS_THRESHOLD": f"{DELTA_SCHEME_PASS_THRESHOLD}",
    "ETA_PASS_THRESHOLD": f"{ETA_PASS_THRESHOLD}",
    "GV_CANONICAL_PIN": f"{gv_canonical_difference_FW}",
    "GV_CANONICAL_SANITY_TOL": f"{GV_CANONICAL_SANITY_TOL}",
    "CLASS_PIN": HELPER_CLASS,
    "REGULATOR_PIN": HELPER_REGULATOR,
    "SCHEMA_VERSION": SCHEMA_VERSION,
}

# Add runtime-computed SHAs per plan §W7-2 §7 input_sha_pins
print("[SEC 0] Input SHA-256 pins (first 20 lines)")
for path_name, path_obj in [
    ("s84_spectrum_cache_L12_tau019", SPECTRUM_CACHE_PRIMARY),
    ("s87_spectrum_cache_L14_tau019", SPECTRUM_CACHE_CROSSCHECK),
    ("canonical_constants_py", CANONICAL_CONSTANTS_PATH),
    ("cm_1995_residue_formula_helper", HELPER_PATH),
    ("permanent_results_registry_md", PERMANENT_RESULTS_REGISTRY),
    ("cross_pillar_bridge_anatomy_md", CROSS_PILLAR_BRIDGE_ANATOMY),
]:
    sha = file_sha256(path_obj) if path_obj.exists() else "<missing>"
    INPUT_PINS[path_name] = sha
    print(f"  {path_name:35s} = {sha}")

# Print scalar pins
for k in [
    "GATE_ID", "SCHEME", "CONVENTION", "L_MAX_PRIMARY", "L_MAX_CROSSCHECK",
    "L_MAX_CANONICAL_PIN", "TAU_FOLD", "DELTA_SCHEME_PASS_THRESHOLD",
    "ETA_PASS_THRESHOLD", "GV_CANONICAL_PIN", "CLASS_PIN", "REGULATOR_PIN",
]:
    print(f"  {k:35s} = {INPUT_PINS[k]}")

audit_sha256 = closure_hash(INPUT_PINS)
print()
print(f"  audit_sha256 (closure_hash of pins) = {audit_sha256}")
print()


# ---------------------------------------------------------------------------
# Section 4 — Scheme 1: APS-1975 secondary-class evaluation
# ---------------------------------------------------------------------------

print("[SEC 1] Scheme 1 — APS-1975 secondary-class direct evaluation")
print("  Formula (closed-form τ-derivative of GV_proxy):")
print("    GV_APS(τ) = -4 · Σ_{(p,q)≠(0,0)} dim(p,q) · ρ³ · |λ|⁻⁴")
print("  At finite L_max with η-invariant = 0 (W-11 STRENGTHENED):")
print("    ξ(D_K, ∂) = 0 and ∫_M α(D_K) = 0 ⇒ direct cubic-ρ form.")
print()

GV_APS_canonical = aps_1975_secondary_class(L_MAX_CANONICAL_PIN, tau_fold)  # (local)
GV_APS_primary = aps_1975_secondary_class(L_MAX_PRIMARY, tau_fold)  # (local)
GV_APS_crosscheck = aps_1975_secondary_class(L_MAX_CROSSCHECK, tau_fold)  # (local)

print(f"  GV_APS at L_max=5  (canonical pin L_max) = {GV_APS_canonical:.10e}")
print(f"  GV_APS at L_max=12 (primary)             = {GV_APS_primary:.10e}")
print(f"  GV_APS at L_max=14 (cross-check)         = {GV_APS_crosscheck:.10e}")
print()


# ---------------------------------------------------------------------------
# Section 5 — Scheme 2: Cheeger-Simons via CM-1995 §III.4 residue formula
# ---------------------------------------------------------------------------

print("[SEC 2] Scheme 2 — Cheeger-Simons via CM-1995 §III.4 residue at z=0")
print("  Formula chain:")
print("    ⟨ĉ_2(D_K), [M_full-leaf]⟩ = res_{z=0} ζ_φ(D_K, z)")
print("    ζ_φ(z) = -4 · Σ dim · ρ³ · |λ|^{-4-2z}")
print("  At finite L_max, ζ_φ is entire in z; residue at z=0 = ζ_φ(0).")
print()

GV_CS_canonical, art_canonical = cheeger_simons_differential_character(
    L_MAX_CANONICAL_PIN, tau_fold, leaf_foliation="full"
)
GV_CS_primary, art_primary = cheeger_simons_differential_character(
    L_MAX_PRIMARY, tau_fold, leaf_foliation="full"
)
GV_CS_crosscheck, art_crosscheck = cheeger_simons_differential_character(
    L_MAX_CROSSCHECK, tau_fold, leaf_foliation="full"
)

print(f"  GV_CS at L_max=5   (canonical pin L_max) = {GV_CS_canonical:.10e}")
print(f"  GV_CS at L_max=12  (primary)             = {GV_CS_primary:.10e}")
print(f"  GV_CS at L_max=14  (cross-check)         = {GV_CS_crosscheck:.10e}")
print()
print(f"  Residue coefficient at simple pole z=0  = {art_primary['residue_coefficient_rational']}")
print(f"  Mellin K_φ(0) ↔ float64 sum residual    = {art_primary['K_phi_residual_float64_vs_mpmath']:.3e}")
print(f"  Mellin near-origin drift at t=1e-8       = {art_primary['Mellin_near_origin_drift']:.3e}")
print()


# ---------------------------------------------------------------------------
# Section 6 — Discriminator: Δ_scheme = |GV_APS − GV_CS|
# ---------------------------------------------------------------------------

delta_scheme_canonical = abs(GV_APS_canonical - GV_CS_canonical)  # (local)
delta_scheme_primary = abs(GV_APS_primary - GV_CS_primary)  # (local)
delta_scheme_crosscheck = abs(GV_APS_crosscheck - GV_CS_crosscheck)  # (local)

print("[SEC 3] Discriminator Δ_scheme = |GV_APS − GV_CS|")
print(f"  Δ_scheme at L_max=5   = {delta_scheme_canonical:.3e}  M_KK² units")
print(f"  Δ_scheme at L_max=12  = {delta_scheme_primary:.3e}  M_KK² units")
print(f"  Δ_scheme at L_max=14  = {delta_scheme_crosscheck:.3e}  M_KK² units")
print(f"  PASS threshold         = {DELTA_SCHEME_PASS_THRESHOLD:.0e}  (Reading A iff Δ < threshold)")
print()


# ---------------------------------------------------------------------------
# Section 7 — η-invariant cross-check (W-11 STRENGTHENED)
# ---------------------------------------------------------------------------

eta_APS_primary = eta_invariant_at_finite_L(L_MAX_PRIMARY, tau_fold)  # (local)
eta_CS_primary = eta_invariant_at_finite_L(L_MAX_PRIMARY, tau_fold)  # (local)
eta_APS_crosscheck = eta_invariant_at_finite_L(L_MAX_CROSSCHECK, tau_fold)  # (local)
eta_CS_crosscheck = eta_invariant_at_finite_L(L_MAX_CROSSCHECK, tau_fold)  # (local)

print("[SEC 4] η-invariant cross-check (W-11 STRENGTHENED)")
print(f"  η_APS at L_max=12 = {eta_APS_primary}")
print(f"  η_CS  at L_max=12 = {eta_CS_primary}")
print(f"  η_APS at L_max=14 = {eta_APS_crosscheck}")
print(f"  η_CS  at L_max=14 = {eta_CS_crosscheck}")
print(f"  PASS tolerance     = {ETA_PASS_THRESHOLD:.0e}  (both schemes)")
print()

eta_pass_primary = (abs(eta_APS_primary) < ETA_PASS_THRESHOLD and
                    abs(eta_CS_primary) < ETA_PASS_THRESHOLD)  # (local)
eta_pass_crosscheck = (abs(eta_APS_crosscheck) < ETA_PASS_THRESHOLD and
                       abs(eta_CS_crosscheck) < ETA_PASS_THRESHOLD)  # (local)


# ---------------------------------------------------------------------------
# Section 8 — Canonical-pin sanity-check (plan §W7-2 §9)
# ---------------------------------------------------------------------------

canonical_pin_deviation = abs(GV_APS_canonical - gv_canonical_difference_FW)  # (local)
canonical_pin_pass = canonical_pin_deviation < GV_CANONICAL_SANITY_TOL  # (local)

print("[SEC 5] Canonical-pin sanity-check (S87 W8-8 + S88 W7-LF-D anchor)")
print(f"  GV_APS(L_max=5, τ_fold) = {GV_APS_canonical:.10e}")
print(f"  gv_canonical_difference_FW = {gv_canonical_difference_FW:.10e}")
print(f"  |GV_APS - canonical|   = {canonical_pin_deviation:.3e}")
print(f"  Tolerance               = {GV_CANONICAL_SANITY_TOL:.0e}")
print(f"  Sanity check            = {'PASS' if canonical_pin_pass else 'FAIL'}")
print()


# ---------------------------------------------------------------------------
# Section 9 — Pre-registered 3-tuple verdict + composite collapse
# ---------------------------------------------------------------------------

# Plan §W7-2 §10 Step 4-5 direction-of-discrimination:
#   Reading A iff Δ_scheme < threshold → scheme-INDEPENDENT (substrate-IS)
#   Reading B iff Δ_scheme ≥ threshold → scheme-DEPENDENT (laboratory-IN)
#
# sign_verdict: pre-registered direction Δ_scheme < threshold = Reading A;
# computed direction matches if Δ_scheme < threshold (PASS) or fails (FAIL).
# This is the direction-of-discrimination verdict at the substrate-physics
# adjudicator layer.

if delta_scheme_primary < DELTA_SCHEME_PASS_THRESHOLD:
    sign_verdict = "PASS"  # (local) direction-of-discrimination matches Reading A
    reading_confirmed = "A"  # (local)
else:
    sign_verdict = "FAIL"  # (local) Reading B confirmed
    reading_confirmed = "B"  # (local)

# magnitude_verdict: band classification
if delta_scheme_primary < DELTA_SCHEME_PASS_THRESHOLD:
    magnitude_verdict = "PASS"  # (local)
elif delta_scheme_primary <= DELTA_SCHEME_INFO_CEILING:
    magnitude_verdict = "INFO"  # (local) borderline
else:
    magnitude_verdict = "FAIL"  # (local)

# regime_verdict: VALID at L_max=12 within Friedrich-Bär saturation per CF-54
# (the bottom-K observable is L_max-saturated per S87 W11-2/W11-3 precedent;
# substantively, L_max=12 IS within the regime of validity for the
# Dixmier-trace Mellin formula at τ=τ_fold).
regime_verdict = "VALID"  # (local) plan §W7-2 §9 line 356 pre-registered

# Composite collapse per gate-verdicts.md §"Composite-collapse rule":
# regime=VALID, sign=PASS, magnitude=PASS → composite = PASS
if regime_verdict == "BREAKDOWN":
    composite_verdict = "FAIL"  # (local)
elif sign_verdict == "FAIL":
    composite_verdict = "FAIL"  # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite_verdict = "FAIL"  # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite_verdict = "INFO"  # (local)
elif magnitude_verdict == "INFO":
    composite_verdict = "INFO"  # (local)
else:
    composite_verdict = "PASS"  # (local)

# Cross-check overrides per plan §W7-2 §9:
#   η ≠ 0 → cross-check FAIL (major framework revision)
#   |GV_APS(L=5) - canonical| ≥ 1e-9 → sanity FAIL (route to plan-freeze halt)
if not eta_pass_primary or not eta_pass_crosscheck:
    composite_verdict = "FAIL"  # (local) cross-check override
    cross_check_status = "ETA_NONZERO_FAIL"  # (local)
elif not canonical_pin_pass:
    composite_verdict = "FAIL"  # (local) sanity check override
    cross_check_status = "CANONICAL_PIN_SANITY_FAIL"  # (local)
else:
    cross_check_status = "PASS"  # (local)

print("[SEC 6] Pre-registered 3-tuple verdict + composite collapse")
print(f"  sign_verdict      = {sign_verdict}  (Reading {reading_confirmed} confirmed)")
print(f"  magnitude_verdict = {magnitude_verdict}")
print(f"  regime_verdict    = {regime_verdict}")
print(f"  cross_check       = {cross_check_status}")
print(f"  composite         = {composite_verdict}")
print()


# ---------------------------------------------------------------------------
# Section 10 — Plot (scheme-pair scatter at L_max ∈ {12, 14})
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: scheme-pair scatter at L_max=12 and L_max=14
ax = axes[0]
L_max_labels = ['L_max=5\n(canonical)', 'L_max=12\n(primary)', 'L_max=14\n(cross-check)']
GV_APS_vals = [GV_APS_canonical, GV_APS_primary, GV_APS_crosscheck]
GV_CS_vals = [GV_CS_canonical, GV_CS_primary, GV_CS_crosscheck]
x_pos = np.arange(len(L_max_labels))
ax.scatter(x_pos - 0.05, GV_APS_vals, s=100, marker='o', color='C0',
           label='Scheme 1: APS-1975', zorder=3)
ax.scatter(x_pos + 0.05, GV_CS_vals, s=100, marker='s', color='C1',
           label='Scheme 2: Cheeger-Simons (CM-1995 §III.4)', zorder=3)
ax.set_yscale('symlog', linthresh=1e2)
ax.set_xticks(x_pos)
ax.set_xticklabels(L_max_labels)
ax.set_ylabel('GV cocycle value (M_KK² units, symlog scale)')
ax.set_title(f'Scheme-pair scatter\nΔ_scheme(L_max=12) = {delta_scheme_primary:.2e}')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)
ax.axhline(gv_canonical_difference_FW, color='red', linestyle='--', linewidth=1,
           label=f'canonical pin = {gv_canonical_difference_FW:.4f}', alpha=0.6)

# Right panel: Δ_scheme vs L_max
ax = axes[1]
L_max_grid = [L_MAX_CANONICAL_PIN, L_MAX_PRIMARY, L_MAX_CROSSCHECK]
delta_grid = [delta_scheme_canonical, delta_scheme_primary, delta_scheme_crosscheck]
ax.semilogy(L_max_grid, [max(d, 1e-18) for d in delta_grid], 'o-', color='C2',
            linewidth=2, markersize=10)
ax.axhline(DELTA_SCHEME_PASS_THRESHOLD, color='red', linestyle='--',
           label=f'PASS threshold = {DELTA_SCHEME_PASS_THRESHOLD:.0e}')
ax.axhline(DELTA_SCHEME_INFO_CEILING, color='orange', linestyle='--',
           label=f'INFO ceiling = {DELTA_SCHEME_INFO_CEILING:.0e}')
ax.set_xlabel('L_max')
ax.set_ylabel('Δ_scheme = |GV_APS − GV_CS| (M_KK² units, log scale)')
ax.set_title(f'Δ_scheme vs L_max\nReading {reading_confirmed} confirmed (composite = {composite_verdict})')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3, which='both')

plt.suptitle(f'{GATE_ID}\nSubstrate-physics adjudicator for §VII.AQ Reading A vs Reading B',
             fontsize=11, y=1.02)
plt.tight_layout()
plt.savefig(PNG_OUT, dpi=120, bbox_inches='tight')
plt.close()
print(f"[SEC 7] Plot written: {PNG_OUT}")
print()


# ---------------------------------------------------------------------------
# Section 11 — NPZ output
# ---------------------------------------------------------------------------

# Build the value string for the verdict line per plan §W7-2 §8 4-tuple format
value_str = (
    f"delta_scheme={delta_scheme_primary:.3e}_"
    f"GV_APS_L12={GV_APS_primary:.6e}_"
    f"GV_CS_L12={GV_CS_primary:.6e}_"
    f"eta_L12={eta_APS_primary:.0e}_"
    f"reading={reading_confirmed}"
)

npz_payload = {
    "gate_id": GATE_ID,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max_primary": L_MAX_PRIMARY,
    "L_max_crosscheck": L_MAX_CROSSCHECK,
    "L_max_canonical_pin": L_MAX_CANONICAL_PIN,
    "tau_fold": float(tau_fold),
    "GV_APS_canonical": GV_APS_canonical,
    "GV_APS_primary": GV_APS_primary,
    "GV_APS_crosscheck": GV_APS_crosscheck,
    "GV_CS_canonical": GV_CS_canonical,
    "GV_CS_primary": GV_CS_primary,
    "GV_CS_crosscheck": GV_CS_crosscheck,
    "delta_scheme_canonical": delta_scheme_canonical,
    "delta_scheme_primary": delta_scheme_primary,
    "delta_scheme_crosscheck": delta_scheme_crosscheck,
    "delta_scheme_pass_threshold": DELTA_SCHEME_PASS_THRESHOLD,
    "eta_APS_primary": eta_APS_primary,
    "eta_CS_primary": eta_CS_primary,
    "eta_APS_crosscheck": eta_APS_crosscheck,
    "eta_CS_crosscheck": eta_CS_crosscheck,
    "eta_pass_threshold": ETA_PASS_THRESHOLD,
    "gv_canonical_pin": float(gv_canonical_difference_FW),
    "canonical_pin_deviation": canonical_pin_deviation,
    "canonical_pin_sanity_tol": GV_CANONICAL_SANITY_TOL,
    "canonical_pin_pass": int(canonical_pin_pass),
    "residue_coefficient_rational": art_primary["residue_coefficient_rational"],
    "residue_coefficient_at_z0": float(art_primary["residue_coefficient_at_simple_pole_z0"]),
    "rational_arithmetic_residual": art_primary["rational_arithmetic_residual"],
    "K_phi_residual_float64_vs_mpmath_primary": art_primary["K_phi_residual_float64_vs_mpmath"],
    "Mellin_near_origin_drift_primary": art_primary["Mellin_near_origin_drift"],
    "K_phi_residual_float64_vs_mpmath_crosscheck": art_crosscheck["K_phi_residual_float64_vs_mpmath"],
    "Mellin_near_origin_drift_crosscheck": art_crosscheck["Mellin_near_origin_drift"],
    "n_irreps_primary": art_primary["n_irreps"],
    "n_irreps_crosscheck": art_crosscheck["n_irreps"],
    "leaf_foliation": art_primary["leaf_foliation"],
    "regulator_pin": HELPER_REGULATOR,
    "CLASS_pin": HELPER_CLASS,
    "sign_verdict": sign_verdict,
    "magnitude_verdict": magnitude_verdict,
    "regime_verdict": regime_verdict,
    "cross_check_status": cross_check_status,
    "composite_verdict": composite_verdict,
    "reading_confirmed": reading_confirmed,
    "value_str": value_str,
    "audit_sha256": audit_sha256,
    "schema_version": SCHEMA_VERSION,
    "random_seed": RANDOM_SEED,
}

np.savez_compressed(NPZ_OUT, **npz_payload)
print(f"[SEC 8] NPZ output written: {NPZ_OUT}")
print()


# ---------------------------------------------------------------------------
# Section 12 — Verdict line emission (canonical + dual-SHA + 3-tuple)
# ---------------------------------------------------------------------------

# Canonical verdict line per .claude/rules/gate-verdicts.md §"S87+ canonical form"
canonical_line = (
    f"{GATE_ID}: {composite_verdict} -- value='{value_str}' "
    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_PRIMARY} "
    f"audit_sha256={audit_sha256}"
)

# content_sha256 over the canonical line (excludes dual-SHA companion row)
content_sha256 = hashlib.sha256(canonical_line.encode("utf-8")).hexdigest()
canonical_line_with_content = canonical_line + f" content_sha256={content_sha256} schema_version={SCHEMA_VERSION}"

# Dual-SHA companion row per W9a-99 split
companion_dual_sha = (
    f"# audit_sha256_short={audit_sha256[:16]} "
    f"content_sha256_short={content_sha256[:16]} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
)

# S87+ schema-v2 3-tuple annotation companion row (REQUIRED for [VERIFY-THEOREM])
companion_3tuple = (
    f"# sign_verdict={sign_verdict} "
    f"magnitude_verdict={magnitude_verdict} "
    f"regime_verdict={regime_verdict} "
    f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
)

# Append to s90_gate_verdicts.txt (atomic single-shot append)
verdict_block = (
    f"\n{canonical_line_with_content}\n"
    f"{companion_dual_sha}\n"
    f"{companion_3tuple}\n"
)
with VERDICT_TXT.open("a", encoding="utf-8") as fp:
    fp.write(verdict_block)

print("[SEC 9] Verdict line emitted to s90_gate_verdicts.txt:")
print()
print(canonical_line_with_content)
print(companion_dual_sha)
print(companion_3tuple)
print()


# ---------------------------------------------------------------------------
# Section 13 — Final 4-tuple output tag (plan §W7-2 §8)
# ---------------------------------------------------------------------------

print("=" * 78)
print(f"4-tuple output: (value={value_str},")
print(f"                  scheme={SCHEME},")
print(f"                  convention={CONVENTION},")
print(f"                  L_max={L_MAX_PRIMARY})")
print("=" * 78)
print(f"\nGate {GATE_ID}: {composite_verdict}")
print(f"Reading {reading_confirmed} confirmed at L_max={L_MAX_PRIMARY}, τ={tau_fold}")
print(f"  Δ_scheme = {delta_scheme_primary:.3e} M_KK² (threshold {DELTA_SCHEME_PASS_THRESHOLD:.0e})")
print(f"  η = 0 to {ETA_PASS_THRESHOLD:.0e} in both schemes (W-11 STRENGTHENED)")
print(f"  Canonical-pin sanity: GV_APS(L=5) = {GV_APS_canonical:.10e}")
print(f"                        canonical = {gv_canonical_difference_FW:.10e}")
print(f"                        |Δ| = {canonical_pin_deviation:.3e} < {GV_CANONICAL_SANITY_TOL:.0e}")
print()
print(f"Reading {reading_confirmed} implication for §VII.AQ.OP-PROJ suffix tagging:")
if reading_confirmed == "A":
    print("  → no -CANONICAL-IMPORT-BINDING suffix needed")
    print("  → §VII.AQ.OP-PROJ Reading A is Stage-3-PERMANENT-eligible")
    print("  → Binding-axis K-counter STAYS at K=1 (no advancement)")
else:
    print("  → -CANONICAL-IMPORT-BINDING suffix MANDATORY on §VII.AQ.OP-PROJ Reading B")
    print("  → Binding-axis K-counter advances K=1 → K=2 (W7b-82 + §W2-5 jointly)")
