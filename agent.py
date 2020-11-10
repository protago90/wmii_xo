import random
import time


class Agent():
    def __init__(self, sign):
        self.sign = sign
        self.nap = 1
    
    def make_move(self, board):
        pass


class HumanAgnet(Agent):
    def __init__(self, sign):
        super().__init__(sign)

    def make_move(self, board):
        valid = False
        pos = None
        while not valid:
            try:
                pos = int(input(f'# Ruch {self.sign}: '))
                if pos not in board.get_valid_moves():
                    raise ValueError
                valid = True
            except ValueError:
                print('# Popraw ruch.')
        return pos


class RandomAgnet(Agent):
    def __init__(self, sign):
        super().__init__(sign)
    
    def make_move(self, board):
        print(f'# Ruch {self.sign}\'a')
        time.sleep(self.nap)
        return random.choice(board.get_valid_moves())


class MinMaxAgnet(Agent):
    def __init__(self, sign):
        super().__init__(sign)

    def make_move(self, board):
        pass