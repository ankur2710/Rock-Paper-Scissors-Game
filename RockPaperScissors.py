from tkinter import *
from PIL import Image, ImageTk
import random
import sqlite3
root = Tk()
root.title('Rock Paper Scissors Game')
root.resizable(width=False, height=False)
click = True
userWin = 0
compWin = 0
counter = 0
turns = 5
