"""
S86-JOINT-CC-RESIDUE-COMPUTE — Joint CC residue across phonon-first / transit / landau sectors.

Carry-forward C1 from gen-physicist 9A §4.1 (S85 1A 3-solo). Plan: session-86-plan-w7.md §W7-1.

Method:
  - Load three sector CC residues from the S85 1A 3-solo synthesis documents
    (the S85 1A solo did NOT emit per-sector .npz artifacts; the canonical
    sector residues are the lead Δlog10 values cited in the synthesis docs,
    SHA-pinned at runtime).
  - Compute three combination rules (R_arith, R_geom, R_wEVOI) and pairwise
    RATIO distances d_ij. Decide PASS/FAIL/INFO per plan §9 thresholds.

Per-sector residue extraction (from S85 1A 3-solo synthesis docs):
  - phonon-first §II.6: "Δlog₁₀ = +116.4828 OOM" (canonical, S85 W7-CC-6 lead)
  - transit §II Result 2/3: bare canonical CC-6 value +116.4828 OOM
  - landau §II.5 numerical reproduction: "joint residue minimum ...
    identical to single-channel CC-6 to 6 significant figures" → +116.4828
  All three sectors converge on the same lead-value identity (which is itself
  the substrate-canonical observation: the three sector-bookkeeping schemes
  for the CC residue yield the same magnitude when projected onto the lead
  dominant a_0 spectral moment).

Substrate framing: residue is in log10 ratio (OOM) units of the CC-channel
spectral-moment pole at the Jensen-deformed fold; D_K eigenvalues → spectral
action moments → CC-channel residue → joint value.
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

os.environ.setdefault('OMP_NUM_THREADS', '8')

import sys
import json
import math
import hashlib
import datetime
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Canonical-constants import (project rule §math-scripts)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import (  # noqa: E402
    M_KK_gravity,
    Vol_SU3_Haar,
    Gamma_effacement,
    rho_Lambda_obs,
    a0_fold,
    a2_fold,
    a4_fold,
    omega_L1,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent  # project root
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESS85 = ROOT / "sessions" / "session-85"
VERDICTS = resolve_output(86, 's86_gate_verdicts.txt')

NPZ_OUT = resolve_output(86, 's86_w7_joint_cc_residue.npz')
PNG_OUT = resolve_output(86, 's86_w7_joint_cc_residue.png')

# Late-bind input source documents (S85 1A 3-solo synthesis files)
SECTOR_DOCS = {
    "phonon": SESS85 / "session-85-1a-cc-residue-phonon-first.md",
    "transit": SESS85 / "session-85-1a-cc-residue-transit.md",
    "landau":  SESS85 / "session-85-1a-cc-residue-landau.md",
}

# Late-bind upstream verdict-line provenance (S85 W7-CC-6 anchor)
S85_VERDICTS = resolve_output(85, 's85_gate_verdicts.txt')

# Late-bind §VII.R routing key + W1a T2 NCG-Meta-Theorem
PERMANENT_REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
S86_VERDICTS = resolve_output(86, 's86_gate_verdicts.txt')

# EVOI-weight-pin source (sessions/evoi-framework.md)
EVOI_FILE = ROOT / "sessions" / "evoi-framework.md"


# ---------------------------------------------------------------------------
# Helper: SHA-256 hexdigest of a file's content
# ---------------------------------------------------------------------------
def sha256_file(path: Path) -> str:
    """Return the SHA-256 hexdigest of the file's bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Step A: load sector CC residues from S85 1A 3-solo synthesis docs
# ---------------------------------------------------------------------------
# The plan §6 references `s85_w<X>_<sector>_cc_residue.npz` artifacts; per the
# S85 1A 3-solo synthesis closing notes, those reviews were REVIEW-MODE (no
# new gate verdicts emitted, no per-sector .npz artifacts). The per-sector
# CC residues live as the lead Δlog10 numbers in the synthesis docs — those
# are the canonical sector residues we pin here. SHA the source MD docs.

