import cv2
import numpy as np

# 读取图片
img = cv2.imread('minecraft.jpg')

# 图像各像素加100
m = np.ones(img.shape,dtype='uint8')*100

# Opencv 加法运算
result1 = cv2.add(img,m)

# Opencv 减法运算
result2 = cv2.subtract(img,m)

# 显示图像
cv2.imshow('original',img)
cv2.imshow('add result',result1)
cv2.imshow('subtract result',result2)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
