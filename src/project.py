"""
Main entry point and TUI controller for the Tic-Tac-Toe application.

This module is responsible for orchestrating the entire game. It uses the
Textual framework to build, render, and manage the interactive terminal
user interface.

Its key responsibilities include:
- Composing the layout of the game grid and all other UI widgets.
- Handling user input, specifically mouse clicks on the game cells.
- Managing the application's state
(the board, current player, game-over status).
- Triggering the AI's turn after a delay
 and updating the board with its move.
- Integrating the pure game rules from `game_logic.py` and the optimal
  move calculation from `ai_player.py` to create a complete and interactive
  game loop.
- Handling the end-of-game sequence (displaying results and exiting).
"""

from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static
from textual.message import Message
from textual.reactive import reactive

from game_logic import create_board, check_winner, is_board_full
from ai_player import get_ai_move, HUMAN_PLAYER, AI_PLAYER

CSS_PATH = Path(__file__).parent.parent / "assets" / "main.css"


class TicTacToeCell(Static):
    """
    A widget representing a single, clickable cell in the Tic-Tac-Toe grid.
    """

    def __init__(self, row: int, col: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.row = row
        self.col = col

    class Clicked(Message):
        """A custom message to be sent when a cell is clicked."""

        def __init__(self, row: int, col: int) -> None:
            self.row = row
            self.col = col
            super().__init__()

    def on_click(self) -> None:
        """Handles a mouse click event on this cell."""
        self.post_message(self.Clicked(self.row, self.col))


class TicTacToeApp(App):
    """The main Textual application for the Tic-Tac-Toe game."""

    CSS_PATH = CSS_PATH

    board = reactive(create_board)
    current_player = reactive(HUMAN_PLAYER)
    game_over = reactive(False)
    winner = reactive(None)

    def compose(self) -> ComposeResult:
        """
        Creates the layout and widgets for the application.
        This method is called once when the app starts.
        """

        yield Static("Your turn (X)", id="info-label")

        with Container(id="center-container"):
            with Container(id="game-grid"):
                for r in range(3):
                    for c in range(3):
                        yield TicTacToeCell(row=r, col=c, id=f"cell-{r}-{c}")

    def on_tic_tac_toe_cell_clicked(
        self, message: TicTacToeCell.Clicked
    ) -> None:  # noqa: E501
        """A message handler that is called when any TicTacToeCell posts a `Clicked` message."""  # noqa: E501

        if self.game_over or self.current_player != HUMAN_PLAYER:
            return

        if self.board[message.row][message.col] == " ":
            self.board[message.row][message.col] = HUMAN_PLAYER
            self.update_board_display()
            self.check_game_state()

            if not self.game_over:
                self.current_player = AI_PLAYER
                self.query_one("#info-label", Static).update(
                    "AI is thinking..."
                )  # noqa: E501
                self.set_timer(1.0, self.make_ai_move)

    def make_ai_move(self) -> None:
        """Calculates and performs the AI's move."""
        row, col = get_ai_move(self.board)
        self.board[row][col] = AI_PLAYER
        self.update_board_display()
        self.check_game_state()

        if not self.game_over:
            self.current_player = HUMAN_PLAYER
            self.query_one("#info-label", Static).update("Your turn (X)")

    def check_game_state(self) -> None:
        """Checks if the game has ended (either by a win or a draw) and updates the state."""  # noqa: E501

        if check_winner(self.board, self.current_player):  # noqa: E501
            self.game_over = True
            self.winner = self.current_player
            self.query_one("#info-label", Static).update(
                f"Player {self.winner} wins!"
            )  # noqa: E501
            self.update_colors()
            self.set_timer(2.0, self.exit_game)
        elif is_board_full(self.board):
            self.game_over = True
            self.query_one("#info-label", Static).update("It's a draw!")
            self.update_colors()
            self.set_timer(2.0, self.exit_game)

    def update_board_display(self) -> None:
        """Updates the visual display of the grid to match the internal `self.board` state."""  # noqa: E501
        for r in range(3):
            for c in range(3):
                cell_widget = self.query_one(f"#cell-{r}-{c}", TicTacToeCell)
                cell_widget.update(self.board[r][c])

    def update_colors(self) -> None:
        """Applies a CSS class to the root widget to change the board's color scheme."""  # noqa: E501
        if self.winner == HUMAN_PLAYER:
            self.add_class("win")
        elif self.winner == AI_PLAYER:
            self.add_class("loss")
        else:
            self.add_class("draw")

    def exit_game(self) -> None:
        """A simple method to exit the application."""
        self.exit()


if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
