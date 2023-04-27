import random
import math

RULE = 'Find the greatest common divisor of given numbers.'
MIN_VALUE = 1
MAX_VALUE = 30

def brain_plays():
    number_one = random.randint(MIN_VALUE, MAX_VALUE)
    number_two = random.randint(MIN_VALUE, MAX_VALUE)
    question = f'{number_one} {number_two}'
    correct_answer = str(math.gcd(number_one, number_two))

    return question, correct_answer
