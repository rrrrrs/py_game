import cv2
import numpy as np
import matplotlib.pyplot as plt

fuben_dialog_complete_path = 'D:\\code\\py_gm\\pygm\\asset\\fuben_dialog_complete.png'
fuben_dialog_next_path = 'D:\\code\\py_gm\\pygm\\asset\\fuben_dialog_next.png'
fuben_dialog_fighting_path = 'D:\\code\\py_gm\\pygm\\asset\\fuben_dialog_fight.png'
fuben_dialog_tiaoguo_path = 'D:\\code\\py_gm\\pygm\\asset\\fuben_dialog_tiaoguo.png'

def showpic(img):
    plt.clf()
    plt.figure()
    plt.axis('off')
    plt.imshow(img, animated=True)
    plt.tight_layout()
    plt.show()



def get_target_point(big_path, sml_path, max):
    # 通过模板对比，找目标位置，
    # 如果找到，即返回按钮中心位置
    big_img = cv2.imread(big_path)
    sml_img = cv2.imread(sml_path)
    # 模板匹配
    result = cv2.matchTemplate(big_img, sml_img, cv2.TM_CCOEFF_NORMED)
    # 找到最大值和最大值的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 如果使用 TM_CCOEFF_NORMED 算法，则最大值即为相似度的值
    print('匹配相似度：', max_val)

    if (max_val < max):
        return None, 0, 0
    else:
        # 找到匹配位置的左上角和右下角坐标
        w, h = sml_img.shape[:2]
        top_left = max_loc
        bottom_right = (top_left[0] + h, top_left[1] + w)
        # 在大图上标记匹配位置
        cv2.rectangle(big_img, top_left, bottom_right, (255, 0, 0), 2)

        showpic(big_img)
        mid_x = top_left[0] + (bottom_right[0]-top_left[0])/2
        mid_y = top_left[1] + (bottom_right[1]-top_left[1])/2
        return big_img, mid_x, mid_y

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

    return threshold

if __name__ == '__main__' :
    # 示例用法
    template_path = '../asset/test2.png'  # 模板图像路径
    image_path = '../asset/test3.png'        # 待搜索的图像路径
    get_target_point(template_path, image_path, 0.5)