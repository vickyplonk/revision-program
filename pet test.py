

from tkinter import *  
from PIL import ImageTk,Image
from random import randint

root = Tk()
root.title("Pet")

canvas = Canvas(root, width = 570, height = 1000)  
canvas.pack()
canvas.configure(bg="peach puff")

clicked2="Red"
clicked1="Cat"
name="pee pee poo poo"
def created_pet():
    global pet_pic
    #if the user wants a pet
    if clicked1=="Cat":
        #what colour the user wanted
        if clicked2=="Red":
            pet_pic = ImageTk.PhotoImage(Image.open("redcat.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Orange":
            pet_pic = ImageTk.PhotoImage(Image.open("orangecat.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Yellow":
            pet_pic = ImageTk.PhotoImage(Image.open("yellowcat.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Green":
            pet_pic = ImageTk.PhotoImage(Image.open("greencat.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Blue":
            pet_pic = ImageTk.PhotoImage(Image.open("bluecat.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic)
    #if the user wants a dog
    elif clicked1=="Dog":
        #what colour the user wanted
        if clicked2=="Red":
            pet_pic = ImageTk.PhotoImage(Image.open("reddog.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Orange":
            pet_pic = ImageTk.PhotoImage(Image.open("orangedog.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Yellow":
            pet_pic = ImageTk.PhotoImage(Image.open("yellowdog.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Green":
            pet_pic = ImageTk.PhotoImage(Image.open("greendog.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Blue":
            pet_pic = ImageTk.PhotoImage(Image.open("bluedog.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic)
    #if the user wants a fish
    elif clicked1=="Fish":
        #what colour the user wanted
        if clicked2=="Red":
            pet_pic = ImageTk.PhotoImage(Image.open("redfish.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Orange":
            pet_pic = ImageTk.PhotoImage(Image.open("orangefish.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Yellow":
            pet_pic = ImageTk.PhotoImage(Image.open("yellowfish.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Green":
            pet_pic = ImageTk.PhotoImage(Image.open("greenfish.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic) 
        elif clicked2=="Blue":
            pet_pic = ImageTk.PhotoImage(Image.open("bluefish.png"))
            canvas.create_image(20,20, anchor=NW, image=pet_pic)
    #label for the pet
    pet_name = Label(canvas, text=name, bg="lavender", fg="black", font=48)
    pet_name.place(relx=0.5, rely=0.6, anchor="center")

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
    def help_guide():
        print("helpp")
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
    button_help=Button(canvas, text="Help", command=help_guide, fg="black", bg="lavender")
    button_help.place(relx=0.9,rely=0.9,anchor="center")
    
created_pet()
root.mainloop() 
