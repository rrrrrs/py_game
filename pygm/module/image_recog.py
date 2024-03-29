import cv2
import numpy as np

def find_template(template_path, image_path):
    # 读取模板和图像
    template = cv2.imread(template_path, 0)
    image = cv2.imread(image_path)

    # 获取模板的宽度和高度
    w, h = template.shape[::-1]

    # 模板匹配
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # 设定阈值
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 画出找到的位置
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    # 显示结果图像
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 示例用法
template_path = 'test1.png'  # 模板图像路径
image_path = 'temp1.png'        # 待搜索的图像路径
find_template(template_path, image_path)