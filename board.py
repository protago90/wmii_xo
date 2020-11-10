class TheBoard():
    def __init__(self):
        self.board = [0 for _ in range(9)]
        self.map = {1: 'X', -1: 'O', 0: ' '}
        self.map_inv = {v: k for k, v in self.map.items()}
        self.winner = None
        self.msg = '{:>10} | {} | {}'

    def print_intro(self):
        print('Witaj w Kółko vs Krzyżyk!')
        for a, b, c in [range(9)[i*3-3 : i*3] for i in range(3, 0, -1)]:
            print(self.msg.format(a, b, c))

    def print_state(self):
        for row in [self.board[i*3-3 : i*3] for i in range(3, 0, -1)]:
            a, b, c = [self.map.get(x) for x in row]
            print(self.msg.format(a, b, c))

    def process_move(self, sign, pos):
        val = self.map_inv.get(sign)
        if self.board[pos] == 0:
            self.board[pos] = val
            if self.check_end_state():
                self.winner = sign
            return True
        return False

    def check_end_state(self):  
        #todo: optimize to only affected cross sections
        for row in (self.board[i*3 : i*3 + 3] for i in range(3)):
            if abs(sum(row)) == 3:
                return True
        for col in ([self.board[i+j] for j in [0, 3, 6]] for i in range(3)):
            if abs(sum(col)) == 3:
                return True
        for diag in ([self.board[i] for i in [0, 4, 8]], 
                     [self.board[i] for i in [2, 4, 6]]):
            if abs(sum(diag)) == 3:
                return True
        return False

    def get_valid_moves(self):
        return [i for i, v in enumerate(self.board) if v == 0]
    
    def check_gameplay(self):
        return len(self.get_valid_moves()) >= 1
