import sqlite3
import sys
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
        self.label_cats = []
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
        self.label_cats = []
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
        self.label_cats.append(nom_categorie)
        self.label_cats[y] = QtWidgets.QLabel(self.scrollAreaWidgetContents_cat)
        self.scrollAreaWidgetContents_cat.setMinimumSize(QtCore.QSize(0, (y + 1)*31))
        self.label_cats[y].setGeometry(QtCore.QRect(10, y * 31, 201, 31))
        self.label_cats[y].setObjectName("label_cat" + str(y))
        self.label_cats[y].setText(nom_categorie)
        self.label_cats[y].show()

    def ajouter_categorie(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("INSERT INTO categories (nom_categorie) VALUES(?)", (self.ajouter_cat.displayText(),))
        conn.commit()
        cur.close()
        conn.close()

        print("Catégorie ajoutée : " + self.ajouter_cat.displayText())
        self.ajouter_ligne_categorie(len(self.label_cats), self.ajouter_cat.displayText())
        self.ajouter_cat.setText("")

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()

    classGestion = ClasseGestion(fenetreGestion)

    fenetreGestion.show()
    sys.exit(app.exec_())
