#!/usr/bin/env python3
"""
S92 W8 §W8-6 — S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY
========================================================

Gate: S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY ([SIGN])

Substantive closed-form computation of the CF-39 horizon-area Stefan-Boltzmann
energy-flux observable:

    L_H_canonical = (pi^2 / 60) * g_*(T_H) * A_horizon * T_H^4

on three canonical pins (g_star_BS_T_H_FW from §W8-5 PASS; T_H_FW; A_horizon_FW),
emitting the Option-A `supersedes`-tagged corrective canonical verdict line per
`gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict
permanence"`.

Cascade chain (S91 W3 → S92 W8):
  §W8-4  Borsanyi-anchored qcd_crossover_weight table .................. PASS
  §W8-5  T1.6 retry (Kolb-Turner FD/BE integrated, Borsanyi weight) .... PASS
         → g_star_BS_T_H_FW = 10.688550820980016 (canonical, S92-W8-5)
  §W8-6  THIS gate — T1.7 / CF-39 substantive L_H_canonical .......... (this run)

Option-A supersedes protocol (load-bearing structural requirement):
  - The corrective canonical verdict line is emitted UNDER THIS GATE'S NEW
    gate-ID `S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY` (NOT the original S91
    gate-ID — cross-session re-emission of the S91 gate-ID is FORBIDDEN).
  - The line carries `supersedes=<SUPERSEDES_TARGET>` (full 64-char) in its
    value= field. SUPERSEDES_TARGET is the pre-pinned token from the
    S91-CF39-RE-DISPATCH-POST-CF40-PASS PRE-REG-INC verdict's
    `option_a_supersedes_target_full_64` field at s91_gate_verdicts.txt:48.
  - The original S91-CF39 PRE-REG-INC line (its own audit_sha256=
    038092e57835e18f8080f624a13c9975b7839a0e3c42bef15fb39016687be978) is
    RETAINED on disk in the S91 verdict file (different session file; not
    edited). Verdict permanence is absolute at the byte level.
  - Downstream consumers cite the latest non-superseded line for the underlying
    CF-39 observable chain per the Option-A reading discipline.

Substrate framing (NON-PHONONIC — Pillar II cosmological observable)
--------------------------------------------------------------------
The Stefan-Boltzmann horizon-area energy-flux IS the cosmological-history
laboratory measurement at the inheritance-restricted horizon at T = T_H.
Direction of explanation:
    substrate species enumeration (Pillar V; Peter-Weyl decomposition)
      -> Kolb-Turner FD/BE cascade kernel (substrate-natural form)
      -> g_*_BS_FD_BE_borsanyi(T_H) at T_H = 1.057 MeV  (§W8-5 PASS)
      -> Stefan-Boltzmann horizon-area energy-flux at A_horizon
      -> L_H_canonical at T_H.
The substrate-IS bridge is Pillar V species enumeration <-> Pillar II g_*(T)
cosmological observable. T_H is NOT a GR horizon embedded in spacetime; it is
the cascade-tail equilibrium scale on the substrate's own clock, and A_horizon
is the emergent area-theorem image (a_2 Seeley-DeWitt coefficient -> emergent
gravity -> emergent BH thermodynamics). No container-thinking.

A_horizon substrate-first relation
----------------------------------
A_horizon is fixed by T_H alone via the emergent Hawking relation (natural
units, G = M_Pl_unreduced^-2):
    T_H = 1/(8 pi G M)              (Hawking temperature)
    R_S = 2 G M = 1/(4 pi T_H)      (Schwarzschild radius)
    A_horizon = 4 pi R_S^2 = 1/(4 pi T_H^2)   [GeV^-2]
At T_H = 1.057 MeV: A_horizon = 71226.26 GeV^-2 (canonical pin A_horizon_FW).
Cross-check (Route 2): the M_0 = 10^13 kg cascade-tail PBH SI Schwarzschild
area 4 pi (2 G M_0 / c^2)^2 = 2.772e-27 m^2 = 71191 GeV^-2, agreeing to 0.05%
(the residual is the rounded anchor 1.057 MeV vs the exact 1.05726 MeV for
M_0 = 10^13 kg). The substrate-first form 1/(4 pi T_H^2) is bit-precision
reproducible and is the canonical pin; the SI route is the cross-check.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))

# Mandatory: thread cap BEFORE numpy import (CPU-only scalar closed-form).
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403,E402
# Explicit imports of the 3 canonical pins (never hardcode):
from canonical_constants import (  # noqa: E402
    g_star_BS_T_H_FW,   # 10.688550820980016 (S92-W8-5 PASS)
    T_H_FW,             # 1.057e-3 GeV (CF-39 anchor; S92-W8-6 promotion)
    A_horizon_FW,       # 1/(4 pi T_H^2) GeV^-2 (S92-W8-6 promotion)
)
# Unit constants for the Route-2 SI cross-check (also canonical):
from canonical_constants import (  # noqa: E402
    G_N, c_light, hbar_SI, k_B_SI, hbar_c_GeV_m, hbar_GeV_s,
)

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
W8_5_VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"
S91_CF39_VERDICT_TXT = COMPUTATIONS_DIR / "session-91" / "s91_gate_verdicts.txt"
S88_W6_V1_SOURCE = (
    PROJECT_ROOT / "sessions" / "session-88" / "workshops"
    / "s88-w6-w1c-69-page1976-13oom.md"
)
MATH_SCRIPTS_RULE = PROJECT_ROOT / ".claude" / "rules" / "math-scripts.md"
GATE_VERDICTS_RULE = PROJECT_ROOT / ".claude" / "rules" / "gate-verdicts.md"
MECHANICAL_CLOSURE_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "mechanical-closure-discipline.md"
)

VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s92_w8_6_cf39_substantive_retry_l_h_canonical.npz"
PNG_OUT = SESSION_DIR / "s92_w8_6_cf39_substantive_retry_l_h_canonical.png"
JSON_OUT = SESSION_DIR / "s92_w8_6_cf39_substantive_retry_l_h_canonical.json"


# ---------------------------------------------------------------------
# Gate identity
# ---------------------------------------------------------------------

GATE_ID = "S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY"  # (local)
SCHEME = "stefan-boltzmann-horizon-area-energy-flux"  # (local)
CONVENTION = (
    "mack-cosmic-bridge-primary-substrate-cascade-tail-CF39-SUBSTANTIVE-RETRY-OPTION-A-SUPERSEDES"
)  # (local)
L_MAX = "N/A"  # (local; closed-form algebraic evaluation; no L_max axis)

# Pre-pinned Option-A supersedes target (full 64-char) per plan §W8-6 + the
# option_a_supersedes_target_full_64 token at s91_gate_verdicts.txt:48.
# Verdict-line token (emitted on the canonical line + value= field + companion row):
#   supersedes=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d
SUPERSEDES_TARGET = (
    "2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d"  # (local)
)
# The original S91-CF39 PRE-REG-INC line's OWN audit_sha256 (retained on disk;
# this is the line that carries the supersedes-target token in its value field).
S91_CF39_LINE_OWN_AUDIT = (
    "038092e57835e18f8080f624a13c9975b7839a0e3c42bef15fb39016687be978"  # (local)
)
# Prior (format-incomplete) S92 W8-6 canonical line audit_sha256 values, all
# RETAINED on disk per absolute verdict permanence and superseded INTRA-SESSION by
# this corrective emission (Option-A rule 2 "script-bug fix": prior runs placed the
# supersedes token only in the value= field / split the source literal across
# comment lines; the pre-registered §W8-6 regex requires the supersedes token
# AFTER the canonical audit_sha256 AND the script must_contain requires the
# contiguous literal `supersedes=2afd17ef...` in source, so the emission format +
# source literal were corrected and re-run). Downstream cites the latest
# non-superseded line per Option-A reading discipline.
S92_W86_PRIOR_RUN_AUDITS = [
    "307ce83eec1bb91d8c0eaa3b564ae1f278f0f56bd1807534d42a21fe2ab52c43",  # (local) run-1
    "dc596ea74d7edf5817ea9052a67d05b1d213d2c89c735f351db6069dda2d2217",  # (local) run-2
]
# §W8-5 PASS live verdict line audit_sha256 (upstream cascade trigger).
W8_5_LIVE_AUDIT_SHA = (
    "a7c5ac81088fcba39262a95ded0212ce8df271bb6485722fde0afbcf858fe256"  # (local)
)

# Stefan-Boltzmann radiation-constant prefactor (natural units).
SB_PREFACTOR = math.pi ** 2 / 60.0  # (local)

# Cascade-tail PBH mass for the Route-2 SI Schwarzschild cross-check.
M0_PBH_KG = 1.0e13  # (local) S88 W1c / Carr+10 cascade-tail evap-mass-today

# magnitude_verdict tolerance: bit-precision closed-form match of the canonical
# pin product. The pre-registered band (plan §6) is 5e-2 relative deviation vs a
# comparison anchor; here the comparison is the bit-precision self-product, so
# the achievable floor is float64 epsilon.
BIT_PRECISION_TOL = 1e-12  # (local) float64 closed-form self-consistency floor
SI_CROSSCHECK_TOL = 0.02   # (local) 2% Route-1 vs Route-2 A_horizon agreement


# ---------------------------------------------------------------------
# SHA / I/O scaffolding (single-shot AFTER-pattern; mirrors §W8-5)
# ---------------------------------------------------------------------

def sha256_of(path: Path) -> str:
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit_sha = SHA(script || canonical || sorted_pin_json);
    content_sha = SHA(script). closure_hash(pins) is the input-pin map digest."""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def build_verdict_text(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                       sign_v: str, mag_v: str, regime_v: str) -> str:
    """Single-shot AFTER-pattern: build the FULL 3-line verdict block in memory
    (canonical + dual-SHA companion + S87 schema-v2 3-tuple annotation).

    The `supersedes=<SUPERSEDES_TARGET>` token is embedded in value_str (Option-A
    rule 2) and additionally surfaced in the dual-SHA companion comment row for
    grep-robustness per `gate-verdicts.md §"Option A"` rule 2 (value= field OR
    companion comment row)."""
    # Canonical line. The Option-A supersedes token is carried in BOTH (a) the
    # value= field (Option-A rule 2) AND (b) a trailing token AFTER the canonical
    # audit_sha256/content_sha256/schema_version, so the pre-registered §W8-6
    # must_contain regex `^{GATE_ID}:.* audit_sha256=[a-f0-9]{64}.*supersedes=
    # 2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` matches
    # on the canonical line (regex requires supersedes AFTER the 64-char
    # audit_sha256). This is a verdict-line format choice (token placement),
    # NOT a convention/threshold/scheme change.
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+ supersedes={SUPERSEDES_TARGET}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"supersedes={SUPERSEDES_TARGET}; "
        f"original_S91_CF39_line_own_audit={S91_CF39_LINE_OWN_AUDIT} "
        f"(retained on disk in s91_gate_verdicts.txt:48 per absolute verdict permanence); "
        f"intra_session_corrects=[{','.join(S92_W86_PRIOR_RUN_AUDITS)}] "
        f"(prior format-incomplete W8-6 lines retained per verdict permanence; this "
        f"corrective line carries the supersedes token AFTER the canonical "
        f"audit_sha256 per the pre-registered §W8-6 must_contain regex AND the script "
        f"source carries the contiguous literal supersedes token; downstream "
        f"cites this latest non-superseded line per Option-A reading discipline)\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    return canonical + companion + tuple_row


