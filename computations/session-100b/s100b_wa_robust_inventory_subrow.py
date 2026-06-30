# -*- coding: utf-8 -*-
"""
S100b-WA-ROBUST Step-3 registry landing (mack-cosmic-bridge sole writer).

Canonical write-order Step 3 (math-scripts.md): after (1) verdict-line emission
via emit_verdict and (2) canonical_constants [SKIPPED -- no NEW framework
prediction constant: d_sigma is an observational-scoring output; wa_FW = 0
already canonical], this helper lands:

  a. falsifier-master-inventory.md -- Row #1 sub-row `1.wa-robust-s100b`
     ('w_a (Planck-low-ell-independent)' robustness scoring), inserted directly
     after the existing `1.dovekie-2026-update` sub-row (sole-writer file; the
     established Row-#1 sub-row house pattern).
  b. falsifier-watchlist.md -- `w_a (Planck-low-ell-independent)` audit-pin
     annotation section + change-log row.

All numbers are READ FROM s100b_wa_robust.npz at execution time (Class-8.3
round-trip discipline: downstream consumes the data file, not prose); the
dual SHAs are READ FROM the canonical verdict line. Idempotency-guarded.

NOT a computation gate: no verdict line is emitted by this helper.
"""

import io
import os
import re
import sys

import numpy as np

ROOT = r"C:\sandbox\Ainulindale Exflation"  # (local)
HERE = os.path.join(ROOT, "computations", "session-100b")  # (local)
NPZ = os.path.join(HERE, "s100b_wa_robust.npz")  # (local)
VERDICTS = os.path.join(HERE, "s100b_gate_verdicts.txt")  # (local)
INVENTORY = os.path.join(ROOT, "sessions", "framework", "registry",
                         "falsifier-master-inventory.md")  # (local)
WATCHLIST = os.path.join(ROOT, "sessions", "framework", "registry",
                         "falsifier-watchlist.md")  # (local)

SUBROW_KEY = "1.wa-robust-s100b"  # (local)
WATCH_MARKER = "#### `w_a (Planck-low-ell-independent)` -- S100b-WA-ROBUST audit-pin"  # (local)


