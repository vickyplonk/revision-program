#flashcard test
from tkinter import *


def flashcards():
    #deleting all the labels and buttons currently in the GUI
    for label in canvas.winfo_children():
        label.destroy()

    topic="1.Structure and Function of Processors"

    title=(topic +" : Flashcards")
    intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
    intro_title.place(relx=0.5, rely=0.2, anchor="center")
    def reset_procedure():
        for label in canvas.winfo_children():
            label.destroy()
        button=Button(canvas,text="Flashcards" ,command=flashcards, fg="black", bg="lavender", font=buttonfontsize)
        button.place(relx=0.1,rely=0.9, anchor="center")
    button_settings=Button(canvas, text="Settings", command=reset_procedure, fg="black", bg="lavender", font=buttonfontsize)
    button_settings.place(relx=0.9,rely=0.9, anchor="center")
    button_home=Button(canvas, text="Home", command=reset_procedure, fg="black", bg="lavender", font=buttonfontsize)
    button_home.place(relx=0.1,rely=0.9, anchor="center")
    
    #creating empty lists
    term=[]
    answer=[]

    #selection to choose the differnt file to open
    if topic=="1.Structure and Function of Processors":
        #opening file
        file_flashcards=open("1flashcards.txt","r")
        #for each line in the file
        #split the line into different parts separated by a semi-colon
        for line in file_flashcards:
            parts=line.split(";")
            #append each part to the list
            term.append(parts[0])
            answer.append(parts[1])
        #close the file
        file_flashcards.close()
    if topic =="2.OOP":
        file_flashcards=open("2flashcards.txt","r")
        for line in file_flashcards:
            parts=line.split(";")
            term.append(parts[0])
            answer.append(parts[1])
        file_flashcards.close()
    if topic =="3.Pseudocode":
        file_flashcards=open("3flashcards.txt","r")
        for line in file_flashcards:
            parts=line.split(";")
            term.append(parts[0])
            answer.append(parts[1])
        file_flashcards.close()
        
    #making the card number variable global
    global card_number, text_term, text_answer, display_answer
    #initializing the variable with a value of 0 - acts as the list index
    card_number=0
    text_term=term[card_number]
    print(text_term)
    text_answer=answer[card_number]
    print(text_answer)
    display_answer=""
    #getting length of list to be used as a boundary
    total=len(term)
    
    #next card procedure
    def next_card():
        root.update_idletasks()
        global card_number
        #if card number is less than the length of the list then the next card can be displayed

        #make it work by making it display on the gui
        if card_number<(total-1):
            text_term=term[card_number+1]
            global text_answer
            text_answer=answer[card_number+1]
            #incrementing by 1
            card_number=card_number+1
            global label_term
            label_term.destroy()
            label_answer.destroy()

            label_term=Label(frame_term, text=text_term, font=subtitlefontsize,wraplengt=375)
            label_term.place(x=5,y=5)

            label_answer.destroy()

        else:
            print("no more terms")
    #styll need to do this to make previous button work
    def last_card():
        global card_number
        if card_number!=0:
            text_term=term[card_number-1]
            global text_answer, label_term
            text_answer=answer[card_number-1]
            card_number=card_number-1
            label_term.destroy()
            label_answer.destroy()
            
            label_term=Label(frame_term, text=text_term, font=subtitlefontsize,wraplengt=375)
            label_term.place(x=5,y=5)
            label_answer.destroy()

        else:
            print("no more terms")
    def reveal_card():
        #show text answer
        display_answer=text_answer
        global label_answer

        label_answer=Label(frame_answer, text=display_answer, font=subtitlefontsize,wraplengt=375)
        label_answer.place(x=5,y=5)

    #maybe have a frame for each term and answer and a cover button/next button/flip button
    frame_term= Frame(canvas, height = 400,width = 400, bg="cornflower blue")
    frame_term.place(x=50, y=400)
    frame_answer= Frame(canvas, height = 400,width = 400, bg="salmon")
    frame_answer.place(x=550, y=400)
    button_next=Button(canvas, text="Next", command=next_card, fg="black", bg="lavender", font=buttonfontsize).place(relx=0.25,rely=0.85, anchor="center")
    button_previous=Button(canvas, text="Previous", command=last_card, fg="black", bg="lavender", font=buttonfontsize).place(relx=0.75,rely=0.85, anchor="center")
    button_reveal=Button(canvas, text="Reveal", command=reveal_card, fg="black", bg="lavender", font=buttonfontsize).place(relx=0.5,rely=0.85, anchor="center")
    global label_answer, label_term
    label_term=Label(frame_term, text=text_term, font=subtitlefontsize,wraplengt=375)
    label_term.place(x=5,y=5)
    label_answer=Label(frame_answer, text=display_answer, font=subtitlefontsize,wraplengt=375)
    label_answer.place(x=5,y=5)

root = Tk()
root.title("Computer Science Revision Program")
root.geometry("1000x1000")
root.iconbitmap("kirby cubed.ico")
colour="peach puff"
root.configure(bg="peach puff")

titlefontsize="none 24 bold"
buttonfontsize="none 12"
subtitlefontsize="none 12 bold"

#making a class for the windows
class Window:
    def __init__(self, root):
        #making a canvas widget for the snow and rest of program
        global canvas
        canvas = Canvas(root, height=1000, width=1000, bg=colour)
        canvas.place(x=0, y=0)
#instantiating an object
window=Window(root)
flashcards()
