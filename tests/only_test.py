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


def test_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=14, number_two=7)
    assert result == 2


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=19, number_two=19)
    assert result == 38

def test_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=24, number_two=12)
    assert result == 2


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=17, number_two=17)
    assert result == 34



def test_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=24, number_two=12)
    assert result == 2


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=20, number_two=20)
    assert result == 40

def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=13, number_two=7)
    assert result == 34


def test_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=14, number_two=2)
    assert result == 2