from tkinter import *
import random



def next_turn(row,column):
    
    global player

    if button[row][column]['text'] == '':
        button[row][column]['text'] = player

        if win_detect() == False:
            print('non')
        elif win_detect() == True:
            print('gg')
        elif win_detect() == 'no_match':
            print('no_match')            

        if player == players[1]:
            player = players[0]
        else:
            player = players[1]

def win_detect():
    for row in range(3):
        if button[row][0]['text'] == button[row][1]['text'] == button[row][2]['text'] != '':
            return True

    for column in range(3):
        if button[0][column]['text'] == button[1][column]['text'] == button[2][column]['text'] != '':
            return True
        
    if button[0][0]['text'] == button[1][1]['text'] == button[2][2]['text'] != '':
        return True

    elif button[0][2]['text'] == button[1][1]['text'] == button[2][0]['text'] != '':
        return True
    
    return no_match()

def no_match():
    for row in range(3):
        for column in range(3):
            if button[row][column]['text'] == '' :
                return False
    return 'no_match'


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