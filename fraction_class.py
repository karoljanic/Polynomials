class Fraction:
    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, int):      # numerator must be integer
            self.numerator = numerator
        else:
            raise BadNumerateTypeException()

        if isinstance(denominator, int):    # denominator must be integer
            self.denominator = denominator
        else:
            raise BadDenominatorTypeException()

        self.simplify()

    def __repr__(self):     # printing style
        if self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return "{}".format(int(self.numerator))
        else:
            return "{}/{}".format(int(self.numerator), int(self.denominator))

    def __add__(self, other):   # addition: self + other
        n = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        d = (self.denominator * other.denominator)
        result = Fraction(int(n), int(d))
        result.simplify()
        return result

    def __sub__(self, other):   # substraction: self - other
        n = (self.numerator * other.denominator) + (self.denominator * -1 * other.numerator)
        d = (self.denominator * other.denominator)
        result = Fraction(int(n), int(d))
        result.simplify()
        return result

    def __mul__(self, other):   # multiplication: self * other
        result = Fraction(int(self.numerator * other.numerator), int(self.denominator * other.denominator))
        result.simplify()
        return result

    def __truediv__(self, other):   # real number division: self / other
        result = Fraction(int(self.numerator * other.denominator), int(self.denominator * other.numerator))
        result.simplify()
        return result

    def __pow__(self, power):       # exponentiation: self**power
        if not isinstance(power, int):
            raise BadPowerTypeException()
        result = Fraction(int(self.numerator ** power), int(self.denominator ** power))
        result.simplify()
        return result

    def __neg__(self):      # opposite fraction: -self
        result = Fraction(-int(self.numerator), int(self.denominator))
        return result

    def __abs__(self):      # absolute value: abs(self)
        result = Fraction(abs(int(self.numerator)), abs(int(self.denominator)))
        return result

    def __invert__(self):      # inverse of the fraction: ~self
        self.numerator, self.denominator = self.denominator, self.numerator
        self.simplify()
        return self

    def __int__(self):      # converting fraction to integer number: int(self)
        return int(self.numerator//self.denominator)

    def __float__(self):    # converting fraction to float number: float(self)
        return self.numerator / self.denominator

    def __lt__(self, other):    # self < other
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):    # self <= other
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __eq__(self, other):    # self == other
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ge__(self, other):    # self >= other
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __gt__(self, other):    # self > other
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __floor__(self):        # math.floor(self)
        return round((self.numerator * 1.0 / self.denominator - 0.5))

    def __ceil__(self):         # math.ceil(self)
        return round((self.numerator * 1.0 / self.denominator + 0.5))

    def decimal(self, decimal_places=2):       # max decimal_places = 15; return approximate value of the expression
        if not 0 <= decimal_places <= 15:
            raise BadArgumentException()

        return round(self.numerator * 1.0 / self.denominator, decimal_places)

    def simplify(self):     # simplifying fraction
        a = self.numerator
        b = self.denominator
        r = 1
        while r != 0:
            r = a % b
            a, b = b, r
        self.numerator //= a
        self.denominator //= a


class BadNumerateTypeException(Exception):      # exception: bad numerator value
    def __init__(self):
        super().__init__("Bad argument. Numerator must be integer!")


class BadDenominatorTypeException(Exception):   # exception: bad denominator value
    def __init__(self):
        super().__init__("Bad argument. Denominator must be integer!")


class BadArgumentException(Exception):      # exception: bad decimal places number
    def __init__(self):
        super().__init__("Bad argument. Decimal places number should be integer between <0,15>!")


class BadPowerTypeException(Exception):     # exception: bad power value
    def __init__(self):
        super().__init__("Bad argument. Power must be integer!")
