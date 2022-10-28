import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    get_user_name = prompt.string('May I have your name? ')
    print(f'Hello, {get_user_name}!')
    return get_user_name


def random_number():
    result = random.randint(1, 101)
    return result


def game_over_message(u_answer, c_answer, name):
    print(f"'{u_answer}' is wrong answer;(. Correct answer was '{c_answer}'.")
    print(f"Let's try again, {name}!")


def question(quest):
    print(f"Qestion: {quest}")
