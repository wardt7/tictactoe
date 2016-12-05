# This file is based on a file called "lab_getting_select",
# obtained from https://github.com/covcom/ECU177_sockets, copyright Dr David Croft

# This file uses an external library named "PiGlow", which can be found at https://github.com/pimoroni/piglow.
# The code requires a PiGlow external module to run, which can be used upon request.
# Copyright Pimoroni Ltd

import socket, pickle, select
piglow = None
try:
    import piglow
    print("Connections are displayed in the top arm; chatroom connections are displayed in the right arm; number of games are displayed in the bottom arm")
    piglow_on = True
except ImportError:
    print("The PiGlow module is not installed on this machine")
    piglow_on = False
except OSError:
    print("The PiGlow module is not installed on this machine")
    piglow_on = False

class Chat:
    """
    This is a class for handling the server itself. It contains functions for:

        1. Initialising the server
        2. Adding and removing connections
        3. Polling all of the current connections to the server and seeing if anything needs to be done and taking
           appropriate action
        4. A win checking function to see if a player has won their game.
        5. Sending data to clients in an appropriate format.
        6. Controlling the "PiGlow" module on the raspberry pi
        7. Handling the shutdown of the server.

    All functions are object methods and as such all have the argument self; this argument will not be referred to
    in function docstrings

    Object Variables:
        self._connections
            Type: list
            This variable contains all of the connections to the server, regardless of why they have connected.
        self.__port
            Type: int
            This variable holds the port number to be used by the server's socket
        self._server
            Type: object
            Is a socket object; this opens up communication between the server and the client. Uses the port number
            held in self.__port
        self._master_dict
            Type: dict
            This variable is what we send to clients when we communicate with them. The keys are the variables
            we want to send to the target client; the values of the keys are the values held in the variables we
            want to send.
        self._games
            Type: list
            This holds lists of games that are currently being played at the moment (with each of those lists
            containing connections that are relevant to the game). NOTE: The first list (at index 0) is reserved
            for the chatroom, and should not be considered as a normal game.
        self._removals
            Type: list
            This holds all of the connections that are to be shut down; if a connection is being read and is found
            in the list, then it is shut down.

    """
    def __init__(self, port=12345):
        self._connections = []
        self.__port = port

        self._server = socket.socket()         # Create a server socket
        self._server.bind(('', self.__port))          # Bind to the port
        self._server.listen(5)                 # Now wait for client connections

        self._master_dict = {}
        self._games = [[]]
        self._removals = []

    def get_port(self):
        """
        Purpose: 
            Returns the port that is currently being used.

        Arguments: 
            None

        Returns: 
            self.__port

        """
        return self.__port

    def shutdown(self):
        '''
        Purpose:
            Shutdown the server socket.

        Arguments:
            None

        Modifies:
            self._server
                Tells the server to shutdown and close the connection
            self._connections
                Closes all of the connections in self._connections

        Returns:
            None 

         '''

        for c in self._connections:
            c.close()

        self._server.shutdown(1)
        self._server.close()

    def poll(self):
        ''' 
        Purpose:
            Poll the server's socket to see if there is anything to read, and act accordingly

        Arguments:
            None

        Modifies:
            self._connections
                Adds connections to it when a new client connects; removes connection when it disconnects
            self._games
                Adds and removes connections when they are in the chatroom. Also removes games from self._games when one of the players disconnects
            self._removals
                Adds connections to the list when a connection must be removed next time around (due to someone disconnecting from a game)
            self._master_dict
                Adds variables as keys and the value of the variables as the value of their respective keys. This is so that data can be sent to clients.

         '''

        read, write, error = select.select( self._connections+[self._server], self._connections, self._connections, 0 )

        for conn in read:
            if conn is self._server:                 # new client connecting
                c, addr = conn.accept()
                self._connections.append(c)            # add to list of open self._connections

                print('Got connection from {}'.format(addr) )

            elif conn in self._removals:
                # There is a connection to be closed in the removals list
                print("Disconnected")
                self._removals.remove(conn)
                self._connections.remove(conn)
                conn.close()

            else:
                try:
                    msgbytes = conn.recv(1024)
                except ConnectionResetError:
                    # The connection got reset so we immediately know it disconnected
                    msgbytes = False
                except OSError:
                    # We had a problem with the socket so we need to disconnect it
                    msgbytes = False

                if not msgbytes:                     # treat empty message as a disconnection
                    print('Disconnected')
                    for index in range(len(self._games)):
                        if conn in self._games[index]:
                            if index != 0:
                                # Obtain the game that has ended
                                new_remove = self._games[index]
                                # We set self._games[index] to [] as other games would start to search in the wrong game
                                self._games[index] = []
                                new_remove.remove(conn)
                                self._connections.remove(conn)
                                try:
                                    # We make sure that the other connection disconnects next time around
                                    self._removals.append(new_remove[0])
                                    self._master_dict["disconnected"] = True
                                    self.send_data(new_remove[0])
                                except IndexError:
                                    # There was only 1 person in the game so no-one else to remove
                                    pass
                                conn.close()
                                break
                    for user in self._games[0]:
                        if conn == user[0]:
                            # The connection is in the chatroom so we only remove that connection
                            self._games[0].remove(user)
                            self._connections.remove(conn)
                            break

                else:
                    self._master_dict = pickle.loads(msgbytes)
                    if self._master_dict["game_no"] is None:
                        # Add the given connection to a game
                        game_no = self.connect_game(conn,1)
                        self._master_dict["game_no"] = game_no
                        if len(self._games[game_no]) == 2:
                            # The game is full, start the game
                            self._master_dict["player_turn"] = "X"
                            # Tell players their piece, then send them this with who's turn it is
                            for index in range(2):
                                # The player who's turn it isn't must receive their data first in order to maintain network
                                # synchronicity (otherwise the game will get "stuck").
                                if index == 0:
                                    self._master_dict["player_piece"] = "O"
                                else:
                                    self._master_dict["player_piece"] = "X"
                                self.send_data(self._games[game_no][index])
                                print("sent")
                    elif self._master_dict["game_no"] == 0:
                        # The connection is related to the chatroom
                        if "username" in self._master_dict:
                            # A username has been set for the connection
                            for users in self._games[0]:
                                if users[1] == self._master_dict["username"]:
                                    # The username has been taken, send back a flag to say so.
                                    self._master_dict["flag"] = True
                                    self.send_data(conn)
                                    continue
                            self._games[0].append((conn,self._master_dict["username"]))
                        else:
                            # Get the username of the person who sent the message
                            username = None
                            for users in self._games[0]:
                                if conn in users:
                                    username = users[1]
                                    break
                            if username == None:
                                # We got a message from a connection that doesn't have a username
                                self._master_dict["flag"] = True
                                self.send_data(conn)
                                continue
                            # Send off the message received to other clients, adding the sender's username in the
                            # process.
                            msg = "{} said: {}".format(username,self._master_dict["message"])
                            self._master_dict["message"] = msg
                            for c in self._games[0]:
                                if c[0] != conn:
                                    self.send_data(c[0])


                    else:
                        # Connection is already in a game; take the obtained data and analyse it to see if someone has won
                        board = self._master_dict["board"]
                        win = self.win_check(board)
                        if win != "-" or self._master_dict["turns"] == 9:
                            # We have a final result (winner or draw). Send this to both clients.
                            self._master_dict["win"] = win
                            for index in range(2):
                                self.send_data(self._games[self._master_dict["game_no"]][index])
                                print("sent")
                        else:
                            if self._master_dict["player_turn"] == "X":
                                self._master_dict["player_turn"] = "O"
                            else:
                                self._master_dict["player_turn"] = "X"
                            self._master_dict["board"] = board
                            # If the client accidentally sends their player_piece we must remove it from the dictionary before sending it to
                            # both clients, otherwise they will have the same piece
                            self._master_dict.pop("player_piece",None)
                            for index in range(2):
                                self.send_data(self._games[self._master_dict["game_no"]][index])
                    # We clean the client's held dictionary in order to remove old data in the dictionary
                    self._master_dict = {}

    def connect_game(self, conn, index):
        """
        Purpose: 
            Connect a given client to a game

        Arguments:
            conn
                Type: tuple
                This is the connection we are trying to connect to a game
            index
                Type: int
                This is the index of the game we are looking at to see if there is a slot available

        Modifies:
            self._games
                The function adds the connection to a list in self._games.

        Returns:
            EITHER:
                The function, but with an incremented index
            OR:
                The index of the game we put the connection in.

        """
        try:
            if len(self._games[index]) < 2:
            # Someone waiting for a game; add new player to game
                self._games[index].append(conn)
                return index
            else:
            # Move onto the next game location
                return self.connect_game(conn,index+1)
        except IndexError:
            # All game locations looked at, no spaces. Start a new game location
            self._games.append([conn])
            return index


    def send_data(self, conn):
        """
        Purpose: 
            Send data to a client

        Arguments:
            conn
                Type: tuple
                This is the connection we want to send information to

        Modifies:
            Sends an encoded message to the connection

        Returns:
            None.

        """
        msgbytes = pickle.dumps(self._master_dict, protocol=0)
        try:
            conn.send(msgbytes)
        except OSError:
            # For some reason we couldn't send to the connection, remove it from our connections
            self._removals.append(conn)

    def win_check(self, board):
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

    def poll_piglow(self):
        """

        Purpose:
            Update the piglow module with new information. The piglow displays the amount of games, connections,
            and people in the chatroom as a 6 bit binary number.

        Arguments:
            None

        Modifies:
            The brightness of the LEDs on the PiGlow Module

        Returns:
            None

        """
        number_connections = len(self._connections)
        number_chatroom = len(self._games[0])
        number_games = 0
        # These lists contain the pins for representing the amount of connections, games and people in the chatroom
        # The first pin represents the most significant binary bit (2^5)
        connections_pinlist = [5,4,3,2,1,0]
        chatroom_pinlist = [11,10,9,8,7,6]
        games_pinlist = [17,16,15,14,13,12]
        for i in range(len(self._games)):
            # We look at all of the lists in self._games. If the list we're at isn't the chatroom and is currently
            # in play, we increase the amount of games there are.
            if i == 0:
                continue
            if len(self._games[i]) == 2:
                number_games += 1
        # Convert our decimal value to a binary string and remove the first 2 characters (As these just represent
        # that the string is a binary number)
        number_connections = bin(number_connections)[2:]
        number_chatroom = bin(number_chatroom)[2:]
        number_games = bin(number_games)[2:]
        # If any of our binary numbers have more than 6 bits, default to displaying the maximum number possible
        if len(number_connections) > 6:
            number_connections = "111111"
        if len(number_chatroom) > 6:
            number_chatroom = "111111"
        if len(number_games) > 6:
            number_games = "111111"
        # If there are less than 6 bits in the number then append 0s onto the front until we have 6 bits
        while len(number_connections) != 6:
            number_connections = "0"+number_connections
        while len(number_chatroom) != 6:
            number_chatroom = "0"+number_chatroom
        while len(number_games) != 6:
            number_games = "0"+number_games
        # Go through the binary numbers; if the number is a 1, turn on the pin that represents the 1 in the number
        for index in range(len(number_connections)):
            if number_connections[index] == "1":
                piglow.set(connections_pinlist[index],100)
            else:
                piglow.set(connections_pinlist[index],0)
        for index in range(len(number_chatroom)):
            if number_chatroom[index] == "1":
                piglow.set(chatroom_pinlist[index],100)
            else:
                piglow.set(chatroom_pinlist[index],0)
        for index in range(len(number_games)):
            if number_games[index] == "1":
                piglow.set(games_pinlist[index],100)
            else:
                piglow.set(games_pinlist[index],0)
        piglow.show()





                        

if __name__ == '__main__':
    # Initialise a server object
    c = Chat()

    try:
        print( "Server is running on port {}".format( c.get_port() ) )

        while True:
            # Call the function for polling the client connections
            c.poll()
            if piglow:
                # We try to update the piglow; if the physical module isn't actually installed then we get an IOError
                # exception; if so, don't poll the piglow in the future.
                try:
                    c.poll_piglow()
                except IOError:
                    print("The PiGlow module isn't seated properly; please reseat and restart the server.")
                    piglow = False

    except KeyboardInterrupt:
        pass

    finally:
        # Turn off the LEDs in the piglow if possible
        if piglow:
            try:
                piglow.set(0,0)
                piglow.show()
            except OSError:
                print("The PiGlow module isn't seated properly; please reseat and restart the server.")
                piglow_on = False
        # make certain everthing gets closed down properly
        print( "Shutdown" )
        c.shutdown()
        exit()