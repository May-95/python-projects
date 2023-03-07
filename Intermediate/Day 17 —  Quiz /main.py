from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

current_number = 0

quiz = QuizBrain(question_bank)

print("Welcome to the trivia quiz!")

while quiz.still_has_questions():
    quiz.next_question()
    current_number += 1

print("You have completed the quiz.")
print(f"Your final score is {quiz.score} / {quiz.question_number}.")
