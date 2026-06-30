"""
S84 W3-30: S84-SLOT-SPAN-SCALING
lizzi-spectral-functional-theorist

Gate ID: S84-SLOT-SPAN-SCALING
Hypothesis: span(k, L_max) obeys a power-law  C(k) * L_max^alpha(k)
            for k in {0, 2, 4} and L_max in {3, 5, 7, 9}, across the
            5-regulator F_KK family {zeta, Zubarev, SDW, dim-reg, lattice-BR}.
PASS: R^2 > 0.99 for each k.
INFO: 2/3 k-values R^2>0.99, one in [0.95, 0.99].
FAIL: any k has R^2 <= 0.95.

Substitution chain (locked norm, Lambda^2 = 1 at L_max=3 anchor):

  Step 1 (truncation scale of D_K^2 on Peter-Weyl):
      L_max acts as an angular-momentum cutoff. For SU(3) (Weyl dim d=8),
      the largest eigenvalue scales as
          Lambda^2(L_max) = L_max * (L_max + 2).
      (Standard Casimir scaling; reproduces S73b a_2 ~ L^4.04.)

  Step 2 (truncated Mellin moment of D_K^2 at slot k):
      f_k^R(L_max) := int_0^{Lambda(L_max)^2} x^{(k-1)/2} w^R(x) dx
      where w^R(x) is the regulator weight:
          w^zeta(x) = x^0             (zeta-renormalized, no kernel)
          w^SDW(x)  = 1{x<=1}         (sharp-DeWitt step at unit scale)
          w^Zub(x)  = 1/(1 + x/Lambda_Z^2)  (Lorentzian, Lambda_Z=1)
          w^dim(x)  = x^{-eps}        (dim-reg, eps=0.1 operational pin)
          w^lat(x)  = 1/2             (lattice-BR flat offset)

  Step 3 (closed-form integrals, truncation Lambda^2(L_max) == Q):
      zeta   : f_k^zeta(Q)  = Q^{(k+1)/2} / (k+1)       [raw Mellin power]
      SDW    : f_k^SDW(Q)   = 2/(k+1)   if Q>=1 else Q^{(k+1)/2} * 2/(k+1)
                (Q>=1 at L_max>=1, so constant 2/(k+1); L_max-independent)
      Zub    : f_k^Zub(Q)   = int_0^Q x^{(k-1)/2}/(1+x) dx
      dim    : f_k^dim(Q)   = Q^{(k+1)/2 - eps} / ((k+1)/2 - eps)
      lat    : f_k^lat(Q)   = (1/2) * Q^{(k+1)/2} / ((k+1)/2)

  Step 4 (span and regression):
      span(k, L_max) = max_R f_k^R / min_R f_k^R
      ln span = ln C(k) + alpha(k) * ln L_max   (linear regression)

  Direction:
      - zeta/dim-reg/lattice grow as Q^{(k+1)/2} ~ L_max^{k+1}.
      - SDW is L_max-constant (step kernel saturates).
      - Hence span grows at least as fast as L_max^{k+1} -> alpha(k) is expected
        positive and monotone in k. alpha(k=0) ~ 1, alpha(k=2) ~ 3, alpha(k=4) ~ 5.
      - Clean power-law fit expected because the closed forms ARE pure powers
        (up to the Zubarev log correction which is subleading).
"""
from __future__ import annotations
import sys, os, json, hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 1. INPUT SHA PINS
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
CANON_PY = os.path.join(HERE, "canonical_constants.py")
ATLAS_JSON = os.path.join(HERE, "s84_w3_vii_k_prop_atlas.json")
FTRAJ_NPZ = os.path.join(HERE, "s84_w3_f_traj_mellin_atlas.npz")

