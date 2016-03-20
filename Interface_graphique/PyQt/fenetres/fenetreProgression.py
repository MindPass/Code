# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/fenetreProgression.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fenetreProgression(object):
    def setupUi(self, fenetreProgression):
        fenetreProgression.setObjectName("fenetreProgression")
        fenetreProgression.setWindowModality(QtCore.Qt.WindowModal)
        fenetreProgression.setEnabled(True)
        fenetreProgression.resize(855, 542)
        fenetreProgression.setMinimumSize(QtCore.QSize(0, 0))
        fenetreProgression.setMaximumSize(QtCore.QSize(1011, 645))
        fenetreProgression.setStyleSheet("")
        self.verticalLayoutWidget = QtWidgets.QWidget(fenetreProgression)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 831, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setAccessibleName("")
        self.progressBar.setStyleSheet("QProgressBar {\n"
"background-color: lightgrey;\n"
"border: 2px solid purple;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.flecheGauche = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.flecheGauche.setObjectName("flecheGauche")
        self.horizontalLayout.addWidget(self.flecheGauche)
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(779, 536))
        self.frame.setMaximumSize(QtCore.QSize(779, 536))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.flecheDroite = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.flecheDroite.setObjectName("flecheDroite")
        self.horizontalLayout.addWidget(self.flecheDroite)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 100)
        self.horizontalLayout.setStretch(2, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(fenetreProgression)
        QtCore.QMetaObject.connectSlotsByName(fenetreProgression)

    def retranslateUi(self, fenetreProgression):
        _translate = QtCore.QCoreApplication.translate
        fenetreProgression.setWindowTitle(_translate("fenetreProgression", "Progression"))
        self.progressBar.setFormat(_translate("fenetreProgression", "%p%"))
        self.flecheGauche.setText(_translate("fenetreProgression", "flecheGauche"))
        self.flecheDroite.setText(_translate("fenetreProgression", "flecheDroite"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreProgression = QtWidgets.QWidget()
    ui = Ui_fenetreProgression()
    ui.setupUi(fenetreProgression)
    fenetreProgression.show()
    sys.exit(app.exec_())

