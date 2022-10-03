from tkinter import*
from tkinter.font import BOLD
import random   

win1=Tk()
win2=Toplevel()
win3=Toplevel()
win2.withdraw()
win3.withdraw()
global player_score
player_score=0
global computer_score
computer_score=0
global store
store=0

# creating windows--------------------------------------------------


def new():
    win1.withdraw()
    win2.deiconify()
    win3.withdraw()
    win2.title('New window')
    win2.geometry('850x580')
    win2.configure(bg='navajo white')
    global store
    store=0
    lf2=LabelFrame(win2,height=55,width=140)
    l5=Label(lf2,text=txt.get().upper(),font=('Arial bold',15))
    lf2.place(relx=0.33,rely=0.15,anchor=CENTER)
    l5.place(relx=0.5,rely=0.5,anchor=CENTER)

    win2.mainloop()


def new1():
    win2.withdraw()
    win3.withdraw()
    win3.deiconify()
    win3.geometry('380x300')
    l4=Label(win3,text='Your score is : '+ str(store),font=('Arial bold',17))
    l4.place(relx=0.5,rely=0.3,anchor=CENTER)

    win3.mainloop()

    
win1.title('WELCOME')
win1.geometry('460x410')
win1.configure(bg='light cyan')

def exit():
    win3.destroy()
    win2.destroy()
    win1.destroy()


# Driving code---------------------------------------------------------------

computer_gameplay = {
   '0':'Rock',
   '1':'Paper',
   '2':'Scissor',
   '3':'Lizard',
   '4':'Spock'
}

# user gameplay functions-------------------------


def rock():
    global player_score
    global computer_score
    global store
    choice=computer_gameplay[str(random.randint(0,4))]
    if choice=='Rock':
        result='Match Draw!'
    elif choice=='Scissor':
        result='You win! GO for another round!'
        player_score+=1
    elif choice=='Paper':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Lizard':
        result='You win! GO for another round!'
        player_score+=1
    elif choice=='Spock':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    l9.config(text='SCORE: '+str(player_score))
    l10.config(text='SCORE: '+str(computer_score))
    if(computer_score==3):
        store=player_score
        computer_score=0
        player_score=0
        lc1.config(text='')
        lc2.config(text='')
        label_result.config(text='')
        l9.config(text='SCORE: '+str(player_score))
        l10.config(text='SCORE: '+str(computer_score))
        new1()
    lc1.config(text='Rock')
    lc2.config(text=choice)
    label_result.config(text=result)


def paper():
    global store
    global player_score
    global computer_score
    choice=computer_gameplay[str(random.randint(0,4))]
    if choice=='Paper':
        result='Match Draw!'
    elif choice=='Rock':
        result='You win! Go for another round!'
        player_score+=1
    elif choice=='Scissor':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Lizard':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Spock':
        result='You Win! Go for another round'
        player_score+=1
    l9.config(text='SCORE: '+str(player_score))
    l10.config(text='SCORE: '+str(computer_score))
    if(computer_score==3):
        store=player_score
        computer_score=0
        player_score=0
        lc1.config(text='')
        lc2.config(text='')
        label_result.config(text='')
        l9.config(text='SCORE: '+str(player_score))
        l10.config(text='SCORE: '+str(computer_score))
        new1()
    lc1.config(text='Paper')
    lc2.config(text=choice)
    label_result.config(text=result)


def scissor():
    global store
    global player_score
    global computer_score
    choice=computer_gameplay[str(random.randint(0,4))]
    if choice=='Scissor':
        result='Match Draw!'
    elif choice=='Paper':
        result='You win! Go for another round!'
        player_score+=1
    elif choice=='Rock':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Spock':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Lizard':
        result='You Win! Go for another round'
        player_score+=1
    l9.config(text='SCORE: '+str(player_score))
    l10.config(text='SCORE: '+str(computer_score))
    if(computer_score==3):
        store=player_score
        computer_score=0
        player_score=0
        lc1.config(text='')
        lc2.config(text='')
        label_result.config(text='')
        l9.config(text='SCORE: '+str(player_score))
        l10.config(text='SCORE: '+str(computer_score))
        new1()
    lc1.config(text='Scissor')
    lc2.config(text=choice)
    label_result.config(text=result)


def lizard():
    global store
    global player_score
    global computer_score
    choice=computer_gameplay[str(random.randint(0,4))]
    if choice=='Lizard':
        result='Match Draw!'
    elif choice=='Paper':
        result='You win! Go for another round!'
        player_score+=1
    elif choice=='Scissor':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Rock':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Spock':
        result='You Win! Go for another round'
        player_score+=1
    l9.config(text='SCORE: '+str(player_score))
    l10.config(text='SCORE: '+str(computer_score))
    if(computer_score==3):
        store=player_score
        computer_score=0
        player_score=0
        lc1.config(text='')
        lc2.config(text='')
        label_result.config(text='')
        l9.config(text='SCORE: '+str(player_score))
        l10.config(text='SCORE: '+str(computer_score))
        new1()
    lc1.config(text='Lizard')
    lc2.config(text=choice)
    label_result.config(text=result)


