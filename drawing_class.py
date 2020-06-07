import turtle

scale = 10

def draw_test_frame(self):
    self.pencolor("white")
    self.pendown()
    self.forward(4 * scale)
    self.left(90)
    self.forward(7 * scale)
    self.left(90)
    self.forward(4 * scale)
    self.left(90)
    self.forward(7 * scale)
    self.left(90)
    self.pencolor("black")

def draw_space(self, units):
    self.penup()
    self.forward(units * scale)

def draw_0(self):
    self.penup()
    self.left(90)
    self.forward(2 * scale)
    self.right(90)
    self.left(-90)
    self.pendown()
    self.circle(2 * scale, 180)
    self.forward(3 * scale)
    self.circle(2 * scale, 180)
    self.forward(3 * scale)
    self.penup()
    self.forward(2 * scale)
    self.left(90)
    self.forward(4 * scale)

def draw_1(self):
    self.penup()
    self.forward(3.5 * scale)
    self.left(90)
    self.pendown()
    self.forward(7 * scale)
    self.left(135)
    self.forward(4.5 * scale)
    self.penup()
    self.right(180)
    self.forward(4.5 * scale)
    self.right(135)
    self.forward(7 * scale)
    self.left(90)
    self.forward(0.5 * scale)

def draw_2(self):
    self.penup()
    self.forward(4 * scale)
    self.right(180)
    self.pendown()
    self.forward(4 * scale)
    self.right(135)
    self.forward(5 * scale)
    self.circle(2 * scale, 225)
    self.penup()
    self.forward(4.95 * scale)
    self.left(90)
    self.forward(3.9 * scale)

def draw_3(self):
    self.penup()
    self.forward(0.25 * scale)
    self.left(90)
    self.forward(1.75 * scale)
    self.right(180)
    self.pendown()
    self.circle(1.75 * scale, 270)
    self.right(180)
    self.circle(1.75 * scale, 270)
    self.penup()
    self.forward(5.25 * scale)
    self.left(90)
    self.forward(3.75 * scale)

def draw_4(self):
    self.penup()
    self.forward(3 * scale)
    self.left(90)
    self.forward(4 * scale)
    self.right(180)
    self.pendown()
    self.forward(4 * scale)
    self.penup()
    self.right(180)
    self.forward(3 * scale)
    self.right(90)
    self.forward(scale)
    self.right(180)
    self.pendown()
    self.forward(4 * scale)
    self.right(120)
    self.forward(4.6 * scale)
    self.penup()
    self.right(180)
    self.forward(4.6 * scale)
    self.left(120)
    self.right(90)
    self.forward(3 * scale)
    self.left(90)
    self.forward(4 * scale)

def draw_5(self):
    self.penup()
    self.left(90)
    self.forward(2 * scale)
    self.right(180)
    self.pendown()
    self.circle(2 * scale, 270)
    self.forward(1.5 * scale)
    self.right(90)
    self.forward(3 * scale)
    self.right(90)
    self.forward(3.5 * scale)
    self.penup()
    self.right(90)
    self.forward(7 * scale)
    self.left(90)

def draw_6(self):
    self.penup()
    self.forward(2 * scale)
    self.pendown()
    self.circle(2 * scale, 360)
    self.penup()
    self.right(180)
    self.forward(2 * scale)
    self.right(90)
    self.forward(2 * scale)
    self.pendown()
    self.forward(3 * scale)
    self.right(90)
    self.penup()
    self.forward(4 * scale)
    self.right(270)
    self.pendown()
    self.circle(2 * scale, 180)
    self.penup()
    self.forward(5 * scale)
    self.left(90)
    self.forward(4 * scale)

def draw_7(self):
    self.penup()
    self.forward(scale)
    self.left(68)
    self.pendown()
    self.forward(7.5 * scale)
    self.left(112)
    self.forward(3.7 * scale)
    self.penup()
    self.right(180)
    self.forward(3.7 * scale)
    self.right(112)
    self.forward(4 * scale)
    self.pendown()
    self.right(68)
    self.forward(1.5 * scale)
    self.right(180)
    self.forward(3 * scale)
    self.penup()
    self.right(180)
    self.forward(1.5 * scale)
    self.left(68)
    self.forward(3.5 * scale)
    self.right(68)
    self.right(180)
    self.forward(3 * scale)

