# This function is used in order to delay AI decisions in order to make them appear "human"
from time import sleep
import pickle, socket, select


def main_menu():
        """
        Purpose:
            Operate the main menu of the program.

        Arguments:
            None.

        Returns:
            None.
        """
        menu_on = True
        while menu_on:
                print("Hello, welcome to the Tic Tac Toe game. What would you like to do?")
                print("A = Play a local game")
                print("B = Play a game against an AI")
                print("C = Play an online game")
                print("D = Join the online chat room")
                print("E = Exit")
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
                        game = Game()
                        game.online_game()
                elif choice == "D":
                        chat = Chat()
                        chat.online_chatroom()
                elif choice == "E":
                        print("Thanks for playing")
                        menu_on = False
                else:
                        print("That was an invalid choice, try again")
        exit()

def local_game(ai=None):
        """
        Purpose:
            Operate a game of tictactoe on the client. This is either a 2 player local game, or a 1 player game against an AI.

        Arguments:
            ai
                Type: int (sometimes None)
                Tells the program whether or not we're using an AI. If the value is None then no AI is used; if the value is 1
                then the hard AI is used.

        Returns:
            None.

        """
        board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        player_one = ai is None
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
        """

        Purpose: 
            See if someone has won a game of tictactoe when given a board

        Arguments:
            board
                Type: list
                This contains a specifically formatted list that represents the game board.
                A valid value of this would be [["-","X","O"],["-","X","O"],["-","X","O"]]
                The string "-" represents a blank space while "X" and "O" represent board pieces.
                Note that the value of board[2][0] represents the bottom left corner.
                Likewise, the value of board[0][2] represents the top right corner.

        Returns:
            One of the following:
                "-" if there is no winner
                "X" if X is the winner
                "O" if O is the winner

        """
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
        """
        Purpose:
            A function for operating a hard AI. The algorithm is loosely based on "MiniMax" with heuristic analysis.

        Arguments:
            board
                Type: list
                This contains a specifically formatted list that represents the game board.
                A valid value of this would be [["-","X","O"],["-","X","O"],["-","X","O"]]
                The string "-" represents a blank space while "X" and "O" represent board pieces.
                Note that the value of board[2][0] represents the bottom left corner.
                Likewise, the value of board[0][2] represents the top right corner.
            ai_piece
                Type: string (char)
                This is a single character which represents the piece that the ai is using. Should either
                be "X" or "O"

        Returns:
            A tuple, holding the location of where the AI wants to place its piece. The first element is the Y co-ord, the second element the X co-ord

        """
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
        return (selection[1],selection[2])

def ai_hard_heuristic(board, ai_piece):
        """
        Purpose:
            For a given game board, analyse how good the move the ai made was

        Arguments:
            board
                Type: list
                This contains a specifically formatted list that represents the game board.
                A valid value of this would be [["-","X","O"],["-","X","O"],["-","X","O"]]
                The string "-" represents a blank space while "X" and "O" represent board pieces.
                Note that the value of board[2][0] represents the bottom left corner.
                Likewise, the value of board[0][2] represents the top right corner.
            ai_piece
                Type: string (char)
                This is a single character which represents the piece that the ai is using. Should either
                be "X" or "O"

        Returns:
            The "rating" of a board. Always an integer number

        """
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
    """
    Purpose:
        Show instructions for how to play Tic Tac Toe

    Arguments:
        None

    Returns:
        None

    """
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
    """
    Purpose:
        Ask a player whether or not they want to play as "X" or as "O"

    Arguments:
        None

    Returns:
        EITHER:
            True if player 1 wants to use X
        OR: 
            False if player 1 wants to use O
    """
    while True:
        player1 = input("---|Player 1/Human, would you like to be X or O|--: ")
        if player1 =='X':
                return True
        elif player1 == 'O':
                return False
        else:
                print("That was an invalid input, try again.")

