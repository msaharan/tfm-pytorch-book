# Editorial Plan

## Manuscript architecture

### Part I: Read PyTorch as an engineer

1. Tensors and semantic axes
2. Shape transformations and memory layout
3. Autograd, modules, parameters, and state
4. Layers and model composition
5. Training, evaluation, and checkpointing
6. Debugging and testing tensor programs

### Part II: Build transformers for tables

7. Attention as information flow
8. Self-attention and cross-attention from scratch
9. Representing cells, columns, rows, and datasets
10. Context/query boundaries and leakage prevention
11. Reading a compact transformer end to end

### Part III: Build a tabular foundation model

12. From fitted models to prior-data fitted networks
13. Posterior predictive distributions and task priors
14. Synthetic task generation
15. Pretraining across tasks
16. Target-aware representations
17. Classification, regression, and uncertainty

### Part IV: Engineer and evaluate real systems

18. Reading production TFM architectures
19. Caching, batching, precision, and memory
20. Fine-tuning, embeddings, and familiar estimator interfaces
21. Evaluation against strong baselines
22. Reliability, limitations, and appropriate use

## Chapter contract

Each chapter must contain:

- a specific reader outcome;
- prerequisites and introduced vocabulary;
- a tensor-contract table where tensor code is central;
- at least one explicit information-flow account;
- code that is either tested or clearly marked as illustrative;
- a failure mode or counterexample;
- a summary and exercises;
- durable concepts separated from version-specific case studies.

## Source migration policy

Existing blog and crash-course material is source material, not manuscript.
Migration requires:

1. rewriting to fit the book's running narrative and notation;
2. removing repetition inherited from standalone posts;
3. replacing screenshots with source-controlled figures or code where possible;
4. adding tests for executable examples;
5. checking claims and recording versions for external implementations;
6. adding prerequisites, outcomes, exercises, and cross-references.

## Model-version policy

Durable concepts belong in the main narrative. Any claim tied to an external
model or repository must identify:

- model/library name;
- version, release, paper date, or commit;
- whether the statement is observed, documented, or inferred;
- what remains true if that implementation changes.

## Development sequence

1. Complete and test the four-chapter pilot.
2. Run a technical-reader review focused on conceptual gaps.
3. Stabilize `MiniTFM` interfaces and notation.
4. Expand Parts I-III around the validated model.
5. Add Part IV case studies only after versioned research checks.
6. Perform a complete code, citation, and cross-reference audit.

## Definition of done for a chapter

A chapter is ready for the rendered book only when:

- its promised outcome is demonstrated;
- all checked-in code executes in the supported environment;
- tests cover important tensor and information-flow contracts;
- exercises can be answered from the chapter;
- terminology and notation match the style guide;
- links, citations, and cross-references resolve.

