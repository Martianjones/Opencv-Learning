import cv2
import numpy as np
from setuptools.command.rotate import rotate

# 读取图片
src = cv2.imread('street.jpg')
rows,cols,channel = src.shape

# 函数参数
M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
rotated = cv2.warpAffine(src,M,(cols,rows))

# 显示图像
cv2.imshow('Original',src)
cv2.imshow('Rotated',rotated)

# 等待显示
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