# The following code is based off a file called "lab_getting_started_client.py",
# which is available at https://github.com/covcom/ECU177_sockets
class Client:
    """
    This is a class for handling the users connection to the server. It contains functions for:

        1. Sending data to the server via a pickled dictionary
        2. Receiving and decoding a pickled dictionary, and unpackig the data so that variables are loaded with new data
        3. Ending the connection with the server cleanly

    All functions are object methods and as such all have the argument self; this argument will not be referred to
    in function docstrings

    Object Variables:
        self.__port
            Type: int
            This variable holds the port number to be used by the server's socket
        self.__c
            Type: object
            Is a socket object; this opens up communication between the client and the server. Uses the port number
            held in self.__port
        self.__master_dict
            Type: dict
            This variable is what we send to the server when we communicate with it. The keys are the variables
            we want to send to the target server; the values of the keys are the values held in the variables we
            want to send.
        self.__flag
            Type: bool (sometimes None)
            This variable can be used as a warning signal from the server; whilst it is currently used only in the subclass
            Chat for alerting us when a username has been taken, it is intended for wider spread use in the future (for example,
            when validity checks are transferred from the client to the server, it will be used there to alert the client of an
            invalid move.)

    Note that this code is based on a file called "lab_getting_started_client.py", authored by Dr. David Croft. Available at
    https://github.com/covcom/ECU177_sockets


    """
    def __init__(self):
        self.__port = 12345
        self.__c = socket.socket()
        self.__c.connect(("10.0.87.77",self.__port))
        self.__master_dict = {}
        self.__flag = None


    def recv_data(self):
        """
        Purpose:
            Receive data from the server and unpack it into a given set of variables

        Arguments:
            None

        Modifies:
            self.__board, self.__player_turn, self.__game_no, self.__turns, self.__player_piece,self.__win, self.__disconnected, self.__message, self.__flag
                If one of these variables is in self.__master_dict, then we load the respective data into the variable

        Returns:
            True if we successfully receive and unpack data

            False if we have lost the connection to the server

            None if we receive a blocking error (i.e. nothing to read but not because of a disconnection)

        """
        self.__master_dict = {}
        try:
            raw_recv = self.__c.recv(1024)
        except ConnectionAbortedError:
            return False
        except ConnectionResetError:
            return False
        except BlockingIOError:
            return None
        if not raw_recv:
            return False
        else:
            # Decode the received message to obtain a dictionary; load the values into their respective variables
            self.__master_dict = pickle.loads(raw_recv)
            if "board" in self.__master_dict:
                self.__board = self.__master_dict["board"]
            if "player_turn" in self.__master_dict:
                self.__player_turn = self.__master_dict["player_turn"]
            if "game_no" in self.__master_dict:
                self.__game_no = self.__master_dict["game_no"]
            if "turns" in self.__master_dict:
                self.__turns = self.__master_dict["turns"]
            if "player_piece" in self.__master_dict:
                self.__player_piece = self.__master_dict["player_piece"]
            if "win" in self.__master_dict:
                self.__win = self.__master_dict["win"]
            if "disconnected" in self.__master_dict:
                self.__disconnected = self.__master_dict["disconnected"]
            if "message" in self.__master_dict:
                self.__message = self.__master_dict["message"]
            if "flag" in self.__master_dict:
                self.__flag = self.__master_dict["flag"]
            return True

    def send_data(self):
        """
        Purpose:
            Encode self.__master_dict and send it to the server for processing.

        Arguments:
            None

        Returns:
            None
        """
        msgbytes = pickle.dumps(self.__master_dict, protocol=0)
        try:
            self.__c.send(msgbytes)
        except ConnectionAbortedError:
            return
        except ConnectionResetError:
            return

    def end_connection(self):
        """
        Purpose:
            Run the functions for shutting down the connection between the client and the server
            
        Arguments:
            None

        Modifies:
            self.__c
                Ends the connection between the client and the server

        Returns:
            None
        """
        self.__c.shutdown(1)
        self.__c.close()



