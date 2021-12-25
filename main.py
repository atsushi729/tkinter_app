#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox


class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=380,
                         borderwidth=1, relief='groove')

        self.message = tkinter.Message(self, aspect=300)
        self.text_box = tkinter.Entry(self)
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.confirm_message()

    def confirm_message(self):
        response = messagebox.askyesno('確認', 'Do you wanna continue?')
        if response == True:
            self.create_widgets()
        else:
            msg = messagebox.showinfo("hi", "see you")
            self.message['text'] = msg
            response['command'] = self.root.destroy

    def create_widgets(self):
        # close buttom
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = 'close'
        quit_btn['fg'] = '#ff0000'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')

        self.text_box['width'] = 15
        self.text_box.pack()

        # submit button
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = 'exec'
        submit_btn['command'] = self.input_hundler
        submit_btn.pack()

        # pop-up button
        button_center1 = tkinter.Button(self)
        button_center1['text'] = 'do not push this'
        button_center1['command'] = self.show_message
        button_center1.pack(fill='y')

        # label
        # label = tkinter.Label(self.place(x = 10, y = 80))
        label = tkinter.Label(self)
        label['text'] = 'your name'
        label.pack(side = 'right')

        # text box
        # txt = tkinter.Entry(self.place(x = 90, y = 80))
        txt = tkinter.Entry(self)
        txt.pack(side = 'right')

        self.message.pack()

    def input_hundler(self):
        text = self.text_box.get()
        self.message['text'] = text + '!!'

    def show_message(self):
        msg = messagebox.showinfo("hi", "Hello World")
        self.message['text'] = msg


root = tkinter.Tk()
root.title('TYPE SOME')
root.geometry('400x300')
app = Application(root=root)
app.mainloop()
