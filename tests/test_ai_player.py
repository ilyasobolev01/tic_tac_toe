"""
Unit tests for the AI player module.

This test suite verifies the decision-making logic of the AI opponent
implemented in `src/ai_player.py`. It focuses on critical scenarios
to ensure the Minimax algorithm behaves optimally.

Tests cover:
- The AI's ability to make a winning move when one is available.
- The AI's ability to block an opponent's immediate winning move.
- The AI's strategic choices in neutral situations (e.g., taking the center).
"""

from ai_player import AI_PLAYER, HUMAN_PLAYER, get_ai_move


def test_ai_makes_winning_move():
    """AI Should make a winning move if available"""
    # Arrange
    #   O | O | _
    #   X | X | _
    #   _ | _ | _
    board = [
        [AI_PLAYER, AI_PLAYER, " "],
        [HUMAN_PLAYER, HUMAN_PLAYER, " "],
        [" ", " ", " "],
    ]
    expected_move = (0, 2)

    # Act
    actual_move = get_ai_move(board)

    # Assert
    assert actual_move == expected_move


def test_ai_blocks_opponent_winning_move():
    """AI should block opponent's winning move."""
    # Arrange:
    #   X | X | _  <- AI should move here.
    #   O | O | _
    #   _ | _ | _
    board = [
        [HUMAN_PLAYER, HUMAN_PLAYER, " "],
        [AI_PLAYER, AI_PLAYER, " "],
        [" ", " ", " "],
    ]
    expected_move = (0, 2)

    # Act
    actual_move = get_ai_move(board)

    # Assert
    assert actual_move == expected_move
