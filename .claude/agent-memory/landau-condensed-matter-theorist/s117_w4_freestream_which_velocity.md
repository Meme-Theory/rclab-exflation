---
name: s117-w4-freestream-which-velocity
description: Symmetry-first structure for DM free-streaming coldness — parity selection rule on the squeeze occupation (T^{0i}=0) + the which-velocity category distinction (bulk-current vs internal-occupation-variance). Reusable for any warm-DM / free-streaming gate.
metadata:
  type: project
---

S117 W4-1 (CF-S117-FREESTREAM-AT-ANCHOR, PASS) established a **reusable symmetry-first
template** for DM free-streaming coldness in this framework. The structure (not the
numbers — those live in the verdict file + knowledge.db) is the durable content:

**The warmness order parameter vanishes by a parity selection rule.** The "warmness" of a
relic is the bulk 4-momentum current `T^{0i} = ∫ k n(k) d³k`. The GGE transit creates
quasiparticles in (k, −k) squeeze pairs ⇒ the frozen occupation `n(k)=n(−k)` is EVEN ⇒
the momentum-density integrand `k·n(k)` is ODD ⇒ `T^{0i}=0` EXACTLY by parity. This is the
substrate-level content of CDM-CONSTRUCT-44 (5 proofs, S44). Coldness is a **symmetry
certainty** (w=0, dust), not a small-thermal-velocity accident. This is the Landau move:
the symmetry classification of the creation process settles the question before any detailed
dynamics. `v_fs^4D = T^{0i}/T^{00} = 0 ⇒ λ_fs^4D = 0`.

**The which-velocity category distinction (load-bearing guard).** Two ORTHOGONAL velocity
observables must never be conflated:
- `v_fs^4D` = bulk current / energy density (a COLLECTIVE observable) → 0 by parity.
- `v_rms_internal` = variance of the single-mode occupation (a FIBER-SPECTRUM observable) → finite.
A relic can have zero bulk velocity AND a large internal momentum spread. Reading the
internal spread AS the 4D free-streaming velocity is the IS-not-IN container error
([[s84-w5-66-landau-symmetry-class]] / phononic-framing). This reproduces the S42 history:
S42's "89 Mpc (HDM)" was the internal-spread-as-velocity reading, SUPERSEDED by
CDM-CONSTRUCT-44 (T^{0i}=0 ⇒ CDM reading λ_fs→0 is correct).

**Why the algebraic reading MUST be load-bearing (a numerical signature).** The naive
non-relativistic internal velocity `√⟨(k/m)²⟩` is UV-sensitive (numerator cutoff-linear
for an occupation falling as k⁻⁴) — at the anchored mass it computes to 2.48 > c, an
unphysical "velocity." The physically-bounded reading `√⟨v_g²⟩ = √⟨k²/(k²+m²)⟩ ≤ c`
converges (0.733c here). The ill-definedness of the (k/m) 2nd moment is itself the evidence
that the symmetry/algebraic Track A, not a moment integral, carries the coldness verdict.
GENERAL LESSON: when asked for a relativistic relic's "velocity dispersion," use the bounded
group-velocity moment `⟨k²/(k²+m²)⟩`, never the NR `⟨(k/m)²⟩` (the latter is a category-error
trap that downstream container-thinking will mis-read as warmth).

**z_tr metric (FREE-STREAMING-58) is mass-robust.** At fixed production velocity the s58
z_tr depends on v_prod (=c_Gold), not m; the dominant factor is the GUT-scale production
redshift z_prod~1e29, so z_tr ≫ z_threshold for ANY v∈[0.1,0.999] (22 OOM). A heavier mass
at fixed PRODUCTION MOMENTUM is LESS relativistic ⇒ even colder. Frozen occupation built
closed-form from BdG dispersion + canonical squeeze (r_squeeze=arctanh√n_Bog, n_peak=(W_BG−1)/2
— both DERIVED from canonical n_Bog/W_BG, never hardcoded).

Scope guard: this gate is KINEMATIC only — it does NOT touch relic SURVIVAL (Reading A:
CPT + GGE integrability S_ent=0 + Γ_grav<H_0, atlas-04 C11-conditional). Survival ⊥
free-streaming coldness ⊥ Leggett-mode sharpness (the W-2 workshop two-observable separation).
See [[s116-w2-leggett-dm-edge-survival]].