class Game(Client):
    """
    This is a class specifically designed for running an online game between this client and another client via a server. It is a subclass of Client. It contains functions for:

        1. Running the online game loop.

    All functions are object methods and as such all have the argument self; this argument will not be referred to
    in function docstrings

    Object Arguments:
        self.__board
            Type: list
            This contains a specifically formatted list that represents the game board.
            A valid value of this would be [["-","X","O"],["-","X","O"],["-","X","O"]]
            The string "-" represents a blank space while "X" and "O" represent board pieces.
            Note that the value of board[2][0] represents the bottom left corner.
            Likewise, the value of board[0][2] represents the top right corner.

        self.__player_turn
            Type: string (char), sometimes None
            This contains a single character ("X" or "O") that represents who's turn it is to make a move

        self.__player_piece
            Type: string (char), sometimes None
            This contains a single character ("X" or "O") which is this client's playing piece

        self.__game_no
            Type: int, sometimes None
            This contains the number of the game which the client is in. It is always sent in the master_dictionary when communicating with the server

        self.__win
            Type: String (char), sometimes None
            This contains a string which represents the winner when the winner is found. Is "X" or "O" when X or O have won respectively, or "-" when it is
            a draw
        
        self.__disconnected
            Type: bool
            Is True when the client has disconnected from the server.



    """
    def __init__(self):
        Client.__init__(self)
        self.__board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.__player_turn = None
        self.__player_piece = None
        self.__game_no = None
        self.__win = None
        self.__turns = 0
        self.__disconnected = False

    def online_game(self):
        """
        Purpose:
            Play a game of tic-tac-toe with another computer via a server by sending and receiving data in the form of an encoded dictionary

        Arguments:
            None

        Modifies:
            self.__board
                The state of this list changes when a player makes a move.

            self.__player_turn
                Changes when it is the other player's turn to make a move

            self.__game_no
                Changes when connecting to the game that the client has been put in

            self.__player_piece
                Changes when connecting to the board piece that has been assigned to it by the server

            self.__win
                Changes when a winner has been found

            self.__turns
                Increments by 1 after each turn

            self.__disconnected
                Becomes True when the client has disconnected unexpectedly from the server

        Returns:
            None (although print statements are run when returning)

        """
        print("Connecting you to a random online game")
        # The value of self.__game_no is None; the server recognises this as a request to join a game, and allocates a game to the connection
        self.__master_dict["game_no"] = self.__game_no
        self.send_data()
        while True:
            # Obtain the latest data from the server at the start of each loop, then display the new board to the user
            result = self.recv_data()
            print("You are in game: {}. Your piece is: {}".format(self.__game_no, self.__player_piece))
            print(self.__board[0])
            print(self.__board[1])
            print(self.__board[2])
            if result == False or self.__disconnected:
                # Note: result == False is True when the server disconnects; self.__disconnected is True when the opponent disconnects
                self.end_connection()
                return print("You or your opponent disconnected from the server. Returning you to the main menu")
            elif self.__win is not None:
                # A final result has been determined, end the game
                self.end_connection()
                if self.__win != "-":
                    return print("{} is the winner! Returning you to the main menu.".format(self.__win))
                else:
                    return print("It's a draw! Returning you to the main menu.")
            elif self.__player_turn != self.__player_piece:
                print("It's the other player's turn!")
            else:
                print("It's your turn!")
                selecting = True
                while selecting:
                    choice = input("Enter a number between 1 and 9.\n")
                    if choice == "1":
                            selection = self.__board[2][0]
                    elif choice == "2":
                            selection = self.__board[2][1]
                    elif choice == "3":
                            selection = self.__board[2][2]
                    elif choice == "4":
                            selection = self.__board[1][0]
                    elif choice == "5":
                            selection = self.__board[1][1]
                    elif choice == "6":
                            selection = self.__board[1][2]
                    elif choice == "7":
                            selection = self.__board[0][0]
                    elif choice == "8":
                            selection = self.__board[0][1]
                    elif choice == "9":
                            selection = self.__board[0][2]
                    else:
                            print("That was invalid")
                            continue
                    if selection == "-":
                        if choice == "1":
                                self.__board[2][0] = self.__player_piece
                        elif choice == "2":
                                self.__board[2][1] = self.__player_piece
                        elif choice == "3":
                                self.__board[2][2] = self.__player_piece
                        elif choice == "4":
                                self.__board[1][0] = self.__player_piece
                        elif choice == "5":
                                self.__board[1][1] = self.__player_piece
                        elif choice == "6":
                                self.__board[1][2] = self.__player_piece
                        elif choice == "7":
                                self.__board[0][0] = self.__player_piece
                        elif choice == "8":
                                self.__board[0][1] = self.__player_piece
                        else:
                                self.__board[0][2] = self.__player_piece
                        selecting = False
                    else:
                            print("Invalid move, try again")
                            continue
                # Load in the newly adjusted variables into the master dictionary and send to the server
                self.__master_dict["board"] = self.__board
                self.__master_dict["game_no"] = self.__game_no
                self.__master_dict["player_turn"] = self.__player_turn
                self.__master_dict["turns"] = self.__turns+1
                self.send_data()
                continue


