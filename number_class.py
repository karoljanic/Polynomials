import fraction_class as fraction
import root_class as root
import re

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
                self.expressions.append(root.Root(int(k)))
            elif k == "":
                self.expressions.append(root.Root(0))
            else:
                raise TypeError


    def __repr__(self):     # printing style
        result = ""
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

