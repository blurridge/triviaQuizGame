# Main

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from tkinter import *

window = Tk()
window.title("Trivia Quiz Game by blurridge")
window.geometry("1000x700")
window.resizable(False, False)
question_bank = list()

for questions in question_data:
    new_q = Question(questions["text"], questions["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(window, question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.game_over_screen()

window.mainloop()