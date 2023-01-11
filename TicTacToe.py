"""
TicTacToe.py.py
Ashley Ung 
This program functions as a tic tac toe game amongst 2 players, using the command line. 
"""

def displayBoard ():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print ()
    print (row1)
    print (row2)
    print (row3)
    print ()
