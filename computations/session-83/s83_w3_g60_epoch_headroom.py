"""
S83 W3 G60 — EPOCH-LOCAL-HEADROOM-AUDIT
Gate: S83-EPOCH-LOCAL-HEADROOM-AUDIT

Registry identity from S82 W-2 Wrap-Up #8 (s82-as-ledger-self-consistent.md §Wrap-Up #8).

Two-line structural identity:
    headroom_mixed(fold, pivot) := F_3PI(N_fold) / F_slot(N_pivot)
    headroom_local(N)           := F_3PI(N)      / F_slot(N)

SUBSTITUTION CHAIN (mandatory per math-scripts.md):
  Step 1: Define quantities
    F_3PI(N)       := amplitude amplification from 3PI NLO closure at e-fold N
    F_slot(N)      := k_a2 * F_amp(N)  where k_a2 = a_2(tau_pivot)/a_2_fold
    F_3PI(N_fold)  = F_3PI(0)   = 47.9177  (Python-verified from workshop CR4/DS3)
    F_3PI(N_pivot) = F_canonical = 1.0166   (Python-verified from workshop §What Holds #2)
    F_amp_lin(0)   = 6857.69              (Python-verified from workshop §What Holds #3)
    F_amp_canonical= 1.0166               (same as F_3PI at pivot)
    k_a2           = 0.3822               (S78 W2-D framework-canonical)
  Step 2: Substitution
    F_slot(N_pivot) = k_a2 * F_amp_canonical = 0.3822 * 1.0166
    F_slot(N_fold)  = k_a2 * F_amp_lin(0)   = 0.3822 * 6857.69
    headroom_mixed  = F_3PI(0) / F_slot(N_pivot) = 47.9177 / (0.3822 * 1.0166)
    headroom_local(pivot) = F_3PI(pivot) / F_slot(pivot) = 1.0166 / (0.3822 * 1.0166)
    narrowing = headroom_mixed / headroom_local(pivot)
  Step 3: Simplify
    headroom_local(pivot) = F_3PI(pivot) / (k_a2 * F_3PI(pivot)) = 1/k_a2
    Therefore: headroom_local(pivot) = 1/0.3822 = 2.6165...
    headroom_mixed = 47.9177 / (0.3822 * 1.0166) = 47.9177 / 0.38855 = 123.33...
    narrowing = (47.9177 / 0.38855) / (1.0166 / 0.38855) = 47.9177 / 1.0166 = 47.13...
  Step 4: Direction
    headroom_local(pivot) = 2.617 < headroom_mixed = 123.34
    Safety cushion is 47.14x TIGHTER under epoch-local reading (DS3/CR4 correction).
    PASS: identity stated with explicit values, epoch labeling, and substitution chain.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')

import numpy as np
import json
import hashlib
import pathlib
import sys

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Input values from S82 W-2 CR4/DS3 substitution chains (Python-verified)
# These are workshop-validated intermediate results, NOT framework canonical
# constants — all tagged (local) per math-scripts.md audit policy.
# ---------------------------------------------------------------------------

F_3PI_fold     = 47.9177   # (local) F_amp^{3PI}(N=0)  — fold value, S82 W-2 CR4
F_3PI_pivot    = 1.0166    # (local) F_amp^{3PI}(N=55) ≈ F_canonical, S82 §What Holds #2
F_amp_lin_fold = 6857.69   # (local) F_amp_lin(N=0)    — linear amplification at fold
k_a2           = 0.3822    # (local) a_2(tau_pivot)/a_2_fold, S78 W2-D framework-canonical

# ---------------------------------------------------------------------------
# Step 2: Substitution
# ---------------------------------------------------------------------------
F_slot_pivot = k_a2 * F_3PI_pivot          # (local) slot amplitude at pivot
F_slot_fold  = k_a2 * F_amp_lin_fold       # (local) slot amplitude at fold

headroom_mixed         = F_3PI_fold / F_slot_pivot    # (local) epoch-MIXED (fold ceiling / pivot slot)
headroom_local_pivot   = F_3PI_pivot / F_slot_pivot   # (local) epoch-LOCAL at pivot
headroom_local_fold    = F_3PI_fold  / F_slot_fold    # (local) epoch-LOCAL at fold

narrowing_factor       = headroom_mixed / headroom_local_pivot   # (local) how much tighter epoch-local is

# ---------------------------------------------------------------------------
# Step 3: Verify against workshop-stated values
# ---------------------------------------------------------------------------
# Workshop states: headroom_mixed=123.34, headroom_local_pivot=2.617, narrowing=47.14
ref_mixed   = 123.34   # (local) reference from workshop CR4/DS3
ref_local   = 2.617    # (local) reference from workshop CR4/DS3
ref_narrow  = 47.14    # (local) reference from workshop

tol = 0.005  # (local) 0.5% tolerance for rounding in source

err_mixed  = abs(headroom_mixed        - ref_mixed)  / ref_mixed    # (local)
err_local  = abs(headroom_local_pivot  - ref_local)  / ref_local    # (local)
err_narrow = abs(narrowing_factor      - ref_narrow) / ref_narrow   # (local)

chain_verified = (err_mixed < tol) and (err_local < tol) and (err_narrow < tol)  # (local)

# log10 headroom values (for OOM classification)
log10_headroom_mixed = np.log10(headroom_mixed)           # (local)
log10_headroom_local = np.log10(headroom_local_pivot)     # (local)
log10_headroom_fold  = np.log10(headroom_local_fold)      # (local) should be -1.738

# Workshop states log10_headroom_fold = -1.738 (slot EXCEEDS 3PI ceiling at fold)
ref_log10_fold = -1.738  # (local)
err_log10_fold = abs(log10_headroom_fold - ref_log10_fold)  # (local) absolute OOM error

# ---------------------------------------------------------------------------
# Step 4: Direction verdict
# headroom_local < headroom_mixed  =>  epoch-local reading is TIGHTER
# The A_s PASS-F2 cushion is narrowing_factor times tighter than originally advertised
# ---------------------------------------------------------------------------
direction_correct = (headroom_local_pivot < headroom_mixed) and (narrowing_factor > 40)  # (local)

print("=" * 70)
print("S83-EPOCH-LOCAL-HEADROOM-AUDIT — Substitution Chain Verification")
print("=" * 70)
print()
print("Input values (from S82 W-2 CR4/DS3):")
print(f"  F_3PI(fold)     = {F_3PI_fold}")
print(f"  F_3PI(pivot)    = {F_3PI_pivot}")
print(f"  F_amp_lin(fold) = {F_amp_lin_fold}")
print(f"  k_a2            = {k_a2}")
print()
print("Substitution step:")
print(f"  F_slot(pivot)   = k_a2 * F_3PI(pivot) = {k_a2} * {F_3PI_pivot} = {F_slot_pivot:.6f}")
print(f"  F_slot(fold)    = k_a2 * F_lin(fold)  = {k_a2} * {F_amp_lin_fold} = {F_slot_fold:.4f}")
print()
print("Simplified forms:")
print(f"  headroom_mixed        = F_3PI(fold) / F_slot(pivot) = {F_3PI_fold} / {F_slot_pivot:.6f} = {headroom_mixed:.4f}")
print(f"  headroom_local(pivot) = F_3PI(pivot)/ F_slot(pivot) = {F_3PI_pivot} / {F_slot_pivot:.6f} = {headroom_local_pivot:.4f}")
print(f"  headroom_local(fold)  = F_3PI(fold) / F_slot(fold)  = {F_3PI_fold} / {F_slot_fold:.4f} = {headroom_local_fold:.6f}")
print(f"  narrowing_factor      = headroom_mixed / headroom_local(pivot) = {headroom_mixed:.4f} / {headroom_local_pivot:.4f} = {narrowing_factor:.4f}")
print()
print("OOM classification:")
print(f"  log10(headroom_mixed)        = {log10_headroom_mixed:.3f} OOM")
print(f"  log10(headroom_local_pivot)  = {log10_headroom_local:.3f} OOM  [pivot slot below 3PI ceiling]")
print(f"  log10(headroom_local_fold)   = {log10_headroom_fold:.3f} OOM  [slot EXCEEDS ceiling at fold]")
print(f"  ref log10_fold = {ref_log10_fold:.3f}, err = {err_log10_fold:.4f} OOM")
print()
print("Workshop reference cross-check:")
print(f"  headroom_mixed:  computed={headroom_mixed:.4f}  ref={ref_mixed}  err={err_mixed*100:.3f}%  {'PASS' if err_mixed < tol else 'FAIL'}")
print(f"  headroom_local:  computed={headroom_local_pivot:.4f}  ref={ref_local}   err={err_local*100:.3f}%  {'PASS' if err_local < tol else 'FAIL'}")
print(f"  narrowing:       computed={narrowing_factor:.4f}  ref={ref_narrow}  err={err_narrow*100:.3f}%  {'PASS' if err_narrow < tol else 'FAIL'}")
print()
print("Direction:")
print(f"  headroom_local ({headroom_local_pivot:.3f}) < headroom_mixed ({headroom_mixed:.2f})")
print(f"  => Epoch-local reading is {narrowing_factor:.2f}x TIGHTER than epoch-mixed.")
print(f"  => A_s PASS-F2 safety cushion is {narrowing_factor:.2f}x tighter than originally advertised.")
print()

# ---------------------------------------------------------------------------
# Two-line registry identity (canonical form)
# ---------------------------------------------------------------------------
identity_line1 = (
    f"headroom_mixed(fold,pivot) := F_3PI(N_fold) / F_slot(N_pivot) "
    f"= {F_3PI_fold} / {F_slot_pivot:.6f} = {headroom_mixed:.2f}"
)
identity_line2 = (
    f"headroom_local(N)          := F_3PI(N)      / F_slot(N)      "
    f"[pivot: {F_3PI_pivot}/{F_slot_pivot:.6f}={headroom_local_pivot:.3f}; "
    f"fold: {F_3PI_fold}/{F_slot_fold:.2f}={headroom_local_fold:.4f}]; "
    f"narrowing = {narrowing_factor:.2f}x"
)

print("TWO-LINE REGISTRY IDENTITY:")
print(f"  Line 1: {identity_line1}")
print(f"  Line 2: {identity_line2}")
print()

# ---------------------------------------------------------------------------
# Gate verdict
# ---------------------------------------------------------------------------
gate_pass = chain_verified and direction_correct  # (local)

if gate_pass:
    verdict_str = "PASS"
    verdict_detail = (
        f"2-line epoch-local headroom identity stated with explicit substitution chain "
        f"and epoch labeling. headroom_mixed={headroom_mixed:.2f}, "
        f"headroom_local(pivot)={headroom_local_pivot:.3f}, "
        f"narrowing={narrowing_factor:.2f}x. All three cross-checks within 0.5% of "
        f"S82 W-2 CR4/DS3 workshop values."
    )
else:
    verdict_str = "FAIL"
    verdict_detail = (
        f"Numerical mismatch: err_mixed={err_mixed:.4f}, err_local={err_local:.4f}, "
        f"err_narrow={err_narrow:.4f}"
    )

print(f"GATE VERDICT: S83-EPOCH-LOCAL-HEADROOM-AUDIT")
print(f"Result: {verdict_str}")
print(f"Detail: {verdict_detail}")
print()

# ---------------------------------------------------------------------------
# Save outputs
# ---------------------------------------------------------------------------
results = {
    "gate": "S83-EPOCH-LOCAL-HEADROOM-AUDIT",
    "verdict": verdict_str,
    "F_3PI_fold": F_3PI_fold,
    "F_3PI_pivot": F_3PI_pivot,
    "F_amp_lin_fold": F_amp_lin_fold,
    "k_a2": k_a2,
    "F_slot_pivot": float(F_slot_pivot),
    "F_slot_fold": float(F_slot_fold),
    "headroom_mixed": float(headroom_mixed),
    "headroom_local_pivot": float(headroom_local_pivot),
    "headroom_local_fold": float(headroom_local_fold),
    "narrowing_factor": float(narrowing_factor),
    "log10_headroom_mixed": float(log10_headroom_mixed),
    "log10_headroom_local_pivot": float(log10_headroom_local),
    "log10_headroom_local_fold": float(log10_headroom_fold),
    "chain_verified": bool(chain_verified),
    "direction_correct": bool(direction_correct),
    "err_mixed_pct": float(err_mixed * 100),
    "err_local_pct": float(err_local * 100),
    "err_narrow_pct": float(err_narrow * 100),
    "identity_line1": identity_line1,
    "identity_line2": identity_line2,
    "source": "s82-as-ledger-self-consistent.md §Wrap-Up #8 (CR4/DS3)",
    "session": "S82/S83",
}

outdir = pathlib.Path(__file__).parent
npz_path = outdir / "s83_w3_g60_epoch_headroom.npz"
np.savez(str(npz_path), **{k: str(v) if isinstance(v, str) else v for k, v in results.items()})
print(f"Saved: {npz_path}")

# ---------------------------------------------------------------------------
# PNG — bar chart comparing headroom values
# ---------------------------------------------------------------------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left: headroom comparison
    ax = axes[0]
    labels  = ["headroom_mixed\n(fold/pivot)", "headroom_local\n(pivot)", "headroom_local\n(fold)"]
    values  = [headroom_mixed, headroom_local_pivot, abs(headroom_local_fold)]
    colors  = ["#c0392b", "#27ae60", "#e67e22"]
    bars = ax.bar(labels, values, color=colors, edgecolor="black", linewidth=0.8)
    ax.set_yscale("log")
    ax.set_ylabel("Headroom value (log scale)")
    ax.set_title("Epoch-Local vs Epoch-Mixed Headroom\n(S82 W-2 Wrap-Up #8 CR4/DS3)")
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.15,
                f"{val:.3f}", ha="center", va="bottom", fontsize=9)
    ax.axhline(1.0, color="gray", linestyle="--", linewidth=0.8, label="headroom=1 (ceiling=slot)")
    ax.legend(fontsize=8)

    # Right: OOM values
    ax2 = axes[1]
    oom_labels = ["log10(mixed)", "log10(local\npivot)", "log10(local\nfold)"]
    oom_vals   = [log10_headroom_mixed, log10_headroom_local, log10_headroom_fold]
    oom_colors = ["#c0392b", "#27ae60", "#e67e22"]
    ax2.bar(oom_labels, oom_vals, color=oom_colors, edgecolor="black", linewidth=0.8)
    ax2.axhline(0.0, color="gray", linestyle="--", linewidth=0.8, label="OOM=0 (headroom=1)")
    ax2.set_ylabel("log10(headroom) [OOM]")
    ax2.set_title("OOM Classification\n(+ = slot below ceiling; - = slot EXCEEDS ceiling)")
    for i, (lbl, v) in enumerate(zip(oom_labels, oom_vals)):
        ax2.text(i, v + (0.05 if v >= 0 else -0.12),
                 f"{v:.3f}", ha="center", va="bottom", fontsize=9)
    ax2.legend(fontsize=8)

    plt.suptitle(
        f"S83-EPOCH-LOCAL-HEADROOM-AUDIT: narrowing = {narrowing_factor:.2f}x\n"
        f"Verdict: {verdict_str}",
        fontsize=11, fontweight="bold"
    )
    plt.tight_layout()
    png_path = outdir / "s83_w3_g60_epoch_headroom.png"
    plt.savefig(str(png_path), dpi=120, bbox_inches="tight")
    plt.close()
    print(f"Saved: {png_path}")
except Exception as e:
    print(f"[WARNING] PNG generation failed: {e}")
    png_path = None

# ---------------------------------------------------------------------------
# SHA256 of input pin map (for verdict provenance)
# ---------------------------------------------------------------------------
pin_map = {
    "F_3PI_fold": F_3PI_fold,
    "F_3PI_pivot": F_3PI_pivot,
    "F_amp_lin_fold": F_amp_lin_fold,
    "k_a2": k_a2,
    "source": "s82-as-ledger-self-consistent.md §Wrap-Up #8",
}
pin_str = json.dumps(pin_map, sort_keys=True)
sha256  = hashlib.sha256(pin_str.encode()).hexdigest()

print()
print(f"Input pin SHA256: {sha256}")
print()
print("VERDICT LINE (for s83_gate_verdicts.txt):")
verdict_line = (
    f"S83-EPOCH-LOCAL-HEADROOM-AUDIT: {verdict_str} -- "
    f"value=headroom_mixed={headroom_mixed:.2f}_headroom_local_pivot={headroom_local_pivot:.3f}_narrowing={narrowing_factor:.2f}x "
    f"scheme=epoch-local-headroom "
    f"convention=2-line-registry-S82-W2-WrapUp8 "
    f"L_max=N/A "
    f"sha256={sha256}"
)
print(verdict_line)
