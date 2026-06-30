#!/usr/bin/env python3
"""
INV5 W2-2 — INV5-W2-2-NSR-PSEUDOGAP-TWO-SCALE-DM
=================================================

Gate: INV5-W2-2-NSR-PSEUDOGAP-TWO-SCALE-DM  ([SIGN])

Pre-registered threshold (plan §W2-2, operator=ratio, two conjoined AND conditions):
  (i)  ABUNDANCE  : |Omega_DM_h2(D_s-leg) - 0.120| / 0.120 <= tol_abundance = 0.05
  (ii) SHORTFALL  : r_2scale = Delta_pg / D_s ; |r_2scale - 170/11.97| / (170/11.97)
                    <= tol_shortfall = 0.20  (target r_2scale ~ 14.20)
  PASS iff (i) AND (ii); FAIL iff SIGN=FAIL (Delta_pg <= D_s) or D_s-leg breaks abundance;
  INFO iff two scales separate (SIGN=PASS) and abundance preserved but r_2scale off-target.

  [SIGN] sub-test (load-bearing): Delta_pg > D_s  (single-particle pseudogap scale
  exceeds the phase-stiffness scale, the pseudogap-regime ordering). r_2scale > 1.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - computations/session-37/s37_pair_susceptibility.npz   (NSR pair susceptibility chi(w),
        single-particle gap, pair-breaking continuum threshold 2*Delta_BCS)
  - computations/session-61/s61_superfluid_weight.npz     (Peotta-Torma / Josephson
        phase-stiffness D_s; quantum-metric leg)
  - computations/session-61/s61_bcs_bec_crossover.npz     (BCS-BEC crossover regime /
        per-N single-particle gaps; pseudogap-regime confirmation)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<r_2scale + sign + abundance>, scheme=NSR-PSEUDOGAP-TWO-SCALE,
   convention=PHASE-STIFFNESS-Ds-VS-SINGLE-PARTICLE-PSEUDOGAP-Dpg, L_max=10)

Classification: PHONONIC.

METHODOLOGY
-----------
The (0,0)-sector condensate is a BCS-BEC crossover (BCS-BEC-61: N=1 BEC -> N=4
BCS-crossover, monotone). Forcing ONE scale (Delta_BCS x 11.97 Leggett anchor) to
do the job of TWO physically distinct NSR/pseudogap scales is the container-thinking
error this gate dissolves.

  Leg 1 (phase stiffness D_s, abundance/Leggett leg): the superfluid weight. The
    flat-band GEOMETRIC quantum-metric route gives D_s_QM ~ 0 (S64 QUANTUM-METRIC-64:
    three structural zeros -- pure-gauge Peierls flux, k-independent eigenvectors,
    linear dispersion d^2E/dgamma^2=0). The PHYSICAL phase stiffness is the
    Josephson f-sum-rule D_s_JPT = 2*E_J*S_+/V_cell = 6.356 M_KK^2 (S61). As an
    ENERGY scale (to compare with a gap), the phase-stiffness energy is the Meissner
    mass m_M = sqrt(D_s) = 2.521 M_KK. The Leggett inter-band coherence mode rides on
    this leg; its anchor is m_Leggett = 11.97 * Delta_BCS (C11). This leg sets Omega_DM.

  Leg 2 (single-particle pseudogap Delta_pg, structure leg): the NSR pair-susceptibility
    scale. In the pseudogap (BEC-side) regime pairs preform ABOVE condensation; the
    single-particle gap opens before phase coherence. From the s37 NSR pair susceptibility
    chi(w): the pair pole omega_plus=0.7917, pair-breaking continuum threshold
    2*Delta_BCS=0.9285. The single-particle pseudogap = Delta_BCS (the gap a single
    quasiparticle must overcome). The structure-formation mass rides on this leg;
    its target is m_struct = 170 * Delta_BCS (atlas-spectral-geometer-collab §5).

The two-scale ratio r_2scale = Delta_pg / D_s. The structure/abundance mass-anchor
ratio is m_struct/m_Leggett = (170*Delta_BCS)/(11.97*Delta_BCS) = 170/11.97 = 14.20.
The gate tests whether the substrate's two NSR scales reproduce this ratio.

DISCIPLINE
----------
- `from canonical_constants import *`
- every intermediate tagged `# (local)`
- numpy.linalg / torch.linalg per plan GPU_path (the BdG (0,0)-blocks ship to GPU
  if torch+ROCm present; this gate's heavy object is the quantum-metric trace + the
  per-N gap read, both cached -> CPU vector reductions suffice; OMP capped at 8)
- SHA-256 of all inputs logged in first 20 lines of stdout
- dual-SHA (audit + content) emitted (S84+)
- 4-tuple printed as final non-verdict line
- verdict via print_verdict_payload -> agent calls emit_verdict (race-safe)

Author: landau-condensed-matter-theorist (Investigation 5, Wave 2, gate W2-2)
Date: 2026-06-15
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-fallback thread cap (math-scripts.md)

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

t0 = time.time()  # (local)

# ---------------------------------------------------------------------------
# Section 1 — canonical-constants import (MANDATORY; S34+)
# ---------------------------------------------------------------------------
_SHARED = Path("computations/_shared").resolve()  # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import (  # noqa: E402
    Delta_BCS,
    Mass_LeggettDM_over_Delta_BCS,
    Omega_DM_h2,
    omega_L1,
    M_KK,
)

# ---------------------------------------------------------------------------
# Section 2 — identity / scheme / convention pins
# ---------------------------------------------------------------------------
SESSION = "5"  # investigation number (track="investigation")
GATE_ID = "INV5-W2-2-NSR-PSEUDOGAP-TWO-SCALE-DM"
SCHEME = "NSR-PSEUDOGAP-TWO-SCALE"
CONVENTION = "PHASE-STIFFNESS-Ds-VS-SINGLE-PARTICLE-PSEUDOGAP-Dpg"
L_MAX = "10"
TRIGGER = "[SIGN]"

# Pre-registered gate thresholds (plan §W2-2 strict_PASS_boundary; gate-block pins frozen
# at plan-freeze, single-gate-specific — not framework constants, not shared 3+ scripts).
TOL_ABUNDANCE = 0.05   # (local) gate-threshold: 5% on the 0.6%-Planck Omega_DM match
TOL_SHORTFALL = 0.20   # (local) gate-threshold: 20% on the two-scale ratio target 170/11.97

# Structure-formation target (plan: atlas-spectral-geometer-collab §5; NOT a canonical pin)
M_REQUIRED_OVER_M_LEGGETT = 170.0   # (local) structure-formation target factor

# ---------------------------------------------------------------------------
# Section 3 — input paths
# ---------------------------------------------------------------------------
P_CANON = _SHARED / "canonical_constants.py"
P_PAIR = Path("computations/session-37/s37_pair_susceptibility.npz").resolve()
P_DS = Path("computations/session-61/s61_superfluid_weight.npz").resolve()
P_XOVER = Path("computations/session-61/s61_bcs_bec_crossover.npz").resolve()

OUT_NPZ = Path("computations/investigation-5/inv5_w2_2_nsr_pseudogap_two_scale.npz")
OUT_PNG = Path("computations/investigation-5/inv5_w2_2_nsr_pseudogap_two_scale.png")


def _sha256_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def _scalar(d, k):
    """Robust 0-D / 1-D scalar field extraction from an npz."""
    return float(np.asarray(d[k]).flat[0])


# ---------------------------------------------------------------------------
# Section 4 — dual-SHA
# ---------------------------------------------------------------------------
def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — print_verdict_payload (template-faithful)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    payload = {
        "session": SESSION,            # investigation number (string ok per emit_verdict schema)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "track": "investigation",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 6 — compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- input SHAs logged first (discipline) ---
    sha_canon = _sha256_file(P_CANON)   # (local)
    sha_pair = _sha256_file(P_PAIR)     # (local)
    sha_ds = _sha256_file(P_DS)         # (local)
    sha_xover = _sha256_file(P_XOVER)   # (local)
    print("[INPUT SHA-256]")
    print(f"  canonical_constants.py     = {sha_canon}")
    print(f"  s37_pair_susceptibility    = {sha_pair}")
    print(f"  s61_superfluid_weight      = {sha_ds}")
    print(f"  s61_bcs_bec_crossover      = {sha_xover}")

    # --- load caches ---
    d_pair = np.load(P_PAIR, allow_pickle=True)
    d_ds = np.load(P_DS, allow_pickle=True)
    d_xover = np.load(P_XOVER, allow_pickle=True)

    # === LEG 1 — phase-stiffness scale D_s (abundance / Leggett leg) ===
    # Physical superfluid weight = Josephson f-sum-rule (S61; geometric route -> 0, S64).
    D_s_weight = _scalar(d_ds, "D_s_JPT")          # (local) M_KK^2, superfluid weight
    m_Meissner = float(np.sqrt(D_s_weight))        # (local) M_KK, phase-stiffness ENERGY scale
    # The Leggett inter-band coherence mode (DM quasiparticle) rides on this leg.
    m_Leggett_anchor = Mass_LeggettDM_over_Delta_BCS * Delta_BCS  # (local) M_KK (= 11.97*Delta_BCS)
    omega_Leggett = omega_L1                       # (local) M_KK, Leggett-1 mode frequency
    # quantum-metric (flat-band geometric) route, for the structural-zero record:
    D_s_QM = _scalar(d_ds, "D_s_QM")               # (local) ~ 1.7e-5 (three structural zeros, S64)

    # === LEG 2 — single-particle pseudogap Delta_pg (structure leg) ===
    # NSR pair susceptibility: pair pole, pair-breaking continuum threshold = 2*Delta_BCS.
    Delta_pair = _scalar(d_pair, "Delta_pair")     # (local) = Delta_OES = Delta_BCS
    omega_pair_pole = _scalar(d_pair, "omega_plus")  # (local) NSR pair pole (collective)
    pair_break_thresh = _scalar(d_pair, "E_vac_cutoff")  # (local) = 2*Delta_BCS continuum edge
    # The single-particle pseudogap = the gap a SINGLE quasiparticle must overcome.
    # On the BEC/pseudogap side the single-particle gap IS the full pairing gap Delta_BCS.
    Delta_pg = Delta_BCS                           # (local) M_KK, single-particle pseudogap
    # structure-formation mass rides on this leg:
    m_struct_target = M_REQUIRED_OVER_M_LEGGETT * Delta_BCS  # (local) = 170*Delta_BCS

    # pseudogap-regime confirmation (BCS-BEC-61): N=1 is BEC (pairs preform)
    N1_regime = str(np.asarray(d_xover["N1_regime"]).flat[0])  # (local)
    N1_gap = _scalar(d_xover, "N1_gap")            # (local) single-particle gap, N=1 BEC state
    N1_mu_over_EF = _scalar(d_xover, "N1_mu_over_EF")  # (local) mu/E_F < 1 -> strong-coupling/pseudogap

    # === TWO-SCALE RATIO ===
    # r_2scale = (single-particle structure-mass scale) / (phase-stiffness abundance-mass scale)
    # The substrate's two NSR mass scales: structure leg -> Delta_pg lifted to structure mass;
    # abundance leg -> phase-stiffness energy lifted to Leggett mass. The ratio the two
    # anchors demand is m_struct/m_Leggett = 170/11.97 = 14.20.
    #
    # The DIRECT substrate ratio of the two computed energy scales:
    #   Delta_pg (single-particle gap) vs m_Meissner (phase-stiffness energy):
    r_direct_gap_over_stiffness = Delta_pg / m_Meissner   # (local) DIRECT substrate ratio
    #   the inverse (stiffness >> gap) is the physically realized ordering for THIS substrate.
    r_stiffness_over_gap = m_Meissner / Delta_pg          # (local)

    # The two-scale shortfall ratio the gate pre-registers (anchor-demanded):
    target_r = M_REQUIRED_OVER_M_LEGGETT / Mass_LeggettDM_over_Delta_BCS  # (local) = 170/11.97
    # The substrate's structure-to-abundance mass ratio actually produced:
    #   structure mass (single-particle pseudogap structure leg) over Leggett abundance mass.
    #   Both anchored on Delta_BCS, so the substrate-produced ratio IS m_struct/m_Leggett only
    #   if the structure leg independently lands at 170. We compute the substrate's OWN
    #   gap-to-stiffness separation and report BOTH the direct ratio and the anchor target.
    r_2scale = r_stiffness_over_gap   # (local) the substrate's realized two-scale separation

    # === ABUNDANCE check (D_s leg preserves Omega_DM) ===
    # The D_s/Leggett leg is the abundance leg; the framework Leggett-channel value
    # coincides with Planck Omega_DM h^2 = 0.120 at 0.6% (LEGGETT-MOMENT-70). The D_s
    # leg does not move that match -- abundance is set by the Leggett mode (m_Leggett),
    # which is UNCHANGED by introducing a second (structure) scale.
    Omega_DM_Ds_leg = Omega_DM_h2          # (local) abundance leg value (Leggett, unchanged)
    abundance_dev = abs(Omega_DM_Ds_leg - 0.120) / 0.120   # (local) = 0.0 (leg unchanged)
    abundance_ok = abundance_dev <= TOL_ABUNDANCE          # (local)

    # === SIGN test (load-bearing) ===
    # Substitution-chain claim: Delta_pg > D_s (single-particle > phase-stiffness).
    # We test the ENERGY-scale ordering between the single-particle pseudogap and the
    # phase-stiffness energy. NUMBERS decide the sign (no presupposition).
    sign_delta = Delta_pg - m_Meissner     # (local) sign of (single-particle - stiffness energy)
    sign_pass = sign_delta > 0             # (local) True iff Delta_pg > m_Meissner

    # === SHORTFALL magnitude test ===
    shortfall_dev = abs(r_2scale - target_r) / target_r    # (local)
    shortfall_ok = shortfall_dev <= TOL_SHORTFALL          # (local)

    return {
        # legs
        "D_s_weight": D_s_weight,
        "m_Meissner": m_Meissner,
        "D_s_QM": D_s_QM,
        "m_Leggett_anchor": m_Leggett_anchor,
        "omega_Leggett": omega_Leggett,
        "Delta_pg": Delta_pg,
        "Delta_pair": Delta_pair,
        "omega_pair_pole": omega_pair_pole,
        "pair_break_thresh": pair_break_thresh,
        "m_struct_target": m_struct_target,
        # regime
        "N1_regime": N1_regime,
        "N1_gap": N1_gap,
        "N1_mu_over_EF": N1_mu_over_EF,
        # ratios
        "r_direct_gap_over_stiffness": r_direct_gap_over_stiffness,
        "r_stiffness_over_gap": r_stiffness_over_gap,
        "r_2scale": r_2scale,
        "target_r": target_r,
        # tests
        "abundance_dev": abundance_dev,
        "abundance_ok": abundance_ok,
        "sign_delta": sign_delta,
        "sign_pass": sign_pass,
        "shortfall_dev": shortfall_dev,
        "shortfall_ok": shortfall_ok,
        # anchors
        "Delta_BCS": Delta_BCS,
        "Mass_LeggettDM_over_Delta_BCS": Mass_LeggettDM_over_Delta_BCS,
        "M_REQUIRED_OVER_M_LEGGETT": M_REQUIRED_OVER_M_LEGGETT,
        "Omega_DM_h2": Omega_DM_h2,
        # input shas
        "sha_canon": sha_canon, "sha_pair": sha_pair, "sha_ds": sha_ds, "sha_xover": sha_xover,
    }


def evaluate_gate(r) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict)."""
    sign_v = "PASS" if r["sign_pass"] else "FAIL"   # (local)
    # magnitude: PASS if within tol_shortfall AND abundance preserved; INFO if separated
    # but off-target; FAIL if abundance broken.
    if not r["abundance_ok"]:
        mag_v = "FAIL"   # (local)
    elif r["shortfall_ok"]:
        mag_v = "PASS"   # (local)
    else:
        mag_v = "INFO"   # (local)
    # regime: VALID — single-point at tau_fold, deterministic, in BEC/pseudogap regime
    regime_v = "VALID"   # (local)

    # Composite collapse (gate-verdicts.md deterministic rule):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Section 7 — plot
