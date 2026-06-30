#!/usr/bin/env python3
"""
S103 W1-5 S103-B2-ISOBREAK-REGISTRY-LANDING — §VII.BY B2 second-order isotropy-BREAKING companion entry
======================================================================================================

Gate: S103-B2-ISOBREAK-REGISTRY-LANDING ([AUDIT])
  Single-shot AFTER-pattern bridge-landing of the §VII.BY registry entry: the B2 (1,1)-fiber band
  second-order (O(ε²)) isotropy-BREAKING companion of §VII.BR Corollary U, citing the NOW-PATCHED
  Release-condition-R order-class clause (CF-S103-VIIBR-ORDER-CLAUSE-PATCH = PASS, verdict :64).

Pre-registered threshold (artifact-existence + content-marker; per plan §W1-5):
  PASS ⟺ (§VII.BY section present) ∧ (O(ε²) frame-invariant non-Schur-scalar holonomy discriminator
          stated, NOT the literal O(ε) band-matrix anisotropy) ∧ (four witnesses present:
          f_WZ=2.888785e-06, frame_resid=1.776e-15, slope_angle=1.9999, n_broken=4/4) ∧
          (Release-condition-R companion-of-§VII.BR-Corollary-U anchor citing the Item-4 patched clause)
          ∧ (LC-lineage-conditional caveat carried) ∧ (5-anatomy/3-level N/A-with-reason) ∧
          verify_section_matches==True.
  PREREQ (orchestrator-verified at dispatch): Item-4 (CF-S103-VIIBR-ORDER-CLAUSE-PATCH) verdict == PASS.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - canonical_constants.py (append-only-extended mid-session; SHA computed at runtime, feeds audit only,
    disclosed per substrate-first-canonical-sourcing.md §(ii.B))
  - computations/session-102/s102_w7_b2_eps2_wz_holonomy.npz (60 keys; PRIMARY witness source; W7-3)
  - sessions/permanent-results-registry.md (pre-write SHA — MUST include the Item-4 patch on §VII.BR)
  - promotion_text span (the appended §VII.BY block; HARD-asserted SHA + len)
  - script bytes

Output 4-tuple:
  (value=<landed_VII.BY_section_byte_match...>, scheme=REGISTRY-LANDING-AFTER-PATTERN,
   convention=INTRA-PILLAR-STRUCTURAL-THEOREM-...-COMPANION-OF-VIIBR-COROLLARY-U..., L_max=10)

Classification: GEOMETRIC (B2-band second-order isotropy breaking on the (1,1)-fiber; spectral-triple
band geometry, intra-pillar companion of §VII.BR Corollary U; re-derives NOTHING — consumes the
W7-3 npz witnesses).

METHODOLOGY
-----------
build_promotion_text (FULL §VII.BY body) → write_atomic_with_fsync (binary append, no flatten) →
re_read + verify_section_matches → exactly ONE emit_verdict payload. The witnesses are pre-computed
in s102_w7_b2_eps2_wz_holonomy.npz; this gate REGISTERS the companion entry (no physics compute).
Idempotent via the FROZEN section-header anchor: if §VII.BY already present byte-faithful, re-run is a
NO-OP PASS.

DISCIPLINE
----------
- `from canonical_constants import *`
- String assembly + SHA + file I/O only (CPU, OMP 8).
- AFTER-pattern (registry-landing.md §"Bridge-Landing Script Architecture"): build-in-memory →
  write → re-read+verify → ONE verdict. No conditional rewrite branch.
- Verdict emitted via the `emit_verdict` knowledge-MCP tool (script PRINTS payload; agent calls tool).
- The 64-char closure SHA is computed at runtime from the ordered input-pin map (never hardcoded).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys

_SHARED = os.path.dirname(os.path.abspath(__file__))  # (local)
if _SHARED not in sys.path:
    sys.path.insert(0, _SHARED)

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SHARED_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-103"

SESSION = "S103"                                                  # (local)
GATE_ID = "S103-B2-ISOBREAK-REGISTRY-LANDING"                     # (local)
SCHEME = "REGISTRY-LANDING-AFTER-PATTERN"                         # (local)
CONVENTION = (
    "INTRA-PILLAR-STRUCTURAL-THEOREM-5ANATOMY-3LEVEL-NA-WITH-REASON;"
    "COMPANION-OF-VIIBR-COROLLARY-U;"
    "O-EPS-SQUARED-FRAME-INVARIANT-NON-SCHUR-SCALAR-HOLONOMY-DISCRIMINATOR;"
    "LC-LINEAGE-CONDITIONAL-CAVEAT-CARRIED"
)                                                                 # (local)
L_MAX = 10                                                        # (local)

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
NPZ_WITNESS = COMPUTATIONS_DIR / "session-102" / "s102_w7_b2_eps2_wz_holonomy.npz"  # (local)
CANON = SHARED_DIR / "canonical_constants.py"                     # (local)

OUT_NPZ = SESSION_OUT_DIR / "s103_b2_isobreak_registry_landing.npz"  # (local)

SECTION_HEADER_PREFIX = "### §VII.BY"                             # (local)  frozen anchor
PLAN_PREDICTED_LETTER = "BY"                                      # (local)
DOCUMENTED_FRONTIER = "BX"                                        # (local)

# Plan-pinned witness values (re-verified against the npz at runtime, NOT hardcoded into the text)
W_F_WZ = 2.888785e-06            # (local) published 7-sig-fig form of f_WZ
W_FRAME_RESID = 1.776e-15        # (local) published form of frame_resid
W_SLOPE_ANGLE = 1.9999           # (local) published form of slope_angle (≈ 2)
W_N_BROKEN = 4                   # (local)

INPUT_FILES = [CANON, NPZ_WITNESS, REGISTRY]


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


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


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Letter-scan (header-anchored occupied-set; walk up from frontier)
# ---------------------------------------------------------------------------
def scan_next_free_letter(registry_text: str) -> tuple[str, dict]:
    """Header-line-anchored occupied-set over ## / ### / #### levels; walk up from BX.

    Returns (chosen_letter, diag). Legacy off-sequence anchors (PROP, AAU) are
    occupied tokens, never re-allocated, never frontier (they are NOT in the
    two-letter B-walk band). The walk is over the §VII.{LL} two-letter alphabetic
    sequence starting at the documented frontier §VII.BX → BY → BZ → ...
    """
    import re

    # Occupied two-letter §VII tokens at any header level.
    occ = set()  # (local)
    for m in re.finditer(r"^#{2,4}\s+§VII\.([A-Z]{1,3})\b", registry_text, flags=re.M):
        occ.add(m.group(1))
    # Also count any §VII.LL appearing in the slot-index table rows (header-vs-table drift guard).
    for m in re.finditer(r"\|\s*§VII\.([A-Z]{1,3})\b", registry_text):
        occ.add(m.group(1))

    # Two-letter alphabetic successor walk: B[A..Z], then C[A..Z], ...
    def two_letter_seq(start: str):
        first = ord(start[0]) - ord("A")
        second = ord(start[1]) - ord("A")
        f, s = first, second  # (local)
        while f < 26:
            yield chr(ord("A") + f) + chr(ord("A") + s)
            s += 1  # (local)
            if s >= 26:
                s = 0  # (local)
                f += 1  # (local)

    chosen = None  # (local)
    for cand in two_letter_seq(DOCUMENTED_FRONTIER):
        if cand == DOCUMENTED_FRONTIER:
            continue  # frontier is occupied by definition; start walking ABOVE it
        if cand not in occ:
            chosen = cand
            break
    diag = {
        "documented_frontier": DOCUMENTED_FRONTIER,
        "plan_predicted_letter": PLAN_PREDICTED_LETTER,
        "chosen_letter": chosen,
        "BX_occupied": "BX" in occ,
        "BY_occupied_before_write": "BY" in occ,
        "BZ_occupied": "BZ" in occ,
        "n_occupied_two_letter_tokens": len(occ),
        "legacy_offseq_PROP_occupied": "PROP" in occ,
        "legacy_offseq_AAU_occupied": "AAU" in occ,
    }
    return chosen, diag


# ---------------------------------------------------------------------------
# Section 6 — Promotion-text builder (pure function; FULL §VII.BY body)
# ---------------------------------------------------------------------------
def build_promotion_text(w: dict, landing_audit_head: str) -> str:
    """Assemble the FULL §VII.BY section body in memory. Pure function; no I/O.

    `w` carries the npz-verified witnesses (so the published numbers in the text
    are tied to the artifact, not free-floating). `landing_audit_head` is filled
    after the dual-SHA is computed (so the self-citing 'landing audit' head is
    correct); to keep build pure for the verify step, the body uses the npz
    witness numbers and the §VII.BR closure SHAs, NOT the landing audit (which is
    re-injected via the slot-table row + an explicit Closure-SHA-pin sentence
    pointing at the verdict line).
    """
    f_wz = w["f_WZ_pub"]            # (local)
    fr = w["frame_resid_pub"]       # (local)
    sl = w["slope_angle_pub"]       # (local)
    nb = w["n_broken"]              # (local)
    nsf = w["non_scalar_frac"]      # (local)
    f_wz_full = w["f_WZ_full"]      # (local)
    fr_full = w["frame_resid_full"] # (local)
    sl_full = w["slope_angle_full"] # (local)
    npz_audit = w["npz_audit_sha"]  # (local)

    header = (
        f"{SECTION_HEADER_PREFIX} — Second-Order Isotropy-BREAKING of the B2 (1,1)-Fiber Band: "
        "the Release-Condition-R Companion of §VII.BR Corollary U — U(2) Isotropy Releases via a "
        "Frame-Invariant Non-Abelian (Wilczek–Zee) Holonomy at O(ε²), NOT the Literal O(ε) "
        "Band-Matrix Anisotropy (STAGE-3-PERMANENT intra-pillar GEOMETRIC structural companion "
        "theorem — the discriminator the no-go LICENSES once isotropy breaks; registers the "
        "OUTCOME of the §VII.BR Release-condition-R forward gate [CF-S101-B2-ISOTROPY-BREAKING "
        "→ S102 W7-3]; consumes s102_w7_b2_eps2_wz_holonomy.npz [W7-3 witnesses] — re-derives "
        "NOTHING physical; cites the NOW-PATCHED §VII.BR Release-condition-R order-class clause "
        "[CF-S103-VIIBR-ORDER-CLAUSE-PATCH = PASS]; substrate-physics derivation lineage "
        "berry-geometric-phase-theorist [W7-3 holonomy compute] with the §VII.BR Schur-rigidity "
        "structural frame [gen-physicist S101 W6-6 landing]; S103 W1-5 landing — gen-physicist "
        "orchestrator-direct registry §VII sole-writer for this NCG/geometric structural landing "
        "per `feedback_mack-bridge-role.md` [NOT a §7 falsifier-surface row — mack-cosmic-bridge "
        "does NOT apply]; single-shot AFTER-pattern per `registry-landing.md` §\"Bridge-Landing "
        "Script Architecture\"; slot §VII.BY runtime-verified next-free over ALL header levels "
        "[documented frontier §VII.BX]; 2026-06-10)"
    )

    status = (
        "**Status**: **STAGE-3-PERMANENT** intra-pillar structural companion theorem. The breaking "
        "ORDER and the frame-invariant non-Schur-scalar discriminator are OPERATOR-INDEPENDENT "
        "structural facts (they transfer as-is under either branch of the τ=0 canonicity "
        "adjudication, exactly like the §VII.BR T1/T2/P/U/R clauses): the O(ε²) Schur-complement "
        "order of an off-block coset deformation, the O(ε²) Stokes order of a closed coset loop's "
        "Wilczek–Zee holonomy, and the frame-invariance of the non-Schur-scalar trace are NOT "
        "near-tolerance numerical coincidences at any `L_max`. This entry is the companion of the "
        "STAGE-3-PERMANENT §VII.BR Corollary U; it does NOT open a fresh joint cross-axis theorem "
        "(no new Stage-2 PASS-AND is required), because its structural content is the discriminator "
        "§VII.BR Corollary U ALREADY licenses and the order-class statement it instantiates is the "
        "NOW-PATCHED Release-condition-R clause of the STAGE-3-PERMANENT §VII.BR entry. The witness "
        "NUMBERS are LC-lineage-conditional (inherited verbatim from §VII.BR; see the caveat below). "
        "NO new compute gate: this is a registry-landing of pre-computed sub-results "
        f"(`f_WZ`, `frame_resid`, `slope_angle`, `non_scalar_frac`, `n_broken` in "
        "`s102_w7_b2_eps2_wz_holonomy.npz`), transcribed (binding-text discipline; re-derives "
        "NOTHING physical)."
    )

    classification = (
        "**Result classification**: **GEOMETRIC** (a statement about the fabric's own spectral-triple "
        "band geometry — the B2 (1,1)-fiber band is a Peter-Weyl block of `D_K`, and the U(2) "
        "isotropy it breaks IS the band's own intrinsic symmetry, not an external gauge container). "
        "The observable this entry registers is the C² coset-doublet Wilson-loop holonomy `f_WZ` and "
        "its frame-invariant non-Schur-scalar character under an isotropy-breaking deformation."
    )

    anatomy_class = (
        "**Classification (load-bearing for plan-freeze audit)**: this is an **INTRA-PILLAR STRUCTURAL "
        "COMPANION THEOREM** on the band-geometry axis, the Release-condition-R companion of the "
        "§VII.BR Schur-rigidity complex. It is NOT a cross-pillar convergence bridge: the 5-anatomy "
        "IS-not-IN elements + the 3-level ladder are declared **N/A-with-reason** (there is no "
        "laboratory-IN continuum-image observable and no HKR / K-theory / Connes–Karoubi bridge map "
        "is claimed; the statement is a Schur-complement order-counting + Stokes order-counting + "
        "frame-invariance fact intrinsic to `(A_K, H_K, D_K)` on its own (τ,μ) deformation manifold). "
        "A plan-freeze auditor MUST read it with the §VII.BR / §VII.BV N/A-with-reason structure, NOT "
        "as a convergence bridge (which would HARD-HALT on a non-binding Level-2 per "
        "`cross-pillar-bridge-anatomy.md §\"Level-2 sub-class (binding vs non-binding)\"`)."
    )

    structural_verdict = (
        "**STRUCTURAL VERDICT (the second-order isotropy-breaking discriminator).** Let "
        "`(A_K, H_K, D_K(τ,μ))`, `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`, be the spectral triple on the "
        "U(2)-invariant volume-preserving TT (τ,μ) surface, and let P be the B2 (1,1)-fiber band "
        "projector (a Peter-Weyl block). §VII.BR proved (Corollary U) that on a G-INVARIANT base "
        "**no G-invariant functional of the band geometry distinguishes a genuinely non-Abelian "
        "(Wilczek–Zee) band from a direct sum of `d_α` identical Abelian channels** — the CKH "
        "discriminator requires either (i) invariant band-matrix anisotropy (excluded by T2: "
        "`M_ab ∝ 1`) or (ii) a canonical band-member frame (excluded: the band is an irreducible "
        "G-space; the Abelian sum spans a 670× range over the U(2) gauge orbit while the "
        "non-Abelian trace is invariant to 1.67e-16). **§VII.BR Release condition R** (the "
        "NOW-PATCHED order-class clause, CF-S103-VIIBR-ORDER-CLAUSE-PATCH) states that under an "
        "isotropy-breaking deformation `H + ε·δH` with `[ρ(g),δH] ≠ 0`, the onset ORDER in ε is set "
        "by the deformation class: an **in-block** δH (non-Schur-scalar in-band part `P·δH·P ≠ 0`) "
        "splits the band at **O(ε)** (open linear response), whereas an **off-block** δH (the "
        "substrate-natural C²-coset directions λ₄..λ₇, for which `P·δH·P ≡ 0` so `C₁ = 0` is "
        "STRUCTURAL not fine-tuned) develops its anisotropy at **O(ε²)** via the second-order "
        "Schur-complement term, AND the **closed-loop** Wilczek–Zee holonomy `∮A_coset` around a "
        "coset loop of radius ε is a DISTINCT object whose **O(ε²)** order is fixed by Stokes "
        "(curvature flux ∝ enclosed loop-area ∝ ε²) independent of abelian/non-abelian character — "
        "its discriminating content for genuine WZ structure being the **frame-invariant "
        "non-Schur-scalar trace** (`non_scalar_frac → 1`), NOT the ε-order. **This entry registers "
        "the OUTCOME on the substrate's off-block realization (W7-3, the C² coset doublet of the B2 "
        "(1,1)-fiber band):** the discriminator object is the **O(ε²) frame-invariant non-Schur-scalar "
        f"Wilczek–Zee holonomy** `f_WZ`, and it is genuinely NON-ABELIAN. The four witnesses "
        f"(`s102_w7_b2_eps2_wz_holonomy.npz`, audit `{npz_audit[:16]}…`):"
    )

    witness_table = (
        "\n\n"
        "| Witness | npz key | Value | Reading |\n"
        "|:--------|:--------|:------|:--------|\n"
        f"| Holonomy magnitude (converged) | `f_WZ` | {f_wz} (full {f_wz_full!r}; `conv_fwz` over n_loop ∈ {{256,512,1024,2048}}) | the non-abelian Wilson-loop holonomy on the C² coset doublet is nonzero |\n"
        f"| Frame-invariance residual | `frame_resid` | {fr} (full {fr_full!r}; spread over 8-sample Haar U(2) frames, `frame_invariant_ok=True`) | the holonomy is frame-INVARIANT to 15 decades — NOT a gauge artifact of the `eigh` intra-eigenspace rotation (contrast the §VII.BR Abelian-sum, which spans 670× over the U(2) orbit) |\n"
        f"| Holonomy ANGLE log-log slope in ε | `slope_angle` | {sl} (full {sl_full!r}; `angle_scan` over ε ∈ {{1e-4…1e-2}}) | the holonomy ANGLE ∝ ε^{{{sl}}} ≈ ε² — the breaking is a SECOND-order effect in ε (the closed-loop O(ε²) Stokes order) |\n"
        f"| Non-Schur-scalar fraction | `curv_nonscalar` | {nsf} | the curvature content is genuinely non-Schur-scalar (non-abelian discriminator → 1) |\n"
        f"| Broken U(2) generators | `n_broken` | {nb}/4 (`stab_idx=[0,1,2,7]`, `dim_band=4`) | all four U(2)-isotropy generators release — the isotropy breaks isotropically on the full band |\n"
    )

    chain = (
        "\n\n"
        "**SUBSTITUTION CHAIN (the order + non-Schur-scalar claim).**\n\n"
        "Claim: \"The B2 (1,1)-fiber band breaks U(2) isotropy at **O(ε²)** via a non-trivial "
        "non-abelian (Wilczek–Zee) holonomy — a frame-invariant non-Schur-scalar discriminator — NOT "
        "the literal **O(ε)** band-matrix anisotropy of the §VII.BR Release-condition-R generic case.\"\n\n"
        "- **Def 1**: ε := isotropy-breaking deformation amplitude (§VII.BR Release-condition-R; the "
        "Item-4-patched clause now states in-block O(ε) vs off-block/closed-loop O(ε²) order classes).\n"
        "- **Def 2**: `f_WZ(ε)` := the frame-invariant non-abelian Wilson-loop holonomy on the C² "
        f"coset doublet of the B2 (1,1)-fiber band. npz: `f_WZ`={f_wz}, `frame_resid`={fr} ⇒ "
        "`frame_invariant_ok=True`.\n"
        "- **Def 3**: `slope_angle` := the log-log slope of the holonomy angle vs ε (the ORDER of the "
        f"holonomy in ε); npz `slope_angle`={sl}. `non_scalar_frac` := the fraction of band-matrix "
        f"content NOT Schur-scalar; npz `curv_nonscalar`={nsf}. `n_broken` := number of U(2)-isotropy "
        f"generators broken; npz `n_broken`={nb}/4.\n"
        f"- **Substitute**: `slope_angle`={sl} ⇒ `f_WZ ∝ ε^{{{sl}}} ≈ ε²` (a SECOND-order effect in ε); "
        f"`frame_resid`={fr} ⇒ the holonomy is frame-INVARIANT to 15 decades (NOT a gauge artifact of "
        "the `eigh` intra-eigenspace rotation, unlike the §VII.BR Abelian-sum which spans 670× over "
        f"the U(2) orbit); `n_broken`={nb}/4 ⇒ all four U(2) generators release.\n"
        "- **Simplify**: the discriminator object is the **O(ε²) frame-invariant non-Schur-scalar "
        f"holonomy** `f_WZ` (`curv_nonscalar`={nsf}), which is PRECISELY the §VII.BR Corollary U "
        "discriminator that the no-go LICENSES once isotropy breaks (the Release-condition-R "
        "\"anisotropy iff genuine within-band Wilczek–Zee structure exists\").\n"
        f"- **Canonical form**: `ord(B2 isotropy breaking via WZ holonomy) = 2` (O(ε²)); the "
        "discriminator is frame-invariant non-Schur-scalar (`non_scalar_frac → 1`), DISTINCT from the "
        "generic O(ε) in-block band-matrix anisotropy.\n"
        "- **Direction**: the B2 breaking is **HIGHER order** (O(ε²) holonomy) than the generic "
        "in-block anisotropy (O(ε)); the discriminator that licenses the genuine non-abelian reading "
        "is the **frame-invariant holonomy**, NOT the literal O(ε) band-matrix anisotropy (which "
        "§VII.BR Corollary U showed is gauge-ambiguous in an exactly-degenerate band). Hence this "
        "companion entry states the discriminator as the **O(ε²) frame-invariant non-Schur-scalar "
        "holonomy**, citing the Item-4-patched order-class clause.\n"
        "- **Conclusion**: the B2 second-order isotropy-BREAKING entry IS the Release-condition-R "
        f"companion of §VII.BR Corollary U; discriminator = O(ε²) frame-invariant non-abelian WZ "
        f"holonomy (`f_WZ`={f_wz}, `frame_resid`={fr}, `slope_angle`={sl}, `n_broken`={nb}/4). ∎ "
        "(W7-3 compute + the S-4-reconciled / Item-4-patched §VII.BR clause; this gate REGISTERS the "
        "companion entry.)"
    )

    refinement = (
        "\n\n"
        "**Refinement sub-row (non-blocking; S103 W7-3 → W3 coupling).** The orthogonal C² coset "
        "doublet `[3,5]` (the `next_pair` recorded in the W7-3 npz) was independently landed PASS "
        "this session as `S103-B2-WZ-HOLONOMY-COSET2` (verdict in "
        "`computations/session-103/s103_gate_verdicts.txt`, audit `49705bbc…`): `f_WZ([3,5]) = "
        "2.888785e-06` matching the first doublet to 4 sig figs, `angle_slope = 1.9999`, "
        "`frame_resid = 2.665e-15`, `non_scalar_frac = 1.0`, `n_broken = 4`. Together the two "
        "doublets show the C² coset span is COMPLETE and the isotropy-breaking is non-abelian on the "
        "FULL coset, isotropically. The PRIMARY citation of THIS entry remains the S-4-reconciled / "
        "Item-4-patched §VII.BR Release-condition-R clause + the W7-3 first-doublet result per the "
        "plan; the COSET2 result is a confirming refinement, NOT a co-primary anchor."
    )

    anatomy_block = (
        "\n\n"
        "**REGISTRY-ANATOMY COMPLIANCE.** (i) Entry class = **intra-pillar structural companion "
        "theorem** (single-axis GEOMETRIC; the companion of the STAGE-3-PERMANENT §VII.BR Corollary "
        "U). This is **NOT a cross-pillar bridge**, so the 5-anatomy IS-not-IN elements + the 3-level "
        "ladder are declared **N/A-with-reason**: there is no laboratory-IN observable and no HKR / "
        "K-theory / Connes–Karoubi bridge map is claimed (an order-counting + frame-invariance fact "
        "intrinsic to `(A_K, H_K, D_K)`); the \"Level-3 < Level-2\" registry-PASS inequality is "
        "vacuously N/A (no continuum-image envelope). The Level-2 sub-class question does not arise "
        "(NON-BINDING by N/A-with-reason). (ii) Projection-side = **SINGLE-READING, "
        "operator/projector-side**: the entry quantifies over G-invariant FUNCTIONALS of the band "
        "projector `P` and its coset-loop holonomy (a Corollary-U-class statement), so the bare slot "
        "`§VII.BY` (no `.OP-PROJ`/`.STATE-PROJ` suffix) is admissible under `registry-landing.md` "
        "Reading-A naming hygiene precisely because this explicit single-reading sentence is carried; "
        "no state-pair functional clause exists. (iii) No state-history labels in the entry text "
        "(Class-(h) parse-tree N/A; \"Bogoliubov\" does not appear). (iv) Substrate-IS level tag = "
        "**Level 2** (moduli-deformation per `phononic-framing.md §\"Single-τ-slice vs "
        "moduli-deformation substrate-IS levels\"`): the base B is the substrate's OWN (τ,μ) "
        "deformation manifold on the U(2)-invariant volume-preserving TT surface — not a coordinate "
        "container; the ε-deformation is the substrate's own intrinsic isotropy-breaking direction. "
        "Companion-orthogonality: §VII.BY is a STRUCTURAL-ORTHOGONAL-COMPANION of §VII.BR (the no-go "
        "Corollary U at G-INVARIANT base; §VII.BY is what happens when isotropy BREAKS) — the two are "
        "NOT cross-corner co-primary (both are operator/projector-side, Corner-I algebra-INVARIANT "
        "band-geometry functionals; co-primary across them is not asserted — §VII.BR is the licensing "
        "no-go, §VII.BY is the licensed discriminator's OUTCOME)."
    )

    lineage = (
        "\n\n"
        "**Lineage caveat (MANDATORY; inherited verbatim from §VII.BR).** The witness NUMBERS are "
        "**LC-lineage-conditional**: the consumed s84 spectrum-cache lineage sits at the Levi-Civita "
        "torsion point `t = 1/2` of the Lai–Teh family (W6-2 UNTRUSTED-UPSTREAM caveat; operator "
        "CANONICITY under Q1-workshop adjudication, numerical validity control-verified at machine "
        "epsilon). The split this text preserves, exactly as §VII.BR does: the **STRUCTURAL "
        "content** — the Schur-complement O(ε²) order of an off-block coset deformation, the Stokes "
        "O(ε²) order of the closed coset-loop holonomy, the frame-invariance of the non-Schur-scalar "
        "trace, and the Corollary-U companion relation — is **OPERATOR-INDEPENDENT** (it uses only "
        "(E1)-equivariance, functional calculus, and the off-block `P·δH·P ≡ 0` structure, none of "
        "which reference the torsion point; it transfers as-is under EITHER branch of the τ=0 "
        "canonicity adjudication). The **specific witness NUMBERS** (`f_WZ = 2.888785e-06`, "
        "`frame_resid = 1.776e-15`, `slope_angle = 1.9999`, `n_broken = 4/4`, and the COSET2 values) "
        "are **LC-lineage-conditional** and would be recomputed under a re-adjudicated operator. The "
        "order distinction is operator-INDEPENDENT and adds NO new LC-lineage-conditional number "
        "beyond those already recorded at S101 W5-4 and S102 W7-3."
    )

    substrate_framing = (
        "\n\n"
        "**Substrate framing** (`phononic-framing.md §\"IS Space, Not IN Space\"`). The substrate IS "
        "the spectral-triple band geometry; the B2 (1,1)-fiber band is a Peter-Weyl block of `D_K` "
        "and the U(2) isotropy is the band's OWN intrinsic symmetry. **Direction**: `D_K (1,1)-fiber "
        "band-projector families → the C² coset-doublet Wilson-loop holonomy f_WZ under an "
        "isotropy-breaking deformation → the O(ε²) frame-invariant non-abelian (Wilczek–Zee) "
        "discriminator → U(2) isotropy breaks (n_broken=4/4)`. §VII.BR proved that on a G-INVARIANT "
        "base no invariant distinguishes abelian from non-abelian; this entry registers what happens "
        "when isotropy BREAKS — the frame-invariant holonomy (NOT the gauge-ambiguous Abelian-sum) "
        "becomes the genuine discriminator. The breaking is intrinsic to the fabric's own deformation "
        "manifold, not a measurement IN a container. **FORBIDDEN inversion (container thinking)**: "
        "\"the B2 band sits in an external U(2) gauge space that breaks\" → INVERT: the U(2) isotropy "
        "IS the band's own intrinsic symmetry; the deformation breaks it from within, and the "
        "frame-invariant holonomy is the substrate's own discriminator. The discriminator is stated "
        "as the **O(ε²) frame-invariant non-Schur-scalar holonomy** (`non_scalar_frac → 1`), citing "
        "the Item-4-disambiguated §VII.BR Release-condition-R clause — NOT the literal \"O(ε) "
        "band-matrix anisotropy\" (which §VII.BR Corollary U showed is gauge-ambiguous in an "
        "exactly-degenerate band)."
    )

    provenance = (
        "\n\n"
        "**Provenance.** PRIMARY = the NOW-PATCHED §VII.BR Release-condition-R order-class clause "
        "(`CF-S103-VIIBR-ORDER-CLAUSE-PATCH` PASS, verdict-line audit "
        "`a57f5be0f2e4b50be821081e8d113b3124f7621a42262178426ae732f5115880` in "
        "`computations/session-103/s103_gate_verdicts.txt`; the patched §VII.BR span SHA "
        "`5d37b1004e6fff0fe3be46465b0837589a98bea612cfc2ef9358a856c0810c1d`) + the W7-3 first-doublet "
        f"witnesses in `computations/session-102/s102_w7_b2_eps2_wz_holonomy.npz` (audit_sha256 "
        f"`{npz_audit}`; `f_WZ`/`frame_resid`/`slope_angle`/`curv_nonscalar`/`n_broken` "
        "VALUES authoritative — NOT re-adjudicated; the frame-invariance + non-Schur-scalar readings "
        "are RE-VERIFIED here from the npz at landing). Companion anchor: §VII.BR Schur-Rigidity "
        "Structural Theorem (Corollary U + Release condition R; STAGE-3-PERMANENT, audit `6c53304a`). "
        "Confirming refinement: `S103-B2-WZ-HOLONOMY-COSET2` PASS (audit `49705bbc…`; orthogonal "
        "`[3,5]` coset doublet, C² span complete). Upstream lineage: `S101-B2-ISOTROPY-BREAKING` "
        "INFO (W5-4; `B2split_slope=2.0000`, `OmegaD/Omegac=2.0`) — the §VII.BR Release-condition-R "
        "forward gate. NO compute gate — registry-landing of pre-computed sub-results (binding-text "
        "discipline; the O(ε²) holonomy + frame-invariance + non-Schur-scalar character are the W7-3 "
        "compute OUTCOME, the order-class structure is the §VII.BR theorem). §VII.BY slot verified "
        "next-free at runtime via the all-header-level append-protocol scan (documented frontier "
        "§VII.BX). This is a §VII NCG/geometric structural-theorem landing, NOT a §7 falsifier-surface "
        "row — mack-cosmic-bridge sole-writer does NOT apply (`feedback_mack-bridge-role.md`). "
        "canonical_constants.py was append-only-extended mid-session; its SHA is computed at runtime "
        "and feeds audit_sha256 only (no stale pin; disclosed per "
        "`substrate-first-canonical-sourcing.md §(ii.B)`)."
    )

    closure = (
        "\n\n"
        "**Closure SHA pin** (over the ordered input-pin map): the full dual-SHA "
        "(audit_sha256 / content_sha256) is on the `S103-B2-ISOBREAK-REGISTRY-LANDING` verdict line "
        f"in `computations/session-103/s103_gate_verdicts.txt` (landing audit head `{landing_audit_head}`); "
        "registry_pre_write_file_sha256, witness_npz_sha256, and the §VII.BR Release-condition-R "
        "patched-span SHA are pinned in the companion comment rows."
    )

    body = (
        header
        + "\n\n"
        + status
        + "\n\n"
        + classification
        + "\n\n"
        + anatomy_class
        + "\n\n"
        + structural_verdict
        + witness_table
        + chain
        + refinement
        + anatomy_block
        + lineage
        + substrate_framing
        + provenance
        + closure
        + "\n"
    )
    return body


def build_slot_table_row(landing_audit_head: str) -> str:
    """One slot-index-table row matching the §VII.BX row shape (adjacent to BX at :160)."""
    return (
        "| §VII.BY | THM | Second-Order Isotropy-BREAKING of the B2 (1,1)-Fiber Band — the "
        "Release-condition-R companion of §VII.BR Corollary U: off-block C²-coset deformation "
        "develops anisotropy at `O(ε²)` (Schur-complement; C₁=0 STRUCTURAL) and the closed-loop "
        "Wilczek–Zee holonomy `f_WZ=2.888785e-06` is frame-invariant (`frame_resid=1.776e-15`) "
        "non-Schur-scalar (`non_scalar_frac→1`), `slope_angle=1.9999≈2`, `n_broken=4/4` — U(2) "
        "isotropy releases isotropically; discriminator = the O(ε²) frame-invariant non-Schur-scalar "
        "holonomy, NOT the literal O(ε) band-matrix anisotropy, STAGE-3-PERMANENT "
        f"(S103 W1-5 landing audit {landing_audit_head}…, intra-pillar GEOMETRIC companion; consumes "
        "s102_w7_b2_eps2_wz_holonomy.npz [W7-3] — re-derives NOTHING; cites the NOW-PATCHED §VII.BR "
        "Release-condition-R order-class clause CF-S103-VIIBR-ORDER-CLAUSE-PATCH PASS a57f5be0…; "
        "STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BR [Corollary U no-go at G-invariant base; §VII.BY = "
        "the licensed discriminator's OUTCOME when isotropy breaks]; confirming refinement "
        "S103-B2-WZ-HOLONOMY-COSET2 PASS 49705bbc [orthogonal [3,5] coset, C² span complete]; "
        "5-anatomy + 3-level N/A-with-reason; Level-2 moduli-deformation (τ,μ); LC-lineage-conditional "
        "witnesses inherited from §VII.BR; section body at §VII.BY) | gen-physicist | 2026-06-10 |"
    )


# ---------------------------------------------------------------------------
# Section 7 — Atomic write + re-read verify
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(path: Path, new_bytes_full: bytes) -> None:
    """Write the FULL new file bytes atomically (temp + fsync + os.replace)."""
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with open(tmp, "wb") as f:
        f.write(new_bytes_full)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def verify_section_matches(actual_text: str, expected_section: str) -> bool:
    """The expected §VII.BY section is present in the file byte-faithfully."""
    return expected_section in actual_text


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload printer
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (pre-write registry SHA; npz; canonical)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1a. Verify the Item-4 patch is materially present in the registry (prereq sanity, not a clause).
    registry_text = REGISTRY.read_text(encoding="utf-8")  # (local)
    item4_markers_present = (
        ("Release condition R" in registry_text)
        and ("splits the band at **O(ε)**" in registry_text)
        and ("**O(ε²)**" in registry_text)
        and ("frame-invariant non-Schur-scalar trace" in registry_text)
    )  # (local)
    print(f"  Item-4 patch materially present in §VII.BR Release-condition-R: {item4_markers_present}")

    # 2. Load the W7-3 witnesses; re-verify against the plan-pinned published forms.
    d = np.load(NPZ_WITNESS, allow_pickle=True)  # (local)
    f_wz_full = float(d["f_WZ"])             # (local)
    frame_resid_full = float(d["frame_resid"])  # (local)
    slope_angle_full = float(d["slope_angle"])  # (local)
    n_broken = int(d["n_broken"])            # (local)
    non_scalar_frac = float(d["curv_nonscalar"])  # (local)
    frame_invariant_ok = bool(d["frame_invariant_ok"])  # (local)
    npz_audit_sha = str(d["audit_sha256"])   # (local)

    # Witness consistency checks (the published forms the §VII.BY text uses must match the npz).
    chk_fwz = abs(f_wz_full - W_F_WZ) <= 5e-12          # (local) 7-sig-fig form
    chk_fr = abs(frame_resid_full - W_FRAME_RESID) <= 1e-17  # (local)
    chk_slope = abs(slope_angle_full - W_SLOPE_ANGLE) <= 1e-3  # (local) ≈2 to 4 sig figs
    chk_nb = n_broken == W_N_BROKEN                     # (local)
    chk_nsf = abs(non_scalar_frac - 1.0) <= 1e-9        # (local) non_scalar_frac → 1
    witnesses_ok = (
        chk_fwz and chk_fr and chk_slope and chk_nb and chk_nsf and frame_invariant_ok
    )  # (local)
    print(
        f"  witnesses: f_WZ={f_wz_full:.6e}(ok={chk_fwz}) frame_resid={frame_resid_full:.3e}(ok={chk_fr}) "
        f"slope_angle={slope_angle_full:.4f}(ok={chk_slope}) n_broken={n_broken}(ok={chk_nb}) "
        f"non_scalar_frac={non_scalar_frac:.6f}(ok={chk_nsf}) frame_invariant_ok={frame_invariant_ok}"
    )
    assert witnesses_ok, "npz witnesses do not match the plan-pinned published forms"

    # 3. Letter-scan (header-anchored; walk up from documented frontier §VII.BX).
    chosen_letter, scan_diag = scan_next_free_letter(registry_text)
    print(f"  letter-scan: {scan_diag}")
    slot_collision = chosen_letter != PLAN_PREDICTED_LETTER  # (local)
    if slot_collision:
        print(
            f"  !! SLOT COLLISION: plan predicted §VII.{PLAN_PREDICTED_LETTER} but next-free is "
            f"§VII.{chosen_letter} — FAIL-with-remediation"
        )

    # 4. Compute the dual-SHA over (script + canonical + pinmap) — this is the landing audit.
    #    The promotion text uses the npz witnesses + §VII.BR SHAs (NOT the landing audit, kept pure),
    #    re-injecting only the audit HEAD into a self-pointer sentence + the slot-table row.
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    landing_audit_head = audit_sha[:16]  # (local)

    # 5. Build the FULL §VII.BY section + the slot-table row (pure functions).
    w = {
        "f_WZ_pub": W_F_WZ,
        "frame_resid_pub": W_FRAME_RESID,
        "slope_angle_pub": W_SLOPE_ANGLE,
        "n_broken": n_broken,
        "non_scalar_frac": non_scalar_frac,
        "f_WZ_full": f_wz_full,
        "frame_resid_full": frame_resid_full,
        "slope_angle_full": slope_angle_full,
        "npz_audit_sha": npz_audit_sha,
    }  # (local)
    section_text = build_promotion_text(w, landing_audit_head)  # (local)
    slot_row = build_slot_table_row(landing_audit_head)         # (local)
    section_span_sha = sha256_text(section_text)                # (local)
    print(f"  §VII.BY section span SHA: {section_span_sha[:16]}... ({len(section_text)} chars)")

    # 6. Idempotency: if §VII.BY header already present, NO-OP (re-run safety).
    already_present = SECTION_HEADER_PREFIX in registry_text  # (local)

    verdict = "FAIL"  # (local) default; flips to PASS only on clean verify
    if slot_collision:
        # FAIL-with-remediation; do NOT write to a colliding slot.
        value = (
            f"SLOT-COLLISION_plan_predicted_VII.{PLAN_PREDICTED_LETTER}_runtime_next_free_"
            f"VII.{chosen_letter}_remediation_reauthor_to_VII.{chosen_letter}"
        )  # (local)
        verify_ok = False  # (local)
        slot_row_inserted = False  # (local)
        section_appended = False  # (local)
    elif already_present:
        # Idempotent re-run: verify the section is byte-faithful, emit PASS NO-OP.
        verify_ok = verify_section_matches(registry_text, section_text)  # (local)
        slot_row_inserted = ("| §VII.BY | THM |" in registry_text)  # (local)
        section_appended = False  # (local)  no new write
        if verify_ok and slot_row_inserted:
            verdict = "PASS"
            value = (
                f"landed_VII.BY_section_byte_match_True_IDEMPOTENT-NOOP_"
                f"slot_row_present_True_letter=BY"
            )  # (local)
        else:
            value = (
                f"VII.BY_header_present_but_section_byte_match={verify_ok}_"
                f"slot_row_present={slot_row_inserted}_NEEDS-REMEDIATION"
            )  # (local)
    else:
        # Fresh landing: (a) insert the slot-table row adjacent to the BX row;
        #                (b) append the §VII.BY section at end-of-file.
        bx_row_marker = "| §VII.BX | THM |"  # (local)
        lines = registry_text.split("\n")  # (local)
        bx_idx = None  # (local)
        for i, ln in enumerate(lines):
            if ln.startswith(bx_row_marker):
                bx_idx = i
                break
        assert bx_idx is not None, "BX slot-table row not found (header-vs-table anchor)"
        # Insert BY row immediately AFTER the BX row.
        lines.insert(bx_idx + 1, slot_row)
        registry_with_row = "\n".join(lines)  # (local)
        slot_row_inserted = True  # (local)

        # Append the §VII.BY section at end-of-file (clean tail-append; preserve trailing newline state).
        sep = "" if registry_with_row.endswith("\n") else "\n"  # (local)
        new_full = registry_with_row + sep + "\n" + section_text  # (local)
        write_atomic_with_fsync(REGISTRY, new_full.encode("utf-8"))
        section_appended = True  # (local)

        # Re-read + verify (the SINGLE verification step that determines the verdict).
        actual = REGISTRY.read_text(encoding="utf-8")  # (local)
        verify_ok = (
            verify_section_matches(actual, section_text)
            and ("| §VII.BY | THM |" in actual)
            and (slot_row in actual)
        )  # (local)
        if verify_ok:
            verdict = "PASS"
            value = (
                f"landed_VII.BY_section_byte_match_True_slot_row_inserted_True_"
                f"letter=BY_frontier=BX_fWZ=2.888785e-06_frame_resid=1.776e-15_"
                f"slope_angle=1.9999_n_broken=4of4_nonscalar=1.0_"
                f"discriminator=O(eps2)-frame-invariant-non-Schur-scalar-holonomy_"
                f"companion-of-VIIBR-CorollaryU_Item4-patch-PASS_section_span_sha={section_span_sha[:16]}"
            )  # (local)
        else:
            value = (
                f"verify_section_matches=False_assembly_bug_"
                f"header_present={SECTION_HEADER_PREFIX in actual}_"
                f"slot_row_present={'| §VII.BY | THM |' in actual}"
            )  # (local)

    # 7. Persist the landing record (npz sidecar).
    SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        chosen_letter=chosen_letter,
        plan_predicted_letter=PLAN_PREDICTED_LETTER,
        documented_frontier=DOCUMENTED_FRONTIER,
        slot_collision=slot_collision,
        already_present=already_present,
        section_appended=section_appended,
        slot_row_inserted=slot_row_inserted,
        verify_ok=verify_ok,
        item4_patch_present=item4_markers_present,
        f_WZ=f_wz_full,
        frame_resid=frame_resid_full,
        slope_angle=slope_angle_full,
        n_broken=n_broken,
        non_scalar_frac=non_scalar_frac,
        frame_invariant_ok=frame_invariant_ok,
        witnesses_ok=witnesses_ok,
        npz_witness_audit_sha=npz_audit_sha,
        registry_pre_write_sha=pins.get("sessions/permanent-results-registry.md", ""),
        section_span_sha=section_span_sha,
        section_len=len(section_text),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scan_diag=json.dumps(scan_diag),
    )
    print(f"  sidecar written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 8. Emit 4-tuple + verdict payload (exactly one).
    tag = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
    print(tag)

    extra_rows = [
        f"# §VII.BY landing: companion-of-§VII.BR-Corollary-U; discriminator=O(ε²) frame-invariant "
        f"non-Schur-scalar holonomy (NOT literal O(ε) band-matrix anisotropy); witnesses "
        f"f_WZ=2.888785e-06 frame_resid=1.776e-15 slope_angle=1.9999 n_broken=4/4 non_scalar_frac→1 "
        f"(s102_w7_b2_eps2_wz_holonomy.npz audit {npz_audit_sha[:16]}…; LC-lineage-conditional)",
        f"# Item-4 prereq: CF-S103-VIIBR-ORDER-CLAUSE-PATCH PASS (verdict :64, audit a57f5be0…); "
        f"patched §VII.BR Release-condition-R order-class clause materially present={item4_markers_present}; "
        f"normal AFTER-pattern path (mechanical-closure branch NOT applicable)",
        f"# §VII.BY slot runtime-verified next-free over ALL header levels (documented frontier §VII.BX; "
        f"legacy off-seq PROP/AAU treated as occupied, not frontier); section_span_sha={section_span_sha[:16]}…; "
        f"section_len={len(section_text)}; registry_pre_write_sha={pins.get('sessions/permanent-results-registry.md','')[:16]}…; "
        f"canonical_constants.py SHA computed at runtime, feeds audit only (substrate-first-canonical-sourcing.md §(ii.B))",
        f"# refinement (non-blocking): S103-B2-WZ-HOLONOMY-COSET2 PASS (audit 49705bbc…; orthogonal [3,5] "
        f"coset doublet, C² span complete, isotropy breaks isotropically); PRIMARY citation remains the "
        f"S-4-reconciled/Item-4-patched §VII.BR clause + W7-3 first doublet (NOT co-primary)",
    ]  # (local)

    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
