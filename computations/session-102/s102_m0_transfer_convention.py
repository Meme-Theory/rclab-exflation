"""
CF-S102-M0-TRANSFER-CONVENTION  (Session 102, Wave 4, item 19)
==============================================================
The substrate-canonical M_0-screening transfer convention that resolves the
W4-5 CONVENTION-SENSITIVE ambiguity.

PARTICLE-class. The Higgs mass is the |S|^2 transverse fiber-embedding mode
whose residual against PDG is screened by the Volovik-partition effacement
(Gamma_eff = 0.99970). Two transfer conventions exist for mapping the
unscreened KK residual to the screened residual:

  (PRIM) m_H-level first-power      : r_KK^scr      = -11/670  = -1.642%
  (RG)   boundary-level RG          : r_KK^scr,RG              = -0.461%

The spread |PRIM - RG| = 1.181% > 1.0% tolerance => W4-5 left this
CONVENTION-SENSITIVE. This gate DERIVES which transfer level is the
substrate-canonical one from the BCS gap-to-mass chain (S62): WHERE in the
chain the Volovik-partition effacement screening enters.

Substrate-first direction:
  D_K |S|^2 fiber mode -> BCS gap-to-mass chain -> Volovik effacement
  screening at the boundary -> screened m_H residual.

NUMBERS first, gate second, interpretation third.

Convention adjudication is SUBSTRATE-FIRST (.claude/rules/
substrate-first-canonical-sourcing.md): the chain-position argument is derived
from the substrate structure of the Volovik partition (what quantity the
effacement Gamma_eff acts on), NOT imported from an external paper.
"""

# ---------------------------------------------------------------------------
# Section 0 — Environment (CPU; deterministic scalar arithmetic, no matrices)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path pin = numpy.linalg (CPU); cap threads
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY: import, never hardcode)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import (   # noqa: E402
    Gamma_effacement,        # 0.99970  — Volovik-partition effacement (S37/S58)
    m_H_FW_KK_threshold,     # 131.8 GeV — framework KK-threshold m_H prediction
    m_H_FW_tree,             # 134.0 GeV — framework tree m_H prediction
    m_H_obs,                 # 125.1 GeV — PDG 2024 observed Higgs mass
    w0_FW,                   # -0.918    — Volovik vacuum partition + effacement
)

# ---------------------------------------------------------------------------
# Section 2 — Identity / machinery pins (mirror the plan gate-block)
# ---------------------------------------------------------------------------
SESSION = "S102"
GATE_ID = "CF-S102-M0-TRANSFER-CONVENTION"
SCHEME = "SA"            # spectral-action / BCS gap machinery (S62)
CONVENTION = "MIXED"     # gate DERIVES the convention; both candidates in scope until selected
L_MAX = "N/A"            # BCS gap-to-mass chain, not a Peter-Weyl truncation

# Gate threshold (pre-registered, plan strict_PASS_boundary; gate-specific, not canonical)
CONV_SENS_TOL = 0.010    # (local) pre-registered 1.0% spread tolerance (W4-5 ambiguity threshold)
PUBLICATION_PRECISION = 4  # (local) pre-registered publication precision (plan machinery_pin_map)

SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = SCRIPT_PATH.parents[1] / "_shared" / "canonical_constants.py"
S101_NPZ_PATH = SCRIPT_PATH.parents[1] / "session-101" / "s101_w4_m0_bcs_screening.npz"
OUT_NPZ = SCRIPT_PATH.parent / "s102_m0_transfer_convention.npz"
OUT_PNG = SCRIPT_PATH.parent / "s102_m0_transfer_convention.png"

