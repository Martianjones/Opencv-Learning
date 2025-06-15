import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dot.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 均值滤波
result1 = cv2.blur(source,(3,3))

# 方框滤波
result2 = cv2.boxFilter(source,-1,(3,3),normalize=1)

# 高斯滤波
result3 = cv2.GaussianBlur(source,(7,7),0)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

# 显示图形
titles = ['原始图像','均值滤波','方框滤波','高斯滤波']
images = [source,result1,result2,result3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()