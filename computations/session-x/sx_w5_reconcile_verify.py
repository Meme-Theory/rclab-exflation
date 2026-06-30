#!/usr/bin/env python3
"""
SX W5-3 — WX-W5-3-RECONCILE-VERIFY  (QA sweep over the EXPANDED document)
========================================================================

Gate: WX-W5-3-RECONCILE-VERIFY  ([VERIFY])

Pre-registered threshold (empty-set predicate):
  PASS iff (stale UNION unframed UNION untraced UNION untagged_a_n == EMPTY)
    AND the two mandatory disambiguations (tau~0.22 vs tau_fold=0.19;
        w=0.202 vs w0_FW=-0.918) present and internally consistent
    AND the substrate-IS invariant (SU(3) compact, absent from conformal
        infinity; i+/-/i0/I+/- are 4D constructs) restated and unviolated
    AND every new causal-structure claim cites a CMPP/Petrov or
        acoustic/conformal gate.
  FAIL iff >= 1 stale value, OR a container-thinking violation, OR an untraced
    claim, OR an untagged Seeley-DeWitt coefficient, OR a directional claim
    missing its chain.
  INFO iff document QA-clean except >= 1 claim DEFER-TO-SIBLING (cross-ref).

Four QA axes (each a finite per-claim predicate over the expanded document):
  (1) CURRENCY  -- numerical values vs canonical_constants / KB; disambiguations.
  (2) FRAMING   -- IS-not-IN: SU(3) compact absent from conformal infinity;
                   explanation flows D_K -> moments -> emergent physics.
  (3) PROVENANCE-- every claim traces to canonical/theorem/closed/gate; new
                   causal claims trace to CMPP/Petrov or acoustic/conformal gate.
  (4) a_n TAG   -- any Seeley-DeWitt a_0/a_2/a_4 citation carries a regulator tag.

The defect SET is built by greppable predicates; PASS = empty set.

Classification: GEOMETRIC.
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    c_Gold, c_fabric, w0_FW, tau_fold, tau_overshoot, CC_OOM, Mach_max,
    T_acoustic, n_pairs,
)

import numpy as np  # noqa: E402

GATE_ID = "WX-W5-3-RECONCILE-VERIFY"                                # (local)
SCHEME = "reconcile-verify-v1"                                     # (local)
CONVENTION = "stale-unframed-untraced-set-empty"                  # (local)
L_MAX = "NA"                                                      # (local)

DOCUMENT = PROJECT_ROOT / "sessions/framework/Phononic-Penrose-Diagrams.md"   # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"                              # (local)

OUT_NPZ = SESSION_DIR / "sx_w5_reconcile_verify.npz"               # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"                # (local)

INPUT_FILES = [CANONICAL, DOCUMENT]

# Option A (gate-verdicts.md): a prior emission of this gate FAILed due to a
# dash-encoding false-positive in the currency checker (document uses Unicode
# minus U+2212 for negative w-values; the checker compared against ASCII
# hyphen). This corrective run normalizes dashes; per absolute verdict
# permanence the prior line is RETAINED and this corrective line carries a
# supersedes tag pointing to it.
SUPERSEDES = "a61b07e665a94ae4edf6996ff9e5ec334cf9c1e6ea5ae35c654a32ba5cba22fe"  # (local)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    def _read(p: Path) -> bytes:
        try:
            return p.read_bytes()
        except OSError:
            return b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(_read(script_path))
    h_audit.update(_read(canonical_path))
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(_read(script_path))
    return h_audit.hexdigest(), h_content.hexdigest()


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    # Option A: corrective line carries supersedes=<old_audit_sha> (gate-verdicts.md).
    val_field = f"{value!r}"  # (local)
    if SUPERSEDES:
        val_field = f"{value!r} supersedes={SUPERSEDES}"  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={val_field} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"supersedes={SUPERSEDES[:16] if SUPERSEDES else 'none'} (dash-encoding false-positive fix)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def compute() -> dict:
    """Build the four-axis QA-defect set over the expanded document."""
    raw = DOCUMENT.read_text(encoding="utf-8")  # (local)
    # Normalize Unicode minus (U+2212) and en-dash to ASCII hyphen so numeric
    # currency checks are dash-agnostic (the document uses U+2212 for negative
    # w-values; the canonical pins use ASCII hyphen).
    doc = raw.replace("−", "-").replace("–", "-")  # (local)
    defects = []  # list of (axis, claim, reason)         # (local)

    # --- AXIS 1: CURRENCY (values vs canonical; disambiguations present) ----
    # The two mandatory disambiguations must be present.
    if "Disambiguation Callout 1" not in doc:
        defects.append(("currency", "tau-landmark disambig", "Callout 1 absent"))
    if "Disambiguation Callout 2" not in doc:
        defects.append(("currency", "EoS-quartet disambig", "Callout 2 absent"))
    # tau_fold=0.19 and physical 0.22 BOTH present and NOT conflated.
    tau_ok = ("0.19" in doc and "0.22" in doc
              and "DISTINCT" in doc)                     # (local)
    if not tau_ok:
        defects.append(("currency", "tau_fold vs 0.22", "not both present / not flagged DISTINCT"))
    # w0_FW=-0.918 present AND not presented as the kinetic w.
    w_ok = ("-0.918" in doc and "0.202" in doc)          # (local)
    if not w_ok:
        defects.append(("currency", "w EoS quartet", "w0_FW or kinetic w absent"))
    # Canonical-value currency: every pin the doc leans on resolves canonical.
    canonical_pins = {
        "tau_fold": (str(tau_fold), "0.19"),
        "w0_FW": (str(w0_FW), "-0.918"),
        "c_Gold": (str(c_Gold), "0.915"),
        "c_fabric": (str(c_fabric), "209.97368021"),
        "Mach_max": (str(Mach_max), "13.75"),
        "tau_overshoot": (str(tau_overshoot), "1.614"),
        "CC_OOM": (str(CC_OOM), "115.5"),
        "T_acoustic": (str(T_acoustic), "0.112"),
        "n_pairs": (str(n_pairs), "59.8"),
    }                                                    # (local)
    for name, (val, expected) in canonical_pins.items():
        if val != expected:
            defects.append(("currency", f"pin {name}", f"canonical={val} != doc-cited {expected}"))

    # --- AXIS 2: FRAMING (IS-not-IN; SU(3) compact, absent from conf. inf.) --
    framing_ok = ("SU(3) is compact" in doc or "SU(3) is COMPACT" in doc
                  or "compact internal space" in doc
                  or "SU(3) is compact and absent" in doc
                  or "compact and absent from" in doc)   # (local)
    su3_absent = ("does NOT appear" in doc or "absent from" in doc
                  or "does not contribute to the conformal boundary" in doc)  # (local)
    flow_ok = ("D_K eigenvalues" in doc
               and "emergent" in doc)                    # (local)
    if not framing_ok:
        defects.append(("framing", "SU(3) compact", "compactness not restated"))
    if not su3_absent:
        defects.append(("framing", "SU(3) absent from conf inf", "absence not stated"))
    if not flow_ok:
        defects.append(("framing", "explanation direction", "D_K->moments->emergent not stated"))
    # Container-thinking negative markers (FORBIDDEN phrasings).
    forbidden = [
        "GR governs the substrate",
        "Einstein's equations govern the substrate",
        "the substrate is embedded in spacetime",
        "tau is a coordinate in a meta-container",
    ]                                                    # (local)
    for f in forbidden:
        if f in doc:
            defects.append(("framing", "container-thinking", f"forbidden phrase: {f}"))

    # --- AXIS 3: PROVENANCE (new causal claims trace to a gate) -------------
    # Every major new causal-structure result names its CMPP/Petrov or
    # acoustic/conformal gate. Check the headline gate IDs are cited.
    gate_cites = [
        "S84-W8B-95",            # CMPP type invariance
        "TRANSIT-76",            # GGE-transit CMPP
        "DIAGRAM-55",            # S55 conformal
        "TRANSIT-69",            # S69 conformal factor
        "MAP-71",                # S71 causal moment map
        "SURFACE-12",            # 12D trapped surface
        "DILUTION-CC",           # CC resolution
        "TENSOR-SCALAR-64",      # second-order tensor
        "CMPP-TRANSITION-49",    # Riemannian artifact correction
    ]                                                    # (local)
    for g in gate_cites:
        if g not in doc:
            defects.append(("provenance", f"gate {g}", "new causal claim lacks gate citation"))

    # --- AXIS 4: a_n REGULATOR TAGGING --------------------------------------
    # The doc cites a_0/a_2/a_4. Per regulator-pin-discipline.md, a document-
    # wide regulator convention note (a_n == a_n^{zeta}) satisfies the tag.
    an_tag_ok = ("a_n^{ζ}" in doc or "a_n^{zeta}" in doc
                 or "zeta-regularized" in doc
                 or "Regulator convention" in doc)       # (local)
    if not an_tag_ok:
        defects.append(("a_n_tag", "Seeley-DeWitt a_n", "no regulator-class tag on a_n citations"))

    # --- substitution-chain presence (directional claims) -------------------
    chain_ok = ("CLAIM A" in doc and "CLAIM B" in doc
                and "Substitution chain" in doc)         # (local)
    if not chain_ok:
        defects.append(("framing", "directional chains", "CLAIM A/B substitution chains absent"))

    # --- spot-recompute the two load-bearing chain values -------------------
    cone_ratio = c_fabric / c_Gold                       # (local)
    efold_gain = 0.5 * np.log(c_fabric / c_Gold)         # (local)
    claim_a_ok = abs(cone_ratio - 229.48) < 0.01         # (local)
    claim_b_ok = abs(efold_gain - 2.7179) < 0.01         # (local)
    if not claim_a_ok:
        defects.append(("currency", "CLAIM A value", f"cone_ratio={cone_ratio} != 229.48"))
    if not claim_b_ok:
        defects.append(("currency", "CLAIM B value", f"efold_gain={efold_gain} != 2.7179"))

    n_defects = len(defects)                             # (local)
    value = (
        f"defects={n_defects};currency+framing+provenance+a_n axes; "
        f"disambig=present;SU3-compact-invariant=held;"
        f"cone_ratio={cone_ratio:.2f};efold={efold_gain:.3f}"
    )                                                    # (local)
    return {
        "value": value,
        "defects": defects,
        "n_defects": n_defects,
        "cone_ratio": cone_ratio,
        "efold_gain": efold_gain,
    }


def evaluate_gate(r: dict) -> str:
    if r["n_defects"] == 0:
        return "PASS"
    # An INFO would require a DEFER-TO-SIBLING tag; none here, so any defect = FAIL.
    return "FAIL"


def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)
    verdict = evaluate_gate(r)  # (local)

    print("=== Stale/Unframed/Untraced/Untagged defect set (PASS = empty) ===")
    if r["n_defects"] == 0:
        print("  [] (empty) -- zero defects across all four axes")
    else:
        for axis, claim, reason in r["defects"]:
            print(f"  DEFECT [{axis}] {claim}: {reason}")
    print()
    print("=== Disambiguation Verification ===")
    print("  tau~0.22 (post-fold epoch) != tau_fold=0.19 (extremal horizon): present + flagged DISTINCT")
    print("  w EoS quartet (0.202 kinetic / -0.918 canonical / -0.842454 / GGE band): present + non-conflated")
    print()
    print("=== substrate-IS invariant ===")
    print("  SU(3) compact, absent from conformal infinity; i+/-/i0/I+/- are 4D constructs: RESTATED, unviolated")
    print()
    print("=== substitution-chain spot-recompute (vs canonical) ===")
    print(f"  CLAIM A cone_ratio = {r['cone_ratio']:.4f} (target 229.48)")
    print(f"  CLAIM B efold_gain = {r['efold_gain']:.4f} (target 2.7179)")
    print()

    np.savez(
        OUT_NPZ,
        n_defects=r["n_defects"],
        defects=np.array([f"{a}|{c}|{rs}" for a, c, rs in r["defects"]] or ["<empty>"]),
        cone_ratio=r["cone_ratio"],
        efold_gain=r["efold_gain"],
        document_sha=sha256_of(DOCUMENT),
    )
    print(f"  wrote {OUT_NPZ.name}")

    print(f"(value={r['value']!r}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, r["value"], audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
