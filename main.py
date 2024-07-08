import sys
from PyQt5.QtWidgets import QApplication
from to_do_list_app import ToDoList_interface

app = QApplication(sys.argv)
to_do_list_app= ToDoList_interface()
to_do_list_app.show()
sys.exit(app.exec_())

