#!/usr/bin/env python3
import random

RULE = 'What number is missing in the progression?'


def random_string(n1, n2=101):
    start_step = 2
    end_step = 5
    start_cut = 5
    end_cut = 11
    start = min(n1, n2)
    stop = max(n1, n2)
    step = random.randint(start_step, end_step)
    cut = random.randint(start_cut, end_cut)
    return list(range(start, stop, step)[:cut])


def mask_symbol(string):
    symbol = '..'
    length = len(string)
    random_index = random.randint(1, length - 2)
    get_mask_symbol = string.pop(random_index)
    string.insert(random_index, symbol)
    result = ''
    for x in string:
        result += (str(x) + ' ')
    return [result, get_mask_symbol]


def game():
    num_1 = random.randint(1, 50)
    string_generation = mask_symbol(random_string(num_1))
    question_generation = string_generation[0]
    correct_answer = string_generation[1]
    return question_generation, str(correct_answer)
