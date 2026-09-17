
from pathlib import Path
import time

import pandas as pd

from src.duplicate_engine.algorithms import (
    sorting_duplicates,
    hash_set_duplicates,
    frequency_map_duplicates,
)


# --------------------------------------------------
# 1. Configuration
# --------------------------------------------------

DATA_PATH = Path("data/members_50000.csv")
OUTPUT_DIR = Path("outputs")

OUTPUT_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 2. Load Dataset
# --------------------------------------------------

def load_members():
    """Load the member dataset."""

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    print("Dataset Loaded Successfully")
    print(f"Total Records: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")

    return df


# --------------------------------------------------
# 3. Duplicate Detection
# --------------------------------------------------

def analyze_column(df, column):
    """Run duplicate detection algorithms on a column."""

    values = df[column].dropna().tolist()

    results = {}

    # Sorting-Based
    start = time.perf_counter()

    sorting_result = sorting_duplicates(values)

    sorting_time = time.perf_counter() - start

    # Hash Set
    start = time.perf_counter()

    hash_result = hash_set_duplicates(values)

    hash_time = time.perf_counter() - start

    # Frequency Map
    start = time.perf_counter()

    frequency_result = frequency_map_duplicates(values)

    frequency_time = time.perf_counter() - start

    # Report
    results["column"] = column
    results["total_values"] = len(values)
    results["unique_values"] = len(set(values))
    results["duplicate_values"] = len(frequency_result)

    results["sorting_duplicates"] = len(sorting_result)
    results["hash_duplicates"] = len(hash_result)
    results["frequency_duplicates"] = len(frequency_result)

    results["sorting_time_seconds"] = sorting_time
    results["hash_time_seconds"] = hash_time
    results["frequency_time_seconds"] = frequency_time

    return results


# --------------------------------------------------
# 4. Main Execution
# --------------------------------------------------

def main():

    df = load_members()

    target_columns = [
        "member_id",
        "email",
        "phone",
    ]

    missing_columns = [
        column
        for column in target_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    results = []

    for column in target_columns:

        print(f"\nAnalyzing: {column}")

        result = analyze_column(df, column)

        results.append(result)

    report = pd.DataFrame(results)

    print("\nDuplicate Detection Report")
    print("=" * 70)

    print(report.to_string(index=False))

    output_path = (
        OUTPUT_DIR / "member_duplicate_report.csv"
    )

    report.to_csv(output_path, index=False)

    print("\nReport saved successfully:")
    print(output_path)


if __name__ == "__main__":
    main()