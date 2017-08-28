#!/usr/bin/python
# coding=utf-8


import numpy as np
import cv2

# 创建一块黑板
img = np.zeros((512, 512, 3), np.uint8)
# Draw Line
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# Drawing Rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 1)
# Drawing Circle
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
# Drawing Ellipse
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# Drawing Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'wangning', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

# 展示图片 (窗口名称,图片引用)
cv2.imshow('Hello', img)

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()  # Create a black image
