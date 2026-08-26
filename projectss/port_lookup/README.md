# Port Lookup

Looks up the common service for a port, or a range of ports, using a
static dictionary — not a live scan.

## Run it

python main3.py

**Input:** start port, end port

**Output:** only ports with a known service

Port 21 -> FTP
Port 22 -> SSH
Port 80 -> HTTP

## Concepts used

**Dictionaries** · **functions** · **range()** · **loops** · **conditionals** · **f-strings**

## Next

Replace the static lookup with a real `socket` check to test whether
ports are actually open — that version will get a full findings/
recommendations report, since it'll be a real scan.
