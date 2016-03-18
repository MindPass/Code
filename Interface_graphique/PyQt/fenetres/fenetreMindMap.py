# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/fenetreMindMap.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fenetreMindMap(object):
    def setupUi(self, fenetreMindMap):
        fenetreMindMap.setObjectName("fenetreMindMap")
        fenetreMindMap.resize(698, 578)

        self.retranslateUi(fenetreMindMap)
        QtCore.QMetaObject.connectSlotsByName(fenetreMindMap)

    def retranslateUi(self, fenetreMindMap):
        _translate = QtCore.QCoreApplication.translate
        fenetreMindMap.setWindowTitle(_translate("fenetreMindMap", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreMindMap = QtWidgets.QWidget()
    ui = Ui_fenetreMindMap()
    ui.setupUi(fenetreMindMap)
    fenetreMindMap.show()
    sys.exit(app.exec_())

