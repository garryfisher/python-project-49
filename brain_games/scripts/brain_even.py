#!/usr/bin/env python3
from brain_games.cli import welcome_user, random_number, game_over_message, question


RULES = "Answer 'yes' if the number is even, otherwise answer 'no'."


def job_calculation(number):
    if number % 2 == 0:
        return 'yes'
    elif number % 2 == 1:
        return 'no'

def main():
    print('')


if __name__ == '__main__':
    main()

main()
print('brain-even\n')
name = welcome_user()
print(RULES)
tries = 3
while tries > 0:
    fix_number = random_number()
    question(fix_number)
    user_answer = input("Your answer: ")
    correct_answer = job_calculation(fix_number)
    if user_answer == 'yes' or user_answer == 'no':
        if user_answer == correct_answer:
            print('Correct!')
            tries -= 1
        elif user_answer != correct_answer:
            game_over_message(user_answer, correct_answer, name)
            break
    else:
        break
if tries == 0:
    print(f'Congratulations, {name}!')

