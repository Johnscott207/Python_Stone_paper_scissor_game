import random
"""
### Algorithm of Stone Paper Scissor Game
item = ["Stone","Paper","Scissor"]
while True:
    i = input("Press R \n")
    if(i=="r"):
        c= random.choice(item)
        u= random.choice(item)
        if(c=="Stone" and u=="Scissor") or (c=="Paper" and u=="Stone") or (c=="Scissor" and u=="Paper"):
            print(f"Computer {c} > {u} User You \n are Loser!")
        elif c==u:
            print(f"Computer {c} == {u} User \n Match Draw")
        else:
            print(f"Computer {c} > {u} User \n You are Win!")
    if(i=="e"):
        break
"""
item = ["Stone","Paper","Scissor"]
cnum = 0
count = 0
def ran():
    global cnum, count
    if cnum == 0:
        can.itemconfig(image_container,image=img)
        can2.itemconfig(image_container2,image=img3)
    elif cnum == 1:
        can.itemconfig(image_container,image=img2)
        can2.itemconfig(image_container2,image=img)
    elif cnum == 2:
        can.itemconfig(image_container,image=img3)
        can2.itemconfig(image_container2,image=img2)
    cnum = cnum + 1
    if cnum > 2:cnum = 0
    count = count + 1
    if(count > 50):
        count = 0
        cnum = 0
        results()
    else:
        l3.configure(text="")
        l3.configure(foreground = 'black')  

        tim = Timer(0.05,ran)
        tim.start()

def results():
    c= random.choice(item)
    u= random.choice(item)
    can.itemconfig(image_container,image=dir[c])
    can2.itemconfig(image_container2,image=dir[u])
    if(c=="Stone" and u=="Scissor") or (c=="Paper" and u=="Stone") or (c=="Scissor" and u=="Paper"):
        print(f"Computer {c} > {u} User \n You are Loser!")
        l3.configure(text="You are Loser!")
        l3.configure(foreground = 'red')  

    elif c==u:
        print(f"Computer {c} == {u} User \n Match Draw")
        l3.configure(text="Match Draw \n Try Again")
        l3.configure(foreground = 'black')  

    else:
        print(f"Computer {c} > {u} User \n You are Win!")
        l3.configure(text="You are Win!")
        l3.configure(foreground = 'green')  

    

from tkinter import *
from PIL import ImageTk, Image
from threading import Timer
root = Tk()
root.geometry("700x500")
l1 = Label(root,width=25,font=("Arial",18), text = "Computer")
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2 = Label(root,width=20,font=("Arial",18), text = "User")
l2.grid(row = 0, column = 1, sticky = W, pady = 2)

can = Canvas(root, width = 300, height = 300)  
can.grid(row = 1, column = 0, sticky = W, pady = 2)    
can2 = Canvas(root, width = 300, height = 300)  
can2.grid(row = 1, column = 1, sticky = W, pady = 2)    

btn = Button(root,width=10,text="Play",bg='#F2B33D',command= ran)
btn.grid(row=2,column=0, pady= 2, columnspan=2)

l3 = Label(root,font=("Arial",25), text = "",foreground='#F2B33D')
l3.grid(row = 3, column = 0, pady = 20,columnspan=2)
#img = PhotoImage(file="/stone.jpg")   
img = ImageTk.PhotoImage(Image.open("scissors.jpg"))  
img2 = ImageTk.PhotoImage(Image.open("Paper.jpg"))  
img3 = ImageTk.PhotoImage(Image.open("stone.jpg"))  

image_container=can.create_image(50,50,anchor=NW, image=img)
image_container2=can2.create_image(50,50,anchor=NW, image=img)

dir = {
    "Stone":img3,
    "Paper":img2,
    "Scissor":img
}



'''
widgets are added here
'''
root.mainloop()