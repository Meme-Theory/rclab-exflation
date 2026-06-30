#!/usr/bin/env python3
"""
S93 W2-4 — VII.AU CF-37 Fredholm-module-as-canonical corpus-row landing
=======================================================================

Gate: S93-W2-4-VII-AU-CF37-MODULE-AS-CANONICAL-CORPUS-ROW ([VERIFY])

Pre-registered threshold (METHODOLOGY/registry-class; corpus §19
weighting-functional-family directive; CF-S93-W1-3 re-scoped EXECUTION leg):
  PASS iff ALL of:
    (i)   topological shadow [phi_cd] in Z^3 declared as Element-1 substrate-IS
          observable (VALUE-PINNED to the W2-1 integer triple (0,0,0))
    AND (ii)  analytic shadow mu_cd declared physical-content-NOT-bridge-observable
          (scope distinction, corpus §19.0 MANDATORY)
    AND (iii) weighting-functional family Phi_w + topological STOPPING rule
          (base-count not fiber-count) at K=1 SUGGESTION
    AND (iv)  the two methodology sub-lessons (A moment-problem diagnosis +
          B residual-reading discipline) in ONE row, NOT two (fiber-counting error
          forbidden).
  detect_weighting_functional_family must return canonical_id_complete
  (has_family_reaxis AND has_stopping_rule; NO fiber-count misframe → reframe).

  Verdict logic (single-shot AFTER-pattern):
    build_corpus_row_text -> write_atomic_with_fsync -> re_read + verify_section_matches
    -> emit ONE verdict line. PASS iff the row is on disk with all 4 predicates +
    detector canonical_id_complete + substantive_line_count >= 15 + the value-pinned
    [phi_cd]=(0,0,0) Element-1. INFO iff the value-pin is CHAINED-on-W2-1 (W2-1 npz
    absent at dispatch). FAIL iff a content predicate is missing OR the detector fires
    canonical_id_incomplete OR the sub-lessons are split into two rows.

UPSTREAM (W2-1 LANDED, INFO): the [phi_cd] integer triple is loaded from
  computations/session-93/s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.npz
  (key phi_cd_integer_triple = [0 0 0], int64). W2-1 closed INFO (not PASS): HARD-1
  integrality PASS at machine-zero; HARD-2 grading-signed winding FAIL (T_signed=0,
  measured eps_Cgamma=+1 commute rule). Per the plan Wave-2 Decision Point "If W2-1
  INFO" branch: record the integer triple as VALUE-PINNED (discharging the corpus
  §19.1 "value-pinning queued" residual) AND flag the winding reconciliation as a
  Stage-2-style cross-axis follow-up (vdd rep-side/J-twisted K-homology vs volovik
  BdG-sector winding under chi-inheritance, on the SAME triple). W2-1's structural
  finding: the BDI winding N_K=2 (KO-dim=6) cannot live in the gamma_9-grading-signed
  total T_signed (=0, balanced 8/8 spinor chirality); it must be read from a DIFFERENT
  pairing. This goes in the corpus row's analytic-shadow / winding-reconciliation note.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/registry/cross-pillar-bridge-corpus.md (post-write state; feeds audit_sha256)
  - computations/session-93/s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.npz (CHAINED — [phi_cd] value)
  - computations/_shared/canonical_constants.py (M_KK, tau_fold, Delta_BCS, M_Pl_reduced — the Phi_w prefactor + anchors)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<row-landing-summary>,
   scheme=MODULE-AS-CANONICAL-CORPUS-ROW-LANDING-WEIGHTING-FUNCTIONAL-FAMILY-MACK-SOLE-WRITER-AFTER-PATTERN,
   convention=VII-AU-CF37-(c)o(d)-Fredholm-module-canonical-topological-shadow-phicd-Z3-Element-1-..., L_max=N/A)

Classification: NON-PHONONIC (corpus-row registry landing) — but the CONTENT it
lands is the deepest substrate-IS identification in the §VII.AU program: the substrate
IS the Fredholm module (H_K, D_K(tau_fold), gamma, J) at the (c)∘(d) image.

METHODOLOGY
-----------
mack sole-writer corpus-row landing (single-shot AFTER-pattern per
registry-landing.md §"Bridge-Landing Script Architecture"). The corpus §19.0 DIRECTIVE
+ §19.1 K=1 calibration instance were EFFECTED IN-SESSION by the S92 workshop
(volovik x vdd; corpus lines 970-1085). This gate lands the PERMANENT registry-row of
the module-as-canonical as corpus §19.2 — the CF-S93-W1-3 EXECUTION leg, re-scoped per
corpus §19 CF-(ii) from "canonical-identity NOT YET pinned" to "land the
module-as-canonical row". The row's NEW load-bearing content vs §19.1: the topological
shadow is now VALUE-PINNED to the W2-1 integer triple (0,0,0) (discharging §19.1's
"value-pinning queued" honest residual) + the winding-reconciliation follow-up note
(W2-1 closed INFO; T_signed=0 != N_K=2; the BDI winding lives in a different pairing).

Substrate framing: NON-PHONONIC (corpus-row registry landing). The substrate IS the
Fredholm module (H_K, D_K(tau_fold), gamma, J) at the (c)∘(d) image, a Level-1
single-tau-slice object per phononic-framing.md. Its topological shadow [phi_cd] in Z^3
carries the cocycle-ratio invariants the lab falsifies as integers; its analytic shadow
mu_cd carries the BdG energies the lab measures as line positions. Every weighting
functional Phi_w factors through the same finite [phi_cd] — so the K-counter is a
base-count, not a fiber-count (topological STOPPING rule, the anti-inflation DERIVATION
not heuristic). Direction of explanation flows FROM the module DOWNWARD through the two
forgetful maps (index -> class; |D_K| -> measure); container-thinking ("one scalar IS
the canonical") is FORBIDDEN and INVERTED to "the module is the canonical; the scalars
are moments of its analytic shadow."

DISCIPLINE
----------
- `from canonical_constants import *` (Section 1).
- Every local/intermediate tagged `# (local)`.
- CPU-only (corpus-text edit + SHA + W2-1 npz read; no linear algebra); OMP capped to 8.
- SHA-256 of all input files logged in first lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema) via append_verdict.
- 4-tuple printed as the final non-verdict line.
- Single-shot AFTER-pattern: build text in memory -> write_atomic_with_fsync ->
  re_read + verify -> emit ONE verdict line. NO conditional rewrite branch.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (set BEFORE numpy import; no GPU used)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Explicit import of the canonical anchors the corpus row references (the Phi_w
# prefactor + the substrate-distance anchors). These descend from substrate spectral
# geometry; they are not external inputs.
from canonical_constants import (  # noqa: E402
    M_KK,
    M_Pl_reduced,
    tau_fold,
    Delta_BCS,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import time     # noqa: E402

import numpy as np  # noqa: E402

# Detector — the registry-completeness check on the canonical-identification axis.
# detect_weighting_functional_family verifies the row re-axes §(ii.A) to a
# weighting-functional FAMILY (has_family_reaxis) AND cites the topological STOPPING
# rule (has_stopping_rule), with NO un-reframed fiber-count misframe.
sys.path.insert(0, str(SHARED_DIR))
from _cross_pillar_bridge_audit import detect_weighting_functional_family  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S93"                                                            # (local)
GATE_ID = "S93-W2-4-VII-AU-CF37-MODULE-AS-CANONICAL-CORPUS-ROW"            # (local)
SCHEME = (
    "MODULE-AS-CANONICAL-CORPUS-ROW-LANDING-WEIGHTING-FUNCTIONAL-FAMILY-"
    "MACK-SOLE-WRITER-AFTER-PATTERN"
)                                                                          # (local)
CONVENTION = (
    "VII-AU-CF37-(c)o(d)-Fredholm-module-canonical-topological-shadow-phicd-Z3-"
    "Element-1-analytic-shadow-mucd-physical-NOT-bridge-K1-SUGGESTION-corpus-19"
)                                                                          # (local)
L_MAX = "N/A"                                                              # (local)

# Canonical write-order verdict-file path per gate-verdicts.md §"Canonical Verdict-File Path":
# computations/session-{N}/s{N}_gate_verdicts.txt  (NOT computations/_shared/)
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"                        # (local)
OUT_JSON = SESSION_DIR / "s93_w2_4_vii_au_cf37_module_as_canonical_corpus_row.json"  # (local)
OUT_PNG = SESSION_DIR / "s93_w2_4_vii_au_cf37_module_as_canonical_corpus_row.png"    # (local)

CORPUS_PATH = (
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"
)                                                                          # (local)
W2_1_NPZ = SESSION_DIR / "s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.npz"  # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                     # (local)

INPUT_FILES = [CORPUS_PATH, W2_1_NPZ, CANONICAL_PATH]                      # (local)

# The new corpus sub-section anchor (the permanent module-as-canonical row).
ROW_ANCHOR = "### §19.2"                                                   # (local)
# Insert the new §19.2 immediately BEFORE the §20 header (§19 ends at the §20 boundary;
# corpus §20 currently lands at line ~1183 with the "## §20." heading). Runtime-resolve
# per substrate-first-canonical-sourcing.md §(ii.B) — find the FIRST top-level header
# after §19.1's content.
INSERT_BEFORE_ANCHOR = "## §20."                                          # (local)

# Citation pins (verbatim from plan §W2-4 + Input-SHA ledger; audit-chain citation pins).
W2_1_AUDIT_SHA = "76e5d744b36b7b35edced48bffe63659c0e667ee2f60bd9272203819496c5f99"  # (local) S93 §W2-1 canonical (latest non-superseded; INFO)
CHI_PRIME_AUDIT_SHA = "90bba262af80a04c"  # (local) S89 §W2-3 chi'-inheritance morphism (16-hex head as in corpus §19.1)

K_COUNTER_STATUS = "K=1 SUGGESTION"        # (local) topological stopping rule: base-count not fiber-count


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema; W9a-99 split)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical_constants.py) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append a single canonical verdict line + dual-SHA companion row (S84+ schema).

    Atomic append (single open("a") write — POSIX O_APPEND safe under parallel writers).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"METHODOLOGY/registry-class corpus-row landing artifact-existence; "
        f"[VERIFY] no [SIGN] 3-tuple\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 5 — build the corpus §19.2 module-as-canonical row text (in memory)
# ---------------------------------------------------------------------------
def load_phi_cd_triple() -> tuple[tuple, bool, str]:
    """Load the W2-1 integer triple [phi_cd] in Z^3. Returns (triple, value_pinned, note).

    value_pinned=True iff the W2-1 npz is on disk with phi_cd_integer_triple. If absent,
    fall back to the corpus §19.1 type-pin and return value_pinned=False (the row records
    the type-pinned class with the value-pin marked CHAINED on S93-W2-1 -> INFO).
    """
    if W2_1_NPZ.exists():
        d = np.load(W2_1_NPZ, allow_pickle=True)  # (local)
        if "phi_cd_integer_triple" in d:
            trip = tuple(int(x) for x in d["phi_cd_integer_triple"])  # (local)
            # Cross-read the W2-1 verdict context recorded in the npz for the note.
            t_signed = float(d["T_signed_grading"]) if "T_signed_grading" in d else None  # (local)
            n_k = int(d["N_K_winding"]) if "N_K_winding" in d else 2  # (local)
            eps = int(d["eps_Cgamma"]) if "eps_Cgamma" in d else 1  # (local)
            note = (
                f"value-pinned from W2-1 npz (key phi_cd_integer_triple); "
                f"T_signed_grading={t_signed}; N_K_winding={n_k}; eps_Cgamma={eps}"
            )  # (local)
            return trip, True, note
    # Fallback: type-pinned class, value-pin CHAINED on W2-1.
    return (None, None, None), False, "type-pinned; value-pin CHAINED on S93-W2-1 (npz absent at dispatch)"


def build_corpus_row_text(triple: tuple, value_pinned: bool) -> str:
    """Build the FULL §19.2 module-as-canonical permanent registry-row text in memory.

    The row carries the 4 content predicates the detector + plan require:
      (i)   topological shadow [phi_cd] in Z^3 as Element-1 substrate-IS observable
            (VALUE-PINNED to the W2-1 integer triple)
      (ii)  analytic shadow mu_cd as physical-content-NOT-bridge-observable (scope distinction)
      (iii) weighting-functional family Phi_w + topological STOPPING rule (base-count) at K=1 SUGGESTION
      (iv)  the two methodology sub-lessons (A + B) in ONE row.
    PLUS the W2-1 INFO-branch additions: the value-pinned triple discharging the §19.1
    "value-pinning queued" residual + the winding-reconciliation follow-up note.
    """
    if value_pinned:
        trip_str = f"({triple[0]}, {triple[1]}, {triple[2]})"  # (local)
        value_line = (
            f"**VALUE-PINNED** to `[φ_cd] = (n_(0,0), n_(0,1), n_(1,0)) = {trip_str} ∈ ℤ³` "
            f"(S93 §W2-1 `S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE`, "
            f"audit_sha256=`{W2_1_AUDIT_SHA}`; the integer-triple value loaded from "
            f"`computations/session-93/s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.npz` "
            f"key `phi_cd_integer_triple`). This DISCHARGES the §19.1 honest residual "
            f"\"value-pinning queued\": the per-sector indices are now COMPUTED (machine-zero "
            f"integrality, `max_a |n_a − round(n_a)| = 0.00e+00`), not existence-argued. The "
            f"cross-pillar-bridge Element-1 substrate-IS observable is a CONCRETE integer triple "
            f"⇒ envelope-FREE Level-2 (Level-2-trivial-by-saturation: the image is L_max-saturated "
            f"on the closed (c)∘(d) corridor, `N_image=112` bit-identical at L=10/12, foreclosing "
            f"any `L^{{-α}}`)."
        )  # (local)
    else:
        trip_str = "(n_(0,0), n_(0,1), n_(1,0))"  # (local)
        value_line = (
            f"**TYPE-PINNED** as `[φ_cd] = {trip_str} ∈ ℤ³` (the class is declared; the integer-triple "
            f"VALUE is **CHAINED on S93-W2-1** `S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE`, "
            f"which had not landed at this gate's dispatch — per the §19.1 \"value-pinning queued\" "
            f"residual). A same-session value-backfill closes the value-pin once W2-1 returns."
        )  # (local)

    text = f"""{ROW_ANCHOR} — Module-as-canonical PERMANENT registry-row landing (CF-S93-W1-3 EXECUTION leg; value-pinned [φ_cd]; S93 §W2-4 mack-cosmic-bridge)

