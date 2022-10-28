#!/usr/bin/env python3
from brain_games.cli import welcome_user, random_number, game_over_message
import random
import math


RULES = 'Find the greatest common divisor of given nubers.'


def question(n1, n2):
    print(f'Question: {str(n1)} {str(n2)}')


def gcd(n1, n2):
    result = math.gcd(n1, n2)
    return result


def main():
    print('')


if __name__ == '__main__':
    main()


main()
print('brain-gcd')
name = welcome_user()
print(RULES)
tries = 3
while tries > 0:
    num_1 = random_number()
    num_2 = random_number()
    correct_answer = gcd(num_1, num_2)
    question(num_1, num_2)
    user_answer = input("Your answer: ")
    if user_answer == str(correct_answer):
        print('Correct!')
        tries -= 1
    elif not user_answer == str(correct_answer):
        game_over_message(user_answer, correct_answer, name)
        break
if tries == 0:
    print(f'Congratulations, {name}!')     

