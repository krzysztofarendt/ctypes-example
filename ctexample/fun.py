from pathlib import Path
import ctypes


# Load the shared library
parent_dir = Path(__file__).parent
libfun = ctypes.CDLL(str(parent_dir / "library" / "libfun.so"))

class Obj(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int * 3),
        ("y", ctypes.c_int),
    ]

libfun.fun.argtypes = [ctypes.POINTER(Obj)]
libfun.fun.restype = None

def fun(x1, x2, x3):
    int3 = ctypes.c_int * 3
    inp = Obj(
        int3(x1, x2, x3),
        ctypes.c_int(0),
    )
    libfun.fun(inp)
    return inp.y


if __name__ == "__main__":
    y = fun(5, 5, 20)  # Should return 10, because (5 + 5 + 20) / 3 = 10
    print(y)
