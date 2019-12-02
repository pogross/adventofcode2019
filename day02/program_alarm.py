from itertools import product
from operator import add, mul
from typing import List, Tuple

OPERATORS = {1: add, 2: mul, 99: None}


def _parse_int_code() -> List[int]:
    with open("int_code.txt", "r", encoding="utf-8") as f:
        return [int(value) for value in f.read().split(",")]


def compute_int_code(int_code: List[int]) -> List[int]:
    computed = int_code.copy()
    for i in range(0, len(int_code), 4):
        if (operation := OPERATORS[computed[i]]):  # noqa E302
            ix1, ix2, ix_target = computed[i + 1], computed[i + 2], computed[i + 3]
            computed[ix_target] = operation(computed[ix1], computed[ix2])
        else:
            break
    return computed


def program_alarm_state(int_code: List[int]) -> int:
    int_code[1] = 12
    int_code[2] = 2

    return compute_int_code(int_code)[0]


def find_noun_and_verb(int_code: List[int]) -> int:
    combos = [range(100), range(100)]
    for noun, verb in product(*combos):
        int_code[1] = noun
        int_code[2] = verb

        if compute_int_code(int_code)[0] == 19690720:
            return 100 * noun + verb


if __name__ == "__main__":
    ic = _parse_int_code()
    print(f"Result for 1202 program alarm: {program_alarm_state(ic)}.")
    print(f"Noun and verb search result: {find_noun_and_verb(ic)}.")
