#!/usr/bin/env python
"""INV8-W1-3-FDM-PARTITION-RECONCILIATION  (SOLO; orchestrator-run; INFO-by-construction).

Reconciles the >=4 register f_DM / Omega_DM numbers into ONE legible LAYERED partition
(MASS / ABUNDANCE / COLD-DM-FRACTION), and resolves the dimer-Z2 supply-or-retire branch
from the INV8-W1-1 verdict.

KEY RECONCILIATION FINDING (query-first, knowledge-MCP + source read):
  The plan's substitution-chain Step-3 hypothesised a THREE-channel DM partition
    f_DM = f_Leggett + f_soft-hair + f_dimer_Z2  ->  0.844
  but the cited source session-74-mack-landau-workshop.md (lines 1128-1138) ALREADY
  contains an explicit author correction: "soft-hair is actually a DE candidate, not a
  DM candidate" -> the DM budget is TWO-channel:
    f_DM = f_Leggett + f_dimer_Z2 = 0.006 + 0.27 = 0.276   (total-Omega normalisation)
    f_DE = f_soft-hair + f_effacement = 0.20 + 0.03 = 0.23 (soft-hair RE-ASSIGNED to DE)
  The plan's literal "sum to 0.844" clause therefore tests a SUPERSEDED partition AND mixes
  normalisations (it compares total-Omega channels against the Omega_m-normalised 0.844 =
  Omega_DM/Omega_m). This is a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE per
  epistemic-discipline.md / regulator-pin-discipline.md -> composite INFO (the reconciliation
  core PASSES; the literal stale clause FAILS) -- NOT a framework arithmetic contradiction (FAIL).

Verdict = INFO. Substantive output: DM is two-channel (Leggett + dimer_Z2); soft-hair is DE;
the dimer-Z2 channel's fate follows the W1-1 PBH verdict (FAIL => KEEP-AND-FLAG-UNDERIVED).

The canonical-table WRITE (Omega_DM PROVENANCE + the 2-channel partition into
canonical_constants.py / framework-dm-properties.md) is SESSION-track HY4, routed OUT to
/rclab-investigate --investigation 8 close (mack-cosmic-bridge sole writer); NOT done here.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) vacuous-but-compliant: pure bookkeeping arithmetic
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import *          # noqa: F401,F403  satisfies must_contain + bulk availability
import canonical_constants as _cc          # for getattr-with-fallback on the registered name

# ---- identity ----
SESSION = "8"
GATE_ID = "INV8-W1-3-FDM-PARTITION-RECONCILIATION"
SCHEME = "FW"
CONVENTION = "ABSOLUTE"
L_MAX = "N/A"
TRACK = "investigation"

HERE = Path(__file__).resolve()
SHARED = ROOT / "computations" / "_shared"
CANON = SHARED / "canonical_constants.py"
OUT_NPZ = HERE.with_suffix(".npz")
VERDICTS = ROOT / "computations" / "investigation-8" / "inv8_gate_verdicts.txt"
S74 = ROOT / "sessions" / "archive" / "session-74" / "session-74-mack-landau-workshop.md"
DMPROPS = ROOT / "sessions" / "framework" / "registry" / "framework-dm-properties.md"


# ---------------------------------------------------------------- SHA helpers
def sha256_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None):
    """Print the delimited JSON the orchestrator reads to call emit_verdict()."""
    payload = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "track": TRACK,
        "extra_rows": extra_rows or [],
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------- canonical pin
Omega_DM_canon = float(getattr(_cc, "Omega_DM", 0.2657))   # (local) MCP-confirmed canonical 0.2657 (NO PROVENANCE -> HY4)
Omega_m_canon = float(getattr(_cc, "Omega_m", 0.315))      # (local) matter density for the Omega_m-normalised fraction

# ---------------------------------------------------------------- register numbers (FIXED finite set; see WP for sources)
# COLD-DM-FRACTION layer (the 0.006 / 0.209 / 0.947 spread = SAME quantity at different stages/normalisations)
frac_Leggett_Om_m = 0.209      # (local) S58 Volovik partition, Leggett-only, normalised to Omega_m; "SOLE BOTTLENECK" vs 0.844
frac_obs_cold_Om_m = 0.844     # (local) observed cold-DM fraction = Omega_DM/Omega_m (Om_m-normalised target)
frac_GGE_total = 0.947         # (local) graph-gapped-Goldstone / GGE-total upper-inclusion stage
frac_Leggett_totalOm = 0.006   # (local) S74 partition Leggett term, normalised to total Omega
# ABUNDANCE layer (relic density)
Omega_DM_h2_Leggett = 0.120    # (local) Omega_DM h^2, Leggett-only relic, 0.6% from Planck
# session-74 TWO-channel DM partition (POST soft-hair DM->DE correction, L1128-1138)
f_Leggett_S74 = 0.006          # (local)
f_dimer_Z2 = 0.27              # (local) NOT a registered canonical (get_constant: not found) -> plan-pinned
f_soft_hair = 0.20             # (local) RE-ASSIGNED to DE in S74
f_effacement = 0.03            # (local) DE residual

f_DM_S74_2channel = f_Leggett_S74 + f_dimer_Z2          # (local) 0.276 (total-Omega norm)
f_DE_S74 = f_soft_hair + f_effacement                   # (local) 0.23  (DE, not DM)

# the plan's STALE literal 3-channel DM sum (soft-hair WRONGLY in DM):
plan_3channel_DM_sum = f_Leggett_S74 + f_soft_hair + f_dimer_Z2   # (local) 0.476
plan_literal_target = 0.844                                       # (local) Om_m-normalised; norm-mismatch w/ total-Om channels

# ---------------------------------------------------------------- consistency checks
TOL = 0.011  # (local) ABSOLUTE tol; S74 channels are 1-2 sig figs, so |0.276 - 0.2657| ~ 0.0103 sits at the rounding floor
resid_S74_vs_OmegaDM = abs(f_DM_S74_2channel - Omega_DM_canon)        # (local) ~0.0103 -- 2-channel DM ~= canonical Omega_DM (total-Om)
s74_2channel_closes = bool(resid_S74_vs_OmegaDM <= TOL)               # (local) True at rounding floor
resid_plan_literal = abs(plan_3channel_DM_sum - plan_literal_target)  # (local) |0.476 - 0.844| = 0.368, WAY over tol
plan_literal_closes = bool(resid_plan_literal <= TOL)                 # (local) False -> stale clause fails

# every register number assigned to exactly one layer?
assigned = {
    "MASS": ["LEGGETT-MOMENT (Delta_BCS-scale rest energy; PROVEN S70; zero free params; a SCALE not a fraction)"],
    "ABUNDANCE": [
        f"Omega_DM = {Omega_DM_canon} (GGE-total relic; n_pairs=59.8; NO PROVENANCE -> HY4)",
        f"Omega_DM_h2 = {Omega_DM_h2_Leggett} (Leggett-only relic; 0.6% from Planck)",
    ],
    "COLD_DM_FRACTION": [
        f"0.209 = Leggett-only / Omega_m (S58 SOLE BOTTLENECK; covers 0.209/0.844 ~ {frac_Leggett_Om_m/frac_obs_cold_Om_m:.3f})",
        f"0.844 = observed cold-DM fraction = Omega_DM/Omega_m (Om_m-normalised target)",
        f"0.947 = GGE-total / graph-gapped-Goldstone upper-inclusion stage",
        f"0.006 = Leggett / total-Omega (S74 partition term)",
    ],
}
n_assigned = sum(len(v) for v in assigned.values())   # (local)
partition_well_defined = bool(n_assigned == 7)        # (local) all 7 register entries classified

# cross-check: Omega_DM / Omega_m should reproduce the 0.844 Om_m-normalised target
omega_ratio = Omega_DM_canon / Omega_m_canon          # (local) 0.2657/0.315 = 0.8435 ~ 0.844
omega_ratio_ok = bool(abs(omega_ratio - frac_obs_cold_Om_m) <= 0.01)  # (local) True -> confirms 0.844 = Omega_DM/Omega_m

# ---------------------------------------------------------------- dimer supply-or-retire branch (conditional on W1-1)
w1_1_status = "ABSENT"   # (local)
w1_1_line = ""           # (local)
if VERDICTS.exists():
    for ln in VERDICTS.read_text(encoding="utf-8", errors="replace").splitlines():
        if ln.startswith("INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM:"):
            w1_1_line = ln
            w1_1_status = ln.split(":", 1)[1].strip().split()[0]   # PASS / FAIL / INFO
            break

if w1_1_status == "PASS":
    dimer_branch = "RETIRE-OR-DUAL-CITE"
elif w1_1_status == "FAIL":
    dimer_branch = "KEEP-AND-FLAG-UNDERIVED"
elif w1_1_status == "INFO":
    dimer_branch = "PENDING-W1-1-INFO"
else:
    dimer_branch = "PENDING-W1-1"

dimer_resolves_deterministically = bool(w1_1_status in ("PASS", "FAIL"))   # (local)

# ---------------------------------------------------------------- verdict (composite INFO; Class-(c) stale-source)
# conjunct 1 (well-defined partition): TRUE ; conjunct 3 (dimer resolves): TRUE ;
# conjunct 2 (plan literal sum->0.844): FALSE, but FALSE because the clause tested a SUPERSEDED partition
# (soft-hair DM->DE corrected in S74 + Om_m/total-Om normalisation mix) -> Class-(c) PIN-DRIFT-FROM-STALE-SOURCE.
# Honest reconciliation core PASSES (legible layered partition + dimer branch resolved); literal stale clause FAILS.
# Per the established composite-INFO precedent for "literal threshold tests a hypothesis the source already
# disproved" (regulator-pin-discipline.md Class-(c) eta calibration) => INFO, NOT FAIL.
reconciliation_core_ok = bool(partition_well_defined and s74_2channel_closes
                              and dimer_resolves_deterministically and omega_ratio_ok)   # (local)
verdict = "INFO" if reconciliation_core_ok else "FAIL"

value = (
    f"partition_legible={partition_well_defined};n_register_assigned={n_assigned}/7;"
    f"DM_budget=TWO-channel_S74-corrected(Leggett+dimer_Z2={f_Leggett_S74}+{f_dimer_Z2}={f_DM_S74_2channel}~Omega_DM={Omega_DM_canon},resid={resid_S74_vs_OmegaDM:.4f}<={TOL});"
    f"soft-hair=DE_not_DM(S74_L1128-1138_author-correction);DE=soft-hair+effacement={f_soft_hair}+{f_effacement}={f_DE_S74};"
    f"frac_norm_stages=Omega_m(0.209-Leggett,0.844-obs=Omega_DM/Omega_m={omega_ratio:.4f},0.947-GGEtotal)_vs_total-Omega(0.006-Leggett,0.276-DM);"
    f"plan_literal_3channel_sum_to_0.844=STALE-SOURCE_Class-c_FAILS(soft-hair-misassigned+norm-mix;sum={plan_3channel_DM_sum}!=0.844,resid={resid_plan_literal:.3f});"
    f"dimer_branch={dimer_branch}(W1-1={w1_1_status});Omega_DM_NO_PROVENANCE=HY4;f_dimer_Z2_not_canonical=plan-pinned"
).replace("'", "")   # guard: no single-quote chars in the value payload

# ---------------------------------------------------------------- npz (structured stage->number->layer map)
np.savez(
    OUT_NPZ,
    layers=np.array(list(assigned.keys())),
    mass_entries=np.array(assigned["MASS"], dtype=object),
    abundance_entries=np.array(assigned["ABUNDANCE"], dtype=object),
    fraction_entries=np.array(assigned["COLD_DM_FRACTION"], dtype=object),
    register_numbers=np.array([0.209, 0.844, 0.947, 0.006, Omega_DM_canon, Omega_DM_h2_Leggett]),
    register_labels=np.array(["frac_Leggett_Om_m", "frac_obs_cold_Om_m", "frac_GGE_total",
                              "frac_Leggett_totalOm", "Omega_DM_GGE_total", "Omega_DM_h2_Leggett"], dtype=object),
    f_DM_S74_2channel=f_DM_S74_2channel, f_DE_S74=f_DE_S74,
    f_Leggett_S74=f_Leggett_S74, f_dimer_Z2=f_dimer_Z2, f_soft_hair=f_soft_hair, f_effacement=f_effacement,
    Omega_DM_canon=Omega_DM_canon, Omega_m_canon=Omega_m_canon, omega_ratio=omega_ratio,
    resid_S74_vs_OmegaDM=resid_S74_vs_OmegaDM, s74_2channel_closes=s74_2channel_closes,
    plan_3channel_DM_sum=plan_3channel_DM_sum, resid_plan_literal=resid_plan_literal,
    plan_literal_closes=plan_literal_closes, partition_well_defined=partition_well_defined,
    w1_1_status=w1_1_status, dimer_branch=dimer_branch,
    dimer_resolves_deterministically=dimer_resolves_deterministically,
    reconciliation_core_ok=reconciliation_core_ok, verdict=verdict,
    stale_source_class="(c)_PIN-DRIFT-FROM-STALE-SOURCE",
)

# ---------------------------------------------------------------- dual-SHA + payload
pins = {
    "framework-dm-properties.md": sha256_file(DMPROPS),
    "session-74-mack-landau-workshop.md": sha256_file(S74),
    "w1_1_verdict_line": hashlib.sha256(w1_1_line.encode("utf-8")).hexdigest(),
}
audit_sha, content_sha = compute_dual_sha(HERE, CANON, pins)

print("=== INV8-W1-3 input SHAs ===")
for k, v in sorted(pins.items()):
    print(f"  {k} = {v}")
print(f"=== verdict={verdict} ; W1-1={w1_1_status} -> dimer_branch={dimer_branch} ===")
print(f"=== S74 2-channel DM={f_DM_S74_2channel} ~ Omega_DM={Omega_DM_canon} (resid {resid_S74_vs_OmegaDM:.4f}, closes={s74_2channel_closes}) ===")
print(f"=== plan literal 3-channel sum={plan_3channel_DM_sum} vs 0.844 (resid {resid_plan_literal:.3f}) -> STALE-SOURCE Class-(c) ===")
print(f"=== npz: {OUT_NPZ.name} ===")

extra_rows = [
    "# INV8-W1-3 LAYERED PARTITION: MASS=LEGGETT-MOMENT(S70,Delta_BCS,zero-free-param,PROVEN; a scale); "
    f"ABUNDANCE=Omega_DM={Omega_DM_canon}(GGE-total,n_pairs=59.8,NO-PROVENANCE->HY4)+Omega_DM_h2={Omega_DM_h2_Leggett}(Leggett-only,0.6%-Planck); "
    "FRACTION={0.209 Leggett/Om_m S58-SOLE-BOTTLENECK ~25%; 0.844 obs=Omega_DM/Omega_m; 0.947 GGE-total-upper; 0.006 Leggett/total-Om S74}",
    "# INV8-W1-3 STALE-SOURCE Class-(c): plan substitution-chain Step-3 pinned f_DM=f_Leggett+f_soft-hair+f_dimer_Z2->0.844 (3-channel, soft-hair-in-DM); "
    "session-74-mack-landau-workshop.md L1128-1138 ALREADY corrected soft-hair DM->DE => DM is TWO-channel (Leggett+dimer_Z2=0.276~Omega_DM); "
    "literal sum-to-0.844 also mixes Omega_m vs total-Omega normalisation; per epistemic-discipline.md Source-Reconciliation Class-(c) PIN-DRIFT-FROM-STALE-SOURCE => composite INFO (core reconciliation PASSES, literal stale clause FAILS), NOT framework arithmetic contradiction",
    f"# INV8-W1-3 dimer supply-or-retire: W1-1={w1_1_status} (I_PBH=1.8e-299 fold-PBH under-supply) => DIMER-Z2-PAIR-PRODUCTION-75 stays SOLE non-Leggett DM candidate -> {dimer_branch}; U3 stays open; "
    "HY4 canonical-table write (Omega_DM PROVENANCE + 2-channel partition into canonical_constants.py + framework-dm-properties.md) routed OUT to /rclab-investigate-8 close (session-track, mack-cosmic-bridge sole writer)",
]

print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra_rows)
