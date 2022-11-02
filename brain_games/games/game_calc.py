import random

RULE = "What is the result of the expression?"
SYMBOLS = '+', '-', '*'


def calculation_game():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    random_symbol = random.choice(SYMBOLS)
    question_generator = f'{num_1} {random_symbol} {num_2}'
    if random_symbol == "+":
        correct_answer = num_1 + num_2
    elif random_symbol == "-":
        correct_answer = num_1 - num_2
    elif random_symbol == "*":
        correct_answer = num_1 * num_2
    return question_generator, str(correct_answer)
