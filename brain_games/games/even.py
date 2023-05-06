import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 30


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_round():
    question = random.randint(MIN_VALUE, MAX_VALUE)
    correct_answer = is_even(question)

    return question, correct_answer