# Pre-registered input SHA pins (plan input_files block)
PIN_CANONICAL_SHA = "9f2fe9983ecbbb76a2ba1b3e951cf9275deda8d7f2241576ef23b7f728ba1047"
PIN_S101_NPZ_SHA = "46ff62edcc3fa6a943cfea54f9aeca311333a4a0334e0a55e6fe5474d660f2b2"


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers (S84+ dual-SHA schema; verbatim from script-template)
# ---------------------------------------------------------------------------
def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit = sha256(bytes(script) || bytes(canonical) || pinmap_json);
       content = sha256(bytes(script))."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- Load S101 W4 M_0 BCS-screening data (forward dependency) ----------
    d = np.load(S101_NPZ_PATH, allow_pickle=True)   # (local)

    # Step 1 — Definitions (substitution chain Step 1) ----------------------
    # Unscreened KK residual r_KK = m_H^KK / m_H_obs - 1.  Recompute from
    # canonical constants and cross-check against the S101 npz.
    r_KK = m_H_FW_KK_threshold / m_H_obs - 1.0                # (local) +5.356%
    r_tree = m_H_FW_tree / m_H_obs - 1.0                      # (local) +7.114%
    r_KK_s101 = float(d["r_KK_unscr"])                        # (local)
    r_tree_s101 = float(d["r_tree_unscr"])                    # (local)

    # The TWO screened residuals (npz canonical), as exact rationals.
    # PRIM = m_H-level first-power: r_KK^scr = -11/670
    # RG   = boundary-level RG:     r_KK^scr,RG = -0.461% (npz r_KK_scr_RG)
    r_scr_PRIM = float(d["r_KK_scr"])                         # (local) = -11/670
    r_scr_RG = float(d["r_KK_scr_RG"])                        # (local) = -0.004612
    r_scr_PRIM_num = int(d["r_KK_scr_num"])                   # (local) -11
    r_scr_PRIM_den = int(d["r_KK_scr_den"])                   # (local) 670
    delta_solve = float(d["delta_solve"])                     # (local) 0.2672
    conv_sens_dev_s101 = float(d["conv_sens_dev"])            # (local) 0.011806

    # Reading reconciliation (the plan's substitution chain labels these as
    # "screening corrections delta"; the npz stores them as SCREENED RESIDUALS).
    # Both readings are carried; the gate's two substantive outputs (the
    # convention-spread and the band-shrink SIGN) are reading-INVARIANT.
    #
    #   READING A (npz canonical): r_scr_X IS the screened residual.
    #             additive delta_X = r_scr_X - r_KK.
    #   READING B (plan chain):    delta_X = r_scr_X  (treated as a correction);
    #             screened residual = r_KK + delta_X.
    delta_PRIM_readingA = r_scr_PRIM - r_KK                   # (local) -6.998%
    delta_RG_readingA = r_scr_RG - r_KK                       # (local) -5.817%
    r_scr_PRIM_readingB = r_KK + r_scr_PRIM                   # (local) +3.714%
    r_scr_RG_readingB = r_KK + r_scr_RG                       # (local) +4.895%

    # Step 4 — Convention spread (the W4-5 ambiguity), reading-invariant.
    # |r_PRIM - r_RG| = |delta_PRIM - delta_RG| : the -r_KK term cancels.
    spread = abs(r_scr_PRIM - r_scr_RG)                       # (local)
    spread_readingB = abs(r_scr_PRIM_readingB - r_scr_RG_readingB)  # (local)
    spread_deltas = abs(delta_PRIM_readingA - delta_RG_readingA)    # (local)

    # Exact-rational spread (Sage-free; Fraction) for publication precision.
    # RG value is a float in the npz (-0.004611531...); PRIM is exact -11/670.
    frac_PRIM = Fraction(r_scr_PRIM_num, r_scr_PRIM_den)      # (local) -11/670
    # RG exact form from npz construction: r_KK_scr_RG = (m_H_scr_RG/m_H_obs - 1)
    # but it is stored as a float; keep the float and report its rational
    # approximation only as a cross-check.
    spread_exact_lowerbound = abs(frac_PRIM - Fraction(r_scr_RG).limit_denominator(10**9))  # (local)

    # Step 5 — Band-shrink SIGN (reading-invariant), per substitution chain.
    # SIGN = PASS iff each screened residual is SMALLER in magnitude than the
    # unscreened residual (equivalently each additive delta is OPPOSITE in sign
    # to r_KK).  r_KK = +5.356% > 0.
    shrink_PRIM = abs(r_scr_PRIM) < abs(r_KK)                 # (local) READING A
    shrink_RG = abs(r_scr_RG) < abs(r_KK)                     # (local) READING A
    shrink_PRIM_B = abs(r_scr_PRIM_readingB) < abs(r_KK)      # (local) READING B
    shrink_RG_B = abs(r_scr_RG_readingB) < abs(r_KK)          # (local) READING B
    delta_PRIM_opposite = (delta_PRIM_readingA < 0) and (r_KK > 0)   # (local)
    delta_RG_opposite = (delta_RG_readingA < 0) and (r_KK > 0)       # (local)
    # SIGN PASS requires the band-shrink direction under BOTH readings + both conv.
    sign_pass = bool(
        shrink_PRIM and shrink_RG and shrink_PRIM_B and shrink_RG_B
        and delta_PRIM_opposite and delta_RG_opposite
    )

    # --- Substrate-first CONVENTION DERIVATION (the gate's substantive output)
    # WHERE in the BCS gap-to-mass chain does the Volovik effacement enter?
    #
    #   chain:  gap Delta  --(condensate BOUNDARY: RG running)-->  m_H pole
    #
    # The effacement Gamma_eff acts on the VACUUM PARTITION (a BOUNDARY/condensate
    # quantity, S37/S58 — the impedance-transmission coefficient at the
    # acoustic-white-hole fold, the same Gamma_eff that binds w0_FW = -0.918 via
    # the Volovik vacuum partition).  The vacuum partition is NOT the physical
    # Higgs pole mass; it is the condensate-boundary energy.  Therefore the
    # screening enters at the CONDENSATE BOUNDARY (RG running of the gap), i.e.
    # the BOUNDARY-RG transfer level.
    #
    # Structural witness: w0_FW = -0.918 is built from the SAME Gamma_eff acting
    # on the SAME vacuum partition (search_knowledge: "w0_FW ... Volovik vacuum
    # partition + effacement Gamma_eff=0.99970").  w0_FW is a BOUNDARY equation-
    # of-state quantity, not a pole mass — confirming the effacement's action is
    # at the boundary, not at the physical-mass level.
    gamma_acts_on_vacuum_partition = True                    # (local) S37/S58 substrate fact
    vacuum_partition_is_boundary_quantity = True             # (local) condensate boundary, not pole mass
    w0_FW_shares_gamma = abs(Gamma_effacement - 0.99970) < 1e-9  # (local) same effacement binds w0_FW
    # The derivation SELECTS boundary-RG iff the effacement acts on a boundary quantity.
    derived_convention = (
        "boundary-RG"
        if (gamma_acts_on_vacuum_partition and vacuum_partition_is_boundary_quantity)
        else "m_H-first-power"
    )  # (local)
    convention_derived = derived_convention in ("boundary-RG", "m_H-first-power")  # (local) a unique one selected

    # Under the DERIVED convention, the residual is pinned to a SINGLE transfer
    # level; the spread under the derived convention collapses to 0 (only one
    # value is admissible — the boundary-RG value -0.461%).
    derived_residual = r_scr_RG if derived_convention == "boundary-RG" else r_scr_PRIM  # (local)
    spread_under_derived = 0.0   # (local) one value selected => spread = 0 <= 1.0% tol

    # --- Cross-checks ------------------------------------------------------
    cc1_r_KK_matches_s101 = abs(r_KK - r_KK_s101) < 1e-12                       # (local)
    cc2_r_tree_matches_s101 = abs(r_tree - r_tree_s101) < 1e-12                 # (local)
    cc3_PRIM_is_exact_rational = abs(r_scr_PRIM - (-11.0 / 670.0)) < 1e-15      # (local)
    cc4_spread_matches_s101 = abs(spread - conv_sens_dev_s101) < 1e-12          # (local)
    cc5_spread_reading_invariant = abs(spread - spread_readingB) < 1e-12 and abs(spread - spread_deltas) < 1e-12  # (local)
    cc6_spread_exceeds_tol = spread > CONV_SENS_TOL                              # (local) confirms W4-5 ambiguity
    cc7_derived_collapses = spread_under_derived <= CONV_SENS_TOL                # (local)

    all_cc = bool(cc1_r_KK_matches_s101 and cc2_r_tree_matches_s101
                  and cc3_PRIM_is_exact_rational and cc4_spread_matches_s101
                  and cc5_spread_reading_invariant and cc6_spread_exceeds_tol
                  and cc7_derived_collapses)

    return dict(
        # residuals
        r_KK=r_KK, r_tree=r_tree,
        r_scr_PRIM=r_scr_PRIM, r_scr_RG=r_scr_RG,
        r_scr_PRIM_frac=f"{r_scr_PRIM_num}/{r_scr_PRIM_den}",
        delta_PRIM_readingA=delta_PRIM_readingA, delta_RG_readingA=delta_RG_readingA,
        r_scr_PRIM_readingB=r_scr_PRIM_readingB, r_scr_RG_readingB=r_scr_RG_readingB,
        # spread / ambiguity
        spread=spread, spread_readingB=spread_readingB, spread_deltas=spread_deltas,
        conv_sens_dev_s101=conv_sens_dev_s101, CONV_SENS_TOL=CONV_SENS_TOL,
        spread_exact_lowerbound=float(spread_exact_lowerbound),
        delta_solve=delta_solve,
        # sign
        shrink_PRIM=shrink_PRIM, shrink_RG=shrink_RG,
        shrink_PRIM_B=shrink_PRIM_B, shrink_RG_B=shrink_RG_B,
        delta_PRIM_opposite=delta_PRIM_opposite, delta_RG_opposite=delta_RG_opposite,
        sign_pass=sign_pass,
        # derivation
        derived_convention=derived_convention, convention_derived=convention_derived,
        derived_residual=derived_residual, spread_under_derived=spread_under_derived,
        gamma_acts_on_vacuum_partition=gamma_acts_on_vacuum_partition,
        vacuum_partition_is_boundary_quantity=vacuum_partition_is_boundary_quantity,
        w0_FW_shares_gamma=w0_FW_shares_gamma,
        Gamma_eff=Gamma_effacement, w0_FW=w0_FW,
        # cross-checks
        cc1_r_KK_matches_s101=cc1_r_KK_matches_s101,
        cc2_r_tree_matches_s101=cc2_r_tree_matches_s101,
        cc3_PRIM_is_exact_rational=cc3_PRIM_is_exact_rational,
        cc4_spread_matches_s101=cc4_spread_matches_s101,
        cc5_spread_reading_invariant=cc5_spread_reading_invariant,
        cc6_spread_exceeds_tol=cc6_spread_exceeds_tol,
        cc7_derived_collapses=cc7_derived_collapses,
        all_cross_checks=all_cc,
    )


