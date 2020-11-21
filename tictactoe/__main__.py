from agent import HumanUI, RandomBot, MinMaxBot, CustomBot, DebutsBot
from board import TheBoard
from collections import Counter
from tqdm import tqdm #install


class Player():
    human = HumanUI
    minmax = MinMaxBot
    random = RandomBot
    custom = CustomBot
    debuts = DebutsBot

    @classmethod
    def set(cls, player, sign):
        return getattr(cls, player)(sign=sign)


def run_gameplay(board, x_player, o_player, show):
    map_sign_to_player = {'X': x_player, 'O': o_player}
    sign = 'X'
    sign_next = 'O'
    while board.check_open_moves():
        move = map_sign_to_player.get(sign).make_move(board)
        board.process_move(sign, move)
        if show:
            print(f'# Ruch "{sign}"')
            board.print_state()
        if board.winner:
            print(f'# Gracz "{sign}" wygrywa') if show else None
            break
        sign, sign_next = sign_next, sign
    return board.winner


def main(x_player, o_player, nap=1, show=True):
    board = TheBoard()
    board.print_intro() if show else None
    x_player.nap = nap
    o_player.nap = nap
    winner = run_gameplay(board, x_player, o_player, show)
    return winner


def main_tournament(x_player, o_player, n=10, nap=0, show=False):
    records = []
    for _ in tqdm(range(n), desc="Tournament"):
        records.append(
            main(x_player, o_player, nap, show))
    stats = Counter([r for r in records])
    x = stats.get('X', 0)
    o = stats.get('O', 0)
    d = n - x - o
    fmt = '\033[91m' #\033[1m
    msg = '{:>2} results:{} "X" {} bot -- {} : {} : {} -- "O" {} bot'
    print(msg.format('', fmt, x_player.id, x, d, o, o_player.id))


if __name__ == '__main__':
    x_player = Player.set('minmax', 'X')
    o_player = Player.set('custom', 'O')
    main(x_player, o_player)
    # main_tournament(x_player, o_player, n=10)
