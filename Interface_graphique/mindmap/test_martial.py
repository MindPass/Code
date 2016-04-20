import sys
from PyQt5 import QtWidgets, QtSvg
import svgwrite
from svgwrite import cm, mm   
    

dwg = svgwrite.Drawing("new.svg", debug=True)
shapes = dwg.add(dwg.g(id='shapes', fill='red'))

# set presentation attributes at object creation as SVG-Attributes
shapes.add(dwg.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='blue',
                      stroke_width=3))

dwg.save()

app = QtWidgets.QApplication(sys.argv) 


svgWidget = QtSvg.QSvgWidget('basic_shapes.svg')
svgWidget.setGeometry(50,50,700,700)
svgWidget.show()


sys.exit(app.exec_())