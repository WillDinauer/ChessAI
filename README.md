# Chess AI
William Dinauer, Fall 2022

## Description
This is an artificial intelligence program built using Python to play the game of chess. There are different types of Chess AI that I have implemented, using different algorithms in an attempt to optimize the bot.
Notably, the Minimax algorithm is used to find a decent move by searching up to a specified depth. Alpha-Beta Pruning is used to increase the efficiency of the AI, decreasing the search space given the size of the depth.

To play against the bot, change player1 (White) or player2 (Black) to HumanPlayer in either test_chess.py or gui_chess.py

## Usage

To run the AI, either run test_chess.py or gui_chess.py.
test_chess.py allows a human player to play against any AI they may choose.
gui_chess.py allows a visual representation of two AI playing against each other.

You can test different AI by replacing player1 and player2 with the respective AI you'd like to test.
I'd recommend not going beyond a depth of 4-5 for most AI as the runtime gets exponentially longer to find a move.
