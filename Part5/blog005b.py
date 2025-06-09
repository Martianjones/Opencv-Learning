import cv2
import numpy as np

# 读取图片
img = cv2.imread('lena.jpg')
img1 = cv2.imread('landscape_1.png')
# 定义200*200矩阵
face = np.ones((200,200,3))

# 显示原始图像
cv2.imshow('Demo',img)

# 显示ROI区域
face = img[50:250,50:250]
cv2.imshow('face',face)
img1[50:225,50:225] = face
cv2.imshow('landscape',img1)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
1、shape
通过shape关键字获取图像的形状，返回包含行数、列数、通道数的元组。其中灰度图像返回行数和列数，彩色图像返回行数、列数和通道数。
2、size
通过size关键字获取图像的像素数目，其中灰度图像返回行数×列数，彩色图像返回行数×列数×通道数。
3、dtype
通过dtype关键字获取图像的数据类型，通常返回uint8
'''