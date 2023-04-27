import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 30

def brain_plays():
    question = random.randint(MIN_VALUE, MAX_VALUE)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
