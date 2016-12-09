def show_instructions():
    """Loads the rules and instructions of the Tic Tac Toe game"""
    print("Hello and welcome to Tic Tac Toe")
    print("When you have started up a game, you will enter numbers 1-9")
    print("The numbers represent the squares of the Tic Tac Toe board")
    print("For example:")
    print("Entering the number 1 would represent the bottom left square")
    print("You keep making moves until there is a winner or a draw")
    print("Each players moves will be represented by X and O")
    print("You cannot make a move where there is a square taken by the other player")
    print("To win, you have to get you letter, X or O, three in a row in any direction")
    print("There will be a draw if the board is filled after 9 moves") 
    print("Have fun playing!")
       

def main_menu():
    """This loads up the main menu where players can choose what they would
    like to do"""
    menu_on = True
    while menu_on:
        print("Welcome to Tic Tac Toe")
        print("Choose an option you would like to do?")
        print("1 = Play a local game")
        print("2 = Play against the computer")
        print("3 = Exit")
        choice = input("Enter what you would like to do")
        if choice == "1":
            local_game()
        elif == "2":
            computer_game()
        elif choice == "3":
            print("Thanks for playing Tic Tac Toe")
            menu_on = False
        else:
            print("That wasn't a valid option, please choose again")
exit()
        
board = [["-","-","-"],["-","-","-"],["-","-","-"]]  

def local_game():
    """This starts a local game of two human players and the players keep playing
    until a winner is found or there is a draw"""
        game_on = True
        player_one = True
        while game_on:
            print(board[0])
            print(board[1])
            print(board[2])
            if player_one = True
                print("Player one, make your move")
            else:
                print("Player two, make your move")
            choice = input("Enter a number 1 to 9")
            if choice == "1":
                selection = board[2][0]
            elif choice = "2":
                selection = board[2][1]
            elif choice = "3":
                selection = board[2][2]
            elif choice = "4":
                selection = board[1][0]
            elif choice = "5":
                selection = board[1][1]
            elif choice = "6":
                selection = board[1][2]
            elif choice = "7":
                selection = board[0][0]
            elif choice = "8":
                selection = board[0][1]
            elif choice = "9":
                selection = board[0][2]
            else:
                print("That wasn't a valid selection")
                continue
            if selection == "-":
                if player_one:
                    letter = "O"
                else:
                    letter = "X"
                if choice == "1":
                    board[2][0] = letter
                elif choice == "2":
                    board[2][1] = letter
                elif choice == "3":
                    board[2][2] = letter
                elif choice == "4":
                    board[1][0] = letter
                elif choice == "5":
                    board[1][1] = letter
                elif choice == "6":
                    board[1][2] = letter
                elif choice == "7":
                    board[0][0] = letter
                elif choice == "8":
                    board[0][1] = letter
                else:
                    board[0][2] = letter
                win = win_check(board)
                if win != "-":
                    return print(win, "is the winner. Well done!")
                else:
                    turns += 1
                    if turns == 9:
                        return print("This game is a tie")
                    else:
                        player_one = not player_one
                        continue
                    
            else:
                print("That move is invalid, choose again")
                continue
            
def win_check(board):
    """Checks to see if there is any winner by seeing if the letters
    X or O have three in a row in any direction. If so, then a winner
    is declared"""
#check if there's a win on any vertical line
    if board[2][0] == "X" and board[1][0] == "X" and board[0][0] == "X":
        return True
    if board[2][0] == "O" and board[1][0] == "O" and board[0][0] == "O":
        return True
    if board[2][1] == "X" and board[1][1] == "X" and board[0][1] == "X":
        return True
    if board[2][1] == "O" and board[1][1] == "O" and board[0][1] == "O":
        return True
    if board[2][2] == "X" and board[1][2] == "X" and board[0][2] == "X":
        return True
    if board[2][2] == "O" and board[1][2] == "O" and board[0][2] == "O":
        return True
#check if there's a win on any horizontal line
    if board[2][0] == "X" and board[2][1] == "X" and board[2][1] == "X":
        return True
    if board[2][0] == "O" and board[2][1] == "O" and board[2][1] == "O":
        return True
    if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return True
    if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return True
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return True
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return True
#check if there's a win on any diagonal line
    if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        return True
    if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        return True
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return True
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return True

def computer_game():
    game_on = True
        human_player = True
        while game_on:
            print(board[0])
            print(board[1])
            print(board[2])
            if human_player = True
                print("Human player, make your move")
            else:
                print("The computer is making a move")
            choice = input("Enter a number 1 to 9")
            if choice == "1":
                selection = board[2][0]
            elif choice = "2":
                selection = board[2][1]
            elif choice = "3":
                selection = board[2][2]
            elif choice = "4":
                selection = board[1][0]
            elif choice = "5":
                selection = board[1][1]
            elif choice = "6":
                selection = board[1][2]
            elif choice = "7":
                selection = board[0][0]
            elif choice = "8":
                selection = board[0][1]
            elif choice = "9":
                selection = board[0][2]
            else:
                print("That wasn't a valid selection")
                continue
             if selection == "-":
                if human_player:
                    letter = "O"
                else:
                    letter = "X"
                if choice == "1":
                    board[2][0] = letter
                elif choice == "2":
                    board[2][1] = letter
                elif choice == "3":
                    board[2][2] = letter
                elif choice == "4":
                    board[1][0] = letter
                elif choice == "5":
                    board[1][1] = letter
                elif choice == "6":
                    board[1][2] = letter
                elif choice == "7":
                    board[0][0] = letter
                elif choice == "8":
                    board[0][1] = letter
                else:
                    board[0][2] = letter
                win = win_check(board)
                if win != "-":
                    return print(win, "is the winner!")
                else:
                    turns += 1
                    if turns == 9:
                        return print("This game is a tie")
                    else:
                        human_player = not human_player
                        
                        while human_player = not human_player:
    
                            if selection == "-":
                                AI_choice = board[2][0] or board[2][1] or board[2][2]
                                AI_choice = board[1][0] or board[1][1] or board[1][2]
                                AI_choice = board[0][0] or board[0][1] or board[0][2]
                            else:
                                None
                                continue
                                                
             else:
                print("That move is invalid, choose again")
                continue
            
                

                    
            
           
                
    

    
