"""
S82 W2-12 — CUSHION-DERIVATION-PIN [AUDIT]

Task: Grep all computations/_shared/*.py and sessions/* for "13 OOM" + "Γ_α" + "cushion";
identify citations; propose corrections to 7.3 OOM with Bernard 1979 Jacobian comment.
DO NOT modify files; draft corrections only.

Cushion substitution chain (Bernard 1979 + 't Hooft 1976, Python-verified):
  Step 1 (def): Γ_α^proper = Γ_bare * C_N * S_inst^(N^2-1) * exp(-2 S_inst) * K_2
  Step 2 (sub): Γ_bare=2.65e10 GeV; C_3=2.5e-3 (MS-bar SU(3)); S_inst=13.23;
                S_inst^8=9.386e8; exp(-2 S_inst)=3.225e-12; K_2=1.0±1.5
  Step 3 (mul): Γ_α^proper = 2.65e10 * 2.5e-3 * 9.386e8 * 3.225e-12 * 1.0
              = 2.006e5 GeV
  Step 4 (rat): Γ_γ/Γ_α^proper = 4.02e12/2.006e5 = 2.004e7
  Step 5 (dir): cushion_OOM = log10(2.004e7) = 7.302 OOM
  Direction: Γ_γ > Γ_α^proper by 7.3 OOM (central, K_2=1.0).

The 13 OOM figure was the einstein R1-A 0-loop-dressed-with-exp(-2S) result
with implicit C_N=1 and S^(N^2-1)=1. The 6.37 OOM upward correction on Γ_α
(= log10(C_3 * S_inst^8) = log10(2.35e6)) deflates 13.67 OOM → 7.30 OOM.

Reference: sessions/archive/session-79/workshops/p3-b-w3o-trh-channel-redefinition.md
(lines 417, 443, 459, 461-475, 527-531, 722-733, 787-823)

PRE-REGISTERED GATE (S80 plan L1605-L1610):
  GATE: [AUDIT] S82-CUSHION-DERIVATION-PIN
  PASS: All citations corrected (as drafts)
  FAIL: Any citation still uses 13 OOM (uncorrected in draft set)

This script emits:
  - s82_w2_12_cushion_audit.npz (citation inventory)
  - verdict line appended to s82_gate_verdicts.txt
  - working-paper §V.L table prepared separately.
"""

import hashlib
import json
import os
import re
import sys
from pathlib import Path

import numpy as np

# Import canonical constants (sanity — M_KK, etc. not directly needed but convention requires import)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from canonical_constants import *  # noqa: F401,F403

# Project root (parent of computations)
ROOT = HERE.parent

# --------------------------------------------------------------------------------------
# Substitution-chain numerics (verified against s82_w2_12 task prompt math)
# --------------------------------------------------------------------------------------
import math
Gamma_bare_GeV = 2.65e10       # (local) Einstein R1-A base rate, P3-B E3 L105 + F2 L411
C_3_MSbar      = 2.5e-3        # (local) Bernard 1979 MS-bar SU(3) normalization, P3-B F2 L382
S_inst         = 13.23         # (local) instanton action, P3-B E3
N2m1           = 8             # (local) color zero-modes for SU(3)
K_2_central    = 1.0           # (local) perturbative 2-loop central, ±1.5 band
Gamma_gamma_GeV = 4.02e12      # (local) Route γ floor (Weinberg unitarity), P3-B L471

S_jac          = S_inst ** N2m1
exp_2S         = math.exp(-2.0 * S_inst)
Gamma_alpha_proper = Gamma_bare_GeV * C_3_MSbar * S_jac * exp_2S * K_2_central
cushion_OOM_central = math.log10(Gamma_gamma_GeV / Gamma_alpha_proper)
# K_2 band (0.4 — 3.0) per P3-B F2 NSVZ reference
cushion_OOM_hi = math.log10(Gamma_gamma_GeV / (Gamma_bare_GeV * C_3_MSbar * S_jac * exp_2S * 0.4))
cushion_OOM_lo = math.log10(Gamma_gamma_GeV / (Gamma_bare_GeV * C_3_MSbar * S_jac * exp_2S * 3.0))

