from random import randint
board_count = 0
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def play_game():
    global board_count
    display_board()
    while board_count < 9:
        handle_turn()


def handle_turn():
    global board_count
    user_input = input('Enter a block: 1 - 9: ')
    allowed_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while int(user_input) - 1 not in allowed_input:
        print('Wrong input, try again')
        user_input = input('Enter a block: 1 - 9: ')
    board[int(user_input) - 1] = 'X'
    board_count += 1
    print(' ')
    display_board()
    winner_checker()
    cpu_input = randint(0, 8)
    while cpu_input == int(user_input) - 1:
        cpu_input = randint(0, 8)

    board[cpu_input] = 'O'
    board_count += 1
    print(' ')
    display_board()
    winner_checker()


def winner_checker(*args):
    winning_positions_x = ['X', 'X', 'X']
    winning_positions_o = ['O', 'O', 'O']
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    colum_1 = board[0] == board[3] == board[6] != '-'
    colum_2 = board[1] == board[4] == board[7] != '-'
    colum_3 = board[2] == board[5] == board[8] != '-'

    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'

    if row_1:
        if board[0] == 'X':
            print('User wins')
        else:
            print('CPU wins')
    elif row_2:
        if board[3] == 'X':
            print('User wins')
        else:
            print('CPU wins')
    elif row_3:
        if board[6] == 'X':
            print('User wins')
        else:
            print('CPU wins')
    elif colum_1:
        if board[0] == 'X':
            print('User wins')
        else:
            print('CPU wins')
    elif colum_2:
        if board[1] == 'X':
            print('User wins')
        else:
            print('CPU wins')
    elif colum_3:
        if board[2] == 'X':
            print('User wins')
        else:
            print('CPU wins')
    elif diagonal_1:
        if board[0] == 'X':
            print('User wins')
        else:
            print('CPU wins')
    elif diagonal_2:
        if board[6] == 'X':
            print('User wins')
        else:
            print('CPU wins')


play_game()
