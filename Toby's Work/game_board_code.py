class gameBoard:
    def __init__(self):
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.turn = 0

    def win_check(self):
        """Function to check if win condition reached"""
        for i in range(3):
            for j in range(3):
                # iterates through every section of the board
                section = self.board[i][j]
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
                                    next_section = self.board[i+k][j+l]
                                    if next_section == section:
                                        if next_section == self.board[i+k+k][j+l+l]:
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

    def minimax(self):
        selection = [None,None,None]
        temp_board = self.board
        for i in range(3):
            for j in range(3):
                if temp_board[i][j] == "-":
                    temp_board[i][j] = "X"
                    rating = self.heuristic(temp_board)
                    if selection[0] is None or rating > selection[0]:
                        selection = [rating, i, j]
                    else:
                        pass
                    temp_board[i][j] = "-"
                else:
                    pass
        return [selection[1],selection[2]]

    def heuristic(self, temp_board):
        rating = 0
        for i in range(3):
            for j in range(3):
                # iterates through every section of the board
                section = temp_board[i][j]
                if section == "-":
                    # we only need to check this later on (e.g. in ["O", "-", "O"] the "-" is important)
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
                                    next_section = temp_board[i+k][j+l]
                                    if next_section == section:
                                        if next_section == temp_board[i+k+k][j+l+l]:
                                            # Winning move; automatically return high rating
                                            if next_section == "X":
                                                return 1000
                                            else:
                                                pass
                                        elif next_section == "O" and temp_board[i+k+k][j+l+l] == "X":
                                            # Game-saving move; adjust rating significantly
                                            rating += 10
                                        else:
                                            # Two symbols were the same but the one after was not; potential win/loss
                                            if next_section == "X":
                                                # Good but not winning move; adjust rating minimally
                                                rating += 1
                                            else:
                                                # Winner will be "O"; adjust rating negatively significantly
                                                rating -= 10
                                    elif next_section == "-":
                                        if section == temp_board[i+k+k][j+l+l]:
                                            # Potential Win/Loss move, split symbols (e.g. ["O","-","O"]
                                            if section == "X":
                                                # Good but not winning move; adjust rating minimally
                                                rating += 1
                                            else:
                                                # Winner will be "O"; adjust rating negatively significantly
                                                rating -= 10
                                        else:
                                            pass
                                    elif section == "O" and next_section == "X":
                                        if section == temp_board[i+k+k][j+l+l]:
                                            # Game-saving move, adjust rating significantly
                                            rating += 10
                                        elif next_section == temp_board[i+k+k][j+l+l]:
                                            # Pointless move, adjust rating negatively
                                            rating -= 1
                                        else:
                                            # Placement is neither here nor there
                                            pass
                                    else:
                                        # The symbols are not the same so do not contribute to a complete line
                                        pass
                                except IndexError:
                                    # The index we passed was too large (looking for something outside the board
                                    pass
        return rating


game = gameBoard()
print(game.minimax())