def _sha(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

sha_canon  = _sha(CANON_PY)
sha_atlas  = _sha(ATLAS_JSON) if os.path.exists(ATLAS_JSON) else "MISSING"
sha_ftraj  = _sha(FTRAJ_NPZ)  if os.path.exists(FTRAJ_NPZ)  else "MISSING"

print("== S84 W3-30  slot-span scaling  (lizzi) ==")
print(f"sha canonical_constants.py              = {sha_canon}")
print(f"sha s84_w3_vii_k_prop_atlas.json        = {sha_atlas}")
print(f"sha s84_w3_f_traj_mellin_atlas.npz      = {sha_ftraj}")

# ---------------------------------------------------------------------------
# Section 2. PIN MAP — L_max scan, slot labels, regulator family
# ---------------------------------------------------------------------------
L_max_scan = np.array([3, 5, 7, 9], dtype=int)       # (local) plan pin
k_slots    = np.array([0, 2, 4], dtype=int)          # (local) plan pin
F_KK       = ["zeta", "Zubarev", "SDW", "dim-reg", "lattice-BR"]  # (local)
eps_dim    = 0.1                                     # (local) dim-reg operational pin

def Lambda2(L: int) -> float:
    """Step 1: SU(3) Peter-Weyl Casimir-like truncation scale."""
    return float(L) * float(L + 2)                   # (local)

# ---------------------------------------------------------------------------
# Section 3. REGULATOR-SPECIFIC TRUNCATED MELLIN MOMENTS f_k^R(L)
# ---------------------------------------------------------------------------
def f_zeta(k: int, L: int) -> float:
    Q = Lambda2(L)                                   # (local)
    p = (k + 1.0) / 2.0                              # (local)
    return (Q ** p) / (k + 1.0)                      # (local)

def f_sdw(k: int, L: int) -> float:
    # SDW step kernel saturates at Q>=1 (always true for L>=1):
    return 2.0 / (k + 1.0)                           # (local)

def f_zub(k: int, L: int) -> float:
    # f_k^Zub(Q) = int_0^Q x^((k-1)/2) / (1 + x) dx  — numerical quadrature
    Q = Lambda2(L)                                   # (local)
    # Avoid x=0 singularity for k=0 (integrand ~ x^{-1/2}, integrable)
    xs = np.linspace(1e-9, Q, 50001)                 # (local)
    ys = (xs ** ((k - 1) / 2.0)) / (1.0 + xs)        # (local)
    return float(np.trapezoid(ys, xs))               # (local)

def f_dim(k: int, L: int) -> float:
    Q = Lambda2(L)                                   # (local)
    p = (k + 1.0) / 2.0 - eps_dim                    # (local)
    return (Q ** p) / p                              # (local)

def f_lat(k: int, L: int) -> float:
    Q = Lambda2(L)                                   # (local)
    p = (k + 1.0) / 2.0                              # (local)
    return 0.5 * (Q ** p) / p                        # (local)

REG_FUNCS = {                                        # (local)
    "zeta":       f_zeta,
    "Zubarev":    f_zub,
    "SDW":        f_sdw,
    "dim-reg":    f_dim,
    "lattice-BR": f_lat,
}

# ---------------------------------------------------------------------------
# Section 4. COMPUTE SPAN(k, L_max) AND POWER-LAW FIT
# ---------------------------------------------------------------------------
print("\n-- f_k^R(L_max) table --")
span_table = np.zeros((len(k_slots), len(L_max_scan)))  # (local)
moment_cube = np.zeros((len(k_slots), len(L_max_scan), len(F_KK)))  # (local)
for i, k in enumerate(k_slots):
    print(f"\n  k = {k}")
    print(f"  {'L_max':>6s} | " + " ".join(f"{R:>12s}" for R in F_KK) + f" | {'span':>12s}")
    for j, L in enumerate(L_max_scan):
        vals = []                                    # (local)
        for m, R in enumerate(F_KK):
            v = REG_FUNCS[R](int(k), int(L))         # (local)
            moment_cube[i, j, m] = v
            vals.append(v)
        vals_arr = np.array(vals)                    # (local)
        s = float(np.max(vals_arr) / np.min(vals_arr))  # (local) span
        span_table[i, j] = s
        print(f"  {int(L):>6d} | " + " ".join(f"{v:>12.4e}" for v in vals_arr)
              + f" | {s:>12.4e}")

# Power-law fit per k: ln(span) = ln C + alpha * ln L_max
fits = []                                            # (local)
print("\n-- per-k power-law fits  ln span = ln C + alpha * ln L_max --")
print(f"  {'k':>3s} | {'alpha':>10s} {'ln C':>10s} {'C':>12s} {'R^2':>10s}  class")
R2_list = []                                         # (local)
alpha_list = []                                      # (local)
C_list = []                                          # (local)
for i, k in enumerate(k_slots):
    x = np.log(L_max_scan.astype(float))             # (local)
    y = np.log(span_table[i, :])                     # (local)
    alpha, lnC = np.polyfit(x, y, 1)                 # (local)
    y_pred = alpha * x + lnC                         # (local)
    ss_res = float(np.sum((y - y_pred) ** 2))        # (local)
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))    # (local)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0  # (local)
    if R2 > 0.99:
        cls = "CLEAN"                                # (local)
    elif R2 > 0.95:
        cls = "SOFT"                                 # (local)
    else:
        cls = "NON-POWER"                            # (local)
    fits.append({"k": int(k), "alpha": float(alpha), "lnC": float(lnC),
                 "C": float(np.exp(lnC)), "R2": float(R2), "class": cls})
    R2_list.append(R2)
    alpha_list.append(float(alpha))
    C_list.append(float(np.exp(lnC)))
    print(f"  {int(k):>3d} | {alpha:>10.4f} {lnC:>10.4f} {np.exp(lnC):>12.4e} "
          f"{R2:>10.6f}  {cls}")

