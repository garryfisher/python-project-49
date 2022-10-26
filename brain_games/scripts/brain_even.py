#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random


def random_number():
    random_number = random.randint(1, 101)
    return random_number


def even_not_even(number):
    if number % 2 == 0:
        return 'yes'
    elif number % 2 == 1:
        return 'no'


def is_answer_wrong(item):
    if item == 'yes':
        print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
        Let's try again, {name}!""")
    elif item == 'no':
        print(f"""'no' is wrong answer ;(. Correct answer was 'yes'.
        Let's try again, {name}!""")


def main():
    return


if __name__ == '__main__':
    main()


print('brain-even\n\nWelcome to the Brain Games')
name = welcome_user()
print(f'Hello, {name}!')
print('Answer "yes" if the number is even, otherwise answer "no".')
tries = 3
while tries > 0:
    fixing_number = random_number()
    print(f'Questions: {fixing_number}')
    user_answer = input("Your answer: ")
    if user_answer == 'yes' or user_answer == 'no':
        if user_answer == even_not_even(fixing_number):
            print('Correct!')
            tries -= 1
    elif user_answer != even_not_even(fixing_number):
        is_answer_wrong(user_answer)
        break
    else:
        break
if tries == 0:
    print(f'Congratulations, {name}!')

