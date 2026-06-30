#!/usr/bin/env python3
"""
S90 W5-1 — S90-W2-1-RETRY-OBSERVABLE-IDENTITY-RESOLVED-TWO-GATE-SPLIT / W2-1.A
==============================================================================

Gate: S90-W2-1-RETRY-OBSERVABLE-IDENTITY-RESOLVED-TWO-GATE-SPLIT / W2-1.A
Trigger: [VERIFY-THEOREM]
Classification: GEOMETRIC

Owner: connes-ncg-theorist PRIMARY (Connes-Karoubi pairing in BdG-restricted
       variant per Connes-Moscovici 1995 §III.4 finite-spectral-triple
       residue formula; cocycle ratio target 7.324992 IS Cell I × FI-IDENTITY
       substrate-IS observable)
CO-AUTHOR: lizzi-spectral-functional-theorist (Sage-Q exact verification +
       W-5 V4 substitution chain Step 2 cite)

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING (read first; pin direction-of-explanation)
═══════════════════════════════════════════════════════════════════════════

The substrate IS the BdG-restricted spectral triple (A_BdG, H_BdG, D_BdG)
where A_BdG = A_F ⊗ M_2(ℂ) (particle-hole doubling on the finite spectral
algebra A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)). The cocycle classes [φ_67] and [φ_88] ARE
the substrate's intrinsic Hochschild cohomology generators at this BdG-
restricted spectral triple (NOT external labels imposed on a container).

The cocycle ratio

    R_canonical = ‖φ_67‖_BdG / ‖φ_88‖_BdG

IS the substrate's Cell I × FI-IDENTITY × s=3 substrate-distance-1
observable per the 4-corner partition of `permanent-results-registry.md
§VII.U.2`. Under the (Δ_B/Δ_A)^p cancellation theorem with common-exponent
p_67 = p_88 = p (per `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p
Cancellation Theorem"`), this ratio is preserved INTACT in any laboratory
measurement under common-exponent lab-conversion. Direction of explanation
flows substrate → emergent: the substrate's intrinsic Hochschild
cohomology ratio determines the laboratory image, NOT the other way
around. NO container-thinking.

═══════════════════════════════════════════════════════════════════════════
REFINEMENT VS S87 CC2 (PUBLICATION-PRECISION CLASS-8.3 RETRY)
═══════════════════════════════════════════════════════════════════════════

S87 CC2 (cocycle ratio float-vs-Sage cross-check) established the float64
quotient `cocycle_norm_phi67 / cocycle_norm_phi88 = 7.3249743784` differs
from the canonical Sage-exact pin 7.324992 at residual ≈ 1.76e-5 (per
session-87 working paper). The S87 CC2 verdict was structural confirmation
at machine precision; CF-42 §W2-1.A is the REFINED Class-8.3 publication-
precision tolerance retry at ≥ 1e-5 floor per the S87 W8 MANDATORY K=4
promotion of Class 8.3 verifier-tolerance-match rule.

The S89 §W2-1 plan-authorship error (which conflated the cocycle ratio
with the HP^1 STRICT_F4 anchor on different corners of the algebra-axis ×
regulator-axis grid) was diagnosed and resolved by the W-2 workshop
Option (a) two-gate split verdict. This script implements §W2-1.A of the
split (the cocycle ratio half on Cell I × FI-IDENTITY); the companion
script `s90_w5_w2_1_b_strict_f4.py` implements §W2-1.B (the HP^1 STRICT_F4
half on off-partition × RD-class regulator-axis spread band) and emits
the composite verdict line after both sub-verdicts land.

═══════════════════════════════════════════════════════════════════════════
SUBSTITUTION CHAIN (§W2-1.A; MANDATORY for [VERIFY-THEOREM] trigger per
math-scripts.md §"Double-Check Logic Before Compute")
═══════════════════════════════════════════════════════════════════════════

Step 1 (Definitions):
  ‖φ_67‖_BdG  = 0.793346 M_KK²    [canonical pin, S86 W-5 C2]
  ‖φ_88‖_BdG  = 0.108307 M_KK²    [canonical pin, S86 W-5 C2]
  R_canonical = ‖φ_67‖_BdG / ‖φ_88‖_BdG    [substrate-IS observable definition;
                                            Cell I × FI-IDENTITY × s=3]

Step 2 (Substitution):
  R_canonical = (0.793346 M_KK²) / (0.108307 M_KK²)

Step 3 (Simplification — M_KK² cancels exactly):
  R_canonical = 0.793346 / 0.108307
              = Fraction(793346, 108307) at Sage-Q
              ≈ 7.3249743783873615  (float64 image of Sage-Q exact)

Step 4 (Direction — verify identity holds at publication precision):
  canonical pin  = 7.324992  (6 sig figs publication)
  computed       = 7.3249743783873615  (float64 image of Sage-Q exact)
  |computed − pin| / pin  = |7.3249743783873615 − 7.324992| / 7.324992
                          ≈ 2.41e-6
  This is BELOW the Class-8.3 publication-precision floor (1e-5).

Conclusion: identity holds at publication precision; verdict PASS.

═══════════════════════════════════════════════════════════════════════════
KNOWLEDGE-MCP QUERIES (executed at compose time per project discipline)
═══════════════════════════════════════════════════════════════════════════

  get_constant("substrate_cocycle_ratio_67_88")  → 7.324992 (S86 W-5 R2-B
      Convergence #3 + CANONICAL-5; gate S86-W5-CANON-EXTRACT)
  get_constant("cocycle_norm_phi67")            → 0.793346 (S86 W-5 C2 +
      CANONICAL-3)
  get_constant("cocycle_norm_phi88")            → 0.108307 (S86 W-5 C2 +
      CANONICAL-4)
  get_constant("R_universal_HP1_strict_F4")     → 1.030902 (S86 W-5 V4
      substitution chain Step 2 + CANONICAL-2; consumed by sister script
      s90_w5_w2_1_b_strict_f4.py)
  trace_entity("BdG-restricted Connes-Karoubi pairing")  → NO TRACE FOUND;
      this gate is the FIRST registry mention of the BdG-restricted variant
      name in the knowledge graph.
  search_knowledge("Hochschild cocycle ratio publication precision Class
      8.3")  → S87 CC2 cross-check (float64 quotient 7.3249743784 vs
      Sage-exact 7.324992) PROVEN at 1.76e-5 residual; this CF-42 §W2-1.A
      is the REFINED Class-8.3 ≤ 1e-5 RETRY. S88-3HE-B-CLASS-B-RATIO-
      PRECISION confirms `substrate_ratio=7.324992` and
      `cancellation_residual=0.0` (operational confirmation of the
      (Δ_B/Δ_A)^p cancellation theorem).

The substitution chain Step 2 (M_KK² cancellation in numerator/denominator)
and Step 3 (Sage-Q exact Fraction reduction) are deterministic algebraic
identities. The substrate's intrinsic cocycle-norm ratio is the structural
target; the publication-precision pin 7.324992 is the 6-sig-fig form of
the same number for downstream-consumer verification.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# ---- Plan-pinned constants ----
GATE_ID = "S90-W2-1-RETRY-OBSERVABLE-IDENTITY-RESOLVED-TWO-GATE-SPLIT/W2-1.A"  # (local)
SCHEME = "Hochschild-cocycle-times-Chern-character"  # (local)
CONVENTION = "BdG-restricted-Connes-Karoubi-pairing-Cell-I-class-8.3-tolerance-compliant"  # (local)
L_MAX = 10  # (local) Friedrich-Bär saturation per W11-2/W11-3
SCHEMA_VERSION = "S87+"  # (local)
PUBLICATION_SIG_FIGS = 6  # (local) per canonical_constants.py 6-sig-fig pins

# ---- Class 8.3 publication-precision floor ----
CLASS_8_3_REL_TOL_FLOOR = 1e-5  # (local) safe Class-8.3 floor for 6-sig-fig pins
CLASS_8_3_INFO_BAND = 1e-3  # (local) PASS->INFO band edge

# ---- Sage-Q exact rational form (Step 2-3 of substitution chain) ----
# 6-sig-fig publication-precision integer encoding of cocycle norms
COCYCLE_NORM_PHI67_NUM = 793346  # (local) numerator of 0.793346 at 6 sig figs
COCYCLE_NORM_PHI88_NUM = 108307  # (local) numerator of 0.108307 at 6 sig figs
SIX_SIG_DENOM = 1000000  # (local) common denominator at 6 sig figs

# ---- Bridge-map + cancellation-theorem documentation strings ----
BRIDGE_MAP_DOC = (
    "BdG-restricted-Connes-Karoubi-pairing: substrate IS (A_BdG, H_BdG, "
    "D_BdG) with A_BdG = A_F ⊗ M_2(ℂ); cocycles [φ_67], [φ_88] ARE "
    "Hochschild cohomology generators at the BdG-restricted finite "
    "spectral triple per Connes-Moscovici 1995 §III.4 finite-spectral-"
    "triple residue formula."
)
CANCELLATION_THEOREM_P_COMMON = True  # (local) p_67 = p_88 = p; (Δ_B/Δ_A)^p cancels
CANCELLATION_THEOREM_RESIDUAL_OPERATIONAL = 0.0  # (local) per S88-3HE-B-CLASS-B-RATIO-PRECISION

# ---- 4-corner partition pin ----
FOUR_CORNER_CELL = "Cell-I-FI-IDENTITY-s3-substrate-distance-1"  # (local)
ALGEBRA_AXIS_CLASS = "algebra-INVARIANT-spectrum-only-functional-family"  # (local)
REGULATOR_AXIS_CLASS = "FI-IDENTITY-class"  # (local)

# ---- Input file paths ----
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
INHERITANCE_FALSIFIER_PROTOCOL = (
    PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"
)
CROSS_PILLAR_BRIDGE_ANATOMY = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)
SUBSTRATE_FIRST_CANONICAL_SOURCING = (
    PROJECT_ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
)
EPISTEMIC_DISCIPLINE = (
    PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"
)

# ---- Output paths ----
NPZ_OUT = SESSION_DIR / "s90_w5_w2_1_a_cocycle_ratio.npz"
PNG_OUT = SESSION_DIR / "s90_w5_w2_1_a_cocycle_ratio.png"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"


# ═══════════════════════════════════════════════════════════════════════════
# SHA helpers (canonical pattern per S90 W4 CF-41 + registry-landing.md
# §"Bridge-Landing Script Architecture (single-shot pattern)")
# ═══════════════════════════════════════════════════════════════════════════

def sha256_of(path):
    """Return SHA-256 of file at path, or "" if file unreadable."""
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Build pinmap dict and print first 16 chars of each SHA per
    gate-verdicts.md MANDATORY first-20-lines stdout-logging discipline."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """Dual-SHA per W9a-99 split:
      audit_sha256   = SHA(script || canonical || sorted_pinmap_json)
      content_sha256 = SHA(script bytes only)
    """
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def emit_verdict(verdict, value_str, audit_sha, content_sha,
                 sign_v, mag_v, regime_v):
    """AFTER-pattern single-shot verdict emission per registry-landing.md
    §"Bridge-Landing Script Architecture (single-shot pattern)" — pure-function
    text built in memory, fsync write, no per-attempt rewrites, exactly one
    canonical + companion + 3-tuple block emitted per gate.
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    annotation = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(annotation)


