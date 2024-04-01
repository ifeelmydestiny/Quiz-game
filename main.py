import quiz_brain
from data import question_data
from question_model import  Question
from quiz_brain import QuizBrain
# from quiz_brain import still_alive

# is_off = False
# i = 0
# while is_off:
#     question = (question_data[i])["text"]
#     answer = (question_data[i])["answer"].lower()
#     print(f"Question: {question}")
#     user_ans = input("what is your answer: ").lower()
#     if user_ans == answer:
#         i += 1
#         is_off = True
#     else:
#         print(f"You loose the right answer is {answer}.")
#         is_off = False
Question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text,question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)
# quiz.next_question()

while quiz.still_alive():
    # quiz.next_question()
    if quiz.check_brain():
        still_alive =  True
    else:
        still_alive = False