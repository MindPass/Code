# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/pageGestion.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PageGestion(object):
    def setupUi(self, PageGestion):
        PageGestion.setObjectName("PageGestion")
        PageGestion.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PageGestion)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 434, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.siteLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.siteLayout.setContentsMargins(0, -1, -1, -1)
        self.siteLayout.setObjectName("siteLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("QGridLayout{\n"
"rgb(90, 93, 255);\n"
"}")
        self.label.setObjectName("label")
        self.siteLayout.addWidget(self.label, 0, 0, 1, 1)
        self.affichageMdp = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.affichageMdp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.affichageMdp.setObjectName("affichageMdp")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.affichageMdp.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.affichageMdp.addTab(self.tab_2, "")
        self.siteLayout.addWidget(self.affichageMdp, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("QGridLayout {\n"
"background-color: lightgrey;\n"
"border: 2px solid purple;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.siteLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.siteLayout.setColumnStretch(0, 200)
        self.siteLayout.setColumnStretch(1, 200)
        self.siteLayout.setColumnStretch(2, 200)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(570, 60, 151, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(570, 150, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.categorie1 = QtWidgets.QLabel(self.centralwidget)
        self.categorie1.setGeometry(QtCore.QRect(580, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.categorie1.setFont(font)
        self.categorie1.setStyleSheet("categorie1{\n"
"rgb(0, 0, 127);\n"
"}")
        self.categorie1.setObjectName("categorie1")
        PageGestion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PageGestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PageGestion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PageGestion)
        self.statusbar.setObjectName("statusbar")
        PageGestion.setStatusBar(self.statusbar)

        self.retranslateUi(PageGestion)
        self.affichageMdp.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PageGestion)

    def retranslateUi(self, PageGestion):
        _translate = QtCore.QCoreApplication.translate
        PageGestion.setWindowTitle(_translate("PageGestion", "Page de Gestion"))
        self.label.setText(_translate("PageGestion", "Site"))
        self.affichageMdp.setTabText(self.affichageMdp.indexOf(self.tab), _translate("PageGestion", "Tab 1"))
        self.affichageMdp.setTabText(self.affichageMdp.indexOf(self.tab_2), _translate("PageGestion", "Tab 2"))
        self.label_2.setText(_translate("PageGestion", "Login"))
        self.label_3.setText(_translate("PageGestion", "Catégories"))
        self.lineEdit.setText(_translate("PageGestion", "Créer catégorie"))
        self.categorie1.setText(_translate("PageGestion", "Important"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PageGestion = QtWidgets.QMainWindow()
    ui = Ui_PageGestion()
    ui.setupUi(PageGestion)
    PageGestion.show()
    sys.exit(app.exec_())

