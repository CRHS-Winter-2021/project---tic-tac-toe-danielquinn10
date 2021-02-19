import random

##Tic Tac Toe
#Name:Daniel Quinn
#Date:


#1. (Var) Setup the empty board as a list
theBoard = [
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]


#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none
def printBoard(board):
    print(theBoard[7], "|", theBoard[8], "|", theBoard[9])
    print("---------")
    print(theBoard[4], "|", theBoard[5], "|", theBoard[6])
    print("---------")
    print(theBoard[1], "|", theBoard[2], "|", theBoard[3])


#3a. (fun) Determine if player is X or O
player1 = ''
player2 = ''

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None
def chooseLetter():
    global player1
    global player2
    player1 = input("Is player 1 X or O? ")
    player1 = player1.upper()
    while player1 != 'X' and player1 != 'O':
        print("That's not an option. ")
        print(" ")
        player1 = input("Is player 1 X or O? ")
        player1 = player1.upper()
    if player1 == "X" or player1 == "x":
        player2 = "O"
    else:
        player2 = "X"


#3b. (fun) Choose starting player 1 or 2
def chooseStart():
    global startPlayer
    global secondPlayer
    startPlayer = input("Who plays first?(X,O,Random)")
    startPlayer = startPlayer.upper()
    while startPlayer != 'X' and startPlayer != 'O' and startPlayer != 'RANDOM':
        print("That's not an option. ")
        print(" ")
        startPlayer = input("Who plays first?(X,O,Random)")
        secondPlayer = 0
        startPlayer = startPlayer.upper()

    if startPlayer == "X":
        secondPlayer = "O"

    if startPlayer == "O":
        secondPlayer = "X"

    if startPlayer == "RANDOM":
        x = random.randint(1, 2)
        if x == 1:
            startPlayer = "X"
            secondPlayer = "O"
            print("X plays first")
        elif x == 2:
            print("O plays first")
            startPlayer = "O"
            secondPlayer = "X"


#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none
def playerMove(board, player):
    print(" ")
    move = input("Where do you want to play? ")
    while move != '1' and move != '2' and move != '3' and move != '4' and move != '5' and move != '6' and move != '7' and move != '8' and move != '9':
        print("That's not an option. ")
        print(" ")
        move = input("Where do you want to play? ")

    move = int(move)
    if theBoard[move] == " ":
        theBoard[move] = player
    else:
        print("You can't play here. Try again. ")
        playerMove(board, player)
    print(" ")


#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
def checkWin(board, player):
    #Win in top row for Player
    rowT1 = (theBoard[7] == player and theBoard[8] == player
             and theBoard[9] == player)

    #Win in middle row for Player
    rowM1 = (theBoard[4] == player and theBoard[5] == player
             and theBoard[6] == player)

    #Win in bottom row for Player
    rowB1 = (theBoard[1] == player and theBoard[2] == player
             and theBoard[3] == player)

    #Win in left column for Player
    colL1 = (theBoard[7] == player and theBoard[4] == player
             and theBoard[1] == player)

    #Win in middle column for Player
    colM1 = (theBoard[8] == player and theBoard[5] == player
             and theBoard[2] == player)

    #Win in right column for Player
    colR1 = (theBoard[9] == player and theBoard[6] == player
             and theBoard[3] == player)

    #Win in top left diagonal for Player
    diaL1 = (theBoard[7] == player and theBoard[5] == player
             and theBoard[3] == player)

    #Win in top right diagonal for Player
    diaR1 = (theBoard[9] == player and theBoard[5] == player
             and theBoard[1] == player)

    if rowT1 or rowM1 or rowB1 or colL1 or colM1 or colR1 or diaL1 or diaR1:
        return True


#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise
def checkFull(board):
    if theBoard[1] != " " and theBoard[2] != " " and theBoard[
            3] != " " and theBoard[1] != " " and theBoard[
                4] != " " and theBoard[5] != " " and theBoard[
                    6] != " " and theBoard[7] != " " and theBoard[
                        8] != " " and theBoard[9] != " ":
        return True


#Welcome function
def welcome():
    print(" ")
    print("Welcome to Tic Tac Toe!")
    print(" ")
    play = input("Press enter to start. Type help for instructions. ")
    print(" ")
    print("-----------------------")
    play.lower()

    while play == "help":
        global theBoard
        print(
            "The main objective of this game is to get 3 in a row before your opponent. You will take turns playing in one of the 9 available space. These are the numbers that correspond to each space: "
        )
        theBoard = [
            " ",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]
        printBoard(theBoard)
        theBoard = [
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
        ]
        play = input("Would you like to play? Type help for instructions. ")


#7. Main function
def main():
    #Set up and first move
    welcome()
    chooseLetter()
    chooseStart()
    printBoard(theBoard)
    playerMove(theBoard, startPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, startPlayer):
        return startPlayer + " Wins"
    
    #Second move
    playerMove(theBoard, secondPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, secondPlayer):
        return secondPlayer + " Wins"

    #Third move
    playerMove(theBoard, startPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, startPlayer):
        return startPlayer + " Wins"

    #Fourth move
    playerMove(theBoard, secondPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, secondPlayer):
        return secondPlayer + " Wins"

    #Fifth move
    playerMove(theBoard, startPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, startPlayer):
        return startPlayer + " Wins"

    #Sixth move
    playerMove(theBoard, secondPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, secondPlayer):
        return secondPlayer + " Wins"
    if checkFull(theBoard):
        return "Draw"

    #Seventh move
    playerMove(theBoard, startPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, startPlayer):
        return startPlayer + " Wins"
    if checkFull(theBoard):
        return "Draw"

    #Eighth move
    playerMove(theBoard, secondPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, secondPlayer):
        return secondPlayer + " Wins"
    if checkFull(theBoard):
        return "Draw"

    #Ninth move
    playerMove(theBoard, startPlayer)
    printBoard(theBoard)
    if checkWin(theBoard, startPlayer):
        return startPlayer + " Wins"
    if checkFull(theBoard):
        return "Draw"


#Start function
def start():
  global theBoard
  startGame = input("Do you want to play Tic-Tac-Toe? ")
  startGame = startGame.lower()

  while startGame != 'yes' and startGame != 'no':
    print("That's not an option. Please say yes or no. ")
    print(" ")
    startGame = input("Do you want to play Tic-Tac-Toe? ")
    startGame = startGame.lower()

  while startGame.lower() == "yes":
    theBoard = [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ]
    main()
    startGame = input("Do you want to play again? ")
    while startGame != 'yes' and startGame != 'no':
        print("That's not an option. Please say yes or no. ")
        print(" ")
        startGame = input("Do you want to play again? ")
        startGame = startGame.lower()

  if startGame == 'no':
    print('Good Bye')

start()