import time
from module import leidianDevice

class TabHelper(object):
    def __init__(self, widget=None):
        self.widget = widget
        self.drop_items = []
        self.devices = []
        self.device = None
        self.read_devices()
        self.setTab()

    def read_devices(self):
        self.devices = leidianDevice.get_all_leidian_devices()
        self.drop_items = [item['name'] for item in self.devices]
        if self.device is not None:
            self.set_device(self.device['name'])

    def set_device(self, name):
        if name is None:
            return

        for device in self.devices:
            if device['name'] == name:
                self.device = device
        self.checkADBState()


    def setTab(self):

        # btn
        self.widget.start_btn.clicked.connect(self.startBtnClicked)

        # checkbox
        self.widget.shimen_cb.stateChanged.connect(lambda: self.checkboxStateCallback(self.widget.shimen_cb))

        # names = [self.items['name'] for item in array]
        self.widget.comboBox.clear()
        self.widget.comboBox.addItems(self.drop_items)
        self.combox_selected(0)
        # 信号
        # self.widget.comboBox.currentIndexChanged[str].connect(self.print_value)  # 条目发生改变，发射信号，传递条目内容
        self.widget.comboBox.currentIndexChanged[int].connect(self.combox_selected)  # 条目发生改变，发射信号，传递条目索引
        # self.widget.comboBox.highlighted[str].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目内容
        # self.widget.comboBox.highlighted[int].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目索引

    def checkboxStateCallback(self, cb):
        # self.checkADBState(False)
        if cb.isChecked():
            print("{} has been checked".format(cb.text()))
        else:
            print("{} has been unchecked".format(cb.text()))

    def startBtnClicked(self):
        if self.device['hwnd'] == 0:
            print("模拟器未启动,自动启动模拟器...")
            leidianDevice.open_leidian_device(self.device['name'])
            time.sleep(1)
            self.read_devices()
        else:
            print('模拟器已启动，开始任务')

    def combox_selected(self, i):
        self.device = self.devices[i]
        self.checkADBState()

    def checkADBState(self):
        is_open = (self.device['hwnd'] != 0)
        if is_open:
            self.widget.stateLabel.setText('已开启')
        else:
            self.widget.stateLabel.setText('已关闭')
