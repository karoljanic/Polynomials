import fraction_class as fraction
import root_class as root
import re

def take_second(x):
    return x[1]

class Number:
    # expression can be:
    # 0       ""                            ---                         it is zero
    # 1       "x",                x must belong to integers;            it is a integer
    # 2       "a/b",              a,b must belong to integers,          a/b is a fraction
    # 3       "x^n",              x,n must belong to integers,          x to the power of n
    # 4       "a*x^n",            a,x,n must belong to integers;        a times x to the power of n
    # 5       "(a/b)*x^n",        a,b,x,n must belong to integers;      a/b times x to the power of n
    # 6       "x^(m/n)",          x,m,n must belong to integers;        n-th root of x to the power of m
    # 7       "a*x^(m/n)",        a,x,m,n must belong to integers;      a times n-th root of x to the power of m
    # 8       "(a/b)*x^(m/n),     a,b,x,m,n must belong to integers;    a/b times n-th root of x to the power of m
    # we can add minus(-) before first number, e.g.: "-x",  "-a/b",  "-x^(m/n)",  "-a*x^(m/n)",  "-(a/b)*x^(m/n)"
    # this minus sign applies to the whole number

    def __init__(self, *args):  # provide expressions, separate them wit a coma
        self.expressions = []
        for k in args:
            if k != "":
                if k[0] == "-":
                    val = -1
                    k = k[1:]
                else:
                    val = 1
            if re.match(r"^-?\([0-9]+/[0-9]+\)\*[0-9]+\^\([0-9]+/[0-9]+\)$", k):
                a = k[1:k.find("/")]
                b = k[k.find("/")+1:k.find(")")]
                x = k[k.find(")")+2:k.find("^")]
                k = k[1:k.find("/")] + k[k.find("/")+1:k.find(")")]+k[k.find(")")+1:]
                m = k[k.find("(")+1:k.find("/")]
                n = k[k.find("/")+1:k.find(")")]
                self.expressions.append(root.Root(fraction.Fraction(int(a),int(b))*fraction.Fraction(val), int(n), int(x)**int(m)))
            elif re.match(r"^-?[0-9]+\*[0-9]+\^\([0-9]+/[0-9]+\)$", k):
                a = k[:k.find("*")]
                x = k[k.find("*") + 1:k.find("^")]
                m = k[k.find("^") + 2:k.find("/")]
                n = k[k.find("/") + 1:-1]
                self.expressions.append(root.Root(int(a)*val,int(n), int(x)**int(m)))
            elif re.match(r"^-?[0-9]+\^\([0-9]+/[0-9]+\)$", k):
                x = k[:k.find("^")]
                m = k[k.find("^")+2:k.find("/")]
                n = k[k.find("/")+1:-1]
                self.expressions.append(root.Root(val,int(n),int(x)**int(m)))
            elif re.match(r"^-?\([0-9]+/[0-9]+\)\*[0-9]+\^[0-9]+$", k):
                a = k[1:k.find("/")]
                b = k[k.find("/") + 1:k.find(")")]
                x = k[k.find(")") + 2:k.find("^")]
                n = k[k.find("^")+1:]
                self.expressions.append(root.Root(fraction.Fraction(int(a), int(b))*fraction.Fraction(val), 1, int(x)**int(n)))
            elif re.match(r"^-?[0-9]+\*[0-9]+\^[0-9]+$", k):
                a = k[:k.find("*")]
                x = k[k.find("*")+1:k.find("^")]
                n = k[k.find("^")+1:]
                self.expressions.append(root.Root(val*int(a)*int(x)**int(n)))
            elif re.match(r"^-?[0-9]+\^[0-9]+$", k):
                x = k[:k.find("^")]
                n = k[k.find("^")+1:]
                self.expressions.append(root.Root(val*int(x)**int(n)))
            elif re.match(r"^-?[0-9]+/[0-9]+$", k):
                a = k[:k.find("/")]
                b = k[k.find("/")+1:]
                self.expressions.append(root.Root(fraction.Fraction(int(a), int(b))*fraction.Fraction(val)))
            elif re.match("^-?[0-9]+$", k):
                self.expressions.append(root.Root(int(k)*int(val)))
            elif k == "":
                self.expressions.append(root.Root(0))
            else:
                raise TypeError

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
                if self.expressions[i].coefficient.decimal()<0:
                    result += " "
                    result += str(self.expressions[i])
                else:
                    result += " +"
                    result += str(self.expressions[i])

        return result


    def simplify(self):
        for x in self.expressions:
            x.simplify()
        result = []
        unique = []
        for x in self.expressions:
            if not [x.degree, x.number] in unique:
                unique.append([x.degree, x.number])

        s = sorted(unique, key = take_second)

        val = fraction.Fraction(0)
        for x in unique:
            for y in self.expressions:
                if y.degree == x[0] and y.number == x[1]:
                    val = val + y.coefficient
            result.append(root.Root(val, int(x[0]), int(x[1])))
            val = fraction.Fraction(0)

        self.expressions = result

    def __add__(self, other):
        result = Number("")
        result.expressions = self.expressions + other.expressions

        result.simplify()
        return result

    def __sub__(self, other):
        result = Number("")
        for x in self.expressions:
            result.expressions.append(x)
        for x in other.expressions:
            result.expressions.append(-x)

        result.simplify()
        return result

    def __mul__(self, other):
        result = Number("")
        for x in self.expressions:
            for y in other.expressions:
                result.expressions.append(x*y)

        result.simplify()
        return result

    def __truediv__(self, other):
        if len(other.expressions) > 1:
            return [self.decimal(4) / other.decimal(4)]
        else:
            d = other.expressions[0]
            result = Number("")
            for x in self.expressions:
                result.expressions.append(x/d)


            result.simplify()
            return result

    def __eq__(self, other):
        if self.decimal(15) == other.decimal(15):
            return True
        else:
            return False

    def __neg__(self):

        result = Number("")
        for x in self.expressions:
            result.expressions.append(-x)

        return result


    def decimal(self, decimalplaces = 2):
        result = 0
        for x in self.expressions:
            result += x.decimal(15)

        return round(result, decimalplaces)


