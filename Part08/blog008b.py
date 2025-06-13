import cv2
import numpy as np
import matplotlib.pyplot as plt

from Part8.blog008a import newImage

# 读入原始图像
img = cv2.imread('street.jpg')

# 获取图像高度和宽度
height = img.shape[0]
width = img.shape[1]

# 创建三幅图像，用于2、4、8级量化
newImage1 = np.zeros((height,width,3),np.uint8)
newImage2 = np.zeros((height,width,3),np.uint8)
newImage3 = np.zeros((height,width,3),np.uint8)

# 量化等级为2的量化处理
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i,j][k] < 128:
                gray = 0
            else:
                gray = 128
            newImage1[i,j][k] = np.uint8(gray)

# 量化等级为4的量化处理
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i,j][k] < 64:
                gray = 0
            elif img[i,j][k] < 128:
                gray = 64
            elif img[i,j][k] < 192:
                gray = 128
            else:
                gray = 192
            newImage2[i,j][k] = np.uint8(gray)

# 量化等级为8的量化处理
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i,j][k] < 32:
                gray = 0
            elif img[i,j][k] < 64:
                gray = 32
            elif img[i,j][k] < 96:
                gray = 64
            elif img[i,j][k] <128:
                gray = 96
            elif img[i,j][k] <160:
                gray = 128
            elif img[i,j][k] <192:
                gray = 160
            elif img[i,j][k] < 224:
                gray = 192
            else:
                gray = 224
            newImage3[i,j][k] = np.uint8(gray)

# 显示图片
cv2.imshow('Source',img)
cv2.imshow('level2',newImage1)
cv2.imshow('level4',newImage2)
cv2.imshow('level8',newImage3)

# 等待显示
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()