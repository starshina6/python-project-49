import random
import math

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True

def brain_plays():
    example = random.randint(0, 100)
    if is_prime(example):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return example, correct_answer
