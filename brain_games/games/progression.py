import random

RULE = 'What number is missing in the progression?'
MIN_VALUE = 1
MAX_VALUE = 30


def get_progression():
    first_number = random.randint(MIN_VALUE, MAX_VALUE)
    progression = [first_number]

    progression_len = random.randint(MIN_VALUE, MAX_VALUE)
    step = random.randint(MIN_VALUE, MAX_VALUE)
    i = 1

    while i < progression_len:
        next_number = progression[i - 1] + step
        progression.append(next_number)
        i += 1

    return progression


def brain_plays():
    progression = get_progression()

    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)

    answer = progression[random_index]
    correct_answer = str(answer)

    progression[random_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
