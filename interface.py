import drawing_class as draw
import polynomial_class as poly
from tkinter import *
import turtle
import re


class Interface():
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=1250, height=750, relief="raised")
        self.canvas.pack()
        self.window.title("Polynomials")
        self.canvas.config(bg="black")

        self.alex = turtle.RawTurtle(self.canvas)
        draw.scale = 4

        self.entry = Entry()
        self.info = Label()

        self.enter_frame()

        self.window.mainloop()

    def enter_frame(self):
        label1 = Label(self.window, text="Enter degree of polynomial:", font=("Courier", 16),
                       background="black", foreground="orange")

        self.entry = Entry(self.window, font=("Courier", 14), background="white", foreground="black",
                           justify=CENTER, width=5)

        self.info = Label(self.window, font=("Courier", 14), text="Bad input!",
                          background="black", foreground="black")

        enter_button = Button(self.window, text="Enter", font=("Courier", 14), command=self.check, background="blue",
                              foreground="black", justify=CENTER)

        self.canvas.create_window(300, 30, window=label1)
        self.canvas.create_window(225, 75, window=self.entry)
        self.canvas.create_window(325, 75, window=enter_button)
        self.canvas.create_window(450, 75, window=self.info)

    def check(self):
        s = self.entry.get()
        if re.match(r"^[1-9]+[0-9]*$", s):
            self.info.config(foreground="black")
            self.poly_frame()
        else:
            self.info.config(foreground="red")

    def set_start_pos(self):
        pass
        """
        self.alex.penup()
        self.alex.backward(self.canvas.winfo_width() / 2)
        self.alex.left(90)
        self.alex.forward(self.canvas.winfo_height() / 2)
        self.alex.backward(draw.scale * 7)
        self.alex.right(90)
        self.alex.forward(2 * draw.scale)
        """

    def monomial(self, wid):
        draw.draw_x(self.alex)

        entry1 = Entry(self.window, font=("Courier", 14),background="yellow", foreground="black", justify=CENTER, width=5)
        self.canvas.create_window(300+100*wid,500,window=entry1)
        entry1.pack()




    def poly_frame(self):
        for i in range(int(self.entry.get())):
            self.monomial(i)