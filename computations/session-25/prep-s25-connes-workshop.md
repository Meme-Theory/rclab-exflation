---
gate: S25-CONNES-WORKSHOP
script_original: computations/session-25/s25_connes_workshop.py
script_t3: computations/_shared/t3-intake/s25_connes_workshop.py
session_origin: S25
tier: 3
classification: INFO (diagnostic harvest; 7 NCG items, no pre-registered threshold)
---

# Prep block — S25-CONNES-WORKSHOP

## 1. Locate + migrate

Original script was NOT in `computations/_shared/` (only archive `.npz`
side-cars were). Located at `computations/session-25/s25_connes_workshop.py`
(453 lines, 17,293 bytes). All three input archives are also in
`computations/_shared/` — script was written with `BASE =
"C:/sandbox/.../computations"` pre-S51 archiving; paths rebased
to `computations/_shared` in rerun copy.

## 2. Knowledge MCP pre-checks

- `trace_entity("connes_workshop")`: returns the provenance record
  (s25 / connes_workshop), two theorems (J_BdG^2 = +1, J_BdG gamma = -gamma J_BdG),
  and 10 equation fragments identifying the major numpy statements in
  the script (sectors collection, a_2, a_4, derivatives, R^2 dominance).
- `search_knowledge("S25 Connes workshop")`: 4 provenance hits
  (connes_workshop, einstein_results, connes_results, kk_workshop)
  and 16 equation hits all traceable to this script. No pre-registered
  PASS/FAIL threshold found — this is a diagnostic harvest.

## 3. Canonical constants

Original script hardcodes only algebraic identities (20/3, 1/90, 125, 8,
2 for the Seeley-DeWitt reduction), literal thresholds (1e-14, 1e-30,
1e-15), the 4D-integrated test function form `g(Y) = exp(-Y)(2+Y)`, and
the Lambda scan `[1, 2, 5, 10]`. NONE are framework constants. `from
canonical_constants import *` added per mandatory discipline
(math-scripts.md), not because any canonical name is used. Every
assignment tagged `# (local)`.

## 4. Environment

- Python: `C:/sandbox/Ainulindale Exflation/phonon-exflation-sim/.venv312/Scripts/python.exe`
- `OMP_NUM_THREADS=8` set at module import (CPU-only path; the largest
  array operation is a sum over 11,424 × 21 = 239,904 floats, well below
  the 100×100 matrix threshold for GPU usage).
- No torch / cupy required. No modification to canonical_constants.py.

## 5. SHA-256 input pins (64-char hex)

| File                                       | SHA-256                                                          | Bytes   |
|--------------------------------------------|------------------------------------------------------------------|---------|
| `computations/session-19/s19a_sweep_data.npz`        | `ad2a0da375f516aa24430db6630c733300428fa9682b0986a70b9b766aec1f5a` | 757,008 |
| `computations/session-23/s23a_kosmann_singlet.npz`   | `ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214` | 340,866 |
| `computations/_shared/r20a_riemann_tensor.npz`    | `fc256a9b4791b1d6e1416f93cabbb0e28fe0c858bf2aeb04414b7767a7351fe9` |  21,194 |

## 6. Closure SHA-256

Hash of `json.dumps(input_pins, sort_keys=True, separators=(',',':'))`:

```
f21c36e6a68c818ed5f04cda3332fd4e3564bcb04a2f67ca49f9e52b3f879059
```

Payload:
```
{"r20a_riemann_tensor.npz":"fc256a9b4791b1d6e1416f93cabbb0e28fe0c858bf2aeb04414b7767a7351fe9","s19a_sweep_data.npz":"ad2a0da375f516aa24430db6630c733300428fa9682b0986a70b9b766aec1f5a","s23a_kosmann_singlet.npz":"ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214"}
```

## 7. 4-tuple (S81 canonical verdict)

| Field      | Value                                                                  |
|------------|------------------------------------------------------------------------|
| value      | `7.814786e+03`                                                         |
| scheme     | `truncated_eta_zeta_reg_signed_power_sum`                              |
| convention | `BDI_lambda_minus_lambda_pairing_KOdim6`                               |
| L_max      | `11424_eigenvalues_s19a_sweep_21tau_grid`                              |
| sha256     | `f21c36e6a68c818ed5f04cda3332fd4e3564bcb04a2f67ca49f9e52b3f879059`     |

The `value` is the maximum `|eta_N(s)|` observed over sampled s in
{0.5, 1, 2, 4} × tau_indices {0, 4, 8, 12, 16, 20}. It is NOT machine
zero because the s19a archive stores non-negative |lambda| rather than
signed D_K eigenvalues (verified: n_neg = 0, n_pos = 11,424, min =
0.833, at tau_idx in {0, 10, 20}), so `np.sign(evals)` trivially
returns +1 and the eta formula degenerates to the zeta sum.

## 8. Substitution-chain checks performed in verdict

- **Dixmier ratio direction**: JSON summary reports
  `dixmier_monotone_decreasing=true`. Derived from
  `diffs = np.diff(dixmier_ratios)`, `np.all(diffs <= 1e-12)`.
  Physical interpretation: D_K stiffens (eigenvalues grow) under Jensen,
  so |D|^{-8} sum shrinks. Consistent with R_scalar growing 2.000 at
  tau=0 to 27.320 at tau=2.
- **Lichnerowicz bound**: min|lambda|(tau=0)=0.8333 ≥ sqrt(R/4)(tau=0)
  = sqrt(2/4) = 0.7071. Satisfied.
- **Seeley-DeWitt derivative signs**: da_2/dtau and da_4/dtau both
  positive for all tau in [0, 2] per tabulated output. No opposite-sign
  configuration, hence no Starobinsky-type extremum — structural
  conclusion unchanged from original.
- **R^2 dominance**: `R2_frac = 125 R^2 / (125 R^2 + |-8|Ric|^2 + 2K|)`.
  99.40% at tau=0, 98.75% at tau=1, 98.43% at tau=2.
- **Factorial divergence of a_{2k}**: estimated |a_6|/|a_4| ~ 2R grows
  from 4.0 (tau=0) to 54.6 (tau=2). Asymptotic expansion not
  convergent at any tau. Structural finding (unchanged).

## 9. Archive-format caveat (NEW finding)

The original s25 script claimed "max|eta| at all s, all tau: MACHINE
ZERO" and "APS boundary correction: 0 exactly" — both invalid
inferences from the s19a archive:

- Archive stores |lambda| only (verified: n_neg = 0 in every tau slice).
- `np.sign(|lambda|) = +1` for all entries.
- eta_N(s) reduces to sum |lambda|^{-s}, the truncated spectral zeta,
  which is finite and nonzero (7.81e+03 at the sampled grid).
- C7 "idx = N_evals" per sector (reported "NON-TRIVIAL") is the same
  artifact.

The BDI theorem (eta = 0 by lambda <-> -lambda pairing) is STRUCTURALLY
valid but was never actually verified against this archive. A signed
eigenvalue archive would be needed to empirically confirm eta = 0 at
this truncation.

This does not contradict proven BDI results; it records that one
item of the original workshop's "verification" column was asserted,
not measured.

## 10. Output

- Results NPZ (side-car): `computations/_shared/t3-intake/s25_connes_workshop.npz`
- Stdout log: `computations/_shared/t3-intake/s25_connes_workshop.stdout.log`
- Verdict: `computations/_shared/t3-intake/s25_connes_workshop_verdict.txt`
- Prep: `computations/_shared/t3-intake/prep-s25-connes-workshop.md` (this file)

No historical file is overwritten. The canonical `computations/session-25/s25_connes_results.npz` remains untouched.
