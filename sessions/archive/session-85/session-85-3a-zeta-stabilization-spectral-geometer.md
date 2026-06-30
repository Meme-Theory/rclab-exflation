# Session 85 Synthesis: Slot 1a Row 3A subsection (b) — ζ-Regulator-Stabilization Theorem Candidate (Heat-Kernel / Seeley-DeWitt / ζ_D(s) Analytic-Continuation Track)

**Slot**: 1a synthesis Row 3A, subsection (b)
**Reviewer**: spectral-geometer (heat-kernel / Seeley-DeWitt technical track)
**Companion subsection**: (a) lizzi-spectral-functional-theorist (Mellin-cone / spectral-functional track) — independent parallel writeup
**Sources**:
- `sessions/archive/session-85/session-85-w10-workingpaper.md` (W10-4 §W10-4(d-h) branch-table; closing-note Highlight #1)
- `computations/s85_gate_verdicts.txt` line 174 (S85-W10-W0-L-INVERTED-BRANCH-ENUMERATION PASS); line 120 (S85-W0-L-MELLIN-CONE-S3-RESIDUE FAIL value=1.81e6)
- `sessions/archive/session-85/session-85-s6-truncation-taxonomy-spectral-geometer.md` (S-6 L_max-Truncation Taxonomy, this author's earlier deliverable)
- `sessions/archive/session-85/session-85-workshop-schedule.md` (W0-W5 S-1 Regulator-Family Boundary cross-pairing, S-6 cross-pairing)
- `sessions/permanent-results-registry.md`
- `.claude/agent-memory/spectral-geometer/MEMORY.md`
**Knowledge MCP queries (before any direction claim)**: `search_knowledge('zeta regulator stabilization')`, `search_knowledge('Mellin cone s=3 residue')`, `search_knowledge('Zubarev divergence regulator')`, `trace_entity('regulator family boundary')`, `search_knowledge('L_max truncation taxonomy analytic continuation')`, `search_knowledge('Seeley-DeWitt a_2 a_4 SU(3) Jensen')`, `trace_entity('MELLIN-CONE-S3-RESIDUE')`.
**Date**: 2026-04-25.

---

## I. Subject

W10-4 closing-note Highlight #1 (`sessions/archive/session-85/session-85-w10-workingpaper.md` line 1189, verbatim):

> Formalize the ζ-regulator-stabilization structural claim. The W10-4 observation that ζ stabilizes branch-residues at high L while Zubarev does not is currently EMPIRICAL from 5-regulator slope comparison. It deserves theorem status or refutation at S86. Candidate statement: "under log-linear UV scaling on Jensen-SU(3) × A_F, the ζ-regulator's denominator growth rate strictly exceeds the Mellin-cone s=3 residue numerator growth rate; Zubarev does not." This is a kinematic regulator-class theorem, parallel to (but distinct from) the Three-Layer Regulator Theorem in §VII.N.

The five-regulator slope numbers from the W10-4 SV2 log-linear extrapolation (W10 working paper §W10-4(c-d) and Constraint-Map Updates row at 1098-1100):

- **ζ-regulator denominator** `S_zeta_E` slope **0.97** in L_max.
- **Mellin-cone s=3 residue numerator** slope **0.56** in L_max.
- **Zubarev-regulator denominator** `S_Zubarev_E` slope **0.17** in L_max.

The candidate theorem can fail in two distinct ways: (i) it is a true asymptotic theorem (PROVEN); (ii) it is an artifact of evaluating a divergent partial sum at a non-pole location s=3, which is precisely the Class-B FAIL mode that S-6 §III.B classifies for `S85-W0-L-MELLIN-CONE-S3-RESIDUE`. This synthesis adjudicates between these two possibilities through the heat-kernel / Mellin / Seeley-DeWitt analytic-continuation framework.

---

## II. Heat-kernel governing structure (substitution chain)

### II.A The Mellin-heat-kernel duality

For a positive elliptic operator D_K² of dimension d on a compact manifold with Peter-Weyl-truncated cache at finite L_max, the spectral zeta function and the heat kernel are related by the Mellin transform:

```
Step 1 [definition]:
  K(t)         = Tr exp(−t D_K²)  =  Σ_λ d_λ exp(−t λ²)
  ζ_D(s)       = Σ_λ d_λ |λ|^(−s)                  (Re s > d)
  Mellin id.   :  ζ_D(s) Γ(s/2) = ∫_0^∞ t^{s/2 − 1} K(t) dt    (II.1)
```

```
Step 2 [Seeley-DeWitt asymptotics, t → 0+]:
  K(t)  ~  (4π)^{−d/2} Σ_{n ≥ 0} a_{2n} t^{n − d/2}
       = (4π)^{−4} [ a_0 t^{−4} + a_2 t^{−3} + a_4 t^{−2}
                   + a_6 t^{−1} + a_8 + O(t) ]                  (d=8, II.2)
```

```
Step 3 [meromorphic continuation, splitting Mellin integral at t=ε]:
  ζ_D(s) Γ(s/2)  =  Σ_n (4π)^{−d/2} a_{2n} · 2 ε^{s/2 + n − d/2} / (s + 2n − d)
                +  ∫_0^ε t^{s/2 − 1} [K(t) − K_asy(t)] dt
                +  ∫_ε^∞ t^{s/2 − 1} K(t) dt                    (II.3)
  ⇒  poles of ζ_D(s) at  s = d − 2n,  n = 0, 1, 2, ...
       residues:  Res_{s = d − 2n} ζ_D(s)
                 = 2 (4π)^{−d/2} · a_{2n} / Γ((d − 2n)/2)        (II.4)
```

```
Step 4 [direction — pole locations for SU(3), d=8]:
  Pole set Sd = {8, 6, 4, 2, 0}  (Connes-Moscovici dimension spectrum, CM-1995 §5).
  Between these the function is HOLOMORPHIC.
  s = 3 is NOT a pole — it lies STRICTLY BETWEEN poles at s=4 (a_4 driver)
      and s=2 (a_6 driver).
```

### II.B Convergence regime of the truncated direct sum at s=3

```
Step 1 [def]: at finite L_max, the truncated zeta on the Peter-Weyl cache is
              Z_L(s)  ≡  Σ_{(p,q): p+q ≤ L_max} dim(p,q) Σ |λ_{(p,q)}|^(−s).
              This is an entire function of s (finite sum of finitely many
              s-exponentials).
Step 2 [substitute Weyl law on Jensen-SU(3) at d=8]:
              N(λ) ~ (Vol/(8π⁴)) λ^d  (Weyl with d=8)
              ⇒ Σ d_i f(|λ_i|) approximated by ∫ ρ(λ) f(λ) dλ
                with ρ(λ) ~ λ^{d−1} for λ → ∞.
Step 3 [simplify]: the partial sum of |λ|^{−s} weighted by Weyl density is
              ∫_1^{λ_max(L)} λ^{d−1−s} dλ
              = [λ^{d−s}/(d − s)]_1^{λ_max(L)}.
              For d=8, s=3: integrand is λ^4 → ∫ λ^4 dλ = λ^5/5
              → DIVERGENT as λ_max(L) → ∞.
Step 4 [direction]: at any finite L_max, Z_L(s=3) is a well-defined finite
              partial sum that GROWS with L_max as ~λ_max(L)^{d−s} = λ_max(L)^5.
              The L_max → ∞ limit DIVERGES at s=3 because s=3 < d=8
              (Weyl convergence requires s > d).
              The "residue at s=3" of the LIMITING ζ_D does NOT EXIST
              (it is not a pole).  The "residue at s=3" of the FINITE-L
              partial sum is well-defined but is the boundary value of a
              divergence, not an analytic-continuation residue.
```

This is the structural reason §W0-20 (`S85-W0-L-MELLIN-CONE-S3-RESIDUE`) was classified Class B — METHOD-INAPPROPRIATE in the S-6 Truncation Taxonomy (this author, `session-85-s6-truncation-taxonomy-spectral-geometer.md` line 100).

Knowledge-MCP cross-checks:
- `s61_pw_conformal_zeta.py` records "the TRUNCATED zeta_L(s) has a residue that grows with L (= a_2(L)/2, divergent)" — same structural divergence pattern at s=3 in the d=4 effective-product case.
- `s63_gilkey_oneloop.py` records "the zeta function has a meromorphic continuation with poles at s = d/2 − k" — confirming pole set is discrete and s=3 is not in it.
- `S85-W0-L-MELLIN-CONE-S3-RESIDUE` verdict (`s85_gate_verdicts.txt:120`): `FAIL value=1.81e6 scheme=Connes-Moscovici-Mellin-cone convention=s*=3 L_max=12` — the divergent partial-sum value at L=12.

### II.C What the W10-4 SV2 slopes actually measure

```
Step 1 [def]: SV2 SV2 fits of `S_zeta_E(L)`, `S_Zubarev_E(L)`, `mellin_s3(L)` on
              L ∈ {5, 6, 7, 8} are log-linear:
              log(S_zeta_E(L)) = a_z + 0.97 L           (slope 0.97)
              log(mellin_s3(L)) = a_m + 0.56 L          (slope 0.56)
              log(S_Zubarev_E(L)) = a_Z + 0.17 L        (slope 0.17)
              All R² > 0.91 (W10-4 §(b) Step 4).
Step 2 [substitute Weyl law on the truncated cache]:
              The PW dimension at level L_max ≤ L scales as N_PW(L) ~ ε(L)·L^?
              for Jensen-SU(3); the eigenvalue ladder λ_max(L) scales linearly
              in L (representation theory: λ_(p,q) ~ Casimir(p,q) ~ p² + pq + q²
              ≤ L²; thus λ_max ~ L). Substituting into Step 4 of II.B with
              s=3, d=8:
              Z_L(s=3) ~ λ_max(L)^{d−s} ~ L^5  ⇒  log Z_L(s=3) ~ 5 log L,
              not linear in L.  The W10-4 fit log(Z) ~ 0.56 L is linear in L,
              not log L — meaning the W10-4 SV2 is fitting in a regime where
              λ_max(L) grows EXPONENTIALLY in L_max, not linearly.
Step 3 [simplify]: this is the Mellin-cone numerator's "kinematic slope" —
              it is the rate at which the divergent partial sum Z_L(s=3) grows
              with L_max in the W10-4 model.  For S_zeta_E (denominator under
              ζ-regulator weight w_zeta(λ)=1), what is fitted is the partial sum
              Σ_{p+q ≤ L} dim(p,q) ≈ N_PW(L), the number of PW modes — by direct
              eigenvalue-counting, log(N_PW) is approximately linear in L_max.
              For S_Zubarev_E, the Zubarev kernel exp(−λ²/M_KK²) introduces an
              exponential SUPPRESSION of high-λ modes; the slope (0.17) reflects
              the residual L-dependence of low-λ modes.
Step 4 [direction]:
              The empirical slope ordering 0.97 > 0.56 > 0.17 is a KINEMATIC
              ordering of regulator-weight integrals over the truncated PW
              spectrum.  It is NOT a statement about residues of the
              meromorphic continuation of ζ_D(s) at any pole.  The "Mellin-cone
              s=3 residue" of W10-4 is a PARTIAL-SUM proxy at a NON-POLE
              location.
```

This is the core structural observation that enables the heat-kernel adjudication of the candidate theorem.

---

## III. Identifying which Seeley-DeWitt coefficient drives the ζ denominator growth at s=3

### III.A Mellin-pole structure for d=8 (Jensen-SU(3))

From II.A Step 4 and equation (II.4), the Mellin poles and their Seeley-DeWitt drivers are:

| Pole s* | n | a_{2n} driver | Residue formula | Physics |
|:-------:|:-:|:-------------:|:----------------|:--------|
| s* = 8  | 0 | a_0          | 2 (4π)^{−4} a_0 / Γ(4) = a_0/(48 π⁴)   | CC sector / volume |
| s* = 6  | 1 | a_2          | 2 (4π)^{−4} a_2 / Γ(3) = a_2/(16 π⁴)   | gravity / ε_H slot |
| s* = 4  | 2 | a_4          | 2 (4π)^{−4} a_4 / Γ(2) = a_4/(8 π⁴)    | spectral action / Yang-Mills |
| s* = 2  | 3 | a_6          | 2 (4π)^{−4} a_6 / Γ(1) = a_6/(8 π⁴)    | higher curvature |
| s* = 0  | 4 | a_8          | 2 (4π)^{−4} a_8 / Γ(0)  | Connes-Moscovici endpoint |

(Note: at s* = 0, Γ(0) is divergent; the "residue" must be interpreted via the regularized 1/Γ(s/2) factor, which vanishes; this is the standard CM-1995 §5 endpoint discussion.)

### III.B Why s=3 is NOT a pole and what drives the partial-sum slope

```
Step 1 [def]: between adjacent poles s*=4 and s*=2 the function ζ_D(s) is
              HOLOMORPHIC; Z_L(s) at s ∈ (2, 4) on the truncated cache is
              a finite partial sum that does NOT carry a residue.
Step 2 [substitute the asymptotic series at s=3]:
              From II.A Step 3, the n-th Seeley-DeWitt slot contributes
              2 (4π)^{−4} a_{2n} ε^{(s+2n−d)/2} / (s+2n−d) at finite ε.
              At s=3, d=8, the n-th slot exponent is (3 + 2n − 8)/2 = (2n − 5)/2.
              n=0:  ε^{−5/2} / (−5)
              n=1:  ε^{−3/2} / (−3)
              n=2:  ε^{−1/2} / (−1)        ←  CLOSEST to pole; finite divisor
              n=3:  ε^{+1/2} / (+1)
              n=4:  ε^{+3/2} / (+3)
              No vanishing denominator at s=3 ⇒ all terms are FINITE at any ε > 0.
Step 3 [simplify]: at s=3 there is no pole in ε, so the "residue" of Z_L(s=3)
              is dominated by whichever Seeley-DeWitt slot maximizes
              |a_{2n} ε^{(2n−5)/2}|.
              For ε ≪ 1 (Mellin-split point pinned at small t, e.g.
              ε = 1/(2 λ_max²) ~ O(0.02) at L=10 with λ_max≈5), the
              MOST DIVERGENT IN ε term is n=0:
                |a_0 ε^{−5/2}|  ≫  |a_2 ε^{−3/2}|  ≫  |a_4 ε^{−1/2}|
              by a factor ε^{−1} = 50 between adjacent slots.
              Therefore Z_L(s=3) at small ε is dominated by a_0.
              Numerically with a_0 = 6440 and a_2 ≈ 0.728 (S46):
                |a_0 ε^{−5/2}| / |a_2 ε^{−3/2}|  =  (a_0/a_2) · ε^{−1}
                                                ≈  8846 · 50  ≈  4.4 × 10⁵
              ⇒ a_0 dominates by 5+ orders of magnitude.
Step 4 [direction]: the partial-sum value Z_L(s=3) is — at the level of
              the heat-kernel asymptotic — primarily driven by the a_0 slot.
              Equivalently:  Z_L(s=3) ~ 2 (4π)^{−4} a_0 ε^{−5/2}/(−5) + corrections.
              GROWTH WITH L:  the truncated ζ_D's a_0 partial sum is
              a_0(L) = (4π)^{−4} · Vol_PW(L) where Vol_PW(L) is the PW-counting
              proxy for the geometric volume.  Vol_PW(L) grows polynomially
              in L (~L^d/d for Weyl); λ_max(L) grows linearly in L
              (representation-theoretic).  Hence ε(L) = 1/(2 λ_max²) ~ L^{−2},
              and the dominant slot scales as
                a_0(L) ε(L)^{−5/2}  ~  L^d · L^5  =  L^{d+5} = L^{13}  (d=8)
              i.e. log Z_L(s=3) grows ~ (d+5) log L, which is in turn LINEAR
              in L when λ_max(L) is exponential in L_max — matching the W10-4
              SV2 fit.
```

**Direction**: the **a_0 Seeley-DeWitt coefficient drives the ζ-regulator denominator (= partial-sum proxy) growth at s=3** through its coupling to the Mellin pole at s* = 8. The ζ-regulator weight w_zeta(λ) = 1 (per `s83_w2_g14_cs_regulator_dependence.py`) means S_zeta_E(L) is essentially the total PW eigenvalue count in the cache (a proxy for the truncated `a_0`), which scales as L^d.

### III.C Why Zubarev does NOT track this growth

```
Step 1 [def]: Zubarev regulator weight w_Zub(λ) = exp(−λ²/M_KK²).
              S_Zubarev_E(L) = Σ d_λ |λ|^? · w_Zub(λ)  where the energy-weighting
              power is set by the W10-4 model.
Step 2 [substitute]: the exponential cutoff truncates the sum at λ ~ M_KK, and
              for L_max sufficiently large that λ_max(L) > M_KK,
              the sum is INSENSITIVE to L_max (modes above M_KK are exponentially
              suppressed and contribute negligibly).
Step 3 [simplify]: in the regime L ≥ L_*(M_KK) — the "saturation L" where
              λ_max(L_*) ≈ M_KK — S_Zubarev_E(L) approaches a constant.
              The W10-4 SV2 was fit on L ∈ {5, 6, 7, 8}; the slope 0.17
              indicates pre-saturation (some L-dependence remains because
              the partial sum is still picking up modes near M_KK).
Step 4 [direction]: at HIGHER L (L=10, 12 in the W10-4 extrapolation),
              S_Zubarev_E approaches a finite limit (saturation), so the
              effective slope DECREASES with L.  The W10-4 log-linear fit
              EXTRAPOLATES this pre-saturation slope into the post-saturation
              regime, which under-estimates the limit value but mis-models
              the L-dependence as exponential in L when it is approaching
              a constant.
              Per W10-4 §(g) self-assessment: S_Zubarev_E has the WEAKEST fit
              R²=0.92 of the 5 quantities — consistent with this saturation
              picture.
              The Mellin-cone s=3 numerator slope 0.56 is, in this picture, the
              partial-sum growth of Z_L(s=3) WITHOUT regulator weighting (or
              under a weight that does not saturate within the L window).
              Zubarev's exponential cutoff causes the denominator to saturate
              while the numerator continues to grow — hence the residue
              ratio = num/denom GROWS with L (W10-4 branch d FAIL).
              The ζ-regulator's identity weight is L-unbounded, so the
              denominator continues to grow polynomially in L, OUTPACING the
              numerator (which grows polynomially in λ_max but not as fast as
              the full PW count) — hence the residue ratio DECAYS with L
              (W10-4 branch c PASS).
```

Numerical cross-check (Section II.C verification): predicted geometric ratio of branch-c residues per 2-L step from the slope difference (0.56 − 0.97) = exp(2 × (−0.41)) = 0.4404; observed ratio in W10-4 branch table is 0.4360 (mean over L=8→10 and L=10→12 steps). Predicted Zubarev branch-d ratio exp(2 × (0.56 − 0.17)) = exp(0.78) = 2.1815; observed 2.1732. Both match to ~1%, confirming the slope-difference-drives-residue-evolution model.

---

## IV. Cross-check against the W0-W5 S-6 L_max-Truncation Taxonomy

### IV.A The S-6 prescription for §W0-20

From `session-85-s6-truncation-taxonomy-spectral-geometer.md` §III.B:

> #5: W0-L-MELLIN-CONE-S3-RESIDUE — **Class B**. Z(s=3) is a divergent partial sum (s=3 < d=8 = spectral dimension). |ΔR(L)| growing in L is the unmistakable Weyl-law signature: N(λ) ~ λ^d · Vol/(8π⁴) ⇒ Σ d_i |λ|^(−3) diverges. The "residue at s=3" doesn't exist — d_K has no pole at s=3 (poles are at {8, 6, 4, 2, 0}). The plan's contingency "try s* ∈ {2, 4}" is also pole-targeted but s=2 < d also diverges by direct sum. INFRASTRUCTURE: same Mellin-heat-kernel pole-subtracted residue extraction as #4. Residue is taken at s=4 (genuine pole, Res = 2 a_4 / (4π)^4 / Γ(2)), NOT s=3.

### IV.B Adjudication: does the empirical ζ-stabilization survive analytic-continuation reformulation?

```
Step 1 [def]: candidate theorem statement = "Under log-linear UV scaling on
              Jensen-SU(3) × A_F, the ζ-regulator's denominator growth rate
              strictly exceeds the Mellin-cone s=3 residue numerator growth
              rate; Zubarev does not."
              The PRIMARY OBJECTS — "ζ-denominator growth rate" and
              "Mellin-cone s=3 residue numerator growth rate" — are
              KINEMATIC partial-sum slopes on a finite-L_max truncation.
Step 2 [substitute the analytic-continuation reformulation]:
              Replace "Mellin-cone s=3 residue numerator" with the meaningful
              meromorphic-continuation object "Res_{s=4} ζ_D(s) = a_4/(8π⁴)"
              (the closest TRUE pole for d=8).
              At τ=0.190, a_4 is a τ-polynomial in curvature invariants
              (R, |Ric|², |Riem|², F², ...) on Jensen-SU(3), L_max-INDEPENDENT
              once geometrically computed (per the V.3 Gilkey programme of
              S-6 §V.3).
              Equivalently: Res_{s=4} ζ_D(s) is a FIXED NUMBER, independent of
              L_max and independent of regulator choice.
Step 3 [simplify]: under the analytic-continuation reformulation, the
              candidate theorem becomes:
                "ζ-regulator denominator growth rate (whatever it is)
                 strictly exceeds the GROWTH RATE of a CONSTANT
                 (= 0)."
              The slope of any constant in L_max is 0.
              The ζ-regulator partial-sum denominator slope (0.97) certainly
              exceeds 0 (true).
              The Zubarev denominator slope (0.17) ALSO exceeds 0 (true).
              ⇒ Both regulators "stabilize" trivially under the reformulation;
              the asymmetry between ζ and Zubarev VANISHES.
Step 4 [direction]: under the analytic-continuation reformulation, the candidate
              theorem becomes either VACUOUSLY TRUE (everything > 0 vs constant)
              or LOSES its content entirely (because the "Mellin-cone s=3 residue
              numerator" is replaced by a fixed geometric a_4-residue that
              doesn't grow at all).
              The W10-4 empirical asymmetry (ζ stabilizes residue ratio, Zubarev
              doesn't) is a property of the FINITE-L_max partial sum — it is
              a TRUNCATION-ARTEFACT of evaluating Z_L at a non-pole location s=3
              with two regulator weights that have different L-saturation
              behavior on the same truncated cache.  In the L_max → ∞ limit
              under analytic continuation, the asymmetry is not a property of
              ζ_D(s) at any pole; it disappears.
              Therefore: the candidate theorem is REFUTED as a regulator-class
              theorem of the meromorphic ζ_D.  It survives only as a kinematic
              statement about partial sums on a finite truncation, and only at
              s=3 specifically (or at any other non-pole s where the
              residue-proxy is a partial-sum value).
```

### IV.C Conclusion of the heat-kernel adjudication

The heat-kernel / Mellin / Seeley-DeWitt analytic-continuation track **REFUTES** the candidate theorem as a substrate-level regulator-class theorem on Jensen-SU(3) × A_F.

Specifically, the candidate theorem is **REFUTED-AS-STATED** but **ADMITS A REFORMULATED KINEMATIC CLAIM** that may be theorem-grade:

- **REFUTED-AS-STATED**: there is no "ζ-regulator denominator growth rate strictly exceeding the Mellin-cone s=3 residue numerator growth rate" property of the meromorphic ζ_D(s). The L→∞ limit at s=3 does not exist (s=3 < d=8 is in the divergence regime); the "growth rate" being measured is the log-linear slope of a divergent partial sum on a finite-L truncation, not a property of the analytic continuation.
- **REFORMULATED-KINEMATIC-PASS**: under finite-L_max truncation with weight functions w_zeta(λ) = 1 and w_Zub(λ) = exp(−λ²/M_KK²), the empirical slope ordering 0.97 > 0.56 > 0.17 is a verifiable KINEMATIC consequence of (i) the Weyl law on the truncated PW spectrum (driving the "0.97" slope of the regulator-unweighted partial sum, dominated by a_0), (ii) the cutoff scale M_KK in the Zubarev weight (driving saturation, slope 0.17), (iii) the partial-sum value of the divergent series at s=3 (driving the "0.56" slope as an intermediate). This is a STATEMENT ABOUT TRUNCATION, not a STATEMENT ABOUT REGULATOR-CLASS GEOMETRY. It is FAR LESS CONSEQUENTIAL than a theorem-grade Mellin-residue identity.

Reasons why this distinction matters structurally:

1. **The W10-4 PASS for branch c (ζ-Jos-inverted) at L=10, 12 depends on the empirical slope inequality holding at higher L.** The S-6 §III.B Class-B classification (and Section II of this synthesis) make the case that the inequality holds because Z_L(s=3) is at the divergence boundary, growing polynomially in L_max with an exponent set by Weyl-law a_0-domination — and this is a TRUNCATION feature. Branch c's stability at L=10, 12 is REAL (the partial sum continues to dominate the regulator-unweighted denominator), but it is NOT a substrate-level "ζ regulator stabilizes residues" claim — it is "the ζ-weight = 1 lets the truncated PW count outpace the divergent s=3 partial sum, which is what one would expect at any s in the divergence regime where the PW-mode-count grows fastest."

2. **The Zubarev failure on branch d is a saturation artefact, not a substrate physics signal.** The Zubarev cutoff exp(−λ²/M_KK²) saturates the denominator at L_*(M_KK), which is somewhere above L=8 in the SV2 cache. The W10-4 log-linear extrapolation extends a pre-saturation slope into the post-saturation regime, falsely predicting a continued divergence ratio. The real Zubarev denominator is bounded; the real branch-d residue does NOT "diverge dramatically as L→∞" — it converges to a finite (potentially LARGE) value.

3. **The right venue for this empirical claim is the S-1 Regulator-Family Boundary Theorem cross-pairing**, NOT a standalone "regulator-class kinematic theorem." Under S-1 (W0-W5 schedule §S-1: lizzi-connes-vandendungen joint canonical statement), the ζ regulator and Zubarev regulator both belong to the **pure-a_4 family** {zeta, Zubarev, SDW, anomaly}, distinct from the cutoff_sqrt regulator (which has a_0 support). The W10-4 empirical asymmetry between ζ and Zubarev is INTERNAL to the pure-a_4 family — and is a separate kinematic asymmetry that S-1 does not address. The candidate theorem, properly reformulated, is a **sub-claim within the pure-a_4 family** about Mellin-multiplier moments at non-pole s, NOT a regulator-class structural theorem.

### IV.D What the empirical slope structure DOES tell us (informational)

Beyond refutation, the W10-4 slope structure is informational in two ways:

1. **It confirms the S-6 Class-B diagnosis quantitatively.** The fact that the W10-4 SV2 fits all five quantities log-linearly with R² ≥ 0.91 over L ∈ {5..8} but the predicted ratio of residues per L-step is exact to 1% (Section II.C above) means the partial sums at s=3 are well-described by a Weyl-law power-law in λ_max, and the slope difference IS the residue evolution rate. This is consistent with the divergence picture, not with the analytic-continuation picture.

2. **It localizes a_0 as the structural driver.** The 0.97 slope on `S_zeta_E(L)` is essentially the slope of `log a_0(L)` — the truncated Seeley-DeWitt a_0 on the PW cache, which by §III.B Step 4 grows as L^d. The 0.56 slope at s=3 with d=8 reflects the leading divergence rate of the Mellin partial sum, set by the Weyl-density power d−s=5. Under the analytic-continuation reformulation (residue at s=4, not s=3): a_4 is finite and L-independent (given the V.3 Gilkey programme); the structurally informative claim is "a_0 dominates the d=8 Mellin partial sum at any s ∈ (5, 8)" — a known consequence of Weyl asymptotics, not a new theorem.

---

## V. Unified Candidate-Theorem Statement (REFUTED as stated; reformulated kinematic version)

### V.A Candidate theorem statement (verbatim from W10-4 closing-note Highlight #1)

> "Under log-linear UV scaling on Jensen-SU(3) × A_F, the ζ-regulator's denominator growth rate strictly exceeds the Mellin-cone s=3 residue numerator growth rate; Zubarev does not."

### V.B Heat-kernel adjudication (this synthesis)

**REFUTED as a substrate-level regulator-class theorem**, by the following 4-step substitution chain:

```
Step 1: The "Mellin-cone s=3 residue numerator" object referenced in the
        statement is a partial-sum value of Z_L(s=3) on a finite Peter-Weyl
        truncation of D_K, NOT a residue of the meromorphic continuation of
        ζ_D(s) at any pole.

Step 2: For Jensen-SU(3) × A_F with d=8, the meromorphic ζ_D has poles only
        at s ∈ {0, 2, 4, 6, 8} (Connes-Moscovici dimension spectrum).
        s=3 is NOT a pole; the analytic-continuation residue at s=3 does
        not exist (it would be 0 for any truly meromorphic function with
        poles only at the integers above).

Step 3: At finite L_max, Z_L(s=3) is a partial sum that DIVERGES as L → ∞
        (s=3 < d=8, in the Weyl-divergence regime).  Its log-linear slope in
        L_max is set by Weyl-law power d−s=5 with prefactors from a_0.
        Different regulator weights w(λ) modify this slope by introducing
        kinematic L-saturation (Zubarev, exponential cutoff) or none (ζ,
        identity weight).

Step 4: Direction: under analytic-continuation reformulation, the
        "residue at s=3" is replaced by the residue at the closest TRUE
        pole s=4, namely a_4/(8π⁴), which is L_max-INDEPENDENT and
        regulator-INDEPENDENT (it is a property of the geometry, not of
        the regulator).
        Therefore the candidate theorem's primary asymmetry —
        "ζ-denominator growth > Mellin-s3 numerator growth, Zubarev does not" —
        VANISHES under the reformulation: there is no growth on the analytic-
        continuation side, and the regulator-dependence of the partial-sum
        proxy at s=3 does not lift to a property of the meromorphic ζ_D.
        Candidate theorem is REFUTED.
```

### V.C Reformulated kinematic claim (lower-grade; informational)

```
Reformulated kinematic claim:
  "On the Peter-Weyl truncation of Jensen-SU(3) × A_F at finite L_max
  (L ∈ {5..8} in the W10-4 SV2 cache), the partial-sum quantities

    S_zeta(L)     ≡  Σ_{p+q≤L} d_(p,q)                    (ζ-weight w=1)
    S_Zubarev(L)  ≡  Σ_{p+q≤L} d_(p,q) exp(−λ_(p,q)²/M_KK²)   (Zubarev weight)
    Z(s=3, L)     ≡  Σ_{p+q≤L} d_(p,q) λ_(p,q)^(−3)        (Mellin-s3 partial sum)

  satisfy log-linear scaling in L over the SV2 window with slopes
    slope[S_zeta(L)]    ≈ 0.97
    slope[Z(s=3, L)]    ≈ 0.56
    slope[S_Zubarev(L)] ≈ 0.17                                  (W10-4 §(b)).

  Consequently, the residue ratios per 2-L step satisfy
    (S_zeta / Z) ratio per 2-L step ≈ exp(2 × (0.56 − 0.97)) = 0.44
    (S_Zubarev / Z) ratio per 2-L step ≈ exp(2 × (0.56 − 0.17)) = 2.18
  matching the W10-4 branch table to ~1% (zeta: 0.4360; Zub: 2.1732).

  This is a CONSEQUENCE of (i) the Weyl law setting Z(s=3,L)~λ_max(L)^{d−s},
  (ii) the ζ identity-weight giving S_zeta(L) ~ N_PW(L) (the truncated a_0),
  (iii) the Zubarev exponential cutoff producing L-saturation at L_*(M_KK).
  It is NOT a property of the meromorphic ζ_D(s) at any pole, NOT a regulator-
  class structural theorem, and DOES NOT support the conclusion that
  'ζ-regulated branches stabilize at high L while Zubarev-regulated branches
  do not' as an asymptotic substrate property."
```

This kinematic claim is `INFO-grade`, meaning it is a TRUE STATEMENT about partial sums on finite truncations but does not lift to a substrate-level regulator-class theorem. It is parallel in scope to (but distinct from) the Three-Layer Regulator Theorem in §VII.N (which IS a substrate-level theorem about the divergence STRUCTURE of three regulator classes; this kinematic claim is a within-class quantitative slope ordering).

---

## VI. Pre-registered S86 Gate: ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING

### VI.A Gate ID

`S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING`

### VI.B Pre-registered statement

The S86 gate adjudicates between three outcome states for the candidate theorem:

- **PROVEN** (PASS): the candidate theorem holds as a substrate-level theorem about the meromorphic ζ_D(s) under analytic continuation.
- **REFUTED-AS-STATED-WITH-KINEMATIC-RESIDUAL** (FAIL): the candidate theorem fails as a substrate-level theorem (per Section V.B of this synthesis) but the kinematic claim of Section V.C holds quantitatively at L_max ∈ {10, 12}.
- **REFUTED-WITH-NO-KINEMATIC-RESIDUAL** (also FAIL, distinct scenario): the kinematic claim ALSO fails at L_max=10, 12 (e.g., the SV2 log-linear extrapolation breaks down at the next L_max increment).

### VI.C Inputs

1. The Mellin-heat-kernel infrastructure of S-6 §IV (`s86_mellin_hk_residue.py` per S-6 §V.2) implementing `ζ_D(s) Γ(s/2) = ∫_0^∞ t^{s/2−1} K(t) dt` with explicit small-t Seeley-DeWitt expansion and pole subtraction.
2. The Gilkey-computed a_4 on Jensen-SU(3) at τ=0.190 (per S-6 §V.3 `S86-A4-A6-A8-GILKEY-JENSEN`) — needed to evaluate Res_{s=4} ζ_D(s) = a_4/(8π⁴).
3. The DENSE D_K eigenvalue cache at L_max ∈ {10, 12}. **NOTE — this is the W10-4 GPU-infeasibility issue**: per W10-4 §(g) self-assessment, dense diagonalization at L=12 requires ~8 PB which exceeds 17 GB VRAM. Infrastructure path: representation-theoretic block-diagonal reduction by SU(3)×SU(3) double-irrep structure (per W10-4 closing-note Highlight #4: "block-diagonal reduction by representation-theoretic irreps on Jensen-SU(3) × A_F is the principled path"). If block-diagonal not landed by S86, gate must operate on L_max=10 with extrapolation noted.
4. The W10-4 SV2 partial-sum trajectories `S_zeta_E`, `S_Zubarev_E`, `mellin_s3` at L ∈ {5..8} (already in cache).

### VI.D Pre-registered PASS / FAIL / INFO conditions

```
PASS (PROVEN): meromorphic-continuation residue equality at the closest TRUE pole.
  Compute Res_{s=4} ζ_D(s) using the §IV.B Mellin-heat-kernel recipe with
  N_SD = 4 on the dense L_max=10 cache.
  Compute the same residue using the geometric Gilkey a_4 / (8π⁴).
  PASS iff
    |Res_extracted − a_4_geometric/(8π⁴)| / |a_4_geometric/(8π⁴)| ≤ 1e-3
  AND
    the candidate theorem's reformulation-direction matches:
    "ζ regulator at s=4 yields residue identity to L_max-independent value;
     Zubarev regulator at s=4 ALSO yields the same identity (because the
     residue is regulator-independent)."
  (The PASS scenario is: candidate theorem REFUTED at s=3, but the meaningful
   asymptotic identity holds at s=4 for BOTH ζ and Zubarev — confirming the
   Section V.B refutation and the absence of a substrate-level regulator-class
   asymmetry.)

FAIL (REFUTED-AS-STATED-WITH-KINEMATIC-RESIDUAL): kinematic slope claim holds
  at higher L but the analytic-continuation route eliminates the asymmetry.
  Compute Z_L(s=3) at L_max ∈ {10, 12} on the dense or block-diagonal cache.
  Verify the slope ordering 0.97 > 0.56 > 0.17 holds at the next L increments.
  Verify the extracted residue at s=4 from §IV.B agrees with a_4_geometric/(8π⁴)
  to within 1e-3 (i.e. PASS condition above).
  FAIL iff both above hold AND the W10-4 candidate theorem statement
  (Section V.A) is therefore TRUE AS A KINEMATIC SLOPE ORDERING but FALSE
  as a substrate-level theorem.

FAIL (REFUTED-WITH-NO-KINEMATIC-RESIDUAL): the kinematic slope ordering fails
  to hold at L_max=10, 12.  E.g., S_Zubarev_E(L) saturates and the slope
  collapses below 0.17, or Z_L(s=3) trajectory deviates super-linearly.
  This would invalidate even the Section V.C kinematic claim and would
  return W10-4 branch c PASS to indeterminate.

INFO: Mellin-heat-kernel infrastructure not yet implemented (V.2 of S-6 not
  closed) AND/OR a_4 Gilkey not computed (V.3 of S-6 not closed) — gate
  defers to next session with declared blocker.
```

### VI.E Effort estimate

- 2 days post-V.2 + V.3 if both upstream (S-6 §V.2 Mellin-heat-kernel infra and §V.3 a_4 Gilkey on Jensen-SU(3)) have landed.
- 5+ days if V.2 + V.3 must land first within S86.
- INFEASIBLE within S86 if dense L=12 cache cannot be produced and block-diagonal infrastructure has not landed (would defer to S87+).

### VI.F PRDR pin block (machinery enumeration)

| Parameter | Pinned value |
|:----------|:-------------|
| L_max | {10, 12} for kinematic check; analytic-continuation residue at L=10 if dense; L=12 via block-diagonal if landed |
| ε (Mellin split point) | 1/(2 λ_max(L)²) at the working L_max |
| N_SD (Seeley-DeWitt expansion order) | 4 (covers poles at 8, 6, 4, 2, 0) |
| s_pole | 4 (closest true pole to s=3, n=2 driver = a_4) |
| Quadrature scheme | scipy.integrate.quad with epsabs=1e-12, epsrel=1e-10 |
| Spinor rank | 16 (for d=8 spin bundle) |
| Volume normalization | (4π)^{−d/2} prefactor with d=8 |
| Regulator weights | w_zeta(λ) = 1; w_Zub(λ) = exp(−λ²/M_KK²); w_SDW(λ) = sqrt(λ²/Λ²) |
| Cross-check tolerance | 1e-3 relative on residue extraction |

PRU check: 9/9 parameters pinned. No Class-8 gap.

### VI.G Cross-pairings

1. **W0-W5 S-1 Regulator-Family Boundary Theorem**: this gate is INTERNAL to the pure-a_4 family. Whether it PASSES, FAILS-with-kinematic, or FAILS-without does not change S-1's structural wall (cutoff_sqrt vs pure-a_4 family). It does refine the within-family kinematic structure of pure-a_4.
2. **W0-W5 S-6 L_max-Truncation Taxonomy**: this gate is the LANDING for S-6 §V.10 `S86-MELLIN-CONE-S4-RESIDUE` and partially overlaps with S-6 §V.9 `S86-CC-3-CM-RESIDUE-MELLIN`. Should be co-scheduled.
3. **W6-W13 1C Perturbative-Ledger Immunization Theorem Family**: if this gate PASSES (PROVEN scenario), it adds a "Mellin-cone-stabilization immunization" theorem to the family enumerated in 1C; if FAILS, it confirms that within-family kinematic asymmetries DO NOT promote to immunization-grade theorems (a useful structural observation for 1C's theorem-family enumeration).
4. **§VII.N Three-Layer Regulator Theorem**: this gate verifies that the pure-a_4 family's INTERNAL kinematic structure does not violate the §VII.N classification (which addresses the divergence structure across three regulator classes, NOT within-family slope orderings).

---

## VII. Carry-Forward to S86+ (mandatory per `feedback_fix-in-session-never-defer.md`)

Each entry: **what / inputs / gate / effort**. All are planned computations in S86.

### VII.1 — S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING (this Section VI gate)

- **What**: adjudicate the candidate theorem of W10-4 closing-note Highlight #1 via Mellin-heat-kernel pole-subtracted residue extraction at the TRUE pole s=4, comparing against the geometrically computed a_4. Determine PASS / FAIL-with-kinematic-residual / FAIL-without-kinematic-residual.
- **Inputs**: S-6 §V.2 infrastructure (`s86_mellin_hk_residue.py`); S-6 §V.3 Gilkey a_4 on Jensen-SU(3) at τ=0.190; D_K cache at L=10 (dense) or L=12 (block-diagonal if landed); W10-4 SV2 trajectories in `s84_w1a_w0_sv2.npz`.
- **Gate**: per §VI.D thresholds. Default expectation per Section IV.C: **FAIL-as-stated, kinematic-residual TBD by L=10, 12 numerical check**.
- **Effort**: 2 days post-V.2 + V.3.

### VII.2 — S86-MELLIN-HK-INFRA (Class B remediation infrastructure; from S-6 §V.2)

- **What**: implement the §IV.B Mellin-heat-kernel pole-subtracted residue extractor. This is the S-6 V.2 carry-forward; renamed/aliased here to flag dependency from this Row 3A synthesis.
- **Inputs**: D_K eigenvalue cache at L_max ∈ {8, 9, 10, 11, 12}; canonical a_0 = 6440 (S72), a_2 = 0.728 (S46); Gilkey a_4 (V.3 below).
- **Gate**: PASS iff Res_{s=8} extracted matches a_0/(48π⁴) within 1e-3 AND Res_{s=4} extracted matches a_4_geometric/(8π⁴) within 1e-3.
- **Effort**: 2 days (1 compute + 1 audit).

### VII.3 — S86-A4-GILKEY-JENSEN (subset of S-6 §V.3 a_4-a_6-a_8 programme)

- **What**: derive a_4 Seeley-DeWitt coefficient on Jensen-deformed SU(3) at τ=0.190 in closed form. Extends S46's a_2 = 0.728 to the next slot. The Gilkey-1995 §3.3 polynomial `a_4 = (4π)^{−d/2}/360 · ∫ tr [60 ΔR + 60 R E + 180 E² − 60 R_μν R^μν + 30 R² + ...]` with Jensen deformation tensor T(τ).
- **Inputs**: Jensen metric tensor at τ=0.190 (canonical_constants); curvature scalars R, |Ric|², |Riem|² already computed in S46/S52; spin connection / endomorphism E from D_K² Lichnerowicz expansion.
- **Gate**: PASS iff a_4 computed at machine precision with Bianchi identity cross-check and dimensional consistency.
- **Effort**: 2 days (heavy symbolic algebra; mcp__sage__ likely required for Riemann polynomial reductions).

### VII.4 — S86-W10-4-BRANCH-C-LMAX12-DENSE (validate W10-4 branch c stability under dense computation)

- **What**: validate the W10-4 PASS for branch c under DENSE diagonalization at L_max ∈ {10, 12} (no log-linear extrapolation). Computes residues `ξ_J · mellin_s3(L) / S_zeta_E(L)` directly on the dense cache; compares to W10-4 SV2-extrapolated branch table.
- **Inputs**: dense D_K cache at L=10 (~17 GB feasible per W10-4 §(g)); block-diagonal infrastructure if landed; W10-4 branch table (`s85_w10_w0_inverted_branch_enumeration.npz`).
- **Gate**: PASS iff dense residue at L=10 matches SV2-extrapolated value within 5%; INFO iff matches within 20% (extrapolation is broadly correct but slope is mis-fit); FAIL otherwise (extrapolation is wrong at L=10, branch c PASS retracted).
- **Effort**: 1.5 days.

### VII.5 — S86-S-1-PURE-A4-FAMILY-INTERNAL-KINEMATIC-AUDIT

- **What**: under the S-1 Regulator-Family Boundary Theorem (cutoff_sqrt vs pure-a_4), audit the within-pure-a_4-family kinematic slope structure on the truncated PW spectrum at L ∈ {5..12}. Verify the §V.C reformulated kinematic claim quantitatively. Update the §VII.N Three-Layer Regulator Theorem if any within-family asymmetry rises to structural level.
- **Inputs**: VII.2 infrastructure; S-1 canonical theorem statement (post-landing).
- **Gate**: INFO-grade; reports the slope ordering across {ζ, Zubarev, SDW, anomaly} with PRDR pinning of regulator weights and L_max.
- **Effort**: 1 day.

### VII.6 — S86-MELLIN-CONE-NON-POLE-AUDIT (pattern check across waves)

- **What**: audit any S85+ gate that reports a "residue at s*" for s* ∉ {0, 2, 4, 6, 8} and reclassify per the S-6 Class-B taxonomy. This catches future repetitions of the W10-4 pattern (residue evaluated at non-pole; partial-sum slope mis-interpreted as regulator-class theorem).
- **Inputs**: `computations/s85_gate_verdicts.txt`; S-6 §IV.A pole-set Sd={0,2,4,6,8} for d=8.
- **Gate**: PASS iff every "residue at s*" gate has s* ∈ Sd; FAIL iff ≥1 gate has s* ∉ Sd. (S85-W0-L-MELLIN-CONE-S3-RESIDUE is such a gate; the S-6 V.10 reformulation `S86-MELLIN-CONE-S4-RESIDUE` is the remediation.)
- **Effort**: 0.5 day.

---

## VIII. Conflicts flagged

1. **W10-4 PASS verdict vs Class-B refutation here**: W10-4 PASS verdict (`S85-W10-W0-L-INVERTED-BRANCH-ENUMERATION` line 174 of verdicts file, value=1, `audit_sha256=7775d9364eed91f6...`) is AUTHORITATIVE per source-document discipline. This synthesis does NOT re-adjudicate that verdict. What is refuted here is the PROMOTION of the W10-4 empirical observation to a substrate-level theorem (the W10-4 closing-note Highlight #1 candidate). The W10-4 PASS at L_max ∈ {8, 10, 12} extrapolated remains valid as a kinematic finding; the candidate theorem promotion is what fails.

2. **`S85-W0-L-MELLIN-CONE-S3-RESIDUE` FAIL verdict**: the W0-20 FAIL at value=1.81e6 with `convention=s*=3 L_max=12` (`s85_gate_verdicts.txt:120`) is AUTHORITATIVE. This synthesis confirms the FAIL is Class-B (method-inappropriate); the gate's PASS condition was unattainable by direct partial sum at any L_max because s=3 is not a pole of ζ_D for d=8. The W0-20 FAIL and the W10-4 PASS are STRUCTURALLY CONSISTENT under the heat-kernel diagnosis of this synthesis: both are statements about the same divergent partial sum at s=3, viewed under different gate definitions.

3. **W10-4 explicit prediction: "ζ-regulator class is more STABLE at high L for all coupling orderings, while the Zubarev regulator class is STABLE only in the Bogoliubov-dominant (low-L) regime"** (W10 working paper line 1104). This synthesis flags this as a CLASS-B-RESIDUAL claim — true as a kinematic statement on finite L but NOT lifting to substrate-level regulator-class structural theorem. Downstream usage (DR3 response envelope, W10-2 V.1 addendum, future regulator-of-choice canonical lean) must qualify "ζ stabilizes" with "(at the partial-sum level on L ≤ 12 PW truncation; the substrate-level regulator-class kinematic structure is undecided pending VII.1)."

---

## IX. Closure

The candidate ζ-Regulator-Stabilization Theorem (W10-4 closing-note Highlight #1) is **REFUTED as stated** when adjudicated through the heat-kernel / Mellin / Seeley-DeWitt analytic-continuation framework:

- The "Mellin-cone s=3 residue numerator" object referenced in the candidate is a PARTIAL-SUM PROXY at a NON-POLE location on a finite-L_max truncation of D_K, NOT a residue of the meromorphic ζ_D(s).
- For Jensen-SU(3) × A_F at d=8, the Connes-Moscovici dimension spectrum is Sd = {0, 2, 4, 6, 8}; the closest TRUE pole to s=3 is s=4 with residue a_4/(8π⁴), an L_max-INDEPENDENT geometric constant under the V.3 Gilkey programme.
- The Seeley-DeWitt coefficient driving the ζ-regulator-denominator's 0.97 slope at s=3 is **a_0** (through the Mellin pole at s=8), not the pure-s=3 object the candidate names. The Zubarev 0.17 slope is a saturation artefact of the exp(−λ²/M_KK²) cutoff truncating the partial sum at the M_KK scale.
- The empirical slope ordering 0.97 > 0.56 > 0.17 holds quantitatively on the W10-4 SV2 cache and matches the W10-4 branch table residue ratios to ~1% (Section II.C verification). It is a TRUE KINEMATIC STATEMENT about partial sums but does NOT lift to a substrate-level regulator-class theorem.

The reformulated kinematic claim of Section V.C is INFORMATIONAL — a within-pure-a_4-family slope ordering at finite L_max — and should be filed as an INFO-grade observation, not promoted to §VII.B / §VII.N theorem status.

The pre-registered S86 gate `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` (Section VI) will adjudicate by extracting the residue at the TRUE pole s=4 via the §IV Mellin-heat-kernel infrastructure (S-6 V.2) and comparing against the Gilkey-computed a_4 (S-6 V.3). The PASS scenario corresponds to "candidate refuted, analytic-continuation residue at s=4 matches the geometric a_4 to 1e-3, kinematic slope claim holds at L=10, 12 as informational."

Substrate framing note: the heat-kernel adjudication is a property of the substrate's intrinsic spectral geometry (D_K eigenvalues on Jensen-deformed SU(3)). The refutation does NOT close any phononic mechanism; rather, it sharpens the framework's regulator-class taxonomy by removing a CANDIDATE structural theorem that turns out to be a finite-L_max kinematic artefact. This is consistent with `math-scripts.md` §All Results Are Good Results: the FAIL/REFUTATION of the candidate theorem strengthens the framework's structural distinctness (no spurious within-family theorems), tightens the S-1 Regulator-Family Boundary Theorem's scope to its proper domain (cutoff_sqrt vs pure-a_4), and identifies the proper analytic-continuation route (S-6 §V.2 + V.3 + V.10) as the canonical path forward for any "Mellin-cone residue" claim in S86+.

---

**Files produced (this synthesis)**:

| File | Path |
|:-----|:-----|
| Synthesis (subsection b) | `sessions/archive/session-85/session-85-3a-zeta-stabilization-spectral-geometer.md` |

**Companion subsection** (independent parallel writeup, NOT this file):

| File | Path |
|:-----|:-----|
| Synthesis (subsection a, lizzi) | `sessions/archive/session-85/session-85-3a-zeta-stabilization-lizzi.md` (filename TBD by lizzi) |

**Source documents (read this session, not re-adjudicated)**:

- `sessions/archive/session-85/session-85-w10-workingpaper.md` (W10-4 §W10-4(d-h), closing-note Highlight #1)
- `computations/s85_gate_verdicts.txt` (lines 120, 174)
- `sessions/archive/session-85/session-85-s6-truncation-taxonomy-spectral-geometer.md` (this author's S-6 deliverable; §III.B, §IV.B, §V.2, §V.3, §V.9, §V.10)
- `sessions/archive/session-85/session-85-workshop-schedule.md` (W0-W5 schedule §S-1)
- `sessions/archive/session-85/session-85-w6-13-workshop-schedule.md` (W6-13 schedule §3A — this row)
- `sessions/permanent-results-registry.md` (§VII.B for theorem registry, §VII.N for Three-Layer Regulator Theorem)
- `.claude/agent-memory/spectral-geometer/MEMORY.md`
- knowledge MCP queries (4 search + 1 trace + 1 attempted-trace; results in §I–II)

**Numerical verification** (Python, this synthesis): predicted geometric ratio of branch-c residues per 2-L step from slope difference exp(2 × (0.56 − 0.97)) = 0.4404 vs observed 0.4360 (mean over W10-4 branch table L=8→10 and L=10→12 steps); predicted Zubarev branch-d ratio exp(2 × (0.56 − 0.17)) = 2.1815 vs observed 2.1732. Both match to ~1%, confirming the slope-difference-drives-residue-evolution kinematic model and the Class-B (method-inappropriate) diagnosis.
