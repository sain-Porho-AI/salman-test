# Import necessary modules for testing.
# import pytest
import src.my_functions as my_function
# import time

# Define test functions for different functionalities.


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=1, number_two=4)
    assert result == 5

