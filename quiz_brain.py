
class QuizBrain:
    def __init__(self, list):
        self.question_num = 0
        self.question_list = list
    def still_alive(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        self.quiz_ans = input(f"Q.{self.question_num}:  {current_question.text} (True/Fasle): ").lower()

    def check_brain(self):
        return self.next_question() == self.quiz_ans()

