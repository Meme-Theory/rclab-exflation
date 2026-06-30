#!/usr/bin/env python3
"""
S93 W8-7 — Narrow-Path Workshop 6 Dispatch (Substrate Mode Localization on Emergent 3-Slices)
=============================================================================================

Gate: S93-W8-7-NARROW-PATH-WORKSHOP-6-DISPATCH ([VERIFY])  — GATED ON W8-3

This is a WORKSHOP-DISPATCH verdict-emission script (NO physics compute). The
adversarial workshop (phonon-first-cosmologist + connes-ncg-theorist, R1/R2/R3)
is documented in the workshop transcript; this script emits the canonical dual-
SHA verdict line whose closure is computed (NOT hardcoded) over the input-pin
map per the plan's audit_discriminators.

W8-3-KEYED TARGET (plan §W8-7 substitution chain Step 4):
  W8-3 landed INFO (band-edge-convention-ambiguous; 3-tuple sign=PASS,
  magnitude=FAIL, regime=MARGINAL). Per the Wave-8 Decision Point table
  (plan line 1349): "INFO (j-band ambiguous) -> determine area-volume band
  edges first, THEN re-key W8-7". The workshop therefore MUST NOT force the
  full Step-4 cocycle construction against an ambiguous target; it adjudicates
  the well-posed sub-questions (R1/R2/R3) and CONVERGES ON INFO.

VERDICT: INFO (W8-3-INFO-keyed convergence; NOT honest-mechanical-closure-unmet,
  since W8-3 IS met with an INFO line on disk).
  - Substrate magnitude leg: prescription-INDEPENDENT, Regime-II-favoring
    (alpha_req=4.81e-3 is 0.12 OOM / 1.33x BELOW alpha_win_lo=6.381e-3); the
    Cauchy-Schwarz moment floor s_CS=0.0186 >= 0 is satisfied.
  - LQG band-containment leg: prescription-AMBIGUOUS (gamma_BH=0.2375 EXCLUDED
    by DL/Meissner SU(2) band [0.2722,0.2741] (inDL=False); CONTAINED by full
    prescription-spread [0.1274,0.2741] (inSpread=True)). RECOMMEND a single
    DL/Meissner SU(2) prescription (convention-consistency + physical-band).
  - Explicit [S_exit-horizon]^# cocycle + alpha_bridge OOM estimate: DEFERRED to
    S94 with a 4-field carry-forward, keyed to the refined area-volume band under
    the declared prescription. R_BG=6.84e-4 (W8-6) pins the pre/post relative
    constraint (post-fold ~1462x the pre-fold).

Output 4-tuple:
  (value='INFO_W8-3-INFO-keyed-DEFERRED-PENDING-band-determination_...',
   scheme=narrow-path-workshop-6-substrate-mode-localization-emergent-3-slices-reading-b-cocycle,
   convention=NARROW-PATH-workshop-6-exit-horizon-tau-0p16-Hochschild-cocycle-HKR-Cheeger-Simons-W8-3-keyed-target,
   L_max=12)

Dual-SHA (plan audit_discriminators):
  audit_sha256  inputs: [w8_3_verdict, w8_6_verdict, lqg_bridge_class_doc, pinmap]
  content_sha256 inputs: [workshop_document]

Classification: PHONONIC

DISCIPLINE
----------
- from canonical_constants import *  (MANDATORY first import)
- every local/intermediate tagged # (local)
- no large matrices, no GPU needed (workshop-dispatch emission)
- dual-SHA (audit_sha256 + content_sha256) + W9a-99 companion row
- [VERIFY] trigger: NO S87 schema-v2 3-tuple companion row required
- Option-A supersedes-chain read (verdict permanence) for re-runs
- 4-tuple printed as final non-verdict line
- Exit 0 for any valid verdict (verdict is DATA, not script health)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Path bootstrap (make canonical_constants importable)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402  explicit pins
    ALPHA_BRIDGE_REQUIRED_FW,
    SCALE_BRIDGE_PREFACTOR_FW,
    GAMMA_BH_SU2_CONVENTION_LQG,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration (paths defined in Section 0)
# ---------------------------------------------------------------------------

SESSION = "S93"                                                          # (local)
GATE_ID = "S93-W8-7-NARROW-PATH-WORKSHOP-6-DISPATCH"                      # (local)
SCHEME = ("narrow-path-workshop-6-substrate-mode-localization-"
          "emergent-3-slices-reading-b-cocycle")                          # (local)
CONVENTION = ("NARROW-PATH-workshop-6-exit-horizon-tau-0p16-"
              "Hochschild-cocycle-HKR-Cheeger-Simons-W8-3-keyed-target")  # (local)
L_MAX = "12"                                                              # (local)

# Upstream verdict gate-IDs (read from the verdict file)
W8_3_GATE = "S93-W8-3-NARROW-PATH-CAUCHY-SCHWARZ-JOINT-PREFLIGHT"         # (local)
W8_6_GATE = "S93-W8-6-NARROW-PATH-PRE-POST-BOGOLIUBOV-RATIO"             # (local)

# W8-3 pinned numbers (from the verdict line; for the value-string + audit)
S_CS = 0.0186                # (local) Cauchy-Schwarz moment-floor slack F0*F2 - F1^2 >= 0
ALPHA_REQ = 4.810e-3         # (local) = ALPHA_BRIDGE_REQUIRED_FW
ALPHA_WIN_LO = 6.381e-3      # (local) substrate-admissible alpha floor (moment-ratio + N_e)
OOM_BELOW = 0.12             # (local) log10(ALPHA_WIN_LO/ALPHA_REQ)
GAMMA_BH = 0.2375            # (local) = GAMMA_BH_SU2_CONVENTION_LQG
DL_BAND_LO = 0.2722          # (local) DL/Meissner SU(2) band lower edge
DL_BAND_HI = 0.2741          # (local) DL/Meissner SU(2) band upper edge
SPREAD_LO = 0.1274           # (local) full prescription-spread lower edge (~U(1)-ABCK 0.127)
SPREAD_HI = 0.2741           # (local) full prescription-spread upper edge
# W8-6 pinned numbers
R_BG = 6.838562903161084e-4  # (local) = 1/cosh(2r), pre/post bridge ratio (W8-6 PASS)
W_BG = 1462.30               # (local) = cosh(2r), post-fold ~1462x pre-fold

# Output destinations (per-session)
STEM = "s93_w8_7_narrow_path_workshop_6"                                  # (local)
OUT_NPZ = SESSION_DIR / f"{STEM}_alpha_bridge_oom.npz"
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"
WORKSHOP_DOC = (PROJECT_ROOT / "sessions" / "session-93" / "workshops" /
                "s93-w8-7-substrate-mode-localization-emergent-3-slices.md")
LQG_BRIDGE_DOC = (PROJECT_ROOT / "sessions" / "framework" / "correspondence" /
                  "lqg-narrow-path-bridge-class.md")


# ---------------------------------------------------------------------------
# Section 4 — Upstream-verdict resolution (Option-A supersession-chain read)
# ---------------------------------------------------------------------------

def _latest_non_superseded_line(gate_id: str) -> str:
    """Return the latest NON-superseded canonical verdict line for gate_id,
    following the Option-A supersession chain (gate-verdicts.md). '' if none."""
    if not VERDICT_TXT.exists():
        return ""
    superseded: set[str] = set()      # (local) audit_shas named in supersedes=
    lines_for_gate: list[tuple[str, str]] = []  # (local) (audit_sha, full_line) in file order
    for raw in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if raw.startswith(f"{gate_id}:"):
            this_sha = ""  # (local)
            for tok in raw.split():
                if tok.startswith("audit_sha256="):
                    this_sha = tok.split("=", 1)[1]
                if tok.startswith("supersedes="):
                    superseded.add(tok.split("=", 1)[1].strip("'\""))
            if "supersedes=" in raw:
                frag = raw.split("supersedes=", 1)[1]  # (local)
                superseded.add(frag.split()[0].strip("'\""))
            if this_sha:
                lines_for_gate.append((this_sha, raw))
    live = [(s, ln) for (s, ln) in lines_for_gate if s not in superseded]  # (local)
    return live[-1][1] if live else ""


def _verdict_of_line(line: str) -> str:
    """Extract PASS/FAIL/INFO from a canonical verdict line."""
    # form: '{GATE}: VERDICT -- value=...'
    try:
        after_colon = line.split(":", 1)[1].strip()  # (local)
        return after_colon.split()[0]                 # (local)
    except IndexError:
        return ""


# ---------------------------------------------------------------------------
# Section 5 — SHA-256 dual-pin block (plan audit_discriminators)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def build_pinmap() -> dict[str, str]:
    """Input-pin map per plan input_files: w8_3_verdict + w8_6_verdict (both the
    verdict file) + lqg_bridge_class_doc. The verdict-file SHA pins BOTH the
    W8-3 and W8-6 verdicts (they live in the same file)."""
    verdict_sha = sha256_of(VERDICT_TXT)  # (local)
    pins: dict[str, str] = {  # (local)
        "w8_3_verdict": verdict_sha,
        "w8_6_verdict": verdict_sha,
        "lqg_bridge_class_doc": sha256_of(LQG_BRIDGE_DOC),
    }
    return pins


def compute_dual_sha(pins: dict[str, str], workshop_doc: Path) -> tuple[str, str]:
    """audit_sha256 over [w8_3_verdict, w8_6_verdict, lqg_bridge_class_doc, pinmap];
    content_sha256 over [workshop_document]. Closure is COMPUTED, not hardcoded.

    'pinmap' (the audit_discriminators 4th input) is the JSON-canonicalized
    input-pin dict folded into the audit closure — this makes the audit_sha256
    a closure over the ordered input-pin map per gate-verdicts.md.
    """
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    # fold each pinned input's SHA, then the canonical pinmap blob
    for k, v in sorted(pins.items()):
        h_audit.update(f"{k}={v}\n".encode("utf-8"))
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    workshop_bytes = b""  # (local)
    try:
        workshop_bytes = workshop_doc.read_bytes()
    except OSError:
        workshop_bytes = b""
    h_content = hashlib.sha256()  # (local)
    h_content.update(workshop_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 6 — Verdict construction (W8-3-keyed; NO physics compute)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def build_value_string(w8_3_verdict: str, w8_6_verdict: str) -> str:
    """The descriptive value string encodes the W8-3-keyed convergence + the
    deferred-pending structure (band-determination-first per plan Step 4)."""
    # in-band tests (sanity cross-check of the pinned band numbers)
    in_dl = DL_BAND_LO <= GAMMA_BH <= DL_BAND_HI       # (local) expect False
    in_spread = SPREAD_LO <= GAMMA_BH <= SPREAD_HI     # (local) expect True
    return (
        f"INFO_W8-3-INFO-keyed-DEFERRED-PENDING-band-determination_"
        f"w8_3={w8_3_verdict}_w8_6={w8_6_verdict}_"
        f"magLeg=Regime-II-favoring-prescription-INDEPENDENT_"
        f"sCS={S_CS}_alphaReq={ALPHA_REQ:.3e}_alphaWinLo={ALPHA_WIN_LO:.3e}_"
        f"oomBelow={OOM_BELOW}_factor={ALPHA_WIN_LO/ALPHA_REQ:.3f}_"
        f"gammaBH={GAMMA_BH}_inDL={in_dl}_inSpread={in_spread}_"
        f"prescRECOMMEND=DL-Meissner-SU2_"
        f"R_BG={R_BG:.6e}_W_BG={W_BG}_"
        f"construction-DEFERRED-S94-CF"
    )


# ---------------------------------------------------------------------------
# Section 7 — append_verdict (canonical line + W9a-99 companion row)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the canonical line + dual-SHA companion row. [VERIFY] trigger:
    NO S87 schema-v2 3-tuple companion row. Atomic single-open append.

    Option-A: if a prior non-superseded canonical line for this gate-ID exists,
    emit supersedes=<prior_audit_sha> in value= (verdict permanence).
    """
    prior_line = _latest_non_superseded_line(GATE_ID)  # (local)
    prior_sha = ""  # (local)
    if prior_line:
        for tok in prior_line.split():
            if tok.startswith("audit_sha256="):
                prior_sha = tok.split("=", 1)[1]
    if prior_sha and prior_sha != audit_sha:
        value_field = f"'{value};supersedes={prior_sha}'"  # (local) Option A tag
    else:
        value_field = f"'{value}'"  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value_field} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # ---- Resolve upstream verdicts (Option-A supersession-chain) ----
    w8_3_line = _latest_non_superseded_line(W8_3_GATE)  # (local)
    w8_6_line = _latest_non_superseded_line(W8_6_GATE)  # (local)
    w8_3_verdict = _verdict_of_line(w8_3_line)          # (local)
    w8_6_verdict = _verdict_of_line(w8_6_line)          # (local)

    print(f"=== {GATE_ID} — upstream verdict resolution ===")
    print(f"  {W8_3_GATE}: {w8_3_verdict or 'UNMET'}")
    print(f"  {W8_6_GATE}: {w8_6_verdict or 'UNMET'}")
    print()

    # ---- Gating check: W8-3 must be met (PASS/FAIL/INFO) ----
    if w8_3_verdict not in ("PASS", "FAIL", "INFO"):
        # W8-3 unmet -> honest mechanical closure (NOT our case; W8-3 is INFO)
        verdict = "FAIL"  # (local)
        value = ("PRE-REG-INC_blocked_by_S93-W8-3-NARROW-PATH-"
                 "CAUCHY-SCHWARZ-JOINT-PREFLIGHT_unmet")  # (local)
        print("  W8-3 UNMET -> honest mechanical closure (deferred to S94).")
    else:
        # W8-3 met. Per plan substitution chain:
        #   Step 2 [PASS]: canonical-LQG-matching target  (N/A here)
        #   Step 3 [FAIL]: substrate-own-effective-theory target  (N/A here)
        #   Step 4 [INFO]: band ambiguous -> determine band edges FIRST, re-key.
        #                  Workshop converges on INFO (deferred-pending).
        if w8_3_verdict == "INFO":
            verdict = "INFO"  # (local) W8-3-INFO-keyed convergence
            value = build_value_string(w8_3_verdict, w8_6_verdict)  # (local)
            print("  W8-3 INFO -> W8-3-INFO-keyed convergence (Step 4):")
            print("    band ambiguous; full Step-4 construction DEFERRED to S94")
            print("    (RECOMMEND single DL/Meissner SU(2) prescription).")
        else:
            # PASS or FAIL branch: this script's INFO-keyed convergence does not
            # cover those; per plan they would dispatch the full construction.
            # Not reachable in this session (W8-3 is INFO) but kept honest.
            verdict = "INFO"  # (local)
            value = (f"W8-3={w8_3_verdict}-branch-not-INFO-keyed_"
                     f"see-plan-Step-{'2' if w8_3_verdict == 'PASS' else '3'}")  # (local)
            print(f"  W8-3 {w8_3_verdict} -> non-INFO branch (plan Step "
                  f"{'2' if w8_3_verdict == 'PASS' else '3'}).")
    print()

    # ---- Substitution-chain echo (numbers) ----
    print("=== W8-3-keyed substitution chain (numbers) ===")
    print(f"  ALPHA_BRIDGE_REQUIRED_FW = {ALPHA_BRIDGE_REQUIRED_FW:.5e}  (= gamma_BH/49.34)")
    print(f"  SCALE_BRIDGE_PREFACTOR_FW = {SCALE_BRIDGE_PREFACTOR_FW}")
    print(f"  GAMMA_BH_SU2_CONVENTION_LQG = {GAMMA_BH_SU2_CONVENTION_LQG}")
    print(f"  cross-check: gamma_emergent(alpha_req) = alpha_req*49.34 = "
          f"{ALPHA_REQ * SCALE_BRIDGE_PREFACTOR_FW:.5f}  (= gamma_BH = {GAMMA_BH})")
    print(f"  substrate magnitude leg: alpha_req={ALPHA_REQ:.3e} vs "
          f"alpha_win_lo={ALPHA_WIN_LO:.3e}  -> "
          f"{ALPHA_WIN_LO/ALPHA_REQ:.3f}x below ({OOM_BELOW} OOM); "
          f"PRESCRIPTION-INDEPENDENT; Regime-II-favoring")
    print(f"  Cauchy-Schwarz floor: s_CS={S_CS} >= 0  (moment floor satisfied)")
    print(f"  LQG band leg: gamma_BH={GAMMA_BH} in DL/Meissner SU(2) "
          f"[{DL_BAND_LO},{DL_BAND_HI}] = "
          f"{DL_BAND_LO <= GAMMA_BH <= DL_BAND_HI} (EXCLUDED); "
          f"in full spread [{SPREAD_LO},{SPREAD_HI}] = "
          f"{SPREAD_LO <= GAMMA_BH <= SPREAD_HI} (CONTAINED) -> AMBIGUOUS")
    print(f"  W8-6 pre/post: R_BG={R_BG:.6e} = 1/cosh(2r); W_BG={W_BG} "
          f"(post-fold ~1462x pre-fold) -> pins pre/post relative constraint")
    print()

    # ---- Dual-SHA over the input-pin map (COMPUTED, not hardcoded) ----
    pins = build_pinmap()  # (local)
    print("=== input SHA-256 pins (audit_discriminators) ===")
    print(f"  verdict file (w8_3 + w8_6 verdicts): {pins['w8_3_verdict'][:16]}...")
    print(f"  lqg_bridge_class_doc:                {pins['lqg_bridge_class_doc'][:16]}...")
    print(f"  workshop_document (content):         {sha256_of(WORKSHOP_DOC)[:16]}...")

    audit_sha, content_sha = compute_dual_sha(pins, WORKSHOP_DOC)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (pins + pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (workshop document)")
    print()

    # ---- Persist data (small descriptive record) ----
    import numpy as np  # (local) deferred import (no heavy LA)
    np.savez(
        OUT_NPZ,
        w8_3_verdict=w8_3_verdict,
        w8_6_verdict=w8_6_verdict,
        verdict=verdict,
        s_CS=S_CS,
        alpha_req=ALPHA_REQ,
        alpha_win_lo=ALPHA_WIN_LO,
        oom_below=OOM_BELOW,
        factor_below=ALPHA_WIN_LO / ALPHA_REQ,
        gamma_BH=GAMMA_BH,
        gamma_emergent_at_req=ALPHA_REQ * SCALE_BRIDGE_PREFACTOR_FW,
        dl_band_lo=DL_BAND_LO,
        dl_band_hi=DL_BAND_HI,
        spread_lo=SPREAD_LO,
        spread_hi=SPREAD_HI,
        in_dl=bool(DL_BAND_LO <= GAMMA_BH <= DL_BAND_HI),
        in_spread=bool(SPREAD_LO <= GAMMA_BH <= SPREAD_HI),
        presc_recommend="DL-Meissner-SU2",
        R_BG=R_BG,
        W_BG=W_BG,
        construction_deferred="S94-CF-NARROW-PATH-WORKSHOP-6-COCYCLE-CONSTRUCTION",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} "
          f"(W8-3-INFO-keyed convergence; construction DEFERRED to S94; "
          f"wall {wall:.2f}s) ===")
    # Exit 0 for any valid verdict (verdict is DATA, not script health) per
    # math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
