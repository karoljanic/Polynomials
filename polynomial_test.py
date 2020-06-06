import polynomial_class as poly


a = poly.Polynomial("P(x)", ["5/2", "-7", "0", "11"])
b = poly.Polynomial("R(x)", ["2", "6", "-4", "0"])
c = poly.Polynomial("S(x)", ["-2", "5", "0", "-3"])
d = poly.Polynomial("T(x)", ["2", "0", "12", "0"])
e = poly.Polynomial("U(x)", ["1", "2", "-1", "-4", "0", "1"])
f = poly.Polynomial("W(x)", ["-1", "5", "-6"])
g = poly.Polynomial("U(x)", ["0"])
h = poly.Polynomial("X(x)", ["7", "-2/3", "-1", "-0", "-3^(1/3)", "1", "-(2/3)*7^(1/5)"])

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print("")
h.draw_it()

print(a*b)
