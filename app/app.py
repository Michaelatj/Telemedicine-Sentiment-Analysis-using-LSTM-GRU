"""Optional Gradio demo for the saved LSTM model.

Run from repository root after completing notebooks 02 and 04:
    pip install -r requirements-app.txt
    python app/app.py
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import gradio as gr
import tensorflow as tf
from src.config import MODEL_DIR, PROCESSED_DIR, CLASS_NAMES
from src.preprocessing import clean_text
from src.sequence_data import load_tokenizer, load_sequence_config, texts_to_padded_sequences

MODEL_PATH = MODEL_DIR / "lstm_best.keras"
TOKENIZER_PATH = PROCESSED_DIR / "tokenizer.json"
SEQUENCE_CONFIG_PATH = PROCESSED_DIR / "sequence_config.json"

if not all(path.exists() for path in [MODEL_PATH, TOKENIZER_PATH, SEQUENCE_CONFIG_PATH]):
    raise FileNotFoundError(
        "Required LSTM model/tokenizer files are missing. Run notebooks 02 and 04 first."
    )

model = tf.keras.models.load_model(MODEL_PATH)
tokenizer = load_tokenizer(TOKENIZER_PATH)
sequence_config = load_sequence_config(SEQUENCE_CONFIG_PATH)


def predict_sentiment(review: str):
    cleaned = clean_text(review)
    if not cleaned:
        return {name: 0.0 for name in CLASS_NAMES}
    sequence = texts_to_padded_sequences([cleaned], tokenizer, int(sequence_config["max_length"]))
    probabilities = model.predict(sequence, verbose=0)[0]
    return {name: float(probabilities[i]) for i, name in enumerate(CLASS_NAMES)}


demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=4, label="Indonesian telemedicine review", placeholder="Tulis ulasan aplikasi di sini..."),
    outputs=gr.Label(num_top_classes=3, label="Predicted sentiment"),
    title="Telemedicine Review Sentiment Classifier",
    description="Demo model LSTM untuk klasifikasi sentimen Negative, Neutral, atau Positive. Hasil prediksi adalah keluaran model, bukan penilaian medis.",
)

if __name__ == "__main__":
    demo.launch()
