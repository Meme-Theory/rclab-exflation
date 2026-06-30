import numpy as np
d = np.load('computations/session-59/s59_neff_ba.npz', allow_pickle=True)
f = open('computations/session-59/s59_neff_read.txt', 'w')
for k in ['Delta_N_eff_conservative', 'Delta_N_eff_aggressive', 'g_BA_conservative',
           'g_BA_aggressive', 'gate_verdict', 'gate_detail', 'dilution_factor_CMB',
           'rho_1nu_over_rho_gamma', 'F_BA', 'E_matter_Volovik', 'M_KK',
           'g_star_Shattering', 'g_star_S_post_ee', 'g_star_S_Shattering',
           'N_eff_Planck_2018', 'sigma_N_eff_Planck_2018', 'n_BA_modes']:
    v = d[k]
    f.write(f'{k} = {v.item() if v.ndim == 0 else v}\n')
f.close()
