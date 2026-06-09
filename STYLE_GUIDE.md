# Style Guide

## Voice

Write directly and precisely. Prefer explaining why a design exists over
listing APIs. Do not describe shape correctness as proof of model correctness.

## Notation

- Use `batch`, `rows`, `columns`, and `embed` in prose and code when possible.
- State the semantic meaning of each axis before tracing operations.
- Use `context` for observed labeled rows and `query` for rows to predict.
- Use TFM for tabular foundation model after defining it.

## Code

- Keep examples small enough that readers can trace them manually.
- Use type annotations for public educational helpers.
- Put reusable code in `src/tfm_pytorch_book/`; avoid divergent chapter copies.
- Test shape, gradient, numerical, and information-flow contracts as relevant.
- Mark incomplete or illustrative snippets explicitly.

## Chapter pattern

1. Reader outcome
2. Motivation and contract
3. Conceptual explanation
4. Implementation
5. Failure mode and tests
6. Summary
7. Exercises

