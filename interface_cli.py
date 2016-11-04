# This function is used in order to delay AI decisions in order to make them appear "human"
from time import sleep


def main_menu():
        """Starts the main menu of the game; provides a way of calling individual functions for
        playing the game, and also handles some operations which don't require additional functions
        such as exiting the entire game. Has no arguments and always returns None"""
        menu_on = True
        while menu_on:
                print("Hello, welcome to the Tic Tac Toe game. What would you like to do?")
                print("A = Play a local game")
                print("B = Play a game against an AI")
                print("C = Exit")
                choice = input("Enter your choice\n")
                if choice == "A":
                        local_game()
                elif choice == "B":
                        print("What difficulty would you like to play against?")
                        print("A = Hard")
                        print("B = Go back to the Main Menu")
                        choice = input("Enter your choice\n")
                        if choice == "A":
                                local_game(1)
                        else:
                                continue
                elif choice == "C":
                        print("Thanks for playing")
                        menu_on = False
                else:
                        print("That was an invalid choice, try again")
        exit()

def local_game(ai=None):
        """Starts a local 2 player game of tic tac toe. The function should keep running
        until a winner is found or until 9 turns have elapsed (as after 9 turns there
        are no more moves available). Has 1 parameter to determine if AI is used. Always returns None."""
        board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        player_one = True
        turns = 0
        show_instructions()
        # Asks the player (1) to select what piece they want to use, X or O
        if XorOPlayer():
                player_one_piece = "X"
                player_two_piece = "O"
        else:
                player_one_piece = "O"
                player_two_piece = "X"
        while True:
                print(board[0])
                print(board[1])
                print(board[2])
                if player_one:
                        print("Player one, make a move")
                else:
                        if ai == 1:
                                print("It's the AI's turn!")
                                sleep(2)
                                # Run the hard AI algorithm, place the AI piece and check if it has won
                                ai_selection = ai_hard(board, player_two_piece)
                                board[ai_selection[0]][ai_selection[1]] = player_two_piece
                                win = win_check(board)
                                if win != "-":
                                        return print("The AI is the winner! Game Over!")
                                else:
                                        turns += 1
                                        if turns == 9:
                                                print(board[0])
                                                print(board[1])
                                                print(board[2])
                                                return print("It's a draw!")
                                        else:
                                                player_one = not player_one
                                                continue
                        else:
                                print("Player two, make a move")
                choice = input("Enter a number from 1 to 9\n")
                # Obtains the symbol at the location selected to check for invalid moves
                if choice == "1":
                        selection = board[2][0]
                elif choice == "2":
                        selection = board[2][1]
                elif choice == "3":
                        selection = board[2][2]
                elif choice == "4":
                        selection = board[1][0]
                elif choice == "5":
                        selection = board[1][1]
                elif choice == "6":
                        selection = board[1][2]
                elif choice == "7":
                        selection = board[0][0]
                elif choice == "8":
                        selection = board[0][1]
                elif choice == "9":
                        selection = board[0][2]
                else:
                        print("That was invalid")
                        continue
                if selection == "-":
                        if player_one:
                                symbol = player_one_piece
                        else:
                                symbol = player_two_piece
                        # Changes the symbol at the selected location to the current player's token
                        if choice == "1":
                                board[2][0] = symbol
                        elif choice == "2":
                                board[2][1] = symbol
                        elif choice == "3":
                                board[2][2] = symbol
                        elif choice == "4":
                                board[1][0] = symbol
                        elif choice == "5":
                                board[1][1] = symbol
                        elif choice == "6":
                                board[1][2] = symbol
                        elif choice == "7":
                                board[0][0] = symbol
                        elif choice == "8":
                                board[0][1] = symbol
                        else:
                                board[0][2] = symbol
                        win = win_check(board)
                        if win != "-":
                                return print(win, "is the winner! Congratulations!")
                        else:
                                turns += 1
                                if turns == 9:
                                        return print("It's a draw!")
                                else:
                                        player_one = not player_one
                                        continue
                else:
                        print("Invalid move, try again")
                        continue



def win_check(board):
        """Function to check if win condition reached. Input: board (board is a list containing 3 lists
        each containing 3 elements. Each element is a "X", "O", or "-".). Output: "X", "O" (representing
        the winner, Crosses or Noughts respectively), "-" (representing no winner)"""
        for co_ord_y in range(3):
            for co_ord_x in range(3):
                # iterates through every section of the board
                section = board[co_ord_y][co_ord_x]
                if section == "-":
                    # we don't need to check a section if it is blank
                    pass
                else:
                    for offset_y in [-1, 0, 1]:
                        for offset_x in [-1, 0, 1]:
                            # iterate through all locations next to the location we previously found
                            if co_ord_y+offset_y < 0 or co_ord_x+offset_x < 0 or co_ord_y+offset_y+offset_y < 0 or co_ord_x+offset_x+offset_x < 0:
                                # We ignore negatives as these are outside the board
                                pass
                            elif offset_y == 0 and offset_x == 0:
                                # We create an exception to stop the use of the same position
                                pass
                            else:
                                try:
                                    next_section = board[co_ord_y+offset_y][co_ord_x+offset_x]
                                    if next_section == section:
                                        if section == board[co_ord_y+offset_y+offset_y][co_ord_x+offset_x+offset_x]:
                                            return section
                                        else:
                                            # Two symbols were the same but the one after was not
                                            pass
                                    else:
                                        # The symbols are not the same so do not contribute to a complete line
                                        pass
                                except IndexError:
                                    # The index we passed was too large (looking for something outside the board)
                                    pass
        return "-"

