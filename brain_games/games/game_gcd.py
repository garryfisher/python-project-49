import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    get_gcd = math.gcd(number1, number2)
    return get_gcd


def get_game():
    num_1 = random.randint(1, 101)
    num_2 = random.randint(1, 101)
    correct_answer = get_gcd(num_1, num_2)
    question_generator = f'{str(num_1)} {str(num_2)}'
    return question_generator, str(correct_answer)