def main():
    d = np.load(NPZ, allow_pickle=False)
    d_sigma = float(d["d_sigma"])  # (local)
    wa_mean = float(d["wa_mean"])  # (local)
    sig_up = float(d["wa_sig_up"])  # (local)
    sig_dn = float(d["wa_sig_dn"])  # (local)
    w0_mean = float(d["w0_mean"])  # (local)
    w0_q16 = float(d["w0_q16"])  # (local)
    w0_q84 = float(d["w0_q84"])  # (local)
    dsv = d["d_sigma_variants"]  # (local) V0..V3
    rb = d["route_b"]  # (local) [w0, w0_sig, wa, sig_up, sig_dn]
    rbc = d["route_b_consistency"]  # (local) [dAB, sigB, ok]
    dsb = d["d_sigma_route_b_anchor"]  # (local) [ACT, SPT]
    conv = d["conv_deltas"]  # (local) [dA, dB]

    verdict_line = None  # (local)
    with io.open(VERDICTS, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("S100b-WA-ROBUST:"):
                verdict_line = line.strip()  # (local) latest wins
    if verdict_line is None:
        print("FATAL: no S100b-WA-ROBUST canonical verdict line found -- run emit_verdict first")
        return 2
    m_a = re.search(r"audit_sha256=([a-f0-9]{64})", verdict_line)  # (local)
    m_c = re.search(r"content_sha256=([a-f0-9]{64})", verdict_line)  # (local)
    m_v = re.match(r"S100b-WA-ROBUST:\s+(PASS|FAIL|INFO)", verdict_line)  # (local)
    if not (m_a and m_c and m_v):
        print("FATAL: verdict line malformed")
        return 2
    audit16, content16 = m_a.group(1)[:16], m_c.group(1)[:16]  # (local)
    verdict = m_v.group(1)  # (local)

    tag = {"PASS": "SURVIVES (< 2 sigma)", "INFO": "INTERMEDIATE (2-3 sigma)",
           "FAIL": "UNDER PRESSURE (> 3 sigma)"}[verdict]  # (local)

    subrow = (
        f"| {SUBROW_KEY} | audit pins (Row #1 w_a-axis robustness sub-row; S100b W1-3 "
        f"`S100b-WA-ROBUST` mack-cosmic-bridge Planck-low-ell-independent scoring) | "
        f"four-fold lock w_a = 0 (S58) scored against the systematics-robust combination "
        f"free of the three DDE-signal localizations (SN photometric offset, Planck ell<~30 "
        f"anomaly, single z~0.7 bump): compressed Planck+ACT geometric CMB (R, ell_a, omega_b; "
        f"Bansal-Huterer Eq. 5-6) + DESI DR2 BAO (13 distances, Tab. IV) + Pantheon+ "
        f"(Efstathiou SS2(i) Om = 0.333 +/- 0.018, shape-matched); full-64-hex source pin per "
        f"`.claude/rules/gate-verdicts.md` | route-A compressed-likelihood reconstruction "
        f"(grid posterior, omega_b analytic marginalization) + route-B published anchor "
        f"(Giare Tab. II WMAP+ACT+DESI+PP) | "
        f"w_a(robust) = {wa_mean:.4f} +{sig_up:.4f}/-{sig_dn:.4f} => d_sigma = {d_sigma:.3f} "
        f"(sigma_gov = toward-zero upper bar) -- {tag}; vs canonical baselines 2.92 "
        f"(DR2-marginalized), 3.74 (DESY5-joint), 2.82 (PP-joint); route-B anchors: ACT+WMAP "
        f"{float(dsb[0]):.3f} sigma, SPT+WMAP {float(dsb[1]):.3f} sigma; SN-mapping variants "
        f"V1/V2/V3 = {float(dsv[1]):.3f}/{float(dsv[2]):.3f}/{float(dsv[3]):.3f} sigma | "
        f"n/a (audit-pin sub-row; Row #1 primary cell unchanged; R_842/DR3 binding NOT triggered "
        f"-- the robust combination is a DR2-era systematics probe, not the binding instrument) | "
        f"route-A vs route-B: |w_a^A - w_a^B| = {float(rbc[0]):.3f} <= 1 sigma^B = "
        f"{float(rbc[1]):.2f} ({'CONSISTENT' if rbc[2] > 0.5 else 'INCONSISTENT'}); "
        f"grid-convergence deltas (w0/wa, Om/H0 halving) = {float(conv[0]):.3f}/{float(conv[1]):.3f} "
        f"(< 0.05 pinned); route-A w_0 = {w0_mean:.4f} [{w0_q16:.4f}, {w0_q84:.4f}] | "
        f"n/a (audit-pin sub-row; detector horizon inherited from Row #1 = DESI DR3 2026 binding "
        f"instrument) | FW (inherited) | ABSOLUTE-sigma-gov-toward-zero-ROUTE-A-primary | N/A | "
        f"`{content16}` | `{audit16}` (gate `S100b-WA-ROBUST` {verdict}; full 64-hex in "
        f"computations/session-100b/s100b_gate_verdicts.txt) |\n"
    )

    with io.open(INVENTORY, "r", encoding="utf-8") as f:
        inv = f.read()  # (local)
    if SUBROW_KEY in inv:
        print(f"  inventory: sub-row {SUBROW_KEY} already present -- skipping (idempotent)")
    else:
        # insert directly after the 1.dovekie-2026-update sub-row line (Row #1 block)
        lines = inv.splitlines(keepends=True)  # (local)
        idx = None  # (local)
        for i, ln in enumerate(lines):
            if ln.startswith("| 1.dovekie-2026-update |"):
                idx = i
                break
        if idx is None:
            print("FATAL: dovekie anchor sub-row not found in inventory")
            return 2
        lines.insert(idx + 1, subrow)
        with io.open(INVENTORY, "w", encoding="utf-8", newline="") as f:
            f.write("".join(lines))
        print(f"  inventory: sub-row {SUBROW_KEY} inserted after 1.dovekie-2026-update")

    watch_section = f"""
---

## S100b W1-3 w_a robustness audit-pin (S100b-WA-ROBUST)

{WATCH_MARKER}

- **What**: the four-fold lock w_a = 0 (S58) scored against the Planck-low-ell-INDEPENDENT
  combination (compressed Planck+ACT geometric CMB + DESI DR2 BAO + Pantheon+) -- the
  combination free of the three DDE-signal localizations (SN photometric offset, Planck
  ell<~30 anomaly, single z~0.7 H(z) bump).
- **Result**: w_a(robust) = {wa_mean:.4f} +{sig_up:.4f}/-{sig_dn:.4f} => d_sigma = {d_sigma:.3f}
  ({verdict}; sigma_gov = toward-zero bar) vs canonical baselines 2.92 (DR2-marginalized) /
  3.74 (DESY5-joint) / 2.82 (PP-joint). Route-B published anchors (Giare Tab. II):
  ACT+WMAP {float(dsb[0]):.3f} sigma; SPT+WMAP {float(dsb[1]):.3f} sigma.
- **Sagan caveat (pre-registered)**: w_a = 0 is a NULL that LCDM shares -- survival earns
  FALSIFICATION-SURVIVAL only, NO Bayesian credit over LCDM; the discriminating quantity is
  w_0 at fixed w_a = 0 (W1-4 + DESI DR3 R_842).
- **Status impact**: `w_a` row stays LIVE; DR3 remains the binding instrument (R_842,
  S84-DR3-RESPONSE-PROTOCOL). This sub-row is the master-inventory `1.wa-robust-s100b` mirror.
- **Provenance**: gate `S100b-WA-ROBUST` ({verdict}), audit `{audit16}` / content `{content16}`
  (full 64-hex in computations/session-100b/s100b_gate_verdicts.txt);
  data computations/session-100b/s100b_wa_robust.npz.
"""

    with io.open(WATCHLIST, "r", encoding="utf-8") as f:
        watch = f.read()  # (local)
    if WATCH_MARKER in watch:
        print("  watchlist: annotation already present -- skipping (idempotent)")
    else:
        chlog_row = (f"| 2026-06-07 | S100b W1-3 | `S100b-WA-ROBUST` w_a robustness audit-pin appended "
                     f"(d_sigma = {d_sigma:.3f} {verdict} vs Planck-low-ell-independent combination; "
                     f"statuses UNCHANGED -- DR3 stays the binding instrument) | mack-cosmic-bridge |\n")  # (local)
        lines = watch.splitlines(keepends=True)  # (local)
        idx = None  # (local)
        for i, ln in enumerate(lines):
            if ln.startswith("| 2026-06-06 | S100b plan-freeze |"):
                idx = i
                break
        if idx is None:
            print("FATAL: watchlist change-log anchor row not found")
            return 2
        lines.insert(idx + 1, chlog_row)
        watch = "".join(lines) + watch_section  # (local)
        with io.open(WATCHLIST, "w", encoding="utf-8", newline="") as f:
            f.write(watch)
        print("  watchlist: annotation section + change-log row appended")
    print("Step-3 registry landing complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