> **Provenance**: S93 §W2-4 `{GATE_ID}` (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`; single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture"`, 2026-05-24). This is the **PERMANENT registry-row form** of the §19.0 DIRECTIVE + §19.1 K=1 calibration instance — the **CF-S93-W1-3 EXECUTION leg**, re-scoped per corpus §19 CF-(ii) from "canonical-identity NOT YET pinned" to "land the module-as-canonical row". The canonical = Fredholm module identification is the S92 §VII.AU CF-37 workshop's CONVERGED sub-question-(a) verdict (volovik × vdd; corpus §19, already effected in-session); this row lands its permanent form AND value-pins its topological shadow from the S93 §W2-1 Fredholm-index gate.

**The canonical IS the Fredholm module.** At the §VII.AU CF-37 (c)∘(d) corridor on `(A_K, H_K, D_K(τ))` (substrate-distance-2 pole s=4), the deeper substrate-IS canonical is the **Fredholm module** `(H_K, D_K(τ_fold=0.190), γ, J)|_{{(c)∘(d) image}}` — a Level-1 single-τ-slice object per `phononic-framing.md §"IS Space, Not IN Space"` — NOT any single scalar and NOT either single shadow. Both shadows descend from the module by distinct forgetful maps (index → class; `|D_K|` → measure), exactly as the §19.0 directive diagram specifies. Direction of explanation flows FROM the module DOWNWARD; container-thinking ("one of the three scalars `{{R_ansatz, R_CM_full, R_third}}` IS the canonical") is FORBIDDEN and INVERTED to "the module is the canonical; the three scalars are moments of its analytic shadow; the cocycle-ratio invariants are relative invariants of its topological shadow".

