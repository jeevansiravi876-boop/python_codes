from question_model import Question
from data import question_data
from quiz_brain import QuizeBrain
question_bank =[]
for question in question_data:
    question_text = question["text"]
    question_answer =question["answer"]
    next_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(next_question)

quiz = QuizeBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
