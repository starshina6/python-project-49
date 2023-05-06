import prompt

ROUNDS_COUNT = 3


def play_game(game):
    index = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULE)

    while index < ROUNDS_COUNT:
        question, correct_answer = game.get_round()

        print(f'Question: {question}')
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
