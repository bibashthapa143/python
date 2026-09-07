# 🧩 Functions in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Functions-orange)
![Status](https://img.shields.io/badge/Status-Learning-brightgreen)

> Notes and examples covering Python functions — from basics to default parameters, `*args`, `**kwargs`, and advanced patterns.

---

## 📑 Table of Contents
- [What is a Function?](#-what-is-a-function)
- [1. Basic Function](#1-basic-function)
- [2. Parameters vs Arguments](#2-parameters-vs-arguments)
- [3. Return Values](#3-return-values)
- [4. Default Parameters](#4-default-parameters)
- [5. Positional vs Keyword Arguments](#5-positional-vs-keyword-arguments)
- [6. *args — Flexible Positional Arguments](#6-args--flexible-positional-arguments)
- [7. **kwargs — Flexible Keyword Arguments](#7-kwargs--flexible-keyword-arguments)
- [8. Combining Everything](#8-combining-everything)
- [9. Unpacking with * and ** (Calling Functions)](#9-unpacking-with--and--calling-functions)
- [10. Keyword-Only Arguments](#10-keyword-only-arguments)
- [11. Lambda Functions](#11-lambda-functions)
- [12. Scope — Local vs Global](#12-scope--local-vs-global)
- [13. Docstrings](#13-docstrings)
- [Common Pitfalls](#-common-pitfalls)

---

## 💡 What is a Function?

A function is a reusable block of code that performs a task. Instead of repeating code, you define it once and **call** it whenever needed.

---

## 1. Basic Function

```python
def greet():
    print("Hello!")

greet()   # calling the function
```

---

## 2. Parameters vs Arguments

```python
def greet(name):   # "name" is a parameter
    print(f"Hello, {name}!")

greet("Eros")      # "Eros" is the argument
```

> 🔹 **Parameter** = the placeholder in the function definition. **Argument** = the actual value passed when calling it.

---

## 3. Return Values

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)   # 7
```

> 🔹 `return` sends a value back to wherever the function was called. Without `return`, a function gives back `None`.

---

## 4. Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Eros")             # Hello, Eros!
greet("Eros", "Hey")      # Hey, Eros!
```

> 🔹 A default value makes a parameter **optional**. Skip it → default is used. Pass it → your value overrides the default.

⚠️ Default parameters must come **after** required (non-default) ones:
```python
def greet(greeting="Hello", name):   # ❌ SyntaxError
```

---

## 5. Positional vs Keyword Arguments

```python
def profile(name, age):
    print(f"{name} is {age} years old")

profile("Eros", 20)          # positional — order matters
profile(age=20, name="Eros") # keyword — order doesn't matter
```

---

## 6. *args — Flexible Positional Arguments

Collects any number of positional arguments into a **tuple**.

```python
def add(*numbers):
    print(numbers)        # tuple, e.g. (1, 2, 3)
    return sum(numbers)

add(1, 2)          # (1, 2) -> 3
add(1, 2, 3, 4)    # (1, 2, 3, 4) -> 10
add()              # () -> 0
```

More examples:
```python
def multiply(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def find_max(*numbers):
    if not numbers:
        return None
    return max(numbers)
```

---

## 7. **kwargs — Flexible Keyword Arguments

Collects any number of named arguments into a **dictionary**.

```python
def show_info(**details):
    print(details)   # {'name': 'Eros', 'age': 20}

show_info(name="Eros", age=20)
```

More examples:
```python
def print_receipt(**items):
    total = 0
    for item, price in items.items():
        print(f"{item}: Rs.{price}")
        total += price
    print(f"Total: Rs.{total}")

print_receipt(apple=30, banana=20, mango=50)
```

---

## 8. Combining Everything

**Order rule:** `normal params → *args → default params (keyword-only) → **kwargs`

```python
def profile(name, *hobbies, greeting="Hello", **extra):
    print(f"{greeting}, {name}!")
    print(f"Hobbies: {hobbies}")
    print(f"Extra info: {extra}")

profile(
    "Eros",
    "coding", "gaming",
    greeting="Hey",
    college="Morgan International College",
    age=20
)
```

Output:
```
Hey, Eros!
Hobbies: ('coding', 'gaming')
Extra info: {'college': 'Morgan International College', 'age': 20}
```

> ⚠️ Putting a default parameter **before** `*args` is risky — positional arguments fill left to right, so a value meant for `*args` can accidentally overwrite the default. Placing defaults **after** `*args` forces them to be passed by keyword only, avoiding ambiguity.

---

## 9. Unpacking with * and ** (Calling Functions)

`*` and `**` aren't just for function definitions — they also **unpack** collections when calling a function.

```python
def multiply(*numbers):
    ...

values = [2, 3, 4]
multiply(*values)     # same as multiply(2, 3, 4)

def configure(**settings):
    ...

options = {"theme": "dark", "font_size": 14}
configure(**options)  # same as configure(theme="dark", font_size=14)
```

| Context | Meaning |
|---|---|
| `*args` / `**kwargs` in `def` | **Packing** — collect extra arguments |
| `*list` / `**dict` in a function call | **Unpacking** — spread a collection into arguments |

---

## 10. Keyword-Only Arguments

Any parameter after `*args` (or a bare `*`) **must** be passed by keyword:

```python
def order(item, *, urgent=False):
    print(item, urgent)

order("pizza", urgent=True)   # ✅ works
order("pizza", True)          # ❌ TypeError
```

---

## 11. Lambda Functions

A short, anonymous, one-line function — used for quick throwaway logic.

```python
square = lambda x: x * x
print(square(5))   # 25

# Common use: as a key for sorting
names = ["Eros", "a", "banana"]
names.sort(key=lambda x: len(x))
```

---

## 12. Scope — Local vs Global

```python
x = 10   # global variable

def show():
    x = 5   # local variable — separate from global x
    print(x)

show()      # 5
print(x)    # 10
```

To modify a global variable inside a function, use `global`:
```python
def update():
    global x
    x = 20
```

---

## 13. Docstrings

```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

print(add.__doc__)   # Returns the sum of a and b.
```

> 🔹 Docstrings document what a function does — accessible via `.__doc__` or `help(add)`.

---

## ⚠️ Common Pitfalls

- **Mutable default arguments** — a classic Python trap:
  ```python
  def add_item(item, items=[]):   # ❌ dangerous
      items.append(item)
      return items
  ```
  The same list is reused across calls. Fix with:
  ```python
  def add_item(item, items=None):
      if items is None:
          items = []
      items.append(item)
      return items
  ```
- **Forgetting `return`** — the function runs but gives back `None`.
- **Mixing up `*args` order** — placing a default parameter before `*args` can silently consume a value meant for `*args`.
- **Confusing packing vs unpacking** — `*args` in a `def` packs; `*list` in a call unpacks.

---

<p align="center">📁 Part of <b>python/basic/concepts</b></p>
