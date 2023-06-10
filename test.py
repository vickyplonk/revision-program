#test file

#font size
##from tkinter import *
##root=Tk()
##root.geometry("1000x800")
##root.iconbitmap("kirby cubed.ico")
##root.configure(bg="peach puff")
##colour1="cornflower blue"
##root.configure(bg=colour1)
##colour="Lavender"
##titlefontsize="none 24 bold"
##labelfontsize="none 100 bold"
##
##title=Label(root, text="ur mum", bg=colour, font=titlefontsize)
##subtitle=Label(root, text="ur mother", bg=colour, font=labelfontsize)
##title.place(relx=0.5, rely=0.2, anchor="center")
##subtitle.place(relx=0.5, rely=0.4, anchor="center")
##
##titlefontsize="48"
##labelfontsize="200"
##title1=Label(root, text="ur mum", bg=colour, font="none 48 bold")
##subtitle1=Label(root, text="ur mother", bg=colour, font="none 5")
##title1.place(relx=0.5, rely=0.6, anchor="center")
##subtitle1.place(relx=0.5, rely=0.8, anchor="center")
  
#file reading
##f=open("test.txt","a")
##for i in range(0,10):
##    f.write("one\n")
##f.close()
##f=open("test.txt","r")
##for x in f:
##  print(x) 
##f.close()



##file = open("usernames and passwords test.txt","a")
##for i in range(0,3):
##    username=input("enter username")
##    password=input("enter password")
##    name=input("enter name")
##    file.write(username+";"+password+";"+name+"\n")
##file.close()
##file = open("usernames and passwords test.txt","r")
##for line in file:
##  parts = line.split(";")
##  username = parts[0]
##  password = parts[1]
##  name = parts[2]
##  print(username+password+name)
##  print(parts)
##file.close()


##pet_type="dog"
##pet_colour="green"
##pet_name="vicky"
##username1="vicky"
##with open("test.txt", "r+") as f:
##    d = f.readlines()
##    f.seek(0)
##    for line in f:
##        if line.startswith(username1):
##            f.write(line+";"+pet_type+";"+pet_colour+";"+pet_name)
##    f.truncate()

global valid
valid=True
symbols=["#","£","&","@","$"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
password="passwor"
def password_validator():
    if len(password)<8:
        print("Enter a password with 8 or more characters")
        valid=False
        print(valid)
    if not any(char in symbols for char in password):
        print('Enter a password with a symbol (£&@$#)')
    if not any(char in numbers for char in password):
        print('Enter a password with a number')
    if not any(char.isupper() for char in password):
        print('Enter a password with a uppercase character')
    if not any(char.islower() for char in password):
        print('Enter a password with a lowercase character')
password_validator()
