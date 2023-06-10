from tkinter import *
import hashlib
from random import randint
from turtle import *

root = Tk()
root.title("Merry Christmas")
root.geometry("1000x1000")
colour="misty rose"
root.configure(bg=colour)



class Window:
    def __init__(self, root):
        global canvas, turtle
        canvas = Canvas(root, height=1000, width=1000, bg=colour)
        canvas.place(x=0, y=0)

window=Window(root)

def snow():
    xs =[]
    ys=[]
    size=[]
    for i in range(100):
        xs.append(randint(0, 1000))
        ys.append(randint(0, 1000))
        size.append(randint(1, 10))
    def render():
        canvas.delete("all")
        for i in range(100):
            x = xs[i]
            y = ys[i]
            s = size[i]
            totalx=x+s
            totaly=y+s
            canvas.create_oval(x, y, totalx, totaly, fill="white", outline="white")

            ys[i] = ys[i] + (s / 10) 
            xs[i] = xs[i] - 5
            if y > 1000:
                ys[i] = 0
            if x < 0:
                xs[i] = 1000
            elif x > 1000:
                xs[i] = 0
        canvas.after(3, render)
    render()

snow()


