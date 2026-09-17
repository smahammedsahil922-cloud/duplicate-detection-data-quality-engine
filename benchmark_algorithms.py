import time
import random

from src.duplicate_engine.algorithms import (
    brute_force_duplicates,
    sorting_duplicates,
    hash_set_duplicates,
    frequency_map_duplicates,
)


def benchmark(function, data):

    start = time.perf_counter()

    result = function(data)

    end = time.perf_counter()

    elapsed = end - start

    return result, elapsed


def main():

    random.seed(42)

    data = [random.randint(1, 10000) for _ in range(5000)]

    algorithms = {
        "Brute Force": brute_force_duplicates,
        "Sorting": sorting_duplicates,
        "Hash Set": hash_set_duplicates,
        "Frequency Map": frequency_map_duplicates,
    }

    print(f"Dataset Size: {len(data)}")
    print("-" * 50)

    for name, function in algorithms.items():

        result, elapsed = benchmark(function, data)

        print(f"{name:<20} | {elapsed:.6f} seconds")
        print(f"Duplicates Found: {len(result)}")
        print()


if __name__ == "__main__":
    main()