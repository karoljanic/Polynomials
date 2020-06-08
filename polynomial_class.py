import number_class as number
import drawing_class as draw

class Polynomial:
    # coefficients must be given in the same way as numbers from 'number_class.py' in a one list
    # the name of the polynomial must contain its name and the variable in round brackets, e.g.: "P(x)", "Poly(a)"
    def __init__(self, name, coefficents):
        self.name = name
        self.coeffs = []
        for x in coefficents:
            self.coeffs.append(number.Number(x))
        self.simplify()

    def __repr__(self):
        self.simplify()
        val = 0
        for x in self.coeffs:
            if x.decimal(15) != 0:
                val +=1
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
            elif self.coeffs[i].decimal(15) != 0 :
                result += " +"
                result += str(self.coeffs[i])
                if n > 0:
                    result += variable
                if n > 1:
                    result += "^"+str(n)
            n -= 1

        newresult = ""
        for i in range(result.find("=")+2, len(result)):
            if result[i] == "1":
                if i+1 <len(result):
                    if result[i+1] == variable:
                        pass
                    else:
                        newresult += result[i]
                else:
                    newresult += result[i]
            else:
                newresult += result[i]

        return self.name+" = "+newresult

    def change_name(self, new_name):
        self.name = new_name

    def get_degree_of_polynomial(self):
        self.simplify()

        return len(self.coeffs)-1

    def get_monomials(self):
        self.simplify()
        return self.coeffs

    def simplify(self):
        val = 0
        for x in self.coeffs:
            if x.decimal(15) != 0:
                val += 1
        if val == 0:
            self.coeffs = [number.Number("0")]

        while self.coeffs[0].decimal(15) == 0 and len(self.coeffs)!= 1:
            self.coeffs.remove(self.coeffs[0])

    def __eq__(self, other):
        self.simplify()
        other.simplify()

        return self.coeffs == other.coeffs

    def __ne__(self, other):
        self.simplify()
        other.simplify()

        return self.coeffs != other.coeffs

    def __add__(self, other):
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

        result = Polynomial("Added("+self.name[-2]+")",[])
        result.coeffs = list(reversed(c))

        return result


    def __sub__(self, other):
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

    def __mul__(self, other):
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

    def get_value(self, argument):
        result = self.coeffs[0]
        n = len(self.coeffs)
        for i in range(1, n):
            result = result * argument + self.coeffs[i]

        return result

    def divisors(self,x):
        if x < 0:
            x = -x
        d = []
        for i in range(1,x+1):
            if x%i == 0:
                d.append(i)
        minus_d = [-x for x in reversed(d)]
        return (minus_d,d)

    def find_integer_roots(self):
        while self.coeffs[0] == 0 and len(self.coeffs)!= 1:
            del self.coeffs[0]
        r = set()
        if not isinstance(self.coeffs[-1],int):
            if len(r) == 0:
                r.add('-')
            return r
        if len(self.coeffs) == 1:
            if self.coeffs[0] == 0:
                r.add('R')
            else:
                r.add('-')
        elif self.coeffs[-1] == 0:
            c = self.coeffs
            r.add(0)
            while c[-1] == 0:
                del c[-1]
        else:
            c = self.coeffs

            d = self.divisors(c[-1])

            for i in range(len(d[0])):
                if self.get_value(d[0][i]) == 0:
                    r.add(d[0][i])
                if self.get_value(d[1][i]) == 0:
                    r.add(d[1][i])

        return r

    

    def __truediv__(self, other):       # Poly1 / Poly2
        print("div")

    def __floordiv__(self, other):      # Poly1 // Poly2
        print("flordiv")

    def __divmod__(self, other):        # Poly1 % Poly2
        print("divmod")
