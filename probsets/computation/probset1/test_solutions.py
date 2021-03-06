# test_solutions.py
"""Volume 1B: Testing.
<Name>
<Class>
<Date>
"""

import solutions as soln
import pytest
import math


# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(3, 4) == 7, "Addition failed on positive integers"

def test_smallest_factor():
    assert soln.smallest_factor(1) == 1, "Smallest factor failed on 1"
    assert soln.smallest_factor(2) == 2, "smallest factor failed on primes"
    assert soln.smallest_factor(4) == 2, "smallest factor failed on composites"

# Problem 2: Test the operator function from solutions.py
def test_operator():
    assert soln.operator(1, 1, "+") == 2, "something is wrong with addition"
    assert soln.operator(1, 1, "-") == 0, "something is wrong with subtraction"
    assert soln.operator(2, 2, "*") == 4, "something is wrong with multiplication"
    assert soln.operator(6, 3, "/") == 2, "something is wrong with division"
    # we will now test the Error messages using raise and with
    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 2, 3)
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper should be a string"
    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 2, "+-")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper should be one character"
    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 0, "/")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "You can't divide by zero!"
    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 3, "&")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper can only be: '+', '/', '-', or '*'"

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

def test_complex_sub(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 - number_2 == soln.ComplexNumber(-4, -3)
    assert number_1 - number_3 == soln.ComplexNumber(-1, -7)
    assert number_2 - number_3 == soln.ComplexNumber(3 , -4)
    assert number_3 - number_3 == soln.ComplexNumber(0, 0)

def test_complex_conjugate(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.conjugate() == soln.ComplexNumber(1, -2)
    assert number_2.conjugate() == soln.ComplexNumber(5, -5)
    assert number_3.conjugate() == soln.ComplexNumber(2, -9)

def test_complex_norm(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.norm() == 5**0.5
    assert number_2.norm() == 5*2**0.5
    assert number_3.norm() == 85**0.5

def test_complex_equal(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert (number_1  == number_2) == False
    assert (number_1  == number_3) == False
    assert (number_2  == number_3) == False
    assert (number_3  == number_3) == True

def test_complex_string(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert str(number_1) == "1+2i"
    assert str(number_2) == "5+5i"
    assert str(number_3) == "2+9i"


def test_complex_truediv(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert (number_1/number_2) == soln.ComplexNumber(0.3, 0.1)
    assert (number_1/number_1) == soln.ComplexNumber(1.0, 0)
    with pytest.raises(Exception) as excinfo:
        (number_1/(number_2 - number_2))
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Cannot divide by zero"


# Problem 4: Write test cases for the Set game.
def test_setgame():
    with pytest.raises(Exception) as excinfo:
        soln.setgame("hands/setgameTestcase2.txt")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Wrong card numbers!"
    with pytest.raises(Exception) as excinfo:
        soln.setgame("hands/setgameTestcase3.txt")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Invalid cards!"
    with pytest.raises(Exception) as excinfo:
        soln.setgame("hands/setgameTestcase4.txt")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Duplicate cards!"
    with pytest.raises(Exception) as excinfo:
        soln.setgame("hands/setgameTestcase5.txt")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Invalid categories!"
    assert  (((),
              (0, 1, 2),
              (0, 3, 4),
              (0, 5, 6),
              (0, 7, 8),
              (0, 10, 11),
              (1, 8, 10),
              (1, 9, 11),
              (2, 7, 11),
              (2, 8, 9),
              (7, 9, 10))== soln.setgame("hands/setgameTestcase1.txt"))
