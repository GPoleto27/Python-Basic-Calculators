#! /usr/bin/env python3

from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')


class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTKalculator")
        self.set_border_width(10)

        grid = Gtk.Grid()
        grid.set_column_spacing(2)
        grid.set_row_spacing(2)
        self.add(grid)

        self.entry = Gtk.Entry()
        grid.attach(self.entry, 0, 0, 4, 1)

        button = Gtk.Button.new_with_mnemonic("1")
        button.connect("clicked", self.pushInput, "1")
        grid.attach(button, 0, 1, 1, 1)

        button = Gtk.Button.new_with_mnemonic("2")
        button.connect("clicked", self.pushInput, "2")
        grid.attach(button, 1, 1, 1, 1)

        button = Gtk.Button.new_with_mnemonic("3")
        button.connect("clicked", self.pushInput, "3")
        grid.attach(button, 2, 1, 1, 1)

        button = Gtk.Button.new_with_mnemonic("4")
        button.connect("clicked", self.pushInput, "4")
        grid.attach(button, 0, 2, 1, 1)

        button = Gtk.Button.new_with_mnemonic("5")
        button.connect("clicked", self.pushInput, "5")
        grid.attach(button, 1, 2, 1, 1)

        button = Gtk.Button.new_with_mnemonic("6")
        button.connect("clicked", self.pushInput, "6")
        grid.attach(button, 2, 2, 1, 1)

        button = Gtk.Button.new_with_mnemonic("7")
        button.connect("clicked", self.pushInput, "7")
        grid.attach(button, 0, 3, 1, 1)

        button = Gtk.Button.new_with_mnemonic("8")
        button.connect("clicked", self.pushInput, "8")
        grid.attach(button, 1, 3, 1, 1)

        button = Gtk.Button.new_with_mnemonic("9")
        button.connect("clicked", self.pushInput, "9")
        grid.attach(button, 2, 3, 1, 1)

        button = Gtk.Button.new_with_mnemonic(".")
        button.connect("clicked", self.pushInput, ".")
        grid.attach(button, 0, 4, 1, 1)

        button = Gtk.Button.new_with_mnemonic("0")
        button.connect("clicked", self.pushInput, "0")
        grid.attach(button, 1, 4, 1, 1)

        button = Gtk.Button.new_with_mnemonic("=")
        button.connect("clicked", self.evaluate)
        grid.attach(button, 2, 4, 1, 1)

        button = Gtk.Button.new_with_mnemonic("+")
        button.connect("clicked", self.pushInput, "+")
        grid.attach(button, 3, 1, 1, 1)

        button = Gtk.Button.new_with_mnemonic("-")
        button.connect("clicked", self.pushInput, "-")
        grid.attach(button, 3, 2, 1, 1)

        button = Gtk.Button.new_with_mnemonic("X")
        button.connect("clicked", self.pushInput, "*")
        grid.attach(button, 3, 3, 1, 1)

        button = Gtk.Button.new_with_mnemonic("/")
        button.connect("clicked", self.pushInput, "/")
        grid.attach(button, 3, 4, 1, 1)

        button = Gtk.Button.new_with_mnemonic("<")
        button.connect("clicked", self.backspace)
        grid.attach(button, 4, 0, 1, 1)

        button = Gtk.Button.new_with_mnemonic("%")
        button.connect("clicked", self.pushInput, "%")
        grid.attach(button, 4, 1, 1, 1)

        button = Gtk.Button.new_with_mnemonic("^")
        button.connect("clicked", self.pushInput, "**")
        grid.attach(button, 4, 2, 1, 1)

        button = Gtk.Button.new_with_mnemonic("(")
        button.connect("clicked", self.pushInput, "(")
        grid.attach(button, 4, 3, 1, 1)

        button = Gtk.Button.new_with_mnemonic(")")
        button.connect("clicked", self.pushInput, ")")
        grid.attach(button, 4, 4, 1, 1)

    def backspace(self, button):
        self.entry.set_text(self.entry.get_text()[0:-1])

    def pushInput(self, button, input):
        self.entry.set_text(self.entry.get_text() + input)

    def evaluate(self, button):
        self.entry.set_text(str(eval(self.entry.get_text())))


win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
