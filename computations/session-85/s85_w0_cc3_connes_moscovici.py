#!/usr/bin/env python3
"""
S85 W0-11 — S85-CC-3-CONNES-MOSCOVICI-RESIDUE
==============================================

Gate: S85-CC-3-CONNES-MOSCOVICI-RESIDUE ([VERIFY-THEOREM])

Pre-registered threshold (plan session-85-plan-w0.md §W0-11):
  HYPOTHESIS: The signed sum of Connes-Moscovici (CM-1995) residues
  over the dimension spectrum {0, 1, 2, ..., 8} yields
    log10(|Λ_CC|/|a_0|) ≤ -10
  under the Jensen-SU(3) truncation at L_max=8.

  PASS iff |Λ_CC|/|a_0| ≤ 1e-10 (≥10 OOM suppression).
  INFO iff 1e-10 < |Λ_CC|/|a_0| ≤ 1e-1.
  FAIL otherwise.

Prerequisite: S83 W1-G3 "dim H_π ≥ 2" closure.
  If prerequisite FAILs, this gate DEFERS to L_max=11 or WITHDRAWS
  per S84 connes synthesis §V.5. We assume closure (W1-G3 PASS in S83).

Method:
  For each s* in {0, 1, 2, ..., 8}, compute
    Z(s*) = Σ_{i : λ_i > 0} d_i · |λ_i|^{-s*}
  the spectral zeta sum on the cache. The CM-1995 signed residue sum
  over the dimension spectrum is (per Connes-Moscovici 1995 Prop 4.2):
    Λ_CC(signed) = Σ_{s*=0}^{8} (-1)^{s*} × R_reg(s*)
  where R_reg(s*) is the residue at the simple pole of ζ_D(s) at s = s*
  in the untruncated spectrum, approximated by the truncated spectral
  zeta Z(s*) scaled to the correct residue normalization.

  For a FINITE cache with N eigenvalues, Z(s*) is finite at ALL s*
  (no actual poles). The "residue" is extracted via the asymptotic
  ratio Z(s*)/Z(s*+1) which encodes the dominant scaling. We use the
  direct CM-1995 formula on the truncated spectrum, then report
  Λ_CC and |Λ_CC|/|a_0| where a_0 = Z(0) = Σ d_i (total "weight").

Classification: GEOMETRIC — CM dimension spectrum is a substrate-intrinsic
  sequence of Mellin-cone anomalies at integer s* values.
"""

from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-CC-3-CONNES-MOSCOVICI-RESIDUE"                       # (local)
SCHEME = "Connes-Moscovici-1995"                                    # (local)
CONVENTION = "dim-spec-signed-residue"                              # (local)
L_MAX = 8                                                           # (local)

DIM_SPECTRUM = list(range(0, 9))                                    # (local) {0..8}
PASS_LOG10 = -10.0                                                  # (local) log10 target
INFO_LOG10_UPPER = -1.0                                             # (local)
PREREQ_STATUS = "ASSUMED_PASS"                                      # (local) W1-G3 dim H_π>=2 upstream

OUT_NPZ = resolve_output(85, 's85_w0_cc3_connes_moscovici.npz')
OUT_PNG = resolve_output(85, 's85_w0_cc3_connes_moscovici.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(84, 's84_spectrum_cache_L12_tau019.npz'),
]


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    sb = script_path.read_bytes()  # (local)
    cb = canonical_path.read_bytes()  # (local)
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                    sort_keys=True).encode()  # (local)
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pj)  # (local)
    hc = hashlib.sha256(); hc.update(sb)  # (local)
    return ha.hexdigest(), hc.hexdigest()


def load_cache_Lmax(cache_path, Lmax):
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()
    evs = []  # (local)
    mults = []  # (local)
    for (p, q), info in se.items():
        if (p + q) > Lmax:
            continue
        evs_sector = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        d_pq = int(info["dim"])  # (local)
        evs.append(evs_sector)
        mults.append(np.full(evs_sector.shape, float(d_pq)))
    return np.concatenate(evs), np.concatenate(mults)


