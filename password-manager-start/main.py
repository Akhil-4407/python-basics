from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for x in range(nr_letters)]


    syms = [random.choice(symbols) for x in range(nr_symbols)]
    password_list.extend(syms)


    nums= [random.choice(numbers) for x in range(nr_numbers)]
    password_list.extend(nums)
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)
    

def save():
    new_data = {web_entry.get():{
        "Email":email_entry.get(),
        "Password":pass_entry.get()
    }}
    if len(web_entry.get()) == 0 or len(pass_entry.get()) == 0: 
        messagebox.showinfo(title="Error",message="Please fill the empty fields")
    else:
        try:
            with open("./data.json","r") as file:
                data= json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("./data.json","w") as file:
                json.dump(data,file,indent=4)
                web_entry.delete(0,END)
                pass_entry.delete(0,END)
                
def search():
    if len(web_entry.get()) == 0:
        messagebox.showinfo(title="Error",message="No details of the Website are given.")
    else:
        try:
            with open("./data.json","r") as file:
                data = json.load(file)
        except:
            messagebox.showinfo(title="No data saved",message="No Data File Found.")
        else:
            if web_entry.get() in data:
                web_email = data[web_entry.get()]["Email"]
                web_pass = data[web_entry.get()]["Password"]
                messagebox.showinfo(title="Saved Data",message=f"Email: {web_email}\nPassword: {web_pass}")
            else:
                messagebox.showinfo(title="No Info",message="No detials present")


window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(width=200,height=200)
img= PhotoImage(file="./logo.png")
pass_img = canvas.create_image(100,100,image = img)
canvas.grid(column=1,row=0)


web_label = Label(text="Website:")
web_label.grid(column=0,row=1)


web_entry = Entry(width=35)
web_entry.grid(column=1,row=1)
web_entry.focus()


web_search = Button(text="Search",width=21,command=search)
web_search.grid(column=2,row=1)


email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)


email_entry = Entry(width=62)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"akhil.k.hlc0008@gmail.com")


pass_label = Label(text="Password:")
pass_label.grid(column=0,row=3)

pass_entry = Entry(width=35)
pass_entry.grid(column=1,row=3)

gen_button = Button(text="Generate Password",command=gen_pass,width=21)
gen_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()