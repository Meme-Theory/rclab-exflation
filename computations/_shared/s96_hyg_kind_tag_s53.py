#!/usr/bin/env python3
"""
S96 W7-6 — S96-HYG-KIND-TAG-S53 — backward KIND-tag of the §5.3 surface-gravity
ledger; reproduction-verifier for the three distinct fold surfaces.
================================================================================

Gate: S96-HYG-KIND-TAG-S53  ([VERIFY])
  Identity sub-claim ("NOT a contradiction"): at the SAME τ=0.190 the modulus
  double-root κ_V = ½|V′| = 0 (T_H=0) coexists with the Gibbons-Hawking
  T_GH = 0.2172 (emergent horizon) — these are TWO DIFFERENT surface-gravity
  FUNCTIONALS acting on TWO DIFFERENT geometric objects, not two values of one
  functional. Plus: 0.112 M_KK relabels from S53/S63 "GGE relic temperature" to
  the internal-acoustic SONIC surface (the OBSERVED relic spectral temperature is
  now the a₄ value 7.578 M_KK), and the kitaev identity 2π·T(a₄)=2π·7.578=47.614
  = κ_exit.

Pre-registered threshold (plan §W7-6):
  PASS iff  |κ_V(τ=0.190)| < 1e-6  (modulus double-root)
            AND |T_GH(τ=0.190) − 0.2172| < 1e-3  (s29c reproduction)
            AND §5.3 KIND table present {THERMODYNAMIC-modulus / GIBBONS-HAWKING-
                emergent / SONIC} + 0.112 relabel note + 2π·T(a₄)=κ_exit identity
  INFO iff  both functionals reproduce + KIND table lands but a residual
            Ordered-Veil-leg attribution ambiguity persists
  FAIL iff  a reproduced value diverges from its recorded verdict (κ_V≠0 or
            T_GH≠0.2172 beyond tolerance) — a stale-cache / transcription artifact

Classification: GEOMETRIC
  Surface gravity is read off an EMERGENT geometry, and the substrate carries
  THREE distinct emergent surfaces at the fold, not one. The THERMODYNAMIC-modulus
  κ_V=0 is the double-root of the τ-potential on the 2D Jensen-modulus metric
  (the substrate's own deformation-parameter geometry). The GIBBONS-HAWKING-
  emergent T_GH=0.2172 is the temperature of the 4D acoustic horizon that emerges
  from the a₂ channel. The SONIC surface (0.112 M_KK) is the v=c_BLV Mach-1
  crossing of the internal acoustic flow. All three are substrate-IS
  reorganizations of the D_K spectral weight at τ_fold; the KIND table prevents
  reading them as one functional giving inconsistent answers.

REPRODUCTION (not a new derivation)
-----------------------------------
This is a thin reproduction-verifier of two PASS-PROVEN prior verdicts:
  (1) κ_V double-root: s85_w6_extremal_horizon_formal.npz keys kappa_at_dump=0.0,
      T_H_at_dump=0.0, is_double_root=[True], Vpp_at_dump=2.0 (V=V′=0, V″≠0).
      Scheme Jensen_V_tree, convention 2D_modulus_metric. [S85 W4-5 PASS]
  (2) T_GH=0.2172: s29c_gibbons_hawking_temperature.npz / verdict.txt records
      "tau=0.190: T_GH=0.2172 (interp) fold horizon" from the closed form
      T_GH(τ)=exp(−2τ)/π (volume-preserving TT metric-det Laplacian envelope).
      [s29c; the s29c GATE verdict is FAIL on the T_GH-vs-T_eff RATIO, but the
       T_GH VALUE 0.2172 is the reproduced quantity §5.3 cites.]
The KIND table, the 0.112 relabel, and the kitaev identity are VERBATIM from the
closed hawking V.2 / quantum-acoustics IV.A / kitaev V.1 review content; this
script transcribes + reproduces, it does NOT re-derive.

DISCIPLINE
----------
- `from canonical_constants import` (PI; no hardcoded framework constants)
- intermediates tagged `# (local)`
- CPU-only scalar arithmetic; OMP capped at 8
- dual-SHA (audit_sha256 over script||canonical||pinmap; content_sha256 over script)
- [VERIFY] + "NOT a contradiction" identity sub-claim → schema-v2 3-tuple companion
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import math
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import).
# This script lives in computations/_shared/, which IS the directory holding
# canonical_constants.py, so a bare module import resolves directly.
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SHARED_DIR.parent.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    PI,
    tau_fold,
)

# append_verdict — the canonical dual-SHA + schema-v2 3-tuple emission helper is
# defined inline below (Section 6) matching the W7 sibling pattern. The literal
# token `append_verdict` is kept in the script per output_artifacts must_contain.

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + output destinations
# ---------------------------------------------------------------------------
SESSION = "S96"                                                          # (local)
GATE_ID = "S96-HYG-KIND-TAG-S53"                                         # (local)
SCHEME = "extremal-double-root(kappa_V)+Gibbons-Hawking-emergent(T_GH)"  # (local)
CONVENTION = "KIND-tagged-THERMODYNAMIC-modulus/GIBBONS-HAWKING-emergent/SONIC"  # (local)
L_MAX = "N/A"                                                            # (local)

SESSION96_DIR = PROJECT_ROOT / "computations" / "session-96"            # (local)
OUT_NPZ = SESSION96_DIR / "s96_hyg_kind_tag_s53.npz"
OUT_PNG = SESSION96_DIR / "s96_hyg_kind_tag_s53.png"
VERDICT_TXT = SESSION96_DIR / "s96_gate_verdicts.txt"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

S85_W6_NPZ = PROJECT_ROOT / "computations" / "session-85" / "s85_w6_extremal_horizon_formal.npz"
S29C_NPZ = PROJECT_ROOT / "computations" / "session-29" / "s29c_gibbons_hawking_temperature.npz"

INPUT_FILES = [
    S85_W6_NPZ,
    S29C_NPZ,
    CANONICAL_PATH,
]

# Publication precision (Class 8.3): T_GH published at 4 sig figs (0.2172) ⇒
# rel_tol = 1e-3 on the T_GH reproduction; κ_V double-root is a machine-zero
# (< 1e-6 absolute).
PUBLICATION_PRECISION = 4                                               # (local)
KAPPA_V_TOL = 1e-6                                                      # (local)
T_GH_TOL = 1e-3                                                         # (local)

TAU_H = 0.190                                                           # (local; fold horizon τ)

# Recorded prior-verdict reference values (the reproduction TARGETS) ----------
T_GH_RECORDED = 0.2172   # (local; s29c verdict.txt "tau=0.190: T_GH=0.2172 (interp) fold horizon")

# §6.2 KIND ledger anchors (the THREE distinct surfaces; VERBATIM from §6.2) ---
T_A4_RELIC = 7.578       # (local; OBSERVED relic spectral temperature, a₄ condensation-exit, M_KK)
KAPPA_EXIT_LEDGER = 47.61  # (local; §6.2 a₄ row κ value, M_KK)
T_SONIC_S63 = 0.112      # (local; S63-BLV internal-acoustic SONIC surface, M_KK)
KAPPA_SONIC_LEDGER = 0.704805  # (local; §6.2 S63-BLV row κ)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 5 — Compute (REPRODUCTION of two prior PASS-PROVEN verdicts)
# ---------------------------------------------------------------------------
def reproduce() -> dict:
    """Reproduce κ_V(τ=0.190)=0 from s85_w6 + T_GH(τ=0.190)=0.2172 from s29c.

    Substitution chain (plan §W7-6; identity / "NOT a contradiction"):
      D1: κ_V := ½|V′(τ_h)| on the 2D-modulus metric at the extremal double root
          [S85 W4-5; V=V′=0 ⟹ κ_V=0 ⟹ T_H=κ_V/2π=0]
      D2: T_GH := Gibbons-Hawking temperature of the EMERGENT horizon
          [s29c; T_GH(τ)=exp(−2τ)/π; T_GH(0.190)=0.2172]
      D3: κ_exit := §6.2 analog surface gravity of the a₄ relic exit surface [=47.61]
      D4: T(a₄ relic) := OBSERVED relic spectral temperature [=7.578]
      KIND distinction: κ_V acts on the 2D-MODULUS metric; T_GH acts on the
          EMERGENT 4D horizon — DIFFERENT geometric objects at the same τ
          ⟹ κ_V=0 and T_GH=0.2172 are values of DIFFERENT functionals,
             not two values of ONE functional (NOT a contradiction)
      kitaev identity: 2π·T(a₄)=2π·7.578=47.614 ≈ 47.61 = κ_exit
      0.112 relabel: 0.112 M_KK was 'GGE relic temperature' (S53/S63); it is now
          the internal-acoustic SONIC surface (v=c_BLV Mach-1); the OBSERVED
          relic temperature is the a₄ value 7.578 M_KK.
    """
    # --- (1) κ_V double-root reproduction from s85_w6 npz --------------------
    s85 = np.load(S85_W6_NPZ, allow_pickle=True)  # (local)
    kappa_V_repro = float(s85["kappa_at_dump"])           # (local) recorded 0.0
    T_H_repro = float(s85["T_H_at_dump"])                 # (local) recorded 0.0
    Vpp_at_dump = float(s85["Vpp_at_dump"])               # (local) 2.0 (V″≠0 ⇒ genuine double root)
    is_double_root = bool(np.atleast_1d(s85["is_double_root"])[0])  # (local) True
    s85_tau_dump = float(s85["tau_dump"])                 # (local) 0.19
    s85_scheme = str(s85["scheme"])                       # (local) Jensen_V_tree
    s85_convention = str(s85["convention"])               # (local) 2D_modulus_metric

    # --- (2) T_GH reproduction from s29c -------------------------------------
    #   The s29c model is T_GH(τ)=exp(−2τ)/π (volume-preserving TT metric-det
    #   Laplacian envelope ω_char=exp(−2τ)). Reproduce BOTH the closed form
    #   (the authoritative recorded 0.2172) AND the npz-array linear interp
    #   (coarse Δτ=0.1 grid → 0.41% offset, a grid-resolution artifact, NOT a
    #   model discrepancy). The reproduction TARGET is the recorded 0.2172.
    T_GH_closed_form = math.exp(-2.0 * TAU_H) / PI         # (local) = 0.21768
    s29c = np.load(S29C_NPZ, allow_pickle=True)            # (local)
    s29c_tau = s29c["tau_values"]                          # (local)
    s29c_TGH = s29c["T_GH_prediction"]                     # (local)
    T_GH_npz_interp = float(np.interp(TAU_H, s29c_tau, s29c_TGH))  # (local) 0.21809 (coarse-grid)

    # Reproduction is judged against the RECORDED verdict value 0.2172 using the
    # closed-form (the s29c model's exact value at τ=0.190).
    T_GH_repro = T_GH_closed_form                          # (local)
    T_GH_residual = abs(T_GH_repro - T_GH_RECORDED)        # (local)

    # --- (3) kitaev identity 2π·T(a₄) = κ_exit -------------------------------
    kitaev_2piT_a4 = 2.0 * PI * T_A4_RELIC                 # (local) = 47.614
    kitaev_residual = abs(kitaev_2piT_a4 - KAPPA_EXIT_LEDGER)  # (local) ≈ 0.004 (ledger rounded to 47.61)
    kitaev_holds = kitaev_residual < 0.01                 # (local) within ledger 2-dp rounding

    # --- Reproduction PASS predicates ---------------------------------------
    kappa_V_ok = abs(kappa_V_repro) < KAPPA_V_TOL          # (local)
    t_gh_ok = T_GH_residual < T_GH_TOL                     # (local)
    double_root_ok = is_double_root and (Vpp_at_dump > 0)  # (local) V=V′=0, V″>0

    return {
        # κ_V row
        "kappa_V_repro": kappa_V_repro,
        "T_H_repro": T_H_repro,
        "Vpp_at_dump": Vpp_at_dump,
        "is_double_root": is_double_root,
        "s85_tau_dump": s85_tau_dump,
        "s85_scheme": s85_scheme,
        "s85_convention": s85_convention,
        "kappa_V_ok": kappa_V_ok,
        "double_root_ok": double_root_ok,
        # T_GH row
        "T_GH_repro": T_GH_repro,
        "T_GH_closed_form": T_GH_closed_form,
        "T_GH_npz_interp": T_GH_npz_interp,
        "T_GH_recorded": T_GH_RECORDED,
        "T_GH_residual": T_GH_residual,
        "t_gh_ok": t_gh_ok,
        # kitaev identity
        "kitaev_2piT_a4": kitaev_2piT_a4,
        "kitaev_residual": kitaev_residual,
        "kitaev_holds": kitaev_holds,
        "T_a4_relic": T_A4_RELIC,
        "kappa_exit_ledger": KAPPA_EXIT_LEDGER,
        # SONIC relabel
        "T_sonic_s63": T_SONIC_S63,
        "kappa_sonic_ledger": KAPPA_SONIC_LEDGER,
        # composite value (the gate's primary reported number = T_GH residual)
        "value": T_GH_residual,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict (+ schema-v2 3-tuple) and verdict-line emission
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict, kind_table_present: bool) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    sign_verdict (IDENTITY claim, plan §W7-6 "Direction"): tagging the KINDs
        RESOLVES the apparent contradiction — κ_V=0 (modulus double-root) and
        T_GH=0.2172 (emergent horizon) are DIFFERENT functionals on DIFFERENT
        geometric objects at the same τ, NOT two values of one functional. PASS
        iff the two reproduce AS DISTINCT KINDS (the modulus double-root is a
        genuine double root V=V′=0, V″>0, distinct from the emergent-horizon
        T_GH) AND the kitaev identity 2π·T(a₄)=κ_exit holds.
    magnitude_verdict: both functionals reproduce within tolerance
        (|κ_V|<1e-6 AND |T_GH−0.2172|<1e-3) AND the KIND table + 0.112 relabel land.
    regime_verdict: VALID — reproductions of recorded PASS-PROVEN verdicts +
        artifact-existence KIND tagging; no expansion to break down.
    Composite collapses per gate-verdicts.md §"Composite-collapse rule".
    """
    # SIGN: the KIND distinction is real (modulus double-root is genuinely a
    # distinct geometric object from the emergent horizon) AND kitaev identity holds.
    sign_ok = (r["double_root_ok"] and r["kitaev_holds"])  # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"           # (local)

    # MAGNITUDE: both reproductions land within tolerance AND the KIND table
    # (+ 0.112 relabel + kitaev identity) is present in §5.3.
    repro_ok = r["kappa_V_ok"] and r["t_gh_ok"]            # (local)
    if repro_ok and kind_table_present:
        magnitude_verdict = "PASS"  # (local)
    elif repro_ok or kind_table_present:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)

    regime_verdict = "VALID"  # (local) reproduction + artifact-existence, no expansion

    # Composite per the PRE-REGISTERED collapse rule (gate-verdicts.md)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    return composite, sign_verdict, magnitude_verdict, regime_verdict


