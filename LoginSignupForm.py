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

#------------------------------------------

# Function creating the whole ROCK-PAPER-SCISSORS Game
def play():
    global rHandButton, pHandButton, sHandButton, userWin, compWin, Scoreboard, resetButton, rockLabel, paperLabel, scissorLabel, buttonHolder, LeaderBoardBtn
    rockLabel = Label(root, text='Rock', bg='#238f02', fg='white', width=35, padx=10, pady=10)
    paperLabel = Label(root, text='Paper', bg='#de9a03', fg='white', width=35, padx=10, pady=10)
    scissorLabel = Label(root, text='Scissors', bg='#c20c0c', fg='white', width=35, padx=10, pady=10)
    rockLabel.grid(row=0, column=0, padx=5, pady=7)
    paperLabel.grid(row=0, column=1, padx=5, pady=5)
    scissorLabel.grid(row=0, column=2, padx=5, pady=5)
    rHandButton = Button(root, image=rHandPhoto, command=lambda: youPick('rock'))
    pHandButton = Button(root, image=pHandPhoto, command=lambda: youPick('paper'))
    sHandButton = Button(root, image=sHandPhoto, command=lambda: youPick('scissors'))
    rHandButton.grid(row=1, column=0)
    pHandButton.grid(row=1, column=1)
    sHandButton.grid(row=1, column=2)
    Scoreboard = Label(root, text="SCORE \n\n    " + USER.upper() + " - " + str(userWin) + "\t\tCOMPUTER - " + str(compWin), bg='blue',
                       fg='white', padx=10, pady=20)
    Scoreboard.config(font=("Times", 15))
    Scoreboard.grid(row=2, column=0, columnspan=2, sticky=W + E, padx=10, pady=10)
    buttonHolder = Frame(root)
    buttonHolder.grid(row=2, column=2)
    resetButton = Button(buttonHolder, text='RESET', fg='white', command=lambda: reset_frame(), bg='green', width=30,
                         pady=10)
    resetButton.pack(pady=5)
    LeaderBoardBtn = Button(buttonHolder, text='Leader Board', fg='white', command=lambda: getLeaderboard(), bg='black',
                            width=30, pady=10)
    LeaderBoardBtn.pack(pady=5)

# Computer randomly picks a choice
def computerPick():
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

# Function to play the game again after it is finished once
def playAgain():
    global counter, userWin, compWin, rHandButton, pHandButton, sHandButton
    counter = 0
    userWin = 0
    compWin = 0
    # top.quit()
    start()
    return

