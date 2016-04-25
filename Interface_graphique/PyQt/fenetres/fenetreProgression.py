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
        fenetreProgression.resize(740, 630)
        fenetreProgression.setMinimumSize(QtCore.QSize(740, 630))
        fenetreProgression.setMaximumSize(QtCore.QSize(740, 630))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ressources/MindPass-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fenetreProgression.setWindowIcon(icon)
        fenetreProgression.setStyleSheet("QWidget#fenetreProgression {\n"
"    background: qradialgradient(spread:pad, cx:0, cy:1, radius:1.406, fx:0, fy:1, stop:0 rgba(244, 216, 148, 255), stop:1 rgba(255, 102, 102, 255));\n"
"}\n"
"\n"
"QSlider, QLabel, QVBoxLayout, QGridLayout {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid white;\n"
"background: rgba(255,255,255,100);\n"
"height: 8px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid white;\n"
"height: 8px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgba(255,255,255,100);\n"
"border: 1px solid white;\n"
"height: 8px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #aaa;\n"
"width: 13px;\n"
"margin-top: -4px;\n"
"margin-bottom: -4px;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 7px;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(fenetreProgression)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 721, 552))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 20)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        ##### A GARDER - debut
        self.horizontalSlider.valueChanged[int].connect(self.changeValue)
        ##### A GARDER - fin

        self.gridLayout.addWidget(self.horizontalSlider, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
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
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.imageDefil = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.imageDefil.setText("")
        self.imageDefil.setPixmap(QtGui.QPixmap("../../test alex slideshow + svg/Pub1.svg"))
        self.imageDefil.setAlignment(QtCore.Qt.AlignCenter)
        self.imageDefil.setObjectName("imageDefil")
        self.gridLayout.addWidget(self.imageDefil, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(fenetreProgression)
        self.label.setGeometry(QtCore.QRect(142, 540, 455, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../ressources/MindPass-transparent.svg"))
        self.label.setObjectName("label")

        self.retranslateUi(fenetreProgression)
        QtCore.QMetaObject.connectSlotsByName(fenetreProgression)


    ##### A GARDER - debut
    def changeValue(self, value):

        if value >= 0 and value < 25:
            self.imageDefil.setPixmap(QtGui.QPixmap("../../test alex slideshow + svg/Pub1.svg"))
        elif value >=25 and value < 50:
            self.imageDefil.setPixmap(QtGui.QPixmap("../../test alex slideshow + svg/Zeichen_123.svg"))
        elif value >= 50 and value < 75:
            self.imageDefil.setPixmap(QtGui.QPixmap("../../test alex slideshow + svg/mute.png"))
        else:
            self.imageDefil.setPixmap(QtGui.QPixmap("../../test alex slideshow + svg/Pub1.svg"))
    ##### A GARDER - fin


    def retranslateUi(self, fenetreProgression):
        _translate = QtCore.QCoreApplication.translate
        fenetreProgression.setWindowTitle(_translate("fenetreProgression", "Scan en cours - MindPass"))
        self.progressBar.setFormat(_translate("fenetreProgression", "%p%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreProgression = QtWidgets.QWidget()
    ui = Ui_fenetreProgression()
    ui.setupUi(fenetreProgression)
    fenetreProgression.show()
    sys.exit(app.exec_())

