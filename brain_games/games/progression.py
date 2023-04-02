import random

RULE = 'What number is missing in the progression?'


def get_progression():
    first_number = random.randint(0, 10)
    progression = [first_number]

    progression_len = random.randint(5, 10)
    step = random.randint(2, 10)
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
    example = ' '.join(map(str, progression))

    return example, correct_answer
