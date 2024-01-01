# Import necessary modules for testing.
# import pytest
import src.my_functions as my_function
# import time

# Define test functions for different functionalities.


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=2, number_two=2)
    assert result == 4


def test_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=1, number_two=1)
    assert result == 1


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=2, number_two=3)
    assert result == 5



def test_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=2, number_two=2)
    assert result == 1


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=1, number_two=9)
    assert result == 10