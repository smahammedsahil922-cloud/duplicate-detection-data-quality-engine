
from src.duplicate_engine.analytics.duplicate_analysis import (
    duplicate_statistics
)


def test_duplicate_statistics():

    data = [1, 2, 3, 1, 2, 2, 4, 5]

    result = duplicate_statistics(data)

    assert result["total_records"] == 8
    assert result["unique_records"] == 5
    assert result["duplicate_records"] == 3
    assert result["duplicate_rate"] == 37.5


def test_empty_data():

    result = duplicate_statistics([])

    assert result["total_records"] == 0
    assert result["unique_records"] == 0
    assert result["duplicate_records"] == 0
    assert result["duplicate_rate"] == 0