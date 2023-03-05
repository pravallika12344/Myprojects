from question import Question
from quizbrain import QuizBrain
from question_list import questions_list
question_bank=[]
for question in questions_list:
    question_text=question["text"]
    question_answer=question["answer"]
    question_bank.append(Question(question_text,question_answer))
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You have completed the quiz with the score {quiz.score}/{quiz.question_number}")