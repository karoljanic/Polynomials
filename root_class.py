import fraction_class as f

class Root:
    def __init__(self,coefficient,degree,number):
        self.coefficient = coefficient
        self.degree = degree
        self.number = number

    def __repr__(self):
        if self.degree == 1 and self.number == 1:
            return ("{}".format(self.coefficient))
        else:
            return ("{}*({}^(1/{}))".format(self.coefficient,int(self.number),int(self.degree)))

    def simplify(self):
        d = []
        i = 2
        y = self.number
        while y != 1:
            if y%i == 0:
                d.append(i)
                y /= i
            else:
                i += 1
        for i in d:
            if d.count(i) >= self.degree:
                for j in range(self.degree):
                    d.remove(i)
                self.number/=i**self.degree
                self.coefficient *= i

        for i in d:
            if self.degree % (d.count(i)) == 0 and d.count(i) != 1:
                self.degree/= d.count(i)
                self.degree = int(self.degree)
                self.number = i
                for j in range(d.count(i)-1):
                    d.remove(i)

        if self.number == 1:
            self.degree = 1


    def decimal(self, decimalplaces = 2):       # max decimalplaces = 15
        return round(self.coefficient * self.number**(1/self.degree),decimalplaces)


class Roots:
    def __init__(self, roots):
        self.roots = roots

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

