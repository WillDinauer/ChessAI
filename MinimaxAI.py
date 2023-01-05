# MinimaxAI
# William Dinauer, 2022

import math
import random
import time
from time import sleep

import chess


class MinimaxAI():
    def __init__(self, depth):
        self.depth_lim = depth
        self.max_calls = 0
        self.min_calls = 0

    # Minimax Search
    def choose_move(self, board):
        player = 1 - int(board.turn)
        self.max_calls = 0
        self.min_calls = 0
        value, move = self.max_value(board, 0, player)
        print("chosen move: %s" % move)
        print("max calls: %d" % self.max_calls)
        print("min calls: %d" % self.min_calls)
        print("Minimax Value: %f" % value)
        return move

    # Return Max Value Move for Minimax
    def max_value(self, board, depth, player):
        self.max_calls += 1
        # Terminal state
        if board.is_game_over():
            return self.terminal_utility(board, player)

        # Depth limit reached - return the current evaluation
        if depth == self.depth_lim:
            return self.evaluation(board, player), None

        # Initialize the move and value to return
        v = -math.inf
        final_move = None
        moves = list(board.legal_moves)
        # Shuffle the moves to avoid repetition
        random.shuffle(moves)
        # Recurse over every possible move
        for move in moves:
            # Try the move
            board.push(move)
            v2, a2 = self.min_value(board, depth + 1, player)
            if v2 > v:  # Found a better move!
                v = v2
                final_move = move
            # Undo the move
            board.pop()
        return v, final_move

    # Return Min Value Move for Minimax
    def min_value(self, board, depth, player):
        self.min_calls += 1
        # Terminal state
        if board.is_game_over():
            return self.terminal_utility(board, player)

        # Depth limit reached - return the current evaluation
        if depth == self.depth_lim:
            return self.evaluation(board, player), None

        # Initialize the move and value to return
        v = math.inf
        final_move = None
        moves = list(board.legal_moves)
        # Shuffle the moves to avoid repetition
        random.shuffle(moves)
        # Recurse over every possible move
        for move in moves:
            # Try the move
            board.push(move)
            v2, a2 = self.max_value(board, depth + 1, player)
            if v2 < v:  # Found a better move!
                v = v2
                final_move = move
            # Undo the move
            board.pop()
        return v, final_move

    # Evaluation Function
    def evaluation(self, board, player):
        # Look at the piece map
        dictionary = board.piece_map()

        # Piece scores for black and white
        black = 0
        white = 0

        # Loop over every piece
        for idx in dictionary:
            p = dictionary[idx]
            piece = p.piece_type

            # Add white pieces to white's score
            if p.color:
                if piece == 1:                      # Pawn
                    white += 1
                elif piece == 2 or piece == 3:      # Knight and Bishop
                    white += 3
                elif piece == 4:                    # Rook
                    white += 5
                elif piece == 5:                    # Queen
                    white += 8
            # Add black pieces to black's score
            else:
                if piece == 1:                      # Pawn
                    black += 1
                elif piece == 2 or piece == 3:      # Knight and Bishop
                    black += 3
                elif piece == 4:                    # Rook
                    black += 5
                elif piece == 5:                    # Queen
                    black += 8

        # Try to Control the Center
        center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]
        for square in center_squares:
            for piece in board.attackers(chess.WHITE, square):
                white += 0.01
            for piece in board.attackers(chess.BLACK, square):
                black += 0.01

        # Avoid Checks and Look for Checks
        # if board.is_check():
        #     in_check = 1-board.turn
        #     if in_check == white:
        #         black += .5
        #     else:
        #         white += .5

        # Evaluation depending on the current player
        if player == 0:
            # Incentive to turn white pawns into better pieces even when black lacks pieces
            if black == 0:
                return (white/(white+5))-0.5
            return (white/(white+black))-0.5
        # Same incentive for black pawns when white lacks pieces
        if white == 0:
            return (black/(black+5))-0.5
        return (black/(white+black))-0.5

    # Utility Function (Game Over)
    def terminal_utility(self, board, player):
        # If we're already in checkmate, return -1 if we're the current player (loss)
        if board.is_checkmate():
            if 1 - int(board.turn) is player:
                return -1, None
            return 1, None
        # return 0 otherwise - we have a draw
        return 0, None
