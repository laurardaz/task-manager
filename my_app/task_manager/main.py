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


        # APPLY JSON STYLESHEET
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)

        self.show()

        self.ui.profileBtn.clicked.connect(lambda: self.ui.profileContainer.expandMenu())
        self.ui.closeProfileBtn.clicked.connect(lambda: self.ui.profileContainer.collapseMenu())

        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        self.ui.AddProjectBtn.clicked.connect(lambda: self.ui.popupAddNewContainer.collapseMenu())
        self.ui.AddTaskBtn.clicked.connect(lambda: self.ui.popupAddNewContainer.collapseMenu())


        self.ui.tasksTableWidget.setColumnWidth(0, 200)
        self.ui.tasksTableWidget.setColumnWidth(1, 200)
        self.ui.tasksTableWidget.setColumnWidth(2, 100)
        self.ui.tasksTableWidget.setColumnWidth(3, 100)
        self.ui.tasksTableWidget.setColumnWidth(4, 100)
        self.ui.tasksTableWidget.setColumnWidth(5, 100)
        self.ui.tasksTableWidget.setColumnWidth(0, 100)
        self.ui.tasksTableWidget.setColumnWidth(0, 150)
        self.loaddata()

    def loaddata(self):
        tasks=[{"название":"Сходить в магазин","описание":"купить еду","проект":"Домашний","приоритет":"Средний",
                "начало":"12.01.2023","окончание":"13.01.2023","статус":"нет","действие":"нет"},
               {"название": "Доделать модель", "описание": "покрыть лаком", "проект": "Хобби", "приоритет": "Низкий",
                "начало": "09.01.2023", "окончание": "15.01.2023", "статус": "нет", "действие": "нет"}
               ]
        row = 0
        self.ui.tasksTableWidget.setRowCount(len(tasks))
        for task in tasks:
            self.ui.tasksTableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(task["название"]))
            self.ui.tasksTableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(task["описание"]))
            self.ui.tasksTableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(task["проект"]))
            self.ui.tasksTableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(task["приоритет"]))
            self.ui.tasksTableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(task["начало"])))
            self.ui.tasksTableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(task["окончание"])))
            row =+1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
