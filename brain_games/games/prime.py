import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


def brain_plays():
    question = random.randint(0, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
