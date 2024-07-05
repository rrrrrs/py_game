import configparser
import logging
import os
import time
from threading import Thread
from PyQt5.QtWidgets import QFileDialog

from Task import auto_copy_thread
from module import leidianDevice, image_recog
from module import textOCR
from tkinter import messagebox
class TabHelper(object):
    def __init__(self, widget=None, window=None):
        self.widget = widget
        self.window = window
        self.drop_items = []
        self.devices = []
        self.device = None
        # self.read_devices()
        self.setTab()
        self.auto_fuben_t = None
        self.config_path = os.path.join(os.getcwd(), 'user', 'config.ini')
        self.config = configparser.ConfigParser()
        self.init_config()

    def init_config(self):
        # 初始化配置文件
        target_dir = os.path.dirname(self.config_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        if not os.path.exists(self.config_path):
            with open(self.config_path, 'w') as new_file:
                new_file.write('[DEFAULT] \nServerAliveInterval = 45\nCompression = yes\nCompressionLevel = 9\nForwardX11 = yes\n')
                self.config.read(self.config_path)
                # self.config['DEFAULT']['Adb_path'] = 'D:\\tools\\leidian\\ldmutiplayer\\'
        # print(self.config['DEFAULT']['Adb_path'])


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
        self.widget.baotu_cb.stateChanged.connect(lambda: self.checkboxStateCallback(self.widget.baotu_cb))
        self.widget.mijing_cb.stateChanged.connect(lambda: self.checkboxStateCallback(self.widget.mijing_cb))
        self.widget.yunbiao_cb.stateChanged.connect(lambda: self.checkboxStateCallback(self.widget.yunbiao_cb))
        self.widget.fuben_cb.stateChanged.connect(lambda: self.checkboxStateCallback(self.widget.fuben_cb))
        self.widget.zhuogui_cb.stateChanged.connect(lambda: self.checkboxStateCallback(self.widget.zhuogui_cb))

        # self.widget.device_box.clear()
        # self.widget.device_box.addItems(self.drop_items)
        self.device_selected(0)
        # self.widget.device_box.currentIndexChanged[str].connect(self.print_value)  # 条目发生改变，发射信号，传递条目内容
        self.widget.device_box.currentIndexChanged[int].connect(self.device_selected)  # 条目发生改变，发射信号，传递条目索引
        # self.widget.device_box.highlighted[str].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目内容
        # self.widget.device_box.highlighted[int].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目索引

        self.widget.shake_btn.clicked.connect(self.shake_action)

        # 工具
        self.widget.tool_btn_2.clicked.connect(self.cap_current_screen)
        self.widget.tool_btn_3.clicked.connect(self.auto_fuben_action)

    def checkboxStateCallback(self, cb):
        if cb.isChecked():
            print("{} has been checked".format(cb.text()))
        else:
            print("{} has been unchecked".format(cb.text()))

    def cap_current_screen(self):
        leidianDevice.save_current_pic_to(None, self.device['name'])


    def auto_fuben_action(self):
        dev_name = self.device['name']
        if self.auto_fuben_t is None:
            self.auto_fuben_t = auto_copy_thread.Auto_copy_Thread(dev_name)
            self.auto_fuben_t.start()
        else:
            self.auto_fuben_t.stop_thread()

    def startBtnClicked(self):
        print("startBtnClicked")

    def path_action(self):
        filepath = QFileDialog.getExistingDirectory(self.window, "选雷电路径")
        if filepath is not None and leidianDevice.check_cmd_path(filepath):
            leidianDevice.set_cmd_path(filepath)
            self.config['Default']['adb_path'] = filepath
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)
            self.read_devices()
            self.widget.path_label.setText(filepath)
            self.widget.log_text.appendPlainText("需要读取的路径为:" + filepath)
        else:
            messagebox.showerror('错误', '雷电路径错误')
            print('雷电路径错误')

    def shake_action(self):
        if self.device['hwnd'] != 0:
            leidianDevice.shake(self.device['hwnd'])
        else:
            messagebox.showerror('错误', '模拟器未启动')
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