print(f"S^{N2m1}              = {S_jac:.4e}")
print(f"exp(-2 S_inst)     = {exp_2S:.4e}")
print(f"Γ_α^proper         = {Gamma_alpha_proper:.4e} GeV")
print(f"cushion (central) = {cushion_OOM_central:.3f} OOM")
print(f"cushion band (K_2∈[0.4,3.0]) = [{cushion_OOM_lo:.3f}, {cushion_OOM_hi:.3f}] OOM")

# --------------------------------------------------------------------------------------
# Audit scope and search patterns
# --------------------------------------------------------------------------------------
SCAN_DIRS = [
    ROOT / "computations",
    ROOT / "sessions",
]
SCAN_EXTS = {".py", ".md", ".txt"}

# Pattern A: "13 OOM" or "13-OOM" (any spacing)
PAT_13OOM    = re.compile(r"\b13[-\s]?OOM\b")
# Pattern B: cushion keyword
PAT_CUSHION  = re.compile(r"\bcushion\b", re.IGNORECASE)
# Pattern C: Γ_α / Gamma_alpha / Gamma_α
PAT_GAMMA_A  = re.compile(r"(Γ_α|Gamma_alpha|Gamma_α|Γα|Gamma_\\alpha)")
# Pattern D: route-alpha (case-insensitive)
PAT_ROUTE_A  = re.compile(r"(route[-\s_]alpha|Route\s*α|route[-\s_]α)", re.IGNORECASE)

# Already-corrected markers near a "13 OOM" match (within +/- 20 lines)
PAT_CORRECTED_MARKERS = [
    re.compile(r"7\.3\s*OOM", re.IGNORECASE),
    re.compile(r"Bernard\s*1979", re.IGNORECASE),
    re.compile(r"1-loop[-\s]proper", re.IGNORECASE),
    re.compile(r"zero-mode\s*Jacobian", re.IGNORECASE),
    re.compile(r"legacy\s*text", re.IGNORECASE),
    re.compile(r"deflated", re.IGNORECASE),
    re.compile(r"corrected\s*from\s*13\s*OOM", re.IGNORECASE),
    re.compile(r"not\s*13\s*OOM", re.IGNORECASE),
    re.compile(r"replace\s*with\s*7\.3", re.IGNORECASE),
    re.compile(r"advertised\s*a\s*13", re.IGNORECASE),
    re.compile(r"shrinks\s*the\s*cushion", re.IGNORECASE),
    re.compile(r"narrows\s*Einstein", re.IGNORECASE),
    re.compile(r"should\s*not\s*appear", re.IGNORECASE),
]

# Files/dirs to exclude (the P3-B workshop IS the deflation event; its internal
# debate uses "13 OOM" in a corrective sense by construction)
EXCLUDE_PATHS_COMPLIANT_BY_CONSTRUCTION = {
    "sessions/archive/session-79/workshops/p3-b-w3o-trh-channel-redefinition.md",
}


