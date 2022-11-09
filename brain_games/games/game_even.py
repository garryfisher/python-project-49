import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game():
    question_generator = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question_generator) else 'no'
    return question_generator, correct_answer
