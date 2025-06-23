import numpy as np
import cv2
import matplotlib.pyplot as plt


# 图像素描特效以及卡通特效
img = cv2.imread('cangyuantu.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#-----------------------------------
#   素描特效
#-----------------------------------
# 高斯滤波降噪
gaussian = cv2.GaussianBlur(gray,(5,5),0)

# Canny算子
canny= cv2.Canny(gaussian,50,150)

# 阈值化处理
ret,result1 = cv2.threshold(canny,100,255,cv2.THRESH_BINARY_INV)

#-----------------------------------
#   卡通特效
#-----------------------------------
# 定义双边滤波的数目
num_bilateral = 7

# 用高斯金字塔降低取样
img_color = img
for i in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color,d = 9,sigmaColor=9,sigmaSpace=7)
# 中值滤波处理
img_blur = cv2.medianBlur(gray,7)
# 边缘检测及自适应阈值化处理
img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)
# 转换回彩色图像
img_edge = cv2.cvtColor(img_edge,cv2.COLOR_BGR2RGB)

# 与运算
img_cartoon = cv2.bitwise_and(img_color,img_edge)

# 正常显示中文
plt.rcParams['font.sans-serif']=['SimHei']

# 显示图像
titles = ['原始图像','素描特效','卡通特效']
images = [img,result1,img_cartoon]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()