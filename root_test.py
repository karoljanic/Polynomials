import root_class as r
import fraction_class as f

x = r.Root(f.Fraction(2,3),2,24)
y = r.Root(8,2,288)
z = r.Root(5,4,64)
w = r.Root(9,2,49)

a = r.Roots([x,y])
b = r.Roots([z,w])

a.simplify()
b.simplify()

a.display()
b.display()

c = b-a
print("Wynik: ", end = "")
c.display()
print("")

