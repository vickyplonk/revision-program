#A-Level Revision Program
from tkinter import *
import hashlib
from random import randint
from os import startfile

root = Tk()
root.title("Computer Science Revision Program")
root.geometry("1000x1000")
root.iconbitmap("kirby cubed.ico")
colour="peach puff"
root.configure(bg="peach puff")

#making a class for the windows
class Window:
    def __init__(self, root):
        #making a canvas widget for the snow and rest of program
        global canvas
        canvas = Canvas(root, height=1000, width=1000, bg=colour)
        canvas.place(x=0, y=0)
#instantiating an object
window=Window(root)

#snow procedure to make a snowfall effect
def snow():
    #arrays for the position and size of the snowflakes
    xs =[]
    ys=[]
    size=[]
    #for loop runs 100 times for 100 snowflakes
    for i in range(100):
        #random numbers added to arrays to 1000 as that is the maximum
        #size of the canvas
        xs.append(randint(0, 1000))
        ys.append(randint(0, 1000))
        #sizes of the snowflakes will range from 1 to 10
        size.append(randint(1, 10))

    #procedure to make snowfall
    def snowfall():
        #delete everything from the canvas so far
        canvas.delete("all")
        #for each of the 100 snowflakes
        for i in range(100):
            #getting each snowflake from the array
            x = xs[i]
            y = ys[i]
            s = size[i]
            totalx=x+s
            totaly=y+s
            #make the snowflake
            canvas.create_oval(x, y, totalx, totaly, fill="white", outline="white")
            #update the arrays so that the snowflakes will be able to move
            ys[i] = ys[i] + (s / 10) 
            xs[i] = xs[i] - 5
            
            if y > 1000:
                ys[i] = 0
            if x < 0:
                xs[i] = 1000
            elif x > 1000:
                xs[i] = 0
        canvas.after(3, snowfall)
    snowfall()

#making the font sizes for each of different sizes
titlefontsize="none 24 bold"
buttonfontsize="none 12"
subtitlefontsize="none 12 bold"
#making the variables global
global logged_in, password_hash
password_hash=""
logged_in=False

def login_check():
    if logged_in == True:
        revision_program()
    else:
        start()
