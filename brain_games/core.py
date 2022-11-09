import prompt


MAX_TRIES = 3


def run_game(game_name):
    number_of_tries = MAX_TRIES
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(f'{game_name.RULE}')
    while number_of_tries > 0:
        question, correct_answer = game_name.get_game()
        print(f"Question: {question}")
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            number_of_tries -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
