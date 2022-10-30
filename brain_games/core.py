from brain_games.cli import welcome_user, get_user_answer


def game_start(game_name):
    tries = 3
    name = welcome_user(game_name.RULE)
    while tries > 0:
        question, correct_answer = game_name.game()
        user_answer = get_user_answer(question)
        print(user_answer)
        if user_answer == correct_answer:
            print('Correct!')
            tries -= 1
        elif not user_answer == correct_answer:
            print(
        	f"'{user_answer}' is wrong answer ;(.",
        	f"Correct answer was '{correct_answer}'",
            )
            print(f"Let's try again, {name}!")
            break
        else:
            break
        if tries == 0:
            print(f"Congratulations, {name}!")
