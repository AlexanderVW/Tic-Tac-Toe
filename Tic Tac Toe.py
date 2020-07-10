from tkinter import *
import tkinter.font as f
tk = Tk()
tk.geometry("300x300")
tk.title("Tic Tac Toe")
icon = "X"
font = f.Font(size=90)
button_list = [-10, -10, -10, -10, -10, -10, -10, -10, -10]


def reset():
    global button_list, icon
    button_list = [-10, -10, -10, -10, -10, -10, -10, -10, -10]
    b1.configure(text="", state=ACTIVE)
    b2.configure(text="", state=ACTIVE)
    b3.configure(text="", state=ACTIVE)
    b4.configure(text="", state=ACTIVE)
    b5.configure(text="", state=ACTIVE)
    b6.configure(text="", state=ACTIVE)
    b7.configure(text="", state=ACTIVE)
    b8.configure(text="", state=ACTIVE)
    b9.configure(text="", state=ACTIVE)
    icon = "X"


def winner():
    row1 = button_list[0] + button_list[1] + button_list[2]
    row2 = button_list[3] + button_list[4] + button_list[5]
    row3 = button_list[6] + button_list[7] + button_list[8]
    co1 = button_list[0] + button_list[3] + button_list[6]
    co2 = button_list[1] + button_list[4] + button_list[7]
    co3 = button_list[2] + button_list[5] + button_list[8]
    di1 = button_list[0] + button_list[4] + button_list[8]
    di2 = button_list[6] + button_list[4] + button_list[2]
    options = [row1, row2, row3, co1, co2, co3, di1, di2]
    for option in options:
        if option == 3:
            print("X wins")
            reset()
        if option == 0:
            print("O wins")
            reset()


def change(btn, index):
    global icon, button_list, font
    btn.configure(text=icon, state=DISABLED, font=font)
    if icon == "X":
        icon = "O"
        button_list[index] = 1
    else:
        icon = "X"
        button_list[index] = 0
    winner()


b1 = Button(tk, text="", command=lambda: change(b1, 0))
b1.place(x=0, y=0, width=100, height=100)
b2 = Button(tk, text="", command=lambda: change(b2, 1))
b2.place(x=100, y=0, width=100, height=100)
b3 = Button(tk, text="", command=lambda: change(b3, 2))
b3.place(x=200, y=0, width=100, height=100)
b4 = Button(tk, text="", command=lambda: change(b4, 3))
b4.place(x=0, y=100, width=100, height=100)
b5 = Button(tk, text="", command=lambda: change(b5, 4))
b5.place(x=100, y=100, width=100, height=100)
b6 = Button(tk, text="", command=lambda: change(b6, 5))
b6.place(x=200, y=100, width=100, height=100)
b7 = Button(tk, text="", command=lambda: change(b7, 6))
b7.place(x=0, y=200, width=100, height=100)
b8 = Button(tk, text="", command=lambda: change(b8, 7))
b8.place(x=100, y=200, width=100, height=100)
b9 = Button(tk, text="", command=lambda: change(b9, 8))
b9.place(x=200, y=200, width=100, height=100)
tk.mainloop()
