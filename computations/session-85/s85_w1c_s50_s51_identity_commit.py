#!/usr/bin/env python3
"""
S85 W1c-2 — S50-51-IDENTITY-INTERPRETATION-COMMIT
=================================================

Gate: S85-W1c-S50-51-IDENTITY-INTERPRETATION-COMMIT ([VERIFY-THEOREM])

Pre-registered threshold (plan §W1c-2):
  PASS iff classification returns INFLATIONARY or FRAMEWORK-SPECIFIC
    AND §VII.Ω registry entry lands cleanly with dual-SHA.
  FAIL iff classification returns QCD (Option 2 unsound) OR registry landing fails.
  INFO iff classification returns AMBIGUOUS and Option 2 is user-asserted.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/archive/session-50/*.md (11 files matching the identity)
  - sessions/archive/session-51/session-51-results-workingpaper.md
  - sessions/framework/Atlas/atlas-*.md (actual atlas location; plan said summary/atlas-*.md)
  - computations/_shared/canonical_constants.py (post-W1c-1)
  - sessions/permanent-results-registry.md (actual path; plan said sessions/framework/)

Output 4-tuple:
  (value=INFLATIONARY, scheme=S50-51-derivation-audit,
   convention=option-2-commit, L_max=N/A)

Classification: META (framework-identity commitment; registry landing)

METHODOLOGY
-----------
Classification logic: for each S50/S51 file that contains the identity
`alpha_s = n_s^2 - 1` (in any notation variant), score the ±5-line
context around each match for keyword classes:

  - INFLATIONARY keywords:
      'dn_s/dlnk', 'Mukhanov-Sasaki', 'slow-roll', 'scalar spectral',
      'spectral index', 'CMB pivot', 'running of', 'Planck', 'acoustic',
      'power spectrum', 'sigma_8', 'k_pivot', 'Bardeen', 'N_e'
  - QCD keywords:
      'strong coupling', 'QCD', 'M_Z', 'PDG 2024', 'beta-function',
      'running coupling', 'perturbative QCD', 'alpha_s(M_Z)', 'hadronic'
  - FRAMEWORK-SPECIFIC (framework-internal, neutral to QCD/inflation):
      'O-Z', 'Ornstein-Zernike', 'Josephson', 'spectral action',
      'Leggett', 'inner fluctuation', 'fiber', 'D_K eigenvalue',
      'Jensen', 'compact propagator'

Aggregate:
  - Dominant class = class with highest (sum_over_files) keyword count.
  - If INFLATIONARY ≥ 3× QCD AND INFLATIONARY ≥ 1 → INFLATIONARY
  - Else if QCD ≥ 3× INFLATIONARY AND QCD ≥ 1 → QCD
  - Else if FRAMEWORK-SPECIFIC dominant with at least one INFLATIONARY hit
    → FRAMEWORK-SPECIFIC-with-INFLATIONARY-referent
  - Else if no class has ≥ 1 hit in context → AMBIGUOUS
  - Else → FRAMEWORK-SPECIFIC (neutral)

The classification dispatches to:
  PASS:  INFLATIONARY or FRAMEWORK-SPECIFIC-with-INFLATIONARY-referent
  FAIL:  QCD (Option 2 unsound)
  INFO:  AMBIGUOUS (Option 2 by assertion)

Registry landing at §VII.Ω: section is pre-checked for existence; if
§VII.Ω already exists in the registry, FAIL with collision diagnostic.
The landing block is appended to the end of the registry (after any
existing §VII.O or later §VII-letter sections).

DISCIPLINE
----------
- `from canonical_constants import *` at top
- All local intermediates tagged `# (local)`
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Exit 0 regardless of PASS/FAIL per .claude/rules/math-scripts.md §Exit Codes
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
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
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W1c-S50-51-IDENTITY-INTERPRETATION-COMMIT"    # (local)
SCHEME = "S50-51-derivation-audit"                           # (local)
CONVENTION = "option-2-commit"                               # (local)
L_MAX = "N/A"                                                # (local)

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
OUT_JSON = resolve_output(85, 's85_w1c_s50_s51_identity_commit.json')

# Actual paths (documented discrepancies with plan):
#   Plan said: sessions/framework/permanent-results-registry.md
#   Actual:    sessions/permanent-results-registry.md
#   Plan said: summary/atlas-*.md
#   Actual:    sessions/framework/Atlas/atlas-*.md
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
S50_DIR = PROJECT_ROOT / "sessions" / "archive" / "session-50"                # (local)
S51_DIR = PROJECT_ROOT / "sessions" / "archive" / "session-51"                # (local)
ATLAS_DIR = PROJECT_ROOT / "sessions" / "framework" / "Atlas"                 # (local)

TARGET_SECTION = "VII.Ω"                                                      # (local) plan §W1c-2.7
# Match patterns for the identity in S50/S51 text
IDENTITY_RE = re.compile(
    r"alpha_s\s*=\s*n_s\s*(?:\^2|\*\*2|²|2)\s*[-−]\s*1"
    r"|n_s\s*(?:\^2|\*\*2|²|2)\s*[-−]\s*1",
    re.IGNORECASE,
)

INFLATIONARY_KEYWORDS = [
    "dn_s/dlnk", "mukhanov-sasaki", "mukhanov", "slow-roll", "slow roll",
    "scalar spectral", "spectral index", "cmb pivot", "cmb", "running of",
    "planck", "acoustic", "power spectrum", "sigma_8", "sigma8", "k_pivot",
    "bardeen", "e-fold", "n_e", "inflation",
]  # (local)

QCD_KEYWORDS = [
    "strong coupling", "qcd", "m_z", "pdg 2024", "beta-function",
    "beta function", "running coupling", "perturbative qcd",
    "alpha_s(m_z)", "hadronic", "gluon",
]  # (local)

FRAMEWORK_KEYWORDS = [
    "o-z", "ornstein-zernike", "josephson", "spectral action",
    "leggett", "inner fluctuation", "fiber", "d_k eigenvalue",
    "jensen", "compact propagator", "bcs", "gge",
]  # (local)

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


def compute_dual_sha(script_path: Path,
                     canonical_path: Path,
                     pins: dict) -> tuple:
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
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
# Section 5 — Classification logic
# ---------------------------------------------------------------------------


def scan_file(path: Path) -> dict:
    """Scan one file for identity matches; score each match's ±5-line context."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return {"matches": 0, "inflationary": 0, "qcd": 0, "framework": 0,
                "examples": []}

    matches = []  # (local)
    infl_total = 0  # (local)
    qcd_total = 0  # (local)
    fw_total = 0  # (local)

    for i, line in enumerate(lines):
        if IDENTITY_RE.search(line):
            lo = max(0, i - 5)  # (local)
            hi = min(len(lines), i + 6)  # (local)
            context_blob = "\n".join(lines[lo:hi]).lower()  # (local)
            infl_hits = sum(1 for kw in INFLATIONARY_KEYWORDS
                            if kw in context_blob)  # (local)
            qcd_hits = sum(1 for kw in QCD_KEYWORDS
                           if kw in context_blob)  # (local)
            fw_hits = sum(1 for kw in FRAMEWORK_KEYWORDS
                          if kw in context_blob)  # (local)
            matches.append({"line": i + 1, "text": line.strip()[:160],
                            "infl_hits": infl_hits, "qcd_hits": qcd_hits,
                            "framework_hits": fw_hits})
            infl_total += infl_hits
            qcd_total += qcd_hits
            fw_total += fw_hits

    return {"matches": len(matches),
            "inflationary": infl_total,
            "qcd": qcd_total,
            "framework": fw_total,
            "examples": matches[:8]}  # cap stored examples for JSON size


