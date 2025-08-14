from game_logic import check_winner, is_board_full, get_available_moves

# Constants for readability
AI_PLAYER = 'O'
HUMAN_PLAYER = 'X'

def minimax(board, is_maximizing):
    """
    Recursively calculates the "score" for the current state of the board.
    """

    if check_winner(board, AI_PLAYER):
        return 10
    elif check_winner(board, HUMAN_PLAYER):
        return -10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row, col in get_available_moves(board):
            board[row][col] = AI_PLAYER
            score = minimax(board, False)
            board[row][col] = ' '  # Canceling the move.
            best_score = max(score, best_score)
        return best_score
    else: # Minimizing player
        best_score = float('inf')
        for row, col in get_available_moves(board):
            board[row][col] = HUMAN_PLAYER
            score = minimax(board, True)
            board[row][col] = ' ' # Canceling the move.
            best_score = min(score, best_score)
        return best_score
    
def get_ai_move(board):
    """
    Finds the best possible move for the AI using the Minimax algorythm.
    """
    best_score = -float('inf')
    best_move = None

    for row, col in get_available_moves(board):
        board[row][col] = AI_PLAYER  # Making the test move
        score = minimax(board, False) # Evaluating test the move (now it's human's turn)
        board[row][col] = ' '  # Canceling the test move

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move