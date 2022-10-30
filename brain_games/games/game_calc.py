#!/usr/bin/env python3
import random

RULE = "What is the result of the expression?"


def game():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    symbols = '+', '-', '*'
    r_symbol = random.choice(symbols)
    quest_generator = f'{num_1} {r_symbol} {num_2}'
    if r_symbol == "+":
        correct_answer = num_1 + num_2
    elif r_symbol == "-":
        correct_answer = num_1 - num_2
    elif r_symbol == "*":
        correct_answer = num_1 * num_2
    return quest_generator, str(correct_answer)
