import fraction_class as fraction
import root_class as root
import  re

class Number:
    # expressions can be:
    #       "x",                x must belong to integers;            it is a integer
    #       "a/b",              a,b must belong to integers,          a/b is a fraction
    #       "x^n",              x,n must belong to integers,          x to the power of n
    #       "a*x^n",            a,x,n must belong to integers;        a times x to the power of n
    #       "(a/b)*x^n",        a,b,x,n must belong to integers;      a/b times x to the power of n
    #       "x^(m/n)",          x,m,n must belong to integers;        n-th root of x to the power of m
    #       "a*x^(m/n)",        a,x,m,n must belong to integers;      a times n-th root of x to the power of m
    #       "(a/b)*x^(m/n),     a,b,x,m,n must belong to integers;    a/b times n-th root of x to the power of m

    def __init__(self, *args):  # provide expressions


    def __repr__(self):
        pass

    def __add__(self, other):
        self.simplify()
        other.simplify()

        result = Roots(self.roots + other.roots)
        result.simplify()

        return result

    def __sub__(self, other):
        self.simplify()
        other.simplify()

        for x in other.roots:
            x.coefficient *= -1

        result = Roots(self.roots + other.roots)
        result.simplify()

        return result

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def simplify(self):
        for x in self.roots:
            x.simplify()
        n = len(self.roots)
        for k in range(n):
            for i in range(n):
                for j in range(i+1,n):
                    try:
                        if self.roots[i].number == self.roots[j].number and self.roots[i].degree == self.roots[j].degree:
                            self.roots[i].coefficient += self.roots[j].coefficient
                            del self.roots[j]
                    except:
                        pass



    def decimal(self, decimalplaces=2):  # max decimalplaces = 15
        return round(self.coefficient * self.number ** (1 / self.degree), decimalplaces)

    def display(self):
        for x in self.roots:
            print(x, sep = " ", end = "   ")
        print("")