def spock():
    global store
    global player_score
    global computer_score
    choice=computer_gameplay[str(random.randint(0,4))]
    if choice=='Spock':
        result='Match Draw!'
    elif choice=='Rock':
        result='You win! Go for another round!'
        player_score+=1
    elif choice=='Paper':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Lizard':
        computer_score+=1
        result='Computer Wins you have '+str(2-computer_score)+' lives left!'
    elif choice=='Scissor':
        result='You Win! Go for another round'
        player_score+=1
    l9.config(text='SCORE: '+str(player_score))
    l10.config(text='SCORE: '+str(computer_score))
    if(computer_score==3):
        store=player_score
        computer_score=0
        player_score=0
        lc1.config(text='')
        lc2.config(text='')
        label_result.config(text='')
        l9.config(text='SCORE: '+str(player_score))
        l10.config(text='SCORE: '+str(computer_score))
        new1()
    lc1.config(text='Spock')
    lc2.config(text=choice)
    label_result.config(text=result)




# Texts and Entry----------------

txt=Entry(win1,width=19,font=('Arial',14),bd=3)
txt.place(relx=0.71, rely=0.6, anchor=CENTER)




# images added------------------


im1=PhotoImage(file='scissors.png')
im2=im1.subsample(5,5)
im3=PhotoImage(file='player.png')
im4=im3.subsample(5,5)
im5=PhotoImage(file='computer-png-hd-45246.png')
im6=im5.subsample(2,2)
im7=PhotoImage(file='prock.png')
im8=im7.subsample(11,11)
im9=PhotoImage(file='paper.png')
im10=im9.subsample(10,10)
im11=PhotoImage(file='lizard.png')
im12=im11.subsample(11,11)
im13=PhotoImage(file='spock.png')
im14=im13.subsample(7,7)




#All Labels-------------------------


lf1=LabelFrame(win1,height=165,width=320,bg='light cyan',bd=3)
lf1.place(relx=0.5,rely=0.25,anchor=CENTER)
l0=Label(lf1,text='THE GAME OF\nCHANCES',font=('Arial bold',24),bg='light cyan')
l0.place(relx=0.5,rely=0.47,anchor=CENTER)


l1=Label(win1,text='Enter Player Name',font=('Arial bold',16),bg='light cyan')
l1.place(relx=0.24, rely=0.6, anchor=CENTER)

lf3=LabelFrame(win2,height=55,width=160)
lf3.place(relx=0.77,rely=0.15,anchor=CENTER)
l2=Label(lf3,text='COMPUTER',font=('Arial bold',15))
l2.place(relx=0.5,rely=0.5,anchor=CENTER)

l3=Label(win3,text='GAME OVER',font=('Arial bold',15))
l3.place(relx=0.5,rely=0.3,anchor=CENTER)


lf4=LabelFrame(win2,height=180,width=180,bg='black')
lf4.place(relx=0.33,rely=0.44,anchor=CENTER)
l6=Label(lf4,image=im4,bg='black')
l6.place(relx=0.5,rely=0.5,anchor=CENTER)

l7=Label(win2,text='Vs',font=('Arial bold',20))
l7.place(relx=0.55,rely=0.5,anchor=CENTER)


lf5=LabelFrame(win2,height=180,width=180)
lf5.place(relx=0.77,rely=0.44,anchor=CENTER)
l8=Label(lf5,image=im6)
l8.place(relx=0.46,rely=0.5,anchor=CENTER)


lf6=LabelFrame(win2,height=60,width=240)
lf6.place(relx=0.33,rely=0.89,anchor=CENTER)
l9=Label(lf6,text="SCORE: "+str(player_score),font=('Arial bold',14))
l9.place(relx=0.49,rely=0.5,anchor=CENTER)


lf7=LabelFrame(win2,height=60,width=240)
lf7.place(relx=0.77,rely=0.89,anchor=CENTER)
l10=Label(lf7,text="SCORE: "+ str(computer_score),font=('Arial bold',14))
l10.place(relx=0.49,rely=0.5,anchor=CENTER)


# Gameplay labels---------------------


lc1=Label(win2,text='',font=('Arial bold',13),bg='navajo white',fg='black')
lc1.place(relx=0.33,rely=0.71,anchor=CENTER)
lc2=Label(win2,text='',font=('Arial bold',13),bg='navajo white',fg='black')
lc2.place(relx=0.79,rely=0.71,anchor=CENTER)
label_result=Label(win2,text='',font=('Arial bold',15),bg='navajo white',fg='black')
label_result.place(relx=0.55,rely=0.78,anchor=CENTER)




# All buttons-----------------------------------------------


b1=Button(win1,text='PLAY',font=('Arial bold',16),command=new,bg='blue',fg='white',width=17)
b1.place(relx=0.5, rely=0.8, anchor=CENTER)

b3=Button(win3,text='PLAY\nAGAIN',font=4,width=10,command=new)
b4=Button(win3,text='EXIT',font=4,width=10,command=exit)
b3.place(relx=0.32,rely=0.66,anchor=CENTER)
b4.place(relx=0.7,rely=0.66,anchor=CENTER)

# Gameplay buttons---------------------

b5=Button(win2,text='ROCK',image=im8,width=60,compound=TOP,command=rock)
b5.place(relx=0.08,rely=0.15,anchor=CENTER)
b6=Button(win2,text='PAPER',image=im10,width=60,compound=TOP,command=paper)
b6.place(relx=0.08,rely=0.32,anchor=CENTER)
b7=Button(win2,text='SCISSORS',image=im2,width=60,compound=TOP,command=scissor)
b7.place(relx=0.08,rely=0.49,anchor=CENTER)
b8=Button(win2,text='LIZARD',image=im12,width=60,compound=TOP,command=lizard)
b8.place(relx=0.08,rely=0.66,anchor=CENTER)
b9=Button(win2,text='SPOCK',image=im14,width=60,compound=TOP,command=spock)
b9.place(relx=0.08,rely=0.83,anchor=CENTER)


win1.mainloop()