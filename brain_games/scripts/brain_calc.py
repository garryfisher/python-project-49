#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random


def random_number():
    random_number = random.randint(1, 51)
    return random_number


def random_symbol():
    symbol = '+', '-', '*'
    random_symbol = random.choice(symbol)
    return random_symbol


def question(n1, n2, s):
    print(f'Question: {str(n1)} {s} {str(n2)}')


def calculate(n1, n2, s):
    if s == "+":
        answer = n1 + n2
    elif s == "-":
        answer = n1 - n2
    elif s == "*":
        answer = n1 * n2
    return answer


def compare_answer_calc():
    if user_answer == str(correct_answer):
        print("Correct!")
    elif not user_answer == str(correct_answer):
        print(f"""'{user_answer}' is wrong answer ;(.
Correct answer was '{correct_answer}'""")


def main():
    return


if __name__ == '__main__':
    main()


print('brain-calc\n\nWelcome to the Brain Games!')
name = welcome_user()
print(f'Hello, {name}')
tries = 3
while tries > 0:
    num_1 = random_number()
    num_2 = random_number()
    symbol = random_symbol()
    correct_answer = calculate(num_1, num_2, symbol)
    question(num_1, num_2, symbol)
    user_answer = input("Your answer: ")
    if user_answer == str(correct_answer):
        print('Correct!')
        tries -= 1
    elif not user_answer == str(correct_answer):
        print(f"'{user_answer}' is wrong answer ;(.Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
        break
if tries == 0:
    print(f'Congratulations, {name}!')     

