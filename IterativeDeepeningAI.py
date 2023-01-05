# IterativeDeepeningAI
#
# AI that performs iterative deepening and continually prints its results
#
# William Dinauer, 2022

import math
import random
import time
from time import sleep

import chess
from AlphaBetaAI import AlphaBetaAI


class IterativeDeepeningAI():
    def __init__(self, depth):
        self.depth_lim = depth

    # Iterative Deepening
    def choose_move(self, board):
        best_move = list()
        for i in range(1, self.depth_lim+1):
            p = AlphaBetaAI(i)
            # choose a move for the specific depth
            move = p.choose_move(board)
            # accumulate best moves
            best_move.append(move)
            print("Depth: %d, Move: %s" % (i, move))
        # Return the best move at the furthest depth
        return best_move[self.depth_lim-1]
