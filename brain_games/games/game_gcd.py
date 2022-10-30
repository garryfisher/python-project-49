#!/usr/bin/env python3
import random
import math

RULE = 'Find the greatest common divisor of given nubers.'


def game():
    num_1 = random.randint(1, 101)
    num_2 = random.randint(1, 101)
    correct_answer = math.gcd(num_1, num_2)
    question_generator = f'{str(num_1)} {str(num_2)}'
    return question_generator, str(correct_answer)
