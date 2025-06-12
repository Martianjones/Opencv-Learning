import cv2
import numpy as np

# 图像灰度非线性变换

img = cv2.imread('nightstreetscene.png')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
height,width = grayImage.shape[:2]
result = np.zeros((height,width),np.uint8)

# 图像灰度非线性变换：DB = DA*DA / 255
for i in range(height):
    for j in range(width):
        gray = int(grayImage[i,j])*int(grayImage[i,j]) / 255
        result[i,j] = np.uint8(gray)

cv2.imshow('Gray Image',grayImage)
cv2.imshow('Result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()