class QuizBrain:
    def __init__(self, q_list: []):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return len(self.question_list) - self.question_number >= 1

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(F"Your current score is: {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        q = current_question.text
        self.question_number += 1
        question = f"Q.{self.question_number}: {q} True or False? \n"
        # pri int(question)
        user_answer = input(question)
        return self.check_answer(user_answer, current_question.answer)
