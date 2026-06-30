#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-CONSOL-3REGISTER-TABLE — capstone §7.1 ATOMIC section-scoped patch
=====================================================================
mack-cosmic-bridge sole writer of the §7 falsifier/observable surface.

Applies the 3-register split (from s96_consol_3register_table.md) to the capstone
§7.1, as an ATOMIC section-scoped write (read -> splice ONLY the §7.1 region ->
fsync + os.replace). Preserves ALL other capstone sections byte-for-byte
(W7 landed §3.3/§5.3/§7.2/§7.3/§8.2a/§9 — must NOT be clobbered).

Patch operations (confined to the §7.1 region between the '### 7.1' header and the
'### 7.2' header):
  (1) INSERT the 3-register split block immediately after the §7.1 intro paragraph,
      BEFORE the flat 'Outputs by spectral-moment layer' table. The 3-register split
      is the PRIMARY epistemic view; the flat table is retained below as a
      "flat reference (all rows, one list)" detail.
  (2) FIX the sigma_8 comparison anchor in the flat table: 'Planck `0.829`' (which is
      S_8, mis-labeled) -> 'Planck σ₈ `0.811` (S₈ `0.829`)' (W6-7 anchor-hygiene; the
      canonical Planck σ₈ is 0.811, NOT 0.829).
  (3) ADD a one-line §7.2 cross-reference note for the W6-3 CGWB peak-frequency
      SCOPE-CORRECTION (the substantive correction lands in falsifier-master-inventory
      Row #7.audit; here we add a pointer so the §7 prose and the inventory agree).

NON-PHONONIC (methodology / curated-doc designated-writer reviewed patch).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import hashlib
from pathlib import Path

# Canonical import: the σ₈ anchor fix asserts the Planck σ₈ value (0.811) this patch writes.
_SHARED = Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))
from canonical_constants import sigma_8  # noqa: E402  Planck 2018 σ₈ = 0.811 (NOT S₈ = 0.829)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CAPSTONE = PROJECT_ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"
REG_MD = PROJECT_ROOT / "computations" / "session-96" / "s96_consol_3register_table.md"

# W7-landed section markers that MUST survive byte-for-byte (diff guard).
W7_GUARD_MARKERS = [
    "Scorecard status reconciliation (register-pinned)",     # §7.3 W8-1/W7-7a landing
    "α_s — the most-misread row, structurally resolved",     # §7.1 α_s box
    "CC caveat box — what the equilibrium identity",          # §7.1 CC caveat box
    "joint-BF multiplies ALGEBRAICALLY-AND-STATISTICALLY",   # §7.3 W7-7a
    "R_K(0)` normalization firewall",                         # §8.2a W7-4 firewall
]


