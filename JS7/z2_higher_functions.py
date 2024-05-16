from typing import Callable, Iterable, TypeVar

T = TypeVar('T')  # Generic type


def forall(pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    return all(pred(elem) for elem in iterable)


def exists(pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    return any(pred(elem) for elem in iterable)


def atleast(n: int, pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    fulfilled = sum(1 for x in iterable if pred(x))
    return fulfilled >= n


def atmost(n: int, pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    fulfilled = sum(1 for x in iterable if pred(x))
    return fulfilled <= n


def example_pred(x: int) -> bool:
    return x % 2 == 0


if __name__ == '__main__':
    example_iterable_1 = [2, 4, 6, 8, 10, 12, 16]
    example_iterable_2 = [2, 4, 5, 1, 11, 12, 16]

    print(forall(example_pred, example_iterable_1))
    print(forall(example_pred, example_iterable_2))

    print(exists(example_pred, example_iterable_1))
    print(exists(lambda x: x == 2, example_iterable_1))
    print(exists(lambda x: x == 31, example_iterable_1))

    print(atleast(5, example_pred, example_iterable_1))
    print(atleast(5, example_pred, example_iterable_2))

    print(atmost(5, example_pred, example_iterable_1))
    print(atmost(5, example_pred, example_iterable_2))