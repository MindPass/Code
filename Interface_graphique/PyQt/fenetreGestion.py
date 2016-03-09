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
        fenetreGestion.resize(1200, 800)
        fenetreGestion.setStyleSheet("QWidget {\n"
"border: none;\n"
"background: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QMainWindow {\n"
"background: qradialgradient(spread:pad, cx:0, cy:1, radius:1.406, fx:0, fy:1, stop:0 rgba(244, 216, 148, 255), stop:1 rgba(255, 102, 102, 255));\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background: rgba(255,255,255,100);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"background: none;\n"
"color: white;\n"
"}\n"
"\n"
"Line {\n"
"background: none;\n"
"border: 1px solid bottom;\n"
"}\n"
"\n"
"#label_3 {\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"siteLayout_3 {\n"
"background: rgba(255,255,255,25);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(fenetreGestion)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(950, 20, 211, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(949, 50, 231, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(950, 70, 221, 35))
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.categorie1 = QtWidgets.QLabel(self.centralwidget)
        self.categorie1.setGeometry(QtCore.QRect(950, 110, 191, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.categorie1.setFont(font)
        self.categorie1.setStyleSheet("categorie1{\n"
"rgb(0, 0, 127);\n"
"}")
        self.categorie1.setObjectName("categorie1")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 60, 901, 691))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 901, 691))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 880, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.siteLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.siteLayout_2.setContentsMargins(0, -1, -1, -1)
        self.siteLayout_2.setObjectName("siteLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.siteLayout_2.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("QGridLayout{\n"
"rgb(90, 93, 255);\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.siteLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.siteLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.siteLayout_2.addWidget(self.checkBox, 0, 3, 1, 1)
        self.siteLayout_2.setColumnStretch(0, 100)
        self.siteLayout_2.setColumnStretch(1, 100)
        self.siteLayout_2.setColumnStretch(2, 100)
        self.siteLayout_2.setColumnStretch(3, 12)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(880, 0, 20, 741))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 880, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.siteLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.siteLayout_3.setContentsMargins(0, -1, -1, -1)
        self.siteLayout_3.setObjectName("siteLayout_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.siteLayout_3.addWidget(self.lineEdit_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setStyleSheet("QGridLayout{\n"
"rgb(90, 93, 255);\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.siteLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setMaxLength(32767)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.siteLayout_3.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_2.setText("")
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.siteLayout_3.addWidget(self.checkBox_2, 0, 3, 1, 1)
        self.siteLayout_3.setColumnStretch(0, 100)
        self.siteLayout_3.setColumnStretch(1, 100)
        self.siteLayout_3.setColumnStretch(2, 100)
        self.siteLayout_3.setColumnStretch(3, 12)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        fenetreGestion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fenetreGestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 38))
        self.menubar.setObjectName("menubar")
        fenetreGestion.setMenuBar(self.menubar)

        self.retranslateUi(fenetreGestion)
        QtCore.QMetaObject.connectSlotsByName(fenetreGestion)

    def retranslateUi(self, fenetreGestion):
        _translate = QtCore.QCoreApplication.translate
        fenetreGestion.setWindowTitle(_translate("fenetreGestion", "Page de Gestion - MindPass"))
        self.label_3.setText(_translate("fenetreGestion", "Catégories"))
        self.lineEdit.setText(_translate("fenetreGestion", "Créer catégorie"))
        self.categorie1.setText(_translate("fenetreGestion", "Important"))
        self.lineEdit_3.setText(_translate("fenetreGestion", "Mot de passe 1"))
        self.label_4.setText(_translate("fenetreGestion", "Site 1"))
        self.lineEdit_2.setText(_translate("fenetreGestion", "Identifiant 1"))
        self.lineEdit_4.setText(_translate("fenetreGestion", "Mot de passe 2"))
        self.label_5.setText(_translate("fenetreGestion", "Site 2"))
        self.lineEdit_5.setText(_translate("fenetreGestion", "Identifiant 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()
    ui = Ui_fenetreGestion()
    ui.setupUi(fenetreGestion)
    fenetreGestion.show()
    sys.exit(app.exec_())

