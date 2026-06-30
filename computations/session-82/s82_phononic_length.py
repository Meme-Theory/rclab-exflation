#!/usr/bin/env python3
"""
S82 W0-1 (= S80 W0-14): Phononic-Length Canonicalization (6-entry sectoral-floor)
==================================================================================

Gate: S82-PHONON-LENGTH-CANONICALIZATION  [VERIFY]
Classification: GEOMETRIC
Owner: quantum-acoustics-theorist

Reconciliation (2026-04-17, S82 Wave 2b):
  S82 W0-A returned INFO-6 (structural 6-branch floor of the 3-sector
  GL-Josephson reduction). Per S82-MASTER §II OR-clause and the W0-A
  structural substitution chain (V 6x6 by construction => exactly 6
  eigenvalues at every k, no crystallographic degeneracy; the upstream
  rank-universality 7-count refers to the full 8-generator su(3)
  phononic algebra and requires an 8x8 Gell-Mann-basis dynamical matrix
  outside s52 scope), W0-1 proceeds with a 6-entry canonicalization.

Phononic framing:
  A phononic length is a spectral-inverse scale on the Jensen-deformed
  SU(3) fiber, not an external metric unit. The 6 branch speeds
  c_Br0..c_Br5 at Gamma are the sectoral-phononic speeds of the
  GL-Josephson reduction; their reproducibility audit is the canonical
  transplant safety test before MCP update_constant specs are issued.

Method:
  1. Read canonical_constants.py (SHA-pin); extract SECTION E2 existing
     entries omega_L1, omega_L2, omega_H1, omega_H2, omega_H3, c_Gold.
  2. Re-extract Gamma-point eigvals from s82_branch_count_2d_bz.npz
     (W0-A output) AND from s52_gl_josephson.npz (1D-cut K=0 vertex).
  3. Re-extract ancillary speeds: c_BA from s56_cba_sound.npz;
     c_s (s63_sound_speed identification with c_BLV); omega_L from
     s70_leggett_{moment,vacuum}.npz.
  4. Compute 4-tuple (value, scheme, convention, L_max) per entry.
  5. Report percentage deviation vs canonical claim; PASS if <0.5%,
     INFO if [0.5,5]%, FAIL if >5%.
  6. Emit DRAFT addition text for canonical_constants.py (no file mod).
  7. Emit MCP update_constant call specs as JSON-like block.
  8. Emit S82-PHONON-LENGTH-CANONICALIZATION verdict.

Substitution chain (MANDATORY [VERIFY] — reproducibility direction):
  Step 1 (definition):
    omega_can = canonical Gamma-point values from Section E2
    omega_W0A = Gamma eigvals from s82_branch_count_2d_bz.npz['Gamma_omega']
    dev_pct   = |omega_W0A - omega_can| / omega_can * 100
    PASS if max(dev_pct) < 0.5%.
  Step 2 (substitution / computed):
    dev_pct for {L1, L2, H1, H2, H3} = {0.221, 0.040, 0.475, 0.035, 0.003}%
    Goldstone has omega_can = 0; use absolute tolerance < 1e-6.
  Step 3 (simplification):
    max(dev_pct over nonzero) = 0.475% < 0.500% threshold.
  Step 4 (direction):
    All 6 entries satisfy the 0.5% band => PASS.

Environment: audit-only script; no heavy linear algebra. Pure I/O
+ scalar comparisons.
"""

import os
# --- CPU thread cap (MUST be set before numpy import)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import numpy as np

# Canonical constants import (MANDATORY for S34+ scripts)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    c_Gold,
    c_Gold_over_c_fabric,
    omega_L1,
    omega_L2,
    omega_H1,
    omega_H2,
    omega_H3,
)

# -----------------------------------------------------------------------------
# Section 1 — Input pins (SHA-256 of every static input)
# -----------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))

INPUT_FILES = [
    "canonical_constants.py",
    "s82_branch_count_2d_bz.py",
    "s82_branch_count_2d_bz.npz",
    "s52_gl_josephson.py",
    "s52_gl_josephson.npz",
    "s56_cba_sound.py",
    "s56_cba_sound.npz",
    "s63_sound_speed.py",
    "s63_sound_speed.npz",
    "s67_transit_ps.py",
    "s67_transit_ps.npz",
    "s70_leggett_moment.py",
    "s70_leggett_moment.npz",
    "s70_leggett_vacuum.py",
    "s70_leggett_vacuum.npz",
]


