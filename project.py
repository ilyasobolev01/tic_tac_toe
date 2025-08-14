from game_logic import create_board, print_board, check_winner#, is_board_full # (вам нужно будет ее дописать)

def main():
        board = create_board()
        current_player = 'X'
    
        while True:
            print_board(board)
            # ... здесь будет код для получения ввода от пользователя ...
            
            # ... здесь будет проверка победителя ...
            
            # ... здесь будет смена игрока (X -> O, O -> X) ...
            
            # Для начала просто выйдем из цикла
            break 


def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()