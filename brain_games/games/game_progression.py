import random

RULE = 'What number is missing in the progression?'
START_STEP, END_STEP = 2, 5
START_CUT, END_CUT = 5, 11
SYMBOL = '..'


def generate_string(number_1, number_2=101):
    """Функция формирует строку нужной длины"""
    step = random.randint(START_STEP, END_STEP)
    cut = random.randint(START_CUT, END_CUT)
    start = min(number_1, number_2)
    stop = max(number_1, number_2)
    return list(range(start, stop, step)[:cut])


def mask_symbol(string):
    """Функция маскирует случайный символ в полученной
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


def is_progression(number1):
    string_generation = generate_string(number1)
    string_masking = mask_symbol(string_generation)
    return string_masking[0], string_masking[1]


def get_game():
    num_1 = random.randint(1, 50)
    question_generation, correct_answer = is_progression(num_1)
    return question_generation, str(correct_answer)
