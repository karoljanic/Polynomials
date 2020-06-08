import drawing_class as d
import number_class as number
import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("green")
d.scale = 5

num = number.Number("-2/9", "(2/3)*5^(1/2)", "5^(1/3)")

d.draw_number(t, num)
