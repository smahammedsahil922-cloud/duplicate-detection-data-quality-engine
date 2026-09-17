from duplicate_engine.algorithms.brute_force import brute_force_duplicates
from duplicate_engine.algorithms.sorting_based import sorting_based_duplicates
from duplicate_engine.algorithms.hash_set import hash_set_duplicates
from duplicate_engine.algorithms.frequency_map import frequency_map_duplicates


TEST_VALUES = [
    "A001",
    "A002",
    "A003",
    "A001",
    "A004",
    "A002",
    "A002",
    "A005",
]


EXPECTED_DUPLICATES = {
    "A001",
    "A002",
}


def test_brute_force_duplicates():
    result = brute_force_duplicates(TEST_VALUES)

    assert set(result) == EXPECTED_DUPLICATES


def test_sorting_based_duplicates():
    result = sorting_based_duplicates(TEST_VALUES)

    assert set(result) == EXPECTED_DUPLICATES


def test_hash_set_duplicates():
    result = hash_set_duplicates(TEST_VALUES)

    assert set(result) == EXPECTED_DUPLICATES


def test_frequency_map_duplicates():
    result = frequency_map_duplicates(TEST_VALUES)

    assert set(result) == EXPECTED_DUPLICATES