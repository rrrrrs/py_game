# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from views.mainWindow import Ui_MainWindow

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
