import polynomial_class as poly


a = poly.Polynomial("P(x)", ["5/2", "-7", "0", "11"])
b = poly.Polynomial("R(x)", ["2", "6", "-4", "0"])
c = poly.Polynomial("S(x)", ["-2", "5", "0", "-3"])
d = poly.Polynomial("T(x)", ["2", "0", "12", "0"])
e = poly.Polynomial("U(x)", ["4", "2", "-3", "-4"])
f = poly.Polynomial("W(x)", ["-1", "5", "-6"])

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print("")

print(a*b)