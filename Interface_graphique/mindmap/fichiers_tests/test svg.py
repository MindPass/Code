import sys
from PyQt5 import QtWidgets, QtSvg

app = QtWidgets.QApplication(sys.argv) 
svgWidget = QtSvg.QSvgWidget('Zeichen_123.svg')
svgWidget.setGeometry(50,50,500,400)
svgWidget.show()

sys.exit(app.exec_())