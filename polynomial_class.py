import number_class as number


def divisors(x):  # it returns list of the integer divisors
    if x == 0:
        return [0]

    if x < 0:
        x = -x

    d = []
    for i in range(1, x + 1):
        if x % i == 0:
            d.append(i)

    res = []
    for i in range(len(d)):
        res.append(d[i])
        res.append(-d[i])
    return res


def nwd(a, b):       # the greatest common divisor
    while b:
        a, b = b, a % b
    return a


def nww(a, b):       # the least common multiple
    return a*b//nwd(a, b)


class Polynomial:
    # coefficients must be given in the same way as numbers from 'number_class.py' in a one list
    # the name of the polynomial must contain its name and the variable in round brackets, e.g.: "P(x)", "Poly(a)"

    def __init__(self, name, coefficents):
        self.name = name
        self.coeffs = []
        for x in coefficents:
            self.coeffs.append(number.Number(x))
        self.simplify()

    def __repr__(self):     # printing style
        self.simplify()
        val = 0
        for x in self.coeffs:
            if x.decimal(15) != 0:
                val += 1
        if val == 0:
            return self.name+" = 0"
        variable = self.name[-2]
        n = len(self.coeffs)-1
        result = self.name + " ="
        for i in range(len(self.coeffs)):
            if i == 0 or self.coeffs[i].decimal(15) < 0:
                result += str(self.coeffs[i])
                if n > 0:
                    result += variable
                if n > 1:
                    result += "^"+str(n)
            elif self.coeffs[i].decimal(15) != 0:
                result += " +"
                result += str(self.coeffs[i])
                if n > 0:
                    result += variable
                if n > 1:
                    result += "^"+str(n)
            n -= 1

        new_result = ""
        numbers = {"-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for i in range(result.find("=")+2, len(result)):
            if result[i] == "1":
                if i+1 < len(result):
                    if result[i+1] == variable and i > 0 and result[i-1] not in numbers:
                        pass
                    else:
                        new_result += result[i]
                else:
                    new_result += result[i]
            else:
                new_result += result[i]

        return self.name+" = "+new_result

    def __add__(self, other):   # addition: self + other
        self.simplify()
        other.simplify()

        a = list(reversed(self.coeffs))
        b = list(reversed(other.coeffs))
        if len(b) > len(a):
            a, b = b, a

        c = []
        for i in range(len(a)):
            if i < len(b):
                c.append(a[i]+b[i])
            else:
                c.append(a[i])

        result = Polynomial("Added("+self.name[-2]+")", [])
        result.coeffs = list(reversed(c))

        return result

    def __sub__(self, other):   # substraction: self - other
        self.simplify()
        other.simplify()

        a = list(reversed(self.coeffs))
        b = list(reversed(other.coeffs))
        c = []

        if len(a) == len(b):
            for i in range(len(a)):
                c.append(a[i]-b[i])
        elif len(a) > len(b):
            for i in range(len(a)):
                if i >= len(b):
                    c.append(a[i])
                else:
                    c.append(a[i]-b[i])
        else:
            for i in range(len(b)):
                if i >= len(a):
                    c.append(-b[i])
                else:
                    c.append(a[i]-b[i])

        result = Polynomial("Subtracted(" + self.name[-2] + ")", [])
        result.coeffs = list(reversed(c))

        return result

    def __mul__(self, other):   # multiplication: self * other
        self.simplify()
        other.simplify()

        p = []
        n = self.get_degree_of_polynomial()+other.get_degree_of_polynomial()
        for i in range(n+1):
            p.append(number.Number("0"))
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                p[i+j] += self.coeffs[i]*other.coeffs[j]

        result = Polynomial("Multiplied("+self.name[-2]+")", [""])
        result.coeffs = p

        return result

# about dividing polynomials: P(x) = Q(x)*S(x) + R(x), Q(x) is a divisor

    def __truediv__(self, other):       # self / other; it return tuple( S(x),R(x) )
        if other == Polynomial("P(x)", ["1"]):
            return self, Polynomial("R(x)", [])
        zero = Polynomial("Z(x)", [""])
        if zero == other:
            raise ZeroDivisionError()
        s_x = Polynomial("S(x)", [])
        a = Polynomial("A(x)", [])
        b = Polynomial("B(x)", [])
        for x in self.coeffs:
            a.coeffs.append(x)
        for x in other.coeffs:
            b.coeffs.append(x)

        while a.get_degree_of_polynomial() >= b.get_degree_of_polynomial():
            m = a.coeffs[0]/b.coeffs[0]
            n = a.get_degree_of_polynomial()-b.get_degree_of_polynomial()
            poly = Polynomial("P(x)", [])
            for i in range(n):
                poly.coeffs.append(number.Number("0"))
            poly.coeffs[0] = m
            s_x += poly
            a_poly = b*poly
            a -= a_poly
            s_x.change_name("S(" + self.name[-2] + ")")
            a.change_name("R(" + self.name[-2] + ")")
        res = (s_x, a)
        return res

    def __floordiv__(self, other):      # self // other; it return S(x)
        zero = Polynomial("Z(x)", [""])
        if zero == other:
            raise ZeroDivisionError()
        return (self/other)[0]

    def __mod__(self, other):        # self % other; it return R(x)
        zero = Polynomial("Z(x)", [""])
        if zero == other:
            raise ZeroDivisionError()
        return (self/other)[1]

    def __pow__(self, power):  # exponentiation: self**power
        result = Polynomial("Poly", [])
        if power == 0:
            result.coeffs.append(number.Number("1"))
            result.simplify()
            result.name = "RaisedTo{}Power(".format(power) + self.name[-2] + ")"
            return result

        for x in self.coeffs:
            result.coeffs.append(x)
        for i in range(power-1):
            result *= self

        result.simplify()
        result.name = "RaisedTo{}Power".format(power)+"("+self.name[-2]+")"
        return result

    def __neg__(self):      # opposite fraction: -self
        result = Polynomial("OppositeCoefficients("+self.name[-2]+")", [])
        for x in self.coeffs:
            result.coeffs.append(-x)

        return result

    def __eq__(self, other):    # self == other
        self.simplify()
        other.simplify()

        return self.coeffs == other.coeffs

    def change_name(self, new_name):    # changing name of the polynomial
        self.name = new_name

    def get_degree_of_polynomial(self):     # it returns degree of the polynomial
        self.simplify()

        return len(self.coeffs)-1

    def get_monomials(self):        # it returns list of monomials forming a polynomial
        self.simplify()
        return self.coeffs

    def simplify(self):     # simplifying polynomial
        val = 0
        for x in self.coeffs:
            if x.decimal(15) != 0:
                val += 1
        if val == 0:
            self.coeffs = [number.Number("0")]

        while self.coeffs[0].decimal(15) == 0 and len(self.coeffs) != 1:
            self.coeffs.remove(self.coeffs[0])

    def get_value(self, argument):      # it returns the polynomial value for a given variable
        self.simplify()
        result = self.coeffs[0]
        n = len(self.coeffs)
        for i in range(1, n):
            result = result * argument
            result += self.coeffs[i]

        return result

    def linear_equation(self):      # it solves self = 0
        return -self.coeffs[1] / self.coeffs[0]

    def delta_metod(self, only_solution=False):         # it solves step by step: self = 0 using the delta method,
        if not self.get_degree_of_polynomial() == 2:    # degree of polynomial must be 2
            raise InvalidPolynomialDegree("delta")

        step0 = str(self)
        step0 = step0[step0.find("=") + 2:] + " = 0"
        step1 = "a ="+str(self.coeffs[0])+"     "+"b ="+str(self.coeffs[1])+"     "+"c ="+str(self.coeffs[2])
        x_0 = "xyz"
        x_1 = "xyz"
        x_2 = "xyz"
        delta = self.coeffs[1]*self.coeffs[1] - number.Number("4")*self.coeffs[0]*self.coeffs[2]
        if delta.decimal(15) == 0:
            step2 = '\u0394' + " = b^2 - 4ac = "+str(delta)
        else:
            step2 = '\u0394' + " = b^2 - 4ac =" + str(delta)
        if delta.decimal(15) < 0:
            step3 = "("+'\u0394'+" < 0) ==> 0 solutions"
            step4 = ""
        elif delta.decimal(15) == 0:
            step3 = "(" + '\u0394' + " = 0) ==> 1 solution"
            x_0 = -self.coeffs[1] / number.Number("2") / self.coeffs[0]
            step4 = "x_0 = -b/2a ="+str(x_0)
        else:
            step3 = "(" + '\u0394' + " > 0) ==> 2 solutions"
            power = number.Number("1/2")
            x_1 = (-self.coeffs[1] + delta ** power) / number.Number("2") / self.coeffs[0]
            x_2 = (-self.coeffs[1] - delta ** power) / number.Number("2") / self.coeffs[0]
            step4 = "x_1 = [-b+"+'\u0394'+"^(1/2)]/2a ="
            if x_1.decimal(15) == 0:
                step4 += " "
            step4 += str(x_1)+"\n" + "x_2 = [-b-"+'\u0394'+"^(1/2)]/2a ="
            if x_2.decimal(15) == 0:
                step4 += " "
            step4 += str(x_2)

        if only_solution:
            if isinstance(x_1, number.Number):
                return [x_1, x_2]
            elif isinstance(x_0, number.Number):
                return [x_0]
            else:
                return []
        else:
            return [step0, step1, step2, step3, step4]

    def cardano_metod(self):    # it solves step by step: self = 0 using Cardano's way, degree of polynomial must be 3
        self.simplify()
        if not self.get_degree_of_polynomial() == 3:
            raise InvalidPolynomialDegree("Cardano")
        poly = Polynomial("P(x)", [])
        for x in self.coeffs:
            poly.coeffs.append(x)
        poly.simplify()

        a = poly.coeffs[0]
        # b = poly.coeffs[1]
        # c = poly.coeffs[2]
        # d = poly.coeffs[3]
        step0 = str(poly)
        step0 = step0[step0.find("=") + 2:] + " = 0"

        step1 = " "
        if a != number.Number("1"):
            step1 = step0 + "  / :" + str(a)
            for i in range(len(poly.coeffs)):
                poly.coeffs[i] /= a
            s = str(poly)
            s = s[s.find("=") + 2:] + " = 0"
            step1 += "\n" + s

        a = poly.coeffs[0]
        b = poly.coeffs[1]
        c = poly.coeffs[2]
        d = poly.coeffs[3]
        p = 1
        q = 1
        step2 = ""
        if b != number.Number("0"):
            step2 = "for x substitute (y-" + str(b / number.Number("3")) + "):\n"
            s = str(poly).replace("x", "(y-" + str(b / number.Number("3")) + ")")
            step2 += s[s.find("=") + 2:] + " = 0\n"
            p = c / a - (b ** 2) / number.Number("3")
            q = number.Number("2") * (b ** 3) / number.Number("27") - b * c / number.Number("3") + d
            step2 += "y^3"
            if p < number.Number("0"):
                step2 += str(p)
            else:
                step2 += " +" + str(p)
            step2 += "y"
            if q < number.Number("0"):
                step2 += str(q)
            else:
                step2 += " +" + str(q)
            step2 += " = 0"
        elif b == number.Number("0"):
            step2 = " "
            p = c
            q = d
        delta = (p/number.Number("3"))**3 + (q/number.Number("2"))**2
        if delta.decimal(15) == 0:
            step3 = '\u0394' + " = (p/3)^3 + (q/2)^2 = " + str(delta)
        else:
            step3 = '\u0394' + " = (p/3)^3 + (q/2)^2 =" + str(delta)

        if delta > number.Number("0"):
            step4 = "1 real solution"
        elif delta < number.Number("0"):
            step4 = "2 real solution"
        else:
            step4 = "3 real solution"

        return [step0, step1, step2, step3, step4]

    def find_integer_roots(self):       # it returns list of integer roots
        for x in self.coeffs:
            if len(x.expressions) == 1 and x.expressions[0].number ** x.expressions[0].degree == 1 \
                    and x.expressions[0].coefficient.denominator == 1:
                pass
            else:
                raise InvalidCoefficientNumber

#            d_nww = self.coeffs[0].expressions[0].coefficient.denominator
#            for k in self.coeffs:
#                d_nww = nww(d_nww, k.expressions[0].coefficient.denominator)
#        print(d_nww)
        d = int(self.coeffs[-1].expressions[0])
        divs = divisors(d)
        sols = []
        for x in divs:
            if self.get_value(number.Number(str(x))) == number.Number("0"):
                sols.append(number.Number(str(x)))
                if len(sols) == self.get_degree_of_polynomial():
                    break

        return sols

    def find_rational_roots(self):      # it returns list of rational roots
        for x in self.coeffs:
            if len(x.expressions) == 1 and x.expressions[0].number ** x.expressions[0].degree == 1 \
                    and x.expressions[0].coefficient.denominator == 1:
                pass
            else:
                raise InvalidCoefficientNumber

        #            d_nww = self.coeffs[0].expressions[0].coefficient.denominator
        #            for k in self.coeffs:
        #                d_nww = nww(d_nww, k.expressions[0].coefficient.denominator)
        #        print(d_nww)
        d = int(self.coeffs[-1].expressions[0])
        a = int(self.coeffs[0].expressions[0])
        divs_d = divisors(d)
        divs_a = divisors(a)
        sols = []
        for i in divs_d:
            for j in divs_a:
                if j != 0:
                    p = number.Number(str(i))/number.Number(str(j))
                    if self.get_value(p) == number.Number("0") and p not in sols:
                        sols.append(p)
                        if len(sols) == self.get_degree_of_polynomial():
                            break

        return sols

    def break_down_to_factor(self, only_resultat=True):          # it returns a polynomial broken down
        roots = []                                               # to the lowest possible real factors

        if len(self.coeffs) == 1 and self.coeffs[0] == number.Number("0"):
            return self.name + " = 0"

        poly = Polynomial("P(x)", [])
        for x in self.coeffs:
            poly.coeffs.append(x)
        poly.simplify()

        for x in poly.coeffs:
            if len(x.expressions) == 1 and x.expressions[0].number ** x.expressions[0].degree == 1:
                pass
            else:
                raise InvalidCoefficientNumber

        nww_d = poly.coeffs[0].expressions[0].coefficient.denominator
        for x in poly.coeffs:
            nww_d = nww(nww_d, x.expressions[0].coefficient.denominator)

        nww_d = number.Number(str(nww_d))
        for i in range(len(poly.coeffs)):
            poly.coeffs[i] *= nww_d

        divs = poly.find_rational_roots()
        while divs:
            for d in divs:
                roots.append(d)
                p = Polynomial("P(x)", ["1"])
                p.coeffs = [number.Number("1"), -d]
                poly //= p
                divs = poly.find_rational_roots()

        if poly.coeffs[0] == number.Number("-1"):
            a = number.Number("-1") / nww_d
            poly = -poly
        elif poly.coeffs[0] != number.Number("1"):
            a = poly.coeffs[0]
            for k in poly.coeffs:
                a = nwd(int(a), int(k))
            a = number.Number(str(a))
            for i in range(len(poly.coeffs)):
                poly.coeffs[i] /= a
        else:
            a = number.Number("1")/nww_d

        if poly.get_degree_of_polynomial() == 2:
            roots += poly.delta_metod(True)

        if a == number.Number("1"):
            a = ""
        elif a == number.Number("-1"):
            a = "-"
        else:
            a = str(a)

        result = self.name+" = "+a

        unique_roots = []
        for x in roots:
            if x not in unique_roots:
                unique_roots.append(x)
        if number.Number("0") in roots:
            unique_roots.remove(number.Number("0"))
            unique_roots.insert(0, number.Number("0"))
        unique_roots = sorted(unique_roots, reverse=True)
        for x in unique_roots:
            if x.decimal(15) > 0:
                result += "(x" + str(-x) + ")"
            elif x.decimal(15) < 0:
                result += "(x +" + str(-x) + ")"
            else:
                result += "x"

            if roots.count(x) != 1:
                result += "^" + str(roots.count(x))

        if poly != Polynomial("P(x)", "1"):
            s = str(poly)
            result += "(" + s[s.find("=")+2:] + ")"

        if only_resultat:
            return result
        else:
            return [sorted(unique_roots), roots, poly.get_degree_of_polynomial() < 3]

    def __lt__(self, other):  # self < other; it solves inequality; return a list with intervals
        poly = self-other
        divs = poly.break_down_to_factor(False)
        unique_d = divs[0]
        result = []
        if divs[2]:
            for i in range(len(unique_d)):
                if i == 0:
                    if poly.get_value(unique_d[i]+number.Number("-1")) < number.Number("0"):
                        result.append("(-Inf,"+str(unique_d[i])+")")
                if i == len(unique_d)-1:
                    if poly.get_value(unique_d[i]+number.Number("1")) < number.Number("0"):
                        result.append("("+str(unique_d[i])+", Inf)")
                    continue
                if poly.get_value((unique_d[i]+unique_d[i+1])/number.Number("2")) < number.Number("0"):
                    result.append("("+str(unique_d[i])+", "+str(unique_d[i+1])+")")

            return result, False
        else:
            raise InvalidRoots()

    def __le__(self, other):  # self <= other; it solves inequality; return a list with intervals
        poly = self - other
        divs = poly.break_down_to_factor(False)
        unique_d = divs[0]
        result = []
        if divs[2]:
            for i in range(len(unique_d)):
                if i == 0:
                    if poly.get_value(unique_d[i] + number.Number("-1")) <= number.Number("0"):
                        result.append(["-Inf", str(unique_d[i])])
                    else:
                        result.append([str(unique_d[i]), str(unique_d[i])])
                if i == len(unique_d) - 1:
                    if poly.get_value(unique_d[i] + number.Number("1")) <= number.Number("0"):
                        result.append([str(unique_d[i]), "Inf"])
                    else:
                        result.append([str(unique_d[i]), str(unique_d[i])])
                    continue
                if poly.get_value((unique_d[i] + unique_d[i + 1]) / number.Number("2")) <= number.Number("0"):
                    result.append([str(unique_d[i]), str(unique_d[i+1])])
                else:
                    result.append([str(unique_d[i]), str(unique_d[i])])

            n = len(result)
            for k in range(n):
                for i in range(len(result)-1):
                    if result[i][1] == result[i+1][0]:
                        result[i][1] = result[i+1][1]
                        del result[i+1]
                        break

            for i in range(len(result)):
                if result[i][0] == result[i][1]:
                    del result[i][0]

            return result, True
        else:
            raise InvalidRoots()

    def __gt__(self, other):  # self > other; it solves inequality; return a list with intervals
        poly = self-other
        divs = poly.break_down_to_factor(False)
        unique_d = divs[0]
        result = []
        if divs[2]:
            for i in range(len(unique_d)):
                if i == 0:
                    if poly.get_value(unique_d[i]+number.Number("-1")) > number.Number("0"):
                        result.append("(-Inf,"+str(unique_d[i])+")")
                if i == len(unique_d)-1:
                    if poly.get_value(unique_d[i]+number.Number("1")) > number.Number("0"):
                        result.append("("+str(unique_d[i])+", Inf)")
                    continue
                if poly.get_value((unique_d[i]+unique_d[i+1])/number.Number("2")) > number.Number("0"):
                    result.append("("+str(unique_d[i])+", "+str(unique_d[i+1])+")")

            return result, False
        else:
            raise InvalidRoots()

    def __ge__(self, other):  # self >= other; it solves inequality; return a list with intervals
        poly = self - other
        divs = poly.break_down_to_factor(False)
        unique_d = divs[0]
        result = []
        if divs[2]:
            for i in range(len(unique_d)):
                if i == 0:
                    if poly.get_value(unique_d[i] + number.Number("-1")) >= number.Number("0"):
                        result.append(["-Inf", str(unique_d[i])])
                    else:
                        result.append([str(unique_d[i]), str(unique_d[i])])
                if i == len(unique_d) - 1:
                    if poly.get_value(unique_d[i] + number.Number("1")) >= number.Number("0"):
                        result.append([str(unique_d[i]), "Inf"])
                    else:
                        result.append([str(unique_d[i]), str(unique_d[i])])
                    continue
                if poly.get_value((unique_d[i] + unique_d[i + 1]) / number.Number("2")) >= number.Number("0"):
                    result.append([str(unique_d[i]), str(unique_d[i+1])])
                else:
                    result.append([str(unique_d[i]), str(unique_d[i])])

            n = len(result)
            for k in range(n):
                for i in range(len(result) - 1):
                    if result[i][1] == result[i + 1][0]:
                        result[i][1] = result[i + 1][1]
                        del result[i + 1]
                        break

            for i in range(len(result)):
                if result[i][0] == result[i][1]:
                    del result[i][0]

            return result, True
        else:
            raise InvalidRoots()


class InvalidPolynomialDegree(Exception):      # exception: invalid polynomial degree
    def __init__(self, method):
        if method == "delta":
            super().__init__("Invalid polynomial degree. If you want to use the delta method, the degree of "
                             "polynomial must be 2")
        elif method == "Cardano":
            super().__init__("Invalid polynomial degree. If you want to use the Cardano's way, the degree of "
                             "polynomial must be 3")


class InvalidCoefficientNumber(Exception):       # exception: invalid coefficient number
    def __init__(self):
        super().__init__("Invalid coefficient number. Coefficients must be integer!")


class InvalidRoots(Exception):      # exception: invalid polynomial's roots
    def __init__(self):
        super().__init__("Invalid roots of polynomial. All roots must be rational numbers!")
