# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBar.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 200)
        Form.setStyleSheet("")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(100, 60, 600, 40))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ressources/MindPass-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        with open("style/progressBar.css","r") as feuilleDeStyle:
            self.progressBar.setStyleSheet(feuilleDeStyle.read())
        
        self.progressBar.setAccessibleName("")
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MindPass - Scan en cours..."))
        self.progressBar.setFormat(_translate("Form", "%p%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

