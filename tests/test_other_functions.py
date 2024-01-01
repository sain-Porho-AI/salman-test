import src.my_functions as my_function


def test_for_divide1():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=100, number_two=5)
    assert result == 20


def test_for_divide2():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=33, number_two=3)
    assert result == 11


def test_for_divide3():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=20, number_two=2)
    assert result == 10
