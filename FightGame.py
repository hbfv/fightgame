#V0.2
import random
import tkinter

###############################################
#MAIN MENU WINDOW
def boxer():
    global cclass
    cclass="boxer"
    menu.destroy()
    gameplay()
def kickboxer():
    global cclass
    cclass="kickboxer"
    menu.destroy()
    gameplay()
def wrestler():
    global cclass
    cclass="wrestler"
    menu.destroy()
    gameplay()

menu=tkinter.Tk()
menu.title("Fight Game - Menu")
menu.geometry("300x300")
menu.configure(background="#7F0404", cursor="dot")
title=tkinter.Label(menu, text="Fight Game", font=("Courier", 28, "bold"), pady=20,bg="#7F0404", fg="white")
boxer=tkinter.Button(menu, text="Boxer", command=boxer, pady=20, width=100)
kickboxer=tkinter.Button(menu, text="Kick Boxer",command=kickboxer, pady=20, width=100)
wrestler=tkinter.Button(menu, text="Wrestler",command=wrestler, pady=20, width=100)
title.pack()
boxer.pack()
kickboxer.pack()
wrestler.pack()

###############################################


###############################################
#GAME WINDOW
def gameplay():
    window=tkinter.Tk()
    window.title("Fight Game - Playing")
    window.geometry("640x480")
    window.configure(background="#7F0404", cursor="dot")
    global health
    global cclass
    if cclass=="boxer":
        pmodifier=1.5
        kmodifier=0.5
        gmodifier=0.25
        health=125
    elif cclass=="kickboxer":
        pmodifier=0.75
        kmodifier=1.5
        gmodifier=0.25
        health=125
    elif cclass=="wrestler":
        pmodifier=0.5
        kmodifier=0.5
        gmodifier=2
        health=175

    global ehealth
    ehealth=health*1.25
    global emodifier
    emodifier=1.4

    global pwin
    pwin=0

    def pwin():
        global ehealth
        if ehealth<=0:
            print("Player has won")
            global pwin
            pwin=1

    def ewin():
        global health
        if health<=0:
            print("Enemy has won")
            global pwin
            pwin=1

    def echance():
        global pwin
        if pwin!=1:
            global health
            echance=random.randint(0,13)
            if echance>=5:
                global ehealth
                health-=random.randint(10,20)*emodifier
                print("Player health is now: "+str(health))
                healthl.configure(text="Health: "+str(health))
            elif echance<=4:
                chance=1
                while chance<7:
                    health-=random.randint(2,7)*emodifier
                    chance=random.randint(0,11)
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(health))
            elif echance>=11:
                print("Enemy attack missed!")

    def punchp():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=11:
                print("Player attack missed!")
            else:
                ehealth-=random.randint(10,20)*pmodifier
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(ehealth))
            pwin()
            echance()
            ewin()


    def kickp():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=11:
                print("Player attack missed!")
            else:    
                ehealth-=random.randint(10,20)*kmodifier
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(ehealth))
            pwin()
            echance()
            ewin()

    def grapplep():
        if pwin!=1:
            global ehealth
            chance=1
            while chance<7:
                ehealth-=random.randint(2,7)*gmodifier
                chance=random.randint(0,11)
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(ehealth))
            pwin()
            echance()
            ewin()
		
    player=tkinter.Label(window, text="Player", font=("Courier", 24, "bold"))
    healthl=tkinter.Label(window, text=("Health: "+str(health)), font=("Courier", 18))
    enemy=tkinter.Label(window, text="Enemy", font=("Courier", 24, "bold"))
    ehealthl=tkinter.Label(window, text=("Health: "+str(ehealth)), font=("Courier", 18))
    punch=tkinter.Button(window, text="Punch",command=punchp)
    kick=tkinter.Button(window, text="Kick", command =kickp)
    grapple=tkinter.Button(window, text="Grapple", command=grapplep)

###############################################
#LOAD INTO GAME WINDOW
    player.pack(pady=10, padx=20, fill=tkinter.X)
    healthl.pack()
    punch.pack(pady=5)
    kick.pack(pady=5)
    grapple.pack(pady=5)
    enemy.pack(pady=10, padx=20, fill=tkinter.X)
    ehealthl.pack()

###############################################
    window.mainloop()
