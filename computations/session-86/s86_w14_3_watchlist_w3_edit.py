"""
S86-WATCHLIST-W3-EDIT — Row #7 (CGWB rho_AC) Companion-null column + (A)/(C) discriminator.

GATE
----
S86-WATCHLIST-W3-EDIT (META — registry maintenance with substrate-direct content).

CONTEXT
-------
Per orchestrator override: P11 (`S86-MASTER-INVENTORY-W6-W13-LAND` in W13)
ALREADY landed the substantive content of plan §W14-3:
  - PAIR-3 annotation column with W13-2.Ω null pin `f514d642fe2a80ac` (8.299e-58)
  - Predictions cell with rho_AC=2.10 (fixed-f) / 2.38 (fixed-k) / 8.299e-58 (companion-null)
  - Live-watch envelope cell: PASS if (A) band; FAIL if (C) null confirmed
  - Internal-consistency split cell: (A) flat acoustic vs (C) Companion-null

ROUTE ADJUDICATION
------------------
Route (a) PASS-incremental-upgrade:
  Sub-(i) FULL-64-hex audit-pin sub-row 7.audit (analog of W14-2's row 3.audit upgrade)
  Sub-(ii) explicit (A)/(C) discriminator paragraph as stand-alone Notes sub-section
  Either or both qualify as ADDITIVE.

Route (b) INFO-P11-redundancy:
  Mark INFO with diagnostic; carry-forward review.

DECISION
--------
Route (a). Both sub-(i) and sub-(ii) are landed.
- Sub-(i): adds row 7.audit with FULL-64-hex content_sha256 + audit_sha256 from
  S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT (s85_gate_verdicts.txt:201). This
  parallels the row 3.audit landing W14-2 already executed and addresses the
  gate-verdicts.md "FULL 64-character hexdigest" canonical-form requirement
  for downstream audit-traceability.
- Sub-(ii): adds a 6-element discriminator paragraph as a Notes sub-section
  beneath the table. The 6 required content tokens (per Field 9 PASS criteria
  + Field 6 paragraph spec) are:
    1. Named (A) and (C) regulator classes
    2. 5-regulator partition F_4 = {ζ, Zubarev, SDW} (A) / M = {cutoff_sqrt, anomaly} (C)
    3. Source citation: S85 W12-4 + lizzi S-7 §V.6 Mellin Strip Theorem
    4. (A) prediction: O(10^-10) at f_LISA = 3 mHz (CGWB-ABSOLUTE-PT family cross-ref)
    5. (C) prediction: 8.299e-58 (W13-2.Ω)
    6. LISA Ω_GW > 10^-12 forward-falsifier threshold

These are ADDITIVE per the plan §W14-3 instruction. Re-writing P11-landed
cells is FORBIDDEN per the spawn prompt; this script does not touch any
existing row #7 cell content.

OUTPUT
------
- Edited sessions/framework/registry/falsifier-master-inventory.md (route (a) edit applied)
- Verdict line + companion row appended to computations/session-86/s86_gate_verdicts.txt

ENVIRONMENT
-----------
- Python: phonon-exflation-sim/.venv312/Scripts/python.exe
- GPU: NOT NEEDED (pure file I/O + SHA computation)
"""

import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INVENTORY_PATH = REPO_ROOT / "sessions" / "framework" / "falsifier-master-inventory.md"
S85_VERDICTS_PATH = REPO_ROOT / "computations" / "session-85" / "s85_gate_verdicts.txt"
S86_VERDICTS_PATH = REPO_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

