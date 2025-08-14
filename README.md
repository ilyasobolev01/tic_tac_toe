
# TIC-TAC-TOERTURE
    #### Video Demo:  <URL HERE>
    #### Description:

A console-based implementation of Tic-Tac-Toe where a human player competes against an AI opponent. The goal is to create an AI that can never be beaten.

* **`project.py`**: This will be the main entry point. It will contain the primary game loop and handle user interaction (like getting player input). 

* **`game_logic.py`**: This module will contain the core game mechanics, independent of the user or AI. Things like checking for a winner, checking for a draw, and printing the board. 

* **`ai_player.py`**: All the AI-specific logic will go here. This is where the Minimax algorithm will be implemented. 

* **`test_project.py`**: Contains all the tests for the functions in `project.py`, `game_logic.py` and `ai_player.py`.

## Design Decisions 

1.  **Board Representation:** I chose to represent the game board as a list of lists (a 3x3 matrix), e.g., `[['X', 'O', ' '], ...]`. The alternative was a flat list of 9 elements. I opted for the matrix structure because it makes the logic for checking rows and columns much more intuitive and readable. Mapping a 2D grid to a 2D list feels more natural than calculating indices for a 1D list.

2.  **AI Algorithm:** Instead of using a simple set of `if/else` rules for the AI (e.g., "take the center if available"), I decided to implement the **Minimax algorithm**. While more complex, this approach guarantees truly optimal play. It was a deliberate choice to explore a classic AI algorithm and ensure the project's core promise of an "unbeatable" opponent was met.

3.  **Modular Structure:** The code is split into `main.py`, `game_logic.py`, and `ai_player.py`. This was a conscious decision to enforce **Separation of Concerns**. `game_logic.py` knows nothing about the AI or the user interface; it only knows the rules of Tic-Tac-Toe. This separation made testing significantly easier, as I could write unit tests for the game's core rules and the AI's logic independently.

4. **File Naming Convention:** The project's file and module names use `snake_case` (e.g., `game_logic.py`). This choice was made for two primary reasons:

    1.  **PEP 8 Compliance:** It follows the official Python style guide, promoting code readability and consistency with community standards.
    
    2.  **Cross-Platform Compatibility:** This convention eliminates potential import errors caused by case-sensitivity differences between operating systems. File systems on development machines (like Windows/macOS) are often case-insensitive, while deployment environments (like Linux servers) are case-sensitive. Using all-lowercase names ensures the code is portable and robust.

*(To be filled in after development)*