def start():
    if logged_in == True:
        revision_program()
    for label in canvas.winfo_children():
        label.destroy()

    intro_title = Label(canvas, text="Computer Science Revision Program", bg="lavender", fg="black", font=titlefontsize)
    intro_title.place(relx=0.5, rely=0.2, anchor="center")
    #colours: peach puff, lavender, lavender blush, misty rose, cornflower blue 
    global settings
    def settings():
        for label in canvas.winfo_children():
            label.destroy()
        button_home=Button(canvas, text="Home", command=login_check, fg="black", bg="lavender", font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")        
        settings_title = Label(canvas, text="Settings", bg="lavender", fg="black", font=titlefontsize)
        settings_title.place(relx=0.5, rely=0.2, anchor="center")
        #change font size settings
        def small_font_size():
            global titlefontsize, buttonfontsize,subtitlefontsize
            titlefontsize="none 20 bold"
            buttonfontsize="none 8"
            subtitlefontsize="none 8 bold"
        def medium_font_size():
            global titlefontsize, buttonfontsize,subtitlefontsize
            titlefontsize="none 24 bold"
            buttonfontsize="none 12"
            subtitlefontsize="none 12 bold"
        def large_font_size():
            global titlefontsize, buttonfontsize,subtitlefontsize
            titlefontsize="none 28 bold"
            buttonfontsize="none 16"
            subtitlefontsize="none 16 bold"
        def xlarge_font_size():
            global titlefontsize, buttonfontsize,subtitlefontsize
            titlefontsize="none 32 bold"
            buttonfontsize="none 20"
            subtitlefontsize="none 20 bold"
        button_small=Button(canvas, text="Small Font", command=small_font_size, fg="black", bg="lavender", font=buttonfontsize)
        button_small.place(relx=0.2,rely=0.3, anchor="center")
        button_medium=Button(canvas, text="Medium Font", command=medium_font_size, fg="black", bg="lavender", font=buttonfontsize)
        button_medium.place(relx=0.4,rely=0.3, anchor="center") 
        button_large=Button(canvas, text="Large Font", command=large_font_size, fg="black", bg="lavender", font=buttonfontsize)
        button_large.place(relx=0.6,rely=0.3, anchor="center")
        button_xlarge=Button(canvas, text="X Large Font", command=xlarge_font_size, fg="black", bg="lavender", font=buttonfontsize)
        button_xlarge.place(relx=0.8,rely=0.3, anchor="center")

        #change colour
        def change_background():
            global colour
            colour =clicked.get()
            canvas.configure(bg=colour)
        options=["white smoke","peach puff","navajo white",  "mint cream","light pink","lavender blush", "misty rose", "cornflower blue","sky blue","sea green", "medium sea green", "light salmon","gray19","gray69"]
        clicked=StringVar()
        clicked.set(options[0])
        drop=OptionMenu(canvas,clicked, *options)
        drop.place(relx=0.35, rely=0.4)
        button_colour=Button(canvas,text="Choose Background Colour", command = change_background)
        button_colour.place(relx=0.6, rely=0.42, anchor="center")
        gray19_darkmode=Label(canvas, text ="gray19 for dark mode",bg="lavender", fg="black", font=subtitlefontsize)
        gray19_darkmode.place(relx=0.5,anchor="center",rely=0.47)

       
    button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
    button_settings.place(relx=0.9,rely=0.9, anchor="center")
    #login procedure
    def login():
        #destroying all the labels in the window
        for label in canvas.winfo_children():
            label.destroy()
        #making buttons and labels
        button_home=Button(canvas, text="Home", command=start, fg="black", bg="lavender", font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")
        button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
        button_settings.place(relx=0.9,rely=0.9, anchor="center")
        login_title = Label(canvas, text="Login", bg="lavender", fg="black", font=titlefontsize, width="10")
        login_title.place(relx=0.5, rely=0.2, anchor="center")
        #login system
        global login_username, login_password
        #making the labels and entry fields for the user to input their details
        username_label=Label(canvas, text ="Enter Your Username",bg="lavender", fg="black", font=subtitlefontsize)
        username_label.place(relx=0.5, rely=0.4, anchor="center")
        login_username=Entry(canvas, width = 50)
        login_username.place(relx =0.5, rely=0.45, anchor ="center")
        password_label=Label(canvas, text ="Enter Your Password",bg="lavender", fg="black", font=subtitlefontsize)
        password_label.place(relx=0.5, rely=0.5, anchor="center")
        login_password=Entry(canvas, width = 50,show="*")
        login_password.place(relx =0.5, rely=0.55, anchor ="center")

        def login_click():
            global username, password,username_found
            #getting the users inputted details from the fields
            username=login_username.get()
            password=login_password.get()
            #finding login details from text file
            global username_found
            username_found=False
            #opening file with the user's details
            file_userdetails=open("user details.txt","r")
            for line in file_userdetails:
                global parts, username1, password1, name1, has_pet
                #splitting each line in the file and storing them in an array
                parts=line.split(";")
                username1 = parts[0]
                password1 = parts[1]
                name1 = parts[2]
                #comparing if the username is equivalent to a username in the file
                if username1==username:
                    #hashing the password
                    password=password.encode()
                    password=hashlib.sha256(password).hexdigest()
                    #comparing the hashed password and the hashed password stored in the file
                    if password1==password:
                        username_found=True
                        #successful login
                        def success_login():
                            #delete all the labels
                            for label in canvas.winfo_children():
                                label.destroy()
                            #making the button and label
                            loginlabel=Label(canvas, text ="Login Successful",bg="lavender", fg="black", font=subtitlefontsize)
                            loginlabel.place(relx=0.5, rely=0.3, anchor="center")
                            #procedd button then runs the main revision program procedure
                            button_login=Button(canvas, text="Proceed", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
                            button_login.place(relx=0.5,rely=0.5, anchor="center")                            
                        success_login() 
            if username_found==False:
                def unsuccessful_login():
                    #delete all labels and make the login and button
                    for label in canvas.winfo_children():
                        label.destroy()
                    loginlabel=Label(canvas, text ="Login Unsuccessful, Try Again",bg="lavender", fg="black", font=subtitlefontsize)
                    loginlabel.place(relx=0.5, rely=0.3, anchor="center")
                    button_login=Button(canvas, text="Login Again", command=login, fg="black", bg="lavender", font=buttonfontsize)
                    button_login.place(relx=0.5,rely=0.5, anchor="center")
                unsuccessful_login()
        #button to login
        button_login1=Button(canvas, text="Login", command=login_click, fg="black", bg="lavender", font=buttonfontsize)
        button_login1.place(relx=0.5,rely=0.6, anchor="center")
        #changes logged_in
    button_login=Button(canvas, text="Login", command=login, fg="black", bg="lavender", font=buttonfontsize)
    button_login.place(relx=0.35,rely=0.5, anchor="center")
    def register():
        #deleting all the labels
        for label in canvas.winfo_children():
            label.destroy()
        #making the buttons and labels
        button_home=Button(canvas, text="Home", command=start ,fg="black", bg="lavender", font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")
        button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
        button_settings.place(relx=0.9,rely=0.9, anchor="center")
        register_title = Label(canvas, text="Register", bg="lavender", fg="black", font=titlefontsize)
        register_title.place(relx=0.5, rely=0.2, anchor="center")
        #register system
        username_label=Label(canvas, text ="Create Your Username",bg="lavender", fg="black", font=subtitlefontsize)
        username_label.place(relx=0.5, rely=0.4, anchor="center")
        global register_username, name_entry, register_password
        #making the entry field and labels and positioning these labels and entries
        register_username=Entry(canvas, width = 50)
        register_username.place(relx =0.5, rely=0.45, anchor ="center")
        password_label=Label(canvas, text ="Create Your Password",bg="lavender", fg="black", font=subtitlefontsize)
        password_label.place(relx=0.5, rely=0.5, anchor="center")
        password_conditions=Label(canvas, text="Password must contain 8 or more uppercase or lowercase characters, numbers and symbols", bg="lavender", fg="black", font=buttonfontsize)
        password_conditions.place(relx=0.5, rely=0.55,anchor ="center")
        register_password=Entry(canvas, width = 50,show="*")
        register_password.place(relx =0.5, rely=0.6, anchor ="center")
        name_label=Label(canvas, text ="Enter Your Name",bg="lavender", fg="black", font=subtitlefontsize)
        name_label.place(relx=0.5, rely=0.65, anchor="center")
        name_entry=Entry(canvas, width = 50)
        name_entry.place(relx =0.5, rely=0.7, anchor ="center")
        def unsuccessful_register():
            #deleting labels
            for label in root.winfo_children():
                label.destroy()
            #closing the file
            file_userdetail.close()
            register_allowed = False
            #making the label and placing it
            error_label = Label(root, text="Username Is Taken, Pick Another Username", bg="lavender",
                                fg="black", font=subtitlefontsize)
            error_label.place(relx=0.5, rely=0.3, anchor="center")
            #generating the username using randint
            if username!="":
                x = randint(0, 100)
                x = str(x)
                error_label_two = Label(root, text="Try " + username + x, bg="lavender", fg="black",
                                        font=subtitlefontsize)
                error_label_two.place(relx=0.5, rely=0.4, anchor="center")
            button_login = Button(root, text="Register Again", command=register, fg="black", bg="lavender",
                                  font=buttonfontsize)
            button_login.place(relx=0.5, rely=0.5, anchor="center")
        def register_click():
            global register_allowed, password, username, name
            register_allowed=True
            #getting the user's details from the entry box
            username=register_username.get()
            password=register_password.get()
            name=name_entry.get()
            #if username is blank, register is not allowed
            if username=="":
                register_allowed=False
            #check if someone else has that username already
            file_userdetails=open("user details.txt","r")
            for line in file_userdetails:
                parts=line.split(";")
                username_check = parts[0]
                if username_check==username:
                    unsuccessful_register()
            #if password is empty, a message to say to register again is shwon
            if password =="":
                for label in canvas.winfo_children():
                    label.destroy()
                register_allowed=False
                error_label=Label(canvas, text = "You need to enter a password",bg="lavender", fg="black", font=subtitlefontsize)
                error_label.place(relx=0.5, rely=0.3, anchor="center")
                button_login=Button(canvas, text="Register Again", command=register, fg="black", bg="lavender", font=buttonfontsize)
                button_login.place(relx=0.5,rely=0.5, anchor="center")

            #array holding symbols and numbers
            symbols=["#","£","&","@","$"]
            numbers=["1","2","3","4","5","6","7","8","9","0"]
            global error_message
            error_message=""
            #password validator procedure
            def password_validator():
                global error_message
                #checking whether username is longer than 8 characters
                if len(password)<8:
                    error_message=("Enter a password with 8 or more characters\n")
                #checking if there is a character in the password
                if not any(char in symbols for char in password):
                    error_message=(error_message+"Enter a password with a symbol (£&@$#)\n")
                #checking if there is a number in the password
                if not any(char in numbers for char in password):
                    error_message=(error_message+"Enter a password with a number\n")
                #checking if there's a uppercase letter
                if not any(char.isupper() for char in password):
                    error_message=(error_message+"Enter a password with a uppercase character\n")
                #checking if there's a lowercase letter
                if not any(char.islower() for char in password):
                    error_message=(error_message+"Enter a password with a lowercase character\n")
                #check if error message is blank, if yes then the password is allowed
                if error_message!="":
                    for label in canvas.winfo_children():
                        label.destroy()
                    global register_allowed
                    register_allowed=False
                    #making the label and button
                    error_label=Label(canvas, text = error_message,bg="lavender", fg="black", font=subtitlefontsize)
                    error_label.place(relx=0.5, rely=0.3, anchor="center")
                    button_login=Button(canvas, text="Register Again", command=register, fg="black", bg="lavender", font=buttonfontsize)
                    button_login.place(relx=0.5,rely=0.5, anchor="center")
                else:
                    #hashing the password
                    global password_hash
                    password_hash=password.encode()
                    password_hash=hashlib.sha256(password_hash).hexdigest()
            password_validator()    
            if name=="":
                register_allowed=False

            #if the register attempt is valid
            def register_valid():
                #write the user details into the file
                file_userdetails=open("user details.txt","a")
                file_userdetails.write(username+";"+password_hash+";"+name+"\n")
                file_userdetails.close()
                #run the start procedure
                start()
            if register_allowed==False:
                register()
            else:
                register_valid()
        #making button
        button_register1=Button(canvas, text="Register", command=register_click, fg="black", bg="lavender", font=buttonfontsize)
        button_register1.place(relx=0.5,rely=0.8, anchor="center")
    #making buttons and placing them
    button_register=Button(canvas, text="Register", command=register, fg="black", bg="lavender", font=buttonfontsize)
    button_register.place(relx=0.65,rely=0.5, anchor="center")
    button_home=Button(canvas, text="Home", command=start, fg="black", bg="lavender", font=buttonfontsize)
    button_home.place(relx=0.1,rely=0.9, anchor="center")
    button_snow_on=Button(canvas,text="Snow", command = snow)
    button_snow_on.place(relx=0.5, rely=0.9, anchor="center")

global revision_program
def revision_program():
    global logged_in
    username_found=True
    logged_in =True
    #deleting all the labels and titles
    for label in canvas.winfo_children():
        label.destroy()

    #making the labels and buttonss
    intro_title = Label(canvas, text="Welcome To The Computer Science Revision Program",
                        bg="lavender", fg="black", font=titlefontsize)
    intro_title.place(relx=0.5, rely=0.2, anchor="center")
    button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
    button_settings.place(relx=0.9,rely=0.9, anchor="center")
    button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
    button_home.place(relx=0.1,rely=0.9, anchor="center")

    def revision():
        for label in canvas.winfo_children():
            label.destroy()
        button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
        button_settings.place(relx=0.9,rely=0.9, anchor="center")
        button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")

        def notes():
            for label in canvas.winfo_children():
                label.destroy()
            #frame
            frame = Frame(canvas)
            frame.place(x=10,y=10)
            #scrollbars 
            y_sb = Scrollbar(frame, orient=VERTICAL )
            y_sb.pack(side=RIGHT, fill=BOTH)
            x_sb = Scrollbar(frame, orient=HORIZONTAL)
            x_sb.pack(side=BOTTOM, fill=BOTH)
            #where the text goes
            text_area = Text(frame, width=120, height=50)
            text_area.pack()
            text_area.config(yscrollcommand=y_sb.set)
            y_sb.config(command=text_area.yview)
            text_area.config(xscrollcommand=x_sb.set)
            x_sb.config(command=text_area.xview)
            button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")
            global path
            #outputting notes file
            if topic=="1.Structure and Function of Processors":
                path="C:/Users/vickylam/Documents/a level coursework/1notes.txt"
            if topic =="2.OOP":
                path="C:/Users/vickylam/Documents/a level coursework/2notes.txt"
            if topic =="3.Pseudocode":
                path="C:/Users/vickylam/Documents/a level coursework/3notes.txt"
            paths = open(path)
            file_cont = paths.read()
            text_area.insert(END, file_cont)
            paths.close()

        def videos():
            for label in canvas.winfo_children():
                label.destroy()
            title=(topic +" : Videos")
            def play_video():
                if topic=="1.Structure and Function of Processors":
                    startfile(r"C:\Users\vickylam\Documents\a level coursework\1video.mp4")
                if topic =="2.OOP":
                    startfile(r"C:\Users\vickylam\Documents\a level coursework\2video.mp4")
                if topic =="3.Pseudocode":
                    startfile(r"C:\Users\vickylam\Documents\a level coursework\3video.mp4")
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")   
            button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")

            button_play_video=Button(canvas, text="Play Video", command=play_video, fg="black", bg="lavender", font="40")
            button_play_video.place(relx=0.5,rely=0.5, anchor="center")

        def flashcards():
            for label in canvas.winfo_children():
                label.destroy()
            if topic=="1.Structure and Function of Processors":
                file_flashcards=open("1flashcards","r")
                #maybe have a frame for each term and answer and a cover button/next button/flip button
                for line in file_flashcards:
                    parts=line.split(",")
                    term[i] = parts[0]
                    answer[i]=parts[1]              
            if topic =="2.OOP":
                file_flashcards=open("2flashcards","r")
            if topic =="3.Pseudocode":
                file_flashcards=open("3flashcards","r")
            title=(topic +" : Flashcards")
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")   
            button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")

            #deleting all the labels and buttons currently in the GUI
            for label in canvas.winfo_children():
                label.destroy()


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
        def test():
            for label in canvas.winfo_children():
                label.destroy()
            title=(topic +" : Test")
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")               
            button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")
            
        def progress():
            for label in canvas.winfo_children():
                label.destroy()
            title=(topic +" : Progress")
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")   
            button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")
            
        def change_topic():
            global topic
            global method
            topic=clicked_topic.get()
            method=clicked_method.get()
            if method == "Notes":
                notes()
            elif method == "Flashcards":
                flashcards()
            elif method=="Videos":
                videos()
            elif method == "Test":
                test()
            elif method =="Progress":
                progress()
        intro_title = Label(canvas, text="Computer Science Revision Program", bg="lavender", fg="black", font=titlefontsize)
        intro_title.place(relx=0.5, rely=0.2, anchor="center")
        intro_label=Label(canvas, text = "Choose your topic and mode",bg="lavender", fg="black", font=subtitlefontsize)
        intro_label.place(relx=0.5, rely=0.3, anchor="center")
        topic_choice=["1.Structure and Function of Processors","2.OOP","3.Pseudocode"]
        method_choice=["Notes","Flashcards","Videos","Test","Progress"]
        clicked_topic=StringVar()
        clicked_topic.set(topic_choice[0])
        clicked_method=StringVar()
        clicked_method.set(method_choice[0])
        drop1=OptionMenu(canvas,clicked_topic, *topic_choice)
        drop1.place(relx=0.5,rely=0.5, anchor="center")
        drop2=OptionMenu(canvas,clicked_method, *method_choice)
        drop2.place(relx=0.5, rely=0.6, anchor="center")
        button_selection=Button(canvas, text="Confirm your choices",command=change_topic)
        button_selection.place(relx=0.5, rely=0.7, anchor="center")

    button_revision=Button(canvas, text="Revision", command=revision, fg="black", bg="lavender", font=buttonfontsize)
    button_revision.place(relx=0.5,rely=0.5, anchor="center")

##also make minigames against computer for complexity            
##    def save_pet():
##        #write attributes to text file
##        global pet_type, pet_colour, pet_name
##        pet_type=clicked1.get() 
##        pet_colour=clicked2.get() 
##        pet_name=pet_name_entry.get()
##        #default if nothing entered
##        if pet_name_entry.get()=="":
##           pet_name="ur mum"
##        file_pet_details.close()
##        file_pet_details=open("pet details.txt","a")
##        file_pet_details.write(username1+";"+pet_type+";"+pet_colour+";"+pet_name+"\n")
##        file_pet_details.close()
##        revision_program()
##        
##    def create_pet():
##        #OOP class of pet
##        global pet_name_entry, clicked1, clicked2, pet_name_entry
##        options1=["Cat","Dog","Fish","Ferret","Hamster","Pig"]
##        clicked1=StringVar()
##        clicked1.set(options1[0])
##        drop1=OptionMenu(canvas,clicked1, *options1)
##        drop1.place(relx=0.5, rely=0.4,anchor="center")
##        options2=["Red","Orange","Yellow","Green","Blue","Indigo","Violet"]
##        clicked2=StringVar()
##        clicked2.set(options2[0])
##        drop2=OptionMenu(canvas,clicked2, *options2)
##        drop2.place(relx=0.5, rely=0.5,anchor="center")
##        pet_name_entry=Entry(canvas, width = 50)
##        pet_name_entry.place(relx =0.5, rely=0.65, anchor ="center")
##        name_label=Label(canvas, text ="Enter Your Pet's Name",bg="lavender", fg="black", font=subtitlefontsize)
##        name_label.place(relx=0.5, rely=0.6, anchor="center")
##        button_create_pet=Button(canvas, text="Create Pet", command=save_pet, fg="black", bg="lavender", font=buttonfontsize)
##        button_create_pet.place(relx=0.5,rely=0.9, anchor="center")
##    def created_pet():
##        print("picture of users pet")
##        
##    #pet button
##    def pet():
##        for label in canvas.winfo_children():
##            label.destroy()
##        button_pet.destroy()
##        button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
##        button_home.place(relx=0.1,rely=0.9, anchor="center")
##        button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
##        button_settings.place(relx=0.9,rely=0.9, anchor="center")
##        pet_title = Label(canvas, text="Pet", bg="lavender", fg="black", font=titlefontsize)
##        pet_title.place(relx=0.5, rely=0.2, anchor="center")
##        file_pet_details=open("pet details.txt","r")
##        for line in file_pet_details:
##            parts1=line.split(";")
##            if parts1[0]==username1:
##                file_pet_details.close()
##                created_pet()
##        create_pet()
##    button_pet=Button(canvas, text="Pet", command=pet, fg="black", bg="lavender", font=buttonfontsize)
##    button_pet.place(relx=0.9,rely=0.1, anchor="center")


start()

