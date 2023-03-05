from question import Question
class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}:{current_question.q_text} (True/False)?")
        self.check_answer(user_ans,current_question.q_answer)
    def still_has_questions(self):
        if self.question_number!=len(self.question_list):
            return True
        return False
    def check_answer(self,user_ans,correct_ans):
        self.user_ans=user_ans
        self.correct_ans=correct_ans
        if self.user_ans==self.correct_ans:
            print("you got it right")
            self.score+=1
        else:
            print("wrong")
        print(f"Your current score is {self.score}/{self.question_number}")