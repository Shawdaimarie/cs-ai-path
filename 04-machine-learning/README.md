# 04 · Machine Learning

**Goal:** Frame a problem as a learning problem, train classical models, and — most importantly — evaluate them honestly.
**Time:** ~100 hours

## Why this tier exists

Most ML failures in the real world are evaluation failures: data leaking from test into train, the wrong metric, a baseline nobody checked. Deep learning is Tier 05. This tier teaches the discipline that makes any model trustworthy.

## Resources, in order

1. **Machine Learning Specialization** (Andrew Ng, Coursera — free to audit) — ~40 hours
   All three courses. Course 1 for regression and classification, Course 2 for neural nets and the practical advice on bias/variance, Course 3 for unsupervised and recommenders.

2. **An Introduction to Statistical Learning** (free PDF at statlearning.com) — ~40 hours
   Chapters 2–8, with the Python labs. The chapters on resampling and model selection are the heart of this tier.

3. **scikit-learn user guide** — ~20 hours
   Read the sections on model evaluation, cross-validation, and pipelines. Learn `Pipeline` properly — it's how you prevent leakage structurally rather than by being careful.

## Optional

- **Kaggle Learn: Intermediate Machine Learning** and **Feature Engineering** — short, practical, hands-on

## Checkpoint

From scratch in NumPy:

- [ ] Linear regression (closed form *and* gradient descent)
- [ ] Logistic regression
- [ ] k-means

Then, on a public tabular dataset:

- [ ] Build a train/validation/test split and justify it
- [ ] Beat a sensible baseline (predict the mean, predict the majority class)
- [ ] Explain, in writing, why your evaluation isn't leaking

## Capstone

An end-to-end ML project on real data, with a written report covering:

- The problem, and why it's a learning problem
- The data: where it came from, what's wrong with it, what you did about it
- The evaluation method, and why that metric
- Results against a baseline
- What you'd do differently with twice the time

The report matters more than the model. A mediocre model with an honest report beats a great model with a vague one.
