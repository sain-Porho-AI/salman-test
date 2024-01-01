import src.my_functions as my_function


def test_for_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=100, number_two=10)
    assert result == 10


def test_for_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=30, number_two=3)
    assert result == 10


def test_for_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=30, number_two=2)
    assert result == 15
