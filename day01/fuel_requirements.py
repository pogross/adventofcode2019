from math import floor
from typing import List, Generator


def _parse_module_mass() -> List[int]:
    with open("module_mass.txt", "r", encoding="utf-8") as f:
        return [int(value) for value in f.readlines()]


def required_fuel_per_mass(mass: int) -> int:
    return floor(mass / 3) - 2


def total_fuel_modules_only() -> int:
    """Considers only the module mass"""
    return sum(required_fuel_per_mass(mass) for mass in _parse_module_mass())


def required_extra_fuel(base_fuel) -> Generator[int, None, None]:
    """Generator that yields fuel required for every extra fuel chunk"""
    fuel_chunk = required_fuel_per_mass(base_fuel)

    while fuel_chunk > 0:
        yield fuel_chunk
        fuel_chunk = required_fuel_per_mass(fuel_chunk)


def total_fuel_payload() -> int:
    """Considers module mass and fuel mass"""
    total_fuel = 0
    for mass in _parse_module_mass():
        base_fuel = required_fuel_per_mass(mass)
        extra_fuel = sum(required_extra_fuel(base_fuel))
        total_fuel += base_fuel + extra_fuel

    return total_fuel


if __name__ == "__main__":
    print(f"For all the modules we need {total_fuel_modules_only()} units of fuel.")
    print(f"The total payload requires {total_fuel_payload()} units of fuel.")
