import prompt
from brain_games.games.even import chek_even


def start_games():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    chek_even()
    print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
    