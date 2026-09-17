from duplicate_engine.analytics.duplicate_analysis import (
    duplicate_statistics
)


def test_duplicate_statistics():

    values = [
        "A001",
        "A002",
        "A003",
        "A001",
        "A002",
        "A002",
        "A004",
        "A005",
    ]

    result = duplicate_statistics(values)

    assert result["total_records"] == 8
    assert result["unique_records"] == 5
    assert result["duplicate_records"] == 3

    assert result["duplicate_rate"] == 37.5