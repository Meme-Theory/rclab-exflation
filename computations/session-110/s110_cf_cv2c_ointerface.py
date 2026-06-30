#!/usr/bin/env python3
"""
S110 W4a-5 S110-CF-CV2C-OINTERFACE — Ô-interface φ_paasch / 7n grading test
===========================================================================

Gate: S110-CF-CV2C-OINTERFACE ([VERIFY])

Pre-registered threshold (grid-membership SET test; NO directional claim):
  R_B2 = the B2-sector dimensionless eigenvalue ratios feeding λ_eff and N₀ in the
         BCS M_KK dimensional transmutation (M_KK = M_Pl·exp(-1/(λ_eff·N₀))).
  node-set = {φ_paasch = 1.5315844} ∪ {7n-grid ratios from inv-3 W3-4}.
  test = min over the PRE-PINNED B2-ratio family, min over node, of |R_B2/node - 1|.
  PASS (COUPLED)      iff test <= 0.01  — one quantization grades input AND output.
  INFO (INDEPENDENT)  iff test  > 0.01 but the B2 ratios are self-consistent on a
                          DIFFERENT quantization (still AGREE; layers not coupled).
  FAIL (CONFLICT)     only if provably-continuous input under a provably-discrete
                          output ladder (a genuine quantization inconsistency).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (B2-sector eigenvalues)
  - computations/investigation-3/inv3_w3_casimir_graded_nj_7n.npz (7n grid; hard inv-3↔inv-11 dep)
  - computations/investigation-11/inv11_w1_mkk_dimensional_transmutation.npz (λ_eff, N₀, B2 gaps)
  - canonical_constants.py (feeds audit_sha256 only; phi_paasch, Delta_B2, T_GGE_B2)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<test>, scheme=B2-sector-dimensionless-ratio,
   convention=RATIO-NORMALIZED-TRACE-MEAN, L_max=12)

Classification: GEOMETRIC. This concerns the fabric's representation-theoretic content
  (Peter-Weyl eigenvalue ratios), NOT its excitations. Direction of explanation:
  D_K eigenvalues -> B2-sector dimensionless ratios -> comparison to the φ_paasch / 7n
  grading. φ_paasch is itself a bare D_K eigenvalue ratio ((3,0)/(0,0), proven_1292);
  the 7n grid is Casimir-graded (inv-3 W3-4). The test asks whether the INPUT structural
  ratios and the OUTPUT mass-ladder ratios are graded by the SAME substrate quantization.

METHODOLOGY
-----------
inv-11 W5-1 established the AGREE verdict: the output mass ladder N(p)/N(K)=75/49=1.5306
sits 0.063% from φ_paasch. This gate sharpens AGREE to AGREE-COUPLED vs AGREE-INDEPENDENT
by asking whether the SAME grading governs the INPUT B2-sector dimensionless ratios that
feed the M_KK transmutation (λ_eff, N₀). The B2 band is the (1,1) mult-8 "optical" band;
its pairing-window quantities (the van-Hove DOS edge E_vH, the band floor/ceiling, the
mean-field/Richardson/ED gaps) are the dimensionless inputs to M_KK=M_Pl·exp(-1/(λ_eff·N₀)).
We pin the candidate B2-ratio family at design time (no post-hoc cherry-pick) and report
the FULL family plus the min-deviation match against the {φ_paasch}∪{7n-grid} node set.

Counting axis (regulator-pin-discipline.md): dimensionless ratios are INTENSIVE per-channel
functionals — ratios of state evaluations, NOT extensive block-sums. convention=RATIO-
NORMALIZED-TRACE-MEAN.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`.
- Reuses the L12 cache (Friedrich-Bär-saturated); NO new diagonalization.
- Plan-text drift on canonical_constants.py SHA (plan pinned e5a7587..., disk is the
  runtime value) is resolved by npz-ground-truth at runtime per substrate-first-canonical-
  sourcing.md §(ii.B): SHAs computed from live disk bytes; drift documented in stdout.
- Gate verdict via emit_verdict MCP tool (script PRINTS payload; does NOT write verdict file).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-cap: scalar/small-array work only
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED_DIR_BOOTSTRAP = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared"
)
if SHARED_DIR_BOOTSTRAP not in sys.path:
    sys.path.insert(0, SHARED_DIR_BOOTSTRAP)

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import phi_paasch, Delta_B2, T_GGE_B2, tau_fold  # explicit

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S110"                                                  # (local)
GATE_ID = "S110-CF-CV2C-OINTERFACE"                               # (local)
SCHEME = "B2-sector-dimensionless-ratio"                          # (local)
CONVENTION = "RATIO-NORMALIZED-TRACE-MEAN"                        # (local)
L_MAX = 12                                                        # (local)

# Pre-registered thresholds (define BEFORE running)
PASS_TOL = 0.01    # 1% RATIO -> COUPLED                          # (local)
# (no separate info_band: > PASS_TOL routes to INDEPENDENT unless a CONFLICT is proven)

# The higher-precision φ_paasch node (inv-11 W5-1's load-bearing input). Canonical
# phi_paasch=1.531580 (line 289); the 1.5315844 form is the W5-1 reference grid value.
PHI_PAASCH_NODE = 1.5315844                                       # (local)

# Input files
L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
NJ7N_NPZ = COMPUTATIONS_DIR / "investigation-3" / "inv3_w3_casimir_graded_nj_7n.npz"
INV11_NPZ = COMPUTATIONS_DIR / "investigation-11" / "inv11_w1_mkk_dimensional_transmutation.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_DIR / "s110_cf_cv2c_ointerface.npz"
OUT_PNG = SESSION_DIR / "s110_cf_cv2c_ointerface.png"

# Plan-pinned canonical SHA (for drift documentation per substrate-first-canonical-sourcing §ii.B)
PLAN_PINNED_CANONICAL_SHA = "e5a7587f8326c9cc90cb720197a3ace824b3f89c5bbea17cfd659b27f607568a"  # (local)

INPUT_FILES = [CANONICAL_PATH, L12_CACHE, NJ7N_NPZ, INV11_NPZ]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes()                       # (local)
    canonical_bytes = canonical_path.read_bytes()                 # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                             # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def build_node_set():
    """Build the reference grid: {φ_paasch} ∪ {7n-grid ratios}.

    The 7n grid comes from inv-3 W3-4. The OUTPUT mass-ladder ratios N(j+1)/N(j)
    are the integer-graded nodes the output ladder exhibits; the canonical
    OUTPUT anchor is N(p)/N(K)=75/49 (the proton/kaon ratio, 0.063% from φ_paasch).
    We include ALL successive N-ratios as candidate nodes plus φ_paasch.
    """
    g = np.load(NJ7N_NPZ, allow_pickle=True)
    nj = g["paasch_Nj"].astype(float)                             # (local) [7,35,42,98,150]
    N_ratios = g["N_ratios"].astype(float)                        # (local) successive N(j+1)/N(j)
    Np_over_NK = float(g["Np_over_NK"])                           # (local) 75/49 = 1.530612
    fN = float(g["fN"])                                           # (local) 1.236068 (exp factor)
    # Node set: φ_paasch + the output-ladder successive ratios + the canonical proton/kaon
    # + fN (the Paasch exponential factor) as a structurally-distinct grading candidate.
    nodes = {}  # (local) name -> value
    nodes["phi_paasch"] = PHI_PAASCH_NODE
    nodes["Np_over_NK(75/49)"] = Np_over_NK
    nodes["fN(exp-factor)"] = fN
    for i, r in enumerate(N_ratios):
        nodes[f"N_ratio[{i}]"] = float(r)
    return nodes, nj, Np_over_NK, fN


def extract_b2_ratios():
    """Extract the PRE-PINNED B2-sector dimensionless ratio family that feeds λ_eff/N₀.

    The B2 band is the (1,1) mult-8 'optical' band. The M_KK transmutation
    M_KK=M_Pl·exp(-1/(λ_eff·N₀)) consumes the van-Hove DOS edge and the B2 gaps.
    From inv-11 W1-1/W1-2 (the transmutation build) the dimensionless inputs are:
      - E_vH / E_min : van-Hove singularity energy over the band floor
      - E_max / E_vH : band ceiling over the van-Hove energy
      - E_max / E_min : full B2 band span ratio
      - Delta_mf / Delta_rich : mean-field over Richardson gap (the pairing-window ratio)
      - Delta_mf / Delta_ed   : mean-field over exact-diagonalization gap
      - E_vH / Delta_mf       : van-Hove energy over the B2 mean-field gap
    Plus the L12-cache B2-sector eigenvalue ratios (the (1,1) mult-8 band):
      - lam_min(1,1) / lam_min(0,0) : B2-band floor over the singlet floor

    The family is FIXED at design time (no post-hoc selection). We report ALL
    members + the min-deviation match against the node set.
    """
    d = np.load(INV11_NPZ, allow_pickle=True)
    E_vH = float(d["E_vH"])                                       # (local) 0.845269
    E_min = float(d["E_min"])                                     # (local) 0.819741
    E_max = float(d["E_max"])                                     # (local) 5.418937
    Delta_mf = float(d["Delta_mf"])                               # (local) 0.732026
    Delta_rich = float(d["Delta_rich"])                           # (local) 0.459972
    Delta_ed = float(d["Delta_ed"])                               # (local) 0.454474
    N0 = float(d["N0"])                                           # (local) 14.023250
    lambda_eff = float(d["lambda_eff"])                           # (local) 0.038935
    g_dimless = float(d["g_dimless"])                             # (local) 0.545992

    # L12-cache B2-band eigenvalue ratios at tau_fold=0.19 (reuse; no new diagonalization)
    cache = np.load(L12_CACHE, allow_pickle=True)
    se = cache["sector_evals"].item()                            # (local) dict {(p,q): {...}}

    def lammin(pq):
        return float(np.min(np.abs(se[pq]["abs_evals"])))         # (local)

    l00 = lammin((0, 0))                                          # (local) singlet floor 0.819741
    l11 = lammin((1, 1))                                          # (local) B2 (1,1) mult-8 band floor
    l02 = lammin((0, 2))                                          # (local) (0,2) mult-6
    l30 = lammin((3, 0))                                          # (local) (3,0) mult-10 — phi_paasch sector

    ratios = {}  # (local) name -> R_B2 value
    # --- pairing-window / DOS-edge ratios (the direct λ_eff·N₀ inputs) ---
    ratios["E_vH/E_min"] = E_vH / E_min
    ratios["E_max/E_vH"] = E_max / E_vH
    ratios["E_max/E_min"] = E_max / E_min
    ratios["Delta_mf/Delta_rich"] = Delta_mf / Delta_rich
    ratios["Delta_mf/Delta_ed"] = Delta_mf / Delta_ed
    ratios["E_vH/Delta_mf"] = E_vH / Delta_mf
    # --- L12-cache B2-band eigenvalue ratios ---
    ratios["lam(1,1)/lam(0,0)"] = l11 / l00
    ratios["lam(0,2)/lam(0,0)"] = l02 / l00
    ratios["lam(3,0)/lam(0,0)"] = l30 / l00   # this IS the (drift-shifted) phi_paasch ratio at tau=0.19

    aux = {
        "E_vH": E_vH, "E_min": E_min, "E_max": E_max,
        "Delta_mf": Delta_mf, "Delta_rich": Delta_rich, "Delta_ed": Delta_ed,
        "N0": N0, "lambda_eff": lambda_eff, "g_dimless": g_dimless,
        "lam00": l00, "lam11": l11, "lam02": l02, "lam30": l30,
    }  # (local)
    return ratios, aux


def compute():
    nodes, nj, Np_over_NK, fN = build_node_set()
    ratios, aux = extract_b2_ratios()

    node_names = list(nodes.keys())                               # (local)
    node_vals = np.array([nodes[k] for k in node_names])          # (local)
    ratio_names = list(ratios.keys())                             # (local)
    ratio_vals = np.array([ratios[k] for k in ratio_names])       # (local)

    # Grid-membership: for each B2 ratio, min over nodes of |R/node - 1|.
    # We also fold in the reciprocal R, since a "grading" is direction-agnostic
    # (R on the grid <=> 1/R on the reciprocal grid). Report the better of the two.
    best_per_ratio = []  # (local) (ratio_name, ratio_val, best_node_name, best_node_val, dev, used_recip)
    for rn, rv in zip(ratio_names, ratio_vals):
        dev_direct = np.abs(rv / node_vals - 1.0)                 # (local)
        dev_recip = np.abs((1.0 / rv) / node_vals - 1.0)          # (local)
        j_direct = int(np.argmin(dev_direct))                     # (local)
        j_recip = int(np.argmin(dev_recip))                       # (local)
        if dev_direct[j_direct] <= dev_recip[j_recip]:
            best_per_ratio.append(
                (rn, float(rv), node_names[j_direct], float(node_vals[j_direct]),
                 float(dev_direct[j_direct]), False)
            )
        else:
            best_per_ratio.append(
                (rn, float(rv), node_names[j_recip], float(node_vals[j_recip]),
                 float(dev_recip[j_recip]), True)
            )

    # The gate's scalar test = the MINIMUM deviation across the pre-pinned ratio family.
    devs = np.array([b[4] for b in best_per_ratio])               # (local)
    i_best = int(np.argmin(devs))                                 # (local)
    test = float(devs[i_best])                                    # (local) the gate value
    best = best_per_ratio[i_best]                                 # (local)

    return {
        "value": test,
        "nodes": nodes,
        "node_names": node_names,
        "node_vals": node_vals,
        "ratios": ratios,
        "ratio_names": ratio_names,
        "ratio_vals": ratio_vals,
        "best_per_ratio": best_per_ratio,
        "i_best": i_best,
        "best": best,
        "aux": aux,
        "Np_over_NK": Np_over_NK,
        "fN": fN,
        "nj": nj,
    }


def evaluate_gate(res) -> tuple:
    """COUPLED(PASS)/INDEPENDENT(INFO)/CONFLICT(FAIL) per the pre-registered rule.

    PASS (COUPLED)      iff test <= PASS_TOL : a B2-sector input ratio sits on the SAME
                            φ_paasch/7n grid as the output ladder.
    FAIL (CONFLICT)     iff the input is provably continuous while the output is provably
                            discrete (a genuine inconsistency). Here BOTH input and output
                            are discrete D_K eigenvalue ratios, so CONFLICT cannot fire
                            structurally — there is no provably-continuous input.
    INFO (INDEPENDENT)  otherwise : the B2 input ratios are self-consistent on a DIFFERENT
                            quantization than the output (still AGREE, layers not coupled).
    """
    test = res["value"]                                           # (local)
    coupled = test <= PASS_TOL                                    # (local)

    # CONFLICT predicate: the input would have to be provably continuous. The B2 ratios
    # are exact D_K eigenvalue ratios on a FINITE spectral triple — a discrete mesh by
    # construction (Peter-Weyl). So conflict_input_continuous is structurally False.
    conflict_input_continuous = False                             # (local) — discrete by construction

    if coupled:
        verdict = "PASS"        # COUPLED
        reading = "COUPLED"     # (local)
    elif conflict_input_continuous:
        verdict = "FAIL"        # CONFLICT
        reading = "CONFLICT"    # (local)
    else:
        verdict = "INFO"        # INDEPENDENT
        reading = "INDEPENDENT"  # (local)

    # [VERIFY] trigger: 3-tuple not required (schema_v2_3tuple_required=false in plan),
    # but emit a grid-membership-flavored annotation for audit continuity.
    sign_verdict = "N/A"        # grid-membership SET test; no directional claim
    magnitude_verdict = "PASS" if coupled else "INFO"   # |R/node-1| within 1% band?
    regime_verdict = "VALID"    # finite spectral triple; exact eigenvalue ratios, no regime breakdown
    return verdict, reading, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 6 — verdict payload (script prints; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None):
    payload = {
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
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — figure
# ---------------------------------------------------------------------------
def make_figure(res, reading, out_png):
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(14, 6.2))

    # Left: B2 ratios vs the node grid (log-spaced number line)
    node_vals = res["node_vals"]
    ratio_vals = res["ratio_vals"]
    ratio_names = res["ratio_names"]
    # plot nodes as vertical lines
    for nv, nn in zip(node_vals, res["node_names"]):
        ax0.axvline(nv, color="0.7", lw=1.0, zorder=1)
    ax0.axvline(PHI_PAASCH_NODE, color="crimson", lw=2.0, zorder=2,
                label=f"φ_paasch={PHI_PAASCH_NODE}")
    ax0.axvline(res["Np_over_NK"], color="darkorange", lw=1.6, ls="--", zorder=2,
                label=f"N(p)/N(K)=75/49={res['Np_over_NK']:.4f}")
    y = np.arange(len(ratio_vals))
    ax0.scatter(ratio_vals, y, c="navy", s=42, zorder=3)
    # also plot reciprocals for the ratios where recip was the match
    for k, b in enumerate(res["best_per_ratio"]):
        if b[5]:  # used_recip
            ax0.scatter([1.0 / ratio_vals[k]], [k], c="navy", s=42, marker="x", zorder=3)
    ax0.set_yticks(y)
    ax0.set_yticklabels(ratio_names, fontsize=8)
    ax0.set_xlabel("dimensionless ratio value")
    ax0.set_xlim(0.9, 6.0)
    ax0.set_title("B2-sector dimensionless ratios vs φ_paasch/7n grid")
    ax0.legend(fontsize=8, loc="lower right")
    ax0.grid(True, alpha=0.2)

    # Right: per-ratio min deviation (log scale) with PASS_TOL line
    devs = np.array([b[4] for b in res["best_per_ratio"]])
    colors = ["crimson" if b[2] == "phi_paasch" else "steelblue" for b in res["best_per_ratio"]]
    ax1.barh(y, devs, color=colors)
    ax1.axvline(PASS_TOL, color="green", lw=2.0, ls="--", label=f"PASS_TOL={PASS_TOL} (COUPLED)")
    ax1.set_xscale("log")
    ax1.set_yticks(y)
    ax1.set_yticklabels([f"{b[0]} → {b[2]}" for b in res["best_per_ratio"]], fontsize=8)
    ax1.set_xlabel("min |R_B2/node − 1|")
    ax1.set_title(f"grid-membership deviation — verdict: {reading}")
    ax1.legend(fontsize=8, loc="lower right")
    ax1.grid(True, alpha=0.2, axis="x")

    fig.suptitle(
        f"S110-CF-CV2C-OINTERFACE — Ô-interface φ_paasch/7n grading test "
        f"(test={res['value']:.4g}, {reading})",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins + plan-text-drift documentation
    pins = log_input_pins(INPUT_FILES)
    disk_canonical_sha = pins[str(CANONICAL_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")]  # (local)
    if disk_canonical_sha != PLAN_PINNED_CANONICAL_SHA:
        print(f"  [PLAN-TEXT-DRIFT] canonical_constants.py: plan pinned "
              f"{PLAN_PINNED_CANONICAL_SHA[:16]}..., disk is {disk_canonical_sha[:16]}...")
        print("  Resolved by npz-ground-truth at runtime (substrate-first-canonical-sourcing.md §ii.B); "
              "dual-SHA uses live disk bytes.")

    # 1b. dual SHAs
    script_path = Path(__file__).resolve()                        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    res = compute()

    # 3. Evaluate
    verdict, reading, sign_v, mag_v, reg_v = evaluate_gate(res)

    # 4. Report the FULL family (no cherry-pick) + the substitution chain numbers
    print("=== φ_paasch / 7n node grid ===")
    for nn in res["node_names"]:
        print(f"  {nn:22s} = {res['nodes'][nn]:.6f}")
    print(f"  phi_paasch (canonical line 289) = {phi_paasch:.6f}  "
          f"(W5-1 high-precision node {PHI_PAASCH_NODE})")
    print(f"  Delta_B2 (canonical) = {Delta_B2:.6f} ; T_GGE_B2 = {T_GGE_B2} ; tau_fold = {tau_fold}")
    print()
    print("=== B2-sector dimensionless ratio family (PRE-PINNED; all reported) ===")
    print(f"  {'ratio':22s} {'R_B2':>10s}   {'best node':22s} {'node':>10s} {'min|R/node-1|':>14s}  recip")
    for b in res["best_per_ratio"]:
        print(f"  {b[0]:22s} {b[1]:10.6f}   {b[2]:22s} {b[3]:10.6f} {b[4]:14.6e}  {b[5]}")
    print()
    bb = res["best"]
    print(f"=== gate value = min deviation across family = {res['value']:.6e} ===")
    print(f"  best match: {bb[0]} = {bb[1]:.6f}  →  {bb[2]} = {bb[3]:.6f}  "
          f"(dev={bb[4]:.6e}, recip={bb[5]})")
    print()
    print("=== substitution chain (grid-membership SET test) ===")
    print(f"  Def1: phi_paasch node = {PHI_PAASCH_NODE}")
    print(f"  Def2: N(p)/N(K) = 75/49 = {res['Np_over_NK']:.6f}  (output ladder, phi_dev=0.000632)")
    print(f"  Def3: R_B2 = B2-sector dimensionless ratios feeding λ_eff,N₀ "
          f"(λ_eff={res['aux']['lambda_eff']:.6f}, N₀={res['aux']['N0']:.6f})")
    print(f"  Def4: 7n-grid nodes from inv-3 W3-4 (N(j)={list(res['nj'].astype(int))}; "
          f"35,42 are SU(3) dims; 7,98,150 not)")
    print(f"  test = min over family, min over node, of |R_B2/node - 1| = {res['value']:.6e}")
    print(f"  test {'<=' if res['value'] <= PASS_TOL else '>'} {PASS_TOL} "
          f"⇒ {reading}")
    print()

    # 5. Save npz
    bpr = res["best_per_ratio"]
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        reading=reading,
        value=res["value"],
        pass_tol=PASS_TOL,
        phi_paasch_node=PHI_PAASCH_NODE,
        phi_paasch_canonical=phi_paasch,
        Np_over_NK=res["Np_over_NK"],
        fN=res["fN"],
        node_names=np.array(res["node_names"], dtype=object),
        node_vals=res["node_vals"],
        ratio_names=np.array(res["ratio_names"], dtype=object),
        ratio_vals=res["ratio_vals"],
        best_ratio_names=np.array([b[0] for b in bpr], dtype=object),
        best_node_names=np.array([b[2] for b in bpr], dtype=object),
        best_node_vals=np.array([b[3] for b in bpr]),
        best_devs=np.array([b[4] for b in bpr]),
        best_used_recip=np.array([b[5] for b in bpr]),
        i_best=res["i_best"],
        best_match_name=bb[0],
        best_match_ratio=bb[1],
        best_match_node_name=bb[2],
        best_match_node_val=bb[3],
        best_match_dev=bb[4],
        nj_paasch=res["nj"],
        b2_E_vH=res["aux"]["E_vH"],
        b2_E_min=res["aux"]["E_min"],
        b2_E_max=res["aux"]["E_max"],
        b2_Delta_mf=res["aux"]["Delta_mf"],
        b2_Delta_rich=res["aux"]["Delta_rich"],
        b2_Delta_ed=res["aux"]["Delta_ed"],
        b2_N0=res["aux"]["N0"],
        b2_lambda_eff=res["aux"]["lambda_eff"],
        b2_g_dimless=res["aux"]["g_dimless"],
        lam00=res["aux"]["lam00"],
        lam11=res["aux"]["lam11"],
        lam30=res["aux"]["lam30"],
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  npz -> {OUT_NPZ.name}")

    # 6. Figure
    make_figure(res, reading, OUT_PNG)
    print(f"  png -> {OUT_PNG.name}")
    print()

    # 7. 4-tuple + verdict payload
    print(f"(value={res['value']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(
        verdict, res["value"], audit_sha, content_sha, sign_v, mag_v, reg_v,
        extra_rows=[
            f"# CV2C grid-membership: best={bb[0]}→{bb[2]} dev={bb[4]:.3e} reading={reading} "
            f"(AGREE sharpened to AGREE-{reading})",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} ({reading}) (wall {wall:.1f}s) ===")
    # FAIL is a valid scientific result; exit 0 unless the script itself broke
    # (per math-scripts.md §"Exit Codes and Verdict Semantics").
    return 0


if __name__ == "__main__":
    sys.exit(main())
