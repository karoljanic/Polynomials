class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return ("{}/{}".format(int(self.numerator), int(self.denominator)))

    def __add__(self, other):
        n = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        d = (self.denominator * other.denominator)
        result = Fraction(n, d)
        result.simplify()
        return result

    def __sub__(self, other):
        n = (self.numerator * other.denominator) + (self.denominator * -1 * other.numerator)
        d = (self.denominator * other.denominator)
        result = Fraction(n, d)
        result.simplify()
        return result

    def __mul__(self, other):
        result = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        result.simplify()
        return result

    def __truediv__(self, other):
        result = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        result.simplify()
        return result

    def __pow__(self, power):
        result = Fraction(self.numerator ** power, self.denominator ** power)
        result.simplify()
        return result

    def simplify(self):
        a = self.numerator
        b = self.denominator
        r = 1
        while r != 0:
            r = a % b
            a, b = b, r
        self.numerator /= a
        self.denominator /= a

    def inverse(self):
        self.numerator, self.denominator = self.denominator, self.numerator

    def decimal(self, decimalplaces = 2):       # max decimalplaces = 15
        return round(self.numerator * 1.0 / self.denominator, decimalplaces)
