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

from game_logic import create_board


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
