import random

RULE = 'What number is missing in the progression?'


def generate_progression():
    step = random.randint(2, 10)
    start = random.randint(1, 100)
    stop = start + (step * 10)
    progression = []
    for x in range(start, stop, step):
        progression.append(str(x))
    return progression


def get_game():
    progression = generate_progression()
    random_index = random.randint(0, 9)
    correct_answer = progression[random_index]
    progression[random_index] = ".."
    question_generation = ' '.join(progression)
    return question_generation, correct_answer
