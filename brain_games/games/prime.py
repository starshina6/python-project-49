import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 30


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


def brain_plays():
    question = random.randint(MIN_VALUE, MAX_VALUE)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
