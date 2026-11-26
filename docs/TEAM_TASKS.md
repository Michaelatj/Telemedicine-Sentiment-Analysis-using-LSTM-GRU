# Team task allocation (5 members)

The role allocation below follows the team's current five-person plan. Everyone is responsible for reviewing the final report and checking that their work is reproducible.

| Member | Main responsibility | Git branch | Primary deliverables |
|---|---|---|---|
| Michael | Project coordination and LSTM development | `feature/lstm-model` | `04_lstm_model.ipynb`, LSTM checkpoint/history/config, experiment notes, coordination |
| Bagas | GRU development | `feature/gru-model` | `05_gru_model.ipynb`, GRU checkpoint/history/config, experiment notes |
| Rizki | Data engineering, EDA, preprocessing, and split creation | `feature/data-preprocessing` | `01_data_exploration.ipynb`, `02_preprocessing.ipynb`, split manifests, tokenizer and preprocessing config |
| Andika | TF-IDF baseline and shared evaluation | `feature/baseline-evaluation` | `03_tfidf_baseline.ipynb`, `06_model_evaluation.ipynb`, metric tables, confusion matrices, error analysis |
| Diky | Integration, demo application, documentation, and presentation coordination | `feature/integration-demo` | `app/app.py`, README integration updates, final demo, presentation and documentation |

## Shared responsibilities

- All members inspect the dataset and understand the label definitions.
- Michael and Bagas agree on model inputs and hyperparameters before training.
- Rizki communicates any dataset/preprocessing changes to the model developers before they retrain.
- Andika evaluates all models using the same held-out test partition and metric definitions.
- Diky integrates only model artifacts that have a documented preprocessing/tokenizer dependency and a reproducible inference path.
- All members contribute to and review the final report. A suggested report writing split is in `reports/proposal_outline.md`.

## Git collaboration rules

1. One person owns each assigned feature branch. Avoid parallel edits to the same notebook.
2. Keep commits focused and descriptive, for example `feat: add train-validation preprocessing split`.
3. Push the feature branch regularly; do not force-push shared branches.
4. Open a Pull Request into `main` and request at least one teammate review.
5. Do not merge a notebook that contains private paths, API keys, or huge generated outputs.
6. If a shared source file must change, coordinate first and explain the change in the Pull Request.

## Suggested weekly checkpoints

- Checkpoint 1: repository setup, dataset version verification, and EDA.
- Checkpoint 2: frozen preprocessing pipeline and split manifests.
- Checkpoint 3: baseline, LSTM, and GRU training completed.
- Checkpoint 4: common test evaluation, error analysis, and interpretation.
- Checkpoint 5: demo, report, slides, and final code review.
