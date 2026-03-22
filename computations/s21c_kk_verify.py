#!/usr/bin/env python3
"""Quick verification of branching, T''(0), delta_T, S_signed for Stage 1 assessment."""

import numpy as np
from collections import defaultdict

# ========== SU(3) weight enumeration ==========
def su3_weights(p, q):
    pos_roots = [(2, -1), (-1, 2), (1, 1)]
    def inner(mu, nu):
        return (2*mu[0]*nu[0] + mu[0]*nu[1] + mu[1]*nu[0] + 2*mu[1]*nu[1]) / 3.0

    all_weights = {}
    visited = set()
    queue = [(p, q)]
    visited.add((p, q))

    while queue:
        m1, m2 = queue.pop(0)
        all_weights[(m1, m2)] = 0
        for alpha in [(2, -1), (-1, 2)]:
            new = (m1 - alpha[0], m2 - alpha[1])
            if new not in visited:
                a_num = q - new[1] - 2*new[0] + 2*p
                if a_num % 3 == 0:
                    a = a_num // 3
                    b = new[0] - p + 2*a
                    if a >= 0 and b >= 0:
                        visited.add(new)
                        queue.append(new)

    Lambda = (p, q)
    Lambda_rho_sq = inner((p+1, q+1), (p+1, q+1))
    all_weights[Lambda] = 1

    weight_list = sorted(all_weights.keys(), key=lambda w: -(w[0] + w[1]))

    for mu in weight_list:
        if mu == Lambda:
            continue
        mu_rho_sq = inner((mu[0]+1, mu[1]+1), (mu[0]+1, mu[1]+1))
        denom = Lambda_rho_sq - mu_rho_sq
        if abs(denom) < 1e-10:
            all_weights[mu] = 0
            continue
        numer = 0.0
        for alpha in pos_roots:
            k = 1
            while True:
                shifted = (mu[0] + k*alpha[0], mu[1] + k*alpha[1])
                if shifted in all_weights and all_weights[shifted] > 0:
                    numer += 2 * inner(shifted, alpha) * all_weights[shifted]
                    k += 1
                else:
                    break
        mult = numer / denom
        all_weights[mu] = max(0, int(round(mult)))

    return [(m1, m2, mult) for (m1, m2), mult in all_weights.items() if mult > 0]


def branch_su3(p, q):
    weights = su3_weights(p, q)
    y_groups = defaultdict(list)
    for m1, m2, mult in weights:
        Y = (m1 + 2*m2) / 3.0
        I3 = m1 / 2.0
        Y_key = round(Y * 9) / 9.0
        y_groups[Y_key].append((I3, mult))

    b_1 = 0.0
    b_2 = 0.0
    total_dim = 0

    for Y, states in y_groups.items():
        i3_mults = defaultdict(int)
        for i3, mult in states:
            i3_mults[i3] += mult

        remaining = dict(i3_mults)
        while any(v > 0 for v in remaining.values()):
            nonzero = [(i3, m) for i3, m in remaining.items() if m > 0]
            if not nonzero:
                break
            max_i3 = max(nonzero, key=lambda x: abs(x[0]))[0]
            j = abs(max_i3)

            valid = True
            for i3_2 in range(int(-2*j), int(2*j) + 1, 2):
                i3_val = i3_2 / 2.0
                if remaining.get(i3_val, 0) <= 0:
                    valid = False
                    break

            if not valid:
                remaining[max_i3] = 0
                continue

            for i3_2 in range(int(-2*j), int(2*j) + 1, 2):
                remaining[i3_2 / 2.0] -= 1

            dim_m = int(2*j + 1)
            b_1 += dim_m * Y**2
            b_2 += dim_m * j * (j + 1)
            total_dim += dim_m

    expected = (p+1)*(q+1)*(p+q+2)//2
    if total_dim != expected:
        print(f"  DIM MISMATCH ({p},{q}): {total_dim} vs {expected}")

    return b_1, b_2, b_1 - b_2


# ========== MAIN ==========
print("=== b_1/b_2 RATIO CHECK ===")
print(f"{'(p,q)':>8s} {'dim':>5s} {'b1':>10s} {'b2':>10s} {'b1/b2':>10s} {'Delta_b':>10s}")
print("-" * 55)

all_branching = {}
for pq_sum in range(7):
    for p in range(pq_sum + 1):
        q = pq_sum - p
        b1, b2, db = branch_su3(p, q)
        dim_pq = (p+1)*(q+1)*(p+q+2)//2
        ratio = b1/b2 if b2 > 0 else float("nan")
        all_branching[(p, q)] = {"b1": b1, "b2": b2, "Delta_b": db, "dim": dim_pq}
        print(f"({p},{q}):   {dim_pq:5d} {b1:10.4f} {b2:10.4f} {ratio:10.6f} {db:10.4f}")

# ========== T''(0) ==========
print()
print("=== T''(0) SIGN GATE ===")
d = np.load("tier0-computation/s19a_sweep_data.npz", allow_pickle=True)
tau_values = d["tau_values"]
dtau = 0.1

