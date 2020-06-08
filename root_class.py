import fraction_class as f


def nwd(a, b):       # the greatest common divisor
    while b:
        a, b = b, a % b
    return a


def nww(a, b):       # the least common multiple
    return a*b//nwd(a, b)


class Root:
    def __init__(self, coefficient, degree=1, number=1):

        if isinstance(coefficient, int):           # coefficient can be Fraction or integer
            self.coefficient = f.Fraction(coefficient)
        elif isinstance(coefficient, f.Fraction):
            self.coefficient = coefficient
        else:
            raise BadCoefficientTypeException()

        if isinstance(degree, int):
            self.degree = degree                   # degree must be positive integer
        else:
            raise BadDegreeTypeException()

        if isinstance(number, int):                # number under root must be positive integer
            self.number = number
        else:
            raise BadNumberTypeException()

        self.simplify()

    def __repr__(self):     # printing style
        self.simplify()
        if self.coefficient.numerator == 0:
            return "0"
        if self.degree == 1 and self.number == 1 and self.coefficient.decimal() == -1:
            return "-1"
        if self.degree == 1 and self.number == 1 and self.coefficient.decimal() == 1:
            return "1"
        if self.degree == 1 and self.number == 1:
            return "{}".format(self.coefficient)
        if self.coefficient.decimal() == 1:
            return "{}^(1/{})".format(int(self.number), int(self.degree))
        if self.coefficient.decimal() == -1:
            return "-{}^(1/{})".format(int(self.number), int(self.degree))
        else:
            return "{}*({}^(1/{}))".format(self.coefficient, int(self.number), int(self.degree))

    def __add__(self, other):   # addition: self + other
        self.simplify()
        other.simplify()

        if self.degree == other.degree and self.number == other.number:
            return [Root(self.coefficient+other.coefficient, int(self.degree), int(self.number))]
        else:
            return [self, other]

    def __sub__(self, other):    # substraction: self - other
        self.simplify()
        other.simplify()

        if self.degree == other.degree and self.number == other.number:
            return [Root(self.coefficient - other.coefficient, int(self.degree), int(self.number))]
        else:
            return [self, Root(-other.coefficient, int(other.degree), int(other.number))]

    def __mul__(self, other):   # multiplication: self * other
        self.simplify()
        other.simplify()

        coeff = self.coefficient*other.coefficient
        degree = self.degree*other.degree
        num = self.number**other.degree * other.number**self.degree
        r = Root(coeff, int(degree), int(num))
        r.simplify()
        return r

    def __truediv__(self, other):   # real number division: self / other # this need fix
        self.simplify()
        other.simplify()

        coeff = self.coefficient / other.coefficient
        deg = nww(self.degree, other.degree)

        a = pow(self.number, deg//self.degree)
        b = pow(other.number, deg//other.degree)
        c = b

        coeff = coeff / f.Fraction(b)
        d = a * (c ** (deg-1))

        return Root(coeff, int(deg), int(d))

    def __pow__(self, power, modulo=None):      # exponentiation: self ** power
        if not isinstance(power, int):
            raise BadPowerTypeException()
        x = Root(1)
        for i in range(power):
            x = x*self
            x.simplify()

        return x

    def __neg__(self):      # opposite number: -self
        return Root(-self.coefficient, int(self.degree), int(self.number))

    def __abs__(self):      # absolute value: abs(self)
        return Root(abs(self.coefficient), int(self.degree), int(self.number))

    def __invert__(self):   # inverse of the root: ~self # this need fix ater truediv
        r = Root(1)
        return r/self

    def __int__(self):      # converting root to integer number: int(self)
        return int(self.decimal(15))

    def __float__(self):    # converting fraction to float number: float(self)
        return self.decimal(15)

    def __lt__(self, other):    # self < other
        return self.decimal() < other.decimal()

    def __le__(self, other):    # self <= other
        return self.decimal() <= other.decimal()

    def __eq__(self, other):    # self == other
        self.simplify()
        other.simplify()
        return self.coefficient == other.coefficient and self.degree == other.degree and self.number == other.number

    def __ge__(self, other):    # self >= other
        return self.decimal() >= other.decimal()

    def __gt__(self, other):    # self > other
        return self.decimal() > other.decimal()

    def __floor__(self):        # math.floor(self)
        return round((self.decimal(15) - 0.5))

    def __ceil__(self):         # math.ceil(self)
        return round((self.decimal(15) + 0.5))

    def simplify(self):    # simplifying number
        dividers = []
        i = 2
        num = self.number
        while num != 1:
            if num % i == 0:
                dividers.append(i)
                num /= i
            else:
                i += 1
        if len(dividers) > 0:
            unique_dividers = list(set(dividers))
            counts = []

            for i in unique_dividers:
                counts.append(dividers.count(i))

            for i in range(len(counts)):
                if counts[i] >= self.degree:
                    n = self.degree
                    a = counts[i] // self.degree
                    self.coefficient = self.coefficient * (unique_dividers[i]**a)
                    self.number /= (unique_dividers[i]**(n*a))

        if self.number == 1:
            self.degree = 1

        dividers = []
        i = 2
        num = self.number
        while num != 1:
            if num % i == 0:
                dividers.append(i)
                num /= i
            else:
                i += 1
        if len(dividers) > 0:
            unique_dividers = list(set(dividers))
            counts = []
            for i in unique_dividers:
                counts.append(dividers.count(i))
            p = counts[0]

            for i in counts:
                p = nwd(p, i)
            if self.degree % p == 0:
                self.degree //= p
                self.number = pow(self.number, (1/p))

        self.coefficient.simplify()

    def decimal(self, decimal_places=2):       # max decimal_places = 15; return approximate value of the expression
        if not 0 <= decimal_places <= 15:
            raise BadArgumentException()

        result = self.coefficient.decimal(15)*pow(self.number, (1/self.degree))
        return round(result, decimal_places)


class BadCoefficientTypeException(Exception):      # exception: bad coefficient value
    def __init__(self):
        super().__init__("Bad argument. Coefficient must be integer or Fraction!")


class BadDegreeTypeException(Exception):      # exception: bad degree value
    def __init__(self):
        super().__init__("Bad argument. Degree must be positive integer!")


class BadNumberTypeException(Exception):      # exception: bad number under root value
    def __init__(self):
        super().__init__("Bad argument. Number under root must be positive integer!")


class BadPowerTypeException(Exception):     # exception: bad power value
    def __init__(self):
        super().__init__("Bad argument. Power must be integer!")


class BadArgumentException(Exception):      # exception: bad decimal places number
    def __init__(self):
        super().__init__("Bad argument. Decimal places number should be integer between <0,15>!")
