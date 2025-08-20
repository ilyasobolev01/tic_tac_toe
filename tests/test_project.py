"""
Integration tests for the main TicTacToe application (main.py).

This test suite verifies that all components of the application (game logic,
AI player, and Textual UI) work together correctly. It uses the Textual
Pilot to simulate user interactions like clicking on cells and then asserts
on the application's state and visual output.

These tests cover end-to-end user scenarios, such as:
- A full gameplay loop (human move -> AI move).
- Winning, losing, and draw conditions.
- User input validation (e.g., clicking on an occupied cell).
"""

import pytest

from project import TicTacToeApp, HUMAN_PLAYER, AI_PLAYER


@pytest.mark.asyncio
async def test_initial_state():
    """Tests that the application starts in a correct, clean state."""
    # Arrange
    app = TicTacToeApp()

    # Act & Assert
    async with app.run_test() as pilot:
        info_label = pilot.app.query_one("#info-label").renderable
        assert "Your turn (X)" in str(info_label)

        assert all(cell == " " for row in pilot.app.board for cell in row)
        assert not pilot.app.game_over
        assert pilot.app.current_player == HUMAN_PLAYER


@pytest.mark.asyncio
async def test_human_player_makes_a_valid_move():
    """Tests a full turn: human makes a valid move, and the AI responds."""
    # Arrange
    app = TicTacToeApp()

    # Act
    async with app.run_test() as pilot:
        await pilot.click("#cell-1-1")
        # Wait for the AI's turn (the app has a 1.0s delay)
        await pilot.pause(1.5)

        # Assert
        # 1. Human's move is registered
        assert pilot.app.board[1][1] == HUMAN_PLAYER

        # 2. AI has made a move in response
        ai_move_made = any(
            pilot.app.board[r][c] == AI_PLAYER
            for r in range(3)
            for c in range(3)  # noqa: E501
        )
        assert ai_move_made

        # 3. Control has returned to the human player
        info_label = pilot.app.query_one("#info-label").renderable
        assert "Your turn (X)" in str(info_label)
        assert pilot.app.current_player == HUMAN_PLAYER


@pytest.mark.asyncio
async def test_click_on_occupied_cell_is_ignored():
    """Ensures that clicking on an already occupied cell has no effect."""
    # Arrange
    app = TicTacToeApp()
    async with app.run_test() as pilot:
        #   _ | _ | _
        #   _ | X | _
        #   _ | _ | _
        pilot.app.board[1][1] = HUMAN_PLAYER
        pilot.app.update_board_display()
        # Set turn to AI to ensure no move is made accidentally
        pilot.app.current_player = AI_PLAYER
        await pilot.pause()

        initial_board_state = [row[:] for row in pilot.app.board]

        # Act: Attempt to click the occupied cell
        await pilot.click("#cell-1-1")
        await pilot.pause()

        # Assert: The board and player have not changed
        assert pilot.app.board == initial_board_state
        assert pilot.app.current_player == AI_PLAYER


@pytest.mark.asyncio
async def test_human_win_condition():
    """Tests the scenario where the human player makes a winning move."""
    # Arrange
    app = TicTacToeApp()
    async with app.run_test() as pilot:
        # Set up a board where the human is one move away from winning
        #   X | X | _  <- Winning move here
        #   O | O | _
        #   _ | _ | _
        pilot.app.board = [
            [HUMAN_PLAYER, HUMAN_PLAYER, " "],
            [AI_PLAYER, AI_PLAYER, " "],
            [" ", " ", " "],
        ]
        pilot.app.update_board_display()
        await pilot.pause()

        # Act: Human makes the winning move
        await pilot.click("#cell-0-2")
        await pilot.pause(0.5)

        # Assert: The game ends with a human win
        assert pilot.app.game_over
        assert pilot.app.winner == HUMAN_PLAYER
        info_label = pilot.app.query_one("#info-label").renderable
        assert "Player X wins!" in str(info_label)
        assert pilot.app.has_class("win")


@pytest.mark.asyncio
async def test_ai_win_condition():
    """Tests the scenario where the AI player wins."""
    # Arrange
    app = TicTacToeApp()
    async with app.run_test() as pilot:
        # Set up a board where the AI will win on its next move
        #   O | O | _  <- AI winning move here
        #   X | X | _
        #   _ | _ | _
        pilot.app.board = [
            [AI_PLAYER, AI_PLAYER, " "],
            [HUMAN_PLAYER, HUMAN_PLAYER, " "],
            [" ", " ", " "],
        ]
        pilot.app.current_player = AI_PLAYER
        pilot.app.update_board_display()
        await pilot.pause()

        # Act: Trigger the AI's move directly for a predictable outcome
        pilot.app.make_ai_move()
        await pilot.pause(0.5)

        # Assert: The game ends with an AI win
        assert pilot.app.game_over
        assert pilot.app.winner == AI_PLAYER
        info_label = pilot.app.query_one("#info-label").renderable
        assert "Player O wins!" in str(info_label)
        assert pilot.app.has_class("loss")


@pytest.mark.asyncio
async def test_draw_condition():
    """Tests the scenario that results in a draw."""
    # Arrange
    app = TicTacToeApp()
    async with app.run_test() as pilot:
        # Set up a board where the next human move results in a draw
        #   X | O | X
        #   X | O | O
        #   O | X | _  <- Final move here
        pilot.app.board = [
            [HUMAN_PLAYER, AI_PLAYER, HUMAN_PLAYER],
            [HUMAN_PLAYER, AI_PLAYER, AI_PLAYER],
            [AI_PLAYER, HUMAN_PLAYER, " "],
        ]
        pilot.app.update_board_display()
        await pilot.pause()

        # Act: Human makes the final move
        await pilot.click("#cell-2-2")
        await pilot.pause(0.5)

        # Assert: The game ends in a draw
        assert pilot.app.game_over
        assert pilot.app.winner is None
        info_label = pilot.app.query_one("#info-label").renderable
        assert "It's a draw!" in str(info_label)
        assert pilot.app.has_class("draw")
