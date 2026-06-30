#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S101-Y1-ZERO-PERMANENCE-LINE  (S101 Wave-6, gate W6-8)
=====================================================

Registry append-end permanence-ledger landing — LAST writer in the W6
single-writer registry chain (serialization 7-of-7; PD-4). Lands the 6c
drafted-verbatim MAP-B `Y₁ = 0 EXACT` permanence line as a NON-LETTER `###`
append-end ledger entry placed immediately AFTER the last §VII letter entry
(currently §VII.BR, landed by W6-6) in `sessions/permanent-results-registry.md`.

Slot reservation: `sessions/framework/s101-slot-pre-allocation-lockfile.md`
block `RESERVED-FOR-S101-W6-8-Y1-ZERO-LINE` (reserves the entry-CLASS, not a
§VII letter — no §VII letter is consumed).

Single-shot AFTER pattern (per `.claude/rules/registry-landing.md §"Bridge-Landing
Script Architecture"` + `computations/_bridge_landing_script_template.py`,
SHA 876c018fafea84742d06934a2061eb765ef41a042cb87ba0f4138caffbe9a68c):

    build_promotion_text  (pure; no I/O)
      -> write_atomic_with_fsync  (BINARY append, newline='\\n', NO neighbor flatten)
      -> re_read + verify_section_matches  (single boolean)
      -> emit ONCE  (print_verdict_payload; agent then calls emit_verdict)

The BEFORE pattern (write -> verify -> conditional rewrite -> re-emit) is
FORBIDDEN. Idempotent: a clean prior landing of the identical block is a NO-OP
re-verify (PRE/POST registry SHA pinned; W6-3 / W6-6 lessons — no dup, single
`###` header prefix, no neighbor flatten).

Substrate framing (PARTICLE): under the MAP-B Casimir-graded substrate-forward
Yukawa map, the lightest neutrino's Yukawa eigenvalue ∝ the quadratic Casimir of
its Peter-Weyl sector; the trivial representation (0,0) has C₂ = 0 identically.
Direction of explanation: D_K Peter-Weyl sector content -> C₂(0,0) = 0
(representation theory, EXACT) -> Y₁ = 0 -> m₁ = 0 (the normal-ordering floor).
The rank-deficiency LCDM-side fits impose by hand EMERGES from the algebra.

NO new sign/direction/threshold claim is computed — drafted-verbatim
transcription. The structural zero C₂(0,0)=0 was established at S100a W5-1 (MAP-B
leg, audit 4f92a5513ad69b07c0ae4ee8d5ed3ffe263aadfd67f19c6634d9d2a1be4d0c3f) and
adjudicated by the S100a W-4 D5 seesaw workshop; this ledger line records that
genre membership without re-opening the W5-1 map-uniqueness INFO.

Env: phonon-exflation-sim/.venv312/Scripts/python.exe ; cwd = project root.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

# ---- canonical constants import (MANDATORY per CLAUDE.md / math-scripts.md) ----
sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import *  # noqa: F401,F403  (compliance import; no framework literal hardcoded)

# ---------------------------------------------------------------------------
# Paths + static SHA pins (from session-101-plan-w6.md §W6-8 input_files)
# ---------------------------------------------------------------------------
ROOT = Path(".").resolve()
HK_PATH        = ROOT / "sessions/session-100a/session-100a-housekeeping.md"
W4_WS_PATH     = ROOT / "sessions/session-100a/workshops/s100a-w5-d5-seesaw-adjudication-workshop.md"
TEMPLATE_PATH  = ROOT / "computations/_bridge_landing_script_template.py"
LOCKFILE_PATH  = ROOT / "sessions/framework/s101-slot-pre-allocation-lockfile.md"
REGISTRY_PATH  = ROOT / "sessions/permanent-results-registry.md"
NPZ_PATH       = ROOT / "computations/session-101/s101_w6_8_y1_zero_permanence_line.npz"

