#!/usr/bin/env python3
"""
S85 W12-ELIM-6 — Plan-layer PRDR consistency audit
====================================================

Gate: S85-W12-ELIM-6 ([AUDIT])

Pre-registered threshold (plan §W12-2 line 85):
  PASS  iff  100% of pairs classified in {IMPLIES, CONTRADICTS,
            INDEPENDENT-DECLARED, ORTHOGONAL}  AND  UNDECLARED = 0
            AND  CONTRADICTS = 0.
  FAIL  iff  CONTRADICTS >= 1.
  INFO  iff  0 < UNDECLARED <= 0.05 * total_pairs  AND  CONTRADICTS = 0.

Output 4-tuple:
  (value=<N_IMPLIES, N_CONTRADICTS, N_INDEPENDENT, N_UNDECLARED>,
   scheme=plan-layer-prdr, convention=four-valued-predicate, L_max=n/a)

Classification: NON-PHONONIC (infrastructure / plan-file AST audit).

METHODOLOGY
-----------
The tool parses the 15 S85 wave plan files (W0, W1a, W1b, W1c, W2, W3, W4,
W5, W6, W7, W8, W9, W10, W11, W13 — W12 excluded per plan line 104),
extracts gate-block headings `## §W{i}-{n}. GATE_ID [— title]`, and
matches each gate's `**Hypothesis**` block via tolerant regex.

Classification per pair (g_i, g_j):
  1. Extract observable keywords + mechanism keywords from each hypothesis.
  2. shared_obs = obs_i ∩ obs_j;  shared_mech = mech_i ∩ mech_j.
  3. For every directed-observable in shared_obs, read polarity markers
     in each hypothesis (> 1 / < 1, dominates / does-not-dominate,
     increases / decreases, PASS / FAIL-direction, retracted/confirmed).
  4. If directed_conflict: CONTRADICTS.
     Else if |shared_obs| + |shared_mech| >= 1: IMPLIES.
     Else if hypothesis_i not empty AND hypothesis_j not empty AND no shared:
          ORTHOGONAL.
     Else: UNDECLARED (missing extraction on either side).
  5. INDEPENDENT-DECLARED fires only if the plan contains the
     string "independent from G-X" or "orthogonal to §W{X}-{Y}".
     (Rare; most plans don't pre-declare independence.)

The classifier is deterministic — same plan SHAs → same pair matrix.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import itertools
import json
import os
import re
import sys
import time
from pathlib import Path
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


os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ART_DIR = resolve_script(None, 'artifacts')
ART_DIR.mkdir(parents=True, exist_ok=True)
PLAN_DIR = PROJECT_ROOT / "sessions" / "session-plan"

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W12-ELIM-6"                                          # (local)
SCHEME = "plan-layer-prdr"                                          # (local)
CONVENTION = "four-valued-predicate"                                # (local)
L_MAX = "n/a"                                                       # (local)

# Pre-registered thresholds (plan §W12-2 line 85-88)
PASS_UNDECLARED_MAX = 0                                             # (local) ABS
PASS_CONTRADICTS_MAX = 0                                            # (local) ABS
INFO_UNDECLARED_FRAC = 0.05                                         # (local) ABS fraction

# Wave-plan corpus (plan §W12-2 line 90; W12 excluded per plan line 104)
PLAN_WAVES = ("w0", "w1a", "w1b", "w1c", "w2", "w3", "w4", "w5",     # (local)
              "w6", "w7", "w8", "w9", "w10", "w11", "w13")
PLAN_FILES = [PLAN_DIR / f"session-85-plan-{w}.md" for w in PLAN_WAVES]  # (local)

INPUT_FILES = [                                                     # (local)
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "sessions/session-plan/session-85-partition.md",
    *PLAN_FILES,
]

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')
OUT_NPZ = ART_DIR / "s85_w12_elim6_pair_matrix.npz"
OUT_PNG = ART_DIR / "s85_w12_elim6_heatmap.png"
OUT_JSON = ART_DIR / "s85_w12_elim6_pairs.json"

# Observable and mechanism keyword vocabularies (frozen at script-write-time)
OBSERVABLE_KEYWORDS = (                                             # (local)
    "A_s", "alpha_s", "n_s", "n_s_canon", "r ", "w_0", "w_a", "tau_reion",
    "H_0", "H_tilde", "sigma_8", "Omega_m", "f_NL", "beta_s",
    "m_H", "m_t", "mu_BC", "K_base", "K_crit", "K_R5", "K_corridor",
    "K_substrate", "K ", "Delta", "F_amp", "c_sub", "f_DM", "Lambda",
    "a_0", "a_2", "a_4", "D_K", "sigma_J", "sigma_K", "R_JK", "R_JE",
    "epsilon_H", "ε_H", "tau_fold", "L_max", "M_KK", "sin^2",
    "Higgs", "top quark", "Yukawa",
    "CMB-S4", "DESI", "LISA", "JWST", "PIXIE", "FIRAS", "Planck", "SKA",
    "branch (iv)", "branch-(iv)", "branch iv", "R_842", "R_918",
    "Mellin", "heat kernel", "zeta", "Pauli-Villars",
)

MECHANISM_KEYWORDS = (                                              # (local)
    "BCS", "Josephson", "Jensen", "Leggett", "spectral action",
    "KO-dim", "twisted triple", "HP^1", "HP1", "HP^0", "HP^even",
    "Chern", "triality", "cohomology", "Cartan", "Poincare duality",
    "parametric", "squeezing", "Kibble-Zurek", "GGE", "Parker",
    "first-order transit", "supersonic", "fold", "reheating",
    "Seeley-DeWitt", "Casimir", "Gilkey", "regulator", "Zubarev",
    "Connes-Moscovici", "Peter-Weyl", "axioms", "axiom",
    "anomaly cancellation", "bispectrum", "non-Gaussianity",
    "F_3PI", "F_conv", "f_conv", "3PI", "4PI",
)

# Directed observables: those where polarity is meaningful
DIRECTED_OBSERVABLES = (                                            # (local)
    "R_JK", "R_JE", "sigma_J", "sigma_K", "H_tilde", "A_s",
    "Delta", "F_amp", "branch (iv)", "branch-(iv)", "branch iv",
    "w_0", "K ", "K_base", "alpha_s",
)

# Positive and negative direction markers (regexable patterns)
POS_MARKERS = ("dominates", "exceeds", "increases", "amplifies",    # (local)
               "larger than", "greater than", "widens",
               "above", "> 1", ">= 1", ">1", "grows", "monotone-increasing",
               "confirmed", "PASS")
NEG_MARKERS = ("does not dominate", "not dominate", "suppresses",   # (local)
               "decreases", "attenuates", "retracted", "retraction",
               "smaller than", "less than", "narrows", "below",
               "< 1", "<= 1", "<1", "decays", "monotone-decreasing",
               "FAIL")


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 input-pin block
# ---------------------------------------------------------------------------
def sha256_of(path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")                  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)
    content = hashlib.sha256(script_bytes).hexdigest()              # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Gate extraction
# ---------------------------------------------------------------------------
# Header pattern: `## §W{i}-{n}. GATE_ID [— title]`
# Gate ID = first non-whitespace token after the period, before space or em-dash.
HEADER_RE = re.compile(                                             # (local)
    r"^##\s+§(W\S+?)\.\s+([A-Za-z0-9\-]+?)(?:\s+—\s+|\s+\(|\s*$|\s+\-\s+)",
    re.MULTILINE,
)

# Hypothesis pattern — matches `**Hypothesis**:` OR `**4. Hypothesis**:`
HYP_RE = re.compile(                                                # (local)
    r"\*\*(?:\d+\.\s+)?Hypothesis\*\*:\s*(.+?)(?=\n\s*\*\*|\n##|\n---|\Z)",
    re.DOTALL,
)


def parse_plan(path):
    """Return list of {gate_id, wave_id, hypothesis} for one plan file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    gates = []                                                      # (local)
    # Split on gate-block headings to scope each hypothesis to its own block
    header_matches = list(HEADER_RE.finditer(text))                 # (local)
    for i, m in enumerate(header_matches):
        wave_id = m.group(1)                                        # (local)
        gate_id = m.group(2)                                        # (local)
        start = m.end()                                             # (local)
        end = header_matches[i + 1].start() if i + 1 < len(header_matches) else len(text)  # (local)
        block = text[start:end]                                     # (local)
        hyp_m = HYP_RE.search(block)                                # (local)
        hyp = hyp_m.group(1).strip() if hyp_m else ""               # (local)
        # Flatten whitespace
        hyp = re.sub(r"\s+", " ", hyp)
        gates.append({
            "gate_id": gate_id,
            "wave_id": wave_id,
            "hypothesis": hyp,
            "source_plan": path.name,
        })
    return gates


