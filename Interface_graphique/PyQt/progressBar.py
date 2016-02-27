# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/progressBar.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1011, 645)
        Form.setMinimumSize(QtCore.QSize(1011, 645))
        Form.setMaximumSize(QtCore.QSize(1011, 645))
        Form.setStyleSheet("")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 951, 571))
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
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.felcheGauche = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.felcheGauche.setObjectName("felcheGauche")
        self.horizontalLayout.addWidget(self.felcheGauche)
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(779, 536))
        self.frame.setMaximumSize(QtCore.QSize(779, 536))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar.raise_()
        self.horizontalLayout.addWidget(self.frame)
        self.flecheDroite = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.flecheDroite.setObjectName("flecheDroite")
        self.horizontalLayout.addWidget(self.flecheDroite)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 100)
        self.horizontalLayout.setStretch(2, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.progressBar.setFormat(_translate("Form", "%p%"))
        self.felcheGauche.setText(_translate("Form", "flecheGauche"))
        self.flecheDroite.setText(_translate("Form", "flecheDroite"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

