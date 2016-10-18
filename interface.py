# This file contains the code for coding the interface we'll be using
# Imports the module we need (Tk-inter)
from tkinter import *
from tkinter import ttk
from tkinter import font

class Interface:
    def __init__(self):
        """Initiates the main menu screen and also sets the variables that will be used in the interface.
        If you are defining variables to be used across the interface, put them in here. Make sure the name
        starts with "self.", else the variable will not work.
        If it's just for 1 screen/function then just put it in the function you're using it in."""
        self.main_menu_screen = Tk()
        # Sets some default fonts for use in the program
        self.font_headings = font.Font(family="Helvetica", size=14)
        self.font_title = font.Font(family="Helvetica", size=32, weight="bold")
        self.font_text = font.Font(family="Helvetica", size=12)
        # Configures the style sheets we're going to use for our project (e.g. the style of the buttons)
        ttk.Style().configure(style="TButton", font=self.font_text)
        ttk.Style().configure(style="TFrame", background="White")
        ttk.Style().configure(style="TLabel", background="White")

    def main_menu(self):
        """This is the first thing we need to set up. We already have a window; include a frame, with a title of the project (TBC) We need 4 buttons that link to the functions local_game_player(), local_game_ai(), online_game() and online_chatroom()
        [This may change depending on how the network lessons pan out]. Make sure to put code before the self.mainmenu.mainloop()
        line else your code will not function. I've added some stuff to initialise the screen, but otherwise you'll be adding
        buttons and stuff."""
        self.main_menu_screen.title("TicTacToe - Main Menu")
        self.main_menu_screen.columnconfigure(0, weight=1)
        self.main_menu_screen.rowconfigure(0, weight=1)
        self.main_menu_screen["background"] = "White"
        self.main_menu_screen.mainloop()

    def local_game_player(self):
        game_player_screen = Toplevel()
        game_player_screen.title("TicTacToe - Local Game - 2 Player")
        game_player_screen.columnconfigure(0, weight=1)
        game_player_screen.rowconfigure(0, weight=1)
        game_player_screen["background"] = "White"
        game_player_screen.mainloop()

    def local_game_ai(self):
        game_ai_screen = Toplevel()
        game_ai_screen.title("TicTacToe - Local Game - 1 Player")
        game_ai_screen.columnconfigure(0, weight=1)
        game_ai_screen.rowconfigure(0, weight=1)
        game_ai_screen["background"] = "White"
        game_ai_screen.mainloop()

    def online_game(self):
        online_game_screen = Toplevel()
        online_game_screen.title("TicTacToe - Online - Game")
        online_game_screen.columnconfigure(0, weight=1)
        online_game_screen.rowconfigure(0, weight=1)
        online_game_screen["background"] = "White"
        online_game_screen.mainloop()

    def online_chatroom(self):
        online_chatroom_screen = Toplevel()
        online_chatroom_screen.title("TicTacToe - Online - Chatroom")
        online_chatroom_screen.columnconfigure(0, weight=1)
        online_chatroom_screen.rowconfigure(0, weight=1)
        online_chatroom_screen["background"] = "White"
        online_chatroom_screen.mainloop()

screen = Interface()
# If you want to test your code, type interface.<function_name>(arguments). Example below:
screen.main_menu()

    
