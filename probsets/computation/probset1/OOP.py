'''
This script is for OOP problem set
'''
# Problem 1
class Backpack(object):
    def __init__(self, name, color, max_size = 5):

        self.name = name
        self.contents = []
        self.color = color
        self.max_size = max_size
    def __eq__(self, other):
        return ([self.name, self.color,  len(self.contents)] == [other.name,  other.color,  len(other.contents)])


    def put(self, item):
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def take(self, item):
        self.contents.remove(item)

    def dump(self):
        self.contents = []

class Jetpack(Backpack):
    def __init__(self, name, color, max_size = 2, fuel = 10):
        Backpack.__init__(self, name, color, max_size)
        self.fuel = fuel

    def fly(self, usage):
        if self.usage <= self.fuel:
            self.fuel = self.fuel - self.usage
        else:
            print("Not enough fuel!")

    def dump(self):
        self.contents = []
        self.fuel     = []

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
