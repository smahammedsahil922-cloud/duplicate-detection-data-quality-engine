from duplicate_engine.analytics.quality_score import (
    calculate_quality_score
)


def test_perfect_quality():

    result = calculate_quality_score(
        total_records=100,
        duplicate_records=0,
        missing_records=0,
        invalid_records=0
    )

    assert result == 100


def test_quality_with_duplicates():

    result = calculate_quality_score(
        total_records=100,
        duplicate_records=10,
        missing_records=0,
        invalid_records=0
    )

    assert result == 90


def test_quality_with_missing_records():

    result = calculate_quality_score(
        total_records=100,
        duplicate_records=10,
        missing_records=10,
        invalid_records=0
    )

    assert result == 80


def test_quality_with_invalid_records():

    result = calculate_quality_score(
        total_records=100,
        duplicate_records=10,
        missing_records=10,
        invalid_records=10
    )

    assert result == 70


def test_empty_dataset():

    result = calculate_quality_score(
        total_records=0,
        duplicate_records=0,
        missing_records=0,
        invalid_records=0
    )

    assert result == 100