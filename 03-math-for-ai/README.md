# 03 · Math for AI

**Goal:** Read a machine learning paper's equations without panic. Understand vectors, matrices, gradients, and distributions intuitively *and* mechanically.
**Time:** ~100 hours

## Why this tier exists

Machine learning is applied linear algebra, calculus, and probability. You can call `model.fit()` without this tier. You cannot debug why it produced garbage.

The order below is intentional: intuition first (video), then mechanics (textbook), then practice (code).

## Resources, in order

1. **3Blue1Brown: Essence of Linear Algebra** — ~6 hours
   Watch all of it before touching a textbook. Vectors as arrows, matrices as transformations, determinants as area scaling. Pause and predict before each reveal.

2. **3Blue1Brown: Essence of Calculus** — ~5 hours
   Same approach. Chain rule is the one to internalize — backpropagation *is* the chain rule.

3. **Mathematics for Machine Learning** (Deisenroth, Faisal, Ong — free PDF at mml-book.com) — ~60 hours
   Chapters 2–7: linear algebra, analytic geometry, matrix decompositions, vector calculus, probability, optimization. Do the exercises. This is the slow, rigorous pass.

4. **Khan Academy: Statistics and Probability** — ~25 hours
   Random variables, distributions, expectation, variance, Bayes. Skip descriptive statistics if you know it.

## Optional

- **MIT 18.06: Linear Algebra** (Gilbert Strang) — the classic lecture series, if you want the full rigorous course

## Checkpoint

By hand, on paper:

- [ ] Derive the gradient of a two-layer network's mean-squared-error loss with respect to every weight
- [ ] Compute the eigenvalues and eigenvectors of a 2×2 matrix and explain what they mean geometrically

In NumPy, without using the built-in function for it:

- [ ] Matrix multiplication
- [ ] Softmax (numerically stable)
- [ ] A sampler for a 2D Gaussian with a given mean and covariance

## No capstone

The checkpoint is the deliverable. Commit your NumPy implementations to a repo — you'll reuse them in Tier 05.
