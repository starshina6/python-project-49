#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()
