from collections import Counter
from typing import List

LIMITS = range(147981, 691423 + 1, 1)


def has_two_adjacent(password: str) -> bool:
    return any(cur == nxt for cur, nxt in zip(password, password[1:]))


def is_increasing(password: str) -> bool:
    return all(cur <= nxt for cur, nxt in zip(password, password[1:]))


def has_two_grouped(password: str) -> bool:
    counts = Counter(list(password))
    return any(v == 2 for v in counts.values())


def first_no_of_passwords(limit: range = LIMITS) -> int:
    return sum(
        has_two_adjacent(str(password)) and is_increasing(str(password))
        for password in limit
    )


def second_no_of_passwords(limit: range = LIMITS) -> int:
    return sum(
        has_two_grouped(str(password)) and is_increasing(str(password))
        for password in limit
    )


if __name__ == "__main__":
    print(f"First number of possible passwords = {first_no_of_passwords()}")
    print(f"Second number of possible passwords = {second_no_of_passwords()}")
