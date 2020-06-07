import drawing_class as d
import number_class as number
import turtle

num = number.Number("-8/9")

t = turtle.Turtle()
turtle.Screen().bgcolor("green")
d.scale = 5
d.draw_number(t,num)



