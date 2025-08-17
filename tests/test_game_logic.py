"""
Unit tests for the core game logic module.

This test suite verifies the correctness of the functions defined in
`src/game_logic.py`. It covers scenarios such as:
- Board creation.
- Win condition checking (horizontal, vertical, diagonal).
- Draw condition checking.
- Retrieval of available moves.
"""

# Sources:
# 1. Roy Osherove's Naming Standards for Tests
# https://www.google.com/url?sa=E&q=https%3A%2F%2Fosherove.com%2Fblog%2F2005%2F4%2F3%2Fnaming-standards-for-unit-tests.html
# 2. Abstract: Behavior-Driven Developement - Given-When-Then
# 3. Test-Driven Developement: By Example by Kent Beck
# 4. Arrange-Act-Assert:
# https://www.google.com/url?sa=E&q=http://xunitpatterns.com/Arrange%20Act%20Assert.html

from game_logic import create_board, check_winner, is_board_full, get_available_moves


def test_create_board_returns_a_clean_3x3_grid():
    """
    Should return an empty 3x3 grid.
    """
    # Arrange
    expected_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Act
    actual_board = create_board()

    # Assert
    assert actual_board == expected_board


def test_check_winner_with_horizontal_win():
    """Should return True for a horizontal win."""
    board = [["X", "X", "X"], ["O", " ", "O"], [" ", " ", " "]]
    assert check_winner(board, "X") is True


def test_check_winner_with_vertical_win():
    """Should return True for a vertical win."""
    board = [["O", "X", " "], ["O", "X", " "], [" ", "X", "O"]]
    assert check_winner(board, "X") is True


def test_check_winner_with_diagonal_win():
    """Should return True for a diagonal win."""
    board = [["O", " ", "X"], [" ", "X", "O"], ["X", " ", " "]]
    assert check_winner(board, "X") is True


def test_check_winner_on_ongoing_game():
    """Should return False when no winner is present."""
    board = [["X", "O", "X"], ["O", " ", " "], [" ", " ", " "]]
    assert check_winner(board, "X") is False
    assert check_winner(board, "O") is False


def test_check_winner_returns_false_for_other_player():
    """Should return False if we check for 'O' but 'X' won."""
    board = [["X", "X", "X"], ["O", " ", "O"], [" ", " ", " "]]
    assert check_winner(board, "O") is False


def test_get_available_moves_with_empty_cells():
    """Should return a list of tuples for each empty cell on the board"""

    board = [
        ["X", "O", "X"],
        ["X", "O", " "],
        ["O", " ", " "],
    ]

    expected_moves = [(1, 2), (2, 1), (2, 2)]

    actual_moves = get_available_moves(board)

    assert set(expected_moves) == set(actual_moves)


def test_is_board_full_with_full_board():
    """Should return True for a full board"""

board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "X", "O"]
    ]

assert is_board_full(board) is True

def test_is_board_full_with_empty_board():
    """Should return False for an empty board"""

board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

assert is_board_full(board) is False


def test_is_board_full_for_ongoing_game():
    """Should return False for an onging game"""

board = [
        ["X", "X", "O"],
        ["O", " ", " "],
        ["", " ", " "]
    ]

assert is_board_full(board) is False
