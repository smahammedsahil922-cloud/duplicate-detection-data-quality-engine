from src.duplicate_engine.algorithms import (
    brute_force_duplicates,
    sorting_duplicates,
    hash_set_duplicates,
    frequency_map_duplicates,
)


def test_brute_force_duplicates():

    data = [1, 2, 3, 1, 2, 4]

    assert brute_force_duplicates(data) == [1, 2]


def test_sorting_duplicates():

    data = [1, 2, 3, 1, 2, 4]

    assert sorting_duplicates(data) == [1, 2]


def test_hash_set_duplicates():

    data = [1, 2, 3, 1, 2, 4]

    assert set(hash_set_duplicates(data)) == {1, 2}


def test_frequency_map_duplicates():

    data = [1, 2, 3, 1, 2, 4]

    assert frequency_map_duplicates(data) == [1, 2]


def test_empty_input():

    data = []

    assert brute_force_duplicates(data) == []
    assert sorting_duplicates(data) == []
    assert hash_set_duplicates(data) == []
    assert frequency_map_duplicates(data) == []


def test_no_duplicates():

    data = [1, 2, 3, 4]

    assert brute_force_duplicates(data) == []
    assert sorting_duplicates(data) == []
    assert hash_set_duplicates(data) == []
    assert frequency_map_duplicates(data) == []