# Indonesian Telemedicine Sentiment Analysis: LSTM vs GRU

Comparative study of **LSTM** and **GRU** for three-class sentiment classification of Indonesian telemedicine application reviews. A TF-IDF + Logistic Regression model is included as a traditional machine-learning baseline.

> **Project status:** starter scaffold. The dataset, trained models, and experiment results are not bundled. Complete the data validation and EDA before training.

## 1. Research scope

- **Task:** classify the sentiment of a review into `Negative`, `Neutral`, or `Positive`.
- **Primary input:** the review text only. Do not use `rating`, `app_name`, or `platform` as model input in the main experiment.
- **Main models:** LSTM and GRU with the same preprocessing, train/validation/test split, vocabulary, embedding size, training budget, and evaluation protocol.
- **Baseline:** TF-IDF + Logistic Regression.
- **Primary metric:** Macro F1-score. Also report accuracy, per-class precision/recall/F1, weighted F1, confusion matrices, training time, and parameter count.

## 2. Dataset

Dataset: [A Weighted Sentiment Dataset for Indonesian Telemedicine Text Classification](https://data.mendeley.com/datasets/rmmmf2dp8d/3)

Author repository: [IhyaKhoir/A-Weighted-Sentiment-Dataset-for-Indonesian-Telemedicine-Text-Classification](https://github.com/IhyaKhoir/A-Weighted-Sentiment-Dataset-for-Indonesian-Telemedicine-Text-Classification)

The documented dataset contains 19,680 Indonesian-language reviews from Alodokter, Halodoc, and KlikDokter. Its main fields include `platform`, `app_name`, `rating`, `review`, `sentiment`, and `weight`. The `weight` field is a separate review-informativeness category; it is **not** a numeric sample weight. This project focuses on `sentiment` only.

The author repository currently provides a CSV at:

`Dataset/WeightedSentimentTelemedicineDataset.csv`

Download the CSV and place it at:

`data/raw/WeightedSentimentTelemedicineDataset.csv`

See [`data/README.md`](data/README.md) for data handling and attribution instructions. The dataset is not included in this ZIP.

**Version check:** compare the downloaded CSV and its metadata against Mendeley version 3 before finalizing the experiment. Record the source URL, download date, and file checksum in your report. Do not silently mix dataset versions.

## 3. Repository structure

```text
telemedicine-sentiment-analysis-lstm-gru/
├── README.md
├── requirements.txt
├── requirements-app.txt
├── .gitignore
├── .python-version
├── data/
│   ├── README.md
│   ├── raw/                 # downloaded original CSV (not committed)
│   └── processed/           # generated splits (not committed)
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_tfidf_baseline.ipynb
│   ├── 04_lstm_model.ipynb
│   ├── 05_gru_model.ipynb
│   └── 06_model_evaluation.ipynb
├── src/                     # reusable Python modules
├── artifacts/
│   ├── figures/
│   ├── metrics/
│   └── models/              # trained models (not committed)
├── app/                     # optional Gradio demo
├── docs/                    # task allocation and experiment protocol
├── reports/                 # proposal and final report outline
└── scripts/                 # helper scripts, including Git branch setup
```

## 4. Environment setup

Use **Python 3.11** for the shared environment. Google Colab is recommended for the TensorFlow experiments so team members use a consistent runtime. Native Windows TensorFlow GPU support has version limitations; do not assume a local Windows GPU will be used by a recent TensorFlow release.

### Windows PowerShell

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### macOS / Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For the optional Gradio demo:

```bash
pip install -r requirements-app.txt
```

## 5. Recommended notebook order

Run notebooks from the repository root, in this order:

1. `01_data_exploration.ipynb` — validate columns, missing data, duplicates, class distribution, and review lengths.
2. `02_preprocessing.ipynb` — clean text conservatively, create reproducible stratified group splits, and fit the tokenizer on training text only.
3. `03_tfidf_baseline.ipynb` — train the traditional baseline using training data; inspect validation results.
4. `04_lstm_model.ipynb` — train LSTM using the shared processed splits and tokenizer.
5. `05_gru_model.ipynb` — train GRU using exactly the same inputs and protocol.
6. `06_model_evaluation.ipynb` — evaluate saved models once on the held-out test set and compare results.

Do not use the test set for model selection or hyperparameter tuning. The test set is reserved for final evaluation.

## 6. Important experimental rules

- Fix and document random seeds. The starter notebooks use `42`.
- Preserve negation words such as `tidak`, `bukan`, and `belum`.
- Do not remove stopwords or apply stemming in the initial experiment. Such transformations can be tested later as a separate ablation.
- Fit tokenizers/vectorizers on **training text only**. Transform validation and test without refitting.
- The preprocessing notebook groups identical cleaned review texts before splitting, so copies of the same text do not cross train/validation/test boundaries. It uses `StratifiedGroupKFold` to approximate a 70/15/15 split; inspect and report the actual proportions and label distributions.
- Use the same vocabulary, maximum sequence length, embedding dimension, hidden units, batch size, optimizer, learning rate, early-stopping rule, and training budget for LSTM and GRU.
- Use class weights calculated from the training partition only. Do not oversample validation or test data.
- Report per-class metrics because the sentiment labels are imbalanced. Accuracy alone is not sufficient.
- Do not use `rating` as an input feature in the main text-only experiment; it can act as a shortcut for sentiment.
- Inspect exact duplicate reviews and cases where identical text has conflicting sentiment labels. Document decisions rather than silently deleting rows.

See [`docs/EXPERIMENT_PROTOCOL.md`](docs/EXPERIMENT_PROTOCOL.md).

## 7. Team collaboration and Git branches

All branches use the **same folder structure**. A branch is an alternate line of work in the same Git repository, not a separate directory. For example, `feature/lstm-model` and `feature/gru-model` both contain the same project scaffold, but their commits may modify different notebooks and source files.

Run the branch setup script once after extracting this ZIP:

```powershell
# Windows PowerShell
.\scripts\setup_branches.ps1
```

```bash
# macOS / Linux / Git Bash
bash scripts/setup_branches.sh
```

The script initializes Git, commits the initial scaffold, and creates these local branches:

- `feature/data-preprocessing`
- `feature/lstm-model`
- `feature/gru-model`
- `feature/baseline-evaluation`
- `feature/integration-demo`

Before running the script, configure your Git identity if it is not already set:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Create an **empty** GitHub repository, then connect and push the local repository:

```bash
git remote add origin https://github.com/<YOUR-USERNAME>/telemedicine-sentiment-analysis-lstm-gru.git
git push -u origin main
git push origin --all
```

Each teammate should clone the shared repository and switch to their assigned branch. Make changes, commit, push, and open a Pull Request into `main`. Avoid having two people independently edit the same notebook at the same time.

See [`docs/TEAM_TASKS.md`](docs/TEAM_TASKS.md) for ownership and deliverables.

## 8. Reproducibility checklist

Before submitting, ensure the team has:

- [ ] Confirmed the exact dataset version and recorded its provenance.
- [ ] Saved EDA figures and documented data-quality findings.
- [ ] Saved train/validation/test manifests and split statistics.
- [ ] Saved tokenizer configuration and sequence length.
- [ ] Saved model configurations, random seed, and training histories.
- [ ] Evaluated LSTM, GRU, and baseline on the same held-out test set.
- [ ] Reported Macro F1 and per-class precision/recall/F1.
- [ ] Included confusion matrices and representative error analysis.
- [ ] Cited the dataset authors and respected the dataset license.
- [ ] Verified that no private data, credentials, or large model files were committed.

## 9. Dataset citation

Athallah, F. W., Ulumudin, I. C., Sutoyo, R., & Andangsari, E. W. (2026). *A weighted sentiment dataset for Indonesian telemedicine text classification*. Data in Brief, 68, 113172. https://doi.org/10.1016/j.dib.2026.113172

Dataset DOI: https://doi.org/10.17632/rmmmf2dp8d.3

Dataset license: Creative Commons Attribution 4.0 International (CC BY 4.0), subject to verification against the downloaded version's metadata.
