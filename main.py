

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from inter2 import Ui_mainWindow
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

def application():
    app = QApplication(sys.argv)
    window = mywindow()

    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    application()