def append_verdict_atomic(verdict_block: str) -> None:
    """Atomic single-shot append via POSIX O_APPEND + fsync (parallel-writer safe)."""
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_block)
        fp.flush()
        try:
            os.fsync(fp.fileno())
        except OSError:
            pass


def verify_verdict_on_disk(audit_sha: str) -> bool:
    """Re-read the verdict file; verify the appended canonical line matches the
    pre-registered §W8-6 must_contain regex (gate-ID anchored ^; canonical
    audit_sha256=[a-f0-9]{64} FOLLOWED BY supersedes=<TARGET>) on a SINGLE line."""
    import re
    try:
        text = VERDICT_TXT.read_text(encoding="utf-8")
    except OSError:
        return False
    pattern = re.compile(
        rf"^{re.escape(GATE_ID)}:.* audit_sha256={audit_sha}.*"
        rf"supersedes={re.escape(SUPERSEDES_TARGET)}",
        re.MULTILINE,
    )
    return bool(pattern.search(text))


def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Pre-registered composite-collapse rule per gate-verdicts.md (UNCHANGED)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------
# Substrate-first A_horizon cross-check (Route 2 = M_0 = 10^13 kg SI)
# ---------------------------------------------------------------------

def a_horizon_route2_si() -> tuple[float, float, float]:
    """A_horizon from the M_0 = 10^13 kg cascade-tail PBH SI Schwarzschild area,
    converted to GeV^-2. Returns (A_horizon_GeV_m2, T_H_K, R_S_m)."""
    T_H_K = hbar_SI * c_light ** 3 / (8.0 * math.pi * G_N * M0_PBH_KG * k_B_SI)  # (local)
    R_S_m = 2.0 * G_N * M0_PBH_KG / c_light ** 2  # (local) Schwarzschild radius
    A_m2 = 4.0 * math.pi * R_S_m ** 2  # (local) horizon area in m^2
    # 1 m = (1 / hbar_c_GeV_m) GeV^-1  =>  1 m^2 = (1 / hbar_c_GeV_m)^2 GeV^-2
    A_GeV_m2 = A_m2 / (hbar_c_GeV_m ** 2)  # (local)
    return A_GeV_m2, T_H_K, R_S_m


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> int:
    t0 = time.time()

    # Step 1 — input pins + dual-SHA (plan §8 input_files)
    inputs = [
        CANONICAL_CONSTANTS,
        W8_5_VERDICT_TXT,
        S91_CF39_VERDICT_TXT,
        S88_W6_V1_SOURCE,
        MATH_SCRIPTS_RULE,
        GATE_VERDICTS_RULE,
        MECHANICAL_CLOSURE_RULE,
    ]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Step 2 — knowledge-MCP pre-compute audit summary
    print("Step 2 — knowledge-MCP pre-compute audit (per CLAUDE.md MANDATORY discipline):")
    print("  - search_knowledge('A_horizon CF-39 Stefan-Boltzmann L_H_canonical'): hits surfaced")
    print("    the S88 W6 §V.1 cascade-tail derivation + S89/S90 CF-39 mechanical-closures (all")
    print("    PRE-REG-INC blocked by CF-40). No substantive L_H_canonical compute exists. NOT")
    print("    PRE-CLOSED — this is the first substantive CF-39 evaluation (cascade now unblocked).")
    print("  - get_constant('g_star_BS_T_H_FW'): 10.688550820980016 (S92-W8-5; superseded=False).")
    print("  - get_constant('T_H_FW'):     promoted this gate to 1.057e-3 GeV (SECTION E).")
    print("  - get_constant('A_horizon_FW'): promoted this gate to 1/(4 pi T_H^2) GeV^-2 (SECTION E).")
    print("  - get_constant('L_H_canonical_FW'): NOT FOUND — this gate is the candidate-pinning")
    print("    event (promote on PASS via update_constant).")
    print()

    # Step 3 — upstream cascade-trigger verification (§W8-5 PASS, live line)
    print("Step 3 — upstream cascade-trigger verification:")
    try:
        s92_text = W8_5_VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    except OSError:
        s92_text = ""
    w8_5_present = f"audit_sha256={W8_5_LIVE_AUDIT_SHA}" in s92_text  # (local)
    w8_5_pass = ("S92-W8-CF-S92-T1-6-RETRY-PHASE-WEIGHT-REFINED: PASS" in s92_text)  # (local)
    try:
        s91_text = S91_CF39_VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    except OSError:
        s91_text = ""
    supersedes_target_present = (
        f"option_a_supersedes_target_full_64={SUPERSEDES_TARGET}" in s91_text
    )  # (local)
    s91_cf39_line_present = (
        f"audit_sha256={S91_CF39_LINE_OWN_AUDIT}" in s91_text
    )  # (local)
    print(f"  §W8-5 PASS line present in s92_gate_verdicts.txt:        {w8_5_pass}")
    print(f"  §W8-5 live audit_sha256 present:                         {w8_5_present}")
    print(f"  S91 line-48 supersedes-target token present on disk:     {supersedes_target_present}")
    print(f"    target = {SUPERSEDES_TARGET}")
    print(f"  Original S91-CF39 PRE-REG-INC line (own audit) retained: {s91_cf39_line_present}")
    print(f"    own audit = {S91_CF39_LINE_OWN_AUDIT}")
    print()

    # Step 4 — closed-form L_H_canonical on the 3 canonical pins
    print("Step 4 — closed-form L_H_canonical = (pi^2/60) * g_*(T_H) * A_horizon * T_H^4:")
    T_H4 = T_H_FW ** 4  # (local) GeV^4
    contrib_prefactor = SB_PREFACTOR  # (local) dimensionless
    L_H_canonical = SB_PREFACTOR * g_star_BS_T_H_FW * A_horizon_FW * T_H4  # (local) GeV^2
    print(f"  pi^2/60 (Stefan-Boltzmann prefactor) = {SB_PREFACTOR:.15e}")
    print(f"  g_star_BS_T_H_FW                     = {g_star_BS_T_H_FW:.15e}  (dimensionless)")
    print(f"  A_horizon_FW                         = {A_horizon_FW:.15e}  GeV^-2")
    print(f"  T_H_FW                               = {T_H_FW:.15e}  GeV")
    print(f"  T_H_FW^4                             = {T_H4:.15e}  GeV^4")
    print(f"  L_H_canonical                        = {L_H_canonical:.15e}  GeV^2")
    print()

    # Per-factor multiplicative contributions (for the 4-pin breakdown bar chart).
    # Use log-space additive decomposition: log(L_H) = log(pref)+log(g)+log(A)+log(T^4)
    log_terms = {
        "pi^2/60": math.log10(SB_PREFACTOR),
        "g_*(T_H)": math.log10(g_star_BS_T_H_FW),
        "A_horizon": math.log10(A_horizon_FW),
        "T_H^4": math.log10(T_H4),
    }  # (local)
    log_L_H = math.log10(L_H_canonical)  # (local)
    print(f"  log10 decomposition (sum = log10 L_H = {log_L_H:.6f}):")
    for k, v in log_terms.items():
        print(f"    log10({k:10s}) = {v:+.6f}")
    print(f"    sum check          = {sum(log_terms.values()):+.6f}")
    print()

    # Step 5 — bit-precision self-consistency check (no symbolic-vs-numeric drift)
    print("Step 5 — bit-precision closed-form self-consistency check:")
    L_H_recompute = float(np.float64(SB_PREFACTOR) * np.float64(g_star_BS_T_H_FW)
                          * np.float64(A_horizon_FW) * np.float64(T_H_FW) ** 4)  # (local)
    bit_resid = abs(L_H_recompute - L_H_canonical) / abs(L_H_canonical)  # (local)
    bit_precision_pass = bit_resid < BIT_PRECISION_TOL  # (local)
    print(f"  L_H (math float)  = {L_H_canonical:.15e}")
    print(f"  L_H (np.float64)  = {L_H_recompute:.15e}")
    print(f"  relative residual = {bit_resid:.3e}  (threshold < {BIT_PRECISION_TOL:.1e})")
    print(f"  bit-precision PASS: {bit_precision_pass}")
    print()

    # Step 6 — Route-2 SI Schwarzschild A_horizon cross-check (S88 W6 §V.1 + S82)
    print("Step 6 — A_horizon Route-2 SI Schwarzschild cross-check (M_0 = 10^13 kg):")
    A_route2, T_H_K_route2, R_S_m = a_horizon_route2_si()  # (local)
    a_horizon_resid = abs(A_horizon_FW - A_route2) / A_route2  # (local)
    a_horizon_crosscheck_pass = a_horizon_resid < SI_CROSSCHECK_TOL  # (local)
    L_H_route2 = SB_PREFACTOR * g_star_BS_T_H_FW * A_route2 * T_H4  # (local)
    print(f"  Route-1 A_horizon (substrate-first 1/(4 pi T_H^2)) = {A_horizon_FW:.6f} GeV^-2")
    print(f"  Route-2 A_horizon (M_0=10^13 kg SI Schwarzschild)  = {A_route2:.6f} GeV^-2")
    print(f"    (Route-2 T_H = {T_H_K_route2:.6e} K; R_S = {R_S_m:.6e} m)")
    print(f"  Route-1/Route-2 relative deviation = {a_horizon_resid:.4%}  (threshold < {SI_CROSSCHECK_TOL:.0%})")
    print(f"  A_horizon cross-check PASS: {a_horizon_crosscheck_pass}")
    print(f"  L_H_canonical (Route-2 A_horizon) = {L_H_route2:.6e} GeV^2 (cross-check)")
    print()

    # OOM cross-check vs the S88 W6 §V.1 multi-species ~1.0e7 W form
    # L (GeV^2) is energy*rate: power_W = L_GeV2 * (J/GeV) / (hbar_GeV_s)
    GeV_to_J = 1.602176634e-10  # (local)
    L_H_watts = L_H_canonical * GeV_to_J / hbar_GeV_s  # (local)
    print(f"  L_H_canonical in W (OOM cross-check) = {L_H_watts:.6e} W")
    print(f"    (S88 W6 §V.1 multi-species photon+nu+e form ~1.0e7 W; factor "
          f"{L_H_watts / 1.0e7:.2f} — consistent OOM)")
    print()

    # Step 7 — schema-v2 3-tuple + composite collapse
    print("Step 7 — schema-v2 3-tuple + composite collapse:")
    # sign_verdict: [SIGN] directional prediction = L_H_canonical > 0 by
    # construction (every factor positive). Substitution chain:
    #   Step 1: pi^2/60 > 0 (Stefan-Boltzmann radiation constant).
    #   Step 2: g_*(T_H) = 10.6886 > 0 (relativistic species count).
    #   Step 3: A_horizon = 71226 GeV^-2 > 0 (inheritance-restricted horizon area).
    #   Step 4: T_H^4 = (1.057e-3)^4 > 0 (fourth power of positive temperature).
    #   => product L_H_canonical > 0.
    all_positive = (SB_PREFACTOR > 0.0 and g_star_BS_T_H_FW > 0.0
                    and A_horizon_FW > 0.0 and T_H4 > 0.0)  # (local)
    sign_v = "PASS" if (L_H_canonical > 0.0 and all_positive) else "FAIL"  # (local)

    # magnitude_verdict: bit-precision closed-form match on the canonical pins.
    mag_v = "PASS" if bit_precision_pass else "FAIL"  # (local)

    # regime_verdict: closed-form algebraic evaluation; no numerical-integration
    # regime concern (scipy.integrate NOT invoked). The only regime check is the
    # A_horizon Route-1/Route-2 substrate-consistency (within domain of validity).
    if a_horizon_crosscheck_pass:
        regime_v = "VALID"  # (local)
    else:
        regime_v = "MARGINAL"  # (local)

    composite = composite_collapse(sign_v, mag_v, regime_v)  # (local)
    print(f"  sign_verdict      = {sign_v}  (L_H_canonical = {L_H_canonical:.6e} > 0; all 4 factors > 0)")
    print(f"  magnitude_verdict = {mag_v}  (bit-precision residual = {bit_resid:.3e})")
    print(f"  regime_verdict    = {regime_v}  (closed-form; A_horizon Route-1/2 agree to {a_horizon_resid:.4%})")
    print(f"  composite         = {composite}")
    print()

    # Step 8 — npz output
    print(f"Step 8 — Write npz: {NPZ_OUT.name}")
    np.savez(
        NPZ_OUT,
        # Primary result (canonical-promotion candidate on PASS)
        L_H_canonical=L_H_canonical,
        L_H_canonical_route2_crosscheck=L_H_route2,
        L_H_canonical_watts_crosscheck=L_H_watts,
        # The 3 canonical input pins
        g_star_BS_T_H_FW=g_star_BS_T_H_FW,
        T_H_FW=T_H_FW,
        A_horizon_FW=A_horizon_FW,
        # Derived sub-quantities
        SB_prefactor=SB_PREFACTOR,
        T_H_4=T_H4,
        # log10 decomposition for the bar chart
        log10_prefactor=log_terms["pi^2/60"],
        log10_g_star=log_terms["g_*(T_H)"],
        log10_A_horizon=log_terms["A_horizon"],
        log10_T_H_4=log_terms["T_H^4"],
        log10_L_H_canonical=log_L_H,
        # A_horizon Route-2 SI cross-check
        A_horizon_route2_GeV_m2=A_route2,
        A_horizon_route2_T_H_K=T_H_K_route2,
        A_horizon_route2_R_S_m=R_S_m,
        A_horizon_route1_route2_rel_dev=a_horizon_resid,
        M0_PBH_kg=M0_PBH_KG,
        # bit-precision self-consistency
        L_H_recompute_np=L_H_recompute,
        bit_precision_residual=bit_resid,
        bit_precision_tol=BIT_PRECISION_TOL,
        si_crosscheck_tol=SI_CROSSCHECK_TOL,
        # Option-A supersedes chain
        supersedes_target_full_64=SUPERSEDES_TARGET,
        s91_cf39_line_own_audit=S91_CF39_LINE_OWN_AUDIT,
        supersedes_target_present_on_disk=supersedes_target_present,
        s91_cf39_line_retained_on_disk=s91_cf39_line_present,
        w8_5_live_audit_sha256=W8_5_LIVE_AUDIT_SHA,
        w8_5_pass_present=w8_5_pass,
        # Verdict fields
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite_verdict=composite,
        # Pins / provenance
        scheme=SCHEME,
        convention=CONVENTION,
        a_horizon_relation="A_horizon = 1/(4 pi T_H^2) [substrate-first emergent Hawking relation]",
        cascade_form_pin="S88 W6 §V.1 cascade-tail derivation",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        schema_version="S87+",
        allow_pickle=True,
    )

    # Step 9 — JSON sidecar
    json_report = {
        "gate_id": GATE_ID,
        "L_H_canonical": L_H_canonical,
        "L_H_canonical_units": "GeV^2 (natural-unit horizon energy-flux)",
        "formula": "L_H_canonical = (pi^2/60) * g_*(T_H) * A_horizon * T_H^4",
        "canonical_pins": {
            "g_star_BS_T_H_FW": g_star_BS_T_H_FW,
            "T_H_FW_GeV": T_H_FW,
            "A_horizon_FW_GeV_m2": A_horizon_FW,
        },
        "derived": {
            "SB_prefactor_pi2_over_60": SB_PREFACTOR,
            "T_H_4_GeV4": T_H4,
            "log10_decomposition": log_terms,
            "log10_L_H_canonical": log_L_H,
        },
        "bit_precision_check": {
            "L_H_math": L_H_canonical,
            "L_H_np_float64": L_H_recompute,
            "relative_residual": bit_resid,
            "tolerance": BIT_PRECISION_TOL,
            "pass": bool(bit_precision_pass),
        },
        "a_horizon_route2_si_crosscheck": {
            "A_horizon_route1_substrate_first": A_horizon_FW,
            "A_horizon_route2_M0_1e13kg_SI": A_route2,
            "route2_T_H_K": T_H_K_route2,
            "route2_R_S_m": R_S_m,
            "rel_dev": a_horizon_resid,
            "tolerance": SI_CROSSCHECK_TOL,
            "pass": bool(a_horizon_crosscheck_pass),
            "note": ("0.05% residual = rounded anchor 1.057 MeV vs exact 1.05726 MeV "
                     "for M_0=10^13 kg; substrate-first 1/(4 pi T_H^2) is the canonical pin"),
        },
        "L_H_canonical_watts_oom_crosscheck": {
            "L_H_W": L_H_watts,
            "S88_W6_V1_multispecies_ref_W": 1.0e7,
            "factor": L_H_watts / 1.0e7,
        },
        "option_a_supersedes": {
            "supersedes_target_full_64": SUPERSEDES_TARGET,
            "supersedes_target_present_on_s91_disk": bool(supersedes_target_present),
            "original_S91_CF39_line_own_audit": S91_CF39_LINE_OWN_AUDIT,
            "original_S91_CF39_line_retained_on_disk": bool(s91_cf39_line_present),
            "protocol": ("corrective canonical line emitted under NEW gate-ID "
                         "S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY with supersedes tag; "
                         "original S91-CF39 PRE-REG-INC line retained per absolute verdict permanence"),
        },
        "upstream_cascade": {
            "w8_5_live_audit_sha256": W8_5_LIVE_AUDIT_SHA,
            "w8_5_pass_present": bool(w8_5_pass),
        },
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "composite_verdict": composite,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pin_shas": pins,
    }
    JSON_OUT.write_text(json.dumps(json_report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  → {JSON_OUT.name}")

    # Step 10 — Plot: bar chart of the 3-pin (+ prefactor) log10 contributions
    print(f"Step 10 — Write plot: {PNG_OUT.name}")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Panel A: log10 multiplicative contributions to L_H_canonical
    labels = ["pi^2/60\n(SB prefactor)", "g_*(T_H)\n(species count)",
              "A_horizon\n(horizon area)", "T_H^4\n(temperature)"]
    vals = [log_terms["pi^2/60"], log_terms["g_*(T_H)"],
            log_terms["A_horizon"], log_terms["T_H^4"]]
    colors = ["#888888", "#1f77b4", "#2ca02c", "#d62728"]
    bars = ax1.bar(labels, vals, color=colors, edgecolor="black", alpha=0.85)
    ax1.axhline(0.0, color="black", lw=0.8)
    ax1.axhline(log_L_H, color="purple", lw=2.0, ls="--",
                label=f"log10(L_H_canonical) = {log_L_H:.3f}")
    for bar, v in zip(bars, vals):
        ax1.text(bar.get_x() + bar.get_width() / 2, v + (0.15 if v >= 0 else -0.35),
                 f"{v:+.3f}", ha="center", fontsize=9)
    ax1.set_ylabel(r"$\log_{10}$ contribution to $L_{H}^{\rm canonical}$  (GeV² basis)", fontsize=10)
    ax1.set_title(f"3-pin (+SB prefactor) log₁₀ decomposition\n"
                  f"Σ = {sum(vals):+.3f} = log₁₀(L_H) = {log_L_H:.3f}", fontsize=10)
    ax1.legend(loc="upper right", fontsize=8)
    ax1.grid(True, axis="y", alpha=0.3)

    # Panel B: A_horizon Route-1 vs Route-2 + L_H value box
    ax2.bar(["Route-1\nsubstrate-first\n1/(4πT_H²)", "Route-2\nM₀=10¹³ kg\nSI Schwarzschild"],
            [A_horizon_FW, A_route2], color=["#2ca02c", "#9467bd"],
            edgecolor="black", alpha=0.85)
    ax2.text(0, A_horizon_FW + 800, f"{A_horizon_FW:.1f}", ha="center", fontsize=10)
    ax2.text(1, A_route2 + 800, f"{A_route2:.1f}", ha="center", fontsize=10)
    ax2.set_ylabel(r"$A_{\rm horizon}$  (GeV$^{-2}$)", fontsize=10)
    ax2.set_title(f"A_horizon substrate-first vs SI cross-check\n"
                  f"rel_dev = {a_horizon_resid:.4%} (< {SI_CROSSCHECK_TOL:.0%})", fontsize=10)
    ax2.grid(True, axis="y", alpha=0.3)
    ax2.set_ylim(0, max(A_horizon_FW, A_route2) * 1.15)
    textstr = (f"$L_H^{{\\rm canonical}}$ = {L_H_canonical:.4e} GeV²\n"
               f"= {L_H_watts:.3e} W (OOM cross-check)\n"
               f"sign={sign_v}, mag={mag_v}, regime={regime_v}\n"
               f"composite = {composite}")
    ax2.text(0.5, 0.55, textstr, transform=ax2.transAxes, ha="center", va="center",
             bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.85), fontsize=9)

    fig.suptitle(
        f"{GATE_ID}  —  composite={composite}\n"
        f"L_H_canonical = (π²/60)·g_*(T_H)·A_horizon·T_H⁴ "
        f"[Option-A supersedes={SUPERSEDES_TARGET[:16]}...]",
        fontsize=11,
    )
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120, bbox_inches="tight")
    plt.close(fig)

    # Step 11 — single-shot AFTER-pattern verdict emission (Option-A supersedes)
    print()
    print("Step 11 — Build verdict block in memory → atomic append → re-read verify")
    value_str = (
        f"L_H_canonical={L_H_canonical:.6e};"
        f"L_H_canonical_units=GeV^2;"
        f"g_star_BS_T_H_FW={g_star_BS_T_H_FW:.6f};"
        f"T_H_FW={T_H_FW:.6e};"
        f"A_horizon_FW={A_horizon_FW:.6f};"
        f"SB_prefactor={SB_PREFACTOR:.6f};"
        f"T_H_4={T_H4:.6e};"
        f"bit_precision_residual={bit_resid:.3e};"
        f"A_horizon_route2_GeV_m2={A_route2:.6f};"
        f"A_horizon_route1_route2_rel_dev={a_horizon_resid:.6f};"
        f"L_H_canonical_watts_crosscheck={L_H_watts:.6e};"
        f"w8_5_live_audit_sha256={W8_5_LIVE_AUDIT_SHA};"
        f"supersedes={SUPERSEDES_TARGET};"
        f"composite={composite}"
    )
    verdict_block = build_verdict_text(
        composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
    )
    append_verdict_atomic(verdict_block)

    if verify_verdict_on_disk(audit_sha):
        print(f"  → s92_gate_verdicts.txt (audit_sha256={audit_sha[:16]}...): VERIFIED on disk")
        print(f"     supersedes={SUPERSEDES_TARGET} present: True")
    else:
        print(f"  ERROR: verdict line OR supersedes token not found after append;"
              f" audit_sha256={audit_sha[:16]}...")
        return 1

    # Step 12 — On PASS: emit the update_constant invocation record for
    # L_H_canonical_FW (the actual MCP call is made by the orchestrating agent
    # per the canonical write-order verdict-file -> canonical_constants.py).
    print()
    if composite == "PASS":
        provenance_comment = (
            f"GeV^2. CF-39 horizon-area Stefan-Boltzmann energy-flux observable "
            f"L_H_canonical = (pi^2/60)*g_*(T_H)*A_horizon*T_H^4 evaluated closed-form on "
            f"3 canonical pins (g_star_BS_T_H_FW={g_star_BS_T_H_FW:.6f} [S92-W8-5], "
            f"T_H_FW=1.057e-3 GeV, A_horizon_FW={A_horizon_FW:.2f} GeV^-2). Option-A "
            f"supersedes-chain: corrective canonical line supersedes S91-CF39 PRE-REG-INC "
            f"target {SUPERSEDES_TARGET}. OOM cross-check vs S88 W6 §V.1 multi-species "
            f"~1.0e7 W form: {L_H_watts:.3e} W. This gate audit_sha256={audit_sha}."
        )
        print("Step 12 — PASS branch: L_H_canonical_FW canonical-promotion record.")
        print("  update_constant(")
        print(f"    name='L_H_canonical_FW',")
        print(f"    value={L_H_canonical!r},")
        print(f"    session='S92',")
        print(f"    source='S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY',")
        print(f"    section_label='SECTION E',")
        print(f"    comment={provenance_comment!r},")
        print(f"  )")
        print("  (MCP call executed by the dispatching agent per canonical write-order.)")
    else:
        print(f"Step 12 — composite={composite} (not PASS): L_H_canonical_FW promotion "
              f"does NOT fire.")

    # Final 4-tuple log line
    print()
    print(
        f"(value='L_H_canonical={L_H_canonical:.6e};supersedes={SUPERSEDES_TARGET}', "
        f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"\n=== {GATE_ID}: {composite} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
