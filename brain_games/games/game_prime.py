import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number


def get_game():
    number = random.randint(1, 100)
    question_generator = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question_generator, correct_answer