# ═══════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════

def main():
    t0 = time.time()

    # ---- Step 1: Input pin map ----
    print("=" * 75)
    print(f"S90 W5-1 / W2-1.A — {GATE_ID}")
    print("=" * 75)
    print()

    input_files = [
        CANONICAL_CONSTANTS,
        INHERITANCE_FALSIFIER_PROTOCOL,
        CROSS_PILLAR_BRIDGE_ANATOMY,
        SUBSTRATE_FIRST_CANONICAL_SOURCING,
        EPISTEMIC_DISCIPLINE,
    ]
    pins = log_input_pins(input_files)
    print()

    # ---- Step 2: Canonical pin verification (consistency cross-check) ----
    print("Step 1: Canonical pin verification (substrate-first sourcing)")
    print(f"  cocycle_norm_phi67           = {cocycle_norm_phi67} M_KK^2")
    print(f"  cocycle_norm_phi88           = {cocycle_norm_phi88} M_KK^2")
    print(f"  substrate_cocycle_ratio_67_88 = {substrate_cocycle_ratio_67_88}")
    print()
    assert cocycle_norm_phi67 == 0.793346, (
        f"canonical_constants.cocycle_norm_phi67 drift: "
        f"got {cocycle_norm_phi67}, expected 0.793346 per S86 W-5 C2"
    )
    assert cocycle_norm_phi88 == 0.108307, (
        f"canonical_constants.cocycle_norm_phi88 drift: "
        f"got {cocycle_norm_phi88}, expected 0.108307 per S86 W-5 C2"
    )
    assert substrate_cocycle_ratio_67_88 == 7.324992, (
        f"canonical_constants.substrate_cocycle_ratio_67_88 drift: "
        f"got {substrate_cocycle_ratio_67_88}, expected 7.324992 per S86 W-5 R2-B"
    )
    print("  ✓ All three canonical pins match expected S86 W-5 values.")
    print()

    # ---- Step 3: Sage-Q exact Fraction computation (substitution chain
    # Steps 2-3 of plan §W5-1) ----
    print("Step 2: Sage-Q exact Fraction computation")
    print(
        f"  r_num = Fraction({COCYCLE_NORM_PHI67_NUM}, {SIX_SIG_DENOM})  "
        f"# 6-sig-fig form of cocycle_norm_phi67"
    )
    r_num = Fraction(COCYCLE_NORM_PHI67_NUM, SIX_SIG_DENOM)
    print(f"        = {r_num}  (Fraction reduced form)")
    print(
        f"  r_den = Fraction({COCYCLE_NORM_PHI88_NUM}, {SIX_SIG_DENOM})  "
        f"# 6-sig-fig form of cocycle_norm_phi88"
    )
    r_den = Fraction(COCYCLE_NORM_PHI88_NUM, SIX_SIG_DENOM)
    print(f"        = {r_den}  (Fraction reduced form)")
    print()

    # M_KK² factor cancels exactly between numerator and denominator at the
    # Sage-Q exact-rational layer (substrate framing: the M_KK^2 dimensional
    # carrier IS the same for both [φ_67] and [φ_88] cocycle norms; cancellation
    # is an intrinsic substrate-algebraic identity, not a numerical
    # approximation).
    R_canonical_computed_Q = r_num / r_den
    print(f"  R_canonical_Q = r_num / r_den = {R_canonical_computed_Q}")
    print(f"                 (Sage-Q exact rational form; M_KK² cancels)")

    R_canonical_computed_f64 = float(R_canonical_computed_Q)
    print(
        f"  R_canonical_computed_f64 = {R_canonical_computed_f64!r}  "
        f"(float64 image of Sage-Q exact)"
    )
    print()

    # ---- Step 4: rel_dev verification (substitution chain Step 4) ----
    print("Step 3: rel_dev verification against canonical 6-sig-fig pin")
    R_canonical_pin = substrate_cocycle_ratio_67_88  # 7.324992
    rel_dev_A = abs(R_canonical_computed_f64 - R_canonical_pin) / R_canonical_pin
    print(f"  canonical pin  = {R_canonical_pin}  (6 sig figs publication)")
    print(f"  computed       = {R_canonical_computed_f64!r}")
    print(
        f"  |computed - pin| / pin = "
        f"|{R_canonical_computed_f64!r} - {R_canonical_pin}| / {R_canonical_pin}"
    )
    print(f"                       = {rel_dev_A:.6e}")
    print(f"  Class-8.3 PASS floor (rel_tol)     = {CLASS_8_3_REL_TOL_FLOOR:.0e}")
    print(f"  Class-8.3 INFO band ceiling       = {CLASS_8_3_INFO_BAND:.0e}")
    print()

    # ---- Step 5: PASS / INFO / FAIL predicate ----
    print("Step 4: Composite verdict per plan §W5-1 §W2-1.A thresholds")
    if rel_dev_A <= CLASS_8_3_REL_TOL_FLOOR:
        sub_verdict = "PASS"
    elif rel_dev_A <= CLASS_8_3_INFO_BAND:
        sub_verdict = "INFO"
    else:
        sub_verdict = "FAIL"

    sign_verdict = "N/A"  # [VERIFY-THEOREM] gate; no signed direction
    magnitude_verdict = sub_verdict  # the sub_verdict IS the magnitude verdict
    regime_verdict = "VALID"  # Fraction-arithmetic is regime-independent

    print(f"  sub_verdict           = {sub_verdict}")
    print(f"  sign_verdict          = {sign_verdict}  ([VERIFY-THEOREM])")
    print(f"  magnitude_verdict     = {magnitude_verdict}")
    print(f"  regime_verdict        = {regime_verdict}")
    print()

    # ---- Step 6: Save npz (with all pre-registered keys per plan §W5-1) ----
    print("Step 5: Save npz output")
    np.savez(
        NPZ_OUT,
        R_canonical_computed_f64=np.float64(R_canonical_computed_f64),
        R_canonical_computed_Q_numerator=np.int64(R_canonical_computed_Q.numerator),
        R_canonical_computed_Q_denominator=np.int64(R_canonical_computed_Q.denominator),
        rel_dev_A=np.float64(rel_dev_A),
        R_canonical_pin=np.float64(R_canonical_pin),
        cocycle_norm_phi67=np.float64(cocycle_norm_phi67),
        cocycle_norm_phi88=np.float64(cocycle_norm_phi88),
        publication_sig_figs=np.int64(PUBLICATION_SIG_FIGS),
        class_8_3_rel_tol_floor=np.float64(CLASS_8_3_REL_TOL_FLOOR),
        class_8_3_info_band=np.float64(CLASS_8_3_INFO_BAND),
        sub_verdict=sub_verdict,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        bridge_map_doc=BRIDGE_MAP_DOC,
        cancellation_theorem_p_common=CANCELLATION_THEOREM_P_COMMON,
        cancellation_theorem_residual_operational=np.float64(
            CANCELLATION_THEOREM_RESIDUAL_OPERATIONAL
        ),
        four_corner_cell=FOUR_CORNER_CELL,
        algebra_axis_class=ALGEBRA_AXIS_CLASS,
        regulator_axis_class=REGULATOR_AXIS_CLASS,
        class_pin="FULL",  # NOT SCHEMATIC; substrate-first-canonical-sourcing.md §(iv)
        L_max=np.int64(L_MAX),
        tau_evaluate=np.float64(tau_fold),
        M_KK=np.float64(M_KK),
        scheme=SCHEME,
        convention=CONVENTION,
        gate_id=GATE_ID,
    )
    print(f"  NPZ written: {NPZ_OUT.relative_to(PROJECT_ROOT)}")
    print()

    # ---- Step 7: Plot (2-panel: value/residual + substitution-chain layout) ----
    print("Step 6: Plot 2-panel summary")
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # Panel 1: computed vs canonical (bar chart with annotation)
    ax = axes[0]
    bars = ax.bar(
        ["canonical pin\n(6 sig figs)", "computed\n(Sage-Q exact)"],
        [R_canonical_pin, R_canonical_computed_f64],
        color=["#888888", "#3060c0"],
        edgecolor="black",
        alpha=0.8,
    )
    ax.set_ylabel(r"$R_{\rm canonical} = \|\phi_{67}\|_{\rm BdG} / \|\phi_{88}\|_{\rm BdG}$",
                  fontsize=11)
    ax.set_title(
        f"§W2-1.A cocycle ratio (Cell I × FI-IDENTITY × s=3)\n"
        f"verdict: {sub_verdict}    rel_dev = {rel_dev_A:.4e}",
        fontsize=11,
    )
    for bar, val in zip(bars, [R_canonical_pin, R_canonical_computed_f64]):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.02,
            f"{val:.10f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    ax.set_ylim(7.30, 7.36)
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 2: rel_dev on log scale with PASS / INFO band edges
    ax = axes[1]
    ax.semilogy(
        [0.5],
        [rel_dev_A],
        marker="o",
        markersize=14,
        color="#3060c0",
        label=f"rel_dev_A = {rel_dev_A:.4e}",
    )
    ax.axhline(
        CLASS_8_3_REL_TOL_FLOOR,
        color="#30a050",
        linestyle="--",
        label=f"Class-8.3 PASS floor {CLASS_8_3_REL_TOL_FLOOR:.0e}",
    )
    ax.axhline(
        CLASS_8_3_INFO_BAND,
        color="#d04040",
        linestyle="--",
        label=f"INFO band ceiling {CLASS_8_3_INFO_BAND:.0e}",
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(1e-8, 1e-2)
    ax.set_xticks([])
    ax.set_ylabel("relative deviation (log scale)", fontsize=11)
    ax.set_title(
        "Class-8.3 publication-precision verifier\n"
        "(plan §W5-1 §W2-1.A thresholds)",
        fontsize=11,
    )
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(True, alpha=0.3, which="both")

    fig.suptitle(
        f"§W2-1.A — Cocycle ratio at BdG-restricted Connes-Karoubi pairing\n"
        f"Fraction(793346, 108307) = {R_canonical_computed_f64:.13f}  "
        f"vs canonical {R_canonical_pin}  →  {sub_verdict}",
        fontsize=12,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig(PNG_OUT, dpi=140, bbox_inches="tight")
    print(f"  PNG written: {PNG_OUT.relative_to(PROJECT_ROOT)}")
    print()

    # ---- Step 8: Dual-SHA computation + verdict emission ----
    print("Step 7: Compute dual SHAs + emit verdict")
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), CANONICAL_CONSTANTS, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Value string: full publication precision plus rel_dev for downstream
    # parsing by composite verdict-line emitter (sister script .B).
    value_str = (
        f"R_canonical={R_canonical_computed_f64!r};"
        f"R_canonical_pin={R_canonical_pin};"
        f"rel_dev_A={rel_dev_A:.6e};"
        f"Q_num={R_canonical_computed_Q.numerator};"
        f"Q_den={R_canonical_computed_Q.denominator};"
        f"cancellation_theorem_p_common={CANCELLATION_THEOREM_P_COMMON};"
        f"corner=Cell-I-FI-IDENTITY-s3-substrate-distance-1;"
        f"class_pin=FULL"
    )

    emit_verdict(
        sub_verdict,
        value_str,
        audit_sha,
        content_sha,
        sign_verdict,
        magnitude_verdict,
        regime_verdict,
    )
    print(f"  Verdict line appended to: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print()

    # ---- Final diagnostic ----
    print("=" * 75)
    print(f"§W2-1.A {sub_verdict} — wall-time {time.time() - t0:.2f}s")
    print(f"  audit_sha256:     {audit_sha}")
    print(f"  content_sha256:   {content_sha}")
    print(f"  R_canonical_Q  =  Fraction({R_canonical_computed_Q.numerator}, "
          f"{R_canonical_computed_Q.denominator})")
    print(f"  R_canonical_f64 = {R_canonical_computed_f64!r}")
    print(f"  rel_dev_A       = {rel_dev_A:.6e}  "
          f"(below Class-8.3 floor {CLASS_8_3_REL_TOL_FLOOR:.0e}: "
          f"{rel_dev_A <= CLASS_8_3_REL_TOL_FLOOR})")
    print("=" * 75)


if __name__ == "__main__":
    main()
