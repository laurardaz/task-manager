import sys
# from PyQt5 import QtWidgets, uic
#
# app = QtWidgets.QApplication(sys.argv)
#
# window = uic.loadUi("mainwindow.ui")
# window.show()
# app.exec()

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("mainwindow.ui")

app = QApplication(sys.argv)
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()