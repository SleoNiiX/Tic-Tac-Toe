from tkinter import *
import random



def next_turn(row,column):
    
    global player

    if button[row][column]['text'] == '':
        button[row][column]['text'] = player

        if player == players[1]:
            player = players[0]
        else:
            player = players[1]

window = Tk()
window.title("Tic Tac Toe")

players = ["X","O"]
player = players[random.randint(0,1)]
button = [[0,0,0],
          [0,0,0],
          [0,0,0]]

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        button[row][column] = Button(frame, text='', font=('Courrier',20), width = 5, height=2, command= lambda row=row, column=column: next_turn(row,column))
        button[row][column].grid(row=row,column=column)

window.mainloop()