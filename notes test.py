from tkinter import *


topic="1.Structure and Function of Processors"

ws = Tk()
ws.title("Computer Science Revision Program")
ws.geometry("1000x800")

ws.iconbitmap("kirby cubed.ico")
colour="peach puff"
ws.configure(bg="peach puff")

#frame
frame = Frame(ws)
frame.pack(pady=20)

#scrollbars 
y_sb = Scrollbar(frame, orient=VERTICAL )
y_sb.pack(side=RIGHT, fill=BOTH)
x_sb = Scrollbar(frame, orient=HORIZONTAL)
x_sb.pack(side=BOTTOM, fill=BOTH)

#where the text goes
txtarea = Text(frame, width=400, height=40)
txtarea.pack(side=LEFT)

txtarea.config(yscrollcommand=y_sb.set)
y_sb.config(command=txtarea.yview)
txtarea.config(xscrollcommand=x_sb.set)
x_sb.config(command=txtarea.xview)

#outputting notes file
if topic=="1.Structure and Function of Processors":
    path="C:/Users/vickylam/Documents/a level coursework/1notes.txt"
elif topic =="2. OOP":
    path="C:/Users/vickylam/Documents/a level coursework/2notes.txt"
elif topic =="3. Pseudocode":
    path="C:/Users/vickylam/Documents/a level coursework/3notes.txt"
path = open(path)
file_cont = path.read()
txtarea.insert(END, file_cont)
path.close()

# adding buttons 
Button(ws, text="Exit", command=lambda:ws.destroy()).pack(side=LEFT, expand=True, fill=X, padx=20, pady=20)

