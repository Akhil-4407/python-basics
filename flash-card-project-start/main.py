BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
try:
    data_list = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_list = pd.read_csv("./data/french_words.csv")
    print("working")
data_list = data_list.to_dict(orient="records")
card= ""
timer=""
def on_click():
    global card,timer,data_list
    card = random.choice(data_list)
    timer = window.after_cancel(timer)
    canvas.itemconfig(card_front,image=card_img)
    canvas.itemconfig(french_label,text="French",fill="black")
    canvas.itemconfig(french_word,text=f"{card["French"]}",fill="black")
    timer = window.after(3000,reverse,card)


def known_click():
    global data_list,card
    data_list.remove(card)
    known = pd.DataFrame(data_list)
    known.to_csv("./data/words_to_learn.csv",index=False)
    on_click()


def reverse(a):
    
    canvas.itemconfig(card_front,image=opp_img)
    canvas.itemconfig(french_label,text="English",fill="white")
    canvas.itemconfig(french_word,text=f"{a["English"]}",fill="white")


window = Tk()
window.config(padx=50,pady=50)
window.configure(bg=BACKGROUND_COLOR)
timer = window.after(3000,reverse,card)

canvas = Canvas(width=800,height=526)
card_img= PhotoImage(file="./images/card_front.png")
card_front= canvas.create_image(400,263,image=card_img)
canvas.grid(column=0,row=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)


tick_image = PhotoImage(file="./images/right.png")
opp_img = PhotoImage(file="./images/card_back.png")


french_label = canvas.create_text(400,150,text=f"Title",font=("Ariel",40,"italic"))
french_word = canvas.create_text(400,263,text=f"Word",font=("Ariel",60,"bold"))

tick_button = Button(image=tick_image,highlightthickness=0,command=known_click)
tick_button.grid(column=1,row=1)


cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image,highlightthickness=0,command=on_click)
cross_button.grid(column=0,row=1)

on_click()
window.mainloop()