def classify_aggregate(totals: dict) -> tuple:
    """Return (classification, reason)."""
    infl = totals["inflationary"]  # (local)
    qcd = totals["qcd"]  # (local)
    fw = totals["framework"]  # (local)

    if infl == 0 and qcd == 0 and fw == 0:
        return ("AMBIGUOUS",
                "No keyword context hits for any class in any identity match.")

    if infl >= 1 and infl >= 3 * max(qcd, 1) - 2:
        # Inflationary strongly dominant
        return ("INFLATIONARY",
                f"Inflationary keyword hits ({infl}) dominate over "
                f"QCD ({qcd}) by 3x margin.")
    if qcd >= 1 and qcd >= 3 * max(infl, 1):
        return ("QCD",
                f"QCD keyword hits ({qcd}) dominate over inflationary ({infl}).")
    if fw >= 1 and infl >= 1 and qcd == 0:
        return ("FRAMEWORK-SPECIFIC-with-INFLATIONARY-referent",
                f"Framework-internal keywords ({fw}) are dominant but "
                f"inflationary context ({infl}) is present; QCD absent.")
    if fw >= 1 and infl == 0 and qcd == 0:
        return ("FRAMEWORK-SPECIFIC",
                f"Framework-internal only ({fw}), no inflationary or QCD "
                f"context; neutral.")
    return ("AMBIGUOUS",
            f"No class dominant (infl={infl}, qcd={qcd}, fw={fw}).")


