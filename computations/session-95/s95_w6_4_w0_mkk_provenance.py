#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
W0-MKK-PROVENANCE  (S95 W6-4)
=============================

Gate: W0-MKK-PROVENANCE  [VERIFY]
Classification: NON-PHONONIC (constant-provenance hygiene; PASS predicate is
                provenance-PRESENT on each target constant, NOT a numerical
                comparison against a threshold).
Owner: mack-cosmic-bridge (Cosmic Bridge; observational-cosmology / DM-DE interface).
Plan: sessions/session-plan/session-95-plan-w6.md §W6-4.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE DOES
═══════════════════════════════════════════════════════════════════════════

A constant-PROVENANCE-completeness hygiene gate. The framework constants below
ARE substrate-derived (the substrate IS the spectral triple; these numbers are
spectral moments / vacuum-partition outputs of D_K on Jensen-deformed SU(3)):

  - w0_FW = -0.918       : framework dark-energy w_0 from the Volovik vacuum
                           partition + effacement (Gamma_effacement=0.99970),
                           S58 four-fold structural lock. BINDS Falsifier #1
                           (DESI DR3 / R_842 rectangle, S84-DR3-RESPONSE-PROTOCOL).
  - M_KK  = 7.428660036284456e16 GeV
                         : default alias of M_KK_gravity (spectral-zeta /
                           Newton's-constant gravity route, S42). Alternate
                           Kerner gauge-metric route M_KK_kerner=5.04e17 GeV;
                           OOM_diff_MKK=0.831664779390838 (0.83-decade tension).

Each carried an INLINE provenance comment but NO machine-readable PROVENANCE-dict
entry (the dict `get_constant` / the knowledge MCP reads). Confirmed at this
planning run: get_constant("w0_FW") / get_constant("M_KK") both returned the
value with "No PROVENANCE entry". M_KK_gravity ALREADY carried provenance; the
gap was on the bare M_KK alias.

ADDITIONAL HYGIENE (routed to this wave from W3/W5):
  - (a) Delta_B3 = 0.176 (S38 B3-sector pairing gap) lacked a PROVENANCE entry.
        DISTINCT from the new Delta_B3_s53=0.084152 order-parameter gap added in
        W3-3. ADDRESSED here (third provenance write).
  - (b) f2 ≈ 92 CC-dictionary value has no canonical pin (only f_2_default=2.34
        Gaussian-scheme). NOTED ONLY (conditional — pin iff a consumer exists);
        NO write here (no consumer identified; pinning an unconsumed value would
        be canonical-clutter, not hygiene). Flagged in WP §W6-4 for orchestrator.

THE FIX (already on disk before this script runs, per the FIX-IN-SESSION write):
  PROVENANCE-dict entries for "M_KK", "w0_FW", "Delta_B3" were ADDED to
  computations/_shared/canonical_constants.py (Section F-hygiene block before the
  dict's closing brace). The existing variable ASSIGNMENTS are UNTOUCHED — this is
  provenance-transcription, NOT a re-value. (update_constant REFUSES to touch an
  existing constant by design — "manually edit canonical_constants.py" — which is
  exactly the manual PROVENANCE-dict edit performed; the MCP get_constant reads the
  live dict, so the provenance is visible immediately, and /weave --update syncs
  knowledge.db on the next index rebuild per math-scripts.md §"Sync enforcement".)

This script RE-CONFIRMS the fix: (1) value-invariance (the three values are
bit-unchanged vs their pre-registered values), (2) provenance-PRESENT (each target
key now has a non-empty PROVENANCE-dict entry with session+source). Verdict PASS iff
both hold for ALL target constants.

═══════════════════════════════════════════════════════════════════════════
NO DIRECTIONAL CLAIM  (plan §W6-4 substitution_chain.required: false)
═══════════════════════════════════════════════════════════════════════════
This is a provenance-existence hygiene write. There is NO sign / direction /
threshold claim and NO schema-v2 3-tuple companion row (plan
schema_v2_3tuple_required: false). The only quantitative check is value-INVARIANCE
(values must be bit-unchanged), which is an equality check, not a directional
prediction.

Verdict file: computations/session-95/s95_gate_verdicts.txt
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU-only (dict read + SHA; no linalg, no GPU)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent  # (local) project root
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

# Per computations/_shared/CLAUDE.md ALL scripts MUST import canonical_constants.
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    PROVENANCE,
    M_KK,
    M_KK_gravity,
    M_KK_kerner,
    OOM_diff_MKK,
    w0_FW,
    wa_FW,
    Delta_B3,
    Delta_B3_s53,
    f_2_default,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "W0-MKK-PROVENANCE"  # (local)
SCHEME = "constant-hygiene"  # (local) plan-pinned scheme
CONVENTION = "provenance-transcription-no-revalue"  # (local) plan-pinned convention
L_MAX = "N/A"  # (local) constant-provenance hygiene; no L_max
SCHEMA_VERSION = "S84+"  # (local)

SESSION_DIR = ROOT / "computations" / "session-95"  # (local)
OUT_NPZ = SESSION_DIR / "s95_w6_4_w0_mkk_provenance.npz"  # (local)
OUT_PNG = SESSION_DIR / "s95_w6_4_w0_mkk_provenance.png"  # (local)
OUT_JSON = SESSION_DIR / "s95_w6_4_w0_mkk_provenance.json"  # (local)
VERDICT_FILE = SESSION_DIR / "s95_gate_verdicts.txt"  # (local)

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
SCRIPT_PATH = Path(__file__).resolve()  # (local)

# ---------------------------------------------------------------------------
# Pre-registered target constants + their bit-exact expected values.
# Plan §W6-4: PRIMARY {w0_FW, M_KK}; ADDITIONAL hygiene (a) {Delta_B3}.
# (tolerance: exact — values must be bit-unchanged.)
# ---------------------------------------------------------------------------
PRIMARY_TARGETS = {  # (local) the two plan-PRIMARY constants
    "w0_FW": -0.918,
    "M_KK": 7.428660036284456e16,
}
HYGIENE_TARGETS = {  # (local) the routed-in additional hygiene constant (a)
    "Delta_B3": 0.176,
}
ALL_TARGETS = {**PRIMARY_TARGETS, **HYGIENE_TARGETS}  # (local)

# Item (b): f2 ≈ 92 CC-dictionary value — NOTED ONLY (conditional, no consumer).
F2_CC_DICT_NOTED_VALUE = 92.0  # (local) the un-pinned CC-dictionary f_2 (narrative only; NOT written)


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 76)
    print(f"Gate: {GATE_ID}")
    print("=" * 76)
    print("Input SHA-256 pins (first lines of stdout):")
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        rel = str(p.relative_to(ROOT)).replace("\\", "/") if p.exists() else str(p)
        print(f"  {name:24s} = {sha[:16]}...  ({rel})")
    return pins


def provenance_nonempty(entry: dict | None) -> bool:
    """A PROVENANCE-dict entry is non-empty iff it exists AND carries a session AND a source."""
    return bool(entry) and bool(entry.get("session")) and bool(entry.get("source"))


def compute_dual_sha(pins: dict, facts: dict) -> tuple[str, str]:
    """Dual-SHA per S84+ schema.
    content_sha256 = SHA over the canonical-constants PROVENANCE-dict text for the target keys
      (the artifact whose state-with-content IS the hygiene predicate).
    audit_sha256   = SHA over the input-pin map + the provenance/value facts + per-gate identity
      keys (gate-distinct).
    """
    content_payload = json.dumps(  # (local) the provenance entries for the target keys (sorted)
        {k: PROVENANCE.get(k) for k in sorted(ALL_TARGETS)}, sort_keys=True, default=str
    ).encode("utf-8")
    content = hashlib.sha256(content_payload).hexdigest()  # (local)

    pinmap_json = json.dumps(dict(sorted(pins.items())), sort_keys=True).encode("utf-8")  # (local)
    facts_json = json.dumps(dict(sorted(facts.items())), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    h_audit.update(facts_json)
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}|L_max={L_MAX}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str) -> None:
    """Single canonical dual-SHA verdict line + companion row. Constant-provenance hygiene;
    [VERIFY] — no [SIGN] 3-tuple (provenance-existence + value-invariance, not a sign/direction
    prediction; plan §W6-4 schema_v2_3tuple_required: false). Append-only single open("a") write.
    First emission for this gate-ID this session (no supersedes).
    """
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; NON-PHONONIC constant-provenance hygiene; "
        f"mack-cosmic-bridge; added PROVENANCE-dict entries for M_KK (alias of M_KK_gravity), "
        f"w0_FW (S58 four-fold lock; binds Falsifier #1 DESI DR3), Delta_B3 (S38; item (a)); "
        f"values BIT-UNCHANGED (-0.918, 7.428660036284456e16, 0.176); f2=92 NOTED-ONLY item (b) "
        f"(no consumer, no write); [VERIFY] no [SIGN] 3-tuple\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def main() -> int:
    print(f"=== {GATE_ID} ===")
    input_files = {
        "canonical_constants": CANONICAL_CONSTANTS,
        "script": SCRIPT_PATH,
    }
    pins = log_input_pins(input_files)

    # ------------------------------------------------------------------
    # 1. Value-invariance check (NOT a directional claim — an equality check).
    #    The provenance write must NOT have changed any constant VALUE.
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("1. Value-invariance (provenance-transcription must NOT re-value)")
    print("=" * 76)
    live_values = {  # (local) the live imported values
        "w0_FW": float(w0_FW),
        "M_KK": float(M_KK),
        "Delta_B3": float(Delta_B3),
    }
    value_invariant = {}  # (local) per-constant bit-exact match
    for k, expected in ALL_TARGETS.items():
        match = (live_values[k] == expected)  # (local) exact equality (tolerance: exact)
        value_invariant[k] = match
        print(f"  {k:12s}: live={live_values[k]!r}  expected={expected!r}  bit-unchanged={match}")
    all_values_invariant = all(value_invariant.values())  # (local)
    print(f"  --> ALL values bit-unchanged: {all_values_invariant}")

    # Context cross-checks (route documentation; not gate-decisive)
    mkk_is_gravity_alias = (M_KK == M_KK_gravity)  # (local) M_KK is the gravity-route alias
    doubled_gap_nominal = 2.0 * float(Delta_B3_s53)  # (local) 0.168304 — the NOMINAL doubled gap
    doubled_gap_rel_dev = abs(doubled_gap_nominal - float(Delta_B3)) / float(Delta_B3)  # (local)
    print(f"  context: M_KK is M_KK_gravity alias = {mkk_is_gravity_alias} "
          f"(gravity route 7.43e16; Kerner alt {M_KK_kerner:.3e}; OOM_diff={OOM_diff_MKK:.6f})")
    print(f"  context: 2*Delta_B3_s53={doubled_gap_nominal:.6f} vs Delta_B3={Delta_B3} "
          f"(rel dev {doubled_gap_rel_dev:.4%} — NOMINAL doubling, NOT bit-exact; S38 predates s53)")

    # ------------------------------------------------------------------
    # 2. Provenance-PRESENT check (the gate's literal PASS predicate).
    #    Each target key must now carry a non-empty PROVENANCE-dict entry.
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("2. Provenance-PRESENT (the literal hygiene PASS predicate)")
    print("=" * 76)
    provenance_present = {}  # (local) per-constant non-empty PROVENANCE
    for k in ALL_TARGETS:
        entry = PROVENANCE.get(k)  # (local)
        present = provenance_nonempty(entry)  # (local)
        provenance_present[k] = present
        sess = entry.get("session") if entry else None  # (local)
        src = (entry.get("source") if entry else "") or ""  # (local)
        print(f"  {k:12s}: PROVENANCE non-empty={present}  session={sess!r}  source={src[:54]!r}")
    all_provenance_present = all(provenance_present.values())  # (local)
    print(f"  --> ALL target constants carry non-empty PROVENANCE: {all_provenance_present}")

    # Cross-check: M_KK_gravity (the alias source) provenance is intact + untouched.
    mkk_gravity_present = provenance_nonempty(PROVENANCE.get("M_KK_gravity"))  # (local)
    print(f"  cross-check: M_KK_gravity (alias source) provenance intact = {mkk_gravity_present}")

    # ------------------------------------------------------------------
    # 3. Item (b) f2=92 — NOTED ONLY (conditional; no consumer ==> no write)
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("3. Item (b) f2 ≈ 92 CC-dictionary value — NOTED ONLY (no write)")
    print("=" * 76)
    f2_default_pinned = (float(f_2_default) == 2.34)  # (local) the only pinned f_2 (Gaussian scheme)
    f2_cc_pinned = ("f_2_cc" in PROVENANCE) or ("f2_cc" in PROVENANCE)  # (local) is the CC f2=92 pinned?
    print(f"  f_2_default={f_2_default} (Gaussian-cutoff, S62) pinned = {f2_default_pinned}")
    print(f"  CC-dictionary f2≈{F2_CC_DICT_NOTED_VALUE:.0f} pinned as canonical = {f2_cc_pinned} "
          f"(EXPECTED False — conditional item, no consumer identified)")
    print("  DECISION: NO write for f2=92 (pinning an unconsumed value is canonical-clutter, not "
          "hygiene). Flagged in WP §W6-4 for orchestrator follow-up: pin ONLY if a consumer exists.")

    # ------------------------------------------------------------------
    # 4. Verdict
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("4. Verdict")
    print("=" * 76)
    # PASS iff every target constant is BOTH value-invariant AND provenance-present.
    verdict = "PASS" if (all_values_invariant and all_provenance_present) else "FAIL"  # (local)
    print(f"  all_values_invariant      = {all_values_invariant}")
    print(f"  all_provenance_present    = {all_provenance_present}")
    print(f"  >>> VERDICT: {verdict}")

    # ------------------------------------------------------------------
    # 5. value string
    # ------------------------------------------------------------------
    value_str = (  # (local)
        f"provenance_present_primary_w0_FW={provenance_present['w0_FW']}_M_KK={provenance_present['M_KK']}_"
        f"hygiene_a_Delta_B3={provenance_present['Delta_B3']}_"
        f"all_provenance_present={all_provenance_present}_"
        f"value_invariant_w0_FW={value_invariant['w0_FW']}_M_KK={value_invariant['M_KK']}_"
        f"Delta_B3={value_invariant['Delta_B3']}_all_values_invariant={all_values_invariant}_"
        f"w0_FW=-0.918_S58_four-fold-lock_binds_Falsifier1_DESI-DR3_dual-canonical_branch-iv_-0.842454_conditional_"
        f"M_KK=7.428660036284456e16_S42_gravity-route_alias_of_M_KK_gravity_Kerner-alt_5.04e17_OOM_diff_0.831665_"
        f"Delta_B3=0.176_S38_item-a_distinct_from_Delta_B3_s53_0.084152_nominal-2x_reldev_{doubled_gap_rel_dev:.4f}_"
        f"M_KK_gravity_provenance_intact={mkk_gravity_present}_"
        f"item_b_f2=92_NOTED-ONLY_no_consumer_no_write_f2_cc_pinned={f2_cc_pinned}_"
        f"fix=PROVENANCE-dict_entries_added_to_canonical_constants.py_values_BIT-UNCHANGED_"
        f"sync=knowledge.db_via_weave-update_get_constant_reads_live_dict_nonempty_NOW"
    )

    # ------------------------------------------------------------------
    # 6. dual-SHA over the PROVENANCE-dict target entries + facts
    # ------------------------------------------------------------------
    facts = {  # (local) provenance/value facts pinned into audit_sha256
        "all_values_invariant": str(all_values_invariant),
        "all_provenance_present": str(all_provenance_present),
        "w0_FW_value": f"{float(w0_FW):.12g}",
        "w0_FW_session": str(PROVENANCE.get("w0_FW", {}).get("session")),
        "M_KK_value": f"{float(M_KK):.17g}",
        "M_KK_session": str(PROVENANCE.get("M_KK", {}).get("session")),
        "Delta_B3_value": f"{float(Delta_B3):.12g}",
        "Delta_B3_session": str(PROVENANCE.get("Delta_B3", {}).get("session")),
        "f2_cc_pinned": str(f2_cc_pinned),
    }
    audit_sha, content_sha = compute_dual_sha(pins, facts)  # (local)

    # ------------------------------------------------------------------
    # 7. artifacts (npz + json + png) BEFORE verdict emission
    # ------------------------------------------------------------------
    _emit_npz_and_json(
        live_values, value_invariant, all_values_invariant,
        provenance_present, all_provenance_present, mkk_gravity_present,
        doubled_gap_nominal, doubled_gap_rel_dev, f2_default_pinned, f2_cc_pinned,
        verdict, value_str, audit_sha, content_sha,
    )
    _emit_plot(provenance_present, value_invariant, verdict)

    # ------------------------------------------------------------------
    # 8. emit verdict line (exactly one canonical + companion)
    # ------------------------------------------------------------------
    append_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"\n  4-tuple: (value=<...>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")
    print(f"\n  >>> VERDICT: {verdict}")
    print("  w0_FW (S58 four-fold lock; binds Falsifier #1 DESI DR3) + M_KK (S42 gravity-route alias)")
    print("  + Delta_B3 (S38; item (a)) now carry non-empty PROVENANCE; values BIT-UNCHANGED.")
    print("  Item (b) f2=92: NOTED-ONLY (no consumer, no write) — flagged in WP §W6-4 for orchestrator.")
    print("  knowledge.db syncs on next /weave --update; get_constant reads the live dict (non-empty NOW).")
    return 0  # verdict is DATA; exit 0 regardless of PASS/FAIL (math-scripts.md §"Exit Codes")


