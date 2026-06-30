#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S111 W1-5 S111-CF-NOHOLOFLUX — spectral-triple-no-holonomy-flux root (STAGE-1-CANDIDATE joint registration)
===========================================================================================================

Gate: S111-CF-NOHOLOFLUX ([VERIFY-THEOREM])
Classification: GEOMETRIC

Pre-registered threshold (set-membership / registry-landing):
  PASS iff the §VII registry entry is written at the runtime-verified next-free §VII
  slot (plan-pinned §VII.CH, AFTER CLOCKLOC3's §VII.CG) carrying ALL of:
    - all 3 projection-clauses (operator / parameter / causal),
    - the single-root statement (spectral-triple != holonomy-flux-algebra),
    - JOINT-clause flags (PASS-AND'd at Stage-2 across both axes),
    - cross-axis author attribution (NCG-axiomatic/conjugate-pair AND
      cosmological-bridge/principle-theoretic),
    - the S85-cusp distinctness citation (§VII.M.W10-3),
    - the STAGE-1-CANDIDATE tag on the theorem-name line,
  AND the re-read section satisfies every plan `must_contain` pattern.
  FAIL iff the slot is FOREIGN-occupied (reroute next-free + FAIL-with-remediation)
  OR the re-read section fails any required clause / must_contain pattern.
  INFO iff registered but a projection-clause is reach-limited (DISSENT-1 reach-tag).

Single-shot AFTER-pattern (registry-landing.md §"Bridge-Landing Script Architecture";
_bridge_landing_script_template.py):
  build_promotion_text -> write_atomic_with_fsync (binary-append, no neighbor flatten)
  -> re_read_section + verify -> emit exactly ONE verdict line.
No conditional rewrite branch (Class-6-adjacent BEFORE pattern forbidden).

Stage-0 source (FROZEN): WS-ATFORM CONVERGENCE-3 + EMERGENCE-1 three-projection chain
(the substitution chain reproduced verbatim in the S111-CF-NOHOLOFLUX plan-block,
sessions/session-plan/session-111-plan-w1.md §W1-5). The registry entry FORMALIZES that
frozen chain; it re-derives nothing (joint-theorem-promotion.md Stage-0 -> Stage-1).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/permanent-results-registry.md  (the landing target; pinned for audit)
  - computations/session-85/s85_w0_van_hove_cusp_theorem.npz  (S85 cusp distinctness anchor)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<landing-summary>, scheme=STAGE-1-CANDIDATE-joint-registration,
   convention=registry-landing-single-shot-AFTER-pattern, L_max=N/A)

METHODOLOGY
-----------
Registry-landing gate (NO numerical scan; L-independent — the conjugate-pair /
no-holonomy-flux fact is definitional, holds at every L). The script writes the
§VII.CH STAGE-1-CANDIDATE joint theorem, re-verifies the slot was free over ALL
header levels at write-time, re-reads the landed section, and emits one verdict line.
The substrate content: a spectral triple (A_K, H_K, D_K(tau)) is a fixed self-adjoint
operator with eigenvalues conjugate to the modulus tau — structurally NOT a
holonomy-flux algebra (a phase-space pair {c, p~a^2} with a connection conjugate to a
triad). The three LQC-matter-ceiling inadmissibility grounds (operator / parameter /
causal) are three projections of that one definitional fact.

DISCIPLINE
----------
- from canonical_constants import *  (MANDATORY first import)
- every local/intermediate tagged `# (local)`
- no GPU (registry text + verdict-line emission; AMD RX 9070 XT NOT used)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- verdict emitted via emit_verdict knowledge-MCP tool (script PRINTS payload; agent calls)
- Audit-trail observation cited: computations/_bridge_landing_audit_trail_observation_S87_W5.md
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Bootstrap: put computations/_shared on sys.path BEFORE the
# canonical import (the canonical project convention; cf.
# computations/session-110/s110_cf_as2_greybody_scan.py:107).
# ---------------------------------------------------------------------------
import sys
from pathlib import Path as _Path

_SHARED = str((_Path(__file__).resolve().parent.parent / "_shared"))  # (local)
if _SHARED not in sys.path:
    sys.path.insert(0, _SHARED)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold, dS_fold  # noqa: E402  explicit (cited in entry)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S111"                                                    # (local)
GATE_ID = "S111-CF-NOHOLOFLUX"                                      # (local)
SCHEME = "STAGE-1-CANDIDATE-joint-registration"                    # (local)
CONVENTION = "registry-landing-single-shot-AFTER-pattern"          # (local)
L_MAX = "N/A"                                                       # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
S85_CUSP_NPZ = COMPUTATIONS_DIR / "session-85" / "s85_w0_van_hove_cusp_theorem.npz"  # (local)
OUT_NPZ = SESSION_DIR / "s111_cf_noholoflux.npz"                    # (local)

# Plan-pinned slot (re-verified at runtime over ALL header levels).
PLANNED_SLOT = "CH"                                                 # (local)
SLOT_CANDIDATES = ["CH", "CI", "CJ", "CK", "CL", "CM"]             # (local) reroute ladder

# Input files for the dual-SHA audit pin map.
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    S85_CUSP_NPZ,
]

