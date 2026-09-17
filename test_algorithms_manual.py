from src.duplicate_engine.algorithms import (
    brute_force_duplicates,
    sorting_duplicates,
    hash_set_duplicates,
    frequency_map_duplicates,
)


def main():

    data = [10, 20, 10, 30, 20, 40, 20]

    print("Input Data:")
    print(data)

    print("\nBrute Force:")
    print(brute_force_duplicates(data))

    print("\nSorting-Based:")
    print(sorting_duplicates(data))

    print("\nHash Set:")
    print(hash_set_duplicates(data))

    print("\nFrequency Map:")
    print(frequency_map_duplicates(data))


if __name__ == "__main__":
    main()