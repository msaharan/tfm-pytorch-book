# Engineering Tabular Foundation Models with PyTorch

This repository contains the manuscript and executable companion code for:

> **Engineering Tabular Foundation Models with PyTorch**
> *From Tensor Geometry and Attention to In-Context Learning Systems*

The book teaches readers to understand, implement, test, evaluate, and operate
tabular foundation models. PyTorch is taught through that objective rather than
as an isolated API catalogue.

## Current status

The project is in its **pilot manuscript** phase. The initial milestone is four
connected chapters that validate the book's teaching method:

1. read PyTorch through semantic axes;
2. express attention as information flow;
3. derive the tabular foundation model problem;
4. build and test a minimal in-context table predictor.

See [the book proposal](proposal/book-proposal.md),
[editorial plan](proposal/editorial-plan.md), and
[source inventory](proposal/source-inventory.md) for the complete scope.

## Repository layout

```text
book/                 Quarto manuscript
proposal/             audience, positioning, roadmap, and editorial decisions
src/tfm_pytorch_book/ recurring educational implementation
tests/                tests for code used by the manuscript
_quarto.yml           book navigation and output configuration
```

## Build the book

Prerequisites:

- [Quarto](https://quarto.org/)
- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync --group dev
uv run pytest
quarto preview
```

Rendered output is written to `_book/`.

## Editorial principle

Every technical chapter must connect four questions:

1. What is the tensor geometry?
2. What computation is learned?
3. Where can information flow?
4. What changes at runtime?

This is not a guide to calling one pretrained estimator. It is a guide to
reasoning about tabular foundation models as mathematical objects, PyTorch
programs, and engineered systems.