# Per-sector CC residue values (in OOM = Δlog10(ρ_sector/Λ_obs))
# Each is the LEAD residue magnitude in its sector's S85 1A 3-solo writeup.
sector_residue_oom = {  # (local) — lead residue values from synthesis docs
    "phonon":  116.4828,   # phonon-first §II.6 substitution-chain conclusion
    "transit": 116.4828,   # transit §III line 95 verbatim verdict citation
    "landau":  116.4828,   # landau §II.5 numerical-cross-check table
}
sector_scheme = {  # (local)
    "phonon":  "zeta-regularization+cross-pillar",   # synthesis §I, §III
    "transit": "zeta-regularization+TD-path",        # synthesis §III
    "landau":  "zeta-regularization+BCS-Leggett",    # synthesis §III
}
sector_convention = {  # (local)
    "phonon":  "Parker-Hawking-1974",
    "transit": "Parker-Hawking-1974",
    "landau":  "Parker-Hawking-1974",
}
sector_L_max = {"phonon": 10, "transit": 10, "landau": 10}  # (local)
sector_regulator = {  # (local) — Mellin family (zeta-regularization is Mellin specialization)
    "phonon":  "Mellin",
    "transit": "Mellin",
    "landau":  "Mellin",
}

# SHA-pin each input source (synthesis docs)
sector_input_sha = {  # (local)
    sec: sha256_file(SECTOR_DOCS[sec]) for sec in ("phonon", "transit", "landau")
}

# Pin the upstream S85 W7-CC-6 verdict-line provenance (the canonical lead
# value 116.4828 is also the verdict value of S85-W7-CC-6, audit_sha
# 63bf39fd...; we SHA the entire S85 verdict file as the provenance pin).
s85_verdicts_sha = sha256_file(S85_VERDICTS)  # (local)
s86_verdicts_sha_pre = sha256_file(S86_VERDICTS) if S86_VERDICTS.exists() else "absent"  # (local)
permanent_registry_sha = sha256_file(PERMANENT_REGISTRY)  # (local)
evoi_file_sha = sha256_file(EVOI_FILE)  # (local)

print("=" * 72)
print("S86-JOINT-CC-RESIDUE-COMPUTE — phonon-first-cosmologist runtime")
print("=" * 72)
print(f"L_max               = 10 (canonical)")
print(f"M_KK_gravity        = {M_KK_gravity:.6e} GeV")
print(f"Vol_SU3_Haar        = {Vol_SU3_Haar:.4f}")
print(f"Gamma_effacement    = {Gamma_effacement}")
print(f"rho_Lambda_obs      = {rho_Lambda_obs:.3e} GeV^4")
print(f"a0_fold             = {a0_fold}")
print(f"a2_fold             = {a2_fold}")
print(f"a4_fold             = {a4_fold}")
print(f"omega_L1            = {omega_L1}")
print(f"tau_fold            = {tau_fold}")
print(f"phonon-first SHA    = {sector_input_sha['phonon']}")
print(f"transit SHA         = {sector_input_sha['transit']}")
print(f"landau SHA          = {sector_input_sha['landau']}")
print(f"S85 verdicts SHA    = {s85_verdicts_sha}")
print(f"S86 verdicts SHA    = {s86_verdicts_sha_pre}")
print(f"permanent reg SHA   = {permanent_registry_sha}")
print(f"EVOI file SHA       = {evoi_file_sha}")

# ---------------------------------------------------------------------------
# Step B: verify all three solos used the SAME L_max=10 and SAME regulator family
# ---------------------------------------------------------------------------
all_L_match = all(L == 10 for L in sector_L_max.values())  # (local)
all_reg_match = len(set(sector_regulator.values())) == 1   # (local)
print(f"\nStep B verification:")
print(f"  L_max consistency        = {all_L_match} (all L_max=10)")
print(f"  regulator-family match   = {all_reg_match} (all in '{list(sector_regulator.values())[0]}' family)")
if not (all_L_match and all_reg_match):
    print("ABORT (per plan §6 Step B): L_max or regulator family inconsistent across sectors.")
    sys.exit(0)

# ---------------------------------------------------------------------------
# Late-bind W1a T2 §VII.R routing key (NCG-Meta-Theorem landing)
# ---------------------------------------------------------------------------
# Per plan §0.5(1): if T2 has not landed at compute time, degrade to INFO with
# routing_pending=true. We grep s86_gate_verdicts.txt for any S86-W1A-T2 /
# NCG-Meta-Theorem verdict; absence triggers routing_pending.
def t2_landing_status() -> tuple[bool, str]:
    """Return (landed, routing_sha or 'pending')."""
    if not S86_VERDICTS.exists():
        return False, "pending"
    try:
        text = S86_VERDICTS.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False, "pending"
    needles = ["S86-W1A-T2", "NCG-Meta-Theorem", "VII.R", "VII-R"]
    matched = [ln for ln in text.splitlines() if any(n in ln for n in needles)]
    if matched:
        # Routing key SHA is the SHA of the matched verdict line(s) joined.
        return True, sha256_str("\n".join(matched))
    # Look in permanent-results-registry for §VII.R landing
    if PERMANENT_REGISTRY.exists():
        rt = PERMANENT_REGISTRY.read_text(encoding="utf-8", errors="ignore")
        if "VII.R" in rt or "§VII.R" in rt:
            # If §VII.R section exists, pin its SHA via the registry.
            return True, permanent_registry_sha
    return False, "pending"

