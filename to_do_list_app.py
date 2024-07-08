from PyQt5 import QtWidgets
from interface import Ui_mainWindow

class ToDoList_interface(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        