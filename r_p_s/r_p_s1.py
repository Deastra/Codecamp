import random
import tkinter


win=tkinter.Tk()
win.geometry("900x400")
win.config(bg="black")

rock=tkinter.PhotoImage(file="rr.gif")
paper=tkinter.PhotoImage(file="pp.gif")
scissors=tkinter.PhotoImage(file="ss.gif")
#####################################
rock1=tkinter.PhotoImage(file="rr1.gif")
paper1=tkinter.PhotoImage(file="pp1.gif")
scissors1=tkinter.PhotoImage(file="ss1.gif")

def game(user_choise):
    l=["rock",'paper','scissors',"rock",'paper','scissors']
    l=l*3

    l_check=['scissors',"rock",'paper','scissors','rock']

    comp_choise=random.choice(l)

    
    draw=0
    
    for i in range(1,len(l_check)-1):
        if comp_choise==l_check[i] and user_choise==l_check[i+1]:

            l_mark=tkinter.Label(win,text=">",font="50",background="white")
            l_mark.place(x=350,y=130,width=100,height=200)
            
            l_round=tkinter.Label(win,text="User won the round!",font="15",background="green",fg="white")
            l_round.place(x=290,y=340,width=230,height=50)

            draw=1
            break
            
        elif comp_choise==l_check[i] and user_choise==l_check[i-1]:

            l_mark=tkinter.Label(win,text="<",font="50",background="white")
            l_mark.place(x=350,y=130,width=100,height=200)
            
            l_round=tkinter.Label(win,text="Computer won the round!",font="15",background="red",fg="white")
            l_round.place(x=290,y=340,width=230,height=50)
            
            draw=1
            break
        
    if draw==0:
        l_mark=tkinter.Label(win,text="=",font="50",background="white")
        l_mark.place(x=350,y=130,width=100,height=200)
        
        l_round=tkinter.Label(win,text="Draw Round!",font="15",background="blue",fg="white")
        l_round.place(x=290,y=340,width=230,height=50)

    if comp_choise=="scissors":
        l_comp=tkinter.Label(win,image=scissors1,background="white")
        l_comp.image=scissors1
        l_comp.place(x=450,y=130,width=200,height=200)
    elif comp_choise =="rock":
        l_comp=tkinter.Label(win,image=rock1,background="white")
        l_comp.image=rock1
        l_comp.place(x=450,y=130,width=200,height=200)
    elif comp_choise =="paper":
        l_comp=tkinter.Label(win,image=paper1,background="white")
        l_comp.image=paper1
        l_comp.place(x=450,y=130,width=200,height=200)
        


def scissor_f():
    l_user=tkinter.Label(win,image=scissors,background="white")
    l_user.image=scissors
    l_user.place(x=150,y=130,width=200,height=200)

    user_choise="scissors"
    game(user_choise)

def rock_f():
    l_user=tkinter.Label(win,image=rock,background="white")
    l_user.image=scissors
    l_user.place(x=150,y=130,width=200,height=200)

    user_choise="rock"
    game(user_choise)
    
def paper_f():
    l_user=tkinter.Label(win,image=paper,background="white")
    l_user.image=scissors
    l_user.place(x=150,y=130,width=200,height=200)

    user_choise="paper"
    game(user_choise)


###############################


rock_b=tkinter.Button(win,text="rock",command=rock_f,fg="red",background="aqua",activebackground="yellow",font='12')
rock_b.place(x=150,y=0,width=100,height=50)

paper_b=tkinter.Button(win,text="paper",command=paper_f,fg="red",background="aqua",activebackground="yellow",font='12')
paper_b.place(x=350,y=0,width=100,height=50)

scissor_b=tkinter.Button(win,text="scissors",command=scissor_f,fg="red",background="aqua",activebackground="yellow",font='12')
scissor_b.place(x=550,y=0,width=100,height=50)

quit_b=tkinter.Button(win,text="Quit",command=win.destroy,fg="crimson",background="blue",activebackground="red",font='12')
quit_b.place(x=800,y=0,width=80,height=50)


win.mainloop()













