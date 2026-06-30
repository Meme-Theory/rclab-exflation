#!/usr/bin/env python3
"""
S103 W1-2 — S103-LAMBDA2-MONOTONICITY-REGISTRY-LANDING — §VII.BW λ²-moment monotonicity
========================================================================================

Gate: S103-LAMBDA2-MONOTONICITY-REGISTRY-LANDING ([AUDIT])

Pre-registered threshold (artifact-existence + content-marker; NO numerical threshold):
  PASS iff (§VII.BW section body present in permanent-results-registry.md)
        AND (theorem statement with closed form dM₂/dτ = d·[C₂·gC + gS] present)
        AND ('Schur lemma' / 'Schur corollary' framing for equipartition step (ii) present)
        AND (|λ|-action f=√x SIGN-corollary anchor re-scope present: 58672.8 = |λ|-action
             gradient; 213991.8 = λ²-moment gradient)
        AND (STAGE-1-CANDIDATE tag present)
        AND (5-anatomy / 3-level N/A-with-reason present)
        AND (slot-index TABLE row `| §VII.BW | THM | ... |` present, adjacent to the BV row)
        AND verify_section_matches(actual, expected) == True
  FAIL iff verify_section_matches == False (assembly bug / slot collision; AFTER-pattern emits
       FAIL once, NO in-script corrective rewrite — remediation escalates to S104).
  INFO iff next-free-letter scan finds §VII.BW occupied at runtime → reroute with
       FAIL-with-remediation (audit-trail visibility), then the rerouted slot lands.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-102/s102_trd2_monotonicity_analytic.npz  (proof certificate; all numbers)
  - sessions/permanent-results-registry.md                        (registry pre-write file SHA)
  - canonical_constants.py (feeds audit_sha256 only; carries dS_fold = 58672.80241318)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<verify bool + landed letter>,
   scheme=REGISTRY-LANDING-AFTER-PATTERN,
   convention=INTRA-PILLAR-STRUCTURAL-THEOREM-STAGE-1-CANDIDATE-5ANATOMY-3LEVEL-NA-WITH-REASON;
              SCHUR-COROLLARY-EQUIPARTITION;LAMBDA-ACTION-SQRT-X-SIGN-COROLLARY-ANCHOR,
   L_max=L-uniform)

Classification: GEOMETRIC (λ²-moment monotonicity on the Jensen-deformed spectral triple — the FABRIC).

METHODOLOGY
-----------
Single-shot AFTER-pattern bridge-landing per `registry-landing.md` §"Bridge-Landing Script
Architecture": build_promotion_text builds the FULL §VII.BW body in memory; write_atomic_with_fsync
writes BOTH (a) the section body at the runtime next-free §VII letter (over ALL header levels
## / ### / ####) AND (b) a matching slot-index TABLE row adjacent to the §VII.BV row;
re_read + verify_section_matches yields a single boolean over BOTH; exactly ONE emit_verdict
payload is printed for the agent. The §VII.BW theorem REGISTERS the proven λ²-moment monotonicity
closed form M₂(p,q;τ) with dM₂/dτ = d·[C₂·gC + gS], (u−1)-factorized with strictly-positive
cofactors, L-uniform and strict for τ>0. The proof is derived UPSTREAM (W3-14 closed form +
S-2 proof-check synthesis, PASS); this gate TRANSCRIBES it — re-derives NOTHING (binding-text
discipline). It applies the TWO MINOR S-2 proof-check remediations:
  (i)  the equipartition step S_su2:S_c2:S_u1 = 3:4:1 is a SCHUR-LEMMA COROLLARY (the rep-trace
       form Tr(ρ(X_b)ρ(X_d)) is the unique ad-invariant symmetric form up to scale on simple
       su(3) ⇒ ∝ Killing form ⇒ block sums 3:4:1 for EVERY (p,q)), NOT a numerically-certified fit;
  (ii) the +58672.8 spectral-action gradient is the |λ|-action (f=√x) SIGN-corollary of E7's
       "S_f monotone for ALL monotone f," distinct from the λ²-MOMENT gradient dS₂/dτ = 213991.8;
       the previously-cited "ratio 2.647" conflated the two functionals — a functional-label
       mismatch; BOTH gradients are positive (E7), so the dS/dτ>0 SIGN-corollary is unchanged.

PLAN-TEXT-DRIFT DISCLOSURE (substrate-first-canonical-sourcing.md §(ii.B))
--------------------------------------------------------------------------
The proof certificate npz stores the cofactor arrays as INTEGER-SCALED / DESCENDING-POWER forms
  cofactor_gC = [12, 12, 12, 4]   cofactor_gS = [10, 10, 10, 6, 2, 2]
whereas the plan hypothesis + S-2 synthesis quote the HUMAN-READABLE POLYNOMIAL-COEFFICIENT forms
  gC = [4/3, 4, 4, 4]  (the constant 4/3 = constant term of 4u³+4u²+4u+4/3)
  gS = [2, 2, 6, 10, 10, 10]  (ascending-power coefficients of 10u⁵+10u⁴+10u³+6u²+2u+2)
These are mathematically equivalent representations of the SAME cofactor polynomials (the npz form
clears the 4/3 rational by ×3 and lists in descending power order). The registry text cites BOTH:
the synthesis polynomial form (4u³+4u²+4u+4/3 / 10u⁵+10u⁴+10u³+6u²+2u+2) is the AUTHORITATIVE
human-readable form per the proof; the npz arrays are the byte-level ground truth (consumed for the
all_positive / remainder=0 / sign_match flags). The drift is representation-only; the substantive
PASS conditions (cofactor_gC_all_positive, cofactor_gS_all_positive, factor_remainder=0,
min_dM2_dtau_over_domain>0, sign_match) hold IDENTICALLY in both forms.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No linear algebra (string assembly + SHA + file I/O only); CPU path, OMP cap.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- regulator_pin=a_2^{ζ} carried as an emit_verdict extra-row (regulator-pin-discipline.md)
- Verdict emitted via emit_verdict MCP tool (script PRINTS payload; agent calls the tool).
  Script does NOT write the verdict file (Windows cross-process O_APPEND race).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import dS_fold, S_fold, tau_fold  # explicit (provenance pins)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent                 # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent                          # computations
PROJECT_ROOT = COMPUTATIONS_DIR.parent                        # project root
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-103"            # per-session outputs land here

SESSION = "S103"                                              # (local)
GATE_ID = "S103-LAMBDA2-MONOTONICITY-REGISTRY-LANDING"        # (local)
SCHEME = "REGISTRY-LANDING-AFTER-PATTERN"                     # (local)
CONVENTION = ("INTRA-PILLAR-STRUCTURAL-THEOREM-STAGE-1-CANDIDATE-5ANATOMY-3LEVEL-NA-WITH-REASON;"
              "SCHUR-COROLLARY-EQUIPARTITION;"
              "LAMBDA-ACTION-SQRT-X-SIGN-COROLLARY-ANCHOR")   # (local)
L_MAX = "L-uniform"                                           # (local) closed form is L-independent

PLAN_FREEZE_LETTER = "BW"                                     # (local) plan-freeze prediction
PLAN_FRONTIER_LETTER = "BV"                                   # (local) documented highest prior §VII letter (this session, W1-1)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"   # (local)
WITNESS_NPZ = COMPUTATIONS_DIR / "session-102" / "s102_trd2_monotonicity_analytic.npz"  # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"        # (local)

OUT_NPZ = SESSION_OUT_DIR / "s103_lambda2_monotonicity_registry_landing.npz"   # (local)

# slot-index TABLE anchor: the §VII.BV row (frontier) — we insert the §VII.BW row right after it.
BV_TABLE_ROW_PREFIX = "| §VII.BV | THM |"                     # (local)

INPUT_FILES = [
    CANONICAL_PATH,
    WITNESS_NPZ,
    REGISTRY_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str],
                     registry_pre_sha: str, promotion_span_sha: str) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json || registry_pre_sha || promo_span_sha);
    content = sha256(script).  (Per plan audit_sha256_inputs:
    [script, npz, registry_pre_write_file_sha, promotion_text_span_sha, pinmap].)"""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(f"registry_pre_sha={registry_pre_sha}\n".encode("utf-8"))
    h_audit.update(f"promotion_span_sha={promotion_span_sha}\n".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4b — Next-free §VII letter scan (ALL header levels)
# ---------------------------------------------------------------------------

def _letter_to_int(letters: str) -> int:
    """Bijective base-26: A=1 .. Z=26, AA=27, ... BV=74, BW=75, etc."""
    n = 0  # (local)
    for ch in letters:
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n


def _int_to_letter(n: int) -> str:
    """Bijective base-26 inverse: 1->A, 26->Z, 27->AA, 75->BW, ..."""
    out = ""  # (local)
    while n > 0:
        n, rem = divmod(n - 1, 26)
        out = chr(ord("A") + rem) + out
    return out


def occupied_vii_letters(registry_text: str) -> set[str]:
    """Set of letter-runs occupied by ## / ### / #### §VII.<LETTERS> SECTION HEADERS
    (line-start anchored). Prose mentions of `§VII.XXX` mid-line are NOT section anchors.
    The captured group stops at the first `.`/space so sub-section suffixes (`.OP-PROJ`,
    `.U.2`) collapse onto their parent letter."""
    hits = re.findall(r"^#{2,4} §VII\.([A-Z]+)(?:[.\s]|$)", registry_text,
                      re.MULTILINE)  # (local)
    return set(hits)


def next_free_vii_letter(registry_text: str, frontier: str = "BV") -> str:
    """Smallest UNOCCUPIED letter in the canonical A,B,...,Z,AA,AB,... stream strictly after
    `frontier`. Walks the sequence upward from the documented dense frontier (W1-1 landed
    §VII.BV this session) and returns the first slot not already a section header — treating
    any off-sequence legacy/semantic anchors (`§VII.PROP`, `§VII.AAU`) as OCCUPIED so they
    are never re-allocated, while NOT letting their large base-26 value inflate the frontier
    (the W1-1 letter-scan lesson). Robust across the Z->AA and BZ->CA rollovers."""
    occupied = occupied_vii_letters(registry_text)  # (local)
    n = _letter_to_int(frontier) + 1  # (local) start one past the frontier
    while True:
        cand = _int_to_letter(n)  # (local)
        if cand not in occupied:
            return cand
        n += 1


def section_header_present(registry_text: str, letter: str) -> bool:
    pat = re.compile(rf"^#{{2,4}} §VII\.{re.escape(letter)}\b", re.MULTILINE)  # (local)
    return bool(pat.search(registry_text))


def table_row_present(registry_text: str, letter: str) -> bool:
    """True iff a slot-index TABLE row `| §VII.<letter> | THM |` exists (line-anchored)."""
    pat = re.compile(rf"^\| §VII\.{re.escape(letter)} \| THM \|", re.MULTILINE)  # (local)
    return bool(pat.search(registry_text))


# ---------------------------------------------------------------------------
# Section 5 — Witness numbers (consume the s102 proof certificate; re-derive NOTHING)
# ---------------------------------------------------------------------------

def load_witness() -> dict:
    """Load the pre-computed λ²-monotonicity proof certificate; NO recomputation."""
    d = np.load(WITNESS_NPZ, allow_pickle=True)  # (local)
    return {
        # cofactor arrays — npz integer-scaled / descending-power storage form
        "cofactor_gC_npz": d["cofactor_gC"].astype(int).tolist(),     # [12,12,12,4]
        "cofactor_gS_npz": d["cofactor_gS"].astype(int).tolist(),     # [10,10,10,6,2,2]
        "cofactor_gC_all_positive": bool(d["cofactor_gC_all_positive"]),
        "cofactor_gS_all_positive": bool(d["cofactor_gS_all_positive"]),
        "factor_remainder_gC": int(d["factor_remainder_gC"]),
        "factor_remainder_gS": int(d["factor_remainder_gS"]),
        # strict-positivity of the derivative over the physical domain
        "min_dM2_dtau_over_domain": float(d["min_dM2_dtau_over_domain"]),
        "argmin_dM2": d["argmin_dM2"].astype(float).tolist(),
        "dM2_dtau_at_tau0_maxabs": float(d["dM2_dtau_at_tau0_maxabs"]),
        # equipartition Schur-witness (float floor of an exact Schur identity)
        "max_equipartition_deviation": float(d["max_equipartition_deviation"]),
        # closed-form cross-check residuals
        "max_rel_M2": float(d["max_rel_M2"]),
        "max_rel_TrOmega2": float(d["max_rel_TrOmega2"]),
        "max_rel_dM2": float(d["max_rel_dM2"]),
        # the TWO functional gradients (the anchor re-scope (ii))
        "dS_fold_canonical": float(d["dS_fold_canonical"]),                 # |λ|-action grad, 58672.8 anchor
        "dS_full_dtau_reproduced": float(d["dS_full_dtau_reproduced"]),     # |λ|-action grad reproduced
        "anchor_repro_rel_err": float(d["anchor_repro_rel_err"]),
        "dS2_lambda2_action_grad_analytic": float(d["dS2_lambda2_action_grad_analytic"]),  # λ²-grad, 213991.8
        "literal_xcheck_ratio": float(d["literal_xcheck_ratio"]),
        "literal_xcheck_pass": bool(d["literal_xcheck_pass"]),
        # sign / verdict tuple of the proof certificate
        "sign_match": bool(d["sign_match"]),
        "sign_verdict": str(d["sign_verdict"]),
        "magnitude_verdict": str(d["magnitude_verdict"]),
        "regime_verdict": str(d["regime_verdict"]),
        "composite": str(d["composite"]),
        "tau_fold_npz": float(d["tau_fold"]),
        "tau_NEC": float(d["tau_NEC"]),
        "witness_audit_sha256": str(d["audit_sha256"]),
        "witness_content_sha256": str(d["content_sha256"]),
    }


# ---------------------------------------------------------------------------
# Section 6 — Build promotion text (FULL §VII.BW body in memory)
# ---------------------------------------------------------------------------

def build_promotion_text(letter: str, w: dict, registry_pre_sha: str,
                         witness_npz_sha: str) -> str:
    """Return the FULL §VII.<letter> section body (pure function; no I/O)."""
    minv = w["min_dM2_dtau_over_domain"]  # (local)
    am = w["argmin_dM2"]  # (local) [p, q, tau] at argmin
    dS_grad = w["dS_fold_canonical"]  # (local) 58672.8 |λ|-action gradient
    dS2_grad = w["dS2_lambda2_action_grad_analytic"]  # (local) 213991.8 λ²-moment gradient
    lit_ratio = w["literal_xcheck_ratio"]  # (local) 2.647 the conflation artifact
    raw_ratio = dS2_grad / dS_grad  # (local) 3.647 = 213991.8/58672.8
    eqdev = w["max_equipartition_deviation"]  # (local)
    gC_npz = w["cofactor_gC_npz"]  # (local)
    gS_npz = w["cofactor_gS_npz"]  # (local)
    wsha = w["witness_audit_sha256"]  # (local)

    body = f"""### §VII.{letter} — λ²-Moment Monotonicity Closed Form on the Jensen-Deformed Spectral Triple: dM₂/dτ = d·[C₂·gC(τ) + gS(τ)] is Strictly Positive for τ>0, L-Uniform (STAGE-1-CANDIDATE intra-pillar structural theorem — the exflationary spectral-complexification gradient ⟨λ²⟩(τ) increases monotonically off the cold bi-invariant point; transcribed from the S102 W3-14 closed-form derivation + S102 connes-NCG λ² proof-check synthesis [S-2: VERDICT PASS, MINOR-only]; substrate-physics derivation lineage connes-ncg-theorist [NCG-axiomatic Schur-lemma equipartition] + the E7 Structural Monotonicity class [atlas-07 W7]; S103 W1-2 landing — gen-physicist orchestrator-direct registry §VII sole-writer for this NCG/geometric structural landing per `feedback_mack-bridge-role.md` [NOT a §7 falsifier-surface row — mack-cosmic-bridge does NOT apply]; single-shot AFTER-pattern per `registry-landing.md` §"Bridge-Landing Script Architecture"; slot §VII.{letter} runtime-verified next-free over ALL header levels [highest prior §VII.BV]; 2026-06-10)

**Status**: **STAGE-1-CANDIDATE** intra-pillar structural theorem per `joint-theorem-promotion.md` §"Stage 1". The closed form is analytically PROVEN UPSTREAM (S102 W3-14 + the S-2 proof-check synthesis, overall verdict **PASS**, severity MINOR-only: the only correction is a registry-text WORDING upgrade, not a blocker). This gate REGISTERS that proven result as a candidate row and APPLIES the two MINOR S-2 remediations: (i) the equipartition step is framed as a **Schur-lemma corollary** (representation theory), NOT a numerically-certified fit; (ii) the +58672.8 spectral-action gradient is re-scoped as the **|λ|-action (f=√x) SIGN-corollary** of E7, distinct from the λ²-moment gradient 213991.8. NO new compute gate: the proof certificate `s102_trd2_monotonicity_analytic.npz` is pre-computed and the numbers are transcribed VERBATIM (binding-text discipline; re-derives NOTHING). This is a SINGLE-AXIS GEOMETRIC structural theorem (NOT a joint cross-axis theorem requiring a Stage-2 cross-axis PASS-AND); STAGE-1-CANDIDATE is the landing grade, with STAGE-3 eligibility a future single-axis verify (the conclusion is an exact representation-theoretic + (u−1)-factorization identity, not a near-tolerance numerical coincidence).

**Result classification**: **GEOMETRIC** (a statement about the internal fabric — the second spectral moment ⟨λ²⟩ of the Dirac operator `D_K` on Jensen-deformed SU(3) and its τ-derivative — NOT its excitations). `M₂(p,q;τ)` is the `a_2^{{ζ}}` zeta-regulated Seeley-DeWitt ingredient (the second spectral moment → the induced Einstein-Hilbert kinematic skeleton); its strictly-positive τ-derivative IS the substrate's exflationary complexification driver (internal spectral complexification, NOT metric expansion).

**Classification (load-bearing for plan-freeze audit)**: this is an **INTRA-PILLAR STRUCTURAL THEOREM** on the spectral-triple axis (the substrate's own deformation flow). It is NOT a cross-pillar convergence bridge: the 5-anatomy IS-not-IN elements + the 3-level ladder are declared **N/A-with-reason** (there is no laboratory-IN continuum-image observable and no HKR / K-theory / Connes–Karoubi bridge map is claimed; the monotonicity is intrinsic to `(A_K, H_K, D_K(τ))`). A plan-freeze auditor MUST read it as an intra-pillar structural theorem with the §VII.BM/§VII.BV N/A-with-reason structure, NOT as a convergence bridge (which would HARD-HALT on a non-binding Level-2 per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`).

**Regulator pin**: `a_2^{{ζ}}` (zeta-regulated Seeley-DeWitt second moment) per `regulator-pin-discipline.md`. The λ²-moment `M₂ = ⟨λ²⟩ = Σ_k m_k λ_k²`-class trace is the zeta-regulated `a_2` ingredient (via the monotone-`f` inheritance: `a_2^{{ζ}}` is the `f(x)=x` member of the E7 all-monotone-`f` family on the dimension-spectrum residue).

**STRUCTURAL VERDICT (the λ²-moment monotonicity closed form)**: Let `(A_K, H_K, D_K(τ))`, `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`, be the Jensen-deformed spectral triple, and for each Peter-Weyl sector `(p,q)` (degeneracy `d = d(p,q) > 0`, quadratic Casimir `C₂ = C₂(p,q) ≥ 0`) let `M₂(p,q;τ) := ⟨λ²⟩` be the zeta-regulated second spectral moment. With `u := e^τ`, the closed form is

```
M₂(p,q;τ) = (2/3)·C₂·d·(3e^{{2τ}} + 4e^{{−τ}} + e^{{−2τ}}) + d·(5e^{{2τ}} + 4e^{{−τ}} + 2e^{{−2τ}} + ½e^{{−4τ}} + ½)
dM₂/dτ   = d·[ C₂·gC(τ) + gS(τ) ]
```

where the deformation cofactors factor through `(u−1)` with **strictly-positive** coefficient polynomials:

```
gC(τ)·e^{{2τ}} = (u−1)·(4u³ + 4u² + 4u + 4/3)                         [polynomial cofactor: 4,4,4,4/3]
gS(τ)·e^{{4τ}} = (u−1)·(10u⁵ + 10u⁴ + 10u³ + 6u² + 2u + 2)            [polynomial cofactor: 10,10,10,6,2,2]
```

Every coefficient in both cofactor polynomials is `> 0` (including the constant terms `4/3 > 0`, `2 > 0`), and the factorization remainder at `(u−1)` is **0** EXACTLY (Sage QQ; npz `factor_remainder_gC = {w['factor_remainder_gC']}`, `factor_remainder_gS = {w['factor_remainder_gS']}`; `cofactor_gC_all_positive = {w['cofactor_gC_all_positive']}`, `cofactor_gS_all_positive = {w['cofactor_gS_all_positive']}`). For `u > 1` (i.e. `τ > 0`): `gC, gS = (u−1)·(positive) > 0`, **zero iff u = 1 (τ = 0)**. Since `C₂(p,q) ≥ 0` and `d(p,q) > 0`, **`dM₂/dτ = d·[C₂·gC + gS] > 0` strictly for every τ > 0, every sector (p,q), L-UNIFORMLY** (the positivity is term-by-term, hence independent of the truncation `L_max`). The minimum of `dM₂/dτ` over the scanned physical domain is `min_dM2_dtau_over_domain = {minv:.9f} > 0` (at `[p,q,τ] = {am}`), and `sign_match = {w['sign_match']}`. ∎ (proven UPSTREAM at S102 W3-14 + S-2 proof-check; this entry TRANSCRIBES the chain.)

**MINOR remediation (i) — Schur-lemma equipartition (NOT a numerically-certified fit)**: the load-bearing equipartition relation `S_su2 : S_c2 : S_u1 = 3 : 4 : 1` (the per-block trace split = block dimensions) is a **Schur-lemma COROLLARY**, derivable SYMBOLICALLY for every irrep — NOT a fit that might break at higher `(p,q)`. The rep-trace form `B^ρ_{{bd}} := Tr(ρ(X_b)ρ(X_d))` is an `su(3)`-invariant symmetric bilinear form on the Lie algebra; `su(3)` is SIMPLE ⇒ the space of `ad`-invariant symmetric forms is ONE-DIMENSIONAL (the Dynkin-index fact) ⇒ `B^ρ ∝ Killing form` ⇒ isotropic in the Gell-Mann basis ⇒ the per-subalgebra block sums are `3:4:1 = dim(su(2)) : dim(su(2)_c) : dim(u(1))` EXACTLY for every `(p,q)`. The npz `max_equipartition_deviation = {eqdev:.3e}` is the FLOAT SHADOW of this exact Schur identity (not the certifier): the WP's prior "NUMERICALLY-CERTIFIED FIT" label UNDERSTATED the result; the Schur derivation closes it for general `(p,q)` and is reusable for higher moments `M₄, M₆`. (S-2 proof-check synthesis §1; Schur's lemma is a PROVEN pure-math result in the framework — knowledge-MCP theorem set.)

**MINOR remediation (ii) — |λ|-action (f=√x) SIGN-corollary anchor re-scope (functional-label disambiguation)**: the spectral-action gradient `dS/dτ = +58672.8` (canonical_constants `dS_fold = {dS_fold:.8f}`, `S_fold = {S_fold:.8f}`, S42 `s42_gradient_stiffness`; npz `dS_fold_canonical = {dS_grad:.5f}`, `dS_full_dtau_reproduced = {w['dS_full_dtau_reproduced']:.5f}`, `anchor_repro_rel_err = {w['anchor_repro_rel_err']:.3e}` at float floor) is computed with the **f = √x (|λ|-action) cutoff** — it is the **SIGN-corollary `dS_{{|λ|}}/dτ > 0`** of E7's "`S_f` monotone for ALL monotone `f`," NOT a magnitude target for the λ²-proof. The **λ²-MOMENT gradient is a DIFFERENT functional**: `dS₂/dτ = {dS2_grad:.5f}` (npz `dS2_lambda2_action_grad_analytic`). The previously-cited "ratio 2.647" (npz `literal_xcheck_ratio = {lit_ratio:.6f}`; the raw gradient ratio `{dS2_grad:.1f}/{dS_grad:.1f} = {raw_ratio:.6f}`, minus 1) CONFLATED the |λ|-action gradient with the λ²-moment gradient — a **functional-label mismatch**, NOT a substrate inconsistency. BOTH functionals are strictly increasing (E7 all-monotone-`f`), so the `dS/dτ > 0` SIGN-corollary direction is UNCHANGED under either functional; the `literal_xcheck_pass = {w['literal_xcheck_pass']}` records only that the |λ|-action gradient ≠ the λ²-gradient (they are different functionals), NOT a failed monotonicity claim.

**Substitution chain (transcribed sign argument — no re-derivation; witness numbers from `s102_trd2_monotonicity_analytic.npz`, audit_sha256 `{wsha[:16]}…`):**

```
Claim: "dM₂/dτ > 0 strict for τ>0 (⟨λ²⟩ increases monotonically); the +58672.8 anchor is the
        |λ|-action (f=√x) SIGN-corollary of E7, distinct from the λ²-moment gradient 213991.8;
        the ratio-2.647 reading was a functional-label mismatch."

Definition 1: M₂(p,q;τ) := zeta-regulated second spectral moment ⟨λ²⟩ on sector (p,q) at
              deformation τ (the a_2^{{ζ}} ingredient). Closed form dM₂/dτ = d·[C₂·gC + gS].
              [npz: max_rel_M2={w['max_rel_M2']:.3e}, max_rel_dM2={w['max_rel_dM2']:.3e} — closed
               form reproduces the direct moment to float floor]
Definition 2: gC, gS := deformation cofactors; gC·e^{{2τ}} = (u−1)(4u³+4u²+4u+4/3),
              gS·e^{{4τ}} = (u−1)(10u⁵+10u⁴+10u³+6u²+2u+2); npz integer-scaled storage
              cofactor_gC={gC_npz}, cofactor_gS={gS_npz} (×3 / descending-power image of the
              same polynomials); cofactor_gC_all_positive={w['cofactor_gC_all_positive']},
              cofactor_gS_all_positive={w['cofactor_gS_all_positive']}; d = sector degeneracy > 0;
              C₂ = quadratic Casimir ≥ 0.
Definition 3: u := e^τ, the (u−1)-factorization variable; u > 1 ⟺ τ > 0.
Substitute:   dM₂/dτ = d · [ C₂ · (u−1)(4u³+4u²+4u+4/3)·e^{{−2τ}}
                            + (u−1)(10u⁵+10u⁴+10u³+6u²+2u+2)·e^{{−4τ}} ]
              with d>0, C₂≥0, all polynomial coefficients >0, and (u−1)>0 for τ>0.
Simplify:     a sum/product of strictly-positive terms (times the non-negative C₂·d weight, with the
              gS term strictly positive on its own) is strictly positive ⇒ dM₂/dτ > 0 for all τ>0,
              L-uniformly, sector-by-sector. npz min_dM2_dtau_over_domain = {minv:.9f} > 0;
              sign_match = {w['sign_match']}; dM2_dtau_at_tau0_maxabs = {w['dM2_dtau_at_tau0_maxabs']:.3e}
              (the FD float floor of the algebraic zero gC(0)=gS(0)=0 at τ=0).
Canonical:    dM₂/dτ > 0 (strict, τ>0); = 0 iff τ=0 (the unique critical point — the cold
              bi-invariant point u=1, the substrate's τ=0 unstable maximum from which the
              spectrum cascades into complexity).
              [equipartition step (ii): the 3:4:1 cross-sector cofactor split is Schur's lemma on
               the G-equivariant rep-trace form of the simple su(3) — NOT a fit; npz
               max_equipartition_deviation = {eqdev:.3e} is the Schur-corollary float witness.]
Direction (anchor re-scope): dS/dτ = +{dS_grad:.1f} is the f=√x |λ|-action gradient (SIGN-corollary
              dS_{{|λ|}}/dτ > 0 of E7's ALL-monotone-f). The λ²-MOMENT gradient is the DIFFERENT
              functional dS₂/dτ = {dS2_grad:.1f}. The "ratio 2.647" (= raw {raw_ratio:.3f} − 1)
              conflated the two; both are positive (E7), so the SIGN-corollary direction is unchanged.
Conclusion:   M₂ is strictly monotone increasing for τ>0 (registrable closed form); the +58672.8
              anchor is correctly the |λ|-action SIGN-corollary of E7, the λ²-gradient being
              213991.8 — both readings preserve dS/dτ>0. ∎ (S-2 proof-check PASS; this gate
              REGISTERS the closed form + applies the two MINOR remediations.)
```

**Limiting cases (S-2 proof-check §3; clean at both ends)**:
- **τ = 0 (u = 1)**: `gC(0) = 4 − 8/3 − 4/3 = 0` and `gS(0) = 10 − 4 − 4 − 2 = 0` EXACTLY (Sage QQ) ⇒ `dM₂/dτ|₀ = 0` — the cold bi-invariant point is the **unique critical point** (substrate language: the τ=0 vacuum is the unstable maximum from which the spectrum cascades; matches the registry "cold big bang, τ=0 unstable maximum"). npz `dM2_dtau_at_tau0_maxabs = {w['dM2_dtau_at_tau0_maxabs']:.3e}` is the FD float floor of this algebraic zero.
- **τ → ∞**: `dM₂/dτ ~ d·(4C₂ + 10)·e^{{2τ}} → +∞` — strictly increasing, NO upper turning point. The proof holds on the entire physical domain `[0, τ_NEC = {w['tau_NEC']})` and beyond (consistent with the proof certificate `regime_verdict = {w['regime_verdict']}`).

**Anchor structure**: **PRIMARY + INDEPENDENT-CROSS-CHECK** per `registry-landing.md`. The closed-form derivation (S102 W3-14, the PRIMARY anchor) is independently cross-checked by the S-2 proof-check synthesis (the Schur-lemma derivation of step (ii) + the Sage-QQ (u−1)-factorization of step (iii) + the limiting-case verification — an INDEPENDENT route reproducing the same monotonicity conclusion). This is NOT a sequential V+C chain (the proof-check does not SUPPLY a premise the closed form lacks; it re-derives the same conclusion by an alternative argument), so SOURCE-DOUBLE-CITE-CO-PRIMARY does NOT apply — the correct tag is PRIMARY + INDEPENDENT-CROSS-CHECK. **Corner check**: the λ²-moment `M₂ = Σ_k m_k λ_k²` is an **algebra-INVARIANT spectrum-only functional** (Corner I) per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-at-K=3 — it depends only on `{{λ_k, m_k}}`, not on a state-pair on `A_K`.

**STRUCTURAL relation to the E7 Structural Monotonicity class** (NOT co-primary): the E7 result (atlas-07 W7; CUTOFF-SA-37, S37 — "`S_f` monotone for ALL monotone `f`, ALL cutoffs `Λ`, ALL 10 sectors, same direction") is the PARENT structural theorem. This §VII.{letter} is the **`f(x) = x` (λ²-moment) SHARPENING** of E7: where E7 asserts monotonicity for the whole monotone-`f` family, this entry supplies the EXACT closed form `dM₂/dτ = d·[C₂·gC + gS]` for the specific `f(x) = x` member, with the explicit `(u−1)`-factorization that makes the mechanism transparent (term-by-term positivity ⇒ L-uniform). E7 is the umbrella; this is its closed-form λ² instance.

**5-anatomy (IS-not-IN) — declared N/A-with-reason** (intra-pillar structural theorem; no laboratory-IN continuum-image observable, no HKR / K-theory / Connes–Karoubi bridge map):
1. **Substrate-IS observable** — the second spectral moment `M₂(p,q;τ) = ⟨λ²⟩` and its τ-derivative `dM₂/dτ` on the Jensen-deformed spectral triple `(A_K, H_K, D_K(τ))` (Level-2 moduli-deformation substrate-IS — the τ-flow is the substrate's intrinsic Jensen TT-deformation parameter, `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). The substrate IS this moment-flow.
2. **Laboratory-IN observable** — **N/A-with-reason**: this is an intra-pillar structural statement about the fabric's own deformation flow, NOT a substrate↔laboratory convergence bridge. There is no continuum measurement the moment-derivative converges TO; `dM₂/dτ > 0` is a fact about the substrate's internal complexification, measured by the substrate on itself.
3. **Bridge map** — **N/A-with-reason**: there is no HKR / Connes–Karoubi continuum pairing; the "map" is the closed-form derivative operator `d/dτ` applied to the substrate's own `a_2^{{ζ}}` moment.
4. **Algebraic envelope** — **N/A-with-reason** (Level-2 NON-BINDING / structurally-exact): the strict positivity is EXACT at every `L_max` (term-by-term `(u−1)·(positive)` factorization; `α = ∞`, NOT a convergent `L^{{−α}}`); no `c_continuum` exists.
5. **Empirical anchor** — **N/A-with-reason**: there is no `Level-3 < Level-2` convergence inequality; the result IS the exact closed form, confirmed by the proof-certificate residuals (`max_rel_dM2 = {w['max_rel_dM2']:.3e}`, `min_dM2_dtau_over_domain = {minv:.3e} > 0`) at L_max=10.

**Three-level structural-confidence ladder — declared N/A-with-reason** (the standard convergence ladder does not apply to an exact closed-form identity):
- **Level 1** — the `(u−1)`-factorized strictly-positive-cofactor monotonicity identity + the Schur-lemma equipartition (regulator-invariant, holds at every `L_max`: the term-by-term positivity is a closed-form algebraic identity, NOT a truncation-dependent estimate). STRUCTURAL THEOREM.
- **Level 2** — **N/A-with-reason** (NON-BINDING / structurally-exact; no `c_continuum` — the strict positivity IS exact identically, term-by-term).
- **Level 3** — **N/A-with-reason**: the standard "Level-3 < Level-2" convergence-PASS criterion does NOT apply (the closed form is exact; the proof-certificate residuals are float-floor cross-checks of an algebraic identity, not a convergence anchor).

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`): the fabric IS the Jensen-deformed spectral triple `(A_K, H_K, D_K(τ))`; `⟨λ²⟩(τ)` IS the second spectral moment of `D_K` (the `a_2^{{ζ}}` ingredient → the induced Einstein-Hilbert kinematic skeleton). **Direction**: `D_K eigenvalues → ⟨λ²⟩ second moment M₂(p,q;τ) → its strictly-positive τ-derivative dM₂/dτ = d·[C₂·gC + gS] (forced by the (u−1)-factorization with strictly-positive cofactors + the Schur-lemma equipartition) → the spectral action's monotone flow toward the fold`. In substrate language `d⟨λ²⟩/dτ = Σ_sectors (positive Casimir weight)·(u−1)·(positive cofactor) > 0` makes the exflation mechanism transparent: spectral complexity grows monotonically inside each fiber-point as τ increases off the bi-invariant point `u=1`. This is the substrate's **exflation** (internal spectral complexification), NOT metric expansion; the cold τ=0 vacuum is the unique critical point. FORBIDDEN inversion (container thinking): "⟨λ²⟩ increases because the spectral triple expands in a τ-coordinate container" → INVERT: τ IS the substrate's intrinsic deformation parameter (Level-2 moduli-deformation substrate-IS); the moment-flow `dM₂/dτ > 0` is a fact about the fabric's own structure, not motion through a meta-container. Gravity (`a_2`) and the gauge action (`a_4`) are downstream moments of this same monotone flow.

**Closure SHA pin** (over the ordered input-pin map): registry_pre_write_file_sha256=`{registry_pre_sha[:16]}…`; witness_npz_sha256=`{witness_npz_sha[:16]}…`; witness_audit_sha256=`{wsha[:16]}…`. The full dual-SHA (audit_sha256 / content_sha256) is on the `S103-LAMBDA2-MONOTONICITY-REGISTRY-LANDING` verdict line in `computations/session-103/s103_gate_verdicts.txt` (with a `regulator_pin=a_2^{{ζ}}` companion extra-row).

**Provenance**: S102 W3-14 closed-form derivation (`dM₂/dτ = d·[C₂·gC + gS]`, (u−1)-factorization) + `sessions/session-102/session-102-connes-ncg-lambda2-proofcheck-synthesis.md` (S-2 proof-check, VERDICT **PASS**, severity MINOR: state equipartition as Schur-lemma corollary + re-scope the +58672.8 anchor as the |λ|-action SIGN-corollary); witness `computations/session-102/s102_trd2_monotonicity_analytic.npz` (audit_sha256 `{wsha}`; keys cofactor_gC/gS (+_all_positive), factor_remainder_gC/gS=0, min_dM2_dtau_over_domain={minv:.6e}, sign_match=True, dS_fold_canonical={dS_grad:.5f}, dS2_lambda2_action_grad_analytic={dS2_grad:.5f}, literal_xcheck_ratio={lit_ratio:.6f}; NOT re-adjudicated — VALUES authoritative). The npz cofactor arrays are the INTEGER-SCALED / descending-power image of the synthesis polynomial coefficients [4/3,4,4,4] / [2,2,6,10,10,10] (representation-only plan-text drift, disclosed per `substrate-first-canonical-sourcing.md §(ii.B)`; all_positive / remainder=0 / sign_match hold identically in both forms). Anchors: E7 Structural Monotonicity class (atlas-07 W7; CUTOFF-SA-37, S37 — PARENT; this entry is its f(x)=x λ²-moment sharpening); Schur's lemma (PROVEN pure-math, framework theorem set); `dS_fold = {dS_fold:.8f}` (S42 `s42_gradient_stiffness`, canonical_constants). NO compute gate — registry-landing of an upstream-proven closed form (binding-text discipline). §VII.{letter} slot verified next-free at runtime via the all-header-level append-protocol scan (highest prior §VII.BV). This is a §VII NCG/geometric structural-theorem landing, NOT a §7 falsifier-surface row — mack-cosmic-bridge sole-writer does NOT apply (`feedback_mack-bridge-role.md`).

"""
    return body


def build_table_row(letter: str, w: dict, audit_sha: str) -> str:
    """Return the single slot-index TABLE row for §VII.<letter> (matching the BV row shape)."""
    minv = w["min_dM2_dtau_over_domain"]  # (local)
    dS_grad = w["dS_fold_canonical"]  # (local)
    dS2_grad = w["dS2_lambda2_action_grad_analytic"]  # (local)
    row = (f"| §VII.{letter} | THM | λ²-Moment Monotonicity Closed Form on the Jensen-Deformed "
           f"Spectral Triple — `dM₂/dτ = d·[C₂·gC + gS]` is strictly positive for τ>0, L-uniform "
           f"((u−1)-factorized with strictly-positive cofactors [4/3,4,4,4]/[2,2,6,10,10,10], "
           f"npz min_dM2_dtau_over_domain={minv:.3e}>0, sign_match=True), STAGE-1-CANDIDATE "
           f"(S103 W1-2 landing audit {audit_sha[:8]}, intra-pillar GEOMETRIC structural theorem; "
           f"transcribed from S102 W3-14 closed form + S-2 proof-check synthesis [VERDICT PASS, "
           f"MINOR-only]; a_2^{{ζ}} regulator pin; two MINOR remediations applied — (i) equipartition "
           f"3:4:1 as Schur-lemma corollary [rep-trace form ∝ Killing on simple su(3)], (ii) +58672.8 "
           f"re-scoped as the |λ|-action f=√x SIGN-corollary of E7, distinct from the λ²-moment "
           f"gradient {dS2_grad:.1f} [|λ|-action gradient {dS_grad:.1f}]; f(x)=x sharpening of the E7 "
           f"Structural Monotonicity class; PRIMARY+INDEPENDENT-CROSS-CHECK, Corner-I algebra-INVARIANT; "
           f"5-anatomy+3-level N/A-with-reason; Level-2 moduli-deformation τ-flow; section body at "
           f"§VII.{letter}) | gen-physicist | 2026-06-10 |")  # (local)
    return row


# ---------------------------------------------------------------------------
# Section 7 — Atomic write (section body + slot-index table row) + re-read verify
# ---------------------------------------------------------------------------

def write_atomic_with_fsync(registry_path: Path, full_text: str) -> None:
    """Write full_text to registry_path atomically (temp + os.replace + fsync)."""
    tmp = registry_path.with_suffix(registry_path.suffix + ".tmp_s103bw")  # (local)
    data = full_text.encode("utf-8")  # (local)
    with open(tmp, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, registry_path)


def insert_table_row(registry_text: str, bv_prefix: str, new_row: str) -> tuple[str, bool]:
    """Insert new_row immediately AFTER the §VII.BV slot-index TABLE row (line-anchored).
    Returns (new_text, inserted_bool). Idempotent: if new_row already present, no-op."""
    if new_row in registry_text:
        return registry_text, False  # (local) idempotent
    lines = registry_text.split("\n")  # (local)
    out: list[str] = []  # (local)
    inserted = False  # (local)
    for ln in lines:
        out.append(ln)
        if (not inserted) and ln.startswith(bv_prefix):
            out.append(new_row)
            inserted = True
    return "\n".join(out), inserted


def verify_section_matches(actual_full_text: str, expected_section: str) -> bool:
    """True iff the expected §VII section body appears verbatim in the re-read file."""
    return expected_section.strip() in actual_full_text


# ---------------------------------------------------------------------------
# Section 8 — Gate verdict payload (printed for the agent's emit_verdict call)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": 103,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 2. Witness numbers (no recomputation)
    w = load_witness()
    print()
    print("=== Witness (s102_trd2_monotonicity_analytic.npz; re-derives NOTHING) ===")
    print(f"  cofactor_gC (npz)     = {w['cofactor_gC_npz']}  (×3/desc-power image of [4,4,4,4/3])")
    print(f"  cofactor_gS (npz)     = {w['cofactor_gS_npz']}  (desc-power image of [10,10,10,6,2,2])")
    print(f"  cofactor_gC_all_positive = {w['cofactor_gC_all_positive']} | gS = {w['cofactor_gS_all_positive']}")
    print(f"  factor_remainder_gC   = {w['factor_remainder_gC']} | gS = {w['factor_remainder_gS']} (Sage QQ, (u-1) divides exactly)")
    print(f"  min_dM2_dtau_over_domain = {w['min_dM2_dtau_over_domain']:.9f}  (> 0; at {w['argmin_dM2']})")
    print(f"  dM2_dtau_at_tau0_maxabs  = {w['dM2_dtau_at_tau0_maxabs']:.3e}  (FD floor of algebraic 0)")
    print(f"  max_equipartition_deviation = {w['max_equipartition_deviation']:.3e}  (Schur-corollary float shadow)")
    print(f"  sign_match = {w['sign_match']} | composite (cert) = {w['composite']}")
    print(f"  --- anchor re-scope (ii) ---")
    print(f"  dS_fold_canonical (|λ|-action grad)     = {w['dS_fold_canonical']:.5f}  (= +58672.8 anchor)")
    print(f"  dS_full_dtau_reproduced                 = {w['dS_full_dtau_reproduced']:.5f}  (rel_err {w['anchor_repro_rel_err']:.3e})")
    print(f"  dS2_lambda2_action_grad_analytic (λ²)   = {w['dS2_lambda2_action_grad_analytic']:.5f}  (= 213991.8 λ²-grad)")
    print(f"  literal_xcheck_ratio = {w['literal_xcheck_ratio']:.6f} | literal_xcheck_pass = {w['literal_xcheck_pass']} (different functionals, NOT a fail)")
    print(f"  canonical_constants dS_fold = {dS_fold:.8f} | S_fold = {S_fold:.8f}")
    print(f"  witness audit = {w['witness_audit_sha256'][:16]}...")
    print()

    # 3. Read registry; capture pre-write SHA; resolve next-free §VII letter (ALL header levels)
    registry_pre_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    registry_pre_sha = sha256_of_text(registry_pre_text)  # (local)
    witness_npz_sha = pins[str(WITNESS_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")]  # (local)

    runtime_letter = next_free_vii_letter(registry_pre_text, frontier=PLAN_FRONTIER_LETTER)  # (local)
    plan_occupied = section_header_present(registry_pre_text, PLAN_FREEZE_LETTER)  # (local)
    print("=== Next-free §VII letter scan (ALL header levels) ===")
    print(f"  plan-freeze prediction: §VII.{PLAN_FREEZE_LETTER}  (header occupied={plan_occupied})")
    print(f"  runtime next-free:      §VII.{runtime_letter}")

    rerouted = (runtime_letter != PLAN_FREEZE_LETTER)  # (local)
    letter = runtime_letter  # (local) land at the runtime next-free letter regardless
    if rerouted:
        print(f"  REROUTE: plan §VII.{PLAN_FREEZE_LETTER} occupied -> landing §VII.{letter} "
              f"(FAIL-with-remediation in verdict, audit-trail visibility)")
    print()

    # 4. Build the FULL promotion text in memory (pure function)
    section_body = build_promotion_text(letter, w, registry_pre_sha, witness_npz_sha)  # (local)
    promotion_span_sha = sha256_of_text(section_body)  # (local)
    print(f"  promotion-text span SHA: {promotion_span_sha[:16]}...  (len={len(section_body)} chars)")

    # 4b. Dual-SHA (audit consumes registry_pre_sha + promotion_span_sha per plan audit_sha256_inputs)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins,
                                              registry_pre_sha, promotion_span_sha)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+registry_pre+promo_span)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    table_row = build_table_row(letter, w, audit_sha)  # (local)
    print(f"  slot-index table row: {table_row[:80]}...")
    print()

    # 5. Append section + insert table row; write atomically. Idempotent on re-run.
    section_already = section_body.strip() in registry_pre_text  # (local)
    row_already = table_row in registry_pre_text  # (local)

    text_with_row, row_inserted = insert_table_row(registry_pre_text, BV_TABLE_ROW_PREFIX, table_row)  # (local)
    if section_already:
        full_text = text_with_row  # (local) body present; only (maybe) row inserted
        print("  Section body already present (idempotent re-run for body).")
    else:
        sep = "" if text_with_row.endswith("\n\n") else ("\n" if text_with_row.endswith("\n") else "\n\n")  # (local)
        full_text = text_with_row + sep + section_body  # (local)

    if full_text != registry_pre_text:
        write_atomic_with_fsync(REGISTRY_PATH, full_text)
        print(f"  Wrote §VII.{letter} body (section_new={not section_already}) + "
              f"table_row (row_new={row_inserted}) to {REGISTRY_PATH.name}")
    else:
        print("  Nothing to write (fully idempotent re-run).")

    # 6. Re-read + verify (the FINAL verification step) — BOTH body AND table row
    registry_post_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    registry_post_sha = sha256_of_text(registry_post_text)  # (local)
    verify_ok = verify_section_matches(registry_post_text, section_body)  # (local)
    header_landed = section_header_present(registry_post_text, letter)  # (local)
    table_row_landed = table_row_present(registry_post_text, letter)  # (local)
    # Content-marker checks (the operator-set the gate PASS requires)
    markers = {  # (local)
        "STAGE-1-CANDIDATE": "STAGE-1-CANDIDATE" in section_body,
        "Schur": ("Schur lemma" in section_body) or ("Schur-lemma" in section_body),
        "lambda-action-sign-corollary": ("|λ|-action" in section_body
                                         and "SIGN-corollary" in section_body
                                         and "58672.8" in section_body
                                         and "213991.8" in section_body),
        "closed-form": "dM₂/dτ = d·[ C₂·gC(τ) + gS(τ) ]" in section_body or "dM₂/dτ = d·[C₂·gC + gS]" in section_body,
        "5-anatomy": "5-anatomy" in section_body,
        "3-level N/A": "Three-level structural-confidence ladder — declared N/A-with-reason" in section_body,
        "a2-zeta-regulator-pin": "a_2^{ζ}" in section_body,
    }
    all_markers = all(markers.values())  # (local)
    print("=== Re-read verify ===")
    print(f"  verify_section_matches = {verify_ok}")
    print(f"  header §VII.{letter} present = {header_landed}")
    print(f"  slot-index table row §VII.{letter} present = {table_row_landed}")
    for k, v in markers.items():
        print(f"  marker[{k}] = {v}")
    print(f"  all content markers = {all_markers}")
    print()

    # 7. Verdict (AFTER-pattern: verdict IS the boolean; no corrective rewrite)
    section_present_and_correct = bool(verify_ok and header_landed and table_row_landed
                                       and all_markers)  # (local)
    if rerouted:
        verdict = "FAIL"  # (local) slot collision at plan-pinned letter -> FAIL-with-remediation
    elif section_present_and_correct:
        verdict = "PASS"  # (local)
    else:
        verdict = "FAIL"  # (local) assembly bug / slot collision

    value = (f"sec_match={verify_ok};landed=§VII.{letter};table_row={table_row_landed};"
             f"plan_letter=§VII.{PLAN_FREEZE_LETTER};rerouted={rerouted};markers_ok={all_markers};"
             f"min_dM2_dtau={w['min_dM2_dtau_over_domain']:.6e};sign_match={w['sign_match']};"
             f"lambda_action_grad={w['dS_fold_canonical']:.1f};lambda2_grad={w['dS2_lambda2_action_grad_analytic']:.1f}")  # (local)

    # 8. Persist npz audit record
    SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        verify_section_matches=verify_ok,
        header_landed=header_landed,
        table_row_landed=table_row_landed,
        all_content_markers=all_markers,
        landed_letter=letter,
        plan_freeze_letter=PLAN_FREEZE_LETTER,
        rerouted=rerouted,
        registry_pre_write_sha256=registry_pre_sha,
        registry_post_write_sha256=registry_post_sha,
        promotion_text_span_sha256=promotion_span_sha,
        witness_npz_sha256=witness_npz_sha,
        witness_audit_sha256=w["witness_audit_sha256"],
        cofactor_gC_npz=np.array(w["cofactor_gC_npz"]),
        cofactor_gS_npz=np.array(w["cofactor_gS_npz"]),
        cofactor_gC_all_positive=w["cofactor_gC_all_positive"],
        cofactor_gS_all_positive=w["cofactor_gS_all_positive"],
        factor_remainder_gC=w["factor_remainder_gC"],
        factor_remainder_gS=w["factor_remainder_gS"],
        min_dM2_dtau_over_domain=w["min_dM2_dtau_over_domain"],
        dM2_dtau_at_tau0_maxabs=w["dM2_dtau_at_tau0_maxabs"],
        max_equipartition_deviation=w["max_equipartition_deviation"],
        sign_match=w["sign_match"],
        dS_fold_canonical=w["dS_fold_canonical"],
        dS2_lambda2_action_grad_analytic=w["dS2_lambda2_action_grad_analytic"],
        literal_xcheck_ratio=w["literal_xcheck_ratio"],
        literal_xcheck_pass=w["literal_xcheck_pass"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
    )
    print(f"  wrote {OUT_NPZ.name}")

    # 9. 4-tuple + verdict payload (exactly one); carry the a_2^{ζ} regulator_pin extra-row
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [  # (local)
        "# regulator_pin=a_2^{ζ} (zeta-regulated Seeley-DeWitt 2nd moment; "
        "regulator-pin-discipline.md) — λ²-moment M₂ is the a_2^{ζ} ingredient via monotone-f inheritance",
    ]
    if rerouted:
        extra.append(f"# slot-reroute: plan §VII.{PLAN_FREEZE_LETTER} occupied -> landed §VII.{letter} "
                     f"per epistemic-discipline.md Registry-Write-Hygiene item 3 (FAIL-with-remediation)")
    note = (f"§VII.{letter} λ²-moment monotonicity closed form dM₂/dτ=d·[C₂·gC+gS]>0 for τ>0 (STAGE-1-CANDIDATE); "
            f"Schur-lemma equipartition; |λ|-action SIGN-corollary anchor re-scope "
            f"(58672.8=|λ|-action grad / 213991.8=λ²-grad); span_sha={promotion_span_sha[:16]}")  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else (0 if section_present_and_correct else 1)


if __name__ == "__main__":
    sys.exit(main())
