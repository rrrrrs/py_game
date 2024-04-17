import threading
import time

from module import leidianDevice, image_recog

a = 5

def copy_task_t(device_name):
    while True:
        p = leidianDevice.get_current_pic(device_name=device_name)
        if p in "ssdasdasdasdasdasd":
            pass
        leidianDevice.tap(device_name, 30, 30)

        # find 长安城 -> 点击
        leidianDevice.tap(device_name, 1200, 200)

        # 点击小地图，找仙子,并点击
        leidianDevice.tap(device_name, 100, 40)
        p = leidianDevice.get_current_pic(device_name=device_name)
        (img, x, y) = image_recog.find_template(template_path=p, image_path="small_pic.png")
        leidianDevice.tap(device_name, x, y)


        # 等待副本对话框
        t = 0
        while t < 10:
            p = leidianDevice.get_current_pic(device_name=device_name)
            (img, x, y) = image_recog.find_template(template_path=p, image_path="副本对话框.png")
            if img is not None:
                leidianDevice.tap(device_name, x, y)
                break
            time.sleep(1)

        # 选择侠士副本
        leidianDevice.tap(device_name, 10, 10)
        leidianDevice.tap(device_name, 1200, 1100)
        t = 0
        while t < 30:

            time.sleep(1)
        time.sleep(10)

def start_copy_with_captain(device_name):
    # 功能开启TCP接收线程
    clent_t = threading.Thread(target=copy_task_t, args=(device_name,))
    clent_t.start()


if '__main__' == __name__:
    start_copy_with_captain('arr')
    pass