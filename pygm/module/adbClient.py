import subprocess
import time
import os
from subprocess import run
import random
from common import commonString
def time_stamp():
    """
    生产年月日，时分秒
    """
    now = int(round(time.time() * 1000))
    return time.strftime('%Y-%m-%d_%H%M%S', time.localtime(now / 1000))

class AdbClient(object):

    def __init__(self, save_path=None, file_name=None):
        self.save_path = save_path
        self.file_name = file_name

    def get_connected_devices(self):
        try:
            # 运行adb命令并捕获输出
            output = subprocess.check_output(['adb', 'devices']).decode().split('\n')
            # 第一行是标题，忽略
            devices = [line.split('\t')[0] for line in output[1:] if line.strip() != '' and not line.startswith('*')]
            return devices
        except subprocess.CalledProcessError:
            # 如果出现错误，返回空列表
            return []

    def screen_swipe(self, device_name, from_x, from_y, to_x, to_y):
        record = r"adb -s {} shell input swipe {} {} {} {}".format(device_name,from_x, from_y, to_x, to_y)
        os.system(record)

    def start_guaguale(self, device_name):
        """
        刮刮乐
        :param device_name: adb device name
        :return: null
        """
        # from_x = 800
        from_y = 450
        to_x = 1100
        # to_y = 600

        for i in range(0, 15):
            from_x = 800 - random.randint(0, 30)
            from_y = from_y + random.randint(0, 10)

            to_x = to_x + random.randint(0, 30)
            to_y = from_y + random.randint(0, 10)

            adb.screen_swipe(device_name, from_x, from_y, to_x, to_y)

    def screen_shot_and_pull(self, device_name=None, pull_path=None, file_path=None, file_name=None, is_delete=True):
        """
        device_name: 设备名
        file_path: 截图在设备里存储的位置
        pull_path: 截图导出的位置
        file_name: 截图名称
        is_delete: 用完了是否删除
        名称是时间戳命名格式
        需要传一个保存图片路径，路径目录不存在的话，会自动创建
        """
        if file_name is not None:
            img_name = file_name
        else:
            img_name = time_stamp()+"_"+str(random.randint(99, 199))

        shot = r"adb -s {} shell screencap -p /sdcard/{}.png".format(device_name, img_name)
        run(shot, shell=True)

        if pull_path is None:
            return

        if not os.path.exists(pull_path):
            os.makedirs(pull_path, exist_ok=True)
        # pull_png = r"adb -s {} pull /sdcard/{}.png {}  >> log1.txt".format(device_name, img_name, pull_path)
        # run(pull_png, shell=True)
        self.pull_file(device_name, "/sdcard/{}.png".format(img_name), pull_path)

        #清除冗余数据
        if is_delete:
            self.delete_file(device_name, img_name)

    def delete_file(self, device_name, img_name):
        delete_png = r"adb -s {} shell rm /sdcard/{}.png ".format(device_name, img_name)
        run(delete_png, shell=True)


    def screen_record(self, device_name=None):
        """
        时间戳命名
        关掉cmd命令窗口，即可保存视频
        需要传一个保存视频路径
        """
        t = time_stamp()
        record = r"adb -s {} shell screenrecord /sdcard/{}.mp4".format(device_name, t)
        os.system(record)

        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        pull_png = r"adb -s {} pull /sdcard/{}.mp4 {}".format(device_name, t, self.save_path)
        run(pull_png, shell=True)

    def log_cat(self, device_name, log_path):
        """
        关掉cmd命令窗口，即可保存日志
        需要传一个保存日志路径及其名称 例:D:\log\crash.log
        """
        log = r"adb -s {} logcat > {}".format(device_name, self.file_name)
        os.system(log)

    def pull_file(self, device_name, device_path, pull_path):
        """
        从设备拉数据下来
        """
        pull_png = r"adb -s {} pull {} {}  >> nul".format(device_name, device_path, pull_path)
        run(pull_png, shell=True)

    def push_file(self, device_name=None):
        """
        上传数据到设备
        """
        push = r"adb -s {} push {} {}".format(device_name, self.res, self.dst)
        os.system(push)

    def cmd(self, cmdStr):
        run(cmdStr, shell=True)


if __name__ == '__main__':

    adb = AdbClient()
    connected_devices = adb.get_connected_devices()
    print("Connected devices:", connected_devices)

    adb.start_guaguale(connected_devices[0])

    # adb.screen_shot_and_pull(device_name=connected_devices[0], pull_path="C:\\Users\\raosong\\Desktop\\imgs")
    # adb.screen_shot_and_pull(device_name=connected_devices[1], pull_path="C:\\Users\\raosong\\Desktop\\imgs")

