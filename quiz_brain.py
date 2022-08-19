# Quiz Brain

class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0  
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        self.curr_q = self.question_list[self.question_number]
        self.question_number+=1
        return f"Q.{self.question_number} {self.curr_q.text}"

    def check_answer(self, user_ans):
        if self.curr_q.answer.lower() == user_ans.lower():
            self.score += 1