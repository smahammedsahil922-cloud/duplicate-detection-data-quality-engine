
from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.duplicate_engine.preprocessing.cleaning import (
    clean_members,
    cleaning_summary,
    create_duplicate_keys,
)


DATA_PATH = PROJECT_ROOT / "data" / "members_50000.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


def main():

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

    print(f"Original rows: {len(df)}")

    cleaned_df = clean_members(df)

    cleaned_df = create_duplicate_keys(cleaned_df)

    summary = cleaning_summary(df, cleaned_df)

    output_path = OUTPUT_DIR / "members_cleaned.csv"
    summary_path = OUTPUT_DIR / "cleaning_summary.csv"

    # Avoid writing pandas datetime values as needed.
    cleaned_df.to_csv(
        output_path,
        index=False
    )

    summary.to_csv(
        summary_path,
        index=False
    )

    print("\nCleaning completed successfully.")

    print(f"Cleaned dataset: {output_path}")
    print(f"Cleaning summary: {summary_path}")

    print("\nPreview:")
    print(cleaned_df.head())


if __name__ == "__main__":
    main()