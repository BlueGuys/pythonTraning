#!/usr/bin/python
# coding=utf-8


import cv2
from matplotlib import pyplot

# 加载图片
# 转换为灰度图像
img = cv2.imread('./lzs.jpg')
print img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 移除noisy
img1 = cv2.GaussianBlur(gray, (3, 3), 0)

# 边缘检测
laplacian = cv2.Laplacian(img1, cv2.CV_64F)
sobelx = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=5)  # x
sobely = cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=5)  # y

pyplot.subplot(2, 2, 1), pyplot.imshow(img1, cmap='gray')
pyplot.title('Origin'), pyplot.xticks([]), pyplot.yticks([])
pyplot.subplot(2, 2, 2), pyplot.imshow(laplacian, cmap='gray')
pyplot.title('Laplacian'), pyplot.xticks([]), pyplot.yticks([])
pyplot.subplot(2, 2, 3), pyplot.imshow(sobelx, cmap='gray')
pyplot.title('Sobel X'), pyplot.xticks([]), pyplot.yticks([])
pyplot.subplot(2, 2, 4), pyplot.imshow(sobely, cmap='gray')
pyplot.title('Sobel Y'), pyplot.xticks([]), pyplot.yticks([])

pyplot.show()