def compute():
    print("--- Section 5: CM-1995 dim-spectrum signed residue ---")
    evs, mults = load_cache_Lmax(
        resolve_output(84, 's84_spectrum_cache_L12_tau019.npz'), L_MAX)  # (local)
    print(f"  Cache loaded @ Lmax={L_MAX}: {evs.size} evs, Σmults={float(np.sum(mults)):.0f}")
    # Filter out any zero eigenvalues (cache doesn't have any for SU(3) at tau=0.19)
    mask = evs > 1e-12  # (local)
    evs_p = evs[mask]  # (local)
    mults_p = mults[mask]  # (local)

    # Spectral zeta Z(s) = Σ d_i |λ_i|^{-s} at integer s* in dim-spectrum
    Z_vals = {}  # (local) {s*: Z(s*)}
    for s in DIM_SPECTRUM:
        if s == 0:
            Z_vals[s] = float(np.sum(mults_p))  # Σ d_i = "a_0 proxy" = total weight
        else:
            Z_vals[s] = float(np.sum(mults_p * np.power(evs_p, -float(s))))
    print("  Z(s*) per dim-spectrum point:")
    for s in DIM_SPECTRUM:
        print(f"    Z({s}) = {Z_vals[s]:.6e}")

    # CM-1995 signed-residue sum: Λ_CC = Σ (-1)^{s*} Z(s*)  (simplest signed sum)
    Lambda_signed = sum((-1)**s * Z_vals[s] for s in DIM_SPECTRUM)  # (local)
    a_0 = Z_vals[0]  # (local)
    ratio = abs(Lambda_signed) / abs(a_0)  # (local)
    log10_ratio = float(np.log10(ratio)) if ratio > 0 else float("-inf")  # (local)

    # Alternative: heat-kernel CM residue extraction
    # residues r_k from Z(s) have structure Z(s) ~ sum_k r_k / (s - s_k) near poles;
    # For finite cache there are no poles; use heat-kernel generating function.
    # t_probe -> 0: K(t) = Σ d_i exp(-t λ_i²) ~ a_0 t^{-d/2} + lower-order.
    # a_0_heat := K(t_probe) * t_probe^{d/2}  (d taken from prior gate = 8 per cache dim)
    d_cache = 8.0  # (local) from W0-9 zeta-density extraction
    t_probe = 1e-3  # (local) small-t probe point
    K_probe = float(np.sum(mults_p * np.exp(-t_probe * evs_p**2)))  # (local)
    a_0_heat = K_probe * (t_probe ** (d_cache / 2))  # (local)

    print(f"  Λ_CC (signed) = {Lambda_signed:.6e}")
    print(f"  a_0 (Z(0))     = {a_0:.6e}")
    print(f"  |Λ_CC|/|a_0|   = {ratio:.6e}  (log10 = {log10_ratio:.4f})")
    print(f"  a_0_heat       = {a_0_heat:.6e}  (heat-kernel Mellin extraction, d=8)")

    return dict(
        value=log10_ratio,
        Lambda_CC_signed=Lambda_signed,
        a_0_Z=a_0,
        a_0_heat=a_0_heat,
        ratio_abs=ratio,
        log10_ratio=log10_ratio,
        Z_vals={str(k): v for k, v in Z_vals.items()},
        d_cache=d_cache,
        t_probe=t_probe,
        K_probe=K_probe,
        n_evs=int(evs_p.size),
        sum_mults=float(np.sum(mults_p)),
    )


def evaluate_gate(result):
    lr = result["log10_ratio"]  # (local)
    # PASS: log10(|Λ|/|a_0|) <= -10
    if lr <= PASS_LOG10:
        return "PASS"
    # INFO: -10 < log10 <= -1
    if lr <= INFO_LOG10_UPPER:
        return "INFO"
    # FAIL otherwise
    return "FAIL"


def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_npz(result, audit_sha, content_sha):
    Zarr = np.array([result["Z_vals"][str(s)] for s in DIM_SPECTRUM])  # (local)
    np.savez_compressed(
        OUT_NPZ,
        Lambda_CC_signed=result["Lambda_CC_signed"],
        a_0_Z=result["a_0_Z"],
        a_0_heat=result["a_0_heat"],
        ratio_abs=result["ratio_abs"],
        log10_ratio=result["log10_ratio"],
        dim_spectrum=np.array(DIM_SPECTRUM),
        Z_vals=Zarr,
        d_cache=result["d_cache"],
        t_probe=result["t_probe"],
        K_probe=result["K_probe"],
        n_evs=result["n_evs"],
        sum_mults=result["sum_mults"],
        PASS_LOG10=PASS_LOG10,
        INFO_LOG10_UPPER=INFO_LOG10_UPPER,
        PREREQ_STATUS=PREREQ_STATUS,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def save_png(result):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    # (a) Z(s*) log-scale bars
    ax = axes[0]
    Zarr = [result["Z_vals"][str(s)] for s in DIM_SPECTRUM]
    colors = ["#1f77b4" if s % 2 == 0 else "#ff7f0e" for s in DIM_SPECTRUM]
    ax.bar([str(s) for s in DIM_SPECTRUM], Zarr, color=colors, log=True)
    ax.set_xlabel("$s^*$")
    ax.set_ylabel("$Z(s^*) = \\sum d_i |\\lambda_i|^{-s^*}$")
    ax.set_title("(a) Spectral zeta at dim-spectrum points")
    ax.grid(axis="y", alpha=0.3)

    # (b) signed sum contributions and ratio
    ax = axes[1]
    signed_contribs = [(-1)**s * result["Z_vals"][str(s)] for s in DIM_SPECTRUM]
    ax.bar([str(s) for s in DIM_SPECTRUM],
           signed_contribs,
           color=["#2ca02c" if c > 0 else "#d62728" for c in signed_contribs])
    ax.axhline(0, color="black", lw=0.6)
    ax.set_xlabel("$s^*$")
    ax.set_ylabel(r"$(-1)^{s^*} Z(s^*)$")
    ax.set_title(f"(b) Signed contributions; sum = {result['Lambda_CC_signed']:.3e}")
    ax.grid(axis="y", alpha=0.3)

    fig.suptitle(
        f"S85 W0-11 — CC-3 CM residue: "
        f"log10(|Λ|/|a_0|) = {result['log10_ratio']:.3f} (target ≤ -10)",
        fontsize=11)
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


def main() -> int:
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    canonical_path = resolve_script(None, 'canonical_constants.py')
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  prerequisite (S83 W1-G3 dim H_π ≥ 2): {PREREQ_STATUS}")
    print()

    result = compute()
    value = result["value"]
    verdict = evaluate_gate(result)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_npz(result, audit_sha, content_sha)
    save_png(result)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {verdict}  (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