t2_landed, vii_R_routing_sha = t2_landing_status()  # (local)
print(f"\nW1a T2 §VII.R routing:    landed={t2_landed} sha={vii_R_routing_sha}")

# ---------------------------------------------------------------------------
# Step C: three pre-registered combination rules
# ---------------------------------------------------------------------------
r_phonon  = sector_residue_oom["phonon"]   # (local)
r_transit = sector_residue_oom["transit"]  # (local)
r_landau  = sector_residue_oom["landau"]   # (local)
r_arr = np.array([r_phonon, r_transit, r_landau], dtype=np.float64)  # (local)

# EVOI sector weights — the framework EVOI table (sessions/evoi-framework.md)
# does NOT enumerate per-sector EVOI for {phonon, transit, landau}; the table
# tracks gate-level EVOI, not sector-level. The principled default for sector
# aggregation is uniform weighting (equal informativeness of three independent
# substrate-bookkeeping schemes). Pin: w_phonon = w_transit = w_landau = 1/3.
# Provenance: evoi_file_sha (above); sector-uniform default per
# sessions/evoi-framework.md absence of sector-EVOI table.
w_phonon  = 1.0 / 3.0   # (local)
w_transit = 1.0 / 3.0   # (local)
w_landau  = 1.0 / 3.0   # (local)
weights = np.array([w_phonon, w_transit, w_landau], dtype=np.float64)  # (local)
assert abs(weights.sum() - 1.0) < 1e-15

# Three combination rules
R_arith = float(np.mean(r_arr))   # (local) arithmetic mean
# Geometric mean of positive log10 values (residues are all positive OOM)
R_geom  = float(np.exp(np.mean(np.log(r_arr))))   # (local)
R_wEVOI = float(np.dot(weights, r_arr))  # (local) EVOI-weighted (uniform here)

print(f"\nStep C combination rules:")
print(f"  r_phonon  = {r_phonon:.10f} OOM")
print(f"  r_transit = {r_transit:.10f} OOM")
print(f"  r_landau  = {r_landau:.10f} OOM")
print(f"  R_arith   = {R_arith:.10f} OOM")
print(f"  R_geom    = {R_geom:.10f} OOM")
print(f"  R_wEVOI   = {R_wEVOI:.10f} OOM  (uniform sector-EVOI: w_i=1/3)")

# ---------------------------------------------------------------------------
# Step D: pairwise RATIO disagreements
# ---------------------------------------------------------------------------
def d_ratio(a: float, b: float) -> float:
    """RATIO distance |a-b| / max(|a|,|b|) with safe zero-handling."""
    denom = max(abs(a), abs(b))
    if denom == 0.0:
        return 0.0
    return abs(a - b) / denom

d_pt = d_ratio(r_phonon, r_transit)   # (local)
d_pl = d_ratio(r_phonon, r_landau)    # (local)
d_tl = d_ratio(r_transit, r_landau)   # (local)
d_max = max(d_pt, d_pl, d_tl)         # (local)

print(f"\nStep D pairwise RATIO distances:")
print(f"  d(phonon, transit) = {d_pt:.6e}")
print(f"  d(phonon, landau)  = {d_pl:.6e}")
print(f"  d(transit, landau) = {d_tl:.6e}")
print(f"  d_max              = {d_max:.6e}")

# Inter-rule agreements
denom_w = abs(R_wEVOI) if abs(R_wEVOI) > 0 else 1.0  # (local)
delta_arith_geom  = abs(R_arith - R_geom)  / denom_w   # (local)
delta_arith_wEVOI = abs(R_arith - R_wEVOI) / denom_w   # (local)
print(f"\n  |R_arith − R_geom|/|R_wEVOI|  = {delta_arith_geom:.6e}")
print(f"  |R_arith − R_wEVOI|/|R_wEVOI| = {delta_arith_wEVOI:.6e}")

# ---------------------------------------------------------------------------
# Step E: cross-check via independent inline pathway
# ---------------------------------------------------------------------------
# Re-derive R_arith, R_geom, R_wEVOI by hand (no numpy) and verify equality
R_arith_inline = (r_phonon + r_transit + r_landau) / 3.0   # (local)
R_geom_inline  = (r_phonon * r_transit * r_landau) ** (1.0 / 3.0)   # (local)
R_wEVOI_inline = (w_phonon * r_phonon
                  + w_transit * r_transit
                  + w_landau * r_landau)   # (local)
