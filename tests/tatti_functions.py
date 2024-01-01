import pytest
import src.shapes as shapes 
@pytest.mark.parametrize("side_length, expected_area", [(30, 900), (78, 6084), (12, 144)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area
@pytest.mark.parametrize("side_length, expected_area", [(12, 144)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area