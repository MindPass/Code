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


# Filtre les événements de FocusOut (ex pour une lineEdit)
class Filter(QtCore.QObject):
    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusOut:
            # do custom stuff
            print(widget)
            print(widget.text())
            print("focus out")
            # return False so that the widget will also handle the event
            # otherwise it won't focus out
            return False
        else:
            # we don't care about other events
            return False


class ClasseGestion(Ui_fenetreGestion):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        self.ajouter_cat.setPlaceholderText("Ajouter une catégorie")
        self.ajouter_cat.returnPressed.connect(self.check_if_exist)

        self.lignes_site = []
        self.lignes_cat = []
        self.lignes_pwd = []
        self._filter = Filter()

        # A mettre dans lancement()
        self.afficher_sites()
        self.afficher_categories()
        self.afficher_pwds()

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

        print("Catégorie ajoutée : " + self.ajouter_cat.displayText())
        self.ajouter_ligne_categorie(len(self.lignes_cat), self.ajouter_cat.displayText())
        self.ajouter_cat.setText("")

      ###### PASSWORD
    def afficher_pwds(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute('SELECT mdp FROM sites_reconnus')
        tab = cur.fetchall()

        if tab:
            for k in range(len(tab)):
                self.ajouter_ligne_pwd(k, tab[k][0])

        conn.commit()
        cur.close()
        conn.close()lignes_pwd

    def ajouter_ligne_pwds(self, y, nom_categorie):
        self.lignes_pwd.append({'ligne_pwd': QtWidgets.QHBoxLayout()})
        self.lignes_pwd[y]['ligne_pwd'].setObjectName("ligne_pwd")
        self.lignes_pwd[y]['label_pwd'] = QtWidgets.QLabel(self.scrollAreaWidgetContents_pwd)
        self.lignes_pwd[y]['label_pwd'].setMaximumSize(QtCore.QSize(16777215, 608))
        self.lignes_pwd[y]['label_pwd'].setObjectName("label_pwd")
        self.lignes_pwd[y]['label_pwd'].setText(nom_categorie)
        self.lignes_pwd[y]['ligne_pwd'].addWidget(self.lignes_pwd[y]['label_pwd'])
        self.lignes_pwd[y]['pushButton_pwd'] = QtWidgets.QPushButton(self.scrollAreaWidgetContents_pwd)
        self.lignes_pwd[y]['pushButton_pwd'].setEnabled(True)
        self.lignes_pwd[y]['pushButton_pwd'].setObjectName("pushButton_pwd")
        self.lignes_pwd[y]['pushButton_pwd'].setText('X')
        self.lignes_pwd[y]['ligne_pwd'].addWidget(self.lignes_pwd[y]['pushButton_pwd'])
        self.verticalLayout_2.addLayout(self.lignes_pwd[y]['ligne_pwd'])

        # On garde l'alignement haut
        self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)

        # Evenement quand le boutton de suppression est cliqué
        self.lignes_pwd[y]["pushButton_pwd"].clicked.connect(partial(self.supprimer_pwd, y=y))

    def ajouter_pwd(self):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("INSERT INTO categories (nom_categorie) VALUES(?)", (self.ajouter_cat.displayText(),))
        conn.commit()
        cur.close()
        conn.close()

        print("Catégorie ajoutée : " + self.ajouter_cat.displayText())
        self.ajouter_ligne_categorie(len(self.lignes_cat), self.ajouter_cat.displayText())
        self.ajouter_cat.setText("")


    def supprimer_pwd(self, y):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("DELETE FROM categories WHERE nom_categorie=?", (self.lignes_cat[y]["label_cat"].text(),))
        conn.commit()
        cur.close()
        conn.close()

        print("Suppression de " + str(self.lignes_cat[y]["label_cat"].text()))

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

        self.afficher_categories()


        ##### PASSWORD




    def supprimer_cat(self, y):
        conn = sqlite3.connect(bdd)
        cur = conn.cursor()
        cur.execute("DELETE FROM categories WHERE nom_categorie=?", (self.lignes_cat[y]["label_cat"].text(),))
        conn.commit()
        cur.close()
        conn.close()

        print("Suppression de " + str(self.lignes_cat[y]["label_cat"].text()))

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

        self.afficher_categories()


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
        self.lignes_site.append({'ligne_site': QtWidgets.QHBoxLayout()})
        self.lignes_site[y]['ligne_site'] = QtWidgets.QHBoxLayout()
        self.lignes_site[y]['ligne_site'].setObjectName("ligne_site")
        self.lignes_site[y]['site_web'] = QtWidgets.QLabel(self.scrollAreaWidgetContents_sites)
        self.lignes_site[y]['site_web'].setAlignment(QtCore.Qt.AlignCenter)
        self.lignes_site[y]['site_web'].setObjectName("site_web")
        self.lignes_site[y]['site_web'].setText(site_web)
        self.lignes_site[y]['ligne_site'].addWidget(self.lignes_site[y]['site_web'])
        self.lignes_site[y]['identifiant'] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_sites)
        self.lignes_site[y]['identifiant'].setAlignment(QtCore.Qt.AlignCenter)
        self.lignes_site[y]['identifiant'].setObjectName("identifiant")

        if identifiant is None:
            self.lignes_site[y]['identifiant'].setPlaceholderText("Ajouter un pseudo")
        else:
            self.lignes_site[y]['identifiant'].setText(identifiant)

        # Event filter pour les identifiants
        self.lignes_site[y]["identifiant"].installEventFilter(self._filter)

        self.lignes_site[y]['ligne_site'].addWidget(self.lignes_site[y]['identifiant'])
        self.lignes_site[y]['mdp'] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_sites)
        self.lignes_site[y]['mdp'].setMaximumSize(QtCore.QSize(16777215, 40))
        self.lignes_site[y]['mdp'].setObjectName("mdp")

        if mdp is None:
            self.lignes_site[y]['mdp'].setPlaceholderText("Ajouter un mdp")
        else:
            self.lignes_site[y]['mdp'].setText(mdp)


        self.lignes_site[y]['ligne_site'].addWidget(self.lignes_site[y]['mdp'])
        self.lignes_site[y]['categorie'] = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_sites)
        self.lignes_site[y]['categorie'].setEnabled(True)
        self.lignes_site[y]['categorie'].setText(categorie)
        self.lignes_site[y]['categorie'].setObjectName("categorie")
        self.lignes_site[y]['ligne_site'].addWidget(self.lignes_site[y]['categorie'])
        self.lignes_site[y]['ligne_site'].setStretch(0, 1)
        self.lignes_site[y]['ligne_site'].setStretch(1, 1)
        self.lignes_site[y]['ligne_site'].setStretch(2, 1)
        self.verticalLayout.addLayout(self.lignes_site[y]['ligne_site'])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()

    classGestion = ClasseGestion(fenetreGestion)

    fenetreGestion.show()
    sys.exit(app.exec_())
