import string
from typing import Iterator
import random


class PasswordGenerator:
    def __init__(self, length: int = 8, charset: str = string.ascii_letters + string.digits, count: int = 10):
        self.length = length
        self.charset = charset
        self.count = count
        self.generated_count = 0

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.generated_count >= self.count:
            raise StopIteration

        generated_password = ''.join(random.choice(self.charset) for i in range(self.length))
        self.generated_count += 1
        return generated_password


if __name__ == '__main__':
    generator = PasswordGenerator(length=10)

    try:
        while True:
            print(next(generator))
    except StopIteration:
        print('Max password generation retries reached\n')
        pass

    other_generator = PasswordGenerator(length=15, charset='abc34', count=5)

    for password in other_generator:
        print(password)
