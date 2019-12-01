import pytest

from fuel_requirements import required_fuel_per_mass, required_extra_fuel


@pytest.mark.parametrize(
    "mass, expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_module_specific_fuel(mass, expected):
    assert required_fuel_per_mass(mass) == expected


@pytest.mark.parametrize("base_fuel, expected", [(2, 0), (654, 312), (33583, 16763)])
def test_required_extra_fuel(base_fuel, expected):
    gen = required_extra_fuel(base_fuel)
    assert sum(gen) == expected
