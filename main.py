# Main

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from gui import QuizInter
from tkinter import *

question_bank = list()

for questions in question_data:
    new_q = Question(questions["text"], questions["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz_gui = QuizInter(quiz)
