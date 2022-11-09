import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    get_gcd = math.gcd(number1, number2)
    return get_gcd


def get_game():
    number1 = random.randint(1, 101)
    number2 = random.randint(1, 101)
    correct_answer = get_gcd(number1, number2)
    question_generator = f'{str(number1)} {str(number2)}'
    return question_generator, str(correct_answer)
