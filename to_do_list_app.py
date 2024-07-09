from PyQt5 import QtWidgets, QtCore
from interface import Ui_mainWindow

class ToDoList_interface(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # buton interaction
        self.pushButton_addTask.clicked.connect(self.add_task)
        self.pushButton_delete.clicked.connect(self.delete_completed_tasks)
        self.pushButton_delete_all.clicked.connect(self.delete_all_tasks)
    
    def add_task(self):
        task_text = self.lineEdit_tasks.text().strip()

        if task_text:
            item = QtWidgets.QListWidgetItem(task_text)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)
            self.lineEdit_tasks.clear()
        
        else:
            QtWidgets.QMessageBox.warning(self, "Warning!", "Task cannot be empty!")

    def delete_completed_tasks(self):
        pass

    def delete_all_tasks(self):
        pass