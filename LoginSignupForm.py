""" INSTRUCTIONS :-
1) If you are running the project for the first time on your system, then call the functions create() and LeaderboardCreate()
to create the required database for the project. This should create .db files in the repository same as this (.py) file is in.
After you have run these 2 functions for once comment the function calls as the required .db files have already been created.
Now you can run this .py file any number of times. The database files needs to created only once.

create() - 330
LeaderboardCreate() - 351

Note : Do remember to comment these two function calls after you have called them once. These functions are to be run for only once.

2) Change the value of turns variable according to your wish - turns variable(line no. - 34) defines how many turns are there in a single game.
"""

from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox
import random

sqlite3.paramstyle = 'named'

root = Tk()
root.title("Login/Signup Form")
root.geometry("400x400")
root.resizable(width=False, height=False)
lframe = LabelFrame(root, padx = 15, pady = 15, borderwidth=5)
sframe = LabelFrame(root, padx=15, pady=15, borderwidth=5)
USER = ""
UserGender = ""
userWin = 0
compWin = 0
counter = 0
turns = 5  # After how many turns the game will end
rHandButton = ''
pHandButton = ''
sHandButton = ''

