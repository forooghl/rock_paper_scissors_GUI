import tkinter
from tkinter import Tk
from tkinter import *
from tkinter import messagebox
import random

#show who win
def GameResult():
    global RChoice , HChoice , win , winLabel , point

    #show robot choice lable
    if RChoice == 'rock':
        rockL.place(x = 210 , y = 0)
    elif RChoice == 'paper':
        paperL.place(x = 210 , y = 0)
    elif RChoice == 'scissors':
        scissorsL.place(x = 210 , y = 0)

    #add win lable on screen
    winLabel = Label(main , font = 'arial' , text = "Winner: " + win)
    winLabel.pack()
    winLabel.place(x = 230 , y = 155)
    winLabel['bg'] = '#E3E3FF'

    #show human choice lable
    if HChoice == 'rock':
        rockLH.place(x = 210 , y = 200)

    elif HChoice == 'paper':
        paperLH.place(x = 210 , y = 200)

    elif HChoice == 'scissors':
        scissorsLH.place(x = 210 , y = 200)

    #hide button
    rock.place(x = 210 , y = 400)
    paper.place(x = 210 , y = 400)
    scissors.place(x = 210 , y = 400)

    #game over message
    if point < 0 :
        point = 0
        score.config(text = "Score : " + str(point))
        messagebox.showinfo("Loser" , "Game Over")

    #add play again button
    playagainButton = tkinter.Button(main , text = 'Play again' , command = Playagain)
    playagainButton.pack()
    playagainButton.place(x = 540 , y = 370)
    playagainButton['bg'] = '#F9F2BB'


#play again function
def Playagain():
    global winLable

    #hide robot lable choice
    rockL.place(x = 210 , y = 400)
    paperL.place(x = 210 , y = 400)
    scissorsL.place(x = 210 , y = 400)

    #hide human lable choice
    rockLH.place(x = 210 , y = 400)
    paperLH.place(x = 210 , y = 400)
    scissorsLH.place(x = 210 , y = 400)

    #destroy win lable
    winLabel.destroy()

    #show buttons
    rock.place(x = 10 , y = 100)
    paper.place(x = 210 , y = 100)
    scissors.place(x = 410 , y = 100)

#robot choice
def OurturnFun():
    global RChoice , dice

    #random choice for robot
    if dice == 1:
        RChoice = "rock"
    elif dice == 2:
        RChoice = "paper"
    elif dice == 3:
        RChoice = "scissors"

    #random num in range 1 - 3
    dice = random.randint(1 , 3)

#Human choice
def YourturnFun(choice):
    global HChoice

    #call robot choice function
    OurturnFun()

    #find out what is human choice
    if choice == 'rock':
        HChoice = "rock"
    elif choice == 'paper':
        HChoice = "paper"
    elif choice == 'scissors':
        HChoice = "scissors"

    #call winner function and check who win
    Winner()

def ScoreFun():
    global point , win

    #calculate score
    if win == "Human" :
        point += 1
    elif win == "Robot":
        point -= 1

    #refresh score on board
    score.config(text = "Score : " + str(point))

def Winner():
    global win , HChoice , RChoice

    #check who win
    if HChoice == 'rock' and RChoice == 'rock':
        win = "Equal"
    elif HChoice == 'paper' and RChoice == 'paper':
        win = "Equal"
    elif HChoice == 'scissors' and RChoice == 'scissors':
        win = "Equal"
    elif HChoice == 'rock' and RChoice == 'scissors':
        win = "Human"
    elif HChoice == 'paper' and RChoice == 'rock':
        win = "Human"
    elif HChoice == 'scissors' and RChoice == 'paper':
        win = "Human"
    elif HChoice == 'rock' and RChoice == 'paper':
        win = "Robot"
    elif HChoice == 'paper' and RChoice == 'scissors':
        win = "Robot"
    elif HChoice == 'scissors' and RChoice == 'rock':
        win = "Robot"

    #call score function to refresh score
    ScoreFun()

    #call Game result
    GameResult()

#Main program
main = Tk()
main.title("rock paper scissors")
main.geometry("610x400")
main.resizable(width = False, height = False)
main['bg'] = '#F9F2BB'

#Variable
point = 0
HChoice = ""
RChoice = ""
win = ""
dice = random.randint(1 , 3)
winLabel = Label()

#Image of rock ...
rockIcon = PhotoImage(file = r"rock.png")
paperIcon = PhotoImage(file = r"paper.png")
scissorsIcon = PhotoImage(file = r"scissors.png")

#score lable
score = Label(main , font = 'arial' , text = "Score : 0")
score.pack()
score.place(x = 0 , y = 0)
score['bg'] = '#F9F2BB'

#rock paper scissors Lable for robot
rockL = Label(main , image = rockIcon , width = 180 )
rockL.pack()
rockL.place(x = 210 , y = 400)
rockL['bg'] = '#E3E3FF'

paperL = Label(main , image = paperIcon , width = 180 )
paperL.pack()
paperL.place(x = 210 , y = 400)
paperL['bg'] = '#E3E3FF'

scissorsL = Label(main , image = scissorsIcon , width = 180)
scissorsL.pack()
scissorsL.place(x = 210 , y = 400)
scissorsL['bg'] = '#E3E3FF'

#rock paper scissors Lable for human
rockLH = Label(main , image = rockIcon , width = 180 )
rockLH.pack()
rockLH.place(x = 210 , y = 400)
rockLH['bg'] = '#E3E3FF'

paperLH = Label(main , image = paperIcon , width = 180 )
paperLH.pack()
paperLH.place(x = 210 , y = 400)
paperLH['bg'] = '#E3E3FF'

scissorsLH = Label(main , image = scissorsIcon , width = 180)
scissorsLH.pack()
scissorsLH.place(x = 210 , y = 400)
scissorsLH['bg'] = '#E3E3FF'

# rock paper scissors button
rock = tkinter.Button(main , image = rockIcon , width = 180 , command = lambda choice = "rock" : YourturnFun(choice))
rock.pack()
rock.place(x = 10 , y = 100)
rock['bg'] = '#FFDBDB'

paper = tkinter.Button(main , image = paperIcon , width = 180 , command = lambda choice = "paper" : YourturnFun(choice))
paper.pack()
paper.place(x = 210 , y = 100)
paper['bg'] = '#FFDBDB'

scissors = tkinter.Button(main , image = scissorsIcon , width = 180 , command = lambda choice = "scissors" : YourturnFun(choice))
scissors.pack()
scissors.place(x = 410 , y = 100)
scissors['bg'] = '#FFDBDB'

#GAME loop
main.mainloop()
