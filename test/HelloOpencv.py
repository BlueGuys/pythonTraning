#!/usr/bin/python
# coding=utf-8


import cv2


# 图像的读取
def read_image():
    # 读取图像获得图像引用
    img = cv2.imread('./a01.jpg')
    # 展示图片 (窗口名称,图片引用)
    cv2.imshow('Hello', img)
    print img.shape
    print img.size
    print img.dtype

    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


# read_image()


# 图像的保存
def save_image():
    # 读取图像获得图像引用
    img = cv2.imread('./a01.jpg', 0)
    # 保存图像(路径，引用)
    cv2.imwrite('./a02.jpg', img)
    # 第三个参数针对特定的格式：
    # 对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95。 注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int。下面是以不同质量存储的两幅图：
    cv2.imwrite('./a03.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
    # 对于PNG，第三个参数表示的是压缩级别。cv2.IMWRITE_PNG_COMPRESSION，从0到9,压缩级别越高，图像尺寸越小。默认级别为3：
    cv2.imwrite("./a04.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

# save_image()


# 读取摄像头
def read_capture():
    cap = cv2.VideoCapture(0)
    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # wait for ESC key to exit
            cv2.imwrite('./wangning.jpg', frame)
            cv2.destroyAllWindows()
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# read_capture()





