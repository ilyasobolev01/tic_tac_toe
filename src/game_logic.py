"""
Core Game Logic for Tic-Tac-Toe.

This module contains the pure, state-agnostic functions that define the
rules of the game. It is responsible for creating the board, checking for
winners, and determining game-end conditions like a draw.

This module knows nothing about the UI, the AI, or how the game is run.
"""

from typing import List, Tuple  # for older versions of Python


def create_board() -> List[List[str]]:
    """Creates an empty 3x3 board."""

    return [[" " for _ in range(3)] for _ in range(3)]


def check_winner(board: List[List[str]], player: str) -> bool:
    """Checks if the specified player has won the game."""

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    # The main diagonal: row index equals column index (0,0), (1,1), (2,2)
    if all(board[i][i] == player for i in range(3)):
        return True

    # The anti-diagonal is where row index + column index always equals 2s
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board: List[List[str]]) -> bool:
    """Checks if the game board is full"""
    return all(" " not in row for row in board)


def get_available_moves(board) -> List[Tuple[int, int]]:
    """Returns a list of all available (empty) moves on the board."""
    moves = []

    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == " ":
                moves.append((row_idx, col_idx))
    return moves
