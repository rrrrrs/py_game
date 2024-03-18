# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.tabContent import Ui_Form
from helpers.tabHelper import TabHelper

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tabWidget = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(793, 598)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 531, 431))
        self.tabWidget.setObjectName("tabWidget")

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab")
        self.tabWidget.addTab(self.tab1, "11")
        self.content1 = Ui_Form()
        self.content1.setupUi(self.tab1)


        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab")
        self.tabWidget.addTab(self.tab2, "22")
        self.content2 = Ui_Form()
        self.content2.setupUi(self.tab2)


        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "tool"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab 1"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Tab 2"))

        self.helper1 = TabHelper(self.content1)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
