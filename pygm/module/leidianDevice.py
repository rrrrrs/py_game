import subprocess
import win32gui
import pyautogui

def get_cmd_path():
    cmd_path = "D:\\tools\\leidian\\LDPlayer9\\ldconsole.exe"
    return cmd_path


def get_all_leidian_devices():
    """
    获取雷电模拟器
    :return: [{}]
    """
    try:
        # 运行adb命令并捕获输出
        cmd_path = get_cmd_path()
        output = subprocess.check_output([cmd_path, 'list2']).decode()

        # 解析输出
        data = []
        for line in output.split('\n'):
            if not line.startswith('CreateFile() Error'):
                fields = line.strip().split(',')
                if len(fields) >= 3:  # 确保字段数够
                    data.append({'closed': int(fields[0]), 'name': fields[1], 'hwnd': fields[2]})

        return data
    except subprocess.CalledProcessError:
        # 如果出现错误，返回空列表
        return []

def shake_leidian_device(hwnd):
    win32gui.SetForegroundWindow(hwnd)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('6')
    pyautogui.keyUp('6')
    pyautogui.keyUp('ctrl')


if __name__ == '__main__':
    res = get_all_leidian_devices()
    for device in res:
        shake_leidian_device(device['hwnd'])
        if 0 == device['closed']:
            print("device {} is opened".format(device['name']))
        else:
            print("device {} is not opened".format(device['name']))
