---
name: S84 W2-18 Layer Transport Audit Result
description: Kasparov transport T_L2->L3 exists and is finite/monotonic for all 8 G55-MIXED rows; sub-tag centroid prediction FAILS at raw-ratio construction (slot-magnitude dominates pinning-class)
type: project
---

# S84 W2-18 LAYER-TRANSPORT-AUDIT -- INFO

**Gate**: S84-LAYER-TRANSPORT-AUDIT
**Verdict**: INFO -- value=5.000e-1 scheme=Zubarev-L2 convention=CC5 L_max=5
**Closure SHA**: 553bfed1c9a829544ec7eeb650c43f8847b87bfd3b6439f584ab11d40ddee223

**Why**: The W2c-18 hypothesis decomposed as two claims: (1) T_{L2->L3} exists as a finite monotonic map for all MIXED rows; (2) sub-tag centroid clustering (FI-pin [0.8, 1.5], mostly-RD <0.5, promotable >2) predicts sigma_row magnitude. Claim (1) CONFIRMED -- 8/8 finite, 8/8 positive sign, 0 UNDEFINED. Claim (2) FALSIFIED -- 4/8 in band, with 11-14 OOM mismatches for FI-pin and promotable.

**How to apply**: When using this result in future sessions, distinguish the two tracks:
- MIXED bucket is NOT structurally degenerate at the transport level (Kasparov factorization is well-defined).
- The FI-pin / mostly-RD / promotable partition tracks a DIFFERENT structural invariant than raw span_L3 / Delta_L2 ratio. The 13-OOM sigma_row spread across rows is driven by which Mellin slot dominates (f_conv ~ 1e-9, M_0 ~ 1e5, g ~ 1).
- Carry-forward computations to test normalized / log-space / slot-conditional formulations in W3.

## Key numbers

- **L2 anchor**: S_Zubarev = 3805.668 (canonical), S_zeta = 159936 (W1-G1)
- **Uniform Delta_L2** for zeta-pinned rows: 156130.33
- **Span ladder** (slot-dominated, not pinning-dominated):
  - f_conv (rows 4, 27, 38): span ~ 2.9e-9, sigma ~ 1.9e-14 (rows 4, 38) to 3.4e-10 (row 27)
  - g (rows 17, 18, 42): span = 3.085, sigma = 1.98e-5
  - M_0 (rows 13, 33): span = 7.81e+4, sigma = 0.500

## 10 vs 8 row discrepancy

- **G54 atlas** (formal VII.K): 10 rows tagged MIXED-KK-class by classification heuristic, NO per-regulator observable data.
- **G55 sub-tags** (S82 workshop authority): 8 rows with explicit observable + Mellin + sub-tag.
- **2 G54-only rows** (Mach number, alpha_crit Hessian): NO transport data, reported as SUBTAG-UNAVAILABLE extras. Structural observation: VII.K atlas contains entries with insufficient metadata for transport mechanics.

## Files

- Script: `computations/s84_w2c_layer_transport_audit.py`
- Data: `computations/s84_w2c_layer_transport_audit.npz`
- Section text: `computations/s84_w2c_layer_transport_audit.md`
- Verdict: `computations/s84_gate_verdicts.txt` line 21
- Working paper: `sessions/archive/session-84/session-84-w2-workingpaper.md` §W2-18 (line 534+)
