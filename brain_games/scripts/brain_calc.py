#!/usr/bin/env python3
from brain_games.engine import start_games
from brain_games.games.calc import random_calc


def main():
    start_games(random_calc)


if __name__ == '__main__':
    main()
