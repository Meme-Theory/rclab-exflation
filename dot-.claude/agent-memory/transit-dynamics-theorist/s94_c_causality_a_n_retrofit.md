---
name: s94-c-causality-a-n-retrofit
description: S94 W6-21 — Phononic-C-Causality.md a_n regulator-pin retrofit; all 193 bare a_n are zeta-scheme Seeley-DeWitt; audit-script REPO_ROOT bug
metadata:
  type: project
---

# S94-A_N-RETROFIT-C-CAUSALITY (W6-21) — doc fully regulator-pin-compliant

**Result**: `sessions/framework/Phononic-C-Causality.md` (the C-Causality doc I author) now satisfies `regulator-pin-discipline.md` forward-looking. All 193 retained-prose bare `a_n` retrofitted with `^{zeta}` tags; `_a_n_regulator_pin_audit.py --target <doc>` returns `n_untagged_seeley_dewitt = 0`. Verdict PASS (audit `aa04474568d9...` inaugural; `9af1d930...` corrective).

**Why:** discharges the grandfathered-legacy regulator-pin gap that made the prior WX-W4-3-RECONCILE-VERIFY-C-CAUSALITY close INFO (`bare_retained=193_GRANDFATHERED`).

**How to apply (future doc-retrofit gates + any consumer of a_n from this doc):**

- **Every bare a_n in C-Causality is a Chamseddine-Connes Seeley-DeWitt moment** — ZERO non-Seeley-DeWitt (no lattice spacings / plain vars / string literals / generic indices). Breakdown: 115 `a_2` + 58 `a_0` + 20 `a_4` = 193. Semantics: a_0 = zeroth moment (volume/vacuum/cosmological term), a_2 = second moment (Einstein-Hilbert; `M_Pl_eff^2 = a_2/(48 pi^2) = 5.862 M_KK^2`; Newton's constant), a_4 = fourth moment (Yang-Mills + Higgs quartic).
- **Regulator = zeta, doc-self-declared at line 138**: "The Seeley-DeWitt coefficients cited throughout this document are in the zeta-function regularization scheme." This + the 11 pre-existing `^{zeta}` tags fix `^{zeta}` as the default for every citation. The decoupling theorem is regulator-INVARIANT at the polynomial-degree level (Gilkey orthogonality), but the NUMERICAL values (a2_fold=2776.165..., a4_fold=1350.722...) are zeta-scheme half-zeta_D(1)/(2).
- **`a_2^bos`/`a_2^Dirac` are NOT regulator tags** — they are boson-vs-Dirac contribution labels (ratio 61/20, S44). Already non-bare; the `(?!\^)` guard leaves them untouched. Do not "fix" them with a regulator tag.
- **Generic-family `a_n` (literal letter n)** — e.g. eq 3.1 `f_n Lambda^{d-2n} a_n`, "the a_n Seeley-DeWitt coefficients" — is NOT matched by the audit regex `\ba_(\d+)\b` (needs a DIGIT). Out of scope; leave as-is.

**Tag form**: `^{zeta}` (ASCII, matching the doc's established 11 tags) — NOT the `^{ζ}` unicode glyph; keep one in-doc convention.

## Audit-script latent bug fixed (load-bearing for future .md scans)

`computations/_shared/_a_n_regulator_pin_audit.py`: `PROJECT_ROOT = Path(__file__).resolve().parent.parent` = **`computations/`**, NOT the repo root. So the legacy `TARGET_DIRS=["computations",...]` glob resolved to `computations/computations/**` (empty) — the audit was effectively scanning nothing under that doubled path. Added `REPO_ROOT = PROJECT_ROOT.parent` and made `MD_TARGETS` (the C-Causality doc) + the new `--target <path>` flag resolve repo-root-relative; `audit_file()` now relativizes against REPO_ROOT with a fallback. JSON gained `n_untagged_seeley_dewitt` alias + `target` key. If extending the audit to other framework `.md` docs, add them to `MD_TARGETS` (repo-root-relative).

## Verdict-emission lesson (re-run robustness)

Initial verdict logic gated on `pre_tagged_total == 11` (the inaugural-only invariant) → a FALSE FAIL on idempotent re-run (doc already retrofitted → tagged=204). Fixed: PASS iff `n_untagged==0 AND tagged_total>=11 AND post_tagged==pre_tagged+pre_bare`. Added `--no-emit` (re-verify without appending) and `--supersede <sha>` (Option-A corrective per `gate-verdicts.md`). The spurious FAIL was retired via a supersedes-tagged corrective PASS; canonical reading (supersession-aware `_consolidate_intake.extract_supersedes_pointers`) = PASS. Lesson: METHODOLOGY-class retrofit verdicts must key on the artifact END-STATE, not on whether THIS run did the mutation.
