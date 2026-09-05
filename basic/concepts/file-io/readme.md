# 📁 File Handling in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-File%20I%2FO-orange)
![Status](https://img.shields.io/badge/Status-Learning-brightgreen)

> Notes and examples covering how to read, write, and manage files in Python — from basics to advanced patterns.

---

## 📑 Table of Contents
- [What is File Handling?](#-what-is-file-handling)
- [1. Opening a File](#1-opening-a-file)
- [2. The Better Way — with](#2-the-better-way--with)
- [3. File Modes](#3-file-modes)
- [4. Writing to a File](#4-writing-to-a-file)
- [5. Reading a File](#5-reading-a-file)
- [6. Adding New Lines](#6-adding-new-lines)
- [7. Combining Write + Read](#7-combining-write--read-a-mode-and-w-mode)
- [8. file.seek()](#8-fileseek)
- [9. Alternate Writing Methods](#9-alternate-writing-methods)
- [10. File Handling + Error Handling](#10-file-handling--error-handling)
- [11. Common Pitfalls](#-common-pitfalls)

---

## 💡 What is File Handling?

File handling lets a program **read from** and **write to** files on disk — like `.txt`, `.csv`, `.json` — so data can persist beyond the program's runtime.

---

## 1. Opening a File

```python
file = open("notes.txt", "r")   # "r" = read mode
content = file.read()
print(content)
file.close()
```

> ⚠️ This works, but if an error happens between `open()` and `close()`, the file never gets closed properly — bad practice.

---

## 2. The Better Way — with

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

> 🔹 `with` automatically closes the file when the block ends — even if an error happens inside it. This is the **standard** way to handle files in Python.

`as file` just names the file object returned by `open()` — you could call it `f`, `handle`, anything. It's a variable, not a keyword.

---

## 3. File Modes

| Mode | Meaning | Erases Existing Content? | Creates File if Missing? |
|---|---|---|---|
| `"r"` | Read (file must exist) | No | ❌ No — raises `FileNotFoundError` |
| `"w"` | Write | ✅ Yes | ✅ Yes |
| `"a"` | Append | No | ✅ Yes |
| `"r+"` | Read + Write | No | ❌ No |
| `"w+"` | Write + Read | ✅ Yes | ✅ Yes |
| `"a+"` | Append + Read | No | ✅ Yes |

---

## 4. Writing to a File

```python
with open("notes.txt", "w") as file:
    file.write("Hello, this is day 5!\n")
    file.write("Learning file handling.\n")
```

> ⚠️ `"w"` mode **erases** everything already in the file before writing.

---

## 5. Reading a File

```python
# Read everything at once
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

```python
# Read line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())   # strip() removes the trailing newline
```

---

## 6. Adding New Lines

```python
with open("notes.txt", "w") as file:
    file.write("Apple\n")   # \n moves to the next line
    file.write("ball")
```

Output:
```
Apple
ball
```

`\n` is the newline character — without it, everything gets written on a single line.

---

## 7. Combining Write + Read (a+ mode and w+ mode)

`"a"` and `"w"` modes are **write-only** — calling `.read()` on them raises an error. To both write and read in the same block, use `"a+"` or `"w+"`.

```python
with open("ports.txt", "a+") as file:
    file.write("500\n")
    file.write("100\n")
    file.seek(0)              # move cursor back to the start
    content = file.read()
    print(content)
```

> ⚠️ `"w+"` erases the file first. `"a+"` keeps existing content and adds to the end.

---

## 8. file.seek()

After writing, the file's internal cursor sits at the **end** of the file. `.read()` from there returns nothing.

```python
file.seek(0)   # moves cursor back to position 0 (the start)
```

Always call `seek(0)` before reading if you just wrote to the file in the same block.

---

## 9. Alternate Writing Methods

**writelines() — write a list of lines at once**
```python
with open("notes.txt", "w") as file:
    lines = ["Apple\n", "ball\n"]
    file.writelines(lines)
```

**print() with file= — auto-adds newline**
```python
with open("notes.txt", "w") as file:
    print("Apple", file=file)
    print("ball", file=file)
```

> 🔹 Most common in practice: plain `\n` inside strings. The others are situational — `writelines()` when you already have a list, `print(file=...)` for quick scripts.

---

## 10. File Handling + Error Handling

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("That file doesn't exist!")
```

> 🔹 Always wrap file reads in `try/except` when the file's existence isn't guaranteed — e.g. user-provided filenames.

---

## ⚠️ Common Pitfalls

- **`FileNotFoundError` on `"r"` mode** — the file doesn't exist yet, or the script is running from a different working directory than expected. Check with:
  ```python
  import os
  print(os.getcwd())      # current working directory
  print(os.listdir())     # files Python can see from here
  ```
- **Forgetting `as file`** — without it, you have no variable to call `.read()`/`.write()` on inside the `with` block.
- **Reading right after writing without `seek(0)`** — returns an empty string, since the cursor is at the end of the file.
- **Using `"w"` when you meant `"a"`** — `"w"` silently erases existing content.

---

<p align="center">📁 Part of <b>python/basic/concepts</b></p>
