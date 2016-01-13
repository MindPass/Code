from tkinter import *
 

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Bienvenue sur MindPass')
Mafenetre['bg']='lightblue' # couleur de fond

Frame1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
Frame1.pack(side=LEFT,padx=10,pady=5)

Button(Frame1,text="X",fg='navy',command=Frame1.destroy).pack(padx=10,pady=5,side=LEFT)
Label(Frame1,text="facebook.com", fg="black").pack(padx=10,side=LEFT)
Label(Frame1,text="Identifiant", fg="lightgrey").pack(padx=10,side=LEFT)
Label(Frame1,text="Mot de Passe", fg="lightgrey").pack(padx=10,side=LEFT)
#Button(Frame1,text="Effacer",fg='navy',command=Frame1.destroy).pack(padx=10,pady=10)

Mafenetre.state('zoomed') # Page plein écran

Mafenetre.mainloop()