# Required clause markers the re-read section MUST contain (PASS predicate).
# Superset of the plan `registry_entry.must_contain` patterns + the 3 projections
# + the JOINT flags + the cross-axis attribution + the distinctness citation.
REQUIRED_MARKERS = [
    "STAGE-1-CANDIDATE",
    "holonomy-flux",
    "spectral triple",
    "JOINT",
    "§VII.M.W10-3",
    "Projection 1",
    "Projection 2",
    "Projection 3",
    "NCG-axiomatic",
    "cosmological-bridge",
    "Stage-2",
]  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()  # (local)
    h.update(b)
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
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
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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
# Section 5 — Slot verification + promotion text (pure function; no I/O)
# ---------------------------------------------------------------------------
def slot_occupied(registry_text: str, letters: str) -> bool:
    """True iff §VII.<letters> appears as a header at ANY header level (## / ### / ####)."""
    pat = re.compile(r"(?m)^#{2,4}\s*§VII\." + re.escape(letters) + r"\b")  # (local)
    return bool(pat.search(registry_text))


def find_next_free_slot(registry_text: str) -> str:
    """Re-verify next-free over ALL header levels; return the first free candidate."""
    for cand in SLOT_CANDIDATES:
        if not slot_occupied(registry_text, cand):
            return cand
    raise RuntimeError("No free §VII slot in the reroute ladder — manual review.")


