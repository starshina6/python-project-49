import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_plays():
    example = random.randint(1, 100)

    if example % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return example, correct_answer
