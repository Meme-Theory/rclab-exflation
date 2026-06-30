"""
S84 W3-24: S84-F-TRAJ-MELLIN-ATLAS / S84-F-TRAJ-3-2-PERMANENT
lizzi-spectral-functional-theorist

Hypothesis: F_traj(k) = f_k^zeta / f_k^SDW = 3/2 universally across k in {0,2,4,6,8}
  -> candidate Lizzi a_2-ratio theorem.

Substitution chain (locked normalization, L_k = 1, Lambda^2 = 1):
  Step 1 (CC half-zeta at slot k):      f_k^zeta = 1
  Step 2 (sharp-DeWitt sqrt(x) kernel): f_k^SDW  = int_0^1 x^((k-1)/2) dx = 2/(k+1)
           (anchor at k=2: 2/(2+1) = 2/3  -- matches S83 G4 f2_SDW = 2/3)
  Step 3 (ratio per slot):              F_traj(k) = f_k^zeta / f_k^SDW = (k+1)/2
  Step 4 (threshold check):             |F_traj(k) - 3/2| < 1e-4 only when k = 2
  Direction: F_traj(k) is strictly monotone-increasing in k. The identity is
             k=2 specific, NOT universal. Theorem promotion FAILS.

Cross-schemes (Zubarev, dim-reg, lattice-BR): recorded per-slot as diagnostics.
"""
from __future__ import annotations
import sys, os, json, hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403
# ─── W6-71 Mellin discipline markers (S86 W0c-6 retrofit) ───
# MELLIN-CONVERGENCE-STRIP: -1, +3   # (W6-71_default; per-script audit needed)
# MELLIN-RESIDUE-EXTRACTION: residue-at-pole_via_lhopital   # (W6-71_default; per-script audit needed)
# MELLIN-COUNTERTERM-SUBTRACTION: a_2_zeta-regulated   # (W6-71_default; per-script audit needed)
# MELLIN-ANALYTIC-CONTINUATION-PATH: vertical-line_Re(s)=1   # (W6-71_default; per-script audit needed)
# MELLIN-CLOSURE-VERIFICATION: self-consistent_at_residue   # (W6-71_default; per-script audit needed)
# ─────────────────────────────────────────────────────────────


# ---------------------------------------------------------------------------
# Section 1. INPUT SHA PINS
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
ANCHOR_NPZ = os.path.join(HERE, "s83_w1_g4_epsilon_h_trajectory_fi.npz")
CANON_PY   = os.path.join(HERE, "canonical_constants.py")

