import prompt


MAX_TRIES_IN_GAME = 3


def welcome_user(rule=""):
    print('Welcome to the Brain Games!')
    get_user_name = prompt.string('May I have your name? ')
    print(f'Hello, {get_user_name}!')
    print(f'{rule}')
    return get_user_name


def get_user_answer(question):
    print(f"Question: {question}")
    get_user_answer = input('Your answer: ')
    return get_user_answer


def run_game(game_name):
    number_of_tries = MAX_TRIES_IN_GAME
    name = welcome_user(game_name.RULE)
    while number_of_tries > 0:
        question, correct_answer = game_name.get_game()
        user_answer = get_user_answer(question)
        if user_answer == correct_answer:
            print('Correct!')
            number_of_tries -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
        print(f"Congratulations, {name}!")
