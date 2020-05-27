class Polynomial:
    def __init__(self, name, coefficents):
        self.coeffs = coefficents
        while self.coeffs[0] == 0 and len(self.coeffs) != 1:
            del self.coeffs[0]
        self.name = name

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

    def get_degree_of_polynomial(self):
        while self.coeffs[0] == 0 and len(self.coeffs)!= 1:
            del self.coeffs[0]

        return  len(self.coeffs)-1

    def get_monomials(self):
        p = list(reversed(self.coeffs))
        mono = []
        variable = self.name[-2]
        if self.coeffs == [0]:
            return [0]
        for i in range(len(p)):
            if p[i] == 0 and False:
                mono.append(str(0))
            elif (str(p[i])[0] == "0" or (str(p[i])[0] == "-" and str(p[i])[1] == "0")) and not '.' in list(str(p[i])):
                pass
            elif i == 0:
                mono.append(str(p[i]))
            elif i == 1:
                if p[i] == 1:
                    mono.append("-")
                elif p[i] == -1:
                    mono.append("-" + variable)
                else:
                    mono.append(str(p[i]) + variable)
            else:
                if p[i] == 1:
                    mono.append(variable + "^" + str(i))
                elif p[i] == -1:
                    mono.append("-" + variable + "^" + str(i))
                else:
                    mono.append(str(p[i])+variable+"^"+str(i))
        return list(reversed(mono))

    def display(self):
        print(self.name, "=", self.get_monomials()[0], "", sep=" ", end="")
        t = 0
        for x in self.get_monomials():
            if x == "0":
                t += 1
        if t == len(self.get_monomials()):
            pass
        else:
            for i in range(1, len(self.get_monomials())):
                if list(self.get_monomials()[i])[0] == "-":
                    print(self.get_monomials()[i], end="")
                else:
                    print("+",self.get_monomials()[i],sep="", end="")
                print(" ", end="")
        print("")

    def __eq__(self, other):

        while self.coeffs[0] == 0 and len(self.coeffs)!= 1:
            del self.coeffs[0]

        while other.coeffs[0] == 0 and len(other.coeffs)!= 1:
            del other.coeffs[0]

        return self.coeffs == other.coeffs

    def __ne__(self, other):
        while self.coeffs[0] == 0 and len(self.coeffs)!= 1:
            del self.coeffs[0]

        while other.coeffs[0] == 0 and len(other.coeffs)!= 1:
            del other.coeffs[0]

        return self.coeffs != other.coeffs

    def __add__(self, other):
        a = list(reversed(self.coeffs))
        b = list(reversed(other.coeffs))
        if len(b) > len(a):
            a,b = b,a
        c = []
        for i in range(len(a)):
            if i < len(b):
                c.append(a[i]+b[i])
            else:
                c.append(a[i])

        return Polynomial("Added("+self.name[-2]+")",list(reversed(c)))

    def __sub__(self, other):
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

        return Polynomial("Subtracted(" + self.name[-2] + ")", list(reversed(c)))

    def __mul__(self, other):
        while self.coeffs[0] == 0 and len(self.coeffs)!= 1:
            del self.coeffs[0]
        p = []
        n = self.get_degree_of_polynomial()+other.get_degree_of_polynomial()
        for i in range(n+1):
            p.append(0)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                p[i+j] += self.coeffs[i]*other.coeffs[j]
        return Polynomial("Multiplied("+self.name[-2]+")", p)

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
