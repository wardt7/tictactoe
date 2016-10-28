def main_menu():
        """Starts the main menu of the game; provides a way of calling individual functions for
        playing the game, and also handles some operations which don't require additional functions
        such as exiting the entire game. Has no arguments and always returns None"""
        menu_on = True
        while menu_on:
                print("Hello, welcome to the Tic Tac Toe game. What would you like to do?")
                print("A = play a local game")
                print("B = Exit")
                choice = input("Enter your choice\n")
                if choice == "A":
                        local_game_2_player()                        
                elif choice == "B":
                        print("Thanks for playing")
                        menu_on = False
                else:
                        print("That was an invalid choice, try again")
        exit()

def local_game_2_player():
        """Starts a local 2 player game of tic tac toe. The function should keep running
        until a winner is found or until 9 turns have elapsed (as after 9 turns there
        are no more moves available). Has no arguments and always returns None."""
        game_on = True
        board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        player_one = True
        turns = 0
        while game_on:
                print(board[0])
                print(board[1])
                print(board[2])
                if player_one:
                        print("Player one, make a move")
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
                                symbol = "X"
                        else:
                                symbol = "O"
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
                            if co_ord_y+offset_y < 0 or co_ord_x+offset_x < 0:
                                # We ignore negatives as these are outside the board
                                pass
                            elif offset_y == 0 and offset_x == 0:
                                # We create an exception to stop the use of the same position
                                pass
                            else:
                                try:
                                    next_section = board[co_ord_y+offset_y][co_ord_x+offset_x]
                                    if next_section == section:
                                        if co_ord_y+offset_y+offset_y < 0 or co_ord_x+offset_x+offset_x < 0:
                                                # We ignore negatives as these are outside the board
                                                pass
                                        elif section == board[co_ord_y+offset_y+offset_y][co_ord_x+offset_x+offset_x]:
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

main_menu()
