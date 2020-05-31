class Fraction:
    def __init__(self, numerator, denominator = 1):
        if isinstance(numerator, int):      # numerator must be integer
            self.numerator = numerator
        else:
            raise TypeError

        if isinstance(denominator, int):    # denominator must be integer
            self.denominator = denominator
        else:
            raise TypeError

        self.simplify()

    def __repr__(self):     # printing style
        if self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return ("{}".format(int(self.numerator)))
        else:
            return ("{}/{}".format(int(self.numerator), int(self.denominator)))

    def __add__(self, other):   # addition: +
        n = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        d = (self.denominator * other.denominator)
        result = Fraction(n, d)
        result.simplify()
        return result

    def __sub__(self, other):   # substraction: -
        n = (self.numerator * other.denominator) + (self.denominator * -1 * other.numerator)
        d = (self.denominator * other.denominator)
        result = Fraction(n, d)
        result.simplify()
        return result

    def __mul__(self, other):   # multiplication: *
        result = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        result.simplify()
        return result

    def __truediv__(self, other):   # real number division: /
        result = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        result.simplify()
        return result

    def __pow__(self, power, modulo=None):      # exponentiation: **
        if not modulo == None:                  # exponentiation with modulo unavailable
            pass
        else:
            result = Fraction(self.numerator ** power, self.denominator ** power)
            result.simplify()
            return result

    def __neg__(self):      # opposite fraction: -
        result = Fraction(-self.numerator, self.denominator)
        return result

    def __int__(self):      # converting fraction to integer
        return int(self.numerator//self.denominator)

    def simplify(self):     # simplifying fraction
        a = self.numerator
        b = self.denominator
        r = 1
        while r != 0:
            r = a % b
            a, b = b, r
        self.numerator /= a
        self.denominator /= a

    def inverse(self):      # inverse of the fraction
        self.numerator, self.denominator = self.denominator, self.numerator

    def decimal(self, decimalplaces = 2):       # max decimalplaces = 15; return approximate value of the expression
        return round(self.numerator * 1.0 / self.denominator, decimalplaces)
