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
        fenetreProgression.resize(740, 500)
        fenetreProgression.setMinimumSize(QtCore.QSize(740, 500))
        fenetreProgression.setMaximumSize(QtCore.QSize(740, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ressources/MindPass-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fenetreProgression.setWindowIcon(icon)
        fenetreProgression.setStyleSheet("QWidget#fenetreProgression {\n"
"  background: qradialgradient(spread:pad, cx:0, cy:1, radius:1.406, fx:0, fy:1, stop:0 rgba(244, 216, 148, 255), stop:1 rgba(255, 102, 102, 255));\n"
"}\n"
"\n"
"QSlider, QLabel, QVBoxLayout, QGridLayout {\n"
"  background: transparent;\n"
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(fenetreProgression)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 722, 482))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setAccessibleName("")
        self.progressBar.setStyleSheet("QProgressBar {\n"
"background-color: lightgrey;\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_image_prec = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_image_prec.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton_image_prec.setObjectName("pushButton_image_prec")
        self.horizontalLayout.addWidget(self.pushButton_image_prec)
        self.imageDefil = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.imageDefil.setMaximumSize(QtCore.QSize(700, 500))
        self.imageDefil.setMouseTracking(True)
        self.imageDefil.setText("")
        self.imageDefil.setPixmap(QtGui.QPixmap("../ressources/images/Pub0.svg"))
        self.imageDefil.setAlignment(QtCore.Qt.AlignCenter)
        self.imageDefil.setObjectName("imageDefil")
        self.horizontalLayout.addWidget(self.imageDefil)
        self.pushButton_image_suiv = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_image_suiv.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton_image_suiv.setObjectName("pushButton_image_suiv")
        self.horizontalLayout.addWidget(self.pushButton_image_suiv)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bouton_page_suiv = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_page_suiv.sizePolicy().hasHeightForWidth())
        self.bouton_page_suiv.setSizePolicy(sizePolicy)
        self.bouton_page_suiv.setObjectName("bouton_page_suiv")
        self.horizontalLayout_2.addWidget(self.bouton_page_suiv)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(fenetreProgression)
        QtCore.QMetaObject.connectSlotsByName(fenetreProgression)

    def retranslateUi(self, fenetreProgression):
        _translate = QtCore.QCoreApplication.translate
        fenetreProgression.setWindowTitle(_translate("fenetreProgression", "Scan en cours - MindPass"))
        self.progressBar.setFormat(_translate("fenetreProgression", "%p%"))
        self.pushButton_image_prec.setText(_translate("fenetreProgression", "<"))
        self.pushButton_image_suiv.setText(_translate("fenetreProgression", ">"))
        self.bouton_page_suiv.setText(_translate("fenetreProgression", "Suivant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreProgression = QtWidgets.QWidget()
    ui = Ui_fenetreProgression()
    ui.setupUi(fenetreProgression)
    fenetreProgression.show()
    sys.exit(app.exec_())

