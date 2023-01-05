# ComparisonAI
#
# A test AI for comparing Minimax and AlphaBeta
#
# William Dinauer, 2022

import chess
from AlphaBetaAI import AlphaBetaAI
from MinimaxAI import MinimaxAI

class ComparisonAI():
    def __init__(self, depth):
        self.depth_lim = depth

    # Iterative Deepening
    def choose_move(self, board):
        mmAI = MinimaxAI(self.depth_lim)
        abAI = AlphaBetaAI(self.depth_lim)

        mm_move = mmAI.choose_move(board)
        ab_move = abAI.choose_move(board)

        return ab_move