# ---------------------------------------------------------------------------
# Section 5. VERDICT LOGIC
# ---------------------------------------------------------------------------
n_clean = sum(1 for r in R2_list if r > 0.99)        # (local)
n_soft  = sum(1 for r in R2_list if 0.95 < r <= 0.99)  # (local)
n_bad   = sum(1 for r in R2_list if r <= 0.95)       # (local)

if n_clean == len(k_slots):
    verdict = "PASS"
    meaning = "Clean power-law scaling on all k in {0,2,4}; span(k,L_max) tabulatable."
elif n_clean == len(k_slots) - 1 and n_soft == 1:
    verdict = "INFO"
    meaning = "2/3 k-slots clean, 1 soft — partial power-law, one slot multi-scale."
else:
    verdict = "FAIL"
    meaning = "Non-power-law scaling; multi-scale or crossover behavior."

print(f"\nverdict = {verdict}  (n_clean={n_clean}  n_soft={n_soft}  n_bad={n_bad})")
print(f"meaning : {meaning}")

# Structural note: alpha(k) monotone in k?
alpha_monotone = all(alpha_list[i] < alpha_list[i+1] for i in range(len(alpha_list)-1))
print(f"alpha monotone-increasing in k: {alpha_monotone}  "
      f"(alphas = {['%.3f' % a for a in alpha_list]})")

# ---------------------------------------------------------------------------
# Section 6. CLOSURE SHA  (unique pin-map -- includes gate_id to avoid
#                         sibling-gate collisions per S84 audit)
# ---------------------------------------------------------------------------
pin_map = {
    "gate_id": "S84-SLOT-SPAN-SCALING",
    "script_path": "computations/session-84/s84_w3_slot_span_scaling.py",
    "canonical_constants.py": sha_canon,
    "s84_w3_vii_k_prop_atlas.json": sha_atlas,
    "s84_w3_f_traj_mellin_atlas.npz": sha_ftraj,
    "L_max_scan": L_max_scan.tolist(),
    "k_slots": k_slots.tolist(),
    "F_KK": F_KK,
    "eps_dim": eps_dim,
    "span_table": span_table.tolist(),
    "alpha_list": alpha_list,
    "C_list": C_list,
    "R2_list": [float(r) for r in R2_list],
    "scheme": "ConvA-F_KK5",
    "convention": "locked-norm-truncated-Mellin",
}
closure_str = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
closure_sha = hashlib.sha256(closure_str.encode("utf-8")).hexdigest()
print(f"\nclosure_sha256 = {closure_sha}")

