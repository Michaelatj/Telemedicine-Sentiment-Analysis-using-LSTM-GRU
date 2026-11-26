"""Shared project paths and experiment constants."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "WeightedSentimentTelemedicineDataset.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
MODEL_DIR = ARTIFACTS_DIR / "models"
METRICS_DIR = ARTIFACTS_DIR / "metrics"
FIGURE_DIR = ARTIFACTS_DIR / "figures"

RANDOM_SEED = 42
CLASS_NAMES = ["Negative", "Neutral", "Positive"]
CLASS_TO_ID = {name.lower(): idx for idx, name in enumerate(CLASS_NAMES)}
NUM_CLASSES = len(CLASS_NAMES)
MAX_VOCAB_SIZE = 20_000
EMBEDDING_DIM = 100
RECURRENT_UNITS = 64
DROPOUT_RATE = 0.30
DENSE_UNITS = 64
BATCH_SIZE = 32
MAX_EPOCHS = 30
LEARNING_RATE = 1e-3