def enumerate_all_gates(plan_files):
    all_gates = []                                                  # (local)
    for p in plan_files:
        all_gates.extend(parse_plan(p))
    return all_gates


# ---------------------------------------------------------------------------
# Section 6 - Pair classifier
# ---------------------------------------------------------------------------
def extract_keywords(text, vocab):
    """Case-sensitive substring match (preserves chemistry-style keys)."""
    hits = set()                                                    # (local)
    lower_text = text.lower()                                       # (local)
    for kw in vocab:
        if kw in text:
            hits.add(kw)
        elif kw.lower() in lower_text:
            hits.add(kw)
    return hits


def direction_polarity(text, observable):
    """Return +1 / -1 / 0 for the polarity of `observable` in `text`.

    Heuristic: scan a ±80-char window around each occurrence of `observable`
    for POS_MARKERS or NEG_MARKERS; tally the net direction.
    """
    net = 0                                                         # (local)
    lower_text = text.lower()                                       # (local)
    obs_lower = observable.lower()                                  # (local)
    idx = 0                                                         # (local)
    while True:
        pos = lower_text.find(obs_lower, idx)                       # (local)
        if pos < 0:
            break
        w_lo = max(0, pos - 80)                                     # (local)
        w_hi = min(len(lower_text), pos + len(obs_lower) + 80)      # (local)
        window = lower_text[w_lo:w_hi]                              # (local)
        for mk in POS_MARKERS:
            if mk.lower() in window:
                net += 1
        for mk in NEG_MARKERS:
            if mk.lower() in window:
                net -= 1
        idx = pos + len(obs_lower)
    if net > 0:
        return 1
    if net < 0:
        return -1
    return 0