# Static SHA pins (plan §W6-8 input_files + Wave-6 Input-SHA Ledger)
PIN_HK_SHA       = "07b164c185ffd724d3495d27561c3a67f6796381010503b76a41ad31b39f8571"
PIN_W4_WS_SHA    = "d7632f2c6e4e455d02e0640182933fcbac301a8fea2b082218abb2b2d67f0ca5"
PIN_TEMPLATE_SHA = "876c018fafea84742d06934a2061eb765ef41a042cb87ba0f4138caffbe9a68c"
# Anchor row: S100a W5-1 = S100a-MD-NORMALIZATION (MAP-B leg) full-64 audit
ANCHOR_W51_AUDIT = "4f92a5513ad69b07c0ae4ee8d5ed3ffe263aadfd67f19c6634d9d2a1be4d0c3f"

# Pre-registered verbatim-extraction self-test pins (computed at plan-prep from the
# pinned housekeeping byte content; HARD-asserted at runtime to catch span drift).
EXPECT_SPAN_CHARS  = 292   # (local)
EXPECT_SPAN_UTF8   = 302   # (local)
EXPECT_SPAN_SHA    = "1c62dd566b5be9823ed966e8d8807e402e34e2a464e36909831dbdffb5a41379"

GATE_ID    = "S101-Y1-ZERO-PERMANENCE-LINE"
ENTRY_CLASS = "append-end-permanence-ledger-NON-LETTER"
RESERVED_FOR = "RESERVED-FOR-S101-W6-8-Y1-ZERO-LINE"
ENTRY_ANCHOR_HEADER = "### Y1-ZERO-PERMANENCE — MAP-B structural zero"  # uniqueness/idempotency probe


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# (0) Input-SHA pre-flight (static pins must match on disk)
# ---------------------------------------------------------------------------
def preflight_inputs():
    checks = {
        "housekeeping": (HK_PATH, PIN_HK_SHA),
        "w4_workshop":  (W4_WS_PATH, PIN_W4_WS_SHA),
        "bridge_template": (TEMPLATE_PATH, PIN_TEMPLATE_SHA),
    }
    out = {}
    for name, (p, pin) in checks.items():
        actual = sha256_file(p)
        ok = (actual == pin)
        out[name] = {"path": str(p), "pin": pin, "actual": actual, "match": ok}
        print(f"[input-pin] {name:16s} pin={pin[:16]}… actual={actual[:16]}… match={ok}")
        if not ok:
            raise SystemExit(f"INPUT-SHA MISMATCH on {name}: pinned {pin} != on-disk {actual}")
    # lockfile + registry are runtime-resolved (live targets); log their SHAs
    out["lockfile"] = {"path": str(LOCKFILE_PATH), "sha256": sha256_file(LOCKFILE_PATH)}
    print(f"[input-pin] lockfile         sha256={out['lockfile']['sha256'][:16]}… (runtime-resolved)")
    return out


# ---------------------------------------------------------------------------
# (1) Programmatic verbatim extraction of the 6c span from housekeeping §D
# ---------------------------------------------------------------------------
def extract_6c_line() -> str:
    """Extract the drafted-verbatim quoted span between *" and "* of the
    '(6c) MAP-B permanence-ledger line' bullet in housekeeping §D.
    HARD-assert span length + SHA (catches any source drift)."""
    txt = HK_PATH.read_text(encoding="utf-8")
    marker = "**(6c) MAP-B permanence-ledger line**"
    idx = txt.find(marker)
    if idx < 0:
        raise SystemExit("EXTRACTION FAIL: 6c marker not found in housekeeping §D")
    q_open = txt.find('*"', idx)
    q_close = txt.find('"*', q_open + 2)
    if q_open < 0 or q_close < 0:
        raise SystemExit("EXTRACTION FAIL: 6c quoted span delimiters (*\" … \"*) not found")
    line = txt[q_open + 2: q_close]  # exclusive of the *" and "*

    n_chars = len(line)                       # (local)
    n_bytes = len(line.encode("utf-8"))       # (local)
    span_sha = sha256_text(line)              # (local)
    print(f"[extract] 6c span: {n_chars} chars / {n_bytes} utf-8 bytes ; sha={span_sha[:16]}…")

    # HARD asserts — drafted-verbatim binding (plan item (b))
    assert line.startswith("Y₁ = 0 EXACT from C₂(0,0) = 0"), "6c span start drift"
    assert line.endswith("previously imposed by hand)."), "6c span end drift"
    assert "—" in line, "6c span em-dash missing"
    assert n_chars == EXPECT_SPAN_CHARS, f"span char-count drift: {n_chars} != {EXPECT_SPAN_CHARS}"
    assert n_bytes == EXPECT_SPAN_UTF8, f"span utf8-byte drift: {n_bytes} != {EXPECT_SPAN_UTF8}"
    assert span_sha == EXPECT_SPAN_SHA, f"span SHA drift: {span_sha} != {EXPECT_SPAN_SHA}"
    print("[extract] HARD-ASSERTS PASS (start/end/em-dash/char/byte/SHA all match pinned span)")
    return line


