import random

RULE = "What is the result of the expression?"
SYMBOLS = '+', '-', '*'


def calculate(number1, number2, symbol):
    if symbol == "+":
        get_calculate = number1 + number2
    elif symbol == "-":
        get_calculate = number1 - number2
    elif symbol == "*":
        get_calculate = number1 * number2
    return get_calculate


def get_game():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    random_symbol = random.choice(SYMBOLS)
    correct_answer = calculate(num_1, num_2, random_symbol)
    question_generator = f'{num_1} {random_symbol} {num_2}'
    return question_generator, str(correct_answer)
