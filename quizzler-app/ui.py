from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Interface:
    def __init__(self,quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        
        self.text_label = Label(text=f"Score: {self.quiz.score}")
        self.text_label.grid(column=1,row=0)
        self.text_label.config(bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300,height=250)
        self.canvas.config(bg="white",highlightthickness=0)
        self.question = self.canvas.create_text(150,125,width=280,text=f"write",font=("Arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        img = PhotoImage(file="./images/true.png")
        self.correct = Button(image=img,highlightthickness=0,command=self.true_ans)
        self.correct.grid(column=0,row=2)


        img1 = PhotoImage(file="./images/false.png")
        self.incorrect = Button(image=img1,command=self.false_ans)
        self.incorrect.grid(column=1,row=2)
        self.incorrect.config(highlightthickness=0)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.text_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.itemconfig(self.question,text=q_text)
    def true_ans(self):
        is_ans = self.quiz.check_answer("True")
        self.feedback(is_ans)
    def false_ans(self):
        is_ans = self.quiz.check_answer("False")
        self.feedback(is_ans)
    def feedback(self,ans):
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.bg_color)
    def bg_color(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions(): 
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.question,text="You have reached the end of the quiz.")
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")