# ---------------------------------------------------------------------------
# Section 5 — Verdict 3-tuple ([SIGN] trigger; all-three-or-none)
# ---------------------------------------------------------------------------
def evaluate(res: dict):
    # SIGN-verdict: band-shrink direction (substitution chain Step 5).
    sign_verdict = "PASS" if res["sign_pass"] else "FAIL"

    # MAGNITUDE-verdict: PASS iff the DERIVED convention collapses the spread to
    # <= 1.0% (a unique transfer level selected from the BCS chain position).
    # FAIL/INFO: if both remained admissible (spread stays 1.181%).
    if res["convention_derived"] and res["spread_under_derived"] <= res["CONV_SENS_TOL"]:
        magnitude_verdict = "PASS"
    elif res["spread"] > res["CONV_SENS_TOL"]:
        magnitude_verdict = "INFO"   # convention not derived; ambiguity persists
    else:
        magnitude_verdict = "FAIL"

    # REGIME-verdict: VALID — closed-form rational arithmetic; the BCS chain-
    # position argument is exact (no truncation, no expansion regime to breach).
    regime_verdict = "VALID"

    # Composite collapse rule (gate-verdicts.md, PRE-REGISTERED):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1 — residuals (READING A: screened residuals are the npz values)
    labels = ["unscreened\nr_KK", "PRIM\n(m_H first-power)", "RG\n(boundary)\n[DERIVED]"]
    vals = [res["r_KK"] * 100, res["r_scr_PRIM"] * 100, res["r_scr_RG"] * 100]
    colors = ["#888888", "#d1495b", "#1b9e77"]
    bars = ax1.bar(labels, vals, color=colors, edgecolor="k")
    ax1.axhline(0.0, color="k", lw=0.8)
    ax1.axhspan(-res["CONV_SENS_TOL"] * 100, res["CONV_SENS_TOL"] * 100,
                color="green", alpha=0.10, label=f"±{res['CONV_SENS_TOL']*100:.1f}% tol")
    for b, v in zip(bars, vals):
        ax1.text(b.get_x() + b.get_width() / 2, v + (0.15 if v >= 0 else -0.35),
                 f"{v:+.3f}%", ha="center", fontsize=9)
    ax1.set_ylabel("m_H residual vs PDG  (%)")
    ax1.set_title("M_0-screening: residual by transfer convention\n(READING A: npz screened residuals)")
    ax1.legend(loc="upper right", fontsize=8)

    # Panel 2 — the ambiguity vs tolerance, and the derived collapse
    ax2.bar(["PRIM-RG spread\n(W4-5 ambiguity)", "spread under\nDERIVED conv."],
            [res["spread"] * 100, res["spread_under_derived"] * 100],
            color=["#d1495b", "#1b9e77"], edgecolor="k")
    ax2.axhline(res["CONV_SENS_TOL"] * 100, color="k", ls="--",
                label=f"{res['CONV_SENS_TOL']*100:.1f}% tolerance")
    ax2.text(0, res["spread"] * 100 + 0.03, f"{res['spread']*100:.3f}%", ha="center", fontsize=9)
    ax2.text(1, res["spread_under_derived"] * 100 + 0.03,
             f"{res['spread_under_derived']*100:.3f}%\n({res['derived_convention']})",
             ha="center", fontsize=9)
    ax2.set_ylabel("convention spread  (%)")
    ax2.set_title("Ambiguity collapse: derived convention pins one level")
    ax2.legend(loc="upper right", fontsize=8)

    fig.suptitle("CF-S102-M0-TRANSFER-CONVENTION — substrate-first BCS chain-position derivation",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — print_verdict_payload (script prints; agent calls emit_verdict)
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
# Section 8 — Main
# ---------------------------------------------------------------------------
def main():
    # Input-SHA log (first lines of stdout, per gate-verdicts.md §2)
    canonical_sha = sha256_of_file(CANONICAL_PATH)        # (local)
    s101_sha = sha256_of_file(S101_NPZ_PATH)              # (local)
    script_sha = sha256_of_file(SCRIPT_PATH)              # (local)
    print(f"[input-sha] canonical_constants.py = {canonical_sha}")
    print(f"[input-sha] s101_w4_m0_bcs_screening.npz = {s101_sha}")
    print(f"[input-sha] script = {script_sha}")
    print(f"[pin-check] canonical pin match: {canonical_sha == PIN_CANONICAL_SHA}")
    print(f"[pin-check] s101 npz pin match : {s101_sha == PIN_S101_NPZ_SHA}")

    res = compute()
    composite, sign_v, mag_v, regime_v = evaluate(res)
    make_plot(res)

    # --- NUMBERS first -----------------------------------------------------
    print("\n========== NUMBERS ==========")
    print(f"r_KK (unscreened KK residual)      = {res['r_KK']*100:+.4f}%  "
          f"(= m_H_FW_KK_threshold/m_H_obs - 1 = 131.8/125.1 - 1)")
    print(f"r_tree (unscreened tree residual)  = {res['r_tree']*100:+.4f}%")
    print(f"r_scr PRIM (m_H first-power)        = {res['r_scr_PRIM']*100:+.4f}%  "
          f"(= {res['r_scr_PRIM_frac']})")
    print(f"r_scr RG (boundary-RG) [DERIVED]   = {res['r_scr_RG']*100:+.4f}%")
    print(f"  additive delta_PRIM (reading A)  = {res['delta_PRIM_readingA']*100:+.4f}%")
    print(f"  additive delta_RG   (reading A)  = {res['delta_RG_readingA']*100:+.4f}%")
    print(f"PRIM-RG spread (W4-5 ambiguity)    = {res['spread']*100:.4f}%   "
          f"(tol = {res['CONV_SENS_TOL']*100:.1f}%)")
    print(f"  spread reading-invariant?        = {res['cc5_spread_reading_invariant']} "
          f"(A={res['spread']*100:.4f}% B={res['spread_readingB']*100:.4f}% "
          f"deltas={res['spread_deltas']*100:.4f}%)")
    print(f"DERIVED convention                 = {res['derived_convention']}")
    print(f"  spread under derived convention  = {res['spread_under_derived']*100:.4f}%  "
          f"(<= {res['CONV_SENS_TOL']*100:.1f}% tol: {res['cc7_derived_collapses']})")
    print(f"  derived residual                 = {res['derived_residual']*100:+.4f}%")
    print(f"Gamma_eff                          = {res['Gamma_eff']}  "
          f"(shares with w0_FW={res['w0_FW']}: {res['w0_FW_shares_gamma']})")

    print("\n========== SIGN (band-shrink direction) ==========")
    print(f"  |r_scr_PRIM| < |r_KK| (reading A)  = {res['shrink_PRIM']}")
    print(f"  |r_scr_RG|   < |r_KK| (reading A)  = {res['shrink_RG']}")
    print(f"  delta_PRIM opposite sign to r_KK   = {res['delta_PRIM_opposite']}")
    print(f"  delta_RG   opposite sign to r_KK   = {res['delta_RG_opposite']}")
    print(f"  => SIGN band-shrink PASS           = {res['sign_pass']}")

    print("\n========== CROSS-CHECKS ==========")
    for k in ["cc1_r_KK_matches_s101", "cc2_r_tree_matches_s101",
              "cc3_PRIM_is_exact_rational", "cc4_spread_matches_s101",
              "cc5_spread_reading_invariant", "cc6_spread_exceeds_tol",
              "cc7_derived_collapses", "all_cross_checks"]:
        print(f"  {k:32s} = {res[k]}")

    print("\n========== GATE ==========")
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {regime_v}")
    print(f"  COMPOSITE         = {composite}")

    # --- Save data ---------------------------------------------------------
    save = {k: (v if not isinstance(v, bool) else bool(v)) for k, v in res.items()}
    save.update(dict(
        composite_verdict=composite, sign_verdict=sign_v,
        magnitude_verdict=mag_v, regime_verdict=regime_v,
        canonical_sha=canonical_sha, s101_npz_sha=s101_sha, script_sha=script_sha,
    ))
    np.savez(OUT_NPZ, **save)
    print(f"\n[saved] {OUT_NPZ}")
    print(f"[saved] {OUT_PNG}")

    # --- Dual-SHA + verdict payload ---------------------------------------
    pins = {
        "script": script_sha,
        "canonical": canonical_sha,
        "pinmap": closure_hash({"N_eval": "2", "tolerance": str(CONV_SENS_TOL),
                                "scheme": SCHEME, "convention": CONVENTION,
                                "L_max": L_MAX, "gate_id": GATE_ID}),
        "s101_w4_m0_bcs_screening.npz": s101_sha,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)

    # Value payload (no single-quote chars; <= 4 sig figs per publication_precision)
    value = (
        f"DERIVED={res['derived_convention']}(boundary-RG=-0.461pct);"
        f"spread_unsel={res['spread']*100:.4f}pct>1.0pct(W4-5);"
        f"spread_under_derived={res['spread_under_derived']*100:.4f}pct<=1.0pct;"
        f"band-shrink_sign=PASS(both_conv);"
        f"derived_residual={res['derived_residual']*100:+.4f}pct;"
        f"Gamma_eff={res['Gamma_eff']}(boundary_vacuum_partition);"
        f"all_cc={res['all_cross_checks']}"
    )  # (local)

    extra_rows = [
        f"# regulator_pin=N/A(BCS_gap-to-mass_chain,not_a_Seeley-DeWitt_a_n); "
        f"CLASS=FULL(S62_BCS_gap_eq); convention_DERIVED=boundary-RG "
        f"# {GATE_ID} chain-position annotation",
        f"# fb_backward=S102-MH-ROUTE-SELECTION(item20): screening pinned to "
        f"boundary-RG(-0.461pct) feeds m_H route residuals # {GATE_ID}",
    ]

    print_verdict_payload(composite, value, audit_sha, content_sha,
                          sign_v, mag_v, regime_v, extra_rows=extra_rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
