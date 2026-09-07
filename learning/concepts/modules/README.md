# 📦 Modules in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Modules-orange)
![Status](https://img.shields.io/badge/Status-Learning-brightgreen)

> Notes and examples covering Python modules — built-in, third-party, and your own — from basics to packaging.

---

## 📑 Table of Contents
- [What is a Module?](#-what-is-a-module)
- [1. Importing a Module](#1-importing-a-module)
- [2. Import Variations](#2-import-variations)
- [3. Creating Your Own Module](#3-creating-your-own-module)
- [4. `if __name__ == "__main__"`](#4-if-__name__--__main__)
- [5. Packages (Folders of Modules)](#5-packages-folders-of-modules)
- [6. Useful Built-in Modules](#6-useful-built-in-modules)
- [7. Third-Party Modules (pip)](#7-third-party-modules-pip)
- [8. Virtual Environments](#8-virtual-environments)
- [9. `dir()` and `help()`](#9-dir-and-help)
- [Common Pitfalls](#-common-pitfalls)

---

## 💡 What is a Module?

A module is just a **`.py` file** containing code (functions, classes, variables) that you can reuse in other files by importing it. Python itself comes with many built-in modules (`math`, `os`, `random`, etc.).

---

## 1. Importing a Module

```python
import math

print(math.sqrt(16))    # 4.0
print(math.pi)           # 3.14159...
```

---

## 2. Import Variations

```python
# Import the whole module
import math
math.sqrt(16)

# Import with an alias (common for long names)
import numpy as np
np.array([1, 2, 3])

# Import specific things only
from math import sqrt, pi
sqrt(16)     # no need for math. prefix

# Import everything (⚠️ avoid — pollutes namespace, unclear origins)
from math import *
```

| Style | When to use |
|---|---|
| `import module` | Default, clearest — shows where functions come from |
| `import module as alias` | Long/common module names (`pandas as pd`) |
| `from module import x` | Only need one or two specific things |
| `from module import *` | Avoid — makes code hard to read/debug |

---

## 3. Creating Your Own Module

**`mymath.py`**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159
```

**`main.py`** (same folder)
```python
import mymath

print(mymath.add(2, 3))       # 5
print(mymath.PI)              # 3.14159
```

> 🔹 Any `.py` file can be imported as a module, as long as it's in the same folder (or Python's search path).

---

## 4. `if __name__ == "__main__"`

Lets a file behave differently depending on whether it's **run directly** or **imported**.

**`mymath.py`**
```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    # only runs when this file is executed directly
    print("Testing:", add(2, 3))
```

- Run `python mymath.py` → prints `Testing: 5`
- `import mymath` from another file → the test line does **not** run

> 🔹 This is the standard way to add test code or a "demo" to a module without it running every time someone imports it.

---

## 5. Packages (Folders of Modules)

A package is a folder containing multiple modules, with an `__init__.py` file (can be empty) marking it as a package.

```
mypackage/
├── __init__.py
├── math_utils.py
└── string_utils.py
```

```python
from mypackage import math_utils
math_utils.add(2, 3)

# or
from mypackage.math_utils import add
add(2, 3)
```

---

## 6. Useful Built-in Modules

| Module | Purpose | Example |
|---|---|---|
| `math` | Math functions/constants | `math.sqrt(9)`, `math.pi` |
| `random` | Random values | `random.randint(1, 10)`, `random.choice(list)` |
| `os` | OS-level operations (files, paths, env) | `os.getcwd()`, `os.listdir()` |
| `sys` | Interpreter/system info | `sys.argv`, `sys.exit()` |
| `datetime` | Dates and times | `datetime.now()` |
| `json` | Read/write JSON data | `json.load(file)`, `json.dumps(data)` |
| `time` | Time-related functions | `time.sleep(2)` |
| `re` | Regular expressions | `re.match(pattern, text)` |

```python
import random
print(random.randint(1, 100))     # random number between 1-100
print(random.choice(["a", "b", "c"]))  # random pick from a list
```

---

## 7. Third-Party Modules (pip)

Modules not built into Python — installed separately.

```bash
pip install requests
```

```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

> 🔹 Third-party modules are listed in a project's `requirements.txt` so others can install the same dependencies:
> ```bash
> pip freeze > requirements.txt
> pip install -r requirements.txt
> ```

---

## 8. Virtual Environments

Keeps each project's installed packages isolated from others.

```bash
python -m venv venv          # create a virtual environment
venv\Scripts\activate         # activate (Windows)
source venv/bin/activate      # activate (Mac/Linux)
pip install requests          # installs only inside this environment
deactivate                    # exit the environment
```

> 🔹 Prevents version conflicts between projects that need different versions of the same package.

---

## 9. `dir()` and `help()`

```python
import math

print(dir(math))     # lists everything available in the module
help(math.sqrt)       # shows documentation for a specific function
```

---

## ⚠️ Common Pitfalls

- **Naming your own file the same as a built-in module** (e.g. `random.py`) — Python imports *your* file instead of the built-in one, causing confusing errors.
- **`from module import *`** — makes it unclear where a function came from, and can silently override existing names.
- **Circular imports** — two modules importing each other directly can cause `ImportError`. Restructure code to avoid the cycle.
- **Forgetting `__init__.py`** in older Python versions — needed to mark a folder as a package (optional in Python 3.3+, but still common practice).
- **Running a script from the wrong folder** — relative imports can fail if you're not running from the expected working directory.

---

<p align="center">📁 Part of <b>python/basic/concepts</b></p>
