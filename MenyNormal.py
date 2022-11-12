from typing import List
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication ,QInputDialog, QMessageBox, QWidget, QTableWidget, QTableWidgetItem
import csv
import os


class MenyNormal(QtWidgets.QDialog):
    def __init__(self):
        super(MenyNormal, self).__init__()

        uic.loadUi('MenyNormal.ui', self)










if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MenyNormal()
    win.show()
    app.exec()