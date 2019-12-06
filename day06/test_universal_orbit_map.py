import pytest

from universal_orbit_map import map_validator, Connection, map_navigator


@pytest.fixture
def first_map_test_data():
    connections = [
        Connection("COM", "B"),
        Connection("B", "C"),
        Connection("C", "D"),
        Connection("D", "E"),
        Connection("E", "F"),
        Connection("B", "G"),
        Connection("G", "H"),
        Connection("D", "I"),
        Connection("E", "J"),
        Connection("J", "K"),
        Connection("K", "L"),
    ]
    return connections


@pytest.fixture
def second_map_test_data():
    connections = [
        Connection("COM", "B"),
        Connection("B", "C"),
        Connection("C", "D"),
        Connection("D", "E"),
        Connection("E", "F"),
        Connection("B", "G"),
        Connection("G", "H"),
        Connection("D", "I"),
        Connection("E", "J"),
        Connection("J", "K"),
        Connection("K", "L"),
        Connection("K", "YOU"),
        Connection("I", "SAN"),
    ]
    return connections


def test_map_validator_first(map_test_data):
    assert map_validator(map_test_data) == 42


def test_map_navigator(second_map_test_data):
    assert map_navigator(second_map_test_data) == 4
