import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculation_game():
    num_1 = random.randint(1, 101)
    question_generator = str(num_1)
    index = 0
    for i in range(2, num_1 // 2 + 1):
        if (num_1 % i) == 0:
            index += 1
    	    correct_answer = 'yes' if index <= 0 else 'no'
    return question_generator, correct_answer
