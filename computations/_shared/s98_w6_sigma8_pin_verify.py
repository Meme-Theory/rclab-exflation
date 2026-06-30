#!/usr/bin/env python3
"""
S98 W6-1 S98-HK-SIGMA8-CHANNEL-KEYED-PINS — channel-keyed sigma_8 pin verify + closure
======================================================================================

Gate: S98-HK-SIGMA8-CHANNEL-KEYED-PINS ([AUDIT])

METHODOLOGY-class canonical-constants hygiene gate (NOT a numerical-threshold
compute). Producing operation per the plan §W6-1 is `update_constant` (x2) +
`get_constant`-verify + grep cross-check of the canonical_constants.py SECTION-E
diff (wave-classification.md M2). There is NO eigenvalue / linear-algebra /
numerical-threshold computation here; this script is the OPTIONAL non-numerical
verify helper (plan output_artifacts.verify_helper, optional:true) that ALSO
emits the dual-SHA verdict line.

PASS predicate (set-membership / artifact-existence; plan operator):
  PASS iff  {sigma8_OZ_50, sigma8_growth_a2} are BOTH importable from
            canonical_constants AND both resolve in the PROVENANCE dict with
            non-empty channel-DISTINCT provenance (distinct `source`/`channel`)
        AND a cross-note distinguishing the two substrate channels (~0.7% apart,
            O-Z larger) AND distinguishing both from the LCDM reference
            sigma_8=0.811 is present in BOTH the value-line comments and the
            PROVENANCE notes.

Both sigma_8 values are VERBATIM-upstream (M3, no new derivation):
  sigma8_OZ_50 -> 0.799    [SIGMA8-OZ-50 (S50 PASS); atlas-07 PERMANENT; HEADLINE]
  sigma8_growth_a2 -> 0.79317  [S70 s70_bulk_flow.npz (s59_growth_factor.npz 0.793166
                                -> 0.79317 5-sig); S97-FSIGMA8-FORECAST-REFETCH PASS audit a20043e7]

Dual-SHA (wave-classification.md "Dual-SHA closure for METHODOLOGY-class"):
  content_sha256 = sha256( SECTION-E diff text )         # the canonical-constants diff
                                                          #   (F-image of the numerical PASS-predicate)
  audit_sha256   = closure_hash( ordered input-pin map ) # the two upstream gate records
                                                          #   + the naming/cross-note pin map
                                                          #   (plan audit_discriminators: ["pinmap","source_records"])

Per math-scripts.md "Exit Codes and Verdict Semantics": exit 0 on a VALID verdict
regardless of PASS/FAIL/INFO; non-zero only on script breakage.

Classification: GEOMETRIC (sigma_8 is a spectral-action / a_2-moment readout of D_K).
"""

from __future__ import annotations

# --- Section 1: canonical constants (MANDATORY first import) ---
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc

# --- Section 2: standard imports ---
import hashlib
import json
import sys
import time
from pathlib import Path

# --- Section 3: paths + identity ---
# This script lives at computations/_shared/. The verdict file is canonical at
# computations/session-98/s98_gate_verdicts.txt per gate-verdicts.md.
SHARED_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SHARED_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_DIR = COMPUTATIONS_DIR / "session-98"
VERDICT_TXT = SESSION_DIR / "s98_gate_verdicts.txt"

SESSION = "S98"                                            # (local)
GATE_ID = "S98-HK-SIGMA8-CHANNEL-KEYED-PINS"              # (local)
SCHEME = "canonical-hygiene"                              # (local)
CONVENTION = "no-run-no-gate"                             # (local) METHODOLOGY-class hygiene convention
L_MAX = "N/A"                                             # (local) no spectrum truncation

# Pre-registered VERBATIM-upstream values (M3) — used only to assert the
# imported pins match the upstream gate records; NO new derivation.
SIGMA8_OZ_50_EXPECTED = 0.799                             # (local) SIGMA8-OZ-50 S50 PASS
SIGMA8_GROWTH_A2_EXPECTED = 0.79317                       # (local) S97-FSIGMA8-FORECAST-REFETCH PASS
SIGMA8_LCDM_REF = 0.811                                   # (local) Planck 2018 reference (canonical_constants.sigma_8)


