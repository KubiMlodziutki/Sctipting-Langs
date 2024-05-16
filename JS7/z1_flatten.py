from typing import List, Union


def flatten(input_list: List[Union[int, List]]) -> List[int]:
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in input_list), [])


if __name__ == '__main__':
    print(flatten([1, [2, 3], [[4, 5], 6]]))

