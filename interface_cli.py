def main_menu():
        menu_on = True
        while menu_on:
                print("Hello, welcome to the Tic Tac Toe game. What would you like to do?")
                print("A = play a local game")
                print("B = Exit")
                choice = input("Enter your choice")
                if choice == "A":
                        game_on = True
                        board = [["-","-","-"],["-","-","-"],["-","-","-"]]
                        player_one = True
                        while game_on:
                                print(board[0])
                                print(board[1])
                                print(board[2])
                                if player_one:
                                        print("Player one, make a move")
                                else:
                                        print("Player two, make a move")
                                choice = input("Enter a number from 1 to 9")
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
                                        pass
                                else:
                                        print("Invalid move, try again")
                                        continue
                                        
                elif choice == "B":
                        print("Thanks for playing")
                        menu_on = False
                else:
                        print("That was an invalid choice, try again")
        exit()
                        

def win_check(board):
        """Function to check if win condition reached"""
        for i in range(3):
            for j in range(3):
                # iterates through every section of the board
                section = board[i][j]
                if section == "-":
                    # we don't need to check a section if it is blank
                    pass
                else:
                    for k in [-1, 0, 1]:
                        for l in [-1, 0, 1]:
                            # iterate through all locations next to the location we previously found
                            if i+k < 0 or j+l < 0:
                                # We ignore negatives as these are outside the board
                                pass
                            elif k == 0 and l == 0:
                                # We create an exception to stop the use of the same position
                                pass
                            else:
                                try:
                                    next_section = board[i+k][j+l]
                                    if next_section == section:
                                        if next_section == board[i+k+k][j+l+l]:
                                            # Winner found; returns the symbol of the winner
                                            return section
                                        else:
                                            # Two symbols were the same but the one after was not
                                            pass
                                    else:
                                        # The symbols are not the same so do not contribute to a complete line
                                        pass
                                except IndexError:
                                    # The index we passed was too large (looking for something outside the board
                                    pass
        # No winner; dash returned
        return "-"
