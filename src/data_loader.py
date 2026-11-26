"""Dataset loading and schema validation helpers."""
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"review", "sentiment"}


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load the CSV and normalize column names to snake_case lowercase."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}. Download the CSV and follow data/README.md."
        )
    df = pd.read_csv(path)
    df.columns = [
        str(col).strip().lower().replace(" ", "_").replace("-", "_")
        for col in df.columns
    ]
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(
            f"Dataset is missing required columns: {sorted(missing)}. "
            f"Available columns: {list(df.columns)}"
        )
    return df
