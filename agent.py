import random
import time


class Agent():
    def __init__(self, sign):
        self.sign = sign
        self.nap = .6
    
    def make_move(self, board):
        pass


class HumanAgent(Agent):
    def __init__(self, sign):
        super().__init__(sign)

    def make_move(self, board):
        while True:
            try:
                pos = int(input(f'# Wskaż pozycję 1-9: ')) - 1
                if pos in board.get_valid_moves():
                    return pos
            except ValueError: pass


class RandomAgent(Agent):
    def __init__(self, sign):
        super().__init__(sign)
    
    def make_move(self, board):
        time.sleep(self.nap)
        return random.choice(board.get_valid_moves())


class MinMaxAgent(Agent):
    def __init__(self, sign):
        super().__init__(sign)

    def make_move(self, board):
        pass
