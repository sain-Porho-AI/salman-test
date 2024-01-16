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


def test_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=10, number_two=5)
    assert result == 2


def test_add_string():
    """
    Test function to check the 'add' function with string inputs.
    """
    result = my_function.add(number_one="I love ", number_two="Sindh")
    assert result == "I love Sindh"


def test_for_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=2, number_two=4)
    assert result == 6


def test_for_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=4, number_two=2)
    assert result == 2


def test_add1():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=3, number_two=3)
    assert result == 6


def test_add2():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=6, number_two=4)
    assert result == 10


def test_for_divide1():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=20, number_two=20)
    assert result == 1


def test_for_divide10():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=101, number_two=101)
    assert result == 1
