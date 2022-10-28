#!/usr/bin/env python3
from brain_games.cli import welcome_user, random_number, game_over_message, question
import random

RULES = 'What number is missing in the progression?'

def random_string(n1, n2 = 101):
    start_step = 2
    end_step = 5
    start_cut = 5
    end_cut = 11
    start = min(n1, n2)
    stop = max(n1, n2)
    step = random.randint(start_step, end_step)
    cut = random.randint(start_cut, end_cut)
    return list(range(start, stop, step)[:cut])
    

def mask_symbol(string):
    symbol = '..'
    length = len(string)
    random_index = random.randint(1, length - 2)
    get_mask_symbol = string.pop(random_index)
    string.insert(random_index, symbol)
    result = ''
    for x in string:
        result += (str(x) + ' ')
    return [result, get_mask_symbol]    

def main():
    print('')
     
       
main()
print('brain-progression\n')
name = welcome_user()
print(RULES)
tries = 3
while tries > 0:
    num_1 = random_number()
    q_str = mask_symbol(random_string(num_1))
    quest, correct_answer = q_str[0], q_str[1]
    question(quest)
    user_answer = input('Your answer: ')
    if user_answer == str(correct_answer):
        print('Correct!')
        tries -= 1
    elif not user_answer == str(correct_answer):
        game_over_message(user_answer, correct_answer, name)
        break
    else:
        break
if tries == 0:
    print(f'Congradulations, {name}')







if __name__ == '__main__':
    main()


