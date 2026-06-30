"""S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE (S86 W7-2).

Branch-c phonon-mechanism 10x ABSOLUTE discriminator vs landau and kaku siblings.

Plan: sessions/session-plan/session-86-plan-w7.md §W7-2 (lines 329-611).
Source solos (S85 3B 3-solo set, .md format — NOT .npz):
  - sessions/archive/session-85/session-85-3b-branch-c-phonon-volovik.md
  - sessions/archive/session-85/session-85-3b-branch-c-phonon-landau.md
  - sessions/archive/session-85/session-85-3b-branch-c-phonon-kaku.md
W4 P4 BRANCH-IV-FORMULATION-COMMIT (S86): PASS at audit_sha256 acc751101c8ca6ce...

Method (per plan §6):
  Step A — load three sibling signature observables (each from its 3B solo).
  Step B — verify all three solos predict the SAME observable class.
  Step C — compute R_vL = |O_volovik|/|O_landau|, R_vK = |O_volovik|/|O_kaku|.
  Step D — R_min = min(R_vL, R_vK).
  Step E — consistency cross-check R_Lv ≤ 0.1 AND R_Kv ≤ 0.1 (anti-cherrypick).
  Step F — closure SHA over ordered input-pin map.

Decision rule (per plan §9):
  PASS  iff R_min ≥ 10 AND R_Lv ≤ 0.1 AND R_Kv ≤ 0.1.
  INFO  iff 5 ≤ R_min < 10 OR Step B abort path fires (observable classes differ).
  FAIL  iff R_min < 5, OR (R_min ≥ 10 BUT consistency cross-check fails).

This script's verdict path: STEP B abort → INFO with reason
"sibling observables not commensurable". Volovik solo predicts a residue
enhancement ratio (≈127.88), landau predicts a Bogoliubov mixing-angle
ratio Q(L=12) (≈11.308), kaku predicts a CP-odd 4-point function ratio
(0 EXACTLY). Three different observable classes — no commensurable
absolute-magnitude ratio is defined.

Per the plan §6 abort path, the script computes R_vL, R_vK, R_min as
DIAGNOSTIC values (under the as-reported numerics) and emits INFO with
reason logged in the verdict-line scheme tag.
"""

from canonical_constants import M_KK, tau_fold  # noqa: F401
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

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json  # noqa: E402
import pathlib  # noqa: E402
import sys  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")  # (local)
import matplotlib.pyplot as plt  # noqa: E402


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent  # (local)
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
S85_3B_DIR = REPO_ROOT / "sessions" / "session-85"  # (local)

VOLOVIK_SOLO = S85_3B_DIR / "session-85-3b-branch-c-phonon-volovik.md"  # (local)
LANDAU_SOLO = S85_3B_DIR / "session-85-3b-branch-c-phonon-landau.md"  # (local)
KAKU_SOLO = S85_3B_DIR / "session-85-3b-branch-c-phonon-kaku.md"  # (local)

S86_VERDICT = resolve_output(86, 's86_gate_verdicts.txt')  # (local)
OUT_NPZ = resolve_output(86, 's86_w7_branchc_discriminator.npz')  # (local)
OUT_PNG = resolve_output(86, 's86_w7_branchc_discriminator.png')  # (local)

GATE_ID = "S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE"  # (local)
SCHEME = "ABSOLUTE-min-dominance"  # (local) plan §7
CONVENTION = "branch-c-vs-{landau,kaku}"  # (local) plan §7
L_MAX_TAG = 10  # (local) plan §7

PASS_R_MIN = 10.0  # (local) plan §9 PASS threshold
INFO_R_MIN_LO = 5.0  # (local) plan §9 INFO band lower bound
PASS_INV_RATIO = 0.1  # (local) plan §9 consistency threshold


