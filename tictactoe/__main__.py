#!/usr/bin/python
from agent import HumanUI, RandomBot, MinMaxBot, CustomBot, DebutsBot
from board import TheBoard
import argparse
from collections import Counter
from tqdm import tqdm #install


class Player():
    human = HumanUI
    minmax = MinMaxBot
    random = RandomBot
    custom = CustomBot
    debuts = DebutsBot

    @classmethod
    def set(cls, player, sign, debug=None, nap=None):
        return getattr(cls, player)(sign=sign, nap=nap, debug=debug)

    @classmethod
    def list(cls):
        return [str(k) for k, v in cls.__dict__.items() 
                if not k.startswith('__') and callable(v)]


def parse_args():
    args = argparse.ArgumentParser()
    bots = Player.list()
    args.add_argument('-x', '--x_player', type=str, default='human',
                      required=False, help='"X" player.', choices=bots)
    args.add_argument('-o', '--o_player', type=str, default='custom',
                      required=False, help='"O" player.', choices=bots)
    args.add_argument('-n', '--n_games', type=int, default=0, 
                      required=False, help='N games in tournament.')
    args.add_argument('-d', '--debug', action='store_true', 
                      required=False, help='Debug search bot rationele.')   
    return args.parse_args()


def run_gameplay(board, x_player, o_player, show):
    map_sign_to_player = {'X': x_player, 'O': o_player}
    sign = 'X'
    sign_next = 'O'
    while board.check_open_moves():
        move = map_sign_to_player.get(sign).make_move(board)
        board.process_move(sign, move)
        if show:
            print(f'# "{sign}" moves:')
            board.print_state()
        if board.winner:
            print(f'# Player "{sign}" wins the game!') if show else None
            break
        sign, sign_next = sign_next, sign
    return board.winner


def main_game(x_player, o_player, show=True):
    board = TheBoard()
    board.print_intro() if show else None
    winner = run_gameplay(board, x_player, o_player, show)
    return winner


def main_tournament(x_player, o_player, n=10, show=False):
    records = []
    for _ in tqdm(range(n), desc="Tournament"):
        records.append(
            main_game(x_player, o_player, show))
    stats = Counter([r for r in records])
    x = stats.get('X', 0)
    o = stats.get('O', 0)
    d = n - x - o
    fmt = '\033[91m' #\033[1m
    msg = '{:>2} results:{} "X" {} bot -- {} : {} : {} -- "O" {} bot'
    print(msg.format('', fmt, x_player.id, x, d, o, o_player.id))


def main():
    args = parse_args()
    x_player = args.x_player
    o_player = args.o_player
    n = abs(args.n_games)
    if n == 0:
        debug = args.debug
        x_player = Player.set(x_player, 'X', debug, nap=1.5)
        o_player = Player.set(o_player, 'O', debug, nap=1.5)
        main_game(x_player, o_player)
    else:
        x_player = Player.set(x_player, 'X')
        o_player = Player.set(o_player, 'O')
        main_tournament(x_player, o_player, n=n)


if __name__ == '__main__':
    main()
