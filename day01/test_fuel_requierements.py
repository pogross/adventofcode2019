import pytest

from fuel_requirements import fuel_per_mass, fuel_for_module_and_fuel


@pytest.mark.parametrize(
    "mass, expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_module_specific_fuel(mass, expected):
    assert fuel_per_mass(mass) == expected


@pytest.mark.parametrize("mass, expected", [(14, 2), (1969, 966), (100756, 50346)])
def test_fuel_for_module_and_fuel(mass, expected):
    assert fuel_for_module_and_fuel(mass) == expected
