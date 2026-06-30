#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-W1-MKK-SECONDS  —  M_KK^{-1} -> seconds dimensional bridge for the emergent FRW timescale.

Gate: S96-W1-MKK-SECONDS  (session-96, wave 1, gate 3; mack-cosmic-bridge)
Plan: sessions/session-plan/session-96-plan-w1.md  §W1-3
Trigger: [VERIFY]  (verify the M_KK^{-1} -> seconds map against the SI dimensional chain; pin the result)
Classification: GEOMETRIC  (physical-scale normalization of the emergent-time variable)

WHAT THIS DOES
--------------
Closes the `seconds_norm_open=True` piece flagged in S95-W3-1: the structural EH lift
(K -> g_M) is done; only the M_KK^{-1} -> physical-seconds clock-rate normalization was missing.

SUBSTRATE-FIRST FRAMING (phononic-framing.md)
---------------------------------------------
M_KK is NOT a length or a box size — it is the substrate's intrinsic ENERGY scale (the KK
threshold of the SU(3) fiber spectrum). M_KK^{-1} is therefore the substrate's intrinsic
CLOCK TICK in natural units (hbar=c=1). This gate reads off that tick in laboratory SI
seconds via hbar. The "physical time" of the emergent FRW a(t) is NOT an external clock the
substrate evolves against — it is the readout of the substrate's own spectral-reorganization
rate, normalized to seconds. Arrow held:  D_K -> M_KK -> clock tick -> seconds for a(t).

DIMENSIONAL BRIDGE — SUBSTITUTION CHAIN (math-scripts.md §"Double-Check Logic Before Compute")
-----------------------------------------------------------------------------------------------
Claim: t[s] = hbar_SI/(M_KK·GeV_to_J)  AND this is bit-consistent with t[s] = 1/(M_KK·GeV_to_inv_s).

  Step 1 — Definitions (ALL from canonical_constants.py):
    M_KK         = 7.428660036284456e16 GeV        [M_KK alias = M_KK_gravity, S42]
    hbar_SI      = 1.054571817e-34 J·s             [line 43, CODATA 2018]
    eV_SI        = 1.602176634e-19 J/eV            [line 47, exact SI]
    eV_per_GeV   = 1e9                             [line 48]
    GeV_to_J     = eV_SI·eV_per_GeV = 1.602176634e-10 J/GeV   [derived from canonicals; exact]
    GeV_to_inv_s = 1.5193e24 s^{-1}                [line 238; = 1 GeV/hbar in s^{-1}, 5 sig figs]

  Step 2 — Route 1 (hbar / E):
    E_MKK[J]    = M_KK · GeV_to_J
    t_route1[s] = hbar_SI / E_MKK[J] = hbar_SI / (M_KK · GeV_to_J)

  Step 3 — Route 2 (1/(M_KK·GeV_to_inv_s)) and the algebraic identity:
    GeV_to_inv_s ≡ GeV_to_J / hbar_SI            [by definition: 1 GeV/hbar in s^{-1}]
    t_route2[s]  = 1 / (M_KK · GeV_to_inv_s)
                 = hbar_SI / (M_KK · GeV_to_J)   [substitute GeV_to_inv_s]
                 = t_route1[s]                    [ALGEBRAICALLY IDENTICAL up to GeV_to_inv_s 5-sig-fig rounding]

  Step 4 — Direction read-off (from canonical form):
    t[s] = hbar_SI/(M_KK·GeV_to_J) ∝ 1/M_KK  ⇒  LARGER M_KK ⇒ SMALLER physical-time tick.
    With M_KK = 7.43e16 GeV (GUT-scale), M_KK^{-1} ≈ 8.86e-42 s.

  Step 5 — Conclusion + cross-check:
    M_KK_inv_seconds ≈ 8.86e-42 s (the substrate clock tick). Any emergent Δt[M_KK^{-1}] becomes
    Δt[s] = Δt · 8.86e-42. INDEPENDENT prior route (S52 12D-reduction): t_fold = 5.573349e-4 M_KK^{-1}
    "= 1.680e3 s" — VERIFY against it (see CROSS-CHECK note below; this legacy seconds figure is
    found to be a stale units bug, ~47.5 OOM off, and does NOT match the SI chain).