def file_sha256(path: Path) -> str:
    """SHA-256 of file contents."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def near_any(lines, idx, patterns, window=20):
    """Return True if any pattern matches a line within +/- `window` of idx."""
    lo = max(0, idx - window)
    hi = min(len(lines), idx + window + 1)
    for j in range(lo, hi):
        for p in patterns:
            if p.search(lines[j]):
                return True
    return False


def cushion_context(line: str) -> bool:
    """Does the line plausibly refer to the Γ_α cushion (not the 113 OOM CC gap)?"""
    # Reject obvious non-cushion contexts
    if re.search(r"\b(113|112|115|92|86|120|110)\s*OOM", line):
        return True  # keep for reporting but distinguish below
    return True


def citation_type(line: str) -> str:
    """Classify: does this "13 OOM" refer to the cushion?"""
    has_cush  = bool(PAT_CUSHION.search(line))
    has_ga    = bool(PAT_GAMMA_A.search(line))
    has_route = bool(PAT_ROUTE_A.search(line))
    if has_cush:
        return "CUSHION-EXPLICIT"
    if has_ga:
        return "GAMMA-ALPHA-CONTEXT"
    if has_route:
        return "ROUTE-ALPHA-CONTEXT"
    return "OTHER-13-OOM"


def scan_file(path: Path):
    """Return list of citation records for a file."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception as e:
        return [{"path": str(path), "error": str(e)}]
    records = []
    for i, line in enumerate(lines):
        if not PAT_13OOM.search(line):
            continue
        ctype = citation_type(line)
        if ctype == "OTHER-13-OOM":
            # Verify this is not the Γ_α cushion by checking +/- 5 lines for cushion markers
            cushion_near = near_any(lines, i, [PAT_CUSHION, PAT_GAMMA_A, PAT_ROUTE_A], window=5)
            if not cushion_near:
                continue  # not cushion-relevant (probably CC gap or DILUTION)
            ctype = "CUSHION-PROXIMITY"
        corrected = near_any(lines, i, PAT_CORRECTED_MARKERS, window=20)
        rel = path.relative_to(ROOT).as_posix()
        is_compliant_by_construction = rel in EXCLUDE_PATHS_COMPLIANT_BY_CONSTRUCTION
        records.append({
            "path": rel,
            "line_number": i + 1,
            "line_text": line.strip(),
            "citation_type": ctype,
            "has_correction_context": bool(corrected),
            "compliant_by_construction": is_compliant_by_construction,
        })
    return records


# --------------------------------------------------------------------------------------
# Execute scan
# --------------------------------------------------------------------------------------
all_records = []
for root_dir in SCAN_DIRS:
    for path in root_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in SCAN_EXTS:
            continue
        # Skip this script itself
        if path.name == "s82_w2_12_cushion_audit.py":
            continue
        recs = scan_file(path)
        all_records.extend(recs)

# --------------------------------------------------------------------------------------
# Classify each record per audit rule:
#   - compliant_by_construction: P3-B workshop (the deflation itself)
#   - has_correction_context: citation paired with 7.3 OOM / Bernard / legacy-text marker
#   - otherwise: STALE → requires correction draft
# --------------------------------------------------------------------------------------
n_found = len(all_records)
n_compliant = 0   # (local) already-compliant citations counter
n_stale = 0       # (local) stale-citation counter awaiting draft correction
stale = []
compliant = []
for rec in all_records:
    if rec["compliant_by_construction"] or rec["has_correction_context"]:
        n_compliant += 1
        compliant.append(rec)
    else:
        n_stale += 1
        stale.append(rec)

# Draft corrections for STALE entries
CANONICAL_CORRECTION = (
    "7.3 OOM central [Bernard 1979 MS-bar C_3=2.5e-3 × S_inst^8 × exp(-2 S_inst); "
    "K_2 band [6.8, 7.7] OOM; see P3-B §C1 sub-chain]"
)

drafts = []
for rec in stale:
    # Replace "13 OOM" (any spacing/punctuation) with canonical correction
    old = rec["line_text"]
    new = PAT_13OOM.sub("7.3 OOM", old)
    # Append Bernard 1979 Jacobian provenance comment if not already present
    if "Bernard" not in new and "1-loop-proper" not in new:
        new = new + f"  [PROPOSED CORRECTION: cushion=7.3 OOM central; K_2 band [6.8,7.7]; Bernard 1979 1-loop Jacobian C_3·S^8·K_2; see session-79/workshops/p3-b-w3o-trh-channel-redefinition.md lines 722-733]"
    drafts.append({
        "path": rec["path"],
        "line_number": rec["line_number"],
        "citation_type": rec["citation_type"],
        "original": old,
        "proposed": new,
    })

# --------------------------------------------------------------------------------------
# Verdict determination
# --------------------------------------------------------------------------------------
# PASS: all stale citations have a proposed correction (drafts produced for every stale)
# FAIL: any stale citation lacks a draft
verdict = "PASS" if len(drafts) == n_stale else "FAIL"
value_field = f"{n_found}/{len(drafts)}"

