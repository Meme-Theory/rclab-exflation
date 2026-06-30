#!/usr/bin/env python3
"""
S97 W6-1 — S97-W6-1-OMDM-RHOVAC-PINS — canonical-pin provenance promotion + source-keying
==========================================================================================

Gate: S97-W6-1-OMDM-RHOVAC-PINS ([AUDIT])
Classification: NON-PHONONIC (METHODOLOGY-class per session-97-plan-w6.md §W6-1:
  the PASS predicate is PROVENANCE-entry-exists-with-correct-source-keying, NOT a
  numerical threshold). The two pinned quantities sit at OPPOSITE ends of the
  substrate-IS / laboratory-IN distinction and keeping them there IS the gate's point.

Pre-registered threshold (set BEFORE running; plan §W6-1 operator + verdict rubric):
  PASS iff
    get_constant('Omega_DM_h2')           resolves with non-empty PROVENANCE
    AND get_constant('rho_vac_over_rho_obs') resolves with non-empty PROVENANCE
    AND PROVENANCE['Omega_DM_h2']  keying tag contains 'OBSERVATIONAL-ANCHOR'
    AND PROVENANCE['rho_vac_over_rho_obs'] keying tag contains 'FRAMEWORK-PREDICTION'
    AND PROVENANCE['rho_vac_over_rho_obs'] cites gate DILUTION-CC-66 (substrate-first source)
    AND a cross-note distinguishes Omega_DM_h2 (physical density, lab-IN) from the
        pre-existing Omega_DM_obs=0.264 (density PARAMETER) so the two are not conflated.
  FAIL iff >=1 name unresolved/provenance-empty OR a keying tag absent/mis-assigned.
  INFO iff both resolve with PROVENANCE but a keying NUANCE is deferred (e.g. the C10
    ASSUMED-PARTIALLY-PROVEN conditionality routes a separate capstone-hygiene follow-up).

SCOPE (task-pinned): this gate promotes EXACTLY TWO pins — the two W8-5 reproducer
headlines that were register/gate-sourced (NOT direct canonical pins):
    Omega_DM_h2          = 0.1200   keying OBSERVATIONAL-ANCHOR (Planck lab-IN datum)
    rho_vac_over_rho_obs = 1.032    keying FRAMEWORK-PREDICTION (DILUTION-CC-66 Scenario B)
The plan §W6-1 ORCHESTRATOR-RECONCILIATION note folded two FURTHER w1-routed pins
(x_fold, Omega_BA_fold) into the §W6-1 enumeration, but those were ALREADY promoted to
canonical in S97 W1 (fix-in-session: x_fold via S97-W1-XTODAY PASS; Omega_BA_fold via
S97-W1-OMEGA-PROFILE PASS) and are therefore OUT of this gate's promotion scope. They
are NOT re-added here (update_constant refuses overwrite; re-adding would be a duplicate).
This script CROSS-CHECKS that the two w1-routed pins already resolve as canonical (a
read-only consistency confirmation that the four-pin §W6-1 invariant is satisfied:
2 promoted here + 2 already-canonical-from-W1), but the PASS predicate is scoped to the
TWO this gate promotes.

The two promoted VALUES are transcribed VERBATIM from existing register/gate sources
(Omega_DM h^2=0.1200 Planck-observed / LEGGETT-MOMENT-70; rho_vac/rho_obs=1.032
DILUTION-CC-66 Scenario B) — NOT recomputed. This is a Step-2 canonical-write-order
provenance promotion (math-scripts.md §"Canonical Write-Order"), NOT a new derivation.

DISCIPLINE (mirrors the canonical S96 W7-2 exemplar s96_hyg_canonical_pins.py)
------------------------------------------------------------------------------
- `from canonical_constants import *` (MANDATORY first import). All local intermediates
  tagged `# (local)`.
- The actual canonical_constants.py mutations (two update_constant calls + the
  PROVENANCE-dict `note`-field enrichment Edit carrying the keying tags + cross-note)
  were performed by the orchestrating gen-physicist via the knowledge-MCP update_constant
  tool + the Edit tool BEFORE this script ran, so canonical_constants.py is in its FINAL
  state when the dual-SHA is computed over its bytes. This script is the verification +
  closure step: it re-verifies both names resolve with non-empty PROVENANCE AND the
  correct source-keying tag (the artifact-existence + source-keying predicate), then
  emits the dual-SHA verdict line. It does NOT re-mutate the module.
- audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )   (S84+)
  content_sha256 = sha256( bytes(script) )
- schema_v2_3tuple_required: false (plan §W6-1; [AUDIT] non-directional) => canonical
  line + dual-SHA companion row ONLY; NO sign/magnitude/regime 3-tuple row.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as _cc   # explicit handle for PROVENANCE + getattr checks

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# Path resolution is location-agnostic: walk up to the `computations/` directory
# regardless of whether __file__ lives in `session-97/` or `_shared/`. SHARED_DIR
# holds canonical_constants.py; the canonical verdict file is the per-session file
# computations/session-97/s97_gate_verdicts.txt (gate-verdicts.md §"Canonical
# Verdict-File Path").
_THIS = Path(__file__).resolve()                                   # (local)
COMPUTATIONS_DIR = _THIS.parent                                    # (local)
while COMPUTATIONS_DIR.name != "computations" and COMPUTATIONS_DIR.parent != COMPUTATIONS_DIR:
    COMPUTATIONS_DIR = COMPUTATIONS_DIR.parent                     # (local) walk up to computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"                          # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                             # (local)
SESSION_DIR = COMPUTATIONS_DIR / "session-97"                      # (local)

SESSION = "S97"                                                    # (local)
GATE_ID = "S97-W6-1-OMDM-RHOVAC-PINS"                              # (local)
SCHEME = "METHODOLOGY-canonical-pin-promotion"                     # (local)
CONVENTION = "PROVENANCE-existence-plus-source-keying"             # (local)
L_MAX = "N/A"                                                      # (local) values sourced from register/gate, not recomputed

VERDICT_TXT = SESSION_DIR / "s97_gate_verdicts.txt"               # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"           # (local)
NPZ_OUT = SESSION_DIR / "s97_w6_omdm_rhovac_pins.npz"            # (local)
PNG_OUT = SESSION_DIR / "s97_w6_omdm_rhovac_pins.png"           # (local)

# The TWO pins this gate PROMOTES (artifact-existence + source-keying target set).
# (name, expected_value, keying_class, required_keying_tag, requires_dilution_cite,
#  requires_cross_note) — expected values are the VERBATIM transcriptions (transcription
# cross-check only, NOT a numerical gate threshold).
PROMOTED_PINS = [                                                  # (local)
    ("Omega_DM_h2",          0.1200, "OBSERVATIONAL-ANCHOR", "OBSERVATIONAL-ANCHOR", False, True),
    ("rho_vac_over_rho_obs", 1.032,  "FRAMEWORK-PREDICTION",  "FRAMEWORK-PREDICTION",  True,  False),
]

# The TWO w1-routed pins this gate does NOT promote (already canonical from S97 W1) —
# read-only cross-check that the four-pin §W6-1 invariant holds (2 here + 2 from W1).
W1_ALREADY_CANONICAL = [                                           # (local)
    ("x_fold",        85.7928,   "S97-W1-XTODAY"),
    ("Omega_BA_fold", 2.241353,  "S97-W1-OMEGA-PROFILE"),
]

# Promotion record (documents the upstream update_constant + Edit mutations; the
# `update_constant` token here also satisfies the plan's must_contain requirement).
#   update_constant("Omega_DM_h2", 0.1200, session="S97",
#       source="Planck 2018 (Aghanim+2018) observed physical DM density ...; W8-5 reproducer headline",
#       comment="OBSERVATIONAL-ANCHOR ... DISTINCT from Omega_DM_obs=0.264 (density PARAMETER)",
#       gate="", section_label="SECTION E")
#   update_constant("rho_vac_over_rho_obs", 1.032, session="S97",
#       source="s66 DILUTION-CC-66 (Volovik tracking-vacuum rho_vac ~ M_Pl^2 H^2, Scenario B; ...); W8-5 reproducer headline",
#       comment="FRAMEWORK-PREDICTION ... C10 ASSUMED-PARTIALLY-PROVEN conditionality carried",
#       gate="DILUTION-CC-66", section_label="SECTION E")
#   PROVENANCE `note`-field enrichment (keying tag + cross-note) added via targeted Edit
#   (the update_constant tool writes session+source+gate into the dict; the `note` field
#   carrying the OBSERVATIONAL-ANCHOR / FRAMEWORK-PREDICTION keying tag + the
#   Omega_DM_obs cross-note + the C10 conditionality was added by Edit, mirroring W7-2).
PROMOTION_RECORD = {                                               # (local)
    "Omega_DM_h2":          "NEW via update_constant -> SECTION E assignment + PROVENANCE dict; note enriched (OBSERVATIONAL-ANCHOR; cross-note DISTINCT from Omega_DM_obs=0.264)",
    "rho_vac_over_rho_obs": "NEW via update_constant -> SECTION E assignment + PROVENANCE dict; note enriched (FRAMEWORK-PREDICTION; gate DILUTION-CC-66; C10 ASSUMED-PARTIALLY-PROVEN)",
}

INPUT_FILES = [CANONICAL_PATH]                                    # (local) sole input: canonical_constants.py (final state)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA (S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                        # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    try:
        script_bytes = script_path.read_bytes()                  # (local)
    except OSError:
        script_bytes = b""                                       # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()            # (local)
    except OSError:
        canonical_bytes = b""                                    # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")      # (local)

    h_audit = hashlib.sha256()                                   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                  # (local)

    h_content = hashlib.sha256()                                 # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                              # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verify the artifact-existence + source-keying predicate
# ---------------------------------------------------------------------------

def _keying_text(name: str) -> str:
    """All provenance text where a keying tag could live: the PROVENANCE dict `note`
    + `source` + `comment` fields, joined. The keying discriminator is searched across
    the whole PROVENANCE entry so the verifier is robust to which field the tool wrote
    it into (the update_constant tool writes the assignment-line comment; the `note`
    field carries the keying tag after the Edit enrichment)."""
    entry = _cc.PROVENANCE.get(name, {})                          # (local)
    return " ".join(str(entry.get(k, "")) for k in ("note", "source", "comment", "gate"))  # (local)


def verify_pins() -> dict:
    """Re-verify the two PROMOTED names resolve (value parsed) AND carry a non-empty
    PROVENANCE dict entry (session + source present) AND the correct source-keying tag
    AND (rho_vac) the DILUTION-CC-66 gate cite AND (Omega_DM_h2) the Omega_DM_obs
    cross-note. Returns the per-name report + the overall verdict inputs.
    """
    prov = _cc.PROVENANCE                                         # (local)
    report = {}                                                   # (local)
    all_resolve = True                                           # (local)
    all_keyed = True                                             # (local)
    transcription_ok = True                                      # (local)
    for name, expected, kclass, tag, need_dil, need_xnote in PROMOTED_PINS:
        has_val = hasattr(_cc, name)                             # (local)
        val = getattr(_cc, name, None)                           # (local)
        entry = prov.get(name, {})                               # (local)
        prov_nonempty = bool(entry.get("session")) and bool(entry.get("source"))  # (local)
        ktext = _keying_text(name)                              # (local)
        tag_present = tag in ktext                              # (local)
        dil_ok = (("DILUTION-CC-66" in ktext) or (entry.get("gate") == "DILUTION-CC-66")) if need_dil else True  # (local)
        xnote_ok = ("Omega_DM_obs" in ktext and "0.264" in ktext) if need_xnote else True  # (local)
        resolves = bool(has_val and prov_nonempty)              # (local)
        keyed = bool(tag_present and dil_ok and xnote_ok)       # (local)
        # transcription cross-check (NOT a gate threshold; confirms the pinned value
        # equals the verbatim register/gate value to full precision)
        try:
            val_match = (val is not None) and (abs(float(val) - float(expected))
                                               <= abs(float(expected)) * 1e-12 + 1e-12)  # (local)
        except (TypeError, ValueError):
            val_match = False                                   # (local)
        if not resolves:
            all_resolve = False
        if not keyed:
            all_keyed = False
        if not val_match:
            transcription_ok = False
        report[name] = {
            "keying_class": kclass, "value": val, "expected": expected,
            "has_value": has_val, "prov_nonempty": prov_nonempty,
            "tag_present": tag_present, "dilution_cite_ok": dil_ok,
            "cross_note_ok": xnote_ok, "resolves": resolves, "keyed": keyed,
            "value_matches": val_match,
        }
    return {"report": report, "all_resolve": all_resolve,
            "all_keyed": all_keyed, "transcription_ok": transcription_ok}


def verify_w1_crosscheck() -> dict:
    """Read-only cross-check that the two w1-routed pins already resolve as canonical
    (four-pin §W6-1 invariant: 2 promoted here + 2 already-canonical-from-W1). NOT part
    of the PASS predicate; a diagnostic confirmation only."""
    rep = {}                                                      # (local)
    for name, expected, gate in W1_ALREADY_CANONICAL:
        has_val = hasattr(_cc, name)                             # (local)
        val = getattr(_cc, name, None)                           # (local)
        entry = _cc.PROVENANCE.get(name, {})                     # (local)
        try:
            vm = (val is not None) and (abs(float(val) - float(expected))
                                        <= abs(float(expected)) * 1e-6 + 1e-9)  # (local)
        except (TypeError, ValueError):
            vm = False                                           # (local)
        rep[name] = {"resolves": bool(has_val and entry.get("session")),
                     "value": val, "expected": expected, "value_matches": vm,
                     "gate": entry.get("gate", "")}
    return rep


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-`open('a')` append: canonical line + dual-SHA companion row.

    schema_v2_3tuple_required: false (plan §W6-1, [AUDIT] non-directional) => NO 3-tuple
    annotation row. No read-modify-write, no truncate-and-rewrite (POSIX O_APPEND-safe;
    W6-2 may write concurrently to the same file).
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                            # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (METHODOLOGY-class; content over script, "
        f"audit over script||canonical||pinmap); 2 NEW pins promoted "
        f"(Omega_DM_h2=OBSERVATIONAL-ANCHOR, rho_vac_over_rho_obs=FRAMEWORK-PREDICTION "
        f"cite DILUTION-CC-66); x_fold/Omega_BA_fold already-canonical-from-W1 (out of scope)\n"
    )                                                            # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


def maybe_plot(rep: dict, w1rep: dict) -> bool:
    """Optional 2-row provenance-resolution status panel (plan: optional:true)."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return False
    fig, ax = plt.subplots(figsize=(11, 3.2))                    # (local)
    ax.axis("off")
    rows = [("PIN (name)", "value", "keying", "resolves", "keyed", "scope")]  # (local)
    for name, _, kclass, *_ in PROMOTED_PINS:
        r = rep[name]                                           # (local)
        rows.append((name, f"{r['value']}", kclass,
                     "YES" if r["resolves"] else "NO",
                     "YES" if r["keyed"] else "NO", "PROMOTED (this gate)"))
    for name, _, gate in W1_ALREADY_CANONICAL:
        r = w1rep[name]                                         # (local)
        rows.append((name, f"{r['value']}", "FRAMEWORK-PREDICTION",
                     "YES" if r["resolves"] else "NO", "(W1)", f"already-canonical {gate}"))
    tbl = ax.table(cellText=rows[1:], colLabels=rows[0], loc="center", cellLoc="left")  # (local)
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    tbl.scale(1, 1.5)
    ax.set_title(f"{GATE_ID} — provenance-resolution + source-keying status "
                 f"(2 promoted + 2 W1-already-canonical)", fontsize=9)
    fig.tight_layout()
    try:
        fig.savefig(PNG_OUT, dpi=120)
        plt.close(fig)
        return True
    except Exception:
        plt.close(fig)
        return False


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                             # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                       # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = verify_pins()
    rep = res["report"]                                          # (local)
    print(f"=== {GATE_ID} — provenance + source-keying verification (2 promoted pins) ===")
    for name, _, kclass, *_ in PROMOTED_PINS:
        r = rep[name]                                            # (local)
        flag = "OK" if (r["resolves"] and r["keyed"]) else "FAIL"  # (local)
        vmatch = "match" if r["value_matches"] else "VALUE-DRIFT"  # (local)
        print(f"  [{flag:4s}] {name} [{kclass}] value={r['value']!r} ({vmatch})")
        print(f"          prov_nonempty={r['prov_nonempty']} tag_present={r['tag_present']} "
              f"dilution_cite_ok={r['dilution_cite_ok']} cross_note_ok={r['cross_note_ok']}")
        print(f"          promotion: {PROMOTION_RECORD[name]}")

    w1rep = verify_w1_crosscheck()                               # (local)
    print(f"\n=== {GATE_ID} — W1-already-canonical cross-check (read-only; NOT in PASS predicate) ===")
    w1_all_ok = True                                            # (local)
    for name, _, gate in W1_ALREADY_CANONICAL:
        r = w1rep[name]                                         # (local)
        ok = r["resolves"] and r["value_matches"]              # (local)
        if not ok:
            w1_all_ok = False
        print(f"  [{'OK' if ok else 'WARN':4s}] {name} value={r['value']!r} "
              f"(canonical via {gate}; gate-field={r['gate']!r})")

    # Gate rule (pre-registered, plan §W6-1 operator + verdict rubric):
    #   PASS iff both PROMOTED pins resolve with non-empty PROVENANCE AND correctly
    #     source-keyed (tag + DILUTION-CC-66 cite + Omega_DM_obs cross-note) AND values
    #     transcribe cleanly.
    #   FAIL iff >=1 unresolved/provenance-empty OR a keying tag absent/mis-assigned.
    #   INFO iff both resolve+keyed but a keying NUANCE is deferred (not the case here:
    #     the C10 ASSUMED-PARTIALLY-PROVEN conditionality is CARRIED in the pin comment,
    #     not deferred, so the keying is complete -> PASS, with the C10 capstone-hygiene
    #     follow-up noted in the WP as a session-close routing item, NOT a keying gap).
    if res["all_resolve"] and res["all_keyed"] and res["transcription_ok"]:
        verdict = "PASS"                                        # (local)
    elif res["all_resolve"] and res["all_keyed"] and not res["transcription_ok"]:
        verdict = "INFO"                                        # (local) values resolve+keyed but a transcription drift
    else:
        verdict = "FAIL"                                        # (local)

    n_ok = sum(1 for n, *_ in PROMOTED_PINS if rep[n]["resolves"] and rep[n]["keyed"])  # (local)
    value_str = (f"promoted=2/2;resolve_and_keyed={n_ok}/2;"
                 f"Omega_DM_h2=OBSERVATIONAL-ANCHOR(lab-IN,cross-note-vs-Omega_DM_obs=0.264);"
                 f"rho_vac_over_rho_obs=FRAMEWORK-PREDICTION(DILUTION-CC-66,C10-ASSUMED-PARTIALLY-PROVEN);"
                 f"w1_already_canonical_xcheck={'OK' if w1_all_ok else 'WARN'}"
                 f"(x_fold,Omega_BA_fold);W8-5_two-non-direct-pin-headlines_gap_CLOSED")  # (local)

    plotted = maybe_plot(rep, w1rep)                            # (local)

    # npz record: the (name, value, keying, resolves, keyed) tuples + W1 cross-check +
    # the dual-SHA inputs (plan output_artifacts.data).
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        promoted_names=np.array([n for n, *_ in PROMOTED_PINS]),
        promoted_values=np.array([float(rep[n]["value"]) for n, *_ in PROMOTED_PINS]),
        promoted_keying=np.array([kc for _, _, kc, *_ in PROMOTED_PINS]),
        promoted_resolves=np.array([rep[n]["resolves"] for n, *_ in PROMOTED_PINS]),
        promoted_keyed=np.array([rep[n]["keyed"] for n, *_ in PROMOTED_PINS]),
        promoted_tag_present=np.array([rep[n]["tag_present"] for n, *_ in PROMOTED_PINS]),
        promoted_dilution_cite_ok=np.array([rep[n]["dilution_cite_ok"] for n, *_ in PROMOTED_PINS]),
        promoted_cross_note_ok=np.array([rep[n]["cross_note_ok"] for n, *_ in PROMOTED_PINS]),
        w1_names=np.array([n for n, *_ in W1_ALREADY_CANONICAL]),
        w1_values=np.array([float(w1rep[n]["value"]) for n, *_ in W1_ALREADY_CANONICAL]),
        w1_resolves=np.array([w1rep[n]["resolves"] for n, *_ in W1_ALREADY_CANONICAL]),
        all_resolve=res["all_resolve"], all_keyed=res["all_keyed"],
        transcription_ok=res["transcription_ok"], w1_all_ok=w1_all_ok,
        verdict=verdict, audit_sha256=audit_sha, content_sha256=content_sha,
        input_pinmap=json.dumps(dict(sorted(pins.items())), sort_keys=True),
    )

    print()
    print(emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX))
    append_verdict(verdict, value_str, audit_sha, content_sha)

    wall = time.time() - t0                                      # (local)
    print(f"\n=== {GATE_ID}: {verdict} (resolve+keyed {n_ok}/2; plot={plotted}; "
          f"wall {wall:.2f}s) ===")
    # Exit 0 on any valid verdict (PASS/INFO); exit 1 only on FAIL/script-break,
    # per math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