**Content predicate (i) — TOPOLOGICAL SHADOW `[φ_cd] ∈ K^0(A_K) ≅ ℤ³` as the cross-pillar-bridge Element-1 substrate-IS observable.** {value_line} Element-1 is specifically the topological shadow `[φ_cd]`, NOT the module and NOT the measure (the bridge-anatomy scope distinction below). The per-sector eigenvalue counts `{{(0,0):16, (0,1):48, (1,0):48}}`, `N_image=112`, dim-weighted total `Σ d_a·n_a = 1·16 + 3·48 + 3·48 = 304` are the substrate-IS image data; the integer triple `[φ_cd]` is the index of its topological shadow (a 48-mode sector carries index 0 via a 24/24 grading split — the answer the §19.1 open question awaited, now resolved by W2-1: **the 24/24 split, index 0** per sector, `dim H_a^+ = dim H_a^- = d_a·8`).

**Content predicate (ii) — ANALYTIC SHADOW `μ_cd` is physical-content-NOT-bridge-observable (scope distinction, corpus §19.0 MANDATORY).** The analytic shadow `μ_cd` (= `|D_K|` restricted to the image, the spectral measure) carries the BdG energies and NMR line positions the laboratory measures, and it IS substrate-IS, but it is **NOT the cross-pillar-bridge Element-1 observable**. Three structural reasons (corpus §19.0): (1) an integer-valued substrate-IS observable licenses an envelope-FREE Level-2, whereas a measure-anchored bridge would still owe an `L^{{-α}}` envelope; (2) the integer falsifier (lab integer-count) is a property of the class pairing `⟨[F_K], P_a⟩ ∈ ℤ`, not of the smeared measure; (3) the Connes-Karoubi bridge-map (Element 3) is by construction a class-level operation — a measure cannot source a Connes-Karoubi pairing (Kasparov-product factorization `[D_total] = [D_fiber] ⊗_B [D_base]`, vdd Paper 01 `1811.07824`, lives at the CLASS level). The three witnesses that force the canonical BELOW both shadows (§19.1): cocycle-RATIO invariant `793346/108307` (`S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM`, not extractable from any single-weight measure-moment ⇒ class ⊐ measure); regulator-class invariance `7.324974` across the full UV-atlas (`S89-SUBSTRATE-COCYCLE-RATIO-REGULATOR-CLASS-INVARIANCE-SCAN`, FI ⇒ topological); Z_factor 2.28% analytic defect (`R_CM_full` from its integer K_0-rank skeleton ⇒ measure ⊐ class on the spectral axis). Neither shadow dominates ⇒ canonical = the MODULE (the join).

