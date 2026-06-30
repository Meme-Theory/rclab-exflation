---
paths:
  - "computations/_shared/**"
  - "phonon-exflation-sim/**"
  - "*.py"
---

# Computation Environment

## Hardware
- **CPU**: AMD Ryzen 32-core
- **RAM**: 128GB
- **GPU**: AMD Radeon RX 9070 XT (17.1 GB VRAM, ROCm 7.2)
- **OS**: Windows 11 (MINGW64/Git Bash)

## Python Environment

**ALWAYS use the GPU-enabled venv for ALL scripts** — there is no reason to use the CPU-only system Python.

- **Python**: 3.12 (`phonon-exflation-sim/.venv312/`)
- **Torch**: 2.9.1+rocmsdk20260116 (**GPU ACTIVE**: RX 9070 XT, 17.1 GB VRAM)
- **Invoke**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" script.py`
- **Use for**: EVERYTHING — computations, GPE simulation, GPU work, all scripts

### Key Packages (both environments have numpy/scipy/matplotlib):

| Package | System (CPU) | Venv (GPU) | Used By |
|:--------|:-------------|:-----------|:--------|
| numpy | 2.4.1 | installed | Everything |
| scipy | 1.17.0 | installed | Eigenvalue solvers |
| matplotlib | 3.10.8 | installed | Plotting |
| h5py | 3.15.1 | installed | Simulation data I/O |
| pyFFTW | 0.15.1 | installed | FFT-based GPE solver (32 threads) |
| numexpr | 2.14.1 | installed | Fast array expressions |
| torch | 2.10.0+cpu | **2.9.1+rocm** | GPU compute via venv only |

## Running Scripts
- **ALL scripts**: Use the venv Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe" script.py`
- The RX 9070 XT has 17 GB VRAM — eigenvalue sweeps, Pfaffian computations, spectral action scans all benefit from GPU.
- **Typical runtime**: ~8.7s per $s$-value at `max_pq_sum=6` for Dirac spectrum. ~25 sps at 1024x1024 for GPE simulation.

## Heavy Linear Algebra — Prefer GPU (MANDATORY)

Compute-mode agents default to `numpy.linalg` out of training bias. On this machine it is the wrong default. For matrices ≥ 100×100:

- **Eigvals / SVD / matrix products**: use `torch.linalg.eigvals`, `torch.linalg.svd`, `torch.matmul` on ROCm.
- **FFTs**: use `torch.fft`.
- **Pattern**:
  ```python
  import torch
  t = torch.tensor(M, device='cuda')          # ship to GPU
  evals = torch.linalg.eigvals(t).cpu().numpy()  # compute, bring back
  ```
- **Why**: `numpy.linalg.eigvals` threads across 32 CPU cores; when two compute-mode agents run in parallel they contend and each takes ~2× wall time. A 400×400 eigvals on GPU runs in tens of milliseconds vs ~15 s on CPU.
- **Validation**: for first use in a script, cross-check the first few eigenvalues against `numpy.linalg.eigvals` on a small test matrix to catch any numerics surprises.

## CPU Thread Cap When GPU Not Used

If an operation is truly CPU-only (small matrices, iterative solvers without GPU support, legacy scipy paths), cap threads to avoid contention with other concurrent agents:

```python
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')
# … then:
import numpy as np
```

Set **before** `import numpy` — numpy reads these env vars at import time, not at call time.