def _sha(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

sha_anchor = _sha(ANCHOR_NPZ) if os.path.exists(ANCHOR_NPZ) else "MISSING"
sha_canon  = _sha(CANON_PY)

print("== S84 W3-24  F_traj Mellin atlas ==")
print(f"sha s83_w1_g4_epsilon_h_trajectory_fi.npz = {sha_anchor}")
print(f"sha canonical_constants.py                = {sha_canon}")

# ---------------------------------------------------------------------------
# Section 2. MELLIN SLOTS AND SLOT WEIGHTS
# ---------------------------------------------------------------------------
# Locked normalization per S83 G4 PRDR:
#   zeta     : f_k^zeta = 1 (CC half-zeta at slot k, Lambda^2=1, L_k=1)
#   SDW      : f_k^SDW  = 2/(k+1)  (sharp-DeWitt sqrt(x) kernel, L_k=1)
#   Zubarev  : f_k^Zub  = 1/(k+1)  (Lorentzian-cutoff Mellin, L_k=1)  [cross-check]
#   dim-reg  : f_k^dim  = 1         (dimensional regularization, MS-bar rescaling) [cross-check]
#   lat-BR   : f_k^lat  = 1/2       (lattice-BR scheme, k-independent offset)     [cross-check]

k_slots = np.array([0, 2, 4, 6, 8], dtype=int)
N_eval = len(k_slots)

def f_zeta(k):   return 1.0                 # CC half-zeta locked norm
def f_sdw(k):    return 2.0 / (k + 1.0)      # sqrt(x) heat-kernel integral
def f_zub(k):    return 1.0 / (k + 1.0)      # Lorentzian Mellin
def f_dim(k):    return 1.0                 # dim-reg (MS-bar rescale)
def f_lat(k):    return 0.5                 # lattice-BR offset

# ---------------------------------------------------------------------------
# Section 3. F_traj(k) PER SLOT — canonical zeta/SDW pair
# ---------------------------------------------------------------------------
F_traj_main = np.array([f_zeta(k) / f_sdw(k) for k in k_slots])  # (local)
tol_strict  = 1e-4                                               # (local)
dev         = np.abs(F_traj_main - 1.5)                          # (local)
strict_mask = dev < tol_strict                                   # (local)
near_mask   = (dev >= tol_strict) & (dev < 1e-2)                 # (local)

n_strict = int(strict_mask.sum())
n_near   = int(near_mask.sum())
n_not    = int((~(strict_mask | near_mask)).sum())

# Cross-scheme F_traj against SDW baseline (diagnostic; NOT part of 3/2 test)
F_zub_sdw = np.array([f_zub(k) / f_sdw(k) for k in k_slots])    # (local)
F_dim_sdw = np.array([f_dim(k) / f_sdw(k) for k in k_slots])    # (local)
F_lat_sdw = np.array([f_lat(k) / f_sdw(k) for k in k_slots])    # (local)

print("\n-- per-slot F_traj = f_k^zeta / f_k^SDW --")
print(f"  {'k':>3s} | {'f_zeta':>10s} {'f_SDW':>10s} {'F_traj':>10s} {'|F-3/2|':>12s}  class")
for i, k in enumerate(k_slots):
    cls = "STRICT-3/2" if strict_mask[i] else ("NEAR-3/2" if near_mask[i] else "NOT-3/2")
    print(f"  {int(k):>3d} | {f_zeta(k):>10.6f} {f_sdw(k):>10.6f} "
          f"{F_traj_main[i]:>10.6f} {dev[i]:>12.3e}  {cls}")

# Anchor cross-check: k=2 must reproduce S83 G4 exactly
F_k2 = F_traj_main[1]
anchor_ok = abs(F_k2 - 1.5) < 1e-12
print(f"\n-- anchor cross-check S83 G4 -- F_traj(k=2) = {F_k2:.12f}  (expect 1.5)  OK={anchor_ok}")

# ---------------------------------------------------------------------------
# Section 4. VERDICT LOGIC
# ---------------------------------------------------------------------------
if n_strict >= 4:
    verdict = "PASS"
    meaning = "Lizzi a_2-ratio theorem promoted (universal 3/2)."
elif n_strict == 3:
    verdict = "INFO"
    meaning = "Partial universality; triage per-slot."
else:
    verdict = "FAIL"
    meaning = "F_traj=3/2 is k=2-specific, not universal. Theorem proposal down-scoped."

value_str = "[" + ",".join(f"{v:.6f}" for v in F_traj_main) + "]"
print(f"\nverdict={verdict}  n_strict={n_strict}/{N_eval}  n_near={n_near}  n_not={n_not}")
print(f"meaning: {meaning}")

# ---------------------------------------------------------------------------
# Section 5. CLOSURE SHA
# ---------------------------------------------------------------------------
pin_map = {
    "s83_w1_g4_epsilon_h_trajectory_fi.npz": sha_anchor,
    "canonical_constants.py": sha_canon,
    "k_slots": k_slots.tolist(),
    "F_traj_main": [float(x) for x in F_traj_main],
    "tol_strict": tol_strict,
    "L_max": 5,
    "scheme": "zeta/SDW",
    "convention": "locked-norm",
}
closure_str = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
closure_sha = hashlib.sha256(closure_str.encode("utf-8")).hexdigest()
print(f"\nclosure_sha256 = {closure_sha}")

# ---------------------------------------------------------------------------
# Section 6. OUTPUTS
# ---------------------------------------------------------------------------
atlas = {
    "gate_id_atlas":    "S84-F-TRAJ-MELLIN-ATLAS",
    "gate_id_theorem":  "S84-F-TRAJ-3-2-PERMANENT",
    "classification":   "GEOMETRIC",
    "L_max":            5,
    "scheme":           "zeta/SDW",
    "convention":       "locked-norm",
    "k_slots":          k_slots.tolist(),
    "F_traj_zeta_SDW":  [float(x) for x in F_traj_main],
    "F_traj_Zub_SDW":   [float(x) for x in F_zub_sdw],
    "F_traj_dim_SDW":   [float(x) for x in F_dim_sdw],
    "F_traj_lat_SDW":   [float(x) for x in F_lat_sdw],
    "dev_from_3_2":     [float(x) for x in dev],
    "n_strict_3_2":     n_strict,
    "n_near_3_2":       n_near,
    "n_not_3_2":        n_not,
    "verdict":          verdict,
    "meaning":          meaning,
    "anchor_k2":        float(F_k2),
    "closure_sha256":   closure_sha,
    "input_shas": {
        "s83_w1_g4_epsilon_h_trajectory_fi.npz": sha_anchor,
        "canonical_constants.py": sha_canon,
    },
    "closed_form": "F_traj(k) = (k+1)/2",
}

out_json = os.path.join(HERE, "s84_w3_f_traj_mellin_atlas.json")
out_npz  = os.path.join(HERE, "s84_w3_f_traj_mellin_atlas.npz")
out_png  = os.path.join(HERE, "s84_w3_f_traj_mellin_atlas.png")

with open(out_json, "w") as fh:
    json.dump(atlas, fh, indent=2)
np.savez(out_npz,
         k_slots=k_slots, F_traj_main=F_traj_main,
         F_zub_sdw=F_zub_sdw, F_dim_sdw=F_dim_sdw, F_lat_sdw=F_lat_sdw,
         dev=dev, closure_sha256=closure_sha)

# Plot: F_traj vs k with 3/2 reference line
fig, ax = plt.subplots(figsize=(7.2, 4.6))
ax.axhline(1.5, color="k", linestyle="--", linewidth=1, label="3/2 reference")
ax.plot(k_slots, F_traj_main, "o-", color="C0", linewidth=2, markersize=9,
        label="F_traj = f_k^zeta / f_k^SDW = (k+1)/2")
ax.plot(k_slots, F_zub_sdw, "s:",  color="C1", alpha=0.7, label="Zubarev/SDW (diag)")
ax.plot(k_slots, F_dim_sdw, "^:",  color="C2", alpha=0.7, label="dim-reg/SDW (diag)")
ax.plot(k_slots, F_lat_sdw, "v:",  color="C3", alpha=0.7, label="lattice-BR/SDW (diag)")
for i, k in enumerate(k_slots):
    ax.annotate(f"{F_traj_main[i]:.2f}", (k, F_traj_main[i]),
                textcoords="offset points", xytext=(6, 6), fontsize=9)
ax.set_xlabel("Mellin slot k")
ax.set_ylabel("F_traj(k)")
ax.set_title(f"S84 W3-24 F_traj Mellin atlas — verdict={verdict}  ({n_strict}/{N_eval} STRICT-3/2)")
ax.legend(loc="best", fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(out_png, dpi=140)
plt.close(fig)

# ---------------------------------------------------------------------------
# Section 7. FINAL 4-TUPLE TAG
# ---------------------------------------------------------------------------
print(f"\n(value={value_str}, scheme=zeta/SDW, convention=locked-norm, L_max=5)")
print(f"VERDICT-LINE: S84-F-TRAJ-MELLIN-ATLAS: {verdict} -- value={value_str} "
      f"scheme=zeta/SDW convention=locked-norm L_max=5 sha256={closure_sha}")
print(f"VERDICT-LINE: S84-F-TRAJ-3-2-PERMANENT: {verdict} -- value=n_strict={n_strict}/{N_eval} "
      f"scheme=zeta/SDW convention=locked-norm L_max=5 sha256={closure_sha}")
