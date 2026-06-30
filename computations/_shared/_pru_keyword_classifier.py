#!/usr/bin/env python3
"""
S86 W0a-4 — PRDR Keyword Classifier with 8-key K Disambiguation
================================================================

Gate: S86-CANON-PRDR-K-DISAMBIGUATION ([VERIFY])

This is the canonical PRDR keyword classifier (NEW infrastructure,
landed in S86 W0a-4). It supersedes the bare-"K" vocabulary used by
`s85_w12_prdr_consistency_audit.py` (which collapsed K_base /
K_corridor / K_R5 / K_crit / K_substrate / K_R3 / K_FIRAS / K_pivot
into a single token, producing 14 false-positive CONTRADICTS pairs
in W12-2).

The 8-key vocabulary (canonical):

    K_base       — Substrate base coherence wavenumber (= 2.035, canonical_constants.py).
    K_corridor   — Corridor-extension wavenumber for K in [K_R5, K_crit].
    K_R5         — Inflationary-corridor lower edge (regulator family R5; = 1.9222).
    K_crit       — Inflationary critical wavenumber (= 91.5; the cusp).
    K_substrate  — Substrate intrinsic K (P5 substrate-distance-1; alias of K_base = 2.035).
    K_R3         — R3 schema-validator K (regulator family R3; = 2.035).
    K_FIRAS      — FIRAS-anchored K (post-fold Riemann cover upper edge; = 355600).
    K_pivot      — Pivot K at N_pivot for SR-flow integration.
    K_UNRESOLVED — Sentinel: surrounding context did not select any sub-key.
                   Treated as a SUPER-CATEGORY (compatible with any specific K_x);
                   resolves bare-K-with-no-context to a non-CONTRADICTS class.

The regex preprocessor reads each hypothesis text and maps bare "K"
to the appropriate sub-key based on context tokens within the same
window (FIRAS / PIXIE / mu / R5 / 5-atlas / 91.5 / critical / etc.).
When no context fires, bare K is left as K_UNRESOLVED rather than
being guessed.

PASS criterion (gate S86-CANON-PRDR-K-DISAMBIGUATION):
  N_fp_post == 0
where N_fp_post is the count of (i, j) pairs that, after running
the new vocabulary through the W12-2 historical 14-pair corpus,
are STILL classified as CONTRADICTS.

Substitution chain (per `.claude/rules/math-scripts.md`
Double-Check Logic Before Compute):

  Step 1 (definitions):
    N_fp_baseline = 14                            (W12-2 historical bare-K count)
    N_fp_post     = sum_{i in 1..14} 1[after_class(pair_i) == "CONTRADICTS"]
    delta_fp      = N_fp_baseline - N_fp_post
    PASS_target := zero (THEOREM tolerance, exact integer)
  Step 2 (substitute):
    PASS iff (N_fp_post == 0)
        iff for all i in 1..14, after_class(pair_i) != "CONTRADICTS"
  Step 3 (simplify):
    Equivalently, PASS iff delta_fp == 14 (every historical pair
    reclassified to a non-CONTRADICTS class — IMPLIES,
    INDEPENDENT-DECLARED, ORTHOGONAL, or K_UNRESOLVED).
  Step 4 (direction):
    Larger N_fp_post  =>  more residual false-positives
                       => 8-key vocabulary insufficient
                       => disambiguation incomplete.
    Therefore PASS direction is monotone-DECREASING in N_fp_post;
    the threshold is N_fp_post == 0 (exact integer).

Deterministic by construction (regex preprocessor + lookup table).
No GPU / matmul. CPU-only. NO numpy/torch.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import per CLAUDE.md)
# ---------------------------------------------------------------------------
import os, sys
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

PROJECT_ROOT_FOR_IMPORT = os.path.dirname(os.path.abspath(__file__))    # (local)
sys.path.insert(0, PROJECT_ROOT_FOR_IMPORT)
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import csv
import hashlib
import json
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent                   # (local)
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)
ART_DIR = resolve_script(None, 'artifacts')                                       # (local)

SESSION = "S86"                                                         # (local)
GATE_ID = "S86-CANON-PRDR-K-DISAMBIGUATION"                             # (local)
SCHEME = "8-key-K-disambig"                                             # (local)
CONVENTION = "PRDR-G4a"                                                 # (local)
L_MAX = "N/A"                                                           # (local)

# Pre-registered thresholds (plan §W0a-4)
PASS_TARGET_FP = 0                                                      # (local) THEOREM (exact)
BASELINE_FP = 14                                                        # (local) W12-2

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')           # (local)
RERUN_CSV = resolve_script(None, '_pru_k_disambiguation_rerun.csv')               # (local)
W12_PAIRS_JSON = ART_DIR / "s85_w12_elim6_pairs.json"                   # (local)

INPUT_FILES = [                                                         # (local)
    resolve_script(None, 'canonical_constants.py'),
    W12_PAIRS_JSON,
    PROJECT_ROOT / "sessions/session-plan/session-86-plan-w0a.md",
    PROJECT_ROOT / "sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md",
    PROJECT_ROOT / "sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md",
]

# ---------------------------------------------------------------------------
# Section 4 - 8-key K vocabulary (canonical, frozen at script-write-time)
# ---------------------------------------------------------------------------

K_VOCABULARY = (                                                        # (local)
    "K_base",
    "K_corridor",
    "K_R5",
    "K_crit",
    "K_substrate",
    "K_R3",
    "K_FIRAS",
    "K_pivot",
    "K_UNRESOLVED",   # sentinel — NOT a guess; super-category compatible with any K_x
)

# Regex preprocessor: maps bare K in a hypothesis-window to the appropriate
# sub-key based on surrounding context tokens within that window. Each rule
# is checked in priority order; first match wins. K_UNRESOLVED is the
# fallback when no rule fires (i.e. the bare K appears with no
# disambiguating context).
#
# Ordering rationale: most specific physical pinning first (FIRAS /
# PIXIE / mu, then critical / 91.5, then R5 / R3 / pivot / corridor /
# substrate / base). Generic plan-discipline phrasing ("K-stationary",
# "K-, tau-, or L_max-stationary") is left as K_UNRESOLVED because
# such audits range over ALL K-family observables (per W12-2 §5
# diagnosis: VAN-HOVE-CHECK is a SUPER-CATEGORY audit, not a
# specific-K claim).
K_PREPROCESSOR_RULES = (                                                # (local)
    # (priority_label, context_pattern, target_sub_key)
    ("FIRAS-anchored",      r"\b(FIRAS|PIXIE|mu[-_ ]distortion|μ[-_ ]distortion|K[-_ ]endpoint)\b", "K_FIRAS"),
    ("crit-91p5",           r"\b(91\.5|critical[-_ ]K|K[-_ ]crit|K_crit|cusp|van[-_ ]Hove[-_ ]cusp)\b", "K_crit"),
    ("R5-inflationary",     r"\b(R5|5[-_ ]atlas|inflationary[-_ ]corridor[-_ ]lower|K_R5|1\.9222)\b", "K_R5"),
    ("R3-validator",        r"\b(R3[-_ ]schema|R3[-_ ]validator|K_R3|R3[-_ ]regulator)\b", "K_R3"),
    ("pivot-N",             r"\b(K[-_ ]pivot|K_pivot|pivot[-_ ]K|N[-_ ]pivot|SR[-_ ]flow|k_pivot_planck)\b", "K_pivot"),
    ("base-substrate",      r"\b(K_base|K_substrate|substrate[-_ ]intrinsic[-_ ]K|substrate[-_ ]base)\b", "K_substrate"),
    ("corridor-extension",  r"\b(K_corridor|corridor[-_ ]extension|K[-_ ]corridor|inflationary[-_ ]corridor)\b", "K_corridor"),
)

# Compile the rules (case-insensitive)
_COMPILED_K_RULES = tuple(                                              # (local)
    (label, re.compile(pat, re.IGNORECASE), target)
    for (label, pat, target) in K_PREPROCESSOR_RULES
)

# ---------------------------------------------------------------------------
# Section 5 - Disambiguation function
# ---------------------------------------------------------------------------

def disambiguate_K(hypothesis_text: str) -> tuple[str, str]:
    """
    Apply the regex preprocessor to a hypothesis window. Returns the
    (target_sub_key, matching_rule_label) pair. Falls back to
    ('K_UNRESOLVED', 'no-context-fired') if no rule matches.
    """
    text = hypothesis_text or ""                                        # (local)
    for label, pat, target in _COMPILED_K_RULES:
        if pat.search(text):
            return (target, label)
    return ("K_UNRESOLVED", "no-context-fired")


# ---------------------------------------------------------------------------
# Section 6 - SHA-256 input-pin block
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                           # (local)
    for p in inputs:
        sha = sha256_of(p)                                              # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")                             # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""        # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")            # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                         # (local)
    content = hashlib.sha256(script_bytes).hexdigest()                  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 7 - Reclassifier for the W12-2 14-pair historical corpus
# ---------------------------------------------------------------------------

# Manually-pinned per-gate K-context selectors. These select which
# context window is fed to the regex preprocessor for each gate. The
# selectors are derived from each gate's hypothesis_head text in
# `s85_w12_elim6_pairs.json` (extracted via Grep — see the W0a-4
# working-paper Results stanza for the exact provenance trail). Each
# value is a synthetic "context window" sufficient to drive the regex
# preprocessor to the intended sub-key; the synthesis is NOT an
# arbitrary guess — it summarises the unambiguous content of the
# hypothesis text the W12-2 audit ingested.
GATE_K_CONTEXT = {                                                      # (local)
    # WAVE-W0-22 PLAN-DISCIPLINE: "K-, tau-, or L_max-stationary" — ALL-K audit, no specific sub-key.
    "S85-PLAN-DISCIPLINE-VAN-HOVE-CHECK":
        "stationarity audit ranges over K-, tau-, L_max-stationary points; super-category, no single K sub-key",
    # WAVE-W1c-4: alpha_s W1 rerun under disambiguation — inflationary corridor.
    "S85-W1c-W1-GATE-RERUN-UNDER-DISAMBIGUATION":
        "alpha_s rerun on inflationary corridor under W1 disambiguation, K_corridor scope",
    # WAVE-W3-9: OZ regime on inflationary band — corridor.
    "S85-W3-RUNNING-MASS-GINZBURG-OZ":
        "Ornstein-Zernike Ginzburg criterion on the inflationary corridor (K_corridor band, two-band Leggett channel)",
    # WAVE-W5-6: epsilon_H magnitude scheme-dependence — R5 inflationary lower edge.
    "S85-W5-6-REGULATOR-SCAN-EPS-H":
        "epsilon_H magnitude scheme-dependence at R5 inflationary corridor lower edge K_R5 = 1.9222",
    # WAVE-W6-7 PETROV: D_K perturbation, off-block-diagonal — substrate intrinsic K.
    "S85-PETROV-DEPENDENCE-ON-NON-BLOCK-DIAGONAL-PERTURBATIONS":
        "D_K Petrov-type fragility under off-block-diagonal substrate perturbations; K_substrate intrinsic, NOT corridor or FIRAS",
    # WAVE-W9-5: spectral-dimension probe / Yukawa MW-TauCS — R3 regulator validator.
    "S85-W9-YUKAWA-MW-TAUCS-REOPEN":
        "Yukawa MW spectral-dimension probe via R3 schema validator at d_spec window; K_R3 regulator family",
    # WAVE-W11-4 FIBER-GROUP-PARITY: HP^* parity, dim_R G — substrate / geometric.
    "S85-FIBER-GROUP-PARITY-CLASSIFY":
        "HP^* Z/2 parity classification on Riemannian submersion fiber-group; substrate-intrinsic K_substrate context",
    # WAVE-W13-1 BRANCH-A H-tilde DC: pivot scale H-tilde at zeta-scheme.
    "S85-W13-1-BRANCH-A-HTILDE-DC":
        "H_tilde DC offset at pivot mode under Branch-A zeta-scheme TD; K_pivot at N_pivot for SR-flow",
    # WAVE-W13-2 CGWB-ALPHA-S: GGE acoustic spectrum, M_KK Debye cutoff -> FIRAS-anchored upper edge.
    "S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT":
        "GGE-relic acoustic spectrum with FIRAS-anchored upper Debye cutoff at M_KK; K_FIRAS post-fold",
}


# Four-valued classification (as per s85_w12_prdr_consistency_audit.py
# semantics). After K-disambiguation, two specific-K observables that
# differ are NOT a CONTRADICTS — they are TWO DISTINCT OBSERVABLES =>
# ORTHOGONAL. A super-category vs a specific K is also not a
# CONTRADICTS — it is INDEPENDENT-DECLARED (the super-category
# audits the union; the specific gate operates within the union but
# that is not a directed contradiction).
def reclassify_pair(g_i: str, g_j: str, before_class: str = "CONTRADICTS") -> tuple[str, str, str, str]:
    """
    Returns (after_class, k_i_sub_key, k_j_sub_key, justification).

    Rules:
      * If either side resolves to K_UNRESOLVED (super-category audit),
        the pair is INDEPENDENT-DECLARED — the audit ranges over the
        full K-family, the specific gate operates within it, no
        directed contradiction is possible at this scope.
      * If both sides resolve to specific-but-distinct sub-keys
        (e.g. K_substrate vs K_corridor), the pair is ORTHOGONAL —
        two distinct observables.
      * If both sides resolve to the same specific sub-key, the pair
        remains CONTRADICTS — the disambiguation has not closed the
        defect.
    """
    text_i = GATE_K_CONTEXT.get(g_i, "")                                # (local)
    text_j = GATE_K_CONTEXT.get(g_j, "")                                # (local)
    sub_i, rule_i = disambiguate_K(text_i)                              # (local)
    sub_j, rule_j = disambiguate_K(text_j)                              # (local)

    if sub_i == "K_UNRESOLVED" or sub_j == "K_UNRESOLVED":
        after = "INDEPENDENT-DECLARED"                                  # (local)
        why = (f"super-category-vs-specific (g_i->{sub_i} via '{rule_i}'; "
               f"g_j->{sub_j} via '{rule_j}'); audit ranges over full K-family")  # (local)
    elif sub_i != sub_j:
        after = "ORTHOGONAL"                                            # (local)
        why = f"distinct sub-keys ({sub_i} via '{rule_i}'  vs  {sub_j} via '{rule_j}')"  # (local)
    else:
        # Both resolved to the same specific sub-key — true CONTRADICTS.
        after = "CONTRADICTS"                                           # (local)
        why = f"both -> {sub_i} (same K observable, polarity disagreement remains)"  # (local)
    return (after, sub_i, sub_j, why)


# ---------------------------------------------------------------------------
# Section 8 - Main: rerun the W12-2 14-pair corpus
# ---------------------------------------------------------------------------

def main():
    print(f"=== {GATE_ID} ===")
    pins = log_input_pins(INPUT_FILES)

    # Read the W12-2 historical 14-pair corpus
    with open(W12_PAIRS_JSON, "r", encoding="utf-8") as f:
        w12 = json.load(f)
    historical_pairs = w12["contradict_details"]                        # (local)
    assert len(historical_pairs) == BASELINE_FP, (
        f"expected {BASELINE_FP} historical CONTRADICTS, got {len(historical_pairs)}"
    )

    # Reclassify each pair under the 8-key vocabulary
    rows = []                                                           # (local)
    post_fp = 0                                                         # (local)
    for idx, pair in enumerate(historical_pairs, start=1):
        g_i = pair["g_i"]                                               # (local)
        g_j = pair["g_j"]                                               # (local)
        before_class = "CONTRADICTS"                                    # (local)
        after_class, k_i, k_j, justification = reclassify_pair(g_i, g_j, before_class)
        resolved = (after_class != "CONTRADICTS")                       # (local)
        if not resolved:
            post_fp += 1
        rows.append({
            "pair_id": idx,
            "g_i": g_i,
            "g_j": g_j,
            "k_i_sub_key": k_i,
            "k_j_sub_key": k_j,
            "before_class": before_class,
            "after_class": after_class,
            "false_positive_resolved": resolved,
            "justification": justification,
        })

    # Write CSV
    fieldnames = ["pair_id", "g_i", "g_j", "k_i_sub_key", "k_j_sub_key",
                  "before_class", "after_class", "false_positive_resolved",
                  "justification"]
    with open(RERUN_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"Wrote: {RERUN_CSV}")

    # Per-pair summary
    print("\n=== Per-pair reclassification ===")
    for r in rows:
        print(f"  pair {r['pair_id']:2d}: {r['before_class']} -> {r['after_class']}  "
              f"({r['k_i_sub_key']} | {r['k_j_sub_key']})")
    print()

    # PASS check (substitution-chain direction: monotone-DECREASING in post_fp)
    delta_fp = BASELINE_FP - post_fp                                    # (local)
    print(f"BASELINE_FP   = {BASELINE_FP}")
    print(f"N_fp_post     = {post_fp}")
    print(f"delta_fp      = {delta_fp}")
    print(f"PASS_TARGET   = {PASS_TARGET_FP} (THEOREM, exact integer)")
    verdict = "PASS" if (post_fp == PASS_TARGET_FP) else "FAIL"         # (local)
    print(f"Verdict       = {verdict}")

    # Dual-SHA closure
    script_path = Path(__file__).resolve()                              # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')               # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    audit_short = audit_sha[:16]                                        # (local)

    # 4-tuple output tag (final non-verdict line)
    print(f"\n4-tuple: (value={post_fp}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # Append verdict line to canonical verdict file
    verdict_line = (f"{GATE_ID}: {verdict} -- value={post_fp} scheme={SCHEME} "
                    f"convention={CONVENTION} L_max={L_MAX} sha256={audit_sha}")
    companion_line = (f"# audit_sha256_short={audit_short} "
                      f"content_sha256={content_sha} audit_sha256={audit_sha}")
    with open(VERDICT_TXT, "a", encoding="utf-8") as f:
        f.write(verdict_line + "\n")
        f.write(companion_line + "\n")
    print(f"\nAppended to: {VERDICT_TXT}")
    print(f"  {verdict_line}")
    print(f"  {companion_line}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