# ---------------------------------------------------------------------------
# Section 7. OUTPUTS
# ---------------------------------------------------------------------------
atlas = {
    "gate_id": "S84-SLOT-SPAN-SCALING",
    "classification": "GEOMETRIC",
    "L_max_scan": L_max_scan.tolist(),
    "k_slots": k_slots.tolist(),
    "F_KK": F_KK,
    "eps_dim": eps_dim,
    "moment_cube_shape": list(moment_cube.shape),
    "span_table": span_table.tolist(),
    "fits": fits,
    "n_clean": n_clean,
    "n_soft": n_soft,
    "n_bad": n_bad,
    "alpha_monotone_in_k": bool(alpha_monotone),
    "verdict": verdict,
    "meaning": meaning,
    "closure_sha256": closure_sha,
    "input_shas": {
        "canonical_constants.py": sha_canon,
        "s84_w3_vii_k_prop_atlas.json": sha_atlas,
        "s84_w3_f_traj_mellin_atlas.npz": sha_ftraj,
    },
}

out_json = os.path.join(HERE, "s84_w3_slot_span_scaling.json")
out_npz  = os.path.join(HERE, "s84_w3_slot_span_scaling.npz")
out_png  = os.path.join(HERE, "s84_w3_slot_span_scaling.png")

with open(out_json, "w") as fh:
    json.dump(atlas, fh, indent=2)
np.savez(out_npz,
         L_max_scan=L_max_scan, k_slots=k_slots,
         moment_cube=moment_cube, span_table=span_table,
         alpha=np.array(alpha_list), C=np.array(C_list),
         R2=np.array(R2_list), closure_sha256=closure_sha)

# Plot: log-log span vs L_max per k
fig, axs = plt.subplots(1, len(k_slots), figsize=(4.4*len(k_slots), 4.6), sharey=False)
for i, k in enumerate(k_slots):
    ax = axs[i]
    ax.loglog(L_max_scan, span_table[i, :], "o", markersize=10, color=f"C{i}",
              label=f"span(k={k},L)")
    Lgrid = np.linspace(L_max_scan.min(), L_max_scan.max(), 100)  # (local)
    ax.loglog(Lgrid, C_list[i] * Lgrid ** alpha_list[i], "--", color=f"C{i}",
              label=f"fit alpha={alpha_list[i]:.3f}  R^2={R2_list[i]:.4f}")
    ax.set_xlabel("L_max")
    ax.set_ylabel("span(k, L_max)")
    ax.set_title(f"k = {k}")
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, which="both", alpha=0.3)
fig.suptitle(f"S84 W3-30 slot-span scaling — verdict={verdict}  "
             f"(clean={n_clean}/{len(k_slots)}, alpha-monotone={alpha_monotone})")
fig.tight_layout()
fig.savefig(out_png, dpi=140)
plt.close(fig)

# ---------------------------------------------------------------------------
# Section 8. FINAL 4-TUPLE TAG
# ---------------------------------------------------------------------------
alpha_str = "[" + ",".join(f"{a:.4f}" for a in alpha_list) + "]"
R2_str    = "[" + ",".join(f"{r:.4f}" for r in R2_list) + "]"
value_str = f"alpha={alpha_str};R2={R2_str}"
print(f"\n(value={value_str}, scheme=ConvA-F_KK5, convention=locked-norm-truncated-Mellin, L_max=scan{L_max_scan.tolist()})")
print(f"VERDICT-LINE: S84-SLOT-SPAN-SCALING: {verdict} -- value={value_str} "
      f"scheme=ConvA-F_KK5 convention=locked-norm-truncated-Mellin "
      f"L_max=scan{L_max_scan.tolist()} sha256={closure_sha}")
