import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def get_game():
    question_generator = random.randint(1, 100)
    correct_answer = is_even(question_generator)
    return question_generator, correct_answer
