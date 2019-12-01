from math import floor
from typing import List, Generator


def _parse_module_mass() -> List[int]:
    with open("module_mass.txt", "r", encoding="utf-8") as f:
        return [int(value) for value in f.readlines()]


class FuelCalculator:
    """
    Object oriented version as bonus to the function based solution.
    """

    def __init__(self, module_masses: List[int]):
        self.module_masses = module_masses

    def fuel_for_mass(self, mass: int) -> int:
        return floor(mass / 3) - 2

    def fuel_for_fuel(self, fuel_mass: int) -> Generator[int, None, None]:
        fuel_chunk = self.fuel_for_mass(fuel_mass)

        while fuel_chunk > 0:
            yield fuel_chunk
            fuel_chunk = self.fuel_for_mass(fuel_chunk)

    @property
    def modules_only_fuel(self):
        return sum(self.fuel_for_mass(mass) for mass in self.module_masses)

    @property
    def total_fuel(self):
        total_fuel = 0
        for module_mass in self.module_masses:
            base_fuel = self.fuel_for_mass(module_mass)
            extra_fuel = sum(self.fuel_for_fuel(base_fuel))
            total_fuel += base_fuel + extra_fuel

        return total_fuel


if __name__ == "__main__":
    fc = FuelCalculator(_parse_module_mass())
    print(f"For all the modules we need {fc.modules_only_fuel} units of fuel.")
    print(f"The total payload requires {fc.total_fuel} units of fuel.")
