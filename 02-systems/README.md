# 02 · Systems

**Goal:** Understand what the computer is doing underneath your code — processes, memory, networks, and persistent data.
**Time:** ~120 hours

## Why this tier exists

AI systems are systems. Training runs fail on disk I/O, inference bottlenecks on memory bandwidth, and every deployed model sits behind a network. Engineers who skip this tier spend their careers confused by their own error messages.

## Resources, in order

1. **Operating Systems: Three Easy Pieces** (free at pages.cs.wisc.edu/~remzi/OSTEP) — ~50 hours
   Read the three parts in order: virtualization (processes, memory), concurrency (threads, locks), persistence (files, disks). Do the homework simulations — they're short and clarifying.

2. **Computer Networking: A Top-Down Approach**, chapters 1–4 — ~30 hours
   Application, transport, network layers. The companion lecture videos by the authors are free and follow the book closely.

3. **CMU 15-445: Database Systems**, first half — ~40 hours
   Storage, buffer pools, indexes, query execution. If you only want to be fluent in SQL rather than understand engines, do **SQLBolt** instead (~8 hours) and come back later.

## Optional

- **Designing Data-Intensive Applications** (Kleppmann) — paid. The book every backend engineer eventually reads. Chapters 1–6 are the core.

## Checkpoint

- [ ] Write an HTTP server in Python using only the `socket` module — no frameworks — that serves static files
- [ ] Make it handle concurrent requests using threads
- [ ] Design a normalized schema in SQLite that logs each request (timestamp, path, status, duration) and write it from the server
- [ ] Explain what happens, layer by layer, when a browser requests a page from your server

## Capstone

A small web service with a database, deployed somewhere public (a free tier on any host is fine). Requirements:

- A real data model with at least three related tables
- Handles at least one operation that would break without a transaction
- A README with an architecture section: a diagram, and a paragraph on what breaks first under load and why
