import cv2
import numpy as np


# 图像特效之浮雕特效
img = cv2.imread('shanghai.jpg')

# 获取图像的高度和宽度
height,width = img.shape[:2]

# 图像灰度处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 创建目标图像
dstImage = np.zeros((height,width,1),np.uint8)

# 浮雕特效算法：
for i in range(0,height):
    for j in range(0,width-1):
        grayCurrentPixel = int(gray[i,j])
        grayNextPixel = int(gray[i,j+1])
        newPixel = grayCurrentPixel - grayNextPixel + 100
        if newPixel > 255:
            newPixel = 255
        if newPixel < 0:
            newPixel =0
        dstImage[i,j] = newPixel

# # 通过函数实现
# kernel = np.array([[-1,0,0],[0,1,0],[0,0,0]])
# dstImage = cv2.filter2D(img,-1,kernel)

# 显示图像
cv2.imshow('Source',img)
cv2.imshow('Destination',dstImage)
cv2.waitKey(0)
cv2.destroyAllWindows()