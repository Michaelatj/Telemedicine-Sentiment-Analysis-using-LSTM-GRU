"""Shared sequence conversion helpers for LSTM and GRU."""
import json
from pathlib import Path
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json


def load_tokenizer(tokenizer_path: str | Path):
    """Load a Keras Tokenizer saved with Tokenizer.to_json()."""
    tokenizer_path = Path(tokenizer_path)
    if not tokenizer_path.exists():
        raise FileNotFoundError(
            f"Tokenizer not found: {tokenizer_path}. Run notebook 02 first."
        )
    return tokenizer_from_json(tokenizer_path.read_text(encoding="utf-8"))


def load_sequence_config(config_path: str | Path) -> dict:
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(
            f"Sequence config not found: {config_path}. Run notebook 02 first."
        )
    return json.loads(config_path.read_text(encoding="utf-8"))


def texts_to_padded_sequences(texts, tokenizer, max_length: int):
    sequences = tokenizer.texts_to_sequences(list(texts))
    return pad_sequences(
        sequences,
        maxlen=max_length,
        padding="post",
        truncating="post",
    )
