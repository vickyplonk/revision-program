from tkinter import *
from random import randint

class Window:
    def __init__(self, master):
        global canvas

        canvas = Canvas(master, height=1000, width=1000, bg="peach puff")
        canvas.pack()

        frame1 = Frame(master)
        frame1.pack()
        MainWindow = canvas.create_window(1000,800,window=frame1)


w=1000
h=1000
root=Tk()
root.title("Christmas")
root.geometry("1000x800")
root.config(background = "sea green")

window=Window(root)

        
def snow():

    xs =[]
    ys=[]
    size=[]

    for i in range(100):
        xs.append(randint(0, w))
        ys.append(randint(0, h))
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
            xs[i] = xs[i] - 1
            if y > h:
                ys[i] = 0
            if x < 0:
                xs[i] = w
            elif x > w:
                xs[i] = 0
        canvas.after(10, render)
    render()
snow()

settings_title = Label(root, text="Settings", bg="lavender", fg="black", font="50")
settings_title.place(relx=0.5, rely=0.2, anchor="center")
