#A-Level Revision Program
from tkinter import *
import hashlib

root = Tk()
root.title("Computer Science Revision Program")
root.geometry("1000x800")
root.iconbitmap("kirby cubed.ico")
colour="peach puff"
root.configure(bg="peach puff")

titlefontsize="none 24 bold"
buttonfontsize="none 12"
subtitlefontsize="none 12 bold"
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
    for label in root.winfo_children():
        label.destroy()

    intro_title = Label(root, text="Computer Science Revision Program", bg="lavender", fg="black", font=titlefontsize)
    intro_title.place(relx=0.5, rely=0.2, anchor="center")
    #colours: peach puff, lavender, lavender blush, misty rose, cornflower blue 
    global settings
    def settings():
        for label in root.winfo_children():
            label.destroy()
        button_home=Button(root, text="Home", command=login_check, fg="black", bg="lavender", font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")        
        settings_title = Label(root, text="Settings", bg="lavender", fg="black", font=titlefontsize)
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
        button_small=Button(root, text="Small Font", command=small_font_size, fg="black", bg="lavender", font=buttonfontsize)
        button_small.place(relx=0.2,rely=0.3, anchor="center")
        button_medium=Button(root, text="Medium Font", command=medium_font_size, fg="black", bg="lavender", font=buttonfontsize)
        button_medium.place(relx=0.4,rely=0.3, anchor="center") 
        button_large=Button(root, text="Large Font", command=large_font_size, fg="black", bg="lavender", font=buttonfontsize)
        button_large.place(relx=0.6,rely=0.3, anchor="center")
        button_xlarge=Button(root, text="X Large Font", command=xlarge_font_size, fg="black", bg="lavender", font=buttonfontsize)
        button_xlarge.place(relx=0.8,rely=0.3, anchor="center")

        #change colour
        def change_background():
            global colour
            colour =clicked.get()
            root.configure(bg=colour)
        options=["white smoke","peach puff","navajo white",  "mint cream","light pink","lavender blush", "misty rose", "cornflower blue","sky blue","sea green", "medium sea green", "light salmon","gray19","gray69"]
        clicked=StringVar()
        clicked.set(options[0])
        drop=OptionMenu(root,clicked, *options)
        drop.place(relx=0.35, rely=0.4)
        button_colour=Button(root,text="Choose Background Colour", command = change_background)
        button_colour.place(relx=0.6, rely=0.42, anchor="center")
        gray19_darkmode=Label(root, text ="gray19 for dark mode",bg="lavender", fg="black", font=subtitlefontsize)
        gray19_darkmode.place(relx=0.5,anchor="center",rely=0.47)
    button_settings=Button(root, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
    button_settings.place(relx=0.9,rely=0.9, anchor="center")

    def login():
        for label in root.winfo_children():
            label.destroy()
        button_home=Button(root, text="Home", command=start, fg="black", bg="lavender", font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")
        button_settings=Button(root, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
        button_settings.place(relx=0.9,rely=0.9, anchor="center")
        login_title = Label(root, text="Login", bg="lavender", fg="black", font=titlefontsize, width="10")
        login_title.place(relx=0.5, rely=0.2, anchor="center")
        #login system
        global login_username, login_password
        username_label=Label(root, text ="Enter Your Username",bg="lavender", fg="black", font=subtitlefontsize)
        username_label.place(relx=0.5, rely=0.4, anchor="center")
        login_username=Entry(root, width = 50)
        login_username.place(relx =0.5, rely=0.45, anchor ="center")
        password_label=Label(root, text ="Enter Your Password",bg="lavender", fg="black", font=subtitlefontsize)
        password_label.place(relx=0.5, rely=0.5, anchor="center")
        login_password=Entry(root, width = 50,show="*")
        login_password.place(relx =0.5, rely=0.55, anchor ="center")

        def login_click():
            global username, password,username_found
            username=login_username.get()
            password=login_password.get()
            #finding login details from text file
            global username_found
            username_found=False
            file_userdetails=open("user details.txt","r")
            for line in file_userdetails:
                global parts, username1, password1, name1, has_pet
                parts=line.split(";")
                username1 = parts[0]
                password1 = parts[1]
                name1 = parts[2]
                if username1==username:
                    password=password.encode()
                    password=hashlib.sha256(password).hexdigest()
                    if password1==password:
                        username_found=True
                        def success_login():
                            for label in root.winfo_children():
                                label.destroy()
                            loginlabel=Label(root, text ="Login Successful",bg="lavender", fg="black", font=subtitlefontsize)
                            loginlabel.place(relx=0.5, rely=0.3, anchor="center")
                            button_login=Button(root, text="Proceed", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
                            button_login.place(relx=0.5,rely=0.5, anchor="center")                            
                        success_login() 
            if username_found==False:
                def unsuccessful_login():
                    for label in root.winfo_children():
                        label.destroy()
                    loginlabel=Label(root, text ="Login Unsuccessful, Try Again",bg="lavender", fg="black", font=subtitlefontsize)
                    loginlabel.place(relx=0.5, rely=0.3, anchor="center")
                    button_login=Button(root, text="Login Again", command=login, fg="black", bg="lavender", font=buttonfontsize)
                    button_login.place(relx=0.5,rely=0.5, anchor="center")
                unsuccessful_login()

        button_login1=Button(root, text="Login", command=login_click, fg="black", bg="lavender", font=buttonfontsize)
        button_login1.place(relx=0.5,rely=0.6, anchor="center")
        #changes logged_in
    button_login=Button(root, text="Login", command=login, fg="black", bg="lavender", font=buttonfontsize)
    button_login.place(relx=0.35,rely=0.5, anchor="center")

    def register():
        for label in root.winfo_children():
            label.destroy()
        button_home=Button(root, text="Home", command=start ,fg="black", bg="lavender", font=buttonfontsize)
        button_home.place(relx=0.1,rely=0.9, anchor="center")
        button_settings=Button(root, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
        button_settings.place(relx=0.9,rely=0.9, anchor="center")
        register_title = Label(root, text="Register", bg="lavender", fg="black", font=titlefontsize)
        register_title.place(relx=0.5, rely=0.2, anchor="center")
        #register system
        username_label=Label(root, text ="Create Your Username",bg="lavender", fg="black", font=subtitlefontsize)
        username_label.place(relx=0.5, rely=0.4, anchor="center")
        global register_username, name_entry, register_password
        register_username=Entry(root, width = 50)
        register_username.place(relx =0.5, rely=0.45, anchor ="center")
        password_label=Label(root, text ="Create Your Password",bg="lavender", fg="black", font=subtitlefontsize)
        password_label.place(relx=0.5, rely=0.5, anchor="center")
        password_conditions=Label(root, text="Password must contain 8 or more uppercase or lowercase characters, numbers and symbols", bg="lavender", fg="black", font=buttonfontsize)
        password_conditions.place(relx=0.5, rely=0.55,anchor ="center")
        register_password=Entry(root, width = 50,show="*")
        register_password.place(relx =0.5, rely=0.6, anchor ="center")
        name_label=Label(root, text ="Enter Your Name",bg="lavender", fg="black", font=subtitlefontsize)
        name_label.place(relx=0.5, rely=0.65, anchor="center")
        name_entry=Entry(root, width = 50)
        name_entry.place(relx =0.5, rely=0.7, anchor ="center")
        def register_click():
            global register_allowed, password, username, name
            register_allowed=True
            username=register_username.get()
            password=register_password.get()
            name=name_entry.get()
            username="poo"
            password="password"
            if username=="":
                register_allowed=False
            #check if someone else has that username already
            file_userdetails=open("user details.txt","r")
            for line in file_userdetails:
                parts=line.split(";")
                username_check = parts[0]
                if username_check==username:
                    for label in root.winfo_children():
                        label.destroy()
                    file_userdetails.close()
                    register_allowed=False
                    error_label=Label(root, text = "Username Is Taken, Pick Another Username",bg="lavender", fg="black", font=subtitlefontsize)
                    error_label.place(relx=0.5, rely=0.3, anchor="center")
                    button_login=Button(root, text="Register Again", command=register, fg="black", bg="lavender", font=buttonfontsize)
                    button_login.place(relx=0.5,rely=0.5, anchor="center")

            if password =="":
                for label in root.winfo_children():
                    label.destroy()
                register_allowed=False
                error_label=Label(root, text = "You need to enter a password",bg="lavender", fg="black", font=subtitlefontsize)
                error_label.place(relx=0.5, rely=0.3, anchor="center")
                button_login=Button(root, text="Register Again", command=register, fg="black", bg="lavender", font=buttonfontsize)
                button_login.place(relx=0.5,rely=0.5, anchor="center")
                
            symbols=["#","£","&","@","$"]
            numbers=["1","2","3","4","5","6","7","8","9","0"]
            global error_message
            error_message=""
            def password_validator():
                global error_message
                if len(password)<8:
                    error_message=("Enter a password with 8 or more characters\n")
                if not any(char in symbols for char in password):
                    error_message=(error_message+"Enter a password with a symbol (£&@$#)\n")
                if not any(char in numbers for char in password):
                    error_message=(error_message+"Enter a password with a number\n")
                if not any(char.isupper() for char in password):
                    error_message=(error_message+"Enter a password with a uppercase character\n")
                if not any(char.islower() for char in password):
                    error_message=(error_message+"Enter a password with a lowercase character\n")
                if error_message!="":
                    for label in root.winfo_children():
                        label.destroy()
                    global register_allowed
                    register_allowed=False
                    error_label=Label(root, text = error_message,bg="lavender", fg="black", font=subtitlefontsize)
                    error_label.place(relx=0.5, rely=0.3, anchor="center")
                    button_login=Button(root, text="Register Again", command=register, fg="black", bg="lavender", font=buttonfontsize)
                    button_login.place(relx=0.5,rely=0.5, anchor="center")
                    print(register_allowed)
                else:
                    #hashing the password
                    global password_hash
                    password_hash=password.encode()
                    password_hash=hashlib.sha256(password_hash).hexdigest()
            password_validator()    

            if name=="":
                register_allowed=False
            def register_valid():
                print(register_allowed)
                print("valid")
                file_userdetails=open("user details.txt","a")
                file_userdetails.write(username+";"+password_hash+";"+name+"\n")
                file_userdetails.close()
                start()
            print(register_allowed)
            if register_allowed==False:
                register()
            else:
                register_valid()
        button_register1=Button(root, text="Register", command=register_click, fg="black", bg="lavender", font=buttonfontsize)
        button_register1.place(relx=0.5,rely=0.8, anchor="center")
        register_click()
    button_register=Button(root, text="Register", command=register, fg="black", bg="lavender", font=buttonfontsize)
    button_register.place(relx=0.65,rely=0.5, anchor="center")

    button_home=Button(root, text="Home", command=start, fg="black", bg="lavender", font=buttonfontsize)
    button_home.place(relx=0.1,rely=0.9, anchor="center")
    register()
start()


global revision_program
def revision_program():
    global logged_in
    username_found=True
    logged_in =True
    #deleting all the labels and titles
    for label in root.winfo_children():
        label.destroy()
    #making the labels and buttonss
    intro_title = Label(root, text="Welcome To The Computer Science Revision Program",
                        bg="lavender", fg="black", font=titlefontsize)
    intro_title.place(relx=0.5, rely=0.2, anchor="center")
    button_settings=Button(root, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
    button_settings.place(relx=0.9,rely=0.9, anchor="center")
    button_home=Button(root, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
    button_home.place(relx=0.1,rely=0.9, anchor="center")

    def revision():
        for label in root.winfo_children():
            label.destroy()
        #make topic list drop down menu, revision method in one screen
        #topic choice: 1.Structure and Function of Processors 2.OOP 3.Pseudocode"
        #methods: notes/flashcards/videos/tests/progress - to make files
        print("revision procedure")

    button_revision=Button(root, text="Revision", command=revision, fg="black", bg="lavender", font=buttonfontsize)
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
##        drop1=OptionMenu(root,clicked1, *options1)
##        drop1.place(relx=0.5, rely=0.4,anchor="center")
##        options2=["Red","Orange","Yellow","Green","Blue","Indigo","Violet"]
##        clicked2=StringVar()
##        clicked2.set(options2[0])
##        drop2=OptionMenu(root,clicked2, *options2)
##        drop2.place(relx=0.5, rely=0.5,anchor="center")
##        pet_name_entry=Entry(root, width = 50)
##        pet_name_entry.place(relx =0.5, rely=0.65, anchor ="center")
##        name_label=Label(root, text ="Enter Your Pet's Name",bg="lavender", fg="black", font=subtitlefontsize)
##        name_label.place(relx=0.5, rely=0.6, anchor="center")
##        button_create_pet=Button(root, text="Create Pet", command=save_pet, fg="black", bg="lavender", font=buttonfontsize)
##        button_create_pet.place(relx=0.5,rely=0.9, anchor="center")
##    def created_pet():
##        print("picture of users pet")
##        
##    #pet button
##    def pet():
##        for label in root.winfo_children():
##            label.destroy()
##        button_pet.destroy()
##        button_home=Button(root, text="Home", command=revision_program, fg="black", bg="lavender", font=buttonfontsize)
##        button_home.place(relx=0.1,rely=0.9, anchor="center")
##        button_settings=Button(root, text="Settings", command=settings, fg="black", bg="lavender", font=buttonfontsize)
##        button_settings.place(relx=0.9,rely=0.9, anchor="center")
##        pet_title = Label(root, text="Pet", bg="lavender", fg="black", font=titlefontsize)
##        pet_title.place(relx=0.5, rely=0.2, anchor="center")
##        file_pet_details=open("pet details.txt","r")
##        for line in file_pet_details:
##            parts1=line.split(";")
##            if parts1[0]==username1:
##                file_pet_details.close()
##                created_pet()
##        create_pet()
##    button_pet=Button(root, text="Pet", command=pet, fg="black", bg="lavender", font=buttonfontsize)
##    button_pet.place(relx=0.9,rely=0.1, anchor="center")




