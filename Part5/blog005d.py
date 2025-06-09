import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
src = cv2.imread('lena.jpg')

# 图像类型转换
imgRGB = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
imgHsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
imgYCrCb = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
imgHLS = cv2.cvtColor(src,cv2.COLOR_BGR2HLS)
imgXYZ = cv2.cvtColor(src,cv2.COLOR_BGR2XYZ)
imgLAB = cv2.cvtColor(src,cv2.COLOR_BGR2LAB)
imgYUV = cv2.cvtColor(src,cv2.COLOR_BGR2YUV)

# 调用matplotlib显示处理结果
titles = ['BGR','RGB','GRAY','HSV','YCrCb','HLS','XYZ','LAB','YUV']
images = [src,imgRGB,imgGray,imgHsv,imgYCrCb,imgHLS,imgXYZ,imgLAB,imgYUV]
for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


