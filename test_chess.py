# test_chess
#
# Simple test to play against any of the AI
#
# William Dinauer, 2022

import chess

from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IterativeDeepeningAI import IterativeDeepeningAI
import sys
from ComparisonAI import ComparisonAI

player1 = HumanPlayer()
player2 = IterativeDeepeningAI(4)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()