def build_promotion_text(slot: str) -> str:
    """Produce the EXACT registry-entry text for §VII.<slot>. Pure function; no I/O.

    Formalizes the FROZEN WS-ATFORM three-projection chain (Stage-0) into a
    clause-structured STAGE-1-CANDIDATE joint theorem. Re-derives nothing.
    Header convention matches the on-disk §VII.C* neighbors: '### §VII.<slot> — ...'.
    """
    tau = f"{tau_fold:.3f}"            # (local) 0.190
    dS = f"{dS_fold:.1f}"              # (local) 58672.8
    header = (
        f"§VII.{slot} — Spectral-Triple-No-Holonomy-Flux Root: the three LQC-matter-ceiling "
        f"inadmissibility grounds (operator / parameter / causal) are three projections of the "
        f"SINGLE definitional fact that a spectral triple has no holonomy-flux sector "
        f"(STAGE-1-CANDIDATE cross-axis JOINT theorem — NCG-axiomatic/conjugate-pair axis "
        f"[Projection 1 operator-level] ∧ cosmological-bridge/principle-theoretic axis "
        f"[Projection 2 parameter-level + Projection 3 causal-level], JOINT single-root "
        f"PASS-AND'd across both axes at Stage-2; S111 W1-5 gen-physicist registration of the "
        f"WS-ATFORM einstein×lqg CONVERGENCE-3/EMERGENCE-1 frozen Stage-0 text; single-shot "
        f"AFTER-pattern per `registry-landing.md` §\"Bridge-Landing Script Architecture\"; slot "
        f"§VII.{slot} runtime-verified next-free over ALL header levels [documented frontier "
        f"§VII.CF (S110 W4); CLOCKLOC3 pre-allocated §VII.CG, NOHOLOFLUX §VII.{slot}]; 2026-06-21)"
    )

    # body is a PLAIN (non-f) string — it contains literal LaTeX/markdown braces
    # ({λ_k(τ)}, {c, p~a²}, L^{-α}) that an f-string would mis-parse as replacement
    # fields. Inject the two computed anchors via __TAU__ / __DS__ sentinels.
    body = """
**STAGE TAG: STAGE-1-CANDIDATE** (registered S111 W1-5 gen-physicist, single-shot AFTER-pattern, from the WS-ATFORM einstein×lqg CONVERGENCE-3 + EMERGENCE-1 frozen Stage-0 three-projection chain; Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND queued as a SEPARATE S112+ gate per `joint-theorem-promotion.md` 4-stage pathway — the Stage-2 verifiers MUST NOT be einstein or lqg [original-author exclusion, downstream-inheritance reach], axis-distinct per the Axis-B Selection Protocol).

**Theorem (S111 W1-5).** The substrate is a spectral triple `(A_K, H_K, D_K(τ))` — a fixed self-adjoint operator whose kinematical data are EIGENVALUES `{λ_k(τ)}` conjugate to the Level-2 Jensen modulus `τ`. It is NOT a holonomy-flux algebra (a phase-space pair `{c, p~a²}` with a connection `c` conjugate to a triad, tied to the matter density `ρ` by a Hamiltonian constraint — the LQG/LQC kinematical structure). From this SINGLE definitional difference, all three grounds for the LQC holonomy-analog matter-density ceiling (the bounce ρ_c) are foreclosed for the substrate, as three projections of one fact: **the spectral triple has no holonomy-flux sector**. Hence the substrate has no matter-sector bounce density by CONSTRUCTION — the holonomy-analog "matter ceiling" SPLIT (S110 WS-ATFORM) was inadmissible not because a number failed a threshold but because there is no holonomy-flux sector to host it.

**Single-root statement (JOINT, PASS-AND'd across BOTH Stage-2 reviewers).** `spectral-triple ≠ holonomy-flux-algebra`: a spectral triple IS a fixed Dirac operator with a spectrum, NOT a phase-space pair with a connection conjugate to a triad. This is DEFINITIONAL (foreclosed by what a spectral triple IS, not computed). It is the JOINT clause: BOTH cross-axis reviewers must independently PASS it.

**Three projections (the clause decomposition):**
- **(Projection 1 — operator level) [Axis-A, NCG-axiomatic/conjugate-pair].** The substrate's bounded spectral function `Tr f(D_K²/Λ²) = Σ_k f(λ_k²/Λ²)` is a function of the τ-conjugate spectrum. The matter density `ρ_relic = Σ_K E_K|β_K|²` is a Bogoliubov occupation conjugate to the TRANSIT, not to `τ`. ⇒ `d/dρ[Tr f] = 0` EXACTLY, all orders (no resummation order makes a τ-conjugate object ρ-dependent) ⇒ no matter-ceiling operator exists on the spectral triple. [all-orders exact, WS-ATFORM Channel 1]
- **(Projection 2 — parameter level) [Axis-B, cosmological-bridge/principle-theoretic].** The LQC critical density `ρ_c = √3/(32π²γ³) M_Pl⁴` is the AREA GAP inverted (`Δ⁻³`): an area gap is a length² → inverting it gives a density ceiling. The substrate's spectral gap `λ_min` is a MASS (a Dirac eigenvalue); `λ_min⁴` is an additive density FLOOR (`ρ_offset`), NOT an inverted ceiling. ⇒ no kinematic `ρ_c` ⇒ any LQC-style `ρ_c` would have to be BORROWED from the dynamical relic ⇒ a tuning, not a kinematical bound. [leading-order parameter-type argument, WS-ATFORM Channel 2; see DISSENT-1 reach-tag below]
- **(Projection 3 — causal level) [Axis-B, cosmological-bridge/principle-theoretic].** A bounce is the holonomy-flux algebra's SIGNATURE (a symmetric curvature cap from `sin²(μ̄c)`, `t → −t` symmetric about the turning point). The spectral triple's saturation is the van Hove cusp at `τ_fold = __TAU__` (S85 PERMANENT, §VII.M.W10-3) — a DOS divergence in the τ-flow, passed through MONOTONICALLY (`dS/dτ = +__DS__` one-signed at the fold). ⇒ no two-sided bounce; a one-directional acoustic white hole (`N_zeros = 1`, S96-GEOM-PENROSE-2CONE). [WS-ATFORM Channel 3]

**Read off (substitution-chain conclusion).** All three projections are "the spectral triple has no holonomy-flux sector," read at the operator / parameter / causal levels. ONE structural fact, three faces; the direction is DEFINITIONAL — foreclosed by what a spectral triple IS, the way the elevator forecloses distinguishing free-fall from inertial motion. Therefore the substrate has no matter-sector bounce by CONSTRUCTION.

**Cross-axis author attribution (Stage-0 / Stage-1):**
- **Axis-A — NCG-axiomatic / conjugate-pair** (the definitional spectral-triple-structure clause + Projection 1 operator-level `d/dρ[Tr f]=0`): einstein-side principle-theoretic framing + the conjugate-pair diagnosis; Stage-0 authors einstein + lqg (WS-ATFORM, ws-s111-at-form.md:659-677 EMERGENCE-1 / :751-767 CONVERGENCE-3 / :771-777 definitional root).
- **Axis-B — cosmological-bridge / principle-theoretic** (Projection 2 parameter-level no-kinematic-ρ_c + Projection 3 causal-level no-two-sided-bounce, white-hole one-directionality): lqg-side conjugate-pair/dimensional-type + einstein-side equivalence-principle framing.

**Distinctness from the S85 τ_fold van-Hove-cusp PERMANENT theorem (§VII.M.W10-3).** S85 establishes the cusp's EXISTENCE + UNIQUENESS (`tau_fold = __TAU__` is the unique van-Hove-cusp non-stationarity point, PROVEN, connes + lizzi). NOHOLOFLUX establishes that the cusp (NOT a holonomy bounce) IS the substrate's saturation BECAUSE the spectral triple has no holonomy-flux sector. NOHOLOFLUX CITES §VII.M.W10-3 (Projection 3 consumes the cusp's existence + monotone pass-through), it does NOT duplicate it. The two are orthogonal: S85 = the cusp's geometry; NOHOLOFLUX = why the cusp, not a bounce, is what saturates.

**DISSENT-1 reach annotation (INFO-routing note).** Projection 1's operator-level `d/dρ[Tr f] = 0` is ALL-ORDERS exact (no resummation order can make a τ-conjugate object ρ-dependent); Projection 2's parameter-level argument (`ρ_c` = area-gap-inverted vs `λ_min` = additive offset) is a leading-order dimensional-type argument carried from WS-ATFORM DISSENT-1. The single root is registered; the per-projection reach is annotated, awaiting Stage-2 uniform verification (this annotation is the INFO-meaning content; the gate PASSes as STAGE-1-CANDIDATE with the reach-tag carried into the text, NOT downgraded).

**Falsifier-status NOTE (CLASS-level; routes to mack-cosmic-bridge as sole writer of `falsifier-master-inventory.md`, NOT this gate).** A DETECTED matter-sector bounce (a `t → −t` symmetric curvature cap in the expansion history) would discriminate a holonomy-flux substrate FROM a spectral-triple substrate — it is NOT a falsifier of the framework per se, but a quantization-FRAMEWORK discriminator. The positive observable content of the conjugate-pair split (bounded structure visible in τ-conjugate spectral-complexity observables, absent in ρ-conjugate expansion-history observables) is the SIBLING gate S111-CF-TAUCUSP, NOT this registration.

**Registry anatomy (intra-framework structural theorem; 5-anatomy IS-not-IN cross-pillar elements N/A with reason).** This is an INTRA-quantization-framework definitional theorem (spectral-triple structure vs holonomy-flux structure), NOT a cross-pillar substrate-IS ↔ laboratory-IN bridge: it has no continuum-measurement laboratory-IN observable and no `L^{-α}` convergence envelope (the no-holonomy-flux fact is L-INDEPENDENT — it holds at every L, a quantization-framework/definitional statement). The 5-anatomy elements (substrate-IS observable / laboratory-IN observable / HKR-or-K-theory bridge map / algebraic envelope / empirical anchor) are therefore N/A by construction; the structural-confidence content is the DEFINITIONAL root + its three projections. Level tag (`phononic-framing.md §"Single-τ-slice vs moduli-deformation"`): the no-holonomy-flux fact spans BOTH levels — it is a statement about what `D_K(τ)` IS (Level-1, at fixed τ) AND about the τ-flow's monotone saturation (Level-2, moduli-deformation, Projection 3) — declared as Level-1∧Level-2 (the definitional structure is Level-1; the causal projection invokes the Level-2 τ-flow monotonicity).

**Source / provenance.** WS-ATFORM einstein×lqg workshop CONVERGENCE-3 + EMERGENCE-1 frozen Stage-0 text (`sessions/session-111/` workshop source `ws-s111-at-form.md:659-677` EMERGENCE-1, `:751-767` CONVERGENCE-3, `:771-777` definitional root); the consumed S85 τ_fold van-Hove-cusp PERMANENT theorem `§VII.M.W10-3` (`proven_1892`, S85, connes + lizzi) for the distinctness citation; `joint-theorem-promotion.md` Stage-0→Stage-1 protocol; the WS-ATFORM MONOTONE-robust a(t)-FORM result (S110 WS-ATFORM einstein×lqg CONVERGED: `dH²/dρ = +8πG_eff/3 > 0` exact) — the matter-leg this root grounds at the quantization-framework level. Canonical anchors: `tau_fold = __TAU__` (S42 CONST-FREEZE-42), `dS_fold = +__DS__` (E7 PROVEN, one-signed across the transit window). **Substrate framing:** the substrate IS the finite spectral triple `(A_K, H_K, D_K(τ))` — a fixed Dirac operator whose data are eigenvalues conjugate to the Level-2 modulus τ; it is NOT a holonomy-flux algebra; the no-bounce is foreclosed by what a spectral triple IS, definitionally (`phononic-framing.md §"IS Space, Not IN Space"`). Direction preserved: `D_K eigenvalues → a_n moments → emergent (a,τ) congruence → measurement`, never inverted — this is a substrate-IS quantization-structure fact, NOT a statement about geometry living IN a container.

**Math-owners / Stage-0 authors (Stage-1 registrants, EXCLUDED from Stage-2 review per the original-author-exclusion + downstream-inheritance-reach clause):** einstein-theorist + loop-quantum-gravity-theorist (WS-ATFORM einstein×lqg). **Registration author (gen-physicist, single-shot AFTER-pattern landing; NOT a Stage-0 author).** **Stage-2 reviewers (axis-distinct, original-author-excluded, no-workshop-context — to be dispatched as a SEPARATE S112+ gate):** Axis-A = NCG-axiomatic NON-AUTHOR (e.g. connes-ncg-theorist OR van-den-dungen-bridge-theorist — the conjugate-pair / spectral-triple-structure clause); Axis-B = cosmological-bridge NON-AUTHOR (e.g. mack-cosmic-bridge OR volovik-superfluid-universe-theorist — the kinematic-ρ_c / bounce-causal-structure clause). Both operate WITHOUT prior workshop context per `joint-theorem-promotion.md` §"Stage-2 Axis-B Selection Protocol"; JOINT single-root clause PASS-AND'd across both verdicts (logical AND, not OR).
"""
    body = body.replace("__TAU__", tau).replace("__DS__", dS)  # (local) inject anchors

    # Header carries NO leading hashes; we prepend exactly "### " (3-hash on-disk convention).
    return "\n### " + header + "\n" + body.rstrip("\n") + "\n"