def sha256_of_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    original = CAPSTONE.read_text(encoding="utf-8")
    orig_sha = sha256_of_bytes(original.encode("utf-8"))
    print(f"[patch] capstone original sha256={orig_sha[:16]}... ({len(original)} chars)")

    # Idempotency guard: if the 3-register split header is already present, do not double-insert.
    REG_HEADER = "Outputs by epistemic register (3-register split)"
    if REG_HEADER in original:
        print("[patch] 3-register split already present in capstone -> idempotent no-op (verify path)")
        # Still verify W7 guards survive.
        for m in W7_GUARD_MARKERS:
            assert m in original, f"W7 guard marker LOST: {m!r}"
        print("[patch] all W7 guard markers present; no write needed.")
        return 0

    lines = original.splitlines(keepends=True)

    # ---- locate the §7.1 region boundaries ----
    idx_71_header = None     # line idx of '### 7.1 Outputs by spectral-moment layer'
    idx_72_header = None     # line idx of '### 7.2 Falsifier anchors'
    for i, ln in enumerate(lines):
        if ln.startswith("### 7.1 "):
            idx_71_header = i
        elif ln.startswith("### 7.2 "):
            idx_72_header = i
            break
    assert idx_71_header is not None, "§7.1 header not found"
    assert idx_72_header is not None and idx_72_header > idx_71_header, "§7.2 header not found after §7.1"

    # The flat table header row within §7.1 (the '| Observable | Layer / E-no. | ...' line).
    idx_flat_table = None
    for i in range(idx_71_header, idx_72_header):
        if lines[i].startswith("| Observable |") and "Layer" in lines[i]:
            idx_flat_table = i
            break
    assert idx_flat_table is not None, "§7.1 flat table header not found"

    # ---- (1) build the 3-register split block (read the generated markdown) ----
    reg_block = REG_MD.read_text(encoding="utf-8").rstrip("\n")
    # Demote the generated '### §7.1 — ...' top header to a sub-note (the capstone already
    # has the '### 7.1' header); keep it as a bolded lead-in so the section structure is clean.
    reg_block_lines = reg_block.splitlines()
    if reg_block_lines and reg_block_lines[0].startswith("### §7.1"):
        reg_block_lines = reg_block_lines[1:]  # drop the duplicate top header
    reg_block = "\n".join(reg_block_lines).strip("\n")

    insert_block = (
        "\n"
        "> **Epistemic-register split (W8-2 consolidation, `S96-CONSOL-3REGISTER-TABLE`).** "
        "The single flat table below is re-presented as **three epistemic registers** so a referee "
        "reads each claim at its true register — the external review flagged the flat table for "
        "*\"visually flattening conditional and unconditional claims into a common rhetorical register.\"* "
        "The 3-register split (keyed by the `S96-CONSOL-STATUS-SYNC`-reconciled status tags) is the "
        "PRIMARY view; the flat table is retained as a flat reference. **No value changes** — only the "
        "epistemic sorting. SUM-check: 7 robust + 6 conditional + 1 falsified = 14 rows (partition exact, "
        "no flattening; `m_H` is a disclosed dual-status straddle placed in CONDITIONAL).\n\n"
        + reg_block + "\n\n"
        "**Flat reference (all 14 rows, one list).** The same rows, un-stratified, for cross-checking "
        "the partition above:\n"
    )

    # ---- assemble the patched §7.1 region ----
    # head = up to and including the §7.1 intro paragraph (everything before the flat table header)
    head = lines[:idx_flat_table]
    flat_and_tail = lines[idx_flat_table:idx_72_header]   # flat table + §7.1 prose boxes up to §7.2
    rest = lines[idx_72_header:]                           # §7.2 onward (UNTOUCHED)

    # ---- (2) fix the sigma_8 comparison anchor inside the flat table ----
    patched_flat = []
    sigma8_fixed = False
    for ln in flat_and_tail:
        if ln.startswith("| **σ₈†**") and "Planck `0.829`" in ln:
            assert abs(float(sigma_8) - 0.811) < 1e-9, (
                f"canonical sigma_8={sigma_8} != 0.811; anchor-fix value drift")  # (local)
            ln = ln.replace("Planck `0.829`",
                            f"Planck σ₈ `{sigma_8}` (S₈ `0.829`)")
            sigma8_fixed = True
        patched_flat.append(ln)
    assert sigma8_fixed, "σ₈ flat-table anchor fix did not apply (expected 'Planck `0.829`' in σ₈ row)"

    # ---- (3) §7.2 CGWB peak-frequency scope-correction cross-ref ----
    # Insert a pointer note immediately after the §7.2 header (line rest[0]) without touching
    # the W7-landed §7.2 rows. We add ONE blockquote note after the §7.2 header + its intro.
    cgwb_note = (
        "\n> **W8-2 scope-correction — CGWB row #7 (frequency vs amplitude).** The LISA flagship is the "
        "Ω_GW **IR-tail amplitude** (`Ω_GW^(A) ~ 1e-10` at 3 mHz, 11+ OOM above LISA-PLS; "
        "`S96-OBS-OMEGAGW-GGE-VS-ZN` PASS), **NOT** the spectral peak. The peak **frequency** sits at "
        "`f_obs ≈ 8.48×10³⁹ Hz` (GHz+, 43.9 decades above LISA; `S96-OBS-CGWB-PEAK-FREQ`, D4 resolved "
        "AGAINST the mHz peak) — reaching the LISA band would require `κ = 25 s/M_KK⁻¹`, 42.5 OOM from the "
        "natural `ħ/M_KK`. Read row #7 as the **amplitude** discriminator (live), not a peak-in-band claim. "
        "Full split: `falsifier-master-inventory.md` Row #7.audit.\n"
    )
    # rest[0] is the '### 7.2 ...' header line; rest[1] is blank; rest[2] is the §7.2 intro/table.
    # Place the note after the header line (rest[0]) and any immediately-following blank line.
    insert_at = 1                                                          # (local)
    while insert_at < len(rest) and rest[insert_at].strip() == "":
        insert_at += 1
    rest_patched = rest[:insert_at] + [cgwb_note] + rest[insert_at:]

    patched = "".join(head) + insert_block + "\n" + "".join(patched_flat) + "".join(rest_patched)

    # ---- diff guard: every W7 marker MUST survive ----
    for m in W7_GUARD_MARKERS:
        assert m in patched, f"W7 guard marker would be LOST by patch: {m!r}"
    # the §7.2 / §7.3 / §8 headers must all still be present
    for h in ("### 7.2 ", "### 7.3 ", "## §8 "):
        assert h in patched, f"section header LOST: {h!r}"

    # ---- atomic write (fsync + os.replace) ----
    tmp = CAPSTONE.with_suffix(".md.tmp_w82")
    with tmp.open("w", encoding="utf-8", newline="") as fp:
        fp.write(patched)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, CAPSTONE)

    new_sha = sha256_of_bytes(patched.encode("utf-8"))
    print(f"[patch] σ₈ anchor fixed: {sigma8_fixed}")
    print(f"[patch] capstone patched sha256={new_sha[:16]}... ({len(patched)} chars; "
          f"+{len(patched) - len(original)} chars)")
    print("[patch] 3-register split inserted; flat table retained; §7.2 CGWB scope-note added; "
          "W7 guards intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
