import drawing_class as draw
from tkinter import *
import turtle
import re

class Interface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Polynomials")
        self.window.config(background="black")
        self.window.geometry("1000x700")

        self.first_frame()
        self.create_wigets()

        self.canvas = Canvas(master=self.window, width=500, height=500)
        self.canvas.config(background="green")
        self.canvas.pack()

        self.alex = turtle.RawTurtle(self.canvas)
        self.alex.pencolor("blue")

        #draw.scale = 5
        #draw.draw_integer_number(self.alex, "35")


        self.window.mainloop()

    def create_wigets(self):
        pass

    def first_frame(self):
        frame1 = Frame(self.window)
        frame2 = Frame(self.window)
        frame3 = Frame(self.window)
        frame1.config(background="black")
        frame2.config(background="black")
        frame3.config(background="black")

        frame1.pack()
        frame2.pack()
        frame3.pack()

        label1 = Label(frame1, text="Enter degree of polynomial:", font=("Courier", 16),
                       background="black", foreground="orange")

        self.entry1 = Entry(frame2, font=("Courier", 14),
                            background="white", foreground="black", justify=CENTER, width=5)

        sep1 = Label(frame2, text="   ", background="black", foreground="black")

        sep2 = Label(frame2, text="   ", background="black", foreground="black")

        self.info = Label(frame2, font=("Courier", 14), text="Bad input!",
                          background="black", foreground="black")

        btn1 = Button(frame2, text="Enter", font=("Courier", 14), command=self.check,
                      background="blue", foreground="black", justify=CENTER)


        sep3 = Label(frame3, text=" ", font=("Courier", 3),
                     background="black", foreground="black")

        label1.pack(side=LEFT)
        self.entry1.pack(side=LEFT)
        sep1.pack(side=LEFT)
        btn1.pack(side=LEFT)
        sep2.pack(side=LEFT)
        self.info.pack(side=LEFT)
        sep3.pack()

    def check(self):
        s = self.entry1.get()
        if re.match(r"^[1-9]+[0-9]*$",s):
            self.stage_2()
            self.info.config(foreground="black")
        else:
            self.info.config(foreground="red")

    def stage_2(self):
        pass