def ai_hard(board, ai_piece):
        """This function contains the code for the hardest AI in the game. I (Toby) originally got the idea from a Numberphile video explaining minimax.
        The function looks ahead to the next move at all of the possible moves available, and using a heuristic algorithm analyzes whether or not
        the move is good. Requires one input, board, which is the current game board. Outputs the location where the AI's move is to be placed."""
        # The first element in selection holds the rating of the current best move so that the current best move can be checked against other moves
        # during analysis. The second and third elements hold the Y and X co-ordinates respectively.
        selection = [None,None,None]
        for co_ord_y in range(3):
            for co_ord_x in range(3):
                # iterates through every section of the board
                if board[co_ord_y][co_ord_x] == "-":
                        # Change the space to the AI piece (X)
                        board[co_ord_y][co_ord_x] = ai_piece
                        # Run the heuristic algorithm; If selection is better or if there isn't a selection, then location becomes current selection
                        rating = ai_hard_heuristic(board, ai_piece)
                        if selection[0] is None or rating > selection[0]:
                            selection = [rating, co_ord_y, co_ord_x]
                        else:
                            pass
                        board[co_ord_y][co_ord_x] = "-"
                else:
                    pass
        return [selection[1],selection[2]]

def ai_hard_heuristic(board, ai_piece):
        """This function is the heuristic algorithm for ai_hard. It takes one input, board, which is an adjusted game board from the ai_hard function.
        The function outputs a rating (as an integer) for the given board."""
        rating = 0
        for co_ord_y in range(3):
            for co_ord_x in range(3):
                # iterates through every section of the board
                section = board[co_ord_y][co_ord_x]
                if section == "-":
                    # we only need to check this later on (e.g. in ["O", "-", "O"] the "-" is important)
                    pass
                else:
                    for offset_y in [-1, 0, 1]:
                        for offset_x in [-1, 0, 1]:
                            # iterate through all locations next to the location we previously found
                            if co_ord_y+offset_y < 0 or co_ord_x+offset_x < 0 or co_ord_y+offset_y+offset_y < 0 or co_ord_x+offset_x+offset_x < 0:
                                # We ignore negatives as these are outside the board
                                pass
                            elif offset_y == 0 and offset_x == 0:
                                # We create an exception to stop the use of the same position
                                pass
                            else:
                                try:
                                    next_section = board[co_ord_y+offset_y][co_ord_x+offset_x]
                                    if next_section == section:
                                        if next_section == board[co_ord_y+offset_y+offset_y][co_ord_x+offset_x+offset_x]:
                                            # Winning move; automatically return high rating
                                            if next_section == ai_piece:
                                                return 1000
                                            else:
                                                pass
                                        elif next_section != ai_piece and board[co_ord_y+offset_y+offset_y][co_ord_x+offset_x+offset_x] == ai_piece:
                                            # Game-saving move; adjust rating significantly
                                            rating += 10
                                        else:
                                            # Two symbols were the same but the one after was not; potential win/loss
                                            if next_section == ai_piece:
                                                # Good but not winning move; adjust rating minimally
                                                rating += 1
                                            else:
                                                # Winner will be "O"; adjust rating negatively significantly
                                                rating -= 10
                                    elif next_section == "-":
                                        if section == board[co_ord_y+offset_y+offset_y][co_ord_x+offset_x+offset_x]:
                                            # Potential Win/Loss move, split symbols (e.g. ["O","-","O"]
                                            if section == ai_piece:
                                                # Good but not winning move; adjust rating minimally
                                                rating += 1
                                            else:
                                                # Winner will be "O"; adjust rating negatively significantly
                                                rating -= 10
                                        else:
                                            pass
                                    elif section != ai_piece and next_section == ai_piece:
                                        if section == board[co_ord_y+offset_y+offset_y][co_ord_x+offset_x+offset_x]:
                                            # Game-saving move, adjust rating significantly
                                            rating += 10
                                        elif next_section == board[co_ord_y+offset_y+offset_y][co_ord_x+offset_x+offset_x]:
                                            # Pointless move, adjust rating negatively
                                            rating -= 1
                                        else:
                                            # Placement doesn't positively or negatively affect the game
                                            pass
                                    else:
                                        # The symbols are not the same so do not contribute to a complete line
                                        pass
                                except IndexError:
                                    # The index we passed was too large (looking for something outside the board
                                    pass
        # Return the final rating of the board
        return rating

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

def XorOPlayer():
        while True:
                player1 = input("---|Player 1/Human, would you like to be X or O|--: ")
                if player1 =='X':
                        return True
                elif player1 == 'O':
                        return False
                else:
                        print("That was an invalid input, try again.")
                
main_menu()