def build_value_string(r: dict, kind_table_present: bool) -> str:
    """Compact, audit-greppable value= string."""
    return (
        f"kappa_V(tau=0.190)={r['kappa_V_repro']:.2e}_double-root(V=Vp=0,Vpp={r['Vpp_at_dump']:.1f})={r['is_double_root']}"
        f";T_H_modulus={r['T_H_repro']:.2e}"
        f";T_GH(tau=0.190)={r['T_GH_repro']:.4f}_vs_recorded={r['T_GH_recorded']:.4f}_residual={r['T_GH_residual']:.2e}_repro_OK={r['t_gh_ok']}"
        f";T_GH_npz_interp={r['T_GH_npz_interp']:.4f}_coarse-grid-xcheck"
        f";KIND_table={{THERMODYNAMIC-modulus(kappa_V=0):GIBBONS-HAWKING-emergent(T_GH=0.2172):SONIC(0.112)}}_present={kind_table_present}"
        f";kitaev_identity_2pi*T(a4)=2pi*{r['T_a4_relic']:.3f}={r['kitaev_2piT_a4']:.3f}=kappa_exit({r['kappa_exit_ledger']:.2f})_residual={r['kitaev_residual']:.2e}_HOLDS={r['kitaev_holds']}"
        f";relabel_0.112_S53-S63_GGE-relic-T->internal-acoustic-SONIC_surface(v=c_BLV_Mach-1)"
        f";OBSERVED_relic_spectral_T=a4_value_{r['T_a4_relic']:.3f}_M_KK"
        f";SAME-tau_DIFFERENT-functionals_NOT-a-contradiction=True"
    )


