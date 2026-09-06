# 📦 Python Modules — Quick Reference

*Definition → Syntax → Example, for fast revision.*

---

## Importing

Reuse code from another file (built-in, third-party, or your own).
```python
import module_name
```
```python
import math
math.sqrt(16)   # 4.0
```

## Import Variations

| Style | Syntax | Example |
|---|---|---|
| Alias | `import x as y` | `import numpy as np` |
| Specific items | `from x import y` | `from math import sqrt` |
| Everything (avoid) | `from x import *` | pollutes namespace |

```python
from math import sqrt, pi
sqrt(16)      # no prefix needed
```

---

## Your Own Module

Any `.py` file is importable as a module.
```python
# mymath.py
def add(a, b):
    return a + b
```
```python
# main.py
import mymath
mymath.add(2, 3)   # 5
```

## `if __name__ == "__main__"`

Runs code only when the file is executed directly, not when imported.
```python
if __name__ == "__main__":
    # test/demo code here
```
```python
# mymath.py
if __name__ == "__main__":
    print(add(2, 3))   # only runs via `python mymath.py`
```

---

## Packages

A folder of modules, marked with `__init__.py`.
```
mypackage/
├── __init__.py
└── math_utils.py
```
```python
from mypackage import math_utils
math_utils.add(2, 3)
```

---

## Useful Built-in Modules

| Module | Purpose | Example |
|---|---|---|
| `math` | math functions | `math.sqrt(9)` |
| `random` | random values | `random.randint(1, 10)` |
| `os` | files/paths/env | `os.getcwd()` |
| `datetime` | dates & times | `datetime.now()` |
| `json` | read/write JSON | `json.load(file)` |

---

## Third-Party Modules

Installed via `pip`, not built into Python.
```bash
pip install requests
```
```python
import requests
requests.get("https://api.github.com")
```

## Virtual Environments

Keeps each project's packages isolated.
```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install requests
deactivate
```

---

## `dir()` and `help()`

Inspect what a module offers.
```python
dir(math)        # list everything in the module
help(math.sqrt)  # docs for a specific function
```

---

## Quick Import Cheatsheet

| Situation | Use |
|---|---|
| Need the whole module | `import module` |
| Long/common name | `import module as alias` |
| Only need 1–2 things | `from module import x` |
| Never | `from module import *` |
