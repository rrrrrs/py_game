import os
import random
import subprocess
import time

import win32gui
import pyautogui

import common.commonString

dir_path = 'C:\\Users\\raosong\\Desktop\\screencap\\data'
def get_cmd_path():
    if  common.commonString.cmd_path == "" or common.commonString.cmd_path is None:
        cmd_path = "D:\\leidian\\LDPlayer64\\ldconsole.exe"
        return cmd_path
    return common.commonString.cmd_path
def set_cmd_path(cmd):
    common.commonString.cmd_path = cmd+"/ldconsole.exe"
    print("重新设定雷电路径" + common.commonString.cmd_path)
def check_cmd_path(path):
    return os.path.exists(path+"/ldconsole.exe")


def get_all_leidian_devices():
    # 获取所有雷电模拟器
    try:
        # 运行adb命令并捕获输出
        cmd_path = get_cmd_path()
        print('run command:{} {}'.format(cmd_path, 'list2'))
        output = subprocess.check_output([cmd_path, 'list2'], encoding='GBK')
        print(output)
        if output is None:
            print("未获取到雷电设备")
            return []
        # output = output.decode()
        # print("获取到雷电设备："+output)

        # 解析输出
        data = []
        for line in output.split('\n'):
            if not line.startswith('CreateFile() Error'):
                fields = line.strip().split(',')
                if len(fields) >= 4:  # 确保字段数够
                    data.append({'index': int(fields[0]), 'name': fields[1], 'hwnd': int(fields[2]) })

        return data
    except subprocess.CalledProcessError:
        # 如果出现错误，返回空列表
        return []

def open_leidian_device(name):
    # 启动雷电模拟器
    try:
        # 运行adb命令并捕获输出
        cmd_path = get_cmd_path()
        print('run command:{} {} {} {}'.format(cmd_path, 'launch', '--name', name))
        output = subprocess.check_output([cmd_path, 'launch', '--name', name]).decode()
        print("启动成功")
    except subprocess.CalledProcessError:
        # 如果出现错误，返回空列表
        return []

def get_current_pic_path(device_name):
    # 截图。当前
    cmd_path = get_cmd_path()
    fp = "/sdcard/current_0.png"
    cap_str = "{} adb --name {} --command \"shell screencap -p {} \" ".format(cmd_path, device_name, fp)
    subprocess.run(cap_str)
    loc_path = "{}\\current_0.png".format(dir_path)
    pull(device_name, '/sdcard/current_0.png', loc_path)
    return loc_path

def save_current_pic_to(path, device_name):
    cmd_path = get_cmd_path()
    fp = "/sdcard/current_0.png"
    cap_str = "{} adb --name {} --command \"shell screencap -p {} \" ".format(cmd_path, device_name, fp)
    subprocess.run(cap_str)
    r = random.randint(1000000, 99999999)
    pull(device_name, '/sdcard/current_0.png', "C:\\Users\\wangh\\Desktop\\screencap\\source\\{}.png".format(r))


def pull(device_name, file_path, loc_path):
    cmd_path = get_cmd_path()
    pull_str = "{} adb --name {} --command \" pull {} {}\" ".format(cmd_path, device_name, file_path, loc_path)
    subprocess.run(pull_str)



def tap(device_name, x, y):
    cmd_path = get_cmd_path()
    tap_str = "{} adb --name {} --command \"shell input tap {} {} \" ".format(cmd_path, device_name, x, y)
    subprocess.run(tap_str, shell=True)

def swipe(device_name, from_x, from_y, to_x, to_y):
    cmd_path = get_cmd_path()
    swipe_str = "{} adb --name {} --command  \"shell input swipe {} {} {} {}\"".format(cmd_path, device_name, from_x, from_y, to_x, to_y)
    subprocess.run(swipe_str, shell=True)


def guagaule(device_name):
    from_y = 450
    to_x = 1100
    for i in range(0, 15):
        from_x = 800 - random.randint(0, 30)
        from_y = from_y + random.randint(0, 10)
        to_x = to_x + random.randint(0, 30)
        to_y = from_y + random.randint(0, 10)
        swipe(device_name, from_x, from_y, to_x, to_y)

def shake(hwnd):
    win32gui.SetForegroundWindow(hwnd)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('6')
    pyautogui.keyUp('6')
    pyautogui.keyUp('ctrl')

if __name__ == '__main__':
    res = get_all_leidian_devices()
    for device in res:
        if device['hwnd'] != 0:
            # shake(device['hwnd'])
            # tap(device['name'], 200, 200)
            guagaule(device['name'])
            break
        else:
            print("device {} is not opened".format(device['name']))
        time.sleep(0.1)