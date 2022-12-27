import os
import sys
from PySide2 import *


from mainwindow import *

from Custom_Widgets.Widgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)

        self.show()

        self.ui.profileBtn.clicked.connect(lambda: self.ui.profileContainer.expandMenu())
        self.ui.closeProfileBtn.clicked.connect(lambda: self.ui.profileContainer.collapseMenu())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
