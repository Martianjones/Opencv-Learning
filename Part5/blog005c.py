import cv2
import numpy as np

# 读取图片
img = cv2.imread('landscape_1.png')

# 拆分通道
b,g,r = cv2.split(img)
# b = cv2.split(img)[0]
# g = cv2.split(img)[1]
# r = cv2.split(img)[2]

# 合并通道
m = cv2.merge([b,g,r])
cv2.imshow('Merge',m)

# 显示原始图像
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)

# 显示蓝色
rows,cols,chn = img.shape
g = np.zeros((rows,cols),dtype = img.dtype)
r = np.zeros((rows,cols),dtype=img.dtype)

test = cv2.merge([b,g,r])
cv2.imshow('BluePicture',test)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()