import random

RULE = 'What is the result of the expression?'
MIN_VALUE = 1
MAX_VALUE = 30

def brain_plays():
    number_one = random.randint(MIN_VALUE, MAX_VALUE)
    number_two = random.randint(MIN_VALUE, MAX_VALUE)
    char = random.choice('+-*')
    question = f'{number_one} {char} {number_two}'
    correct_answer = str(eval(question))

    return question, correct_answer
