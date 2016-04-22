#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a QSlider widget.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
import time
from PyQt5 import QtSvg
from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        date_debut = time.time()
        intervalle = 25
        
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)


        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Zeichen_123.svg'))
        self.label.setGeometry(160, 40, 600, 400)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()
        
        
    def changeValue(self, value):

        if value >= 0 and value < 25:
            self.label.setPixmap(QPixmap('Zeichen_123.svg'))
        elif value >=25 and value < 50:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value >= 50 and value < 75:
            self.label.setPixmap(QPixmap('Zeichen_123.svg'))
        else:
            self.label.setPixmap(QPixmap('mute.png'))
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())