def draw_8(self):
    self.penup()
    self.forward(2 * scale)
    self.pendown()
    self.circle(1.75 * scale)
    self.penup()
    self.left(90)
    self.forward(3.5 * scale)
    self.pendown()
    self.right(90)
    self.circle(1.75 * scale)
    self.penup()
    self.forward(2 * scale)
    self.right(90)
    self.forward(3.5 * scale)
    self.left(90)

def draw_9(self):
    self.penup()
    self.left(90)
    self.forward(3.5 * scale)
    self.right(90)
    self.forward(2 * scale)
    self.pendown()
    self.circle(1.75 * scale)
    self.circle(1.75 * scale, 90)
    self.right(180)
    self.forward(3.5 * scale)
    self.right(180)
    self.circle(1.75 * scale, -180)
    self.penup()
    self.forward(1.75 * scale)
    self.left(90)
    self.forward(3.75 * scale)

def draw_left_bracket(self):
    self.penup()
    self.forward(4 * scale)
    self.pendown()
    self.circle(3.5*scale, -90)
    self.circle(3.5*scale, -90)
    self.penup()
    self.left(90)
    self.forward(7 * scale)
    self.left(90)

def draw_right_bracket(self):
    self.pendown()
    self.circle(3.5 * scale, 90)
    self.circle(3.5 * scale, 90)
    self.penup()
    self.left(90)
    self.forward(7 * scale)
    self.left(90)
    self.forward(4 * scale)

def draw_plus(self):
    self.penup()
    self.forward(0.5 * scale)
    self.left(90)
    self.forward(3.5 * scale)
    self.right(90)
    self.pendown()
    self.forward(3 * scale)
    self.penup()
    self.left(90)
    self.forward(1.5 * scale)
    self.left(90)
    self.forward(1.5 * scale)
    self.left(90)
    self.pendown()
    self.forward(3 * scale)
    self.penup()
    self.forward(2 * scale)
    self.left(90)
    self.forward(2 * scale)

def draw_minus(self):
    self.penup()
    self.forward(0.5 * scale)
    self.left(90)
    self.forward(3.5 * scale)
    self.right(90)
    self.pendown()
    self.forward(3 * scale)
    self.penup()
    self.forward(0.5 * scale)
    self.right(90)
    self.forward(3.5 * scale)
    self.left(90)

def draw_integer_number(self, number):
    for x in number:
        if x == "0":
            draw_0(self)
        elif x == "1":
            draw_1(self)
        elif x == "2":
            draw_2(self)
        elif x == "3":
            draw_3(self)
        elif x == "4":
            draw_4(self)
        elif x == "5":
            draw_5(self)
        elif x == "6":
            draw_6(self)
        elif x == "7":
            draw_7(self)
        elif x == "8":
            draw_8(self)
        elif x == "9":
            draw_9(self)
        elif x == "-":
            draw_minus(self)


def draw_root_symbol(self, howm_many_digits, degree = 2):
    global scale
    self.penup()
    self.right(90)
    self.forward(0.5 * scale)
    self.left(90)
    self.left(90)
    self.forward(3 * scale)
    self.pendown()
    self.right(90)
    scale = scale / 2
    draw_integer_number(self,degree)
    scale *= 2
    self.right(180)
    self.forward(2 * scale)
    self.right(90)
    self.right(180)
    self.forward(scale)
    self.right(180)
    self.pendown()
    self.right(90)
    self.forward(scale)
    self.right(60)
    self.forward(2.2 * scale)
    self.right(120)
    self.right(180)
    self.left(75)
    self.forward(8 * scale)
    self.right(75)
    self.forward(howm_many_digits * 4 * scale)
    self.forward(0.5 * scale)
    self.right(90)
    self.forward(scale)
    self.left(90)
    self.penup()
    self.right(180)
    self.forward(howm_many_digits * 4 * scale)
    self.forward(0.65 * scale)
    self.left(90)
    self.forward(6.3 * scale)
    self.left(90)

def draw_root(self, number_under_root, degree = "2"):
    global scale
    h_m_d = len(number_under_root)
    draw_root_symbol(self,h_m_d, degree)
    draw_integer_number(self,number_under_root)
    self.forward(scale)

