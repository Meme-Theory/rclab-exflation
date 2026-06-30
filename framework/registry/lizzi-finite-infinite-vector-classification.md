---
type: registry-canonical
ingested-by: /weave --update
---

# Lizzi Finite-Vector vs Infinite-Vector Regulator Classification

**Registry ID**: `lizzi-finite-infinite-vector-classification`
**Owner agent(s)**: `lizzi-spectral-functional-theorist` (primary); backstop `connes-ncg-theorist` per S86 plan W2 §W2-3.4
**Last updated**: `2026-04-26, S86-W2-C11`
**Ingestion**: `/weave --update` picks up this file; `knowledge.db` stores one row per entry. Project-level (not agent-private) because the gate `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` writes this file as its registry output (Output-target test for AMRI), and downstream gates pin it as Input-SHA (Input-pin test for AMRI).
**Source plan**: `sessions/session-plan/session-86-plan-w2.md` §W2-3
**Producing script**: `computations/s86_w2_c11_mellin_multiplier_infinite_vector.py`
**Status**: ACTIVE (S86 W2-C11 land)
**Consumer gates** (forward): S86 W1b T5 (Mellin-Strip Theorem), S86 W1b T6 (HP^1 near-invariance), S86 W1b T7, S86 W2 C9 (Mellin heat-kernel infra), S86 W2 C10, S86 W3-G56 (Heitsch cocycle), S87+ Lizzi-track entries to §VII.B.

**Provenance.** S86 W2-3 C11 gate `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` (PASS, max_rel_err = 8.07e-28 vs threshold 1e-12). Source carry-forwards: lizzi 9A §A-3 (INFINITE-VECTOR extension proposal) + lizzi S-1 §IV (the F_4 finite-vector formalism) + lizzi 3A §V.4 (the infinite-vector scaffold). Closed-form identity from Erdelyi 1953 Mellin transform tables; substitution chain in S86 plan w2 §W2-3.10. Type: project-level registry per `.claude/rules/agent-standards.md` §Memory Scope.

**Substrate framing.** The Mellin transform of the Zubarev kernel reveals that Zubarev acts on the substrate's spectral content as an **infinite-dimensional multiplier** (a continuous Mellin profile over s in C), while zeta acts as a **4-dimensional multiplier** on the discrete Seeley-DeWitt slots {a_0, a_2, a_4, a_6}. The substrate's spectral content (the D_K eigenvalue spectrum) is the same in both cases; the regulator-class asymmetry lives entirely in the lens, not in D_K.

This is NOT a statement that "Zubarev sees more of the substrate." Both regulators see all of D_K. The asymmetry is structural to the regulator's algebraic class — specifically, to the dimensionality of its multiplier vector over the spectral-action expansion.

---

## §1 Finite-Vector Class (Lizzi S-1 §IV formalism)

A regulator R belongs to the **finite-vector class** if there exists a finite integer N_R such that the spectral action expands as a finite linear combination of Seeley-DeWitt slots:

```
S_R[D_K] = sum_{n in S_R} f_n^R * a_n[D_K]
```

where S_R is a finite index set with |S_R| = N_R, the f_n^R are scalar multipliers (the finite-vector components), and a_n[D_K] is the n-th Seeley-DeWitt heat-kernel coefficient.

**Canonical example: zeta-regulator (S-1 §IV.5).** The zeta-regulated spectral action involves four discrete slots over the supported moments {0, 2, 4, 6}:

```
e_4^{zeta} = (f_0^{zeta}, f_2^{zeta}, f_4^{zeta}, f_6^{zeta}) = (1, 1, 1, 1) in R^4
```

(per the Connes-Moscovici 1995 residue convention; values 1 from the canonical zeta normalization at s=0).

**Members of F_4 (finite-vector with support {0, 2, 4, 6}):** zeta, SDW, sharp-cutoff, anomaly (when truncated at f_n=0 for n notin {0,2,4,6}). The Andrianov-Lizzi (arXiv:1001.2036) sharp-cutoff forces e_4^{cutoff} = (1/2, 1, 1, 1).

**Multiplier algebra:** componentwise multiplication and addition on R^4 (or R^|S_R|). The class is closed under linear combination and pointwise scaling.

**Dimensionality:** dim(multiplier space) = |S_R|, finite (typically 4 for canonical NCG).

---

## §2 Infinite-Vector Class (Lizzi 3A §V.4 + S86 C11 extension)

A regulator R belongs to the **infinite-vector class** if its spectral action is presented as a continuous integral against a Mellin profile, not a finite slot expansion:

