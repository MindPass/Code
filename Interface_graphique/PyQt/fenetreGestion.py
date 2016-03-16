# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/fenetreGestion.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fenetreGestion(object):
    def setupUi(self, fenetreGestion):
        fenetreGestion.setObjectName("fenetreGestion")
        fenetreGestion.resize(1200, 900)
        fenetreGestion.setMinimumSize(QtCore.QSize(1200, 900))
        fenetreGestion.setMaximumSize(QtCore.QSize(1200, 900))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ressources/MindPass-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fenetreGestion.setWindowIcon(icon)
        
        with open("style/fenetreGestion.css", "r") as feuilleDeStyle:        
            fenetreGestion.setStyleSheet(feuilleDeStyle.read())
            
        self.centralwidget = QtWidgets.QWidget(fenetreGestion)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 881, 750))
        
        with open("style/fenetreGestionScrollArea.css", "r") as feuilleDeStyleScrollArea:        
            self.scrollArea.setStyleSheet(feuilleDeStyleScrollArea.read())
            
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 881, 750))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 881, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.horizontalLayout.setStretch(0, 100)
        self.horizontalLayout.setStretch(1, 120)
        self.horizontalLayout.setStretch(2, 120)
        self.horizontalLayout.setStretch(3, 10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(930, 70, 3, 750))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.catTitle = QtWidgets.QLabel(self.centralwidget)
        self.catTitle.setGeometry(QtCore.QRect(960, 50, 210, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.catTitle.setFont(font)
        self.catTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.catTitle.setIndent(0)
        self.catTitle.setObjectName("catTitle")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(950, 130, 230, 45))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        fenetreGestion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fenetreGestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 38))
        self.menubar.setObjectName("menubar")
        fenetreGestion.setMenuBar(self.menubar)

        self.retranslateUi(fenetreGestion)
        QtCore.QMetaObject.connectSlotsByName(fenetreGestion)

    def retranslateUi(self, fenetreGestion):
        _translate = QtCore.QCoreApplication.translate
        fenetreGestion.setWindowTitle(_translate("MainWindow", "Gestion - MindPass"))
        self.label.setText(_translate("MainWindow", "Site 1"))
        self.lineEdit_2.setText(_translate("MainWindow", "Identifiant"))
        self.lineEdit_3.setText(_translate("MainWindow", "Mot de passe"))
        self.catTitle.setText(_translate("MainWindow", "Catégories"))
        self.lineEdit.setText(_translate("MainWindow", "Ajouter une catégorie"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()
    ui = Ui_fenetreGestion()
    ui.setupUi(fenetreGestion)
    fenetreGestion.show()
    sys.exit(app.exec_())