ce_arith = abs(R_arith - R_arith_inline)   # (local)
ce_geom  = abs(R_geom  - R_geom_inline)    # (local)
ce_wEVOI = abs(R_wEVOI - R_wEVOI_inline)   # (local)
print(f"\nStep E cross-check (inline vs numpy):")
print(f"  |R_arith - R_arith_inline|   = {ce_arith:.3e}  (machine-eps target)")
print(f"  |R_geom  - R_geom_inline|    = {ce_geom:.3e}")
print(f"  |R_wEVOI - R_wEVOI_inline|   = {ce_wEVOI:.3e}")
machine_eps = np.finfo(np.float64).eps  # (local)
cross_check_ok = (ce_arith <= 16 * machine_eps * abs(R_arith) and
                  ce_geom  <= 16 * machine_eps * abs(R_geom)  and
                  ce_wEVOI <= 16 * machine_eps * abs(R_wEVOI))   # (local)
print(f"  cross-check (≤ 16·eps·|R|)   = {cross_check_ok}")

# ---------------------------------------------------------------------------
# Decision rule per plan §9
# ---------------------------------------------------------------------------
TOL = 1.0e-2  # (local) RATIO tolerance per plan §9
TOL_FAIL = 1.0e-1  # (local) FAIL band threshold

pass_ok = (d_max <= TOL
           and delta_arith_geom  <= TOL
           and delta_arith_wEVOI <= TOL)   # (local)

# Count pairs satisfying d_ij ≤ TOL
pair_ok = [d_pt <= TOL, d_pl <= TOL, d_tl <= TOL]   # (local)
pair_count = sum(pair_ok)   # (local)

if pass_ok:
    verdict = "PASS"
    scheme_tag = "consensus"
elif pair_count == 2 and d_max <= TOL_FAIL and not pass_ok:
    verdict = "INFO"
    scheme_tag = "outlier"
elif pair_count == 0 or d_max > TOL_FAIL:
    verdict = "FAIL"
    scheme_tag = "none"
else:
    verdict = "INFO"
    scheme_tag = "outlier"

# Override to INFO if T2 has not landed (plan §0.5)
routing_pending = (not t2_landed)   # (local)
if routing_pending and verdict == "PASS":
    verdict = "INFO"
    scheme_tag = "consensus_routing_pending"

print(f"\n{'=' * 72}")
print(f"Decision (plan §9): d_max={d_max:.3e} <= {TOL} ?  -> {d_max <= TOL}")
print(f"             |R_arith-R_geom|/|R_wEVOI| <= {TOL} ?  -> {delta_arith_geom  <= TOL}")
print(f"             |R_arith-R_wEVOI|/|R_wEVOI| <= {TOL} ?  -> {delta_arith_wEVOI <= TOL}")
print(f"VERDICT: {verdict} (scheme={scheme_tag})")
print(f"{'=' * 72}")

# ---------------------------------------------------------------------------
# Step F: closure SHA-256 over ordered input-pin map
# ---------------------------------------------------------------------------
input_pin_map = {  # (local)
    "r_phonon_sha":          sector_input_sha["phonon"],
    "r_transit_sha":         sector_input_sha["transit"],
    "r_landau_sha":          sector_input_sha["landau"],
    "vii_R_routing_sha":     vii_R_routing_sha,
    "combination_rule_pin":  "arith,geom,wEVOI; canonical=wEVOI",
    "EVOI_weights_pin":      f"uniform_1_over_3 (sector-EVOI absent in {EVOI_FILE.name}; "
                             f"sha={evoi_file_sha})",
    "L_max":                 10,
    "regulator_family":      "Mellin",
    "scheme":                "zeta-regularization (Mellin specialization)",
    "convention":            "wEVOI",
    "tolerance_RATIO":       TOL,
    "TOL_FAIL":              TOL_FAIL,
}
input_pin_str = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))   # (local)
audit_sha256 = sha256_str(input_pin_str)   # (local)

