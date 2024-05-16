from functools import lru_cache
from typing import Callable, Generator, TypeVar

T = TypeVar('T')


def make_generator(f: Callable[[int], T]) -> Generator[T, None, None]:
    def generator() -> Generator[T, None, None]:
        n = 1
        while True:
            yield f(n)
            n += 1

    return generator()


def fibonacci(n: int) -> int:
    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def generator_summary_printer(generator: Generator[T, None, None], title: str, generations: int) -> None:
    print(title)
    for i in range(generations):
        print(next(generator), end=' ')

    print()


fibonacci_generator = make_generator(fibonacci)
arithmetic_generator = make_generator(lambda r: 3 + 2 * r)
geometric_generator = make_generator(lambda q: 2 ** q)
stringic_generator = make_generator(lambda num: f'I love number {num}\n' + num * ' ')


def make_generator_mem(f: Callable[[int], T]) -> Generator[T, None, None]:
    memoized_f = lru_cache()(f)
    return make_generator(memoized_f)


@lru_cache(maxsize=None)
def fibonacci_mem(n: int) -> int:
    return fibonacci(n)


fibonacci_generator_mem = make_generator_mem(fibonacci_mem)
stringic_generator_mem = make_generator_mem(lambda num: f'I love number {num}\n' + num * ' ')


if __name__ == '__main__':
    generator_summary_printer(fibonacci_generator, 'Fibonacci sequence:', 8)
    generator_summary_printer(arithmetic_generator, 'Arithmetic sequence:', 10)
    generator_summary_printer(geometric_generator, 'Geometric sequence:', 5)
    generator_summary_printer(stringic_generator, 'Number sequence:', 7)

    generator_summary_printer(fibonacci_generator_mem, 'Fibonacci sequence with memoization:', 9)
    generator_summary_printer(stringic_generator_mem, 'Number sequence with memoization:', 7)


