import fraction_class as fraction
import root_class as root
import number_class as number
import polynomial_class as poly
import math

a = poly.Polynomial("P(x)", ["5/2", "-7", "0", "11"])
b = poly.Polynomial("R(x)", ["2", "6", "-4", "0"])
c = poly.Polynomial("S(x)", ["-2", "5", "0", "-3"])
d = poly.Polynomial("T(x)", ["2", "0", "12", "0"])
e = poly.Polynomial("U(x)", ["1", "2", "-1", "-4", "0", "1"])
f = poly.Polynomial("W(x)", ["-1", "5", "-6"])
g = poly.Polynomial("U(x)", ["2","3"])
h = poly.Polynomial("X(x)", ["7", "-2/3", "-1", "-0", "-3^(1/3)", "1", "-(2/3)*7^(1/5)"])
x = poly.Polynomial("X(x)", ["1", "3", "-10", "0", "0", "0"])
z = poly.Polynomial("Z(x)", ["1", "0", "4", "0"])
y = poly.Polynomial("Y(x)", ["1","-2","-13", "14", "24"])
w = poly.Polynomial("W(x)", ["35","24","-227","60","36","0","0"])

"""
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
"""
test2 = poly.Polynomial("T2(x)", ["1", "9", "-21", "-245", "0"])
test = poly.Polynomial("T(x)",["7", "-49","-56","602", "511", "-973", "-1974", "-9660", "-12600", "0"])
test3 = poly.Polynomial("T3(x)", ["1", "-3", "-9", "-9"])
print(test)
#print(test.find_rational_roots())
print(test.break_down_to_factor(False))

print("")
print(test3)
print(test3.break_down_to_factor(False))
"""
import drawing_class as d
import number_class as number
import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("green")
d.scale = 5

num = number.Number("-2/9", "(2/3)*5^(1/2)", "5^(1/3)")

d.draw_number(t, num)
"""






