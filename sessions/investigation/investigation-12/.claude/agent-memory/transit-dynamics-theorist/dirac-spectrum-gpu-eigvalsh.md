---
name: dirac-spectrum-gpu-eigvalsh
description: GPU diagonalization of D_K blocks on this ROCm build requires eigvalsh on i*D (Hermitian), NOT eigvals (needs MAGMA, absent)
metadata:
  type: reference
---

On the AMD RX 9070 XT / ROCm `torch 2.9.1+rocm` build in this project, `torch.linalg.eigvals` (the GENERAL non-Hermitian eig) raises `RuntimeError: Calling torch.linalg.eig on a CUDA tensor requires compiling PyTorch with MAGMA`. This build lacks MAGMA. Only the Hermitian routine `torch.linalg.eigvalsh` is GPU-native.

**Fix for D_K blocks:** `D_K` (from `dirac_operator_on_irrep`) is ANTI-Hermitian by construction (math convention, no factor of i — see `dirac_spectrum.py` docstring lines ~1242-1244; eigenvalues purely imaginary). Therefore `H = i*D_K` is exactly Hermitian (residual 0-4e-16) with REAL eigenvalues equal to `imag(eig(D_K))`. Diagonalize on GPU via:
```python
H = 1j * D
ev = torch.linalg.eigvalsh(torch.tensor(H, device='cuda')).cpu().numpy()  # REAL
spectrum = np.sort(np.abs(ev))   # the |lambda_k| set
```
Verified `== numpy |eigvals(D).imag|` to 1e-14 across blocks dim 128/432/1024 (INV12-W3-1 pre-flight). This is both MAGMA-free AND numerically superior (exploits Hermiticity, no spurious imaginary leakage) and faster than the general eig.

**Benign stderr banner:** running the venv python emits `Ainulindale: Unknown command line argument '...offload-arch.exe'` — a ROCm-SDK init artifact from the SPACE in the project path; harmless, `torch.cuda.is_available()` still returns True.

Used by [[relic-spectrum-bdg-dispersion]] for the per-(p,q)-block lambda_k(tau) trajectory construction.
