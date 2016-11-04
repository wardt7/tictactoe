#python tic tac toe game

    
gameboard = [0,1,2,3,4,5,6,7,8]                #make game board

playerOneTurn = True                           //
winner = False


def drawBoard(board):                      #display game board
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t","---------")
    print("\t",board[3], "|", board[4], "|", board[5])
    print("\t","---------")
    print("\t",board[6], "|", board[7], "|", board[8])
    print()

while not winner :
    drawBoard()

    if playerOneTurn :
        print "Player 1:"
    else :
        print "Player 2:"

    choice = int(input(">> "))

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

       for x in range (0, 3) :  #
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :  #
            winner = True
            drawBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        drawBoard()

print "Player " + str(int(playerOneTurn + 1)) + " wins!\n" #
