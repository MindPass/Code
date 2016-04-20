import sys
sys.path.append("../svgwrite-1.1.6")
from PyQt5 import QtWidgets, QtSvg
import svgwrite
from svgwrite import cm, mm, px   
    

dwg = svgwrite.Drawing("new.svg", debug=True)

# dwg.add(dwg.circle(center=(50,50), r=10))
dwg.add(dwg.path(d="m 50,50 c 20.51273,-1.01016 5.05077,-30.61426 26.57365,-30.61426",
	style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:0.7;stroke-miterlimit:4;stroke-dasharray:2"))
# dwg.add(dwg.path(d="m 10,10 C100,100 250,100 250,200 S400,300 400,200",style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:0.7;stroke-miterlimit:4;stroke-dasharray:2"))
# shapes = dwg.add(dwg.g(id='shapes'))

# # set presentation attributes at object creation as SVG-Attributes
# shapes.add(dwg.circle(center=(50, 50), r='5cm', stroke='blue',
#                       stroke_width=3))

dwg.save()

app = QtWidgets.QApplication(sys.argv) 


svgWidget = QtSvg.QSvgWidget('new.svg')
svgWidget.resize(400,400)
svgWidget.show()


sys.exit(app.exec_())