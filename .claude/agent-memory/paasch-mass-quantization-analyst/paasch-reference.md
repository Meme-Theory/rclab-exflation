---
name: Paasch Reference
description: Consolidated Paasch numerics, OCR errata, gate registry, and structural verdicts for the Paasch program within NCG. Replaces session-detail / structural-verdicts / verified-numerics / full_analysis.
type: reference
---

# Paasch Reference (Consolidated)

## Canonical Numerics (Paasch derived vs measured)

| Quantity | Paasch | Measured | Rel Dev | Source |
|----------|--------|----------|---------|--------|
| phi_paasch | 1.5315844 | (from x=e^{-x^2}) | exact | 2009 Eq(2g) |
| alpha | 0.007297359 | 0.0072973526 | 8.8e-7 (~0.9 ppm) | 2016 FSC paper |
| m_proton | 1.67262110e-27 kg | 1.67262192e-27 | 4.9e-7 | 2016 calc paper |
| m_neutron | 1.67492745e-27 kg | 1.67492750e-27 | 2.9e-8 | 2016 calc paper |
| fN | 1.236068 = 2/golden = sqrt(5)-1 | (algebraic) | 1.6e-6 | 2016 calc paper |
| sqrt(7/3) | 1.527525 | (D_K round-metric ratio) | — | tau=0 limit |
| phi crossing | tau = 0.1499 (s22a_paasch_curve) | — | — | S22a |
| dump point | tau = 0.190 (B2 minimum) | — | — | S33 |
| inter-sector R at fold | 27.2 | PDG 32.6 | 17% | S36 W2-A |
| BCS gap Delta | 0.025 spectral = 2.5e14 GeV | — | — | S36 |

## Mass Numbers N(j) = (m_j/m_e)^{2/3}

| Particle | N(j) | 7n | M(j)=(m_j/m_e)^{1/3} |
|----------|------|----|-----------------------|
| electron | 7    | 7*1  | 1.913 |
| muon     | 35   | 7*5  | 5.916 |
| pion     | 42   | 7*6  | 6.481 |
| kaon     | 98   | 7*14 | 9.899 |
| proton   | 150  | ~7*21 | 12.247 |

fN applies to M values: M(i+1) = M(i)*fN, so N(i+1) = N(i)*fN^2.
N(p)/N(K) = 150/98 = 1.531 (0.04% from phi_paasch).

## OCR Errata (.md transcriptions garble equations heavily)

- N(j) exponent = **2/3** (not 1/2 as OCR-rendered)
- phi^{3/2} = **1.895438** (not 1.8985 as garbled in 30+ doc locations)
- m_E = sqrt(m_e * m_p) = **21.9 MeV** (NOT half muon; Eq 4.7a gives half-muon separately)
- Paper 04 alpha formula (1/f)^{2*n3} OCR-garbled — only final numerical value reliable
- Cross-check ALL formulas numerically before quoting

## Transcendental Equations

- phi_paasch: x = e^{-x^2}, phi = 1/x = 1.5315844; equivalent ln(phi) = 1/phi^2
- NOT golden ratio: 4*phi_golden^2 = 1.52786 (0.24% gap, different transcendental equation)
- alpha: from ln(x) = -x combined with n3 = 10

## Gate Registry (Paasch within NCG)

| Gate | Verdict | Session | Key Number |
|------|---------|---------|------------|
| PT-count           | CLOSED       | S35 | — |
| PT-ratio           | FAIL         | S35 | s=0.38 vs 2.63 needed |
| alpha-dim (n3=10)  | STRUCTURAL   | S48 | exact SU(3) identity |
| PHI-GOLDEN-22      | FAIL         | S48 | 1.680 vs 1.618 (3.8%) |
| FN-CENTROID-47     | FAIL         | S48 | 1.194 vs 1.236 (3.4%) |
| TRIAL-FACTOR       | INFO         | S48 | P~15% adjusted |
| SIX-SEQUENCE       | UNIFORM      | S48 | chi2 p=0.40 |
| PAASCH-SPIRAL-47   | FAIL         | S47 | Rayleigh p=0.702 |
| PHI-BDG-47         | FAIL         | S47 | max R_dressed=1.465 |
| PAASCH-CC          | CLOSED       | S56 | structurally different exponentials |
| LOG-SIGNED-40      | **OPEN**     | S48 | single-point only; tau sweep needed |
| INV3-W3-2 (W3-kink)| FAIL         | INV3 | M(6,5) c=4/5 integrable kink spectrum is SINGLE-MASS (degenerate doublet, Chim-Zam/Koberle-Swieca via arXiv:0909.2192) -> only ratio 1.000; no phi/fN. phi NOT a c=4/5 universality-class MASS number. |

