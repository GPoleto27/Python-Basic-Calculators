#! /usr/bin/env python3

import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master=None):
        self.main = tk.Frame(master)
        self.main["padx"] = 10
        self.main["pady"] = 10
        self.main.pack()

        self.expression = tk.StringVar()

        def pushInput(value):
            self.expression.set(self.expression.get() + value)

        def backspace():
            self.expression.set(self.expression.get()[0:-1])

        def evaluate():
            self.expression.set(eval(self.expression.get()))

        self.inputFrame = tk.Frame(self.main)
        self.inputFrame.pack(side="top")

        self.keyboardFrame = tk.Frame(self.main)
        self.keyboardFrame.pack(side="bottom")

        self.input = tk.Entry(self.inputFrame)
        self.input["width"] = 17
        self.input["textvariable"] = self.expression

        self.clear = tk.Button(self.inputFrame)
        self.clear["text"] = "<"
        self.clear["command"] = lambda: backspace()

        self.n1 = tk.Button(self.keyboardFrame)
        self.n1["text"] = "1"
        self.n1["height"] = 1
        self.n1["width"] = 1
        self.n1["command"] = lambda: pushInput("1")

        self.n2 = tk.Button(self.keyboardFrame)
        self.n2["text"] = "2"
        self.n2["height"] = 1
        self.n2["width"] = 1
        self.n2["command"] = lambda: pushInput("2")

        self.n3 = tk.Button(self.keyboardFrame)
        self.n3["text"] = "3"
        self.n3["height"] = 1
        self.n3["width"] = 1
        self.n3["command"] = lambda: pushInput("3")

        self.n4 = tk.Button(self.keyboardFrame)
        self.n4["text"] = "4"
        self.n4["height"] = 1
        self.n4["width"] = 1
        self.n4["command"] = lambda: pushInput("4")

        self.n5 = tk.Button(self.keyboardFrame)
        self.n5["text"] = "5"
        self.n5["height"] = 1
        self.n5["width"] = 1
        self.n5["command"] = lambda: pushInput("5")

        self.n6 = tk.Button(self.keyboardFrame)
        self.n6["text"] = "6"
        self.n6["height"] = 1
        self.n6["width"] = 1
        self.n6["command"] = lambda: pushInput("6")

        self.n7 = tk.Button(self.keyboardFrame)
        self.n7["text"] = "7"
        self.n7["height"] = 1
        self.n7["width"] = 1
        self.n7["command"] = lambda: pushInput("7")

        self.n8 = tk.Button(self.keyboardFrame)
        self.n8["text"] = "8"
        self.n8["height"] = 1
        self.n8["width"] = 1
        self.n8["command"] = lambda: pushInput("8")

        self.n9 = tk.Button(self.keyboardFrame)
        self.n9["text"] = "9"
        self.n9["height"] = 1
        self.n9["width"] = 1
        self.n9["command"] = lambda: pushInput("9")

        self.n0 = tk.Button(self.keyboardFrame)
        self.n0["text"] = "0"
        self.n0["height"] = 1
        self.n0["width"] = 1
        self.n0["command"] = lambda: pushInput("0")

        self.point = tk.Button(self.keyboardFrame)
        self.point["text"] = "."
        self.point["height"] = 1
        self.point["width"] = 1
        self.point["command"] = lambda: pushInput(".")

        self.equal = tk.Button(self.keyboardFrame)
        self.equal["text"] = "="
        self.equal["height"] = 1
        self.equal["width"] = 1
        self.equal["command"] = lambda: evaluate()

        self.plus = tk.Button(self.keyboardFrame)
        self.plus["text"] = "+"
        self.plus["height"] = 1
        self.plus["width"] = 1
        self.plus["command"] = lambda: pushInput("+")

        self.minus = tk.Button(self.keyboardFrame)
        self.minus["text"] = "-"
        self.minus["height"] = 1
        self.minus["width"] = 1
        self.minus["command"] = lambda: pushInput("-")

        self.times = tk.Button(self.keyboardFrame)
        self.times["text"] = "X"
        self.times["height"] = 1
        self.times["width"] = 1
        self.times["command"] = lambda: pushInput("*")

        self.divide = tk.Button(self.keyboardFrame)
        self.divide["text"] = "/"
        self.divide["height"] = 1
        self.divide["width"] = 1
        self.divide["command"] = lambda: pushInput("/")

        self.mod = tk.Button(self.keyboardFrame)
        self.mod["text"] = "%"
        self.mod["height"] = 1
        self.mod["width"] = 1
        self.mod["command"] = lambda: pushInput("%")

        self.power = tk.Button(self.keyboardFrame)
        self.power["text"] = "^"
        self.power["height"] = 1
        self.power["width"] = 1
        self.power["command"] = lambda: pushInput("**")

        self.open = tk.Button(self.keyboardFrame)
        self.open["text"] = "("
        self.open["height"] = 1
        self.open["width"] = 1
        self.open["command"] = lambda: pushInput("(")

        self.close = tk.Button(self.keyboardFrame)
        self.close["text"] = ")"
        self.close["height"] = 1
        self.close["width"] = 1
        self.close["command"] = lambda: pushInput(")")

        self.input.grid (row=0, column=0)
        self.clear.grid (row=0, column=1)
        self.n1.grid    (row=1, column=0)
        self.n2.grid    (row=1, column=1)
        self.n3.grid    (row=1, column=2)
        self.n4.grid    (row=2, column=0)
        self.n5.grid    (row=2, column=1)
        self.n6.grid    (row=2, column=2)
        self.n7.grid    (row=3, column=0)
        self.n8.grid    (row=3, column=1)
        self.n9.grid    (row=3, column=2)
        self.n0.grid    (row=4, column=1)
        self.point.grid (row=4, column=0)
        self.equal.grid (row=4, column=2)
        self.plus.grid  (row=1, column=3)
        self.minus.grid (row=2, column=3)
        self.times.grid (row=3, column=3)
        self.divide.grid(row=4, column=3)
        self.mod.grid   (row=1, column=4)
        self.power.grid (row=2, column=4)
        self.open.grid  (row=3, column=4)
        self.close.grid (row=4, column=4)


root = tk.Tk()
root.title("Tkalculator")
Application(root)
root.mainloop()