def _emit_npz_and_json(live_values, value_invariant, all_values_invariant,
                       provenance_present, all_provenance_present, mkk_gravity_present,
                       doubled_gap_nominal, doubled_gap_rel_dev, f2_default_pinned, f2_cc_pinned,
                       verdict, value_str, audit_sha, content_sha):
    np.savez(
        OUT_NPZ,
        # live values (bit-exact)
        w0_FW=np.float64(live_values["w0_FW"]),
        M_KK=np.float64(live_values["M_KK"]),
        Delta_B3=np.float64(live_values["Delta_B3"]),
        wa_FW=np.float64(wa_FW),
        M_KK_gravity=np.float64(M_KK_gravity),
        M_KK_kerner=np.float64(M_KK_kerner),
        OOM_diff_MKK=np.float64(OOM_diff_MKK),
        Delta_B3_s53=np.float64(Delta_B3_s53),
        doubled_gap_nominal=np.float64(doubled_gap_nominal),
        doubled_gap_rel_dev=np.float64(doubled_gap_rel_dev),
        f_2_default=np.float64(f_2_default),
        f2_cc_noted_value=np.float64(F2_CC_DICT_NOTED_VALUE),
        # value-invariance
        value_invariant_w0_FW=np.bool_(value_invariant["w0_FW"]),
        value_invariant_M_KK=np.bool_(value_invariant["M_KK"]),
        value_invariant_Delta_B3=np.bool_(value_invariant["Delta_B3"]),
        all_values_invariant=np.bool_(all_values_invariant),
        # provenance-present (the literal PASS predicate)
        provenance_present_w0_FW=np.bool_(provenance_present["w0_FW"]),
        provenance_present_M_KK=np.bool_(provenance_present["M_KK"]),
        provenance_present_Delta_B3=np.bool_(provenance_present["Delta_B3"]),
        all_provenance_present=np.bool_(all_provenance_present),
        mkk_gravity_provenance_intact=np.bool_(mkk_gravity_present),
        # item (b)
        f2_default_pinned=np.bool_(f2_default_pinned),
        f2_cc_pinned=np.bool_(f2_cc_pinned),
        f2_decision="NOTED-ONLY-no-consumer-no-write-flagged-for-orchestrator",
        # provenance sessions/sources for the three targets
        w0_FW_session=str(PROVENANCE.get("w0_FW", {}).get("session")),
        w0_FW_source=str(PROVENANCE.get("w0_FW", {}).get("source")),
        M_KK_session=str(PROVENANCE.get("M_KK", {}).get("session")),
        M_KK_source=str(PROVENANCE.get("M_KK", {}).get("source")),
        Delta_B3_session=str(PROVENANCE.get("Delta_B3", {}).get("session")),
        Delta_B3_source=str(PROVENANCE.get("Delta_B3", {}).get("source")),
        # metadata
        L_max=str(L_MAX),
        verdict=str(verdict),
        scheme=SCHEME,
        convention=CONVENTION,
        gate_id=GATE_ID,
        audit_sha256=str(audit_sha),
        content_sha256=str(content_sha),
        fix_target="canonical_constants.py PROVENANCE dict (Section F-hygiene)",
        revalue=np.bool_(False),
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")
    _chk = np.load(OUT_NPZ, allow_pickle=True)  # (local)
    rt_ok = (bool(_chk["all_provenance_present"]) == all_provenance_present) and (
        float(_chk["w0_FW"]) == live_values["w0_FW"]
    )  # (local) round-trip integrity
    print(f"  round-trip: npz all_provenance_present + w0_FW preserved: {rt_ok}")

    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "task": ("mack-cosmic-bridge W0-MKK-PROVENANCE: add PROVENANCE-dict entries for w0_FW + M_KK "
                 "(+ Delta_B3, routed-in hygiene item (a)) to canonical_constants.py; values bit-unchanged"),
        "targets": {
            "w0_FW": {
                "value": live_values["w0_FW"],
                "value_invariant": value_invariant["w0_FW"],
                "provenance_present": provenance_present["w0_FW"],
                "session": PROVENANCE.get("w0_FW", {}).get("session"),
                "source": PROVENANCE.get("w0_FW", {}).get("source"),
                "role": ("framework dark-energy w_0 from Volovik vacuum partition + effacement "
                         "(Gamma_effacement=0.99970), S58 four-fold lock; BINDS Falsifier #1 (DESI DR3 / "
                         "R_842 rectangle). Dual canonical: branch-(iv) w0_FW_R842=-0.842454 is "
                         "DR3-PASS-conditional (NOT a standalone canonical constant)."),
            },
            "M_KK": {
                "value": live_values["M_KK"],
                "value_invariant": value_invariant["M_KK"],
                "provenance_present": provenance_present["M_KK"],
                "session": PROVENANCE.get("M_KK", {}).get("session"),
                "source": PROVENANCE.get("M_KK", {}).get("source"),
                "role": ("default alias of M_KK_gravity = 7.428660036284456e16 GeV (spectral-zeta / "
                         "Newton's-constant gravity route, S42; conservative route). Kerner gauge-metric "
                         "alt M_KK_kerner=5.041679838376001e17; OOM_diff_MKK=0.831664779390838 (0.83-decade "
                         "tension, both CONST-FREEZE-42 PASS). Gap was on the bare alias; M_KK_gravity "
                         "already carried provenance."),
            },
            "Delta_B3": {
                "value": live_values["Delta_B3"],
                "value_invariant": value_invariant["Delta_B3"],
                "provenance_present": provenance_present["Delta_B3"],
                "session": PROVENANCE.get("Delta_B3", {}).get("session"),
                "source": PROVENANCE.get("Delta_B3", {}).get("source"),
                "role": ("S38 B3-sector pairing gap = 0.176 (M_KK units); routed-in hygiene item (a). "
                         "NOMINAL doubled-gap convention of Delta_B3_s53=0.084152 (S53), but 2x is "
                         f"approximate (2*Delta_B3_s53=0.168304, rel dev {doubled_gap_rel_dev:.4%}; S38 "
                         "predates the s53 per-band derivation). DISTINCT constant from Delta_B3_s53."),
            },
        },
        "item_b_f2_92": {
            "decision": "NOTED-ONLY (conditional; no write)",
            "reason": ("the only pinned f_2 is f_2_default=2.34 (Gaussian-cutoff, S62); the CC-dictionary "
                       "f2≈92 has no canonical pin and no identified consumer. Pinning an unconsumed value "
                       "would be canonical-clutter, not hygiene. Pin ONLY IF a consumer surfaces."),
            "f2_cc_pinned": f2_cc_pinned,
            "flagged_for": "orchestrator follow-up (WP §W6-4)",
        },
        "fix": {
            "target_file": "computations/_shared/canonical_constants.py",
            "where": "PROVENANCE dict, Section F-hygiene block before the closing brace",
            "operation": ("ADD machine-readable PROVENANCE-dict entries for the three keys; existing "
                          "variable assignments UNTOUCHED (provenance-transcription, NOT a re-value)."),
            "revalue": False,
            "update_constant_note": ("mcp.update_constant REFUSES to touch an existing constant by design "
                                     "('manually edit canonical_constants.py') — the manual PROVENANCE-dict "
                                     "edit is exactly that safe path. get_constant reads the live dict, so "
                                     "the provenance is visible immediately; knowledge.db syncs on next "
                                     "/weave --update per math-scripts.md §'Sync enforcement'."),
        },
        "substrate_framing": ("NON-PHONONIC constant-provenance hygiene. The constants ARE substrate-derived "
                              "(w0_FW from the Volovik vacuum partition + effacement; M_KK from the spectral-zeta / "
                              "Newton's-constant gravity route; Delta_B3 from the S38 B3-sector pairing gap). This "
                              "gate adds the audit-trail provenance so those substrate derivations are traceable "
                              "from the knowledge MCP — closing an AMRI-adjacent gap at the canonical-constants "
                              "layer (provenance belongs in canonical_constants.py + knowledge.db, NEVER in agent "
                              "memory) before the DESI DR3 falsifier binds."),
        "M1_M4_self_classification": {
            "M1_artifact_existence_with_content": True,
            "M2_canonical_constants_edit_plus_sha_no_numerical_compute": True,
            "M3_provenance_transcription_from_inline_comments_plus_knowledge_graph_edges": True,
            "M4_methodology_allowlist": "N/A (COMPUTE-class hygiene gate; no registry/rule-file edit)",
        },
    }
    OUT_JSON.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  JSON sidecar -> {OUT_JSON.relative_to(ROOT)}")


