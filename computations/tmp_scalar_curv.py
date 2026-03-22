import numpy as np

f_abc_list = [
    (1,2,3, 1.0),
    (1,4,7, 0.5), (1,5,6, -0.5),
    (2,4,6, 0.5), (2,5,7, 0.5),
    (3,4,5, 0.5), (3,6,7, -0.5),
    (4,5,8, np.sqrt(3)/2), (6,7,8, np.sqrt(3)/2),
]
f_dict = {}
for a,b,c,v in f_abc_list:
    f_dict[(a,b,c)] = v

def get_f(a,b,c):
    for (i,j,k), sign in [((a,b,c),1), ((b,c,a),1), ((c,a,b),1),
                           ((b,a,c),-1), ((a,c,b),-1), ((c,b,a),-1)]:
        if (i,j,k) in f_dict:
            return sign * f_dict[(i,j,k)]
    return 0.0

def blk(a):
    if a == 8: return 0
    elif a <= 3: return 1
    else: return 2

def scalar_curvature_LC(L1, L2, L3):
    Ls = [L1, L2, L3]
    N = 9  # indices 1..8

    # Structure constants in ONB: C^c_{ab} = -f_{abc} * sqrt(2*Lc/(La*Lb))
    C = np.zeros((N,N,N))
    for a in range(1,N):
        La = Ls[blk(a)]
        for b in range(1,N):
            Lb = Ls[blk(b)]
            for c in range(1,N):
                Lc = Ls[blk(c)]
                fv = get_f(a,b,c)
                if abs(fv) > 1e-15:
                    C[c,a,b] = -fv * np.sqrt(2*Lc/(La*Lb))

    # Levi-Civita connection: Gam^c_{ab} = (1/2)(C^c_{ab} + C^a_{cb} + C^b_{ca})
    # Using Koszul formula for left-invariant metric on Lie group
    Gam = np.zeros((N,N,N))
    for c in range(1,N):
        for a in range(1,N):
            for b in range(1,N):
                Gam[c,a,b] = 0.5*(C[c,a,b] + C[a,c,b] + C[b,c,a])

    # Verify torsion-free: Gam^c_{ab} - Gam^c_{ba} = C^c_{ab}
    max_torsion_err = 0
    for c in range(1,N):
        for a in range(1,N):
            for b in range(1,N):
                err = abs((Gam[c,a,b] - Gam[c,b,a]) - C[c,a,b])
                max_torsion_err = max(max_torsion_err, err)
    print(f"Torsion-free check: max error = {max_torsion_err:.2e}")

    # Riemann tensor (for left-invariant fields, partial derivatives vanish):
    # R^f_{abc} = sum_d (Gam^f_{ad} Gam^d_{bc} - Gam^f_{bd} Gam^d_{ac} - C^d_{ab} Gam^f_{dc})
    # Ricci: Ric_{ac} = sum_b R^b_{abc} = sum_{b,d} (Gam^b_{ad} Gam^d_{bc} - Gam^b_{bd} Gam^d_{ac} - C^d_{ab} Gam^b_{dc})
    # R = sum_a Ric_{aa}

    R_val = 0.0
    for a in range(1,N):
        for b in range(1,N):
            for d in range(1,N):
                R_val += (Gam[b,a,d]*Gam[d,b,a]
                         - Gam[b,b,d]*Gam[d,a,a]
                         - C[d,a,b]*Gam[b,d,a])
    return R_val

def R_3_70(s):
    return 1.5 * (2*np.exp(2*s) - 1 + 8*(np.exp(-s) - np.exp(-4*s)))

print("=== Levi-Civita curvature vs eq 3.70 ===")
for s in [0.0, 0.1, 0.15, 0.2, 0.35, 0.5]:
    L1, L2, L3 = np.exp(2*s), np.exp(-2*s), np.exp(s)
    rm = scalar_curvature_LC(L1, L2, L3)
    r70 = R_3_70(s)
    ratio = rm/r70 if abs(r70) > 1e-10 else 0
    print(f"s={s:.2f}: R_LC={rm:10.4f}  R_3.70={r70:10.4f}  ratio={ratio:.6f}")

# Check bi-invariant at different kappa
print("\n=== Bi-invariant at various kappa ===")
for kappa in [1, 2, 4, 8, 10]:
    R = scalar_curvature_LC(kappa, kappa, kappa)
    print(f"kappa={kappa}: R = {R:.6f}")

# Also try the prompt formula
print("\n=== Prompt formula ===")
def R_prompt(L1, L2, L3):
    return 1.0/(2*L2) + 1.0/L3 - L2/(4*L3**2) - L1/(2*L3**2)

for s in [0.0, 0.1, 0.35, 0.5]:
    L1, L2, L3 = np.exp(2*s), np.exp(-2*s), np.exp(s)
    print(f"s={s:.2f}: R_prompt={R_prompt(L1,L2,L3):.6f}, R_LC={scalar_curvature_LC(L1,L2,L3):.6f}, R_3.70={R_3_70(s):.6f}")
