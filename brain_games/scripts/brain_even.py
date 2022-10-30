#!/usr/bin/env python3
from brain_games.core import game_start
from brain_games.games import game_even


def main():
    game_start(game_even)   # запуск игры(какой игры)


if __name__ == '__main__':
    main()
