##from tkinter import *
##root = Tk()
##
##Label(text="Position 1", width=10).grid(row=0, column=0)
##Label(text="Position 2", width=10).grid(row=0, column=1)
##Label(text="Position 3", width=10).grid(row=1, column=0)
##Label(text="Position 4", width=10).grid(row=1, column=1)
##root.mainloop()

from tkinter import *
root = Tk()
root.geometry("1000x1000")
root.configure(bg="peach puff")

frame_term= Frame(root, height = 400,width = 400, bg="cornflower blue").place(x=50, y=400)
frame_answer= Frame(root, height = 400,width = 400, bg="salmon").place(x=550, y=400)

root.mainloop()