```
S_R[D_K] = (1 / 2 pi i) int_{Re(s) = c} M_R(s) * Tr |D_K|^{-2s} ds
```

where M_R(s) is a function of complex s (the multiplier profile), the contour Re(s) = c sits in the regulator's strip of convergence, and the action couples to the full spectrum of D^{-2s} rather than to four discrete moments.

**Canonical example: Zubarev kernel f_Z(x) = exp(-x / Lambda_Z^2).** The Mellin transform is:

```
M[f_Z](s) = int_0^inf x^{s-1} exp(-x / Lambda_Z^2) dx = Lambda_Z^{2s} * Gamma(s)        (Erdelyi 1953)
```

Substitution chain (S86 plan w2 §W2-3.10): u = x / Lambda_Z^2, dx = Lambda_Z^2 du gives M[f_Z](s) = Lambda_Z^{2(s-1)} * Lambda_Z^2 * int_0^inf u^{s-1} exp(-u) du = Lambda_Z^{2s} * Gamma(s).

**Numerical verification (S86 C11, mpmath workdps=50, Lambda_Z = 1.0 M_KK units):**

| s | numerical (mp.quad) | closed-form Lambda_Z^{2s} * Gamma(s) | rel_err |
|:--|:----|:----|:----|
| 0.5 | 1.7724538509055160 | 1.7724538509055160 | 8.07e-28 |
| 1.0 | 1.0000000000000000 | 1.0000000000000000 | 0.0 |
| 1.5 | 0.8862269254527580 | 0.8862269254527580 | 0.0 |
| 2.0 | 1.0000000000000000 | 1.0000000000000000 | 0.0 |
| 2.5 | 1.3293403881791370 | 1.3293403881791370 | 0.0 |
| 3.0 | 2.0000000000000000 | 2.0000000000000000 | 0.0 |
| 3.5 | 3.3233509704478426 | 3.3233509704478426 | 0.0 |
| 4.0 | 6.0000000000000000 | 6.0000000000000000 | 0.0 |

max_rel_err = 8.07e-28; threshold 1e-12 PASS by 16 OOM. Cross-checks (i) M[f_Z](1) = Lambda_Z^2 and (ii) M[f_Z](2) = Lambda_Z^4 reproduce to rel_err = 0. Cross-check (iii) recurrence M[f_Z](s+1)/M[f_Z](s) = Lambda_Z^2 * s holds at rel_err <= 1.78e-51 across the sweep.

**Multiplier "vector":** a function M_R: C -> C, infinite-dimensional (the multiplier algebra is the algebra of analytic-on-strip functions, not R^N).

**Dimensionality:** dim(multiplier space) = aleph_1 (continuum); a single complex-analytic function over the strip of convergence.

**Mixed-support family M = {cutoff_sqrt, anomaly}.** These are ALSO infinite-vector when their Mellin profile is non-vanishing on a continuous set, BUT with a different multiplier algebra than Zubarev (e.g. cutoff_sqrt's profile has hyperbolic-secant-shaped strip behavior; anomaly's profile carries phase-discontinuity at integer s). The F_4 / M partition theorem is therefore NOT "finite vs infinite" alone — it is "finite-vector OR infinite-vector with discrete-support-only-on-{0,2,4,6}" vs "infinite-vector with mixed support."

---

## §3 Asymmetry Table

| Regulator | Class | Multiplier vector | Dimensionality | Strip of convergence (Re s) | Source |
|:--|:--|:--|:--|:--|:--|
| zeta | FINITE-VECTOR (F_4) | e_4^{zeta} = (1, 1, 1, 1) | 4 | residues at s in {0, 1, 2, 3} | Connes-Moscovici 1995; S-1 §IV.5 |
| SDW (f*) | FINITE-VECTOR (F_4) | e_4^{SDW} = (0.0883, 215.0, 6447, ...) (S78 W2-D) | 4 | finite (X_MAX=50 truncation) | S72 W2 PASS; S78 W2-D |
| sharp-cutoff | FINITE-VECTOR (F_4) | e_4^{cutoff} = (1/2, 1, 1, 1) | 4 | classical | Andrianov-Lizzi arXiv:1001.2036 |
| anomaly | FINITE-VECTOR (F_4, truncated) / INFINITE-VECTOR (M, untruncated) | depends on phi-expansion order | 4 (truncated) or aleph_1 | mixed | Andrianov-Lizzi arXiv:1001.2036; S78 W2-D |
| Zubarev | **INFINITE-VECTOR (unique in F_4 sub-atlas)** | M_Z(s) = Lambda_Z^{2s} * Gamma(s) | aleph_1 | Re(s) > 0 | **S86 C11 (this gate)** |
| cutoff_sqrt | INFINITE-VECTOR (M family) | M(s) related to sqrt(x) Mellin profile | aleph_1 | mixed | S72 W2; S86 C11 §2 last paragraph |

