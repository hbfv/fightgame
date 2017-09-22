#V0.15
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
menu.configure(background="#7F0404")
boxer=tkinter.Button(menu, text="Boxer", command=boxer)
kickboxer=tkinter.Button(menu, text="Kick Boxer",command=kickboxer)
wrestler=tkinter.Button(menu, text="Wrestler",command=wrestler)
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
    window.configure(background="#7F0404")

    global cclass
    if cclass=="boxer":
        pmodifier=1.5
        kmodifier=0.5
        gmodifier=0.25
        global health
        health=125
    elif cclass=="kickboxer":
        pmodifier=0.75
        kmodifier=1.5
        gmodifier=0.25
        global health
        health=125
    elif cclass=="wrestler":
        pmodifier=0.5
        kmodifier=0.5
        gmodifier=2
        global health
        health=175

    global ehealth
    ehealth=150
    global emodifier
    emodifier=1.25

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
            echance=random.randint(0,10)
            if echance>3:
                global ehealth
                health-=random.randint(10,20)*emodifier
                print("Player health is now: "+str(health))
                healthl.configure(text="Health: "+str(health))
            elif echance<=3:
                chance=1
                while chance<7:
                    health-=random.randint(2,7)*emodifier
                    chance=random.randint(0,11)
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(health))

    def punchp():
        global pwin
        if pwin!=1:
            global ehealth
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
		
		
    player=tkinter.Label(window, text="Player")
    healthl=tkinter.Label(window, text="Health: "+str(health))
    enemy=tkinter.Label(window, text="Enemy")
    ehealthl=tkinter.Label(window, text="Health: "+str(ehealth))
    punch=tkinter.Button(window, text="Punch",command=punchp)
    kick=tkinter.Button(window, text="Kick", command =kickp)
    grapple=tkinter.Button(window, text="Grapple", command=grapplep)

###############################################
#LOAD INTO GAME WINDOW
    player.pack()
    healthl.pack()
    punch.pack()
    kick.pack()
    grapple.pack()
    enemy.pack()
    ehealthl.pack()

###############################################
    window.mainloop()
