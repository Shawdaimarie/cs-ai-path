# 05 · Deep Learning

**Goal:** Understand backpropagation deeply enough to implement it, then use PyTorch fluently.
**Time:** ~120 hours

## Why this tier exists

Frameworks hide the mechanism. If you learn PyTorch first, you'll be able to train models and never understand why they don't converge. So the order here is: build autograd yourself, then earn the framework.

## Resources, in order

1. **Andrej Karpathy: Neural Networks: Zero to Hero** — ~40 hours
   Start with *micrograd* and *makemore*. Type every line yourself; don't copy. Stop before the GPT video — that's Tier 06.

2. **Dive into Deep Learning** (free at d2l.ai) — ~50 hours
   Chapters on linear networks, multilayer perceptrons, builders' guide, CNNs, optimization, and attention mechanisms. The PyTorch tabs are the ones to use.

3. **fast.ai: Practical Deep Learning for Coders** — ~30 hours
   Top-down complement: start from working models and dig in. Do it *after* the bottom-up work so the magic doesn't stay magic.

## Optional

- **Stanford CS231n lecture notes** — convolutional networks in depth, and the best single explanation of backprop in the wild

## Checkpoint

- [ ] Implement a scalar autograd engine (like micrograd) from a blank file, without reference
- [ ] Train an MLP on MNIST using only your engine and NumPy — reach 95%+ test accuracy
- [ ] Reproduce the same result in PyTorch in under 50 lines
- [ ] Explain why the PyTorch version is faster, in terms of what's actually happening

## Capstone

Train a model on a dataset you assembled *yourself* — images, audio, or text. Requirements:

- A written description of how the data was collected and labeled
- Training and validation curves
- A section on failure cases: what does the model get wrong, and can you guess why?
- The compute you used (hardware, wall-clock time)

Assembling your own data is the point. Anyone can train on MNIST.
