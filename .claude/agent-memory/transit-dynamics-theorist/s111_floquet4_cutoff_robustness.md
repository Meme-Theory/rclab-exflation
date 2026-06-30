---
name: s111-floquet4-cutoff-robustness
description: McLachlan Mathieu tongue half-width exponent theorem (Δa_½^(n) ∝ q_M^n) closes L_max≥12 re-opening of §VII.BP DEAD; the prefactor 1/64 at n=3 is load-bearing (bare-(q_M)³ mnemonic loose)
metadata:
  type: project
---

S111-CF-FLOQUET4 (§VII.CJ STAGE-1-CANDIDATE registration, Wave 5): cutoff-robustness scaling theorem protecting §VII.BP H-PARITY-DRIVE-EXCLUSION DEAD against any L_max≥12 truncation extension.

**The registered theorem (EXPONENT only)**: McLachlan/DLMF-28.6 n-th Mathieu instability-tongue half-width about a=n² has leading power exactly n on q. Sage-exact (`y'' + (a−2q cos2x)y=0` convention):
- n=1: full width = 2q − q³/32 ⇒ degree_q = 1
- n=2: full width = q²/2 − q⁴/18 ⇒ degree_q = 2
- n=3: full width = q³/32 (leading term IS q³) ⇒ degree_q = 3
The EXPONENT n is the registered claim; the ×16 (and ALL coefficient) prefactors are DIAGNOSTIC-ONLY / NOT registered (convention-ambiguous). Plan's "n=2→q²/12" is the a₂ characteristic-curve DISPLACEMENT coeff, not the n=2 tongue half-width (half-width = q²/4); the exponent is convention-independent so the registration is unaffected.

**Decisive prefactor finding (mnemonic-vs-exact discipline, math-scripts.md)**: the plan's bare `(q_M)^{n≥3} ≤ 1e-7` bound FAILS at the broad-band-max q_M=5.248e-3 (gives 1.445e-7 > 1e-7, off by 1.4×). The fix is the McLachlan PREFACTOR: at the worst-case high-A mode (A=9.000371, closest to zone n=3, npz i_closest=1168), the ACTUAL half-width is q³/64 = 2.26e-9, not bare q³. The LOAD-BEARING certificate is the NO-OVERLAP condition: half-width < detuning for ALL modes. From inv12_w3_2 npz: 0 of 1248 relic modes have half-width ≥ detuning; worst case A=9.000371 has half-width 2.26e-9 vs detuning 3.712e-4 (~5 OOM margin). High-A modes (A>9, the 80 modes a higher L_max would add near) land ONLY near zones n=3,4 (npz nearest_n∈{3,4}); zones n=1,2 saturated by low-A modes. So new modes get exponentially-suppressed tongues (q^{n≥3}/prefactor) and never overlap their detuning.

**Verdict**: Stage-1 registration PASS. §VII.BP DEAD is now cutoff-robustness-theorem-protected (3rd-pin: aggregate max|TrM|<2 + 84× depth-threshold + this L_max-extension theorem). Stage-2 cross-axis verify = separate S112+ gate.

**Key npz scalars** (inv12_w3_2_floquet_ordered_veil_resonance.npz): A_relic∈[0.876,12.646], q_relic∈[3.64e-4,5.25e-3], h_par=0.00083, A_zone_centers=[1,4,9,16,25,36], i_closest=1168 (→A=9.000371, the zone-n=3-nearest mode = my worst case, NOT the near-a=1 mode FLOQUET1 uses). tongue_halfwidth_relic max GLOBAL=9.32e-4 at A=2.245 (zone n=1); among A>9 max=4.05e-9.

Registry two-surface landing LANDED at slot **§VII.CJ** (master-index row + section body, single-shot AFTER-pattern, roundtrip_ok=True; frontier was §VII.CI). Verdict PASS, audit_sha256=5c762280c5c97d5d…, content_sha256=83062c4e9dcd0dfa…. Script: computations/session-111/s111_cf_floquet4_cutoff_robustness_theorem.py.

**Two reusable lessons (registry-landing single-shot, caught + fixed in-session)**:
1. np.savez keys CANNOT contain hyphens/`-7` (`bare_qM3_le_1e-7` parses as `bare_qM3_le_1e − 7` → SyntaxError). Use `_1em7`.
2. Section-body roundtrip-SHA self-reference trap: `build_promotion_text` returning `"\n### "+header` (leading \n) while `re_read_section` matches at `^### §VII.CJ` (no leading \n) makes the re-read SHA ≠ the built-text SHA → roundtrip FAIL. FIX: return section WITHOUT leading \n; `write_both_surfaces` adds the `\n\n` separator BEFORE `### ` (excluded by the `^###` match). NEVER embed a section's own SHA inside that section (circular). Embed the section SHA in the master-index ROW only (a provenance pointer, not what the section hashes). Master-index marker check must be case-insensitive (row says "Cutoff-Robustness", marker "cutoff-robustness").
3. Master-index table is NOT alphabetically contiguous: frontier rows §VII.CA-CI cluster at table TOP (lines 163-171), then older non-alphabetical rows. Splice new row AFTER the §VII.CI master-index ROW via exact-anchor regex `^(\|\s*§VII\.CI\b.*\n)`; append section body at EOF (last section). Two surfaces, one atomic write (temp + os.replace + fsync).

Cross-ref [[s101_w5_2_ladder_composition_results]] (Floquet/clock context), MEMORY.md FLOQUET INV12 W3-2 entry.
