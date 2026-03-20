# Verified Numerics & Erratum Log

## Paasch Derived vs Measured
| Quantity | Paasch | Measured (CODATA 2018) | Rel Dev |
|----------|--------|------------------------|---------|
| phi_paasch | 1.5315844 | (derived, exact) | N/A |
| alpha | 0.007297359 | 0.0072973526 | 8.8e-7 (~0.9 ppm) |
| m_proton | 1.67262110e-27 kg | 1.67262192e-27 | 4.9e-7 |
| m_neutron | 1.67492745e-27 kg | 1.67492750e-27 | 2.9e-8 |
| Wyler alpha | 0.007297353 | 0.0072973526 | 0.6 ppm (comparison) |

## Mass Numbers N(j) = (mj/me)^{2/3}
| Particle | N(j) | 7n | M(j)=(mj/me)^{1/3} |
|----------|------|----|---------------------|
| electron | 7 | 7*1 | 1.913 |
| muon | 35 | 7*5 | 5.916 |
| pion | 42 | 7*6 | 6.481 |
| kaon | 98 | 7*14 | 9.899 |
| proton | 150 | ~7*21 | 12.247 |

fN applies to M values: M(i+1) = M(i)*fN. Then N = M^2. fN = 2*golden = 1.236068 (1.6e-6).

## Round-Metric Algebraic Values (D_K on SU(3))
| Sector | lambda_min^2 | Exact | At tau=0.15 |
|--------|-------------|-------|-------------|
| (0,0) | 0.75 | 3/4 | numerical |
| (3,0) | 1.75 | 7/4 | numerical |
| ratio | 1.527525 | sqrt(7/3) | 1.531580 (0.0005% from phi_paasch) |

## Transcendental Equations
- phi_paasch: x = e^{-x^2}, phi = 1/x = 1.5315844. Equivalent: ln(phi) = 1/phi^2.
- NOT golden ratio: 4*phi_golden^2 = 1.52786 (0.24% gap, different transcendental equation)
- Alpha: from ln(x) = -x, combined with n3=10

## Tau-Dependent Ratio (from s22a_paasch_curve.npz)
| tau | E_{(3,0)}/E_{(0,0)} | dev from phi_paasch |
|-----|---------------------|-------------------|
| 0.10 | 1.537088 | +0.36% |
| 0.15 | ~1.531580 | +0.0005% |
| 0.190 | 1.52276 | -0.576% (P-30phi FAIL) |
| 0.20 | 1.519977 | -0.76% |
| 0.50 | 1.368478 | -10.65% |

## Session 40 BCS Data at Fold (tau=0.190)
| Quantity | Value | Unit |
|----------|-------|------|
| E_qp(B2) | 2.228 | M_KK |
| E_qp(B1) | 1.138 | M_KK |
| E_qp(B3) | 0.990 | M_KK |
| Delta_B2 | 2.06 | M_KK |
| Delta_B1 | 0.79 | M_KK |
| Delta_B3 | 0.18 | M_KK |
| T_Gibbs | 0.113 | M_KK |
| T_acoustic | 0.158 (Rindler), 0.112 (acoustic) | M_KK |
| T_a/T_Gibbs | 0.993 | (acoustic metric) |
| M_ATDHFB | 1.695 | M_KK units |
| sigma_ZP | 0.026 | tau units |
| E_qp(B2)/E_qp(B1) | 1.958 | (~2.0, within 2.1%) |

## QRPA Frequencies at Fold
| Mode | omega | omega/omega_0 | Branch |
|------|-------|---------------|--------|
| 0 | 1.632 | 1.000 | B1 (99.3%) |
| 1 | 1.894 | 1.161 | B3 mixed |
| 2 | 2.001 | 1.226 | B3 mixed |
| 3 | 2.096 | 1.284 | B3 + B1 |
| 4 | 2.856 | 1.750 | B2 intra |
| 5 | 3.245 | 1.988 | B2 collective |
| 6 | 3.323 | 2.036 | B2 intra |
| 7 | 3.448 | 2.113 | B2 intra |

Notable: omega_2/omega_0 = 1.226, 0.8% from fN = 1.236.
Notable: omega_5/omega_0 = 1.988, ~2.0.

## ERRATUM LOG
- phi^{3/2} = 1.895438 (NOT 1.8985 as garbled in 30+ doc locations)
- N(j) exponent = 2/3 (NOT 1/2, OCR error in .md transcriptions)
- m_E = sqrt(me*mp) = 21.9 MeV (NOT half muon). Eq 4.7a gives half-muon separately.
- Paper 04 alpha formula (1/f)^{2*n3} is OCR-garbled. Only final result value reliable.
