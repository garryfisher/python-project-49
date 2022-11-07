import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def is_gcd(number1, number2):
    is_gcd = math.gcd(number1, number2)
    return is_gcd


def get_game():
    num_1 = random.randint(1, 101)
    num_2 = random.randint(1, 101)
    correct_answer = is_gcd(num_1, num_2)
    question_generator = f'{str(num_1)} {str(num_2)}'
    return question_generator, str(correct_answer)
