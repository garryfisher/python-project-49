#!/usr/bin/env python3
import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    quest_generator = random.randint(1, 100)
    if quest_generator % 2 == 0:
        correct_answer = 'yes'
    elif quest_generator % 2 == 1:
        correct_answer = 'no'
    return quest_generator, correct_answer
