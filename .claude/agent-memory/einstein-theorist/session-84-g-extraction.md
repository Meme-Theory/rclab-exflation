---
name: session-84-g-extraction
description: G extraction from spectral action — OBSTRUCTED by two-layer regulator + M_KK ambiguity; 6.1 OOM scheme spread verified
type: project
---

# G-from-a_2 Feasibility (pre-S84 audit, NIST-BIPM 2026 G)

**Fact:** Framework CANNOT currently predict G from first principles as a single-valued number.

**Why:** Two-layer obstruction:
1. **Regulator f unpinned.** f_2 = ∫f(u) u du is a scalar moment of a regulator that the framework has CHOSEN differently in different sessions (sharp=1, SDW-L2=2/3, Gauss=2.34, f*=214.97). 4+ OOM span in f_2 alone.
2. **M_KK route-dependent.** M_KK_gravity is circular (from G); M_KK_kerner is 0.83 decades away. Need third route.

**Master equation canonical form (form A, s61/s74):**
`1/(16π G_N) = f_2 · a_2 · M_KK² / (24π²)`
Equivalently: `G_N = 3π / (2 f_2 a_2 M_KK²)`

Three active master-equation forms in live scripts (s61/s74 A, s62 C, s42-task) differ by 45× factor. a_2 normalization (zeta vs SDW-density vs Vol-absorbed) not uniform.

**Verified numerical spread** (Kerner M_KK, CCM form A, 2026-04-19 Python check):
- f_2 = 1 (sharp):   G_pred / G_obs = 0.995   (accidental near-match)
- f_2 = 2/3 (SDW):   G_pred / G_obs = 1.493
- f_2 = 2.34 (Gauss):G_pred / G_obs = 0.425
- f_2 = 215 (f*):    G_pred / G_obs = 4.6e-3

Total span across master-eq × scheme × M_KK combos: **6.13 OOM**.

**Key principle (Einstein discipline):** The f_2 = 1 match at G_pred ≈ G_obs is NOT a prediction — it is what happens when we pick one regulator out of four. Without an FI-property principle selecting f, the match is scheme-shopping (Pattern 3', S79).

**How to apply:**
- If user asks for G prediction: report OBSTRUCTED, not a number
- Upstream computation needed: S83 W1-G6 successor — regulator-pinning from FI-property theorem
- Secondary: master-equation reconciliation (bookkeeping only)
- Tertiary: independent third M_KK route
- After all three close, G-EXTRACT gate becomes single-valued and can be run

**Gate pre-registration (contingent):**
- PASS: |log10(G_pred/G_obs)| < 0.02 (4.7% — not the NIST 5.7e-5; truncation + convention dominate)
- INFO: 0.02 to 0.50
- FAIL: > 0.50 (factor 3 miss)
- EVOI today: < 0.01. Do NOT run before W1-G6 closes.

**BCS correction to a_2:** right sign (reduces a_2), subthreshold magnitude (S76).
Truncation at L_max=10 regulates a_2 = Σ mult/λ² which would diverge on d=8 internal.
