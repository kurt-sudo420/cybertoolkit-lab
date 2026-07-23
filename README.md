# CyberToolkit

A command-line collection of basic network security utilities, written in Python. Built as a hands-on way to work with sockets, hashing, and the everyday building blocks of network security work.

## ⚠️ Scope of use

The **port scanner** and **banner grabber** make network connections to other hosts. Only use them against:

- systems you own, or
- systems you have **explicit written authorization** to test.

Scanning or probing hosts without permission may violate network policy (including university acceptable-use policy) and, in many jurisdictions, the law. When in doubt, don't run it.

## Tools

| # | Tool | What it does |
|---|------|--------------|
| 1 | Port Scanner | Checks which TCP ports are open on a host. Supports port ranges and runs concurrently. |
| 2 | SHA-256 File Hash | Computes the SHA-256 digest of a file, read in chunks so large files work. |
| 3 | Password Generator | Generates a cryptographically secure random password of a chosen length. |
| 4 | DNS Lookup | Resolves a domain to all of its IP addresses. |
| 5 | Banner Grabber | Connects to a host:port and prints any service banner returned. |

## Usage

```bash
python cybertoolkit.py
```

Then choose a tool from the menu. Example scan:

```
Choice: 1
Enter IP or hostname: scanme.nmap.org
Ports [Enter for common ports]: 20-100

Scanning 45.33.32.156 (81 ports)...

Open ports:
     22/tcp  SSH
     80/tcp  HTTP
```

(`scanme.nmap.org` is a host Nmap provides specifically for testing — one of the few you can legally scan without prior arrangement.)

## Design notes

A few choices worth calling out, since they're the difference between a tutorial script and something considered:

- **Threaded scanning.** A sequential scan of 1,000 ports at a 0.5s timeout could take minutes when ports are filtered. A `ThreadPoolExecutor` overlaps the waiting, so the scan is bounded by the slowest port rather than the sum of all of them.
- **`secrets`, not `random`.** The password generator uses `secrets.choice`. Python's `random` module is a pseudo-random generator and is unsafe for anything security-related.
- **Chunked hashing.** Files are read 64 KB at a time rather than loaded whole, so hashing a large file doesn't depend on it fitting in memory.
- **Specific exception handling.** Each tool catches the errors it actually expects (`ConnectionRefusedError`, `socket.timeout`, `FileNotFoundError`) and reports them distinctly, rather than a bare `except` that hides what went wrong and swallows Ctrl+C.
- **Hostnames resolved once.** The scanner resolves a hostname to an IP before the loop, so a bad hostname fails immediately instead of erroring on every port.

## Tests

```bash
python -m pytest test_cybertoolkit.py -v
```

The tests cover the port-specification parser (ranges, lists, dedup, invalid input). The network functions are verified manually against a local listener.

## Requirements

Python 3.8+. Standard library only — no dependencies.

## Possible extensions

- UDP scanning (this only does TCP)
- Export results to JSON or CSV
- Concurrent banner grabbing across multiple ports
- Reverse DNS lookups
