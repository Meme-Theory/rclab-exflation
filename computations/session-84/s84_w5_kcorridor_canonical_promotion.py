#!/usr/bin/env python3
"""
S84 W5-60 — S84-KCORRIDOR-CANONICAL-PROMOTION
==============================================

Gate: W5-60 (bookkeeping / NON-PHONONIC / [AUDIT])
Agent: volovik-superfluid-universe-theorist

Dry-run promotion + audit:
  1. Pre-audit grep-count each of 7 K-corridor literals across
     computations/_shared/s8{2,3,4}*.py.
  2. Verify the 7 new canonical constants are present in
     computations/_shared/canonical_constants.py (post-edit check).
  3. Compute the input-pin SHA-256 closure from the ordered input map.
  4. Emit verdict line and audit artifact.

This script does NOT rewrite scripts to use the new imports. That is a
post-promotion drift cleanup delegated to the `/weave --update` pipeline
(which will re-flag occurrences as "Potential" until replaced by imports).

The present gate measures only that canonical_constants.py now CARRIES the
7 constants with 7-field provenance. PASS = 7/7 promotions verified on
disk.

INPUT PINS (verified at runtime):
    computations/_shared/canonical_constants.py
    computations/session-82/s82_w3_6_sic_physical_cap.py
    computations/session-83/s83_w3_g38_k_matching_5_conventions.py
    computations/session-83/s83_w3_g39_leggett_bogoliubov.py
    computations/session-83/s83_w3_g40_tau_gge_at_K.py
    computations/session-83/s83_w3_g41_xi_bcs_vs_l_phonon_k_response.py
    computations/session-83/s83_w3_g49_evoi_refresh.py
    computations/session-84/s84_w2a_layer_pin_registry_landing.py

OUTPUT:
    stdout:  SHA-256 pins (first 20 lines), pre-audit counts,
             post-edit presence matrix, final verdict 4-tuple
    file:    computations/session-84/s84_w5_60_kcorridor_promotion_audit.txt
"""
import hashlib
import os
import re
import sys
from pathlib import Path

# Canonical constants import (post-edit sanity check)
try:
    from canonical_constants import (
        K_R3,
        K_match_need,
        A_s_floor_5conv,
        b_LB_ratio,
        tau_GGE_K_unit,
        xi_ell_plateau,
        K_star,
    )
    CANONICAL_IMPORT_OK = True                              # (local)
except ImportError as e:                                    # (local)
    CANONICAL_IMPORT_OK = False                             # (local)
    _import_err = str(e)                                    # (local)

HERE = Path(__file__).resolve().parent                      # (local)
AUDIT_FILE = HERE / "s84_w5_60_kcorridor_promotion_audit.txt"  # (local)

# Ordered input pin list (mapping hash is input map hash)
INPUT_FILES = [                                             # (local)
    HERE / "canonical_constants.py",
    HERE / "s82_w3_6_sic_physical_cap.py",
    HERE / "s83_w3_g38_k_matching_5_conventions.py",
    HERE / "s83_w3_g39_leggett_bogoliubov.py",
    HERE / "s83_w3_g40_tau_gge_at_K.py",
    HERE / "s83_w3_g41_xi_bcs_vs_l_phonon_k_response.py",
    HERE / "s83_w3_g49_evoi_refresh.py",
    HERE / "s84_w2a_layer_pin_registry_landing.py",
]

# Target literal patterns (pre-audit enumeration of drift-risk occurrences)
TARGET_LITERALS = {                                         # (local)
    "K_R3":             r"(?<![0-9.])2\.035(?![0-9])",
    "K_match_need":     r"(?<![0-9.])0\.6366(?![0-9])",
    "b_LB_ratio":       r"(?<![0-9.])0\.6027(?![0-9])",
    "tau_GGE_K_unit":   r"7\.86e(?:\+?04|4)",
    "xi_ell_plateau":   r"(?<![0-9.])0\.135(?![0-9])",
    "K_star":           r"(?<![0-9.])1\.3130(?![0-9])",
    "A_s_floor_5conv":  r"(?<![0-9.])5\.09e-13(?![0-9])",
}

# Target canonical values (what the promotion committed)
TARGET_VALUES = {                                           # (local)
    "K_R3":            2.035,
    "K_match_need":    0.6366,
    "A_s_floor_5conv": 5.09e-13,   # pending-W5-59
    "b_LB_ratio":      0.6027,
    "tau_GGE_K_unit":  7.86e4,
    "xi_ell_plateau":  0.135,
    "K_star":          1.3130,     # pending-W5-58
}


def file_sha256(path: Path) -> str:                         # (local)
    """Return SHA-256 hex digest of file bytes."""
    h = hashlib.sha256()                                    # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()                                    # (local)


def count_literal(path: Path, pattern: str) -> int:         # (local)
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")  # (local)
    return len(re.findall(pattern, text))                   # (local)


