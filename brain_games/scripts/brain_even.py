#!/usr/bin/env python3
from brain_games.engine import start_games
from brain_games.games.even import chek_even


def main():
    start_games(chek_even)


if __name__ == '__main__':
    main()
