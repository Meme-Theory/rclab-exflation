#!/usr/bin/env python3
"""
s61_gl_staircase.py — Ginzburg-Landau Free Energy for CC Staircase
====================================================================

Task: GL-STAIRCASE-61
Agent: Landau Condensed-Matter Theorist

PHYSICS:
  The discrete E_GS(N) staircase has Gi = 421,000 — fluctuations completely
  wash out the individual steps. But the Ginzburg-Landau free energy F(n)
  in the CONTINUOUS pair density n = N/N_modes is a well-defined thermodynamic
  potential even when discrete features are smeared. This is exactly how
  Landau theory works: it captures the macroscopic phase structure while
  remaining agnostic about microscopic discreteness.

  The CC gap in the GL picture emerges from the curvature d^2F/dn^2 at the
  equilibrium density n_eq, not from discrete step heights. This mirrors
  Volovik's q-theory where Lambda = partial F / partial q |_{q=q_eq}.

METHOD:
  1. Load E_GS(N) for N = 0..4 from both baseline and compound datasets.
  2. Convert to pair density n = N/8.
  3. Fit F(n) = F_0 + a*n + b*n^2 + c*n^3 (Landau polynomial, cubic).
  4. Also fit quartic F(n) = F_0 + a*n + b*n^2 + c*n^3 + d*n^4.
  5. Find equilibrium n_eq from dF/dn = 0.
  6. Pair susceptibility: chi_q = 1 / (d^2F/dn^2)|_{n_eq}.
  7. CC gap (GL): delta_Lambda = (d^2F/dn^2)|_{n_eq} * (1/N_modes)^2 / 2
     = 1 / (2 * N_modes^2 * chi_q).

GATE: GL-STAIRCASE-61
  PASS if chi_q_min < 0.1
  FAIL if chi_q > 0.5 everywhere
  INFO if chi_q_min in [0.1, 0.5]

Output: s61_gl_staircase.npz, s61_gl_staircase.png
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Import canonical constants
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import tau_fold, rho_Lambda_obs, M_KK_gravity as M_KK

# ===========================================================================
#  1. LOAD DATA
# ===========================================================================
data_dir = Path(__file__).parent

# Baseline staircase (S60)
d_base = np.load(data_dir / "s60_staircase_ext.npz", allow_pickle=True)
E_GS_baseline = d_base["E_GS_A"]  # N = 0,1,2,3,4
N_modes = int(d_base["N_modes"])   # = 8

# Compound staircase (S61, with Penrose + Josephson + Bekenstein corrections)
d_comp = np.load(data_dir / "s61_compound_staircase.npz", allow_pickle=True)
E_GS_compound = d_comp["E_GS_compound"]  # N = 0,1,2,3,4

# Pair number and pair density
N_values = np.arange(len(E_GS_baseline))  # [0, 1, 2, 3, 4]
n_values = N_values / N_modes               # [0, 0.125, 0.25, 0.375, 0.5]

print("=" * 70)
print("GL-STAIRCASE-61: Ginzburg-Landau Free Energy for CC Staircase")
print("=" * 70)
print()
print(f"N_modes = {N_modes}")
print(f"tau_fold = {tau_fold}")
print(f"N_values = {N_values}")
print(f"n_values = {n_values}")
print()
print("E_GS (baseline):  ", E_GS_baseline)
print("E_GS (compound):  ", E_GS_compound)
print()

# ===========================================================================
#  2. FIT LANDAU POLYNOMIAL F(n) = F_0 + a*n + b*n^2 + c*n^3 [+ d*n^4]
# ===========================================================================

def fit_landau_polynomial(n, F, degree=3):
    """
    Fit F(n) to a polynomial of given degree.
    Returns coefficients [F_0, a, b, c, ...] in ascending power order.
    """
    # numpy polyfit returns coefficients in DESCENDING order
    coeffs_desc = np.polyfit(n, F, degree)
    # Reverse to ascending: [F_0, a, b, c, ...]
    coeffs_asc = coeffs_desc[::-1]
    return coeffs_asc, coeffs_desc


def analyze_landau_free_energy(n_data, F_data, coeffs_desc, label, N_modes_local):
    """
    Given polynomial coefficients (descending order from np.polyfit),
    find equilibrium, susceptibility, and CC gap.
    """
    # Construct polynomial and its derivatives
    F_poly = np.poly1d(coeffs_desc)
    dF = F_poly.deriv(1)   # dF/dn
    d2F = F_poly.deriv(2)  # d^2F/dn^2

    # Fine grid for analysis
    n_fine = np.linspace(0, 0.6, 10000)
    F_fine = F_poly(n_fine)
    dF_fine = dF(n_fine)
    d2F_fine = d2F(n_fine)

    # Find equilibrium: dF/dn = 0
    # Look for sign changes in dF_fine within physical range [0, 0.5]
    mask_phys = (n_fine >= 0) & (n_fine <= 0.55)
    dF_phys = dF_fine[mask_phys]
    n_phys = n_fine[mask_phys]

    # Find all zero crossings
    sign_changes = np.where(np.diff(np.sign(dF_phys)))[0]
    n_eq_candidates = []
    for idx in sign_changes:
        # Linear interpolation for precise crossing
        n1, n2 = n_phys[idx], n_phys[idx + 1]
        f1, f2 = dF_phys[idx], dF_phys[idx + 1]
        n_cross = n1 - f1 * (n2 - n1) / (f2 - f1)
        n_eq_candidates.append(n_cross)

    # Also check boundary: if dF/dn > 0 at n=0 and polynomial is bounded,
    # the equilibrium might be at n=0 itself
    if len(n_eq_candidates) == 0:
        # No zero crossing: check if minimum of F is at boundary
        n_min_idx = np.argmin(F_fine[mask_phys])
        n_eq = n_phys[n_min_idx]
        eq_type = "boundary"
    else:
        # Find the TRUE minimum among candidates (d2F > 0)
        stable_eqs = []
        for nc in n_eq_candidates:
            d2F_val = d2F(nc)
            if d2F_val > 0:
                stable_eqs.append((nc, F_poly(nc), d2F_val))
        if len(stable_eqs) > 0:
            # Pick the one with lowest F
            stable_eqs.sort(key=lambda x: x[1])
            n_eq = stable_eqs[0][0]
            eq_type = "interior"
        else:
            # All extrema are maxima — use global minimum on [0, 0.5]
            n_min_idx = np.argmin(F_fine[mask_phys])
            n_eq = n_phys[n_min_idx]
            eq_type = "boundary (all extrema unstable)"

    # Curvature and susceptibility at equilibrium
    d2F_eq = d2F(n_eq)
    if d2F_eq > 0:
        chi_q = 1.0 / d2F_eq
    else:
        chi_q = np.inf  # unstable or flat

    # CC gap in GL picture
    # delta_Lambda = F(n_eq + 1/N_modes) - F(n_eq)
    # In the harmonic approximation: ~ (1/2) * d2F * (1/N_modes)^2
    delta_n = 1.0 / N_modes_local
    delta_Lambda_exact = F_poly(n_eq + delta_n) - F_poly(n_eq)
    delta_Lambda_harmonic = 0.5 * d2F_eq * delta_n**2

    # Residuals
    F_fit = F_poly(n_data)
    residuals = F_data - F_fit
    rms_residual = np.sqrt(np.mean(residuals**2))

    result = {
        "label": label,
        "n_eq": n_eq,
        "eq_type": eq_type,
        "F_eq": float(F_poly(n_eq)),
        "dF_eq": float(dF(n_eq)),
        "d2F_eq": float(d2F_eq),
        "chi_q": chi_q,
        "delta_Lambda_exact": delta_Lambda_exact,
        "delta_Lambda_harmonic": delta_Lambda_harmonic,
        "rms_residual": rms_residual,
        "n_eq_candidates": n_eq_candidates,
        "n_fine": n_fine,
        "F_fine": F_fine,
        "dF_fine": dF_fine,
        "d2F_fine": d2F_fine,
    }
    return result


print("-" * 70)
print("FITTING LANDAU POLYNOMIALS")
print("-" * 70)

results = {}
datasets = {
    "baseline": (E_GS_baseline, "Baseline (S60)"),
    "compound": (E_GS_compound, "Compound (S61)"),
}

for dset_key, (E_GS, dset_label) in datasets.items():
    print(f"\n{'='*50}")
    print(f"  Dataset: {dset_label}")
    print(f"{'='*50}")

    for degree in [3, 4]:
        deg_label = f"{dset_key}_deg{degree}"
        full_label = f"{dset_label}, degree {degree}"

        coeffs_asc, coeffs_desc = fit_landau_polynomial(n_values, E_GS, degree)

        print(f"\n  Degree {degree} fit:")
        print(f"    F(n) = {coeffs_asc[0]:.6f}", end="")
        symbols = ["", " n", " n^2", " n^3", " n^4"]
        for i in range(1, len(coeffs_asc)):
            sign = "+" if coeffs_asc[i] >= 0 else "-"
            print(f" {sign} {abs(coeffs_asc[i]):.6f}{symbols[i]}", end="")
        print()

        res = analyze_landau_free_energy(
            n_values, E_GS, coeffs_desc, full_label, N_modes
        )

        print(f"    n_eq = {res['n_eq']:.6f} ({res['eq_type']})")
        print(f"    F(n_eq) = {res['F_eq']:.6f}")
        print(f"    d^2F/dn^2 |_eq = {res['d2F_eq']:.6f}")
        print(f"    chi_q = 1/d2F = {res['chi_q']:.6f}")
        print(f"    delta_Lambda (exact) = {res['delta_Lambda_exact']:.6e}")
        print(f"    delta_Lambda (harmonic) = {res['delta_Lambda_harmonic']:.6e}")
        print(f"    RMS residual = {res['rms_residual']:.6e}")
        if len(res['n_eq_candidates']) > 0:
            print(f"    All dF/dn=0 crossings: {[f'{x:.4f}' for x in res['n_eq_candidates']]}")

        results[deg_label] = {
            "coeffs_asc": coeffs_asc,
            "coeffs_desc": coeffs_desc,
            "analysis": res,
        }

# ===========================================================================
#  3. IDENTIFY OPTIMAL FIT AND EXTRACT GATE QUANTITIES
# ===========================================================================

print("\n" + "=" * 70)
print("GATE EVALUATION: GL-STAIRCASE-61")
print("=" * 70)

# Collect chi_q values across all fits
chi_values = {}
for key, val in results.items():
    chi = val["analysis"]["chi_q"]
    chi_values[key] = chi
    print(f"  {key}: chi_q = {chi:.6f}")

chi_min = min(v for v in chi_values.values() if np.isfinite(v))
chi_min_key = [k for k, v in chi_values.items() if v == chi_min][0]
print(f"\n  chi_q minimum = {chi_min:.6f} (from {chi_min_key})")

# Gate logic
if chi_min < 0.1:
    gate_verdict = "PASS"
    gate_reason = f"chi_q_min = {chi_min:.6f} < 0.1: GL free energy has stiff curvature"
elif chi_min > 0.5:
    gate_verdict = "FAIL"
    gate_reason = f"chi_q_min = {chi_min:.6f} > 0.5: GL free energy too soft everywhere"
else:
    gate_verdict = "INFO"
    gate_reason = f"chi_q_min = {chi_min:.6f} in [0.1, 0.5]: intermediate curvature"

print(f"\n  GATE VERDICT: {gate_verdict}")
print(f"  REASON: {gate_reason}")

# ===========================================================================
#  4. PHYSICAL INTERPRETATION: CC GAP IN NATURAL UNITS
# ===========================================================================

print("\n" + "=" * 70)
print("PHYSICAL QUANTITIES")
print("=" * 70)

# Use the compound degree-3 fit as the primary result
# (it includes all corrections and cubic is the minimal Landau form)
primary = results["compound_deg3"]["analysis"]

print(f"\nPrimary fit: Compound, degree 3")
print(f"  n_eq = {primary['n_eq']:.6f} (equilibrium pair density)")
print(f"  N_eq = n_eq * N_modes = {primary['n_eq'] * N_modes:.4f} (equilibrium pair number)")
print(f"  chi_q = {primary['chi_q']:.6f} (pair susceptibility)")
print(f"  d2F/dn2 = {primary['d2F_eq']:.6f} (GL stiffness)")
print(f"  delta_Lambda_GL = {primary['delta_Lambda_exact']:.6e} (in M_KK units)")
print(f"  delta_Lambda_harmonic = {primary['delta_Lambda_harmonic']:.6e}")

# Convert to physical units
# E_GS is in units of M_KK. So F(n) is in M_KK units.
# CC gap in M_KK^4: delta_rho = delta_Lambda * M_KK^4 / Vol_fiber
# But what we really want is the ratio delta_Lambda / F scale
print(f"\n  GL gap / rho_Lambda_obs:")
print(f"    delta_Lambda_exact [M_KK units] = {primary['delta_Lambda_exact']:.6e}")
print(f"    This is the dimensionless GL contribution to CC at n = n_eq + 1/8")

# Also extract the Volovik q-theory connection:
# In q-theory: Lambda = (partial F / partial q)|_{q_eq}
# Here dF/dn|_{n_eq} = 0 by definition, so the CC = 0 at equilibrium.
# The RESIDUAL CC comes from the mismatch between discrete n and continuous n_eq.
delta_n_mismatch = primary["n_eq"] - round(primary["n_eq"] * N_modes) / N_modes
N_eq_rounded = round(primary["n_eq"] * N_modes)
n_eq_discrete = N_eq_rounded / N_modes

print(f"\n  Volovik q-theory connection:")
print(f"    Continuous n_eq = {primary['n_eq']:.6f}")
print(f"    Nearest discrete N = {N_eq_rounded}, n_discrete = {n_eq_discrete:.6f}")
print(f"    Mismatch delta_n = {primary['n_eq'] - n_eq_discrete:.6e}")
print(f"    Residual F at discrete: {primary['delta_Lambda_exact']:.6e} (vs F_eq = {primary['F_eq']:.6e})")

# ===========================================================================
#  5. COMPARISON: BASELINE vs COMPOUND
# ===========================================================================

print("\n" + "=" * 70)
print("COMPARISON: BASELINE vs COMPOUND (degree 3)")
print("=" * 70)

for key in ["baseline_deg3", "compound_deg3"]:
    r = results[key]["analysis"]
    c = results[key]["coeffs_asc"]
    print(f"\n  {key}:")
    print(f"    F_0 = {c[0]:.6f}, a = {c[1]:.6f}, b = {c[2]:.6f}, c = {c[3]:.6f}")
    print(f"    n_eq = {r['n_eq']:.6f}, chi_q = {r['chi_q']:.6f}")
    print(f"    delta_Lambda = {r['delta_Lambda_exact']:.6e}")

# ===========================================================================
#  6. PLOT
# ===========================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    "GL-STAIRCASE-61: Ginzburg-Landau Free Energy for CC Staircase\n"
    r"$F(n) = F_0 + an + bn^2 + cn^3$  (Landau polynomial in pair density $n = N/8$)",
    fontsize=13, fontweight="bold",
)

colors = {"baseline_deg3": "C0", "baseline_deg4": "C0",
          "compound_deg3": "C3", "compound_deg4": "C3"}
styles = {"baseline_deg3": "-", "baseline_deg4": "--",
          "compound_deg3": "-", "compound_deg4": "--"}

# Panel (a): F(n) — both datasets
ax = axes[0, 0]
ax.set_title("(a) Free energy F(n)", fontweight="bold")

for dset_key, (E_GS, dset_label) in datasets.items():
    col = "C0" if dset_key == "baseline" else "C3"
    ax.plot(n_values, E_GS, "o", color=col, markersize=8, label=f"E_GS {dset_label}", zorder=5)

    for degree in [3, 4]:
        deg_label = f"{dset_key}_deg{degree}"
        r = results[deg_label]
        n_fine = r["analysis"]["n_fine"]
        F_fine = r["analysis"]["F_fine"]
        ls = "-" if degree == 3 else "--"
        mask = (n_fine >= -0.02) & (n_fine <= 0.55)
        ax.plot(n_fine[mask], F_fine[mask], ls, color=col, alpha=0.7,
                label=f"deg {degree} {dset_key}")

        # Mark equilibrium
        n_eq = r["analysis"]["n_eq"]
        F_eq = r["analysis"]["F_eq"]
        if degree == 3:
            ax.axvline(n_eq, color=col, ls=":", alpha=0.4)
            ax.plot(n_eq, F_eq, "s", color=col, markersize=10, zorder=6)

ax.set_xlabel(r"Pair density $n = N/N_{modes}$")
ax.set_ylabel(r"$F(n)$ [M$_{KK}$ units]")
ax.legend(fontsize=7, loc="upper left")
ax.set_xlim(-0.02, 0.55)
ax.grid(True, alpha=0.3)

# Panel (b): dF/dn — both datasets, degree 3
ax = axes[0, 1]
ax.set_title(r"(b) Chemical potential $\mu = dF/dn$", fontweight="bold")

for dset_key, (E_GS, dset_label) in datasets.items():
    col = "C0" if dset_key == "baseline" else "C3"
    deg_label = f"{dset_key}_deg3"
    r = results[deg_label]["analysis"]
    n_fine = r["n_fine"]
    dF_fine = r["dF_fine"]
    mask = (n_fine >= -0.02) & (n_fine <= 0.55)
    ax.plot(n_fine[mask], dF_fine[mask], "-", color=col, label=f"{dset_label}")

    n_eq = r["n_eq"]
    ax.plot(n_eq, 0, "s", color=col, markersize=10, zorder=6)

ax.axhline(0, color="k", ls="-", alpha=0.3)
ax.set_xlabel(r"Pair density $n$")
ax.set_ylabel(r"$dF/dn$")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (c): d2F/dn2 (curvature / inverse susceptibility)
ax = axes[1, 0]
ax.set_title(r"(c) Inverse susceptibility $\chi_q^{-1} = d^2F/dn^2$", fontweight="bold")

for dset_key, (E_GS, dset_label) in datasets.items():
    col = "C0" if dset_key == "baseline" else "C3"
    deg_label = f"{dset_key}_deg3"
    r = results[deg_label]["analysis"]
    n_fine = r["n_fine"]
    d2F_fine = r["d2F_fine"]
    mask = (n_fine >= -0.02) & (n_fine <= 0.55)
    ax.plot(n_fine[mask], d2F_fine[mask], "-", color=col, label=f"{dset_label}")

    n_eq = r["n_eq"]
    d2F_eq = r["d2F_eq"]
    ax.plot(n_eq, d2F_eq, "s", color=col, markersize=10, zorder=6)

ax.axhline(0, color="k", ls="-", alpha=0.3)
ax.set_xlabel(r"Pair density $n$")
ax.set_ylabel(r"$d^2F/dn^2$")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (d): Summary table
ax = axes[1, 1]
ax.axis("off")
ax.set_title("(d) GL Summary", fontweight="bold")

rows = []
for key in ["baseline_deg3", "compound_deg3", "baseline_deg4", "compound_deg4"]:
    r = results[key]["analysis"]
    c = results[key]["coeffs_asc"]
    rows.append([
        key.replace("_", " "),
        f"{r['n_eq']:.4f}",
        f"{r['chi_q']:.4f}",
        f"{r['d2F_eq']:.3f}",
        f"{r['delta_Lambda_exact']:.3e}",
        f"{r['rms_residual']:.2e}",
    ])

table = ax.table(
    cellText=rows,
    colLabels=["Fit", r"$n_{eq}$", r"$\chi_q$", r"$d^2F/dn^2$",
               r"$\Delta\Lambda_{GL}$", "RMS"],
    loc="center",
    cellLoc="center",
)
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.1, 1.5)

# Gate verdict annotation
ax.text(
    0.5, 0.05,
    f"GATE: GL-STAIRCASE-61 = {gate_verdict}\n{gate_reason}",
    transform=ax.transAxes, ha="center", va="bottom", fontsize=10,
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.3",
        facecolor="lightgreen" if gate_verdict == "PASS" else
        ("lightyellow" if gate_verdict == "INFO" else "lightsalmon"),
        alpha=0.8,  # (local)
    ),
)

plt.tight_layout()
plt.savefig(data_dir / "s61_gl_staircase.png", dpi=150, bbox_inches="tight")
print(f"\nPlot saved: {data_dir / 's61_gl_staircase.png'}")

# ===========================================================================
#  7. SAVE DATA
# ===========================================================================

# Prepare arrays for saving
save_dict = {
    # Input data
    "N_values": N_values,
    "n_values": n_values,
    "N_modes": np.int64(N_modes),
    "tau_fold": np.float64(tau_fold),
    "E_GS_baseline": E_GS_baseline,
    "E_GS_compound": E_GS_compound,
}

# Save all fit results
for key, val in results.items():
    prefix = key  # e.g., "baseline_deg3"
    save_dict[f"{prefix}_coeffs_asc"] = val["coeffs_asc"]
    save_dict[f"{prefix}_coeffs_desc"] = val["coeffs_desc"]
    r = val["analysis"]
    save_dict[f"{prefix}_n_eq"] = np.float64(r["n_eq"])
    save_dict[f"{prefix}_F_eq"] = np.float64(r["F_eq"])
    save_dict[f"{prefix}_d2F_eq"] = np.float64(r["d2F_eq"])
    save_dict[f"{prefix}_chi_q"] = np.float64(r["chi_q"])
    save_dict[f"{prefix}_delta_Lambda_exact"] = np.float64(r["delta_Lambda_exact"])
    save_dict[f"{prefix}_delta_Lambda_harmonic"] = np.float64(r["delta_Lambda_harmonic"])
    save_dict[f"{prefix}_rms_residual"] = np.float64(r["rms_residual"])
    save_dict[f"{prefix}_eq_type"] = np.array(r["eq_type"])

# Gate
save_dict["gate_name"] = np.array("GL-STAIRCASE-61")
save_dict["gate_verdict"] = np.array(gate_verdict)
save_dict["gate_reason"] = np.array(gate_reason)
save_dict["chi_q_min"] = np.float64(chi_min)
save_dict["chi_q_min_fit"] = np.array(chi_min_key)

np.savez(data_dir / "s61_gl_staircase.npz", **save_dict)
print(f"Data saved: {data_dir / 's61_gl_staircase.npz'}")

# ===========================================================================
#  8. FINAL SUMMARY
# ===========================================================================

print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print(f"""
Primary result (compound, degree 3):
  F(n) = {results['compound_deg3']['coeffs_asc'][0]:.6f} + {results['compound_deg3']['coeffs_asc'][1]:.6f} n + {results['compound_deg3']['coeffs_asc'][2]:.6f} n^2 + {results['compound_deg3']['coeffs_asc'][3]:.6f} n^3
  n_eq = {results['compound_deg3']['analysis']['n_eq']:.6f}
  N_eq = {results['compound_deg3']['analysis']['n_eq'] * N_modes:.4f}
  chi_q = {results['compound_deg3']['analysis']['chi_q']:.6f}
  d^2F/dn^2 = {results['compound_deg3']['analysis']['d2F_eq']:.6f}
  delta_Lambda_GL = {results['compound_deg3']['analysis']['delta_Lambda_exact']:.6e}

Baseline comparison (baseline, degree 3):
  F(n) = {results['baseline_deg3']['coeffs_asc'][0]:.6f} + {results['baseline_deg3']['coeffs_asc'][1]:.6f} n + {results['baseline_deg3']['coeffs_asc'][2]:.6f} n^2 + {results['baseline_deg3']['coeffs_asc'][3]:.6f} n^3
  n_eq = {results['baseline_deg3']['analysis']['n_eq']:.6f}
  chi_q = {results['baseline_deg3']['analysis']['chi_q']:.6f}

GATE: GL-STAIRCASE-61 = {gate_verdict}
  {gate_reason}
""")
