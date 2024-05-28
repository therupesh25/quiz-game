from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_l=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    first = Question(question_text,question_answer)
    question_l.append(first)
quiz = QuizBrain(question_l)
while quiz.still_have():
    quiz.next_question()
print(f"you've scored {quiz.score}/{len(quiz.q_lis)}")
print("you've completed the game".center(20,"-"))





