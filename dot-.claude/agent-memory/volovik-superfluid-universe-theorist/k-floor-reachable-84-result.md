---
name: S84 W5-63 K-floor reachable 4-hull
description: W5-63 FAIL with 5/5 OUT. 4-hull=[1.9222,2.1849] all targets {1.0..1.7} below hull_lo=K_R5. K_Ri regulator-invariant, CC3 PASS. Triple-support K-floor-WALL candidate.
type: project
---

S84 W5-63 GATE-K-FLOOR-REACHABLE verdict: **FAIL** (strongest margin).

**Result**: reachable_count = 0/5. outside_count = 5/5. edge_count = 0/5.

**4-hull** (R4 excluded per Gate 61):
- K_R1 = 2.1849 (B3-only) — hull_hi
- K_R2 = 2.0491 (geo-mean)
- K_R3 = 2.0353 (3/3/2-weighted, canonical)
- K_R5 = 1.9222 (B2-only, Bogoliubov-primary) — hull_lo
- hull = [1.9222, 2.1849], width 0.2627

**5-target corridor** T = {1.0, 1.1, 1.3, 1.5, 1.7}. max(T) = 1.7 < hull_lo = 1.9222. ALL targets below lower hull edge. reachable = 0.

**Substitution chain**:
- Step 1: K_Ri from per-band S_IC_Bj = 1 + 2 n_Bj (GGE occupation), hull = [min K_Ri, max K_Ri], reachable = |{k ∈ T: k ∈ hull}|.
- Step 2: From Delta_B2=0.7704, Delta_B1=0.4643, Delta_B3=0.1760, T_B2=0.6680, T_B1=0.435, T_B3=0.178 → K_R1=2.1849, K_R2=2.0491, K_R3=2.0353, K_R5=1.9222.
- Step 3: max(T)=1.7 < 1.9222=hull_lo. All 5 targets OUT.
- Step 4: reachable=0, outside=5 ≥ FAIL threshold 3. Verdict FAIL.

**Cross-checks (all PASS)**:
- CC1: Landau V.1 ledger reproduction (4 decimal agreement).
- CC2: monotonicity (0 flips in in_hull for monotone T).
- CC3: zeta hull = Zubarev hull (identical). K_Ri are GGE-thermal, NOT regulator-dressed. Regulator acts on A_s_base prefactor xi, not on K-convention readout.
- CC4: torch-vs-numpy GPU: machine-exact 0.0e+00 agreement.
- CC5: R4-inclusion counterfactual hull = [1.9222, 15.95]; reachable still 0/5 (hull_lo unchanged).

**W5-54 feed reconciliation**: W5-54 FAIL (K_match(Zubarev)=32.40 vs K_match(zeta)=0.6366, factor 50.9×) is regulator-dressing on A_s_base, NOT on K_Ri. CC3 confirms K-convention layer is regulator-invariant. The S83 G38 WALL at K=0.6366 is zeta-specific; the W5-63 4-hull lower edge 1.9222 is regulator-invariant.

**Structural consequence (K-floor-WALL-JOINT candidate)**: Per plan §7 (L917-L918), W5-63 FAIL + W5-59 floor-under-R5 → **K-FLOOR-WALL-JOINT** promotion:
- W5-54: K_match regulator-shifted (50.9× factor).
- W5-59: A_s_floor(R5) = 1.10e-13 (Branch-B).
- W5-63: 4-hull lower edge at K_R5 = 1.9222, corridor {1.0..1.7} entirely below.

Three independent supports convert the K-floor from a single-convention basin to a structural wall.

**closure_sha = 29af1e682f59c6ec7481ffaf84ca70d3f00a9ad5a8b5365c53e78cadfb66aead**
