import prompt


def welcome_user(rule=""):
    print('Welcome to the Brain Games!')
    get_user_name = prompt.string('May I have your name? ')
    print(f'Hello, {get_user_name}!')
    print(f'{rule}')
    return get_user_name
