from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = 1
timer = ""


def reset_timer():
    global check
    check = 1
    window.after_cancel(timer)
    canvas.itemconfig(time_count,text=f"00:00")
    timer_label.config(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 50))
    checkmark.config(text="",fg=GREEN,bg=YELLOW,highlightthickness=0)

def on_click():
    global check
    if check % 2 != 0:
        count_check(WORK_MIN*60)
        timer_label.config(text="WORK",fg=GREEN)
    if check % 8 == 0:
        count_check(LONG_BREAK_MIN*60)
        timer_label.config(timer_label,text="LONG BREAK",fg=RED)
    elif check % 2 == 0:
        count_check(SHORT_BREAK_MIN*60)
        timer_label.config(timer_label,text="SHORT BREAK",fg=PINK)
    check+= 1 
 

def count_check(count):
    global check,timer
    mins = math.floor(count/60)
    seconds = int(count % 60)
    if seconds == 0:
        seconds = "00"
    elif seconds>0 and seconds <10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(time_count,text=f"{mins}:{seconds}")
    if count>0:
        timer = window.after(1000,count_check,count-1)
    if count == 0:
        marks= ""
        if check % 2 == 0:
            for i in range(int(check//2)):
                marks += "✓"
            checkmark.config(text=marks)
        on_click()


window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 50))
timer_label.grid(column=1,row=0)


reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=img)
time_count = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start = Button(text="Start",highlightthickness=0,command=on_click)
start.grid(column=0,row=2)

          
checkmark = Label(text="",fg=GREEN,bg=YELLOW,highlightthickness=0)
checkmark.grid(column=1,row=3)

window.mainloop()
