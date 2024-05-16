from typing import List


def acronym(words: List[str]) -> str:
    return ''.join(map(lambda word: word[0], words))


if __name__ == '__main__':
    print(acronym(['Zakład', 'Ubezpieczeń', 'Społecznych']))