# -*-coding:utf8-*-#
"""
Created on Wed Feb 04 21:53:05 2015

@author: http://2hwp.com/
"""

import os
import cv2
from PIL import Image
import uuid


# detectFaces()返回图像中所有人脸的矩形坐标（矩形左上、右下顶点）
# 使用haar特征的级联分类器haarcascade_frontalface_default.xml，在haarcascades目录下还有其他的训练好的xml文件可供选择。
# 注：haarcascades目录下训练好的分类器必须以灰度图作为输入。
def detectFaces(image_name):
    img = cv2.imread(image_name)
    face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img  # if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)  # 1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    result = []
    for (x, y, width, height) in faces:
        result.append((x, y, x + width, y + height))
    return result


# 保存人脸图
def saveFaces(image_name):
    faces = detectFaces(image_name)
    if faces:
        # 将人脸保存在save_dir目录下。
        # Image模块：Image.open获取图像句柄，crop剪切图像(剪切的区域就是detectFaces返回的坐标)，save保存。
        # os.mkdir(save_dir)
        for (x1, y1, x2, y2) in faces:
            file_name = os.path.join('_faces', str(uuid.uuid1()) + ".jpg")
            Image.open(image_name).crop((x1, y1, x2, y2)).save(file_name)


def startCheck(path):
    list_dirs = os.walk(path)
    for root, dirs, files in list_dirs:
        for f in files:
            absolute_path = os.path.join(root, f)
            relative_path = absolute_path.replace('/Users/wangning/Code/github/pythonTraning/opencv', '.')
            if os.path.splitext(relative_path)[1] == '.jpg' or os.path.splitext(relative_path)[1] == '.JPG':
                saveFaces(relative_path)
                print(relative_path)


if __name__ == '__main__':
    startCheck('/Users/wangning/Code/github/pythonTraning/opencv/origin')
