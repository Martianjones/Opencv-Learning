import cv2
import numpy as np
import matplotlib.pyplot as plt

# 基于均值漂移算法的图像分割

img = cv2.imread('people.jpg')
spatialRad = 50 #空间窗口大小
colorRad = 50   #色彩窗口大小
maxPyrLevel = 2 #金字塔层数

# 图像均值漂移分割
dst = cv2.pyrMeanShiftFiltering(img,spatialRad,colorRad,maxPyrLevel)

# 显示图像
cv2.imshow('Source',img)
cv2.imshow('Dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()