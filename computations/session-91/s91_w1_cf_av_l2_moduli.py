#!/usr/bin/env python3
"""
S91 W1-5 - CF-AV-L2-MODULI  (M9; Level-2 moduli-deformation; PRE-REG-INC closure)
=================================================================================

Gate: CF-AV-L2-MODULI  ([VERIFY-THEOREM])

PRE-REG-INC CLOSURE per `mechanical-closure-discipline.md §"When mechanical
closure IS acceptable"` (user directive 2026-05-16; right-maths discipline)
================================================================================

The §VII.AV Level-2 moduli-deformation test (per `phononic-framing.md
§"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY)
requires evaluating the canonical L_emp = d² ln P_GGE / d(ln K)² observable
at three τ-slices τ ∈ {0.18, 0.19, 0.20} on the substrate spectral triple
(A_K^{≤12}, H_K^{≤12}, D_K^{≤12}(τ)). The substrate's spectrum λ_k(τ) varies
with the Jensen deformation parameter τ; the FULL Level-2 test requires
off-fold caches at τ=0.18 and τ=0.20:

    REQUIRED inputs (NOT PRESENT at S91 W1):
      - computations/session-91/s91_w1_spectrum_cache_L12_tau018.npz
      - computations/session-91/s91_w1_spectrum_cache_L12_tau020.npz

Plan W1-5 Field 6 specified that the script raise RuntimeError if these
caches are missing; per user directive 2026-05-16 ("don't 'do' wrong tests
just for a fail when the right test 'can' be done now"), raising
RuntimeError is a "test for a fail" — the substrate-physical question's
RIGHT TEST cannot be performed at this session because the off-fold
substrate-physics infrastructure is not yet built.

The substrate-physically-correct action per `mechanical-closure-discipline.md`:
emit PRE-REG-INC verdict honestly documenting the upstream-cache-build
prerequisite, with available substrate-physics context (canonical
`kappa_2_substrate_FW` Taylor coefficient cross-check), and propagate
the cache-build as a carry-forward to next session.

SUBSTRATE-PHYSICS CONTEXT (canonical inputs available at this session)
----------------------------------------------------------------------
Canonical constants pinned at S90 close + S91 W0:
  - tau_fold = 0.19  (substrate's intrinsic fold position; canonical_constants.py)
  - kappa_2_substrate_FW = 0.021018084987437196
      (CM-1995 §III.4 second-order Jensen perturbation on HK-5 closed form
       5/(1−τ/(5π)); kappa_2 = 1/(5π² A³) with A = 1 − τ_fold/(5π);
       substrate-IS analytic Taylor coefficient; regulator-class INVARIANT)
  - L_emp_canonical = -7.046336474406761 (at τ_fold = 0.19; verified W1-1 + W1-3)

Taylor-expansion prediction for L_emp(τ) under K_canonical(τ) propagation:
  K_canonical(τ) = K_CANONICAL_AT_FOLD · (1 − (τ − τ_fold) · kappa_2_substrate_FW)
  with K_CANONICAL_AT_FOLD = 1.0 (per W1-1 + W1-3 canonical K-horizon)

  K_canonical(τ=0.18) ≈ 1.0 + 0.01 · 0.021018 = 1.000210
  K_canonical(τ=0.20) ≈ 1.0 − 0.01 · 0.021018 = 0.999790

These K_canonical shifts are TINY (Δ ≈ 0.02% = 2e-4) — smaller than the
W1-1/W1-3 K-grid step DLNK = 1e-3. Under fixed-substrate-at-τ_fold
evaluation, L_emp(K=K_canonical(τ)) would be essentially indistinguishable
from L_emp(K=1) within K-grid resolution.

CRITICAL: this K_canonical(τ) effect is a METHODOLOGY-LAYER artifact
(K-grid re-centering); it is NOT the substrate-physics Level-2 moduli
deformation. The TRUE Level-2 test requires off-fold D_K(τ) spectra
where the eigenvalues themselves vary with τ (NOT just the K-grid center).

VERDICT: PRE-REG-INC FAIL
-------------------------
Per `mechanical-closure-discipline.md §"Audit-trail signature"`:

    value='PRE-REG-INC_blocked_by_off-fold-caches-tau-018-020-NOT-PRESENT'

Substrate-physics interpretation: the Level-2 moduli-deformation test
cannot be evaluated at S91 W1 because the substrate-IS off-fold caches
at τ=0.18, τ=0.20 require independent build (D_K(τ) diagonalization at
L_max=12; ~3-4 hours GPU per cache per plan W1-5 §12 effort estimate).

This is honest deferral, NOT a substrate-physics FAIL. Routing:
  - Forward gate seed (S92+): build off-fold caches via D_K(τ)
    diagonalization at L_max=12 for τ ∈ {0.18, 0.20}; then re-dispatch
    W1-5 as `S92-CF-AV-L2-MODULI-RETRY` per `gate-verdicts.md` Option A
    `supersedes=<this audit_sha>` protocol.
  - Within-wave: §W1-5 PRE-REG-INC does NOT contradict the W1-1+W1-3
    OPERATIONAL-ALIGNMENT binding finding for §VII.AV; the moduli-
    deformation test is INDEPENDENT of the operational-alignment axis.

INPUT FILES
-----------
- canonical_constants.py
- script bytes
- off-fold cache pre-check (existence check only; no read)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    tau_fold,
    kappa_2_substrate_FW,
)

import numpy as np  # noqa: E402

# ============================ Gate-block constants ============================
GATE_ID = "CF-AV-L2-MODULI"
SCHEME = "Level-2-moduli-deformation-extension-VII-AV-substrate-distance-2-pole-s4"
CONVENTION = (
    "VII-AV-LEVEL-2-MODULI-PRE-REG-INC-CLOSURE-OFF-FOLD-CACHES-MISSING-"
    "PER-USER-RIGHT-MATHS-2026-05-16"
)
L_MAX = 12  # (local) plan W1-5 Field 7

# Substrate-physics constants
L_EMP_CANONICAL = -7.046336474406761  # (local) section VII.AV registry line 18092
K_CANONICAL_AT_FOLD = 1.0              # (local) canonical K-horizon (W1-1 + W1-3 baseline)
TAU_VALUES = [0.18, 0.19, 0.20]        # (local) plan W1-5 Field 6
THRESHOLD_INVARIANT = 1e-2             # (local) plan W1-5 Field 9
THRESHOLD_DEFORMABLE = 1e-1            # (local) plan W1-5 Field 9

# Output paths
OUT_NPZ = ROOT / "computations" / "session-91" / "s91_w1_cf_av_l2_moduli.npz"
VERDICT_FILE = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

# Input file paths
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
CACHE_018_PATH = ROOT / "computations" / "session-91" / "s91_w1_spectrum_cache_L12_tau018.npz"  # soft prereq (off-fold cache; PRE-REG-INC if absent, built S92+)
CACHE_020_PATH = ROOT / "computations" / "session-91" / "s91_w1_spectrum_cache_L12_tau020.npz"  # soft prereq (off-fold cache; PRE-REG-INC if absent, built S92+)
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "script": SCRIPT_PATH,
}


# ============================ SHA helpers ============================
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:36s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:36s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(
    composite: str, value_str: str,
    audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
    blocking_reason: str,
) -> None:
    """Atomic single-shot append per `gate-verdicts.md` S87+ canonical form +
    mechanical-closure-discipline.md PRE-REG-INC audit-trail signature.
    """
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    blocking_row = (
        f"# blocking_reason={blocking_reason} "
        f"# {GATE_ID} mechanical-closure-discipline.md PRE-REG-INC audit-trail "
        f"signature (off-fold caches not present; right-maths closure per user "
        f"directive 2026-05-16)\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(blocking_row)


# ============================ Main ============================
def main() -> int:
    import time
    t0 = time.time()

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...  (script+canonical+pinmap)")
    print(f"  content_sha256 = {content_sha[:16]}...  (script only)")
    print()

    # 2. Pre-flight: check off-fold cache existence
    print("Pre-flight: checking off-fold cache existence...")
    cache_018_exists = CACHE_018_PATH.exists()
    cache_020_exists = CACHE_020_PATH.exists()
    print(f"  s91_w1_spectrum_cache_L12_tau018.npz: {'PRESENT' if cache_018_exists else 'MISSING'}")
    print(f"  s91_w1_spectrum_cache_L12_tau020.npz: {'PRESENT' if cache_020_exists else 'MISSING'}")
    print()

    if not (cache_018_exists and cache_020_exists):
        # PRE-REG-INC closure per mechanical-closure-discipline.md
        print("=" * 72)
        print("PRE-REG-INC CLOSURE TRIGGERED")
        print("=" * 72)
        print("Off-fold cache(s) NOT present; the Level-2 moduli-deformation test")
        print("requires substrate-IS spectra at τ ∈ {0.18, 0.20}, which require")
        print("independent build (D_K(τ) diagonalization at L_max=12; ~3-4 hours")
        print("GPU per cache per plan W1-5 §12 effort estimate).")
        print()

        # Substrate-physics context: Taylor-expansion prediction
        print("Substrate-physics Taylor-expansion context (canonical inputs available):")
        K_canonical_018 = K_CANONICAL_AT_FOLD * (
            1.0 - (0.18 - tau_fold) * kappa_2_substrate_FW
        )  # (local)
        K_canonical_020 = K_CANONICAL_AT_FOLD * (
            1.0 - (0.20 - tau_fold) * kappa_2_substrate_FW
        )  # (local)
        print(f"  tau_fold                     = {tau_fold}")
        print(f"  kappa_2_substrate_FW         = {kappa_2_substrate_FW}")
        print(f"  K_CANONICAL_AT_FOLD          = {K_CANONICAL_AT_FOLD}")
        print(f"  K_canonical(τ=0.18) (Taylor) = {K_canonical_018:.10f} "
              f"(Δ_K = {K_canonical_018 - K_CANONICAL_AT_FOLD:+.6e})")
        print(f"  K_canonical(τ=0.20) (Taylor) = {K_canonical_020:.10f} "
              f"(Δ_K = {K_canonical_020 - K_CANONICAL_AT_FOLD:+.6e})")
        print()
        print(f"  L_emp_canonical (τ_fold)     = {L_EMP_CANONICAL}")
        print(f"  L_emp_Taylor(τ=0.18) ≈ L_emp_canonical (Δ_K ≈ 2e-4 << DLNK=1e-3 K-grid step)")
        print(f"  L_emp_Taylor(τ=0.20) ≈ L_emp_canonical (same reason)")
        print()
        print("CRITICAL: the K_canonical(τ) METHODOLOGY-LAYER shift is sub-resolution")
        print("of the K-grid; this DOES NOT substitute for the substrate-physics")
        print("Level-2 moduli-deformation test, which requires off-fold D_K(τ) spectra.")
        print()

        # Save NPZ with diagnostic context
        np.savez(
            OUT_NPZ,
            verdict="PRE-REG-INC",
            blocking_reason="off-fold-caches-tau-018-020-NOT-PRESENT",
            tau_fold=tau_fold,
            kappa_2_substrate_FW=kappa_2_substrate_FW,
            K_CANONICAL_AT_FOLD=K_CANONICAL_AT_FOLD,
            K_canonical_018_Taylor=K_canonical_018,
            K_canonical_020_Taylor=K_canonical_020,
            L_EMP_CANONICAL=L_EMP_CANONICAL,
            TAU_VALUES=np.array(TAU_VALUES),
            cache_018_exists=cache_018_exists,
            cache_020_exists=cache_020_exists,
            required_inputs=np.array(
                [str(CACHE_018_PATH), str(CACHE_020_PATH)], dtype=object
            ),
            forward_carry_to_session="S92+",
            forward_remediation="build D_K(τ) caches via diagonalization at L_max=12 for τ ∈ {0.18, 0.20}; then re-dispatch W1-5 per Option A supersedes protocol",
        )

        # Emit PRE-REG-INC verdict line
        value_str = "PRE-REG-INC_blocked_by_off-fold-caches-tau-018-020-NOT-PRESENT"
        blocking_reason = "off-fold-caches-tau-018-020-NOT-PRESENT-requires-D_K-diagonalization-at-L_max-12"
        append_verdict(
            composite="FAIL",  # FAIL per mechanical-closure-discipline.md PRE-REG-INC convention
            value_str=value_str,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="N/A",  # No directional prediction; gate is structurally untestable
            mag_v="N/A",   # No magnitude comparison; prerequisite missing
            reg_v="BREAKDOWN",  # Regime: substrate-physics infrastructure not built
            blocking_reason=blocking_reason,
        )

        wall = time.time() - t0  # (local)
        print(f"=== {GATE_ID}: FAIL (PRE-REG-INC) (wall {wall:.1f}s) ===")
        print(f"    value: {value_str}")
        print(f"    audit_sha256:   {audit_sha}")
        print(f"    content_sha256: {content_sha}")
        return 0  # PRE-REG-INC exits 0; this is honest deferral, not script breakage

    # Else: off-fold caches present → run the substantive Level-2 moduli test
    # (NOT IMPLEMENTED at S91 W1; would require the actual evaluator from plan W1-5)
    print("Off-fold caches present — full Level-2 moduli test pathway")
    print("(NOT IMPLEMENTED at S91 W1; would require full Level-2 evaluator pipeline)")
    print()
    # Mark as INFO instead of running an incomplete pipeline
    value_str = "off-fold-caches-present-but-full-Level-2-evaluator-pipeline-NOT-IMPLEMENTED"
    append_verdict(
        composite="INFO",
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v="N/A",
        mag_v="N/A",
        reg_v="MARGINAL",
        blocking_reason="off-fold-caches-present-but-pipeline-not-implemented",
    )
    wall = time.time() - t0  # (local)
    print(f"=== {GATE_ID}: INFO (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
