import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 30


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_round():
    question = random.randint(MIN_VALUE, MAX_VALUE)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
