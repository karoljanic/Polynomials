import fraction_class as f

def nwd(a,b):       # the greatest common divisor
    while b:
        a, b = b, a % b
    return a

def nww(a,b):       # the least common multiple
    return a*b//nwd(a,b)


class Root:
    def __init__(self, coefficient, degree = 1, number = 1):

        if isinstance(coefficient, int):           # coefficient can be Fraction or integer
            self.coefficient = f.Fraction(coefficient)
        elif isinstance(coefficient, f.Fraction):
            self.coefficient = coefficient
        else:
            raise TypeError

        if isinstance(degree, int):
            self.degree = degree                   # degree must be positive integer
        else:
            raise TypeError

        if isinstance(number, int):                # number must be positive integer
            self.number = number
        else:
            raise TypeError

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
            return ("{}".format(self.coefficient))
        if self.coefficient.decimal() == 1:
            return ("{}^(1/{})".format(int(self.number), int(self.degree)))
        if self.coefficient.decimal() == -1:
            return ("-{}^(1/{})".format(int(self.number), int(self.degree)))
        else:
            return ("{}*({}^(1/{}))".format(self.coefficient,int(self.number),int(self.degree)))


    def __add__(self, other):   # addition: +
        self.simplify()
        other.simplify()

        if self.degree == other.degree and self.number == other.number:
            return [Root(self.coefficient+other.coefficient, int(self.degree), int(self.number))]
        else:
            return [self,other]

    def __sub__(self, other):    # substraction: -
        self.simplify()
        other.simplify()

        if self.degree == other.degree and self.number == other.number:
            return [Root(self.coefficient - other.coefficient, int(self.degree), int(self.number))]
        else:
            return [self, Root(-other.coefficient, int(other.degree), int(other.number))]

    def __mul__(self, other):   # multiplication: *
        self.simplify()
        other.simplify()

        coeff = self.coefficient*other.coefficient
        degree = self.degree*other.degree
        num = self.number**other.degree * other.number**self.degree
        r = Root(coeff, int(degree), int(num))
        r.simplify()
        return r

    def __truediv__(self, other):   # real number division: /
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


    def __floordiv__(self, other):      # integers division: //
        pass                            # operation unavailable

    def __mod__(self, other):           # modulo: %
        pass                            # operation unavailable

    def __pow__(self, power, modulo=None):      # exponentiation: **
        if not modulo == None:                  # exponentiation with modulo unavailable
            pass
        else:
            x = Root(1)
            for i in range(power):
                x = x*self
                x.simplify()

            return x

    def __neg__(self):      # opposite number: -
        return Root(-self.coefficient, int(self.degree), int(self.number))

    def simplify(self):    # simplifying number
        dividers = []
        i = 2
        num = self.number
        while num != 1:
            if num%i == 0:
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
                p = nwd(p,i)
            if self.degree % p == 0:
                self.degree //= p
                self.number = pow(self.number, (1/p))

        self.coefficient.simplify()


    def decimal(self, decimalplaces = 2):       # max decimalplaces = 15; return approximate value of the expression
        result = self.coefficient.decimal(15)*pow(self.number, (1/self.degree))
        return round(result,decimalplaces)






