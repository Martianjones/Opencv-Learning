import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# 自适应阈值化处理
# 当同一幅图像上不同部分具有不同亮度时，需要采用自适应阈值化处理方法，根据图像上的每一个小区域，计算其对应的阈值
# 从而使得同一幅图像上的不同区域采用不同的阈值，在亮度不同的情况下得到更好的结果

img = cv2.imread('dog.jpg')

# 图像灰度化处理
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 固定值阈值化处理
r,thresh1 = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)

# 自适应阈值化处理 法一
thresh2 = cv2.adaptiveThreshold(grayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

# 自适应阈值化处理 法二
thresh3 = cv2.adaptiveThreshold(grayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# 设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

# 显示图像
titles = ['灰度图像','全局阈值','自适应平均阈值','自适应高斯阈值']
images = [grayImage,thresh1,thresh2,thresh3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
