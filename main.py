import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


def display_instructions():
    print("""
        Welcome to Tic-Tac-Toe!

        Instructions:
        1. The game is played on a 3x3 grid.
        2. Players take turns to place their marker (X or O) in an empty cell.
        3. The first player to align three markers horizontally, vertically, or diagonally wins.
        4. If all 9 cells are filled and no player has aligned three markers, the game ends in a draw.
        5. Grid starts at 1 and goes to 9. (Left to right)

        Have fun!
        """)
def tic_tac_toe_menu():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        show_instructions = input("Do you want to see the instructions? (yes/no): ").strip().lower()
        if show_instructions in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if show_instructions == "yes":
        display_instructions()

    while True:
        mode = input("Do you want to play against another player or the computer? (player/computer): ").strip().lower()
        if mode in ["player", "computer"]:
            return mode
        else:
            print("Invalid input. Please type 'player' or 'computer'.")

tic_tac_toe_menu()


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def computerInput(board):
    while True:
        inp = random.randint(1, 9)
        if board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            break


def playerInput(board):
    while True:
        try:
            inp = int(input("Enter a number 1-9: "))
            if 1 <= inp <= 9:
                if board[inp - 1] == "-":
                    board[inp - 1] = currentPlayer
                    break
                else:
                    print("Spot is already taken, try again!")
            else:
                print("Enter a number between 1 and 9!")
        except ValueError:
            print("Invalid input. Enter a number 1-9.")


def checkHorizontle(board):
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


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board [4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] == board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!!")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

mode = tic_tac_toe_menu()
while gameRunning:
    printBoard(board)
    if mode == "player" or currentPlayer == "X":
        playerInput(board)
    else:
        computerInput(board)
    checkWin()
    checkTie(board)
    if gameRunning:
        switchPlayer()

