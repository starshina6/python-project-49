import random

RULE = 'What number is missing in the progression?'
START_MIN_VALUE = 0
START_MAX_VALUE = 10
LEN_MIN_VALUE = 5
LEN_MAX_VALUE = 10
STEP_MIN_VALUE = 2
STEP_MAX_VALUE = 10


def get_progression(initial_term, common_difference, length):
    progression = []
    for n in range(1, length + 1):
        next_number = initial_term + (n - 1) * common_difference
        progression.append(next_number)
    return progression


def get_round():
    initial_term = random.randint(START_MIN_VALUE, START_MAX_VALUE)
    common_difference = random.randint(STEP_MIN_VALUE, STEP_MAX_VALUE)
    length = random.randint(LEN_MIN_VALUE, LEN_MAX_VALUE)

    progression = get_progression(initial_term, common_difference, length)

    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)

    answer = progression[random_index]
    correct_answer = str(answer)

    progression[random_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
