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
        Form.resize(1008, 638)
        Form.setStyleSheet("")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(200, 60, 631, 41))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 200, 481, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteButton1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteButton1.setObjectName("deleteButton1")
        self.horizontalLayout.addWidget(self.deleteButton1)
        self.label_site1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_site1.setObjectName("label_site1")
        self.horizontalLayout.addWidget(self.label_site1, 0, QtCore.Qt.AlignHCenter)
        self.label_mdp1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_mdp1.setObjectName("label_mdp1")
        self.horizontalLayout.addWidget(self.label_mdp1, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.setStretch(0, 50)
        self.horizontalLayout.setStretch(1, 100)
        self.horizontalLayout.setStretch(2, 100)
        self.radioButton1_site1 = QtWidgets.QRadioButton(Form)
        self.radioButton1_site1.setGeometry(QtCore.QRect(80, 170, 82, 17))
        self.radioButton1_site1.setObjectName("radioButton1_site1")
        self.radioButton2_site1 = QtWidgets.QRadioButton(Form)
        self.radioButton2_site1.setGeometry(QtCore.QRect(120, 170, 82, 17))
        self.radioButton2_site1.setObjectName("radioButton2_site1")
        self.lineEdit_mdp1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_mdp1.setGeometry(QtCore.QRect(670, 230, 181, 21))
        self.lineEdit_mdp1.setText("")
        self.lineEdit_mdp1.setObjectName("lineEdit_mdp1")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 350, 481, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteButton2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.deleteButton2.setObjectName("deleteButton2")
        self.horizontalLayout_2.addWidget(self.deleteButton2)
        self.label_site2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_site2.setObjectName("label_site2")
        self.horizontalLayout_2.addWidget(self.label_site2, 0, QtCore.Qt.AlignHCenter)
        self.label_mdp2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_mdp2.setObjectName("label_mdp2")
        self.horizontalLayout_2.addWidget(self.label_mdp2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.setStretch(0, 50)
        self.horizontalLayout_2.setStretch(1, 100)
        self.horizontalLayout_2.setStretch(2, 100)
        self.radioButton2_site2 = QtWidgets.QRadioButton(Form)
        self.radioButton2_site2.setGeometry(QtCore.QRect(120, 320, 82, 17))
        self.radioButton2_site2.setObjectName("radioButton2_site2")
        self.lineEdit_mdp2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_mdp2.setGeometry(QtCore.QRect(670, 380, 181, 21))
        self.lineEdit_mdp2.setText("")
        self.lineEdit_mdp2.setObjectName("lineEdit_mdp2")
        self.radioButtons_site2 = QtWidgets.QRadioButton(Form)
        self.radioButtons_site2.setGeometry(QtCore.QRect(80, 320, 82, 17))
        self.radioButtons_site2.setObjectName("radioButtons_site2")

        self.retranslateUi(Form)
        self.radioButton2_site1.clicked.connect(self.label_mdp1.lower)
        self.deleteButton1.clicked.connect(self.label_site1.hide)
        self.deleteButton1.clicked.connect(self.label_mdp1.hide)
        self.deleteButton1.clicked.connect(self.deleteButton1.hide)
        self.deleteButton1.clicked.connect(self.radioButton1_site1.hide)
        self.deleteButton1.clicked.connect(self.radioButton2_site1.hide)
        self.deleteButton1.clicked.connect(self.lineEdit_mdp1.hide)
        self.radioButton2_site1.clicked.connect(self.label_mdp1.update)
        self.deleteButton2.clicked.connect(self.radioButtons_site2.hide)
        self.deleteButton2.clicked.connect(self.label_site2.hide)
        self.deleteButton2.clicked.connect(self.label_mdp2.hide)
        self.deleteButton2.clicked.connect(self.lineEdit_mdp2.hide)
        self.deleteButton2.clicked.connect(self.deleteButton2.hide)
        self.deleteButton2.clicked.connect(self.radioButton2_site2.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.deleteButton1.setText(_translate("Form", "delete"))
        self.label_site1.setText(_translate("Form", "site1"))
        self.label_mdp1.setText(_translate("Form", "Mot de passe 1"))
        self.radioButton1_site1.setText(_translate("Form", "1"))
        self.radioButton2_site1.setText(_translate("Form", "2"))
        self.deleteButton2.setText(_translate("Form", "delete"))
        self.label_site2.setText(_translate("Form", "site2"))
        self.label_mdp2.setText(_translate("Form", "Mot de passe 2"))
        self.radioButton2_site2.setText(_translate("Form", "2"))
        self.radioButtons_site2.setText(_translate("Form", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