def draw_x(self, power = "-"):
    global scale
    self.pendown()
    self.left(45)
    self.forward(pow(2, (1 / 2)) * 4 * scale)
    self.left(225)
    self.penup()
    self.forward(4 * scale)
    self.left(225)
    self.pendown()
    self.forward(pow(2, (1 / 2)) * 4 * scale)
    self.left(225)
    self.penup()
    self.forward(4 * scale)
    self.right(90)
    self.forward(scale)
    self.left(90)
    if power != "-":
        scale /= 2
        draw_integer_number(self,power)
        scale *= 2
    self.right(90)
    self.forward(3 * scale)
    self.left(90)


def draw_fraction(self, numerator, denominator):
    global scale
    self.penup()
    self.right(90)
    self.forward(scale)
    self.left(90)
    n1 = len(numerator)
    n2 = len(denominator)
    n = max(n1, n2)
    scale /= 2
    self.forward((n-n2)*scale*2)
    self.pendown()
    draw_integer_number(self,denominator)
    self.forward((n - n2) * scale * 2)
    self.left(90)
    self.forward(7 * scale)
    self.forward(scale)
    self.left(90)
    self.pendown()
    self.forward(n * scale * 4)
    self.penup()
    self.right(90)
    self.forward(scale)
    self.right(90)
    self.forward((n-n1)*scale*2)
    draw_integer_number(self,numerator)
    self.forward((n - n1) * scale * 2)
    self.right(90)
    self.forward(7 * scale)
    self.left(90)
    scale *= 2

def draw_number(self, number): # from format: 'number_class.py'
    global scale
    if len(number.expressions) > 1:
        draw_left_bracket()

    for i in range(len(number.expressions)):
        x = number.expressions[i]
        if i == 0 and x.decimal(15) < 0 and x.coefficient.denominator != 1:
            draw_minus(self)
        elif i == 0 or (x.decimal(15) < 0 and x.coefficient.denominator == 1):
            pass
        elif x.decimal(15) < 0:
            draw_minus(self)
        else:
            draw_plus(self)
        if x.coefficient.decimal(15) == 1 and pow(x.number, (1/x.degree)) == 1:
            draw_1(self)
        elif x.coefficient.decimal(15) == -1 and pow(x.number, (1/x.degree)) == 1:
            draw_minus(self)
            draw_1(self)
        if x.coefficient.decimal(15) == 1 and pow(x.number, (1 / x.degree)) != 1:
            pass
        elif x.coefficient.decimal(15) == -1 and pow(x.number, (1 / x.degree)) != 1:
            draw_minus(self)
        elif x.coefficient.denominator == 1:
            draw_integer_number(self,str(int(x.coefficient.numerator)))
        elif x.coefficient.denominator == -1:
            draw_minus(self)
            draw_integer_number(self,str(int(x.coefficient.numerator)))
        else:
            draw_fraction(self,str(abs(int(x.coefficient.numerator))), str(abs(int(x.coefficient.denominator))))
            draw_space(self,1)

        if pow(x.number, (1/x.degree)) != 1:
            draw_root(self,str(int(x.number)), str(int(x.degree)))

    if len(number.expressions) > 1:
        draw_right_bracket(self)

"""
def draw_number_to_poly(self, number): # from format: 'number_class.py'
    if len(number.expressions) > 1:
        draw_left_bracket()

    for i in range(len(number.expressions)):
        x = number.expressions[i]
        if i == 0 or (x.decimal(15) < 0 and x.coefficient.denominator == 1):
            pass
        elif x.decimal(15) < 0:
            draw_minus()
        else:
            draw_plus()
        if x.coefficient.decimal(15) == 1:
            pass
        elif x.coefficient.decimal(15) == -1:
            draw_minus()
        elif x.coefficient.denominator == 1:
            draw_integer_number(str(int(x.coefficient.numerator)))
        elif x.coefficient.denominator == -1:
            draw_minus()
            draw_integer_number(str(int(x.coefficient.numerator)))
        else:
            draw_fraction(str(abs(int(x.coefficient.numerator))), str(abs(int(x.coefficient.denominator))))
            draw_space(1)

        if pow(x.number, (1/x.degree)) != 1:
            draw_root(str(int(x.number)), str(int(x.degree)))

    if len(number.expressions) > 1:
        draw_right_bracket()
"""