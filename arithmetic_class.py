import fraction_class as f

class Arithmetic:

    def __init__(self,**kwargs):    # give the data first by specifying the type
        ints = []                   # integers [i1,i2,...]: i = n           ==> an integer with value n
        frac = []                   # fractions [f1,f2,...]: f = (x,y)      ==> a fraction x/y
        self.roots = []             # roots [r1,r2,...]: r = (a,n,x)        ==> a * root of nth degree with x
        self.complex = []           # available in the future

        for key, value in kwargs.items():
            if key == "i":
                for x in value:
                    ints.append(x)
            elif key == "f":
                for x in value:
                    frac.append(x)
            elif key == "r":
                for x in value:
                    self.roots.append(x)
            elif key == "ac" or key == "tcd" or key == "tcr":
                for x in value:
                    self.complex.append(x)

        self.integer = 0
        for x in ints:
            self.integer += x

        self.fraction = f.Fraction(0,1)
        for x in frac:
            self.fraction += f.Fraction(x[0], x[1])

    def __repr__(self):
        pass

    def __add__(self, other):           # +
        pass

    def __sub__(self, other):           # -
        pass

    def __mul__(self, other):           # *
        pass

    def __truediv__(self, other):       # /
        pass

    def __floordiv__(self, other):      # //
        pass

    def __mod__(selfs):                 # %
        pass

    def __lt__(self, other):            # <
        pass

    def __gt__(self, other):            # >
        pass

    def __le__(self):                  # <=
        pass

    def __ge__(self):                   # >=
        pass

    def __eq__(self, other):            # ==
        pass

    def __ne__(self, other):            # !=
        pass

    def __pow__(self, power, modulo=None):      # **
        pass


