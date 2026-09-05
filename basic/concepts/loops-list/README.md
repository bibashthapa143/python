# 🔁 Loops & Lists in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Loops%20%26%20Lists-orange)
![Status](https://img.shields.io/badge/Status-Learning-brightgreen)

> Notes and examples covering loops (`for`, `while`) and lists — from basics to advanced patterns like comprehensions and slicing.

---

## 📑 Table of Contents
- [Part 1: Loops](#-part-1-loops)
  - [1. for Loop](#1-for-loop)
  - [2. while Loop](#2-while-loop)
  - [3. range()](#3-range)
  - [4. break, continue, pass](#4-break-continue-pass)
  - [5. else with Loops](#5-else-with-loops)
  - [6. Nested Loops](#6-nested-loops)
  - [7. enumerate()](#7-enumerate)
  - [8. zip()](#8-zip)
- [Part 2: Lists](#-part-2-lists)
  - [9. Creating & Accessing Lists](#9-creating--accessing-lists)
  - [10. Slicing](#10-slicing)
  - [11. Common List Methods](#11-common-list-methods)
  - [12. List Comprehensions](#12-list-comprehensions)
  - [13. Nested Lists](#13-nested-lists)
  - [14. Sorting](#14-sorting)
  - [15. Copying Lists](#15-copying-lists)
- [Common Pitfalls](#-common-pitfalls)

---

## 🔁 Part 1: Loops

## 1. for Loop

Used to iterate over a sequence (list, string, range, etc.)

```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```

## 2. while Loop

Repeats as long as a condition is `True`.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

> ⚠️ Make sure the condition eventually becomes `False`, or you get an **infinite loop**.

## 3. range()

Generates a sequence of numbers — commonly used with `for`.

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8 (step of 2)

for i in range(5):
    print(i)
```

## 4. break, continue, pass

```python
for i in range(5):
    if i == 3:
        break        # exits the loop entirely
    print(i)
# 0 1 2

for i in range(5):
    if i == 3:
        continue     # skips this iteration only
    print(i)
# 0 1 2 4

for i in range(5):
    if i == 3:
        pass         # does nothing, placeholder
    print(i)
# 0 1 2 3 4
```

## 5. else with Loops

The `else` block runs if the loop finishes **without hitting `break`**.

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop finished without break")
```

> 🔹 Useful for search patterns — e.g. "if item was never found, do X."

## 6. Nested Loops

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

## 7. enumerate()

Gives you both the index and the value while looping.

```python
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 mango
```

## 8. zip()

Loops through multiple lists in parallel.

```python
names = ["Eros", "Sam"]
ages = [20, 22]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

---

## 📋 Part 2: Lists

## 9. Creating & Accessing Lists

```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])     # apple (first item)
print(fruits[-1])    # mango (last item)
```

> 🔹 Lists are **ordered**, **mutable** (changeable), and can hold mixed types: `[1, "two", 3.0, True]`

## 10. Slicing

```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3]   — index 1 up to (not including) 4
print(numbers[:3])     # [0, 1, 2]   — from start
print(numbers[3:])     # [3, 4, 5]   — to end
print(numbers[::2])    # [0, 2, 4]   — every 2nd item
print(numbers[::-1])   # [5, 4, 3, 2, 1, 0] — reversed
```

## 11. Common List Methods

| Method | What it does | Example |
|---|---|---|
| `.append(x)` | Add item to end | `fruits.append("kiwi")` |
| `.insert(i, x)` | Insert at index | `fruits.insert(1, "kiwi")` |
| `.remove(x)` | Remove first matching value | `fruits.remove("apple")` |
| `.pop(i)` | Remove & return item at index (default: last) | `fruits.pop()` |
| `.sort()` | Sort in place | `numbers.sort()` |
| `.reverse()` | Reverse in place | `numbers.reverse()` |
| `.index(x)` | Find index of value | `fruits.index("mango")` |
| `.count(x)` | Count occurrences | `numbers.count(2)` |
| `.extend(list)` | Add all items from another list | `fruits.extend(["kiwi", "pear"])` |
| `.clear()` | Remove all items | `fruits.clear()` |
| `len(list)` | Number of items | `len(fruits)` |

## 12. List Comprehensions

A compact way to build a list from a loop.

```python
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

# with a condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8]

# equivalent long-form:
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
```

> 🔹 Comprehensions are more Pythonic and often faster than a manual loop + `.append()`.

## 13. Nested Lists

```python
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[0])       # [1, 2]
print(matrix[0][1])    # 2

for row in matrix:
    for value in row:
        print(value)
```

## 14. Sorting

```python
numbers = [3, 1, 4, 1, 5]

numbers.sort()                 # in-place, changes original
sorted_copy = sorted(numbers)  # returns a new sorted list, original unchanged

numbers.sort(reverse=True)     # descending order

# sort by custom key
words = ["banana", "kiwi", "apple"]
words.sort(key=len)            # sort by length
```

## 15. Copying Lists

```python
original = [1, 2, 3]

# ❌ This does NOT copy — both names point to the same list
copy_wrong = original
copy_wrong.append(4)
print(original)   # [1, 2, 3, 4] — original changed too!

# ✅ Proper copy
copy_right = original.copy()
# or
copy_right = original[:]
# or
copy_right = list(original)
```

---

## ⚠️ Common Pitfalls

- **Modifying a list while looping over it** — can skip items or cause bugs:
  ```python
  for item in my_list:
      if item == "x":
          my_list.remove(item)   # ❌ risky — loop over a copy instead
  for item in my_list[:]:
      ...
  ```
- **`copy_wrong = original`** — this doesn't create a new list, just another name for the same one. Use `.copy()`, `[:]`, or `list()`.
- **Off-by-one slicing errors** — remember `list[a:b]` excludes index `b`.
- **Infinite `while` loops** — always double check the condition changes over iterations.
- **`range(5)` doesn't include 5** — it goes from `0` to `4`.

---

<p align="center">📁 Part of <b>python/basic/concepts</b></p>
