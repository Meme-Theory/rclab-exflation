"""
Compute backend abstraction layer.

Priority order:
  1. PyTorch (NVIDIA/AMD GPU via CUDA/ROCm) -- if available
  2. CuPy (NVIDIA GPU) -- if available and GPU works
  3. pyfftw (multithreaded FFTW) -- fastest CPU FFT
  4. scipy.fft with workers=-1 -- decent multithreading
  5. numpy.fft -- single-threaded fallback

Override with EXFLATION_GPU=off to skip GPU detection.
Override with EXFLATION_BACKEND=torch|cupy to force a specific GPU backend.
Override FFT thread count with EXFLATION_FFT_THREADS (default: all cores).

Usage:
    from src.backend import xp, fft, to_numpy, ensure_array, synchronize, BACKEND_NAME
"""

import os
import numpy as np
import numpy.fft as _npfft

BACKEND_NAME = "numpy"
FFT_BACKEND = "numpy"
_fft_threads = int(os.environ.get("EXFLATION_FFT_THREADS", "0")) or os.cpu_count()

xp = np
fft = _npfft

# --- GPU backend selection ---
_gpu_env = os.environ.get("EXFLATION_GPU", "on").lower()
_backend_pref = os.environ.get("EXFLATION_BACKEND", "").lower()

# --- Try PyTorch GPU (NVIDIA + AMD ROCm) ---
if (_gpu_env not in ("off", "0", "false", "no")
        and _backend_pref not in ("cupy", "numpy", "cpu")):
    try:
        import torch as _torch
        if _torch.cuda.is_available():
            _torch_device = _torch.device('cuda')

            def _to_torch_dtype(dtype):
                """Map Python/NumPy dtypes to PyTorch equivalents."""
                if dtype is None:
                    return None
                if dtype is complex or dtype == np.complex128:
                    return _torch.complex128
                if dtype is float or dtype == np.float64:
                    return _torch.float64
                if dtype is int or dtype == np.int64:
                    return _torch.int64
                if dtype == np.complex64:
                    return _torch.complex64
                if dtype == np.float32:
                    return _torch.float32
                return None

            class _TorchXP:
                """PyTorch drop-in namespace mimicking numpy array operations."""

                def __init__(self, device):
                    self._device = device

                def abs(self, x):
                    return _torch.abs(x)

                def angle(self, x):
                    return _torch.angle(x)

                def exp(self, x):
                    return _torch.exp(x)

                def sqrt(self, x):
                    if not isinstance(x, _torch.Tensor):
                        x = _torch.tensor(x, device=self._device,
                                          dtype=_torch.float64)
                    return _torch.sqrt(x)

                def sum(self, x, axis=None):
                    if axis is None:
                        return _torch.sum(x)
                    return _torch.sum(x, dim=axis)

                def real(self, x):
                    return _torch.real(x)

                def round(self, x):
                    return _torch.round(x)

                def max(self, x):
                    return _torch.max(x)

                def roll(self, x, shift, axis=None):
                    if axis is None:
                        return _torch.roll(x, shift)
                    return _torch.roll(x, shift, dims=axis)

                def bincount(self, x, weights=None, minlength=0):
                    return _torch.bincount(x, weights=weights,
                                           minlength=minlength)

                def ones(self, shape, dtype=None):
                    return _torch.ones(shape, device=self._device,
                                       dtype=_to_torch_dtype(dtype))

                def linspace(self, start, stop, num, endpoint=True, dtype=None):
                    td = _to_torch_dtype(dtype) or _torch.float64
                    if endpoint:
                        return _torch.linspace(start, stop, num,
                                               device=self._device, dtype=td)
                    step = (stop - start) / num
                    return (_torch.arange(num, device=self._device, dtype=td)
                            * step + start)

                def meshgrid(self, *tensors, indexing='xy'):
                    return _torch.meshgrid(*tensors, indexing=indexing)

            class _TorchFFT:
                """PyTorch FFT drop-in mimicking numpy.fft interface."""

                def __init__(self, device):
                    self._device = device

                def fft2(self, x, *args, **kwargs):
                    return _torch.fft.fft2(x, *args, **kwargs)

                def ifft2(self, x, *args, **kwargs):
                    return _torch.fft.ifft2(x, *args, **kwargs)

                def fft(self, x, *args, **kwargs):
                    return _torch.fft.fft(x, *args, **kwargs)

                def ifft(self, x, *args, **kwargs):
                    return _torch.fft.ifft(x, *args, **kwargs)

                def fftfreq(self, n, d=1.0):
                    return _torch.fft.fftfreq(n, d=d, device=self._device,
                                              dtype=_torch.float64)

            # Smoke test
            _test = _torch.tensor([1.0, 2.0], device=_torch_device)
            assert float(_torch.sum(_test)) == 3.0
            del _test

            # Disable autograd -- not needed for numerical simulation
            _torch.set_grad_enabled(False)

            xp = _TorchXP(_torch_device)
            fft = _TorchFFT(_torch_device)
            BACKEND_NAME = "torch"
            _gpu_name = _torch.cuda.get_device_name()
            FFT_BACKEND = f"torch.fft ({_gpu_name})"
    except Exception:
        pass