# ---------------------------------------------------------------------------
# (2) build_promotion_text  (PURE — no I/O; full text in memory)
# ---------------------------------------------------------------------------
def build_promotion_text(six_c_line: str) -> str:
    """Produce the EXACT append-end ledger block to write. Pure function.

    Block structure (plan item (a)-(d)):
      (a) HEADER — non-letter `###` append-end ledger entry
      (b) THE LINE — VERBATIM (the extracted 6c span; byte-as-source)
      (c) ANCHOR ROW — S100a W5-1 = S100a-MD-NORMALIZATION (full-64 audit) +
          W-4 AGENDA-6c workshop provenance + housekeeping §D 6c
      (d) SCOPE NOTE — records the structural-zero genre membership; does NOT
          promote MAP-B over MAP-A (W5-1 INFO map-non-uniqueness untouched)
    """
    header = ("### Y1-ZERO-PERMANENCE — MAP-B structural zero "
              "(S100a W-4 AGENDA-6c drafted-verbatim; S101 W6-8 landing — gen-physicist)")

    body = (
        f"{header}\n"
        f"\n"
        f"**Permanence-ledger line (drafted-verbatim, S100a W-4 AGENDA-6c; binding).** "
        f"This is a permanence-ledger entry appended after the last §VII letter "
        f"entry (the lockfile reserves the entry-class "
        f"`{RESERVED_FOR}`, not a §VII letter; no §VII letter is consumed). "
        f"The line below is byte-verbatim from the SHA-pinned housekeeping §D "
        f"`(6c)` quoted span (unicode em-dashes/subscripts land as in the source):\n"
        f"\n"
        f"> {six_c_line}\n"
        f"\n"
        f"**Anchor row.** S100a W5-1 = `S100a-MD-NORMALIZATION` "
        f"(full-64 audit_sha256 `{ANCHOR_W51_AUDIT}`; the MAP-B Casimir-graded map "
        f"is one of the two substrate-forward Y_i maps recorded there) + provenance "
        f"pointer to the W-4 workshop AGENDA-6c routing "
        f"(`sessions/session-100a/workshops/s100a-w5-d5-seesaw-adjudication-workshop.md`, "
        f"SHA `{PIN_W4_WS_SHA}`) + housekeeping §D `(6c)` "
        f"(`sessions/session-100a/session-100a-housekeeping.md`, SHA `{PIN_HK_SHA}`). "
        f"Structural content: Y₁ = 0 is EXACT because the trivial representation's "
        f"quadratic Casimir C₂(0,0) = 0 enters the MAP-B Casimir-graded Yukawa "
        f"multiplicatively — representation theory, not a tuned parameter; "
        f"the rank-deficiency m₁ = 0 (normal-ordering floor) EMERGES from the algebra.\n"
        f"\n"
        f"**Scope note.** This line records the STRUCTURAL-ZERO genre membership of "
        f"Y₁ = 0 under MAP-B; it does NOT promote MAP-B over MAP-A — the S100a W5-1 "
        f"INFO recorded the two substrate-forward Y_i maps NON-UNIQUE (47.4% "
        f"disagreement) with the residual-Dirac-scale anchor STRUCTURALLY IRREDUCIBLE, "
        f"and that map-uniqueness adjudication is untouched by this ledger line.\n"
        f"\n"
        f"**Provenance.** Drafted in FINAL form by the S100a W-4 D5 seesaw-adjudication "
        f"workshop (R3 [AGENDA-6c]); routed ROUTED-TO-ORCHESTRATOR to the S101 "
        f"bridge-landing wave per housekeeping §D. Landed S101 W6-8 (single-shot "
        f"AFTER-pattern, gen-physicist), 7-of-7 (LAST) in the W6 single-writer "
        f"registry chain — its append point follows the W6-1…W6-6 §VII.BM–BR "
        f"extensions. Lockfile reservation: `{RESERVED_FOR}` "
        f"(`sessions/framework/s101-slot-pre-allocation-lockfile.md`). Cross-link: "
        f"S100a-MD-NORMALIZATION INFO lineage; EVOI §1 rank-3 (Σm_ν seesaw) LANDED row.\n"
    )
    return body


