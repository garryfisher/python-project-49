#!/usr/bin/env python3
from brain_games.core import game_start
from brain_games.games import game_progression


def main():
    game_start(game_progression)   # запуск_игры(какой_игры)


if __name__ == '__main__':
    main()
