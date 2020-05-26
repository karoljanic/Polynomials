import polynomial_class as p

wielomian1 = p.Polynomial( "P(x)",[-2,-3,6,3,-1,4,0])
wielomian1.display()
wielomian2 = p.Polynomial("R(x)", [-1, -2,4, 9, 3, 9,8])
wielomian2.display()

wielomian3 = wielomian1+wielomian2
print("P(x)+R(x) = ", end = "")
wielomian3.display()

wielomian4 = wielomian1-wielomian2
print("P(x)-R(x) = ", end = "")
wielomian4.display()

wielomian5 = p.Polynomial("A(y)", [25,-725,4575,-7875])  #roots: 21,3,5, A(-1) = -13200
wielomian5.display()
print("A(-1)=",wielomian5.get_value(-1))
print("Roots A(y):",(wielomian5.find_integer_roots()))

wielomian6 = p.Polynomial("B(x)", [1,1,0,-2,0])
wielomian6.display()
print("Roots B(x):",(wielomian6.find_integer_roots()))

wielomian7 = p.Polynomial("C(x)", [10,0,0,0])
wielomian7.display()
print("Roots C(x):",(wielomian7.find_integer_roots()))

wielomian8 = p.Polynomial("D(x)", [10])
wielomian8.display()
print("Roots D(x):",(wielomian8.find_integer_roots()))

wielomian9 = p.Polynomial("E(x)", [0])
wielomian9.display()
print("Roots E(x):",(wielomian9.find_integer_roots()))

wielomian8 = p.Polynomial("D(x)", [3,-14,-57,56])
wielomian9 = p.Polynomial("E(x)", [3,-14,3,2])

wynik = wielomian8*wielomian9
wynik.display()