def make_append_payload(promotion_text: str) -> bytes:
    """Bytes to append. The registry currently ends with a single '\\n'.
    Prepend ONE '\\n' separator (blank line before the `###` header → clean
    markdown), append the block (which ends in a single '\\n'). NO neighbor
    flatten — the prior §VII.BR entry's terminal newline is preserved intact."""
    return ("\n" + promotion_text).encode("utf-8")


# ---------------------------------------------------------------------------
# (3) write_atomic_with_fsync — BINARY append, no neighbor flatten
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(append_bytes: bytes):
    with open(REGISTRY_PATH, "ab") as fh:   # binary append; no '\n' translation
        fh.write(append_bytes)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# (4) re_read + verify_section_matches
# ---------------------------------------------------------------------------
def re_read_entry_block() -> str:
    """Re-read the on-disk append-end ledger entry: from the header anchor to EOF."""
    txt = REGISTRY_PATH.read_text(encoding="utf-8")
    i = txt.find(ENTRY_ANCHOR_HEADER)
    if i < 0:
        return ""
    return txt[i:]  # header → EOF (this is the LAST block in the file)


def verify_section_matches(actual_block: str, expected_block: str) -> bool:
    return actual_block == expected_block


# ---------------------------------------------------------------------------
# audit_sha256 — closure over the ordered input-pin map (runtime-computed)
# ---------------------------------------------------------------------------
def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def print_verdict_payload(verdict, value, scheme, convention, l_max,
                          audit_sha, content_sha):
    """Print the canonical verdict payload for the agent to pass to emit_verdict.
    The script PRINTS; the agent calls the race-safe emit_verdict MCP tool."""
    print("\n===== VERDICT PAYLOAD (agent -> emit_verdict) =====")
    print(f"gate_id      = {GATE_ID}")
    print(f"session      = 101")
    print(f"verdict      = {verdict}")
    print(f"value        = {value}")
    print(f"scheme       = {scheme}")
    print(f"convention   = {convention}")
    print(f"l_max        = {l_max}")
    print(f"audit_sha256 = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    print("===================================================")


def main():
    print("=" * 72)
    print(f"{GATE_ID}  —  S101 W6-8 append-end permanence-ledger landing")
    print("=" * 72)

    # (0) input pins
    inputs = preflight_inputs()
    lockfile_sha = inputs["lockfile"]["sha256"]

    # Confirm lockfile reserves this entry-class to W6-8
    lf_txt = LOCKFILE_PATH.read_text(encoding="utf-8")
    if RESERVED_FOR not in lf_txt:
        raise SystemExit(f"LOCKFILE FAIL: {RESERVED_FOR} block not present")
    print(f"[lockfile] {RESERVED_FOR} present — entry-class reserved to W6-8")

    # Registry PRE-append state SHA (idempotency + audit pin)
    registry_pre_sha = sha256_file(REGISTRY_PATH)
    print(f"[registry] PRE-append SHA = {registry_pre_sha[:16]}…  "
          f"({REGISTRY_PATH.read_bytes().__len__()} bytes)")

    # (1) verbatim extraction (HARD-asserted)
    six_c_line = extract_6c_line()
    span_sha = sha256_text(six_c_line)  # (local)

    # (2) build promotion text (pure)
    promotion_text = build_promotion_text(six_c_line)
    promo_sha = sha256_text(promotion_text)  # (local)
    print(f"[build] promotion_text: {len(promotion_text)} chars ; sha={promo_sha[:16]}…")

    # Idempotency: if the identical block is already the file tail, NO-OP re-verify
    existing = re_read_entry_block()
    already_clean = (existing == promotion_text)
    if existing and already_clean:
        print("[idempotent] identical ledger block already on disk — NO-OP re-verify (no append)")
    elif existing and not already_clean:
        # A non-identical prior entry exists → honest FAIL (do NOT rewrite; AFTER pattern)
        print("[idempotent] a NON-identical Y1-ZERO block exists on disk — honest mismatch path")
    else:
        # (3) write (binary append, no neighbor flatten)
        append_bytes = make_append_payload(promotion_text)
        write_atomic_with_fsync(append_bytes)
        print(f"[write] appended {len(append_bytes)} bytes (1 leading '\\n' separator + block)")

    # (4) re-read + verify (single point of decision)
    actual_block = re_read_entry_block()
    matched = verify_section_matches(actual_block, promotion_text)
    print(f"[verify] section_match = {matched}")

    # content_sha256 over the re-read on-disk ledger entry (post-fsync)
    content_sha = sha256_text(actual_block) if actual_block else sha256_text("")

    # Registry POST-append state SHA
    registry_post_sha = sha256_file(REGISTRY_PATH)
    print(f"[registry] POST-append SHA = {registry_post_sha[:16]}…  "
          f"({REGISTRY_PATH.read_bytes().__len__()} bytes)")

    # audit_sha256 closure over the ordered input-pin map (per-gate-distinct)
    audit_pin_map = {
        "gate_id": GATE_ID,
        "entry_class": ENTRY_CLASS,
        "reserved_for": RESERVED_FOR,
        "script_sha256": sha256_file(Path(__file__).resolve()),
        "housekeeping_sha256": PIN_HK_SHA,
        "w4_workshop_sha256": PIN_W4_WS_SHA,
        "bridge_template_sha256": PIN_TEMPLATE_SHA,
        "lockfile_sha256": lockfile_sha,
        "registry_pre_append_sha256": registry_pre_sha,
        "registry_post_append_sha256": registry_post_sha,
        "anchor_w51_audit": ANCHOR_W51_AUDIT,
        "extraction_span_sha256": span_sha,
        "promotion_text_sha256": promo_sha,
        "scheme": "BRIDGE-LANDING-AFTER-PATTERN",
        "convention": "SINGLE-SHOT-VERBATIM-EXTRACTION",
    }
    audit_sha = closure_hash(audit_pin_map)

    verdict = "PASS" if matched else "FAIL"
    value = ("Y1=0_EXACT_C2(0,0)=0_MAP-B_permanence-ledger_landed_append-end_NON-LETTER"
             if matched else
             "entry_mismatch_or_quoted-span_drift_honest_close_remediation_S102")

    # landing-record npz
    import numpy as np
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        entry_anchor_header=ENTRY_ANCHOR_HEADER,
        extraction_span=six_c_line,
        extraction_span_chars=len(six_c_line),
        extraction_span_utf8_bytes=len(six_c_line.encode("utf-8")),
        extraction_span_sha256=span_sha,
        promotion_text_sha256=promo_sha,
        content_sha256=content_sha,
        audit_sha256=audit_sha,
        registry_pre_append_sha256=registry_pre_sha,
        registry_post_append_sha256=registry_post_sha,
        anchor_w51_audit=ANCHOR_W51_AUDIT,
        C2_trivial_rep=0,  # C₂(0,0)=0 exact-integer (structural zero)
        Y1=0,              # Y₁=0 exact (MAP-B)
        m1_eV=0.0,         # m₁=0 normal-ordering floor
        section_match=matched,
        reserved_for=RESERVED_FOR,
        ts=datetime.now(timezone.utc).isoformat(),
    )
    print(f"[npz] wrote {NPZ_PATH}")

    print(f"\n[SHA] extraction_span_sha256 = {span_sha}")
    print(f"[SHA] content_sha256        = {content_sha}")
    print(f"[SHA] audit_sha256          = {audit_sha}")

    print_verdict_payload(verdict, value, "BRIDGE-LANDING-AFTER-PATTERN",
                          "SINGLE-SHOT-VERBATIM-EXTRACTION", "N/A",
                          audit_sha, content_sha)

    # exit 0 regardless of scientific verdict (verdict is data, not script health)
    sys.exit(0)


if __name__ == "__main__":
    main()
