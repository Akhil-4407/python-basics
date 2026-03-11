from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="New Text",font=("Arial",24,"bold"))

my_label.grid(column=0,row=0)

def button_clicked():
    my_label["text"] = input.get()
button = Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)
def button_not():
    print("Hope not")
button_2 = Button(text="Rather not",command=button_not)
button_2.grid(column=2,row=0)

input = Entry()
input.grid(column=3,row=2)

window.mainloop()