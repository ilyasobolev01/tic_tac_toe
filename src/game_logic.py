"""
Core Game Logic for Tic-Tac-Toe.

This module contains the pure, state-agnostic functions that define the
rules of the game. It is responsible for creating the board, checking for
winners, and determining game-end conditions like a draw.

This module knows nothing about the UI, the AI, or how the game is run.
"""

from typing import List  # for older versions of Python


def create_board() -> List[List[str]]:
    """Creates an empty 3x3 board."""

    return [[" " for _ in range(3)] for _ in range(3)]
