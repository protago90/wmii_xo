from agent import HumanAgent, RandomAgent, MinMaxAgent
from board import TheBoard


def gameplay(board, x_agent, o_agent):
    board.print_intro()
    map_sign_to_agent = {'X': x_agent, 'O': o_agent}
    sign = 'X'
    sign_next = 'O'
    while board.check_open_moves():
        print(f'# Ruch "{sign}"')
        pos = map_sign_to_agent.get(sign).make_move(board)
        board.process_move(sign, pos)
        board.print_state()
        if board.winner:
            print(f'# Gracz "{sign}" wygrywa')
            break
        sign, sign_next = sign_next, sign


if __name__ == '__main__':
    board = TheBoard()
    x_agent = MinMaxAgent('X') #HumanAgent('X')
    o_agent = MinMaxAgent('O')
    gameplay(board, x_agent, o_agent)
    