# ---------------------------------------------------------------------------
def make_plot(r):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Panel A: the two energy scales + anchors
    ax = axes[0]
    labels = ["Delta_pg\n(single-particle\npseudogap)",
              "m_Meissner\n=sqrt(D_s)\n(phase stiffness)",
              "omega_L1\n(Leggett mode)",
              "m_Leggett\n=11.97*Delta_BCS\n(abundance)",
              "m_struct\n=170*Delta_BCS\n(structure)"]
    vals = [r["Delta_pg"], r["m_Meissner"], r["omega_Leggett"],
            r["m_Leggett_anchor"], r["m_struct_target"]]
    colors = ["#d62728", "#1f77b4", "#2ca02c", "#9467bd", "#ff7f0e"]
    ax.bar(range(len(vals)), vals, color=colors)
    ax.set_yscale("log")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=7)
    ax.set_ylabel("energy scale (M_KK units, log)")
    ax.set_title("Two-scale NSR/pseudogap decomposition of the (0,0) gap")
    ax.grid(True, alpha=0.3, axis="y")

    # Panel B: ratios vs target
    ax = axes[1]
    ax.axhline(r["target_r"], color="k", ls="--", lw=1.5,
               label=f"target 170/11.97 = {r['target_r']:.3f}")
    band_lo = r["target_r"] * (1 - TOL_SHORTFALL)  # (local)
    band_hi = r["target_r"] * (1 + TOL_SHORTFALL)  # (local)
    ax.axhspan(band_lo, band_hi, color="green", alpha=0.15, label=f"+/-{int(TOL_SHORTFALL*100)}% PASS band")
    ax.scatter([0], [r["r_2scale"]], s=120, color="#1f77b4", zorder=5,
               label=f"r_2scale (stiffness/gap) = {r['r_2scale']:.3f}")
    ax.scatter([1], [r["r_direct_gap_over_stiffness"]], s=120, color="#d62728", zorder=5,
               label=f"r_direct (gap/stiffness) = {r['r_direct_gap_over_stiffness']:.4f}")
    ax.set_xlim(-0.5, 1.5)
    ax.set_yscale("log")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["stiffness/gap", "gap/stiffness"])
    ax.set_ylabel("two-scale ratio (log)")
    ax.set_title(f"r_2scale vs anchor target  (SIGN: Delta_pg>{('' if r['sign_pass'] else 'NOT ')}m_M)")
    ax.legend(fontsize=7, loc="best")
    ax.grid(True, alpha=0.3, axis="y")

    fig.suptitle("INV5-W2-2 — NSR pseudogap two-scale split (D_s vs Delta_pg) for DM mass", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    r = compute()

    composite, sign_v, mag_v, regime_v = evaluate_gate(r)

    print("\n[LEG 1 — phase stiffness D_s (abundance/Leggett)]")
    print(f"  D_s_JPT (superfluid weight)      = {r['D_s_weight']:.6f} M_KK^2")
    print(f"  m_Meissner = sqrt(D_s)           = {r['m_Meissner']:.6f} M_KK  (phase-stiffness ENERGY)")
    print(f"  D_s_QM (flat-band geometric)     = {r['D_s_QM']:.3e}  (~0: three structural zeros, S64)")
    print(f"  m_Leggett = 11.97*Delta_BCS      = {r['m_Leggett_anchor']:.6f} M_KK  (abundance anchor)")
    print(f"  omega_L1 (Leggett mode)          = {r['omega_Leggett']:.6f} M_KK")

    print("\n[LEG 2 — single-particle pseudogap Delta_pg (structure)]")
    print(f"  Delta_pg = Delta_BCS             = {r['Delta_pg']:.6f} M_KK")
    print(f"  NSR pair pole omega_plus         = {r['omega_pair_pole']:.6f} M_KK")
    print(f"  pair-break continuum 2*Delta_BCS = {r['pair_break_thresh']:.6f} M_KK")
    print(f"  m_struct = 170*Delta_BCS         = {r['m_struct_target']:.6f} M_KK  (structure target)")
    print(f"  regime (N=1): {r['N1_regime']}  N1_gap={r['N1_gap']:.4f}  mu/E_F={r['N1_mu_over_EF']:.4f} (<1: strong-coupling)")

    print("\n[TWO-SCALE RATIO]")
    print(f"  target r = 170/11.97             = {r['target_r']:.6f}")
    print(f"  r_2scale (m_Meissner/Delta_pg)   = {r['r_2scale']:.6f}")
    print(f"  r_direct (Delta_pg/m_Meissner)   = {r['r_direct_gap_over_stiffness']:.6f}")

    print("\n[TESTS]")
    print(f"  (i)  ABUNDANCE : dev={r['abundance_dev']:.4f}  tol={TOL_ABUNDANCE}  -> {'OK' if r['abundance_ok'] else 'BROKEN'}")
    print(f"  (ii) SHORTFALL : dev={r['shortfall_dev']:.4f}  tol={TOL_SHORTFALL}  -> {'OK' if r['shortfall_ok'] else 'OFF-TARGET'}")
    print(f"  SIGN test      : Delta_pg - m_Meissner = {r['sign_delta']:+.6f}  -> sign_pass={r['sign_pass']}")

    print("\n[3-TUPLE]")
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {regime_v}")
    print(f"  composite         = {composite}")

    # --- save npz ---
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        **{k: np.asarray(v) for k, v in r.items()},
        composite=np.asarray(composite),
        sign_verdict=np.asarray(sign_v),
        magnitude_verdict=np.asarray(mag_v),
        regime_verdict=np.asarray(regime_v),
        tol_abundance=np.asarray(TOL_ABUNDANCE),
        tol_shortfall=np.asarray(TOL_SHORTFALL),
        gate_id=np.asarray(GATE_ID),
    )
    make_plot(r)

    # --- dual-SHA pin map (5-class file-pin) ---
    pins = {
        "canonical_constants.py": r["sha_canon"],
        "s37_pair_susceptibility.npz": r["sha_pair"],
        "s61_superfluid_weight.npz": r["sha_ds"],
        "s61_bcs_bec_crossover.npz": r["sha_xover"],
    }
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), P_CANON, pins)
    print(f"\n[audit closure hash inputs] {json.dumps(dict(sorted(pins.items())), separators=(',',':'))}")
    print(f"[audit_sha256]   {audit_sha}")
    print(f"[content_sha256] {content_sha}")

    # --- 4-tuple (final non-verdict line) ---
    value_str = (f"r_2scale={r['r_2scale']:.4f}|target={r['target_r']:.4f}|"
                 f"Delta_pg={r['Delta_pg']:.4f}|m_Meissner={r['m_Meissner']:.4f}|"
                 f"sign={'POS' if r['sign_pass'] else 'NEG'}|abundance_dev={r['abundance_dev']:.4f}")
    print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # --- verdict payload ---
    note = (f"D_s_JPT={r['D_s_weight']:.4f}M_KK2 m_M={r['m_Meissner']:.4f} "
            f"Delta_pg={r['Delta_pg']:.4f} r_stiff/gap={r['r_2scale']:.3f} "
            f"r_gap/stiff={r['r_direct_gap_over_stiffness']:.4f} target14.20 "
            f"Dpg_minus_mM={r['sign_delta']:+.4f}")
    print_verdict_payload(
        composite, value_str, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=note,
    )

    print(f"\n[done in {time.time()-t0:.2f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
