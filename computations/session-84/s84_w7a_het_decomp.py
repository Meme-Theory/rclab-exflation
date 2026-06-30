"""
S84 W7a-72: S84-HET-DECOMP
Test whether framework's Psi_+ = C^16 embeds into E_8 adjoint via
E_6 x SU(3) -> SO(10) x U(1) -> SU(5) -> SM branching (Slansky 1981).

Classification: GEOMETRIC (spectral-triple representation content).
Agent: kaku-speculative-theorist.

Pre-work (knowledge MCP):
  search_knowledge("E_8 branching heterotic A_F Psi_+")  -> confirms
    PERMANENT result: SM quantum numbers from Psi_+ = C^16 (S7).

Method:
  1. Tabulate the Slansky 1981 branching chain:
     E_8 -> E_6 x SU(3)
     27 of E_6 -> 16 + 10 + 1 under SO(10) x U(1)
     16 of SO(10) -> 10 + 5-bar + 1 under SU(5)
     10 of SU(5) -> (3,2,+1/6) + (3-bar,1,-2/3) + (1,1,+1)  under SM
      5-bar of SU(5) -> (3-bar,1,+1/3) + (1,2,-1/2)          under SM
       1 of SU(5) -> (1,1,0)
  2. Tabulate framework Psi_+ = C^16 (from A_F = C+H+M_3(C), S7 permanent).
  3. Check set equality of (SU(3)_C, SU(2)_L, Y) triples between framework
     and heterotic 16 of SO(10).
  4. hypercharge_preserved = True iff ratio Y_framework/Y_heterotic = const
     for all 16 entries (rational equality, no normalization freedom since
     U(1)_Y convention is fixed by SU(5) embedding on both sides).
  5. Cross-checks:
     (a) anomaly cancellation: tr(Y) = 0 and tr(Y^3) = 0 per generation
     (b) total dim count = 16
     (c) E_8 branching completeness: 248 = 78+8+27*3+27bar*3 = 78+8+81+81 = 248

Threshold (pre-registered):
  PASS:  best_match >= 0.50 AND hypercharge_preserved AND anomaly_cancellation
  INFO:  0.25 <= best_match < 0.50 OR (>= 0.50 w/ hypercharge mismatch)
  FAIL:  best_match < 0.25

Substitution chain (hypercharge preservation):
  Step 1: Y_framework = {+1/6, -2/3, +1/3, -1/2, +1, 0} (from A_F)
  Step 2: Y_heterotic = U(1)_Y from SU(5) Georgi-Glashow embedding
          inside 16 of SO(10) inside 27 of E_6 inside E_8.
  Step 3: Match triples (SU(3)_C, SU(2)_L, Y) component-wise.
  Step 4: If 16 of SO(10) reproduces all 16 framework triples -> MATCH.
"""

from canonical_constants import *  # tau_fold, M_KK, etc. (not used here but mandatory)
import hashlib
import json
import numpy as np
from fractions import Fraction
from pathlib import Path

# -------------------------------------------------------------------
# SHA-256 input pins (mandatory S81+)
# -------------------------------------------------------------------

