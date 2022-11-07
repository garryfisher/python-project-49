import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        return 'yes'
    return 'no'


def get_game():
    number = random.randint(1, 101)
    question_generator = str(number)
    correct_answer = is_prime(number)
    return question_generator, correct_answer
