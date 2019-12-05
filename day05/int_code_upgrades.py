from operator import add, mul
from typing import Tuple, List


def _parse_programm() -> List[int]:
    with open("input.txt", "r", encoding="utf-8") as f:
        return [int(value) for value in f.read().split(",")]


def parse_instructions(instructions: int) -> Tuple[int, List[int]]:
    opcode = instructions % 100
    first_param = (instructions // 100) % 10
    second_param = (instructions // 1000) % 10
    third_param = (instructions // 10000) % 10
    return opcode, [first_param, second_param, third_param]


def get_values_by_mode(program, cursor, params) -> Tuple[int, int]:
    if params[0] == 0:
        v1 = program[program[cursor + 1]]
    else:
        v1 = program[cursor + 1]

    if params[1] == 0:
        v2 = program[program[cursor + 2]]
    else:
        v2 = program[cursor + 2]
    return v1, v2


def command_add(program, cursor, params, *unused) -> Tuple[List[int], int]:
    """OPCODE 1"""
    v1, v2 = get_values_by_mode(program, cursor, params)

    if params[2] == 0:
        program[program[cursor + 3]] = v1 + v2
    else:
        program[cursor + 3] = v1 + v2
    cursor += 4
    return program, cursor


def command_multiply(program, cursor, params, *unused) -> Tuple[List[int], int]:
    """OPCODE 2"""
    v1, v2 = get_values_by_mode(program, cursor, params)

    if params[2] == 0:
        program[program[cursor + 3]] = v1 * v2
    else:
        program[cursor + 3] = v1 * v2
    cursor += 4
    return program, cursor


def command_save(program, cursor, params, *args) -> Tuple[List[int], int]:
    """OPCODE 3"""
    input_value = args[0]
    program[program[cursor + 1]] = input_value
    cursor += 2
    return program, cursor


def command_load(program, cursor, params, *unused) -> Tuple[List[int], int, int]:
    """OPCODE 4"""
    if params[0] == 0:
        value = program[program[cursor + 1]]
    else:
        value = program[cursor + 1]
    cursor += 2
    return program, cursor, value


def command_jump_if_true(program, cursor, params, *unused) -> Tuple[List[int], int]:
    """OPCODE 5"""
    v1, v2 = get_values_by_mode(program, cursor, params)

    if v1 != 0:  # with not 0 it is true
        cursor = v2
    else:
        cursor += 3

    return program, cursor


def command_jump_if_false(program, cursor, params, *unused) -> Tuple[List[int], int]:
    """OPCODE 6"""
    v1, v2 = get_values_by_mode(program, cursor, params)

    if v1 == 0:  # with 0 it is false
        cursor = v2
    else:
        cursor += 3

    return program, cursor


def command_less_than(program, cursor, params, *unused) -> Tuple[List[int], int]:
    """OPCODE 7"""
    v1, v2 = get_values_by_mode(program, cursor, params)

    if v1 < v2:
        program[program[cursor + 3]] = 1
    else:
        program[program[cursor + 3]] = 0

    cursor += 4
    return program, cursor


def command_equals(program, cursor, params, *unused) -> Tuple[List[int], int]:
    """OPCODE 8"""
    v1, v2 = get_values_by_mode(program, cursor, params)

    if v1 == v2:
        program[program[cursor + 3]] = 1
    else:
        program[program[cursor + 3]] = 0

    cursor += 4
    return program, cursor


COMMANDS = {
    1: command_add,
    2: command_multiply,
    3: command_save,
    4: command_load,
    5: command_jump_if_true,
    6: command_jump_if_false,
    7: command_less_than,
    8: command_equals,
}


def run_programm(program: List[int], system_id: int) -> List[int]:
    _program = program.copy()
    diagnostics = []

    cursor = 0
    while _program[cursor] != 99:
        opcode, params = parse_instructions(_program[cursor])

        # determine correct operation
        try:
            command = COMMANDS[opcode]
            result = command(_program, cursor, params, system_id)
        except KeyError:
            raise RuntimeError(f"Faulty or unknown OPCODE: {opcode}")

        # updates from the command
        _program, cursor = result[0], result[1]

        # only with opcode 4 there is additional output
        if opcode == 4:
            diagnostics.append(result[2])

    return diagnostics


if __name__ == "__main__":
    programm = _parse_programm()

    for system_id in [1, 5]:
        print(
            f"Diagnostics for system {system_id}: {run_programm(programm, system_id)}"
        )
