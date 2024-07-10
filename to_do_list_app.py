from PyQt5 import QtWidgets, QtCore
from interface import Ui_mainWindow

FILE_PATH = "tasks.txt"

class ToDoList_interface(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # buton interaction
        self.pushButton_addTask.clicked.connect(self.add_task)
        self.pushButton_delete.clicked.connect(self.delete_completed_tasks)
        self.pushButton_delete_all.clicked.connect(self.delete_all_tasks)
        self.listWidget.itemChanged.connect(self.mark_task_completed)
    
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
        items_to_delete = []
        
        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            if item.checkState() == QtCore.Qt.Checked:
                items_to_delete.append(index)

        for index in reversed(items_to_delete):
            self.listWidget.takeItem(index)

    def delete_all_tasks(self):
        self.listWidget.clear()

    def mark_task_completed(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            item.setForeground(QtCore.Qt.gray)
            item.setBackground(QtCore.Qt.lightGray)
        else:
            item.setForeground(QtCore.Qt.black)
            item.setBackground(QtCore.Qt.white)

    def save_tasks(self):
        with open(FILE_PATH, 'w') as file:
            for i in range(self.listWidget.count()):
                item = self.listWidget.item(i)
                task_text = item.text()
                if item.checkState() == QtCore.Qt.Checked:
                    file.write(f"[x] {task_text}\n")
                else:
                    file.write(f"[ ] {task_text}\n")

    def load_tasks(self):
        try:
            with open(FILE_PATH, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("[x]"):
                        task_text = line[4:]
                        item = QtWidgets.QListWidgetItem(task_text)
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        item.setCheckState(QtCore.Qt.Checked)
                        item.setForeground(QtCore.Qt.gray)
                        item.setBackground(QtCore.Qt.lightGray)
                    else:
                        task_text = line[4:]
                        item = QtWidgets.QListWidgetItem(task_text)
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setForeground(QtCore.Qt.black)
                        item.setBackground(QtCore.Qt.white)
                    self.listWidget.addItem(item)
        except FileNotFoundError:
            pass

    def closeEvent(self, event):
        self.save_tasks()
        event.accept()