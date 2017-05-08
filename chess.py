# encoding definition
"""coding=utf-8"""
from colorama import Fore, Back, Style


# ChessBoard function definition
def ChessBoard(userColumns, userRows):
    board = ''
    # index for control lines
    for i in range(userRows):
        # index for control characters in lines
        for j in range(userColumns):
            if (i + j) % 2 == 0:
                board += Back.WHITE + ' ' + Back.RESET
            else:
                board += Back.BLACK + ' ' + Back.RESET
        board += '\n'
    print(board)


# input loop
while True:
    # script description
    print(Fore.RED + '\n=========================================' + Fore.YELLOW + 'v1.0.170508' + Fore.RESET)
    print(Fore.CYAN + 'This Python2/Python3 script will draw a chess board\nusing the following inputs...' + Style.DIM + Fore.WHITE + '\n(For exit, enter 0 in any of the inputs.)' + Fore.RESET + Style.RESET_ALL)
    print(Fore.BLUE + '----------------------------------------------------' + Fore.RESET)
    # user input prompt and evaluation
    try:
        userColumns = int(input(Fore.YELLOW + 'Enter a value for the number of COLUMNS: ' + Fore.RESET))
        userRows = int(input(Fore.YELLOW + 'Enter a value for the number of ROWS: ' + Fore.RESET))
    except Exception:
        print('\n' + Back.RED + ' *** INPUT ERROR ***' + Back.RESET + '\n' + Back.RED + ' Input value of Columns and Rows should be a Number. ' + Back.RESET)
        continue
    print(Fore.RED + '====================================================\n' + Fore.RESET)

    # user input evaluation
    if userColumns == 0 or userRows == 0:
        print(Back.MAGENTA + '-----------------' + Back.RESET)
        print(Back.MAGENTA + '|' + Back.RESET + Style.BRIGHT + '  Good Bye!!!  ' + Style.RESET_ALL + Back.MAGENTA + '|' + Back.RESET)
        print(Back.MAGENTA + '-----------------' + Back.RESET + '\n')
        break
    elif userColumns < 3 or userRows < 3:
        print(Back.RED + ' *** INPUT ERROR *** ' + Back.RESET + '\n' + Back.RED + ' Input value of Columns and Rows should not be less than 3 units. ' + Back.RESET)
    else:
        # board outputs
        ChessBoard(userColumns, userRows)
        break
