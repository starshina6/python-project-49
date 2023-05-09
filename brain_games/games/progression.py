import random

RULE = 'What number is missing in the progression?'
START_MIN_VALUE = 0
START_MAX_VALUE = 10
LEN_MIN_VALUE = 5
LEN_MAX_VALUE = 10
STEP_MIN_VALUE = 2
STEP_MAX_VALUE = 10


def get_progression():
    first_number = random.randint(START_MIN_VALUE, START_MAX_VALUE)
    progression = [first_number]

    progression_len = random.randint(LEN_MIN_VALUE, LEN_MAX_VALUE)
    step = random.randint(STEP_MIN_VALUE, STEP_MAX_VALUE)

    i = 1

    while i < progression_len:
        next_number = progression[i - 1] + step
        progression.append(next_number)
        i += 1

    return progression


def get_round():
    progression = get_progression()

    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)

    answer = progression[random_index]
    correct_answer = str(answer)

    progression[random_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