def sha256_of_file(p: Path) -> str:
    """Return SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

SCRIPT_PATH = Path(__file__).resolve()
CC_PATH = SCRIPT_PATH.parent / "canonical_constants.py"

sha_script = sha256_of_file(SCRIPT_PATH)     # (local)
sha_cc = sha256_of_file(CC_PATH)             # (local)

print("=" * 72)
print("S84 W7a-72  S84-HET-DECOMP")
print("  script sha256: " + sha_script)
print("  canonical_constants.py sha256: " + sha_cc)
print("=" * 72)

# -------------------------------------------------------------------
# Step 1: Framework Psi_+ = C^16 (S7-S8 permanent)
#   Each entry: (name, SU(3)_C_dim_signed, SU(2)_L_dim, Y_fraction, multiplicity)
#   SU(3)_C_dim_signed: +3 = fundamental, -3 = antifundamental, +1 = singlet
# -------------------------------------------------------------------

# Standard SM convention: all 16 entries of Psi_+ in LEFT-HANDED form
#   Q_L   : (3,  2, +1/6)   dim = 6
#   u_R^c : (-3, 1, -2/3)   dim = 3   (antifundamental because left-handed)
#   d_R^c : (-3, 1, +1/3)   dim = 3
#   L_L   : ( 1, 2, -1/2)   dim = 2
#   e_R^c : ( 1, 1,  +1)    dim = 1
#   nu_R^c: ( 1, 1,   0)    dim = 1
# Total = 6 + 3 + 3 + 2 + 1 + 1 = 16.

psi_plus_framework = [
    # (label,          SU3c,  SU2L, Y,              dim)
    ("Q_L",            3,     2,    Fraction(1, 6), 6),
    ("u_R_conj",      -3,     1,    Fraction(-2, 3), 3),
    ("d_R_conj",      -3,     1,    Fraction(1, 3), 3),
    ("L_L",            1,     2,    Fraction(-1, 2), 2),
    ("e_R_conj",       1,     1,    Fraction(1, 1), 1),
    ("nu_R_conj",      1,     1,    Fraction(0, 1), 1),
]

total_dim_framework = sum(r[4] for r in psi_plus_framework)  # (local)
assert total_dim_framework == 16, f"Framework Psi_+ dim = {total_dim_framework}, expected 16"
print(f"\nFramework Psi_+ total dim: {total_dim_framework} (expected 16) OK")

# -------------------------------------------------------------------
# Step 2: Heterotic branching via Slansky 1981 tables.
#   E_8 (adjoint 248) -> E_6 x SU(3):
#     248 = (78, 1) + (1, 8) + (27, 3) + (27-bar, 3-bar)
#   Dimensions: 78 + 8 + 27*3 + 27*3 = 78 + 8 + 81 + 81 = 248. CHECK.
#
#   27 of E_6 -> SO(10) x U(1)_psi:
#     27 = 16_{+1} + 10_{-2} + 1_{+4}   (Slansky Table 56; psi charges)
#   Dimensions: 16 + 10 + 1 = 27. CHECK.
#
#   16 of SO(10) -> SU(5) x U(1)_chi:
#     16 = 10_{-1} + 5-bar_{+3} + 1_{-5}
#   Dimensions: 10 + 5 + 1 = 16. CHECK.
#
#   SU(5) -> SU(3)_C x SU(2)_L x U(1)_Y (Georgi-Glashow):
#     10 = (3, 2, +1/6) + (3-bar, 1, -2/3) + (1, 1, +1)    dim 6+3+1 = 10
#     5-bar = (3-bar, 1, +1/3) + (1, 2, -1/2)              dim 3+2   = 5
#     1 = (1, 1, 0)                                        dim 1
#   Total = 10 + 5 + 1 = 16. CHECK.
#
#   Standard embedding: U(1)_Y normalization = Slansky convention.
# -------------------------------------------------------------------

# The 16 of SO(10) fully decomposed to SM irreps:
so10_16_decomp = [
    # (origin_SU5_irrep, SU3c,  SU2L, Y,              dim)
    ("10",               3,     2,    Fraction(1, 6), 6),
    ("10",              -3,     1,    Fraction(-2, 3), 3),
    ("10",               1,     1,    Fraction(1, 1), 1),
    ("5-bar",           -3,     1,    Fraction(1, 3), 3),
    ("5-bar",            1,     2,    Fraction(-1, 2), 2),
    ("1",                1,     1,    Fraction(0, 1), 1),
]

total_dim_so10_16 = sum(r[4] for r in so10_16_decomp)  # (local)
assert total_dim_so10_16 == 16, f"SO(10) 16 dim = {total_dim_so10_16}, expected 16"
print(f"Heterotic 16 of SO(10) total dim: {total_dim_so10_16} (expected 16) OK")

# Cross-check (c): 27 of E_6 completeness
e6_27_decomp_sm = so10_16_decomp + [
    # 10_{-2} of SO(10) -> (1,2,+1/2) + (1,2,-1/2) + (3,1,-1/3) + (3-bar,1,+1/3)
    # These are the Higgs and colored-Higgs sector; NOT part of Psi_+.
    ("10_SO10", 1, 2, Fraction(1, 2), 2),
    ("10_SO10", 1, 2, Fraction(-1, 2), 2),
    ("10_SO10", 3, 1, Fraction(-1, 3), 3),
    ("10_SO10", -3, 1, Fraction(1, 3), 3),
    # 1_{+4} of SO(10) -> (1,1,0) singlet
    ("1_SO10", 1, 1, Fraction(0, 1), 1),
]
total_dim_e6_27 = sum(r[4] for r in e6_27_decomp_sm)  # (local)
assert total_dim_e6_27 == 27, f"E_6 27 dim = {total_dim_e6_27}, expected 27"
print(f"Heterotic 27 of E_6 total dim: {total_dim_e6_27} (expected 27) OK")

# Cross-check E_8 adjoint:
dim_E8 = 78 + 8 + 27 * 3 + 27 * 3  # (local)
assert dim_E8 == 248, f"E_8 adjoint total = {dim_E8}, expected 248"
print(f"E_8 adjoint under E_6xSU(3): 78 + 8 + 81 + 81 = {dim_E8} (expected 248) OK")

# -------------------------------------------------------------------
# Step 3: Match framework triples vs heterotic 16 of SO(10).
#   Framework entries are identified (up to ordering) with heterotic
#   entries if (SU3c_signed, SU2L_dim, Y_Fraction) agree exactly.
# -------------------------------------------------------------------

def canonical_triple(entry):
    """Strip label and dim; return (SU3c, SU2L, Y) triple for matching."""
    _, c, l, y, _ = entry
    return (int(c), int(l), Fraction(y))

framework_triples = sorted(canonical_triple(r) for r in psi_plus_framework)  # (local)
heterotic_triples = sorted(canonical_triple(r) for r in so10_16_decomp)      # (local)

print("\nFramework Psi_+ triples (SU3c, SU2L, Y):")
for t in framework_triples:
    print(f"  {t}")
print("Heterotic 16 of SO(10) triples (SU3c, SU2L, Y):")
for t in heterotic_triples:
    print(f"  {t}")

# Multiset match: require every framework triple to appear in heterotic decomp.
# Weighted by dim so that (3,2,+1/6) with dim=6 counts as 6/16 of the match.

framework_dim_map = {}  # (local)
for label, c, l, y, d in psi_plus_framework:
    key = (int(c), int(l), Fraction(y))
    framework_dim_map[key] = framework_dim_map.get(key, 0) + int(d)

heterotic_dim_map = {}  # (local)
for label, c, l, y, d in so10_16_decomp:
    key = (int(c), int(l), Fraction(y))
    heterotic_dim_map[key] = heterotic_dim_map.get(key, 0) + int(d)

matched_dim = 0  # (local)
for key, f_dim in framework_dim_map.items():
    h_dim = heterotic_dim_map.get(key, 0)
    matched_dim += min(f_dim, h_dim)

best_match = matched_dim / 16.0  # (local)
print(f"\nMatched dim (min over triples): {matched_dim} / 16 = {best_match:.4f}")

# -------------------------------------------------------------------
# Step 4: Hypercharge preservation.
#   For every framework triple, does the heterotic branching produce
#   exactly the same Y? Normalization k=1 (same SU(5) embedding both sides).
# -------------------------------------------------------------------

hypercharge_preserved = True  # (local)
hypercharge_ratio_set = set()  # (local)
for key, f_dim in framework_dim_map.items():
    if key not in heterotic_dim_map:
        hypercharge_preserved = False
        print(f"  MISS: framework triple {key} not in heterotic decomp")
        continue
    c, l, y = key
    # Y ratios (both sides have same Y if they agree triple-wise -> ratio = 1)
    if y != 0:
        hypercharge_ratio_set.add(Fraction(y, y))  # trivially 1
    # If y == 0, ratio undefined; skip (nu_R_conj is singlet).

# Consistency check: Y_framework / Y_heterotic must be a single constant
# across all nonzero-Y entries. Here it is trivially 1 since triples match.
if len(hypercharge_ratio_set) > 1:
    hypercharge_preserved = False
    print(f"  Multiple Y ratios detected: {hypercharge_ratio_set}")
elif len(hypercharge_ratio_set) == 1:
    print(f"  Y ratio (framework / heterotic): {list(hypercharge_ratio_set)[0]} (unique)")

print(f"hypercharge_preserved = {hypercharge_preserved}")

# -------------------------------------------------------------------
# Step 5: Anomaly cancellation cross-check.
#   For a single SM generation (16 of SO(10)), verify:
#     Sum_i d_i * Y_i     = 0   (U(1)_Y gauge anomaly, weighted by dim)
#     Sum_i d_i * Y_i^3   = 0   (U(1)_Y^3 anomaly)
#   Each irrep contributes d_i = SU3c_dim * SU2L_dim copies.
# -------------------------------------------------------------------

def d_abs(c, l):
    return abs(int(c)) * int(l)

sum_Y = Fraction(0)       # (local)
sum_Y3 = Fraction(0)      # (local)
for (_, c, l, y, _) in so10_16_decomp:
    d = d_abs(c, l)
    # For antifundamental (c<0), Y flips sign? No — Y is already signed
    # in our table. Conventional trace is over complex dim = |c|*l.
    sum_Y += d * Fraction(y)
    sum_Y3 += d * Fraction(y) ** 3

print(f"\nAnomaly cancellation check (16 of SO(10)):")
print(f"  Sum_i d_i * Y_i    = {sum_Y}   (expected 0)")
print(f"  Sum_i d_i * Y_i^3  = {sum_Y3}   (expected 0)")

anomaly_cancellation = (sum_Y == 0) and (sum_Y3 == 0)  # (local)
print(f"anomaly_cancellation = {anomaly_cancellation}")

# -------------------------------------------------------------------
# Step 6: Verdict
# -------------------------------------------------------------------

PASS_threshold = 0.50   # (local)
INFO_threshold = 0.25   # (local)

if best_match >= PASS_threshold and hypercharge_preserved and anomaly_cancellation:
    verdict = "PASS"
elif best_match >= INFO_threshold:
    verdict = "INFO"
else:
    verdict = "FAIL"

print(f"\n=== VERDICT ===")
print(f"best_match = {best_match:.4f}")
print(f"hypercharge_preserved = {hypercharge_preserved}")
print(f"anomaly_cancellation = {anomaly_cancellation}")
print(f"verdict = {verdict}")

# -------------------------------------------------------------------
# Closure SHA-256 over ordered input-pin map (S81+ canonical)
# -------------------------------------------------------------------

input_pin_map = {
    "script_sha256": sha_script,
    "canonical_constants_sha256": sha_cc,
    "scheme": "Slansky1981",
    "convention": "standard_embedding",
    "L_max": "N/A",
    "PASS_threshold": str(PASS_threshold),
    "INFO_threshold": str(INFO_threshold),
    "framework_Psi_plus_total_dim": total_dim_framework,
    "heterotic_16_SO10_total_dim": total_dim_so10_16,
    "E_8_adjoint_dim": dim_E8,
    "matched_dim": matched_dim,
    "best_match": f"{best_match:.6f}",
    "hypercharge_preserved": hypercharge_preserved,
    "anomaly_cancellation": anomaly_cancellation,
    "verdict": verdict,
}

pin_json = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
closure_sha = hashlib.sha256(pin_json.encode("utf-8")).hexdigest()  # (local)
print(f"\nclosure sha256 (64-char): {closure_sha}")
print(f"(pin_json length: {len(pin_json)} bytes)")

# -------------------------------------------------------------------
# Save data
# -------------------------------------------------------------------

out_data = SCRIPT_PATH.parent / "s84_w7a_72_data.npz"
np.savez(
    out_data,
    best_match=best_match,
    matched_dim=matched_dim,
    total_dim_framework=total_dim_framework,
    total_dim_so10_16=total_dim_so10_16,
    dim_E8=dim_E8,
    sum_Y=float(sum_Y),
    sum_Y3=float(sum_Y3),
    hypercharge_preserved=hypercharge_preserved,
    anomaly_cancellation=anomaly_cancellation,
    verdict_str=verdict,
    closure_sha=closure_sha,
    framework_triples=np.array([(c, l, float(y)) for (c, l, y) in framework_triples]),
    heterotic_triples=np.array([(c, l, float(y)) for (c, l, y) in heterotic_triples]),
)
print(f"data written: {out_data.name}")

# -------------------------------------------------------------------
# Plot (bar chart: framework dim vs heterotic dim by triple)
# -------------------------------------------------------------------

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    all_keys = sorted(set(framework_dim_map.keys()) | set(heterotic_dim_map.keys()),
                      key=lambda k: (float(k[2]), k[0], k[1]))  # sort by Y then rep
    labels = [f"({k[0]:+d},{k[1]},{k[2]})" for k in all_keys]
    f_vals = [framework_dim_map.get(k, 0) for k in all_keys]
    h_vals = [heterotic_dim_map.get(k, 0) for k in all_keys]

    x = np.arange(len(all_keys))  # (local)
    width = 0.38                   # (local)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(x - width / 2, f_vals, width, label="Framework Psi_+", color="#3c78d8")
    ax.bar(x + width / 2, h_vals, width, label="Heterotic 16 of SO(10)", color="#e69138")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=8)
    ax.set_ylabel("dim")
    ax.set_title(f"S84-HET-DECOMP: Psi_+ vs 16 of SO(10)  (match = {best_match:.3f}, {verdict})")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    plot_path = SCRIPT_PATH.parent / "s84_w7a_72_plot.png"
    fig.savefig(plot_path, dpi=140)
    plt.close(fig)
    print(f"plot written: {plot_path.name}")
except Exception as e:
    print(f"(plot skipped: {e})")

# -------------------------------------------------------------------
# Canonical verdict line (append to computations/session-84/s84_gate_verdicts.txt)
# -------------------------------------------------------------------

verdict_line = (
    f"S84-HET-DECOMP: {verdict} -- value={best_match:.4f} "
    f"scheme=Slansky1981 convention=standard_embedding L_max=N/A "
    f"sha256={closure_sha}"
)
print(f"\nVERDICT LINE (append to computations/session-84/s84_gate_verdicts.txt):")
print(verdict_line)

verdict_file = SCRIPT_PATH.parent / "s84_gate_verdicts.txt"
with open(verdict_file, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
print(f"verdict appended to {verdict_file.name}")
