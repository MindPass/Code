import sqlite3
import sys

sys.path.append('../fenetres/')
from functools import partial
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from fenetreGestion import Ui_fenetreGestion

bdd = "../../../Traitement_mails/bdd.sq3"

def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")

class LineEditWithFocusOut(QtWidgets.QLineEdit):
    """docstring for LineEditWithFocusOut"""

    def focusOutEvent(self, arg):
        QtWidgets.QLineEdit.focusOutEvent(self, arg)
        # self.id contient l'id de la LigneEdit, ajouté dans afficher_ligne_site()
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("UPDATE sites_reconnus SET identifiant=? WHERE rowid=?", (self.text(), self.id+1))
        conn.commit()
        cur.close()
        conn.close()

        if self.text() == "":
            self.setPlaceholderText("Ajouter un pseudo")
        

class ClasseGestion(Ui_fenetreGestion):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        self.ajouter_cat.setPlaceholderText("Ajouter une catégorie")
        self.ajouter_pwd.setPlaceholderText("Ajouter un mot de passe")
        self.ajouter_cat.returnPressed.connect(self.check_if_exist_cat)
        self.ajouter_pwd.returnPressed.connect(self.check_if_exist_pwd)

        self.sites = []
        self.lignes_cat = []
        self.pwds = []

    def lancement(self):
        self.afficher_sites()
        self.afficher_categories()
        self.afficher_pwds()

    # CATEGORIES 
 
    def check_if_exist_cat(self):
        """
        Vérifier que la catégorie en question n'est pas déjà dans la base de donnée
        """
        if self.ajouter_cat.displayText() != "":
            conn = sqlite3.connect(bdd)
            cur = conn.cursor()

            cur.execute("SELECT nom_categorie FROM categories WHERE nom_categorie=?", (self.ajouter_cat.displayText(),))
            categories_table = cur.fetchall()

            conn.commit()
            cur.close()
            conn.close()

            conditions = not categories_table or categories_table[0][0] != self.ajouter_cat.displayText()
            if conditions:
                self.ajouter_categorie()

    def afficher_categories(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('SELECT nom_categorie FROM categories')
        tab = cur.fetchall()

        if tab:
            for k in range(len(tab)):
                self.ajouter_ligne_categorie(k, tab[k][0])

        conn.commit()
        cur.close() 
        conn.close()

    def ajouter_ligne_categorie(self, y, nom_categorie):
        self.lignes_cat.append({'ligne_categorie': QtWidgets.QHBoxLayout()})
        self.lignes_cat[y]['ligne_categorie'].setObjectName("ligne_categorie")
        self.lignes_cat[y]['label_cat'] = QtWidgets.QLabel(self.scrollAreaWidgetContents_cat)
        self.lignes_cat[y]['label_cat'].setMaximumSize(QtCore.QSize(16777215, 608))
        self.lignes_cat[y]['label_cat'].setObjectName("label_cat")
        self.lignes_cat[y]['label_cat'].setText(nom_categorie)
        self.lignes_cat[y]['ligne_categorie'].addWidget(self.lignes_cat[y]['label_cat'])
        self.lignes_cat[y]['pushButton_cat'] = QtWidgets.QPushButton(self.scrollAreaWidgetContents_cat)
        self.lignes_cat[y]['pushButton_cat'].setEnabled(True)
        self.lignes_cat[y]['pushButton_cat'].setObjectName("pushButton_cat")
        self.lignes_cat[y]['pushButton_cat'].setText('X')
        self.lignes_cat[y]['ligne_categorie'].addWidget(self.lignes_cat[y]['pushButton_cat'])
        self.verticalLayout_3.addLayout(self.lignes_cat[y]['ligne_categorie'])

        # On garde l'alignement haut
        self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop)

        # Evenement quand le boutton de suppression est cliqué
        self.lignes_cat[y]["pushButton_cat"].clicked.connect(partial(self.supprimer_cat, y=y))

    def ajouter_categorie(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("INSERT INTO categories (nom_categorie) VALUES(?)", (self.ajouter_cat.displayText(),))
        conn.commit()
        cur.close()
        conn.close()

        # ajout de la catégorie dans la scrollArea Categories        
        self.ajouter_ligne_categorie(len(self.lignes_cat), self.ajouter_cat.displayText())
        print("Catégorie ajoutée : ")

        # ajout de la catégorie dans les comboBox
        for y in range(len(self.sites)):
            self.sites[y]['categorie'].addItem(self.ajouter_cat.displayText())

        self.ajouter_cat.setText("")

    def supprimer_cat(self, y):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("DELETE FROM categories WHERE nom_categorie=?", (self.lignes_cat[y]["label_cat"].text(),))
        conn.commit()
        cur.close()
        conn.close()

        print("Suppression de " + str(self.lignes_cat[y]["label_cat"].text()))

        # suppression des items dans les ComboBox
        for k in range(len(self.sites)):
            if self.sites[k]['categorie'].currentText() == self.lignes_cat[y]['label_cat'].text():
                # si la catégorie supprimée était celle du site, alors on change la catégorie de celui-ci en le choix vide:""
                if self.sites[k]['categorie'].findText("") == -1:
                    # si il n'y a pas le choix vide "", on l'ajoute
                    self.sites[k]['categorie'].addItem("")
                self.sites[k]['categorie'].setCurrentIndex(self.sites[k]['categorie'].findText(""))
            index = self.sites[k]['categorie'].findText(self.lignes_cat[y]["label_cat"].text())
            self.sites[k]['categorie'].removeItem(index)

        # destruction des layouts dans la scroll_area
        self.scrollAreaWidgetContents_cat.deleteLater()
        # on vide les attributs
        self.lignes_cat = []
        # On en recrée un vide
        self.scrollAreaWidgetContents_cat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_cat.setGeometry(QtCore.QRect(0, 0, 177, 767))
        self.scrollAreaWidgetContents_cat.setObjectName("scrollAreaWidgetContents_cat")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_cat)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_cat.setWidget(self.scrollAreaWidgetContents_cat)
        # on relance la méthode d'affichage des catégories
        self.afficher_categories()

        # PASSWORD
 
    def afficher_combo_cat(self, y):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('SELECT nom_categorie FROM categories')
        tab = cur.fetchall()
        result = []
        for k in range(len(tab)):
            result.append(tab[k][0])
        cur.execute('SELECT categorie FROM sites_reconnus WHERE rowid=?', (y + 1,))
        cat_ligne = cur.fetchall()[0][0]

        if cat_ligne and (cat_ligne in result):
            self.sites[y]['categorie'].addItem(cat_ligne)
            for nom_categorie in result:
                if nom_categorie != cat_ligne:
                    self.sites[y]['categorie'].addItem(nom_categorie)
            self.sites[y]['categorie'].addItem("")
        else:
            self.sites[y]['categorie'].addItem("")
            for nom_categorie in result:
                self.sites[y]['categorie'].addItem(nom_categorie)
        cur.close()
        conn.close()
   
    def cat_changement(self, y):

        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('UPDATE sites_reconnus SET categorie=? WHERE rowid=?',
                    (self.sites[y]['categorie'].currentText(), y + 1))

        print("Catégorie changée en"+ str(self.sites[y]['categorie'].currentText()))
        conn.commit()
        cur.close()
        conn.close()

    # PASSWORDS

    def check_if_exist_pwd(self):
        """
        Vérifier que le pwd en question n'est pas déjà dans la base de donnée
        """
        if self.ajouter_pwd.displayText() != "":
            conn = sqlite3.connect(bdd)
            cur = conn.cursor()

            cur.execute("SELECT mdp FROM mdps WHERE mdp=?", (self.ajouter_pwd.displayText(),))
            pwds_table = cur.fetchall()

            conn.commit()
            cur.close()
            conn.close()

            conditions = not pwds_table or pwds_table[0][0] != self.ajouter_pwd.displayText()
            if conditions:
                self.ajouter_password()

    def afficher_pwds(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('SELECT mdp FROM mdps')
        tab = cur.fetchall()

        if tab:
            for k in range(len(tab)):
                self.ajouter_ligne_pwd(k, tab[k][0])

        conn.commit()
        cur.close()
        conn.close()

    def ajouter_ligne_pwd(self, y, nom_categorie):
        self.pwds.append({'ligne_pwd': QtWidgets.QHBoxLayout()})
        self.pwds[y]['ligne_pwd'].setObjectName("ligne_pwd")
        self.pwds[y]['label_pwd'] = QtWidgets.QLabel(self.scrollAreaWidgetContents_pwd)
        self.pwds[y]['label_pwd'].setMaximumSize(QtCore.QSize(16777215, 608))
        self.pwds[y]['label_pwd'].setObjectName("label_pwd")
        self.pwds[y]['label_pwd'].setText(nom_categorie)
        self.pwds[y]['ligne_pwd'].addWidget(self.pwds[y]['label_pwd'])
        self.pwds[y]['pushButton_pwd'] = QtWidgets.QPushButton(self.scrollAreaWidgetContents_pwd)
        self.pwds[y]['pushButton_pwd'].setEnabled(True)
        self.pwds[y]['pushButton_pwd'].setObjectName("pushButton_pwd")
        self.pwds[y]['pushButton_pwd'].setText('X')
        self.pwds[y]['ligne_pwd'].addWidget(self.pwds[y]['pushButton_pwd'])
        self.verticalLayout_2.addLayout(self.pwds[y]['ligne_pwd'])

        # On garde l'alignement haut
        self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)

        # Evenement quand le boutton de suppression est cliqué
        self.pwds[y]["pushButton_pwd"].clicked.connect(partial(self.supprimer_password, y=y))

    def ajouter_password(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("INSERT INTO mdps (mdp) VALUES(?)", (self.ajouter_pwd.displayText(),))
        conn.commit()
        cur.close()
        conn.close()

        # ajout dans la ScrollArea Passwords
        self.ajouter_ligne_pwd(len(self.pwds), self.ajouter_pwd.displayText())
        print("Password ajoutée : " + self.ajouter_pwd.displayText())

        # ajout du mdp dans les comboBox
        for y in range(len(self.sites)):
            self.sites[y]['mdp'].addItem(self.ajouter_pwd.displayText())

        self.ajouter_pwd.setText("")

    def afficher_combo_pwd(self, y):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('SELECT mdp FROM mdps')
        tab = cur.fetchall()
        result = []
        for k in range(len(tab)):
            result.append(tab[k][0])
        cur.execute('SELECT mdp FROM sites_reconnus WHERE rowid=?', (y + 1,))
        pwd_ligne = cur.fetchall()[0][0]

        if pwd_ligne and (pwd_ligne in result):
            self.sites[y]['mdp'].addItem(pwd_ligne)
            for nom_pwd in result:
                if nom_pwd != pwd_ligne:
                    self.sites[y]['mdp'].addItem(nom_pwd)
            self.sites[y]['mdp'].addItem("")
        else:
            self.sites[y]['mdp'].addItem("")
            for nom_pwd in result:
                self.sites[y]['mdp'].addItem(nom_pwd)
        cur.close()
        conn.close()

    def supprimer_password(self, y):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("DELETE FROM mdps WHERE mdp=?", (self.pwds[y]["label_pwd"].text(),))
        conn.commit()
        cur.close()
        conn.close()

        print("Suppression du Password: " + str(self.pwds[y]["label_pwd"].text()))

        # suppression des items dans les ComboBox
        for k in range(len(self.sites)):
            if self.sites[k]['mdp'].currentText() == self.pwds[y]['label_pwd'].text():
                # si la catégorie supprimée était celle du site, alors on change la catégorie de celui-ci en le choix vide:""
                if self.sites[k]['mdp'].findText("") == -1:
                    # si il n'y a pas le choix vide "", on l'ajoute
                    self.sites[k]['mdp'].addItem("")
                self.sites[k]['mdp'].setCurrentIndex(self.sites[k]['mdp'].findText(""))
            index = self.sites[k]['mdp'].findText(self.pwds[y]["label_pwd"].text())
            self.sites[k]['mdp'].removeItem(index)

        # destruction des layouts dans la scroll_area
        self.scrollAreaWidgetContents_pwd.deleteLater()
        # on vide les attributs
        self.pwds = []
        # On en recrée un vide
        self.scrollAreaWidgetContents_pwd = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_pwd.setGeometry(QtCore.QRect(0, 0, 177, 767))
        self.scrollAreaWidgetContents_pwd.setObjectName("scrollAreaWidgetContents_pwd")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_pwd)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_pwd.setWidget(self.scrollAreaWidgetContents_pwd)

        self.afficher_pwds()

    def pwd_changement(self, y):

        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('UPDATE sites_reconnus SET mdp=? WHERE rowid=?',
                    (self.sites[y]['mdp'].currentText(), y + 1))

        print("Pwd changée en"+ str(self.sites[y]['mdp'].currentText()))
        conn.commit()
        cur.close()
        conn.close()

    # SITES

    def afficher_sites(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('SELECT site_web, identifiant, mdp, categorie FROM sites_reconnus')
        tab = cur.fetchall()

        for k in range(len(tab)):
            self.ajouter_ligne_site(k, tab[k][0], tab[k][1], tab[k][2], tab[k][3])

        conn.commit()
        cur.close()
        conn.close()

    def ajouter_ligne_site(self, y, site_web, identifiant, mdp, categorie):
        self.sites.append({'ligne_site': QtWidgets.QHBoxLayout()})
        self.sites[y]['ligne_site'] = QtWidgets.QHBoxLayout()
        self.sites[y]['ligne_site'].setObjectName("ligne_site")
        self.sites[y]['site_web'] = QtWidgets.QLabel(self.scrollAreaWidgetContents_sites)
        self.sites[y]['site_web'].setAlignment(QtCore.Qt.AlignCenter)
        self.sites[y]['site_web'].setObjectName("site_web")
        self.sites[y]['site_web'].setText(site_web)
        self.sites[y]['ligne_site'].addWidget(self.sites[y]['site_web'])

        self.sites[y]['identifiant'] = LineEditWithFocusOut(self.scrollAreaWidgetContents_sites)
        self.sites[y]['identifiant'].setAlignment(QtCore.Qt.AlignCenter)
        self.sites[y]['identifiant'].setObjectName('identifiant')
        self.sites[y]['identifiant'].id = y # On définit une id pour cet objet


        if identifiant is None or identifiant == "":
            self.sites[y]['identifiant'].setPlaceholderText("Ajouter un pseudo")
        else:
            self.sites[y]['identifiant'].setText(identifiant)

        # Event filter pour les identifiants
        # QtWidgets.QWidget.focusOutEvent(self.sites[y]["identifiant"], self.print_)
        #self.sites[y]["identifiant"].installEventFilter(event)
        self.sites[y]['ligne_site'].addWidget(self.sites[y]['identifiant'])

        self.sites[y]['mdp'] = QtWidgets.QComboBox(self.scrollAreaWidgetContents_sites)
        self.sites[y]['mdp'].setObjectName("mdp")
        self.afficher_combo_pwd(y) # affichage des éléments de la combobox en fonction de la bdd
        self.sites[y]['ligne_site'].addWidget(self.sites[y]['mdp'])
        self.sites[y]['categorie'] = QtWidgets.QComboBox(self.scrollAreaWidgetContents_sites)
        self.sites[y]['categorie'].setObjectName("categorie")
        self.afficher_combo_cat(y)  # affichage des éléments de la combobox en fonction de la bdd
        self.sites[y]['ligne_site'].addWidget(self.sites[y]['categorie'])
        self.sites[y]['ligne_site'].setStretch(0, 2)
        self.sites[y]['ligne_site'].setStretch(1, 2)
        self.sites[y]['ligne_site'].setStretch(2, 2)
        self.sites[y]['ligne_site'].setStretch(3, 2)
        self.verticalLayout.addLayout(self.sites[y]['ligne_site'])

        # Changement de pwd/catégories
        self.sites[y]['categorie'].currentIndexChanged.connect(partial(self.cat_changement, y=y))
        self.sites[y]['mdp'].currentIndexChanged.connect(partial(self.pwd_changement, y=y))

 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()

    classGestion = ClasseGestion(fenetreGestion)

    fenetreGestion.show()
    sys.exit(app.exec_())
