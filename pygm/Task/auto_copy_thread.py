import time
from threading import Thread
from module import leidianDevice, image_recog

class Auto_copy_Thread(Thread):
    def __init__(self, device_name):
        super().__init__()
        self.dev_name = device_name
        self.running = True
        # 侠士副本
        self.copy_dif_idx = 2
        # 普通副本
        self.copy_nor_idx = 3
    def stop_thread(self):
        self.running = False
    def run(self):
        while self.running:
            print("running")

            is_xia = True if (self.copy_dif_idx > 0) else False
            str1 = "侠士" if (self.copy_dif_idx > 0) else "普通本"
            print("开始选择副本：{} {}".format(str1, self.copy_dif_idx if is_xia else self.copy_nor_idx))
            # 副本执行顺序 侠士2 ->     侠士1 ->      普通本3 -> 普通本2 -> 普通本1 -> 结束
            #            is_xia 2    is_xia 1
            if self.copy_nor_idx < 1:
                print("所有副本结束")
                break

            if self.copy_dif_idx < 1:
                print("难度副本结束")
            elif self.copy_dif_idx >= 1:
                self.copy_dif_idx -= 1
            else:
                self.copy_nor_idx -= 1

            if is_xia:
                self.auto_choose_copy(True, self.copy_dif_idx)
            else:
                self.auto_choose_copy(False, self.copy_nor_idx)

    def auto_choose_copy(self, is_xia, index):
        """
        自动选择副本： 站街状态 -> 进入副本
        :param is_xia: 是否是侠士副本
        :param index: 第几个副本【1,2,3】
        """
        p = leidianDevice.get_current_pic(device_name=self.dev_name)
        if p in "ssdasdasdasdasdasd":
            pass
        leidianDevice.tap(self.dev_name, 30, 30)

        # find 长安城 -> 点击
        leidianDevice.tap(self.dev_name, 1200, 200)

        # 点击小地图，找仙子,并点击
        leidianDevice.tap(self.dev_name, 100, 40)
        p = leidianDevice.get_current_pic(device_name=self.dev_name)
        (img, x, y) = image_recog.find_template(template_path=p, image_path="small_pic.png")
        leidianDevice.tap(self.dev_name, x, y)

        # 等待副本对话框
        t = 0
        while t < 10:
            p = leidianDevice.get_current_pic(device_name=self.dev_name)
            (img, x, y) = image_recog.find_template(template_path=p, image_path="副本对话框.png")
            if img is not None:
                leidianDevice.tap(self.dev_name, x, y)
                break
            time.sleep(1)
            t -= 1

        # 选择侠士副本
        if is_xia:
            leidianDevice.tap(self.dev_name, 10, 10)  # 侠士本tab

        # 选择第几个副本
        if index == 1:
            leidianDevice.tap(self.dev_name, 10, 10)  # 副本开始按钮
        elif index == 2:
            leidianDevice.tap(self.dev_name, 20, 10)
        elif index == 3:
            leidianDevice.tap(self.dev_name, 30, 10)

        print("副本选择完成，开始等待副本任务")


    def auto_copy_thread(self):
        # 开始自动副本了
        while self.running:
            time.sleep(1)



if __name__ == '__main__':
    c = Auto_copy_Thread('device_name')
    c.start()
