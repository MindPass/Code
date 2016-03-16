import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Interface_graphique.PyQt.fenetreGestion import Ui_fenetreGestion

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
        self.fenetre = fenetre
        self.setupUi(self.fenetre)

        self.h_layouts = []
        self.afficher_sites()

    def afficher_sites(self):
        bdd = "../../Traitement_mails/bdd.sq3"
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()

        cur.execute('SELECT site_web, identifiant, mdp, categorie FROM sites_reconnus')
        tab = cur.fetchall()

        print_(len(tab))
        print_(tab)

        for k in range(len(tab)):
            self.ajouter_ligne(k, tab[k][0], tab[k][1], tab[k][2], tab[k][3])


        conn.commit()
        cur.close()
        conn.close()

    def ajouter_ligne(self, y, site_web, identifiant, mdp, categorie):
        self.h_layouts.append({"horizontalLayoutWidget": QtWidgets.QWidget(self.scrollAreaWidgetContents)})
        self.h_layouts[y]["horizontalLayoutWidget"].setGeometry(QtCore.QRect(0, y * 80, 881, 80))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, (y+1)*80))
        self.h_layouts[y]["horizontalLayoutWidget"].setObjectName("horizontalLayoutWidget")
        self.h_layouts[y]["ligne"] = QtWidgets.QHBoxLayout(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["ligne"].setObjectName("ligne")
        self.h_layouts[y]["site_web"] = QtWidgets.QLabel(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["site_web"].setAlignment(QtCore.Qt.AlignCenter)
        self.h_layouts[y]["site_web"].setText(site_web)
        self.h_layouts[y]["site_web"].setObjectName("site_web")
        self.h_layouts[y]["ligne"].addWidget(self.h_layouts[y]["site_web"])
        self.h_layouts[y]["identifiant"] = QtWidgets.QLineEdit(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["identifiant"].setAlignment(QtCore.Qt.AlignCenter)
        self.h_layouts[y]["identifiant"].setText(identifiant)
        self.h_layouts[y]["identifiant"].setObjectName("identifiant")
        self.h_layouts[y]["ligne"].addWidget(self.h_layouts[y]["identifiant"])
        self.h_layouts[y]["mdp"] = QtWidgets.QLineEdit(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["mdp"].setAlignment(QtCore.Qt.AlignCenter)
        self.h_layouts[y]["mdp"].setText(mdp)
        self.h_layouts[y]["mdp"].setObjectName("mdp")
        self.h_layouts[y]["ligne"].addWidget(self.h_layouts[y]["mdp"])
        self.h_layouts[y]["categorie"] = QtWidgets.QCheckBox(self.h_layouts[y]["horizontalLayoutWidget"])
        self.h_layouts[y]["categorie"].setText(categorie)
        self.h_layouts[y]["categorie"].setObjectName("categorie")
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
