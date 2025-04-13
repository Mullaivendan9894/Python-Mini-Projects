from question_model import Question
from data import questions_data
from quiz_brain import QuizBrain

question_bank = []

for question in questions_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("Great! you have completed the quizz!")
print(f"Your final score: {quiz.score}/{len(question_bank)}")

