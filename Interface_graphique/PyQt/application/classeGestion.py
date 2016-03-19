import sqlite3
import sys
from functools import partial
sys.path.append('../fenetres/')
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


class ClasseGestion(Ui_fenetreGestion):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        self.h_layouts = []
        self.lignes_cat = []

    def lancement(self):
        self.afficher_sites()
        self.afficher_categories()
        self.ajouter_cat.setPlaceholderText("Ajouter une catégorie")
        self.ajouter_cat.returnPressed.connect(self.check_if_exist)

    def check_if_exist(self):
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
        self.lignes_cat.append({"horizontalLayoutWidget_2": QtWidgets.QWidget(self.scrollAreaWidgetContents_cat)})
        self.scrollAreaWidgetContents_cat.setMinimumSize(QtCore.QSize(0, (y + 1) * 40+10))
        self.lignes_cat[y]["horizontalLayoutWidget_2"].setGeometry(QtCore.QRect(10, y*40+10, 201, 41))
        self.lignes_cat[y]["horizontalLayoutWidget_2"].setObjectName("horizontalLayoutWidget_2")
        self.lignes_cat[y]["ligne_cat"] = QtWidgets.QHBoxLayout(self.lignes_cat[y]["horizontalLayoutWidget_2"])
        self.lignes_cat[y]["ligne_cat"].setObjectName("ligne_cat")
        self.lignes_cat[y]["label_cat"] = QtWidgets.QLabel(self.lignes_cat[y]["horizontalLayoutWidget_2"])
        self.lignes_cat[y]["label_cat"].setObjectName("label_cat")
        self.lignes_cat[y]["label_cat"].setText(nom_categorie)
        self.lignes_cat[y]["ligne_cat"].addWidget(self.lignes_cat[y]["label_cat"])
        self.lignes_cat[y]["pushButton_cat"] = QtWidgets.QPushButton(self.lignes_cat[y]["horizontalLayoutWidget_2"])
        self.lignes_cat[y]["pushButton_cat"].setEnabled(True)
        self.lignes_cat[y]["pushButton_cat"].setObjectName("pushButton_cat")
        self.lignes_cat[y]["pushButton_cat"].setText('X')
        self.lignes_cat[y]["ligne_cat"].addWidget(self.lignes_cat[y]["pushButton_cat"])
        self.lignes_cat[y]["ligne_cat"].setStretch(0, 9)
        self.lignes_cat[y]["ligne_cat"].setStretch(1, 1)

        # Affichage du layout
        self.lignes_cat[y]["horizontalLayoutWidget_2"].show()

        # Appel de la fonction supprimer_cat de paramètre y
        self.lignes_cat[y]["pushButton_cat"].clicked.connect(partial(self.supprimer_cat, y=y))

    def ajouter_categorie(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("INSERT INTO categories (nom_categorie) VALUES(?)", (self.ajouter_cat.displayText(),))
        conn.commit()
        cur.close()
        conn.close()

        print("Catégorie ajoutée : " + self.ajouter_cat.displayText())
        self.ajouter_ligne_categorie(len(self.lignes_cat), self.ajouter_cat.displayText())
        self.ajouter_cat.setText("")

    def supprimer_cat(self, y):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("DELETE FROM categories WHERE nom_categorie=?", (self.lignes_cat[y]["label_cat"].text(),))
        conn.commit()
        cur.close()
        conn.close()

        print_("Suppression de "+str(self.lignes_cat[y]["label_cat"].text()))

        # destruction des layouts dans la scroll_area
        self.scrollAreaWidgetContents_cat.deleteLater()
        # on vide les attributs
        self.lignes_cat = []
        # On en recrée un vide
        self.scrollAreaWidgetContents_cat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_cat.setGeometry(QtCore.QRect(0, 0, 219, 742))
        self.scrollAreaWidgetContents_cat.setObjectName("scrollAreaWidgetContents_cat")
        self.scrollArea_cat.setWidget(self.scrollAreaWidgetContents_cat)

        self.afficher_categories()

    def afficher_sites(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('SELECT site_web, identifiant, mdp, categorie FROM sites_reconnus')
        tab = cur.fetchall()

        for k in range(len(tab)):
            self.ajouter_ligne(k, tab[k][0], tab[k][1], tab[k][2], tab[k][3])

        conn.commit()
        cur.close()
        conn.close()

    def ajouter_ligne(self, y, site_web, identifiant, mdp, categorie):
        self.h_layouts.append({"horizontalLayoutWidget": QtWidgets.QWidget(self.scrollAreaWidgetContents)})
        self.h_layouts[y]["horizontalLayoutWidget"].setGeometry(QtCore.QRect(0, y * 80, 881, 80))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, (y + 1) * 80))
        self.h_layouts[y]["horizontalLayoutWidget"].setObjectName("horizontalLayoutWidget" + str(y))
        self.h_layouts[y]["ligne"] = QtWidgets.QHBoxLayout(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["ligne"].setObjectName("ligne" + str(y))
        self.h_layouts[y]["site_web"] = QtWidgets.QLabel(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["site_web"].setAlignment(QtCore.Qt.AlignCenter)
        self.h_layouts[y]["site_web"].setText(site_web)
        self.h_layouts[y]["site_web"].setObjectName("site_web" + str(y))
        self.h_layouts[y]["ligne"].addWidget(self.h_layouts[y]["site_web"])
        self.h_layouts[y]["identifiant"] = QtWidgets.QLineEdit(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["identifiant"].setAlignment(QtCore.Qt.AlignCenter)
        self.h_layouts[y]["identifiant"].setPlaceholderText(identifiant)
        self.h_layouts[y]["identifiant"].setObjectName("identifiant" + str(y))
        self.h_layouts[y]["ligne"].addWidget(self.h_layouts[y]["identifiant"])
        self.h_layouts[y]["mdp"] = QtWidgets.QLineEdit(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["mdp"].setAlignment(QtCore.Qt.AlignCenter)
        self.h_layouts[y]["mdp"].setPlaceholderText(mdp)
        self.h_layouts[y]["mdp"].setObjectName("mdp" + str(y))
        self.h_layouts[y]["ligne"].addWidget(self.h_layouts[y]["mdp"])
        self.h_layouts[y]["categorie"] = QtWidgets.QCheckBox(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["categorie"].setText(categorie)
        self.h_layouts[y]["categorie"].setObjectName("categorie" + str(y))
        self.h_layouts[y]["ligne"].addWidget(self.h_layouts[y]["categorie"])
        self.h_layouts[y]["ligne"].setStretch(0, 100)
        self.h_layouts[y]["ligne"].setStretch(1, 120)
        self.h_layouts[y]["ligne"].setStretch(2, 120)
        self.h_layouts[y]["ligne"].setStretch(3, 10)

        # On affiche le layout
        self.h_layouts[y]["horizontalLayoutWidget"].show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()

    classGestion = ClasseGestion(fenetreGestion)
    classGestion.lancement()

    fenetreGestion.show()
    sys.exit(app.exec_())
