import turtle


class Drawing:
    def __init__(self):
        self.alex = turtle.Turtle()
        self.window = turtle.Screen()
        self.window.bgcolor("green")
        self.window.tracer(1)
        self.alex.pencolor("black")
        self.alex.pensize = 0.2

        self.scale = 25

    def draw_test_frame(self):
        self.alex.pencolor("white")
        self.alex.pendown()
        self.alex.forward(4 * self.scale)
        self.alex.left(90)
        self.alex.forward(7 * self.scale)
        self.alex.left(90)
        self.alex.forward(4 * self.scale)
        self.alex.left(90)
        self.alex.forward(7 * self.scale)
        self.alex.left(90)
        self.alex.pencolor("black")

    def draw_space(self, units):
        self.alex.penup()
        self.alex.forward(units * self.scale)

    def draw_0(self):
        self.alex.penup()
        self.alex.left(90)
        self.alex.forward(2 * self.scale)
        self.alex.right(90)
        self.alex.left(-90)
        self.alex.pendown()
        self.alex.circle(2 * self.scale, 180)
        self.alex.forward(3 * self.scale)
        self.alex.circle(2 * self.scale, 180)
        self.alex.forward(3 * self.scale)
        self.alex.penup()
        self.alex.forward(2 * self.scale)
        self.alex.left(90)
        self.alex.forward(4 * self.scale)

    def draw_1(self):
        self.alex.penup()
        self.alex.forward(3.5 * self.scale)
        self.alex.left(90)
        self.alex.pendown()
        self.alex.forward(7 * self.scale)
        self.alex.left(135)
        self.alex.forward(4.5 * self.scale)
        self.alex.penup()
        self.alex.right(180)
        self.alex.forward(4.5 * self.scale)
        self.alex.right(135)
        self.alex.forward(7 * self.scale)
        self.alex.left(90)
        self.alex.forward(0.5 * self.scale)

    def draw_2(self):
        self.alex.penup()
        self.alex.forward(4 * self.scale)
        self.alex.right(180)
        self.alex.pendown()
        self.alex.forward(4 * self.scale)
        self.alex.right(135)
        self.alex.forward(5 * self.scale)
        self.alex.circle(2 * self.scale, 225)
        self.alex.penup()
        self.alex.forward(4.95 * self.scale)
        self.alex.left(90)
        self.alex.forward(3.9 * self.scale)

    def draw_3(self):
        self.alex.penup()
        self.alex.forward(0.25 * self.scale)
        self.alex.left(90)
        self.alex.forward(1.75 * self.scale)
        self.alex.right(180)
        self.alex.pendown()
        self.alex.circle(1.75 * self.scale, 270)
        self.alex.right(180)
        self.alex.circle(1.75 * self.scale, 270)
        self.alex.penup()
        self.alex.forward(5.25 * self.scale)
        self.alex.left(90)
        self.alex.forward(3.75 * self.scale)

    def draw_4(self):
        self.alex.penup()
        self.alex.forward(3 * self.scale)
        self.alex.left(90)
        self.alex.forward(4 * self.scale)
        self.alex.right(180)
        self.alex.pendown()
        self.alex.forward(4 * self.scale)
        self.alex.penup()
        self.alex.right(180)
        self.alex.forward(3 * self.scale)
        self.alex.right(90)
        self.alex.forward(self.scale)
        self.alex.right(180)
        self.alex.pendown()
        self.alex.forward(4 * self.scale)
        self.alex.right(120)
        self.alex.forward(4.6 * self.scale)
        self.alex.penup()
        self.alex.right(180)
        self.alex.forward(4.6 * self.scale)
        self.alex.left(120)
        self.alex.right(90)
        self.alex.forward(3 * self.scale)
        self.alex.left(90)
        self.alex.forward(4 * self.scale)

    def draw_5(self):
        self.alex.penup()
        self.alex.left(90)
        self.alex.forward(2 * self.scale)
        self.alex.right(180)
        self.alex.pendown()
        self.alex.circle(2 * self.scale, 270)
        self.alex.forward(1.5 * self.scale)
        self.alex.right(90)
        self.alex.forward(3 * self.scale)
        self.alex.right(90)
        self.alex.forward(3.5 * self.scale)
        self.alex.penup()
        self.alex.right(90)
        self.alex.forward(7 * self.scale)
        self.alex.left(90)

    def draw_6(self):
        self.alex.penup()
        self.alex.forward(2 * self.scale)
        self.alex.pendown()
        self.alex.circle(2 * self.scale, 360)
        self.alex.penup()
        self.alex.right(180)
        self.alex.forward(2 * self.scale)
        self.alex.right(90)
        self.alex.forward(2 * self.scale)
        self.alex.pendown()
        self.alex.forward(3 * self.scale)
        self.alex.right(90)
        self.alex.penup()
        self.alex.forward(4 * self.scale)
        self.alex.right(270)
        self.alex.pendown()
        self.alex.circle(2 * self.scale, 180)
        self.alex.penup()
        self.alex.forward(5 * self.scale)
        self.alex.left(90)
        self.alex.forward(4 * self.scale)

    def draw_7(self):
        self.alex.penup()
        self.alex.forward(self.scale)
        self.alex.left(68)
        self.alex.pendown()
        self.alex.forward(7.5 * self.scale)
        self.alex.left(112)
        self.alex.forward(3.7 * self.scale)
        self.alex.penup()
        self.alex.right(180)
        self.alex.forward(3.7 * self.scale)
        self.alex.right(112)
        self.alex.forward(4 * self.scale)
        self.alex.pendown()
        self.alex.right(68)
        self.alex.forward(1.5 * self.scale)
        self.alex.right(180)
        self.alex.forward(3 * self.scale)
        self.alex.penup()
        self.alex.right(180)
        self.alex.forward(1.5 * self.scale)
        self.alex.left(68)
        self.alex.forward(3.5 * self.scale)
        self.alex.right(68)
        self.alex.right(180)
        self.alex.forward(3 * self.scale)

    def draw_8(self):
        self.alex.penup()
        self.alex.forward(2 * self.scale)
        self.alex.pendown()
        self.alex.circle(1.75 * self.scale)
        self.alex.penup()
        self.alex.left(90)
        self.alex.forward(3.5 * self.scale)
        self.alex.pendown()
        self.alex.right(90)
        self.alex.circle(1.75 * self.scale)
        self.alex.penup()
        self.alex.forward(2 * self.scale)
        self.alex.right(90)
        self.alex.forward(3.5 * self.scale)
        self.alex.left(90)

    def draw_9(self):
        self.alex.penup()
        self.alex.left(90)
        self.alex.forward(3.5 * self.scale)
        self.alex.right(90)
        self.alex.forward(2 * self.scale)
        self.alex.pendown()
        self.alex.circle(1.75 * self.scale)
        self.alex.circle(1.75 * self.scale, 90)
        self.alex.right(180)
        self.alex.forward(3.5 * self.scale)
        self.alex.right(180)
        self.alex.circle(1.75 * self.scale, -180)
        self.alex.penup()
        self.alex.forward(1.75 * self.scale)
        self.alex.left(90)
        self.alex.forward(3.75 * self.scale)

    def draw_left_bracket(self):
        self.alex.penup()
        self.alex.forward(4 * self.scale)
        self.alex.pendown()
        self.alex.circle(3.5*self.scale, -90)
        self.alex.circle(3.5*self.scale, -90)
        self.alex.penup()
        self.alex.left(90)
        self.alex.forward(7 * self.scale)
        self.alex.left(90)

    def draw_right_bracket(self):
        self.alex.pendown()
        self.alex.circle(3.5 * self.scale, 90)
        self.alex.circle(3.5 * self.scale, 90)
        self.alex.penup()
        self.alex.left(90)
        self.alex.forward(7 * self.scale)
        self.alex.left(90)
        self.alex.forward(4 * self.scale)

    def draw_plus(self):
        self.alex.penup()
        self.alex.forward(0.5 * self.scale)
        self.alex.left(90)
        self.alex.forward(3.5 * self.scale)
        self.alex.right(90)
        self.alex.pendown()
        self.alex.forward(3 * self.scale)
        self.alex.penup()
        self.alex.left(90)
        self.alex.forward(1.5 * self.scale)
        self.alex.left(90)
        self.alex.forward(1.5 * self.scale)
        self.alex.left(90)
        self.alex.pendown()
        self.alex.forward(3 * self.scale)
        self.alex.penup()
        self.alex.forward(2 * self.scale)
        self.alex.left(90)
        self.alex.forward(2 * self.scale)

    def draw_minus(self):
        self.alex.penup()
        self.alex.forward(0.5 * self.scale)
        self.alex.left(90)
        self.alex.forward(3.5 * self.scale)
        self.alex.right(90)
        self.alex.pendown()
        self.alex.forward(3 * self.scale)
        self.alex.penup()
        self.alex.forward(0.5 * self.scale)
        self.alex.right(90)
        self.alex.forward(3.5 * self.scale)
        self.alex.left(90)

    def draw_integer_number(self, number):
        for x in number:
            if x == "0":
                self.draw_0()
            elif x == "1":
                self.draw_1()
            elif x == "2":
                self.draw_2()
            elif x == "3":
                self.draw_3()
            elif x == "4":
                self.draw_4()
            elif x == "5":
                self.draw_5()
            elif x == "6":
                self.draw_6()
            elif x == "7":
                self.draw_7()
            elif x == "8":
                self.draw_8()
            elif x == "9":
                self.draw_9()
            elif x == "-":
                self.draw_minus()

    def draw_root_symbol(self, howm_many_digits, degree = 2):
        self.alex.penup()
        self.alex.right(90)
        self.alex.forward(0.5 * self.scale)
        self.alex.left(90)
        self.alex.left(90)
        self.alex.forward(3 * self.scale)
        self.alex.pendown()
        self.alex.right(90)
        self.scale /= 2
        self.draw_integer_number(degree)
        self.scale *= 2
        self.alex.right(180)
        self.alex.forward(2 * self.scale)
        self.alex.right(90)
        self.alex.right(180)
        self.alex.forward(self.scale)
        self.alex.right(180)
        self.alex.pendown()
        self.alex.right(90)
        self.alex.forward(self.scale)
        self.alex.right(60)
        self.alex.forward(2.2 * self.scale)
        self.alex.right(120)
        self.alex.right(180)
        self.alex.left(75)
        self.alex.forward(8 * self.scale)
        self.alex.right(75)
        self.alex.forward(howm_many_digits * 4 * self.scale)
        self.alex.forward(0.5 * self.scale)
        self.alex.right(90)
        self.alex.forward(self.scale)
        self.alex.left(90)
        self.alex.penup()
        self.alex.right(180)
        self.alex.forward(howm_many_digits * 4 * self.scale)
        self.alex.forward(0.65 * self.scale)
        self.alex.left(90)
        self.alex.forward(6.3 * self.scale)
        self.alex.left(90)

    def draw_root(self, number_under_root, degree = "2"):
        h_m_d = len(number_under_root)
        self.draw_root_symbol(h_m_d, degree)
        self.draw_integer_number(number_under_root)
        self.alex.forward(self.scale)

    def draw_x(self, power = "-"):
        self.alex.pendown()
        self.alex.left(45)
        self.alex.forward(pow(2, (1 / 2)) * 4 * self.scale)
        self.alex.left(225)
        self.alex.penup()
        self.alex.forward(4 * self.scale)
        self.alex.left(225)
        self.alex.pendown()
        self.alex.forward(pow(2, (1 / 2)) * 4 * self.scale)
        self.alex.left(225)
        self.alex.penup()
        self.alex.forward(4 * self.scale)
        self.alex.right(90)
        self.alex.forward(self.scale)
        self.alex.left(90)
        if power != "-":
            self.scale /= 2
            self.draw_integer_number(power)
            self.scale *= 2
        self.alex.right(90)
        self.alex.forward(3 * self.scale)
        self.alex.left(90)


    def draw_fraction(self, numerator, denominator):
        self.alex.penup()
        self.alex.right(90)
        self.alex.forward(self.scale)
        self.alex.left(90)
        n1 = len(numerator)
        n2 = len(denominator)
        n = max(n1, n2)
        self.scale /= 2
        self.alex.forward((n-n2)*self.scale*2)
        self.alex.pendown()
        self.draw_integer_number(denominator)
        self.alex.forward((n - n2) * self.scale * 2)
        self.alex.left(90)
        self.alex.forward(7 * self.scale)
        self.alex.forward(self.scale)
        self.alex.left(90)
        self.alex.pendown()
        self.alex.forward(n * self.scale * 4)
        self.alex.penup()
        self.alex.right(90)
        self.alex.forward(self.scale)
        self.alex.right(90)
        self.alex.forward((n-n1)*self.scale*2)
        self.draw_integer_number(numerator)
        self.alex.forward((n - n1) * self.scale * 2)
        self.alex.right(90)
        self.alex.forward(7 * self.scale)
        self.alex.left(90)
        self.scale *= 2

    def draw_number(self, number): # from format: 'number_class.py'
        if len(number.expressions) > 1:
            self.draw_left_bracket()

        for i in range(len(number.expressions)):
            x = number.expressions[i]
            if i == 0 and x.decimal(15) < 0 and x.coefficient.denominator != 1:
                self.draw_minus()
            elif i == 0 or (x.decimal(15) < 0 and x.coefficient.denominator == 1):
                pass
            elif x.decimal(15) < 0:
                self.draw_minus()
            else:
                self.draw_plus()
            if x.coefficient.decimal(15) == 1 and pow(x.number, (1/x.degree)) == 1:
                self.draw_1()
            elif x.coefficient.decimal(15) == -1 and pow(x.number, (1/x.degree)) == 1:
                self.draw_minus()
                self.draw_1()
            if x.coefficient.decimal(15) == 1 and pow(x.number, (1 / x.degree)) != 1:
                pass
            elif x.coefficient.decimal(15) == -1 and pow(x.number, (1 / x.degree)) != 1:
                self.draw_minus()
            elif x.coefficient.denominator == 1:
                self.draw_integer_number(str(int(x.coefficient.numerator)))
            elif x.coefficient.denominator == -1:
                self.draw_minus()
                self.draw_integer_number(str(int(x.coefficient.numerator)))
            else:
                self.draw_fraction(str(abs(int(x.coefficient.numerator))), str(abs(int(x.coefficient.denominator))))
                self.draw_space(1)

            if pow(x.number, (1/x.degree)) != 1:
                self.draw_root(str(int(x.number)), str(int(x.degree)))

        if len(number.expressions) > 1:
            self.draw_right_bracket()

    def draw_number_to_poly(self, number): # from format: 'number_class.py'
        if len(number.expressions) > 1:
            self.draw_left_bracket()

        for i in range(len(number.expressions)):
            x = number.expressions[i]
            if i == 0 or (x.decimal(15) < 0 and x.coefficient.denominator == 1):
                pass
            elif x.decimal(15) < 0:
                self.draw_minus()
            else:
                self.draw_plus()
            if x.coefficient.decimal(15) == 1:
                pass
            elif x.coefficient.decimal(15) == -1:
                self.draw_minus()
            elif x.coefficient.denominator == 1:
                self.draw_integer_number(str(int(x.coefficient.numerator)))
            elif x.coefficient.denominator == -1:
                self.draw_minus()
                self.draw_integer_number(str(int(x.coefficient.numerator)))
            else:
                self.draw_fraction(str(abs(int(x.coefficient.numerator))), str(abs(int(x.coefficient.denominator))))
                self.draw_space(1)

            if pow(x.number, (1/x.degree)) != 1:
                self.draw_root(str(int(x.number)), str(int(x.degree)))

        if len(number.expressions) > 1:
            self.draw_right_bracket()
