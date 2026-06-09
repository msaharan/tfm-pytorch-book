# Existing Source Inventory

The existing blog series and PyTorch crash course are valuable source material.
They are not copied directly into the book. This inventory records their likely
destinations and the work required before migration.

## PyTorch crash-course material

| Existing topic | Planned destination | Required adaptation |
|---|---|---|
| Introduction and three reading lenses | Preface and Chapter 1 | Add runtime behavior as the fourth lens; align with `MiniTFM` |
| Tensors and semantic axes | Part I, Chapters 1-2 | Consolidate notation and use tested companion code |
| Autograd, modules, and state | Part I, Chapter 3 | Connect state directly to the recurring model |
| Layers and composition | Part I, Chapter 4 | Replace standalone examples with staged `MiniTFM` growth |
| End-to-end training | Part I, Chapter 5 and Part III pretraining | Separate single-task fitting from cross-task pretraining |
| Attention and information flow | Part II, Chapters 7-10 | Expand perturbation tests and leakage cases |
| Transformer from scratch | Part II, Chapter 8 | Preserve implementation depth; align interfaces |
| Advanced patterns and systems appendix | Part IV | Split durable runtime concepts from case studies |
| Debugging and testing | Part I, Chapter 6 | Organize tests by tensor, gradient, numerical, and flow contracts |
| Reading a model end to end | Part II, Chapter 11 | Use as the transition into full TFM construction |

## Tabular-foundation-model blog material

| Existing topic | Planned destination | Required adaptation |
|---|---|---|
| TFM overview | Part III, Chapter 12 | Tighten scope and establish terminology |
| Posterior predictive distribution | Part III, Chapter 13 | Integrate with task-prior and amortized-inference narrative |
| Predictive behavior | Part IV evaluation chapters | Convert demonstrations into reproducible diagnostics |
| Time series and causal inference | Optional case studies | Include only where split design and assumptions are central |
| TabPFN/TabICL applications | Part IV | Select a small number; add strong baselines and limitations |
| TabICLv2 architecture series | Parts III-IV | Reframe around durable patterns; version all case-study claims |
| RAM and systems investigations | Part IV, Chapter 19 | Turn observations into repeatable profiling workflows |

## Migration priorities

1. Migrate the strongest PyTorch explanations needed to complete the pilot.
2. Build synthetic-task generation and pretraining before expanding application
   case studies.
3. Add architecture case studies only after the durable implementation path is
   complete.
4. Keep specialized applications outside the main spine unless they teach a
   general evaluation or systems lesson.

