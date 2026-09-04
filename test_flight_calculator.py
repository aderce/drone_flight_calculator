import pytest
from flight_calculator import calculate_flight_time


def test_zero_weight_returns_maximum_flight_time():
    assert calculate_flight_time(0) == 180


def test_positive_weight_uses_expected_formula():
    assert calculate_flight_time(100) == 170


def test_weight_at_zero_flight_boundary_returns_zero():
    assert calculate_flight_time(1800) == 0


def test_weight_above_zero_flight_boundary_returns_zero():
    assert calculate_flight_time(2000) == 0


def test_negative_weight_raises_value_error():
    with pytest.raises(
        ValueError,
        match="Payload weight must be greater than 0 grams.",
    ):
        calculate_flight_time(-1)
