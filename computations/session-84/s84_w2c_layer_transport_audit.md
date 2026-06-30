## §VII.M-TRANSPORT — Layer Transport Audit (S84-LAYER-TRANSPORT-AUDIT)

**Gate**: S84-LAYER-TRANSPORT-AUDIT
**Trigger**: [AUDIT]
**Classification**: META (substrate-level Kasparov factorization, NOT GR coordinate transformation)
**Verdict**: INFO -- value=5.000000e-01 scheme=Zubarev-L2 convention=CC5 L_max=5
**Closure SHA-256**: 553bfed1c9a829544ec7eeb650c43f8847b87bfd3b6439f584ab11d40ddee223

### Substrate framing

The transport map T_{L2->L3} is a Kasparov-style factorization of an observable through the substrate-action layer. Direction of explanation is `D_K -> S_L2 -> span_L3 -> observable`. The map is NOT a coordinate transformation on an external spacetime container.

L2 = substrate-action functional `S_L2(reg) = sum_j d_j * w_R(lambda_j)` evaluated on the Jensen-deformed SU(3) flat spectrum at L_max=5, tau_fold=0.19.

L3 = observable spread `span_L3(O) = max_R O(R) - min_R O(R)` across the 5-regulator atlas {zeta, Zubarev, SDW, dim-reg, lattice-BR}.

### Substitution chain (numerical)

1. **L2 anchor (W1-G1)**:
   - `S_zeta = 1.59936e+05`
   - `S_Zubarev = 3.80567e+03` (canonical local minimum)
   - `S_SDW = 3.04975e+05`
   - `S_dim-reg = 1.59936e+05` (= S_zeta; w_R = 1 at the bare substrate-action level)
   - `S_lattice-BR = 1.59936e+05` (= S_zeta; w_R = 1 at the bare substrate-action level)

2. **Delta_L2 for zeta-pinned rows (all 8 G55 rows)**:
   - `Delta_L2 = |S_zeta - S_Zubarev| = |1.59936e+05 - 3.80567e+03| = 1.56130e+05` (uniform)

3. **Per-slot L3 spans (from G34 5-regulator atlas)**:
   - `f_conv`: range [1.6528e-12, 2.9191e-09] -> span = 2.9175e-09
   - `M_0`: range [1.9028e+03, 7.9968e+04] -> span = 7.8065e+04
   - `g`: range [0.8551, 3.9400] -> span = 3.0849
   - `f_2`: range [0.9996, 7.8560] -> span = 6.8563
   - `f_4`: range [0.9966, 30.858] -> span = 29.861

4. **Per-row sigma_row = span_L3 / Delta_L2**:

   | Row | Quantity | Slot^p | span_L3 | Delta_L2 | sigma_row | Sub-tag | In band? |
   |---|---|---|---|---|---|---|---|
   | 4 | A_s | f_conv^1 | 2.918e-09 | 1.5613e+05 | 1.869e-14 | FI-pin [0.8, 1.5] | NO |
   | 13 | r_max | M_0^1 | 7.806e+04 | 1.5613e+05 | 5.000e-01 | mostly-RD <0.5 | YES (boundary) |
   | 17 | w_0 | g^1 | 3.085e+00 | 1.5613e+05 | 1.976e-05 | mostly-RD <0.5 | YES |
   | 18 | Delta w_0 | g^1 | 3.085e+00 | 1.5613e+05 | 1.976e-05 | mostly-RD <0.5 | YES |
   | 27 | mu (FIRAS-Chluba) | f_conv^0.5 | 5.274e-05 | 1.5613e+05 | 3.378e-10 | FI-pin [0.8, 1.5] | NO |
   | 33 | F_amp | M_0^1 | 7.806e+04 | 1.5613e+05 | 5.000e-01 | promotable >2 | NO |
   | 38 | mu_eff Lindblad | f_conv^1 | 2.918e-09 | 1.5613e+05 | 1.869e-14 | mostly-RD <0.5 | YES |
   | 42 | sin^2 theta_W | g^1 | 3.085e+00 | 1.5613e+05 | 1.976e-05 | promotable >2 | NO |

5. **Sign read-off**: All 8 sigma_row values are POSITIVE and FINITE.
   - Positive: 8/8.
   - Negative: 0/8.
   - Undefined (Delta_L2 = 0): 0/8.
   - Sign-monotonicity check: PASS.

6. **CC-5 multiplicative identity** (Cross-check 1, threshold residual < 0.02%):
   - All 8 rows have single Mellin slot decompositions. CC-5 residual = 0.00e+00 EXACT (single-slot rows are trivially exact).
   - Status: PASS.

7. **Sub-tag centroid clustering** (Cross-check 2, factor-1.5 band):
   - FI-pin [0.8, 1.5] band: 0/2 rows in band (rows 4, 27 have sigma ~ 1e-10 to 1e-14).
   - mostly-RD [0, 0.5] band: 4/4 rows in band (sigmas 1.87e-14, 1.98e-5, 1.98e-5, 5.00e-1).
   - promotable >2 band: 0/2 rows in band (rows 33, 42 have sigma ~ 1e-5 and 0.5).
   - Total in band: 4/8.
   - Status: FAIL.