def sha256_path(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()  # (local)


def append_verdict(verdict_line: str, dual_sha_line: str) -> None:
    """Single open('a') append for both lines (atomic-ish on POSIX/NTFS)."""
    with S86_VERDICT.open("a", encoding="utf-8") as fh:
        fh.write(verdict_line + "\n")
        fh.write(dual_sha_line + "\n")


def main() -> int:
    # =========================================================================
    # MCP Pre-Compute Audit (record in WP)
    # =========================================================================
    # Queries executed via mcp__knowledge__ before this script ran:
    #   1. search_knowledge("branch-c phonon mechanism") — confirmed 10 hits across
    #      session-85-3b-branch-c-phonon-{volovik,landau}.md + session-86-plan-w7.md.
    #   2. trace_entity("inverted Josephson retraction") — confirmed S85-W7-W0-RE-AUDIT-AT-L8
    #      gate PASS at audit_sha256=dddf9edda82b4f3e (post-retraction reading).
    #   3. query_entity("gates", "S86-BRANCH-IV-FORMULATION-COMMIT") — no entity in
    #      knowledge.db (gate landed S86 W4 P4; not yet ingested into DB).
    #      Resolved via grep against computations/session-86/s86_gate_verdicts.txt:
    #        PASS verdict at audit_sha256=acc751101c8ca6ce content_sha256=55090d91af40d1e1.
    #   4. search_knowledge("branch iv W12-3 retraction") — confirmed branch (iv) was
    #      retired at S84 (S85 W12-3 follow-up); branch-c is the surviving phonon channel
    #      in the post-retraction 3-branch enumeration.

    # =========================================================================
    # Step 0 — Load source-document SHAs (input-pin map; late-bound)
    # =========================================================================
    if not VOLOVIK_SOLO.exists():
        print(f"ABORT: {VOLOVIK_SOLO} missing", file=sys.stderr)
        return 2
    if not LANDAU_SOLO.exists():
        print(f"ABORT: {LANDAU_SOLO} missing", file=sys.stderr)
        return 2
    if not KAKU_SOLO.exists():
        print(f"ABORT: {KAKU_SOLO} missing", file=sys.stderr)
        return 2

    sha_volovik_solo = sha256_path(VOLOVIK_SOLO)  # (local) input pin 1
    sha_landau_solo = sha256_path(LANDAU_SOLO)  # (local) input pin 2
    sha_kaku_solo = sha256_path(KAKU_SOLO)  # (local) input pin 3

    # W4 P4 BRANCH-IV-FORMULATION-COMMIT verdict (PASS landed before this gate ran)
    branchc_naming_audit_sha = (
        "acc751101c8ca6cec920c8fd58198a6a147bc925455f198613002a8e40161049"
    )  # (local) input pin 4
    branchc_naming_content_sha = (
        "55090d91af40d1e194e3ba879f7c3feba407177968217c45e0b30eed8bb6b3b7"
    )  # (local) input pin 4 content

    # First-20-lines stdout SHA log (per plan §3 of canonical pre-registration)
    print("=== S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE input-pin map ===")
    print(f"input1.volovik_solo_sha256 = {sha_volovik_solo}")
    print(f"input2.landau_solo_sha256  = {sha_landau_solo}")
    print(f"input3.kaku_solo_sha256    = {sha_kaku_solo}")
    print(f"input4.branchc_naming_audit_sha256   = {branchc_naming_audit_sha}")
    print(f"input4.branchc_naming_content_sha256 = {branchc_naming_content_sha}")
    print(f"observable_class_pin = SEE-STEP-B (commensurability test)")
    print(f"ratio_basis_pin      = ABSOLUTE")
    print("================================================================")

    # =========================================================================
    # Step A — Load each sibling's signature observable + (scheme, convention,
    # L_max, observable_class) tag-tuple, by extraction from the S85 3B solo MD.
    # =========================================================================
    # Volovik (a) — GGE-relic / superfluid-universe track:
    #   §II.B Step 3 + Appendix A: residue ratio (c/a) at L=12 = 127.88
    #   §II.D.1 Channel 1 (cosmological): "ΔN_eff(branch-c) =
    #     127.88 · ΔN_eff_baseline   (at L_obs = 12)"
    #   Signature observable: ΔN_eff enhancement ratio at L=12.
    #   Observable class: "residue ratio (relativistic-DOF count enhancement)"
    O_volovik = 127.88  # (local) volovik signature: ΔN_eff enhancement = residue_c/residue_a at L=12
    obs_class_volovik = "residue-ratio-relativistic-DOF-count"  # (local)
    scheme_volovik = "ζ-regulator-Mellin-cone-s3"  # (local) per volovik solo §II.A Step 2
    convention_volovik = "TB-pinned-ξ_J-vs-ξ_E_GGE(L)"  # (local)
    Lmax_volovik = 12  # (local) volovik signature evaluated at L=12 (W10-4 plan-anchor)

    # Landau (b) — Bogoliubov / BCS / Leggett-Josephson phase-channel track:
    #   §II.4 Step 4: Q(L=12) = θ_c(12) / θ_a(12) = 11.308
    #   Signature observable: Bogoliubov mixing-angle ratio Q at L=12.
    #   Observable class: "Bogoliubov mixing-angle ratio"
    O_landau = 11.308  # (local) landau signature: mixing-angle ratio Q(12) = θ_c/θ_a
    obs_class_landau = "Bogoliubov-mixing-angle-ratio"  # (local)
    scheme_landau = "Bogoliubov-coefficient-mapping"  # (local) per landau solo §II.1
    convention_landau = "u=cosh(r),v=sinh(r),θ=arctan(tanh(r))"  # (local)
    Lmax_landau = 12  # (local) landau signature evaluated at L=12

    # Kaku (c) — Josephson-inverted vacuum / instanton-anti-instanton pair:
    #   §II.4 + §V.1 PASS-(c) prediction: CP-odd ratio = 0 EXACTLY
    #   (CP-pair-balance theorem on (1, 1̄) symmetric sector at fixed N_GGE).
    #   Signature observable: CP-odd 4-point function ratio at GGE relic scale.
    #   Observable class: "CP-odd 4-point function ratio"
    O_kaku = 0.0  # (local) kaku signature: CP-odd ratio (PASS-(c) PRED = 0 EXACTLY)
    obs_class_kaku = "CP-odd-4pt-function-ratio"  # (local)
    scheme_kaku = "CP-pair-balance-theorem"  # (local) per kaku solo §II.4 + §V.1
    convention_kaku = "<TBBB>_CP_odd-at-GGE-relic-band-ℓ100"  # (local)
    Lmax_kaku = 12  # (local) kaku signature pre-registered at L=12

    # =========================================================================
    # Step B — Verify all three solos predict the SAME observable class.
    # Plan §6 Step B abort path: "If observable classes differ, abort and emit
    # INFO with reason: 'sibling observables not commensurable'."
    # =========================================================================
    obs_classes = (obs_class_volovik, obs_class_landau, obs_class_kaku)  # (local)
    classes_unique = len(set(obs_classes)) == 1  # (local) commensurability test
    classes_pairwise = (
        obs_class_volovik != obs_class_landau,  # (local)
        obs_class_volovik != obs_class_kaku,  # (local)
        obs_class_landau != obs_class_kaku,  # (local)
    )  # (local)
    step_b_abort = not classes_unique  # (local) True ⇒ INFO path

    print("=== Step B (observable-class commensurability) ===")
    print(f"obs_class(volovik) = {obs_class_volovik}")
    print(f"obs_class(landau)  = {obs_class_landau}")
    print(f"obs_class(kaku)    = {obs_class_kaku}")
    print(f"classes_unique = {classes_unique}")
    print(f"pairwise_distinct = (vL,vK,LK) = {classes_pairwise}")
    print(f"Step B abort? = {step_b_abort}")

    # =========================================================================
    # Step C — Compute R_vL, R_vK (DIAGNOSTIC under Step-B abort; STRUCTURAL
    # under non-abort). Use ABSOLUTE ratio per plan §7 ratio_basis_pin.
    # =========================================================================
    abs_O_v = abs(O_volovik)  # (local)
    abs_O_L = abs(O_landau)  # (local)
    abs_O_K = abs(O_kaku)  # (local)

    # R_vL = |O_volovik| / |O_landau|
    if abs_O_L > 0:
        R_vL = abs_O_v / abs_O_L  # (local)
    else:
        R_vL = float("inf")  # (local) divergent ratio
    # R_vK = |O_volovik| / |O_kaku|
    if abs_O_K > 0:
        R_vK = abs_O_v / abs_O_K  # (local)
    else:
        R_vK = float("inf")  # (local) divergent ratio (kaku exact null prediction)

    # =========================================================================
    # Step D — R_min = min(R_vL, R_vK)
    # =========================================================================
    R_min = min(R_vL, R_vK)  # (local)

    # =========================================================================
    # Step E — Inverse consistency cross-check (anti-cherrypick).
    # =========================================================================
    if abs_O_v > 0:
        R_Lv = abs_O_L / abs_O_v  # (local)
        R_Kv = abs_O_K / abs_O_v  # (local)
    else:
        R_Lv = float("inf")  # (local)
        R_Kv = float("inf")  # (local)

    consistency_pass = (R_Lv <= PASS_INV_RATIO) and (R_Kv <= PASS_INV_RATIO)  # (local)

    print("=== Step C/D/E (ratios) ===")
    print(f"R_vL = |O_volovik|/|O_landau| = {abs_O_v}/{abs_O_L} = {R_vL}")
    print(f"R_vK = |O_volovik|/|O_kaku|   = {abs_O_v}/{abs_O_K} = {R_vK}")
    print(f"R_min = min(R_vL, R_vK)       = {R_min}")
    print(f"R_Lv = |O_landau|/|O_volovik| = {R_Lv}")
    print(f"R_Kv = |O_kaku|/|O_volovik|   = {R_Kv}")
    print(f"consistency_pass = {consistency_pass}")

    # =========================================================================
    # Decision rule (per plan §9):
    # =========================================================================
    if step_b_abort:
        verdict = "INFO"  # (local)
        verdict_reason = "sibling-observables-not-commensurable"  # (local)
    elif R_min >= PASS_R_MIN and consistency_pass:
        verdict = "PASS"  # (local)
        verdict_reason = "branch-c-dominates-both-siblings-by-≥10x-ABSOLUTE"  # (local)
    elif R_min >= PASS_R_MIN and not consistency_pass:
        verdict = "FAIL"  # (local)
        verdict_reason = "FAIL-CONSISTENCY-input-arithmetic-error"  # (local)
    elif INFO_R_MIN_LO <= R_min < PASS_R_MIN:
        verdict = "INFO"  # (local)
        verdict_reason = "intermediate-dominance-band-5≤R_min<10"  # (local)
    else:
        verdict = "FAIL"  # (local)
        verdict_reason = "no-observable-discrimination-R_min<5"  # (local)

    print(f"=== VERDICT: {verdict} ({verdict_reason}) ===")

    # =========================================================================
    # Step F — closure SHA over ordered input-pin map.
    # =========================================================================
    pin_map = {  # (local)
        "1.volovik_solo_sha256": sha_volovik_solo,
        "2.landau_solo_sha256": sha_landau_solo,
        "3.kaku_solo_sha256": sha_kaku_solo,
        "4.branchc_naming_audit_sha256": branchc_naming_audit_sha,
        "4.branchc_naming_content_sha256": branchc_naming_content_sha,
        "observable_class_pin.volovik": obs_class_volovik,
        "observable_class_pin.landau": obs_class_landau,
        "observable_class_pin.kaku": obs_class_kaku,
        "ratio_basis_pin": "ABSOLUTE",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "PASS_R_MIN": PASS_R_MIN,
        "PASS_INV_RATIO": PASS_INV_RATIO,
    }
    pin_map_json = json.dumps(pin_map, sort_keys=True).encode("utf-8")  # (local)
    audit_sha256 = hashlib.sha256(pin_map_json).hexdigest()  # (local)

    # content_sha256 = SHA-256 of the verdict-content tuple (R_min, verdict, ratios)
    content_tuple = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "R_vL": R_vL if np.isfinite(R_vL) else "inf",
        "R_vK": R_vK if np.isfinite(R_vK) else "inf",
        "R_min": R_min if np.isfinite(R_min) else "inf",
        "R_Lv": R_Lv if np.isfinite(R_Lv) else "inf",
        "R_Kv": R_Kv if np.isfinite(R_Kv) else "inf",
        "O_volovik": O_volovik,
        "O_landau": O_landau,
        "O_kaku": O_kaku,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "verdict_reason": verdict_reason,
    }
    content_json = json.dumps(content_tuple, sort_keys=True).encode("utf-8")  # (local)
    content_sha256 = hashlib.sha256(content_json).hexdigest()  # (local)

    print(f"audit_sha256   = {audit_sha256}")
    print(f"content_sha256 = {content_sha256}")

    # =========================================================================
    # Save .npz artifact
    # =========================================================================
    np.savez(
        OUT_NPZ,
        O_volovik=np.float64(O_volovik),
        O_landau=np.float64(O_landau),
        O_kaku=np.float64(O_kaku),
        R_vL=np.float64(R_vL),
        R_vK=np.float64(R_vK),
        R_min=np.float64(R_min),
        R_Lv=np.float64(R_Lv),
        R_Kv=np.float64(R_Kv),
        obs_class_volovik=np.array(obs_class_volovik),
        obs_class_landau=np.array(obs_class_landau),
        obs_class_kaku=np.array(obs_class_kaku),
        verdict=np.array(verdict),
        verdict_reason=np.array(verdict_reason),
        audit_sha256=np.array(audit_sha256),
        content_sha256=np.array(content_sha256),
    )

    # =========================================================================
    # Plot (3-bar magnitude plot — log scale for the kaku=0 + volovik=128 spread)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(7.5, 5.0))
    siblings = ["volovik\n(branch-c)", "landau", "kaku"]  # (local)
    mags = [abs_O_v, abs_O_L, abs_O_K]  # (local)
    classes = [obs_class_volovik, obs_class_landau, obs_class_kaku]  # (local)
    colors = ["#2c7fb8", "#7fcdbb", "#d95f02"]  # (local)

    # Use a small floor (1e-15) for log-scale display of the kaku=0 prediction
    mags_plot = [m if m > 0 else 1e-15 for m in mags]  # (local) display floor
    bars = ax.bar(siblings, mags_plot, color=colors, edgecolor="black", linewidth=0.7)
    ax.set_yscale("log")
    ax.set_ylabel("|O_sibling|  (log scale; observable-class differs per sibling)")
    ax.set_title(
        "S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE — sibling magnitudes\n"
        f"R_vL={R_vL:.3e}  R_vK={R_vK:.3e}  R_min={R_min:.3e}  verdict={verdict}"
    )
    for bar, mag, cls in zip(bars, mags, classes):
        height = bar.get_height()
        label = f"{mag:.3g}\n[{cls}]"  # (local)
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height * 1.4,
            label,
            ha="center",
            va="bottom",
            fontsize=8,
        )
    ax.set_ylim(1e-16, max(mags_plot) * 50)
    ax.grid(True, axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)

    # =========================================================================
    # Append verdict line to s86_gate_verdicts.txt (canonical form)
    # =========================================================================
    # value=R_min — per plan §6 verdict-line format:
    #   "value=<R_min> scheme=ABSOLUTE-min-dominance convention=branch-c-vs-{landau,kaku}
    #    L_max=10 sha256=<64-char>"
    # When R_min is divergent (kaku exact null), report 'inf'.
    if np.isfinite(R_min):
        value_str = f"{R_min:.6e}"  # (local)
    else:
        value_str = "inf"  # (local) divergent under kaku exact null

    info_reason_tag = (
        f" info_reason={verdict_reason}" if verdict in ("INFO", "FAIL") else ""
    )  # (local)

    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={value_str} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version=S84+{info_reason_tag}"
    )  # (local)

    dual_sha_line = (
        f"# {GATE_ID}: audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256={content_sha256} audit_sha256={audit_sha256}"
    )  # (local)

    append_verdict(verdict_line, dual_sha_line)

    print(f"=== Appended verdict line to {S86_VERDICT.name} ===")
    print(verdict_line)
    print(dual_sha_line)

    # 4-tuple final non-verdict line
    print(
        f"4-tuple: (value={value_str}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX_TAG})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
