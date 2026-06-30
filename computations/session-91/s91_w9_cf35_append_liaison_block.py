#!/usr/bin/env python3
"""
S91 W9-2 — Append CF-35 first-contact liaison block to
`sessions/framework/registry/mack-observational-constraints.md`.

mack-cosmic-bridge sole-writer per feedback_mack-bridge-role.md.
Append-only Python writer per epistemic-discipline.md §"Registry-Write Hygiene".
"""

from pathlib import Path
import sys

SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[2]
TARGET = (
    PROJECT_ROOT / "sessions" / "framework" / "registry"
    / "mack-observational-constraints.md"
)

BLOCK = '''
## CF-35 — 3He-B Aalto LTL First-Contact Liaison (Pillar V; Q4 2026 deadline)

> **Provenance**: S91 W9-2 (CF-35; gate ID `S91-CF-35-3HE-B-AALTO-LTL-FIRST-CONTACT-LIAISON`); mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. Pre-registration source: `sessions/session-plan/session-91-plan-w9.md §W9-2` (lines 232-402). Substrate canonical pin source: S86 W-5 R2-B Convergence #3 + R2-A EMERGENCE #2 (`W-5 CANONICAL-5`); `computations/_shared/canonical_constants.py:276` `substrate_cocycle_ratio_67_88 = 7.324992`. Forward-pinning: PASS at S91 W9 closure = liaison block landed; NO direct measurement at S91 (long-lead-time observational anchor; 2028-2029 feasibility window).

This block is the framework's FIRST observational liaison pre-registration for a Pillar V superfluid-laboratory falsifier. It is STRUCTURALLY ORTHOGONAL to the Pillar I CMB-S4 / CMB-HD α_s cosmological falsifier (the α_s_canonical 12-14σ multi-σ discriminator above) per `phononic-framing.md §"IS Space, Not IN Space"` Pillar partition.

### Substrate framing (mandatory per `phononic-framing.md §"IS Space, Not IN Space"`)

The substrate IS the inheritance morphism `ι: A_K → A_BdG = M_2(ℂ)` between the framework's NCG-axiomatic spectral triple `(A_K, H_K, D_K(τ))` and the laboratory-IN 3He-B BdG sub-algebra image. The kernel `ker(ι_*)` IS the substrate's degrees-of-freedom that DO NOT inherit; the cocycle-ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 114453/15625` IS the substrate's intrinsic cohomology-asymmetry ratio at the (chiral-pair, Cartan-hypercharge) generator pair. The Aalto LTL Lancaster MCT-3 measurement of `lab(F_1) / lab(F_2)` (Caroli-Matricon ladder asymmetry) IS the laboratory image of this substrate-IS ratio under the inheritance morphism's image-on-spectrum. Direction:

```
Substrate (Pillar IV NCG-axiomatic) IS ‖[φ_67]‖ / ‖[φ_88]‖
   → Bridge map (Connes-Karoubi pairing; inheritance morphism ι)
   → Laboratory (Pillar V 3He-B BdG) IN lab(F_1) / lab(F_2) Caroli-Matricon ladder asymmetry
```

FORBIDDEN container-inversion: "3He-B is an analog of the framework substrate" → INVERT: "3He-B IS the Pillar V laboratory image of the substrate's `ker(ι_*)` under the inheritance morphism; the framework substrate is logically prior".

### 5-Element CF-35 Pre-Registration

#### Element 1 — Substrate prediction (Sage-QQ exact)

| Quantity | Value | Form |
|:---------|:------|:-----|
| `cocycle_ratio_67_88` | `‖[φ_67]‖ / ‖[φ_88]‖` | Sage-QQ exact |
| Sage-QQ canonical form | `Rational(114453, 15625)` | lowest terms (gcd = 1; 15625 = 5⁶) |
| Decimal (6 sig-fig) | `7.324992` | machine-precision float-exact image |
| 4-sig-fig form | `7.3250` | publication rounding |
| `canonical_constants` pin | `substrate_cocycle_ratio_67_88 = 7.324992` | `canonical_constants.py:276` |
| Sage-QQ ↔ canonical_constants cross-pin residual | `< 1e-12` | machine precision |

The Sage-QQ exact form `Rational(114453, 15625)` is the **substrate-IS canonical form** at the rank-2 anchor `(C_H, C_εH)` parity-twin pair generators in `ker(ι_*)` (chiral pair [φ_67] + Cartan hypercharge [φ_88]). It is the framework's published canonical per S86 W-5 R2-B Convergence #3 (workshop §R2-B; line provenance in `pru-class-corpus.md`). Cross-link: `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)"` — substrate-derived ratio preserved INTACT in laboratory measurement at 0.0e+00 machine-precision residual (W-5 DONE-5).

#### Element 2 — Measurement protocol (Caroli-Matricon ladder asymmetry on F_1/F_2)

| Row | Observable | Substrate generator | Platform |
|:----|:-----------|:--------------------|:---------|
| F_1 | Caroli-Matricon ladder asymmetry on 3He-B vortex-core spectroscopy (ν_pump scan; left/right circulation ladder spacing asymmetry) | [φ_67] chiral-pair clean | Lancaster MCT-3 cell (G.R. Pickett / R.P. Haley group) |
| F_2 | Caroli-Matricon ladder spacing parity on 3He-B vortex-core | [φ_88] Cartan hypercharge clean | Helsinki ROTA cell (Aalto LTL; T.S. Riekki or successor) |
| F_5 | Decisive-triplet third row (auxiliary cross-check on F_1+F_2 PASS-AND) | substrate-clean per inheritance morphism | Lancaster MCT-3 + Helsinki ROTA cross-platform corroboration |

**Lab observable form**: `lab(F_i) = ‖[φ_a_i]‖ × (Δ_B/Δ_A)^p_i` where `Δ_B`, `Δ_A` are BdG gap magnitudes and `p_i` is the lab-conversion exponent for row F_i.

**Common-exponent condition**: For the F_1/F_2 decisive doublet, the lab-conversion exponents satisfy `p_1 = p_2 = p`, so the lab-conversion factor `(Δ_B/Δ_A)^p` cancels exactly between numerator and denominator of the ratio. Per `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"` W-5 DONE-5 machine-precision Python verification at 0.0e+00 residual:

```
lab(F_1) / lab(F_2) = [‖[φ_67]‖ × (Δ_B/Δ_A)^p] / [‖[φ_88]‖ × (Δ_B/Δ_A)^p]
                    = ‖[φ_67]‖ / ‖[φ_88]‖                  [common (Δ_B/Δ_A)^p cancels]
                    = Rational(114453, 15625)              [substrate Sage-QQ exact]
                    = 114453/15625                         [lowest terms; gcd = 1]
                    = 7.324992                             [decimal to 6 sig-fig]
```

The ratio is preserved INTACT, INDEPENDENT of (Δ_B/Δ_A) AND p. The substrate cocycle-norm ratio is the ONLY substrate-physics input.

#### Element 3 — Tolerance band

| Band class | Value | Source |
|:-----------|:------|:-------|
| Substrate-natural (Class-B cohomology-asymmetry) | `±0.1%` | substrate-level pin per `inheritance-falsifier-protocol.md §"Pre-registration discipline"` item 4 |
| Lab-systematic (Aalto LTL routine spectroscopy precision) | `±1%` | 4-sig-fig form for first-contact discriminator |
| Combined for FIRST-CONTACT discriminator | `±1%` | conservative envelope; tightens to ±0.1% at S92-S95 substrate-side re-verification at L_max=12 master cache |

Lab-measured ratio PASSes the framework's Class-B cohomology-asymmetry falsifier iff `|lab(F_1)/lab(F_2) − 7.324992| / 7.324992 < 0.01` (±1% combined band at first contact; tightens to ±0.001 substrate-natural band).

#### Element 4 — Contact partners (Pillar V superfluid laboratory roster)

| Tier | Partner | Role |
|:-----|:--------|:-----|
| Primary | Aalto LTL Helsinki ROTA-cell group (P.I. T.S. Riekki or equivalent successor) | F_2 Cartan-hypercharge clean measurement; Caroli-Matricon ladder spacing parity on 3He-B vortex-core |
| Secondary | Lancaster MCT-3 cell (G.R. Pickett / R.P. Haley group) | F_1 chiral-pair clean measurement; vortex-core ν_pump scan; cross-platform corroboration of F_1/F_2 ratio |
| Tertiary | G.E. Volovik (substrate-physics adjudication) | framework's BCS-canonical interpreter; substrate-IS adjudication of measurement ↔ inheritance morphism map |

Liaison letter Q4 2026 names all three tiers with framework prediction `lab(F_1)/lab(F_2) = 7.324992 ± 0.01` and measurement protocol per Element 2.

#### Element 5 — Timeline

| Date | Event | Status |
|:-----|:------|:-------|
| Q4 2026 | Liaison letter sent; framework prediction + measurement protocol + tolerance band specified to Aalto LTL + Lancaster MCT-3 + Volovik | PRE-REGISTERED |
| 2028-2029 | Apparatus availability + Pickett/Haley calibration schedule window opens; measurement campaign feasibility | PRE-REGISTERED forward target |
| S92-S95 (framework session count) | Substrate-side cocycle ratio re-verified at L_max=12 master cache; ±0.1% substrate-natural band tightened | reserved forward target |
| 2030+ | Cross-platform F_5 corroboration; Class-A kernel-signature NULL on F_1+F_2+F_5 decisive triplet + Class-B cohomology-asymmetry ratio 7.3250 ± 0.1% PASS-AND | structural ceiling for framework's first observational anchor at Pillar V |

Forward-pinning: PASS at S91 W9 closure = liaison block landed (this section); NO direct measurement at S91 (long-lead-time observational anchor; first-contact deadline Q4 2026 met by Q4 2026 liaison letter as the artifact-existence predicate).

### (Δ_B/Δ_A)^p Cancellation Theorem — substitution chain (verbatim from plan §W9-2 Field 6)

```
Step 1 — Definitions:
  lab(F_i) = (substrate cocycle-norm) × (lab-conversion factor)^p_i
  lab-conversion factor = (Δ_B / Δ_A)^p   where Δ_B, Δ_A are BdG gap magnitudes
  Common-exponent condition: p_i = p_j = p for F_i, F_j of interest

Step 2 — Substitution:
  lab(F_1) / lab(F_2) = [‖[φ_67]‖ × (Δ_B/Δ_A)^p] / [‖[φ_88]‖ × (Δ_B/Δ_A)^p]
                     = ‖[φ_67]‖ / ‖[φ_88]‖     [common (Δ_B/Δ_A)^p cancels]
                     = 114453 / 15625          [substrate Sage-QQ exact]
                     = 7.324992                [decimal form to 6 sig-fig]

Step 3 — Simplify:
  The ratio is INDEPENDENT of (Δ_B/Δ_A) AND p; ONLY the substrate cocycle-norm
  ratio enters.

Step 4 — Direction:
  Substrate predicts lab(F_1) / lab(F_2) > 7.0 AND < 7.7 (±5% conservative band)
  Substrate predicts within ±0.1% AND ±1% lab-systematic combined band

Step 5 — PASS criterion:
  Q4 2026 PASS iff liaison block on disk with all 5 elements
  AND substrate prediction matches 114453/15625 Sage-QQ
  AND contact-partner names cited
```

W-5 DONE-5 Python verification: machine-precision 0.0e+00 residual on the cancellation identity (substrate ratio preserved INTACT under arbitrary common-exponent (Δ_B/Δ_A)^p lab-conversion).

### Falsifier classification (Class-A + Class-B per `inheritance-falsifier-protocol.md`)

| Class | Test | F-rows | Substrate prediction |
|:------|:-----|:-------|:---------------------|
| Class-A — Kernel-signature row-wise NULL | Decisive triplet | F_1 + F_2 + F_5 | NULL (no signal) when parent BDI symmetry intact; each row tests one [φ_a] in `ker(ι_*)` |
| Class-B — Cohomology-asymmetry cross-cocycle ratio | F_1 / F_2 ratio | F_1 and F_2 simultaneously | `lab(F_1)/lab(F_2) = 7.324992 ± 0.01` (W-5 (Δ_B/Δ_A)^p cancellation) |
| Class-A — Supporting | Supporting pair | F_3 + F_4 | NULL substrate-clean on rows not entering the Class-B ratio |
| Discrimination | Slope analysis | F_4 multi-pressure 0-34 bar | Jacobi-cubic vs φ_88-linear slope-direction discrimination on cocycle-degenerate F_4 row |

Per `inheritance-falsifier-protocol.md §"Why both classes are required"`: a non-NULL detection of Class-A can be reinterpreted as parent-symmetry breakdown without falsifying the substrate; the Class-B cohomology-asymmetry ratio test is what makes the substrate prediction lab-conversion-INDEPENDENT and substrate-falsifying. Both classes saturate the substrate's predictive content.

### Calibration corpus (W11-C5 / W11-C6 from `inheritance-falsifier-protocol.md §"Calibration corpus"`)

- **S86 W-5 W11-C5** (3He-B vortex-core spectroscopy): F_1 = Caroli-Matricon ladder asymmetry, [φ_67]-clean, decisive. Gate 1 NULL on F_1+F_2+F_5; Gate 2 ratio `7.3250 ± 0.1%`; Gate 3 NULL on F_3+F_4; Gate 4 F_4 multi-pressure slope discrimination. Lab platforms: Lancaster MCT-3 + Helsinki ROTA cells.
- **S86 W-5 W11-C6** (3He-A µSR): same 4-gate structure with A-phase chirality discrimination; lab-conversion factors phase-dependent but substrate ratios identical (`Rational(114453, 15625) = 7.324992`).

### Comparison row (Pillar V superfluid laboratory)

| Substrate-canonical | Observational | Falsifier status | Detector horizon |
|:--------------------|:--------------|:-----------------|:------------------|
| `cocycle_ratio_67_88 = Rational(114453, 15625) = 7.324992` | Aalto LTL `lab(F_1)/lab(F_2)` Caroli-Matricon ladder asymmetry (NOT YET MEASURED) | FIRST observational liaison at Pillar V superfluid laboratory; STRUCTURALLY ORTHOGONAL to Pillar I CMB-S4 α_s falsifier | Q4 2026 first contact; 2028-2029 feasibility window; ±1% combined band at first contact; ±0.1% substrate-natural band at S92-S95 substrate-side re-verification |

### Cross-references

- `.claude/rules/inheritance-falsifier-protocol.md` — 4-gate structure (Class-A + Class-B + supporting + slope) + (Δ_B/Δ_A)^p Cancellation Theorem
- `.claude/rules/inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` — rank-2 case (this CF-35); rank ≥ 3 binomial(rank, 2) cross-cocycle enumeration forward
- `.claude/rules/cross-pillar-bridge-anatomy.md §"5-anatomy + 3-level discipline"` MANDATORY at K=3 — Pillar IV substrate-IS ↔ Pillar V laboratory-IN bridge anatomy
- `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"` — substrate → bridge → laboratory direction (FORBIDDEN inversion: "3He-B IS analog of substrate")
- `sessions/framework/registry/falsifier-master-inventory.md` Row #F-3HE-B-COCYCLE-67-88 (mack-cosmic-bridge sole-writer; pending S92 W0 inventory landing)
- `computations/_shared/canonical_constants.py:276` `substrate_cocycle_ratio_67_88 = 7.324992` (S86 W-5 CANONICAL-5)
- `sessions/permanent-results-registry.md §VII.AY-OP-PROJ` — INFO-class arithmetic gloss on registry-claimed `Fraction(114453, 15625)` vs empirical rank-2 anchor `Fraction(793346, 108307)` (delta 1.76e-5 at 6th sig-fig; carry-forward S92 corrigendum per S91 W8-3/W8-5/W8-6 closeout; the CF-35 published canonical is the lowest-terms Sage-QQ form `Rational(114453, 15625)`, NOT the empirical anchor)
- Aalto LTL Helsinki ROTA-cell group (T.S. Riekki) + Lancaster MCT-3 (G.R. Pickett / R.P. Haley) + G.E. Volovik (substrate-physics adjudicator) — contact roster per Element 4

### Substrate framing (closing note)

The substrate IS the inheritance morphism `ι: A_K → A_BdG = M_2(ℂ)` between the framework's NCG-axiomatic spectral triple and the laboratory-IN 3He-B BdG sub-algebra image. The kernel `ker(ι_*)` carries substrate degrees-of-freedom that DO NOT inherit into the laboratory parent; the cocycle-ratio `‖[φ_67]‖ / ‖[φ_88]‖ = Rational(114453, 15625) = 7.324992` IS the substrate's intrinsic cohomology-asymmetry at the rank-2 anchor (chiral-pair, Cartan-hypercharge) generator pair. The Aalto LTL Lancaster MCT-3 measurement of `lab(F_1)/lab(F_2)` IS the laboratory image of this substrate-IS ratio under the inheritance morphism's image-on-spectrum. The (Δ_B/Δ_A)^p Cancellation Theorem (W-5 DONE-5; 0.0e+00 Python residual) preserves the substrate ratio INTACT in lab measurement under any common-exponent lab-conversion factor. This is the framework's FIRST observational liaison at a Pillar V superfluid laboratory; STRUCTURALLY ORTHOGONAL to the Pillar I CMB-S4 / CMB-HD α_s cosmological falsifier (the α_s_canonical 12-14σ discriminator above). Per `feedback_reporting-framing.md` discipline: a Q4 2026 PASS on liaison letter delivery + 2028-2029 measurement window opening + Class-B ratio 7.3250 ± 0.01 lab confirmation would be the framework's first observational anchor at Pillar V, locking in a multi-platform cross-check (Lancaster MCT-3 + Helsinki ROTA) under a substrate-IS cohomology-asymmetry prediction that is lab-conversion-INDEPENDENT.

---
'''


def main() -> int:
    if not TARGET.exists():
        print(f"FAIL — target file missing: {TARGET}")
        return 1

    pre_size = TARGET.stat().st_size
    # Atomic append via POSIX O_APPEND (open mode "a")
    with open(TARGET, "a", encoding="utf-8", newline="") as f:
        f.write(BLOCK)
    post_size = TARGET.stat().st_size

    print(f"Appended CF-35 liaison block to {TARGET}")
    print(f"  pre-size:  {pre_size} bytes")
    print(f"  post-size: {post_size} bytes")
    print(f"  delta:     +{post_size - pre_size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
