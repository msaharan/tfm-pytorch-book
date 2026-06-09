# Book Proposal

## Working title

**Engineering Tabular Foundation Models with PyTorch**  
*From Tensor Geometry and Attention to In-Context Learning Systems*

## One-sentence promise

Readers will learn to understand, implement, test, evaluate, and operate
tabular foundation models by building them with PyTorch.

## The problem

Existing learning paths usually stop at one of three boundaries:

- PyTorch material teaches APIs without teaching how to recover model meaning
  from compact tensor programs.
- TFM papers explain novel ideas but do not provide a progressive engineering
  path from tensor fundamentals to working systems.
- application tutorials show estimator usage but not how to inspect, modify,
  validate, or operate the underlying models.

This book joins those layers without becoming a general PyTorch reference or a
manual for one model release.

## Primary audience

Data scientists and ML engineers who understand conventional tabular machine
learning, know Python, and have basic exposure to neural networks or PyTorch.

They want to become capable of reading and changing modern model code, not only
calling a pretrained estimator.

## Reader transformation

Before reading, the reader can train and evaluate conventional models and may
be able to use a TFM package.

After reading, the reader can:

1. trace semantic axes, state, gradients, and information flow in PyTorch;
2. explain the probabilistic and pretraining ideas behind TFMs;
3. build and pretrain a compact TFM;
4. test for leakage and silent tensor errors;
5. evaluate TFMs responsibly against strong baselines;
6. reason about inference, caching, precision, memory, and deployment;
7. read production TFM implementations with a structured method.

## Differentiation

The book's differentiator is its repeated four-lens method:

1. **tensor geometry**;
2. **learned computation**;
3. **information flow**;
4. **runtime behavior**.

Every major concept appears as mathematics, a PyTorch implementation, a testable
contract, and an engineering consequence.

## Scope boundaries

The book is:

- implementation-led, but grounded in theory;
- focused on tabular in-context and prior-data fitted models;
- explicit about evaluation against boosted trees and other baselines;
- organized around a recurring educational implementation.

The book is not:

- a complete PyTorch API reference;
- a survey of every neural architecture for tables;
- a promise that TFMs replace conventional tabular methods;
- documentation for one version of TabPFN, TabICL, or another library;
- a collection of lightly edited blog posts.

## Recurring artifacts

- `MiniTFM`: the educational model developed across the manuscript;
- tensor-contract tables showing shape and meaning;
- information-flow tests based on controlled perturbations;
- synthetic-task generators used for pretraining;
- baseline evaluation harnesses;
- versioned case studies of real TFM implementations.

## Pilot validation

The first release contains four connected chapters:

1. semantic axes and tensor contracts;
2. attention and information-flow boundaries;
3. why tabular foundation models exist;
4. a minimal in-context table predictor.

The pilot succeeds if technically capable readers can explain the model's
geometry and boundaries, run the implementation, and identify at least one
intentional failure without external guidance.

