import prompt

SCORE_MAX = 3


def start_games(game):
    index = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULE)

    while index < SCORE_MAX:
        example, correct_answer = game.brain_plays()

        print(f'Question: {example}')
        player_answer = prompt.string('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correst answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')
