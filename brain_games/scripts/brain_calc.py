#!/usr/bin/env python3
from brain_games.cli import welcome_user, random_number, game_over_message
import random


RULES = 'What is the resut of the expression?'


def random_symbol():
    symbol = '+', '-', '*'
    random_symbol = random.choice(symbol)
    return random_symbol


def question(n1, n2, s):
    print(f'Question: {str(n1)} {s} {str(n2)}')


def job_calculate(n1, n2, s):
    if s == "+":
        answer = n1 + n2
    elif s == "-":
        answer = n1 - n2
    elif s == "*":
        answer = n1 * n2
    return answer


def main():
    print('')
    

if __name__ == '__main__':
    main()


main()
print('brain-calc')
name = welcome_user()
print(RULES)
tries = 3
while tries > 0:
    num_1 = random_number()
    num_2 = random_number()
    symbol = random_symbol()
    correct_answer = job_calculate(num_1, num_2, symbol)
    question(num_1, num_2, symbol)
    user_answer = input("Your answer: ")
    if user_answer == str(correct_answer):
        print('Correct!')
        tries -= 1
    elif not user_answer == str(correct_answer):
        game_over_message(user_answer, correct_answer, name)
        break
if tries == 0:
    print(f'Congratulations, {name}!')     

