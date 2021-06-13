from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit, QMessageBox
from PortfolioOfSecuritiesWindows import Ui_MainWindow

import numpy as np
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.groupBox.setTitle("Акции")
        self.pushButton.clicked.connect(self.exit)

    @QtCore.pyqtSlot()
    def exit(self):
        quit()


def main_application():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_application()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
