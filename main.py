
from agent import HumanAgnet, RandomAgnet
from board import TheBoard
import time


def gameplay(board, x_agent, o_agent):
    player = 'X'
    board.print_intro()
    while board.check_gameplay():
        if player == 'X':
            pos = x_agent.make_move(board)
        else:
            pos = o_agent.make_move(board)
        if board.process_move(player, pos):
            board.print_state()
        if board.winner:
            print(f'# Gracz "{player}" wygrywa')
            return player
        player = 'O' if player == 'X' else 'X'


if __name__ == '__main__':
    board = TheBoard()
    x_agent = HumanAgnet('X')
    o_agent = RandomAgnet('O')
    gameplay(board, x_agent, o_agent)