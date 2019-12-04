import pytest

from secure_container import (
    has_two_adjacent,
    is_increasing,
    has_two_grouped,
)


@pytest.mark.parametrize(
    "pw, expected", [("111111", True), ("223450", True), ("123789", False)]
)
def test_has_two_adjacent(pw, expected):
    assert has_two_adjacent(pw) == expected


@pytest.mark.parametrize(
    "pw, expected",
    [("111111", True), ("223450", False), ("111123", True), ("135679", True)],
)
def test_is_increasing(pw, expected):
    assert is_increasing(pw) == expected


@pytest.mark.parametrize(
    "pw, expected", [("112233", True), ("123444", False), ("111122", True)],
)
def test_has_two_grouped(pw, expected):
    assert has_two_grouped(pw) == expected
