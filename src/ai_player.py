"""
AI Player featuring the Minimax Algorithm.

This module provides the AI opponent for the Tic-Tac-Toe game. The AI's
decision-making is powered by the Minimax algorithm, a recursive function
that explores all possible future game states to find the optimal move.

The primary function intended for external use is `get_ai_move()`, which
evaluates the current board and returns the coordinates for the best
possible move for the AI player ('O'). The implementation assumes that the
AI is the maximizing player, aiming for a win (+10), while the human is the
minimizing player (-10).
"""

from game_logic import check_winner, get_available_moves, is_board_full
from typing import List, Tuple, Optional

# Constants for readability
AI_PLAYER = "O"
HUMAN_PLAYER = "X"


def minimax(board, is_maximizing):
    """Recursively calculates "score" for current state of the board."""

    if check_winner(board, AI_PLAYER):
        return 10

    elif check_winner(board, HUMAN_PLAYER):
        return -10

    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row, col in get_available_moves(board):
            board[row][col] = AI_PLAYER
            score = minimax(board, False)
            board[row][col] = " "  # Canceling the move.
            best_score = max(score, best_score)

        return best_score

    else:  # Minimizing player
        best_score = float("inf")
        for row, col in get_available_moves(board):
            board[row][col] = HUMAN_PLAYER
            score = minimax(board, True)
            board[row][col] = " "  # Canceling the move.
            best_score = min(score, best_score)
        return best_score


def get_ai_move(board: List[List[str]]) -> Optional[Tuple[int, int]]:
    """
    Finds the best possible move for the AI using the Minimax algorithm.

    This function serves as the top-level interface for the AI's
    decision-making. It iterates through all available moves on the current
    board. For each potential move, it calls the recursive `minimax`
    function to evaluate the long-term outcome. It then returns the move
    that corresponds to the highest score.
    """
    best_score = -float("inf")
    best_move = None

    for row, col in get_available_moves(board):

        board[row][col] = AI_PLAYER

        score = minimax(board, False)

        board[row][col] = " "

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move
