#! /usr/bin/env python3

import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master=None):
        self.main = tk.Frame(master)
        self.main["padx"] = 25
        self.main["pady"] = 25
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
        self.input["textvariable"] = self.expression
        self.input.pack()

        self.clear = tk.Button(self.inputFrame)
        self.clear["text"] = "<"
        self.clear["command"] = lambda: backspace()
        self.clear.pack()

        self.n1 = tk.Button(self.keyboardFrame)
        self.n1["text"] = "1"
        self.n1["height"] = 1
        self.n1["width"] = 1
        self.n1["command"] = lambda: pushInput("1")
        self.n1.pack()

        self.n2 = tk.Button(self.keyboardFrame)
        self.n2["text"] = "2"
        self.n2["height"] = 1
        self.n2["width"] = 1
        self.n2["command"] = lambda: pushInput("2")
        self.n2.pack()

        self.n3 = tk.Button(self.keyboardFrame)
        self.n3["text"] = "3"
        self.n3["height"] = 1
        self.n3["width"] = 1
        self.n3["command"] = lambda: pushInput("3")
        self.n3.pack()

        self.n4 = tk.Button(self.keyboardFrame)
        self.n4["text"] = "4"
        self.n4["height"] = 1
        self.n4["width"] = 1
        self.n4["command"] = lambda: pushInput("4")
        self.n4.pack()

        self.n5 = tk.Button(self.keyboardFrame)
        self.n5["text"] = "5"
        self.n5["height"] = 1
        self.n5["width"] = 1
        self.n5["command"] = lambda: pushInput("5")
        self.n5.pack()

        self.n6 = tk.Button(self.keyboardFrame)
        self.n6["text"] = "6"
        self.n6["height"] = 1
        self.n6["width"] = 1
        self.n6["command"] = lambda: pushInput("6")
        self.n6.pack()

        self.n7 = tk.Button(self.keyboardFrame)
        self.n7["text"] = "7"
        self.n7["height"] = 1
        self.n7["width"] = 1
        self.n7["command"] = lambda: pushInput("7")
        self.n7.pack()

        self.n8 = tk.Button(self.keyboardFrame)
        self.n8["text"] = "8"
        self.n8["height"] = 1
        self.n8["width"] = 1
        self.n8["command"] = lambda: pushInput("8")
        self.n8.pack()

        self.n9 = tk.Button(self.keyboardFrame)
        self.n9["text"] = "9"
        self.n9["height"] = 1
        self.n9["width"] = 1
        self.n9["command"] = lambda: pushInput("9")
        self.n9.pack()

        self.n0 = tk.Button(self.keyboardFrame)
        self.n0["text"] = "0"
        self.n0["height"] = 1
        self.n0["width"] = 1
        self.n0["command"] = lambda: pushInput("0")
        self.n0.pack()

        self.equal = tk.Button(self.keyboardFrame)
        self.equal["text"] = "="
        self.equal["height"] = 1
        self.equal["width"] = 1
        self.equal["command"] = lambda: evaluate()
        self.equal.pack()

        self.plus = tk.Button(self.keyboardFrame)
        self.plus["text"] = "+"
        self.plus["height"] = 1
        self.plus["width"] = 1
        self.plus["command"] = lambda: pushInput("+")
        self.plus.pack()

        self.minus = tk.Button(self.keyboardFrame)
        self.minus["text"] = "-"
        self.minus["height"] = 1
        self.minus["width"] = 1
        self.minus["command"] = lambda: pushInput("-")
        self.minus.pack()

        self.times = tk.Button(self.keyboardFrame)
        self.times["text"] = "X"
        self.times["height"] = 1
        self.times["width"] = 1
        self.times["command"] = lambda: pushInput("*")
        self.times.pack()

        self.divide = tk.Button(self.keyboardFrame)
        self.divide["text"] = "/"
        self.divide["height"] = 1
        self.divide["width"] = 1
        self.divide["command"] = lambda: pushInput("/")
        self.divide.pack()

        self.mod = tk.Button(self.keyboardFrame)
        self.mod["text"] = "%"
        self.mod["height"] = 1
        self.mod["width"] = 1
        self.mod["command"] = lambda: pushInput("%")
        self.mod.pack()

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
        self.n0.grid    (row=4, column=0)
        self.equal.grid (row=4, column=1)
        self.mod.grid   (row=4, column=2)
        self.plus.grid  (row=1, column=3)
        self.minus.grid (row=2, column=3)
        self.times.grid (row=3, column=3)
        self.divide.grid(row=4, column=3)


root = tk.Tk()
root.title("Tkalculator")
Application(root)
root.mainloop()
