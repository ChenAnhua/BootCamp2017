# solutions.py
"""Volume IB: Testing.
<Name>
<Date>
"""
import math
import numpy as np
import itertools as it
# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
def operator(a, b, oper):
    if type(oper) != str:
        raise ValueError("Oper should be a string")
    if len(oper) != 1:
        raise ValueError("Oper should be one character")
    if oper == "+":
        return a + b
    if oper == "/":
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return a/float(b)
    if oper == "-":
        return a-b
    if oper == "*":
        return a*b
    else:
        raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-',
                                                                abs(self.imag))

# Problem 5: Write code for the Set game here
def setgame(filename):
    # we will firstly read in the text file
    with open(filename) as f:
        lines = f.read().splitlines()
    if len(lines) != 12:
        raise ValueError("Wrong card numbers!")
    if len(lines) != len(set(lines)):
        raise ValueError("Duplicate cards!")
    if len(min(lines, key=len)) == len(max(lines, key=len)) == 4:
        lines = lines
    else:
        raise ValueError("Invalid cards!")
    # we will transform the list of strings to an array of integers
    lines_mat = np.zeros([12, 4])
    for i in range(0, 12):
        a = np.array([int(j) for j in str(lines[i])])
        lines_mat[i , :] = a
    if np.array(np.unique(lines_mat)) not in np.array([0,1,2]):
        raise ValueError("Invalid categories!")

    # we will now work out the set game based on lines_mat
    card_result = ((),)
    for c in list(it.combinations(range(0,12), 3)):
        result = lines_mat[c, : ].sum(axis = 0)
        remain = np.remainder(result, np.array([3, 3, 3, 3]))
        if all(remain == np.array([0, 0, 0, 0])):
            card_result = card_result + (c, )

    return (card_result)
