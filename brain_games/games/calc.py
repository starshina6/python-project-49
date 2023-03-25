import prompt
import random
from brain_games.engine import start_games, __name__


def random_calc(n):
    start_games()
    print('What is the result of the expression?')
    counter = 0
    n = 3
    while counter < n:
        number_one = random.randint(1, 30)
        number_two = random.randint(1, 30)
        char = random.choice('+-*')
        example = f'{number_one} {char} {number_two}'
        print(f'Question: {example}')
        answer = prompt.string('You answer: ')
        correct_answer = eval(example)
        if int(answer) == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
