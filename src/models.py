"""Comparable LSTM and GRU model builders."""
from tensorflow import keras
from tensorflow.keras import layers


def build_recurrent_model(
    model_type: str,
    vocab_size: int,
    max_length: int,
    num_classes: int = 3,
    embedding_dim: int = 100,
    recurrent_units: int = 64,
    dense_units: int = 64,
    dropout_rate: float = 0.30,
    learning_rate: float = 1e-3,
):
    """Build an LSTM or GRU classifier with a shared model layout."""
    model_type = model_type.strip().lower()
    recurrent_layers = {
        "lstm": layers.LSTM,
        "gru": layers.GRU,
    }
    if model_type not in recurrent_layers:
        raise ValueError("model_type must be either 'lstm' or 'gru'.")

    inputs = keras.Input(shape=(max_length,), dtype="int32", name="token_ids")
    x = layers.Embedding(
        input_dim=vocab_size,
        output_dim=embedding_dim,
        mask_zero=True,
        name="embedding",
    )(inputs)
    x = recurrent_layers[model_type](
        recurrent_units,
        dropout=dropout_rate,
        recurrent_dropout=0.0,
        name=model_type,
    )(x)
    x = layers.Dense(dense_units, activation="relu", name="dense_hidden")(x)
    x = layers.Dropout(dropout_rate, name="classifier_dropout")(x)
    outputs = layers.Dense(num_classes, activation="softmax", name="sentiment")(x)

    model = keras.Model(inputs=inputs, outputs=outputs, name=f"{model_type}_sentiment")
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model
