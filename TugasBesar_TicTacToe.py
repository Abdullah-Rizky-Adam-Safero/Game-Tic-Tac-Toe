from tkinter import *
from tkinter import messagebox
from pygame import mixer
from pygame.locals import *

root = Tk()
root.title("Tic-Tac-Toe Game")

#untuk x jika true x jalan, jika false o jalan
clicked = True
count = 0

#music background
mixer.init()
mixer.music.load("D:\Kuliah\Semester 2\Algoritma dan Program\TB_45-03_ABDULLAH RIZKY ADAM SAFERO-GAME TIC TAC TOE\lofi.mp3")
mixer.music.play(-1)

#fungsi menonaktifkan button ketika permainan selesai
def disable_button():
    t1.config(state=DISABLED)
    t2.config(state=DISABLED)
    t3.config(state=DISABLED)
    t4.config(state=DISABLED)
    t5.config(state=DISABLED)
    t6.config(state=DISABLED)
    t7.config(state=DISABLED)
    t8.config(state=DISABLED)
    t9.config(state=DISABLED)

#fungsi untuk mengecek pemenang
def check_win():
    global win, Tbutton
    win = False

    #x winners
    if (t1["text"] == "X" and t2["text"] == "X" and t3["text"] == "X" or
        t4["text"] == "X" and t5["text"] == "X" and t6["text"] == "X" or 
        t7["text"] == "X" and t8["text"] == "X" and t9["text"] == "X" or 
        t1["text"] == "X" and t4["text"] == "X" and t7["text"] == "X" or 
        t2["text"] == "X" and t5["text"] == "X" and t8["text"] == "X" or 
        t3["text"] == "X" and t6["text"] == "X" and t9["text"] == "X" or 
        t1["text"] == "X" and t5["text"] == "X" and t9["text"] == "X" or 
        t3["text"] == "X" and t5["text"] == "X" and t7["text"] == "X"):
        win = True
        messagebox.showinfo("Tic Tac Toe", "Player X Menang!")
        disable_button()

    #o winners
    if (t1["text"] == "O" and t2["text"] == "O" and t3["text"] == "O" or 
        t4["text"] == "O" and t5["text"] == "O" and t6["text"] == "O" or 
        t7["text"] == "O" and t8["text"] == "O" and t9["text"] == "O" or 
        t1["text"] == "O" and t4["text"] == "O" and t7["text"] == "O" or 
        t2["text"] == "O" and t5["text"] == "O" and t8["text"] == "O" or 
        t3["text"] == "O" and t6["text"] == "O" and t9["text"] == "O" or 
        t1["text"] == "O" and t5["text"] == "O" and t9["text"] == "O" or
        t3["text"] == "O" and t5["text"] == "O" and t7["text"] == "O"):
        win = True
        messagebox.showinfo("Tic Tac Toe", "Player O Menang!")
        disable_button()

    #Tidak ada pemenang
    elif count == 9 and win == False:
        messagebox.showinfo("Tic Tac Toe", "Tidak ada pemenang!")
        disable_button()

#fungsi tombol biar bisa diklik
def t_click(t):
    global clicked, count

    if t["text"] == " " and clicked == True:
        t["text"] = "X"
        clicked = False
        count += 1
        check_win()
    elif t["text"] == " " and clicked == False:
        t["text"] = "O"
        clicked = True
        count += 1
        check_win()
    else:
        messagebox.showerror("Tic Tac Toe", "halo! kotak itu sudah diisi \ntolong gunakan kotak lain")

#fungsi restart Game
def restart():
    global t1, t2, t3, t4, t5, t6, t7, t8, t9
    global clicked, count
    clicked = True
    count = 0
    #membuat tombol
    t1 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t1))
    t2 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t2))
    t3 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t3))
    t4 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t4))
    t5 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t5))
    t6 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t6))
    t7 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t7))
    t8 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t8))
    t9 = Button(root, text=' ', font='Times 20 bold', height=4, width=8, bg="systemButtonFace", command=lambda: t_click(t9))

    #menampilkan tombol
    t1.grid(row=0, column=0, sticky=S+N+E+W)
    t2.grid(row=0, column=1, sticky=S+N+E+W)
    t3.grid(row=0, column=2, sticky=S+N+E+W)
    t4.grid(row=1, column=0, sticky=S+N+E+W)
    t5.grid(row=1, column=1, sticky=S+N+E+W)
    t6.grid(row=1, column=2, sticky=S+N+E+W)
    t7.grid(row=2, column=0, sticky=S+N+E+W)
    t8.grid(row=2, column=1, sticky=S+N+E+W)
    t9.grid(row=2, column=2, sticky=S+N+E+W)

#membuat tombol exit dan restart
reset = Button(root, text='Restart', font='Times 20 bold', height=3, width=6, bg="black", fg = "white" ,command=restart)
exit = Button(root, text='Exit', font='Times 20 bold', height=3, width=6, bg="black", fg = "white" ,command=root.quit)

reset.grid(row=4, column=0, sticky=S+N+E+W)
exit.grid(row=4, column=2, sticky=S+N+E+W)


restart()

root.mainloop()