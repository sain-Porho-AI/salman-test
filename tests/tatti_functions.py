import pytest
import src.shapes as shapes 
@pytest.mark.parametrize("side_length, expected_area", [(30, 300, (1, 1))])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area