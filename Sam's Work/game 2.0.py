import time
import random

"""main():The main function is responsible for running entire program,
allows me to restart the program when game is finished by calling main()"""
def main():
    alist = [1,2,3,4,5,6,7,8,9]

    """PrintBoard function allows me to display
    the board in 3x3 format using lists, icall each element of the list individually
    output: Board"""
    def printBoard( board ): 
                
        print ("   ",(alist[0]), '|', alist[1],'|', alist[2])
        print ("   ","-"*10)
        print ("   ",(alist[3]), '|', alist[4],'|', alist[5])
        print ("   ","-"*10)
        print ("   ",(alist[6]), '|', alist[7],'|', alist[8])
                
    print()

    print()

    """winner() check winning combinations for player vs player gamemode
    i did this using chained statements, triggers when certain spaces are all full such as 123.
    i made one for each player including the computer"""
    def winner ():
        global Win
        if alist [0] == player1 and alist[1] == player1 and alist[2] == player1:#top line horizontal
            Win = 'player1'
            return True
        elif alist[3] == player1 and alist[4] == player1 and alist[5] == player1:#middleline horizontal
            Win = 'player1'
            return True
        elif alist[6] == player1 and alist[7] == player1 and alist[8] == player1:#bottomline horizontal
            Win = 'player1'
            return True
        elif alist[0] == player1 and alist[4] == player1 and alist[8] == player1:#leftline vertical
            Win = 'player1'
            return True
        elif alist[2] == player1 and alist[4] == player1 and alist[6] == player1:#middlevertical
            Win = 'player1'
            return True
        elif alist[0] == player1 and alist[3] == player1 and alist[6] == player1:#rightvertical
            Win = 'player1'
            return True
        elif alist[1] == player1 and alist[4] == player1 and alist[7] == player1:##diagonal 
            Win = 'player1'
            return True
        elif alist[2] == player1 and alist[5] == player1 and alist[8] == player1:##diagonal
            Win = 'player1'
            return True
      



        if alist [0] == player2 and alist[1] == player2 and alist[2] == player2:
            Win = 'player2'
            return True
        elif alist[3] == player2 and alist[4] == player2 and alist[5] == player2:
            Win = 'player2'
            return True
        elif alist[6] == player2 and alist[7] == player2 and alist[8] == player2:
            Win = 'player2'
            return True
        elif alist[0] == player2 and alist[4] == player2 and alist[8] == player2:
            Win = 'player2'
            return True
        elif alist[2] == player2 and alist[4] == player2 and alist[6] == player2:
            Win = 'player2'
            return True
        elif alist[0] == player2 and alist[3] == player2 and alist[6] == player2:
            Win = 'player2'
            return True
        elif alist[1] == player2 and alist[4] == player2 and alist[7] == player2:
            Win = 'player2'
            return True
        elif alist[2] == player2 and alist[5] == player2 and alist[8] == player2:
            Win = 'player2'
            return True

        #Return False if no winner
        return False
        print("draw")

        

    """winner1()is the function that checks the winning combinations
    for player vs computer"""
    def winner1():
        global Win
        if alist [0] == Player1 and alist[1] == Player1 and alist[2] == Player1:#top line horizontal
            Win = 'player1'
            return True
        elif alist[3] == Player1 and alist[4] == Player1 and alist[5] == Player1:#middleline horizontal
            Win = 'player1'
            return True
        elif alist[6] == Player1 and alist[7] == Player1 and alist[8] == Player1:#bottomline horizontal
            Win = 'player1'
            return True
        elif alist[0] == Player1 and alist[4] == Player1 and alist[8] == Player1:#leftline vertical
            Win = 'player1'
            return True
        elif alist[2] == Player1 and alist[4] == Player1 and alist[6] == Player1:#middlevertical
            Win = 'player1'
            return True
        elif alist[0] == Player1 and alist[3] == Player1 and alist[6] == Player1:#rightvertical
            Win = 'player1'
            return True
        elif alist[1] == Player1 and alist[4] == Player1 and alist[7] == Player1:##diagonal 
            Win = 'player1'
            return True
        elif alist[2] == Player1 and alist[5] == Player1 and alist[8] == Player1:##diagonal
            Win = 'player1'
            return True


        if alist [0] == comp and alist[1] == comp and alist[2] == comp:#top line horizontal
            Win = 'Computer'
            return True
        elif alist[3] == comp and alist[4] == comp and alist[5] == comp:#middleline horizontal
            Win = 'Computer'
            return True
        elif alist[6] == comp and alist[7] == comp and alist[8] == comp:#bottomline horizontal
            Win = 'Computer'
            return True
        elif alist[0] == comp and alist[4] == comp and alist[8] == comp:#leftline vertical
            Win = 'Computer'
            return True
        elif alist[2] == comp and alist[4] == comp and alist[6] == comp:#middlevertical
            Win = 'Computer'
            return True
        elif alist[0] == comp and alist[3] == comp and alist[6] == comp:#rightvertical
            Win = 'Computer'
            return True
        elif alist[1] == comp and alist[4] == comp and alist[7] == comp:##diagonal 
            Win = 'Computer'
            return True
        elif alist[2] == comp and alist[5] == comp and alist[8] == comp:##diagonal
            Win = 'Computer'
            return True
        
    ##for player2
            
    """playerchoice1() is the code which checks the value entered and
    then determines where it goes on the board. for eexample if 1 is entered the function will check if the board is full
    play1 and play2 is defined as global variables in the player() function"""
    
    def playerchoice1():
        global taken
        taken = False

        if play1 == '1':
            if alist[0] == 'x' or alist[0]=='o':
                #print("taken")
                taken = True
                return taken
                player()
            else:
                alist[0] = player1
                printBoard(alist)

        if play1 == '2':
            if alist[1] == 'x' or alist[1] =='o':
                print("taken")
                player()
            else:
                alist[1] = player1
                printBoard( alist )

        if play1 == '3':
            if alist[2] == 'x' or alist[2] == 'o':
                print("taken")
                player()
            else:
                alist[2] = player1
                printBoard(alist)

        if play1 == '4':
            if alist[3] == 'x' or alist[3] == 'o':
                print("taken")
                player()
            else:
                alist[3] = player1
                printBoard( alist )

        if play1 == '5':
            if alist[4] == 'x' or alist[4] =='o':
                print("taken")
                player()
            else:
                alist[4] = player1
                printBoard( alist )                
        if play1 == '6':
            if alist[5] == 'x' or alist[5] == 'o':
                print("taken")
                player()
            else:
                alist[5] = player1
                printBoard( alist )
        if play1 == '7':
            if alist[6] == 'x' or alist[6] =='o':
                print("taken")
                player()
            else:
                alist[6] = player1
                printBoard( alist )
        if play1 == '8':
            if alist[7] == 'x' or alist[7] =='o':
                print("taken")
                player()
            else:
                alist[7] = player1
                printBoard( alist )
        if play1 == '9':
            if alist[8] == 'x' or alist[8] =='o':
                print("taken")
                player()
            else:
                alist[8] = player1
                printBoard( alist )  
    """playerchoice2 the same as playerchoice1 but for player2"""            
    def playerchoice2():

        if play2 == '1':
            if alist[0] == 'x' or alist[0] == 'o':
                print("taken")
                player()
            else:
                alist[0] = player2
                printBoard(alist)
        if play2 == '2':
            if alist[1] == 'x' or alist[1] == 'o':
                print("taken")
                player()
            else:
                alist[1] = player2
                printBoard( alist )
        if play2 == '3':
            if alist[2] == 'x' or alist[2] == 'o':
                print("taken")
                player()
            else:
                alist[2] = player2
                printBoard( alist )
        if play2 == '4':
            if alist[3] == 'x' or alist[3] =='o':
                print("taken")
                player()
            else:
                alist[3] = player2
                printBoard( alist )           
        if play2 == '5':
            if alist[4] == 'x' or alist[4] == 'o':
                print("taken")
                player()
            else:
                alist[4] = player2
                printBoard( alist )
        if play2 == '6':
            if alist[5] == 'x' or alist[5]=='o':
                print("taken")
                player()
            else:
                alist[5] = player2
                printBoard( alist )
        if play2 == '7':
            if alist[6] == 'x' or alist[6]=='o':
                print("taken")
                player()
            else:
                alist[6] = player2
                printBoard( alist )
        if play2 == '8':
            if alist[7] == 'x' or alist[7]=='o':
                print("taken")
                player()
            else:
                alist[7] = player2
                printBoard( alist )
        if play2 == '9':
            if alist[8] == 'x' or alist[8]=='o':
                print("taken")
                player()
            else:
                alist[8] = player2
                printBoard( alist )
                
    """player1choice() is the same as playerchoice1
    except its for player1 against the computer"""
    def player1choice():

        if Play1 == '1':
            if alist[0] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[0] = Player1
                printBoard(alist)
                
        if Play1 == '2':
            if alist[1] == 'x' or alist[1] =='o':
                print("taken")
                playervscomputer()
            else:
                alist[1] = Player1
                printBoard( alist )
                
        if Play1 == '3':
            if alist[2] == 'x' or alist[2] == 'o':
                print("taken")
                playervscomputer()
            else:
                alist[2] = Player1
                printBoard(alist)

        if Play1 == '4':
            if alist[3] == 'x' or alist[3] == 'o':
                print("taken")
                playervscomputer()
            else:
                alist[3] = Player1
                printBoard( alist )

        if Play1 == '5':
            if alist[4] == 'x' or alist[4] =='o':
                print("taken")
                playervscomputer()
            else:
                alist[4] = Player1
                printBoard( alist )
                
        if Play1 == '6':
            if alist[5] == 'x' or alist[5] == 'o':
                print("taken")
                playervscomputer()
            else:
                alist[5] = Player1
                printBoard( alist )

        if Play1 == '7':
            if alist[6] == 'x' or alist[6] =='o':
                print("taken")
                playervscomputer()
            else:
                alist[6] = Player1
                printBoard( alist )

        if Play1 == '8':
            if alist[7] == 'x' or alist[7] =='o':
                print("taken")
                playervscomputer()
            else:
                alist[7] = Player1
                printBoard( alist )
                
        if Play1 == '9':
            if alist[8] == 'x' or alist[8] =='o':
                print("taken")
                playervscomputer()
            else:
                alist[8] = Player1
                printBoard( alist )  

    """computer() is the code that will check if space is full
    when computer makes a choice"""
    def computer():
        if AI == '1':
            if alist[0] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[0] = comp
                printBoard(alist)


        if AI == '2':
            if alist[1] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[1] = comp
                printBoard(alist)

        if AI == '3':
            if alist[2] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[2] = comp
                printBoard(alist)

        if AI == '4':
            if alist[3] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[3] = comp
                printBoard(alist)

        if AI == '5':
            if alist[4] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[4] = comp
                printBoard(alist)


        if AI == '6':
            if alist[5] == 'x' or alist[0]=='o':
                print("taken")
            else:
                alist[5] = comp
                printBoard(alist)

        if AI == '7':
            if alist[6] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[6] = comp
                printBoard(alist)

        if AI == '8':
            if alist[7] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[7] = comp
                printBoard(alist)


        if AI == '9':
            if alist[8] == 'x' or alist[0]=='o':
                print("taken")
                playervscomputer()
            else:
                alist[8] = comp
                printBoard(alist)



    """player() function that includes a while loop that determines whos turn it is,
    wont stop until someone wins, also counts the scores
    also includes a restart statement when someone is a winner, so that another game can be played
    Input: would you like to play again? yes = main(), no = return """
    def player():
        global p1score
        p1score = 0
        global p2score
        p2score = 0
        players = [name, 'player2']
        global turn
        turn = random.randint(0,1)
        while True:
            if 'taken' == False:
                return
                    
            print('its\s %s\'s turn' % players[turn])
            if turn == 1:
                if turn == 'taken':
                    print("HEllo")
                else:
                    pass
                
            if winner():#Check if people have won
                if Win == 'player1':
                    print("player1 is winner")
                    p1score = p1score+1
                elif Win == 'player2':
                    print("player2 is winner")
                    p2score = p2score+1
                print('Player1s score =', p1score,'Player2s score =', p2score)
                print("Would you like to play again(yes or no)")
                restart = input("")
                if restart == 'yes':
                    return main() #If so exit this function
                else:
                    print("Thanks For Playing. :)")
                    return
                return
            time.sleep(1)
            turn +=1
            if turn >=2:
                turn = 0
            if turn == 0:
                global play2
                play2 = input("where would you like to move")
                playerchoice2()
            elif turn == 1:
                global play1
                play1 = input("where would you like to move")
                playerchoice1()  
            else:
                pass

    """playervscomputer() is the same as player() but instead with Computer as a player
    this includes the computers decisions which is a random int generator"""
    def playervscomputer():
        #gamerunning = False
        global Player1Score
        Player1Score = 0
        global ComputerScore
        ComputerScore = 0
        players = [name, 'computer']
        global turn
        turn = random.randint(0,1)
        while True:
            print('its\s %s\'s turn' % players[turn])
            if winner1():
                #Check if people have won
                if Win == 'player1':
                    #gamerunning = True
                    #if gamerunning == True:
                    print("player1 is winner")
                    Player1Score = Player1Score+1
                    print("player1s score is", Player1Score, 'Computer Score=', ComputerScore)
                    print("would you like to play again?(yes or no)")
                    restart = input("")
                    if restart =='yes':
                        return main()#####
                    else:
                        print("Thanks for playing")
                        return
                elif Win == 'Computer':
                    print("Computer is winner")
                    ComputerScore = ComputerScore+1
                print('Player1s score =', Player1Score,'Computers score =', ComputerScore)
                print("Would you like to play again(yes or no)")
                restart = input("")
                if restart == 'yes':
                    return main() #If so exit this function
                else:
                    print("Thanks For Playing. :)")
                    return #If so exit this function
            time.sleep(1)
            turn +=1
            if turn >=2:
                turn = 0
            if turn == 0:
                global AI
                AI = random.choice('123456789')
                print(AI)
                computer()
            elif turn == 1:
                global Play1
                Play1 = input("where would you like to move")
                player1choice()
            #elif winner == 'Player1':
                #print("endof game")
                #break   
            else:
                pass

      
    """
    XorOPlayer(): is afunction that allows the player to pick x or o
    also includes an error if player doesnt enter x or o
    input: X or O
    output: would you like to be x or o
    """
    def XorOPlayer():
        global player2
        global player1
        player1 = input("---|Would you like to be x or o|--: ")
        if player1 =='x':
            player1 = 'x'
            player2 = 'o'
        elif player1 == 'o':
            player2 = 'x'
        elif player1 != 'x' or player1 != 'o':
            print("Error: you have not entered x or o, try again")
            XorOPlayer()
        print("player 2 is", player2)

    """XorOAI() is the same as XorOPlayer but for the computer mode
    it will determine whos x or o.
    also includes an error if player doesnt enter x or o"""
    def XorOAI():
        global comp
        global Player1
        Player1 = input("---|Would you like to be x or o|--: ")
        if Player1 =='x':
            Player1 = 'x'
            comp = 'o'
        elif Player1 == 'o':
            comp = 'x'
        elif Player1 != 'x' or player1 != 'o':
            print("Error: you have not entered x or o, try again")
            XorOAI()
        print("Computer is", comp)
        #return playervscomputer()
        
    """gamemode() allows the user to pick how theyd like to play,
    along with a simple error message if the right way is not picked
    Input: 1 or 2, 1 = Singleplayer, 2 = twoplayer"""
    def gamemode():
        print ("So",name,"," "how would you like to play?")
        
        print("---|1. Singleplayer?(against computer)(type '1')")
        print("---|2. Twoplayers?(type '2')")
        gameChoice = input(": ")
        if gameChoice == '2':
            XorOPlayer()
            player()
        elif gameChoice == '1':
            XorOAI()
            playervscomputer()
        elif gameChoice != '1' or gameChoice !='2':
            print("Error: you have not entered 1 or 2")
            time.sleep(1)
            print("Try Again: (1 or 2)")
            time.sleep(1)
            gamemode()


    print("   ---|Welcome|---")
    time.sleep(0.5)
    print ("---|Noughts and Crosses|---")
    time.sleep(1)
    print ("---|A game created by Samuel Taiwo|---")
    global name
    name = input ("---|What is your name?|--: ")
    time.sleep(0.5)
    print("","This is what the board will display as.")
    printBoard( alist )
    time.sleep(1)
    print("You will enter a number between (1-9)" "\n"
          "This will determine where you would like your X or O to go.""\n")
    time.sleep(1)
    #print ("So,",name, "how would you like to play?")
    gamemode()
    
        


main()
