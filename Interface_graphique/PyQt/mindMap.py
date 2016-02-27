# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/mindMap.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mindMap(object):
    def setupUi(self, mindMap):
        mindMap.setObjectName("mindMap")
        mindMap.resize(698, 578)

        self.retranslateUi(mindMap)
        QtCore.QMetaObject.connectSlotsByName(mindMap)

    def retranslateUi(self, mindMap):
        _translate = QtCore.QCoreApplication.translate
        mindMap.setWindowTitle(_translate("mindMap", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mindMap = QtWidgets.QWidget()
    ui = Ui_mindMap()
    ui.setupUi(mindMap)
    mindMap.show()
    sys.exit(app.exec_())

