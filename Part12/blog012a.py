import cv2
import numpy as np

img = cv2.imread('cat.jpg')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
height,width = img.shape[:2]
result = np.zeros((height,width),np.uint8)

for i in range(height):
    for j in range(width):
        if(int(grayImage[i,j]+50)>255):
            gray = 255
        else:
            gray = int(grayImage[i,j]+50)
        result[i,j] = np.uint8(gray)

# 显示图像
cv2.imshow('GrayImage',grayImage)
cv2.imshow('Result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()