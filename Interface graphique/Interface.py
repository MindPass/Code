import poplib, getpass
from tkinter import *

fenetre = Tk()

champ_label = Label(fenetre, text="MindPass")
champ_label.pack()
champ_label = Label(fenetre, text="")
champ_label.pack()
champ_label = Label(fenetre, text="Login :")
champ_label.pack()

def connexion():

    M = poplib.POP3_SSL('pop.laposte.net')
 
    #Login to mail server
    M.user(login.get())
    #M.user(getpass.getuser())

    M.pass_(code.get())
    #M.pass_(getpass.getpass()) 

 
    #print 'Vous avez' + str(nbMessages) + "messages." 
    #print "Message List:"
 
    #Liste le sujet de chaque message

    #Nombre de messages à obtenir
    numMessages = len(M.list()[1])
    for i in range(numMessages):
        for j in M.retr(i+1)[1]:
            print(j)

    M.quit()
    
    

login = StringVar()
ligne_texte = Entry(fenetre, textvariable=login, width=30)
ligne_texte.pack()

champ_label = Label(fenetre, text="Password :")
champ_label.pack()

code = StringVar()
ligne_texte = Entry(fenetre, textvariable=code, show='*', width=30)
ligne_texte.pack()

bouton=Button(fenetre, text="Connexion", command=connexion)
bouton.pack()

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()

fenetre.mainloop()
