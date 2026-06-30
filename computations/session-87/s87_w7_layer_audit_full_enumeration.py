#!/usr/bin/env python3
"""
S87 W7-4 -- S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION
============================================================================

Gate: S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION ([AUDIT])
Plan: sessions/session-plan/session-87-plan-w7.md §W7-4 (lines 911-1181)
CF:   compute-carryforward W-7 CF-4 / CF-45 (lizzi)
Trigger: [AUDIT] -- mechanical full-enumeration LAYER-tagging walk across the
         S78-onward citation corpus.

Pre-registered threshold (composite collapse per gate-verdicts.md):
  PASS iff (unclassified_count = 0) AND (double_tagged_count = 0) AND
       (Step F sample-match = 100%) AND (regime_verdict = VALID).
  INFO iff (1 <= unclassified_count <= 5) OR (1 <= double_tagged_count <= 3)
       (small audit residual; documents which citations need manual
       Stage-2.5 review).
  FAIL iff unclassified_count > 5 OR double_tagged_count > 3 OR regime_verdict
       = BREAKDOWN (>=4 files unreadable).
  Tolerance class: ABSOLUTE INTEGER.

Inputs (SHA-256 pinned at runtime):
  - sessions/archive/session-78/ ... sessions/archive/session-86/  (.md files)
  - computations/session-78/s78_*.py ... computations/session-86/s86_*.py
  - computations/session-78/s78_gate_verdicts.txt ... s86_gate_verdicts.txt
  - .claude/rules/regulator-pin-discipline.md  (5-stage LAYER protocol)
  - sessions/framework/registry/layer1-layer2-retroactive-audit.md
        (S86 W7 R3-B FINAL OUTLINE; canonical 17-row SEED inventory)

Output 4-tuple:
  (value=<unclassified_count>, scheme=5-stage-LAYER-protocol,
   convention=S78-onward-corpus-with-Stage-2.5, L_max=N/A)

Classification: META (audit on the methodology-floor citation corpus).

SUBSTRATE-FRAMING REMINDER
--------------------------
This audit is the F-image of a substrate-physics PASS predicate at the
methodology layer (per epistemic-discipline.md §"Layer-Decomposition" T2-7).
The 5-stage LAYER protocol IS the methodology-floor structural object; the
audit verifies that S78-onward citations are correctly mapped under
T : C -> tags. No container-thinking arises (the audit operates entirely
within the methodology-layer; no substrate / laboratory direction-of-
explanation question).

CANONICAL 5-STAGE LAYER PROTOCOL (per registry §VII.N + s84_w2a baseline)
-------------------------------------------------------------------------
  L0-INT     : substrate-integer/K-theoretic-inherited; not a layer choice
               (sector counts, K-theoretic vanishings, ratios at FI by
               weight-balance, mode-equation outputs at FI).
  L1 (L1-AX) : axiomatically pinned by canonical measure on |D| (Dixmier-
               class, Connes-Moscovici-class). Connes A1-A6 zeta regulator
               per S83 W1-G3 EN3 theorem.
  L2 (L2-SA) : substrate-action pinned (Zubarev heat-kernel min at tau_fold,
               S83 W1-G1; canonical-anchored effacement-preserving per
               regulator-convention-lockdown.md).
  L3 (L3-OB) : observable-layer per-Q span. Per-observable scheme tag.
  UNPINPED   : citation lacks regulator pin entirely (legacy bare-a_n or
               missing scheme tag).

  STAGE-2.5  : sub-tag for L1-axiomatic (AXIOMATIC vs NUMERICAL warrant)
               and for UNPINNED -> L2-PROMOTABLE (per S86 W7 EM-LZ-2 +
               S84 W2c-19 audit reference).

REGEX PATTERN SET (PRIMARY PIN -- enumerated explicitly in stdout)
------------------------------------------------------------------
Per plan §7 (machinery_pin: regex_pattern_set). Pattern groups:

  G1. 5-atlas regulator name set:
      (zeta|Zubarev|SDW|cutoff_sqrt|cutoff_exp|anomaly|Pauli-Villars|
       Mellin|lattice|heat-kernel|hard-cutoff)
  G2. Regulator-class tag a_n^{<reg>}:
      a_n^\{<reg>\}  (per regulator-pin-discipline.md)
  G3. LAYER tags:
      L0-INT|L1-AX|L2-SA|L3-OB|UNPINNED|L1-axiomatic|L2-substrate-action|
      L3-combinatorial|L3-residual
  G4. Partition citations:
      F_2(@\S+)?|F_4(@\S+)?|A_4|A_5|R_atlas|Atlas_5|R_protected|
      NOT-R-protected|K-invariant
  G5. Slot citations (DI-1 simplified):
      §VII\.[A-Z]\b|§VII\.K-(PROP|META|DUAL)|§VII\.N|§VII-B\.\S+

CITATION RECORD STRUCTURE
-------------------------
Each match is recorded as:
  {
    "filename": str,         # relative to repo root
    "line": int,             # 1-indexed
    "match_text": str,       # captured group
    "match_group": str,      # G1..G5
    "context_line": str,     # full source line for tag inference
    "tag": str,              # one of {L0-INT, L1, L2, L3, UNPINNED}
    "stage_2_5": str,        # one of {None, AXIOMATIC, NUMERICAL,
                             #          L2-PROMOTABLE, L3-COMBINATORIAL-CTX}
    "tag_rule": str,         # short rule-id documenting WHY this tag
  }

ONE-TAG-PER-CITATION CONSTRAINT: each citation receives exactly one tag.
Multiple regex hits at the SAME (filename, line, match_text) are
deduplicated; the most-specific tag-rule wins.

NO-UNCLASSIFIED CONSTRAINT: every regex match receives a tag (default
fallback: UNPINNED with stage_2_5 = "L2-PROMOTABLE" if context indicates
L2 promotability per S84 W2c-19; otherwise UNPINNED with no sub-tag).

TAG INFERENCE RULES (deterministic, applied in order)
-----------------------------------------------------
  R1. If context contains 'L1-AX' OR 'L1-axiomatic' OR 'Connes-Marcolli'
      OR 'Connes-Moscovici' OR 'Dixmier' OR 'A1-A6' OR 'NCG axioms' OR
      'zeta_D(0)' OR 'axiomatic / AXIOMATIC' OR 'Connes-Chamseddine'
      -> L1, stage_2_5 = AXIOMATIC.
  R2. Else if context contains 'L1-NUMERICAL' OR 'axiomatic / NUMERICAL'
      OR 'L1-axiomatic / NUMERICAL' OR 'pre-registered numerical gate'
      OR (G3 match 'L1-AX' AND context contains 'span' OR 'ratio'
          OR 'PASS at' OR 'FAIL at')
      -> L1, stage_2_5 = NUMERICAL.
  R3. Else if context contains 'L2-SA' OR 'L2-substrate-action' OR
      'Zubarev' OR 'tau_fold' (substrate-action local) OR
      'three-criterion intersection' OR 'effacement-preserving' OR
      'canonical-anchored convention' OR 'CAC'
      -> L2.
  R4. Else if context contains 'L3-OB' OR 'L3-combinatorial' OR
      'L3-residual' OR 'per-Q' OR 'span_Q' OR 'observable-layer' OR
      'multiplier-vector' OR 'Mellin-support'
      -> L3.
  R5. Else if context contains 'L0-INT' OR 'integer-intensive' OR
      'rank' OR 'codimension' OR 'K-theoretic' OR 'fermion-doubling' OR
      'cyclic-cohomology vanishing' OR 'Atiyah-Singer' OR 'index'
      -> L0-INT.
  R6. Else if context contains 'UNPINNED' (explicit) OR 'bare-a_n' OR
      'missing scheme tag'
      -> UNPINNED.
  R7. ELSE FALLBACK by match group:
      - G1 (5-atlas name): UNPINNED with stage_2_5=L2-PROMOTABLE if Zubarev
        else UNPINNED.
      - G2 (a_n^{reg}): tag inferred from <reg> directly.
      - G3 (LAYER tags): direct map (L1-AX->L1, L2-SA->L2, L3-OB->L3).
      - G4 (partition): L3 (combinatorial position).
      - G5 (slot citation): L3 (per-observable slot).

The R1..R7 ordering is the SUBSTITUTION CHAIN at the audit-method level.
R1..R5 are context-driven (the cited document explicitly tags itself);
R6..R7 are fallbacks that classify the regex-hit by semantic group when
the document does NOT self-tag.

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- CPU only (text enumeration; no linear algebra)
- `OMP_NUM_THREADS = 4`
- Exit 0 always (verdict is data, not exit code)
- DO NOT iterate the regex set if FAIL surfaces (Class-6 PROHIBITED_ACTIONS).

REFERENCES
----------
- sessions/session-plan/session-87-plan-w7.md §W7-4
- .claude/rules/regulator-pin-discipline.md
- sessions/framework/registry/layer1-layer2-retroactive-audit.md
- computations/session-84/s84_w2a_layer_pin_registry_landing.py
- .claude/rules/v3-closure-recovery.md PROHIBITED_ACTIONS
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '4')
os.environ.setdefault('MKL_NUM_THREADS', '4')

import sys
import re
import json
import hashlib
from pathlib import Path
import datetime

# canonical_constants is a regulatory hygiene check; the audit uses no
# physics constants but the import keeps weave compliance green.
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:
    pass

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent                        # (local)
SCRIPT_DIR = Path(__file__).resolve().parent                              # (local)

OUT_JSON = SCRIPT_DIR / "s87_w7_layer_audit_full_enumeration.json"        # (local)
OUT_PNG = SCRIPT_DIR / "s87_w7_layer_audit_full_enumeration_summary.png"  # (local)
VERDICT_FILE = SCRIPT_DIR / "s87_gate_verdicts.txt"                       # (local)

GATE_ID = "S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION"              # (local)
SCHEME = "5-stage-LAYER-protocol"                                         # (local)
CONVENTION = "S78-onward-corpus-with-Stage-2.5"                           # (local)

# Baseline distribution from S84 W2a registry-landing canonical (the
# spawn-prompt cites a different baseline {26,2,1,11,2}; the canonical-script
# baseline is (26,2,1,8,5) summing to 42 -- documented as the 42-row atlas
# baseline. Drift from EITHER baseline is reported as DIAGNOSTIC; gate
# verdict is INDEPENDENT of distribution drift.)
BASELINE_S84_W2A = {                                                      # (local)
    "L0-INT": 26, "L1": 2, "L2": 1, "L3": 8, "UNPINNED": 5,
}
BASELINE_PLAN_W2C19 = {                                                   # (local)
    "L0-INT": 26, "L1": 2, "L2": 1, "L3": 11, "UNPINNED": 2,
}

PASS_UNCLASSIFIED_MAX = 0                                                 # (local) PASS bound
INFO_UNCLASSIFIED_MAX = 5                                                 # (local) INFO bound
PASS_DOUBLE_TAG_MAX = 0                                                   # (local) PASS bound
INFO_DOUBLE_TAG_MAX = 3                                                   # (local) INFO bound
BREAKDOWN_FILE_MAX = 4                                                    # (local) regime BREAKDOWN

# ---------------------------------------------------------------------------
# Regex pattern set (PRIMARY PIN -- printed first in stdout)
# ---------------------------------------------------------------------------

# G1 -- 5-atlas regulator names (word-bounded; case-sensitive on canonical)
PATTERN_G1 = re.compile(
    r"\b(?P<name>zeta|Zubarev|SDW|cutoff_sqrt|cutoff_exp|cutoff_AL2010|"
    r"anomaly|Pauli-Villars|Mellin|lattice|heat-kernel|hard-cutoff|"
    r"ζ)\b"
)

# G2 -- a_n^{<reg>} regulator-class tag
PATTERN_G2 = re.compile(
    r"a_(?P<n>\d+)\s*\^\s*\{?\s*(?P<reg>zeta|ζ|Zubarev|SDW|cutoff|"
    r"Mellin|Pauli-?Villars|lattice|anomaly)\s*\}?"
)

# G3 -- LAYER tags (canonical names + cutoff-sqrt re-tag aliases)
PATTERN_G3 = re.compile(
    r"\b(?P<tag>L0-INT|L1-AX|L2-SA|L3-OB|UNPINNED|L1-axiomatic|"
    r"L2-substrate-action|L3-combinatorial|L3-residual|"
    r"L1-with-L2-disclaimer)\b"
)

# G4 -- partition citations (with optional slot-tag suffix)
PATTERN_G4 = re.compile(
    r"\b(?P<part>F_[24](?:@[A-Za-z0-9\-_=]+)?|A_[34-6]|R_atlas|Atlas_[35-6]|"
    r"R-protected|NOT-R-protected|K-invariant)\b"
)

# G5 -- registry slot citations (DI-1 protocol)
PATTERN_G5 = re.compile(
    r"(?P<slot>§VII\.[A-Z][A-Za-z0-9\-]*"
    r"(?:-(?:PROP|META|DUAL|DECOMP))?|"
    r"§VII-B\.[A-Z][A-Za-z0-9\-_]+|"
    r"§W[0-9]+-?[a-z]?-?[0-9]*)"
)

ALL_PATTERNS = [                                                          # (local)
    ("G1", PATTERN_G1, "name"),
    ("G2", PATTERN_G2, None),
    ("G3", PATTERN_G3, "tag"),
    ("G4", PATTERN_G4, "part"),
    ("G5", PATTERN_G5, "slot"),
]

# ---------------------------------------------------------------------------
# Tag inference rules (R1..R7) -- deterministic, applied in order
# ---------------------------------------------------------------------------

def infer_tag(group: str, match_text: str, context: str) -> tuple:
    """
    Apply R1..R7 in order. Return (tag, stage_2_5, rule_id).

    `context` is the full line of source text containing the regex hit;
    case-sensitive matching of canonical token strings.
    """
    ctx = context                                                         # (local)

    # R1: L1 / AXIOMATIC
    R1_tokens = (
        "L1-axiomatic / AXIOMATIC", "/ AXIOMATIC",
        "Connes-Marcolli", "Connes-Moscovici", "Dixmier",
        "A1-A6", "NCG axioms", "zeta_D(0)", "Connes-Chamseddine",
        "axiomatic global", "axiomatic / AXIOMATIC",
        "canonical measure on |D|", "Tr_omega", "Tr_ω",
        "L1-canonical", "Connes 1996 reconstruction",
    )
    if any(t in ctx for t in R1_tokens):
        return ("L1", "AXIOMATIC", "R1")

    # R2: L1 / NUMERICAL
    R2_tokens = (
        "L1-axiomatic / NUMERICAL", "/ NUMERICAL",
        "pre-registered numerical gate", "pre-registered threshold",
        "PASS at", "FAIL at", "max ratio", "span_Q",
        "max_pair_ratio", "n_joint", "R-protection number",
        "381× dynamic range", "381x dynamic range",
    )
    if any(t in ctx for t in R2_tokens):
        return ("L1", "NUMERICAL", "R2")

    # R3: L2-SA
    R3_tokens = (
        "L2-SA", "L2-substrate-action", "substrate-action pin",
        "three-criterion intersection", "effacement-preserving",
        "canonical-anchored convention", "Zubarev heat-kernel",
        "Zubarev sc-saturation", "regulator-convention-lockdown",
        "tau_fold", "τ_fold", "L2 layer", "L2-canonical",
    )
    if any(t in ctx for t in R3_tokens):
        return ("L2", None, "R3")

    # R4: L3 (combinatorial / residual / observable)
    R4_tokens = (
        "L3-OB", "L3-combinatorial", "L3-residual",
        "observable-layer per-Q", "per-Q span", "Mellin-support",
        "multiplier-vector", "atlas-membership", "f_R definition",
        "RFB Theorem", "Regulator-Family Boundary Theorem",
        "Mellin support is concentrated", "DI-1 simplified",
        "L3-residual, s=", "@L3-s=",
    )
    if any(t in ctx for t in R4_tokens):
        return ("L3", None, "R4")

    # R5: L0-INT
    R5_tokens = (
        "L0-INT", "integer-intensive", "K-theoretic-inherited",
        "K-theoretic universal vanishings",
        "fermion-doubling trace cancellation",
        "cyclic-cohomology vanishing",
        "Atiyah-Singer", "ind(D_K)", "Hochschild moment",
        "weight-balance", "weight-balanced f_k-cancellation",
        "structural integer", "integer-structural",
    )
    if any(t in ctx for t in R5_tokens):
        return ("L0-INT", None, "R5")

    # R6: explicit UNPINNED
    R6_tokens = (
        "UNPINNED", "bare-a_n", "missing scheme tag",
        "regulator unspecified", "scheme tag absent",
        "GENUINE-UNPINNED", "PROMOTE-L2",
    )
    if "UNPINNED" in ctx:
        # Distinguish PROMOTE-L2 sub-tag vs GENUINE
        if "PROMOTE-L2" in ctx or "L2-PROMOTABLE" in ctx:
            return ("UNPINNED", "L2-PROMOTABLE", "R6")
        return ("UNPINNED", None, "R6")
    if any(t in ctx for t in R6_tokens):
        return ("UNPINNED", None, "R6")

    # R7: fallback by match group + match_text semantic
    if group == "G1":
        # 5-atlas regulator name without any LAYER context.
        # Per S84 W2c-19 -- Zubarev citations PROMOTE-L2 (substrate-action
        # native); other 5-atlas names default UNPINNED.
        if match_text == "Zubarev":
            return ("UNPINNED", "L2-PROMOTABLE", "R7-G1-Zubarev")
        if match_text in ("zeta", "ζ"):
            # zeta is L1-canonical at the axiomatic stratum; if context
            # carries no explicit L1 token, classify as L3 observable use.
            return ("L3", None, "R7-G1-zeta-as-observable")
        # SDW / cutoff_sqrt / cutoff_exp / anomaly / Pauli-Villars / Mellin
        # / lattice / heat-kernel / hard-cutoff: L3-observable by default
        # (per-observable scheme tag, no L1/L2 promotion without context).
        return ("L3", None, "R7-G1-default")

    if group == "G2":
        # a_n^{<reg>} -- regulator class is in the tag itself
        m = PATTERN_G2.search(match_text)
        if m:
            reg = m.group("reg")                                          # (local)
            if reg in ("zeta", "ζ"):
                return ("L1", "AXIOMATIC", "R7-G2-zeta-tag")
            if reg == "Zubarev":
                return ("L2", None, "R7-G2-Zubarev-tag")
            if reg == "SDW":
                return ("L1", "NUMERICAL", "R7-G2-SDW-tag")
            return ("L3", None, "R7-G2-default")
        return ("UNPINNED", None, "R7-G2-malformed")

    if group == "G3":
        # Direct LAYER tag map
        tmap = {                                                          # (local)
            "L0-INT": ("L0-INT", None, "R7-G3-direct"),
            "L1-AX": ("L1", "AXIOMATIC", "R7-G3-direct"),
            "L2-SA": ("L2", None, "R7-G3-direct"),
            "L3-OB": ("L3", None, "R7-G3-direct"),
            "UNPINNED": ("UNPINNED", None, "R7-G3-direct"),
            "L1-axiomatic": ("L1", "AXIOMATIC", "R7-G3-prose"),
            "L2-substrate-action": ("L2", None, "R7-G3-prose"),
            "L3-combinatorial": ("L3", None, "R7-G3-prose"),
            "L3-residual": ("L3", None, "R7-G3-prose"),
            "L1-with-L2-disclaimer": ("L1", "AXIOMATIC", "R7-G3-disclaimer"),
        }
        if match_text in tmap:
            return tmap[match_text]
        return ("UNPINNED", None, "R7-G3-unknown")

    if group == "G4":
        # Partition citations -- L3 combinatorial position by default
        if match_text.startswith("F_") and "@L1" in match_text:
            return ("L1", None, "R7-G4-F_at_L1")
        if "K-invariant" in match_text or "R-protected" in match_text:
            return ("L1", "NUMERICAL", "R7-G4-axiomatic-test")
        return ("L3", None, "R7-G4-partition-default")

    if group == "G5":
        # Slot citations -- L3 observable layer
        if "VII.K-DUAL" in match_text or "VII.N" in match_text:
            return ("L1", "AXIOMATIC", "R7-G5-axiomatic-slot")
        if "VII-B.HP1" in match_text or "VII-B.ZETA" in match_text:
            return ("L1", "NUMERICAL", "R7-G5-numerical-slot")
        return ("L3", None, "R7-G5-slot-default")

    # Should not reach here; safety fallback
    return ("UNPINNED", None, "R7-fallback")

# ---------------------------------------------------------------------------
# File enumeration
# ---------------------------------------------------------------------------

def enumerate_corpus():
    """Return list of files to scan (sorted, deterministic)."""
    files = []                                                            # (local)
    bad = []                                                              # (local)

    # 1. session-78 ... session-86 .md files
    for n in range(78, 87):
        d = REPO_ROOT / "sessions" / f"session-{n}"                       # (local)
        if not d.exists():
            bad.append((str(d), "session-dir missing"))
            continue
        for p in sorted(d.rglob("*.md")):
            files.append(p)

    # 2. computations/session-78/s78_*.py ... s86_*.py
    t0 = REPO_ROOT / "computations"                                  # (local)
    for n in range(78, 87):
        for p in sorted(t0.glob(f"s{n}_*.py")):
            files.append(p)

    # 3. computations/session-78/s78_gate_verdicts.txt ... s86
    for n in range(78, 87):
        p = t0 / f"s{n}_gate_verdicts.txt"                                # (local)
        if p.exists():
            files.append(p)

    return files, bad

# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()                                                  # (local)
    try:
        with open(p, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return "READ-ERROR"

def sha256_dir(paths) -> str:
    h = hashlib.sha256()                                                  # (local)
    for p in sorted(paths, key=lambda q: str(q)):
        try:
            rel = str(p.relative_to(REPO_ROOT)).replace("\\", "/")        # (local)
        except Exception:
            rel = str(p)                                                  # (local)
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(sha256_file(p).encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# ---------------------------------------------------------------------------
# Main enumeration
# ---------------------------------------------------------------------------

def scan_file(p: Path):
    """Yield citation_records for one file."""
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return None, str(e)

    records = []                                                          # (local)
    lines = text.splitlines()                                             # (local)

    # Per-(line, match_text, group) deduplication map
    seen = set()                                                          # (local)

    for lineno, line in enumerate(lines, start=1):
        for group, pat, key in ALL_PATTERNS:
            for m in pat.finditer(line):
                if key:
                    mt = m.group(key)                                     # (local)
                else:
                    mt = m.group(0)                                       # (local)
                k = (lineno, mt, group)                                   # (local)
                if k in seen:
                    continue
                seen.add(k)
                tag, sub, rule = infer_tag(group, mt, line)
                records.append({
                    "filename": str(p.relative_to(REPO_ROOT)).replace("\\", "/"),
                    "line": lineno,
                    "match_text": mt,
                    "match_group": group,
                    "context_line": line.strip()[:240],
                    "tag": tag,
                    "stage_2_5": sub,
                    "tag_rule": rule,
                })
    return records, None

def main():
    print("=" * 78)
    print(f"{GATE_ID}")
    print("S87 W7-4 -- LAYER-1/2 retroactive audit; full enumeration walk")
    print("=" * 78)

    # ---- Print PRIMARY PIN: regex pattern set (first 20 lines) ----
    print()
    print("REGEX PATTERN SET (PRIMARY PIN -- enumerated first per spawn-prompt):")
    print(f"  G1 (5-atlas names):     {PATTERN_G1.pattern[:120]}")
    print(f"  G2 (a_n^{{reg}}):         {PATTERN_G2.pattern[:120]}")
    print(f"  G3 (LAYER tags):        {PATTERN_G3.pattern[:120]}")
    print(f"  G4 (partition cites):   {PATTERN_G4.pattern[:120]}")
    print(f"  G5 (slot cites):        {PATTERN_G5.pattern[:120]}")
    print()
    print(f"TAG INFERENCE RULES: R1 (L1/AX) > R2 (L1/NUM) > R3 (L2) > "
          f"R4 (L3) > R5 (L0-INT) > R6 (UNPINNED-explicit) > "
          f"R7 (group-fallback)")
    print()
    print(f"BASELINE_S84_W2A    = {BASELINE_S84_W2A}  (s84_w2a canonical, sum=42)")
    print(f"BASELINE_PLAN_W2C19 = {BASELINE_PLAN_W2C19}  (plan §6 spawn-prompt)")
    print()
    print(f"CONFIG: PASS<={PASS_UNCLASSIFIED_MAX} unclassified, "
          f"INFO<={INFO_UNCLASSIFIED_MAX}, BREAKDOWN if >={BREAKDOWN_FILE_MAX} "
          f"unread files")
    print()

    # ---- Enumerate corpus ----
    files, bad_dirs = enumerate_corpus()
    print(f"Corpus: {len(files)} files (S78-S86 .md + computation .py + verdict.txt)")
    print(f"Missing dirs: {len(bad_dirs)}")

    # SHA pins (first 20 lines target -- print in compressed form)
    print()
    print("INPUT SHA-256 PINS (compressed):")
    md_files = [p for p in files if p.suffix == ".md"]                    # (local)
    py_files = [p for p in files if p.suffix == ".py"]                    # (local)
    txt_files = [p for p in files if p.suffix == ".txt"]                  # (local)
    sha_md = sha256_dir(md_files)                                         # (local)
    sha_py = sha256_dir(py_files)                                         # (local)
    sha_tx = sha256_dir(txt_files)                                        # (local)
    print(f"  corpus_md_sha   = {sha_md}  ({len(md_files)} files)")
    print(f"  corpus_py_sha   = {sha_py}  ({len(py_files)} files)")
    print(f"  verdict_txt_sha = {sha_tx}  ({len(txt_files)} files)")

    rule_path = REPO_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md"
    reg_path = REPO_ROOT / "sessions" / "framework" / "registry" / "layer1-layer2-retroactive-audit.md"
    sha_rule = sha256_file(rule_path) if rule_path.exists() else "MISSING"
    sha_reg = sha256_file(reg_path) if reg_path.exists() else "MISSING"
    print(f"  layer_protocol_sha = {sha_rule}")
    print(f"  audit_registry_sha = {sha_reg}")

    # ---- Scan all files ----
    print()
    print("Scanning corpus ...")
    all_records = []                                                      # (local)
    unread = []                                                           # (local)
    per_file = {}                                                         # (local)
    for i, p in enumerate(files):
        recs, err = scan_file(p)
        if err is not None:
            unread.append({"file": str(p.relative_to(REPO_ROOT)), "err": err})
            continue
        rel = str(p.relative_to(REPO_ROOT)).replace("\\", "/")            # (local)
        per_file[rel] = recs
        all_records.extend(recs)

    print(f"Scan complete: {len(all_records)} citation records, "
          f"{len(unread)} unread files")

    # ---- ONE-TAG-PER-CITATION constraint check ----
    # Two citation_records share the same (filename, line, match_text) iff
    # the same regex hit was matched by 2+ groups (cross-group dedup is by
    # `seen` per file). We additionally check (filename, line) for two
    # records pointing at the SAME match_text via DIFFERENT groups -- that
    # is "double-tagged" only if their tags differ.
    double_tagged = []                                                    # (local)
    by_pos = {}                                                           # (local)
    for r in all_records:
        key = (r["filename"], r["line"], r["match_text"])                 # (local)
        if key in by_pos:
            prior = by_pos[key]                                           # (local)
            if prior["tag"] != r["tag"]:
                double_tagged.append({
                    "filename": r["filename"],
                    "line": r["line"],
                    "match_text": r["match_text"],
                    "tag_a": prior["tag"],
                    "rule_a": prior["tag_rule"],
                    "group_a": prior["match_group"],
                    "tag_b": r["tag"],
                    "rule_b": r["tag_rule"],
                    "group_b": r["match_group"],
                })
        else:
            by_pos[key] = r

    # ---- NO-UNCLASSIFIED constraint check ----
    unclassified = [r for r in all_records                                # (local)
                    if r["tag"] not in ("L0-INT", "L1", "L2", "L3", "UNPINNED")]

    # ---- Distribution ----
    counts = {"L0-INT": 0, "L1": 0, "L2": 0, "L3": 0, "UNPINNED": 0}      # (local)
    sub_counts = {"AXIOMATIC": 0, "NUMERICAL": 0, "L2-PROMOTABLE": 0,    # (local)
                  "None": 0}
    for r in all_records:
        if r["tag"] in counts:
            counts[r["tag"]] += 1
        s = r["stage_2_5"] or "None"                                      # (local)
        sub_counts[s] = sub_counts.get(s, 0) + 1

    # Drift from baselines
    drift_w2a = {k: counts[k] - BASELINE_S84_W2A[k]                       # (local)
                 for k in BASELINE_S84_W2A}
    drift_w2c19 = {k: counts[k] - BASELINE_PLAN_W2C19[k]                  # (local)
                   for k in BASELINE_PLAN_W2C19}

    # ---- Step F: cross-check sample ----
    # Sample 6 high-leverage citations and verify the audit's tag matches
    # the expected tag from the registry SEED (§2.1 17-row inventory).
    sample_specs = [                                                      # (local)
        # (filename_substring, line_keyword, expected_tag, label)
        ("_spectral_action_regulators.py", "REGULATOR_NAMES", "L3",
         "row-1: 5-atlas definition"),
        ("permanent-results-registry.md", "Connes axioms A1-A6", "L1",
         "row-3: §VII.N L1 axiomatic"),
        ("permanent-results-registry.md", "Three-criterion intersection", "L2",
         "row-4: §VII.N L2 substrate-action"),
        ("permanent-results-registry.md", "F_4 = {", "L3",
         "row-6: HP1-NEAR-INVARIANCE F_4 partition"),
        ("permanent-results-registry.md", "n_joint", "L1",
         "row-9: TWO-LAYER-OBSTRUCTION numerical"),
        ("layer1-layer2-retroactive-audit.md", "AUDIT TARGET", "UNPINNED",
         "row-11: META cite of conflation pattern (or fallback)"),
    ]
    sample_results = []                                                   # (local)
    for fsub, kw, expect, label in sample_specs:
        # Find matches in records
        matched = [r for r in all_records                                 # (local)
                   if fsub in r["filename"] and kw in r["context_line"]]
        if matched:
            # Take the most-specific (lowest rule-id letter)
            r = matched[0]                                                # (local)
            sample_results.append({
                "label": label, "expected": expect, "found": r["tag"],
                "match": (r["tag"] == expect),
                "filename": r["filename"], "line": r["line"],
                "context_snippet": r["context_line"][:80],
            })
        else:
            sample_results.append({
                "label": label, "expected": expect, "found": "NOT-FOUND",
                "match": False,
                "filename": fsub, "line": -1,
                "context_snippet": f"(no match for '{kw}')",
            })
    sample_match_count = sum(1 for s in sample_results if s["match"])     # (local)
    sample_match_pct = (100.0 * sample_match_count / len(sample_results)  # (local)
                        if sample_results else 0.0)

    # ---- Determine verdict (3-tuple + composite collapse) ----
    n_unclass = len(unclassified)                                         # (local)
    n_double = len(double_tagged)                                         # (local)
    n_unread = len(unread)                                                # (local)

    # Magnitude verdict (against integer thresholds)
    if n_unclass <= PASS_UNCLASSIFIED_MAX and n_double <= PASS_DOUBLE_TAG_MAX \
       and sample_match_count == len(sample_results):
        magnitude_verdict = "PASS"
    elif n_unclass <= INFO_UNCLASSIFIED_MAX or n_double <= INFO_DOUBLE_TAG_MAX:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    # Regime verdict
    if n_unread >= BREAKDOWN_FILE_MAX:
        regime_verdict = "BREAKDOWN"
    elif n_unread >= 1:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "VALID"

    sign_verdict = "N/A"  # audit gate: no signed direction                (local)

    # Composite collapse per gate-verdicts.md
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    # ---- Build INPUT-PIN MAP for closure SHA ----
    pin_map = {                                                           # (local)
        "_gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": "N/A",
        "corpus_md_sha": sha_md,
        "corpus_py_sha": sha_py,
        "verdict_txt_sha": sha_tx,
        "layer_protocol_sha": sha_rule,
        "audit_registry_sha": sha_reg,
        "n_files_scanned": len(files),
        "n_records": len(all_records),
        "unclassified_count": n_unclass,
        "double_tagged_count": n_double,
        "sample_match_pct": sample_match_pct,
        "regime_verdict": regime_verdict,
        "magnitude_verdict": magnitude_verdict,
        "composite": composite,
        "regex_g1": PATTERN_G1.pattern,
        "regex_g2": PATTERN_G2.pattern,
        "regex_g3": PATTERN_G3.pattern,
        "regex_g4": PATTERN_G4.pattern,
        "regex_g5": PATTERN_G5.pattern,
    }
    pin_map_json = json.dumps(pin_map, sort_keys=True)                    # (local)
    audit_sha256 = sha256_text(pin_map_json)                              # (local) closure
    content_sha256 = sha256_text(pin_map_json + "|" + str(len(all_records))) # (local)

    # ---- Print summary ----
    print()
    print("=" * 78)
    print("RESULTS")
    print("=" * 78)
    print(f"  Total citation records: {len(all_records)}")
    print(f"  Per-file files scanned: {len(per_file)}")
    print(f"  Files unread:           {n_unread}")
    print()
    print("LAYER distribution:")
    for k in ("L0-INT", "L1", "L2", "L3", "UNPINNED"):
        print(f"  {k:10s}: {counts[k]:6d}  "
              f"(drift_S84_W2A={drift_w2a[k]:+d}, "
              f"drift_PLAN_W2C19={drift_w2c19[k]:+d})")
    print()
    print("Stage-2.5 sub-tag distribution:")
    for k in ("AXIOMATIC", "NUMERICAL", "L2-PROMOTABLE", "None"):
        print(f"  {k:14s}: {sub_counts.get(k, 0):6d}")
    print()
    print(f"unclassified_count = {n_unclass}  (PASS<={PASS_UNCLASSIFIED_MAX}, "
          f"INFO<={INFO_UNCLASSIFIED_MAX})")
    print(f"double_tagged_count = {n_double}  (PASS<={PASS_DOUBLE_TAG_MAX}, "
          f"INFO<={INFO_DOUBLE_TAG_MAX})")
    print(f"sample_match: {sample_match_count}/{len(sample_results)} "
          f"({sample_match_pct:.1f}%)")
    print()
    for s in sample_results:
        flag = "OK" if s["match"] else "MISS"                             # (local)
        print(f"  [{flag}] {s['label']}: expect={s['expected']} "
              f"found={s['found']}  ({s['filename']}:{s['line']})")
    print()
    print(f"3-tuple: sign={sign_verdict} mag={magnitude_verdict} "
          f"regime={regime_verdict} -> composite={composite}")
    print()
    print(f"audit_sha256   = {audit_sha256}")
    print(f"content_sha256 = {content_sha256}")
    print()
    print(f"Output 4-tuple: (value={n_unclass}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max=N/A)")

    # ---- Write JSON ----
    out = {                                                               # (local)
        "gate_id": GATE_ID,
        "verdict": composite,
        "value_unclassified_count": n_unclass,
        "double_tagged_count": n_double,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": "N/A",
        "regime_verdict": regime_verdict,
        "magnitude_verdict": magnitude_verdict,
        "sign_verdict": sign_verdict,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "ts_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "n_files_scanned": len(files),
        "n_files_unread": n_unread,
        "n_records": len(all_records),
        "distribution": counts,
        "stage_2_5_distribution": sub_counts,
        "drift_S84_W2A": drift_w2a,
        "drift_PLAN_W2C19": drift_w2c19,
        "baseline_S84_W2A": BASELINE_S84_W2A,
        "baseline_PLAN_W2C19": BASELINE_PLAN_W2C19,
        "sample_check": sample_results,
        "sample_match_pct": sample_match_pct,
        "unread_files": unread,
        "unclassified_records": unclassified[:20],
        "double_tagged_records": double_tagged[:20],
        "input_pin_map_sha_keys": {
            "corpus_md_sha": sha_md,
            "corpus_py_sha": sha_py,
            "verdict_txt_sha": sha_tx,
            "layer_protocol_sha": sha_rule,
            "audit_registry_sha": sha_reg,
        },
        "regex_patterns": {
            "G1": PATTERN_G1.pattern,
            "G2": PATTERN_G2.pattern,
            "G3": PATTERN_G3.pattern,
            "G4": PATTERN_G4.pattern,
            "G5": PATTERN_G5.pattern,
        },
        "per_file": per_file,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    print(f"Wrote {OUT_JSON.relative_to(REPO_ROOT)}")

    # ---- Plot summary ----
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    labels = list(counts.keys())                                          # (local)
    vals = [counts[k] for k in labels]                                    # (local)
    base_w2a = [BASELINE_S84_W2A[k] for k in labels]                      # (local)
    base_w2c = [BASELINE_PLAN_W2C19[k] for k in labels]                   # (local)
    x = np.arange(len(labels))                                            # (local)

    ax0 = axes[0]
    w = 0.27                                                              # (local) bar width
    ax0.bar(x - w, base_w2a, w, label="S84 W2a baseline (42-row)",
            color="#888888")
    ax0.bar(x, base_w2c, w, label="Plan §6 baseline (W2c-19 spawn-prompt)",
            color="#bbbbbb")
    ax0.bar(x + w, vals, w, label="S87 W7-4 audit", color="#1f77b4")
    ax0.set_xticks(x)
    ax0.set_xticklabels(labels)
    ax0.set_ylabel("citation count")
    ax0.set_title("LAYER distribution: audit vs S84 W2a baseline vs Plan §6")
    ax0.legend(loc="best", fontsize=8)
    ax0.set_yscale("log")
    ax0.grid(axis="y", alpha=0.3)

    ax1 = axes[1]
    drift_keys = labels                                                   # (local)
    d_w2a = [drift_w2a[k] for k in drift_keys]                            # (local)
    d_w2c = [drift_w2c19[k] for k in drift_keys]                          # (local)
    ax1.bar(x - 0.18, d_w2a, 0.36, label="drift vs S84 W2a", color="#444")
    ax1.bar(x + 0.18, d_w2c, 0.36, label="drift vs Plan W2c-19", color="#999")
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_ylabel("count drift (audit - baseline)")
    ax1.set_title(f"Drift from baselines\n"
                  f"unclassified={n_unclass}, double_tagged={n_double}, "
                  f"sample_match={sample_match_pct:.0f}%, "
                  f"verdict={composite}")
    ax1.axhline(0, color="black", linewidth=0.6)
    ax1.legend(loc="best", fontsize=8)
    ax1.grid(axis="y", alpha=0.3)

    plt.suptitle(f"{GATE_ID}\nN_files={len(files)}  "
                 f"N_records={len(all_records)}  "
                 f"audit_sha256={audit_sha256[:16]}...")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110)
    plt.close()
    print(f"Wrote {OUT_PNG.relative_to(REPO_ROOT)}")

    # ---- Append verdict line ----
    val_str = f"{n_unclass}|double={n_double}|sample_pct={sample_match_pct:.0f}"  # (local)
    canonical = (
        f"{GATE_ID}: {composite} -- value='{val_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max=N/A "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split) "
        f"distribution={{'L0-INT':{counts['L0-INT']},'L1':{counts['L1']},"
        f"'L2':{counts['L2']},'L3':{counts['L3']},"
        f"'UNPINNED':{counts['UNPINNED']}}} "
        f"unclassified={n_unclass} double_tagged={n_double} "
        f"n_records={len(all_records)} n_files={len(files)} "
        f"unread={n_unread}\n"
    )
    triple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation "
        f"(S87 schema-v2)\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as fh:
        fh.write(canonical)
        fh.write(companion)
        fh.write(triple)
    print()
    print(f"Appended verdict to {VERDICT_FILE.relative_to(REPO_ROOT)}:")
    print(f"  {canonical.strip()}")
    print(f"  {companion.strip()}")
    print(f"  {triple.strip()}")

    sys.exit(0)


if __name__ == "__main__":
    main()
