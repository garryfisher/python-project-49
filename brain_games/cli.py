import prompt


def welcome_user():
    get_user_name = prompt.string('May I have your name? ')
    return get_user_name
