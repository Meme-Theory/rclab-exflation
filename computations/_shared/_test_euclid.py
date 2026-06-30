import sys
sys.path.insert(0, 'computations')
import traceback
try:
    import numpy as np
    from canonical_constants import (
        T_acoustic, E_cond, E_B1, E_B2_mean, E_B3_mean,
        PI, N_dof_BCS, E_exc, n_pairs, tau_fold,
        omega_PV, Delta_0_GL, S_inst, omega_att,
        E_cond_ED_8mode, J_C2, N_cells, M_KK
    )
    with open('computations/_shared/_test_euclid_ok.txt','w') as f:
        f.write(f'IMPORTS OK\n')
        f.write(f'T_acoustic={T_acoustic}\n')
        f.write(f'E_B1={E_B1}\n')
        f.write(f'E_B2_mean={E_B2_mean}\n')
        f.write(f'E_B3_mean={E_B3_mean}\n')
        f.write(f'N_cells={N_cells}\n')

    vp = np.load('computations/session-58/s58_volovik_partition.npz', allow_pickle=True)
    F_J = float(vp['F_Josephson'])
    E_m = float(vp['E_matter_Volovik'])
    with open('computations/_shared/_test_euclid_ok.txt','a') as f:
        f.write(f'NPZ LOAD OK: F_J={F_J}, E_m={E_m}\n')
        f.write('ALL GOOD\n')
except Exception as e:
    with open('computations/_shared/_test_euclid_ok.txt','w') as f:
        f.write(f'ERROR: {e}\n')
        f.write(traceback.format_exc())