# W13-2 canonical pins (verified via grep against s85_gate_verdicts.txt:201)
W13_2_AUDIT_SHA_FULL = "f514d642fe2a80ac408ddc0a09da94c5a8590a0127b4754fd337ea57eb2c02c1"  # (local)
W13_2_CONTENT_SHA_FULL = "58630dc36e59af32dfece11e521736c13c27f9a943a91ac03bb91249f2529779"  # (local)
W13_2_OMEGA_GW_LISA = 8.299e-58  # (local) per S85 W13-2 verdict line
W13_2_GATE_ID = "S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT"  # (local)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    # ------------------------------------------------------------------
    # Pre-edit pins
    # ------------------------------------------------------------------
    pre_edit_inventory_sha = sha256_file(INVENTORY_PATH)  # (local)
    pre_edit_inventory_bytes = INVENTORY_PATH.stat().st_size  # (local)
    s85_verdicts_input_sha = sha256_file(S85_VERDICTS_PATH)  # (local)

    print(f"INPUT-PIN: inventory_pre_sha256 = {pre_edit_inventory_sha}")
    print(f"INPUT-PIN: inventory_pre_bytes  = {pre_edit_inventory_bytes}")
    print(f"INPUT-PIN: s85_verdicts_sha256  = {s85_verdicts_input_sha}")
    print(f"INPUT-PIN: w13_2_audit_full     = {W13_2_AUDIT_SHA_FULL}")
    print(f"INPUT-PIN: w13_2_content_full   = {W13_2_CONTENT_SHA_FULL}")
    print(f"INPUT-PIN: w13_2_omega_gw_lisa  = {W13_2_OMEGA_GW_LISA}")

    # ------------------------------------------------------------------
    # Read pre-edit inventory and verify Row #7 content (P11 substrate)
    # ------------------------------------------------------------------
    inventory_text = INVENTORY_PATH.read_text(encoding="utf-8")  # (local)

    # Verify Row #7 primary cells are present (these MUST NOT be mutated)
    row7_required_substrings = [  # (local)
        "| 7 | CGWB rho_AC",
        "rho_AC=2.10 (fixed-f); rho_AC=2.38 (fixed-k); Companion-null (C-regulator) = 8.299e-58 (W13-2.Ω)",
        "PAIR-3: Companion-null (C-regulator) column with W13-2.Ω null pin `f514d642fe2a80ac` (8.299e-58)",
    ]
    for s in row7_required_substrings:
        assert s in inventory_text, f"P11 Row #7 substring missing pre-edit: {s!r}"

    # ------------------------------------------------------------------
    # Construct ADDITIVE edits
    # ------------------------------------------------------------------

    # Sub-(i): row 7.audit sub-row, parallel to row 3.audit pattern
    row_7_audit_line = (  # (local)
        "| 7.audit | audit pins (Row #7 strengthening citation; S86 W14-3) "
        "| full-64-hex W13-2 joint-Fisher canonical pin per `.claude/rules/gate-verdicts.md` "
        "| source: `computations/session-85/s85_gate_verdicts.txt:201` "
        "| W13-2 joint-Fisher pin: content_sha256=`" + W13_2_CONTENT_SHA_FULL + "` "
        "audit_sha256=`" + W13_2_AUDIT_SHA_FULL + "` "
        "— strengthening citation only; no value change to rho_AC predictions or Companion-null pin "
        "| n/a (audit-pin sub-row, not a live-watch envelope) "
        "| n/a (audit-pin sub-row carries no internal-consistency split; Row #7 primary cell unchanged) "
        "| n/a (audit-pin sub-row; detector horizon inherited from Row #7) "
        "| zeta+C-regulator-companion (inherited) "
        "| GGE-relic-tensor-Mach-13.75 (inherited) "
        "| 10 (inherited) "
        "| `e55e2b1aa85861f9` (inherited from Row #7) "
        "| `f720201bd1e2f4ef` (inherited from Row #7; FULL-64-hex W13-2.Ω inherited audit pin: "
        "`" + W13_2_AUDIT_SHA_FULL + "`) "
        "| S86 W14-3 audit-pin sub-row (additive citation upgrade per gate-verdicts.md canonical-form rule)\n"
    )

    # Sub-(ii): (A)/(C) discriminator paragraph as a stand-alone Notes
    # sub-section. Located AFTER the lab-falsifier table and BEFORE
    # `## Provenance`. This addresses Field 9 PASS criteria explicitly:
    # - named (A)/(C) classes
    # - 5-regulator partition + family names
    # - LISA falsification threshold cited
    discriminator_section = (  # (local)
        "\n## Row #7 — (A)/(C) regulator-class discriminator (S86 W14-3 paragraph)\n\n"
        "The 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} splits into the\n"
        "pure-a_4 family **F_4 = {ζ, Zubarev, SDW}** (the **(A)-regulator class**) and the\n"
        "mixed-support family **M = {cutoff_sqrt, anomaly}** (the **(C)-regulator class**)\n"
        "per S85 W12-4 + lizzi S-7 §V.6 Mellin Strip Theorem. CGWB Ω_GW(LISA) is\n"
        "regulator-class-bipolar:\n\n"
        "- **(A)-class prediction**: O(10⁻¹⁰) LISA-detectable spectral density at\n"
        "  f_LISA = 3 mHz (cross-ref CGWB-ABSOLUTE-PT family; S84 W6 PT-absolute landing).\n"
        "- **(C)-class prediction**: the W13-2.Ω 45-OOM null Ω_GW = 8.299e-58 (the\n"
        "  Companion-null pin landed in PAIR-3, sourced from\n"
        "  `computations/session-85/s85_gate_verdicts.txt:201`).\n\n"
        "**Forward-falsifier threshold**: a LISA detection at Ω_GW > 10⁻¹² over the\n"
        "4-yr nominal mission falsifies the (C) class; a LISA non-detection at\n"
        "Ω_GW < 10⁻¹² is consistent with both classes (with (C) the cleaner null).\n"
        "This is a forward-falsifier (mid-2030s nominal LISA horizon), not a S86 gate.\n\n"
        "**Cross-references**: S86 W8 P6/P7 CGWB ⊥ α_s 3-arm × 3-layer commit; S86 W3\n"
        "W0-7 re-emission; S86 W14-2 row 3.audit (parallel audit-pin sub-row pattern);\n"
        "S86 W11 C7 L_max-direct chain.\n\n"
        "**Substrate framing (PHONONIC)**: CGWB Ω_GW is a SUBSTRATE OBSERVABLE —\n"
        "gravitational-wave background generated by phonon-relay patterns in the\n"
        "post-fold GGE relic, propagating on the emergent g_M metric. The (A)/(C)\n"
        "regulator-class structure is INTERNAL to the substrate spectral triple:\n"
        "different regulator choices select different a_4^{<regulator>} spectral\n"
        "content, and a_4 is the gravity-channel spectral moment (per\n"
        "`.claude/rules/regulator-pin-discipline.md`). (A)-class regulators preserve\n"
        "a_4 magnitude; (C)-class regulators suppress it ~45 OOM. This row is\n"
        "structurally substrate-direct — the LISA reading discriminates between two\n"
        "equally substrate-grounded regulator-class commitments, NOT between the\n"
        "framework and a container-thinking alternative.\n"
    )

    # ------------------------------------------------------------------
    # Apply edits
    # ------------------------------------------------------------------

    # Edit 1: insert row 7.audit immediately after the existing row 7 line.
    # Row 7 begins with "| 7 | CGWB rho_AC". Locate its end-of-line and
    # inject row 7.audit on the next line.
    row7_anchor = "| 7 | CGWB rho_AC"  # (local)
    idx = inventory_text.index(row7_anchor)
    # Find end of that line (newline after row 7)
    line_end = inventory_text.index("\n", idx) + 1
    new_inventory_text = (
        inventory_text[:line_end] + row_7_audit_line + inventory_text[line_end:]
    )

    # Edit 2: insert discriminator section immediately before `## Provenance`.
    provenance_anchor = "\n## Provenance\n"  # (local)
    pidx = new_inventory_text.index(provenance_anchor)
    new_inventory_text = (
        new_inventory_text[:pidx] + discriminator_section + new_inventory_text[pidx:]
    )

    # ------------------------------------------------------------------
    # Verify ADDITIVE-only constraint:
    #   - Row #7 primary line remains present byte-equal
    #   - PAIR-3 annotation cell remains present byte-equal
    #   - Predictions cell remains present byte-equal
    # ------------------------------------------------------------------
    for s in row7_required_substrings:
        assert s in new_inventory_text, f"P11 Row #7 substring corrupted post-edit: {s!r}"

    # ------------------------------------------------------------------
    # Write inventory
    # ------------------------------------------------------------------
    INVENTORY_PATH.write_text(new_inventory_text, encoding="utf-8")
    post_edit_inventory_sha = sha256_file(INVENTORY_PATH)  # (local)
    post_edit_inventory_bytes = INVENTORY_PATH.stat().st_size  # (local)

    print(f"OUTPUT: inventory_post_sha256 = {post_edit_inventory_sha}")
    print(f"OUTPUT: inventory_post_bytes  = {post_edit_inventory_bytes}")
    print(f"OUTPUT: bytes_added           = {post_edit_inventory_bytes - pre_edit_inventory_bytes}")

    # Verdict counters
    column_added = 0  # (local) -- no NEW table column added (row 7.audit slots into existing schema)
    paragraphs_added = 1  # (local) -- discriminator paragraph (multi-paragraph Notes section)
    audit_subrow_added = 1  # (local) -- row 7.audit
    additive_only = True  # (local) -- verified by re-substring check above

    # ------------------------------------------------------------------
    # Build canonical input-pin map for closure (deterministic JSON)
    # ------------------------------------------------------------------
    pin_map = {
        "audit_subrow_added": audit_subrow_added,
        "column_added": column_added,
        "edit_rule": "ADDITIVE-only-no-mutation",
        "gate_id": "S86-WATCHLIST-W3-EDIT",
        "inventory_path": "sessions/framework/registry/falsifier-master-inventory.md",
        "inventory_post_sha256": post_edit_inventory_sha,
        "inventory_pre_sha256": pre_edit_inventory_sha,
        "p11_predecessor": "S86-MASTER-INVENTORY-W6-W13-LAND",
        "paragraphs_added": paragraphs_added,
        "regulator_class_partition": {
            "A_class": ["zeta", "Zubarev", "SDW"],
            "C_class": ["cutoff_sqrt", "anomaly"],
        },
        "route_adjudication": "a-PASS-incremental-upgrade",
        "row7_primary_unchanged": additive_only,
        "s85_verdicts_input_sha256": s85_verdicts_input_sha,
        "schema_version": "S84+",
        "source_verdict_gate_id": W13_2_GATE_ID,
        "w13_2_audit_sha256_full": W13_2_AUDIT_SHA_FULL,
        "w13_2_content_sha256_full": W13_2_CONTENT_SHA_FULL,
        "w13_2_omega_gw_lisa": W13_2_OMEGA_GW_LISA,
    }
    pin_map_canonical = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    audit_sha256 = hashlib.sha256(pin_map_canonical.encode("utf-8")).hexdigest()  # (local)

    print(f"OUTPUT: audit_sha256 = {audit_sha256}")

    # ------------------------------------------------------------------
    # Determine verdict per Field 9
    # PASS criteria:
    #   (1) row 7.audit landed with full-64-hex content+audit pins from W13-2 → YES
    #   (2) discriminator paragraph present naming (A)/(C) classes,
    #       5-regulator partition, LISA falsification threshold → YES
    #   (3) Row #7 primary cell byte-unchanged → YES (verified by re-substring check)
    # ------------------------------------------------------------------
    pass_check_1 = W13_2_AUDIT_SHA_FULL in new_inventory_text  # (local)
    pass_check_2 = (
        "(A)-regulator class" in new_inventory_text
        and "(C)-regulator class" in new_inventory_text
        and "F_4 = {ζ, Zubarev, SDW}" in new_inventory_text
        and "M = {cutoff_sqrt, anomaly}" in new_inventory_text
        and "Ω_GW > 10⁻¹²" in new_inventory_text
    )
    pass_check_3 = additive_only

    verdict = "PASS" if (pass_check_1 and pass_check_2 and pass_check_3) else "FAIL"  # (local)
    print(f"OUTPUT: pass_check_audit_pin_landed   = {pass_check_1}")
    print(f"OUTPUT: pass_check_discriminator_full = {pass_check_2}")
    print(f"OUTPUT: pass_check_row7_unchanged     = {pass_check_3}")
    print(f"OUTPUT: verdict = {verdict}")

    # ------------------------------------------------------------------
    # Output 4-tuple: (value=audit_subrow_added=1+paragraphs_added=1,
    #                 scheme=inventory, convention=MD-EDIT, L_max=n/a)
    # ------------------------------------------------------------------
    value_str = (  # (local)
        f"audit_subrow_added={audit_subrow_added}"
        f"+paragraphs_added={paragraphs_added}"
        f"+column_added={column_added}"
    )

    # ------------------------------------------------------------------
    # Append verdict line + companion row to s86_gate_verdicts.txt
    # ------------------------------------------------------------------
    verdict_line = (
        f"S86-WATCHLIST-W3-EDIT: {verdict} -- "
        f'value="{value_str}" '
        f"scheme=inventory convention=MD-EDIT L_max=n/a "
        f"audit_sha256={audit_sha256} "
        f"content_sha256={post_edit_inventory_sha} "
        f"schema_version=S84+\n"
    )
    companion_row = (
        f"# audit_sha256 companion row: S86-WATCHLIST-W3-EDIT "
        f"audit={audit_sha256[:16]} content={post_edit_inventory_sha[:16]}\n"
    )

    with open(S86_VERDICTS_PATH, "a", encoding="utf-8") as f:
        f.write(verdict_line)
        f.write(companion_row)

    print()
    print("VERDICT-LINE APPENDED:")
    print(verdict_line.rstrip())
    print(companion_row.rstrip())

    sys.exit(0)


if __name__ == "__main__":
    main()