p_arr = d["sector_p_0"]
q_arr = d["sector_q_0"]
mults = d["multiplicities_0"]
n = len(p_arr)

lam = [np.abs(d[f"eigenvalues_{i}"]) for i in range(4)]

dlam = (-3*lam[0] + 4*lam[1] - lam[2]) / (2*dtau)
d2lam = (2*lam[0] - 5*lam[1] + 4*lam[2] - lam[3]) / (dtau**2)

delta_b = np.zeros(n)
for i in range(n):
    key = (int(p_arr[i]), int(q_arr[i]))
    if key in all_branching:
        delta_b[i] = all_branching[key]["Delta_b"]

safe = lam[0] > 1e-10
bracket = np.zeros(n)
bracket[safe] = d2lam[safe]/lam[0][safe] - (dlam[safe]/lam[0][safe])**2

integrand = delta_b * bracket
T_pp = np.sum(integrand) / (64 * np.pi**2)
T_pp_w = np.sum(integrand * mults) / (64 * np.pi**2)

print(f"T''(0) unweighted: {T_pp:.4f}")
print(f"T''(0) weighted:   {T_pp_w:.4f}")
print(f"Sign: {'POSITIVE' if T_pp > 0 else 'NEGATIVE'}")

# Bracket statistics
print(f"\nBracket stats (d2ln(lam)/dtau2):")
print(f"  Mean: {np.mean(bracket[safe]):.4f}")
print(f"  Positive: {np.sum(bracket[safe] > 0)}, Negative: {np.sum(bracket[safe] < 0)}")

# Sector breakdown
print("\nSector contributions:")
cum = 0
for pq_sum in range(7):
    for p in range(pq_sum + 1):
        q = pq_sum - p
        mask = (p_arr == p) & (q_arr == q)
        if mask.sum() == 0:
            continue
        c = np.sum(integrand[mask]) / (64 * np.pi**2)
        cum += c
        pct = c/T_pp*100 if abs(T_pp) > 0 else 0
        print(f"  ({p},{q}): {c:12.2f}  cum={cum:12.2f}  ({pct:5.1f}%)")

# ========== delta_T(tau) ==========
print()
print("=== delta_T(tau) ===")
delta_T_vals = []
for t_idx in range(len(tau_values)):
    tau = tau_values[t_idx]
    ev = np.abs(d[f"eigenvalues_{t_idx}"])
    safe_m = ev > 1e-15
    ln_lam_sq = np.zeros(n)
    ln_lam_sq[safe_m] = np.log(ev[safe_m]**2)
    dT = -np.sum(delta_b * ln_lam_sq) / (64 * np.pi**2 * np.exp(4*tau))
    delta_T_vals.append(dT)
    print(f"  tau={tau:.1f}: delta_T={dT:12.4f}")

delta_T_arr = np.array(delta_T_vals)
# Check for zero crossing
sign_changes = np.where(np.diff(np.sign(delta_T_arr)))[0]
if len(sign_changes) > 0:
    for sc in sign_changes:
        t1, t2 = tau_values[sc], tau_values[sc+1]
        d1, d2 = delta_T_arr[sc], delta_T_arr[sc+1]
        t_cross = t1 + (t2 - t1) * abs(d1) / (abs(d1) + abs(d2))
        print(f"\n  ZERO CROSSING at tau ~ {t_cross:.3f} (between {t1:.1f} and {t2:.1f})")
else:
    print(f"\n  No zero crossing. delta_T is {'positive' if delta_T_arr[0] > 0 else 'negative'} throughout.")

# ========== S_signed(tau) ==========
print()
print("=== S_signed(tau) ===")
S_signed = np.zeros(len(tau_values))
for t_idx in range(len(tau_values)):
    ev = np.abs(d[f"eigenvalues_{t_idx}"])
    safe_m = ev > 1e-15
    ln_lam_sq = np.zeros(n)
    ln_lam_sq[safe_m] = np.log(ev[safe_m]**2)
    S_signed[t_idx] = np.sum(delta_b * ln_lam_sq)

dS = np.diff(S_signed)
if np.all(dS <= 0):
    monotonic = "monotonic decreasing"
elif np.all(dS >= 0):
    monotonic = "monotonic increasing"
else:
    monotonic = "NON-MONOTONIC"

print(f"S_signed behavior: {monotonic}")
print(f"S_signed(0) = {S_signed[0]:.2f}, S_signed(2) = {S_signed[-1]:.2f}")
min_idx = np.argmin(S_signed)
print(f"Min at tau={tau_values[min_idx]:.1f}, value={S_signed[min_idx]:.2f}")

# Save results
np.savez("tier0-computation/s21c_S_signed.npz",
         tau_values=tau_values, S_signed=S_signed,
         delta_b_by_eigenvalue=delta_b, verdict=monotonic)

print("\n=== SUMMARY ===")
print(f"b_1/b_2 ratio: check table above")
print(f"T''(0) = {T_pp:.4f} ({'POSITIVE' if T_pp > 0 else 'NEGATIVE'})")
print(f"S_signed: {monotonic}")
print(f"delta_T: {'zero crossing found' if len(sign_changes) > 0 else 'no crossing'}")
