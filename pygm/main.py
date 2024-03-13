# -*- coding: utf-8 -*-
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.mainUI import Ui_MainWindow


def startActionCallback():
    print("actionCallback")
    window.content1.baotuCheckBox.setChecked(True)
    window.content1.baotuCheckBox.setEnabled(False)
    window.content1.deviceLabel.setText("device01")

def checkboxStateCallback(cb):
    checkADBState()
    if cb.isChecked():
        print("{} has been checked".format(cb.text()))
    else:
        print("{} has been unchecked".format(cb.text()))

def checkADBState():
    pixmap = None  #pixmap 智能加载绝对路径
    # if ui.shimenCheckbox.isChecked():
    #     p = os.path.dirname(__file__) + "./asset/led_red.png"
    #     pixmap = QtGui.QPixmap(p)
    # else:
    #     p = os.path.dirname(__file__) + "./asset/led_yellow.png"
    #     pixmap = QtGui.QPixmap(p)
    # ui.stateLabel.setPixmap(pixmap)

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(window)
    window.content1.startBtn.clicked.connect(startActionCallback)
    window.content1.shimenCheckbox.stateChanged.connect(lambda: checkboxStateCallback(window.content1.shimenCheckbox))
    window.show()
    sys.exit(app.exec_())