class Chat(Client):
    """
    This class is used to connect and manage a connection to the chatroom run by a server. It is a subclass of Client. It has functions for:

        1. Setting the client's username
        2. Running the connection to the chatroom

    All functions are object methods and as such all have the argument self; this argument will not be referred to
    in function docstrings

    Object Variables include:
        self.__game_no
            Type: int (constant)
            Is always 0; indicates to the server that the client is in the chat room.
    """
    def __init__(self):
        Client.__init__(self)
        self.__game_no = 0

    def set_username(self):
        """
        Purpose:
            Set the username of the client and send this information to the server

        Arguments:
            None

        Returns:
            None
        """
        username = input("What would you like your username to be?\n")
        self.__master_dict["username"] = username
        self.__master_dict["game_no"] = self.__game_no
        self.send_data()

    # This code is based off of the "solved_server.py" file provided by Dr. David Croft. This can be found at
    # https://github.com/covcom/ECU177_sockets
    def online_chatroom(self):
        """
        Purpose:
            Manage the general running of the chatroom

        Arguments:
            None

        Returns:
            None

        This code is based off of the "solved_server.py" file provided by Dr. David Croft. This can be found at
        https://github.com/covcom/ECU177_sockets  # This code is based off of the "solved_server.py" file provided by Dr. David Croft. This can be found at
        https://github.com/covcom/ECU177_sockets
        """
        # Set the socket so that when there is nothing to read we get a blocking error
        self.__c.setblocking(0)
        self.set_username()
        self.__master_dict = {}
        try:
            while True:
                read, write, error = select.select([self.__c],[self.__c],[self.__c])
                if read != []:
                    # We have something to read, obtain that data and handle it.
                    recv = self.recv_data()
                    if not recv:
                        print("Connection to the host was lost. Returning you to the main menu")
                        raise KeyboardInterrupt
                    elif recv is None:
                        pass
                    elif self.__flag:
                        print("You've used a username that's already been taken. Try again")
                        self.set_username()
                    else:
                        print(self.__master_dict["message"])
                    self.__master_dict = {}
                    continue
                if write != []:
                    # We can write to the server, allow the user to input something if they want to and send it if they have inputted something
                    msg = input(">")
                    if msg == "\exit":
                        # The user wishes to end the connection with the server
                        print("Taking you back to the main menu")
                        raise KeyboardInterrupt
                    elif len(msg) != 0:
                        self.__master_dict["message"] = msg
                        self.__master_dict["game_no"] = self.__game_no
                        self.send_data()
                    else:
                        pass

        except KeyboardInterrupt:
            pass
        finally:
            self.end_connection()



main_menu()