def _emit_plot(provenance_present, value_invariant, verdict):
    fig, ax = plt.subplots(1, 1, figsize=(11.0, 4.8))
    targets = list(provenance_present.keys())  # (local) ['w0_FW','M_KK','Delta_B3']
    y = np.arange(len(targets))[::-1]  # (local) top-to-bottom
    # Two status columns: provenance-present (x=0) and value-invariant (x=1)
    for yi, k in zip(y, targets):
        prov = provenance_present[k]  # (local)
        inv = value_invariant[k]  # (local)
        ax.plot([0], [yi], "o", ms=20, color=("C2" if prov else "C3"),
                markeredgecolor="black", zorder=3)
        ax.plot([1], [yi], "o", ms=20, color=("C2" if inv else "C3"),
                markeredgecolor="black", zorder=3)
        ax.text(0, yi, "P" if prov else "X", ha="center", va="center",
                fontsize=11, fontweight="bold", color="white", zorder=4)
        ax.text(1, yi, "P" if inv else "X", ha="center", va="center",
                fontsize=11, fontweight="bold", color="white", zorder=4)
        tag = ("(primary)" if k in PRIMARY_TARGETS else "(item a)")  # (local)
        ax.text(-0.35, yi, f"{k}  {tag}", ha="right", va="center", fontsize=11, fontweight="bold")
    ax.set_xlim(-1.7, 2.0)
    ax.set_ylim(-0.7, len(targets) - 0.3)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["PROVENANCE\npresent", "value\nbit-unchanged"], fontsize=10)
    ax.set_yticks([])
    # item (b) annotation
    ax.text(0.5, -0.55,
            "item (b) f2≈92: NOTED-ONLY (no consumer, no write) — flagged for orchestrator",
            ha="center", va="center", fontsize=8.5, style="italic", color="0.35")
    ax.set_title(
        f"{GATE_ID}  —  constant-PROVENANCE-completeness hygiene (mack-cosmic-bridge)\n"
        f"w0_FW (S58 four-fold lock; binds Falsifier #1 DESI DR3) + M_KK (S42 gravity-route alias) "
        f"+ Delta_B3 (S38)\n"
        f"PROVENANCE-dict entries ADDED to canonical_constants.py; values BIT-UNCHANGED "
        f"(transcription, not re-value)  —  verdict: {verdict}",
        fontsize=8.6,
    )
    ax.grid(True, axis="x", ls=":", alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
