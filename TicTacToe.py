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

def playerMoves (icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
        
    print ("Your turn player {}".format(number))
    
    choice = int (input ("Enter your move (1-9):").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print ()
        print ("Damn :-( That space is already taken!")
