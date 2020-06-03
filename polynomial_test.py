import polynomial_class as poly

test = poly.Polynomial("P(x)", ["1", "2*2^(1/2)", "0", "1/2"])
test1 = poly.Polynomial("R(x)", ["0", "0"])
test2 = poly.Polynomial("P(x)", ["-1", "2*2^(1/2)","-7", "-0", "-1/2"])
test3 = poly.Polynomial("P(x)", ["0", "-1", "2*2^(1/2)","-7", "-0", "-1/2"])

print(test)

print(test1)

print(test2)

print(test2 != test3)

print(test3.get_degree_of_polynomial())
