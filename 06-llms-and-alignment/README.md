# 06 · LLMs & Alignment

**Goal:** Understand how transformers and language models are built, trained, and evaluated — and the open problems in making them safe and reliable.
**Time:** ~100 hours

## Why this tier exists

Language models are the center of gravity in AI right now. But understanding the architecture is only half of it. The other half — how models are aligned, where that fails, and how you'd know — is treated as core here, not as an ethics appendix. You can't build reliable systems without it.

## Resources, in order

### Architecture and training

1. **Attention Is All You Need** (Vaswani et al., 2017) — ~4 hours
   Read it once for shape, then again after step 2 for detail. It's short.

2. **Andrej Karpathy: Let's build GPT** and the **nanoGPT** repository — ~20 hours
   Build the transformer from the micrograd foundations of Tier 05. Then read nanoGPT line by line.

3. **Stanford CS224N** — ~30 hours
   The lectures on transformers, pretraining, and prompting/RLHF. Skip the early word-vector material if you're short on time.

4. **Hugging Face LLM Course** — ~20 hours
   Tokenizers, fine-tuning, and the practical ecosystem. This is where you learn the tooling everyone actually uses.

### Alignment and safety — core, not optional

5. **Training language models to follow instructions with human feedback** (Ouyang et al., 2022) — ~4 hours
   The InstructGPT paper. This is what turned a text predictor into an assistant.

6. **Constitutional AI: Harmlessness from AI Feedback** (Bai et al., 2022) — ~4 hours
   How to align with a written set of principles rather than only human labels.

7. **Anthropic: Core Views on AI Safety** — ~2 hours
   A readable overview of why the field exists and what the open problems are.

## Checkpoint

- [ ] Train a small character-level GPT on a text corpus you chose — anything but the Shakespeare default
- [ ] Write one page: what RLHF does, what it doesn't solve, and why
- [ ] Demonstrate one concrete failure mode (sycophancy, confident hallucination, prompt injection) with any model you have access to, and document it

## Capstone

Fine-tune an open-weight model on a narrow task. Requirements:

- A task definition and a held-out evaluation set you built
- Results before and after fine-tuning, on that set
- A section on where it still fails — with examples
- Published, with the eval set, so someone else could reproduce it

Publishing the failures is the assignment. It's the habit the field needs most.
