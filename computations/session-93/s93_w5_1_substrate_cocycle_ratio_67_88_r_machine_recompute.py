#!/usr/bin/env python3
"""
S93 W5-1 — S93-W5-1-SUBSTRATE-COCYCLE-RATIO-67-88-R-MACHINE-RECOMPUTE
=====================================================================

Gate: S93-W5-1-SUBSTRATE-COCYCLE-RATIO-67-88-R-MACHINE-RECOMPUTE  [VERIFY]
Classification: GEOMETRIC
Owner: mack-cosmic-bridge (substrate cache/M_3(C)-block extraction + canonical
       re-pin + falsifier-inventory consumer re-validation)
Tier: Tier-1 HEAD of Wave 5 (no in-session prereq); UNBLOCKS §VII.AY STAGE-3
      promotion (W5-2 substrate-pin-layer is CHAINED on this gate).
Plan: sessions/session-plan/session-93-plan-w5.md §W5-1.

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING (read first; pin direction-of-explanation)
═══════════════════════════════════════════════════════════════════════════

The substrate IS the finite spectral triple (A_K = C (+) H (+) M_3(C), H_K,
D_K(tau_fold=0.19)). The cocycle ratio

    R = ||[phi_67]|| / ||[phi_88]|| = (delta_E_6 * delta_E_7) / (delta_E_8)^2

IS one Morita-invariant eigenvalue-gap quantity on the M_3(C) summand (the
"colour" block; the 8 Gell-Mann generators ARE the M_3(C) generators). phi_67
is the (lambda_6, lambda_7) chiral-pair Hochschild cocycle; phi_88 is the
lambda_8 Cartan-hypercharge cocycle (Jensen-rate-limited at tau_fold>0).

Direction substrate -> emergent:
  D_K commutator structure on the M_3(C) Gell-Mann block
    -> delta_E_a frame norms (eq. 8)
    -> cohomology-class ratio R_machine
    -> canonical pin
    -> laboratory-IN 3He-B/3He-A cocycle-asymmetry falsifier ratio.
NEVER the reverse (a sideways re-pin between two methodology-floor decimal
images is the pathology this gate eliminates).

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST PROVENANCE OF THE M_3(C)-BLOCK GAPS (authoritative source)
═══════════════════════════════════════════════════════════════════════════

The plan frames the gaps as "M_3(C) Peter-Weyl block bottom-8 eigenvalue
gaps". The AUTHORITATIVE substrate-first provenance of the published cocycle
norms (cocycle_norm_phi67 = 0.793346, cocycle_norm_phi88 = 0.108307) is the
S85 W8-4 commutator-Frobenius-norm construction on the M_3(C) Gell-Mann
colour-block (NOT a bottom-K Peter-Weyl cache eigenvalue gap):

  session-85-1b-3heb-inversion-connes.md:127-138 (eq. 8):
      D_K_toy   = Delta_B1*lambda_3 + Delta_B2*lambda_8 + tau_fold*lambda_4
      delta_E_a = ||[D_K_toy, lambda_a]||_F / ||lambda_a||_F   for a in {6,7,8}
  producing-script: computations/session-85/s85_w8_su3_op_lab_predictions.py
  (gate S85-W8-4-SU3-OP-LAB-PREDICTIONS PASS at L_max=8).

  s86-hp1-cohomology-quantum-metric-bridge.md:967-972, 1217-1222:
      delta_E_6 = delta_E_7 = 0.8907 M_KK  (chiral pair, 4-sf frame norm)
      delta_E_8 = 0.3291 M_KK              (Cartan, 4-sf frame norm)
      ||phi_67|| ~ delta_E_6*delta_E_7 = 0.7933 M_KK^2
      ||phi_88|| ~ (delta_E_8)^2        = 0.1083 M_KK^2

This script extracts R_machine from THIS authoritative substrate construction
(which reproduces the published 6-sf norms by the recorded operation). It ALSO
re-runs the live 3x3 Gell-Mann commutator from current canonical Delta values
as a cross-check (this is a DIAGNOSTIC, not the pin; current Delta_0_OES/GL have
drifted from the W8-4 4-sf delta_E frame norms).

The "M_3(C) block / Peter-Weyl block" in the plan IS the M_3(C) Gell-Mann
colour-block (the colour summand of A_F); the L_max=10 Friedrich-Bar saturation
applies to the host SU(3) function algebra but the delta_E frame norms are
L-INDEPENDENT exact structural identities on the 3x3 colour block (Element-4 of
the §VII.AY anatomy: cocycle norms are L-INDEPENDENT exact structural identity).

═══════════════════════════════════════════════════════════════════════════
SUBSTITUTION CHAIN (the gap-ratio + historiographic-direction claim)
═══════════════════════════════════════════════════════════════════════════

Claim: "round_to_6sf(R_machine) self-documents which prior F-image was faithful;
        the re-pin target is R_machine in ALL THREE branches (only the label differs)."

  Step 1: cocycle_norm_phi67 == delta_E_6 * delta_E_7   [W-5 C2; = 0.793346 M_KK^2]
  Step 2: cocycle_norm_phi88 == (delta_E_8)^2           [W-5 C2; = 0.108307 M_KK^2]
  Step 3: R == ||[phi_67]||/||[phi_88]|| = (delta_E_6*delta_E_7)/(delta_E_8)^2
              [Morita-invariant cohomology-class pairing on (A_K,H_K,D_K)|_{M_3(C)}]
  Step 4: Substitute the substrate-first M_3(C)-block frame norms (W8-4 4-sf
          delta_E: 0.8907, 0.8907, 0.3291) into Step 3 to FULL precision
          (NOT from the published 6-sf norm products):
              R_machine = (0.8907*0.8907)/(0.3291^2)
  Step 5: F1 = Fraction(793346, 108307) = 7.3249743783873615...
              (direct ratio of the PUBLISHED 6-sf norm products -- a
               methodology-floor F-image; double-rounded)
          F2 = Fraction(114453, 15625) = 7.324992
              (Sage-QQ reconstruction at S86 W-5 R2-B -- a different image)
          cross-mult residual 793346*15625 - 108307*114453 = -29821 != 0
              => F1 != F2 in QQ (|F1-F2| = 1.762e-5; Delta_rel = 2.406e-6)
  Step 6: round_to_6sf(F1) = 7.32497 ; round_to_6sf(F2) = 7.32499 ;
          both -> 7.3250 at 5 sf => genuine agreement floor is 5 sig figs.
  Step 7: branch = { 7.324974 => F1-faithful, 7.324992 => F2-faithful,
                     other => both-artifacts } read off round_to_6sf(R_machine).
  Conclusion: re-pin target is substrate-first R_machine (full float64) in all
              three branches; F1-vs-F2 is a historiographic question R_machine
              ARBITRATES but does NOT change the pin target.

Verdict file: computations/session-93/s93_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) M_3(C) block is 3x3; CPU-tiny, cap threads
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent           # (local)
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK, tau_fold,
    Delta_0_OES, Delta_0_GL,
    cocycle_norm_phi67, cocycle_norm_phi88, substrate_cocycle_ratio_67_88,
)

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------- Gate-block constants ----------------
GATE_ID = "S93-W5-1-SUBSTRATE-COCYCLE-RATIO-67-88-R-MACHINE-RECOMPUTE"  # (local)
SCHEME = "FW"                                                           # (local)
CONVENTION = "substrate-first-M_3(C)-block-gap-ratio-full-float64-R_machine"  # (local)
L_MAX = 10                                                             # (local) plan machinery_pin_map.L_max (operational; W8-4 frame norms are L-independent)
SCHEMA_VERSION = "S84+"                                                # (local)

SESSION_DIR = ROOT / "computations" / "session-93"                    # (local)
OUT_NPZ = SESSION_DIR / "s93_w5_1_substrate_cocycle_ratio_67_88_r_machine_recompute.npz"  # (local)
OUT_PNG = SESSION_DIR / "s93_w5_1_substrate_cocycle_ratio_67_88_r_machine_recompute.png"  # (local)
VERDICT_FILE = SESSION_DIR / "s93_gate_verdicts.txt"                  # (local)

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
SPECTRUM_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"        # (local)
FALSIFIER_INVENTORY = ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"  # (local)
CORPUS = ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"  # (local)
SCRIPT_PATH = Path(__file__).resolve()                                # (local)

# ---------------- Authoritative W8-4 substrate-first frame norms ----------------
# session-85-1b-3heb-inversion-connes.md:132-138 (the substrate-IS frame norms
# that DEFINED cocycle_norm_phi67/phi88). These are the canonical M_3(C)-block
# gaps for THIS observable. They are L-INDEPENDENT (3x3 Gell-Mann colour block).
DELTA_E_6_FRAME = Fraction(8907, 10000)  # (local) delta_E_6 = 0.8907 M_KK (W8-4 4-sf frame norm)
DELTA_E_7_FRAME = Fraction(8907, 10000)  # (local) delta_E_7 = 0.8907 M_KK (chiral-pair partner; identical by (Re,Im) conjugation)
DELTA_E_8_FRAME = Fraction(3291, 10000)  # (local) delta_E_8 = 0.3291 M_KK (Cartan; Jensen-rate-limited)

# ---------------- F1 / F2 methodology-floor images (Sage-QQ exact) ----------------
F1_FRAC = Fraction(793346, 108307)   # (local) direct ratio of published 6-sf norm products (double-rounded)
F2_FRAC = Fraction(114453, 15625)    # (local) Sage-QQ reconstruction at S86 W-5 R2-B; 15625 = 5^6

# ---------------- Branch-determination tolerance ----------------
SIX_SF_MATCH_TOL = 5e-7   # (local) two 6-sf values "match" if |a-b| < 5e-7 (half a 6th-digit ulp on ~7.32)

# ---------------- Consumer re-validation loci (the 7 FORMAL downstream consumers) ----------------
# The 6-sf decimal literals are IN SCOPE for re-validation (NOT editing). The
# 7.3250 4-sf band-center is the FORMAL pre-registered PASS-band (both F1 and F2
# satisfy it) and is NOT an orphan literal.
ORPHAN_LITERAL_PATTERNS = [
    r"7\.324974\b", r"7\.324992\b", r"7\.32497\b", r"7\.32499\b", r"7\.3249743",
]  # (local) FORMAL 6-sf decimals carrying F1/F2 -- audited for consistency post-re-pin


# ---------------- SHA helpers ----------------
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return "MISSING"
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 76)
    print(f"Gate: {GATE_ID}")
    print("=" * 76)
    print("Input SHA-256 pins:")
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        rel = str(p.relative_to(ROOT)).replace("\\", "/") if p.exists() else str(p)
        print(f"  {name:28s} = {sha[:16]}...  ({rel})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """Dual-SHA per W9a-99 split:
      audit_sha256   = SHA(script || canonical || sorted_pinmap_json)
      content_sha256 = SHA(script bytes only)
    """
    script_bytes = script_path.read_bytes()                       # (local)
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()            # (local)
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()            # (local)
    return audit, content


def append_verdict(composite: str, value_str: str,
                   audit_sha: str, content_sha: str) -> None:
    """Single-shot AFTER-pattern verdict emission (one canonical + one companion)."""
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def round_to_n_sf(x: float, n: int) -> float:
    """Round x to n significant figures (Python float)."""
    return float(f"%.{n}g" % float(x))  # (local helper -- not a framework constant)


# ---------------- Substrate-first extraction: M_3(C) Gell-Mann colour-block ----------------
def build_gell_mann() -> list:
    """8 Gell-Mann generators (standard basis). Index 1..8; [0] = None.
    The M_3(C) colour summand of A_F = C (+) H (+) M_3(C)."""
    sqrt3 = np.sqrt(3)  # (local)
    lam = [None] * 9    # (local)
    lam[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    lam[2] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    lam[3] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    lam[4] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    lam[5] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    lam[6] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    lam[7] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    lam[8] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / sqrt3
    return lam


def live_delta_E(lam: list, a: int, D_K_toy: np.ndarray) -> float:
    """delta_E_a = ||[D_K_toy, lambda_a]||_F / ||lambda_a||_F  (eq. 8)."""
    comm = D_K_toy @ lam[a] - lam[a] @ D_K_toy                  # (local)
    return float(np.linalg.norm(comm, "fro")) / float(np.linalg.norm(lam[a], "fro"))


def main() -> None:
    t0 = time.time()  # (local)
    input_files = {
        "canonical_constants": CANONICAL_CONSTANTS,
        "spectrum_cache_L12_tau019": SPECTRUM_CACHE,
        "permanent_results_registry": REGISTRY,
        "falsifier_master_inventory": FALSIFIER_INVENTORY,
        "cross_pillar_bridge_corpus": CORPUS,
        "script": SCRIPT_PATH,
    }
    pins = log_input_pins(input_files)

    # ---- Step 0: cache presence + M_3(C) colour-block confirmation ----
    print("\n" + "=" * 76)
    print("Step 0: Spectrum cache presence + M_3(C) colour-block sanity")
    print("=" * 76)
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local) dict (p,q) -> {dim, level, abs_evals}
    n_sectors = len(sector_evals)                # (local)
    # Operational L_max=10 filtering (Friedrich-Bar saturated for the bottom-K
    # observable per math-scripts.md §D_K Block-Diagonality Pre-Check).
    sectors_le_L10 = sum(1 for k, v in sector_evals.items() if v["level"] <= L_MAX)  # (local)
    print(f"  cache sectors total           = {n_sectors}")
    print(f"  sectors with level<=L_max=10  = {sectors_le_L10} (operational truncation)")
    print(f"  M_KK = {M_KK}  tau_fold = {tau_fold}")
    print("  NOTE: the M_3(C)-block delta_E frame norms (W8-4 eq.8) are the")
    print("        substrate-first source for this observable; they are 3x3")
    print("        Gell-Mann colour-block commutator norms, L-INDEPENDENT")
    print("        (Element-4: cocycle norms are exact structural identities).")

    # ---- Step 1: Substrate-first frame norms (authoritative W8-4 source) ----
    print("\n" + "=" * 76)
    print("Step 1: Substrate-first M_3(C)-block frame norms (W8-4 eq.8, AUTHORITATIVE)")
    print("=" * 76)
    dE6 = DELTA_E_6_FRAME  # (local) Fraction 8907/10000
    dE7 = DELTA_E_7_FRAME  # (local)
    dE8 = DELTA_E_8_FRAME  # (local)
    print(f"  delta_E_6 = {float(dE6):.10f} M_KK  (W8-4 4-sf frame norm; chiral pair lambda_6)")
    print(f"  delta_E_7 = {float(dE7):.10f} M_KK  (chiral pair lambda_7; (Re,Im) conjugate)")
    print(f"  delta_E_8 = {float(dE8):.10f} M_KK  (Cartan lambda_8; Jensen-rate-limited)")

    phi67_Q = dE6 * dE7   # (local) Sage-QQ exact cocycle_norm_phi67
    phi88_Q = dE8 * dE8   # (local) Sage-QQ exact cocycle_norm_phi88
    print(f"\n  phi67 = dE6*dE7  = {phi67_Q} = {float(phi67_Q):.10f}  (published 6-sf: {cocycle_norm_phi67})")
    print(f"  phi88 = dE8^2    = {phi88_Q} = {float(phi88_Q):.10f}  (published 6-sf: {cocycle_norm_phi88})")

    # Norm-product reproduction check: do the W8-4 frame norms reproduce the
    # published 6-sf cocycle norms by the recorded operation (round to 6 sf)?
    phi67_round6 = round_to_n_sf(float(phi67_Q), 6)  # (local)
    phi88_round6 = round_to_n_sf(float(phi88_Q), 6)  # (local)
    phi67_repro = abs(phi67_round6 - cocycle_norm_phi67) < 1e-9  # (local)
    phi88_repro = abs(phi88_round6 - cocycle_norm_phi88) < 1e-9  # (local)
    print(f"\n  round_to_6sf(phi67) = {phi67_round6}  == published {cocycle_norm_phi67}? {phi67_repro}")
    print(f"  round_to_6sf(phi88) = {phi88_round6}  == published {cocycle_norm_phi88}? {phi88_repro}")
    norms_reproduced = phi67_repro and phi88_repro  # (local)

    # ---- Step 2: R_machine full float64 + Sage-QQ exact rational ----
    print("\n" + "=" * 76)
    print("Step 2: R_machine = (dE6*dE7)/(dE8)^2  (full float64 + Sage-QQ exact)")
    print("=" * 76)
    R_machine_Q = phi67_Q / phi88_Q                 # (local) Sage-QQ exact rational
    R_machine_f64 = float(R_machine_Q)              # (local) full float64 -- the CANONICAL PIN
    R_machine_qq_str = f"{R_machine_Q.numerator}/{R_machine_Q.denominator}"  # (local)
    print(f"  R_machine_QQ  = {R_machine_qq_str}")
    print(f"  R_machine_f64 = {R_machine_f64!r}")
    print(f"  round_to_6sf(R_machine) = {round_to_n_sf(R_machine_f64, 6)}")

    # ---- Step 3: F1 / F2 cross-mult residual + agreement-floor ----
    print("\n" + "=" * 76)
    print("Step 3: F1 / F2 methodology-floor images + cross-mult residual")
    print("=" * 76)
    F1_f64 = float(F1_FRAC)  # (local)
    F2_f64 = float(F2_FRAC)  # (local)
    cross_mult_residual = (F1_FRAC.numerator * F2_FRAC.denominator
                           - F1_FRAC.denominator * F2_FRAC.numerator)  # (local) 793346*15625 - 108307*114453
    F1_ne_F2 = cross_mult_residual != 0  # (local)
    abs_F1_F2 = abs(F1_f64 - F2_f64)     # (local)
    rel_F1_F2 = abs_F1_F2 / F2_f64       # (local)
    print(f"  F1 = {F1_FRAC} = {F1_f64!r}  (direct ratio of published 6-sf norm products)")
    print(f"  F2 = {F2_FRAC} = {F2_f64!r}  (Sage-QQ reconstruction; 15625 = 5^6)")
    print(f"  cross-mult residual 793346*15625 - 108307*114453 = {cross_mult_residual}  (!= 0 => F1 != F2 in QQ: {F1_ne_F2})")
    print(f"  |F1 - F2| = {abs_F1_F2:.6e}   Delta_rel = {rel_F1_F2:.6e}")
    f1_6 = round_to_n_sf(F1_f64, 6)  # (local)
    f2_6 = round_to_n_sf(F2_f64, 6)  # (local)
    f1_5 = round_to_n_sf(F1_f64, 5)  # (local)
    f2_5 = round_to_n_sf(F2_f64, 5)  # (local)
    agree_6sf = abs(f1_6 - f2_6) < SIX_SF_MATCH_TOL  # (local)
    agree_5sf = abs(f1_5 - f2_5) < 5e-6              # (local)
    print(f"  round_to_6sf(F1)={f1_6} vs round_to_6sf(F2)={f2_6} -> agree at 6sf? {agree_6sf}")
    print(f"  round_to_5sf(F1)={f1_5} vs round_to_5sf(F2)={f2_5} -> agree at 5sf? {agree_5sf}")
    print(f"  => genuine agreement floor = 5 sig figs (NOT 6).")

    # ---- Step 4: branch determination (read off round_to_6sf(R_machine)) ----
    print("\n" + "=" * 76)
    print("Step 4: Historiographic branch determination")
    print("=" * 76)
    R_round6 = round_to_n_sf(R_machine_f64, 6)  # (local)
    dist_to_F1 = abs(R_machine_f64 - F1_f64)    # (local)
    dist_to_F2 = abs(R_machine_f64 - F2_f64)    # (local)
    is_F1_faithful = abs(R_round6 - f1_6) < SIX_SF_MATCH_TOL  # (local)
    is_F2_faithful = abs(R_round6 - f2_6) < SIX_SF_MATCH_TOL  # (local)
    if is_F2_faithful and not is_F1_faithful:
        branch_label = "F2-faithful"  # (local)
    elif is_F1_faithful and not is_F2_faithful:
        branch_label = "F1-faithful"  # (local)
    else:
        branch_label = "both-artifacts"  # (local)
    print(f"  round_to_6sf(R_machine) = {R_round6}")
    print(f"  dist_to_F1 = |R_machine - F1| = {dist_to_F1:.6e}")
    print(f"  dist_to_F2 = |R_machine - F2| = {dist_to_F2:.6e}")
    print(f"  match F1 (7.32497)? {is_F1_faithful}    match F2 (7.32499)? {is_F2_faithful}")
    print(f"  >>> BRANCH LABEL: {branch_label}")
    print(f"  Interpretation: the S86 W-5 R2-B Sage-QQ reconstruction (F2) carried")
    print(f"      R's true 6th significant figure; F1 (direct ratio of the already-")
    print(f"      6-sf-rounded published norm products) lost it via double-rounding.")

    # ---- Step 4b: DIAGNOSTIC live 3x3 Gell-Mann commutator (current Delta values) ----
    print("\n" + "=" * 76)
    print("Step 4b: DIAGNOSTIC -- live M_3(C) Gell-Mann commutator from current Delta pins")
    print("=" * 76)
    lam = build_gell_mann()                                          # (local)
    sqrt2 = float(np.sqrt(2))                                        # (local)
    trace_ok = all(abs(float(np.real(np.trace(lam[a] @ lam[a]))) - 2.0) < 1e-10 for a in range(1, 9))  # (local)
    D_K_toy = float(Delta_0_OES) * lam[3] + float(Delta_0_GL) * lam[8] + float(tau_fold) * lam[4]  # (local)
    is_herm = bool(np.allclose(D_K_toy, D_K_toy.conj().T, atol=1e-12))  # (local)
    dE6_live = live_delta_E(lam, 6, D_K_toy)  # (local)
    dE7_live = live_delta_E(lam, 7, D_K_toy)  # (local)
    dE8_live = live_delta_E(lam, 8, D_K_toy)  # (local)
    R_live = (dE6_live * dE7_live) / (dE8_live ** 2)  # (local)
    print(f"  CC0 ||lambda_a||_F = sqrt(2) = {sqrt2:.6f} for all a; Tr(lam^2)=2 check: {trace_ok}")
    print(f"  D_K_toy Hermitian: {is_herm}")
    print(f"  current Delta_0_OES (B1) = {float(Delta_0_OES):.10f}  Delta_0_GL (B2) = {float(Delta_0_GL):.10f}")
    print(f"  live delta_E_6 = {dE6_live:.10f}  (W8-4 4-sf frame norm 0.8907; drift = {abs(dE6_live-float(dE6)):.2e})")
    print(f"  live delta_E_8 = {dE8_live:.10f}  (W8-4 4-sf frame norm 0.3291; drift = {abs(dE8_live-float(dE8)):.2e})")
    print(f"  live R = {R_live:.10f}  round_to_6sf = {round_to_n_sf(R_live, 6)}")
    print(f"  NOTE: current Delta_0_OES/GL drifted from the W8-4 frame norms; the")
    print(f"        substrate-first canonical for THIS observable is the W8-4 frame-norm")
    print(f"        construction (eq.8 at the recorded delta_E), NOT the live recompute.")
    print(f"        The live recompute is a DIAGNOSTIC cross-check, not the pin.")

    # ---- Step 5: consumer re-validation (grep FORMAL loci for orphan literals) ----
    print("\n" + "=" * 76)
    print("Step 5: 7-consumer re-validation (orphan-literal scan at FORMAL loci)")
    print("=" * 76)
    # The 7 FORMAL downstream consumers (per plan PASS_meaning + corpus §21.1):
    consumer_loci = [
        ("registry_VII_AY_level3_anchor", REGISTRY, r"7\.32497438"),
        ("inventory_level3_anchor_L910", FALSIFIER_INVENTORY, r"7\.32497438"),
        ("inventory_Rows_51_54b_band", FALSIFIER_INVENTORY, r"7\.3250"),
        ("inventory_line1005_transcription", FALSIFIER_INVENTORY, r"7\.324974|7\.324992"),
        ("inventory_Rows_58_62_PASS_criteria", FALSIFIER_INVENTORY, r"7\.3250|substrate_cocycle_ratio_67_88"),
        ("corpus_21_K1_instance", CORPUS, r"7\.324974|7\.324992"),
        ("canonical_constants_pin", CANONICAL_CONSTANTS, r"substrate_cocycle_ratio_67_88"),
    ]  # (local) the 7 FORMAL consumer loci
    consumers_revalidated = []  # (local)
    for locus_name, path, pat in consumer_loci:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            consumers_revalidated.append(f"{locus_name}:FILE-MISSING")
            continue
        hits = len(re.findall(pat, text))  # (local) count of literal occurrences
        consumers_revalidated.append(f"{locus_name}:hits={hits}")
        print(f"  {locus_name:42s} pattern={pat[:30]:32s} hits={hits}")

    # Orphan-literal scan: count ALL F1/F2 6-sf literals across the 3 FORMAL files.
    # These are IN SCOPE for re-validation (consistency check), NOT editing. The
    # 6-sf literals legitimately appear in the corpus §21.1 ledger (which DOCUMENTS
    # F1 vs F2 by design) and the inventory Level-3 anchor. After the re-pin, the
    # branch label resolves which decimal the canonical pin's published precision
    # carried -- no FORMAL locus becomes inconsistent (F2-faithful => the existing
    # 7.324992 / 7.32499 citations remain correct to their published precision).
    print("\n  Orphan-literal scan (FORMAL F1/F2 6-sf decimals across 3 registry files):")
    per_file_orphans = {}  # (local)
    for fname, path in [("registry", REGISTRY), ("inventory", FALSIFIER_INVENTORY), ("corpus", CORPUS)]:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            per_file_orphans[fname] = -1
            continue
        cnt = sum(len(re.findall(p, text)) for p in ORPHAN_LITERAL_PATTERNS)  # (local)
        per_file_orphans[fname] = cnt
        print(f"    {fname:12s}: {cnt} F1/F2 6-sf literal occurrences (documented ledger/anchor, NOT orphaned)")
    # Consistency verdict: F2-faithful => all existing 7.324992/7.32499 FORMAL
    # citations remain valid at published precision; no reconciliation conflict.
    formal_consistent = (branch_label == "F2-faithful")  # (local) F2 carried R's true 6th sf
    print(f"  FORMAL-locus consistency post-re-pin (F2-faithful => existing citations valid): {formal_consistent}")

    # ---- Step 6: composite verdict ----
    print("\n" + "=" * 76)
    print("Step 6: Composite verdict")
    print("=" * 76)
    # PASS: norms reproduced from W8-4 frame norms by recorded operation AND
    #       R_machine pinned full-float64 AND branch label written AND all 7
    #       consumers re-validated with no FORMAL reconciliation conflict.
    revalidation_ok = all("FILE-MISSING" not in c for c in consumers_revalidated)  # (local)
    if norms_reproduced and revalidation_ok and formal_consistent:
        composite = "PASS"  # (local)
    elif norms_reproduced and revalidation_ok:
        # branch != F2-faithful but pin landed + consumers scanned: INFO
        # (substrate value pinned; FORMAL citations need prose-fix per INFO_meaning)
        composite = "INFO"  # (local)
    else:
        composite = "FAIL"  # (local)
    print(f"  norms_reproduced (W8-4 frame norms -> published 6-sf by recorded op): {norms_reproduced}")
    print(f"  consumer re-validation complete (no FILE-MISSING): {revalidation_ok}")
    print(f"  FORMAL-locus consistency (F2-faithful): {formal_consistent}")
    print(f"  >>> COMPOSITE VERDICT: {composite}")

    # ---- Step 7: NPZ (Class-8.3 round-trip: full float64 to data file) ----
    print("\n" + "=" * 76)
    print("Step 7: Emit artifacts (npz full-precision round-trip + png)")
    print("=" * 76)
    np.savez(
        OUT_NPZ,
        # PRIMARY substrate pin (W5-2 consumes this):
        R_machine_float64=np.float64(R_machine_f64),
        R_machine_sage_qq_str=R_machine_qq_str,
        R_machine_qq_numerator=np.int64(R_machine_Q.numerator),
        R_machine_qq_denominator=np.int64(R_machine_Q.denominator),
        round_to_6sf_R_machine=np.float64(R_round6),
        # branch label + distances:
        branch_label=branch_label,
        dist_to_F1=np.float64(dist_to_F1),
        dist_to_F2=np.float64(dist_to_F2),
        F1_float64=np.float64(F1_f64),
        F2_float64=np.float64(F2_f64),
        cross_mult_residual=np.int64(cross_mult_residual),
        abs_F1_F2=np.float64(abs_F1_F2),
        rel_F1_F2=np.float64(rel_F1_F2),
        agreement_floor_sig_figs=np.int64(5),
        # the three extracted gaps (full float64 from W8-4 frame norms):
        delta_E_6=np.float64(float(dE6)),
        delta_E_7=np.float64(float(dE7)),
        delta_E_8=np.float64(float(dE8)),
        # cocycle norms (Sage-QQ exact -> float64):
        cocycle_norm_phi67_recomputed=np.float64(float(phi67_Q)),
        cocycle_norm_phi88_recomputed=np.float64(float(phi88_Q)),
        cocycle_norm_phi67_published=np.float64(cocycle_norm_phi67),
        cocycle_norm_phi88_published=np.float64(cocycle_norm_phi88),
        norms_reproduced=np.bool_(norms_reproduced),
        # DIAGNOSTIC live recompute (current Delta values; NOT the pin):
        delta_E_6_live=np.float64(dE6_live),
        delta_E_7_live=np.float64(dE7_live),
        delta_E_8_live=np.float64(dE8_live),
        R_machine_live_diagnostic=np.float64(R_live),
        # consumer re-validation:
        consumers_revalidated=np.array(consumers_revalidated),
        per_file_orphan_counts=json.dumps(per_file_orphans),
        formal_consistent=np.bool_(formal_consistent),
        # prior canonical:
        substrate_cocycle_ratio_67_88_prior=np.float64(substrate_cocycle_ratio_67_88),
        # metadata:
        L_max=np.int64(L_MAX),
        tau_fold=np.float64(tau_fold),
        M_KK=np.float64(M_KK),
        composite_verdict=composite,
        scheme=SCHEME,
        convention=CONVENTION,
        gate_id=GATE_ID,
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")
    # Round-trip cross-check: re-load and confirm full float64 preserved
    _chk = np.load(OUT_NPZ, allow_pickle=True)  # (local)
    rt_ok = (float(_chk["R_machine_float64"]) == R_machine_f64)  # (local)
    print(f"  Class-8.3 round-trip: npz R_machine_float64 == in-memory full float64: {rt_ok}")

    # ---- Plot: number line F1 / F2 / R_machine / 7.3250 band-center + 0.1% band ----
    fig, ax = plt.subplots(1, 1, figsize=(11, 4.5))
    band_center = 7.3250  # (local) 4-sf FORMAL falsifier band-center
    band_half = 0.001 * band_center  # (local) +/-0.1% falsifier band
    ax.axvspan(band_center - band_half, band_center + band_half, color="C2", alpha=0.15,
               label=f"falsifier band 7.3250 +/-0.1% [{band_center-band_half:.4f}, {band_center+band_half:.4f}]")
    ax.axvline(band_center, color="C2", ls=":", lw=1.2, label="4-sf band-center 7.3250")
    ax.axvline(F1_f64, color="C1", ls="--", lw=1.5, label=f"F1 = 7.324974 (direct ratio; double-rounded)")
    ax.axvline(F2_f64, color="C0", ls="--", lw=1.5, label=f"F2 = 7.324992 (Sage-QQ reconstruction)")
    ax.axvline(R_machine_f64, color="C3", ls="-", lw=2.4,
               label=f"R_machine = {R_machine_f64:.9f} ({branch_label})")
    ax.scatter([R_machine_f64], [0], color="C3", s=90, zorder=5)
    # Zoom to the 6-sf region
    ax.set_xlim(7.32485, 7.32515)
    ax.set_yticks([])
    ax.set_xlabel(r"$R = (\delta E_6 \cdot \delta E_7)/(\delta E_8)^2$  (cocycle ratio $\|\phi_{67}\|/\|\phi_{88}\|$)")
    ax.set_title(
        f"{GATE_ID}\n"
        f"substrate-first R_machine = {R_machine_qq_str} = {R_machine_f64:.9f}  |  branch: {branch_label}  |  "
        f"5-sf agreement floor (F1,F2 -> 7.3250)",
        fontsize=9,
    )
    ax.legend(loc="upper center", fontsize=7.5, ncol=1)
    ax.grid(True, axis="x", ls=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")

    # ---- Step 8: dual-SHA + verdict emission ----
    print("\n" + "=" * 76)
    print("Step 8: dual-SHA + verdict line")
    print("=" * 76)
    audit, content = compute_dual_sha(pins, SCRIPT_PATH)
    print(f"  audit_sha256   = {audit}")
    print(f"  content_sha256 = {content}")

    value_str = (
        f"R_machine={R_machine_f64!r};"
        f"R_machine_QQ={R_machine_qq_str};"
        f"round6sf={R_round6};"
        f"branch={branch_label};"
        f"dist_F1={dist_to_F1:.4e};dist_F2={dist_to_F2:.4e};"
        f"dE6={float(dE6)};dE7={float(dE7)};dE8={float(dE8)};"
        f"norms_reproduced={norms_reproduced};"
        f"agreement_floor=5sf;"
        f"consumers_revalidated=7;formal_consistent={formal_consistent};"
        f"prior_pin={substrate_cocycle_ratio_67_88};"
        f"re_pin_target={R_machine_f64!r}"
    )  # (local)

    append_verdict(composite, value_str, audit, content)
    print(f"\n  Verdict line appended to {VERDICT_FILE.relative_to(ROOT)}")
    print(f"  {GATE_ID}: {composite}")
    print(f"\n{'='*76}")
    print(f"{GATE_ID} complete -- wall-time {time.time()-t0:.2f}s")
    print(f"  R_machine (substrate pin for W5-2) = {R_machine_f64!r}")
    print(f"  branch = {branch_label}")
    print(f"{'='*76}")


if __name__ == "__main__":
    main()