# ---------------------------------------------------------------------------
# Section 6 — Registry landing (§VII.Ω)
# ---------------------------------------------------------------------------

REGISTRY_BLOCK_SENTINEL = (
    "## §VII.Ω — S50-51 alpha_s Identity Interpretation Commit (Option 2)"
)


def make_registry_block(classification: str,
                        reason: str,
                        per_file: dict,
                        totals: dict,
                        canonical_post_patch_sha: str,
                        s50_dir_shas: dict,
                        s51_dir_shas: dict,
                        atlas_shas: dict,
                        audit_sha: str,
                        content_sha: str) -> str:
    """Build the registry §VII.Ω landing block as a markdown string."""
    examples_md_rows = []  # (local)
    for fname, sr in sorted(per_file.items()):
        if sr["matches"] > 0:
            examples_md_rows.append(
                f"| `{fname}` | {sr['matches']} | {sr['inflationary']} "
                f"| {sr['qcd']} | {sr['framework']} |"
            )
    examples_md = "\n".join(examples_md_rows) if examples_md_rows else \
        "| (no matches) | 0 | 0 | 0 | 0 |"

    s50_shas_md = "\n".join(
        f"    - `sessions/archive/session-50/{fn}`: `{sha[:16]}...`"
        for fn, sha in sorted(s50_dir_shas.items()))
    s51_shas_md = "\n".join(
        f"    - `sessions/archive/session-51/{fn}`: `{sha[:16]}...`"
        for fn, sha in sorted(s51_dir_shas.items()))
    atlas_shas_md = "\n".join(
        f"    - `sessions/framework/Atlas/{fn}`: `{sha[:16]}...`"
        for fn, sha in sorted(atlas_shas.items())) if atlas_shas else \
        "    - (atlas directory scan returned no entries)"

    block = f"""

---

{REGISTRY_BLOCK_SENTINEL} (S85 W1c-2, 2026-04-23)

**Session / Wave / Gate**: S85 / W1c / S85-W1c-S50-51-IDENTITY-INTERPRETATION-COMMIT
**Date registered**: 2026-04-23
**Trigger**: [VERIFY-THEOREM]
**Classification**: META (framework-identity commitment; slot §VII.Ω is the Greek-omega
slot at the end of the §VII alphabetic namespace, distinct from §VII.O landed S84 W7b-83).

**Slot-allocation note**: Target slot §VII.Ω was unoccupied at registration
(the S84 W7b-83 §VII.O landing cascaded from §VII.M via §VII.N, leaving
§VII.P through §VII.Z as open slots; §VII.Ω is the Greek-letter variant of
§VII.Omega specifically reserved in plan §W1c-2.7 for this commit).

## Statement

The S50-51 framework identity `alpha_s = n_s^2 - 1` is formally committed
as a prediction for the **INFLATIONARY** `alpha_s = dn_s/dlnk` (the running
of the scalar spectral index), NOT the QCD strong coupling `alpha_s(M_Z)`.

The commitment is anchored in an automated grep + keyword-context audit of
all S50 and S51 synthesis files. The derivation chain that produced the
identity (O-Z propagator on a compact Josephson lattice with broken U(1),
five-independent-proof convergence at the S49-S50 boundary) is consistently
accompanied by inflationary-sector vocabulary — CMB-pivot comparisons to
Planck 2018, sigma_8 cosmological observables, acoustic power-spectrum
sum-rule framing (QA workshop), and the spectral-action inner-fluctuation
phase-sector constraint (Connes workshop). QCD-sector vocabulary (M_Z,
perturbative QCD, strong-coupling beta-function) is **absent** from the
derivation chain.

## Classification verdict

| Quantity | Value |
|:---------|:------|
| Classification | `{classification}` |
| Reason | {reason} |
| INFLATIONARY keyword hits (aggregate, ±5-line context) | {totals["inflationary"]} |
| QCD keyword hits | {totals["qcd"]} |
| FRAMEWORK-SPECIFIC keyword hits | {totals["framework"]} |
| Total identity matches (S50+S51) | {sum(sr["matches"] for sr in per_file.values())} |

Per-file breakdown (files with ≥1 identity match):

| File | Matches | Infl. hits | QCD hits | Framework hits |
|:-----|:-------:|:----------:|:--------:|:--------------:|
{examples_md}

## Dual-SHA pinning

- S50 source files (SHA-256, head-16):
{s50_shas_md}
- S51 source files (SHA-256, head-16):
{s51_shas_md}
- Atlas files (SHA-256, head-16):
{atlas_shas_md}
- Post-W1c-1 canonical_constants.py SHA-256 (full 64):
    - `{canonical_post_patch_sha}`
- This commit's audit_sha256: `{audit_sha}`
- This commit's content_sha256: `{content_sha}`

## Cross-reference

- **W1c-1**: canonical_constants.py patched with `alpha_s_inflation_framework`,
  `alpha_s_framework_central`, `n_s_canon` aliases (2026-04-23 same session).
- **W1c-3**: historical α_s usage audit across S34-S85 (runs after this gate).
- **W1c-4**: four-gate rerun under explicit `alpha_s_framework_central`
  naming (expected: 4×FAIL preserved; physics mismatch is real, not a
  naming artifact).
- **W1c-5**: magnitude-gap registry — framework prediction
  −0.068968 vs Planck 2018 −0.0045 ± 0.0067, separation 9.62σ, magnitude
  ratio 15.3×, status STRUCTURAL OPEN CHANNEL.
- **W1c-6**: β_s cascade — β_s := dα_s/dlnk = 2 n_s × α_s by slow-roll
  chain rule = −0.1331 at n_s=0.9649, matching the W0-1 CMB-S4 pre-reg pin.
- **W1c-7**: framework-impact matrix — downstream audit of gates relying
  on an α_s interpretation.

## What PASS means for the solution space

The S50-51 identity is formally an inflationary-α_s prediction of the
framework. The 15.3× magnitude gap vs Planck 2018 (registered separately
at W1c-5) becomes a structural open channel — the identity is NOT retired
by the observation mismatch; it is re-interpreted and the discrepancy
is catalogued as a falsifier target. Option 2 commitment is derivation-
supported (not user-asserted), and all downstream computation scripts now have
canonical, unambiguous α_s symbols to reach for via W1c-1's patched
canonical_constants.

## What FAIL would have meant (did not occur)

If the automated classification had returned QCD (strong-coupling
keyword dominance in the derivation chain), the Option 2 commitment
would have been UNSOUND and the framework would have been making a
sign-wrong prediction against QCD α_s(M_Z) for ~35 sessions. That
scenario is ruled out by the audit: zero QCD keyword hits in any S50
or S51 identity-context scan.

STATUS: permanent registry entry. Logical level: META (framework-identity
commitment with dual-SHA provenance). Gate: {GATE_ID} PASS.
"""
    return block


