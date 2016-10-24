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
