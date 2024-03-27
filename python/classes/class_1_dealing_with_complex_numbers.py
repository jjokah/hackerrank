"""
HackerRank Chanllenge: Classes - Dealing with Complex Numbers (Python)
https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

Create a new data type for complex numbers.
"""


class Complex(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.c = complex(real, imaginary)

    def __add__(self, no):
        _ = self.c + no.c
        return Complex(_.real, _.imag)

    def __sub__(self, no):
        _ = self.c - no.c
        return Complex(_.real, _.imag)

    def __mul__(self, no):
        _ = self.c * no.c
        return Complex(_.real, _.imag)

    def __truediv__(self, no):
        _ = self.c / no.c
        return Complex(_.real, _.imag)

    def mod(self):
        _ = abs(self.c)
        return Complex(_.real, _.imag)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
