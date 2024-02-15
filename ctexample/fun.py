from pathlib import Path
import ctypes


# Load the shared library
parent_dir = Path(__file__).parent
libfun = ctypes.CDLL(str(parent_dir / "library" / "libfun.so"))


def fun(x):
    return libfun.fun(x)
