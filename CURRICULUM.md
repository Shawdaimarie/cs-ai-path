# Curriculum

The complete, ordered path. Each tier lists its goal, core resources, checkpoint, and capstone. Fork this file and check boxes as you go.

Legend: **Core** = required · **Optional** = go deeper if you have time · **Paid** = costs money, always has a free alternative above it

---

## Tier 00 · Prerequisites  (~30 hours)

**Goal:** Be comfortable in a terminal, use Git without fear, and have the math you'll need for Tier 01.

**Core**
- [ ] *The Missing Semester of Your CS Education* (MIT) — shell, editors, Git, debugging
- [ ] *Pro Git*, chapters 1–3 (free online) — enough Git to work on any team
- [ ] Khan Academy: Algebra II and Precalculus units on functions, logarithms, and sequences

**Checkpoint:** From an empty directory, initialize a Git repo, create a branch, make three commits, merge the branch, and push to GitHub — using only the terminal, in under 10 minutes.

---

## Tier 01 · Programming  (~150 hours)

**Goal:** Write clean Python, understand core data structures, and reason about algorithmic complexity.

**Core**
- [ ] *CS50x* (Harvard) — the best single introduction to computer science that exists
- [ ] *CS50P: Introduction to Programming with Python* (Harvard)
- [ ] *MIT 6.006: Introduction to Algorithms* (OpenCourseWare) — lectures and problem sets

**Optional**
- [ ] *Automate the Boring Stuff with Python* — practical scripting
- [ ] LeetCode or NeetCode "Blind 75" — pattern practice, not memorization

**Checkpoint:** Implement a hash map, a binary search tree, and Dijkstra's algorithm from scratch in Python with tests. Explain the time complexity of each operation out loud.

**Capstone:** A command-line tool that solves a real problem for you (file organizer, budget tracker, flashcard app). Tested, documented, on GitHub.

---

## Tier 02 · Systems  (~120 hours)

**Goal:** Understand what the computer is doing underneath your code — processes, memory, networks, and persistent data.

**Core**
- [ ] *Operating Systems: Three Easy Pieces* (free online textbook) — virtualization, concurrency, persistence
- [ ] *Computer Networking: A Top-Down Approach* — chapters 1–4, or the companion lecture videos
- [ ] *CMU 15-445: Database Systems* — first half of the lectures, or *SQLBolt* if you want just the SQL

**Optional**
- [ ] *Designing Data-Intensive Applications* (Kleppmann) **Paid** — the book every backend engineer eventually reads

**Checkpoint:** Write a multithreaded HTTP server in Python from sockets up — no frameworks — that serves static files and handles concurrent requests. Then design a normalized schema for it to log requests to SQLite.

**Capstone:** A small web service with a database, deployed somewhere public, with a README that explains its architecture.

---

## Tier 03 · Math for AI  (~100 hours)

**Goal:** Read a machine learning paper's equations without panic. Understand vectors, matrices, gradients, and distributions intuitively *and* mechanically.

**Core**
- [ ] 3Blue1Brown: *Essence of Linear Algebra* — build intuition first
- [ ] 3Blue1Brown: *Essence of Calculus*
- [ ] *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong — free PDF) — chapters 2–7
- [ ] Khan Academy: Statistics and Probability

**Optional**
- [ ] MIT 18.06: *Linear Algebra* (Gilbert Strang) — the classic, if you want rigor

**Checkpoint:** By hand, compute the gradient of a two-layer network's loss with respect to its weights. In NumPy, implement matrix multiplication, softmax, and a 2D Gaussian sampler without using the built-in functions for them.

---

## Tier 04 · Machine Learning  (~100 hours)

**Goal:** Frame a problem as a learning problem, train classical models, and — most importantly — evaluate them honestly.

**Core**
- [ ] *Machine Learning Specialization* (Andrew Ng, Coursera — free to audit)
- [ ] *An Introduction to Statistical Learning* (free PDF) — chapters 2–8, with the Python labs
- [ ] scikit-learn user guide — model evaluation and cross-validation sections

**Optional**
- [ ] Kaggle Learn: *Intermediate Machine Learning* and *Feature Engineering*

**Checkpoint:** Implement linear regression, logistic regression, and k-means from scratch in NumPy. Then take a public tabular dataset, build a proper train/validation/test split, and beat a baseline — and explain why your evaluation isn't leaking.

**Capstone:** An end-to-end ML project on real data with a written report covering the problem, the data, the evaluation method, the results, and what you'd do differently.

---

## Tier 05 · Deep Learning  (~120 hours)

**Goal:** Understand backpropagation deeply enough to implement it, then use PyTorch fluently.

**Core**
- [ ] Andrej Karpathy: *Neural Networks: Zero to Hero* — build autograd and a language model from scratch
- [ ] *Dive into Deep Learning* (d2l.ai) — chapters on MLPs, CNNs, optimization, and attention
- [ ] fast.ai: *Practical Deep Learning for Coders* — the top-down complement

**Optional**
- [ ] Stanford CS231n lecture notes — convolutional networks in depth

**Checkpoint:** Implement a scalar autograd engine and train an MLP on MNIST using only it and NumPy. Then reproduce the same result in PyTorch in under 50 lines.

**Capstone:** Train a model on a dataset you assembled yourself (images, audio, or text). Document the data, the training curves, the failure cases, and the compute you used.

---

## Tier 06 · LLMs & Alignment  (~100 hours)

**Goal:** Understand how transformers and language models are built, trained, and evaluated — and the open problems in making them safe and reliable.

**Core**
- [ ] *Attention Is All You Need* (Vaswani et al., 2017) — read it twice; it's short
- [ ] Andrej Karpathy: *Let's build GPT* and the nanoGPT repository
- [ ] Stanford CS224N: *Natural Language Processing with Deep Learning* — the transformer and pretraining lectures
- [ ] Hugging Face: *LLM Course* — tokenizers, fine-tuning, and the ecosystem

**Alignment & safety (core, not optional)**
- [ ] *Training language models to follow instructions with human feedback* (Ouyang et al., 2022) — the InstructGPT paper
- [ ] *Constitutional AI: Harmlessness from AI Feedback* (Bai et al., 2022)
- [ ] Anthropic: *Core Views on AI Safety* — a readable overview of why the field exists

**Checkpoint:** Train a small character-level GPT on a text corpus of your choice. Then write a one-page explanation of what RLHF does, what it doesn't solve, and one failure mode you can demonstrate with a model you have access to.

**Capstone:** Fine-tune an open model on a narrow task, build an evaluation set for it, and publish the results — including the cases where it fails.

---

## After the path

You now have seven shipped projects and the foundations most graduates lack. Good next moves:

- Contribute to an open-source ML library
- Reproduce a recent paper and write up what didn't match
- Pick a specialization: systems for ML, interpretability, applied ML, or research

## Changelog

- **2026-08** — Initial curriculum.
