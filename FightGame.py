#V0.1
import random
import tkinter
###############################################
#MAIN MENU WINDOW
def boxer():
    cclass="boxer"
    start=1
    menu.destroy()
    gameplay()
def kickboxer():
    cclass="kickboxer"
    start=1
    menu.destroy()
    gameplay()
def wrestler():
    cclass="wrestler"
    start=1
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


#GAME WINDOW
###############################################
#GAME INITIALISATION
def gameplay():
    window=tkinter.Tk()
    window.title("Fight Game - Playing")
    window.geometry("640x480")
    window.configure(background="#7F0404")
    ###############################################
	global cclass
	if cclass="boxer":
		pmodifier=1.5
    	kmodifier=0.5
    	gmodifier=0.25
    	health=125
	elif cclass="kickboxer":
		pmodifier=0.75
		kmodifier=1.5
		gmodifier=0.25
		health=125
	elif cclass="wrestler":
		pmodifier=0.5
		kmodifier=0.5
		gmodifier=2
		health=175
		
	emodifier=1.25
	ehealth=150
	
    def punchp():
        global ehealth
        health-=random.randint(10,20)*pmodifier
        print("Enemy health is now: "+str(health))
        ehealthl.configure(text="Health: "+str(ehealth))

    def kickp():
        global ehealth
        ehealth-=random.randint(10,20)*kmodifier
        print("Enemy health is now: "+str(rhealth))
        ehealthl.configure(text="Health: "+str(ehealth))

    def grapplep():
	global ehealth
	while chance<7:
        	ehealth-=random.randint(2,7)*gmodifier
                chance=random.randint(0,11)
	        print("Enemy health is now: "+str(rhealth))
		ehealthl.configure(text="Health: "+str(ehealth))
		
		
    player=tkinter.Label(window, text="Player")
    healthl=tkinter.Label(window, text="Health: 100")
    enemy=tkinter.Label(window, text="Enemy")
    ehealthl=tkinter.Label(window, text="Health: 100")
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