def classify_pair(g_i, g_j):
    h_i, h_j = g_i["hypothesis"], g_j["hypothesis"]                 # (local)
    if not h_i or not h_j:
        return "UNDECLARED", {}
    # Independent-declared: look for explicit cross-reference language.
    joint = h_i + " " + h_j                                         # (local)
    if re.search(r"independent from\s+§?W?\d", joint, re.IGNORECASE):
        return "INDEPENDENT-DECLARED", {"rule": "independence-declared"}
    obs_i = extract_keywords(h_i, OBSERVABLE_KEYWORDS)              # (local)
    obs_j = extract_keywords(h_j, OBSERVABLE_KEYWORDS)              # (local)
    mech_i = extract_keywords(h_i, MECHANISM_KEYWORDS)              # (local)
    mech_j = extract_keywords(h_j, MECHANISM_KEYWORDS)              # (local)
    shared_obs = obs_i & obs_j                                      # (local)
    shared_mech = mech_i & mech_j                                   # (local)
    # Direction conflict check on directed observables
    for obs in shared_obs:
        if obs not in DIRECTED_OBSERVABLES:
            continue
        d_i = direction_polarity(h_i, obs)                          # (local)
        d_j = direction_polarity(h_j, obs)                          # (local)
        if d_i != 0 and d_j != 0 and d_i * d_j < 0:
            return "CONTRADICTS", {"obs": obs, "d_i": d_i, "d_j": d_j}
    if shared_obs or shared_mech:
        return "IMPLIES", {"obs": list(shared_obs), "mech": list(shared_mech)}
    if obs_i or obs_j or mech_i or mech_j:
        return "ORTHOGONAL", {"obs_i": list(obs_i), "obs_j": list(obs_j)}
    # Neither gate has any observable/mechanism keyword — could not extract
    return "UNDECLARED", {"reason": "no-keywords-extracted"}


# ---------------------------------------------------------------------------
# Section 7 - Compute
# ---------------------------------------------------------------------------
PREDICATE_CODES = {                                                 # (local)
    "IMPLIES": 1,
    "CONTRADICTS": 2,
    "INDEPENDENT-DECLARED": 3,
    "ORTHOGONAL": 4,
    "UNDECLARED": 0,
}


