#!/usr/bin/env python3
import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def job_calculate(number):
    index = 0
    for i in range(2, number // 2 + 1):
        if (number % i) == 0:
            index += 1
    if index <= 0:
        return 'yes'
    else:
        return 'no'


def game():
    num_1 = random.randint(1, 101)
    correct_answer = job_calculate(num_1)
    return str(num_1), str(correct_answer)
