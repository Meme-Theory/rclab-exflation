#!/usr/bin/env python3
"""
S103 W2-3 — S103-VIIAM-LINDEXED-ANCHOR — L-indexed Level-3 anchor for the §VII.AM envelope row
================================================================================================

Gate: S103-VIIAM-LINDEXED-ANCHOR ([VERIFY])

Pre-registered threshold (cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"):
  Registry-PASS iff  anchor(L=10) < envelope(L=10)   (STRICT central-value inequality, no tolerance band)
  evaluated at alpha = 4.690533158119443 (W1-4 / s101 npz pin).

  PRE-REGISTERED L-INDEXING RULE (declared in plan §W2-3 BEFORE evaluation, anti-comparator-shopping):
      anchor(L=10) := dGamma_over_Gamma[index for L=10]
                    = the per-L convergent effacement deviation at the L=10 slice
                    = 4.3968e-05.
  The dGamma_over_Gamma array (length 4) is indexed at L in {8,9,10,11}  (the first four of the
  s101 L_scan = [8,9,10,11,12]; L=12 is the convergence reference where Gamma_eff -> canonical 0.99970,
  so its deviation is the anchor for the difference array). L=10 is therefore index 2.

  PRE-REGISTERED COMPARATOR (S102 W2 anti-comparator-shopping): the MORE-favorable PREFACTORED envelope
      envelope_prefac(L=10) = C * 10^{-alpha},  C = exp(intercept) = exp(0.6217547500863554) = 1.86219286
                            = 3.7974e-05  (s102 recon npz 'level2_reconciled').
  The bare envelope env_at_Lmax10 = 2.0392e-05 is reported as a CROSS-CHECK (it is the s101 npz field).

  Verdict (governed by the PRE-REGISTERED prefactored comparator):
    PASS iff anchor(L=10) <  envelope_prefac(L=10)  (strict).
    FAIL iff anchor(L=10) >= envelope_prefac(L=10).
    INFO iff the L=10 indexing slice is UNDERDETERMINED (the dGamma length-4 vs L_scan length-5 map
         is ambiguous at the L=10 slice). [Pre-flight: the map is UNAMBIGUOUS -> INFO does not fire;
         see verify_index_unambiguous() below.]

Substitution chain (L-indexing direction claim; MANDATORY per plan §W2-3 substitution_chain.content):
  Definition 1: anchor_FIXED      = 1 - Gamma_eff = 1 - 0.99970 = 3.0e-4   (S102 W2 RECON Level-3, Q3a).
  Definition 2: anchor_LINDEXED(L)= dGamma_over_Gamma(L) = (Gamma_eff(L) - Gamma_canonical)/Gamma_canonical
                                    = the per-L convergent effacement deviation, L-INDEXED.
                                    [s101 npz: [9.70e-05, 6.90e-05, 4.40e-05, 2.11e-05] at L in {8,9,10,11}]
  Definition 3: envelope_prefac(L=10) = C * 10^{-alpha} = 1.8622 * 2.0392e-05 = 3.7974e-05  (PRE-REG comparator).
  Substitute:   anchor_LINDEXED(L=10) = dGamma_over_Gamma[2] = 4.3968e-05.
  Simplify:     anchor_LINDEXED(L=10) / anchor_FIXED = 4.3968e-05 / 3.0e-4 = 0.1466
                => the L-indexed anchor is 6.82x SMALLER than the fixed anchor (SHRINKS / brings CLOSER).
  Canonical:    anchor_LINDEXED(L=10) vs envelope_prefac(L=10): 4.3968e-05 vs 3.7974e-05 => ratio 1.158.
  Direction:    anchor_LINDEXED(L=10) > envelope_prefac(L=10) (ratio 1.158 > 1)
                => strict Level-3 < Level-2 does NOT hold at L=10 even with L-indexing + prefactored envelope.
                (Cross-check bare: 4.3968e-05 > 2.0392e-05, ratio 2.156 => also FAILS.)
  Conclusion:   the L-indexing brings the anchor materially CLOSER (6.8x reduction from 3.0e-4) but at the
                canonical L=10 the indexed anchor still sits 1.16x ABOVE the more-favorable envelope =>
                envelope ROW stays NOT-SATISFIED at L=10 under the pre-registered L-indexed rule. The
                theorem-STRUCTURE (§VII.AM Universal Lock Condition Level-1, STAGE-3-PERMANENT per S100a)
                is UNTOUCHED. The gate EVALUATES the pinned inequality at the L=10 slice ONLY; the
                pre-registered L=10-slice rule is the arbiter, NOT a deeper-L comparator search.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-101/s101_viiam_alpha_envelope_pin.npz  (alpha, dGamma_over_Gamma, env_at_Lmax10, ...)
  - computations/session-102/s102_w2_viiam_l2l3_recon.npz        (level2_reconciled = prefactored envelope, level3)
  - canonical_constants.py (feeds audit_sha256 only)  [Gamma_effacement = 0.99970 cross-check]
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

  Plan-freeze pinned canonical SHA was 9f2fe9983ecbbb76a2ba1b3e951cf9275deda8d7f2241576ef23b7f728ba1047.
  At runtime canonical_constants.py was append-only-extended (S103 W5-2 COMMIT); its SHA DRIFTED. This is a
  benign mid-session canonical extension; re-pinned at runtime and DISCLOSED per
  substrate-first-canonical-sourcing.md §(ii.B). The numerical pin Gamma_effacement = 0.99970 is unchanged
  (verified against the canonical at runtime); the drift does not touch any value this gate consumes.

Output 4-tuple:
  (value=<L3=...;L2prefac=...;ratio...>, scheme=cross-pillar-bridge-anatomy-Registry-PASS-criterion-Lindexed-anchor,
   convention=envelope-comparator-PRE-REGISTERED-prefactored-ii/alpha=4.6905/anchor=Lindexed-dGamma, L_max=10)

Classification: GEOMETRIC (the §VII.AM Universal Lock Condition envelope row is a statement about the
                FABRIC's effacement structure and its L_max convergence; D_K eigenvalues -> spectral moments
                -> effacement factor Gamma_eff(L) -> per-L convergent deviation -> L-indexed Level-3 anchor).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys  # (local)
from pathlib import Path as _Path  # (local)

# canonical_constants.py lives in computations/_shared; add to path before import.
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # (local)
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import Gamma_effacement  # explicit cross-check pin  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = _Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S103"                                                   # (local)
GATE_ID = "S103-VIIAM-LINDEXED-ANCHOR"                             # (local)
SCHEME = "cross-pillar-bridge-anatomy-Registry-PASS-criterion-Lindexed-anchor"  # (local)
CONVENTION = "envelope-comparator-PRE-REGISTERED-prefactored-ii/alpha=4.6905/anchor=Lindexed-dGamma"  # (local)
L_MAX = 10                                                         # (local)

# Pre-registered comparator: prefactored envelope is the registry-PASS arbiter; bare is a cross-check.
PRE_REG_COMPARATOR = "prefactored"                                 # (local)
TARGET_L = 10                                                      # (local)  the L=10 slice ONLY (NOT scanned)

# Plan-freeze pinned canonical SHA (override: drifted at runtime; re-pin + disclose per §(ii.B)).
PLAN_FREEZE_CANONICAL_SHA = (
    "9f2fe9983ecbbb76a2ba1b3e951cf9275deda8d7f2241576ef23b7f728ba1047"
)                                                                  # (local)

IN_S101 = COMPUTATIONS_DIR / "session-101" / "s101_viiam_alpha_envelope_pin.npz"
IN_S102 = COMPUTATIONS_DIR / "session-102" / "s102_w2_viiam_l2l3_recon.npz"

OUT_NPZ = SESSION_DIR / "s103_viiam_lindexed_anchor.npz"
OUT_PNG = SESSION_DIR / "s103_viiam_lindexed_anchor.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    IN_S101,
    IN_S102,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: _Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[_Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: _Path, canonical_path: _Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Index resolution + compute
# ---------------------------------------------------------------------------

def verify_index_unambiguous(L_scan: np.ndarray, dGamma: np.ndarray) -> tuple[bool, int, str]:
    """Resolve the L=10 slice index in the dGamma_over_Gamma array.

    The pre-registered indexing rule: dGamma_over_Gamma (length 4) is indexed at L in {8,9,10,11}
    (the first four of L_scan = [8,9,10,11,12]). L=10 is therefore index 2.

    Returns (unambiguous, index, note). The INFO branch fires iff unambiguous is False.
    """
    note = ""  # (local)
    # Structural requirement of the pre-registered map: dGamma length is exactly len(L_scan) - 1,
    # and the difference/deviation array aligns with the FIRST len(dGamma) entries of L_scan.
    if len(dGamma) != len(L_scan) - 1:
        note = (
            f"AMBIGUOUS: len(dGamma)={len(dGamma)} != len(L_scan)-1={len(L_scan) - 1}; "
            f"the difference-array alignment is undetermined."
        )
        return False, -1, note
    # L=10 must appear in the first len(dGamma) entries of L_scan.
    first_block = list(L_scan[: len(dGamma)])  # (local)  -> [8,9,10,11]
    if TARGET_L not in first_block:
        note = f"AMBIGUOUS: L={TARGET_L} not in difference-array block {first_block}."
        return False, -1, note
    idx = first_block.index(TARGET_L)  # (local) -> 2
    note = (
        f"UNAMBIGUOUS: dGamma (len {len(dGamma)}) indexes L in {first_block} "
        f"(first {len(dGamma)} of L_scan={list(L_scan)}); L={TARGET_L} -> index {idx}. "
        f"L=12 is the convergence reference (Gamma_eff -> canonical, deviation -> anchor)."
    )
    return True, idx, note


def compute(pins: dict[str, str]) -> dict:
    out: dict = {}  # (local)

    # --- Load inputs ---
    d101 = np.load(IN_S101, allow_pickle=True)  # (local)
    d102 = np.load(IN_S102, allow_pickle=True)  # (local)

    L_scan = np.asarray(d101["L_scan"])                                   # (local) [8,9,10,11,12]
    dGamma = np.asarray(d101["dGamma_over_Gamma"], dtype=float)           # (local) len 4
    Gamma_eff_table = np.asarray(d101["Gamma_eff_table"], dtype=float)    # (local) len 5
    gamma_canonical = float(d101["gamma_canonical"])                      # (local) 0.99970
    alpha = float(d101["alpha"])                                          # (local) 4.690533158119443
    intercept = float(d101["intercept"])                                  # (local) 0.6217547500863554
    env_bare_npz = float(d101["env_at_Lmax10"])                           # (local) 2.039233e-05 (= 10^-alpha)
    level3_anchor_fixed = float(d101["level3_anchor"])                    # (local) 3.0e-4 (the S102 fixed anchor)

    level2_reconciled = float(d102["level2_reconciled"])                  # (local) 3.797445e-05 (prefactored, PRE-REG)
    env_prefac_npz = float(d102["env_prefac_Lmax10"])                     # (local) 3.797445e-05 (cross-check)
    env_bare_recon = float(d102["env_bare_Lmax10"])                       # (local) 2.039233e-05 (cross-check)
    C_npz = float(d102["C"])                                             # (local) exp(intercept) = 1.86219286

    # --- Canonical-pin cross-check (Gamma_effacement = 0.99970; SHA drift disclosure) ---
    canonical_runtime_sha = pins.get("computations/_shared/canonical_constants.py", "")  # (local)
    canonical_sha_drifted = (canonical_runtime_sha != PLAN_FREEZE_CANONICAL_SHA)          # (local)
    gamma_canonical_matches = bool(np.isclose(Gamma_effacement, gamma_canonical, atol=1e-12))  # (local)
    fixed_anchor_consistency = bool(
        np.isclose(level3_anchor_fixed, 1.0 - Gamma_effacement, atol=1e-9)
    )  # (local) 3.0e-4 == 1 - 0.99970

    # --- Index resolution (anti-INFO pre-flight) ---
    unambiguous, idx_L10, idx_note = verify_index_unambiguous(L_scan, dGamma)

    # --- Anchor (L-INDEXED, pre-registered) ---
    if unambiguous:
        anchor_L10 = float(dGamma[idx_L10])                              # (local) 4.396804e-05
    else:
        anchor_L10 = float("nan")                                        # (local)

    # Independent re-derivation of the per-L deviation at L=10 from Gamma_eff_table (structural check):
    #   dGamma(L) = (Gamma_eff(L) - gamma_canonical)/gamma_canonical
    L10_pos = int(np.where(L_scan == TARGET_L)[0][0]) if (L_scan == TARGET_L).any() else -1  # (local) 2
    anchor_L10_rederived = (
        (Gamma_eff_table[L10_pos] - gamma_canonical) / gamma_canonical if L10_pos >= 0 else float("nan")
    )                                                                    # (local)
    anchor_rederive_matches = bool(np.isclose(anchor_L10, anchor_L10_rederived, rtol=1e-9))  # (local)

    # --- Envelopes at L=10 (analytic, cross-checked against npz) ---
    C = math.exp(intercept)                                              # (local) 1.86219286
    env_bare_analytic = 10.0 ** (-alpha)                                 # (local) 2.039233e-05
    env_prefac_analytic = C * env_bare_analytic                          # (local) 3.797445e-05

    env_bare = env_bare_analytic                                         # (local) PRE-REG bare comparator
    env_prefac = env_prefac_analytic                                     # (local) PRE-REG prefactored comparator

    # Cross-check analytic-vs-npz envelope agreement (publication precision 6 sig figs):
    bare_cross_ok = bool(np.isclose(env_bare, env_bare_npz, rtol=1e-9))             # (local)
    prefac_cross_ok = bool(np.isclose(env_prefac, level2_reconciled, rtol=1e-9))    # (local)
    C_cross_ok = bool(np.isclose(C, C_npz, rtol=1e-9))                              # (local)

    # --- The pinned inequalities (strict <) ---
    ratio_prefac = anchor_L10 / env_prefac                              # (local) 1.1578
    ratio_bare = anchor_L10 / env_bare                                  # (local) 2.1561
    pass_prefac = bool(anchor_L10 < env_prefac)                        # (local) PRE-REG comparator (arbiter)
    pass_bare = bool(anchor_L10 < env_bare)                            # (local) cross-check

    # L-indexing reduction (substitution-chain "shrinks/closer" claim):
    reduction_factor = level3_anchor_fixed / anchor_L10                # (local) 6.82x smaller
    lindexed_over_fixed = anchor_L10 / level3_anchor_fixed             # (local) 0.1466

    # --- Verdict ---
    if not unambiguous:
        verdict = "INFO"  # (local)
    elif pass_prefac:     # PRE-REGISTERED prefactored comparator governs registry-PASS (strict <)
        verdict = "PASS"  # (local)
    else:
        verdict = "FAIL"  # (local)

    # Pre-registered comparator decision (declared in plan; logged for the audit trail):
    comparator_used = (
        "PRE-REGISTERED:Level-2=prefactored(ii)C*L^-alpha;"
        "Level-3=Lindexed-dGamma[L=10];comparator-arbiter=prefactored"
    )                                                                  # (local)

    # --- value payload string (NO single-quote chars; emit_verdict wraps value='...') ---
    value = (
        f"L3_Lindexed={anchor_L10:.6e}_vs_L2prefac={env_prefac:.6e}@Lmax10;"
        f"ratio_L3/L2prefac={ratio_prefac:.4f}(>1=>FAIL);"
        f"L2bare={env_bare:.6e}(xcheck:ratio_L3/L2bare={ratio_bare:.4f});"
        f"alpha={alpha:.6f};C=exp({intercept:.6f})={C:.6f};"
        f"Lindex(L=10)=idx{idx_L10}(of_dGamma_len{len(dGamma)}_at_L{[int(x) for x in L_scan[:len(dGamma)]]});"
        f"reduction_vs_fixed3.0e-4={reduction_factor:.4f}x;"
        f"registry_pass_prefac={pass_prefac};registry_pass_bare={pass_bare};"
        f"canonical_SHA_drift={canonical_sha_drifted};"
        f"theorem-STRUCTURE=STAGE-3-PERMANENT(Level-1-out-of-scope)"
    )                                                                  # (local)

    # --- pack ---
    out.update(
        dict(
            value=value,
            verdict=verdict,
            # anchor + envelopes
            anchor_L10=anchor_L10,
            anchor_L10_rederived=anchor_L10_rederived,
            anchor_rederive_matches=anchor_rederive_matches,
            env_prefac=env_prefac,
            env_bare=env_bare,
            level2_reconciled=level2_reconciled,
            env_prefac_npz=env_prefac_npz,
            env_bare_npz=env_bare_npz,
            env_bare_recon=env_bare_recon,
            # ratios + verdicts
            ratio_prefac=ratio_prefac,
            ratio_bare=ratio_bare,
            pass_prefac=pass_prefac,
            pass_bare=pass_bare,
            # L-indexing
            idx_L10=idx_L10,
            unambiguous=unambiguous,
            idx_note=idx_note,
            reduction_factor=reduction_factor,
            lindexed_over_fixed=lindexed_over_fixed,
            level3_anchor_fixed=level3_anchor_fixed,
            # pins / constants
            alpha=alpha,
            intercept=intercept,
            C=C,
            C_npz=C_npz,
            C_cross_ok=C_cross_ok,
            bare_cross_ok=bare_cross_ok,
            prefac_cross_ok=prefac_cross_ok,
            gamma_canonical=gamma_canonical,
            Gamma_effacement_canonical=float(Gamma_effacement),
            gamma_canonical_matches=gamma_canonical_matches,
            fixed_anchor_consistency=fixed_anchor_consistency,
            # SHA drift disclosure
            canonical_runtime_sha=canonical_runtime_sha,
            canonical_plan_freeze_sha=PLAN_FREEZE_CANONICAL_SHA,
            canonical_sha_drifted=canonical_sha_drifted,
            # arrays for plot/context
            L_scan=L_scan.astype(int),
            dGamma_over_Gamma=dGamma,
            Gamma_eff_table=Gamma_eff_table,
            comparator_used=comparator_used,
            scope="envelope-ROW-only;theorem-STRUCTURE=STAGE-3-PERMANENT-out-of-scope",
        )
    )
    return out


# ---------------------------------------------------------------------------
# Section 5b — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    L_scan = r["L_scan"]                                               # (local)
    dGamma = r["dGamma_over_Gamma"]                                    # (local)
    Lblock = L_scan[: len(dGamma)]                                     # (local) [8,9,10,11]

    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))

    # Left: dGamma_over_Gamma (L-indexed anchor) vs L, with the two envelope levels.
    ax0 = ax[0]
    ax0.plot(Lblock, dGamma, "o-", color="#1f77b4", lw=2, ms=8,
             label=r"L-indexed anchor $\delta\Gamma_{eff}/\Gamma_{eff}(L)$")
    ax0.scatter([TARGET_L], [r["anchor_L10"]], s=180, facecolors="none",
                edgecolors="red", lw=2.5, zorder=5,
                label=f"anchor(L=10) = {r['anchor_L10']:.4e}")
    ax0.axhline(r["env_prefac"], color="#2ca02c", ls="--", lw=2,
                label=f"envelope_prefac(L=10) = {r['env_prefac']:.4e} (PRE-REG)")
    ax0.axhline(r["env_bare"], color="#9467bd", ls=":", lw=2,
                label=f"envelope_bare(L=10) = {r['env_bare']:.4e} (xcheck)")
    ax0.axhline(r["level3_anchor_fixed"], color="#888888", ls="-.", lw=1.5, alpha=0.7,
                label=f"FIXED anchor 1-$\\Gamma_{{eff}}$ = {r['level3_anchor_fixed']:.1e} (S102)")
    ax0.set_yscale("log")
    ax0.set_xlabel("L (truncation index)")
    ax0.set_ylabel(r"deviation / envelope (log)")
    ax0.set_title("L-indexed Level-3 anchor vs envelope levels")
    ax0.set_xticks(list(Lblock))
    ax0.legend(fontsize=7.5, loc="upper right")
    ax0.grid(True, which="both", alpha=0.3)

    # Right: the L=10 verdict bar (anchor vs the two envelopes).
    ax1 = ax[1]
    labels = ["anchor(L=10)\nL-indexed", "envelope\nprefac (PRE-REG)", "envelope\nbare (xcheck)"]  # (local)
    vals = [r["anchor_L10"], r["env_prefac"], r["env_bare"]]            # (local)
    colors = ["#d62728", "#2ca02c", "#9467bd"]                         # (local)
    bars = ax1.bar(labels, vals, color=colors, alpha=0.85)
    for b, v in zip(bars, vals):
        ax1.text(b.get_x() + b.get_width() / 2, v * 1.02, f"{v:.3e}",
                 ha="center", va="bottom", fontsize=8)
    ax1.set_ylabel("value at L=10")
    verdict = r["verdict"]                                             # (local)
    ax1.set_title(
        f"VERDICT: {verdict}\n"
        f"anchor/env_prefac = {r['ratio_prefac']:.4f} "
        f"({'<1 PASS' if r['pass_prefac'] else '>1 FAIL'})  |  "
        f"anchor/env_bare = {r['ratio_bare']:.4f} "
        f"({'<1 PASS' if r['pass_bare'] else '>1 FAIL'})"
    )
    ax1.grid(True, axis="y", alpha=0.3)
    # Annotate the 6.82x L-indexing reduction.
    ax1.text(0.5, 0.95,
             f"L-indexing: 3.0e-4 -> {r['anchor_L10']:.3e}  ({r['reduction_factor']:.2f}x smaller)\n"
             f"but still {r['ratio_prefac']:.3f}x ABOVE prefac envelope at L=10",
             transform=ax1.transAxes, ha="center", va="top", fontsize=8,
             bbox=dict(boxstyle="round", fc="#fff3cd", ec="#856404", alpha=0.9))

    fig.suptitle(
        f"{GATE_ID} — §VII.AM envelope-ROW L-indexed Level-3 anchor (alpha={r['alpha']:.4f}, L_max=10)\n"
        "Pre-registered L=10-slice rule; theorem-STRUCTURE (Level-1 Universal Lock) UNTOUCHED",
        fontsize=10.5,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = _Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    canonical_runtime_sha = pins.get("computations/_shared/canonical_constants.py", "")  # (local)
    if canonical_runtime_sha != PLAN_FREEZE_CANONICAL_SHA:
        print()
        print("  [SUBSTRATE-FIRST §(ii.B) DISCLOSURE] canonical_constants.py SHA DRIFT detected:")
        print(f"    plan-freeze pin : {PLAN_FREEZE_CANONICAL_SHA}")
        print(f"    runtime         : {canonical_runtime_sha}")
        print("    cause: S103 W5-2 append-only COMMIT (mid-session canonical extension).")
        print("    impact: NONE on this gate's numbers (Gamma_effacement=0.99970 unchanged; verified below).")
    print()

    r = compute(pins)
    value = r["value"]
    verdict = r["verdict"]

    # --- print the numbers (NUMBERS first) ---
    print("=== NUMBERS ===")
    print(f"  L_scan                 = {list(r['L_scan'])}")
    print(f"  dGamma_over_Gamma      = {list(r['dGamma_over_Gamma'])}  (L in {list(r['L_scan'][:len(r['dGamma_over_Gamma'])])})")
    print(f"  index resolution       : {r['idx_note']}")
    print(f"  anchor(L=10) [L-indexed]   = {r['anchor_L10']:.6e}  (dGamma[idx {r['idx_L10']}])")
    print(f"  anchor(L=10) re-derived    = {r['anchor_L10_rederived']:.6e}  (from Gamma_eff_table; match={r['anchor_rederive_matches']})")
    print(f"  envelope_prefac(L=10)      = {r['env_prefac']:.6e}  (PRE-REGISTERED comparator; npz-xcheck ok={r['prefac_cross_ok']})")
    print(f"  envelope_bare(L=10)        = {r['env_bare']:.6e}  (cross-check; npz-xcheck ok={r['bare_cross_ok']})")
    print(f"  C = exp(intercept)         = {r['C']:.6f}  (npz-xcheck ok={r['C_cross_ok']})")
    print(f"  alpha                      = {r['alpha']:.6f}")
    print(f"  FIXED anchor (1-Gamma_eff) = {r['level3_anchor_fixed']:.6e}  (S102 W2; consistency={r['fixed_anchor_consistency']})")
    print(f"  L-indexing reduction       = {r['reduction_factor']:.4f}x smaller (3.0e-4 -> {r['anchor_L10']:.4e})")
    print()
    print("=== INEQUALITIES (strict <) ===")
    print(f"  anchor/env_prefac = {r['ratio_prefac']:.6f}  =>  anchor < env_prefac ? {r['pass_prefac']}  (PRE-REG arbiter)")
    print(f"  anchor/env_bare   = {r['ratio_bare']:.6f}  =>  anchor < env_bare ?   {r['pass_bare']}  (cross-check)")
    print()
    print("=== CROSS-CHECKS ===")
    print(f"  Gamma_effacement (canonical) = {r['Gamma_effacement_canonical']}  ; gamma_canonical (npz) = {r['gamma_canonical']}  ; match={r['gamma_canonical_matches']}")
    print(f"  anchor re-derivation match   = {r['anchor_rederive_matches']}")
    print(f"  envelope analytic-vs-npz     = prefac:{r['prefac_cross_ok']} bare:{r['bare_cross_ok']} C:{r['C_cross_ok']}")
    print(f"  canonical SHA drifted        = {r['canonical_sha_drifted']}  (disclosed per substrate-first §(ii.B))")
    print()

    # --- save data ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        **{k: v for k, v in r.items() if k not in ("value", "verdict", "idx_note", "comparator_used", "scope", "canonical_runtime_sha", "canonical_plan_freeze_sha")},
        idx_note=r["idx_note"],
        comparator_used=r["comparator_used"],
        scope=r["scope"],
        canonical_runtime_sha=canonical_runtime_sha,
        canonical_plan_freeze_sha=PLAN_FREEZE_CANONICAL_SHA,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        alpha_pin=r["alpha"],
    )
    print(f"  data: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- plot ---
    make_plot(r)
    print(f"  plot: {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # --- 4-tuple + emit payload ---
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra = [
        f"# Lindexed-anchor(L=10)={r['anchor_L10']:.6e} env_prefac={r['env_prefac']:.6e} "
        f"env_bare={r['env_bare']:.6e} ratio_prefac={r['ratio_prefac']:.4f} "
        f"# {GATE_ID} L-indexed Level-3 anchor companion",
        f"# canonical-SHA-drift-disclosure plan_freeze={PLAN_FREEZE_CANONICAL_SHA[:16]}... "
        f"runtime={canonical_runtime_sha[:16]}... cause=S103-W5-2-append-only-COMMIT "
        f"# substrate-first-canonical-sourcing.md §(ii.B)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 regardless of scientific verdict (per math-scripts.md §Exit Codes).
    return 0


if __name__ == "__main__":
    _sys.exit(main())
