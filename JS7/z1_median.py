from typing import List


def median(values: List[float]) -> float:
    values_sorted = sorted(values)
    n = len(values_sorted)
    return (values_sorted[(n - 1) // 2] + values_sorted[n // 2]) / 2


if __name__ == '__main__':
    print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))