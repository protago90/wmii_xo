import random
import time


class Agent():
    def __init__(self, sign):
        self.sign = sign
    
    def make_move(self, board):
        pass


class HumanUI(Agent):
    def __init__(self, sign):
        super().__init__(sign)
        self.id = 'Human'

    def make_move(self, board):
        while True:
            try:
                pos = int(input(f'# Wskaż pozycję 1-9: ')) - 1
                if pos in board.get_valid_moves():
                    return pos
            except ValueError: pass


class RandomBot(Agent):
    def __init__(self, sign, nap=0):
        super().__init__(sign)
        self.id = 'Random'
        self.nap = nap
    
    def make_move(self, board):
        time.sleep(self.nap)
        return random.choice(board.get_valid_moves())


class MinMaxBot(Agent):
    def __init__(self, sign, nap=0):
        super().__init__(sign)
        self.id = 'Minmax'
        self.nap = nap

    def make_move(self, board):
        time.sleep(self.nap)
        if len(board.get_valid_moves()) == 9:
            pos = random.choice(board.get_valid_moves())
        else:
            pos = self.apply_minmax(board)
        return pos
    
    def apply_minmax(self, board):
        record = []
        for pos in board.get_valid_moves():
            board.process_move(self.sign, pos)
            score = self.calc_minimax(False, self.sign, board) #oponent
            board.undo_move()
            record.append((pos, score))
        the_pos = sorted(
            record, key=lambda xy: (xy[1], random.random()), reverse=True
        )[0][0]
        return the_pos

    def calc_minimax(self, maximizer, sign, board):
        if board.winner:
            return 1 if self.sign == sign else -1
        if not board.check_open_moves():
            return 0
        sign = 'X' if sign == 'O' else 'O'
        scores = []
        for pos in board.get_valid_moves():
            board.process_move(sign, pos)
            scores.append(self.calc_minimax(not maximizer, sign, board))
            board.undo_move()
        return max(scores) if maximizer else min(scores)


class CustomBot(Agent):
    def __init__(self, sign, nap=0):
        super().__init__(sign)
        self.id = 'Custom'
        self.nap = nap

    def make_move(self, board):
        time.sleep(self.nap)
        sign = 'X' if self.sign == 'O' else 'O'
        pos = self.apply_rule(board, sign)
        return pos

    def apply_rule(self, board, sign):
        moves = board.get_valid_moves()
        if len(moves) == 9:
            return 8 #random.choice([0, 2, 6, 8])
        if len(moves) == 8:
            return 4 if 4 in moves else random.choice([2, 6])
        for pos in moves:
            board.process_move(self.sign, pos)
            if board.winner:
                board.undo_move()
                return pos
            board.undo_move()
            board.process_move(sign, pos) #oponent
            if board.winner:
                board.undo_move()
                return pos
            board.undo_move()
        return random.choice(moves)
