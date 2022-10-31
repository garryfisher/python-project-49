#!/usr/bin/env python3
import random

RULE = 'What number is missing in the progression?'
START_STEP, END_STEP = 2, 5
START_CUT, END_CUT = 5, 11
SYMBOL = '..'


def random_string(n1, n2=101):
    """Функция формирует строку нужной длины"""
    step = random.randint(START_STEP, END_STEP)
    cut = random.randint(START_CUT, END_CUT)
    start = min(n1, n2)
    stop = max(n1, n2)
    return list(range(start, stop, step)[:cut])


def mask_symbol(string):
    """    Функция маскирует случайный символ в полученной
    строке и возвращается строку с маскированным символом
    """
    length = len(string)
    random_index = random.randint(1, length - 2)
    get_mask_symbol = string.pop(random_index)
    string.insert(random_index, SYMBOL)
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