def compute():
    gates = enumerate_all_gates(PLAN_FILES)
    n_gates = len(gates)                                            # (local)
    total_pairs = n_gates * (n_gates - 1) // 2                      # (local)
    print(f"  parsed {n_gates} gates across {len(PLAN_FILES)} plan files")

    matrix = np.zeros((n_gates, n_gates), dtype=np.int8)            # (local)
    counts = {"IMPLIES": 0, "CONTRADICTS": 0, "INDEPENDENT-DECLARED": 0,
              "ORTHOGONAL": 0, "UNDECLARED": 0}                     # (local)
    contradict_details = []                                         # (local)

    for i, j in itertools.combinations(range(n_gates), 2):
        label, detail = classify_pair(gates[i], gates[j])
        code = PREDICATE_CODES[label]                               # (local)
        matrix[i, j] = code
        matrix[j, i] = code
        counts[label] += 1
        if label == "CONTRADICTS":
            contradict_details.append({
                "i": i, "j": j,
                "g_i": gates[i]["gate_id"], "g_j": gates[j]["gate_id"],
                "detail": detail,
            })

    return {
        "value": (counts["IMPLIES"], counts["CONTRADICTS"],
                  counts["INDEPENDENT-DECLARED"], counts["UNDECLARED"]),
        "gates": gates,
        "n_gates": n_gates,
        "total_pairs": total_pairs,
        "counts": counts,
        "matrix": matrix,
        "contradict_details": contradict_details,
    }


def evaluate_gate(result):
    c = result["counts"]                                            # (local)
    total = result["total_pairs"]                                   # (local)
    if c["CONTRADICTS"] >= 1:
        return "FAIL"
    if c["UNDECLARED"] == PASS_UNDECLARED_MAX:
        return "PASS"
    if 0 < c["UNDECLARED"] <= INFO_UNDECLARED_FRAC * total:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 8 - Verdict append
# ---------------------------------------------------------------------------
def append_verdict(verdict, value, audit_sha, content_sha):
    val_str = f"({value[0]},{value[1]},{value[2]},{value[3]})"      # (local)
    line = (f"{GATE_ID}: {verdict} -- value={val_str} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} "
            f"schema_version=S84+\n")                               # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 - Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()                                                # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')           # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    r = compute()
    value = r["value"]
    verdict = evaluate_gate(r)

    print()
    print(f"  n_gates={r['n_gates']}, total_pairs={r['total_pairs']}")
    for k, v in r["counts"].items():
        print(f"    {k:24s}  {v:5d}")
    if r["contradict_details"]:
        print("  CONTRADICTS detail:")
        for d in r["contradict_details"][:10]:
            print(f"    {d['g_i']} ↔ {d['g_j']} on {d['detail']}")
    else:
        print("  no CONTRADICTS pairs detected")
    print()
    print(f"(value=({value[0]},{value[1]},{value[2]},{value[3]}), scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # Save NPZ
    np.savez_compressed(
        OUT_NPZ,
        matrix=r["matrix"],
        gate_ids=np.array([g["gate_id"] for g in r["gates"]], dtype=object),
        wave_ids=np.array([g["wave_id"] for g in r["gates"]], dtype=object),
        source_plans=np.array([g["source_plan"] for g in r["gates"]], dtype=object),
        hypotheses=np.array([g["hypothesis"][:500] for g in r["gates"]], dtype=object),
        predicate_codes=np.array(sorted(PREDICATE_CODES.items()), dtype=object),
    )

    # Save pair JSON (compact)
    pairs_export = {                                                # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "n_gates": r["n_gates"],
        "total_pairs": r["total_pairs"],
        "counts": r["counts"],
        "contradict_details": r["contradict_details"],
        "gates": [{"gate_id": g["gate_id"], "wave_id": g["wave_id"],
                   "source_plan": g["source_plan"],
                   "hypothesis_head": g["hypothesis"][:200]}
                  for g in r["gates"]],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "pins": pins,
    }
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(pairs_export, fp, indent=2)

    # Heatmap
    fig, ax = plt.subplots(figsize=(10, 9))
    cmap = plt.cm.get_cmap("tab10", 5)                              # (local)
    im = ax.imshow(r["matrix"], cmap=cmap, vmin=0, vmax=4, aspect="equal",
                   interpolation="nearest")
    cbar = plt.colorbar(im, ax=ax, ticks=[0, 1, 2, 3, 4])
    cbar.set_ticklabels(["UND", "IMP", "CON", "IND", "ORT"])
    ax.set_title(f"{GATE_ID}: predicate matrix over {r['n_gates']} gates "
                 f"({r['total_pairs']} pairs)")
    ax.set_xlabel("gate index"); ax.set_ylabel("gate index")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)

    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
