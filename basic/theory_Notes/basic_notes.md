# 🐍 Python Basics — Quick Reference

*Definition → Syntax → Example, for fast revision.*

---

## Variables
Stores a value under a name.
```python
name = "value"
```
```python
port = 443
```

## Operators
| Type | Symbols | Example |
|---|---|---|
| Math | `+ - * / %` | `10 % 3` → `1` |
| Compare | `== != > < >= <=` | `port == 443` |
| Logic | `and or not` | `port > 0 and port < 65536` |

---

## Lists `[ ]`
Ordered collection, accessed by **position (index)**, starting at `0`.
```python
my_list = [item1, item2, item3]
my_list[0]        # first item
```
```python
ports = ["22", "80", "443"]
ports[1]          # "80"
```

## Dictionaries `{ }`
Key → value pairs, accessed by **key**, not position.
```python
my_dict = {key: value}
my_dict[key]
my_dict.get(key, default)   # safe lookup — no crash if key missing
```
```python
port_services = {21: "FTP", 22: "SSH", 443: "HTTPS"}
port_services[22]                    # "SSH"
port_services.get(9999, "Unknown")   # "Unknown"
```

---

## Functions
Reusable block of code you can call by name.
```python
def function_name(parameter):
    return result
```
```python
def lookup(port):
    return port_services.get(port, "Unknown")

lookup(443)   # "HTTPS"
```

---

## Loops
Repeat code once per item in a sequence.
```python
for item in sequence:
    # code using item
```
```python
for port in [22, 80, 443]:
    print(port)
```

## List Comprehension
Shortcut for building a list with a loop, in one line.
```python
[expression for item in sequence]
```
```python
[int(p) for p in ["22", "80", "443"]]   # [22, 80, 443]
```

---

## String Methods
| Method | What it does | Example |
|---|---|---|
| `f"{var}"` | insert variable into text | `f"Port {port}"` |
| `.strip()` | remove leading/trailing spaces | `" hi ".strip()` → `"hi"` |
| `.lower()` / `.upper()` | change case | `"Hi".lower()` → `"hi"` |
| `.replace(a, b)` | swap text | `"a-b".replace("-", "_")` → `"a_b"` |
| `.split(sep)` | string → list | `"22,80".split(",")` → `["22","80"]` |
| `sep.join(list)` | list → string | `",".join(["22","80"])` → `"22,80"` |

**Memory trick:** *split the string* (dot on string) → *join with the glue* (dot on separator).

---

## File I/O
Always use `with` — it auto-closes the file.
```python
with open("file.txt", "r") as f:
    content = f.read()          # whole file as one string
```
```python
with open("file.txt", "r") as f:
    for line in f:               # read line by line
        print(line.strip())
```
```python
with open("file.txt", "w") as f:
    f.write("some text\n")       # "w" overwrites, "a" appends
```

| Mode | Meaning |
|---|---|
| `"r"` | read (file must exist) |
| `"w"` | write (creates/overwrites) |
| `"a"` | append (adds to end) |

---

## Error Handling
Catch errors instead of crashing.
```python
try:
    # risky code
except ErrorType:
    # runs if that error happens
else:
    # runs only if try succeeded
finally:
    # always runs, error or not
```
```python
try:
    port = int(input("Enter port: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"Port: {port}")
finally:
    print("Done.")
```

---

## Quick Type Cheatsheet
| Type | Brackets | Access by |
|---|---|---|
| List | `[ ]` | index (position) |
| Dictionary | `{ }` | key |
| String | `" "` | index / methods |
