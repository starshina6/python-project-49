import random

RULE = 'What is the result of the expression?'


def brain_plays():
    number_one = random.randint(1, 30)
    number_two = random.randint(1, 30)
    char = random.choice('+-*')
    example = f'{number_one} {char} {number_two}'
    correct_answer = str(eval(example))

    return example, correct_answer