**Content predicate (iii) — WEIGHTING-FUNCTIONAL FAMILY `Φ_w` + topological STOPPING rule (base-count not fiber-count) at {K_COUNTER_STATUS}.** The `substrate-first-canonical-sourcing.md §(ii.A)` atlas-row/cache-moment binary is re-axed to a one-parameter **weighting-functional family** `Φ_w : [φ_cd] ↦ (M_KK / M_Pl_reduced)² · ∫ |λ|^{{-s}} w(λ) dμ`, parameterized by the weight `w` and ANCHORED to the finite topological base `[φ_cd] ∈ ℤ³`. The §(ii.A) "atlas-row" (`Φ_atlas`, w drops the integral → `R_ansatz=3.900e-04`) and "cache-moment" (`Φ_cache`, `w_CM` the `ζ_D(0)` cubic-ρ residue weight → `R_CM_full=7.978e-04`) labels are TWO members; `Φ_K0` (`w_K0 = d_a/304` the χ'-inheritance-morphism Wedderburn-dimension weight → `R_third=6.960e-06`) is a third; `Φ_Dixmier`, `Φ_Wodzicki`, … are further fibers, ALL through the SAME `[φ_cd]`. **Topological STOPPING rule** (the anti-inflation DERIVATION, not a heuristic): every admissible weighting `Φ_w` **factors through the same finite K_0 class** `[φ_cd] ∈ ℤ³`, therefore counting fibers (weightings) is ILLEGITIMATE — there is provably nothing new to count until the BASE CLASS changes. The K-counter is a **base-count** (count of structurally-distinct K_0 classes at structurally-distinct triples via the Hybrid Independence Test `(i ∨ ii ∨ iii) ∧ iv`, §3), NOT a fiber-count: a single triple reporting N weighting-functionals is K=1 because clause (iv) "independent algebraic envelope" FAILS (all N fibers share the one image / one envelope). **Status**: {K_COUNTER_STATUS}; promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` (advancement = a structurally-distinct triple — different algebra / image / corridor — exhibiting the SAME three-register weighting structure with an INDEPENDENT algebraic envelope; candidate: the `M_4(ℂ)_PS` Pati-Salam block, seed / S91 W9 `hit_iv_pass` Wedderburn-rank distinction). Audit: `computations/_shared/_cross_pillar_bridge_audit.py::detect_weighting_functional_family` (S2 advisory at K=1; NOT HARD-HALT).

**Content predicate (iv) — TWO methodology sub-lessons in ONE row (NOT split into two — the fiber-counting error one level up).** Two structurally-orthogonal methodology observations emerge from the single CF-37 (c)∘(d) gate and land as TWO sub-lessons in THIS ONE row (splitting them into two rows would inflate the corpus-row count for one gate — the same fiber-counting error the topological STOPPING rule forbids one level up):

- **Sub-lesson A (moment-problem diagnosis)**: OOM-separated scalars at one nominal triple are diagnostic of a canonical that is a moment-sequence over a FINER structure (measure, or — when cohomology-ratio / topological invariants are present — a K-homology class / Fredholm module), of which the scalars are distinct moments. The FINENESS of the canonical (measure vs class vs module) is case-dependent: present iff topological invariants beyond the spectrum exist. Precedent: S44 CC/Hausdorff `f_4/f_2 = 1.4e-121` (measure-level moment problem; no cohomology-ratio content); CF-37 (c)∘(d) (module-level — carries cocycle-ratio invariants beyond the measure).
- **Sub-lesson B (residual-reading discipline)**: same registry-slot family does NOT imply same residual-reading; key the reading to SUPPORT-SATURATION status, not slot-family membership. A growing-support observable (s=3 OP-PROJ sister gate, does NOT saturate, rel_drift=2.374e-3) reads a residual as an asymptotic remainder (resolvable at higher L_max); a closed-support observable (s=4 (c)∘(d) corridor, L_max-saturated) reads it as a fixed structural signature (L_max-INDEPENDENT, e.g. the Z_factor 2.28%).

**Winding-reconciliation follow-up note (W2-1 INFO; Stage-2-style cross-axis follow-up on the SAME triple).** S93 §W2-1 closed **INFO** (not PASS): HARD-1 integrality PASS at machine-zero (`[φ_cd]=({triple[0] if value_pinned else 'n_(0,0)'},{triple[1] if value_pinned else 'n_(0,1)'},{triple[2] if value_pinned else 'n_(1,0)'})`), HARD-2 grading-signed winding **FAIL** (`T_signed = 0 ≠ N_K = 2` under the MEASURED `ε_Cγ=+1` commute rule; `J²=+I` BDI, `J γ_9 = +γ_9 J`). The structural finding: the BDI winding `N_K=2` (KO-dim=6 / AZ-class-BDI, a genuine framework-permanent result) **cannot live in the γ_9-grading-signed total `T_signed`** of the (c)∘(d)-image restriction — that total is identically 0 because the SU(3) spinor `ℂ^16` chirality grading is exactly balanced 8/8 (`Γ = I_d ⊗ γ_9` is rep-independent, so NO Peter-Weyl sector can carry a non-zero chiral index from the spinor grading alone). The winding must therefore be read from a **DIFFERENT pairing**, flagged as a Stage-2-style cross-axis follow-up on the SAME integer triple `[φ_cd]`:
  - **(α) rep-side / J-twisted K-homology** (vdd route): a K-homology class on the algebra factor `A_K`, NOT the spinor factor — the framework-permanent `{{J,γ}}=0` (ε''=−1) descends from the algebra-side conjugation, not the spinor-side `C2` (which COMMUTES with `γ_9`, `ε_Cγ=+1`);
  - **(β) BdG-sector winding under the χ-inheritance morphism** (volovik route): the 3He-B branch-count winding evaluated on the FULL BdG spectral triple rather than the bare (c)∘(d) image.
  This is a genuine future-work item (NOT a row-internal contradiction): the value-pin `[φ_cd]=(0,0,0)` is FIRM (the topological shadow IS this triple); the open question is which pairing carries `N_K=2` for the downstream integer 3He-B BDI branch-count Level-3 anchor (Open Question 4). The downstream anchor MUST read the winding from (α) or (β), NOT from `T_signed` of this gate.

**5-anatomy block (envelope-free cross-pillar bridge, both halves; per §19.1)**: substrate-IS = `[φ_cd] ∈ ℤ³` (Level-1, τ_fold=0.190, now value-pinned `({triple[0] if value_pinned else "·"},{triple[1] if value_pinned else "·"},{triple[2] if value_pinned else "·"})`); laboratory-IN = integer BDI branch-count per inheritance sector (OE-form `∑_a Tr(P_a · sign-graded)`); bridge map = Connes-Karoubi pairing; Level-2 envelope = TRIVIAL-by-saturation (the rare envelope-free cross-pillar bridge — the integer is L_max-saturated on the closed image); Level-3 anchor = the measured integer triple (this row) + the integer 3He-B BDI branch-count (downstream, reading the winding from pairing (α)/(β) per the follow-up note). Eigenvalues `|λ| ∈ [0.8197, 1.3277]` M_KK above `Delta_BCS = {Delta_BCS}` M_KK (S70 `BCS-GAP-CANONICAL-70`, R-PROTECTED; gapped ⇒ `ker D = {{0}}`, the integer-quantization is TOPOLOGICAL and immune to pressure/temperature smearing).

**K-counter status**: {K_COUNTER_STATUS} (the weighting-functional-family DIRECTIVE landed at §19.0/§19.1; this §19.2 is its PERMANENT registry-row form with the topological shadow value-pinned, the SAME K=1 calibration instance — NOT a new K-counter advancement). The topological STOPPING rule forecloses K-inflation: a fourth/fifth weighting (Dixmier, Wodzicki) evaluated next session does NOT advance K (all pair the same fixed `[φ_cd]`). K=2/K=3 advancement requires a structurally-distinct `(algebra, image, corridor)` triple with an INDEPENDENT algebraic envelope per the Hybrid Independence Test clause (iv).

**CF-S93-W1-3 re-scope discharge**: this row IS the CF-S93-W1-3 EXECUTION leg, re-scoped per corpus §19 CF-(ii). The re-scope is DISCHARGED: the module-as-canonical permanent registry-row is landed, with the topological shadow value-pinned (`{trip_str if value_pinned else "CHAINED on S93-W2-1"}`) and the winding reconciliation flagged for a Stage-2-style cross-axis follow-up.

**Cross-references**:
- §19.0 DIRECTIVE + §19.1 K=1 calibration instance (the directive + first-instance content this row lands as permanent form).
- Value-pin source: S93 §W2-1 `S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE` (audit_sha256=`{W2_1_AUDIT_SHA}`; INFO — integers value-pinned, winding deferred); npz key `phi_cd_integer_triple`.
- χ'-inheritance morphism: S89 §W2-3 `S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET` (PASS, audit_sha=`{CHI_PRIME_AUDIT_SHA}`; forces `w_K0 = d_a/304`).
- Detector: `computations/_shared/_cross_pillar_bridge_audit.py::detect_weighting_functional_family` (S2 advisory at K=1; canonical_id_complete = family-reaxis ∧ topological-stopping-rule, NO fiber-count misframe).
- Winding-reconciliation follow-up (genuine future work): vdd rep-side/J-twisted K-homology (α) vs volovik BdG-sector winding under χ-inheritance (β), on the SAME triple `[φ_cd]`; downstream integer 3He-B BDI branch-count Level-3 anchor (Open Question 4).
- Two-clause separation (registry-PASS vs K-counter advancement): `cross-pillar-bridge-anatomy.md §"Two-clause separation"`.
- Bridge-anatomy scope basis (class-level, not measure-level): Kasparov-product `[D_total] = [D_fiber] ⊗_B [D_base]`, vdd Paper 01 `1811.07824`; Fredholm-module presentation vdd Paper 04 `1207.2112` §2.

---

"""
    return text


def write_atomic_with_fsync(path: Path, full_text: str) -> None:
    """Write full_text to path atomically (write-temp + fsync + replace)."""
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(full_text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def land_corpus_row(row_text: str) -> dict:
    """Single-shot landing: read corpus, insert §19.2 before the §20 header, write
    atomically, re-read + verify. Returns a verification dict (NO emit here)."""
    pre_text = CORPUS_PATH.read_text(encoding="utf-8")  # (local)
    pre_sha = hashlib.sha256(pre_text.encode("utf-8")).hexdigest()  # (local)

    already_present = ROW_ANCHOR in pre_text  # (local)

    if already_present:
        # Idempotent re-run: the row is already on disk; do NOT duplicate. Verify it.
        post_text = pre_text  # (local)
        inserted = False  # (local)
    else:
        # Insert the §19.2 row immediately BEFORE the first "## §20." top-level header
        # (runtime-resolve per substrate-first-canonical-sourcing.md §(ii.B)).
        idx = pre_text.find("\n" + INSERT_BEFORE_ANCHOR)  # (local)
        if idx < 0:
            # Fallback: append at end of §19 cross-references (before the trailing "---\n\n## §21"
            # if §20 header drifted) — resolve to the LAST "## §" header start as last resort.
            idx = pre_text.rfind("\n## §")  # (local)
        if idx < 0:
            # Final fallback: append at EOF.
            post_text = pre_text.rstrip() + "\n\n" + row_text  # (local)
        else:
            insert_at = idx + 1  # (local) keep the leading newline with the following header
            post_text = pre_text[:insert_at] + row_text + pre_text[insert_at:]  # (local)
        write_atomic_with_fsync(CORPUS_PATH, post_text)
        inserted = True  # (local)

    # Re-read from disk (the FINAL verification step determines the verdict).
    actual = CORPUS_PATH.read_text(encoding="utf-8")  # (local)
    post_sha = hashlib.sha256(actual.encode("utf-8")).hexdigest()  # (local)

    # Locate the landed §19.2 block (from ROW_ANCHOR to the next top-level "## §" header
    # OR the next "### §19." header, whichever comes first after ROW_ANCHOR).
    row_start = actual.find(ROW_ANCHOR)  # (local)
    block = ""  # (local)
    if row_start >= 0:
        rest = actual[row_start + len(ROW_ANCHOR):]  # (local)
        nxt_top = rest.find("\n## §")  # (local)
        block_end = (row_start + len(ROW_ANCHOR) + nxt_top) if nxt_top >= 0 else len(actual)  # (local)
        block = actual[row_start:block_end]  # (local)

    return {
        "pre_sha": pre_sha,
        "post_sha": post_sha,
        "inserted": inserted,
        "already_present": already_present,
        "row_present": row_start >= 0,
        "block": block,
        "block_line_count": len([ln for ln in block.splitlines() if ln.strip()]),
    }


# ---------------------------------------------------------------------------
# Section 6 — verify content predicates + detector
# ---------------------------------------------------------------------------
def verify_row(block: str, triple: tuple, value_pinned: bool) -> dict:
    """Verify the 4 content predicates + the detector verdict on the landed block."""
    # (i) topological shadow [phi_cd] in Z^3 as Element-1 substrate-IS observable.
    pred_i = (
        ("[φ_cd]" in block or "phi_cd" in block.lower())
        and ("ℤ³" in block or "Z^3" in block or "Z³" in block)
        and ("Element-1" in block)
        and ("topological shadow" in block.lower() or "TOPOLOGICAL SHADOW" in block)
    )  # (local)
    # value-pinned (i): the concrete integer triple appears.
    if value_pinned:
        trip_str = f"({triple[0]}, {triple[1]}, {triple[2]})"  # (local)
        pred_i_value_pinned = (trip_str in block) and ("VALUE-PINNED" in block)  # (local)
    else:
        pred_i_value_pinned = "CHAINED on S93-W2-1" in block  # (local)

    # (ii) analytic shadow mu_cd as physical-content-NOT-bridge-observable.
    pred_ii = (
        ("μ_cd" in block or "mu_cd" in block.lower() or "analytic shadow" in block.lower())
        and ("NOT-bridge-observable" in block or "NOT the cross-pillar-bridge" in block
             or "physical-content-NOT-bridge" in block)
    )  # (local)

    # (iii) weighting-functional family + topological STOPPING rule + K=1 SUGGESTION.
    pred_iii = (
        ("weighting-functional family" in block.lower() or "WEIGHTING-FUNCTIONAL FAMILY" in block
         or "Φ_w" in block)
        and ("topological STOPPING rule" in block or "topological stopping rule" in block.lower())
        and ("base-count" in block.lower())
        and ("K=1 SUGGESTION" in block)
    )  # (local)

    # (iv) two methodology sub-lessons (A + B) in ONE row.
    pred_iv = (
        ("Sub-lesson A" in block)
        and ("Sub-lesson B" in block)
        and ("ONE row" in block or "one row" in block.lower())
    )  # (local)

    # Winding-reconciliation follow-up note present (W2-1 INFO branch).
    pred_winding = (
        ("Winding-reconciliation" in block or "winding-reconciliation" in block.lower())
        and ("N_K" in block)
        and ("K-homology" in block)
        and ("BdG" in block)
        and ("DIFFERENT pairing" in block or "different pairing" in block.lower())
    )  # (local)

    # Detector: canonical_id_complete (family-reaxis AND stopping-rule; NO un-reframed misframe).
    det = detect_weighting_functional_family(block, section_anchor=ROW_ANCHOR)  # (local)
    detector_complete = (not det["canonical_id_incomplete"]) and det["reframe_complete"]  # (local)

    substantive_ok = True  # block_line_count checked in land_corpus_row; >=15 enforced in evaluate

    return {
        "pred_i_topological_shadow_element1": bool(pred_i),
        "pred_i_value_pinned": bool(pred_i_value_pinned),
        "pred_ii_analytic_shadow_scope": bool(pred_ii),
        "pred_iii_weighting_family_stopping_rule": bool(pred_iii),
        "pred_iv_two_sublessons_one_row": bool(pred_iv),
        "pred_winding_reconciliation_note": bool(pred_winding),
        "detector": det,
        "detector_complete": bool(detector_complete),
        "all_four_predicates": bool(pred_i and pred_ii and pred_iii and pred_iv),
    }


def evaluate_gate(land: dict, ver: dict, value_pinned: bool) -> tuple[str, str]:
    """Collapse to PASS/FAIL/INFO + value string (single-shot AFTER-pattern verdict)."""
    fail = (
        (not land["row_present"])
        or (not ver["all_four_predicates"])
        or (not ver["detector_complete"])
        or (land["block_line_count"] < 15)
        or (not ver["pred_winding_reconciliation_note"])
    )  # (local)
    value = (
        f"row_present={land['row_present']};inserted={land['inserted']};"
        f"block_lines={land['block_line_count']};"
        f"pred_i_topo_shadow_E1={ver['pred_i_topological_shadow_element1']};"
        f"pred_i_value_pinned={ver['pred_i_value_pinned']};"
        f"pred_ii_analytic_scope={ver['pred_ii_analytic_shadow_scope']};"
        f"pred_iii_wff_stopping={ver['pred_iii_weighting_family_stopping_rule']};"
        f"pred_iv_two_sublessons_one_row={ver['pred_iv_two_sublessons_one_row']};"
        f"pred_winding_reconciliation={ver['pred_winding_reconciliation_note']};"
        f"detector_complete={ver['detector_complete']};"
        f"canonical_id_incomplete={ver['detector']['canonical_id_incomplete']};"
        f"all_four_predicates={ver['all_four_predicates']};"
        f"phi_cd_value_pinned={value_pinned};K_counter={K_COUNTER_STATUS}"
    )  # (local)
    if fail:
        return "FAIL", value
    if not value_pinned:
        # INFO per plan INFO_meaning: type-pinned row, value-pin CHAINED on W2-1.
        return "INFO", value + ";value_pin=CHAINED-on-S93-W2-1"
    # PASS: row landed with value-pinned [phi_cd], all predicates + detector complete.
    return "PASS", value + ";cf_s93_w1_3_rescope=DISCHARGED"


# ---------------------------------------------------------------------------
# Section 7 — plot (optional per plan; lightweight provenance figure)
# ---------------------------------------------------------------------------
def make_plot(triple: tuple, value_pinned: bool, verdict: str) -> None:
    """Lightweight provenance figure: the module → two-shadow descent + value-pin."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt  # (local)
    except Exception as exc:  # pragma: no cover
        print(f"  (plot skipped: {exc})")
        return
    fig, ax = plt.subplots(figsize=(9, 6))  # (local)
    ax.axis("off")
    trip_str = f"({triple[0]}, {triple[1]}, {triple[2]})" if value_pinned else "(CHAINED on W2-1)"  # (local)
    lines = [
        "§VII.AU CF-37 — Fredholm-module-as-canonical (corpus §19.2)",
        "",
        "CANONICAL = Fredholm module (H_K, D_K(τ_fold=0.190), γ, J)|_(c)∘(d) image",
        "         │",
        "         ├─ index [F_K]  ▶  TOPOLOGICAL shadow  [φ_cd] ∈ ℤ³  = " + trip_str,
        "         │                  (Element-1 substrate-IS observable; VALUE-PINNED, envelope-free Level-2)",
        "         │",
        "         └─ take |D_K|   ▶  ANALYTIC shadow  μ_cd  (physical content; NOT bridge observable)",
        "                            │  contract via Φ_w (weighting-functional family)",
        "                            ▼",
        "             {R_ansatz=3.900e-04, R_CM_full=7.978e-04, R_third=6.960e-06}  (moments)",
        "",
        "Topological STOPPING rule: every Φ_w factors through the SAME finite [φ_cd]",
        "  ⇒ K-counter is a BASE-count, not a fiber-count.  K=1 SUGGESTION.",
        "",
        "Winding-reconciliation (W2-1 INFO): T_signed=0 ≠ N_K=2 (spinor γ_9 balanced 8/8);",
        "  BDI winding lives in a DIFFERENT pairing — (α) rep-side/J-twisted K-homology",
        "  OR (β) BdG-sector winding under χ-inheritance.  Stage-2-style follow-up on SAME triple.",
        "",
        f"Verdict: {verdict}   (CF-S93-W1-3 re-scope DISCHARGED)",
    ]  # (local)
    ax.text(0.02, 0.98, "\n".join(lines), va="top", ha="left", family="monospace", fontsize=8.2)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot written: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 8 — 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


# ---------------------------------------------------------------------------
# Section 9 — Main (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1) Load the W2-1 integer triple (Element-1 value).
    triple, value_pinned, phi_note = load_phi_cd_triple()  # (local)
    print(f"[φ_cd] integer triple = {triple}  (value_pinned={value_pinned})")
    print(f"  {phi_note}")

    # 2) Build the FULL corpus §19.2 row text in memory (AFTER-pattern step 1).
    row_text = build_corpus_row_text(triple, value_pinned)  # (local)

    # 3) write_atomic_with_fsync + re_read + verify (AFTER-pattern steps 2+3).
    land = land_corpus_row(row_text)  # (local)
    print(f"corpus row landed: inserted={land['inserted']} already_present={land['already_present']} "
          f"row_present={land['row_present']} block_lines={land['block_line_count']}")

    # 4) Verify the 4 content predicates + detector on the landed block.
    ver = verify_row(land["block"], triple, value_pinned)  # (local)
    print(f"predicates: i={ver['pred_i_topological_shadow_element1']} "
          f"i_value_pinned={ver['pred_i_value_pinned']} ii={ver['pred_ii_analytic_shadow_scope']} "
          f"iii={ver['pred_iii_weighting_family_stopping_rule']} "
          f"iv={ver['pred_iv_two_sublessons_one_row']} "
          f"winding_note={ver['pred_winding_reconciliation_note']}")
    print(f"detector: {ver['detector']['diagnostic']}")
    print(f"detector_complete={ver['detector_complete']} all_four={ver['all_four_predicates']}")

    # 5) Collapse to verdict (AFTER-pattern step: emit ONCE).
    verdict, value = evaluate_gate(land, ver, value_pinned)  # (local)
    print(f"VERDICT: {verdict}")

    # 6) Input pins + dual-SHA (corpus is now post-write; feeds audit_sha256).
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANONICAL_PATH, pins)  # (local)

    # 7) JSON sidecar (full provenance + 4 content-predicate present-flags + detector verdict).
    sidecar = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "phi_cd_integer_triple": list(triple) if value_pinned else None,
        "phi_cd_value_pinned": value_pinned,
        "phi_cd_note": phi_note,
        "W2_1_audit_sha256": W2_1_AUDIT_SHA,
        "chi_prime_audit_sha": CHI_PRIME_AUDIT_SHA,
        "K_counter_status": K_COUNTER_STATUS,
        "content_predicates": {
            "i_topological_shadow_element1": ver["pred_i_topological_shadow_element1"],
            "i_value_pinned": ver["pred_i_value_pinned"],
            "ii_analytic_shadow_scope_distinction": ver["pred_ii_analytic_shadow_scope"],
            "iii_weighting_functional_family_stopping_rule": ver["pred_iii_weighting_family_stopping_rule"],
            "iv_two_sublessons_one_row": ver["pred_iv_two_sublessons_one_row"],
            "winding_reconciliation_followup_note": ver["pred_winding_reconciliation_note"],
            "all_four_predicates": ver["all_four_predicates"],
        },
        "detector": {
            "has_fiber_count_misframe": ver["detector"]["has_fiber_count_misframe"],
            "has_family_reaxis": ver["detector"]["has_family_reaxis"],
            "has_stopping_rule": ver["detector"]["has_stopping_rule"],
            "reframe_complete": ver["detector"]["reframe_complete"],
            "canonical_id_incomplete": ver["detector"]["canonical_id_incomplete"],
            "severity": ver["detector"]["severity"],
            "diagnostic": ver["detector"]["diagnostic"],
        },
        "corpus_landing": {
            "row_anchor": ROW_ANCHOR,
            "inserted": land["inserted"],
            "already_present": land["already_present"],
            "row_present": land["row_present"],
            "block_line_count": land["block_line_count"],
            "pre_corpus_sha256": land["pre_sha"],
            "post_corpus_sha256": land["post_sha"],
        },
        "canonical_anchors_imported": {
            "M_KK": float(M_KK),
            "M_Pl_reduced": float(M_Pl_reduced),
            "tau_fold": float(tau_fold),
            "Delta_BCS": float(Delta_BCS),
        },
        "cf_rescope": "CF-S93-W1-3 (re-scoped: canonical-identity NOT YET pinned -> module-as-canonical row per corpus §19)",
        "m1_m4_self_classification": {
            "M1_pass_predicate_artifact_existence_plus_detector": True,
            "M2_producing_op_corpus_write_grep_sha_detector": True,
            "M3_source_of_truth_verbatim_corpus_19_closed_S92_workshop": True,
            "M4_allowlist_membership": "REQUIRES ORCHESTRATOR APPEND (orchestrator-only edit per recursion-attack closure)",
        },
        "input_pins": pins,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "elapsed_s": round(time.time() - t0, 3),
    }  # (local)
    OUT_JSON.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"  JSON sidecar written: {OUT_JSON.name}")

    # 8) Plot (optional per plan).
    make_plot(triple, value_pinned, verdict)

    # 9) Emit ONE verdict line (single-shot AFTER-pattern; no conditional rewrite).
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  verdict appended: {VERDICT_TXT.name}")

    # 10) 4-tuple as final non-verdict line.
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    print(f"[done in {time.time() - t0:.2f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
