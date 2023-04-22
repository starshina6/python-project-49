import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def brain_plays():
    number_one = random.randint(1, 1000)
    number_two = random.randint(1, 1000)
    question = f'{number_one} {number_two}'
    correct_answer = str(math.gcd(number_one, number_two))

    return question, correct_answer