8. **Direction read-off**:
   - sigma_row spans 13 orders of magnitude (1.87e-14 to 5.00e-1) ACROSS the 8 rows.
   - This range is driven by the dominant Mellin slot magnitude (f_conv ~ 10^-9 vs M_0 ~ 10^5 vs g ~ 1) and NOT by the sub-tag pinning class.
   - Mostly-RD partially aligns with prediction (4/4 in band, but mostly because the band includes everything below 0.75; the rows themselves cluster at 13 orders of magnitude apart).
   - FI-pin and promotable predictions FAIL by 11+ orders of magnitude in the wrong direction.

### Verdict logic (pre-registered)

PASS iff: all rows finite + sign(sigma) = +1 + sub-tag clustering matches.
FAIL iff: any UNDEFINED (Delta_L2 = 0) OR sign(sigma) = -1.
INFO iff: finite + +1 sign + cluster mismatch.

Computed:
- sign_pass = True (8/8 positive, 0 undefined)
- cc5_pass = True (residual = 0)
- cluster_pass = False (4/8 in predicted band)

**Verdict**: INFO. The transport map is FINITE and MONOTONIC for all 8 rows -- confirming the existence of T_{L2->L3} as an explicit map. However, the sub-tag centroid prediction fails: sigma_row magnitude is determined by the dominant Mellin slot, not by the FI-pin / mostly-RD / promotable sub-tag.

### What this PASSES and FAILS in solution space

**Passes (structural existence of transport)**:
- The MIXED bucket is structurally non-degenerate: every row admits a finite, monotonic transport map under T_{L2->L3}.
- The Kasparov-style factorization through the substrate-action layer is well-defined.
- No row produces UNDEFINED or anti-correlated transport.

**Fails (sub-tag centroid prediction)**:
- The pre-registered prediction that FI-pin rows cluster at sigma_row ~ 1, mostly-RD at < 0.5, promotable at > 2 does NOT hold for the constructed transport.
- sigma_row is dominated by Mellin slot magnitude (f_conv-rows are 11-14 OOM smaller than M_0-rows), not by pinning class.
- This suggests EITHER (a) the centroid prediction was based on a different operationalization of "transport rate" (perhaps a normalized or log-rescaled version), OR (b) the sub-tag partition tracks a DIFFERENT structural invariant than the raw span/action ratio.

### Carry-forward computations

1. **W3-MIXED-NORMALIZED-TRANSPORT**: Recompute sigma_row with span_L3 normalized to the canonical observable value (sigma_normalized = span_L3 / |O(zeta)| / Delta_L2 / |S_canonical|). Test whether the centroid prediction reappears under this normalization.

2. **W3-MIXED-LOG-TRANSPORT**: Recompute sigma_row in log space (sigma_log = log(span_L3) - log(Delta_L2)). The 13-OOM range collapses to additive shifts; the sub-tag centroid prediction may apply to log-shifts rather than ratios.

3. **W3-MIXED-SLOT-CONTROLLED**: Test whether sub-tag centroid prediction applies WITHIN-slot rather than ACROSS-slot. Rows 13 and 33 (both M_0^1) have identical sigma = 0.500 yet are tagged mostly-RD vs promotable -- the sub-tag does not predict per-slot variation.

4. **W3-MIXED-RECONSTRUCT-FROM-OBSERVABLES**: Use the actual W2-2 r_max value (1.33e+4), W2-7 w_0 value (-0.9173), etc. directly per row rather than the CC-5 reconstructed observable. Some rows may have additional pre-factors that cancel into the centroid prediction.

### Files

- Script: `computations/session-84/s84_w2c_layer_transport_audit.py`
- Data: `computations/session-84/s84_w2c_layer_transport_audit.npz`
- Verdict: `computations/session-84/s84_gate_verdicts.txt` (line 21)

### Notes on the 10 vs 8 row anchor

The plan §W2c-18 references "10 MIXED rows from the 42-row §VII.K atlas" with the S83-G61 sub-tag partition (8/8 valid). These two row-counts derive from different sources:

- **G54 atlas** (formal §VII.K listing): 10 rows tagged "MIXED-KK-class" by classification heuristic, but stored only as identity strings + sub-section labels (no per-regulator observable values, no Mellin decomposition).
- **G55 sub-tag partition** (S82 workshop authority): 8 rows from S82 §VII.K-META working set, with explicit observable values, Mellin ingredients, and the FI-pin / mostly-RD / promotable assignment.

The 8 G55 rows are the OPERATIONALLY USABLE set for transport computation. The 2 G54-only rows (Mach number, alpha_crit Hessian) are structural classification entries with no per-regulator observable data; they are reported in the data file as `extras_*` fields with `subtag = SUBTAG-UNAVAILABLE` and excluded from the centroid clustering test. The transport audit covers 8/10 of the G54-MIXED rows; the 2 G54-only rows constitute a separate observation that the §VII.K classification atlas contains entries lacking the metadata needed for transport mechanics, which is itself a structural finding for the §VII.K-META completeness audit.
