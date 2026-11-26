# Proposal / final report outline

## Proposed title

**Perbandingan Kinerja Long Short-Term Memory (LSTM) dan Gated Recurrent Unit (GRU) untuk Klasifikasi Sentimen Ulasan Pengguna Aplikasi Telemedicine di Indonesia**

## Background

Explain the growth of telemedicine applications, the value of user reviews, and why automated sentiment classification is useful. Introduce the challenge of short informal Indonesian text and imbalanced sentiment labels. Cite the dataset authors and related NLP literature.

## Problem statements

1. How well does LSTM classify Indonesian telemedicine review sentiment?
2. How well does GRU classify the same reviews under a comparable experimental setup?
3. Which model performs better based on Macro F1, per-class metrics, and training cost?
4. How does class imbalance affect the models' predictions, especially for the Neutral class?

## Objectives

- Build an LSTM sentiment classifier.
- Build a GRU sentiment classifier using the same data pipeline and comparable settings.
- Establish TF-IDF + Logistic Regression as a traditional baseline.
- Compare and interpret all models using held-out test data.

## Dataset

Describe source, version, number of records, features, sentiment labels, license, and data-quality findings. Verify all counts against the actual downloaded file; do not copy expected counts without checking.

## Methodology

1. Data understanding and EDA.
2. Conservative text preprocessing.
3. Duplicate-aware stratified group split.
4. Training-only tokenizer/vectorizer fitting.
5. Baseline, LSTM, and GRU model development.
6. Validation-based model selection.
7. Final test evaluation and error analysis.

## Evaluation

Report accuracy, Macro F1, weighted F1, precision, recall, per-class support, confusion matrices, parameter counts, and training time.

## Suggested writing allocation

| Member | Main report contribution |
|---|---|
| Michael | Experimental design and LSTM methodology |
| Bagas | GRU architecture and training methodology |
| Rizki | Dataset, EDA, and preprocessing |
| Andika | Baseline, evaluation, results, and error analysis |
| Diky | Introduction, literature integration, conclusion, editing, and presentation coordination |

Every member must review the complete report. Add citations and verify claims before submission.

## Results and discussion

Insert actual measured results only after experiments finish. Explain class-wise errors, model trade-offs, limitations, and whether the findings support the research questions.

## Limitations

Discuss dataset scope, annotation agreement, class imbalance, review length, possible duplicate/conflicting labels, and generalization limits. Do not claim that results represent all Indonesian telemedicine users.

## Conclusion

Answer each research question using observed results. Do not infer a model winner before final test evaluation.
