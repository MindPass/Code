from PyQt5 import QtWidgets
from Interface_graphique.PyQt.fenetreProgression import Ui_fenetreProgression
import time

class PageProgression(Ui_fenetreProgression):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        fenetre.show()
        self.loop(5)


    def change_bar_value(self, value):
        self.progressBar.setValue(value)
        QtWidgets.QApplication.processEvents()

    def loop(self, nbr):
        for i in range(nbr):
            ratio = int((i+1)/nbr*100)
            self.change_bar_value(ratio)
            time.sleep(1)
            QtWidgets.QApplication.processEvents()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    fenetreProgression = QtWidgets.QMainWindow()
    page_progression = PageProgression(fenetreProgression)
    sys.exit(app.exec_())