# Function containing the whole logic of won-lose-tie in the game. Decision maker :)
def youPick(yourChoice):
    global click, userWin, compWin, Scoreboard, rockImage, tieImage, paperImage, loseImage, scissorImage, winImage, compPick, rockLabel, paperLabel, scissorLabel, counter, turns, top
    compPick = computerPick()
    if click:
        counter += 1
        if yourChoice == 'rock':
            rHandButton.configure(image=rockImage)
            rockLabel.configure(text='Rock')
            if compPick == 'rock':
                pHandButton.configure(image=rockImage)
                sHandButton.configure(image=tieImage)
                paperLabel.configure(text='Rock')
                scissorLabel.configure(text='Tie')
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image=paperImage)
                sHandButton.configure(image=loseImage)
                paperLabel.configure(text='Paper')
                scissorLabel.configure(text='Lose')
                compWin += 1
                click = False
            else:
                pHandButton.configure(image=scissorImage)
                sHandButton.configure(image=winImage)
                paperLabel.configure(text='Scissors')
                scissorLabel.configure(text='Win')
                userWin += 1
                click = False
        elif yourChoice == 'paper':
            rHandButton.configure(image=paperImage)
            rockLabel.configure(text='Paper')
            if compPick == 'rock':
                pHandButton.configure(image=rockImage)
                sHandButton.configure(image=winImage)
                paperLabel.configure(text='Rock')
                scissorLabel.configure(text='Win')
                userWin += 1
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image=paperImage)
                sHandButton.configure(image=tieImage)
                paperLabel.configure(text='Paper')
                scissorLabel.configure(text='Tie')
                click = False
            else:
                pHandButton.configure(image=scissorImage)
                sHandButton.configure(image=loseImage)
                paperLabel.configure(text='Scissors')
                scissorLabel.configure(text='Lose')
                compWin += 1
                click = False
        else:
            rHandButton.configure(image=scissorImage)
            rockLabel.configure(text='Scissors')
            if compPick == 'rock':
                pHandButton.configure(image=rockImage)
                sHandButton.configure(image=loseImage)
                paperLabel.configure(text='Rock')
                scissorLabel.configure(text='Lose')
                compWin += 1
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image=paperImage)
                sHandButton.configure(image=winImage)
                paperLabel.configure(text='Paper')
                scissorLabel.configure(text='Win')
                userWin += 1
                click = False
            else:
                pHandButton.configure(image=scissorImage)
                sHandButton.configure(image=tieImage)
                paperLabel.configure(text='Scissors')
                scissorLabel.configure(text='Tie')
                click = False
    else:
        if yourChoice == 'rock' or yourChoice == 'paper' or yourChoice == 'scissors':
            rHandButton.configure(image=rHandPhoto)
            pHandButton.configure(image=pHandPhoto)
            sHandButton.configure(image=sHandPhoto)
            rockLabel.configure(text='Rock')
            paperLabel.configure(text='Paper')
            scissorLabel.configure(text='Scissors')
            click = True

    Scoreboard = Label(root, text="SCORE \n\n    "+ USER.upper() +" - " + str(userWin) + "\t\tCOMPUTER - " + str(compWin), bg='blue',
                       fg='white', padx=10, pady=20)
    Scoreboard.config(font=("Times", 15))
    Scoreboard.grid(row=2, column=0, columnspan=2, sticky=W + E, padx=10, pady=10)
    if counter == turns:
        message = ''
        if userWin > compWin:
            message = 'You Won!!'
        elif userWin < compWin:
            message = 'You Lose!!'
        else:
            message = 'You Tied!!'
        insertToLeaderBoard()
        top = Toplevel()
        top.title("Result")
        top.geometry('300x300')
        confetiImg = PhotoImage(file="RockPaperScissorsImages/confeti.gif")
        confetiLabel = Label(top, image=confetiImg)
        confetiLabel.image = confetiImg
        confetiLabel.grid(row=0, column=0)
        messageFrame = Frame(top)
        messageFrame.grid(row=0, column=0)
        message = Label(messageFrame, text=message)
        message.config(font=("Times", 30, 'bold'))
        message.pack()
        exitButton = Button(messageFrame, text="Exit", bg='red', fg='white', width=10, padx=3, pady=3,
                            command=root.quit)
        exitButton.config(font=("Times", 12))
        exitButton.pack(pady=3, padx=3)
        rHandButton.configure(state="disabled")
        pHandButton.configure(state="disabled")
        sHandButton.configure(state="disabled")
        playAgainBtn = Button(messageFrame, text="PlayAgain", bg='#8953ff', fg='white', width=10, padx=3, pady=3,
                            command=playAgain)
        playAgainBtn.config(font=("Times", 12))
        playAgainBtn.pack(pady=3, padx=3)



# Reseting the frame to original starting pictures
def reset_frame():
    global click
    rHandButton.configure(image=rHandPhoto)
    pHandButton.configure(image=pHandPhoto)
    sHandButton.configure(image=sHandPhoto)
    click = True

click = ''

# Function creating the GAME window, reading the images
def start():
    global root, click, rHandPhoto, pHandPhoto, sHandPhoto, userWin, compWin, rockImage, paperImage, scissorImage, loseImage, winImage, tieImage
    root.destroy()
    root = Tk()
    root.title('Rock Paper Scissors Game')
    root.resizable(width=False, height=False)
    click = True
    userWin = 0
    compWin = 0

    # ----------------Image set----------------
    rHandPhoto = PhotoImage(file='RockPaperScissorsImages/rHand.png')
    pHandPhoto = PhotoImage(file='RockPaperScissorsImages/pHand.png')
    sHandPhoto = PhotoImage(file='RockPaperScissorsImages/sHand.png')
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

    # ------------------------------------------
    play()
    return

