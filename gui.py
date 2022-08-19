# GUI

from tkinter import *

FONT = ("Helvetica", 32, "normal")

class QuizInter:

    def __init__(self, quiz_brain):
        self.window = Tk()
        self.window.title("Trivia Quiz Game by blurridge")
        self.window.geometry("1000x700")
        self.window.resizable(False, False)
        self.quiz = quiz_brain
        self.create_score_and_questions()
        self.create_btns()
        self.write_score()
        self.get_question()
        self.window.mainloop()

    def create_score_and_questions(self):
        self.score_label = Label(self.window, text=f"{self.quiz.score}/20", font=FONT, padx=10, pady=10)
        self.score_label.grid(column=0, row=0)
        self.question_label = Label(self.window, text="ERROR: No question", font=FONT, wraplength=500, width=40, height=15, padx=10, pady=10)
        self.question_label.grid(column=1, row=1)

    def create_btns(self):
        self.true_btn = Button(self.window, text="True", command=self.true_pressed, font=FONT, padx=10, pady=10)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(self.window, text="False", command=self.false_pressed, font = FONT, padx=10, pady=10)
        self.false_btn.grid(column=2, row=2)

    def write_score(self):
        self.score_label.config(text=f"{self.quiz.score}/20")

    def game_over_screen(self):
        self.score_label.grid_forget()
        self.true_btn.grid_forget()
        self.false_btn.grid_forget()
        self.question_label.config(text=f"Game over! You scored {self.quiz.score}/20.")
        self.question_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.quit_btn = Button(self.window, text="Quit", command=lambda: self.window.destroy(), font=FONT, padx=10, pady=10)
        self.quit_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    def get_question(self):
        if self.quiz.still_has_questions():
            curr_q = self.quiz.next_question()
            self.question_label.config(text=curr_q)
        else:
            self.game_over_screen()
    
    def true_pressed(self):
        self.quiz.check_answer("true")
        self.write_score()
        self.get_question()
    
    def false_pressed(self):
        self.quiz.check_answer("false")
        self.write_score()
        self.get_question()