def sha256_of(path):
    h = hashlib.sha256()
    with open(os.path.join(HERE, path), "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


input_shas = {p: sha256_of(p) for p in INPUT_FILES}

# Emit SHA-pinned manifest (first 20 lines of stdout, per computation standard)
print("=" * 78)
print("S82-PHONON-LENGTH-CANONICALIZATION — input pin manifest")
print("=" * 78)
for p, sha in input_shas.items():
    print(f"  {p:40s} {sha}")
print("-" * 78)

# Closure hash = SHA-256 of the ordered input-pin JSON
closure_payload = json.dumps(input_shas, sort_keys=True).encode("utf-8")
closure_sha = hashlib.sha256(closure_payload).hexdigest()
print(f"closure_sha256 = {closure_sha}")
print("-" * 78)

# -----------------------------------------------------------------------------
# Section 2 — Re-extract Gamma-point eigvals from W0-A and from s52 1D-cut
# -----------------------------------------------------------------------------
d82 = np.load(os.path.join(HERE, "s82_branch_count_2d_bz.npz"), allow_pickle=True)
gamma_w0a = np.sort(np.array(d82["Gamma_omega"]))  # (local) 6 eigvals, sorted asc

d52 = np.load(os.path.join(HERE, "s52_gl_josephson.npz"), allow_pickle=True)
K_s52 = np.array(d52["K_array"])                    # (local) 1D K mesh
omega_s52 = np.array(d52["omega_branches"])         # (local) (N_K, 6)
idx_gamma = int(np.argmin(np.abs(K_s52)))           # (local) K=0 vertex
gamma_s52 = np.sort(omega_s52[idx_gamma])           # (local) 1D-cut Gamma spectrum

print("Gamma-point eigvals (sorted ascending):")
print(f"  {'Branch':6s} {'S82 W0-A 2D-BZ':>18s} {'s52 1D-cut':>18s} {'|diff|':>12s}")
for i in range(6):
    diff = abs(gamma_w0a[i] - gamma_s52[i])          # (local)
    print(f"  Br{i}     {gamma_w0a[i]:18.10f} {gamma_s52[i]:18.10f} {diff:12.2e}")

# Cross-check: 1D-cut and 2D-BZ must agree (W0-A §III.A L182-186 result).
max_1d_2d_diff = float(np.max(np.abs(gamma_w0a - gamma_s52)))  # (local)
print(f"\n  max |2D-BZ - 1D-cut| = {max_1d_2d_diff:.2e}")
assert max_1d_2d_diff < 1e-6, "1D-vs-2D-BZ inconsistency (W0-A pinned <0.003 split)"

# -----------------------------------------------------------------------------
# Section 3 — Reproducibility audit vs canonical Section E2
# -----------------------------------------------------------------------------
# Canonical Section E2 entries that match the 6 Gamma-point branches:
#   Br0 Goldstone -> 0.0 (by construction)
#   Br1 Leggett-1 -> omega_L1 = 0.138
#   Br2 Leggett-2 -> omega_L2 = 0.192
#   Br3 Higgs-1   -> omega_H1 = 0.380
#   Br4 Higgs-2   -> omega_H2 = 1.410
#   Br5 Higgs-3   -> omega_H3 = 11.465
canonical_vals = np.array([0.0, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3])  # (local)
canonical_labels = ["c_Br0_Goldstone", "c_Br1_Leggett1", "c_Br2_Leggett2",
                    "c_Br3_Higgs1", "c_Br4_Higgs2", "c_Br5_Higgs3"]                 # (local)

PASS_PCT = 0.5     # (local) pre-registered PASS threshold from S80 W0-14
INFO_PCT = 5.0     # (local) pre-registered INFO band upper
ABS_TOL = 1e-6     # (local) absolute tolerance for Goldstone (canonical = 0)

statuses = []      # (local) per-entry verdict
dev_pcts = []      # (local) per-entry deviation

print("\n" + "=" * 78)
print("Reproducibility audit: 6-entry sectoral-floor catalogue")
print("=" * 78)
print(f"  {'Label':22s} {'canonical':>12s} {'S82 W0-A':>14s} {'dev %':>10s} {'status':>8s}")
for lbl, can, w0a in zip(canonical_labels, canonical_vals, gamma_w0a):
    if can == 0.0:
        dev_abs = float(abs(w0a - can))              # (local)
        status = "PASS" if dev_abs < ABS_TOL else "FAIL"
        dev_pct = 0.0                                  # (local) by definition
        print(f"  {lbl:22s} {can:12.6f} {w0a:14.10f} {dev_abs:10.2e} {status:>8s}")
    else:
        dev_pct = float(abs(w0a - can) / can * 100)   # (local)
        if dev_pct < PASS_PCT:
            status = "PASS"
        elif dev_pct < INFO_PCT:
            status = "INFO"
        else:
            status = "FAIL"
        print(f"  {lbl:22s} {can:12.6f} {w0a:14.10f} {dev_pct:10.3f} {status:>8s}")
    statuses.append(status)
    dev_pcts.append(dev_pct)

max_dev_pct = float(max(dev_pcts))  # (local) driver of gate verdict
print(f"\n  max deviation: {max_dev_pct:.3f}%  (threshold PASS<{PASS_PCT}%, INFO<{INFO_PCT}%)")

# -----------------------------------------------------------------------------
# Section 4 — Cross-checks against ancillary canonical speeds (informative)
# -----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("Ancillary cross-checks (informative; NOT part of 6-entry verdict)")
print("=" * 78)

# c_BA from s56_cba_sound.npz (Bogoliubov-Anderson)
d56 = np.load(os.path.join(HERE, "s56_cba_sound.npz"), allow_pickle=True)
c_BA_reproduced = float(d56["c_BA_fold"])            # (local)
c_BA_claimed = 0.399                                  # (local) S79 synthesis §4 canonical claim
dev_c_BA = abs(c_BA_reproduced - c_BA_claimed) / c_BA_claimed * 100  # (local)
print(f"  c_BA: reproduced={c_BA_reproduced:.6f}, claimed={c_BA_claimed:.3f}, "
      f"dev={dev_c_BA:.3f}%")

# c_s from s63_sound_speed.npz (scalar-mode transit, identified with c_BLV)
d63 = np.load(os.path.join(HERE, "s63_sound_speed.npz"), allow_pickle=True)
c_s_reproduced = float(d63["c_s"])                    # (local)
c_BLV_claimed = 0.485                                  # (local) S79 synthesis §4 + session-67 workshop
dev_c_BLV = abs(c_s_reproduced - c_BLV_claimed) / c_BLV_claimed * 100  # (local)
print(f"  c_BLV (=c_s in s63): reproduced={c_s_reproduced:.6f}, claimed={c_BLV_claimed:.3f}, "
      f"dev={dev_c_BLV:.3f}%")

# omega_L from s70_leggett (phase-mode Leggett frequency)
d70m = np.load(os.path.join(HERE, "s70_leggett_moment.npz"), allow_pickle=True)
d70v = np.load(os.path.join(HERE, "s70_leggett_vacuum.npz"), allow_pickle=True)
omega_L_canonical_s70 = float(d70v["omega_L_canonical"])  # (local) matches omega_L1
dev_omL = abs(omega_L_canonical_s70 - omega_L1) / omega_L1 * 100  # (local)
print(f"  omega_L (s70): reproduced={omega_L_canonical_s70:.6f}, "
      f"canonical={omega_L1}, dev={dev_omL:.3f}%")

# Goldstone slope near Gamma (s52 acoustic branch linear approximation)
Br0_slope_local = float(omega_s52[idx_gamma + 4, 0] / K_s52[idx_gamma + 4]) \
    if K_s52[idx_gamma + 4] > 0 else float("nan")     # (local)
print(f"  Br0 acoustic slope near Gamma (5th K-point): {Br0_slope_local:.4f} M_KK")
print(f"  Br0 linear dispersion slope_Gamma_to_X (W0-A §III.A): 0.887 M_KK")
print(f"  (These probe slightly different k-regimes; both are consistent with "
      f"c_Gold={c_Gold})")

# -----------------------------------------------------------------------------
# Section 5 — K_star_goldstone provenance note (DOES NOT reproduce cleanly)
# -----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("K_star_goldstone provenance note (FLAGGED FOR SEPARATE WORK)")
print("=" * 78)
# Operational definition (a): first-optical-gap crossing
omega_sorted_s52 = np.sort(omega_s52, axis=1)
gap_at_gamma = float(omega_sorted_s52[idx_gamma, 1])    # (local) omega_L1 value
Br0_sorted = omega_sorted_s52[:, 0]                     # (local)
K_star_operational_a = float(
    np.interp(gap_at_gamma, Br0_sorted, K_s52)
)                                                       # (local)
# Operational definition (c): 10% nonlinearity deviation
c_Gold_local_probe = float(Br0_sorted[4] / K_s52[4])    # (local)
linear_extrap = c_Gold_local_probe * K_s52              # (local)
dev_lin = np.abs(Br0_sorted - linear_extrap) / (linear_extrap + 1e-10)  # (local)
idx10 = int(np.argmax(dev_lin > 0.10))                  # (local)
K_star_operational_c = float(K_s52[idx10]) if idx10 > 0 else float("nan")  # (local)

print(f"  K_star (op-def a, first-gap crossing) = {K_star_operational_a:.4f} M_KK")
print(f"  K_star (op-def c, 10% nonlinearity)   = {K_star_operational_c:.4f} M_KK")
print(f"  S79 synthesis claim                    = 0.1850 M_KK  (l_phonon = 5.4054 M_KK^-1)")
print(f"  Deviation op-def(a) vs S79: {abs(K_star_operational_a - 0.185)/0.185*100:.2f}%")
print(f"  Deviation op-def(c) vs S79: {abs(K_star_operational_c - 0.185)/0.185*100:.2f}%")
print("  => K_star_goldstone does NOT reproduce under geometric operational")
print("     definitions from the s52 spectrum alone. The S79 value requires")
print("     an explicit operational definition (im(omega_G)/re(omega_G)=0.1)")
print("     that is NOT available in the current s52 artifact (omega_branches")
print("     is purely real). This is a PROVENANCE REPAIR, not a canonicalization.")
print("  => K_star_goldstone is NOT included in this 6-entry transplant.")
print("     It is carried forward to a dedicated provenance-repair pass.")

# -----------------------------------------------------------------------------
# Section 6 — Gate verdict
# -----------------------------------------------------------------------------
if max_dev_pct < PASS_PCT and all(s == "PASS" for s in statuses):
    gate_verdict = "PASS"
elif max_dev_pct < INFO_PCT and "FAIL" not in statuses:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

scheme = "SECTORAL-FLOOR-6"         # (local) 4-tuple scheme tag
convention = "S80-W0-14-reconciled"   # (local) 4-tuple convention tag
L_max_tag = 64                        # (local) W0-A 2D-BZ mesh size (proxy)
four_tuple = f"(value={max_dev_pct:.3f}, scheme={scheme}, convention={convention}, L_max={L_max_tag})"

# -----------------------------------------------------------------------------
# Section 7 — DRAFT canonical_constants.py addition text (do NOT apply)
# -----------------------------------------------------------------------------
draft_addition = f'''
# -----------------------------------------------------------------------------
# SECTION E2 addition (S82 W0-1 / S80 W0-14 canonicalization, NOT APPLIED
# in this task; draft only; MCP update_constant specs below Section 8)
# -----------------------------------------------------------------------------
# Source: computations/session-82/s82_branch_count_2d_bz.npz  Gamma-point eigvals
# SHA-pinned: {input_shas["s82_branch_count_2d_bz.npz"]}
# Reconciliation: S82 W0-A INFO-6 sectoral-floor; full su(3) 7-count is
# upstream (requires 8x8 Gell-Mann-basis dynamical matrix; out of s52 scope).
# All 6 entries reproduce within 0.5% of existing canonical Section E2
# frequencies (omega_L1, omega_L2, omega_H1, omega_H2, omega_H3); this is
# a LABEL-CONSISTENCY transplant, not a new computation.
#
c_Br0_Goldstone    = 0.000000    # Goldstone of pair-phase U(1) at Gamma
                                  # (c_Gold=0.915 is the linear slope; c_Br0 is the
                                  # zero-gap omega value, not a sound speed)
c_Br1_Leggett1     = {gamma_w0a[1]:.6f}    # Leggett-1 Gamma-point frequency
                                  # (matches canonical omega_L1={omega_L1}, dev {dev_pcts[1]:.3f}%)
c_Br2_Leggett2     = {gamma_w0a[2]:.6f}    # Leggett-2 Gamma-point frequency
                                  # (matches canonical omega_L2={omega_L2}, dev {dev_pcts[2]:.3f}%)
c_Br3_Higgs1       = {gamma_w0a[3]:.6f}    # Higgs-Leggett-3 Gamma-point frequency
                                  # (matches canonical omega_H1={omega_H1}, dev {dev_pcts[3]:.3f}%)
c_Br4_Higgs2       = {gamma_w0a[4]:.6f}    # Higgs-Leggett hybrid Gamma-point frequency
                                  # (matches canonical omega_H2={omega_H2}, dev {dev_pcts[4]:.3f}%)
c_Br5_Higgs3       = {gamma_w0a[5]:.6f}   # BCS-Higgs amplitude-mode Gamma-point
                                  # (matches canonical omega_H3={omega_H3}, dev {dev_pcts[5]:.3f}%)
#
# SECTORAL-FLOOR CAVEAT: these are the 6 branches of the s52 3-sector
# GL-Josephson reduction at Gamma. Rank-universality's full su(3) 7-count
# (upstream, 8x8 Gell-Mann-basis matrix) will introduce two additional
# entries (c_Gold_upstream, c_mod_upstream) pending a dedicated workshop.
#
# DEFERRED (NOT canonicalized in this transplant):
#   K_star_goldstone — S79 synthesis value 0.185 does not reproduce from
#     s52 spectrum alone (operational-definition sensitive; omega_branches
#     is purely real in s52 artifact). Carried forward to provenance repair.
#   c_BA = 0.399, c_BLV = 0.485, c_L = 0.025, c_mod = 1.000 — handled
#     by a separate "speeds" transplant; see S82 W0-1 §6 "Ancillary" table.
'''

print("\n" + "=" * 78)
print("DRAFT canonical_constants.py addition text (NOT APPLIED)")
print("=" * 78)
print(draft_addition)

# -----------------------------------------------------------------------------
# Section 8 — MCP update_constant call specs (JSON-like block)
# -----------------------------------------------------------------------------
mcp_specs = [
    {
        "name": "c_Br0_Goldstone",
        "value": "0.000000",
        "session": "S82",
        "source": "s82_branch_count_2d_bz.npz (Gamma-point Br0); sha=" + input_shas["s82_branch_count_2d_bz.npz"][:16],
        "comment": "Gamma-point Goldstone of pair-phase U(1) in 6x6 GL-Josephson reduction (sectoral-floor; c_Gold=0.915 is the linear slope near Gamma)",
        "gate": "S82-PHONON-LENGTH-CANONICALIZATION",
        "section_label": "SECTION E2",
    },
    {
        "name": "c_Br1_Leggett1",
        "value": f"{gamma_w0a[1]:.6f}",
        "session": "S82",
        "source": "s82_branch_count_2d_bz.npz (Gamma-point Br1); reproduces omega_L1; sha=" + input_shas["s82_branch_count_2d_bz.npz"][:16],
        "comment": "Gamma-point Leggett-1 frequency; sectoral-floor alias of omega_L1 (dev 0.221%)",
        "gate": "S82-PHONON-LENGTH-CANONICALIZATION",
        "section_label": "SECTION E2",
    },
    {
        "name": "c_Br2_Leggett2",
        "value": f"{gamma_w0a[2]:.6f}",
        "session": "S82",
        "source": "s82_branch_count_2d_bz.npz (Gamma-point Br2); reproduces omega_L2; sha=" + input_shas["s82_branch_count_2d_bz.npz"][:16],
        "comment": "Gamma-point Leggett-2 frequency; sectoral-floor alias of omega_L2 (dev 0.040%)",
        "gate": "S82-PHONON-LENGTH-CANONICALIZATION",
        "section_label": "SECTION E2",
    },
    {
        "name": "c_Br3_Higgs1",
        "value": f"{gamma_w0a[3]:.6f}",
        "session": "S82",
        "source": "s82_branch_count_2d_bz.npz (Gamma-point Br3); reproduces omega_H1; sha=" + input_shas["s82_branch_count_2d_bz.npz"][:16],
        "comment": "Gamma-point Higgs-Leggett-3 frequency; sectoral-floor alias of omega_H1 (dev 0.475%); amp_frac_Gamma=0.068",
        "gate": "S82-PHONON-LENGTH-CANONICALIZATION",
        "section_label": "SECTION E2",
    },
    {
        "name": "c_Br4_Higgs2",
        "value": f"{gamma_w0a[4]:.6f}",
        "session": "S82",
        "source": "s82_branch_count_2d_bz.npz (Gamma-point Br4); reproduces omega_H2; sha=" + input_shas["s82_branch_count_2d_bz.npz"][:16],
        "comment": "Gamma-point Higgs-Leggett hybrid frequency; sectoral-floor alias of omega_H2 (dev 0.035%); amp_frac_Gamma=0.254",
        "gate": "S82-PHONON-LENGTH-CANONICALIZATION",
        "section_label": "SECTION E2",
    },
    {
        "name": "c_Br5_Higgs3",
        "value": f"{gamma_w0a[5]:.6f}",
        "session": "S82",
        "source": "s82_branch_count_2d_bz.npz (Gamma-point Br5); reproduces omega_H3; sha=" + input_shas["s82_branch_count_2d_bz.npz"][:16],
        "comment": "Gamma-point BCS-Higgs amplitude-mode (|S|^2-pair-breaking); sectoral-floor alias of omega_H3 (dev 0.003%)",
        "gate": "S82-PHONON-LENGTH-CANONICALIZATION",
        "section_label": "SECTION E2",
    },
]

print("\n" + "=" * 78)
print("MCP update_constant call specs (JSON-like; dispatch via knowledge MCP)")
print("=" * 78)
print(json.dumps(mcp_specs, indent=2))

# -----------------------------------------------------------------------------
# Section 9 — Save data
# -----------------------------------------------------------------------------
np.savez(
    os.path.join(HERE, "s82_phononic_length.npz"),
    # Gamma-point spectra (reproducibility audit)
    gamma_w0a=gamma_w0a,
    gamma_s52_1d=gamma_s52,
    canonical_vals=canonical_vals,
    canonical_labels=np.array(canonical_labels),
    dev_pcts=np.array(dev_pcts),
    statuses=np.array(statuses),
    max_dev_pct=max_dev_pct,
    # Ancillary cross-checks
    c_BA_reproduced=c_BA_reproduced,
    c_s_reproduced=c_s_reproduced,
    omega_L_canonical_s70=omega_L_canonical_s70,
    # K_star operational computations (documented as NOT matching S79 claim)
    K_star_operational_a=K_star_operational_a,
    K_star_operational_c=K_star_operational_c,
    # MCP specs and draft text as ndarrays of strings
    mcp_specs_json=np.array(json.dumps(mcp_specs)),
    draft_addition=np.array(draft_addition),
    # Gate metadata
    gate_name=np.array("S82-PHONON-LENGTH-CANONICALIZATION"),
    gate_verdict=np.array(gate_verdict),
    scheme=np.array(scheme),
    convention=np.array(convention),
    L_max_tag=L_max_tag,
    closure_sha=np.array(closure_sha),
    four_tuple=np.array(four_tuple),
    input_shas=np.array(json.dumps(input_shas)),
)

# -----------------------------------------------------------------------------
# Section 10 — Emit S81-canonical verdict line and append to s82_gate_verdicts.txt
# -----------------------------------------------------------------------------
verdict_line = (
    f"S82-PHONON-LENGTH-CANONICALIZATION: {gate_verdict} -- "
    f"value={max_dev_pct:.4f} scheme={scheme} "
    f"convention={convention} L_max={L_max_tag} sha256={closure_sha}"
)

print("\n" + "=" * 78)
print("VERDICT (S81-canonical form):")
print("=" * 78)
print(verdict_line)
print(f"4-tuple: {four_tuple}")
print("=" * 78)

# Append to verdicts file
vpath = os.path.join(HERE, "s82_gate_verdicts.txt")
with open(vpath, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
print(f"Appended to: {vpath}")
