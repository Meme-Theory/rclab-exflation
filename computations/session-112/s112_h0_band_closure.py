#!/usr/bin/env python3
"""
S112 W1-2 CF-S112-H0-BAND-CLOSURE — conditional H0-residual band closure
========================================================================

Gate: CF-S112-H0-BAND-CLOSURE ([SIGN])

Pre-registered threshold (plan §W1-2):
  band_closed := [ (W1-1 verdict == PASS) AND (relief_dimensionful covers
                   residual_held into the H0 band [0.08, 0.10]) ]; CONDITIONAL
                 on the upstream W1-1 (CF-S112-MKK-SUBSTRATE-ANCHOR) verdict.
  - W1-1 PASS  -> attempt the dimensionful draw; PASS iff in-band.
  - W1-1 FAIL  -> M_KK^1 scale leg stays INADMISSIBLE; band_closed=False;
                  H0 relief CAPPED at the 6.125% dimensionless channel
                  (the registered fallback; FAIL with the capped reading).
  - W1-1 INFO/UNCOMPUTED -> mechanical closure (PRE-REG-INC).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-111/s111_cf3_h0_residual.npz  (dimensionless relief
    49/800, held 93.875%, band [0.08,0.10], dimensionful_draw_required=18.36)
  - computations/session-112/s112_gate_verdicts.txt    (W1-1 verdict line,
    runtime-resolved via gate-verdicts.md Option-A supersession reading)
  - canonical_constants.py (feeds audit_sha256; supplies H_0_km_s_Mpc, w0_FW,
    clock_coeff, M_KK as substrate framing anchors)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<band_closed payload>, scheme=emergent-scale-transport-DIMENSIONLESS-ONLY,
   convention=DA-0-PARITY-EVEN, L_max=12)

Classification: PHONONIC. H0 — the emergent expansion rate — is read from the
substrate's GGE-relic transport channel (a_0/a_2 Seeley-DeWitt moments source
the effective Friedmann H^2 = (8 pi G_eff/3) rho_eff). The residual is a
transport observable of the substrate's excitations across the 54.04-decade
substrate-leaf -> CMB-pivot scale separation.

METHODOLOGY
-----------
This gate is the CONDITIONAL downstream consumer of CF-S112-MKK-SUBSTRATE-ANCHOR
(W1-1). It performs NO new substrate compute: the dimensionless transport channel
relief is the exact rational 49/800 = 0.06124965 loaded from s111_cf3, and the
band-closure decision is a function of the W1-1 PASS/FAIL outcome resolved at
runtime from the verdict file. W1-1 returned FAIL (the registered self-referential-
unit-system no-go: a finite spectral triple that measures every observable in
M_KK units cannot fix its own absolute GeV scale from within — the lattice-QCD
scale-setting analog). Per the plan §W1-2 conditional branch logic, the FAIL
outcome selects the FAIL branch: the d_A=+1 ODD M_KK^1 scale leg stays
INADMISSIBLE (only EVEN-degree morphisms can transport a bare external scale to
the pivot; the parity selection rule blocks it, corpus §23.0(5)), so no
dimensionful draw is permitted and relief is CAPPED at the dimensionless channel.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- numpy scalar band-closure arithmetic; no matrix solve, no GPU path needed
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Verdict emitted via emit_verdict knowledge-MCP tool (race-safe); the script
  PRINTS print_verdict_payload, the dispatching AGENT calls emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path

_SESSION_DIR_BOOT = _Path(__file__).resolve().parent
_SHARED_DIR_BOOT = _SESSION_DIR_BOOT.parent / "_shared"
if str(_SHARED_DIR_BOOT) not in _sys.path:
    _sys.path.insert(0, str(_SHARED_DIR_BOOT))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit names used in substrate framing
    H_0_km_s_Mpc,
    w0_FW,
    clock_coeff,
    M_KK,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S112"                                                   # (local)
GATE_ID = "CF-S112-H0-BAND-CLOSURE"                                # (local)
SCHEME = "emergent-scale-transport-DIMENSIONLESS-ONLY"             # (local)
CONVENTION = "DA-0-PARITY-EVEN"                                    # (local)
L_MAX = 12                                                         # (local)

# Upstream gate whose verdict selects the conditional band-closure branch.
UPSTREAM_GATE_ID = "CF-S112-MKK-SUBSTRATE-ANCHOR"                  # (local)

# Output destinations (per-session). The verdict file is written by emit_verdict.
OUT_NPZ = SESSION_DIR / "s112_h0_band_closure.npz"
OUT_PNG = SESSION_DIR / "s112_h0_band_closure.png"

# Input files. The W1-1 verdict file is also an audit input (resolved at runtime).
S111_CF3_NPZ = COMPUTATIONS_DIR / "session-111" / "s111_cf3_h0_residual.npz"
VERDICT_FILE = SESSION_DIR / "s112_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S111_CF3_NPZ,
    VERDICT_FILE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
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
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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
# Section 4b — Runtime resolution of the upstream W1-1 verdict
#   (gate-verdicts.md Option-A supersession reading: scan all canonical lines
#    for the gate-ID, drop any line named in another line's supersedes= token,
#    take the latest non-superseded line as authoritative.)
# ---------------------------------------------------------------------------

def resolve_upstream_verdict(verdict_path: Path, gate_id: str) -> dict:
    """Return {'verdict': PASS|FAIL|INFO|None, 'line': str, 'audit_sha': str}.

    None verdict => the gate-ID has no canonical line (UNCOMPUTED) =>
    the caller routes to mechanical closure.
    """
    if not verdict_path.exists():
        return {"verdict": None, "line": "", "audit_sha": "",
                "reason": "verdict_file_absent"}

    text = verdict_path.read_text(encoding="utf-8", errors="replace")  # (local)
    # Canonical lines only (start with the gate-ID, not a '#' companion row).
    canon_re = re.compile(
        rf"^{re.escape(gate_id)}:\s+(PASS|FAIL|INFO|PRE-REG-INC)\b.*$"
    )  # (local)
    sha_re = re.compile(r"audit_sha256=([a-f0-9]{64})")  # (local)
    sup_re = re.compile(r"supersedes=([a-f0-9]{64})")  # (local)

    canonical_lines: list[tuple[int, str, str]] = []  # (idx, line, audit_sha)
    superseded_shas: set[str] = set()
    for idx, raw in enumerate(text.splitlines()):
        line = raw.rstrip("\n")  # (local)
        m = canon_re.match(line)
        if not m:
            continue
        sha_m = sha_re.search(line)  # (local)
        audit_sha = sha_m.group(1) if sha_m else ""  # (local)
        canonical_lines.append((idx, line, audit_sha))
        sup_m = sup_re.search(line)  # (local)
        if sup_m:
            superseded_shas.add(sup_m.group(1))

    if not canonical_lines:
        return {"verdict": None, "line": "", "audit_sha": "",
                "reason": "no_canonical_line"}

    # Latest non-superseded line (highest file index whose audit_sha is not
    # named in any other line's supersedes= token).
    live = [t for t in canonical_lines if t[2] not in superseded_shas]  # (local)
    chosen = (live[-1] if live else canonical_lines[-1])  # (local)
    _idx, line, audit_sha = chosen
    vm = canon_re.match(line)  # (local)
    verdict = vm.group(1) if vm else None  # (local)
    return {"verdict": verdict, "line": line, "audit_sha": audit_sha,
            "reason": "resolved", "n_canonical": len(canonical_lines),
            "n_superseded": len(superseded_shas)}


# ---------------------------------------------------------------------------
# Section 5 — Compute (conditional band-closure)
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Conditional H0-residual band-closure.

    NUMBERS first (load the s111_cf3 rationals), gate second (the conditional
    band-closure decision under the W1-1 outcome), interpretation third.
    """
    # ---- NUMBERS: load the s111_cf3 dimensionless-channel rationals -------
    cf3 = np.load(S111_CF3_NPZ, allow_pickle=True)  # (local)

    # Exact dimensionless relief (the substrate's d_A=0 even-parity channel):
    #   partial_relief_frac_lo = 1224993 / 20000000 = 0.06124965  (round 49/800)
    relief_num = int(cf3["partial_frac_lo_exact_num"])               # (local) 1224993
    relief_den = int(cf3["partial_frac_lo_exact_den"])               # (local) 20000000
    partial_relief = Fraction(relief_num, relief_den)                # (local) exact
    partial_relief_float = float(partial_relief)                     # (local) 0.06124965
    roundfig_num = int(cf3["partial_frac_roundfig_num"])             # (local) 49
    roundfig_den = int(cf3["partial_frac_roundfig_den"])             # (local) 800
    roundfig_within_4sf = bool(cf3["roundfig_within_4sf"])           # (local) True

    residual_held = float(cf3["residual_held_float"])                # (local) 0.93875035
    band_lo = float(cf3["band_lo"])                                  # (local) 0.08
    band_hi = float(cf3["band_hi"])                                  # (local) 0.10
    band_central = float(cf3["band_central"])                        # (local) 0.09
    band_lit = float(cf3["band_lit"])                                # (local) 0.084
    dimensionful_draw_reqd = float(cf3["dimensionful_draw_required_to_close"])  # (local) 18.36
    mkk1_inadmissible_bare = bool(cf3["M_KK1_scale_leg_INADMISSIBLE"])  # (local) True
    d_A_dH0 = int(cf3["d_A_dH0"])                                    # (local) 0
    deg_T = float(cf3["deg_T"])                                      # (local) 2.0
    a0_a2_orthogonal = bool(cf3["a0_a2_orthogonal"])                 # (local) True
    dec_separation = float(cf3["dec_separation"])                    # (local) 54.04
    best_dimless_frac_lo = float(cf3["best_dimless_frac_lo"])        # (local) 0.06127

    # Internal consistency: the loaded exact rational must equal residual=1-relief
    residual_check = float(1 - partial_relief)                       # (local)
    residual_consistent = bool(abs(residual_check - residual_held) < 1e-9)  # (local)
    # 4sf round-figure fidelity of the dimensionless floor (S111 roundfig check)
    roundfig_recompute_ok = bool(
        abs(partial_relief_float - roundfig_num / roundfig_den) < 5e-7
    )  # (local)

    # ---- GATE: resolve the upstream W1-1 verdict (Option-A reading) -------
    up = resolve_upstream_verdict(VERDICT_FILE, UPSTREAM_GATE_ID)    # (local)
    w1_1_verdict = up["verdict"]                                     # (local)
    w1_1_audit_sha = up["audit_sha"]                                 # (local)

    # ---- Conditional band-closure branch ----------------------------------
    # band_closed = f(W1-1):
    #   PASS  -> M_KK substrate-derived => odd M_KK^1 scale leg ADMISSIBLE
    #            => dimensionful draw permitted => test relief_total in band
    #   FAIL  -> scale leg stays INADMISSIBLE => no draw
    #            => relief_total = partial_relief (capped, 6.125%)
    #   None  -> mechanical closure (PRE-REG-INC)
    branch_taken = ""           # (local)
    band_closed = False         # (local)
    relief_total = partial_relief_float  # (local) default = capped dimensionless
    scale_leg_admissible = False  # (local)
    dimensionful_draw_attempted = False  # (local)
    composite_verdict = "FAIL"  # (local)
    sign_verdict = "N/A"        # (local)
    magnitude_verdict = "FAIL"  # (local)
    regime_verdict = "VALID"    # (local)

    if w1_1_verdict == "PASS":
        # PASS branch (not selected this run — W1-1 FAILed). Released odd leg.
        branch_taken = "PASS-dimensionful"
        scale_leg_admissible = True
        dimensionful_draw_attempted = True
        relief_total = partial_relief_float + residual_held  # full closure attempt
        band_closed = bool(band_lo <= relief_total <= band_hi)
        # SIGN: band-closure tracks the W1-1 scale-leg admissibility (positive).
        sign_verdict = "PASS"
        magnitude_verdict = "PASS" if band_closed else "FAIL"
        regime_verdict = "VALID"
        composite_verdict = "PASS" if band_closed else "FAIL"

    elif w1_1_verdict == "FAIL":
        # FAIL branch — the registered fallback (THIS run).
        # M_KK^1 odd scale leg stays INADMISSIBLE; no dimensionful draw.
        branch_taken = "FAIL-capped-dimensionless"
        scale_leg_admissible = False
        dimensionful_draw_attempted = False
        relief_total = partial_relief_float                    # 0.06124965, capped
        # Substitution chain Step 3: 0.06125 not in [0.08, 0.10] => band NOT closed.
        band_closed = bool(band_lo <= relief_total <= band_hi)  # -> False
        # SIGN read-off (substitution chain Step 4/5): band_closed tracks the SIGN
        # of W1-1 scale-leg admissibility. W1-1 FAIL => leg inadmissible => the
        # band-closure SIGN is correctly NEGATIVE (band does NOT close), which IS
        # the pre-registered directional prediction for the FAIL branch -> SIGN PASS.
        sign_verdict = "PASS"
        # MAGNITUDE: relief 0.06125 is below band_lo 0.08 by |0.08 - 0.06125| = 0.01875,
        # i.e. the residual does NOT land in-band => magnitude FAIL (the capped reading).
        magnitude_verdict = "FAIL"
        # REGIME: the conditional band-closure arithmetic is exact (rationals), the
        # FAIL branch is the registered fallback explicitly anticipated at plan-freeze
        # => the method is within its pre-registered regime throughout.
        regime_verdict = "VALID"
        # Composite collapse (gate-verdicts.md): sign=PASS, magnitude=FAIL, regime=VALID
        #   => composite = FAIL (the capped H0-relief ceiling, a structural boundary).
        composite_verdict = "FAIL"

    else:
        # INFO / UNCOMPUTED at dispatch -> mechanical closure (PRE-REG-INC).
        branch_taken = "PRE-REG-INC-mechanical-closure"
        scale_leg_admissible = False
        dimensionful_draw_attempted = False
        relief_total = partial_relief_float
        band_closed = False
        sign_verdict = "N/A"
        magnitude_verdict = "INFO"
        regime_verdict = "VALID"
        composite_verdict = "INFO"

    # ---- Margins / falsifier-relevant numbers -----------------------------
    band_floor_gap = float(band_lo - relief_total)                  # (local) +0.01875 on FAIL
    relief_ceiling_pct = float(relief_total * 100.0)                # (local) 6.125% on FAIL
    residual_still_held = float(1.0 - relief_total)                 # (local) 0.93875 on FAIL

    # ---- substrate framing anchors (canonical, for the npz record) --------
    h0_anchor = float(H_0_km_s_Mpc)        # (local) 67.4 km/s/Mpc
    w0_anchor = float(w0_FW)               # (local) -0.918
    clock_anchor = float(clock_coeff)      # (local) -3.08
    mkk_anchor = float(M_KK)               # (local) 7.4287e16 GeV (the ONE external scale)

    # ---- value payload string (no single-quote chars) ---------------------
    value = (
        f"branch={branch_taken};"
        f"W1-1_verdict={w1_1_verdict};"
        f"band_closed={band_closed};"
        f"relief_total={relief_total:.8f};"
        f"relief_ceiling_pct={relief_ceiling_pct:.4f};"
        f"partial_relief=49/800={partial_relief_float:.8f};"
        f"residual_held={residual_still_held:.8f};"
        f"band=[{band_lo},{band_hi}];"
        f"band_floor_gap={band_floor_gap:.6f};"
        f"d_A=0;M_KK1_scale_leg_INADMISSIBLE={mkk1_inadmissible_bare};"
        f"scale_leg_admissible={scale_leg_admissible};"
        f"dimensionful_draw_attempted={dimensionful_draw_attempted};"
        f"a0_a2_orthogonal={a0_a2_orthogonal};deg_T={deg_T};"
        f"sign={sign_verdict};mag={magnitude_verdict};regime={regime_verdict};"
        f"3tuple_composite={composite_verdict}"
    )

    return {
        "value": value,
        "composite_verdict": composite_verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # branch / closure
        "branch_taken": branch_taken,
        "w1_1_verdict": str(w1_1_verdict),
        "w1_1_audit_sha": w1_1_audit_sha,
        "w1_1_resolution_reason": up.get("reason", ""),
        "band_closed": band_closed,
        "scale_leg_admissible": scale_leg_admissible,
        "dimensionful_draw_attempted": dimensionful_draw_attempted,
        # numbers (exact + float)
        "partial_relief_num": relief_num,
        "partial_relief_den": relief_den,
        "partial_relief_float": partial_relief_float,
        "roundfig_num": roundfig_num,
        "roundfig_den": roundfig_den,
        "roundfig_within_4sf": roundfig_within_4sf,
        "roundfig_recompute_ok": roundfig_recompute_ok,
        "relief_total": relief_total,
        "relief_ceiling_pct": relief_ceiling_pct,
        "residual_held": residual_held,
        "residual_still_held": residual_still_held,
        "residual_consistent": residual_consistent,
        "band_lo": band_lo,
        "band_hi": band_hi,
        "band_central": band_central,
        "band_lit": band_lit,
        "band_floor_gap": band_floor_gap,
        "dimensionful_draw_reqd": dimensionful_draw_reqd,
        "mkk1_inadmissible_bare": mkk1_inadmissible_bare,
        "d_A_dH0": d_A_dH0,
        "deg_T": deg_T,
        "a0_a2_orthogonal": a0_a2_orthogonal,
        "dec_separation": dec_separation,
        "best_dimless_frac_lo": best_dimless_frac_lo,
        # canonical anchors
        "H_0_km_s_Mpc": h0_anchor,
        "w0_FW": w0_anchor,
        "clock_coeff": clock_anchor,
        "M_KK_external_scale": mkk_anchor,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot (optional per plan; a 1-bar band-position diagram)
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> bool:
    """Band-position diagram: relief_total vs the H0 closure band [0.08,0.10]."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # (local)
        print(f"  [plot skipped: {exc}]")
        return False

    fig, ax = plt.subplots(figsize=(7.2, 3.4))  # (local)
    band_lo = res["band_lo"]      # (local)
    band_hi = res["band_hi"]      # (local)
    relief = res["relief_total"]  # (local)
    dimless = res["partial_relief_float"]  # (local)

    # H0 closure band
    ax.axvspan(band_lo, band_hi, color="#9ecae1", alpha=0.55,
               label=f"H0 closure band [{band_lo:.2f}, {band_hi:.2f}]")
    ax.axvline(res["band_central"], color="#3182bd", ls="--", lw=1.0,
               label=f"band central {res['band_central']:.2f}")
    # capped dimensionless relief (the FAIL-branch ceiling)
    ax.axvline(relief, color="#de2d26", lw=2.4,
               label=f"relief (capped) = {relief:.5f} = 6.125%")
    ax.scatter([dimless], [0.5], color="#de2d26", zorder=5, s=40)
    ax.annotate(
        f"band floor gap = {res['band_floor_gap']:+.5f}\n"
        f"(0.06125 below band_lo 0.08)",
        xy=(relief, 0.5), xytext=(relief + 0.005, 0.78),
        fontsize=8, color="#a50f15",
        arrowprops=dict(arrowstyle="->", color="#a50f15", lw=0.8),
    )

    ax.set_xlim(0.0, 0.12)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel("H0-residual relief fraction")
    ax.set_title(
        "CF-S112-H0-BAND-CLOSURE (FAIL branch)\n"
        "W1-1 FAIL => M_KK^1 odd scale leg INADMISSIBLE => "
        "relief CAPPED at 6.125% dimensionless channel"
    )
    ax.legend(loc="upper right", fontsize=7, framealpha=0.9)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    return True


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str | None = None,
    magnitude_verdict: str | None = None,
    regime_verdict: str | None = None,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """Print the emit_verdict PAYLOAD for the dispatching AGENT (race-safe path)."""
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
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs (S84+)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute (conditional band-closure under the W1-1 outcome)
    res = compute()

    # 3. Report NUMBERS first
    print("=== W1-1 upstream resolution (Option-A supersession reading) ===")
    print(f"  upstream gate     : {UPSTREAM_GATE_ID}")
    print(f"  W1-1 verdict      : {res['w1_1_verdict']}  (reason={res['w1_1_resolution_reason']})")
    print(f"  W1-1 audit_sha256 : {res['w1_1_audit_sha'][:16]}...")
    print()
    print("=== H0-residual band-closure NUMBERS ===")
    print(f"  dimensionless relief (exact) : {res['partial_relief_num']}/{res['partial_relief_den']}"
          f" = {res['partial_relief_float']:.8f}  (round-fig {res['roundfig_num']}/{res['roundfig_den']})")
    print(f"  roundfig within 4sf          : {res['roundfig_within_4sf']}  (recompute_ok={res['roundfig_recompute_ok']})")
    print(f"  residual held                : {res['residual_held']:.8f}  (consistent={res['residual_consistent']})")
    print(f"  H0 closure band              : [{res['band_lo']}, {res['band_hi']}]  central {res['band_central']}  lit {res['band_lit']}")
    print(f"  dimensionful draw required   : {res['dimensionful_draw_reqd']:.6f}  (attempted={res['dimensionful_draw_attempted']})")
    print(f"  M_KK^1 scale leg admissible  : {res['scale_leg_admissible']}  (bare-INADMISSIBLE={res['mkk1_inadmissible_bare']}, d_A={res['d_A_dH0']}, deg_T={res['deg_T']})")
    print()
    print("=== CONDITIONAL BRANCH ===")
    print(f"  branch taken                 : {res['branch_taken']}")
    print(f"  relief_total                 : {res['relief_total']:.8f}  ({res['relief_ceiling_pct']:.4f}% ceiling)")
    print(f"  band_closed                  : {res['band_closed']}")
    print(f"  band floor gap (lo - relief) : {res['band_floor_gap']:+.6f}")
    print(f"  residual still held          : {res['residual_still_held']:.8f}")
    print()

    # 4. Save npz
    np.savez(
        OUT_NPZ,
        **{k: np.array(v) for k, v in res.items()},
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 5. Plot
    make_plot(res)
    print()

    # 6. Verdict (composite from the 3-tuple collapse, computed in compute())
    verdict = res["composite_verdict"]  # (local)
    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Companion extra-rows: pin the conditional branch + parity-pin + falsifier #.
    extra_rows = [
        f"# CF-S112-H0-BAND-CLOSURE conditional branch: W1-1={res['w1_1_verdict']} "
        f"-> {res['branch_taken']}; W1-1 audit_sha256={res['w1_1_audit_sha']}",
        f"# H0-relief ceiling (falsifier-relevant) = {res['relief_ceiling_pct']:.4f}% "
        f"(dimensionless 49/800 channel); residual_held={res['residual_still_held']:.6f} "
        f"pinned to the one external M_KK scale {res['M_KK_external_scale']:.4e} GeV",
        "# convention_parity_pin=RATIO-DA-1-PARITY-odd (released branch face; "
        "M_KK^1 d_A=+1 ODD leg, INADMISSIBLE under W1-1 FAIL; corpus §23.0(5) parity selection rule)",
    ]

    print_verdict_payload(
        verdict, res["value"], audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note="CF-S112-H0-BAND-CLOSURE FAIL branch (W1-1 FAIL): H0 relief capped at 6.125% dimensionless channel",
        extra_rows=extra_rows,
    )

    # 7. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} "
          f"(sign={res['sign_verdict']} mag={res['magnitude_verdict']} regime={res['regime_verdict']}; "
          f"wall {wall:.2f}s) ===")
    # Exit 0 = script healthy regardless of scientific verdict (math-scripts.md).
    return 0


if __name__ == "__main__":
    sys.exit(main())
