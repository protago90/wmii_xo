import random
import time
from functools import reduce


class Agent():
    DEBUG = False
    NAP = 0

    def __init__(self, sign, nap=None, debug=None):
        self.sign = sign
        self.nap = nap if nap else Agent.NAP
        self.debug = debug if debug else Agent.DEBUG
    
    def make_move(self, board):
        pass


class HumanUI(Agent):
    def __init__(self, sign, nap=None, debug=None):
        super().__init__(sign)
        self.id = 'Human'

    def make_move(self, board):
        while True:
            try:
                pos = int(input(f'# Pick position 1-9: ')) - 1
                if pos in board.get_open_moves():
                    return pos
            except ValueError: pass


class AIBot(Agent):
    def __init__(self, sign, nap=None, debug=None):
        super().__init__(sign, nap, debug)
    
    def make_move(self, board):
        time.sleep(self.nap)
        ##if board.check_open_board():
        ##    return random.choice(board.get_open_moves())
        #moves = board.get_open_moves()
        #if len(moves) == 9:
        #    return random.choice([0, 8])
        #if len(moves) == 8:
        #    return 4 if 4 in moves else random.choice([2, 6])
        return self._get_move(board)

    def _get_move(self, board):
        pass


class RandomBot(AIBot):
    def __init__(self, sign, nap=None, debug=None):
        super().__init__(sign, nap)
        self.id = 'Random'
    
    def _get_move(self, board):
        return random.choice(board.get_open_moves())


class DebutsBot(AIBot):
    def __init__(self, sign, nap=None, debug=None):
        super().__init__(sign, nap)
        self.id = 'Debuts'

    def _get_move(self, board):
        sign = 'X' if self.sign == 'O' else 'O'
        moves = board.get_open_moves()
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


class SearchBot(AIBot):
    def __init__(self, sign, nap=None, debug=None):
        super().__init__(sign, nap, debug)

    def _get_move(self, board):
        records = []
        for pos in board.get_open_moves():
            board.process_move(self.sign, pos)
            score = self._eval_game_branch_with_rule(board, self.sign, 1)
            board.undo_move()
            records.append((pos, score))
        if self.debug:
            print(f'# "{self.sign}" -> {[(p+1, round(s, 1)) for p, s in records]}')
        the_pos = self._eval_top_heuristic(records)
        return the_pos

    def _eval_game_branch_with_rule(self, board, sign, step):
        final = self._eval_final_state(board, sign, step)
        if final is not None:
            return final
        sign = 'X' if sign == 'O' else 'O'
        step += 1
        scores = []
        for pos in board.get_open_moves():
            board.process_move(sign, pos)
            scores.append(
                self._eval_game_branch_with_rule(board, sign, step))
            board.undo_move()
        return self._eval_heuristic(sign, scores)

    def _eval_final_state(self, board, sign, step):
        pass

    def _eval_heuristic(self, sign, scores):
        pass

    def _eval_top_heuristic(self, pos_score_pairs):
        pass


class MinMaxBot(SearchBot):
    def __init__(self, sign, nap=None, debug=None):
        super().__init__(sign, nap, debug)
        self.id = 'Minmax'

    def _eval_final_state(self, board, sign, step):
        if board.winner:
            return 1 if self.sign == sign else -1
        if not board.check_open_moves():
            return 0
        return None

    def _eval_heuristic(self, sign, scores):
        return max(scores) if self.sign == sign else min(scores)

    def _eval_top_heuristic(self, pos_score_pairs):
        return sorted(
            pos_score_pairs, key=lambda xy: (xy[1], random.random()), reverse=True
        )[0][0]


class CustomBot(SearchBot):
    def __init__(self, sign, nap=None, debug=None):
        super().__init__(sign, nap, debug)
        self.id = 'Custom'

    def _eval_final_state(self, board, sign, step):
        d = (1/step**2) 
        if board.winner:
            return 1 * d if self.sign == sign else -1 * d
        if not board.check_open_moves():
            return 0
        return None

    def _eval_heuristic(self, sign, scores):
        return sum(scores)

    def _eval_top_heuristic(self, pos_score_pairs):
        return sorted(
            pos_score_pairs, key=lambda xy: (xy[1], random.random()), reverse=True
        )[0][0]
