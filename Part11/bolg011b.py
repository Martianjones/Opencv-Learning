import cv2
import numpy as np

# 平均灰度处理方法

img = cv2.imread('mountain.png')
height,width =img.shape[:2]
grayimg = np.zeros((height,width,3),np.uint8)
grayImg = np.zeros((height,width,3),np.uint8)

# 图像平均灰度处理方法
for i in range(height):
    for j in range(width):
        # 灰度值为RGB 三个分量的平均值
        gray = (int(img[i,j][0])+int(img[i,j][1])+int(img[i,j][2]))/3
        grayI = 0.3 * img[i,j][0] + 0.59 * img[i,j][1]+ 0.11 * img[i,j][2]
        grayimg[i,j] = np.uint8(gray)
        grayImg[i,j] = np.uint8(grayI)

cv2.imshow('Source',img)
cv2.imshow('Gray',grayimg)
cv2.imshow('GrayImg',grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()