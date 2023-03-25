import prompt
import random


def chek_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    n = 3
    while counter < n:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('You answer: ')
        if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
            print('Correct!')
            counter += 1
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.")
            break