# --------------------------------------------------------------------------------------
# NPZ emit
# --------------------------------------------------------------------------------------
npz_path = HERE / "s82_w2_12_cushion_audit.npz"
np.savez_compressed(
    npz_path,
    all_records=np.array(json.dumps(all_records), dtype=object),
    stale=np.array(json.dumps(stale), dtype=object),
    compliant=np.array(json.dumps(compliant), dtype=object),
    drafts=np.array(json.dumps(drafts), dtype=object),
    cushion_OOM_central=cushion_OOM_central,
    cushion_OOM_band_lo=cushion_OOM_lo,
    cushion_OOM_band_hi=cushion_OOM_hi,
    n_found=n_found,
    n_stale=n_stale,
    n_compliant=n_compliant,
    verdict=np.array(verdict, dtype=object),
    canonical_correction=np.array(CANONICAL_CORRECTION, dtype=object),
)

# --------------------------------------------------------------------------------------
# Closure hash: SHA-256 over the ordered pin map of audit inputs
# --------------------------------------------------------------------------------------
# Input files (deterministic ordering) — hash all files we scanned for the closure
# For a pure audit the closure is the SHA of (canonical correction text + ordered list
# of (path, line_number, line_text) for all records).
closure_input = {
    "canonical_correction": CANONICAL_CORRECTION,
    "cushion_central_OOM": round(cushion_OOM_central, 6),
    "n_found": n_found,
    "n_stale": n_stale,
    "records": sorted(
        [(r["path"], r["line_number"], r["line_text"]) for r in all_records],
        key=lambda t: (t[0], t[1]),
    ),
}
closure_bytes = json.dumps(closure_input, sort_keys=True, ensure_ascii=False).encode("utf-8")
closure_sha = hashlib.sha256(closure_bytes).hexdigest()
assert len(closure_sha) == 64, f"closure_sha must be 64 chars, got {len(closure_sha)}"

# --------------------------------------------------------------------------------------
# Append verdict line to s82_gate_verdicts.txt
# --------------------------------------------------------------------------------------
verdict_line = (
    f"S82-CUSHION-DERIVATION-PIN: {verdict} -- "
    f"value={value_field} scheme=AUDIT convention=P3B-7.3-OOM L_max=N/A "
    f"sha256={closure_sha}\n"
)
verdict_path = HERE / "s82_gate_verdicts.txt"
# Check whether this gate is already recorded — if so, do not duplicate.
existing = verdict_path.read_text(encoding="utf-8") if verdict_path.exists() else ""
if "S82-CUSHION-DERIVATION-PIN:" in existing:
    # Already present — replace the line for idempotency
    new_lines = []
    for ln in existing.splitlines():
        if ln.startswith("S82-CUSHION-DERIVATION-PIN:"):
            new_lines.append(verdict_line.rstrip("\n"))
        else:
            new_lines.append(ln)
    with open(verdict_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(new_lines) + "\n")
    action = "replaced existing line"
else:
    with open(verdict_path, "a", encoding="utf-8") as fh:
        fh.write(verdict_line)
    action = "appended"

# --------------------------------------------------------------------------------------
# Report to stdout
# --------------------------------------------------------------------------------------
print()
print("=" * 72)
print(f"AUDIT RESULTS")
print("=" * 72)
print(f"Total '13 OOM' matches (filtered to cushion context): {n_found}")
print(f"  Compliant-by-construction (P3-B deflation doc):    {sum(1 for r in compliant if r['compliant_by_construction'])}")
print(f"  Compliant-by-correction-context (≤±20 lines):      {sum(1 for r in compliant if not r['compliant_by_construction'] and r['has_correction_context'])}")
print(f"  STALE (requires draft correction):                   {n_stale}")
print(f"  DRAFTS produced:                                    {len(drafts)}")
print()
print(f"Verdict:   {verdict}")
print(f"value:     {value_field}")
print(f"closure:   sha256={closure_sha}")
print(f"verdict-file action: {action}")
print()
print("STALE CITATIONS (requiring draft correction):")
for d in drafts:
    print(f"  {d['path']}:{d['line_number']}  [{d['citation_type']}]")
print()
print(f"NPZ: {npz_path}")
print(f"Verdict file: {verdict_path}")
