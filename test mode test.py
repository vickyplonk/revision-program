#test test
from tkinter import *
from random import randint

def test():
    #deleting all the labels and buttons currently in the GUI
    for label in canvas.winfo_children():
        label.destroy()

    topic="1.Structure and Function of Processors"

    title=(topic +" : Test")
    intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
    intro_title.place(relx=0.5, rely=0.2, anchor="center")
    def reset_procedure():
        for label in canvas.winfo_children():
            label.destroy()
        button=Button(canvas,text="Tests" ,command=test, fg="black", bg="lavender", font=buttonfontsize)
        button.place(relx=0.1,rely=0.9, anchor="center")
    button_settings=Button(canvas, text="Settings", command=reset_procedure, fg="black", bg="lavender", font=buttonfontsize)
    button_settings.place(relx=0.9,rely=0.9, anchor="center")
    button_home=Button(canvas, text="Home", command=reset_procedure, fg="black", bg="lavender", font=buttonfontsize)
    button_home.place(relx=0.1,rely=0.9, anchor="center")
    
    #creating empty lists
    question=[]
    #multiple choice test - answer1 will contain the correct answers
    #but i will randomise the order in which the answers are displayed.
    answer1=[]
    answer2=[]
    answer3=[]
    answer4=[]

    #selection to choose the differnt file to open
    if topic=="1.Structure and Function of Processors":
        #opening file
        file_test=open("1test.txt","r")
    if topic =="2.OOP":
        file_test=open("2test.txt","r")
    if topic =="3.Pseudocode":
        file_test=open("3test.txt","r")
    #for each line in the file
    #split the line into different parts separated by a semi-colon
    for line in file_test:
        parts=line.split(";")
        #append each part to the list
        question.append(parts[0])
        answer1.append(parts[1])
        answer2.append(parts[2])
        answer3.append(parts[3])
        answer4.append(parts[4])
    #close the file
    file_test.close()
    total=len(question)
    global question_number, text_question, answer_choices, test_score
    question_number=0
    text_question=question[question_number]
    answer_choices=("A: "+answer1[question_number]+ "\nB: "+answer2[question_number]+"\nC: "+answer3[question_number]+"\nD: "+answer4[question_number])
    test_score=0
    def submit():
        #get answers from quiz - dropdown menu?
        answer=clicked.get()
        if answer =="A":
            #correct answer
            global test_score
            test_score=test_score+1
            #print("score: "+str(test_score))
        
    def next_question():
        submit()
        global question_number
        if question_number<(total-1):
            question_number=question_number+1
            text_question=question[question_number]
            answer_choices=("A: "+answer1[question_number]+ "\nB: "+answer2[question_number]+"\nC: "+answer3[question_number]+"\nD: "+answer4[question_number])
            global label_answer, label_question
            label_question.destroy()
            label_answer.destroy()
            label_question=Label(frame_question, text=text_question, font=subtitlefontsize,wraplengt=375)
            label_question.place(x=5,y=5)
            label_answer=Label(frame_answer, text=answer_choices, font=subtitlefontsize,wraplengt=375)
            label_answer.place(x=5,y=5)          
        else:
            #finish screen
            for label in canvas.winfo_children():
                label.destroy()
            title=(topic +" : Test")
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")
            button_settings=Button(canvas, text="Settings", command=reset_procedure, fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=reset_procedure, fg="black", bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")
            total_score="You got "+str(test_score)+" out of "+str(total)
            label_score=Label(canvas, text=total_score,bg="lavender", fg="black", font=titlefontsize)
            label_score.place(relx=0.5,rely=0.5,anchor="center")
            percentage=(test_score/total)*100
            percentage_message="Well Done :) "+str(percentage)+"%"
            label_percentage=Label(canvas, text=percentage_message,bg="lavender", fg="black", font=titlefontsize)
            label_percentage.place(relx=0.5,rely=0.7,anchor="center")            
            #print as percentage as well
    #maybe have a frame for each question and answer
    frame_question= Frame(canvas, height = 300,width = 400, bg="cornflower blue")
    frame_question.place(x=50, y=400)
    frame_answer= Frame(canvas, height = 300,width = 400, bg="salmon")
    frame_answer.place(x=550, y=400)
    button_submit=Button(canvas, text="Next Question", command=next_question, fg="black", bg="lavender", font=buttonfontsize).place(relx=0.5,rely=0.85, anchor="center")
    #dropdown menu
    answer_options=["A","B","C","D"]
    clicked=StringVar()
    clicked.set(answer_options[0])
    drop=OptionMenu(canvas, clicked,*answer_options)
    drop.place(relx=0.47,rely=0.75)
    global label_answer, label_question
    label_question=Label(frame_question, text=text_question, font=subtitlefontsize,wraplengt=375)
    label_question.place(x=5,y=5)
    label_answer=Label(frame_answer, text=answer_choices, font=subtitlefontsize,wraplengt=375)
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
test()