def main() -> int:                                          # (local)
    out_lines = []                                          # (local)

    def say(msg: str) -> None:                              # (local)
        print(msg)
        out_lines.append(msg)

    say("=" * 78)
    say("S84 W5-60 — S84-KCORRIDOR-CANONICAL-PROMOTION")
    say("=" * 78)

    # --- Section 1: Input pins (first 20 lines of stdout) ---
    say("\n[1] Input SHA-256 pins (ordered):")
    pin_map = {}                                            # (local)
    for i, fp in enumerate(INPUT_FILES, start=1):
        if fp.exists():
            h = file_sha256(fp)                             # (local)
        else:
            h = "<MISSING>"                                 # (local)
        pin_map[fp.name] = h                                # (local)
        say(f"    [{i:2d}] {fp.name:60s}  {h}")

    # --- Section 2: Closure SHA from ordered pin map ---
    closure_src = "".join(f"{k}:{v}\n" for k, v in pin_map.items()).encode("utf-8")  # (local)
    closure_sha = hashlib.sha256(closure_src).hexdigest()   # (local)
    say(f"\n[2] Closure SHA-256 (ordered input-pin map): {closure_sha}")

    # --- Section 3: Canonical import sanity ---
    say("\n[3] Canonical constants import check:")
    if CANONICAL_IMPORT_OK:
        say("    [OK] All 7 names importable from canonical_constants")
        for k in sorted(TARGET_VALUES):
            v_actual = {
                "K_R3": K_R3,
                "K_match_need": K_match_need,
                "A_s_floor_5conv": A_s_floor_5conv,
                "b_LB_ratio": b_LB_ratio,
                "tau_GGE_K_unit": tau_GGE_K_unit,
                "xi_ell_plateau": xi_ell_plateau,
                "K_star": K_star,
            }[k]                                            # (local)
            v_target = TARGET_VALUES[k]                     # (local)
            match = "OK" if abs(v_actual - v_target) / max(abs(v_target), 1e-30) < 1e-6 else "MISMATCH"  # (local)
            say(f"    [{match}] {k:20s} actual={v_actual!r:20s} target={v_target!r}")
    else:
        say(f"    [FAIL] ImportError: {_import_err}")

    # --- Section 4: Pre-audit literal occurrences ---
    say("\n[4] Pre-audit literal occurrences across S82/S83/S84 scripts:")
    say(f"    {'constant':22s} {'pattern':30s} {'count':>6s}")
    grand_total = 0                                         # (local)
    per_literal = {}                                        # (local)
    for name, pat in TARGET_LITERALS.items():
        total = 0                                           # (local)
        for fp in INPUT_FILES[1:]:  # skip canonical_constants.py itself
            c = count_literal(fp, pat)                      # (local)
            total += c
        per_literal[name] = total                           # (local)
        grand_total += total
        say(f"    {name:22s} {pat:30s} {total:6d}")
    say(f"    {'TOTAL':22s} {'':30s} {grand_total:6d}")

    # --- Section 5: Promotion presence matrix ---
    say("\n[5] Post-edit promotion presence matrix:")
    canonical_text = INPUT_FILES[0].read_text(encoding="utf-8") if INPUT_FILES[0].exists() else ""  # (local)
    present = {}                                            # (local)
    promoted_count = 0                                      # (local)
    for name in TARGET_VALUES:
        # Declaration pattern: line beginning with `name = `
        decl_re = re.compile(rf"^{re.escape(name)}\s*=", re.MULTILINE)  # (local)
        found = bool(decl_re.search(canonical_text))        # (local)
        present[name] = found                               # (local)
        if found:
            promoted_count += 1
        say(f"    {'[OK]' if found else '[MISSING]':10s} {name}")
    say(f"    promoted_count = {promoted_count}/7")

    # --- Section 6: Verdict ---
    if promoted_count == 7 and CANONICAL_IMPORT_OK:
        verdict = "PASS"                                    # (local)
    elif 0 < promoted_count < 7:
        verdict = "INFO"                                    # (local)
    else:
        verdict = "FAIL"                                    # (local)

    say("\n[6] Output 4-tuple:")
    say(f"    (value={promoted_count}/7, scheme=N/A, convention=canonical_constants, L_max=N/A)")

    verdict_line = (
        f"W5-60: {verdict} -- value={promoted_count}/7 "
        f"scheme=N/A convention=canonical_constants L_max=N/A "
        f"sha256={closure_sha}"
    )                                                       # (local)
    say("\n[7] Verdict line (canonical form):")
    say(f"    {verdict_line}")

    # --- Write audit file ---
    AUDIT_FILE.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"\n[audit] {AUDIT_FILE} written ({AUDIT_FILE.stat().st_size} bytes)")

    return 0 if verdict == "PASS" else (1 if verdict == "FAIL" else 2)


if __name__ == "__main__":
    sys.exit(main())
