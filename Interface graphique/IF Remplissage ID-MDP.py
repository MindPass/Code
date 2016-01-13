from tkinter import *

# Disparition du texte dans les entrées quand clic il y a
firstclick = True

def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""        
    global firstclick

    if firstclick: # if this is the first time they clicked it
        firstclick = False
        ID.delete(0, "end") # delete all the text in the entry
        MDP.delete(0, "end") # delete all the text in the entry


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Bienvenue sur MindPass :)')
Mafenetre['bg']='lightblue' # couleur de fond

frameConteneur = Frame(Mafenetre,borderwidth=0)
frameConteneur.pack(side=LEFT,padx=10,pady=5,fill=X)

frameOublier = Frame(frameConteneur)
frameOublier.pack(side=LEFT,padx=10,pady=5)
frameAdresse = Frame(frameConteneur,bg="red",borderwidth=2,relief=GROOVE)
frameAdresse.pack(side=LEFT,padx=10,pady=5)
frameID = Frame(frameConteneur,bg="blue",borderwidth=2,relief=GROOVE)
frameID.pack(side=LEFT,padx=10,pady=5)
frameMDP = Frame(frameConteneur,bg="green",borderwidth=2,relief=GROOVE)
frameMDP.pack(side=LEFT,padx=10,pady=5)

Button(frameOublier,text="X",fg='navy',command=frameConteneur.destroy).pack(padx=10,pady=5,side=LEFT)
Label(frameAdresse,text="facebook.com", fg="black", bg="red").pack(padx=10,side=LEFT)

ID=Entry(frameID,text="Identifiant", fg="lightgrey", bg="blue")
ID.insert(0, "Identifiant")
ID.bind('<FocusIn>', on_entry_click)
ID.pack(padx=10,side=LEFT)

MDP=Entry(frameMDP,text="Mot de Passe", fg="lightgrey", bg="green", show="*")
MDP.insert(0, "Mot de passe")
MDP.bind('<FocusIn>', on_entry_click)
MDP.pack(padx=10,side=LEFT)

Mafenetre.state('zoomed') # Page plein écran

Mafenetre.mainloop()