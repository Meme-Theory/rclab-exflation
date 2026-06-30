#!/usr/bin/env python3
"""
S84-W8B-91-CONSTRAINT-LAYER-AUDIT
==================================

Gate: S84-W8B-91-CONSTRAINT-LAYER-AUDIT
Plan: sessions/session-plan/session-84-plan-w8b.md §W8b-91
Agent: schwarzschild-penrose-geometer

Method:
  Deterministic per-row primary-tag layer assignment of the 53 §VII-A + §VII-B
  identities from sessions/permanent-results-registry.md (read-only).

  Five-layer taxonomy (plan §9):
    ALGEBRAIC     — equality/inequality of spectral moments a_k, Mellin
                    integrals, propagation exponents p_i, or exact rational
                    identities on Jensen parameter tau.
    TOPOLOGICAL   — pi_n(G), K-theory class, KO-dim, Euler characteristic,
                    mode-count-by-dimension.
    CAUSAL        — Killing vectors, light-cones, sound speed, Mach number,
                    e-folds, horizon formation, conformal boundaries.
    ENERGETIC     — NEC/DEC/SEC, stress-energy, spectral-action gradient /
                    Hessian convexity, Casimir energy, energy-dissipation ratio.
    THERMODYNAMIC — entropy, temperature, free energy, chemical potential,
                    condensate/gap, Josephson E_J/E_C, density-of-states coupling.

  Secondary-class check: a row is JOINT only if a distinct mathematical root
  (not linguistic borrow) forces a second dominant class. If the "secondary"
  meaning is linguistic / downstream-derived, the row remains primary-tag only.

Threshold (ABSOLUTE):
    joint_math_count <= 1    -> PASS
    joint_math_count in {1,2,3}  -> INFO   (with mathematical reason per row)
    joint_math_count >= 4    -> FAIL

SHA-256 pins logged in first 20 lines of stdout per .claude/rules/gate-verdicts.md.
Dual-SHA S84+: audit_sha256 (ordered input-pin map) + content_sha256 (JSON
serialization of classification).

Read-only on source files.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
from pathlib import Path

# Mandatory: import canonical constants (even though this gate does not use
# numerical values; import establishes provenance compliance).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Input file pins (read-only)
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILES = {
    "permanent-results-registry.md":
        REPO_ROOT / "sessions" / "permanent-results-registry.md",
    "canonical_constants.py":
        REPO_ROOT / "computations" / "_shared" / "canonical_constants.py",
    "session-84-plan-w8b.md":
        REPO_ROOT / "sessions" / "session-plan" / "session-84-plan-w8b.md",
    "MEMORY.md":
        REPO_ROOT / ".claude" / "agent-memory" /
        "schwarzschild-penrose-geometer" / "MEMORY.md",
}


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def log_pins():
    print("=" * 72)
    print("S84-W8B-91-CONSTRAINT-LAYER-AUDIT  |  input-SHA pin map")
    print("=" * 72)
    pin_map = {}
    for name, path in INPUT_FILES.items():
        h = file_sha256(path)
        pin_map[name] = h
        print(f"  {name:40s}  {h}")
    print("=" * 72)
    return pin_map


# ---------------------------------------------------------------------------
# Per-row classification map (deterministic; plan §9 substitution chain).
# Primary tag is the dominant operator class. Secondary flag is included only
# if a genuinely distinct mathematical root forces joint assignment.
#
# Schema: (row_id, section, line_in_registry, identity, primary, joint, rationale)
# ---------------------------------------------------------------------------

LAYER_ALG = "ALGEBRAIC"       # (local)
LAYER_TOP = "TOPOLOGICAL"     # (local)
LAYER_CAU = "CAUSAL"          # (local)
LAYER_ENE = "ENERGETIC"       # (local)
LAYER_THE = "THERMODYNAMIC"   # (local)

CLASSIFICATION = [
    # ---- VII-A (29 rows, registry lines 534-562) ----
    (1,  "VII-A", 534, "g_1/g_2 = e^{-2tau}",
     LAYER_ALG, None,
     "Gauge-coupling ratio as exact algebraic function of Jensen tau; spectral-moment equality."),
    (2,  "VII-A", 535, "sin^2(theta_W) = e^{-4tau}/(1+e^{-4tau})",
     LAYER_ALG, None,
     "Algebraic identity in tau; exact closed form."),
    (3,  "VII-A", 536, "phi_paasch = m_{(3,0)}/m_{(0,0)} = 1.531580",
     LAYER_ALG, None,
     "Mass ratio = D_K eigenvalue ratio = spectral-moment identity."),
    (4,  "VII-A", 537, "F/B fiber ratio ~ 0.55 (Weyl's law)",
     LAYER_ALG, None,
     "Spectral-weight ratio from Weyl asymptotics; moment-counting equality."),
    (5,  "VII-A", 538, "b_1/b_2 = 4/9",
     LAYER_ALG, None,
     "Branching ratio from rep-theoretic decomposition; exact rational."),
    (6,  "VII-A", 539, "e/(ac) = 1/dim(spinor) = 1/16",
     LAYER_ALG, None,
     "Trace-factorization identity; algebraic dimension count (spinor dimension)."),
    (7,  "VII-A", 540, "V(gap,gap) = 0 (selection rule ~1e-29)",
     LAYER_ALG, None,
     "Anti-Hermiticity selection rule; matrix-element algebraic vanishing."),
    (8,  "VII-A", 541, "dalpha/alpha = -3.08 * tau_dot",
     LAYER_ALG, None,
     "Derived from g_1/g_2 algebraic identity; linear relation on couplings."),
    (9,  "VII-A", 542, "a_4/a_2 ~ 985:1 at tau=0",
     LAYER_ALG, None,
     "Seeley-DeWitt coefficient ratio; spectral-moment equality."),
    (10, "VII-A", 543, "Torsion/curvature ratio 2/3 -> 4/3",
     LAYER_ALG, None,
     "Exact rational on connection-algebra components; not stress-energy."),
    (11, "VII-A", 544, "Bosonic gap (tau=0) = 4/9",
     LAYER_ALG, None,
     "Spectral gap = D_K eigenvalue; algebraic rational."),
    (12, "VII-A", 545, "Fermionic gap (tau=0) = 5/6",
     LAYER_ALG, None,
     "Spectral gap = D_K eigenvalue; algebraic rational."),
    (13, "VII-A", 546, "Gap ratio (tau=0) = 15/8",
     LAYER_ALG, None,
     "Ratio of spectral gaps; exact rational."),
    (14, "VII-A", 547, "chi(SU(3)) = 0",
     LAYER_TOP, None,
     "Euler characteristic = topological invariant; homotopy/cohomology class."),
    (15, "VII-A", 548, "R_K(0) = 2.000000",
     LAYER_ALG, None,
     "Ricci scalar at tau=0 = a_2 Seeley-DeWitt coefficient; spectral moment. "
     "Secondary 'curvature = energy-channel' is linguistic downstream (EH action "
     "is an a_2 moment)."),
    (16, "VII-A", 549, "u(1) Ricci eigenvalue = 1/4 for ALL tau",
     LAYER_ALG, None,
     "tau-invariant spectral-moment eigenvalue; algebraic constancy."),
    (17, "VII-A", 550, "|C|^2(0)/K(0) = 5/7",
     LAYER_ALG, None,
     "Weyl-squared / Kretschmann ratio; exact spectral-moment rational."),
    (18, "VII-A", 551, "Jensen metric diagonal g_tau = 3*diag(e^{2tau}x3, e^{-2tau}x4, e^{tau})",
     LAYER_ALG, None,
     "Exact metric formula on Jensen family; algebraic parametrization."),
    (19, "VII-A", 552, "V_tree formula",
     LAYER_ALG, None,
     "Tree-level potential = spectral-moment sum; exact algebraic identity."),
    (20, "VII-A", 553, "N_species at Lambda=1.0 = 104",
     LAYER_ALG, None,
     "Mode count from truncated spectrum; algebraic enumeration (not K-theoretic "
     "class — it's a cutoff-dependent sum)."),
    (21, "VII-A", 554, "Spectral gap minimum = 0.8191 at tau=0.20",
     LAYER_ALG, None,
     "Min D_K eigenvalue over Jensen scan; spectral-moment value."),
    (22, "VII-A", 555, "NEC violation at tau=0.778",
     LAYER_ENE, None,
     "Null Energy Condition T_uv k^u k^v >= 0 is by definition ENERGETIC. "
     "Causal implication (focusing theorem) is downstream, not a joint-math root."),
    (23, "VII-A", 556, "a_4_geom(0) = 1970 exactly",
     LAYER_ALG, None,
     "Seeley-DeWitt fourth coefficient; spectral-moment value."),
    (24, "VII-A", 557, "V'''(0) = 1.11e9",
     LAYER_ALG, None,
     "Third derivative of spectral-moment potential; algebraic value."),
    (25, "VII-A", 558, "f(0,0) Pomeranchuk = -4.687",
     LAYER_THE, None,
     "Landau parameter / Pomeranchuk-stability criterion is a many-body "
     "thermodynamic stability statement on the Fermi-liquid free energy."),
    (26, "VII-A", 559, "g*N(0) singlet = 3.24",
     LAYER_THE, None,
     "Coupling times density-of-states at Fermi level; thermodynamic "
     "susceptibility kernel."),
    (27, "VII-A", 560, "DNP crossing tau = 0.285",
     LAYER_THE, None,
     "Dynamic Nuclear Polarization = statistical polarization instability on "
     "the modulus flow; thermodynamic phase-crossing. Causal interpretation "
     "(phase boundary in tau-flow) is downstream, not joint-math."),
    (28, "VII-A", 561, "FR settling time ~232 Gyr",
     LAYER_ENE, None,
     "Friction-relaxation timescale = inverse of energy-dissipation rate; "
     "primary ENERGETIC. Time-dimensional secondary (linguistic-CAUSAL) "
     "is not a distinct mathematical root — energy dissipation sets the scale."),
    (29, "VII-A", 562, "Berry curvature peak B=982.5 at tau=0.10 (quantum metric)",
     LAYER_ALG, None,
     "Fubini-Study quantum metric peak; algebraic curvature scalar on "
     "projective Hilbert space. Note: erratum — NOT Berry."),

    # ---- VII-B (24 rows, registry lines 568-591) ----
    (30, "VII-B", 568, "tau_fold = 0.190",
     LAYER_ALG, None,
     "Van Hove singularity = spectral-structure feature; algebraic stationary "
     "point of dS/dtau. 'Fold' as geometric concept is downstream naming."),
    (31, "VII-B", 569, "S_fold = 250,361",
     LAYER_ALG, None,
     "Spectral-action value at tau=tau_fold; Mellin/moment integral."),
    (32, "VII-B", 570, "dS/dtau (at fold) = +58,673",
     LAYER_ENE, None,
     "Spectral-action gradient on Jensen flow = energy-direction along moduli; "
     "ENERGETIC monotonicity statement."),
    (33, "VII-B", 571, "d^2S/dtau^2 (at fold) = +317,863",
     LAYER_ENE, None,
     "Spectral-action convexity = energy-Hessian positivity on moduli; "
     "ENERGETIC second-derivative statement."),
    (34, "VII-B", 572, "eps_H = 0.02163",
     LAYER_ENE, None,
     "Hubble slow-roll parameter = stress-energy-driven expansion rate; "
     "ENERGETIC by definition (Einstein-Hilbert source)."),
    (35, "VII-B", 573, "c_BLV = 0.485",
     LAYER_CAU, None,
     "Fabric sound speed = defines acoustic causal cone; CAUSAL by definition "
     "(signal speed sets the light-cone analog)."),
    (36, "VII-B", 574, "Mach number = 13.75",
     LAYER_CAU, None,
     "v_transit / c_BLV > 1 = sonic-horizon / acoustic-white-hole criterion; "
     "CAUSAL-structure statement on causal disconnection."),
    (37, "VII-B", 575, "N_e (transit e-folds) = 3.73e-3",
     LAYER_CAU, None,
     "Number of Hubble times = horizon-measure on causal manifold; CAUSAL. "
     "(Energetic secondary via H is downstream, not joint-math.)"),
    (38, "VII-B", 576, "M_KK = 7.429e16 GeV",
     LAYER_ALG, None,
     "Mass scale = D_K eigenvalue magnitude; spectral-moment value."),
    (39, "VII-B", 577, "a_0 = 6440",
     LAYER_ALG, None,
     "Zeroth Seeley-DeWitt coefficient = mode-count-weighted spectral moment; "
     "algebraic (not a topological dimension count — it's a truncated sum)."),
    (40, "VII-B", 578, "a_2(fold) = 2776.17",
     LAYER_ALG, None,
     "Second Seeley-DeWitt coefficient; spectral moment."),
    (41, "VII-B", 579, "a_4(fold) = 1350.72",
     LAYER_ALG, None,
     "Fourth Seeley-DeWitt coefficient; spectral moment."),
    (42, "VII-B", 580, "Delta_B3 = 0.370 M_KK",
     LAYER_THE, None,
     "BCS condensate gap = order parameter of superconducting phase; "
     "THERMODYNAMIC. Causal-horizon interpretation (BCS-freeze sonic horizon) "
     "is a downstream derivation, not the definitional mathematical root."),
    (43, "VII-B", 581, "omega_L1 = 0.138 M_KK",
     LAYER_ALG, None,
     "Leggett mode frequency = eigenvalue of phase-difference oscillator; "
     "algebraic spectral frequency. Thermodynamic existence (condensate "
     "requirement) is downstream."),
    (44, "VII-B", 582, "Q_Leggett = 18.6",
     LAYER_ENE, None,
     "Quality factor = energy stored per cycle / energy dissipated per cycle; "
     "primary ENERGETIC ratio. Frequency component already carried by row 43; "
     "no distinct second mathematical root here."),
    (45, "VII-B", 583, "E_J/E_C = 8.57 (zeta a_4)",
     LAYER_THE, None,
     "Josephson energy / charging energy ratio = phase-coherence regime "
     "indicator; THERMODYNAMIC (condensate energy scales)."),
    (46, "VII-B", 584, "K_DeWitt = 5.0 exact",
     LAYER_ALG, None,
     "Kinetic-term normalization = algebraic spectral-moment coefficient; "
     "tau-independent exact rational."),
    (47, "VII-B", 585, "J_12/J_23 = 19.52",
     LAYER_ALG, None,
     "Josephson anisotropy ratio from S_3 subgroup rep-theoretic structure; "
     "algebraic rational from representation theory."),
    (48, "VII-B", 586, "alpha_crit (Hessian) = 55",
     LAYER_ALG, None,
     "Critical point of S(alpha) = alpha*a_2 + a_4 polynomial; algebraic "
     "critical-point value, not an energy-condition threshold."),
    (49, "VII-B", 587, "|A_coset|^2 = 3/2+(3/2)e^{-4tau}",
     LAYER_ALG, None,
     "Coset-space algebraic function of Jensen tau; exact closed form."),
    (50, "VII-B", 588, "E_Cas(sigma) = sigma^{-1/8} * E_Cas(1)",
     LAYER_ENE, None,
     "Casimir-energy scaling with sigma-modulus; ENERGETIC (vacuum-energy "
     "scaling relation)."),
    (51, "VII-B", 589, "Josephson anisotropy max/min = 11.80",
     LAYER_ALG, None,
     "Exact algebraic ratio from S_3 subset S_4 subgroup branching."),
    (52, "VII-B", 590, "155,984 D_K eigenvalues at L_max=10",
     LAYER_TOP, None,
     "Peter-Weyl dimension-sum count = sum_rho (dim rho)^2 up to L_max; "
     "K-homology / representation-theoretic enumeration at fixed truncation. "
     "Topological in the sense of counting-by-dimension (K_0 = Z valued count)."),
    (53, "VII-B", 591, "32 tessellation cells (CG(24))",
     LAYER_TOP, None,
     "Cell-complex count from compact-group 24-cell tessellation; "
     "combinatorial / topological cell-count."),
]


def run_audit():
    pin_map = log_pins()
    print()
    print(f"Total classification rows: {len(CLASSIFICATION)}")
    assert len(CLASSIFICATION) == 53, \
        f"Row count mismatch: expected 53, got {len(CLASSIFICATION)}"

    # Tally per-layer counts.
    tally = {LAYER_ALG: 0, LAYER_TOP: 0, LAYER_CAU: 0,
             LAYER_ENE: 0, LAYER_THE: 0}
    joint_math_rows = []      # (local)
    joint_linguistic_rows = []  # (local)
    unassignable = []         # (local)

    for row in CLASSIFICATION:
        rid, sec, ln, identity, primary, joint, rationale = row
        tally[primary] = tally.get(primary, 0) + 1
        if joint is not None:
            joint_math_rows.append((rid, identity, primary, joint, rationale))

    # Per-row table printed for audit.
    print()
    print("-" * 72)
    print("PER-ROW CLASSIFICATION (primary-tag, plan §9 deterministic rule)")
    print("-" * 72)
    print(f"{'#':>3} {'Sec':<6} {'Primary':<14} {'Joint':<14} Identity")
    for row in CLASSIFICATION:
        rid, sec, ln, identity, primary, joint, rationale = row
        j = joint if joint is not None else "-"
        print(f"{rid:>3} {sec:<6} {primary:<14} {j:<14} {identity[:56]}")

    # Distribution.
    print()
    print("-" * 72)
    print("LAYER DISTRIBUTION")
    print("-" * 72)
    for k, v in tally.items():
        print(f"  {k:<14}  count = {v:>2}")
    print(f"  {'TOTAL':<14}  count = {sum(tally.values()):>2}")

    # Joint-math count.
    joint_math_count = len(joint_math_rows)   # (local)
    print()
    print("-" * 72)
    print("JOINT-ASSIGNMENT-MATHEMATICAL rows (distinct mathematical roots)")
    print("-" * 72)
    if not joint_math_rows:
        print("  (none — all 53 rows have a unique primary mathematical-operator class)")
    for jr in joint_math_rows:
        print(f"  row {jr[0]}: primary={jr[2]}  joint={jr[3]}  reason: {jr[4]}")

    # Threshold logic (plan §5).
    joint_threshold_info = 3   # (local) INFO upper bound
    pass_threshold = 1         # (local) PASS allows <=1 linguistic-joint row
    if joint_math_count <= pass_threshold:
        verdict = "PASS"       # (local)
    elif joint_math_count <= joint_threshold_info:
        verdict = "INFO"       # (local)
    else:
        verdict = "FAIL"       # (local)

    unique_count = len(CLASSIFICATION) - joint_math_count  # (local)
    total_count = len(CLASSIFICATION)                      # (local)

    # Expected 4-tuple (plan §8).
    value_str = f"{unique_count}/{total_count}"            # (local)
    scheme = "canonical-5-layer-v1"                        # (local)
    convention = "per-row-primary-tag"                     # (local)
    L_max = "N/A"                                          # (local)

    # Content SHA-256: serialize classification deterministically.
    content_obj = {
        "rows": [
            {
                "id": r[0], "section": r[1], "line": r[2],
                "identity": r[3], "primary": r[4],
                "joint": r[5]
            }
            for r in CLASSIFICATION
        ],
        "tally": tally,
        "joint_math_count": joint_math_count,
        "verdict": verdict,
        "scheme": scheme,
        "convention": convention,
    }
    content_json = json.dumps(content_obj, sort_keys=True,
                              separators=(",", ":"), ensure_ascii=True)
    content_sha256 = hashlib.sha256(content_json.encode("ascii")).hexdigest()

    # Audit SHA-256: ordered input-pin map (canonical-constants gate-verdict form).
    pin_items = sorted(pin_map.items())
    pin_string = "|".join(f"{k}:{v}" for k, v in pin_items)
    audit_sha256 = hashlib.sha256(pin_string.encode("ascii")).hexdigest()

    # Closure SHA-256: combine audit + content + verdict line.
    closure_components = f"{audit_sha256}|{content_sha256}|{verdict}|{value_str}|{scheme}|{convention}|{L_max}"
    closure_sha = hashlib.sha256(closure_components.encode("ascii")).hexdigest()

    print()
    print("=" * 72)
    print("VERDICT")
    print("=" * 72)
    print(f"  verdict       : {verdict}")
    print(f"  value         : {value_str}  (unique-primary / total)")
    print(f"  scheme        : {scheme}")
    print(f"  convention    : {convention}")
    print(f"  L_max         : {L_max}")
    print(f"  audit_sha256  : {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")
    print(f"  closure_sha256: {closure_sha}")
    print()
    print(f"4-tuple: (value={value_str}, scheme={scheme}, "
          f"convention={convention}, L_max={L_max})")
    print()

    # Single canonical verdict line.
    verdict_line = (
        f"S84-W8B-91-CONSTRAINT-LAYER-AUDIT: {verdict} -- "
        f"value={value_str} scheme={scheme} convention={convention} "
        f"L_max={L_max} sha256={closure_sha} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256}"
    )
    print("CANONICAL-VERDICT-LINE:")
    print(verdict_line)

    return {
        "verdict": verdict,
        "value_str": value_str,
        "scheme": scheme,
        "convention": convention,
        "L_max": L_max,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "closure_sha256": closure_sha,
        "verdict_line": verdict_line,
        "tally": tally,
        "joint_math_count": joint_math_count,
        "classification": CLASSIFICATION,
    }


if __name__ == "__main__":
    run_audit()
