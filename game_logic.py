"""
This module contains the core, pure logic for the Tic-Tac-Toe game.

It is responsible for creating the board, checking game state (win/draw),
and providing utility functions related to the game rules. It does not
handle any user input or AI logic.
"""

def create_board():
    """Creates a new, empty 3x3 game board.

    Returns:
        list[list[str]]: A list of lists representing the empty board.
    """
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

def print_board(board):
    """Prints the game board to the console."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    """Checks if the specified player has won the game.

    It checks all rows, columns, and both main diagonals for a winning
    three-in-a-row combination.

    Args:
        board (list[list[str]]): The 3x3 game board represented as a list of lists.
        player (str): The player's symbol to check for ('X' or 'O').

    Returns:
        bool: True if the specified player has won, False otherwise.
    """

    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    # Check diagonals
    # The main diagonal is where row index equals column index (0,0), (1,1), (2,2)
    if all(board[i][i] == player for i in range(3)):
        return True
    
    # The anti-diagonal is where row index + column index always equals 2s
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

if __name__ == '__main__':
    my_board = create_board()
    print("Empty board:")
    print_board(my_board)

    my_board[1][1] = 'X'
    print("\nBoard with a move:")
    print_board(my_board)