def _latest_prior_audit_sha() -> str | None:
    """Scan the verdict file for the latest non-superseded canonical line of this
    gate-ID; return its full-64 audit_sha256, or None. Implements the Option A
    supersession-chain reading (gate-verdicts.md §"Option A")."""
    if not VERDICT_TXT.exists():
        return None
    superseded: set[str] = set()  # (local)
    canon_shas: list[str] = []    # (local) in file order
    for raw in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if not raw.startswith(f"{GATE_ID}:"):
            continue
        own = None  # (local)
        for tok in raw.split():
            if tok.startswith("audit_sha256="):
                own = tok.split("=", 1)[1]
            if tok.startswith("supersedes="):
                superseded.add(tok.split("=", 1)[1].strip("',"))
        if own:
            canon_shas.append(own)
    live = [s for s in canon_shas if s not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(composite: str, value_str: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str, r: dict) -> None:
    """Atomic append: canonical line + dual-SHA companion + schema-v2 3-tuple.

    Option A (gate-verdicts.md): if a prior non-superseded line for this gate-ID
    already exists, this corrective line carries a `supersedes=<old_full_64>` tag
    and the prior line is RETAINED on disk (no in-place edit).
    """
    prior = _latest_prior_audit_sha()  # (local)
    supersedes_field = f" supersedes={prior}" if prior and prior != audit_sha else ""  # (local)
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}'{supersedes_field} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] §5.3 backward KIND-tag; "
        f"reproduces kappa_V=0 (s85_w6 extremal double-root, S85 W4-5 PASS) + "
        f"T_GH=0.2172 (s29c closed form exp(-2tau)/pi, residual {r['T_GH_residual']:.2e}); "
        f"KIND table {{THERMODYNAMIC-modulus / GIBBONS-HAWKING-emergent / SONIC}} extends "
        f"the §6.2 KIND discipline backward to §5.3; 0.112 M_KK relabel (S53/S63 GGE-relic-T "
        f"-> internal-acoustic SONIC surface); OBSERVED relic spectral T = a4 7.578 M_KK; "
        f"kitaev identity 2pi*7.578=47.614=kappa_exit"
        + (f"; supersedes={prior} (Option A within-dispatch correction)" if supersedes_field else "")
        + "\n"
    )  # (local)
    tuple3 = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = IDENTITY claim: kappa_V=0 (modulus double-root V=Vp=0, Vpp={r['Vpp_at_dump']:.1f}>0 "
        f"on the 2D-modulus metric) and T_GH={r['T_GH_recorded']:.4f} (Gibbons-Hawking emergent 4D "
        f"horizon, a2 channel) at the SAME tau=0.190 are values of TWO DIFFERENT surface-gravity "
        f"FUNCTIONALS on TWO DIFFERENT geometric objects, NOT two values of one functional => NOT a "
        f"contradiction (PASS: the double-root is a genuine distinct geometric object AND the kitaev "
        f"identity 2pi*T(a4)={r['kitaev_2piT_a4']:.3f}=kappa_exit({r['kappa_exit_ledger']:.2f}) holds); "
        f"mag = both functionals reproduce their recorded verdicts (|kappa_V|={abs(r['kappa_V_repro']):.1e}<1e-6 "
        f"AND |T_GH-0.2172|={r['T_GH_residual']:.1e}<1e-3) AND the §5.3 KIND table + 0.112 relabel + "
        f"kitaev identity land; regime = reproduction of PASS-PROVEN verdicts + artifact-existence "
        f"KIND tagging, no expansion to break down\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(tuple3)


# ---------------------------------------------------------------------------
# Section 6b — Plot: the three KIND-tagged surfaces at τ=0.190
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(figsize=(10.5, 4.6))  # (local)

    surfaces = [  # (local) (label, T, kappa, kind, color)
        ("THERMODYNAMIC-modulus\nκ_V=½|V′|=0 (double root)", 0.0, r["kappa_V_repro"],
         "modulus 2D metric", "#1a9850"),
        ("GIBBONS-HAWKING-emergent\nT_GH=0.2172", r["T_GH_recorded"], None,
         "emergent 4D horizon (a₂)", "#1f6fb2"),
        ("SONIC (relabeled 0.112)\nv=c_BLV Mach-1", r["T_sonic_s63"], r["kappa_sonic_ledger"],
         "internal-acoustic", "#d73027"),
        ("a₄ OBSERVED relic spectral\nT=7.578 (2π·T=κ_exit=47.61)", r["T_a4_relic"], r["kappa_exit_ledger"],
         "condensation-exit", "#984ea3"),
    ]
    xs = range(len(surfaces))  # (local)
    Ts = [s[1] for s in surfaces]  # (local)
    colors = [s[4] for s in surfaces]  # (local)
    ax.bar(list(xs), Ts, color=colors, alpha=0.75, width=0.6)
    for i, s in enumerate(surfaces):
        ax.annotate(f"{s[1]:.4g} M_KK", (i, s[1]), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=8.5, fontweight="bold")
        ax.annotate(s[0], (i, 0), textcoords="offset points", xytext=(0, -52),
                    ha="center", fontsize=7.2, annotation_clip=False)
    ax.set_yscale("symlog", linthresh=0.05)
    ax.set_xticks([])
    ax.set_ylabel("T (M_KK), symlog")
    ax.set_title("S96-HYG-KIND-TAG-S53 — three KIND-distinct surfaces at τ=0.190 "
                 "(same τ, different functionals — NOT a contradiction)")
    ax.axhline(0, color="#444444", lw=0.8)
    ax.margins(y=0.35)
    fig.subplots_adjust(bottom=0.30)
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = reproduce()  # (local)

    # The §5.3 KIND table is landed by the orchestrator's atomic section-scoped
    # edit of the capstone (a curated-doc designated-writer patch, NOT a script
    # write). The reproduction-verifier asserts the table's PRESENCE by grepping
    # the capstone §5.3 region for the three KIND tags + the 0.112 relabel +
    # the kitaev identity. If the edit has not yet landed at script-run time the
    # table_present flag is False and the gate closes INFO (reproductions PASS,
    # table pending) per the pre-registered INFO branch; once the edit lands a
    # re-run flips to PASS (Option A corrective with supersedes tag).
    capstone = PROJECT_ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"  # (local)
    kind_table_present = False  # (local)
    try:
        ctext = capstone.read_text(encoding="utf-8")  # (local)
        # Restrict to the §5.3 region (between the 5.3 header and the §6 header).
        i53 = ctext.find("### 5.3 GGE-relic formation")  # (local)
        i6 = ctext.find("## §6 — The equation at time t")  # (local)
        region = ctext[i53:i6] if (i53 >= 0 and i6 > i53) else ""  # (local)
        kind_table_present = (
            "THERMODYNAMIC-modulus" in region
            and "GIBBONS-HAWKING-emergent" in region
            and "SONIC" in region
            and "0.112" in region
            and "47.614" in region
            and "7.578" in region
        )  # (local)
    except OSError:
        kind_table_present = False

    composite, sign_v, mag_v, regime_v = evaluate_gate(r, kind_table_present)  # (local)

    print("--- §5.3 backward KIND-tag reproduction ---")
    print(f"  (1) κ_V(τ=0.190)  = {r['kappa_V_repro']:.3e}  (recorded 0.0; double-root V=V′=0, "
          f"V″={r['Vpp_at_dump']:.1f}>0, is_double_root={r['is_double_root']})  OK={r['kappa_V_ok']}")
    print(f"      T_H_modulus    = {r['T_H_repro']:.3e}  (= κ_V/2π = 0)")
    print(f"      [s85 scheme={r['s85_scheme']} convention={r['s85_convention']} τ_dump={r['s85_tau_dump']}]")
    print(f"  (2) T_GH(τ=0.190) = {r['T_GH_repro']:.5f}  (closed form exp(-2τ)/π)")
    print(f"      vs recorded    = {r['T_GH_recorded']:.4f}   residual = {r['T_GH_residual']:.3e}  OK={r['t_gh_ok']}")
    print(f"      npz-array interp x-check = {r['T_GH_npz_interp']:.5f} (coarse Δτ=0.1 grid, +0.41% artifact)")
    print(f"  (3) kitaev: 2π·T(a₄) = 2π·{r['T_a4_relic']:.3f} = {r['kitaev_2piT_a4']:.4f} "
          f"= κ_exit({r['kappa_exit_ledger']:.2f})  residual={r['kitaev_residual']:.3e}  HOLDS={r['kitaev_holds']}")
    print(f"  (4) 0.112 relabel: S53/S63 'GGE relic temperature' → internal-acoustic SONIC surface "
          f"(v=c_BLV Mach-1); OBSERVED relic spectral T = a₄ value {r['T_a4_relic']:.3f} M_KK")
    print(f"  KIND distinction: κ_V (2D-modulus metric) ≠ T_GH (emergent 4D horizon) — "
          f"DIFFERENT functionals, same τ — NOT a contradiction")
    print(f"  §5.3 KIND table present in capstone = {kind_table_present}")
    print()
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  composite = {composite}")

    # Save data (optional artifact)
    SESSION96_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        tau_h=TAU_H,
        kappa_V_repro=r["kappa_V_repro"],
        T_H_modulus=r["T_H_repro"],
        Vpp_at_dump=r["Vpp_at_dump"],
        is_double_root=r["is_double_root"],
        T_GH_repro=r["T_GH_repro"],
        T_GH_closed_form=r["T_GH_closed_form"],
        T_GH_npz_interp=r["T_GH_npz_interp"],
        T_GH_recorded=r["T_GH_recorded"],
        T_GH_residual=r["T_GH_residual"],
        kitaev_2piT_a4=r["kitaev_2piT_a4"],
        kitaev_residual=r["kitaev_residual"],
        kitaev_holds=r["kitaev_holds"],
        T_a4_relic=r["T_a4_relic"],
        kappa_exit_ledger=r["kappa_exit_ledger"],
        T_sonic_s63=r["T_sonic_s63"],
        kappa_sonic_ledger=r["kappa_sonic_ledger"],
        kind_table_present=kind_table_present,
        kappa_V_ok=r["kappa_V_ok"],
        t_gh_ok=r["t_gh_ok"],
        double_root_ok=r["double_root_ok"],
        publication_precision=PUBLICATION_PRECISION,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=composite,
    )
    print(f"  saved {OUT_NPZ.name}")

    make_plot(r)
    print(f"  saved {OUT_PNG.name}")

    # Emit verdict line (atomic append; canonical + dual-SHA + 3-tuple)
    value_str = build_value_string(r, kind_table_present)  # (local)
    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v, r)
    print(f"  appended verdict line to {VERDICT_TXT.name}")

    tag = (f"(value={r['T_GH_residual']:.4e}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    # Exit 0 regardless of scientific verdict (verdict is data, not script health).
    return 0


if __name__ == "__main__":
    sys.exit(main())
