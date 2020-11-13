from agent import HumanAgent, RandomAgent, MinMaxAgent, CustomAgent
from board import TheBoard
from tqdm import tqdm
from collections import Counter


class Agent():
    human = HumanAgent
    minmax = MinMaxAgent
    random = RandomAgent
    #custom = CustomAgent


def the_gameplay(board, x_agent, o_agent, show):
    map_sign_to_agent = {'X': x_agent, 'O': o_agent}
    sign = 'X'
    sign_next = 'O'
    while board.check_open_moves():
        agent = map_sign_to_agent.get(sign)
        pos = agent.make_move(board)
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
    winner = the_gameplay(board, x_agent, o_agent, show)
    return x_agent.id, o_agent.id, winner


def main_tournament(x_agent, o_agent, n=10, show=False):
    record = []
    for _ in tqdm(range(n), desc="Tournament"):
        record.append(
            main(x_agent, o_agent, show))
    stats = Counter([trio[2] for trio in record])
    x = stats.get('X', 0)
    o = stats.get('O', 0)
    d = n - x - o
    x_id = record[0][0]
    o_id = record[0][1]
    fmt = '\033[91m \033[1m'
    msg = '{:>2} results:{} "X" {} agent -- {} : {} : {} -- "O" {} agent'
    print(msg.format('', fmt, x_id, x, d, o, o_id))


if __name__ == '__main__':
    x_agent = Agent.minmax('X')
    o_agent = Agent.minmax('O')
    # main(x_agent, o_agent)
    main_tournament(x_agent, o_agent, n=20)
