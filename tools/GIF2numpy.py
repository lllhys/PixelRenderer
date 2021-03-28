import cv2
import numpy as np
from renderer.color import *


def format_numpy_matrix(matrix):
    numpy_matrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype='uint32')
    # 数据格式转换
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            pixel = matrix[i][j]
            numpy_matrix[i][j] = get_opacity_color_from_list(pixel)
    # 格式化输出
    for i in range(0, matrix.shape[0]):
        line_str = "["
        if i == 0:
            line_str = line_str+'['
        for j in range(0, matrix.shape[1]):
            if j is 0:
                line_str = line_str + str(numpy_matrix[i][j])
            else:
                line_str = line_str + ', ' + str(numpy_matrix[i][j])
        line_str = line_str + ']'
        if i is not matrix.shape[0] - 1:
            line_str = line_str + ', '
        else:
            line_str = line_str + '] '
        print(line_str)


def pic2numpy(picture):
    img = cv2.imread(picture)
    print('numpy.array(')
    format_numpy_matrix(img)
    print(", dtype='uint32')")


def gif2numpy(video):
    print('numpy.array([')
    cap = cv2.VideoCapture(video)  # 打开视频
    while cap.isOpened():
        ret, frame = cap.read()  # 读取视频返回视频是否结束的bool值和每一帧的图像
        if not ret:
            break
        format_numpy_matrix(frame)
        print(',')
    print("], dtype='uint32')")


if __name__ == '__main__':
    gif2numpy("../static/wake.gif")
