# Example code using ctypes

## Introduction

This repository shows:
- how to write a C function
- how to compile it to a shared library `*.so`
- how to call it from Python using `ctypes`

Follow the below steps to run the demo.

## Compilation of C code
```
make libfun.so
```
The shared library will be saved in `ctexample/library`.
It is called from the Python function `fun(x)`
defined in the module `ctexample.fun` (`ctexample/fun.py`).

## Installation of Python package

Create a virtual environment. The below example uses `venv`:
```
git clone https://github.com/krzysztofarendt/ctypes-example
cd ctypes-example
python3.10 -m venv venv
source venv/bin/activate
```
Other programs for virtual environments are e.g. `virtualenv`, `conda`.

Install the package:
```
pip instal -e .
```

## Call C function from Python

Run the below module:
```
python ctexample/fun.py
```

or type the following in the Python console:
```python
from ctexample import fun
fun(5, 5, 20)  # (5 + 5 + 20) / 3 = 10
```
