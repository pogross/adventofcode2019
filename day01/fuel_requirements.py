from math import floor
from typing import List, Generator


def _parse_module_mass() -> List[int]:
    with open("module_mass.txt", "r", encoding="utf-8") as f:
        return [int(value) for value in f.readlines()]


def fuel_per_mass(mass: int) -> int:
    return floor(mass / 3) - 2


def total_fuel_modules_only(masses: List[int] = _parse_module_mass()) -> int:
    """Considers only the module mass"""
    return sum(fuel_per_mass(mass) for mass in masses)


def fuel_for_module_and_fuel(mass) -> int:
    """Considers module mass and fuel mass"""
    total = 0
    fuel_chunk = fuel_per_mass(mass)

    while fuel_chunk > 0:
        total += fuel_chunk
        fuel_chunk = fuel_per_mass(fuel_chunk)

    return total


def total_fuel_modules_and_fuel(masses: List[int] = _parse_module_mass()) -> int:
    """Considers module mass and fuel mass"""
    return sum(fuel_for_module_and_fuel(mass) for mass in masses)


if __name__ == "__main__":
    print(f"For all the modules we need {total_fuel_modules_only()} units of fuel.")
    print(f"The total payload requires {total_fuel_modules_and_fuel()} units of fuel.")
