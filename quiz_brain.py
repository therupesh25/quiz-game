class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.q_lis = q_list

    def still_have(self):
        return self.question_number < len(self.q_lis)

    def next_question(self):
        current_q = self.q_lis[self.question_number]
        self.question_number += 1
        user = input(f"q.{self.question_number} {current_q.text} (True/False)??")
        self.check_answer(user,current_q.answer)

    def check_answer(self,user,correct_answer):
        if user.lower() == correct_answer.lower():
            self.score+=1
            print("you're right..")
        else:
            print("you're wrong..")
        print(f"{round(self.score)}/{self.question_number}")


