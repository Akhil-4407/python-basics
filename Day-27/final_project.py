from tkinter import *
window = Tk()
window.minsize(width=300,height=50)
window.title("Miles to Kilometer convertor")
window.config(padx=20,pady=2)

input_miles = Entry()
input_miles.grid(column=1,row=0)

miles = Label(text="Miles")
miles.grid(column=2,row=0)


is_equal = Label(text="is equal to")

is_equal.grid(column=0,row=1)

result = Label(text="0")

result.grid(column=1,row=1)
def calc():
    ans = round(float(input_miles.get())*1.60934)
    result.config(text=f"{ans}") 
unit = Label(text="Km")

unit.grid(column=2,row=1)

button = Button(text="Calculate",command=calc)

button.grid(column=1,row=3)






window.mainloop()