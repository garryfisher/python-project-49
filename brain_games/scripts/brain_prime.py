#!/usr/bin/env python3
from brain_games.cli import welcome_user, random_number, game_over_message, question
import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    print('')


def job_calculate(n1):
    k = 0
    for i in range(2, n1 // 2 + 1):
        if (n1 % i) == 0:
            k += 1
    if k <= 0:
        return 'yes'
    else:
        return 'no'


main()
print('brain-pime\n')
name = welcome_user()
print(RULES)
tries = 3
while tries > 0:
    num_1 = random_number()
    question(num_1)
    user_answer = input('Your answer: ')
    correct_answer = job_calculate(num_1)
    if user_answer == correct_answer:
        print('Correct!')
        tries -= 1
    else:
        game_over_message(user_answer, correct_answer, name)
        break

if tries == 0:
    print(f'Congratulation, {name}!')


if __name__ == '__main__':
    main()


