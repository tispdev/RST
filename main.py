board = ["-", "-", "-",
         "-", "-", "-",
         "=", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

#print game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    #check if input is valid and if no player has gone there yet
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Spot is already taken!")

#check for win or tie
#check horizontles first
def checkHorizontle(board):
    #global makes changes to the  winner variable
    global winner
    #checks the board to see the winner
    if board[0] == board [1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board [5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return True