VERDICT RUBRIC (plan §W1-3)
---------------------------
  operator: |t_route1 − t_route2| / t_route1  <=  1e-4   (the two SI routes agree)
  PASS : routes agree rel < 1e-4 and M_KK_inv_seconds promoted to canonical.
  INFO : routes agree only rel ∈ [1e-4, 1e-2], traced to GeV_to_inv_s 5-sig-fig precision.
  FAIL : routes disagree > 1e-2 (a dimensional-chain error or a stale GeV_to_inv_s pin).

ENV: phonon-exflation-sim/.venv312/Scripts/python.exe ; GPU_path=cpu-cap-OMP8 (trivial scalar arithmetic).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")      # (local) trivial scalar arithmetic; cap threads
os.environ.setdefault("MKL_NUM_THREADS", "8")      # (local)

import sys
import json
import math
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: import, never hardcode framework constants) ---
HERE = Path(__file__).resolve().parent                              # (local) computations/session-96
SHARED = HERE.parent / "_shared"                                    # (local) computations/_shared
PROJECT_ROOT = HERE.parent.parent                                   # (local) repo root
sys.path.insert(0, str(SHARED))

from canonical_constants import (   # noqa: E402
    M_KK,            # 7.428660036284456e16 GeV  (alias of M_KK_gravity, S42)
    hbar_SI,         # 1.054571817e-34 J·s       (CODATA 2018)
    eV_SI,           # 1.602176634e-19 J/eV      (exact SI)
    eV_per_GeV,      # 1e9                        (eV per GeV)
    GeV_to_inv_s,    # 1.5193e24 s^{-1}          (1 GeV / hbar; 5 sig figs)
)

# ============================================================
# SECTION 0: Identifiers, paths
# ============================================================
GATE_ID = "S96-W1-MKK-SECONDS"                                      # (local)
SCHEME = "SI-dimensional-chain-hbar-over-E"                         # (local) plan scheme tag
CONVENTION = "natural-units-to-SI-M_KK-energy-to-inverse-time"      # (local) plan convention tag
L_MAX = "N/A"                                                       # (local) no spectral computation

PASS_THRESH = 1e-4                                                  # (local) cross-route agreement (plan strict_PASS_boundary)
INFO_THRESH = 1e-2                                                  # (local) INFO band ceiling (plan INFO_meaning)

SCRIPT_PATH = Path(__file__).resolve()                             # (local)
CANONICAL_PY = SHARED / "canonical_constants.py"                   # (local)
NPZ_PATH = HERE / "s96_w1_mkk_seconds.npz"                         # (local)
PNG_PATH = HERE / "s96_w1_mkk_seconds.png"                         # (local)
VERDICT_TXT = HERE / "s96_gate_verdicts.txt"                       # (local) CANONICAL path per gate-verdicts.md

PUB_PRECISION = 6                                                   # (local) M_KK_inv_seconds promoted to canonical; 6 sig figs


