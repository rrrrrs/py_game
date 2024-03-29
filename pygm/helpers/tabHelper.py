import logging
import time
from threading import Thread
from PyQt5.QtWidgets import QFileDialog
from module import leidianDevice
from module import textOCR

class TabHelper(object):
    def __init__(self, widget=None, window=None):
        self.widget = widget
        self.window = window
        self.drop_items = []
        self.devices = []
        self.device = None
        # self.read_devices()
        self.setTab()
        self.auto_jixian_count = 0
        self.auto_jiaxian_switch = False
        self.auto_jixian_t = None


    def read_devices(self):
        self.devices = leidianDevice.get_all_leidian_devices()
        self.drop_items = [item['name'] for item in self.devices]
        if self.device is not None:
            self.set_device(self.device['name'])

        self.widget.device_box.clear()
        self.widget.device_box.addItems(self.drop_items)


    def set_device(self, name):
        if name is None:
            return

        for device in self.devices:
            if device['name'] == name:
                self.device = device
        self.checkADBState()


    def setTab(self):

        self.widget.path_btn.clicked.connect(self.path_action)
        # btn
        self.widget.start_btn.clicked.connect(self.startBtnClicked)


        # checkbox
        self.widget.shimen_cb.stateChanged.connect(lambda: self.checkboxStateCallback(self.widget.shimen_cb))

        # self.widget.device_box.clear()
        # self.widget.device_box.addItems(self.drop_items)
        self.device_selected(0)
        # self.widget.device_box.currentIndexChanged[str].connect(self.print_value)  # 条目发生改变，发射信号，传递条目内容
        self.widget.device_box.currentIndexChanged[int].connect(self.device_selected)  # 条目发生改变，发射信号，传递条目索引
        # self.widget.device_box.highlighted[str].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目内容
        # self.widget.device_box.highlighted[int].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目索引

        self.widget.shake_btn.clicked.connect(self.shake_action)

        # 工具
        self.widget.auto_jixian_btn.clicked.connect(self.auto_jixian_action)

    def checkboxStateCallback(self, cb):
        if cb.isChecked():
            print("{} has been checked".format(cb.text()))
        else:
            print("{} has been unchecked".format(cb.text()))

    def run_auto_jixian_thread(self, device_name):
        while 1:
            if self.auto_jiaxian_switch:
                self.auto_jixian_count += 1
                # 1.选角色1
                leidianDevice.tap(device_name, 640, 460)
                # leidianDevice.tap(device_name, 950, 460)
                # leidianDevice.tap(device_name, 1260, 460)

                # 2.判断
                path = leidianDevice.get_current_pic(device_name)
                text = textOCR.get_num(path, 1)
                print("当前排队状态为："+text)

                if "人数已满" in text:
                    print("进入排队失败，取消排队， 次数={}".format(self.auto_jixian_count))
                    # 2.1退出排队
                    leidianDevice.tap(device_name, 805, 620)
                    time.sleep(0.1)
                    # 2.2 去人退出排队
                    leidianDevice.tap(device_name, 920, 500)
                    time.sleep(0.1)
                elif "排队中" in text:
                    print("成功进入排队, 关闭自动挤线")
                    self.auto_jiaxian_switch = False
                else:
                    print("已不在排队，取消自动挤线")
                    self.auto_jiaxian_switch = False

            time.sleep(0.5)

    def auto_jixian_action(self):
        # 是否创建线程
        if self.auto_jixian_t is None:
            self.auto_jixian_t = Thread(target=self.run_auto_jixian_thread, args=[self.device['name']])
            self.auto_jiaxian_switch = True
            self.auto_jixian_t.start()

        # 是否正在自动点击
        if self.auto_jixian_count != 0:
            self.auto_jiaxian_switch = not self.auto_jiaxian_switch

    def startBtnClicked(self):
        print("startBtnClicked")

    def path_action(self):
        filepath = QFileDialog.getExistingDirectory(self.window, "选雷电路径")
        if filepath is not None:
            leidianDevice.set_cmd_path(filepath)
            self.read_devices()
            self.widget.path_label.setText(filepath)
            self.widget.log_text.appendPlainText("需要读取的路径为:" + filepath)

    def shake_action(self):
        if self.device['hwnd'] != 0:
            leidianDevice.shake(self.device['hwnd'])

    def device_selected(self, i):
        if i >= len(self.devices) or i < 0:
            logging.debug('无设备')
            return
        self.device = self.devices[i]
        self.checkADBState()

    def checkADBState(self):
        is_open = (self.device['hwnd'] != 0)
        if is_open:
            self.widget.stateLabel.setText('已开启')
        else:
            self.widget.stateLabel.setText('已关闭')