# --- Try CuPy (NVIDIA GPU) ---
if (BACKEND_NAME == "numpy"
        and _gpu_env not in ("off", "0", "false", "no")
        and _backend_pref not in ("torch", "numpy", "cpu")):
    try:
        import cupy as _cp
        import cupy.fft as _cpfft
        _test = _cp.array([1.0, 2.0])
        assert float(_cp.sum(_test)) == 3.0
        del _test
        xp = _cp
        fft = _cpfft
        BACKEND_NAME = "cupy"
        FFT_BACKEND = "cupy"
    except Exception:
        pass

# --- If no GPU, find best CPU FFT ---
if BACKEND_NAME == "numpy":
    try:
        import pyfftw
        import pyfftw.interfaces.numpy_fft as _pyfftw_fft
        pyfftw.interfaces.cache.enable()

        class _PyfftwFFT:
            """pyfftw drop-in for numpy.fft with automatic multithreading."""
            def __init__(self, threads):
                self._threads = threads
                self._mod = _pyfftw_fft

            def fft2(self, a, *args, **kwargs):
                kwargs.setdefault('threads', self._threads)
                return self._mod.fft2(a, *args, **kwargs)

            def ifft2(self, a, *args, **kwargs):
                kwargs.setdefault('threads', self._threads)
                return self._mod.ifft2(a, *args, **kwargs)

            def fftfreq(self, n, d=1.0):
                return np.fft.fftfreq(n, d=d)

            def fft(self, a, *args, **kwargs):
                kwargs.setdefault('threads', self._threads)
                return self._mod.fft(a, *args, **kwargs)

            def ifft(self, a, *args, **kwargs):
                kwargs.setdefault('threads', self._threads)
                return self._mod.ifft(a, *args, **kwargs)

        fft = _PyfftwFFT(threads=_fft_threads)
        FFT_BACKEND = f"pyfftw ({_fft_threads} threads)"
    except ImportError:
        try:
            import scipy.fft as _spfft

            class _ScipyFFT:
                """scipy.fft drop-in with automatic workers=-1."""
                def __init__(self, workers):
                    self._workers = workers
                    self._mod = _spfft

                def fft2(self, a, *args, **kwargs):
                    kwargs.setdefault('workers', self._workers)
                    return self._mod.fft2(a, *args, **kwargs)

                def ifft2(self, a, *args, **kwargs):
                    kwargs.setdefault('workers', self._workers)
                    return self._mod.ifft2(a, *args, **kwargs)

                def fftfreq(self, n, d=1.0):
                    return self._mod.fftfreq(n, d=d)

                def fft(self, a, *args, **kwargs):
                    kwargs.setdefault('workers', self._workers)
                    return self._mod.fft(a, *args, **kwargs)

                def ifft(self, a, *args, **kwargs):
                    kwargs.setdefault('workers', self._workers)
                    return self._mod.ifft(a, *args, **kwargs)

            fft = _ScipyFFT(workers=-1)
            FFT_BACKEND = f"scipy.fft ({_fft_threads} threads)"
        except ImportError:
            FFT_BACKEND = "numpy (single-threaded)"


def to_numpy(arr):
    """Transfer array to CPU (NumPy). No-op if already NumPy."""
    if BACKEND_NAME == "torch":
        import torch
        if isinstance(arr, torch.Tensor):
            return arr.detach().cpu().numpy()
    elif BACKEND_NAME == "cupy":
        import cupy
        if isinstance(arr, cupy.ndarray):
            return arr.get()
    return np.asarray(arr)


def ensure_array(arr):
    """Transfer array to active backend (GPU if available, else no-op)."""
    if BACKEND_NAME == "torch":
        import torch
        if not isinstance(arr, torch.Tensor):
            return torch.as_tensor(np.asarray(arr), device=_torch_device)
        return arr.to(_torch_device)
    elif BACKEND_NAME == "cupy":
        import cupy
        if not isinstance(arr, cupy.ndarray):
            return cupy.asarray(arr)
        return arr
    return np.asarray(arr)


def synchronize():
    """Synchronize GPU stream for accurate timing. No-op on CPU."""
    if BACKEND_NAME == "torch":
        import torch
        torch.cuda.synchronize()
    elif BACKEND_NAME == "cupy":
        import cupy
        cupy.cuda.Stream.null.synchronize()


def as_int(arr):
    """Convert array elements to integer type (backend-agnostic)."""
    if BACKEND_NAME == "torch":
        import torch
        return arr.to(torch.int64)
    return arr.astype(int)


def clone(arr):
    """Copy/clone an array (backend-agnostic)."""
    if BACKEND_NAME == "torch":
        return arr.clone()
    return arr.copy()
