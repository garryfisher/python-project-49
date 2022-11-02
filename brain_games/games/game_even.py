import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculation_game():
    question_generator = random.randint(1, 100)
    if question_generator % 2 == 0:
        correct_answer = 'yes'
    elif question_generator % 2 == 1:
        correct_answer = 'no'
    return question_generator, correct_answer
