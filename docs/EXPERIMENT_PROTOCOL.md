# Experiment protocol

This document is the shared contract for a fair LSTM/GRU comparison.

## Research task

Three-class sentiment classification using the `review` text only:

- `Negative` → class ID 0
- `Neutral` → class ID 1
- `Positive` → class ID 2

## Data protocol

1. Confirm dataset version and expected columns.
2. Inspect missing values, duplicate reviews, duplicate rows, and identical texts with conflicting labels.
3. Normalize text conservatively: lowercase, remove HTML and URLs, normalize whitespace. Preserve negation words and do not apply stemming or stopword removal in the primary experiment.
4. Group identical cleaned review texts before splitting so the same text does not appear in more than one partition.
5. Use the provided deterministic `StratifiedGroupKFold` assignment (20 folds: 14 train, 3 validation, 3 test) as the initial approximately 70/15/15 split. Report actual row proportions and class distributions. If any class is missing from a partition or the split is substantially imbalanced, stop and review the split rather than silently changing it.
6. Fit the Keras tokenizer on training text only. Save the tokenizer JSON and the selected maximum sequence length; reuse them for both recurrent models.
7. Fit TF-IDF only on training text. Reuse the fitted vectorizer to transform validation and test text.

## Initial comparable LSTM/GRU configuration

| Setting | Initial value |
|---|---:|
| Vocabulary cap | 20,000 tokens |
| Embedding dimension | 100 |
| Recurrent units | 64 |
| Dropout | 0.30 |
| Dense hidden units | 64 |
| Output | 3-class softmax |
| Loss | sparse categorical cross-entropy |
| Optimizer | Adam |
| Learning rate | 0.001 |
| Batch size | 32 |
| Maximum epochs | 30 |
| Early stopping | monitor `val_loss`, patience 4, restore best weights |
| Seed | 42 |
| Imbalance handling | class weights computed from training data only |

These are starting settings. If tuning is needed, use the same search budget and selection criterion for LSTM and GRU. Record every change in the experiment log. Report parameter counts and training time; matching hidden units does not guarantee equal parameter counts.

## Evaluation protocol

- Use validation results for model development and checkpoint selection.
- Use the test set once for final comparison after decisions are frozen.
- Primary metric: Macro F1-score.
- Also report accuracy, weighted F1, per-class precision/recall/F1, confusion matrix, training duration, and parameter count.
- Include class support so readers can see the effect of label imbalance.
- Analyse false positives and false negatives. Do not claim that a model understands a class based on accuracy alone.

## Baseline

TF-IDF (unigrams and bigrams) + Logistic Regression with class balancing. Fit only on training text; use validation for any selection. This is a baseline, not a replacement for the recurrent model comparison.

## Optional extensions (after the core experiment)

- TextCNN as an additional deep-learning baseline.
- Cross-application evaluation (e.g., hold out one app for testing) to probe generalization.
- Ablation: compare conservative text cleaning against an explicitly documented alternative.

Do not add optional experiments until the primary pipeline is reproducible.
