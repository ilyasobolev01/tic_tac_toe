from game_logic import check_winner, create_board
from ai_player import get_ai_move

def test_function_1():
    ...


def test_function_2():
    ...


def test_function_n():
    ... 

def test_check_winner():
    board = create_board()
    board[0][0] = 'X'
    board[0][1] = 'X'
    board[0][2] = 'X'
    assert check_winner(board, 'X') == True  # Проверяем победу в строке
    assert check_winner(board, 'O') == False # Убеждаемся, что для 'O' победы нет

def test_no_winner():
    board = create_board()
    board[0][0] = 'X'
    board[1][1] = 'O'
    board[2][0] = 'X'
    assert check_winner(board, 'X') == False
    assert check_winner(board, 'O') == False

def test_ai_makes_winning_move():
    #   O | O | _
    #   _ | X | _
    #   X | _ | _
    board = [
        ['O', 'O', ' '],
        [' ', 'X', ' '],
        ['X', ' ', ' ']
    ]
    # ИИ ('O') должен сделать выигрышный ход в (0, 2)
    assert get_ai_move(board) == (0, 2)

def test_ai_blocks_winning_move():
    #   X | X | _
    #   _ | O | _
    #   O | _ | _
    board = [
        ['X', 'X', ' '],
        [' ', 'O', ' '],
        ['O', ' ', ' ']
    ]
    # ИИ ('O') должен заблокировать ход человека в (0, 2)
    assert get_ai_move(board) == (0, 2)