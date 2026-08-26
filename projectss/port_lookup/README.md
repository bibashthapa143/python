# 🔍 Port Lookup

> A lightweight Python tool that maps ports to their common services — the first step toward a full-blown port scanner.

---

## ⚙️ How It Works

Looks up the common service for a single port, or a whole range of ports, using a static dictionary lookup. **Not a live scan** — yet.

## 🚀 Run It

```bash 
python main3.py
``` 

**Input:** start port, end port <br>
**Output:** only the ports that match a known service

```
Port 21 -> FTP
Port 22 -> SSH
Port 80 -> HTTP
```


---

## 🧠 Concepts Practiced

`Dictionaries` `Functions` `range()` `Loops` `Conditionals` `f-strings`

---

## 🔭 What's Next

This is **Step 1** of a bigger build. Coming up:

- Swap the static dictionary for a real `socket` connection check
- Actually test whether ports are open on a target
- Ship a full **findings + recommendations** report, since it'll be a real scan

---
