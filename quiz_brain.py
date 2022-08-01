# Quiz Brain

from tkinter import *

FONT = ("Helvetica", 32, "normal")

class QuizBrain:

    def __init__(self, window, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.window = window
        self.score = 0
        self.curr_answer = StringVar()
        self.create_btns()
        self.create_score_and_questions()

    def create_score_and_questions(self):
        self.score_label = Label(self.window, text=f"{self.score}/20", font=FONT, padx=10, pady=10)
        self.score_label.grid(column=0, row=0)
        self.question_label = Label(self.window, text="ERROR: No question", font=FONT, wraplength=500, width=40, height=15, padx=10, pady=10)
        self.question_label.grid(column=1, row=1)

    def create_btns(self):
        self.true_btn = Button(self.window, text="True", command=lambda: self.curr_answer.set("true"), font=FONT, padx=10, pady=10)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(self.window, text="False", command=lambda: self.curr_answer.set("false"), font = FONT, padx=10, pady=10)
        self.false_btn.grid(column=2, row=2)

    def write_score(self):
        self.score_label.config(text=f"{self.score}/20")
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        curr_q = self.question_list[self.question_number]
        self.question_number+=1
        self.question_label.config(text=f"Q.{self.question_number} {curr_q.text}")
        self.window.wait_variable(self.curr_answer)
        self.check_answer(curr_q.answer)

    def check_answer(self, corr_ans):
        if self.curr_answer.get() == corr_ans.lower():
            self.score += 1
        self.write_score()

    def game_over_screen(self):
        self.score_label.grid_forget()
        self.true_btn.grid_forget()
        self.false_btn.grid_forget()
        self.question_label.config(text=f"Game over! You scored {self.score}/20.")
        self.question_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.quit_btn = Button(self.window, text="Quit", command=lambda: self.window.destroy(), font=FONT, padx=10, pady=10)
        self.quit_btn.place(relx=0.5, rely=0.5, anchor=CENTER)