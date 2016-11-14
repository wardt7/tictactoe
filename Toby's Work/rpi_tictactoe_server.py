# This file uses code obtained from https://github.com/covcom/ECU177_sockets, copyright Dr David Croft & Coventry University
import socket, pickle, select

class Chat:
    def __init__(self, port=12345):
        self.connections = []
        self.port = port

        self.server = socket.socket()         # Create a server socket
        self.server.bind(('', port))          # Bind to the port
        self.server.listen(5)                 # Now wait for client connections

        # self.master_dict is used to transfer variables and the data held in them between the client and the server.
        self.master_dict = {}
        # self.games holds all of the games that are currently in session. self.games[0] is a reserved slot for use as a chatroom.
        self.games = [[]]

    def shutdown(self):
        ''' shutdown the server '''

        for c in self.connections:
            c.close()

        self.server.shutdown(1)
        self.server.close()

    def poll(self):
        ''' see if there is anything for the server to do and do it. call poll() reguarly '''

        read, write, error = select.select( self.connections+[self.server], self.connections, self.connections, 0 )

        for conn in read:
            if conn is self.server:                 # new client connecting
                c, addr = conn.accept()
                self.connections.append(c)            # add to list of open self.connections

                print('Got connection from {}'.format(addr) )

            else:
                msgbytes = conn.recv(1024)

                if not msgbytes:                     # treat empty message as a disconnection
                    print('Disconnected')
                    conn.close()
                    self.connections.remove(conn)
                    # Then go through self.games and remove the connection from there.
                    for i in range(len(self.games)):
                        for j in self.games[i]:
                            if j == conn:
                                self.games[i].remove(conn)
                            else:
                                if i == 0:
                                    # Person disconnected from the chat room so no need to disconnect other people.
                                    # Alternatively, they were the only one in the game, so we don't have to tell
                                    # others to disconnect
                                    continue
                                # Tell the other connection in the game that the other player disconnected
                                self.master_dict["disconnected"] = True
                                self.send_data(j)
                                # Clean the dictionary so we don't accidentally send disconnects to other players
                                self.master_dict = {}
                                # We've removed the connection so we can stop looping.
                                break
                        


                else:
                    self.master_dict = pickle.loads(msgbytes)
                    if self.master_dict["game_no"] is None:
                        # Add the given connection to a game
                        game_no = self.connect_game(conn,1)
                        self.master_dict["game_no"] = game_no
                        if len(self.games[game_no]) == 2:
                            # The game is full, start the game
                            self.master_dict["player_turn"] = "X"
                            # Tell players their piece, then send them this with who's turn it is
                            for index in range(2):
                                # The player who's turn it isn't must receive their data first in order to maintain network
                                # synchronicity (otherwise the game will get "stuck").
                                if index == 0:
                                    self.master_dict["player_piece"] = "O"
                                else:
                                    self.master_dict["player_piece"] = "X"
                                self.send_data(self.games[game_no][index])
                                print("sent")
                    else:
                        # Connection is already in a game; take the obtained data and analyse it to see if someone has won
                        board = self.master_dict["board"]
                        win = self.win_check(board)
                        if win != "-" or self.master_dict["turns"] == 9:
                            # We have a final result (winner or draw). Send this to both clients.
                            self.master_dict["win"] = win
                            for index in range(2):
                                self.send_data(self.games[self.master_dict["game_no"]][index])
                                print("sent")
                        else:
                            if self.master_dict["player_turn"] == "X":
                                self.master_dict["player_turn"] = "O"
                            else:
                                self.master_dict["player_turn"] = "X"
                            self.master_dict["board"] = board
                            # If the client accidentally sends their player_piece we must remove it from the dictionary before sending it to
                            # both clients, otherwise they will have the same piece
                            self.master_dict.pop("player_piece",None)
                            for index in range(2):
                                self.send_data(self.games[self.master_dict["game_no"]][index])
                    # We clean the client's held dictionary in order to remove old data in the dictionary
                    self.master_dict = {}





    def connect_game(self, conn, index):
        """Function for adding a connection to a game. Has 2 parameters (and self); conn, which holds the connection we're trying add
        to the game; and index, the index we're looking at for this call of the function (the function is recursive). Returns
        the index of the game we added the connection to, which is the game no. we send to the client."""
        try:
            if len(self.games[index]) < 2:
            # Someone waiting for a game; add new player to game
                self.games[index].append(conn)
                return index
            else:
            # Move onto the next game location
                return self.connect_game(conn,index+1)
        except IndexError:
            # All game locations looked at, no spaces. Start a new game location
            self.games.append([conn])
            return index

    def send_data(self, conn):
        """Function for sending self.master_dict to the server. Has no parameters (except for self); outputs None at all times."""
        # Note that we use protocol 0 in order to guarantee compatibility (errors appeared when the server client was on linux). This
        # can be changed in order to message size, but would require both the client and server code altering to accomodate.
        msgbytes = pickle.dumps(self.master_dict, protocol=0)
        conn.send(msgbytes)

    def win_check(self, board):
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




                        

if __name__ ==p '__main__':
    # Initialise a server object
    c = Chat()

    try:
        print( "Server is running on port {}".format( c.port ) )

        while True:
            # Call the function for polling the client connections
            c.poll()

    except KeyboardInterrupt:
        pass

    finally:                                        # make certain everthing gets closed down properly
        print( "Shutdown" )
        c.shutdown()