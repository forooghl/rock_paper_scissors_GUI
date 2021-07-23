import tkinter
from tkinter import Tk
from tkinter import *
from tkinter import messagebox
import random

def HideButton():
    print("Hide rock paper scissors button")
    print("show who win and show robot and human choice")

def ShowButton():
    print("Hide who win and hide robot and human choice")
    print("Show rock paper scissors button")

#robot choice
def OurturnFun():
    global RChoice , dice

    if dice == 1:
        RChoice = "rock"
    elif dice == 2:
        RChoice = "paper"
    elif dice == 3:
        RChoice = "scissors"
    print("dice: " ,dice)
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
    print("human choice: " , HChoice)

def ScoreFun():
    global point , win

    if win == "Human" :
        point += 1
    elif win == "Robot":
        point -= 1

    if point < 0 :
        messagebox.showinfo("Loser" , "Game Over")
        point = 0

    print("score: " , point)
    #refresh score on board
    score.config(text = "Score : " + str(point))



def Winner():
    global win , HChoice , RChoice

    if HChoice == 'rock' and RChoice == 'rock':
        win = "NoBody"
    elif HChoice == 'paper' and RChoice == 'paper':
        win = "Nobody"
    elif HChoice == 'scissors' and RChoice == 'scissors':
        win = "Nobody"
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
    print("winner: ", win)

    #call score function to refresh score
    ScoreFun()

#Main program
main = Tk()
main.title("rock paper scissors")
main.geometry("610x400")
main.resizable(width = False, height = False)

#Variable
point = 0
HChoice = ""
RChoice = ""
win = ""
dice = random.randint(1 , 3)

#Image of rock ...
rockIcon = PhotoImage(file = r"D:\Work\Pythonexe\Project\Rock Paper Scissors\Icon\rock.png")
paperIcon = PhotoImage(file = r"D:\Work\Pythonexe\Project\Rock Paper Scissors\Icon\paper.png")
scissorsIcon = PhotoImage(file = r"D:\Work\Pythonexe\Project\Rock Paper Scissors\Icon\scissors.png")

#score lable
score = Label(main , text = "Score : 0")
score.place(x = 0 , y = 0)
score.pack

# rock paper scissors button
rock = tkinter.Button(main , image = rockIcon , width = 180 , command = lambda choice = "rock" : YourturnFun(choice))
rock.pack()
rock.place(x = 10 , y = 100)

paper = tkinter.Button(main , image = paperIcon , width = 180 , command = lambda choice = "paper" : YourturnFun(choice))
paper.pack()
paper.place(x = 210 , y = 100)

scissors = tkinter.Button(main , image = scissorsIcon , width = 180 , command = lambda choice = "scissors" : YourturnFun(choice))
scissors.pack()
scissors.place(x = 410 , y = 100)

main.mainloop()