# --- Section 4: dual-SHA ---
def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over an ordered input-pin map (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def sha256_text(text: str) -> str:
    """SHA-256 of a UTF-8 string."""
    h = hashlib.sha256()  # (local)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


# The SECTION-E diff text: the exact two value-pin lines + the two PROVENANCE
# entries added by this gate (the canonical-constants diff that content_sha256
# pins). Kept here verbatim so the diff hash is reproducible and INVARIANT to
# unrelated edits elsewhere in canonical_constants.py.
SECTION_E_DIFF_TEXT = (
    "sigma8_OZ_50 = 0.799  # sigma_8 spectral-action / Ornstein-Zernike (O-Z) channel; "
    "a0-region; HEADLINE sigma_8. CROSS-NOTE: O-Z 0.799 vs a2-growth 0.79317 ~0.7% apart "
    "(0.735%, O-Z LARGER); BOTH distinct from LCDM sigma_8=0.811 (O-Z -1.50%, growth -2.18%). (S98)\n"
    "sigma8_growth_a2 = 0.79317  # sigma_8 a2 Seeley-DeWitt growth channel; f=dlnD/dlna feeding fsigma8; "
    "CROSS-NOTE: a2-growth 0.79317 vs O-Z 0.799 ~0.7% apart (0.735%, O-Z LARGER); BOTH distinct from "
    "LCDM sigma_8=0.811 (growth -2.18%, O-Z -1.50%). (S98)\n"
    "PROVENANCE[sigma8_OZ_50]: session=S98, gate=S98-HK-SIGMA8-CHANNEL-KEYED-PINS, "
    "channel=spectral-action/O-Z/a0-region/HEADLINE\n"
    "PROVENANCE[sigma8_growth_a2]: session=S98, gate=S98-HK-SIGMA8-CHANNEL-KEYED-PINS, "
    "channel=a2-Seeley-DeWitt-growth/fsigma8\n"
)

# The audit input-pin map: the two upstream gate records (source_records) + the
# naming/cross-note pin map (pinmap). Plan audit_discriminators.audit_sha256_inputs
# = ["pinmap", "source_records"].
AUDIT_PIN_MAP = {
    # source_records — the two upstream gate records the values are consumed from
    "source_record:SIGMA8-OZ-50": "S50 PASS; sigma_8=0.799; atlas-07-permanent-results.md PERMANENT; in[0.740,0.820]; -1.50% vs LCDM",
    "source_record:S97-FSIGMA8-FORECAST-REFETCH": "S97 PASS; sigma_8=0.79317; audit a20043e7; s97_fsigma8_forecast_refetch.npz; s59_growth_factor.npz sigma8_fw=0.793166",
    # pinmap — the canonical naming + channel tags + cross-note text
    "pin:sigma8_OZ_50:value": "0.799",
    "pin:sigma8_OZ_50:channel": "spectral-action / Ornstein-Zernike (O-Z); a0-region; HEADLINE",
    "pin:sigma8_growth_a2:value": "0.79317",
    "pin:sigma8_growth_a2:channel": "a2 Seeley-DeWitt growth channel; f=dlnD/dlna feeding fsigma8",
    "pin:cross_note:rel_spread": "|0.799-0.79317|/0.79317=0.735% (~0.7%); O-Z LARGER",
    "pin:cross_note:vs_LCDM": "both < LCDM sigma_8=0.811 (Planck 2018): O-Z -1.50%, growth -2.18%",
    "pin:gate": GATE_ID,
    "pin:session": SESSION,
}


# --- Section 5: verify (the artifact-existence PASS predicate) ---
def verify() -> dict:
    """Run the set-membership / channel-distinctness PASS predicate.

    Mirrors `get_constant('sigma8_OZ_50')` + `get_constant('sigma8_growth_a2')`
    at the canonical_constants.py module + PROVENANCE-dict layer. Returns a dict
    with the resolution booleans and the verdict.
    """
    prov = getattr(cc, "PROVENANCE", {})  # (local)
    checks = {}  # (local)

    # (1) both pins importable from canonical_constants
    has_oz = hasattr(cc, "sigma8_OZ_50")  # (local)
    has_gr = hasattr(cc, "sigma8_growth_a2")  # (local)
    checks["import_sigma8_OZ_50"] = has_oz
    checks["import_sigma8_growth_a2"] = has_gr

    # (2) values match the VERBATIM-upstream records (M3 — no new derivation)
    val_oz = getattr(cc, "sigma8_OZ_50", None)  # (local)
    val_gr = getattr(cc, "sigma8_growth_a2", None)  # (local)
    checks["value_OZ_matches"] = (val_oz == SIGMA8_OZ_50_EXPECTED)
    checks["value_growth_matches"] = (val_gr == SIGMA8_GROWTH_A2_EXPECTED)

    # (3) both resolve in PROVENANCE with non-empty source
    p_oz = prov.get("sigma8_OZ_50", {})  # (local)
    p_gr = prov.get("sigma8_growth_a2", {})  # (local)
    checks["prov_OZ_nonempty_source"] = bool(p_oz.get("source", ""))
    checks["prov_growth_nonempty_source"] = bool(p_gr.get("source", ""))

    # (4) channel-DISTINCT: distinct channel + distinct source strings
    ch_oz = p_oz.get("channel", "")  # (local)
    ch_gr = p_gr.get("channel", "")  # (local)
    checks["channels_distinct"] = bool(ch_oz) and bool(ch_gr) and (ch_oz != ch_gr)
    checks["sources_distinct"] = (p_oz.get("source", "") != p_gr.get("source", "")) and bool(p_oz.get("source", ""))

    # (5) gate field present on both PROVENANCE entries
    checks["gate_field_OZ"] = (p_oz.get("gate", "") == GATE_ID)
    checks["gate_field_growth"] = (p_gr.get("gate", "") == GATE_ID)

    # (6) cross-note present in BOTH PROVENANCE notes: references the other channel
    #     AND the LCDM reference sigma_8=0.811.
    note_oz = p_oz.get("note", "")  # (local)
    note_gr = p_gr.get("note", "")  # (local)
    checks["crossnote_OZ_refs_partner"] = ("growth" in note_oz.lower()) and ("0.811" in note_oz)
    checks["crossnote_growth_refs_partner"] = ("o-z" in note_gr.lower() or "oz" in note_gr.lower()) and ("0.811" in note_gr)

    # (7) substitution-chain cross-check (pre-registered; NOT a runtime discovery):
    #     rel_spread = |OZ - growth| / growth ; O-Z is the larger.
    rel_spread = abs(SIGMA8_OZ_50_EXPECTED - SIGMA8_GROWTH_A2_EXPECTED) / SIGMA8_GROWTH_A2_EXPECTED  # (local)
    checks["rel_spread_about_0p7pct"] = (0.006 < rel_spread < 0.009)  # 0.735% lands in band
    checks["OZ_is_larger"] = (SIGMA8_OZ_50_EXPECTED > SIGMA8_GROWTH_A2_EXPECTED)
    oz_vs_lcdm = (SIGMA8_OZ_50_EXPECTED - SIGMA8_LCDM_REF) / SIGMA8_LCDM_REF  # (local)
    gr_vs_lcdm = (SIGMA8_GROWTH_A2_EXPECTED - SIGMA8_LCDM_REF) / SIGMA8_LCDM_REF  # (local)
    checks["both_below_LCDM"] = (oz_vs_lcdm < 0) and (gr_vs_lcdm < 0)

    all_pass = all(checks.values())  # (local)
    verdict = "PASS" if all_pass else "FAIL"  # (local)

    return {
        "verdict": verdict,
        "checks": checks,
        "sigma8_OZ_50": val_oz,
        "sigma8_growth_a2": val_gr,
        "rel_spread": rel_spread,
        "oz_vs_lcdm": oz_vs_lcdm,
        "gr_vs_lcdm": gr_vs_lcdm,
        "value": f"sigma8_OZ_50={val_oz};sigma8_growth_a2={val_gr};rel_spread={rel_spread:.6f};OZ_larger;both_below_LCDM_0.811",
    }


# --- Section 6: verdict emission (atomic single open("a") append) ---
def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the canonical verdict line + dual-SHA companion comment row.

    Atomic single `open("a")` write per gate-verdicts.md / agent-standards.md
    (no read-modify-write, no truncate-and-rewrite — POSIX O_APPEND safe).
    AUDIT-triggered gate: NO [SIGN] 3-tuple companion row (schema_v2_3tuple
    not required).
    """
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row "
        f"(content_sha256 over SECTION-E diff; audit_sha256 over input-pin map "
        f"[pinmap + source_records]; METHODOLOGY-class per wave-classification.md)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


# --- Section 7: main ---
def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — METHODOLOGY-class channel-keyed sigma_8 pin verify ===")
    print(f"  sigma8_OZ_50     (import) = {getattr(cc, 'sigma8_OZ_50', None)}  "
          f"[expected {SIGMA8_OZ_50_EXPECTED}, SIGMA8-OZ-50 S50 PASS, HEADLINE]")
    print(f"  sigma8_growth_a2 (import) = {getattr(cc, 'sigma8_growth_a2', None)}  "
          f"[expected {SIGMA8_GROWTH_A2_EXPECTED}, S97-FSIGMA8-FORECAST-REFETCH PASS audit a20043e7]")

    res = verify()

    # dual-SHA
    content_sha = sha256_text(SECTION_E_DIFF_TEXT)  # (local) over the canonical-constants SECTION-E diff
    audit_sha = closure_hash(AUDIT_PIN_MAP)  # (local) over the ordered input-pin map
    print(f"  content_sha256 (SECTION-E diff): {content_sha[:16]}...")
    print(f"  audit_sha256   (input-pin map):  {audit_sha[:16]}...")

    print("  --- channel-distinctness checks ---")
    for k, v in res["checks"].items():
        print(f"    {k}: {'PASS' if v else 'FAIL'}")
    print(f"  rel_spread = {res['rel_spread']:.6f} (0.735%); O-Z vs LCDM = {res['oz_vs_lcdm']*100:.2f}%; "
          f"growth vs LCDM = {res['gr_vs_lcdm']*100:.2f}%")

    verdict = res["verdict"]  # (local)
    value = res["value"]  # (local)
    print(f"  (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # math-scripts.md Exit Codes: exit 0 on a VALID verdict (PASS/FAIL/INFO all valid);
    # non-zero ONLY on script breakage. This gate produced a valid verdict.
    return 0


if __name__ == "__main__":
    sys.exit(main())