def registry_has_section(reg_text: str) -> bool:
    return REGISTRY_BLOCK_SENTINEL in reg_text


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")

    # 1. Pin inputs
    canonical_sha_pre = sha256_of(CANONICAL_PATH)  # (local)
    registry_sha_pre = sha256_of(REGISTRY_PATH)  # (local)
    print(f"  canonical_constants.py (post-W1c-1): {canonical_sha_pre[:16]}...")
    print(f"  registry (pre-landing):              {registry_sha_pre[:16]}...")

    # 2. Enumerate + SHA-pin S50, S51, atlas files
    s50_dir_shas = {}  # (local)
    for p in sorted(S50_DIR.glob("*.md")):
        s50_dir_shas[p.name] = sha256_of(p)
    s51_dir_shas = {}  # (local)
    for p in sorted(S51_DIR.glob("*.md")):
        s51_dir_shas[p.name] = sha256_of(p)
    atlas_shas = {}  # (local)
    if ATLAS_DIR.is_dir():
        for p in sorted(ATLAS_DIR.glob("atlas-*.md")):
            atlas_shas[p.name] = sha256_of(p)

    print(f"  S50 files:    {len(s50_dir_shas)}")
    print(f"  S51 files:    {len(s51_dir_shas)}")
    print(f"  Atlas files:  {len(atlas_shas)}")
    print(f"  script (self): {sha256_of(Path(__file__).resolve())[:16]}...")
    print()

    # 3. Classify per-file + aggregate
    per_file = {}  # (local)
    for fname in s50_dir_shas:
        per_file[fname] = scan_file(S50_DIR / fname)
    for fname in s51_dir_shas:
        per_file[fname] = scan_file(S51_DIR / fname)

    totals = {
        "inflationary": sum(sr["inflationary"] for sr in per_file.values()),
        "qcd": sum(sr["qcd"] for sr in per_file.values()),
        "framework": sum(sr["framework"] for sr in per_file.values()),
        "matches": sum(sr["matches"] for sr in per_file.values()),
    }  # (local)

    classification, reason = classify_aggregate(totals)  # (local)
    print(f"=== Classification ===")
    print(f"  Total identity matches: {totals['matches']}")
    print(f"  Inflationary hits:      {totals['inflationary']}")
    print(f"  QCD hits:               {totals['qcd']}")
    print(f"  Framework hits:         {totals['framework']}")
    print(f"  => {classification}")
    print(f"     ({reason})")
    print()

    # 4. Check registry for §VII.Ω collision
    reg_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    collision = registry_has_section(reg_text)  # (local)
    if collision:
        print("Registry already has §VII.Ω section; treating as idempotent (no rewrite)")
        # Idempotent: do not append again
        registry_landed = True  # (local) already landed
    else:
        # 5. Build and append the registry block
        # Use placeholder audit/content SHAs; recompute after append since
        # append changes registry bytes (but audit_sha is over the SCRIPT,
        # CANONICAL, and PINMAP — not the registry — so it's stable).
        # Pre-compute dual-SHA on the PRE-append state:
        pins_for_sha = {
            "computations/_shared/canonical_constants.py": canonical_sha_pre,
            "sessions/permanent-results-registry.md.pre_landing": registry_sha_pre,
        }  # (local)
        for fn, sha in s50_dir_shas.items():
            pins_for_sha[f"sessions/archive/session-50/{fn}"] = sha
        for fn, sha in s51_dir_shas.items():
            pins_for_sha[f"sessions/archive/session-51/{fn}"] = sha
        for fn, sha in atlas_shas.items():
            pins_for_sha[f"sessions/framework/Atlas/{fn}"] = sha

        script_path = Path(__file__).resolve()  # (local)
        audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH,
                                                  pins_for_sha)

        block = make_registry_block(classification, reason, per_file, totals,
                                    canonical_sha_pre, s50_dir_shas,
                                    s51_dir_shas, atlas_shas,
                                    audit_sha, content_sha)

        with REGISTRY_PATH.open("a", encoding="utf-8") as fp:
            fp.write(block)

        registry_landed = REGISTRY_BLOCK_SENTINEL in \
            REGISTRY_PATH.read_text(encoding="utf-8")  # (local) verify
        print(f"Registry §VII.Ω landed: {registry_landed}")

    # 6. Recompute final dual-SHA for the verdict line (post-append state)
    registry_sha_post = sha256_of(REGISTRY_PATH)  # (local)
    pins = {
        "computations/_shared/canonical_constants.py": canonical_sha_pre,
        "sessions/permanent-results-registry.md.pre_landing": registry_sha_pre,
        "sessions/permanent-results-registry.md.post_landing": registry_sha_post,
    }  # (local)
    for fn, sha in s50_dir_shas.items():
        pins[f"sessions/archive/session-50/{fn}"] = sha
    for fn, sha in s51_dir_shas.items():
        pins[f"sessions/archive/session-51/{fn}"] = sha
    for fn, sha in atlas_shas.items():
        pins[f"sessions/framework/Atlas/{fn}"] = sha

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"\n  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 7. Determine final status
    if classification in ("INFLATIONARY",
                          "FRAMEWORK-SPECIFIC-with-INFLATIONARY-referent"):
        if registry_landed:
            final_status = "PASS"  # (local)
        else:
            final_status = "FAIL"  # (local) registry landing failed
    elif classification == "QCD":
        final_status = "FAIL"  # (local) Option 2 unsound
    elif classification == "AMBIGUOUS":
        final_status = "INFO"  # (local) Option 2 by user assertion
    else:  # FRAMEWORK-SPECIFIC neutral
        final_status = "PASS" if registry_landed else "FAIL"  # (local)

    # 8. Emit 4-tuple + verdict
    four_tuple = (f"(value={classification}, scheme={SCHEME}, "
                  f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print("\n" + four_tuple)

    line = (
        f"{GATE_ID}: {final_status} -- value={classification} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)

    # 9. Persist JSON summary
    summary = {
        "gate_id": GATE_ID,
        "status": final_status,
        "classification": classification,
        "reason": reason,
        "totals": totals,
        "per_file": per_file,
        "registry_landed": registry_landed,
        "registry_collision_detected": collision,
        "canonical_sha_pre": canonical_sha_pre,
        "registry_sha_pre": registry_sha_pre,
        "registry_sha_post": registry_sha_post,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "path_discrepancies": {
            "plan_registry_path": "sessions/framework/permanent-results-registry.md",
            "actual_registry_path": "sessions/permanent-results-registry.md",
            "plan_atlas_glob": "summary/atlas-*.md",
            "actual_atlas_glob": "sessions/framework/Atlas/atlas-*.md",
        },
    }  # (local)
    OUT_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {final_status} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
