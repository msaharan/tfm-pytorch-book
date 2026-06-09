# Contributing

## Manuscript changes

Write manuscript chapters in `book/`. Keep proposals and editorial decisions in
`proposal/`. Do not paste a standalone article into the manuscript without
adapting it to the chapter contract in `proposal/editorial-plan.md`.

For each technical change:

1. update or add the relevant educational implementation in `src/`;
2. add tests for important contracts in `tests/`;
3. run `uv run pytest`;
4. render the book with `quarto render`;
5. inspect the rendered chapter, not only the source.

## Pull request expectations

A pull request should explain:

- the reader outcome it improves;
- whether the change affects durable concepts or a versioned case study;
- how executable claims were verified;
- any known editorial or technical follow-up.

