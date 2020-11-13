import math


class TheBoard():
    def __init__(self):
        self.board = [0 for _ in range(9)]
        self.map_val_to_sign = {1: 'X', -1: 'O', 0: ' '}
        self.map_sign_to_val = {v: k for k, v in self.map_val_to_sign.items()}
        self.winner = None
        self.moves_registry = []
        self.msg = "{:>10} | {} | {}"

    @staticmethod
    def _split_vector(vec, desc=False):
        vecs = [vec[i*3 : i*3+3] for i in range(3)]
        return vecs[::-1] if desc else vecs

    def print_intro(self):
        print('# Witaj w Kółko vs Krzyżyk!')
        for a, b, c in self._split_vector(range(1, 10), desc=True):
            print(self.msg.format(a, b, c))

    def print_state(self):
        for row in self._split_vector(self.board, desc=True):
            a, b, c = [self.map_val_to_sign.get(v) for v in row]
            print(self.msg.format(a, b, c))

    @staticmethod
    def _check_win_line(vec):
        return abs(sum(vec)) == 3

    def _check_end_state(self, pos):
        i_row = math.floor(pos/3)
        the_row = self._split_vector(self.board)[i_row]
        if self._check_win_line(the_row):
            return True
        i_col = pos % 3
        the_col = [self.board[i_col+i] for i in range(0, 9, 3)]
        if self._check_win_line(the_col):
            return True
        diag_1 = [0, 4, 8]
        if pos in diag_1:
            if self._check_win_line(self.board[i] for i in diag_1):
                return True
        diag_2 = [2, 4, 6]
        if pos in diag_2:
            if self._check_win_line(self.board[i] for i in diag_2):
                return True
        return False

    def process_move(self, sign, pos):
        self.board[pos] = self.map_sign_to_val.get(sign)
        self.moves_registry.append(pos)
        if self._check_end_state(pos):
            self.winner = sign
    
    def undo_move(self):
        pos = self.moves_registry.pop()
        self.board[pos] = 0 
        self.winner = None

    def get_valid_moves(self):
        return [i for i, v in enumerate(self.board) if v == 0]
    
    def check_open_moves(self):
        return len(self.get_valid_moves()) >= 1