# ============================================================
# SECTION 1: dual-SHA helpers (S84+ schema; mirrors _script_template append_verdict pattern)
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
# ============================================================
def sha256_of(path: Path) -> str:                                  # (local)
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:                               # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                        # (local)
        try:
            rel = str(Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)                                          # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:                             # (local)
    items = sorted(pins.items())                                  # (local)
    h = hashlib.sha256()                                          # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):  # (local)
    try:
        script_bytes = Path(script_path).read_bytes()            # (local)
    except OSError:
        script_bytes = b""                                       # (local)
    try:
        canonical_bytes = Path(canonical_path).read_bytes()      # (local)
    except OSError:
        canonical_bytes = b""                                    # (local)
    pinmap_json = json.dumps(                                     # (local)
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")

    h_audit = hashlib.sha256()                                    # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                   # (local)

    h_content = hashlib.sha256()                                  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                               # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:  # (local)
    """Atomic append (single open('a')) of the dual-SHA verdict to the CANONICAL verdict file."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] SI dimensional bridge; no [SIGN] 3-tuple\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ============================================================
# SECTION 2: the dimensional bridge — TWO SI routes
# ============================================================
print("=" * 76)
print(f"{GATE_ID}  (M_KK^-1 -> seconds dimensional bridge for the emergent FRW timescale)")
print("=" * 76)

# Derived conversion (from canonicals; exact). eV_SI*1e9 == 1.602176634e-10 J/GeV.
GeV_to_J = eV_SI * eV_per_GeV                          # (local) J per GeV, exact; = 1.602176634e-10

print("\n[SEC 2] Inputs (canonical):")
print(f"  M_KK         = {M_KK!r} GeV   (alias M_KK_gravity, S42)")
print(f"  hbar_SI      = {hbar_SI!r} J*s (CODATA 2018)")
print(f"  eV_SI        = {eV_SI!r} J/eV (exact)")
print(f"  eV_per_GeV   = {eV_per_GeV!r}")
print(f"  GeV_to_J     = eV_SI*eV_per_GeV = {GeV_to_J!r} J/GeV (derived, exact)")
print(f"  GeV_to_inv_s = {GeV_to_inv_s!r} s^-1 (canonical pin, 5 sig figs)")

# Route 1:  t = hbar / E,  E = M_KK * GeV_to_J
E_MKK_J = M_KK * GeV_to_J                              # (local) M_KK energy in Joules
t_route1 = hbar_SI / E_MKK_J                           # (local) seconds; hbar/E primary route
# Route 2:  t = 1 / (M_KK * GeV_to_inv_s)
t_route2 = 1.0 / (M_KK * GeV_to_inv_s)                 # (local) seconds; GeV_to_inv_s pin route

# Algebraic-identity witness: GeV_to_inv_s should equal GeV_to_J/hbar_SI
GeV_to_inv_s_identity = GeV_to_J / hbar_SI             # (local) exact value of the canonical pin
pin_rounding_rel = abs(GeV_to_inv_s - GeV_to_inv_s_identity) / GeV_to_inv_s_identity  # (local)

# Cross-route agreement (the gate operator)
rel_disagreement = abs(t_route1 - t_route2) / t_route1  # (local) plan operator value

print("\n[SEC 2] Two SI routes:")
print(f"  E_MKK[J]                = {E_MKK_J!r}")
print(f"  t_route1 = hbar/E       = {t_route1!r} s")
print(f"  t_route2 = 1/(M_KK*GeV_to_inv_s) = {t_route2!r} s")
print(f"  GeV_to_inv_s (exact)    = {GeV_to_inv_s_identity!r}  (pin = {GeV_to_inv_s!r})")
print(f"  pin 5-sig-fig rel error = {pin_rounding_rel:.3e}")
print(f"  |t1-t2|/t1 (operator)   = {rel_disagreement:.6e}   (PASS<= {PASS_THRESH:.0e})")

# Canonical promotion value: the hbar/E primary route (full float64)
M_KK_inv_seconds = t_route1                            # (local) the substrate clock tick in seconds


# ============================================================
# SECTION 3: S52 12D-reduction cross-check (VERIFY)
#   S52 output (s52_12d_reduction_output.txt lines 188-189):
#     "Total time to fold: 5.573349e-04 M_KK^{-1} = 1.680e+03 seconds (physical)"
#   S52 used M_KK (canonical Kerner) = 5.042e17 GeV (line 8), NOT the gravity-route M_KK.
# ============================================================
S52_t_fold_natural = 5.573349e-04                     # (local) S52 t_fold in M_KK^{-1} (natural units)
S52_claimed_seconds = 1.680e3                         # (local) S52 OUTPUT seconds figure (to be verified)
M_KK_kerner_S52 = 5.042e17                            # (local) GeV; the M_KK S52 actually used

# Correct SI conversion of the S52 t_fold, under BOTH M_KK conventions:
S52_t_fold_seconds_grav = S52_t_fold_natural * M_KK_inv_seconds                # (local) gravity-route M_KK
S52_t_fold_seconds_kerner = S52_t_fold_natural / (M_KK_kerner_S52 * GeV_to_inv_s)  # (local) Kerner M_KK
# OOM gap between S52's claimed seconds and the correct SI value (gravity route)
S52_OOM_gap_grav = math.log10(S52_claimed_seconds) - math.log10(S52_t_fold_seconds_grav)  # (local)
# implied M_KK behind the 1.680e3 s figure (diagnostic: physically nonsensical)
S52_implied_MKKinv_seconds = S52_claimed_seconds / S52_t_fold_natural          # (local)
S52_implied_MKK_GeV = 1.0 / (S52_implied_MKKinv_seconds * GeV_to_inv_s)        # (local)

print("\n[SEC 3] S52 12D-reduction cross-check (VERIFY):")
print(f"  S52 t_fold              = {S52_t_fold_natural!r} M_KK^-1 (natural)")
print(f"  S52 claimed seconds     = {S52_claimed_seconds!r} s")
print(f"  correct SI (grav M_KK)  = {S52_t_fold_seconds_grav!r} s")
print(f"  correct SI (Kerner M_KK)= {S52_t_fold_seconds_kerner!r} s")
print(f"  OOM gap (S52 vs SI grav)= {S52_OOM_gap_grav:.3f}  <-- S52 seconds figure is a STALE UNITS BUG")
print(f"  implied M_KK^-1 (s)     = {S52_implied_MKKinv_seconds!r}  -> implied M_KK = {S52_implied_MKK_GeV!r} GeV (nonsensical)")

# Cross-check VERDICT logic: the cross-check passes iff S52 seconds matches the SI value to <1 OOM.
S52_crosscheck_pass = abs(S52_OOM_gap_grav) < 1.0     # (local) False (it is ~47.5 OOM off)


# ============================================================
# SECTION 4: VERDICT (gate operator: cross-ROUTE agreement, NOT the S52 cross-check)
# ============================================================
if rel_disagreement <= PASS_THRESH:
    verdict = "PASS"                                  # (local)
elif rel_disagreement <= INFO_THRESH:
    verdict = "INFO"                                  # (local)
else:
    verdict = "FAIL"                                  # (local)

# 6-sig-fig published form of the canonical value
M_KK_inv_seconds_6sf = float(f"{M_KK_inv_seconds:.{PUB_PRECISION - 1}e}")  # (local) 8.86044e-42

value_str = (
    f"M_KK_inv_seconds={M_KK_inv_seconds:.6e}_s;rel_routes={rel_disagreement:.3e};"
    f"PASS_le_{PASS_THRESH:.0e};S52_crosscheck=FAIL_{S52_OOM_gap_grav:.1f}OOM_legacy_units_bug"
)  # (local)

print("\n[SEC 4] VERDICT")
print(f"  rel_routes={rel_disagreement:.6e}  threshold<= {PASS_THRESH:.0e}  -> {verdict}")
print(f"  M_KK_inv_seconds (6sf) = {M_KK_inv_seconds_6sf!r} s")
print(f"  S52 cross-check PASS?  = {S52_crosscheck_pass} (legacy 1.680e3 s is ~{S52_OOM_gap_grav:.1f} OOM off)")


# ============================================================
# SECTION 5: persist npz + png
# ============================================================
np.savez(
    NPZ_PATH,
    # canonical inputs
    M_KK_GeV=float(M_KK),
    hbar_SI=float(hbar_SI),
    eV_SI=float(eV_SI),
    eV_per_GeV=float(eV_per_GeV),
    GeV_to_J=float(GeV_to_J),
    GeV_to_inv_s_pin=float(GeV_to_inv_s),
    GeV_to_inv_s_exact=float(GeV_to_inv_s_identity),
    pin_rounding_rel=float(pin_rounding_rel),
    # primary result (full float64) + routes
    E_MKK_J=float(E_MKK_J),
    t_route1_s=float(t_route1),
    t_route2_s=float(t_route2),
    rel_disagreement=float(rel_disagreement),
    M_KK_inv_seconds=float(M_KK_inv_seconds),
    M_KK_inv_seconds_6sf=float(M_KK_inv_seconds_6sf),
    PASS_THRESH=float(PASS_THRESH),
    INFO_THRESH=float(INFO_THRESH),
    verdict=str(verdict),
    # S52 cross-check
    S52_t_fold_natural=float(S52_t_fold_natural),
    S52_claimed_seconds=float(S52_claimed_seconds),
    M_KK_kerner_S52=float(M_KK_kerner_S52),
    S52_t_fold_seconds_grav=float(S52_t_fold_seconds_grav),
    S52_t_fold_seconds_kerner=float(S52_t_fold_seconds_kerner),
    S52_OOM_gap_grav=float(S52_OOM_gap_grav),
    S52_implied_MKK_GeV=float(S52_implied_MKK_GeV),
    S52_crosscheck_pass=bool(S52_crosscheck_pass),
)
print(f"\n[SEC 5] npz -> {NPZ_PATH}")

# Plot: the two SI routes (agree) and the S52 cross-check on a log-time axis.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))

# Left: the two routes on a tight linear axis (they overlap to 5 sig figs)
routes = [t_route1, t_route2]                          # (local)
labels = ["route 1\nℏ/E", "route 2\n1/(M_KK·GeV→s⁻¹)"]  # (local)
ax1.bar([0, 1], routes, width=0.5, color=["#2c7fb8", "#7fcdbb"])
ax1.set_xticks([0, 1])
ax1.set_xticklabels(labels, fontsize=9)
ax1.set_ylabel("M_KK$^{-1}$  [s]")
ax1.set_title(f"Two SI routes AGREE (rel = {rel_disagreement:.2e} < {PASS_THRESH:.0e})\n"
              f"M_KK$^{{-1}}$ = {M_KK_inv_seconds_6sf:.5e} s   [{verdict}]", fontsize=9)
ax1.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
for i, v in enumerate(routes):
    ax1.text(i, v, f"{v:.5e}", ha="center", va="bottom", fontsize=7.5)

# Right: log10(seconds) — S52 claimed vs correct SI (shows the ~47.5 OOM legacy bug)
log_vals = [
    math.log10(M_KK_inv_seconds),
    math.log10(S52_t_fold_seconds_grav),
    math.log10(S52_claimed_seconds),
]                                                      # (local)
log_labels = ["M_KK$^{-1}$\n(this gate)", "S52 t_fold\nSI-correct", "S52 t_fold\nCLAIMED (bug)"]  # (local)
colors = ["#2c7fb8", "#31a354", "#de2d26"]            # (local)
ax2.bar([0, 1, 2], log_vals, width=0.55, color=colors)
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(log_labels, fontsize=8.5)
ax2.set_ylabel(r"$\log_{10}$( time / s )")
ax2.set_title(f"S52 cross-check: claimed 1.680e3 s is\n~{S52_OOM_gap_grav:.1f} OOM off (stale units bug)",
              fontsize=9)
ax2.axhline(0.0, color="k", lw=0.6, ls=":")
for i, v in enumerate(log_vals):
    ax2.text(i, v, f"{v:.1f}", ha="center",
             va="bottom" if v >= 0 else "top", fontsize=8)

fig.suptitle("S96-W1-MKK-SECONDS — substrate clock tick M_KK$^{-1}$ in SI seconds "
             "(D_K → M_KK → tick → a(t) seconds)", fontsize=10)
fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig(PNG_PATH, dpi=130)
plt.close(fig)
print(f"[SEC 5] png -> {PNG_PATH}")


# ============================================================
# SECTION 6: dual-SHA + verdict emission
# ============================================================
INPUT_FILES = [SCRIPT_PATH, CANONICAL_PY]             # (local) audit_sha256_inputs: script, canonical, pinmap
pins = log_input_pins(INPUT_FILES)                    # (local)
clos = closure_hash(pins)                             # (local) closure over input pin map
audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PY, pins)  # (local)

print(f"\n[SEC 6] closure_hash(pins) = {clos[:16]}...")
print(f"        audit_sha256       = {audit_sha[:16]}...  (script+canonical+pinmap)")
print(f"        content_sha256     = {content_sha[:16]}...  (script only)")

# 4-tuple output tag (final non-verdict line)
print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

append_verdict(verdict, value_str, audit_sha, content_sha)
print(f"\n[SEC 6] verdict appended -> {VERDICT_TXT}")
print(f"        {GATE_ID}: {verdict}")

sys.exit(0)   # exit code reflects SCRIPT HEALTH, not the scientific verdict (math-scripts.md)
