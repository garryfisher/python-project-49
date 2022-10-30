import prompt


def welcome_user(rule=""):
    print('Welcome to the Brain Games!')
    print(f'{rule}')
    get_user_name = prompt.string('May I have your name? ')
    print(f'Hello, {get_user_name}!')
    return get_user_name


def get_user_answer(question):
    print(f"Questions: {question}")
    get_user_answer = input('Your answer: ')
    return get_user_answer
