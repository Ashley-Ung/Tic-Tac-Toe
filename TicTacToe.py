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
        
def IsDraw ():
    if " " not in board:
        return True
    else:
        return False

def bIsWinner (icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

    
board = [" " for x in range (9)]

while True:
    displayBoard ()
    playerMoves ("X")
    displayBoard ()
    if bIsWinner ("X"):
        print ("Yay! X wins!")
        break
    elif IsDraw ():
        print ("Yay, it's a Draw!")
        break
    playerMoves ("O")
    if bIsWinner ("O"):
        displayBoard ()
        print ("Yay! O wins!")
        break
    elif IsDraw ():
        print ("It's a IsDraw!")
        break
    