The unique-infinite-vector-in-F_4 status of Zubarev is what S-1's finite-vector formalism could not absorb (S-1 §IV expressed e_4 over a 4-dimensional vector space and no extension to function-valued multipliers existed). The C11 gate provides the closed-form Mellin profile that promotes Zubarev to infinite-vector class while keeping its support effectively at the same SD slots (the residues of Lambda_Z^{2s} * Gamma(s) at s in {0, 1, 2, 3} couple to the same {a_0, a_2, a_4, a_6} via the standard residue prescription).

---

## §4 Implications for the F_4 / M Partition Theorem

**Theorem statement (refined post-C11).** Let R denote any regulator admissible at the spectral triple's d_spec=8 NCG. Then R lies in exactly one of:

  (a) **F_4** = finite-vector class with support exactly {0, 2, 4, 6} (zeta, SDW, sharp-cutoff truncated; finite multiplier algebra over R^4).

  (b) **M** = mixed-support class (cutoff_sqrt, anomaly with non-truncated phi-expansion; infinite-vector with continuous Mellin profile having residues OUTSIDE {s in {0, 1, 2, 3}}).

  (c) **F_4-INF** = a singleton sub-atlas containing Zubarev: infinite-vector class WHOSE Mellin-profile residues land EXACTLY on the F_4 slots {0, 1, 2, 3} (i.e. {a_0, a_2, a_4, a_6}).

The pre-C11 partition was binary {F_4, M}. The C11 result splits F_4 into {F_4 finite-vector, F_4-INF singleton-infinite-vector} on the basis of multiplier-algebra dimension while preserving the SD-slot coupling structure. This is the **regulator-class structural floor** explaining why F_4 = {zeta, SDW, Zubarev} cannot collapse to a single equivalence class even when all three couple to the same a_n: zeta and SDW are R^4-vectors; Zubarev is a function on the strip Re(s) > 0.

**Downstream consequences.**

1. **Mellin Strip / Convergence Cone Theorem (T5 in S86 W1b).** Gains a sister classification pillar: the strip of convergence Re(s) > 0 of the Zubarev profile is exactly the analytic structure that the T5 cone identifies. Zubarev's infinite-vector membership is the analytic precondition for T5 to land at all.

2. **R-protected observables (S74 W4-F).** R-family ratios that cancel both the f_n choice AND the slot indices are FI under Zubarev because the entire multiplier profile cancels in the ratio — finite-vector regulators only cancel the f_n component-wise. Zubarev's R-protection is therefore stronger than zeta's, not weaker.

3. **F_4 sub-atlas heterogeneity (S83+ workshops).** Citations to "F_4 = {zeta, Zubarev, SDW}" must henceforth specify whether the result depends on the multiplier-algebra dimension (in which case Zubarev separates) or only on slot-support (in which case all three are equivalent). The drift between these two readings was the mechanism of S82 W2-8 / W2-D apparent regulator splits.

4. **No collapse to "Zubarev = enriched zeta."** Both regulators couple to the same a_n via residues, but the multiplier algebras have different dimensions; finite-dimensional projection of an infinite-vector profile onto e_4^{zeta} loses information (the off-residue strip behavior). The C11 closed-form Mellin transform is the algebraic record of what is lost.

5. **S86 W1b T5/T6/T7 + W3-G56 Heitsch cocycle anchor.** The T5 (Mellin strip) and T6 (HP^1 near-invariance) results both rely on Zubarev's analytic profile; the C11 closed-form M[f_Z](s) = Lambda_Z^{2s} * Gamma(s) is the anchor that makes those strip-bounded statements landable in the Lizzi-track cluster of §VII-B. T7 PASS reuses the same algebraic structure.

---

**Status.** S86 C11 (this gate) PASS lands the asymmetry as a registered framework distinction. Future syntheses citing "F_4 vs M partition" should reference this note for the multiplier-class dimension AND the SD-slot support, both. The finite-vs-infinite distinction is permanent — it follows directly from the algebraic structure of the Mellin transform of the regulator kernel and is independent of any computation choice.
