#A-Level Revision Program
from tkinter import *
from PIL import ImageTk,Image  
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
        options=["white smoke","peach puff","navajo white",  "mint cream","light pink","lavender blush",
                 "misty rose", "cornflower blue","sky blue","sea green", "medium sea green", "light salmon","gray19","gray69"]
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
                            loginlabel=Label(canvas, text ="Login Successful",bg="lavender"
                                             , fg="black", font=subtitlefontsize)
                            loginlabel.place(relx=0.5, rely=0.3, anchor="center")
                            #proceed button then runs the main revision program procedure
                            button_login=Button(canvas, text="Proceed", command=revision_program,
                                                fg="black", bg="lavender", font=buttonfontsize)
                            button_login.place(relx=0.5,rely=0.5, anchor="center")                            
                        success_login() 
            if username_found==False:
                def unsuccessful_login():
                    #delete all labels and make the login and button
                    for label in canvas.winfo_children():
                        label.destroy()
                    loginlabel=Label(canvas, text ="Login Unsuccessful, Try Again",
                                     bg="lavender", fg="black", font=subtitlefontsize)
                    loginlabel.place(relx=0.5, rely=0.3, anchor="center")
                    button_login=Button(canvas, text="Login Again", command=login,
                                        fg="black", bg="lavender", font=buttonfontsize)
                    button_login.place(relx=0.5,rely=0.5, anchor="center")
                unsuccessful_login()
        #button to login
        button_login1=Button(canvas, text="Login", command=login_click,
                             fg="black", bg="lavender", font=buttonfontsize)
        button_login1.place(relx=0.5,rely=0.6, anchor="center")
        #changes logged_in
    button_login=Button(canvas, text="Login", command=login, fg="black",
                        bg="lavender", font=buttonfontsize)
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
        password_conditions=Label(canvas, text="Password must contain 8 or more uppercase or lowercase characters, numbers and symbols",
                                  bg="lavender", fg="black", font=buttonfontsize)
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
            file_userdetails.close()
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
            #if password is empty, a message to say to register again is shown
            if password =="":
                for label in canvas.winfo_children():
                    label.destroy()
                register_allowed=False
                error_label=Label(canvas, text = "You need to enter a password",
                                  bg="lavender", fg="black", font=subtitlefontsize)
                error_label.place(relx=0.5, rely=0.3, anchor="center")
                button_login=Button(canvas, text="Register Again", command=register,
                                    fg="black", bg="lavender", font=buttonfontsize)
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
            button_settings=Button(canvas, text="Settings", command=settings,
                                   fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program,
                               fg="black", bg="lavender", font=buttonfontsize)
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
            #making the labels and buttons for this procedure
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")   
            button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")
            button_play_video=Button(canvas, text="Play Video", command=play_video, fg="black", bg="lavender", font="40")
            button_play_video.place(relx=0.5,rely=0.5, anchor="center")

        def flashcards():
            #deleting all the labels and buttons currently in the GUI
            for label in canvas.winfo_children():
                label.destroy()
            #making the buttons and labels for this procedure
            title=(topic +" : Flashcards")
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")
            button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")
            
            #creating empty lists
            term=[]
            answer=[]

            #selection to choose the different file to open
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
                    parts=line.split(",")
                    term.append(parts[0])
                    answer.append(parts[1])
                file_flashcards.close()
            if topic =="3.Pseudocode":
                file_flashcards=open("3flashcards.txt","r")
                for line in file_flashcards:
                    parts=line.split(",")
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
                    #deleting all the buttons and labels and frames
                    for label in canvas.winfo_children():
                        label.destroy()
                    #making the labels
                    title=(topic +" : Flashcards")
                    intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
                    intro_title.place(relx=0.5, rely=0.2, anchor="center")
                    no_more_terms=Label(canvas, text="There are no more terms",bg="lavender", fg="black", font=titlefontsize)
                    no_more_terms.place(relx=0.5, rely=0.5, anchor="center")
                    #default buttons
                    button_settings=Button(canvas, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
                    button_settings.place(relx=0.9,rely=0.9, anchor="center")
                    button_home=Button(canvas, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
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
                    #deleting all the buttons and labels and frames
                    for label in canvas.winfo_children():
                        label.destroy()
                    #making the labels
                    title=(topic +" : Flashcards")
                    intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
                    intro_title.place(relx=0.5, rely=0.2, anchor="center")
                    no_more_terms=Label(canvas, text="There are no more terms",bg="lavender",
                                        fg="black", font=titlefontsize)
                    no_more_terms.place(relx=0.5, rely=0.5, anchor="center")
                    #default buttons
                    button_settings=Button(canvas, text="Settings", command=settings, fg="black",
                                           bg="lavender", font=buttonfontsize)
                    button_settings.place(relx=0.9,rely=0.9, anchor="center")
                    button_home=Button(canvas, text="Home", command=revision_program, fg="black",
                                       bg="lavender", font=buttonfontsize)
                    button_home.place(relx=0.1,rely=0.9, anchor="center")
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
            button_next=Button(canvas, text="Next", command=next_card, fg="black", bg="lavender",
                               font=buttonfontsize).place(relx=0.25,rely=0.85, anchor="center")
            button_previous=Button(canvas, text="Previous", command=last_card, fg="black", bg="lavender",
                                   font=buttonfontsize).place(relx=0.75,rely=0.85, anchor="center")
            button_reveal=Button(canvas, text="Reveal", command=reveal_card, fg="black", bg="lavender",
                                 font=buttonfontsize).place(relx=0.5,rely=0.85, anchor="center")
            global label_answer, label_term
            label_term=Label(frame_term, text=text_term, font=subtitlefontsize,wraplengt=375)
            label_term.place(x=5,y=5)
            label_answer=Label(frame_answer, text=display_answer, font=subtitlefontsize,wraplengt=375)
            label_answer.place(x=5,y=5)
            
        def test():
            #deleting all current labels in the GUI
            for label in canvas.winfo_children():
                label.destroy()
            #making the default labels and buttons
            title=(topic +" : Test")
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")               
            button_settings=Button(canvas, text="Settings", command=settings, fg="black",
                                   bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black",
                               bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")
            #creating empty lists
            question=[]
            #multiple choice test - array to store each answer(A,B,C,D)
            answer1=[]
            answer2=[]
            answer3=[]
            answer4=[]
            #selection to choose the different file to open
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
            #getting the length of the questions
            total=len(question)
            #globalising variables to use throughout the program
            global question_number, text_question, answer_choices, test_score
            question_number=0
            #getting the data from the array using the question number as the index
            #putting this data into variables to use for
            text_question=question[question_number]
            answer_choices=("A: "+answer1[question_number]+ "\nB: "+answer2[question_number]+
                            "\nC: "+answer3[question_number]+"\nD: "+answer4[question_number])
            test_score=0
            #procedure to check the answer
            def submit():
                #get answers from quiz - dropdown menu?
                answer=clicked.get()
                if answer =="A":
                    #correct answer
                    global test_score
                    test_score=test_score+1
                    #print("score: "+str(test_score))

            #procedure to display the next question
            def next_question():
                submit()
                global question_number
                #if there are question numbers left then display the next question
                if question_number<(total-1):
                    #increment the question number
                    question_number=question_number+1
                    #put the question and answer into the variable
                    text_question=question[question_number]
                    answer_choices=("A: "+answer1[question_number]+ "\nB: "+answer2[question_number]+
                                    "\nC: "+answer3[question_number]+"\nD: "+answer4[question_number])
                    global label_answer, label_question
                    #refreshing the labels with the new question and answer choices
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
                    #displaying the default titles and labels
                    title=(topic +" : Test")
                    intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
                    intro_title.place(relx=0.5, rely=0.2, anchor="center")
                    button_settings=Button(canvas, text="Settings", command=reset_procedure, fg="black",
                                           bg="lavender", font=buttonfontsize)
                    button_settings.place(relx=0.9,rely=0.9, anchor="center")
                    button_home=Button(canvas, text="Home", command=reset_procedure, fg="black",
                                       bg="lavender", font=buttonfontsize)
                    button_home.place(relx=0.1,rely=0.9, anchor="center")
                    #displaying the total score and percentage
                    total_score="You got "+str(test_score)+" out of "+str(total)
                    label_score=Label(canvas, text=total_score,bg="lavender", fg="black", font=titlefontsize)
                    label_score.place(relx=0.5,rely=0.5,anchor="center")
                    percentage=(test_score/total)*100
                    percentage_message="Well Done :) "+str(percentage)+"%"
                    label_percentage=Label(canvas, text=percentage_message,bg="lavender",
                                           fg="black", font=titlefontsize)
                    label_percentage.place(relx=0.5,rely=0.7,anchor="center")
                    #adding data to progress file
                    file_progress=open("userprogress.txt","r")
                    x=0
                    #writing the text file out
                    for line in file_progress:
                        if x==0:
                            topic_one_progress=line
                        if x==1:
                            topic_two_progress=line
                        if x==2:
                            topic_three_progress=line
                        x=x+1
                    file_progress.close()
                    #open file as write + delete all contents
                    file_progress=open("userprogress.txt","r+")
                    file_progress.truncate(0)
                    #appending each array with the new score and rewriting to the file
                    if topic=="1.Structure and Function of Processors":
                        file_progress.write(topic_one_progress+";"+percentage+"\n")
                        file_progress.write(topic_two_progress+"\n")
                        file_progress.write(topic_three_progress+"\n")
                    if topic =="2.OOP":
                        topic_two_progress.append(percentage)
                        file_progress.write(topic_one_progress+"\n")
                        file_progress.write(topic_two_progress+";"+percentage+"\n")
                        file_progress.write(topic_three_progress+"\n")  
                    if topic =="3.Pseudocode":
                        topic_three_progress.append(percentage)
                        file_progress.write(topic_one_progress+"\n")
                        file_progress.write(topic_two_progress+"\n")
                        file_progress.write(topic_three_progress+";"+percentage+"\n")
                    file_progress.close()
            #maybe have a frame for each question and answer
            frame_question= Frame(canvas, height = 300,width = 400, bg="cornflower blue")
            frame_question.place(x=50, y=400)
            frame_answer= Frame(canvas, height = 300,width = 400, bg="salmon")
            frame_answer.place(x=550, y=400)
            button_submit=Button(canvas, text="Next Question", command=next_question, fg="black",
                                 bg="lavender", font=buttonfontsize).place(relx=0.5,rely=0.85, anchor="center")
            #dropdown menu
            answer_options=["A","B","C","D"]
            clicked=StringVar()
            clicked.set(answer_options[0])
            drop=OptionMenu(canvas, clicked,*answer_options)
            drop.place(relx=0.47,rely=0.75)
            #making a frame for the question and answer
            global label_answer, label_question
            label_question=Label(frame_question, text=text_question, font=subtitlefontsize,wraplengt=375)
            label_question.place(x=5,y=5)
            label_answer=Label(frame_answer, text=answer_choices, font=subtitlefontsize,wraplengt=375)
            label_answer.place(x=5,y=5)
            
        def progress():
            #deleting all the labels on the GUI
            for label in canvas.winfo_children():
                label.destroy()   
            #making the default titles and labels
            title=(topic +" : Progress")
            intro_title = Label(canvas, text=title,bg="lavender", fg="black", font=titlefontsize)
            intro_title.place(relx=0.5, rely=0.2, anchor="center")   
            button_settings=Button(canvas, text="Settings", command=settings, fg="black",
                                   bg="lavender", font=buttonfontsize)
            button_settings.place(relx=0.9,rely=0.9, anchor="center")
            button_home=Button(canvas, text="Home", command=revision_program, fg="black",
                               bg="lavender", font=buttonfontsize)
            button_home.place(relx=0.1,rely=0.9, anchor="center")
            #usernameprogress.txt open file
            progress_name=username+"progress.txt"
            file_progress=open("userprogress.txt","r")
            #line 1 = topic 1, line 2 =  topic 2, line 3 = topic 3, split each line into array
            x=0
            for line in file_progress:
                parts=line.split(";")
                if x==0:
                    topic_one_progress=parts
                    print (topic_one_progress)
                if x==1:
                    topic_two_progress=parts
                    print(topic_two_progress)
                if x==2:
                    topic_three_progress=parts
                    print(topic_three_progress)
                x=x+1
            file_progress.close()
            #this procedure needs to display it
            topic_one_total=0
            topic_two_total=0
            topic_three_total=0
            #topic 1 percentage
            topic_one_length=len(topic_one_progress)
            for i in range(0,topic_one_length-1):
                percentage=float(topic_one_progress[i])
                topic_one_total=topic_one_total+percentage
            topic_one_percentage=topic_one_total/topic_one_length
            #topic 2 percentage
            topic_two_length=len(topic_two_progress)
            for i in range(0,topic_two_length-1):
                percentage=float(topic_two_progress[i])
                topic_two_total=topic_two_total+percentage
            topic_two_percentage=topic_two_total/topic_two_length
            #topic 3 percentage
            topic_three_length=len(topic_three_progress)
            for i in range(0,topic_three_length-1):
                percentage=float(topic_three_progress[i])
                topic_three_total=topic_three_total+percentage
            topic_three_percentage=topic_three_total/topic_three_length
            #making the variables that hold the message
            topic_one="For topic one you did "+ str(topic_one_length)+" tests and your average percentage was "+str(topic_one_percentage)
            topic_two="For topic two you did "+ str(topic_two_length)+" tests and your average percentage was "+str(topic_two_percentage)
            topic_three="For topic three you did "+ str(topic_three_length)+" tests and your average percentage was "+str(topic_three_percentage)
            #making the labels for the messages
            label_topic_one=Label(canvas, text =topic_one,bg="lavender", fg="black", font=subtitlefontsize)
            label_topic_one.place(relx=0.5, rely=0.4, anchor="center")
            label_topic_two=Label(canvas, text =topic_two,bg="lavender", fg="black", font=subtitlefontsize)
            label_topic_two.place(relx=0.5, rely=0.5, anchor="center")
            label_topic_three=Label(canvas, text =topic_three,bg="lavender", fg="black", font=subtitlefontsize)
            label_topic_three.place(relx=0.5, rely=0.6, anchor="center")
            #making feedback
            feedback_messages=["doing more flashcards","watching more videos","doing some past papers","reading notes","watching Craig n Dave"]
            x=randint(0,4)
            improvements="You could improve by "+feedback_messages[x]
            label_feedback=Label(canvas,text=improvements,bg="lavender", fg="black", font=subtitlefontsize)
            label_feedback.place(relx=0.5, rely=0.8, anchor="center")
            
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

#also make minigames against computer for complexity
    global pet_pic
    def created_pet():
        global pet_pic
        for label in canvas.winfo_children():
            label.destroy()
        root2 = Tk()
        canvas1 = Canvas(root2, width = 1000, height = 1000)
        canvas1.pack() 
        if clicked1=="Cat":
            if clicked2=="Red":
                pet_pic = ImageTk.PhotoImage(Image.open("redcat.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Orange":
                pet_pic = ImageTk.PhotoImage(Image.open("orangecat.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Yellow":
                pet_pic = ImageTk.PhotoImage(Image.open("yellowcat.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Green":
                pet_pic = ImageTk.PhotoImage(Image.open("greencat.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Blue":
                pet_pic = ImageTk.PhotoImage(Image.open("bluecat.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked1=="Dog":
            if clicked2=="Red":
                pet_pic = ImageTk.PhotoImage(Image.open("reddog.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Orange":
                pet_pic = ImageTk.PhotoImage(Image.open("orangedog.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Yellow":
                pet_pic = ImageTk.PhotoImage(Image.open("yellowdog.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Green":
                pet_pic = ImageTk.PhotoImage(Image.open("greendog.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Blue":
                pet_pic = ImageTk.PhotoImage(Image.open("bluedog.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked1=="Fish":
            if clicked2=="Red":
                pet_pic = ImageTk.PhotoImage(Image.open("redfish.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Orange":
                pet_pic = ImageTk.PhotoImage(Image.open("orangefish.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Yellow":
                pet_pic = ImageTk.PhotoImage(Image.open("yellowfish.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Green":
                pet_pic = ImageTk.PhotoImage(Image.open("greenfish.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic) 
            elif clicked2=="Blue":
                pet_pic = ImageTk.PhotoImage(Image.open("bluefish.png"))
                canvas1.create_image(20,20, anchor=NW, image=pet_pic)
            canvas1.mainloop()
        #label for the pet
        pet_name = Label(canvas, text=name, bg="lavender", fg="black", font=48)
        pet_name.place(relx=0.5, rely=0.6, anchor="center")
        revision_program()
        
        def save_pet():
            #write attributes to text file
            global pet_type, pet_colour, pet_name
            pet_type=clicked1.get() 
            pet_colour=clicked2.get() 
            pet_name=pet_name_entry.get()
            #default if nothing entered
            if pet_name_entry.get()=="":
               pet_name="ur mum"
        #feed procedure that runs when the feed button is pressed
        def feed():
            global label_message
            label_message.destroy()
            #list storing messages
            feed_messages=["thank you for feeding me <3","good munch","more please","yummy","munchies"]
            x=randint(0,4)
            #generating a random message
            good_food=feed_messages[x]
            #displaying the message
            label_message=Label(canvas,text=good_food,bg="lavender", fg="black", font=48)
            label_message.place(relx=0.5, rely=0.7, anchor="center")   
        #motivation procedure
        def motivation():
            global label_message
            label_message.destroy()
            #list to store messages
            motivational_messages=["Keep Going!","You're doing Great!","Wonderful Progress!"
                                   ,"You're so Lovely!","You're so Wonderful!"]
            x=randint(0,4)
            #displaying the message from the list
            label_message=Label(canvas,text=motivational_messages[x],bg="lavender", fg="black", font=48)
            label_message.place(relx=0.5, rely=0.7, anchor="center") 

        def game():
            global label_game
            #guess the comp sci word game, opening file and putting the words and clues into list
            game_file=open("game.txt","r")
            game_words=[]
            game_clue_1=[]
            game_clue_2=[]
            game_clue_3=[]
            for line in game_file:
                parts=line.split(";")
                game_words.append(parts[0])
                game_clue_1.append(parts[1])
                game_clue_2.append(parts[2])
                game_clue_3.append(parts[3])
            game_file.close()
            
            #initializing these variables
            global card_counter,parts_counter,reveal_counter
            card_counter=0
            parts_counter=0
            reveal_counter=0
            
            #next word procedure to move on to the next word
            def next_card():
                global card_counter, reveal_counter, label_clue, label_word
                card_counter=card_counter+1
                label_word.destroy()
                reveal_counter=0
                label_clue.destroy()
                label_word.destroy()
                
            #next clue procedure to display the next clue
            def next_clue():
                global reveal_counter, label_clue, clue
                #if statements to branch to the different clues
                if reveal_counter==0:
                    clue=game_clue_1[card_counter]
                if reveal_counter==1:
                    clue=game_clue_2[card_counter]
                if reveal_counter==2:
                    clue=game_clue_3[card_counter]
                reveal_counter=reveal_counter+1
                label_clue.destroy()
                label_clue=Label(canvas,text=clue,bg="lavender", fg="black", font=48)
                label_clue.place(relx=0.5,rely=0.9,anchor="center")
                
            #reveal procedure to reveal the word
            def reveal():
                word=game_words[card_counter]
                label_word=Label(canvas,text=word,bg="lavender", fg="black", font=48)
                label_word.place(relx=0.1, rely=0.9,anchor="center")
            global label_clue, label_word
            label_clue=Label()
            label_word=Label()

            button_next_card=Button(canvas, text="Next Card", command=next_card, fg="black", bg="lavender")
            button_next_card.place(relx=0.7,rely=0.85, anchor="center")
            button_reveal=Button(canvas, text="Reveal", command=reveal, fg="black", bg="lavender")
            button_reveal.place(relx=0.3,rely=0.85, anchor="center")
            button_next_clue=Button(canvas, text="Next Clue", command=next_clue, fg="black", bg="lavender")
            button_next_clue.place(relx=0.5,rely=0.85, anchor="center")
            
        #initializing the labels
        global label_message, label_motivation
        label_message=Label(canvas,text="",bg="lavender", fg="black", font=48)
        label_game=Label(canvas,text="",bg="lavender", fg="black", font=48)
        #making feed button and motivation button and game button
        button_feed=Button(canvas, text="Feed", command=feed, fg="black", bg="lavender")
        button_feed.place(relx=0.3,rely=0.8, anchor="center")
        button_game=Button(canvas, text="Play", command=game, fg="black", bg="lavender")
        button_game.place(relx=0.5,rely=0.8, anchor="center")
        button_motivation=Button(canvas, text="GO!!!", command=motivation, fg="black", bg="lavender")
        button_motivation.place(relx=0.7,rely=0.8, anchor="center")

        created_pet()
        
    def create_pet():
        #OOP class of pet
        global pet_name_entry, clicked1, clicked2, pet_name_entry
        options1=["Cat","Dog","Fish"]
        clicked1=StringVar()
        clicked1.set(options1[0])
        drop1=OptionMenu(canvas,clicked1, *options1)
        drop1.place(relx=0.5, rely=0.4,anchor="center")
        options2=["Red","Orange","Yellow","Green","Blue"]
        clicked2=StringVar()
        clicked2.set(options2[0])
        drop2=OptionMenu(canvas,clicked2, *options2)
        drop2.place(relx=0.5, rely=0.5,anchor="center")
        pet_name_entry=Entry(canvas, width = 50)
        pet_name_entry.place(relx =0.5, rely=0.65, anchor ="center")
        name_label=Label(canvas, text ="Enter Your Pet's Name",bg="lavender",
                         fg="black", font=subtitlefontsize)
        name_label.place(relx=0.5, rely=0.6, anchor="center")
        button_create_pet=Button(canvas, text="Create Pet", command=save_pet,
                                 fg="black", bg="lavender", font=buttonfontsize)
        button_create_pet.place(relx=0.5,rely=0.9, anchor="center")

        
    #pet button
    def pet():
        for label in canvas.winfo_children():
            label.destroy()
        button_pet.destroy()
        button_home=Button(canvas, text="Home", command=revision_program,
                           fg="black", bg="lavender", font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")
        button_settings=Button(canvas, text="Settings", command=settings,
                               fg="black", bg="lavender", font=buttonfontsize)
        button_settings.place(relx=0.9,rely=0.9, anchor="center")
        pet_title = Label(canvas, text="Pet", bg="lavender", fg="black",
                          font=titlefontsize)
        pet_title.place(relx=0.5, rely=0.2, anchor="center")
        create_pet()
    button_pet=Button(canvas, text="Pet", command=pet, fg="black",
                      bg="lavender", font=buttonfontsize)
    button_pet.place(relx=0.9,rely=0.1, anchor="center")

    def help_guide():
        #deleting the labels and buttons
        for label in canvas.winfo_children():
            label.destroy()
        #making the buttons and labels
        button_home=Button(canvas, text="Home", command=revision_program,
                           fg="black", bg="lavender",font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")
        button_settings=Button(canvas, text="Settings", command=settings,
                               fg="black", bg="lavender",font=buttonfontsize)
        button_settings.place(relx=0.9,rely=0.9, anchor="center")
        #making a frame to display the help guide
        frame = Frame(canvas)
        frame.place(x=10,y=150)
        #scrollbars 
        y_sb = Scrollbar(frame, orient=VERTICAL )
        y_sb.pack(side=RIGHT, fill=BOTH)
        x_sb = Scrollbar(frame, orient=HORIZONTAL)
        x_sb.pack(side=BOTTOM, fill=BOTH)
        #where the text goes
        text_area = Text(frame, width=120, height=30)
        text_area.pack()
        text_area.config(yscrollcommand=y_sb.set)
        y_sb.config(command=text_area.yview)
        text_area.config(xscrollcommand=x_sb.set)
        x_sb.config(command=text_area.xview)
        global path
        #outputting notes file
        path="C:/Users/vickylam/Documents/a level coursework/help.txt"
        paths = open(path)
        file_cont = paths.read()
        text_area.insert(END, file_cont)
        paths.close()
    #making the help button on the main page
    button_help=Button(canvas, text="Help", command=help_guide,
                       fg="black", bg="lavender", font=buttonfontsize)
    button_help.place(relx=0.1,rely=0.1, anchor="center")

start()

