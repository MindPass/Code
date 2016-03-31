from tkinter import *


liste_test = ['facebook.com', 'twitter.com', 'lequipe.fr', 'eurosport.com', 'jaiplusdidee.fr']


# Disparition du texte dans les entrées quand clic il y a
firstclickID, firstclickMDP = True, True
def on_entry_click_ID(event):
    """function that gets called whenever entry1 is clicked"""        
    global firstclickID
    if firstclickID: # if this is the first time they clicked it
        firstclickID = False
        ID.delete(0, "end") # delete all the text in the entry
def on_entry_click_MDP(event):
    """function that gets called whenever entry1 is clicked"""        
    global firstclickMDP
    if firstclickMDP: # if this is the first time they clicked it
        firstclickMDP = False
        MDP.delete(0, "end") # delete all the text in the entry

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Bienvenue sur MindPass')
Mafenetre['bg']='lightblue' # couleur de fond

photo = PhotoImage(file="LogoMindPass.png")

canvas = Canvas(Mafenetre,width=3000, height=445, bg="lightblue")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()


# non fonctionnelle pour l'instant
scrollbar = Scrollbar(Mafenetre)
scrollbar.pack(side = RIGHT, fill=Y )

for i in range(len(liste_test)):
    if i%2==0:
        frameConteneur = Frame(Mafenetre,bg="#eaeaea",borderwidth=0)
    else:
        frameConteneur = Frame(Mafenetre,bg="#f6f6f6",borderwidth=0)
    frameConteneur.pack(side=TOP,fill=X)
    frameOublier = Frame(frameConteneur)
    frameOublier.pack(side=LEFT)
    frameAdresse = Frame(frameConteneur,bg="white",borderwidth=0,relief=FLAT)
    frameAdresse.pack(side=LEFT,padx=20,pady=5)
    frameID = Frame(frameConteneur,bg="white",borderwidth=2,relief=FLAT)
    frameID.pack(side=LEFT,padx=20,pady=5)
    frameMDP = Frame(frameConteneur,bg="white",borderwidth=2,relief=FLAT)
    frameMDP.pack(side=LEFT,padx=20,pady=5)

    Button(frameOublier,text="X",fg='navy',command=frameConteneur.destroy).pack(padx=10,pady=5,side=LEFT)
    
    Label(frameAdresse,text="www.{}".format(liste_test[i]), fg="black", width=30).pack(side=LEFT)
    
    ID=Entry(frameID,text="Identifiant", fg="#bbb", bg="white", borderwidth=0)
    ID.bind('<FocusIn>', on_entry_click_ID)
    ID.pack(padx=10,side=LEFT)
    
    MDP=Entry(frameMDP,text="Mot de Passe", fg="#bbb", bg="white", borderwidth=0) # ajouter <<<show="*">>> pour ne pas voir les caractères saisis
    MDP.bind('<FocusIn>', on_entry_click_MDP)
    MDP.pack(padx=10,side=LEFT)

ID.insert(0, "Identifiant")
MDP.insert(0, "Mot de passe")

Mafenetre.state('zoomed') # Page affichée en plein écran

Mafenetre.mainloop()