import cv2
import ddddocr

class TEXT_TYPE():
    GOLD = 1
    SILVER = 2
    OTHER = 3

def get_num(img_path, type):
    if type == 1:
        xy_0 = (123, 180)
        xy_1 = (214, 218)

    img = cv2.imread(img_path)
    if img is None:
        print("识别图片有误！")
        return

    cropped = img[xy_0[1]:xy_1[1], xy_0[0]:xy_1[0],]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("temp1.png", cropped)

    ocr = ddddocr.DdddOcr(show_ad=False)
    with open('temp1.png', 'rb') as f:
        img_byte = f.read()

    res = ocr.classification(img_byte)
    return res


if __name__ == '__main__':
    get_num('../asset/test_login.png', TEXT_TYPE.GOLD)
