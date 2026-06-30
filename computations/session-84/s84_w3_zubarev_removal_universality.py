"""
S84-ZUBAREV-REMOVAL-UNIVERSALITY (W3-29)

Recompute G34 3 spans on F_KK' = F_KK \ {Zubarev} = {zeta, SDW, dimreg, lattice-BR}.
Hypothesis: G34 FAIL at max_span=42.03 is Zubarev-specific (L_max=5, Lambda_Z=0 outlier).
PASS if max_span' < 1.5.
"""
from __future__ import annotations
import sys, os, json, hashlib, time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403


def span_of(vals):
    """Span = max(|v|)/min(|v|), inf if min==0."""
    a = np.array([abs(v) for v in vals])  # (local)
    if a.min() <= 0:
        return float('inf')
    return float(a.max() / a.min())


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for ch in iter(lambda: f.read(65536), b''):
            h.update(ch)
    return h.hexdigest()


def main() -> int:
    t0 = time.time()  # (local)
    src = "computations/session-83/s83_w3_g34_cc_ratio_cluster_universality.npz"
    d = np.load(src, allow_pickle=True)

    # F_KK' = F_KK \ {Zubarev}
    reduced = ["zeta", "SDW", "dimreg", "lattice_BR"]  # (local)
    full = ["zeta", "Zubarev", "SDW", "dimreg", "lattice_BR"]  # (local)

    gates = {
        "ns_over_alphas": "span_1_ns_alphas",
        "As_over_mu":     "span_2_As_mu",
        "fNL_over_r":     "span_3_fNL_r",
    }

    spans_full = {}   # (local)
    spans_reduced = {}  # (local)
    values_by_gate = {}  # (local)

    for gkey in gates:
        vals_full = {r: float(d[f"{gkey}_{r}"]) for r in full}     # (local)
        vals_red  = {r: vals_full[r] for r in reduced}              # (local)
        values_by_gate[gkey] = vals_full
        spans_full[gkey]    = span_of(vals_full.values())
        spans_reduced[gkey] = span_of(vals_red.values())

    max_span_full    = max(spans_full.values())      # (local)
    max_span_reduced = max(spans_reduced.values())   # (local)

    # Gate thresholds
    PASS_TH = 1.5   # (local)
    INFO_TH = 2.5   # (local)
    if max_span_reduced < PASS_TH:
        verdict = "PASS"
    elif max_span_reduced < INFO_TH:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    # INPUT-PIN MAP -> SHA
    pins = {
        "s83_w3_g34_npz_sha": sha256_file(src),
        "canonical_constants_sha": sha256_file("computations/_shared/canonical_constants.py"),
        "L_max": 5,
        "F_KK_reduced": reduced,
        "PASS_TH": PASS_TH,
        "INFO_TH": INFO_TH,
        "spans_full": spans_full,
        "spans_reduced": spans_reduced,
        "max_span_full": max_span_full,
        "max_span_reduced": max_span_reduced,
    }
    closure = hashlib.sha256(json.dumps(pins, sort_keys=True, default=str).encode()).hexdigest()

    print("=" * 72)
    print("S84-ZUBAREV-REMOVAL-UNIVERSALITY (W3-29)")
    print("=" * 72)
    print(f"L_max = 5")
    print(f"F_KK (full):    {full}")
    print(f"F_KK (reduced): {reduced}  [Zubarev removed]")
    print()
    print("Per-gate raw values:")
    for gkey, vmap in values_by_gate.items():
        print(f"  {gkey}:")
        for r, v in vmap.items():
            mark = "  (removed)" if r == "Zubarev" else ""  # (local)
            print(f"    {r:12s}  {v:+.6e}{mark}")
    print()
    print(f"{'Gate':<20}{'span(full)':>14}{'span(reduced)':>17}{'delta':>12}")
    for g in gates:
        print(f"{g:<20}{spans_full[g]:>14.4f}{spans_reduced[g]:>17.4f}"
              f"{spans_full[g]-spans_reduced[g]:>12.4f}")
    print()
    print(f"max_span (full,     5-reg) = {max_span_full:.4f}")
    print(f"max_span (reduced,  4-reg) = {max_span_reduced:.4f}")
    print(f"PASS threshold = {PASS_TH} | INFO threshold = {INFO_TH}")
    print(f"Verdict: {verdict}")
    print(f"Closure SHA: {closure}")
    print(f"Elapsed: {time.time()-t0:.2f}s")

    # Save
    np.savez("computations/session-84/s84_w3_zubarev_removal_universality.npz",
             L_max=5,
             F_KK_full=np.array(full),
             F_KK_reduced=np.array(reduced),
             spans_full_ns_alphas=spans_full["ns_over_alphas"],
             spans_full_As_mu=spans_full["As_over_mu"],
             spans_full_fNL_r=spans_full["fNL_over_r"],
             spans_reduced_ns_alphas=spans_reduced["ns_over_alphas"],
             spans_reduced_As_mu=spans_reduced["As_over_mu"],
             spans_reduced_fNL_r=spans_reduced["fNL_over_r"],
             max_span_full=max_span_full,
             max_span_reduced=max_span_reduced,
             PASS_TH=PASS_TH, INFO_TH=INFO_TH,
             verdict=verdict, closure=closure)

    # Plot before/after
    fig, ax = plt.subplots(figsize=(8, 5))
    gate_names = list(gates.keys())  # (local)
    x = np.arange(len(gate_names))   # (local)
    w = 0.35                          # (local)
    ax.bar(x - w/2, [spans_full[g]    for g in gate_names], w, label="Full F_KK (5 reg)")
    ax.bar(x + w/2, [spans_reduced[g] for g in gate_names], w, label="F_KK \\ Zubarev (4 reg)")
    ax.axhline(PASS_TH, color="green", ls="--", label=f"PASS = {PASS_TH}")
    ax.axhline(INFO_TH, color="orange", ls="--", label=f"INFO = {INFO_TH}")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(gate_names)
    ax.set_ylabel("span = max(|v|)/min(|v|)")
    ax.set_title(f"W3-29: Zubarev removal. max_span 5->4 reg: {max_span_full:.2f} -> {max_span_reduced:.3f}  [{verdict}]")
    ax.legend()
    plt.tight_layout()
    plt.savefig("computations/session-84/s84_w3_zubarev_removal_universality.png", dpi=130)

    # Verdict line
    line = (f"S84-ZUBAREV-REMOVAL-UNIVERSALITY [VERIFY] {verdict} "
            f"max_span_reduced={max_span_reduced:.4f} "
            f"max_span_full={max_span_full:.4f} "
            f"L_max=5 scheme=F_KK_minus_Zubarev "
            f"closure={closure}")
    with open("computations/session-84/s84_gate_verdicts.txt", "a") as f:
        f.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