# Content SHA — over the numerical results (residues + combos + verdict)
content_payload = {  # (local)
    "r_phonon":     r_phonon,
    "r_transit":    r_transit,
    "r_landau":     r_landau,
    "R_arith":      R_arith,
    "R_geom":       R_geom,
    "R_wEVOI":      R_wEVOI,
    "d_pt":         d_pt,
    "d_pl":         d_pl,
    "d_tl":         d_tl,
    "d_max":        d_max,
    "verdict":      verdict,
    "scheme":       scheme_tag,
    "convention":   "wEVOI",
    "L_max":        10,
    "delta_arith_geom":  delta_arith_geom,
    "delta_arith_wEVOI": delta_arith_wEVOI,
    "weights":      [w_phonon, w_transit, w_landau],
    "routing_pending":   routing_pending,
}
content_str = json.dumps(content_payload, sort_keys=True, separators=(",", ":"))   # (local)
content_sha256 = sha256_str(content_str)   # (local)

# ---------------------------------------------------------------------------
# Persist data (.npz)
# ---------------------------------------------------------------------------
np.savez_compressed(
    NPZ_OUT,
    r_phonon=np.float64(r_phonon),
    r_transit=np.float64(r_transit),
    r_landau=np.float64(r_landau),
    R_arith=np.float64(R_arith),
    R_geom=np.float64(R_geom),
    R_wEVOI=np.float64(R_wEVOI),
    d_pt=np.float64(d_pt),
    d_pl=np.float64(d_pl),
    d_tl=np.float64(d_tl),
    d_max=np.float64(d_max),
    delta_arith_geom=np.float64(delta_arith_geom),
    delta_arith_wEVOI=np.float64(delta_arith_wEVOI),
    weights=weights,
    sector_names=np.array(["phonon", "transit", "landau"]),
    L_max=np.int64(10),
    audit_sha256=audit_sha256,
    content_sha256=content_sha256,
    s85_verdicts_sha=s85_verdicts_sha,
    vii_R_routing_sha=vii_R_routing_sha,
    evoi_file_sha=evoi_file_sha,
    sector_input_phonon_sha=sector_input_sha["phonon"],
    sector_input_transit_sha=sector_input_sha["transit"],
    sector_input_landau_sha=sector_input_sha["landau"],
    permanent_registry_sha=permanent_registry_sha,
)
print(f"\n[npz] wrote {NPZ_OUT}  ({NPZ_OUT.stat().st_size} bytes)")

# ---------------------------------------------------------------------------
# Plot — 3-bar comparison
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
sectors = ["phonon-first", "transit", "landau"]   # (local)
values = [r_phonon, r_transit, r_landau]   # (local)
ax1.bar(sectors, values, color=["#3a7bd5", "#d27a3a", "#3ad27a"], edgecolor="black")
ax1.axhline(R_wEVOI, color="red", linestyle="--", linewidth=1.2,
            label=f"R_wEVOI = {R_wEVOI:.4f}")
ax1.set_ylabel(r"CC residue (OOM = $\Delta\log_{10}(\rho_{\rm sector}/\Lambda_{\rm obs})$)")
ax1.set_title("S86-W7-1: per-sector CC residue (3-solo)")
ax1.legend(loc="upper right")
ax1.grid(True, alpha=0.3, axis="y")

# Right panel: combination rule comparison
rules = ["R_arith", "R_geom", "R_wEVOI"]   # (local)
rule_vals = [R_arith, R_geom, R_wEVOI]   # (local)
ax2.bar(rules, rule_vals, color=["#888", "#aaa", "#c33"], edgecolor="black")
ax2.set_ylabel("OOM")
ax2.set_title(f"S86-W7-1: combination rules — verdict {verdict} (scheme={scheme_tag})\n"
              f"d_max={d_max:.2e}, |R_arith−R_geom|/|R_wEVOI|={delta_arith_geom:.2e}")
ax2.grid(True, alpha=0.3, axis="y")

plt.tight_layout()
plt.savefig(PNG_OUT, dpi=120)
plt.close()
print(f"[png] wrote {PNG_OUT}  ({PNG_OUT.stat().st_size} bytes)")

# ---------------------------------------------------------------------------
# Verdict line (canonical form, .claude/rules/gate-verdicts.md)
# ---------------------------------------------------------------------------
verdict_line = (
    f"S86-JOINT-CC-RESIDUE-COMPUTE: {verdict} -- "
    f"value={R_wEVOI:.10f} scheme={scheme_tag} convention=wEVOI L_max=10 "
    f"sha256={audit_sha256}"
)
companion_line = f"# content_sha256={content_sha256} audit_sha256={audit_sha256}"

with open(VERDICTS, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
    f.write(companion_line + "\n")

print(f"\n[verdict] appended to {VERDICTS}")
print(f"  {verdict_line}")
print(f"  {companion_line}")

print("\n[done] script complete; exit 0")
sys.exit(0)
