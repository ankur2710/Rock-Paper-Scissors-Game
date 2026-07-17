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
#----------------Image set----------------
rHandPhoto = PhotoImage(file = 'rHand.png')
pHandPhoto = PhotoImage(file = 'pHand.png')
sHandPhoto = PhotoImage(file = 'sHand.png')
rock = Image.open("RockPaperScissorsImages/Rockimg.jpg")
rockImage = ImageTk.PhotoImage(rock)
paper = Image.open("RockPaperScissorsImages/Paperimg.jpg")
paperImage = ImageTk.PhotoImage(paper)
scissors = Image.open("RockPaperScissorsImages/Scissorsimg.jpg")
scissorImage = ImageTk.PhotoImage(scissors)
win = Image.open("RockPaperScissorsImages/YouWin.jpg")
winImage = ImageTk.PhotoImage(win)
lose = Image.open("RockPaperScissorsImages/YouLose.jpg")
loseImage = ImageTk.PhotoImage(lose)
tie = Image.open("RockPaperScissorsImages/YouTie.jpg")
tieImage = ImageTk.PhotoImage(tie)
#------------------------------------------
