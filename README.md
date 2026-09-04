# cs-ai-path

**A sequenced path from the foundations of computer science to research-level understanding of modern AI.**

Open resources. Strict order. Nothing extraneous.

---

## What this is

Most roadmaps are inventories: fifty resources per topic and no argument for which one matters. This is a curriculum in the original sense - an ordered course of study with a defined standard at each stage.

Every tier specifies:

- **One objective** - the capability you hold on completion
- **Three to five selected resources** - chosen for depth and precision, not popularity
- **A checkpoint** - a concrete demonstration that must be passed before advancing
- **A time budget** - realistic hours for focused, uninterrupted work

Progress is sequential. A tier is skipped only when its checkpoint can be passed without preparation.

## Who it is for

- Aspiring researchers who want the foundations a graduate program assumes but rarely teaches
- Engineers moving toward research or research-adjacent roles in AI
- Practitioners who can train or deploy models but want to understand the mechanisms underneath
- Anyone who intends to read, reproduce, and eventually contribute to primary literature

Prerequisites: a computer, roughly 8-10 hours per week, and the discipline to complete checkpoints rather than skim past them. No prior formal training is assumed.

## The path

| Tier | Focus | Hours |
|---|---|---:|
| [00 - Prerequisites](00-prerequisites/) | Mathematical readiness, the shell, version control | 30 |
| [01 - Programming](01-programming/) | Python, data structures, algorithmic analysis | 150 |
| [02 - Systems](02-systems/) | Operating systems, networks, storage engines | 120 |
| [03 - Mathematics for AI](03-math-for-ai/) | Linear algebra, probability, multivariable calculus | 100 |
| [04 - Machine Learning](04-machine-learning/) | Statistical learning, evaluation methodology | 100 |
| [05 - Deep Learning](05-deep-learning/) | Automatic differentiation from first principles to PyTorch | 120 |
| [06 - LLMs and Alignment](06-llms-and-alignment/) | Transformer architecture, pretraining, RLHF, safety | 100 |
| [Projects](projects/) | One capstone per tier, held to a published standard | - |

**Total: approximately 720 hours** - eighteen months at 10 hours per week, nine at 20. The complete sequence, with rationale and checkpoints, is in [CURRICULUM.md](CURRICULUM.md).

## Method

1. **Begin at Tier 00** regardless of background. The checkpoint, not self-assessment, determines whether it can be skipped.
2. **Pass the checkpoint before advancing.** Reading produces familiarity. Building produces understanding.
3. **Publish each capstone** to a separate repository before starting the next tier. The record of work is part of the training.
4. **Track progress** by forking this repository and completing the checklists in `CURRICULUM.md`.

## Principles

- **Sequence over volume.** The ordering is the contribution. Individual resources are replaceable; the structure is not.
- **Open by default.** Every core resource is freely available. Commercial alternatives are marked and never required.
- **Mechanism before abstraction.** Automatic differentiation is implemented by hand before a framework is introduced.
- **Primary sources.** Where a foundational paper exists, it is assigned directly rather than summarized.
- **Alignment is core material.** Safety and evaluation literature is part of Tier 06, not an appendix.
- **Subject to revision.** A resource is replaced when a stronger one is identified. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Evidence and scope

This repository is a curriculum design and research-planning artifact. It does not claim that every tier or capstone has already been completed by the author, and it is not a degree, credential, or substitute for supervised research.

The intended evidence loop is:

```text
objective -> primary sources -> implementation -> checkpoint -> public artifact -> review
```

For an example of the engineering standard expected from a capstone, see [Sentinel](https://github.com/Shawdaimarie/sentinel): a governed agent-execution and deterministic evaluation platform with tests, independent verifiers, CI, dependency audit, CodeQL, and explicit scope limits.

## Contributing

Contributions are welcome and held to a deliberately high standard. A resource is added only when it replaces a weaker one or fills a demonstrated gap. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

Curriculum text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Any code in this repository is licensed under [MIT](LICENSE).
