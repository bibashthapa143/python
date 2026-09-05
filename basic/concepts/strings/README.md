# 🔤 Strings in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Strings-orange)
![Status](https://img.shields.io/badge/Status-Learning-brightgreen)

> Notes and examples covering Python strings — creation, formatting, methods, and advanced patterns.

---

## 📑 Table of Contents
- [What is a String?](#-what-is-a-string)
- [1. Creating Strings](#1-creating-strings)
- [2. Indexing & Slicing](#2-indexing--slicing)
- [3. String Concatenation](#3-string-concatenation)
- [4. f-strings (Formatting)](#4-f-strings-formatting)
- [5. Other Formatting Methods](#5-other-formatting-methods)
- [6. Common String Methods](#6-common-string-methods)
- [7. Checking String Content](#7-checking-string-content)
- [8. Splitting & Joining](#8-splitting--joining)
- [9. Escape Characters](#9-escape-characters)
- [10. Multi-line Strings](#10-multi-line-strings)
- [11. Strings Are Immutable](#11-strings-are-immutable)
- [12. Looping Through a String](#12-looping-through-a-string)
- [13. Raw Strings](#13-raw-strings)
- [Common Pitfalls](#-common-pitfalls)

---

## 💡 What is a String?

A string is a sequence of characters used to represent text, enclosed in quotes (`'...'` or `"..."`).

---

## 1. Creating Strings

```python
name = "Eros"
name2 = 'Eros'          # single or double quotes both work
sentence = "It's fine"  # use double quotes if the text has an apostrophe
```

---

## 2. Indexing & Slicing

```python
word = "Python"

print(word[0])      # P   (first character)
print(word[-1])     # n   (last character)
print(word[0:3])    # Pyt (index 0 up to, not including, 3)
print(word[::-1])   # nohtyP (reversed)
```

---

## 3. String Concatenation

```python
first = "Hello"
second = "World"

print(first + " " + second)     # Hello World
print(first * 3)                # HelloHelloHello
```

---

## 4. f-strings (Formatting)

The modern, preferred way to insert variables into strings.

```python
name = "Eros"
age = 20
print(f"{name} is {age} years old")   # Eros is 20 years old

# expressions work too
print(f"Next year: {age + 1}")

# formatting numbers
price = 49.999
print(f"Price: {price:.2f}")    # Price: 50.00
```

---

## 5. Other Formatting Methods

```python
# .format()
print("{} is {} years old".format(name, age))

# % formatting (older style, still seen in legacy code)
print("%s is %d years old" % (name, age))
```

> 🔹 f-strings are the standard in modern Python — use them by default.

---

## 6. Common String Methods

| Method | What it does | Example |
|---|---|---|
| `.lower()` | Convert to lowercase | `"HELLO".lower()` → `"hello"` |
| `.upper()` | Convert to uppercase | `"hello".upper()` → `"HELLO"` |
| `.strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `.replace(a, b)` | Replace substring | `"cat".replace("c", "b")` → `"bat"` |
| `.split(sep)` | Split into a list | `"a,b,c".split(",")` → `['a','b','c']` |
| `.join(list)` | Join list into a string | `"-".join(["a","b"])` → `"a-b"` |
| `.find(sub)` | Index of first match (-1 if not found) | `"hello".find("l")` → `2` |
| `.count(sub)` | Count occurrences | `"hello".count("l")` → `2` |
| `.startswith(x)` | Check start | `"hello".startswith("he")` → `True` |
| `.endswith(x)` | Check end | `"hello".endswith("lo")` → `True` |
| `.title()` | Capitalize each word | `"hello world".title()` → `"Hello World"` |
| `len(str)` | Length of string | `len("hello")` → `5` |

---

## 7. Checking String Content

```python
"123".isdigit()      # True — all digits
"abc".isalpha()       # True — all letters
"abc123".isalnum()    # True — letters and/or digits
"   ".isspace()       # True — all whitespace
"Hello".isupper()     # False
"HELLO".isupper()     # True
```

---

## 8. Splitting & Joining

```python
sentence = "I love Python programming"
words = sentence.split()          # splits by whitespace by default
print(words)                       # ['I', 'love', 'Python', 'programming']

csv_line = "apple,banana,mango"
items = csv_line.split(",")
print(items)                       # ['apple', 'banana', 'mango']

# joining back together
joined = ", ".join(items)
print(joined)                      # apple, banana, mango
```

---

## 9. Escape Characters

| Escape | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

```python
print("Line1\nLine2")     # prints on two lines
print("Name:\tEros")      # tab-separated
print("She said \"hi\"")  # She said "hi"
```

---

## 10. Multi-line Strings

```python
message = """This is line one.
This is line two.
This is line three."""
print(message)
```

> 🔹 Triple quotes (`"""..."""` or `'''...'''`) also double as docstrings for functions/classes.

---

## 11. Strings Are Immutable

Once created, a string **cannot be changed** in place — any "modification" creates a new string.

```python
word = "hello"
word[0] = "H"    # ❌ TypeError: 'str' object does not support item assignment

# Correct way — build a new string
word = "H" + word[1:]
print(word)      # Hello
```

---

## 12. Looping Through a String

```python
for char in "Python":
    print(char)
```

---

## 13. Raw Strings

Prevents `\` from being treated as an escape character — useful for file paths and regex patterns.

```python
path = "C:\new_folder"      # ❌ \n is read as newline — breaks the path
path = r"C:\new_folder"     # ✅ raw string — backslash is literal
```

---

## ⚠️ Common Pitfalls

- **Trying to modify a string directly** (`word[0] = "x"`) — strings are immutable; build a new one instead.
- **Forgetting `.split()` splits on whitespace by default** — pass a separator explicitly for CSV-like data: `.split(",")`.
- **Mixing up `.find()` and `.index()`** — `.find()` returns `-1` if not found, `.index()` raises `ValueError`.
- **Using `%` or `.format()` in new code** — prefer f-strings for readability.
- **Forgetting `r""` for Windows file paths** — `\n`, `\t` etc. inside a normal string get interpreted as escape sequences.

---

<p align="center">📁 Part of <b>python/basic/concepts</b></p>
