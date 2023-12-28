import pytest
import src.shapes as shapes 

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81),(6,36),(3, 9),(10, 100), (20, 400)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area