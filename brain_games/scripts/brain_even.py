from brain_games.cli import welcome_user
from random import randint
import prompt

welcome_user()


"""
1. Сделать выдачу рандомного числа.
2. Написал цикл предлагающий вопрос с рандомным числом 3 раза.
3. Если ответ 3 раза, то завершить с поздравлением.
4. Если нет ответа, то завершить с ошибкой.
"""


from random import randint
import prompt

def random_number_for_questions():
    question_number = randint(1, 100)
    return question_number

  
fix_random_number = random_number_for_questions()



def user_answer():
    answer = prompt.string('Your answer: ')
    if fix_random_number % 2 == 0 and answer == 'yes':
      return 'Correct!'
    elif fix_random_number % 2 == 1 and answer == 'no':
      return 'Correct!'
    else:
      return


print('Answer "yes" if the number is even, otherwise answer "no".')
print(f'Question: {fix_random_number}')
user_answer()
