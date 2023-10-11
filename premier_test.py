from tkinter import *


window = Tk()
window.title("Tic Tac Toe")
window.geometry("300x300")
window.minsize(300, 300)
window.config(background='black')

frame = Frame(window, bg='black')

nw_frame = Frame(frame, bg='white')
n_frame = Frame(frame, bg='white')
ne_frame = Frame(frame, bg='white')

button = Button(nw_frame, text="tacos")
button.pack(expand=YES)

button = Button(n_frame, text="tacos")
button.pack(expand=YES)

button = Button(ne_frame, text="tacos")
button.pack(expand=YES)

nw_frame.grid(column=0, row=0)
n_frame.grid(column=1, row=0)
ne_frame.grid(column=2, row=0)


w_frame = Frame(frame, bg='white')
m_frame = Frame(frame, bg='white')
e_frame = Frame(frame, bg='white')

button = Button(w_frame, text="tacos")
button.pack(expand=YES)

button = Button(m_frame, text="tacos")
button.pack(expand=YES)

button = Button(e_frame, text="tacos")
button.pack(expand=YES)

w_frame.grid(column=0, row=1 )
m_frame.grid(column=1, row=1 )
e_frame.grid(column=2, row=1)


sw_frame = Frame(frame, bg='white')
s_frame = Frame(frame, bg='white')
se_frame = Frame(frame, bg='white')

button = Button(sw_frame, text="tacos")
button.pack(expand=YES)

button = Button(s_frame, text="tacos")
button.pack(expand=YES)

button = Button(se_frame, text="tacos")
button.pack(expand=YES)

sw_frame.grid(column=0, row=2 )
s_frame.grid(column=1, row=2 )
se_frame.grid(column=2, row=2)

frame.pack(expand=Y)

window.mainloop()