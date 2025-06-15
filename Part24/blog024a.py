import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('noisedot.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 中值滤波
result1 = cv2.medianBlur(source,3)

# 双边滤波
result2 = cv2.bilateralFilter(source,15,150,150)

# 显示图像
cv2.imshow('Source',source)
cv2.imshow('MedianBlur',result1)
cv2.imshow('BilateralFilter',result2)

cv2.waitKey(0)
cv2.destroyAllWindows()