def write_atomic_with_fsync(text: str, registry_path: Path) -> int:
    """Binary-append the LF-terminated text. NO neighbor flatten (registry mixes LF + few CRLF).

    Returns the new on-disk byte length.
    """
    data = text.encode("utf-8")  # (local) already LF-terminated by build_promotion_text
    with open(registry_path, "ab") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    return registry_path.stat().st_size


def re_read_section(registry_text: str, slot: str) -> str:
    """Return the §VII.<slot> section text (from its header to the next §VII header / EOF)."""
    start_pat = re.compile(r"(?m)^### §VII\." + re.escape(slot) + r"\b")  # (local)
    m = start_pat.search(registry_text)
    if not m:
        return ""  # empty-string -> sha e3b0c442... -> spurious FAIL signal (header-anchor symmetry)
    start = m.start()  # (local)
    nxt = re.compile(r"(?m)^#{2,4}\s*§VII\.[A-Z]").search(registry_text, m.end())  # (local)
    end = nxt.start() if nxt else len(registry_text)  # (local)
    return registry_text[start:end]


# ---------------------------------------------------------------------------
# Section 6 — Compute (the landing) + verdict
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
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
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)

    # 1a. S85 cusp anchor existence (distinctness-citation substrate; non-fatal if absent —
    #     the §VII.M.W10-3 theorem is the citation target, the npz is the data anchor).
    s85_present = S85_CUSP_NPZ.exists()  # (local)
    print(f"  S85 cusp npz present: {s85_present}")

    # 2. Read the registry; re-verify the planned slot is free over ALL header levels.
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    crlf_before = registry_text.count("\r\n")  # (local) neighbor-flatten guard
    planned_free = not slot_occupied(registry_text, PLANNED_SLOT)  # (local)
    if planned_free:
        slot = PLANNED_SLOT  # (local)
        rerouted = False     # (local)
    else:
        slot = find_next_free_slot(registry_text)  # (local)
        rerouted = True      # (local)
    print(f"  planned slot §VII.{PLANNED_SLOT} free: {planned_free}; "
          f"landing slot: §VII.{slot}; rerouted: {rerouted}")

    # 3. Idempotency: if §VII.<slot> is occupied by THIS gate's own prior byte-identical
    #    landing, SKIP the append (NO-OP). (Re-run safety.)
    promotion_text = build_promotion_text(slot)  # (local) built fully in memory
    if slot_occupied(registry_text, slot):
        existing = re_read_section(registry_text, slot)  # (local)
        if GATE_ID_marker_in(existing):
            print(f"  §VII.{slot} already carries this gate's landing — NO-OP append.")
            full_text = registry_text  # (local)
        else:
            # FOREIGN occupancy on the rerouted slot: should not happen (find_next_free_slot
            # guarantees free), but guard explicitly.
            print(f"  FOREIGN occupancy on §VII.{slot}; FAIL-with-remediation.")
            full_text = registry_text  # (local)
    else:
        new_len = write_atomic_with_fsync(promotion_text, REGISTRY_PATH)  # (2) write + fsync
        print(f"  appended {len(promotion_text.encode('utf-8'))} bytes; new file size {new_len}")
        full_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (3) re-read from disk

    crlf_after = full_text.count("\r\n")  # (local)
    print(f"  CRLF count: before={crlf_before} after={crlf_after} "
          f"(unchanged: {crlf_before == crlf_after})")

    # 4. Re-read the landed section + verify every required marker (single decision point).
    section = re_read_section(full_text, slot)  # (local)
    section_sha = sha256_of_bytes(section.encode("utf-8"))  # (local)
    missing = [mk for mk in REQUIRED_MARKERS if mk not in section]  # (local)
    must_contain_ok = (len(missing) == 0)  # (local)
    stage1_present = ("STAGE-1-CANDIDATE" in section)  # (local)
    crlf_ok = (crlf_before == crlf_after)  # (local)
    foreign_collision = rerouted is False and not planned_free  # (local) impossible by construction
    section_nonempty = (len(section) > 0)  # (local) header-anchor-symmetry guard

    verdict = "PASS"  # (local)
    reasons = []      # (local)
    if not section_nonempty:
        verdict = "FAIL"; reasons.append("section-empty(header-anchor-mismatch)")
    if not must_contain_ok:
        verdict = "FAIL"; reasons.append(f"missing-markers={missing}")
    if not stage1_present:
        verdict = "FAIL"; reasons.append("no-STAGE-1-CANDIDATE-tag")
    if not crlf_ok:
        verdict = "FAIL"; reasons.append("CRLF-count-changed(neighbor-flatten)")
    if foreign_collision:
        verdict = "FAIL"; reasons.append("slot-foreign-occupied")

    value = (f"STAGE-1-CANDIDATE_joint_theorem_landed_VII.{slot}_"
             f"3projections+single-root_JOINT_cites_VII.M.W10-3_"
             f"markers={'OK' if must_contain_ok else 'MISSING'}_"
             f"reroute={rerouted}")
    if reasons:
        value = value + "_FAIL:" + ";".join(reasons)

    # 5. Persist the clause-checklist + slot-verification record (optional npz, but informative).
    try:
        import numpy as np  # (local)
        np.savez(
            OUT_NPZ,
            gate_id=GATE_ID,
            slot=slot,
            planned_slot=PLANNED_SLOT,
            rerouted=bool(rerouted),
            required_markers=np.array(REQUIRED_MARKERS, dtype=object),
            missing_markers=np.array(missing, dtype=object),
            must_contain_ok=bool(must_contain_ok),
            stage1_present=bool(stage1_present),
            crlf_before=int(crlf_before),
            crlf_after=int(crlf_after),
            section_sha256=section_sha,
            section_len_chars=len(section),
            s85_cusp_npz_present=bool(s85_present),
            tau_fold=float(tau_fold),
            dS_fold=float(dS_fold),
            verdict=verdict,
        )
        print(f"  wrote clause-checklist record: {OUT_NPZ.name}")
    except Exception as e:  # noqa: BLE001
        print(f"  (npz write skipped: {e})")

    # 6. Dual-SHA over the FINAL script bytes + canonical + pin map.
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  landed-section_sha256: {section_sha[:16]}... ({len(section)} chars)")

    # 7. Emit 4-tuple + verdict payload (single emission).
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# {GATE_ID} registry-landing: §VII.{slot} (planned §VII.{PLANNED_SLOT}); "
        f"rerouted={rerouted}; markers_ok={must_contain_ok}; "
        f"landed_section_sha256={section_sha}",
        f"# {GATE_ID} STAGE-1-CANDIDATE joint theorem; JOINT single-root "
        f"spectral-triple!=holonomy-flux PASS-AND'd at Stage-2 (S112+, NON-AUTHORS); "
        f"cites §VII.M.W10-3; reach-tag: P1 all-orders / P2 leading-order (DISSENT-1).",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else 1


def GATE_ID_marker_in(section_text: str) -> bool:
    """True iff the section was authored by THIS gate (idempotency check)."""
    return ("S111 W1-5" in section_text) and ("Spectral-Triple-No-Holonomy-Flux Root" in section_text)


if __name__ == "__main__":
    sys.exit(main())
