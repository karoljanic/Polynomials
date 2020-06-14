import fraction_class as fraction
import root_class as root
import re


def take_second(x):     # return the second element of list
    return x[1]


class Number:
    # expression can be:
    # 0       ""                            ---                         it is zero
    # 1       "x",                x must belong to integers;            it is a integer
    # 2.0     "a/b",              a,b must belong to integers;          a/b is a fraction
    # 2.1     "c(a/b)"            c,a,b must belong to integers;        mixed number: it is a fraction (c*b+a)/b
    # 3.0     "x^n",              x,n must belong to integers;          x to the power of n
    # 3.1     "(a/b)^n"           a,b,n must belong to integers;        a/b to the power of n
    # 4.0     "a*x^n",            a,x,n must belong to integers;        a times x to the power of n
    # 4.1     "(a/b)*x^n",        a,b,x,n must belong to integers;      a/b times x to the power of n
    # 5.0     "x^(1/n)",          a,n must belong to integers;          n-th root of x
    # 5.1     "x^(m/n)",          x,m,n must belong to integers;        n-th root of x to the power of m
    # 5.2     "a*x^(m/n)",        a,x,m,n must belong to integers;      a times n-th root of x to the power of m
    # 5.3    "(a/b)*x^(m/n)",     a,b,x,m,n must belong to integers;    a/b times n-th root of x to the power of m
    # we can add minus(-) before first number, e.g.: "-x",  "-a/b",  "-x^(m/n)",  "-a*x^(m/n)",  "-(a/b)*x^(m/n)"
    # this minus sign applies to the whole number

    def __init__(self, *args):  # provide expressions, separate them wit a coma
        self.expressions = []
        val = 7
        for k in args:
            if k != "":
                if k[0] == "-":
                    val = -1
                    k = k[1:]
                else:
                    val = 1
            if re.match(r"^-?\([0-9]+/[0-9]+\)\*[0-9]+\^\([0-9]+/[0-9]+\)$", k):    # 5.3
                a = k[1:k.find("/")]
                b = k[k.find("/")+1:k.find(")")]
                x = k[k.find(")")+2:k.find("^")]
                k = k[1:k.find("/")] + k[k.find("/")+1:k.find(")")]+k[k.find(")")+1:]
                m = k[k.find("(")+1:k.find("/")]
                n = k[k.find("/")+1:k.find(")")]
                self.expressions.append(root.Root(fraction.Fraction
                                                  (int(a), int(b))*fraction.Fraction(val), int(n), int(x)**int(m)))
            elif re.match(r"^-?[0-9]+\*[0-9]+\^\([0-9]+/[0-9]+\)$", k):         # 5.2
                a = k[:k.find("*")]
                x = k[k.find("*") + 1:k.find("^")]
                m = k[k.find("^") + 2:k.find("/")]
                n = k[k.find("/") + 1:-1]
                self.expressions.append(root.Root(int(a)*val, int(n), int(x)**int(m)))
            elif re.match(r"^-?[0-9]+\^\([0-9]+/[0-9]+\)$", k):         # 5.0, 5.1
                x = k[:k.find("^")]
                m = k[k.find("^")+2:k.find("/")]
                n = k[k.find("/")+1:-1]
                self.expressions.append(root.Root(val, int(n), int(x)**int(m)))
            elif re.match(r"^-?\([0-9]+/[0-9]+\)\*[0-9]+\^[0-9]+$", k):         # 4.1
                a = k[1:k.find("/")]
                b = k[k.find("/") + 1:k.find(")")]
                x = k[k.find(")") + 2:k.find("^")]
                n = k[k.find("^")+1:]
                self.expressions.append(root.Root(fraction.Fraction
                                                  (int(a), int(b))*fraction.Fraction(val), 1, int(x)**int(n)))
            elif re.match(r"^-?[0-9]+\*[0-9]+\^[0-9]+$", k):            # 4.0
                a = k[:k.find("*")]
                x = k[k.find("*")+1:k.find("^")]
                n = k[k.find("^")+1:]
                self.expressions.append(root.Root(val*int(a)*int(x)**int(n)))
            elif re.match(r"^\([0-9]+/[0-9]+\)\^[0-9]+$", k):        # 3.1
                a = int(k[1:k.find("/")])
                b = int(k[k.find("/")+1:k.find(")")])
                n = int(k[k.find(")")+2:])
                f = fraction.Fraction(a**n, b**n)
                f *= fraction.Fraction(val)
                self.expressions.append(root.Root(f, 1, 1))
            elif re.match(r"^-?[0-9]+\^[0-9]+$", k):            # 3.0
                x = k[:k.find("^")]
                n = k[k.find("^")+1:]
                self.expressions.append(root.Root(val*int(x)**int(n)))
            elif re.match(r"^[0-9]+\([0-9]+/[0-9]+\)$", k):          # 2.1
                c = int(k[:k.find("(")])
                a = int(k[k.find("(")+1:k.find("/")])
                b = int(k[k.find("/")+1:-1])
                f = fraction.Fraction(c*b+a, b)
                f *= fraction.Fraction(val)
                self.expressions.append(root.Root(f, 1, 1))
            elif re.match(r"^-?[0-9]+/[0-9]+$", k):             # 2.0
                a = k[:k.find("/")]
                b = k[k.find("/")+1:]
                self.expressions.append(root.Root(fraction.Fraction(int(a), int(b))*fraction.Fraction(val)))
            elif re.match("^-?[0-9]+$", k):         # 1
                self.expressions.append(root.Root(int(k)*int(val)))
            elif k == "":               # 0
                self.expressions.append(root.Root(0))
            else:
                raise BadExpressionFormatException()

        self.simplify()

    def __repr__(self):     # printing style
        result = ""
        if len(self.expressions) > 1:
            for x in self.expressions:
                if x.coefficient.decimal() == 0:
                    self.expressions.remove(x)
        if len(self.expressions) == 1 and self.expressions[0].decimal() == 0:
            return "0"

        for i in range(len(self.expressions)):
            if i == 0:
                result += " "
                result += str(self.expressions[i])
            else:
                if self.expressions[i].coefficient.decimal() < 0:
                    result += " "
                    result += str(self.expressions[i])
                else:
                    result += " +"
                    result += str(self.expressions[i])

        return result

    def __add__(self, other):       # addition: self + other
        result = Number("")
        result.expressions = self.expressions + other.expressions

        result.simplify()
        return result

    def __sub__(self, other):       # addition: self + other
        result = Number("")
        for x in self.expressions:
            result.expressions.append(x)
        for x in other.expressions:
            result.expressions.append(-x)

        result.simplify()
        return result

    def __mul__(self, other):       # multiplication: self * other
        result = Number("")
        for x in self.expressions:
            for y in other.expressions:
                result.expressions.append(x*y)

        result.simplify()
        return result

    def __truediv__(self, other):       # real number division: self / other
        # if the number of other.expressions is equal to one, the result is exact, otherwise it is float
        # in future: exact division by an expression containing 2nd degree and/or 3th degree root
        if len(other.expressions) > 1:
            return self.decimal(4) / other.decimal(4)
        else:
            d = other.expressions[0]
            result = Number("")
            for x in self.expressions:
                result.expressions.append(x/d)

            result.simplify()
            return result

    def __pow__(self, power, modulo=None):      # exponentiation: self ** power
        if isinstance(power, int):
            result = Number("1")
            for i in range(power):
                result *= self
            result.simplify()

            return result
        elif isinstance(power, Number) and len(self.expressions) == 1 and len(power.expressions) == 1 \
                and power.expressions[0].number ** power.expressions[0].degree == 1:
            p = power.expressions[0]
            power = fraction.Fraction(p.coefficient.numerator, p.coefficient.denominator)
            result = self.expressions[0] ** power
            result.simplify()
            res = Number()
            res.expressions.append(result)
            return res
        else:
            raise UnavaiableOperationException()

    def __neg__(self):      # opposite number: -self
        result = Number("")
        for x in self.expressions:
            result.expressions.append(-x)
        result.simplify()

        return result

    def __abs__(self):      # absolute value: abs(self)
        self.simplify()
        if self.decimal(15) < 0:
            return -self
        else:
            return self

    def __invert__(self):   # inverse of the root: ~self
        # if the number of other.expressions is equal to one, the result is exact, otherwise it is float
        # in future: exact division by an expression containing 2nd degree and/or 3th degree root
        result = Number("1")
        result /= self
        if not isinstance(result, float):
            result.simplify()

        return result

    def __int__(self):      # converting number to integer number: int(self)
        return int(self.decimal(15))

    def __float__(self):    # converting number to float number: float(self)
        return self.decimal(15)

    def __lt__(self, other):    # self < other
        return self.decimal() < other.decimal()

    def __le__(self, other):    # self <= other
        return self.decimal() <= other.decimal()

    def __eq__(self, other):
        n = 0
        for x in self.expressions:
            if x in other.expressions:
                n += 1
            else:
                break
        if n == len(self.expressions):
            return True
        else:
            return False

    def __ge__(self, other):    # self >= other
        return self.decimal() >= other.decimal()

    def __gt__(self, other):    # self > other
        return self.decimal() > other.decimal()

    def __floor__(self):        # math.floor(self)
        return round((self.decimal(15) - 0.5))

    def __ceil__(self):         # math.ceil(self)
        return round((self.decimal(15) + 0.5))

    def simplify(self):     # simplifying number
        for x in self.expressions:
            x.simplify()
        result = []
        unique = []
        for x in self.expressions:
            if not [x.degree, x.number] in unique:
                unique.append([x.degree, x.number])

        unique = sorted(unique, key=take_second)

        val = fraction.Fraction(0)
        for x in unique:
            for y in self.expressions:
                if y.degree == x[0] and y.number == x[1]:
                    val = val + y.coefficient
            result.append(root.Root(val, int(x[0]), int(x[1])))
            val = fraction.Fraction(0)

        self.expressions = result

    def decimal(self, decimal_places=2):    # max decimal_places = 15; return approximate value of the root
        if not 0 <= decimal_places <= 15:
            raise BadArgumentException()

        result = 0
        for x in self.expressions:
            result += x.decimal(15)

        return round(result, decimal_places)


class BadExpressionFormatException(Exception):      # exception: bad argument of expression
    def __init__(self):
        super().__init__("Bad argument. Expression doesn't match the to described format!")


class BadArgumentException(Exception):      # exception: bad decimal places number
    def __init__(self):
        super().__init__("Bad argument. Decimal places number should be integer between <0,15>!")


class UnavaiableOperationException(Exception):       # exception: class can't do it
    def __init__(self):
        super().__init__("Sorry. We can't caltulate it. ;(. Power must be integer or fraction. "
                         "If power is fraction, len(number.expressions) must be 1!")
