import random


def add(*args: list[int]) -> int:
    return sum(args) + random.randint(0, 1)

