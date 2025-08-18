"""
Main entry point and TUI controller for the Tic-Tac-Toe application.

This module is responsible for orchestrating the entire game. It uses the
Textual framework to build, render, and manage the interactive terminal
user interface.

Its key responsibilities include:
- Composing the layout of the game grid and all other UI widgets.
- Handling user input, specifically mouse clicks on the game cells.
- Managing the application's state (the board, current player, game-over status).
- Triggering the AI's turn after a delay and updating the board with its move.
- Integrating the pure game rules from `game_logic.py` and the optimal
  move calculation from `ai_player.py` to create a complete and interactive
  game loop.
- Handling the end-of-game sequence (displaying results and exiting).
"""

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static


class TicTacToeCell(Static):
    """A widget representing a single, clickable cell in the Tic-Tac-Toe grid."""

    pass


class TicTacToeApp(App):
    """The main Textual application for the Tic-Tac-Toe game."""

    def compose(self):
        """
        Creates the layout and widgets for the application.
        This method is called once when the app starts.
        """

        yield Static("Your turn (X)", id="info-label")

        with Container(id="center-container"):
            with Container(id="game-grid"):
                for r in range(3):
                    for c in range(3):
                        yield TicTacToeCell(id=f"cell-{r}-{c}")


if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
