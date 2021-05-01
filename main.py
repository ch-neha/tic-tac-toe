import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

screen = tk.Tk()
screen.title("tic-tac-toe")

clicked = []
buttons = []
count = 1
gameover = False

for i in range(9):
    clicked.append(True)


def distroy_screen():
    screen.destroy()


def gameOver(win):
    go_screen = tk.Toplevel(screen)
    go_screen.title("GameOver")
    myFont = font.Font(size=20)
    l = tk.Label(go_screen, text="PLAYER "+win+" WINS!", fg="#009933")
    l['font'] = myFont
    l.pack(padx=20, pady=20)
    tk.Button(go_screen, text="   OK   ", command=distroy_screen).pack(pady=10)
    go_screen.mainloop()


def tie():
    go_screen = tk.Toplevel(screen)
    go_screen.title("GameOver")
    l = tk.Label(go_screen, text="IT'S A TIE!", fg="#009933")
    l['font'] = myFont
    l.pack(padx=20, pady=20)
    tk.Button(go_screen, text="   OK   ", command=distroy_screen).pack(pady=10)
    go_screen.mainloop()


def checkWinner():
    list = [0, 3, 6]
    global buttons, count, gameover
    for j in list:
        if buttons[j]["text"] == buttons[j+1]["text"] == buttons[j+2]["text"]:
            if buttons[j]["text"] == "X":
                gameOver("X")
                gameover = True
            elif buttons[j]["text"] == "O":
                gameOver("O")
                gameover = True
    for i in range(3):
        if buttons[i]["text"] == buttons[i+3]["text"] == buttons[i+6]["text"]:
            if buttons[i]["text"] == "X":
                gameOver("X")
                gameover = True
            elif buttons[i]["text"] == "O":
                gameOver("O")
                gameover = True
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"]:
        if buttons[0]["text"] == "X":
            gameOver("X")
            gameover = True
        elif buttons[0]["text"] == "O":
            gameOver("O")
            gameover = True
    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"]:
        if buttons[2]["text"] == "X":
            gameOver("X")
            gameover = True
        elif buttons[2]["text"] == "O":
            gameOver("O")
            gameover = True
    if gameover == False and count == 10:
        tie()


def click(i):
    global count, buttons, clicked
    if count % 2 == 0 and clicked[i] == True:
        buttons[i]["text"] = "O"
        clicked[i] = False
        count += 1
    elif count % 2 == 1 and clicked[i] == True:
        buttons[i]["text"] = "X"
        clicked[i] = False
        count += 1
    checkWinner()


j, k = 1, 1
for i in range(1, 10):
    myFont = font.Font(size=30)
    b = tk.Button(screen, text="   ", padx=40, pady=40, bg='#ffff00',
                  command=lambda i=i-1: click(i))
    k = i % 3
    if(i % 3 == 0):
        k = 3
    b.grid(row=j, column=k)
    b['font'] = myFont
    buttons.append(b)
    if(i % 3 == 0):
        j += 1

tk.messagebox.showinfo(
    "Instructions", "Player X starts the game.\nClick on any button to start")
screen.mainloop()
