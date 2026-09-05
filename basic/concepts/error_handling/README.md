# ⚠️ Error Handling in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Error%20Handling-orange)
![Status](https://img.shields.io/badge/Status-Learning-brightgreen)

> Notes and examples covering how Python handles errors gracefully instead of crashing — from basics to advanced patterns.

---

## 📑 Table of Contents
- [What is Error Handling?](#-what-is-error-handling)
- [1. Basic try/except](#1-basic-tryexcept)
- [2. Catching Specific Errors](#2-catching-specific-errors)
- [3. Catching Multiple Errors](#3-catching-multiple-errors-in-one-block)
- [4. else Block](#4-else--runs-only-if-no-error-happened)
- [5. finally Block](#5-finally--always-runs-no-matter-what)
- [6. Exception Hierarchy](#6-exception-hierarchy)
- [7. raise Keyword](#7-raise--trigger-an-error-on-purpose)
- [8. Exception Chaining](#8-exception-chaining-raise--from-e)
- [9. Custom Exceptions](#9-custom-exceptions)
- [10. EAFP vs LBYL](#10-eafp-vs-lbyl-python-philosophy)
- [Common Built-in Exceptions](#-common-built-in-exceptions)

---

## 💡 What is Error Handling?

Error handling lets a program respond to problems (missing files, wrong input, dividing by zero) **instead of crashing**. Python does this with `try`, `except`, `else`, `finally`, and `raise`.

---

## 1. Basic try/except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
```

> 🔹 Code in `try` runs first. If it fails, Python jumps to the matching `except` block instead of crashing.

---

## 2. Catching Specific Errors

```python
try:
    value = int("abc")
except ValueError:
    print("That's not a valid number")
except TypeError:
    print("Wrong type used")
```

> 🔹 Order matters — Python checks top to bottom and stops at the **first match**. Always list specific errors before general ones.

---

## 3. Catching Multiple Errors in One Block

```python
try:
    risky()
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```

---

## 4. else — Runs Only If No Error Happened

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", x)
```

---

## 5. finally — Always Runs, No Matter What

```python
try:
    return "from try"
finally:
    print("cleanup happens here")
```

> 🔹 Used for cleanup: closing files, releasing connections, etc. Runs even if the `try` block returns early.

---

## 6. Exception Hierarchy

All exceptions inherit from `BaseException` → `Exception`. Catching a **parent** catches its **children** too.

```
Exception
 ├── ArithmeticError
 │     └── ZeroDivisionError
 ├── LookupError
 │     ├── IndexError
 │     └── KeyError
 ├── ValueError
 └── TypeError
```

```python
except ArithmeticError:   # also catches ZeroDivisionError
```

---

## 7. raise — Trigger an Error on Purpose

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
```

---

## 8. Exception Chaining (raise ... from e)

```python
try:
    prices["mango"]
except KeyError as e:
    raise ValueError("mango is not sold here") from e
```

> 🔹 Wraps a low-level error into a clearer, more meaningful one — while keeping the original visible in the traceback for debugging.

---

## 9. Custom Exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Tried to withdraw {amount}, only {balance} available")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
```

> 🔹 Custom exceptions can carry **structured data**, not just a message.

---

## 10. EAFP vs LBYL (Python Philosophy)

Python prefers **"Easier to Ask Forgiveness than Permission"**:

```python
# ✅ EAFP (Pythonic)
try:
    value = my_dict["key"]
except KeyError:
    value = "default"

# ⚠️ LBYL (less Pythonic)
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = "default"
```

---

## 📋 Common Built-in Exceptions

| Exception | When It Happens |
|---|---|
| `ValueError` | Right type, wrong value (e.g. `int("abc")`) |
| `TypeError` | Wrong type used in an operation |
| `ZeroDivisionError` | Dividing by zero |
| `FileNotFoundError` | File doesn't exist |
| `KeyError` | Missing dictionary key |
| `IndexError` | List index out of range |

---

<p align="center">📁 Part of <b>python/basic/concepts</b></p>
