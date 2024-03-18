import os

from PyQt5 import QtGui

from module import leidianDevice
class TabHelper(object):
    def __init__(self, widget=None):
        self.widget = widget
        self.items = []
        self.devices = []
        self.read_devices()
        self.setTab()

    def read_devices(self):
        self.devices = leidianDevice.get_all_leidian_devices()
        self.items = [item['name'] for item in self.devices]

        # for device in res:
        #     self.items.append("{} {}".format(device['name'], "open" if 0 == device['id'] else "close"))
        #     self.items.append("{}".format(device['name']))


    def setTab(self):

        #btn
        self.widget.startBtn.clicked.connect(self.startBtnClicked)

        #checkbox
        self.widget.shimenCheckbox.stateChanged.connect(lambda: self.checkboxStateCallback(self.widget.shimenCheckbox))

        # names = [self.items['name'] for item in array]
        self.widget.comboBox.clear()
        self.widget.comboBox.addItems(self.items)
        # 信号
        # self.widget.comboBox.currentIndexChanged[str].connect(self.print_value)  # 条目发生改变，发射信号，传递条目内容
        self.widget.comboBox.currentIndexChanged[int].connect(self.combox_selected)  # 条目发生改变，发射信号，传递条目索引
        # self.widget.comboBox.highlighted[str].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目内容
        # self.widget.comboBox.highlighted[int].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目索引

    def checkboxStateCallback(self, cb):
        self.checkADBState(False)
        if cb.isChecked():
            print("{} has been checked".format(cb.text()))
        else:
            print("{} has been unchecked".format(cb.text()))

    def startBtnClicked(self):
        print("adb start capsheet")

    def combox_selected(self, i):
        value = self.devices[i]['closed']
        print(value)
        self.checkADBState(value==0)

    def checkADBState(self, is_open):
        pixmap = None  # pixmap 只能加载绝对路径
        if is_open:
            p = os.path.dirname(__file__) + "/asset/led_red.png"
            pixmap = QtGui.QPixmap(p)
        else:
            p = os.path.dirname(__file__) + "/asset/led_yellow.png"
            pixmap = QtGui.QPixmap(p)
        self.widget.stateLabel.setPixmap(pixmap)
