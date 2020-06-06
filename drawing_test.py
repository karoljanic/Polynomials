import drawing_class as d
import number_class as number

drawing = d.Drawing()
drawing.scale = 4

num = number.Number( "34", "2^(1/3)")
drawing.draw_number(num)


drawing.window.exitonclick()