### INV3-W3-2 detail (W3 minimal model M(6,5) / Z3-Potts kink masses vs phi/fN)
- **Decisive lit**: arXiv:0909.2192 (Lepori-Toth-Delfino) — 3-state Potts critical pt = D4 (c=4/5) = M(6,5); integrable (h=0 thermal) kinks ALL EQUAL MASS (Chim-Zam IJMPA7:5317, Koberle-Swieca PLB86:209). Nontrivial meson/baryon ratios only for h!=0, CONTINUOUS in eta_pm (NON-universal). => only universality-class mass ratio = 1.000.
- **CFT-charge map (verified)**: M(6,5) c=4/5 = ORDINARY 3-state Potts; M(6,7) c=6/7 = TRICRITICAL Potts = E6 theory (arXiv:2311.00654 Eq14: ratios sqrt2, 2cos(pi/12), 2 — none is phi/fN); Ising M(4,3) c=1/2 = E8 (Coldea golden=1.618, different class).
- **Look-elsewhere**: 236 of 1307 scanned algebraic ratios fall within 5% of phi OR fN — the sin(k pi/h)/2cos(k pi/n) family is DENSE near both; systematic scan hits fN to 0.0000% (sin(5pi/10)/sin(3pi/10)) and phi to 0.033% (2cos(2pi/9)). A bare 2% match is weak by construction.
- **TRAP (do NOT count as PASS)**: M(6,5) Kac scaling-DIMENSION ratio Delta(4,5)/Delta(3,1)=1.2375 is 0.12% from fN — but a conformal WEIGHT is not a MASS. S33a's `s33a_w3_kink_masses.py` mixed affine-Toda fundamental masses + Kac dims vs phi only (no fN); this gate separates kink-MASS (PASS-eligible) from dimension-ratio (diagnostic).
- **Consequence**: A3 six-sequence<->Z3-wall map loses its universality-class anchor; phi_paasch stays a bare-(3,0)/(0,0) GEOMETRIC fact only (consistent w/ PHI-BDG-47). Corridor "phi forced by c=4/5 CFT" CLOSED.

## Proven Structural Facts (machine epsilon or algebraic)

- D_K exactly block-diagonal in Peter-Weyl (S22b, 8.4e-15). Inter-sector coupling = 0.
- phi_paasch is INTER-SECTOR ONLY: m_{(3,0)}/m_{(0,0)}. No intra-sector crossings.
- BCS exp(-1/M) categorically destroys phi structure (S27, proven algebraically).
- phi_paasch = bare-spectrum property at tau=0.15. BdG compresses ratio monotonically toward 1.
- N3-DIM-48: n3 = dim(3,0) = #sectors(p+q<=3) = T_4 = 10. Exact SU(3) algebraic identity. **Sole surviving Paasch-NCG bridge.**
- phi_paasch is recursion-invariant (S42): geometric property of K=SU(3), independent of M_KK/G/Lambda.
- Normal ordering B1 < B2 < B3 at ALL tau > 0: structural theorem (S36).
- Casimir potential on Peter-Weyl lattice is POLYNOMIAL, NOT logarithmic (S56).
- Casimir-Josephson V_constrained EXACTLY rank-1 (S52); J_12/J_23 = (v_1/v_3)^2 = 19.5197 tau-independent.

## QRPA at Fold (omega/omega_0)

omega_0 = 1.632 (B1 99.3%); notable: omega_2/omega_0 = 1.226 (0.8% from fN=1.236);
omega_5/omega_0 = 1.988 (~2.0). E_qp(B2)/E_qp(B1) = 1.958 (within 2.1% of 2.0).

## Branch Eigenvalues at Fold (tau=0.190, M_KK units)

| Branch | E_qp | Delta | C_2 |
|--------|------|-------|-----|
| B1     | 1.138 | 0.79 | acoustic dominant |
| B2     | 2.228 | 2.06 | flat singlet |
| B3     | 0.990 | 0.18 | gap induced (Delta=0 isolated) |

T_Gibbs = 0.113; T_acoustic = 0.112 (acoustic metric). M_ATDHFB = 1.695. sigma_ZP = 0.026 tau-units.

## LNH Classification (algebraic core vs scaffolding)

- **LNH-independent (algebraic core)**: phi, spiral, N(j), 7n pattern, golden ratio, fN, ln(x)=-x
- **LNH-dependent (scaffolding)**: exponential model, equilibrium state, derivation paths for m_p / m_n / alpha, G-EM unification
- Kepler analogy: right algebraic structure, wrong cosmological scaffolding. Dirac G ~ 1/t excluded by LLR |G_dot/G| < 7e-13 yr^-1 by ~100x.

## Open Computation (one item)

- **LOG-SIGNED-40 tau sweep**: per-sector eigenvalues at all 5 tau (single-point S_signed(0.19)=+787.773 only). Requires Dirac recomputation across the tau axis.

## Key File Paths (data + collabs)

- Paasch core papers: `researchers/Paasch/02_...md`, `03_...md`, `04_...md`
- Paasch library index: `researchers/Paasch/index.md` (46 papers)
- Dump point computation: `computations/s33w3_paasch_dump_point.py`
- Paasch curve data: `computations/s22a_paasch_curve.npz`
- Spiral computation: `computations/s47_paasch_spiral.py`, `s47_phi_bdg.py`
- Backlog computation: `computations/s48_paasch_backlog.py`
- Casimir-Josephson: `computations/s52_casimir_josephson.py`
- Collabs: `sessions/archive/session-{34,36,40,46}/session-N-paasch-collab.md`,
  `sessions/archive/session-56/session-56-paasch-collab.md`
