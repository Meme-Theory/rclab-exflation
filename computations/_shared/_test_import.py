import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
try:
    from canonical_constants import Omega_m, Omega_Lambda, sigma_8
    with open('_test_ok.txt', 'w') as f:
        f.write(f"OK: Omega_m={Omega_m}, Omega_L={Omega_Lambda}, sig8={sigma_8}\n")
except Exception as e:
    with open('_test_ok.txt', 'w') as f:
        f.write(f"FAIL: {e}\n")
