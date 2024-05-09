import time
from threading import Thread
from module import leidianDevice, image_recog

class Auto_shimen_Thread(Thread):
    def __init__(self, device_name):
        super().__init__()
        self.dev_name = device_name
        self.running = True
    def stop_thread(self):
        self.running = False
    def run(self):
        """
        自动选择副本： 站街状态 -> 开始师门
        """
        # 1.检测当前（站街）任务栏有无师门 任务并点击
        p = leidianDevice.get_current_pic_path(device_name=self.dev_name)
        (img, x, y) = image_recog.find_template(template_path=p, image_path="师门.pic.png")
        if img is not None:
            print("找到师门任务")
            leidianDevice.tap(self.dev_name, x, y)

        # 2.检测师门任务弹出窗
        p = leidianDevice.get_current_pic_path(device_name=self.dev_name)
        (img, x, y) = image_recog.find_template(template_path=p, image_path="开始师门.pic.png")
        if img is not None:
            print("开始师门任务")
            leidianDevice.tap(self.dev_name, x, y)

        # 2.1是否继续完成师门
        p = leidianDevice.get_current_pic_path(device_name=self.dev_name)
        (img, x, y) = image_recog.find_template(template_path=p, image_path="继续师门.pic.png")
        if img is not None:
            print("继续师门任务")
            leidianDevice.tap(self.dev_name, x, y)


    def auto_copy_thread(self):
        # 开始自动副本了
        while self.running:
            print("等待师门任务完成..")
            p = leidianDevice.get_current_pic_path(device_name=self.dev_name)
            (img, x, y) = image_recog.find_template(template_path=p, image_path="师门结算页面.pic.png")
            if img is not None:
                print("师门任务完成")
                break
            time.sleep(10)

        print("师门任务完成，一般会有弹窗，类似于九转天阶、剑会新赛季之类的")
        print("尽量花30s在这里循环处理弹窗")



if __name__ == '__main__':
    c = Auto_shimen_Thread('device_name')
    c.start()
