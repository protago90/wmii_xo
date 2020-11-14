from agent import HumanAgent, RandomAgent, MinMaxAgent, CustomAgent
from board import TheBoard
from collections import Counter
from tqdm import tqdm #install


class Agent():
    human = HumanAgent
    minmax = MinMaxAgent
    random = RandomAgent
    #custom = CustomAgent


def run_gameplay(board, x_agent, o_agent, show):
    map_sign_to_agent = {'X': x_agent, 'O': o_agent}
    sign = 'X'
    sign_next = 'O'
    while board.check_open_moves():
        pos = map_sign_to_agent.get(sign).make_move(board)
        board.process_move(sign, pos)
        if show:
            print(f'# Ruch "{sign}"')
            board.print_state()
        if board.winner:
            print(f'# Gracz "{sign}" wygrywa') if show else None
            break
        sign, sign_next = sign_next, sign
    return board.winner


def main(x_agent, o_agent, show=True):
    board = TheBoard()
    board.print_intro() if show else None
    winner = run_gameplay(board, x_agent, o_agent, show)
    return winner


def main_tournament(x_agent, o_agent, n=10, show=False):
    records = []
    for _ in tqdm(range(n), desc="Tournament"):
        records.append(
            main(x_agent, o_agent, show))
    stats = Counter([r for r in records])
    x = stats.get('X', 0)
    o = stats.get('O', 0)
    d = n - x - o
    fmt = '\033[91m' #\033[1m
    msg = '{:>2} results:{} "X" {} agent -- {} : {} : {} -- "O" {} agent'
    print(msg.format('', fmt, x_agent.id, x, d, o, o_agent.id))


if __name__ == '__main__':
    x_agent = Agent.random('X')
    o_agent = Agent.minmax('O')
    main(x_agent, o_agent)
    # main_tournament(x_agent, o_agent, n=1)
